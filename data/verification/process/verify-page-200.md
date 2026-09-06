# Verification process log — verify-page-200


## [2026-09-06T02:16:47.353Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 200 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-200.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-200.json. Write /home/sfmqrb/git/rishe/data/verification/page-200.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 200` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:16:48.855Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T02:16:49.562Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:16:49.584Z] TOOL RESULT

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


## [2026-09-06T02:16:49.993Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-200.txt"
}
```


### [2026-09-06T02:16:50.006Z] TOOL RESULT

```
1	=== PDF page 200 (book page 170) ===
2	--- entry 0 ---
3	ROOT Guhâ -> redirect to Gwhi
4	--- entry 1 ---
5	ROOT Guheguh -> redirect to Dhogh
6	--- entry 2 ---
7	ROOT Guhei -> redirect to Gwhi
8	--- entry 3 ---
9	ROOT Ğul -> redirect to Dhogh
10	--- entry 4 ---
11	ROOT Gulgul -> redirect to Gwer 3
12	--- entry 5 ---
13	ROOT Gumnos -> redirect to Nogw
14	--- entry 6 ---
15	ROOT Gunos -> redirect to Nogw
16	--- entry 7 ---
17	ROOT [Persian] Gŭrb, Kŭrb : stocking  (refs MON:3434)
18	#1 (parent #0) [Arabic] refs=FVF:177; ARB:101 | jaurb, jaurab : stocking, sock ; j.r.b : he wears socks
19	  #2 (parent #1) [Persian] refs=MON:3434 | jŭrâb «جوراب» : stocking, sock
20	  #3 (parent #1) [Portuguese] refs=KLN:678 | greba : leg or shin protection
21	    #4 (parent #3) [Old French] refs=KLN:678 | greve : shin armor, shin
22	      #5 (parent #4) [English] refs=KLN:678 | greave : leg armor | NOTE: AHD:577 derives this word from a different root.
23	--- entry 8 ---
24	ROOT [Indo-European] Gurdos, Gurdus : brave, proud  (refs IEC:307)
25	#1 (parent #0) [Old Persian] refs=BQT:1786; HUB:91 | Vtra, Vurt : hero
26	#2 (parent #0) [Armenian] refs=IEC:307 | kord : rough
27	  #3 (parent #1) [Pahlavi] refs=BQT:1786 | gort, gurt : hero, strong
28	    #4 (parent #3) [Persian] refs=HRN:200; BQT:1786; IEC:307 | gord «گرد» : strong, hero | extra: گردان،گردزاد
29	--- entry 9 ---
30	ROOT [Indo-European] Gurdos, Gurdus : sluggish, stupid  (refs IEC:373)
31	#1 (parent #0) [Persian] refs=IEC:373; MON:3470 | gŭl «گول» : stupid | extra: گول زدن ، گول خوردن
32	#2 (parent #0) [Latin] refs=IEC:373 | gurdus : stupid
33	#3 (parent #0) [Greek] refs=IEC:373 | bradus : sluggish
34	  #4 (parent #3) [Latin] refs=IEC:373 | bardus : stupid
35	
```


## [2026-09-06T02:16:53.026Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-200.json",
 "description": "Read source JSON for page 200"
}
```


### [2026-09-06T02:16:53.068Z] TOOL RESULT

```
{
  "pdf_page": 200,
  "book_page": 170,
  "entries": [
    {
      "root": {"name": "Guhâ", "redirect": "Gwhi"},
      "nodes": []
    },
    {
      "root": {"name": "Guheguh", "redirect": "Dhogh"},
      "nodes": []
    },
    {
      "root": {"name": "Guhei", "redirect": "Gwhi"},
      "nodes": []
    },
    {
      "root": {"name": "Ğul", "redirect": "Dhogh"},
      "nodes": []
    },
    {
      "root": {"name": "Gulgul", "redirect": "Gwer 3"},
      "nodes": []
    },
    {
      "root": {"name": "Gumnos", "redirect": "Nogw"},
      "nodes": []
    },
    {
      "root": {"name": "Gunos", "redirect": "Nogw"},
      "nodes": []
    },
    {
      "root": {
        "name": "Gŭrb, Kŭrb",
        "lang": "Persian",
        "refs": "MON:3434",
        "gloss": "stocking",
        "script": "گورب",
        "script_extra": "گوراب ۲"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVF:177; ARB:101",
          "words": [
            {"translit": "jaurb, jaurab", "gloss": "stocking, sock", "script": null},
            {"translit": "j.r.b", "gloss": "he wears socks", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:3434",
          "words": [
            {"translit": "jŭrâb", "gloss": "stocking, sock", "script": "جوراب"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Portuguese",
          "refs": "KLN:678",
          "words": [
            {"translit": "greba", "gloss": "leg or shin protection", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old French",
          "refs": "KLN:678",
          "words": [
            {"translit": "greve", "gloss": "shin armor, shin", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:678",
          "words": [
            {"translit": "greave", "gloss": "leg armor", "script": null}
          ],
          "note": "AHD:577 derives this word from a different root.",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gurdos, Gurdus",
        "lang": "Indo-European",
        "refs": "IEC:307",
        "gloss": "brave, proud"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "BQT:1786; HUB:91",
          "words": [
            {"translit": "Vtra, Vurt", "gloss": "hero", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:307",
          "words": [
            {"translit": "kord", "gloss": "rough", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1786",
          "words": [
            {"translit": "gort, gurt", "gloss": "hero, strong", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "HRN:200; BQT:1786; IEC:307",
          "words": [
            {"translit": "gord", "gloss": "strong, hero", "script": "گرد"}
          ],
          "script_extra": "گردان،گردزاد",
          "note": null,
          "quote": {
            "text": "بهومان چنین گفت سهراب گرد - که اندیشه از دل بباید سترد",
            "poet": "Ferdowsî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Gurdos, Gurdus",
        "lang": "Indo-European",
        "refs": "IEC:373",
        "gloss": "sluggish, stupid"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:373; MON:3470",
          "words": [
            {"translit": "gŭl", "gloss": "stupid", "script": "گول"}
          ],
          "script_extra": "گول زدن ، گول خوردن",
          "note": null,
          "quote": {
            "text": "آن زنک میخواست تا با مول خود - جمع گردد پیش شوی گول خود",
            "poet": "Molavî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "IEC:373",
          "words": [
            {"translit": "gurdus", "gloss": "stupid", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:373",
          "words": [
            {"translit": "bradus", "gloss": "sluggish", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "IEC:373",
          "words": [
            {"translit": "bardus", "gloss": "stupid", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T02:16:53.721Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:16:53.769Z] TOOL RESULT

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


## [2026-09-06T02:16:59.787Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVF','FVQ','ARB','IEC','HUB','HRN','BQT','MON','KLN','AHD','POK','WLD','PHD','LKT','SKT','LEW','LAT','AFM','PLA','TAD','RCH','ARY','SYN','NYB','FSF','FRS']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\""
}
```


## [2026-09-06T02:17:00.185Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -80 data/verification/page-124.json"
}
```


### [2026-09-06T02:17:01.911Z] TOOL RESULT

```
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
```


### [2026-09-06T02:17:01.960Z] TOOL RESULT

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
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
      ],
      "ref_check": [
        {
          "ref": "AHD:1512",
          "status": "supports",
          "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination."
        },
        {
          "ref": "POK:235",
          "status": "supports",
          "note": "POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'."
        }
      ],
      "consulted": [
        {
          "src": "POK",
          "where": "pp.235-239, dʰē-2",
          "stance": "supports",
          "note": "supplies not only the root but every Iranian form of the chart: 'Avestan Old pers. data-', 'Avestan ni-δaiti- f. „laying down, putting away, hiding“', 'Avestan gao-δi- „milk container“', 'Avestan gao-δana- n. „milk container“', 'Avestan daman-, dąman- n. „site, creature“'."
        },
        {
          "src": "WLD",
          "where": "Bd. I pp.826-830 (p.828)",
          "stance": "supports",
          "note": "the parent article of Pokorny's; p.828 carries 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“', 'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“', 'av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“'."
        },
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. dhē-¹",
          "stance": "supports",
          "note": "'To set, put. Contracted from *dheə.' Same gloss as Nourai's 'to do, set'."
        },
        {
          "src": "Wiktionary",
          "where": "Reconstruction:Proto-Indo-European/dʰeh₁-",
          "stance": "supports",
          "note": "'*dʰeh₁- (perfective): to do; to put, place.'"
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "ma[n]dz-dha; ahura-mazdha",
          "verdict": "confirmed",
          "derivation": "The Avestan words are mazdā- / mazdah- n. 'memory, wisdom' and the divine name ahura- mazdā- 'Lord Wisdom' (Ahura Mazda). The second member really is this root: the compound is Proto-Indo-Iranian *mns-dʰeh₁- 'to set (something) in mind, commit to memory', i.e. *men- 'think' + *dʰeh₁- 'put'; Pokorny treats it under mendʰ- (Page(s): 730): 'Avestan mazda, mazdah- n. „Gedächtnis“, mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'. Nourai's odd transliteration 'ma[n]dz-dha / ahura-mazdha' is copied letter for letter from Klein s.v. Ormazd ('ma(n)dzdha-, ‘wise’, which is a compound formed from the I.-E. bases *men-dh- and *dhe- ‘to put, place’'); the actually attested Avestan spelling is mazdā-, so the -dh- here is Klein's etymologising respelling, not an Avestan form. The gloss 'done learning, wise' and the cross-reference to Men 1 are both correct.",
          "derivation_fa": "واژهٔ اوستایی mazdā- / mazdah- به معنی «خرد، یاد» و نام ایزدی ahura-mazdā- «سرورِ خرد» از ترکیب هندوایرانی آغازین *mns-dʰeh₁- «در یاد نهادن» ساخته شده است؛ یعنی ستاک *men- «اندیشیدن» به علاوهٔ همین ریشهٔ *dʰeh₁- «نهادن». پوکورنی این واژه را در صفحهٔ ۷۳۰ ذیل mendʰ- آورده (نه در صفحهٔ ۲۳۵ که نورایی ارجاع داده). املای غریبِ «ma[n]dz-dha» عیناً از کلاین (ذیل Ormazd) گرفته شده و صورت اوستایی واقعی mazdā- است. در مجموع ادعای نورایی درست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/Ahura_Mazda",
            "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
          ],
          "ref_check": [
            {
              "ref": "POK:235",
              "status": "partial",
              "note": "POK_full.txt lines 22276-22510: the lemma at 'Page(s): 235-239' is 'dʰe-2, Meaning: to put, place, say' and it does NOT mention mazdā anywhere. Pokorny discusses mazdā s.v. mendh- at 'Page(s): 730' (line 59307: 'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'). The -dhā element is this root, so the claim holds, but the cited page is the wrong one."
            }
          ],
          "consulted": [
            {
              "src": "POK",
              "where": "p.730 s.v. mendh- (POK_full.txt line 59307)",
              "stance": "supports",
              "note": "'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)' — the compound of *men-dh- + *dhē-."
            },
```


## [2026-09-06T02:17:23.054Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"جورب\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -30; echo \"=== AFM ===\"; grep -n \"جورب\" AFM.txt | head -20; echo \"=== TAD ===\"; grep -n \"جورب\" TAD.txt | head -20; echo \"=== FVQ ===\"; grep -n -i \"jaurab\\|jawrab\" FVQ.txt | head"
}
```


### [2026-09-06T02:17:23.175Z] TOOL RESULT

```
ARB_mo3rb.txt:2394:و« جورب » وأعيله : « (ورب » ٠‏ و« مورج » وا : « موزة » 
ARB_mo3rb.txt:8832:فعلا 6 تقال يصف لعن الثلياء *” وقد تجررب حور بين ©“ يعنى لبسبما ٠‏ و ” جور بته جورب “ 
ARB_mo3rb.txt:26690:)4 : ١85 ©5165 36560 جورب ههة:‎ 
=== AFM ===
=== TAD ===
2569:كاسات وقاشين - لانيني 3ع معناه غطاء عقب الرجل . وجورب 
=== FVQ ===
```


## [2026-09-06T02:17:23.746Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN greave ===\"; grep -n \"greave\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== SKT ===\"; grep -n \"greave\" SKT.txt | head; echo \"=== AHD ===\"; grep -n -i \"greave\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T02:17:23.835Z] TOOL RESULT

```
=== KLN greave ===
KLN_1971.txt:105804:graves, n. pi. — A var. of greaves. 
KLN_1971.txt:105913:greave, n., armor for the leg. — ME. greve, fr. 
KLN_1971.txt:105915:OF. greve, ‘shin; greave’, fr. Port, greba, fr. 
KLN_1971.txt:105920:greave, n., sediment of melted tallow. — LG. 
KLN_1971.txt:165346:— L., ‘a legging, greave’, prob. meaning lit. 
KLN_1971.txt:207529:rel. to rillons, ‘greaves of pork’, fr. ride, ‘piece of 
KLN_1966.txt:16621:graven,  adj.,  carved  (archaic).  —  ME.  graven,  fr. OE.  grafen,  prop.  pp.  of  grafan,  ‘to  dig,  carve’. See  grave,  ‘to  dig,  carve’, graveolent,  adj.,  having  a  rank  smell.  —  L.  grave- olens,  gen.  -ends,  ‘strong-smelling’,  prop,  grave olens,  fr.  grave,  neut.  of  gravis,  ‘heavy’,  and pres.  part,  of  olere,  ‘to  smell’.  See  grave,  weigh¬ ty’,  olfactory  and  -ent. graves,  n.  pi.  —  A  var.  of  greaves.
KLN_1966.txt:16639:greave,  n.,  armor  for  the  leg.  —  ME.  greve,  fr.
KLN_1966.txt:16640:OF.  greve,  ‘shin;  greave’,  fr.  Port,  greba,  fr. Egypt.  Arab,  gaurab,  corresponding  to  Arab. jditrab,  ‘stocking,  apparel  for  the  leg’. Derivative:  greav-ed,  adj.
KLN_1966.txt:16641:greave,  n.,  sediment  of  melted  tallow.  —  LG. greven  (pi.),  rel.  to  OHG.  griobo  (MHG.,  G. griebe)',  of  uncertain  origin.
KLN_1966.txt:26023:—  L.,  ‘a  legging,  greave’,  prob.  meaning  lit. ‘something  sharp-edged’,  and  rel.  to  ocris,  ‘a rugged,  stony  mountain’,  acer,  ‘sharp’.  See  acrid and  words  there  referred  to  and  cp.  esp.  the second  element  in  mediocre.
KLN_1966.txt:32928:rillettes,  rilletts,  n.  pi.,  potted  meat.  —  F.  rillettes, rel.  to  rillons,  ‘greaves  of  pork’,  fr.  rille,  ‘piece  of pork’,  a  dialectal  var.  of  OF.  reille,  ‘small  plank, lath’,  itself  a  popular  collateral  form  of  regie, ‘rule,  plank’.  See  rule  and  dimin.  suff.  -ette.
=== SKT ===
7962:fe¥Mi<  I  \  WftToa.  sediment  ofmelted jSg^^  0.  Swcil.  rre/amr,  dirt ; ^^^K,  'lieht-tliii,  rc/it$e  ol  tal- ^^^^^pjulciug  ;  Swed.  dial,  ^trvar, Dliu  <f  Low  li.  ^rven,  greaves,  G.
22800:grave,    graze,   greaves,    gnret.  fW/.
23588:rcl.  bice,  bijon.  blond,  blouse,  brattice, te«  (il,  biet'ze  (2),  broil  (2).  buffer  (,0, ffer  (3).  buffet  (I),  buffet  (j),  huffoon. ruattft  (burgoiict),  busk  (i),  buttress, t>ba|^  {»),  culibcr  ^calibre),  calipers, lirer,  champagne,  chcval-dc-frise,  chi- Bcry,  chiffonier,  cockaJe.  curlew,  davit, le,  dtMase,  drab  (a),  drape,  dupe,  ease, ibiiitlc  (O,  embattle  (a),  cmblaion,  era- S*  { I  \  emboM  (2),  embrasure,  embroider, ibroil,  entice,  entrench,  fribble,  frieze  (i), ppery,  furbelow,  galley,  galliot,  gallon, rland,  gasccmade,  gavotte,  gibbet,  giblets, (3),  gingham,  gobelin,  gormandise, lUTnand,  graze  (l)?,  greaves  (,a),  grouse, illotine,  guxxle,  harass,  haricot  (i),  hari- (a\  harlequin,  harlot,  harridan,  hnunt, ik  ;a],  jacKetf  jostle,  lawn  (^a),  lees, tch,  loo,  lozenge,  magnolia,  maraud, utia,  martinet,  martingale,  martlet,  mich, Trtise,  musit.  Nicotian,  pamphlet?,  pa- Kv  pedigree?,  pillory,  pinch,  pinchbeck vritma/  name),  pirouette,  piss,  pittance, plin,    ricochet,    roan,    sautcmc,    savoy,
=== AHD ===
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
```


## [2026-09-06T02:17:38.464Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2380,2400p' ARB_mo3rb.txt; echo \"=== 8820-8845 ===\"; sed -n '8820,8845p' ARB_mo3rb.txt"
}
```


### [2026-09-06T02:17:38.529Z] TOOL RESULT

```
0 ةم 


ما صنت بعد طوى القريق * من شرية فير النجاء الادفي 





. م ع د يل و ىا ير 
ْ وكذلك يقولون : « كلجة » و« كلقة » و« قيلقة » ٠.‏ و« حربز » للربز ٠‏ 
سودق 5 3-9 1 07 و(ء) 1 1 
2 1 1 أصله : موزة © ه 6 
و« جورب » وأعيله : « (ورب » ٠‏ و« مورج » وا : « موزة » 
5 3 7 
وأبدلوا ال خرف الذى 2 الباء والفاء فأه 6 ور ما أبداوه بأء ٠‏ قالوا : 
و4 20 003 
٠‏ ٍ 00 7 و 
د فالود » 6 و« ثرنك » ٠‏ وقال عضوم : ١‏ يرلك » ه 
وأبدلوأ أأسين دن الشين » فقالوأ للم حراء 2 « دست »2 وفى بالفارسية : 
=== 8820-8845 ===
(1) بسر ابكيم واللام المشددة المكسورةٌ ٠‏ وما سيأق فى المادة ذ كه ياقوت ف البلدات معناه ٠‏ 

(0) كلة «اصأة» ل تذكرق 1 

2( كلبة « معرب »> ل تذ, فى م ٠‏ | 

: من أول المادة إلى آخر البيت كلام أبن دريد فى اجمهرة ( © : 50 * ) ولكن أول كلامه‎ (١ 
1 5 » وجحورت أءم فارسى عرب‎ « 

)6( فى الاسات : « واطورب لفاتة الرجل » معرب ء وهو بالفاسية *” كورب * ٠‏ وابمسم 
** سوارية “» زادرا الحاء لمكان العجمة » ونظاسيره ءن العرربية القشاعمة ٠‏ ود قالوا ”” الموارب “ ٠‏ 
كا قالوا فى جميع ”الكل“ الكابل ““؛ ونظيره ءن العربية الكوا كب ٠‏ واستع.ل ابن السكيت منه 
فعلا 6 تقال يصف لعن الثلياء *” وقد تجررب حور بين ©“ يعنى لبسبما ٠‏ و ” جور بته جورب “ 
أى ألسته اطورب فلسه » ٠‏ 

() « الرق > يقت الراء والتون : الكدر ٠‏ وفى س « زق » بالزاى » وهوخطا ٠‏ وقوله 
« بعيشة » يريد عانشة »© ولكن نص اللغويرن على منع هذا » فتى الأسان : « وعائشة مهموزة » 
رلاتقل عيشة ٠‏ قال ابن السكيت : تقول : هى مائشة 6 ولا تقل العيشة » وتقول : هى ريطة » 
ولا تقل رائطة » وتقول : هو من نى عبذالله » ولائة_ل عائذالله » ٠‏ والبيث فى رواية الأغانى 
٠ 0‏ ؛ 5ه ساسى) : 
أثم بعائش عيثا غبر ذى ري * مأليذ برملة نبذ الاورب الالق 


8
```


## [2026-09-06T02:17:41.510Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"greave\\|greve\" KLN_1966.txt | sed -n '1,5p'; echo \"---- find page marker near line 16639 ----\"; awk 'NR>=16600 && NR<=16660' KLN_1966.txt | grep -n \"\" | head -5; echo \"=== leaf index of greave ===\"; python3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=d.find(\"greave,  n.,  armor  for  the  leg\")\nprint('charpos',i)\nprint('leaf(0-based formfeeds before):', d[:i].count('\\f'))\nEOF"
}
```


### [2026-09-06T02:17:43.303Z] TOOL RESULT

```
1948:aggrieve,  tr.  v.,  i)  to  grieve;  2)  to  injure  in  one’s rights.  —  ME.  agreven,  fr.  OF.  agrever,  fr.  L. aggravare,  ‘to  make  heavier’.  See  aggravate. Derivatives:  aggriev-ed,  adj.,  aggriev-ed-ly,  adv., aggriev-ed-ness,  n.
8735:Congreve  rocket,  Congreve  match.  —  Both  named after  their  inventor  Sir  William  Congreve (1772-1828).
16617:Derivative:  grave-less,  adj. grave,  tr.  v.,  to  clean  (the  wooden  hull  of  a  ship) of  grass,  etc.  —  OF.  grave  (F.  grive),  ‘strand of  sand,  sandbank’.  See  gravel  and  cp.  Graves, grave,  adj.,  weighty.  —  F.,  fr.  L.  gravis,  ‘heavy, weighty;  troublesome,  painful,  grievous,  hard; important,  honorable’,  which  is  cogn.  with  OI. gurufi,  ‘heavy,  weighty’  (compar.  gariyas-; superl.  garifthah),  Avestic  gouru-  (only  in  com¬ pounds),  ‘heavy,  weighty’,  Gk.  (Japoi;,  ‘weight’, ^apu?,  ‘heavy’,  Pptffeiv,  ‘to  be  laden  with’ ,  Ppiffu?, ‘heavy’,  ppuxp6e,  ‘strong’,  Goth,  kaurus,  ‘heavy’, Lett,  grids,  ‘heavy’.  Cp.  gravedo,  gravid,  gravity, grief,  grieve,  grievous,  aggravate,  aggrieve,  in¬ gravescent.  Cp.  also  baro-,  bary,  Briareus,  brute, centrobaric,  charivari,  garce,  guru,  isobar, grave,  n.,  a  count;  used  esp.  of  the  counts  of Nassau.  —  MDu.  grave  (whence  Du.  graaf), ‘count’,  rel.  to  OHG.  gravo  (whence  MHG. grave,  G.  Graf),  MLG.  grive  (whence  ON. greifi,  Dan.,  Swed.  greve),  ‘count’.  The  orig.
16621:graven,  adj.,  carved  (archaic).  —  ME.  graven,  fr. OE.  grafen,  prop.  pp.  of  grafan,  ‘to  dig,  carve’. See  grave,  ‘to  dig,  carve’, graveolent,  adj.,  having  a  rank  smell.  —  L.  grave- olens,  gen.  -ends,  ‘strong-smelling’,  prop,  grave olens,  fr.  grave,  neut.  of  gravis,  ‘heavy’,  and pres.  part,  of  olere,  ‘to  smell’.  See  grave,  weigh¬ ty’,  olfactory  and  -ent. graves,  n.  pi.  —  A  var.  of  greaves.
16639:greave,  n.,  armor  for  the  leg.  —  ME.  greve,  fr.
---- find page marker near line 16639 ----
1:grate,  n.,  a  frame  of  metal  bars.  —  ME.  grate, fr.  ML.  grata,  ‘lattice’  (whence  also  It.  grata, ‘grate,  gridiron’),  fr.  L.  cratis,  ‘wickerwork, hurdle’.  See  crate  and  cp.  graticule,  griddle, hurdle.
2:Derivative:  grate,  tr.  v.,  to  furnish  with  a  grate, grateful,  adj.  —  Formed  with  suff.  -ful  from  ob- sol.  grate,  ‘agreable,  thankful’,  fr.  L.  grdtus, ‘agreable,  grateful’,  whence  gratia,  ‘kindness, loveliness’.  See  grace,  n.,  and  cp.  words  there referred  to.
3:Derivatives:  grateful-ly,  adv. graticule,  n.,  a  design  divided  into  squares.  —  F., fr.  ML.  graticula,  ‘gridiron’,  dimin.  of  grata. See  grate,  ‘frame  of  metal  bars’,  and  -cule. gratification,  n.  —  L.  gratificdtio,  gen.  -onis, ‘obligingness,  complaisance’,  fr.  gratificatus, pp.  of  gratificari.  See  next  word  and  -ation. gratify,  tr,  v.,  to  please.  —  F.  gratifier,  fr.  L.  gra- tificdre,  a  collateral  form  of  gratificari,  ‘to  do favor  to,  to  oblige,  gratify’,  formed  fr.  grdtus, ‘agreeable,  grateful’,  and  -ficare,  fr.  facere,  ‘to make,  do’.  See  grace,  n.,  and  -fy.
4:Derivatives:  gratifi-ed,  adj.,  gratifi-ed-ly,  adv., gratifi-er,  n„  gratify-ing,  adj.,  gratify-ing-ly,  adv. gratin,  n.,  light  crust  over  a  dish.  —  F.,  ‘burnt part;  bread  crumbs’,  fr.  OF.  grater  (F.  gratter), ‘to  scrape,  scratch’,  of  Teut.  origin.  See  grate, ‘to  scrape’.
5:gratinate,  tr.  v.,  to  cook  until  a  crust  is  formed.  — Formed  with  verbal  suff.  -ate  fr.  F.  graliner, ‘to  prepare  a  dish  with  bread  crumbs’,  fr.  gratin. See  prec.  word.
=== leaf index of greave ===
charpos 4188420
leaf(0-based formfeeds before): 366
```


## [2026-09-06T02:17:55.045Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','IEC','HUB','HRN','BQT','MON','ARB','FVF','LKT','PHD','NYB','LEW','LAT','POK','AHD','SYN','RCH','ARY','CHEUNG','WEB','FSD','TTS','DEV','PHN']:\n  v=d[k]; print('==',k, '|', v.get('page_offset'), '|', str(v.get('lookup_hint'))[:300])\n\""
}
```


### [2026-09-06T02:17:56.753Z] TOOL RESULT

```
Exit code 1
== KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== IEC | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== HRN | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== BQT | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== ARB | None | Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
== FVF | None | Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.
== LKT | leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== PHD | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== LEW | 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== POK | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== AHD | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== SYN | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== RCH | leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are Persian/Arabic in script (poorly OCRed) followed by transliteration and English gloss; grep the English gloss or transliteration.
== ARY | printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARYTraceback (most recent call last):
  File "<string>", line 4, in <module>
KeyError: 'CHEUNG'
```


## [2026-09-06T02:18:10.723Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i in (364,365,366,367):\n    p=pages[i]\n    print('--- leaf',i,'first 200:',repr(p[:200]))\n    print('    last 200:',repr(p[-200:]))\nEOF"
}
```


### [2026-09-06T02:18:12.541Z] TOOL RESULT

```
--- leaf 364 first 200: 'tter’, lit.  ‘that  which  is  written’,  from  the  stem  of ypatpEiv,  ‘to  write’.  See  -graph  and  cp.  gramarye, grammatical.\ngrammarian,  n.,  a  student  of,  or  an  expert  in, grammar.  — '
    last 200: 'nel.  —  OF.  *gra - pelle,  dimin.  of  grape,  ‘hook’.  See  grape  and  cp. prec.  word.\nDerivatives:  grapple,  tr.  and  intr.  v.,  grappl-er, n.,  grappl-ing,  n.\ngrapsoid,  adj.,  pertaining  '
--- leaf 365 first 200: 'to  the  genus  Grapsus (zool.)  —  Lit.  ‘resembling  a  crab’.  See  Grap- sus  and  -oid.\nGrapsus,  n.,  a  genus  of  crabs  (zool.)  —  ModL., fr.  Gk.  Ypa+aio?,  ‘crab’,  which  is  of  uncerta'
    last 200: '  gra,  G.  gran,  ‘gray’,  and  cogn.  with  L. rdvus,  ‘gray’.  See  roan,  ‘chestnut-colored’,  and cp.  grizzle,  ‘gray’,  and  words  there  referred to.\nDerivatives :  gray,  grey,  n.  and  tr.'
--- leaf 366 first 200: '  and  intr.  v., gray-ish,  adj.,  gray-ly,  adv.,  gray-ness,  n. graylag,  greylag,  n.,  the  gray  goose.  —  Short  for gray  lag  goose,  i.e.  ‘the  gray  lagging  goose’  (see lag,  adj.,  an'
    last 200: 'gridelin ,  lit.  ‘gray  of  flax’,  i.e.  ‘flax  gray’.  For the  etymology  of  gris  see  grizzle,  adj. ;  de,  ‘from, of’,  comes  fr.  L.  de,  ‘away  from,  from’  (see de-) ;  tin,  ‘flax,  li'
--- leaf 367 first 200: 'nen’,  derives  fr.  L.  linum  (see linen).\ngridiron,  n.  —  ME.  gredirne,  gridirne,  folk- etymological  variants  of  ME.  gredire,  gridire (due  to  a  confusion  of  the  ending  -ire  with  '
    last 200: 'nd  and  cp.  gristle, grist,  n.,  size  of  rope.  —  Of  uncertain  origin; perh.  rel.  to  gird,  ‘to  encircle’, gristle,  n.,  cartilage.  —  ME.  gristil,  fr.  OE.  gristle, rel.  to  OFris.,'
```


## [2026-09-06T02:18:20.554Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gurdos\\|gurdus\\|gṛdos\\|gṛdus\\|g\\.rdos\" IEC.txt | head -20; echo \"=== leaf around p307 ===\"; python3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(len(pages))\n# leaf ~ p/2+15 -> p307 -> leaf ~168 ; p373 -> leaf ~201\nfor i in (167,168,169):\n    print('=== leaf',i,'===')\n    print(pages[i][:1500])\nEOF"
}
```


### [2026-09-06T02:18:22.318Z] TOOL RESULT

```
4505:gurdos, ios, us ‘swollen, proud, stout, brave, violent. (This form is often coincidental with type *gurdus ‘sluggish, ponderous, awkward’, etc. an extn. of type *gurus “heavy” with various extns. of type *guriu-, guruu-, gureio, gurnd-, etc.). WP I, 641, 649-650, II, 278 Skt. gudah (^ball. WP I, 614); Per. (ambig. OPer.?) gurd ‘hero’; Oss. qal (1) ‘proud’; Arm. cf. kord ‘rough’, beside nkrtem “try”?; OW. W gwrdd ‘stout, fierce; OCS grüdü ‘proud; horrid’; R. gordyj, Cz. hrdý ‘proud’; Blg. grád, gård ‘ugly’; Srb. gfd ‘ugly; gi- gantic'; OE cf. cyrten ‘intelligent’. (The near- homophone gurd-, q.v. seems to be present in Skt. jadah; Per. gül; Oss.Dig. $ála; Gk. bradús, LW in Lat. bardus; Lat. (Late-Lat. or Hispano-Lat.) gurdus; Li. gurdùs; Latv. gurds)
5401:gurdos, us (form of gurdos, us, q.v.) “slug- gish, stupid, stiff, awkward'. Cf. WP I, 641 & II, 278 and gurndis Per. gül “idiot”; Oss. qal ‘proud’: Dig. $àla (‘stu- pid'. Abaev); Arm. (Iran. LW?) kurt ‘eunuch’; Gk. bradüs ‘sluggish’; LW in Lat. bardus 'slug- gish, stupid; Lat. gurdus “stupid? (in LL: *blunt); W brydd ‘weak’; Pol. gardy ‘finicky’; Blg. grád ‘ugly’; Srb. grd ‘ugly, monstrous, dirty, nasty’; Slovene gfd also: ‘naughty’; Cz. hrd ‘proud’; Lusat. hordy, id.; Pol. cf. also wz- garda ‘contempt’ beside gardzić ‘despise’; Li. gurdùs ‘sluggish, ailing, weak’; Latv. gurds ‘tired, faint’
5426:gurndis “heavy, bulky'. WP I, 699. Cf. gurus, gurdos (gurdos) Per. cf. garan ‘heavy; expensive’; Alb. (LW?) i rándé, i rëndë, adj. “heavy”; Lat. grandis ‘big’; Tokh. A. (ambig.) krant, krent “lovely”
=== leaf around p307 ===
858
=== leaf 167 ===
ub, mud’; OE clæman ‘to smear’; clam ‘daub’; ON kleima,
gliu- (glou-) ]— glomor-
10
20
25
30
35
40
45
280
v. id.; Sw. klema ‘pamper’; Cz. cf. hlem-yzd (Canal For -yZd' see ūĝā, io & cf. Lat. vesper- ügo); Li. cf. gliem-eZiai, pl. ‘molluscs’; Latv. glaimi, pl. ‘flattery’; gliemis ‘mollusc’; gliem- ezis ‘snail, mussel’
(gloin-, gloip-, gloist-, formulae implied for OCS glénü ‘mucus’; Slk. hlien ‘mud’; Alb. glepë ‘rheum’; and Li. glaistas ‘mortar, putty’ respectively. Cf. gloi- and derivatives)
gloitos ‘compact, sticking, sticky; mucus,
glue’. Cf. gloi- & derivs. & WP I, 620. Cf. also glot-, à, io, gleu-, glü-, etc. Lat. (ambig.) glütus ‘compact’; glüten ‘glue, solder’; Olr. (ambig.) gláed ('glue'. See gloiios) beside glaedaim ‘adhere’; gláeta (pp. :glued"); W glud ‘sticky; glue’; Br. glüd ‘glue’; OCor. glut, Cor. gloes, id.; gloeja (for gloedZa, v. *stick&); MHG kleit, gs -des “garment; animal- skin; cloth” and com. Gmc.; Li. cf. glaistas ‘smear, grease, glaze, mortar, putty’
gloiobha ‘clod, sod”. Cf. gloi- and derivs. Lat. glaeba, glëba; R glyba; Pol. gleba (e for y as in ser: R syr, m. (cheese). (For the pho- nology cf. IE *quoie implied in Gk. poía, Ionic koíé: Lat. quae; OCS kaja beside m. kv)
glombos, ios (1) “mass, lump, clump'. Cf. WP I, 616 & glembó Sw. klamp “lump, stump’; Fris. klampe “pile; swollen ankle’, beside Norw. klepp “lump, dough-ball’; ON kleppr “lump; plummet’; Cz. hloub, Slovak hlúb ‘cabbage-stump’; Pol. glab, id. (Isophonic: SGer. Klampfe, LG klampe 'clam
=== leaf 168 ===
klāt ‘Jump’; Du. kloot ‘ball, testis; Blg. glužd (“not in wood, fr. *eloudio); (E cleat ‘bat- te1 1s of uncertain background, cf. OE clēot for *cleat ? ‘poultice’ or sim.)
glom&- (glong-) — glüd-
10
20
25
30
35
40
45
282
gloudhros, see gleudh-
gloumos, à ‘slime, grease’. Fris. (ambig.) kliem ‘ointment; klieme, v. ‘make stick, smear’; Li. glaumaf, pl. ‘mucus’
(glout-, see gleu-, glūt- and cf. gloit-). WP I, 618-9
glubo, io (glüb-) (1) ‘seize, clutch? LG kluppen; OE clyppan; Upper G cf. Klupf ‘fright; MHG kKlupf, id.; G (fr. LG) Kluppe ‘calipers; pliers; Du. cf. kloft ‘knot, tuft; ON (*-ü-) kiýpa ‘pinch’; Norw. klype, id.; cf. Li. (*-ou-) glaubiù, ^ti; OCS glúbljo, glú- běti & glübiti ‘seize’
(glubo, ið (2). Gmc. only: OHG chlopfon, LG kioppen; Du. id.)
glubh- ‘cut open, split’. Cf. gleubh-. WP I, 661 Hitt. cf. kullupi ‘digger’; Gk. glüpho, glüpto ‘gouge, carve’; gluphis ‘notch, of arrow’; MHG klobe ‘slit, chink; peg, wedge’; OFris. klova ‘cleft, division’; OE dote ‘buckle’; ON klofi, klof ‘cleft, groove; fork of legs’; G Kloben ‘chip, log, socket, clamp’; MHG kloben, v. ‘split; ON klyfja, id. beside klofna, id. Long-gde in MHG klüben ‘chip off; rob’. (Isophonic are MHG klobe ‘bundle, faggot’: OE clufu ‘clove of garlic’; OS kluf-lók ‘garlic’; EME clove of wool ‘bale of wool; Fris. klobbe ‘lump’; ON klyf “pack, truss’; Sw. klubb ‘lump’; klubba ‘cudgel, club’, w. expres- sive doubling). Lat. glüma ‘husk, glume’ is preferably to Li. gliaudas ‘husk’ qua *gleudma, see gleud-. See, h
=== leaf 169 ===
g, group; ball of (bread: Cz. s-hluk, dim. hloucek ‘group, gang’
glüt- (1) ‘guip, swallow’; gluto(n), glutən- ‘gullet Oss. qürtt ‘gulp’; Lat. glutio, ire, v.; gluto, gs.-onis ‘glutton’; gluttus ‘gullet, foodpipe'; Ir. glota, gs. glotan ‘gullet’; cf. glothar ‘gurgle’; Gaelic glut ‘voracity’; glutair ‘glutton’; Br. glut ‘gluttonous; glutton'; OCS glüsto, glütiti “swallow? (= Lat. glutio); Cz. hlt ‘gulp’; hitan, hltoii ‘glutton’; Slovene gólt, m. ‘gullet’; Ukr. (*-ū-) hlytaty (devour ; Cz. hltati, id.);
compact. Cf. glemb-,
gluks- — gnambhio
20
25
30
35
40
45
284
variant: R glot, glotok ‘gulp’; glotat', v. “swal- low?
glut- (2) “stuck, adhered; sticky; mucus, lump, cluster. WP I, 621, Cf. gleu-, glu-, gloit-, etc. Lat. (ambig.) glütus ‘compact’; glüs, gs glütis ‘glue’; MHG klūde ‘bale’; cf. E clod (fr. *glutós) and Du. klodder ‘blotch, blob’; Mir. and Ir. diüth, dlüith, adj. compact
glb- (glbh-) Lat. galba *meat-maggot'; galbulus 'cypress- cone’; (either) Du. kollop ‘puck in icehockey, chock, polo-bal; EME collop “lump of lard for frying; LG külp ‘bulging eye’; kulp-ig ‘fat, blunt’; külpen, pl. “hard unripe fruit’ (fr. *glb-), (or) OHG kolbo ‘cudgel’; Du. kolf “butt of gun’; Sw. kolb “club, pommel’; ON kólfr *bell-clapper'; kylfi, id. & kylfa ‘cudger. (Isophonic is Ir. glib, gliob, f. “lock of hair, tress’, as also Li. gilbstü, gilbti “get well)
glgos ‘gulp, gurgle’. Cf. gulg-, gulgul-, gu- lug-, guluk-, gərgəl-, etc. Ir. glug ‘gurgle’; MHG kolc, gs kolkes ‘eddy’; Du kolk, id.;
```


## [2026-09-06T02:18:35.054Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['gurdos, ios, us','gurdos, us (form of']:\n    i=d.find(pat)\n    leaf=d[:i].count('\\f')\n    print(pat,'-> leaf',leaf)\npages=d.split('\\f')\nfor L in (180,181,213,214):\n    nums=re.findall(r'\\n(\\d{3})\\n',pages[L])\n    print('leaf',L,'nums',nums)\nEOF"
}
```


### [2026-09-06T02:18:36.659Z] TOOL RESULT

```
gurdos, ios, us -> leaf 181
gurdos, us (form of -> leaf 217
leaf 180 nums ['304', '305']
leaf 181 nums ['306', '307']
leaf 213 nums ['365', '366']
leaf 214 nums ['367', '368']
```


## [2026-09-06T02:18:40.975Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaf217 nums',re.findall(r'\\n(\\d{3})\\n',pages[217]))\ni=d.find('gurdos, ios, us'); print(repr(d[i-400:i+40]))\nj=d.find('gurdos, us (form of'); print(repr(d[j-400:j+40]))\nEOF"
}
```


### [2026-09-06T02:18:42.918Z] TOOL RESULT

```
leaf217 nums ['373']
', sty, cage, pit? (LW in Cz. koba ‘small room’, kobka \'cel); OE cofa ‘closet, ark, cave, den E cove; ON kofi “hut, cell; Du. cf. kof (?) “kind of boat: LG Kofen; G Koben “sty, hovel\ngür- (1) “squat, idle, lounge ON kúra, MLG küren, G kauern, id.; E to cower; OSw. kura; Cz. hytit, id.; Li. güris idler”; j-gürinti (2) "be huddled\'; güràties idle\ngür- (?) (2) ‘cover Per. gür ‘tomb’; Sw. kur ‘awning’\ngurdos, ios, us ‘swollen, proud, stout, '
'gur- (2) ‘heavy’. See gurus\ngur- (3) ‘appellation, song, praise; revere, sacrifice, worship’. Cf. gurdh- (1) and gurtos Skt. giráh, gir ‘praise’; Lat. au-gur, gs -guris, au-guria (here despite WH); Li. giriü, ti ‘praise’; gyrà ‘boasting’\ngurbh- (?) ‘thrive’. Evidence ambig. Vedic grbhnámi “welcome, accept, be fruitful; pp. grbhitáh, pp. ‘fruitful’; Li. gurbstü, gurbti ‘thrive’; gurbüs *Iuxuriant?\ngurdos, us (form of gurdos, us, q.v.) “s'
```


## [2026-09-06T02:19:01.245Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD gurd ===\"; grep -n \"^gurd\\|^gwrd\\|gurd \" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"^gurt\\|^gurd\\|gurt \" NYB_vol2_glossary.txt | head -20; echo \"=== HRN ===\"; grep -n -i \"gurd\\|gurt\" HRN.txt | head -20"
}
```


### [2026-09-06T02:19:01.327Z] TOOL RESULT

```
=== PHD gurd ===
PHD.txt:5444:gurgānīg gursagih gursag durgar jorda jorda 1-2gurdih gurd gurdwar gurdag dum, 1021 joma jomā gumānīh gumānīgīh gumānīg gumān gumāngar gumār- gumārdan gumārdag jumb- dumbēmand jumbāgīh jumbīh-
PHD_mackenzie.txt:2621:gurd [gwlt' I P gwrd, N......,] hero.
PHD_mackenzie.txt:2623:gurdag [gwltk I N ......,a] kidney.
PHD_mackenzie.txt:2626:gurdwar [gwltw'l] befitting a hero.
PHD_mackenzie.txt:10727:gurd
PHD_mackenzie.txt:10730:gurdwar            \..,~"          gug.ay                   -OWJt'
PHD_mackenzie.txt:10731:gurdag                \~~     .    gugayih
=== NYB ===
1730:gurtéh
1744:gurtéh [gwltyh] a part of the warrior’s armour, *neck-protector’ 855. Skr ren- ders the series zen u zréh u ~ by sarva- sannüha- = tavoTaAta. — gurt- < *kur-t- from the root kur- discussed by Bailey, Nyberg Vol. 9-16: Av. (474) kuirit- (< kurit), nom. kwiris, Vd. 14°, following immediately after zräöö (v. zreh) in the enumeration of a Zoroastrian warrior’s armour, is rendered in Phl. by griv-pan ‘neck-protector’ with the gl. han i hac tarak apác 6 zre bast estet ‘that which is attached to the helmet at the back of the armour’. — Cf gri-kaft.
1748:gurt-vär [gwltw'l] worthy of a hero, heroic 272’, 281. — MPrthPrs gwrd (S, A-H III); NP gurd.
7173:gurd: gurt-var
=== HRN ===
1682:§ähn. P. VI, 270, Vers 1331: ba merd-t gurd ser-l
5490:ai. ragandr 'Strick, Riemen, Zügel, Gurt'; arm. LW.
7441:aw. kasa- 'Achselhöhle'; phlv. kas; ai. kdksa- 'Gurt-
7443:bei. LW. kaB^ kos 'Gurt, Riemen, Achselgrube' (130);
7806:899. gurd 'Held'.
7808:phlv. gurt 'Held' (AV.), gurtlh vd. 20 (21).
7813:Dialektisch (K*ä§än, Q.) bedeutet (jurd, gurdl *hoch,
7857:(ZPGl.) ; phlv. gurtak ; ai.-präkr. (Du.) vfkkd- *Nieren'.
7858:kurd. gurdale (H. -Seh.), gu7*cik{y)\ bei. guttiy;
18473:K. gurd 899.
19263:gurdale 905, 929 Anm.
```


## [2026-09-06T02:19:02.173Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(len(pages))\nprint(pages[101][:3000])\nEOF"
}
```


### [2026-09-06T02:19:03.658Z] TOOL RESULT

```
300
— 91 —
umgekehrt wie Prellwitz, Etym. Wb. der griech.
Sprache meint).
892. Darmesteter iibersetzt zd. vUara- durch allee' und
vergleicht np. gtiJar a ferry, a passage* (vgl. guSar
*Durchgang'). Auch unsicher.
893. Np. guddSta/n =- 'vorbei lassen, passiren lassen, lassen'
ist Causativum zu gudastan Voriibergehen , vorbei-
gehen, vergehen'.
895. Np. garr *Kratze' stimmt jedenfalls lautlich voU-
kommen zu zd. garenu^.
897. Vullers hat gurdzldan (mit u) einherstolzieren,
ebenso Sal. Shuk. gurdztdan *sieh wiegend gehn\
Fr. Miiller, WZKM. 8, 189 stellt das Wort zu gurdz
*£ber , ich halte an der Zusammenstellung mit skr.
vraj fest.
898. Np. girdn *schwer = ap. ^grana-?
899. Vgl. zd. vareti' in hqmvareti- *Tapferkeit\ Phi. gurt
steht fiir alteres *vurt = ap. "^vrta-.
900. Vgl. auch ZDMtt. 30, 138—141. Das in der Note
angefiihrte vird 'Schiiler hat keinesfalls etwas mit np.
sdgird 'Schiiler' = phi. asdkert zu thun.
901. Np. gird 'Umkreis, rund, rings* liegt im Phi. als
g(i)rt vor, vgl. Phi. Vd. p. 211, Z. 9, Bdh. Gl. 219,
6uj. Abal. 74 u. s. w. und das dazu gehOrige gird<i
rundes Brot' ^= arab. jardaqa im Armenischen als
grtak *Laib Brot', das ein phi. *girtak voraussetzt.
Ich wtirde danach als Grundform ap. *grta- ansetzen.
Dem steht allerdings die ansprechende Zusammen-
stellung von np. gird mit skr. vart *sich drehen' == np.
gardidan entgegen. Aber skr. *varta- ware = phi.
*vart = np. *gard, skr. "^vHa^ = phi. *giirt = np.
*gurd. Das von Horn erwahnte phi. vartdk ist seiner
Bedeutung nach dunkel.
902. Np. gard *Staub* = phi. vart ^Staub', Yfitk. i. Zar. 68,
Anm. 69.
908. Die Etym. ist m5glich, aber unsicher, so lange der
Beweis fiir die Entstehung von g aus v nicht aus dem
```


## [2026-09-06T02:19:24.216Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\ni=d.find(\"899. gurd 'Held'\")\nleaf=d[:i].count('\\f')\nprint('leaf',leaf,'-> printed p',leaf-21)\npages=d.split('\\f')\nprint(pages[leaf][:2500])\nEOF"
}
```


### [2026-09-06T02:19:25.841Z] TOOL RESULT

```
leaf 221 -> printed p 200
— 200 —
895. ger, gerr (AM. 28 Zeile 4) ^Krätze.
aw. garenu' *Krätze' vd. 7, 58 (145), yt. 13, 131
(Darmesteter, ebenso Jackson, der Amer. or. Soc.
Proc. 1889, XXV und Avesta Grammar § 806 ai.
gfdhnü' vergleicht; Geldner übersetzt KZ. 25, 551
^Sonnenglut' , Bartholomae, Studien II, 96 Trost',
cfr. lat. gelu^ ksl. zUdica^ nhd. kalt), also unsicher;
phlv. gar [skr. gard- *eine Krankheit' bezeichnet nach
dem PW. wahrscheinlich Schlingbeschwerden oder
ähnliches],
LW. kurd. gv' 'Krätze'; bei. gar ^Aussatz, Räude,
Krätze' (69) ; vergl. nslov. gar je *Krätze', garjaOj garat
^kratzen' (Miklosich, Denkschr. WAW. Band 37, 40).
896. guräz *Eber .
aw. varäza- 'Eber ; phlv. varOz (geschrieben varoc),
arm. LW. varaz, vgl. Varazdat, Baoa^rj^, OvuQoiCfjg
(Armenier); ai. varähd- *Eber'.
kurd. heräz,
V
np. veraz *Eber' wird im FS (Vullers) durch einen
V
angeblichen Sähnämevers belegt, der aber des Metrums
halber kein solcher sein kann.
897. geräziden 'schreiten .
ai. V^vra}', vrdjati schreiten, gehen, fortgehen'
(Rückert, ZDMG. 10, 165).
898. girun 'schwer.
Kä§. gerün, gurun^ guro.
Vergl. aw. gouru- (d. i. garii-) ^) in gouru.zaodra-
unlustiger Opferer' (Geldner); phlv. gar an 'schwer ^);
ai. gurü' 'schwer, vergl. Comp, gdrtyas-^ Sup. gdrisfha-.
Die Grundform hatte einen r- Vokal.
899. gurd 'Held'.
[/^var- 'beschützen, wehren', vergl. ai. vft- 'Heer ;
phlv. gurt 'Held' (AV.), gurtlh vd. 20 (21).
*) Bartholomae, Handbuch § 8.
*) Gehört hierher auch das rätselhafte phlv. grM (vd. 5 (48) GH.,
z. B. hi^-l gräi 'grosse Unreinheit*?), vergl. np. giräi No. 5 bei
Vullers?
```


## [2026-09-06T02:19:36.967Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN gul ===\"; grep -n \"g[uû]l 'D\\|gül\\|gul 'ein\\|Dummkopf\\|Tor'\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n -i \"dumm\\|Tor\\b\" HUB.txt | head -20"
}
```


### [2026-09-06T02:19:37.039Z] TOOL RESULT

```
=== HRN gul ===
304:gültig an; hierhin gehören Fälle wie kusäden. Und nicht
1533:vergl. skr. atlgün-, angüli- Tinger, Zehe'.
16080:gülirarl 941^
=== HUB ===
67:an den Autor nicht immer billige Anforderungen gestellt
949:an ancestor, 2) great, venerable'.
1086:Anteir (vgl. np, baxt 'Schicksal, Gliick* =^ skr. bhaktor-
1344:im Neupersischen *barvez anstatt parvez Victor, felix,
1346:p^rdz Victor, felix, faustus ?
1535:354. Np. peroz Victor, felix, faustus' kann nicht = zd.
2499:um zahr = zahra auf ap. "^zartor- = "^zartaka- gelb'
4653:= zd. mq^rem spentem; np. tOr *Aufzug beim Gewebe* =
4707:= phi. framatOr^), ap. framatar- 'Gebieter (ace. frama-
6087:ustun - sutun 'Saule' ; ustor = sutor *Ross'; uspurz = supurz
6104:'loben*, zd. stw, sutor ^Ross' = zd. staora-; siitun Saiile*
6271:np. Savur als Var. bei Vullers; parvez Victor, felix*
6273:vielleicht beeinflusst durch perGz victor, felix' (s. oben p. 40).
7271:pahragban 'Wache', talmud. KiD^ims *Polizeidirektor' (Hoff-
8226:bazban (Fird. II, 740, 1053), bazvan ^exactor vectigalium' ; ba-
9242:k) Ap. pm = np. m : raiman *dolorum structor H. 643 ?
```


## [2026-09-06T02:19:37.806Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\nd=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\n# find pdf page tags\nfor i,p in enumerate(pages[:3]):\n    print(i, p[:200].replace('\\n','|'))\nEOF"
}
```


### [2026-09-06T02:19:39.263Z] TOOL RESULT

```
leaves 721
0 [pdf page 1]|[NOT OCRED - use tools/ref_page.py]|
1 [pdf page 2]|7|Ub|sits k ge|AS ۱۰۶۲ ‏نتف‌بال‎|‏ومع‎ ‘oo ‏داي و‎ el Oe||far|en rotons ‘ ‘ ths ۰ ‏دیهان‎|‎۳ 2 7|۰ SF Ps|On Awe|۰|‏-ل‎ 9 ‘il|۱۳۴۳ ‏چاپ دوم فروردین‎|‏با تجدید نظر کامل‎|‏بسرمایه کتاپفروشی 
2 [pdf page 3]|اداره ‎“oes‏|‏ساره و6۷ ۲۰۹||pe ۰ ay sf s ‏ار بخ‎|‏سرام ودارت‌شسات‎||د انشمند محتر ,آقای‌د کترحمد معین‌استاد د انشگاه تهران|درپاسخ نامه مورخ ۲۳ اشعارمیدارد :|‎ool‏ حقوق تجد ید طبع کتاب پره
```


## [2026-09-06T02:19:42.771Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1786 --image 2>&1 | tail -60"
}
```


### [2026-09-06T02:19:50.921Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1786.png
REF: BQT:1786  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 583  OCR-lang: fas

کرختن -۱۷۸۹-
بممتی کر بچه. است که تالار وخانة كکوچك باشد | اهست؟ - وکردون وفلك را هم میگوبند 9 -
و نقب - وزبر زمین -وچاه - و زنداترا نیز | یکی از نامهای آفتاب‌است - وبمعنی بوی‌خوش
کویند . باشد -- ونقع‌وفایده ومنفمت راکویند - وعکی
گرختن! - بنم اول. مخفنف کربختن را نیز کفته‌اند ‎٩‏ - و بمعنی غم و اندوه ۷
است . وشادی وبیغمی لیز آمده‌است؛ ودرین دومعنی از
گرد - بفتح اول و سکون ثانی و دای | اضداداست - وبرق راهم گفته‌اند وآن‌فملهاست
ابجد » خاك راکوبند ۴ - وخاك برانگیخته را که بوقت باریدن بلران در هوا بهم میرسد -
خصوصا۴ -وبمعنی کردیدن وچرخ‌زدن-و کردنده وجنسی از ابریشم وابریشمینه باشد ۸ - و پم
وگردان - وامر بگردیدن وچرخ زدن (۱) هم | اول, مبارز ودلاوروبهادر وشجاع راکوبند ‎٩‏ -
(۱) چش : - وکردنده ... چرخ زدن .
۹ - رك : گربختن .
۲ -تن بی روح چیست ؟ هشتی کرد روح بی علم چیست ؟ پادی سرد .
اوحدی «فرهنکه نظام» .
۴ - بعنی غبار . رك. : رشیدی » هندی باستان - ۷2۳۲, ۷4۳1218 (چرخیدن).وخیع
4 » منجی 88781 «اسشق ۰۹۶۲ پپلوی ۷8۳۸ (کردء غبار) «هوبشمان ۹*۲ .
۴ - رشه ۶ گردیدن » است . 8 -اسم فاعل مرخم بمعنی کردنده و مجازل
آسمان وفلك :
به پیران چنین گفت‌کامرو ز کرد نه بر آرزو کشت گاه نبرد .
*فردوسی طوسی شاهنامةٌ بخ ج 4ص ۹*۸ ورك : فهرست ولف .
‎٩‏ - جهانگیری این معنی را آورده وبیت ذبل را از انوری شاهد آن قرار داده :
کر خام نبسته است صبارنگه رباحین از گرد چرا رنگه دهد آب روان را ؟
رشیدی پس از نقل قول ,جهانگیری کوید : « اما ظاهراً درين نت «کرده» باید خواند
نه‌کرد . > . مولف سراج اللفه بر جهانگیری اعتراض کرده وگفته اگر رنگه چیزی خام باشد
وقت شتن خود رنگه در آب میریزد له عکس آن . پس هعتی شمر این است که صبا رنگه
رباحین را خام بسته است که رنگه مشکل کرد درآب ريخته رنگین کرده است . در این معنی‌لفظ
«کرد» در شمر مد کور بمعنی اول است «بنقل فرهنگه نظام > » اما همین بیت در دیوان آلوری
چاپ تبریز ص؟ ولیز در نسخهةٌ خطی متعلق بکتابخانهٌ دهخدا چنین آمده :
گرخام نهبتشت صبا رنگه رباحین ازعکی چرا رنگه دهدآب روانرا؟
وشاید موْلف جهانگیری‌بانقابل سخ» معنی مذ کور را برای «کرد» استنباط کرده است.
۷ - ز تنهائی مگرکردی بدل داشت ‏ از سودای درون دردی بدل داشغت .
خوارزمی «فرهنگك نظام» ۰
۸ رك : جهانگیری . ‎٩‏ - در پهلوی 81۳1 . از ریشه]3۷۳ پارسی‌باستان-
-0۷718 «هوبشمان ۸۹۹ ۰ در لهجد‌کاشان 81701.81۳0 (بلند . بلندی) «اسشق ۸۹۹ :
بهومان چنین گفت سهرا ب کرد که اندیشه ازدل بباید مترد .
فردوسی طوسی «لغت فری ۶۹۸ -
( برهان قاطع ۳۳۸ )
```


## [2026-09-06T02:20:19.648Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BQT; cat > data/verification/sources/refs/ocr/BQT/1786.vision.txt <<'EOF'\n[Read from the rendered image data/verification/sources/refs/ocr/BQT/1786.png = BQT_v3_picofile.pdf pdf page 583.\n NOTE: the running head of this leaf prints ۱۷۸۹ (p. 1789), i.e. the scan runs ~3 pages ahead of\n Nourai's citation BQT:1786; the گرد entry he means is this one.]\n\nHeadword and senses (col. 2):\nگرد - بفتح اول و سکون ثانی و دال ابجد، خاک را گویند ...\n  و بمعنی گردیدن و چرخ زدن - و گردنده و گردان ...\n  و بفتح اول، مبارز و دلاور و بهادر و شجاع را گویند ۹\n\nMo'in's footnotes on the same page:\n ۴ - یعنی غبار. رک: رشیدی، هندی باستان ... پهلوی vard (گرد، غبار)، هوبشمان ۹۰۲.\n ۹ - در پهلوی gurt . از ریشهٔ var ، پارسی باستان -vrta- ، «هوبشمان ۸۹۹». در لهجهٔ کاشان\n     gurd/gurdi (بلند، بلندی)، «اشتق ۸۹۹»:\n       بهومان چنین گفت سهراب گرد\n       که اندیشه از دل بباید سترد.\n     فردوسی طوسی «لغت فرس ۶۹۸»\nEOF\necho saved; ls -la data/verification/sources/refs/ocr/BQT/ | head"
}
```


## [2026-09-06T02:20:20.594Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON part files size ===\"; wc -c MON_part1.txt MON_part2.txt; echo \"=== گوراب ===\"; grep -c \"گوراب\" MON_part1.txt MON_part2.txt; grep -n \"گوراب\" MON_part1.txt MON_part2.txt | head -5; echo \"=== جوراب ===\"; grep -n \"جوراب\" MON_part1.txt MON_part2.txt | head -5; echo \"=== گول ===\"; grep -n \"گول\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T02:20:21.376Z] TOOL RESULT

```
saved
total 16824
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 22:20 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb 368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb   1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb 534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb   2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 446843 Sep  4 13:39 1225.png
-rw-rw-r--  1 sfmqrb sfmqrb   4412 Sep  4 13:39 1225.txt
```


### [2026-09-06T02:20:21.494Z] TOOL RESULT

```
=== MON part files size ===
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
=== گوراب ===
MON_part2.txt:2
MON_part1.txt:1
MON_part2.txt:35979:گوراب: و [- گورابه] (امر.) گنبدی 
MON_part2.txt:35982:گوراب: ۲0و [قس. کوراب] (امر.) زمین 
MON_part1.txt:48890:جورات: 0 |- گوراب - گورب] 1( 
=== جوراب ===
MON_part2.txt:5126:می‌دارند با به جوراب يا کرست و با پستان‌ها 
MON_part2.txt:23182:از آن برای تنگک کردن دهانهٌ جوراب (در 
MON_part2.txt:23184:استفاده کنند: جوراب کش. 
MON_part2.txt:33120:قروین» گل گیوه» کل جوراب. گل شوره: 
MON_part2.txt:73893:بر بافتن جوراب که بجای ابریشم در آن بکار 
=== گول ===
MON_part2.txt:358:گول زردن» فرب دادن اغفال. 
MON_part2.txt:611:غاوت: 2۷۱ [ع. . غباوة] (مص‌ل.) گول 
MON_part2.txt:612:گردیدن. ابله شدن. (امص.) گولی. ابلهی» 
MON_part2.txt:650:غبی: [ا (ص.) کند ذهن» گول» کم فهم. 
MON_part2.txt:658:غبین: زرا [ع.] (ص.) سست خرد» گول»
```


## [2026-09-06T02:20:28.354Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '48880,48900p' MON_part1.txt; echo \"=== part2 35970-35995 ===\"; sed -n '35970,35995p' MON_part2.txt; echo \"=== page markers? ===\"; grep -c $'\\f' MON_part1.txt MON_part2.txt; head -3 MON_part1.txt"
}
```


### [2026-09-06T02:20:30.297Z] TOOL RESULT

```
جور: 12۷0070 (ع.] (سصل.) ستم 
کردن) سل کردن: (.) ستم ظلم. یکی از 
پیالةٌ جور بیالهٌ مالامال است. 

جور: تا[ (ا.) نوع» گونه قسم. (جان. کیا.) 


ناجور. (عم. ۱ ۷۳۳ 

جورات: 0 |- گوراب - گورب] 1( 
پایتبه‌ای که آن را از نخ‌های پنبه‌ای یا پشمی 
و با ابرشمی بافند و با را بدان پوشانند؛ ج. 
(ع.) جوراب. 

چسوزاعند: (.04)0۷درق جع[ [- 
گوزآ گند - جوزغند] (امر.) هلو یا شفتالوی 
خشک کرده که مغز ردو در مبان آن 
آکنده باشد» جوز آ گند» جوزغند. 
جوزیو یا: (.«ملدوودنی- سح[ [- کو ز بو با 
- جوزیواه معر.] (امر.) (گیا.) گیاهی از تیرة 
=== part2 35970-35995 ===
گور (خود) را گم کردن: (عم ۰ (به هنگام 
توهین و تحقیر استعمال ی ) دور شدن؛ 
2 زحمت کردن. 

گور: (قسد. 07)867اع (.) دشت» صحراه 
گورخر. جای بی آب و علف که پشته و 
شکستکی تسار دافته‌راشت, (خان. 4 کرو 
گور سرخ: نوعی اسب. 

گوراب: و [- گورابه] (امر.) گنبدی 
که بر سر قبر سازند. 

گوراب: ۲0و [قس. کوراب] (امر.) زمین 
شوره‌زاری باشد در صحرا که از دور به آب 
ب( کتارن و 
مازندران) محلی که در آن هر هفته یک بار 
بازار تشکیل شود؛ هفته بازار. 

گور اسب: »هت (امر.) (جان.) گونة 
وحشی اسب که مخصوص آفر بقا است. نام 
علمی این حیوان هیپوتیگریس است که 
ترجمهٌ آن به فارسی اسب ببری می‌باشد. 
وجه تسمیه بدان جهت است که سطح بدن 
حیوان دارای خطوط تیره و روشنی است که 
از دور شباهت به پوست ببر پیدا می‌کند. 

=== page markers? ===
MON_part1.txt:0
MON_part2.txt:0
0 
2
```


## [2026-09-06T02:20:45.331Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^گول\\|گول:\" MON_part2.txt | head -10; echo \"---\"; grep -n \"گول\" MON_part2.txt | sed -n '1,40p'"
}
```


### [2026-09-06T02:20:45.450Z] TOOL RESULT

```
358:گول زردن» فرب دادن اغفال. 
7231:گول خورده. سغبون» زیان دیده. شیفته» 
29336:گاگول: اوق (ص.) (عم.) احمق» گیج. 
36823:گول 
36864:گول؛ اتاع ( 
39790:گول. 
67144:منگول: أ-ع۱20 (ص. ) (عم.) یه ز یبا و با 
67146:منگول: (عم.) شاد و با نشاط. صیج: - شنگول 
87919:ویرگول: ]۷ (.) نشانة فاصله در جمله و 
---
358:گول زردن» فرب دادن اغفال. 
611:غاوت: 2۷۱ [ع. . غباوة] (مص‌ل.) گول 
612:گردیدن. ابله شدن. (امص.) گولی. ابلهی» 
650:غبی: [ا (ص.) کند ذهن» گول» کم فهم. 
658:غبین: زرا [ع.] (ص.) سست خرد» گول» 
665:غت؛ ۲ , (ص.) جاهل» نادان. گول؛ کم 
948:غرار: :۱*8 [ع.) (مصل.) گول خوردن» 
1436:امیدوار کردن کسی راه فریفتن» گول زدن. 
1438:بیخبری» غفلت. (ص.) فریفته» گول خورده. 
2780:غافلی» نادانی» گولی؛ احمقی. 
7226:فربب دادن گول زدن» گمراه کردن. مغون 
7227:کردن. (مصل.) فریب خوردن» گول 
7231:گول خورده. سغبون» زیان دیده. شیفته» 
12177:لباس کند؛ ژیگولو. 
24828:زنگوله: کلاه چوبین که زنگله‌ها بدان بندند 
24871:بدو دادن. رسوا کردن. گول زدن» فریفتن (با 
24878:(عم. .) او را گول زدن» فریفتن (با ربودن پول 
27847:و استر) غیر اصیل کندرو و پالانی. گول؛ 
29336:گاگول: اوق (ص.) (عم.) احمق» گیج. 
29779:منگولة دم آنها نیز سفید رنگ است. . پوست 
33239:گل‌هايش به شکل زنگوله و غالا سفید 
33249:سفید و بنفش دارد؛ گل زنگوله» سریس» 
33514:می‌باشد. گل زنگوله: (گیا.) گیاهی است از 
34218:گلاج: 2012 [- گولاج - گولانج| (.) نانی 
36823:گول 
36864:گول؛ اتاع ( 
37834:لاد ه: (0-):۱20 (ص.) احمق» ابله؛ گول. 
39600:زیبا روی. اعجوبه. گول بی‌خرد که او را 
39790:گول. 
55071:و یگولو. ضح. مزلف بر وزن معظم کلم 
61506:(در خرید و فروش و غیره)؛ گول خورده؛ 
61591:و ۱2۳۲ (ع.] (امف.) ) گول حورده. 
67090:(فرعا.جما.) کم هوش؛ گول. 
67144:منگول: أ-ع۱20 (ص. ) (عم.) یه ز یبا و با 
67145:نمکك. راید شنگول (و) 
67146:منگول: (عم.) شاد و با نشاط. صیج: - شنگول 
67147:و منگول و حبکث (حبه) ) انگور نام سه 
67148:غاله است که در قصه شنکول و منگول 
67149:فرزند بز هستند و گرگ شنگول و منگول را 
67152:نگوله: (ع-)داتاع ۵۱۵۵ | ب منگله] (.)
```


## [2026-09-06T02:20:45.649Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T02:20:45.655Z] TOOL RESULT

```


```


## [2026-09-06T02:20:48.469Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36818,36870p' MON_part2.txt"
}
```


### [2026-09-06T02:20:48.524Z] TOOL RESULT

```
؟ رد تاه (۱.) (شیم.) شبه فلری است 
که از ایام قد یم شناخته شده است. عنصری 
است جامد و به رنگ زرد لیمویی؛ نی مره و 


گول 


فررهنگ فارسی معین 


۱ ۱ 


ان سس سس سا کاس دیش تسب تست تسش 


بی‌بو؛ وزن مخصوص آن ۱/۹۵ است و 
در ۱۱۴/۵ درجه دوب شود و در 
۵ درجه به جوش می آید. گوگرد در 
آب محلول است و بهترین حلالش سولفور 
دو کرین است. گوگرد در طبیعت به وفور 
بصورت سولفورها با سولفات‌ها یا بصورت 
اصلی خو بش در حوالی کوه‌های آتشفشان 
یافت می‌شود. گوگرد حرارت و الکتر یسیته 
را هدایت نمی‌کند از این جهت عایق خوبی 
است و به همین مناسبت در صنعت از تر کیب 
وگرد و ک‌ائوچو جسمی بنام ابوئیت 
ی و ها 
صح.- اگر گوگرد مذاب را بطور بط سرد 
کند به شکل سوزن‌های منشوری شکل 
و شوک اف اکن آن را دفعة سرد کنند 
بصورت یک رشته کش‌دار درمیآید و در 
صورتی که گوگرد و محلول در سولفور 
دوکرین تبخیر شود گوگرد در ته ظرف به 
شکل ۸ وجهی‌متبلورمی‌گردد. گوگرد 
احمر: فسفر سرح. ۱ . (کیم.) اکسیر مصنوع در 
غایت سرخیء گوگرد سرخ؛ کبریت احمر. 
گوگرد سرخ زردشتی: (کد.) آتش» هیزم 
افر وخته. 
و (00:۷ع)2201 (.) بشمینه‌ای انتت. تا 
موی‌های آویخته که درویشان پوشند؛ دلق. 
کون الا (ص.) اسله» احمق. نادان. (.) 
بر ری (ص.) لوچ. فت کر وان 


گول؛ اتاع ( 
در یاچه. 

گون: (قد. :1۱)86ع | گونه, گونا] (ا ) رنگ.» 
لون. رخسار» چهره» گونه. نوع» قسم. طرز؛ 
روش؛ شیوه. شکل» هیثت. (پس.) بصورت 
پسوند در ترکیبات ات ی رک
```


## [2026-09-06T02:20:49.731Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/greave",
 "prompt": "Give the full etymology entry for \"greave\" (armor for the leg), verbatim. Also any mention of Arabic jawrab or Portuguese greba."
}
```


### [2026-09-06T02:20:55.720Z] TOOL RESULT

```
# Greave Etymology Entry

Here is the full etymology entry for "greave":

**greave(n.)** — "metal armor to protect the front of the leg below the knee," c. 1300, from Old French *greve* "shin, armor for the leg" (12c.), of unknown origin. [Klein suggests it ultimately is from Egyptian Arabic *gaurab* "stocking, apparel for the leg."]

**Regarding your additional requests:** The provided content contains no mention of Arabic "jawrab" or Portuguese "greba." The only non-English language reference is to Egyptian Arabic *gaurab*, which Klein proposed as a possible ultimate origin for the Old French term.
```


## [2026-09-06T02:21:05.398Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%B1%D8%A8",
 "prompt": "Give the Arabic and Persian sections verbatim: etymology of Arabic جورب (jawrab) and Persian جوراب (jurâb) 'sock, stocking'. Does it say it is borrowed from Persian گورب/گوراب? Also any Middle Persian form."
}
```


## [2026-09-06T02:21:06.237Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%AF",
 "prompt": "List all Persian etymology sections for گرد. In particular the one meaning 'hero, champion, brave' (gord) — give its etymology verbatim (Middle Persian form, Proto-Iranian reconstruction, cognates)."
}
```


### [2026-09-06T02:21:11.139Z] TOOL RESULT

```
# Etymology Summary

**Arabic جورب (jawrab):**
The entry states it is "Possibly from (or cognate with) Persian جوراب (jôrâb, 'sock, stocking')," with earlier Persian forms گورب (gôrab) and گوراب (gôrâb). A speculative theory proposes these derive from Middle Persian "*gōrb/pāy" (literally "grave of foot"), though this may be folk etymology.

**Alternative origin:** The Arabic and Persian forms might alternatively derive from Aramaic גְּרָב/גְּרַב (gəraḇ, gərāḇ), meaning "skin bottle or pouch," with the shift to footwear meaning occurring in an undetermined language.

**Key point:** The text does not definitively confirm borrowing—it uses cautious language like "possibly" and presents the relationship as potentially being cognate rather than direct borrowing from Persian.
```


### [2026-09-06T02:21:12.216Z] TOOL RESULT

```
# Etymology of گرد (gord) - "Hero"

**Middle Persian Form:** (gwlt' /⁠gurd⁠/, "hero")

**Proto-Iranian Reconstruction:** Not explicitly provided in the entry.

**Etymology Statement:** "Inherited from Middle Persian [gwlt' /gurd/, 'hero']. Akin to Central Kurdish گورد (gurd, 'hero, gentleman, brave') and گورج (gurc, 'ready, alert, swift')"

**Cognates Listed:**
- Central Kurdish: gurd ("hero, gentleman, brave") and gurc ("ready, alert, swift")
- Possibly related to کرد/Kurd

The entry notes this sense may be connected to the Kurd ethnonym, though this relationship remains speculative rather than definitively established.
```


## [2026-09-06T02:21:18.128Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gurdus",
 "prompt": "Give the Latin entry for gurdus verbatim: meaning and etymology (any mention of Hispanic/Spanish origin, Quintilian, or PIE root)."
}
```


## [2026-09-06T02:21:20.146Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B2%CF%81%CE%B1%CE%B4%CF%8D%CF%82",
 "prompt": "Give the Ancient Greek entry βραδύς verbatim: meaning and etymology (PIE reconstruction, cognates including Latin bardus, gurdus, Persian, Old Church Slavonic)."
}
```


### [2026-09-06T02:21:23.189Z] TOOL RESULT

```
# Latin Entry: gurdus

**Meaning:** A derogatory noun meaning dolt, numbskull, blockhead, dullard, oaf, or lout.

**Etymology:** Derived from Proto-Italic *gʷordos* ("stubborn, heavy"), possibly from Proto-Indo-European *gʷr̥dos*, a variant of the PIE root meaning "slow, heavy, tired." Quintilian stated: "gurdus, which is colloquially used in the sense of 'stupid,' is derived from Spain." The root's precise PIE origin remains uncertain.
```


### [2026-09-06T02:21:27.345Z] TOOL RESULT

```
# Ancient Greek Entry: βραδύς

**Meaning:**
The adjective βραδύς (brădŭ́s) means "slow," "slow-witted/dull," or in temporal contexts, "late" or "tardy."

**Etymology:**
The word derives from Proto-Indo-European *gʷr̥dus ("slow"), which shares formal and semantic resemblance to PIE *gʷreh₂- ("heavy").

**Cognates:**
The entry lists several related words across Indo-European languages:
- Lithuanian: gurdùs ("slow")
- Latvian: gur̃ds ("tired")
- Latin: gurdus ("dolt, heavy")

**Note on the source:** The webpage does not mention "bardus" or Persian cognates. The Latin cognate provided is "gurdus," not "bardus." Old Church Slavonic cognates are also not included in this Wiktionary entry.
```


## [2026-09-06T02:21:43.702Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%84",
 "prompt": "Give all Persian entries for گول: pronunciations (gul/gol), meanings, and any etymology given (Middle Persian, Proto-Iranian, or borrowing)."
}
```


## [2026-09-06T02:21:43.846Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/bardus",
 "prompt": "Give the Latin entry bardus verbatim: meanings and etymology (borrowed from Greek βραδύς?)."
}
```


### [2026-09-06T02:21:48.909Z] TOOL RESULT

```
# Persian Entry for گول

## Pronunciations
- **Classical Persian**: /ˈɡoːl/
- **Dari (formal)**: [ɡoːl]
- **Iranian Persian**: [ɡ̥uːl̥]
- **Tajik (formal)**: [ɡɵl]

Transliterations: gōl (Classical/Dari), gul (Iranian), gül (Tajik)

## Meanings
1. "deceit; trick"
2. "idiot"

## Etymology
The entry does not provide explicit etymological information for the Persian term. It does not list Middle Persian or Proto-Iranian origins. The document shows that in Urdu, the related term was borrowed from Sanskrit गोल (gola), but no such etymological path is stated for Persian گول itself.
```


### [2026-09-06T02:21:51.184Z] TOOL RESULT

```
# Latin Entry: *bardus*

## Meanings

**Etymology 1 (Adjective):** "stupid, oafish, dull of apprehension" (marked as rare)

**Etymology 2 (Noun):** "a bard (a poet and singer among the Gauls)"

## Etymology

**Etymology 1:** The source states the origin is "Unknown, thought to be a loanword, perhaps from Etruscan." It notes a comparison to *bārō* meaning "dunce, lout."

**Etymology 2:** Derived from Proto-Celtic *\*bardos* ("bard"), ultimately from Proto-Indo-European *\*gʷerH-* ("to approve, praise"), which also yields Latin *grātus*.

## Regarding Greek Origin

The page makes **no mention** of a Greek borrowing (βραδύς or otherwise). Both etymologies presented are distinct from Greek sources.
```


## [2026-09-06T02:21:56.701Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LEW bardus ===\"; grep -n \"^bardus\\|bardus,\" LEW_1910.txt | head; echo \"=== LEW gurdus ===\"; grep -n \"^gurdus\\|gurdus\" LEW_1910.txt | head; echo \"=== LAT bardus ===\"; grep -n \"bardus\" LAT.txt | head; echo \"=== LAT gurdus ===\"; grep -n \"gurdus\" LAT.txt | head"
}
```


### [2026-09-06T02:21:56.788Z] TOOL RESULT

```
=== LEW bardus ===
=== LEW gurdus ===
=== LAT bardus ===
6911:bardus, -1 m.: mot gaulois, cf. P.F.31,13, - gallice appellatur qui
6914:bardus, -a, -u*: lent d'esprit, sot; - stultus a tarditate in¬
6941:haut et qui rappelle bardus., etc., un baro d'origine germanique, auquel
6949:fatuus uel pinguis (= sans doute bardus), CGL IV 600,17.
=== LAT gurdus ===
27146:gurdus, -a, -um: lourd (sena propre et figur£); ^pais, lourdaud,
27150:ne derive pas de gurdus, mais serable d'origine gauloise.
```


## [2026-09-06T02:22:00.286Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6908,6925p' LAT.txt; echo \"=== gurdus ===\"; sed -n '27143,27155p' LAT.txt; echo \"=== leaves ===\"; python3 - <<'EOF'\nd=open('LAT.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['bardus, -a, -u','gurdus, -a, -um']:\n    i=d.find(pat); print(pat,'leaf',d[:i].count('\\f'), '-> p~',d[:i].count('\\f')-18)\nEOF"
}
```


### [2026-09-06T02:22:02.009Z] TOOL RESULT

```
bardla : dans CGL III 433,9, t7tms cpopac, equa bardia.
bardocucullus, -I m.: manteau gaulois (Martial); cf. sans doute
bardaicus... calceus a gente Bardorum , schol.Iuuen.16,13.
bardus, -1 m.: mot gaulois, cf. P.F.31,13, - gallice appellatur qui
uirorum fortium laudes canit, auquel s'apparente barditus de Tac.,
Gerra.3.
bardus, -a, -u*: lent d'esprit, sot; - stultus a tarditate in¬
genii appellatur... trahitur autem a Graeco, quod illi ( 3 ap 8 ug dicunt,
P.F.31,10. Rare; mot populaire, sans doute emprunti, comme 1 'indique
Festus. "Les mots de ce sens sont souvent des eaprunts; cf. ali.
idiot, kretin" (Niedermann).
bargus,-a, -um (Gloss.): <xcpur|C, ingenio carens. II faut y joindre1 X 9
basilicus
sans doute barginna ( barginus, bargena, bargina) souvent glose barbarus,
et les noms propres Bargius, Barginna, etrusques?
bargus, -I m‘. : echafaud. Seulement dans la loi Salique, cf.Thes.
s.n. Sans doute mot germanique.
barla ( barria, braria ): regula, noma, rubrica CGL V 592,43; IV
=== gurdus ===
"fourreur" (VI e s.). Mot tardif, 4 tranger. M.L.3919.
gunt(h)a, -ae f. : sorte de sepulture CIL XI 6 332. Der .guntarius
(transcriptions grecques youvTr|, youv-rtxpoov). Mot ^tranger, tardif.
gurdus, -a, -um: lourd (sena propre et figur£); ^pais, lourdaud,
balourd. Mot vulgaire (Laberius, cf. Geli.16,7,8), espagnol, d'apres
Quint.i,s,57• Bien represente dans les 1 . romanes, M.L.3930, et passe
en gall. gwrdd. Gurdonicus qu'on lit dans Sulpice Severe, Dial.1,37,«
ne derive pas de gurdus, mais serable d'origine gauloise.
Si le ( 3 p- de gr. | 3 p<x 8 ue "lent" repose sur g w r - ce qui n'est pas
evident: , 3 p- peut etre issu de nr- on rapprocherait cet adjectif,
en supposant un ancien *g wu rd~. Pour un mot populaire de ce genre,
une etymologie indo-enropeenne ne s 4 npose du reste pas, V. F.Schoell,
IF 31j 313 et suiv.
=== leaves ===
bardus, -a, -u leaf 136 -> p~ 118
gurdus, -a, -um leaf 526 -> p~ 508
```


## [2026-09-06T02:22:14.919Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 200 -l 200 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg200 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T02:22:16.419Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%AF%D5%B8%D6%80%D5%A4",
 "prompt": "Give the Armenian entry կորդ (kord): meaning and etymology, including any PIE reconstruction and cognates (Greek, Latin, Slavic)."
}
```


### [2026-09-06T02:22:17.556Z] TOOL RESULT

```
total 26752
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 22:22 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   91088 Sep  5 22:21 bqt90.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   26679 Sep  5 22:22 hdr88.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12667 Sep  5 22:22 hdr89.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    3718 Sep  5 22:21 p199_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4112 Sep  5 22:21 p199_pgang.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34164 Sep  5 22:21 p199_pgang_zoom.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   78016 Sep  5 22:20 pg191.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71828 Sep  5 22:17 pg192.png
-rw-rw-r-- 1 sfmqrb sfmqrb  128252 Sep  5 22:21 pg199hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78587 Sep  5 22:19 pg199.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78934 Sep  5 22:22 pg200.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb       0 Sep  5 22:19 tad60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


### [2026-09-06T02:22:23.519Z] TOOL RESULT

```
# Armenian Entry: կորդ (kord)

## Meaning
The word functions as both an adjective and noun in Armenian:
- **Adjective**: "unploughed" or "uncultivated" (describing land/ground); dialectally means "hard"
- **Noun**: unploughed or uncultivated land

## Etymology
The origin remains uncertain. The entry suggests two possible derivations:

**Possible connection**: Related to Old Armenian խորթ (xortʻ)

**Proto-Indo-European hypothesis**: Derived from "*gʰordʰo-" with cognates including:
- Proto-Slavic *gordъ
- Proto-Germanic *gardaz

Under this theory, the original Armenian sense would have referred to an "enclosed pasture-land, pen, etc."

The word descends from Old Armenian կորդ (kord), maintaining the same essential meanings across both linguistic periods.
```


## [2026-09-06T02:22:30.033Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg200.png"
}
```


### [2026-09-06T02:22:30.781Z] TOOL RESULT

```

```


## [2026-09-06T02:22:30.776Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T02:22:45.454Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg200.png')\nprint(im.size)\n# Vtra box approx x 600-940, y 1690-1760 in 1546x2000 scale -> multiply 1.65\nbox=(int(590*1.65),int(1690*1.65),int(950*1.65),int(1760*1.65))\nim.crop(box).resize((int((box[2]-box[0])*2.2),int((box[3]-box[1])*2.2)),Image.LANCZOS).save('vtra.png')\nbox2=(int(360*1.65),int(660*1.65),int(1060*1.65),int(730*1.65))\nim.crop(box2).resize((int((box2[2]-box2[0])*2.0),int((box2[3]-box2[1])*2.0)),Image.LANCZOS).save('jaurb.png')\n\""
}
```


### [2026-09-06T02:22:47.486Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-06T02:22:49.778Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/vtra.png"
}
```


### [2026-09-06T02:22:49.794Z] TOOL RESULT

```

```


## [2026-09-06T02:22:57.467Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg200.png')\nim.crop((590,1690,960,1790)).resize((370*3,100*3),Image.LANCZOS).save('vtra.png')\nim.crop((590,1090,1060,1200)).resize((470*3,110*3),Image.LANCZOS).save('jaurb.png')\nim.crop((560,920,1300,1000)).resize((740*3,80*3),Image.LANCZOS).save('rootbox.png')\n\""
}
```


### [2026-09-06T02:22:59.244Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:23:01.407Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/vtra.png"
}
```


### [2026-09-06T02:23:01.422Z] TOOL RESULT

```

```


## [2026-09-06T02:23:07.869Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/jaurb.png"
}
```


### [2026-09-06T02:23:07.888Z] TOOL RESULT

```

```


## [2026-09-06T02:23:24.474Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT jaurab/greba ===\"; grep -n -i \"jaurab\\|dschaurab\\|greba\\|greve\" LKT.txt | head; echo \"=== PLA ===\"; grep -n \"جورب\\|ǧaurab\\|gaurab\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head; echo \"=== TAD ctx ===\"; sed -n '2560,2575p' TAD.txt; echo \"=== SKT greave armor ===\"; grep -n -i \"greave, armour\\|greave, armor\\|GREAVE\" SKT.txt | head; echo \"=== FSD/WEB greave ===\"; grep -n \"greave\" FSD_vol2.txt WEB_vol1.txt | head"
}
```


### [2026-09-06T02:23:24.607Z] TOOL RESULT

```
=== LKT jaurab/greba ===
=== PLA ===
6653:—2- $arab: "Strumpf" = gaurab q. v. 
=== TAD ctx ===

"تان حب فارسي « انكشتانه » معناه اصبعي مرادفه فم الخباط 

-1 ب أرامي 8 كر 0 معناه جام مكل شيء والمراد به خريطة 
امتكدي يجمم فها رزقه ومن ل المذكور « كناش » فى قالون ان سينا 
وهو دقتر يكتب فيه الانسان ما ينغي أن محنظه 

“كيك تعريب « كاك 6 القارسبى 

كاسات وقاشين - لانيني 3ع معناه غطاء عقب الرجل . وجورب 
ج جوارب فارسي معناه قبر الر جل مرادفه لفافة الرجل 0 

كليرس وتالى 5ه معناه إرث ونصيب واللمراد به كبئة اليعة لان 


لله نصيمهم 
=== SKT greave armor ===
7962:fe¥Mi<  I  \  WftToa.  sediment  ofmelted jSg^^  0.  Swcil.  rre/amr,  dirt ; ^^^K,  'lieht-tliii,  rc/it$e  ol  tal- ^^^^^pjulciug  ;  Swed.  dial,  ^trvar, Dliu  <f  Low  li.  ^rven,  greaves,  G.
22800:grave,    graze,   greaves,    gnret.  fW/.
23588:rcl.  bice,  bijon.  blond,  blouse,  brattice, te«  (il,  biet'ze  (2),  broil  (2).  buffer  (,0, ffer  (3).  buffet  (I),  buffet  (j),  huffoon. ruattft  (burgoiict),  busk  (i),  buttress, t>ba|^  {»),  culibcr  ^calibre),  calipers, lirer,  champagne,  chcval-dc-frise,  chi- Bcry,  chiffonier,  cockaJe.  curlew,  davit, le,  dtMase,  drab  (a),  drape,  dupe,  ease, ibiiitlc  (O,  embattle  (a),  cmblaion,  era- S*  { I  \  emboM  (2),  embrasure,  embroider, ibroil,  entice,  entrench,  fribble,  frieze  (i), ppery,  furbelow,  galley,  galliot,  gallon, rland,  gasccmade,  gavotte,  gibbet,  giblets, (3),  gingham,  gobelin,  gormandise, lUTnand,  graze  (l)?,  greaves  (,a),  grouse, illotine,  guxxle,  harass,  haricot  (i),  hari- (a\  harlequin,  harlot,  harridan,  hnunt, ik  ;a],  jacKetf  jostle,  lawn  (^a),  lees, tch,  loo,  lozenge,  magnolia,  maraud, utia,  martinet,  martingale,  martlet,  mich, Trtise,  musit.  Nicotian,  pamphlet?,  pa- Kv  pedigree?,  pillory,  pinch,  pinchbeck vritma/  name),  pirouette,  piss,  pittance, plin,    ricochet,    roan,    sautcmc,    savoy,
=== FSD/WEB greave ===
WEB_vol1.txt:84102:graves, n.pl. same as greaves (cracklings). Graves’ dis-ease’, [after Robert Graves (1797- 1853), Ir. physician.] exophthalmic goiter. grave’stOne, 7, a tombstone. h grave/yard, n. a yard or enclosure for the in- terment of the dead; a cemetery. grav/ic, a. relating to gravitation. [Rare.] grav/id, a. [L. gravidus, pregnant, from gravis, heavy.] pregnant; with child. grav/i-da-ted, a. made pregnant; big. [Obs.] grav-i-da’tion, n. pregnancy. [Obs.] gra-vid/i-ty, n. pregnancy. 3 grav'igrāde, a. [L. gravis, heavy, and gradi, to walk.] heavy-footed; of slow movement. grav/i-grade, n. an animal that walks heavily, as an elephant. gra-vim/e-tér, n. [L. gravis, heavy, and mel- rum, a measure.] an instrument for determin- ane Ute specific gravity of bodies, solid or iquid. grav-i-met’ric, a. relating to weight meas- urement: distinguished from volumetric. gray-imet’ric-Al-ly, adv. in a gravimetric manner; by means of gravimetry. gra-vim/e-try, n. [from L. gravis, heavy; and analra] the measurement of weight or den- Siy: stāv'ing, n. 1, the act of cleaning a ship's om. finn or cutting, as in sculp- graving dock; a dock for holding a ship for Bes: or cleaning the bottom, etc.; a dry Srav/ing piéce, in shipbuilding, a new piece of wood inserted to repair damages. Grav/i-tate, v.i; gravitated, pt., pp.; gravita- g, ppr. (L. gravitas (-atis), heaviness, from gravis, heavy.] with the feces pone to move in accordance 5 of gravity. aes ans oF pall: to tend to settle at a bot- , a liquid. demedine Roe ene to move (toward rav-itā’ti . A Ve n. 1. the fact, act, or effect of . in physics, the fo b i arti , rce by which every Se ee matter tends to approach every of gravitation iet the universe. Newton's law matter aon is that every body or portion of its quantity of and is attracted directly as
WEB_vol1.txt:84255:gréaves, n.pl.[ME. greves, grayvez: greaves, pl. of greve, the shia | Zi OFT. greves, legs from the ankle to the knee. mile
FSD_vol2.txt:36318:grav'er-yt,  n.  Engraving  or  carving, graves’,  I   grSvz;  2   Sravg,  n.  pi.  The  refuse  or  sediment  of lard  or  tallow;  greaves:  made  Into  cakes  as  food  for  dogs, bait  for  ilsh.  etc.  [Form  of  «kbavf.s2.1 graves^,  tt.  pi.  [F.i  1.  I.ana  composed  of  light,  gravelly  soil. 2.  (0.1  Wine  produced  from  grapes  grown  on  such  soil.  See
FSD_vol2.txt:36377:bles,  etc.  [Formerly  greavy,  orlg.  an  a.,  <   greaves*.)
FSD_vol2.txt:36554:Great  Yar'mautfa,  1   yar'maflti;  3   yar'mutb.  A   seaport, fishing  station,  and  borough  In  Norlolh,  England, greave,  1   grlv ;   2   8r5v,  s«.  Same  as  gbavbL  [   <   geeaves^.I greavet,  «.  A   bush;  bough:  grove, greaves,  Same  us  grieve,  n.  Igreaves.
FSD_vol2.txt:36555:greaved,  1   gri  vd ;   2   grgvd,  -pa.  Armored  with  or  protected  by greave.s*,  1   grrvz;  3   iravs,  n.  pi.  Armor  to  protect  the lege  from  knee  to  ankle:  used  also  in  the  singular.  _   See illua.  under  akmor.  [   <;  OF.  gretes,  pi.  of  greiie,  shin.] greaves^,  n.  pi.  Pieces  of  boiled  tallow»sorap;  cracklings. See  GB.WES.  [Of  LO.  or  Scand.  orlg.;  ep.  LG.  greve,  the refu.se  of  lard  or  tallow,  OSw.  grefwar,  dirt.]
FSD_vol2.txt:41305:Har'greaves,  i   har'gtivz;  2   har'grgvg.  James  (   •-'•/-177S).
FSD_vol2.txt:72059:SaWdJri  lYsrvtnXo  ffirtfter  T   i   I   tlnguished  by  Intellectual  power.- l..greaved,  a.  Charac-  LaUive,  1   la riv;  2 lariv,  Jean  Mauduitde  (8/6l747-V!»i837).
FSD_vol2.txt:72060:firi  LI  tit  -“i’-nir  «   rW  tcrlzed  by  platcs  resembling  greavet  which  protect  the  La"ri"vcy',  1   laTEvG';  2   lii'Ti've',  Flerre  de  (16S0?-1612?).
```


## [2026-09-06T02:23:33.969Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gaurab\\|ǧaurab\\|jaurab\\|gaurāb\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-06T02:23:34.029Z] TOOL RESULT

```
6653:—2- $arab: "Strumpf" = gaurab q. v.
```


## [2026-09-06T02:23:36.881Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Strumpf\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20; echo \"=== ctx 6645-6660 ===\"; sed -n '6640,6660p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-06T02:23:36.946Z] TOOL RESULT

```
6653:—2- $arab: "Strumpf" = gaurab q. v. 
7779:L,» - $auräb: "Schuh, Strumpf" aus dem pers. _!,, Zürab, eventuell 
=== ctx 6645-6660 ===

In - Zuddäd: "Hügel" aus dem pers. “Ss kuh a <—Tmp.913 kof °. 
-so- Badar: Pl. v. _,» gudar q. v. 
„Lo - ZadIsäbür = Zundisäbür s. Zundisäbür ©. 
»L.s- $aräbäd: ein Dorf in der Nähe v. Marw in Khurasan 7, 
_ _ = ——ı _ - - 
S>li >- Harabädi: Nisba v. »V1,> garabäd s. Karabad. 
oT =... -.. o. 
BIP Zu Saräbäd = Saräbäd s. $aräbä . 
»Le- Yarädig: Pl. v. Syp Bardaq s. Sardag. 
Le - Zarädig: Pl. v. 3y>%fardag s. Bardaq. 
olr- baräfis = Jaranfas q. v. 
aeLo - $arähiyya: "Truppe" aus dem pers. 22 gu üh e— mp...» gröh. 
—2- $arab: "Strumpf" = gaurab q. v. 


Ob>L>. $arbädgän: eine Stadt im Iran T mp. wswWo@> girdapätakän 9 
gird + pätan air. *pati "schützen" 10 > pers. golpäygän. 


1. LD.s. v.
```


## [2026-09-06T02:23:40.400Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7770,7795p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-06T02:23:40.463Z] TOOL RESULT

```
sl,,»- Züdaba = Züdab s. Züdab. 
3»? - Züdar: "wildes Büffelkalb" pers. ı mp .)>p gäwdar 2, 


5? - Büdarz: "Eigenname" aus dem pers. inf güdarz 3, 
„9 - $ür: eine Stadt in Provinz Fars, aus dem pers. „Sgür. 


L,» - $auräb: "Schuh, Strumpf" aus dem pers. _!,, Zürab, eventuell 
ur File 


x -_ 


golpä "Stoff für den Fuß" 4 syr. ou. 


a1,» - faurägiyya: "eine Geldeinheit", eigentlich Nisba v. Gaurgan 
(eine Stadt in Fars)- 


Ob, - Zaurgan: ein Ort in Fars. s. $aurägiyya.
```


## [2026-09-06T02:24:01.956Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK bradus ===\"; grep -n \"βραδύς\\|bradús\\|bradus\" POK_full.txt | head; echo \"=== POK gurdus/gurdos ===\"; grep -n \"gurdus\\|gurdos\\|gurdùs\\|gùrdus\" POK_full.txt | head; echo \"=== POK lemma g\\\"er heavy ===\"; grep -n \"lemma: gʷer-2\\|lemma: gʷerǝ-2\\|Meaning: heavy\" POK_full.txt | head"
}
```


### [2026-09-06T02:24:02.039Z] TOOL RESULT

```
=== POK bradus ===
=== POK gurdus/gurdos ===
34086:about Latin gurduss. WH. I 627. 
=== POK lemma g"er heavy ===
33831:Meaning: heavy sound, thunder, grumble 
39519:Meaning: heavy 
83984:Meaning: heavy
```


## [2026-09-06T02:24:03.736Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD gwere heavy ===\"; grep -n \"gWer\\|gwera-\\|BARYON\\|GRIEVE\" AHD_watkins1985.txt | head -8"
}
```


### [2026-09-06T02:24:03.787Z] TOOL RESULT

```
=== AHD gwere heavy ===
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1219:AGIO al-1 AGITATE ag- AGLET ak- AGMINATE ag- AGNAIL angh- AGNATE gene- AGNI egni- _ AGNOMEN no-men- AGNOSIA gnd- AGO ghé- -AGOGUE ag- AGONY ag- AGORA! ger-1 AGORAPHOBIA ger-! AGRAFFE ger-2 AGRAPHA gerbh- AGRAPHIA gerbh- AGRARIAN agro- AGREE gWere-3 AGRESTAL agro- AGRIA agro- AGRICULTURE agfo- AGRIOECOLOGY agro- AGRIOLOGY agro- AGROSTOLOGY agro- AHIMSA ghei-i, ne AHRIMAN men-1
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
```


## [2026-09-06T02:24:12.294Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '34060,34100p' POK_full.txt; echo \"=== grep brad ===\"; grep -n \"bradýs\\|bradýs\\|brad\\b\\|βραδ\" POK_full.txt | head"
}
```


### [2026-09-06T02:24:12.407Z] TOOL RESULT

```
fermentation ', Dutch gruit^ malt, yeast, residuum ', Norwegian grutu. " residuum '; Old 
English grotv\. " coarse meal, flour' (Germanic *gruta-)\ 

with formants -to- or -so-Middle Low German grus, gros' crumbled stones, gravel '; 

Balto Slavic *grudid^ stamp ' in Lithuanian grudziu or grudau, grust/" stomp (barley for 
the pearl barley preparation); bump; touch '; ablaut, graudus besides ' brittle ' also " 
stirring, wistful ', Old Prussian engraudTsnan f\Vk. Sg. ' pity ', grudas'corr\, grain'; Latvian 
gruzu, grudu, ^ms/'bump, poke, stomp', grudenesi. PI. " pearl barley '; ablaut, graudsm. 
"corn, grain', grauzu, graudu, grausV rumble, thunder ', graudiensrr\. " lightning strike ', 
grausliP\. ' rubble, debris '; 

Church Slavic gruda'c\od of earth', collective grud//ear\6 (deriving from an already 
collective *ghrdud-d!"a) gruzdije; Serbo-Croatian Brno's 'clump' etc. (6^ proves initial long 
diphthong du)\ with -/77e/7.- Serbo-Croatian grumen 'c\od', russ. grumds.; here also with 
transference on the mental area russ.-Church Slavic st-grustiti sa^ grieve ', russ. grustbi. 
" distress, sorrow ', sloven, grustm. " disgust, repulsion, loathing ' (^from short diphthong, 
Indo Germanic su, the old sensory meaning still in grusc rr\. " grit, mountain rubble '), with 
weak grade i/.' Serbo-Croatian grsti. m. ' disgust, repulsion, loathing ' (proto 
Slavic *grbstb), g'rstiti-se " be disgusted ', as well as *grbdb in Old Church Slavic grbdh 
"horrendus, terribilis', Serbo-Croatian grd^ hideous, unsavory, distasteful, nasty', from 
which also Old Church Slavic grbdb "stout, proud' (originally " feeling disgust, fastidiously 
'), russ. gordyjds., Serbo-Croatian grd^ sioui, proud, terrible', etc.; 

Maybe nasalized alb. (^krude) krunde, crumps "debris ' 

about Latin gurduss. WH. I 627. 

extension ghreug(h?)-: 

Lithuanian grauzas^ gravel ', gruzotas^ uneven, bumpy ' (is Latvian gruzis, PI. gruzi^ 
rubble, horror, dismay ' ndd. loanword?); 

poln. gruz^ rubble, mortar', PI. " debris, ruins ', kir. Ami" debris ', PI. " rubble ' (barely 
from Middle High German grus^ horror, dismay ' because of:) poln. p'mz/a "clump'. Upper 
Serbian hruzia " clump, clod '. 

extension ghreu-b^-: 



=== grep brad ===
13102:breath). Old IcelandiCit'/'adr'stormy, hot tempered, hasty', brad^ tarred wood, creosoted ', 
13112:"calf, late Latin borrows brado^ham\ Old English braedem.. Old Icelandic brad^x3>N meat'. 
13258:wall, scaffold, trestle', Czech zabrad/o ^handraW, parapet' ); russ. borona' harrow', and with 
60207:cymr. brad 6s. ( *mr9-to-) to Old Irish *marnaid' betrays ', subjunctive -mera;
```


## [2026-09-06T02:24:24.452Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY latin index gurd/gul ===\"; grep -n -i \"GURD\\|GORD\\|GUL\\b\\|GOL\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== ARY pages گرد ===\"; grep -n \"گرد (\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY گول ===\"; grep -n \"گول\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T02:24:24.533Z] TOOL RESULT

```
=== ARY latin index gurd/gul ===
145:05S p ST SMakya Gays 3 althiy y a Gul
188:OLS (Yo oe Las 1 O44 Gordo aye sb; SCIENCE (giles) jth tay Se”
281:NBL; 9 lo 2 yey came Gael 52 23k I uty Sle aslo age abst y wa Gul
288:“list ga 6529S 4 9a Gul Sdagge NS eT 1 gen sr gegen gga yy
519:Ab shoal etbtth til 92 S pte 9 SUR L Wj eat 37 22 end GOL,
520:aceolndys Sighyysl sea GUL) CALE yo edie dp cary g 2p) ULI SU 5a JT jl
584:eel PLS OSU gh 9 em a aly etn gy outed 45 gol 3}
781:eeK eat cael > ange Ob5 AS obo po "op SL gS" otly GOL! Tages
960:baile gy My Obst cobeal ghac 5 yo Fat cul curd oylbl Gul oa Sb pa ory
1021:ty ad Gol Gale p99 9 00d gE py 4 ed Ends gtbe 32 paint Ebaby
1080:Shall pl stl HIS Satay ltd hls Gadd Oh I ta Seal Slated gol Sts
1127:he Bal Wks 4 BAS cell 4 AS Als! GUL; Obslole y SLIKEI algo 5
1141:52590 38) 537 Gilg) GOL; a sath 9 ging Shar ob ple Jy Curl 03 Srl wore y
1314:INS AS gw Bin § 309,53 phyla eal gest 4 Sp 1 tag Sead gol ntl
1815:we Slip (ailegy GUL; 9 SY 2 5s cel om
2844:i Sy ahs Se te 9 (SL 2 eu alaul 9 He GOL) ST 0 OT OSU L slabs» “vale!
3418:wand Lj CA olla WEY sph yt g te Glk5 S132 0519 gol gamed
3446:: B20 TIM O35 tp BA y GUST 59 5s gol pO
3621:a gph 602 S Gla Fogg) GUL; 22 05s cal om
3710:gen GUL; 42 OT Glan Jy e| CONOMATOPOETIC) “pls yal gol S aw Sy
=== ARY pages گرد ===
=== ARY گول ===
8099:چم این واژه در زبان آلمانی: گول زدن؛ گمراه کردن. :
```


## [2026-09-06T02:24:26.565Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nimport re\nd=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\n# find pdf tags\nm=re.search(r'\\[pdf page (\\d+)\\]',pages[100]); print(pages[100][:120])\n# search for gurdus / bradys\nfor pat in ['gurdus','bardus','βραδύς','bradys','gṛdus']:\n    idx=[i for i,p in enumerate(pages) if pat in p]\n    print(pat, idx[:10])\nEOF"
}
```


### [2026-09-06T02:24:28.298Z] TOOL RESULT

```
leaves 895
92                                             aldh-     — albho-
aldh- „Trog; Welle".
     Altn. ahla f. „Welle, Wellen
gurdus [649]
bardus []
βραδύς []
bradys []
gṛdus []
```


## [2026-09-06T02:24:34.415Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nd=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\np=pages[649]\nprint(p[:60])\ni=p.find('gurdus')\nprint(p[max(0,i-2500):i+900])\nEOF"
}
```


### [2026-09-06T02:24:36.125Z] TOOL RESULT

```
                                                                                                           ;




                                          gurdo-s?   — gh rd                                         641


  Mir. gall „Auslander“,          cymr. gal       ds.,   gall.   Gallus,   Gallia (Fick II 4 108
zw.)     bleiben   jedenfalls fern.           Yon den Yersuchen, den            idg. Ursinn des
Wortes zu erraten (s. Yf. LEWb. 2 370f., Giintert IF. 32, 394), bleibt er-
wagenswert die Ankniipfung an die Praep. *eghs „ex“ als *(e)yhos-sti-s
„auswarts befindlich" (Fay Min. 1907, 38 f., AlPh. 34, 37); die Guttural-
frage ware glatt, wenn slav. gostb aus dem Germ, stammte iden Palatal
von eghs nach Fay der in *ghos-stis ausgeschalteten Wirkung des anl. e-
zuzuschreiben, ist undiskutierbar, solange wir iiber die Entw. von Pala-
talen aus Yelaren im dunkeln sind).


gurdo-S?      „steif,   unbeholfen oder anmaBend                   dastehend" {g^rdu-s ?        s.   u.).

  Lat. gurdas  „dumm, tolpelhaft, hebes, obtusus" (roman. ,,dick, fett, starr,
steif, geschwollen, erfroren", s. Scholl IF. 31, 313 f., wo auch gegen die
Annahme spanischer Herkunft), aksl. grzdv, russ. gdrdyj .,stolz, hochmiitig"
                                                  4
v. Sabler KZ. 31, 278, Stokes BB. 18, 89, Fick I    41 1; nicht iiberzeugend
geht Berneker 370 wegen serb. grd (auBer ,,stolz; sehrecklich", diese beiden
Bed. nur alt) auch „ha81ich“, Komp. grdt „sehlechter, schlimmer^, poln.
gardy „wahlerisch, heikel im Essen" u. dgl. (die ein versch. ursl. *gn(h
sind, s. u. ghreu   ghreud- „reiben‘ ) fiir „stolz“ von einer Gdbed. „sich wo-
vor ekelnd" aus, statt von der Yorstellung des ,steifabweisenden ‘. ;


   Gr. /Spado? „langsam, trage" (zu gurdus von Walter KZ. 11, 437, Froehde
BB. 1, 331; 3, 1 2 S f 14, 105, Bersu Gutt. 152 gestellt) konnte unter einer
                         .   ;



Gdbed. „wie ein Stock dastehend" angeschlossen werden, wobei lat. si.
gurdus fiir *g'i{„)rdus stiinde; doch erwagt Bechtel KZ. 46, 162, Lexil. 38
fiir /Spado? eine Gdf. ^padd?, zu /uegdei      y.cokvsi,  •    /uegdsToa cnegt]-            ‘




’deiaa Hes., djusgd <x> „beraube", so daB es „geistig oder in der Bewegungs-
freiheit geschadigt, gehemmt" ware.
    Ai. jadhu- angeblich     starr, kalt, stumpfsinnig" (Froehde aaO.) ist in
                                 ,,



der Bed. unsicher und stimmt im Wzauslaut nicht, vgl. Bartholomae IF. 3,
198f.,    Solmsen Stud. 30;           iiber weiteres,         was fernzuhalten ist,   s.   Berneker
aaO., iiber lat. tardus Yf.           LEWb. 2 S3f.

ghfd „Herz“, nur arisch               (vgl.   *kere
```


## [2026-09-06T02:24:51.186Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor L in (657,658):\n    print('=== leaf',L,'===')\n    print(pages[L][:400])\nEOF\necho \"=== POK 39519 ctx ===\"; sed -n '39505,39560p' POK_full.txt"
}
```


### [2026-09-06T02:24:52.961Z] TOOL RESULT

```
=== leaf 657 ===
„Begierde, Heftigkeit, Grausamkeit" u. dgl. (Zup. G. 176 m. Lit.. Fick III 4
144 f., Falk-Torp u grue, grunde; anders, aber nicht einleuchtend Wiede-
                                   .



mann BB. 27, 239); die von v. d. Osten-Saeken IF. 28, 419 zunachst mit
den germ. Gruppen verglichenen Worte wie abg. gndz „horrendus, terri-
bilis" (ursl. % grz<h, versch. von *gtr(h „stolz“, s. *gurdos), skr. 
=== leaf 658 ===
                                                ,




650                                                           greut-   — greus-

schwaehster Stufe n                       (s.       auBer Zup. G. 176 bes. v. d. Osten-Sacken IF. 28,
419) skr. grst f. m. ,,Ekel“ <ursl. *gnstb), grstitise slov. grstitise „sich ekeln“,   ,


so win das von ursl. * (forth „stolz“ (s. *gurdos) zu trennende *grzih i
=== POK 39519 ctx ===
Gr. ppayxia, papayxia ' gill offish' : alb. Geg {* g"er- g"ha) verza^ (*throat), gill offish' : 
Latvian barda^<^\\\ offish' : Latvian : M/'o'a "beard' [fa]; barzda {'6\a\.) "beard'. 
Root / lemma: g^er-l, g^ere-: " to devour; throat ' > Root/ lemma: b'^arH^a: " beard' 

5. With pure velar: gr. y£py£pO(; ppoyxoq Hes., yapyapscbv " uvula in mouth', yapyapi^w 
"gurgle' (: Armenian kerker/m 'become hoarse'?) perhaps through labialization after forms 
with yup- (yopyupn "subterraneous, underground jail, water pipe '), yet is previously ger- 
besides g"er- because of ge/- besides g^e/- is safe. 

References: WP. I 682 ff., WH. I 627 f., Trautmann 89 f., 98, Specht KZ. 59, 1 10, 1 . 
Page(s): 474-476 

Root / lemma: g''er-2, g^erQ-, g^erQu-, g^en- 

Meaning: heavy 

Material: Old Indie gurii-h' heavy, important, venerable ' (compounds ganyan. Sup. 

garistha-h), agru-' available, unoccupied; unmarried', gru-mustf-h' heavy handful ', 



garima^ heaviness' {*g"'er9-); Avestan gouru- (in compound) " lieavy '; npers. giran^ lieavy 
' {*grana-\ reshuffling after *frana-^i\}\\y, 

gr. papu(; " heavy ', papuvw "beschwere", papo^ n. " heaviness'; Note: common lllyrian 
g"'-> b-. 

Maybe alb. barre^ burden, pregnancy '. 

Latin gravis ' heavy, weighty ' ( *g"ra-u-is)\ 

Middle Irish bair^ heavy ' (?), baire^ distress (?)', bruth^ weight, mass' {*g"rutu-), cymr. 
it'/yn/ 'strong, strength ' {*bruwo). Middle Irish br6^bu\k, mass'; Note: common lllyrian g"- > 
b-. 

Gothic kaurJosUoxu. PI. f. ' heavy ', kaurjan' grouch'; 

Lithuanian gurstu, gurti^ lie down (from the winds) ', Latvian gurstu, gurt^ tire; lie down 
(from the winds) ', gufds^ fatigued, faint, languid' (compare also papuq and gravis\v\ the 
meaning ' weighted, pressed down, faint, languid'), whereof with further shifting from ' 
faint, languid, weighted ' to "tame, domesticated, mild' (compare Old High German 75/775/"' 
sorrowful ' : gr. n[J£poc; "tame, domesticated') perhaps: 

Gothic qafrrus^ of persons, gentle, kind ', qafrrei^ gentleness, softness, kindness ', Old 
Norse kyrr, kvirr^sWW, peaceful'. Middle High German kurre. Modern High German kirre^ 
tame, domesticated, trustful ' {*g'^er-ar6s or -eras, -uros); 

Latvian gruts " heavy ' = Latin brutus (Oscan-Umbrian loanword) " heavy, clumsy, 
insensible, unreasonable '; 

Tocharian A kra-marts^ heavy ' (?); Van Windekens Lexique 44. 

Here further as n- derivatives from g"era-av\6 g"erau-: Go\h\c {asilu-) qafrnus^ 
(Esels)muhle ' {*g"er9nu-). Old Norse kverni. {*g"erna) " millstone, quern ', Old English 
cweorn6s.. Old High German quirn, quirna^s.;
```


## [2026-09-06T02:25:13.951Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; wc -l data/verification/sources/refs/ARB_mo3rb.txt; python3 - <<'EOF'\nd=open('data/verification/sources/refs/ARB_mo3rb.txt',encoding='utf-8',errors='replace').read()\nn=len(d)\ni=d.find('واطورب لفاتة الرجل')\nj=d.find('و« جورب »')\nprint('total chars',n,'entry pos',i, 'frac', round(i/n,3), 'muqaddima pos',j,'frac',round(j/n,3))\nEOF"
}
```


### [2026-09-06T02:25:15.685Z] TOOL RESULT

```
37284 data/verification/sources/refs/ARB_mo3rb.txt
total chars 776377 entry pos 222417 frac 0.286 muqaddima pos 62297 frac 0.08
```


## [2026-09-06T02:25:21.977Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%AF%D9%88%D9%84/",
 "prompt": "Quote the فرهنگ معین (Mo'in) section for گول verbatim, including any bracketed origin tag such as [په.] or [ع.]. Also quote لغت‌نامه دهخدا if present."
}
```


## [2026-09-06T02:25:23.951Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AC%D9%88%D8%B1%D8%A7%D8%A8/",
 "prompt": "Quote the فرهنگ معین (Mo'in) section for جوراب verbatim including bracketed origin tags, and any mention of گوراب or گورب. Also quote دهخدا if it discusses the origin."
}
```


### [2026-09-06T02:25:27.955Z] TOOL RESULT

```
# Excerpts from Abadis Dictionary for گول

## From Farhang-e Mo'in (Moein Dictionary):

"۱ - (ص . )ابله ، نادان . ۲ - (اِ. ) مکر، فریب . ۳ - دلق .  
(اِ. )۱ - حوض . استخر، تالاب . ۲ - دریاچه ."

## From Loghat-nameh-ye Dehkhoda (Dehkhoda Dictionary):

The entry provides extensive etymological information, noting that گول means "a fool" or "naive person" (ابله، نادان، احمق), and alternatively refers to water-related features like pools and ponds (حوض، استخر). The dictionary includes historical literary references and notes various related terms across Persian dialects, with discussions of possible Turkish and Sanskrit origins.
```


### [2026-09-06T02:25:30.971Z] TOOL RESULT

```
# فرهنگ معین Definition

According to Farhang-e Mo'in:

> "(اِ. ) پوششی که آن را از نخ های پنبه ای یا پشمی و یا ابریشمی بافند و پا را با آن پوشانند"

This describes a garment woven from cotton, wool, or silk threads used to cover the foot.

# Dehkhoda Dictionary Entry

The Dehkhoda section notes:

> "پای تابه ای که از نخ های پنبه ای یا پشمی یا ابریشمی بافند و پاها را بدان پوشانند"

It characterizes the item as a foot covering made from natural fibers.

Neither source explicitly discusses etymology or alternative forms like گوراب/گورب in their main definitions.
```


## [2026-09-06T02:25:41.637Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://www.etymonline.com/word/greave\" \\\n \"https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%B1%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%84\" \\\n \"https://en.wiktionary.org/wiki/gurdus\" \\\n \"https://en.wiktionary.org/wiki/%CE%B2%CF%81%CE%B1%CE%B4%CF%8D%CF%82\" \\\n \"https://en.wiktionary.org/wiki/bardus\" \\\n \"https://en.wiktionary.org/wiki/%D5%AF%D5%B8%D6%80%D5%A4\" \\\n \"https://abadis.ir/fatofa/%DA%AF%D9%88%D9%84/\" \\\n \"https://abadis.ir/fatofa/%D8%AC%D9%88%D8%B1%D8%A7%D8%A8/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 200 (book p.170): roots Gurb/Kurb (stocking->greave) and Gurdos I/II (gord, gul, gurdus, bradus, bardus, kord)\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T02:25:49.392Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/97aeee577e5e5f16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/834629c13a5a5ebb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8eadaeb66a150fd7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fabe74ec2c234180.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/76b3de0dc61f8600.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/28a0054ba16bc178.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/27db41488eb7f899.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb1b70e90a688670.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7760e00632433f80.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f54a8ea0c1f07f67.txt
```


## [2026-09-06T02:26:04.174Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg200.png data/verification/sources/refs/ocr/BOOK/200.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3\ncd data/verification/sources/refs; echo \"=== LKT Strumpf ===\"; grep -n -i \"strumpf\" LKT.txt | head; echo \"=== DEV/PHN ===\"; grep -n -i \"jaurab\\|djaurab\\|greve\\|greba\" DEV.txt PHN.txt LAM.txt DOZ.txt | head; echo \"=== RCH گورب ===\"; grep -n \"gurb\\|jaurab\" RCH.txt | head"
}
```


### [2026-09-06T02:26:06.008Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
=== LKT Strumpf ===
1159:'Verkrüppelt,  einarmig'  [vom  Stamme sol,  col  'link,  ungeschickt,  krüppelhaft' Vämbery  TktEtWb  S.  153,  Nr.  165]; hieraus  rum.  ciolac  'dass.'  und  mit eigenartigem  Bedeutungswandel  russ. ciilok,  bulg.  culka  'Strumpf.  [Gorja- jew  417.
1163:'Strumpf;  hieraus  rum.  ciorap  'dass.' und  Ableitungen  cioräpel,  cioräpior; bulg.  corap,  serb.  carapa  'Strumpf.
=== DEV/PHN ===
=== RCH گورب ===
51549:ightly.  ^Rejoicing  at  (an  enemy’s)  distress.  ^   shutur-gurbah  (Camel-cat),  i.  e.  any  two  things
72025:P gurbur  gurbuz  also  Jj^gz/rfiy),  A   deceiver,  se-
72028:^ gurbaguy  Name  of  a   fragrant  shrub, p   gurbahy  A   cat.  Wild  thyme.  Name  of  an  odoriferous tree  called  bed^mushk.  gurba^i  dbiy  An
72029:otter.  gurbah  az  baghal  afgandarty  Throw-
72031:J   gurbah  dar  ambdn  ddshiany  To  practise  deceit
72033:ricious. gurba^i  daihtly  A   kind  of  panther  or  wild
72035:p   «Xj  gurhah*bedy  A   species  of  the  willow, p   ^   f   gurbah^chashniy  Gray-eyed  (like  a   cat), p   4]  J   gurbah-dalaky  A   ferret,  a   marten,  a   weasel, p   ^,Li  ^ gurbah^tdn  (or  gtirbab^gin)y  Like  a   cat,
```


## [2026-09-06T02:26:11.134Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1155,1170p' LKT.txt; echo \"=== leaf ===\"; python3 - <<'EOF'\nd=open('LKT.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\npos=sum(len(l)+1 for l in lines[:1160])\nprint('leaf',d[:pos].count('\\f'),'-> printed p',d[:pos].count('\\f')-26)\nEOF"
}
```


### [2026-09-06T02:26:12.905Z] TOOL RESULT

```
'Tuch';  hieraus  bulg.  coha  'Tuch',  serb. öoha  'dass.,  Tuchkleid',  russ.  (alt)  cuga 'enger  langer  Rock',  klruss.  cuha,  öiihana 'Mantel,  Oberkleid  aus  Wolle'.  —  Die Zusammensetzung  tk.  Jo^arf«r 'Geschäfts- träger, Agent'  ergibt  rum.  ciohodar 'Diener'.    [Bern  SlEtWb  159.
436.  Tk.  cojan:
'Roheisen'  [Kölekian  Kämüs  482],  kas.- tat.  cujyn;  hieraus  bulg.  cugun,  russ. cugun,  klruss.  cugun,  cagun,  cawun, caun,  poln.  czugtin  'Gußeisen'.  [Gor- jajew  416.    Bern  SlEtWb  161.
437.  Tk.  colak:
'Verkrüppelt,  einarmig'  [vom  Stamme sol,  col  'link,  ungeschickt,  krüppelhaft' Vämbery  TktEtWb  S.  153,  Nr.  165]; hieraus  rum.  ciolac  'dass.'  und  mit eigenartigem  Bedeutungswandel  russ. ciilok,  bulg.  culka  'Strumpf.  [Gorja- jew  417.
438.  Tk.  comak:
'Keule,  Knüppel'  [Kelekian  Kämüs  481, vom  Stamme  jMm,  Jmwi,  öotn  'vereinigen, fest,  dicht,  Körper  von  runder  geschlos- senei-  Form'  Vämbery  TktEtWb  S.  137, Nr.  14711];  hieraus  rum.  ciomag  'dass.' und  Ableitungen  ciomaga^,  ciomägealä. Nach  seinem  Werkzeuge  in  der  Hand ist  benannt  russ.  cumak  'Fuhrmann (besonders  in  Südrußland),  Knecht'.
439.  Tk.  corab:
'Strumpf;  hieraus  rum.  ciorap  'dass.' und  Ableitungen  cioräpel,  cioräpior; bulg.  corap,  serb.  carapa  'Strumpf.
440.  Tk.  corba:
'Suppe';  hieraus  rum.  ciorba  'Suppe', ciorbalic  'Suppenschüssel',  ciorbulifä; bulg.  serb.  corba  'Suppe',  poln.  czorba 'Suppe,  aufgeweichtes  Brof ,  russ.  (dial.) scorba  'Fischsuppe'.  —  Zu  Zeiten  der Janitscharen  [s.  hier  Nr.  954]  hießen  die Hauptleute  od.  Regimentskommandeure tk.  öorbagy,  eigentlich  'Koch',  hieraus rum.  ciorbagiü  'Herr'.  [Bern  SlEtWb 159/160.
441.  Tk.  cörek:
'Kuchen';  hieraus  rum.  ciurcchi  'eine Art  Kuchen'.
442.  Tk.  cotra:
[Nach  Pu§cariu  Et.  Wb.  der  rum.  Spr.382 aus  it.  ciotola  'Trinkgefäß'  <^  lat.*  cytola] 'Tragbares  Holzgefäß  für  Wein  oder dergl.'  [K6lekian  Kämüs  477  mit  Ab- bildung]; hieraus  rum.  citurä,  ciuturä 'Eimer,  hölzerne  Feldflasche;  Mundstück eines  Pfeifenrohres';  bulg.  cotra,  ötitura 'Flasche,  Holzflasche',  serb.  cutura  'dass.'. [Bern  SlEtWb  164.
443.  Tk.  culdar:
=== leaf ===
leaf 62 -> printed p 36
```


## [2026-09-06T02:26:21.982Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/greba",
 "prompt": "Is there a Spanish or Portuguese entry 'greba'? Give its meaning and etymology verbatim (is it from Old French grève?)."
}
```


### [2026-09-06T02:26:27.371Z] TOOL RESULT

```
# Spanish Entry for "Greba"

Yes, there is a Spanish entry. According to the Wiktionary page:

**Meaning:** "greba" is "a piece of armor for the leg" (the article states it means "[greave](/wiki/greave#Etymology_3 "greave")")

**Etymology:** The page does not provide etymology information for the Spanish term, so I cannot confirm whether it derives from Old French *grève* based on this content. The etymology section only appears under the Basque entry, which notes that Basque "greba" was "[Borrowed](/wiki/Appendix:Glossary#loanword "Appendix:Glossary") from [French](https://en.wikipedia.org/wiki/French_language "w:French language") _[grève](/wiki/gr%C3%A8ve#French "grève")_."
```


## [2026-09-06T02:26:31.248Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://dle.rae.es/greba",
 "prompt": "Give the DRAE entry for 'greba' verbatim, especially the etymology line (Del ...)."
}
```


### [2026-09-06T02:26:33.033Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T02:26:35.147Z] TOOL CALL #64: WebSearch

```json
{
 "query": "DRAE greba etimología \"del fr. ant. greve\" armadura pierna"
}
```


### [2026-09-06T02:26:41.605Z] TOOL RESULT

```
Web search results for query: "DRAE greba etimología "del fr. ant. greve" armadura pierna"

Links: [{"title":"greba | Diccionario de la lengua española (2001) | RAE - ASALE","url":"https://www.rae.es/drae2001/greba"},{"title":"greba | Definición | Diccionario de la lengua española | RAE - ASALE","url":"https://dle.rae.es/greba"},{"title":"GREBA - Diccionario etimológico","url":"https://etimologias.dechile.net/?greba="},{"title":"greba Que es, Concepto y Definicion","url":"https://www.bibliatodo.com/Diccionario-biblico/greba"},{"title":"Greba - Wikipedia, la enciclopedia libre","url":"https://es.wikipedia.org/wiki/Greba"},{"title":"greba - Iedra.","url":"https://iedra.es/palabras/greba"},{"title":"Grebas Griegas, Romanas, Vikingas Y Medievales: La Evolución De La Protección De Las Piernas | ⚔️ Tienda-Medieval","url":"https://blog.tienda-medieval.com/grebas-griegas-espartanas-romanas-y-vikingas/"},{"title":"GREBA - Diccionario Abierto de Español","url":"https://www.significadode.org/greba.htm"},{"title":"GREBA - Definition and synonyms of greba in the Spanish dictionary","url":"https://educalingo.com/en/dic-es/greba"},{"title":"Greba","url":"https://es-academic.com/dic.nsf/eswiki/543729"}]

Based on the search results, here's the information about the DRAE entry for "greba":

## Definición

La greba es una pieza de la armadura antigua que cubría la pierna desde la rodilla hasta la garganta del pie.

## Etimología

La palabra procede del francés antiguo "grève". Según fuentes etimológicas más detalladas, la palabra greba es préstamo del francés grève, voz que se considera derivada de un verbo graver con el sentido de cavar y el más específico de labrar en hueco o en relieve algo.

La búsqueda encontró la entrada del DRAE (versión 2001) que corrobora exactamente la información que solicitaste: etimología "del fr. ant. grève" y que se trata de una armadura para la pierna.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T02:26:47.487Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/greba\" \"https://www.rae.es/drae2001/greba\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 200: Spanish/Portuguese greba 'greave' - direction of borrowing vs Old French greve\" 2>&1 | tail -1; done; echo ---; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-06T02:26:49.682Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2db166c2f3e12287.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a8f4b74bd5d6ee6f.txt
---
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


## [2026-09-06T02:26:52.307Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-06T02:26:52.398Z] TOOL RESULT

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


## [2026-09-06T02:28:20.166Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT hamvareti ===\"; grep -n \"hqm.varəti\\|hąm.varəti\\|hamvareti\\|varəti-\\|hqmvarəti\" BRT.txt | head -10; echo \"=== BRT vareta ===\"; grep -n \"^vart\\|varəθra\\|verethra\" BRT.txt | head -5; echo \"=== KNT vrta ===\"; grep -n -i \"vrta\\|varta-\\|hero\" KNT.txt | head -10"
}
```


### [2026-09-06T02:28:20.252Z] TOOL RESULT

```
=== BRT hamvareti ===
=== BRT vareta ===
=== KNT vrta ===
415:$14. EARLY STEPS IN THE DecipHERMENT. ОР inscriptions and writing are mentioned in a num- ber of ancient authors, from Herodotus onward, and are remarked upon and described by certain modern travelers early in the seventeenth century, who published parts of inscriptions from Per- sepolis in the accounts of their travels. The first inscription to be published in complete form was DPe, given by Chardin in 1711. Better copies of several were given in 1778 by Carsten Niebuhr, who recognized that the inscriptions were com- posed in three systems of writing, and that the writing ran from left to right: the direction of the writing was shown by two copies of XPe with somewhat differmg line-divisions. О. б. Tychsen in 1798 discovered that the three systems of writing represented three different languages, and that a recurrmg diagonal wedge in the simplest of the three types was a word-divider; but he wrongly assigned the inscriptions to the Parthian period. Friedrich Münter in 1802 inde- pendently identified the word-divider, and thought that a frequently recurring series of characters must be the word for ‘king’; he as- signed the mscriptions to the Achaemenian pe- riod
898:*ebherom, OP abaram, Skt. dbharam, Gk. ёфероу. *ekuom, OP asam, Skt. ат, Lt. equom.
1031:III. OP b is mostly from pIE bh; for pIE b was an extremely rare sound, and its only prob- able occurrence in OP is in d-big-na-, second component of Bagábigna-, if this is a participle to the root in Skt. bija- ‘seed’ (see Lex. s.v.). pIE *ebherom ‘I bore’, OP abaram ‘I esteemed’,
1127:$84. Finan DrENTALS were weakened and did not appear in the writing of OP. After d they re- mained in the pronunciation sufficiently to pre- vent the writing of the vowel as long (586.11): OP abara ‘he bore’, Skt. dbharat; OP 3d pl. abara, Skt. dbharan, for *ebheront. After à, it is likely that they disappeared entirely; for hyaparam seems to be abl. *hyid + aparam, and the crasis indicates a previous loss of the -d.
1596:There is a possibility that there was anaptyxis in the clusters dr br fr zr before a, but OP writ- ing can give no evidence on this point. NPers. has duróy = OP drauga, birddér = OP таа, jarmén = framünà; but the anaptyxis may be later than the OP period. For Zra*ka, Greek has Zapayya: (in Arrian) and Zapéyya (in Herodotus) with anaptyxis, but Greek has no initial sr- or zr-, and there is also the form Араүү:ауһ (in Diodorus) without anaptyxis, when the initial cluster is one which is normal in
1900:Xšayāršan- (from *zšaya-aršan-) ‘Hero of Kings’; Gau-baruv-a- ‘Lord of cattle’; Va'u-misa- ‘Friend of the good’.
1914:b. Genitive: Arta-xéaga- ‘Having a kingdom of justice’; Aršāma- (from *aría-ama-) ‘Having the might of a hero’; Haxd-manis- ‘Having the mind of a friend’; Garma-pada- ‘(Month) having the place of heat’; Asa-garta- (Тапа) having caves of stone’. :
2563:II. The secondary ending - was attached di- rectly to the thematic vowel -o-: pIE ebhero-m ‘I bore’, Skt. dbharam, Gk. éepor, OP abaram; Skt. dpyccham, OP aparsam. Other OP examples: niy- asddayam, franayam, arasam, etc. When attached to non-thematic stems, the -m became vocalic, and developed in pAr. to -am, a generalization of the antevocalic value, furthered by the identity
2580:I. The primary ending was pIE -néz, which was attached to the thematic vowel -o-: pIE *bheronti, Gk. Dor. $porri, Skt. bháranti, OP bara"tiy; Skt.
2583:II. The secondary ending was pIE -nt, which - lost the final ¢ in pAr. unless sentence phonetics ` permitted its retention; for in pAr. only a single consonant could stand at the end of a word. In OP, also, the final n was not written (§112). Be- fore this ending the thematic vowel was -o-: pIE *ebheront, Gk. égepov, Skt. dbharan, OP abara”; OP abava", anaya”, ayauda", asiyava", alarsa”, agar- báya"; passive арата", ayadiya". Non-thematic stems would normally have pIE -nt after conso- nants, becoming pAr. -at; but this was commonly replaced by -an(t) after the -am of the Ist sg.: pIE *és-nt, but Skt. азат, ОР аһа”; OP apariy- diya”, avájana",
```


## [2026-09-06T02:28:27.708Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT hamvar ===\"; grep -n -i \"hamvar\\|hqmvar\\|ham.var\\|Tapferkeit\" BRT.txt | head -8; echo \"=== KNT varta/vrta lexicon ===\"; grep -n -i \"varta-\\|vrta-\\|\\bvar-\\b\" KNT.txt | head -8; echo \"=== NYB var- ===\"; grep -n \"^gurt\\b\\|^gurt \" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T02:28:27.826Z] TOOL RESULT

```
=== BRT hamvar ===
11507:•  j.  Jayäurvah-,  Jiyäurvah-  Adj.  'wach, wachsam':  mihr3m..a:i^afn3m  *jayäurva- t?h»m  Yt  10.  7  '';  —  mi^r?m  timatahä^a jiySurum  VtJO.  141;  7^,42;  —  naityqm ham.var3itlm  .  .  äsitS^ätüm  jayäurBm (ÄSf.)'>  \.62.S.  Yt75.39  (wo  •rum).
11853:•  j.  taxmo.tasyah-  Adj.  'der  tapfrer  ist als  der  tapfre':  ham.varntlm  .  .  yä  *'ias- yayii'l  (als  NSf.!t'>  Vr.  7.  3.
16650:•  j.  bayö.baxta-  Adj.  'von  den  Göttern bestimmt,  gefügt':  'ttm  paiti  yaomm  Yt ^'.35;  _  =wVyLi'5(?).  a)  -fc«  ASn. als  Adv.  'auf  (besondere)  Fügung  der Götter'";  nairyqm  ham-varaitlm  ..yä  dim (sd.)  jasaiti  'ttmcit  ". .  die  sich,  und  zwar auf  besondere  Fügung  der  Götter,  bei  ihnen (den  Männern)  einstellt"  Vr.  7. 3.
18753:•  j.  nairyf^niJii^.vänti'vant-  Adj.  'der ' mannhafte  Tapferkeit  besitzt*;  tir7zSJa-\ man^m  Tantum  taxtnpm  Yt.  ig.  42.
23914:KompE.- Ableit  ««s  v^%'u,a..  -  Vü.-.  rama-   "  J-  vi-gi>r»ptay-  f  'Ergreifen,  Gefangen- m-,  s.  noch  No.  —  '>  So  nennt  sich  AhM.;   nähme,  -schafV;  nairyam  ham.varnUm  .  .
30001:I  •  j.  ham.varatay-,  ham-varetay-**  f, •Wehrhaftigkeit,  Tapfeikeit",  stets  mit nairya-    Adj.    verbunden:     däyä    mt  .  .
30004:I  der  mannhaften  Tapferkeit"  Yt.  io.  7 1 ;  —
=== KNT varta/vrta lexicon ===
=== NYB var- ===
1730:gurtéh
1744:gurtéh [gwltyh] a part of the warrior’s armour, *neck-protector’ 855. Skr ren- ders the series zen u zréh u ~ by sarva- sannüha- = tavoTaAta. — gurt- < *kur-t- from the root kur- discussed by Bailey, Nyberg Vol. 9-16: Av. (474) kuirit- (< kurit), nom. kwiris, Vd. 14°, following immediately after zräöö (v. zreh) in the enumeration of a Zoroastrian warrior’s armour, is rendered in Phl. by griv-pan ‘neck-protector’ with the gl. han i hac tarak apác 6 zre bast estet ‘that which is attached to the helmet at the back of the armour’. — Cf gri-kaft.
1748:gurt-vär [gwltw'l] worthy of a hero, heroic 272’, 281. — MPrthPrs gwrd (S, A-H III); NP gurd.
```


## [2026-09-06T02:28:34.186Z] AGENT

Now I'll write the verification file.


## [2026-09-06T02:36:24.618Z] TOOL CALL #69: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build200.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_WIKT_JAWRAB=\"https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%B1%D8%A8\"\nW_WIKT_GORD=\"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%AF\"\nW_WIKT_GUL=\"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%84\"\nW_WIKT_GURDUS=\"https://en.wiktionary.org/wiki/gurdus\"\nW_WIKT_BRADUS=\"https://en.wiktionary.org/wiki/%CE%B2%CF%81%CE%B1%CE%B4%CF%8D%CF%82\"\nW_WIKT_BARDUS=\"https://en.wiktionary.org/wiki/bardus\"\nW_WIKT_KORD=\"https://en.wiktionary.org/wiki/%D5%AF%D5%B8%D6%80%D5%A4\"\nW_WIKT_GREBA=\"https://en.wiktionary.org/wiki/greba\"\nW_ETY_GREAVE=\"https://www.etymonline.com/word/greave\"\nW_ABADIS_GUL=\"https://abadis.ir/fatofa/%DA%AF%D9%88%D9%84/\"\nW_ABADIS_JURAB=\"https://abadis.ir/fatofa/%D8%AC%D9%88%D8%B1%D8%A7%D8%A8/\"\nW_DRAE=\"https://www.rae.es/drae2001/greba\"\n\ndoc = {\n \"pdf_page\": 200,\n \"book_page\": 170,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n\n # ---------------- entry 7 : Persian Gurb, Kurb 'stocking' ----------------\n {\n  \"entry\": 7,\n  \"root\": \"Gŭrb, Kŭrb\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"New Persian گورب / گوراب gōrb, gōrāb 'stocking' (the Persian word behind Arabic جَوْرَب jawrab), of itself unexplained origin\",\n  \"note\": \"The Persian side of the root box is well documented. Mo'in's own lexicon, the reference Nourai cites, opens the entry جوراب with the equation '[= گوراب ـ گورب]' and defines it 'پایتابه‌ای که آن را از نخ‌های پنبه‌ای یا پشمی و یا ابریشمی بافند و پا را بدان پوشانند؛ ج. (ع.) جوارب', so گورب / گوراب as a Persian by-form of جوراب is Mo'in's, not Nourai's invention. The Arabic tradition says the same and says it earlier: al-Jawaliqi's al-Muʿarrab already lists «جورب» وأصله «كورب» among the words in which Persian k/g was replaced by Arabic j, and his editor's footnote quotes Lisān al-ʿArab 'والجورب لفافة الرجل معرب وهو بالفارسية كورب'. What is NOT established is where the Persian word itself comes from: al-ʿUnaysi (TAD) explains it as 'قبر الرجل' (the 'grave of the foot', گور + پا), Asbaghi 1988 offers گورپا gōl-pā / gōr-pā 'cloth for the foot' with a Syriac parallel, and Wiktionary keeps open an Aramaic gərāb 'leather pouch'. Nourai's own root label 'Kŭrb' with k- is exactly the Lisān's كورب, so the two spellings of the root box are both real. The whole western branch of the chart (Portuguese → Old French → English greave) rests on a single source, Klein, and is contradicted by the standard Spanish and French authorities: see nodes #3 and #4.\",\n  \"note_fa\": \"خانهٔ ریشه درست است تا آنجا که به فارسی و عربی مربوط می‌شود: معین در مدخل «جوراب» خود می‌نویسد «[= گوراب ـ گورب]» و آن را «پایتابه‌ای که از نخ‌های پنبه‌ای یا پشمی یا ابریشمی بافند» تعریف می‌کند، و جوالیقی در «المعرّب» پیش‌تر گفته بود «و«جورب» وأصله «كورب»»، و لسان‌العرب نیز «الجورب لفافة الرجل معرّب وهو بالفارسية كورب». پس صورت‌های «گورب/کورب» ساختهٔ نورایی نیست. اما خاستگاه خود واژهٔ فارسی روشن نیست: عنیسی آن را «قبر الرِّجل» (گور + پا) می‌داند، اصباغی «گورپا» را پیشنهاد می‌کند و ویکی‌واژه امکان وام‌گیری از آرامی gərāb «انبان چرمی» را باز می‌گذارد. شاخهٔ اروپایی نمودار (پرتغالی ← فرانسهٔ کهن ← انگلیسی) تنها بر کلاین استوار است و فرهنگ‌های معتبر اسپانیایی و فرانسوی جهت وام‌گیری را وارونه می‌دانند. حکم: با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_WIKT_JAWRAB, W_ABADIS_JURAB],\n  \"ref_check\": [\n    {\"ref\": \"MON:3434\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi, s.v. جوراب (MON_part1.txt line 48890): 'جوراب: [= گوراب ـ گورب] ۱) پایتابه‌ای که آن را از نخ‌های پنبه‌ای یا پشمی و یا ابریشمی بافند و پا را بدان پوشانند؛ ج. (ع.) جوارب.' The bracketed equation is exactly Nourai's root box. The local scan of Mo'in carries no page numbers, so p.3434 itself could not be confirmed; the abadis.ir copy of the Mo'in entry (فرهنگ معین) gives the same wording.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"ARB\", \"where\": \"al-Jawaliqi, al-Muʿarrab, muqaddima (ARB_mo3rb.txt line 2394)\", \"stance\": \"supports\", \"note\": \"'و«جورب» وأصله: «كورب»، و«مورج» وأصله: «موزة»' — in the list of Persian words whose k/g Arabic replaced with j.\"},\n    {\"src\": \"TAD\", \"where\": \"al-ʿUnaysi, Tafsir al-alfaz al-dakhila (TAD.txt line 2569)\", \"stance\": \"supports\", \"note\": \"'وجورب ج جوارب فارسي معناه قبر الرجل مرادفه لفافة الرجل' — 'jawrab, pl. jawārib, Persian, meaning the grave of the foot'; the گور 'grave' + پا 'foot' folk etymology.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, s.v. ǧaurāb (PLA_asbaghi_1988_ia_djvu.txt line 7779)\", \"stance\": \"partial\", \"note\": \"'ǧaurāb: „Schuh, Strumpf“ aus dem pers. جوراب ǧūrāb, eventuell … golpā „Stoff für den Fuß“' — Arabic from Persian, but Asbaghi's Persian etymon is گورپا, not گورب.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-farisiyya al-muʿarraba (grep 'جورب' in AFM.txt/AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"no hit: Addi Shir has no entry for جورب.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. جورب\", \"stance\": \"partial\", \"note\": \"'Possibly from (or cognate with) Persian جوراب (jôrâb)', earlier گورب (gôrab)/گوراب (gôrâb); also floats an Aramaic גְּרָב gərāb 'skin bottle, pouch'. Direction of borrowing left open.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Arabic\", \"words\": \"jaurb, jaurab; j.r.b\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"The Arabic word is جَوْرَب jawrab 'sock, stocking', pl. جَوَارِب jawārib; Nourai's 'jaurb, jaurab' renders the two vocalisations jawrab / jawrab~jaurab found in the lexica. The loan is old and the Arab lexicographers themselves label it aʿjamī: Ibn Durayd (Jamhara) has 'وجورب أعجمي معرب', and Lisān al-ʿArab, quoted in the notes to al-Jawaliqi's al-Muʿarrab, says 'والجورب لفافة الرجل معرب وهو بالفارسية كورب' — 'the jawrab, the foot-wrapping, is Arabicised; in Persian it is kūrb'. Persian initial g- regularly appears as Arabic j- in this stratum (گورب → جورب, exactly as al-Jawaliqi's list has گل > جل, موزه > مورج). Asbaghi 1988 confirms the direction (Persian → Arabic) while preferring گورپا as the etymon. The second line of the box, 'j.r.b : he wears socks', is not quite right: جورب is quadriliteral (j-w-r-b), not a triliteral root; what the lexica actually record is the denominative جَوْرَبَ jawraba 'he put socks on (someone)' and Ibn al-Sikkīt's تَجَوْرَبَ tajawraba 'he wore socks' — the phrase quoted in al-Jawaliqi's footnote, 'وجوربته جورب أى ألبسته الجورب فلبسه'. So a verb of that meaning exists, but it is derived from the noun, not a root behind it.\",\n    \"derivation_fa\": \"واژهٔ عربی جَوْرَب «جوراب» است (جمع: جَوارِب) و خودِ لغویان عرب آن را معرّب می‌دانند: ابن‌درید در «جمهرة» می‌آورد «وجورب أعجمي معرّب» و لسان‌العرب می‌گوید «والجورب لفافة الرِّجل معرّب وهو بالفارسية كورب». تبدیل گـ فارسی به جـ عربی در این لایه از وام‌واژه‌ها قاعده‌مند است (گورب ← جورب، درست مانند گل ← جل و موزه ← مورج در فهرست جوالیقی). اصباغی (۱۹۸۸) نیز جهت وام‌گیری (فارسی ← عربی) را تأیید می‌کند. اما سطر دوم خانه، «j.r.b: جوراب می‌پوشد»، دقیق نیست: «جورب» ریشهٔ سه‌حرفی ندارد و رباعی است (ج‌ـ و‌ـ ر‌ـ ب)؛ آنچه در متون آمده فعل مشتق از اسم است: جَوْرَبَ «به کسی جوراب پوشاند» و تَجَوْرَبَ «جوراب پوشید». حکم: با احتیاط پذیرفتنی است.\",\n    \"sources\": [W_WIKT_JAWRAB],\n    \"ref_check\": [\n      {\"ref\": \"FVF:177\", \"status\": \"not_checked\", \"note\": \"FVF = Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi (Tehran 1347). refs_online.json records no downloadable copy — only the noorlib.ir page viewer (browser/login) — so p.177 could not be read.\"},\n      {\"ref\": \"ARB:101\", \"status\": \"supports\", \"note\": \"al-Jawaliqi, al-Muʿarrab: the entry الجورب with editor's footnote (6) in ARB_mo3rb.txt line 8832: 'فى اللسان: «والجورب لفافة الرجل» معرب، وهو بالفارسية «كورب» … واستعمل ابن السكيت منه فعلاً … «وقد تجورب جوربين» يعنى لبسهما، و«جوربته جورب» أى ألبسته الجورب فلبسه.' The mo3rb text file carries no page breaks; the entry sits at 29% of the file, consistent with p.101 of the Shakir edition (bāb al-jīm).\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. greave (KLN_1966.txt line 16640, leaf 366)\", \"stance\": \"supports\", \"note\": \"'fr. Egypt. Arab. gaurab, corresponding to Arab. jaurab, „stocking, apparel for the leg“' — Klein's Arabic form is exactly Nourai's.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi s.v. ǧaurāb (line 7779)\", \"stance\": \"supports\", \"note\": \"'ǧaurāb: „Schuh, Strumpf“ aus dem pers. ǧūrāb' — listed among the Persian loanwords in Arabic.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (grep 'jaurab/jawrab' in FVQ.txt)\", \"stance\": \"silent\", \"note\": \"no hit — the word is not Qur'anic, so Jeffery has no entry; nothing for or against.\"},\n      {\"src\": \"TAD\", \"where\": \"al-ʿUnaysi (TAD.txt line 2569)\", \"stance\": \"supports\", \"note\": \"'وجورب ج جوارب فارسي' — flatly labels it Persian.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Persian\", \"words\": \"jŭrâb «جوراب»\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian جوراب jūrāb / jōrāb 'sock, stocking' is the Arabised form come home again — a Persian → Arabic → Persian round trip of the kind Nourai's chart draws correctly here. The native Persian گورب / گوراب survived only marginally (and in place-names such as گوراب in Gilan), while the Arabic-shaped جوراب with initial j- became the ordinary word from the classical period on; Mo'in's entry places the two side by side, 'جوراب: [= گوراب ـ گورب]', which is precisely a statement that the j-form and the g-form are the same word. The Arabic plural جوارب was borrowed with it (Mo'in: 'ج. (ع.) جوارب'). From Persian/Arabic the word travelled further: Ottoman Turkish çorap, whence Romanian ciorap, Bulgarian чорап, Serbian čarapa (Lokotsch no. 439).\",\n    \"derivation_fa\": \"«جوراب» فارسی نو همان صورت معرّبِ بازگشته به فارسی است؛ یعنی یک وام‌گیری رفت‌وبرگشتی: فارسی گورب/گوراب ← عربی جَوْرَب ← فارسی جوراب. صورت بومی «گوراب» تنها به‌صورت حاشیه‌ای (و در نام‌جای‌هایی چون گورابِ گیلان) ماند، حال آنکه صورت با جـِ عربی از دورهٔ کلاسیک به بعد واژهٔ رایج شد. معین همین را می‌گوید که «جوراب [= گوراب ـ گورب]» و جمع عربی آن «جوارب» را نیز نقل می‌کند. از فارسی/عربی به ترکی عثمانی çorap و از آنجا به رومانیایی ciorap و بلغاری/صربی چورَپ/čarapa رفت (لوکوچ، شمارهٔ ۴۳۹). حکم: ادعای نورایی درست است.\",\n    \"sources\": [W_WIKT_JAWRAB, W_ABADIS_JURAB],\n    \"ref_check\": [\n      {\"ref\": \"MON:3434\", \"status\": \"supports\", \"note\": \"MON_part1.txt line 48890, s.v. جوراب: '[= گوراب ـ گورب] … پایتابه‌ای که آن را از نخ‌های پنبه‌ای یا پشمی و یا ابریشمی بافند و پا را بدان پوشانند؛ ج. (ع.) جوارب.' Page number not checkable in the local page-less scan; the same text stands under فرهنگ معین on abadis.ir.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. جوراب (abadis.ir, فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"'(اِ.) پوششی که آن را از نخ‌های پنبه‌ای یا پشمی و یا ابریشمی بافند و پا را با آن پوشانند.'\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi s.v. ǧaurāb (line 7779)\", \"stance\": \"supports\", \"note\": \"Arabic ǧaurāb 'aus dem pers. ǧūrāb' — Asbaghi's Persian source form is already the j-form جوراب, i.e. the round trip Nourai draws.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 439, p.36 (LKT.txt line 1163, leaf 62)\", \"stance\": \"supports\", \"note\": \"'439. Tk. çorab: „Strumpf“; hieraus rum. ciorap „dass.“ …; bulg. čorap, serb. čarapa „Strumpf“' — the onward spread of the same word through Turkish.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Portuguese\", \"words\": \"greba\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"The Iberian word exists — Spanish greba 'pieza de la armadura antigua que cubría la pierna desde la rodilla hasta la garganta del pie' (Portuguese greva) — but the direction of the arrow is the one modern lexicography rejects. Klein 1966 s.v. greave is the sole authority for it: 'ME. greve, fr. OF. greve „shin; greave“, fr. Port. greba, fr. Egypt. Arab. gaurab, corresponding to Arab. jaurab' — i.e. Klein makes the Iberian form the source of the French. The Spanish Academy dictionary derives greba the other way round, 'del fr. ant. grève', and Wiktionary's Basque cognate is likewise 'borrowed from French grève'. Chronology supports the Academy: Old French grève 'shin' is 12th-century, Spanish greba only 15th-century, in the age when French plate-armour vocabulary flooded the Peninsula. Lokotsch's Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, the standard catalogue of exactly this kind of Arabism, has no entry for greba/grève at all, though it does carry جورب under Turkish çorab (no. 439) — a telling silence.\",\n    \"derivation_fa\": \"واژهٔ ایبریایی وجود دارد: اسپانیایی greba «ساق‌بندِ زره، پوششی که ساق پا را از زانو تا مچ می‌پوشاند» (پرتغالی greva)؛ اما جهت پیکان همان است که فرهنگ‌نویسی امروزی رد می‌کند. تنها منبع این ادعا کلاین (۱۹۶۶) است که می‌نویسد فرانسهٔ کهن grève از پرتغالی greba و آن از عربی مصری gaurab آمده. فرهنگ فرهنگستان اسپانیا (RAE) عکس آن را می‌گوید: greba «del fr. ant. grève»، و ویکی‌واژه نیز باسکی greba را وام از فرانسوی می‌داند. گواه تاریخی هم با فرهنگستان است: grève فرانسهٔ کهن از سدهٔ دوازدهم است و greba اسپانیایی از سدهٔ پانزدهم، یعنی روزگاری که واژگان زرهِ صفحه‌ایِ فرانسوی به شبه‌جزیره سرازیر شد. لوکوچ نیز که فهرست‌نویسِ همین گونه وام‌واژه‌های شرقی در زبان‌های اروپایی است، هیچ مدخلی برای greba/grève ندارد. حکم: پژوهش امروزی این حلقه را رد می‌کند.\",\n    \"sources\": [W_WIKT_GREBA, W_DRAE, W_ETY_GREAVE],\n    \"ref_check\": [\n      {\"ref\": \"KLN:678\", \"status\": \"supports\", \"note\": \"Klein 1966 (KLN_1966.txt line 16640, leaf 366, in the g-r-e range that falls on pp. ~677-679 of vol. I): 'greave, n., armor for the leg. — ME. greve, fr. OF. greve, „shin; greave“, fr. Port. greba, fr. Egypt. Arab. gaurab, corresponding to Arab. jaurab, „stocking, apparel for the leg“.' The reference says exactly what Nourai's arrow says; the reference is what is wrong, not the citation.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 s.v. greave\", \"stance\": \"supports\", \"note\": \"the source of the whole branch, quoted above.\"},\n      {\"src\": \"DRAE\", \"where\": \"Diccionario de la lengua española (2001) s.v. greba\", \"stance\": \"contradicts\", \"note\": \"'greba. (Del fr. ant. grève.) f. Pieza de la armadura antigua, que cubría la pierna desde la rodilla hasta la garganta del pie' — French to Spanish, not Spanish to French.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch 1927 (grep 'greba', 'grève', 'jaurab')\", \"stance\": \"silent\", \"note\": \"no entry — Lokotsch's catalogue of European orientalisms records جورب only as Turkish çorab (no. 439, p.36) and knows nothing of a Romance greba from it.\"},\n      {\"src\": \"DEV/PHN\", \"where\": \"Devic 1876 and Pihan 1866 (grep 'greve', 'greba', 'jaurab')\", \"stance\": \"silent\", \"note\": \"neither dictionary of French words of Oriental origin has grève among them.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Old French\", \"words\": \"greve\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"Old French grève 'shin; armour for the shin' is real and is first attested in the 12th century; from it come both the Middle English word (node #5) and, by all modern accounts, Spanish greba and Basque greba. What is disputed is its parent as drawn. Klein alone makes it a borrowing of Portuguese greba < Arabic; Etymonline reports the consensus — 'from Old French greve „shin, armor for the leg“ (12c.), of unknown origin' — and relegates Klein to a bracket: '[Klein suggests it ultimately is from Egyptian Arabic gaurab „stocking, apparel for the leg“.]' Funk & Wagnalls and Webster, which both have the word, give the chain only as far back as French and stop: 'Armor to protect the legs from knee to ankle … [< OF. greves, pl. of greve, shin]' (FSD); 'ME. greves … OFr. greves, legs from the ankle to the knee' (WEB). No French authority takes the word out of French, and none of the Arabism dictionaries (Lokotsch, Devic, Pihan, Lammens, Dozy) claims it. The node itself (the word, the language, the gloss) is correct; the edge Portuguese → Old French is not.\",\n    \"derivation_fa\": \"«grève» در فرانسهٔ کهن به معنی «ساق پا؛ ساق‌بندِ زره» واژه‌ای واقعی و از سدهٔ دوازدهم گواهی‌شده است و به اجماع فرهنگ‌ها خاستگاه greave انگلیسی (خانهٔ ۵) و نیز greba اسپانیایی و باسکی است. آنچه محل اختلاف است پدرِ ترسیم‌شدهٔ آن است: تنها کلاین آن را وام از پرتغالی greba و در نهایت از عربی می‌داند؛ اتیمولاین دیدگاه رایج را چنین می‌آورد: «از فرانسهٔ کهن grève «ساق، زرهِ ساق» (سدهٔ ۱۲م)، با خاستگاه ناشناخته»، و پیشنهاد کلاین را تنها در قلاب می‌آورد. فانک‌ اند واگنالز و وبستر هم زنجیره را تا فرانسوی می‌برند و می‌ایستند. هیچ‌یک از فرهنگ‌های وام‌واژه‌های شرقی در فرانسوی (لوکوچ، دویک، پیان، لامنس، دوزی) این واژه را از آنِ خود نمی‌داند. خودِ خانه (واژه، زبان، معنی) درست است؛ پیکانِ پرتغالی ← فرانسهٔ کهن درست نیست.\",\n    \"sources\": [W_ETY_GREAVE, W_DRAE],\n    \"ref_check\": [\n      {\"ref\": \"KLN:678\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. greave: 'OF. greve, „shin; greave“, fr. Port. greba' — verbatim Nourai's arrow.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"Etymonline\", \"where\": \"s.v. greave (n.)\", \"stance\": \"contradicts\", \"note\": \"'from Old French greve „shin, armor for the leg“ (12c.), of unknown origin. [Klein suggests it ultimately is from Egyptian Arabic gaurab „stocking, apparel for the leg.“]' — the Arabic route is reported as one man's suggestion, not the received etymology.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, vol. 2 s.v. greaves³ (FSD_vol2.txt line 36555)\", \"stance\": \"partial\", \"note\": \"'Armor to protect the legs from knee to ankle … [< OF. greves, pl. of greve, shin.]' — stops at Old French, no Iberian or Arabic step.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. greaves (WEB_vol1.txt line 84255)\", \"stance\": \"partial\", \"note\": \"'ME. greves, grayvez … OFr. greves, legs from the ankle to the knee' — likewise stops at Old French.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (grep 'greave' in SKT.txt)\", \"stance\": \"silent\", \"note\": \"Skeat's OCR carries only greaves 'sediment of melted tallow' (< Low German greven); the armour word is not treated, so no support for the Arabic route from him either.\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"English\", \"words\": \"greave\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"English greave 'armour for the leg below the knee' is Middle English greve, borrowed from Old French grève in the 13th–14th century (c. 1300 in Etymonline; the plural greaves is the usual form, as in the arming descriptions of Sir Gawain and Malory) — this last link of the chain is uncontroversial and is given identically by Klein, Funk & Wagnalls ('< OF. greves, pl. of greve, shin'), Webster ('ME. greves, grayvez … OFr. greves') and Etymonline. Nourai's own NOTE, 'AHD:577 derives this word from a different root', is worth taking seriously and is best read as follows: the American Heritage Dictionary's Indo-European index assigns GREAVES to the root ghrebh-² 'to dig, bury, scratch' (via Low German greven 'fibrous refuse of tallow'), which is the homonym greaves 'cracklings, tallow sediment', an entirely different word of Low German origin — so AHD is not contradicting the armour word's French origin, it is indexing the other greaves. On the deeper question the modern view is Etymonline's: Old French grève is 'of unknown origin', Klein's Arabic derivation being a suggestion only.\",\n    \"derivation_fa\": \"انگلیسی greave «زرهِ ساق پا» از انگلیسی میانه greve و آن وام از فرانسهٔ کهن grève در سده‌های سیزدهم–چهاردهم میلادی است (اتیمولاین: حدود ۱۳۰۰م)؛ این حلقهٔ پایانی زنجیره هیچ اختلافی ندارد و کلاین، فانک اند واگنالز، وبستر و اتیمولاین همگی یکسان می‌گویند. یادداشت خودِ نورایی که «AHD:577 این واژه را از ریشهٔ دیگری می‌گیرد» شایستهٔ توجه است: در پیوستِ ریشه‌های هندواروپاییِ فرهنگ American Heritage واژهٔ GREAVES ذیل ریشهٔ ghrebh-² «کندن، دفن کردن» آمده، ولی آن، واژهٔ هم‌آوای دیگری است، یعنی greaves «تفالهٔ پیهِ گداخته» از آلمانی سفلی greven — پس AHD خاستگاه فرانسویِ نامِ زره را رد نمی‌کند، بلکه واژهٔ دیگری را فهرست کرده است. دربارهٔ خاستگاه ژرف‌تر، دیدگاه امروزی همان اتیمولاین است: grève فرانسهٔ کهن «با خاستگاه ناشناخته». حکم: این حلقه درست است.\",\n    \"sources\": [W_ETY_GREAVE],\n    \"ref_check\": [\n      {\"ref\": \"KLN:678\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. greave (KLN_1966.txt line 16639-16640): 'greave, n., armor for the leg. — ME. greve, fr. OF. greve …'\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. ghrebh-² (AHD_watkins1985.txt lines 526, 1567)\", \"stance\": \"partial\", \"note\": \"'GREAVES ghrebh-2' in the index, and under the root '4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES.' — this is greaves 'tallow cracklings', not the armour; so the NOTE's 'different root' concerns a homonym.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 2 (line 36555)\", \"stance\": \"supports\", \"note\": \"'greaves³ … Armor to protect the legs from knee to ankle: used also in the singular. [< OF. greves, pl. of greve, shin.]' and separately 'greaves⁴ … Pieces of boiled tallow-scrap; cracklings … [Of LG. or Scand. orig.]' — the two homonyms kept apart, exactly as needed to read the NOTE.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. greave (n.)\", \"stance\": \"supports\", \"note\": \"'c. 1300, from Old French greve „shin, armor for the leg“ (12c.)'.\"}\n    ]\n   }\n  ]\n },\n\n # ---------------- entry 8 : IE Gurdos 'brave, proud' ----------------\n {\n  \"entry\": 8,\n  \"root\": \"Gurdos, Gurdus (brave, proud)\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Mann's *gʷr̥dos/-us '(standing) stiff, ungainly or haughty' — a lemma of Walde-Pokorny I 641 that Pokorny 1959 and Watkins/AHD no longer carry\",\n  \"note\": \"The root box reproduces Nourai's source faithfully: Mann, IEC p.307 (leaf 181 of the local scan, running heads 306/307) opens 'gurdos, ios, us „swollen, proud, stout, brave, violent“ … WP I, 641, 649-650, II, 278', and lists under it 'Per. (ambig. OPer.?) gurd „hero“; Arm. cf. kord „rough“; OCS grŭdŭ „proud; horrid“; R. gordyj …'. Mann's own authority, Walde-Pokorny I 641, does carry the lemma but with a question mark — 'gurdo-s? „steif, unbeholfen oder anmaßend dastehend“ (gʷr̥du-s? s. u.)' — and its material is Latin gurdus and the Slavic words, no Iranian at all. Pokorny's 1959 IEW dropped it: there is no gʷerd- lemma, Latin gurdus is dismissed with a bare cross-reference ('about Latin gurdus s. WH. I 627'), and Old Church Slavonic grъdъ / Russian gordyj are put under ghreu-d- 'to rub, crush'. Watkins's AHD appendix has nothing of the kind either. So this 'root' is Mann's, not standard, and it must further be said that the Persian branch drawn beneath it (Old Persian *vṛta- → Pahlavi gurt → گرد) has a completely different and much better attested source: Hübschmann's derivation from the verbal root var- 'to ward, protect' (Av. hąm-varəti- 'valour'), which is what BOTH of Nourai's own references for that branch, HUB:91 and Mo'in's footnote in Borhān, actually say. The Persian material is therefore right in itself and wrongly hung on this root.\",\n  \"note_fa\": \"خانهٔ ریشه، منبع نورایی را درست بازمی‌تاباند: مان در IEC ص ۳۰۷ می‌نویسد «gurdos, ios, us „swollen, proud, stout, brave, violent“ … WP I, 641, 649-650, II, 278» و ذیل آن «Per. (ambig. OPer.?) gurd „hero“؛ Arm. cf. kord „rough“؛ OCS grŭdŭ» را می‌آورد. مأخذ خود مان، والده‑پوکورنی ج۱ ص ۶۴۱، این ماده را با علامت پرسش دارد: «gurdo-s? „steif, unbeholfen oder anmaßend dastehend“ (gʷr̥du-s?)» و موادش تنها لاتینی gurdus و واژه‌های اسلاوی است، بی هیچ نمونهٔ ایرانی. پوکورنی در چاپ ۱۹۵۹ این ماده را کنار گذاشت: نه مدخلی برای gʷerd- دارد، gurdus لاتینی را تنها با ارجاع به والده‑هوفمان رد می‌کند و grъdъ اسلاوی کهن و gordyj روسی را ذیل ghreu-d- «سودن، خرد کردن» می‌آورد؛ واتکینز نیز چنین ریشه‌ای ندارد. مهم‌تر آنکه شاخهٔ ایرانیِ زیر آن (پارسی باستان *vṛta- ← پهلوی gurt ← گرد) ریشه‌شناسی کاملاً دیگری دارد که هر دو مرجعِ خودِ نورایی (هوبشمان ۹۱ و حاشیهٔ معین در برهان قاطع) می‌گویند: از ستاک var- «پاسداشتن، دفاع کردن»، هم‌ریشه با اوستایی hąm-varəti- «دلیری». پس مواد فارسی درست‌اند اما زیر ریشهٔ نادرستی نشسته‌اند. حکم: با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_WIKT_GORD],\n  \"ref_check\": [\n    {\"ref\": \"IEC:307\", \"status\": \"supports\", \"note\": \"Mann, IEC, leaf 181 of IEC.txt (running heads '306','307'): 'gurdos, ios, us „swollen, proud, stout, brave, violent“. (This form is often coincidental with type *gurdus „sluggish, ponderous, awkward“ … an extn. of type *gurus „heavy“ …). WP I, 641, 649-650, II, 278 … Per. (ambig. OPer.?) gurd „hero“; Oss. qal (1) „proud“; Arm. cf. kord „rough“ … OCS grŭdŭ „proud; horrid“; R. gordyj, Cz. hrdý „proud“.' The cited page is exactly right.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 641 (WLD_Bd1_pages.txt leaf 649, running head 'gurdo-s? — ghr̥d 641')\", \"stance\": \"partial\", \"note\": \"'gurdo-s? „steif, unbeholfen oder anmaßend dastehend“ (gʷr̥du-s? s. u.). Lat. gurdus „dumm, tölpelhaft“ …, aksl. grъdъ, russ. górdyj „stolz, hochmütig“.' The lemma exists, but with a query and with no Iranian material whatever.\"},\n    {\"src\": \"POK\", \"where\": \"Pokorny IEW: no gʷerd- lemma; ghreu-d- (POK_full.txt line ~34086) and gʷer-2 'heavy' p.476 (line 39519)\", \"stance\": \"contradicts\", \"note\": \"Pokorny gives Slavic 'Old Church Slavic grъdъ „horrendus, terribilis“ … russ. gordyj' under the extension ghreu-d- 'to rub', and disposes of the Latin word in one line, 'about Latin gurdus s. WH. I 627'. He recognises no root of this shape.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷerə-2 'Heavy' [Pok. 2. gʷer- 476]\", \"stance\": \"silent\", \"note\": \"the appendix has gʷerə-² 'Heavy' (gravis, barus, guru-, brūtus) but no gʷerd-/gurdos and no 'brave, proud' root.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms (concepts 'BRAVE', 'PROUD')\", \"stance\": \"silent\", \"note\": \"Buck's discussions of 'brave' and 'proud' nowhere set up a common IE *gʷr̥d-; the Slavic 'proud' words are treated as a Slavic-internal group.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"Vtra, Vurt\",\n    \"verdict\": \"transcription_suspect\",\n    \"error_in\": \"book\",\n    \"book_prints\": \"Vtra, Vurt\",\n    \"correct_form\": \"*vṛta- (Vrta) / *vurt\",\n    \"derivation\": \"The printed page (pdf 200, book p.170) really does read 'Vtra, Vurt : hero', with no diacritics — the JSON extraction is faithful — but 'Vtra' is an impossible Old Iranian shape and is a metathesis misprint for *Vṛta-. Nourai's own reference proves it: Hübschmann, Persische Studien p.91 no. 899, reads 'Vgl. zd. varəti- in hąm-varəti- „Tapferkeit“. Phl. gurt steht für älteres *vurt = ap. *vṛta-' — 'Pahlavi gurt stands for an older *vurt = Old Persian *vṛta-'. Mo'in's footnote in Borhān-e Qāteʿ says the same in Persian, 'در پهلوی gurt. از ریشهٔ var، پارسی باستان -vrta-، هوبشمان ۸۹۹'. So the two forms in the box are Hübschmann's *vṛta- (the Old Iranian ancestor) and *vurt (the intermediate); the vocalic r̥ was lost in printing. Note further that the form itself is unattested: Kent's Old Persian lexicon has no varta-/vṛta- 'hero', so 'Old Persian' here means 'reconstructed Old Iranian', and — decisively for the chart — a form beginning in v- cannot descend from an Indo-European root *gʷr̥dos, since Iranian *gʷ gives g-, not v-. The word belongs to the root var- 'to ward off, protect' (Av. ham.varətay- f. 'Wehrhaftigkeit, Tapferkeit', Bartholomae AiW s.v.), not here.\",\n    \"derivation_fa\": \"صفحهٔ چاپی (صفحهٔ ۲۰۰ پی‌دی‌اف، ص ۱۷۰ کتاب) به‌روشنی «Vtra, Vurt : hero» را می‌آورد و بی هیچ نشانه‌گذاری — پس خطای خوانشِ اسکن در کار نیست و داده‌ها وفادارند — اما «Vtra» صورتی ناممکن در ایرانی باستان است و قلبِ چاپیِ *Vṛta- است. مرجعِ خودِ نورایی این را ثابت می‌کند: هوبشمان در «مطالعات فارسی» ص ۹۱ شمارهٔ ۸۹۹ می‌نویسد «Vgl. zd. varəti- in hąm-varəti- „Tapferkeit“. Phl. gurt steht für älteres *vurt = ap. *vṛta-». معین نیز در حاشیهٔ برهان قاطع همین را به فارسی آورده: «در پهلوی gurt. از ریشهٔ var، پارسی باستان -vrta-، هوبشمان ۸۹۹». افزون بر این، این صورت گواهی‌شده نیست؛ در واژه‌نامهٔ پارسی باستانِ کنت چنین واژه‌ای نیست، پس «پارسی باستان» اینجا یعنی «ایرانی باستانِ بازسازی‌شده». و نکتهٔ تعیین‌کننده: صورتی که با v- آغاز می‌شود نمی‌تواند از ریشهٔ هندواروپاییِ *gʷr̥dos بیاید، زیرا *gʷ در ایرانی به g بدل می‌شود نه به v. این واژه از ستاک var- «پاسداشتن» است (اوستایی ham.varətay- «دلیری»، بارتولومه). حکم: خطای چاپی کتاب.\",\n    \"sources\": [W_WIKT_GORD],\n    \"ref_check\": [\n      {\"ref\": \"HUB:91\", \"status\": \"supports\", \"note\": \"Hübschmann, Persische Studien, HUB.txt leaf 101 = printed p.91 (header '— 91 —'), no. 899: 'Vgl. zd. varəti- in hąm-varəti- „Tapferkeit“. Phl. gurt steht für älteres *vurt = ap. *vṛta-.' Both of Nourai's forms come from this line; the page is exactly right.\"},\n      {\"ref\": \"BQT:1786\", \"status\": \"supports\", \"note\": \"Borhān-e Qāteʿ with Mo'in's notes, s.v. گرد, footnote 9: 'در پهلوی gurt . از ریشهٔ var ، پارسی باستان -vrta- ، «هوبشمان ۸۹۹»'. Read from the rendered scan (data/verification/sources/refs/ocr/BQT/1786.png = BQT_v3_picofile.pdf p.583, saved as 1786.vision.txt). CAVEAT: the running head of that leaf prints ۱۷۸۹, so this scan runs ~3 pages ahead of Nourai's citation; the entry meant is unquestionably this one, since it also carries the Ferdowsi verse Nourai quotes.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie no. 899, p.200 (HRN.txt leaf 221, header '— 200 —')\", \"stance\": \"supports\", \"note\": \"'899. gurd „Held“. [√var- „beschützen, wehren“, vergl. ai. vṛt- „Heer“; phlv. gurt „Held“ (AV.), gurtīh vd. 20 (21).' — the root is var-, not a gʷerd-.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch s.v. ham.varətay- (BRT.txt line 30001)\", \"stance\": \"supports\", \"note\": \"'ham.varətay-, ham-varetay- f. „Wehrhaftigkeit, Tapferkeit“, stets mit nairya- Adj. verbunden' — the Avestan abstract Hübschmann compares, from var-.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (grep 'vṛta', 'varta-')\", \"stance\": \"silent\", \"note\": \"no such Old Persian entry: the form is a reconstruction, not an attested inscriptional word.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.307\", \"stance\": \"partial\", \"note\": \"Mann himself hedges the Iranian: 'Per. (ambig. OPer.?) gurd „hero“' — he cites the New Persian form, not any *vṛta-, and marks the Old Persian status as doubtful.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Armenian\", \"words\": \"kord\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"The Armenian word is real — Old and Modern Armenian կորդ kord, adjective 'unploughed, uncultivated (of land)', dialectally 'hard', and as a noun 'fallow land' — but Nourai's gloss 'rough' and its attachment to this root are both Mann's, and Mann himself hedges: his line at IEC 307 reads 'Arm. cf. kord „rough“, beside nkrtem „try“?', where 'cf.' and the question mark mark it as a comparison, not a derivation. Armenian etymology takes the word elsewhere: Wiktionary (following Martirosyan) leaves the origin uncertain and offers either a connection with Old Armenian խորթ xortʻ or a PIE *gʰordʰo- 'enclosure' (Proto-Slavic *gordъ, Proto-Germanic *gardaz), with an original sense 'enclosed pasture-land, pen'. That reconstruction has a plain velar and an aspirated dental, neither of which can be reconciled with a labiovelar *gʷr̥d-. There is also a semantic gap: 'untilled land' is not 'brave, proud'. So the node contradicts nothing in Armenian, but the arrow from this root is not what the Armenian literature draws.\",\n    \"derivation_fa\": \"واژهٔ ارمنی واقعی است: կորդ (kord) در ارمنی کهن و امروزی صفت است به معنی «شخم‌نخورده، نکاشته (دربارهٔ زمین)» و در گویش‌ها «سخت»، و به‌عنوان اسم «زمین بایر». اما هم معنی «زبر/خشن» که نورایی آورده و هم بستن آن به این ریشه از مان است، و خودِ مان محتاطانه نوشته: «Arm. cf. kord „rough“, beside nkrtem „try“?» که «cf.» و علامت پرسش نشان می‌دهد این تنها یک مقایسه است نه اشتقاق. ریشه‌شناسی ارمنی راه دیگری می‌رود: ویکی‌واژه (به پیروی از مارتیروسیان) خاستگاه را نامعلوم می‌داند و یا پیوند با խորթ ارمنی کهن یا بازسازی هندواروپایی *gʰordʰo- «چراگاهِ محصور، آغل» (اسلاوی آغازین *gordъ، ژرمنی آغازین *gardaz) را پیش می‌نهد. آن بازسازی کامِ ساده و دندانیِ دمیده دارد و با لبی‑کامیِ *gʷr̥d- سازگار نیست؛ افزون بر این «زمین نکاشته» با «دلیر، سرافراز» فاصلهٔ معنایی دارد. حکم: پژوهش امروزی این پیوند را نمی‌پذیرد.\",\n    \"sources\": [W_WIKT_KORD],\n    \"ref_check\": [\n      {\"ref\": \"IEC:307\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 181 (p.307): '… Arm. cf. kord „rough“, beside nkrtem „try“?' — Nourai's node is a straight lift of Mann's line, gloss included; Mann's own 'cf.' and '?' are what the chart drops.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. կորդ (kord)\", \"stance\": \"contradicts\", \"note\": \"'unploughed, uncultivated; dialectally hard' — 'Origin uncertain. Perhaps related to խորթ (xortʻ); or from *gʰordʰo- (cf. Proto-Slavic *gordъ, Proto-Germanic *gardaz), the original meaning being „enclosed pasture-land, pen“'.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 641 (leaf 649)\", \"stance\": \"silent\", \"note\": \"the lemma gurdo-s? lists only Latin gurdus and the Slavic words; Armenian kord does not appear there, so Mann's Armenian is his own addition to WP's material.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny IEW (grep 'kord')\", \"stance\": \"silent\", \"note\": \"no Armenian kord under any root of this shape.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Pahlavi\", \"words\": \"gort, gurt\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Middle Persian gurd, written gwlt' in Book Pahlavi and gwrd in Manichaean/Parthian script, 'hero, brave, warrior', is solidly attested and is exactly the form the chart wants: MacKenzie's Concise Pahlavi Dictionary has 'gurd [gwlt' | P gwrd] hero' with the derivative 'gurdwar [gwltw'l] befitting a hero', and Nyberg's Manual of Pahlavi II glosses 'gurt-vār [gwltw'l] worthy of a hero, heroic 272', 281. — MPrthPrs gwrd (S, A-H III); NP gurd.' Horn no. 899 cites it from the Ardā Wīrāz text ('phlv. gurt „Held“ (AV.), gurtīh'). Nourai's two spellings 'gort, gurt' are simply the two conventional readings of the same gwlt' — Mo'in's footnote in Borhān transliterates it gurt, MacKenzie gurd; the vowel is short u and the final stop is written with t in the older, d in the newer convention. The step from the pre-form *vurt/*vṛta- is Hübschmann's regular one: Old Iranian initial v- before a labial vowel becomes g- in Middle Persian (the same change as in gurg 'wolf' < *vṛka-, gōšt 'meat', guftan < *gaub-), so *vurt > gurt.\",\n    \"derivation_fa\": \"فارسی میانه gurd، در پهلوی کتابی gwlt' و در پارتی/مانوی gwrd، به معنی «پهلوان، دلیر»، به‌خوبی گواهی شده و دقیقاً همان صورتی است که نمودار می‌خواهد: مکنزی در «فرهنگ کوچک پهلوی» می‌آورد «gurd [gwlt' | P gwrd] hero» و مشتق «gurdwar [gwltw'l] befitting a hero»؛ نیبرگ در ج۲ «راهنمای پهلوی» می‌نویسد «gurt-vār [gwltw'l] worthy of a hero, heroic … MPrthPrs gwrd؛ NP gurd»؛ و هرن (شمارهٔ ۸۹۹) آن را از «ارداویراف‌نامه» شاهد می‌آورد. دو املای نورایی («gort, gurt») تنها دو خوانش قراردادیِ همان gwlt' است. گذار از صورت پیشین *vurt/*vṛta- تحول آواییِ قاعده‌مندِ ایرانی است: و‑ آغازینِ ایرانی باستان پیش از واکهٔ لبی در فارسی میانه به گـ بدل می‌شود (همان دگرگونی که در «گرگ» < *vṛka- دیده می‌شود)، پس *vurt > gurt. حکم: ادعای نورایی درست است.\",\n    \"sources\": [W_WIKT_GORD],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1786\", \"status\": \"supports\", \"note\": \"Mo'in's footnote 9 to گرد in Borhān-e Qāteʿ (scan p.1789 = BQT_v3 pdf p.583, saved at data/verification/sources/refs/ocr/BQT/1786.vision.txt): 'در پهلوی gurt . از ریشهٔ var ، پارسی باستان -vrta- ، «هوبشمان ۸۹۹»' — the Pahlavi form and its reading gurt are Mo'in's own.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt line 2621)\", \"stance\": \"supports\", \"note\": \"'gurd [gwlt' | P gwrd] hero.' with 'gurdwar [gwltw'l] befitting a hero' at line 2626.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. gurt-vār (NYB_vol2_glossary.txt line 1748)\", \"stance\": \"supports\", \"note\": \"'gurt-vār [gwltw'l] worthy of a hero, heroic 272', 281. — MPrthPrs gwrd (S, A-H III); NP gurd.'\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 899, p.200\", \"stance\": \"supports\", \"note\": \"'phlv. gurt „Held“ (AV.), gurtīh vd. 20 (21)' — attested in the Ardā Wīrāz text.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Persian\", \"words\": \"gord «گرد»\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian گرد gord 'hero, champion, brave man' continues Middle Persian gurd (gwlt') without change beyond the ordinary Middle-to-New Persian shortening/lowering of the vowel; Wiktionary states it flatly, 'Inherited from Middle Persian gwlt' /gurd/ „hero“', comparing Central Kurdish گورد gurd 'hero, brave'. The chart's extra forms are genuine derivatives of it: گردان gordān, the plural used collectively for the champions of the Shāhnāma, and گردزاد gord-zād 'born of a hero'. The Ferdowsi line the chart prints, 'بهومان چنین گفت سهراب گرد / که اندیشه از دل بباید سترد', is the same verse Mo'in cites in his footnote to گرد in Borhān-e Qāteʿ (crediting Loghat-e Fors 698), so it is quoted from Nourai's own source and is correctly attributed. The one thing that does not follow is the position of this word in the chart: gord goes back through gurt to *vurt/*vṛta- and the root var- 'to ward, protect' (Horn, Hübschmann, Mo'in), not to an Indo-European *gʷr̥dos.\",\n    \"derivation_fa\": \"«گرد» در فارسی نو به معنی «پهلوان، دلاور» دنبالهٔ بی‌واسطهٔ gurd فارسی میانه (gwlt') است و جز کوتاه‌شدن/تغییر کیفیت واکه دگرگونی دیگری نیافته؛ ویکی‌واژه صریح می‌گوید «برگرفته از فارسی میانه gwlt' /gurd/ „پهلوان“» و کردی سورانی «گورد» را هم‌ریشه می‌داند. صورت‌های افزودهٔ نمودار نیز مشتق‌های راستین همان‌اند: «گردان» (جمعِ پهلوانان شاهنامه) و «گردزاد» «زادهٔ پهلوان». بیتِ فردوسی که در نمودار آمده — «بهومان چنین گفت سهراب گرد / که اندیشه از دل بباید سترد» — همان بیتی است که معین در حاشیهٔ «گرد» در برهان قاطع (به نقل از لغت فرس ۶۹۸) آورده؛ پس شاهد از مأخذ خودِ نورایی است و درست نسبت داده شده. تنها چیزی که درست نیست جای این واژه در نمودار است: «گرد» از راه gurt به *vurt/*vṛta- و ستاک var- «پاسداشتن» می‌رسد (هرن، هوبشمان، معین)، نه به ریشهٔ هندواروپایی *gʷr̥dos. حکم: خودِ حلقهٔ فارسی درست است.\",\n    \"sources\": [W_WIKT_GORD],\n    \"ref_check\": [\n      {\"ref\": \"HRN:200\", \"status\": \"supports\", \"note\": \"Horn's numbered entry 899 stands on printed p.200 (HRN.txt leaf 221, header '— 200 —'): '899. gurd „Held“ … phlv. gurt „Held“ (AV.)'. Nourai's page citation is exact.\"},\n      {\"ref\": \"BQT:1786\", \"status\": \"supports\", \"note\": \"Borhān-e Qāteʿ s.v. گرد: 'و بفتح اول، مبارز و دلاور و بهادر و شجاع را گویند ۹' with footnote 9 giving the Pahlavi and Old Persian forms and the Ferdowsi verse that the chart prints. Read from the rendered image (ocr/BQT/1786.png, pdf p.583); the leaf's running head prints ۱۷۸۹, ~3 pages ahead of the citation.\"},\n      {\"ref\": \"IEC:307\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 181 (p.307): 'Per. (ambig. OPer.?) gurd „hero“' — Mann does list the Persian word under his root, so the citation supports the arrow, but with an explicit '(ambig. OPer.?)' hedge and with no phonological argument.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. گرد, etymology 'hero'\", \"stance\": \"supports\", \"note\": \"'Inherited from Middle Persian gwlt' /gurd/, „hero“. Akin to Central Kurdish گورد (gurd, „hero, gentleman, brave“) and گورج (gurc, „ready, alert, swift“).' No Indo-European *gʷr̥d- is invoked.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. gurd (line 2621)\", \"stance\": \"supports\", \"note\": \"'gurd [gwlt' | P gwrd] hero' — the direct Middle Persian ancestor.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.91 no. 899\", \"stance\": \"partial\", \"note\": \"supports the Persian word and its Pahlavi ancestor but assigns it to var-: 'Phl. gurt steht für älteres *vurt = ap. *vṛta-', which is incompatible with the root box above it.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in's footnote in Borhān (ocr/BQT/1786.vision.txt)\", \"stance\": \"partial\", \"note\": \"'در پهلوی gurt. از ریشهٔ var، پارسی باستان -vrta-' — same split: the word is right, the root is not Nourai's.\"}\n    ]\n   }\n  ]\n },\n\n # ---------------- entry 9 : IE Gurdos 'sluggish, stupid' ----------------\n {\n  \"entry\": 9,\n  \"root\": \"Gurdos, Gurdus (sluggish, stupid)\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *gʷr̥dus 'slow, sluggish', a u-stem beside *gʷerh₂- 'heavy' (Walde-Pokorny I 641; Mann IEC 373)\",\n  \"note\": \"This root box is sound, and better supported than its twin on the same page. Mann's entry at IEC p.373 (leaf 217 of the local scan, running head '373') reads 'gurdos, us (form of gurdos, us, q.v.) „sluggish, stupid, stiff, awkward“. Cf. WP I, 641 & II, 278 … Per. gül „idiot“; … Gk. bradús „sluggish“; LW in Lat. bardus „sluggish, stupid“; Lat. gurdus „stupid“ … Li. gurdùs „sluggish, ailing, weak“; Latv. gurds „tired, faint“' — every one of Nourai's four boxes, in Mann's own order. Independently, Wiktionary reconstructs precisely *gʷr̥dus 'slow' as the source of Greek βραδύς, with Latin gurdus, Lithuanian gurdùs and Latvian gur̃ds as cognates, and notes the formal and semantic tie to *gʷreh₂-/*gʷerh₂- 'heavy'; Pokorny, though he has no gʷr̥du- lemma, puts the Baltic members (Lith. gurstu/gurti, Latv. gurds 'fatigued, faint') under gʷer-2 'heavy', p.476. Nourai's separation of this root from the 'brave, proud' one is Mann's own — Mann prints the two as near-homophones and expressly warns that they are 'often coincidental'. The weak point of the chart is not the root but its Persian box: see node #1.\",\n  \"note_fa\": \"این خانهٔ ریشه استوار است و از همتای خود در همین صفحه پشتوانهٔ بهتری دارد. مدخل مان در IEC ص ۳۷۳ چنین است: «gurdos, us (form of gurdos, us, q.v.) „sluggish, stupid, stiff, awkward“. Cf. WP I, 641 & II, 278 … Per. gül „idiot“؛ … Gk. bradús „sluggish“؛ LW in Lat. bardus؛ Lat. gurdus „stupid“ … Li. gurdùs؛ Latv. gurds» — یعنی هر چهار خانهٔ نورایی، به همان ترتیبِ مان. مستقل از آن، ویکی‌واژه دقیقاً *gʷr̥dus «کند» را برای βραδύς یونانی بازسازی می‌کند و gurdus لاتینی و gurdùs لیتوانیایی و gur̃ds لتونیایی را هم‌ریشهٔ آن می‌شمارد و پیوند صوری و معناییِ آن را با *gʷerh₂- «سنگین» یادآور می‌شود؛ پوکورنی نیز اگرچه چنین مدخلی ندارد، اعضای بالتیک را ذیل gʷer-2 «سنگین» (ص ۴۷۶) می‌آورد. جدا کردن این ریشه از ریشهٔ «دلیر، سرافراز» نیز کارِ خودِ مان است و او صریح می‌گوید این دو «بارها بر هم منطبق می‌شوند». نقطهٔ ضعف نمودار خودِ ریشه نیست، بلکه خانهٔ فارسیِ آن است (خانهٔ ۱). حکم: ادعای نورایی دربارهٔ ریشه درست است.\",\n  \"sources\": [W_WIKT_BRADUS, W_WIKT_GURDUS],\n  \"ref_check\": [\n    {\"ref\": \"IEC:373\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 217 (running head '373'): 'gurdos, us (form of gurdos, us, q.v.) „sluggish, stupid, stiff, awkward“. Cf. WP I, 641 & II, 278 and gurndis. Per. gül „idiot“; Oss. qal „proud“ … Gk. bradüs „sluggish“; LW in Lat. bardus „sluggish, stupid“; Lat. gurdus „stupid“ (in LL: „blunt“) … Li. gurdùs; Latv. gurds „tired, faint“.' Page and content both exact.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 641 (WLD_Bd1_pages.txt leaf 649)\", \"stance\": \"supports\", \"note\": \"'Gr. βραδύς „langsam, träge“ (zu gurdus von Walter KZ. 11, 437, Froehde BB. 1, 331 … gestellt) könnte unter einer Gdbed. „wie ein Stock dastehend“ angeschlossen werden, wobei lat. gurdus für *gʷ(ʰ)rdus stünde' — the exact pairing of βραδύς with gurdus that Mann and Nourai take over, though WP flags Bechtel's rival *βραδός.\"},\n    {\"src\": \"POK\", \"where\": \"Pokorny IEW, gʷer-2 'heavy', p.476 (POK_full.txt line 39519)\", \"stance\": \"partial\", \"note\": \"'Lithuanian gurstu, gurti „lie down (from the winds)“, Latvian gurstu, gurt „tire“, gurds „fatigued, faint, languid“ (compare also βαρύς and gravis in the meaning „weighted, pressed down, faint, languid“)' — the Baltic members of this group are Pokorny's, under 'heavy'; he does not set up a separate *gʷr̥du- root and does not mention βραδύς here.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-2 'Heavy' [Pok. 2. gʷer- 476]\", \"stance\": \"partial\", \"note\": \"the appendix derives Latin brūtus 'heavy, unwieldy, dull, stupid' from a suffixed extended *gʷrə-u-to- of the same 'heavy' root — the same semantic path 'heavy' → 'dull, stupid' that this root box assumes, but Watkins lists no *gʷr̥du-.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction cited s.v. βραδύς\", \"stance\": \"supports\", \"note\": \"'From Proto-Indo-European *gʷr̥dus („slow“) … formally and semantically resembling *gʷreh₂- („heavy“)', with cognates Lithuanian gurdùs, Latvian gur̃ds, Latin gurdus.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Persian\", \"words\": \"gŭl «گول»\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"Persian گول 'fool, dupe; deceit' is a real and common word (Mo'in: '۱- (ص.) ابله، نادان. ۲- (اِ.) مکر، فریب', with the everyday collocations گول زدن 'to dupe' and گول خوردن 'to be duped' that the chart prints), but the derivation from this Indo-European root rests on Mann alone — 'Per. gül „idiot“' at IEC 373, with no argument and no Middle Iranian form — and it does not survive checking. First, no Iranian etymological authority endorses it: Horn's Grundriss and Hübschmann's Persische Studien have no entry for the word at all, Mo'in gives it without any origin tag (contrast the '[په.]' he attaches to inherited words), Wiktionary's Persian entry offers no etymology, and Dehkhoda canvasses Turkic and Sanskrit sources instead. Second, the vowel is wrong: Classical Persian and Dari have gōl with long ō (Tajik gül, Dari [ɡoːl]), which continues Middle Persian ō from Old Iranian *au or *ā-u; an Old Iranian *gʷr̥du- would have given *gurd-, and it did — that outcome is گرد gord of the previous chart, which cannot also be گول. Nourai's own transcription 'gŭl' with a breve papers over this. The word is best left unexplained rather than attached here.\",\n    \"derivation_fa\": \"«گول» در فارسی واژه‌ای رایج و واقعی است (معین: «۱- (ص.) ابله، نادان. ۲- (اِ.) مکر، فریب»، با ترکیب‌های روزمرهٔ «گول زدن» و «گول خوردن» که در نمودار آمده)، اما اشتقاق آن از این ریشهٔ هندواروپایی تنها بر مان استوار است — «Per. gül „idiot“» در IEC ص ۳۷۳، بی هیچ استدلال و بی هیچ صورت ایرانی میانه — و در بوتهٔ آزمون نمی‌ماند. نخست آنکه هیچ مرجع ریشه‌شناسی ایرانی آن را نمی‌پذیرد: هرن و هوبشمان اصلاً مدخلی برای این واژه ندارند، معین آن را بی هیچ نشانِ خاستگاه (مانند «[په.]») می‌آورد، ویکی‌واژه ریشه‌شناسی نمی‌دهد و دهخدا به‌جای آن از احتمال خاستگاه ترکی و سنسکریت سخن می‌گوید. دوم آنکه واکه نمی‌خواند: در فارسی کلاسیک و دری gōl با واو مجهولِ کشیده است (تاجیکی gül، دری [ɡoːl]) که دنبالهٔ ō فارسی میانه از *au یا *ā-u ایرانی باستان است؛ حال آنکه *gʷr̥du- ایرانی باستان به *gurd- می‌انجامید — و انجامیده است: همان «گرد» نمودار پیشین، که نمی‌تواند هم‌زمان «گول» هم باشد. آوانگاریِ «gŭl» با علامت کوتاهی در کتاب همین دشواری را می‌پوشاند. حکم: پژوهش امروزی این اشتقاق را نمی‌پذیرد و واژه را بی‌ریشه‌شناسیِ پذیرفته می‌داند.\",\n    \"sources\": [W_WIKT_GUL, W_ABADIS_GUL],\n    \"ref_check\": [\n      {\"ref\": \"IEC:373\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 217 (p.373): 'Per. gül „idiot“; Oss. qal „proud“: Dig. ǧāla („stupid“. Abaev); Arm. (Iran. LW?) kurt „eunuch“ …' — Mann does list it, so the citation is accurate; it is Mann's claim that fails.\"},\n      {\"ref\": \"MON:3470\", \"status\": \"partial\", \"note\": \"Mo'in's entry does exist and matches the gloss — MON_part2.txt (s.v. گول): '(ص.) ابله، احمق، نادان' — and abadis.ir's فرهنگ معین text reads '۱- (ص.) ابله، نادان. ۲- (اِ.) مکر، فریب. ۳- دلق.' But Mo'in gives NO origin tag, so he supports the word and its meaning, not the Indo-European derivation. The local Mo'in scan has no page numbers, so p.3470 itself could not be confirmed.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie (grep 'gul', 'Dummkopf', 'Tor')\", \"stance\": \"silent\", \"note\": \"no entry for گول among Horn's numbered New Persian etymologies.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (same greps)\", \"stance\": \"silent\", \"note\": \"no entry; neither of the two standard 19th-century New Persian etymological handbooks knows the word.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. گول\", \"stance\": \"partial\", \"note\": \"'۱- (ص.) ابله، نادان. ۲- (اِ.) مکر، فریب. ۳- دلق.' — no bracketed origin tag of any kind.\"},\n      {\"src\": \"Wiktionary/Dehkhoda\", \"where\": \"en.wiktionary s.v. گول; لغت‌نامهٔ دهخدا via abadis.ir\", \"stance\": \"contradicts\", \"note\": \"Wiktionary gives Classical Persian /ˈɡoːl/, Dari [ɡoːl], Tajik gül and no etymology at all; Dehkhoda's entry discusses possible Turkish and Sanskrit origins — nobody derives it from an IE *gʷr̥du-.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Latin\", \"words\": \"gurdus\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Latin gurdus 'dolt, blockhead; dull, thick' is genuine but marked as low and provincial from its first appearance: Quintilian, Inst. 1.5.57, says outright 'gurdus, quem pro stolido accipit vulgus, ex Hispania duxisse originem audivi' — the word came from Spain — and Aulus Gellius cites it from the mimographer Laberius. Ernout-Meillet accordingly print 'gurdus, -a, -um: lourd (sens propre et figuré) … Mot vulgaire (Laberius, cf. Gell.16,7,8), espagnol, d'après Quint.', and then reason exactly as the chart does but with a warning: 'Si le βρ- de gr. βραδύς „lent“ repose sur *gʷr-, ce qui n'est pas évident … on rapprocherait cet adjectif, en supposant un ancien *gʷr̥d-. Pour un mot populaire de ce genre, une étymologie indo-européenne ne s'impose du reste pas.' Walde-Pokorny I 641 is bolder and makes gurdus the head of the lemma, citing Schöll IF 31, 313 against the Spanish origin. Wiktionary's compromise, 'from Proto-Italic *gʷordos, possibly from PIE *gʷr̥dos', is where matters stand. So the word, the gloss and the possible root are right; whether it is an inherited Italic word or a Hispanic substrate borrowing is genuinely open, and the chart's flat arrow hides that.\",\n    \"derivation_fa\": \"لاتینی gurdus «کودن، کندذهن؛ سنگین» واژه‌ای واقعی است اما از همان نخستین گواهی‌ها «عامیانه و ولایتی» شمرده شده: کوینتیلیانوس (۱٬۵٬۵۷) صریح می‌گوید «شنیده‌ام gurdus که عوام آن را به‌جای stolidus به کار می‌برند از اسپانیا آمده است»، و آولوس گلیوس آن را از لابریوسِ میم‌نویس نقل می‌کند. ارنو و مه‌یه نیز می‌نویسند: «gurdus … واژه‌ای عامیانه (لابریوس)، اسپانیایی، بنا بر کوینتیلیانوس»، و سپس درست مانند نمودار استدلال می‌کنند اما با هشدار: «اگر βρ- در βραδύς یونانی بازماندهٔ *gʷr- باشد — که آشکار نیست — می‌توان این صفت را با فرضِ *gʷr̥d- کهن به آن نزدیک کرد. برای واژه‌ای عامیانه از این دست، ریشه‌شناسی هندواروپایی اصلاً ضروری نیست.» والده‑پوکورنی (ج۱ ص ۶۴۱) جسورتر است و gurdus را سرمدخل قرار می‌دهد و به استناد شول خاستگاه اسپانیایی را رد می‌کند. ویکی‌واژه راه میانه می‌رود: «از ایتالیک آغازین *gʷordos، شاید از هندواروپایی *gʷr̥dos». پس واژه و معنی و امکان ریشه درست است، اما اینکه ارثی است یا وامِ زیرلایهٔ اسپانیایی، هنوز باز است. حکم: با احتیاط پذیرفتنی است.\",\n    \"sources\": [W_WIKT_GURDUS],\n    \"ref_check\": [\n      {\"ref\": \"IEC:373\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 217 (p.373): 'Lat. gurdus „stupid“ (in LL: „blunt“)' listed directly under the root, as the chart draws it.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dictionnaire étymologique de la langue latine, s.v. gurdus (LAT.txt line 27146, leaf 526)\", \"stance\": \"partial\", \"note\": \"'gurdus, -a, -um: lourd … Mot vulgaire (Laberius, cf. Gell.16,7,8), espagnol, d'après Quint.1,5,57 … Si le βρ- de gr. βραδύς „lent“ repose sur gʷr- ce qui n'est pas évident … on rapprocherait cet adjectif, en supposant un ancien *gʷr̥d-. Pour un mot populaire de ce genre, une étymologie indo-européenne ne s'impose du reste pas.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 641 (leaf 649)\", \"stance\": \"supports\", \"note\": \"'Lat. gurdus „dumm, tölpelhaft, hebes, obtusus“ … s. Schöll IF. 31, 313 f., wo auch gegen die Annahme spanischer Herkunft' — WP makes it the head word of the root and argues against the Hispanic origin.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny IEW (POK_full.txt line 34086, under the ghreu- extensions)\", \"stance\": \"contradicts\", \"note\": \"'about Latin gurdus s. WH. I 627.' — Pokorny refuses to place it under any root of his own and hands it to Walde-Hofmann.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. gurdus\", \"stance\": \"partial\", \"note\": \"'From Proto-Italic *gʷordos („stubborn, heavy“), possibly from Proto-Indo-European *gʷr̥dos … The root's precise PIE origin remains uncertain,' quoting Quintilian on the Spanish origin.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Greek\", \"words\": \"bradus\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Ancient Greek βραδύς bradús 'slow, sluggish; slow-witted, dull; late' (Homer onward, e.g. Il. 10.226 and proverbially in Aesop's hare and tortoise) is the best-founded member of the whole root. Wiktionary reconstructs it directly as PIE *gʷr̥dus 'slow', with Lithuanian gurdùs 'slow', Latvian gur̃ds 'tired' and Latin gurdus as cognates, and notes the tie to *gʷreh₂- 'heavy'. The phonology is regular Greek: a labiovelar *gʷ becomes b before a consonant and before back vowels (as in *gʷm̥-yō > βαίνω, *gʷou- > βοῦς), and the syllabic *r̥ appears as ρα, giving *gʷr̥dus > βραδύς. Walde-Pokorny I 641 already made this equation ('Gr. βραδύς „langsam, träge“ (zu gurdus … gestellt) … wobei lat. gurdus für *gʷ(ʰ)rdus stünde'), while noting Bechtel's alternative *βραδός; the alternative has not prevailed. Nourai's transliteration 'bradus' and gloss 'sluggish' are Mann's, verbatim.\",\n    \"derivation_fa\": \"یونانی باستان βραδύς (bradús) «کند، سست؛ کندذهن؛ دیر» از هومر به بعد گواهی شده و استوارترین عضو این خانوادهٔ ریشه است. ویکی‌واژه آن را مستقیماً از هندواروپاییِ *gʷr̥dus «کند» بازسازی می‌کند و gurdùs لیتوانیایی، gur̃ds لتونیایی و gurdus لاتینی را هم‌ریشهٔ آن می‌شمارد و پیوندش را با *gʷerh₂- «سنگین» یادآور می‌شود. دگرگونی آوایی هم قاعده‌مندِ یونانی است: لبی‑کامیِ *gʷ پیش از همخوان و واکه‌های پسین به b بدل می‌شود (چنان‌که در βαίνω و βοῦς) و *r̥ هجایی به ρα می‌انجامد؛ پس *gʷr̥dus > βραδύς. والده‑پوکورنی (ج۱ ص ۶۴۱) پیش‌تر همین برابری را نهاده بود، هرچند به بازسازی رقیبِ بختل (*βραδός) نیز اشاره کرده که پذیرفته نشد. آوانویسی «bradus» و معنی «sluggish» در نمودار عیناً از مان است. حکم: ادعای نورایی درست است.\",\n    \"sources\": [W_WIKT_BRADUS],\n    \"ref_check\": [\n      {\"ref\": \"IEC:373\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 217 (p.373): 'Gk. bradüs „sluggish“; LW in Lat. bardus „sluggish, stupid“' — both the Greek box and the arrow to Latin bardus come from this line.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 641 (leaf 649)\", \"stance\": \"supports\", \"note\": \"'Gr. βραδύς „langsam, träge“ (zu gurdus von Walter KZ. 11, 437, Froehde BB. 1, 331; 3, 128 f.; 14, 105, Bersu Gutt. 152 gestellt) könnte … angeschlossen werden … doch erwägt Bechtel KZ. 46, 162 für βραδύς eine Gdf. *βραδός.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. βραδύς\", \"stance\": \"supports\", \"note\": \"'From Proto-Indo-European *gʷr̥dus („slow“), which shares formal and semantic resemblance to *gʷreh₂- („heavy“). Cognates: Lithuanian gurdùs („slow“), Latvian gur̃ds („tired“), Latin gurdus.'\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny IEW gʷer-2 p.476\", \"stance\": \"partial\", \"note\": \"carries the Baltic cognates ('Lithuanian gurstu, gurti', 'Latvian gurds „fatigued, faint, languid“') under 'heavy' but does not name βραδύς there.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Latin\", \"words\": \"bardus\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Latin bardus 'stupid, dull of apprehension' (to be kept apart from the homonym bardus 'Gaulish bard', which is Celtic *bardos from *gʷerH- 'to praise') is a rare, colloquial word, and the derivation the chart draws is the ancient one: Festus, in Paulus's epitome (P.F. 31,10), explains 'bardus stultus a tarditate ingenii appellatur … trahitur autem a Graeco, quod illi βραδύς dicunt' — 'it is drawn from the Greek, which they call bradus'. Ernout-Meillet accept the borrowing on that testimony: 'Rare; mot populaire, sans doute emprunté, comme l'indique Festus. „Les mots de ce sens sont souvent des emprunts; cf. all. idiot, kretin“ (Niedermann).' Mann, Nourai's source, likewise writes 'LW in Lat. bardus', i.e. a loanword from Greek — so the arrow Greek → Latin, rather than a direct descent from the root, is exactly right. The caution is that Wiktionary now calls the origin 'unknown, thought to be a loanword, perhaps from Etruscan', comparing bārō 'dunce, lout'; Festus's Greek etymology, though ancient and accepted by Ernout-Meillet, is not certain, and a shortened Greek ᾰ for the Greek stem vowel would be irregular.\",\n    \"derivation_fa\": \"لاتینی bardus «کودن، کندفهم» (که باید از هم‌آوایش bardus «شاعرِ گُل» جدا شود؛ آن یکی از سلتی *bardos و ریشهٔ *gʷerH- «ستودن» است) واژه‌ای کمیاب و عامیانه است، و اشتقاقی که نمودار می‌کشد همان اشتقاق باستانی است: فستوس در تلخیص پاولوس (P.F. 31,10) می‌نویسد «bardus stultus a tarditate ingenii appellatur … trahitur autem a Graeco, quod illi βραδύς dicunt» یعنی «از یونانی گرفته شده که آن را bradus می‌گویند». ارنو و مه‌یه بر پایهٔ همین گواهی وام‌گیری را می‌پذیرند: «کمیاب؛ واژه‌ای عامیانه، بی‌گمان وام‌واژه، چنان‌که فستوس می‌گوید». مان نیز که مأخذ نورایی است می‌نویسد «LW in Lat. bardus»، یعنی وام‌واژه از یونانی؛ پس پیکانِ یونانی ← لاتینی (به جای اشتقاق مستقیم از ریشه) درست کشیده شده است. احتیاط آنکه ویکی‌واژه امروز خاستگاه را «ناشناخته، احتمالاً وام‌واژه، شاید از اتروسکی» می‌داند و آن را با bārō می‌سنجد. حکم: با احتیاط پذیرفتنی است.\",\n    \"sources\": [W_WIKT_BARDUS],\n    \"ref_check\": [\n      {\"ref\": \"IEC:373\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 217 (p.373): 'Gk. bradüs „sluggish“; LW in Lat. bardus „sluggish, stupid“' — Mann marks it a loanword from Greek, which is exactly the arrow Nourai draws.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. bardus, -a, -um (LAT.txt line 6914, leaf 136 ≈ p.118)\", \"stance\": \"supports\", \"note\": \"'bardus, -a, -um: lent d'esprit, sot; „stultus a tarditate ingenii appellatur… trahitur autem a Graeco, quod illi βραδύς dicunt“, P.F.31,10. Rare; mot populaire, sans doute emprunté, comme l'indique Festus.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. bardus (Etymology 1)\", \"stance\": \"contradicts\", \"note\": \"'Unknown, thought to be a loanword, perhaps from Etruscan', comparing bārō 'dunce, lout'; the Greek source is not mentioned.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. bardus, -ī m. (line 6911)\", \"stance\": \"partial\", \"note\": \"'bardus, -ī m.: mot gaulois, cf. P.F.31,13, „gallice appellatur qui virorum fortium laudes canit“' — the homonym 'bard', which must not be confused with this node (Watkins puts BARD¹ under gʷerə-3 'to praise').\"}\n    ]\n   }\n  ]\n }\n ]\n}\n\nimport io\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-200.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build200.py"
}
```


### [2026-09-06T02:36:27.590Z] TOOL RESULT

```
ok
```


## [2026-09-06T02:36:31.555Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-200.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 200"
}
```


### [2026-09-06T02:36:33.318Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 3, 'confirmed': 5, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'plausible': 2, 'confirmed': 1}
ref checks: {'not_checked': 1, 'supports': 15, 'partial': 2}
books consulted: {'supports': 20, 'silent': 9, 'contradicts': 6, 'partial': 11} | by book: {'Wiktionary': 5, 'MON': 3, 'HRN': 3, 'WLD': 3, 'POK': 3, 'LAT': 3, 'KLN': 2, 'PLA': 2, 'LKT': 2, 'Etymonline': 2, 'FSD': 2, 'PHD': 2, 'HUB': 2, 'FVQ': 1, 'TAD': 1, 'DRAE': 1, 'DEV/PHN': 1, 'WEB': 1, 'SKT': 1, 'AHD': 1, 'BRT': 1, 'KNT': 1, 'IEC': 1, 'NYB': 1, 'Wiktionary/Dehkhoda': 1}
```


## [2026-09-06T02:37:04.054Z] AGENT

Page 200 (book p.170) verified. `verify_check.py 200` → 13/13 nodes, **0 PROBLEM lines**.

**Counts** — roots: 1 confirmed, 2 plausible. Nodes: 5 confirmed, 3 plausible, 4 disputed, 1 transcription_suspect. Ref checks: 15 supports, 2 partial, 1 not_checked (FVF:177 — Emam Shushtari exists only behind noorlib's browser viewer).

**transcription_suspect**
- *Gurdos "brave"* #1 Old Persian `Vtra, Vurt` — the printed page really shows "Vtra" (extraction is faithful; PNG saved to `refs/ocr/BOOK/200.png`). It is a metathesis misprint for **\*vṛta-**: Nourai's own HUB:91 (Hübschmann no. 899, p.91) reads "Phl. gurt steht für älteres \*vurt = ap. \*vṛta-", and Mo'in's Borhān footnote says the same. `error_in: book`.

**disputed**
- *Gŭrb/Kŭrb* #3 Portuguese `greba` — DRAE derives Spanish greba "del fr. ant. grève"; the arrow runs backwards. Klein 1966 (KLN:678) is the sole source and says exactly what the chart says.
- *Gŭrb/Kŭrb* #4 Old French `greve` — Etymonline: "of unknown origin", Klein's Arabic route relegated to a bracket; Lokotsch, Devic, Pihan, Skeat all silent.
- *Gurdos "brave"* #2 Armenian `kord` — actually "unploughed land"; Wiktionary/Martirosyan prefer PIE \*gʰordʰo- "enclosure". Mann's own line is "Arm. **cf.** kord … ?".
- *Gurdos "sluggish"* #1 Persian `gŭl` گول — Mann alone; Classical Persian gōl (long ō) cannot come from \*gʷr̥du- (that gives گرد gord, the previous chart). Horn, Hübschmann, Mo'in and Wiktionary give no etymology; Dehkhoda points to Turkic/Sanskrit.

**Also worth noting** (not extraction errors): the Arabic node's "j.r.b" is not a root — جورب is quadriliteral, the verb is denominal جَوْرَبَ/تَجَوْرَبَ. The root box *Gurdos "brave, proud"* is Mann-only: Walde-Pokorny I 641 carries it with a query and no Iranian material, Pokorny 1959 dropped it and reassigned the Slavic words to ghreu-d-; and the whole Persian branch under it (\*vṛta- → gurt → گرد) belongs to var- "to ward", per both of Nourai's own refs. AHD:577 in the English NOTE turns out to concern the homonym *greaves* "tallow cracklings" (ghrebh-²), not the armour.

**No extraction errors found** — the JSON matches the printed page at every point checked.

**Ref-page drift to record:** BQT:1786 — the گرد entry with Mo'in's footnote sits on printed p.1789 of the local vol.3 scan (pdf p.583), ~3 pages ahead of Nourai's citation; page read and saved to `refs/ocr/BQT/1786.png` + `1786.vision.txt`. 12 web pages archived via `fetch_source.py`.
