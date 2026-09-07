# Verification process log — verify-page-333


## [2026-09-07T16:12:39.672Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 333 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-333.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-333.json. Write /home/sfmqrb/git/rishe/data/verification/page-333.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 333` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:12:41.714Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T16:12:42.422Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:12:42.437Z] TOOL RESULT

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


## [2026-09-07T16:12:42.969Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-333.txt"
}
```


### [2026-09-07T16:12:42.982Z] TOOL RESULT

```
1	=== PDF page 333 (book page 303) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Men 2 : to remain  (refs POK:729)
4	#1 (parent #0) [Avestan / Old Persian] refs=KLN:934; HRN:215; KNT:202 | man 2 : await
5	  #2 (parent #1) [Pahlavi] refs=HRN:215 | mân-stan : to stay
6	    #3 (parent #2) [Persian] refs=BQT:1950 | mândan 2 «ماندن ۲» : to remain, stay
7	  #4 (parent #1) [Avestan] refs=SNS:74 | upa-mati : remain, endure, keep the hopes up ☞Upo
8	    #5 (parent #4) [Pahlavi] refs=SNS:74 | ômĕd : hope
9	      #6 (parent #5) [Persian] refs=MON | omîd «امید ( امیدوار )» : hope | NOTE: AEF:147 offers a few possible roots for this word and concludes that the root is not quite clear.
10	#7 (parent #0) [Latin] refs=AHD; KLN | maněre : to remain
11	  #8 (parent #7) [English] refs=None | mansion, permanent, remain
12	--- entry 1 ---
13	ROOT [Indo-European] Men 3 : to stand out, project  (refs POK:726)
14	#1 (parent #0) [Avestan] refs=POK:726; KLN:1009 | mati, mnti : sticking out, prominent ; fra-manyente : they get a head start
15	#2 (parent #0) [Latin] refs=AHD | mont : mountain
16	  #3 (parent #2) [French] refs=None | 
17	    #4 (parent #3) [Persian] refs=MON |  | extra: مونترال ، مونتکارلو
18	مونتگمری ، پارامونت
19	  #5 (parent #2) [English] refs=KLN:1009 | mount, mountain, amount, paramount, piedmont
20	#6 (parent #0) [Latin] refs=AHD | miněre : to project
21	  #7 (parent #6) [English] refs=None | prominent, eminent, imminent
22	#8 (parent #0) [Indo-European] refs=POK:726,747; KLN:932 | Mon, Mono : neck, throat
23	  #9 (parent #8) [Avestan] refs=POK:747 | minu : throat ; manaothri, moneutro : neck, throat
24	  #10 (parent #8) [Germanic] refs=AHD | monô : neck
25	    #11 (parent #10) [English] refs=KLN:932 | mane
26	--- entry 2 ---
27	ROOT Men-dh -> redirect to Men 1
28	--- entry 3 ---
29	ROOT Měnôt -> redirect to Me 2
30	
```


## [2026-09-07T16:12:46.406Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-333.json",
 "description": "Read source JSON page 333"
}
```


### [2026-09-07T16:12:46.443Z] TOOL RESULT

```
{
  "pdf_page": 333,
  "book_page": 303,
  "entries": [
    {
      "root": {
        "name": "Men 2",
        "lang": "Indo-European",
        "refs": "POK:729",
        "gloss": "to remain",
        "note": "BQT:1949 claims this word is ultimately from root \"Dem:house\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:934; HRN:215; KNT:202",
          "words": [
            {"translit": "man 2", "gloss": "await", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:215",
          "words": [
            {"translit": "mân-stan", "gloss": "to stay", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1950",
          "words": [
            {"translit": "mândan 2", "gloss": "to remain, stay", "script": "ماندن ۲"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Avestan",
          "refs": "SNS:74",
          "words": [
            {"translit": "upa-mati", "gloss": "remain, endure, keep the hopes up", "script": null, "see": ["Upo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "SNS:74",
          "words": [
            {"translit": "ômĕd", "gloss": "hope", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "omîd", "gloss": "hope", "script": "امید ( امیدوار )"}
          ],
          "script_extra": null,
          "note": "AEF:147 offers a few possible roots for this word and concludes that the root is not quite clear.",
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "maněre", "gloss": "to remain", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mansion, permanent, remain", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Men 3",
        "lang": "Indo-European",
        "refs": "POK:726",
        "gloss": "to stand out, project"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:726; KLN:1009",
          "words": [
            {"translit": "mati, mnti", "gloss": "sticking out, prominent", "script": null},
            {"translit": "fra-manyente", "gloss": "they get a head start", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "mont", "gloss": "mountain", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "مونترال ، مونتکارلو\nمونتگمری ، پارامونت",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 2,
          "lang": "English",
          "refs": "KLN:1009",
          "words": [
            {"translit": "mount, mountain, amount, paramount, piedmont", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "miněre", "gloss": "to project", "script": null}
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
            {"translit": "prominent, eminent, imminent", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:726,747; KLN:932",
          "words": [
            {"translit": "Mon, Mono", "gloss": "neck, throat", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Avestan",
          "refs": "POK:747",
          "words": [
            {"translit": "minu", "gloss": "throat", "script": null},
            {"translit": "manaothri, moneutro", "gloss": "neck, throat", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "monô", "gloss": "neck", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "KLN:932",
          "words": [
            {"translit": "mane", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Men-dh",
        "redirect": "Men 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Měnôt",
        "redirect": "Me 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T16:12:46.700Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T16:12:46.762Z] TOOL RESULT

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


## [2026-09-07T16:13:10.679Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','KNT','BQT','MON','SNS','AHD','AEF','BRT','PHD','NYB','WLD','IEC','SYN','LEW','LAT','ARY','SKT','CHEUNG','HUB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


### [2026-09-07T16:13:12.104Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

CHEUNG MISSING

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
```


## [2026-09-07T16:13:16.111Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','KNT','BQT','SNS','AHD']:\n    v=d[k]\n    print('==',k, v.get('page_offset'))\n    print('   hint:', v.get('lookup_hint'))\n    print('   local:', v.get('local_file'))\n\""
}
```


### [2026-09-07T16:13:17.387Z] TOOL RESULT

```
== POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
== KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
== HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
== KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
== BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
== SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
   hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
== AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
```


## [2026-09-07T16:13:21.096Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 72[0-9]\\|Page(s): 74[0-9]\" POK_full.txt | head -60"
}
```


### [2026-09-07T16:13:21.152Z] TOOL RESULT

```
58703:Page(s): 722 
58717:Page(s): 722 
58732:Page(s): 723 
58788:Page(s): 723-724 
58808:Page(s): 724 
58822:Page(s): 724 
59092:Page(s): 720 
59118:Page(s): 720 
59139:Page(s): 720 
59198:Page(s): 720-721 
59212:Page(s): 721 
59252:Page(s): 721-722 
59269:Page(s): 725 
59285:Page(s): 725 
59301:Page(s): 725 
59374:Page(s): 729 
59397:Page(s): 729-730 
59499:Page(s): 726 
59529:Page(s): 726 
59673:Page(s): 726-728 
59709:Page(s): 728-729 
59731:Page(s): 729 aaypa 
59968:Page(s): 740 
60334:Page(s): 741 
60353:Page(s): 743-744 
60450:Page(s): 744-745 
60468:Page(s): 745 
60607:Page(s): 741-743 
60612:Page(s): 745 
60645:Page(s): 743 
60657:Page(s): 745-746 
60673:Page(s): 746 
60884:Page(s): 722-723 
60914:Page(s): 724 
61040:Page(s): 725 
61119:Page(s): 743 
61173:Page(s): 740-741 
61190:Page(s): 746 
61202:Page(s): 747 
61220:Page(s): 747 
61237:Page(s): 747 
61252:Page(s): 747 
61275:Page(s): 747-748 
61310:Page(s): 748 
61331:Page(s): 748-749 
61349:Page(s): 749 
61368:Page(s): 749 
61419:Page(s): 749 
61500:Page(s): 746-747 
61542:Page(s): 746
```


## [2026-09-07T16:13:23.714Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '59355,59420p;59480,59540p' POK_full.txt"
}
```


### [2026-09-07T16:13:23.768Z] TOOL RESULT

```
Material: Alb. merit, mend^ suckle, suck', mezej^ suckle '; mes, mez/m. " fullness ', mezat 
"young bull, the young of an animal ', /77ezc»/'e "young cow' {*mondJo-), mez^ colt, foal'; 
lllyrian PN Mendai. "mare', ablaut. PN Mandeta; mandos ^srwaW horse', out of it dial. 
/77a/7/7i/5.' (under the influence of common Celtic -ns-, -nt- > -nn-) Latin mannus^ a small 
Gallic horse, coach-horse, cob '; Messapic Juppiter Menzana {*mendJo-no-) " the God to 
whom horses were sacrificed '; from lllyrian derives rom. mandius^ fertility, cattle' 
(Rumanian minz^ fertility ', /77a/7za/ "young cow'. Modern High German Tirol Manz, Menz^ 
infertile cow', Rhineland Minzekalb, Basque mando' a mule ', etc.); Middle Irish menn 
{*mendo-), mennan'young animal, calf, fertility ', secondary bennan' little calf, kid, little 
deer', nir. binnseach, gael. m/nnseacb ^oung goat, kid', cymr. mynnan'k\6', corn, m/'n^ a 
young goat, kid ', bret. /77e/7/7 "young animal', menn gavryoung goat, kid'; (common Celtic 
-ns-, -nt- > -nn-), gall. PN Epo-manduo-durum, brit. PN Mandu-essedum {\\\yr\an 
loanword?); probably also the Bavarian FIN Mindef, Old High German manzonm. PI. "teat, 
udder'; lllyrian gall, mand- cou\d also contain Indo Germanic ablaut mpd- 



References: WP. II 232, WH. II 29 f., MarstranderZceltPh. 7, 384 f., Krahe, WiJrzburg. Jb. 
1, 189,202. 
Page(s): 729 

Root / lemma: mehnd^a, -om) 

Meaning: defect, flaw, *nnental disability 

Note: 

Root/ lemma: mehnd^a, -om)\ defect, flaw, *nnental disability, derived from Root/ lemma: 

menA'"-: to pay attention to; vivacious, wisdom. Probably taboo word. 
Material: Old Indie minda^ body defect ' (for *manda afier /7/>7d/a 'reprimand'); 

Latin mendum, menda " a fault, error, blunder ', e-mendare " to free from faults, correct, 
improve, amend ', whereoi mend/cus^ beggarly, needy, in want, indigent, poor, paltry, 
sorry, pitiful, a beggar, mendicant ' and mendax, -acis' given to lying, false, mendacious '; 

perhaps Old Irish mennar^ a spot, mark, stain ', (common Celtic -ns-, -nt- > -nn-), zero 
grade Old Irish m/nd'mark, token, sign, feature, characteristic mark or property' {*mndun.; 
also in the meaning ' a royal headdress, diadem ' = " a mark, indication, proof, sign, token, 
signal ' dass. word), cymr. mann'p\ace', mann geni^ birthmark '. 

References: WP. II 270, WH. II 69, J. Loth RC. 44, 362 f. 
Page(s): 729-730 

Root / lemma: mehn(e)hgh-, mohn(e)hgh-, mijgh- 

Meaning: abundant, excessive 

Material: Old Indie magha-y\. 'gift, present', maghavan(t)-^ rich in gifts, generous '; m. ' 

donor, giver', marhhate^ gives, makes a donation ', maifihistha-^ im hochsten Made 

freigebig, iJberaus reichlich ', mamhana' gladly, willingly'; 

Old Irish men/cc'o^en, rich, frequent', cymr. mynych' often, frequently ', corn. 
menough ds. {*meneggi-, expressive); Gothic manags. Old High German Old Saxon 
manag. Old English manig, menig^much, a lot of, many ', Old Icelandic mengiu. 'bulk, 
mass'; mangr, margr^ many, much, a lot of, friendly '; Old Church Slavic m-tnog'b 'much, a 
lot of {*monogo-), compare also Lithuanian /77//7/a'bulk, mass' {*menia). 

References: WP. II 268 f., Trautmann 189. 
Page(s): 730 

Root / lemma: mehn(9)hk- 


Latin e-mineo, -ere' to stand out, project, reach upward ', im-minere' to project over, 
lean towards, hang down over, overhang, overarch ', pro-minere' to stand out, jut, be 
prominent, overhang, project, extend '; from these compounds are probably -A consecutive 
words to define: minae' projecting points, pinnacles ', minor, -arf to jut forth, project ', 
minax' jutting out, projecting, overhanging '; mons, -tis' a mountain, mount, range of 
mountains ' (hybridization from *montos and *mnti-)\ mentum' the chin ', with cymr. manV 
jaw, mouth ' as */r7/7/c-equatable (out of it Middle Irish manf the place of an unusual 
tooth, gums '); abret. -monid, redirected cymr. mynydd, corn, meneth, bret. menez 
"mountain' {*monlio-), cymr. gor-fynydd' ascension, process of ascending ' (formal = Old 
Irish /b/777/75 'shoulder'); s. also under mehnth-2. 

Old Icelandic m0nir'n6ge of the roof (lengthened grade besides Celtic *mdniio-), m0na 
" tower '; 



related is probably *mohnoh-' nape, neck '. 

References: WP. II 263, WH. II 73 f., 90, 108 f. 
Page(s): 726 



Root / lemma: mehn-2 

Meaning: to step, tread over, press 

Material: Old Indie carma-mnas Horn. PI. " skinner, tanner'; Aeolic piaiEiaai " kicking, 

stepping, treading ' (*[jaTr||Ji), paTsTTraTsT Hes., Denom. from a /77/7-/d5 "getreten'; cymr. 

mati7ru'w\t\r\ Fijften treten', bret. mantra 6s. {*mntr-), gall.-/775/7/5/c»/7(*gestampfter) "way' in 

Petro-mantaion' fourfold road' (= Petru-), i\4anta/o-magus ' S\.raQ>enie\6' , Phrygian PN 

Maviakoq; also Middle Irish meni. "meal, flour, dust, powder'; Lithuanian minu, minti 

"tread, flax brechen, Felle gerben', Latvian minu, /77/?"tread, tan, convert hide into leather'; 

Old Bulgarian *mbng, mgti' to press together ', russ. mnu, mjatb "break, rupture (flax or 

hemp), knead, tread (loam, clay), zerknittern, zerknijllen'; 



gr. ijviov " moss, Meergras ' ([jviapoq, [jviosk; " mossy '), M^oot;, mvoO(; (*mv6Fo(;) "soft 
fluff, underfur ', [jvoTov piaAoKOv Hes., Lithuanian miniava^ Flachsseide, Filzgras '. 

References: WP. II 263, Veudryes BSL 38, 113 f., Trautmann 185. 
Page(s): 726 

Root / lemma: mehn-3 

Meaning: to think, mind; spiritual activity 

Note: extended mehneh-. mnah-ar\6 mneh-, irienei-. mehi- 

Material: Old Indie manyate^ thinks ', Avestan mainyeiteAs., ap. ma/nyahay {\n6o 

Germanic *men-i-o-, = gr. |jaivo|jai " bucket, careen, fly, travel at a reckless speed ', Old
```


## [2026-09-07T16:13:31.789Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Root / lemma: mehn\" POK_full.txt | head -40"
}
```


### [2026-09-07T16:13:31.834Z] TOOL RESULT

```
59303:Root / lemma: mehnA^- 
59352:Root / lemma: mehnd-, mohnd- [mQd-l) 
59376:Root / lemma: mehnd^a, -om) 
59399:Root / lemma: mehn(e)hgh-, mohn(e)hgh-, mijgh- 
59418:Root / lemma: mehn(9)hk- 
59451:Root / lemma: mehng- 
59472:Root / lemma: mehn-1 
59503:Root / lemma: mehn-2 
59531:Root / lemma: mehn-3 
59675:Root / lemma: mehn-4 
59711:Root / lemma: mehn-5 
59733:Root / lemma: mehnth-1, mehth- 
59769:Root / lemma: mehnth-2
```


## [2026-09-07T16:13:35.061Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '59472,59500p' POK_full.txt; echo \"=== men-5 ===\"; sed -n '59711,59735p' POK_full.txt; echo \"=== men-4 ===\"; sed -n '59675,59712p' POK_full.txt"
}
```


### [2026-09-07T16:13:35.141Z] TOOL RESULT

```
Root / lemma: mehn-1 

Meaning: to tower 

Material: Avestan framanyente {: Latin pro-minere) " they obtain projection ', mati- {*mnti-) " 

protrusion of mountain range'; 

Latin e-mineo, -ere' to stand out, project, reach upward ', im-minere' to project over, 
lean towards, hang down over, overhang, overarch ', pro-minere' to stand out, jut, be 
prominent, overhang, project, extend '; from these compounds are probably -A consecutive 
words to define: minae' projecting points, pinnacles ', minor, -arf to jut forth, project ', 
minax' jutting out, projecting, overhanging '; mons, -tis' a mountain, mount, range of 
mountains ' (hybridization from *montos and *mnti-)\ mentum' the chin ', with cymr. manV 
jaw, mouth ' as */r7/7/c-equatable (out of it Middle Irish manf the place of an unusual 
tooth, gums '); abret. -monid, redirected cymr. mynydd, corn, meneth, bret. menez 
"mountain' {*monlio-), cymr. gor-fynydd' ascension, process of ascending ' (formal = Old 
Irish /b/777/75 'shoulder'); s. also under mehnth-2. 

Old Icelandic m0nir'n6ge of the roof (lengthened grade besides Celtic *mdniio-), m0na 
" tower '; 



related is probably *mohnoh-' nape, neck '. 

References: WP. II 263, WH. II 73 f., 90, 108 f. 
Page(s): 726 

=== men-5 ===
Root / lemma: mehn-5 

Meaning: to stay, stand still 

Note: (= /77e/7/7- "think'?) 

Material: Old Indie man- {parimamandhi, amaman) "hesitate, stand idle ', Avestan ap. man- 

" abide, remain, wait, hold on', Avestan fra-man-' persist, stand firm '; Armenian mnam^ 



stay, expect ' ( *mena-); gr. |j£vco, (jifjvu) (|j£p£vr|Ka) " stay ', povn f. ' staying ', p6vipo(; " 
persisting ', fj£|jvu)v " donkey ' ("persistent '); Latin maneo, -e/ie (compare fj£|j£vr|-Ka) " to 
stay, remain, abide, tarry ' ( *meneid), Denomin. mantare " to stay, remain, wait '; Old Irish 
ainmne, cymr. amynedd, mcymr. anmynedd^ patience ' {*an-menia)\ 

Tocharian A B mask- " be, exist '; Hittite mH'm-ma-/" reiuse'. 

References: WP. II 267, WH. II 26, Pedersen Hittite 121. 
Page(s): 729 aaypa 

Root / lemma: mehnth-1, mehth- 

Meaning: to mix up, stir 
=== men-4 ===
Root / lemma: mehn-4 

Meaning: small, to diminish 

Note: partly with u-, uo-, partly with A'-formant 

Material: u-, uo-siercw Armenian manr. Gen. manu ^smaW, thin, fine', manuk^V\6, child, 

knave, boy, servant'; gr. pavu-^a iJOvoKScpaAov OKopoSov Hes., pavu piiKpov (Hs. niKpov) 

'fKQa\xayzc, Hes., Mav6(;, Attic pav6(; (*pavF6(;) 'thin, lax, sparse ', diss, pavov (= pavov) 

Aehtov Hes.; 

in addition as " be isolated ' after Brugmann RhMus. 62, 634 f. (Lithuanian) pavausrai 

TTapsAKETai Hes.; i.e. ' to draw aside, pervert ' and with Diss, possibly Attic pavauaoc; "(* 

who keep away apart from others ' =) " der kleine Mann mit beschranktem Gesichtskreis '; 

ograde Ionian pouvoq, Doric pajvoc;, Attic \x6yoc, (*|j6vFo(;) " alone, occasionally '; Old Irish 

mm {* merih) ' smooth, gentle'; menb^smaW, old Menueh Gen., cymr. di-fanw^ insignificant 

', di-fenwi {*mnu-) " reduce, vilify, scold'. 

With Ar-formants: Old Indie manak^ a little, a bit '; Old High German mengen {*mangjan) 
and mango/on '{r\\ss', Modern High German mangein. Middle High German manc{-g-) 
'lack, disability '; Lithuanian /77e/7/r5S "small, insignificant ', menke^ codfish, cod-like 
predatory fish ', etc.; 

Tocharian B menkT small '; Hittite ma-ni-in-ku-wa-an-te-esHom. PI. "short'. 

References: WP. II 266 f., WH. II 93. 
Page(s): 728-729 

Root / lemma: mehn-5
```


## [2026-09-07T16:13:42.666Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=61190 && NR<=61290' POK_full.txt"
}
```


### [2026-09-07T16:13:43.985Z] TOOL RESULT

```
Page(s): 746 

Root / lemma: mod'^ro-or mafS^ro- 
Meaning: blue; a kind of plant 



Material: Old Icelandic madra^ Our Lady's Bedstraw, Yellow Bedstraw, Maid's Hair, Petty 
Mugget, Cheese Renning ', isl. hvTt-, kross-madra eic. 'Galium boreale, smooth green red 
', Old High German matara^ madder, type of plant ', Old English maedere, maeddrei. ds.. 
Middle Low German mede. Old Frisian m/de6s.; S\ay\c*modrb (e.g. Czech modrf} 'blue'. 
References: WP. II 305. 
Page(s): 747 

Root / lemma: moiso-s or maiso-s 

Meaning: sheep; hide, leatherwork 

Material: Old Indie mesa-m. 'aries, ram', mesh' fleece ', Avestan maesa-^anes, ram, 

sheep'; 

Old Icelandic me/ssm. 'basket'. Old High German me/sfsja' baggage ', Middle Low 
German /77e5e 'barrel'. 

Old Bulgarian mechb^hose', russ. mechleW, fur, hose; sack, bag' (etc.); Lithuanian 
maisas, /r75/se'Heunetz ', Latvian maiss, ma/kss'sack, bag'. Old Prussian moasis 
'bellows'; 

References: WP. II 303, Trautmann 165, Specht Indo Germanic Dekl. 52 f. 
Page(s): 747 

Root / lemma: moRs, Aryan *moRsu 

Meaning: soon 

Material: Old Indie Adv. /77a/rsJ'rash, hasty, bald, early, matutinal', maksumaksu^ right 

away '; Instr. PI. maksubhih, Superl. maksutama-, with nasal: Old Indie marjksu^ soon'; 

Avestan mosu^ immediately, right away'; common Old Indie gh- > ks- 

Latin mox^ soon ' = meymr. moch^ soon ' (out of it Middle Irish moch6s.), Old Irish mo 
soon ', as proverb mos-, mus- : mos-riccub- sa ' I will come soon ', mus-creitfeV they will 
believe soon'. 

References: WP. II 303 f., WH. II 117. 
Page(s): 747 

Root / lemma: molko- 

Meaning: leather pouch 

Material: Old High German malaha. Middle High German malhe^ leather bag'. Old 

Icelandic ma/r'sack, bag', gr. tarent. (joAyoc; 'sack, bag from cowhide '; the inconsistency 



in gutturals is expounded probably through borrowing from |joAY6(;from an other language 
(Thrak. ?) and use from gr. ^for which belongs to k. 
References: WP. II 308; Vendryes BSL. 41. 134 ff. 
Page(s): 747 

Root / lemma: mono- 
Meaning: neck 

Note: in derivatives (esp. with formants -T, -io-) also ' necklace, Halsschmuck' 
Material: Old Indie manyai. " nape '; Avestan minu-^ Halsgeschmeide ' (/from Avestan a) 
and with lengthened grade manao&rf neck, nape ' {*mon-eu-tro-)\ paon. pov-anoq, -wnog 
" bison ' ("mahnenartig'); gall.-gr. [javiaKr|<;, fjavvo(;, pavvaKiov "collar, neckband Celtic 
Volker' (povvoc; Doric?); Latin /77c»/7/7e "collar, neckband as jewellery' (from *monT-as Old 
Bulgarian moni-sto); Old Irish muin-^ neck ' in muin-torc^ necklace ', muiner neck 
\*moniklo-), cymr. mwn, mwnwgr neck '; Old Irish /b/7r7/75e "shoulder' {*for-monio-)\ Old 
Irish muince' collar| neckband; chain for neck ', loanword from acymr. minci^ necklace] 
collar; collar (for horses and other animals) ' (from mwng^ mane ' + ci, see above S. 518); 
from *moniio-^ neck ': cymr. /77>77yo'o'" mountain', corn, meneth, abr. -monid, bret. menez 
ds.; Old Icelandic men. Old English mene. Old High German menni {*manjan) " 
Halsgeschmeide ', Old Icelandic mgn. Old English manu. Old High German mana 
(Germanic *mand) " mane '; Old Church Slavic mon/sto 'coWar, neckband', polab. 
m/me/st/a' coral '; with formant ff. Middle Irish mong' mane, hair', cymr. mwng^ mane ', 
Old Icelandic makke " oberer Teil des Pferdehalses ', Danish manke " mane '; perhaps 
here lllyrian (paeon.) jjovanoq, -wnoq " bison ' ("mahnenartig'); 
References: WP. II 305, WH. II 108, Trautmann 169, J. Loth RC 45, 196 ff. 
See also: compare above S. 726 men- " tower '. 
Page(s): 747-748 

Root / lemma: mori, mori 
Meaning: sea 

Material: Latin mare, -/sn. (/-stem; Gen. PI. /775/'^/r7 secondary; with unclear a); Old Irish 

mu/rGen. moran., cymr. corn. bret. mor'sea', gall. Mor-/m, Aremori-aVN " 

f 

IVIeeranwohner ', mori-marusa^ mare mortum '; PN Mori-dunum'moo'c '; Gothic mareii. 

"sea'. Old Saxon men. Old High German man, mends. (-/77-stem); Gothic man'-saiwsxw. 

"sea'. Old Icelandic marr. Gen. mararm. " sea'. Old High German man, meri{Gen. meres)
```


## [2026-09-07T16:13:53.577Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"manao\" BRT.txt | head -20; echo \"--- minu ---\"; grep -n \"minu-\\|minu\\b\" BRT.txt | head -20"
}
```


### [2026-09-07T16:13:53.639Z] TOOL RESULT

```
10095:KompA.,  E.  —  Vgl-  'gayit-  EN.  —  Zum  V. 'gay-.  —  ai.  j,'äya-  m.  'Familie;  Haus  und Hof;  s.  f;ac%ä-.  —  Pü. :  yäii,  Sü.:  jhilam.  — I)  D.  i.  dai  Leben,  wie  es  dem  guten  Sinn {den  Gutgesinnten)  tu  teil  wird;  vgl.  ahüm yj  vau/üas  mananhö  Y.  ^3-  Si  Tiaakhis  äyafilä manaahö  Y.  zS.  7 ,  vaakhis  mäyi  manaahö Y.  4t-  2,    Tiahiitim   .  .  vanhfiii   manaoAö   Y.
11258:•  g.  äazdah'vant-  Adj.  'einsichtig,  ver- ständig': yä  manaohrlHaA.)  'äöaghvantsm ar}^ahyS  Y.  44.  5;  —  hyai  urvalsm  (sd.) "dönifkvadtbyS  Y.JI.3.
11761:surunvata  yasna  tarn  yjzäi  . .  arfdvJm YL5, 9;  /7.  3;  —  la  hasHt  upa.sbayeiU tqra.-fravalayS  Yt.ij.ög;  —  .Ja  nipa- yemi  vispa  vokü  Yt  5. 89;  —  harn  taät (NDm.)  bJeus  baratö ..  tistryasi'a ..  daFvasca .  .  la  (Sp.  615  m.)  yaitya^S  Yt.  S artikelhaft:  //{AD£)  aifam  paili  sruye(sä.) aZsa  druxs  upa.dvqsaiti'S ."j.  24'"';  — ya^a te  vTspe  aurvanta  zasvauha  (sd.)  paili. jasqnXX.  ^.\%t\  ;o.i2S;  —  ta  nS  data  tä (Sp.  6 1 5  u.)  fravaocäma  Y.  70.  2 ;  —  ava  Al baraytn  läshm  dauru{'si.)  upa  tqm  manao- ürTm  "sie  sollen  ihm  . .  am  Hals  anbringt V.  ij.  30;  —  minutn  barat  andvl  .,  upa tqm  srirqm  manao^rim'Vt. 5.  i2T. titn  urva^fm  /rayavaySiJ'(sä.)  sna^äi  Yt. 7.  24;  —  i^m  valmcit  yazamaide  "(ihn) den  f. , ."  Yl  75. 1 ;  i;  —  äal  t>m  varpm kfrsnava  V.  2.  25;  —  avavanOm  asa- vaynyäi  (sd.)  tqm  ä^qm  dagtayJ  V.  5. 14;  —  ä  tai  :^ami5  yasamaide  Vr.  ig.  a ; Ytö.iä;  —  nöit  kl  tä  vlsB  tilyul . . apaili.- buili  haca  vTiibyS  para.baraiti  (sd.)  V.  13. 40(?);  —  nava  äfs. .  navata  baiiacajipsa V.  21.  3  (?);  —  s.  noch  Yt.  10.  6,  i§.  49, V.p,  29;  s.  Sp.  616  o.  bb)  mit  rela- tivischem  Anschlüsse' ;  a)  im  gAiv.:  at  tSng dngva  ySng  asalefl  vazdrJng p,lt  gä fror»' f^{s6..)  Y.4Ö.4;  —  t3is  . .  yäis  daiäis  . . ^,46.  15.  B)imjAvr.:  tat  drvais..ta! . .  pairi.urvalstsm  yat  tamS  voku  Yt. //.  a; Y-jÄ  I';  —  ta  (NPn.)  ns  ama  ta"  . . uxjamyqn  yä  staota  yestiya  Y.  55.  3;  — ta  vanukJ?  tä  vahisth  yazamaide  ya  .  . fravasayö  Yt. y.  27;  —  tä  .  .  upastqm k^Ttti  dahiita  ya  fravasayS  Yt  13. 17;  76;
16796:3,  3;  —  aomca  sükim  yim  baraiti  iarS masyS  "und  jene  Sehkraft,  die  besitzt  .  ." Yti4'29;  —  amimca  vfr}%ra-^ti?mca  .  . yim  asps  arsa  baraiti  .  .yim  ^raitaonS .  . barat  Vti4-Z9i  39'i  'i  —  asim..  bar  in- tim vispi  baslasa  "die  A.,  die  alle  Heil- mittel besitzt"  Y.  52.  2.  a)  mit  einer örtlichen  Bestimmung,  uzw.  i)  des  wo? durch  Praen.:  minum  barai  .  .  ar7äv! ..  . upa  . .  manaohrim  "einen  Schmuck  trägt .  . A. ..  am  Hals"  Vtj.  127;  —  mit  hilbaröit upa  kawm'ii.28;^bäoa  %2fam  tarasia  . . 3^arf%a  bairyeinteW.j.aij.  2)  des  wo- hin?; a)  durch  Adv.:  Ava  .  .  irislanqm tanüm  baräma  kva  niäa^äma  "wohin sollen  wir.. tragen, wo  niederlegen?"  V.tf.44; —  s.  noch  Y.  65. 6  unter  3.  b)  durch Praen.:  tsi  abyä  (zu  3  b)  bairyaiiti  vattkSus ä  dsmäni  mananhs  "die  werden,  von  den beiden  hinweg,  in  das  Haus  des  VM.  ge- tragen werden"  Y._y2. 1 5 ;  ungeschickt  ver- wendet V._^.  2g,  s.  c;  —  yö  upairi  hunartm (sd.)  manB  barät  P._j7 ;  38^  (?).  c)  durch Dat:  ya%a  nä  däityö  *daityäi  (Sp.  729  m.) *bairyäi/aS^  *x^airyeti/a  V.J.  40;  —  tl Sbya  (Sp.  10  m.)  bairydnie  yaisqjn  .  .  V. j.  29(s.  b).  d)  durch  Akk.,  verbunden
19715:•  j.,  g.,  p.  'man-  V.  'denken',  Fraes.  i man-,  a6  mainya-,  maniya-,  30  (Iter.) mqnaya-,  s-Ko\.  i'>  mar?A-,  mfngh-;  Perf. I  mamati'-.mamn:  —  PPfP.  mata-,  PFP. 'mahiaa-.         S.  noch  zu  ^manao^rJ-.
19759:•  g.  'manaodri-  f.  'Gemahnerin  an  — ' (Gen.),  mit  Akk.:  u^  arJm.p&wa(sd.)  x/a- pa^a  yä  °5/l/(NP.)  catdBnghaanbm  an- ^aAya  ". .  die  den  Veisändigen  an  seine Pflicht  gemahnen"  Y.44.5.
19761:•  j.  'manaoSri-  £  'Hals,  Nacken',  uzw. a^anscher  Wesen'' :  "an"  F.  jg;  —  minum barat..ar3dvlsära..upa  tarn  srJrqm'^rim Yt5. 127;  —  ava  hl  (nämLjfi«J)  baraytn taihm  dauru  (sd.)  upa  tqm  «Srüw  V.7_j,30.
22307:Sinn,  sva.  'zu  höchster  Entfaltung,  Grösse und  Schöne  bringen'" :  vakislim  . .  maedai oval  xsdirgm  hyat  ksi  voha  vaxsal{?io'üy') manatihä  ". .  das  Beste  ,  .:  jenes  Reich des  M.,  das  ihm  VM.  erhohen  wird"  Y. J/.  6;  —  vatahsul  xSa^rä  manavhs  asä mat  ärmaiti}  vaxft  utayBill  tpvlil  "die Reiche  des  VM.  wird  zusammen  mit  Ala Arm.  erhöhen,  den  Bestand  und  die  Kraft" Y.j.^.  11;  — ya  (nämi.  *"3i^rJ)  därayat vahütim  manS  tä  masds  tnainyB  uxiyS yS  , .  "welche  (Räume)  der  beste  Sinn inne  haben  wird,  die  erhöhst  du,  o  M., durch  den  Geist,  der  .  ."  Y.  31.  T,  — damqn  .  .  *yam  ddial  ahurS  mazdi  .  . %ra0ita  vohu  manaoha  vaxst  a/a  "die Wesen  .  ,,  die  AAAf.  geschaffen  hat  .  ., (die  er)  durch  VM.  vollkommen  machen, durch  A.  erhöhen  wird"  Vr.  J2.  4 ;  —  vaAa itxsyä  maftavAa  xsa>rä  asäcS  us'/J  taiiüm ,'durch  VM.  erhöhe,  durch  XI  und  A. nach  Wunsch  den  Leib"  Y._y_?.  loS';  — al  tsi  laväis  vahtmm  (sd.)  vaxsai  Y,  48. 1 ; —  vgl.  asaoxsayant-.
23552:KompA.,  E.;  Ableit.;  vAbleil.  —  lEt.  a.  unter v.Ular..  —  mp.  västr.  —  Pn.:  västr;  aber  tu Y.  33.  3 :  vartJläri),  lu  Y.  33.  4,  44-  'O,  S'- 14,  j*.  4:  käri).  —  OVgl.  lUI/JZ/ny-.  vä-va fehhinPü.  — »)Vgl,y.jo.io:  ä  huhtSS  vaa- lüu!  manaohS  .  .  asaSyäcä.  Beide  Anadrücke besagen  das  selbe.  —  3)  Der  DS.  'räd  sehr prägnant;  a»a.  'damit  sie  seine  Weide  sei', inünitiTiscb.  VeI.  iSl  Bthl.  IF.  j.  356.  — 4)  Weil  man  västr'  mit  varit'  verknüpfte ;  und DsT.  ZA.  r-  113,  230  glaubt  an  diese  Etjrmo- logie;  s.  IFAni.  6.  43.
24432:•  j.  irispa.®«urva-  Adj.  -  ? -:  püirs 'vö  urvijKOoto  urvi.vir»%rB  stvi.manao^ris Yt.5.30.
26248:faiS..:^aiai^(iA.)  \.34.ii;  —  vafdäJ  \.^i.\^-,32.ft;  —  diidi  mäi . . awLmOii läsnanqm  fsd.^  jqm  . .  ilttl  aii  a^rS  hainsti  ipfniää  maiitrü  wuttdJ  briHrntj' Y.4A. 3.  yüiti  manaoAä  r-t-Aä  •mihi  "scfafnk  mir..
26796:•  j.  stri-manaoÖTi-''  Adj.  (auch  mask.) 'mit  starkem,  derbem  Nacken':  pu^rö  ,  . =m(NSm.)  Yt.p.30.
27431:—  upa  tqm  'rqm  manao%rim  Yt.5.  la?;  — 'ra..daimäna  YL70.107;  —  ■'ra(NDm.) vä  aahm  bäzava  (sd.)  Yt.  5. 7.  b)  von Tieren:  aspahe  hhrpa  .  .  'rahe  YtÄ  18; Yt.  14.  7,  23,  25.         c)  sonst:  unaranam
28619:—  jahikayai:  mJ  Al  (fem.)  avi  pahm ava.hilta  Yt.j7.57;  N.jo  (nSit  At);  — zaohrä  .  .  bansma  .  .  pasUm  .  .  ma  Al (Plur.)  mairyS  g»urvayöil  (Sp.  537  o,)  .  . yai  sl  mairys  gpurvayai  Yt.  A*.  s8ff.;  — ipa  . .  ava  Al  baraym  . .  djuru  upa  tarn manaoisnm  V.jj.30;  Ä.S',  9.40,  49; — yS imqm  zqm  aiwi.vfnsyöti  . .  upa  hl  (fem.) gasrwm  baraiti  V._y.3S;  YL/7,21,  V./5.43 (zu  a);  —  p)r?sat  sarahuilrs  .  .  paiti  it aoxta  ahurS  mazd'j  H. /.  iE;  J,  A.  4-6. P.  27,  FrW.  10. 40;  —  iiyri/  . .  lata  dim ahurS  mazdä  avan  . .  pairi  ll  .  .  mihrS
28731:haomanaohimna-
--- minu ---
26928:mit  frä  Med,  'sich  womit  (Akk.)  breit, augenfällig  machen,  womit  Staat  machen, etwas  prunkend  zur  Schau  tragen'; vantäiahs  .  .  frä  gaosävara  sispimna (NPm.)  cä^ru.karana  minu(sd.ya  zaranyS.- pisi  ". .  ein  vierkantiges  Ohrgehänge  zum Staat  tragend  und  .  ."  Vtij.  10;  —  */ra *gaosävara  sXsp^mnaQiSf.)  ü^ruJtarana .  .  ar»dvX  YL5.  127;  —  andvT  .  .  frä srTra  *'zus  sispata  *urvaiH  basujtaoyehi '^A.  .  .  herrliche  Sachen  trägt  sie  zur Schau,  die  anmutige,  ■ ,"  Ytj.  7.
27909:•  j.  zaranyo.pis-,  **pi9--  Adj.  (auch  fem.) 'goldgeschmückt':  yS  paoiryS  °pTsS  srirä barssnava  ginwnaiti  "der  als  erster  die goldgeschmückten  .  .  Höhen  erklimmt" Yt.  JO.  1 3 ;  —  fr3  gaosavara  sisptmna  .  . minu{%A.)ca  -/m  (ADf.)'>  YtJj.io;  — ya^a  vil  *>r?tats.pai'hi  (sd.)  yaia  vä *-pafki  {K'Pa.)''^  ydha  v<t  *kilat  gaonaiiam Aog.  ly.
```


## [2026-09-07T16:14:01.960Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"•  j.  minu\\|• *j\\. *minu\\|minu-  \" BRT.txt | head; echo \"=== grep minu headword ===\"; grep -n \"^• .*minu\" BRT.txt | head; echo \"=== mati ===\"; grep -n \"^• .*mati-\" BRT.txt | head -20; echo \"=== framany ===\"; grep -n \"framany\\|fra.many\\|framqny\" BRT.txt | head -10"
}
```


### [2026-09-07T16:14:02.097Z] TOOL RESULT

```
=== grep minu headword ===
8245:•  J->  S->  P-  UP^  1)  Praea  i)  mit  Akk.; a)  räumlich,  a)  "hin  -  zu':  mi%r)m  yO  .  . fravazaiU  Aaea  karsvar»  yat  arjsaAi  'pa karsvar»  yat  ifaniraitm  Yt  lO.  67;  — "iräyS  °pa  naz'a.paötm  (sd.)  asatUi ..bar^is V.9,11;  Vd.J2;  —  ui'trö  .  .  yS  kapm aipi.spayeiti  spaeitit^m  upa  vayoan»ni Auxmao%re  (sd.)  .  .  YL/4.13;  — para  te gaosp^nta  .  .  hao^asca  . .  *fraisyämaAi  naz- dista  upa  . .  raocä  . .  P.  34.  ß)  'bei, an':  ipanS yöi  hislmte  a:^arö  °pa  ^^anntjm V.  13.28;  —  tqm  yazata  ..  °pa  zrayi^ vouruJcaam  Ytf.iiö;  33,  38,  54,  72,  76, /2.16,  /5. 19,  27,  31';  —  *"/a  *mailUn (sd.)  barfsatiham  ^.3.20;  —  at-a  tu  anya mays  äitt  (sd.)  JasOit  .  .  paoirim  °pa mayiin  ..  tanüm  pairi.yaozdai^ita'^ .<).^\; 31',  Ö.38,  5.54;  —  minum  bara^ ..  aridvl
11690:•  j-  "^y^-  V.  'debilitare,  minuere*.  Praes. \\  jina-,  »7  (Pass.)  j^'o-'',  —  Inf /oyat'*.
19761:•  j.  'manaoSri-  £  'Hals,  Nacken',  uzw. a^anscher  Wesen'' :  "an"  F.  jg;  —  minum barat..ar3dvlsära..upa  tarn  srJrqm'^rim Yt5. 127;  —  ava  hl  (nämLjfi«J)  baraytn taihm  dauru  (sd.)  upa  tqm  «Srüw  V.7_j,30.
27909:•  j.  zaranyo.pis-,  **pi9--  Adj.  (auch  fem.) 'goldgeschmückt':  yS  paoiryS  °pTsS  srirä barssnava  ginwnaiti  "der  als  erster  die goldgeschmückten  .  .  Höhen  erklimmt" Yt.  JO.  1 3 ;  —  fr3  gaosavara  sisptmna  .  . minu{%A.)ca  -/m  (ADf.)'>  YtJj.io;  — ya^a  vil  *>r?tats.pai'hi  (sd.)  yaia  vä *-pafki  {K'Pa.)''^  ydha  v<t  *kilat  gaonaiiam Aog.  ly.
27912:•  j.  *zaranyö.tninav-  Adj.  'der  goldenen Halsschmuck  trägt":  vaim  saranyB.pusim  . . ^'minum'^  ..  zaranyS.v^iim  Yt/j.  57-
=== mati ===
8063:•  g-,  j.  isya-  Adj.  (fem.  "yä-)  i)  'erwünscht; begehrenswert':  kä  %wsi  asa  äkä  (sd.) andrang  'yl  Y.4S.%;  —  asahyä  >wj.i  (sd.) aslm  yqm  'yqm  "den Preis ..,  den  begehrens- werten, welchen  . ."  Y.54.r._  2)  von Personen  'lieb,  traut':  b?rfx<iqm  nwi  .  . daldöist  (sd.)  k}krp7m  damaysi  vauhuyäi yqm  Asi  'yqm''>  dälB  x/ayqs  mazdä  ahurB . .  äzdyäi  (sd.)  "den  .  ■  Leib  der  lieben (Jungfrau)  .  .,  welcher  der  Herrscher MAh.  es  gewähre  für  ihr  gutes  Ich  .  . zu  gelangen"  Y.5^.17;  —  hyat  *aS>ia>ihz dngvats  S»äna  °y}ng  avAayS  (sd.)  Y.js, 16.  a)  insbes,  von  'airyaman-  (sd.): il  airySmä  (sd.)  "yö  rafooräi  jatitü  Y.  ^4- 1;  V.  22.9,  19,  20,  a)  mit  'airyamati- (sd.,  auch  fdSt):  mryamamm  'slm  Vr,  2. 10;  usw.;  —  airyamattö  °ye/ie  Vr.  j.8;  usw.
=== framany ===
4786:vaams  tisit  framanyents  "laufend  kommen sie  (nämL  mthrSjlrujB)  nicht  vom  Fleck, reitend    machen    sie    keinen   Fortschritt/, fahrend  gewmnen   sie  keinen  Vorsprung" Yt  jo.ao.  2)  'übergehen,  auslassen'"':
14892:causa':  ySi  vanhd^ra  framanydnte  (sd.) VJtar».qzahyekeca  'ti ..Y.  6^.  13.  S) 'ge- mäss'(?);  AämS.fyaokna  .  .  bavainti  a^ahe 'ti  pantqm  alahe  °ti  mq'^r>m  asahe  °ti /rasastlm  Y.4-  43.  ^)  ^ur  Bezeichnung
18857:•  j.  "lüuiti  As  aSe  ysi  mafyäAa  ^aranti framanyäe  V.  7.  55 :  —  ?  — .
19736:aät  fra  -?-:  "»la»!*' (sd.)  An  aOt  ySi ma^äia  ^ar^nti  framanyete  V.  7.  55.
19750:mit  fra  'aushaireu':  ySi  varghä^ra  (sd.) framanyättU  vSan.aza&yeAeca  patH  .  .  Y. 68. 13.
19753:tacints  ndit  apayanti  (sd.)  bar^nlS  ttSiJ frastanvanti  vazjnts  nSil  framanyente  Yt.
22468:•  j,  vaDha'Ora  Adv.  'an  dem  Ort  des Aufenthalts':  ySi  V  framanyeinte  vltan.- qtahyeheSa  paiti  "die  an  ihrer  Stätte  aus- 1 harren  zum  Zweck  der  Überwindung  der Not"  Y.6S.i3'\  I
23166:1)  'fahren';  i)  Irans.;  a)  von  Zugtieren sva.  'ziehen*:  srao&m  ..yim  ..  aurvanlS .. vatmti  Y.57.  37;  Yt.  ;o.  68,  47,  77. 12;  — aurvants  . .  vazimna  yim  vohüm  sraohm Y. 57.29;  —  s.  noch  'vazäna-,  b)  vom Wind;  a'hra  pascaUa  vazaite  vätB  .  . varymca  maiy>mca  fyanhumta  avi  ('hin zu  . .')  asä  . .  YL<y,  33.  c)  vom  Fahrer, sva.  'lenken':  y&  *paourvS  väsim  vataite VL5.  11;  —  s.  noch  Absol.  2)  intrans.; a)  von  Zugtieren:  ahmya  väse  vatänte ("a^warS  aunian/s"a.ndtmW^enz\eheTi,," YtJO.iag.  b)  vom  Fahrer;  Akt  und Med:  dahmS..  banmnS  vä  vazimnS  vS ". .  reitend  oder  fahrend"  N.  J7 ;  —  talints . . barmtB  .  .  vaz?nts  nSit  framanyenU  (sd.) "laufend  . .  reitend  , .  fahrend  . ."  Yt  10.  ao; —  fravaiayB  . . ya  aojislä  vaz>ntqm  Yt 13.  a6;  —  ahmya  *vasa  (sd.)  vazsmna (NSf.)  Yt  5.  n ;  —  dasimm  hl  upa  ar^m vazaite  .  .  sraess  Ytro.  100;  100,  laö', 70;  —  vTspS  hl  ypa  *ar^j  vastnti yä  apB  Yt  10.  100;  —  mi^r)m  ,  .  ys vUpähu  harsvShu  .  ,  vataite  ^ar»nS.dä YtJO.i6;  107;  — yat  d^ra  para.jasaiti vaztmnB  (näml.  mihrB)  Yt.70.  loi;  86, 74. 2 ;  —  nixiata  ahmät  vazata  atarl YtJO.  127.  c)    von    Heer  und   Volk
```


## [2026-09-07T16:14:11.575Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'bleiben\\|bleiben, warten\\|'warten\" BRT.txt | head -20; echo \"=== upa.mati ===\"; grep -n \"upa\\.mati\\|upamati\\|upa\\.mai\" BRT.txt | head -10"
}
```


### [2026-09-07T16:14:11.633Z] TOOL RESULT

```
19443:i)  'weilen,  wohnen':  va^hu^  sraols mitayatu  asisvatsuki  tha  mi^natu'^  Y.io.i; — yahmi  zl  kacit  tanunani  dräpHim  (sd.) . . mag^aine  mi^näj  Y.  16. 10.  2)  'bleiben': ya^a  granis  .  .  mtimaUi  miäsra  Yt  10. 39.  3)  'dauerad  vorhanden  sein':  tia mi^thit  .  .  ai?iAai  gunäayäi  (sd.)  V._j.  32,
19741:•  i*i  E-i  P-  "nian-  V.  'bleiben;  warten'. Praes.17  flM»)'a.,3o(Iter.,Kaus.)MdUni>tf-, mqnaya-.  —  AbsoL  •maittm.
19742:1)  'bleiben',  nur  Kaus.  'zum  Bleiben zwingen,  aufhalten,  im  Wege  stehen':  at akfä  ma  bSndvak/a  (sd.)  mätiayätt  ^aZsS Y.4p.a.  a)  'warten  auf—,  erwarten': Wpatava^  vJ'itmiit^  ata  mam  amanaye^ yäta  adam  arasam  madam  Bh.2. 1 1 ;  6, 9.
19743:mit  upa  'warten,  ab-,  zuwarten';  a)  mit Angabe  der  Dauer  des  Wartens  durch Akk.:  navoMapanm  ufa.mqnayM  <UU ySi  masdayasna  , .  pascaSa  . .  "neun  Tage sollen  die  Af.  warten  , .;  dann  . ."  V.j.  42; Vd.  //;  —  Äff/  dra/S  upajHqitayfn  .  . '^rixlapanm  upajnqnaytn  "wie  lang  sollen sie  zuwarten?  . ."  V.  5. 53!;  —  s.  noch AbsoL  b)  mit  Angabe  des  Endpunkts des  Wartens  1)  durch  mai  mit  Instr.  eines Nom.  act'':  inai  eu^ranqm  /roMuxii  mcU voitranqm  tnhaiii  upa.mqnayfti  "man  soll warten,  bis  die  Schuhe  ausgezogen,  bis  die Kleidet  at^elegtsind"  V.6.27.  ß)duidi vUp»M  a  ahmat  y«f  "usque  eo  donec*: vTtpitn  a  ahmäl  upa.mqnaytn  yaf  Ai  .  . varta  AOu  bavaj  V.  S.  38.  VgL  noch AbsoL  A)  bes.  vom  Ausbalten  da Trauerzeit  nach  dem  Tod  eines  Ange- hörigen, während   deren  das   Sterbehaus
19751:np.  mättdan  'bleiben',  nbll.  mänaf  'müde  ver- den';  at  mamandhi  (usw.?,  KZ-ig-^xi),  vgl. Pü.:  MmäBff(?,  WZKM.i?.33o).— Pii.:wänfl'<iK, pälan,  (inY-^^p):  minhütan,  (inY.tfc*):  mem- tan  (wie  für  ^mart-).  —  Vgl.  nmänaya-.  — I)  Eig.  'warten  unter  gleichzeitigcT  Betätigung von  -'.  —  >)  Wie  aus  V.  13.  3  heryonagehen scheint  —  3)  Pü.:  mäneiict.
=== upa.mati ===
7485:•  j.  "äste  Inf."'  ('zu  siuen'),  mit  Absol. 'in  dem  (durch  das  Absol,  bezeichneten) Tun  dauernd  verharren':  uxme  xraiwe yaonsm  (sd.)  ä'  ¥..^.45;  —  cvat  dräjö upa.maitim  (sd.)  ä"  .  .  V.j.53;  54.
```


## [2026-09-07T16:14:29.984Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD umme ===\"; grep -n \"ummēd\\|umme_d\\|ummēt\\|omēd\\|ōmēd\\|hope\" PHD.txt | head -20; echo \"=== PHD man ===\"; grep -n \"^mān\\|mānistan\\|mānēn\\|to remain\\|to stay\" PHD.txt | head -20"
}
```


### [2026-09-07T16:14:30.047Z] TOOL RESULT

```
=== PHD umme ===
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
2309:hope ēmēd, ummēd.
2310:hopeful ummēdwār.
2311:hopeless anumméd.
=== PHD man ===
440:mānbed
452:mānbān [m?np?n!] watch-dog.
453:mānbed [mnpt'] master of the house.
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
724:māništ,
3376:remain (abaz) mandan, (mānistan), padan, pattüdan ; — over parréxtan.
3806:stay abaz padan, mandan, (mānistan), pattüdan, win(n)irdan.
4898:māndagīh māndag, mānīg māništ māništag
4899:mān
4964:kadag man-t mānistanī
4965:māndanī
```


## [2026-09-07T16:14:38.550Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 236 (p215) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==237' HRN.txt | head -60"
}
```


### [2026-09-07T16:14:39.764Z] TOOL RESULT

```
=== HRN leaf 236 (p215) ===
PMMi
«iE
- 215 ^
wa;K. müm, aar. mäm 'Grossmutter ; af/. mäml'Tdnte;
gr. jLidinfia^ ^afA.fA.riy jLta/4f.da *Mama, Grossmutter ; lat.
wamma, wammula 'Mama, Grossmutter ; ahd. muoma,
mömä 'Muhme y Tante (zumeist aus Fick, Vergl.
Wörterb. ^ II, 182, sowie Delbrück, Verwandtschafts-
namen S. 73, 97).
^4. man 'Haus'.
ap. maniya- 'Haus' (die elamitische Version be-
stätigt nach freundlicher Mitteilung Jensen' s diese
Übersetzung); phlv. man *Haus* (für aw. nmäna')^
mcln(i)5n, man(i)st (Salemann, Litbl. f. or. Phil. II, 82)
'Wohnung', mänpan, man{i)stan, man{i)stan Vohnen'.
Dazu auch np. münden 'bleiben, sich aufhalten
(No. 966).
Die von den Wörterbüchern überlieferte Bedeutung
'Hausgerät' kann ich für man nicht belegen, auch nicht
in der Verbindung ;^clw u man, wo nur zwei Synonyma
formelhaft zusammengestellt sind (ganz deutlich z. B.
äähn. I, 44 Vers 179 ; Vis und Ramin S. 60 Vers 12,
65 Vers 4, 77 Vers 18). Die Vergleichung mit arm.
aman *Gefäss', syr. JXD 'Gefäss bleibt also zweifelhaft *).
965. -man '-Sinn, Gemüt' in peiijman, sad\man, qehr\man
u. a. xn.
aw. vergl. a^nö.^manah- u. v. a. m. ; phlv. pasmuln
(päz. pasämün); ai. vergl. -manas-.
Zu mand. WXD 'Geist' oder wohl noch besser 'In-
telligenz' vergl. Nöldeke, Mandäische Grammatik
XXXII; hierher oss. -mmi in däU\inon 'unterirdischer
Geist', väli[mon 'himmlischer Geist' (190)?
np. serman *löwengleich' wird auch 'löwensinnig
sein, wennschon natürlich auch die Ableitung von
manisten (No. 967) 'gleichen, ähnlich sein' möglich wäre.
966. münden 'bleiben ; lassen', manlden {manlde, Sahn. II,
840 Vers 1198).
g. menadmün.
*) Vergl. auch I^öldeke, Pers, Stuclien II, 40 (Correqturnote),
```


## [2026-09-07T16:14:45.942Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==238' HRN.txt | head -50"
}
```


### [2026-09-07T16:14:47.158Z] TOOL RESULT

```
ap. Vornan-, amänaya 'es erwartete (mich)'; aw.
l/^mafi', iipa mqnayen *sie sollen abwarten*; phlv.
man(i)sn, män(i)stan, päz. mändan ; arm. mnam 'bleiben,
erwarten, aufwarten, übrig bleiben (H. No. 204) ; lat.
maneö; gv. /.ihw,
kurd. main 'bleiben'; bei. mänay, pp. mantä *müde
werden* (233), vergl. np. mande *müde' (afy. LW. mända,
kurd. mdndu 'müde', H.-Sch.).
967. mänisten gleichen, ähnlieh sein*, mänend ahnlich',
y
mäHd 'wie es scheint* (bahn. I, 156 Anm. 10, Calc).
i/^tnan' 'meinen, halten für', vergl. aw. mqnayen alw
ya&a 'ebenso wie, gleichwie*.
Nöldeko (mündliche Mitteilung) stellt dagegen np.
mänisten zu [/^niä-^ skr. mäna- 'Bild, Erscheinung;
Ähnlichkeit (spät)' vergleichend.
968. '»nah, meh *Mond, Monat' ^).
ap. müh' 'Monat'; aw. mäh- 'Mond, Monat*; phlv.
mäh; ai. mds- 'Mond, Monat'; arm. amis- 'Monat' (H.
No. 13).
kurd. LW. meh 'Mond, Monat'; afy. tarög[mair
'schwarzer Mond', d. i. 'Nacht ohne Mondlicht', spög]-
mm 'helle Nacht', miyOst 'Monat' (aus *mai]astj Darme-
steter, CXXIII); oss. d. mäyä, t. mäi 'Mond, Monat'5
bei. LW. mäh, mä, n. maha (158) ; wa;<. mHi^ sar. mäs^
§iyn. mSst, minj. yomya, sangl. dul[fnik ('Vollmond').
Daneben erscheint auch eine Form mit Nasal: np.
mäng 'Mond', g. mäm, kauk.-bergjüd. meng,
969. mahl 'Fisch'.
g. müsü (d. i. mäsü), vergl. mäs mäht (AM. 24
Zeile 4).
aw. masya- 'Fisch'; phlv. mählk; ai. mätsya- 'Fisch*.
I) In Yls und Bämln kann man manchmal auf einer Seite die
vier Bedeutungen : 'Mond, Monat, Mondgesicht, Medien' lesen.
Ar. mäSiy 'weisser Honig', moMyat 'glatter Panzer; "Wein* (dazu
wohl auch mär^ *good natured, gay, jovial* bei Johnson) erklärt
Nöldeke bei Weber, Monatsber. BAW. 1879 S. 812 als 'raedisch*;
daraus sind entlehnt skr. ntädhi', mafhi- 'Ringelpanzor*.
```


## [2026-09-07T16:14:53.094Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==218' KNT.txt | head -40"
}
```


### [2026-09-07T16:14:54.597Z] TOOL RESULT

```
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps,
```


## [2026-09-07T16:15:01.585Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^man- vb\\|man- vb\\.\\|amānaya\\|amanaya\" KNT.txt | head -10"
}
```


### [2026-09-07T16:15:01.637Z] TOOL RESULT

```
2928:(e) In a volition, object of a verb of mental action, without conjunction: tya amanayaty kuna- @пайу DSI 3f ‘what I thought I will do’.
3606:63 :cità : mim : amanaya : Árminiy&ty : yata : adam : arasam : Madam
5767:tman- vb. ‘think’: Av. man-yele, Skt. mán- yale, Gk. utuova ‘(I bave thought of,) I desire’, Lat. memini ‘I remember’, pIE *men-. See also manah-. maniyary lst sg. mid. (§214, 5238.1) DNb 38. amaniyazy lst sg. imf. mid. (8214, 6233.11) DSI 3f. mantydhaiy 2d sg. subj. mid. (831, $222.11, §234.1) DB 4.39 (manl. . .); DPe 20 (maniydhay, $27, 552.11); DNa 38 (maniya- [...); XPh 47 (maniyaty, without the h*: $27, $52.VI, Lg. 13.302; Hz. AMI 8.66, ApI 243-4). maniyál|taty) sub). mid. (5222.1) DB 4.50.
5768:^man- vb. ‘remain’: Av. man-, iterative pres. manaya- (8123, $215), Gk. pvo, Lt. maneo; prob- ably specialization of pIE *men- ‘think’ (see ‘man-) in meaning ‘remain thinking. amdnaya imf. DB 2.48, 63; amünaiya ($48) DB 2.28.
```


## [2026-09-07T16:15:08.028Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 5768 (1-based)\npre='\\n'.join(lines[:5768])\nprint('leaf(0-based)=',pre.count('\\f'))\nEOF"
}
```


### [2026-09-07T16:15:10.479Z] TOOL RESULT

```
leaf(0-based)= 226
```


## [2026-09-07T16:15:18.642Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==227' KNT.txt | grep -n \"OLD PERSIAN\\|LEXICON\\|^[0-9][0-9][0-9]\" | head; echo \"---- headwords on that leaf ----\"; awk 'BEGIN{RS=\"\\f\"} NR==227' KNT.txt | cut -c1-60 | head -40"
}
```


### [2026-09-07T16:15:19.960Z] TOOL RESULT

```
---- headwords on that leaf ----
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; А
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media�
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418;
(2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10
tman- vb. ‘think’: Av. man-yele, Skt. mán- yale, Gk. ut
^man- vb. ‘remain’: Av. man-, iterative pres. manaya- (8
mana'uwin- adj. ‘mindful, wilful, hot-tem- pered’: from 
manah- sb. ‘thinking power, power of will’ (Jn. Iran. Re
DNb32. manahà isn. (JNES 4.45; wrongly gen., Hz. ApI 240-2 
méaniya- sb., probably ‘personal property’ in the house
+mamaita, see Atamatta-.
тауйта- sb. ‘doorknob’: Skt. maytikha- ‘peg’, 
mar- vb. ‘die’: Av. mar-, pres. miryeite ($122, $214), S
marika- sb. ‘person of lower rank, subject’, as shown by
Müru- sb. ‘Maru’, a town in Media (ef. König, RulD 71)
M árgava- adj. ‘Margian’: adj. to Margu-, with vriddhi 
Margu- sb. ‘Margiana’, a province of the Persian Empire:
marta- ріс. as ad]. ‘dead’: Av. marata-,-N Pers. murd
```


## [2026-09-07T16:15:27.449Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 224 225 226 227 228; do echo \"-- leaf $i:\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | grep -oE \"(OLD PERSIAN [0-9]+|[0-9]+ OLD PERSIAN|LEXICON [0-9]+|[0-9]+ LEXICON)\" | head -3; done"
}
```


### [2026-09-07T16:15:28.710Z] TOOL RESULT

```
-- leaf 224:
-- leaf 225:
202 OLD PERSIAN
-- leaf 226:
-- leaf 227:
LEXICON 203
-- leaf 228:
```


## [2026-09-07T16:15:36.710Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== mane ===\"; grep -n \"^mane,\" KLN_1966.txt | head -3; echo \"=== mount ===\"; grep -n \"^mount,\" KLN_1966.txt | head -3; echo \"=== mountain ===\"; grep -n \"^mountain,\" KLN_1966.txt | head -3; echo \"=== manor/mansion/permanent/remain ===\"; grep -n \"^mansion,\\|^permanent,\\|^remain,\\|^manor,\" KLN_1966.txt | head -8; echo \"=== paramount/piedmont/amount ===\"; grep -n \"^paramount,\\|^piedmont,\\|^amount,\" KLN_1966.txt | head -6"
}
```


### [2026-09-07T16:15:36.834Z] TOOL RESULT

```
=== mane ===
22780:mane,  n.  —  ME.  mane,  fr.  OE.  manu,  rel.  to  ON. mon,  Dan.,  Swed.  man,  OFris.  mana,  MDu., Du.  manen,  OHG.  mana,  MHG.  mane,  G. Mdhne,  ‘mane’,  OE.  mene,  OHG.  menni,  ‘neck¬ lace’,  and  cogn.  with  OI.  manyd,  ‘nape  of  the neck’,  Gaul.-Gk.  p.otvi<ba)S,  [x<£wo?,  ‘Celtic necklace’,  L.  monile,  ‘necklace’,  OSlav.  monisto, of  s.m.,  OIr.  muin  (for  * moni -),  ‘neck’,  Mir. mong,  ‘mane,  hair’,  W.  mwng,  ‘mane’.  All  these words  prob.  derive  ult.  fr.  I.-E.  base  *men-,  ‘to stand  out,  project’,  whence  L.  eminere,  ‘to  stand out’,  mans,  ‘mountain’.  See  mount,  ‘hill’,  and  cp. minatory.  Cp.  also  moniliform.
=== mount ===
24525:mount,  n.,  hill,  mountain.  —  ME.  mont,  mount, partly  fr.  OE.  munt  (fr.  L.  montem),  partly  fr. OF.  (=  F.)  mont,  ‘hill,  mountain’,  fr.  L.  mon¬ tem,  acc.  of  mons,  ‘mount,  mountain’,  which  is rel.  to  mention,  chin',  munile,  ‘necklace’,  minae, ‘projecting  points  or  pinnacles’  (of  walls); threats’,  e-minere,  ‘to  stand  out,  project;  to  be eminent’,  im-minere,  ‘to  hang  over,  project  over; to  threaten’,  pro-minere,  ‘to  jut  out,  project’,  fr. I.-E.  base  *men-,  ‘to  stand  out,  project’,  whence also  W.  mynydd,  Co.  meneth,  ModBret.  menez, ‘mountain’,  ON.  mcena,  ‘to  tower  above’,  moenir, ‘ridge  of  a  roof’,  and  possibly  also  Avestic mati-  (for  *mnti-),  ‘promontory’,  fra-manyente, ‘they  get  a  head  start’.  Cp.  mount,  v.,  mountain. Cp.  also  adminicle,  amenable,  amount,  commina- tion,  demeanor,  eminent,  imminent,  manada, mane,  marmot,  menace,  mental,  ‘pertaining  to the  chin’,  minatory,  moniliform,  monte,  mont-de- piete,  muromontite,  paramount,  prominent,  pro¬ montory,  rodomontade.
24526:mount,  intr.  v.,  to  go  up,  to  climb;  tr.  v.,  to ascend.  —  ME.  monten,  mounten,  fr.  OF.  (= F.)  monter,  ‘to  go  up,  ascend,  climb,  mount’,  lit. to  go  up  hill’,  fr.  VL.  *montdre,  fr.  L.  mons,  gen. montis.  See  mount,  ‘hill’,  and  cp.  remount,  sur¬ mount,  montage  and  the  first  element  in  mounte¬ bank.
=== mountain ===
=== manor/mansion/permanent/remain ===
22836:manor,  n.,  residence  of  a  nobleman.  ME. maner,  fr.  OF.  (=  F.)  manoir,  ‘manor’,  prop, subst.  use  of  the  infinitive  manoir,  ‘to  dwell’,  fr.
28219:permanent,  adj.  —  ME.,  fr.  MF.  (=  F.)  perma¬
32270:remain,  intr.  v.  —  ME.  remainen,  fr.  OF.  remain- dre,  remanoir,  ‘to  remain’,  fr.  L.  remanere,  ‘to stay  behind,  remain’,  fr.  re-  and  manere,  ‘to  stay, remain’.  See  mansion  and  cp.  words  there  re¬ ferred  to.
32271:remain,  n.  —  ME.,  fr.  MF.  remain,  back  forma¬ tion  fr.  OF.  remaindre,  remanoir,  ‘to  remain’. See  next  word.
=== paramount/piedmont/amount ===
2523:amount,  intr.  v.  —  ME.,  fr.  OF  amonter,  ‘to raise  , fr.  amont ,  ‘upward’,  lit.  ‘up  hill’,  fr.  a,  ‘to  (see 4),  and  mont,  ‘hill,  mountain’.  See  mount  and cp.  paramount,  tantamount.
27312:paramount,  adj.  —  OF.  paramont,  ‘that  which  is at  the  top’,  compounded  of  par,  ‘by’  (fr.  L  .per-), and  amont  (fr.  a  mont),  ‘uphill,  above’.  See  per- and  amount.
```


## [2026-09-07T16:15:45.012Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^mansion\" KLN_1966.txt | head -3; echo \"=== leaf calc ===\"; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [22780,22836,24525,32270,2523,27312]:\n    print(ln, 'leaf', '\\n'.join(lines[:ln]).count('\\f'))\nEOF"
}
```


### [2026-09-07T16:15:46.457Z] TOOL RESULT

```
=== leaf calc ===
22780 leaf 501
22836 leaf 502
24525 leaf 541
32270 leaf 705
2523 leaf 45
27312 leaf 602
```


## [2026-09-07T16:15:55.653Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==502' KLN_1966.txt | grep -nE \"^[0-9]{3,4}|[0-9]{3,4}$\" | head -6; echo \"--- 542 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==542' KLN_1966.txt | grep -nE \"^[0-9]{3,4}|[0-9]{3,4}$\" | head -6"
}
```


### [2026-09-07T16:15:56.874Z] TOOL RESULT

```
6:932
18:933
47:934
--- 542 ---
17:1010
```


## [2026-09-07T16:16:02.291Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==502' KLN_1966.txt | sed -n '40,75p'"
}
```


### [2026-09-07T16:16:03.535Z] TOOL RESULT

```
manifest,  adj.  —  Late  ME.,  fr.  L.  manifestus, ‘clear,  evident’,  orig.  ‘that  which  can  be  seized by  the  hand’,  compounded  of  manus,  ‘hand’, and  -festus,  ‘capable  of  being  seized’,  which  is prob.  cognate  with  OI.  dhdrsati,  ‘dares',  Gk. ttdpcos,  D-pdcoos,  ‘courage,  audacity’,  OE.  ic dearr,  ‘I  dare’.  See  dare  and  words  there  referred to  and  cp.  esp.  infest.
Derivatives :  manifest,  v.  (q.v.),  manifest-ly,  adv., manifest-ness,  n.
manifest,  tr.  and  intr.  v.  —  Late  ME.,  fr.  L.  mani- festdre,  ‘to  show  clearly,  exhibit,  make  public, to  manifest’  (prob.  through  the  medium  of  F. manifester),  fr.  L.  manifestus.  See  manifest,  adj. manifest,  n.  —  MF.  (=  F.)  manifeste,  fr.  manifes¬ ter,  fr.  L.  manifestdre.  See  manifest,  v. manifestant,  n„  one  who  takes  part  in  a  manifes¬ tation.  —  F.,  pres.  part,  of  manifester.  See  mani¬ fest,  v.,  and  -ant.
manifestation,  n.  —  ME.  manifestacion,  fr.  Late L.  manifestatio,  gen.  -dnis,  fr.  L.  manifestatus, pp.  of  manifestdre.  See  manifest,  v.,  and  -ation. Derivative:  manifestation-al,  adj. manifestative,  adj.  —  Formed  with  suff.  -ive  fr.  L. manifestatus,  pp.  of  manifestdre.  See  manifest,  v. Derivative:  manifestative-ly,  adv. manifesto,  n.,  a  public  declaration.  —  It.,  fr.  ma- nifestare,  fr.  L.  manifestdre.  See  manifest,  v.  and adj.
manifold,  adj.  —  ME.  manifatd,  manifold,  fr.  OE. manigfeald.  See  many  and  -fold.
Derivatives:  manifold,  n.  and  tr.  v.,  manifold-ly, adv.,  manifold-ness,  n.
Manihot
934
Manihot,  n.,  a  genus  of  plants  of  the  spurge  fam¬ ily  {hot.)  —  ModL.,  fr.  F.  manihot,  ‘cassava’.
See  manioc.
manikin,  n.,  1)  a  little  man;  a  dwarf;  2)  a  model of  the  human  body;  3)  a  mannequin.  —  Du. manneken,  ‘little  man’,  dimin.  of  man,  ‘man’.
See  man  and  cp.  Manacus,  manakin,  mannequin. Manila,  n.,  cigar;  elemi;  hemp;  nut;  paper.  — From  the  name  of  the  capital  of  the  Philippine Islands.
manilla,  n.,  a  ring,  bracelet.  —  Sp.,  fr.  L.  monilia, pi.  of  monile,  ‘collar,  necklace’  (see  moniliform) ; influenced  in  form  by  Sp.  mano,  ‘hand’, manilla,  also  manille,  n.,  the  second  highest  trump in  ombre  or  quadrille.  —  Dissimilated  fr.  Sp. malilla  (viz.  carta),  dimin.  of  mala,  fem.  of  mala, ‘bad’.  See  male-.
manioc,  n.,  1)  cassava  (a  tropical  plant) ;  2)  starch obtained  from  manioc.  —  F.,  fr.  manihot,  ma- niot,  ‘cassava’,  prob.  directly  borrowed  fr.  Tupi manioch.  Cp.  Sp.  and  Port,  mandioca,  which derive  fr.  Tupi  mandioca,  a  collateral  form  of Tupi  manioch.  Cp.  Manihot. maniple,  n.,  1)  a  company  of  footsoldiers  in  the Roman  army;  2)  in  the  Eucharistic  Church,  a short  scarf  worn  on  the  left  arm.  —  ME.,  fr.  OF. maniple  (F.  manipule ),  ‘a  handful ,  fr.  L.  mani- pulus,  ‘a  handful,  a  small  bundle,  company, maniple',  lit.  ‘that  which  fills  the  hand  ,  fr. mantis,  ‘hand’,  and  the  base  of  pie-re,  ‘to  fill’, ple-mts,  ‘full’.  See  manual,  ad}.,  and  full,  adj.,and cp.  plenum.  The  sense  ‘division  of  an  army’  de¬ veloped  figuratively  and  is  to  be  explained  from the  fact  that  haybundles  variously  bound  served as  standards  for  the  maniples, manipulable,  adj.  —  See  manipulate  and  -able, manipu
```


## [2026-09-07T16:16:09.255Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mansion\" KLN_1966.txt | head -5; echo \"=== manse ===\"; grep -n \"^manse\\b\\|manse,  n\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T16:16:09.321Z] TOOL RESULT

```
6501:caravanserai,  n.,  Eastern  inn,  esp.  for  caravans. —  F.  caravanserai,  fr.  Pers.  karwansarai,  fr. karwan  (see  caravan)  and  sarai,  ‘mansion,  inn’, which  is  prob.  rel.  to  Avestic  {trayeihti,  ‘they protect’,  Ol.  trdyate,  ‘protects’, caravel,  carvel,  n.,  any  of  various  kinds  of  light vessels.  —  F.  earavelle,  fr.  Sp.  carabela,  dimin. formed  fr.  cdrabo,  ‘a  small  vessel’,  fr.  Arab. qdrib,  ‘bark’,  which  is  traceable  to  Gk.  x£px|3o<;, 'horned  beetle;  crayfish;  a  light  ship’.  See  scarab, caraway,  n.,  a  plant  with  aromatic  seeds.  —  ME carawai,  fr.  OSp.  (=  Sp.)  alcaravea  (whence Sp.  carvi),  fr.  Arab,  al-karawiyd’ ,  fr.  a /-,  ‘the’, and  karawiyd',  fr.  L.  carum,  careum,  fr.  Gk. xxpov,  xapcov,  ‘caraway’,  which  is  of  uncertain origin.  Cp.  skirret.
10774:demesne,  n„  i)  possession  (of  land)  as  one’s  own (law)\  2)  an  estate  kept  by  the  owner  for  his own  use.  —  ME.  demein ,  fr.  AF.  demeine,  de¬ mesne  (with  silent  r),  fr.  OF.  demaine,  demeine (whence  also  F.  domaine ,  ‘domain,  estate’),  fr. L.  dominions,  ‘pertaining  to  the  lord’,  fr.  domi- nus,  ‘lord,  master’.  See  domain.  The  s  in  demesne is  prob.  due  to  an  erroneous  association  of  this word  with  OF.  maisniee,  mesnee,  ‘household’, fr.  VL.  *mdnsionata,  fr.  L.  mansio,  gen.  -onis, ‘habitation’  (see  mansion).
20830:kolo,  n.,  a  popular  round  dance  of  the  Slavonic nations.  —  OSlav.  kolo,  ‘circle,  wheel’,  cogn. with  Ol.  cakrah,  Gk.  xuxXo?,  OE.  hweogol, hweol,  ‘wheel’.  See  wheel,  and  cp.  kolach. konak,  n.,  a  large  mansion  or  government  house in  Turkey.  —  Turk,  qonaq,  ‘inn,  mansion,  go- vemmenthouse’.
22837:L.  manere,  ‘to  remain'.  See  mansion  and  cp. words  there  referred  to.
22838:Derivative:  manor-ial,  adj. mansard,  n.,  a  garret.  —  F.  mansarde,  shortened fr.  toit  a  la  mansarde',  named  after  the  French architect  Francois  Mansard  (1598-1666). manse,  n.,  residence  of  a  Scottish  presbyterian minister.  —  ML.  mansus  (also  mansa  and  man- sum),  ‘a  dwelling’,  prop,  masc.,  resp.  fem.  or neut.  pp.  of  L.  manere,  ‘to  remain’,  used  as  a noun.  See  mansion  and  cp.  manor, mansion,  n.,  a  stately  residence.  ME.  mansi- oun,  fr.  OF.  (=  F.)  mansion,  fr.  L.  mansidnem, acc.’  of  mansio,  ‘a  staying,  remaining;  night quarters,  station’  (whence  also  OF.,  F.  maison, ‘house-),  fr.  mansus,  pp.  of  manere,  ‘to  stay,  re¬ main’  (in  VL.,  ‘to  dwell’),  which  is  cogn.  with Gk.  piveiv,  ‘to  remain’,  povf),  ‘a  staying’,  Aves- tic  man-,  Pers.  mandan,  ‘to  remain’,  Arm.  mnam, ‘I  remain,  wait  for',  possibly  also  with  Toch. AB  mask-  ‘to  be’,  fr.  I.-E.  base  *men-,  ‘to  re¬ main,  wait  for’.  Cp.  manor,  manse,  immanent, meinic,  menage,  menial,  meno-,  remaining , permanent,  remain,  remnant, mansuete,  adj.,  tame,  gentle,  mild.  —  ME.,  fr.  L. mdnsuetus,  ‘tamed’,  pp.  of  mdnsuescere,  ‘to tame’,  lit.  ‘to  accustom  to  the  hand’,  fr.  manus, ‘hand’,  and  suescere,  ‘to  accustom,  habituate  . See  manual,  adj.,  and  custom  and  cp.  mastiff. Cp.  also  desuetude.
=== manse ===
22838:Derivative:  manor-ial,  adj. mansard,  n.,  a  garret.  —  F.  mansarde,  shortened fr.  toit  a  la  mansarde',  named  after  the  French architect  Francois  Mansard  (1598-1666). manse,  n.,  residence  of  a  Scottish  presbyterian minister.  —  ML.  mansus  (also  mansa  and  man- sum),  ‘a  dwelling’,  prop,  masc.,  resp.  fem.  or neut.  pp.  of  L.  manere,  ‘to  remain’,  used  as  a noun.  See  mansion  and  cp.  manor, mansion,  n.,  a  stately  residence.  ME.  mansi- oun,  fr.  OF.  (=  F.)  mansion,  fr.  L.  mansidnem, acc.’  of  mansio,  ‘a  staying,  remaining;  night quarters,  station’  (whence  also  OF.,  F.  maison, ‘house-),  fr.  mansus,  pp.  of  manere,  ‘to  stay,  re¬ main’  (in  VL.,  ‘to  dwell’),  which  is  cogn.  with Gk.  piveiv,  ‘to  remain’,  povf),  ‘a  staying’,  Aves- tic  man-,  Pers.  mandan,  ‘to  remain’,  Arm.  mnam, ‘I  remain,  wait  for',  possibly  also  with  Toch. AB  mask-  ‘to  be’,  fr.  I.-E.  base  *men-,  ‘to  re¬ main,  wait  for’.  Cp.  manor,  manse,  immanent, meinic,  menage,  menial,  meno-,  remaining , permanent,  remain,  remnant, mansuete,  adj.,  tame,  gentle,  mild.  —  ME.,  fr.  L. mdnsuetus,  ‘tamed’,  pp.  of  mdnsuescere,  ‘to tame’,  lit.  ‘to  accustom  to  the  hand’,  fr.  manus, ‘hand’,  and  suescere,  ‘to  accustom,  habituate  . See  manual,  adj.,  and  custom  and  cp.  mastiff. Cp.  also  desuetude.
```


## [2026-09-07T16:16:19.873Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==502' KLN_1966.txt | grep -n \"mansion,  n.,  a  stately\\|^93[234]$\\|manor,  n.,\\|mane,  n.\" | head"
}
```


### [2026-09-07T16:16:21.148Z] TOOL RESULT

```
6:932
10:mane,  n.  —  ME.  mane,  fr.  OE.  manu,  rel.  to  ON. mon,  Dan.,  Swed.  man,  OFris.  mana,  MDu., Du.  manen,  OHG.  mana,  MHG.  mane,  G. Mdhne,  ‘mane’,  OE.  mene,  OHG.  menni,  ‘neck¬ lace’,  and  cogn.  with  OI.  manyd,  ‘nape  of  the neck’,  Gaul.-Gk.  p.otvi<ba)S,  [x<£wo?,  ‘Celtic necklace’,  L.  monile,  ‘necklace’,  OSlav.  monisto, of  s.m.,  OIr.  muin  (for  * moni -),  ‘neck’,  Mir. mong,  ‘mane,  hair’,  W.  mwng,  ‘mane’.  All  these words  prob.  derive  ult.  fr.  I.-E.  base  *men-,  ‘to stand  out,  project’,  whence  L.  eminere,  ‘to  stand out’,  mans,  ‘mountain’.  See  mount,  ‘hill’,  and  cp. minatory.  Cp.  also  moniliform.
18:933
47:934
```


## [2026-09-07T16:16:28.690Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ōmēd\\|omed\\|ômed\\|umēd\\|ummed\\|upa.mati\\|upa-mati\\|upamati\\|upa.maiti\" SNS_pages.txt | head -20"
}
```


### [2026-09-07T16:16:28.738Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:16:32.355Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"omed\\|umed\\|amid\\|omid\" SNS_pages.txt | head -20; echo \"--- size ---\"; wc -l SNS_pages.txt SNS.txt; echo \"--- sample leaf 80 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==80' SNS_pages.txt | head -30"
}
```


### [2026-09-07T16:16:33.608Z] TOOL RESULT

```
--- size ---
  16583 SNS_pages.txt
  34173 SNS.txt
  50756 total
--- sample leaf 80 ---
                                      U; a-— Ufc.U»1><
     >   TV                                                                                                             ^bc^b^b             .3
                                                                                                                                                 1,
                                                                                                                                                                  )W



                                                                                                                                     Gl.    76)fra+v^ang: t_
                        . l   iJ U..^>'c> :farr5x/farraxV:
                prwxyh(.^-)>W^-          1870) X v a r,nah- *-
     pi*.                                                                    :
                                                                                              j


                               frox :V (Wan-                      "' 65 •>
                  .,V*U^V:fc>:farraxVbavad:                       **•*>**>
                                                                    .t-t-vti **



                                                                                                      y    •    *>Wj Mr.**, ii, 65) fr ,
              iTW/u j   _^o       :X.Wi«>. 974)fra5sta                           :
                                                                                     b-
                                                                                                                                     Ift-V/VTtf
                                                                                                                                                         y ijrt
                                                                                                                                                      ( P5.
                                                                                                                                                            57)


                                              .YY/T*5            {.Junkev.       30)
```


## [2026-09-07T16:16:45.389Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\"; echo \"=== upa in SNS ===\"; grep -c \"upa\" data/verification/sources/refs/SNS_pages.txt; grep -n \"upa\\.\" data/verification/sources/refs/SNS_pages.txt | head -10"
}
```


### [2026-09-07T16:16:46.714Z] TOOL RESULT

```
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
=== upa in SNS ===
9
```


## [2026-09-07T16:16:49.652Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"upa\" SNS_pages.txt | head -12"
}
```


### [2026-09-07T16:16:49.700Z] TOOL RESULT

```
3761:        xVarsand:^ CMan. Stud. 83)hwnsnd                        :>J* (a-i                         \&mU :man                  *Af JJi|rf fc»j/ upa   + mati ^M^T^fifcff^^                                   ltSl   j
5482:                                     *^ J*<   ***** ***** *"*'               •tiw*J sakisupan:       Jj> tr*-^ ^ pasus.haurva-: t«
10058:         Uen*.176)upSri                  :       l upairi : is- upariy:                            ^
10193: Cupa + a)              upa-^Uc^^ ^var ***•>•«*     1"
10449:                                                                     gryft                     vayaos uparS. ^U.jij l,**.**^ l^l            U ^TL •;»,.»
14951:                                                     upara-ksauma-                     gav- 100/22
14952:                                                     upari 253/21                      giray- 318/20
15078:                                          antarvayu 81/4                upariy 253/21
15322:upairi 253/21             karsyan 212/2
```


## [2026-09-07T16:16:54.272Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:3761])\nprint('leaf0=',pre.count('\\f'))\nEOF\nawk 'BEGIN{RS=\"\\f\"} NR==0' SNS_pages.txt >/dev/null\n"
}
```


### [2026-09-07T16:16:55.540Z] TOOL RESULT

```
leaf0= 53
```


## [2026-09-07T16:16:59.128Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==54' SNS_pages.txt | grep -n \"pdf page\\|upa\" ; echo \"====\"; awk 'BEGIN{RS=\"\\f\"} NR==54' SNS_pages.txt | head -5"
}
```


### [2026-09-07T16:17:00.361Z] TOOL RESULT

```
55:        xVarsand:^ CMan. Stud. 83)hwnsnd                        :>J* (a-i                         \&mU :man                  *Af JJi|rf fc»j/ upa   + mati ^M^T^fifcff^^                                   ltSl   j
====
Yfl
                                bc-,Uub^                                                                                                    c-,L;c-,U ta l; 4 jl                                                      Yf


                                                                                                                   .«uiy       tV/T1 ^ -6-Y/HJ^ -Y*/1o ^ -Y/f ^ -YY/Y ^
```


## [2026-09-07T16:17:06.429Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 tools/ref_page.py SNS:74 --image 2>&1 | head -30"
}
```


### [2026-09-07T16:17:08.568Z] TOOL RESULT

```
no scan of SNS covers printed page 74 (see 'scans' in refs_online.json)
```


## [2026-09-07T16:17:12.780Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && for n in 53 54; do curl -s -o sns_n$n.jpg \"https://archive.org/download/VajnameShayest/page/n$n.jpg\" && ls -la sns_n$n.jpg; done"
}
```


### [2026-09-07T16:17:15.652Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 0 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 0 Sep  7 12:17 sns_n54.jpg
```


## [2026-09-07T16:17:19.239Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && for n in 53 54; do curl -sL -o sns_n$n.jpg \"https://archive.org/download/VajnameShayest/page/n$n_w1600.jpg\"; ls -la sns_n$n.jpg; done; file sns_n53.jpg"
}
```


### [2026-09-07T16:17:23.405Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 35039 Sep  7 12:17 sns_n54.jpg
sns_n53.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1006x754, components 3
```


## [2026-09-07T16:17:29.265Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -s \"https://archive.org/metadata/VajnameShayest\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nfor f in d.get('files',[]):\n    print(f['name'], f.get('format'), f.get('size'))\n\" | head -30"
}
```


### [2026-09-07T16:17:30.886Z] TOOL RESULT

```
ia800605.us.archive.org /10/items/VajnameShayest
VajnameShayest_archive.torrent Archive BitTorrent 7240
VajnameShayest_files.xml Metadata None
VajnameShayest_meta.sqlite Metadata 9216
VajnameShayest_meta.xml Metadata 974
__ia_thumb.jpg Item Tile 4105
vajname shayest.djvu DjVu 3102117
vajname shayest.gif Animated GIF 335999
vajname shayest.pdf Image Container PDF 55078614
vajname shayest_abbyy.gz Abbyy GZ 5125710
vajname shayest_djvu.txt DjVuTXT 325929
vajname shayest_djvu.xml Djvu XML 3165209
vajname shayest_jp2.zip Single Page Processed JP2 ZIP 25800322
vajname shayest_scandata.xml Scandata 72233
vajname shayest_text.pdf Additional Text PDF 12288786
```


## [2026-09-07T16:17:34.837Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -sL -o sns53.png \"https://ia800605.us.archive.org/BookReader/BookReaderImages.php?zip=/10/items/VajnameShayest/vajname%20shayest_jp2.zip&file=vajname%20shayest_jp2/vajname%20shayest_0053.jp2&scale=2&rotate=0\" && file sns53.png && ls -la sns53.png"
}
```


### [2026-09-07T16:17:36.748Z] TOOL RESULT

```
sns53.png: ASCII text
-rw-rw-r-- 1 sfmqrb sfmqrb 49 Sep  7 12:17 sns53.png
```


## [2026-09-07T16:17:41.035Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat sns53.png; echo; curl -sL \"https://api.archivelab.org/books/VajnameShayest/pages\" -o /dev/null -w \"%{http_code}\\n\"; curl -sL -o sns53b.jpg \"https://api.archivelab.org/books/VajnameShayest/pages/53/ocr\" -w \"%{http_code}\\n\" | head -2"
}
```


### [2026-09-07T16:18:06.670Z] TOOL RESULT

```
Error serving request:
  Image error: not found


000
000
```


## [2026-09-07T16:18:11.105Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -sL -o sns_text.pdf \"https://ia800605.us.archive.org/10/items/VajnameShayest/vajname%20shayest_text.pdf\" && ls -la sns_text.pdf && pdfinfo sns_text.pdf | head -5"
}
```


### [2026-09-07T16:18:13.532Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
Title:           Vajname Shayest
Keywords:        http://archive.org/details/VajnameShayest
Author:          tavoosi dr
Creator:         Digitized by the Internet Archive
Producer:        Recoded by LuraDocument PDF v2.53
```


## [2026-09-07T16:18:16.922Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 54 -l 54 -r 300 -png -singlefile sns_text.pdf sns_p54 && ls -la sns_p54.png"
}
```


### [2026-09-07T16:18:21.924Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1021826 Sep  7 12:18 sns_p54.png
```


## [2026-09-07T16:18:24.481Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/sns_p54.png"
}
```


### [2026-09-07T16:18:25.487Z] TOOL RESULT

```

```


## [2026-09-07T16:18:25.484Z] INPUT

[Image: original 4471x3350, displayed at 2000x1499. Multiply coordinates by 2.24 to map to original image.]


## [2026-09-07T16:18:54.400Z] TOOL CALL #44: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/sns_p54.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS/74.png && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS/74.vision.txt <<'EOF'\nSNS (Tavoosi, Vāzhe-nāme-ye Šāyast nē Šāyast, Shiraz Univ. 1365) printed p. 74\n(= pdf page 54 of the archive.org \"vajname shayest_text.pdf\"; running head numeral ۷۴ at top right;\nfacing page ۷۵ is the left half of the same scan leaf, so SNS_pages.txt leaf 53/54 = pp. 74-75).\nRead from the page image by vision (OCR of this book is unusable).\n\nEntry, right column, lines ~17-24:\n\n  <Pahlavi script> ōmēd: امید\n    *ava + √may-  (GNPE. 26)   کردی: umīd, umūd / افغانی: umēd\n    شکل هزوارش آن: <Pahlavi> (Junker, 4.)\n    است. پروفسور کانگا آن را از upa + mati اوستایی و ریشهٔ man: ماندن،\n    صبر کردن میداند  (Kanga. Cit. Han. 46-7.)\n    این واژه در دیگر نوشته‌های پهلوی به شکل <Pahlavi> ēmēd هم آمده است. ک ۱۷/۲۰\n\nTranslation of the Persian: \"ōmēd 'hope'. *ava + √may- (GNPE 26); Kurdish umīd, umūd,\nAfghan umēd; its heterographic (huzvāreš) shape is … (Junker 4). Professor Kanga takes it\nfrom Avestan upa + mati and the root man- 'to remain, to wait' (Kanga, cit. Han. 46-7).\nIn other Pahlavi writings this word also appears in the shape ēmēd. (ŠnŠ 17/20)\"\n\nNeighbouring entries on the same page: hē, hast, hēm, amāh hēm, hēd, hēnd, andar hēnd,\nhād, čē hād, had, -ōmand (\"اومند، مند، پسوند دارندگی است\"; Mir.Man. II 54), -ōmandīh,\nōmēd, hōmdrōn.\nEOF\necho saved"
}
```


### [2026-09-07T16:18:55.679Z] TOOL RESULT

```
saved
```


## [2026-09-07T16:19:00.364Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB umed ===\"; grep -n -i \"um[eē]d\\|ummīd\\|omēd\\|ōmēd\" HUB.txt | head -10; echo \"=== HRN umed ===\"; grep -n -i \"umed\\|umēd\\|ummīd\\|ummēd\\|Hoffnung\" HRN.txt | head -10; echo \"=== NYB ===\"; grep -n \"ummēt\\|ummēd\\|umēt\\|ōmēt\\|hope\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T16:19:00.438Z] TOOL RESULT

```
=== HUB umed ===
3607:schreibung beibehalten. Np. naumed (= afgh. LW.
3609:umU. Vgl. naumed Fird. I, 133, Z. 2.
9243:1) Doppel-w liegt vor in ummed = umed, 6med *Hoflf-
=== HRN umed ===
1372:109. iimed ^Hoffnung, umimd, ömed, vergl. ^utunted.
1376:LW. kurd. umäd, umld; af/. umed; bei. tumned, n.
3902:*) Reimt auf umed (Vis und Rämln, Seite 85 Vers 3 v. u.).
9033:1048. numed 'hoffnungslos'.
9034:phlv. anömet 'hoffnungslos'; vergl. ötwed, umed
9036:Der Bedeutung nach eine Doublette zu na-umed.
10896:umed-T merä jumle pdväz-t ö
=== NYB ===
23:I gladly appoint myself à champion of the rehabilitation of Pazand, too often regarded with diffidence and disdain. It became obsolete on many points and requires a great amount of time-consuming critical research before it can be fully utilized. I sincerely hope that this branch of philology will find a careful and scholarly devotee, who does not shrink from the preliminary critical work. -
364:akómandihà [>k'wmndyh"] in an evil man- ner, pitilessly, mercilessly 75°. Paz. sub- stitutes for it anačmediha ‘hopelessly’. — From akömand ‘belonging to (the world of) Evil’, aka; v. ak-deneh.
925:this passage is & hopeless mess (Bthl. regarded it to be the translation of Av. bàóa which has, however, another sense, v. 8. v. bāstān).
2810:ömet [^wmyt'] hope 66°. 12116, — < Olr *aBi-mati-, abstr. derived from afi + Av. (1121 sqq.) man- (v. ménitan); in
2812:ham-oden < *ham-aßden), whence NP ummēd ; in SW > *aißimati- > *ayißmati- > *ayim(m)ét, whence émét (written 'dmet, cf n. pr. Ēmēt, patr. Ēmētān, q.v., also with secondary aspiration Hémét; Arab ’Imäd) or ah(im)mét > ahmét ['smyt! S, I, 25 + NP amid].
3198:2räd [l’d; inser. and Ps. Pdy] postpos. l. for the sake of, because of, for, on behalf of, in favour of (7220-21), con- cerning (37?. 2919 etc. passim); ham cim ~ for that very reason 512-13, 671-2; han cim ~ 342, & ~ 795. 9626, 982° for that reason; ēt ~ cé because (conj.) 773-5; ce ~ why? 3511. 795; õi ke ~ for whom 183; — preceded by an inf. or a v. n.: in order to, for the purpose of, because: ditan i Zartuxšt ~ (in order) to see Z. 4777, 5218-19; ves avis matārēh i xrat ~ because more wisdom had been allotted to him 9041-12; — forms together with hac or pat a frame preposition: hac bim i Artaxšēr ~ for fear of A. 1525; 3719. 4612-19; hac hin cim ~ 118%; kirpak i pat dat ~ kart for the sake of Law 6419; pat omet +... ~ in hope of 1211917; pat hän cim ~ cé because (conj.) 10421-22, — 2. used as in NP: a) ‘to, for’: cahārpādān ~ ap hamë dat 1419; Papak ~ héc fradand ne būt P. had no child 19; 32-4, 422;  ménam to ~ nevakeh 4771, v.s. v. méni- tan; 427; frazand i zu&s m kar u kirpak bē- dimoxtan 652-23; — b) denoting the dir. obj. of the pres. tense: hakar né han ~ <apdc> dārēt if you do not abjure that (religion) 191; 2520-21; 453; — c) denoting
```


## [2026-09-07T16:19:11.789Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf0=', '\\n'.join(lines[:1372]).count('\\f'))\nEOF\nsed -n '1365,1385p' HRN.txt"
}
```


### [2026-09-07T16:19:13.153Z] TOOL RESULT

```
leaf0= 47
ap. ima- 'dieser; aw. ima-; ai. imd-,
bei. ma[röci 'heute* (226); wa/. gern etc. 'dieser*.
de Goeje's (Bibl. geogr. arab. IV, 175) Erklärung des ar. LW. (?)
äkrän^ akrän (Epitheton aquae pessimae) als wörtl. 'noxam proferens*
ist sehr unsicher.
*) Gesprochen -m6-. mb in Lehnwörtern, z. B. Talmud "^^DN»
arm. amhar (No 111).— 26 —
109. iimed ^Hoffnung, umimd, ömed, vergl. ^utunted.
phlv. nmet bezw. ö)net (auch auf einer Gemme, Hörn,
Mitteilungen, Heft IV, S. 38), ömeivar (vd. 3, 32), vergl.
(inömet,
LW. kurd. umäd, umld; af/. umed; bei. tumned, n.
ömBS (281).
ai. *ava -;- l^may- einsenken*, vergl. methi- ^Pfeiler,
Pfosten (?). Dazu auch bei. s. nük aufgerichtet'
(Bartholomae, ZDMG. 44, 553).
110. enhäz^) 'Genosse, Gemahl, Gemahlin, lumbäz.
Ursprünglich *Spielgenosse*, statt *henwaz? Dann
vergl. np. hä/ten (No. 150).
111. enhästen^) 'anfüllen, anhäufen', Praes. enbär-em,
enhärden, enbär^).
```


## [2026-09-07T16:19:26.690Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%A7%D9%85%DB%8C%D8%AF\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/men-\" ; do echo \"########## $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 333: omid / PIE men- roots' 2>&1 | tail -3; done"
}
```


### [2026-09-07T16:19:28.980Z] TOOL RESULT

```
########## https://en.wiktionary.org/wiki/%D8%A7%D9%85%DB%8C%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/53ccd20c681bd34d.txt
########## https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/men-
/home/sfmqrb/git/rishe/data/verification/sources/web/f249e87bde5d28c8.txt
```


## [2026-09-07T16:19:31.993Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,60p' 53ccd20c681bd34d.txt"
}
```


### [2026-09-07T16:19:32.033Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%A7%D9%85%DB%8C%D8%AF
FETCHED: 2026-09-07T16:19:28Z
STATUS: 200
TITLE: امید - Wiktionary, the free dictionary

امید - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

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
 Gojri 

 Toggle Gojri subsection
```


## [2026-09-07T16:19:35.798Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"etymology\\|Middle Persian\\|Proto-Iranian\\|ummēd\\|abi\\|Hasandust\\|hope\" 53ccd20c681bd34d.txt | sed -n '1,60p'"
}
```


### [2026-09-07T16:19:35.853Z] TOOL RESULT

```
62: Etymology 
82: Etymology 
108: Etymology 
131: Etymology 
222: Etymology
232: hope , optimism , faith , anticipation 
260: Etymology
263: Inherited from Middle Persian [Book Pahlavi needed] ( ʾwmyt' /⁠ummēd⁠/ , “ hope ” ) , [ 1 ] from Proto-Iranian *hamwátiš .
287: umēd, ummēd
291: umēd, ummēd, umayd
304: امید • ( umēd, ummēd / omid, ommid ) ( plural امیدها ( umēd-hā, ummēd-hā / omid-hâ, ommid-hâ ) , Tajik spelling умед , or уммед ) 
306: hope 
429: → Punjabi: 
443: Arabic script: اُميدَ ( umed, ummīd, ummed ) 
466: امید • ( umēd  / omid or ummēd  / ommid ) ( Tajik spelling Умед or Уммед ) 
468: a male given name , Omid , Umed , Umid , and Ummed , from Middle Persian 
473: ^ MacKenzie, D. N. ( 1971 ), “ummēd”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 84 
478: Etymology
481: Borrowed from Classical Persian امید ( umēd, umīd, ummēd, ummīd ) .
495: hope 
518: Qureshi, Bashir Ahmad ( 1971 ), “ اميد ”, in Kitabistan's 20th Century Standard Dictionary , Lahore: Kitabistan Pub. Co., page 75 
525: Etymology
535: hope 
543: Gojri terms derived from Middle Persian 
544: Gojri terms derived from Proto-Iranian 
551: Persian terms derived from Middle Persian 
552: Persian terms inherited from Middle Persian 
555: Persian terms inherited from Proto-Iranian 
556: Persian terms derived from Proto-Iranian 
565: Persian male given names from Middle Persian 
568: Urdu terms derived from Middle Persian 
569: Urdu terms derived from Proto-Iranian 
598: Requests for Book Pahlavi script for Middle Persian terms
```


## [2026-09-07T16:19:42.134Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hamw%C3%A1ti%C5%A1\" --note 'page 333: Proto-Iranian *hamwátiš, source of MP ummēd / NP omid' 2>&1 | tail -2"
}
```


### [2026-09-07T16:19:44.335Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/80c4c9fc4a26e86f.txt
```


## [2026-09-07T16:19:48.254Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/^ *Etymology/,/^ *Descendants/p' 80c4c9fc4a26e86f.txt | head -50; echo \"====\"; grep -n -i \"hamwat\\|ham-\\|Cheung\\|Hasandust\\|*wat\\|reconstruct\" 80c4c9fc4a26e86f.txt | head -20"
}
```


### [2026-09-07T16:19:49.579Z] TOOL RESULT

```
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Inflection 

 1.2.2 
 Related terms 

 1.2.3 
 Descendants 
 Etymology
 [ edit ] 

 From *hamwátati ( “ to hope for, believe ” ) +‎ *-iš .

 Noun
 [ edit ] 

 *hamwátiš 

 hope , belief , faith 

 Inflection
 [ edit ] 

 masculine/feminine i-stem

 singular

 dual

 plural

 nominative

 *hamwátiš

 *hamwátiH

 *hamwátayah

 vocative

 *hamwátay

 *hamwátiH

====
ugrep: error: error at position 38
(?mi)hamwat\|ham-\|Cheung\|Hasandust\|*wat\|reconstruct
             empty (sub)expression___/
```


## [2026-09-07T16:20:03.534Z] TOOL CALL #52: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hamw%C3%A1tati\" --note 'page 333: PIr *hamwátati, verb behind MP ummēd' 2>&1 | tail -2"
}
```


### [2026-09-07T16:20:06.811Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c0e513f1737319a1.txt
```


## [2026-09-07T16:20:10.246Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/Etymology$/,/^ *Verb/' c0e513f1737319a1.txt | head -30; echo \"=== refs ===\"; grep -n -i \"Cheung\\|Rastorgueva\\|Hasandust\\|reference\" c0e513f1737319a1.txt | head"
}
```


### [2026-09-07T16:20:11.585Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 From *ham- +‎ *wátati ( “ to be familiar with ” ) , from Proto-Indo-Iranian *wátati . [ 1 ] [ 2 ] 

 Verb
=== refs ===
77: References 
455: References
458: ↑ 1.0 1.1 Cheung, Johnny ( 2007 ), “ *u̯at ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , pages 428-429
```


## [2026-09-07T16:20:16.576Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ummēd\\|ummed\\|umēd\\|ōmēd\\|omed\" CHEUNG.txt | head -10; echo \"=== uat entry ===\"; grep -n \"^\\*u̯at\\|u̯at\\b\" CHEUNG.txt | head -10"
}
```


### [2026-09-07T16:20:16.639Z] TOOL RESULT

```
3464:*NWIR: Gur. čāšīáīn/-čāšy- ‘to be accustomed to, adept at’ 
11598:‘to get accustomed to’. 
14584:used, accustomed to, to contract an (annoying) habit’, Wa. yaxk (ppp.) ‘learned? || (+ 
14585:*us- ?) Yzgh. Soxs-/Soxt ‘to get accustomed to, get spoiled, learn? 
14587:*SANSKRIT: oc ‘to be accustomed, get used to, be(come) at ease with’ (RV) 
14601:accustomed to’, OCS učiti ‘to learn’, Lith. junkti ‘to become accustomed to’, Goth. 
14604:bi-uhts (ppp.) ‘accustomed’ 
17878:(cf. Skt. oc ‘to be accustomed, to get used to’), comparable to *iaué, which has been 
21241:‘to be necessary’ || (+ *abi-) BSogd. ’Bs’xs- ‘to be trained, accustomed, tamed’, 
30171:*CHORESMIAN: m/n’s- ‘to become acquainted, accustomed’, (caus.) m/n’sy- ‘to 
=== uat entry ===
```


## [2026-09-07T16:20:20.570Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"umm[eē]\\|Hoffnung\\|'hope'\\|“hope\\|hope’\" CHEUNG.txt | head -15; echo \"=== search vat ===\"; grep -n \"vat.*to be familiar\\|familiar with\" CHEUNG.txt | head -10"
}
```


### [2026-09-07T16:20:20.636Z] TOOL RESULT

```
2117:(+ *ш-) ? Oss. D. ivaerzun/ivarzt ‘to promise; to give hope’ (< *‘to cushion someone 
24734:become warm’, Pash. döbay, (Wan.) doba ‘summer’, Yi. idou, Wa. andáv ‘fever’ 
27286:‘wish’, bavar, bawar (m.), (Sor.) bawar, birwa ‘belief; hope’ (Pers. LW ?) || (+ *uz-) 
27656:*NWIR: (+ *pati-) NP payüsidan ‘to expect, hope’ 
=== search vat ===
21259:vile’ || (+ *ui-) m/wsxs- ‘to separate’ || (+ *ham-) m/sxs- ‘to be united, familiar with
```


## [2026-09-07T16:20:27.751Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ham-uat\\|ham-vat\\|hamvat\\|\\*uat\\|\\* uat\\|humat\\|ummēt\" CHEUNG.txt | head -10; echo \"=== try 'wat' headword lines ===\"; grep -nE \"^\\*?[uv]̯?at[ -]\" CHEUNG.txt | head -10; echo \"=== 'to know, understand' entries near end ===\"; grep -n \"OLD INDIAN: vātayati\\|vātay\\|Skt. vātay\" CHEUNG.txt | head"
}
```


### [2026-09-07T16:20:27.825Z] TOOL RESULT

```
27627:*uat 427 
27669:*uat ‘to inspire, be informed, acquainted’ 
55324:*grabH (s.v.), *uat, *zanH? 
=== try 'wat' headword lines ===
27627:*uat 427 
27669:*uat ‘to inspire, be informed, acquainted’ 
33892:vat-, 427 
=== 'to know, understand' entries near end ===
```


## [2026-09-07T16:20:30.449Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27669,27730p' CHEUNG.txt"
}
```


### [2026-09-07T16:20:30.493Z] TOOL RESULT

```
*uat ‘to inspire, be informed, acquainted’ 

*AVESTAN: vat- ‘to inspire ?, be informed, acquainted’ || (+ *api-) ‘to be acquainted 
with’ || (+ *fra-) ‘to show to’ — Liste: 49 

Pres. them.: IND. med. 2sg. YAv. apiuuatahe (Y 9.25), SUBJ. med. 3sg. YAv. apiuuataite (V 9.2, V 9.47, 
V 9.52); Aor. them. red.: SUBJ. 3sg. YAv. api “vaotat (Yt 9.26); Caus.: IND. 1р1. OAv. fra vatoiiamahr 
(Y 35.7), IMPV. Zeg, OAV. frä vätöiiö.tü (Y 35.7) 

*PARTHIAN: (+ *fra-) frwd- ‘to be informed; to know, understand’ || (+ *ui-) wywd- 
‘to distinguish, separate’ || (+ *ham-) hmwd- ‘to believe’ = Ghilain: 53, 96 | 
DMMPP: 157b, 360a, 179a f., 41а 

(+ * fra-) Pres.: IND. 35р. “frwdyd, SUBJ. 2sg. frwd’h; Partic.: perf. pass. frwd’d || (+ *ui-) Pres.: PRES. 
35р. wywdyd, 3р1. wywdynd, SUBJ. 2sg. wywd’h; Partic.: perf. pass. П wywd'd; Inf.: wywd’’d, wywd'd 
|| (+ *ham-) Pres.: IND. 159. hmwd’m, 3sg. hmwdyd, lpl."hmwd'm, 3р1. hmwdynd, SUBJ. 1р1. hmwd’m; 
Partic.: perf. pass. "mwst 

*KHOTANESE: (+ *fra-) OKh. hot- (hvi-) ‘to be able’ 2 SGS: 155 

*SOGDIAN: (+ *ham-) CSogd. ’wt- ‘to hope for’, SSogd. "nwth (Sims-Williams), 
CSogd. "wt ‘hope, faith’ 

Pres.: IMPV. 2sg. CSogd. "wt 


428 *uaxš 


*NEIR: (+ *4-) Pash. (Afr.) awla ‘wish, desire’, ? Oss. I. ud, D. od ‘ghost, soul, spirit’ 
*MISC: (+ *fra- or *ham- ?) Arm. (LW) hawat ‘belief’ 

*SANSKRIT: vat ‘to appropriate spiritually’ (RV+) = EWAia П: 494 

«PIE *uet- ‘to be informed, acquainted’ — LIV: 694 | Pok.: 346 

*IE COGNATES: Olrish fethid ‘notices, expects’ 


*REFERENCES: DKS: 498a f.; Sims-Williams 1985: 96 ad 26; Abaev, Slovar’ IV: 6 f.; Werba 1997: 232; 
Cheung 2002: 233; NEVP: 12 


*uaxš ‘to grow; increase’ 

*AVESTAN: vaxs- ‘to grow’ || (+ *abi-) ‘to let grow, spoke (the fire)’ || (+ *uz-) ‘to 
grow up(wards)’ || (+ *fra-) ‘to grow forth’ = Liste: 48 

Pres. them. ja-: IND. 3sg. OAv. uxsileiti (Y 44.3), YAv. uxsüeiti (Y 10.6, Yt 7.2, Yt 8.43, etc.), ҮАУ. 
uzuxsiieiti (Yt 6.2 f., Yt 7.4, Ny 1.12, etc.), 3pl. YAv. uzuxsiüieinti (Yt 13.10, Yt 13.14), INJ. 2sg. OAv. 
uxsiio (Y 31.7), 3pl. YAv. uxsin (Yt 13.93, Yt 17.18), SUBJ. 3pl. YAv. fra uxsiian (V 5.12 f., V 8.9 £); 
Fut.: med. 3pl. ? YAv. vaxsiiente (Yt 8.42); Aor. athem.: INJ. 3sg. vaxst (Y 34.11, Vr 12.4), SUBJ. 3sg. 
OAv. vaxsat (Y 31.6, Y 48.1, Y 48.6), med. 3pl. OAv. vaxsonte (Y 32.4), OPT. med. 1sg. OAv. uxsiia (Y 
33.10); Partic.: pres. YAv. uzuxSiiant- (V 18.63), med. YAv. uzuxsiiamna- (Yt 4.8); Caus.: IND. 3du. 
Y Av. vaxsaiiato (Y 10.3), SUBJ. 3sg. ҮАУ. aißi.uuaxsaiiät (N 73), ОРТ. 35р. Y Av. aifi.vaxsaiioit (N 81). 
© Kellens – Рігаг 1991: 106 interpret OAv. uxsiia differently: pres. IND. 1sg. 

*MIDDLE PERSIAN: BMP whs- /waxs-/ ‘to grow; to blaze’, BMP whsyn- /waxsen-/ 
(caus.) “to light a fire’ || (+ *fra-) ? MMP frwxs- ‘to sell’. 0 The verb ВМР whs- is 
always used in connection with "twr/'dwr ‘fire’. Several semantic shifts need to be 
assumed for MMP frwxs-, not all of which are evident: **to grow’ > *‘to prosper’ > 
*'to prosper through trade’ > *‘to sell’. = DMMPP: 158a
```


## [2026-09-07T16:20:43.638Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for n in 32 33 34; do echo \"===== pdf $n =====\"; awk -v k=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==k' BQT_v4_pages.txt | head -40; done"
}
```


### [2026-09-07T16:20:44.887Z] TOOL RESULT

```
===== pdf 32 =====
[pdf page 33]
ماعلق -۹-
و یازه(۱) طم خدای عزوجل است ۱ - وبمعتی | چیزی شدن باشد بعنی شبه ومانند ونظیرشدن -
شبه و نظیر و مثل و مانند هم آمده است ۴ مانطس ‎٩‏ - با نون وطای حطی‌وسین
ویستی‌هماا - وکوبی وینداری ۴ نیز کفته‌اند. معقص وحرکت لامعلوم . حجری است هندی
مافاف ؟ - بروزن آلاف . ماماچه را | پمتی‌سنکی است که درهندوستان میباشد. کویند
کویندو جرمی قابله خوانند - و بمعنی ناف‌هم باطل‌السحر است, هر که باخود دارد سحر پروی
آمده است وآ نکوی باشد در شکم.#* کار تکند و از جمیع امراض محفوظ باشد.
هافستی * « بر وزن داستن . بصفت مانب ۷ - بنکون نون وکاف فارسی,

() چك : ژند وپاژند .

۱ - در فرهتگه دسانیر (ص ۲۹۵ ) پس از نقل قول برهان کوبد : « باید داننت که
مونا بالواو خدا را کوبند > هزوارش 51۵2. 1712۵02 بهلوی ۷۷۵1808 (خدا) رك : بونکر.
قرهتکه چهلويك س2۸ ضل۱ سور : ص۱۱۳ :۱ . جهانگیری نیز بنقل از * ژند » این کلمه
را بممتی خدا آورده . ۴ - صفت معبهه از « ماندن > بمعنی مانند بودن :
قرو ستبی دل دشمن بدا ن كلك شهابآبین بدرانی صف لشکر بدان تیغ فلك مانا -

۴ رد : ح٩‏ صفحهٌ قبل - ازرقی هروی « رشیدی > «فرهنگه تظلم».

۴ - مخفف « مام ناف » همین معنی « رشیدی > + - از : مان ( ماندن )
[ر3 : مایدن] ۳-ستن ( پوند مصدری ) جزء اول ازربِعهٌ - 138 ( آندبشیدن » تصورکردن)»
قی : اوستا 2102 2۳6 13282768 (مانند » نظیر) . نولد که «مانتن» را از ربشةٌ -۰332
ساسکریت -32288 (عکس, تصویر » ظهور, شباهت) میداند * اسشق ۹۹۷ > هوبشمان مانستن‌را
با تواستن قیل ی کرده » کوید : بنابراین مانستن (شبیه بودن) همچنانکه نول دک ه گفته ممکشست
از08339 (مانتد » شبیه) هشتق باشد » و قس : دانتن ۸ هوبشمان ۹۹۷ .

‎٩‏ - در تحقةٌ حکیم موّمن و فهرست مخزن الادوبه و ذبل قوامیس دزی تیست » شاید
مس « مالیشطم *رك : دزی ج ۷ص 090 . ۷ - از اوستا 332۷۷880 ( رلد: هاء)
این‌کلمه دریسنی‌لهجه های ابرانی بافی‌مانده : کردی 13288 ۰ 13288 ۰ 332388 :10317288
( مله ),* ژایا ص ۳۸۸ ۰ درطبری نیز 33288 :

‏مه آش پرستی ته دیم ور قدیمه بهاره ۰ بهشته, مهر ومانگه» ته دیمه.
( آتش پرستی من در پیش روی توعادت قدیم است . بهار است » بهشت. است » خورشید و ماه
است . نه رویت ) «رضاقلی هدایت . انجمن‌آرا : دیم .> در فارسی هم‌آمده است :

‏بگرمی بدیشان یکی بان زد کزآن باتک تب لرزه بر مانگه زد .

‏عنصری بلخی « انجمن‌آرا » .
و« مانگه دیم » ( ماه صورت ) در اعلام کسان آمده .
===== pdf 33 =====
[pdf page 34]
۱۹۱۱۳ مانه

بمعنی ماء باشد که قمر است - و بمعنی آفتاب مانو سار - بامین بی نقله بر وزن

هم ابنظرآمده است و بمعنی اول اسح است. آلوزار » نام یکی از کشنده ها و قاتلان داراب
مانمی ۱ « بنکون ثالك و کر میم این دارات است که او را فریب داد و قصد حیات

ونون ساکن‌درآخر » بلغت زند وپازند (۱) جامی اوکرد ۴ -

باشد که بدان (؟) شراب و آب و امثال آن مانوش - بروزن خاموش . نام کوعی

خورند .3۳ است که منوچپر در آن کوه متولد شد و آنرا
مانند7 باد ۴ - اعاره بنالم‌برزعاست | مانوشان هم میکویند * .

و آن عالمی باشد میان ملك و لکوت . مانوك ۱ - بائاك بواوکشیده وبکاف
مالورگ - با ثاك بواو کنشیده ورای | زده » مرغی است کهآنر! بفارسی‌چکاوك میگویند

بی نقطةٌ مفتوح بکاف زده » بمعنی چکاوك است |[ وبعربی ابوالملیج خوانند ؛ و بسن ی کوبند مرغی

وآن پرنده‌ای باشد که‌یعربی ابوالملیج خواشش | است‌آب ی که سرخا ب کوبندش .

سی کوبند پرنده ایست آب ی که آنرا سرخاب مافه ۷ « بر وزن خانه , بسمتی اسباب

میگوبند ۴ - و لام دارویی هم‌هست ؛ و بمعنی | و ضروربات خانه و منزل باشد - و مهمل خاته

اول جحذف رای قرشت هم آمده است. هم هست. .

(۱) چك : ژند وپاژند . (۲) چش : درآن .

۱ - پپلوی « جام » ۷22 وهزوارش آن 1218/0 7 1۳222 است « نیب رکه ص۲۶۸.

و این هزوارش را پیشتر مانمن میضواندند . رك : پوتکر صس ۱۱۹ ؛ بوستی . بندهش آص ۲۲۹ :
زان ان و ۴ -ظ . برساخته فرقة آذرکیوان .

۴ - درافرهنکه رشیدی « مانو رکه > بمعنی * مرغابی تیز پ رکه سرخاب نی زکوبند >
و در جهانگیری بمعنی « چکاو » آمده و هيچيك شاهد ندارند . رك4 : مانوك .

۴ - مصحف « جاتوسار » (.م.) ۳ جانوسیار . 8 - چنین نامی در شاهنامه و
فهرست ولف نیامده ‏ ولی دربندهش مانوش ( منوش ) هم بکوهی اطلاق شده که منوچهر درآن
===== pdf 34 =====
[pdf page 35]
مالی -۱۹۱۲-
مافی « بروزن دانی بممتی نادر باشد | و جد از عیسی علیه السلام ظاهر شد و دعوای
که از سرت است که بی همتا و بیمثل وابکه | ییغمبری کرد » وبهرام شاه بن هرموز شاء او را
وتنها باشد ‎٩‏ - و نام نقاشی بوده مشهور درزمان بقتل آورد ۲ .
اردشیر و بعضی کوبند در زمان بهرام شام بود افیف « بر وزن جاوید » بمنی گذاشت
۱ - ققه‌اللقةٌ عامیانه . در پهلوی 13211 ( از : مان (خانه) + يك [سبت پهلوی] )
بمعنی منضوب بغانه , مربوط بغانه ؛ در اوستا 8838838 * پاروجا مس ۰۳۱۲
۲ - 31801 . بونانی ۸1465 ( اضانی 81488105 » نیز 8]2868105 ) «یوستی.
نام نامه ص۱۹۰ :
۱ مانی از نجپای ار نت رس
ایران ود وبنایر ‏ 1 و و یه دوه
روایات مادرتش از | و هه ص ی
خاندان خاهان 3 پا 9 رو سیر ین ها
آشکانی بوده‌است. 3 دی 11 پا ۷ 2
پدر ماتی فاتك 4 :! 1 ۸ را
و02۳ با 9 0 (< کنر 7 7 پر
رم مدا ۳7 امه 1
وی لا و اک .ی
رم سا با اه گرا
ود که با رگ زر وه و لا
مهاجرت کرد ودر ار ۳۱ ملس ‎٩‏ ام ۹
قربه‌ای درم رکز پا :۱ : 7
ولایت 38/16594656 ی ! 9 2 زب 4
مکن کزید و با 1 4 1 0 2
فرقةٌ منشله که سم و کر
است . و در آن ۱ :4 0 دنم
زمان درنواحی‌یین ود نت 1 ۵
فران‌ودجلسا کن اوه بیج ۹
موی ۰ 93 ور وا با
منت هگا اه
۷ متولد شد بخ ۹ ۳ 4
ود رکو دکی‌آیین
منتله گرفته ولی مینیاتور مانوی ( لو کوك , خوتشو )
بسد . چون ازادیان زمان خود مانند زرتشتی ومیحی‌وآبینهای گنوستی‌مخصوصاً لك ابن دسان
ومرقیون‌مطلم گشت, هنکر مذهب مفتله کردید . مانی‌چند بارمکاشفاتی یافت و فرشته‌ای اسرار
جهانر! بدو عرضه کرد . پس بدعوت پرداخت وخود را «فارقلیط» که مسیح غظهوراورا خبرداده بود
بقیه در مفحةٌ ۱۹۵۳
```


## [2026-09-07T16:21:15.827Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for n in 30 31; do echo \"===== block $((n+1)) =====\"; awk -v k=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==k' BQT_v4_pages.txt | head -45; done"
}
```


### [2026-09-07T16:21:17.162Z] TOOL RESULT

```
===== block 31 =====
[pdf page 31]
مالیطرنا م۱۹۶۸
کوبند بوتانی ات .38 خوانند, وصعترا کرچه باسین بی‌نقطه است لیکن
مالیطر فا ۱ « بفتح طای حطی‌وسکون | درکتب طبی بصاد نوشته‌اند تا بشمین مشتبه‌نشود.
رای قرشت و لون بالف کشیده . و پلفت بونانی | خوردن‌آن درطمام ضمف‌چشم را نافع باشد وقوت
زاج سیاه باشد و آن را زاج کفشگران اس باصره را نگاه دارد -
میگوشد؛ وبحذف مانی‌هم آمده است که ملیطرنا مامهستان « بفتح ثالك ‏ و کسرهایروزن
باشد. + ناوکستان . دوائی است که آنرا ساذج هندی
ها » بروزن لام » مادرراگوبند وبمرپی | کوبند و آن برکی است مانند بر که کردکان
والده و ام خوانند ۲ .28 و در روی آب پیدا میشود . بخورآن بجه را از
مامك * بروزن ناوك . مصفر هام است نگ بزیرآورد(؟) -
که مادر باشد پستی ماد رک - و مادر را هم مامیشا ؟ - با ناك بتتای‌رسید. دای
میگوبند ۴۳ .#* متلئه بالف کشیده , بلفت سربانی نام رستنیی‌باشد
مامون « بروزن (۱) هامون . نوعی‌از بفایت بیمزه ودرآب بهم میرسد ودر قاضات بکار
پودنه کوهی باشد و آلرا بس‌بی صعتر الجمام | برند و عصارة آنرا شیاف مامینا خوانند .
() چك : بوزن . () چش : آرد . ۹
۱ - بونانی 33612818712 ‎٩‏ اشتینگای > . ؟ -قی : ماما ۰ مامی » لیتوانی
8 30۵ (مادر) . املاوی کلیسیابی 38778 ( ماما ) » آلبانی 136116 » وخی
.۰ سربکلی 33282 (مادر بز رکه) . افغانی 12181 (عمه » خاله) ۰ بونانی114772302 ۰
6 ( ماما » مادربز رکه ) . لاتینی 33870382 » 17121212118 ( ماما + مادربز رکه ) ۰
آلمانی عالی قدیم 30002 . 3301 ( عمه . خاله ) «اسشق ۹۹۳ > ۰ پازند 133878(مادر)
* باروچا ۰۳۱۱
شاد الا بدر مر که نه‌یینی مردم بکر جز در رحم مام نیابی دختر.
انوری ابیوردی درقصیدء راجع بحملهٌ غزان . « فرهنگه نظام » -
۴ - از : هام (هم.) + که ( پوند تحبیب و تصفیر ) .
۴ - ممیتا « دزی ج ۲ اس چ۹۱ ۰ 80818106۳ (ف) ۸« دزی جس ۲:۵0
0 مالیدن - بفتح دال » اوستا - 33872 » 1287628111 ( جاروب شده ) » پهلوی
2 ] ۸۵۵ ۰ 2۳2 ] فقاطعهل .۰ متفه ] هط۵5ل , ۵ط22720(9 ( جماع ) ۰
(جناع کردن). 2211088 ۰ 332[)1(808 ؛ هندی باستان- 2:۲2 , [ع12279180
( پاك کردن ) »کردی 2 3.3110 ( جارو ب کردن ) بلوچی 2 و2212 . 22160285
( ساییدن ‏ مالیدن , مخلوط کردن ) » استی 323۳218 ( جاروب کردن ) « اسشق ۹۹۲ 4
دست کشیدن روی چیزی ۰ چبزی را دردست مکرر فغار دادن » دوچیز را بهم فشاردادن » مشت
ومال دادن » چیزی را ( مانند رنگه , روغن ) روی جم ی کشیدن .
2 ماما.- رك : مام ؛ در تهرانی 3387528 (قابله . مام‌ناف) » در افغانی 112132 (دائی,
خال ) در فارسی آدیی بمعتی مادر است :
هت مامات اسب و باپا خر تو مشواتر چو خوانمت استن . سنائی غزنوی .
و رل :کنجینة کنجوی ص ۱۳۹ ۰
۵ مام لاف - قابله « رشیدی > و مخقف آن ماناف (ه.م.)

===== block 32 =====
[pdf page 32]
-۱۹4۹- مانا
مامیرآن ۱ - با رای بی نقطه پروزن ِ که عربان بیت خوانند ۴ - واسباب وضروریات
غازبخان » نوعی از عروق‌السفر است وآن دوائی | خانه را نیز کوبند - و بمعنی ما باش د که متکلم
باشد زرد رنکه بسپزی مابل » باريك و کره‌رار | مح‌الغیر است ۴ - و بمعتی مارا هم هست که در
میشود . گرم و خغك است در چهارم . برقانرا مقابل شما را باشد ۴ - و امربرگذاشتن ومالدن
نافع است و آنرا بعربی بقلةالخطاطیف و شجرة | هم هست بعنی بگذار و باش و بمان ۴ - و شبه
الخطاطیف خوانند . کوبند چون +جچةٌ پرستوك در و مثل و مانند را نیز کوبند 9 - و بممنی باقی
آشیان نابینا شود مادر وی غاخی از مامبران | و ابد و جاویدان هم کفته اند - و بلفت هندی
آورده درآشیانه نهد چشم بچه‌اش بینا کردد . | بمعنی حرمت وعزت وقبول ومقبول باشد -
۱ ید هافا٩‏ - بر وزن دانا . بزبان زند
۱ ۳ میرمیران « دزی ج؟ ص۹۲۸ * مرمیران « دزی ج ۲ ص۵۸۵ ۰۹ لغت فارمی
است . فرهنگه نوبسان‌آنرا با 3611608108 (خالیدولیون [ه.م.] ) بونانیان مترادف داسته‌اند
و اسم عربی « بقلة الخطاطیف > ترجمهٌ این کلم بودانی - بعنی « گیاه پرستوها » - است -
«ناه) - 11602۵1۵ کنته‌اند که محتملا 61140186-) (فر) راکه دارای عصاره وريشهٌ زرد
رنگه است » با داروی شرقی دیگر ی که آنم دارای ریشه های زرد رنگه است بعنی عنام۲۰
8 خلط کرده‌اند . اصل گیاه اخیر از چین است وریشه های آنرا بابران وهند میبردند ودر
مغزن‌الادویه شرح آن‌آمده . مایرهوف همین قول را معتبرمیداند « عقار ۷۸۱ اف >. ور4: دزی
چص ۵۹۵ ۴ - پپلوی 28 ( خانه » مکن ) « یب رکه ص۱۶۶ * » پارسی باستان
- 328812 ( خانه » سرای ) » در پهلوی بجای - 373288 اوستایی‌کامهٌ 7320 ( خانه ) را
بکار برده اند , 28)1(9878 ۰ 28)1(501 ( منزل ) , 340028 ۰3200:9120
منز لکردن ) »و « ماندن » فارسی نیز ازهمین ربقه است . «اسشق ۹۹4*.
۴ - ضمیراول شخص‌جمع مفعولی: دادمان » گفتمان ؛ وضمیر اضافی (ملکی): کتابمان ۰
کلاهمان . درپهلوی 3328 « نیب رکه ص ۱4۵ . ۴ -ر4 : ماندن .
8 - مان صورت پسوند بمعانی‌ذیل بکاررود: الف) - مان ۳ - من ۰ ازاوستابی 1387225
بهئوی 3281128 ( اندبشیدن ) : شادمان » پشیمان: » پژمان » نربمان , رادمان » قهرمان .
دشمن « فاب ‎٩‏ ص ۰۷۳ ب )مان ( از ريشة 46۳888 (کانتها ) و 8673288 ( دیگر
بخشهای اوستا ۰ پپلوی 1328 بمعمتی خانه ) : کشتمان . دودمان » کرزمان ۶ فاب ۱ ص۷۳ح >
ج ) پسوند سازندة اسم معتی از ربشهٌ قعل : سازمان » زایمان . د): پوند سازندة آسم ذات از
مصدر مرخم : ساختمان . علاوه بر اینها پسوند مان ( از مصدر مانستن ) را ذ کر کرده اند و
« شیرمان > و «آسمان مان » ( رك : فرهنکه نظام ) را شاهدآورده‌اند » ولی استعمال آین‌کلمات
محتاج بأیید شواهد است . - پهلوی ۳32881 (مانند » نظیر ) * ناوادیا ۰۴۱۹۲
در فارسی تصورت ادات تشبیه وشغك و تردید و بممنی گوبی » پنداری ومانند آید :
آنکی که مرا یکشت باز آمد پیش ماناکه دلش بسوخت برکشتهٌ خویش .
« گلتان ۰۱۳۰
```


## [2026-09-07T16:21:41.059Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"ماندن\" BQT_v4_pages.txt | head -20"
}
```


### [2026-09-07T16:21:41.105Z] TOOL RESULT

```
1158:منز لکردن ) »و « ماندن » فارسی نیز ازهمین ربقه است . «اسشق ۹۹4*.
1160:کلاهمان . درپهلوی 3328 « نیب رکه ص ۱4۵ . ۴ -ر4 : ماندن .
1187:را بممتی خدا آورده . ۴ - صفت معبهه از « ماندن > بمعنی مانند بودن :
1192:۴ - مخفف « مام ناف » همین معنی « رشیدی > + - از : مان ( ماندن )
1216:مقل2ق . ارمنی 338222 ( ماندن » انتظار کشیدن , خدمت کردن ) » لانینی ۰32886۵
1217:بودانی 33628 ۶ کردی 73218 ( ماندن ) » بلوجچی 33882810 ۰ 333812 ( خته شدن )
1270:5 مالند - بفتح سوم . از مصدر «مانتن» و « ماندن > ۰ و آن ادا نشبیه است (رك :
1422:۹ -,ماضی « مانیدن »* ماندن . ۲ - «مانید , چون جرم امت . چون کاری
5340:موزه در گل‌ماندن » کدبه از موسیقار ۴ - با قان بروزن بوتیمار:
5475:کلیسا نوازند ۱ ؛ وبعی دیگر کوبند مولوزنکی - و دیر ماندن و درتگه کردن و تأخیر نمودن
9199:رفتن باشد - وکنایه از درماندن ودرمانده شدن | شود .
11340:و زیبایی وصف میکرده‌اند » سپس بواسطةٌ وبران شدن‌آن قسور بدست پمقوب وتماندن نام ولشالی
12457:را نی ز کوبند - ومدت ماندنآفتاب دربرج‌حمل- | وفتح فوقاتی» بمعنی پیت باد دکه‌عر بان‌بافیش(۱)
20914:پارید پنکس بر ایرانیان بماندند حیران همه در میان
```


## [2026-09-07T16:21:47.414Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [1216,1270]:\n    print(ln,'block(1based)=', '\\n'.join(lines[:ln]).count('\\f')+1)\nEOF"
}
```


### [2026-09-07T16:21:48.726Z] TOOL RESULT

```
1216 block(1based)= 33
1270 block(1based)= 34
```


## [2026-09-07T16:21:51.630Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && sed -n '1200,1230p' BQT_v4_pages.txt"
}
```


### [2026-09-07T16:21:51.675Z] TOOL RESULT

```
مس « مالیشطم *رك : دزی ج ۷ص 090 . ۷ - از اوستا 332۷۷880 ( رلد: هاء)
این‌کلمه دریسنی‌لهجه های ابرانی بافی‌مانده : کردی 13288 ۰ 13288 ۰ 332388 :10317288
( مله ),* ژایا ص ۳۸۸ ۰ درطبری نیز 33288 :

‏مه آش پرستی ته دیم ور قدیمه بهاره ۰ بهشته, مهر ومانگه» ته دیمه.
( آتش پرستی من در پیش روی توعادت قدیم است . بهار است » بهشت. است » خورشید و ماه
است . نه رویت ) «رضاقلی هدایت . انجمن‌آرا : دیم .> در فارسی هم‌آمده است :

‏بگرمی بدیشان یکی بان زد کزآن باتک تب لرزه بر مانگه زد .

‏عنصری بلخی « انجمن‌آرا » .
و« مانگه دیم » ( ماه صورت ) در اعلام کسان آمده .

‏۵ مائشن - بختح دال ».از : مان ( ریشه )+ دن ( پوند مصدری ) ۰ ایرانی باستان
3280 * پارتولمه ۰۴۱۱۲۶ پپلوی 31284188 «لیبر که ۵-۱4۶ * « تاوادیا ۱۹۲ :۶۲ ؛پارسی
باستان و اوستا - 33272 ۰ ( انتظار کشیدن ) ۰ پهلوی ۳22)1(9128 , 3228)1(9180 ۰ بازند
مقل2ق . ارمنی 338222 ( ماندن » انتظار کشیدن , خدمت کردن ) » لانینی ۰32886۵
بودانی 33628 ۶ کردی 73218 ( ماندن ) » بلوجچی 33882810 ۰ 333812 ( خته شدن )
قی : ظرمی‌ماندم. اقانی ع ۳32802 ۰ کردی 8۳28800 (خته) « اسشق ۹۹۹»؛ توقف کردن,
منزل کردن » اقامت کردن - انتظار کشیدن - خسته شدن - شبیه ومانند بودن - گذاشتن‌ونهادن-
[pdf page 34]
۱۹۱۱۳ مانه

بمعنی ماء باشد که قمر است - و بمعنی آفتاب مانو سار - بامین بی نقله بر وزن

هم ابنظرآمده است و بمعنی اول اسح است. آلوزار » نام یکی از کشنده ها و قاتلان داراب
مانمی ۱ « بنکون ثالك و کر میم این دارات است که او را فریب داد و قصد حیات

ونون ساکن‌درآخر » بلغت زند وپازند (۱) جامی اوکرد ۴ -

باشد که بدان (؟) شراب و آب و امثال آن مانوش - بروزن خاموش . نام کوعی
```


## [2026-09-07T16:22:15.925Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"مونترال\" \"مونت‌کارلو\" \"مونتکارلو\" \"پارامونت\" \"مونتگمری\"; do echo \"== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done"
}
```


### [2026-09-07T16:22:17.763Z] TOOL RESULT

```
Exit code 1
== مونترال
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
== مونت‌کارلو
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
== مونتکارلو
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
== پارامونت
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
== مونتگمری
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part1.txt:0
```


## [2026-09-07T16:22:24.800Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A7%D9%85%DB%8C%D8%AF/\" --note 'page 333: Mo\\047in entry for امید (omid)' 2>&1 | tail -2; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%85%D9%88%D9%86%D8%AA%D8%B1%D8%A7%D9%84/\" --note 'page 333: Persian مونترال Montreal' 2>&1 | tail -2"
}
```


### [2026-09-07T16:22:29.805Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/43c6b1d75a0fa9d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d50b36ce1e29075.txt
```


## [2026-09-07T16:22:33.243Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== omid ===\"; grep -n \"معین\\|امید\" 43c6b1d75a0fa9d8.txt | head -20; echo; echo \"=== montreal ===\"; grep -n \"معین\\|مونترال\\|فر\\.\" 6d50b36ce1e29075.txt | head -20"
}
```


### [2026-09-07T16:22:33.332Z] TOOL RESULT

```
=== omid ===
4:TITLE: امید - معنی در دیکشنری آبادیس
6:امید - معنی در دیکشنری آبادیس 
10: امید
13: مترادف امید : آرزو، امل، امیدواری، انتظار، توقع، چشم داشت، رجا
14: متضاد امید : نومیدی، یاس
21: اسم: امید (پسر) (فارسی) (تلفظ: om (m) id) (فارسی: اميد) (انگلیسی: omid) 
27: امید. [ اُ / اُم ْ می ] ( اِ ) در پهلوی ، اُمِت . در پازند، اُمِذ . ( از حاشیه برهان قاطعچ معین ). آرزو. ( حاشیه برهان قاطع ) ( ناظم الاطباء ).رجاء. ( ناظم الاطباء ) ( منتهی الارب ) ( تاج المصادر بیهقی ). رجو. رجاوة. مهه. ( منتهی الارب ) ( تاج المصادر بیهقی ). مرجاة. ( منتهی الارب ). امل. امله. ترجی. ارتجاء. ترجیه. آرمان. ( از یادداشتهای مؤلف ) : 
34:امیدم چنانست کز کردگار
36:از لب تو مر مرا هزار امید است 
38:همه بر امید اعتماد مکنید چنانکه دست از کار کردن بکشید. ( تاریخ بیهقی ).
44:ز دوزخ گذار و بفردوس امید. اسدی.
45:یکی نهاده بُوَد گوش بر امید سرود
46:یکی چشیده بُوَد داغ بر امید کباب. قطران.
48:باین امید که گفتم بسیت باید بود. ناصرخسرو.
55:فراخی امید و درازی امل. ناصرخسرو.
56:و در این امید پیر گشت. ( مجمل التواریخ و القصص ). بر درگاه ملک مقیم شده ام و آنرا قبله حاجات و مقصد امید ساخته. ( کلیله و دمنه ).
57:مرا وصال نباید همان امید خوش است 
60:شتابد سویم چون بمقصد امید. اثیر اخسیکتی.
69:دماغه ... یا دماغه امید نیک قطعه انتهایی افریقا را از طرف جنوب غربی تشکیل میدهد . 
71: فرهنگ معین

=== montreal ===
4:TITLE: مونترال - معنی در دیکشنری آبادیس
6:مونترال - معنی در دیکشنری آبادیس 
10: مونترال
23:از لحاظ جغرافیایی مونترآل در شرق کانادا در جنوب غرب استان کبک قرار دارد. مونترآل در ۵۳۹ کیلومتری شمال شرقی تورنتو و در ۱۹۰ کیلومتری شرق اتاوا قرار دارد. این شهر بزرگ ترین مرکز تجاری - صنعتی و فرهنگی کبک است. مونترال به آب های آزاد دسترسی دارد. حدود ۶۷٪ ساکنان آن فرانسه زبان می باشند. شهر مونترآل یک شهر با مجموعه ای از فرهنگ های مختلف است. شهر مونترآل یکی از مراکز عمده مهاجرین ایرانی در کشور کانادا می باشد. مونترآل در ۱۹۷۶ میزبان بازی های المپیک تابستانی بود. 
25:مونترال دارای آب و هوای قاره ای مرطوب است. ( طبقه بندی اقلیمی کوپن: به Dfa / DFB ) [ ۲] [ ۳] 
37:بندر درون بومی و مرکز تجاری کِبِک، کانادا، با ۳,۶۰۶,۷۰۰ نفر جمعیت (۲۰۰۴). در جزیرۀ مونترال در محل تلاقی رودهای اوتاوا و سنت لارنس واقع شده است. مونترال دومین بندر بزرگ ساحل شرقی امریکای شمالی، بندر اصلی شبکۀ آبی سنت لارنس ـ گریت لیکس (دریاچه های بزرگ) و دورترین بندر درون بومی جهان از دریا، واقع در ۱,۶۰۰کیلومتری اقیانوس اطلس، است. صنایع آن عبارت اند از پالایش نفت، تولید ابزار و آلات فنی، فرآوری مواد غذایی، فولاد، هواپیما، کشتی، مواد پتروشیمی، توتون، پوشاک، خمیر کاغذ و کاغذ. فرانسوی ها در ۱۶۴۲ مونترال را تأسیس کردند؛ در ۱۷۶۳ به تملک بریتانیا درآمد. این شهر در توفان بزرگ یخ ژانویۀ (۱۹۹۸) به شدت آسیب دید و دکل های برق از یخ پوشیده شد و بعضی از آن ها زیر فشار یخ واژگون شدند. مونترال دومین شهر بزرگ فرانسوی زبان پس از پاریس است. wikijoo: مونترآل 
41: معرفی شهر مونترال
42:مونترال یکی از مهم ترین و جذاب ترین شهرهای کاناداست و در استان کبک قرار دارد. این شهر پس از تورنتو، از بزرگ ترین شهرهای کانادا به شمار می آید و به خاطر ترکیب خاصی از فرهنگ اروپایی و آمریکای شمالی شناخته می شود. 
44:ویژگی های اصلی مونترال
45:• زبان رسمی و رایج: بیشتر مردم مونترال به فرانسوی صحبت می کنند، اما انگلیسی هم بسیار رایج است. 
47:• جمعیت: مونترال شهری پرجمعیت و چندفرهنگی است و مهاجران زیادی از کشورهای مختلف در آن زندگی می کنند. 
52:چرا مونترال معروف است؟
54:مونترال یکی از مراکز مهم فرهنگی کاناداست. این شهر:
63:مونترال ترکیبی از بافت تاریخی و مدرن است:
64:• مونترال قدیم ( Old Montreal ) با خیابان های سنگ فرش و ساختمان های تاریخی
68:مونترال یکی از شهرهای مهم دانشجویی کاناداست و دانشگاه های معتبری مثل:
75:مونترال سیستم حمل ونقل عمومی نسبتاً خوبی دارد:
81:مونترال به خاطر تنوع غذایی اش هم معروف است. چند مورد مشهور:
85:کافه ها، رستوران ها و بازارهای محلی بخش مهمی از زندگی شهری در مونترال هستند. 
87:مزایای زندگی در مونترال
```


## [2026-09-07T16:22:41.444Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '69,85p' 43c6b1d75a0fa9d8.txt"
}
```


### [2026-09-07T16:22:41.493Z] TOOL RESULT

```
دماغه ... یا دماغه امید نیک قطعه انتهایی افریقا را از طرف جنوب غربی تشکیل میدهد . 

 فرهنگ معین

 (اُ مّ ) (اِ. ) ۱ - آرزو. ۲ - چشمداشت . 

 فرهنگ عمید

 آرزوی روی دادن امری همراه با انتظار تحقق آن، چشمداشت.
* امید بستن: (مصدر لازم، مصدر متعدی ) خواهان چیزی یا کسی شدن.
* امید داشتن: (مصدر لازم، مصدر متعدی ) امیدوار بودن، انتظار داشتن. 

 گویش مازنی

 /omid/ آبستن

 واژه نامه بختیاریکا
```


## [2026-09-07T16:22:49.209Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD men roots ===\"; grep -n \"^men-\\|^men-[0-9]\\|^mon-\\|^men\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T16:22:49.253Z] TOOL RESULT

```
=== AHD men roots ===
217:men-1, I. Zero-grade form *mn-...
745:men-!, To think; with derivatives referring to various qualities and states of mind and thought. I. Zero-grade form *mn-. 1. Suffixed form *mmy-ti- in: a. Germanic “ga-mundi- (*ga-, intensive prefix; see kom), in Old English gemynd, memory, mind: MIND; b. Latin méns (stem ment-), mind: MENTAL; AMENT?, DEMENT; c. Latin mentid, remembrance, mention: MENTION. 2. Suffixed form *mn-to- in Greek -matos, “willing”: AUTOMATIC. 3. Suffixed form *mn-yo- in: a. Greek mainesthai, to be
747:meng-
749:men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously “chin, jaw, mouth,” in Germanic *mun- thaz in Old English mith mouth: mouTu. 2. Latin mi- nae, projecting points, threats (> mindri, to threaten): MENACE, MINACIOUS; AMENABLE, DEMEAN!, PROME- NADE. 3. Latin -minére, to project, jut, threaten: EMI- NENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin méns (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT!, MOUNT?, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726, 2. menth- 732.] men-3, To remain. Variant suffixed (stative) form *man-é- in Latin manére, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.] men-‘. Small, isolated. 1. Greek manos, rare, sparse: MANOMETER. 2. Suffixed o-grade form *mon-wo- in Greek monos, alone, only, single, sole: MONAD, MONAS- TERY, MONK, MONO-; PSEUDOMONAD. 3. Possibly also suffixed form *men-i-, a small fish, in Old English myne, mynwe, minnow, perhaps the source of Middle English meneu, a small fish: MINNOW. [Pok. 4. men- 728, meni- 731.] mend-. Physical defect, fault. 1. Latin mendum, menda, defect, fault: MENDICANT; AMEND, EMEND, (MEND). 2. Latin mendax, lying, liar: MENDACIOUS. [Pok. mend(a) 729.) mendh-'. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMAT- ICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.] mendh-?. To chew. 1. Latin mandere, to chew: MANDI- BLE, (MANGE), MANGER. 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew: MASSETER; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE; Cc. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.] menegh-. Copious. Germanic *managa- in Old English manig, menig, many: MANY. [Pok. men(e)gh- 730.] meng-. To furbish. 1. Latin mango, furbisher, gem pol- isher, swindler: MONGER. 2. Greek manganon, magic
```


## [2026-09-07T16:22:56.724Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"MANE\\b\\|mono-, Neck\\|Neck\\.\" AHD_watkins1985.txt | head -10; echo \"=== search mane derivative ===\"; grep -n \"in Old English manu\\|manu, mane\\|mane:\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T16:22:56.784Z] TOOL RESULT

```
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
762:mizdho-. Reward. West Germanic *médé- in Old English méd, reward, compensation, meed: MEED. [Pok. mizdho- 746. m6-. To exert oneself. Suffixed form *mé-I- in: a. Latin molés, heavy bulk, mass, massive structure: MOLE%, MOLECULE; DEMOLISH; b. Latin molestus (irregularly from mdélés), labored, difficult, troublesome: MOLEST. [Pok. m6- 746.] m6d-. To meet, assemble. 1. Germanic *mdtjan in Old English métan, to meet: MEET!. 2. Germanic *méta- in Old English mot, gemét (ge-, together; see kom), meet- ing, moot, assembly, council: MOOT; FOLKMOTE, GEMOT, WITENAGEMOT. 3. Perhaps suffixed zero-grade form *mod-tlo- in Germanic *mathla- in Old Norse mdl, speech, agreement (> Norwegian mdi, speech): MAIL; (BLACKMAIL), RIKSMAL. [Pok. mdd- 746.] modhro-. A color. Germanic *madraz in Old English meedere, madder: MADDER!. [Pok. modhro- 747.] molko-. Skin bag. Germanic *malhé- in Old High Ger- man malha, pouch, bag, akin to the Germanic source of Old French male, bag: Matti. [Pok. molko- 747.] mone. Neck, nape of the neck. 1. Germanic *man6 in Old English manu, mane: MANE. 2. Latin monile, necklace: MONILIFORM. [Pok. mono- 747.] mori-. Body of water; lake (?), sea (?). 1. Germanic *mari- in: a. Old English mere (> Middle English mere), sea, lake, pond: MERE?; (MERMAID); b. Old Norse marr, sea, akin to the Scandinavian source of MARRAM; C. Old High German mari (> German Meer), sea: MEER- SCHAUM. 2. Germanic *mariska-, water-logged land, in: a. Old English mersc, merisc, marsh: MARSH; b. Old French marasc, maresc, marsh: MORASS. 3. Latin mare (> French mer), sea: MARE?, (MARINARA), MARINE, MARI- TIME; BECHE-DE-MER, MARICOLOUS, MARICULTURE, OR- MER, ULTRAMARINE. [Pok. mori 748.] mormor-. Also murmur-. Murmur. Imitative root. Latin murmur, a murmur: MURMUR. [Pok. mormor- 748.] moro-. Blackberry, mulberry. 1. Greek moron, mulberry, in sukomoros, an African fig tree: SYCAMORE. 2. Latin morum, mulberry (probably from Greek): MORULA, MUR- REY; MULBERRY. [Pok. moro- 749.] morwi-. Ant. 1. Germanic variant form *meur- in Danish myre, ant, akin to the Scandinavian source of Middle English mire, ant: PISMIRE. 2. Variant form *morm- in: a. Greek murméx, ant: MYRMECO-; b. (with dissimila- tion) Latin formica, ant: FORMIC, FORMICARY; FORMICI- vorous. [Pok. morui- 749.] m6(u)lo-. Name of a plant. Greek mélu, moly: MOLY. [Pok. mé(u)-lo- 750.] m6(u)ro-. Foolish. Greek méros, foolish: MORON; OXYMO- RON. [Pok. mé(u)ro- 750.] mozgo-. Marrow. Germanic *mazg6- in Old English mezrg, mzerh, marrow: MARROW. [Pok. moz-g-o- 750.] mregh-m(n)o-. Brain. 1. Germanic *brag-na- in Old English bregen, brain: BRAIN. 2. Greek bregma, the front part of the head: BREGMA. [Pok. mregh-m(n)o- 750.] mregh-u-. Short. I. Suffixed form *mregh-w-i- in Latin brevis, short (> briima, the shortest day, winter): BRIEF, BRUMAL; ABBREVIATE, (ABRIDGE). II. Zero-grade form *“mrghu-. 1.Germanic *murgja-, short, also pleasant, joyful, in: a. Old English myrge, mirige, pleasant: MERRY; b. Germanic *murgithd, pleasantness, in Old English myrgth, pleasure, joy: MIRTH. 2. Greek brakhus, short: BRACHY-; AMPHIBRACH, TRIBRACH. 3. Greek com- parative brakhion, shorter, hence also “upper arm” (as opposed to the longer forearm): BRACE, BRACERO, BRA- CHIUM, BRASSARD, BRASSIERE, PRETZEL; EMBRACE. [Pok. mreghu- 750.] mu'-. Imitative of inarticulate sounds. 1. Reduplicated form in Germanic *mum- in: a. Middle Low German mummen, to be silent, akin to Middle English mum, silent: MUM}; b. Icelandic mumpa, to eat greedily, akin to the probable Scandinavian source of dialectal English mump, to mumble, grimace: MUMPs; c. Low German
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1811:MANACLE man-2 MANAGE man-2 MANANA ma-1 -MANCY men-! MANDAMUS man-2 MANDARIN men-1 MANDATE man-2 MANDIBLE mendh-2 MANDOLIN pandoura MANE mon-
=== search mane derivative ===
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
762:mizdho-. Reward. West Germanic *médé- in Old English méd, reward, compensation, meed: MEED. [Pok. mizdho- 746. m6-. To exert oneself. Suffixed form *mé-I- in: a. Latin molés, heavy bulk, mass, massive structure: MOLE%, MOLECULE; DEMOLISH; b. Latin molestus (irregularly from mdélés), labored, difficult, troublesome: MOLEST. [Pok. m6- 746.] m6d-. To meet, assemble. 1. Germanic *mdtjan in Old English métan, to meet: MEET!. 2. Germanic *méta- in Old English mot, gemét (ge-, together; see kom), meet- ing, moot, assembly, council: MOOT; FOLKMOTE, GEMOT, WITENAGEMOT. 3. Perhaps suffixed zero-grade form *mod-tlo- in Germanic *mathla- in Old Norse mdl, speech, agreement (> Norwegian mdi, speech): MAIL; (BLACKMAIL), RIKSMAL. [Pok. mdd- 746.] modhro-. A color. Germanic *madraz in Old English meedere, madder: MADDER!. [Pok. modhro- 747.] molko-. Skin bag. Germanic *malhé- in Old High Ger- man malha, pouch, bag, akin to the Germanic source of Old French male, bag: Matti. [Pok. molko- 747.] mone. Neck, nape of the neck. 1. Germanic *man6 in Old English manu, mane: MANE. 2. Latin monile, necklace: MONILIFORM. [Pok. mono- 747.] mori-. Body of water; lake (?), sea (?). 1. Germanic *mari- in: a. Old English mere (> Middle English mere), sea, lake, pond: MERE?; (MERMAID); b. Old Norse marr, sea, akin to the Scandinavian source of MARRAM; C. Old High German mari (> German Meer), sea: MEER- SCHAUM. 2. Germanic *mariska-, water-logged land, in: a. Old English mersc, merisc, marsh: MARSH; b. Old French marasc, maresc, marsh: MORASS. 3. Latin mare (> French mer), sea: MARE?, (MARINARA), MARINE, MARI- TIME; BECHE-DE-MER, MARICOLOUS, MARICULTURE, OR- MER, ULTRAMARINE. [Pok. mori 748.] mormor-. Also murmur-. Murmur. Imitative root. Latin murmur, a murmur: MURMUR. [Pok. mormor- 748.] moro-. Blackberry, mulberry. 1. Greek moron, mulberry, in sukomoros, an African fig tree: SYCAMORE. 2. Latin morum, mulberry (probably from Greek): MORULA, MUR- REY; MULBERRY. [Pok. moro- 749.] morwi-. Ant. 1. Germanic variant form *meur- in Danish myre, ant, akin to the Scandinavian source of Middle English mire, ant: PISMIRE. 2. Variant form *morm- in: a. Greek murméx, ant: MYRMECO-; b. (with dissimila- tion) Latin formica, ant: FORMIC, FORMICARY; FORMICI- vorous. [Pok. morui- 749.] m6(u)lo-. Name of a plant. Greek mélu, moly: MOLY. [Pok. mé(u)-lo- 750.] m6(u)ro-. Foolish. Greek méros, foolish: MORON; OXYMO- RON. [Pok. mé(u)ro- 750.] mozgo-. Marrow. Germanic *mazg6- in Old English mezrg, mzerh, marrow: MARROW. [Pok. moz-g-o- 750.] mregh-m(n)o-. Brain. 1. Germanic *brag-na- in Old English bregen, brain: BRAIN. 2. Greek bregma, the front part of the head: BREGMA. [Pok. mregh-m(n)o- 750.] mregh-u-. Short. I. Suffixed form *mregh-w-i- in Latin brevis, short (> briima, the shortest day, winter): BRIEF, BRUMAL; ABBREVIATE, (ABRIDGE). II. Zero-grade form *“mrghu-. 1.Germanic *murgja-, short, also pleasant, joyful, in: a. Old English myrge, mirige, pleasant: MERRY; b. Germanic *murgithd, pleasantness, in Old English myrgth, pleasure, joy: MIRTH. 2. Greek brakhus, short: BRACHY-; AMPHIBRACH, TRIBRACH. 3. Greek com- parative brakhion, shorter, hence also “upper arm” (as opposed to the longer forearm): BRACE, BRACERO, BRA- CHIUM, BRASSARD, BRASSIERE, PRETZEL; EMBRACE. [Pok. mreghu- 750.] mu'-. Imitative of inarticulate sounds. 1. Reduplicated form in Germanic *mum- in: a. Middle Low German mummen, to be silent, akin to Middle English mum, silent: MUM}; b. Icelandic mumpa, to eat greedily, akin to the probable Scandinavian source of dialectal English mump, to mumble, grimace: MUMPs; c. Low German
```


## [2026-09-07T16:23:09.443Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC men- ===\"; grep -nE \"^men(o|ō|ē|-)|^menō |^mn̥ti|^monos|^monā\" IEC.txt | head -20; echo \"=== IEC mont ===\"; grep -n \"mont-\\|mṇti\\|mnti\" IEC.txt | head -10; echo \"=== IEC mon- neck ===\"; grep -n \"monos\\b.*neck\\|mono-.*neck\\|'neck'\" IEC.txt | head -10"
}
```


### [2026-09-07T16:23:09.518Z] TOOL RESULT

```
=== IEC men- ===
10631:meno (1) “remember; think; remind’. Cf. mno (1). WP II, 264 Skt. cf. a-manami ‘mention’; mnaye, mp. "am mentioned'; mánman, n. see menmn- (1); Gk. cf. eu-menéo ‘think well of; be kind’; cf. mém- in mémphomai ‘reproach’; OLat. meno re member" beside minae (threats, lit. 'remind- ers”); Ir. cf. meanma, m. (^mind'. See menmn- (1); ON minna, v. ((remind'; impers. Áremem- ber’, denom.?); mod. cf. menjar, minjar, fpl. ‘memorial; Sw. minnas, refi. ‘remember’; minne, wn. ‘memory’; Li. menù, miñti ‘re- member’; mënamas, adj. ‘supposed’; cf. menà, f. ‘thought’
10637:menos, -es- “power, craft, ability, skil’. WP II, 264 Skt. mánas, n. “mind, mood, skilP ; Av. mano, n. id.; manahyo, adj. ‘intellectual; Per. manis ‘temperament; Gk. ménos, gs -eos, n. ‘power, desire, plan, design’; cf. a-meínon, comp. "better" It. ména (^work, task, condition, qua- lity, kind', whence menare ‘do, put, move, lead, deal, make"); OLat. cf. Menerua, Lat. Minerva (‘goddess of arts and crafts’, fr. *me- nes-uà) beside minerval, n. *college-fee'; ad- miniculum “prop, aid’; W cf. menw, m. “in- tellec'; ON cf. mennt, f. “art, skill; menntr, adj. (educated', fr. menna, v. ‘educate’. Re- dup.?); Li. ménas, m. "art
11136:monos, us (monuos) ‘remaining, alone, single, individual. WP II, 267 Gk. mónos, moünos ‘alone’; moné *dwelling'; OBr. cf. guo-monet ‘domain’; W mon, f. ‘iso- lation, solitary object. Cf. meno (3) & mnó (3)
=== IEC mont ===
6695:kam- (2) ‘restrain’; kam-, kamont- “rein, bridle, horse-collar? Per. kamand ‘halter’; Du. baam: E hames ‘horse-collar’ beside MHG hamen, ON hemja
6705:kamont-, see kam- (2)
10651:mentis, us thought, remembrance'. (Variant of type mntis, q. v.), cf. mend (1) Skt. mantih, f., and mántuh, f. *thought'; Go. cf. ana-minds, f. ‘supposition’; OHG gamin- thi, n. ‘remembrance’
10923:mn-, zero-radical form of men-, see meng (1), mntis, etc. OS munan, inf. (aor. pres.) ‘think, believe"; OE man, 3s. (aor. pres.), munan, inf. *mind, remember; cf. mun, adj. ‘mindful; myne, m. *memory, wish, feeling; MHG cf. münigen, v. ‘remember; ON munr, npl. munir, m. “mind; love; desire; delight; Icel. cf. muna, a-st. ‘vary’; Go. muns ‘thought?
10957:mnt- (2) (mont-) ‘wrong, error, falsehood'. Cf. mont- Skt. cf. (o-gde) mantuh (2) “fault; Gk. mate, f. ‘error, crime, folly’ beside máten, Dor. má- tàn ("falsely, in vain”, fr. *nptam); Lat. men- tior, -iri, v. ‘tell lies’. (For isophonic Gk. mán- tis *prophet" cf. mant-) (-n-)
11137:mont- (1) ‘defective; defect. Cf. mnt- (2) Skt. cf. mantuh, m. (2) ‘fault’; Br. mons 'de- fective; Cor. cf. mans, adj. (‘crippleďd’, fr. *mnt-)
11138:mont- (month-) “stir, disturbance, move, re- moval; movable(s)'. Cf. mentó, mentos, mnt- MHG cf. mende, sf. ‘joy’; ge-mende, adj. ‘gay’; menden, mennen ('rejoice' if for *monteijo); OS mendian, v. id.; OCS motü, m. 'distur- bance; filth’; Pol. met, m. ‘cloudy water’; Cz. cf. moutev, f. /(stirring-stick'; s-mutek, m. ‘mourning’; Li. mantà (property, movables’. Sense of Lat. mobiles res furniture); Latv. manta, f. id.; mante, f. *potter's spatula’
13564:pro-mntis (-mtis, pro-) ‘intention, will, meaning, responsibility, care’. Cf. pro-, mntis. (Semantics diversified in the derived forms) Skt. pramatih, f. ‘care, protection’; Per. far- mūd, s. ‘ommand’, cf. farmūdan, v., radical: farma, v. "order": Gk. prómantis ‘prophetic;
=== IEC mon- neck ===
```


## [2026-09-07T16:23:16.231Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"meno (3)\\|mnō (3)\\|mno (3)\\|menó (3)\" IEC.txt | head; echo \"=== monile/monilis ===\"; grep -n \"monilis\\|monile\\|moni-.*neck\\|monios\" IEC.txt | head -6; echo \"=== mons entry ===\"; grep -n \"^mons\\|montis\\|mṇtis.*mountain\\|'mountain'\" IEC.txt | head -8"
}
```


### [2026-09-07T16:23:16.310Z] TOOL RESULT

```
10630:menmn- (2) ‘remaining; remainder, dwel- ling, place’. Cf. meno (3). Var: mən- Br. mann, f. ‘place’; W man, pl. -au, m. & f., id.; OE cf. æ-men(ne) ‘deserted’; -menne, s. (‘solitude’, fr. *aue-^). (All forms *men- or *mon-)
10633:menó (3), (míméno) ‘remain, be, rest. Cf.
10950:mno, io (mon-) (3) ‘remain’. Cf. meno (3). WP II, 267 Skt. (alleged) man- ‘hesitate’; Av. man-, v. ‘remain’; Ober, man-, id.; Per. manam, inf: mandan, id. (Indo-Iran. prob. e-gde); Arm. (e-gde) mnam, v. id. beside mena-, cpds. *sole-; Gk. (intensive) miímno beside méno, id.; Lat. (r-gde) maneo, ere, id.; Br. ménel, inf., manet, pp. id.
11136:monos, us (monuos) ‘remaining, alone, single, individual. WP II, 267 Gk. mónos, moünos ‘alone’; moné *dwelling'; OBr. cf. guo-monet ‘domain’; W mon, f. ‘iso- lation, solitary object. Cf. meno (3) & mnó (3)
=== monile/monilis ===
11101:mon-, (monio, monuis, monus) ‘neck, nape; mane’ Skt. cf. manya, f. du. & pl. ‘muscles of neck, nape’; manyākā, f. id.; OPer. (in Gk.) maniá- kēs, m. ‘necklace’; Av. cf. manoðris, f. “back of head” beside (variant) minus, m. (“neck- lace’, fr. *mon-); Iran. LW in Arm. maneak ‘necklace’; Doric mónnos E mánnos (“neck- lace”, from Iran.?); Lat. cf. monile, n. id. (and
11121:monil-, see mon- ‘neck’, etc. Lat. monile, n. ‘necklace, horsecollar ; MIr. muinél, muineul, mod. muinéal, m. id.
11124:monios, io ‘mind, thought, memory’. Cf. menó (1), etc. Skt. manyah 'opinionated'; manyüh, m. ‘mood’; Av. cf. mano, adj. ‘mental, intellec- tual'; mainis, m. ‘penalty’; Gk. cf. -monë in pé-moné, f. ‘injury and *mon- in móm-pheé (*blame', cf. mend (1) & bhà-mi); ON menjar, fpl ‘souvenir; memorial; Li. manüs (thought- ful, intelligent; Latv. mana, f. ‘reason, wis- dom, conscience
=== mons entry ===
10995:moghənt- (moghnt-) ‘big, great strong’. (The velar consonant is represented in Av. mayom ‘greatness’, and is explicit in Skt. maghám *reward'") Skt. mahát ‘great; greatness’; Av. cf. mazafit, id. (w. secondary palatalism?); Tokh. mokats ‘strong’; Lat. prob. mons, gs montis, gp mon- tium, m. “mountain; mass, quantity” (but cf. Av. matis 'cliff, peak' for possible variant *mnt-. For Olr. mét, melt, f. ‘size, greatness’; Ir. méid, m & f ‘quantum’; OW meint, f., W maint, m. amount, size, quantity’; Br. ment, mend, f. id.; OBrit. pa-mint “how much cf. megont- ‘quantity’ above); OFris. magande “mighty, able’; ON megandi, id.; OCS mogoti, mogosti, m. ‘master; Cz. cf. mohutny ‘mighty’; v$e-mohoucí ‘almighty’; R mogücij ‘powerful’; Srb. moguć possible; wealthy; powerful. Cf. WP II, 238 & 257
```


## [2026-09-07T16:23:27.678Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW maneo ===\"; grep -n \"^maneo\\|^maneō\\|maneo, -ere\" LEW_1910.txt | head -5; echo \"=== LEW mons ===\"; grep -n \"^mons\\|^mōns\\|mons, -tis\" LEW_1910.txt | head -5; echo \"=== LEW mineo ===\"; grep -n \"^mineo\\|^-mineo\\|emineo\\|ē-mineo\" LEW_1910.txt | head -5; echo \"=== LEW monile ===\"; grep -n \"^monile\" LEW_1910.txt | head -3"
}
```


### [2026-09-07T16:23:27.766Z] TOOL RESULT

```
=== LEW maneo ===
=== LEW mons ===
=== LEW mineo ===
=== LEW monile ===
```


## [2026-09-07T16:23:31.421Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"maneo\" LEW_1910.txt | head -5; echo \"---- LAT ----\"; grep -n \"maneo\\|mane5\\|manere\" LAT.txt | head -8; echo \"=== LAT mons ===\"; grep -n \"mons, montis\\|mons :\\|mons\\b\" LAT.txt | head -8"
}
```


### [2026-09-07T16:23:31.494Z] TOOL RESULT

```
---- LAT ----
36165:ad cuiusmodi religionem Graeci quoque, cum lumen affertur, solentmane5
36174:maneo, -es, mansi, mansum, -ere (un ancien supin *mantum est at-
36194:(dpoq. impdr.); circum-, con-maneo (= cnjp,p,evcd, auvoi,xw); immaneo:
36195:rester dans (tardif et rare; calque de ep.p,evoo); intermaneo: rester
36196:parmi (Luc.); permaneo: rester jusqu'au bout, M.L.6417; permansio
36197:(Cic.); remaneo : rester en arriere, demeurer, M.L.7194; remansio
36198:(Cic.), remansor et subremaneo; emaneo: rester dehors; depasser les
36216:ter le rapprochement avec lat. manere et arm. mnam "3 e reste"; y aurait-il
=== LAT mons ===
2191:arietem immolat, dicti ab agon, et les noms propred mons Quirinalis
9057:mons (cf. les derivis bas latins campdneus, -nius, dans les Gromat.
23364:la forme en -ti- ne peut etre que secondaire; cf. mons. Sans doute
37593:de la racine *men- "etre saillant", cf. mons, emineo (sous minae),
38067:une racine mei-. Mais on a peine A separer e-nineS de mons; 1 'amS;
38071:lant" representee en latin meme par mons (v. ce mot) et par monile,
38075:sont autres que dans maneo, canem', cf. ce qui est dit de mons. Mais
38866:mons, etc. (v. ce mot). Le mot signifiant "nuque" sert aussi a indiquer
```


## [2026-09-07T16:23:34.661Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36174,36225p' LAT.txt; echo \"########## minae/emineo ##########\"; sed -n '38060,38090p' LAT.txt; echo \"########## monile ##########\"; sed -n '38860,38880p' LAT.txt"
}
```


### [2026-09-07T16:23:34.748Z] TOOL RESULT

```
maneo, -es, mansi, mansum, -ere (un ancien supin *mantum est at-
teste indirectement par les formes d'iteratifs archaiques manto,-as
"saepe mangre", F.118,1; ommentans (liu.Andr.) "saepe obmanens" id.
ao0,3; cf. merto, pulto): 1° rester (sens absolu), d'ou "demeurer, se-
journer" ( cf. (leveiv); a° attendre (sens tran sitif). — Ancien, usuel.
M.L.say6. Celt.: iri. maner; bret. manout ?
Derives et composes: mansid: fait de rester ou de sejourner (Ter.,
Cic.); lieu de sejour (.pecorum mansid', mansid equorum = ototootoctiov) ,
halte, etape (epoq. imper.) et par suite, avec developpement de sens
concret (cf. legio) "maison" (ou l'on fait 4 t ape), mansio habens tria
tecta: TpiCTTeya (Gloss.). Mansio s'est conserve a la fois dans le
sens de "etable, abri pour les troupeaux", et de "maison" (ou il
a, avec casa, supplante domus et aedes ), cf.M.L.5311, et a fourni
de nombreux d^rivds attest^s directement ou par les langues romanes,
*mansiondta S313, *mansiondticus 5314, *ndnsidnlle 5316, mdnsionarius
"de passage", -un coniugiun Fulg.j subst. mansiondrius m.: ostiarius,
qui custodit aedem (Gloss.), conserve dans les 1 . romanes avec le
sens de "serviteur", M.L.531«; mansiuncula (Vulg.): petite loge,
chambre; ndnsor,-oris ; mansorius (tous deux dans Aug.); cf. aussi
M.L.5332 *ma(n)sum, 5333 ma(nj sura, 5318 *ma(n)suarius; mansito, -as
(dpoq. impdr.); circum-, con-maneo (= cnjp,p,evcd, auvoi,xw); immaneo:
rester dans (tardif et rare; calque de ep.p,evoo); intermaneo: rester
parmi (Luc.); permaneo: rester jusqu'au bout, M.L.6417; permansio
(Cic.); remaneo : rester en arriere, demeurer, M.L.7194; remansio
(Cic.), remansor et subremaneo; emaneo: rester dehors; depasser les
limites d'une permission (t.de la 1. militaire c. remansor ; de la,
Smansor, emansio). De manens, la 1 . philosophi que a tire manentia
(S t- Aug.) pour traduire (xovq, cttoct
L’a n r est pass^ a i en aucun cas, grace a quoi il n’y a pas eu
conflit homonymique avec e-mineo.
Il est douteux qu'il y ait eu un present ra^lical indo-europeen;
car gr. (xevo) "j e reste" est isole; le present a redoublement p,i,(XV(jO
a une valeur "determinee". L'e de nandre a peut-etre eon correspondant
dans le parfadt gr. p,ep,evr)xa, le latin a recouru a ce type faute d'avoir
un present radical ancien; mansum a 4 t 4 fait sur mansi qui est evi-
demment secondaire. L'armenien a une forme en -a- (suffixe -a-; et
la racine a un degre long e): mnam "3 e reste". En indo-iranien, il
n'y a pas non plus de forme radicale simple; le vedique a un impdratif
A redoublement mamandhi...; la racine existe aussi en iranien, et
notamment dans persan mandan "rester"; av. mqnaya- suppose manaya-.
M.H.Pedersen, V.G.d.k.Spr. II 456, admet que v. iri. ana id "il reste"
repondrait a skr. aniti "il respire"; il est difficile cependant d'ecar-
ter le rapprochement avec lat. manere et arm. mnam "3 e reste"; y aurait-il
eu quelque contamination ?
Manes (Dl), -Ium m.: (Dieux) Manep. Le ion est g 4 neralement inter¬
prete comme le pluriel de 1 'adj. manis, "les Dieux bons", cf. Bucheler,
C.E.1164,1, Di Manes, manes sitis, .epithete par laquelle on designait60 3 -
manis
par eupb^misme leg esprits des morts, et specialement des parents
( di parentes) . La notion des Manes s'etant obacurcie, Dl manSs est
devenu une sorte de cliche employe en pariant des morts, et meme d’un
seul individu: Dis Manibus coniugis n'a guere d'autre sens que "a la
########## minae/emineo ##########
"mines" monnaie grecque), me liust te minis certare necum quam minaciis',
cf. M.L. 5584.
Autres derives: minatio (rare); minitor,-aris (minito), et ses
derivas; ad-minor, -minitor (ital.), comminor "se mettre a faire des
menaces"; interminor (-mino), contamination de minor et de interdico,
dans la 1 . des comiques; praeminor (Apul.).
Aucune dt^mologie n'appara£t pour une forme minae, qui supposerait
une racine mei-. Mais on a peine A separer e-nineS de mons; 1 'amS;
minent de Lucrece ne suffit pas i garantir un ancien mtneS: la forme
peut etre tirde de SnineS, promineo, etc., qui sont courants. 11 y
aurait alors une dtymologie. Car il y a une racine *men- "etre sail-
lant" representee en latin meme par mons (v. ce mot) et par monile,
peut-etre aussi par mentum', mais minae ne pourrait etre apparenti
que si c r etait un derivd d , une forme radicale *m *n- qui aurait abouti
a min- dans les conditions ou l'on a cinis, sine', les conditions
sont autres que dans maneo, canem', cf. ce qui est dit de mons. Mais
pareille hypothese est arbitraire.
Minerua ( arch. et dial. Menerua), -ae f.: — dicta quod bene moneat.
Hanc enim pagani pro sapientia ponebant, P.F.109,37; cf. Fest. 332,23,
promeneruat item (i.e. in carmine Saliari) pro monet. Rattachd ordi-
nairement a la racine *men~, cf. mens. Mais le mot semble d'origine
etrusque.
Derives: Mineruium', -udlis adj., -ual n.: cadeau ou salaire fait au
professeur; -ualiciun.
mingo, “is, mixl, mictum (et minxi, minctum), -ere: pisser. Po¬
pulaire ou technique (satiriques, Celse). Forme A nasale infixde appa-
rentee A meio. M.L.5563 mictum.
Derives et composes: mictio, mictus, mictito, micturio, mictorius,
mictilis, mictualis', commingo, M.L.3085, conmictilis. Les gloses
ont un iteratif mlnsare: saepius ningere, CGL IV 358,35; V 307,37
(cf. pisdre M.L.G544).
########## monile ##########
le dial. italien de Verone, M.L.56G0.
D 4 riv 4 d'un mot signifiant "nuque", cf. skr.ndnya "nuque", av.
manaoQrl-, gall. nwniog l et irl.muinel "cou". Les notions de "nuque"
de "objet saillant" ^tant liees, comme on le voit par gr. Xocpoc "col¬
line" et "nuque" et hom.8ei.pac "eminence" en face de 8et.pT} "nuque,
cou" et par av. grlva- "eminence" et "nuque". On rapprochera donc lat.
mons, etc. (v. ce mot). Le mot signifiant "nuque" sert aussi a indiquer
la "criniere" (d f un cheval), ainsi le correspondant slave griva de
indo-iran .grlva- signifie "criniere" et aussi en russe "eminence".
Cf. le sens germanique du mot parent de str.manya dans v.h.a. mana,
v.angl .manu "criniere", et aussi iri. mong "criniere"; ceci rend compte
du second sens de monile. Quant a 1'autre sens, cf.iri. muin-torc
"torques", v.h.a.mermt "collier", v.sl. monisto "collier" (formation733
mon strum
obscure); de mene en slave grivina "collier", de griva, au sens ancien
de "nuque, cou". Le mot p,txvUOtxriS designe en grec le "collier" porte
par des guerriers barbares; il doit etre d'origine gauloise; cf. aus -
si jxavvos ou p.ovvo£ atteste par Pollux V 99 et par le scholiaste de
Theocrite XI 41.
nonna, monnula, -ae f. (bas latin): terne de tendresse, de ca~
ractere populaire, a geminee expressive. Cf .nonnus, -a, etc.Dey.ova?
```


## [2026-09-07T16:23:50.353Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT mati / Bergvorsprung ===\"; grep -n \"Bergvorsprung\\|Vorgebirge\\|maiti-  f\\|'mati-\" BRT.txt | head -10; echo \"=== HUB manden ===\"; grep -n -i \"mänden\\|manden\\|mänistan\\|manistan\" HUB.txt | head -10"
}
```


### [2026-09-07T16:23:50.411Z] TOOL RESULT

```
=== BRT mati / Bergvorsprung ===
=== HUB manden ===
3426:iran. I, p. 211). So kann manistan *ahnlich sein' mit
```


## [2026-09-07T16:23:59.958Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^• .*mati\\b\\|•  j\\.  mati\\|maiti-\" BRT.txt | head -10; echo \"=== grep 'mati-' anywhere ===\"; grep -o \"mati-[^ ]*\" BRT.txt | sort | uniq -c | sort -rn | head -10"
}
```


### [2026-09-07T16:24:00.057Z] TOOL RESULT

```
7746:•  g.  aras  (,  j.  ar/)  Adv.  'richtig,  recht, wahr':  ärmati^iS uxitäil  fyaoianä  ?r'  daid- yat  (sd.)  Y.  44. 10;  —  beim  V.  vi-kay-: frB  va  fraSxya . .  mrüiteisA)  . .  ä.manat?hä 3f  vlHdysi  (sd.)  Y.  4f).  6;  —  os^ä  hudatthö ir'  vlsystä  nStt  duzdrn^hü  (sd.)  Y._jo.  3; 6;  —  beim  V.  vak-:  tat  %V}ä  p>r3Sä  (sd.) ar'  nwi  vaoc^  aAurJ  Y.44.i~i9"; — 'r° msi  prj-.ücqnt''  vauhSui  va/u/{sd.)  mana- uhS  Y,  48'().
8063:•  g-,  j.  isya-  Adj.  (fem.  "yä-)  i)  'erwünscht; begehrenswert':  kä  %wsi  asa  äkä  (sd.) andrang  'yl  Y.4S.%;  —  asahyä  >wj.i  (sd.) aslm  yqm  'yqm  "den Preis ..,  den  begehrens- werten, welchen  . ."  Y.54.r._  2)  von Personen  'lieb,  traut':  b?rfx<iqm  nwi  .  . daldöist  (sd.)  k}krp7m  damaysi  vauhuyäi yqm  Asi  'yqm''>  dälB  x/ayqs  mazdä  ahurB . .  äzdyäi  (sd.)  "den  .  ■  Leib  der  lieben (Jungfrau)  .  .,  welcher  der  Herrscher MAh.  es  gewähre  für  ihr  gutes  Ich  .  . zu  gelangen"  Y.5^.17;  —  hyat  *aS>ia>ihz dngvats  S»äna  °y}ng  avAayS  (sd.)  Y.js, 16.  a)  insbes,  von  'airyaman-  (sd.): il  airySmä  (sd.)  "yö  rafooräi  jatitü  Y.  ^4- 1;  V.  22.9,  19,  20,  a)  mit  'airyamati- (sd.,  auch  fdSt):  mryamamm  'slm  Vr,  2. 10;  usw.;  —  airyamattö  °ye/ie  Vr.  j.8;  usw.
11359:—  ahe  zl  nä  ..  aframannti  (sd.)  ästrydte yaha  gä^anqmat  N.22 ;  —  daivayasnoHbyS paurvS  ämayayanta  yaha  mazdayasnaH- byasät  V.  7. 37;  —  Aamah a  iStverz.) ya'ha paraat  Yt.  S- 65  usw.;  —  bei  negirtem Hauptsatz:  »Sij  masyS  ..  ao/if  {sd.)  maiti- yäe  duimat^m  ya'ha  mihrasHt  ..mainyäe kumatim  Yt  m,  106;  106';  —  nSit  mallm ..masya  /ia^aite(sd.)  äsnö  xratu/ya^a  mi- ^r»mät..Aacaite..Yl.io.iOT.  a)  wieder- holt 'sowohl  , .  als  auch,  nicht  nur  . . sondern  auch,  et  ..et.,  et ..,  cum.,  tum': vatjharsStascit  maytt}niasä( srSvaySi^Y.  12; zit  *N.  log^^i  —  raixtnä  aspSnili  sädrä- Ht  /axrq)i5(sd.)  Y.34.J ; — savAimat  *anu.- sasträi  sa^himHi  *anu.mainyäi  Yt  10. 137;  P.2Ö(?);  — fratar?mHt  ti  havamm vaüa   upa,staomi  . .  upanmcit  .  .  Y.  10.  3;
13700:•  j.  dürae-karana-  Adj.  'des  Enden  in der  Feme  liegen,  fembegrenzt":  asmati>m
19715:•  j.,  g.,  p.  'man-  V.  'denken',  Fraes.  i man-,  a6  mainya-,  maniya-,  30  (Iter.) mqnaya-,  s-Ko\.  i'>  mar?A-,  mfngh-;  Perf. I  mamati'-.mamn:  —  PPfP.  mata-,  PFP. 'mahiaa-.         S.  noch  zu  ^manao^rJ-.
25476:•  j.  irimant-  Adj.  (fem.  'maiti-)  'mit Unrat  angefüllt':  bagvan  mayanqm  'maiti- nam  .  .  aipi.ianyat  V.  14.  6.
27959:•  j.  zarannmaiti-  L  Naioe  etnes  Flusses**: trayS ya(  kasaim  . .  avi  tjm  arihaiUacatti .  .  'maHla  Ytiff.66L
=== grep 'mati-' anywhere ===
      2 mati-
      1 mati-.
```


## [2026-09-07T16:24:11.822Z] TOOL CALL #76: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/mansion\" \\\n \"https://www.etymonline.com/word/mount\" \\\n \"https://www.etymonline.com/word/prominent\" \\\n \"https://www.etymonline.com/word/mane\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%86%D8%AF%D9%86\" ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 333: Men2/Men3 chains (maneo, mons, -mineo, mane, mandan)' 2>&1 | tail -1; done"
}
```


### [2026-09-07T16:24:15.640Z] TOOL RESULT

```
### https://www.etymonline.com/word/mansion
/home/sfmqrb/git/rishe/data/verification/sources/web/defd8eb60069148e.txt
### https://www.etymonline.com/word/mount
/home/sfmqrb/git/rishe/data/verification/sources/web/9a25043bdcdeed3f.txt
### https://www.etymonline.com/word/prominent
/home/sfmqrb/git/rishe/data/verification/sources/web/01dcf1fcc98265b2.txt
### https://www.etymonline.com/word/mane
/home/sfmqrb/git/rishe/data/verification/sources/web/771d20575029b0c6.txt
### https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%86%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/ff6fd07203196bd5.txt
```


## [2026-09-07T16:24:19.167Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in defd8eb60069148e 9a25043bdcdeed3f 01dcf1fcc98265b2 771d20575029b0c6; do echo \"##### $f\"; grep -n -i \"PIE root\\|from PIE\\|Proto-Indo-European\" $f | head -6; done"
}
```


### [2026-09-07T16:24:20.486Z] TOOL RESULT

```
##### defd8eb60069148e
ugrep: warning: defd8eb60069148e: No such file or directory
##### 9a25043bdcdeed3f
ugrep: warning: 9a25043bdcdeed3f: No such file or directory
##### 01dcf1fcc98265b2
ugrep: warning: 01dcf1fcc98265b2: No such file or directory
##### 771d20575029b0c6
ugrep: warning: 771d20575029b0c6: No such file or directory
```


## [2026-09-07T16:24:23.740Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && ls -t | head -8; for f in defd8eb60069148e.txt 9a25043bdcdeed3f.txt; do echo \"##### $f\"; head -20 $f; done"
}
```


### [2026-09-07T16:24:24.909Z] TOOL RESULT

```
ff6fd07203196bd5.txt
index.jsonl
771d20575029b0c6.txt
01dcf1fcc98265b2.txt
9a25043bdcdeed3f.txt
defd8eb60069148e.txt
6d50b36ce1e29075.txt
43c6b1d75a0fa9d8.txt
##### defd8eb60069148e.txt
URL: https://www.etymonline.com/word/mansion
FETCHED: 2026-09-07T16:24:13Z
STATUS: 200
TITLE: Mansion - Etymology, Origin & Meaning

Mansion - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
##### 9a25043bdcdeed3f.txt
URL: https://www.etymonline.com/word/mount
FETCHED: 2026-09-07T16:24:13Z
STATUS: 200
TITLE: Mount - Etymology, Origin & Meaning

Mount - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
```


## [2026-09-07T16:24:28.602Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in defd8eb60069148e.txt 9a25043bdcdeed3f.txt 01dcf1fcc98265b2.txt 771d20575029b0c6.txt; do echo \"##### $f\"; grep -n \"root \\*men\\|\\*men-\\|\\*mon-\\|PIE\" $f | head -8; done"
}
```


### [2026-09-07T16:24:29.811Z] TOOL RESULT

```
##### defd8eb60069148e.txt
58: mid-14c., mansioun , "chief residence of a lord," from Old French mansion "stay, permanent abode, house, habitation, home; mansion; state, situation" (13c.), from Latin mansionem (nominative mansio ) "a staying, a remaining, night quarters, station," noun of action from past-participle stem of manere "to stay, abide" (from PIE root *men- (3) "to remain").
77: *men- 
##### 9a25043bdcdeed3f.txt
25: c. 1300, mounten , "to get up on a horse;" mid-14c., "to rise up, rise in amount, ascend; fly," from Old French monter "to go up, ascend, climb, mount," from Vulgar Latin *montare , from Latin mons (genitive montis ) "mountain" (from PIE root *men- (2) "to project"). The transitive meaning "to set or place in position" first recorded 1530s. Sense of "to get up on for purposes of copulation" is from 1590s. Meaning "prepare for presentation or exhibition" is by 1712. Military meaning "set up or post for defense" is by 1706; to mount an attack is by 1943. Related: Mounted ; mounting .
30: "mountain, lofty hill, elevation of land," late Old English, from Anglo-French mount , Old French mont "mountain;" also perhaps partly from Old English munt "mountain;" both the Old English and the French words from Latin montem (nominative mons ) "mountain," from PIE root *men- (2) "to stand out, project." "From the 17th c. in prose used chiefly of a more or less conical hill of moderate height rising from a plain; a hillock" [OED]. Archaic or poetic only by late 19c. except as part of a proper name. The Sermon on the Mount is in Matthew v-vii and Luke vi.
41: late 13c., "to go up, rise, mount (a horse)," from Old French amonter "rise, go up; mean, signify," from amont (adv.) "upward, uphill," literally "to the mountain" (12c.), a contraction of the prepositional phrase a mont , from a (from Latin ad "to;" see ad- ) + Latin montem (nominative mons ) "mountain" (from PIE root *men- (2) "to project").
57: *men- 
##### 01dcf1fcc98265b2.txt
25: mid-15c., "projecting, jutting out, standing out beyond the line or surface of something," from Latin prominentem (nominative prominens ) "prominent," present participle of prominere "jut or stand out, be prominent, overhang," from pro "before, forward" (see pro- ) + -minere "project, jut out," which is related to mons "hill" (from PIE root *men- (2) "to project").
36: *men- (2) 
48: Also in some cases from cognate Greek pro "before, in front of, sooner," which also was used in Greek as a prefix (as in problem ). Both the Latin and Greek words are from PIE *pro- (source also of Sanskrit pra- "before, forward, forth;" Gothic faura "before," Old English fore "before, for, on account of," fram "forward, from;" Old Irish roar "enough"), extended form of root *per- (1) "forward," hence "in front of, before, toward, near," etc.
74: mid-14c., from Old French excellent "outstanding, excellent," from Latin excellentem (nominative excellens) "towering, prominent...out from" (see ex-) + -cellere "rise high, tower," related to celsus "high, lofty, great," from PIE root *kel- (2) "to be prominent...
90: 1560s, "leaping," a heraldic term, from Latin salientem (nominative saliens), present participle of salire "to leap," from a PIE root of uncertain form (source also of Sanskrit sisarsi, sisrate "to flow, run, hurry;"Greek hallesthai "to leap," Middle Irish saltraim "I trample," M
94: "kingly, pertaining to a king," late 14c., from Old French regal "royal" (12c., Modern French réal) and directly from Latin regalis "royal, kingly; of or belonging to a king, worthy of a king," from rex (genitive regis) "king," from PIE root *reg- "move in a straight line," with 
##### 771d20575029b0c6.txt
25: "growth of long hair on the back of the neck and shoulders," characteristic of the horse, lion, and some other animals, Old English manu "mane of a horse," from Proto-Germanic *mano , from PIE *mon- "neck, nape of the neck" (source also of Sanskrit manya "nape of the neck," Old English mene "necklace," Latin monile "necklace," Welsh mwng "mane," Old Church Slavonic monisto , Old Irish muin "neck").
35: also manilio , "metal (usually copper) ring or arm-bracelet sold or bartered by European traders among African peoples," 1550s, from Spanish manilla , from Latin monilia , plural of monile "collar, necklace," from PIE *mon- "neck, nape of the neck" (source also of mane ). Influenced in Spanish by Spanish mano "hand."
63: mid-15c., humain, humaigne, "human," from Old French humain, umain (adj.) "of or belonging to man" (12c.), from Latin humanus "of man, human," also "humane, philanthropic, kind, gentle, polite; learned, refined, civilized." This is in part from PIE *(dh)ghomon-, literally "earthl
71: Old English hær "hair, a hair," from Proto-Germanic *hēran (source also of Old Saxon, Old Norse, Old High German har, Old Frisian her, Dutch and German haar "hair"), perhaps from PIE *ghers- "to stand out, to bristle, rise to a point" (source also of Lithuanian šerys "bristle;" s
```


## [2026-09-07T16:24:36.726Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Middle Persian\\|Proto-Iranian\\|Proto-Indo-European\\|Etymology\" ff6fd07203196bd5.txt | sed -n '1,25p'; echo \"---\"; sed -n '/Inherited from Middle Persian/,+4p' ff6fd07203196bd5.txt | head -12"
}
```


### [2026-09-07T16:24:38.278Z] TOOL RESULT

```
65: Etymology 
172: Etymology
175: Inherited from Middle Persian KTLWNtn' ( māndan ) , KTLWN ( mān- ) , from Old Persian , from Proto-Iranian *(d)mān- ( “ to remain, dwell ” ) , from Proto-Indo-European *men- ( “ to stay, stand still ” ) , related to Latin maneō ( “ to remain ” ) , Ancient Greek μένω ( ménō , “ to remain ” ) .
859: Categories : Persian terms inherited from Middle Persian 
860: Persian terms derived from Middle Persian 
862: Persian terms derived from Proto-Iranian 
863: Persian terms derived from Proto-Indo-European 
---
 Inherited from Middle Persian KTLWNtn' ( māndan ) , KTLWN ( mān- ) , from Old Persian , from Proto-Iranian *(d)mān- ( “ to remain, dwell ” ) , from Proto-Indo-European *men- ( “ to stay, stand still ” ) , related to Latin maneō ( “ to remain ” ) , Ancient Greek μένω ( ménō , “ to remain ” ) .

 Pronunciation
 [ edit ]
```


## [2026-09-07T16:24:46.051Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"ماندن\" ARY_pages.txt | head -5; echo \"=== امید ===\"; grep -n \"^امید\\|امید \" ARY_pages.txt | head -5; echo \"=== latin index men ===\"; grep -n -i \"MANEO\\|MEN-\\|MONO\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T16:24:46.122Z] TOOL RESULT

```
11659:چم این واژه در زبان‌های ژرمنی و زبان تخاری: ماندن» بجا ماندن؛ رفتن,
=== امید ===
36:امیدوارم که این کتاب دوست‌داران زبان پارسی و زبانشناسی را خوش آید.
1253:شدکم نیست. پژوهشهای پیشاهنگانه معمولاً هم راهگشا هستند و هم محتمل به داشتن لغزش. امید من
1264:نبوده‌ام با بکار بردن «شاید؛ در جلو واژه به خواننده هشدار داده‌ام. امید غایی من این است که دراین 8
1341:امید برای پژوهشهای آینده :
1345:امید من این است که پژوهشگران دیگر به تدریج کاستی‌ها را برطرف کرده و فرهنگه‌های کاملتری از
=== latin index men ===
13460:‘MANEO, MANERE LATIN) oS
15642:rrvr tab obey AMEN, AMEN-AIN (GREEK) (gly
```


## [2026-09-07T16:24:49.372Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '13450,13470p' ARY_latin_index_pages.txt; echo \"=== ماندن context ===\"; sed -n '11648,11672p' ARY_pages.txt"
}
```


### [2026-09-07T16:24:49.427Z] TOOL RESULT

```
MAN., MANDAN, MANISTAN
"REFERENCES eat MAIN, MANDU (KURDISH) 62,
| Troromm OOS~C~SD MANTA, MANAGH (BALUCHD 23h
BARNHART: (MANSION) 631 MANDA AFGHAND) (5-4) is!
MACKENZIE: MASK :(TOKHARIAN A) A 655
(REMAIN) 130, (STAY) 134 MASK {(TOKHARIAN B) B 5 55
BUCK: 838 (SANSKRIT) 3 Sle
ONIONS: (MANSION) 533 MAN., MAMANDBT
SKEAT: (REMAIN) 509 MNAM, MUNAL — :(ARMENIAN) 4
140s seb oby ‘MENO, MENEIN GREER) lip,
‘MANEO, MANERE LATIN) oS
[pdf page 462]
|
FY | Cyd po 4) ole
i HOLD CHURCH SLAVIC) oS 3%! AVESTAN) ply!
| MEsect - MAWNGH, MA, MAH.
MEsic (CZECH) Se MAH HOLD PERSIAN) joel gs),
| MJESIC (SERBIAN) 9 po MAH (PAHLAVI) 5 shy,
MESIC (BOHEMIAN) gus y MEH KURDISH) (53,5
MESIAC (SLOVAK) $1 U1 -MEY 4AFGHANI) (3.4) gli!
(LITHUANIAN) gl 3 MAN x(TOKHARIAN A) A 5 ,\55
=== ماندن context ===

نروژق ان 17 ۹

یادداشت: 1 ۰

۱- واژه‌ی انگلیسی 11۷13 نیز از همین واجربشه است: انگلیسی کهن: ۳.131۸۷ فریزی کهن: 1318۸ن1؛ ساکسونی

کهن: 11881۸3 هلندی: 1.2۷87 آلمانی کهن: 188500 ایسلندی کهن: 11۳۸ گوتبک: 128۸۷

۲ چم این واژه در زبان لاتین: دارای چشم تارء

چم این واژه در زبان‌های ژرمنی و زبان تخاری: ماندن» بجا ماندن؛ رفتن,

چم این واژه در زبان آلبانی و هتیت: کلیف (کردن).

چم این واژه در زبان لیتوانی و لتونی؛ پیروی کردن» رهبری کردن.
[pdf page 393]
۴ | فه فیه (به چم *پارو" و *سکان")
چم این واژه در زبان یونانی: چربی,
اد
سانسکریت (84(798/7): دون هلندی (ل007): - 87۸۸
بونانی (07874): اسلاری کهن (۲/0اشا5 تل#ناتل صتم):
5 ,5۳۸7715 ,ال8775 زال‌ران
لاتین (7100مل): 500۸ ایرلندی کهن (للکنها صام): 500
ایسلندی کهن (/(1۸۷۸1۵ یه صام).
```


## [2026-09-07T16:24:58.454Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk 'NR<=13460 && /\\[pdf page/ {p=$0} END{}' ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<13460' | tail -2; echo \"=== also find ARY_pages entry for man- ===\"; grep -n \"MANDAN\\|MANISTAN\" ARY_pages.txt | head -5"
}
```


### [2026-09-07T16:24:59.787Z] TOOL RESULT

```
13402:[pdf page 460]
13434:[pdf page 461]
=== also find ARY_pages entry for man- ===
```


## [2026-09-07T16:25:07.470Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN remain ===\"; grep -n \"12.15 REMAIN\\|REMAIN, STAY\\|^12\\.15\" SYN.txt | head -5; echo \"=== SYN mountain ===\"; grep -n \"MOUNTAIN, HILL\\|1\\.22 MOUNTAIN\" SYN.txt | head -5; echo \"=== SYN neck ===\"; grep -n \"NECK$\\|4\\.28 NECK\\|NECK, NAPE\" SYN.txt | head -5; echo \"=== SYN hope ===\"; grep -n \"16\\.6[0-9] HOPE\\|HOPE$\" SYN.txt | head -5"
}
```


### [2026-09-07T16:25:08.726Z] TOOL RESULT

```
=== SYN remain ===
21316:12.15 STAND (vb. intr.)
21331:12.16 REMAIN, STAY, WAIT
=== SYN mountain ===
=== SYN neck ===
6001:a 4.28 NECK NG ath? T#AxvAos, Bion Goth. als Lith. kaklas Lat. ob ON _hals, sviri Lett.  kakls ee colla Dan. _hals ChSl. vyja, Sia coy Sw. hals SCr. _ vrat (Sija) Sp. cuello OE heals, sweora Boh.  fkrk, sje om git Ms hals, swere, necke Pol. — szyja, kark I, = A D ve a faa ae Du. hals ar reel kantha-
=== SYN hope ===
29310:16.63 HOPE (sb.)
```


## [2026-09-07T16:25:12.750Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21331,21395p' SYN.txt | grep -n -i \"maneo\\|Av\\. man\\|Pers\\|men-\\|remain\" | head -15; echo \"###### hope\"; sed -n '29310,29400p' SYN.txt | grep -n -i \"Pers\\.\\|umed\\|umid\\|Av\\.\" | head -10"
}
```


### [2026-09-07T16:25:12.820Z] TOOL RESULT

```
1:12.16 REMAIN, STAY, WAIT
8:Rum. _ rédminea, aslepia NE remain, slay, wait Av. man-
13:Words for ‘remain, stay’ (in one place as opposed to ‘move, go’) coincide in part with those for ‘remain’ = ‘be left over’ (12.17), the development being mostly from the first to the second, but sometimes the opposite. Furthermore, just as words for ‘remain’ may be used for ‘await, wait for’ (as Grk. pévw Hom. Il. 16.620, etc., Lat. manére hostem, OPers. mam amdanaya ‘awaited me’), so conversely there is a group of words which, from such notions as ‘watch, look for, hope for’, have come to mean ‘wait for’ and may then be used also intransi- tively for ‘wait’ closely approaching ‘re- main, stay’. Hence such words are added in the list, even though most of them are still distinguished in feeling and range of use from those given in the first place.
14:1, IE *men- ‘remain’, to be distin- guished from *men- ‘think’, even though they may be ultimately the same. Walde-P. 2.267. Ernout-M. 587. Walde-H. 2.26.
15:Grk. pévw, also pluvw poet.; Lat. manere; AV. man- in upa-manaya- ‘wait for’, mdnaya- ‘cause to remain’, OPers. manaya- ‘wait for’, NPers. mandan ‘re- main’, Skt. man- in Ved, imperat. ma- mandhi ‘delay’; Arm. mnam ‘remain, wait for’; here prob. Ir. ainmne, W. an- mynedd ‘patience’ (cf. Grk. bro-novy ‘pa- tience’).
17:2. It. restare, Fr. rester (latter with -3- from the It. or Lat. form), fr. Lat. restare ‘stand firm, remain = be left’, epd. of stare ‘stand’. REW 7248. Gamillscheg 759 f.
18:It. rimanere, Rum. réminea, OFr. re- maindre (> ME remayne, NE remain), fr. Lat. remanére ‘be left’ (epd. of manére, above, 1).
24:Ir. anaim, NIr. fanaim : Skt. anil ‘breathes’, ete., IE *an- in words for ‘breathe, breath’ (4.51), with semantic development through ‘breathe hard, pant?(?) to ‘rest’, or possibly a blend with forms of IE *men- (above, 1):
28:con 2.456. Thur- Airaphs ‘persisting’, etc. The Gme. de- p, 1.0! ie out-M. 587. velopment through ‘remain stuck’.
35:ME remayne, NE remain, see above, 2.
47:4, Goth. saljan, eurrences ‘remain, abide’ = ‘have an
64:12.17 REMAIN (= Be Left Over)
65:Grk. —elropar Goth. aflifnan Lith. i8likti, pasiliki NG pew ON lifa, lifna Lett. atlikt Lat. _relinqui (remanére, Dan. _ Dlive tilovers (tilbage) ChSl.  ostati restare) Sw. bliva évrig (kvar) SCr. _ ostati It. rimanere, restare Or belifan, lefan Boh. —ztistati Fr. rester ME leve, remayne Pol. zostaé Sp. reslar, quedar NE be lefi, remain Russ. ostat'sja Rum, rdminea Du. blijven Skt: ¢ig- in pass. Ir. do-fuarat, fedligedar OHG biliban (8sg.) MHG beliben Nir. fanaim NHG bleiben W. bod yn weddill Br. chom
###### hope
8:Nir.  dichas, sil OHG  gedingi, wan Av. vyabra-
36:Av. vyaéra-, etym.? Barth. 1475 f.
82:ork. maT Os ON tryggr, trar Lett.  uzticigs NG oT OS jfaltis Dan. fro Ch&l.  vérinit iat. ad ‘eale Sw. trogen SCr.  ujeran tt ie 2) ical OE getriewe, tréowe Boh. _vérny pr. (ide i i ME _trewe, faithful Pol. wierny gp. Le 08 statornic NE faithful, loyal (true) Russ. vernyj Rum. creat a : Du. = trouw Skt.  bhakta- Ir hie OHG  gitriwwi Av. — aradra- NIr. ae _ MHG  getriuwe, triuwe W. de leal NHG lreu, getreu Br. ’
87:4. Goth. triggws, ON tryggr (Dan. tryg, Sw. trygg ‘safe’), OE getriewe, tréo- we, ME trewe, NE true (now mostly arch. in this sense), OS triuwi, Du. trouw, OHG gitriuwi, MHG getriuwe, late triu(we), NHG treu, getreu, Gme. *trew- wi- beside *trawia- in ON frir, Dan., Sw. tro (Sw. now only religious ‘believ- ing’; for general sense trogen, deriv. of vb. tro ‘believe’, cf. Hellquist 1008) : OPruss. druwis ‘belief, faith’, druwtt ‘believe’, Lith. driutas ‘strong, firm’, ChSIl. si-dravit ‘well, sound’, Skt. dhruva- Av. drva-, OPers. duruva- ‘firm, sound, secure’, Ir. derb ‘certain’, dron ‘firm’, all ultimately, with notion of ‘firm’, con- nected with words for ‘oak’ and ‘tree’. Walde-P. 1.804 ff. Falk-Torp 1284f., 1290.
```


## [2026-09-07T16:25:22.418Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -3; grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | tail -3"
}
```


### [2026-09-07T16:25:22.480Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-07T16:25:26.850Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -c \"\" WLD_Bd2_pages.txt; python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('blocks',len(pages))\n# find page containing 'mono-' neck or 'men-' remain\nimport re\nfor i,p in enumerate(pages):\n    if 'mane' in p and 'monile' in p:\n        print('---',i, p[:300])\nEOF"
}
```


### [2026-09-07T16:25:28.098Z] TOOL RESULT

```
47596
blocks 725
```


## [2026-09-07T16:25:32.361Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor kw in ['monile','maneö','maneo','mqnaya','mänistan','manaoöri','manao']:\n    hits=[i for i,p in enumerate(pages) if kw in p]\n    print(kw, hits[:8])\nEOF"
}
```


### [2026-09-07T16:25:33.875Z] TOOL RESULT

```
monile [299, 309]
maneö []
maneo [271]
mqnaya []
mänistan []
manaoöri []
manao [309]
```


## [2026-09-07T16:25:37.344Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (271,299,309):\n    print('#########',i)\n    print(pages[i][:2600])\nEOF"
}
```


### [2026-09-07T16:25:38.626Z] TOOL RESULT

```
######### 271
                                                      meu           mem-                                           267

und mit Diss, wahrscheinlich att. ^dvavoog „(*wer sich abseits, von andern
fernhalt^ =) .,der kleine Mann mit beschranktem Gresichtskreis"'; o-stufig
jon. jLiovvog, dor, jucovogy att. /xovog         Kretschmer KZ. 31,444);
kaum osk. menvtm ^,minuere'^ (Bugge aaO wohl mit nachlassigem e fiir i       ;



zu lat. mimio, v. Planta I 190, Buck Gr. 35); air. menb „klein‘', 'ihenhacli
„Teilchen‘‘ (von Pedersen KG. I 64 freilich aus ^mhmo- erklart; 2i\tMenueli,
aber kaum g. sg. eines Prauennamens Merib, Thurneysen KZ. 37, 114 Anm. 1),
cymr. di-femvi „verkleinern, schmahen^' (Rhys, s. Stokes KZ. 38, 468).
  Nicht hierher ir. mann ,.Unze^^ Oorm. (Pick II ^ 208); mit ir. menh wiirde
sich     ags.    minn „klein,             gering,      minne „klein, gering,
                                                           niedrig^',       nd. minyi,
mager, kranklich“ decken (Pick III ^ 3   0, Palk-Torp   u, mangel^ die auch
                                                                      1



ahd. mtmhva^ ags. myn{iv)a „Elritze“     doch s. auch u.          —
                                                                „Pischname''
—   anreihen), aber eher rich tiger zu got. usw. mlnniza „minor“ gehoreii,
s. mei- „mindern‘‘. Lit. mindu „durchaus, ja“ (Pick I^ 519) bleibt fern; des-
gleichen nhd. nd. man „nur“ (s. Palk-Torp u. yneii m. Lit.).
     Mit g-Pormans;        ai. mandk „ein wenig“ (aber uber maioku- „schwach,

schwankend''          meng- „kneten“); tochar. B. menki „minder, geringeP^
                       s.   u.
(Levi“Meillet Journ. as. 1912,1 112); lit. menkas „gering“; ahd. mengen
{^mangjan) und mangolon „entbehren'', nhd. mangcln, mhd. mane (-^-)
„Mangel, Gebrechen“ (aber lat. manens bleibt fern, s. u. menq- „kneten‘0-
   S. Pick II ^ 208, III * 309, 310, Vf. LEWb.^ u. mancus, Meillet rad. men- 9
ziir Scheidung von men- „treten‘‘ und menq- „kneten‘' s. unter letzterem.



5.   men- „bleiben, stillestehm' {—men „denken'^ s, u.).
     Ai.man- {jmrimamandh}, dmaman) „zogern, stillestehn^,                                          av. ap.       man-
„bleiben,        warten^^,       av.     fra-man- „ausharren‘^:                   arm,     nmam (Hiibschmann
Arm. St. I 43, Arm. Gr. I 475)                             ,
                                                               bleibe,     erwarte“               vgl.    von men-
jjdenken^       avd- usw.) gr. yevcoj /djnvco (jisyevrixo) „bleibe ‘'5 j^iovri „das
                 gr.    
######### 299
                                    mela^dh-                                     295

blat,  as. blad „Blatt'' (diese untereinander von Frohde BB. 7, 326 ver-
bunden) moglich erscheinen; doch hat letzteres bei der Sippe von Blume,
lat. fids zu verbleiben (s. Wz.          und enthalt das o von fMort] eine
ernste formale Schwierigkeit (die allerdings bei Anknltpfung an flcod'Qog,
s. u, vermieden ^viirde).

   Sehr unsicher nur sind anzureihen („hervorkomnien, sichtbarwerden              —
Erhohung^'?) alb. maV .,Berg, Gebirge‘‘, maje „Spitze, Gipfel“ (aus
Oder als monia zu men- „ragen“? s. G. Meyer Alb. Wb. 255, 257), lett.
mala „(erh6hter) Rand, Ufer^^ {mele ,,Zunge‘'?? s. Berneker II 72, 74), ir.
mala, acc.-pl. mailgea ,,Augenwimper‘'‘ (ibd. Pick II * 203, Pedersen KG.
II 99), ir. mell (f^mel-no ~) „globus,- locus editus collis‘‘   (B. bei Pick
II ^ 215 zw., Liden Stud. 89; die Sippe jnd?.a, lat. ymiltiis usw. steht fiir
sich), womit Petersson (Stud, zu Fort. Reg. 23 f. (Lit.), 73 f., wohl richtig
ai. maw- ,,Perle“ (dies nach Windisch KZ. 27, 16S; andere Deutungen bei

Bezz. BB. 27, 17 J, Pedersen KZ. 36, 92, s. dagegen Vf. LEWb.^ u. monlle),
manilca- ru. „(*bauschig runder) groBer Wassertopf", malla- m., in der
Bed. „Trinkgefa6, Ge^6 iiberhaupt^ und „Wasyr^ verbindet (auch "^manda-
„Kreis, rund“ als Gdlage von mdndala- „rund^‘            —
                                                    dies mit ir. mdl bereits
von Zupitza KZ. 36, 65 verkniipft      —  mnndapa- m. n. „IIaIIe, Tempel,
                                           ,


Laube'*, und zweifelhafteres).    Diese ganze Gruppe mit dem Bed.-Kem
.AVolbung, rundliches“ ist wohl als selbstandige Sippe von mela „hervor-
kommen“ abzurucken; weitere Beziehung zu mel-gili)- „schweilen“ und
ynel- „stark, gro6''unter einer Gdbed. „schwellen“ (Petersson LUA. 1916,
S4)  und zu meladh „Erhohung, Kopf' (ebda.) ist ganz fraglich.
  mani- gewifi nicht zu lat. monile (s. "^mono- „Nacken, Hals“); aus aram,
man laBt es Halevy Msl. 11, SI entlehnt sein.
  Wenn der Wz. ‘'^melci auch diese Bed. „hochkomnien, Erhohung^* zuzu-
billigen ist, kann als rf/^-Erweiterung zu ihr gelten:



mela^dh- (gnohdh-,    niohdli-} „Erhohung, Kopf^ (vgl. zum dli die Sippen
      von ai. urdhvd' „hoch** und anord. qrdugr „steil“?).
   Ai. rnrirdhan- m. „Kopf',     av. Jca-m9r9da- ,,Kopf daevischer Wesen“
^'eigentlich „was fur ein KopP Bartholomae IF. 5, 224, Altiran. Wb. 440),
ags. ynolda „the top of the head'', afries. meldke {^middi-lcD, Holthausen
IF. 32, 333) „KopP, gr. fXco&gog (Gdf, ^mlodh-ros oder ^mohdhros mft
sog. J) ,.hoch au
######### 309
                                           modhro* oder madhro       mondo-s                              305

glichen werden, auf eine idg, w-Wz. zuriick. Grundsatzlich moglicli                                        ist

Vereinigung unter idg. moud-: mUd und mo\ti\d-: mod-,

modhro- oder madhro- „blau; Farberpflanze'*^?
  Isl. madra „galium verum^^, isl. livlt-, krosS'-niadrausw. ^Galium bor-
eale, glatte Wiesenrote“, ahd.  matara ^Farberrote^^, ags. mcede^'e, mceddre
ds.  Slav. modr% (z. B. cech. modry) y,blau“?
      :




   Berneker II 66f. zw., mit Lit. iiber abw. Deutungen von modi^; von
diesen ware die Verbindung mit gi\ juddgva n. pi. „Schleben‘'^ mit obigem
vereinbar, wenn dieses der Entlehnung verdacbtige Wort speziell aus dem
Norden der Balkanhalbinsel (Media fiir Media aspirata, a ursprgl. oder
illyr.     fiir   o)   stammte.

mono- „Nacken,                 Hais“, in Ableitungen              (bes.   m. Formans   -7,       -jo-)   auch
          jJIalskette,        Halsschmuck“,
     Ai. mdnya j.HackeA' (aber mani- „Perle“, nicht ^jHalskette'', bleibt fern,
s.   Vf. LEWb.'*^ u. monile,      und u, Wz. mela- „hervorkommen“) av. minii-                ;


„Halsgescbmeide''            aus avest. 9, vgl. Bartholomae IF. 3, 172; airan. Wb.
                                {i

1186, wo          gegen assyr. Ursprung), und mit Hochstufe der w-Formans (Char-
pentier KZ. 43, 165), manao^rl „irala, ^N^acken*^ (zur Bed. s. Bartholomae
IF. 19, Beitr. 205 f.); paon. yov-aTio^ „Wisent'' (Berneker II 76); gall.-gr.
                 juavvdyuov j.Halsband keltischer Yolker“ {juovvog dorisch?
fiavidTcrjg, judvvog,
s. G. Meyer Alb. Wb. 257 f.); lat. monile ,,Halsband als Schmuck; Mahne^'
(von       wie abg. moni-sto, Hirt 31, 11; zur Bed. vgl. ai. grlvci „Nacken*':
abg. griva                           :    grivhna „Halsband‘');    air.   muin- „Hals“   in        miiintorc
,,Halskette“, mulnel „Hals'', cymr. mion.mivnivgl                              dJiv^formnae (Zimmer
CZ. I 92 Anm.)                             formell = cymr. gor-fynydd „Auf-
                             ,,Schulter“ {^for-monjo-,
stieg“) ; air. muince ,xollarium“,acymr. mind „monile'‘ (Zweifel bei Peder-
sen KG. I 33, der Zs. von cymr. mwng^ s. u., mit dem 2. Gliede von bret.
mor-go „Collier de chevaP' und Entlehnung des ir. Wortes aus dem brit.
erwagt); die kelt. Worte nach Zimmer KZ. 24, 210, Pick II^ 216. Aisl.
men^ ags. mene, ahd. menni „Halsgeschmeide“, aisl. mow, ags. mami^ ahd.
mana „Mahne''. Abg, monisto (s. o) „Halsband^‘ (slov. mcnina „()hrge-
schmeide” Lw. aus ahd. menniX). Mit form
```


## [2026-09-07T16:25:53.096Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[267][:2500])\nEOF"
}
```


### [2026-09-07T16:25:54.370Z] TOOL RESULT

```
                                                men         men-                                  263

    1. men-    „emporragen“.
       Av. framanyente ,,sie gewinnen Yorsprung“, mail- „Vorspmng des Ge-
    birges“        pro-miner e\ Bartholomae Airan. Wb. 1112, 1125); sehr frag-
    lich gr. juovoa {^montla „*Bergnymphe“?? Wackernagel KZ. 33, 571 ff.;
    s. u. ^mendh- „seinen Sian worauf richten*'); desgleichen alb.       „Spitze,
    Gipfek^ (^moyiial. eher wegen maV „Ber8‘“ aus "^maV      s. u. meJo- hervor-

kommen'' and G. Meyer Alb. Wb. 255, 257, Alb. St. Ill 63); lat. emineo,
-ere „heraus-,  hervorragen^ mminlre „drohend liber etwas hereinragen“,
prominere ,,hervorragen‘^; aus diesen Zs. ist wohl                    —
                                                      unter Mitwirkung rein
lantlicher Anlebnung an minor „kleiner'* — auch das i folgender Worte
zu erklaren: minae ,,die hervorragenden Zinnen (murorum); Drohungen^^
minor -arl ,,einporragen, iiberragen, droben'^, minCix „ragend, iiberragend,
           ^

drobend'* (s. Vf. LE\Yb - s. v. minae moenia wiirde nur der Bed. ,,Zinnen‘'
                                            ;
                                                        :




unmittelbar geniigen; lett. mlna „Stufe'‘, Fick 513, gebort zu nu n- „treten'%
das gegen Fick aaO. BB. 28, 104 Persson Beitr. 562 von men „emporragen,
zu wirken'O      ;   mans,   -tis „Berg‘'       (in die /-Dekl. ubergefiibrfces   ^monios^   s.   zu-
letzt      Brugmann IP 2, 410);             „hervorragende Ecke“ mentnm
                                          verniutlicb        als
„Kinn, Gebaudevorsprung‘‘, mit cymr. mant „Kinnlade, Mund“ als "^mnto-
gleicbsetzbar (daraus mir. mant ,,die Stelle eines ausgefallenen Zabnes,
Zahnfieiscb“; Zupitza BB. 25, 94 Anm. 3, Pedersen KG. I 24) vielleicht
aucb mentida „penis'' (s. Yf. LEWb.^ s. v. m. Lit.) abret. -monid^ umge-
                                                                       ;


lautet       mijnydd^ corn, meneth^ hret. menc 0 „Berg^‘ {"^moniio-^ Fick II ^
210, Pedersen KG. I 33; letzterer legt kaum ricbtig die Bed. „Hals“ zu-
grunde — s. mo^is- ..Kacken, Hals''                     —
                                        nach ).6q^og ,,Kacken" und „Hugel"),
cymr. (jor-fynydd „Aufstieg" (formell = air. formna ,,Scbulter“, Pedersen
KG. II 12); aisl.       „DacbfirsP (debnstufig neben kelt. ^mdniio-). mma
..emporragen" (Persson KZ. 33, 292).
  S. Vf. LEWb.^ s. Yv.; verwandt ist wahrscbei
```


## [2026-09-07T16:26:04.779Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^• \" BRT.txt | awk -F: '$1>19690 && $1<19790' | cut -c1-140"
}
```


### [2026-09-07T16:26:06.046Z] TOOL RESULT

```
19691:•  j.  mat.ditnan-  Adj.  'sammt  seinen  Ge- schöpfen, seiner  Schöpfung':  hamistayatca . .  angrake  *mainySul  °manS  duidäm
19693:•  j,  mat.-paiti.p9r38av-  Adj.  (fem.  °S7'T-) 'mit  den  .^tworten*'  versehen,  sammt  den Antworten':  yasmm  .  .  haptar»h�
19696:•  j,  mat-paiti.frasa-  Adj,  (fem,  'sa-)  'mit den  Antworten  versehen,  sammt  den  Ant- worten': gä'hi  .  .  'sa  Y.57,  8.
19698:•  j.  matp^rasav-  Adj.  (fem.  'svf-)  'mit den  Fragen  *'  versehen,  sammt  den  Fragen' : yasmm  . .  haptarahaittm  . .  'sUm
19707:•  j.  inat.va£astaätay-  Adj.  'sammt  den StropbeD,  mit  allen  Stiophea':  yastam  . . haptaahäitlm  .  ,  mai.a/smamfn  *flm
19709:•  ]•  matraO«-  Adj.  'sammt  den  Wagen': karivars  yal  :fanira%>m  mat.ßum  •%>m H.J.14.
19711:•  j.  mat-saofLbuye  Inf.  'immerBammend zu  werden,  semper  infiammari':  saoH.buye .  .  m'  ahmya  nmätu  Y.  62,  3.
19714:•  j.  maabäna-  Adj.,  Pj-AorM.:  s.  'man-.
19715:•  j.,  g.,  p.  'man-  V.  'denken',  Fraes.  i man-,  a6  mainya-,  maniya-,  30  (Iter.) mqnaya-,  s-Ko\.  i'>  mar?A-,  mfngh-;
19741:•  i*i  E-i  P-  "nian-  V.  'bleiben;  warten'. Praes.17  flM»)'a.,3o(Iter.,Kaus.)MdUni>tf-, mqnaya-.  —  AbsoL  •maittm.
19752:•  j.  3man-  V,,  nur  mit  frä  'Vorsprung gewinnen'.     Piaes.  27  manya-.
19756:•  j.,  g.  'mana-  n.  1)  'Masse,  Art  und Weise':  ia^a  zaota  (sd.)  g^a  Jrasräva- yäitii . .  tard^uifri  'na  li.33;  —
19758:•  j.  'mana-  m,  'Sinn,  WiUe',  sva.  manaA-. KompE.  —  Zorn  V.  ■'man-.
19759:•  g.  'manaodri-  f.  'Gemahnerin  an  — ' (Gen.),  mit  Akk.:  u^  arJm.p&wa(sd.)  x/a- pa^a  yä  °5/l/(NP.)  catdBnghaanbm  a
19761:•  j.  'manaoSri-  £  'Hals,  Nacken',  uzw. a^anscher  Wesen'' :  "an"  F.  jg;  —  minum barat..ar3dvlsära..upa  tarn  srJrqm'
19763:•  i.puxhm'^Taaxian'toä  nsit payaahff'ü.öj. Pö.:  mid.
19765:•  j.  mana-vantay-  f.  -  ?  - :  mßjfvm  . .  ys *raInaol'  daße  ma/^anam  yahmai  raiitu/ dar?yäi  hax^rai  frabavara  'vain
19767:•  j.  manas.paoirya-  Adj.  'der  eiste  im Denken'(?)'':  ii,a  dtm  para.HnasH  yim ahurim  .  ,  'ya^yB  damabyö  Y.  ig.it;  �
19770:•  j.,  g.  "manah-  n.  'der  innere  Sinn,  Geist" als  Sitz  des  Denkens,  Erkennens  und Wollens;  'Sinn,  Geist;  Denken,  Ged
```


## [2026-09-07T16:26:19.114Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Vorsprung\" BRT.txt | cut -c1-200; echo \"=== headwords mai around ===\"; grep -n \"^• \" BRT.txt | awk -F: '$1>19550 && $1<19695' | cut -c1-90"
}
```


### [2026-09-07T16:26:20.335Z] TOOL RESULT

```
4786:vaams  tisit  framanyents  "laufend  kommen sie  (nämL  mthrSjlrujB)  nicht  vom  Fleck, reitend    machen    sie    keinen   Fortschritt/, fahrend  gewmnen   sie  keinen  Vorsprung" Yt  jo.ao. 
17718:Zum  V.  iman- ;  eig.  'Hervorr^en,  Vorsprung'. —  Vgl.  gall.  'Ep-iiirm  {Ipt;;  ?),  alb.  maji 'Spitie';  s.  dazu  Fick  Wb.4  i.  310,  Peksson KZ.  ^3,  29a.  —  Pü.:  «  ne  ki  
19752:•  j.  3man-  V,,  nur  mit  frä  'Vorsprung gewinnen'.     Piaes.  27  manya-.
=== headwords mai around ===
19551:•  j.  maxäl-  f.  'Fliege':  druxs  yä  nasus  .. nivSiryete  mqnaym  ahe  >fl5
19553:•  j.  *niaxäi.V«hrp-"  f  'Fliegengestalt':  a^a druxs  ya  nasus  upa.dvqtaiti
19555:•  j.  maxäi.b3r«ta-  Adj.  'von  Riegen  ver- tragen, fortgeschleppt':  '0  nas
19557:•  j.  maxätay-  m.  EN.  eines  Gläubigen: sps.pt&ü  °Uis  alaonB  "des  Sp.,
19559:•  p.  maäya-  Adj.,  bezeichnet  ein  Volk'*: ima  dahySvJ'  fyä  adam  agarbä
19562:•  j.  C,  g.)  mata-  Adj.,  PPfP. :  s.  'mu;/-.  [P. 25:  lies  humata^
19564:•  j.  'matay-  f.  'Denken*.  [P,  25:  lies ar?m.maiti;  —  ^.41:  lies  /arS.
19566:•  j.  »■''matay-''  m.  'Vorspning  (des  Gebirgs), promunturium':  aofistimca
19576:•  j.  "maite  *>  F.  6.
19578:•  j.  'mad-  V.  'sich  berauschen'.  Fraes.  2 ma^a-,  24  mahaya-.  —  PPfP. 
19581:•  j.  ^mad-  V.  'zumessen'.    x-Aor,  i  mas-. 'zumessen,  zuteilen':  asakya  
19584:•  j.  ^mad-   Adj.  'sich  berauschend,   be-
19588:•  j.  tnaSaxa-  m.,  'xä-  f.  Ileuschrecke', ein  i/dA^sches  Tier:  ti  sUnS  
19592:•  j.  iiiaSav  n.  '(Wein  uzw.)  Beerenwein'  '* : gqm^a  ..yaom?a  . .  ''iula 
19602:•  j.  matvmsin  Adr.:  s.  ma^fma-.
19603:•  j.  maSsmö.nmäna-  n.  "mittleres  Haus, Haus  von  mittlerer  Grösse':  /ra
19605:•  j.  maiSim  Adv.:  s.  ^mathya-.
19607:•  j.iiia9u'inant- Adj.'Met,  Wein  enthaltend' : myazihm  (sd.)  .  .  gaomjntsm 
19610:•  j.  madamya  Adv.:  s.  mahmya-.
19611:•  j.  maJmya-,  maSsmya-  Adj.  'der  in der  Mitte  befindliche,  mittlere';  a)
19623:•  j.  'maiÜya-''  i)  Adj.  (fem.  'yä-)  'raedius' zeitlich;  in  "partitivem
19633:•  j.  'maiSya-  n.  'geistiges,  alkoholisches Getränk':  yni  .  .  'lyanqm  pa
19635:•  p.  pasävc^  adam  karam  "madyakä'Hivä avakanam  Bh.  /,  1 8 :  —  ?  �
19637:•  j.  maidyii  Adv,:  s.  'maitya-.
19638:•  j.  maiJtyäna-,  maiSyi^ia-  n.  'Mitte'; a)  des  Leibes,   a)  des  Menschen
19644:•  j.  maiSyÜrya-  m.  Name  der  Gottheit der  fünften  J^eszeit  und  des  an 
19647:•  j.  maiSyöi  Adv.:  s.  'mathya-, KompA.   —    S.  auch  maüyäirya-.  —
19648:•  j.  (3.)matJyöi.paitiStiina-  Adj.  'bis  zur Mitte  des  Beins  reichend,  so
19650:•  g.  maidyoi.maoha-,  j.  '^maitlyöL- maDlia-*>in.£N.zweierGläubiger:  i)  'h
19656:•  j.  mai^ÖLmaDhay-  patr.  Adj.  'von Ma^yHi.mänka  abstammend,  dessen  Nach-
19658:•  j.  mai8yöi.zar9maya-')  m,  Name  der Gottheit  der  ersten  Jahreszeit  und 
19669:•  j.  maiSyoi-äad-  Adj.  (auch  fem.)  'in der  Mitte'*  siUend':  vlhäjpahe  
19671:•  j.  maidyi^na-  n. :  s.  ma^yäna-.
19672:•  p.  maftiSta-  Adj.:  s.  unter  masiUa-.
19673:•  y,  g.  tnaf)  i)  Adv.  'immer,  immerdar': m°  va  fadais(sd.)..pairi/asai..
19680:•  j.  matafsman-  Adj.  (auch  fem.)  'sammt den  Verszeilen,  mit  allen  Versze
19687:•  j.  ^matgaoSävara- ■)  Adj.  (fem,  'ra-) 'mit  Ohrsdimuck,  Ohrgehängen  v
19689:•  j.  matgü'ihi-  Adj.  'mit  Unrat^  Kot  be- haftet, unrein':  nasaum  '^am  V
19691:•  j.  mat.ditnan-  Adj.  'sammt  seinen  Ge- schöpfen, seiner  Schöpfung':  ham
19693:•  j,  mat.-paiti.p9r38av-  Adj.  (fem.  °S7'T-) 'mit  den  .^tworten*'  versehen
```


## [2026-09-07T16:26:30.142Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19566,19577p' BRT.txt | cut -c1-600; echo \"=== 17710-17722 ===\"; sed -n '17714,17720p' BRT.txt | cut -c1-500"
}
```


### [2026-09-07T16:26:30.204Z] TOOL RESULT

```
•  j.  »■''matay-''  m.  'Vorspning  (des  Gebirgs), promunturium':  aofistimca  ..  masdayama vaS)ySJ>m?jnia  upa  maillm ''  iantaahqin pqsl&./ra%anhfm  (sd.)  hl  kamir^tm  vlnä-
dby  Google
»113
hay?n  *'. .  sollen  die  M.  auf  einem  Vor- sprung des  Gebirgs'*  ihm  den  Kopf schinden  . ."  V.j.io.
Zam  V.  3man:  —  lat.  vgl.  monl-isil
apat  i  mdm[i)]mt'i)  pabiäil,  etl.i /a
—  NA.  ufa-m".   —    *)  Ebenda  soll  dann  die
Leiche    den    Geiern     überani-wortet    werden.
Dazu   wird   der   Ort   gewablL   —    3)  Womit
'malay-  im  Abiaal  steht  —  1)  So  nach  Dst.
•  j.  "maite  *>  F.  6.
Fä.-.fiaJmSn,  —  >>  Ist  keia  Wort,  londem aus  vokumaiic  (Pü.;  vih  pcUniäti)  abgerissen; Bthl.  IF.  II.  134.
=== 17710-17722 ===
injra-
Muts':  yaha  vaim  humananhs  'narthasca (NPm.)  urväzimna  haomananhimna  va- nänia  vlsp!  karghs  Yt  lO.  34.
ai.  prämanas-  Adj.  (AV.  2.  l8.  1 ;  Bloomtibu): ■provident'), /rajBOHaj-  Adj,  tieiter  geBlimmt'.
•  j.  fra-mainya-  n.  'Praevalcnz,  Vonnacht über  — '  (Gen.):  nöii  nmänS.baxffm  . .  nöit 'manim  brä'iranqm  aglius/e (sd.)  P.43i  — *a^a  *nä  äxsta  (sd.)  htyqn  *ya'^a  *«3 buyill  . .  akmäi  saokäi  frasastäi  fraväkai Uta  *°mainyäi'^  ". .  uns  zum  Voiteil,  zum Ruhm,  zum  Preis  und  zur  Vormacht"  YL l6.3'.
Zum  V.  iman- ;  eig.  'Hervorr^en,  Vorsprung'. —  Vgl.  gall.  'Ep-iiirm  {Ipt;;  ?),  alb.  maji 'Spitie';  s.  dazu  Fick  Wb.4  i.  310,  Peksson KZ.  ^3,  29a.  —  Pü.:  «  ne  ki  pa  framänfatlh  i itätaräa  .,,  erL:  andar  iSnak pa pei fätik  diil istiU—  0  So  nur  K  13;  dafür  spricht  aber  die Lesung  /ramainSi  (mit  Epenthese!)  Ton  Fl usw.  NA.  korrigirt.  —  »)  Es  scheinen  nicht- zusammengehörige Sllicke  verbunden  zu  sein. aimäi  (Flur.)  passt  n
•  j.  fra-mar^ntam  Absol.  'beim  Auisagen (der  Gebete)',  mit  Gen.  subj.  ■>:  ySi  däilya.- yaona  carmta  (Sp,  449  u.)  ff  aisqm  nsil aSalsam  ratufris  raiufritim  *%w»r»sfiiti "(Leute)  die  ..,  falls  sie  die  Gebete  auf- sagen: ihnen  kann  nicht . .  vorschreiben" N.52.
KompE.  —  Zum  V.  »mar-.  —  Vä.-./ricSImart asi  Bsän,  erl.:  iviän  gäsäniär yasi  baziii  aiidar- vaSl  5  bun  „ht.  ~  ■)  Vgl.  a/ramar^nU,».
```


## [2026-09-07T16:26:44.240Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 333 -l 333 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg333 && ls -la pg333.png"
}
```


### [2026-09-07T16:26:45.951Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70886 Sep  7 12:26 pg333.png
```


## [2026-09-07T16:26:48.829Z] TOOL CALL #95: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg333.png"
}
```


### [2026-09-07T16:26:49.170Z] TOOL RESULT

```

```


## [2026-09-07T16:26:49.168Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T16:27:05.813Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 333 -l 333 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg333hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg333hi.png'); print(im.size)\n# top-right empty box region: in 1700x2200 at 200dpi it was approx x 848-1188, y 775-860 -> scale x2\nim.crop((1650,1500,2450,1780)).save('box1.png')\nim.crop((2150,2280,2500,2540)).save('box2.png')\n\"; ls -la box1.png box2.png"
}
```


### [2026-09-07T16:27:08.547Z] TOOL RESULT

```
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb 1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1988 Sep  7 12:27 box2.png
```


## [2026-09-07T16:27:11.746Z] TOOL CALL #97: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/box1.png"
}
```


### [2026-09-07T16:27:11.761Z] TOOL RESULT

```

```


## [2026-09-07T16:27:15.607Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg333hi.png')\nim.crop((1780,1660,2650,1930)).save('box1b.png')\nim.crop((2380,2480,2650,2760)).save('box2b.png')\n\"; echo ok"
}
```


### [2026-09-07T16:27:17.168Z] TOOL RESULT

```
ok
```


## [2026-09-07T16:27:20.063Z] TOOL CALL #99: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/box1b.png"
}
```


### [2026-09-07T16:27:20.075Z] TOOL RESULT

```

```


## [2026-09-07T16:27:28.046Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB manistan ===\"; grep -n \"mānistan\\|manistan\\|mānistan\\|mān-\\|mānēnītan\" NYB_vol2_glossary.txt | head -8; echo \"=== SKT ===\"; grep -n \"^Mansion\\|^Remain\\|^Mount\\|^Mane\\|^Mountain\" SKT.txt | head -8"
}
```


### [2026-09-07T16:27:28.112Z] TOOL RESULT

```
=== NYB manistan ===
1511:704, 8823. 10811 (1105 restore frda%). — | a-burt-framānēh, framān-burtār, -r&h. —
1522:framān-burtār [—-bwlt'l] submissive to commands, obedient 68°. — V. burtär.
7256:malax: Sak malidan: malitan mana: mānākēh mānistan: mānākēh māndagī: māndakēh mary: *murv marzbàn: marz-pàn mäyah: mātakēh mazah: micak
=== SKT ===
11032:Mane.  (£.)  A.  S.  manu-  Te gen.  of  m,iw,  a  mane ;  Swed  and Da,  moan,  O.  Ou.  man*,  G-  makm«^  i mana.  Cf.  W.  myngwn^  maac  froi neck ;  Iruh  muina,  collar,  from neck ;  Skt  manyd,  the  tendon  fag nape  of  the  neck :  I.,  moftiitt Orig.  sense  '  hair  ou  thr  nvd^*  '
15919:Remain ;  sec  Maiudon.
```


## [2026-09-07T16:27:34.941Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"KTLWN\" NYB_vol2_glossary.txt | head -8; echo \"=== SKT Mansion ===\"; grep -n \"^Mansion\" SKT.txt; grep -n \"Mansion\" SKT.txt | head -4"
}
```


### [2026-09-07T16:27:35.002Z] TOOL RESULT

```
38:The Aramaic ideograms used in this Manual are listed here, together with a pre- liminary analysis of the Aramaic lexical material from which they derive. From an Aramaic point of view, most of the forms in which the verbal ideograms appear in Book Pahlavi (as well as in the inscriptions and in the Psalter) are spurious, fabricated as they are by Iranian-speaking scribes and hence without any linguistic foundation. In fact, only impf. forms of the type YKTLWN = YIQT'LUN and some few other forms can claim to be genuine Aramaic. The intricate process by which the Iranian scribes transformed Aramaic forms into purely graphic signs will be dealt with in my new edition of the Frahang i Pahlavik. Here such ideographical forms as have totally fallen out of the Aramaic verbal system will be explained merely by reference to the closest corresponding Aramaic forms or simply to the triconsonantal root, from which the 3d p. sg. perf. can be easily seen, e. g. NKS, pf. N'KAS (NB: — roots as BNY, HZY have the perf. B'NA, HAZA; HDY has HADI).
127:KTLWN-: (KTR) pa**el KATTAR to wait for, to remain
236:YKTLWN-: YIQT' LUN impf. 3d p. pl. of QTL to kill
2415:mändan [m’ndn'; KTLWN-tn'] man-, to remain, to stop 117-14. 1613. 4411, 697; to live 1513. 521%, 9720; — apäc ~ to be left 289, 2926-27; without apāc in, this sense 1527, 108%; frāc ~ 1039. — Av. (1124) 2man-; common Ir.
2852:ēzanišn [YKTLWN-8n'] v. n. of.
2853:özatan [?wetn'; YKTLWN-tn'] özan- (YKTLWN-x, for ózanet 29%) to kill; cond. 3d p. sg. hakar-im . . . nē dzat hah 3221, 3d pl. hakar-im ... ne ozat hand 335; — pt. pass. dzatak killed: hunuskan ozatak gurg a bitch wolf whose cubs had been killed 4927; hunuskän özatak dit saw the cubs killed 50!; — v. n. dzanisn 1. pred. : be ozanišn is to be killed 108; 2. as a subst. : kārēcār u ozanišn 134; pat ozanišn āivēnak 1032, v. divénak. — Av. (491) ava-gan-, pres. -jan-, pt. -jata-; MPrth
=== SKT Mansion ===
11209:MastilT:  see  Mansion.
11396:Uenagerie ;  see  Mansion.
```


## [2026-09-07T16:27:42.925Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"men-\" f249e87bde5d28c8.txt | sed -n '1,25p'"
}
```


### [2026-09-07T16:27:42.974Z] TOOL RESULT

```
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/men-
4:TITLE: Reconstruction:Proto-Indo-European/men- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/men- - Wiktionary, the free dictionary 
99: Reconstruction:Proto-Indo-European/ men- 
161: *men- ( perfective ) [ 1 ] [ 2 ] 
178: Terms derived from the Proto-Indo-European root *men- (think) (91 c, 0 e) 
260: *men- [ 4 ] [ 5 ] [ 6 ] 
267: Terms derived from the Proto-Indo-European root *men- (stay) (9 c, 0 e) 
278: *mí-men-ti ~ *mí-mn̥-nti ( i-reduplicated athematic present ) [ 4 ] [ 7 ] [ 8 ] 
323: Proto-Celtic: *an-men- ( “ patience, forbearance ” ) [ 13 ] [ 7 ] 
331: ^ Or from *memóne , from the root *men- ( “ to think ” ) . 
336: *men- 
343: Terms derived from the Proto-Indo-European root *men- (stand out) (30 c, 0 e) 
349: *men-eh₂ 
377: *men- [ 14 ] ( see also formations containing -n- under *mey- ( “ small, little ” ) ) 
384: Terms derived from the Proto-Indo-European root *men- (small) (33 c, 0 e) 
429: ^ Rix, Helmut , editor ( 2001 ), “ 1.*men- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 435 
433: ↑ 4.0 4.1 4.2 4.3 4.4 4.5 4.6 Rix, Helmut , editor ( 2001 ), “ 2.*men- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 437 
435: ^ Pokorny, Julius ( 1959 ), “ men- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 2, Bern, München: Francke Verlag, page 729 
437: ^ Mallory, J. P. with Adams, D. Q. ( 2006 ), “*men-”, in The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 227 
451: ^ Matasović, Ranko ( 2009 ), “*an-men-V-”, in Etymological Dictionary of Proto-Celtic (Leiden Indo-European Etymological Dictionary Series; 9), Leiden: Brill , →ISBN , page 38 
453: ^ Pokorny, Julius ( 1959 ), “ men- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 2, Bern, München: Francke Verlag, page 728 
457: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/men-&oldid=91807744 "
500: Reconstruction:Proto-Indo-European/ men-
```


## [2026-09-07T16:27:46.326Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '255,350p' f249e87bde5d28c8.txt"
}
```


### [2026-09-07T16:27:46.369Z] TOOL RESULT

```
 ⇒ Proto-Indo-Iranian: *mántras ( see there for further descendants )

 Root
 [ edit ] 

 *men- [ 4 ] [ 5 ] [ 6 ] 

 to stay , remain 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *men- (stay) (9 c, 0 e) 

 *mén-e-ti ( root thematic present ) [ 4 ] [ 7 ] 
 Proto-Hellenic: *ménō 
 Ancient Greek: μένω ( ménō , “ to stay, remain ” ) 

 > ? *me-món-e ( reduplicated stative ) 
 Proto-Indo-Iranian: *mamā́na 
 Proto-Indo-Aryan: *mamā́na 
 Sanskrit: ममन्धि ( mamandhi , “ wait! ” , 2sg.ipv.perf.act. ) , अम॑मन् ( ámaman , “ had waited ” , 3sg.plqpf.act. ) , ममन्यात् ( mamanyāt , 3sg.opt.perf.act. ) [ note 1 ] 

 *mí-men-ti ~ *mí-mn̥-nti ( i-reduplicated athematic present ) [ 4 ] [ 7 ] [ 8 ] 
 Proto-Hellenic: 
 Ancient Greek: μίμνω ( mímnō , “ to stay, remain ” ) 

 > ? Proto-Anatolian: ( unlikely [ 9 ] ) 
 Hittite: 𒈪𒅎𒈠𒄿 ( mi-im-ma-i , “ to refuse, decline ” , 3sg.pres.act. ) 

 *mḗn-s-t ~ *mén-s-n̥t ( s-aorist ) [ 4 ] 
 Proto-Hellenic: 
 Ancient Greek: ἔμεινα ( émeina , “ remained ” ) 

 Proto-Italic: 
 Latin: mānsī ( “ remained ” ) 

 *mon-éye-ti ( éye-causative ) [ 4 ] [ 7 ] 
 Proto-Indo-Iranian: *mānáyati 
 Proto-Iranian: *mānáyati ( see there for further descendants )

 *m̥n-éh₁ye-ti ( eh₁-stative ) [ 4 ] [ 10 ] 
 Proto-Armenian: *menāye- [ 11 ] 
 Old Armenian: մնամ ( mnam , 1sg.pres. ) 
 Armenian: մնալ ( mnal ) 

 Proto-Italic: *m(V)nēō [ 10 ] ( unexplained -o- ) 
 Latin: maneō ( see there for further descendants )

 *mn̥-sḱé-ti ( sḱe-present ) [ 4 ] [ 12 ] 
 Proto-Armenian: *menāsḱet [ 11 ] 
 Old Armenian: մնաց ( mnacʻ , 3sg.aor. ) 

 ( possibly ) Proto-Tocharian: *mäsk- ( “ to reside, be ” ) [ 12 ] 
 Tocharian A: mäskatär 

 Tocharian B: mäsketär 

 *mon-éh₂ 
 Proto-Hellenic: *monā́ 
 Ancient Greek: μονή ( monḗ , “ staying, detention ” ) 

 *mé-mn-ō 
 Proto-Hellenic: 
 Ancient Greek: Μέμνων ( Mémnōn ) 

 Unsorted formations 

 Proto-Celtic: *an-men- ( “ patience, forbearance ” ) [ 13 ] [ 7 ] 
 Middle Welsh: anmynedd , amynedd 

 Old Irish: ainmne 

 Notes
 [ edit ] 

 ^ Or from *memóne , from the root *men- ( “ to think ” ) . 

 Root
 [ edit ] 

 *men- 

 to stand out , to tower 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *men- (stand out) (30 c, 0 e) 

 *mn̥-éh₁-ye-ti 
 Proto-Italic: *menēō 
 Latin: (ē)mineō , (im)mineō , (prō)mineō ( see there for further descendants )

 *men-eh₂ 
 Proto-Italic: *menā
```


## [2026-09-07T16:29:04.388Z] TOOL CALL #104: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/mons\" \\\n \"https://en.wiktionary.org/wiki/Monte_Carlo\" \\\n \"https://en.wiktionary.org/wiki/Montgomery\" \\\n \"https://www.etymonline.com/word/paramount\" ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 333, Men 3: Latin mons; French/Italian/English mont- proper names borrowed into Persian' 2>&1 | tail -1; done"
}
```


### [2026-09-07T16:29:07.357Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/mons
/home/sfmqrb/git/rishe/data/verification/sources/web/e627ad421fa74d34.txt
### https://en.wiktionary.org/wiki/Monte_Carlo
/home/sfmqrb/git/rishe/data/verification/sources/web/948ca2fa4ac91867.txt
### https://en.wiktionary.org/wiki/Montgomery
/home/sfmqrb/git/rishe/data/verification/sources/web/b440a4bf5aa787bd.txt
### https://www.etymonline.com/word/paramount
/home/sfmqrb/git/rishe/data/verification/sources/web/7d1b02c816e53b53.txt
```


## [2026-09-07T16:29:12.866Z] TOOL CALL #105: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== mons ==\"; grep -n \"From Proto-Italic\\|Proto-Indo-European\\|mountain\" e627ad421fa74d34.txt | head -6; echo \"== Monte Carlo ==\"; grep -n -i \"italian\\|Charles\\|named\\|monte\" 948ca2fa4ac91867.txt | head -8; echo \"== Montgomery ==\"; grep -n -i \"Norman\\|Old French\\|from.*mont\\|surname\\|place\" b440a4bf5aa787bd.txt | head -8; echo \"== paramount ==\"; grep -n \"amont\\|Old French\\|1530\" 7d1b02c816e53b53.txt | head -5"
}
```


### [2026-09-07T16:29:12.952Z] TOOL RESULT

```
== mons ==
282: Borrowed from Latin mōns ( “ mountain ” ) . Doublet of mount .
303: ( astronomy , geology ) An extraterrestrial mountain or volcano .
323: astronomy: mountain on a planet or moon
435: Proto-Indo-European *men- 
437: Proto-Indo-European *-tis 
439: Proto-Indo-European *móntis 
== Monte Carlo ==
1:URL: https://en.wiktionary.org/wiki/Monte_Carlo
4:TITLE: Monte Carlo - Wiktionary, the free dictionary
6:Monte Carlo - Wiktionary, the free dictionary 
100: Italian 
102: Toggle Italian subsection 
195: Monte Carlo 
263: See also: Monte-Carlo and Montecarlo 
268: English Wikipedia has an article on: Monte Carlo 
== Montgomery ==
188: From a Norman surname, from a place in Normandy ( Old French for "Gomeric's hill"). Gumaric was a Germanic personal name composed of *gumô ( “ man ” ) and *rīks ( “ ruler ” ) (whence the modern French surnames Gomery , Gommery and Gumery [ 1 ] or the Galician placename Gomariz ).
209: A surname from Old French .
213: A male given name transferred from the surname .
215: A number of places in the United States :
218: 2015 March 5, Douglas Brinkley, “Selma’s historic bridge deserves a better name”, in CNN ‎ [1] , archived from the original on 26 April 2015 : So when King – who had been in Atlanta for “Bloody Sunday” – telegrammed Parks about returning to Alabama to take part in a third mass march from Selma to Montgomery , her immediate answer was “Why, of course.” 
220: A census-designated place in Chatham County , Georgia .
321: Unadapted borrowing from English Montgomery .
335: Retrieved from " https://en.wiktionary.org/w/index.php?title=Montgomery&oldid=92416984 "
== paramount ==
25: "supreme, superior in power or jurisdiction," 1530s, from Anglo-French paramont , Old French paramont "above" (in place, order, degree), mid-14c., from Old French par "by," from Latin per "through, for, by" (see per (prep.)) + amont "up," from a mont "upward" (see amount (v.)). The word is equivalent to the Latin phrase per ad montem , literally "to the hill." Related: Paramountcy .
26: also from 1530s 
32: late 13c., "to go up, rise, mount (a horse)," from Old French amonter "rise, go up; mean, signify," from amont (adv.) "upward, uphill," literally "to the mountain" (12c.), a contraction of the prepositional phrase a mont , from a (from Latin ad "to;" see ad- ) + Latin montem (nominative mons ) "mountain" (from PIE root *men- (2) "to project").
70: late 14c., "beyond expression, too great for words, inexpressible," from Old French ineffable (14c.) or directly from Latin ineffabilis "unutterable," from in- "not, opposite of" (see in- (1)) + effabilis "speakable," from effari "utter," from assimilated form of ex "out" (see ex
82: c. 1500, "a favorite; a darling, one who or that which is beloved" (a sense now obsolete), from Old French mignon "a favorite, darling" (n.), also a term of (probably homosexual) abuse; as an adjective, "dainty, pleasing, favorite," from mignot "pretty, attractive, dainty, gracio
```


## [2026-09-07T16:29:18.427Z] TOOL CALL #106: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T16:29:18.464Z] TOOL RESULT

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
```


## [2026-09-07T16:29:21.186Z] TOOL CALL #107: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-07T16:29:21.224Z] TOOL RESULT

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


## [2026-09-07T16:40:44.196Z] TOOL CALL #108: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build333.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_MEN  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/men-\"\nW_MAND = \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%86%D8%AF%D9%86\"\nW_OMID = \"https://en.wiktionary.org/wiki/%D8%A7%D9%85%DB%8C%D8%AF\"\nW_HWT  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hamw%C3%A1ti%C5%A1\"\nW_HWTV = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hamw%C3%A1tati\"\nA_OMID = \"https://abadis.ir/fatofa/%D8%A7%D9%85%DB%8C%D8%AF/\"\nA_MTRL = \"https://abadis.ir/fatofa/%D9%85%D9%88%D9%86%D8%AA%D8%B1%D8%A7%D9%84/\"\nE_MANS = \"https://www.etymonline.com/word/mansion\"\nE_MOUNT= \"https://www.etymonline.com/word/mount\"\nE_PROM = \"https://www.etymonline.com/word/prominent\"\nE_MANE = \"https://www.etymonline.com/word/mane\"\nE_PARA = \"https://www.etymonline.com/word/paramount\"\nW_MONS = \"https://en.wiktionary.org/wiki/mons\"\nW_MC   = \"https://en.wiktionary.org/wiki/Monte_Carlo\"\nW_MG   = \"https://en.wiktionary.org/wiki/Montgomery\"\n\nPOK729 = (\"POK_full.txt 'Root / lemma: mehn-5' (= men-5) \\\"Meaning: to stay, stand still\\\", \"\n          \"Note \\\"(= men- 'think'?)\\\", Material \\\"Avestan ap. man- 'abide, remain, wait, hold on', \"\n          \"Avestan fra-man- 'persist' ... Latin maneo, -ere\\\", \\\"Page(s): 729\\\"\")\nPOK726 = (\"POK_full.txt 'Root / lemma: mehn-1' \\\"Meaning: to tower\\\", Material \\\"Avestan framanyente \"\n          \"(: Latin pro-minere) 'they obtain projection', mati- (*mnti-) 'protrusion of mountain range'; \"\n          \"Latin e-mineo ... mons, -tis ... related is probably *mohnoh- 'nape, neck'\\\", \\\"Page(s): 726\\\"\")\nPOK747 = (\"POK_full.txt 'Root / lemma: mono-' \\\"Meaning: neck\\\", Note \\\"in derivatives ... also 'necklace, \"\n          \"Halsschmuck'\\\", Material \\\"Old Indie manya 'nape'; Avestan minu- 'Halsgeschmeide' ... manao&rf \"\n          \"'neck, nape' (*mon-eu-tro-) ... Germanic *mand 'mane'\\\", \\\"Page(s): 747-748\\\", \"\n          \"\\\"See also: compare above S. 726 men- 'tower'\\\"\")\n\ndef n(i, lang, words, verdict, deriv, deriv_fa, sources, refs, cons):\n    return {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n            \"derivation\": deriv, \"derivation_fa\": deriv_fa,\n            \"sources\": sources, \"ref_check\": refs, \"consulted\": cons}\n\n# ------------------------------------------------------------------ entry 0\ne0_nodes = [\n n(1, \"Avestan / Old Persian\", \"man 2\",\n   \"confirmed\",\n   \"Av. and OP man- 'to remain, wait, abide' (Bartholomae AiW col. 1124-1126 s.v. 2man- V. 'bleiben; \"\n   \"warten', with the iterative/causative stem manaya-; OP amanaya 'he waited' DB 2.28, 2.48, 2.63, \"\n   \"amanaya mam 'awaited me'; Av. upa-manayen 'they shall wait' V.5.42, fra-man- 'to persist'). The \"\n   \"e-grade root *men- appears in Iranian as man-, the causative *mon-eye-ti as OIr. *manaya- > Av./OP \"\n   \"manaya-; the 'await' sense is the transitive use of 'stay put' (exactly as Gk. menein tina, Lat. \"\n   \"manere hostem). Nourai's numbering 'man 2' separates it from man- 'to think' (AiW 1man-), which is \"\n   \"correct practice, although Kent and Pokorny both suspect the two are ultimately one root \"\n   \"('probably specialization of pIE *men- \\\"think\\\" in meaning \\\"remain thinking\\\"' - Kent p. 202).\",\n   \"ریشهٔ ایرانی باستان man- «ماندن، چشم داشتن، انتطار کشیدن» در اوستایی و پارسی باستان هر دو گواه دارد؛ \"\n   \"بارتولومه در فرهنگ ایرانی باستان (ستون ۱۱۲۴–۱۱۲۶) آن را man- دوم «باقی ماندن؛ منتطر ماندن» می‌خواند و \"\n   \"ستاک موکرر/سببی manaya- را برای آن می‌آورد: در سنگ‌نوشتهٔ بیستون amanaya «منتطر ماند» و در وندیداد upa.manayen \"\n   \"«باید درنگ کنند». معنای «انتطار» تحول معنایی طبیعی از «بر جای ماندن» است. ادعای نورایی درست است؛ \"\n   \"فقط بدانیم که کنت و پوکورنی این ریشه را احتمالاً همان man- «اندیشیدن» می‌دانند.\",\n   [W_MAND, W_MEN, E_MANS],\n   [{\"ref\":\"KLN:934\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 502 (printed pp. 932-934), s.v. 'mansion': 'fr. mansus, pp. of manere ... which is cogn. with Gk. menein, mone, Avestic man-, Pers. mandan, \\\"to remain\\\", Arm. mnam ... fr. I.-E. base *men-, \\\"to remain, wait for\\\"' - exactly Nourai's arrow.\"},\n    {\"ref\":\"HRN:215\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 237-238 (printed pp. 215-216), no. 966 'manden \\\"bleiben; lassen\\\"': 'ap. Vman-, amanaya \\\"es erwartete (mich)\\\"; aw. Vman-, upa manayen \\\"sie sollen abwarten\\\"'.\"},\n    {\"ref\":\"KNT:202\",\"status\":\"supports\",\"note\":\"KNT.txt leaf 226 (running heads '202 OLD PERSIAN' on leaf 225, 'LEXICON 203' on leaf 227): '2man- vb. \\\"remain\\\": Av. man-, iterative pres. manaya-, Gk. mno, Lt. maneo; probably specialization of pIE *men- \\\"think\\\" ... amanaya imf. DB 2.48, 63'.\"}],\n   [{\"src\":\"BRT\",\"where\":\"col. 1124-1126 (BRT.txt line 19741-19751)\",\"stance\":\"supports\",\"note\":\"'j., g., p. 2man- V. \\\"bleiben; warten\\\". Praes. manaya- ... upa \\\"warten, ab-, zuwarten\\\" (V.5.42, V.6.27, V.8.38)'; the same article ends 'np. mandan \\\"bleiben\\\"'.\"},\n    {\"src\":\"POK\",\"where\":\"p. 729 (men-5)\",\"stance\":\"supports\",\"note\":POK729},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p. 267\",\"stance\":\"supports\",\"note\":\"'5. men- \\\"bleiben, stillestehn\\\" (= men \\\"denken\\\"? s. u.). Ai. man- ..., av. ap. man- \\\"bleiben, warten\\\", av. fra-man- \\\"ausharren\\\": arm. mnam ... gr. meno' (WLD_Bd2_pages.txt block 271).\"},\n    {\"src\":\"SYN\",\"where\":\"12.16 REMAIN, STAY, WAIT\",\"stance\":\"supports\",\"note\":\"'1. IE *men- \\\"remain\\\", to be distinguished from *men- \\\"think\\\", even though they may be ultimately the same. Walde-P. 2.267 ... Av. man- in upa-manaya- \\\"wait for\\\", manaya- \\\"cause to remain\\\", OPers. manaya- \\\"wait for\\\", NPers. mandan \\\"remain\\\"'.\"},\n    {\"src\":\"IEC\",\"where\":\"col./p. under 'mno, io (mon-) (3)'\",\"stance\":\"supports\",\"note\":\"Mann: 'mno, io (mon-) (3) \\\"remain\\\". WP II, 267 ... Av. man-, v. \\\"remain\\\", OPer. man-, id.; Per. manam, inf. mandan, id.; Arm. mnam; Gk. mimno beside meno; Lat. maneo, ere, id.'\"},\n    {\"src\":\"AHD\",\"where\":\"s.v. men-3\",\"stance\":\"partial\",\"note\":\"Watkins 1985 'men-3. To remain. Variant suffixed (stative) form *man-e- in Latin manere ... [Pok. 5. men- 729]' - has the root and Latin, but lists no Iranian reflex.\"}]),\n\n n(2, \"Pahlavi\", \"mân-stan\",\n   \"confirmed\",\n   \"Middle Persian manistan / mandan, pres. stem man- (Book Pahlavi <KTLWN-tn'>, i.e. the Aramaic \"\n   \"ideogram of the root KTR 'to wait', with phonetic <m'ndn'>), 'to stay, remain'. Old Iranian man- \"\n   \"with the MP infinitive suffix -istan/-tan gives man(i)stan beside the -d- infinitive mandan (the \"\n   \"-nd- of mandan is the regular MP outcome of the *-nt-/*-n-t- past stem, whence also the past stem \"\n   \"mand). Nourai's hyphenated spelling 'man-stan' reproduces Horn's citation form 'phlv. man(i)sn, \"\n   \"man(i)stan'. MacKenzie glosses 'mandan, 1man- [KTLWN-tn'] stay, remain' and 'manistan = mandan'.\",\n   \"در فارسی میانه (پهلوی) مصدر mānistan / māndan با ستاک حال mān- «ماندن، درنگ کردن» به کار رفته \"\n   \"و در خط پهلوی با هزوارش <KTLWN-tn'> (از ریشهٔ آرامی KTR «منتطر ماندن») نوشته می‌شده است. \"\n   \"پسوند مصدری -istan بر ستاک man- افزوده شده و صورت دوم māndan از ستاک گذشتهٔ mānd ساخته شده است. \"\n   \"مکنزی و نیبرگ و معین (حاشیهٔ برهان قاطع) هر سه همین اندرون را می‌دهند؛ ادعای نورایی درست است. \"\n   \"نگارش «mân-stan» در نمودار همان شکل ارجاعی هرن است.\",\n   [W_MAND],\n   [{\"ref\":\"HRN:215\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 238 (printed p. 216, entry 966 begun on p. 215): 'phlv. man(i)sn, man(i)stan, paz. mandan' listed directly under np. manden < ap./aw. man-.\"}],\n   [{\"src\":\"PHD\",\"where\":\"p. 53 s.v. mandan (PHD.txt line 455)\",\"stance\":\"supports\",\"note\":\"MacKenzie: \\\"mandan, 1man- [KTLWN-tn' < A V ktr | M m'nd, N ~] stay, remain\\\"; \\\"manistan [{KTLWN}stn'] = mandan\\\".\"},\n    {\"src\":\"NYB\",\"where\":\"Glossary s.v. mandan (NYB_vol2_glossary.txt line 2415)\",\"stance\":\"supports\",\"note\":\"Nyberg: \\\"mandan [m'ndn'; KTLWN-tn'] man-, to remain, to stop ... - Av. (1124) 2man-; common Ir.\\\" - i.e. he refers the MP verb to Bartholomae's AiW col. 1124 2man-, precisely Nourai's parent.\"},\n    {\"src\":\"BQT\",\"where\":\"vol. 4 p. 1950 (pdf 33), Mo'in's footnote on ماندن\",\"stance\":\"supports\",\"note\":\"'ماندن - بفتح دال. از: مان (ریشه) + دن ... ایرانی باستان *man- «پارتولمه ۱۱۲۶»؛ پهلوی mānistan «نیبرگ ۱۴۶-۵» ... پارسی باستان و اوستا -man- (انتطار کشیدن)؛ پهلوی mān(i)štan، mān(i)stan، پازند māndan'.\"}]),\n\n n(3, \"Persian\", \"mândan 2\",\n   \"confirmed\",\n   \"New Persian ماندن mandan 'to remain, stay', pres. stem مان- man-, direct continuation of MP \"\n   \"mandan/manistan with no phonetic change beyond the loss of the MP infinitive ending -tan > NP -dan \"\n   \"after n. The other senses listed in Borhan (توقف کردن، منزل کردن، انتطار کشیدن، خسته شدن) \"\n   \"reproduce the Old Iranian range; the participle مانده manda 'tired' (cf. Kurd. manda, Afgh. manda, \"\n   \"Bal. managh 'to become tired') is the same stem. Nourai's '2' distinguishes it from ماندن / \"\n   \"مانستن 'to resemble', which Mo'in derives from man- 'to think' - a distinction the sources make too.\",\n   \"«ماندن» فارسی نو دنبالهٔ بی‌واسطهٔ māndan/mānistan پهلوی است؛ تنها دگرگونی افتادن پایانهٔ \"\n   \"مصدری -tan و جایگزینی -dan پس از n است. معین در حاشیهٔ برهان قاطع (ص ۱۹۵۰) روشن می‌نویسد: \"\n   \"ایرانی باستان *man-، پارسی باستان و اوستایی man- «انتطار کشیدن»، لاتینی maneō، یونانی ménō. \"\n   \"شمارهٔ ۲ نورایی این فعل را از «مانستن/مانند بودن» جدا می‌کند که معین آن را از man- «اندیشیدن» می‌داند؛ \"\n   \"ادعای نورایی درست است.\",\n   [W_MAND],\n   [{\"ref\":\"BQT:1950\",\"status\":\"supports\",\"note\":\"BQT vol. 4 pdf p. 33 = printed 1950 (offset +1917 confirmed by the running head ۱۹۴۹ on pdf 32 and the note 'بقیه در صفحهٔ ۱۹۵۳' on pdf 35): Mo'in's footnote s.v. ماندن - 'ایرانی باستان *man- «پارتولمه ۱۱۲۶» ... ارمنی mnam، لاتینی maneō، یونانی ménō، کردی mān'.\"}],\n   [{\"src\":\"HRN\",\"where\":\"no. 966, pp. 215-216\",\"stance\":\"supports\",\"note\":\"'966. manden \\\"bleiben; lassen\\\" ... ap. Vman-, amanaya ...; aw. Vman-, upa manayen ...; phlv. man(i)sn, man(i)stan, paz. mandan; arm. mnam; lat. maneo; gr. meno; kurd. main; bal. manay'.\"},\n    {\"src\":\"ARY\",\"where\":\"Latin index, pdf p. 461 (printed 462), s.v. MAN-, MANDAN, MANISTAN\",\"stance\":\"supports\",\"note\":\"Aryanpur's independent entry lists MAN- (Avestan), MAN- (Sanskrit), MNAM (Armenian), MENO/MENEIN (Greek), MANEO/MANERE (Latin), MAIN/MANDU (Kurdish), MANTA/MANAGH (Baluchi), MASK (Tokharian), with refs to Barnhart (MANSION) 631, MacKenzie, Buck 838, Skeat (REMAIN) 509.\"},\n    {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in s.v. امید/ماندن via abadis.ir\",\"stance\":\"silent\",\"note\":\"The Mo'in lexicon entry gives only the senses, no origin tag; the etymology is in Mo'in's Borhan footnote (see ref_check).\"},\n    {\"src\":\"CHEUNG\",\"where\":\"Etymological Dictionary of the Iranian Verb\",\"stance\":\"silent\",\"note\":\"grep of CHEUNG.txt for 'mandan', 'man-' 'to remain' found no *man- 'to remain' entry (Cheung's lemma list omits it); no contrary statement.\"}]),\n\n n(4, \"Avestan\", \"upa-mati\",\n   \"plausible\",\n   \"The Avestan material is real but not quite in the shape drawn. Bartholomae has the verb upa + man- \"\n   \"'warten, ab-, zuwarten' (V.5.42 'nine days shall the Mazdayasnians wait', V.6.27, V.8.38) and the \"\n   \"verbal abstract upa.maiti- f. 'waiting' (cvat drajo upa.maitim aste V.5.53 'how long shall one \"\n   \"remain sitting in waiting'); Buck cites Av. upa-manaya- 'wait for' under IE *men- 'remain'. So the \"\n   \"arrow man- > upa-mati- is formally sound: prefix upa- 'up to, at' + the zero-grade abstract *-mati- \"\n   \"(*mn-ti-). What is NOT attested is the gloss 'keep the hopes up': Av. upa.maiti- means 'delay, \"\n   \"waiting', and the notion 'hope' is imported here only because Nourai wants it as the ancestor of \"\n   \"MP omed (see node 5, where that step is disputed).\",\n   \"در اوستا فعل upa + man- «درنگ کردن، منتطر ماندن» و اسم معنای upa.maiti- «انتطار، درنگ» \"\n   \"گواه دارد (وندیداد ۵/۴۲ و ۵/۵۳؛ بارتولومه). پیشوند upa- بر ستاک صفر *mn-ti- افزوده شده، پس این پیوند \"\n   \"از نطر ساخت درست است؛ اما معنای «امید داشتن» در متون اوستایی برای این واژه دیده نمی‌شود؛ این معنا را \"\n   \"نورایی از روی مقصدش (رساندن به «امید») افزوده است. با احتیاط پذیرفتنی است: واژه درست است، معنا نه.\",\n   [W_OMID],\n   [{\"ref\":\"SNS:74\",\"status\":\"partial\",\"note\":\"SNS printed p. 74 (pdf 54 of the IA text-PDF; running head ۷۴; reading saved at data/verification/sources/refs/ocr/SNS/74.vision.txt) s.v. omed: it gives *ava + Vmay- (GNPE 26) as the etymology and only then adds 'پروفسور کانگا آن را از upa + mati اوستایی و ریشهٔ man: ماندن، صبر کردن میداند (Kanga. cit. Han. 46-7)'. So the reference carries Nourai's upa+mati only as Kanga's opinion, not as its own.\"}],\n   [{\"src\":\"BRT\",\"where\":\"col. 1125 (upa + man-) and col. 349 s.v. aste (BRT.txt lines 19743, 7485)\",\"stance\":\"partial\",\"note\":\"'mit upa \\\"warten, ab-, zuwarten\\\" ... navo x'sapanam upa.manayen \\\"nine nights the Mazdayasnians shall wait\\\" V.5.42'; 'cvat drajo upa.maitim a(ste) V.5.53' - the form is upa.maiti-, glossed 'waiting', with no sense 'hope'.\"},\n    {\"src\":\"SYN\",\"where\":\"12.16\",\"stance\":\"supports\",\"note\":\"Buck lists 'Av. man- in upa-manaya- \\\"wait for\\\"' under IE *men- 'remain' - the same prefixed formation.\"},\n    {\"src\":\"POK\",\"where\":\"p. 729\",\"stance\":\"partial\",\"note\":\"Pokorny's men-5 lists 'Avestan fra-man- \\\"persist, stand firm\\\"' but no upa-mati-.\"}]),\n\n n(5, \"Pahlavi\", \"ômĕd\",\n   \"disputed\",\n   \"The word is real: Book Pahlavi <'wmyt'> 'hope', read ummed by MacKenzie, omet by Nyberg, omed by \"\n   \"Tavoosi (SNS), with the variant <'ymyt'> emed and the derivatives ummedwar, an-ummed 'hopeless'. \"\n   \"What is disputed is the parent. (i) Bartholomae/Horn take it from *ava + may- 'to set, fix in' \"\n   \"(Horn no. 109, HRN p. 26; this is the 'GNPE 26' cited by SNS). (ii) Nyberg derives it from Old \"\n   \"Iranian *abi-mati-, an abstract of abi- + man- 'to THINK' (not 'to remain'), with a SW development \"\n   \"*aibimati- > *ayibmati- > *ayim(m)et > emet, and a form ham-omed whence NP ummed. (iii) The current \"\n   \"standard account (Wiktionary, following Cheung 2007 s.v. *uat) reconstructs Proto-Iranian *hamwatis \"\n   \"'hope' < *ham- + *wat- 'to be informed, acquainted', supported by Parthian hmwd- 'to believe' and \"\n   \"Christian Sogdian 'wt- 'to hope for', 'nwth 'hope, faith', Arm. LW hawat 'belief'. Nourai's route \"\n   \"(Av. upa-mati- > omed) is Kanga's older proposal, adopted by no modern authority; the vowel of \"\n   \"<'wmyt'> (u-/o-, never *upa-) is the main obstacle.\",\n   \"واژهٔ پهلوی <'wmyt'> «امید» مسلم است (مکنزی: ummēd؛ نیبرگ: ōmēt؛ طووسی: ōmēd) و صورت دیگرش ēmēd است؛ \"\n   \"اما ریشهٔ آن مورد اختلاف است. بارتولومه و هرن (شمارهٔ ۱۰۹) آن را از *ava + may- «نشاندن، فرو کردن» می‌دانند؛ \"\n   \"نیبرگ از ایرانی باستان *abi-mati- (از ریشهٔ man- «اندیشیدن»، نه «ماندن»)؛ و پژوهش امروزی (چونگ ۲۰۰۷ ذیل *uat \"\n   \"و ویکی‌واژه) از ایرانی آغازین *ham-wati- «امید، باور»، هم‌ریشه با پارتی hmwd- «باور داشتن» و سغدی مسیحی \"\n   \"'nwth «امید». پس مسیر نورایی (upa-mati- اوستایی) پیشنهاد کهن کانگاست و پژوهش امروزی آن را رد می‌کند.\",\n   [W_OMID, W_HWT, W_HWTV, A_OMID],\n   [{\"ref\":\"SNS:74\",\"status\":\"partial\",\"note\":\"SNS p. 74 (vision reading saved at data/verification/sources/refs/ocr/SNS/74.vision.txt) prints the Pahlavi reading omed exactly as Nourai does, but heads the entry with '*ava + Vmay- (GNPE. 26)' and gives upa+mati only as 'پروفسور کانگا آن را ... میداند'.\"}],\n   [{\"src\":\"NYB\",\"where\":\"Glossary s.v. omet (NYB_vol2_glossary.txt lines 2810-2812)\",\"stance\":\"contradicts\",\"note\":\"\\\"omet ['wmyt'] hope 66. 12116. - < OIr *abi-mati-, abstr. derived from abi + Av. (1121 sqq.) man- (v. menitan); ... whence NP ummed; in SW > *aibimati- > *ayibmati- > *ayim(m)et, whence emet\\\" - a different prefix (abi-, not upa-) and the 'think' root.\"},\n    {\"src\":\"HRN\",\"where\":\"no. 109, p. 26\",\"stance\":\"contradicts\",\"note\":\"\\\"109. umed 'Hoffnung', umid, omed ... phlv. umet bezw. omet ... ai. *ava + Vmay- 'einsenken', vergl. methi- 'Pfeiler, Pfosten' (?) ... (Bartholomae, ZDMG. 44, 553)\\\" - Horn/Bartholomae derive it from may-, not man-.\"},\n    {\"src\":\"PHD\",\"where\":\"p. 84 s.v. ummed (PHD.txt line 599); p. 32 s.v. emed (line 321)\",\"stance\":\"partial\",\"note\":\"\\\"ummed ['wmyt' | N ~] hope. ~war [-w'r] hopeful\\\"; \\\"emed [*'ymyt'] hope\\\"; \\\"an-ummed ['nwmyt' | N naumed] hopeless, despairing\\\" - MacKenzie reads the word ummed and offers no etymology.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"s.v. *uat 'to inspire, be informed, acquainted', pp. 427-428\",\"stance\":\"contradicts\",\"note\":\"\\\"*PARTHIAN: (+ *ham-) hmwd- 'to believe' ... *SOGDIAN: (+ *ham-) CSogd. 'wt- 'to hope for', ... CSogd. 'nwth 'hope, faith' ... *MISC: (+ *fra- or *ham- ?) Arm. (LW) hawat 'belief'\\\" - the *ham-wat- family that modern accounts make the source of MP ummed.\"},\n    {\"src\":\"BQT\",\"where\":\"Mo'in's Borhan footnote on امید, quoted by Dehkhoda via abadis.ir\",\"stance\":\"partial\",\"note\":\"'امید. [اُ / اُمْ می] (اِ) در پهلوی، اُمِت. در پازند، اُمِذ. (از حاشیه برهان قاطع چ معین)' - Mo'in gives only MP umet / Pazand umed, no Avestan antecedent.\"}]),\n\n n(6, \"Persian\", \"omîd\",\n   \"disputed\",\n   \"NP امید omid/ommid (Classical umed, ummed, umid, ummid; Tajik умед/уммед) is the regular reflex of MP \"\n   \"<'wmyt'> ummed (MP -e- > NP -i- in the classical spelling امید, final -t > -d), with the \"\n   \"derivative امیدوار omidvar < MP ummedwar and the negative ناامید na-omid (< MP an-ummed). \"\n   \"The Persian-side chain MP > NP is beyond doubt (MacKenzie 1971 p. 84 is the reference Wiktionary \"\n   \"cites). What is disputed is the far end: Wiktionary/Cheung give Proto-Iranian *hamwatis (*ham- + \"\n   \"*wat- 'be informed'), Nyberg *abi-mati- (from man- 'think'), Horn/Bartholomae *ava-may-. Nourai's \"\n   \"chart NOTE, quoting AEF:147 (Khaleqi Motlaq's Persian version of Horn) that 'the root is not quite \"\n   \"clear', is therefore right, and is the honest reading of the evidence; but the chart nevertheless \"\n   \"draws the arrow from Men 2 as if settled, which modern scholarship does not accept.\",\n   \"«امید» فارسی نو از فارسی میانهٔ ummēd/ōmēt است (أ کشیدهٔ پهلوی در فارسی به ی بدل شده و t پایانی نرم شده)؛ \"\n   \"مشتقات آن «امیدوار» (< ummēdwār) و «ناامید» (< an-ummēd) همین را تأیید می‌کنند؛ تا اینجا جای تردید نیست. \"\n   \"اما سرچشمهٔ کهن‌تر محل اختلاف است: پژوهش امروزی (چونگ، ویکی‌واژه) *ham-wati-، نیبرگ *abi-mati-، و هرن *ava-may- می‌آورند، \"\n   \"هیچ کدام upa-mati- را. خود نورایی در یادداشت نمودار (به نقل از «اساس اشتقاق فارسی» ۱۴۷) می‌پذیرد که \"\n   \"ریشه روشن نیست؛ این یادداشت درست است و پیکان نمودار بیش از اندازه قطعی ترسیم شده است.\",\n   [W_OMID, W_HWT, A_OMID],\n   [{\"ref\":\"MON\",\"status\":\"partial\",\"note\":\"Farhang-e Mo'in s.v. امید (via abadis.ir, archived): '(اُ مّ) (اِ.) ۱ - آرزو. ۲ - چشمداشت.' - the lexicon entry carries no etymological tag at all, so MON supports the word and its meaning but says nothing about the Avestan parent. (Mo'in's etymological note lives in his Borhan footnote: 'in Pahlavi umet, in Pazand umed'.)\"}],\n   [{\"src\":\"MON\",\"where\":\"abadis.ir امید, section فرهنگ معین\",\"stance\":\"silent\",\"note\":\"no origin bracket in the entry; Dehkhoda on the same page quotes Mo'in's Borhan footnote 'in Pahlavi umet, in Pazand umed'.\"},\n    {\"src\":\"PHD\",\"where\":\"p. 84\",\"stance\":\"supports\",\"note\":\"\\\"ummed ['wmyt' | N ~] hope\\\" - MacKenzie's '| N ~' marks NP omid as the direct continuation; this is the citation Wiktionary gives for the MP > NP step.\"},\n    {\"src\":\"HRN\",\"where\":\"no. 109, p. 26\",\"stance\":\"partial\",\"note\":\"Horn lists 'umed \\\"Hoffnung\\\", umid, omed' with phlv. umet/omet and the Kurdish/Afghan/Baluchi cognates, but derives the whole family from *ava + may-, not from man-.\"},\n    {\"src\":\"ARY\",\"where\":\"Farhang-e Rishe-ha-ye Hend-o-Orupayi\",\"stance\":\"silent\",\"note\":\"grep of ARY_pages.txt / ARY_latin_index_pages.txt for امید / UMED / OMID as a headword found no entry (the hits are Aryanpur's own prose).\"}]),\n\n n(7, \"Latin\", \"maněre\",\n   \"confirmed\",\n   \"Latin manere, maneo, mansi, mansum 'to stay, remain' (intr.) and 'to wait for' (tr.), from a \"\n   \"stative *m(V)n-eh1-ye- (Wiktionary/LIV *mn-eh1-ye-ti; the -a- of manere is unexplained, \"\n   \"Ernout-Meillet), matching Gk. menein and the perfect memeneka. The book's breve in 'maněre' is \"\n   \"Nourai's house notation for the stem vowel; the classical quantity is manēre (2nd conjugation, \"\n   \"long ē), and the JSON faithfully reproduces the printed page. Ernout-Meillet make the Iranian \"\n   \"connection explicit: 'la racine existe aussi en iranien, et notamment dans persan mandan \"\n   \"\\\"rester\\\"', which is exactly the sibling relation Nourai draws.\",\n   \"لاتینی manēre (مضارع maneō) «ماندن، منتطر ماندن» از ستاک حالتی *mn-eh₁-ye- است و برابر یونانی ménō \"\n   \"و هم‌ریشهٔ ماندن فارسی است؛ ارنو-مییه خود می‌نویسد «این ریشه در ایرانی هم هست، به‌ویژه در ماندن فارسی». \"\n   \"نشانهٔ کوتاهی روی e در «maněre» قرارداد نگارشی خود نورایی است (صورت کلاسیک manēre با أ کشیده)، و خوانش اسکن درست است. \"\n   \"ادعای نورایی درست است.\",\n   [E_MANS, W_MEN],\n   [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt s.v. men-3: 'men-3. To remain. Variant suffixed (stative) form *man-e- in Latin manere, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.]'\"},\n    {\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966.txt p. 934 s.v. 'mansion': 'fr. mansus, pp. of manere, \\\"to stay, remain\\\" ... fr. I.-E. base *men-, \\\"to remain, wait for\\\"'.\"}],\n   [{\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. maneo (LAT.txt lines 36174-36216)\",\"stance\":\"supports\",\"note\":\"'maneo, -es, mansi, mansum, -ere: 1o rester ...; 2o attendre ... la racine existe aussi en iranien, et notamment dans persan mandan \\\"rester\\\"; av. mąnaya- suppose manaya-.'\"},\n    {\"src\":\"POK\",\"where\":\"p. 729\",\"stance\":\"supports\",\"note\":\"'Latin maneo, -ere (compare memene-ka) \\\"to stay, remain, abide, tarry\\\" (*meneio), Denomin. mantare'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p. 267\",\"stance\":\"supports\",\"note\":\"lat. maneo is listed in the men- 'bleiben' article alongside av. ap. man- (WLD_Bd2_pages.txt block 271).\"}]),\n\n n(8, \"English\", \"mansion, permanent, remain\",\n   \"confirmed\",\n   \"All three come through French from manere. mansion: L. mansio, -onis 'a staying, night quarters' \"\n   \"(noun of action from the pp. stem mans-) > OF mansion 'stay, abode' (13c.) > ME mansioun (mid-14c.) \"\n   \"'chief residence of a lord' > mansion; the same L. word gave OF/F maison 'house'. permanent: L. \"\n   \"permanens, pres. part. of permanere (per- 'through' + manere) > MF permanent > late ME. remain: L. \"\n   \"remanere 'to stay behind' > OF remaindre/remanoir > ME remainen (with the stem of the stressed \"\n   \"forms generalised) > remain; the doublet remnant is from the OF pres. part. remanant.\",\n   \"هر سه واژهٔ انگلیسی از راه فرانسه از manēre لاتین آمده‌اند: mansion از mansiō «درنگ، منزلگاه» \"\n   \"از ستاک اسم مفعول mans- وارد فرانسهٔ کهن و سپس انگلیسی میانه شده (همین واژه maison فرانسوی را هم داده)؛ \"\n   \"permanent از اسم فاعل permanens (per- + manēre)؛ و remain از remanere «بر جای ماندن» از راه remaindre \"\n   \"فرانسهٔ کهن. ادعای نورایی درست است و زنجیره از نوع جاافتاده‌ترین است.\",\n   [E_MANS],\n   [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference of its own; it inherits AHD; KLN from its Latin parent, both of which list MANSION / PERMANENT / REMAIN among the derivatives of manere.\"}],\n   [{\"src\":\"KLN\",\"where\":\"p. 934 s.v. mansion; p. 1129 s.v. permanent; p. 1330 s.v. remain\",\"stance\":\"supports\",\"note\":\"'mansion ... Cp. manor, manse, immanent, ... permanent, remain, remnant'; 'remain, intr. v. - ME. remainen, fr. OF. remaindre, remanoir ... fr. L. remanere ... fr. re- and manere. See mansion'.\"},\n    {\"src\":\"SKT\",\"where\":\"s.v. Remain\",\"stance\":\"supports\",\"note\":\"Skeat's cross-reference 'Remain; see Mansion' (SKT.txt line 15919) puts the two under one head.\"},\n    {\"src\":\"AHD\",\"where\":\"s.v. men-3\",\"stance\":\"supports\",\"note\":\"lists MANOR, MANSE, MANSION, (MENAGE), IMMANENT, PERMANENT, REMAIN as the English derivatives.\"}]),\n]\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Men 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *men- 'to stay, remain, stand still' (Pokorny 5. men- 729; LIV 2.*men-)\",\n \"note\": (\"Root, language label and gloss are all right: Pokorny's 5. men- 'bleiben, stillestehn' stands \"\n          \"on p. 729, exactly the page Nourai cites, and AHD men-3 'To remain' refers to the same \"\n          \"[Pok. 5. men- 729]. Pokorny himself adds the query '(= men- \\\"think\\\"?)', and Kent (p. 202) \"\n          \"calls the 'remain' root 'probably a specialization of pIE *men- \\\"think\\\"'; Buck (12.16) \"\n          \"insists the two 'are to be distinguished ... even though they may be ultimately the same'. \"\n          \"Nourai's separate numbering therefore reflects the majority practice. \"\n          \"On the root box's own NOTE ('BQT:1949 claims this word is ultimately from root \\\"Dem:house\\\"'): \"\n          \"Mo'in's footnote on Borhan p. 1949 s.v. مان does say that Pahlavi man 'house' replaced \"\n          \"Avestan *nmana- (which is indeed from *dem- 'house') and adds 'و «ماندن» \"\n          \"فارسی نیز ازهمین ریشه است' - so Nourai reports him fairly. But on the very next page \"\n          \"(1950) Mo'in's own footnote on ماندن gives Old Iranian *man- (Bartholomae 1126), \"\n          \"OP/Av. man- 'to wait', Lat. maneo, Gk. meno - i.e. Nourai's root. Every other authority \"\n          \"(Bartholomae, Horn, Kent, Klein, Buck, Mann, Nyberg, Wiktionary) puts mandan under *men- \"\n          \"'remain'; Wiktionary's Proto-Iranian *(d)man- only concedes possible contamination with the \"\n          \"'house' word. Nourai is right to keep the two apart. The extraction of this page is faithful \"\n          \"to the printed chart in every box.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *men- «ماندن، بر جای ایستادن» همان men- پنجم پوکورنی \"\n             \"(ص ۷۲۹) است؛ برچسب زبانی و معنای نمودار هر دو درستند. خود پوکورنی و کنت احتمال می‌دهند \"\n             \"که این ریشه در نهایت همان *men- «اندیشیدن» باشد، ولی باک (Buck) تأکید می‌کند که باید جدا شمرده شوند. \"\n             \"دربارهٔ یادداشت نمودار: درست است که معین در حاشیهٔ برهان قاطع (ص ۱۹۴۹، ذیل «مان») «ماندن» را \"\n             \"به همان ریشهٔ mān «خانه» می‌برد، اما در صفحهٔ پسین (۱۹۵۰، ذیل «ماندن») خود او ایرانی باستان *man- \"\n             \"«انتطار کشیدن» را می‌آورد؛ پژوهش امروزی نیز همین را می‌گوید. دو گرهٔ «امید» (۵ و ۶) تنها کاستی \"\n             \"جدی این نمودارند.\"),\n \"sources\": [W_MEN, W_MAND, E_MANS],\n \"ref_check\": [{\"ref\":\"POK:729\",\"status\":\"supports\",\"note\":POK729}],\n \"consulted\": [\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. men-3\",\"stance\":\"supports\",\"note\":\"'men-3. To remain ... [Pok. 5. men- 729]' - same root, same Pokorny page.\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. II p. 267\",\"stance\":\"supports\",\"note\":\"'5. men- \\\"bleiben, stillestehn\\\" (= men \\\"denken\\\"? s. u.)' with av. ap. man-, gr. meno, lat. maneo, arm. mnam.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann s.v. 'mno, io (mon-) (3) \\\"remain\\\"'\",\"stance\":\"supports\",\"note\":\"'WP II, 267 ... Av. man-, v. \\\"remain\\\", OPer. man-, id.; Per. manam, inf. mandan, id.'\"},\n   {\"src\":\"SYN\",\"where\":\"12.16 REMAIN, STAY, WAIT\",\"stance\":\"supports\",\"note\":\"'1. IE *men- \\\"remain\\\", to be distinguished from *men- \\\"think\\\", even though they may be ultimately the same.'\"},\n   {\"src\":\"BQT\",\"where\":\"vol. 4 pp. 1949-1950 (pdf 32-33)\",\"stance\":\"partial\",\"note\":\"p. 1949 s.v. مان links NP ماندن to Pahlavi mān 'house' ('و «ماندن» فارسی نیز ازهمین ریشه است، اسشق ۹۹۴'), which is what Nourai's root note reports; p. 1950 s.v. ماندن gives Old Iranian *man- 'to wait' instead.\"},\n ],\n \"nodes\": e0_nodes,\n}\n\n# ------------------------------------------------------------------ entry 1\ne1_nodes = [\n n(1, \"Avestan\", \"mati, mnti; fra-manyente\",\n   \"confirmed\",\n   \"Both items are genuine and both belong to this root. (a) Av. matay-/maiti- m. 'mountain spur, \"\n   \"promontory' is a headword in Bartholomae's AiW col. 1112 - 'Vorsprung (des Gebirgs), promunturium', \"\n   \"attested upa maitim ... 'on a spur of the mountain range' V.6.10 - with Bartholomae's own note \"\n   \"'Zum V. 3man-; lat. vgl. mont-is'. (b) Av. fra-manyente 'they gain a lead' is Yt 10.20 (vazǝntō \"\n   \"nōit framanyente 'driving they gain no head start'), and Bartholomae sets up a whole verb for it: \"\n   \"'3man- V., nur mit fra \\\"Vorsprung gewinnen\\\"'. Pokorny p. 726 and Klein p. 1009 quote precisely \"\n   \"these two forms, and Klein's wording ('Avestic mati- (for *mnti-)') explains the chart's second \"\n   \"item: 'mnti' is the PIE zero-grade *mn-ti- reconstructed behind mati-, not a second Avestan word - \"\n   \"Nourai's habit of printing the reconstruction beside the attested form without an asterisk.\",\n   \"دو واژهٔ این گره هر دو در اوستا گواه دارند: matay-/maiti- «دماغه، پشته، برآمدگی کوه» \"\n   \"(وندیداد ۶/۱۰؛ بارتولومه ستون ۱۱۱۲ که خود می‌نویسد از ریشهٔ man- سوم و هم‌ریشهٔ mons لاتینی است) و \"\n   \"framanyente «پیش می‌افتند، جلو می‌زنند» (یشت ۱۰/۲۰). پوکورنی (ص ۷۲۶) و کلاین (ص ۱۰۰۹) همین دو را \"\n   \"می‌آورند. تنها نکته این که «mnti» واژهٔ اوستایی دیگری نیست، بلکه صورت بازسازی‌شدهٔ *mn̥-ti- است که \"\n   \"نورایی بر پایهٔ کلاین بی‌ستاره نوشته است. ادعای نورایی درست است.\",\n   [W_MONS],\n   [{\"ref\":\"POK:726\",\"status\":\"supports\",\"note\":POK726},\n    {\"ref\":\"KLN:1009\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 541-542 (printed p. 1009) s.v. 'mount, n.': '... fr. I.-E. base *men-, \\\"to stand out, project\\\" ... and possibly also Avestic mati- (for *mnti-), \\\"promontory\\\", fra-manyente, \\\"they get a head start\\\"' - Nourai's glosses are a verbatim borrowing from Klein, including 'they get a head start'.\"}],\n   [{\"src\":\"BRT\",\"where\":\"col. 1112 s.v. 2matay- and col. 1125 s.v. 3man- (BRT.txt lines 19566, 19752)\",\"stance\":\"supports\",\"note\":\"'2matay- m. \\\"Vorsprung (des Gebirgs), promunturium\\\": ... upa maitim ... V.6.10 ... Zum V. 3man-; - lat. vgl. mont-is'; '3man- V., nur mit fra \\\"Vorsprung gewinnen\\\". Praes. manya-'; and Yt 10.20 'vazǝntō nōit framanyente \\\"fahrend gewinnen sie keinen Vorsprung\\\"'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p. 263\",\"stance\":\"supports\",\"note\":\"'1. men- \\\"emporragen\\\". Av. framanyente \\\"sie gewinnen Vorsprung\\\", mati- \\\"Vorsprung des Gebirges\\\" (: pro-minere; Bartholomae Airan. Wb. 1112, 1125)' - Walde-Pokorny even give the AiW columns.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann s.v. moghent-\",\"stance\":\"partial\",\"note\":\"Mann mentions 'Av. matis \\\"cliff, peak\\\" for possible variant *mnt-' but only as a side note while assigning Latin mons to a different root.\"}]),\n\n n(2, \"Latin\", \"mont\",\n   \"confirmed\",\n   \"Latin mons, gen. montis, m. 'mountain' - the chart's 'mont' is the oblique stem, Nourai's usual \"\n   \"citation form. It goes back to a suffixed o-grade *mon-ti- (Wiktionary *montis; Pokorny calls the \"\n   \"attested paradigm a 'hybridization from *montos and *mnti-'), i.e. the same formation as Av. \"\n   \"matay-. Ernout-Meillet: 'il y a une racine *men- \\\"etre saillant\\\" representee en latin meme par \"\n   \"mons ... et par monile'. Dissent to record: Mann (IEC) prints Latin mons under *moghent- 'big, \"\n   \"great, strong' beside Skt. mahat, calling the -ti- formation secondary; that is a minority view \"\n   \"against Pokorny, Walde-Hofmann, Ernout-Meillet, Watkins, Klein and Etymonline.\",\n   \"لاتینی mōns (مضاف montis) «کوه»؛ شکل «mont» در نمودار همان ستاک مایل است. از ساخت *mon-ti- با \"\n   \"درجهٔ o ریشه، یعنی همان ساختی که در matay- اوستایی دیده می‌شود؛ ارنو-مییه روشن می‌گوید که ریشهٔ *men- \"\n   \"«برآمدن، بیرون زدن» در خود لاتین با mons و monile نماینده دارد. ادعای نورایی درست است؛ فقط منّ (Mann) \"\n   \"در فرهنگ تطبیقی خود mons را به ریشهٔ *moghent- «بزرگ» می‌برد که رأیی اقلیتی است.\",\n   [E_MOUNT, W_MONS],\n   [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt s.v. men-2: '4. Suffixed o-grade form *mon-ti- in Latin mons (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT1, MOUNT2, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726 ...]'\"}],\n   [{\"src\":\"POK\",\"where\":\"p. 726 (men-1)\",\"stance\":\"supports\",\"note\":\"'mons, -tis \\\"a mountain, mount, range of mountains\\\" (hybridization from *montos and *mnti-)'.\"},\n    {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. minae/emineo (LAT.txt lines 38067-38075)\",\"stance\":\"supports\",\"note\":\"'Car il y a une racine *men- \\\"etre saillant\\\" representee en latin meme par mons (v. ce mot) et par monile, peut-etre aussi par mentum'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p. 263\",\"stance\":\"supports\",\"note\":\"under 1. men- 'emporragen': 'mons, -tis \\\"Berg\\\" (in die i-Dekl. ubergefuhrtes *monios)'.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann s.v. moghent-\",\"stance\":\"contradicts\",\"note\":\"'Lat. prob. mons, gs montis ... \\\"mountain; mass, quantity\\\" (but cf. Av. matis \\\"cliff, peak\\\" for possible variant *mnt-)' - Mann files mons under 'big, great, strong', not under 'project'.\"}]),\n\n n(3, \"French\", \"\",\n   \"confirmed\",\n   \"Pass-through node: Old French / French mont 'hill, mountain', the direct popular continuation of \"\n   \"Latin montem (acc.), attested from the 11th c. (Chanson de Roland) and productive in compounds and \"\n   \"toponyms (a mont > amont 'upstream, uphill', Mont-Royal, Mont-Saint-Michel). The box is deliberately \"\n   \"empty on the printed page - Nourai leaves the form implicit because it is identical with the Latin \"\n   \"stem he has just given.\",\n   \"گرهٔ گذری: فرانسهٔ کهن و فرانسهٔ نو mont «کوه، تپه» دنبالهٔ مستقیم montem لاتینی است و از سدهٔ \"\n   \"یازدهم گواه دارد؛ در نام‌جاها و ترکیبها (amont، Mont-Royal) زایا بوده است. جعبهٔ این گره در کتاب \"\n   \"چاپی خالی است و خوانش اسکن درست است؛ نورایی صورت فرانسوی را به قرینهٔ ستاک لاتین واگذاشته است.\",\n   [E_MOUNT],\n   [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference; it inherits AHD from the Latin parent, which lists MONTE/MOUNT/MOUNTAIN as the Romance-mediated derivatives.\"}],\n   [{\"src\":\"KLN\",\"where\":\"p. 1009 s.v. mount, n.\",\"stance\":\"supports\",\"note\":\"'ME. mont, mount, partly fr. OE. munt (fr. L. montem), partly fr. OF. (= F.) mont, \\\"hill, mountain\\\", fr. L. montem, acc. of mons'.\"},\n    {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. mons\",\"stance\":\"supports\",\"note\":\"the article gives the Romance continuations of mons/montem (M.L. references) as the regular popular development.\"}]),\n\n n(4, \"Persian\", \"\",\n   \"plausible\",\n   \"The four Persian forms printed here are 20th-c. transcribed proper names: مونترال Montreal, \"\n   \"مونتکارلو Monte Carlo, مونتگمری Montgomery, پارامونت Paramount. Each does contain the \"\n   \"mont- element, so the root claim is right, but 'French' as the single immediate parent is only \"\n   \"partly true. Montreal is French (Mont Royal, the hill named by Cartier 1535; the city founded 1642) \"\n   \"and reached Persian through French. Monte Carlo is ITALIAN monte (the quarter was named in 1866 \"\n   \"for Charles III of Monaco), not French. Montgomery is a Norman-French toponym of Normandy \"\n   \"('Gomeric's hill', mont + the Germanic name Gumaric) that became an English surname and reached \"\n   \"Persian through English. Paramount is English, from Anglo-French/OF paramont (par + a mont \"\n   \"'uphill'), and in Persian is the film-studio name, borrowed from English. So: correct root, \"\n   \"loose intermediary.\",\n   \"چهار نام فارسی این جعبه همه وام‌واژهٔ سدهٔ بیستم و از نوع «نام خاص» اند: «مونترال» از فرانسه \"\n   \"(Mont Réal)، «مونت‌کارلو» از ایتالیایی monte و نام کارلوس سوم (۱۸۶۶)، «مونتگمری» از نام‌جایی در نورماندی \"\n   \"(mont + نام ژرمنی Gumaric) که از راه انگلیسی رسیده، و «پارامونت» وام‌واژهٔ انگلیسی (paramount < par + amont). \"\n   \"پس ریشه درست است اما «فرانسه» به تنهایی واسطهٔ درست همهٔ آنها نیست؛ با احتیاط پذیرفتنی است.\",\n   [A_MTRL, W_MC, W_MG, E_PARA],\n   [{\"ref\":\"MON\",\"status\":\"not_checked\",\"note\":\"the local Mo'in files (MON_part1/2, MON_2vol_Adena) are the lexicon volumes; مونترال / مونتکارلو / مونتگمری / پارامونت are proper names, i.e. Mo'in vols 5-6 (a'lam), which are not on disk and are not carried by vajehyab/abadis. grep of all four spellings in every local MON file returned 0 hits.\"}],\n   [{\"src\":\"MON\",\"where\":\"abadis.ir مونترال (encyclopaedic entry, archived)\",\"stance\":\"partial\",\"note\":\"'فرانسوی ها در ۱۶۴۲ مونترال را تأسیس کردند؛ در ۱۷۶۳ به تملک بریتانیا درآمد. مونترال دومین شهر بزرگ فرانسوی زبان پس از پاریس است' - confirms the French route for this one name only.\"},\n    {\"src\":\"KLN\",\"where\":\"p. 1009 s.v. mount, n. (list of cognate derivatives)\",\"stance\":\"supports\",\"note\":\"Klein's own cross-reference list under mount includes 'monte, mont-de-piete, paramount, ... rodomontade', i.e. the Italian and English mont- names belong to this root.\"},\n    {\"src\":\"LKT\",\"where\":\"Lokotsch, Etym. Wb. der europ. Worter orientalischen Ursprungs\",\"stance\":\"silent\",\"note\":\"grep found nothing: Lokotsch covers oriental words in European languages, i.e. the opposite direction, so it has nothing on European proper names entering Persian.\"}]),\n\n n(5, \"English\", \"mount, mountain, amount, paramount, piedmont\",\n   \"confirmed\",\n   \"All five are mont- words that entered English from French (with a partial native reinforcement in \"\n   \"mount). mount 'hill': late OE, from Anglo-French/OF mont and partly OE munt, both < L. montem. \"\n   \"mountain: ME mountaine < OF montaigne < VL *montanea (fem. of montaneus 'mountainous'). amount \"\n   \"(vb., late 13c.): OF amonter, from amont 'uphill' = a mont (L. ad + montem); the modern 'sum' sense \"\n   \"is a 16c. development of 'rise to'. paramount (1530s): AF paramont / OF paramont 'above', par (L. \"\n   \"per) + amont. piedmont: It. Piemonte 'foot of the mountain' (pie 'foot' + monte), used of the \"\n   \"Appalachian foreland from the 19c. Klein p. 1009 lists mount, mountain, amount and paramount \"\n   \"together under this base.\",\n   \"هر پنج واژه از راه فرانسه به انگلیسی رسیده‌اند: mount از mont فرانسهٔ کهن (با تقویت از munt \"\n   \"انگلیسی کهن)، mountain از montaigne از لاتین عامیانهٔ *montanea، amount از amonter (a mont «سربالا»)، \"\n   \"paramount از par + amont فرانسهٔ کهن، و piedmont از Piemonte ایتالیایی «پای کوه». تحول معنایی amount \"\n   \"از «بالا رفتن» به «مبلغ، مقدار» در سدهٔ شانزدهم رخ داده. ادعای نورایی درست است.\",\n   [E_MOUNT, E_PARA],\n   [{\"ref\":\"KLN:1009\",\"status\":\"supports\",\"note\":\"KLN_1966.txt p. 1009 s.v. 'mount, n.' ends 'Cp. mount, v., mountain. Cp. also adminicle, amenable, amount, ... paramount, prominent, promontory, rodomontade' - Nourai's English list is drawn from that page.\"}],\n   [{\"src\":\"AHD\",\"where\":\"s.v. men-2\",\"stance\":\"supports\",\"note\":\"'MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT1, MOUNT2, MOUNTAIN; AMOUNT, ULTRAMONTANE'.\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat s.v. Mount, Mountain\",\"stance\":\"supports\",\"note\":\"Skeat refers mount and mountain to L. mons, montis, and amount to OF amonter.\"}]),\n\n n(6, \"Latin\", \"miněre\",\n   \"plausible\",\n   \"The meaning and the root are right, but the form is a grammarian's abstraction: there is no \"\n   \"independent Latin verb *minere. The verb is attested only in the compounds e-mineo 'stand out', \"\n   \"im-mineo 'overhang, threaten', pro-mineo 'jut out'; Watkins therefore prints it with a hyphen, \"\n   \"'Latin -minere, to project', and Ernout-Meillet warn that Lucretius' eminent 'ne suffit pas a \"\n   \"garantir un ancien *mineo'. Phonologically it is a zero-grade stative *mn-eh1-ye- > Proto-Italic \"\n   \"*menezo > (compound) -mineo, the i coming partly from the unstressed medial syllable and partly \"\n   \"from analogy with minor 'threaten'. Nourai's dropping of the hyphen makes an unattested Latin \"\n   \"lemma look attested; the derivation itself is sound.\",\n   \"معنا و ریشه درست، اما صورت مستقل minēre در لاتین گواه ندارد؛ این فعل تنها در ترکیب‌های \"\n   \"مرکب دیده می‌شود: ē-mineō، im-mineō، prō-mineō. واتکینز در پیوست فرهنگ میراث امریکایی آن را با \"\n   \"خط پیوند «-minēre» می‌نویسد و ارنو-مییه هشدار می‌دهد که شاهد لوکریتیوس برای وجود *mineō کافی نیست. ساخت \"\n   \"آن ستاک حالتی درجهٔ صفر *mn̥-eh₁-ye- است؛ افتادن خط پیوند در نمودار تنها کاستی این گره است: \"\n   \"با احتیاط پذیرفتنی است.\",\n   [E_PROM, W_MEN],\n   [{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"AHD_watkins1985.txt s.v. men-2: '3. Latin -minere, to project, jut, threaten: EMINENT, IMMINENT, PROMINENT.' Watkins' leading hyphen marks exactly what the chart omits - the verb exists only in compounds.\"}],\n   [{\"src\":\"POK\",\"where\":\"p. 726\",\"stance\":\"partial\",\"note\":\"Pokorny lists only the compounds: 'Latin e-mineo, -ere ..., im-minere ..., pro-minere ...; from these compounds are probably consecutive words ... minae, minor, -ari, minax'.\"},\n    {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. minae (LAT.txt lines 38067-38075)\",\"stance\":\"partial\",\"note\":\"'l'eminent de Lucrece ne suffit pas a garantir un ancien *mineo: la forme peut etre tiree de eminero, promineo, etc., qui sont courants'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p. 263\",\"stance\":\"partial\",\"note\":\"'lat. emineo, -ere \\\"heraus-, hervorragen\\\", imminere ..., prominere ...; aus diesen Zs. ist wohl ... auch das i folgender Worte zu erklaren' - again only the compounds.\"}]),\n\n n(7, \"English\", \"prominent, eminent, imminent\",\n   \"confirmed\",\n   \"Learned Latinate borrowings of the present participles of the three compounds: prominent (mid-15c.) \"\n   \"< L. prominentem, ppr. of prominere (pro- 'forward' + -minere); eminent (mid-15c.) < L. eminentem \"\n   \"'standing out, projecting', whence the figurative 'distinguished'; imminent (1520s) < L. imminentem \"\n   \"'overhanging, impending', with the semantic slide 'hanging over' > 'about to happen'. All three \"\n   \"came in through Middle French as well as directly from Latin, in the fifteenth-century wave of \"\n   \"learned loans, and none passed through a popular French stage.\",\n   \"هر سه واژه وام‌واژهٔ عالمانه از اسم فاعل همان سه فعل مرکب لاتین اند: prominent از prōminentem، \"\n   \"eminent از ēminentem «برآمده» که معنای مجازی «برجسته، نامدار» گرفته، و imminent از imminentem \"\n   \"«فروافتاده بر سر» با تحول معنایی «بر سر آویخته» > «نزدیک، قریب‌الوقوع». همه در سدهٔ پانزدهم و شانزدهم \"\n   \"میلادی به انگلیسی راه یافته‌اند. ادعای نورایی درست است.\",\n   [E_PROM],\n   [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference on the node; it inherits AHD from its Latin parent, where the three words are the listed derivatives of -minere ('EMINENT, IMMINENT, PROMINENT').\"}],\n   [{\"src\":\"AHD\",\"where\":\"s.v. men-2, sense 3\",\"stance\":\"supports\",\"note\":\"'Latin -minere, to project, jut, threaten: EMINENT, IMMINENT, PROMINENT.'\"},\n    {\"src\":\"KLN\",\"where\":\"p. 1009 s.v. mount, n.\",\"stance\":\"supports\",\"note\":\"Klein's cross-list under this base includes 'eminent, imminent, ... prominent, promontory'.\"}]),\n\n n(8, \"Indo-European\", \"Mon, Mono\",\n   \"plausible\",\n   \"PIE *mono-/*mon(e)- 'neck, nape' (in derivatives also 'necklace, mane') is a real reconstruction - \"\n   \"Pokorny gives it as a headword on pp. 747-748 and Watkins as 'mon-. Neck, nape of the neck. [Pok. \"\n   \"mono- 747]'. Two reservations. (i) The gloss: every source gives 'neck, nape' (and derivatively \"\n   \"'necklace, mane'); 'throat' appears in none of them, and the *mon- words are all about the outside \"\n   \"of the neck. (ii) The arrow from Men 3: Pokorny does license it, cautiously, at both ends \"\n   \"('related is probably *mono- \\\"nape, neck\\\"' under men- p. 726, and 'compare above S. 726 men- \"\n   \"\\\"tower\\\"' at the end of the mono- article), and Ernout-Meillet argue it semantically ('les notions \"\n   \"de \\\"nuque\\\" [et] de \\\"objet saillant\\\" etant liees, comme on le voit par gr. lophos \\\"colline\\\" et \"\n   \"\\\"nuque\\\"'). But Watkins, Walde-Pokorny, Mann and Etymonline all keep *mon- 'neck' as an \"\n   \"independent root with no derivation from *men- 'project'. So the node is a defensible minority \"\n   \"position, not settled fact.\",\n   \"ریشهٔ بازسازی‌شدهٔ *mono- «گردن، پس‌گردن» (و در مشتقات «گردن‌افزار، یال») واقعی است و \"\n   \"پوکورنی آن را در صفحهٔ ۷۴۷-۷۴۸ مدخل مستقل قرار داده است. دو ایراد: نخست اینکه معنای «نای، گلو» \"\n   \"(throat) در هیچ منبعی نیست؛ دوم اینکه وابستگی این ریشه به Men ۳ تنها احتمالی است: پوکورنی و \"\n   \"ارنو-مییه ان را محتمل می‌دانند ولی واتکینز، والده-پوکورنی و منّ آن را ریشهٔ مستقل می‌شمارند. \"\n   \"پس با احتیاط پذیرفتنی است.\",\n   [E_MANE],\n   [{\"ref\":\"POK:726,747\",\"status\":\"supports\",\"note\":POK747 + \" -- and p. 726 (men-1) ends 'related is probably *mohnoh- \\\"nape, neck\\\"', so both of Nourai's page numbers do carry the claim.\"},\n    {\"ref\":\"KLN:932\",\"status\":\"supports\",\"note\":\"KLN_1966.txt p. 932 s.v. 'mane': '... cogn. with OI. manya, \\\"nape of the neck\\\", Gaul.-Gk. maniakes, mannos, \\\"Celtic necklace\\\", L. monile, \\\"necklace\\\", OSlav. monisto ... All these words prob. derive ult. fr. I.-E. base *men-, \\\"to stand out, project\\\", whence L. eminere ... mons, \\\"mountain\\\". See mount, \\\"hill\\\"' - Klein makes exactly Nourai's subordination.\"}],\n   [{\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. mon-\",\"stance\":\"partial\",\"note\":\"'mon-. Neck, nape of the neck. 1. Germanic *mano in Old English manu, mane: MANE. 2. Latin monile, necklace: MONILIFORM. [Pok. mono- 747.]' - an independent root entry, not a derivative of men-2, and glossed 'neck, nape' only.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p. 305\",\"stance\":\"partial\",\"note\":\"'mono- \\\"Nacken, Hals\\\", in Ableitungen (bes. m. Formans -i, -io-) auch \\\"Halskette, Halsschmuck\\\"' - a separate article, with no reference back to men- 'emporragen' (WLD_Bd2_pages.txt block 309).\"},\n    {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. monile (LAT.txt lines 38860-38870)\",\"stance\":\"supports\",\"note\":\"'Les notions de \\\"nuque\\\" [et] de \\\"objet saillant\\\" etant liees, comme on le voit par gr. lophos \\\"colline\\\" et \\\"nuque\\\" ... On rapprochera donc lat. mons, etc.' - the semantic bridge Nourai's arrow needs.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann s.v. 'mon-, (monio, monuis, monus) \\\"neck, nape; mane\\\"'\",\"stance\":\"partial\",\"note\":\"an independent root entry (Skt. manya, OPer. maniakes, Av. manaothris/minus, Lat. monile) with no link to *men- 'project'.\"}]),\n\n n(9, \"Avestan\", \"minu; manaothri, moneutro\",\n   \"plausible\",\n   \"manaothri- is exactly right; minu- is right in form but wrongly glossed, and 'moneutro' is not an \"\n   \"Avestan word. Av. manaoθrī- f. is a Bartholomae headword, 'Hals, Nacken' - Yt 5.127 upa tǟm \"\n   \"srīrǟm manaoθrīm 'on her beautiful neck', V.13.30 - formed with the lengthened u-suffix, \"\n   \"*mon-eu-tro- (Charpentier), and it is 'moneutro' that Nourai prints beside it: Pokorny's \"\n   \"reconstruction, without its asterisk, listed as if it were a second attested Avestan form (the same \"\n   \"habit as 'mnti' in node 1). Av. minu- is not 'throat' but 'neck-ornament, necklace': WLD 'minu- \"\n   \"\\\"Halsgeschmeide\\\" (u aus avest. ǝ)', Pokorny 'Halsgeschmeide', Mann 'necklace', and the text \"\n   \"itself has minūm baraṭ ... upa tǟm srīrǟm manaoθrīm 'she wore a necklace on her beautiful \"\n   \"neck' (Yt 5.127), plus the compound zaranyo.minav- 'wearing golden neck-jewellery' (Yt 17.57). The \"\n   \"derivation of both from *mon- is uncontroversial; the glosses are the problem, and they are the \"\n   \"book's own (verified on the printed page).\",\n   \"manaoθrī- درست است: مدخلی است در فرهنگ بارتولومه به معنای «گردن، پس‌گردن» (یشت ۵/۱۲۷)؛ \"\n   \"اما «moneutro» واژهٔ اوستایی نیست بلکه صورت بازسازی‌شدهٔ *mon-eu-tro- پوکورنی است که بدون ستاره \"\n   \"چاپ شده. مهم‌تر اینکه minu- معنای «گلو» ندارد، بلکه «گردن‌آویز، گردن‌افزار» است: در یشت ۵/۱۲۷ \"\n   \"minūm baraṭ ... upa tǟm srīrǟm manaoθrīm «گردن‌آویزی را بر گردن زیبای خود داشت» و صفت مرکب \"\n   \"zaranyo.minav- «دارای گردن‌افزار زرین». معنای نمودار خطای خود کتاب است (روی صفحهٔ چاپی وارسی شد)، \"\n   \"نه خطای خوانش اسکن؛ بنابراین گره با احتیاط پذیرفتنی است.\",\n   [E_MANE],\n   [{\"ref\":\"POK:747\",\"status\":\"partial\",\"note\":POK747 + \" -- the page supports the derivation of both words from *mono-, but glosses Av. minu- 'Halsgeschmeide' (neck-ornament), not 'throat', and prints *mon-eu-tro- as a reconstruction, i.e. the chart's 'moneutro' is Pokorny's starred form.\"}],\n   [{\"src\":\"BRT\",\"where\":\"col. 1129 s.v. 2manaoθrī- and s.v. zaranyo.minav- (BRT.txt lines 19761, 27912, 26928)\",\"stance\":\"partial\",\"note\":\"'2manaoθrī- f. \\\"Hals, Nacken\\\", uzw. ahurischer Wesen: minūm baraṭ..arǝdvī sūra..upa tǟm srīrǟm manaoθrīm Yt 5.127'; 'zaranyo.minav- Adj. \\\"der goldenen Halsschmuck tragt\\\"' - manaoθrī- is 'neck', minū- is the ornament worn on it.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. II p. 305\",\"stance\":\"partial\",\"note\":\"'av. minu- \\\"Halsgeschmeide\\\" (u aus avest. ǝ, vgl. Bartholomae IF. 3, 172; airan. Wb. 1186 ...), und mit Hochstufe der u-Formans (Charpentier KZ. 43, 165), manaoθrī \\\"Hals, Nacken\\\"'.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann s.v. mon- 'neck, nape; mane'\",\"stance\":\"partial\",\"note\":\"'Av. cf. manoöris, f. \\\"back of head\\\" beside (variant) minus, m. (\\\"necklace\\\", fr. *mon-)' - again 'necklace', not 'throat'.\"},\n    {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. monile\",\"stance\":\"supports\",\"note\":\"'Derive d'un mot signifiant \\\"nuque\\\", cf. skr. manya \\\"nuque\\\", av. manaothri-, gall. mwnwgl et irl. muinel \\\"cou\\\"' - independent confirmation of Av. manaothri- 'neck'.\"}]),\n\n n(10, \"Germanic\", \"monô\",\n   \"plausible\",\n   \"The Germanic word is real and belongs here, but the citation form and the gloss are both off by \"\n   \"one step. What is reconstructed is Proto-Germanic *manō 'mane' (a-grade), not *monō: Watkins \"\n   \"'Germanic *mano in Old English manu, mane', Walde-Pokorny 'aisl. mǝn, ags. manu, ahd. mana \"\n   \"(Germanic *manō) \\\"Mahne\\\"'. *monō is the PIE o-grade from which the Germanic form descends - \"\n   \"again the reconstruction printed as the attested form. And its meaning in Germanic is 'mane', not \"\n   \"'neck'; the 'neck' sense survives only in the -jan- derivative *manja- (ON men, OE mene, OHG \"\n   \"menni 'necklace'). Ernout-Meillet explain the shift: the word for 'nape' regularly comes to denote \"\n   \"the horse's mane (cf. Slavic griva 'mane' beside Indo-Iranian grīva- 'nape').\",\n   \"واژهٔ ژرمنی درست است و به همین خانواده می‌رسد، اما صورت بازسازی‌شدهٔ ژرمنی آغازین *manō \"\n   \"«یال» است نه *monō (واتکینز: Germanic *manō > انگلیسی کهن manu؛ والده-پوکورنی: aisl. mǝn، ahd. mana). \"\n   \"معنای ژرمنی آن هم «یال» است نه «گردن»؛ معنای «گردن‌بند» در مشتق *manja- (ON men، OE mene، OHG menni) مانده است. \"\n   \"تحول معنایی «پس‌گردن» > «یال» را ارنو-مییه با قیاس grīva- هندوایرانی و griva اسلاوی توضیح می‌دهد. \"\n   \"پس با احتیاط پذیرفتنی است.\",\n   [E_MANE],\n   [{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"AHD_watkins1985.txt s.v. mon-: '1. Germanic *mano in Old English manu, mane: MANE' - the Germanic form is *mano (a-grade) and the gloss is 'mane'; the chart's *mono 'neck' is the PIE preform, not the Germanic word.\"}],\n   [{\"src\":\"WLD\",\"where\":\"Bd. II p. 305\",\"stance\":\"partial\",\"note\":\"'Aisl. men, ags. mene, ahd. menni \\\"Halsgeschmeide\\\", aisl. mǝn, ags. manu, ahd. mana (Germanic *manō) \\\"Mahne\\\"' - two distinct Germanic formations, *manja- 'necklace' and *manō 'mane'.\"},\n    {\"src\":\"POK\",\"where\":\"pp. 747-748\",\"stance\":\"partial\",\"note\":\"same split: 'Old Icelandic men. Old English mene. Old High German menni \\\"Halsgeschmeide\\\", Old Icelandic mgn [mǝn]. Old English manu. Old High German mana (Germanic *mand [*manō]) \\\"mane\\\"'.\"},\n    {\"src\":\"KLN\",\"where\":\"p. 932 s.v. mane\",\"stance\":\"supports\",\"note\":\"'ME. mane, fr. OE. manu, rel. to ON. mon, Dan., Swed. man, OFris. mana, MDu., Du. manen, OHG. mana, MHG. mane, G. Mahne, \\\"mane\\\", OE. mene, OHG. menni, \\\"necklace\\\"'.\"}]),\n\n n(11, \"English\", \"mane\",\n   \"confirmed\",\n   \"English mane < ME mane < OE manu 'mane of a horse' (a fem. n-stem), from Proto-Germanic *manō, \"\n   \"with the regular OE loss of final -ō > -u and no further change beyond ME levelling of the \"\n   \"inflection; cognate ON mǝn, OHG mana, G. Mähne. The sense has stayed 'the long hair on the neck \"\n   \"of horse or lion' throughout, which is why Skeat gives the original sense as 'hair on the neck'.\",\n   \"«mane» انگلیسی از manu انگلیسی کهن «یال اسب» است، از ژرمنی آغازین *manō؛ هم‌ریشه با mǝn \"\n   \"ایسلندی کهن، mana آلمانی عالی کهن و Mähne آلمانی. معنا از آغاز همواره «موی بلند گردن اسب و شیر» \"\n   \"بوده و اسکیت معنای نخستین را «موی روی گردن» می‌داند. ادعای نورایی درست است.\",\n   [E_MANE],\n   [{\"ref\":\"KLN:932\",\"status\":\"supports\",\"note\":\"KLN_1966.txt p. 932: 'mane, n. - ME. mane, fr. OE. manu, rel. to ON. mon, ... and cogn. with OI. manya, \\\"nape of the neck\\\" ... L. monile, \\\"necklace\\\" ... All these words prob. derive ult. fr. I.-E. base *men-, \\\"to stand out, project\\\"'.\"}],\n   [{\"src\":\"SKT\",\"where\":\"Skeat s.v. Mane (SKT.txt line 11032)\",\"stance\":\"supports\",\"note\":\"'Mane. A.S. manu ... Cf. W. myngwn, mane from neck; Irish muin, collar, from neck; Skt. manya, the tendon [of the] nape of the neck; L. monile. Orig. sense \\\"hair on the neck\\\".'\"},\n    {\"src\":\"AHD\",\"where\":\"s.v. mon-\",\"stance\":\"supports\",\"note\":\"'Germanic *mano in Old English manu, mane: MANE.'\"}]),\n]\n\nentry1 = {\n \"entry\": 1,\n \"root\": \"Men 3\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *men- 'to stand out, project, tower' (Pokorny 1. men- 726)\",\n \"note\": (\"Root, label and gloss are correct: Pokorny's 1. men- 'emporragen' is on p. 726, the page \"\n          \"Nourai cites, and Watkins' men-2 'To project' refers to the same [Pok. 1. men- 726]. \"\n          \"Bartholomae independently sets up an Avestan verb for it (3man- 'nur mit fra \\\"Vorsprung \"\n          \"gewinnen\\\"', AiW col. 1125) and a noun matay- 'promontory' (col. 1112), so the Iranian \"\n          \"branch of this chart rests on real material. Two structural remarks. (1) Throughout this \"\n          \"entry Nourai prints PIE reconstructions beside attested forms without an asterisk - 'mnti' \"\n          \"next to Avestan mati- (node 1), 'moneutro' next to manaothri- (node 9), Germanic 'mono' for \"\n          \"*mano (node 10). This is a house convention, verified against the printed page, not an \"\n          \"extraction error, but it makes reconstructions look attested. (2) The subordination of \"\n          \"*mon- 'neck' (node 8) to this root follows Pokorny's cautious 'related is probably' and \"\n          \"Klein p. 932; Watkins, Walde-Pokorny, Mann and Etymonline keep the two roots apart. \"\n          \"The extraction is faithful; the printed chart has two completely EMPTY, unlabelled boxes \"\n          \"(one to the right of node 1, one to the right of node 9), verified at 400 dpi, and the JSON \"\n          \"rightly omits them.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *men- «برآمدن، بیرون زدن، برافراشته بودن» همان men- یکم \"\n             \"پوکورنی (ص ۷۲۶) است و واتکینز نیز men-2 خود را به همین صفحه ارجاع می‌دهد؛ برچسب زبانی و \"\n             \"معنا درستند. بارتولومه هم فعل اوستایی man- سوم (تنها با fra-، «پیش افتادن») و اسم matay- \"\n             \"«دماغه، برآمدگی کوه» را مستقلاً مدخل کرده است. دو نکته: نورایی در این نمودار صورت‌های \"\n             \"بازسازی‌شده را بدون ستاره پهلوی صورت‌های گواه‌دار می‌نویسد (mnti، moneutro، mono) که قرارداد \"\n             \"خود اوست و خطای خوانش اسکن نیست؛ و زیرمجموعه کردن ریشهٔ *mon- «گردن» به این ریشه تنها احتمالی \"\n             \"است. دو جعبهٔ کاملاً خالی نیز در صفحهٔ چاپی هست که درست از داده حذف شده‌اند.\"),\n \"sources\": [E_MOUNT, E_PROM, E_MANE, W_MONS, W_MEN],\n \"ref_check\": [{\"ref\":\"POK:726\",\"status\":\"supports\",\"note\":POK726}],\n \"consulted\": [\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. men-2\",\"stance\":\"supports\",\"note\":\"'men-2. To project. ... 3. Latin -minere, to project, jut, threaten: EMINENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin mons (stem mont-), mountain ... [Pok. 1. men- 726, 2. menth- 732.]'\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. II p. 263\",\"stance\":\"supports\",\"note\":\"'1. men- \\\"emporragen\\\". Av. framanyente \\\"sie gewinnen Vorsprung\\\", mati- \\\"Vorsprung des Gebirges\\\" (: pro-minere; Bartholomae Airan. Wb. 1112, 1125) ... lat. emineo ... mons, -tis \\\"Berg\\\"'.\"},\n   {\"src\":\"BRT\",\"where\":\"cols. 1112, 1125\",\"stance\":\"supports\",\"note\":\"'2matay- m. \\\"Vorsprung (des Gebirgs), promunturium\\\" ... Zum V. 3man-; - lat. vgl. mont-is'; '3man- V., nur mit fra \\\"Vorsprung gewinnen\\\"'.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann, s.v. moghent- and mon-\",\"stance\":\"partial\",\"note\":\"Mann assigns Latin mons to *moghent- 'big, great, strong' and treats mon- 'neck, nape; mane' as an independent root; he thus dissents from two of this chart's links while noting 'Av. matis \\\"cliff, peak\\\"'.\"},\n   {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.vv. minae, monile\",\"stance\":\"supports\",\"note\":\"'il y a une racine *men- \\\"etre saillant\\\" representee en latin meme par mons ... et par monile'; and s.v. monile the semantic bridge 'nuque' ~ 'objet saillant' with 'On rapprochera donc lat. mons'.\"},\n ],\n \"nodes\": e1_nodes,\n}\n\nout = {\n \"pdf_page\": 333,\n \"book_page\": 303,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [entry0, entry1],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-333.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build333.py"
}
```


### [2026-09-07T16:40:45.987Z] TOOL RESULT

```
written
```


## [2026-09-07T16:40:52.598Z] TOOL CALL #109: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-333.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 333"
}
```


### [2026-09-07T16:40:53.956Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'confirmed': 11, 'plausible': 6, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'partial': 6, 'not_checked': 4}
books consulted: {'supports': 35, 'partial': 19, 'silent': 5, 'contradicts': 4} | by book: {'WLD': 8, 'POK': 6, 'AHD': 6, 'LAT': 6, 'IEC': 5, 'KLN': 5, 'BRT': 4, 'PHD': 3, 'HRN': 3, 'MON': 3, 'SKT': 3, 'SYN': 2, 'NYB': 2, 'BQT': 2, 'ARY': 2, 'CHEUNG': 2, 'LKT': 1}
```


## [2026-09-07T16:40:59.100Z] TOOL CALL #110: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\narch=set()\nfor line in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: arch.add(json.loads(line)['url'])\n    except Exception: pass\nd=json.load(open('data/verification/page-333.json'))\nused=set()\nfor e in d['entries']:\n    used.update(e.get('sources',[]))\n    for n in e['nodes']: used.update(n.get('sources',[]))\nmissing=[u for u in used if u not in arch]\nprint('used',len(used),'missing',missing)\nEOF"
}
```


### [2026-09-07T16:41:00.471Z] TOOL RESULT

```
used 15 missing []
```


## [2026-09-07T16:41:08.431Z] TOOL CALL #111: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg333.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/333.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/333.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS/"
}
```


### [2026-09-07T16:41:08.509Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70886 Sep  7 12:41 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/333.png

/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS/:
total 1428
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  7 12:18 .
drwxrwxr-x 12 sfmqrb sfmqrb    4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb    1389 Sep  4 16:10 14.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  410799 Sep  6 11:23 299.png
-rw-rw-r--  1 sfmqrb sfmqrb    1281 Sep  6 11:23 299.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1220 Sep  4 15:51 6.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1021826 Sep  7 12:18 74.png
-rw-rw-r--  1 sfmqrb sfmqrb    1450 Sep  7 12:18 74.vision.txt
```


## [2026-09-07T16:41:36.004Z] AGENT

Done. `data/verification/page-333.json` written; `verify_check.py 333` reports **19/19 nodes, 0 PROBLEM lines**.

**Page 333 (book 303) — verdicts**
- Roots: 2 confirmed (Men 2 = Pokorny 5. men- 729; Men 3 = Pokorny 1. men- 726 — both page numbers exact)
- Nodes: 11 confirmed, 6 plausible, 2 disputed
- Ref checks: 14 supports, 6 partial, 4 not_checked · Books consulted: 35 supports, 19 partial, 5 silent, 4 contradicts

**Disputed**
- Men 2 #5 `ômĕd` (Pahlavi 'hope') — word is real (`'wmyt'`), but the parent isn't. Nyberg: `*abi-mati-` from man- *"think"*; Horn/Bartholomae: `*ava-may-`; current standard (Wiktionary via Cheung 2007 s.v. `*u̯at`): PIr `*ham-wati-`, cf. Parthian hmwd- 'believe', CSogd. ʾnwth 'hope'. Nourai's Av. upa-mati- route is Kanga's old proposal.
- Men 2 #6 `omîd` — MP→NP step certain; the Avestan ancestry is not. Nourai's own chart NOTE (AEF:147, "root not quite clear") is correct and the arrow is drawn more firmly than the evidence allows.

**Plausible (with reasons)**
- Men 2 #4 `upa-mati` — Av. upa.maiti- 'waiting' is attested (V.5.53), but the gloss "keep the hopes up" is not.
- Men 3 #4 Persian names — root right, intermediary loose: Monte Carlo is Italian, Montgomery/Paramount came via English, only Montreal via French.
- Men 3 #6 `miněre` — no independent Latin verb; attested only in ē-/im-/prō-mineō (Watkins prints "-minēre"; Ernout-Meillet warn against *mineō).
- Men 3 #8 `Mon, Mono` — real root, but glossed 'neck, nape' everywhere, never 'throat'; subordination to *men- follows Pokorny's "probably" + Klein, while Watkins, Walde-Pokorny, Mann and Etymonline keep it separate.
- Men 3 #9 `minu` — means 'necklace, neck-ornament' (Yt 5.127; WP II 305; Mann), not 'throat'; 'moneutro' is Pokorny's `*mon-eu-tro-` printed without its asterisk.
- Men 3 #10 `monô` — Germanic form is `*manō` 'mane'; `*monō` is the PIE o-grade, and the Germanic sense is 'mane', not 'neck'.

**Notable ref findings**
- SNS:74 checked from the page image (OCR unusable): it heads the ōmēd entry with `*ava + √may- (GNPE 26)` and gives upa+mati only as "پروفسور کانگا … میداند". Reading saved to `data/verification/sources/refs/ocr/SNS/74.vision.txt` + `74.png`.
- BQT:1950 (vol. 4 pdf 33, offset +1917 confirmed by running heads) fully supports the māndan chain: "ایرانی باستان *man- «پارتولمه ۱۱۲۶» … لاتینی maneō، یونانی ménō".
- The root-box note is fair to BQT:1949 (Mo'in does tie ماندن to mān 'house' = Av. nmāna- < *dem-), but Mo'in contradicts himself on p. 1950, and every other authority puts māndan under *men-. Nourai is right to keep them apart.
- BRT does have Av. `²matay-` 'promунturium' (col. 1112) and a dedicated `³man-` "nur mit frā 'Vorsprung gewinnen'" (col. 1125) — the Iranian side of Men 3 is solid.

**No extraction errors.** The JSON matches the printed chart box for box. Two notes for the owner: (1) the printed page has two completely empty, unlabelled boxes (right of Men 3 #1 and #9), verified at 400 dpi — the JSON rightly omits them; (2) printing PIE reconstructions without asterisks beside attested forms (`mnti`, `moneutro`, `monô`, and `maněre`/`miněre` breves) is Nourai's own house convention, faithfully extracted. Page PNG archived at `data/verification/sources/refs/ocr/BOOK/333.png`; 15 web sources archived via `fetch_source.py`.
