# Verification process log — verify-page-353


## [2026-09-07T18:17:52.311Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 353 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-353.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-353.json. Write /home/sfmqrb/git/rishe/data/verification/page-353.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 353` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:17:54.497Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:17:55.149Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:17:55.162Z] TOOL RESULT

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


## [2026-09-07T18:17:55.594Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-353.txt"
}
```


### [2026-09-07T18:17:55.614Z] TOOL RESULT

```
1	=== PDF page 353 (book page 323) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nebh, Nembh, Ombhro : Nebh: cloud; Nembh: moisture; Ombhro: rain  (refs POK:315)
4	#1 (parent #0) [Avestan] refs=POK:316 | nab, napta : humidity, moisture
5	  #2 (parent #1) [Pahlavi] refs=HRN:232; SNS:282 | namb : moisture
6	    #3 (parent #2) [Persian] refs=POK:316; BQT:2167; HRN:232 | nam «نم» : moisture
7	  #4 (parent #1) [Persian] refs=SNS:282; HRN:232; BQT:2155; POK:316 | naft «نفت ( نفط )» : oil, kerosene | NOTE: See BQT:2155 and Akkadian root "Nabatu:to shine" for another derivation.
8	#5 (parent #0) [Avestan] refs=BQT:2170; MON:4818 | nemadhka : salt
9	  #6 (parent #5) [Persian] refs=BQT:2170; MON:4818 | namak «نمک ( بانمک ، نمکین ، نمکدان )» : salt, charm
10	  #7 (parent #5) [Sogdian] refs=SOD:239 | nm`dk : salt
11	#8 (parent #0) [Avestan] refs=KLN:772; POK:316; SNS:11 | awrem, awra, awar : cloud | NOTE: BQT:79 derives these from Sanskrit "ab-bhra: water carrier". See roots "Ab 1" & "Bher 1"
12	  #9 (parent #8) [Pahlavi] refs=SNS:11 | awr, avr, abr : cloud ; abr-âmŭn : cloudy
13	    #10 (parent #9) [Persian] refs=POK:316; SNS:11 | abr «ابر» : cloud ; abrâmŭn «ابرآمون» : cloudy
14	#11 (parent #0) [Latin] refs=AHD | Neptunus : sea god
15	  #12 (parent #11) [French] refs=None | 
16	    #13 (parent #12) [Persian] refs=MON | Neptune «نپتون»
17	  #14 (parent #11) [English] refs=None | Neptune
18	#15 (parent #0) [Latin] refs=None | 
19	  #16 (parent #15) [English] refs=None | nebula, nimbus
20	
```


## [2026-09-07T18:17:59.365Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-353.json",
 "description": "Read source JSON page 353"
}
```


### [2026-09-07T18:17:59.406Z] TOOL RESULT

```
{
  "pdf_page": 353,
  "book_page": 323,
  "entries": [
    {
      "root": {
        "name": "Nebh, Nembh, Ombhro",
        "lang": "Indo-European",
        "refs": "POK:315",
        "gloss": "Nebh: cloud; Nembh: moisture; Ombhro: rain"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:316",
          "words": [
            {
              "translit": "nab, napta",
              "gloss": "humidity, moisture",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:232; SNS:282",
          "words": [
            {
              "translit": "namb",
              "gloss": "moisture",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:316; BQT:2167; HRN:232",
          "words": [
            {
              "translit": "nam",
              "gloss": "moisture",
              "script": "نم"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Persian",
          "refs": "SNS:282; HRN:232; BQT:2155; POK:316",
          "words": [
            {
              "translit": "naft",
              "gloss": "oil, kerosene",
              "script": "نفت ( نفط )"
            }
          ],
          "script_extra": null,
          "note": "See BQT:2155 and Akkadian root \"Nabatu:to shine\" for another derivation.",
          "quote": {
            "text": "باسپ و بنفت آتش اندر زدند - همه هندیان دست بر سر زدند",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:2170; MON:4818",
          "words": [
            {
              "translit": "nemadhka",
              "gloss": "salt",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:2170; MON:4818",
          "words": [
            {
              "translit": "namak",
              "gloss": "salt, charm",
              "script": "نمک ( بانمک ، نمکین ، نمکدان )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "Sogdian",
          "refs": "SOD:239",
          "words": [
            {
              "translit": "nm`dk",
              "gloss": "salt",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:772; POK:316; SNS:11",
          "words": [
            {
              "translit": "awrem, awra, awar",
              "gloss": "cloud",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "BQT:79 derives these from Sanskrit \"ab-bhra: water carrier\". See roots \"Ab 1\" & \"Bher 1\"",
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "SNS:11",
          "words": [
            {
              "translit": "awr, avr, abr",
              "gloss": "cloud",
              "script": null
            },
            {
              "translit": "abr-âmŭn",
              "gloss": "cloudy",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "POK:316; SNS:11",
          "words": [
            {
              "translit": "abr",
              "gloss": "cloud",
              "script": "ابر"
            },
            {
              "translit": "abrâmŭn",
              "gloss": "cloudy",
              "script": "ابرآمون"
            }
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
            {
              "translit": "Neptunus",
              "gloss": "sea god",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {
              "translit": "Neptune",
              "gloss": null,
              "script": "نپتون"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "Neptune",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "nebula, nimbus",
              "gloss": null,
              "script": null
            }
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


## [2026-09-07T18:18:00.995Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','SNS','BQT','MON','SOD','KLN','AHD','WLD','BRT','PHD','NYB','IEC','SYN','HUB','ARY','CHEUNG','FVQ','SKT','WEB','FSD','LKT']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-07T18:18:03.359Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries:
```


## [2026-09-07T18:18:37.166Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80 && echo \"---\" && python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['POK'].get('page_offset'))\nprint(d['POK'].get('lookup_hint'))\nprint(d['BQT'].get('page_offset'))\nprint(d['BQT'].get('lookup_hint'))\nprint(d['SNS'])\n\""
}
```


### [2026-09-07T18:18:38.411Z] TOOL RESULT

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
---
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
{'title': 'Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986', 'kind': 'archive_djvu', 'url': 'https://archive.org/details/VajnameShayest', 'lookup_hint': "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'], 'page_offset': '242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image', 'covers_etymology': True, 'notes': 'OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image.'}
```


## [2026-09-07T18:18:42.305Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: enebh\\|lemma: nebh\\|lemma: ombh\\|lemma: embh\" POK_full.txt"
}
```


### [2026-09-07T18:18:42.360Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:18:42.638Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==324||NR==325' POK_01.txt | head -120"
}
```


### [2026-09-07T18:18:44.134Z] TOOL RESULT

```
l  ansammeln'.
Letzteres  wird   dagegen  von  Pedersen  KG.  I  126  unwahrscheinlich  zii *air.  olc,  elc  ,malus'  gestellt,  s.  ^elk-  ,hungrig;  schlecht'. WP.  I  160.
em-,  ein.'-  ,nehmen';  ursprünglich  athematisches  Präsens.
Lat.  emöj  -ere,  eml  (lit.  emiau),  emptum  (=  lit.  imtas,  apr.  imtä  f.,  abg. j^t^)  ,nehmen  (nur  in  Kompositis),  kaufen',  osk.  pert-emest  ,perimet',  pert-^^ emust   ,peremerit',  per-emust    ,perceperit'    (zum    Perf.    *emed)j   pert-umum ,perimere'    (assil.    aus    ^pertemom)]    umbr.    emantu{r)    ,accipiantur'    emp ,emptus';  ^-
air.  em-  in  ar-fo-em-  ,nehmen,  empfangen',  Yerbaln.  airitiu  (:lat.  empti^  4 lit.  i§-imils  , Ausnahme'),  dl-em-  ,schützen',  usw.;  ^  ;|
lit.  imÄ,  Prät.  emiaü,   iihti   ,nehmen',   ostlit.    Präs.  jemiij   apr.    imt   ds.;" lett.  jemuj  jemu,  jemt   und  jemtj    daneben  fiemu,  nemu^  nemt   (wohl  durch
311
Kontamination  einer  Entsprechung  von  got.  niman  .nehmen^  entstanden, JJndzelin,  Lett.  Gr.  564);
aksl.  img  (^m<^,  vgl.  v^z-tmQ  .nehme  weg^.  usw.)  jeti  .nehmen'  (perfektiv), daneben  imperfektiv:  jemlg,  imati  ds..  und  als  .haben':  Zustandsverb imamby  im^jq,  imeti  {*,mä-,  *,me-)]
neben  idg.  em-  stehen  die  Reimwurzeln  jem-  und  nem-,  wohl  ursprüng- lich verschieden  und  nur  sekundär  gelegentlich  angeglichen;
hitt.  u-e-mi-ja-mi  (u-emijami??)  .ich  fasse,  finde'.  Pedersen  Hitt.  82i.  135.
WP.  I  1^4  f..  WH.  I  400  ff..  862;  Trautmann  103  f..  Meillet  Slave  commun^ 80.  203  f..  EM  2  300  f.
embhi-,  empi-  .Stechmücke.  Biene'?    Mit  tabuierendem  Wechsel  hhip?
Gr.  i^rrig,  -idog  .Stechmücke';
ahd.  imhi  (ältester  Beleg  impi  piano),  mhd.  imbe  (*embi-o-)  .Bienen- schwarm. Bienenstock',  erst  spät-mhd.  .Biene',  nhd.  Imme,  ablautend  ags. imhe  (*umhia)  .Bienenschwarm'.
WP.  I  125.  WH.  I  57.
j.  en  ;in'  ( :  *^ ;  slav.  auch  *on?);  eni,  n(e)i]  vielleicht  auch  ndbi  (Ausgang wie  epi^  obhi  usw.  vielleicht  mit  dem  Lok.  auf  -i  verwandt,  wenn nicht  gar  nach  ihm  geschaffen).
Ai.  in  dnlka-  n.  .Angesicht'  (=  3iV.  ainika-  ds.)  aus  *eni-oqu.'^
*ni-  in  ai.  ni-jd-  .eingeboren,  innewohnend,  beständig,  eigen',  av.  ni-zdnta- .eingeboren.  ingenuus'.  ai.  ni-tya-  .beständig,  eigen'  =  gall.  Nitio-hroges, VN  (Gegensatz  zu  Ällo-broges)  =  got.  nipjis  .Verwandter',  anord.  nidr .Verwandter',  ags.  niddas  PI.  .Männer.  Menschen',  auch  im  Verbalpräf. ar.  ni-  .hinein',  z.  B.  ai.  nigam-,  av.   nigam-   .in  einen  Zustand  gelangen';
arm.  i  (vor  Vokal  y  und  n-)  aus  *iri.  älter  *e7i  .in',  adnominal  m.  Lok. un
d  Akk.;
gr.  h,  dial.  iv  und  (poet.)  m,  hl  (so  hom.  stets  als  Postposition;  att. nur  mehr  IW  als  Prädikat  =  h^soxi)  .in',  adnominal  mit  Dat.  (=  Lok.). Gen.  und  in  einem  Teil  des  Gebietes  auch  noch  mit  Akk.  (, wohin'),  in letzterer  Geltung  anderwärts  nach  k^  zu  hg  (att.  dg]  danach  eXavo  wie ^?a>  erweitert,  antekons.  daraus  ^g);   tiefstufig  ä-  {n)  z.  B.  in  d-Xsyu)  usw.;
über  das  strittige  IW«,  evrs  .bis'  s.  Schwyzer  Gr.  Gr.  I  629 f.;
maked.  iv\
messap.  in]
alb.  inj  .bis'  (*ewi);
lat.  in,  ältest  en)  osk.  en,  umbr.  en-  {en-dendu  .intendito').  Postposition osk.  -en,  umbr.  -em,  -e,  adnom.  mit  Dat.  (=  Lok.).  Akk.  und  Gen.  (des Bereiches):
312
.  in-  ,in^  ,^adnominal  m.  Dat.  und  Akk.;  nasalierend)^  in-  (leniere  At eni,  vgl.  ingen  aus  urir.  ini-gena  ,Tochter^;   v^ermengt  mit  ind~  =  o-aii    >  -
air
aus  O/tC.        *Ä*-*     ''"'»VC''«'    CliUO      Lllil..     «'#l<«'-«JQ#€.L*      ^  J.  I^^XXÜV?!.      )        V  ^1  IXiCllg  li      JJJ.1  b      t-ZtCfc-    z^s    (y»»l|
ande-,  s.  Thumeysen  Grammar  531  f.,  Pedersen  KG.  I  45),  acjmr.  abret in  ,m^j  com.  bret.  en,  ncymr.  yn-j  gall.   essedon  (*en-sedon)  ^Streitwao-A  t embrekton  ^eingetauchter  Bissen^  (s.  unter  mereq-)-,  *
got.  in  ,\n',  adnom.  m.  Dat.,  Akk.,  Gen.;  ahd.  as.  ags.  in,  anord.  %  {^t adnom.  m.  Dat.  und  Akk.,  aus  *em  (über  Ableitungen  wie  got.  {7,' ,hinein^,  inna^  innana,  wohl  aus  *eni-n-,  s.  Brugmann  IF.  33,  304 f.)-
apr.  en  ,in',  adnom.  m.  Dat.  und  Akk.,  lett.  ie-  (nur  Präfix);  tiefstufi^ ^T}  in  lit.  f  (älter  und  heute  dial.  in,  int)  ,in^,  adnom.  m.  Lok.  und  Akk  •
aksl.  on-  {on-uUa  ,Schuhwerk^,  q-doh  ,Tal^),  schwundstuf,  v^n',  v^  in< adnom.  m.  Lok.  und  Akk. ;
toch.  AB  y-,  yn-j  B  in-  (nur  Präfix).
n-dhi:  ai.  ddhi  ,über,  auP,  apers.  adiy  ,in';  gall.  Intensivpräfix  Andi> (PN  Ände-roudus  ,der  sehr  rote^),  cymr.  an{ne)-  in  anne-l  ,Vorrichtunc^ =  air.  2«cZe-Z  {*ndhi-l-om),  cymr.  an-daw  ,lauschen^  (zu  taw  ,schweigend')* air.  ind-  (teils  aus  *indi-j  teils  aus  sekundärem  *indo-)  in  ind-reth  ,Eia- fall'  (*indi-reto-),  indnaide  (s.  weiter  unten),  usw.  Pedersen  (KG.  I  45)' will  auch  got.  und  ,bis  zu'  hierher  stellen;  s.  über  andere  Möglichkeiten  ' oben  S.  50  und  S.  181.  >^
(e)nero-  ,innerlich':  arm.  *nero-  ,das  Innere',  vorausgesetzt  von  ner- ,intra,  hinein',  nerJts  ,innen',  nerkoy  , drinnen';  vielleicht  gr.  bvsqol  als  ,die drinnen',  nämlich  in  der  Erde;  oder  besser  Hypostase  aus  o\  iy  egc^?
ni-,  nei'  ,nieder',  Komparativ  nitero-  ,nieder'  (im  Gegensatz  zu  ,oberer'):
ai.  ni,  av.  nl  ,nieder(wärts)',  ai.  nitardm  ,unterwärts',  av.  nitdma-  ,der
unterste';
arm.  ni-,  n-  ,nieder';  ;!fj
kelt.  *ne  aus  *nei  in  air.  ar-neut-saj  in-neut-sa  ,ich  erwarte',  (urir. *-ne-sedu)j  Yerbaln.  indn{a)ide  (*indo-ne-sodion)  und  in  ar-neigdet  ,sie beten'  (*ari-ne-gedont)]  vgl.  anders  Bergin  Eriu  10,  111;
ahd.  nid
```


## [2026-09-07T18:18:50.833Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nebh\\|nem-bh\\|ombhro\\|m̥bhro\\|enebh\" POK_01.txt | head -40"
}
```


### [2026-09-07T18:18:50.878Z] TOOL RESULT

```
4636:I.  {enehh-),  emhh-,  ombh-,  nobh-  (nebh-?),  rpbh-  ,NabeP,  mehrfach  mit i-Formantien. Ai.  ndbhya-  n.  ,Nabe^,  nähhi-  f.  , Nabel,  Nabe,  Verwandtschaft^,  näbhlla- n.  (unhelegt)  ,Schamgegend,  Nabelvertiefung';  av.  nahä-nazdista-  ,der  ver-  ' wandtschaftlich  nächststehende',  daneben  mit  ar.  ph:  av.  näfö,  npers.  näf ,Nabel';
4645:2.  (enebh-):  nebh-,  emhh',mhh-  (Kontaminationsform  nembh-);  z.T.  emb-, omb-  aus  embh-,  ombh-  , feucht,  Wasser',  daraus  ,Dampf,  Dunst, Nebel,  Wolke'.
4646:nebhos- :  ai.  ndbhas-  n.  ,Nebel,  Dunst,  Gewölk,  Luftraum,  Himmel', daneben  Wurzelflexion  im  dehnstuf.  f.  Plur.  ndbha/i(?)]  av.  nabah-  n.  PI. ,Luf träum,  Himmel';
4651:mit  i-Formans  (nebhelä):
4653:aber  air.  nel  m..  Gen.  niuil  ,Wolke,  Nebel'  nicht  aus  *nebhlo-,  sondern Lehnwort  aus  cjmr.  niwl,  nificl,  ncorn.  niul  ds.  (die  wiederum  nach  Lotli RC  20,  346  f.  Lw.  aus  spätlat.  *nibulus  für  nübilus);
4659:Meeres'  aus   *nebh-tu-s;    des  -p-  im   skyth.  FIN  Naparis,  apers.  Quell  ^  '' NdTtag  stammt  aus  iran.  apa-  ^Wasser,  Quelle'  (Brandenstein,  OLZ  1940 435  ff.).
```


## [2026-09-07T18:18:53.448Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4630,4700p' POK_01.txt"
}
```


### [2026-09-07T18:18:53.491Z] TOOL RESULT

```
lit.  jper-n-ai  ,im  vorigen  Jahre*,  lett.  p§rns  , vorjährig* ;  '""5^
russ.  dial.,  cech.  lo-ni  (^ol-ni)  , letztjährig*.
Specht  Dekl.  16  stellt  dazu  das  Pron.  en  in  gr.  evrj  , jener  (Tag  oder jenes  Jahr*?).
Schwyzer  Gr.  Gr.  I  424  mit  Anm.  5,  Feist  140  f.,  Specht  Dekl.  15  f.
en  ,siehe  da!^  '
Gr.  ^V,  ijrjVj  lat.  en  ,siehe  da!^ WP.  I  127,  WH.  I  403  f.
I.  {enehh-),  emhh-,  ombh-,  nobh-  (nebh-?),  rpbh-  ,NabeP,  mehrfach  mit i-Formantien. Ai.  ndbhya-  n.  ,Nabe^,  nähhi-  f.  , Nabel,  Nabe,  Verwandtschaft^,  näbhlla- n.  (unhelegt)  ,Schamgegend,  Nabelvertiefung';  av.  nahä-nazdista-  ,der  ver-  ' wandtschaftlich  nächststehende',  daneben  mit  ar.  ph:  av.  näfö,  npers.  näf ,Nabel';
315
oT.  dficpalög  (Nom.  PL  auch  o^LcpaUg)  ,Nabel,  Schildbuckel',  wohl  auch }j^i(pa'Asg  ;die  unreifen  Weinbeeren  oder  Oliven  oder  andere  Früchte'  (als nabelartig  vorgestülpte  Knöpfchen),  d^cpa-ug  ,der  Kelch  der  Eichel;
lat.  umbillcus  ,Nabel',  umhö,  -önis  , Schildbuckel';
air.  imhliu  ,Nabel'  {*emUlön-),  mir.  imlecan  ds.  (ein  Versuch  zur  Suffix- erklärung bei  Pedersen  KG.  I  495);
ahd.  nahüj  ags.  nafu^  aisl.  nof  ,Radnabe'  (auch  in  ahd.  naba-ger,  ags. nafu-gär,  aisl.  nafarr  ,grober  Bohrer'),  ahd.  nahalo,  ags.  nafela,  aisl.  naß ^Nabel';  dazu  nach  Liden  KZ.  61,  17  ahd.  amban,  amhon,  m.  (o-St.) ^Wanst',  as.  dmhön  ,abdomina',  Nom.  Akk.  PI.  eines  m.  ow-St.  (germ. ^amhan-,  idg.   *omhhon-)]
apr.  nahis  ,Nabe,  Nabel',  lett.  naba  ,Nabel'.
Vielleicht  hierher  ags.  umbor  ,kleines  Kind',  auch  der  ital.  VN  Umbri (*mbh-),  anderer  Ablaut  im  germ.  VN  Ämbrones  {*ombh-)  anders  Kretschmer Gl.  21,  116  f.
WP.  I  130,  EM  1122,   Specht  Dekl.  100.
2.  (enebh-):  nebh-,  emhh',mhh-  (Kontaminationsform  nembh-);  z.T.  emb-, omb-  aus  embh-,  ombh-  , feucht,  Wasser',  daraus  ,Dampf,  Dunst, Nebel,  Wolke'.
nebhos- :  ai.  ndbhas-  n.  ,Nebel,  Dunst,  Gewölk,  Luftraum,  Himmel', daneben  Wurzelflexion  im  dehnstuf.  f.  Plur.  ndbha/i(?)]  av.  nabah-  n.  PI. ,Luf träum,  Himmel';
gr.  v€g)og,  -ovg  n.  ,Wolke,  Nebel'  (Denom.  primärer  Form  ^vvvecpSL  ,es  um- zieht sich',  ^vwivocpe  ,es  ist  wolkig');
auch  (s.  u.  nem-  ,biegen')  air.  nem  (n.  es-St.),  nir.  neamh^  cymr.  com. nef  , Himmel';
abg.  neboy  -ese  n.  , Himmel',  zum  i-St.  umgebildet  in  lit.  debesis  f.  und  m. , Wolke'  (aber  alter  konson.  PL,  z.  B.  Gen.  PL  debesy,\  d  für  n  durch  Ein- fluß von  dangüs  , Himmel');
hitt.  ne-pi-is  (nebis)  n.  , Himmel'  Gen.  nebisas;
mit  i-Formans  (nebhelä):
gr.  vE(pilv  ,Wolke,  Nebel',  =  lat.  nebula  ,Dunst,  Nebel',  Wolke';
aber  air.  nel  m..  Gen.  niuil  ,Wolke,  Nebel'  nicht  aus  *nebhlo-,  sondern Lehnwort  aus  cjmr.  niwl,  nificl,  ncorn.  niul  ds.  (die  wiederum  nach  Lotli RC  20,  346  f.  Lw.  aus  spätlat.  *nibulus  für  nübilus);
ahd.  nebul  m.  ^Nebel',  as.  nebal  ,Nebel,  Dunkel',  ags.  nifol  ds.,  aisl.  nifl- heimr  u.  dgl.,  njöl  ,Dunkelheit,  Nacht'  (germ.  *neila-  und  *nibula-  aus -elo-j  aisl.  nifl-  aus  *mSi7a-);
unsicher  ai.  nabhanü-  m.,  nabhanu-  f.,  wahrscheinlich  ,Quelle';  av.  aiiixi-
316  ^
naptlm  asti  ,er  (befeuchtet  =)  besudelt  mit  Blut',  napta-  , feucht'  {*nah-ta-) npers.  neft  ,Najphtha' -^  ,^
vielleicht  hierher  lat.  Neptünus  ,Gott  der  Quellen  und  Flüsse,  dann  des  "f
Meeres'  aus   *nebh-tu-s;    des  -p-  im   skyth.  FIN  Naparis,  apers.  Quell  ^  '' NdTtag  stammt  aus  iran.  apa-  ^Wasser,  Quelle'  (Brandenstein,  OLZ  1940 435  ff.).
inbb-(rO'):  g
ai.  abhrd-  m.  ,trübes  Wetter,  Gewölk',  n.  ,Wolke,  Luftraum'  {*7ribhros)  "
av.  avrra-  n.  ,Wolke';  fern  bleibt  wegen  der  Bedeutung  gr.  dq)QÖg  ,Schaum'  ■
(Meillet  BSL  31,  51);  k
in  die  i-Dekl.  übergetreten  lat.  imher,  imbris  ,Regenguß'  =  osk.  Anafnss  -•,''
wohl  ,imbribus'.  .:
Hierher  auch  die  Flußnamen  gall.  *Ämbräj  mcymr.  Amir,  Amyr  sowie  -l nhd.  Amper  und  Ammer  (kelt.  *  Ambra),  Emmer  (kelt.  *  Ambria)]  dazu  auch
engl.  Amber -^    frz.  Ambre,   Ambrole]    span.  Ambron,  Ambror-,    ital.  Ambi-a  '
Ambria,   Ambro,  Ambrio   usw.,  letztere  sind  bestimmt   ven. -illyrisch;   vgl.  ^
ohne   formantisches  r  gall.   inter   ambes    ,inter    rivos',    ambe    ,rivo',   abrit.  "^'
Amboglanna   ,Ufer  des  Stromes',   sowie   arm.  amb    und   (mit   idg.  b)  amp  .^j
,AYolke'.  X
emb{h)-  :  omb{h)- :
ai.  ämbhas-  n.  ,Regenwasser';  ambu  n.  ,Wasser',  gr.  ^iißqoq  m.  ,Regen'
(zum  b  vgl.  oben  arm.  amp  und  Schwyzer  Gr.  Gr.  I  333) ;  hierher  auch  lak.  J;
di.iq^ä  , Geruch,  Hauch',  arkad.  si)Oi.i(pog  ,wohlriechend',  usw.  jj
nembh-:  ^^
pehl.  namb,  nam,  npers.  nem  , feucht,  Feuchtigkeit',  pehl.  nambltan  ,be-  W^
feuchten' ;  ■^^■_
lat.  nimbus  , Sturzregen,  Platzregen;  Sturmwolke,  Regenwolke'.  '5-
WP.  I  131,  WH.  I  681,    II  151  f.,   Specht  Dekl.  16f.  %
enek-,  nek-,   enk-,  nk-   , reichen,    erreichen,    erlangen'   und   (nur  Gr.  Bsl.)    . ,tragen';  onko-s  ,Tracht,  Anteil'.  ^
Ai.  aänötiy  av.  asnaoiti  (*nk-neu-)  ,gelangt  hin  zu  etwas,  erreicht',  Perf. ai.  andmsa  (idg.  *ön-onke  =  air.  ro-änaic) ;
ai.  ndäati,  av.  -nasaiti  (*nek-,  ursprüngl.  wohl  athematisch,  vgl.  2.  Sg. naksi  usw.),  ai.  ndksati  , erreicht,  erlangt',  Desid.  dnaksati  , sucht  zu  er- reichen, strebt  zu',  dmsah  m.  ,Anteil',  av.  qsa-  , Partei',  ai.  ndm§a-h  m. ,Erlangung',  -namiana-  (Kreuzung  von  ams-  und  nas-)]  -,-
arm.  liasi  ,bin  angekommen',  danach  hasanem  ,komme  zu  etwas,  komme     :.g. an';   nach  Pisani  Armen.  5  hierher  hunj-Jt,  linjo-c  , Ernte'  {^onkos)\  3:
gr.  (*enek-)  ÖL-rjvsytrjg  , durch  eine  Strecke  hindurchreichend  =  ununter-     j- brochen'  (dor.  und   att.  Sißveni^g  aus  *dia-Tjv£xrjg?,  anders  Boisacq   s.  v.),
317
^oö'TjVsy-rjg  ;bis  zu  den  Füßen  herabreichend^,  dovQ-r]vsyirjg  ,einen  Speerwurf ^yeit^  ==  ;S0  weit  man  mit  einem  geschleuderten  Speere  reicht'  oder  pass. vom  Speer  erreicht',  wie  y.evTQ-7]v8yirjg  ,vom  Stachel  (erreicht  =)  angetrieben'; Pass.  Aor.  '^vsx^rjv  ,wurde  getragen',  Perf.  xar-rjvoyia  Hes.,  h-rjvoxa  (iv- ist  darin  wohl  Reduplikation;  ebenso  im  Med.  iv-rjvsy(.iaL,  zu  dem  sich als   3.  Sg.  iv-rjveyycTai   statt  Hv-rjvs'/iTai  gesellte,   nach   dem  Aor.  iveyy,eTv)]
*e7ik-   im   red.   Aor.   iv-6yy.-eTv  (*enk-enlc-)  , tragen';  s.  unten  hitt.  ÄenÄ:zi;
*onJc-  in  iJyxog  , Tracht,  Last'  (=  ai.  dnisa-h,  bsl.  *nasa-) ;
^vsiv.a  dagegen  zur  Wz.  *seik-  ,langen',  s.  dort  und  Boisacq  251  f.  m. Lit.j  durch  Kreuzung  mit  ihm  wurde  'irjveyv.ov  zu  ^jvsyaa,  ijveLy-Aa]
lat.  nactus  (und  nanctus)  sum,  nancisci  (arch.  auch  nanciö,  -Ire)  , er- langen' (-a- =  ^,  so  daß  wac^ws  =  germ.  *nuh-ta-',  die  Nasalierung  des Präs.  ist  wohl  sekundär  (Kuiper  Nasalpräs.  163) ;
air.  ro-icc  , erreicht',  do-icc  ,kommt',  air-icc-  , finden',  con-icc-  ,können' usw.;  wohl  in  die  themat.  Konjugation  übergeführtes  dehnstufiges  *enk-ti, woraus  *lnk-,  *inc-,  icc--,  Verbalnomina  rlchtUj  tichtWj  s-Konj.  -i  aus  *enkst] Perf.  ro-änaic  (s.  oben);  s-Prät.  du-uicc  {^'onk-i-s-t)  ,hat  gebracht'  usw. s.  unten  S.  347 ;  Schwundstufe  nk-  in  cymr.  di-anc  ,entfliehen',  cyfranc (^kom-ro-anko-)  =  air.  comracc  »Zusammentreffen';  nach  Loth  RC  40,  353 ir.  oc^  cymr.  wnc,  long  ,bei'  aus  *onko-  ,Nachbarschaft'?;  dazu  mcymr. ech-wng  , Vertreibung';  nach  Vendryes  (MSL  13,  394)  hierher  auch  der gall.  VN  *Selva-nectes  (latinis.  Silvanectes)  ,qui  ont  obtenu  propriete',  zu air.  selb  , Besitz^;
got.  ganah  (Prät.-Präs.)  ,es  reicht  =  genügt',  Inf.  ganaühan  (über  germ. rmh-  s.  oben),  ahd.  ginah,  ags.  geneah  ds. ;  got.  *hinauhan  , erlaubt  sein', got.  ganaüha  m.,  ahd.  (usw.)  ginuht  f.  , Genüge';  ö-stufig:  got.  ganöhs ,genug,  viel',  ags.  genöh,  genüg,  anord.  {g)nögr,  ahd.  ginuog  ,genug'  usw.; e-stufig,  wie  es  scheint,  anord.  nä  ^nahekommen,  erreichen,  bekommen', ags.  (ge)ncegan  ,sich  jemandem  nähern,  anreden,  angreifen';
über  got.  neh  Adv.  ,nahe,  nahe  an',  neJva  ds.,  as.  näh,  ags.  neah  ,nah', Präp.  ,nahebei',  ahd.  näh  Adj.  ,nahe',  Adv.-Präp.  ,nahe',  nhd.  nach  s.  oben S.  40;  man  stellt  auch  alb.  nes,  nes-er  , Morgen'  (*nök-)  dazu,  ebenso  lett. näku,  näki  ,kommen',  lit.  pranökti  , überholen',  nökti  , reifen',  die  aber  idg. ä  voraussetzen ;  vgl.  Mühlenbach-Endzelin,  Lett.-D.  Wb.  II  698 ;
über  das  von  Jokl  SBWienAk.  168,  I  36  mit  pranökti  verglichene  alb. ke-nak  ,befriedigen,  vergnügen'  s.  denselben  lA.  35,  36;
bsl.  *nesö  ,trage'  (vgl.  ai.  naiati)  in:
Vit.  nesü,  nesiaü,  nesti]  IqU,  nesu,  ne§u,  nest]  dazu  Iterativum  lett.  «esa^, lit.  nesiai  =  lett.  nesi  m.  PL  ,Tracht  Wasser',  lit.  na§tä,  lett.  nasta  f. ,Last' ;
aksl.  nesg,  nesti,  Iterativum  nositi  usw.,
*
H
```


## [2026-09-07T18:19:10.569Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 253 254; do echo \"=== NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-07T18:19:11.729Z] TOOL RESULT

```
=== NR=253
MI
— 231 -
WSO, niiad 'Geschlecht, Abstammung, Adel' *), nizade 'von
adeliger Abstammung 2).
aw. ^nizäti", vergl. skr. Jati-.
1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
niedrig*.
ap. *ni -h l/yaw- niederschlagen*, also etwa ein ap.
*/ii/a«/M- 'niederschlagbar voraussetzend, vergl. indische
Bildungen auf -tti- bei B. Lind n er, Altindische Nomi-
nalbildung, 8 54, Ib (S. 80).
Unsicher.
1032. niSästen 'sich setzen lassen', Praos. uisän-em,
nisänden.
Causativ zu nisesten (No. 1083); phlv. n(i)sastan (vd.
16 (17) ÖL), n(i)sanet (M6n.).
1033. nisesten 'sitzen*, Praes. nisln-em,
g. senastmün 'sich setzen'.
ap. m + [/^had-, Caus. niyasädayam; aw. ni -\-
l^had-, mshiSaiti 'sitzen, sich setzen', Caus. niSädayöis;
phlv. n(i)sastan, n(i)$fnet (vd. 16 (1)) ; ai. ni + [/^sad-,
stdati,
kurd. LW. nisin 'sich setzen'; bei. nindag^ n. nin-
day^ Causat. nistainay (264).
Der Nasal der Wurzelsilbe in np. nism-em ist auf-
fallig (er findet sich auch in bei. nindag, ksl. sedq
(sösti), apr. midMs, ist also wohl alt), ebenso das
lange f. Vergl. Bartholomae, Studien II, 97, 98,
der eine Erklärung für die iranischen Formen allein
versucht. Np. nisäxten 'sich setzen lassen* (z. B. Vis
und Rämin, Seite 24 Vers 7) ist eine Analogiebildung.
1034. niseb Unteres; unten'.
aw. *mxsvaepa-, vergl. x^^^W^' (No. 799) ; phlv.
n(i)Sep (AV.), n(i)sepitan^ n(i)sepmd 'sie gehen unter*
(Salemaifn, Mel. asiat. IX, 238), vergl. v(i)seft, 'Ver-
lorenes Sprachgut*, No. 229.
>) VergL Rückert, ZDMa. 10, 138.
2J Vergl. besonders äähn. II, 765 Vers 11 ; auch II, 611 Vers 1601.
=== NR=254
— 232 -
1034*>*» niseni *Nest* (Sahn. I, 137 Vers 146), nisemen i).
Doch wohl auch zu np. nisesten (No. 1033), wenn-
schon die Erklärung der Formen schwierig ist. Ge-
hört dazu etwa auch äsyäne *Nest' (No. 35)?
skr. LW. niglmana" (PärasTpr. ed. Weber, No. 433).
1035. neft ^Naphta .
aw. napta- *feucht' ; ai. l/^nabh-, ndbhatB 'spalten,
platzen; hervorquellen*.
LW. ar. naft; kurd. nefte; bei. n. napt 'Donnerkeil,
Blitzstrahl, Kanone' (No. 177) gehört aber wohl nicht
hierher.
Arische Doppelformen naph- und nabh-, vergl.
Hörn, KZ. 32, 584 No. 16.
1036. fUgasten malen', Praes. nigär-em, nigarld^n^ nigär
*Bild*, nigdristdn (Häfiz 16, 5).
Causativum zu nigertdeny nigeristen (No. 1038),
wörtlich *ansehbar, sichtbar machen'; phlv. '^n(i)kar
etc., vergl. arm. LW, nkar 'Bild', nkaren, tikarem,
1037. nigäh 'Anblick, Aufmerksamkeit*.
aw. *nikasa- (vergl. ägäh, No. 40); phlv. n(i)käs.
LW. kurd. nekä; bei. nikäh (263).
Kä§. V. hat sogar als Verbum [/^kos- *sehen' noch
erhalten, nämlich in Praes. bitkesün, Impt. bikes, Inf.
bikasdn u. s. w. (s. v. nigäh kerden).
1038. nigertden 'betrachten', nigeristen.
Käs. Q. vergl. angastän^ batangastdn (s. v. nigc^
kerden),
Wohl zu derselben Wurzel wie aw. hankäray§mi,
siehe np. engärden (No. 123); phlv. n(i)karitan,
n(i)kar(i)sn,
kurd. nirin, nihirin 'betrachten.
1039. nem 'feucht; Feuchtigkeit'.
aw. napta- 'feucht' {[/^nab-, namb- d. i. nabh-,
nambh'); phlv. namb^ nam.
^)In SpiegeTs Chrestomathie, S. 97, 5, durch einen Vers
Väqänl's belegt.
```


## [2026-09-07T18:19:17.171Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"namb\\|nam-b\\|naft\\|napt\" SNS_pages.txt | head -20; echo \"=== awr\"; grep -n \"awr\\b\\|abr\\|awr-\\|āwr\" SNS_pages.txt | head -20"
}
```


### [2026-09-07T18:19:17.230Z] TOOL RESULT

```
11252:                                                                                                       ^^j f* v*i namb
11253:              Vo-» ^                                              nambh-,
11258:invinahtar:                        .^Irf-.vinShtarsV^-*                             nabh-         CHSf^Shah tj\ napta-
14894:                                                               prayah 126/7                 nambh-nabh- 282/3
15206: napta- 282/3
=== awr
1149:                                                                                                                                               :     i**    abr-amOn                   t   ^-JS^ j       .aj^T^Uji. U *** .a-i^JT^l^L L«**
1319:1o                                          is* '*U«0*V : abrninftiu
7442:                                                                   t»m*> _!>«*                     •fiJbgaljJ,!^^ rj^wr ,5^. :stabra2f/stavrak:
15844:                                                         spandmad gah 176/14               stabrajr/stavrak 178
16501:abr/avr 11/7                    afzOnlgiha 18/4
16503:abramOn 11/10                   afzQn 17/19
```


## [2026-09-07T18:19:21.670Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11245,11262p' SNS_pages.txt; echo \"=== page 11 area\"; sed -n '1140,1160p' SNS_pages.txt"
}
```


### [2026-09-07T18:19:21.728Z] TOOL RESULT

```
                                                                                                                                                                    TAT

O-utl .^J.jU.^^.ojlp: vinahtarih:
                                              -oW<^"                                        •V/A^ .A^JoUi.^^..
                                                                                                                              niraayend:                       -*^-€l


                                                                                                       ^^j f* v*i namb
              Vo-» ^                                              nambh-,
                                                                                                               •      '       '         :                  :   _A>$   i



invinahtar:                        .^Irf-.vinShtarsV^-*                             nabh-         CHSf^Shah tj\ napta-
                                                                                              :
                                                                                                                                                        :      ^
                                                                                                      •6/\osS .%x/X<S
                                                                                                                                      {GNPE. 232)
=== page 11 area

                                            .j/ti      -^ .c^yl*                havist IV""*'
                                                                                    :



                           ^ \*/a^ {AiWb
                      -&/)•>                                       .     1806) haviito- I
                 •   k/\o^ o^Jk o'^     'havistan         :                                     :       WlO'*'
                                                                                                                                               :     i**    abr-amOn                   t   ^-JS^ j       .aj^T^Uji. U *** .a-i^JT^l^L L«**
                                                                                                                                                   lJ

                                                      .^jjj J**               -   U .*ili;xanay                             i    ij
!•
     /r^ .ao-fa-ti-TA-lA-W/T ^(GNPE. 103 . ) j/khan-j                                                               1
                                                                                                                                **•

                                                •X/\Y^ .fi-T/IT^                            •   ?/!»** -r«-\i
                                                                                                                                                           h'rayn         :^k {AiWb                  .    1809)     hamina-        ,   hami: fc»
                                                                  •    0* T   :    ahSn/ahan                                          »»                     W/1A       --S       (ij6.y~»J          hamln :L {Mir. Man.                        I.       39)
        :    \****>     I*      tjax"       .^^^j/i Uiftfc.l56)ayagh-                                                       i   I*-
```


## [2026-09-07T18:19:28.801Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i \"BQT\\|MON\\|SOD\"; echo \"--- ocr dirs\"; ls ocr 2>/dev/null | head"
}
```


### [2026-09-07T18:19:28.858Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
MON_part1.txt
MON_part2.txt
SOD_pages.txt
SOD.txt
--- ocr dirs
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
```


## [2026-09-07T18:19:31.909Z] TOOL CALL #14: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT | head -50; echo \"---SOD\"; ls data/verification/sources/refs/ocr/SOD | head"
}
```


### [2026-09-07T18:19:31.954Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1237.png
1237.txt
1237.vision.txt
1261.png
1261.txt
1266.png
1266.txt
1266.vision.txt
1267.png
1267.txt
1267.vision.txt
1272.png
1272.txt
1275.png
1275.txt
1279.png
1279.txt
1280.png
1280.txt
1280.vision.txt
1294.png
1294.txt
1294.vision.txt
1296.png
1296.txt
1296.vision.txt
1297.png
1297.txt
1298.png
1298.txt
1299.png
---SOD
70.vision.txt
```


## [2026-09-07T18:19:32.376Z] TOOL CALL #15: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-07T18:19:32.418Z] TOOL RESULT

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
```


## [2026-09-07T18:19:35.771Z] TOOL CALL #16: Bash

```json
{
 "command": "for p in 2155 2167 2170 79; do echo \"############ BQT:$p\"; timeout 600 python3 tools/ref_page.py BQT:$p --image 2>&1 | tail -40; done",
 "timeout": 600000
}
```


### [2026-09-07T18:19:46.695Z] TOOL RESULT

```
############ BQT:2155
REF: BQT:2155  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 238  OCR-lang: fas

<وو۱و-< نت
فام است که تیره رنگه و سیاه فام باشد - ودر ففت ۱ « بروزن هفت » روغنی باش د که
عریی سیم قلب ناسره را کوبند . درولایت عپروان پیدا میشود وآن سیاه وسفیدعن
۹ - دراوستا -88068 ( تره نمناك )., هندی باستان -82010 , 28080216 (شکاتن,
تر کیدن ) « اسشق ۱۰۳۵ *. هوبشمان کوید : اسم مفعول ازريشة 82018 در اوستا -088008
آمده , که نظایر متعدد دارد . اسم مفمول مشتوم به 12- :338012 است . قن : - 02812 >
ساسکریت -۳20412 وغیره . دلیلی فیست کهآ نرا از ربشهٌ 8203 بدانیم . آیا این کل ه هند
و ژُرمانی ( هندواروپایی ) است ؟ ارمنی *32۷1 ( قیر » لفت ) , بونانی 240121172 « هوبشمان
۵ , دراوراق مانوی ( پهلوی ) 810 ( قیر ۰ افت ) ۸۸14416 0۲ 191] ۸ ,17688108)
۰( .0 را ,12 ,8505 و...86۲9188! لانینی 31801018 . از وی دیگرمژلف معجمیات
عريية - سامیه نوسد ( ص۹-۲۰۸) : « لفط : اصل‌آن کدی است بسورت فملی « نباو» ( بفتح
اول و دوم وضم چهارم ) بمعنی : درخشید . روشن کرد » نابید » طلوع کرد » آغا ز کرد » و ازآن
«بطو » ( بکسراول وضم سوم )آمده بمعنی نوره و « لمبطو» ( بفتح اول وسوم وضم‌چهارم) بممنی
روشنایی » درخشند کی و « نباطش * ( بفتح اول وکسر چهارم ) بمعنی با درخشند کی » آشکارا :
و ازآنست كلمهٌ « تبطو» ( بفتح اول و ضم سوم ) بمعنی لفط » وشکی لبست که سبب اطلاق این
اسم برآن آست که یکی از خواس « لفط » نبوط آست بعنی خروج ازجوف زمین وچون آلرا
بوزانند درخشد کی گیرد » پس آلرا بمعنی « تابط , خارج , لامع . مشرق »گرفتند . بنابررین
سربانی . لفت اصلی این کلمه بیست بلکه اکدی اصل آنت و ازین بنمام ژبانهای دیگر رفته »
وغرابتی هم ندارد؛ زبرا عراق - با بلاد اآکد. بابل ؛آشور - از قدیمترین ازمنه هنبع لفط بود ۰
چنانکه اکنون‌هم است؛ ونقط فقط درعصر ماکشف شده بلکه وجود آن همواره درعراق شناخته
بوده است » زیر| بصورت درباچه هابی برمطح زمین نبعان دارد و درشب میدرخشد وئورآن از دور
پیداست؛ وفعل « لفط » درعربی بمعنی پراگنده شد وخارج شده آمده ومبدل آن « لبط > است
بمعنی بیرون‌آمد آب وخارج شد .» :
باسپ و بنفت آش آندر زدنهت همه هندیان دست برسر زدند.
فردوسی‌طوسی « شاهنامةٌ بخ ج۷اص۱۸۶۲ ۰
از هلیله قبضش شد اطلاق رفت آب آتشرع را مدد شد همچو لفت.
مولوی بلخی‌رومی « مثنوی چاپ لیکلسن دفتر اوّل ص ۵ ).
بقیه ازحاشيهٌ صفحهٌ ۷۱۵۶
آورد للی بجوال و به‌بایه از ساحل دربا چو حمالان بکتّف بار(سار.دهخدا) .
3 منوچهری دامقانی ص ۱۶۸۶ » و رك : جپالگیری .
اما این کلمه عربی است « فاة بالفتح» چیز بلایه وردی و بقیه و رانده و دور کرده, فوة بالفتح,
ولفاه کسحاب , ولفاية كسحابة ویضم ولفاوة كثشمامة مثله .» « منتهی‌الارب » - بمعنی‌لبهره وناسره :
این که زحمت کم کنم نوعی ز تشوبر است از آ نك .|
شدهای بی نفایه اسست این و ناقد بی یر .
انوری اییوردی ۶ جهانگیری ».
میاد دين هدی را چئو تایه آمام ته نیز صدر زمالرا چئو لبهره ندریم.
سوزلی سمرقندی «چهانگیری».

############ BQT:2167
REF: BQT:2167  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 250  OCR-lang: fas

بیان بیستم
در نون با میم مشتّم‌ل برسی و پنج لغت و کنایت

نم ۱ < بفتح اول وسکون ثانی؛معروف | هم هست . 1
است که رطوبت اندك باشد - و بمعنی طراوت‌هم مار ۴ - بر وزن سوار, بممنی ایما
آمده است. و آشاره باشد ؛ ونماران بمعنی آشارات » بواسطةٌ

نماد - بروزن سواد » بممتی‌نمود باشد | آنکه جمع نمار است .
که ماضی نمودن است پعنی ظاهر شد و نمایان نماز ۴ - بنتح اول و ثابی بالف کشیده
کردید ۲ - وبمعنی‌فاعل هم‌آمده است که ظاهر | و بزای نقطه‌دار زده , بمعنی بندکی و اطاعت
کننده باشد -وبمعنی‌ظاهر کردونمایان گردانید۳ | وادای طامت (۱) وسجود «پرستش و خدمتگاری

(۱) چش : - وادای طامت .

۱۹ - فارسی 882 از 88۳۵8 88008-۳۳۵ 6 مانند 1۳273 از پارسی باستان .
-۵7۵ ۳ -088ط362 آمده , اففای ۵0۳4 ۰ 20۳۵4 « حوبشمان ۱۰۳۹ » پپلوی
۰38۳ 0 » بلوچی 88720 ( شبنم » مه) « اسشق ۰۶۱۶۳۹ کردی 26۵1 ۰ 161۷
( مرطوب ) « ژابا ص 4۲۳ .۰

زروی تو بچه معنی‌همی پروی دگل؟ زچشم من بچه معنی‌همی ببارد 0؟

معزی لیشاپوری ص 4۹۷ ۰

۴ #نمود : ‎٩‏ نماد » یعنی نمود . عنصری ( بلخی) کوید :

زان گاید فقم که بگشادی زان نماید ترا که بنمادی .»

« لغت فری ص ۱۱۶ ۰

۴ - از دساتیر ۸« فرهنگه دساتیر ص ۷۷۰ > . آقای حکمت در « پارسی انغز . تهران
۳۹۰ ص ۱۸۶ این کلمه را مسحف « نماد » (ه.م.) پنداشته اند .

۴ - پپلوی ۵۳۵0 ۰ ازایرانی باستان -38772 ( خم شدن , تعظیم کردن ) «بارتولمه
۹۱ لیب رکه اس ۱۵۶ > ورك : هوبشمان۱۶۸۰ ؛ قِس : اوستابی -361221 ( دعا ).هندی
باستان -360389 ۰ پازند 88۳220 ۰ افمای زط370۵ ۰ بلوچی 82۳35 ۰ 82۷855 ۰
رك : اسشق ۱۶۶۰ کردی [8ر8 . 851 ( ساز) , زازا 862 « ابا 4۷۶ *:اورامانی
20۳2 «که . اورامان ۱۲۵ ؛ گیلکی 3877182 - مجازاً عبادت مخصوس ملمانان ۰

############ BQT:2170
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2170.png
REF: BQT:2170  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 253  OCR-lang: fas

تمعك ۱
سس ی
۱ تشاک ۱ - بر وزن سرعك » شیربرا نمگزی - بنتح اول و ائی و سکون
گونند که آزیتان کوسفند و کاو بردوغ وماست | کاف وزای نقطه‌دار بتحتانی دشیده , حلوائی‌است
بدوشند -وبمعنی‌قیماق شیرخام وهسکه‌وکره(۱) | که آنرا از آرد و شکر با عل و دوشاب پزند
هم آمده است. ومغز گردکان وبادام و پسته وامثال آن‌داخل کنند
نمشیدن - بروزن فهمیدن . بمعنیکام وفند سوده ومشك و کلاب‌برآن پاشند وخورند؛
بافتن و بمراد رسیدن باشد 4 وبسی گوبند میوه های خشك شده داخل کنند.
نمك انگیزیدن - کنابه از کریه نمکسود ۴ - هرجیزراکویندکه بر
کردن باشد . آن مك پاشیده باشند عموماً - و گوشت قدید
۰ 7( برچگر داشتن «کنابه‌از ۰ وکیاب گوشت قدید راگویند خضوصاً .
برمحنت وعذاب پرعذاب کشیدن باشد . نمکینه بفتح اول و ثانی و کاف
نمکدان ؟ ب نان ا: دی« | بتختانی کشیده وئون مفتوح » دوغ و ماستی‌باشد
3 "- کنایه از دهان مصشوق | که درآن‌مك وزبره و کشنیز کوفته ربخته‌باشند
ومحبوب است . ۱ وعربان ملحیه خوانند .
نمکدان شکستن -کنبه از حق نمنك * « بضم اول وئانی(۲) وسکون
لاشناسی کردن و بیوفائی ورزیدن باشد . بون(۳) وکاف» چیزیست سرخ وشبیه بمرجان.
از شور وغوغا وفربادکردن باشد . رسیده و دال ابجد بالف کشیده و بای قرشت
(۱) چش :-کره . (۷) چش:- وئانی. (۳) خم۱:- نون .
۸-۱ منك » بفتحتین مکه و بعی گفته‌اند دمشك بکسرتین کفی و قیماغی که بالای
شیر خام جمم شود.؟ ‌- بعصی بمعنی گورماست کفته‌اند :
درجهان بمحاق فوتی چون معك وفندلیست مشنو این ازمن که عمری درپی آن بوده‌ام.
بحاق اطعمه « چاپ استالبول ص ۰.۷۹
۴ - از : مك +دان ( پوند ظرف ) » آلتی که درآن مك‌کنند .
۳ - از : مك + سود ( سوده «* سائیده ) » معرب آن هم سکود « دزی ج ۷ ص
تخمدمها ۴ - از : مك اینه (سبت). 8 - مسحف «متك» (ه.م.)
۹ - پهلوی ۳( اسشق 7۲۳ از : لمو (نمودن) + دار ( ۳ 87۲ ]آپوند
آسم فاعلی ومفمولی ( رك : دارمستش. تتبعات ۱ ص ۰.۲۸۳
نمك - بفتح اول‌ودوم » پهلوی887728 «ناوادیاس ۶۱۹۳ ۰ ازاوستا 7237321068
هرچند معنی فرق‌کند. ,176 ,8505 ب... ۳67512 ۸110016 0۶ 1191 ۸ و وصندده۲)
(85. 0 را - دراوستا و ود! ازهنمك» (ملح) اسمی لیست ولمك بدین معنی متأخر است. درازد
هندوان اس آسم‌این جوهر ازم ورطوبت مشتق است 2 پورداود . گاتها چاپ ۱ ص46 ؛ مادُسختی
بطعم شور ء قابل نرم شدن و حل شدن در مایمات ۰ که آنرا در خوراکها بکار برند » ملح :
«نوشیروان عادل را درشکار گاه صیدی کباب کردند ونمك نبود » غلامی بروستا رفت تا نمثحاسل
کند .» «کلستان صس 4۱ >.
(برهان قاطع ۳۷۴)

############ BQT:79
no scan of BQT covers printed page 79 (see 'scans' in refs_online.json)
```


## [2026-09-07T18:20:09.797Z] TOOL CALL #17: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2170.png"
}
```


### [2026-09-07T18:20:10.528Z] TOOL RESULT

```

```


## [2026-09-07T18:20:10.525Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T18:20:43.359Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && cat > ocr/BQT/2170.vision.txt <<'EOF'\n[BQT p.2170 (Borhan-e Qate', ed. Mo'in, vol. 4), read from the page image — headword نمك and neighbours; footnote 5 is Mo'in's etymological note on نمك]\n\nFootnote ۵:\n«۵ ـ نمك ـ بفتح اول و دوم، پهلوی namak «ناوادیاس ۱۶۳»، از اوستا nəmadhka‑\nهرچند معنی فرق کند. (Henning, A list of Middle Persian ..., BSOS, IX, I, p. 85)\nـ در اوستا و ودا از «نمك» (ملح) اسمی نیست و نمك بدین معنی متأخر است. در نزد\nهندوان هم اسم این جوهر از «نم» و رطوبت مشتق است. «پورداود، گاتها چاپ ۱ ص ۴۵»؛\nماده‌سختی بطعم شور، قابل نرم شدن و حل شدن در مایعات، که آنرا در خوراکها بکار برند، ملح:\n«نوشیروان عادل را در شکارگاه صیدی کباب کردند و نمك نبود، غلامی بروستا رفت تا نمك حاصل\nکند.» «گلستان ص ۴۱».»\n\nOther footnotes on the page: ۲ ـ از: نمك + دان (پسوند ظرف)؛ ۳ ـ از: نمك + سود\n(سوده = سائیده)، معرب آن هم نمكسود «دزی ج ۲ ص ۷۲۶»؛ ۴ ـ از: نمك + ینه (نسبت)؛\n۶ ـ نمودار: پهلوی n(i)mūtār «اسشق ۱۰۴۲»، از: نمو (نمودن) + دار (= tār پسوند اسم\nفاعلی و مفعولی).\nRunning head: نمك ‎-۲۱۷۰-‎ ; page foot: (برهان قاطع ۳۷۴)\nEOF\necho saved; grep -c . ocr/BQT/2170.vision.txt"
}
```


### [2026-09-07T18:20:45.014Z] TOOL RESULT

```
saved
14
```


## [2026-09-07T18:20:45.532Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nəmadka\\|nmadka\\|nemadka\\|namadka\\|nəmata\" BRT.txt | head; echo \"=== BRT aβra\"; grep -n \"aßra\\|avra-\\|a\\.ßra\" BRT.txt | head -10; echo \"=== BRT napta\"; grep -n \"napta\\|nabah\\|nab\\.h\" BRT.txt | head -15"
}
```


### [2026-09-07T18:20:45.626Z] TOOL RESULT

```
=== BRT aβra
14915:ai.  vgl.  pratifthäy  f.  ■Widerstand'.  —  Pü.  (in 1):  pa  isliSn  i yam,  erl.:  ba  gii  djrel;  gasäti pa  rtäyiitt  apar  mgöiS;  {zu  2):  paßrand'') (Part;  Ausgang  unsicher);  (zu  3):  fiar  tos  t pa an  i  :faiaiik  ke  häl  der  afar  i'WJS  iavät, 50. :  rSjyaiyaca  pralikaraiüm  (np.  GL  pdtl- raßany)  sMtim.  —  t)  \g\i  za  pai'i.aslÖ.vara/1-.
15066:Ableit.  lu  paityaitk-;  vgl.  Bthl.  IT.  3.  267.  — Pü.  (zu  V.):  faßrai,  (lu  N.):  fehlt.  —  »  NA. */i j;  s.  aber  F  1  usw. ;  vgl.  noch  No.  1  tu  paüis. —  »)  Fraarasj/an  sprichtl  —  3)  In  den  Hds. getrennt:  fiaiti  si.~  t)  D.  L  solche  von  einem andern   Pflanzenexemplai;   Pü.  verstehe    icb
15118:KompA.  (vgL  faityai>g>i4b<it3aA'ya-).  —  Eig. 'sich  incückbewegend',  ASn.  au»  "'aog-  Adj.  '> ; tum  Inf.  anjci.  —  Fn.:  /o  paßrak  rawüniA'),
15132:ASn.  ans  'paiiyäpa-  Adj-,  Ableit,  %a  faiii-\-äf-. —  np.  »gl.  päifyäi.  —  S.  auch  *ptaiifa:  — Pa,:  S  faßrai;  falirai  i"  äf,  erL:  d  fai.
=== BRT napta
2547:•  j.  aetada  Adv.  i)  'hier,  da;  dort';  °ia'  •  j.  aeta'vant-  Adj.  'tantus,  so  gross,  so hl  uzbao'jitm  tanäm  nidai'iyqn  V.  5.  12;  viel',  nur  Neuir.  (mit  Gen.  part.):  'vat 45,59,  6'.46,Äii,  100, /Ö.2; —  'oa  an-  alsascit  ästnraytili  (sd.)  N./:i;  —  °%-at hava  asti-ainti  V.rf.i;  • —  bariinava  paiti  ^AuSkanqm  aismanqm  "vat  naptanqm  V.j.
2575:•  j.  aetada  Adv.  i)  'hier,  da;  dort':  "öa  •  j.  aeta'vant- Adj.  'tantus,  so  gross, hl  uzbaoijqm  tanüni  mdaHyqn  V.  5,  12;  viel',  nur  Neulr.  (mit  Gen.  pari.):  ' 45,59,  6".46,  ^.  II,  100, /6".2; —  ''ja  at?-\aisasnt  astüraytiti  (sd.)  N. ;:;;  —  ° kava  astz'ainti  V.^.i;  —  bar>^ava  paiti '  huSkanqm  a!smanqm  'vai  naptanqm  \
10733:Y,  17. 1 1 :  s.  unter  xldhrS.naptar-.  [Y. ^.10:  lies  mqgHje/'.]
17674:•  j.  fra'bäzu.dr^ab-  n.  'Länge  eines FrabStav*^ :  frära%m.dräj5  yat  naptanqm °/s  yat  kuikanqm  (nänü.  aismanam)  "in der  Idnge  eines  Fmr.  von  feuchten,  in der  Länge  einer  Frad.  von  trockenen (Hölzera)"  V.  7. 33,  34;  30.
18268:•  j.  frl'riflmdräjah-  n.  'I.änge  eines  Fr. (Elle)'*':  °Js yai  hulkanqm  frabazu.dmjö yat  naptanqm  "in  der  Länge  eines  Fr. von  trockenem,  eines  Frab.  von  feuchtem Holz"  V.  7. 30,  33 ;  29,  5.  4  PiiZ.3;  —  *"> N.  10  j  ".
18541:•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
18556:•  j.  napta-  Adj.  'feucht':  altavat  huskatiam alsmanqm  aztavat  "ianqm  V,  7.  31;  29,  30, 33.  34;  —  kuskanqm  yavanqm  .  .  'tanan V.7.35.
18558:•  j.  naptar- :  «qM'^  m.:  s,  unter  napäi-
18565:j.  nah-  V.  *befeuchten,  benetzen'.   PPfP. napta-^''  (sbes.);  Absol.  'napilm.
18568:g.  nabah-  n.,  Plur.  'Luftraum,  Himmel': iasmJ  d^rpla  zqmui  adf(sd.)  °iasalY.44.^. •ähko!-  n.  —  Pü.:  s,  unter  adf.
```


## [2026-09-07T18:20:58.166Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Wolke\" BRT.txt | head -20; echo \"=== madka\"; grep -n \"madka\\|maSka\\|nsmad\\|n3mad\" BRT.txt | head -10"
}
```


### [2026-09-07T18:20:58.222Z] TOOL RESULT

```
3684:sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, länger":  »»3  ^I^ä  *fX  äsbävayal  (sd.)  Y. Jt.i7.  3)  'auch,  gar,  besonders',  das vorherg.  Wort  hervorhebend:  maS^a  .  . pirs^u  'pi  ffi/ajii/Vjy  "die  Wolken,  die  sich gar  weithin  verbreiten"  YLA40;  io.44; —  \daraiy  'piy  "gar  fernhin"  X.7. 2;  D, 6'.a,  4";  —  ai'e  °pi  dai'jyanlS  "'äx£  y^a^ besonders  hinsehend"  Yt/0.45;  45;  — *avat  'pi  ya^a  . .  "soviel  gerade  (,  eben) aIs.."V.ö'.io;22,Äa3,J7.7.  I^Praen. 1)  mit  Akk.  a)  'über  —  hin';  a)  zeitlich: dar>-^3mHt  °pi  zrvätam  Y.  6-1. 3 ;  Yt  i^. aö,  ß)  räumlich:  vTspqmHl  'pi  imqm  sqm Y. 57.33; — liuire fraväitUßA.)  tq%ryqm  °pi xSapamm  Yt  74. 1 3 ;  —  yavat  anu  "pi  *i}iti garayS  visasiar?  vlsptm  aval  °pi..  "so  gross der  Raum  ist,  über  den  hin  sich  die  üerge erstrecken,  über  all  den  Raum  hin  . ." Yt. 7p.8.  b)  'bei':  k?m  ksm  °pi  nmäm "bei  Jedem  im  Haus"  Yt.  5. 102.  2)  mit Lok.  'bei',  zeitlich:  mi^nm ..yahmi  ssire m%%rS.dru}5  'pi  %n<isi  paun'a{sA.)  masyS- kunhs  ". .  bei  dessen  Gericht  . ."  Yt.  lo. 8of?).  3)  mit  Instr.  'nach',  zeitlich: s.  aipi  tä,  aipi  taiS  bes.  III)  Praev. {m\\.kan',  karat-,  gart-,  gam-,  vai-,  varpi- ua.).  [IIBh.4.8:  lies  utämaty^'»; —  Y.
4000:•  j.  awra-  n.  i)  'Regenwolke,  Wolke': yaha  'nm  vätsJsism  Y,(?.32;  —  'ra upapä  Yt  74.41;  —  'm  F.7.  2)  "Regeii, Regenschauer':  ma?ya  .  .  yähva  urväi/is (sd.)  'r&  Yt.Ä40.
4001:KompE.   —    ai.  aikrä-   n.  'Wolke';    np,  abt •Wolke',  afy.  erif  'Wolke',  baJ.  haur  'Regen'.
10040:ser: US  vS  apqm  aaavS  apaitijrsta  jashnti Yt.  (?.  29.  c)  'aufsteigen',  von  Wolken: namia  dunman  (sd.)  uzjasaili  harat^yS Paiti    bartzayh    Yt.  iQ.  50.  a)    'in    die
13680:•  j.  dunman-  n.  ''Nebel,  Nebelwolke, Wolke':  yayata  'ma  ,  .  frä.ap3m  nyäpftn upa.3p^m  (sd.)  V.21.2;  F.^g;  —  apim.. MdSrra  vat>m  'mqnia  ¥.5.15;  —  naioa 'man  utjasaiti  haratky3  paiti  banzayä "und  nicht  steigen  Nebel  empor  von . ."  Yt. 10. 50;  —  Hat  tat  'man  hqm.hishnti  . .  äat tat  '"tan  frasäupayeiti  (sd.)  magyS-kara Yt  S.  31 1
13682:•  j,  dunmö.frut-  Adj.  'in"  den  Wolken fliegend':  vats  (NP.)  vänti  'tB  (NP.)  xä paiti  Yt/J.i4-
13683:*/rut-  Adj.,  zum  V.  /rav:  —  ai.  'prul-  Adj.  — >)  Oder  auch  'mit'  oder  'mittelst',  wenn  die Wolken  als  Flügel  des  Windes  gedacht  wur- den.   DsT.s  *poussant  tes  nuees'  ist  unrichtig.
13993:•  g.  dv^nman-  n.  'Wolke':  k!  vätäi dvqnmaibyascä  yaog3t  äsS  "wer  verband mit  Wind  und  Wolken  die  Schnelle?"  Y.
17774:mit  US  1)  'aufziehen,  aufsteigen',  von Wolken :  äat  magya  usfravante  . .  yahva  . . "alsdann  steigen  die  Wolken  auf  . ."  Yt, 8. 40.  2)    Kaus.  'hinaus-,   fortschwem-
19433:•  ].  'maej'a-  n.  'Wolke':  andvlm  ..yaiAe ca%wärS  arläna  hqmdälat  aAurS  masdS vat?mca  värimla  -jgmla  fyaahum^a  Yt 5.120;  ÄSS,  Y.io.3;  —  Bat  *ya^*  ui.- fravänti  kuyäirya  äpö  öanntii'  ySkva  . . p?r3%u  aipi  vjJasSitlS  avS  urvaitls  (sd) "dann  steigen  die  Wolken  auf,  die  die  . . Wasser  enthalten,  (die  Wolken)  in  denen . .,
19440:Et.?  —  Pü.:  wa'>-  —  '>  Oder  dgl.  — »)  Wohl  nur  Transsltr.  'Wolke'  (Horm  NpEl. 236)  kann  doch  nicht  gemeint  sein.  Zu  V.  T3 \iX  PQ.  nicht  in  Ordnung;  m  d  z  n  an  n.
22600:feuchten  Wolken  von  oben  her  die  grossen
22981:Zum  V.  Ivat:  —  ai.  ürmäy-  f.,  sbal.  ^tiarm; PDs.  T/arm  'Wolke,  Nebel'.  —  Vgl,  a^a-i.- varalay:
23483:Ir.  wohl  'sfä/fcSä-  (IF.  p.  261),  Bildung  mit Int-Red.  —  ")  Ohne  Wert  Gdn.  KZ.  ij.  551 1 'Wolkenbruch',    Dst.   ZA.  2.  5491    *rinconti-
25655:•  j.  'urvant-  Adj.  (fem.  'vSiti-)  'flicssend, strömend',  auch  mit  Akk.  des  Inhalts'*: maiya  .  .  yahva  'väitii  (NPf.  statt  n.) awra  p)r3hu  aipi  vJjasäiti?  avS  "vaitTs (NPf.)  hapta  kar^qn  "die  Wolken  . .,  in denen  die  strömenden  Regenschauer  ent- halten sind,  die  Wasser  strömend  sich  gar weithin  verbreiten  über  die  sieben  K.  hin" Yl  Ä  40 ;  —  andvt  süra  . .  frä  . .  sispata *'vaiti''>  iaBu.staayeAi  (sd.)  Yt5.  7.
29197:•  j,,  g.  ha'ÖTä  i)  Adv.  "an  einem  Ort, zu  gleicher  Zeit;  zusammen,  zugleich': ap»m  tazähi  tatn  yö  ahurS  mazdä  zra- yanha^  hata  vouru,kasät  °ra  vstimca  dun- mqnca  "entlässt  du  . .  das  Wasser  aus  dem Meer  V.,  zugleich  den  Wind  und  die Wolken"  V.  5.  15;  Vyt  42(?);  —  tä  'ra fra/rSvayühi  avi  zrayü  .  .  V.5.  16;  10; —  mit  vfspa-  'alle  zusammen"':  na^a vUpe  'ra  daiva  mahrka%ai  upadarznvainii
=== madka
```


## [2026-09-07T18:21:08.498Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=3990 && NR<=4005' BRT.txt | cut -c1-200; echo \"=== find col markers near 4000\"; awk 'NR>=3940 && NR<=4002 {if ($0 ~ /^[0-9]{2,4}$/ || $0 ~ /^ *[0-9]{2,4} *$/) print NR\": \"$0}' BRT.txt | tail -5; echo \"=== near 18556\"; awk 'NR>=18400 && NR<=18570 {if ($0 ~ /^ *[0-9]{3,4} *$/) print NR\": \"$0}' BRT.txt | tail -5"
}
```


### [2026-09-07T18:21:10.006Z] TOOL RESULT

```
Komp.:  anvi-^'ySvAana-,  zum  V.  >^Ö^..  —  Vgl. np.  ffrähani)  'Hemd',  hamyä»^')  'Gürtel'.  — Pü. ;  aiiByäAami,  'AanilniiTi,  erl.:  hisdt.  — »  Vgl.  zu  diesem  Bild  V.  iS, 
—  »  Hier  -Aäiiä.  —  3)  Vgl.  iSU  IF.  /AliO.
—  4)  Hds.  •Aii/a;  Pü.:  nndeotlich.  —  5)  Ans */ar(i);'ä^a'M-;s.daxuIlBU.FSt.  ioi.FkMDller WZKM.  S.  93.  —  <•>  Aus  *hamiähana'  (zu  HoRN GIrPh.  /b.  96.  7b).  —  7)  S."z
•  j.  aiwyaohayamna-  Adj.,  PFM.:  s. Komp.;  ahoi-Y^y&ah' .
db,Google
99
aiwyaohä-
afradsr^svant-
•  j.  aiwyaaha-  f.  'Lesen,  Studium'  uzw.  1  durch,  dass  ihm  (dem  Schüler)  kein  Be- der  heiligen  Texte:  ka  asti  ihy^a  »la/^!  scheid  wird?"  N.  ij; —  vtspagsu  "partnti saonB
heiligen  Texte)  nicht  obliegt,  (dass  er)  die G.  nicht  aufsagt"  V.iS.g'K Aus  ar.  *ai*jäsä-  (oder  auch  'asä-,   %  36S,  3, igS.']'}),  »om  V. 'a^-,  —  Pü.:  anvyähan  ahoyä- ha
•  j.  awra-  n.  i)  'Regenwolke,  Wolke': yaha  'nm  vätsJsism  Y,(?.32;  —  'ra upapä  Yt  74.41;  —  'm  F.7.  2)  "Regeii, Regenschauer':  ma?ya  .  .  yähva  urväi/is (sd.)  'r&  Yt.Ä
KompE.   —    ai.  aikrä-   n.  'Wolke';    np,  abt •Wolke',  afy.  erif  'Wolke',  baJ.  haur  'Regen'.
—  Fii.:  awr,  {lu  F.  /):  m  dtrk, j.  awS'  (KonpA.):  s.  'avaA:
•  j.  aw2-däta-  Adj.  'ins  Wasser  gelegt, im  Wasser  ruhend':  vätasca  ys  darsU 'timca  ifaivnS  YtÄ  34.
•  j.  await-dina- Adj.  'einen  Wasserbehälter, ein  Wasserbecken  bildend':  vairfsla  °nht>hs (als  AP.)  Y.42.a.
*dina-  n.,  zum  V.  'i/J- ;  :ü.  'dhäiia-  n.,  np.  'dän.
=== find col markers near 4000
3963: 97
3995: 99
=== near 18556
```


## [2026-09-07T18:21:15.238Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=18570 {if ($0 ~ /^ *[0-9]{3,4} *$/) {n=NR; v=$0}} END{}' BRT.txt; awk 'NR<=18570 && ($0 ~ /^ *[0-9]{3,4} *$/) {n=NR; v=$0} END {print n\": \"v}' BRT.txt; awk 'NR<=18570 && ($0 ~ /^ *[0-9]{2,4} *$/) {n=NR; v=$0} END {print n\": \"v}' BRT.txt"
}
```


### [2026-09-07T18:21:16.749Z] TOOL RESULT

```
17866: 998
18371: 17
```


## [2026-09-07T18:21:26.239Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^abr \\|abr \\[\\|nam \\[\\|namb\\|namak\\|naft\\|nam(b)\" PHD.txt | head -20; echo \"=== PHD pages variant\"; grep -n \"namb\\|namak\\|naft\" PHD_pages.txt | head -20"
}
```


### [2026-09-07T18:21:26.293Z] TOOL RESULT

```
230:babr [bpl | N ~] tiger.
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
376:gabr [gpl, gwbl | M gbr, N ? gór] hollow, cavity, womb. ~ih: hollowness. баё [gc | N ~] plaster, gypsum. -ёп [-yn!] (made of) plaster. gad [gt! = Av. gada-] club, mace. gādan, gày- [SL Y TWN-tn! < А V sry ?; g'tn! | N ~] copulate with. gadar [g??]] husband. gadwar [gtwl = Av. gaóawara-] bearing a club. 1gàh [gs | M ek, N ~] place, throne, bed. ?6àh [g’s | N ~] time; a fifth division of the day; = ģāhānbār. збаһ [gs] а Gatha, hymn. gah4n [g’s’n'] the Gathas; those scriptures dealing with spiritual and theological matters. ģāhānbār [gnb] | N gáhanbár] the six divisions of the year, the five-day festivals celebrated at the ends of these. ģāhānīg [g?snyk!] relating to the Gathas; spiritual; the five epact days at the end of the year. gahbed [g’spt' | N *gahbad] treasurer, banker. ~ih: treasurership. gahl [г()А | N gal] sorghum, giant millet. gāhüg [p hwk'] bier. gāhwārag [g’swlk' | N gāhwāra] cot, cradle. ģāl [2° household, following.
494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
1486:damp naft; v. moist.
1553:demolish nambāstan.
1558:depart franaftan.
1563:descendant naft.
1872:fall down (collapse) nambastan.
2112:go franaftan, raftan, Sudan; cause to ~ rawénidan.
2839:moist naft, tarr, xwēd.
2887:naphtha naft.
3229:proceed franaftan, raftan.
3366:reject anaftan, spóxtan.
3505:salt namak; (land) sórag.
4667:parwar- parwarisn Frawardin Frawardīgān fraward parwardan frawardag franam- parwast parwastan franaftan frušag
5164:wardišnīgīh E 4) vo t | wardišnīg Véi ru re 1 wardišn i0 «e ` -om “G\- nam KA nimāy- -AAG A namāz °з^6 \ wimēhgen 1 5^6 nimüdan Viel namak 1361 namad VEGA, nasa, wisē А99 | wisāy- = A235 1 wisān- - ras "wisāndan x 75991 wë = 1693 1 wēxtan! Veras i wisānišnīh AS PO v351 wisānišn vu rudi namiz! «eX wasyar asi wisin(n)- — pai wasyar `Y, 9459 A nask V A35 \ nasruštīli ^ TANT 1
=== PHD pages variant
1027:AnAb-, -iAn, v. anaftan.
1042:inaftan, anib- ['n)pen', )n)p- I M )n)pt, Cn'm-)] avert, reject, frustrate.
2315:franaftan, ·franam- [plnptn l , ·plnm- I M prnpt, prnm-] go, proceed,
2317:franaftan, franam- [pln)ptn 1, pln)m- I P frn)m-] I. lead, conduct, re-
3643:Inaft [npt l I = M, N .......] moist, damp; naphtha.
3644:2naft [npt l ] descendant.
3653:namak [nmk ' I M nmyhk, N .....] salt.
5974:Aryan £ranag; - home, land £ran-         avert anaftan.
6235:combustion sog, sozisn.                  conduct (v.) franaftan.
6309:crime agrift, winah.                       damp naft; v. moist.
6389:depart franaftan.                          difficult duskar, dus(x)war, gariin.
6395:descendant naft.                           dignity huskohih, skoh.
6707:go franaftan, raftan, sudan; cause to            waranig.
6767:hardness, hardship skeftih.              heir namburdiir; enoken.
6980:lead (v.) anidan, franaftan, hiixtan,        hawand, Manigo
7121:moist naft, tarr, xwed.
7126:  new -- andarmah.                             naphtha naft.
7305:   skohih.                                     proceed franaftan, raftan.
7323:   afrinagan, homast.                          promote franaftan, abgar-.
7326:pregnancy iibusih.                             propagate franaftan, rawagenidan.
```


## [2026-09-07T18:21:36.416Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^abr\\|abr \\[\\|abr(\" PHD_pages.txt | head; echo \"=== cloud\"; grep -n \"cloud\" PHD_pages.txt | head; echo \"=== NYB\"; grep -n \"namb\\|namak\\|naft \\|abr \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T18:21:36.486Z] TOOL RESULT

```
813:abr [lbl, 'pl I N -] cloud.           ,\'\ f:>( I
814:abrang ['plng I N aurang] glory, splendour.
815:abrastan, abraz- ['jWstn l , )j)l'e- I M 'br'st, N (afraltan), afraz-] lift, raise.
816:abraz [lj)l'c I N afraz] acclivity.
817:abre~om ['plyf(w)m I M 'brylwm, N -] silk.
819:abroxtan, abrl>z- [lplwhtn', )plwe- I M )brwxt, 'brwc-, N afroxtan,
1449:babr [bpl IN ......] tiger.
1809:Idabr [dpl] sinner, deceiver.
1810:2dabr [dpl] ·dark-coloured.
2411:Itabr [gpl, gwbll M gbr, N ? gar] hollow, cavity, womb.
=== cloud
813:abr [lbl, 'pl I N -] cloud.           ,\'\ f:>( I
3525:mey [myy I P myg, N . . . . ] cloud, mist.
4563:snOy [snwd] (rain-, snow-)cloud.
6208:cloud abr, mey, snoy.                    complete (v.) frazaftan, hangirden-
=== NYB
841:ayinaftan [’dynptn'] to reach, to get at, to touch: 6 mar gav ayinaft as for the scoundrel, (his) hands touched 61", with the gl. kū-š ēvak pat dit frac zat he clapped his hands together; 6¢ mar han i dašn gav 6 rān apar ayinaft as for the secundrel, (his) right hand got at his hip = the scoundrel put his right hand on his hip 61%; [yērtāt bē ahi/ayi/-naftak 4 angust but the corn had reached the height of 4 fingers PR 29° (written *hdynptk', a
844:with the common alternation of -y- : -h-]. — < abs + Av. (1041) nam-, cf MPrth ’bnft "hynd ‘they went off (to the tomb)’ M 18! (S), Ghilain 73, cf Skr abhi-nam- ‘to approach a p.’; as to the develop- ment of abi- in SW cf s. v. omet; as to -mt- > -ft- v. s. v. ahrüm and hanžaftan. Another °bnfin ^to flee’ < Av. (l.c.) apa-nam- (MHC), v. Ghilain, l.c. Cf franaftan, vinaftakeh. NP inaft ‘petition, need, demand’.
2934:pand-namak [pnd SM-k'] “The Book of Counsels’’, title of a treatise 62. — Av. (847) panti-, pa0- ‘path, road’; MPrthPrs pnd “path; counsel’; NP pand ‘counsel, doctrine, rite’.
3070:patkust [p'tkwst] district, province Pl: 8. — The reading is unambiguous and already established by Herzfeld. The form commonly met with in BP is p'tkws = pätkös; MPrthPrs p’dgws, MPrs also p’ygws; Paz. pad-kés (Mx 135). Cf kust, kustak.
4224:doubt by the inscription SM 1. 41 in a passage which is fragmentary but offers wšyk in a coherent piece of text and in unambiguous spelling and meaning. — < Olr "vi-šaika-; etymology ?
4726:JN = Jamasp-namak: 1) Jámáspi, Pahlavi, Pázend and Persian texts with Gujarati Transliteration of the Pahlavi Jámáspi, English and Gujarati Translations with Notes of the Pahlavi Jámáspi, Gujarati Translation of the Persian Jámáspi, and English Translation of the Pazend Jámáspi, by Jivanji Jamshedji Modi. Bombay 1903 (Pahlavi Translations, Part III). 2) Giuseppe Messina, Libro apocalittico Persiano Ayātkār i Zämäspik, Biblica et Orientalia N. 9. Roma 1939.
4730:KnA = Kärnamak ed. Antič, v. MP I, p. XI.
6046:ming: namak
6077:pnd: pand-namak
```


## [2026-09-07T18:21:43.263Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^namak\\|namak \\[\\|^nam \\|nam \\[nm\\]\\|^apr\\|^abr\" NYB_vol2_glossary.txt | head -20; echo \"===\"; grep -n \"salt\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T18:21:43.326Z] TOOL RESULT

```
2934:pand-namak [pnd SM-k'] “The Book of Counsels’’, title of a treatise 62. — Av. (847) panti-, pa0- ‘path, road’; MPrthPrs pnd “path; counsel’; NP pand ‘counsel, doctrine, rite’.
6961:abr: avr
===
38:The Aramaic ideograms used in this Manual are listed here, together with a pre- liminary analysis of the Aramaic lexical material from which they derive. From an Aramaic point of view, most of the forms in which the verbal ideograms appear in Book Pahlavi (as well as in the inscriptions and in the Psalter) are spurious, fabricated as they are by Iranian-speaking scribes and hence without any linguistic foundation. In fact, only impf. forms of the type YKTLWN = YIQT'LUN and some few other forms can claim to be genuine Aramaic. The intricate process by which the Iranian scribes transformed Aramaic forms into purely graphic signs will be dealt with in my new edition of the Frahang i Pahlavik. Here such ideographical forms as have totally fallen out of the Aramaic verbal system will be explained merely by reference to the closest corresponding Aramaic forms or simply to the triconsonantal root, from which the 3d p. sg. perf. can be easily seen, e. g. NKS, pf. N'KAS (NB: — roots as BNY, HZY have the perf. B'NA, HAZA; HDY has HADI).
```


## [2026-09-07T18:21:48.849Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^avr\\|avr \\[\\|avr(\" NYB_vol2_glossary.txt | head; echo \"===namak idx\"; sed -n '6040,6050p;6955,6965p' NYB_vol2_glossary.txt"
}
```


### [2026-09-07T18:21:48.905Z] TOOL RESULT

```
813:avr [pl] cloud(s) 411%. 717%. 8523.. 861, 891%, — Av. (99) awra-; Paz. awar; NP abr.
815:avrang ['plng] splendour, magnificence 1219. — < Olr *abi-ranga- v. rang; NP aurang, afrang. [On MPrth ’drng v. Hen- ning, TPhS 1945, 154 n. 1].
816:avrangikiha ['plngykyh?] in a splendid manner, comp. ~-tar: har cé ~-tar in the most splendid manner 121*.
1244:davr [dpl] course, rough, a nickname of King Yazdagird I: 115’, in Arab sources (references v. Cat. 67) transliterated dafr and translated al-fazz-; renders Av. (1789) harata- ‘well-fed’ Vd. 224; stout, robust, of a warrior DkM 75°. Often written ddpl: PR 5? (ddplyh =:) davréh u drustéh antonyms of carpeh u datistanéh; also in BdA, v. s. v. Gafr-gav, where the constant confusion between ~ and gafr is dealt with. Paz. dawar (Bd Antià 431°; SGV V, 61. 74 is uncertain, and emended by West and de Menasce). — Olr *dabra-, re- presented by Av. (680) dawrd-mačši- ‘possessing well-fed sheep’; Markwart’s etymology (Cat. 1. c.) is untenable.
3538:stavr [stpl] strong, sturdy 718; comp. ~-tar 4918, — Av. (1592) stawra-; MPrth Prs 'stbr, v. Sogd 18; Paz. adv. stavarihā ‘thickly, firmly’ (Mx); NP sitabr; from the same root Ps. stpty, MPrth sstft ‘strong, firm’.
===namak idx
256
qwdk: kotak qyh: !kas
m’hyg: mšhik mn: man
m’n’g: mānākēh m'ny: Mani m’yg: mätakik mgj: mazg
mn-: mönitan mnysn: ménisn mrdwhm: martom mrg: marg
mrw: ?murv mrz-: marzihistan mwrdy?ng: Mahlah mwrw: lmurv mwrw?: murvāk mwy'g: mödak my?n: miyàn myrd: mart mysg: hamésak mzd: mizd
ming: namak
nn: nan
n'y-pzd: nad, pazditan n'zwg: *Mihr-naz nbyg: nipék
nbyštn, nbys-: nipištan nfryn: nifrin
nh’dn, nyh’dg: nihätan - nheyhr: naxeir
va + -pi: aivap vara-: ham-var vatsa-: vaccak vāyu-: *vai
vic-: lvéxtan vicära, vicärayati: vicar vijate: ?vöxtan vrsan-: gusn
New Persian
ab: ap
abad, abadan: apatan
abistan: äpustan
abr: avr
ačar, adar: ātur
afgandan, augandan: apa-kandan
afli)rin: àfrin
Afrasiyab: Fräsiyäk
```


## [2026-09-07T18:21:58.758Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"MING\" NYB_vol2_glossary.txt | head -5; echo \"=== MON files\"; wc -l MON_part1.txt MON_part2.txt; grep -n \"4818\\|۴۸۱۸\" MON_part2.txt | head"
}
```


### [2026-09-07T18:21:58.839Z] TOOL RESULT

```
=== MON files
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
```


## [2026-09-07T18:22:01.912Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['MON']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-07T18:22:03.100Z] TOOL RESULT

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


## [2026-09-07T18:22:09.031Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نمک\" MON_part2.txt | head -8; echo \"=== نپتون\"; grep -n \"نپتون\" MON_part1.txt MON_part2.txt | head -5; echo \"=== نفت\"; grep -n \"^نفت\\|نفت \" MON_part2.txt | head -5"
}
```


### [2026-09-07T18:22:09.108Z] TOOL RESULT

```
6893:آید: نمکک‌فروش. 
10909:انمکاس صدا ندار د. 
18308:بخواهند یک دانه سبر) و نمکك و فلفل به 
18326:نمکن (لف.) کاسةٌ چشم: (پز.) هر یک از دو 
18825:ناسپاس. حق نشناس» نمکث به حرام. 
19586:ملیح. کان نمکك: ( کد.) معشوق ملیح 
19923:نم خوابانیدن: کباب نمکسود. کباب 
19927:و نمکک مخلوط کنند و یک شبانه روز 
=== نپتون
MON_part1.txt:81744:مشتری» زحل, اورانوس» نپتون» پلوتن. 
=== نفت
16403:همان ترکیبات هیدرو کربورهای نفت است 
16425:نفت در نه دیگ‌های تصفبه مقادیری زبادی 
19612:کانفت؛: ۱ [- کامفت ِ قامیت ِِ قانفت 
23319:نفت کش: کشتبی که خاص حمل نفت است. 
25116:و به همین جهت آن را در نفت یا روغن
```


## [2026-09-07T18:22:13.729Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nm.dk\\|nmʼdk\\|nm'dk\\|nmydk\" SOD_pages.txt | head -10; echo \"=== salt\"; grep -n \"salt\" SOD_pages.txt | head -15"
}
```


### [2026-09-07T18:22:13.799Z] TOOL RESULT

```
=== salt
3755:Psalter.  Same Khomese
4718:     STSC, Psalter. 132.21                                         Sogdica. 27.28; Perikhanian, SI 1988, I33n5
14470:         place 140 Psalter. 133.24
20812:                                                                            salty
20820:                                                                            salt
22409:      STSC 137 Psalter. 131.12
22708:     pacaySar (pcxt'r-) ©perf. st. =»pcxs-, pcyt-,                 TSP 10.10; STSC 133.28, Psalter. 133.28 pl41
30078:     rock salt                                                               GMS 1372, 500; >tf, STii 3.1.11                     tA/„
39310: rock salt 9135                           sad    1154,9036
39331:   5328, 10811                           salt 5973                              scented 2883, 2884, 2894, 2895
39332:(to)rub    1 108, 3448, 5485, 7209       salty    5972                          scentholder 2889
```


## [2026-09-07T18:22:18.686Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"5973\\|5972\\|5971 \\|5974\" SOD_pages.txt | head; echo \"=== ctx\"; sed -n '20800,20830p' SOD_pages.txt"
}
```


### [2026-09-07T18:22:18.752Z] TOOL RESULT

```
20813:              Gauthiot. JA 1912, 352; Anc. Lett.; VJ; TSP-,            5972 nmWynch M                                jl^'J^
20817:                                                                       5973 nm'Skdi) B, M                                    jLi
20822:               opt. nmy(})y ); Anc. Lett. 3.11; TSP 3242, 247;         5974 nmVk(w)     B, M, S                  o*U<w
20867:      5971 nm'cyw pr-                        (jy> ^^ j>) j^jU              nimane =»nm}ny, nm'n'kCw)
39113:(ffl)pay homage      5971                persecution     7498                      place of the gods 2605
39238:     (to)reject      1321, 1340, 7115, 7139,     repentance       5974, 5978, 5980, 5983    resurrector  5544
39331:   5328, 10811                           salt 5973                              scented 2883, 2884, 2894, 2895
39332:(to)rub    1 108, 3448, 5485, 7209       salty    5972                          scentholder 2889
=== ctx
     niyosne ^ny'ws^k
     listener                                                 5960 nqt'nq'ry C = n+ qt'nq'ry =» n-, qt'nyq'ry
                                                                                MH^^MMM^HMi^M
                                                                                          nm'nyy



       239

       5961 NLPwtlLP(w))           B, S                     (j*)Jj*         namacyw Par- ^nnVcbry*
              zar ©Idg. =>z*r, z'r1                                         (to)pay homage
              thousand                                                      TSP; VJ; BSTBL; SCE
                                                                            salty
              Gauthiot. JA 1912, 352; Anc. Lett.; VJ; TSP-,            5972 nmWynch M                                jl^'J^
                Frag. Len.; MDii A- 15, 6                                   namaSkenc (nmySk'ynch) ^nm^kCh)
       5962 nm-1     B, C, S     jj ^   <_*^- L j^j5   jj r^)0=9^A
                                                                            Sogdica. 720 n p8
                                                                       5973 nm'Skdi) B, M                                    jLi
              nam- ^nm'y-1                                                  namaSk ©<Av. namaSka; Khwar jimOk
              Oo)consent, (fo)accept (wsei wM /leg.
                                                                            salt
              Benv. BSAOS 30, 1967, 505f; GMS 818A (used in                 GMS 1053; TSP 19.8; Bailey. BSOAS 1975, 54
               opt. nmy(})y ); Anc. Lett. 3.11; TSP 3242, 247;         5974 nmVk(w)     B, M, S                  o*U<w
/%'
               VJ; BSTii: C2 gloss.; Frag., Len^ MDii                       nimane, nimanak(u) ^nm'ny, nm'nyy
                                                                            repentance
      5963 *nm-2 M                    C^J'j^^^J'^^
           nam ^nmy^, nmsy^Ch), nmtMkr'k, nmy, nynVn                        VJ; TSP; GMS 1061; Tales. 467.29; Frag. Len.
           0<?)despise                                                        86.4, 46.5; nmWkw, TSP 2.8, 573; VJ 446,
           Hen. BSOAS 10, 102; BBB 59                                        nmW, VJ 470
      5964 nm^y      B ■* nm-1                                        5975 nrn'n'w B -» nm'n'kCw)
```


## [2026-09-07T18:22:31.331Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"awra\\|Avestic awra\\|abhra\" KLN_1966.txt | head -20"
}
```


### [2026-09-07T18:22:31.385Z] TOOL RESULT

```
4628:Derivatives:  beautiful-ly,  adv.,  beautiful-ness,  n. beautify,  tr.  v.  —  See  beauty  and  -fy. beauty,  n.  —  ME.  bealte,  beaute  (F.  beaute ),  fr. L.  bellitdtem,  acc.  of  bellitas,  ‘prettiness,  charm, loveliness,  beauty’,  fr.  bellus,  ‘pretty,  handsome, charming,  fine,  lovely,  beautiful’,  which  stands for  *dwenelos,  *dwenlos,  and  is  rel.  to  L.  bene, ‘well’,  bonus,  earlier  *dwenos,  ‘good’,  prob.  also to  bedre,  ‘to  make  happy’,  beatus  ‘happy’  and cogn.  with  OI.  duvas-,  ‘gift,  honor,  respect’, duvas-yati,  ‘honors,  respects’.  Cp.  bonus,  and words  there  referred  to.  Cp.  also  beatify,  bel- dam(e),  belladonna,  belle,  belles-lettres,  Beilis,  bel¬ vedere,  clarabella,  embellish,  Christabel,  Rosabel, beaver,  n.,  a  rodent  of  the  genus  Castor.  —  ME. bever,  fr.  OE.  beofor,  rel.  to  ON.  biorr,  OS.  bibar, OHG.  bibar,  MHG.,  G.  biber,  ‘beaver’,  and cogn.  with  L.  fiber,  OSlav.  bebru,  Lith.  bebrus (also  dissimilated  into  vebrus,  debrus),  Lett. bgbrs,  bebris,  OPruss.  bebrus,  W.  befer,  Bret. bieuzr,  Avestic  bawra,  ‘beaver’.  All  these  words lit.  denote  ‘the  brown  animal’;  they  derive  fr. I.-E.  *bhe-bhru-s,  ‘very  brown’,  whence  also  OI. babhruh,  adj.,  ‘brown’;  n.,  ‘the  larger  ichneu¬ mon’.  I.-E.  *bhe-bhru-s  is  reduplication  of  base *bhero-,  ‘brown’.  Both  the  bear  and  the  beaver are  called  after  their  color.  See  bear,  n.,  and brown.
18769:imbricate,  adj.,  overlapping  like  tiles  ( zool .  and bot.)  —  L.  imbricatus,  ‘covered  with  tiles’,  pp. of  imbricare,  ‘to  cover  with  tiles;  to  form  like a  tile’,  fr.  imbrex,  gen.  imbricis,  ‘a  hollow  roof tile  to  lead  off  the  rain’,  fr.  imber,  gen.  imbris, ‘rain’,  which  stands  for  *mbhros  and  is  cogn. with  Gk.  8|jt.(3po?,  ‘rain’,  OI.  abhram,  ‘cloud, atmosphere’,  AvesticaH'r^/n,‘cloud’,OI.am6Aa/i, ‘water’,  Arm.  amb,  amp,  ‘cloud’,  ump,  ‘drink’, and  also  with  L.  nebula ,  ‘mist’.  See  nebula  and cp.  ombro-.  Gk.  &<?p6q,  ‘foam’,  is  not  cognate with  L.  imber,  but  with  Arm.  p'rp'ur,  ‘foam’, imbricate  tr.  v.,  to  lay  so  as  to  overlap;  intr.  v., to  overlap.  —  L.  imbricatus,  pp.  of  imbricare. See  imbricate,  adj.
26234:ombro-,  combining  form  meaning  ‘rain’.  —  Gk. op[3po-,  fr.  opPpos,  ‘rain’,  cogn.  with  Ol. abhram,  ‘cloud,  atmosphere’.  See  imbricate, ombrograph,  n.,  a  rain  gauge.  —  Compounded  of ombro-  and  Gk.-ypaqjoc,  fr.  ypaipEiv,  ‘to  write’. See  -graph.
```


## [2026-09-07T18:22:39.062Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=18769 && ($0 ~ /^ *[0-9]{2,4} *$/) {n=NR; v=$0} END {print n\": \"v}' KLN_1966.txt; awk 'NR>=18769 && NR<=18830 && ($0 ~ /^ *[0-9]{2,4} *$/) {print NR\": \"$0}' KLN_1966.txt | head -3; echo \"=== nebula/nimbus in KLN\"; grep -n \"nebula,  n\\|nimbus,  n\" KLN_1966.txt | head"
}
```


### [2026-09-07T18:22:40.304Z] TOOL RESULT

```
9203: 41
=== nebula/nimbus in KLN
25093:Nebuchadnezzar,  Nebuchadrezzar,  n.,  king  of Babylon  (604-562  B.C.E.).  —  Heb.  N^bhukhadh- netztzdr,  acollateral  (oimo(Nebhiikhadhretztzdr, fr.  Bab.  Nabu-kudurri-usur,  which  prob.  means lit.  ‘Nebo,  protect  the  boundary’.  Cp.  Gk.  Na- poxoSpooopo;  in  Strabo  15,1,6,  and  in  Josephus Flavius,  Contra  Apionem  1,146. nebula,  n.,  a  cloudlike  patch  in  the  sky  (astron.) —  L.,  ‘mist,  fog,  cloud’,  fr.  I.-E.  base  *(e)nebh-, ‘moist,  vapor,  mist,  cloud’,  whence'  also  OI. ndbhas-,  ‘vapor,  cloud,  fog,  sky’,  Avestic  nabah -, ‘air,  sky’,  Gk.  veipo?,  vcfpeXz],  ‘cloud,  mist’,  OS. nebal,  OFris.  nevil,  MDu.,  Du.  novel,  OHG. nebul,  MHG.,  G.  nebel,  ‘fog’,  ON.  nifl-  (in Niflheimr,  ‘abode  of  darkness’,  i.e.  ‘the  nether world’),  njol,  ‘night’,  OE.  nifol  (adj.),  ‘dark’, MW.  nyfel,  ‘cloud’,  W.  ttiwl,  Co.  niul,  ‘cloud, fog’,  OIr.  nem,  ‘sky’,  OSlav.  nebo  (gen.  nebese), ‘sky’,  Lith.  debesls  (for  *nebesis ),  ‘cloud’  (the d-  is  prob.  due  to  the  influence  of  dangits, ‘sky’),  Hitt,  nepish  (gen.  nepishash),  ‘sky’,  Aves¬ tic  napla-,  ‘moist,  humid’.  Cp.  nepheline,  nepho-, Neptune,  Nibelungs,  nimbus,  imbricate. Derivatives:  nebul-ar,  adj.,  nebul-iz-ation,  n., nebul-ize,  tr.  v.,  nebul-iz-er,  n.,  nebulous  (q.v.) nebulosity,  n.,  1)  condition  of  being  nebulous;  2) cloudiness;  3)  a  nebula.  —  F.  nebulosite,  fr. Late  L.  nebulositatem ,  acc.  of  nebuldsitas,  fr.  L. nebulosus.  See  nebulous  and  -ity. nebulous,  adj.,  1)  resembling  a  nebula ;  2)  clouded, cloudy,  misty;  3)  vague  —  L.  nebulosus,  ‘cloudy’, fr.  nebula.  See  nebula  and  -ous.
25440:Derivatives:  nimble-ness ,  n.,  nimbl-yt  adv. nimbose,  adj.,  cloudy.  —  L.  nimbosus,  ‘cloudy, stormy’,  fr.  nimbus.  See  nimbus  and  -ose. Derivative:  nimbos-ity,  n. nimbus,  n.,  1)  a  cloudlike  splendor  round  the head  of  a  divinity ;  a  cloud  surrounding  a  person or  thing;  an  aura,  a  halo  (art)',  2)  a  raincloud (meteor.)  —  L.,  ‘rainstorm,  thundercloud’,  fr. *nembhos',  cogn.  with  Pahlavi  namb,  nam,  ‘dew, fog,  mist’,  ModPers.  nem,  ‘moist,  moisture',  fr. I.-E.  base  *nembh-,  which  is  rel.  to  base  *enebh-, ‘moist,  vapor,  mist,  cloud’,  whence  OI.  nabhas-, ‘mist,  cloud,  sky’,  Gk.  vlqso ?,  vs^eXv),  ‘cloud, mist’,  L.  nebula,  ‘mist,  fog,  cloud’.  See  nebula and  cp.  words  there  referred  to.
```


## [2026-09-07T18:22:50.814Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l KLN_1966.txt && grep -c $'\\f' KLN_1966.txt; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('pages',len(pages))\nfor i,p in enumerate(pages):\n    if 'imbricate,  adj.' in p: print('leaf idx',i)\n    if 'nimbus,  n.,  1)' in p: print('nimbus leaf idx',i)\n    if 'Neptune,  n.' in p: print('neptune leaf',i)\nEOF"
}
```


### [2026-09-07T18:22:52.263Z] TOOL RESULT

```
41262 KLN_1966.txt
902
pages 903
leaf idx 415
neptune leaf 557
nimbus leaf idx 561
```


## [2026-09-07T18:22:59.899Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    m=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', p)\n    if m: print(i, m[:4])\nEOF"
}
```


### [2026-09-07T18:23:01.370Z] TOOL RESULT

```
0 ['1966']
6 ['37']
17 ['10', '11']
18 ['12', '13']
19 ['14', '15']
20 ['16']
21 ['18', '19']
22 ['20']
23 ['22']
24 ['23', '24']
25 ['25', '26']
26 ['27', '28']
27 ['29', '30']
29 ['04', '35']
31 ['36', '37']
32 ['39']
33 ['40', '41']
34 ['42', '43']
35 ['44', '45']
36 ['46']
37 ['49']
38 ['50', '51']
39 ['52', '53']
40 ['54', '55']
42 ['58', '59']
43 ['60', '61']
44 ['62', '63']
45 ['64', '65']
46 ['66']
47 ['67', '68']
48 ['69', '70', '71']
49 ['72', '73']
50 ['74', '75']
51 ['76']
52 ['77', '78', '79']
54 ['80', '81']
55 ['82', '83', '84']
56 ['85']
57 ['86', '87']
60 ['92', '93']
62 ['96']
64 ['100', '101']
65 ['102', '103']
66 ['104', '105']
67 ['106', '107']
68 ['108', '109']
69 ['110', '111']
70 ['112']
71 ['113', '114']
72 ['115', '116', '117']
74 ['120', '121']
75 ['122']
76 ['123']
77 ['124', '125', '126', '127']
78 ['128', '129']
80 ['130', '131']
81 ['132', '133']
82 ['134']
83 ['135', '136', '137']
85 ['140', '141']
86 ['142', '143']
87 ['144', '145']
88 ['146']
89 ['148', '149']
90 ['150', '151']
92 ['154', '155']
93 ['156']
94 ['157']
96 ['161']
97 ['164', '165']
99 ['166', '167']
100 ['166', '169']
101 ['170', '171']
102 ['172', '173', '174']
104 ['176']
106 ['180', '181']
107 ['182', '183']
109 ['186', '187']
112 ['193']
113 ['194', '195']
114 ['196', '197']
115 ['198']
116 ['199', '200', '201']
117 ['202']
118 ['203', '204']
119 ['205']
120 ['206', '207']
121 ['208', '209']
122 ['210', '211']
123 ['212', '213']
124 ['214', '217']
125 ['218', '219']
128 ['222', '223']
129 ['224', '225']
130 ['226', '227']
131 ['228']
132 ['230']
133 ['232', '233']
134 ['234', '235']
135 ['236', '237']
136 ['238', '239']
137 ['240']
138 ['243']
139 ['244', '245']
140 ['246', '247']
141 ['248', '249']
142 ['250', '251']
144 ['254']
146 ['256', '257']
147 ['258', '259', '260', '261']
149 ['262', '263']
150 ['264', '265']
151 ['266', '267']
152 ['268', '269']
153 ['270', '271']
154 ['272', '273']
155 ['275']
156 ['276', '277']
158 ['280', '281']
159 ['282', '283']
161 ['286']
164 ['292', '293']
165 ['294', '295']
167 ['298']
168 ['299', '300']
172 ['306', '307']
174 ['310', '311']
175 ['312', '313']
176 ['314', '315']
177 ['316', '317']
178 ['318', '319']
180 ['322', '323']
181 ['324', '325']
182 ['327']
183 ['328', '329']
184 ['330', '331']
185 ['332', '333']
186 ['334', '335']
187 ['336', '337']
188 ['338', '339']
189 ['340']
190 ['341', '342', '343']
192 ['340']
193 ['348', '349']
194 ['350']
195 ['351', '352']
196 ['41']
197 ['357']
198 ['358', '359']
199 ['360', '361']
201 ['362', '363']
202 ['364', '365', '366']
206 ['373']
207 ['374', '375']
208 ['376', '377']
209 ['378', '379']
210 ['380']
211 ['382']
212 ['385']
213 ['386', '387']
214 ['386']
215 ['389', '390', '391']
216 ['392']
217 ['393', '394']
218 ['396', '397']
220 ['400']
221 ['401', '402', '403']
223 ['404', '405']
224 ['406', '407']
226 ['410', '411']
228 ['414', '415']
229 ['416', '417']
231 ['420', '421']
232 ['422', '423']
233 ['424', '425']
234 ['426', '427']
235 ['428', '429']
237 ['432', '433']
238 ['434', '435']
239 ['436', '437']
240 ['438', '439']
241 ['440', '441']
244 ['444', '445', '446']
245 ['447', '448']
246 ['449']
247 ['450', '451', '452', '453']
248 ['454']
249 ['455']
250 ['456', '457']
252 ['460', '461']
253 ['462', '463']
254 ['464', '466']
255 ['466', '467']
256 ['468', '469']
257 ['470', '471']
258 ['472']
259 ['473', '474', '475']
260 ['476']
261 ['477']
263 ['480', '481', '483']
264 ['484', '485']
265 ['486']
266 ['487']
267 ['488', '489', '490', '491']
270 ['497']
273 ['501', '502', '503']
274 ['504', '505']
276 ['506', '507']
277 ['508']
278 ['510']
279 ['512', '513']
281 ['516', '517']
282 ['518', '519']
283 ['520', '521']
284 ['522', '523']
285 ['524', '525']
287 ['528', '529']
288 ['531']
289 ['532', '533']
290 ['534', '535']
291 ['536', '537']
292 ['538', '539']
293 ['540']
294 ['541']
295 ['542', '543']
296 ['544', '343']
298 ['548', '549']
299 ['550', '551']
300 ['552']
301 ['554', '555']
302 ['556', '557']
303 ['558']
304 ['560', '561']
305 ['562', '563']
306 ['564', '565']
307 ['566', '567']
308 ['300']
309 ['570', '571']
311 ['574', '575']
312 ['576', '311']
313 ['578', '579']
314 ['580', '581']
315 ['582', '583']
316 ['584']
317 ['585', '586']
318 ['587', '588', '589']
320 ['590', '591']
322 ['596', '597']
324 ['598', '599']
325 ['600', '601']
326 ['602', '603']
327 ['604', '605']
332 ['613', '614']
333 ['615']
334 ['616', '617', '618']
336 ['620', '621']
337 ['622', '623']
338 ['624', '625']
339 ['626', '627']
340 ['628', '629']
341 ['630']
342 ['632']
343 ['634', '635']
344 ['636', '637']
345 ['638', '639']
346 ['640']
348 ['644', '646']
349 ['646', '647']
350 ['648']
351 ['650', '651']
353 ['033']
355 ['658']
356 ['659', '660']
357 ['661']
359 ['664', '665']
360 ['666', '667']
361 ['668', '669', '670']
362 ['671', '672']
364 ['674', '675', '676']
365 ['677']
366 ['678', '679', '680']
367 ['681']
368 ['682']
370 ['686']
371 ['688', '689']
372 ['690', '691']
373 ['693']
374 ['694', '695']
375 ['696', '697']
376 ['698', '699']
377 ['700', '701']
378 ['702', '703']
379 ['704', '705']
380 ['706']
381 ['707', '708']
382 ['709', '710']
383 ['711', '712']
384 ['713', '714']
385 ['715']
386 ['716', '717']
387 ['718', '719']
388 ['720', '721']
389 ['722', '723']
390 ['724', '725']
391 ['726', '727']
393 ['730', '731']
394 ['732', '733']
395 ['734', '735']
396 ['736', '737']
397 ['738', '739']
398 ['740', '741']
399 ['742']
400 ['743']
401 ['746']
402 ['747', '748', '749']
404 ['750', '751']
405 ['752', '753', '754', '755']
406 ['756']
407 ['757']
408 ['758', '759', '760']
409 ['761', '762']
411 ['764', '765']
412 ['766', '767']
413 ['768', '769']
414 ['770', '771']
415 ['772', '773']
416 ['774', '775']
417 ['776', '777']
418 ['778', '779']
419 ['780', '781']
420 ['782', '783']
422 ['786', '787']
423 ['788', '789']
424 ['790']
425 ['791']
426 ['794', '795']
428 ['796', '797']
429 ['798', '799']
430 ['800', '801']
431 ['802', '803']
432 ['804', '805']
433 ['806', '807']
434 ['808']
435 ['809', '810', '811']
436 ['812', '813']
437 ['814']
438 ['815']
441 ['816', '817']
443 ['820', '821']
444 ['822']
445 ['824', '825']
446 ['826', '827']
447 ['828', '829']
448 ['830', '831']
449 ['832', '833']
450 ['834', '835']
451 ['636', '837']
452 ['838']
453 ['840', '841']
454 ['842', '843']
455 ['844', '845', '846']
456 ['848']
457 ['849']
458 ['850', '851']
459 ['852', '853', '1967']
460 ['857']
461 ['858', '859']
462 ['860', '861']
463 ['862', '863']
464 ['864', '865']
465 ['866', '867']
466 ['868']
467 ['869', '870']
468 ['871', '872', '873']
469 ['874']
470 ['875', '876']
472 ['878', '879']
473 ['880', '881']
474 ['882', '883']
477 ['888']
478 ['889']
479 ['890', '891']
480 ['892', '893']
482 ['897']
483 ['898', '899']
484 ['900', '901']
485 ['902', '903']
486 ['904']
487 ['905', '906']
488 ['907', '908']
489 ['909']
490 ['910', '911']
491 ['912', '913']
492 ['914', '915', '916']
493 ['919']
495 ['921', '922']
496 ['923', '924']
497 ['925', '926']
498 ['927', '928']
499 ['929']
500 ['930', '931']
501 ['932', '933', '934']
502 ['935', '936']
503 ['937', '938', '939']
505 ['940', '941']
506 ['942', '943', '944', '945']
507 ['946', '947']
509 ['948', '949']
510 ['950']
511 ['953']
513 ['957']
514 ['958']
518 ['966', '967']
519 ['968']
520 ['970', '971']
521 ['972']
522 ['974']
523 ['976']
524 ['977', '978']
525 ['979', '980']
529 ['986', '987']
530 ['988', '989']
531 ['990', '991']
532 ['992', '993']
533 ['994']
535 ['998', '999']
536 ['1000']
537 ['1002', '1003']
538 ['1004', '1005']
539 ['1006', '1007']
540 ['1008', '1009']
541 ['1010']
542 ['1011', '1012']
544 ['1015', '1016', '1017']
546 ['1021']
547 ['1022']
550 ['1028']
552 ['1033']
553 ['1035']
554 ['1036']
555 ['1039']
556 ['1040']
559 ['1046']
564 ['1054']
565 ['1056', '1057']
566 ['1058', '1059']
567 ['1060', '1061']
568 ['1062', '1063']
569 ['1064']
570 ['1066']
571 ['1067', '1068']
572 ['1070', '1071']
573 ['1072']
578 ['1081']
579 ['1082', '1083']
580 ['1084', '1085']
581 ['1086']
582 ['1088', '1089']
584 ['1093']
585 ['1094', '1095']
586 ['1096']
589 ['1103']
591 ['1106', '1107']
592 ['1108']
594 ['1113']
595 ['1114', '1115']
596 ['1116', '1117']
597 ['1118', '1119']
598 ['1120', '1121']
599 ['1122', '1123']
600 ['1124', '1125']
601 ['1126', '1127']
602 ['1126']
604 ['1130', '1131', '1132', '1133']
605 ['1134', '1135']
607 ['1136', '1137', '1138', '1139']
608 ['1140']
612 ['1146']
613 ['1148', '1149']
614 ['1150', '1131']
615 ['1153']
616 ['1154', '1155']
617 ['1156', '1157']
618 ['1158']
619 ['1160', '1161']
620 ['1162']
621 ['1164']
622 ['1166', '1167']
623 ['1168']
624 ['1169', '1170', '1171']
625 ['1172']
627 ['1176']
628 ['1177', '1178', '1179']
630 ['1180', '1181', '1182']
631 ['1183']
635 ['1190']
639 ['1198', '1199']
640 ['1200', '1201']
642 ['1204', '1200']
643 ['1206']
645 ['1209', '1210']
646 ['1213']
647 ['1214', '1215']
648 ['1216', '1217']
649 ['1218', '1219']
650 ['1220', '1221']
652 ['1223']
655 ['1228']
656 ['1231']
657 ['1232']
664 ['1245', '1246', '1247']
665 ['1249']
666 ['1250', '1251']
667 ['1252', '1253']
668 ['1254', '1255']
669 ['1256', '1257']
670 ['1258']
671 ['1259', '1260', '1261']
673 ['1263', '1264']
678 ['1273']
679 ['1274', '1275']
680 ['1276']
681 ['1278', '1279']
682 ['1280']
683 ['1285']
685 ['1286', '1287']
686 ['1288']
688 ['1294', '1295']
689 ['1297']
691 ['1298']
692 ['1300']
695 ['1307']
696 ['1309']
697 ['1311']
699 ['1312', '1313']
700 ['1314', '1315']
701 ['1316', '1317']
702 ['1318', '1319']
703 ['1320', '1321']
704 ['1322', '1323']
705 ['1324', '1325', '1326']
707 ['1329']
708 ['1001']
711 ['1336']
713 ['1341']
714 ['1342']
715 ['1044', '1345']
716 ['1346', '1347']
719 ['1353']
720 ['1354', '1355']
721 ['1356']
722 ['1359']
723 ['1360']
726 ['1365']
729 ['1373']
731 ['1377']
732 ['1378']
734 ['1382']
739 ['1391', '1392']
744 ['1401', '1402']
745 ['1405']
750 ['1413']
752 ['1416']
755 ['1422']
756 ['1424', '1425']
757 ['1426', '1427']
758 ['1428']
764 ['1439', '1440', '1441']
765 ['1442']
766 ['1443', '1445']
767 ['1444', '1446']
768 ['1448']
769 ['1449', '1450', '1451']
771 ['1452', '1453']
772 ['1454', '1455', '1456']
777 ['1465']
778 ['1466', '1467']
779 ['1469']
780 ['1470', '1471']
781 ['1473']
783 ['1477']
784 ['1479']
786 ['1483']
787 ['1485']
790 ['1491']
791 ['1492']
794 ['1499']
796 ['1501']
797 ['1503']
798 ['1505']
799 ['1507']
802 ['1513']
803 ['1514', '1515']
804 ['19']
811 ['1529', '1531']
813 ['1533']
814 ['1534']
815 ['1537']
817 ['1541']
818 ['1543']
819 ['1544', '1545']
820 ['1340']
821 ['1548', '1549']
822 ['1510', '1551']
823 ['1552', '1553']
824 ['1554', '1555']
825 ['1556']
829 ['1565']
830 ['1566']
831 ['1568', '1569']
833 ['1572']
835 ['1577']
836 ['1578', '1579']
837 ['1580']
838 ['1583']
839 ['1584', '1003']
845 ['1596', '1597']
846 ['1598', '1599']
847 ['1600', '1601']
848 ['1602', '1603']
849 ['1604', '1606']
852 ['1608', '1609']
862 ['1626']
863 ['1629']
864 ['1630']
865 ['1632', '1633']
866 ['1634', '1635']
867 ['1636', '1637']
869 ['1641']
870 ['1642', '1643']
871 ['1644', '1043']
872 ['1040', '1647']
878 ['1657']
880 ['1661', '1662']
883 ['1666']
887 ['1675']
888 ['1676']
889 ['1679']
890 ['1680']
892 ['1003']
895 ['1691']
896 ['1692']
898 ['1694', '1695']
899 ['1696']
```


## [2026-09-07T18:23:09.654Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\np=t[557]\ni=p.find('Neptune')\nprint(p[i-200:i+1400])\nEOF"
}
```


### [2026-09-07T18:23:11.022Z] TOOL RESULT

```
tis- mo,  fr.  nipote,  ‘nephew’,  fr.  L.  nepotem,  acc.  of nepos.  See  nephew.  For  the  ending  see  suff.  -ism.
nepotist,  n.,  one  who  practices  nepotism.  —  See prec.  word  and  -ist.
Neptune,  n.,  1)  the  god  of  the  sea  in  Roman mythology;  identified  later  with  the  Greek  god Poseidon ;  2)  name  of  a  planet.  —  L.  Nepliimis, ‘the  sea  god;  the  sea’,  prob.  fr.  I.-E.  base *(e)nebh-,  ‘moist’,  whence  also  Avestic  napta-, ‘moist,  humid’,  L.  nebula,  ‘mist,  fog,  cloud’.  See nebula.
Neptunian,  adj.,  1)  pertaining  to  Neptune;  2) formed  by  water;  3)  pertaining  to  the  planet Neptune.  —  See  prec.  word  and  -ian.
Neptunist,  n.,  an  adherent  of  the  now  obsolete view  that  the  action  of  water  had  an  important part  in  the  formation  of  rocks.  —  Sec  Neptune and  -ist.
neptunium,  n.,  a  chemical  element.  —  ModL., coined  by  E.  M.  McMillan  of  the  University  of California  fr.  L.  Neptunus  (see  Neptune  and chem.  suff.  -ium).  He  called  this  element,  which lies  beyond  uranium,  after  the  planet  Neptune, because  the  orbit  of  this  planet  round  the  sun lies  beyond  that  of  the  planet  Uranus.
Nereid,  n. ,  l )  a  sea  nymph ;  2)  (not  cap.)  any  mem¬ ber  of  the  genus  of  worms  called  Nereis.  —  L. Nereis,  gen.  Nereidos,  fr.  Gk.  Nr(pr;  15,  NvjpEt?, gen.  N/;p7)'f8o5,  N^pEiSop,  lit.  ‘a  daughter  of Nereus’,  fr.Nrjpcuc.  See  Nereus  and  3rd  -id  and cp.  aneroid.
Nereis,  n.,  a  genus  of  marine  worms  (zool.)  —  L., fr.  Gk.  Nrjpirjt?,  na
```


## [2026-09-07T18:23:15.452Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nebh\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-07T18:23:15.499Z] TOOL RESULT

```
136:Conceptions of the sky, heaven, were var- ied in the different dialects. As we have seen, the root deiw- occurs widely as the divinized bright sky. On the other hand, certain lan- guages viewed the heavens as basically cloudy; nebh- is “sky” in Balto-Slavic and Iranian, but “cloud” elsewhere. Another div- inized natural phenomenon is illustrated by the root (s)tene-, “thunder,” and the name of the Germanic god THOR.
775:nebh-
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
801:ombh-ro-. Rain. 1. Zero-grade form *mbh-ro- in Latin imber, rain: IMBRICATE. 2. Possibly zero-grade suffixed form *mbh-u- in Latin imbuere, to moisten, stain: IMBUE. See nebh-. [In Pok. 2. (enebh-) 315.]
1907:NEB _ nabja- NEBULA nebh- NEBULOUS nebh- NECESSARY ked- NECK ken-5 NECRO- nek-1 NECROMANCY negw-ro-, nek-1 NECROPOLIS pele-3 NECROSIS nek-1 NECTAR nek-! NECTARINE nek-1 NEE gene-
1908:NEED nau-! NEEDLE (s)né- NEFARIOUS dhé-1, ne NEGATE ne NEGLECT leg-1, ne NEGLIGEE ne NEGOTIATE ne NEGRO negW-ro- NEIGHBOR bheue-, néhw-iz NEITHER kWo-, ne NEKTON sna- NEMATO- (s)né- NEMESIS nem- NEO- newo- NEOGAEA gé@ NEON newo- NEONATE gene- NEOPHYTE bheue- NEOTERIC newo- NEPENTHE kWent(h)-, ne NEPHELINE nebh- NEPHELOMETER nebh- NEPHEW nepdot- NEPHOLOGY nebh- NEPHRO- negWh-ro- NEPOTISM nepot- NEREID nere- NEREIS nere- NEREUS nere- NERITIC nere- NERVE (s)neou- NESCIENCE ne, skei- NESS nas-
1914:NIBBLE ken-2 NICE ne, skei- NICHE nizdo- NICKNAME aug-? NICTITATE kneigh- NIDDERING nei- NIDE_ nizdo- NIDIFY dhé-1, nizdo- NIDUS nizdo- NIECE nepot- NIELLO negW-ro- NIFLHEIM nebh-, tkei- NIGGARD_ ken-2 NIGH néhw-iz NIGHT nekw-t- NIGHTINGALE ghel-1 NIGHTMARE mer-2 NIGRESCENCE neg¥-ro- NIGRITUDE neg¥-ro- NIGROSINE negW-ro- NIHILISM ne NIHILITY ne
1919:NIMBLE nem- NIMBUS nebh- NIMIETY ne
```


## [2026-09-07T18:23:23.767Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"NEPTUNE\\|Neptun\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T18:23:23.809Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:23:30.099Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T18:23:30.104Z] TOOL RESULT

```


```


## [2026-09-07T18:23:35.618Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9b%CA%B0os",
 "prompt": "Give the reconstructed form, meaning, and the full list of descendants (Indo-Iranian: Sanskrit, Avestan; Iranian: Middle Persian, Persian; Latin, Greek, Slavic, Hittite), plus any notes on the root *nebʰ- and related forms like *n̥bʰrós."
}
```


## [2026-09-07T18:23:38.123Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%DA%A9",
 "prompt": "For the Persian entry نمک (namak): give the full etymology (Middle Persian form, Proto-Iranian reconstruction, any Avestan form cited, cognates such as Sogdian, Khwarezmian, Ossetian), and any cited authorities (Hasandust, Cheung, MacKenzie)."
}
```


### [2026-09-07T18:23:41.182Z] TOOL RESULT

```
# Proto-Indo-European *nébʰos

**Reconstructed Form:** *nébʰos (neuter noun, oblique stem *nébʰes-)

**Meanings:**
1. Cloud
2. Mist, moisture

**Etymology:** Derived from "*nebʰ-" ("to become damp, cloudy") plus the athematic nominative suffix "*-os". In derived terms, the meaning shifts to "sky" or "heaven."

**Major Descendants:**

- **Sanskrit:** From Proto-Indo-Iranian *nábʰas
- **Avestan:** From Proto-Indo-Iranian *nábʰas
- **Greek:** νεφέλη (nephélē) from Proto-Hellenic *nepʰélā
- **Latin:** nebula from Proto-Italic *neβelā
- **Hittite:** From Proto-Anatolian *nébos
- **Old Armenian:** ամպ (amp), ամբ (amb)
- **Slavic:** From Proto-Balto-Slavic *nébas

**Root *nebʰ-:** This root connects to atmospheric phenomena. The related form "*n̥bʰrós" appears in the related terms section, representing an alternative vocalization of the root.
```


### [2026-09-07T18:23:43.454Z] TOOL RESULT

```
# Etymology of Persian نمک (namak)

Based on the Wiktionary content provided, the etymology information is limited:

**Middle Persian origin:** The entry states the word comes "From Middle Persian _𐫗𐫖𐫏𐫍𐫐_ (namak)."

Unfortunately, the webpage does not include:
- Proto-Iranian reconstructions
- Avestan forms
- Cognates (Sogdian, Khwarezmian, Ossetian)
- Cited authorities or linguistic references (Hasandust, Cheung, MacKenzie)

The entry only documents the direct Middle Persian ancestry and shows modern descendants in Assamese, Bengali, Gujarati, Hindustani, and Punjabi. For deeper etymological analysis beyond the Middle Persian stage, you would need to consult specialized historical linguistics sources not present in this dictionary entry.
```


## [2026-09-07T18:23:48.350Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85",
 "prompt": "For the Persian entry نم (nam) \"moisture/damp\": give the full etymology chain (Middle Persian form and spelling, Proto-Iranian, PIE root), cognates, and any authorities cited."
}
```


## [2026-09-07T18:23:50.270Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%AA",
 "prompt": "For the Persian entry نفت (naft) and any Arabic نفط entry: give the full etymology (Middle Persian, Old Iranian/Avestan napta-, PIE root), the Greek naphtha / Akkadian napṭu connection and direction of borrowing, and authorities cited."
}
```


### [2026-09-07T18:23:55.874Z] TOOL RESULT

```
# Persian نم (nam) Etymology Chain

**Middle Persian Form:**
"𐭭𐭬" (nam)

**Etymology Chain:**
The word derives from Proto-Iranian *nábah, which comes from Proto-Indo-Iranian *nábʰas, ultimately from the Proto-Indo-European root *nébʰos ("mist/cloud").

**Cognates:**
The page lists descendants across multiple languages including Azerbaijani nəm, Hindustani (Hindi नम nam / Urdu نَم nam), Kyrgyz ным nım, Ottoman Turkish نم (nem), and Uyghur نەم (nem).

**Authorities Cited:**
The etymological information appears to cite scholarly reconstruction of proto-language forms, though no modern linguistic authorities are explicitly named in the entry's etymology section for the Persian word specifically.
```


### [2026-09-07T18:23:57.964Z] TOOL RESULT

```
# Etymology of نفت (naft)

Based on the Wiktionary content provided, here's the documented etymology:

## Persian Origin Path

The Persian نفت (naft) derives from **Middle Persian** (npt' /naft/, meaning "moist, damp; naphtha"), which traces back to **Old Persian** *naftah ("naphtha").

## Language Transmission

The word traveled through multiple language families:

- **Ottoman Turkish** adopted it directly "from Persian"
- **Russian** received нефть (neftʹ) from Ottoman Turkish
- **Multiple Turkic languages** (Kyrgyz, Tatar, Uzbek) borrowed from Russian
- **Armenian, Azerbaijani, Gujarati, and Urdu** all borrowed from Persian sources

## Related Terms

The Wiktionary entry notes "See also" references to Arabic terms (نقب, تفت, ثقب), though the page doesn't elaborate on potential Semitic connections or discuss the Greek "naphtha" relationship the prompt requests.

**Limitation**: The provided content lacks detailed discussion of "Greek naphtha / Akkadian napṭu connection" or broader Indo-European etymological analysis you've referenced.
```


## [2026-09-07T18:24:07.780Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/naphtha",
 "prompt": "Give the full etymology entry for naphtha, including the Greek, Persian, and Semitic/Akkadian discussion."
}
```


## [2026-09-07T18:24:08.611Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Neptune",
 "prompt": "Give the full etymology entry for Neptune, including any statement about the origin of Latin Neptunus (PIE *nebh-, *nept-, or unknown)."
}
```


### [2026-09-07T18:24:12.794Z] TOOL RESULT

```
# Etymology of Naphtha

The word naphtha entered English around the 1570s through Latin and Greek sources. According to the Online Etymology Dictionary, it derives from "Greek _naphtha_ 'bitumen,' perhaps from Persian _neft_ 'pitch,' or Aramaic (Semitic) _naphta, nephta_," though the document notes these potential source languages "could as well be from Greek."

The term appeared in Middle English as _napte_ during the late 14th century via Old French _napte_, but the modern usage represents a reintroduction of the earlier form. Historically, ancient writers used naphtha to describe "a more fluid and volatile variety of natural asphalt or bitumen." In contemporary usage, the term refers to a "colorless inflammable liquid distilled from petroleum."

The word's exact origin remains uncertain, with competing theories about whether Greek, Persian, or Semitic languages provided the root, creating etymological ambiguity about its ultimate source.
```


### [2026-09-07T18:24:14.763Z] TOOL RESULT

```
# Etymology of Neptune

The name Neptune enters English in the late 14th century from Latin *Neptunus*, the Roman god of the sea. According to etymonline, the Latin origin "probably" derives from the PIE root *\*nebh-* meaning "cloud," connected to Latin *nebula* ("fog, mist, cloud"), via a sense development toward "moist, wet."

**Key historical points:**

The planet Neptune was discovered by German astronomer Johann Gottfried Galle on September 23-24, 1846, and named by French astronomer Urbain Le Verrier, who had mathematically predicted its location based on irregularities in Uranus's orbit. Though invisible to the naked eye, it had been observed telescopically since Galileo's time, though not recognized as a planet until its formal identification.

**Related terms:** The etymology page also documents *Neptunian* (1650s, theological/geological usage) and *neptunium* (1941, the chemical element named for its position in the periodic table following uranium, mirroring Neptune's position beyond Uranus in our solar system).
```


## [2026-09-07T18:24:23.921Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA (Asbaghi)\"; grep -n -i \"naft\\|nafṭ\\|نفط\" PLA*.txt 2>/dev/null | head -10; ls | grep -i pla; echo \"=== AFM (Addi Shir)\"; grep -n \"نفط\" AFM.txt AFM_pages.txt 2>/dev/null | head -5; echo \"=== LKT\"; grep -n -i \"naphtha\\|Naphta\" LKT.txt | head -5; echo \"=== FVQ\"; grep -n -i \"naft\" FVQ_pages.txt | head -5"
}
```


### [2026-09-07T18:24:24.008Z] TOOL RESULT

```
=== PLA (Asbaghi)
(eval):1: no matches found: PLA*.txt
=== AFM (Addi Shir)
AFM_pages.txt:2129:اي اتح كل اليا حتت مكل ܢ تشبه.رائحة النفط» ,
AFM.txt:3466:اي اتح كل اليا حتت مكل ܢ تشبه.رائحة النفط» , 
=== LKT
2771:'Schmutz',  dazu  Adj.  kirli  'schmutzig' [vom  Stamme  kir  'schmieren,  Farbe, Schmutz'  Vämbery  TktEtWb  S.  89, Nr.  92];  hieraus  bulg.  kir  'Sehmutz  am Körper',  kirliiv  'schmutzig',  russ.  kir 'mit  Naphtha  getränkte  Erde'.  [Bern SlEtWb  505.
3547:'Erdpech,  Naplitha'  (Horn  NpEt  S.  23'2, Nr.  103Ö],  ar.  naft  [der  Wurzel  nafata 'sieden,  wallen'  anfrepaßl;  nachZAkkFW (iO  jedoch  ülier  aram.  napfä  aus  ass. naptu  'Erdöl'],  Ik.  na/t,  neft;  hieraus gr.  vctqpöa  [ngr.  tö  vd9Ti],  lat.  naphtha und  sp.  nafta,  frz.  naphte,  rum.  7iafta, naft;  luss.  neft';  dtsch.  Naphtha  'Erd- pech, Petroleum'.  [Gorjajew  228.  Löbel EITAP  68.  Eguilaz  462.
5852:3^a&ofe  1542 Nadir  1565 Nankint'gJ  1554 Naphtha  1538 J^a/-(/e  1548 Natron  1567 JV^afscfe  1530 Neschires  j.  127 iST/if/r/M  1569 Nirwana  1573 Nischan  1574
7440:naphtha  1538 wj^er  1568 nitrum  1567 nucha  1579 nuphar  1570
=== FVQ
2561:3 All those given by Cheikho, Nafttfinlya, 230, are doubtless influenced by Qur'anic
12358:Naftaraiai 27
```


## [2026-09-07T18:24:36.478Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB nem/abr/namak\"; grep -n \"nem \\|namb\\|abr \\|namak\" HUB.txt | head -12; echo \"=== CHEUNG nab/nam\"; grep -n \"^\\*nab\\|^\\*nam\\|nab- \\|namb\" CHEUNG.txt | head -12"
}
```


### [2026-09-07T18:24:36.534Z] TOOL RESULT

```
=== HUB nem/abr/namak
50:seinem Grundriss der neupersischen Etymologie (Strassburg
818:Nach Noldeke ist vabr 'Klippdachs* „wohl echt
830:zuriickgehen und einem np. *vah' entsprechen wurden
1036:schen nur *babr entsprechen wiirde (vgl. Nr. 181) nichts
1766:I, p. 496. Man miisste mit einem idg. kerk^s als
1903:im Phi. also wohl xrdsTtan, Aber auch aus einem alteren
2457:„plene geschriebenem i bezw. e" auch Ganjeshayagan
2470:jaunem geh5rt wohl nicht hierher.
3130:1 m ae) katnal gelesen werden und entsprSche dann einem ap. ^kamarda-
3481:und zwar von einem Praesensstamm man- (3. sg.
3484:224) von einem Praesensstamm men- (3. sg. phi.
3526:da nur menuk einem ap. *fnamyu' = zd. mainyu-
=== CHEUNG nab/nam
4476:throw’ leaves so little or no unambigous traces in (Dlr. / IE. Perhaps, this may be 
9056:haécat.aspa- (Y 46.15, Y 53.3); Inf.: YAv. hixtaiiae(-ca) ‘to moisten, [BMP transl.] /namb kardan/’ (V 
18231:*nab ‘to make wet, moisten’ 
18246:(*nambV-), Awrom. nim ‘damp’ (< Kurd. ?), Gz. nám-o-nà ‘wet’ 
18249:moisten, make wet’, Pash. nund, numd ‘wet’, Pash. naw (m.), Sh. namb ‘moisture, 
18489:*nam ‘to bend, bow’ 
18553:*namH ‘to strike, beat’ 
47947:namb, 276 
55617:*namH, *pais (s.v.), *skard 
55789:*nam, *suaH (s.v.) 
57194:*nab
```


## [2026-09-07T18:24:39.324Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18225,18265p' CHEUNG.txt"
}
```


### [2026-09-07T18:24:39.370Z] TOOL RESULT

```
276 *nab 


N 


*nab ‘to make wet, moisten’ 

*AVESTAN: YAv. napía- (ppp.) ‘moist, wet’ || (+ *abi-) YAv. aiBi.naptim 
*moistening' (V 7.12 f.) 

*MIDDLE PERSIAN: BMP nmb ‘moisture’, MMP npt ‘moist, damp, naphtha’, BMP 
npt /naft/ ‘moist, damp; naphtha’ Ò Also Akkad. naptu ‘naphtha’! > DMMPP: 244a 
*PARTHIAN: "nf ‘moist, damp; naphtha’ > DMMPP: 244a 

*KHOTANESE: (+ *à-) ? anahà ‘moistened’ 

*SOGDIAN: BSogd. nßt’k, nBtk, MSogd. nBtyy, nBtyy, SSogd. "ntc" (f.) ‘moist’ 
*CHORESMIAN: nfdk, npc, nBdc (f.) ‘moist, humid’ 

*NWIR: NP namidan/nam- (denomin.) ‘to grow moist', Kurd. nim ‘dampness’ 
(*nambV-), Awrom. nim ‘damp’ (< Kurd. ?), Gz. nám-o-nà ‘wet’ 

*NEIR: Sangl. nav-, Yi. nov-/nivd, M. nav-, niv-/nivd- ‘to rain’, Wa. пыу-/поуа ‘to 
moisten, make wet’, Pash. nund, numd ‘wet’, Pash. naw (m.), Sh. namb ‘moisture, 
humidity’, Sariq. nom ‘wet, moist’ 

*SANSKRIT: abhrá- ‘cloud’ (RV+), nábhas- (n.) ‘moisture, cloud, mass of clouds, 
mist’ (RV+) > EWAia I: 94, II: 13 

© The verbal forms of *nab are attested in some Pamiri languages. 

«PIE *neb'- ‘to moisten, be wet’ > LIV: 448 | Pok.: 315 f. 

*IE COGNATES: Gr. ovvvé get, Extveger ‘is cloudy, clouded; [Zeus] makes cloudy, 
clouded’, Hitt. /nepis-/ (n.) ‘sky’, Gr. уёфос (n.) ‘cloud, mass of clouds’, OCS nebo, 


nebes-e (n.) ‘heaven’, OHG nebul (m.), NHG Nebel, etc. 
*REFERENCES: EVP: 52 f.; IIFL II: 233b, 532a, 405b; MacKenzie 1966: 103; MacKenzie, Pahlavi: 57; 
EVS: 49a; WIM 1/2: 709 f.; DKS: 18b; Steblin-Kamenskij 1999: 252; NEVP: 59
```


## [2026-09-07T18:24:48.601Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN salt\"; grep -n \"namak\\|nemek\" SYN.txt | head -6; echo \"=== SYN cloud/abr\"; grep -n \"Pers. abr\\|abr, \" SYN.txt | head -6; echo \"=== IEC nebhos\"; grep -n \"nebhos\\|nebhelā\\|nembh\\|mbhro\" IEC.txt | head -8"
}
```


### [2026-09-07T18:24:48.684Z] TOOL RESULT

```
=== SYN salt
=== SYN cloud/abr
=== IEC nebhos
3677:-es- alternating with n.a.sg. -os, pl. -eso, a neuter type of "universal" aspect: see menos, 2enos, nebhos, quelos, ieuos, etc.
4492:gumbhros (gumuros) *mass'. Cf. gumb-, etc. MHG kumber, kummer ‘rubbish’; G Kum- mer, id. (and ‘rubble’); Frisian: kommer ‘hare’s droppings’; Li. gumbras, gùmuras ‘Jump’
5653:ĝenos (2) -es-, n. type “race, kind, tribe’. WP I, 576 Skt. jánas; Gk. génos; lat. genus; Olr. gein, n. ( birth", but ambig.); W gên, pl. genoedd (life, soul, intellect; pl. -oedd as in nefoedd, *heav- ens”, fr. *nebheso, see nebhos). As part ofa cpd. cf. Arm. -cin, Lat. -genus; Gaul. -geno-; Olr. -gan (Eogan: OW Owein); OCS cf. ljubí-znü “dear, friendly”
5837:$ombhros, is "a horned animal, bison’. Cf. $ombhos, 3embh- Thrac. zómbron, acc. sg. ‘bison’; Byzantine Gk. id. as LW; OCS zobri, m. id.; Cz. R zubr, id. (Here also isophonic ON gambr, gambrs gs.; gammr, gs gammrs ‘vulture’; Li. Zambris *plowshare? if the general sense is ‘horned, spiked’)
9896:list- (listis) — Imbhro, ió
9912:Imbhro, ið “flop, lumber Oss. lábirín, láburun ‘collapse’; WG, LG lum- mern ‘lounge, idle’; cf. lummer, adj. “ponde- rous, lumbering’; ME lomeren, v.; E to lum- ber; Icel. lumbra, v. ‘pound, browbeat’. Cf.
11502:mbhros, is ‘cloud, vapour, drizzle’. WP I, 131. (ambig. cf. əmbros, is) Skt. abhráh, m. “rain-cloud'; Av. awrom, n. "Cloud: Per. abr, id. beside abar ‘fog’; Oss. arv ‘sky’ (Abaev); Gk. aphrós, m. ‘foam’; Lat. (prob.) imber, gs imbris, m. (ambig.) ‘rain’
11569:nebholos, à ‘mist, cloud’. WP I, 131. See nebhos. Variants: nebhul-, nebhel- Gk. nephélé ('cloud'. e fr. stem of nephos, -e-); Lat. nebula, id.; Olr. nél, néll, Ir. néall, m. ‘cloud’; W cf. nifwl, niwl, pl: -oedd, m. (fog, fr. a variant *nebhul-); cf. also nyfel, m. (ether, fr. *nebhél-); OHG nébol, nëbul, MHG nébel, sm. “cloud, darkness’; OE nifol ‘dark’; ON nifl-, cpds. ‘mist? (vocalism ob- scure, perh. fr. *nebhlu-)
```


## [2026-09-07T18:24:55.742Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^nebhos\\|nebhos, \\|nembhos\\|nemb-\\|nembh\" IEC.txt | head -8; echo \"---\"; sed -n '11570,11580p' IEC.txt"
}
```


### [2026-09-07T18:24:55.800Z] TOOL RESULT

```
3677:-es- alternating with n.a.sg. -os, pl. -eso, a neuter type of "universal" aspect: see menos, 2enos, nebhos, quelos, ieuos, etc.
11570:nebhos, -es- ‘sky, cloud, mist’. WP I, 131 Skt. nábhas, n. 'sky, mist, cloud'; Hitt. nepis, gs nepisas (for *nebes, nebesas 'sky); Gk. néphos, gs: -eos, n. "doud: Lat. cf. neb-ula, f. id. beside nimbus (if for *nenebhos); cf. Olr. nem, gs: nime (sky, heaven’. Etym. as Lat. nimbus or fr. *nebhmn-, cf. W nen, pl: -oedd, f. ‘vault of heaven; ceiling); W nef, pl: -oedd, f. ((heaven', phonol. *nebh- or as Ir.); Br. nef, énv, pl: -u, m. ‘sky’; Cor. cf. nev- ek-, adj. ‘heavenly’; MW also nefedd, pl. “hea- vens’; OCS nebo, gs: -ese, n. Cake heaven” and com. S1.); R nébo and (pl. form) nebesà, id. beside nébo (njobo ‘palate’). For Lithuan. debesys, gp: debesų, m., debesis, -iés, f. “cloud? and Latv. debess, gs id. ‘sky’; debesis "Cloud cf. the synth. cpds in Gk. dnóphos ‘dusk’ beside knéphas, gs: -ous, ds: -aj & -ei, id., of uncertain composition, but cf. (zero- grade form of) prefixes *de- and *eKs-. Cf. Li. devyni in relation to dësimt ‘9:10
11785:nobhesos (nebhos, -es-?) ‘centre-bit of drill (9). Cf. nobh- above ON nafarr, ds: nafri, m. *gimlet'; Cz. nebozez, id.
---
nebhos, -es- ‘sky, cloud, mist’. WP I, 131 Skt. nábhas, n. 'sky, mist, cloud'; Hitt. nepis, gs nepisas (for *nebes, nebesas 'sky); Gk. néphos, gs: -eos, n. "doud: Lat. cf. neb-ula, f. id. beside nimbus (if for *nenebhos); cf. Olr. nem, gs: nime (sky, heaven’. Etym. as Lat. nimbus or fr. *nebhmn-, cf. W nen, pl: -oedd, f. ‘vault of heaven; ceiling); W nef, pl: -oedd, f. ((heaven', phonol. *nebh- or as Ir.); Br. nef, énv, pl: -u, m. ‘sky’; Cor. cf. nev- ek-, adj. ‘heavenly’; MW also nefedd, pl. “hea- vens’; OCS nebo, gs: -ese, n. Cake heaven” and com. S1.); R nébo and (pl. form) nebesà, id. beside nébo (njobo ‘palate’). For Lithuan. debesys, gp: debesų, m., debesis, -iés, f. “cloud? and Latv. debess, gs id. ‘sky’; debesis "Cloud cf. the synth. cpds in Gk. dnóphos ‘dusk’ beside knéphas, gs: -ous, ds: -aj & -ei, id., of uncertain composition, but cf. (zero- grade form of) prefixes *de- and *eKs-. Cf. Li. devyni in relation to dësimt ‘9:10
nebhül-, nebhüt- ‘non-existent’. Cf. bhü-, ne- Lat. nebulo, gs: -onis (rogue, worthless per- son’; OCS nebyli, m. "a nobody, un-person'; Pol. niebyty, adj. ‘non-existent, without pre- cedent'. Cf. also Per. nabüd ‘non-existent; Li. nebütas, id.; Latv. nebüte ‘non-existence’
(ne-dhla, notional variant of type nétr-, see nëið & nétis, us. OE nædl, f. ‘needle’; OFris. nedle, nēlde; Fris. naeld; MDu. naalde, f. id.; ON nál, f. id.; but Go. népla; Anglian nepl, f. & OHG nadala indicate a variant of type *netla)
neg (negi, negu, -o) a sentence-particle. Cf.
831
ne, ge OS nek ‘or’; OFris. naka ‘while; as soon as’; OCS nego, neZe, negü, cj. or than; OCz. než “than'; Srb. nego ‘but; than’; Li. nèg, négi, négu ‘so; tham’; Latv. nedz ‘nor’
negh- (negh-?) ‘bind’. Evidence ambig. Skt. nahyàmi, v. id.; Av. naz-, id.; Per. cf. naž ‘wards of a key” (?); Srb. cf. (?) negve ‘fetters’; ON cf. nist, n. brooch’, if fr. *neghst-, but WH and Kluge otherwise, see necto, Nestel); Lat. extn. in necto, pf. negt, sup. nexum ‘bind’ beside nexus, nexa ‘join’. O-gde prob. in OHG *nastila, actually nestila, f. & nestilo ‘bang’. (FK:EWDS: Nestel improb.)
negu, see nég
negum- (?) ‘unseemly, naked'. Variant: n- gum- Hitt. cf. nekumanc- ‘naked’; Gk. (aphetic?) gumnós, id. (phonol. of guné, kúklos. Here, unless gumnós = 'comely'?; cf. OE cyme ‘comely’: Gk. ganós?); MHG cf. unkome 'awk- ward": OE uncyme ‘uncomely, unseemly'. The background of Skt. nagnáh & of OE nacod, etc. is uncertain. Cf. nogud-, etc.
neguhros, ó(n) (reguhnos, õn) ‘kidney’. WP I, 134 Gk. nephrós, m. id.; Praen. nefrones, pl. id.; Lat. dial. cf. nebrundines, pl. id. (synth. cpd.?); beside Lat. renés, pl. (w. metath.); OHG nioro, wm. id. (& ‘testicle’); G Nieren, pl. id.; Sw. njure, wm. sg. id.
nei “neither, nor'. WP II, 320. Cf. ne, ei Boeot. Arc. nei “indeed, yes? (a formal equi- valent, but semantics obscure, cf. Mod. Gk. nai yes); Cypr. ni. .. .ni... ‘neither. . .nor'; N. Alb. ne, ne, ., id.; OLat. nei, Lat. ni ‘f not, unless, that. . .not'; Osc. & Umb. nei ‘no’; Go. nei ‘not’; OHG ni, ON ní ‘no’; OCS and com. Slav. ni “neither; nor; Li. Latv. nel. . .nel. . ., id.
```


## [2026-09-07T18:25:01.269Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i \"wld\\|walde\"; echo \"===\"; ls incoming | head -30"
}
```


### [2026-09-07T18:25:01.325Z] TOOL RESULT

```
WLD_band3.txt
===
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-07T18:25:04.562Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; echo \"=== band3 grep\"; cd .. && cd .. && grep -n \"nebh\\|nembh\" WLD_band3.txt | head -10"
}
```


### [2026-09-07T18:25:05.921Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
=== band3 grep
3099:misten Lome 247%. | mindern 5. mei- 242°, | Nabel [. (enebh-), ee «ada gete. | ukthen | Pe a0 h Grtl ypeiges se ii no", mek’. 244*, wee ? magern gerk’=) gork'- |. mili- dua- B16. nad be blon depd- T74- 20. miBhandeln aslfge- 714%. | nac wl fend AST*. tahken 5,al- 80. Mist equ. 381, | nach fagh- 195
3107:Nebel 2. (enebh-) 131, | Ohr _ s 18, is 408,
```


## [2026-09-07T18:25:09.911Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"napta\\|namb\\|awra\\|abhra\" WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-07T18:25:09.972Z] TOOL RESULT

```
11851:tholomae Airan. Wb. 92), napta- „feucht u npers. neft „Naphta“ Lit. iiber      ,
11867:      mbh-: ai. abhra- m. „triibes Wetter, Gewolk“, n. „Wolke, Luftraum“,
11868:av. awra- n.                             „Wolke u   ,
25360:       Ai. urabhra- m. .,Widder“ (d. i.
35040:                             (Perssons Beitr. 195 Yerbindung   mit ai. f cabhra                                                  m. n. „Erd-
79684: dipsati (=a y. diwz-, s. u.), dabhra- „wenig, gering, dfirftig";
79728:gr. toipos „lockere Steinart, Tuff" trotz der Berufung auf ai. dabhra-
```


## [2026-09-07T18:25:13.573Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '11820,11890p' WLD_Bd1_pages.txt; echo \"=== find page tag\"; awk 'NR<=11851 && /\\[pdf page/ {n=NR; v=$0} END{print n\": \"v}' WLD_Bd1_pages.txt; grep -n \"131\" WLD_Bd1_pages.txt | awk -F: '$1>11700 && $1<11900' | head"
}
```


### [2026-09-07T18:25:14.892Z] TOOL RESULT

```
(n. ts-St.\ nir. neamh, cymr. corn, ncf „Himmel ‘, zum /-St. umgebildet
                                                                                      L




in lit. debes'is „Wolke u (aber Gen. PI. debesu !) {d fur n nicht Folge des Er-
satzes  von *nevynl „9“, vgl. apr. nnvints „der neunte“, durch devyn'r,
eher wird EinfluB von dangiis „IIimmel“ mitgewirkt baben. Uhlenbeck
Ai. Wb. 143; gewiB nicht aus *d-ncbesis mit (/-Vorschlag: viepog dvotpog,                                            :




Meringer SBAkWien 125, 11 40, Schrijnen KZ. 42, 104).
   Gr. vscpeh] „Volke, Nebel“, lat. nebula „Dunst, Nebel“ aber air. ml m.,                            ;


gen. nittil „Wolke, Nebel“ nicht aus hiebhle-, sondern nach Pokorny KZ.
50, 46 Lehnwort aus cymr. niwl, niftvl, ncorn. niul ds. (die wiederum
nach Loth Rc. 20, 346 f. Lw. aus lat. nibulus ftir uubilus        ahd. uebul                                   ) ;


„Nebel“, as. nehal „Nebel, Dunkel“, ags. nifol ds., aisl. nifl-heimr u. dgl.),
njol „Dunkelheit, Nacht“ (germ. *nebla- und *nitnda- aus - e lo-: aisl. nifl-
aus *nitila~).
    Ai. nabhanu- m., nabhand f. wahrscheinlich „Quelle a (andere mit nabh-
beginnende Nomina sind in der Bed. noch unsicherer, s. auch u. nebh-
„bersten“); av. aiwinaptJm asti „er (befeuchtet =) besudelt mit Blut“ (Bar-
tholomae Airan. Wb. 92), napta- „feucht u npers. neft „Naphta“ Lit. iiber      ,


diese nicht wahrscheinlicher auf sna-, sn-ip- „flieBen“ bezogenen Worte
                                               r
s. u. sna -)  dehnstufig ai. nubhah f. pi. „W olken“ (nach J. Schmidt PI.
                         ;


1 4 5 f Anm.
        .        aber lat. niibes zu sneudh-).
                                     1    ;




      mbh-: ai. abhra- m. „triibes Wetter, Gewolk“, n. „Wolke, Luftraum“,
av. awra- n.                             „Wolke u   ,
                                                        gr. dcpqog   „Schaum“ in die i-Decl. iibergetreten lat.
's.   W. Meyer KZ. 28, 174)                                    imber, hubris„RegenguB“         —
                                                                                           osk. anafrhs wohl
„imbribus“ (Bugge KZ. 2, 386, v. Planta I 320, 455, Vf. LEWb. 2 s. v.                                                          .




Hierher auch die FluBnamen gall. Ambris, cymr. Ambyr, Amir, Amyr
(Fickll 4 16), sowie Amper (NebenfluB der Isar) und Emmcr NebenfluB der                                    i




Weser die gegen Meringer DLZ. 1915, 449 als kelt., nicht germ, anzu-
             1

                 ,



sprechen sind. Vgl. ohne formantisches r gall, inter ambes „inter rivos“,
=== find page tag
: 
11787:    Curtius 294, Schmidt KZ. 23,270, Hirt Abl. 131, Meringer WS. 5, 82f.
11804:                                                                      enebh-                                             131
```


## [2026-09-07T18:25:18.961Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '11890,11925p' WLD_Bd1_pages.txt"
}
```


### [2026-09-07T18:25:19.008Z] TOOL RESULT

```
sprechen sind. Vgl. ohne formantisches r gall, inter ambes „inter rivos“,
ambe „rivo“, abrit. Amboylanna „Ufer des Stromes (Fick II 4 16: wohl                          -1




urspriingliche Beziehung zu *ab-, *a/>- „Wasser“, s. Vf. LEWb. 2 u. amnis',
sowie arm. amb und mit idg. b) amp „Wolke“ 'siehe Hiibschmann Arm.
St. I   1
          8, Arm. Gr. I 417'.
      Ganz unsicker deutet Johansson IF. 4, 145 Anm. 4                                             alb.   mbreme „ Abend
als *(a)mb(Ji)r-mc- „Tauzeit“.

      emb(h)-                :       ai.      ambhas- n. „Wasser“; ambit n. „AVasser“, gr. opfigog ,,Regen“
 zum b vgl. oben arm. amp; Scheftelowitz BB. 29, 41 will auch fur amp
mit idg. bh- auskommen, und als o-stufige Form auch amp „Trunk, Trank“,
ampeni „trinke“ anreihen?                                  .




      nembh-           nam, np. nem „feucht, Feuchtigkeit u pehl. nam-
                                 :       pehl. narnb,                                                            ,


bitan„befeuchten“, lat. nimbus  „Sturzregen, Platzregen; Sturmwolke,
Regenwolke    Horn Np. Et. Nr. 1039, Johansson IF. 4, 139f. Anm. 3;
                                     ;<
132                    eu(o)nien-, (o)nomen-, nomen-, e n(„)men-             — enos-, onos'

aber mir .nimb ,.Tropfen“, Fick I 4 193, stammt aus dem Lat., Osthoff IF.
4, 27b f.   .
```


## [2026-09-07T18:25:27.501Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/ARY; echo \"===\"; python3 -c \"\nimport json,os\np='incoming/ARY/ARY_headwords.json'\nprint(os.path.exists(p))\n\" ; ls ocr/ARY | head"
}
```


### [2026-09-07T18:25:29.095Z] TOOL RESULT

```
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
===
False
0051.png
0051.txt
0051.vision.txt
0136.png
0136.txt
0136.vision.txt
0153.png
0153.txt
0153.vision.txt
0291.png
```


## [2026-09-07T18:25:32.040Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نمک\\|^نم \\|ابر\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-07T18:25:32.095Z] TOOL RESULT

```
87:معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
113:ارتش و فناوری وگسترش از راه کوچگری را میسر نمود. بنابراین دیدمان (17733083) مردمان این
291:همریشه‌اند می‌توان نتیجه گرفت که آنان در رام کردن اسب و استفاده از ترابرهای چرخدار پیشگام
292:بوده‌اند و تحرکك و تفوقی که سوارکاری و ترابری به آنها داده عامل بزرگی در گسترش آنها بوده
431:اروپایی به ویژه زبان‌های کهن اروپایی وجود دارد. کمی بعد که به بررسی نوشتارهای کهن ابراني (به
544:باید به طور علمی و سامانمند بررسی و اثبات گردد. مثلاً آوای یونانی 2۳3 برابر است با آوای ژرمنی
560:واژه‌ی بنیادین را احیاکرد. مثلاً پس از تعبین برابرهای واژه‌ی «زمین» (سانسکریت: 4۵7۸8 یونانی؛ . ,
917:۱-برابری و اخوت.۲- رفتار نیمه جنونآمیز و سرمستانه هنگام نبرد یا تهاجم یا مراسم وابسته به
947:انلاق می‌شد که به زنی تجاو زکرده و لذا منفور است. بنابراین شاید بتوان نتیجه گرفت که در میان هند
1035:می‌شد. (برابرهای این واژه چنین‌اند - سانسکریت: ۷181۳۸77؛ لیتوانی: ‎٩۷18871۳۸75‏
1039:۸۸ ابر لندی کهن:117۸7؟ پروسی کهن: 0 فارسی: نوده). ظاهراً 1۸77۸" به
1052:ویژگی‌های ابر انسانی ضامن خوبی محصول و زایندگی دام‌ها و پر ماهی بودن رودها و فراوانی
1139:اندازه‌ای است که برخی از واژه‌ها و جمله‌های سانسکریتکاملاً مشاب پرابرهای اوستایی ود هستند.
1156:است)؛ پارتی (زبان مردم سرزمین‌های شمال خاوری فلات ابران)؛ ختنی (6107۸7388)»
1203:نمی‌دهند: ۱-برابر نمایی واژه‌های فارسی و دیگر زبان‌های ایرانی با زبان‌های اروپایی (مثلاً یونانی و
1228:دوم -برابریابی و تطبیق واژه‌های ایرانی با واژه‌های سانسکریت از یک سو و واژه‌های اروپایی از
1232:فهرست‌های آنها فاقد برابرهای فارسی نوین هستند. اصولاً پژوهشهای ایشان از دیدگاه یک زبان
1590:ابرنند 8381۸ ,1818 ,ت88 ,810شآ133) و در بت 13070 ,108 ساکن شدند و نام خود را به آن
1640:سانمکریت (54(/557): ۸۷1105 ,شتا هلدی (للع007). 6 ,۸65
2019:۲ آن (دریرابر ین)
```


## [2026-09-07T18:25:36.754Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l incoming/ARY/ARY_pages.txt incoming/ARY/ARY_latin_index_pages.txt; grep -n -i \"nebh\\|NEBULA\\|nimbus\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-07T18:25:36.806Z] TOOL RESULT

```
  16204 incoming/ARY/ARY_pages.txt
  15967 incoming/ARY/ARY_latin_index_pages.txt
  32171 total
2128:BARNHART: (NEBULA) 697 OBLAK SLOVAK) Sle
14566:NIFOL — {OLD ENGLISH) oy ,-J&i\ NEBULA LATIN) ops
14575:BARNHART: (NEBULA) 637 NEBE CZECH) Soy
14579:ONIONS: (NEBULA) 605
14580:SKEAT: (NEBULA) 397
```


## [2026-09-07T18:25:40.281Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14555,14590p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== which pdf page\"; awk 'NR<=14566 && /\\[pdf page/ {v=$0} END{print v}' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-07T18:25:41.672Z] TOOL RESULT

```
[Ra ReRTAN) |
NUBES SUTALIAN) ol} NABAH- HAVESTAN) leu!
NOR ARUMANIAN) gly) NAMNA, «(OLD PERSIAN) deol guj
NUVEM, PORTUGUESE) Js NABNA-
NEBULOSO NAM, NAMB, (PAHLAVI) 5.4,
OLD SCANDINAVIAN) 55-41-41) NAMBITAN
NIFLE, NJOL NEMI, NEM (RURDISH) 52
NEBLA — (OLD SAXON) pS gS» NAMB HBALUCHI) gr sh
MOLD HIGH GERMAN) pf gall NUMD, NUMD :(AFGHAN}) (4), gli
NEBULE NABHAS GANSKRIT) 4 Sule
NEBEL (GERMAN) gialT NEPHOS, NEPHELE = (GREEK) gli
NIFOL — {OLD ENGLISH) oy ,-J&i\ NEBULA LATIN) ops
NEVEL DUTCH) «sce NEBLEUX, NUE, (FRENCH) Wil
OLD CHURCH SLAVIC) ps3 NUAGE
NEBO, NEBESA NUBE, NEBULOSO (SPANISH) (plity!
[pdf page 500]
|
Or | ls
‘REFERENCES bok NIEBO POLISH) leg)
POKORNY, SSB NEBO ARUSSIAN) «ous
BARNHART: (NEBULA) 637 NEBE CZECH) Soy
DELAMARRE: —(NUAGE, NUEE) 187 DEBESIS LITHUANIAN) (ge)
MACKENZIE: (MOISTURE) 124 NEM, NEL (OLD IRISH) 4S 5.) ,\
BUCK: 10741075 NEPIS, NEPISAS (HITTITE) en
ONIONS: (NEBULA) 605
SKEAT: (NEBULA) 397
MALLORY: 6
vi tabi oby
Fast Loge Sag
leetlas |
OAT ne alia Saas 42 oy gulp =A |

{che SNAPTA 5 glee! NABHANU 2 SL Jel ately Geos jh "el sh easly oY |

eal ot Fob oly eat JINAPHTHA (583 gulp Las (NAPT :

=== which pdf page
[pdf page 499]
```


## [2026-09-07T18:25:52.119Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14500,14556p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-07T18:25:52.165Z] TOOL RESULT

```
SITAN, SAHISA (GOTHIC) SG, NIYASHADAYAM, (NI)SHASTA
(OLD SCANDINAVIAN) Sigh! NISHASTAN, (PAHLAVI) 53g
SITJA, SIT NISHEM
SITTIAN — :(OLD SAXON) 5 gip-S NISHIN KURDISH) 52,5
SITTA {OLD FRISIAN) eS 63.5 NINDAG, NINDAGH, :(BALUCHI) gz sh
(OLD HIGH GERMAN) 6 git NISHTAINAGH
SIZZEN, SIZZU NASTAL, NAS 4AFGHANI) (54) Jui!
SITZEN (GERMAN) glT S{DATI, SATTA (SANSKRIT) 24 St
SITTAN (OLD ENGLISH) 4S gl! NISTIM ARMENIAN) go
siT ENGLISH) gulSit HEZESTHAI, HEDARA, :(GREEK) gt.»
SIDDE (DANISH) Laila HEKTOS
SITTA (SWEDISH) (543 yo SEDERE, SEDES, ALATIN) 53
SITE HNORWGIANRS 33,5 SEDEO, SIDO
ZITTEN DUTCH) sala ASSEOIR (FRENCH) sil
SENTAR (SPANISH) glilyel
[pdf page 498]
FA | Gdns eta S
‘REFERENCES both, OLD CHURCH SLAVIC) eps 3%!
POKORNY, = SSS~*~*~*« SEDETI, SESTI
BARNHART: (SIT) 1011 SIEDZIEC APOLISH) lia)
DELAMARRE: (ASSEOIR) 255 SIDIET (RUSSIAN) gas,
MACKENZIE: (SIT) 133, (SEAT) 131 SEDET CZECH) Sy
BUCK: 833-834 SEDIET (SLOVAK) Jol
ONIONS: (SIT) 830 SEDETI, SEDU _ :(LITHUANIAN) ere)
SKEAT: (SIT) 565 SEST LATVIAN) (3) gi)
rite abt oly SESS HOLD IRISH) opS 545 p\
Jeetlaolk
pee AS GLa 22s oo
HUTA SWEDISH) (6.8 yo NIKOHIDAN, PAHLAVI) 6 3h
HUTA —_( os}(NORWGIAN) 15595 NIKOHISHN
PRZE- PRZY- (,ous}(POLISH) lng) KUTSA, (SANSKRIT) 2, Suites
PROKODITU HRUSSIAN) go3 KUTSAYATI
HOLD BULGARIAN) pS 6 554 CHUDAZO GREEK) gli y
KUZHDO, KUDITI OLD SCANDINAVIAN) 45542b\
UT OLD IRISH) gS 5.) HOTA, SKUTA.
OLD HIGH GERMAN) (pS gS), ‘4
"REFERENCES othe Hosc a
POKORNY, ——SS*~*« ING wut TR cenmany gist
‘MACKENZIE: (BLAME) 104 HUSC = (OLD ENGLISH) oS endSs
SKEAT: (HOOT) 276 HOOT ENGLISH) JS}
vist ebb cay HUJE s(DANISH) Shai!
deaths
125 22 2 sae g gry5 SUL 22 059 Gil pe“
Poo
[pdf page 499]
etl At) gaat jl ga SHOUT pK go5ly 2,2 Jl “1
a
: AKASAT, *NIKASA :(AVESTAN) ple)
‘REFERENCES beth NIKAS, NKAS, PAHLAVI) 5 shy
POKORNY =SS*S~*~S~*~S*~«S NIGAH, NIGARIDAN
MACKENZIE: (LOOK) 122 NEKA, (KURDISH) 52,
rier sabi olay NIKAH (GALUCHI) gx hu
KASTE, KASATE: (SANSKRIT) ey Sails
: ieetlosl
AST ry Fi,
[Ra ReRTAN) |
NUBES SUTALIAN) ol} NABAH- HAVESTAN) leu!
```


## [2026-09-07T18:25:59.990Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"NAMAK\\|SALT)\\|ABHRA\\|AWRA\\|ABR \" incoming/ARY/ARY_latin_index_pages.txt | head -12"
}
```


### [2026-09-07T18:26:00.037Z] TOOL RESULT

```
2112:SOMBRA SPANISH) gil AWRA, AWREM —(AVESTAN) yliy!
2113:OMBRA_ AUTALIAN) giSte\ ABR APAHLAVI) 6 hag
2117:EMMER ABHRA A(SANSKRIT) 4 Suile
3154:(OLD CHURCH SLOVIC) ip§5 5.9%! BAWRA, BAWRI—:(AVESTAN) .p\=!
3489:POKORNY, OSO*~CS~*~“CS:*«t WAWRA AFGHAN (3-4) gil
10038:ASTEMPHES GREEK) 3 y STAWRA, STMBHRA
10105:TJOR, TYR (NORWEGIAN) «5}4,: STAORA., STAWRA-:(AVESTAN) .gl-3!
```


## [2026-09-07T18:26:03.325Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2100,2135p' incoming/ARY/ARY_latin_index_pages.txt; awk 'NR<=2112 && /\\[pdf page/ {v=$0} END{print v}' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-07T18:26:04.520Z] TOOL RESULT

```
VER- GAULISH) SS (OLD SCANDINAVIAN) p652hes}
. YFIR
‘REFERENCES cathy HOLD SAXON) ff gipS le
POKORNY, —=~=~S~S*«wLOS 1106, UBAR, UVER
BARNHART: (OVER) 742 UVER, OVER :(OLD FRISIAN) 4S 53.3
DELAMARRE: (SUR, AU-DESSUS) 303 {OLD HIGH GERMAN) gS glasT
MACKENZIE: 1, (OVER) 126, UBAR :
(SUPERIROR) 135 UBER (GERMAN) AST
ONIONS: (OVER) 637 OFER — (OLD ENGLISH) oS 8)
SKEAT: (OVER) 418-419 OVER ENGLISH) gudS3t
A) Labi slay OVER (DANISH) Sails
OVER (SWEDISH) (645 yp»
SOMBRA SPANISH) gil AWRA, AWREM —(AVESTAN) yliy!
OMBRA_ AUTALIAN) giSte\ ABR APAHLAVI) 6 hag
UMBRA H(RUMANIAN) ley ) HAUR, EWR A(KURISH) 53,5
SOMOBRA —_— (PORTUGUESE) Js 5 HAUR ABALUCHI) gx
AMMER, AMPER, (GERMAN) gust ‘ORA AFGHAN (4) gla)
EMMER ABHRA A(SANSKRIT) 4 Suile
AMBER ENGLISH) gud AMB, AMP ARMENIAN) gal
OLD CHURCH SLAVIC) 55 53%! APHROS, OMBROS — (GREEK) (gly
OBLAKU IMBER, IMBRIS ALATIN) 3
OBLOK POLISH) ging) OMBRE (FRENCH) Wil},
[pdf page 76]
oa
WI szssyzl
: OBLAKO ARUSSIAN) «5+,
REFERENCES beth OBLAK (CZECH) Sx
= =
BARNHART: (NEBULA) 697 OBLAK SLOVAK) Sle
MACKENZIE: (CLOUD) 167 AMBRIA, CELTIC) ( gS) gh
BUCK: 3s AMBRA (GAULISH) iS
v4 igbi ob, AMIR, AMYR- WELSH) 69
ethos
Ge Desks Shabs 2 Js ctl eet
BY (A pel slay, pe Uae aly ol Gd9d Es hey AS y BUT hak 22-1
. sel ole
[pdf page 75]
```


## [2026-09-07T18:26:12.424Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,120p' SOURCE_MATRIX.md"
}
```


### [2026-09-07T18:26:12.461Z] TOOL RESULT

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
```


## [2026-09-07T18:26:19.550Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HENNING namak\"; grep -n \"namak\\|nmyhk\\|namadk\" HENNING_selected_papers.txt | head -8; echo \"=== LEW Neptunus\"; grep -n \"Neptunus\\|Neptünus\\|Neptüuus\" LEW_1910.txt | head -5; echo \"=== LAT Neptunus\"; grep -n -i \"neptunus\" LAT.txt | head -5"
}
```


### [2026-09-07T18:26:19.627Z] TOOL RESULT

```
=== HENNING namak
341:names of women contained -f'm(h), see the lists of the Makrndmay — (16) Prob. “not bearing sorrow, sans-souci”, n’ + Brt + tne +h, cf. n'Brtpenenyb, BBB. tns “sorrow”, or “nostalgia”, VJ., 323, 334, 366, 400, 1278; frag, ii (a), 6.—{17) “The ambrosial one.”—(18) “ Sweet-coloured ” rather than “ possessing immortal Iustre ”” (Arm, ‘anvil, etc.).—(19) The fourth letter is not properly exeouted, and looks like a cross between t and w, I cannot explain meyt'nch ; neeyte'nch would mean ‘free from failing ".—(20) “ The salty one.” ‘The reading is not quite certain in so far as the third letter might be ' (nm’3k-). ‘The Sogdian word for “salt” was hitherto unknown. Cf, the Eastern dialect forms as collected by Gauthiot, MSL., xix, p. 149; xx, pp. 5,19, who poses Olr.namddaka-. See further, Morgenstieme, ITFL., ii, register s.v. salt, and cf. Saka namea, nimva, ete., Bailey, BSOS., viii, p. 190, In unpublished Man, MPers. texts we have nmyhg, unfavourable to Gauthiot’s namddaka-. In fact, Gauthiot has only proved that the Olran. form was not namadéka-, and we are at liberty to assume Or, na/imadka- (or na/imadka-). For the final -k of NPers, namak one could compare NPers. mayak: Parth. mg’dg, see BSOS., ix, p. 85. There is every likelihood that Av. nomaBka Yt., xiv, 55, is also “salt” (why should the Vyamburas not have had the detestable habit of throwing salt into the fire in order to change its colour ? Av. aema- is “ the stuff which is thrown into the fire for the purpose of burning it", normally, of course, “fire-wood”),
=== LEW Neptunus
=== LAT Neptunus
13588:II est identifie avec le Neptunus equestris, cf. Serv. anet., Ae .8,635,
13590:turum proposuit... Iste Consus et eques Neptunus dicitur, unde etiam
40153:ponr la foraation Neptunus ^ PortGnus, Port&na et est sana donte le
41165:Neptunus, -i m.: Neptune; dieu marin. Usiti de tout temps; con¬
41170:vation de Neptunus ne s'explique pas par IA, on ne peut s'empecher
```


## [2026-09-07T18:26:32.406Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"maBka\\|maöka\\|ma8ka\\|mafka\\|maSka\" BRT.txt | head -10"
}
```


### [2026-09-07T18:26:32.453Z] TOOL RESULT

```
2312:m.:  maskaUii(nin).
15959:•  j.  patar-  m.  'Hüter,  Schützer,  Schinner', von  Göttern :  'ta  nqma  ahmt  (näml.  AhM.) Yt/.i3;  —  /fiw'näml.  Mi^ra)  maskanahe °/a  nipata  ahi  adruzqm  Yt.  10. 80;  — haom^m  . .  'tsrftn  tanuye  baire  Yt  14. 57.
23387:KompE. ;  Ableit.  —  Ableit.  aus  tiaAma-;  das alte  Verhältnis  von  yasni  %'iyainyi  hat  neben yasnasia  vakmaiea  die  Verbindung  yamyasitt vakmyaifa  ins  I^ben  genifen.  —  K.:  nyi- yiinötnand,  Sü.:  namaskaratiiyah. —  ')Pü. :  amäi it.  Die  Unrichtigkeit  der  GoN.schen  Lesong folgt  aach  daraus,  dasi  v'  allein  -  ohne  yamya- davor  -  eben  nicht  vorkommt.
```


## [2026-09-07T18:26:38.733Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18570,18620p' BRT.txt | cut -c1-400"
}
```


### [2026-09-07T18:26:38.781Z] TOOL RESULT

```
,.  ästryeitiJ  *ts  N.  ij;  —  'lanqm  ioa asaonqm  aiaoninqmca  ahümid  datnqmca  . . Y.2(J.6; — vUpanqm  akmya  nmane  'tanqm paraÄristanam  .  .  fravasayS  "von  allen verstorbenen  Ifächstverwandten  dieses Hauses  .  ."  \.26.T,  j.  18.
Ar.  'iiahAä-naaiisIlia-  eig.  'der  der  Familie, Verwandtschaft  nächtt  stehende*.  Ar.  'nahhä. f.  'Nabel;  Familie';  ahd.  naba  'Nabe',  letl. naba  'Nabel';  vgl.  näfa-  m.;  Richter  1F.  p. 309.  —  ai.  näö/iSafdiitha-n  m.  EN.  (Ableit. ans  ar.  'naih').  —  Pü. ;  nabänaiiHsl  (Transskr.), SQ.:  ncaänvävanikaläh  'novem  familise  pro- pinqui'»).  —  ')  nahlf  
•  p.  nabukudra£ara-  m.  EN.  eines  baby- lonischen Fürsten  (Nebuhadnaar,  Sohn  des Nabonedos) :  1  martiya^  bäbiruviycr  nadt'ta- bairc^  .  .  avaUa  adurujiy<^:  adam  'ra* aptiy  hya*  nabunailahya  pu^''e^  Bh.  r.  ifij 18,  19,  4-  3,  Bh.  d;  —  iyam  arax^  aduru-
)iy<^  .  .:  adaWt  °r<^  am'iy  hy^  nabunai- Uihyä  puV(^  Bh.  i;  Bh.j.  13,  4.  3.
•  p.  nabunaita-  m.  EN.  eines  babylonischen Fürsten,  Nabemdoi:  adam  nabukudracar»^ amiy  hya''  -lahyä  pu%^<^  Bh, /,  16,  J.  13; —  'taAya  pü^'a*  Bh.  4. 3»,  Bh,  d,  i.
j.  m>/>ir- :  I.  unter  nafä/..
dby  Google
I04I  naohuämant-  -
g.  ttafhi-lä :  s,  anter  nafit-.
•  j.  naehui'mant-  m,  Name  eines  Bergs
oderGehiTgs:  aAmaj  Aa/a  ffaraysß-aäx^an .  .  säirivas^a  "masca  Y(.  ig.  4,
Eig.  Bed,?  ~    'TiaaAm-  (=—  ar.  *nasul-  oder
•  ].,  g.  Dana  Adv.  i)  'an  einem  besondem Ort,  abgesondert';  yJ  dät  ntanS  vahyS mazda  asyascä  .  .  %waAinl  xratä  apsmim °nä  aahat  "wer  sein  Denken  (jetzt)  besser macht  und  (jetzt)  schlechter  ,  .,  der  wird nach  deinem  Ratschluss  zuletzt  abgesondert sein"  Y,  48. 4''.  z)  'an  mehreren  ver- schiedenen Orten',  attrib.  sva,  'verschiedene, mehrere';  nabä
KompA.  —  ai.  nänä  Adv.;  s.  daiu  BtHU IF.  10.  10,  12.  116.  —  Pa.  (in  N.)r  ^«/(?,  IF. 12.  1 1 7),  (m  V.) :  vtart  u  ian  «.  —  i)  Zuletzt  zSt. IF./2.  117.— ')  Hd».  aba,  s,  aber  Pü.  —  3)  IF. 12.  115.  —  *)  Weil  man  das  Wort  mit  Harim narlm  V.  JO.  Z  in  BeziehuDg  brachte.
•  j.  nana'rlstay-  m.  EN.  eines  Gläubigen: Uois  paisatat3h5  ai'aonS  Yt  13. 115,
Eig.  'da  und  dort  Sorge  tr^end';  "tastay-  f., .™  V.  rld-  (S  51  II),  ..  in  räl... j.  natalima  N,  86:  lies  tii  nUima.
•  j.,  g.namV,'sich(weg)beugen'.  Praes.3 tuma-,  3  °nma-,  4  näma-,  30  (Kaus.)  »3- maya-.  —  PPfP.  *'nala-;  Inf.  nsinSi.
parö  a^rlf  baoh^  dürSt  tumaiii  Vyt 5/(?).         S.  noch  Inf.
mit  apa  'entfliehen,  weichen  von  —  weg' (Abi.  mit  ha^ä):  paoirXm  i^annS  apani- mata  .  .  yimat  kaca  Yt  J^.  35.
mit^a  i)  'fliehen',  absolut:  /ränämailt . .  artrS  mainyul  Yt/p.gö.  a)  'fliehen vor  -'  (.pars  mit  Abi.,  Lok.):  hö  nöit taritS  *franämaite^^  .  ,  parS  dafvatibyö Y.57. 18;  — frä  akmat  parB  vlspe  daiva tarita  tumanle^.sy.i&,'^t.f).n{wQn3m/irite); — yä^a  assm  mit tarÜS  fra.nmäne .. pat daSvalibyS  Yt.5.4;  —  a?iu pars fränämaiU alsmö'VLit).')^.  3)  Ka
mit  VI  'sich  auseinander  tun,  -ziehen, -dehnen':  ärmaite  fraca  üia  vlla  mmataka
nay-  1043
harShre  pasvqmla  . .  "Arm.,  geh  vorwärts und  tu  dich  auseinander,  um  tragen  zu können  .  ."  V.  2. 10.  a)  Kaus.  'aus- einander treiben,  sprengen':  fravasayS  .  . yi  rasmanS  .  .  vf  ma&iyqmtn   namayeinti
Yty.39-
ai.  nämate,  nämaya'i;  naiah,  ni-näme;  mp. fra-nämilan  (usw.;  s.  Pü-V  -  Pö.  (lu  V.  57)- änäniT/an,  (la  V.  i):  awnämilanS.  ~  1)  Pt4; s.  daj  folg.  mmanle.  —  ')  So  T,  Ausg.  'Hl/a. Pä.:  fehlt  —  3)  Das  .i  darin  ist  Dach  /"J:.- Manier  mit  ^  dargestellt.
•  *iiainra-vak-"  Adj.  'ehrerbietige  Worte sprechend':  'växs  F.je,
Adj.;  np,  nanu  'sintl,  weich'.  —  Pü.:  ä/^i grwiln,  —  I)  Hds.  namnra'.
•  i->  K-.  P-  oay-  V.  'leiten'.  Praes.  2 naya-,  3  nya- '',  1 7  (FuL)  naSiya-;  j-Aor.  i
i)  'Jemanden  leiten,  führen':  darisa  nä pairyaQxtaca  . .  ^nyete  usianavaitli'  vTspä /rasutfiain/ (sd.)  P.jÄ  a)  ["hinführen, hinbringen  zu  —'  (abiy  mit  Akk.):  Äauv {ih''d'laxinam  agarbäye^  anayi^  abiy  mSm Bh.2. 14;  5.1;  —  fravartis  .  .  anayatä (in  pass,  Sbn)  abiy  mim  Bh.2.  13;  — hatev ,.  baitJ*  *anayaiä  (pass.)''  abiy  mäm Bh,  1. 17.  3)  'weg
*astB.vj%Stus  dim  bandayäti  vayö  dim batUm  nayeiti  V.  5. 8 ;  —  sp3n>m  *naisyuti FrB.(?).  a)  mit  Angabe  des  wohin? durch  Akk. :  tsm  *vä  ahum  dngvantB  syao- %anaU  c^äii  dama  nalsat  (Konj.)^'  "zu solchem  Leben  (aber)  wird  euch,  ihr  Drug- genossen,  ob  eurer  Taten  das  eigne  Ich führen"  Y.j/.  20.
mit  ava  i)  'Jemanden  herabfUhren, ■holen  von  —  her,  aus  — '  {haca  mitlnstr.): avanayeni  spmt>m  mainyBm  kaca  . .  *garö nmäna  Yt  75.44.  2)  absolut  'reissen', \omVi 3SStT :  rat)hqm  *avajtayHntTm''^"dit reissende  R."  P.J"^.
mit  upa  'Jemand  herzufuhren':  ya%a  .. batidaymi  .  .  franrasyatam  . .  Uta  bashm upanayeni  Yt.i?.  18.
I  mit/i7i'j/(?}  und  3 'herzuführen, -bringen (lassen)': öwica/yJ  aspaisd^ patiyanayami^ Bh.7.  18.
mit  para  '(als  Beute?)  fortfllhren':  ime nS . .  aspa  para  *mihra  *ioa  nayenU  "die da  führen,  o  M.,  unsre  Rosse  hier  (als Beute?)  fort"  Yt70.42.
ai.  näyaH,  ni}at\  mp.  nUan.  —  PiL  (lu  Y.,  V.) :
ob,Google
»043
•nava-
■aos,  (ta  V-S^:  (eblt;  t.  «m^  >'<>.  4.  — '}  D.  L  iBya-,  $  36S.  II.  —  »)  Ansg.  hit äi«a>-<ia.  —  j)  V.  5,  öa.  wo  die  Stelle  tci- wendet  Lit,  steht  dafür  mjfriiayäl.  —  4)  Hds. tna  njfm^/im  (u>  nach  Blcm3iet  Lei.  95). Pä.:  /a  afe  *iia}J>iii.  —  i)  Do  Stein  lässl aar  noch  äßiajrum  erkemicn,  daTor  eine  Lacke. Vll.  besser  äHy�
•  j.  'nava  Psut  'durchaus  nicht,  überhaupt nicht,  sicher  nicht,  keineswegs':  kä  filasti Li>af  ..tf  he  asii  ä^a  tf  ke  asti  äp^ntii iiC-it  kl  asti  yaotdairym  "Vas  ist  die  Sühne dafür?  .  .  Es  gibt  dafür  überhaupt  keine Sühne  .  ."  V.  j,  39;  —  yS  mqm  . .  dära- yeiä  yaia  täybm  pfssaärtm  n'  ahmt p>sS.- sUrö  ".  .  wie  einen  todsündigen
KompA.  —  Komp. :  *nii'  +  ^vä  j  ar,  •nag^f , $  pa.  I.  —  ai.  »gL  nä  väi').  —  Pö,;  «.  - ■}  NA.  tua!a./rSk-,vfrisäm\  i.  aber  F  1  und S  296.  4.  —  1)  In  der  Bedeotnnc  'überhaupt nicht'  RV.  3.  33,  10,  to.  95.  15.
•  j.  'nava  Part  'oder  nicht';  u^»r»ptat paiti  draonät  (sd.)  «•  tagfnptäl  V.  5. 26;  a6'.
Ableit  —  Komp.:  •«a'  +  Ji»«;  ar.  'nauä, ip2.  t,  Bthi-  BB.  ij.  58'),  —  aL  Hfl  vä.'— Pu,:  ne.  —  >)  VgL  übrigens  daia  'ntna.
•  j.  ^nava  indekL''  Zw.  'neun':  ya^  Ai  'va (als  Nom.)  xsafna  lacantt  Y.g.  35,  ig.  23; i/i.  10,  1 1 ;  —  'va  (als  Akk.)  ptrüwS . . i^rmuFa  V.2.  ^o;  5.  $1,  ().ii,  ii.jaPüZ., 10.18,  14-14,  17-6',  /^.aiPüZ.,  22.ao', P.g,  Yt4-ö(?>,  /9.41;  —  °^'a  «/«  may^m'^ V.5,  54;  —  -zraÄ  yatkj  navaitisca  °vaca sata  'va^a  hatattra  navasSsea  (sd.)  batvqn
•11J114«.  \3lO. —  ')  Man  Tcilangte  den  Plnr. des  Sabst..«,  Tgl.  irJi-No.  3.  —  j>  N.\,  «iira.- jn/*.  —  4)  Dp.  u,  mp.  d  aas  ir.  a^c',  k  Tom ZaUvoct  für  10  iiiiA.
•  j.  *iiava  Adr.:  s.  nara-.
•  j.  nava-  Adj.  (fem.  tj-)  'neu,  frisch': vurärmH  (sd.)  rivärsku  'va  (NSC)  <?/>'  .  - "ra  (NPn.stattf-)  a^viz-i  -ra  (NPn.) Äraräs.i 'vata''>  Ö.JisataJasaKsA.')\.2i.y  a)  IS. "i'd  als  Adv.  'aufs  neue':  .fu^a  xä  ..  apqm /a',inii  'ra  Yt.  Ä  5.
aL  Hffia-  Adj.,  np.'r'W.  —  Pi;  näi.  —  •)  D.  L nat-a  (NPn.)  +/J  (NPn.).
•  nava-karia-  n.  'durch  nenn  parallele Furchstriche  hergestellte  Abgrenzung*:  's'fm frakäravdti  Yt.  4-  6.
VgU  "intarla-.
•  j.  iiava.^ya-  il  "Langenausdehnung von  neun  Schritten,  neun  Schrittlängen': "krigäim  w/3ptm  'gäim  paitynpim  V.6,40.
```


## [2026-09-07T18:26:51.376Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN abr\"; grep -n \"abr 'Wolke\\|abr .Wolke\\|Wolke\" HRN.txt | head -8; echo \"=== HRN Salz\"; grep -n \"Salz\" HRN.txt | head -8"
}
```


### [2026-09-07T18:26:51.431Z] TOOL RESULT

```
=== HRN abr
1007:63. ebr *Wolke .
1009:ap. 'AßpolKo/LiTjg Herod. ; aw. awra- 'Wolke* ; phlv. awr
1011:arm. amp, amb 'Wolke (H. No. 14); kurd. avr, awr,
1773:(H. -Seh.); af/. varyaj 'Wolke*, varyaz, var-edal
8778:1009. mey *Wolke .
8779:aw. maf.ya- *Wolke'; phlv. mey ^ vd. 15 (18); ai.
8781:oss. d. meyä, t. 7nty *Nebel, Wolke' (185).
10753:Wohl kaum in der Bedeutung 'Wolke'.
=== HRN Salz
4538:kurd. x^ *Salz ; bei. väd, n. väd, vad\ vü:: (411)
4539:'Salz.
```


## [2026-09-07T18:26:55.121Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1000,1015p' HRN.txt; echo \"=== which printed page\"; awk 'NR<=1007' HRN.txt | grep -c $'\\f'; echo \"=== namak in HRN\"; grep -n \"nemek\\|namak\\|nemk\" HRN.txt | head"
}
```


### [2026-09-07T18:26:56.401Z] TOOL RESULT

```
62. aylne, älne 'Spiegel'.
a+ i^dai' (ai. dhai-),
bei. ädenk, n. adm, üzma ^Spiegel' (10); kurd. nainik;
oss. d. ai'dänä ^).
A(E).
eba mit', s. ba (No. 145).
eher auf*, s. her (No. 191).
63. ebr *Wolke .
g. awr; Kä§. awr etc.; jüd.-pers. nur n2X.
ap. 'AßpolKo/LiTjg Herod. ; aw. awra- 'Wolke* ; phlv. awr
(geschrieben apr)^ abr; ai. abhrd-,
arm. amp, amb 'Wolke (H. No. 14); kurd. avr, awr,
häür, haur; af/. var-yaj ; oss. arw 'Himmel' (29); bei.
haur *Regen* (163).
64. ebrü 'Augenbraue*, brü, b^rü (Sahn. I, 104 Vers 778).
g. biirä.
=== which printed page
30
=== namak in HRN
4782:533. ~dän 'Behälter , vergl. äbdän, nemekdän etc.
```


## [2026-09-07T18:27:03.705Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 285<=i<=300 and 'ابر' in p:\n        print('---leaf',i, p[:300].replace('\\n',' | ')[:300])\nEOF"
}
```


### [2026-09-07T18:27:04.900Z] TOOL RESULT

```
777
---leaf 286 آ لین جمشید - یکس نون . فلحن | دیم است از سی‌لحن باربد - و نام نوایی هم‌هست | از موسیقی . | وروش‌زا یز گویند - ونامدهی است یت ار | مومیایی . ۳ ۱ | آ لین پرستی - بتح بای فارسی . | کنابه از خدمت کردن با مایت فروتنی باشد . | بیان دوم | در همزه با بای ابجد مشتمل برشصت و دو لغت و کنایت | زد و پلزن )۱( ۳9
---leaf 287 و امد تجرید نوفتر | آای‌افت را با واو جمداز اف که « اوپاشه » باشد ابحد تحرید () نوشتن - | بومن حعنی نز کفته اند ۷ * . ۱ کنابه از توثك خواهش و آرز و کردن و ازخودی ‏ | هام »یر وزن سلام . بسینی ولم است | و مزاحمت اضی بر آمدن واژماسوی اف مجرد | . که قرض باشد . ۶ گردیدن بلشه . | ۱ - فرحنکه نوسان اين بت ر
---leaf 289 - ۷ - ایکا کبا | و سکون الث و ها و رای قرشت ؛ نام اصلی | نیشابور است و ممدن فیروزه آلجاست ٩‏ . | ابر قباك ع من فان . نام ولایتی است | از توابم اره جان ۱ که میان اهواز و فاری | واقم است و آباد کرد قباد شهربار است ؛ و با | زای قطه دار هم کفته اند ۲ . # | ا پر کاد - باکاف‌بروزن‌اتکبار » بمعنی | متحیر و
---leaf 290 و نگذارد که جراحت ورم کند . وااگر بلس رکه | بردمل. وخيارك نهند ب رکرداند ۱ » وابرک کیاپ " | یز بنض آمده است که در آخرش بای ابجد | باشد . ٩‏ | ابر که ین کاف » نم شهزیست از | عراق عجم . و چون‌آن شهر بر زمیتی که درته | آن کوه است واقم شده باين نام موسوم ماختند | ومعوب آن ابر قوه است ۴ حرایین زمان بتعری
---leaf 291 اول و فتح ثانی حوبرء را کویند و آن پرنده | ایست که بمربی « حباری » گوبند ۴ و کی | «تفدری» خوانند و بکسر اول ميو# نوری و و | باوه باشد ۴ . | ا یر هام » باها بروزن شفق فلم . بمعنی | طسمت باشد؛ گویند فرشته ات که تدی سکننده | عالم است - و تام ییفمبری هم هست ۵ . | ار هه - بنتح اول و ثالث و رابع » تام | پ
---leaf 292 مگ بر آن قبر میهد ٩‏ - د الم خخضصی که | کاتای شا تلاح هو : | آ یر هیمیه - مخنف ابراهیمیه است ۰ | وآن نوعی ازآش باشدکه با غوره پزند و مقوی | و مرح اس و فوخه این اف عربی فیست . | ابر یشم - بنتح و ضم شین نقطه دار | معروفست . کویند مقراض کرد آن در مماجین | فوت باه دهد و بدن را فربه کند و پوشیدن‌لبای | آ
---leaf 295 کت آیرویز | نحتانی مجهول و واو » بسعنی آبی باشد و آن | ا ییون « بر وزن و ممنی افیون است | که تربالك باشد ونام داروبی حم هست که بیهوشی | می اورد ۴ ۰ | ونگی ات ععروف. ابی سك ۳ ۲ بای حطی | ۱ ۱ 3 ۱ ‌ ‌‌ هح ‌ | یود ج ( 3 رب وسکون های‌هوز و کسرمیم رتحتانی‌بالف کشیده, | و دال بی نقطه ؛ نام شهرست در خراسان 
---leaf 297 ی سس اعشی | وسکون ثانی و جیم . میواست که آنرا خاوسی | «تریج» اگوبند و پوست آنرا مربی سازند . بخور | کردن تخم آن بواسیر را تافع بود و جربی | «تقاح مائی خوانند . | ا سیر (۲) - بکر اول و سی بی‌شطه | و سکون ثانی و زای‌قطه دار , نام یادشاه خوارزم | است وزمخشری در زمان‌او بود و ماسلطان‌ستجر | چنگه کرد . گ
```


## [2026-09-07T18:27:11.133Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (288,289):\n    print('======== leaf',i)\n    print(t[i])\nEOF"
}
```


### [2026-09-07T18:27:12.442Z] TOOL RESULT

```
======== leaf 288
ابحل ی
)بحل « بنتح اول و ضم حای بی نفطه و«شتکار» نیز گفته‌اند » لقری را نافع است .
و سکون ثانی و لام » نام یادشاه جایلسا باشد » و
آن شهپرست در مقابل جابلفا وهردو درعالم مثال
اند ؛ و بعضی جایرسا گفته اند که بجای لام .
رای قرشت باشد .
) بحاد - باخای نقطه داربر وزن‌اهواز.
تلم ولانتی است ازتر کستان مشهوریظلم:. گویند
مردم آنجا یشتر ترساو آتش پرستند و درآنجا
دبرست سار تسم ۱ .
ایحوسا ۴ - باسین بی نقطه بر وزن
محمودا . بزبان سربانی دوائی است که ب رکه
آن ساه برخی مابل باشد و آنرا« اپوخلما »
آیدا۵ - با دار ابجد بر وزن بد تام
بمعتی چم است که در مقابل جوهر باشد ۴ .
ابف‌آن - بر وزن افغان , بمعنی دودمان
و خاندان باشد - و بمعنی سزاوار و حستحق حم
آمده است ؛ و در موّبد الفضلاء با ذال نقطه دار
نوشته اند * .
ایدرم * ه بکس اول بروزن اسپرم .
نام کتلب شاکمونی ۷ و او باعتفاد کف ند
پیغمس صاحب کتاب است » و معنی این لفت
باعتفاد او اول و آخر کتابها باشد .
اير - یسکون ثانی بروزن صبر » حص‌ون
البلدان) ۸۵25 و ۸۵216 « لت نامه *. ۴ - مصحف کلب « انشوسا » و < انشا »
صت ۸ لغت ناهد *. ات مو ندالفتلاء حم همسن حعتی آورده , شاهدی برای‌آن د نده‌نشد.
محتملاست ممحف «ندام» باشد. «لفت نامه». ۴ ت هردوصورت اند شواهدمحتاح است.
«لفت نامه». ۵ - درسانکربت ۸۵0۵۲۳۵ ودرپالی20101018۲۳۳12. «د کرراجا».
۱ - ۷۵0 ۹2۷۷2 (-اکنی زاهد) وآن نامیاست که اغلب بدان 5002۳1۳8
2 موّسس آیین بودایی را مینامند . پدر او ۹۷0000202 رئی فبله 522
بود و سا کیامونی درنیمة قرن ششم متولد شده .
بشه از صفحهٌ ۷۷
شکی نیست که اصل الفبای عرب . عبرانی - آرامی‌است معهذا ۰ عرب که ازدبگرلفات
سامی آ کاهی نداشته است واز وی دیگر بعات استفراق تام درسنن خوش وبسیب تعصب قومی»
برای‌کطمات معمولهٌ «ابجد» . . . - که ازطریق روایت بدیشان رسده وبرای آنان نامفهوم بود -
تأوبلات دیگری قاثل شدم‌اند . مجموعهٌ تحشقات ایشان - هرچند که جالب توجه است - جز
افانه چیزی نیست . برطبق گفتاربسی از علماء » شش پادشاه مدین‌حروف هجائی را بترتیب‌اسامی
خود مرتب کرده‌اند وبرحسب روات فزشگن شش کلمة اول ازکلمات هشتکانة مزیور اسماء شش دیو
وطبق رواث سوم » کلمات مذ کور نامهای ابلم هفثه است . با وجرد این در بین علمای نحوعرب »
کانی مانند مبرد وسیرافی بوده‌اند که بروابات مذ کور قانع نقنم..س تا کنتماند که لیات
هششکانة ابجدی ازماخذی بگانه اقتبای شده است . « داثرءالممارف اسلام » و رك : دابجد سوزه
بقلم سید محمد علی جمال زاده . مجله‌کاوء سال پنجم شماره *۱ ( قماء ملل و14 :
======== leaf 289
- ۷ - ایکا کبا
و سکون الث و ها و رای قرشت ؛ نام اصلی
نیشابور است و ممدن فیروزه آلجاست ٩‏ .
ابر قباك ع من فان . نام ولایتی است
از توابم اره جان ۱ که میان اهواز و فاری
واقم است و آباد کرد قباد شهربار است ؛ و با
زای قطه دار هم کفته اند ۲ . #
ا پر کاد - باکاف‌بروزن‌اتکبار » بمعنی
متحیر و حیران و س رکردان باند ۸ .
ایکا کیا هیفتح اول وانی‌و کسرکاف
دوم تحتانی بال فکشیده , ننیده و تارعنکبوت را
کویند. اکر بر جراحت نهند خون را باز دارد
انت و بمربی «سحاب» گود ٩‏ - و بمعنی هرد
(۱) هم آمده است که دره‌قابل زن‌باشد, و بفنح
ثانی‌بلفت زند ویازید (۲)لت تناسل را گوید ۳
- و «بر » را نیز گفته الد که بمرمی « علی »
خوانند ۴ و بمعنی بر و آغوش هم هت  .‏
آ برش ع بنتح اول و تال ۰ بر وزن
مهوش ؛رنگه سرخ و سفید در هم امیخته را
گوبند . - و اسبی که نقطه های مخالف رنگه
او پر او باشد ۴  .‏
] پر ش خور شیف کنابه‌ازآسمانت.
ابر شهر - فتح اول و انی و رابع
(۱) چك : مردم ! )۱( چك : ژند و باژند ..
۱ - انسکرت 2080۴4 (با 200068 مرکب از0۳۵ - ۵0 بمعنی برنده وحامل
آب ) « وبلیامز ۳:۷۹ > اومتا 3072 بارتولمه ۹۵ بهلوی 27 « دهارله ۱۷۹ » « عنلی
۶ > ۸ نب رک ٩۱‏ . اففانی ۵۲2 . بلوچی 8۷1۲ (باران) « بارتولمه ۹۵ » , کردی ]اقلا .
اورامانی ۷۴۲ : 4 . اورآمان ۱۲۲ * .گلکی ۳9 دزفولی ۳۷ . ۳ 32602۲
حزواری است بمعنی ره » آلت رجولیت « بندهش ۱۱۲ ۰ ۶ یوستی » بندهش ص۵۱ * . اشتباه
نشود ا.« ابر » که در عربی بمعنی نره و فرزند فررینه است و 26779)2(8 هزوارش پمعنی آلت
رجولت « بوتکر ٩۳‏ ۰ . ۴ - اوتا ۱۳۵17 و ۱۳02۲ بمعنی بالا ۰ عالی»
سال‌کریت ۱1۳8۲1 « بارتولمه ۳۹۶ - ٩۵‏ ۰. پهاوی 8087 < منای ۲۹۹ < اونوالا ۳۳۵ ۰
«نب رکه ن 9
۴ - از آن ایرش وبور وختگك وسیاه که دیده است ه رکز زآ هن سیاء
فردوسی * لت تامه » رك : نوروزنامه س ۱۱۰ . ۵ - ۸52۲5۳229۲ , در ارمنی
01 ۸۳8۲, اینکه‌یسی آنرا بمعنی شهربالا بادکرده‌اند درست نیست. بلکه بمعنی شهر
( 8۳27001 بونانی ) برجته‌ترین قبیله ازسه قبلهٌ داعد28102] که دوت‌بارنی
( شاید : اپارنی » ایرنی ) را تأسیی کردند « مار کوارت . شهرستانهای ابران صس ۵۲ بافوت‌این
نام را جفتح اول وسکون دوم وفتح راء وشن معجمه آورده و کوید سکزی آنرا بی‌مهمله روایت
کرده است, رآن معرب است واصل عجمی‌است زبرا «شهر» بفارسی بمعنی بلداست و «ابر» بمعنی
«غیم». ابرشهر تیشابور است و کاه همزه ر) قاط کنند و 3 برشهر ٩‏ گونشد .۰« ممجم‌البلدان »
« کرستنن . سلطنت فاد ترجمه فارسی ص ۰۳۵ . 1 - ارجان . ۲ - بافوت
هم < ابز قباد * بفتح اول وانی و سکون زاء وضم قاف ر باه موحده و الف و زال مجمه آورده
گوبد : بپمین وجه بزاء بخط چند تن از اهل علم دبدهام وقباد بن‌فیروز یکی ازپادشاهان ابران
ویدر انوشیروان عادل است و نام این موضم در فتوح (اسلام) با « مذار » باد شده و گویا ابر قباد
مجاور «میسان» و «دستمیان» باشد وهلال‌ین محن گوید: ابزقباد. (بازاء) ازطسوح‌های مذار.یین
```


## [2026-09-07T18:27:42.366Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if 'abr-amOn' in p or 'abrninftiu' in p:\n        print('leaf',i)\n        print(p[:2500])\n        break\nEOF"
}
```


### [2026-09-07T18:27:43.936Z] TOOL RESULT

```
243
leaf 19
                                            .       tfUJcu^UftiLttU                                                                                                                            --v L^c--,U»-U*jl



      \\/\6*S -T/IY^ -t-r/fiiS                            (e**.*-Ui)-an                         +   (   u I**   .
                                                                                                                    ^^           |



                                                                                                                                                                                                                                                    •rri
                                                                                                                                           •
                                                                                                                                               M-IV/T^ ham                            :L(4tl/b.           1773)sam :Lham-               :    4_ui    *   fc*,



     -ah§xt cJuaU ahania, ahan5ldan                                                 :   ^ a-hag5                        i
                                                                                                                                **•


     1Y/1Y^             r-'^l^)-isn+ (Pers. Stud. 10)
                       (,,*-.                            *-*-*'                                                                                                               ,
                                                                                                                                                                                  tf Ujbiloo=-S .          jJ^i* : hara-bun-iz                       ^HiA^
             .
                 o ^a,U.        j^n § ahanjisn  :  k«*-cv.                              :
                                                                                                                        -




                                            .j/ti      -^ .c^yl*                havist IV""*'
                                                                                    :



                           ^ \*/a^ {AiWb
                      -&/)•>                                       .     1806) haviito- I
                 •   k/\o^ o^Jk o'^     'havistan         :                                     :       WlO'*'
```


## [2026-09-07T18:27:49.535Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming | cat; find . -iname \"*shayest*\" -o -iname \"SNS*\" | head"
}
```


### [2026-09-07T18:27:49.585Z] TOOL RESULT

```
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
./SNS.txt
./SNS_pages.txt
./ocr/SNS
```


## [2026-09-07T18:27:52.521Z] TOOL CALL #73: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS | head; "
}
```


### [2026-09-07T18:27:52.558Z] TOOL RESULT

```
total 1428
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  7 12:18 .
drwxrwxr-x 13 sfmqrb sfmqrb    4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb    1389 Sep  4 16:10 14.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  410799 Sep  6 11:23 299.png
-rw-rw-r--  1 sfmqrb sfmqrb    1281 Sep  6 11:23 299.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1220 Sep  4 15:51 6.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1021826 Sep  7 12:18 74.png
-rw-rw-r--  1 sfmqrb sfmqrb    1450 Sep  7 12:18 74.vision.txt
```


## [2026-09-07T18:27:55.545Z] TOOL CALL #74: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS/14.vision.txt; echo \"=== 74\"; head -20 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS/74.vision.txt"
}
```


### [2026-09-07T18:27:55.598Z] TOOL RESULT

```
[SNS = Tavoosi, Vazhe-name-ye Shayast ne Shayast, printed p. 14 = archive.org VajnameShayest leaf n23, RIGHT-hand page (numbered ۱۴); each leaf image carries two printed pages, p = 6 + 2*(leaf − 19). Transcribed from the page image by hand, 2026-09-04.]

<pahlavi> avām : وام، قرض.
  ستا: √ap «به دست آوردن»،  فاتر: ʾbʾmyh (Nyb. II. gls. 13) ؛
  (Henning. List, 80) واژه‌نامه مینو خرد تفضلی، پا: awām (مینو خرد). ک ۱۴/۸

<pahlavi> avāmīhā : بوام، بطور وام، وام مانند (قید)  (نک: واژه بالا) ک ۱۴/۸

(other entries on the same page 14: awagi …؛
 apār/appār : دزدیده، ربوده شده، از دست رفته — فاتر: appar (Mir. Man. II.47)،
   نیز BSOAS XII.46 (واژه‌نامه مینو خرد، دکتر تفضلی) و Zum Sasanidischen Recht,
   Bartholomae 5.8: پا apar …؛
 appār bavēd : دزدیده بود / شود …؛
 ābān : آبان، روز دهم هر ماه و ماه هشتم هر سال …؛ ābān-it …؛ ābān : آبها، جمع آب)

[facing page 15 has: abārīg «دیگر، بعد» (ستا/فبب/سا apara- از apa- + ra-, Kent 168;
 فاتر ʾbʾryg Mir.Man. I 32, II 43; پا awarā), abārīg-iz, abāyēd, bē abāyēd,
 ō abāyēd, andar abāyēd, nē abāyēd, abāyēd šudan/dādan/kardan, abāyist]
=== 74
SNS (Tavoosi, Vāzhe-nāme-ye Šāyast nē Šāyast, Shiraz Univ. 1365) printed p. 74
(= pdf page 54 of the archive.org "vajname shayest_text.pdf"; running head numeral ۷۴ at top right;
facing page ۷۵ is the left half of the same scan leaf, so SNS_pages.txt leaf 53/54 = pp. 74-75).
Read from the page image by vision (OCR of this book is unusable).

Entry, right column, lines ~17-24:

  <Pahlavi script> ōmēd: امید
    *ava + √may-  (GNPE. 26)   کردی: umīd, umūd / افغانی: umēd
    شکل هزوارش آن: <Pahlavi> (Junker, 4.)
    است. پروفسور کانگا آن را از upa + mati اوستایی و ریشهٔ man: ماندن،
    صبر کردن میداند  (Kanga. Cit. Han. 46-7.)
    این واژه در دیگر نوشته‌های پهلوی به شکل <Pahlavi> ēmēd هم آمده است. ک ۱۷/۲۰

Translation of the Persian: "ōmēd 'hope'. *ava + √may- (GNPE 26); Kurdish umīd, umūd,
Afghan umēd; its heterographic (huzvāreš) shape is … (Junker 4). Professor Kanga takes it
from Avestan upa + mati and the root man- 'to remain, to wait' (Kanga, cit. Han. 46-7).
In other Pahlavi writings this word also appears in the shape ēmēd. (ŠnŠ 17/20)"

Neighbouring entries on the same page: hē, hast, hēm, amāh hēm, hēd, hēnd, andar hēnd,
```


## [2026-09-07T18:28:11.197Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find leaf index by counting form feeds up to a line\nimport re\ndef leaf_of(lineno):\n    txt='\\n'.join(lines[:lineno])\n    return txt.count('\\f')\nfor ln in (11252, 1149, 16501, 14894):\n    print(ln, 'leaf', leaf_of(ln))\nEOF"
}
```


### [2026-09-07T18:28:12.640Z] TOOL RESULT

```
11252 leaf 159
1149 leaf 19
16501 leaf 239
14894 leaf 206
```


## [2026-09-07T18:28:35.973Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%AD%E0%A5%8D%E0%A4%B0",
 "prompt": "For the Sanskrit entry अभ्र (abhra): give the etymology in full (Proto-Indo-Iranian, PIE *n̥bʰrós, cognates Avestan aβra-, Persian ابر, Greek, Latin) and any note about the folk analysis as ap- + bhr- \"water-bearer\"."
}
```


## [2026-09-07T18:28:37.390Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1",
 "prompt": "For the Persian entry ابر (abr) \"cloud\": give the full etymology (Middle Persian spelling, Proto-Iranian, Avestan, PIE) and cognates listed."
}
```


### [2026-09-07T18:28:41.354Z] TOOL RESULT

```
# Sanskrit अभ्र (abhra) - Etymology

The word derives from **Proto-Indo-Iranian *abʰrás** ("cloud"), which comes from **Proto-Indo-European *n̥bʰrós**.

## Cognates
The entry lists several related terms across Indo-European languages:
- **Avestan**: 𐬀𐬡𐬭𐬀 (aβra)
- **Persian**: ابر (abr)
- **Latin**: imber
- **Ancient Greek**: ἀφρός (aphrós)

## Related Note
While the page does not explicitly mention folk etymological analysis of the word as ap- + bhr- ("water-bearer"), it does document the documented cognate forms that help establish the word's ancient Indo-European roots and demonstrate its historical semantic connection to clouds and water phenomena across multiple language families.
```


### [2026-09-07T18:28:43.798Z] TOOL RESULT

```
# Etymology of Persian ابر (abr) "cloud"

**Middle Persian Origin:**
The word derives from Middle Persian "𐭠𐭯𐭫" (ʾp̄l /abr/), meaning "cloud."

**Proto-Iranian Ancestry:**
It traces back to Proto-Iranian "*abráh" and ultimately to Proto-Indo-Iranian "*abʰrás," which came from Proto-Indo-European "*n̥bʰrós."

**Cognate Languages:**
The Wiktionary entry lists several related words across ancient languages: Avestan "𐬀𐬡𐬭𐬀" (aβra), Sanskrit "अभ्र" (abhra), Latin "imber," and Ancient Greek "ἀφρός" (aphrós). These cognates demonstrate the word's deep roots in Indo-European language families, illustrating how the concept of "cloud" was expressed across diverse ancient cultures through related linguistic forms.
```


## [2026-09-07T18:28:49.807Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%A8%D8%B1%D8%A2%D9%85%D9%88%D9%86/",
 "prompt": "Is there an entry for ابرآمون? What do Dehkhoda, Mo'in or other dictionaries say it means, and any Pahlavi origin given?"
}
```


## [2026-09-07T18:28:51.109Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%86%D9%85%DA%A9&d=moein",
 "prompt": "What does Mo'in's Farhang say for نمک — the origin tag (e.g. [په.] Pahlavi) and definitions? Quote the entry."
}
```


### [2026-09-07T18:28:52.471Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:28:54.748Z] TOOL RESULT

```
# Mo'in's Farhang Entry for نمک

**Origin Tag:** (نَ مَ) (اِ.) — indicating noun in Persian

**Definition:** The entry describes it as "مادة سپیدی است که به آسانی سوده می گردد و در آب حل می شود و آن را از آب دریا و معدن به دست می آورند" — a white substance that dissolves easily in water, obtained from seawater and mines.
```


## [2026-09-07T18:29:01.571Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 -c \"\nimport urllib.parse\nfor w in ['ابرآمون','نپتون','نمک']:\n    print(w, urllib.parse.quote(w))\n\""
}
```


### [2026-09-07T18:29:02.921Z] TOOL RESULT

```
ابرآمون %D8%A7%D8%A8%D8%B1%D8%A2%D9%85%D9%88%D9%86
نپتون %D9%86%D9%BE%D8%AA%D9%88%D9%86
نمک %D9%86%D9%85%DA%A9
```


## [2026-09-07T18:29:07.499Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%86%D9%BE%D8%AA%D9%88%D9%86",
 "prompt": "What entries exist for نپتون? Quote what Dehkhoda or Mo'in or other dictionaries say, including any note that it is from French (فر.) and refers to the Roman sea god / the planet."
}
```


## [2026-09-07T18:29:07.965Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D8%A7%D8%A8%D8%B1%D8%A2%D9%85%D9%88%D9%86",
 "prompt": "Is there an entry for ابرآمون or ابر آمون? Quote any dictionary entry and its meaning."
}
```


### [2026-09-07T18:29:12.710Z] TOOL RESULT

```
# Response

Based on the web page content provided, there is **no direct entry for ابرآمون or ابر آمون**.

The search results show "similar searches" that include related terms:

- **ارامونی** (from Dehkhoda Dictionary): Described as an Anemone flower, with the note that "بیونانی شقایق النعمان است" (it is anemone in Greek)

- **ابریمون** (from Dehkhoda Dictionary): Stated to be "به رومی اسم ایرسا است" (a Roman name: Irsa)

- **ابرنمون** (cloud chart): A cloud identification guide showing different cloud types with corresponding symbols

The page appears to be a Persian dictionary search result that did not find an exact match for your query.
```


### [2026-09-07T18:29:13.561Z] TOOL RESULT

```
# نپتون Dictionary Entries

The page lists several dictionary definitions for نپتون:

**Dehkhoda Dictionary** provides two entries:
1. An astronomical definition: "نام سیاره ای است از منظومه ٔ شمسی" (the name of a planet in the solar system), noting it was discovered in 1846 by Le Verrier.

2. A mythological entry: "در اساطیر روم ، نام الهه ٔ دریاهاست" (in Roman mythology, the name of the sea goddess), depicted with a trident.

**Mo'in Dictionary** describes it as: "هشتمین سیاره از منظومة شمسی است" (the eighth planet of the solar system) with a volume 57 times that of Earth, orbiting the sun every 165 years.

**Amid Dictionary** defines it as a solar system planet with two moons, orbiting between Uranus and Pluto, completing one orbit every 165 years.

**Academy of Persian Language** identifies it as: "هشتمین سیاره‏ای گازی" (the eighth gaseous planet) with a diameter approximately 4 times Earth's size.

The word is noted as originating from French (فر.) and carries both astronomical and classical mythological significance.
```


## [2026-09-07T18:29:38.688Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; curl -s -o sns_meta.json \"https://archive.org/metadata/VajnameShayest\"; python3 -c \"\nimport json;d=json.load(open('sns_meta.json'));print(d.get('server'),d.get('dir'));print([f['name'] for f in d.get('files',[]) if f['name'].endswith(('.pdf','.djvu','.zip','.jp2','.gz'))][:20])\""
}
```


### [2026-09-07T18:29:41.062Z] TOOL RESULT

```
ia600605.us.archive.org /10/items/VajnameShayest
['vajname shayest.djvu', 'vajname shayest.pdf', 'vajname shayest_abbyy.gz', 'vajname shayest_jp2.zip', 'vajname shayest_text.pdf']
```


## [2026-09-07T18:29:51.782Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && for n in 0022 0158; do curl -s -L -o sns_$n.jpg \"https://ia600605.us.archive.org/BookReader/BookReaderImages.php?zip=/10/items/VajnameShayest/vajname%20shayest_jp2.zip&file=vajname%20shayest_jp2/vajname%20shayest_$n.jp2&scale=1&rotate=0\"; file sns_$n.jpg; done"
}
```


### [2026-09-07T18:29:54.108Z] TOOL RESULT

```
sns_0022.jpg: ASCII text
sns_0158.jpg: ASCII text
```


## [2026-09-07T18:29:57.825Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && head -c 300 sns_0022.jpg; echo; echo \"--- try services img\"; curl -s -L -o t1.jpg \"https://archive.org/download/VajnameShayest/page/n22.jpg\" -w \"%{http_code} %{content_type}\\n\"; file t1.jpg"
}
```


### [2026-09-07T18:30:00.185Z] TOOL RESULT

```
Error serving request:
  Image error: not found


--- try services img
200 image/jpeg
t1.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1073x804, components 1
```


## [2026-09-07T18:30:06.987Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && for n in 21 157; do curl -s -L -o sns_n$n.jpg \"https://archive.org/download/VajnameShayest/page/n$n.jpg?fit=height&height=2400\" -w \"n$n: %{http_code} %{size_download}\\n\"; file sns_n$n.jpg; done"
}
```


### [2026-09-07T18:30:12.249Z] TOOL RESULT

```
n21: 200 113320
sns_n21.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1073x804, components 1
n157: 200 135853
sns_n157.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1094x804, components 1
```


## [2026-09-07T18:30:15.183Z] TOOL CALL #87: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/sns_n21.jpg"
}
```


### [2026-09-07T18:30:15.209Z] TOOL RESULT

```

```


## [2026-09-07T18:30:34.523Z] TOOL CALL #88: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/sns_n157.jpg"
}
```


### [2026-09-07T18:30:34.544Z] TOOL RESULT

```

```


## [2026-09-07T18:30:41.786Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -s -L -o sns_n159.jpg \"https://archive.org/download/VajnameShayest/page/n159.jpg?fit=height&height=2400\" -w \"%{http_code} %{size_download}\\n\""
}
```


### [2026-09-07T18:30:44.147Z] TOOL RESULT

```
200 129673
```


## [2026-09-07T18:30:47.317Z] TOOL CALL #90: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/sns_n159.jpg"
}
```


### [2026-09-07T18:30:47.337Z] TOOL RESULT

```

```


## [2026-09-07T18:31:00.670Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Filz\" BRT.txt | head -6"
}
```


### [2026-09-07T18:31:00.713Z] TOOL RESULT

```
18948:KompA.,  E.;  vgl.  auch  *»^maÜj.  —  Zum  V. nam-  '(sich)  heraL beugen',  vgl.  nhd.  reit  und ags.  Aiissan  'liltem'.  S.  auch  JOHANSSON  IF. 3.  54.  —  np.  namad  'grober  Teppich;  Filz'  3).
```


## [2026-09-07T18:31:03.947Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18935,18960p' BRT.txt | cut -c1-500"
}
```


### [2026-09-07T18:31:03.996Z] TOOL RESULT

```
^"Eiweitening'  zu  lit.  ahiti,  kil.  nesli  'tragen' ; vgl.  ksl.  n&&,  j-Aor.;  S  338.  a.  —  Pü.  (lu  Y. 44,  61):  ntlaitl),  (lu  70):  nhiiiehilati,  (10  A): iurlan,  Sü,  (lu  A,):  samänetum.  —  •)  Nach dem  Metnim  zu  streichen.  —  ')  In  Anlehnung an  Y.  44.  13.  —  3)  Oder  kaillant  Vgl. West Sg.-Gloss.  353,  2Ö0.
•  j.  "nä^tanam  aajanka  Yt2. 12,  14,
j.  nähmea  Vyt.  25:  lies  tiäämna-,
•  j.  'ni§9nuia-  Ad}.,  Pj-AorM.:  s.  'nas-.
•  j.  'nääamna-  Adj.,  Pj-AorM.:  s.  'nas-.
g,  nä!ü  Y.  JA  5  1  E.  MOS-.
•  j.,  p.  nah-  m.  'Nase',  Sing,  und  Du.: Waäamsaiy  uta  nüham  utä  gausa  fraja- nam  Bh.  2. 14;  13;  —  yim  yava  vatim närahabya  hubaoüitim^m  ßgaurva  H. 2.8;  26;  —  t^m  vahm  ninhaya  (LS.)'> *uzgnmiiiysil.2.8;  a6;  —  «Jw^a  (ND.)'' F.jd; — yaha  *nänhai''  Aaca  *gaoSaäbya ydha  vä  gaosa  Aaca  *^raaAiiya  (sd.)  P.  28.
Vgl.  nSshan:  —  ai.  Has-:nas-  m.j  mp.  näk (?;  aus  *«äAail).  —  Pii.:  vinU.  —  ')  LS.  im Sinn  des  IS.;  oder  ist  die  Form  ein  zum  ND. neugehildeter  IS.?  S  22J.  3.  —  ')  Oder  IS., oder  allenfalls  auch  NS.  zu  niohan-.  —  3)  Hdi. ittha,  aber  Pu. :  vliük.
•  g.  n»  Part,:  s.  unter  ti3.
namaDhan-  i  oäS
j.  n>l}ma  N.  ^\  lies  nititna.
j.  tanf,  Verbalf.:  s.  unter  nam-.
•  j.  n«mata-"  m,  1)  'Reisig':  nasui  tga- 'kaite  .  ,  7flä(i  .  .  'tS  tarS  yan  "die  A''. verschwindet . .  wie  übers  Jahr  das  (dürre) Reisig"  V.p.  46'';  —  avi  Um  spayUt  . . vJspaca  avi  tiyra  *-ia  ".  .  und  auf  lauter spitzes  (dorniges)  Reisig"  V.J.35; — katgAus .  .  äraasca  *'taheca  ayanheca  "die  Nutz- niessung  von  Holz  und  Reisig  und  Eisen- gerät"  V.5.38.  2)  'Geflecht  aus  Reisig, Hürde'  (nur  Komp.),
KompA.,  E.;  vgl.  auch  *»^maÜj.  —  Zum  V. nam-  '(sich)  heraL beugen',  vgl.  nhd.  reit  und ags.  Aiissan  'liltem'.  S.  auch  JOHANSSON  IF. 3.  54.  —  np.  namad  'grober  Teppich;  Filz'  3).
—  Pü.:  namal;  (luV.j):  apdnnatdl,  un- klar. —  1)  NA.  schwankt  iwischen  niot'  und «im\  Vgl.  auch  das  ai.  LW.  namaJa-,  das ein  mp.  nam-  voraussetit.  —  =)  Die  dün  ge- wordenen  Reiser  der  Bäume  werden  von  den Frühjahrsstürraen  abgerissen  und  verwebt  — U  Vgl.  dazu  oben  Bed.  2.
•  j.  *namato.-aiwi.varana-'*  n.  'Unter- schlupf,   Hütte    aus  Reisiggeflecht"*:  yat
däuru.upa.darane  va  'ne  vä  spS  vs  nä  va
irihyat  V.S.i.
Eig.'ReisigCgeflechtjbedeckung',— Pü.:  nama' apar  nihumbih.  ~-  ')  NA.  tum".  —  s)  Im  Folgen- den als  nmäna-  bezeichnet.
•  j.  *nama8kä-"  f.  'Reisig'  als  Feuerungs- material'>:  yat  .,  mafyaAa  daluayasö  avi atnm  abarjnti  .  .  aft>m  alstmm  yS  vaoce 'ka  nqma  Yl/4-55-
Zu  tamaia-  wie  ai.  asialkä-  (BloouPIeld  SBE. 43-  278)  zu  avalä-  m.  —  0  Wegen  M  s.  S  36S. 50.  NA.  hat  lamAia,  was  ich  nicht  für awestisch  ansehen  kann.  Vgl.  Var.  —  >)  Das aber  zu  verwenden  verpönt  war.
■  j.,  g.  namaohan-  Adj.  1)  ehrfurchtig': *asaca  'tshana  (IS.)  ux^ne  (sd.)  xra'^we yaomm  (sd.)    aste  V.^,  45.  2)    'ehr-
furchtsvoll bittend,  betend' :  yi  mq%ra  (sd.) *vaam  .  .  baraitT  urvahu  aia  *nAa  (NS-) Y.50.  6;  —  vastryS  yyaoHanats  fnfys  Aas Auxratus  -»Aä  yS  . .  "der  Bauer,  der  in seinem  Tun  gerecht  ist,  der  einsichtsvolle, wenn  er  (zu  dem)  betet,  der  . ."  Y.  5/. 5  j  —  yH^i  'nAa  (NS.)  vaHm  baraili  yal gaosXsAyit  Yt  10.  85 ''.
Ableit.  aus  ^mmak:  —  ai.  vgl.  namaniB- Adj.
—  Pü.  (zu  Y.):  nySyünSmandlh,  (zu  Y.  57): ke  varzUar  fa  iuniSn  Kul  fa  Aiaaiän  Auxral Aä/  pa  nyäySn,  (zu  Y.  ySy.  aAräiih  nyäyisn giißär'),  erl.:  ö  iär  u  katpai  franämem.  — i>  Anscheinend  nach  Y.  jo.  ö  geformt.  — 3)  So  bei  Mills.
dby  Google
```


## [2026-09-07T18:31:23.692Z] TOOL CALL #93: WebSearch

```json
{
 "query": "Proto-Iranian *namadka- \"salt\" etymology Persian namak Sogdian nmδk Khotanese"
}
```


## [2026-09-07T18:31:24.905Z] TOOL CALL #94: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/namadka",
 "prompt": "Does this reconstruction page exist? If so give the reconstructed form, meaning, etymology and descendants."
}
```


### [2026-09-07T18:31:26.679Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:31:29.169Z] TOOL RESULT

```
Web search results for query: "Proto-Iranian *namadka- "salt" etymology Persian namak Sogdian nmδk Khotanese"

Links: [{"title":"(PDF) Cultural semantics of the 'salt' word in Persian","url":"https://www.academia.edu/86261982/Cultural_semantics_of_the_salt_word_in_Persian"},{"title":"Cultural semantics of the 'salt' word in Persian","url":"https://benjamins.com/catalog/ijolc.21038.ara"},{"title":"نامه - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%85%D9%87"},{"title":"nmk' - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/nmk'"},{"title":"namak meaning - Persian (Farsi) Dictionary","url":"https://www.chaiandconversation.com/persian/word/namak"},{"title":"Jashak salt dome","url":"https://en.wikipedia.org/wiki/Jashak_salt_dome"},{"title":"Naman, Iran","url":"https://en.wikipedia.org/wiki/Naman,_Iran"},{"title":"Delal sauce","url":"https://en.wikipedia.org/wiki/Delal_sauce"},{"title":"Saltaneh","url":"https://en.wikipedia.org/wiki/Saltaneh"},{"title":"नमक - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%AE%E0%A4%95"}]

Based on the web search results, I found relevant etymological information about the word for salt across Iranian languages:

The term derives from Proto-Iranian *namadka-, with the Bactrian cognate namilgo. The search results show that this Proto-Iranian root reflects the word for salt across various Iranian languages, including Persian namak. Additionally, the search results reference etymological sources including Edelʹman's Etymological Dictionary of Iranian Languages and MacKenzie's Concise Pahlavi Dictionary, which document this linguistic connection.

The results confirm that this is a well-established etymology within Iranian historical linguistics, showing the regular phonetic and morphological developments from the Proto-Iranian ancestor to the attested forms in Middle Persian and later Iranian languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T18:31:32.761Z] TOOL CALL #95: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/nmk%27",
 "prompt": "For the Middle Persian entry nmk' (namak) \"salt\": give the full etymology — Proto-Iranian reconstruction, any Avestan form, cognates (Sogdian, Bactrian, Khotanese, Khwarezmian) and cited authorities."
}
```


### [2026-09-07T18:31:38.674Z] TOOL RESULT

```
# Etymology of Middle Persian nmk' (namak) "salt"

Based on the Wiktionary entry provided, here is what can be stated about the etymology:

**Proto-Iranian Reconstruction:**
The word derives from Proto-Iranian "*namadka-" according to the source material cited.

**Cognates:**
The entry specifically mentions Bactrian "ναμιλγο" (namilgo) as a comparative form.

**Cited Authority:**
The etymology cites Edelʹman's "Etymological Dictionary of Iranian Languages" (2015, volume 5, Moscow: Vostochnaya Literatura, page 464) as the primary source for the Proto-Iranian reconstruction.

**Limitations:**
The webpage does not provide Avestan forms, Sogdian cognates, Khotanese cognates, or Khwarezmian cognates—only the Bactrian parallel is mentioned. The entry also references MacKenzie's "A concise Pahlavi dictionary" (1971) but without additional etymological details beyond confirming the word meaning "salt."

To obtain more complete cognate information across Iranian languages, you would need to consult the full Edelʹman dictionary directly.
```


## [2026-09-07T18:32:12.642Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41160,41185p' LAT.txt"
}
```


### [2026-09-07T18:32:12.689Z] TOOL RESULT

```
dans gr. aveyioS "fils de la soeur" et v.sl.netij t "neveu" (s .ndtjak
"fils de la soeur"), a v.naptya- "descendant", nava-naptya "neuvifeme
giniration", alb. mbese "niece" (peut-etre emprunti a un latin . ne-
potia ?). - Lat. pronepos est a rapprocher' de skr. pranaptar- "arriere-
petit-fils". Emprunts itrusques nefts "nepos", prunts "pronepSs".
Neptunus, -i m.: Neptune; dieu marin. Usiti de tout temps; con¬
servi partiellement dans les 1 . romanes, avec un sens dirivi (fr.
lutin); M.L. 5894. De la: neptunius, -a,-um-, neptunia f.: nom d’une
piante (Ps.Apul., Herb.57); neptunicola (Sil.); Neptunalia.
Le rapport avec av. napta- "humide" est vague. Bien que la diri-
vation de Neptunus ne s'explique pas par IA, on ne peut s'empecher
de penser a 1 'importante figure religieuse indo-iranienne de ved.
ap&m napat , av. apam napi "descendant des eaux"; cf. fortuna A cote
de fortuitus , en face de fors', le mot releverait du vocabulaire reli
gieux commun a 1 1 indo—iranien et a 1 *italo—celtique. D’autre part,
NeptUnus serait formi comme tribunus et dominus s'il avait existe
un *neptu- "substance humide". Emprunt itrusque NeQunst
nepus ( u?):non purus, P.F.163,15* Si la glose est exacte, nepus
pourrait etre un ancien terne de rituel, issu de *ne + put-s, cf.
skr. putah, d'une racine *pewa-/pu-, qu'on a dans purus . Le second
terne du composi n'aurait pas de voyelle thimatique, ce qui repri-
sente 1 'itat ancien; cf .compos en face de potis, etc.
V. ne.
nequalia: y.nex.
nequam: mot invariable composi de la nigation ne et de la par-
ticule indefinie quam, cf. per-quan, quis-quan, 1 'indifini^ pouvant
```


## [2026-09-07T18:32:21.457Z] TOOL CALL #97: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=Neptune",
 "prompt": "What does the American Heritage Dictionary say for Neptune — the etymology and any Indo-European root cross-reference?"
}
```


### [2026-09-07T18:32:25.535Z] TOOL RESULT

```
# Neptune Etymology

According to the dictionary entry, the etymology for Neptune is concise:

**Etymology:** The word traces back to "[Latin _Neptūnus_](https://www.harpercollins.com/products/the-american-heritage-dictionary-of-indo-european-roots-third-edition-calvert-watkins)"

**Indo-European Root Reference:** The entry does not provide a specific cross-reference to an Indo-European root for Neptune itself. However, the page notes that the dictionary includes an appendix of Indo-European roots available online, suggesting users can consult those resources for deeper etymological information on words that derive from proto-languages.
```


## [2026-09-07T18:32:35.377Z] TOOL CALL #98: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nebula",
 "prompt": "Give the full etymology of nebula (date of first English use, Latin source, PIE root) and, if present on the page, of nimbus."
}
```


## [2026-09-07T18:32:36.081Z] TOOL CALL #99: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nimbus",
 "prompt": "Give the full etymology of nimbus: date of first English use, Latin nimbus meaning, and the PIE root/related forms cited."
}
```


### [2026-09-07T18:32:40.973Z] TOOL RESULT

```
# Etymology of Nebula and Nimbus

## Nebula

**First English Use:** Mid-15th century

**Etymology:** The word "nebule" originally meant "a cloud, mist," derived from Latin *nebula* (plural *nebulae*), meaning "mist, vapor, fog, smoke, exhalation," and figuratively "darkness, obscurity."

**PIE Root:** *nebh-*, meaning "cloud"

**Development:** The term was re-borrowed from Latin in the 1660s referring to "cataracts in the eye," with the astronomical sense of "luminous cloud-like patch in the heavens" emerging around 1730. By the 1920s, astronomers using the Mt. Wilson telescope distinguished nearby cosmic gas clouds from distant galaxies.

## Nimbus

**First English Use:** 1610s

**Etymology:** From Latin *nimbus*, meaning "cloud," which "is perhaps related to nebula"

The page notes that nimbus originally described "bright cloud surrounding a divine or sacred personage."
```


### [2026-09-07T18:32:41.641Z] TOOL RESULT

```
# Etymology of Nimbus

**Date of First English Use:** 1610s

**Latin Origin:** The word comes from Latin *nimbus*, meaning "cloud," with a possible connection to *nebula* ("cloud, mist").

**PIE Root:** The Latin term traces back to the Proto-Indo-European root *\*nebh-*, which means "cloud."

**Semantic Development:** Initially referring to "a bright cloud surrounding a divine or sacred personage," the meaning evolved by 1727 to denote "a halo around the head of a representation of a divine or sacred person" in religious art, and acquired figurative uses by 1860.

**Related Forms:** Words derived from the same PIE root include *nebula*, *nebular*, *nebulous*, and the meteorological term *nimbostratus* ("a thick, low, dark cloud from which rain or snow falls").
```


## [2026-09-07T18:33:10.119Z] TOOL CALL #100: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cp $SP/sns_n21.jpg data/verification/sources/refs/ocr/SNS/11.png && cp $SP/sns_n159.jpg data/verification/sources/refs/ocr/SNS/282.png && cat > data/verification/sources/refs/ocr/SNS/11.vision.txt <<'EOF'\n[SNS = Tavoosi, Vazhe-name-ye Shayast ne Shayast, printed p. 11 = archive.org VajnameShayest\nleaf n21, LEFT-hand page (running head numeral ۱۱; the right half of the same leaf is p. ۱۰).\nImage saved as 11.png. Transcribed from the page image by hand (the OCR of this book is unusable),\n2026-09-07, for the verification of PDF page 353 (root Nebh/Nembh/Ombhro, nodes abr / abrāmōn).]\n\np. 11, line 7:\n  <Pahlavi script> : avr/abr : ابر.\n     ستا awar-/awra- ، سا abhrá- ، پا awar (مینو خرد).\n     این واژه به شکل <Pahlavi script> هم آمده است.  ک ۱۰/۲، ک ۵/۷، ک ۱۸/۱۰\n\np. 11, line 10:\n  <Pahlavi script> : abrāmōn : ابرآمون، پرابر، ابری.\n     (نک: āmōn)  ک ۱۰/۲\n\n(Legend used in this glossary: ستا = اوستا (Avestan), سا = سانسکریت (Sanskrit),\nپا = پازند (Pazand), فاتر = فارسی میانهٔ ترفانی/مانوی, ک = ارجاع به متن شایست نه شایست\n(فصل/بند).)\n\nOther entries on the same page: nuh «۹»، nava- (سندی کهن), 9999 «نه هزار و نهصد و نود و نه»،\npid «پدر» (Junker 96, pitar-, pilār-, pit), pidar «پدر».\nEOF\ncat > data/verification/sources/refs/ocr/SNS/282.vision.txt <<'EOF'\n[SNS = Tavoosi, Vazhe-name-ye Shayast ne Shayast, printed p. 282 = archive.org VajnameShayest\nleaf n159, RIGHT-hand page (running head numeral ۲۸۲; the left half of the leaf is p. ۲۸۳).\nImage saved as 282.png. Transcribed from the page image by hand, 2026-09-07, for the\nverification of PDF page 353 (root Nebh/Nembh/Ombhro, nodes namb / namak).]\n\np. 282, line 3:\n  <Pahlavi script> : namb : نمب، نم، رطوبت.\n     ستا : napta- از √nab ، سندی کهن : nambh-, nabh-\n     ک ۹۲/۲، ک ۱۰/۵   (GNPE. 232)\n\np. 282, line 5:\n  <Pahlavi script> : namad : کَمَد (فرش یا چیزی که از پشم مالند).\n     ستا : nəmata- (AiWb. 1068)   ک ۱۰۱/۲–۱۰۲\n\np. 282, line 7:\n  <Pahlavi script> : namak : نمک.   ک ۱۷/۲\n\n(GNPE = P. Horn, Grundriss der neupersischen Etymologie — i.e. Horn p. 232, his no. 1039\n«nem 'feucht; Feuchtigkeit'», which is exactly the page Nourai also cites as HRN:232.)\n\nOther entries on the page: nimāyēnd, nimūd, nimūd ēstēd, nimūdan, vināh, vināh vizārdan …\nEOF\nls -la data/verification/sources/refs/ocr/SNS/"
}
```


### [2026-09-07T18:33:11.470Z] TOOL RESULT

```
total 1676
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  7 14:33 .
drwxrwxr-x 13 sfmqrb sfmqrb    4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  113320 Sep  7 14:33 11.png
-rw-rw-r--  1 sfmqrb sfmqrb    1202 Sep  7 14:33 11.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1389 Sep  4 16:10 14.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  129673 Sep  7 14:33 282.png
-rw-rw-r--  1 sfmqrb sfmqrb    1057 Sep  7 14:33 282.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  410799 Sep  6 11:23 299.png
-rw-rw-r--  1 sfmqrb sfmqrb    1281 Sep  6 11:23 299.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1220 Sep  4 15:51 6.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1021826 Sep  7 12:18 74.png
-rw-rw-r--  1 sfmqrb sfmqrb    1450 Sep  7 12:18 74.vision.txt
```


## [2026-09-07T18:33:29.599Z] TOOL CALL #101: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9b%CA%B0os|page 353 root Nebh/Nembh/Ombhro: PIE *nebhos 'cloud, mist' and root *nebh-, descendants incl. Avestan/Latin/Greek\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%85|page 353 node 3: Persian نم nam < MP nam < Proto-Iranian *nabah- < PIE *nebhos\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%AA|page 353 node 4: Persian نفت naft < MP npt' naft 'moist; naphtha', loans into Ottoman Turkish/Russian etc.\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%85%DA%A9|page 353 node 6: Persian نمک namak < Middle Persian namak\" \\\n \"https://en.wiktionary.org/wiki/nmk%27|page 353 nodes 5-6: Middle Persian nmk' namak 'salt' < Proto-Iranian *namadka- (Edel'man ESIJa V 464), Bactrian namilgo\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%AD%E0%A5%8D%E0%A4%B0|page 353 node 8: Sanskrit abhra- < PII *abhras < PIE *n-bhros, cognate Av. aBra-, Pers. abr (refutes BQT:79 ap+bhr analysis)\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1|page 353 node 10: Persian ابر abr < MP 'pl abr < Proto-Iranian *abrah < PIE *n-bhros\" \\\n \"https://www.etymonline.com/word/naphtha|page 353 node 4 NOTE: naphtha, Greek/Persian/Aramaic-Akkadian competing origins\" \\\n \"https://www.etymonline.com/word/Neptune|page 353 node 11/14: Latin Neptunus probably from PIE *nebh- 'cloud, moist'; English Neptune late 14c\" \\\n \"https://www.etymonline.com/word/nebula|page 353 node 16: English nebula < Latin nebula < PIE *nebh-\" \\\n \"https://www.etymonline.com/word/nimbus|page 353 node 16: English nimbus (1610s) < Latin nimbus 'cloud', related to nebula, PIE *nebh-\" \\\n \"https://www.ahdictionary.com/word/search.html?q=Neptune|page 353 node 11: AHD online gives only 'Latin Neptunus' with no IE root cross-reference (Nourai's AHD ref not confirmed)\" \\\n \"https://vajehyab.com/?q=%D9%86%D9%BE%D8%AA%D9%88%D9%86|page 353 node 13: Persian نپتون from French (فر.), planet and Roman sea god, Dehkhoda + Mo'in\" \\\n ; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "timeout": 300000
}
```


### [2026-09-07T18:33:35.549Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/23ddd405d4755f67.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0626632ff2d06ce9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f20e1d7aabe13bc8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/821fc9a7c6e1802c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05a38e5eb84c826e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee97204589045edd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/866660edcb1e99a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9c82fce9c896780.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/005b3da8a7bba604.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32585d32ffad1ae4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bc1c84fe1423b260.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/25a046c93b3b0011.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4b8c65afacafb5b.txt
```


## [2026-09-07T18:33:41.771Z] TOOL CALL #102: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://vajehyab.com/?q=%D9%86%D9%85%DA%A9&d=moein\" --note \"page 353 node 6: Mo'in's online entry for نمک (no origin tag online; MON:4818 page not mappable)\" 2>&1 | tail -1; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T18:33:43.371Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aeb779d9012977a1.txt
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


## [2026-09-07T18:33:46.309Z] TOOL CALL #103: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-07T18:33:46.360Z] TOOL RESULT

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


## [2026-09-07T18:33:51.346Z] TOOL CALL #104: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-316.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2000])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


### [2026-09-07T18:33:52.729Z] TOOL RESULT

```
{"pdf_page": 316, "book_page": 286, "verified_by": "claude-opus-5", "verified_on": "2026-09-06"}
{
 "entry": 0,
 "root": "Mâ, Mâ-ter",
 "verdict": "plausible",
 "modern_form": "PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)",
 "note": "Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in node #8.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *méh₂tēr «مادر» (پوکورنی ۷۰۰–۷۰۱) و واژهٔ کودکانهٔ *mā- (پوکورنی ۶۹۴) هر دو واقعی اند و برچسب «هندواروپایی» درست است؛ امّا دو نکتهٔ معنایی از خود نورایی است: یکی آنکه پوکورنی در ص ۶۹۴ mā-3 را «مادر» معنی کرده و نه «پستان» — معنای پستان تنها از مشتقّات دوگان‌شده (mamma, mamilla لاتینی) برمی‌آید؛ دوم آنکه تفسیر «mā-ter = خوراک‌دهندهٔ خانواده» پسوند -ter- را پسوند فاعلی گرفته، در حالی که واتکینز و والده‌پوکورنی آن را پسوند واژگان خویشاوندی می‌دان
{
 "id": 1,
 "lang": "Avestan",
 "words": "mâtar",
 "verdict": "confirmed",
 "derivation": "Avestan mātar- f. ‘mother’ is the regular Iranian reflex of PIE *méh₂tēr (nom. *mātē, stem *māter-) via Proto-Iranian *máHtā: the PIE laryngeal *h₂ is lost with lengthening of the vowel, and *-ter- is retained. It is attested in the Younger Avesta (V. 12.1 yaṭ pitā vā mātā vā parəiriθyāiti ‘if father or mother dies’, Yt. 17.16, Y. 38.5 of animal mothers). Old Persian has the same stem, preserved only in the haplologised compound hamātā < *hama-mātā ‘having the same mother’ (Bisitun I 30, of Smerdis and Cambyses). Sanskrit mātár-, Greek Doric mātēr, Latin māter are the exact cognates, so the arrow root → Avestan is correct.",
 "derivation_fa": "اوستایی mātar- «مادر» بازماندهٔ قاعده‌مند هندواروپایی آغازین *méh₂tēr است که از راه ایرانی باستان *máHtā به اوستا رسیده؛ حنجرهٔ هندواروپایی افتاده و در عوض واکه کشیده شده است. این واژه در اوستای نو (وندیداد ۱۲،۱) گواهی دارد و در پارسی باستان تنها در ترکیب hamātā «همان مادری» (سنگ‌نوشتهٔ بیستون) مانده است. بارتولومه (فرهنگ ایرانی باستان، ستون ۱۱۶۷) و کنت همین را می‌گویند؛ پس این پیوند در نمودار نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%F0%90%AC%A8%F0%90%AC%81%F0%90%AC%99%F0%90%AC%80%F0%90%AC%AD",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "partial",
   "note": "Pokorny p.694 (mā-3) does NOT list Avestan mātar-; the Avestan form stands in the neighbouring lemma 'mahter-' … 'Old Indic matar- ‘mother’, Avestan matar-, Armenian mayr … Page(s): 700-701' (POK_full.txt l.57703ff). So the claim is right but the page number should be 700."
  },
  {
   "ref": "SKT:336",
   "status": "partial",
   "note": "Skeat's entry is real but not on p.336 of the edition on disk: 'Mother (1), a female parent. [M.E.] moder. A.S. mōdor … + Du. moeder, Icel. mōðir … L. mater, Gk. mētēr, Skt. mātā, mātṛ … formed with Aryan suffix -tar (of the agent) from √MĀ, orig. to measure … Orig. sense uncertain, perhaps ‘manager’ of the household' — SKT.txt leaf 318, i.e. printed p. ~298 of the 1911 impression (leaf = printed+20); leaf 356 = p.336 is the 'Parity–Parsee' page. Content supports Av./Skt. mātar- as source of ‘mother’, but Skeat's own etymology is √MĀ ‘to measure’, i.e. ‘manager’, not Nourai's ‘feeder’."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "col. ~1167 (lea
```


## [2026-09-07T18:36:05.555Z] TOOL CALL #105: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef marks(i):\n    for j in range(i, i-6, -1):\n        m=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', t[j])\n        if m: return j, m\n    return None\nfor key in ['nebula,  n.,  a  cloudlike','Neptune,  n.,  1)','nimbus,  n.,  1)','imbricate,  adj.']:\n    for i,p in enumerate(t):\n        if key in p:\n            print(key[:20], 'leaf', i, 'nearest marker', marks(i))\n            break\nEOF\necho \"=== SKT nebula\"; grep -n \"Nebula\\|Neptune\" SKT.txt | head -5"
}
```


### [2026-09-07T18:36:07.079Z] TOOL RESULT

```
nebula,  n.,  a  clo leaf 553 nearest marker (553, ['1035'])
Neptune,  n.,  1) leaf 557 nearest marker (556, ['1040'])
nimbus,  n.,  1) leaf 561 nearest marker (559, ['1046'])
imbricate,  adj. leaf 415 nearest marker (415, ['772', '773'])
=== SKT nebula
12206:Nebula,  a  little  cloud,  vt.)     U  m*i +  Gk.  vi-piKfj,  dimin.  of  y(^<n,  cload.iB bkt.  nabhas,  sky,  xlber,  from  imM.  tobi (from  the  barsting  of  nuA'doodi). NAIUI)     Sec  Nave  (1).
12525:Nuptial    (F.  -  U)     F. Huptialis,   belonging  to  a nnptitt.  s.   pi.  a   wedding  —  L.  i bride;  fern,  of  pp  of  mt^rt,  to '  to  veil.'     Allied  to  Nebula.
```


## [2026-09-07T18:36:18.943Z] TOOL CALL #106: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/PLA; grep -n \"naft\\|nafṭ\\|Naphta\" incoming/PLA/*.txt 2>/dev/null | head -8"
}
```


### [2026-09-07T18:36:19.004Z] TOOL RESULT

```
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt:19020:us naft: "Naphtha" aus pers. us naft mp. Yo' naft 1 aw. naphtha 2, 
incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt:19022:pers. näft: "Naphtha, Erdpech'"' ar. naft, aram.s0»), tk. naft, neft 
incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt:19023:Hieraus griech. va va ,„ lat. naphtha, sp. nafta, frz. Nephtha, russ, 
incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt:19038:As- naft = naft a. v. 
incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt:19042:ana - naftiyya: "Feuerwerk" s. naft. 
incoming/PLA/PLA_pages.txt:14669:us          naft:        "Naphtha"              aus    pers. us naft                          mp. Yo' naft        1       aw.     naphtha           2,
incoming/PLA/PLA_pages.txt:14671:            pers.       näft:        "Naphtha,             Erdpech'"'                  ar.    naft,      aram.s0»),        tk.        naft,     neft
incoming/PLA/PLA_pages.txt:14672:            Hieraus        griech.          va        va        ,„    lat.      naphtha,          sp.   nafta,   frz.     Nephtha,            russ,
```


## [2026-09-07T18:36:22.642Z] TOOL CALL #107: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14660,14685p' incoming/PLA/PLA_pages.txt; echo \"=== page tag\"; awk 'NR<=14669 && /\\[pdf page/ {v=$0} END{print v}' incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-07T18:36:23.879Z] TOOL RESULT

```
ei           - na°nä®           = naCna’          q. u.

Fa -na°na®                 = na°nä°             a. v.


bb) - naffät:                   "derjenige,                der Naphtha                 bereitet".


us          naft:        "Naphtha"              aus    pers. us naft                          mp. Yo' naft        1       aw.     naphtha           2,
            syr. N\a3 , mand.                   napt °.
            pers.       näft:        "Naphtha,             Erdpech'"'                  ar.    naft,      aram.s0»),        tk.        naft,     neft
            Hieraus        griech.          va        va        ,„    lat.      naphtha,          sp.   nafta,   frz.     Nephtha,            russ,
            neft,       dtsch.          Naphtha        a
            Naphtha       <Tassyr. >>) pers. >                                  griech       5,


e>- nufugß:               Pl.        v.    ass nuffa                  q.   v.


ana - nufßa = näffa q. v.

zer              -    nafrinag:           "eine       Süßigkeit'"                pers.       6, wahrscheinlich            aus     pers.
            ferini        "Reisbrei"


=== page tag
```


## [2026-09-07T18:36:31.780Z] TOOL CALL #108: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=14669' incoming/PLA/PLA_pages.txt | grep -n \"pdf page\" | tail -2; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d.get('PLA',{}).get('page_offset'));print(d.get('PLA',{}).get('lookup_hint'))\""
}
```


### [2026-09-07T18:36:33.183Z] TOOL RESULT

```
301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-07T18:36:37.071Z] TOOL CALL #109: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'naft:' in p and 'Naphtha' in p:\n        print('leaf(1-based)',i+1,'printed page',i+1-15)\n        break\nEOF"
}
```


### [2026-09-07T18:36:38.386Z] TOOL RESULT

```
leaf(1-based) 277 printed page 262
```


## [2026-09-07T18:36:50.897Z] AGENT

Now I'll write the verification file.


## [2026-09-07T18:45:42.886Z] AGENT

I'll write the verification file now, then run the checker.


## [2026-09-07T18:53:36.407Z] TOOL CALL #110: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk353.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9b%CA%B0os\"\nW_NAM   = \"https://en.wiktionary.org/wiki/%D9%86%D9%85\"\nW_NAFT  = \"https://en.wiktionary.org/wiki/%D9%86%D9%81%D8%AA\"\nW_NAMAK = \"https://en.wiktionary.org/wiki/%D9%86%D9%85%DA%A9\"\nW_NMK   = \"https://en.wiktionary.org/wiki/nmk%27\"\nW_ABHRA = \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%AD%E0%A5%8D%E0%A4%B0\"\nW_ABR   = \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1\"\nE_NAPH  = \"https://www.etymonline.com/word/naphtha\"\nE_NEPT  = \"https://www.etymonline.com/word/Neptune\"\nE_NEB   = \"https://www.etymonline.com/word/nebula\"\nE_NIM   = \"https://www.etymonline.com/word/nimbus\"\nA_NEPT  = \"https://www.ahdictionary.com/word/search.html?q=Neptune\"\nV_NEPT  = \"https://vajehyab.com/?q=%D9%86%D9%BE%D8%AA%D9%88%D9%86\"\nV_NAMAK = \"https://vajehyab.com/?q=%D9%86%D9%85%DA%A9&d=moein\"\n\nPOK_ROOT = (\"POK_01.txt l.4645-4646 (printed pp.315-316): „2. (enebh-): nebh-, embh-, m̥bh- \"\n            \"(Kontaminationsform nembh-); z.T. emb-, omb- aus embh-, ombh-, ‚feucht, Wasser‘, daraus \"\n            \"‚Dampf, Dunst, Nebel, Wolke‘“, with the sub-lemmas nebhos-, nebhelā, m̥bh-(ro-), \"\n            \"emb(h)-:omb(h)- and nembh-.\")\n\nnodes = []\n\n# ---------------- node 1 ----------------\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"nab, napta\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Avestan has the verbal root nab- 'to moisten, to wet' (Bartholomae, AiW: \\\"j. nab- V. 'befeuchten, benetzen'\\\", \"\n  \"with the participle napta- and the absolutive napitīm) and its past participle YAv. napta- 'moist, wet', \"\n  \"used in Vd. 7.30-35 of wet as against dry firewood (frabāzu.drājaŋ yat naptanăm 'the length of a \"\n  \"frabāzu of moist (wood)') and in the compound expression aiβi.naptīm asti 'he besmirches (= wets) with \"\n  \"blood' (Vd. 7.12f.). Phonetically the root is the Iranian reflex of PIE *nebh- (IIr. *nabh-, with Iranian *bh > b), \"\n  \"and the participle *nab-ta- gives napta- by regressive devoicing of b before t — exactly Pokorny's *nab-ta-. \"\n  \"One inexactness: Nourai's \\\"nab\\\" is a verbal ROOT (Horn writes √nab-, namb-), not a noun meaning 'moisture'; \"\n  \"the Avestan NOUN of this family, Gathic nabah- n. (Y. 44.4), means 'air-space, sky', not 'humidity'.\"),\n \"derivation_fa\": (\n  \"در اوستا ستاک فعلی nab- «تر کردن، نمناک کردن» و اسم مفعول آن napta- «تر، نمناک» گواهی دارد (بارتولومه، \"\n  \"فرهنگ ایرانی باستان؛ وندیداد ۷/۳۰–۳۵ در برابر huška- «خشک»). این ستاک بازماندهٔ قاعده‌مند ریشهٔ هندواروپایی \"\n  \"آغازین *nebʰ- است: bʰ هندواروپایی در ایرانی به b بدل شده و در *nab-ta- پیش از t بی‌واک شده و napta- داده است. \"\n  \"تنها بی‌دقتی نمودار این است که «nab» ستاک فعلی است و نه اسمی به معنی «رطوبت»؛ اسم این خانواده در اوستای گاهانی \"\n  \"nabah- است که «فضای آسمان، آسمان» معنی می‌دهد نه «نم». ادعای نورایی در کل درست است.\"),\n \"sources\": [W_PIE, W_NAFT],\n \"ref_check\": [\n   {\"ref\": \"POK:316\", \"status\": \"supports\",\n    \"note\": (\"POK_01.txt l.4659 (printed p.316): „av. aiβi-naptīm asti ‚er (befeuchtet =) besudelt mit Blut‘, \"\n             \"napta- ‚feucht‘ (*nab-ta-) npers. neft ‚Naphtha‘“ — the Avestan root/participle and the \"\n             \"moisture sense are exactly as the chart draws them.\")}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. nab-, napta-, nabah- (BRT.txt ll.18556-18568, cols. ~1039-1041)\",\n    \"stance\": \"supports\",\n    \"note\": (\"\\\"j. napta- Adj. 'feucht': aētavat huškanam aēsmanam aētavat *tanam V. 7.31…\\\"; \\\"j. nab- V. \"\n             \"'befeuchten, benetzen'. PPfP. napta-, Absol. napitīm\\\"; but \\\"g. nabah- n., Plur. 'Luftraum, Himmel' \"\n             \"Y. 44.4\\\" — so 'moisture' belongs to napta-/nab-, 'sky' to nabah-.\")},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 276 s.v. *nab\", \"stance\": \"supports\",\n    \"note\": (\"Cheung 2007, *nab 'to make wet, moisten': \\\"AVESTAN: YAv. napía- (ppp.) 'moist, wet' || (+ *abi-) \"\n             \"YAv. aiβi.naptīm 'moistening' (V 7.12 f.)\\\"; \\\"PIE *neb'- 'to moisten, be wet' > LIV: 448 | Pok.: 315 f.\\\"\")},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 131 (WLD_Bd1_pages.txt l.11851)\", \"stance\": \"supports\",\n    \"note\": \"„av. aiβinaptǔm asti … (Bartholomae Airan. Wb. 92), napta- ‚feucht‘, npers. neft ‚Naphta‘“.\"}]})\n\n# ---------------- node 2 ----------------\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"namb\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Book Pahlavi nmb /namb/ 'moisture' continues the nasal-infixed variant of the root that Pokorny labels the \"\n  \"'Kontaminationsform' *nembh- (from *nebh- crossed with *embh-/*m̥bh-), i.e. OIr. *namba- beside *nab-ta-. \"\n  \"The same stem gives the MP verb nambistan/nambitan 'to moisten' (Walde-Pokorny: \\\"pehl. nambitan 'befeuchten'\\\") \"\n  \"and the Book Pahlavi translation of Av. hixtaiŋe 'to moisten' is glossed /namb kardan/ (Cheung). \"\n  \"MacKenzie's Concise Pahlavi Dictionary prints only the reduced form \\\"nam [nm] moisture\\\", i.e. both namb and nam \"\n  \"existed in MP, the cluster -mb- being simplified to -m- already in late MP; that is why Horn and Pokorny cite \"\n  \"\\\"pehl. namb, nam\\\" side by side. Latin nimbus (< *nembhos) is the exact Italic counterpart of this nasalised grade.\"),\n \"derivation_fa\": (\n  \"در فارسی میانه (پهلوی کتابی) nmb /namb/ «نم، رطوبت» گواهی دارد و بازماندهٔ گونهٔ خیشومی‌شدهٔ ریشه است که پوکورنی \"\n  \"آن را *nembʰ- (گونهٔ آمیخته از *nebʰ- و *embʰ-) می‌نامد؛ از همین ستاک فعل پهلوی nambistan/nambitan «نمناک کردن» \"\n  \"ساخته شده است. مکنزی در فرهنگ کوچک پهلوی تنها گونهٔ ساده‌شدهٔ nam را آورده، پس خوشهٔ -mb- در پایان دورهٔ میانه به \"\n  \"-m- ساده شده بود؛ به همین سبب هرن و پوکورنی هر دو گونهٔ namb و nam را در کنار هم نقل می‌کنند. لاتینی nimbus از \"\n  \"همین درجهٔ خیشومی *nembʰos است. ادعای نورایی درست است.\"),\n \"sources\": [W_NAM],\n \"ref_check\": [\n   {\"ref\": \"HRN:232\", \"status\": \"supports\",\n    \"note\": (\"Horn, Grundriss no. 1039 (HRN.txt \\\\f-leaf 253 = printed p. 232): \\\"nem 'feucht; Feuchtigkeit'. \"\n             \"aw. napta- 'feucht' (√nab-, namb- d. i. nabh-, nambh-); phlv. namb, nam.\\\" — the arrow \"\n             \"Avestan → Pahlavi namb is Horn's own.\")},\n   {\"ref\": \"SNS:282\", \"status\": \"supports\",\n    \"note\": (\"Šāyest nē Šāyast glossary p. 282 line 3 (read from the page image, saved as \"\n             \"data/verification/sources/refs/ocr/SNS/282.png + 282.vision.txt): «namb: نمب، نم، \"\n             \"رطوبت. ستا: napta- از √nab، سندی \"\n             \"کهن: nambh-, nabh- … (GNPE. 232)»; the book's own index confirms the page \"\n             \"(\\\"nambh-nabh- 282/3\\\", \\\"napta- 282/3\\\"). GNPE. 232 = Horn p. 232, i.e. Nourai's other reference.\")}],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"p. 276 s.v. *nab\", \"stance\": \"supports\",\n    \"note\": \"\\\"MIDDLE PERSIAN: BMP nmb 'moisture', MMP npt 'moist, damp, naphtha', BMP npt /naft/\\\"; and s.v. haec- he glosses YAv. hixtaiŋe 'to moisten' with the BMP translation \\\"/namb kardan/\\\".\"},\n   {\"src\": \"PHD\", \"where\": \"p. 57 (PHD_pages.txt l.3643ff)\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie has \\\"nam [nm | N ~] moisture\\\" and \\\"1naft [npt' | = M, N ~] moist, damp; naphtha\\\" but no headword namb — he lemmatises the simplified form only.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 131 (l.11905)\", \"stance\": \"supports\",\n    \"note\": \"„nembh-: pehl. namb, nam, np. nem ‚feucht, Feuchtigkeit‘, pehl. nambitan ‚befeuchten‘, lat. nimbus“.\"},\n   {\"src\": \"NYB\", \"where\": \"vol. II glossary (grep 'namb')\", \"stance\": \"silent\",\n    \"note\": \"Nyberg's ŠKZ/Pahlavi glossary has nothing under namb (only namāz, pand-namak and the unrelated ayinaftan, where he cites \\\"Av. (1041) nam-\\\").\"}]})\n\n# ---------------- node 3 ----------------\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"nam\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"New Persian نم nam 'moisture, damp' is MP namb with the regular late simplification of -mb- to -m- \"\n  \"(Horn transcribes the classical reading as nem; Pokorny \\\"npers. nem\\\"). The denominal verb NP namīdan/nam- \"\n  \"'to grow moist' is built on it (Cheung), and the noun is the source of the Turkic and Indic loans (Ottoman \"\n  \"Turkish نم nem, Azerbaijani nəm, Hindustani nam, Uyghur nəm). Cognate Iranian forms keep the \"\n  \"cluster: Baluchi namb 'dew, mist', Shughni namb 'moisture', Kurdish nim/nem, which is what secures MP namb as the \"\n  \"immediate ancestor. Wiktionary takes a slightly different route (NP nam directly from PIr. *nabah-, i.e. the \"\n  \"s-stem of Av. nabah-), but Horn, Walde-Pokorny and Klein all route it through the nasalised namb, which alone \"\n  \"explains the -mb- of the sister languages.\"),\n \"derivation_fa\": (\n  \"«نم» فارسی نو از فارسی میانهٔ namb است؛ خوشهٔ -mb- در گذر به فارسی نو ساده شده و به -m- بدل شده است \"\n  \"(هرن آن را nem می‌خواند و پوکورنی نیز «npers. nem» آورده). فعل «نمیدن» از همین اسم ساخته شده و صورت‌های \"\n  \"خویشاوند ایرانی — بلوچی namb «شبنم، مه»، شغنی namb، کردی nim/nem — نشان می‌دهند که صورت میانه با -mb- بوده است. \"\n  \"ویکی‌واژه آن را یکسر از ایرانی باستان *nabah- می‌گیرد، ولی هرن و والده‌پوکورنی و کلاین از راه namb می‌روند که \"\n  \"-mb- زبان‌های همریشه را توضیح می‌دهد. ادعای نورایی درست است.\"),\n \"sources\": [W_NAM, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:316\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt l.4645ff (p.316): „nembh-: pehl. namb, nam, npers. nem ‚feucht, Feuchtigkeit‘, pehl. nambītan ‚befeuchten‘; lat. nimbus“.\"},\n   {\"ref\": \"BQT:2167\", \"status\": \"supports\",\n    \"note\": (\"Borhan-e Qate' p. 2167 (vol. 4; fetched with tools/ref_page.py BQT:2167, cache ocr/BQT/2167.txt), \"\n             \"headword «نم» «بفتح اول و سکون ثانی… رطوبت اندک» with Mo'in's footnote 19: \"\n             \"«فارسی nam از namb … پهلوی namb، بلوچی namb (شبنم، مه) «اسشق ۱۰۳۹» ، کردی nem/niv (مرطوب)» \"\n             \"— i.e. Mo'in cites Horn no. 1039, the same chain as the chart.\")},\n   {\"ref\": \"HRN:232\", \"status\": \"supports\",\n    \"note\": \"Horn no. 1039 on printed p. 232: \\\"nem 'feucht; Feuchtigkeit'. aw. napta- 'feucht' (√nab-, namb-); phlv. namb, nam.\\\"\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 57 s.v. nam\", \"stance\": \"supports\",\n    \"note\": \"\\\"nam [nm | N ~] moisture\\\" — MacKenzie explicitly equates the MP and the NP form.\"},\n   {\"src\": \"ARY\", \"where\": \"pdf p. 500 of the ARY scan (entry نم), ARY_latin_index_pages.txt ll.14555-14580\", \"stance\": \"supports\",\n    \"note\": (\"Aryanpur's cognate list for the entry: \\\"NABAH- (AVESTAN) … NAM, NAMB, NAMBITAN (PAHLAVI) … \"\n             \"NEMI, NEM (KURDISH) … NAMB (BALUCHI) … NABHAS (SANSKRIT) … NEBULA (LATIN)\\\", with \"\n             \"\\\"REFERENCES: POKORNY 315; MACKENZIE (MOISTURE) 124; BUCK 10.74-10.75\\\" — an independent modern \"\n             \"cross-check of the whole chain.\")},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 276 s.v. *nab, section NWIR\", \"stance\": \"supports\",\n    \"note\": \"\\\"NP namīdan/nam- (denomin.) 'to grow moist', Kurd. nim 'dampness' (*nambV-)\\\" — the parenthesis *nambV- confirms the nasalised preform.\"}]})\n\n# ---------------- node 4 ----------------\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"naft\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"NP نفت naft 'naphtha, petroleum, kerosene' is MP npt' /naft/ 'moist, damp; naphtha' (MacKenzie p.57; \"\n  \"Manichaean MP npt, Parthian nft), i.e. the Avestan participle napta- 'moist' substantivised as 'the wet stuff' → \"\n  \"'petroleum' — Pokorny 316 prints the equation \\\"napta- 'feucht' (*nab-ta-) npers. neft 'Naphtha'\\\" outright. \"\n  \"The parenthetical نفط of the chart is the Arabic re-spelling: Arabic nafṭ is a Middle-Persian \"\n  \"loan re-fitted to a triliteral root n-f-ṭ (Asbaghi p. 262 \\\"naft: 'Naphtha' aus pers. naft, mp. naft\\\"; \"\n  \"Lokotsch no. 1538 \\\"ar. naft [der Wurzel nafata 'sieden, wallen' angepaßt]\\\"), and it came back into Persian \"\n  \"spelling as an Arabised doublet — a Persian → Arabic → Persian round trip. Nourai's NOTE is fair and \"\n  \"reproduces a real dispute, but it concerns only the onward history: Zimmern (quoted by Lokotsch and by the Semitist \"\n  \"whom Mo'in quotes at length on BQT:2155) makes Greek náphtha come through Aramaic napṭā from Akkadian \"\n  \"napṭu 'petroleum' (root nabāṭu 'to shine'), whereas Persian/Iranian napta- is inherited and \"\n  \"morphologically transparent, so the chart's own arrow (root → Av. nab-/napta- → NP naft) is unaffected; \"\n  \"Etymonline leaves the donor of the Greek word open, and Cheung flags Akkad. naptu as a likely borrowing.\"),\n \"derivation_fa\": (\n  \"«نفت» فارسی نو از فارسی میانهٔ naft (نوشتهٔ npt') «تر، نمناک؛ نفت» است و آن خود همان اسم مفعول اوستایی napta- \"\n  \"«تر» است که معنای «مادهٔ تر، روغن زمین» گرفته؛ پوکورنی در ص ۳۱۶ همین برابری را می‌آورد. صورت «نفط» در پرانتز، \"\n  \"معرّبِ همین واژه است: عربی نفط وام‌واژه‌ای از فارسی میانه است که به ریشهٔ سه‌حرفی ن‌ف‌ط دراُفتاده (اصباغی ص ۲۶۲، \"\n  \"لوکوچ شمارهٔ ۱۵۳۸) و سپس به همان صورتِ معرّب به فارسی بازگشته است — یعنی وام‌گیری دوسویه. یادداشت نورایی درست و \"\n  \"بجاست، ولی تنها به سرنوشت بعدی واژه مربوط می‌شود: بنا بر تسیمرن (نقل در حاشیهٔ برهان قاطع ۲۱۵۵ و لوکوچ) یونانی \"\n  \"náphtha از آرامی napṭā و اکدی napṭu «نفت» (از ریشهٔ nabāṭu «درخشیدن») است، امّا واژهٔ ایرانی موروثی و ساختش روشن \"\n  \"است؛ پس فلش نمودار برجای می‌ماند.\"),\n \"sources\": [W_NAFT, E_NAPH],\n \"ref_check\": [\n   {\"ref\": \"SNS:282\", \"status\": \"partial\",\n    \"note\": (\"SNS p. 282 (image ocr/SNS/282.png) has no headword naft; what it does give, in the namb entry, is \"\n             \"«ستا: napta- از √nab» with the reference (GNPE. 232) — it supports the Avestan link but \"\n             \"not the Persian word itself.\")},\n   {\"ref\": \"HRN:232\", \"status\": \"supports\",\n    \"note\": (\"Horn no. 1035, printed p. 232: \\\"neft 'Naphta'. aw. napta- 'feucht'; ai. √nabh-, nábhate \"\n             \"'spalten, platzen; hervorquellen'. LW. ar. naft; kurd. nefte…\\\" — Horn also marks the Arabic as \"\n             \"the loan (LW.), as the chart's parenthesis implies.\")},\n   {\"ref\": \"BQT:2155\", \"status\": \"supports\",\n    \"note\": (\"Borhan-e Qate' p. 2155 (vol. 4, ref_page.py BQT:2155): Mo'in's footnote 9 «در اوستا napta- (تره \"\n             \"نمناک)، هندی باستان nábhate… «اسشق ۱۰۳۵»؛ هوبشمان گوید: اسم مفعول از ریشهٔ nab-…», followed by \"\n             \"the long quotation from a dictionary of Arabic-Semitic etymology: «لفظ: اصل آن اکدی است بصورت فعلی \"\n             \"«نباطو» … بمعنی: درخشید، روشن کرد… و ازآنست کلمهٔ «نبطو» بمعنی نفط» — this is exactly the \"\n             \"\\\"Akkadian root Nabatu: to shine\\\" alternative that Nourai's NOTE points to. The page also carries the \"\n             \"Ferdowsi verse quoted in the JSON («باسپ و بنفت آتش اندر زدند / همه هندیان دست بر سر زدند», \"\n             \"شاهنامه ج۷ ص۱۸۶۲).\")},\n   {\"ref\": \"POK:316\", \"status\": \"supports\",\n    \"note\": \"„napta- ‚feucht‘ (*nab-ta-) npers. neft ‚Naphtha‘“ (POK_01.txt l.4659).\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 57 s.v. 1naft\", \"stance\": \"supports\",\n    \"note\": \"\\\"1naft [npt' | = M, N ~] moist, damp; naphtha\\\" — MacKenzie's gloss shows the very semantic shift 'moist' → 'naphtha' inside Middle Persian.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 276 s.v. *nab\", \"stance\": \"supports\",\n    \"note\": \"\\\"MMP npt 'moist, damp, naphtha', BMP npt /naft/ … Ò Also Akkad. naptu 'naphtha'!\\\" and \\\"PARTHIAN: nf 'moist, damp; naphtha'\\\" — Cheung's '!' marks the Akkadian form as the odd man out.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 262 s.v. naft\", \"stance\": \"supports\",\n    \"note\": \"„naft: ‚Naphtha‘ aus pers. naft, mp. naft, aw. napta-, syr. …, mand. napt“, with Lokotsch's chain „pers. nāft … ar. naft, aram. … hieraus griech. náphtha, lat. naphtha … russ. neft'“.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1538 (LKT.txt l.3547)\", \"stance\": \"partial\",\n    \"note\": \"„np. neft ‚Erdpech, Naphtha‘ (Horn NpEt S. 232, Nr. 1035), ar. naft [der Wurzel nafata … angepaßt; nach ZAkkFW 60 jedoch über aram. napṭā aus ass. napṭu ‚Erdöl‘]\\\" — both views side by side, i.e. the dispute in Nourai's NOTE is real and unsettled.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 131\", \"stance\": \"supports\",\n    \"note\": \"„napta- ‚feucht‘ npers. neft ‚Naphta‘“, with the caveat that some had wrongly attached these words to snā-, sn-ip- 'fließen'.\"}]})\n\n# ---------------- node 5 ----------------\nnodes.append({\n \"id\": 5, \"lang\": \"Avestan\", \"words\": \"nemadhka\", \"verdict\": \"disputed\",\n \"derivation\": (\n  \"The Avestan form is real but both its meaning and its root affiliation are contested, and the arrow drawn here \"\n  \"(root *nebh-/*nembh- 'moist' → nəmaδka- 'salt') is not supported by any modern authority. \"\n  \"nəmaδkā- is a hapax at Yt. 14.55, and Bartholomae (AiW col. ~1068) glosses it 'Reisig (brushwood) \"\n  \"as fuel', deriving it from nəmata- 'brushwood, wickerwork' ← nam- 'to bend' (hence also NP نمد \"\n  \"namad 'felt'). Henning (BSOS IX/1, p. 85 n. 20 — the very reference Mo'in cites in BQT:2170) argued instead \"\n  \"that \\\"Av. nəmaδka Yt. xiv, 55 is also 'salt'\\\" and reconstructed OIr. *na/imadka-, and Gharib follows him \"\n  \"(SOD 5973 \\\"namaδk ◊< Av. namaδka\\\"). So 'salt' is a defensible reading. What has no support is the \"\n  \"attachment to this root box: Pokorny 315-316 does not list the word at all, Edel'man (ESIJa V 464) reconstructs \"\n  \"PIr. *namadka- without linking it to *nebh-, and Mo'in's own footnote states that neither the Avesta nor the Veda \"\n  \"has a noun for 'salt' and only reports Pourdavoud's remark that \\\"among the Indians the name of this substance is \"\n  \"derived from nəm and moisture\\\" — which is what Nourai turned into a derivation. Everything below this node \"\n  \"(namak, Sogdian namaδk) is internally sound; it is simply filed under the wrong root.\"),\n \"derivation_fa\": (\n  \"صورت اوستایی هست، امّا هم معنی و هم ریشه‌اش مورد اختلاف است و پیوندی که نمودار می‌کشد (ریشهٔ *nebʰ- «نم» ← \"\n  \"nəmaδka- «نمک») در هیچ منبع امروزی پشتوانه ندارد. nəmaδkā- تنها یک‌بار در یشت ۱۴/۵۵ آمده و \"\n  \"بارتولومه آن را «هیزم خرد، خاشاک سوختنی» معنی کرده و به nəmata- «خاشاک، بافتهٔ ترکه» از ریشهٔ nam- «خمیدن» \"\n  \"بازبرده است (که «نمد» فارسی هم از آن است). هنینگ در BSOS IX/۱ ص ۸۵ — همان مأخذی که معین در حاشیهٔ برهان ۲۱۷۰ \"\n  \"می‌آورد — استدلال کرده که این واژه «نمک» است و صورت ایرانی باستان را *namadka- بازساخته، و غریب نیز در فرهنگ \"\n  \"سغدی همین را پذیرفته است. پس معنی «نمک» پذیرفتنی است، ولی وابسته‌کردن آن به ریشهٔ «نم» پذیرفته نیست: پوکورنی این \"\n  \"واژه را در ص ۳۱۵–۳۱۶ نیاورده و ادلمان نیز *namadka- را بی‌هیچ پیوندی با *nebʰ- بازمی‌سازد. خود معین می‌نویسد که \"\n  \"در اوستا و وِدا اسمی برای «نمک» نیست. نتیجه: پژوهش امروزی این فلش را رد می‌کند، هرچند شاخهٔ زیر آن (نمک، سغدی \"\n  \"namaδk) درست است.\"),\n \"sources\": [W_NMK, W_NAMAK],\n \"ref_check\": [\n   {\"ref\": \"BQT:2170\", \"status\": \"supports\",\n    \"note\": (\"Borhan-e Qate' p. 2170 (vol. 4; page image read by vision and transcribed to \"\n             \"ocr/BQT/2170.vision.txt), Mo'in's footnote 5: «نمك ـ بفتح اول و دوم، پهلوی namak «ناوادیاس ۱۶۳»، \"\n             \"از اوستا nəmadhka- هرچند معنی فرق کند. (Henning, A list of Middle Persian …, BSOS, IX, I, p. 85) \"\n             \"ـ در اوستا و ودا از «نمك» (ملح) اسمی نیست و نمك بدین معنی متأخر است» — the spelling \"\n             \"\\\"nəmadhka\\\" of the chart is Mo'in's own, and Mo'in himself flags the semantic difficulty \"\n             \"(\\\"though the meaning differs\\\").\")},\n   {\"ref\": \"MON:4818\", \"status\": \"not_checked\",\n    \"note\": (\"Mo'in's six-volume Farhang-e Farsi is not scanned anywhere (refs_online.json MON notes: only the \"\n             \"2-vol Adena condensation exists, with different pagination and no page mapping), so p. 4818 cannot be \"\n             \"opened; vajehyab's Mo'in text for نمک carries no origin tag at all. The same author's \"\n             \"footnote on BQT:2170, checked above, states the identical claim.\")}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. ~1068 s.v. *nəmaδkā- (BRT.txt l.18948ff)\", \"stance\": \"contradicts\",\n    \"note\": (\"\\\"j. *nəmaδkā- f. 'Reisig' als Feuerungsmaterial: yat … mašyaka daxvayasō avi \"\n             \"ātrəm abarənti … aēsməm yō vaoce 'ka năma Yt. 14. 55. Zu nəmata- \"\n             \"wie ai. ašṭalkā- … zu …\\\" — Bartholomae's gloss is 'brushwood used as fuel', \"\n             \"not 'salt', and he ties it to nəmata- 'Reisig' (← nam- 'to bend'), i.e. a different root.\")},\n   {\"src\": \"HENNING\", \"where\": \"Selected Papers, 'A List of Middle-Persian and Parthian Words' area, n. 20 (HENNING_selected_papers.txt l.341)\", \"stance\": \"partial\",\n    \"note\": (\"\\\"The Sogdian word for 'salt' was hitherto unknown … Gauthiot … who posits OIr. namaδaka- \"\n             \"… we are at liberty to assume OIr. na/imadka- (or na/imaδka-) … There is every likelihood \"\n             \"that Av. nəmaδka Yt. xiv, 55 is also 'salt'\\\" — supports the reading 'salt' but explicitly \"\n             \"as a conjecture, and says nothing about the root *nebh-.\")},\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 5973, printed p. 239\", \"stance\": \"supports\",\n    \"note\": \"\\\"5973 nm'δk(δ) B, M / namaδk ◊< Av. namaδka; Khwar jδk / salt\\\" — Gharib cites the Avestan form with the meaning 'salt'.\"},\n   {\"src\": \"POK\", \"where\": \"pp. 315-316, lemma 2. (enebh-)\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's entry lists nebhos-, nebhelā, napta-/neft, m̥bh-(ro-), emb(h)-/omb(h)- and nembh- — there is no salt word anywhere in it.\"}]})\n\n# ---------------- node 6 ----------------\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"namak\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"NP نمک namak 'salt' is MP namak (nmk'), and the Manichaean MP spelling nmyhk recorded by MacKenzie \"\n  \"is the decisive evidence for the older shape: the -yh- writes a lost intervocalic spirant, so MP namak goes back to \"\n  \"OIr. *namadka- (Henning; PIr. *namadka- in Edel'man, ESIJa V 464), the -δ- being lost before -k- in South-West \"\n  \"Iranian while Sogdian namaδk, Khwarezmian nmδk, Bactrian ναμιλγο and \"\n  \"Khotanese namca keep it. The derivatives in the node are transparent Persian formations: نمکدان \"\n  \"namak-dān 'salt-cellar' (namak + the container suffix -dān, so glossed by Mo'in), نمکین \"\n  \"namakīn and بانمک bā-namak, whose sense 'charming, piquant' (the chart's second gloss \"\n  \"'charm') is a classical Persian metaphor, matched by the Borhan's own «کان نمک: معشوق ملیح». The word itself \"\n  \"and its descent from *namadka- are confirmed; only its placement under the 'moisture' root (see node #5) is not.\"),\n \"derivation_fa\": (\n  \"«نمک» از فارسی میانهٔ namak است و املای مانوی nmyhk (به نقل مکنزی) کلید کار است: -yh- نشانهٔ سایشی از میان‌رفته \"\n  \"است، پس namak از ایرانی باستان *namadka- می‌آید (هنینگ؛ ادلمان، فرهنگ ریشه‌شناختی زبان‌های ایرانی ج۵ ص۴۶۴) که \"\n  \"در جنوب‌غربی -δ- پیش از -k- افتاده، امّا در سغدی namaδk، خوارزمی nmδk، بلخی namilgo و ختنی namca \"\n  \"برجای مانده است. ترکیب‌های نمودار نیز ساخت‌های روشن فارسی‌اند: «نمکدان» از نمک + پسوند ظرفِ -دان (به گفتهٔ معین)، \"\n  \"و «نمکین/بانمک» که معنای «دلنشین، ملیح» گرفته‌اند و همین معنی دوم نمودار است. خودِ واژه و پیوندش با *namadka- \"\n  \"درست است؛ تنها جای‌دادن آن زیر ریشهٔ «نم» (بنگرید به گرهٔ ۵) پذیرفتنی نیست.\"),\n \"sources\": [W_NAMAK, W_NMK, V_NAMAK],\n \"ref_check\": [\n   {\"ref\": \"BQT:2170\", \"status\": \"supports\",\n    \"note\": (\"p. 2170 footnote 5 (ocr/BQT/2170.vision.txt): «نمك … پهلوی namak … از اوستا nəmadhka-», \"\n             \"plus footnote 2 «از: نمك + دان (پسوند ظرف)، آلتی که در آن نمك کنند» and footnote 4 \"\n             \"«از: نمك + ینه (نسبت)» — the Pahlavi ancestor and the compounds of the node are exactly there. \"\n             \"The Borhan text itself glosses «کان نمك: معشوق ملیح», i.e. the 'charm' sense.\")},\n   {\"ref\": \"MON:4818\", \"status\": \"not_checked\",\n    \"note\": \"6-vol Mo'in unscanned (see node #5); vajehyab's Mo'in gives the definition «مادهٔ سپیدی است که … در آب حل می‌شود» but no etymological tag, so the cited page cannot be verified.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 57 s.v. namak\", \"stance\": \"supports\",\n    \"note\": \"\\\"namak [nmk' | M nmyhk, N ~] salt\\\" — MacKenzie's Manichaean form nmyhk is what points to *nama(δ)ka-.\"},\n   {\"src\": \"HENNING\", \"where\": \"Selected Papers, n. 20 (HENNING_selected_papers.txt l.341)\", \"stance\": \"supports\",\n    \"note\": \"\\\"In unpublished Man. MPers. texts we have nmyhg … we are at liberty to assume OIr. na/imadka- … For the final -k of NPers. namak one could compare NPers. mayak : Parth. mg'dg\\\" — the sound law behind namak spelled out.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss (grep 'nemek', 'Salz')\", \"stance\": \"silent\",\n    \"note\": \"Horn has no entry for the word; it turns up only in passing under no. 533 (-dān): \\\"~dān 'Behälter', vergl. ābdān, nemekdān etc.\\\"\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt (grep NAMAK / SALT)\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's Indo-European roots dictionary has no entry for نمک — consistent with the word not belonging to an IE root of the 'moist' family.\"}]})\n\n# ---------------- node 7 ----------------\nnodes.append({\n \"id\": 7, \"lang\": \"Sogdian\", \"words\": \"nm`dk\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Sogdian nm'δk /namaδk/ 'salt' (Buddhist and Manichaean Sogdian) is Gharib's entry no. 5973 on the very page \"\n  \"Nourai cites, and Gharib derives it exactly as the chart does: \\\"namaδk ◊< Av. namaδka; Khwar. jδk\\\". \"\n  \"The word was first identified by Henning in a Manichaean text (\\\"The Sogdian word for 'salt' was hitherto unknown\\\"), \"\n  \"and it is the crucial witness for the reconstruction, because Sogdian keeps the intervocalic -δ- that South-West \"\n  \"Iranian lost (Sogd. namaδk : MP namak), which is what fixes the preform as *namadka- rather than Gauthiot's \"\n  \"*namaδaka-. Nourai's transliteration nm`dk renders aleph by ` and δ by d, his normal convention.\"),\n \"derivation_fa\": (\n  \"سغدی nm'δk /namaδk/ «نمک» همان مدخل شمارهٔ ۵۹۷۳ فرهنگ سغدی غریب در همان صفحه‌ای است که نورایی ارجاع \"\n  \"داده، و غریب نیز آن را از «اوستایی namaδka» گرفته و خوارزمی nmδk را در کنارش آورده است. این واژه را نخست \"\n  \"هنینگ در متنی مانوی شناسایی کرد و گواه کلیدی بازسازی است، زیرا سغدی -δ- میان‌واکه‌ای را نگه داشته و فارسی \"\n  \"میانه از دست داده است (سغدی namaδk در برابر namak)؛ همین قیاس صورت *namadka- را قطعی می‌کند. آوانگاری نورایی \"\n  \"(nm`dk) طبق شیوهٔ خودش الف را با ` و δ را با d نشان می‌دهد. ادعای نورایی درست است.\"),\n \"sources\": [W_NMK],\n \"ref_check\": [\n   {\"ref\": \"SOD:239\", \"status\": \"supports\",\n    \"note\": (\"Gharib, Sogdian Dictionary, printed p. 239 (the page number 239 stands in SOD_pages.txt l.20807, \"\n             \"immediately above the entries): \\\"5973 nm'δk(δ) B, M | namaδk ◊< Av. namaδka; Khwar \"\n             \"jδk | salt | GMS 1053; TSP 19.8; Bailey. BSOAS 1975, 54\\\"; the English index of the same book has \"\n             \"\\\"salt 5973\\\". Page and entry both match Nourai's citation.\")}],\n \"consulted\": [\n   {\"src\": \"HENNING\", \"where\": \"Selected Papers, n. 20\", \"stance\": \"supports\",\n    \"note\": \"\\\"(20) 'The salty one.' … The Sogdian word for 'salt' was hitherto unknown. Cf. the Eastern dialect forms as collected by Gauthiot … cf. Saka namca, nimva, etc., Bailey, BSOS., viii, p. 190.\\\"\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 276 s.v. *nab, section SOGDIAN\", \"stance\": \"silent\",\n    \"note\": \"Cheung's Sogdian material under *nab is only nβt'k/nβtk 'moist' (from *napta-); namaδk does not appear there — i.e. the verb dictionary does not connect the salt word with this root either.\"},\n   {\"src\": \"SOD\", \"where\": \"English index, 'salty 5972 / salt 5973 / rock salt 9135'\", \"stance\": \"supports\",\n    \"note\": \"The neighbouring entry 5972 nm'δynch = namaδkenc 'salty' shows the stem is productive in Sogdian.\"}]})\n\n# ---------------- node 8 ----------------\nnodes.append({\n \"id\": 8, \"lang\": \"Avestan\", \"words\": \"awrem, awra, awar\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Younger Avestan aβra- n. (transliterated awra- by Bartholomae) 'rain-cloud, cloud', also 'rain, rain-shower' \"\n  \"(Y. 68.32 'as a cloud driven by the wind', Yt. 14.41 awra upapā, Yt. 8.40) is the zero-grade *n̥bh-ró- \"\n  \"of the same root: syllabic *n̥ gives Indo-Iranian a-, whence Skt. abhrá- 'cloud' (RV+), while the parallel \"\n  \"*m̥bh-ro-/*ombh-ro- gives Greek ómbros 'rain', Latin imber and Armenian amb/amp. Nourai's three forms are \"\n  \"each a real citation form from one of his sources: awrəm is the accusative singular as printed by Klein \"\n  \"(KLN:772, s.v. imbricate) and by Mann (\\\"Av. awrom, n. 'cloud'\\\"), awra- is Bartholomae's stem (AiW col. 99), and \"\n  \"awar is the Pazand form (Nyberg \\\"Paz. awar\\\") which the Šāyest nē Šāyast glossary quotes \"\n  \"beside awra-. On the NOTE: Mo'in's footnote on BQT:79 does report the old analysis of Skt. abhrá- as ap- + \"\n  \"bhr- 'water-carrier' (Monier-Williams's guess), but that is folk etymology — it cannot explain Gk. ómbros, \"\n  \"Lat. imber or Arm. amb, and Pokorny, Walde-Pokorny, Mayrhofer (via Wiktionary), Cheung and Aryanpur all give \"\n  \"*n̥bhrós. Modern scholarship therefore sides with Nourai's tree, not with the note.\"),\n \"derivation_fa\": (\n  \"اوستایی نو aβra- (که بارتولومه awra- آوانگاری می‌کند) «ابرِ باران، ابر» و نیز «باران» درجهٔ صفرِ همین ریشه \"\n  \"است: *n̥bh-ró-. خیشومی هجایی *n̥ در هندوایرانی a- شده، از این‌رو سنسکریت abhrá- و اوستایی \"\n  \"aβra-؛ و گونهٔ همتای *m̥bhro-/*ombhro- در یونانی ómbros «باران»، لاتینی imber و ارمنی amb/amp دیده \"\n  \"می‌شود. سه صورتی که نورایی آورده هر یک از یکی از مآخذ خودش است: awrəm صورت مفعولی است که کلاین (ص۷۷۲) و مان \"\n  \"آورده‌اند، awra- ستاک بارتولومه (ستون ۹۹) و awar صورت پازند است (نیبرگ) که واژه‌نامهٔ شایست نه شایست هم آورده. \"\n  \"دربارهٔ یادداشت: حاشیهٔ معین در برهان ۷۹ تحلیل کهنِ ap- + bhr- «حامل آب» را نقل می‌کند، ولی این ریشه‌شناسی عامیانه \"\n  \"است و ómbros یونانی و imber لاتینی و amb ارمنی را توضیح نمی‌دهد؛ پوکورنی، والده‌پوکورنی، مایرهوفر، چونگ و \"\n  \"آریان‌پور همه *n̥bhrós می‌دهند. پس پژوهش امروزی جانب نمودار نورایی را می‌گیرد.\"),\n \"sources\": [W_ABHRA, W_ABR, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"KLN:772\", \"status\": \"supports\",\n    \"note\": (\"Klein 1966, printed p. 772 (KLN_1966.txt \\\\f-leaf 415, whose own running numbers are '772 773'), \"\n             \"s.v. imbricate: \\\"fr. imber, gen. imbris, 'rain', which stands for *mbhros and is cogn. with Gk. \"\n             \"ómbros 'rain', OI. abhram 'cloud, atmosphere', Avestic awrəm 'cloud', OI. ambhah 'water', \"\n             \"Arm. amb, amp 'cloud', and also with L. nebula 'mist'\\\" — the page is exactly right and \"\n             \"\\\"awrəm\\\" is the source of Nourai's first form.\")},\n   {\"ref\": \"POK:316\", \"status\": \"supports\",\n    \"note\": \"„m̥bh-(ro-): ai. abhrá- m. ‚trübes Wetter, Gewölk‘, n. ‚Wolke, Luftraum‘ (*n̥bhros), av. awra- n. ‚Wolke‘“; Pokorny adds that Gk. aphrós 'foam' stays out on semantic grounds.\"},\n   {\"ref\": \"SNS:11\", \"status\": \"supports\",\n    \"note\": (\"Šāyest nē Šāyast glossary p. 11 line 7 (image ocr/SNS/11.png, transcription \"\n             \"ocr/SNS/11.vision.txt): «avr/abr: ابر. ستا awar-/awra-، سا abhrá-، پا awar (مینو خرد)» \"\n             \"— the Avestan awar-/awra- and Sanskrit abhrá- of the chart, on the cited page (the book's index \"\n             \"confirms \\\"abr/avr 11/7\\\").\")}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 99 s.v. awra- (BRT.txt l.4000)\", \"stance\": \"supports\",\n    \"note\": \"\\\"j. awra- n. 1) 'Regenwolke, Wolke' … 2) 'Regen, Regenschauer' … ai. abhrá- n. 'Wolke'; np. abr 'Wolke', afy. erif 'Wolke', bal. haur 'Regen'.\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, col./p. under m̥bhros (IEC.txt l.11502)\", \"stance\": \"supports\",\n    \"note\": \"\\\"m̥bhros, is 'cloud, vapour, drizzle'. WP I, 131. Skt. abhráh, m. 'rain-cloud'; Av. awrom, n. 'cloud'; Per. abr, id. beside abar 'fog'; Oss. arv 'sky'; … Lat. (prob.) imber\\\" — Mann's 'awrom' and 'abar' are Nourai's awrem and awar.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 131 (l.11867)\", \"stance\": \"supports\",\n    \"note\": \"„m̥bh-: ai. abhra- m. ‚trübes Wetter, Gewölk‘ … av. awra- n. ‚Wolke‘“.\"},\n   {\"src\": \"ARY\", \"where\": \"pdf p. 76 of the ARY scan (entry ابر)\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur's cognate list: \\\"AWRA, AWREM (AVESTAN) | ABR (PAHLAVI) | HAUR, EWR (KURDISH) | ABHRA (SANSKRIT) | AMB, AMP (ARMENIAN) | APHROS, OMBROS (GREEK) | IMBER, IMBRIS (LATIN)\\\" with references to Pokorny and MacKenzie (CLOUD) 167 — the same two Avestan forms awra/awrem.\"}]})\n\n# ---------------- node 9 ----------------\nnodes.append({\n \"id\": 9, \"lang\": \"Pahlavi\", \"words\": \"awr, avr, abr; abr-âmŭn\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Book Pahlavi ʾbl / ʾpl, read abr (Nyberg transliterates avr, whence the chart's doublet awr/avr/abr), 'cloud' is \"\n  \"Av. aβra- with the regular Middle Persian development of the intervocalic spirant to b and of the historical \"\n  \"spelling with p; MacKenzie prints \\\"abr ['bl, 'pl | N ~] cloud\\\" and Nyberg gives the whole chain \\\"avr [ʾpl] \"\n  \"cloud(s) — Av. (99) awra-; Paz. awar; NP abr\\\", the number 99 being Bartholomae's column. The second word, \"\n  \"abr-āmōn 'cloudy, full of cloud', is a Pahlavi compound of abr with a second element āmōn to which \"\n  \"the Šāyest nē Šāyast glossary cross-refers under its own entry āmōn; it is attested \"\n  \"in ŠnŠ 10.2, and it is not in MacKenzie or Nyberg, so the ŠnŠ glossary (Nourai's SNS:11) is its only \"\n  \"source here.\"),\n \"derivation_fa\": (\n  \"پهلوی کتابی ʾbl/ʾpl که abr خوانده می‌شود (نیبرگ avr آوانگاری می‌کند و از همین‌رو نورایی سه گونهٔ awr/avr/abr \"\n  \"را آورده) بازماندهٔ اوستایی aβra- است: سایشی میان‌واکه‌ای در فارسی میانه به b بدل شده و املای با p تاریخی \"\n  \"است. مکنزی «abr [ʾbl, ʾpl] ابر» و نیبرگ همهٔ زنجیره را می‌آورد: «avr [ʾpl] ابر — اوستایی (۹۹) awra-؛ پازند \"\n  \"awar؛ فارسی نو abr» (۹۹ شمارهٔ ستون بارتولومه است). واژهٔ دوم، abr-āmōn «ابرآلود، پرابر»، ترکیبی پهلوی \"\n  \"است از abr با جزء دوم āmōn (واژه‌نامهٔ شایست نه شایست به مدخل āmōn ارجاع می‌دهد) و در شایست \"\n  \"نه شایست ۱۰/۲ گواهی دارد؛ در مکنزی و نیبرگ نیست.\"),\n \"sources\": [W_ABR],\n \"ref_check\": [\n   {\"ref\": \"SNS:11\", \"status\": \"supports\",\n    \"note\": (\"p. 11 lines 7 and 10 (image ocr/SNS/11.png; transcription ocr/SNS/11.vision.txt): line 7 \"\n             \"«avr/abr: ابر … ستا awar-/awra-، سا abhrá-، پا awar» and line 10 «abrāmōn: \"\n             \"ابرآمون، پرابر، ابری. (نک: āmōn) ک ۱۰/۲» — both words of the node, on the cited page; \"\n             \"the glossary's index lists \\\"abr/avr 11/7\\\" and \\\"abramōn 11/10\\\".\")}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 5 s.v. abr (PHD_pages.txt l.813)\", \"stance\": \"supports\",\n    \"note\": \"\\\"abr ['bl, 'pl | N ~] cloud\\\" — MacKenzie confirms the MP form and its identity with the NP word, but has no abr-āmōn.\"},\n   {\"src\": \"NYB\", \"where\": \"vol. II glossary p. ~13 s.v. avr (NYB_vol2_glossary.txt l.813)\", \"stance\": \"supports\",\n    \"note\": \"\\\"avr [ʾpl] cloud(s) 411, 717, 852, 861, 891 — Av. (99) awra-; Paz. awar; NP abr\\\" — Nyberg gives precisely the Avestan → Pahlavi → New Persian chain of the chart, and his 'Paz. awar' explains Nourai's third Avestan form.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 63, printed p. 9 (HRN.txt leaf 30)\", \"stance\": \"supports\",\n    \"note\": \"\\\"63. ebr 'Wolke'. … aw. awra- 'Wolke'; phlv. awr (geschrieben apr), abr; ai. abhrá-; arm. amp, amb; kurd. avr, awr, häür; bal. haur 'Regen'.\\\"\"}]})\n\n# ---------------- node 10 ----------------\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"abr; abrâmŭn\", \"verdict\": \"plausible\",\n \"derivation\": (\n  \"ابر abr 'cloud' is confirmed beyond doubt: MP abr passes unchanged into New Persian (Horn no. 63 \"\n  \"'ebr'; Bartholomae AiW col. 99 already lists \\\"np. abr 'Wolke'\\\"; Wiktionary: MP ʾp̄l /abr/ < PIr. *abráh < \"\n  \"PIE *n̥bhrós), and it is current from the earliest New Persian poetry onwards. The second word is the \"\n  \"weak point: «ابرآمون» abrāmŭn has no entry in Dehkhoda, Mo'in \"\n  \"or Amid (searched via vajehyab, which returns only the unrelated ابریمون and \"\n  \"ارامونی), i.e. it is not attested as a New Persian word. What Nourai has done is \"\n  \"to copy into his 'Persian' row the Persian GLOSS with which Tavoosi's glossary renders the Pahlavi headword \"\n  \"abrāmōn («ابرآمون، پرابر، ابری») — a transliteration, not a Persian lexeme. Hence \"\n  \"'plausible': the node is right for abr and unsupported for abrāmŭn.\"),\n \"derivation_fa\": (\n  \"«ابر» بی‌گمان درست است: صورت فارسی میانهٔ abr بی‌تغییر به فارسی نو رسیده (هرن شمارهٔ ۶۳؛ بارتولومه در ستون ۹۹ \"\n  \"خودِ «np. abr» را آورده) و از کهن‌ترین شعر فارسی به‌کار رفته است. امّا واژهٔ دوم لغزشگاه است: «ابرآمون» در دهخدا \"\n  \"و معین و عمید مدخل ندارد (جست‌وجو در واژه‌یاب تنها «ابریمون» و «ارامونی» بی‌ربط را می‌آورد)، یعنی به‌عنوان واژهٔ \"\n  \"فارسی نو گواهی ندارد. آنچه نورایی کرده این است که برگردانِ فارسیِ مدخل پهلویِ abrāmōn در واژه‌نامهٔ \"\n  \"طاووسی («ابرآمون، پرابر، ابری») را در ردیف فارسی نشانده است؛ این آوانویسی است نه واژهٔ فارسی. پس: با احتیاط \"\n  \"پذیرفتنی است — برای «ابر» درست، برای «ابرآمون» بی‌پشتوانه.\"),\n \"sources\": [W_ABR, W_ABHRA],\n \"ref_check\": [\n   {\"ref\": \"POK:316\", \"status\": \"partial\",\n    \"note\": \"Pokorny p.316 s.v. m̥bh-(ro-) gives only \\\"ai. abhrá-\\\" and \\\"av. awra- n. 'Wolke'\\\"; no New Persian form is cited in that lemma (unlike his nembh- paragraph, where npers. nem does appear). The root and the Avestan link are supported; the Persian word is not on the page.\"},\n   {\"ref\": \"SNS:11\", \"status\": \"supports\",\n    \"note\": \"p. 11 lines 7/10 gloss the two Pahlavi headwords with the Persian words «ابر» and «ابرآمون، پرابر، ابری» — so the Persian spellings of the node come from here, but as glosses of Pahlavi entries.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 99 s.v. awra-\", \"stance\": \"supports\",\n    \"note\": \"\\\"np. abr 'Wolke'\\\" listed directly under the Avestan entry — Bartholomae himself draws the Avestan → New Persian line.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 63, p. 9\", \"stance\": \"supports\",\n    \"note\": \"\\\"ebr 'Wolke' … phlv. awr (geschrieben apr), abr\\\" — the New Persian headword with the Pahlavi ancestor.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab search for ابرآمون (Dehkhoda / Mo'in / Amid / Academy)\", \"stance\": \"contradicts\",\n    \"note\": \"No dictionary returns an entry for ابرآمون — only ارامونی ('anemone', Dehkhoda) and ابریمون ('Irsa', Dehkhoda); so the word is not a New Persian lexeme.\"},\n   {\"src\": \"ARY\", \"where\": \"pdf p. 76 (entry ابر)\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur lists the Persian headword ابر with Avestan AWRA/AWREM, Pahlavi ABR and Sanskrit ABHRA — modern Persian cross-check for abr (nothing for abrāmŭn).\"}]})\n\n# ---------------- node 11 ----------------\nnodes.append({\n \"id\": 11, \"lang\": \"Latin\", \"words\": \"Neptunus\", \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Latin Neptūnus, originally god of springs and rivers and only then of the sea, is one of two competing \"\n  \"etymologies, and the chart picks the one that is not the majority view. Pokorny gives it with an explicit hedge: \"\n  \"„vielleicht hierher lat. Neptūnus ‚Gott der Quellen und Flüsse, dann des Meeres‘ aus \"\n  \"*nebh-tu-s“, and Klein likewise \\\"prob. fr. I.-E. base *(e)nebh- 'moist', whence also Avestic napta-\\\"; \"\n  \"Etymonline follows them ('probably'). The formation would be a -no- derivative of a *neptu- 'wet substance' \"\n  \"(Ernout-Meillet: \\\"Neptūnus serait formé comme tribūnus et dominus s'il avait existé un *neptu- \"\n  \"'substance humide'\\\"), but those authors call the link with Av. napta- \\\"vague\\\" and prefer connecting the name with \"\n  \"the Indo-Iranian divine figure Ved. apām nápāt / Av. apăm napāt 'descendant of the waters', \"\n  \"i.e. with *nepōt- 'grandson, nephew' rather than *nebh-; the Etruscan Neθuns further clouds the picture. \"\n  \"So the arrow is defensible but contested.\"),\n \"derivation_fa\": (\n  \"لاتینی Neptūnus، که نخست خدای چشمه‌ها و رودها بود و سپس خدای دریا، دو ریشه‌شناسی رقیب دارد و نمودار همان را \"\n  \"برگزیده که رأی اکثریت نیست. پوکورنی با احتیاط می‌نویسد «شاید از *nebh-tu-s» و کلاین نیز «احتمالاً از ریشهٔ \"\n  \"*(e)nebh- «نمناک»، همان که napta- اوستایی از آن است»؛ اتیمونلاین هم همین را با قید «احتمالاً» آورده. ساخت واژه \"\n  \"باید صفتِ -no- بر روی *neptu- «مادهٔ تر» باشد، امّا ارنو و مِیه پیوند با napta- را «مبهم» می‌خوانند و ترجیح \"\n  \"می‌دهند نام را با آن چهرهٔ دینی هندوایرانی، apăm napāt «نوادهٔ آب‌ها»، یعنی با *nepōt- «نواده» \"\n  \"بسنجند، نه با *nebʰ-؛ صورت اتروسکی Neθuns هم کار را پیچیده‌تر می‌کند. پس این فلش با احتیاط پذیرفتنی است.\"),\n \"sources\": [E_NEPT, A_NEPT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"not_found\",\n    \"note\": (\"Watkins's Indo-European roots list — the direct descendant of the 1975 AHD New College appendix that \"\n             \"Nourai cites — has \\\"nebh-. Cloud. … 4. Nasalized form *ne-m-bh- in Latin nimbus: NIMBUS. See \"\n             \"ombhro-. [Pok. (enebh-) 315.]\\\" and \\\"ombh-ro-. Rain. … Latin imber: IMBRICATE\\\", but NEPTUNE occurs \"\n             \"nowhere in the book (grep 'Neptun' in AHD_watkins1985.txt: no hit; it is absent from the English index \"\n             \"too). The online AHD entry for Neptune gives only \\\"[Latin Neptūnus]\\\" with no root cross-reference. \"\n             \"So Nourai's AHD reference does not support this node.\")}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 316 (POK_01.txt l.4659)\", \"stance\": \"partial\",\n    \"note\": \"„vielleicht hierher lat. Neptūnus ‚Gott der Quellen und Flüsse, dann des Meeres‘ aus *nebh-tu-s“ — Pokorny's own 'vielleicht' makes this a suggestion, not a result.\"},\n   {\"src\": \"KLN\", \"where\": \"p. ~1041 s.v. Neptune (KLN_1966.txt leaf 557)\", \"stance\": \"partial\",\n    \"note\": \"\\\"L. Nepliūnus, 'the sea god; the sea', prob. fr. I.-E. base *(e)nebh-, 'moist', whence also Avestic napta-, 'moist, humid', L. nebula … See nebula.\\\"\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. Neptunus (LAT.txt l.41165ff)\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"Le rapport avec av. napta- 'humide' est vague. … on ne peut s'empêcher de penser à l'importante figure religieuse indo-iranienne de ved. apām napat, av. apam napat 'descendant des eaux' … Emprunt étrusque Neθuns\\\" — the standard Latin etymological dictionary prefers a different origin.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde 1910 (grep 'Neptunus')\", \"stance\": \"silent\",\n    \"note\": \"The 1910 Walde on disk yields no hit for Neptunus in the OCR, so it could not be used either way.\"}]})\n\n# ---------------- node 12 ----------------\nnodes.append({\n \"id\": 12, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"A pass-through node with no word printed in the book: it stands for French Neptune, the learned continuation of \"\n  \"Latin Neptūnus — first the Roman god, and from 1846 the planet, which the French astronomer Urbain \"\n  \"Le Verrier named after having predicted its position (Etymonline s.v. Neptune). French is the right intermediary \"\n  \"for the Persian form in node #13, since Persian took its modern astronomical vocabulary through French.\"),\n \"derivation_fa\": (\n  \"این گره واژه‌ای ندارد و تنها حلقهٔ میانی است: فرانسوی Neptune ادامهٔ عالمانهٔ Neptūnus لاتینی است — نخست نام \"\n  \"خدای رومی و از ۱۸۴۶ نام سیّاره، که اوربن لووریه فرانسوی پس از پیش‌بینی جای آن بر آن نهاد. فرانسه به‌درستی حلقهٔ \"\n  \"میانی برای صورت فارسی (گرهٔ ۱۳) است، زیرا واژگان نجومی نوِ فارسی از راه فرانسه آمده است.\"),\n \"sources\": [E_NEPT, V_NEPT],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The book gives no reference for this node (refs=None) and no word, so there is nothing of Nourai's to check.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. ~1041 s.v. Neptune\", \"stance\": \"supports\",\n    \"note\": \"Klein gives the Latin name and its two senses (god / planet), the base for the French learned form.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab, entry نپتون (Dehkhoda)\", \"stance\": \"supports\",\n    \"note\": \"Dehkhoda's entry itself names the French route: the planet \\\"در ۱۸۴۶ توسط لووریه کشف شد\\\", i.e. the word reached Persian with Le Verrier's French discovery.\"}]})\n\n# ---------------- node 13 ----------------\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"Neptune\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Persian نپتون neptūn is a modern loan from French Neptune (French /nɛptyn/ rendered \"\n  \"نپتون, with the French front rounded ü written و), taken over with the \"\n  \"nineteenth- and twentieth-century French-mediated scientific vocabulary of the Dār al-Fonūn era. Both \"\n  \"Mo'in and Dehkhoda have it, and Mo'in tags it (فر.) 'French': Mo'in «هشتمین سیاره از منظومهٔ \"\n  \"شمسی است», Dehkhoda «نام سیاره‌ای است از منظومهٔ شمسی … در ۱۸۴۶ توسط لووریه کشف شد» and, for the \"\n  \"mythological sense, «در اساطیر روم، نام الههٔ دریاهاست». The chart's arrow French → Persian is therefore \"\n  \"right; the word is not an inherited Iranian form but a European borrowing that happens to rejoin the same root at \"\n  \"the top of the tree.\"),\n \"derivation_fa\": (\n  \"«نپتون» وام‌واژه‌ای نو از فرانسوی Neptune است (واکهٔ گِردِ پیشین فرانسوی با «و» نوشته شده) و همراه واژگان علمی \"\n  \"دورهٔ دارالفنون از راه فرانسه به فارسی آمده است. هم معین و هم دهخدا آن را دارند و معین آن را با برچسب (فر.) \"\n  \"می‌آورد: «هشتمین سیاره از منظومهٔ شمسی است»؛ دهخدا نیز «نام سیاره‌ای است از منظومهٔ شمسی … در ۱۸۴۶ توسط \"\n  \"لووریه کشف شد» و در معنی اسطوره‌ای «در اساطیر روم، نام الههٔ دریاهاست». پس فلشِ فرانسوی ← فارسی درست است؛ این \"\n  \"واژه موروثی ایرانی نیست بلکه وام‌واژه‌ای اروپایی است که در بالای درخت به همان ریشه بازمی‌گردد.\"),\n \"sources\": [V_NEPT, E_NEPT],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"partial\",\n    \"note\": (\"Nourai cites MON without a page, and the six-volume Farhang (whose vol. 5-6 carry the proper names) is \"\n             \"not scanned, so the exact locus cannot be opened. The claim itself checks out on vajehyab's Mo'in text: \"\n             \"«نپتون: هشتمین سیاره از منظومهٔ شمسی است», with the French origin tag (فر.) — which is \"\n             \"precisely what the arrow French → Persian asserts.\")}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab entries for نپتون (Mo'in, Dehkhoda, Amid, Academy)\", \"stance\": \"supports\",\n    \"note\": \"All four give the planet (and Dehkhoda also the Roman sea god), and the word is marked as coming from French (فر.).\"},\n   {\"src\": \"KLN\", \"where\": \"p. ~1041 s.v. Neptune / neptunium\", \"stance\": \"supports\",\n    \"note\": \"Klein documents the same modern chain (Latin name → planet named after it), the European vocabulary Persian borrowed from.\"}]})\n\n# ---------------- node 14 ----------------\nnodes.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"Neptune\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"English Neptune is attested from the late fourteenth century, taken from Latin Neptūnus (through Old French \"\n  \"Neptune) as the name of the Roman sea god, identified with Greek Poseidon; the planetary sense dates from its \"\n  \"discovery by Galle on 23-24 September 1846 and Le Verrier's naming, and the derivatives Neptunian (1650s), \"\n  \"Neptunist and neptunium (1941, coined by E. M. McMillan because the element lies beyond uranium as the planet lies \"\n  \"beyond Uranus) follow. The arrow Latin → English is uncontroversial; only the ultimate origin of the Latin \"\n  \"name is in doubt (see node #11).\"),\n \"derivation_fa\": (\n  \"«Neptune» انگلیسی از پایان سدهٔ چهاردهم گواهی دارد و از لاتینی Neptūnus (به میانجی فرانسوی کهن) به‌عنوان نام \"\n  \"خدای دریای رومی — همتای پوسیدون یونانی — گرفته شده است؛ معنی سیّاره از کشف ۱۸۴۶ و نامگذاری لووریه پیدا شد و \"\n  \"مشتق‌های Neptunian (۱۶۵۰s) و neptunium (۱۹۴۱) پس از آن آمدند. فلشِ لاتینی ← انگلیسی بی‌گفت‌وگو درست است؛ تنها \"\n  \"خاستگاه نهایی نام لاتینی در تردید است (بنگرید به گرهٔ ۱۱).\"),\n \"sources\": [E_NEPT],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The book cites no reference for this node (refs=None); the Latin → English step is in any case standard.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. ~1041 s.v. Neptune, Neptunian, neptunium (KLN_1966.txt leaf 557)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Neptune, n., 1) the god of the sea in Roman mythology; identified later with the Greek god Poseidon; 2) name of a planet. — L. Neptūnus\\\", with neptunium \\\"coined by E. M. McMillan … after the planet Neptune\\\".\"},\n   {\"src\": \"FSD\", \"where\": \"Etymonline s.v. Neptune (used in place of the Funk & Wagnalls volume)\", \"stance\": \"supports\",\n    \"note\": \"\\\"late 14c., from Latin Neptunus, the Roman god of the sea\\\"; planet discovered 23-24 Sept. 1846 by Galle, named by Le Verrier.\"}]})\n\n# ---------------- node 15 ----------------\nnodes.append({\n \"id\": 15, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"A second pass-through Latin node, left wordless in the book; it carries the two Latin words that surface in node \"\n  \"#16. Both are on Pokorny's page: nebula 'mist, fog, cloud' is the *-lo-/-lā derivative of the root, „mit \"\n  \"i-Formans (nebhelā): gr. nephelē ‚Wolke, Nebel‘ = lat. nebula“, and nimbus 'rainstorm, \"\n  \"storm-cloud' belongs to the nasalised grade, „nembh-: … lat. nimbus ‚Sturzregen, Platzregen; \"\n  \"Sturmwolke, Regenwolke‘“ — Watkins states the same two derivations (*nebh-elā > nebula; nasalized \"\n  \"*ne-m-bh- > nimbus). Since node #16's words are English, the Latin node is simply the donor stage.\"),\n \"derivation_fa\": (\n  \"این هم گرهٔ میانی لاتینی است و در کتاب واژه‌ای ندارد؛ حاملِ دو واژهٔ لاتینی است که در گرهٔ ۱۶ به انگلیسی می‌رسند. \"\n  \"هر دو در همان صفحهٔ پوکورنی‌اند: nebula «مه، ابر» ساختِ پسوندی *nebhelā است (برابرِ nephelē یونانی) و \"\n  \"nimbus «باران تند، ابر توفانی» از درجهٔ خیشومی *nembʰ-. واتکینز نیز همین دو اشتقاق را می‌آورد. ادعای نمودار درست است.\"),\n \"sources\": [E_NEB, E_NIM],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference and no word in the book (refs=None).\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 315-316, lemma 2. (enebh-)\", \"stance\": \"supports\",\n    \"note\": \"„mit i-Formans (nebhelā): gr. nephelē ‚Wolke, Nebel‘, = lat. nebula ‚Dunst, Nebel, Wolke‘“ and „nembh-: … lat. nimbus ‚Sturzregen, Platzregen; Sturmwolke, Regenwolke‘“.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. nebh- (AHD_watkins1985.txt l.776)\", \"stance\": \"supports\",\n    \"note\": \"\\\"2. Suffixed form *nebh-elā- in: a. Latin nebula, cloud: NEBULA, NEBULOUS … 4. Nasalized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. [Pok. (enebh-) 315.]\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. nebhos and nebholos (IEC.txt ll.11569-11570)\", \"stance\": \"supports\",\n    \"note\": \"\\\"nebholos, ā 'mist, cloud'. WP I, 131. … Lat. nebula, id.\\\"; and s.v. nebhos \\\"Lat. cf. neb-ula, f. id. beside nimbus (if for *nenebhos)\\\".\"}]})\n\n# ---------------- node 16 ----------------\nnodes.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"nebula, nimbus\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Both English words are straight learned borrowings of the Latin nouns of node #15. nebula appears first in Middle \"\n  \"English as nebule 'a cloud, mist' (mid-15c., from Latin nebula), was re-borrowed in the Latin shape in the 1660s \"\n  \"for a cataract of the eye, and acquired the astronomical sense 'luminous cloud-like patch in the heavens' about \"\n  \"1730 (the modern distinction between gas clouds and galaxies is a 1920s Mt. Wilson refinement); Klein derives it \"\n  \"\\\"fr. I.-E. base *(e)nebh- … whence also OI. nábhas-, Avestic nabah- 'air, sky' … Avestic napta- \"\n  \"'moist, humid'\\\". nimbus is 1610s from Latin nimbus 'rainstorm, thundercloud', first of the bright cloud round a \"\n  \"divinity, then 'halo' (1727) and the meteorological cloud type; Klein: \\\"L., 'rainstorm, thundercloud', fr. \"\n  \"*nembhos; cogn. with Pahlavi namb, nam 'dew, fog, mist', ModPers. nem 'moist, moisture', fr. I.-E. base *nembh-\\\" \"\n  \"— so Klein himself joins the English word to the Persian branch of this very chart.\"),\n \"derivation_fa\": (\n  \"هر دو واژهٔ انگلیسی وام‌واژه‌های عالمانهٔ همان دو اسم لاتینی گرهٔ ۱۵ اند. nebula نخست در انگلیسی میانه به صورت \"\n  \"nebule «ابر، مه» (میانهٔ سدهٔ ۱۵) آمد، در دههٔ ۱۶۶۰ به همان شکل لاتینی برای «آب‌مروارید چشم» بازوام گرفته شد و \"\n  \"نزدیک ۱۷۳۰ معنی نجومی «لکهٔ ابرگونهٔ درخشان در آسمان» یافت. nimbus از دههٔ ۱۶۱۰ از لاتینی nimbus «باران تند، ابر \"\n  \"توفانی» است، نخست دربارهٔ هالهٔ ابرگونِ گرد سرِ خدایان، سپس «هاله» (۱۷۲۷) و آنگاه نامِ گونه‌ای ابر. نکتهٔ شنیدنی \"\n  \"آنکه خودِ کلاین nimbus را با «پهلوی namb, nam و فارسی نو nem» هم‌ریشه می‌شمارد، یعنی همان شاخهٔ فارسیِ همین \"\n  \"نمودار. ادعای نورایی درست است.\"),\n \"sources\": [E_NEB, E_NIM],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference is printed for this node (refs=None); the Latin → English chain is uncontroversial and covered by Klein, Skeat and Etymonline below.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"pp. ~1035 s.v. nebula and ~1048 s.v. nimbus (KLN_1966.txt leaves 553, 561)\", \"stance\": \"supports\",\n    \"note\": \"nebula: \\\"L., 'mist, fog, cloud', fr. I.-E. base *(e)nebh-, 'moist, vapor, mist, cloud', whence also OI. nábhas- … Avestic nabah- 'air, sky' … Avestic napta-, 'moist, humid'. Cp. nepheline, nepho-, Neptune, Nibelungs, nimbus, imbricate.\\\" nimbus: \\\"L., 'rainstorm, thundercloud', fr. *nembhos; cogn. with Pahlavi namb, nam, 'dew, fog, mist', ModPers. nem, 'moist, moisture', fr. I.-E. base *nembh-\\\".\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Nebula (SKT.txt l.12206; printed p. 397 per Aryanpur's index)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Nebula, a little cloud … + Gk. nephelē, dimin. of nephos, cloud; Skt. nabhas, sky, æther\\\" — and s.v. Nuptial he notes \\\"Allied to Nebula\\\".\"},\n   {\"src\": \"FSD\", \"where\": \"Etymonline s.v. nebula / nimbus (used for the English dating)\", \"stance\": \"supports\",\n    \"note\": \"nebula: mid-15c. 'nebule, a cloud, mist', re-borrowed 1660s for eye cataracts, astronomical sense c.1730, PIE root *nebh- 'cloud'. nimbus: 1610s, from Latin nimbus 'cloud', 'perhaps related to nebula', halo sense by 1727.\"}]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Nebh, Nembh, Ombhro\",\n \"verdict\": \"confirmed\",\n \"modern_form\": (\"PIE *(e)nebh- / *nebh- 'moist, wet; water → vapour, mist, cloud' (Pokorny 2. (enebh-), pp. 315-316; \"\n                 \"Walde-Pokorny I 131; Watkins nebh- 'cloud'), with the ablaut and nasal variants *m̥bh-ro-/*ombh-ro- \"\n                 \"'rain(-cloud)' (Watkins ombh-ro- 'rain') and *nembh- (Latin nimbus, Pahlavi namb)\"),\n \"note\": (\"The root box is right in substance. Pokorny's lemma on the cited page is „2. (enebh-): nebh-, embh-, \"\n          \"m̥bh- (Kontaminationsform nembh-) … ‚feucht, Wasser‘, daraus ‚Dampf, Dunst, Nebel, \"\n          \"Wolke‘“, and its sub-lemmas are exactly Nourai's three headwords: nebhos-/nebhelā (the 'cloud' \"\n          \"words), nembh- (pehl. namb, nam, npers. nem — 'moisture'), and m̥bh-(ro-)/emb(h)-:omb(h)- (Gk. \"\n          \"ómbros, Lat. imber — 'rain'). Watkins keeps the same division as two headwords, nebh- 'cloud' and \"\n          \"ombh-ro- 'rain', both referred to \\\"[Pok. (enebh-) 315]\\\". Two caveats worth recording: (a) the underlying \"\n          \"sense is 'moist, water', with 'cloud' a derived sense, so glossing Nebh itself as 'cloud' is a shorthand \"\n          \"(defensible, since that is Watkins's own gloss); (b) p. 315 is shared with the homonymous root 1. (enebh-), \"\n          \"embh-, ombh-, nobh- 'navel' (Watkins nobh-, Pok. p. 314-315), which is a different root and must not be \"\n          \"mixed in — Nourai keeps them apart. Downstream, the Iranian and Latin/English branches are sound; the \"\n          \"one branch that does not belong under this root is the 'salt' group (nodes #5-7), and the one arrow whose \"\n          \"cited authority does not back it is Latin Neptunus (node #11, refs=AHD, where Watkins has no Neptune).\"),\n \"note_fa\": (\"جعبهٔ ریشه در اساس درست است. مدخل پوکورنی در همان صفحهٔ ارجاع‌شده چنین است: «۲. (enebh-): nebh-, embh-, \"\n             \"m̥bh- (گونهٔ آمیخته nembh-) … «نمناک، آب» و از آنجا «بخار، مه، ابر»»، و زیرمدخل‌هایش همان سه \"\n             \"سرواژهٔ نورایی‌اند: nebhos-/nebhelā (واژه‌های «ابر»)، nembh- (پهلوی namb/nam و فارسی نو nem = «نم») \"\n             \"و m̥bh-(ro-)/omb(h)- (یونانی ómbros و لاتینی imber = «باران»). واتکینز نیز همین تقسیم را با دو \"\n             \"سرواژهٔ nebh- «ابر» و ombh-ro- «باران» نگه داشته و هر دو را به «پوکورنی ۳۱۵» بازمی‌برد. دو نکتهٔ \"\n             \"احتیاطی: نخست آنکه معنی بنیادین «نمناک، آب» است و «ابر» معنی مشتق، پس «Nebh: ابر» کوتاه‌نویسی است \"\n             \"(هرچند خودِ واتکینز همین را می‌آورد)؛ دوم آنکه صفحهٔ ۳۱۵ با ریشهٔ همنامِ دیگری — ۱. (enebh-)، ombh-, \"\n             \"nobh- «ناف» — شریک است که ریشهٔ جداگانه‌ای است و نباید درآمیخته شود؛ نورایی این دو را از هم جدا نگه \"\n             \"داشته است. در شاخه‌ها، ایرانی و لاتینی/انگلیسی درست‌اند؛ تنها شاخه‌ای که زیر این ریشه جای ندارد گروهِ \"\n             \"«نمک» است (گره‌های ۵ تا ۷) و تنها فلشی که مأخذِ خودش آن را تأیید نمی‌کند Neptūnus لاتینی است \"\n             \"(گرهٔ ۱۱).\"),\n \"sources\": [W_PIE, E_NEB],\n \"ref_check\": [\n   {\"ref\": \"POK:315\", \"status\": \"supports\", \"note\": POK_ROOT + \" The three glosses of the chart map onto these sub-lemmas; the page is correct (the entry runs 315-316).\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 131 (WLD_Bd1_pages.txt ll.11804-11905)\", \"stance\": \"supports\",\n    \"note\": (\"The running head is „enebh- 131“; the entry has nebhos-, nebhelā, av. napta-/npers. neft, \"\n             \"„m̥bh-: ai. abhra-, av. awra- ‚Wolke‘“, „emb(h)-: omb(h)-: … gr. ómbros \"\n             \"‚Regen‘“ and „nembh-: pehl. namb, nam, np. nem ‚feucht, Feuchtigkeit‘ … lat. \"\n             \"nimbus“ — i.e. WP I 131, the reference Pokorny and Mann both give, is the source of the chart's \"\n             \"three-way split.\")},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. nebh- and ombh-ro- (AHD_watkins1985.txt ll.776, 801)\", \"stance\": \"supports\",\n    \"note\": (\"\\\"nebh-. Cloud. … [Pok. (enebh-) 315.]\\\" and \\\"ombh-ro-. Rain. 1. Zero-grade form *mbh-ro- in Latin \"\n             \"imber, rain: IMBRICATE … See nebh-. [In Pok. 2. (enebh-) 315.]\\\"; Watkins's essay adds \\\"nebh- is \"\n             \"'sky' in Balto-Slavic and Iranian, but 'cloud' elsewhere\\\".\")},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. nebhos (l.11570) and m̥bhros (l.11502)\", \"stance\": \"supports\",\n    \"note\": \"\\\"nebhos, -es- 'sky, cloud, mist'. WP I, 131\\\" and \\\"m̥bhros, is 'cloud, vapour, drizzle'. WP I, 131\\\" — an independent reconstruction of the same two stems.\"},\n   {\"src\": \"KLN\", \"where\": \"p. ~1035 s.v. nebula\", \"stance\": \"supports\",\n    \"note\": \"\\\"fr. I.-E. base *(e)nebh-, 'moist, vapor, mist, cloud'\\\" — Klein's base is Nourai's root, with the 'moist' sense first.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 276 s.v. *nab\", \"stance\": \"supports\",\n    \"note\": \"\\\"PIE *neb'- 'to moisten, be wet' > LIV: 448 | Pok.: 315 f.\\\" — the modern Iranian-verb dictionary uses the same root with the 'moisten' gloss.\"}],\n \"nodes\": nodes,\n}\n\ndoc = {\"pdf_page\": 353, \"book_page\": 323, \"verified_by\": \"claude-opus-5\",\n       \"verified_on\": \"2026-09-07\", \"entries\": [entry]}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-353.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk353.py"
}
```


### [2026-09-07T18:53:38.120Z] TOOL RESULT

```
written
```


## [2026-09-07T18:53:41.503Z] TOOL CALL #111: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-353.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 353"
}
```


### [2026-09-07T18:53:42.872Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 13, 'disputed': 1, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'partial': 3, 'not_checked': 6, 'not_found': 1}
books consulted: {'supports': 39, 'partial': 5, 'silent': 6, 'contradicts': 3} | by book: {'CHEUNG': 5, 'PHD': 5, 'KLN': 5, 'BRT': 4, 'WLD': 4, 'ARY': 4, 'HENNING': 3, 'POK': 3, 'HRN': 3, 'MON': 3, 'NYB': 2, 'SOD': 2, 'IEC': 2, 'FSD': 2, 'PLA': 1, 'LKT': 1, 'LAT': 1, 'LEW': 1, 'AHD': 1, 'SKT': 1}
```


## [2026-09-07T18:54:04.249Z] TOOL CALL #112: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-353.json'\nd=json.load(open(p,encoding='utf-8'))\nn=[x for x in d['entries'][0]['nodes'] if x['id']==8][0]\nold=\"(Y. 68.32 'as a cloud driven by the wind', Yt. 14.41 awra upapā, Yt. 8.40)\"\nnew=(\"(Bartholomae quotes yaθa awrəm vātašūtəm 'like a wind-driven cloud' from the Yasna — the \"\n     \"chapter numeral is illegible in our scan of AiW — together with Yt. 14.41 awra upapā and Yt. 8.40)\")\nassert old in n['derivation'], n['derivation'][:400]\nn['derivation']=n['derivation'].replace(old,new)\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=1); f.write('\\n')\nprint('patched')\nEOF\npython3 -m json.tool data/verification/page-353.json >/dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 353; head -c 3 data/verification/page-353.json | xxd | head -1; git status --short"
}
```


### [2026-09-07T18:54:05.625Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 13, 'disputed': 1, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'partial': 3, 'not_checked': 6, 'not_found': 1}
books consulted: {'supports': 39, 'partial': 5, 'silent': 6, 'contradicts': 3} | by book: {'CHEUNG': 5, 'PHD': 5, 'KLN': 5, 'BRT': 4, 'WLD': 4, 'ARY': 4, 'HENNING': 3, 'POK': 3, 'HRN': 3, 'MON': 3, 'NYB': 2, 'SOD': 2, 'IEC': 2, 'FSD': 2, 'PLA': 1, 'LKT': 1, 'LAT': 1, 'LEW': 1, 'AHD': 1, 'SKT': 1}
00000000: 7b0a 20                                  {. 
?? data/verification/page-353.json
```


## [2026-09-07T18:54:25.749Z] AGENT

Done — page 353 verified, `verify_check.py 353` reports 0 PROBLEM lines.

**Page 353 (book p. 323), 1 entry, root "Nebh, Nembh, Ombhro" — root: confirmed; nodes: 13 confirmed, 2 plausible, 1 disputed.**

- **disputed — #5 Avestan `nemadhka` "salt"**: the form is a real hapax (Yt. 14.55), but Bartholomae (AiW ~col. 1068) glosses it 'brushwood used as fuel' (← `nəmata-`, root `nam-` 'to bend'); the sense 'salt' is Henning's conjecture (BSOS IX/1 p. 85 n. 20 — the very source Mo'in cites), followed by Gharib. No source attaches `*namadka-` to the "moist" root: Pokorny 315–316 omits it, Edel'man (ESIJa V 464) reconstructs PIr `*namadka-` with no `*nebʰ-` link, and Mo'in's own footnote says the Avesta/Veda have no noun for 'salt'. Nodes #6 (namak) and #7 (Sogdian namaδk) are themselves confirmed — the sub-tree is sound but filed under the wrong root.
- **plausible — #10 Persian `abrâmŭn` «ابرآمون»**: `abr` is confirmed; ابرآمون has no entry in Dehkhoda/Mo'in/Amid — Nourai copied Tavoosi's Persian *gloss* of the Pahlavi headword `abrāmōn` (SNS p. 11) into a Persian row.
- **plausible — #11 Latin `Neptunus`**: Pokorny ("vielleicht"), Klein and Etymonline ("probably") support `*nebh-tu-s`, but Ernout–Meillet call the link with Av. `napta-` "vague" and prefer Ved./Av. `apām napāt`.
- **Bad reference (not an extraction error) — #11 refs=AHD**: Watkins has `nebh-` and `ombh-ro-` but *no* Neptune anywhere, and AHD online gives only "[Latin Neptūnus]" with no root. Marked `not_found`.
- Chart NOTEs evaluated: BQT:79's `ap-+bhr-` "water-carrier" for `abhrá-`/`abr` is folk etymology (Pokorny, WP, Mayrhofer, Cheung, Aryanpur all give `*n̥bʰrós`) — Nourai's tree wins. BQT:2155's Akkadian `nabāṭu` alternative is a genuine live dispute, but only about who gave Greek `náphtha`; Persian `naft` < Av. `napta-` is unaffected (Lokotsch 1538 prints both views).
- **No extraction errors found**: the JSON matches the printed page, including the Ferdowsi verse on node #4 (verified verbatim on BQT p. 2155).
- New audit artefacts written: `sources/refs/ocr/BQT/2170.vision.txt`, `sources/refs/ocr/SNS/11.png|11.vision.txt`, `sources/refs/ocr/SNS/282.png|282.vision.txt`; 14 web pages archived via `fetch_source.py`.
