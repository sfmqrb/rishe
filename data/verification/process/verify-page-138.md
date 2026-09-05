# Verification process log — verify-page-138


## [2026-09-05T20:08:06.351Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 138 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-138.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-138.json. Write /home/sfmqrb/git/rishe/data/verification/page-138.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 138` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:07.836Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:08:08.542Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:08.556Z] TOOL RESULT

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


## [2026-09-05T20:08:08.800Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-138.txt"
}
```


### [2026-09-05T20:08:08.827Z] TOOL RESULT

```
1	=== PDF page 138 (book page 108) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Dînu, Děnu, Dayânu : law, right, judgment; judge  (refs BQT:916; KLN:399)
4	#1 (parent #0) [Aramaic] refs=BQT:916; KLN:399 | dîn : to rule ; medhînah : district of a governor, province
5	  #2 (parent #1) [Arabic] refs=BQT:916; FVQ:131 | dîn 2 : judgment ; yawm-ed-dîn : day of judgment ; dayn : debt | NOTE: FVQ:132 claims Arabic "dîn:religion" is borrowed from Iranian while "dîn:day of judgment" is borrowed from Aramaic and passed into Iranian languages. See root "Dheye".
6	    #3 (parent #2) [Persian] refs=FVA:148; MON:1597 | dîn 2 «دین ۲» : judgment day ; dayn «دین ۳» : debt | NOTE: See root "Dheye" for "dîn: religion".
7	  #4 (parent #1) [Arabic] refs=KLN:399 | madîneh : city ; tamaddon : civilization
8	    #5 (parent #4) [Persian] refs=MON; FVA:379 | madîneh «مدینه» : city | extra: مدنی ، مداین ، تمدّن ، متمدّن
9	  #6 (parent #1) [Hebrew] refs=KLN:399; BQT:916 | dîn : to judge ; dân : judge ; Dânî-ěl : God is my judge ☞Layh
10	    #7 (parent #6) [English] refs=None | Dan, Daniel
11	--- entry 1 ---
12	ROOT Dkm-tom -> redirect to Dekm
13	--- entry 2 ---
14	ROOT Dlgho -> redirect to Del
15	--- entry 3 ---
16	ROOT [Semitic] D.l.l : to hang down, languish  (refs KLN:419)
17	#1 (parent #0) [Arabic] refs=KLN:419 | dz.l.l, z.l.l : to be low, humble, poor
18	  #2 (parent #1) [Persian] refs=FVA:150 | zalîl «ذلیل» : weak, humiliated | extra: ذلالت ، ذلّت
19	#3 (parent #0) [Hebrew] refs=KLN:419 | delilah : thin, delicate, amorous
20	  #4 (parent #3) [Persian] refs=MON5:526 | Dalîleh «دلیله» : the mistress of Samson
21	  #5 (parent #3) [English] refs=KLN:419; WEB:480 | Delilah
22	--- entry 4 ---
23	ROOT Dnghu -> redirect to Dinghw
24	--- entry 5 ---
25	ROOT Do 1 -> redirect to De 2
26	
```


## [2026-09-05T20:08:12.566Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-138.json",
 "description": "Read source JSON page 138"
}
```


### [2026-09-05T20:08:12.626Z] TOOL RESULT

```
{
  "pdf_page": 138,
  "book_page": 108,
  "entries": [
    {
      "root": {
        "name": "Dînu, Děnu, Dayânu",
        "lang": "Akkadian",
        "refs": "BQT:916; KLN:399",
        "gloss": "law, right, judgment; judge"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "BQT:916; KLN:399",
          "words": [
            {"translit": "dîn", "gloss": "to rule", "script": null},
            {"translit": "medhînah", "gloss": "district of a governor, province", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "BQT:916; FVQ:131",
          "words": [
            {"translit": "dîn 2", "gloss": "judgment", "script": null},
            {"translit": "yawm-ed-dîn", "gloss": "day of judgment", "script": null},
            {"translit": "dayn", "gloss": "debt", "script": null}
          ],
          "note": "FVQ:132 claims Arabic \"dîn:religion\" is borrowed from Iranian while \"dîn:day of judgment\" is borrowed from Aramaic and passed into Iranian languages. See root \"Dheye\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FVA:148; MON:1597",
          "words": [
            {"translit": "dîn 2", "gloss": "judgment day", "script": "دین ۲"},
            {"translit": "dayn", "gloss": "debt", "script": "دین ۳"}
          ],
          "note": "See root \"Dheye\" for \"dîn: religion\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Arabic",
          "refs": "KLN:399",
          "words": [
            {"translit": "madîneh", "gloss": "city", "script": null},
            {"translit": "tamaddon", "gloss": "civilization", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON; FVA:379",
          "words": [
            {"translit": "madîneh", "gloss": "city", "script": "مدینه"}
          ],
          "script_extra": "مدنی ، مداین ، تمدّن ، متمدّن",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Hebrew",
          "refs": "KLN:399; BQT:916",
          "words": [
            {"translit": "dîn", "gloss": "to judge", "script": null},
            {"translit": "dân", "gloss": "judge", "script": null},
            {"translit": "Dânî-ěl", "gloss": "God is my judge", "script": null, "see": ["Layh"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Dan, Daniel", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dkm-tom",
        "redirect": "Dekm"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dlgho",
        "redirect": "Del"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "D.l.l",
        "lang": "Semitic",
        "refs": "KLN:419",
        "gloss": "to hang down, languish"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:419",
          "words": [
            {"translit": "dz.l.l, z.l.l", "gloss": "to be low, humble, poor", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:150",
          "words": [
            {"translit": "zalîl", "gloss": "weak, humiliated", "script": "ذلیل"}
          ],
          "script_extra": "ذلالت ، ذلّت",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:419",
          "words": [
            {"translit": "delilah", "gloss": "thin, delicate, amorous", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON5:526",
          "words": [
            {"translit": "Dalîleh", "gloss": "the mistress of Samson", "script": "دلیله"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:419; WEB:480",
          "words": [
            {"translit": "Delilah", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dnghu",
        "redirect": "Dinghw"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Do 1",
        "redirect": "De 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:08:12.854Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:08:12.908Z] TOOL RESULT

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


## [2026-09-05T20:08:21.692Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','KLN','FVQ','FVA','MON','WEB','AFA','AKD','PLA','AFM','TAD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900]); print()\n\""
}
```


## [2026-09-05T20:08:21.714Z] TOOL CALL #6: Bash

```json
{
 "command": "ls tools/ && sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-05T20:08:23.541Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword bold at line start; e

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.", "notes": "Built from djvu.xml."}

AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.", "notes": "39 citations; check that the 1st-ed. page is within a page or two of Nourai's."}

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
```


### [2026-09-05T20:08:23.587Z] TOOL RESULT

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


## [2026-09-05T20:08:29.340Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Daniel\" KLN_1966.txt | head -20; echo ---; grep -n \"Delilah\" KLN_1966.txt KLN_1971.txt | head -20; echo ---; grep -n \"medina\\|Medina\\|medīnāh\\|medhinah\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T20:08:29.433Z] TOOL RESULT

```
9104:Cooperia,  n.,  a  genus  of  plants  of  the  amaryllis family  (bot.)  —  ModL.,  named  after  Daniel Cooper,  an  English  botanist  of  the  19th  cent. For  the  ending  see  suff.  -ia. co-opt,  tr.  v.  —  L.  cooptare,  ‘to  choose,  elect’,  fr. co-  and  optare,  ‘to  wish,  desire,  require,  demand, choose’.  See  option  and  cp.  adopt, co-optation,  n.  —  L.  cooptatio,  gen.  -dnis,  fr. cooptdtus,  pp.  of  cooptare.  See  prec.  word  and -ion.
10290:Dan,  1)  masc.  PN.;  2)  in  the  Bible:  a)  son  of Jacob  and  Bilhah;  b)  the  tribe  descended  from him.  —  Heb.  Dan,  lit.  ‘he  who  judges',  rel.  to Heb.  din,  ‘to  judge',  Aram,  dun,  din,  Syr.  din, Ugar.  dn,  Akkad,  ddnu,  of  s.m.,  Heb.  and  Aram. din,  ‘judgment’,  dayydn,  Akkad,  dayanu,  ‘judge’, Aram.  midhindl>,  ‘district,  province’  (whence Heb.  medhindh,  Syr.  mldhittd,  of  s.m.,  Arab,  ma- dtnah,  ‘city’),  orig.  ‘district  of  jurisdiction’,  Heb. madhin,  ‘strife,  contention’.  Cp.  Daniel,  Dinah. Cp.  also  Danaiis.
10325:Daniel,  masc.  PN.,  the  hero  of  the  Book  of  Da-
12751:El,  n.,  Hebrew  name  for  God.  —  Heb.  El,  ‘God’, of  uncertain  etymology;  possibly  related  to  el, ‘strong’  (cp.  e.g.  Gen.  31: 29  yesh  ESI  yadt,  ‘it is  in  my  power’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel.
14303:Fahrenheit,  n.,  a  type  of  thermometer.  —  Named after  the  inventor  of  the  mercurial  thermometer, the  German  physicist  Gabriel  Daniel  Fahrenheit (1686-1736).
21398:Leersia,  n.,  a  genus  of  grasses,  the  cut  grass  (bot.) —  ModL.,  named  after  the  German  botanist Johann  Daniel  Leers  (1727-74).  For  the  ending see  1st  suff.  -ia.
29156:Plesiosaurus,  n.,  a  genus  of  lizardlike  marine  rep¬ tiles  of  the  Mesozoic  (paleontol.)  —  ModL., coined  by  William  Daniel  Conybeare  (1787- 1857)  fr.  Gk.  TzXrjuioq,  ‘near’,  and  oaupop,  ‘liz¬ ard’.  The  first  element  is  rel.  to  niXou;,  ‘near’.
33560:named  after  the  American  veterinarian  Daniel Elmer  Salmon  (1850-1914).  For  the  ending  see sufif.  -ella.
34751:sestina,  n.,  a  verse  form  consisting  of  six  stanzas, invented  by  Arnaut  Daniel,  a  Provencal  trouba¬ dour  of  the  12th  cent.  —  It.,  fr.  sesto,  ‘sixth’.  See prec.  word.
35829:Solanaceae,  n.  pi.,  the  nightshade  family  (bot.)  — ModL.,  formed  fr.  Solanum  with  suff.  -aceae. solanaceous,  adj.  —  See  prec.  word  and  -aceous. solan dra,  n.,  a  shrub.  —  Named  after  the  Swedish botanist  Daniel  Solander  (1736-82). solan  goose.  —  Of  Scand.  origin.  Cp.  ON.  siilan, ‘the  gannet’,  fr.  siila,  ‘gannet’  (the  final  -n  repre¬ sents  the  def.  article).  Cp.  also  Norw.  sttla,  hav- sula,  ‘gannet’  (Hav-sula  lit.  means  ‘sea  gannet’, fr.  Norw.  hav,  fr.  ON.  haf  which  is  rel.  to  OE. hsef,  ‘sea’;  see  haff).
39247:tilasite,  n.,  a  magnesium  calcium  arsenate  (min¬ eral.)  —  Swed.  tilasit,  named  after  the  Swedish mining  engineer  Daniel  Tilas.  The  ending  -it goes  back  to  Gk.  -itrfi',  see  subst.  suff.  -ite. tilbury,  n.,  a  kind  of  two  -wheeled  carriage.  — Named  after  a  London  coach  builder,  who  first designed  it.
---
KLN_1971.txt:66947:Delilah, n., the mistress of Samson, who be- 
KLN_1966.txt:10723:Delilah,  n.,  the  mistress  of  Samson,  who  be¬ trayed  Samson  (Judges,  chapter  16).  —  Heb. Dllildh,  lit.  ‘delicate,  languishing,  amorous’, from  the  base  of  d-l-l,  ‘to  hang  down,  to  lan¬ guish’,  whence  also  dal,  ‘low,  poor,  thin’,  dalldh, ‘hair;  thrum’  (lit.  ‘that  which  hangs  down’); rel.  to  Akkad,  da/alu,  ‘to  be  weak  or  humble", Arab,  da! la,  ‘he  was  low  or  pliant’,  tadaldala, ‘it  hung  down,  dandled’,  Ethiop.  dated,  ‘hang¬ ing  curls’.
---
```


## [2026-09-05T20:08:30.180Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==212' KLN_1966.txt | head -80"
}
```


### [2026-09-05T20:08:31.806Z] TOOL RESULT

```
e’;  see  cube  and -ism.  The  word  cubisme  was  coined  by  the French  art  critic  Louis  Vauxcelles  on  the  basis of  a  remark  made  by  the  French  painter  Henri Matisse  (1869-1954)  before  a  landscape  ex¬ hibited  by  Georges  Braque  (1882-1963)  in  the Autumn  Salon  of  1908.  On  that  occasion  Ma¬ tisse  spoke  of  the  ‘small  cubes’  (petits  cubes) characterizing  the  painting  of  Braque.  This  re¬ mark  induced  Vauxcelles  to  form  the  word cubisme.
cubist,  n.,  an  adherent  of  cubism.  —  F.  cubiste, fr.  cube,  ‘cube’.  See  prec.  word  and  -ist. Derivative:  cubist,  adj.
cubit,  n.  —  L.  cubitum  (also  cubitus),  ‘elbow’,  fr. I.-E.  base  *qeu-b-,  ‘to  bend,  curve’,  whence  also cubare,  ‘to  lie  down'.  See  cubicle  and  cp.  cubitus. Cp.  also  codille.
cubital,  adj.,  pertaining  to  the  cubitus  or  cubit.  — L.  cubitalis,  fr.  cubitum  (cubitus).  See  cubit  and adj.  suff.  -al.
cubitus,  n.,  the  ulna  ( anat .)  —  L.  ‘elbow’.  See cubit.
cuboid,  adj.,  resembling  a  cube  in  shape.  —  Gk. xupoEid/jc,  ‘like  a  cube,  cubical’,  compounded of  xu(3o?,  ‘cube’,  and  -oEtSfjt;,  ‘like’,  fr.  eZ8o?, ‘form,  shape’.  See  cube  and  -oid.
Derivative:  cuboid,  n.
cuckold,  n.,  the  husband  of  an  unfaithful  wife.  — ME.  cocold,  kokewold,  kokeweld,  fr.  OF.  cucu- ault,  ‘cuckold’,  a  hybrid  coined  fr.  OF.  cocu (whence  F.  coucou),  ‘cuckoo’,  and  -ault,  -ah, a  suff.  of  Teut.  origin.  See  next  word.  OF.  cocu unites  the  senses  of  ‘cuckoo’  and  ‘cuckold’.  The sense  development  of  OF.  cocu,  cucuault,  ‘finds its  explanation  in  the  fact  that  the  female  of  the cuckoo  never  remains  with  the  same  male  for a  longer  time.  Modern  French  distinguishes  be¬ tween  coucou,  ‘cuckoo’,  and  cocu,  ‘cuckold’. Derivatives:  cuckold,  tr.  v.,  cuckold-ry,  n.
cuckoo,  n.  —  F.  coucou,  fr.  OF.  cocu,  a  word imitative  of  the  bird’s  cry.  Cp.  Gk.  x6xxo!;,  L. cuculus,  ‘cuckoo’,  OI.  kokilah,  ‘the  Indian  cuck¬ oo’,  kdkah,  ‘goose’,  Mir.  cuach,W.  cog,  ‘cuckoo’, which  all  are  of  imitative  origin.  Cp.  cuckold, coccyx,  koel.  Cp.  also  cock.
cuculiform,  adj.,  resembling,  or  pertaining  to, the  cuckoos.  —  Compounded  of  L.  cuculus, ‘cuckoo’,  and  forma,  ‘form,  shape’.  See  cuckoo and  form,  n,
cucullaris,  n.,  the  trapezius  muscle  (anat.)  — Medical  L.  cucullaris,  lit.  ‘resembling  a  cap’,  fr. L.  cucullus,  ‘cap,  hood’.  See  cowl  and  cp. next  word.
cucullate,  cucullated,  adj.,  hooded ;  hood-shaped (bot.  and  zool.)  —  Late  L.  cucullate,  ‘hooded’, pp.  of  cuculldre,  ‘to  cover  with  a  hood’,  fr.  L. cuculle,  ‘cap,  hood’.  See  cowl  and  cp.  prec. word.
Derivative:  cucullate-ly,  adv.
cuculliform,  adj.,  hood-shaped.  —  Compounded
of  L.  cucullus,  ‘cap,  hood’,  and  forma,  ‘form, shape’.  See  cowl  and  form,  n. cuculoid,  adj.,  resembling,  or  pertaining,  to  the cuckoos.  —  A  hybrid  coined  fr.  L.  cuculus, ‘cuckoo’,  and  Gk.  -ost8?)?,  ‘like’,  fr.  elSo?, ‘form,  shape’.  See  cuckoo  and  -oid.  The  correct form  is  cuculiform,  in  which  both  elements  are of  Latin  origin.
cucumber,  n.  —  ME.  cucumer,  fr.  OF.  cocombre, cucombre  (F.  concombre),  fr.  OProven?.  cogom- bre,  fr.  L.  cucumerem,  acc.  of  cucumis,  ‘cucum¬ ber’,  fr.  Gk.  xuxuop,  assimilated  fr.  alxuo?, ‘cucumber’,  a  collateral  form  of  atxur),  of  s.m., which  was  prob.  formed  through  metathesis  fr. Heb.  qishshu'd'1,  ‘cucumber’.  See  Sicyos  and cp.  It.  cocomero,  Sp.  cohombro.  Port,  cogombro, which  also  derive  fr.  L.  cucumerem.  Cp.  also Cucumis.
cucumiform,  adj.,  having  the  form  of  a  cucum¬ ber.  —  Compounded  of  L.  cucumis,  ‘cucumber’, and  forma,  ‘form,  shape’.  See  cucumber  and form,  n.
Cucumis,  n.,  a  genus  of  plants  of  the  cucumber family  (bot.)  —  L.,  ‘cucumber’.  See  cucumber, cucurbit,  n.,  1)  a  gourd ;  2)  a  gourd-shaped  flask.  —
F.  cucurbite,  fr.  L.  cucurbita,  ‘a  gourd’,  which is  cogn.  with  OI.  carbhafah,  ‘gourd’.  The  re¬ duplication  in  L.  cu-cur-bita  is  prob.  due  to  the influence  of  L.  cu-cu-mis,  ‘cucumber’.  Cp.  Rum. cucurbeta,  OProven?.  cogorda,  OF.  coorde (whence  F.  courge  and  gourde),  ‘gourd,  pump¬ kin’,  OE.  cyrfet,  OHG.  kurbij,  MHG.  kiirbij,
G.  Kiirbis),  ‘gourd’,  which  all  derive  from  L.  cu¬ curbita.  Cp.  gourd.
Cucurbita,  n.,  a  genus  of  vines  (bot.)  —  L., ‘gourd’.  See  prec.  word.
Cucurbitaceae,  n.  pi.,  a  family  of  vines  (bot.)  — Formed  fr.  Cucurbita  with  suff.  -aceae. cucurbitaceous,adj.  —  See  prec.  word  and  -aceous. cud,  n.  —  ME.,  fr.  OE.  cwidu,  cudu,  ‘mastic,  cud’, rel.  to  ME.  code,  ‘pitch’,  ON.  kvada,  ‘resin’, OHG.  quit i,  kuti ,  ‘glue’  (whence  MHG.  kiite, kiit,  G.  Kill,  ‘putty’),  and  cogn.  with  OI.  jatu-, lac,  gum’,  and  with  L.  bitumen  (an  Osco- Umbrian  dial,  word;  the  genuine  Latin  form would  have  been  *vetumen,  fr.  *gwetumen), ‘mineral  pitch’.  All  these  words  are  derivatives of  I.-E.  *gwet-,  *geut-,*gut-,  dental  enlargements of  base  *geu-,  ‘to  bend,  curve,  arch’.  See  cove, ‘a  small  bay’,  and  cp.  quid  for  chewing.  Cp.  also bitumen,  bowel,  guttural, cudbear,  n.,  a  dye  made  from  lichens.  —  Coined from  the  name  of  Cuthbert  Gordon  (in  1766) who  patented  this  dye.
cuddle,  tr.  and  intr.  v.  —  Prob.  formed  fr.  dial. cull,  coll,  ‘to  hug,  embrace’,  fr.  ME.  collen,  fr. OF.  coler,  ‘to  embrace’,  fr.  col,  ‘neck’,  fr.  L.  col- lum.  See  collar.
Derivatives:  cuddle,  n.,  cuddle-some,  cuddl-y, adjs.
cuddy,  n.,  a  donkey.  —  From  the  Scot,  name Cuddy,  dimin.  of  Cuthbert.
cuddy
cuddy,  n.,  a  cabin  in  a  ship.  —  Du.  kajuit ,  fr.  F. cahute,  ‘cabin’,  which  is  a  blend  of  cabane,  ‘hut, shanty,  cabin’,  and  hutte,  ‘hut’.  Cp.  G.  Kajiite, Dan.  kahyt,  Swed.  kajuta,  ‘cabin’,  which  all  are borrowed  fr.  F.  cahute ,  and  see  cabin  and  hut. cudgel,  n.  —  ME.  kuggel,  fr.  OE.  cycgel,  rel.  to MDu.  koghele,  ‘club  with  a  round  end’,  Du. kogel,  MHG.  kugele,  kugel,  G.  Kugel,  ‘ball, globe’,  OHG.  coccho,  ‘rounded  ship’,  MFIG. kiule,  kule ,  G.  Keule,  ‘club  with  a  round  end’, Swed.  kugge ,  Norw.  kug,  ‘cog’,  and  cogn.  with Lith.  guga,  ‘pommel  of  a  saddle,  hump,  hillock’, gaiigaras,  ‘summit’,  Russ,  guglja,  ‘tumor,  swell¬ ing’.  Cp.  cog,  ‘tooth  on  a  wheel’.
Derivatives :  cudgel,  tr.  v.,  cudgel(t)-er,  n. cue,  n.,  tail;  billiard  rod.  —  F.  queue,  ‘tail’,  fr. L.  coda,  of  s.m.  See  caudal  and  words  there referred  to  and  cp.  esp.  queue, cue,  n.,  direction  for  an  actor's  appearance.  — Prob.  name  of  the  letter  q,  used  as  the  abbrevia¬ tion  of  L.  q uando,  ‘when  (the  actor  has  to  come in)’.
cueist,  n.,  a  billiard  player  (slang).  — -  A  hybrid coined  fr.  cue,  ‘tail;  billiard  rod’,  a  word  of Latin  origin,  and  suff.  -ist  (fr.  Gk.  -urn)f). cuesta,  n.,  a  hill,  slope  (Southwestern  U.S.A.)  — Sp.,  fr.  L.  costa,  ‘rib,  side’.  See  coast, cuff,  n.,  the  lower  part  of  the  sleeve.  —  ME.  cuff'e, coffe,  ‘glove,  mitten’,  of  uncertain  origin;  not related  to  coif.
Derivatives :  cuff,  tr.  v.,  to  put  cuffs  on,  cuff-er,  n. cuff,  tr.  v.,  to  strike.  —  ME.,  prob.  fr.  ME.  cuffe, ‘glove’,  and  orig.  meaning  ‘to  strike  with  a glove’.  See  cuff,  n.
cuirass,  n.,  armor  protecting  the  breast  and  back. —  F.  cuirasse,  orig.  ‘a  leather  breastplate’,  fr. cuir,  ‘hide,  leather’,  fr.  L.  corium.  Cp.  It.  coraz- za,  OProven?.  coirassa,  cuirassa,  Sp.  coraza. Port,  couraga,  ‘cuirass’,  and  see  corium. Derivatives:  cuirass,  tr.  v.,  cuirass-ed,  adj. cuirassier,  n.,  a  soldier  wearing  a  cuirass.  —  F., formed  with  suff.  -ier  fr.  cuirasse.  See  prec.  word, cuisine,  n.,  the  kitchen;  style  of  cooking.  —  F., ‘kitchen’,  fr.  Late  L.  cocina,  a  var.  of  coquina, ‘kitchen’,  fr.  coquere,  ‘to  cook’.  See  cook  and cp.  kitchen.
cuisse,  cuish,  n..  usually  in  the  pi.,  armor  for  pro¬ tecting  the  thigh.  —  ME.  cuissues,  fr.  OF.  cuis- seaux,  pi.  of  cuissel,  fr.  cuisse,  ‘thigh’,  fr.  L. coxa,  ‘hip’,  whence  also  It.  coscia,  ‘thigh’,  Rum. coapsa,  ‘hip,  thigh’,  O Proven?,  coissa,  cueisa, ‘thigh',  Catal.  cuxa,  OSp.,  Port,  coxa,  of  s.m. See  coxa  and  cp.  cushion.
-ciila,  L.  fern,  dimin.  suff..  corresponding  to masc.  -cuius,  neut.  -culum.  —  Sec  -cule. cul-de-sac,  n.,  a  blind  alley.  —  F.,  lit.  ‘bottom of  a  bag’.  For  the  etymology  of  F.  cut  see  culet. F.  de,  ‘of,  from",  derives  fr.  L.  de,  ‘from,  away from’ ;  see  de-.  For  the  origin  of  F.  sac  see  sac. -cule,  dimin.  subst.  suff.  —  F.  -cule,  fr.  L.  -cuius (masc.),  -cula  (fern.),  or  -culum  (neut.)  Cp.  -cle. culet,  n.,  i)  the  facet  forming  the  bottom  of  a
382
brilliant;  2)  armor  covering  the  hinder  part  of the  body.  —  F.,  dimin.  of  cul,  ‘backside,  poste¬ rior,  bottom’,  fr.  L.  cuius,  ‘posterior,  fundament’, which  is  cogn.  with  OIr.  cul,  W.  cil,  ‘back’.  Cp. culot,  culotte,  bascule,  recoil  and  the  first  ele¬ ment  in  cul-de-sac.  For  the  ending  see  suff.  -et. Culex,  n.,  a  genus  of  mosquitoes.  —  L.  culex, ‘gnat’,  cogn.  with  OIr.  cuil  (for  *ku-li)  ‘gnat’, W.  cylionen,  ‘gnat,  fly’,  Co.  kelionen,  ‘fly’  and prob.  also  with  OI.  sula-,  ‘spear,  spit’.  These words  possibly  derive  fr.  I.-E.  *kul-,  enlargement of  base  *kd-,  ‘pointed’,  whence  also  L.  caucus, ‘wedge’.  See  coin.
culici-,  combining  form  meaning  ‘gnat’.  —  L., stem  of  culex,  gen.  culicis,  ‘gnat’.  See  Culex. Culicidae,  n.  pi.,  a  family  of  insects,  the  mos¬ quitoes  ( entomol .)  —  ModL.,  formed  with  suff. -idae  fr.  L.  culex,  gen.  culicis,  ‘gnat’.  See  Culex. culinary,  adj.,  pertaining  to  the  kitchen;  fit  for cooking  —  L.  culinarius,  ‘pertaining  to  the  kit¬ chen’,  fr.  culina,  ‘kitchen’,  which  is  rel.  to  co¬ quere,  ‘to  cook’.  For  the  suff.  -ina  in  culina  cp. Late  L.  coquina,  ‘kitchen’,  dial.  L .popina,  ‘cook- shop,  eating-house’.  See  cook  and  adj.  suff.  -ary and  cp.  cuisine.  Cp.  also  kiln.
cull,  tr.  v.,  to  select.  -  ME.  cullen,  fr.  OF.  cuillir, coillir  (F.  cueillir),  ‘to  collect,  gather,  pluck’,  fr. L.  colligere,  ‘to  collect’.  See  collect  and  cp.  coil, ‘to  wind’.
Derivatives:  cull,  n.,  cull-age,  n.,  cull-er,  n., cull-ing,  n.
cullender,  n.  —  A  var.  of  colander, cullet,  n.,  broken  or  refuse  glass.  —  F.  collet,  ‘a little  neck’  (see  collet);  so  called  in  allusion  to the  small  pieces  of  glass  at  the  neck  of  the  bottle detached  in  blowing  the  glass, cullion,  n.,  a  base  fellow.  —  The  original  meaning is  ‘testicle’,  fr.  couillon,  ‘testicle;  base  fellow’, fr.  VL.  *colednem,  acc.  of  *coleo,  fr.  L.  coleus, ‘testicles’,  lit.  ‘straining  bag',  which  prob.  de¬ rives  fr.  colum,  ‘strainer,  colander’,  and  lit. means  ‘that  which  pertains  to  the  strainer’.  See colander  and  cp.  cullis.
cullis,  n.,  a  strong  broth  of  meat.  —  OF.  colels, couleis  (F.  coulis),  fr.  VL.  *cdldticius,  ‘that  which pertains  to  straining’,  fr.  L.  colare,  ‘to  strain’. See  colander  and  cp.  coulisse,  cullion. cully,  n.
```


## [2026-09-05T20:08:38.003Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['Dan,  1)  masc.','Delilah,  n.,  the  mistress','Daniel,  masc.  PN.']:\n    i=t.find(pat)\n    leaf=t.count('\\f',0,i)\n    print(pat[:20],'leaf',leaf)\nEOF"
}
```


## [2026-09-05T20:08:38.707Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==222' KLN_1966.txt | grep -n \"Daniel\" "
}
```


### [2026-09-05T20:08:39.792Z] TOOL RESULT

```
Dan,  1)  masc. leaf 220
Delilah,  n.,  the   leaf 231
Daniel,  masc.  PN. leaf 221
```


### [2026-09-05T20:08:41.619Z] TOOL RESULT

```
11:Daniel,  masc.  PN.,  the  hero  of  the  Book  of  Da-
```


## [2026-09-05T20:08:51.226Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== leaf 221 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==222' KLN_1966.txt | sed -n '1,20p'; echo; echo \"=== leaf 221 page nums ===\"; awk 'BEGIN{RS=\"\\f\"} NR==222' KLN_1966.txt | grep -nE '^[0-9]{3}$'; echo \"=== leaf 231 pagenums ===\"; awk 'BEGIN{RS=\"\\f\"} NR==232' KLN_1966.txt | grep -nE '^[0-9]{3}$'"
}
```


## [2026-09-05T20:08:52.368Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"din,  ‘religion\\|Dinah\\|dayydn\\|madtnah\\|maditiah\" KLN_1966.txt | head; echo ---; grep -n \"^Medina\\|Medina,\" KLN_1966.txt | head"
}
```


### [2026-09-05T20:08:53.072Z] TOOL RESULT

```
=== leaf 221 ===
��.
Derivative:  dandruff-y,  adj. dandy,  n.,  a  fop.  —  Fr.  Dandy,  a  var.  of  St.  An¬ drews.  The  name  Andrews  ult.  derives  fr.  the Greek  PN.  ’AvSpeag,  which  is  rel.  to  avSpetog, ‘manly’,  both  being  derivatives  of  avfjp,  gen. dvSpoi;,  ‘man’.  See  andro-.
Derivatives:  dandy,  adj.,  and  the  hybrids  dandy¬ ish,  adj.,  dandy-ism,  n.
dandy,  dandi,  n.,  1)  a  boatman;  2)  a  hammock (Anglo-hid.)  —  Hind,  dandi,  dandi,  fr.  dand, dand,  ‘staff,  stick,  wand,  oar’,  fr.  OI.  dariddlt, of  s.m.,  which  is  of  uncertain  etymology, dandy,  dandi,  n.,  a  Sivaitic  mendicant.  —  Of  the same  origin  as  prec.  word ;  so  called  from  the small  wand  carried  by  him, dandy,  n.  —  Corruption  of  dengue.
Dane,  n.,  a  native  of  Denmark.  —  ME.  Dan,  fr. ON.  Danir  (pi.),  lit.  ‘Lowlanders’,  which  is  rel. to  MLG.  denne,  ‘lowland,  wooded  vale,  den’, OE.  denn,  ‘lair  of  a  wild  beast,  den’.  See  den. For  sense  development  cp.  Pole.
Derivatives:  Dan-ish,  adj.  and  n.
Danegeld,  n.,  an  annual  land  tax  ( English  hist.)  — ME.,  lit.  ‘tribute  paid  to  the  Danes’,  fr.  Dane, gen.  pi.  of  Dan,  ‘Dane’,  and  geld,  ‘payment,  tri¬ bute’,  fr.  OE.  gield,  of  s.m.  See  Dane  and  yield. Danelaw,  also  Danelagh,  n.,  Danish  law  prevail¬ ing  in  the  northeastern  part  of  England  held by  the  Danes  during  the  Danish  Conquest.  — OE.  Dena  lagu,  ‘Danes’  law’.  See  Dane  and  law. danger,  n.  ME.  danger,  ‘power,  difficulty,  re¬ sistance,  jurisdiction’,  fr.  OF.  danger,  ‘power, domination’  (whence  F.  danger,  ‘danger’),  fr. VL.  *dominidrium,  ‘power’,  which  derives  fr. do  minus,  ‘master,  lord’.  The  change  of  L.  o  to  a in  OF.  danger  is  due  to  the  influence  of  L.  dam¬ num,  ‘damage’.  See  dominate  and  dome,  ‘build¬ ing’,  and  cp.  dominion,  dungeon.
Derivatives:  danger-ous,  adj.,  danger-ous-ly, adv.,  danger-ous-ness,  n.
dangle,  intr.  v.,  to  hang  loosely.  —  Of  Scand.  ori¬ gin.  Cp.  Dan.  dangle,  Swed.  dangla,  ‘to  swing about,  dangle’,  which  stand  in  gradational  re¬ lationship  to  Dan  dingle,  Swed.  and  Norw. dingla,  of  s.m.  Cp.  also  adangle.
Derivatives:  dangle,  n.,  dangl-er,  n.,  dangl-ing, adj.,  dangl-ing-ly,  adv.
Daniel,  masc.  PN.,  the  hero  of  the  Book  of  Da-
401
niel  (Bible).  —  Heb.  Ddni'il,  lit.  ‘God  is  my judge’,  rel.  to  Akkad.  Ddnilu.  For  the  first  ele¬ ment  see  Dan,  PN.,  for  the  second  see  El. dank,  adj.,  moist,  damp.  —  ME.  danke,  of  Scand. origin;  cp.  Swed.  dank,  ‘moist  place’,  ddnka, ‘to  moisten’,  which  are  rel.  to  OS.  dunkar, OFris.  diunk,  ‘dark’,  ON.  dokkr,  Du.  donker, OHG.  tunkal ,  dunkal,  MHG.  tunkel,  G.  dunkel, of  s.m.,  and  to  OHG.,  MHG.  damph,  MDu., Du.  damp,  ‘vapbr’.  See  damp.
Derivatives:  dank-ish,  adj.,  dank-ish-ness,  n., dank-ly,  adv.,  dank-ness,  n. danseuse,  n.,  a  femaledancer.  —  F.,  fern,  of  dan- seur,  ‘dancer’,  fr.  danser,  ‘to  dance’.  See  dance,  v. danta,  n.,  a  tapir.  —  Sp.  and  Port,  danta ,  ‘tapir’, fr.  Sp.  de  anta,  short  for  piel  de  anta,  ‘(of) buckskin’,  fr.  de,  ‘of,  from’,  and  anta,  ‘elk,  tapir, buckskin’,  fr.  Arab.  lamt,  ‘antelope’,  the  I  of which  was  mistaken  for  the  article  and  conse¬ quently  dropped.
Dantesque,  adj.,  resembling  Dante  or  his  style.  — Formed  with  suff.  -esque  from  the  name  of  the poet  Dante  (1265-1321).
Danthonia,  n.,  a  genus  of  plants,  the  wild  oat grass  (bot.)  —  ModL.,  named  after  the  French botanist  Ftienne  Danthoine.  For  the  ending  see suff.  -ia.
dap,  intr.  and  tr.  v„  to  fish  by  allowing  the  bait to  dip  into  the  water.  —  Prob.  of  imitative  ori¬ gin.  Cp.  dab,  ‘to  strike  gently’.
Derivative:  dap,  n.
Daphne,  n.,  a  nymph  (who  was  turned  into  a laurel)  (Greek  mythol.)  —  L.,  fr.  Gk.  Aacpwj,  fr. SAcpvr),  ‘laurel’.  See  next  word  and  cp.  Daphnis. Daphne,  n.,  a  genus  of  plants  of  the  mezereon family  (bot.)  — Gk.  Sdhpw),  ‘laurel’,  rel.  to  Per- gamene  Xatpvr),  Thessalian  Soiuyvcc,  of  s.m. ;  bor¬ rowed — together  with  L.  laurus,  ‘laurel’ — from a  language  of  Asia  Minor.  Cp.  prec.  word  and laurel.  Cp.  also  Daucus.
Daphnean,  adj.,  pertaining  to  Daphne.  —  Formed fr.  Daphne  with  suff.  -an.

=== leaf 221 page nums ===
12:401
29:402
30:403
=== leaf 231 pagenums ===
21:420
22:421
```


### [2026-09-05T20:08:53.151Z] TOOL RESULT

```
10290:Dan,  1)  masc.  PN.;  2)  in  the  Bible:  a)  son  of Jacob  and  Bilhah;  b)  the  tribe  descended  from him.  —  Heb.  Dan,  lit.  ‘he  who  judges',  rel.  to Heb.  din,  ‘to  judge',  Aram,  dun,  din,  Syr.  din, Ugar.  dn,  Akkad,  ddnu,  of  s.m.,  Heb.  and  Aram. din,  ‘judgment’,  dayydn,  Akkad,  dayanu,  ‘judge’, Aram.  midhindl>,  ‘district,  province’  (whence Heb.  medhindh,  Syr.  mldhittd,  of  s.m.,  Arab,  ma- dtnah,  ‘city’),  orig.  ‘district  of  jurisdiction’,  Heb. madhin,  ‘strife,  contention’.  Cp.  Daniel,  Dinah. Cp.  also  Danaiis.
11460:Dinah,  fern.  PN.;  in  the  Bible,  Jacob’s  daughter by  Leah.  —  Heb.  Dindh,  lit.  ‘judgment’,  fr.  din, ‘to  judge’.  See  Dan,  PN.
---
```


## [2026-09-05T20:09:26.944Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nb=d['BQT']\nfor k,v in b.items(): print(k,':',str(v)[:600]); print()\n\""
}
```


## [2026-09-05T20:09:28.360Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1,40p' FVQ_pages.txt | head -5; echo \"=== FVQ din ===\"; grep -n \"dîn\\|dīn\\|din (\\|Din (\" FVQ_pages.txt | head -30"
}
```


### [2026-09-05T20:09:28.658Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)

kind : archive_djvu+local_scan_ocr

url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1

lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh

local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/

page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (

covers_etymology : True

notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text file

scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmq

cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


### [2026-09-05T20:09:28.711Z] TOOL RESULT

```
LIJ< OU 158174 >m
> - ;0 73
^ COGAEKWAD*8 ^ORIENTAL SERIES
Published unde* the Authority of
the Government of His Highness
=== FVQ din ===
```


## [2026-09-05T20:09:32.387Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 149 150; do echo \"=== FVQ leaf $((n-1)) (printed p.$((n-1-17))) ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' FVQ_pages.txt; done"
}
```


### [2026-09-05T20:09:33.854Z] TOOL RESULT

```
=== FVQ leaf 148 (printed p.131) ===
FOREIGN VOCABULARY OF THE QUR 5 AN 131
, ^r
They are not very happy over the form, however, for ,*- 1) is fern.
and we should expect 451^0 not v5u^ Exactly the same form, how-
ever, is found in a verse of Khidash b. Zuhair
D ^ ^ .**
IsUo Lfc 4J li^rLs I'lji j*.^ ^U 1C!
" There came to us 'Amir desiring entertainment from us, so we
filled for him a full cup."
so Sibawaih suggested that it should be taken not as an adj. to u-uD
but as a verbal noun. 1
There is ground, however, for thinking that the word is not Arabic
at all. 2 Fraenkel, Fremdw, 282, would relate it to plTl, which we
find in Heb. pHR to crowd, oppress, thrust ; Aram. pPPT ; Syr. %!>
to crowd, squeeze, which is the Ar. T*pO to drive away, expel. The
change of PI to H he would explain as Mesopotamia!!. Thus
would mean " a cup pressed out", referring to the wine pressed to
fill the cup.
Of very frequent occurrence. Of. i, 3 ; ii, 257, etc.
Judgment, Religion, and in ix, 29, verbally " to make profession
of faith ".
fj- ^
In the Qur'an we find also o a debt, that which one owes
*> ^
(cf. iv, 12, 13 ; ii, 282), and i JL for one who receives payment of a
X 1
debt (xxxvii, 51 ; Ivi, 85), besides the verb ^ ]JS " to become debtors
to one another " (ii, 282). These, however, are later developments of
the word within Arabic.
The Muslim authorities usually treat it as an Arabic word (cf.
1 Vide LA, xi, 395, 396.
2 Horovitz, Parodies, 11, says : '* Auch die Herkunft von jUj . . ist unsicher."
=== FVQ leaf 149 (printed p.132) ===
132 FOREIGN VOCABULARY OP THE QUR^AN
Raghib, Mufradat, 175), and derive it from jlS " to do a thing as a
habit", but this verb seems to be denominative from <jO in the
sense of obedience, which, like Al^Ju and jlS (i.e. lAl^jSo and
|uj), is a borrowing from the North, connected with Akk. danu,
Heb. fH ; Syr. tO>. There was a suspicion among the philologers,
however, that it was a foreign word, for LA, xvii, 27, notes tttat some
authorities admitted that it had no verbal root, and al-Khafaji, 90, and
ath-Tha'alibi, Fiqh, 317, include it in their lists of foreign words.
As a matter of fact we have here two separate words of different
origin. 1 (i) In the sense of religion the word is a borrowing from Iranian.
In Phlv. we find jjy den meaning religion? from which come ^xyfo
dendk for religious law, ))0j" ^w-*^ of the same religion, 3 and
)W)0 dendn, used in the sense of "the religious 1 ', i.e. true
believers. This Phlv. j)O is derived from Av. *i)uj^ daena,
religion 4 (though this itself is probably derived from the Elamitish
den)* and besides being the origin of the Mod. Pers. JO, 6 was
borrowed into Arm. as ^te meaning religion, faith (and also law 7
in the sense of a "religious system", e.g. ijJA 1/^/^1% =
u)wo-u. >))($ the Mazdian religion or Law), (ii) In the sense of
Judgment it is a borrowing from the Aramaic. Thus we find in common
use the Rabbinic WH, Syr. U*?> and Mand. WH, all meaning
judgment and, indeed, the judgment of the last day. 8
From the Aramaic the word passed into S. Arabian lrfp| and
1 Noldeke in ZDMG, xxxvii, 534. See also Von Kremer, Mreifsilge, p. vii, and
Ahrens, Christliches, 28, 34.
2 PPGl, 110 ; 8&ya* 9 Glossary, 160, and the den of the Turfan Pahlavi ; Sale-
mann, Manichaische, Mudien, i, 67. For the borrowing (f. Noldeke-Schwally, i, 20 ;
Vollers, ZDMG, 1, 641 ; Noldeke, Mand. Gram, 102.
a Cf. the Av. Al)H)AlA G-^W' Weat ' Gl 8sar y> 35 '
Bartholomae, AI W, 662; Horn, Grundrixs, 133; cf. also the Pazend edlni
= irreligion.
* But see Bartholomac, AIW, 665, and Ziramern, Akkad. Fretndw, 24, who derives
it from Akk. de(i)nu. . .
Addai Sher, 69, discusses its meaning. Curiously enough it is given by the
Lexicons as a borrowing from Arabic, cf. Vullers, Lex, i, 956, but see Bartholomae,
AIW, 665.
7 Hubschmann, Arm. Gramm, i, 139.
Montgomery, Aramaic. Incantation Texts from Nippur, Glossary, p. 285,
8
```


## [2026-09-05T20:09:44.359Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 371 372 373 374 375 376; do echo \"=== leaf $n (est p.$((n+543))) ===\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -60; done 2>&1 | head -200"
}
```


### [2026-09-05T20:09:45.951Z] TOOL RESULT

```
=== leaf 371 (est p.914) ===
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
                                                     ‫ندارد ‪.‬‬

                                                                                                       ‫دیده بان باشد ‪.‬‬

 ‫مردن‪ :‬و فوت شدن باشد ‪ -‬وکنایه از دورشدن‬                             ‫دیده‌ور شدن ه کنابه از رسدن‬
                                    ‫‪.‬‬       ‫©‬        ‫هم هت‬           ‫بجیز هاباشد چنانکه هت ونظرالداختن چنانکه‬
 ‫دی مکافات ‪ -‬کتابه از دبیا عوالم‬                                                                                ‫باد ‪.‬‬
                                            ‫سفلی باشد ‪.‬‬              ‫كر ب=فتح اول بر وزن غير » معبد‬
      ‫‪-‬ابه از فلك است ‪.‬‬
                      ‫دير میناًکن‬                                    ‫رهبان راگوبندا ‪ -‬وبکر اول بمعنی دوراست‬
                                                                    ‫که اقيض ترديك باشد؟ و‪-‬مدت متمادیرا لیز‬
‫دار فك ‪ = ۱‬بر وزن ریوند ‪ .‬بمعنی‬
 ‫دبرباز است که دراز‪ - ,‬ومدت دراز ‪ -‬ودرازی‬
‫زمان باشد ‪ -‬وبمعتی دهر وزمان که دیا ومقدار‬                           ‫دير بار س بابای ابجد بروزن پیشوازه‬
 ‫ح ر کت فلك اعظمباشدهم آ مده ات‪ - ۸‬وصویذ‬                             ‫بمعنی درازاست که درمقابل کوتاه باشد ‪ -‬ودرازی‬
                         ‫بوازوبند را گیوزبند ‪.‬‬                                            ‫رمان ومدت را لیز گویند ‪۰‬‬


   ‫‪ = ۴‬دور » طبری ‪( ۲114‬دور) «ساب‬                          ‫‪( - ۱‬عی) ازسریالی «دائرةالمعارف اسلام» ‪.‬‬
  ‫‪ ۴‬س‪-‬منالی » سنگری » سرخه‌بی وشهمیرزادی ‪ ۳1‬دق ‪۲ .‬‬                                          ‫‪ :‬دور ‪.‬‬   ‫رك‬     ‫طدری ‪۱‬‬

                     ‫‪۰‬‬   ‫‪ :‬لسوم»‬   ‫«الابنيه‬          ‫گوارر»‬    ‫در‬    ‫مود‬   ‫شفه‬    ‫مت‬    ‫کوشت) جون‬     ‫‏‪ : ٩)۹٦‬دو(‬   ‫ص‬


  ‫‪ --‬همرشهة بهلوی‬                       ‫‪.‬‬       ‫دی‬   ‫رك‪:‬‬       ‫‪۵‬‬
                                                                                 ‫‪ _ ۴‬امر از « دیرزستن» ‪.‬‬
                                                                                    ‫« (عهد) طوبل» ‪ .‬رك‪:‬‬         ‫‪8‬‬
            ‫‪Henning, Two central Asian words . Hertford . 1946, p.‬‬                                                  ‫‪۰‬‬
            ‫چو نا بینا درو دوچشم مینا ‪۰‬‬                                ‫‪ - ۲‬شبی دبرند و ظلمت را مهیا‬
  ‫رود کی سمرفندی ‪«.‬لفت فر ‪۱۰۱٩‬‏ ‪.‬‬

         ‫چون توبی دید و بیند این ديرد ‪.‬‬                                     ‫‪ ۸‬بافتی تو بمال غره مشو‬
   ‫دخت فری ‪۱۰۱‬‬
             ‫رود کی سمرقندی‪ .‬ل‬

=== leaf 372 (est p.915) ===
 ‫‪n‬‬     ‫‪Sh‬‬                                                                                                  ‫دفر فف‬



                                         ‫وطعام فز قف ‪.‬‬           ‫رزننده ‪ ۰‬بمعنی‬
                                                                              ‫گبیرو‬
                                                                                  ‫ك‪= ۲ ۵‬‬
                                                                                       ‫دفير‬
                                                                   ‫دبرند است که مدت دراز و زمان عالم باشت ‪.‬‬
‫دز اشت‬        ‫بروزن رزه » يمى‬          ‫دازه =‬
  ‫و قلمه‌وحصار باشد ‪۷‬‬         ‫که رنگه ولون سیاءه ‪٩‬‏‬              ‫‪3‬فز = بکراول وسکون انی مجهول‬
‫واسب واستر وخربرا کیوزبند که از کل تا‬                            ‫و زای قطه دار (‪ » )۱‬رنگك و لون راگوند‬
‫‪-‬لاغ‬
   ‫دمش خط سیاهی کشیده شده باشد ‪٩‬‏ وا‬                             ‫عموماً چنانکه اسب سياه خرو پرویزرا شبدیز‬
‫مایل‬    ‫سبری‬    ‫و‬    ‫و چاروابی که رنگه آن سیاهی‬                  ‫‪ - ۴‬و رنگه سیاه را‬        ‫نیگه‬
                                                                                              ‫بندربعن‬
                                                                                                    ‫شگفت‬
                                                                                                       ‫می‬
                                                 ‫‪5‬‬               ‫کوبند خصوصاً ‪ -۴‬و رنگه خاکتری بیاهی‬
                                                                 ‫اسب و استر‬     ‫صوص‬
                                                                                  ‫مدخکه‬
                                                                                      ‫ان‬            ‫ه‬
                                                                                                    ‫تیز‬
                                                                                                      ‫گلفرا ن‬
                                                                                                            ‫ماب‬
‫دیس د با نانی مجهول بروزن کیس‪.‬‬                               ‫ادات دبگر که از کاکل تا‬   ‫وخر و بحییواز‬
‫همتاومانندوشییهو نظیرباشد‪- ۸‬وبهندی‌بمعنی روز‬                    ‫عنی‬ ‫م‪-‬‬‫ب‪۴‬‬ ‫وشد‬
                                                                           ‫دمش خطی سیاه کشیده شده با‬
‫است که بعربی بوم خوانند‪ -‬وملك وولامت رانیز‬                       ‫حصار وقلعه ‪ 7‬وجاست ‪ - ۴‬ونوعی ازدیگه‬
                                          ‫کوند ‪٩‬‏ ‪.‬‬              ‫ويال باشد ‪۴‬ونوعی ازشیاف است که درچشم‬

‫دیسقوریدوس ‏‪ ١‬بکراولوضم‬                                          ‫رمد کشیده کشند ‏ و چنبر دابره ‪ -‬و غربال‬
‫خامی که واو باشد‬
               ‫قاف وسکون ثالی و الث و‬                                                   ‫و پرویزن را دگیوزیند ‪.‬‬
‫بواو‬   ‫ابجد‬   ‫دال‬   ‫رسینه و‬   ‫بی نقطه بتحتانی‬   ‫رای‬   ‫و‬          ‫دار ندان ‪ = °‬بروزن‌بی‌دندان» سهياية‬
‫دحاکمیمی است از‬                         ‫ا‬‫‪+‬‬                       ‫آهنی باشد که دیگه مین رابربالایآن گذارند‬

                                                                                      ‫(‪ )۱‬چك ‪:‬وزا‪.‬‬

  ‫ازکامة _ ‪ 2502‬باشد‬          ‫آفای‌پورداود نوشته اند‪ :‬شاید دیز»‬           ‫‪۴‬‬           ‫رك ‪ :‬ديرد‬      ‫‪۱‬‬

  ‫‪ :‬تمد یس ‪۰‬‬        ‫دادن که در کلمات‬   ‫وشان‬   ‫مودن‬        ‫اوستابی نمعتی‬       ‫‪682‬‬   ‫بمعنی نما ونشان ‪ ۰‬ازمصدر ‪-‬‬


  ‫فرخاردیی‌وطاقدیس آمده " بنابرین «شبدیز» لفة بمعنی شب نماء وتبدبل سین‌بزاه درکلمه‌اسپربی‬
  ‫= اسپریز دیده ميشود‪ .‬دیزودیزه جکداانه در ادبیات مابمعنی سیاء آمد وبوبژه ازبرای اسب‌سیاه‬
                                                          ‫بکار رفته مانند شبرنگه وشبگون ‪:‬‬
               ‫کرو رده زصرصر در تك وتیز‪.‬‬                           ‫یکی شبگون که امش بودشبدیز‬
                                             ‫آیدز ر‬
                          ‫‪.‬ودی ترديك دزقول ) ‪.‬‬                     ‫رك‪ :‬دز ‪ .‬دژ ؛ آب دیز (=‬           ‫‪۴‬‬
  ‫معنی از باد کلمةٌ « دیگه » («‪.‬م‪ ).‬د قاب اص ‪ ۱۹۲‬ح» ‪.‬قس‪ :‬دیزیی ورك ‪:‬‬                            ‫‪ ۴‬م‪-‬اين‬
  ‫یابه ) |د بگدان ‪ .‬دیگپابه ]‪ ,‬ماز سرانی کنونی‬               ‫س‬    ‫(‬            ‫طبری ‪0‬‬       ‫‪۶‬‬            ‫دىزتدان ‪.‬‬
                                                    ‫ر=‬
                                ‫ان) « راژه نامه ‪. ۷۸۳‬‬ ‫‪ +‬ادان (‬                      ‫‪ 0006211‬از د‪:‬یز ‪9‬‬
  ‫ابا از‬        ‫رن‬
                 ‫ه_‬‫ھ‬                    ‫رك ‪ :‬دوز ‪١‬‏ دز » دژ‪.‬‬          ‫‪۴‬‬                ‫‪ - ۱‬ره ‪ :‬دیز‬
  ‫ربشة اوستابی‪( 56۳20 -‬کء > نظر) ؛ حندی باستان ‪( 6۲0‬رویت » دیده شده )‪( - 49۴ ۰‬فظر‬
                                              ‫ولی ه‬                           ‫دیده شده ) میداند « اسشق ‪roc‬‬
  ‫وتمان آبرا از ره‪ çid ‎‬ساسکرت‪ ) .‬شان دادن‪) ‎‬‬

=== leaf 373 (est p.916) ===
 ‫دطروجاش‬                                                                                  ‫‪4‬‬    ‫سل‬


 ‫خرش" د با فا ورای بشیطه‬
                       ‫دیف د‬                      ‫حکمای بونان ‪ .‬گوبند نباتات و رحتنی را مسار‬
 ‫بروزن فیل مخش ‪ ۰‬نام دوابی است امزوسیقی‪.‬‬                                         ‫خوب شناختی ‪.‬‬
‫دیفرو جاس * = بکراول وسکون‬                       ‫دیس ناو ‪ ۱‬ب=الون بالف کشیده بر‬
‫ثانی وضم ثالث ورای یې نقطه بواو رسیده وجیم‬
‫بالف کشیده بین مهملةٌ زده ‪,‬بلفت یومالی‬                                  ‫دراثیات مذهب خودش ‪.‬‬
‫دوعی از مرقششاست » وآن معدلی وغیرمعدلی‬              ‫مقس ف‬      ‫گنت‬     ‫وزو‬           ‫دسه‬
‫میباشد» و معدلی کلی باشد بيار سختو صلب‬                                                        ‫باشد ‪.‬‬
 ‫مانند سنگه » وآنزا از جزبرة قبری از درون‬
                                                   ‫دیش ِ = بائانی مجپول بروزن رش؛‬
‫چاهی برمی آورند" و غير معدلی‌رااز مس واقره‬
‫و طلا میگیرند ‪ .‬وآن چنان است که چون طلا‬            ‫و آمر بدادن همهت‬    ‫باشد ‪-‬‬   ‫بمعمی داد ودهش‬


 ‫ونقره ومس را بگدازند قدری آب برآن ریز‬                                               ‫ععتی بدش ˆ‬

      ‫‪ - ۱‬قطماً مآخذ برهان‌فاطع کتاب «دبستان المذاهب» است ‪ .‬ملف دبستان‌دریان‌طربشت‬
  ‫‪۱‬‬     ‫از چاپ کلکته ‪ « : )۹۰۸۱‬و درقسمتی ازدب‌ناد ‪ ۰‬او(مزدله) مکومه‪:‬‬        ‫مزدك گوید (س ‪۹۱:‬‬
  ‫واز «دبسناد»(بادالآخر) مطالبی‌تقل میکند‪ .‬تقربباً همةکليات مولف کتاب مزبور بامآخذ بلاواسطة‬
  ‫اوتحت لفط ازشپرستانی ترجمه وبض خیرات جزئی درآن داده شده منتهی دبستان همهرا ازقول‬
 ‫»کوهد مزدك نگاشته است ذکرميکند‪ .‬لازم است از خود بپرسیم کهآبا‬‫کتابی باسم « دسناد خ‬
 ‫مأخذ شهرستانی همان کتاب مزدکی یت ‪ ۲‬ولی ابن امر بنظر مشکل میآبد زبرا اگر چنین‬
  ‫کتابی در حقیقت وجود داشت چگونه باکمال اهمیت وی هيچبك از مورخان قدیم ابرانی وتازی‬
  ‫از آن نامی ببرده‌اند ؟ قبربیبقن است که دبستان از شهرستانی بیروی کرده است ‪ .‬شهرستانی‬
  ‫ازفول او ( عنی‬      ‫ا‬     ‫نکات مهمی دریاب مزدك آورده وهمه را با حملمهای « وراق مگوید ‪۰.‬‬

  ‫مزدك روایت میکنند » و نظایر آن آغا زکرده است ‪ .‬از سوی دبکر در کتاب دستان المذاهب‬
  ‫جمله‌های < و دربخشی از دیستاد » او (مزدك) میگوید» با ‪ ۶‬ودرهمین کتاب میگوید ‪ » ...‬ومانند‬
  ‫آن تماما مطابق وفائم مقام جمله های مذکور از شهرستانی است ‪ .‬چون کتاب « دبسناد» وجود‬
  ‫خارجی نداشته طرز قرائت با منشاه این اسم عجیب برای مااهمیت چندان ندارد‪ .‬حاعل باجاعلان‬
  ‫ولمات قدیمی را بکار برده‌اند‪ ...‬پیداست که‬
                                          ‫لیزکار خود را بکامال مپارت انجام داده و الفاظ ک‬
                       ‫در برهان «دیسناد» براثر غلط در رسم الخط به «دیتاو» تبدبل شده‪ .‬ر ‪:‬‬
        ‫‏‪Christensen, Le Règne du roi 2۷۵۵ 1..., ۵‬‬
  ‫‏‪1925 p. 86 sqq İyi. p. 89, note 1.‬‬
 ‫آبا « دیس‌اد » دبستان مصحف «دربت دبنان» (یهلوی ‪( ) 4517۵0 _ 0061‬بعلی دار کان‬
  ‫رك ‪ :‬کتاب فوق‬
              ‫دىن صحبح ) که بهپیروان آبين بوندس زردشت سلف مزدك اطلاق مشده (‬
      ‫‪ ۴‬بهلوی ‪( 62560‬شکل) «منای ‪.*۱۷۲:۲‬‬                 ‫تالف کربتنن ص ‪۷٩‬‏ ‪ )۸4 -‬یت ‪۲‬‬
                          ‫‪ = ۴‬دیورخش (ه‪.‬م ) ‪:‬‬            ‫رك‪ :‬دش ‪.‬‬       ‫‪۴‬‬            ‫ورك ‪ :‬دىس‪.‬‬


  ‫دامفالی ‪٩۷٩‬‏ ‪.‬‬    ‫« منوچپری‬
  ‫> ردیبرجای‬          ‫‪ ۲‬ص‬   ‫« لك‬   ‫آن دیفروجچس‬   ‫مصحف‬   ‫‪segyrbpiD‬‏‬    ‫دىفروغس‬   ‫عه‬    ‫©‬

                                                                                       ‫(ھ‪e.( .‬‏ ‪۰‬‬

=== leaf 374 (est p.917) ===
 ‫‪-4۱-‬‬                                                                                      ‫دنگ‬
                           ‫آهنین باشد ‪٩‬‏ ‪.‬‬       ‫واز بونه برآورند تفلکه در ته بوته مانده باشد‬
 ‫د یگ بر دینگ = بکسراولوسکون‬                     ‫مرقشیشاست » وآنرا دیفروجس بحذف الف یز‬
                                                ‫کفته‌اند ‪ .‬چون ارا سحق کنند وبرموی غلیظ‬
‫کاف آخر بر وزن بیخ ببریخ » م رکه موش‬                              ‫افشانند رقیق وترم کرداند ‪#.‬‬

                                                  ‫دلگ » بکسراول وسکون‌انی معروف‬
                                                ‫و کاف فارسی » بمعنی دی باشد که روز گنشته‬
                                                ‫است ‪ - ۱‬و بعربی خروس را کوبند ‪ - ۴‬و با‬
 ‫خسس‬   ‫و‬   ‫و دال بی نقطه ‪ ,‬کنابه از مردم شل‬
                                                 ‫تحتالی مجپول» ظرفیکه درآن چیزی پزند؟ ‪-‬‬
                                     ‫باشد ‪3.‬‬
                                                 ‫وتوپ بزر که رالیز گویند که بدانکلوله برقلمه‬
‫دیل ‪ -‬بر وزن فل » بمعتی تقعاه است‬                                                        ‫اندازند ‪.‬‬
 ‫که طرف خط باشد چه‌تعرف نقطه بطرف خط‬             ‫دیگ افز ار ‪ - ۴‬افزار دبک را‬
‫کرده اند ‪ -‬ودل را نیز گوبندکه بعربی قلب‬          ‫گوند‪ .‬یعنی آنچه دردیگه طمام ریز ندازنشود‬
                                                 ‫و کشمش وبادام وفلفل ودارچینی وقرلفل وزبره‬
‫کوسفندان وکاوان و دیگر چاریابان در آنجا‬          ‫ومانندآن ویعربی تابل خوانند وجمع‌آن توّابل‬
                                     ‫باشند ‪.‬‬             ‫است ‪ -‬ودنگه بزر که را نگیفزته‌اند ‪.‬‬

 ‫دیلم = با اول بتحتالی مجهول رسینه‬               ‫دیگ اورار ‪٩‬‏ با واو بوررن‬
 ‫اکیلان‬
      ‫وفتح لام وسکون میم‪ ,‬نام شهپری است ز‬        ‫ومعنی‌دیگه افزاراست که نخود وبادام کوشمش‪-‬‬
 ‫وموی مردم! لجاپیچیده ومجد میباشد و یشتر‬                   ‫ردنگه بز ر گے باشد ی‬     ‫وداروی کرم ‪۳‬‬


 ‫حربة ایشان تبر هیزم شکنی و زویین (‪ )۱‬امت‬        ‫‪-‬عنی‌دیکدان وسه با‬
                                                                  ‫دیگ پایه بم‬

                                                                   ‫(‪ )۱‬چك‪ :‬ژوبین ‪.‬‬

                          ‫تازی ‪.‬‬   ‫ک)اباف‬
                                        ‫‪ ( ۴‬عر‬                      ‫‪.‬‬   ‫‪ :‬دی‬   ‫رك‬    ‫‪۱‬‬
```


## [2026-09-05T20:09:55.971Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 375 376 377; do echo \"=== leaf $n (est p.$((n+543))) ===\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt; done 2>&1 | head -160"
}
```


### [2026-09-05T20:09:57.766Z] TOOL RESULT

```
=== leaf 375 (est p.918) ===
                                                                                                                       ‫‪--‬ي ‪۱4‬‬


‫بر وزن ریبوای » نرجمة‬                ‫دیماس ‪1‬‬                        ‫عربی سختی‬        ‫ر‬
                                                                                     ‫دو‬‫باشد ‪- ۱‬‬                ‫ویچك‬
                                                                                                                  ‫ککه ن‬
‫ظاهر گردسن‬       ‫‪0‬‬       ‫باشد که از واضح شدن‬       ‫توضیح‬
                                                                    ‫گروایند ‪ -‬و جابیرا‬        ‫وه‬
                                                                                               ‫ارن‬
                                                                                                 ‫ززمکا‬
                                                                                                     ‫و محنت رو‬
                                                   ‫‪.‬‬    ‫ا‬           ‫نیز گفته‌اند که مردمان وهورچگان درآ نجاجمع‬

‫یدماطی ‪ -‬با طای‌حطی‌بروزن میقانی؛‬                                                                                      ‫شوند ؟ ‪.‬‬
‫بخار سوخته راکوبند که ازبرق بهم حیرسد وبر‬                           ‫دیلمان ‪ « ۴‬بر وزن بیزبان ؛ بمعنی‬
‫سوخته‌آن سیمایر | منمقد گرداند؛‬               ‫جاحامخورد‬
                                                                             ‫رهی باشد اگزیلان ‪.‬‬ ‫هست ک‬
                                                                                                    ‫شم ا‬
                                                                                                       ‫دیل‬
‫و بعی گویند دیماطی لوعی از ستگت است که‬
                                          ‫در دریا مباشد ‪۰‬‬
                                                                    ‫ی‪۵‬لهاث ‪ -‬بااول بثالی مجهول کشید‪.‬‬
                                                                     ‫لوری‬
                                                                        ‫ا»‬‫وسکون ثالث و میم مفتوح یکاف زحده‬
‫دیماو ند ‪ = ۷‬بفتح واو وسکون لون‬
                                                                    ‫است شبیه بعنكبوت ولعاب اومهلك میباشد اوو‬
                         ‫و دال ‪ ۰.‬تام کوه دماو ند ادخ ‪۰‬‬
                                                                    ‫را بعربی رتبلا خوانند ‪ -‬و بفتح ثالث صفیردیلم‬
 ‫دیمر * س بر وزن دیگر > بمعنی دم‬                                                                                           ‫ام‬
      ‫باشد ویعربی خد گوبند ‪.‬‬               ‫است که رخاره‬
                                                                    ‫كلم = بسکون انی بورزن جیم ‪ ۰‬روی‬
‫یند» مخفف‬       ‫دل‬       ‫بروزن‬   ‫د بمو فك ‪= ۲‬‬
                                                                    ‫ورخاره باشد وبعربی خد گویند ‪ - ۴‬ولوعی‌از‬
      ‫دیماوند است که ناکموه دماوند باشد ‪.‬‬                           ‫چرم هم هست که سازی ادم خوانندش ‪ -‬وبفتح‬

                                                                     ‫انی در عربی جمع دیمه است که باران سخت‬
‫روی ورخاره باشد ‪ - ۸‬وبفتح اول بمعنی‬                                                                ‫باشد ® ‪.‬‬

  ‫‪ ۰‬شهرستالپای ابرانشپر‬              ‫» مار کوارت‬       ‫‪mulêD‬‏‬        ‫‪ ۰‬بهلوی‬    ‫قومی حاکن دبلمان‬           ‫‪۳ ۱‬‬

                                                       ‫‪ ۳‬و‬
                                     ‫‪-‬یمعنی شده و غلام ‪:‬‬                         ‫‪.‬‬   ‫ص ‪۹۷ ۸۷۰ ۷۷۰ ۰ ۲۵ ۰ ۱۳۳‬‬
       ‫هندو شه تکسرتان‪.‬‬                  ‫امبلكل»‬
                                               ‫بلم‬
                                                 ‫دب‬                  ‫در که کورا زشهان ودی‬         ‫همان‬     ‫این است‬

  ‫« خاقالی شروألی ‪. ۳۸۹۳‬‬
‫از ‪ :‬دیلم ‪ +‬ان (یسوند) ؛ مکلن دیلم ها ‪« :‬لاحت دیلم ناحیتی است آبادان و با‬                                          ‫‪۴‬‬
 ‫خواسته ومردمان وی همه لشکری اند با برزعگر وزناشان فيز برزیگری کنند و اشان را هیچ‬
                       ‫شهوری بامنبر فیست وشهرشان کلارست و چالوس » « حدودالمالم ‪.*۷۸‬‬
 ‫‪ _ ۴‬اوستا ‪ , 820۳621 -‬پهلوی ‪ 08076002 ۲86‬پ(ذیرفته‪ .‬برده ‪ ۰‬مشتغل )؛‬
  ‫اورامالی‬    ‫ارمنی ع ‪mêd‬‏ » اسثق ‪٦‬ه“‏ »کروی ‪mêd‬‏ (روی) »افغالی ‪amêl‬‏ «هو شمان ‪۹‬ء‬
  ‫»هرودی و سمنانی ‪ 71‬ک‪,‬شه‌یی ‪ « 011‬ك‪ .‬اورامان ‪۲*۰ : ۱۲۱‬‬
                                                      ‫«ك‪ .‬اورامان ‪ ۱۲۱۰‬ک‬                                                    ‫‪0‬‬
  ‫رك‪ :‬دیمه‪:‬‬          ‫©‬           ‫‪.‬‬    ‫‪ e‬ورك‪ :‬دمه‬       ‫‪GAF‬‏‬    ‫طری‬    ‫(رو) » صاب‬      ‫‏‪ .dîim‬طر ی ‪md‬‏‬                  ‫کیلکی‬

       ‫نعاشه کس کشت باد » غاشة او دەم ‪.‬‬                               ‫رعد‪ .‬مقرعةٌ او درحش‬         ‫مقرعه ز ن گشت‬


  ‫«منوچپری دامفانی ‪٩۵٩‬‏ ‪.‬‬
 ‫«مضفی لماند که دیمای در کتب لفت عربی مثل قاموی و غیرآن بمعنی پوشید کی‬                                             ‫‪۱‬‬
  ‫بمعنی حمام ونام محسی‬               ‫شغال ز بر زمن کنده باشند و‬          ‫ویمعنتی خانه‌ای که حوانات مل روناه و‬

  ‫و طاهر‬     ‫و واضح شدن‬          ‫و اما یمعخی توضرح‬            ‫است‬    ‫أ‬    ‫‪۰‬‬    ‫يود‬   ‫ساخته‬    ‫که حجاح بن توسفب‬

  ‫کردیدن که مصنف آورده درهبچ کتاب از کت متداولة عربی وفارسی بنظر نرسیده ‪ « » .‬چك‬
             ‫رك ‪ :‬دماو لك‪.‬‬           ‫‪۷‬‬          ‫آست‪.‬‬    ‫از بر‌ساخته حهای فرقة آنر کوان‬            ‫‪۰‬‬   ‫وظ‬       ‫‪.‬‬   ‫‪۴‬‬   ‫ح‬    ‫‪°‬‬

                                                                                        ‫‪.‬‬    ‫دم‬    ‫رك‪:‬‬     ‫_‬       ‫‪4‬‬

=== leaf 376 (est p.919) ===
  ‫‪6‬‬                                                                                                     ‫دیمیاد‬

‫دلن ‪ - ۴‬بکر اول بروزن سین ‪ ۰‬نام‬                       ‫روشنی وضیا بود ‪ -‬وغله ای را نکیوزیند که با‬
‫فرشته‌ابست که بمحافظت قلم مأموراست ‪ -‬و نام‬              ‫آب باران حاصل مشود ‪ -‬و بمعنی باران وشم‬
 ‫روز بیست وچهارم بود از ماههای شمی ‪ .‬نيك‬                ‫حم آمده ؛ و بعضی گوبند بمعنی باران عربی‬
 ‫است درین روز فرزند بمکتب فرستادن و نکاح‬                                                              ‫‪١‬‏ ‪.‬‬    ‫ات‬
  ‫کیش‬
    ‫کردن ‪ - ۴‬ودر عربی بمعنی راه وروش و‬                 ‫هیا ‪۲-‬با بای حطی بروزن دبوزاد ‪.‬‬
                                                                                     ‫د‬
 ‫وعادت و فرمان برداری وشن وشو کت و مرتبه‬               ‫آنست که‬
                                                             ‫و آ‬             ‫باند‪.‬‬
                                                                                 ‫تکفسو ر‬          ‫غررور‬
                                                                                                      ‫ک‬
 ‫_ومالك ‪ ,‬یادشاه باشد ‪ -‬وبفتح اول هم درعربی‬
                                                        ‫اموال فانِةٌ خسبه را در نظر نیاورد وبربذل أن‬
                            ‫فرض و وام را گویند ‪:‬‬                                                  ‫فادر باشد ‪۱‬‬

 ‫دیا = بورزن بینا * نام خواهر بوسف‬                      ‫دمین = ‪,‬کر اول و انی مجهول بر‬  ‫ی‬
 ‫علیه‌اللام است ‪ -‬ویمه‌نی داور وداوری و فتوی‬             ‫وزن مين » چلك بازیرا گویند وآن دوچوب‬
                       ‫نوشتن حم آمده ات ® ‪.‬‬
                                                        ‫دار سه وجب و دیگری بقدر بك‬
                                                                                 ‫م یقکی‬
                                                                                      ‫ابست‬
‫د ينار ‪ = 1‬بر وزن بیمار » زر سرخ را‬                     ‫قبضه وهردوسر جوب کوچك تيز میباشد واکثر‬
‫همچو تمام‬        ‫همست‬
                    ‫‌تم‬
                      ‫می م‬
                         ‫هعن‬
                           ‫بم‬            ‫ام‬
                                          ‫تدم ‪-‬‬
                                              ‫وبن‬
                                                ‫گو‬     ‫طفلان‌بدان بازی کنند ؛ وبفتح اول هم‌بنظرآمده‬
‫ینجاه نابه نود که چپل باشد ‪ -‬وپرنده بزرکی‬                         ‫‪۰‬‬   ‫هم میگویند‬   ‫وآلرا دیمین جوب‬           ‫است‬




  ‫«دیمه کن اول» بارانی است که همشه میا بد درآراش ی رعد ویرق‌با در نگ‬                          ‫‪۱‬‬
   ‫میکند پنجروز بادش روزباهفت‌روز ‪,‬با روزی وشبی ‪...‬جمع آن ديم بروزن عنب» «شرح‌فاموس؟‪.‬‬
   ‫اوستا ‪ , 20680 -‬پېلوى‬             ‫‪۴‬‬        ‫ظ برساختهُ فرقه آذر کیوان ‪.‬‬           ‫‪۳‬‬             ‫‪۰‬‬   ‫دم‬     ‫رك‪:‬‬


   ‫‪ 0‬بازد‪ .1‬ارمنیم ‪«060‬اسشق ‪ .»۷۹۵‬دلنا ازمصدر اوستابی ڭڭ( شناختن و اندشیدن)‬
   ‫آمده که‌برایر است‌باريشة ‪ 01‬درسانسکریت‪ .‬دگراتپا ودیگر بخشهای اوستا مکرر کلمةٌ «دئنا»‬
   ‫آمده‪ .‬دین گدارتها بمعانی مختلف کیش‪ ,‬خصایص روحی‪ ,‬تخص معنوی ووجدان بکار رفته‪ .‬بمعنی‬
   ‫اخیر؛ دین یکی ازفوای پنجگانة باطن اسان است‪ .‬ویز نام ابزدی است از ابزدان آبین زرنشتی‬
   ‫و تگهبانی روز بیت و چهارم ماه بایزد دين سپرده شده ‪ .‬ابوربحان در فپرست نامهای روزهای‬
        ‫رده ‪:‬‬
            ‫ایرانی نام این روز را ‪۶‬دین ‪٩‬‏ و درسفدی حم ‪ +‬دین ‪ ۴‬و درخوارزمی نیز «دین؟ بکاد‬
               ‫میخور و شادی کن و خرمنشین ‪.‬‬                  ‫يتن‬
                                                              ‫دکف‬
                                                                ‫دن روز ای روی تو ‪ ۰‬آ‬
   ‫“‪06٦٦‬‏ ‪.‬‬    ‫‪« .‬مسعود صعد‬                                   ‫‪۱‬‬

  ‫اما دین در عریی از ره ذخ و ماشو از زبانهای سامی است ‪ .‬تازبان این کلمه را‬
   ‫مح الواسطه از زبان | کدی گرفته‌اند ‪ .‬در زبان اخیرکلمات ‪ 1۷0۵0‬و ‪ 111‬بعنی فانون وحق‬
   ‫وداوری‌است» ‪ 0۷‬بمعنی حکم کردن و "‪ 2120‬بمعنی قاضی است ‪ .‬درعبری و آرامی‬
   ‫‪ 8‬و ‪ 2814‬بمعنی قالون وحق وداوری است‪ 08/121 .‬و ‪ 202120‬بمعنی‌حاکم و قاضی‪.‬‬
    ‫‪۲‬ص ‪ « ۹۵۱-۹۹۱‬روز شماری ‪۵۵-۷۵۲‬‬                  ‫دین و دبان از آرامی وارد زبان عربی شده ‪ « .‬بشتپا‬
   ‫‪ ۵‬هزء ‪ 8014‬پهلوی ‪ » 02056020‬داوری‪,‬‬                     ‫‪ ۴‬رك‪ :‬دى‪.‬‬            ‫ورك‪ :‬داثرة المعارف‌اسلام‪ .‬‏‬
  ‫از‬     ‫‪ - ۱‬پپاوی ‪ « ۲82061‬تاوادیا ‪۰۹۱‬‬                 ‫حکم «بولکر ‪۹۷٩‬‏ ورك‪ :‬دین(درزبانهای سامی)‪.‬‬
   ‫لاتینی ‪ 511180621‬بتقدیر ‪ 510101110‬بمعنی «نقدی برابر ده‌آی» چه در اول وضع آن ازنقره‬
   ‫ومساوی ده‌ای ‪ 88‬بودو آس ازنقود مسین بود» وبعدها دتاربوی بمعنی خودآی استعمال شد «نقود‬
   ‫برای ارزش دبنار ‪ ۰‬رك ‪ ۳‬داگرة المعارف‬        ‫‪€: +‬‬     ‫“معرب آن حمدنار هری ج ص‪۳۱‬‬                      ‫ج‬      ‫ص‬

              ‫‪)۹۰۱‬‬   ‫‪۹۰۱2‬‬   ‫ص‬   ‫ج‪۱‬‬   ‫اسلام؛ و( ارزش دینار و تومان در فرون مختلفه ‪ .‬مقالات کسرری‬

=== leaf 377 (est p.920) ===
                                                                                                            ‫‪۱۷‬‬


 ‫دی ره ‪ -‬بضم باوزای‌فارسی وسکون‬                                  ‫است چه باز بسیار بزرکه راباونشبت دهند وباز‬
‫که نام روز بانزدهم‬
                 ‫ها مخفف دين پژوه است ‪۴‬‬                          ‫دبتار گویند ‪ .‬و بعضی کویند دبذار نوعی از باز‬
                      ‫باشد ازهرماه ملکی ‪.‬‬
                                                                  ‫است وآن بیاراصیل کومیاب‌میباشد وبرخلاف‬
 ‫دینسافوس ‏‪ - ٩‬بکس اول و اك‬                                      ‫بازهای دیگر بردورمردمك چشم اوتحربرسیاهی‬
 ‫وسین بی‌نقطه (‪ )۳‬بالف کے ده وفای بواو رستده‬                     ‫هت درغایت تراکت ‪ -‬ونخم کشوث را بسریانی‬
‫وسین بینقطة (‪)e‬‏ زده ‪ ۰‬بلغت بونانی نوعی از‬                                                                ‫دثار گوبند ‪.‬‬
 ‫خار باشد وبر گے آن بککر‌کاهو میماند و نآرا‬
 ‫وون ازهم بشکافند‬
                ‫شبرازی طوسك خوانند ‪ .‬چ‬
                                                                 ‫دینار اشمر (‪-‬ر دینار شمر سراف‬
                                                                                                                ‫کوت‬
                                                                                                                  ‫وا‬
‫کرمهای کوچك از مان ساق وبرکه‌آن برآ ند‬
 ‫وآنرابتازی خس‌الکلب کوبند ومشطالراعی همان‬                       ‫دبنارو له = با رای بی‌نقطه (‪ )۱‬بواو‬
‫است ‪ .‬اکر کل وشکوفة آنرا بکوبند و برشیر‬                          ‫کشیده و فتح بای حطی (‪ ۰ )۲‬بسریانی گیاهی‬
```


## [2026-09-05T20:10:17.915Z] TOOL CALL #18: Bash

```json
{
 "command": "sed -n '1,80p' tools/ref_page.py"
}
```


### [2026-09-05T20:10:17.958Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
```


## [2026-09-05T20:10:23.293Z] TOOL CALL #19: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ | grep -i bqt; echo ---; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null"
}
```


### [2026-09-05T20:10:23.399Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  2634275 Sep  4 14:06 BQT_alt_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb      139 Sep  4 14:06 BQT_dli_part1.txt
-rw-rw-r--  1 sfmqrb sfmqrb 26399828 Sep  4 14:06 BQT_v1_djvu.xml
-rw-rw-r--  1 sfmqrb sfmqrb  2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb  4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2359504 Sep  4 14:06 BQT_v2.txt
---
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
```


## [2026-09-05T20:10:34.042Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA medina/Stadt ===\"; grep -n \"Medina\\|medina\\|Medîna\\|madîna\" AFA.txt | head -20; echo \"=== AFA din/Gericht ===\"; grep -n \"Richter\\|Gericht\" AFA.txt | head -20"
}
```


### [2026-09-05T20:10:34.102Z] TOOL RESULT

```
=== AFA medina/Stadt ===
1315:aLlk^to^ T^^* I- 363, 17. (Burton Reise nach Medina und
1552:Ob JoSL ein Platz in Medinah Bekri 159, 1; 175, 13, 14
5593:Von blühendem Weine in Medina bei Fa41 ihn ^Abbäs
8787:Leder schneidet. In Medina heisst es Bu^. Im Buche
8990:•sein Leder schneidet. In Medina heisst es iU^. Im Bache
=== AFA din/Gericht ===
1793:Aramäisch sind auch einige Namen von Gerichten. Längst
6642:arcüp und "l^^Dp (babylonisch)) sondern als eine Gerichts-
9819:seia")]. Wohl aber ist niHO U^U^le > der Gerichtsbezirk".
```


## [2026-09-05T20:10:35.210Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AKD din ===\"; grep -n \"dinu\\|dênu\\|dajanu\\|dayanu\\|Richter\" AKD.txt | head -30"
}
```


### [2026-09-05T20:10:35.262Z] TOOL RESULT

```
=== AKD din ===
306:akk.  dmu,  dnw  Gericht,  Reclit,  Rechtssache,  dami,  richten, dajjänu  Richter  (viell.  <;  sum.  di)  :  >  wahrsch.,  allerdings  schon  in  früher Zeit,  hebr.  ^  u.  aram.  din,   dind  Gericht,  Recht,   Rechtssache,  dnn  richten,
309:dajjän,  dajjana  Richter,  madinta  Stadt  (eig.  Gericlitsbezirk) ;  aus  aram.  ^ arab.  dm,  ätb.  dain  Gericht,  arab.  dajjän  Eichter,  madtnat  Stadt,  wie  auch späthebr.  madinu.  —  Aber  auch  pers.  daena,  den,  dm  Glaube,  Religion O  arab.  dm  Religion)  ist  viell.  erst  <;^  atk.  de(7)nu.  —  Yon  akk.  bei  dnü Prozeßgegner,  wird  beeinflußt  sein  liebr.  haal  vtispäf,  neuliebr.  baal  din, aram.  is'el  dmü;  von  akk.  dma  dahdhu  mit  jeni.  rechten,  prozessieren, hebr.  dlbber  miSpdtnn;  vgl.  auch  akk.  hissil  dajjdnfdi  Ricliterstuhl  und hebr.  kisse  dtn.  [Das  namentlich  im  Hebr.  und  Phon,  heimische  Wort
403:S.  ferner  zu  weitereu  Bezeichniuigen  von  Handwerken,  Künsten  und sonstigen  Berufstätigkeiten  noch  S.  24  zu  dajjanu  Richter,  S.  7  zu purtdu Eilbo^te,  S.  49  zu  asü  Arzt,  S.  40  zu  iJckaru  und  irrüu  Laudmann, S.  40  zu  scikinu  Gärtner,  S.  41  zu  allallu  und  nüqidu  Hirt,  S.  14  f.  zu mdti  jagen,  arru  Vogelfänger,  hfiru  Fischer,  S.  45  zu  malalju Schiffer,  S.  39  zu  nuhatimmu  Bäcker.
522:siidinmi,   saddinu   ein   Kleidungsstück  :  ]>•  viell.    hebr.   sadht  leinenes
637:akk.  edinu  Steppe,  Wüste  (<;  sum.  edin)  :  >  wohl  hebr.  'eden „Eden"  als  Bez.  des  Gebiets  des  Paradieses  (aber  volksetymol.  nüt  'eden Wonne,  verknüpft).  akk.  natnü,  nawü  Trift,  Wüste  :  ]>  viell.  hebr.
879:akk.  anmrdlnu,  murdlnii  (für  ivurdinu)  ein  Staclielgewächs  :  wohl zusammenhängend  mit  aram.  wardd,  arab.  ward  Rose,  wozu  armen,  vard, griech.  QÖSoy,  lat.  rosa  usw.,   Böse.  akk.   etidu,  etidtii  ein  Dornge-
1127:Mögen  auch  jetzt  die  Urteile  darüber  diametral  auseinander  gehen; die  Geschichte  wird  einst  die  unbestechliche  Richterin  darüber  sein,  wer in  diesem  Weltkriege  in  Wirklichkeit  die  Rolle  des  Barbaren  und  Kultur- zerstörers spielt,  und  wer  andererseits  die  edelsten  Kulturgüter  der  Mensch- heit in  Wahrheit  zu  schützen  sich  angelegen  sein  läßt.  Wenn  aber,  wie zu  hoffen  steht,  als  Frucht  dieses  gewaltigsten  aller  bisherigen  Kriege  ein schließlicher  Sieg  des  Kampfes  um  solche  edelste  Güter  der  Menschheit gegen  alle  ihre  Verächter  sich  einstellt,  so  haben  auch  die  siebenzehn jungen  Gelehrten,  von  deren  Tod  für  das  Vaterland  die  anschließenden Blätter  dieses  Programms  leider  Kunde  geben  müssen  —  und  wie  viele Namen  aus  den  früheren  Jahrgängen  dieser  Programme  wären  ihnen  bei- zufügen! — ,  den  Heldentod  nicht  umsonst  erlitten.
1158:Henrico  Mauritio  Equiti  de  Richter Imperatori  Austriaco  a  consiliis  aiiiicis     Professori  Vindobonensi.
```


## [2026-09-05T20:10:47.453Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AKD.txt',encoding='utf-8',errors='replace').read()\ni=t.find('akk.  dmu,  dnw  Gericht')\nprint('leaf',t.count('\\f',0,i))\nEOF\necho \"=== WEB Delilah ===\"; grep -n \"Delilah\" WEB_vol1.txt | head"
}
```


### [2026-09-05T20:10:48.999Z] TOOL RESULT

```
leaf 32
=== WEB Delilah ===
51452:Delilah, n. [Heb. delilan, lit., delic e mistress of S Philistines Be
```


## [2026-09-05T20:10:49.215Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 MON_part1.txt; echo ...; grep -c $'\\f' MON_part1.txt MON_part2.txt; echo \"=== grep دلیله ===\"; grep -n \"دلیله\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head"
}
```


### [2026-09-05T20:10:51.209Z] TOOL RESULT

```
0 
2 

...
MON_part1.txt:0
MON_part2.txt:0
=== grep دلیله ===
```


## [2026-09-05T20:10:57.840Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c MON_part1.txt MON_part2.txt && head -c 800 MON_part1.txt; echo; echo \"=== v1 djvu head ===\"; ls -la incoming/MON/ && head -c 400 incoming/MON/MON_2vol_Adena_v1_djvu.txt"
}
```


### [2026-09-05T20:10:57.890Z] TOOL RESULT

```
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
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
و ده ها وی مزا موی ماما میو و موه ومد موه اش اما موم م میا شا ولمم 


معین, محمد» ۱۳۵۰۰۱۲۹۱ 
فرهنگ معین / محمد معین. -- تهران: آدنا: کتا�
=== v1 djvu head ===
total 48692
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
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


هم مشب جج جب بیج چم �
```


## [2026-09-05T20:10:58.785Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Delilah, n. [Heb.')\nprint('leaf',t.count('\\f',0,i))\nprint(t[i-600:i+400])\nEOF"
}
```


### [2026-09-05T20:11:00.658Z] TOOL RESULT

```
leaf 512
s, lightful.
dé-light/ing, a. g glad.
e
who takes deli easing: i charming ing, gladso;
% 8 adsom captivating, plove.
a deli
dé@-light’ing-ly, adv, in a deligh
dé light’séme, [Archaic and Poet.]
dé-light’/sdme-ly, adv. ver delightful manner.
dé-light’/séme-ness, chaic and Poet,]
dé-lig/nate, v.l. to de trees. [Rare.
1. in the Bible, thi betrayed him to the hair cut off while he
a. very pleas
y pleasi vee [Archaic and Post)!
n. delightfulness. [Ar-
ghtf; n. the quality of ê
ing; de
ght, giving a
nner, emng de.
iving great Pleasure: maki i making
ting manner, lightfuy
ma
Prive of wood by felling
Delilah, n. [Heb. delilan, lit., delic e mistress of S Philistines Be
: 7 A was asleep, ing him of his strength: Tada thus
ate.]
mson, who having his epriv-
. XV1,
2. a false woman; temptress; harlot.
dé-lim/it, v.t. [Fr. délimiter,
of; to bound; to mark the dé-lim/i-tate, v.1.; itating, limitare.] to delimit. dé-lim-i-ta’tion, n. being delimited.
: to limit; h ilare, to mark out the limits.] to c
```


## [2026-09-05T20:11:07.023Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 511 512 513; do echo \"--- leaf $n ---\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' WEB_vol1.txt | grep -oE '\\b4[0-9]{2}\\b' | sort -u | tr '\\n' ' '; echo; done"
}
```


### [2026-09-05T20:11:08.610Z] TOOL RESULT

```
--- leaf 511 ---

--- leaf 512 ---

--- leaf 513 ---
```


## [2026-09-05T20:11:09.047Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON v1 djvu دین ===\"; grep -n \"دیّان\\|دیان\\b\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -5; echo \"=== ذلیل ===\"; grep -n \"ذلیل\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -5; echo \"=== مدینه ===\"; grep -n \"مدینه\" incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5"
}
```


### [2026-09-05T20:11:09.129Z] TOOL RESULT

```
=== MON v1 djvu دین ===
346:مقالات وی در موضوعات ادب؛ تاریخ ادیان» ایران دورة قبل از اسلام و 
4629:مسحصولات فلاحتی» ادیان و مداهب و 
18617:بادیان رومی. 
19899:بادیان: 2-0 (امر .) برده‌ای که بر ثبر 
20045:بادیان: مورزفةه (- بادیانه - وادبان] (ا.) 
=== ذلیل ===
9193:اذل: المعه [ع.] (ص‌تفض.. دلت) ذلیل تره 
9197:کسی را؛ خوار شمردن» خوار و ذلیل گرفتن 
10088:خوار گردانیدن» ذلیل کردن. خشم کردن 
31646:دون» خوار» دانی. ذلیل» زیون بی‌مقداره 
33866:شغلی. از غرور بایین آمدن» ذلیل شدن. 
=== مدینه ===
30220:است که به زبارت به عراق يا مکه و مدینه 
51901:مدینه. منسوب و مربوط به مدینه (شهر) 
51902:مسطلقاً). آنچه مسربوط به مدینه (شهر 
51905:مدن (به ضم اول و دوم) جمع مدینه» ولی 
51906:اصح مدنی است نسبت به مدینه (مفرد).
```


## [2026-09-05T20:11:17.657Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON && echo \"=== ذلیل headword ===\"; grep -n \"^ذلیل\\|^ذلت\\|^ذلال\" MON_2vol_Adena_v1_djvu.txt | head; echo \"=== دین headword v1 ===\"; grep -n \"^دین\" MON_2vol_Adena_v1_djvu.txt | head -20; echo \"=== مدینه/تمدن v2 ===\"; grep -n \"^مدینه\\|^مدنی\\|^تمدن\" MON_2vol_Adena_v2_djvu.txt MON_2vol_Adena_v1_djvu.txt | head -20"
}
```


### [2026-09-05T20:11:17.803Z] TOOL RESULT

```
=== ذلیل headword ===
39423:ذلیل گردانیدن؛ ذلیل شمردن. رام ساختن؛ 
65270:ذلیل گشتن. (امص.) خواری» مدلت» ستی؛ 
=== دین headword v1 ===
3836:دینام و باتری موقعی وصل می‌کند که ولت 
3837:دینام بالاتر از ولت باتری گردد یعنی فقط 
4439:دین» وام) بدهکاری. آلودگی 1 شیر ک: 
10315:دینی زرتشتی) سنگ بزرگی است چهار 
20900:دینار. 
28560:دین یا مذهبی باطل داشتن. پوش به پالان 
31811:دین* موخر. قیقب؟ مق. پیشکوهه» قربوس. 
39382:دین‌دار شدن. (امص.) دین‌ورزی. 
54485:دینی: حوزة علمبة قم. جانب» طرف. وسط 
59737:دینگ: ِ( (عم. ۰ احمق» کودن. 
59739:دینگوز: 120278-2) (ص.) دینگ. الد نگ 
60332:دین. (تص.) حالتی که از موب ظاهر شود 
64311:دینداری کردن. (امص.) دینداری. (.) آیین 
64673:دین: (020)007 [ع.] (.) قر.ص» وام؛ ج‌. 
64676:دین: 40 (اخ.) نام ایزدی است. روز بیست 
64679:دینار: 5 ([- دینار» معر.] (ا.) سکهٌ طلاه 
64689:دینارشمر: ۲ (ص‌فا.) صراف. 
64690:دیناری: -1]027 (ص‌نسه.) بارچه‌ای است 
64693:دینام: همه (.) (مک.) دستگاهی که 
64713:دینامیت: ؛«ةهآة (.) ماده‌ای قابل انفجار 
=== مدینه/تمدن v2 ===
MON_2vol_Adena_v1_djvu.txt:16843:تمدن اآشتتا تباشد (سشر در نورد رنان 
MON_2vol_Adena_v1_djvu.txt:36692:مدینه آغاز می‌شود که برابر با سال ۲ ۰۲ م. 
MON_2vol_Adena_v1_djvu.txt:81786:مدنیه و یکی از اقسام سیاست ملک است که 
MON_2vol_Adena_v1_djvu.txt:82886:مدینه. کشور» مملکت: ایران‌شار (- ابران 
MON_2vol_Adena_v1_djvu.txt:95768:مدنی: (یز.) رشته. 
MON_2vol_Adena_v2_djvu.txt:10888:تمدن و متناسب با مصلحت مردم است و 
MON_2vol_Adena_v2_djvu.txt:51900:مدنی: [۵2022 [ع.] (ص‌نسه.) منسوب به 
MON_2vol_Adena_v2_djvu.txt:51901:مدینه. منسوب و مربوط به مدینه (شهر) 
MON_2vol_Adena_v2_djvu.txt:51907:مدنیت: 0212027-1772 [ع۰] (مسص جد.) 
MON_2vol_Adena_v2_djvu.txt:52008:مدینه‌ای که ساکنان آن کوشش کنند که 
MON_2vol_Adena_v2_djvu.txt:52010:مدینه‌ای بدست حکیمان و فاضلان باشد.
```


## [2026-09-05T20:11:23.572Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON && sed -n '64665,64695p' MON_2vol_Adena_v1_djvu.txt; echo \"=====2\"; sed -n '51895,51930p' MON_2vol_Adena_v2_djvu.txt; echo \"=====3 zalil\"; grep -n \"ذلیل:\\|ذلت:\\|ذلال\" MON_2vol_Adena_v1_djvu.txt | head"
}
```


### [2026-09-05T20:11:23.661Z] TOOL RESULT

```
۵ 


دیمی: آ-()ه ۹2 [ع. ف.] (ص‌نس..) 
شوب دی ان # از آن را مس 
۳ باشد؛ آبباری نشده. (عم.) بی‌مطالعه» 
الیی. 

دین: (020)007 [ع.] (.) قر.ص» وام؛ ج‌. 
دیون. 

دین: 40 (اخ.) نام ایزدی است. روز بیست 
و چهارم هر ماه شمسی. آیین» کیش؛ ج. (ع( 
ادیان. راه» روش. دین محمدی: اسلام. 
دینار: 5 ([- دینار» معر.] (ا.) سکهٌ طلاه 
مسک وک زر. ضح.- ارزش دینار در ایران و 
ممالکك دیگر در ادوار مختلف فرق داشته. 
رکك. ارزش دینار و تومان در قرون مختلفه» 
مقالات کسروی. ج ۱ص ۰۱۰۹-۱۰۲ در 
عهد قاجاریه لس قران. در عسصر 
تاق ات فا وا ول دولت کون 
عراق (بیرالنهرین) که معادل یک لیرة 
انلس است؛ ج. (ع.) دنانیر. دینار رایج: 
دبناری که در میان مردم رواج دارد. 
دینارشمر: ۲ (ص‌فا.) صراف. 
دیناری: -1]027 (ص‌نسه.) بارچه‌ای است 
ابریشمین. نوعی از شراب لعلی. 

دینام: همه (.) (مک.) دستگاهی که 
نیروی مکانیکی را به نیروی الکتریکی 
تبدیل کند و بالعکس (مانند دینام اتومیل). 
=====2
سرش شکسته و زخم به دماغش رسیده. 
آنکه به دماغش آسیب رسیده. (کد.) احمق» 
گود. 

مدنگ؛ هج2هه (.) دندانه کلمدان. 
مدنی: [۵2022 [ع.] (ص‌نسه.) منسوب به 
مدینه. منسوب و مربوط به مدینه (شهر) 
مسطلقاً). آنچه مسربوط به مدینه (شهر 
معروف) باشد. شهرنشین. ضح.- بعصی 
رمدنی» به ضم اول و دوم خوانند منسوب به 
مدن (به ضم اول و دوم) جمع مدینه» ولی 
اصح مدنی است نسبت به مدینه (مفرد). 
مدنیت: 0212027-1772 [ع۰] (مسص جد.) 
مد‌ور؛ 7۵027۷۵۲ [ع. .] (امف ) گر ده دایر ه. 
(بع.) یک مصراع از شعر که آن را بصورت 
دایره نو سند بطوری که از هر کلمة آن 
بتوان شروع کرد و خواند. مدور صغیر: 
(خطا.) قلمی (شعبه‌ای از خط عربی) که از 
مدور کبیر استخراج 0 قلم جامعی 
است که دفاتر و حدیث و اشعار را با ان 
می‌نوشتند (ترجمةً الفهرست ابن‌النديم. 
۴ مدور کبر: (خطا.) قلمی (شعبه‌ای از 
خط عربی) است که از خفیف النصف 
استخراج شده و آن را نویسندگان عهد 
ابن الند یم «ریاسی» می‌گفتند و در دادخواهی 
بکار می‌رفت. (ترجمة الفهرست ابن‌الندیم. 
۱۴-2۳). 

مدول: [۵۵2۵ [ع.] (امف.) دارای دوال؛ 
دوال‌دار. ظاهر ا قماش کناره‌دار و مطرز و 


مدون 
سحیف‌دار است (به استعاره از دوال چرم). 
مد‌ون: 20002۷27 [ع.] (امف.) جمع کرده 
شده. فراهم آمده. کتاب شعر و مجموعة 
=====3 zalil
9196:اذلال: 2121 [ع.] (مص م.) خوار بنداشتن 
39422:تذلیل: ۱22111 [ع.] (مص ع.) خوار کردن» 
65265:لالت: -عه راهاقاهة [ع. ذلالة] (مصل.) 
65271:ج. ذلال. 
65283:جع اذ لاء» اذله و ذلال. دلییل مر ده: (عم.)
```


## [2026-09-05T20:11:31.386Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON && sed -n '65260,65295p' MON_2vol_Adena_v1_djvu.txt"
}
```


### [2026-09-05T20:11:31.445Z] TOOL RESULT

```
مسق. عز. رامی» فروتنی) اس فش کسا.ه 
مهربانی» رحمت» رافت. رفق» نرمی. 

دلا فت: امرقامة [ع. ذلاقة] (اسص.) تبز 
زبانی» فصاحت» کشاده زبانی» چبره زبانی. 
لالت: -عه راهاقاهة [ع. ذلالة] (مصل.) 
خوار شدن ذلیل گردیدن. (امص.) خواری؛ 
دلت» مذلت. 

دلت؛ اداام2 [ع. ذله ] (مص‌ل.) خوار شدن» 
ذلیل گشتن. (امص.) خواری» مدلت» ستی؛ 
ج. ذلال. 

دلق: امه [ع.] (ص.) چیره زبان» تیززبان 
دلیق. 

دلول: اقاهة [ع.] (ص.) رام» مطیع» منقاد؛ 
ج. . اله و دلل. 

دلتیته 221 [غ. ۰] (ص .) گشاده‌زیان؛ 
زبان آور» تیززبان. 

دلیل: 2211۱ [ع.] (ص.) خوار» زبون» حقیر) 
جع اذ لاء» اذله و ذلال. دلییل مر ده: (عم.) 
دشنامی است کسان را. 


۷۲۰ فرهنگ فار سی معیر ذم 


دم : (2200)00 ل. ۰] (مص م .) مذمت کردن» 
نکوهیدن» بد گفتن» قدح کردن) مق. 9 
(امص.) نکوهش» بدگویی» قدح؛ ج. ذموم 


(غم.)
```


## [2026-09-05T20:11:32.195Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== RCH zalil/madinah ===\"; grep -n \"zalíl\\|dhalíl\\|zalil\" RCH.txt | head -10; echo \"=== RCH madína ===\"; grep -n \"madína\\|madínat\" RCH.txt | head -10"
}
```


### [2026-09-05T20:11:32.271Z] TOOL RESULT

```
=== RCH zalil/madinah ===
42051:A   JJ J   zalilf  Abject,  mean,  contemptible.  Gentle,  submissive.
45906:Zulaj/kj  A   species  of  smooth  peach, p   zalily  A   hiccough,  a   belch.
=== RCH madína ===
```


## [2026-09-05T20:11:42.968Z] TOOL CALL #32: Bash

```json
{
 "command": "ls site/pages/138.jpg 2>/dev/null; pdftoppm -f 138 -l 138 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg138 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:11:45.361Z] TOOL RESULT

```
site/pages/138.jpg
total 4284
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:11 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb 746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb  53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb 107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb  89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb  60631 Sep  5 16:11 pg147.png
```


## [2026-09-05T20:11:48.372Z] TOOL CALL #33: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/138.jpg"
}
```


### [2026-09-05T20:11:48.398Z] TOOL RESULT

```

```


## [2026-09-05T20:12:12.838Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:12:12.845Z] TOOL RESULT

```


```


## [2026-09-05T20:12:17.768Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%AF%D9%8A%D9%86%D8%A9",
 "prompt": "Give the Arabic etymology section for مدينة madīna verbatim: is it derived from Aramaic מדינתא mᵊdīntā 'province, jurisdiction' (from dīn 'to judge'), or from the Arabic root d-y-n? Quote what it says, including any mention of Old South Arabian, Akkadian dīnu, and any disputes."
}
```


## [2026-09-05T20:12:19.212Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D9%86",
 "prompt": "Give the Arabic entries verbatim: دِين dīn 'religion' and dīn 'judgment', and دَيْن dayn 'debt'. What etymologies are given — Middle Persian dēn? Aramaic dīnā? Akkadian dīnu? Quote the etymology sections."
}
```


### [2026-09-05T20:12:23.179Z] TOOL RESULT

```
# Arabic Etymology for مدينة (madīna)

Based on the Wiktionary page provided, the Arabic etymology section states:

**Borrowed from Aramaic** _מְדִינְתָּא_ **(məḏīntā)**. The entry notes this word is cognate with Hebrew _מדינה_ (məḏînâ, "state") and Ugaritic _𐎎𐎄𐎐𐎚_ (mdnt). It specifies that "The root م د ن (m d n) is **denominal**."

The page does not mention Old South Arabian, Akkadian dīnu, or any disputes about the etymology. It presents the Aramaic borrowing as definitive, without discussing alternative theories or connection to an Arabic root d-y-n meaning "to judge."
```


### [2026-09-05T20:12:28.535Z] TOOL RESULT

```
# Arabic Entry Analysis: دين

## Verbatim Entries

**دِين** (dīn) - "religion, creed, faith" and "judgement, decision, ruling"

**دَيْن** (dayn) - "debt, debit, liability, pecuniary obligation, financial claim"

## Etymology Sources

The page identifies multiple etymological layers:

**Middle Persian:** "The sense of religious creed or a system of religious rules is borrowed from Middle Persian (dēn), which developed from Old Persian *dainah."

**Aramaic:** "Cognate terms in other Semitic languages also came with a more developed legal sense... bolstered semantically borrowing from Aramaic דִּינָא (dīnā), Classical Syriac ܕܺܝܢܳܐ (dīnā, 'judgement')."

**Akkadian:** The entry notes Akkadian دـ𒁲 (dīnum, "judgement; legal practice, precedent; legal case; court conduct, procedures, rule of law") as a possible ancestral source influencing Semitic legal terminology development.

**Proto-Semitic:** The word ultimately derives from "Proto-Semitic *dVn- ('obligated conduct; decisions of morality or ethics, judgement, decree, ruling')."
```


## [2026-09-05T20:12:34.868Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B0%D9%84",
 "prompt": "Arabic ذَلَّ (ḏalla) — give the etymology verbatim: what Proto-Semitic root, and which Hebrew/Aramaic/Akkadian cognates are cited (e.g. Hebrew זָלַל zālal, or Hebrew דָּלַל dālal)? Also any derived terms like ذَلِيل ḏalīl and ذِلَّة ḏilla."
}
```


## [2026-09-05T20:12:37.585Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%93%D7%9C%D7%99%D7%9C%D7%94",
 "prompt": "Hebrew דְּלִילָה (Delilah) — give the etymology verbatim. Is it from the root ד־ל־ל 'to be weak/low/hang down'? What meaning is given ('delicate, languishing, amorous'?), and any alternative etymologies (e.g. from לילה 'night', or Semitic 'flirtatious')?"
}
```


### [2026-09-05T20:12:39.458Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:12:40.236Z] TOOL RESULT

```
Based on the Wiktionary entry provided, I cannot find the specific etymological information you're requesting.

The page shows that ذل belongs to the Semitic root **ذ ل ل** (ḏ l l) and mentions "10 terms" in this category, but it does not provide:

- Proto-Semitic root details
- Hebrew, Aramaic, or Akkadian cognates
- Etymological explanations for related terms like ذَلِيل (ḏalīl) or ذِلَّة (ḏilla)

The entry only presents three etymologies with definitions and conjugation/declension tables, without the comparative Semitic linguistics data you're seeking. You would need to consult a more comprehensive etymological resource or academic reference on Semitic roots to obtain that information.
```


## [2026-09-05T20:12:44.351Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Delilah",
 "prompt": "Give the etymology of the English proper noun Delilah verbatim — Hebrew form, root, meaning, and any alternative proposals."
}
```


## [2026-09-05T20:12:45.348Z] TOOL CALL #40: WebSearch

```json
{
 "query": "Arabic ذل dhalla Hebrew זלל zalal cognate Proto-Semitic *ḏll \"to be lowly\" versus דלל dalal"
}
```


### [2026-09-05T20:12:48.536Z] TOOL RESULT

```
# Etymology of Delilah

Based on the Wiktionary article, here is the etymology information:

**Hebrew Form & Root:** The word is borrowed from Hebrew דְּלִילָה (d'līla).

**Meaning:** The Hebrew term translates to "[she who] weakened."

**Alternative Proposals:** The article does not mention any alternative etymological proposals for this term.

The etymology section is concise and provides a single, straightforward derivation without discussing competing theories about the name's origins.
```


### [2026-09-05T20:12:55.518Z] TOOL RESULT

```
Web search results for query: "Arabic ذل dhalla Hebrew זלל zalal cognate Proto-Semitic *ḏll "to be lowly" versus דלל dalal"

Links: [{"title":"Halal, Hillul, and the Shared Meanings of Hebrew and Arabic | Hebrew College","url":"https://hebrewcollege.edu/blog/halal-hillul-and-the-shared-meanings-of-hebrew-and-arabic/"},{"title":"K-P-R","url":"https://en.wikipedia.org/wiki/K-P-R"},{"title":"%E1%B8%8E%C4%81l","url":"https://en.wikipedia.org/wiki/%E1%B8%8E%C4%81l"},{"title":"Semitic languages - Wikipedia","url":"https://en.wikipedia.org/wiki/Semitic_languages"},{"title":"When Similar Means Different: Evaluating LLMs on Arabic--Hebrew Cognates","url":"https://arxiv.org/pdf/2606.13218"},{"title":"Zayin","url":"https://en.wikipedia.org/wiki/Zayin"},{"title":"Systematicity between Forms and Meanings across Languages Supports Efficient Communication","url":"https://arxiv.org/pdf/2601.17181"},{"title":"Proto-Semitic phonology | Paul Marciano Wiki | Fandom","url":"https://paul-marciano.fandom.com/wiki/Proto-Semitic_phonology"},{"title":"Grammar of the Alashian Language — Historical Phonology and Morphology","url":"https://www.veche.net/alashian/history"},{"title":"K-T-B","url":"https://en.wikipedia.org/wiki/K-T-B"}]

Based on the search results, I found information about cognate relationships between Arabic and Hebrew words within the Semitic language family, though the specific terms you asked about (ذل dhalla, זלל zalal, and דלל dalal) don't appear directly in these results.

However, the search results do provide relevant context about how such cognate relationships work. The relationship between the Hebrew word shalom and the Arabic word salaam is clear, as the words have nearly identical meanings and are phonetically similar, and the words' phonetic differences can be explained by well-known phonological features of Hebrew and Arabic, showing that the two words have descended from a common ancestor. Such words, when they are found in two languages, are referred to as "cognates."

The search results also note that the relationships between similar-sounding words (and in the case of the Semitic languages, similar roots) are sometimes straightforward and sometimes less so.

Unfortunately, the search results don't contain specific information about the Proto-Semitic root *ḏll and its reflexes in Arabic (dhalla) versus Hebrew (zalal/dalal). To get more detailed etymological information about these specific roots and their semantic distinctions, you might want to consult specialized Semitic language dictionaries or etymological works.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:13:11.911Z] TOOL CALL #41: WebSearch

```json
{
 "query": "BDB Hebrew דלל dalal \"be low\" Arabic compare Gesenius lexicon root H1809"
}
```


## [2026-09-05T20:13:13.719Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN dal/dallah ===\"; grep -n \"d-l-l\\|dalldh\\|dallah\" KLN_1966.txt | head; echo \"=== SKT Delilah ===\"; grep -n \"Delilah\" SKT.txt FSD_vol1.txt FSD_vol2.txt 2>/dev/null | head; echo \"=== FSD Daniel/Dan ===\"; grep -n \"Delilah\" FSD_vol*.txt | head"
}
```


### [2026-09-05T20:13:13.844Z] TOOL RESULT

```
=== KLN dal/dallah ===
2320:Almohades,  n.,  pi.,  members  of  a  Mohammedan sect,  founded  by  Mohammed  ibn  Abdallah.  — Lit.  ‘the  Unitarians’ ;  shortened  fr  *Al-movahides, from  Arab,  al-muwahhidun,  ‘they  who  profess the  unity  of  God’,  fr.  al-,  ‘the’,  and  active  part, of  the  2nd  conjugation  of  wahuda,  ‘he  was  alone’ whence  also  wahtd,  ‘solitary’ ;  rel.  to  Heb.  yahid, ‘only  one,  solitary’,  ydhad,  yahddw,  ‘together’, almond,  n.  —  ME.,  fr.  OF.  almande  (F.  amande), fr.  VL.  amandula,  fr.  L.  amygdala,  fr.  Gk. d;j.o-f8dXr|,  ‘almond’,  which,  according  to  H. Lewy,  Die  semitischen  Fremdworter  im  Griechi- schen,  pp.  25-26,  is  borrowed  from  Heb.  me- ghedh  El,  ‘divine  fruit’.  [The  ending  -ula  in  VL. amandula,  corresponding  to  the  Gk.  ending  -ixXt] in  ajjLuySdXT),  was  mistaken  for  the  dimin.  suff. (see  -ule)  and  consequently  dropped  in  OF.  al¬ mande,  E.  almond,  etc.]  The  n  before  the  d  is excrescent.  Cp.  amygdalate.  Cp.  also  mandorla. almoner,  n.  —  OF.  almosnier  (F.  aumonier),  fr. almosne  (F.  aumone),  fr.  VL.  * alemosina ,  fr. Eccles.  L.  eleemosyna.  See  alms, almonry,  n.  —  OF.  almosnerie  (F.  aumonerie),  fr. almosnier,  ‘almoner’.  See  prec.  word  and  -y  (re¬ presenting  OF.  -ie).
10723:Delilah,  n.,  the  mistress  of  Samson,  who  be¬ trayed  Samson  (Judges,  chapter  16).  —  Heb. Dllildh,  lit.  ‘delicate,  languishing,  amorous’, from  the  base  of  d-l-l,  ‘to  hang  down,  to  lan¬ guish’,  whence  also  dal,  ‘low,  poor,  thin’,  dalldh, ‘hair;  thrum’  (lit.  ‘that  which  hangs  down’); rel.  to  Akkad,  da/alu,  ‘to  be  weak  or  humble", Arab,  da! la,  ‘he  was  low  or  pliant’,  tadaldala, ‘it  hung  down,  dandled’,  Ethiop.  dated,  ‘hang¬ ing  curls’.
=== SKT Delilah ===
FSD_vol1.txt:40064:county.  Cal.,  on  the  north  side  of  the  Strait  of  Karquinea.  Bcn"Ja"mln/*Con.'/stant  Vi  bau'ja'mah'-koh'stuh';  2   bah*- be-night',  1   bi-nait';  2   be-nit\  rf.  1.  To  involve  in  dark-  zha'mSh'-cou 'staff',  Jean  Joseph  (ViolS45-s/j«l€02).  A ness,  whether  physical,  intellectual,  or  moral;  cover  with  „   French  painter;  Samson  and  Delilah. night  or  gloom.  ‘   2.  [Rare.]  To  overtake  with  night.  h   i°5  ^
=== FSD Daniel/Dan ===
FSD_vol1.txt:40064:county.  Cal.,  on  the  north  side  of  the  Strait  of  Karquinea.  Bcn"Ja"mln/*Con.'/stant  Vi  bau'ja'mah'-koh'stuh';  2   bah*- be-night',  1   bi-nait';  2   be-nit\  rf.  1.  To  involve  in  dark-  zha'mSh'-cou 'staff',  Jean  Joseph  (ViolS45-s/j«l€02).  A ness,  whether  physical,  intellectual,  or  moral;  cover  with  „   French  painter;  Samson  and  Delilah. night  or  gloom.  ‘   2.  [Rare.]  To  overtake  with  night.  h   i°5  ^
FSD_vol4.txt:59360:by  -violence,  wrench,  wring,  as,  he  wrested  the  cane  ,,Tlck,  1   rlk,  2   rlk.  tt  &   r(  (Prov  Eng  1   To  turn,  twist away,  we  wrested  the  victory’  from  their  grasp,  Delilah  ^rltk,  n   (Prov  Eng]  A   sprain
```


### [2026-09-05T20:13:21.506Z] TOOL RESULT

```
Web search results for query: "BDB Hebrew דלל dalal "be low" Arabic compare Gesenius lexicon root H1809"

Links: [{"title":"H1809 - dālal - Strong's Hebrew Lexicon (lxx)","url":"https://www.blueletterbible.org/lexicon/h1809/lxx/wlc/"},{"title":"H1809 - dālal - Strong's Hebrew Lexicon (kjv)","url":"https://www.blueletterbible.org/lexicon/h1809/kjv/wlc/0-1/"},{"title":"H1809 דּלל - Strong's Hebrew Lexicon","url":"https://studybible.info/strongs/H1809"},{"title":"H1800 - dal - Strong's Hebrew Lexicon (WLC)","url":"https://www.blueletterbible.org/lexicon/h1800/wlc/wlc/0-1/"},{"title":"H1800 - dal - Strong's Hebrew Lexicon (HNV)","url":"https://www.blueletterbible.org/lexicon/h1800/hnv/wlc/"},{"title":"Strong's Hebrew: 1800. דָּל (dal) -- Poor, weak, lowly","url":"https://biblehub.com/hebrew/1800.htm"},{"title":"H1800 - dal - Strong's Hebrew Lexicon (NIV)","url":"https://www.blueletterbible.org/lexicon/h1800/niv/wlc/0-1/"},{"title":"THE ENHANCED BROWN-DRIVER-BRIGGS HEBREW AND ENGLISH LEXICON","url":"https://hebrewcollege.edu/wp-content/uploads/2018/10/BDB.pdf"},{"title":"Brown%E2%80%93Driver%E2%80%93Briggs","url":"https://en.wikipedia.org/wiki/Brown%E2%80%93Driver%E2%80%93Briggs"},{"title":"%E1%B8%A4-M-D","url":"https://en.wikipedia.org/wiki/%E1%B8%A4-M-D"}]

Based on the search results, here's what I found regarding H1809 (דלל - dalal) in lexical resources:

## Strong's H1809 - דָּלַל (dālal)

The root is described as "a primitive root (compare H1802); to slacken or be feeble; figuratively, to be oppressed" with meanings including "bring low, dry up, be emptied, be not equal, fail, be impoverished, be made thin."

## BDB Lexicon Definition

The BDB provides more detailed meanings: "to hang, languish, hang down, be low" with subdivisions including "(Qal) to hang low, to be low, of distress (fig.), to languish, look weakly (of eyes)" and "(Niphal) to be brought low, be laid low".

## Related Forms

The adjective דַּל (dal) derives from H1809 and means "properly, dangling, i.e. (by implication) weak or thin: lean, needy, poor (man), weaker."

## Note on Gesenius and Comparative Semitic

The BDB lexicon is based on Gesenius as translated by Edward Robinson, by Francis Brown, with the cooperation of S. R. Driver and Charles A. Briggs, based on the 1906 edition. However, the search results do not contain specific information about Gesenius's comparative Arabic notes or a detailed comparison between the Hebrew and Arabic forms of this root.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:14:19.211Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD مدينة/دين ===\"; grep -n \"مدينة\\|( دين )\\|(دين)\" TAD_pages.txt | head -10; echo \"=== AFM دين ===\"; grep -n \"( دين )\\|(دين)\\|( مدينة )\" AFM_pages.txt | head -10; echo \"=== LKT medina/dîn ===\"; grep -n -i \"medina\\|Medîna\" LKT.txt | head -10"
}
```


### [2026-09-05T20:14:19.292Z] TOOL RESULT

```
=== TAD مدينة/دين ===
2432:                                   ‫باسممدينة فى بلاد اليونان مهدا الامبر‬
=== AFM دين ===
=== LKT medina/dîn ===
1888:[Vgl.  hehr,  hägag  'hin  und  hergehen, tanzen,  feiern']  'Pilger',  und  zwar  nach Mekka,  Medina  oder  Jerusalem.  Eine verlängerte  Form  ist  häggi,  besonders pers.  und  tk.,  sie  wird  als  Ehrentitel  für jeden,  der  Mekka  besucht  hat,  benutzt; hieraus  rum.  agiü,  agia  'Pilger',  agiaUc 'Pilgerfahrt  nach  Jerusalem',  bulg. hadzija,  serh. hacija  'Pilger';  engl,  anglo- ind.  hajß,  hadgee,  dlsch.  Hadschi;  frz. hadji  'Mekkapilger',  afrz.  aufage,  asp. a^/^ay'e 'Sarazenenführer'.  [Hobson-Jobson 408/4U9.  Devic  DEl  135.  E£,niilaz  155. ML  3988.
2085:[Vom  ar.  Vb.  hagara  'verlassen,  freund- schaftliche Beziehungen  abbrechen'] 'Auswanderung,  Abbruch  der  Beziehun- gen', insbesondere  der  W^egzug  des  Pro- pheten MUHAMMAD  von  Mekka  nach Medina,  der  nach  der  üblichen  Rech- nung am  16.  Juli  622  n.  Chr.  stattfand; die  muhammedanische  Zeitrechnung  be- ginnt mit  dieser  sog.  „Flucht",  die  aber gar  keine  Flucht  war  [s.  auch  C.  H. Becker,  Islamstudien  I:  Vom  Werden und  Wesen  der  islamischen  W^elt.  Leip- zig 1924.  S.  340];  hieraus  rum.  hegirä, frz.  hegire,  it.  egira,  sp.  hegira,  pg.  he- jira;  engl.  ndl.  hegira,  dtsch.  Hedschra  ; russ.  gidzra
```


## [2026-09-05T20:14:20.767Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT Dan/Daniel ===\"; grep -n \"^Daniel\\|Daniel,\" SKT.txt | head; echo \"=== WEB Daniel ===\"; grep -n \"^Daniel, n\\|Daniel, n\\.\" WEB_vol1.txt | head; echo \"=== WEB Dan, ===\"; grep -n \"Dan, n\\.\" WEB_vol1.txt | head -5"
}
```


### [2026-09-05T20:14:20.841Z] TOOL RESULT

```
=== SKT Dan/Daniel ===
=== WEB Daniel ===
=== WEB Dan, ===
49015:Dan, n. 1. in the Bible, the fifth son of Jacob.
49017:Dan, n. [ME.; OFr., dan, dans, from L. domi- nus, a master, lord.] master; sir: a title; as, Dan Cupid. [Archaic.]
```


## [2026-09-05T20:14:24.820Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49010,49020p' WEB_vol1.txt; echo \"=== Daniel ===\"; grep -n \"Daniel\" WEB_vol1.txt | head -8"
}
```


### [2026-09-05T20:14:24.899Z] TOOL RESULT

```
1, the fruit of a variety of the Prunus do- mestica, a small blue or purple plum: called also damask plum.
2. the tree that it grows on.
bitter or mountain damson; in botany, the Simaruba amara of Guiana and the West In- dies, whose bitter bark has medicinal quali- ties.
damson cheese; conserved damsons pressed into the shape of a cheese.
= dam stdne, the stone closing the front of the hearth in a blast furnace, to which the dam plate is attached.
Dan, n. 1. in the Bible, the fifth son of Jacob.
2. the tribe of Israel descended from him, which settled in northern Palestine.
Dan, n. [ME.; OFr., dan, dans, from L. domi- nus, a master, lord.] master; sir: a title; as, Dan Cupid. [Archaic.]
dan, n. [etym. unknown.] in mining, a small coal-carrying truck or sled.
n/a-@, n. in Greek mythology, the mother of Perseus: she was visited by Zeus in the form of a shower of gold. Also written Danaë.
dan/a-ide, 2. [named for the Danaides of myth-
=== Daniel ===
297:. Dutch . . Danish, Daniel . dative . . definite . derivation . Deuteronomy . dialect, dialectal . dictionary . diminutive . distributive . Doctor . dynamics
19051:I Samuel (I Kings) Daniel
19061:Old Testament Apocrypha I Esdras (III Esdras) Additions to Daniel, includ- IlEsdras(IVEsdras) ing the Song of the Three Tobit (Tobias) Holy Children, the Story of Judith Susanna, and the Idol Bel Additions to Esther and the Dragon Wisdom of Solomon Prayer of Manasses Ecclesiasticus I Maccabees (I Machabees) Baruch II Maccabees (II Machabees)
21046:| i bli/ish-ly, adv. in a bluish manner. ; | plavishaness, n. a small degree of pio oe | blun/dér, v.7.; blundered, pt. pp-, P aces | (Lie IME, blondie Daniels jo |
29698:Daniell cell; a cell in which the anode is zinc, the cathode copper. The zinc plate is sur- rounded by a porous cup filled with dilute sulfuric acid, or a zinc sulfate solution; the copper electrode is immersed in a solution of copper sulfate. 4 s i
29699:ravily cell; a modification of the Daniell call, in which the two fluids are separated by their difference in specific gravity, so that the porous septum is dispensed with.
46610:Crui’sde, Rob/in-sin, the hero of Daniel Defoe's novel Robinson Crusoe (1719), who is euended on an island, as the result of a ship-
70207:Fah/ren-heit (or fir’), a. [named from Gabriel Daniel Fahrenheit (1686-1736), G. physicist who devised the scale.] designating or of a thermometer that places the freezing point of
```


## [2026-09-05T20:14:26.086Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN din ===\"; grep -n \"dîn\\|dên\\|Religion\" HRN.txt | head -10; echo \"=== HUB den ===\"; grep -n \"dên\\|daêna\" HUB.txt | head -10"
}
```


### [2026-09-05T20:14:26.141Z] TOOL RESULT

```
=== HRN din ===
5343:597. dtn 'Glaube, Religion*.
5371:gegen *Glaube, Religion*, wie im Neup.
7653:880. kes 'Religion .
=== HUB den ===
```


## [2026-09-05T20:14:31.186Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5340,5375p' HRN.txt"
}
```


### [2026-09-05T20:14:31.275Z] TOOL RESULT

```
dem, det, y-andman (Hübschmann, No. 88).
kurd. LW. djm\ bei. LW. dem (80); afy. leina
'Pupille.
597. dtn 'Glaube, Religion*.
aw. dafwö-; phlv. diu bezw. den, paz. diu, dlmk,
arm. LW. den.
Allgemein entlehnt*'^).
598. dev 'Dämon, Teufel', dcväne Verrückt*, n^NDH (Jer.
29, 26.) 3).
aw. daeva- 'Dämon'; phlv. dev; ai. devd- 'Gott'.
599. dlvär 'Mauer, Wand'.
ap. ^deghavära- (vergl. gr. th/o^-, osk. felhuss).
Nöldeke (mündliche Mitteilung), unter der Voraus-
setzung, dass die np. Grundform '^devür lautete, was
die Zusammenstellung mit dev (8ähn. I, 24 Vers 86)
wahrscheinlich macht.
kurd. LW. dwär; wa;^. LW. dival^ sar. delvül 'Mauer,
Wand, Umwallung.
*) Der Majhül vokal ist nicht mehr in der Aussprache erhalten.
') College Jensen hat din sogar im Verdachte, babylonisch zu
sein. Er äussert sich in folgender WeiBe über diese Ansicht:
y»Üe(i)nim in der elamitisohen Version = framänä, de(i)Him-
dattira ibid. = framätaram, beides in der Inschr. von Naqs-i-Rustani.
iJeCOnhn unmöglich = daina, muss vielmehr = babyl. dinim sein,
welches in der babyl. Version der Achämonideninschriften vorkommt.
iHiiii = 'Gesetz, Recht* könnte sehr wohl persisches daina übersetzen,
das im Altpersischen nicht vorhanden. Ich halte es daher für möglich
(falls nichts Entscheidendes dagegen einzuwenden), dass daina durcli
elamitischcs den- mit assyr.-babyl. dlmi zu verknüpfen ist."
Vergl. Geldner's Etymologie von aw. dapiä- unter No. 413.
Jensen nimmt als Grundbedeutung *Recht, Gesetz' an, Geldner da-
gegen *Glaube, Religion*, wie im Neup.
^) Ursprünglich natürlich 'teuflisch , dämonisch*, vergl. Sahn. 1,
)5? Vers 408, 413.- 134 —
R
600. -m, zur Bezeichnung des Objekts dienende Partikel,
```


## [2026-09-05T20:14:40.577Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%D9%84%DB%8C%D9%84%D9%87/",
 "prompt": "Show the entries for دلیله — especially any فرهنگ معین or دهخدا section. Does it identify دلیله as the wife/mistress of Samson (شمشون) and/or as دلیلهٔ محتاله of the Arabian Nights? Quote the Persian text."
}
```


### [2026-09-05T20:14:47.247Z] TOOL RESULT

```
# دلیله Dictionary Entry Analysis

Based on the provided content, the dictionary entries **do identify دلیله as Samson's companion**, but they **do not mention the Arabian Nights character** (دلیلهٔ محتاله).

## Key Identifications:

**Dehkhoda Section:**
The entry describes her as "زنی زانیه بود که در وادی سورق...سبب شد که شمشون بدست دشمنانش گرفتار شود" (a woman of ill repute in the valley of Sorek who caused Samson to fall into his enemies' hands).

**Farhangi-ye Farsi Section:**
"زن درباری که سامسون را پس از قطع موهای وی...تسلیم فلسطینیان کرد" (the courtesan woman who, after cutting his hair, delivered Samson to the Philistines).

**Daneshname-ye Omumi Section:**
Provides the full narrative: "دلیله زنی در وادی سوررق که شمشون او را دوست می داشت" (Delilah was a woman in the valley of Sorek whom Samson loved).

## Notable Absence:

There is **no reference to the Arabian Nights character** in any section of this dictionary entry.
```


## [2026-09-05T20:14:54.137Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%DB%8C%D9%86/",
 "prompt": "Show the فرهنگ معین section for دین. How many homonyms are listed and what are their tags? Is there a دین [ع.] (ا.) meaning قرض/وام (debt) and a دین meaning آیین/کیش (religion)? Quote the Persian text of the Mo'in entries."
}
```


## [2026-09-05T20:14:57.298Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%AF%D9%8A%D9%86%D8%A9' --note 'page 138, root Dinu, node 4: Arabic madina < Aramaic mediHta' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D9%86' --note 'page 138, root Dinu, nodes 2-3: Arabic din judgment < Aramaic, din religion < MP den, dayn debt' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Delilah' --note 'page 138, root D.l.l, node 5: English Delilah < Hebrew Delilah' 2>&1 | tail -3"
}
```


### [2026-09-05T20:14:59.874Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for دین

Based on the content provided, the **Farhang-e Mo'in** section lists **2 homonyms** with distinct tags:

1. **دین [ع.] (ا.)** — "قرض، وام. ج. دیون" (debt, loan; plural: debts)

2. **دین [په.]** — Three meanings listed:
   - "۱ - آیین، کیش" (religion, faith)
   - "۲ - راه، روش" (path, way)
   - "۳ - نام روز بیست وچهارم..." (name of 24th day of month)

The first entry is marked as **[ع.]** (Arabic origin) and the second as **[په.]** (Persian origin), clearly distinguishing the two primary senses of the word.
```


### [2026-09-05T20:15:02.970Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8f5cdca53d2814a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59d6bb5c2203296e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cbe7f5b21e05ec57.txt
```


## [2026-09-05T20:15:35.052Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA 9810-9825 ===\"; sed -n '9812,9824p' AFA.txt; echo; echo \"=== AFA leaf of 9819 ===\"; python3 -c \"\nt=open('AFA.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Gerichtsbezirk')\nprint('leaf',t.count('\\f',0,i))\n\"; echo \"=== AKD dalalu ===\"; grep -n \"dalalu\\|dalâlu\\|schwach\\|demütig\" AKD.txt | head -5"
}
```


## [2026-09-05T20:15:36.342Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== RCH dain/madina ===\"; grep -nE \"dain,|dayn|madín|madin\" RCH.txt | head -12; echo \"=== RCH din ===\"; grep -nE \"^A +.{0,12}dín,\" RCH.txt | head -8"
}
```


### [2026-09-05T20:15:36.967Z] TOOL RESULT

```
=== AFA 9810-9825 ===
Dor. Kü-^üti^. 238 , 1 2 wird aus P^ entlehnt sein ; mit
Sicherheit lässt sich das TOn ^Go tds Grottesname ((jauh.
s. T. ^4>) sagen. Über die rerschiedenen unter dieser
Wurzel zusammengefallenen Wörter siehe jetzt auch Nöl-
deke ZDM6. XXXVIL 534 (Omndbedeutung ischnldig
.'■ • i
.♦ . -*.281
seia")]. Wohl aber ist niHO U^U^le > der Gerichtsbezirk".
Auch das eigenthamliche Schwanken der arabischen Tra-
dition in Bezug auf die Nisbabildung, die "Ljjüe neben
IajcVJ« gestattet , als wäre es eine Bildung ÄJUxi ; ferner die
Bildungen JiJu« nnd ^Jü0 (beide denominatir) sind Gründe,
um unseren Verdacht gegen die Echtheit des Wortes zu

=== AFA leaf of 9819 ===
leaf 311
=== AKD dalalu ===
```


### [2026-09-05T20:15:39.002Z] TOOL RESULT

```
=== RCH dain/madina ===
1521:unkind  usage.  Subjugation,  incarceration.  Contempt,  diadain, scorn.  Rough  unequal  ground.  A   male  toifeise. p   Abas^  Name  of  a   city.
3998:adyun^  (pi.  o\'  dayn)  Debts, p   dinnduh^  Tlie  rainbow,
5543:njundaky  BaMised,  broken  sifitlt,  brayed,  j^ed through,  perforated,  pierped.  Dug  out,  hollowed,^  excaoiAod. i(}andidany  To  plaster  (an  edifioe). r   Cm^j\  djmnky  A   wrinkle,  frown,^mttif^. or  contraction  of the  brows  (eitlier  from  age  or  anger).  Htitre^  malevolence, disdain,  anger,,  rage.  An  image.  ^   ^
7059:A   amadinij  The  two  blacln,  aii  dAlei  and  water
13408:A   ihanat^  (iv  of  Disdain,  contempt,  insult,  af- front. Hostility,  enmity,  treachery,  p   W   To  despise,
22387:AjJja^  tahklr^i^ii  of ySl^)  Despising,  contemning.  Scornful neglect,  disdain,  p   dolbpise,  to  hold  in  contempt.
40690:yadayny  Dexterous,  expeditious.  Dimishky  Damascus.  This city  was  the  general  residence  of  the  khalTfs  of  the  house  of Umayyah.  The  great  mosque  was  magnificent  beyond  de- scription, the  walls  being  of  the  finest  marble,  thereof  of  tin, and  the  inside  profusely  decorated  with  gold,  silver,  and  gems. During  the  convulsions  which  in  the  end  ruined  the  empire  of the  khalTfs,  it  had  many  changes  of  masters,  and  was  at  last  de- stroyed by  Tamerlane,  A.  D.  1400.  This  year,  which  was  re- markably unfortunate  for  the  Muslims,  is  distinguished  by  the word  kharahy  (Ruin),  tlie  four  letters  of  which  make
41638:A   dayn  (fifom  ^.*3),  Borrowing,  asking  in  loan.  Becom- ing a   debtor  or  a   creditor.  Lending.  Repaying.  Benefiting. Debt,  payable  with  interest  at  a   fixed  period  expressing
41639:an  indefinite  time).  Death  (as  a   debt  to  nature).  Any  thing not  present,  ^layhi  dayn^  Tie  is  a   debtor.
41640:daynun  lahu^  He  is  a   creditor.  ^   bt  dayni^  He  sold
41642:daynan^  He  gave  it  upon  credit.  ^   akhazahu  daynan^
41643:He  took  it  upon  credit,  p   dayn  knrdan^  To  contract
=== RCH din ===
```


## [2026-09-05T20:15:50.350Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AF%D9%84%DB%8C%D9%84%D9%87/' --note 'page 138, root D.l.l, node 4: Persian Dalileh = Samson mistress, Mo3in/Dehkhoda' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AF%DB%8C%D9%86/' --note 'page 138, root Dinu, node 3: Mo3in din [A.] debt vs din [Pahl.] religion' 2>&1 | tail -2"
}
```


### [2026-09-05T20:15:55.361Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9c4cbadd8d5dae64.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/efb8184626d05573.txt
```


## [2026-09-05T20:16:07.008Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:22:20.463Z] TOOL CALL #54: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-138.json",
 "content": "{\n  \"pdf_page\": 138,\n  \"book_page\": 108,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Dînu, Děnu, Dayânu\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Akkadian dīnu(m)/dēnu(m) 'judgment, verdict, law, lawsuit', dânu 'to judge', dayyānu 'judge' (Proto-Semitic *dyn / *dVn-; possibly itself < Sumerian di 'lawsuit')\",\n      \"note\": \"The root box is right in every part. Akkadian dīnu(m), with the Assyrian/late variant dēnu, means 'judgment, legal decision, law, lawsuit'; the verb is dânu 'to judge'; the agent noun is dayyānu 'judge'. Zimmern, Akkadische Fremdwörter (p. 24) prints exactly these three forms in exactly these senses, and Mo'in's footnote in Borhan-e Qate' (the passage Nourai cites as BQT:916) reproduces Zimmern almost word for word in Persian. Nourai's spellings Dînu / Děnu / Dayânu are the standard Assyriological ones with his own diacritics (ě = e, â = ā). The only thing not stated on the chart is that Akkadian itself may have taken the word from Sumerian di 'lawsuit' (Zimmern: 'viell. < sum. di').\",\n      \"note_fa\": \"ریشهٔ اکدی dīnu / dēnu «داوری، حکم، قانون، دعوی»، فعل dânu «داوری کردن» و dayyānu «داور، قاضی» ریشه‌ای است واقعی و پرکاربرد در متون بابلی و آشوری. زیمرن در «وام‌واژه‌های اکدی» (ص ۲۴) همین سه صورت را با همین معناها آورده و معین در حاشیهٔ برهان قاطع (همان صفحه‌ای که نورایی به آن ارجاع داده) عیناً همین مطلب را به فارسی نقل کرده است: «در زبان اخیر کلمات dīnu و dēnu بمعنی قانون و حق و داوری است، dânu بمعنی حکم کردن و dayyānu بمعنی قاضی است». پس ادعای نورایی دربارهٔ خودِ ریشه درست است؛ تنها نکتهٔ ناگفته آن است که خودِ واژهٔ اکدی شاید از سومری di «دعوی» گرفته شده باشد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D9%86\",\n        \"https://en.wiktionary.org/wiki/%D9%85%D8%AF%D9%8A%D9%86%D8%A9\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"BQT:916\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' with Mo'in's footnotes, vol. 2, form-feed leaf 376 of BQT_v2_pages.txt (printed page ≈ leaf+543, i.e. p. 916–919 within the ±3 uncertainty of that mapping), footnote to the headword «دین»: «اما دین در عربی … مأخوذ از زبانهای سامی است. تازیان این کلمه را مع‌الواسطه از زبان اکدی گرفته‌اند. در زبان اخیر کلمات dīnu و dēnu بمعنی قانون و حق و داوری است، dânu بمعنی حکم کردن و dayyānu بمعنی قاضی است.» This is verbatim Nourai's root box.\"},\n        {\"ref\": \"KLN:399\", \"status\": \"supports\", \"note\": \"Klein 1966, leaf 220 of KLN_1966.txt (leaf 221 carries the printed numerals 401–403, so leaf 220 = pp. 399–400), s.v. 'Dan': '…rel. to Heb. dīn, \\\"to judge\\\", Aram. dūn, dīn, Syr. dīn, Ugar. dn, Akkad. dānu, of s.m., Heb. and Aram. dīn, \\\"judgment\\\", dayyān, Akkad. dayānu, \\\"judge\\\"'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter, p. 24 (leaf 32 of AKD.txt)\", \"stance\": \"supports\", \"note\": \"'akk. dīnu, dēnu Gericht, Recht, Rechtssache, dânu richten, dajjānu Richter (viell. < sum. di)' — grep 'dinu|dajjänu|Richter' in AKD.txt, line 306.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 399 s.v. Dan\", \"stance\": \"supports\", \"note\": \"'Akkad. dānu … Akkad. dayānu, \\\"judge\\\"' — same set of Akkadian forms.\"},\n        {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 376, Mo'in's footnote s.v. دین\", \"stance\": \"supports\", \"note\": \"«کلمات dīnu و dēnu بمعنی قانون و حق و داوری است، dânu بمعنی حکم کردن و dayyānu بمعنی قاضی است».\"},\n        {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān, p. 132 n. 5 (leaf 149 of FVQ_pages.txt)\", \"stance\": \"supports\", \"note\": \"'…Zimmern, Akkad. Fremdw. 24, who derives it from Akk. de(i)nu' — Jeffery cites the very Zimmern page consulted above.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Aramaic\",\n          \"words\": \"dîn; medhînah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Aramaic dīn (verb dān / dīn, noun dīnā, emphatic state) 'to judge; judgment, lawsuit' and the derived noun mᵊdīnāh / emphatic mᵊdīntā 'jurisdiction, district of a governor, province' (m- prefix of place + the root d-y-n, so literally 'area of jurisdiction'). Zimmern (p. 24) makes both Aramaic and Hebrew borrowings from Akkadian, 'wahrsch., allerdings schon in früher Zeit' (probably, though already at an early date) — i.e. the Aramaeans took dīn from the Akkadian legal vocabulary of Mesopotamia during the Neo-Assyrian/Neo-Babylonian period, when Aramaic was becoming the chancery language of the empire, and built mᵊdīntā on it as an administrative term ('satrapy, province' in Ezra/Daniel Aramaic). Nourai's gloss 'to rule' for dīn is loose: the verb means 'to judge, give a verdict', and the sense 'rule' is secondary (a judge rules a district). The form he writes, medhînah, is with the -āh ending the Hebrew shape; the strictly Aramaic emphatic is mᵊdīntā, which is also the form Klein and Zimmern print. The route Akkadian → Aramaic itself is only 'probable' — some Semitists treat the whole family as inherited Proto-Semitic *dyn rather than borrowed.\",\n          \"derivation_fa\": \"در آرامی dīn (فعل dān/dīn) به معنی «داوری کردن، حکم دادن» و مشتقِ آن mᵊdīnāh / mᵊdīntā «حوزهٔ داوری، ولایت، استان» است که از پیشوند مکان‌ساز m- و ریشهٔ d-y-n ساخته شده. زیمرن (ص ۲۴) این واژه را وام‌واژه‌ای می‌داند که آرامیان و عبرانیان «هر دو، و آن هم در دورهٔ کهن» از اکدی گرفته‌اند؛ زمینهٔ تاریخی‌اش دورهٔ نو‌آشوری و نو‌بابلی است که آرامی زبان دیوانی امپراتوری شد و mᵊdīntā در آرامیِ کتاب دانیال و عزرا به معنی «ساتراپی، ولایت» به کار رفت. دو نکتهٔ کوچک: معنایی که نورایی برای dīn آورده («to rule») دقیق نیست و باید «داوری کردن» باشد؛ و صورتی که او با پایانهٔ ‑āh نوشته (medhînah) در حقیقت شکل عبری است، حال آنکه صورت مضافِ آرامی mᵊdīntā است. با این حال ادعای نورایی در اصل درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D8%AF%D9%8A%D9%86%D8%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:399\", \"status\": \"supports\", \"note\": \"Klein leaf 220 s.v. Dan: 'Aram. dūn, dīn … Heb. and Aram. dīn, \\\"judgment\\\" … Aram. midhīnāh, \\\"district, province\\\" (whence Heb. medhīnāh, Syr. mdhittā, Arab. madīnah, \\\"city\\\"), orig. \\\"district of jurisdiction\\\".'\"},\n            {\"ref\": \"BQT:916\", \"status\": \"supports\", \"note\": \"Mo'in's footnote (vol. 2 leaf 376): «در عبری و آرامی dīn … بمعنی قانون و حق و داوری است، dayyān … بمعنی حاکم و قاضی».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AKD\", \"where\": \"Zimmern p. 24 (leaf 32)\", \"stance\": \"supports\", \"note\": \"'> wahrsch., allerdings schon in früher Zeit, hebr. dīn u. aram. dīn, dīnā Gericht, Recht, Rechtssache, dān richten, dajjān, dajjānā Richter, madīntā Stadt (eig. Gerichtsbezirk)'. Note the Aramaic form is madīntā/mᵊdīntā, not -āh.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter im Arabischen, p. 281 (leaf 311 of AFA.txt)\", \"stance\": \"supports\", \"note\": \"'Wohl aber ist מדינה … \\\"der Gerichtsbezirk\\\"' — Fraenkel explicitly analyses the Aramaic noun as 'the judicial district'.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 399 s.v. Dan\", \"stance\": \"supports\", \"note\": \"'Aram. midhīnāh, \\\"district, province\\\" … orig. \\\"district of jurisdiction\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"dîn 2; yawm-ed-dîn; dayn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic دِين dīn 'judgment, requital' (as in يَوْمُ الدِّينِ yawm al-dīn 'the Day of Judgment', Qurʾān 1:3, 82:17-18) is a borrowing from Aramaic/Syriac dīnā 'judgment', specifically from the Jewish-Aramaic and Syriac Christian usage of dīnā for the eschatological judgment. Jeffery (Foreign Vocabulary, p. 132) is unambiguous: 'we have here two separate words of different origin. (i) In the sense of religion the word is a borrowing from Iranian … (ii) In the sense of Judgment it is a borrowing from the Aramaic. Thus we find in common use the Rabbinic דין, Syr. dīnā and Mand. dīn, all meaning judgment and, indeed, the judgment of the last day.' Zimmern (p. 24) traces the same chain one step further back: 'aus aram. > arab. dīn, äth. dain Gericht, arab. dayyān Richter'. دَيْن dayn 'debt' belongs to the same borrowed base but, as Jeffery says of dayn and tadāyantum on p. 131, 'these, however, are later developments of the word within Arabic' — Arabic recast the loan as a native triliteral root د-ي-ن and generated the whole 'obligation/debt/creditor' family from it (madīn 'debtor', dāʾin 'creditor'). So dayn is Aramaic-derived only mediately, through the Arabicised root. Nourai's chart drawing all three in one Arabic box under Aramaic is therefore right in substance.\",\n          \"derivation_fa\": \"واژهٔ عربی «دین» به معنی «جزا، داوری» — چنانکه در «یومُ الدّین» (قرآن، فاتحه ۳ و انفطار ۱۷–۱۸) — وام‌واژه‌ای است از آرامی/سریانی dīnā «داوری، حکم». جفری در «واژگان دخیل در قرآن» (ص ۱۳۲) صریح می‌گوید که در عربی دو «دین» جداگانه داریم: «دین» به معنی کیش که از ایرانی (پهلوی dēn) گرفته شده، و «دین» به معنی جزا و داوری که از آرامی وام گرفته شده و در کاربرد ربّی و سریانی و مندایی به‌ویژه دربارهٔ داوریِ روز واپسین به کار می‌رفته. زیمرن (ص ۲۴) نیز همین زنجیره را دارد: «از آرامی > عربی dīn، حبشی dain، عربی dayyān قاضی». اما «دَین» به معنی وام و بدهی، به گفتهٔ جفری (ص ۱۳۱)، «تحولی متأخر و درون‌عربی» است: عربی این وام‌واژه را همچون ریشهٔ سه‌حرفیِ بومی د-ی-ن بازتحلیل کرد و از آن مدین و دائن و تداین ساخت. بنابراین ترسیم نورایی در کل درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:916\", \"status\": \"supports\", \"note\": \"Mo'in's footnote (vol. 2 leaf 376): «دین و دیّان از آرامی وارد زبان عربی شده».\"},\n            {\"ref\": \"FVQ:131\", \"status\": \"supports\", \"note\": \"Jeffery p. 131 (leaf 148 of FVQ_pages.txt): 'In the Qur'an we find also دين a debt, that which one owes (cf. iv, 12, 13; ii, 282) … besides the verb تداينتم \\\"to become debtors to one another\\\" (ii, 282). These, however, are later developments of the word within Arabic.' — supports both the 'judgment' and the 'debt' words being at this reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"p. 132 (leaf 149)\", \"stance\": \"supports\", \"note\": \"'As a matter of fact we have here two separate words of different origin. (i) In the sense of religion the word is a borrowing from Iranian … (ii) In the sense of Judgment it is a borrowing from the Aramaic.' — exactly the NOTE Nourai attaches to this node.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p. 24 (leaf 32)\", \"stance\": \"supports\", \"note\": \"'aus aram. > arab. dīn, äth. dain Gericht, arab. dajjān Richter, madīnat Stadt'.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie, no. 597 (p. 133), footnote 2\", \"stance\": \"partial\", \"note\": \"Horn reports Jensen's suspicion that even the *religion* word is Babylonian: 'de(i)nim in der elamitischen Version = framānā … muss vielmehr = babyl. dīnim sein … dass daina durch elamitisches den- mit assyr.-babyl. dīnu zu verknüpfen ist.' A minority view that would collapse Nourai's two roots into one.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 399 s.v. Dan\", \"stance\": \"supports\", \"note\": \"'(whence Heb. medhīnāh, Syr. mdhittā, Arab. madīnah, \\\"city\\\")' — Klein routes the Arabic reflexes of this root through Aramaic.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"dîn 2 «دین ۲»; dayn «دین ۳»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both Persian items are learned Arabic borrowings, not inherited Iranian words, and both are taken over in the classical period through Qurʾānic and fiqh vocabulary. دَین dayn 'debt' is beyond doubt: Mo'in's Farhang-e Farsi tags it «دین: [ع.] (ا.) قرض، وام؛ ج. دیون» — Arabic loan, plural دیون — and Richardson (RCH, s.v.) lists the Persianised phrase دین کردن dayn kardan 'to contract a debt'. The second item is where the chart overstates: «دین ۲: judgment day» is not a lexicalised Persian word. Mo'in's dictionary knows only two homonyms, دین [ع.] 'debt' and دین [په.] 'religion, faith, way' (from Pahlavi dēn, Nourai's root 'Dheye'); the 'judgment' sense survives in Persian only inside the borrowed Arabic phrase یوم‌الدین / روز دین in religious prose, not as an independent entry. So the node is right that a Persian دین goes back through Arabic to Aramaic — but that is the debt word; the 'judgment day' headword with its own number is Nourai's own arrangement rather than a lexicographer's.\",\n          \"derivation_fa\": \"هر دو واژهٔ این گره وام‌واژهٔ عربی‌اند و از راه زبان دین و فقه به فارسی درآمده‌اند، نه میراث ایرانی. دربارهٔ «دَین» به معنی قرض تردیدی نیست: معین در فرهنگ فارسی می‌آورد «دین: [ع.] (اِ.) قرض، وام؛ ج. دیون»، و ریچاردسن ترکیب فارسیِ «دین کردن» را در معنی «وام گرفتن» ثبت کرده است. اما «دین ۲» به معنی «روز جزا» واژهٔ مستقلی در فارسی نیست: معین تنها دو هم‌آوا می‌شناسد، «دین [ع.] قرض» و «دین [په.] آیین، کیش» (از پهلوی dēn که ریشهٔ جداگانهٔ «Dheye» نورایی است). معنی «داوری» در فارسی فقط در همان ترکیب عربیِ «یوم‌الدین» و «روز دین» در نثر دینی به کار می‌رود. پس ادعای نورایی با احتیاط پذیرفتنی است: راهِ عربی ← فارسی درست است، ولی سرواژهٔ «دین ۲» ساختهٔ خود اوست نه مدخل فرهنگ‌نویسان.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%AF%DB%8C%D9%86/\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:148\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989) — refs_online.json records no digital copy on any permitted platform (re-searched 2026-09); catalogue record only.\"},\n            {\"ref\": \"MON:1597\", \"status\": \"partial\", \"note\": \"The six-volume Mo'in with its page numbers is not on disk; the two-volume Adena abridgement (MON_2vol_Adena_v1_djvu.txt, line 64673) and vajehyab/abadis both give «دین: [ع.] (ا.) قرض، وام؛ ج. دیون» and a separate «دین: [په.] آیین، کیش», i.e. Mo'in supports the debt word as an Arabic loan but does not carry a Persian headword 'judgment day'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. دین (2-vol. abridgement line 64673; abadis.ir فرهنگ معین section)\", \"stance\": \"partial\", \"note\": \"«دین: [ع.] (ا.) قرض، وام؛ ج. دیون» / «دین: [په.] ۱- آیین، کیش ۲- راه، روش» — two homonyms only, no 'judgment day' headword.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dict., s.v. dayn (RCH.txt lines 41638-41643)\", \"stance\": \"supports\", \"note\": \"'A dayn … Debt, payable with interest at a fixed period … p dayn kardan, To contract [a debt]' — the Arabic word with an established Persian compound verb.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 2 leaf 376, headword دین\", \"stance\": \"supports\", \"note\": \"«و بفتح اول هم در عربی فرض و وام را گویند» — Borhan itself notes the Arabic 'debt' sense beside the Persian religion word.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"madîneh; tamaddon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic مَدِينَة madīna 'city' is a borrowing of Aramaic mᵊdīntā 'jurisdiction, province' (originally 'district of jurisdiction', from d-y-n 'to judge'), with the regular substitution of the Arabic feminine -at for the Aramaic emphatic -tā; the sense narrowed from 'province' to 'walled town', a shift already complete in pre-Islamic Arabia (whence Yathrib became al-Madīna after the hijra of 622). Klein states the route explicitly at the cited page, and Zimmern p. 24 has 'aus aram. > arab. … madīnat Stadt'. Fraenkel (p. 281) gives the decisive internal argument: the Arabic grammarians' own hesitation over the nisba (madanī beside madīnī, as if the word were a maf'ila formation) and the fact that madanī and tamaddun are both denominative are 'Gründe, um unseren Verdacht gegen die Echtheit des Wortes zu [bestärken]' — reasons to doubt that the word is genuinely Arabic. تَمَدُّن tamaddun 'civilization' is thus not directly from Aramaic but is a Form V verbal noun built inside Arabic on the back-formed root م-د-ن extracted from madīna (Wiktionary: 'the root م د ن is denominal'); it is a nineteenth-century nahḍa coinage in its modern sense.\",\n          \"derivation_fa\": \"واژهٔ عربی «مدینة» وام‌واژه‌ای است از آرامی mᵊdīntā «حوزهٔ داوری، ولایت» (از ریشهٔ d-y-n «داوری کردن»)، با جانشینیِ منظمِ پایانهٔ مؤنث عربی ‑ة به‌جای پایانهٔ مضافِ آرامی ‑tā؛ معنی آن از «ولایت» به «شهرِ حصاردار» محدود شده و این تحول پیش از اسلام کامل شده بود، چنانکه پس از هجرت (۶۲۲ م) یثرب «المدینه» نام گرفت. کلاین در همان صفحهٔ ۳۹۹ همین راه را می‌کشد و زیمرن (ص ۲۴) نیز «از آرامی > عربی madīnat شهر». فرنکل (ص ۲۸۱) دلیل درون‌زبانی قاطعی می‌آورد: تردید خود نحویان عرب در نسبت این واژه (مدنی در کنار مدینی) و اینکه «مدنی» و «تمدّن» هر دو مشتقِ اسمی (denominative) اند، نشانهٔ عربی‌نبودنِ اصلِ واژه است. پس «تمدّن» مستقیماً از آرامی نیامده، بلکه مصدر باب تفعّل است که درونِ عربی از ریشهٔ برساختهٔ م-د-ن — که خود از «مدینه» انتزاع شده — ساخته شده، و معنی امروزی‌اش زادهٔ دورهٔ نهضت در سدهٔ نوزدهم است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D8%AF%D9%8A%D9%86%D8%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:399\", \"status\": \"supports\", \"note\": \"Klein leaf 220 s.v. Dan: 'Aram. midhīnāh, \\\"district, province\\\" (whence Heb. medhīnāh, Syr. mdhittā, Arab. madīnah, \\\"city\\\"), orig. \\\"district of jurisdiction\\\".' Klein does not mention tamaddun.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFA\", \"where\": \"Fraenkel p. 281 (leaf 311 of AFA.txt)\", \"stance\": \"supports\", \"note\": \"'…ferner die Bildungen مدني und تمدن (beide denominativ) sind Gründe, um unseren Verdacht gegen die Echtheit des Wortes zu [bestärken]' — Fraenkel treats madīna as an Aramaic loan and madanī/tamaddun as inner-Arabic denominatives.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p. 24 (leaf 32)\", \"stance\": \"supports\", \"note\": \"'aus aram. > arab. dīn … madīnat Stadt, wie auch späthebr. mᵊdīnā'.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba (grep '( مدينة )' in AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"No entry — Addi Shir lists only Persian loans in Arabic, and madīna is not among them, which is itself consistent with an Aramaic (not Persian) source.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"madîneh «مدینه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian مدینه madīne is the Arabic مَدِينَة taken over unchanged except for the regular Persian treatment of Arabic tāʾ marbūṭa as -e (written ه), and it entered Persian with Islam, overwhelmingly as the proper name of the Prophet's city (al-Madīna, formerly Yathrib) rather than as a common noun — Persian's ordinary word for 'city' remained شهر šahr, from Middle Persian šahr. The chart's extra forms are all further Arabic borrowings of the same denominal root م-د-ن: مدنی madanī 'civic, civil' (nisba to Medina; Mo'in: «مدنی: [ع.] (ص نسب.) منسوب به مدینه … شهرنشین»), مداین Madāʾin, the broken plural of madīna and hence the Arabic name of Ctesiphon/Tīsfūn, تمدّن tamaddon 'civilization' and متمدّن motamadden 'civilized' — the last two being late-nineteenth-century loans of the nahḍa vocabulary into the Persian of the constitutional era. None of these is formed on Persian soil; Persian imported each ready-made from Arabic.\",\n          \"derivation_fa\": \"«مدینه» در فارسی همان «مدینة» عربی است که تنها تغییرِ منظمِ تاء مربوطه به «ـه» فارسی را پذیرفته، و با اسلام وارد فارسی شده — آن هم بیشتر همچون نامِ خاصِ شهر پیامبر (المدینه، یثربِ پیشین) نه واژه‌ای عام؛ زیرا واژهٔ عادیِ فارسی برای «شهر» همان «شهر» از فارسی میانهٔ šahr باقی ماند. صورت‌های افزودهٔ نمودار همگی وام‌واژه‌های عربی از همان ریشهٔ اسمیِ م-د-ن‌اند: «مدنی» (نسبت به مدینه؛ معین: «مدنی: [ع.] (ص نسب.) منسوب به مدینه … شهرنشین»)، «مداین» جمع مکسّرِ مدینه و از همین رو نام عربیِ تیسفون، و «تمدّن» و «متمدّن» که وام‌گیری‌های متأخرِ دورهٔ مشروطه از واژگان نهضتِ عربی‌اند. هیچ‌یک ساختهٔ فارسی نیست و همه آماده از عربی گرفته شده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D8%AF%D9%8A%D9%86%D8%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi, s.v. مدنی (2-vol. abridgement MON_2vol_Adena_v2_djvu.txt line 51900): «مدنی: [ع.] (ص نسب.) منسوب به مدینه. منسوب و مربوط به مدینه (شهر معروف) … شهرنشین» — with the note that «مدن» is the plural of مدینه. The Arabic tag [ع.] is Mo'in's, so the loan direction Arabic→Persian is his.\"},\n            {\"ref\": \"FVA:379\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi has no digital copy (refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. مدنی، مدنیت (2-vol. abridgement lines 51900-51907)\", \"stance\": \"supports\", \"note\": \"«مدنی: [ع.] … منسوب به مدینه»؛ «مدنیت: [ع.] (مص جد.)» — Mo'in marks the whole family Arabic, and مدنیت as a modern coinage (مص جد. = new verbal noun).\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel p. 281\", \"stance\": \"supports\", \"note\": \"Same passage as node 4: مدني and تمدن are denominative formations inside Arabic, so Persian received them from Arabic, not from Aramaic.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi (grep مدینه in ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"No entry — Aryanpur covers only Indo-European roots of Persian, so an Aramaic-via-Arabic loan is correctly absent.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Hebrew\",\n          \"words\": \"dîn; dân; Dânî-ěl\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Hebrew words themselves are exactly as the chart gives them: dīn 'to judge; judgment' (Gen. 15:14, Ps. 9:9), the personal name דָּן Dān, which Klein glosses 'lit. \\\"he who judges\\\"' (Genesis 30:6 puns on it: dānannī ʾElōhīm 'God has judged me'), and דָּנִיֵּאל Dānīʾēl 'God is my judge' = dān + ʾēl (Nourai's ☞Layh cross-reference is to his root for ʾēl 'God'). What is not right is the arrow: the chart hangs Hebrew under Aramaic, whereas both Klein and Zimmern place Hebrew and Aramaic side by side as parallel recipients. Zimmern p. 24: Akkadian dīnu '> wahrsch., allerdings schon in früher Zeit, hebr. dīn u. aram. dīn, dīnā' — Hebrew directly, at an early date, not through Aramaic; and Klein's 'Dan' entry lists Heb. dīn, Aram. dūn/dīn, Syr. dīn, Ugar. dn and Akkad. dānu as a set of cognates, not a chain. The Ugaritic evidence (dn 'to judge', and the epic figure Dnil = Danel) shows the root in West Semitic centuries before Aramaic could have mediated anything. The correct picture is Akkadian (or common Proto-Semitic *dyn) → Hebrew and Aramaic in parallel; only the Arabic branch is genuinely Aramaic-mediated. Note also that the strict Hebrew noun 'judge' is dayyān, not dān; dān is the participle/PN.\",\n          \"derivation_fa\": \"خودِ واژه‌های عبری همان است که نمودار می‌گوید: dīn «داوری کردن؛ داوری» (پیدایش ۱۵:۱۴، مزامیر ۹:۹)، نامِ خاصِ דָּן Dān که کلاین آن را «آنکه داوری می‌کند» معنی می‌کند (و پیدایش ۳۰:۶ بر همین نام جناس می‌سازد)، و דָּנִיֵּאל Dānīʾēl «خدا داور من است» از dān + ʾēl. ایراد در جهتِ پیکان است: نورایی گرهِ عبری را زیرِ آرامی گذاشته، حال آنکه هم کلاین و هم زیمرن عبری و آرامی را در کنارِ هم و هر دو را وام‌گیرندهٔ مستقیم می‌دانند. زیمرن (ص ۲۴): اکدی dīnu «> احتمالاً، و آن هم در دورهٔ کهن، عبری dīn و آرامی dīn, dīnā». گواهیِ اوگاریتی (dn «داوری کردن» و نامِ حماسیِ Dnil) نیز نشان می‌دهد این ریشه قرن‌ها پیش از آنکه آرامی بتواند واسطه شود در سامیِ غربی حاضر بوده. پس تصویرِ درست این است: اکدی (یا سامیِ آغازینِ مشترک *dyn) ← عبری و آرامی به‌موازات، و تنها شاخهٔ عربی است که به‌راستی از راه آرامی آمده. افزون بر این، اسمِ «داور» در عبری dayyān است نه dān.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:399\", \"status\": \"partial\", \"note\": \"Klein leaf 220 s.v. Dan has every Hebrew form Nourai gives ('Heb. Dan, lit. \\\"he who judges\\\", rel. to Heb. dīn, \\\"to judge\\\" … Cp. Daniel, Dinah'), and Daniel at leaf 221 (p. 401): 'Heb. Dānīʾēl, lit. \\\"God is my judge\\\", rel. to Akkad. Dāni-ilu.' But Klein relates Hebrew to Akkadian directly and lists Aramaic as a co-ordinate cognate, not as the source of Hebrew.\"},\n            {\"ref\": \"BQT:916\", \"status\": \"partial\", \"note\": \"Mo'in's footnote (vol. 2 leaf 376) puts Hebrew and Aramaic together — «در عبری و آرامی dīn … بمعنی قانون و حق و داوری است» — and derives only the Arabic from Aramaic («دین و دیّان از آرامی وارد زبان عربی شده»); it does not derive Hebrew from Aramaic.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AKD\", \"where\": \"Zimmern p. 24 (leaf 32)\", \"stance\": \"partial\", \"note\": \"'> wahrsch., allerdings schon in früher Zeit, hebr. dīn u. aram. dīn, dīnā' — Hebrew and Aramaic in parallel from Akkadian; contradicts the chart's Aramaic→Hebrew arrow while confirming the words.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 399 s.v. Dan; p. 401 s.v. Daniel; s.v. Dinah (leaf 244)\", \"stance\": \"supports\", \"note\": \"'Dinah … Heb. Dīnāh, lit. \\\"judgment\\\", fr. dīn, \\\"to judge\\\". See Dan, PN.' — confirms the Hebrew root and its onomastics.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Dan (WEB_vol1.txt line 49015)\", \"stance\": \"supports\", \"note\": \"'Dan, n. 1. in the Bible, the fifth son of Jacob. 2. the tribe of Israel descended from him' — confirms the biblical referent (Klein's 'son of Jacob and Bilhah').\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"Dan, Daniel\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Dan and Daniel are the biblical names carried into English along the standard scriptural route: Hebrew דָּן Dān and דָּנִיֵּאל Dānīʾēl → Septuagint Greek Δάν, Δανιήλ (3rd–2nd c. BCE) → Vulgate Latin Dan, Danihel → Old English/Middle English biblical usage; Daniel is recorded as an English given name from the 12th–13th centuries and became common after the Reformation put Old Testament names into general use. Klein (leaf 221 = p. 401) gives the Hebrew source and gloss for Daniel directly, and Webster's records Dan as the biblical son of Jacob. The node carries no refs in the book (refs=None), which is normal for Nourai's terminal English boxes where the preceding Hebrew box is documented. Caution for the reader: the homonymous archaic English title Dan 'master, sir' (Dan Cupid) is unrelated — Webster's derives it from Old French dan, from Latin dominus.\",\n          \"derivation_fa\": \"«Dan» و «Daniel» انگلیسی همان نام‌های کتاب مقدس‌اند که از راهِ معمولِ متونِ دینی به انگلیسی رسیده‌اند: عبری דָּן و דָּנִיֵּאל ← یونانیِ ترجمهٔ سبعینیه Δάν و Δανιήλ (سدهٔ سوم–دوم پیش از میلاد) ← لاتینِ ولگات Dan و Danihel ← کاربردِ کتاب‌مقدسی در انگلیسیِ کهن و میانه؛ Daniel از سدهٔ دوازدهم–سیزدهم همچون نامِ کوچک در انگلستان ثبت شده و پس از نهضتِ اصلاح دینی که نام‌های عهد عتیق را رواج داد فراگیر شد. کلاین (ص ۴۰۱) ریشهٔ عبری و معنی «خدا داور من است» را می‌آورد و وبستر «Dan» را پسر یعقوب می‌داند. این گره در کتاب ارجاعی ندارد (refs=None) که در جعبه‌های پایانیِ انگلیسیِ نورایی عادی است. یک هشدار: «Dan» به معنی «سرور، جناب» در انگلیسیِ کهنه (Dan Cupid) هم‌آواست و بی‌ربط؛ وبستر آن را از فرانسهٔ کهن dan و لاتین dominus می‌گیرد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The book gives no reference for this node; the supporting citation is the parent Hebrew box (KLN:399), which was checked and does cover Dan and Daniel.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 401 s.v. Daniel (leaf 221 of KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'Daniel, masc. PN., the hero of the Book of Daniel (Bible). — Heb. Dānīʾēl, lit. \\\"God is my judge\\\", rel. to Akkad. Dāni-ilu. For the first element see Dan, PN., for the second see El.'\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Dan (line 49015-49017)\", \"stance\": \"supports\", \"note\": \"'Dan, n. 1. in the Bible, the fifth son of Jacob…' and, separately, 'Dan, n. [ME.; OFr., dan, dans, from L. dominus, a master, lord.]' — confirms the biblical name and flags the unrelated homonym.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary (grep 'Daniel' in FSD_vol1-4)\", \"stance\": \"silent\", \"note\": \"Only incidental occurrences (painters', inventors' names); no separate etymological entry for the PN in the OCR.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"D.l.l\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Semitic root d-l-l 'to hang down, to be low, to languish' (Hebrew דָּלַל dālal, דַּל dal 'low, poor, thin'; Akkadian dalālu 'to be weak, humble')\",\n      \"note\": \"The root box reproduces Klein p. 419 word for word: 'from the base of d-l-l, \\\"to hang down, to languish\\\", whence also dal, \\\"low, poor, thin\\\", dallāh, \\\"hair; thrum\\\" (lit. \\\"that which hangs down\\\")'. BDB gives the same for Hebrew dālal: 'to hang, languish, hang down, be low'. Calling it 'Semitic' rather than Hebrew is justified by Klein's own comparanda (Akkadian dalālu, Ethiopic dalal 'hanging curls'). The trouble on this page is not the root but the Arabic branch hung from it — see node 1.\",\n      \"note_fa\": \"جعبهٔ ریشه عیناً همان چیزی است که کلاین در ص ۴۱۹ نوشته: «از ستاکِ d-l-l به معنی آویختن و سست شدن، که dal «پست، تهیدست، نازک» و dallāh «مو، ریشهٔ پارچه» (لفظاً: آنچه آویزان است) نیز از آن است». فرهنگ براون-درایور-بریگز نیز برای عبریِ dālal همین را می‌آورد: «آویختن، سست شدن، پست بودن». برچسبِ «سامی» به‌جای «عبری» با شواهدِ خودِ کلاین (اکدی dalālu، حبشی dalal) موجه است. اشکال این صفحه نه در ریشه، بلکه در شاخهٔ عربی است که از آن آویخته شده — نگاه کنید به گرهِ ۱.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Delilah\"],\n      \"ref_check\": [\n        {\"ref\": \"KLN:419\", \"status\": \"supports\", \"note\": \"Klein 1966, leaf 231 of KLN_1966.txt (the leaf carries the printed numerals 420, 421, so the entry begins on p. 419), s.v. Delilah: '…from the base of d-l-l, \\\"to hang down, to languish\\\", whence also dal, \\\"low, poor, thin\\\", dallāh, \\\"hair; thrum\\\" (lit. \\\"that which hangs down\\\"); rel. to Akkad. dalālu, \\\"to be weak or humble\\\", Arab. dalla, \\\"he was low or pliant\\\", tadaldala, \\\"it hung down, dandled\\\", Ethiop. dalal, \\\"hanging curls\\\".'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"p. 419 s.v. Delilah\", \"stance\": \"supports\", \"note\": \"Quoted above — the source of Nourai's root box, gloss included.\"},\n        {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter (grep 'dalalu|schwach|demütig' in AKD.txt)\", \"stance\": \"silent\", \"note\": \"No entry: Zimmern lists only Akkadian words that were borrowed by other Semitic languages, and dalālu is inherited, not a loan.\"},\n        {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Delilah (WEB_vol1.txt line 51452)\", \"stance\": \"supports\", \"note\": \"'Delilah, n. [Heb. delila[h], lit., delic[ate]…]' — the same base and gloss, independently of Klein.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"dz.l.l, z.l.l\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai's 'dz.l.l' is his transliteration of Arabic ذ-ل-ل (ḏāl), the root of ذَلَّ ḏalla 'to be lowly, abased' and ذَلِيل ḏalīl — chosen because it is the source of the Persian word in the next box, which Persian pronounces with z (hence his alternative 'z.l.l'). But that is not the root Klein cites at the page Nourai references. Klein p. 419 compares Hebrew d-l-l with 'Arab. dalla, \\\"he was low or pliant\\\", tadaldala, \\\"it hung down, dandled\\\"' — Arabic د-ل-ل with dāl, the root of تدلدل tadaldala 'to dangle'. The two Arabic roots are distinct and the regular Proto-Semitic correspondences keep them apart: PS *d gives Hebrew d, Aramaic d, Arabic d (so Hebrew dālal ↔ Arabic dalla), whereas PS *ḏ gives Hebrew z, Aramaic d, Arabic ḏ (so Arabic ḏalla corresponds to Hebrew זָלַל zālal 'to be light, worthless, despised', Lam. 1:11, not to dālal). Wiktionary files ذلّ under its own Semitic root ذ ل ل, separate from د ل ل. Older lexicographers (Gesenius, and BDB in its comparative notes) did sometimes cite Arabic ḏalla under Hebrew dālal on semantic grounds, and Aramaic — where both PS *d and *ḏ fall together as d — makes the confusion easy; so the chart is not arbitrary. But as drawn, the node makes Persian ذلیل a relative of Delilah, and by the sound laws it is not. Modern view: Semitic *d-l-l (Hebrew dālal, Arabic dalla, Akkadian dalālu) and Semitic *ḏ-l-l (Arabic ḏalla > Persian ذلیل, Hebrew zālal) are two roots.\",\n          \"derivation_fa\": \"آنچه نورایی «dz.l.l» نوشته آوانگاریِ اوست از ریشهٔ عربیِ ذ-ل-ل (با ذال)، یعنی ریشهٔ «ذَلَّ» و «ذَلیل»؛ و صورت دومِ «z.l.l» را از آنجا آورده که فارسی‌زبانان ذال را ز تلفظ می‌کنند. اما این همان ریشه‌ای نیست که کلاین در صفحهٔ مورد ارجاع آورده است: کلاین در ص ۴۱۹ عبریِ d-l-l را با «عربیِ dalla، تدلدل» می‌سنجد، یعنی د-ل-ل با دال. این دو ریشه در عربی جدا‌اند و قاعدهٔ ابدالِ سامی نیز آن‌ها را جدا نگاه می‌دارد: *d سامیِ آغازین در عبری d، در آرامی d و در عربی د می‌شود (پس عبری dālal با عربی دَلَّ هم‌ریشه است)، حال آنکه *ḏ در عبری ز، در آرامی د و در عربی ذ می‌شود (پس عربیِ ذَلَّ با عبریِ זָלַל zālal «خوار و بی‌ارزش شدن» هم‌ریشه است، نه با dālal). ویکی‌واژه نیز «ذلّ» را زیر ریشهٔ مستقلِ ذ ل ل می‌آورد. البته فرهنگ‌نویسانِ قدیم‌تر (گزنیوس و حواشیِ BDB) گاه به دلیلِ نزدیکیِ معنایی عربیِ ذَلَّ را ذیلِ عبریِ dālal یاد کرده‌اند، و در آرامی که هر دو واجِ سامی به d بدل شده این خلط آسان است. با این همه، نمودار چنان کشیده شده که «ذلیل» فارسی خویشاوندِ «دلیله» شود، و بنا بر قواعدِ آوایی چنین نیست. رأی امروزی: *d-l-l و *ḏ-l-l دو ریشهٔ جداگانه‌اند و پژوهش امروزی این پیوند را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Delilah\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:419\", \"status\": \"contradicts\", \"note\": \"The cited page gives 'Arab. dalla, \\\"he was low or pliant\\\", tadaldala, \\\"it hung down, dandled\\\"' — Arabic د ل ل with dāl, not the ذ ل ل of Nourai's 'dz.l.l'. Klein's Arabic cognate is therefore a different root from the one that yields Persian ذلیل.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 419 s.v. Delilah (leaf 231)\", \"stance\": \"contradicts\", \"note\": \"'rel. to Akkad. dalālu … Arab. dalla … tadaldala …' — the tadaldala form proves Klein means د ل ل, since تدلدل is built on dāl.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. ذلیل، ذلّت، ذلالت (2-vol. abridgement lines 65265-65283)\", \"stance\": \"partial\", \"note\": \"«ذلیل: [ع.] (ص.) خوار، زبون، حقیر؛ جمع اذلاء، اذله و ذلال»؛ «ذلالت: [ع. ذلالة] خوار شدن، ذلیل گردیدن» — Mo'in files the Persian family firmly under Arabic ذ ل ل, and nowhere connects it with د ل ل.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dict., s.v. zalíl (RCH.txt line 42051)\", \"stance\": \"partial\", \"note\": \"'A ذليل zalíl, Abject, mean, contemptible. Gentle, submissive.' — marked 'A' (Arabic), spelled with ذ.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"zalîl «ذلیل»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge itself is beyond dispute: Persian ذلیل zalīl 'abject, humiliated, weak' is the Arabic adjective ذَلِيل ḏalīl (faʿīl pattern from ذَلَّ ḏalla 'to be lowly'), borrowed together with the rest of its family in the first Islamic centuries through Qurʾānic and administrative Arabic; Persian keeps the Arabic spelling with ذ but pronounces it z, which is the regular Persian treatment of Arabic ḏāl (as in ذکر zekr, لذّت lezzat). Mo'in tags it «[ع.]» and Richardson marks it 'A'; the chart's extra forms ذلالت ḏalāla and ذلّت ḏella are the Arabic verbal nouns of the same root, likewise borrowed ready-made (Mo'in: «ذلالت: [ع. ذلالة] (مص ل.) خوار شدن، ذلیل گردیدن»; «ذلّت: [ع. ذلة] خواری، مذلّت»). The only reservation belongs one box higher up: what is doubtful is not that Persian took zalīl from Arabic, but that Arabic ذ-ل-ل belongs to the Semitic root d-l-l of Delilah (node 1).\",\n          \"derivation_fa\": \"خودِ این پیکان تردیدناپذیر است: «ذلیل» فارسی همان صفتِ عربیِ ذَلیل (بر وزن فَعیل از ذَلَّ «خوار شدن») است که در سده‌های نخستِ اسلامی همراه با دیگر مشتقاتِ همین ریشه از راهِ زبان قرآن و دیوان به فارسی درآمده. فارسی املای عربی را با ذال نگاه داشته ولی آن را ز تلفظ می‌کند، و این تبدیلِ منظمِ ذالِ عربی در فارسی است (چنانکه ذکر > zekr و لذّت > lezzat). معین آن را «[ع.]» برچسب زده و ریچاردسن «A» (عربی)؛ صورت‌های افزودهٔ نمودار، «ذلالت» و «ذلّت»، مصدرهای عربیِ همان ریشه‌اند که آماده وام گرفته شده‌اند («ذلالت: [ع. ذلالة] (مص ل.) خوار شدن، ذلیل گردیدن»). تنها تحفظ به یک جعبه بالاتر مربوط است: آنچه محلِ تردید است پیوندِ ریشهٔ عربیِ ذ-ل-ل با ریشهٔ سامیِ d-l-l (گرهِ ۱) است، نه وام‌گیریِ فارسی از عربی.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%AF%D9%84%DB%8C%D9%84%D9%87/\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:150\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi — no digital copy exists on any permitted platform (refs_online.json, re-searched 2026-09); catalogue record only.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. ذلیل / ذلّت / ذلالت (2-vol. abridgement lines 65265-65283)\", \"stance\": \"supports\", \"note\": \"«ذلیل: [ع.] (ص.) خوار، زبون، حقیر؛ جمع اذلاء، اذله و ذلال» — the [ع.] tag is Mo'in's own statement that the word is an Arabic loan.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dict. (RCH.txt line 42051)\", \"stance\": \"supports\", \"note\": \"'A ذليل zalíl, Abject, mean, contemptible. Gentle, submissive.' — the 'A' prefix is Richardson's mark for an Arabic word current in Persian.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi (grep ذلیل in ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"No entry, as expected for a Semitic loan in a dictionary of Indo-European roots.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Hebrew\",\n          \"words\": \"delilah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Hebrew דְּלִילָה Dəlīlāh, the Philistine woman of Judges 16, is a qᵊṭīlāh-pattern formation on the root d-l-l 'to hang down, be low, languish'. Klein p. 419 gives precisely Nourai's gloss: 'Heb. Dəlīlāh, lit. \\\"delicate, languishing, amorous\\\", from the base of d-l-l'. The 'amorous' shade comes from the by-form dallāh 'hair, thrum, that which hangs down' and from reading the name as 'she of the flowing hair' — a reading suggested by the narrative, in which Samson's hair is the pivot; a second and equally old reading takes the passive sense, 'she who weakened (him)', which is the gloss Wiktionary now prints ('[she who] weakened'). Both readings work off the same root, so the node stands whichever is preferred. (A minority proposal links the name instead to לַיְלָה laylāh 'night', against Samson's šemeš 'sun' — but that is a literary pun, not an etymology.)\",\n          \"derivation_fa\": \"«دْلیلاه» עברי (דְּלִילָה)، زنِ فلسطینیِ بابِ ۱۶ کتابِ داوران، بر وزنِ qᵊṭīlāh از ریشهٔ d-l-l «آویختن، پست بودن، سست شدن» ساخته شده. کلاین در ص ۴۱۹ درست همان معنایی را می‌دهد که نورایی آورده: «عبری Dəlīlāh، لفظاً: نازک، سست، دلربا، از ستاکِ d-l-l». سایهٔ معناییِ «دلربا» از هم‌ریشهٔ dallāh «مو، آنچه آویزان است» می‌آید و از خواندنِ نام به معنیِ «آن‌که گیسوی افشان دارد» — خوانشی که داستان خودْ به آن راه می‌برد، چون گیسوی شمشون محورِ ماجراست. خوانشِ دومِ به‌همان اندازه کهن، معنیِ مجهول را می‌گیرد: «آن‌که او را سست کرد»، و ویکی‌واژه امروز همین را می‌آورد. هر دو خوانش بر همان ریشه استوارند، پس ادعای نورایی درست است. (پیشنهادِ اقلیتی که نام را به «لَیْلاه» شب می‌بندد در برابرِ «شِمِش» خورشیدِ شمشون، جناسی ادبی است نه ریشه‌شناسی.)\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Delilah\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:419\", \"status\": \"supports\", \"note\": \"Klein leaf 231 s.v. Delilah: 'Heb. Dəlīlāh, lit. \\\"delicate, languishing, amorous\\\", from the base of d-l-l, \\\"to hang down, to languish\\\"' — Nourai's gloss is a verbatim copy.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 419 s.v. Delilah\", \"stance\": \"supports\", \"note\": \"Quoted above.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Delilah (WEB_vol1.txt line 51452)\", \"stance\": \"supports\", \"note\": \"'Delilah, n. [Heb. delila[h], lit., delic[ate]…] 1. in the Bible, th[e woman who] betrayed him to the [Philistines by having his] hair cut off while he [was asleep]'.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (grep 'Delilah' in FSD_vol1-4)\", \"stance\": \"silent\", \"note\": \"Only incidental mentions (a painting title, an idiom); no etymological entry in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"Dalîleh «دلیله»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian دلیله Dalīle is indeed the Delilah of Judges 16 — Mo'in's Farhang-e Farsi (the a'lam volumes, which is what MON5:526 points to) defines her as «زن درباری که سامسون را پس از قطع موهای وی … تسلیم فلسطینیان کرد», and Dehkhoda has «زنی زانیه بود که در وادی سورق … سبب شد که شمشون بدست دشمنانش گرفتار شود». What the chart's direct Hebrew→Persian arrow leaves out is the mediation: the name did not travel from Hebrew into Persian, but through Arabic. Persian took it in the vocalisation دَلیلة/دلیله of the Arabic Isrāʾīliyyāt and Qiṣaṣ al-anbiyāʾ literature (Ṭabarī, Thaʿlabī), where the Samson story (شمشون الجبار) circulated from the 9th–10th centuries; the Persian spelling with ه for the Arabic tāʾ marbūṭa is the fingerprint of that route, as is the ī of the second syllable, which matches the Arabic faʿīla shape rather than the Hebrew shewa. A reader should also be warned that Persian دلیله most often evokes a different woman — دلیلهٔ محتاله, the trickster of the Thousand and One Nights — whose name is Arabic دَلَّالة/دَليلة 'guide, procuress' from د-ل-ل 'to point the way', not the Hebrew name at all.\",\n          \"derivation_fa\": \"«دلیله» در فارسی همان دلیلهٔ بابِ ۱۶ داوران است؛ فرهنگ فارسیِ معین (بخش اعلام، همان جایی که ارجاعِ MON5:526 به آن است) او را «زن درباری که سامسون را پس از قطع موهای وی … تسلیم فلسطینیان کرد» می‌شناساند و دهخدا می‌نویسد «زنی زانیه بود که در وادی سورق … سبب شد که شمشون بدست دشمنانش گرفتار شود». آنچه پیکانِ مستقیمِ عبری ← فارسیِ نمودار نادیده می‌گیرد واسطه است: این نام از عبری یکسره به فارسی نیامده، بلکه از راهِ عربی آمده است — از صورتِ «دَلیلة» در ادبِ اسرائیلیات و قصص‌الانبیای عربی (طبری، ثعلبی) که داستانِ «شمشون الجبار» از سدهٔ سوم و چهارم هجری در آن می‌گشت. نشانهٔ این راه، نگارشِ «ـه» به‌جای تاء مربوطهٔ عربی و «ی» کشیدهٔ هجای دوم است که با وزنِ فَعیلهٔ عربی می‌خواند نه با شوایِ عبری. هشدارِ لازم برای خواننده: «دلیله» در فارسی بیشتر یادآورِ زنِ دیگری است — «دلیلهٔ محتاله»ی هزار و یک شب — که نامش عربیِ دَلّاله/دَلیله «راهنما» از ریشهٔ د-ل-ل «راه نمودن» است و هیچ ربطی به نامِ عبری ندارد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%AF%D9%84%DB%8C%D9%84%D9%87/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON5:526\", \"status\": \"supports\", \"note\": \"Volume 5 of the six-volume Mo'in (a'lam) is not on disk and its pagination cannot be checked; but the entry's content is confirmed through the online Farhang-e Mo'in text at abadis.ir/fatofa/دلیله (archived via fetch_source.py): «زن درباری که سامسون را پس از قطع موهای وی … تسلیم فلسطینیان کرد» — exactly Nourai's gloss 'the mistress of Samson'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. دلیله (abadis.ir فرهنگ فارسی section)\", \"stance\": \"supports\", \"note\": \"«زن درباری که سامسون را … تسلیم فلسطینیان کرد» — supports the identification but says nothing about the language of transmission.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (grep دلیله in BQT_v2_pages.txt / v3)\", \"stance\": \"silent\", \"note\": \"Not a Borhan headword — Borhan is a dictionary of Persian words, and biblical proper names of this kind are absent.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dict. (grep 'dalíla' in RCH.txt)\", \"stance\": \"silent\", \"note\": \"No entry for the proper name; Richardson has only the common noun دليل dalíl 'guide, proof' from the unrelated Arabic root د ل ل.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"Delilah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Delilah reaches English by the ordinary scriptural route: Hebrew דְּלִילָה → Septuagint Greek Δαλιδά/Δαλιλά → Vulgate Latin Dalila → Wycliffite and later English Bibles, with the modern spelling Delilah fixed by the Geneva (1560) and King James (1611) versions, which followed the Hebrew rather than the Vulgate. The appellative sense — 'a false woman; temptress; harlot', as Webster's second sense has it — is a seventeenth-century English development from the story, reinforced by Milton's Samson Agonistes (1671). Klein's entry at the cited page supplies the Hebrew source and gloss, and Webster's, the second reference Nourai gives, carries both the etymology and the transferred sense.\",\n          \"derivation_fa\": \"«Delilah» انگلیسی از همان راهِ معمولِ کتاب مقدس به انگلیسی رسیده است: عبری דְּלִילָה ← یونانیِ سبعینیه Δαλιλά ← لاتینِ ولگات Dalila ← ترجمه‌های انگلیسیِ کتاب مقدس، و املای امروزیِ Delilah در انجیلِ ژنو (۱۵۶۰) و ترجمهٔ شاه جیمز (۱۶۱۱) تثبیت شد که به‌جای ولگات از متنِ عبری پیروی کردند. کاربردِ آن همچون اسمِ عام — «زنِ فریبکار، زنِ اغواگر» که وبستر معنیِ دومش آورده — تحولی انگلیسی در سدهٔ هفدهم است که «شمشونِ پهلوان» میلتون (۱۶۷۱) به آن دامن زد. کلاین در صفحهٔ مورد ارجاع ریشه و معنیِ عبری را می‌دهد و وبستر، ارجاعِ دومِ نورایی، هم ریشه‌شناسی و هم معنیِ مجازی را دارد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Delilah\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:419\", \"status\": \"supports\", \"note\": \"Klein leaf 231 (p. 419): 'Delilah, n., the mistress of Samson, who betrayed Samson (Judges, chapter 16). — Heb. Dəlīlāh, lit. \\\"delicate, languishing, amorous\\\"…'\"},\n            {\"ref\": \"WEB:480\", \"status\": \"supports\", \"note\": \"Webster's New Twentieth Century, 2nd ed., vol. 1, leaf 512 of WEB_vol1.txt (printed page numerals are not reliably OCR'd in this scan, but the leaf-to-page offset of roughly 32 for the front matter puts the entry at p. 480): 'Delilah, n. [Heb. delila[h], lit., delic[ate] …] … 2. a false woman; temptress; harlot.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 419 s.v. Delilah\", \"stance\": \"supports\", \"note\": \"Quoted above.\"},\n            {\"src\": \"WEB\", \"where\": \"vol. 1 leaf 512 s.v. Delilah\", \"stance\": \"supports\", \"note\": \"'2. a false woman; temptress; harlot' — the transferred English sense, which Klein does not record.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (grep 'Delilah' in SKT.txt)\", \"stance\": \"silent\", \"note\": \"No entry — Skeat excludes biblical proper names.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T20:22:20.499Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-138.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T20:22:24.188Z] TOOL CALL #55: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-138.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 138"
}
```


### [2026-09-05T20:22:29.728Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 8, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'not_checked': 4, 'partial': 3, 'contradicts': 1}
books consulted: {'supports': 23, 'partial': 5, 'silent': 8, 'contradicts': 1} | by book: {'KLN': 7, 'MON': 5, 'AKD': 4, 'RCH': 4, 'WEB': 4, 'AFA': 3, 'BQT': 2, 'ARY': 2, 'FSD': 2, 'FVQ': 1, 'HRN': 1, 'AFM': 1, 'SKT': 1}
```


## [2026-09-05T20:22:48.957Z] AGENT

Done. `verify_check.py 138` reports 0 PROBLEM lines (12/12 nodes).

**Page 138 (book p. 108) — 2 non-redirect entries, 12 nodes**

Verdicts: roots 2 confirmed; nodes 8 confirmed, 3 plausible, 1 disputed.
Ref checks: 10 supports, 3 partial, 1 contradicts, 4 not_checked (all FVA — Nahvi's book has no digital copy anywhere).

- **disputed** — root `D.l.l`, node 1, Arabic `dz.l.l, z.l.l`: Nourai's root is ذ-ل-ل (source of Persian ذلیل), but Klein at the cited p. 419 compares Hebrew d-l-l with Arabic **د**لّ *dalla* / تدلدل. Proto-Semitic *ḏ → Arabic ذ but Hebrew **ז** (zālal), while *d → Hebrew d / Arabic د, so ذلیل cannot be a relative of Delilah. Two roots conflated.
- **plausible** — `Dînu`, node 3 (Persian دین ۲ "judgment day"): the debt word is a certain Arabic loan (Mo'in «دین: [ع.] قرض، وام»), but Mo'in knows only two homonyms (Arabic "debt", Pahlavi "religion"); a Persian headword "judgment day" is Nourai's own arrangement.
- **plausible** — `Dînu`, node 6 (Hebrew under Aramaic): Zimmern p. 24 and Klein p. 399 make Hebrew and Aramaic *parallel* recipients from Akkadian; only the Arabic branch is Aramaic-mediated. Ugaritic *dn* confirms the root in West Semitic pre-Aramaic.
- **plausible** — `D.l.l`, node 4 (Persian دلیله): content confirmed (Mo'in/Dehkhoda: Samson's betrayer), but the route is Hebrew → Arabic *Qiṣaṣ al-anbiyāʾ* → Persian, not direct; the ـه for tāʾ marbūṭa gives it away.

**No transcription errors** — the JSON is faithful to the printed page (checked `site/pages/138.jpg`). One cosmetic note for the owner: the extraction merged the root box's two printed lines ("Dînu, Děnu : law, right, judgment" / "Dayânu : judge") into one name + one joined gloss; content is preserved, no fix needed unless you want the split.

Best finds: Zimmern, *Akkadische Fremdwörter* p. 24 states Nourai's whole entry-0 chart almost verbatim; Mo'in's footnote in Borhan (vol. 2 leaf 376 ≈ the cited p. 916) is a Persian paraphrase of that same Zimmern page; Jeffery pp. 131–132 confirms the note about the two Arabic *dīn*s; Fraenkel p. 281 supplies the internal-Arabic argument that مدینه is a loan and مدنی/تمدن denominative. 4 web pages archived via `fetch_source.py`.
