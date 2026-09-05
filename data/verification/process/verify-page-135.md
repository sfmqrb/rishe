# Verification process log — verify-page-135


## [2026-09-05T20:07:16.772Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 135 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-135.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-135.json. Write /home/sfmqrb/git/rishe/data/verification/page-135.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 135` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:07:18.464Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:07:19.137Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:07:19.155Z] TOOL RESULT

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


## [2026-09-05T20:07:19.561Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-135.txt"
}
```


### [2026-09-05T20:07:19.587Z] TOOL RESULT

```
1	=== PDF page 135 (book page 105) ===
2	--- entry 0 ---
3	ROOT Dhont -> redirect to Dhen
4	--- entry 1 ---
5	ROOT Dhrâbh -> redirect to Dher 2
6	--- entry 2 ---
7	ROOT [Indo-European] Dhragh 1, Dhreg : to pull  (refs POK:257)
8	#1 (parent #0) [Russian] refs=AHD:400 | drožki : carriage
9	  #2 (parent #1) [Persian] refs=MON:1511; BQT:837 | doroškeh «درشکه» : horse driven carriage
10	  #3 (parent #1) [English] refs=None | droshky
11	#4 (parent #0) [Germanic] refs=AHD | dragan : to draw
12	  #5 (parent #4) [English] refs=None | draw, drag, draft
13	#6 (parent #0) [Germanic] refs=AHD | drinkan : draw into the mouth
14	  #7 (parent #6) [English] refs=None | drink, drown
15	--- entry 3 ---
16	ROOT Dhragh 2 -> redirect to Dher 2
17	--- entry 4 ---
18	ROOT Dhreg -> redirect to Dhragh 1
19	--- entry 5 ---
20	ROOT [Indo-European] Dhreugh : to deceive  (refs POK:276)
21	#1 (parent #0) [Avestan] refs=POK:276; BQT:845; SNS:324 | draoga,drauga : a lie, a demon ; dragvant, drvant : one who likes lies, atheist.
22	  #2 (parent #1) [Pahlavi] refs=BQT:846; SNS:324,325 | drôg : a lie ; druvand : non-believer
23	    #3 (parent #2) [Persian] refs=BQT:846; SNS:324; BQT:845; TZF:22 | dorŭğ «دروغ» : a lie ; dorvand «دُروند» : atheist
24	#4 (parent #0) [Old Persian] refs=KNT:191 | duruj : lie, deceive
25	#5 (parent #0) [Germanic] refs=AHD | drauma : illusion, vision
26	  #6 (parent #5) [English] refs=None | dream
27	--- entry 6 ---
28	ROOT Dhrugh -> redirect to Dhwer
29	--- entry 7 ---
30	ROOT Dhu -> redirect to Dheu 2
31	--- entry 8 ---
32	ROOT Dhu-bh -> redirect to Dheu 2
33	--- entry 9 ---
34	ROOT Dhugh -> redirect to Dheugh
35	--- entry 10 ---
36	ROOT Dhugh-tar -> redirect to Dheugh
37	
```


## [2026-09-05T20:07:22.484Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-135.json",
 "description": "Read page 135 source JSON"
}
```


### [2026-09-05T20:07:22.519Z] TOOL RESULT

```
{
  "pdf_page": 135,
  "book_page": 105,
  "entries": [
    {
      "root": {
        "name": "Dhont",
        "redirect": "Dhen"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhrâbh",
        "redirect": "Dher 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhragh 1, Dhreg",
        "lang": "Indo-European",
        "refs": "POK:257",
        "gloss": "to pull"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Russian",
          "refs": "AHD:400",
          "words": [
            {"translit": "drožki", "gloss": "carriage", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:1511; BQT:837",
          "words": [
            {"translit": "doroškeh", "gloss": "horse driven carriage", "script": "درشکه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "droshky", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "dragan", "gloss": "to draw", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "draw, drag, draft", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "drinkan", "gloss": "draw into the mouth", "script": null}
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
            {"translit": "drink, drown", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dhragh 2",
        "redirect": "Dher 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhreg",
        "redirect": "Dhragh 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhreugh",
        "lang": "Indo-European",
        "refs": "POK:276",
        "gloss": "to deceive"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:276; BQT:845; SNS:324",
          "words": [
            {"translit": "draoga,drauga", "gloss": "a lie, a demon", "script": null},
            {"translit": "dragvant, drvant", "gloss": "one who likes lies, atheist.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:846; SNS:324,325",
          "words": [
            {"translit": "drôg", "gloss": "a lie", "script": null},
            {"translit": "druvand", "gloss": "non-believer", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:846; SNS:324; BQT:845; TZF:22",
          "words": [
            {"translit": "dorŭğ", "gloss": "a lie", "script": "دروغ"},
            {"translit": "dorvand", "gloss": "atheist", "script": "دُروند"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:191",
          "words": [
            {"translit": "duruj", "gloss": "lie, deceive", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "drauma", "gloss": "illusion, vision", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "dream", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dhrugh",
        "redirect": "Dhwer"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhu",
        "redirect": "Dheu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhu-bh",
        "redirect": "Dheu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhugh",
        "redirect": "Dheugh"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhugh-tar",
        "redirect": "Dheugh"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:07:23.292Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---MATRIX---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-05T20:07:23.343Z] TOOL RESULT

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
---MATRIX---
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


## [2026-09-05T20:07:29.291Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','MON','BQT','SNS','KNT','TZF','ARY','HRN','HUB','PHD','NYB','BRT','KLN','SKT','WLD','IEC','SYN','LKT','FSD','WEB','CHEUNG','FSF','IRN','FFD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]);print()\n\"",
 "description": "Inspect refs_online.json entries"
}
```


## [2026-09-05T20:07:30.130Z] TOOL CALL #6: Bash

```json
{
 "command": "head -60 data/verification/page-127.json",
 "description": "Look at prior verification file style"
}
```


### [2026-09-05T20:07:31.444Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadab

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

CHEUNG null

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
```


### [2026-09-05T20:07:31.476Z] TOOL RESULT

```
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


## [2026-09-05T20:08:03.814Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK dherāgh / dhragh ===\"; grep -n -i \"dher[aā]\\{0,2\\}gh\\|dhragh\" POK_01.txt | head -20\necho \"=== POK dhreg ===\"; grep -n \"dhreg\" POK_01.txt | head -20\necho \"=== POK dhreugh ===\"; grep -n -i \"dhreugh\" POK_01.txt | head -20",
 "description": "Grep Pokorny for the two roots"
}
```


## [2026-09-05T20:08:04.881Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD dhragh/dhreg/dhreugh ===\"; grep -n -i \"dhragh\\|dhreg\\|dhreugh\\|dher[aā]gh\" AHD_watkins1985.txt | head -30",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-05T20:08:05.702Z] TOOL RESULT

```
=== POK dherāgh / dhragh ===
3679:Lat.  trahö  .ziehe',  traha  , Schleife',  trägum  ,Schleppnetz',  trägula  ,ds., kleine  Schleife'  können  durch  Spirantendissimilation  {^*dragö  zu  *dragö) auf  dhragh-  zurückgehen,  aber  auch  idg.  t-  haben  (:  air.  traig  ,Fuß'  usw., 8.  trUgh-).
3701:Germ.-sl.  Grundf.    kann   "^dherghno-   sein    und    stünde    dem   freilich   in seiner   Bed.    , Schößling,    Zweig',    PL  ,junges    Gebüsch'    erheblich    anders- gefärbten gr.  TQ€xyog  (Hes.,  anthoL),  tsqxvoq  (Maximus),  kypr.  t«  zsQxvija  ^  • sehr  nahe.
=== POK dhreg ===
3919:X.  dhregh-  ,laufen^
3923:auf  Palatal  wiese  hingegen  lett.  dra^u,  dräzu,  dräzt  ,schnell  laufen^,  lit. padröiti  ds.,  die  aber  mindestens  ebensogut  als  eine  Variante  auf  Palatal neben  dherägh-  ,ziehen^  gelten  könnten.  Doch  sind  sowohl  lit.  (pa)drö£ti als  auch  lett.  dräzt  ,schnell  laufen^  identisch  mit  lit.  dröztij  lett.  dräzt ,schnitzen'  (s.  dhreg-).  Die  Grundbedeutung  ist  ,schnitzen^  Alle  zahlreichen anderen  Bedeutungen  sind  durch  burschikose  Verwendung  zu  erklären.
3925:2.  dhregh'  , quälen,  reizend    '
3933:Auch  eine  Wurzel  *dhrägh-  oder  *dhregh-  :  *dhrögh-  :  *dhrdgh'  wäj möglich.
=== POK dhreugh ===
3640:1.  dhreugh-  gehören   ags.  dryge  , trocken',   drtahnian  .austrocknen,  seihen _  mit  h  statt  ^?  — ,  anord.  draugr  ^verdorrter  Baumstamm',  ahd.  truchan .trocken') ;
3943:got.    drauhsnös    f.  PI.  ,Brocken,    Brosamen';    wohl    als    Umstellung    aus  % *dkrüs-kna    mit    halt,   drushi    nächst   verknüpf  bar;    Einmischung   eines  zu  ' nhd.  trocken,  ags.  dreahnian  —  s.  2.  dher-,  dhreugh-  ,halten'  —  gehörigen. Wortes   würde   allenfalls    beide   überlieferten   Formen  als  wirklich  gespro- chene zu  betrachten  gestatten;  aber  vgl.  daneben  got.  drausnös  ds. ;  —
3955:I,  dhreugh-  ,zittern,  (sich)  schütteln,  einschrumpfen'.
3963:2.  dhreugh'  ^trügen,  listig  schädigen'^    dhrougho-s  ,Täuscher,  SchädiVel
3967:Idg.  dhreugh-  ist  sehr  wahrscheinlich  verwandt  mit  dhuer-  , durch  Täu5 schung  zu  Falle  bringen',  indem  zur  Schwundstufe  *dhru-gh-  aus  *dhuY't sich  neue  Hochstufen  idg.  *dhreugh',  *dhrough-  einstellten.  Mit  dem  er- weiternden gh  wäre  das  von  nhd.  Zwerg  identisch,  wenn  dieses  Wort' nicht  auf  ein  verschiedenes  idg.  dhuergh- , zwerghaft,  verkrüppelt'  (s.  dort) zurückgeht.
3988:lat.  fraus,  -dis  f.  , Betrug,  hinterlistige  Täuschung,  Schaden,  Strafe', frausus  sum  (Plaut.),  umbr.  frosetom  ,fraudätum*,  lat.  früstra  (jünger früsträ)  , irrtümlich,  vergeblich',  davon  früstror,  -äri  ,täusche,  hintergehe' gehören  wohl  als  c?-Erweiterung  unserer  Wurzel  hierher  (s.  darüber  unter dhreugh-)-^  unklar  ist  nur  das  a  (mot  populaire?  EM  382;  unglaubhaft WH.  I  543);
4010:Bartholomae  IF.  12,  131  Anm.  verbindet  av.  drva-  (d.  i.  driiyva-)^  das unter  anderen  Benennungen  körperlicher  Gebrechen  aufgezählt  ist  und vielleicht  , zwerghaft,  verkrüppelt'  bedeutet,  mit  anord.  dvergr,  ags.  dweorg, engl,  dioarfj  mnd.  dwerch,  nnd.  dwarf,  ahd.  twerCj  mhd.  twerc,  -ges,  nhd. Zwerg,  wozu  tiefstufig  *diirgi  in  anord,  dyrgja  , Zwergin',  ndd.  dorf]  nach Krogmann  (KZ.  62,  143)  dazu  lett.  drugt  ,zusammensiiiken'  (s.  oben 1.  dhreugh-).
4011:Für  das  germ.  Wort  käme  andernfalls  die  Deutung  als  , Trugwesen'  in Betracht,  zu  ai.  dhvards-  ,eine  Art  weiblicher  Dämonen',  Wz.  dhuer-  , durch Täuschung  zu  Fall  bringen';  es  wäre  von  dhuer-  dann  mit  demselben  -gh abgeleitet,  das  auch  in  der  WutzqM.  dhreu-gh-  begegnet  {dhuer-gh- :  dhurgh- : dhrugh-y  dhreugh-)]  auch  letzterer  entstammen  Bezeichnungen  für  kobold- artige Trugwesen.
```


### [2026-09-05T20:08:05.753Z] TOOL RESULT

```
=== AHD dhragh/dhreg/dhreugh ===
200:dhreg-. To draw, glide. Variant form of dhrag-. temp-. To stretch. Extension of ten-.
386:dhragh-. To draw, drag on the ground. Rhyming variant tragh-. 1. Germanic *dragan in: a. Old English dragan, to draw, pull: pRaw; b. Old Norse draga, to draw, pull (or Old English dragan): DRAG; c. Old English drexge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 257.]
387:dhreg-. To draw, glide. Variant form of dhragh-. 1. Na- salized Germanic form *drinkan, to draw into the mouth, drink, in Old English drincan, to drink: DRINK. 2. Nasal- ized Germanic form *drankjan, “to cause to drink,” in: a. Old English drencan, to soak: DRENCH; b. Scandina- vian *drunkna, drugna, to drown, akin to the Scandina- vian source of Middle English drounen, to drown: DROWN. [Pok. dhreg- 273.]
388:dhregh-. To run. 1. Greek trekhein (< *threkhein), to run (> trokhos, wheel): TROCHAL, TROCHANTER, TROCHE, TROCHEE; TROCHOPHORE. 2. O-grade form *dhrogh- in Greek trokhileia, trokhilia, system of pulleys, roller of a windlass: TROCHLEA, TRUCK!, (TRUCKLE). [Pok. 1. dhregh- 273.]
391:dhreugh-. To deceive. Germanic suffixed form *drau(g)ma- in Old English dréam, vision, illusion, dream (but attested only in the senses of “joy,” “music”): DREAM. [Pok. 2. dhreugh- 276.]
1094:tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
2411:TRIO trei- TRIOECIOUS weik-1 TRIP der-1 TRIPEDAL ped-1 TRIPLE pel-3, trei- TRIPLEX trei- TRIPLOBLASTIC pel-3 TRIREME ere-1 TRISKELION skel-3 TRISMUS | strei- TRISOCTAHEDRON trei- TRITANOPIA ei- TRITE ter * TRITIUM trei- TRITONE trei- TRITURATE tere-1 TRIUMVIR trei-, wi-ro- TRIUNE oi-no- TRIVET ped-1 TRIVIAL wegh- TRIVIUM wegh- TROCAR kwetwer-, trei- TROCHAL dhregh- TROCHANTER dhregh- TROCHE dhregh- TROCHEE dhregh- TROCHLEA dhregh- TROCHOPHORE dhregh- TROGON tere-1 TROIKA trei- TROPE trep-2 TROPHALLAXIS al-1 TROPHIC- threph- TROPHO-  threph- -TROPHY threph-, trep-2 TROPIC trep-2 TROPO- trep-2 -TROPOUS  trep-2 TROT der-1
2412:TROTH deru TROUBLE twer-1 TROUGH deru TROVER trep-2 TROW deru TRUANT tere-1 TRUCE deru TRUCK! dhregh- TRUCKLE dhregh- TRUCULENT tera-2 TRUE deru TRUFFLE teua- TRUNCATE tere-2 TRUNK tera-2 TRUST deru
```


## [2026-09-05T20:08:16.647Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### page 257 (leaf 265) ###\"; awk 'BEGIN{RS=\"\\f\"} NR==265' POK_01.txt | head -60",
 "description": "Print Pokorny p.257"
}
```


## [2026-09-05T20:08:17.918Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### page 276 (leaf 284) ###\"; awk 'BEGIN{RS=\"\\f\"} NR==284' POK_01.txt | head -80\necho; echo \"### page 273 (leaf 281) ###\"; awk 'BEGIN{RS=\"\\f\"} NR==281' POK_01.txt | head -60",
 "description": "Print Pokorny pp.276 and 273"
}
```


### [2026-09-05T20:08:18.737Z] TOOL RESULT

```
### page 257 (leaf 265) ###
m.  ,Halter', dharitrl  ,Trägerin',  dhartrd-  n.  ,Halt,  Stütze'  .=  av.  darddra-  n.  ,das Festhalten,  Begreifen',  ai.  dhdrma-  (=  Isit.  firmus)  m.  , Satzung,  Sitte,  Recht, Gesetz',  dharmän-  m.  ,Halter',  dhdrman-  n.  ,Halt,  Stütze,  Gesetz,  Brauch', dhdrlmani  Lok.  ,nach  der  Satzung,  nach  Brauch',  dhäraka-  ^haltend;  m. Behälter',  dhrti-  f.  ,das  Festhalten,  Entschlossenheit',  dx-dhr-d-  ,festhaltend',
253
Ahrl  (oder  sadhrlm)    Adv.    ;,auf    eia    Ziel   hinhaltend,   einem    Ziele   zu%
ji^^'m-anc-  ;nach  einem  Ziele  hin  gerichtet,  vereint,  zusammen';  didhlHä ^*     Vbsicht  zu  stützen",  av.  dldardsatä  ,er  schickt  sich  an^;
über  ai.  cZÄiVa-  ,fest^  s.  Wackernagel  Ai.  Gr.  I  25;
arm.  vielleicht  c^ac^ar  (redupl.)  , Aufenthalt,  Ruhe^  (,*Einhalten^,  vgl.  die Bed.  ,weilen,  sich  ruhig  verhalten^,  dadarem  ,nehme  ab  (vom  Wind)^,
1  ^^  ags.  darian  ,latere^,  ndl.  bedaren  ,ruhig  werden  (vom  Wind,  Wetter)^;
oT.    mit    der    Bed.    ,sich    aufstützen,    aufstemmen^    (von    der    schweren
^Vu^zelf.)  ^Qävog  ra.  ,Bank,  SchemeF,  hom.  (ion.)  d'Qfjvvg,  -vog   ,Schemel,
liuderbank^,    ion.    S-Qrjvv^,    böot.    d-gäw^,   -vxog    ,Stuh^    (setzen   ein   urgr,
^^oavo-  voraus,  das  -Qä-  aus  -?'-,  d.  i.  -«»-a-  enthalten  wird),  ion.  Inf.  Aor.
^orcaa^ai  ,sich  setzen^  (urgr.  d-qa-)]  auf  Grund  der  them.  Wurzelf.  *dherS- :
^oS'Vog  m.  ,SesseP;    kypr.  lak.  d-ög-va^'    vtcotioölov   Hes.;    mit   der   Bed.
durch  die  Sinne  festhalten,  beobachten^  und  ,ein  Herkommen,  einen  reli-
«riösen   Gebrauch   festhalten',   ä-d-egeg'   divörjToVj  dvöaiov   Hes.  (vgl.   unten
lit.  dei'^ti  ,brauchbar  sein'),  ivd^qslv  (pvldaasiv  Hes.  (von  der  them.  Wurzelf.
*dhere-]    dagegen    von    *dherd- :)   ^QTjGyicü'   voco   Hes.    (ion.) ^  d-QccaxsLv   (a)'
ivc^uiLvriO'/.BLv  Hes.,  ion.   d-QTjo'KTj'Cr}^  koine  S^QrjGTisia   ,Gottesdienst',  -d-Qfjaycog
1    reli^'iös,  fromm',  d-Qijayisvco  ,beobachte  gottesdienstliche  Gebräuche'.
*'-      Ist  äd-qioi  ,sehe  scharf  an'  bis  auf  die  Tiefstufe  n  der  Präp.  *en  (oder
' ^.  =  ''^STR-'^)   mit  ivd-QSiv  nächst  zu  vergleichen?    (Lit.  bei  ßoisacq  s.  v.)
Wahrscheinlich  hierher  äd-göog,   dd^göog  ,konzentriert,  zusammengedrängt,
versammelt^   (vgl.  zur  Bed.   ai.   sadhryaüc-]    Lit.   bei   Boisacq   s.  v.,    dazu
Brugmann  IF.  38,  135  f.).
Mit.  ai.  dharaka-  ,Behälter'  wird  von  manchen  Scogä^,  -äxog  ,Brust- harnisch;  Rumpf;  vagina'  verglichen.
Lat.  fre-tus  ,worauf  gestützt,  vertrauend',  umbr.  frite  ,fr
```


### [2026-09-05T20:08:20.628Z] TOOL RESULT

```
### page 276 (leaf 284) ###
ein  Ziel  oder  einen  Zweck  erreichen;  intr.  sich  vorfinden, gerade  wobei  sein,  zufallen',  tu/?;  ,Gelingen,  Glückszufall,  Schicksal, Los',  Göttin  Tv%ri  (wohl  ursprüngl.  eine  Wunschkuh?);  ts^xw  (tsv^w,  Aor. srsv^a,  hom.  tstvasIv,  Med.  TezvyiovzOj  TSTVAsad^ai  —  mit  sek.  k  — ,  Perf. Tsrsvxojg,  TSXvArai,  tsTsvxaTai)  ,tauglich  herrichten,  verfertigen,  herstellen, veranlassen,  hervorbringen',  TixvGv.oi.iai  ,mache  zurecht,  ziele',  xsvxog  n. ,alles  Gemachte,  Gerät,  Geschirr,  Zeug,  bes.  Rüstung,  Rüstzeug,  Waffen; Schiffsgerät;  Geschirr,  Gefäß';
ir.  düa7i  ,Gedicht'  (^dhughna),  dual  ,passend'  {*dhughlo-)]
aisl.  Inf.  duga,  Präs.  dugi,  Prät.  dugcta  ,von  Nutzen  sein,  taugen,, glücken',  Präteritopräsens  got.  daug^  ags.  deag,  as.  dög^  ahd.  toug  ,es taugt,  nützt',  Kaus.  mnd.  dögen  ,aushalten',  as.  ä-dögian  ,ds.,  ordnen',. ags.  gedlegan  ,ertragen,  überstehen';  ahd.  tuht  ,Tüchtigkeit,  Kraft',  mhd. tühtecj  nhd.  tüchtig  =  ags.  dyhtig  ,kräftig'  (über  got.  dauhts  ,Gastmahl' s.  Feist  116);
lit.  daüg  ,viel',  dduginti  ,mehren';   russ.  düzij  usw.  ,kräftig'.
WP.  I  847,  Benveniste  BSL.  30,  73  f.,  Pisani  REtlE.  1,  238  ff.
dhlaS'  oder  dbels-  (:  dhls-)  ,quetschen,  drücken'?.
Ai.  dhrsdd-  ,Mahlstein';
gr.  &laoi  ,zerquetsche,  zermalme'  (idg.  *dhlas-ö  oder  *dhlso),  idXda&rjv,. d^laaxoq]
cech.  dlasmati  , drücken'  (*dhläs-mo-  oder  *dhols-mo-)]
(phxb)  j-d'Xdo)^  ist  Kreuzung  von  d-ldo)  mit  (pltßo),  wie  andrerseits  cpXtßa> durch  Kreuzung  mit  d^Xdü)  auch  zu  d-ltßo)  umgestaltet  ist.
WP.  I  877,  Schwyzer  Gr.  Gr.  I  676.
dhlgh-  ,Schuld,  Verpflichtung'.
Air.  dligim  ,habe  worauf  Anspruch,  verdiene',  mcymr.  dlyu,  mit  epenthet. Vokal  dylyu  ,debere',  corn.  dylly  ds.,  mbret.  dellit  ds.,  air.  dliged  n. ^Pflicht,  Gesetz,  Recht'  {^dhlghito-m),  cymr.  dledj  dyled^  mc.  d(y)lyet  L ;Pflicht',  daneben  c^Zi^ , Verdienst'  (*dhlghitä)]  got.  dulgs  ßcliuld^  (an  Geld);.
272
$
aksl.  dhg^   ^Schuld^,    russ.  dolg,    skr.  düg   (Gen.  düga),   poln.   dlug^  ^^ dluh  ds.
Got.  dulgs  und  die  slav.  Worte  sind  wohl  urverwandt.
WP.  I  868,  Trautmann  55.
dho-  ^schärfen^
Ai.  dhära  ^Schneide,  Schärfe,  Klinge^,  av.  därä  f.  ds.,  tizidära-  ^m|* scharfer  Schneide^,  gr.  d^oög  ,scharf,  spitz^,  id-öwaa  ,ich  schärfte,  spitzte* (^d-o-J^ög  wo-Partiz.,  wie  z.  B.  *da-J^6g  ,zerschnitten^  in  dai^a);  für  *c?^ zum  o  vgl.  dorögidü)-).
Ob  hierher  auf  Grund  eines  *dh9-ro-  ,gespitzt^  (:  ai.  dhä-ra)  auch  agg. darod  m.  ,Spieß,  Wurfspieß^,  ahd.  tart  m.  ,Spieß^,  anord.  darrad-r  m.,  darr n.  ,Spieß^? 

### page 273 (leaf 281) ###
ostfries.  dufen,  duven% ,stoßen',  ndl.  c^o/ , Stoß,  Ruderschlag',  aisl.  dubba,  ags.  dubbian  ,zum  Ritter  ^^- schlagen',  ostfries.  dubben  ,stoßen';  da  es  auch  ein  germ.  *dab'  ,schlagen*  '^^^ gibt  (s.  u.  dhäbh-  ,staunen'),  könnte  *dub-  eine  (vielleicht  unter  Beihilfe  der  'ffi Worte  für  ,Pflock,   Zapfen'  zustande  gekommene)  jüngere  Variante  sein.
WP.  I  848.
dheues-,  dhues-,  dheus-,  dhas-  ,stieben,  stäuben,  wirbeln  (nebeln,  regnen, Dunst,  Staub;  aufs  seelische  Gebiet  angewendet:  gestehen,  verwirrt sein,  betäubt, .  dösig,  albern),  stürmen  (vom  Wind  und  aufgeregtem Wesen),  blasen,  wehen,  hauchen,  keuchen  (Hauch,  Atem,  Geist,  Ge- spenst, animal;  riechen,  Geruch)'.  Erweiterung  von  4.  dheu-',  auch Ausdrücke  für  , dunkle  Farben'  scheinen  als  ,nebelgrau,  staubfarben' angereiht  werden  zu  sollen. Ai.  dhvamsati  , zerstiebt,  zerfällt,  geht  zugrunde',  Partiz.  dhvastd-j Kaus.  dhvamsdyati,  dhvasdyati  ,bestäubt,  vernichtet',  dhvasmdn-   m.  ,Ver-
269
dunkelung^;  dhvasird'  ,hestii\iht,  besprengt^,  dhvasrd-  ^bestaubt,  unkenntlich^, dhüdsti-  f.  ;das  Zerstäuben^  (=  ahd.  tunist,  dun{i)st  ,Wind,  Sturm,  Hauch, punst';  ags.  afries.  düst  ,Staub^),  dhüsara-  , staub  farbig^;  zur  Bilduno- (*dhi-es-mi,  Konj.  dheu-s-5  neben  "^dhu-n-es-mi,  Konj.  *dhu-m-s-o)  vgl. Kuiper  Nasalpräs.  41;
o-r.  d-vu)  {ß-vioj)  ,blase,  stürme,  woge,  rauche,  opfere^  als  *dhü-{ö  (v  aus 0-öacüj  ed-vaa)  zur  einf.  Wz.  *dJmi'  (s.  S.  262),  vielleicht  aber  in  der  Bed.  ,rase^ aus  *dhüs-iö,  wie  d-vla  f. , Bacchantin^,  d-viag  ds.  {-^vaC^o}  ,bin  von  bacchischem Taumel  erfaßt')  wohl  aus  *dhüs-{a  wegen  d-vaT&deg'  Bdyixai  Hes.  und ^vad-la  ;Von  den  dvlau  getragene  Gegenstände^,  d-vaTrjQiog  Beiname  des Bacchus ;
lat.  furo  -ere  , rasen,  wüten'  kann  *dhusö  sein,  so  daß  Furiae  =  gr. ^viac,  vgl.  auch  v.  Blumenthal  IF.  49,  172  zu  övauacvar  BdxxccL]  ix^vaarj- iyc7tv6V(T7]  Hes.;  aber  d-vsXXa  ,Sturm,  Windsbraut'  wohl  Femininisierung  eines *^vsXog  , stürmend,  rasend',  wohl  aus  *^uJ^eAos;  ^vfiog  ;Zorn'  ist  =  ^vi^ög ,anima'  und  nicht  wegen  lett.  dusmas  .Zorn'  auf  eine  verschiedene  Grund- form *-9-vafx6g  zurückzuführen;  vgl.  Mühlenbach-Endzelin  I  521;
Ablautform  "^dJmes-  in  hom.  O^eblov  und  d-eCov  (mit  me
```


## [2026-09-05T20:08:29.158Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'dherāgh' in p or 'dherägh-  ,ziehen' in p or ('dherägh' in p and 'ziehen' in p):\n        print('LEAF',i)\nfor i,p in enumerate(pages):\n    if '2.  dhreugh' in p and 'tr' in p:\n        print('DHREUGH LEAF',i)\nEOF",
 "description": "Locate Pokorny leaves for the roots"
}
```


### [2026-09-05T20:08:31.117Z] TOOL RESULT

```
LEAF 285
DHREUGH LEAF 287
```


## [2026-09-05T20:08:35.208Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (268,269,270):\n    print('===== LEAF',i,'=====')\n    print(pages[i][:3000])\nEOF",
 "description": "Print Pokorny leaves 268-270"
}
```


### [2026-09-05T20:08:37.149Z] TOOL RESULT

```
===== LEAF 268 =====
it  1.  dher- , trüber  Boden-
satz' und  4.  dher-?).
Lat.  foria  PL  ^Durchfall'  (bei  Varro  von  Schweinen),  foinö,  -Ire  ,cacäre';
gr.  daQÖaiveL'  iiolvveu  (*dkr-d-)  Hes.,  nach  Fick  KZ.  44,  339  make- donisch, entweder  aus  d-aq-d--  mit  gebrochener  Red.  oder  aus  d-aq-d-  mit demselben  formantischen  -d-  wie  die  z-Erw.  dJir-ei-d-]  sehr  zweifelhaft;
lit.  der-k-iü  derkti  ,besudle  mit  Unflat,  leere  den  After'.
dbr-ei-d' :
anord.  drita  {dreit),  ags.  drltan,  mndl.  ndd.  drlteuj  ahd.  trizan  ,cacäre';    . o-stufig  anord.    dreita  ,facere    cacäre',    schwundstufig    mengl.    nengl.   dirt (aus  *drit),  aisl.  dHtj  fläm.  drits,  trets  , Dreck,  Kot',  westfäl.  dridt  , Schiß';
russ.  dial.  dristdth  ,Durchfall  haben',  bulg.  driskam^  dristh  ,habe  Durch- fall',  serb.   driskatij   dHckatij    cech.  dristati  ds.  (slav.  *drisk-,  *drist-  aus  J^ *dhreid-sk-j  -(s)t-j  Berneker  224).
WP.  I  861  f.,  WH.  I  527  f.
257
rSzb'  ;ziehen;  am  Boden  schleifen^,  gleiclibed.  mit  tmgh-  (s.  d.).
Anord.  draga,  got.  u.  ags.  dragan,  engl,  draio  ^ziehen",  anord.  drag  n. T/uterlage  eines  gezogenen  Gegenstandes^,  norw.  drag  , Luftzug^  Wellen- 'chl'*^;  Wasserlauf,  Zugseil^  dial.  drog  f.  (*dragö)  ^kurzer  Schlitten, ^Y'ecr(spur)  eines  Tieres^  Tal',  anord.  dregill  ,Band',  drög  f.  ^Streifen', ischwed.  dregh  , Schlitten',  ags.  drcege  f.  , Schleppnetz',  mnd.  dragge,  nnd. aucli  dregge  ,Bootsanker',  engl,  dredge  ds.;  ablautend  norw.  dorg  f.  \*durgöj jj,r.  *dhfghä)  , Angelschnur,  die  man  hinter  dem  Boot  herzieht';  mit  der Bed.  ,tragen'  (aus  ,schleppen',  s.  Berneker  212),  ahd.  tragan  ,tragen', iih  {gi)tragon  ,sich  betragen'.
Wohl  hierher  sl.  *därgä  in:  serb.-ksl.  draga  ;Tal',  russ.  doröga  ,Weg, j^eise',  dial.  , Angel',  serb.  dräga  ,Tal',  poln.  droga  ,Weg,  Straße,  Reise', russ.  dorözih  ,aushöhlen',  ßech.  drd^iti  ,einen  Falz  oder  eine  Furche machen,  aushöhlen';  vielleicht  auch  öech.  z-drdhati  se  ,sich  weigern',  poln. icz-dragac  sie  ,sich  sträuben,  nicht  daran  wollen'  (als  ,hinziehen')  und  aksl. podrag^  ,Saum,  Rand  eines  Kleides'  u.  dgl.  (anders  unter  dergli-  , fassen').
Lat.  trahö  .ziehe',  traha  , Schleife',  trägum  ,Schleppnetz',  trägula  ,ds., kleine  Schleife'  können  durch  Spirantendissimilation  {^*dragö  zu  *dragö) auf  dhragh-  zurückgehen,  aber  auch  idg.  t-  haben  (:  air.  traig  ,Fuß'  usw., 8.  trUgh-).
WP.  I  862,  Trautmann  45.
dbcrbh'
===== LEAF 269 =====
  (dherobh-?)  ,arbeiten'.
Arm.  derbuk  ,rough,  stiff,  rüde';
ags.  deorfan  st.  V.  ,arbeiten;  umkommen',  gedeorf  n.  ,  Arbeit,  Mühsal', afries.  for-derva,  mnd.  vor-derven,  mhd.  verderben  ,umkommen',  auch  Kaus. ^verderben';
lit.  dirbu,  dirbti  , arbeiten',  ddrbas  , Arbeit',  darbüs  ,arbeitsam'.
WP.  I  863,  II  631,  Klügelt  101,  649,
dherebh'  , gerinnen,  gerinnen  machen,  ballen,  dickflüssig'.
Ai.  drapsd-h  m.  ,Tropfen'??;
gr.  TQeqisad-ai,  Tstqocpevai  ,gerinnen,  fest  sein',  XQecpu),  dor.  rgdcpco  , mache gerinnen  (ydXa]  tvqöv),  nähre  (*mache  dick,  feist),  erziehe'  (^QeipWy  ed-gstpa), tQocpög  ,nährend',  f.  ,Amme',  d-qe^if-ia  ,das  Genährte,  Pflegling,  Kind, Zuchtvieh',  TQOcpig  ,feist,  stark,  groß',  TQOcpallg^  -Idog  , frischer  Käse,  ge- ronnene Milch',  Taocpvg  , dicht',  rdgcpea  PI.  n.  , Dickicht',  TQacpeqr]  (yfj) ;festes  Land';
nasaliert  und  mit  idg.  b  (idg.  Artikulationsschwankung  in  nasaler  Um- gebung) d-QOi-ißoq  ,geronnene  Masse  (von  Milch,  Blut  usw.)',  ^go^ßdof-iai jgerinne',  d-QOfißeTov  ,Klümpchen';
17
268
as.  derli   (*dartia)  ^kräftig;   böse^^   afries.   mnd.   derve  ^derb,   gerades (verschieden  von  ahd.  derh  ^ungesäuert'  =  anord.  pjctrfr),  ablaut.  anor^ djarfr  , mutig,  kühn'  (die  ältere  Bed.  noch  in  norw.  dial.  dirna  aus  *c?iVa3I ^zunehmen;,  wieder  zu  Kräften  kommen');  anord.  dirfa  , ermutigen';
nasaliert  wohl  anord.  dramh  , Übermut'  (*dick  sein),  nisl.  dramhr  ,Knoteni im  Holz';  anord.  drumhr  , Klotz';  mnd.  drummel  ^gedrungene  Person'.
WP.  I  876.
dheregh-  mit  Formans  -(e)s-  und  -no-  in  Namen  beerentragender  strau- chiger Pflanzen,  bes.  auch  von  solchen  Dornsträuchern,  woraus  z.  t1 ,Dorn'?    Zweifelhafte  Gleichung.
Ai.  dräksä  ,Weintraube';
gallorom.  *dragenos  ,Dorn*,  air.  draigen  m.  , Schlehdorn*,  cymr.  drae^ m.,  nbret.  di^ean  , Dornstrauch'  (kelt.  "^drageno-  aus  *dhr^gli-)'^
vielleicht  auch  ahd.  tirn-pauma  ,cornea  silva*,  tyrn,  dirnhaum  ,cornus*^^ nhd.  dial.  di(e)rle,  dirnlein  ,Kornelkirsche',  Schweiz,  tierlij  falls  nicht! aus  dem  Slav.  in  sehr  alter  Zeit  entlehnt;
lit.  dngnes  PL,  lett.  drigenes  ,schwarzes  Bilsenkraut'  (vgl.  Mühlenbach-1 Endzelin  I  498),    falls  nicht  aus  dem  Slav.  entlehnt;
russ.  dereuj  deren  , Hartriegel,  Kornelkirsche',  skr.  drijen,  öech.  drin  ds. poln.  (alt)  drzon  jBerberitze',  kaschub.  drbn  , Dornen',  polab.  dren  ,Dorn'.
Germ.-sl.  Grundf.    kann   "^dherghno-   sein    und    stünde    dem   freilich   in seiner   Bed.    , Schößling,    Zweig',    PL  ,junges    Gebüsch'    erheblich    anders- gefärbten gr.  TQ€xyog  (Hes.,  anthoL),  tsqxvoq  (Maximus),  kypr.  t«  zsQxvija  ^  • sehr  nahe.
WP.  I  862  f.,  Pedersen  KG.  I  97,  M.-L.  2762.
dheregh-  {dhrgh-nä-)  , drehen,  winden,  wenden'  (auch  , spinnen,  nähen*).
Npers.  darz,  darza  ,Naht*,  darzmän,  darznän  , Faden
===== LEAF 270 =====
 drehen,  sich kehren;  zurückkehren*,  dafn  , bitter,  herbe*  (vgl.  oivog  zgerrsTac  u.  dgl.), darj  jWendung,  Umkehr,  Rückkehr*,  Kaus.  darjucanem  ,verto,  averto, converto,  reddo*;
alb.  dreth  (St.  *dredh-),  Aor.  drodha  ,umdrehen,  zusammendrehen, zwirnen,  spinnen*,  alb.-skutar.  nnrize  ,Windel*  (n-dred-ze)-  nach  Pedersen Hitt.  123,  125,  Toch.  Spracbg.  20  hierher  hitt.  tar-na-ah-hi  ,ich  stecke ein,  lasse  hinein*,  toch.  A  tärnä-,  tärk-,  Prät.  A  cärk,  B  carka  , lassen, entlassen'  (?).
WP.  I  863,  Liden  Arm.  St.  101  ff.,  Meillet  Esquisse^  111,  Kuiper  Nasal- präs. 151.  '^^
259
dbers'  , wagen,  kühn  sein',  älter  ,angreifen,  losgehen*  (auch  mit  -i-,  -u- erweitert).
Ai.  dhrs-nö-ti,  dhdrs-ati  ,ist  dreist,  mutig,  wagt',  ährsü-  (Gramm.),  dhrsat Jierzhaft'  (=  av.  dard^at),  dhrsnii-  ,kühn,  tapfer,  mutig,  dreist,  frech', dhfstd-  ,keck,  frech',  dhfsüa-  ,kühn,  mutig',  dädhrsi-  ,beherzt,  kühn',  mit Objekt  dharsayati  ,wagt  sich  an,  vergreift  sich,  bewältigt',  dharsana-  n. , Angriff,  Mißhandlung',  dharsaka-  ,angreifend,  über  etwas  herfallend';  av. darsam  Adv.  ,heftig,  sehr',  darsi-,  darsyu-,  darsita-  ,kühn',  apers.  adar^- nau§  ,er  wagte',  dädarsi-  EN;
gr.  lesb.  -d-sgaog  n.  ,Mut,  Kühnheit'  (hom.  QsgalTrjg  ,Frechling'),  mit aus  dem  Adj.  verschleppter  Tief  stufe  ion.  altatt.  d^ccQOog  (att.  ^agoog)  ds., att.  d-gdaog  n.  ,Mut,  Kühnheit;  Verwegenheit,  Frechheit',  d-aqüeu),  d^aggeo) ,bin  mutig',  S-agavg  (rhod.  QaQGvßiog,  ther.  Qhagvfxaqhog),  d-gaavg  ,kühn, mutig;  verwegen,  frech'  (=  ai.  dlifsu-),  lesb.  Adv.  -S^goaecjg,  Mgavvog mutig,  getrost,  vertrauend'  (*-9-ag(To-avvog)]
lat.  infestus  , feindlich*,  infestäre  , feindlich  behandeln,  angreifen'  und manifestus   , handgreiflich,   auf  der  Tat  ertappt;    offenkundig'   (*dhers-to-)]
got.  ga-dars  ( :  ai.  Ferf .  dadhdrsa  ,hat  sich  erkühnt'),  Inf.  gadaürsan,  ,ich wage',  as.  gidurran,  ags.  dear^  durran,  ahd.  {gi)tar,  (gi)turran  ,wagen',  ahd. giturst,  ags.  gedyrst  f.  , Kühnheit,  Verwegenheit'  (=  ai.  drsti-h  ,Kühnheit');
lit.  nasaliert  lit.  dresü  ,wage*  (*dhrensö),  dristü,  dristi  {dhrns-)  , wagen', drqsä  (*dkrons-)  , Dreistigkeit',  di-qsüs  =  lett.  drüoss  ,mutig'  (*dhrons-j alit.  noch  drisüs  und  draiisniaus)]  ohne  Nasalierung  apr.  dirstlan  , stattlich* und  dyrsos  ,tüchtig'  (*dirsu-);
hierher  vielleicht  toch.  A  ^sär  ,rauh',  tsrasi  , stark',  B  tsirauüe  , Stärke*.
WP.  I  864,  WH.  I  698  f.,  Trautmann  60,  Van  Windekens  Lexique  147.
dbes-,  dhos-  in  religiösen  Begriffen.
Arm.  di'Jt  , Götter*  (PI.  *dheses)',  lat./eWae  (alat. /esiae)  ,Tage,  an  denen kei
```


## [2026-09-05T20:08:45.658Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (284,285,286,287,288):\n    print('===== LEAF',i,'=====')\n    print(pages[i][:3500])\nEOF",
 "description": "Print Pokorny leaves 284-288"
}
```


### [2026-09-05T20:08:47.662Z] TOOL RESULT

```
===== LEAF 284 =====
 Und  allenfalls  dazu  als  ,mit  einem  Spieße  verwunden^  weiter die  germ.  Sippe  von  as.  ags.  derian  ,verletzen,  kränken^,  ahd.  terren neben  tarörij  -en  ,schaden,  verletzen',  ags.  daru  f.  ,Schade,  Verletzung', ahd.  tara  f.  ,Verletzung' ?
WP.  I867f.  .:^
dbö[u]-  :  dhü-  ,Strick'??
Gr.  '^a)^t(y)J,  -lyyog  f.  ,Strick,  Schnur,  Band,  Sehne  des  Bogens'  (setzt ^-d-w-fio-  oder  -(j,g  voraus),  lat. /wnis  ,Seil,  Strick,  Tau';  Ablaut  ö[u]-:ü-, wenn  lat.  ü  nicht  allenfalls  dial.  Entw.  aus  ö;  nach  J.  Duchesne-Guillemin (BSL.  41,  178)  angeblich  hierher  toch.  AB  tsu-,  B  tsaio  ,sich  vereinigen' (??).
WP.  I  868,  WH.  567  f.  Vgl.  auch  Petersson  Heterokl.  169  f.
dhrebh'  ,zerbrechen,  zermalmen'.
Got.  gadrahan  ,aushauen,  karo^sly^j  anord.  draf  n.,  ags.  droef  n.  , Ab- fall', anord.  drafna  ,sich  in  kleine  Teile  auflösen',  blöp-drefjar  m.  ,Blut- flecken';
aksl.  drohljq,  drobiti  ,zerreiben,  zerbrechen',  russ.  droh^  f.  ,Bruch,  Bruch- stück', russ.-ksl.  drobhm,  bulg.  drohen  ,klein,  gering',  woneben  mit  Ablaut e :  hulg.  drehen  ds.,  dr^eb  ,Abfall  von  Wolle,  beim  Flachsriffeln;  Leber', russ.  drehezg  ,Scherben,  Trümmer';  Fick  BB.  2,  199,  Berneker  225—226 (m.  weiterer  Lit.).
Mit  got.  lilaiwj  patei  luas  gadrahan  us  staina  vergleicht  Hoffmann  BB. 18,  288  Toacpog'  x&cpog  Hes.,  so  daß  die  Anwendung  unserer  Wurzel  auf das  Herausbrechen  von  Steinen  alt  wäre.
Eine  ähnliche  Wz.  dhreh-  in:
Anord.  drepa  ,stechen,  stoßen,  töten',  ags.  drepan  ,erschlagen,  treffen', mnd.  drepen  ,treffen,  kämpfen',  ahd.  treffan  ,treffen,  berühren',  anord. drep  n.  ,Schlag',  ags.  gedrep  ds.,  mhd.  tref  m.  n.  ,Streich,  Schlag,  Treffe
273
2usamraentreffen^,  ags.  drepe  m.  {*drapi-)  ,Totschlag^,  anord.  dräp  n.  ds.; vermutlich   als   kvxdi   drejpit  stefjum:   anord.  dräpa   f.  ^ein  aus  mehreren durch  sog.  stef  unterschiedenen  Teilen   bestehendes    Gedicht;    gewöhnlich ein  Lobgesang^ WP.  I  875  f.
direg--  ^ziehen;  dahinziehen,  gleiten,  streifen^,  gleichbedeutend  mit  trdgh- (s.  dort).
Ai.  dhrdjati  ^streicht,  gleitet  dahin^,  prd-dhrajati  ,eiW,  dhrdjas-  n.,  dhra- jati-  f.  ,das  Streichen,  Zug^,  dhräj-  etwa  .Zugkraft^,  dhräji-,  dhröji-  f. ,Zug,  Trieb^;
auord.  drälc  f.  ,Streifeii^  (:  ai.  dräj-)\  nasaliert  dazu  vielleicht  got.  drlgkan, aisl.  drekka,  ags.  drincan,  ahd.  trinkan  ,trinken^  feinen  guten  Zug  machen, ducere  poculaO;
lit
===== LEAF 285 =====
.  drezöti  ^glattstreichen^,  dryzasj  druo!tl  ,streif]g^,  auch  (?)  lit.  drez-iu, 4i  jreißen'^,  nudrUti  ,herunterreißen^  (Juskevic  346);  dazu  wohl  drö^ti ^schnitzen,  schlagen,  gehen'  usw.,  lett.  dräzt  ds.;  s.  unter  1.  dregh--^
Lett.  dragät  ,zerren^  dagegen  vermutlich  zu  mndl.  trecken  ,ziehen',  s. 4.  der-  (dergh-,  dreg-)  ,schinden'  und    Mühlenbach-Endzelin  I  488  m.  Lit.
WP.  I  874.
X.  dhregh-  ,laufen^
Arm.  durgrij  Gen.  drgan  ,Töpferscheibe'  (nach  Meillet  BSL.  36,  122  aus *dhrgh-) ;
gr.  TQSxo)  (dor.  rgdxoüi),  Fut.  äTto^qi^of-iaL^  ^gi^o)  ,laufen^,  tqoxoq  (:  air. droch)  ,Rad^,  Tgöxog  ,LauF,  fQÖxi'g  ,Läufer,  Bote^,  tQOx'i^og  ,Strandläufer^; kaum  TQccxrjlog  ,Nacken,  Hals^??    Pedersen   IF.  5,  56,  Zup.  KZ.  36,  57;
air.  droch  ,Rad^  (*drogo-n)',
auf  Palatal  wiese  hingegen  lett.  dra^u,  dräzu,  dräzt  ,schnell  laufen^,  lit. padröiti  ds.,  die  aber  mindestens  ebensogut  als  eine  Variante  auf  Palatal neben  dherägh-  ,ziehen^  gelten  könnten.  Doch  sind  sowohl  lit.  (pa)drö£ti als  auch  lett.  dräzt  ,schnell  laufen^  identisch  mit  lit.  dröztij  lett.  dräzt ,schnitzen'  (s.  dhreg-).  Die  Grundbedeutung  ist  ,schnitzen^  Alle  zahlreichen anderen  Bedeutungen  sind  durch  burschikose  Verwendung  zu  erklären.
WP.  I  874  f.
2.  dhregh'  , quälen,  reizend    '
Ai.  dräghate  (Dhätup.)  ,quält,  plagt,  müht  sich^; osset.  äw-därzin  ,reizen^  (E.  Lewj  KZ.  52,  306);
ags.  dracu  L  ,Plage,  QuaP,  dreccan  ,reizen,  plagen'  (?  mit  expressivem  k?)- aksl.  raz-draBg,  -dra^iti  ,zum  Zorn  reizen',  serb.  dräzlm,  drdziti  ,reizen';
18
274
f
ein  «i-Abstraktum  *dra^nh  ^Reizung^   liegt    russ.  draznith  ,reizen,  neck^
zugrunde,  z  statt  i  nach   dem  gleichbedeutenden  Formans    ziih.
Auch  eine  Wurzel  *dhrägh-  oder  *dhregh-  :  *dhrögh-  :  *dhrdgh'  wäj möglich.
WP.  1  875.
dhreibh'  ^treiben,  stoßen^  usw.
Got.  dreiban  ^treiben,   stoßen',   anord.  drifa   ,gezogen    kommen,   ziehei strömen'   usw.,    ags.  drlfan    ,treiben,   jagen,   stürzen',   as.    driban   ,bewe werden,   vertreiben',   ahd.  trlhan   ,peUere,   expellere'    (schwundstuE.  schi Verb    tribön    ,agitare',    uohifribön    ,peragere');    anord.    drift    f.    ,Treibe3 Schneewehe',  drif  n.  ,was   durch   die   Luft  treibt,  Gestöber',  ags.  drif ,Treib.>n,  Trift,    Getriebenes',    drnf  f.  ,Treiben,  Trift,    Herde',    mhd.  trij ds.,  nhd.   Trift  ,Vieh weide,  Herde';
lit.  drimbü,   dribti   ,langsam    niedertropfen',  sniegas  drimba   ,der  Schn( fällt   dicht'   (=  anord.  pä  drtfr  sncer)-,    von   drlb-   aus,   das   sowohl   der, wie    der    e-Reihe    angehören    kann,    ist   Übertritt   in    die    e-Reihe    erfolgt drebiü,  drebti  ,mit  Dickflüssigem   werfen,  klecksen'.
WP.  I  «72,  876,   Wissmann   Nom.  postverb.  68  f.,    Specht  KZ.  68,
dbreu-  mit  kons.  Erweiterungen  ,zerbrechen,  zerbröckeln';  damit  sind  wohl aus  intransitiv*  m  ,abbröckeln'  erklärbare  
===== LEAF 286 =====
Worte  für  , herabfallen] herabtröpfeln'  zu  verbinden.
I.  dbreus-,  ähreu-s-z
Gv.  d^Qccvo)  {Tayf^Qavoi-iaij  i&gavad^rjv)  ,zerbreche,  zermalme',  ■d^gauffTÖg. ä-gavXö^  (*d-()avG-lÖL),  &QavQOg  (Hes.)  , zerbrechlich',  ^^«v^/or,  d^gava^a  , Bruch« stück,  Wunde',  d-Qärvoaoj  (Lyk,),  owied-gärwiai  (Eur.)  ,zerschmettern' (weist  auf  *d-Qav[a]-av6(g^  s.  Boisacq  s.  v.  m.  Lit.);  d^gv/^x^V  (Hom.), ^QvU^ag  (Ijjk.)  , brechen,  zerschmettei-n',  O^fjvXsl  zagdoffSL'  dyX^i  Hes, (*^^rAoc;  aus  *d-{jvG-Xo-\  gr.  -av-  und  -v-  sind  als  Reduktionsstufe  und Schwundstuf«  eines  dhreus-  zu  verstehen,  woneben  dhreus  ;  s.  Bechtel  KZ. 46,  164);
cymr.  dryll    , Bruchstück'    (*dhrus-lio-)j    gallorom.    PL  drullia    , Abfälle'  ■ (Kleinhans  bei  Wartburg  III   163);
got.    drauhsnös    f.  PI.  ,Brocken,    Brosamen';    wohl    als    Umstellung    aus  % *dkrüs-kna    mit    halt,   drushi    nächst   verknüpf  bar;    Einmischung   eines  zu  ' nhd.  trocken,  ags.  dreahnian  —  s.  2.  dher-,  dhreugh-  ,halten'  —  gehörigen. Wortes   würde   allenfalls    beide   überlieferten   Formen  als  wirklich  gespro- chene zu  betrachten  gestatten;  aber  vgl.  daneben  got.  drausnös  ds. ;  —
got.  driusan  ,fallen,  herabfallen',  as.  driosan,  ags.  dreosan  ,fallen',  norw. dial.    drysla    ,herabrieseln';    Kaus.    got.    gadrausjan    ^niederwerfen',    ahd.
275
trören  ^tröpfeln,  triefen  machen,  a,b\verfen';  dazu  als  ^zusammenfallen,  ein- knicken'  mit  lautsyinboliscli  «gedehnter  Schwundstufe:  a^s.  drüsian  ,Träoe sein  (^'0''  Alter)',  engl,  drowse  ,schläfern';  ahd.  trüren  ,uieder^esch lagen sein,  trauern]  die  Augen  senken',  mhd.  trürec  ,traurig';  ags.  ablautend dreorig  ,betrübt';  anord.  dreyri  m.  {*dvauzan-)  ,das  aus  der  Wunde  trie- fende Blut',  as.  drör  ra.  ,Blut'  (ags.  ablautend  dreur  m.  ds),  mhd.  trör in.  , Tau,  Regen,  Blut';
lett.  druska  , Krümel',  lit.  druskä  ,Salz'  (* Krümel)^  apr.  drii.skins  ,0h ren- schinalz'  (überliefei-t  dmskins);  dazu  bsl.  *driizga  ,kleines  Stück'  in  lit. driizgas  ds.,  sloven.  drüzgati  ,
===== LEAF 287 =====
zerdrücken',  usw.
Labialerweiterungen :
dhreuhh-:  ^v.  d^gv/iiw  {iTQv<fr]v)  ,zerreiben,  zerbröckeln;  entkräften, ve^^veichlichen,  hinfällig  machen',  &()v^ij.ta  und  rgtxpog  n.  ,Bruchsiück', Tßi;y>}  , Weichlichkeit,  Üppigkeit',  jQvcpegöq  , weichlich'  (s.  auch  Boisacq  s.v. Ofjürrruß) ;
lett.  di'uhaza  ,Trumm',  druhazas  , Holzsplitter'.
dhreup-:  as.  dritiön,  drüvön  , betrübt  sein';  lett.  drwpn,  drupt  ,zerfallen, in  Trümm.T  gehen',  draü/nt  ,zerbrÖckeln';  vgl.  Mühlenbach- Endzelin  I  öOö.
dhreub-:  anord.  driüpa,  as.  dnopan.  ags.  dreopan^  ahd.  triofan  ,trief.'n, tropfen',  o-stufig  schw.  Verb,  ags.  dreaplan  ,destillare',  e-stufig  dreopioM ds.,  anord.  drüpa  (*-en)  , überhangen,  herabhangen,  sich  bücken',  anord. dropi  m.  , Tropfen',  ags.  dropa,  as.  dropo  ds.;  Intens,  ags.  dryppan,  dropplauy ahd.  tropf ön  , tropfen',  tropf o  , Tropfen';  aisl.  dreypUj  ags.  drinpan  ,träufeln';
air.  druckt  , Tropfen'  {^dhrvptu-s).
WP.  I  872  f.,  WH.  I  553  f.,  Wissmann  Nom.  postverb.  21,  104,  136,  140 f., 182,  Trautraann  61  f.,  Kluge^^  s.  v.  Trauer.
I,  dhreugh-  ,zittern,  (sich)  schütteln,  einschrumpfen'.
Ags.   dryge  , trocken'  usw.,  s.  oben   S.  254 f.   unter  dhereuyh-;
lit  drvgys  , Fieber;  Schmetterling',  lett.  drudzis  , kaltes  Fiebei-;  Fieber', drndzindt  ,nach  Futter  wiehern'  (,*sich  schütteln'),  vielleicht  apr.  drogis jRohr'  (wenn  für  drugis^  s.  Trautniann  Apr.  323  m.  Lit.,  Mühlen bach- Endzelin  I  502);  vielleicht  lett.  drugt  , zusammensinken,  sich  mindern', Berneker  231  zw  ;  s.  auch  unten  S.  279;
poln.  drze,  drzec  ,zittern',  alt  auch  ,firbern',  drgac,  perf.  drguqc  ,zittern, beben;  zappeln,  zucken',  russ.  drozii,  -dtb,  perf,  drögmith  , zittern,  beben' (usw.,  s.  Berneker  231).  Zweisilbige  Wurzelform  *dhereugh-  txler  *dhe7'eiig- vermutet  man  in  gr.  Toi&OQvaasiv  asieiv  Hes.,  xoi^ogv^cuta'  tj  Tot?c  oeio- liob<^  noiovaa  Hes.  und  TavOauvt^Wj  rav-^'alc^w  ds.   Hes.
WF.  I  873  f.,  Berneker  231.
18*
276
9
2.  dhreugh'  ^trügen,  listig  schädigen'^    dhrougho-s  ,Täuscher,  SchädiVel
Ai.  drühyati  , sucht  zu  schaden,  tut  zuleide'  (Fut.  dhröksydti^  Par^ drugdhd-),  apers.  Imperf.  adurujiya  (=  ai.  adruhyat)  ,log',  av.  dryj^d^ jlügt,  betrügt',  ai.  drögha-,  dröha-  m.  , Beleidigung,  Beschädigung,  Verrat av.  draoga-  ,lügnerisch',  m.  ,Lüge,  Trug',  apers.  drauga-  , lügnerisch' druh-  ,schädigend',  f.  , Beschädigung,  Unholdin
===== LEAF 288 =====
,  Gespenst',  m.  ,Unhold' av.  druj-  f.  ,Lüge,  Trug;  Verkörperung  der  Lüge';
mir.  aur-ddrack  (nachtonig  aus  *druag  =  ai.  drögha-)  , Gespenst';
as.  bidriogauj  ahd.  triogan  ,trügen',  anord.  draugr  m.  , Gespenst'^ schwundstufig  as.  gidrog  n.  , Trugbild',  mndl.  gedroch  ds.,  ahd.  gitrog  i} ,Betrug,  teuflisches  Blendwerk';  anord.  draumr^  ahd.  troum,  as.  drt engl,  dream  ,Traum'  (germ.  *drau{y)ma-  ,Trugbild').
Idg.  dhreugh-  ist  sehr  wahrscheinlich  verwandt  mit  dhuer-  , durch  Täu5 schung  zu  Falle  bringen',  indem  zur  Schwundstufe  *dhru-gh-  aus  *dhuY't sich  neue  Hochstufen  idg.  *dhreugh',  *dhrough-  einstellten.  Mit  dem  er- weiternden gh  wäre  das  von  nhd.  Zwerg  identisch,  wenn  dieses  Wort' nicht  auf  ein  verschiedenes  idg.  dhuergh- , zwerghaft,  verkrüppelt'  (s.  dort) zurückgeht.
WP.  I  874.
dhrigh'  (oder  dhreikb-)  ,Haar,  Borste'.
Gr.  d^Qi^j  tQix^g  f.  ,Haar,  Borste',  davon  d-glaaccy  att.  ^giTta  f.,  ein  Fisch mit  feinen  Gräten',  TQixiag,  'f^^X'S  ds.;
mir.  gairb-driuch  (*drigu-  oder  *driku-)  ,Borste'  (garb  ,rauh');
aus  gr.  d^Qiaaa  stammt  wohl  ital.-lombard.  trissa  ,Lota  Iota';  daraus  wohl ebenfalls  Schweiz.   Trische  (11.  Jh.  trisca)]
falls  bsl.  *draika'  ,lang  gestreckt'  als  *dhroiko-  hierher  gehört,  also  lit. driekti  ,ausdehnen,  ausziehen  (einen  Faden)',  drykti  ,in  langen  Fäden herabhängen',  slovak.  driek  m.  , Stamm',  driecny  ,stämmig',  abg.  dvbkoh , Stange',  usw.,  könnte  unsere  Wurzel  als  *dhreikh-  angesetzt  werden.
WP.  I  876,  Jud  BullGlPat.  Suisse  Rom.  11,  8  2,  Trautmann  58  f.,  Ber- neker  223,  232.
dhrono'  ,bunt'?
Für  gr.  ^QÖva  PI.  , Blumenverzierungen  in  Gewändern  (bei  den  alexan- drin. Dichtern  für  q)dQ[.i(xy,a,  Zauber-,  Heilkräuter  gebraucht),  bunte  Ge- wänder, bunte  Tiere'  erschließen  Hoff  mann  BB.  15,  86,  Liden  Stud.  67  f. eine  Grundbed.  ,bunt'.  Unter  dieser  Grundbed.  vergleicht  Liden  aaO. alb.  dre-rij  geg,  dr^-ni-  m.  , Hirsch'  (Tiere  aus  dem  Hirsch-  und  Reh- geschlecht sind  häufig  als  ,gesprenkelt,  bunt'  benannt),  wofür  eine  illyr. Gdf.  *drani-  (idg.  dhroni-)  durch  die  wohl  illjr.  Hesychglosse  aqavL^' klaq)OQ  {A-  verschrieben  für  /1-)  geboten  wird.
277
Stokes  Mel.  Kern  [RC  24,  217]  vermutet  für  d-göva  als  eigentliche  Bed. Stickerei'  wegen  mir.  druine  ds. '    AVP.  I  8'^6  f.,  WH.  I  374.
fitiüg{b)ster'  ,Tocliter';  Guttural  wie  bei  *eg{h)om  ,ich',  s.  dort.
Ai.  duhltdr-  {duhitd),  av.  dugddar-,  duySar-  (aus  *dughter-),  npers. duxtar,  duxt,  arm.  (mit  s  au
```


## [2026-09-05T20:09:09.450Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT draoga ===\"; grep -n \"draoga\\|drauga\" BRT.txt | head -20\necho \"=== BRT drug/druj ===\"; grep -n \"druj-\\|drug-\\|drə\" BRT.txt | head -20\necho \"=== BRT drvant/dragvant ===\"; grep -n \"drvant\\|dr.gvant\\|druuant\\|drvaṇt\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:09:09.526Z] TOOL RESULT

```
=== BRT draoga ===
12781:yeJH .  .pascalta  'Ü/raspayeiti  miirB  Yt.  10. 1 41—43;  loi;  —  dahmS  zaota  tanu.piriäia  1 vfia,sraolSrS  yesi  */'/  tanup>rih5  va^  .  .  I yai  äat  'ii .  .  ti.jS;  vgl.  ^p;  —  hvarlta\ mahrä  . .  aat  'T/  a7'a^ayamaATY.4.ii.*'';\ 3ff.,  34.3,55i,'Vr.n.i3B;—/ravaülys\ .  .  yatlra  vä  'll  (.\Pf.)  paurva  fräyatmte Yt.  13.  47;  —  n  dahyüv^  imä  . .  drauga*- dis  (APf.)    AamihUya    akunaui'  Bh.  4.  4;
13997:767  Muviätaraoani  —  draoga-  7Ö8
14015:fianiv  *^<»foV(sd-)  /y^  manä  iarlam^  iiuLLER  WZKM,/.  153, //,  156,  Fov  KZ.  jj. naisim  vamavätaiy  duruxtam  *mamy.1-  30,  3/.  541,  ZDMG.  51.  595.  Ich  bleibe  bei iaiy  "damit  nicht  dem,  der  .  .,  (dass)  es  dem  %  3ng  II  Gesagten. ihn  nicht  überzeuge,  (sondern  dass  er  es)  I  ,  j_  draoga-,  draoya-,  p.  drauga-  i)  Adj. für  gelogen  halte"  Bh.4.8*>;  —  /■'^''^l  lügnerisch,  unwahr':  yal  ..  *'gpm  väcim imJ' hasiyam  naiy  duruxtam  aiunamm\a„Aai>m  anmäne  {&A.)  *paiti.barata  Yt hamahyayä  %ardcr  "dass  ich  das  wirklich,  |  ig_  jj  jj  m  'Lug,  l.üge':  'gitn  vi'^us
14030:KompA.  —  Zum  V.  draeg-,  —  >)  Mit  poli- tischer Firbungi  I.  in  drauga-.
14034:KompE.  —  Superl.  lu  *''drug-  und  draoga-  Adj.
=== BRT drug/druj ===
6062:und  recht  ist,  das  Ä-^wnsche  Reich  der  Wahr- heit und  seine  Ordnung;  heiliges,  ewiges Recht,  göttliche  Ordnung',  i)  bes.  im Gegensatz  zu  drug-  (sd.);  a)  im  gAw.: alUa  ahmsi  varmäi . .  nidätfm  '&nt  siiidyät tka^äi  (sd.)  rSsayeAhl  druxl  "und  in diesen  (unseren)  Glauben  ist  das  ASa  (die Wahrheit)  niedergelegt  .  .,  in  die  Aftcr- lehre  die  Drug  (die  Lüge).."  Y. ^ß. 3; —  yai  adais(sd.)  "sä  (als  Sub].)^*  *drvßm vSniakaitT  "wenn  . .  das  Asa  (das  Reich der  Wahrheit)  die  Drug  (das  Reich  der Lüge)  überwinden  wird"  Y.4ß.  1;  —  kaära °sai  drvptn  dyai  zastayS  (sd.)  '^.44-  14;
11966:•  j.  tanu.drug-  Adj.  'des  Leib  mit  der Dr.  verbunden,  der  mit  ihr  eins  geworden ist''>:  vUpe  drvants  'drujS{^V.) yS  adtrits.- ikalsß  (sd.)  V.  76.  18.
12480:•  j.  'daeva-  Adj.  (fem.  'dapvj-)  'den Dapva  zugehörig,  von  ihnen  herrührend (usw.),  rfa?iisch':  kB  asti  'vö  ks  da^aySzB "wer  gehört  zu  den  Z>.,  wer  ist  ein  Z>.- Anbeter?"  V.Ä31;  32';  —  kva  asti  'vB kva  datvaydzB  Y.y.sz'y  54'.  yt77.6;  — yat  nürsm  vyämbura  (sd.)  'va  maSyäka da^vayäsB  vohuntm  vä  täc^änti  YL  7^.  54; — -  ga%Bittsca  'vJsüa  *handramana  (sd.) N.  5j;  Yt.  77, 6.  et)  sonst  von  drug-: aiXm  dahaktm  ..  'vTm  *dru/im  V.5. 8;  — Hat  ki  ha,  paiti.davata  ya.  'vi  druxl  V. 18.  $1;  —  nase  °vJ  druxs  SrB.j;  — sraosim  ..yd  janta  °vaya  drujB  Y.57. 15.
14034:KompE.  —  Superl.  lu  *''drug-  und  draoga-  Adj.
14128:■drug-  A
14132:Abteil,  «u  ''drug-,  S  268. 10,  2/j,  IF.  13.  130. —  Vgl.  drujaHl-,  —  mp.  dn-and.  —  Pö. :  drvand. Sq.:  durgaii,  durgalimän.  —  0  Mit  ähn- lichem Gegcnlatz  wie  lu  i.  —  >)  VgL  doli- yhil  yäi  läilärö  drtgTiantö  Y,  46.  1,  femer  zu 'ioDay-,  bhtdva-,  *Ft>hma:  —  3)  Vgl.  Y.  45.  I , 45,  3  ijiacid  drigvt)  und  in  iarafan-,  iiiig-.  — *)  S  a68.  57.  Gani  wertlos  iit  die  Var.  dn/qAyä/, die  NA.  lu  Yt.  r.  iq  aufgenommen  hat.  — S)  Pü.  hat  den  Plural  drvnndän,  ausier  Y.  /o. 16,  wo/o  ÄiJi/reanrf.  —  6)Diemask.  (neutr.) Form  statt  der  fem.,  S  ?Z9.  I,  ^/J.  S.  noch Nu  7,  —  7>  Mask.  (neutr.)  Fonn  -  s.  N0.6  - nach  der  d-Dekl.    Nicht  recht  sicher,  5.  Var.
14154:•  }.,  g.  'drug-  C,  nur  Sing.  'Lüge,  Trug": at  yas  daivä  . .  akäi  (Sp.  45  m.)  mana»hB sta  a'imm  .  .  'üjasca  fiairimirt/iis'H  Y. 72.  3.        A)  insbes.  als  dogmalischer  Term.
14157:drug-  A  I
20541:•  j.  miÖTÖ-drug-  Adj.  'den  Mf^ra  be- lügend, betrügend',  auch  sva.  'den  Vertrag brechend'"':  msrsncaiU  vTspqm  dai^kaom mairyS  'druxs  Yt/o.  a;  19;  —  VtspsAu paiti  barszähu  .  .  spass  änAaire  mikraAe ''  drujim  *AispS.S3mna  Yt.  10. 45;  — pdhS. . yim  wnii  'ärup (SP.)  Yt.  10.4$;  i8,  80;  — aspacilySi  *drujam  vazyqstra  (sd.)  bavaintt Yt.  JO.  20;  —  mihrS  .  .  tiaram  'drujqm apqlgavS  dar)zayeiH  Yt/0.48;  —  mi^rtm .  .yö  nöit  kaAmäi  'drujqm  maiyänqm  aojö da\siti  n5il  zävar»  Yt/O.öz;  62,  23,  26, 37%  38.  73,  133.  J-^- 63;  —  hamistayalca ..  mihrB.zyqmca  *'drujimca  Y.  ö';.  3;*Yt .10.82.
24121:•  j.  vi-drug-  Adj.  'gegen  die  I?ruff  ge- richtet, ihr  Feind':  Mu  druxs'  (statt  GS.) °druxs  "er  ist  der  Dru^ixnt.  der  Drug" V./P.46.
=== BRT drvant/dragvant ===
3151:•  j.  a-x§yamna-,  a-xsyamana-  Adj.  'ohn- mächtig': xlayammm  asavan^m  däyata *tnn>m'^  drvantfm  Y. Ä5;  —  ydi^a  Alm janama  xiayamnö  *'in»qm'>'>Y.6i.5;  — frJnamjtti  .  .   atfrv    maitiyus    "manö    Yt.
3559:drigvantS  maziiis  ciköitfns  anuhlscä  a»- kvascS  apay  ralx)nar)hs  vaidftn  "die ö«(fgläubigen,  die  angelegentlich  darauf bedacht  sind,  die  Hausfrauen  und  -herren um    den  Erwerb    des  Erbes    zu  bringen"
4155:—  tpm  vä  ahäm  drvantB ,  .  nUirint^ät \aastäi  'Muhe]"*  V.5.62.  4)  mit  a) asaanqm  GP.,  b)  drvatqm  GP.;  'Ort,  Auf- enthalt der  a)  Gläubigen,  b)  Ungläubigen', im  Sinn  von  3  a,  b ;  tfm  'hüm  paihyaite yim  asaonam  .  .  tarn  'hüm  paüyatte yim  drvatqm  timanhaitt^m  .  ,  V.iS.jS; 5.62,  5)  mit  timatiha-  Adj.  'der  finstere Aufenth^t,  Raum',  von  der  Hölle:  bunim -TihSus  tpmanhahe  yat  »rr/ats  daozaauhahe
6243:•  j.,  g.  aSS'van- '* :  ajäö»-,  asilun-'^  Adj. (fem.  aiacfiT-,  asäunl-'*)  I)  'der  zum  Asa hält  und  gehört';  I)  von  Menschen  'An- hänger des  Asd,  .^yiigläubig,  (Techt)gläubig, fromm';  1)  bes.  im  Gegensatz  zu  dr>gvant; drvant-  (sd.),  a)  im  gAw,:  ki  'sav3  yäts p^isäi  (sd.)  drfgvä  vä  Y.44-^3;  —  katä- rSm  'savä  va  dngvä  vä  v^nrmaili  (sd.) masyö  V.  j/.  17;  —  kat  (sd,)  'iavä  .. vSnghat  dr»gvatU)m  Y.48.2;  —  *Äai5iyS.- dralsä(sd.)  hyat  isSya  dngväitl  at*'laom rafmS  RySm  Y.  4J.  8 ;  —  kasfuscU  nä  'laum ka%2  (sd.)  atihat  isvScit  (sd.)  Aas  paraoS akS  dngväitl  Y.  47.4;  —  at  yi  aipm dngväitl . .  saslöihya  (sd.)  vä  vansaitl . .  yS 'säum  vahistg  afaaa  (sd.)  vä  , ,  Y.33. 2  f.;
6244:—  hvS  £l  dr^gvh  yS  dr>gvaiti  rahi/ts  hvö 'sat'ä  yakmäi  'savä  fryS  (sd.)  Y.46.6; zit.7/.i3;  —  ndij  nä  pourHs  (sd.)  dr?g- vats  Ryät  cixinusB  at  tSt  vtspsng  anrSng (sd.)  ^'SaonS  ääar!  Y.^j.is;  —  taicU mä  mtSrmdin  (sd.)  jystüm  ySi  *ängvafits .  .  yöi  vahistäl  ^'saonS  .  .  rär»syqn  (sd.) mananhs  Y,_j2. 11;  —  ahmät  *mainy5ul rärs^eintt  (sd.)  drsgvants  .  ,  spptttäl  nöit i>,a  *'iat>nJ  (NP.)  Y.47.4;  —  yä  da  asis (sd,)  drsgvüitl  'säunaEca  V.4J,4;  —  yqm xsnütim  ränsibyä  (sd.)  da  .  .  räsaye^hi (sd.)  dr^antwt  sävayS  -iavanam  V.5J.  9;
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
6284:—  'Zäum  ahura  mazda  Y.  16.  i  o,  Vr.  5. 3, Yt./.5,  72.1,  V.2.39,  s-39<  ''■4».  7-23- A12,  7^.41;  —  ahura  mazda  mainyS s^nista  datar»  gai^anqm  astvaiiinqm (Stverz.)  '/3um  V.  2,  i  usw.;  39  usw.;  — unter  den  Namen  des  Ah  AI.:  "sava nama  ahmt  aiavasUma  nqma  ahmt  Yt 1. 1 2.  a)  auch  Kar'  i^.  (ohne  Nennung des  Namens);  im  Gegensatz  zu  drvant- (sd.  II  2  a  a):  °saono  ahmt  drvatS  nsii  ahmt Y.  10.16;  —  sonst:  *eyum  na  °saonS xsnaohnm  (sd,)  H.  7.  5;  —  s.  noch KompA.  aa)  GS.  mit  stay-  (sd.,  auch fdSt.),  iraOegensatz  zu  drvant—.  o^a^rimca .  .  'saonB  stöis  . .  duzä^r^mca  .  .  drvatö slöHY.  8. 8 ;  52. 4;  —  sonst :  hatkyävarfz^m . .  'säend  stim  G.  _j.  7 ;  Vr.  18.  \\  —  anayra -saons  siis  Yt.  Ä  48;  *V.  2.  19  PüZ., usw.  3)  von  allem,  was  sonst  zur ö.4ansclicn  Welt,  zum  Reich  des  Asa  ge- hört, auch  sva.  'Jieilig';  im  }Av/.  (s.  auch  2) :
9019:•  }.,  g.  kat  Adv.,  an  der  Spitze  des  Satzes; i)  'wann';  -4'  tä  nara  irista  ..nasus  upa.- dvqsaitii  . .  isar>  pasca  parairistim  V,  -j, \l.  2)  als  Fragepart. 'obwohl?,  num?': if=''  asavä  inazdä  vSng/iat  drjgvanim» "wird  der  .,^/aanhänger,  o  M.,  den  Drug- genossen  überwinden?'  Y.  ^iV.  2 ;  —  h asava  .  .  ranat  dnantjmf  asava  vana[ drvantjm  Yty.  28;  —  kat  möi  un-ä  isi (sd.)  caAyil  avauhS  "ob  (wohl)  .  .*'  Y.  50. i;  —  alä  k'  ^wä  darssäiij  i!S&?i  Y.  J<V,5;
9730:—  "Alf  vJsph  ä  xsa>rsi  *yä  ..  ^raasiä'  vTmij(sd.)  katarascit  *parayat  N.  5;5";  — (sd.)  Y.^4.^.  A)  Plur,  und  Sing,  mit  al^S  ''ianam'''' *iris'ifiü»am  ra^s'^{sd.)  N, 2 ; vispa-  Adj.  von  der  Gesammtheit  derl  —  agta paräyaiti (sd.) yaia '^afys^'^A^iii stoflflichen  Lebewesen  'Welt,  Menschheit"  N. 2;  —  myazdava..amyasdavan9tn..yiU)m (vgl.  anhav-  Sp.  io7f,);  y<^a  °^3kva  {%d.)  "'kanqm  frap>r>naoiti  A.j.  11"*;  V. i'fljö^.Äjiiir?/ra(^a>-äne"dassichunabhängig|  19,29,  F,4f-; — /radahüi  'Ibanam  kava- unter  den  Wesen  einhergehe"  Y.9.  17;  —  M^häi  asavastanam  Y.  6S.  4(?);  —  yai aAümca  (sd.)  ratümca  '^anam  Vi.  I0.i}3,'.^avani  aiwi.vanyä  taiiryavantim  ..  ahmt 13. g2;  91;  —  ratu>wim  °%anqm  Yt  /o. ,  (sd-,  Sp,  4)  '"ke  (LS.)"'  ptlanahu  Yt  5. 92;  —  aat  .  .  mraom  .  .  az^m  yö  akurs\  109;  73, 113;  —  ka%S  ayärS  .  .  fprasayäi masda  .  .  yima  .  .  mS  Oi  fniciaya  .  .  mi'  (sd.)  lÄril  ai^T  '^wäAa  '^ahß  tariusiÖl  Y. °'ia  varihaya  ..  mg  vXsäi 'i:anqm  %rätSca'.43-T',  — yS  nS  ainrianqm  (sd.)  irJri- Aarpläca  .  .  V.  2.  4;  5^;  —  aiim  daA3A?m ;  xsäite  °%anam  (als  Obj.)''  .  .  tanunqm  Y. .  .  a^im  *'hsvays  (DP.)  '*  drvant3m  Y.  (J.  ö'j.  7 ;  —  ahmäi  ntmauhs  ävaidayamaidt 8;  —  cim  .  .  qsitm  tsattt  .  .  "'"itä/tz-ö'^  I  '^Sscä  tamiaslä  Y.  jÄ  2;  —  vJspa  °'i:Ssca mahrkaum  Aog.  48;  —  us  *täcil  v.'krka  tanvasca  asdibista  uStänqsca  kihrpasca  . ,
10826:und  bfisem  Reden  euch,  die  Dalva,  was er  den  ZVi^fgenossen "  gelehrt  hat,   um (den  Menschen)  zu  verderben"  Y._j2.s. Za  ü.  V.  i^naA' 'er  Tcrnichtet',  gr.^SiV»;  vgl. *S^;  Bthl.  ZDMC.  50.  711,  —  Pü,!    tt/rär SSel  i  ciSn  Ah  hai  H  i  drvand pätixiähih  "der sie   lehrt,   die  Herrschaft   stsmmc  von   dem I>r".  —   >)  Der  Irrlehrer,   Ton  dem  auch  Y. 32.  6   die  Rede  ist;    s.  noch  No.  2.     Dafür, dass  das  erste  Sabjekt  nicht  ausdrQcklich  be- zeichnet ist,  vgl.  Sp.  5<36  0.  und  die  RV.-Slellen g]-häm  indraica  gacehatam,  a  yäd  ruhava  vänt- nasea  navam  (n.  a. ;  *.  Hask£i,L  JAOS.  ii.  66), die  insofern  der  obigen  ähneln.  —  ')  E»  ist ein  bestimmter,  der  neuen  Lehre  feindlicher Fürst  gemeint;  vgl.  drigvant-  I  a  a  0. j.  xsavaiditn  Vd.  p:  s.  xit/id-  mit  Na.  4. j.  xlm/as:  lies  xivaS.
11033:yat  asti  airyanqm  daRyunqm  .  .  yatc'a asaons  zaraiuslrahe  ". .  quod  est  .  .  pro- vinciarum  .  .  quodque  (sva.  et)  . ."  YL/p. 56 ;  —  vupe  matnyava  dagva  yaloa  vannya Yt.  Jo.  97;  — y5i  vatjAsus  3  wanatahs iyHntJ  yasca  üitx  Y.Jp.  3;  —  hyat  da xyüo^anä  mJzdavqnisA.)  yä^ä  uxha  ",.fa- cinora  . .  quaequc  (sva.  et)  verba"  Y.  43. S  i  —  *gr}AmS  .  .  avAsuf  tnaraxtarS  ahya yai^a  "GrsAmas  ,.  vitae  deslructores  huius quique  (sunt)",  sva.  "Gr.  et..destnictores" Y._j2. 13; — yeTiyaaUSp.  5730.)  hsrnsmya- sattl(sd.)  mt^ahyä  yäca  hsi  ansua  Y.33. i;  —  yi  iluds  dadsniE  da%ranqm  (sd.) haüa  alätinö  y^siä  .  ,  *drigvü.d3byB  "quae debita  poscanlur..a  hdeti  (quaeque  sva.) et  ab  infidelibus"  Y.31.  14;  —  mainyus spSniStS  .  .  yaecä  xsnao/in  (sd.)  aAurjm "Spiritus  sanctissimus  . .  et  (ii)  qui  satis- faciant  . ."  Y.30.  5;  —  ya  ..  väV)r)zli .  .  yala  vaniaitl  Y.  2g.  4;  —  ya  atirayl .,  urBpayeintX  yäca  xrafä  ..  Y.4S.10; 44-  20; — y7  va  möi  na.,  dayat  ..  yqsca haxiäi  (sd.)  "qui  .  .  vir  , .  faciat . .  et  (ii) quos  .  ."  Y.  4ß.  10;  —  at  ta  vaxiya  .  .ya mazda^a  (sd.) .  ,  humqzdra  (sd.)  als  yeca ya  raocSbis  dansata  urväza  "ea  praedi- cabo  . .  quae  (sunt)  recordanda  .  „  a  bene recordante  una  cum  Asä  quaeque,  quae una  cum  luce  videatur  voluptas"  sva,  "et voluptatem  quae  .  ."  Y.^.  i;  —  zu  c: at  yül  dasva  .  .  yasca  vh  .  .  yazaitl  Y. J2.3;  —  ta  vS  mazda  ..  asäi yecä  tatbyaca'''' ärmaitl  ddi^a  insi  istsisi&A.  mit  No.  2)  xsa- %r>m  Y.$i.2.  o)durcheinenKonjunk- tionssatzmit>'<j^j  oder  Ayat,  dem  ^a  folgt; nur  gAw. :  datd?  galmcä  ajyaitimcä  (beide als  I.Glied;  Sp.567  \x^ya%aca  anhat  aps- m^m {sd.)..  Y.30. 4;  — ia'^a  ,.  zar^m (sd.) ..  carani  *ashiitm  (sd.)  xsmakqm  hyatca mSi  hyäi  Vax!  aslS  Y.  44.  17;  —  hyat vJsSnta  (sd.)  dr>gvant>m  avS  AyaÜa  gäui jaidyai  taraol  Y.32. 14.  e)  das  erste Glied  ist  relativisch  gegeben;  nur  gAw. :  yJ *u>i'qfi?m  mS'i  gairü  (sd.)  . .  dadi  asisca '  Syadiananqm  vidus  V.  28.  4.  f)  das erste  Glied  ist  nicht  ausdrücklich  genannt, vielmehr  aus  dem  Zusammenhang  zu  ergän- zen (s.  Sp,  571  u);  nur  gAw.:  ta  uxiiä  . . maeda  asaica  yufmaibya  gtml ". .  (dir),  o J/., unddem.<4j'ii.."Y.^2.9;  — /ö  d)b>naotä
11059:—  vanhSus  *mainySus  Syao^anahya  uxba- Ttyacä  Y.  45. 8 ;  —  pt^xifighim  alt5.kanwt Aumayak>m  daR/ayasmm  drvantsm^a  arp- /al.asp?m  Yt5.ii3  (s.  dagegen  109;  Sp.
11069:p>san?mca  dali-ayasium  drvantimca  anjal.- .rj/iiM  Yt.5.i09(s.  dagegen  113;  Sp.S7om.); —  aktmahe  vaityehe  asaya  frasrlUahe  hä- vanay^sca  asaya  frasalayh  arsuxr,anamc<l valam  Y.  27.  7;  —  ptans  voka  urunascä aiäunam    tumascä   Y.  4^9.  10.  b)  sie
11732:tai  asti  . .  amavastsmgm,  tat^  . .  Yt  /.  3  f.,  ]  *vä  akäm  drtgvants  .  .  dalnS  nalfqi  (sd.) 72. 2*,  H.  2. 18',  36';  —  *vanaite  ak)mal\,  31.20;   verwendet  V.^,63.  b)    ini
11966:•  j.  tanu.drug-  Adj.  'des  Leib  mit  der Dr.  verbunden,  der  mit  ihr  eins  geworden ist''>:  vUpe  drvants  'drujS{^V.) yS  adtrits.- ikalsß  (sd.)  V.  76.  18.
12463:—  'va  Aqm.rae'iui/iyati  (sd.)  Y.ig.20;  — 'va  drvantB  duldanhs  V.  ig.  3,  aS,  44— 47*;  —  'vanqm  da?u9.tim>m  Vtj.  14";  — kS  'vanqm  xawt5  (sd.)  ks  'vanam  xumbö ks  'vanqm  ia.nairls  iB  havqs{sA.)  'vS  in vispö  'vS  kö  para  m^ntö  'vS  k3  pasca m>r)tS  mainyava  'va  /raba7iainlH . .  aria:-a vjptö  ariaca  va^ayS  (sd.)  V.Äsif.;  32'; — ■  'vanqm  rapaks  V.  7.  56;  —  vi  'väiS ayais  *avat>hTs  anantail  aks.dabli  sarvm mruyl  hatqm  draojistais  . .  vT  'vais  vi daFvavatbls  Y.12.4;  6';  —  staoml  ahm ..  näismiisd.)  'vtriAP.")  W.  11.  ig— 12. 1; Yt.  7^.  89;  —  us»M^lala  masyäka  staeta ahm  . .  nTsta  (sd.)  'va  \.  18.16;  —  'va apa.dvaraia  Ytj.  7;  —  vil  apqm  ^a patmtu  vT  'väahs  vT  'vaysil  (NPf.)  Y. 70. 1 ;  —  paitistätSe  t>masciiiranqm  'z-anqm Ytö'.4;  y.  137;  —  duSmainyam  sisdyd 'vqn  apa  "asavqn(sd.)  Yt/p.84; — yaha azpm  uzbanini  hala  'vaHbyB  uyl  lüil'a saokaca..  Ytj.  26;  Jp.  23;  —  AS  (oämL
12470:—  sraohm  ..yd..yBityeiti..Aata  'vaeibys Y-57-IT, — paiti-pirme  vannya  'z/fffAP."') V.  70. 14;  —  yat  baväni  aiwi.vanyä  vTspe •va  Ytp.  4,  /5.2g;  —  imi  alte  vaca  yoi fanti  vjspanam  'vanqm  snahim  V.io. 16;  16,  Y.27.1',  Y.ig.46';  —  snaihi/.. hvS.vafjim  kam^rihe  patti  "vanqm  Y.  57. 31;  31,  YtÖ-s,  jo.aß,  129,  V.79.15;  — pas^a  jainti  'vanqm  . .  fravaxaiU  mihrS Yt  70. 133;  3. 10,' 4-  2,  5-  2^.  V.J.  32;  — hasat^rayna  paiä./asaiit  aiars  .  .  'vanam mainyavanqm  ..  drvatam  Y.S.So;  Y.io. 6,  YL  13. 4S;  —  asfi»  ,  .  taurvayeintim vTspä  tbalsa  'vanqm  maSyänqmca  Y.52. if.;  5.18,  Yl/.i',  S,  6;  —yat  mqm nalcis  taurcayät  nsit  °vS  na^a  masyS  nöii yäiaz'B »a^a pairikä  YtJ.6;  J5.56,2.n(?); — paitiltätse  'vaheca  tbaiiatahs  ma^eheca Y.6S.S;  5S.3,  VLy.'"i42;  ~y8..ä>,r)m urvaaayata  °väatia  haotäti^A.)  mafyäatca Vt  13.  89;  —  'vanqm  parö  draomBku  Yt. ^3-57!  57-  S.  noch  Y.J5.  2  (Sp.  667 u.).  a)  klassifizirt:  mürym  . .  yahmal haca  frabr^SMii  vTspe  mainyava  (Stverz.) •va  yaica  varsnya  (Stverz.)  drvants  Yl /o.  97;  usw.;  —  paiti^tätJe  mäzanyanqm (Stverz.)  'vanam  varmyanqmca  Yt.  13,1  ^T, usw.  b)  namentlich  bezeichnet:  °vö  ao^O V. /j.  i;  —  akataam  dasum'^'^  V. 79.43  (statt  Nom.);  —  °vasca  yS  apaoSs \X.8.ii;  XI,  22,  28  (daiam^'i),  18.2,  6;  — inärS  °vS  V,  ig.  43;  —  kasvjS  'vS  V.  ig. 43;  —  daium  kund»n  V,  75.41;  —  daiwil 'vS  V.  79. 43;  —  driieis  °vS  V.  iq.  43 bßiti  'vS  Y.ig.  i,  2,  43;  —  paitisJ  °vS 'Z'onqm  da!v3JfmS  V,  7^,43;  — "^jm  dalum  V./0.9;  75.43; —  vätJm  'vö (statt  Akk.)  V.  70. 14;  —  vTzansd  °vS nama  .  .  urvän^m  bast>m  vataydti  V.  ig. 39;  —  saouru  'vS  V.  7_9. 43;  —  ar^rff mainyus   .  .  'vanqm  'vs  Y.ig.  1,  43;  44;
12483:•  j.  daeva-yasna-  Adj.  'der  die  Dalva verehrt,  anbetet';  überhaupt  'ungläubig"*: ye^he  .  .  näirika  avayi  xfudrä  Aqm.- rafktoayeiti  mazdayasnanqm  'nanqmca N.  77'';  ~  kalärö  paurvB  ämayante  (sd.) maidayasna/ibyB  va  'nalibyB  vä  V.  7.  36; 37;  —  drvafäB  'naahdYt.  5.  94;  —  huma- yak»m  'n>m  drvanttmca  ..Y\..^.\\y,  109, 5.37;  —  drvatam  'nanqm  Y.ig.  26,41, Yt5.68,  ;;.  4,6;'  —  dusmainys .'. 'n^iAP.) A.  7,  11;  —  daffnqm  'nanam  Y,  72. 1 1 ;  —
12798:Nur  Med.  'sprechen,  sagen,  reden'; i)  mit  Aklc  des  Gesagten:  dalva  drvants .,    ayqm    äaci%rfm    däunta'^    V, /(j.  45;
13174:dasti'°'^  N.  WS;  lOj,';  —  töi  xi  rf,7/<i(NP.) AamaSslärö [f.A.)  ^aSsimahyä  V.^Ä  i2;Yt. //.  15;  —  vav/iid  haoms  hmats  ..*a~ ästS  vaishus  dato  baisasyS  Y.  r/.  16; tat  viriiitim  dad?maidi  kyat  mmS  Y,  jÄ i; — yai  *iri'^äHahe  asaonS  sat^m  da^iliti un'ifram  P.J5;  24  C^a^aili)^^; j/amitfm  a/ai-an^m  dayata{2V.)*axsyaMii>m drvant^m  Y.Ä  5;  —  hyat  ^ws  x/ayas(sd.) alsjm  dyäj  Smmiantsm  y.43-  lo;  — yascä dii^Jtfg  (sd.)  dngvaf}  dadäl  Y.j2, di'iidl  . .  västrySng  . .  aAmä.rafina»/tS  (sd.) V,  40.  3;  —  AumSlm  %wä  . .  dad^maidl Y.  41.  3;  _?5.  9,  Vr.  12.  4;  —  nöit  tarn idravB.fuirJm  {^A.)  .  .doste' '''  Y.10.15J V-  '5-9:  —  y'^  •  ■  häiriM  kuzämitS  da- 'Hliti  Y.  6^.  2 ;  —  ratus  . .  ratunann  ayas- nlm  (sd.)  daste  A.  j.  7 ;  8, 9 ;  —  az3m  ddöqm ..  tistrjm  ..  av5nt>m  (sd.)  yesnyala  ..y^i ti  .  .  HSit  daiayqm  .  .  tisirlm  .  .  avSiitim yesnyata  YtÄ  50-52;  10.  \;  —  spämm da'i»mi^  ..  Avävastnm  V.;j,39; — /lyal dA  (aS.)  iyaoiann  miidavqn  (sd.)  Y.  43. 5;  —  yJ  däl  manS  vakyB  ,  .  aSyascä  (sd.) Y.  ^.  4;  —  a%3tn  daiqm  asö  rämSJäitlm (sd.)  .  .  yahi  sl  .  .  nSit  daiiyqm  .  .  asS ramUJäiim  V.  ;.  i;  Yt /p.  94;  —  tum  .. nmärum  äaiiähi  b?mimitfm  Yt  10.  30;  30;
```


## [2026-09-05T20:09:11.894Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD drō ===\"; grep -n \"dro[zγg]\\|drōz\\|drō\\b\\|druwand\\|druvand\\|drwand\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== KNT duruj/drauga ===\"; grep -n \"duruj\\|drauga\\|draug\\|drujana\\|duruxta\" KNT.txt | head -30",
 "description": "Grep MacKenzie and Kent"
}
```


### [2026-09-05T20:09:11.962Z] TOOL RESULT

```
=== PHD drō ===
PHD.txt:316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
PHD.txt:1815:evil (a.) akēmand, апар, druwand, wad(ag), wattar, duš-; ~ deed dušxwaršt; ~ eye aš, dujdoys?rih; ~ rule dušpādixšāyīh; ~ ruler dušpādixšā(y); — speech dušēwāz- ih, dušhüxt; — spirit Ahreman, gannág mēnēg; ~ thought duš(hu)- mat; of ~ behaviour duškunišn; of — religion agdén, dujdén; of — speech duš-gēwišn; of — thought dušmenišn.
PHD.txt:3665:sinful abàtón, bazakkar, druwand.
PHD.txt:4742:padyabib, ALI 00 t€» о) pādāšn VA My o padirán- ` - My yey a pādīrānēn- -p ry yey a pādīrānēnīdan W3 y ry We pādīrānīdan WS wy veyo pādīrān wey yey os paymar Ne теу o pādēz 23 voy o lpādan Y rero) pādofrāh ау\һе» 0) padzahr NS ve» o» pāygūs ISYA padrozag 15 cP rere pāyram » rey’ о
PHD.txt:5370:darridan m К ey grēh PV drahnāy p" m druxtan wey da grawih җә уў» dro, 1-2ргам у» drang E » druwand 2 iD druwandih ҷу» >
PHD_mackenzie.txt:2081:droz-,v. druxtan.
PHD_mackenzie.txt:2082:drozan [dlwcn l 1M, J drwzn] lying, liar.
PHD_mackenzie.txt:2095:druwand [dlwnd 1M drwnd] evil, sinful, unrighteous.
PHD_mackenzie.txt:2097:druxtan, droz- [dlwhtn , dltvc- I M drwxt, drwz-] lie, deceive.
PHD_mackenzie.txt:3564:mihr-droz [mtr/d/we] = mihrodruJ.
PHD_mackenzie.txt:6239:confession astawanih, xwastiigih j           contract-breaker mihrdroz, mihro-
PHD_mackenzie.txt:6521:evil (a.) akomand, anag, druwand,                  extinguish afsardan.
PHD_mackenzie.txt:6545:excellence pAhlomih.                               falsehood drozanih, mihoxt.
PHD_mackenzie.txt:6557:exit uzenag.                                       fasting padrozag.
PHD_mackenzie.txt:6965:lark cakok.                               liar drozan.
PHD_mackenzie.txt:7000:lineage gohr(ag).                        lying drozan; (prostrate) nibem.
PHD_mackenzie.txt:7595:sinful abiiron, bazakkar, druwand.            smiter zadiir.
PHD_mackenzie.txt:8825:peraman                ,,~4)                   padrozag                   \1c;'}~QJ
PHD_mackenzie.txt:9097:Inihrdroz              ~~ ,'te.G                mehtar                  \\'U1>6
PHD_mackenzie.txt:10531:druwand                   ... \~   gramag
PHD_mackenzie.txt:10533:druwandih               ~\~        drayidan, grayidan      \,~
=== KNT duruj/drauga ===
987:*dhroughos, OP drauga ‘Lie’, Av. draoyó, Skt. drógha-s.
1074:With Skt. d from pIE dh by Grassmann's Law (§73.IV): pIE *dhrugh-je- in OP adurujiya ‘he lied’, Skt.
1076:*dhrougho- in OP drauga- ‘Lie’, Skt. dróha-
1276:OP bajim ‘tribute’. pIE *dhrougho-, OP drauga ‘the Lie, and with
1278:Lie’; adurujiya ‘he lied’, denommative verb
1324:But pIE -gh-to-, becoming -gdho-, plr. -gda-, was in OP replaced by -kt- (analogical to -gt- becoming -kt-): duruxiam ‘false’, pte. to pres. stem durujiya-, cf. drauga- ‘the Lie’ (palataliza- tion only in the present stem, where there is the suffix -jo-).
1339:TpóTEpov. pIE root *dhreugh- in OP drauga- ‘the Lie’, Skt.
1402:‘death’, cf. -30- in OP martiya ‘man’. adurujiya ‘he lied’, cf. drauga ‘the Lie’. asiyava ‘he went forth’, Skt. (mid.) deyavala.
1521:*dhroujh- in drauga ‘Lie’, *dhrugh- m duruxiam ‘false’.
1595:$128. Anapryxis is the development of a vowel between two consonants which the speaker finds it difficult to pronounce without an inter- vening vowel; cf. the common pronunciation of athletic as athaletic. OP has anaptyxis in the cluster dr when it is followed by u: duruva ‘firm’, Skt. dhruvá-s; duruxiam ‘false’, Skt. drudham; adurujiya ‘he lied’, cf. Av. acc. drujim ‘devil’. The only other cluster which suffered anaptyxis in OP was gd, which we find in the name of Sogdiana in its various writings: s'ug"ud" Suguda, ші = Sug'da, but also вирі = Sugda, so that here the pronunciation was a shifting one.
1596:There is a possibility that there was anaptyxis in the clusters dr br fr zr before a, but OP writ- ing can give no evidence on this point. NPers. has duróy = OP drauga, birddér = OP таа, jarmén = framünà; but the anaptyxis may be later than the OP period. For Zra*ka, Greek has Zapayya: (in Arrian) and Zapéyya (in Herodotus) with anaptyxis, but Greek has no initial sr- or zr-, and there is also the form Араүү:ауһ (in Diodorus) without anaptyxis, when the initial cluster is one which is normal in
1633:(1) Neg. a- before consonants, an- before vowels, from *n-; prefix ha- and ham- similarly (= Skt. sa- and sam-). Root final before dental suffixes: pIE gh and gh-t > gdh, replaced by the product of gt in OP: adurujiya and duruxiam (878.11, $242). pIE dh and dh-| > dedh, re- placed by the product of fst in OP: ba*daka and basta (§85, §242). |
1634:(2) pAr. palatalization of velars before palatal vowels, giving an alternation in OP k/c, g/j ($78.11): Maka Maciyà, kunautiy kartam car- lanaiy, kašciy cisci, drauga draujana adurujiya, pard-gmala ha"gmalà à-jamiyü.
1636:(3) plr. change of p tk to f 0 x before con- sonants ($74.D): рага but fra-, aparsam but -frastam, tuvam but ace. ийт, akariya but cazriyü, drauga adurujiya but duructam.
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1785:Agents: baga- ‘dispenser, god’; drauga- ‘deceiver, the Lie’; arSti-bara- ‘spear-bearer’; züra-kara- ‘evil-doer’; dáraniya-kara- ‘gold-worker, gold- smith’,
2027:Nom. Sg. martiya, х$йуабтуа, Ката, baga, drauga, hamiciya, атиќа; man’s name, Kabijiya; place names and ethnics Раза, Майа, Sugda Suguda, Saka, Sparda, Mudréya, Uja боја, Yauna, Parðava, Armina, Arminiya, Asagaria, Gadāra, Márgava, Uyjiya.
2030:АЫ. Sg. draugd; Kabujiyā, Parsü, Suguda,
2481:pIE *dhreugh-: pAr. *drughia- in Skt. drühyati the E deceives’, OP imf. adurujtya', pl. adurujiyasa*, E :
2526:OP drauji-ya- ‘regard as a lie’ in 2d sg. subj. Idrau|jiyühy, to drauga- ‘the Lie’, with change of the final stem vowel to ? before the suffix; ef. Whitney, Skt. Gram. §1059d.
2528:I. The Sigmatic Aorist is seen in niy-aparsam ‘I inscribed’ (or -apiSam?)}, to root pai8-, pIE *peik-; in mid. adarSiy ‘I held’, to root dar-, pIE *dher-; perhaps in pass. -asahya in frasah[ya]. The aorist endings 3d sg. -s-t, pl. -s-nf, may also be respon- sible for the endings of @1$ -diSa" to root ay- (8208); akunaus akunavasa to kar-; adurujiyasa to durujiya-; abaraha to bar-.
2570:II. The secondary ending is -t, which is not written in OP final after & (840); before - the thematic vowel is -e-: pIK *ebheuet, Skt. dbhavat, OP abava; pIE *ebheret, Gk. &фєре, Skt. dbharat, OP abara; Skt. ddruhyat, OP adurujiya; Skt. ddhd- rayat, OP adáraya; viyamarda; unaugmented ava- harida]; etc. Injunctive @adaya. Remodeled non- thematic, dha‘ ‘was’. Passive, abariya, adariya, etc. (§220). Non-thematic: adānā' to z5nà-, adada to 'dá-, айта to *di-, viy-aka" to kan-, avàja" to ava-jan-; in the last two, radical n as well as end- ing é is not represented in the OP orthography. Strong aorist: pIE *edhél, Skt. ddhat, OP ada. Optatives: Skt. gamydi, OP a-jamiya; OP avā- janiyà, Муй, pert. caxriyd.
2584:III. The sigmatic aorist similarly remodeled its 3d pl. from -sat (< -s-nt) to -san(t); thus in ОК, s-aorist €\vo-av ‘they loosed’, whence strong aorist &o-cay ‘they gave’, and (late Greek) thematic éhaBo-cav ‘they took’. So also in OP, the -san j spread to some verhs,! being regularly -ha^ after a _ and -ša” after 1: abaraha^ alongside abara”, patiy- dia", opt. pass. yadiyaisa*, and with extension of — -ša” to the position after a, adurujtyasa", akuna- vasa” alongside akunava*.
2626:druxt6, OP duruxtam. pIE *bhendh-: pte. *bhndh-to- > *bhndzdho-
2702:A. Expressing place where, without a preposi- tion, as in DB 1.34f pasdva drauga dahyauvā vasiy abava щй Parsaty ша Madaty ша aniyãwā dah- yusued ‘afterwards the Lie waxed great in the country, both in Persia and in Media and in the other provinces’; DB 2.75 duvarayãmaiy basta аййттуа ‘he was held bound at my palace en-
2760:67. ApPosrTIVES occur in the following cases; lack of examples in the other cases is accidental: nom. DB 1.1, 1.53, and almost everywhere; ace. DB 1.54, DPd 2, DNb 4, etc.; gen. DB 3.59, DPd 9-11, XPe 14, etc.; loc. infrequent, DB 1.34f. More often the appositive, if more than а single word or if to an oblique ease, is expressed by an anacoluthie nominative phrase, followed by a resumptive pronoun or adverb ($314a; 8312). Partial appositives occur as in DB 1.34f pasdva drauga dahyawd vasiy аата щй Parsaiy ша Mädaiy utü aniyãwā dahyušuvā ‘afterward the Lie became great in the country, both in Persia and in Media and in other provinces’; also DB 1.401, 1.48f, DSf 25f ikä avaniya aniyā XL ara- Santis baránà ата X X атаќаті bar snd ‘the rubble
2812:§26b. THe DEMONSTRATIVE NSM.-NSF. туйт ‘this’, with its suppletions (§199), is likewise either pronoun or adjective, mainly of the following types: tyam Pàrsa ‘this is the Persian’ (DN I), hya imam tacaram akunaus ‘who built this palace’ (DPa 5f) zšāyaðiya ahyayd bimiyd vazrakayd ‘king in this great earth’ (DNa 110). It is а pro- noun with rather distant reference in tya imaty kàram adurujwasa ‘so that these deceived the people’ (DB 4.34f), where zmazy refers to the rebel pretenders listed in DB 4.7-30.
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
3489:38 уй : XIV : тапса : Sakata : dha : yadiy : udapatatà ; hauv : kérahya : avaflü 39 : adurujiya : adam : Bardiya : amiy : һуа : Kürau$ : puça : Kabijiyahya : br
3529:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 79 uk"dracara : amiy : hya : Nabunaitahy& : риса : pasava : kära : һуа : Babiruviya 80 : hamva : ably : avam : Naditabairam : aSiyava : Babirus : hamigiya : abava : x
```


## [2026-09-05T20:09:21.030Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('total leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'drauga-' in p and ('duruj' in p) and i>190:\n        print('LEAF',i)\n        print(p[:2500])\n        print('---')\nEOF",
 "description": "Find Kent lexicon entry for drauga/duruj"
}
```


### [2026-09-05T20:09:22.766Z] TOOL RESULT

```
total leaves 232
LEAF 215
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted by Tm. Lex. 102), ef. OP duviliyam ‘a second time’, Skt. 0015 ‘twice’, Lt. bis, + paranam ‘before, previ- ously’ (Tm. 1.е., and Vdt. Stud. 1.8). This is better than Tm.’s "long aforetime', adv. duvità ong’, GAv. дайа, Skt. dvità (cf. OP duvaistam), + paranam (as above); also than KT's duvità- parnam ‘in two lines’, contaming the cognate of Skt. parnd- ‘wing’ (supported by Wb. ZDMG 61.724-5, KIA 10-1, and by Hz. AMI 1.112n). DB1.10; DBa 17.
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also du
---
```


## [2026-09-05T20:09:39.579Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB drog/druwand ===\"; grep -n \"drōg\\|drōž\\|drōz\\|druwand\\|drwand\\|drug\\b\" NYB_vol2_glossary.txt | head -25\necho \"=== HRN durogh ===\"; grep -n -i \"durōġ\\|duroġ\\|durōgh\\|durog\\|drōġ\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"durōġ\\|duroġ\\|drug\\|draoga\" HUB.txt | head -20",
 "description": "Grep Nyberg, Horn, Hübschmann"
}
```


### [2026-09-05T20:09:39.648Z] TOOL RESULT

```
=== NYB drog/druwand ===
1201:därök [d'Iwk] medicine, drug 90". — MPrthPrs @rwg; Paz. NP dari, Skr. v. ausadha.
1361:druvand [dlwnd] wicked, evil, of Ahriman 642-7 and passim; of human beings 10°. 3414, 6625, 964. 10711 — subst. 7213, 7417, pl. eas. obl. —-än 461, 5313, 7220, 7421, 75°. 10226, 10322, used as cas. rect. 10114-18, — Av. (774 sqq.) dragvant-, drvant- ‘be- longing to the drug' (v. druž); MPrs drwnd (S, A-H II); Paz. daruand, dar- vand.
1369:druž [dlwc'] all that is false, untrue, wrong, deceptive: 1. the world of Guile and Untruth, conceived as a personal cosmic power, 3822, 9313. — 2. individual manifestations of this power, demons, conceived as feminine supernatural be- ings: sg. 5716-25, 583. 9620-24, 9817-19, 101% (voc.). 1023-14; ~ ; anāštēh 671; ^ 4 spazgeh 6811-12; ~ 7 ahramög 10124-25; pl. cas. rect. ~ 648. 65*. 9721, 9819 (of human beings). 10224-27, 1033; pl cas. obl. —-än in the set phrase devün u ~-dn 75" ete. (voc. 9027). V. also mthr-druz, mihrčin-druž. — Av. (778 sqq.) drug-, nom. druxš, gen. drüjö; MPrs drwaš (S); Paz. drü£.
2565:traitor 99.9.12, — Av. (1186) midrö.drug-,.
2785:8 [L, ^'w'; KN] či [LH; LH-y 104; ‘L-y 34%, 528-19] prep. to, with vbs. of motion; temporal: until; the sign of the indir. obj. (2277-5 perhaps the sign of the dir. obj. according to Prth. usage); — combined with other prepositions: andar 6, tài 6, or with an adv.: bē 6, fräc o, nazd 6; — governing a subst. or an adv. and forming with them compound pre- positions and adverbs: 6 berön, 6 nazdik, O pasth, 6 patirak, o peš (frac 6 peš, andar 6 peš); in a frame prep.: 6... rón; v. these ws.; — prev.: 6 druž früc mat the drug came to the place 5715-16; jn this case the ideogr. KN is common: 348 twice. 6521, 9422. — The form LH = 67 as a prep. 1612. 4210, 4424-25, 5617, — 6 cannot govern an encl. pron.; if such a pron. is affixed to the prep. it always belongs to the governed subst.: 6-š zäyısn until his birth 44!2; frāc ör-Sän deh vénam I foresee for their country 504; — in certain cases 6 is replaced by the adv. avis (g. v.). — Represents both Av. (163) ava, OP ava, and Av. (180 sqq.) avi, ao; MPrthPrs ’w; Paz. ó. The ideogr. KN originally rep- resented MIr (MPrthPrs) 6h < Av. (171 sq.) avada, OP avadä ‘thus’; in BP, having lost its final -%, it is used as 6, but chiefly
5137:drug-, druxš, drüjo: druž
=== HRN durogh ===
=== HUB ===
10845:V. DRUGKFEHLERVERZEICHNISS.
```


## [2026-09-05T20:09:41.500Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 دروغ ===\"; grep -n \"دروغ\" BQT_v2_pages.txt | head -20\necho \"=== BQT v2 دروند ===\"; grep -n \"دروند\" BQT_v2_pages.txt | head -20\necho \"=== BQT v2 درشکه ===\"; grep -n \"درشکه\\|درشك\" BQT_v2_pages.txt | head -10",
 "description": "Grep Borhan-e Qate vol2"
}
```


### [2026-09-05T20:09:41.601Z] TOOL RESULT

```
=== BQT v2 دروغ ===
440:   ‫فردوسی « جادو ‏ را غالباً بجای « دروند » پهلوی‌ویازند ودروغپرست ویبرو دبومسناآرد‬
3766:    ‫طبع ‪.‬کشت با وسم و صوبری وسطچ*اماپتاینر متتصوی ‪ -‬هیا ‪ -‬دروغ[ وکی‬
7814:                                                                 ‫‪۸‬‬    ‫و بالالحی (‪ ۷ )۳‬سنی دروغ گوی ‪۷‬‬
10630:   ‫هن احد بت‬        ‫و گفتندی‬   ‫آبرا بدروغ می‌داشتند وهر سخن اورا پاور نداشتندی‬              ‫شل مبکرد »‪ .‬ومردم‬
17868:  ‫)‪ .‬بهلری ‪ 80۳0‬م«نای ‪> ۲۷۲‬‬           ‫‪ 2‬دروغ ‪ -‬نم اول ودوم » ( تلفظ قدیم ‪0‬‬
17870:  ‫‪« ۸۷‬یبر گے ‪٩۵*.‬‏ دراوراق مالوی سهاوی ‪( 2۷۳1 -‬دروغ گفتن» فریفتن)» در پارسی باستان‬
17973:    ‫دروغ‌پرست " |زاوستا_ ‪ « 602۷۲1 - ›4 812۷89‬بارتولمه ‪ » 4۷۷۲‬پازند وپارسی ‪04۳2۷721‬‬
23612: ‫و بپترین آن سفید است » و گوبند بفایت صلب‬                ‫ودروغ است‪ - ۱‬و بك مپره از مهرهای شطرلج‬
27038:                                                         ‫سیب دروغ وخبات یکه ازو اهر شده بود اورا‬
28436:                       ‫نم اول بر وزن دروغ > | کیاهی است دوایی ‪.‬‬            ‫رروع =‬
29791:   ‫در ردیف کناهکارانی چون راهزن و دزد و جادوگر و پیمان شکن و دروغزن آورده شده‬
29793:   ‫علامت دبت) ‪ .‬مالی کهبعقيد زردشتبان بجادوبی و دروغ وفریب خود را پیغمبر خوانده ومدعی‬
35667: ‫شراب را (‪ )۲‬نکیوزنند ‪ -‬وبمعنی‌دروغ وبهتان‬        ‫ولزغرا نیز‬‫هروا آبند و رولد ‪ -‬و ج‬
35724:                                                          ‫و سخن باشد ‪ -‬و بمعنی آفانهٌ دروغ ش‬
35744:            ‫چند فروشی بمن نو اين سرو سروا‪.‬‬              ‫‪ - ۴‬چند دهی وعد دروغ همی چند ؟‬
36116:                        ‫اکر آهم دروغ باشد بعهقروبت که فرمایی سزاوارم ‪« ».‬گلتان ‪.» ۳۵‬‬
=== BQT v2 دروند ===
440:   ‫فردوسی « جادو ‏ را غالباً بجای « دروند » پهلوی‌ویازند ودروغپرست ویبرو دبومسناآرد‬
17210:   ‫‪ - ۴‬از‪ :‬در(ماب) ‪ +‬بند ( از ‪ :‬تن ) = دروند » لغة بمعنی بانه‌ای ( چویکی )که‬
17211:   ‫برای بستن درها بعار برند ‪ .‬معرب آن دهرمبند و دروند ع(ا‪.‬میانه) *دزی ج اص *‪۲٩ : ۳4‬‏‬
17822:‫داغ وشاترا خوانند ‪ - 6‬و بکر اول بر وزن‬         ‫مترقةٌ سالهای ملکی ‪ -‬وماضی دروندن‌هم‌هست‬
17839: ‫‪ - ۴‬دردخهة خطی «لفت محای شوشتر» متعاق‬                ‫» دروندنل ‪.‬‬   ‫‪ - ۷‬رك‪ :‬درودن‬
=== BQT v2 درشکه ===
7836:         ‫فاض ‪۷۲۲‬؛ درآخر کلمات غیرتر کی نز آرند همجون درشکه‌چی ‪ .‬ارابه چی » تماشاچی ‪-‬‬
17541:   ‫مأخون از آلمالی‬           ‫‪ ۵‬درشکه ‪ -‬بطم اول و دوم و کمر چهارم ‪ .‬از روسی ‪۴020۳‬‬
17542:   ‫‪6‬درشکه)؛ گردونۀ چهار چرخه که با اکسشبیده شود و اطافکی برای حمل مسافر‬                ‫(‬
```


## [2026-09-05T20:09:51.882Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17520,17560p' BQT_v2_pages.txt\necho \"=== page tags near ===\"\nawk 'NR<17560 && /\\[pdf page/ {l=$0; n=NR} END{}' BQT_v2_pages.txt\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1>17400 && $1<17600' | head",
 "description": "Print BQT context for درشکه"
}
```


### [2026-09-05T20:09:53.544Z] TOOL RESULT

```
      ‫معرب‌آن بز «درش»*ابن درید» ‪ .‬رکه ‪:‬درشی‪.‬‬                  ‫‪۴‬‬             ‫‪.‬‬       ‫درسته» درشه‪‎‬‬     ‫ر؟‬       ‫‪١‬‬

   ‫‪(22‬آرودی است که‌بسحونریزد‬                  ‫غام ‪0۲‬‬        ‫‪ ۳‬در‬             ‫» (ھ‪ .‬م‪. ‎).‬‬     ‫ورغ‬    ‫«‬    ‫مصحف‬       ‫‪۴‬‬



                             ‫رك‪ :‬درغلبکین ‪.‬‬           ‫‪۵‬‬            ‫‪.‬‬     ‫‪۸‬‬       ‫‪.‬حدود‬    ‫میئورسکی‬        ‫«حجدود الءالم ‪۷۲‬؛‬




      ‫(رأت» سعی کردن ) ‪.‬هندی باستان ‪۲5۳20-‬‬
                                         ‫(جرأت ‪ .‬جارت‪ .‬کوشش) و اوستا ‪ 0156۳31‬ج‬
  ‫‪۰‬‬     ‫وهو‪.‬شمان از ريشةٌ ابرانی‪ 0 ۵6۳5۵۳-‬حدی مزند ‪ ۶‬هویشمان ‪۲۵۵۹‬‬                                        ‫میداند «اسدق ‪۲‬‬
      ‫افغانی ‪« 605۵۷۲0‬هوبشمان‌اضا» ‪ .‬کیلکی ‪405‬نا‪۲‬نا؛ ناهموار ‪ .‬ناصاف‪ -‬زمخت‪.‬سخت » خشن‪-‬‬
                                                                                             ‫غلظ‪ .‬کشف رك‪ :‬درشتی ‪۰‬‬

  ‫‪ ۵‬دشرتی ‪ -‬حم اول و دوم‪ « .‬از‪:‬درشت ‪ +‬ی (مصدری) ؛ درشت بودن » سختی و ستم‬
      ‫تندی‪(« :‬شاهدان) تا خوب و لطیفند درشتی کنند وچون درشت شوند تلطف‬                                  ‫با جور ‪ -‬ترش‌روبی ‏‬
                                                     ‫کنند و دوستی لمایند ‪« ».‬کلتان ‪. ۱۶۱2‬‬
   ‫مأخون از آلمالی‬           ‫‪ ۵‬درشکه ‪ -‬بطم اول و دوم و کمر چهارم ‪ .‬از روسی ‪۴020۳‬‬
   ‫‪6‬درشکه)؛ گردونۀ چهار چرخه که با اکسشبیده شود و اطافکی برای حمل مسافر‬                ‫(‬
                          ‫دارد که‌مقف آلرا میتوان بلند کرده برافراخت وبا تاکرده خواباند ‪.‬‬
  ‫‪-‬‬                                                                           ‫در غو رگی مویز شدن‬

                                                     ‫که آنجا شراب خوب میشود » شوراب درغمی‬
 ‫فروغ‌وروشنی ‏‪ - ٩‬وچیزی که درخشان ‪,‬اشد ‪۵‬‬
 ‫وفوطه‌ای که درروز جنگ بربالای دستار و خود‬          ‫موسیقی که شنیدن‌آن غم‌والم از دل بیرون کند‬
            ‫‪,‬‬   ‫هل‬   ‫که بت رکی دولغها کون‬                         ‫ت رکیبیآن درالدوه باشد‪¥ .‬‬   ‫وهعنی‬


‫درفشان ‪ = ۴‬بروزن درختان » بمعنی‬                     ‫دزن ‪ -‬کنابه‬
                                                              ‫در غو ر گی مشو ب‬
       ‫لرزان باشد ‪ -‬ویمعنی تابان هم هت ‪. ۸‬‬                ‫‪.‬‬      ‫ب)اشدشند‬
                                                                        ‫از بمراد رسیدن وضایع (‪۱‬‬
‫فش کاو ان ‪ ۹‬س یاواوبالف کشید»ه‬        ‫در‬
                                                     ‫ذر عیش‪ -‬بر وزن دروش »‪ ۰‬بمعنی‬
 ‫» وشرح‬     ‫گر‬
             ‫نا‬‫هاوة‬
                  ‫علم بفدرون‌است ومنوب بک‬            ‫ابوه و بسیار باشد ‪ -‬و نام لوعی از زردآلو هم‬
=== page tags near ===
```


## [2026-09-05T20:10:05.445Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3\necho \"---\"\npython3 - <<'EOF'\nimport re\nlines=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ntags=[(i+1,l) for i,l in enumerate(lines) if 'pdf page' in l or re.match(r'^\\s*\\[.*page',l)]\nprint(len(tags))\nfor n,l in tags[:5]: print(n,repr(l[:80]))\n# find tag before line 17541\nprev=[t for t in tags if t[0]<17541]\nprint('PREV', prev[-1] if prev else None)\nprev2=[t for t in tags if t[0]<17868]\nprint('PREV dorugh', prev2[-1] if prev2 else None)\nprev3=[t for t in tags if t[0]<17973]\nprint('PREV droghparast', prev3[-1] if prev3 else None)\nEOF",
 "description": "Map BQT lines to pdf pages"
}
```


### [2026-09-05T20:10:07.172Z] TOOL RESULT

```
---
0
PREV None
PREV dorugh None
PREV droghparast None
```


## [2026-09-05T20:10:12.199Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\npages=t.split('\\f')\nimport sys\nfor i,p in enumerate(pages):\n    if 'درشکه' in p and 'روسی' in p: print('DOROSHKE leaf',i)\n    if 'دروغ' in p and 'پارسی باستان' in p: print('DOROUGH leaf',i)\n    if 'دروغ‌پرست' in p or 'دروغپرست' in p: print('DPARAST leaf',i)\nEOF",
 "description": "Find BQT leaves"
}
```


### [2026-09-05T20:10:13.908Z] TOOL RESULT

```
formfeeds 683
DPARAST leaf 11
DOROSHKE leaf 297
DOROUGH leaf 303
DPARAST leaf 305
```


## [2026-09-05T20:10:17.505Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));import textwrap\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('SNS'),ensure_ascii=False,indent=1))\n\"",
 "description": "BQT and SNS offsets"
}
```


### [2026-09-05T20:10:19.377Z] TOOL RESULT

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
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
```


## [2026-09-05T20:10:29.443Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (303,304,305,306):\n    print('===== LEAF',i,'= printed p.',i+540,'=====')\n    print(pages[i])\nEOF",
 "description": "Print BQT leaves 303-306"
}
```


### [2026-09-05T20:10:31.103Z] TOOL RESULT

```
===== LEAF 303 = printed p. 843 =====
 ‫دروقیئون‬                                                                            ‫مرت‬
‫میگشاید وبعربی مبضم خوانند ‪ ۴‬؛ وباین ممثی‬     ‫استغفار واز انان سناش و دعا وحیوانات دیگر‬

‫بفتح اول همگفته‌اند ‪ -‬و با واو معروف درعربی‬    ‫تسبیح باشد ‪ -‬و نام روز پاجم امت از خمة‬
‫داغ وشاترا خوانند ‪ - 6‬و بکر اول بر وزن‬         ‫مترقةٌ سالهای ملکی ‪ -‬وماضی دروندن‌هم‌هست‬
‫وممنی درفش است که افزار دفش دوزان و امثال‬      ‫رد ‪ -‬وبا واو مجهول» چوب‬
                                                                     ‫یعتی غله را دکرز‬
‫آتیاباشد؟ ‪ -‬وطم روزجنکه را کهممته‌اند ‪-‬‬        ‫ودرخت وتخته باشد وچوب نراش را ازین جهت‬
‫وفوطه را یز کونند که درروزجنگه‌بربالای خود‬                          ‫برند ‪*. ۴‬‬    ‫وگ‬‫کود‬
                                                                                     ‫در‬
‫آهنین ودستار بندند ‪ -‬و بمعنی روشنی آهمده‬      ‫در ودن ؟ د بروز نکشودن‪.‬در وکردن‬
                                 ‫است ‪#. ۷‬‬
                                              ‫و بربدن غله باشد ‪ ۰‬و درو يدن هم باین معئی‬
                                                                                        ‫أت ‪.‬‬
‫درو فینون‪ -‬بفتح‌اول وثائیبواورسیده‬
‫وقاف مفتوح و تحتالی ساکن ولون بوواکشده‬         ‫دروش ‏ م اول و واو مجهول بر‬
‫متی ‪ ۸‬و بعنی‬
           ‫رتیواس‬
                ‫و بنون دیگر زده » لف‬           ‫نشتر<جام راگوبن دکه بدان رکه‬         ‫وزن صروش»‬


 ‫‪ - ۴‬دردخهة خطی «لفت محای شوشتر» متعاق‬                ‫» دروندنل ‪.‬‬   ‫‪ - ۷‬رك‪ :‬درودن‬
 ‫بكتابخانة علامه دهشدا لز آهده‪ :‬درود یمعتی جوب و تخته و درخت و از بجهت جوت تراش را‬

 ‫‪ - ۴‬از‪:‬درو ‪« ۵۲‬هوشمان‪۹۵‬ه» ‪٣‬‏ دن* بوندمصدری؟پاز دد‪ .0۲4 01‬کردی‬                ‫ند‪.‬‬
                                                                                ‫کر‬‫وی‬
                                                                                   ‫کود‬
                                                                                     ‫در‬
 ‫ور ‪:‬‬       ‫‏‪( dirûtin . dirûn‬درو کردن) ‪nûrid ۰‬‏ (درو) ‪ ۰‬وخی ‪ma‬‏ _ ‪ » ward‬اسذق ‪٩‬‏‬
  ‫‪ = ۴‬درفش («‪.‬م‪ > ).‬دراراك (ساطانآباد) بدین معتی ‪5۷00۳3‬‬                      ‫هوشمان اساً ‪.‬‬
 ‫‪ _9‬ابن استنباط ادرست را ازین بيت‬               ‫) « مکی‌نژاد » ‪.‬‬      ‫ان‬
                                                                       ‫اانجو‬
                                                                           ‫رفاث‬  ‫( آل‬
                                                                              ‫ست ک‬
                                                                           ‫سوزلی کرده‌اند ‌‬



        ‫ستوروار بر اعدا نهاد داخ دروش ‪.‬‬        ‫به‌ومه ی که ستور ان دروری داغ کناه‬



  ‫آشکار است که «دروش» درین شمر سوزنی ضبط دیگری از کلمة « درفش » (« م‪ ).‬فارسی است‬
  ‫که هنوز در زبان فارسی رایج است و «داغ درفش » گوبند و از قدیم در ابران معمول بوده است‬
  ‫که برای امتبازچهاریابان وستوران دربهارهر سالگرء هابی راکه درهمان سالزاده میشدند بادرفشی‬
  ‫که درآتش‌حی گذافتدن درراشان‌داغی‌مرز دندوآن دأغ‌علامت مخصوصی بر؛ی‌شناختن آن چهاریا ود‬
  ‫واین‌عمل‌داغ‌زن‌را«درفشرداغ *یا«داغ‌درفش؟میگفتند‪.‬درین‌صورت له دروش کلم تازست وله بمعنی‬
  ‫‪ -‬رك‪ :‬درفش ‪.‬‬     ‫شاست‪.‬معید نفسی‪ .‬دربارة چندلفت فارسی‪ .‬بادناءة پورداودج ‪. ۷۲۲4‬‬
             ‫‪muincyroD = ۸‬‏ «لك ‪ ۲‬ص “‪1A‬‏ ‪.‬‬               ‫‪ ۷‬سکر‪ :‬درفش ‪.‬‬
 ‫‪ 0‬درو دگر‪ -‬صم اول وقتح پنجم » از‪ :‬درود ‪ +‬گر(یسوند شفل) رك ‪ :‬دروده در و گر‪.‬‬
  ‫)‪ .‬بهلری ‪ 80۳0‬م«نای ‪> ۲۷۲‬‬           ‫‪ 2‬دروغ ‪ -‬نم اول ودوم » ( تلفظ قدیم ‪0‬‬
  ‫‪۳۰0‬و‪ . 8۵‬از بارسی باستان ‪ . 28112۳-1‬اوستا ‪« 20802۲-1‬بارتولمه‬      ‫د«ناوادیا ‪3۱‬‬ ‫‪۷‬‬
  ‫‪« ۸۷‬یبر گے ‪٩۵*.‬‏ دراوراق مالوی سهاوی ‪( 2۷۳1 -‬دروغ گفتن» فریفتن)» در پارسی باستان‬
  ‫‏‪s(Herning , A list of Middle Persian...,BSOS,IX,1 ,p. 82) 2۰‬‬
   ‫کردیع ‪. 20۳‬افنانی م ‪. 86۳21‬بلوچى ع ‪ ۰8۵۳1 8۵724‬و ‪ 18۵۳0‬اسشق‪.›۷00‬‬
   ‫فریز دی ویرنی ‪ » 07624‬نطنزی ‪ ۵.۱: 0۲31‬ص‪ .»۲۹۲‬سمنانی ‪ ۰ 1۲۷‬سنگری ‪۳11‬‬
  ‫سرخه‌یی و لاسگردی اانا ‪ .‬شهمیرزادی ‪. 701‬ص ‪ ۳۹۱‬اورامانی ‪ .4 0۲‬اورامان‪.‬‬
  ‫یه در صفحهٌ ‪۸۶۸‬‬

===== LEAF 304 = printed p. 844 =====
 ‫)‪“1‬‬                                                                                                  ‫دروك‬




 ‫باشدا ‪ -‬ونام شهربست (‪ )۳‬درخراسان مابن مرو‬                ‫کوبند بونالی است » بمەنی نباتی کهبدرخت‬
‫وناکه‌آنها یز دوشپراند © ‪ -‬وینم اول پیمانة‬                ‫زیتون ماند لکن از بك کز کوناه تر میباشد‬
‫غله راء‌گوبند ‪ -‬و دعابی باشد که مفان درستایش‬             ‫وبر کش درازتر از برک زیتون امت وکل آن‬
‫خدابتمالی‌و ذرآخوانندویرخوردایها بدمند‪ .‬وبعداز‬            ‫سفید میشود ر تخم آن بمقدار کرسنة کوچك‬
‫آن‌بشورندا وهرچز که‌یر آن‌درون‌خوانده‌ودمیده‬              ‫میباشد و طبع آن همچوطبم بنرالینج (‪ )۱‬است‬
‫ند گوبند مشته شده و هرچیز تخوانده باشند‬
                                        ‫باش‬
                                                                   ‫واگ زیده خوزه یم کهلتز برد‬
‫تایشته یمنی‌ناخوانده " چه یشتن با نحتانی وشین‬             ‫دروك ‪ -‬م اول بروزن‌سلوك ه»یزم‬
‫قرشت (‪ )4‬وفوقاتی» بمعنی خواندن باشد بزبان‬                                             ‫پاريك رکاوبند ‪.‬‬
                                 ‫زند وپازند (‪. ۷ )۵‬‬       ‫در و گر = بض‌اول وثالی (‪ )۲‬وفتح‌کاف‬
‫درون اروده کنابه از صاحب دل‬                               ‫فارسی » مخفف درود گر الست که استاد چوب‬
               ‫وصاحب مجاهده باشدب و‬
‫کی را دگزونند که‬                                          ‫تراش باشد وبعربی‌تجار گوبند‪ -‬ویک اول وفاح‬
                         ‫دل مردمان بدست آ ورد ‪4۸‬‬         ‫ثالی‪ .‬شخصبکه غله میبرد ودروميکند ‪ ۴‬واو را‬
‫درو نج = بفتح اول و رابع و سکون‬
                                                                                ‫بعربی حصاد خوانند ‪. ۴‬‬
‫» ‪ ۰‬وآن دوای باشد‬            ‫جيم ‪ +‬معرب درو لك ات‬         ‫درون = بفتح اول » بمعنی اندرون ‪۴‬‬

   ‫(‪ )۳‬چك ‪ :‬شهری ه‌هت ‪۰‬‬                     ‫وئالی ‪۳‬‬      ‫)‪ (۲‬چك‪:‬‬         ‫بزراشیج ‪۰‬‬   ‫جك‪:‬‬      ‫)‪(۸‬‬


                                       ‫‪ :‬ژند و باژند ‪.‬‬   ‫(ه) چك‬          ‫(‪ )4‬چك ‪- :‬قرشت ‪.‬‬

          ‫‪. ۴‬از درو (هم‪( ۳ + ).‬یوند فاعلی و شنل ‪).‬‬                        ‫رك‪ :‬درود کر ‪.‬‬       ‫‪- ۱‬‬

   ‫‪ = ۴‬اندرون ( «‪.‬م‪ .) .‬اشکاشمی‬                     ‫‪ - . ۳‬حصاد درودن انت ر ک‪ :‬منتهی الارب‪.‬‬

                                 ‫‪ ۰ 00‬مریکلی ‪ « 0131‬کربرسن ‪, ۷۷۰‬کیلکی ‪: 80۲‬‬
                   ‫درون عاقت بر کن ‪۰‬‬     ‫که رش‬                      ‫حذر کن زدود دروتهای رش‬
   ‫‪‎‬ناتلکد« ‪. ۰4٩‬‬
   ‫‪ - °‬دره‌عجم البلدان و حدود العالم تیامده» اما در ذبل عالمآرای عباسی ناد شده ‪ .‬رك‪:‬‬
   ‫‪ 00۲4 _ ۱‬در تلقظ پااسیان ‪ , 0۵۳1‬اوستا‬                           ‫مجلةٌ سخن سال ‪ ۳‬شماره‪ ۳‬ص ‪. ۹۲۲‬‬
   ‫‪[ 02002۳0- .‬نان فذبه]* قس‪ :‬حندی باستان ‪( 5201۷6۳1 . 281۷8۳1‬ملك‪ .‬صرف) «اسشق‬
    ‫‏‪« _Y¥‬وبراف رابرآن‌تخت شاندند وروی‬                   ‫‪ 4۲۵‬و‪. ۸۹۵‬‬     ‫‏‪ ٩۲۷:‬ورك‪ :‬شت ‪۱‬ص ‪٩۱۰‬‏‬                ‫ص‬
   ‫بند بروی فگرذواشتند و آن چهل هزارمرد بر مزشن کردن استادند و درولی ندشتند وقدری په‬
   ‫بقلم نگارنده‬        ‫نهاد ند ‪«( €.‬مفدمة مرجم قدم ارداو برافنامه‪ .‬رك ‪:‬ارداوبرافنامه‬    ‫درون‬    ‫وان‬     ‫(یه)‬

                                       ‫‪- ۸‬صفتی ات خدای را بمعنی مربی باطن ‪:‬‬                         ‫‪. )+۲‬‬
                                                                                                        ‫ص‬
                   ‫بختای |‬       ‫رشد‬
                                   ‫خد بخ‬
                                       ‫ب خر‬
                                          ‫وی‬                       ‫ای درون برور برون ارای !‬
    ‫‪.‬‬    ‫‪٩°‬‏‬   ‫ص‬    ‫چاپ مدری‬    ‫حدبقه سنابی ‪.‬‬   ‫«‬

                         ‫‪: - ٩‬كر ‪,‬كنورد هنورد = ‪ 0۲0016‬جیزد« ‪‎‬صا ‪. ٩۲ :۳۸‬‬

                                                                                       ‫‪۳٩۸‬‏‬         ‫حه‬
                                                                                                     ‫صبهفاز‬
                                                                                                          ‫بق‬
        ‫‪۲‬طبری ‪ , 0۲61‬مازندرانی کنونی ‪ 0180۳0‬د«واژه‌نامه ‪, ۰۵۳۰‬گیلکی ‪ 80۳01‬؛ کذب‪:‬‬
                                                                               ‫‪.‬‬
                                                                       ‫سخن خلاف حققت » ضد راست ‪:‬‬
    ‫«کلتان ‪4۵٩‬‏ ‪.‬‬            ‫جهان دیده بسیارکوید درو غ‪.‬‬             ‫اکر راست میخواهی از من شنو‬

===== LEAF 305 = printed p. 845 =====
  ‫دره‬                                                                                                                ‫ز‪6‬ح‬
                                                                                                                       ‫بی‬


 ‫کنابه ازشکم باشد © ‪ -‬و قوس قزح (‪- ۱ )۳‬‬                         ‫بشکل عقرب وببب آن درونج عفربی خوانندش‪.‬‬
 ‫کومان‌حلاجی رانیزکوبندا ؛ وم اول هم‌بدو‬                      ‫کرم وخشك‌است دردویم(‪ ۱)۰‬کز ندکی‌جانورانرا‬
  ‫ون‬
   ‫ک‪۳‬م)ا‬
       ‫معنی آخر است کقهوس قزح (‬                                ‫کوش اکر فدری از آن درمان‌خانه‬                         ‫افع است‬

                              ‫حلاجی ‪ ۷‬باشد ‪#.‬‬                  ‫بیاویزند از طاعون ایمن باشند‪ .‬و اکرسوراخ‬
                                                                ‫کنند ودرمیان هردوران زن حانملدهفآوریززند‬
 ‫درو لزه و درو یره ‪ ۵‬س با زای‬
                                                                                    ‫آن زن از آفتها محفوظ باشد ‪.‬‬
 ‫هوز و زای فارسی ‪ .‬هر دو آمده است برءزن‬
  ‫تحققه (‪ » )4‬بمعنی دربوزه کودایی باشد ‪9.‬‬                     ‫درو ند = بفتح‌اول بروزن فرزند »نام‬
                                                                ‫پهلوانی‌است ‪-‬ودام داروبی‌هم‌هست ‪ - ۱‬وچنکک‬
‫درو یش سلطان دل = شاره‌برور‬                                     ‫وقلاب رانیز کوبند وبعربی‌معالاق خوانند ‪ -‬وم‬
 ‫کاینات است که بیغمیر ما صلوات الهعله وآله‬                     ‫اول بده‌ذهب ونامقید وفاق‌را گویند بزیان زند‬
                               ‫وسلم باشد ‪.‬‬                                                                 ‫ویازند (‪ )۲‬؟ ‪.‬‬
 ‫دره = بفتح اول و تشدید الی» شکنبة‬                            ‫درون ‪۵‬کنآاربهه‌ازیداندرون وکینه‌ور‬
 ‫کوسفند وغیرء باشد ‪ -‬کوشادکی ميان ده کوه‬                                                                    ‫ومنافق باشد ‪.‬‬
‫رکاپریبزند ‪٩‬‏ ؛ویتخفیف ثالی از همین معنی‬                        ‫؛صفر‬
                                                                   ‫‪ -۳‬بروزن عروسك م‬                        ‫وك‬
                                                                                                            ‫نرل‬
                                                                                                              ‫د‬
 ‫دارد‪ -‬ونام‌ولاتی‌هم‌هت ازملك بدخشان که مردم‬                   ‫درون باشد » و بیخی است دوایی شبیه بعقرب‬
‫آنجا یخوش صورتی مشپورند و انارخوب درا لجا‬                       ‫که آنرا درونج عقربی گویند » و درونج معرب‬
                                                                                                    ‫زک‬
‫مدشود ‪ .-‬و ضاحمول و تشدید الی پوستی چند‬
 ‫باذد باريك که بر هم بدوزند با برهم ببافند‬                     ‫درو نه = بفتح اول وبا واو مجهرل بر‬
‫کوناهکارانرا بدان تنبه سازند وکاه باشد که‬                      ‫وزن نموله » بمعنی درونك است‪ .‬وآن کیاهی‬
 ‫دهل ولقاره رابدان نوازند ویمعتی‌دلیل وبرهان‬                  ‫باشد شبیه بعقرب ‪ - ۴‬وبمعنی درون همهت که‬
   ‫)‪ (4‬چك‪ :‬تخففه‪.‬‬            ‫)س( چش‪ :‬فوی‌وفز ح ‪.‬‬             ‫(‪)۲‬چك‪ :‬ژند وباژند‪.‬‬            ‫)‪ (۱‬چكث‪ :‬دوم‪.‬‬

    ‫»هرند) *مماس ‪۷۲ ۲‬‬        ‫(کافر ‪ ۰‬می دمن‬       ‫بپلوی ار‬                   ‫‪— ¥‬‬        ‫‪.‬مصحف؟* درو ‪1۵‬؟‪.‬‬            ‫‪ ۱‬ظ‬

    ‫دروغ‌پرست " |زاوستا_ ‪ « 602۷۲1 - ›4 812۷89‬بارتولمه ‪ » 4۷۷۲‬پازند وپارسی ‪04۳2۷721‬‬
   ‫رك‪ :‬درو نك درولج ‪۰‬‬        ‫‪> ۴‬‬        ‫‪ -‌ ۳‬رك‪ :‬درو له‪.‬د؛ ولج ‪۰‬‬              ‫لیب رکد‪ »+۰‬ورك ‪:‬اسشق ص‪۳ ۴۲۲ ۰۲‬‬

   ‫‪anurd‬‏ ( کمان ‪ ۰.‬قوی) » تلوچی‬              ‫ت‬    ‫ماک‬           ‫‪۹‬‬                      ‫رك‪ :‬درون ‪.‬‬              ‫‪6‬‬
                                     ‫‏‪ dîn uk , 0‬سوف )حرق » اغدوب ع ‪ 4۳00‬قشسا« ‪. 00۸‬‬
   ‫«ومان وی( کیومرث) بدان‌روز کار چوبین بود بی‌استخوان » بکپاره چون درون‬
                                                                       ‫ک‬                                        ‫‪۷‬‬
                                   ‫درووزه (ھ م‪ (.‬۾ دریوز *‬           ‫=‬   ‫‪۸‬‬              ‫حلاحجان» «نوروزنامه ‪۹۳٩‬‏ ‪.‬‬
    ‫وخی ‪۲621‬‬       ‫(بطلموی ‪(1‬‬            ‫_ اوستا ‪_ûnerad‬‏ (دره‪ ,‬گردنه) ‪ ۳‬سونالی ‪anrûD‬‏‬

   ‫فارسی بمعنّی‬   ‫»ودر‬       ‫ع ‪ered‬‏‬    ‫هو ‪.‬شمان ایض » در ‪9۳‬‬                 ‫و رك‬      ‫‏‪ 9 dher‬أسشق ‪“°‬‬               ‫سریکلی‬

   ‫‪ ۰‬یر لی‬   ‫‪earread‬‏‬   ‫؛ گلکی‬      ‫ارل ودوم)‬     ‫(بكر‬       ‫اسلام ‪ :‬دره‬     ‫الممارف‬   ‫دائرة‬       ‫رك‪:‬‬   ‫وادی عر هی آبد ‪۰‬‬


    ‫سنگری ولاسگردی ‪» 64۲۲310‬سرخه‌بی‬                         ‫‪.-‬دانی ‪۲۲3‬‬             ‫ونطذزی ‪ ۱ .۵« 8۳۳20‬ص‪54‬‬
                                                        ‫‪.‬‬     ‫‪ .‬نهمرزادی ‪« ۲۲00‬ك‪ .‬ص‪۱۸۱‬‬                                    ‫‪6‬‬
    ‫‪4۸‬‬   ‫نقه درصفحه؟‬     ‫‪۳‬‬     ‫‪ ۰‬ددن‬     ‫درودن‬   ‫رك‪:‬‬   ‫وياجم‪.‬‬    ‫اول وفتح دوم‬       ‫نکر‬        ‫=‬   ‫ادن‬    ‫درو‬   ‫‪¥‬‬

===== LEAF 306 = printed p. 846 =====
   ‫نت‬                                                                            ‫درة آسمان‬
‫همآمده است ‪ -‬و بکراول درفربی آلت ضرب | باشد وآن زرست‌رايج ووزنیاست معروف ‪.۷‬‬
‫بررزن سررشته» بمعنی‌جود‬     ‫رشت‬
                              ‫ه‬ ‫د‬                                              ‫وزدارا گوبند ‪.‬‬
                          ‫در آسمان ‏کنابهازکهکنانانت‪ | .‬وعطا وکرم باشد ‪#.‬‬
‫در هم بقلی ‪ = ۲‬مشهور أست ‪٠‬‏ وآن‬                                    ‫وآارا بعریی مجره خواند ‪.‬‬
‫زری بوده‌منتوب برای ‪,‬هودی کهآ را رای‌الیفل‬        ‫هرام » بروزن فرجام ؛ یمعنی درهم‬
                                                                                ‫د‬
                                     ‫رك‪ :‬بشلی ‪.‬‬    ‫‪۴‬‬         ‫‪ - ۱‬رك ‪ :‬درهم » درم ‪.‬‬

                                                                           ‫شه از صفسه ‪۵6۸‬‬

  ‫‪ #‬درهم ‪ -‬بفتح اول وسوم » از‪ :‬در (حرف اضافه) هم ؛ شوش ‪ .‬مختلط‪ .‬شوریده؛‬
      ‫دلتان ‪. ۳:۰‬‬
                ‫را) ونفی کنند تاچندین دزهم چرا گنت ک‬            ‫اد‬
                                                                 ‫شزیندش‬
                                                                      ‫(ودی‬
                                                                         ‫آشفته‪* :‬ملك فرم‬
          ‫(ك‪ :‬درم) ‪.‬‬
                   ‫وفتح (رکسر) سوم » معرب» واحد كوك نقره و واحد وزن ر‬                  ‫وکل‬
                                                                                         ‫رای‬
                                                                                           ‫م‬
  ‫‪ #‬ورویش ‪ .-‬شنح اول » پپلوی ‪hsöyird‬‏ ( فقیر؛ تھی دست ) « ای ‪> ۲: ۲۷۲‬‬
 ‫رتا‪00‬ع‪ . 120‬بازید ‪ . 05۵67780‬هردواز اوسا ‪« 11081۳-‬بارتولمه ‪ . ۷۷۷‬شک کلمه[ شکر‬
  ‫و رك‪ :‬اسشق وهوبشمان ‪ 4۵۵‬؛ دولف «تفس» اصلآ نرا ”در بیش بمعتی‬             ‫ست‪ .‬رك‪ :‬لبر که‬
   ‫قتام الیاب دانته‪ .‬وغالباآترا بممنی ( گدای درخاله ها) گرفته‌الد ف«ولری ‪ . ۱.‬ص ‪٩۳۸: 2‬‏‬
  ‫‪ 04۸ ۳‬ولی ابن اشتقاق عامیانه است ‪ .‬رف‪ :‬مقالة ‪ ۴۲۴‬درباب تاربخ عرب در‪۵‬ا‪1‬ا‪٩06۳‬‏ ج‬
   ‫‪ ,‬شمارء *س‪۹۸‬ه‪ .‬در چپار مقالة نظامی عروضی (ص‪)٩۸‬‏ نام شاهری «پسردرغوش ‪٩‬م‏ده‬             ‫‪۷‬‬
                                                  ‫ومرحوم قزوینی در تعلیقات (س‪ )۲۵۱‬بوشته ‪:‬‬
                                                  ‫« در میزان الافکار فی شرح معیار الاشعار که‬
                                                  ‫رساله امت در عروط تالف خواجه سیرآلدین‬
                                                  ‫طوسی مطوراست که دربسنی ازبلاد ابران‌کمة‬
                                                  ‫درویش را «در غویس» تلفظ لمایند باغین و واو‬
                                                  ‫ممدوله * وقریب بیةین‌است که درغویش دراینجا‬
                                                   ‫همین کلمه است ‪ » .‬در شهمیرزادی ‪051۷780‬‬
                                                   ‫د ‪ 2‬س‪ ۹۷۱۰‬ک‪.‬یلکی ‪ 151۷144‬؛ معرب‬
                                                   ‫آن‌دروش «تفس؟ و «دروش» مصدر معرب است‬
                                                   ‫بمعتی درورش شدن ‪ ۰‬جامهٌ دروشان پوشیدن‬
                                                  ‫دزی جاص ‪۲٩ :۸۳‬‏ ؛ نهیدست " بچییز "‬
                                                                        ‫کدا ‪ .‬فقیر » بی‌توا ‪:‬‬
                                                             ‫شب هر توالگری برایی همی رود‬
                                                  ‫دروش‌هر کجا کهشب] دسر ای اوست‪.‬‬
                                                    ‫‪‎‬ناتسلک« ‪. ۱۱٩‬‬
                                                   ‫‪-‬صوفی» فلندر ‪ .‬رك ‪ :‬دائرة المعارف‬
                                                   ‫اسلام ( ه‪.‬م‪ « : ) .‬طابفة درویشان از جورفاقه‬
                                                   ‫بجان آمده بود واز درویتی بقفان » آحنك‬
           ‫یکی از درویشان عېد اخبر‬                        ‫دعوت اکوردند ‪ « »...‬کلتان ‪۳۰۱٩‬‏ ‪.‬‬
       ‫( برهان اطع ‪) ۱۱۱‬‬
```


## [2026-09-05T20:11:09.423Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS drog/druwand ===\"; grep -n -i \"drog\\|drōg\\|druvand\\|druwand\\|drwnd\\|draoga\" SNS_pages.txt SNS.txt | head -25\necho \"=== MON دروغ / درشکه ===\"; grep -n \"درشکه\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10",
 "description": "Grep SNS and Mo'in"
}
```


### [2026-09-05T20:11:09.529Z] TOOL RESULT

```
=== SNS drog/druwand ===
SNS_pages.txt:8814:                                                                                                      •£UJ:drog/dro/         :   KDB J : ^» : ^j
SNS_pages.txt:8815:                                                                         UiVb, 768)drogha-
SNS_pages.txt:12637:    draoja-, draoga-    :   t- (*A-^» 4*>**    ^-y 5                8            1              -
SNS_pages.txt:12643:    {Mir. Man.   drwg:j^ (AiW>. 768) drOgha-: ^j-^-                                                                                                           ^y.
SNS_pages.txt:12729:                                                                                                                                          .   Xj«   4   ±>Jm 4jiK , jijjo :   druvand:.      J»^-»
SNS_pages.txt:12737:                                                                                                                                 •)Y/16^ •o'y^'o'^u^druvandan:                              V-MW*
SNS_pages.txt:12742:                                                                                                                            lY/Yo^5 •>S.jlxijl. li AiiJ j : druVandIh:,
SNS_pages.txt:14916: traitana- 135/9        drogha- 220/4-323/13
SNS_pages.txt:15525:bwzysn 107/20         drwnd 324/16
SNS_pages.txt:16028:mard I druvand 308/11        m5xag(?) 252/2                     murvag 245/19-249/1       nasrOst 244/15
SNS_pages.txt:16309:dard 320/7                  den 188/17                   doan 327/6                 druvand 324/15
SNS_pages.txt:16310:dar 1 dusax v 100/8         den5g5h 189/23               do hazar 307/20            druvandan 324/18
SNS_pages.txt:16311:darg5h 321/14               d§n ahramogth 193/7          dol 328/9-335/15           druvandth 324/19
SNS_pages.txt:16329:day 193/4                   diblr 308/21                 drOg/drOy 220/3            duzdldag 330/16
SNS.txt:12776:768)drogha- 
SNS.txt:12780:•£UJ:drog/dro/ : KDB J : ^» : ^j 
SNS.txt:17531:draoja-, draoga- : t- (*A-^» 8 4*>** 1 ^- y - 5 
SNS.txt:17532:{Mir. Man. drwg:j^ (AiW>. 768) drOgha-: ^j-^- 
SNS.txt:17678:. Xj« 4 ±>Jm 4jiK , jijjo : druvand:. J»^-» 
SNS.txt:17681:•)Y/16^ •o'y^'o'^u^druvandan: V-MW* 
SNS.txt:28464:drogha- 220/4-323/13 
SNS.txt:30312:drwnd 324/16 
SNS.txt:32006:mard I druvand 308/11 
SNS.txt:33240:drOg/drOy 220/3 
SNS.txt:33255:druvand 324/15 
=== MON دروغ / درشکه ===
MON_part1.txt:10904:گاری و درشکه» حمل و نقل بار» شخم 
MON_part1.txt:28446:درشکه و غیره» چارواء مرکوب» مطیه. 
MON_part1.txt:33863:آمدن از مرکب و وسایل نقلیه (درشکه» 
MON_part1.txt:50058:بچرخد: چرخ درشکه» چرخ ارانه» چرح 
MON_part1.txt:60490:درشکه: 0۳016 .( کردونه چهار جر حه 
MON_part1.txt:77473:بود. مسافر درشکه؛ اتومبیل» هوایما با 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:10904:گاری و درشکه» حمل و نقل بار» شخم 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:28446:درشکه و غیره» چارواء مرکوب» مطیه. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:33863:آمدن از مرکب و وسایل نقلیه (درشکه» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:50058:بچرخد: چرخ درشکه» چرخ ارانه» چرح
```


## [2026-09-05T20:11:11.160Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY دروغ ===\"; grep -n \"دروغ\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY درشکه ===\"; grep -n \"درشکه\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== KLN droshky/drink/dream/draw ===\"; grep -n -i \"droshky\\|drosky\" KLN_1966.txt KLN_1971.txt SKT.txt LKT.txt | head -20",
 "description": "Grep Aryanpur, Klein, Skeat, Lokotsch for droshky"
}
```


### [2026-09-05T20:11:11.245Z] TOOL RESULT

```
=== ARY دروغ ===
8803:چم "راست" در پرابز "کج" و "راست" در برابر دروغ" و "راست" در برابر "چپ" در اکثر زبان‌های هند و اروپانی :
9754:زور (به چم "نادرست و دروغ") / ۳۳۱
=== ARY درشکه ===
=== KLN droshky/drink/dream/draw ===
SKT.txt:23607:Jiussian  :  drosky,  morse,  rouble  (ruble), stcin>e,  verst.
KLN_1971.txt:76170:cp. draggle. Cp. also droshky. 
KLN_1971.txt:76369:droshky. 
KLN_1971.txt:76809:droshky, also drosky, n. — Russ, drozki (pt.\ 
KLN_1966.txt:12206:drag,  tr.  and  intr.  v.  —  ME.  draggen,  fr.  OE. dragan  or  ON.  draga,  ‘to  draw’.  See  draw  and cp.  draggle.  Cp.  also  droshky.
KLN_1966.txt:12238:Formed  with  suff.  ian  fr.  OI.  Dravidah,  name  of a  region  in  Southern  India, draw,  tr.  and  intr.  v.  —  ME.  drahen,  drawen, fr.  OE.  dragan,  ‘to  draw’,  rel.  to  ON.  draga,  ‘to draw’,  OS.  dragan,  OFris.  draga,  drega,  MDu. draghen,  dreghen,  OHG.  tragan,  MHG.,  G. tragen,  ‘to  bear,  carry’,  Goth,  ga-dragan,  ‘to pull,  draw’,  and  perh.  cogn.  with  L.  trahere, ‘to  pull,  draw’.  See  tract,  ‘region’,  and  cp. words  there  referred  to.  Cp.  also  drag,  draggle, drail,  drawl,  dray,  dredge,  ‘dragnet’.  Cp.  also droshky.
KLN_1966.txt:12311:droshky,  also  drosky,  n.  —  Russ,  drozki  (pi.), dimin.  of  drogi  (pi.),  ‘wagon’,  rel.  to  doroga, (which  corresponds  to  Pol.  drag  a,  Czech  draha), ‘way’,  and  cogn.  with  Norw.  drag,  ‘drawing rope’,  and  with  ON.  draga,  ‘to  draw’ ;  see  drag, draw.  For  the  relationship  between  Russ,  drogi, ‘wagon’,  and  doroga,  ‘way’,  cp.  E.  wain  and wagon,  which  are  related  to  way. drosometer,  n.,  an  instrument  for  measuring  the quantity  of  dew.  —  Compounded  of  Gk. Spocrop,  ‘dew’,  and  pirpov,  ‘measure’.  See  Dro¬ sera  and  meter,  ‘poetical  rhythm’, dross,  n.,  refuse.  —  ME.  drosse,  fr.  OE.  dross, ‘dregs,  dirt’,  rel.  to  drosna  (pi.),  ‘dregs’,  MDu. droesen(e),  Du.  droesem,  OHG.  truosana, MHG.  drusene,  G.  Drusen,  ‘husks,  dregs’,  and to  E.  dreg  (q.v.)  Cp.  druse.
```


## [2026-09-05T20:11:19.091Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '60480,60500p' MON_part1.txt\necho \"=== page tags ===\"; grep -c \"pdf page\" MON_part1.txt; grep -n \"pdf page\" MON_part1.txt | head -3",
 "description": "Read Mo'in doroshke entry"
}
```


### [2026-09-05T20:11:19.171Z] TOOL RESULT

```
درشت: 5۷ (ص.) زیر ز مخت» خشن؟ 
مسق. نرم» لیسن. ناهموار» پست و بلند» 
مضر س)؟ مق. هموار. ضحیم» حجیم. 
درشستخو (ی): (0*-.0 (ص‌مر.) تند 
خوی» بد خلق. 

درنستی: -00:081 (حامص.) صخامت. 
ناهمواری. ستم» ظلم» جور. ترشرویی. 
تندی. ضصحخامت. 

درشکه: 0۳016 .( کردونه چهار جر حه 
که با اسب کشیده شود و اطاقکی برای حمل 
مسافر دارد که سقف آن را می‌توان بلند کرد 
و سالای اطاتک را پوشاند با تا کرده 
خوابنید 

در صورنی: 2۳-911121-1) اف. ع] (حر. 
رب. مر.) در حالی» در سوقعی. در صورتی 
که: با وجودی که با وجود اینکه. اگر. 
درع: ٩6‏ [ع.)(.) جامةً جنگی که از 
حلقه‌های آهنی سازند؛ زره ج. درو ع. 
=== page tags ===
0
```


## [2026-09-05T20:11:49.201Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT Droschke ===\"; grep -n -i \"droschke\\|drozki\\|drozki\" LKT.txt | head -10\necho \"=== SKT draw/drag/drink/dream ===\"; grep -n \"^Draw\\|^Drag\\|^Drink\\|^Dream\\|Drosky\" SKT.txt | head\necho \"=== ls BQT ===\"; ls -la | grep -i bqt",
 "description": "Grep Lokotsch and Skeat; list BQT files"
}
```


### [2026-09-05T20:11:49.282Z] TOOL RESULT

```
=== LKT Droschke ===
=== SKT draw/drag/drink/dream ===
5393:Draw.  (E. "I  M.E.rf«mwi.  AS. J (by  change  from  g  to  xd\.  +  Du.  d* Iccl.  SwetT.  draga,  Dan.  ^m^.  Goth,  df G.  tragen.  to  pull  along.  cati7.  AUi Skt.  d/triii^h,  to  lengthen,  to  exert  01 (v'DHAKGH.)
=== ls BQT ===
-rw-rw-r--  1 sfmqrb sfmqrb  2634275 Sep  4 14:06 BQT_alt_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb      139 Sep  4 14:06 BQT_dli_part1.txt
-rw-rw-r--  1 sfmqrb sfmqrb 26399828 Sep  4 14:06 BQT_v1_djvu.xml
-rw-rw-r--  1 sfmqrb sfmqrb  2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb  4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2359504 Sep  4 14:06 BQT_v2.txt
```


## [2026-09-05T20:11:52.462Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:11:52.470Z] TOOL RESULT

```


```


## [2026-09-05T20:11:56.193Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%B4%DA%A9%D9%87",
 "prompt": "Give the full Persian entry for درشکه: etymology (which language it was borrowed from, Russian дрожки or German Droschke), pronunciation, meaning."
}
```


## [2026-09-05T20:11:57.981Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%D8%BA",
 "prompt": "Give the full Persian entry for دروغ: etymology chain (Middle Persian, Old/Proto-Iranian, Avestan, PIE root), meaning, and any cited references."
}
```


### [2026-09-05T20:12:00.619Z] TOOL RESULT

```
# Persian Entry for درشکه

**Etymology:** The word derives from Russian _дрожки_ (drožki), as stated in the Wiktionary entry: "From Russian _дрожки_ (drožki)."

**Pronunciation:** doroške

**Meaning:** A horse-drawn carriage, defined as "horse-drawn carriage" in the source material.

**Plural Form:** درشکه‌ها (doroške-hā)

The entry does not mention German _Droschke_ as an alternative source—only the Russian origin is documented.
```


### [2026-09-05T20:12:39.922Z] TOOL RESULT

```
# Persian Entry for دروغ

**Meaning:** The word دروغ (durōġ / doruġ) means "lie," "untruth," or "falsehood."

**Etymology Chain:**
The word traces back through several ancient language stages:

- **Middle Persian:** From KDBA / dlwb' (drō(g))
- **Old Persian:** From 𐎭𐎼𐎢𐎥 (drauga)
- **Proto-Iranian:** From *dráwgah
- **Proto-Indo-Iranian:** From *dʰráwgʰas
- **Proto-Indo-European:** From *dʰrówgʰos, derived from *dʰrewgʰ-

**Comparative References:**
The entry notes cognates in "German Betrug and Dutch bedrog, both meaning deception," plus a connection to English "dream."

**Note:** The page does not cite Avestan sources specifically, though it documents the descent from Proto-Iranian through documented historical language stages.
```


## [2026-09-05T20:12:50.805Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dream",
 "prompt": "Full etymology of \"dream\": Old English dream 'joy, music', Proto-Germanic *draugmas, relation to PIE *dhreugh- 'to deceive', and the scholarly dispute about whether OE dream 'joy' is the same word as dream 'sleeping vision'."
}
```


## [2026-09-05T20:12:52.384Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/droshky",
 "prompt": "Full etymology of droshky: Russian drozhki, diminutive of drogi, relation to doroga and to the root meaning 'draw/drag'. Also date of first English attestation."
}
```


### [2026-09-05T20:12:56.641Z] TOOL RESULT

```
# Etymology of "Dream"

The word "dream" has a complex linguistic history. In mid-13c., it entered English meaning "sequence of sensations or images passing through the mind of a sleeping person," likely derived from Old Norse *draumr* and other Germanic languages, tracing back to Proto-Germanic *draugmas* meaning "deception, illusion, phantasm."

Interestingly, Old English *dream* originally meant "joy, mirth, noisy merriment," and scholars remain uncertain whether this is the same word as the modern sense. The OED theorizes that the "joy" meaning may have caused speakers to avoid it in literature, substituting *swefn* (sleep) instead—a pattern particularly strong in the Midlands and Northern England under Scandinavian influence.

The figurative sense of "ideal or aspiration" is relatively recent, originating around 1931 from the earlier notion of "something of dream-like beauty or charm" (1888). Related words like "daydream" emerged in the 1680s.
```


### [2026-09-05T20:12:58.260Z] TOOL RESULT

```
# Droshky Etymology

Based on the Etymonline entry, **droshky** has Russian origins. The word derives from "Russian drozhki, diminutive of drogi," which connects to "doroga" and traces back to a root meaning 'draw/drag'.

This etymology reflects how the word entered English from Russian, with the diminutive form suggesting it originally referred to a smaller or lighter type of vehicle—fitting for a traditional Russian carriage or sleigh.
```


## [2026-09-05T20:13:07.451Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dragan%C4%85",
 "prompt": "Etymology of Proto-Germanic *draganą: which PIE root is it derived from, what cognates (Latin trahere, Slavic doroga/drogi), and what descendants (Old English dragan, Old Norse draga)."
}
```


## [2026-09-05T20:13:09.460Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/drinkan%C4%85",
 "prompt": "Etymology of Proto-Germanic *drinkaną 'to drink': what PIE root is proposed, is the etymology considered uncertain/disputed, is a connection with *dʰregʰ- 'to draw' mentioned, and what are the descendants (including *drunkinōną 'to drown')?"
}
```


### [2026-09-05T20:13:12.836Z] TOOL RESULT

```
# Proto-Germanic *draganą Etymology

**PIE Root Origin:**
The term derives from Proto-Indo-European *dʰrógʰ-e-ti, traditionally traced to "*dʰregʰ-" ("to pull, draw, drag"). However, scholar Kroonen expresses skepticism about this connection and "leaves the origin open."

**Key Descendants:**
The entry documents extensive descendants across Germanic languages. Notable examples include Old English *dragan* (evolving into modern English "draw"), Old Norse *draga* (found in Icelandic, Faroese, and Swedish), and Old High German *tragan* (becoming modern German "tragen").

**About Cognates:**
The source material provided does not mention Latin *trahere* or Slavic *doroga/drogi* as cognates. It focuses exclusively on Germanic language family developments rather than cross-linguistic comparisons outside that branch.
```


### [2026-09-05T20:13:16.840Z] TOOL RESULT

```
# Etymology of Proto-Germanic *drinkaną

**PIE Root Proposed:**
The entry suggests a possible connection to Proto-Indo-European *dʰrenǵ- ("to draw into one's mouth, sip, gulp"), described as "a nasalised variant of *dʰreǵ-" ("to draw, glide").

**Etymology Status:**
The connection is presented as uncertain, indicated by the qualifier "Possibly from" rather than a definitive statement.

**Connection to *dʰregʰ-:**
Yes, the document explicitly mentions the root *dʰreǵ- and notes that *dʰrenǵ- represents a nasalized variant of this "draw" root.

**Descendants:**
The entry lists extensive descendants across Germanic branches, including:
- English *drink* and related forms in Scots and Yola
- German *trinken* and numerous regional variants
- Norse languages: Icelandic *drekka*, Swedish *dricka*, Danish *drikke*
- Dutch *drinken* and related languages

However, the document does **not** mention *drunkinōną* meaning "to drown" among the derived terms listed (*drankijaną*, *drunkanaz*, *drunkiz*).
```


## [2026-09-05T20:13:47.710Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line number -> leaf\nleaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf\n    leaf+=l.count('\\f')\nfor ln in (12637,12643,12729,12737,12742,8814,14916,16309):\n    print(ln, 'leaf', m.get(ln))\nprint('total leaves', leaf)\nEOF",
 "description": "Map SNS lines to leaves"
}
```


### [2026-09-05T20:13:49.554Z] TOOL RESULT

```
12637 leaf 178
12643 leaf 178
12729 leaf 179
12737 leaf 179
12742 leaf 179
8814 leaf 127
14916 leaf 206
16309 leaf 235
total leaves 242
```


## [2026-09-05T20:13:53.361Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (177,178,179,180):\n    p=pages[i]\n    print('===== LEAF',i,'=====')\n    print(p[:1800])\nEOF",
 "description": "Print SNS leaves 177-180"
}
```


### [2026-09-05T20:13:55.145Z] TOOL RESULT

```
===== LEAF 177 =====
                                                                                                                                                                  :




                                                                                                                      i—^U-i *-_„U «-Lfl;l^                                       rTo
                           bj^-^U^L^'j

                                                                 ¥"0*
      .
          /W4
          T      (     wd*-^) ****» :garzfid                ;




                                                                                           ^         Jt:      a>^.»    ^oi« ,j3d     fjS   :gragtar:                  V*-A»
                                                                                                                                                                      ^      3
                                                                                                                             Y6/V*** •(-j jt>** : ^)
                                                                                                                                                ,




                                 .^ M „:* sad, 100: J*
>/l*S.6V/>T*         Wa*k«on 106>sata-: L sata-                  &                  (c^t^^ltfU^ljjJ^)^, J/^'i .o«Ijj :drayld:                                         v"-*-"^
                                                                                   Benveniste, BSL, Ell, 1956. p. 49                                    :*& ^'j cw 1 * 1.*

                                                                                   r_r—Y-l/A<£ -W.           Schwartz, JRAS, 1966. p. 119.
^..U^^M** :e sad ud panjah, 150:                                 <
===== LEAF 178 =====
                                                                                         :                                                                                                          ,




    w                                         U- i-_*b *.b «3>3
                                                                                                                                                                li*.b*jlj


                                                                                                                  .rr-n/)*^ -f6/Y^ Uaofcstfn.1061 hazanra-                                              :   fc«




                                                    **»
•   Mb* *   .   ^b       &* «* cu-> druj druz
                     >, ^ . ojl^i *•> •                 «
                                                                :          ,

                                                                                                                                      jljA»J.lojo C o
                                         dru5- »'lta                                                                  •f/1f^                            :dah hazar, 10,000:
    -1,/»r*.Y/1.<* .A/^ .TVT^ M*W. 781)                                                                                                                                                                           ^


           M/U<* .*»JmU rYA/TT** n-VT^ -A/"* -TT-VT
                                            5
                •

                                                                                                               .•j^ibjjl^.ioifie hazar ud sanzdah, 1016: _>s>*e».

                            ^U^^mU'^isUkA'oVu^ druzan:                                         ^
===== LEAF 179 =====
                       '




      rra                                 (U^~l*b«,L*jlj
                                                                                                                                                        Lu BM^UtoU-^jlj                           TY1



      .   1/f^ h/y*S UiW».             421)ustra-: t>^ 5^- ustra-                              :fc-
                                                                     1
                                                                                                         C^b^iA^^I^] *it?*-oij->:dron-I siganag:3V3«_j *>-»

                   V?^ -W/Y** .j-i^: ustur pasm:                                    -*<->o -*>v£

                                                                                                                                                         1/H^ '»>*«• *A*Jj* jttfjJd* o*>^
                                                                •
                                                                    o**i   :zaraan:               W-£
      {Mir. Man.       jmJ   n   :   >^   C#£r. Wan. 11,514)                  zmJ n        :   >;fc
                                                                                                                        r .ii.t$lt-,bSjv*j1
                                                                                                                     ( (_
                                                                                                                                                        jjly.J i ) «^U> .J^jJidrang:
                                                                                                                                                              .
                              
===== LEAF 180 =====
                                              Lj^U-L.jI,                                                                                          L'_       i_-^__   It 4a b a j   I
                                                                                                                                                                                       j                                     TTf


                                                                                                                                      If/** -^igovend;.                                                      ,nd;>*:       J»»C


°*   lj   <5>*-   ^ o^/  «
                                      1
                                          •
                                              o J/ /•* **• : goharldan :              «>*«-«<               '(jA^-f-'Jo^'u^j** :ralrisn:                             yMyTWN, sn:                             >» :    SUW*

iri        :      *V
                       .*i— 'i-x.T'u*** :gohrig:                 ^V         •»>> tf*^ j J

                                                                                                                                  Jj^ Jj**:mIrSd: yMyTWN, yt:
                                                                                                                              .      .
                                                                                                                                                        ya^DY***                                         >*:

                                                                                                         -PY-6o-TY-f^-n-TV-T6-Tf-TT-TT-Y1-To-n-1A-»P-1T-1T/T^
                                                           bj4 < o*
```


## [2026-09-05T20:14:17.677Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12630,12650p' SNS_pages.txt\necho \"########\"\nsed -n '12722,12745p' SNS_pages.txt",
 "description": "Print SNS glossary lines"
}
```


### [2026-09-05T20:14:17.731Z] TOOL RESULT

```
                                                                                                                                                               -H*3 < -H-*; ->/   :grov, grav
                                                                                                                  .**jS.*j.»/.         .»/   lUiift. 530)grlva- :t-,;l  (^^
     6Wj>»^:drSg:                    -L>V*          )F . Jttj»* « tf*i»i       :dr8zan:         **>*           grlv pan         :    ^   -•>,/ :grlvlk           j^
                                                                                                                                                             griva- : ^S tJJ-.              i


                                                                                                                 *»** gryw :>;£ (Arm.  Gram 132)grapan: ^j/ U/
    draoja-, draoga-    :   t- (*A-^» 4*>**    ^-y 5                8            1              -




                                                                                                               {Mir. Man. Ill, 55)gryw :^ {Mir. Man. 11,49) :
    {Mir. Man.   drwg:j^ (AiW>. 768) drOgha-: ^j-^-                                                                                                           ^y.
     .VA/l#«5 (Mir.Man.II,51)drwzn:
                                        Ulr 54    )             ^                                         ,




                                                                                              -Ot«*»           gRM:    ^«o o'jo-'i^j'^^y^U-.Jjjj :drOd: t°»
########


                                                                                                             •   ( -tj*- <s**J daryos :  ^ X4tW>. 777)dri$u - zU



10                 •t/\Ct^       \/\\£ •{*£ g5v&n:                            ^m:^        :    -£»>£
                                                                                                                                          .   Xj«   4   ±>Jm 4jiK , jijjo :   druvand:.      J»^-»
                                                                                                         {Mir.Man.ll t 51\drvnd^L{AiWb.                            783)       drvant-   :    t-
      0-*i Jj» o& yijf
               '                 (ja-a.^.1)   :govi§n-.                     ,56:^*    :       it<jiiyK




                                                                                                                                 •)Y/16^ •o'y^'o'^u^druvandan:                              V-MW*
                              .oil^.j^ :g5vSd-.                                                V"»>*
To                               •j^jWtyjit/t^ -r6-Yr-Yr/r^ -u/t«$
                                                                            *yt:j»    :

                                                                                                                            lY/Yo^5 •>S.jlxijl. li AiiJ j : druVandIh:,
                                                                                                                                                                                        -OJ       X
                                              Lj^U-L.jI,                                                                                          L'_       i_-^__   It 4a b a j   I
                                                                                                                                                                                       j                                     TTf
```


## [2026-09-05T20:15:43.450Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Lüge ===\"; grep -n \"Lüge\" HRN.txt | head -10\necho \"=== HUB Lüge/drug ===\"; grep -n \"Lüge\" HUB.txt | head -10\necho \"=== IEC dhreugh/dhrougho ===\"; grep -n -i \"dhreugh\\|dhrough\\|dhregh\\|dhragh\" IEC.txt | head -20\necho \"=== CHEUNG draug ===\"; grep -n -i \"draug\\|\\*drau\\|drug\" CHEUNG.txt | head -20",
 "description": "Grep Horn, Hübschmann, Mann, Cheung"
}
```


### [2026-09-05T20:15:43.538Z] TOOL RESULT

```
=== HRN Lüge ===
5015:557. iliiröy, deröy 'Lüge; unwahr.
5016:ap. drauga- *Lüge*; i\\^\ draoya'\ phlv. dröy, dröy,
5945:674. zur 'falsch; Lüge*.
=== HUB Lüge/drug ===
=== IEC dhreugh/dhrougho ===
3059:dhrag- ‘flog, torture’. Cf. dhragh- & dhragh- OE dreccan, id. beside dracu, s.; Latv. dragáju “beat, shatter’, cf. dragulis ‘ague’
3060:dhrághó, ið ‘harass’. Cf. dhràgh- (2) and dhraghoó Gk. thrásso, Hom. pf. té-trékha ‘disturb’; Skt. draghe “strain, torture oneself; Tokh. tsárk-, B tsark- ‘harass’; OCS draZo, dražiti “irritate”
3062:dhrágh- (2) “rough, raw, rugged". Cf. dhrgh- Oss. dárzüg ‘rough, raw? beside dirzun, v. ‘tub’; Gk. trakhüs trekhüs “rough, rugged. Variant in Ir. draighean ‘sloe’; Br. draen, dréan ‘thorn, fishbone’; Cor. drain, dren ‘thorn’; W draen, id. (all fr. *dhraghino-). E-gde cf. Gk. trékhnos “shoot? (Hes.)
3075:dhregh- ‘fall, drop; heavy, sluggish; fall, collapse. Sk. drahe, mp. ‘deposit’; Ir. dríog ‘drop, drop- let”; OHG tragi, MHG træge ‘sluggish’ beside MHG tràc-, -ges 'sluggishness' (LW in Du. traag); Li. drégnüs ‘muggy’; dregstu, dregti ‘get muggy’; Latv. dregs ‘thaw, slush’; dregns ‘damp’. Cf. (short-grade) Ir. dreoghaim ‘rot, decay’
3077:dhregho ‘turn’. WP I, 874. See dhr$h- Arm. cf. (z-gde) dardz, Let ‘turn’; dardznem, v. id.; Gk. trékho, fut. mp. thréxomai ‘run, hasten’; (o-gde in) trokhós “wheel, hoop’; and trókhos ‘course, race’; trokholós ‘rolling; rapid’; Alb. dredh, aor. drodha Ge: -e-)
3085:“twist, turn, spin (tr.); Ir. cf. (?) dreas (“bout, turn”, if for *dhre&hso-) (dhrën-, see dhrān-. Vocalism ambiguous in Gk. & Gmc.) Gk. cf. ten-thréne (‘bee or *wasp"); an-thrén& ‘wild bee’; thrénos ‘dirge; OS dràn, Let ‘drone’; OE dræn beside dran, id. (*-oi-?) dhreng- (dhrong-) "wer Go. drigkan, OHG trinkan, etc. («drink', and com. Gmc.); Li. drengiü, ti ‘sleet, pour w. rain’; o-gde in Sw. drank ‘mash; barm’ as well as in G Ge-trank, E to drench, etc: R (Ð cf. driàzgi ‘dirt; twaddle’ (but Pol. drzazga “chip, splinter, log? may be of Wh. R. origin) dhrengh- “slow, sullen, sad, limp, hanging”. Cf. WP I, 813 Per. dirang ‘slow’; Tokh. A trànk-, B treñk- ‘hang’; W dreng, adj. ‘surly’; R cf. drjàgat, drjagnüt ‘dangle’; Li. drengiü, ti (1) “wear out dhrésó, ið (?) “shout, rave’ Gk. thréo ‘shriek’; ON dræsa, f. ‘twaddle’; Latv. cf. (o-gde) draséju ‘yodel, jubilate? dhreudo, io, dhroud-, dhrud- “bully, illtreat, threaten’. Cf. WP I, 870 NG triezen ‘twist, tug, bully); MHG (z-gde) trutzen ‘defy’; Li. (o-gde) draudžiù, draüsti ‘warn, ban’; Latv. draudu, ét ‘threaten’ dhreugh- (1), dhrugh- ‘harm, deceive’. Cf. WP I, 860 & 874 Skt. drohah ‘harm, wrong’; drühyami ‘hurt, offend’; Av. druž- ‘deceive’ beside druxš-, o-gde in draoxš-, id.; LW in Arm. držem, id.; MHG (regen, id. beside (z-gde) troc, gs troges ‘deceit; OS driogan; Du. be-driegen *cheat'; Av. cf. draoyo; Per. durüy ‘falsehood’ dhreugh- (2), dhrough- “good, fit, sprightly, pleasant'. See dhrough- Lat. cf. ? fruor (ambig. ‘enjoy’, if distinct from früx, -gis, frügalis, etc. See bhrüg-); Br. dréó ‘gay, tipsy’; OE dreog ‘fit, sober, serious, gentle beside dréogan ‘behave, experience’; ON drjúgr ‘substantial, lasting’; Li. (o-gde) draugùs ‘sociable’ dhreus- ‘crumble, fall; crumb, fragment(sy Arm. cf. eyğiwr (2) ‘husks’; OE drēosan, v. ‘fall, perish’; drēor, m. ‘blood’; Ukr. cf. dru-
3107:dhro£hos, à ‘turn; going; wheel". Cf. dhregho : Gk. trókhos ‘course’; trokhós *wheel'; MIr. droch *millwhee?'; OE drag ‘crowd, tumult’; OHG traga, MHG trage *bearer, carrier, ve- hicle, holder’. Isophonic, and here only if Go. (and com. Gmc.) vb. dragan, pf. *drog can be equated with Gk. trókhos: trokháo (Iliad)); E dray (ME id.) reflects the R drógi ‘dray, hearse’, droga ‘carriage shaft" only if the latter is a Gmc. LW. Preobr. untenable qua ‘shaker’
3108:dhrógh- “stripe, streak, line’. Cf. dhrég- and dhregh- ON dróg, id. Li. druoZé, id. beside druoZle ‘shaving’
3117:dhroughos dhrugh-) (1) *'comradely; com- rade, friendship, band'. WP I, 860 Skt. cf. (z-gde) druhah 'son'; LLat. dructis ‘escort’; OE dryht (1) ‘company, band be- side ge-dréag, id. (o-gde); ON draugr (1) "warrior; OCS drugü ‘friend’; Li. draügas, Latv. draugs, id. (LLat. dructis is prob. a Gmc. LW); LG droog ‘bold’ (probably here)
3118:dhroughos (2) *bad, evil, shrunken, wizened; evil person or thing’. WP I, 874 Skt. drohah “injury treachery’; Av. draoyo adj. lying'; s. ‘lie’; Ober drauga-, id.; ON draugr ‘wraith’; Icel. draugur, id. (and 'slug- gard"); Sw. (?) dröja, OSw. dróghia ‘hesitate’; OE cf. dréahnian, v. (to drain? in relation to drügop 'drought and dryge ‘dry’; Dutch droog, id.). (The semantic links are obscure. Isophonic with OCS etc. drugü “other?)
3137:dhrugh- (2) “associate”, etc. See dhrough- (1)
3140:dhrugh- (3) “evil”, etc. Cf. dhrough- (2) and dhreugh- (1) Skt. drühyami “hurt; hate? beside (o-gde) drohah ‘harm’; Av. druž- ‘cheat’; DW in Arm. dr£em, id.; OPer. duruj-, v. “lie, cheat; durüy Jie; OHG (e-gde) bi-triugan “cheat? beside trug-, cpds. ‘deceptive’; (LW in) Hung. ördög ‘devil’
3173:dhrgh- ‘crush’, etc. Ambiguous as a basis for Gk. thrásso, (see dhragh- & for the Slav. types Pol. dziergac ‘thrash’; Cz. drhat ‘scour’; R dérgat ‘pluck: twitch’; Blg. drágvam, drágna ‘scrape, scrub’ see drgh-. Li. dree ‘ache, pang’ equates with Ir. driog, id. but under what caption is uncertain see dhrigho, itself un- certain).
6234:Lat. cf. dom-inus; Go. kindins (‘governor fr. a type *$entinos); cf. also Go. piudin-assus (kingdom', but piudans ‘king’; OHG truhtin, OS druhtin, OE dryhten (*lord', cf. dhreugh- (2))
=== CHEUNG draug ===
4960:*drauH. 
5977:*drau2 77 
6010:*drau! *to call on' 
6026:served all three meanings, on which see also *drau’, *drau’. 
6036:*drau? ‘to run’ 
6045:78 *drau3 
6061:*drau ‘to lead astray, delude’ 
6090:(= Ir. *drau’), Pkt. dhutta- (m.) ‘villain, rogue’. > EWAia I: 802, s.v. dhvar 
6092:© This root should be separated from *drau^ ‘to run’ (?), on which see Schwartz 
6103:*draub ? ‘to scratch, peel off ?' 
6112:*drauH 79 
6119:dropt ‘to tear, scratch; to comb’. > If Oss. reduvyn, etc. does contain *draub, we 
6138:*drauH ‘to cut (down), mow, reap’ 
6174:80 *drau(H)s ? 
6177:*drau(H)S ? ‘to make a mark, brand’ 
6198:Q The evidence for the root *drauš is somewhat ambiguous, particularly, 
6203:ingressive s-formation of a root *dreuH-, which is attested in IIr. only (*drauH): 
6212:*drauj ‘to lie, deceive’ 
6266:*drauš ? ‘to grind’ 
6275:© In ESIJa П: l.c., a root *draus is reconstructed, with the meanings ‘to break in
```


## [2026-09-05T20:15:48.976Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 557 ===\"; sed -n '5010,5025p' HRN.txt\necho \"=== CHEUNG *drauj ===\"; sed -n '6212,6266p' CHEUNG.txt",
 "description": "Read Horn 557 and Cheung *drauj"
}
```


### [2026-09-05T20:15:49.044Z] TOOL RESULT

```
=== HRN 557 ===
kurd. dirün, dirütin erndten', dirün 'Erndte*; wa/.
drdw-am.
Das 3 in jüd.-pers. )x5l*n zwingt direivem zu lesen
und mit Spiegel, Arische Periode, 70 gr. Ooftko
'pflücken* zu vergleichen.
557. iliiröy, deröy 'Lüge; unwahr.
ap. drauga- *Lüge*; i\\^\ draoya'\ phlv. dröy, dröy,
LW. kurd, durüy; af/. daröy; bei. davöy^ drög,
n. dröy (49).
558. dnrüne 'Regenbogen'.
skr. drum- 'Bogen' (spät und selten).
bei. drm, drmuk 'Regenbogen* (85); yidg. LW.
drün,
bei. drin beweist, dass die ebenfalls überlieferte
np. Aussprache dnrüne falsch ist, vergl. Hübsch-
mann, ZDMG. 44, 555.
=== CHEUNG *drauj ===
*drauj ‘to lie, deceive’ 

*AVESTAN: druj- (druZ-) ‘to lie, deceive’ (on Z- < *ji- see Martínez 1999: 127 f.) || + 
*abi-) ‘to deceive, lie to someone’ || (+ *a-) “id.” > Liste: 32 

Pres. ja-: IND. med. 3sg. YAv. druZaite (N 84), 3pl. YAv. druzinti (Yt 10.45), SUBJ. 3sg. YAv. druzat 
(Yt 10.108), 3pl. YAv. “aißi.druZänti (Yt 5.90); Partic.: pres. OAv. “ädrujiiant- (31.15), YAv. druZint- (Yt 
8.5, Yt 10.107), perf. pass. Y Av. anadruxta- ‘not-cheated, indeceivable' (Yt 10.23, Yt 10.26, FrW 9.1) 
*OLD PERSIAN: d(u)ruj- ‘to lie, deceive’ = Kent: 191b 

Pres. ja-: impf. IND. 3sg. ad(u)rujiya <[a]-du-u-ru-u-ji-i-y> (DB 1.39), <a-du-u-ru-u-ji-i-y> (DB 1.78, 
DB 3.80, DB 4.13, 4.18, etc), <[a]-[du]-u-ru-u-ji-i-y> (DB 4.8), <a-du-u-ru-u-ji-i-y> (DB 4.10), 
«[a]-du-[u]-[ru]-[u]-[ji]-i-y^ (DB 4.16), <a-du-[u]-ru-u-ji-i-y> (4.21, DB 4.21) (etc.), 3р1. ad(u)rujiyasa" 
<a-du-u-ru-u-ji-i-y-S> (DB 4.34); Partic.: perf. pass. d(u)ruxta- <du-u-ru-u-x-t-m> (DB 4.44), 
<du-u-ru-u-x-t-m> (DB 4.49), «[du]-[u]-[ru]-[u]-[x]-t-» DNb 52, 55), (adv.) d(u)ruxtam ‘falsely’ 
<[du]-[u]-[ru]-[u]-[x]--m> (DB 3.89) 

*MIDDLE PERSIAN: MMP drwz-, ВМР dlwc- /dröz-/ ‘to deceive, break (contract)’ 
c DMMPP: 14la 


*duai ? 81 


Pres.: IND. 35р. (?) MMP drwzyd, BMP dlwoyt /drozed/, 3р1. BMP dlwcynd /drözend/, SUBJ. 3р1. MMP 
drwz’nd, IMPV. 2р1. BMP diwcyt /drozed/; Partic.: perf. pass. BMP diht /druxt/ 


*PARTHIAN: drwj- ‘to Пе” = Ghilain: 95 | DMMPP: 140b 

Pres.: IND. 3pl. drwjynd; Partic.: perf. pass. drwxt-myhr ‘who breaches a contract’ 

*KHOTANESE: drruja- ‘falsehood’ 

*SOGDIAN: BSogd. órymh (f), CSogd. žym- (Е), MSogd. jym’ ‘lie, falsehood’, 
BSogd. örym’s’k, CSogd. Zym’syt (pl.) ‘liars’ 

*BACTRIAN: dpoyo, pwyo ‘falsehood, deceit’, öpwyonıyo ‘false’ = S-W, Bact.: 
190a, b 

*NWIR: NP durög, Bal. d(a)rog, Kurd. (Kurm.) daraw (f.), (Sor.) diro, Abyan. dor, 
Abz. durü, Ard. duru, Khuns. duru, Nn. duru, Qohr. derü, Tal. dü, Kash. dürü ‘lie’ 
*MISC: Огт. drist, daresi ‘lie(s)’, Arm. (LW) drzem ‘I lie’ 

*SANSKRIT: drogh ‘to deceive, deceit? (RV+) = EWAia I: 760 

«PIE *d’reug"- ‘to deceive, deceit? > LIV: 157 | Pok.: 276 


*IE COGNATES: OHG triugan, OE driogan ‘to deceit’ 
*REFERENCES: IIFL I: 393a; WIM I: 351; Nyberg II: 66b; DKS: 168b; Werba 1997: 199; Cabolov 2001: 
274; Lecoq 2002: 575b, 593a, 616a (passim); ESIJa II: 466 ff.; Korn 2005: 205, 373 


*drauš ? ‘to grind’
```


## [2026-09-05T20:16:09.624Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 dherāgh ===\"; grep -n \"dherāgh\\|dherăgh\\|dherägh\\|dhragh\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== WLD Bd1 dhreugh ===\"; grep -n \"dhreugh\\|dhrougho\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== WLD band3 index ===\"; grep -n \"dherāgh\\|dhreugh\\|dherägh\" WLD_band3.txt | head -10",
 "description": "Grep Walde-Pokorny"
}
```


### [2026-09-05T20:16:09.692Z] TOOL RESULT

```
=== WLD Bd1 dherāgh ===
54364:Vf. IF. 19, 106, LEWb. 2 s. v.) auf dhragh- zuriickgehn, aber auch idg. t- 
54964:auch in der Wzf. dhreu-gh- begegnet ( dlmer-gh - : dhurgh : dhragh-, dhreugh-)-, 
=== WLD Bd1 dhreugh ===
54964:auch in der Wzf. dhreu-gh- begegnet ( dlmer-gh - : dhurgh : dhragh-, dhreugh-)-, 
55083:dhreugh dhregk- 
55098:dhreugh- „triigen, listig schadigen". 
55114:Idg. *dhreugh- ist sehr wahrseheinlich verwandt mit *dhuer- „durch 
55116:*dhur-gh- sich neue Hochstufen idg. dhreugh -, dhrough- einstellten. Mit 
=== WLD band3 index ===
```


## [2026-09-05T20:16:10.514Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN drink ===\"; grep -n \"5\\.13 DRINK\\|DRINK (vb\" SYN.txt | head -5\necho \"=== SYN lie/falsehood ===\"; grep -n \"16\\.6[0-9]\\|FALSE\\b\" SYN.txt | head -10",
 "description": "Grep Buck synonyms"
}
```


### [2026-09-05T20:16:10.577Z] TOOL RESULT

```
=== SYN drink ===
8422:5.13 DRINK (vb.)
=== SYN lie/falsehood ===
5093:Russ. ochotit’sja refl. (with na ‘on’ when used transitively) fr. ochata ‘de- sire, will, hunt, chase, sport’ : chotét’, ChSI. chotéi ‘wish’ (16.61). For the change ‘desire’ > ‘hunt’, cf. Skt. lubdha- ‘greedy’, as sb. ‘hunter’. Berneker 398 f.
19195:Dan. tryg, Sw. trygg: ON tryggr, Goth. triggws, OF triewe, OHG gi-triuwi, etc. ‘true, trustworthy’ (16.66). Falk- Torp 1290.
19307:In the Romance languages generally ‘to harm’ is most commonly expressed by phrases, as It. far male, Fr. faire (du) mal, Rum. face réu, all lit. ‘do ill’ (ef. ‘bad’ 16.62). Similarly, after French, Br. ober drouk, etc. and Du. kwaad doen.
19313:m ; es with ol¢ ‘pad’ (16.62). For lor-
19315:Br. ober drouk, ober gwall do ill’ (like fr. faire mal), phrases with words - ‘had’ (16.62), also ober gaow ‘do wrong (ike Fr. faire tort) with gaow ‘false, wrong, 2 lie’ (16.71).
19318:Goth. ga-sleibjan, lit. ‘endanger’ : dips ‘dangerous, bad’, sleibi ‘danger’, Ha ‘dangerous, cruel’, etc. (16.65). te eo ME harme, NE harm, : a OE hearm ‘hurt, injury, harm’ tu, face a fe one harm ; ef tts, coe se ‘ NEG harm but root connection? - Samu shame’, . a a Walde-P. 1.463, NY inj: fh a fits Dack-formation to injury Tight, law? Wrong, injustice’ : izs
21343:Words for ‘remain, stay’ (in one place as opposed to ‘move, go’) coincide in part with those for ‘remain’ = ‘be left over’ (12.17), the development being mostly from the first to the second, but sometimes the opposite. Furthermore, just as words for ‘remain’ may be used for ‘await, wait for’ (as Grk. pévw Hom. Il. 16.620, etc., Lat. manére hostem, OPers. mam amdanaya ‘awaited me’), so conversely there is a group of words which, from such notions as ‘watch, look for, hope for’, have come to mean ‘wait for’ and may then be used also intransi- tively for ‘wait’ closely approaching ‘re- main, stay’. Hence such words are added in the list, even though most of them are still distinguished in feeling and range of use from those given in the first place.
23419:ON tala, Dan. tal, anial, Sw. antal, OE getel, ME tale (OE talu only ‘ac- count, tale’), Du. getal, OHG zala, MHG zal(e), NHG zahl : ON tala ‘speak, talk’, OE italian ‘consider, reckon, account’, OHG zalén ‘count, relate, pay’, etc., (perh. Grk. 560s, Lat. dolus ‘guile, de- ceit?, but see 16.68). Walde-P. 1.808. Falk-Torp 1243. Walde-H. 1.366.
27365:influenced by the more common @ode- pos ‘muddy, turbid’, esp. of water, etc.. but also ‘dirty’ (cf. téare vite Porepav adivbov, Theocr. 16.62), deriv. of 86dos ‘mud, dirt’.
27460:16.61 Wrz, Wiss (vb.)
```


## [2026-09-05T20:16:15.188Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"16.71 \" SYN.txt | head -5\necho \"---\"\nawk 'NR>=8422 && NR<=8440' SYN.txt",
 "description": "Buck 16.71 and 5.13"
}
```


### [2026-09-05T20:16:16.894Z] TOOL RESULT

```
29618:16.71 GOOD (adj.)
---
5.13 DRINK (vb.)
Lith.  gerli Lett. dzert Chsl.  piti SCr. pitt Boh. pili se) a 170d Russ. pit’ Skt. pa- Av. 2’ar-
‘move, glide’). Cf. also Toch. A tsuk- ‘drink’ : Lat. dicere ‘draw, lead’, etc. Walde-P. 1.874. Feist 125. G.S. Lane, Language 14.27.
3. Lith. gertz, Lett. dzert : ChSl. zrétz, Skt. gr-, Lat. vorare, Grk. BiBpooxw, LE *gver- ‘swallow, devour’. Walde-P.. 1.682 ff.
4, Av. x’ar- ‘consume, eat, drink’, x’asar- ‘a drinker’, see 5.11.
The words for the sb. ‘drink’ are near- ly all obvious derivs. of the roots appear- ing in the verbs, as Grk. wGpa, roots, Lat. potid, potus, NHG getrank, etc. Those of different orig. are as follows:
Ir. deog, Nir. deoch, W. diod, MW diawt, OCorn. diot, MBr. diet, orig. ob- scure. Walde-P. 1.786. Stokes 146.
Ir. lind (NIz. lionn ‘ale’), W. llyn, prob. the same word as Ir. lind (s-stem), W. llyn ‘lake, pond’ (1.48). Pedersen 1.37. Persson, Beitriige 878. But sepa- rated by Walde-P. 2.438.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
332 SELECTED INDO-EUROPEAN SYNONYMS 5.14 HUNGER (sb.) Grk. ids, xetva Goth. hithrus, grédus Lith. alkis, badas NG weiva ON hungr Lett. izalkums, bads Lat. famés Dan. hunger ChSl. glad It. fame Sw. hunger SCr. glad Fr. faim OE hungor Boh. hlad Sp. hambre ME hunger Pol. gléd Rum. /foame NE hunger Russ. golod Ir. gorle Du. honger Skt. kgudh-, ksudha- Nir. ocras, goria OHG hungar Ay. $ud- W. newyn MHG hunger Br. naon NHG hunger
Words for ‘hunger’ come by speciali- zation from either ‘want, distress, wast- ing away’ or ‘desire, longing’. Cf. the specialization of NE starve from OF steorfan ‘die’.
1. Grk. Atpds : Aowwds ‘plague’, Ard- fouat ‘withdraw, shrink’, Goth. aflinnan ‘depart’, ON linna ‘cease’, etc., IE *lez-. Walde-P. 2.388. Whatever the ultimate relations of the various IE roots *lei-, the immediate Greek development is fr. ‘waste away’ to ‘hunger’.
Grk. weiva, Ion. zelvy, fr. *réa: Grk. revia ‘poverty’, xévns ‘poor’, mévouat ‘toil, be poor’, xévos ‘toil’, outside con- nections dub. Walde-P. 2.8 f., 661.
2. Lat. famés (> Romance words) etym. dub. Walde-P. 1.829. Ernout- M. 328f. Walde-H. 1.451.
3. Ir. nina, NIr. naoine ‘famine’, W. newyn, Br. naon ‘hunger, famine’, OCorn. naun (gl. famis), prob: Goth. naups, OHG not, OE néad ‘necessity, distress’ (NE need). Walde-P. 2.316. Pedersen 1.61. Stokes 193.
Ir. gorte, NIr. gorta : Ir. goirt ‘bitter, painful’, fr. the root of gorim ‘heat’, ChSI. goréti ‘burn’, etc. (1.85). Walde- P. 1.688. Pedersen 1.33.
NIr. ocras, cpd. of od- and root of
caraim ‘love’. Pedersen 1.476.
```


## [2026-09-05T20:16:23.086Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=8412 && NR<=8424' SYN.txt\necho \"=== 16.66 TRUE / 16.68 deceit ===\"; grep -n \"16.68 \\|16.66 \" SYN.txt | head",
 "description": "Buck drink context"
}
```


### [2026-09-05T20:16:24.852Z] TOOL RESULT

```
eo drigkan, OE drincan, etc., cally th ag etym. disputed. Semanti- Hei ve. fr, ‘draw’ (cf. NE take a ite a diicere pocula, sucds, etc.) connection attractive, and so ultimate ee D with OE dragan ‘draw’, etc.,
% nasalized form of a parallel
Toot (* ( dhreg. Perh. seen in Skt. dhraj-
D DRINK; COOKING AND UTENSILS
Digitized by Arya Samaj Foundation Chennai and eGangotri
331
‘rub’, etc. Walde-P. 1.731. Trautmann 327. Briickner 518, 575.
9. Skt. anna-, Skt., Av. pitu-, above, 1, 2.
Av. x*arafa-, fr. *z*ar- ‘consume’ (5.11). Hence Arm. xor ‘food’ (Hiib-
schmann, Arm, Gram. 160).
5.13 DRINK (vb.)
Lith.  gerli Lett. dzert Chsl.  piti SCr. pitt Boh. pili se) a 170d Russ. pit’ Skt. pa- Av. 2’ar-
‘move, glide’). Cf. also Toch. A tsuk- ‘drink’ : Lat. dicere ‘draw, lead’, etc. Walde-P. 1.874. Feist 125. G.S. Lane, Language 14.27.
=== 16.66 TRUE / 16.68 deceit ===
27465:16.66 Tru
27467:16.68 Dercrir
29408:16.66 TRUE (Or in part sb. Truth)
29473:16.68 DECEIT
```


## [2026-09-05T20:16:44.537Z] TOOL CALL #44: Bash

```json
{
 "command": "ls site/pages/135.jpg 2>/dev/null; SC=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; mkdir -p $SC; pdftoppm -f 135 -l 135 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $SC/pg135 && ls -la $SC/",
 "description": "Render PDF page 135"
}
```


### [2026-09-05T20:16:46.926Z] TOOL RESULT

```
site/pages/135.jpg
total 13276
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:16 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
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
-rw-rw-r-- 1 sfmqrb sfmqrb     395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
```


## [2026-09-05T20:16:49.834Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg135.png"
}
```


### [2026-09-05T20:16:50.183Z] TOOL RESULT

```

```


## [2026-09-05T20:16:50.179Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:17:13.588Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%B4%DA%A9%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%D8%BA' \\\n 'https://www.etymonline.com/word/dream' \\\n 'https://www.etymonline.com/word/droshky' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dragan%C4%85' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/drinkan%C4%85' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 135: roots Dhragh 1/Dhreg (droshky, draw, drink) and Dhreugh (dorugh, dream)' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:18:26.167Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f7269ab1dfa972bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/357b80095e69252d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/67ad7faea47b6d39.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b04e4f1271670c7b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa7ef26de4737508.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcf63fdca11fe0f2.txt
```


## [2026-09-05T20:18:28.958Z] TOOL CALL #47: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:18:29.000Z] TOOL RESULT

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


## [2026-09-05T20:19:33.387Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:26:25.616Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_DORESHKE = \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%B4%DA%A9%D9%87\"\nW_DOROUGH  = \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%D8%BA\"\nE_DREAM    = \"https://www.etymonline.com/word/dream\"\nE_DROSHKY  = \"https://www.etymonline.com/word/droshky\"\nW_DRAGAN   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dragan%C4%85\"\nW_DRINKAN  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/drinkan%C4%85\"\n\ndoc = {\n \"pdf_page\": 135,\n \"book_page\": 105,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 2,\n   \"root\": \"Dhragh 1, Dhreg\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *dʰregʰ- (Pokorny dherā̆gh-) 'to draw, drag along the ground'; beside it PIE *dʰreǵ- (Pokorny dhreg̑-) 'to draw, glide', with nasalised *dʰrenǵ- 'to drink'\",\n   \"note\": \"Nourai's root box merges TWO Pokorny entries under one heading and one citation. POK 257 has 'dherā̆gh- ‚ziehen; am Boden schleifen‘, gleichbed. mit tragh-' (ON draga, Goth./OE dragan, Russ. doróga 'Weg'), which covers nodes 1-5. The drinking node belongs to a different entry, POK 273 'dhreg̑- ‚ziehen; dahinziehen, gleiten, streifen‘' with 'nasaliert dazu vielleicht got. drigkan, aisl. drekka, ags. drincan, ahd. trinkan ‚trinken‘ (einen guten Zug machen, ducere pocula)'. The two roots differ in the final velar (velar gh vs palatal ǵ) and cannot be strict variants of each other; Nourai follows Watkins/AHD, who prints 'dhragh-. To draw, drag on the ground … See also variant form dhreg-' and 'dhreg-. To draw, glide. Variant form of dhragh-', i.e. AHD itself calls them variants. The gloss 'to pull' and the label Indo-European are correct for both. Verdict plausible: the root and its language are real, the equation of the two roots is a simplification that Pokorny (and modern Wiktionary, *dʰregʰ- vs *dʰreǵ-) does not make.\",\n   \"note_fa\": \"جعبهٔ ریشه در واقع دو ریشهٔ جداگانهٔ پوکورنی را در یک قاب آورده است: در صفحهٔ ۲۵۷ «dherā̆gh- کشیدن، بر زمین کشیدن» که واژه‌های ژرمنی dragan و روسی doroga از آن است، و در صفحهٔ ۲۷۳ «dhreǵ- کشیدن، لغزیدن» که صورت خیشومی‌شدهٔ آن (drinkan) به معنی «نوشیدن» است. پایان‌واکهٔ این دو یکی نیست (یکی kʰ کامی و دیگری غیرکامی)، پس از دید سخت‌گیرانهٔ آواشناسی تاریخی نمی‌توان آن‌ها را گونهٔ یکدیگر شمرد؛ اما واتکینز در پیوست ریشه‌های هندواروپاییِ فرهنگ American Heritage خودْ این دو را «صورت‌های گونه‌گونِ هم» خوانده و نورایی از او پیروی کرده است. معنای «کشیدن» و برچسب «هندواروپایی» درست است، ولی یکی‌گرفتن دو ریشه ساده‌سازی است؛ بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\": [W_DRAGAN, W_DRINKAN],\n   \"ref_check\": [\n    {\"ref\": \"POK:257\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 268 (printed p.257): headword OCRed as 'rSzb’ ;ziehen; am Boden schleifen^, gleichbed. mit tragh- (s. d.)' = dherā̆gh-; the entry then lists 'Anord. draga, got. u. ags. dragan, engl. draw ‚ziehen‘ … Wohl hierher sl. *dārgā in: … russ. doróga ‚Weg, Reise‘ … Lat. trahō ‚ziehe‘'. Supports the root, the Germanic node and the Slavic (Russian) node — but this page says nothing about 'drink'; that is POK 273 dhreg̑- (POK_01.txt leaf 284, printed p.273).\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, AHD_watkins1985.txt lines 386-387\", \"stance\": \"supports\",\n     \"note\": \"'dhragh-. To draw, drag on the ground. Rhyming variant tragh-. 1. Germanic *dragan … DRAW … DRAG … DRAY … DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 257.]' and 'dhreg-. To draw, glide. Variant form of dhragh-. 1. Nasalized Germanic form *drinkan, to draw into the mouth, drink … DRINK. 2. Nasalized Germanic form *drankjan … DRENCH … DROWN. [Pok. dhreg- 273.]' — this is plainly Nourai's model for the whole chart.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 862 (WLD_Bd1 djvu line 54364 area)\", \"stance\": \"supports\",\n     \"note\": \"Walde-Pokorny I 862 is the source Pokorny 257 abridges; the local OCR shows the cross-reference '… auf dhragh- zurückgehn, aber auch idg. t-' in the discussion of Lat. trahō.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt lines 3107-3108 (dhroǵhos, dhrógh-)\", \"stance\": \"partial\",\n     \"note\": \"Mann sets up 'dhroǵhos, ā ‘turn; going; wheel’ … OE drag ‘crowd, tumult’; OHG traga … Isophonic, and here only if Go. (and com. Gmc.) vb. dragan, pf. *drōg can be equated with Gk. trókhos … E dray … reflects the R drógi ‘dray, hearse’, droga ‘carriage shaft’ only if the latter is a Gmc. LW' — i.e. Mann keeps the same word-family together but is explicitly unsure of the equations; and he puts the drink-words in a separate root 'dhreng- (dhrong-) … Go. drigkan, OHG trinkan' (line 3085).\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 5.13 DRINK (SYN.txt line 8412 f.)\", \"stance\": \"partial\",\n     \"note\": \"'Goth. drigkan, OE drincan, etc., etym. disputed. Semantically, deriv. fr. ‘draw’ (cf. NE take a drink, Lat. dūcere pocula, sucōs, etc.) connection attractive, and so ultimate connection with OE dragan ‘draw’, etc., as nasalized form of a parallel root (*dhreg-). Perh. seen in Skt. dhraj- ‘move, glide’ … Walde-P. 1.874.' — Buck states exactly Nourai's picture but labels it disputed.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Russian\", \"words\": \"drožki\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Russian дрожки drožki 'light open four-wheeled carriage' is a diminutive plural of дроги drogi 'wagon, dray, hearse' (sg. дрога 'the long perch/shaft that joins the axles of a cart'), and дрога belongs with дорога doroga 'road' < Common Slavic *dorga — the group Pokorny 257 lists under dherā̆gh- ('russ. doróga ‚Weg, Reise‘, russ. dorožitь ‚aushöhlen‘'). The vehicle is named from its shaft, the thing that is 'drawn', exactly as English wain/wagon is named from way; Klein makes that comparison explicitly. The chart draws the arrow straight from the PIE root, which telescopes the real chain PIE *dʰregʰ- > Common Slavic *dorga/*dorgy > Russian drogi > diminutive drožki (a modern Russian formation, 18th c., the vehicle itself being a Moscow/Petersburg cab of that period), but the affiliation is the standard one.\",\n     \"derivation_fa\": \"واژهٔ روسی «дрожки» (drožki) نامِ نوعی کالسکهٔ سبکِ چهارچرخِ روباز است و از نظرِ ساخت، مصغّرِ جمعِ «дроги» (drogi) «گردونه، ارابه» است؛ و این واژه با «дорога» (doroga) «راه» از سلاویِ مشترکِ *dorga پیوند دارد که پوکورنی در صفحهٔ ۲۵۷ زیرِ همین ریشه آورده است. نامِ این گردونه از «تیرِ کشش» آن گرفته شده است، همان‌گونه که در انگلیسی wagon با way پیوند دارد (کلاین همین مقایسه را می‌کند). نمودار پیکان را یکسره از ریشهٔ هندواروپایی به روسی می‌کشد و حلقه‌های میانی (سلاویِ مشترک *dorga > drogi > drožki، که ساختی نو و مربوط به سدهٔ هجدهم میلادی است) را نادیده می‌گیرد، ولی خودِ انتساب درست و پذیرفتهٔ همگان است.\",\n     \"sources\": [E_DROSHKY, W_DORESHKE],\n     \"ref_check\": [\n      {\"ref\": \"AHD:400\", \"status\": \"supports\",\n       \"note\": \"The page number is in the main word-list of the AHD New College Edition (not held locally); the IE-roots appendix of the same dictionary, which is the substance of the claim, says it verbatim: Watkins 1985 s.v. dhragh-, '2. Russian drogi, a wagon: DROSHKY' (AHD_watkins1985.txt line 386).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 257 (POK_01.txt leaf 268)\", \"stance\": \"supports\",\n       \"note\": \"'Wohl hierher sl. *dārgā in: serb.-ksl. draga ‚Tal‘, russ. doróga ‚Weg, Reise‘, dial. ‚Angel‘ … poln. droga ‚Weg, Straße, Reise‘' — the Slavic branch of the root, from which drogi/drožki come.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. droshky (KLN_1966.txt line 12311)\", \"stance\": \"supports\",\n       \"note\": \"'droshky, also drosky, n. — Russ. drozki (pl.), dimin. of drogi (pl.), ‘wagon’, rel. to doroga … ‘way’, and cogn. with Norw. drag, ‘drawing rope’, and with ON. draga, ‘to draw’; see drag, draw.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. dhroǵhos (IEC.txt line 3107)\", \"stance\": \"partial\",\n       \"note\": \"Mann knows 'the R drógi ‘dray, hearse’, droga ‘carriage shaft’' in this family but warns they belong here 'only if the latter is a Gmc. LW', i.e. he entertains a Germanic loan into Slavic instead of common inheritance.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"doroškeh «درشکه»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"درشکه doroške is a 19th-century Qajar-period loan from Russian дрожки drožki, taken over with the vehicle itself during the intensive Russo-Persian contact after the treaties of Golestan (1813) and Torkamānčāy (1828); the Russian plural was reanalysed as a singular and given the ordinary Persian final -e/ه, and the impossible Persian onset dr- was broken by an anaptyctic vowel (dr- > doro-), the same repair as in دورو/درنگ-type clusters. Mo'in's footnote in Borhan-e Qāṭeʿ p.837 states it outright: «درشکه، بضم اول و دوم و کسر چهارم، از روسی droške … گردونهٔ چهار چرخه که با اسب کشیده شود و اطاقکی برای حمل مسافر دارد»; a marginal remark there adds مأخوذ از آلمانی 'taken from German', i.e. possible mediation by German Droschke — but German Droschke is itself an 18th-century borrowing of Russian drozhki, so the ultimate source is Russian either way, and Wiktionary gives the Russian source with no German step.\",\n     \"derivation_fa\": \"«درشکه» وام‌واژه‌ای است از روسیِ дрожки (drožki) که در دورهٔ قاجار همراه با خودِ آن گردونه به ایران آمد؛ روزگارِ آن پس از عهدنامه‌های گلستان (۱۸۱۳م) و ترکمانچای (۱۸۲۸م) و گسترشِ داد و ستد با روسیه است. جمعِ روسی در فارسی مفرد فهمیده شد و «هِ» پایانیِ فارسی گرفت، و چون خوشهٔ آغازینِ dr در فارسی روا نیست واکهٔ میانجی افزوده شد (drožki ← دُرُشکه). معین در حاشیهٔ برهان قاطع، ص ۸۳۷، همین را می‌گوید: «درشکه، بضم اول و دوم و کسر چهارم، از روسی droške … گردونهٔ چهار چرخه که با اسب کشیده شود». در همان حاشیه یادداشتی هست که آن را «مأخوذ از آلمانی» می‌خواند؛ اما آلمانیِ Droschke خود در سدهٔ هجدهم از روسی وام گرفته شده، پس سرچشمه در هر حال روسی است. ویکی‌واژه نیز یکسره آن را از روسی می‌گیرد. ادعای نورایی درست است.\",\n     \"sources\": [W_DORESHKE, E_DROSHKY],\n     \"ref_check\": [\n      {\"ref\": \"BQT:837\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 297 (= printed p.837 with the documented offset printed = leaf + 540): «۵ درشکه - بضم اول و دوم و کسر چهارم. از روسی droške … گردونهٔ چهار چرخه که با اسب کشیده شود و اطاقکی برای حمل مسافر دارد». Nourai's page number is exact — which also confirms the leaf→page offset used elsewhere on this page.\"},\n      {\"ref\": \"MON:1511\", \"status\": \"partial\",\n       \"note\": \"Only the 2-volume Adena abridgement of Moʿin is on disk; its entry (MON_part1.txt line 60490) reads «درشکه: droške ( گردونه چهار چرخه که با اسب کشیده شود و اطاقکی برای حمل مسافر دارد …» — the same gloss but WITHOUT an origin tag, so the abridgement neither confirms nor denies the Russian source; the 6-volume Farhang-e Fārsi p.1511 that Nourai cites was not accessible.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ ed. Moʿin, p.837 (v2 leaf 297)\", \"stance\": \"supports\",\n       \"note\": \"see ref_check: «از روسی droške»; marginal «مأخوذ از آلمانی».\"},\n      {\"src\": \"MON\", \"where\": \"Moʿin (2-vol abridgement), MON_part1.txt line 60490\", \"stance\": \"silent\",\n       \"note\": \"gives the word and its meaning, no etymology tag.\"},\n      {\"src\": \"ARY\", \"where\": \"grep 'درشکه' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"no hit — Aryanpur's dictionary of Indo-European roots of Persian does not treat this modern Russian loan.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"droshky\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English droshky (also drosky) is a direct borrowing of Russian дрожки drozhki, taken up in the 19th century from travellers' and diplomatic accounts of Russia, where it denotes the low open four-wheeled Russian cab; the Russian plural again became an English singular, and Russian ž was rendered by sh. Klein: 'droshky, also drosky, n. — Russ. drozki (pl.), dimin. of drogi (pl.), ‘wagon’'; Etymonline agrees ('from Russian drozhki, diminutive of drogi'). The chart's arrow Russian → English is exactly right.\",\n     \"derivation_fa\": \"«droshky» انگلیسی وام‌واژه‌ای است مستقیم از روسیِ дрожки که در سدهٔ نوزدهم از راهِ سفرنامه‌ها و گزارش‌های اروپاییان از روسیه وارد انگلیسی شد و همان کالسکهٔ کوتاه و روبازِ روسی را می‌رساند. جمعِ روسی در انگلیسی مفردِ droshky شد و ژِ روسی با sh نوشته شد. کلاین می‌نویسد: «droshky … از روسیِ drozki (جمع)، مصغّرِ drogi (جمع) به معنی گردونه»، و اتیمولوژی‌آنلاین نیز همین را می‌آورد. پس پیکانِ «روسی ← انگلیسی» در نمودار درست است.\",\n     \"sources\": [E_DROSHKY],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. droshky (KLN_1966.txt line 12311)\", \"stance\": \"supports\",\n       \"note\": \"'droshky, also drosky, n. — Russ. drozki (pl.), dimin. of drogi (pl.), ‘wagon’, rel. to doroga … see drag, draw.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, list of Russian words in English (SKT.txt line 23607)\", \"stance\": \"supports\",\n       \"note\": \"Skeat's appendix of borrowings lists 'Russian: drosky, morse, rouble (ruble), steppe, verst' — i.e. drosky is classed as a Russian loan.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1435)\", \"stance\": \"supports\",\n       \"note\": \"'DROSHKY dhragh-' in the word-to-root index, matching the appendix entry 'Russian drogi, a wagon: DROSHKY'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Germanic\", \"words\": \"dragan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *draganą 'to draw, pull' (strong verb, class VI) is the direct Germanic continuation of PIE *dʰregʰ-/*dʰrogʰ-e-ti: Gothic ga-dragan, Old Norse draga, Old English dragan, Old Saxon/Old High German tragan, which shifted in the German branch from 'draw' to 'carry' (whence NHG tragen). Pokorny 257 opens the entry with exactly this list ('Anord. draga, got. u. ags. dragan, engl. draw ‚ziehen‘ … mit der Bed. ‚tragen‘ (aus ‚schleppen‘) ahd. tragan'). Nourai's form 'dragan' is the Gothic/Old English shape used as the Germanic citation form, as in Watkins ('Germanic *dragan'). Caveat: Kroonen and Wiktionary note that the PIE etymology is not secure and leave the origin of *draganą open, since outside Germanic only the doubtful Latin trahō and the Slavic 'road' words are adduced.\",\n     \"derivation_fa\": \"ژرمنیِ آغازینِ *draganą «کشیدن» (فعل قویِ ردهٔ ششم) دنبالهٔ مستقیمِ ریشهٔ هندواروپاییِ *dʰregʰ- است: گوتیِ ga-dragan، نورسِ باستان draga، انگلیسیِ باستان dragan، و آلمانیِ علیای باستان tragan که در شاخهٔ آلمانی از «کشیدن» به «بردن، حمل کردن» تحولِ معنایی یافت (آلمانیِ امروز tragen). پوکورنی در صفحهٔ ۲۵۷ همین فهرست را در آغازِ مدخل می‌آورد. صورتِ «dragan» در کتاب همان صورتِ گوتی/انگلیسیِ باستان است که به‌جای صورتِ بازسازیدهٔ ژرمنی به کار رفته، چنان‌که واتکینز نیز می‌نویسد «Germanic *dragan». تنها نکتهٔ احتیاطی این است که کرونن و ویکی‌واژه ریشه‌شناسیِ هندواروپاییِ آن را قطعی نمی‌دانند و خاستگاه را باز می‌گذارند.\",\n     \"sources\": [W_DRAGAN],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. dhragh-: '1. Germanic *dragan in: a. Old English dragan, to draw, pull: DRAW; b. Old Norse draga … DRAG; c. Old English dræge, dragnet: DRAY; d. Old Norse *drahtr, dráttr, act of drawing … DRAFT.' (AHD_watkins1985.txt line 386).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 257 (POK_01.txt leaf 268)\", \"stance\": \"supports\",\n       \"note\": \"'Anord. draga, got. u. ags. dragan, engl. draw ‚ziehen‘ … mit der Bed. ‚tragen‘ (aus ‚schleppen‘ …), ahd. tragan ‚tragen‘'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Draw (SKT.txt line 5393)\", \"stance\": \"supports\",\n       \"note\": \"'Draw. (E.) M.E. drawen. A.S. dragan … + Du. dragen, Icel./Swed. draga, Dan. drage, Goth. [ga-]dragan, G. tragen, to pull along … Skt. dhraj, to lengthen, to exert (√DHARGH.)'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. draw (KLN_1966.txt line 12238)\", \"stance\": \"supports\",\n       \"note\": \"'draw … fr. OE. dragan, ‘to draw’, rel. to ON. draga … OHG. tragan, MHG., G. tragen, ‘to bear, carry’, Goth. ga-dragan, ‘to pull, draw’, and perh. cogn. with L. trahere.'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"draw, drag, draft\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are the English reflexes of *draganą that Watkins lists under this root. DRAW < ME drahen/drawen < OE dragan, with regular OE g > w after a back vowel. DRAG < ME draggen, either OE dragan again or, more probably, Old Norse draga borrowed in the Danelaw, the unshifted -g- pointing to Scandinavian transmission (Klein s.v. drag: 'ME. draggen, fr. OE. dragan or ON. draga'). DRAFT/DRAUGHT < ME draught 'a pulling, a drawing' < a Germanic *drah-tu- (ON dráttr), the -t- abstract to the same verb; 'draft' is the phonetic respelling that became standard in American use. Watkins: 'a. Old English dragan … DRAW; b. Old Norse draga … DRAG; … d. Old Norse *drahtr, dráttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT.'\",\n     \"derivation_fa\": \"هر سه واژه بازتاب‌های انگلیسیِ همان فعلِ ژرمنیِ *draganą اند و واتکینز هر سه را زیرِ همین ریشه آورده است. draw از انگلیسیِ میانهٔ drawen و آن از انگلیسیِ باستان dragan، با تبدیلِ قاعده‌مندِ g پایانی به w پس از واکهٔ پسین. drag از انگلیسیِ میانهٔ draggen است، یا از همان dragan یا — محتمل‌تر — وام‌گیری از نورسِ باستان draga در منطقهٔ دِین‌لا؛ نگه‌داشتنِ g نشانهٔ راهِ اسکاندیناویایی است (کلاین). draft/draught از انگلیسیِ میانهٔ draught «کشش» است، اسمِ ساخته‌شده با پسوندِ -t از همان فعل (قس نورسِ باستان dráttr)؛ املای draft صورتِ آواییِ متأخر و رایج در انگلیسیِ آمریکایی است. ادعای نورایی درست است.\",\n     \"sources\": [W_DRAGAN],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhragh- and word index (AHD_watkins1985.txt lines 386, 1434)\", \"stance\": \"supports\",\n       \"note\": \"index line: 'DRAFT dhragh- DRAG dhragh- … DRAW dhragh- DRAY dhragh-'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. drag / draw (KLN_1966.txt lines 12206, 12238)\", \"stance\": \"supports\",\n       \"note\": \"'drag, tr. and intr. v. — ME. draggen, fr. OE. dragan or ON. draga, ‘to draw’. See draw and cp. draggle. Cp. also droshky.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Draw (SKT.txt line 5393)\", \"stance\": \"supports\",\n       \"note\": \"derives Draw from A.S. dragan '(by change from g to w)'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Germanic\", \"words\": \"drinkan\", \"verdict\": \"plausible\",\n     \"derivation\": \"Proto-Germanic *drinkaną 'to drink' (Gothic drigkan, ON drekka, OE drincan, OHG trinkan) is a Germanic-only strong verb with no secure cognate outside Germanic. The traditional account — the one the chart draws — takes it as a nasal-infixed present to the 'draw' root, i.e. 'to draw (liquid) into the mouth', comparing Latin dūcere pōcula and English take a drink; Pokorny 273 puts it there tentatively ('nasaliert dazu vielleicht got. drigkan … ahd. trinkan ‚trinken‘ (einen guten Zug machen, ducere pocula)'), Watkins states it flatly, and Nourai's gloss 'draw into the mouth' is Watkins' own wording verbatim. But Buck calls the etymology 'disputed' and Wiktionary/Kroonen only say 'possibly from *dʰrenǵ-, a nasalised variant of *dʰreǵ-'. The further problem, noted at the root box, is that this root has a palatal *ǵ while dragan's has a velar *gʰ, so drinkan cannot belong to the same root as dragan in the strict sense. Plausible, not confirmed.\",\n     \"derivation_fa\": \"فعلِ ژرمنیِ آغازینِ *drinkaną «نوشیدن» (گوتی drigkan، نورسِ باستان drekka، انگلیسیِ باستان drincan، آلمانیِ علیای باستان trinkan) هم‌ریشهٔ مطمئنی بیرون از ژرمنی ندارد. تبیینِ سنتی — همان که نمودار می‌کشد — آن را ستاکِ حالِ خیشومی‌شده از ریشهٔ «کشیدن» می‌داند، یعنی «به دهان کشیدن»، با قیاسِ لاتینِ dūcere pōcula و تعبیرِ انگلیسیِ take a drink؛ پوکورنی در صفحهٔ ۲۷۳ آن را با قیدِ «شاید» چنین می‌آورد و واتکینز بی‌تردید، و معنایی که نورایی داده («به دهان کشیدن») عینِ عبارتِ واتکینز است. اما باک این ریشه‌شناسی را «مورد اختلاف» می‌خواند و ویکی‌واژه و کرونن تنها می‌نویسند «شاید از *dʰrenǵ-، گونهٔ خیشومیِ *dʰreǵ-». افزون بر این، این ریشه kʰ کامی دارد و ریشهٔ dragan غیرکامی است، پس این دو در معنای دقیقِ کلمه یک ریشه نیستند. بنابراین این گره «با احتیاط پذیرفتنی» است، نه قطعی.\",\n     \"sources\": [W_DRINKAN],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985: 'dhreg-. To draw, glide. Variant form of dhragh-. 1. Nasalized Germanic form *drinkan, to draw into the mouth, drink, in Old English drincan, to drink: DRINK. [Pok. dhreg- 273.]' (AHD_watkins1985.txt line 387) — the source of both the node's form and its gloss.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 273, s.v. dhreg̑- (POK_01.txt leaf 284)\", \"stance\": \"partial\",\n       \"note\": \"'dhreg̑- ‚ziehen; dahinziehen, gleiten, streifen‘ … Ai. dhrájati ‚streicht, gleitet dahin‘ … nasaliert dazu vielleicht got. drigkan, aisl. drekka, ags. drincan, ahd. trinkan ‚trinken‘ (einen guten Zug machen, ducere pocula)' — same derivation, but with 'vielleicht', and on a different page/root from the one Nourai cites.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.13 DRINK (SYN.txt line 8412)\", \"stance\": \"partial\",\n       \"note\": \"'Goth. drigkan, OE drincan, etc., etym. disputed. Semantically, deriv. fr. ‘draw’ … connection attractive, and so ultimate connection with OE dragan ‘draw’ … as nasalized form of a parallel root (*dhreg-).'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. dhreng- (IEC.txt line 3085)\", \"stance\": \"partial\",\n       \"note\": \"'dhreng- (dhrong-) … Go. drigkan, OHG trinkan, etc. (‘drink’, and com. Gmc.); Li. drengiù, -ti ‘sleet, pour w. rain’ … E to drench' — Mann gives the drink-words a root of their own, not a variant of the drag-root.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"drink, drown\", \"verdict\": \"plausible\",\n     \"derivation\": \"DRINK descends straight from OE drincan (< PGmc *drinkaną) and is therefore as good — and as uncertain — as node 6. DROWN, however, does not come from *drinkan: Middle English drounen has no Old English ancestor (OE used ādrencan/druncnian) and reflects a Scandinavian *drunkna/drugna (ON drukkna 'to be drowned'), a zero-grade *drunk- intransitive-inchoative to the same verb, i.e. a sister formation and not a descendant of the node's own word. Watkins keeps them apart for that reason: '2. Nasalized Germanic form *drankjan, “to cause to drink”, in: a. Old English drencan, to soak: DRENCH; b. Scandinavian *drunkna, drugna, to drown … DROWN.' So the box is right about the family but wrong about the immediate parent of drown.\",\n     \"derivation_fa\": \"«drink» یکسره از انگلیسیِ باستان drincan (از ژرمنیِ *drinkaną) آمده و اعتبارش همان اندازه است که در گرهٔ پیشین گفته شد. اما «drown» فرزندِ *drinkan نیست: صورتِ انگلیسیِ میانهٔ drounen نیایی در انگلیسیِ باستان ندارد (انگلیسیِ باستان ādrencan و druncnian به کار می‌برد) و بازتابِ صورتی اسکاندیناویایی است، *drunkna (نورسِ باستان drukkna «غرق شدن»)، که ساختی درون‌گذر و «شدنی» با درجهٔ صفرِ ستاک است؛ یعنی خواهرِ drink است نه فرزندِ آن. واتکینز نیز همین تفکیک را می‌کند و drown را از «*drunkna, drugna اسکاندیناویایی» می‌گیرد. پس خانوادهٔ واژگانی درست است ولی پدرِ بی‌واسطهٔ drown در نمودار نادرست است.\",\n     \"sources\": [W_DRINKAN],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhreg- (AHD_watkins1985.txt line 387)\", \"stance\": \"partial\",\n       \"note\": \"supports DRINK from *drinkan but routes DROWN through 'Scandinavian *drunkna, drugna, to drown, akin to the Scandinavian source of Middle English drounen' — a different immediate parent from the one the chart draws.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.13 DRINK (SYN.txt line 8412)\", \"stance\": \"partial\",\n       \"note\": \"'Goth. drigkan, OE drincan, etc., etym. disputed' — same caveat as node 6.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. dhreng- (IEC.txt line 3085)\", \"stance\": \"supports\",\n       \"note\": \"Mann groups 'Sw. drank ‘mash; barm’ as well as … G Ge-trank, E to drench, etc.' with Go. drigkan — the o-grade derivatives that also give drown.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 5,\n   \"root\": \"Dhreugh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dʰrewgʰ- 'to deceive, to harm by guile' (Pokorny 2. dhreugh- 276; LIV 157)\",\n   \"note\": \"Pokorny 276 heads the entry '2. dhreugh- ‚trügen, listig schädigen‘, dhroughos ‚Täuscher, Schädiger‘' and its very first citations are the Indo-Iranian ones the chart uses (Skt. drúhyati, OP adurujiya, Av. draoga-, druj-, and germ. *drau(γ)ma- 'Trugbild'). The root name, the language label and the gloss 'to deceive' are all correct. Cheung 2007 (s.v. *drauj) sets the Iranian verb under the same 'PIE *dʰreugʰ- ‘to deceive, deceit’ > LIV: 157 | Pok.: 276'. One drafting note about the page itself: to the right of the Old Persian box the printed chart contains an EMPTY rectangle with an arrow running into it from 'Old Persian duruj'; it carries no language label and no word, and both the JSON extraction and the chart text omit it. It looks like an empty placeholder box left in the artwork, not a lost node, but the owner may want to check it.\",\n   \"note_fa\": \"پوکورنی در صفحهٔ ۲۷۶ مدخل را چنین می‌آغازد: «۲. dhreugh- فریفتن، به نیرنگ زیان رساندن» و نخستین شواهدش همان‌هایی است که نمودار آورده: سنسکریتِ drúhyati، پارسیِ باستانِ adurujiya، اوستاییِ draoga- و druj-، و ژرمنیِ *drau(γ)ma- «تصویرِ فریب». پس نامِ ریشه، برچسبِ زبان و معنای «فریفتن» هر سه درست است. چونگ نیز در فرهنگِ ریشه‌شناختیِ فعلِ ایرانی ذیلِ *drauj همین ریشه را «*dʰreugʰ- فریفتن (LIV ۱۵۷، پوکورنی ۲۷۶)» می‌نویسد. یک نکتهٔ صفحه‌آرایی: در صفحهٔ چاپی، کنارِ جعبهٔ «پارسی باستان duruj» یک مستطیلِ خالی هست که پیکانی به آن می‌رود؛ نه نامِ زبانی دارد و نه واژه‌ای، و در استخراجِ داده نیامده است. به‌احتمالِ زیاد جعبه‌ای خالی و بازمانده از صفحه‌آرایی است، نه گرهی از دست رفته.\",\n   \"sources\": [W_DOROUGH],\n   \"ref_check\": [\n    {\"ref\": \"POK:276\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 287-288 (printed p.276): '2. dhreugh‘ ‚trügen, listig schädigen‘, dhrougho-s ‚Täuscher, Schädiger‘. Ai. drúhyati ‚sucht zu schaden‘ …, apers. Imperf. adurujiya (= ai. adruhyat) ‚log‘, av. druža[iti] ‚lügt, betrügt‘, ai. drógha-, dróha- m. ‚Beleidigung, Beschädigung, Verrat‘, av. draoga- ‚lügnerisch‘, m. ‚Lüge, Trug‘, apers. drauga- … av. druj- f. ‚Lüge, Trug; Verkörperung der Lüge‘ … anord. draumr, ahd. troum, as. drōm, engl. dream ‚Traum‘ (germ. *drau(γ)ma- ‚Trugbild‘).' Every node of this entry is on that one page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 874 (WLD_Bd1 djvu lines 55098-55116)\", \"stance\": \"supports\",\n     \"note\": \"'dhreugh- ‚trügen, listig schädigen“. … Idg. *dhreugh- ist sehr wahrscheinlich verwandt mit *dhuer- ‚durch Täuschung zu Falle bringen“ …' — the fuller source Pokorny 276 abridges.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt line 391)\", \"stance\": \"supports\",\n     \"note\": \"'dhreugh-. To deceive. Germanic suffixed form *drau(g)ma- in Old English drēam, vision, illusion, dream (but attested only in the senses of “joy,” “music”): DREAM. [Pok. 2. dhreugh- 276.]'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *drauj (CHEUNG.txt line 6212 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'*drauj ‘to lie, deceive’ … *AVESTAN: druj- (druž-) … *OLD PERSIAN: d(u)ruj- ‘to lie, deceive’ = Kent: 191b … *MIDDLE PERSIAN: MMP drwz-, BMP dlwc- /drōz-/ … *NWIR: NP durōγ … «PIE *dʰreugʰ- ‘to deceive, deceit’ > LIV: 157 | Pok.: 276»'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. dhreugh- (1) and dhroughos (2) (IEC.txt lines 3085, 3118)\", \"stance\": \"supports\",\n     \"note\": \"'dhreugh- (1), dhrugh- ‘harm, deceive’ … Skt. drohaḥ ‘harm, wrong’; drūhyāmi ‘hurt, offend’; Av. druž- ‘deceive’ … Av. cf. draoγo; Per. durūγ ‘falsehood’' and 'dhroughos (2) … Av. draoγo adj. ‘lying’; s. ‘lie’; OPer. drauga-, id.; ON draugr ‘wraith’'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"draoga,drauga; dragvant, drvant\", \"verdict\": \"plausible\",\n     \"derivation\": \"The Avestan material is real and correctly affiliated, but two details of the box are loose. (a) Bartholomae's headword (AiW 767-768) reads 'draoga-, draoγa-, p. drauga- 1) Adj. ‚lügnerisch, unwahr‘ … 2) n. ‚Lug, Lüge‘' — the 'p.' means altpersisch, so drauga- is the Old Persian form of the same word, not a second Avestan variant; Nourai copied the whole headword into an Avestan box (and drauga- reappears, correctly, as his Old Persian node 4). (b) 'a demon' does not belong to draoga- at all but to the related feminine stem Av. druj- (nom. druxš, gen. drujō) 'the Lie', personified as the chief female daēva-being opposed to Aša — Pokorny 276 renders it 'Lüge, Trug; Verkörperung der Lüge'. (c) 'dragvant, drvant': the attested forms are Gathic drəguuaṇt- and Younger-Avestan drvaṇt- 'possessing the Drug, follower of the Lie' (Bartholomae AiW 783), regularly opposed in the texts to ašavan- 'follower of Aša'; Nourai writes ə as a, his standard practice, so the printed 'dragvant' is his transliteration of drəgvant- rather than a misprint, and his gloss 'one who likes lies, atheist' is a free rendering of Bartholomae's 'Drugtgenosse, ungläubig'. Root affiliation, forms and meanings are otherwise exactly as in Pokorny and Bartholomae.\",\n     \"derivation_fa\": \"دادهٔ اوستایی درست و انتسابش به این ریشه بی‌گمان است، اما سه نکتهٔ کوچک در جعبه هست. نخست، سرواژهٔ بارتولمه (فرهنگ ایرانی باستان، ستون ۷۶۷–۷۶۸) چنین است: «draoga-, draoγa-، پارسی باستان drauga-، ۱) صفت: دروغ‌گو، ناراست … ۲) اسم: دروغ، فریب»؛ یعنی drauga- صورتِ پارسیِ باستان است نه گونه‌ای اوستایی، و نورایی همهٔ سرواژه را در جعبهٔ اوستایی نشانده است (همان drauga- را در گرهٔ ۴ به‌درستی زیرِ پارسی باستان هم آورده). دوم، معنیِ «دیو» از آنِ draoga- نیست، بلکه از آنِ ستاکِ مادینهٔ اوستاییِ druj- (نهادی druxš) است، همان «دْروجِ» شخصیت‌یافته که در برابرِ اَشَه می‌ایستد؛ پوکورنی آن را «دروغ، فریب؛ تجسّمِ دروغ» می‌نویسد. سوم، صورت‌های اصیل drəgvaṇt- (گاهانی) و drvaṇt- (اوستایی نو) «دارندهٔ دروغ، پیروِ دروغ» است (بارتولمه، ستون ۷۸۳) که در متن‌ها همواره در برابرِ ašavan- «پیروِ اَشَه» می‌آید؛ نورایی به شیوهٔ همیشگیِ خود «ə» را «a» می‌نویسد، پس «dragvant» خطای چاپ نیست بلکه شیوهٔ آوانگاریِ اوست. جز این، ریشه و معنا درست است؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_DOROUGH],\n     \"ref_check\": [\n      {\"ref\": \"POK:276\", \"status\": \"supports\",\n       \"note\": \"IEW 276 (POK_01.txt leaf 287-288): 'av. draoga- ‚lügnerisch‘, m. ‚Lüge, Trug‘ … av. druj- f. ‚Lüge, Trug; Verkörperung der Lüge‘' — note that the 'demon' sense sits on druj-, not on draoga-, and that 'apers. drauga-' is given separately as Old Persian.\"},\n      {\"ref\": \"BQT:845\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 305 (= printed p.845): Moʿin's footnote under دروند reads «پهلوی drvand (کافر، بی‌دین) … دروغ‌پرست؛ از اوستا drəgvant-, drvant- (بارتولمه AiW …)، پازند و پارسی darvand … و رک: اسحق ص ۴۲۲» — precisely the Avestan pair Nourai prints, with the same Bartholomae reference.\"},\n      {\"ref\": \"SNS:324\", \"status\": \"supports\",\n       \"note\": \"SNS_pages.txt leaf 178 (Tavoosi's glossary, printed pp. in the low 320s; the printed numerals are too poorly OCRed to fix exactly): the entry drōg gives «draoja-, draoga- : اوستا … {Mir. Man. drwg} (AiW 768) drōgha- : هندی باستان», and the neighbouring entries give druj/druz and druzan — i.e. the Avestan forms with Bartholomae's column number.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW cols. 767-768 and 783 (BRT.txt lines 13997, 14015, 14128-14132)\", \"stance\": \"supports\",\n       \"note\": \"col. 767/768 running head 'draoga- 768'; entry '1. draoga-, draoγa-, p. drauga- 1) Adj. ‚lügnerisch, unwahr‘ … 2) n. ‚Lug, Lüge‘'; and the drəgvant-/drvant- entry ends '… — mp. drvand. — Pü.: drvand.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *drauj (CHEUNG.txt line 6212 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: druj- (druž-) ‘to lie, deceive’ … Partic.: pres. OAv. ādrujiiant- … YAv. družint-' — the verbal side of the same stem.\"},\n      {\"src\": \"AVG\", \"where\": \"grep 'draoga' in AVG.txt (Jackson, Avesta Grammar)\", \"stance\": \"silent\",\n       \"note\": \"the grammar has no lexical entry for this word.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"drôg; druvand\", \"verdict\": \"plausible\",\n     \"derivation\": \"Both Middle Persian words are real. drōg/drōγ 'a lie' is Book Pahlavi <dlwb'>, Manichaean MP drwg, with the verb druxtan / drōz- 'to lie, deceive' (MacKenzie, CPD: 'druxtan, drōz- [dlwhtn’, dlwc-] lie, deceive'; 'drōzan [dlwcn’] lying, liar'; 'drōzanīh: falsehood') and the separate noun druz [dlwc] 'demon'. druwand [dlwnd] is 'evil, sinful, unrighteous' (MacKenzie), Nyberg 'druvand [dlwnd] wicked, evil, of Ahriman … — Av. drəgvant-, drvant- ‘belonging to the drug’ … Paz. daruand, darvand', so Nourai's gloss 'non-believer' is the Zoroastrian sense correctly given. Where the arrow is loose is the parentage: Middle Persian is the direct continuation of the south-west Iranian dialect whose Old-Iranian stage is Old Persian, so MP drōg continues OP drauga- (Horn 557: 'ap. drauga- ‚Lüge‘; av. draoγa-; phlv. drōγ, drōy') and Avestan draoga- is its sister, not its ancestor; likewise MP druwand continues an Old-Persian-type *drugvant-. Wiktionary states the chain as MP drō(g) < OP drauga-, with no Avestan step. Plausible: right root, right forms, genealogically simplified arrow.\",\n     \"derivation_fa\": \"هر دو واژهٔ فارسیِ میانه اصیل‌اند. drōg/drōγ «دروغ» در پهلویِ کتابی <dlwb'> و در مانویِ فارسیِ میانه drwg نوشته می‌شود و فعلِ آن druxtan / drōz- «دروغ گفتن، فریفتن» است (مکنزی: «druxtan, drōz- دروغ گفتن، فریفتن»؛ «drōzan دروغ‌گو»؛ «drōzanīh دروغ»)، و در کنارش اسمِ جداگانهٔ druz «دیو» هست. druwand نیز «بدکار، گناهکار، نادرست» است (مکنزی) و نیبرگ می‌نویسد: «druvand بدکار، بد، صفتِ اهریمن … از اوستاییِ drəgvant-, drvant- ‘وابسته به دروغ’ … پازند daruand, darvand»؛ پس معنایی که نورایی داده («بی‌دین») همان کاربردِ زردشتیِ درست است. سستیِ پیکان در نسب‌نامه است: فارسیِ میانه دنبالهٔ گویشِ جنوب‌غربی است که مرحلهٔ باستانی‌اش پارسیِ باستان است، پس drōg دنبالهٔ drauga-ی پارسیِ باستان است و draoga-ی اوستایی خواهرِ آن است نه نیایش (هرن، شمارهٔ ۵۵۷: «پارسی باستان drauga- دروغ؛ اوستا draoγa-؛ پهلوی drōγ, drōy»). ویکی‌واژه نیز زنجیره را «فارسی میانه drō(g) از پارسی باستان drauga-» می‌نویسد، بی هیچ حلقهٔ اوستایی. بنابراین: ریشه و صورت‌ها درست، پیکان ساده‌شده — با احتیاط پذیرفتنی.\",\n     \"sources\": [W_DOROUGH],\n     \"ref_check\": [\n      {\"ref\": \"BQT:846\", \"status\": \"not_found\",\n       \"note\": \"With the offset verified by Nourai's own BQT:837 for درشکه (printed = v2 leaf + 540), printed p.846 = leaf 306, which carries درهم / درویش, not دروغ. Moʿin's دروغ footnote in fact stands on p.843 (leaf 303): «دروغ … پهلوی drōg … از پارسی باستان *drauga-، اوستا draoga- (بارتولمه AiW) … در اوراق مانوی drwz- (دروغ گفتن، فریفتن) … (Henning, A list of Middle Persian…, BSOS IX,1, p.82) … کردی deroγ، افغانی drōγ، بلوچی drōg …», continuing on p.844; the دروند/دروغ‌پرست note is on p.845. So the page number is off by two or three, but the material Nourai cites exists and says what he says.\"},\n      {\"ref\": \"SNS:324,325\", \"status\": \"supports\",\n       \"note\": \"SNS_pages.txt leaves 178-179: entry «drōg … draoja-, draoga- (AiW 768) drōgha-», entry «drōzan … (Mir.Man.II,51) drwzn», and entry «druvand … {Mir.Man.II,51} drvnd … (AiW 783) drvant- : اوستا», followed by druvandān and druvandīh. Both Pahlavi words of the node, each with its Avestan antecedent — exactly the arrow drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD_mackenzie.txt lines 2081-2097)\", \"stance\": \"supports\",\n       \"note\": \"'drōz-, v. druxtan.' / 'drōzan [dlwcn’ | M, J drwzn] lying, liar. ~īh: falsehood.' / 'druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness.' / 'druxtan, drōz- [dlwhtn’, dlwc- | M drwxt, drwz-] lie, deceive.' / 'druz [dlwc] demon.'\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt lines 1361, 1369)\", \"stance\": \"supports\",\n       \"note\": \"'druvand [dlwnd] wicked, evil, of Ahriman … — Av. (774 sqq.) dragvant-, drvant- ‘belonging to the drug’ (v. druž); MPrs drwnd (S, A-H II); Paz. daruand, darvand.' and 'druž [dlwc’] all that is false, untrue, wrong, deceptive … — Av. (778 sqq.) drug-, nom. druxš, gen. drūjō'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *drauj (CHEUNG.txt line 6212 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'*MIDDLE PERSIAN: MMP drwz-, BMP dlwc- /drōz-/ ‘to deceive, break (contract)’ … *PARTHIAN: drwj- ‘to lie’'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 557 (HRN.txt line 5015)\", \"stance\": \"partial\",\n       \"note\": \"'557. durōγ, derōγ ‘Lüge; unwahr‘. ap. drauga- ‘Lüge‘; av. draoγa-; phlv. drōγ, drōy, LW. kurd. durūγ; afγ. darōγ; bal. davōγ, drōg, drōγ.' — same forms, but Horn puts the Old Persian first, i.e. the Pahlavi continues the Persian line.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"dorŭğ «دروغ»; dorvand «دُروند»\", \"verdict\": \"plausible\",\n     \"derivation\": \"دروغ NP durōγ/dorūγ 'a lie' is the regular descendant of MP drōγ: the inherited Persian ban on initial consonant clusters inserted an anaptyctic u/o (dr- > duru-/doro-, the same repair as OP duruva > NP dorost-type forms and as in doroške above), and MP ō was kept before the final γ, which in modern spoken Persian is [ɣ]; the older pronunciation is written durōγ in Horn (no. 557) and in Moʿin's footnote (BQT p.843), and Cheung lists 'NP durōγ' beside Baluchi d(a)rōg, Kurdish (Sorani) diro, Ossetic-area dialect forms. The word is Iranian throughout and never went through Arabic. دُروند dorvand 'unbeliever, follower of the Lie' is the far rarer member: it continues MP druwand through Pazand darvand (Nyberg, and Moʿin at BQT p.845 «پازند و پارسی darvand»), but it survives only in the Zoroastrian and Middle-Persian-derived tradition — Borhan-e Qāṭeʿ's own headword دروند (p.845) records quite different popular senses ('the name of a champion; a medicinal root; a hook'), and it is Moʿin's footnote, not the dictionary text, that carries the sense Nourai gives. Verdict plausible for the node, taking the weaker of the two words: دروغ alone would be confirmed.\",\n     \"derivation_fa\": \"«دروغ» (durōγ/dorūγ) دنبالهٔ قاعده‌مندِ drōγِ فارسیِ میانه است: چون فارسی خوشهٔ همخوانِ آغازین را برنمی‌تابد، واکهٔ میانجیِ u/o افزوده شد (dr- ← دُرو-)، و ō فارسیِ میانه پیش از غ نگاه داشته شد. تلفظِ کهن‌ترِ durōγ را هم هرن (شمارهٔ ۵۵۷) و هم حاشیهٔ معین بر برهان قاطع (ص ۸۴۳) ثبت کرده‌اند، و چونگ نیز «NP durōγ» را در کنارِ بلوچیِ d(a)rōg و سورانیِ diro می‌آورد. این واژه سراسر ایرانی است و هرگز از عربی نگذشته است. اما «دُروند» بسیار کمیاب‌تر است: دنبالهٔ druwandِ پهلوی از راهِ پازندِ darvand است (نیبرگ؛ و معین در ص ۸۴۵: «پازند و پارسی darvand»)، ولی تنها در سنتِ زردشتی و متن‌های برگرفته از فارسیِ میانه زنده مانده است؛ خودِ برهان قاطع ذیلِ «دروند» (ص ۸۴۵) معناهای عامیانهٔ دیگری آورده («نامِ پهلوانی است، نامِ دارویی، چنگک و قلاب») و آن معنایی که نورایی می‌دهد در حاشیهٔ معین است نه در متن. پس با در نظر گرفتنِ ضعیف‌ترِ دو واژه، این گره «با احتیاط پذیرفتنی» است؛ «دروغ» به‌تنهایی قطعی می‌بود.\",\n     \"sources\": [W_DOROUGH],\n     \"ref_check\": [\n      {\"ref\": \"BQT:846\", \"status\": \"not_found\",\n       \"note\": \"printed p.846 (v2 leaf 306) carries درهم and درویش; the دروغ footnote is on p.843 f. and دروند on p.845 — see node 2.\"},\n      {\"ref\": \"BQT:845\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 305 (printed p.845), headword دروند plus Moʿin's footnote «پهلوی drvand (کافر، بی‌دین) … دروغ‌پرست؛ از اوستا drəgvant-, drvant- (بارتولمه AiW)، پازند و پارسی darvand» — the Persian word and its meaning as Nourai gives them.\"},\n      {\"ref\": \"SNS:324\", \"status\": \"supports\",\n       \"note\": \"SNS glossary (leaves 178-179) has drōg, drōzan, druvand, druvandān, druvandīh with their Avestan and Manichaean-MP antecedents; it is a Pahlavi glossary, so it supports the pre-history rather than the New Persian form itself.\"},\n      {\"ref\": \"TZF:22\", \"status\": \"not_checked\",\n       \"note\": \"Abolghasemi, Tārix-e Moxtasar-e Zabān-e Fārsi: refs_online.json records no accessible copy (not on archive.org; the ketabnak PDF is behind a login), so page 22 could not be read.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 557 (HRN.txt line 5015)\", \"stance\": \"supports\",\n       \"note\": \"'557. durōγ, derōγ ‘Lüge; unwahr‘. ap. drauga- ‘Lüge‘; av. draoγa-; phlv. drōγ, drōy, LW. kurd. durūγ; afγ. darōγ; bal. davōγ, drōg, drōγ (49).'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *drauj, NWIR section (CHEUNG.txt line 6212 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP durōγ, Bal. d(a)rog, Kurd. (Kurm.) daraw (f.), (Sor.) diro, Abyan. dorū, Abz. durū … ‘lie’'.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ ed. Moʿin, pp.843-845\", \"stance\": \"supports\",\n       \"note\": \"p.843 دروغ: «پهلوی drōg … از پارسی باستان *drauga-، اوستا draoga- (بارتولمه AiW) … در اوراق مانوی drwz- (دروغ گفتن، فریفتن)»; p.845 دروند with the darvand footnote.\"},\n      {\"src\": \"MON\", \"where\": \"grep دروند / دروغ in MON_part1/2\", \"stance\": \"silent\",\n       \"note\": \"the 2-volume abridgement on disk yields no etymological entry for either word (only دروغ in running text).\"},\n      {\"src\": \"ARY\", \"where\": \"grep 'دروغ' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"the two hits (lines 8803, 9754) are in discussions of 'راست/دروغ' and 'زور', not a headword entry for دروغ.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"duruj\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Persian duruj- is the verbal root 'to lie, deceive', attested in the Bisotun inscription in the imperfect adurujiya 'he lied' (DB 1.39, 1.78, 3.80, 4.8-29 …), 3pl. adurujiyašā, and in the past participle duruxtam 'false(ly)' (DNb 52, 55; DB 4.44), beside the noun drauga- 'the Lie' — Darius's own term for the imposture of the rebel pretenders and for the disorder that 'waxed great in the country' (DB 1.34). The initial cluster dr- before u is broken by anaptyxis in Old Persian orthography (Kent §128: 'OP has anaptyxis in the cluster dr when it is followed by u: duruva …, duruxtam …, adurujiya'), which is exactly why Nourai's headword is duruj and not druj. Kent's lexicon, on the page Nourai cites, states the whole thing.\",\n     \"derivation_fa\": \"«duruj-» ستاکِ فعلیِ پارسیِ باستان به معنی «دروغ گفتن، فریفتن» است و در سنگ‌نبشتهٔ بیستون در ماضیِ استمراریِ adurujiya «دروغ گفت» (DB ۱٫۳۹، ۱٫۷۸، ۳٫۸۰، ۴٫۸ تا ۲۹ و …) و سوم‌شخصِ جمعِ adurujiyašā و اسمِ مفعولِ duruxtam «دروغ، به‌دروغ» (DNb ۵۲ و ۵۵؛ DB ۴٫۴۴) به کار رفته، در کنارِ اسمِ drauga- «دروغ» که داریوش آن را برای فریبِ مدعیانِ دروغین و آشوبی که «در کشور بزرگ شد» (DB ۱٫۳۴) به کار می‌برد. خوشهٔ آغازینِ dr پیش از u در خطِ پارسیِ باستان با واکهٔ میانجی شکسته می‌شود (کنت، بندِ ۱۲۸)، و همین است که سرواژه duruj است نه druj. کنت در همان صفحه‌ای که نورایی یاد کرده همهٔ این‌ها را می‌آورد؛ ادعای نورایی درست است.\",\n     \"sources\": [W_DOROUGH],\n     \"ref_check\": [\n      {\"ref\": \"KNT:191\", \"status\": \"supports\",\n       \"note\": \"KNT.txt leaf 215 (printed pp.191-192): 'duruj- vb. ‘lie, deceive’: Av. druj- ‘lie’ (draog-, Bthl. AiW 767), pres. družaiti, sb. druz- ‘principle of evil, devil’, Skt. drúhyati ‘deceives’, Gm. trügen, pIE *dhrugh- (§76.III). See also drauga-. adurujiya imf. … DB 1.39, 78; 3.80; 4.8 … duruxtam nsn. past pte. pass.' — the node reproduces this entry, gloss and all. Cheung independently cites the same place: 'OLD PERSIAN: d(u)ruj- ‘to lie, deceive’ = Kent: 191b'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §§76.III, 128, 242 and lexicon p.191\", \"stance\": \"supports\",\n       \"note\": \"'§128 … OP has anaptyxis in the cluster dr when it is followed by u: duruva ‘firm’ …; duruxtam ‘false’ …; adurujiya ‘he lied’, cf. Av. acc. drujim ‘devil’.'\"},\n      {\"src\": \"POK\", \"where\": \"IEW 276 (POK_01.txt leaf 287)\", \"stance\": \"supports\",\n       \"note\": \"'apers. Imperf. adurujiya (= ai. adruhyat) ‚log‘ … apers. drauga- ‚lügnerisch‘'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *drauj, Old Persian section\", \"stance\": \"supports\",\n       \"note\": \"lists every attestation: 'impf. IND. 3sg. ad(u)rujiya (DB 1.39) … 3pl. ad(u)rujiyašā (DB 4.34); Partic.: perf. pass. d(u)ruxta-'.\"},\n      {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon (TLM.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep for 'duruj' in the local OCR returned nothing usable (the file's OCR of the lexicon is poor).\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Germanic\", \"words\": \"drauma\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *draumaz 'dream, vision' goes back to *draugmaz, an m-stem noun to the verb *dreuganą 'to deceive' (OHG triogan, OS bidriogan, ON draugr 'ghost, revenant'), with the regular Germanic loss of -g- before -m- and compensatory lengthening/diphthong; its literal sense is 'a deceiving appearance, phantasm'. Pokorny 276 gives the equation in one line: 'anord. draumr, ahd. troum, as. drōm, engl. dream ‚Traum‘ (germ. *drau(γ)ma- ‚Trugbild‘)', and Watkins repeats it as 'Germanic suffixed form *drau(g)ma-'. Nourai's citation form 'drauma' and gloss 'illusion, vision' render exactly that reconstruction.\",\n     \"derivation_fa\": \"ژرمنیِ آغازینِ *draumaz «رؤیا، دیدار» از *draugmaz آمده است، اسمی با پسوندِ -m از فعلِ *dreuganą «فریفتن» (آلمانیِ علیای باستان triogan، ساکسونِ باستان bidriogan، نورسِ باستان draugr «شبح»)؛ در ژرمنی g پیش از m می‌افتد و واکهٔ پیشین کشیده/دوگانه می‌شود. معنای تحت‌اللفظیِ آن «نمودِ فریبنده، تصویرِ دروغین» است. پوکورنی در صفحهٔ ۲۷۶ همین معادله را در یک سطر می‌آورد: «نورسِ باستان draumr، آلمانیِ علیای باستان troum، ساکسونِ باستان drōm، انگلیسی dream «خواب» (ژرمنیِ *drau(γ)ma- «تصویرِ فریب»)»، و واتکینز نیز آن را «صورتِ پسونددارِ ژرمنیِ *drau(g)ma-» می‌نامد. صورت و معنایی که نورایی داده دقیقاً همین بازسازی است؛ ادعا درست است.\",\n     \"sources\": [E_DREAM],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 391): 'dhreugh-. To deceive. Germanic suffixed form *drau(g)ma- in Old English drēam, vision, illusion, dream (but attested only in the senses of “joy,” “music”): DREAM.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 276 (POK_01.txt leaf 288)\", \"stance\": \"supports\",\n       \"note\": \"'as. bidriogan, ahd. triogan ‚trügen‘, anord. draugr m. ‚Gespenst‘; schwundstufig as. gidrog n. ‚Trugbild‘ … anord. draumr, ahd. troum, as. drōm, engl. dream ‚Traum‘ (germ. *drau(γ)ma- ‚Trugbild‘).'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 874 (WLD_Bd1 djvu line 55098 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'dhreugh- ‚trügen, listig schädigen“' with the same Germanic list that Pokorny 276 abridges.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. dhroughos (2) (IEC.txt line 3118)\", \"stance\": \"partial\",\n       \"note\": \"'dhroughos (2) ‘bad, evil, shrunken, wizened; evil person or thing’ … Av. draoγo adj. ‘lying’ … OPer. drauga-, id.; ON draugr ‘wraith’ … (The semantic links are obscure.)' — Mann keeps the family but flags the semantics as unclear.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"dream\", \"verdict\": \"plausible\",\n     \"derivation\": \"The family is certainly this one, but the immediate parentage of the modern English word is not settled, and the chart's flat arrow Germanic *drauma > dream hides the problem. Old English drēam is abundantly attested — but only in the senses 'joy, mirth, noisy merriment, music'; the sense 'sleeping vision' is expressed in Old English by swefn. 'Dream' in the modern sense appears only in the mid-13th century, in the Danelaw-influenced Midlands and North, which is why the OED and Etymonline derive it from Old Norse draumr (or from the continental Germanic cognates OS drōm, MDu. droom) rather than as a straight continuation of OE drēam, while leaving open whether OE drēam 'joy' is the same word at all; Watkins concedes as much in his parenthesis '(but attested only in the senses of “joy,” “music”)'. Either way the etymon is *drau(g)ma- 'phantasm' from *dʰrewgʰ-, so Nourai's root is right; only the internal English route is glossed over.\",\n     \"derivation_fa\": \"خانوادهٔ واژگانی بی‌گمان همین است، اما نیای بی‌واسطهٔ واژهٔ انگلیسیِ امروز روشن نیست و پیکانِ سادهٔ نمودار این دشواری را می‌پوشاند. «drēam» در انگلیسیِ باستان فراوان به کار رفته است، ولی تنها به معنی «شادی، سرور، هلهله، موسیقی»؛ معنیِ «خواب دیدن» در انگلیسیِ باستان با واژهٔ swefn بیان می‌شد. «dream» به معنیِ امروزی نخست در میانهٔ سدهٔ سیزدهم میلادی و در نواحیِ میانی و شمالیِ زیرِ نفوذِ اسکاندیناوی پیدا می‌شود؛ از همین رو فرهنگِ آکسفورد و اتیمولوژی‌آنلاین آن را از نورسِ باستان draumr (یا از هم‌ریشه‌های قاره‌ای مانندِ drōm و droom) می‌گیرند، نه دنبالهٔ مستقیمِ drēamِ انگلیسیِ باستان، و در این‌که آن دو اصلاً یک واژه باشند تردید روا می‌دارند؛ واتکینز هم در جملهٔ معترضهٔ خود همین را می‌پذیرد. به هر روی، اصلِ واژه همان *drau(g)ma- «تصویرِ فریب» از ریشهٔ *dʰrewgʰ- است، پس ریشه‌ای که نورایی داده درست است و تنها مسیرِ درون‌انگلیسی ساده‌سازی شده است.\",\n     \"sources\": [E_DREAM],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dhreugh- (AHD_watkins1985.txt line 391)\", \"stance\": \"partial\",\n       \"note\": \"derives DREAM from 'Old English drēam, vision, illusion, dream' but adds '(but attested only in the senses of “joy,” “music”)' — the concession that makes the OE step doubtful.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 276 (POK_01.txt leaf 288)\", \"stance\": \"supports\",\n       \"note\": \"'anord. draumr, ahd. troum, as. drōm, engl. dream ‚Traum‘ (germ. *drau(γ)ma- ‚Trugbild‘)' — Pokorny lists English dream directly with ON draumr, without committing to the OE route.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein / Etymonline (word/dream, archived)\", \"stance\": \"partial\",\n       \"note\": \"Etymonline: 'mid-13c., ‘sequence of sensations … of a sleeping person’, probably from Old Norse draumr … from Proto-Germanic *draugmas ‘deception, illusion, phantasm’ … Old English dream meant ‘joy, mirth, noisy merriment’, and scholars remain uncertain whether this is the same word.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"data/verification/page-135.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 -m json.tool data/verification/page-135.json > /dev/null && echo \"valid json\"\npython3 tools/verify_check.py 135",
 "description": "Write and validate page-135.json"
}
```


### [2026-09-05T20:26:28.349Z] TOOL RESULT

```
written
valid json
nodes verified: 13/13
node verdicts: {'confirmed': 7, 'plausible': 6}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 12, 'partial': 1, 'not_checked': 5, 'not_found': 2}
books consulted: {'supports': 27, 'partial': 10, 'silent': 6} | by book: {'POK': 6, 'KLN': 5, 'IEC': 4, 'AHD': 4, 'CHEUNG': 4, 'SKT': 3, 'BQT': 2, 'MON': 2, 'ARY': 2, 'SYN': 2, 'HRN': 2, 'BRT': 1, 'AVG': 1, 'PHD': 1, 'NYB': 1, 'KNT': 1, 'TLM': 1, 'WLD': 1}
```


## [2026-09-05T20:26:35.552Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TLM duruj ===\"; grep -c -i \"duruj\" TLM.txt; grep -n -i \"duruj\\|drauga\" TLM.txt | head -5\necho \"=== AVG draoga ===\"; grep -c -i \"draoga\" AVG.txt; grep -n -i \"draoga\\|drvant\" AVG.txt | head -5",
 "description": "Verify TLM and AVG greps"
}
```


### [2026-09-05T20:26:35.632Z] TOOL RESULT

```
=== TLM duruj ===
15
194:10.  0a-27 )tiy  Darayavaus  xsayafliya  ima  tya  mana  kartam pasava  ya0a  xs-28)aya<9iya  abavarn  Iva”bujiya  nama  Kuraus  pu0ra amaxam  taumay-29)a  hauvama8  ida  xsayafliya  aha  avahya Kanbujiyahya  bra-30)t[a  Bardijya  nama  aha  hamata9  hamapita Kanbujiyahya  pasava  Kan-31)b[ujiya  a]vam  Bardivam  avajan ya&7  Kanbujiya  Bardiyam  avajan  karahy-32)[a  naiy]  azda  abava tya  Bardiya  avajata10  pasava  Kanbujiya  Mudrayam  33)[asiya]va yafti  Kanbujiya  Mudrayam  asiyava  pasava  kara  araika  abava 34)[pasava]  drauga  dahyauva  vasiy11  abavra  uta  Parsaiy  uta Madaiy  ut-35)[a  anjiyauva  daily usuva
195:11.  0atiy  Darayavaus  xsayafliya  pa-36 )[sava]  I   martiya  magus aha  Gaumata  nama12  hauv  udapatata  haca  Paisi-37)[ya]uvadaya Arakadris  nama  kaufa  haca  avadasa  Yiyaxnahya  mah-38)[ya] XIV  raucabis  Sakata  ahan  yadiv  udapatata  hauv  karahya  avaftl 39  )[a]durujiya  adam  Bardiya  amiy  hya  Kuraus  pu0ra  Kanbuji-
246:16.  0atiy  78)  Darayavaus  xsayafliva  va0a  adam  Gaumatam tyam  magum  avajanam  pa-74)sava  I   martiya  A#rina  nama  Upa- dara”mahya1  pu0  a   hauv  udapata[ta  Uvajai]-7o)y  karahya  avafla aflaha  adam  Uvajaiy  xsayatfiya  amiy  pa[sava]  Uva-76)jiya  ham- i0riya  abava"  abiy  avam  [   A   ]<9rinam  asiyava”  hauv  x[saya0iya] 77)abava  Uvajaiy  uta  I   martiya  Babiruviya  Nadi”tabaira  nama Aina[ira]hy-78)a  pu0ra  hauv  udapatata  Babirauv  karam  avafti adurujiya  adam  Nab-79)ukudracara  amiy  hya  Nabunaitahya pu0ra  pasava  kara  hya  Babiruviya  80)haruva  abiy  avam  Nadin- tabairam  asiyava  Babirus  hami(9riya  abava  x-81)sa0ram  tya  Ba- birauv hauv  agarbayata
417:14.  tfatiy  Darayavaus  xsa-77)ya0iya  yata  adam  Parsai[y]  u[t]a Madaiy  aham  patiy  duvitlyam  78)Babiruviya  hami0riya  abava" hacama  I   martiya  Arxa  nama  [Arm]ini-79)va  Halditahya  pu0ra hauv  udapatata  Babirauv  Dubala  nama  [da]hya-80)us  haca  avadasa hauv  [kjarahya  ava&i  adurujiya  adam  Nabukud-81)racara  amiy Nabunaitahya  pu0ra  pasava  kara  Babiruviya  hacama  ha-82)mi- 0riya  abava  abiy  avam  Arxam  asiyava  Babirum  hauv  agarbayat- 83)a  hauv  xsayafliya  abava  Babirauv
444:2.  0atiy  D-3)arayavaus  xs[aya0i]ya  ima  tya  adam  akuna-4)vam vasnii  Aurafmazdjaka1  hamahyaya  0ar-5)da  pasava  ya0a  x[saya- 0iya]  abavam  XIX  hamaran-6)a  akunavam  vasn[a  Aura]mazdaha adamsim2  a-7)janam  uta  IX  xs[aya0iy]a  agarbayam  I   Gaumata 8)nama  magus  aha  [kauvad]urujiya  ava0a  a0aha  adam  9)Bardiya amiy  [hya  Kujraus  pu0ra  hauv  Parsam  ha-lO)mi0riyam  akunau[s I   A0ri]na  nama  Uvajiya  hauv  adu-ll)rujiya  avafla  a[0aha  adam] xsayatfiya  amiy  Uvajaiy  12)hauv  Uvajam  ha[mi0riya]m  akunaus [ma]mi  [I  Na]dintabaira  n-13)ama  Babiruviya  hauv  adurujiya ava0a  afoha  14)adam  Kabukudra[cara  amiy]  hya  Xabunaitahya pu0ra  15)haav  Babirum  [hami]0riyam  akunaus  I   Martiya  na- 16)ma  Parsa  hauv  [ad]u[ruj]iya  avaftx  a0aha  adam  Imani-17)s amiy  Uvajaijy  xsaya]0h'a  hauv  Uvajam  kami0ri3’-a-18)in  akunaus I   Fravar[ti]s  nama  Hilda  hauv  adurujiya  19)ava0a  a0aha  a[da]m [X]sa[0r]ita  amiy  Uvaxstrahya  taumay-20)a  hauv  Madam  [hami- 0rivam]  akunaus  I   Ci0raDtaxma  nama  Asa-2 l)gartiya  hauv  [adu]- rujiya  ava0a  a0aha  adam  xsaya0-22)iya  amiy  Asaga[rtaiy]  Uvaxs- trahva  tauinaya  hauv  23)Asagartam  hami0ri[yam]  akunaus  I Frada  nama  24)Margava  hauv  a[d]u[r]ujiya  ava0a  alalia  adam 25)xsaya0i3’a  a[miy  Mar]gauv  hauv  Margum  hami6iri-26)yam akunaus  [I  Yahyajzdata  nama  Parsa  hauv  a-27)dm’ujiya  ava[0a a0aha]  adam  Bardiya  amiy  hya  Ku-28)raus  pu0ra  ha[uv  Parjsam hami0riyam  akunaus  I   Ar-29)xa  nama  Armiu[iva  hauv]  adurujiya avada  alalia  adam  Nab-30)ukudracara  ami3r  [hya  Nabu]naitahya pu0ra  hauv  Babirum  ham-31  )i0ri3ram  akunaus
=== AVG draoga ===
0
764:Av.  OTvaiito  'swift  steeds'  =  Skt.  drvantas;  Av. auruna-  'wild,  fiery',  cf.  Skt.  arund-;  Av.  aurufd  'bright, white'  =  Skt.  arufds;  Av.  paurvata  'two  mountains'  = Skt.  pdrvatdu;  Av.  taurun9m  'young'  =  Skt.  tdruiiuzm; Av.  hcPrvcpn  'whole'  =  Skt.  sdrvdm  ;  Av.  po"ru-  (also paouru-)  'many',  for  paru-.
4638:Av.  a*rvanj-  adj.  and   noun  'swift,    courser*  =  SkL  drvant-;
```


## [2026-09-05T20:26:50.533Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json,io\np=\"data/verification/page-135.json\"\nd=json.load(open(p,encoding=\"utf-8\"))\ne=[x for x in d[\"entries\"] if x[\"entry\"]==5][0]\nn=[x for x in e[\"nodes\"] if x[\"id\"]==4][0]\nfor c in n[\"consulted\"]:\n    if c[\"src\"]==\"TLM\":\n        c[\"where\"]=\"Tolman, Ancient Persian Lexicon and texts (TLM.txt lines 194-195, 246, 417, 444)\"\n        c[\"stance\"]=\"supports\"\n        c[\"note\"]=\"grep 'duruj' gives 15 hits, all in Tolman's transliterated Bisotun text: 'hauv karahya avaθā [a]durujiya adam Bardiya amiy hya Kuraus puθra' (DB 1.38-39), 'karam avaθā adurujiya adam Nabukudracara amiy' (DB 1.78), and the summary list DB 4.8-30 where each pretender 'adurujiya'; also 'pasava drauga dahyauvā vasiy abava' (DB 1.34) — the attestations behind Kent's entry.\"\n        break\na=[x for x in e[\"nodes\"] if x[\"id\"]==1][0]\nfor c in a[\"consulted\"]:\n    if c[\"src\"]==\"AVG\":\n        c[\"note\"]=\"grep -i 'draoga' in AVG.txt returns 0 hits; Jackson's book is a comparative grammar with no lexicon, so it has nothing to say about this word (its only 'drvant' hits are Av. aurvant- 'swift steed' = Skt. árvant-, an unrelated word).\"\n        break\njson.dump(d,open(p,\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=1)\nopen(p,\"a\",encoding=\"utf-8\").write(\"\\n\")\nprint(\"patched\")\nPYEOF\npython3 -m json.tool data/verification/page-135.json >/dev/null && echo \"valid json\"\npython3 tools/verify_check.py 135",
 "description": "Correct TLM/AVG notes and re-check"
}
```


### [2026-09-05T20:26:53.926Z] TOOL RESULT

```
patched
valid json
nodes verified: 13/13
node verdicts: {'confirmed': 7, 'plausible': 6}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 12, 'partial': 1, 'not_checked': 5, 'not_found': 2}
books consulted: {'supports': 28, 'partial': 10, 'silent': 5} | by book: {'POK': 6, 'KLN': 5, 'IEC': 4, 'AHD': 4, 'CHEUNG': 4, 'SKT': 3, 'BQT': 2, 'MON': 2, 'ARY': 2, 'SYN': 2, 'HRN': 2, 'BRT': 1, 'AVG': 1, 'PHD': 1, 'NYB': 1, 'KNT': 1, 'TLM': 1, 'WLD': 1}
```


## [2026-09-05T20:27:09.741Z] AGENT

Page 135 (book p. 105) verified. `data/verification/page-135.json` written; `verify_check.py 135` shows 13/13 nodes, 0 PROBLEM lines.

**Verdicts** — nodes: 7 confirmed, 6 plausible. Roots: 1 confirmed (Dhreugh), 1 plausible (Dhragh 1, Dhreg). Ref checks: 12 supports, 1 partial, 2 not_found, 5 not_checked (nodes with `refs=None`, plus TZF:22 which has no accessible copy). 43 `consulted` entries from 18 books.

No `disputed` and no `transcription_suspect` items. Points worth the owner's attention:

- **Root "Dhragh 1, Dhreg" (plausible)** — merges two distinct Pokorny entries: *dherā̆gh-* (p. 257, cited) for drag/draw/droshky, and *dhreg̑-* (p. 273, uncited) for drink. Velar *gʰ* vs palatal *ǵ*, so not strict variants; Nourai follows Watkins/AHD, who does call them "variant forms".
- **#6 drinkan / #7 drink, drown (plausible)** — Buck calls the drink etymology "disputed"; and *drown* is not from *drinkan* but from Scandinavian *drunkna* (Watkins routes it separately).
- **#1 Avestan draoga, drauga (plausible)** — *drauga-* is Old Persian (Bartholomae's headword reads "draoga-, draoγa-, p. drauga-"); "a demon" belongs to Av. *druj-*, not *draoga-*.
- **#2 Pahlavi, #3 Persian (plausible)** — MP drōg continues OP *drauga-*, Avestan being a sister form; also دُروند is a learned Zoroastrian word (Borhan's own headword gives entirely different popular senses).
- **#6 dream (plausible)** — OE *drēam* is attested only as "joy, music"; OED/Etymonline route the modern word via ON *draumr*.

**Citation slip (book, not extraction):** BQT:846 (cited twice, for the Pahlavi and Persian nodes) does not hold دروغ/دروند — with the offset independently confirmed by Nourai's own correct BQT:837 for درشکه, Mo'in's دروغ footnote is on p. 843 f. and دروند on p. 845. Recorded as `not_found` with the correct pages quoted.

**One thing for the owner to check in the data:** the printed page has an **empty rectangle** to the right of the "Old Persian duruj" box, with an arrow running into it from that box. It has no language label and no words; both `page-135.json` (extraction) and the chart text omit it. It looks like a leftover placeholder in the artwork rather than a lost node, but it is a difference between the page and the JSON. No other extraction errors — the rendered page matches the JSON node-for-node.
