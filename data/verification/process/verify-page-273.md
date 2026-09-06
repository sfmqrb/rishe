# Verification process log — verify-page-273


## [2026-09-06T21:09:16.945Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 273 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-273.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-273.json. Write /home/sfmqrb/git/rishe/data/verification/page-273.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 273` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:09:18.540Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:09:19.254Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:09:19.274Z] TOOL RESULT

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


## [2026-09-06T21:09:19.505Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-273.txt"
}
```


### [2026-09-06T21:09:19.534Z] TOOL RESULT

```
1	=== PDF page 273 (book page 243) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Korkâ : gravel  (refs POK:615)
4	#1 (parent #0) [Sanskrit] refs=POK:615 | sarkarah : gravel, sugar
5	  #2 (parent #1) [Pali] refs=None | sakkara : sugar
6	    #3 (parent #2) [Persian] refs=BQT:1279 | šekar «شکر» : sugar
7	      #4 (parent #3) [Arabic] refs=PLA:163 | sukkar
8	        #5 (parent #4) [Middle Latin] refs=AHD:1287 | succarum
9	          #6 (parent #5) [French] refs=None | sucre
10	            #7 (parent #6) [Persian] refs=MON:1802 | sâkâroz «ساکاروژ»
11	            #8 (parent #6) [English] refs=KLN:1539 | sugar, sucrose
12	    #9 (parent #2) [Greek] refs=KLN:1370 | sakkaron
13	      #10 (parent #9) [Latin] refs=None | saccharon
14	        #11 (parent #10) [English] refs=AHD:1140 | saccharin, saccharose
15	        #12 (parent #10) [French] refs=VOP:208 | saccharine : sugar, sweet bread
16	          #13 (parent #12) [Persian] refs=VOP:208 | sâxârîn «ساخارین» : a type of sweet bread | extra: سوخاری | NOTE: MON:1945 derives "soxârî" from Russian "suxâr: sweet bread"
17	#14 (parent #0) [Greek] refs=KLN:324 | kroke : pebbles ; krokodilos : pebble worm
18	  #15 (parent #14) [Latin] refs=None | crocodillus
19	    #16 (parent #15) [English] refs=None | crocodile
20	--- entry 1 ---
21	ROOT [Indo-European] Kormo : pain, suffering  (refs POK:615)
22	#1 (parent #0) [Avestan] refs=POK:615 | fšarema : pain
23	  #2 (parent #1) [Persian] refs=HRN:172; BQT:1264 | šarm «شرم» : shame
24	#3 (parent #0) [Germanic] refs=AHD | harmaz : pain
25	  #4 (parent #3) [English] refs=None | harm
26	
```


## [2026-09-06T21:09:23.246Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-273.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-06T21:09:23.298Z] TOOL RESULT

```
{
  "pdf_page": 273,
  "book_page": 243,
  "entries": [
    {
      "root": {
        "name": "Korkâ",
        "lang": "Indo-European",
        "refs": "POK:615",
        "gloss": "gravel"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:615",
          "words": [
            {"translit": "sarkarah", "gloss": "gravel, sugar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pali",
          "refs": null,
          "words": [
            {"translit": "sakkara", "gloss": "sugar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1279",
          "words": [
            {"translit": "šekar", "gloss": "sugar", "script": "شکر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "PLA:163",
          "words": [
            {"translit": "sukkar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Middle Latin",
          "refs": "AHD:1287",
          "words": [
            {"translit": "succarum", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "sucre", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:1802",
          "words": [
            {"translit": "sâkâroz", "gloss": null, "script": "ساکاروژ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:1539",
          "words": [
            {"translit": "sugar, sucrose", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 2,
          "lang": "Greek",
          "refs": "KLN:1370",
          "words": [
            {"translit": "sakkaron", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "saccharon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "AHD:1140",
          "words": [
            {"translit": "saccharin, saccharose", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "French",
          "refs": "VOP:208",
          "words": [
            {"translit": "saccharine", "gloss": "sugar, sweet bread", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "VOP:208",
          "words": [
            {"translit": "sâxârîn", "gloss": "a type of sweet bread", "script": "ساخارین"}
          ],
          "script_extra": "سوخاری",
          "note": "MON:1945 derives \"soxârî\" from Russian \"suxâr: sweet bread\"",
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:324",
          "words": [
            {"translit": "kroke", "gloss": "pebbles", "script": null},
            {"translit": "krokodilos", "gloss": "pebble worm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "crocodillus", "gloss": null, "script": null}
          ],
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
            {"translit": "crocodile", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kormo",
        "lang": "Indo-European",
        "refs": "POK:615",
        "gloss": "pain, suffering"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:615",
          "words": [
            {"translit": "fšarema", "gloss": "pain", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:172; BQT:1264",
          "words": [
            {"translit": "šarm", "gloss": "shame", "script": "شرم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "فردا که پیشگاه حقیقت شود پدید - شرمنده رهروی که عمل بر مجاز کرد",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "harmaz", "gloss": "pain", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "harm", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-06T21:09:25.831Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','PLA','AHD','MON','KLN','VOP','HRN','WLD','SKT','WEB','FSD','LKT','AFM','FVQ','IEC','SYN','BRT','KNT','PHD','NYB','HUB','ARY','HJB','AID']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\"",
 "description": "List refs and lookup keys"
}
```


### [2026-09-06T21:09:27.629Z] TOOL RESULT

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
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
```


## [2026-09-06T21:09:33.272Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','WLD','IEC','SYN','HRN','BRT','BQT','MON','PLA','SKT','LKT','LEW','LAT','ARY','HJB','AID','RCH','FSD','WEB','HUB','PHD']:\n    v=d.get(k,{})\n    print('==',k, '| offset:', v.get('page_offset'), '| local:', v.get('local_file'), '| hint:', str(v.get('lookup_hint'))[:300])\n\"",
 "description": "Print page offsets for refs"
}
```


### [2026-09-06T21:09:34.823Z] TOOL RESULT

```
== POK | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== WLD | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== IEC | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== HRN | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== BRT | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== PLA | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== SKT | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== LKT | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== LEW | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== ARY | offset: printed page = pdf page + 1 | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== HJB | offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt | hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
== AID | offset: leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt | hint: Headword in bold at line start; grep -n '^Word'.
== RCH | offset: leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt | hint: Entries are Persian/Arabic in script (poorly OCRed) followed by transliteration and English gloss; grep the English gloss or transliteration.
== FSD | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== HUB | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== PHD | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
```


## [2026-09-06T21:09:42.324Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 615\" POK_full.txt | head -20; echo \"---lemma korka---\"; grep -n -i \"lemma: k.orka\\|lemma: kormo\\|lemma: korko\" POK_full.txt | head",
 "description": "Grep Pokorny full text for page 615"
}
```


### [2026-09-06T21:09:42.390Z] TOOL RESULT

```
48110:Page(s): 615-616 
---lemma korka---
```


## [2026-09-06T21:09:45.398Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '48090,48125p' POK_full.txt; echo \"=== search kies grus ===\"; grep -n \"Kies, Grus\\|Qual, Schmerz\\|Qual, Schmerz\" POK_full.txt | head",
 "description": "Print Pokorny entry around p.615"
}
```


### [2026-09-06T21:09:45.469Z] TOOL RESULT

```
*KoTpo(; from *K6pjO(; with formants -no-, also Old Icelandic herjann^ father of the army " as 
epithet of Odins from harja-^ army " from; Koipavsu) " command; rule ", Koipavia "power, 
rule", compare of the unadjusted *KoTpo- EN as Koip6|jaxo(; (Boisacq s. v.); 

Middle Irish cuirem. "troop, multitude, crowd, bulk, mass", gall. 777-, Petru-corii 
Volkernamen ("die drei-, vierstammigen"); 

Gothic harjis. Old Icelandic herr. Old English here^ army ", Old High German Old Saxon 
heri^ army, bulk, mass", PN Old Germanic Hari-gasf/ (Dat), perhaps god"s name (Meckel 
KZ. 60, 284); 

Lithuanian kar/as' army", kare'\Nar, fight", /ra/ys "warrior", Latvian kar's '\Nar, fight, army 
", Old Prussian /ra/y/is (consigns kragis) " army ", caryawoytis kVk. Sg. "military parade, 
military march"; 



compare also above kar-1S. 530, where Balto Slavic examples can also belong here. 

References: WP. I 353, 462, Trautmann 118. 
Page(s): 615-616 

Root / lemma: kos(e)lo- 

Meaning: hazel 

Material: Latin corulus^ a hazel-tree, filberttree ', colurnus {*corulinos) " of the hazel, of 

hazel-wood '; 

Old Irish coll, acymr. coll etc. ' hazel' (also gall. Coslo-\n EN); (common Celtic alb. 
abbreviation), [common Celtic si- > II-] 

Old High German hasal(a). Old English haesel. Old Icelandic haslm. " hazel'. Old High 
German hesllfn. Old English hseslen^ of hazel-wood '; 

=== search kies grus ===
```


## [2026-09-06T21:09:52.116Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Meaning: gravel\\|Meaning: pain\\|Meaning: suffering\\|Meaning: grief\" POK_full.txt | head -20; echo \"=== lemma near ===\"; grep -n \"^Root / lemma: kor\\|^Root / lemma: k.or\\|^Root / lemma: kar\" POK_full.txt | head -30",
 "description": "Search Pokorny lemmas for gravel and pain"
}
```


### [2026-09-06T21:09:52.193Z] TOOL RESULT

```
34909:Meaning: gravel 
51693:Meaning: gravel, boulder 
51727:Meaning: suffering, pain 
71538:Meaning: pain, illness, injure, hurt, damage, disable 
=== lemma near ===
43826:Root / lemma: kar-1 
43856:Root / lemma: kar-2, kara- 
43892:Root / lemma: kar-3, redupl. kartiar- 
43964:Root / lemma: kars- 
44252:Root / lemma: kar- 
48081:Root / lemma: koro-s, kono-s
```


## [2026-09-06T21:09:54.511Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51685,51760p' POK_full.txt",
 "description": "Print Pokorny entries for gravel and suffering"
}
```


### [2026-09-06T21:09:54.565Z] TOOL RESULT

```
possibly popular etymology after Kunpo(;, because *KonpTvoc; would allow to think in 
K6npO(;. 

References: WP. I 457, WH. I 171, Trautmann 299. 
Page(s):614 

Root / lemma: Rorka{RrokS7), -Ja 

Meaning: gravel, boulder 

Material: Old Indie sarkara {sarkara-h) " powder, gravel, stone, powder sugar '; 

gr. KpoKP), KpoKaAri "pebble"; perhaps has a *KopKaAa : s'a/'/ra/'a previously after KpsKW 
'hit' metathesis experienced in KpoKaAr). 

References: WP. I 463. 
Page(s):615 

Root / lemma: Rormen- 

Meaning: ' weasel ' 

See also: see above under ker-6. 

Page(s):615 

Root / lemma: Rormno- Rfmno- 

Meaning: acid liquid, lye, urine 

Material: Middle High German hurmen^ fertilize ' (originally probably with Jauche), Modern 

High German harn, harmO\6 High German haran ^unne'; 

Lithuanian sarmas' alkali, leach, lye, buck ', Latvian sarms'\ye', Old Prussian (with the 
ablaut grade from Middle High German hurmen) s/rmes {ior *sirmis) 'lye'. 

References: WP. I 463, Trautmann 300. 
Page(s):615 

Root / lemma: Rormo- 

Meaning: suffering, pain 

Material: Avestan fsarama-vn. ' sense of shame before ', Middle Persian sarm ds.; 

Old Icelandic harmr^ sorrow, distress, damage, injury'. Old English hearmm. ' distress, 
pain, damage, pity'. Old Saxon /7a/777'pain, injury'. Middle Low German /75/777'pain', Old 



High German ^az/a^/r? "affliction, damage, insult'. Modern High German Harm, Old English 
hearm. Old Saxon /75/777 "painful, hurtful '; 

Old Bulgarian sramh "the genitals'. 

References: WP. I 463, Trautmann 299. 
Page(s):615 

Root / lemma: Ro-, Re-{W\Vc\ particle ^e"here'), R(e)i- R(ilio-{*Rehu^ Note: common Proto 

Germanic -u- > -u-, -y-, -/-. 

Meaning: this 

Material: Armenian -^"article' (e.g. marc/-s'\he person'), 5a"this', a/'-s ds., a-5-/"here'; 

Phrygian a£|JOu(v) "this' {*Rem+ di)\ different Pedersen Tochar. 259. 

gr. particle *k£ in k£Tvo(; and iKZ\yoc„ Doric Lesbian K\\yoQ, "that' from *(£)k£-£VO(;; out of it 
back formation (£)k£T "there', (£)k£T9i etc.; *Rio- in or|p£pov, Attic Tr||j£pov "today' 
(*Kic(p£pov), whereupon also *kic(F£T£(; "this year' in a\\izc„ Attic ^\\\zc„ Doric aaizc;. 

Note: 

(common Avestan Slavic k> c: alb. k> ts >q: Greek Tocharian labialized l<^> t, gutturals
```


## [2026-09-06T21:10:27.147Z] TOOL CALL #10: Bash

```json
{
 "command": "ls site/pages/273.jpg 2>/dev/null; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 273 -l 273 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg273 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 273"
}
```


## [2026-09-06T21:10:29.102Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD kormo ===\" && grep -n -i \"kormo\\|korka\\|krok\" AHD_watkins1985.txt | head -20 && echo \"=== AHD harm ===\" && grep -n \"^harm\\b\\|harmaz\" AHD_watkins1985.txt | head",
 "description": "Grep AHD Watkins for kormo/korka"
}
```


### [2026-09-06T21:10:29.367Z] TOOL RESULT

```
site/pages/273.jpg
total 18596
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:10 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     286 Sep  6 17:09 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   65729 Sep  6 17:10 pg273.png
```


### [2026-09-06T21:10:29.425Z] TOOL RESULT

```
=== AHD kormo ===
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
=== AHD harm ===
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
```


## [2026-09-06T21:10:34.208Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg273.png"
}
```


### [2026-09-06T21:10:34.596Z] TOOL RESULT

```

```


## [2026-09-06T21:10:34.593Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:10:48.332Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 273 -l 273 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg273hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg273hi.png'); print(im.size)\nw,h=im.size\n# sakaroz box approx x 1000-1190/1545 ; y 535-610/2000\nim.crop((int(0.63*w),int(0.26*h),int(0.79*w),int(0.31*h))).resize((int(0.16*w*2),int(0.05*h*2))).save('crop_sak.png')\nim.crop((int(0.53*w),int(0.395*h),int(0.79*w),int(0.44*h))).save('crop_sax.png')\nim.crop((int(0.20*w),int(0.185*h),int(0.55*w),int(0.225*h))).save('crop_shekar.png')\n\"; ls",
 "description": "Crop Persian boxes at high res"
}
```


### [2026-09-06T21:10:52.637Z] TOOL RESULT

```
(5100, 6600)
agents.txt
bqt1594_foot.png
bqt83_head.png
bqt_v3_83.png
build261.py
c1.png
c2.png
c3.png
c4.png
coord_pg262.png
crop_ak2.png
crop_ak.png
crop_alk.png
crop_fr269.png
crop_germ269.png
crop_gk269.png
crop_gk271.png
crop_gr267.png
crop_gr.png
crop_kohul.png
crop_lat2.png
crop_latin269.png
crop_lat.png
crop_me2.png
crop_me.png
crop_op2.png
crop_op.png
crop_pers.png
crop_sak.png
crop_sax.png
crop_shekar.png
crop_sirish.png
crop_skt267.png
crop_slav.png
crop_top.png
ediv.pdf
ediv.txt
jscheck.js
merge262.py
mk265.py
mk268.py
mk.pdf
mk.txt
p262-g01.json
p262-g02.json
p262-g03.json
p262-g04.json
p262-g05.json
p262-g06.json
p262-g07.json
p262-g08.json
p262-g09.json
p262-g10.json
p262-g11.json
p262-g12.json
p262-g13.json
p263hi.png
pg261.png
pg262.png
pg263.png
pg264hi.png
pg264.png
pg265_crop.png
pg265.png
pg266.png
pg267.png
pg268.png
pg269.png
pg270hi.png
pg270.png
pg271hi.png
pg271.png
pg272.png
pg273hi.png
pg273.png
```


## [2026-09-06T21:10:54.778Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_sak.png"
}
```


### [2026-09-06T21:10:54.802Z] TOOL RESULT

```

```


## [2026-09-06T21:11:08.617Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_sax.png"
}
```


### [2026-09-06T21:11:08.635Z] TOOL RESULT

```

```


## [2026-09-06T21:11:19.136Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN sugar ===\" && grep -n \"^sugar,\" KLN_1966.txt | head && grep -n \"^sucrose\\|^saccharin\\|^saccharose\\|^crocodile\" KLN_1966.txt | head",
 "description": "Grep Klein for sugar, saccharin, crocodile"
}
```


### [2026-09-06T21:11:19.207Z] TOOL RESULT

```
=== KLN sugar ===
9723:crocodile,  n.  —  ME.  cocodrille,  fr.  OF.  cocodrille, metathesized  fr.  L.  crocodilus,  fr.  Gk.  xpox68TXo<;, ‘lizard;  crocodile’,  dissimilatedfr.*xpoxo-Spt>o<;, lit.  ‘stone  worm’,  fr.  xpixr.  ‘pebble’,  and  SpTXoc, ‘worm’.  Gk.  xp6xrj  is  cogn.  with  OI.  sarkarah, sdrkara,  ‘gravel,  pebble,  sugar’;  see  sugar  and words  there  referred  to.  The  etymology  of  Gk. SpIXo?  is  unknown.
33435:saccharin,  saccharine,  n.,  a  white  crystalline  com¬ pound,  C;H503NS  ( chem .)  —  Coined  by  Fahl- berg  and  List  in  1879  fr.  ML.  sacchartim  (fr.  L. saccharon) ;  see  sacchar-  and  -in. saccharine,  adj.,  of  the  nature  of  sugar.  —  See sacchari-  and  adj.  suff.  -ine. saccharo-,  combining  form.  —  See  sacchar-. Saccharomyces,  n.  pi.,  a  genus  of  fungi,  the
33438:saccharose,  n.,  cane  or  beet  sugar.  —  Formed  fr. Gk.  oaxyapov,  ‘sugar’  (see  sacchar-),  and  subst. suff.  -ose.
```


## [2026-09-06T21:11:19.945Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 172 leaf 193 ===\" && awk 'BEGIN{RS=\"\\f\"} NR==194' HRN.txt | head -60",
 "description": "Print Horn page 172"
}
```


### [2026-09-06T21:11:21.482Z] TOOL RESULT

```
=== HRN 172 leaf 193 ===
— 172 -
phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
arm. LW. staij, davon Denomin. stapim 'eilen.
aw. *aiwis + l^tap-, täpaj/eiti *iri Wärme, Hitze
bringen', dann tropisch-).
Zu aiwis vergl. oben np. hes- (No. 221).
778. sHden gehen; sein, werden', Praes. sev-em.
ap. \/^siya€', aslt/avam, asiyuva 'gehen, marschiren';
aw. {/sav-, suvaite'^) gehen'; ai. [/^cyav-, Ci/dvate 'fort-
gehen ; arm. cit 'Aufbruch', ciiem 'aufbrechen' (H.
No. 242).
kurd. eleu 'gehen', dicm; sify, soal 'werden, gehen';
oss. d. t. cäün 'gehen, schreiten, spazieren, fahren'
(319) ; bei. suta, siit, n. suöa, iud^a (322) ; wa;^. cduam,
si/n. oi\zafcam, sar. va]zevsam.
779. siirrän, serrün 'unablässig lliessend', slrän Kegen' (y),
sun-iden^), vergl. sär {äbsär), särulen, ,
ai. l^ksar-, ksdrati 'fliessen, strömen' (Geiger,
Etym. d. Bai. unter No. 66; bei. ö[ur 'Giessbach'
kann aber nicht verglichen werden, s. Htibsch-
mann, ZDMG. 44, 556).
780. Herrn 'Schaam'.
aw. fsarema- 'Schaam'; phlv. sarm *Schaam', sarm-
[gas 'Genitalien' (vd. 16 (5) Gl.).
oss. t. äfsdrm, d. äfsänni 'Schande' (121) ; LW. aty.
bei. (253) sarm 'Schaam', kurd. serm,
781. sest, sest 'sechzig*.
aw. yscasti- 'sechzig ; päz. säst (FPGl.); ai. saüi-,
kurd. FD. LW. sest; afy. speta,
782. susten Vaschen', Praes. söy-em^),
phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
*) Pfiz. qastäftun^ qastäwidan (Men.) ist Unsinn.
*) An ursprüngliches ^sila^ten (vergl. jjuft aus jf*x^) darf man
wegen Praes. siiäb-em natürlich nicht denken.
^) Bartholomae, Ar. Forsch. III, 33 liest staitc.
*) Zum Teil unbelegt.
^j Reimt auf higöyetl, Vis und Rämln S. 70 Vers 6.
```


## [2026-09-06T21:11:33.436Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== sugar entry ===\" && grep -n \"^sugar\\|^sucrose\\|^sacchar-\" KLN_1966.txt | head -20; echo \"=== ctx ===\"; grep -n \"sugar,  n\\.\" KLN_1966.txt | head",
 "description": "Find Klein sugar and sacchar- entries"
}
```


### [2026-09-06T21:11:33.502Z] TOOL RESULT

```
=== sugar entry ===
=== ctx ===
37391:Sufism,  n.,  mystical  doctrines  of  the  Sufis.  — Formed  fr.  Sufi  with  suff.  -ism. sug-,  assimilated  form  of  sub-  before  g. sugar,  n.  —  ME.  suger,  sugre,  fr.  OF.  (=  F.) sucre,  fr.  ML.  succarum,  fr.  Arab,  sukkar,  fr. Pers.  shakar,  fr.  Pali  sakkard,  fr.  OI.  sarkara, sarkarah,  ‘gravel,  grit,  sugar’,  which  is  cogn. with  Gk.  xp 6>o],  xpoxiXv),  ‘pebble’,  and  with the  first  element  in  xpoxo-Slkog,  ‘crocodile’. Cp.  It.  zucchero,  Sp.  aziicar,  Port,  afucar,  Rum. zdhar,  OHG.  zucura  (whence  MHG.  zuker,  G. Zucker),  ‘sugar’,  which  all  are  borrowed  fr. Arab,  sukkar.  (The  inital  a  in  Sp.  aziicar.  Port. acucar  represents  the  Arab,  article  al).  Cp.  sac- char-,  saccharin,  sucrate,  sucrose.  Cp.  also  jag¬ gery,  the  first  element  in  crocodile,  and  the second  element  in  seersucker.
```


## [2026-09-06T21:11:40.279Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for kw in ['ME.  suger,  sugre','crocodile,  n.','Coined  by  Fahl','sucrose,  n','sacchar-,  combining','Formed  fr. Gk.  oaxyapov']:\n        if kw in p:\n            print('leaf',i,'kw',kw)\nEOF",
 "description": "Locate Klein leaves"
}
```


### [2026-09-06T21:11:42.076Z] TOOL RESULT

```
leaf 207 kw crocodile,  n.
leaf 728 kw Coined  by  Fahl
leaf 728 kw Formed  fr. Gk.  oaxyapov
leaf 816 kw ME.  suger,  sugre
leaf 816 kw sucrose,  n
```


## [2026-09-06T21:11:50.292Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (207,728,816):\n    p=pages[i]\n    print('--- leaf',i,'first 200:',repr(p[:200]))\n    print('    last 200:',repr(p[-200:]))\nEOF",
 "description": "Inspect Klein leaves for page numbers"
}
```


### [2026-09-06T21:11:52.067Z] TOOL RESULT

```
--- leaf 207 first 200: 'ed  of  crino,  ‘hair’  (fr. L.  crinis),  and  lino,  ‘flax’  (fr.  L.  linum).  It.  crino- lino  prop,  denotes  a  fabric  whose  woof  is  made of  hair  and  whose  warp  is  made  of  linen.  S'
    last 200: ' Ypurro?,  ‘curved,  hook-nosed’.  See creep  and  cp.  words  there  referred  to.  Cp.  also croup  (of  a  horse),  crupper,  group.\nDerivatives:  crop,  tr.  v.,  to  cut  off  (esp.  the tops  of'
--- leaf 728 first 200: 'i,  F.  samedi,  ‘Saturday’  and — prob. through  the  medium  of  the  Gothic— the  first element  in  OHG.  samba$-tac  (MHG.  same j- tac,  G.  Sams-tag),  ‘Saturday’].\nSabbathia,  n.,  a  genus  o'
    last 200: 're,  ‘to  gather, pick  up,  carry  off,  steal’.  See  sacred  and  lecture. Derivatives:  sacrileg-ious,  adj.,  sacrileg-ious-ly, adv.,  sacrileg-ious-ness,  n.,  sacrileg-ist,  n. sacring,  n.,  c'
--- leaf 816 first 200: 'uckle’.  See  suckle, n.,  and  subst.  suff.  -ing.\nsuclat,  n.,  any  of  certain  woolen  stuffs;  specif,  the European  broadcloth  ( Anglo-Indian ).  —  Hind. suqlat,  fr.  Pers.  saqallat,  a  '
    last 200: '.  MF.  (=  F.),  fr.  OF., fr.  L.  suggesdonem,  acc.  of  suggestio,  fr.  sugges¬ tus,  pp.  of  suggerere.  See  suggest  and  -ion. suggilate,  tr.  v.,  to  beat  black  and  blue.  — L.  sitgi'
```


## [2026-09-06T21:12:18.555Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\np=pages[728]\ni=p.find('sacchar')\nprint(p[max(0,i-200):i+2500])\nEOF",
 "description": "Print Klein sacchar- entry"
}
```


### [2026-09-06T21:12:20.314Z] TOOL RESULT

```
and  cp.  the  first  element  in  sackbut. saccate,  adj.,  formed  into  a  sac;  having  a  sac.  — ModL.  saccatus,  fr.  L.  saccus,  ‘sack,  bag’.  See sack,  ‘a  bag’,  and  adj.  suff.  -ate. sacchar-,  sacchari-,  saccharo-,  combining  forms meaning  ‘sugar’.  —  Fr.  L.  saccharon,  fr.  Gk. rsaxy ac -v,  ‘sugar’,  fr.  Pali  sakkhard,  fr.  Ol.  sar- kard,  ‘gravel,  grit,  sugar’.  See  sugar  and  cp. words  there  referred  to.
sacchariferous,  adj.,  containing  sugar.  —  Com¬ pounded  of  sacchari-  and  -ferous. saccharify,  tr.  v.,  to  convert  into  sugar.  —  Com¬ pounded  of  sacchari-  and  -fy. saccharimeter,  saccharometer,  n,,  an  instrument for  measuring  the  amount  of  sugar  in  a  solu¬ tion.  —  Compounded  of  sacchari-,  resp.  saccha¬ ro-,  and  Gk.  pirpov,  ‘measure’.  See  meter, ‘poetical  rhythm'.
saccharin,  saccharine,  n.,  a  white  crystalline  com¬ pound,  C;H503NS  ( chem .)  —  Coined  by  Fahl- berg  and  List  in  1879  fr.  ML.  sacchartim  (fr.  L. saccharon) ;  see  sacchar-  and  -in. saccharine,  adj.,  of  the  nature  of  sugar.  —  See sacchari-  and  adj.  suff.  -ine. saccharo-,  combining  form.  —  See  sacchar-. Saccharomyces,  n.  pi.,  a  genus  of  fungi,  the
13/U-
yeasts  (bot.)  —  ModL.,  lit.  ‘sugar  fungi’  (see saccharo-  and  -myces),  prop,  a  loan  translation of  G.  Zuckerpilz,  a  name  given  to  yeast  by Theodor  Schwann  (1810-82).  See  C.  C.  Mettler, History  of  Medicine,  Philadelphia  -  Toronto, 1947,  p.  261.
saccharose,  n.,  cane  or  beet  sugar.  —  Formed  fr. Gk.  oaxyapov,  ‘sugar’  (see  sacchar-),  and  subst. suff.  -ose.
sacciform,  adj.,  sack-shaped.  —  Compounded  of L.  saccus ,  ‘sack,  bag’  and  forma,  ‘form,  shape'. See  sack,  ‘bag’,  and  form,  n. saccule,  n.,  a  little  bag.  —  L.  sacculus,  ‘a  little sack  or  bag’,  dimin.  of  saccus.  See  sack,  ‘bag’, and  -ule.
sacerdotal,  adj.,  pertaining  to  the  priesthood  or to  priests.  —  ME.,  fr.  MF.,  fr.  L.  sacerdotdlis, ‘pertaining  to  priests,  priestly’,  fr.  sacerdds,  gen. -otis,  ‘priest’,  which  stands  for  •  sakro-dho-t-s, lit.  ‘he  who  is  made  holy’,  fr.  sacer,  ‘holy’,  and I.-E.  base  *dhe-,  ‘to  put,  place;  to  make,  ap¬ point’.  See  sacred  and  do.  For  the  ending  see adj.  suff.  -al.
Derivatives :  sacerdotal-ism,  n ,,sacerdotal-ist,  n., sacerdotal-ist-ic,  adj.,  sacerdotal-ly,  adv. sachem,  n.,  supreme  chief.  —  Of  Algonquian  ori¬ gin;  cp.  Narraganset  sachimau.  Cp.  sagamore, sachet,  n.,  a  small  bag  filled  with  aromatic  pow¬ der.  —  F.,  dimin.  of  sac.  See  sac, ‘a  baglike  part’, and  -et.
sack,  n.,
```


## [2026-09-06T21:12:28.790Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('nleaves',len(pages))\nfor target in ['۱۲۷۹','۱۲۶۴','1279','1264']:\n    hits=[i for i,p in enumerate(pages) if target in p[:300] or target in p[-300:]]\n    print(target, hits[:10])\nEOF",
 "description": "Locate BQT v3 pages 1264/1279"
}
```


### [2026-09-06T21:12:30.538Z] TOOL RESULT

```
nleaves 721
۱۲۷۹ [668]
۱۲۶۴ []
1279 []
1264 []
```


## [2026-09-06T21:12:38.775Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (54,55,69,70):\n    print('==== leaf',i,'(pdf page',i+1,')')\n    print(pages[i][:1200])\nEOF",
 "description": "Print BQT v3 candidate leaves"
}
```


### [2026-09-06T21:12:40.350Z] TOOL RESULT

```
==== leaf 54 (pdf page 55 )
[pdf page 55]
کنکر؛ یام و دبوارخاله وغیره ‎٩‏ .

‎Sys‏ - بنتح اول بر وزن فلك » بمعنی
شرا باشده وآن جوششی است که بسیب خون با
صفرا آمیخنه بهم میرسد وبعربی حصبه‌میگوینه
- ودر عربی‌بمعنی‌بلقشنه (۱) است. وآن‌ریسمالی
باشد که بکرآنرا حلقه حلفه کرده گرهی‌برآن
زنه و سس دیگر آبرا از ‎ole‏ حلقها بگذراشه
براهجی که بمجرد کشیدن ریمان آن ‎ile‏
‏تنگه شود - وشاء ‎aly‏ را نیز گویند که راموسیع
بز رکه باشد- و وسط و میان حقیقی راء را هم
کنته اند - وبفتح اول وسکون ‎gl‏ وتالت:جامه
و پارچه‌ای باشد که درآن دارو بندند - و بکسر
اول و سکون ثانی ‎ely‏ » توعی از جوشش‌باشد
که کودکاتر| ‎pe‏ میرسد و آنرا بعربی جدری
خوانند - و در عربی بممتی‌کافر شدن‌باشد بسبب
‎che‏ انباز برخدا روا داشتن" .

‏) چش

‎-۱۱۸-

‏شرم ۴ بر وزن ارم ۰ ‎Le hey‏
و تاموس ‎ath‏ - وآلت تناسل رالیز گوبند ۴ .

‏شرفاق ‎O)‏ ۰ با ون بر وزن تریاق »
گوشت سرخ زابد باشد که بر پلك چشم آدمی
بهم میرسد ۴ .

‏شر نگ ‎pe‏ وزن ‎eS‏ مطلق زهر
را کوبند 6 - و خریزة ۷ ‎ae‏ خود رو که در
صحرا شود وبعربی حنظل‌خوانند - وخرزهره(۳)
را 55 گفته‌اند ۷ و ‎ol‏ درختی است که ب رکش
بقایت تلخ میباشد.ا کر حبوانات بخوردد در حال
بمیرند و عربان قطف میگویند.

‏شروه - با وار بروزن هرزه » نوعی از
خوانندکی باشد که آفرا شهری گوبند - وبلفت
رومی تام پرلوالی بوده ارمنی نژاد.
شرو لین = بر وزن پر
==== leaf 55 (pdf page 56 )
[pdf page 56]
Atte
‏شروان است - و نام یکی از فرزسزادهای ملك‎
. ۱ ‏کیوی برادر الوشیروان هم‌هت‎
‏شریتا ۴ - با نای فرشت (۱) بر وذن‎
‏مسیحا » بلفت 5 وپازند (۲) پادشاه را گویشد.‎

شریدن ۴ = بر وزن رسیدن » بمعنی

تراوبدن باشد - و جنم اول و الی مشدد بروزن
غربدن | بمعنی رختن پی‌دریی باشد ببفاصله.
‎eau, ۵‏ :
سر یتو لقن ‎phe”‏ لون ونای قرشت
پروزن پربروفکن » بلغت زند ویازلد(۲) بمعنی
کشادن‌باشد. و شربتولمی بعنی کشامم‌وشربتونید
‎Mag yin‏

‎ol‏ دهم

‏در شین نقطه دار با سین بی‌نقطه مشتمل برشش لغت و کنایت

‏سپ » بنتح اول وسکون ‎QU‏ و بای
فارسی » بمعنی جهنده و خی زکننده باشذ ۵ -
و بمعنی غیبت (۳) هم‌آمده است که در مقابل
حضور است.

‏شست = بروزن دست » چند ممنی‌دارد:
۱- عددی است معروف که بعربی ستین گویند
و معرب ‎oT‏ شصت باشد ۰.۱۷ ۲- بمعتی زار
‎ath‏ و آن رسمالی است که کبران و هنود بر
کمربندند و ب گردن‌اندازند . . ۳-نش‌ویشتر
فاد و رکه زن باشد و بعربی مبضم خواهد .

‏(۱) چك : پا تا .

‎. ‏چك: ژلد ویاژلد‎ (x)

‏> - انگشت بز رکه‌باندکه انگشت زهگیراست
و بعربی ابهام گویند. 0 - بمعنی زهگی‌باشد
و آن انگفتر ‎gust.‏ است که از استضوان‌سارند
و در الگشت ابهام کنند و دروقت کمانداری زء
کمان را بدان گیرنه و ‎WT‏ باعتبار انگشت‌ابهام
شت میگرند.  ‎-٩‏ قلایی باشدکه ‎holy‏
‏کیرند ۷ . ۷ -مشراب را کویند و آن
چیزیت که بسنی از س
==== leaf 69 (pdf page 70 )
[pdf page 70]
- ۲۷4 ات

ورزش » بمعنی بدنامی باشد یعنی بچیزهای بد
شهرت کردن .

شکرعقیق رنگ - کنابه از لب
معشوق است .

شکر فنده ‎Ga’‏ اول ‎pbs‏ فا
بر وزن درخشنده ؛ بمعنی ‎fb‏ بده و بس در
آینده باشد و اسب سکندری خور را لیز
کفته اند

شکر لب - ‎TU SL pets‏ بالابا
لب پاین او ‎asks‏ و چاك دار ‎ash‏ و همچنی‌از
مادر زایده‌شده باشد- و کنایه ازمحیوپومطلوب
° هست .

‎SX‏ - بر وزن ‎SS‏ مخنف
شکررنکه است ‎ote yy Ke ster‏ چه رنگ‌بسمتی
رونیده و رسته هم آمده است - و بمعنی ‎SE‏
‏ب رکه باشد وآن برکها و پارهای دراز است که
از شکر ‎WL‏ ویرهم بندند .

‏شکروده ؟ © بفتح اول و واو بروزن
فلك زده, مردم ‎abe‏ وچست وچايك وصاحب جد

‏در کارها و ساخته وآماده در مهمات باشد؛ وم
واو هم بنظرآعده است.

‏شگره ۴ = بکراول وفتح نانی‌ونالك»
پرنده ایست شکاری از جنس باشه لیکن ازو
کوچکتر باشد .

‏شکر هنج = بنتح اود ‎bay‏ وسکون‌نون
و جیم » معرب ‎Ka Ls‏ است که خسك
باشد و آن‌خارست سهپهلو ؛ و ‎ork‏ معنی‌بجای
رای قرشت واو هم پنظر آمده است.

‎Jol Ge Fou‏ بروزن
شنوبدن ۰ ‎ines‏ شکار کردن و شکستن دشمن
باشد .

‎WAC el py LSS
‏خوانند.‎ GLU ‏بعربی‎ LT ‏و‎

‏شکستن - بفتح ثالی معروف است ‎٩‏
‏- وبمعنیاعرا کردن ‎ay‏ شدن باشد سوبه‌عنی
خوردن و جاویدن هم آمده است - وخجل‌شدن
= وهزیمت لشکر را نیز گوبند.

‏شکست و همکست = بکرارلوميم,

‎. ‏اسم فاعل از 
==== leaf 70 (pdf page 71 )
[pdf page 71]
از انباع است ۱ - ویمعتی عاضی شکتن باشد
یمنی پیش‌ازاین شکست.

‎pi =e FERS‏ اول و شین قرشت
بی وزن ‎AG‏ آواز پای باشد که در وقت ‎la‏
‏رفتن برآید .

‏شکفت - پکر اول و فتح الی‌وسکون
فا و فوقالی » بمعنی‌غار باشد ۳ و ‎OT‏ جایی‌است
در کوهپا ساخته و ‎Lge‏ شده که اکثر دروشان
» فقیران‌درآنجا بر برد - وبمعنی کج‌وناهموار
پیز کفته‌الد - وبضم‌انی ازهم کشودن رامیگونند
- و شکفتن و واشدن غنچةٌ کل را هم کویند -
و بکسر ثالی ‎ote‏ عجیب و غریب و عجب
و ‎Cod‏ آمده است » وباین معنی با کاف فارسی

‏هم گفته اند ۰
شگفتی ‎ING‏ وضم ثانی,یممنی
واشدن غنچة کل وخندان شدن‌باشد؟ - وبکر
‎gill‏ بمعنی تعجب نمودن ‎٩‏ .
شکفتیدن » یکر اول و ثالی بروزن
‎gn!‏ شکته » پر پیچ وخم :
آی از آن چون چراغ پیشالی

‏۴ هکاشك .
«اسشق ‎٩۷۸۷‏ .

‏وراد

‏فرستیدن | ‎ines‏ تعجب نمودن و متعجب شدن
باشد ؛ وباکاف قارسی هم ‎onl‏ همتی آمده واصح
‎gl‏ است 3 .

‏شکفه ۲ بکر اول و ‎thee‏ وفتح
فا » ‎iden‏ شکوفه است که کل درخت میومدار
باشد .
‎ARS‏ - بر وزن کجك » طنبوره را
کویند » وآن سازست ممروف - و بمعنی‌خاری
‎e‏ هست کرد و مدورکه در دامن آویزدوآواز
پای را لیز گفته‌اند در وقت ‎ly‏ رفتن ۸ .

‏شککال ‎٩‏ = بکر اول بروزن اقبال .
معظم تر ی و بز رکه ترین پادشاهان هندوستان
‎OF‏ ۰
شکله - بکر اول و سکون ثالی وفتح
لام , آنچه ازجامه وامثال ‎OT‏ در ‎gle‏
```


## [2026-09-06T21:12:55.953Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('==== leaf 54 FULL'); print(pages[54])\nprint('==== leaf 68 (pdf 69)'); print(pages[68][:2500])\nEOF",
 "description": "Print full BQT leaves 54 and 68"
}
```


### [2026-09-06T21:12:57.920Z] TOOL RESULT

```
==== leaf 54 FULL
[pdf page 55]
کنکر؛ یام و دبوارخاله وغیره ‎٩‏ .

‎Sys‏ - بنتح اول بر وزن فلك » بمعنی
شرا باشده وآن جوششی است که بسیب خون با
صفرا آمیخنه بهم میرسد وبعربی حصبه‌میگوینه
- ودر عربی‌بمعنی‌بلقشنه (۱) است. وآن‌ریسمالی
باشد که بکرآنرا حلقه حلفه کرده گرهی‌برآن
زنه و سس دیگر آبرا از ‎ole‏ حلقها بگذراشه
براهجی که بمجرد کشیدن ریمان آن ‎ile‏
‏تنگه شود - وشاء ‎aly‏ را نیز گویند که راموسیع
بز رکه باشد- و وسط و میان حقیقی راء را هم
کنته اند - وبفتح اول وسکون ‎gl‏ وتالت:جامه
و پارچه‌ای باشد که درآن دارو بندند - و بکسر
اول و سکون ثانی ‎ely‏ » توعی از جوشش‌باشد
که کودکاتر| ‎pe‏ میرسد و آنرا بعربی جدری
خوانند - و در عربی بممتی‌کافر شدن‌باشد بسبب
‎che‏ انباز برخدا روا داشتن" .

‏) چش

‎-۱۱۸-

‏شرم ۴ بر وزن ارم ۰ ‎Le hey‏
و تاموس ‎ath‏ - وآلت تناسل رالیز گوبند ۴ .

‏شرفاق ‎O)‏ ۰ با ون بر وزن تریاق »
گوشت سرخ زابد باشد که بر پلك چشم آدمی
بهم میرسد ۴ .

‏شر نگ ‎pe‏ وزن ‎eS‏ مطلق زهر
را کوبند 6 - و خریزة ۷ ‎ae‏ خود رو که در
صحرا شود وبعربی حنظل‌خوانند - وخرزهره(۳)
را 55 گفته‌اند ۷ و ‎ol‏ درختی است که ب رکش
بقایت تلخ میباشد.ا کر حبوانات بخوردد در حال
بمیرند و عربان قطف میگویند.

‏شروه - با وار بروزن هرزه » نوعی از
خوانندکی باشد که آفرا شهری گوبند - وبلفت
رومی تام پرلوالی بوده ارمنی نژاد.
شرو لین = بر وزن پروین » نام ‎LE‏

‎)( ‏چك: شرتاق (۳)چك: خرزه‎ (vy)

‎٩‏ - از ‎ew‏ آن تا زخورشیدش فرون, باشد شرف
مشتری خواهد که اورا شرف آبوان بود . «فرخی‌سیستالی 4۳۳ .
۴ - اوستا _ ‎Fsharema‏ ( حیا : عفت) » پهلوی 5027۳0 ( تاوادبا ‎(Vo‏ ۰ استی
صفداق ‎dfsinmi.‏ (عب ۰ نکه), افتانیع « بلوچی ع ‎sharm‏ (حبا) « کردی ‎sherm‏

‎. ٩۷۸۰ gel?

‎ite - ۴‏ «شرمگاء» < پهلوی ‎sharm—gah‏ «تاوادیا ۰۱5۵ :

‏چنین‌دادپاسخ بدو(باردشیربایکان) کدخدای
یکی حقه بد نزد کنجور شاه
بد و کفت شاه:الدراین حقه چیست؛
بد ‎OT ST‏ خون گرم من است
‎om ae‏ دختر اردوان
تکشتم که فرزند بد در ‎We‏
‏نستم(بشتم) بفرمافت آزرم‌خویش

‏۴ (عر) رك : دزی ‎le‏ ۷۵۵ .
6 - شادباش ای ‎tells‏ کشاینده! که‌شد

‏۲ - ظ, خربزه مصحف «خرزهره» است . رله:دح(۳)دربالا .

‎۱۹4 yt Nerium odorum

‏که ای شاه روشن دل و یا کرای!
سزد کر که‌خواهد کنون‌پیشگاه...
‎ole‏ برین حقه بر مهر کیست ؟
بریده زين باز شرم من است
" که تا باز خواهی نش بی روان
بترسیدم از کر دکار جهان
بریدم‌هم آلدر زم ان‌شرم‌خویش.٩‏
‎blak «‏ بخ ج۷ ص۰۲۲

‏دردهان همه ازهیبت نوشهدشرنگه .
فرخی سیستالی.*لفت فری ۰۲۸۱
۷ خرز هزوم

==== leaf 68 (pdf 69)
[pdf page 69]
‎Ks‏ خند ۱ با خای نفطه‌دار بروزن
کمربند , کنابه از تبسم باشد یعنی در زیر لب
خنده کردن -

‏- شکر خنده ۴ » ‎ps‏ دال,بمعنی‌شکر
‎as‏ است که ‎pet‏ باشد.

‏شکر خو اب - بستی شاد خواب‌است
که خواب خوش باشد - و خواب سحر را نیز
کویند .
‎ORS‏ - بکر اول و فتح ثالی و ‎ot‏
‏وسکون ‎Jb‏ ابجد . ‎yin‏ چاره و علاج کند ۴
- ویمعنی شکارکتنده همرهست ۴ ۰

‏شکردن - بروزن چکردن » بمعنی
شکار کردن و شکستن باشد 6 - و بمعنی علاج
وچاره تمودن هم آمده ‎Vet‏

‏شکرده ۷ « بفتح اول و دال ابجدیر
وزن تبرزه + مردم جلد وچابك وصاحب‌جدوجهد
در کارها را کوبند .

‎Se‏ یز »با رای قرشت بروزن سح
خیز » آفچه درشب عروسی برسر عروس وداماد
‎ys‏ کنند ۵ و بعتی کویند آنجه از ‎Sls‏ داماد

‎. ‏شکر خنذه («.م.)‎ = ٩

‏ور شکرخنده‌است شیرین لب

‏۴ _ مضارع«شکردن». فی : ‎Shegerd‏ درزبان کنولی.

‎ee ‏صحیح‎

‏۲۷ ات

‎ley‏ موس فرستند - و کلام شیرین و ضحیح
‎Eh»‏ - و شمر و خوانندکی و کویندکی
را هم کنته‌اند ‎٩‏ - و بمعنی خوش‌طبع‌وبذله ‎SS‏
‏لیز عست - ‎BS any‏ شادی هم آمده است
- ولب خوبالرا ‎ja‏ شکرریز خوالند - و شخصی
را گوبند که ازشکر ليز چیزها سازد و اورابعریی
فناد خوانند.

‎ys Xs‏ طرب » کنایه از کربة
شادی باشد .

‏شکرر یز ی « پروزن سحرخیزی»
کربه‌ای را کویند که از روی شادی وخوشحالی
کنند - و بمعنی گفتار خوش و سخنان شیرین

‏و ارم و آهسته هم آمده است.
2 5 خمه = بنتح زا و ‎SE‏ نقطه‌رار
و میم »کنایه از رسیدن تیراست برنشانه.
شکر ‎Raw‏ = بنتح سین پی‌قط‌وسکون
نون وکاف فارسی » حجر ‎lel‏ ۱۱ است, وآن
سنگی باشد سفید . چون آنرا بسایند وبرموضی
که خون ‎adele‏ باشد ریزند خون را بازدارد

‏شکرش پفتح اول و کر اكت‌بروزن

‎ws Se ۴‏ -یزممشوق متبسم وخوشرو :
‎oe‏ بگیروشمم بکش. ‏ « کلستان ‎SPY‏

‏۴ - یدین معنی ظ .

‏۵ - از: شکر (شکار) ‎Oo‏ ( پوند مصدری ) ح شکریدن ‎KE dy (gm)‏ شکره:

‏جهانا ندانم چرا بروری

‏1 رك: شکرد .

‏چو پرورده خوش را بشکری .
فردوسی طوسی. «لفت فری ‎NOL‏

‏۷ - اسم مقعول از «شکردن» .

‏۸ - نار اشك من هرشب شکر ریزست پنهانی
که همت را زنائوبیت از زالو و پیشالی +

‎٩‏ - مطربان‌توچو برعود شکرریز کنند

‏* - از: شکرریز ‎SH‏ (مصدری) .
ص ۲۵۱ : ‎٩۲‏ .

‏> خافالی شروانی ‎٩4۲۱‏ .
روح را مقز معطر بود و لب شیرین =
صلمان ساوجی. «فرهنک نظام ‎AH‏
‎arabicus — 1%‏ ۱
( برهان فاطع ۱۷۵ )
```


## [2026-09-06T21:13:10.170Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n -i \"sarkara\\|sakkhara\\|sakkara\\|carkara\\|shakar\\|sukkar\" BQT_v3_pages.txt | head -20",
 "description": "Grep BQT v3 for sugar etymology forms"
}
```


### [2026-09-06T21:13:10.220Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:13:14.220Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(64,69):\n    p=pages[i]\n    if 'شکر' in p:\n        print('==== leaf',i,'pdf',i+1,'printed ~',i+1+1209)\n        print(p[:1800])\n        print('...TAIL...')\n        print(p[-1500:])\n        break\nEOF",
 "description": "Find BQT main shekar entry"
}
```


### [2026-09-06T21:13:16.285Z] TOOL RESULT

```
==== leaf 65 pdf 66 printed ~ 1275
[pdf page 66]
۱۷۷
هم باین معنی است - وعکه را نیز کوبند وآن
پرنده‌ایست ممروف.*
شکاشاگ ۱ ‎be‏ شین ‎abd‏ دار بر وزن
‎Ake‏ . آواز پای را گویند که بهنگام رامرفتن
‎aT‏ .

کننده - و امر برخنه کردن هم ‎tele‏
‏کلافه کرده را نیز گویند ۴ .*

شکافه = بروزن ‎ils‏ چویکی باپلرچةً
شاخکی باشد که بدان ساز نوازند وآنرا بعریی
مراب خوانند ۴ - وبمعنی کپواره هم آمدماست

که بعربی مهد گویند .

ae . ‏اول بر وزن غلاف‎ So ۲ SES
‏زن * - سازده و مطرب را‎ SES

ممروفت که رخنه وچاکه باشد - و بمعنی‌رخنه

۱ - اسم صوت < شکشك. قس: چکايك . ‎Mg Kay‏ ۴ رك : شکافتن .

۴ - شکوفه همچو شعاف ‎Col‏ و ‎Gee‏ دیبا بان

مه وخور است ‎Bly Ulan‏ درصراف.
بوالمژیدیلخی . «لفت ‎NEV GS‏

۴ - پیری آغوش باز کرده ‎eld‏ توهمی گوش ‎BEL‏ غوش کابی‌مروزی.«لفت‌فری4۲۸*.
و ركك : شکافه زن . ۵ رگ : شکافه .

چد شکار - بکسر اول ( درلجة مر کزی ) اسم از > شکردن © ‎Cea)‏ قس : شکره»
اشکره"یهلوی؟ 5162 ‎sane)‏
‏استی ع 1۵ ( راندن ,
صید کردن ) ۰ «اسشق ۰۷۸5
‎phil‏ ع 5627 ( صید
‎OST‏ شچیر ) , کردی ع
7 ( وحشی ) از -
8 از 6۵۲ 5(رله :بشگرد
بمعتی شکار) ? هوبشمان۷۸۹»:
‎re‏ لخجیر - هرحیوالی که
صیدشود - هر چیز رابگان
ومفت - یفما وغارت +

#شکا رگا بکر
اول . آنجا که شکار کنند ,
محل صید : « توشیروان‌عادل
را در شکارگاه صیدی کباب
کردند.» ‎MENGES?‏

# شکافتن - بکنر اول ‎Indy)‏ مرکزی) از: شکاف ۳- تن ( پونده‌صدری)» پهلوی
‎shkAfta n‏ «تارادیاه۱۹», کردی ‎bishkiwin shikiwin‏ )+66 زدن ‎(gi.‏ کردیع
‎shikafti n‏ (شکافتن , جدا کردن ‎(Gary per‏ ,بوانی 838008 (کندن .شکستن).ممنی کندن
درف ارسی «کافتن» و «کاوبدن» محفوظ مالده ‎vay gaol?‏ اوستا_041 ۳814-502 (عابودکردن»
قلم‌وقمع ) ‎ca. skaph yu) =skaf ubin,‏ آن‌نکافانیدن = ‎shig&fAnidan‏
‏«هوبشمان ۸۷ ‎MV‏ رخنه کردن 6 چاك کردن ۰ شق کردن » پاره کردن» دربدن - شکستن .

۰

شکار خسرو اول انوشروان ‎clit)‏ قره . قرن #میلادی)

...TAIL...
کردن هم ‎tele‏
‏کلافه کرده را نیز گویند ۴ .*

شکافه = بروزن ‎ils‏ چویکی باپلرچةً
شاخکی باشد که بدان ساز نوازند وآنرا بعریی
مراب خوانند ۴ - وبمعنی کپواره هم آمدماست

که بعربی مهد گویند .

ae . ‏اول بر وزن غلاف‎ So ۲ SES
‏زن * - سازده و مطرب را‎ SES

ممروفت که رخنه وچاکه باشد - و بمعنی‌رخنه

۱ - اسم صوت < شکشك. قس: چکايك . ‎Mg Kay‏ ۴ رك : شکافتن .

۴ - شکوفه همچو شعاف ‎Col‏ و ‎Gee‏ دیبا بان

مه وخور است ‎Bly Ulan‏ درصراف.
بوالمژیدیلخی . «لفت ‎NEV GS‏

۴ - پیری آغوش باز کرده ‎eld‏ توهمی گوش ‎BEL‏ غوش کابی‌مروزی.«لفت‌فری4۲۸*.
و ركك : شکافه زن . ۵ رگ : شکافه .

چد شکار - بکسر اول ( درلجة مر کزی ) اسم از > شکردن © ‎Cea)‏ قس : شکره»
اشکره"یهلوی؟ 5162 ‎sane)‏
‏استی ع 1۵ ( راندن ,
صید کردن ) ۰ «اسشق ۰۷۸5
‎phil‏ ع 5627 ( صید
‎OST‏ شچیر ) , کردی ع
7 ( وحشی ) از -
8 از 6۵۲ 5(رله :بشگرد
بمعتی شکار) ? هوبشمان۷۸۹»:
‎re‏ لخجیر - هرحیوالی که
صیدشود - هر چیز رابگان
ومفت - یفما وغارت +

#شکا رگا بکر
اول . آنجا که شکار کنند ,
محل صید : « توشیروان‌عادل
را در شکارگاه صیدی کباب
کردند.» ‎MENGES?‏

# شکافتن - بکنر اول ‎Indy)‏ مرکزی) از: شکاف ۳- تن ( پونده‌صدری)» پهلوی
‎shkAfta n‏ «تارادیاه۱۹», کردی ‎bishkiwin shikiwin‏ )+66 زدن ‎(gi.‏ کردیع
‎shikafti n‏ (شکافتن , جدا کردن ‎(Gary per‏ ,بوانی 838008 (کندن .شکستن).ممنی کندن
درف ارسی «کافتن» و «کاوبدن» محفوظ مالده ‎vay gaol?‏ اوستا_041 ۳814-502 (عابودکردن»
قلم‌وقمع ) ‎ca. skaph yu) =skaf ubin,‏ آن‌نکافانیدن = ‎shig&fAnidan‏
‏«هوبشمان ۸۷ ‎MV‏ رخنه کردن 6 چاك کردن ۰ شق کردن » پاره کردن» دربدن - شکستن .

۰

شکار خسرو اول انوشروان ‎clit)‏ قره . قرن #میلادی)
```


## [2026-09-06T21:13:25.540Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (66,67):\n    print('==== leaf',i,'pdf',i+1)\n    print(pages[i])\nEOF",
 "description": "Print BQT leaves 66-67"
}
```


### [2026-09-06T21:13:27.448Z] TOOL RESULT

```
==== leaf 66 pdf 67
[pdf page 67]
. ٩ ‏کویند‎

1 ‏هت یکس اول بر وزن خسال‎ SK
‏بمعتی چدار است وآن رسمانی باشد که بردست‎
‏بندند ۴ - و بمعنی‎ chet ‏اسب راستر بد‎ shy
۴ ‏مکر وفریب وحیله ۴ هم آمده ات‎

شکانك نه بفتح اول و ‎Ox‏ بر وزن
‎Byki‏ چینهدان مرغان را کوبند وبعربی‌حوصله
خوانند .

شکاو نده * - بکر اول و فتح واو
پروزن شکافنده » شب زن و چا‌جوی را کویند
و ‎em‏ تشاب خوانند.

شکاو نه ‎٩‏ - بکسراول وفتح‌واوولون»
بمعتی شکاونده است که لقب زن وچاه‌جوی باشد
- وکفن دزد را نیز کویند و او را بعریی ‎PS‏
‏بر وزن نقاش خوانند ؛ و بسکون واو هم درست
است .

شکیا - بکس اول وسکون ‎Ye‏ وبای

‎٩‏ -مثال طبع مثال یکی‌شکافهزست

‏پا

‏فارسی بالف کشیده » مردم ترش رو ومقبوض را
گویند .

‏شکبوی ۲۷ س با بای فارسی بر وزن
بدخوی ‎IT‏ پای را کوبند در شب با نهایت
آهستگی - آهته ‎oly‏ رونده را 55 گفته‌اس
و ‎law gine‏ وآوازی باشد که بشب درخواب‌از
مردم برآید .

‏شکر ه بکس اول و فتح ‎GU‏ مخفف
بروزن ‎Se‏ | بمعنی شکار وشکار کننده‌وشکننده
‎ath‏ همچو دشمن شکر یعنی دشمن شکن ۸ -
و امر بشکارکردن و شکستن هم هست معنی‌شکار
‎oF‏ و دشمن بشکن ‎A‏ - وبا ثالی مشددسیخول
‎SaaS‏ خاریشت تیرانداز باشد ‎٩‏ - وبفتح
اول و ‎ill‏ معروف است و ‎OT‏ چیزی باشد که
قند و بات و چیزهای ‎Sis‏ ازآن مازند *۷ -
و تام زلی بوده که خسرو برغم شیرین اورا در
‎CG Dh‏ خود در آورده بود - وارعی از 2985
سیاء باشد که شش پای دارد و پیوسته بر کل

‏که رود دارد برچوب ب رکشیده چهار.
دقیفی طلوسی.«لفت فرس ‎SAYA‏

‏۴ هت شکال (هم.) ‏ شکیل(«.م.)(عر) پای بند ستور (منتهی‌الارب):

‎JK‏ پای ستوران شده سر زلفی

‏۴ شکیل (هم).

‏لایق این تشبیب است.

‏« کلیله‌ورمته مصحح قریب چاپ پنجم ص۲۳۷ .
‎ima ۷‏ «شلپوی» (ه.م ) ‎Boy‏ شکیوی ۳

‏۰۱ - رگ:شکاونده .

‏.. برهمن گفت: آورده‌اند که درزمین هند شکالی بودازدلیا روی,

‏کزوکره بجز از دست شانه لکشوده.

‏کمالاسه‌عیل. (دبوان‌چاپ‌هندص۱*۸).

‏۴ -وبفتح‌اول = شکال ‏ شقال(ه م.):«وداستان‌شر وشکال

‎Gauls
‏از «شکاویدن».‎ , ashi = ©

‎at A‏ واسم
‎٩‏ هت ‎ar‏ ستر(ه م) .

‏و اسم فاعل (مخفف) از «شکردن» = شکتن .

‏۶ - پهلوی 52687« اونوالا ‎٩۱5۷‏ ۰ استی ‎sackaer‏ «که . است ۰۳۳ ‎SAS‏
‏28۲ تهرانی ‎shekar‏ . در ‎sakxaron yb,‏ , لانینی ‎saccharum‏ معربآن‌سکر
‎pe)‏ اول وقتح دوم مشدد ) " فراسوی 910676 ‎sugar , AGI.‏ , آلمانی ‎Zucker‏ ۰ همه
بلاواسطه با مح‌الواسطه ماخون از سانسکربت ‎Sarkar‏ (هندوستان سرزمین باستالی‌شکراست).
‎ty‏ پورداود . شکر. ‎Une‏ بغما سال‌سوم ‎SLs‏ اص۱۸-۸ و رکه : لك۷ ‎PENNE‏

‎ods ‏و مك و شکر یعنی رخ و زلف‎ Ty

‏رنگه و بوی ‎phy‏ سه بر دل وجان ‎Sry‏
‏«معزی لیشابوری ۳۲۲

==== leaf 67 pdf 68
[pdf page 68]
که شکرییزه

که از شکر سازند و بر هم ‎wate‏ و آلرا شکر
قلم خوانند.

شکر بوره ۴ = پا رایع بواو رسیده
ورای می ‎dhe‏ مفتوح , سنبوسه‌ای ‎ath‏ کهدرون
‎oT‏ از قند ومفز بادام وپستةٌ لیم کوفته پر کنند
‎Mey‏

شکر بوذه ۲ ۰ بنتم زای نقطه دارء
پمعتی شکربوره است که سنبوسةٌ قندی باشد.

شکر بیره * - با رابع بتحتالی رسیده
و فتح رای قرشت » بمعنی ‎ody Ke‏ است که
‎ys‏ قندی باشد,

شکر ‎pin = Mo pd‏ زای شلمدار‌بروزن
ومعنی شکرییره است.
۱ - یعنی شرت ساخته ازآب که شکردرآن‌کنند -ماء السکر.
۴-فیرازلب کم حرف توساقی شنيديم جابی که ‎Ole‏ می ویاقی شک آب‌است.

lls ‏کاشالی. « فرهتکه‎ glue IT ‏ابوطالب‎

شیند - وکنایه از لب ممشوق - وسخن شیرین
‎arom‏

wl, - ‏ه معروف است۱‎ wT Ss
‏هم هست که در میان دو دوست‎ Full ‏ازرنیش‎
‎*. ‏میشود ؟‎ ail,

شکر بادام = زرد آلوی ختك کرده
‎als tas‏ برآورده را ‎SAT‏ مفز بادام بجای
دانه ‎Glas‏ آن گذاشته باشند - و بادام ‎Gas‏
‏شده و بادام فندی را 55 کفته‌الد - و کنابه‌ازلب
و چشم ‎Spine‏ هم هستء

شکر بر گه - بنتح بای ابجد و سکون
رای فرشت و ‎GE‏ فارسی + نوعی از شکر پاره
باشد ۴ - ویرکالهای دراز و بهن را تب زگویند

۴ - که شیرینیی بوده:
‎Sle‏ امید من بی نوا را شکر ب رکه لعلش دوا میفرستد .
عمید لوبکی. «فرهنکه ‎plies‏
‏۴ - شکربورك (رك: بورث) محشی دیواناطعمة بسحاق ‎(Vay)‏ کوید:کوبابقر | بمرور
زمان بورك شده است * و ظ محرف «شکربوزه» ‎Com)‏ :
چرامننش کنی صوفی ز محراب شکر بوره
کسی کوید مسلمان راکه رو ازقبله ‎tole Sy‏
‎Glew «‏ اطعمه ۰۷۹ .
۲ شکربیزه و ‎dy‏ : بوزه :
همچو سک در بدر پدر بوزه خوانده خر زهره را شکر بوژه .
سنا غزلوی. «فرهنکه نظلم» +
۸ - صحیح «شکرییزه» («م.) است ‏ شکربوزه ۰
بیار بوسه منه‌خوان خوردلی که بود تفاوتی ز شکر بیزه تاشکر بوسه .
‎oly‏ قهتانی.«فرهنکه تظام» . رك:شکربوزه . ‎٩‏ * شکربوزهورك:شکریره.
* شکر آویر - یفتح اول ودوم ؛ لوعی‌دستار که ظاهراً دارای منکوله‌های آونزان بوده
و خواجگان وبزرکان برس میگذاتند : « رسالة مولانا جلال الدیین محمد مولوی. فروزانفر.
تپران ۱۳۱۵ ص ‎AS‏ 1
ترا رسد شکر آویزخواجگی که‌جود که آستین بکریمان عالم افشانی.
« حافظ شیرازی ص فکد » . « موز مولوی در پای کردند و «ستار را با شکرآویز
پرییچیدند ...»( مناقب احمد افلاکی بنقل ‎Dey‏ مولالا . ایا : )
```


## [2026-09-06T21:13:47.748Z] TOOL CALL #28: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:1279 --image 2>&1 | head -40",
 "description": "Render BQT page 1279"
}
```


### [2026-09-06T21:13:53.903Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1279.png
REF: BQT:1279  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 70  OCR-lang: fas

-۱۹۷۹-< شکت ومکت
ورزش » بمعنی بدلامی باشد یعنی بچیزهای بد | در کارها و ساخته وآماده در مهمات باشد؛ وم
شهرت کردن . واو هم بنظرآمده است.
شکرعقیق رنگ - کنایه از اب شگره ؟ - بکراول وفتح:ثانی‌ونات»
ممعوق است . پرنده ایست شکاری از جنس باشه لیکن آزو
3 ۹ چکتر باشد .
شکرفنده ۱ بکر اول وفتم فا کوچکتر باشد .
بر وزن درخشنده » بمعنی لغزایده و بمر در شکرهنج - بفتح اول وها وسکون‌نون
آینده باشد - واسب سکندری خور را لیز و جیم » معرب شکرهنگ است که خك
گفته‌اند.3# باشد و آن‌خارست سه‌پهلو ؛ و باین معنی‌بجای
ش‌ رت راگویندکه‌لب بالابا رای قرشت واو هم بنظر آمده است.
لب پابن او شکافته و چاك دار باشد و همجنی‌از شکریدن؟ - بکر اول بروزن
مادر زایده‌شده باغد- و کنایه ازمحبوب‌ومطلوب ۱ شنویدن , بمعنی شکار کردن و شکستن دشمن
هم هست . باشد ۰
شکر نگ - بر وزن بکرنکه , مشنق ۱ شگرینه * - نوی ازحلوای شکرباشد
شکررنگه است بعنی‌شکرروییده چه رنگه‌بممنی | و آلرا بعرپی لاطف خوانند.
روبیده و رسته هم آمده است - و بمعنی شکر شکستن - بفتح ای معروف است ‎٩‏
‏بر که باشد وآن برگها و پارهای دراز است که | - وبمعنی‌اعراش کردن وتند شدن باشد -ویه‌عنی
از شکر سازند وبرهم بدند . خوردن و جاویدن هم آمده است - وخجل‌شدن
شکروده ؟ - بنتح اول و واو بروزن < وهزیمت لشکر را نی زگویند.
فلك زده, مردم جلد وچت وچابك وصاحب جد شکست و مکست بکسراول‌وميم»

۱ - اسم فاعل از «شکرفیدن» ۰ (ه.م.) ۰

۲ - ر4: شکرده . ۴ - از : شکر (شکردن < شکتن » شکارکردن ) +۰
( پوند اصاف وسبت)» پپلوی 2 (بازشکاری ) ۸« اسشق ۷۸۹ بنقل از بندهد..», اقفالی
61 (باز » شاهین) قس: ارمنی 581۲ «هوبشمان ۷۸۹*: «شکره/شکا زر کننده بود . عنصری
(بلخی) کوید :

با غلامان (و) آت شکره کرد کار شکار و کار سره.
لخت فرسی ۸۷۷ ۰

۳ < شکردن (ه.م.) . * - از: شکر ۲ بنه (سبت) .

۹ - اوستا ربشه -2۵0ع5 , 6111 501002 (شکتن).پپلوی 85111625120 کردی ع
0 م 0(02000ط5 ( منمدی) : استی 5304140 ۰ 8311118 ( شکتن, ت رکیدن)
رك: هوبشمان ۷۸۸ . گیلکی 1881625120؛ خرد کردن » ریز ریز کردن.
```


## [2026-09-06T21:14:03.824Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# printed = leaf(1-based) - 15 => p163 -> leaf 178 (1-based) -> index 177\nfor i in (176,177,178):\n    print('=== index',i,'printed',i+1-15)\n    print(pages[i][:1500])\nEOF",
 "description": "Print Asbaghi page 163"
}
```


### [2026-09-06T21:14:05.625Z] TOOL RESULT

```
leaves 302
=== index 176 printed 162
safsir?                                                                                     162                                                           sakäri$

      .                           =                                                                                          1
ui         —           safsir?:                   "Vermittler"                  pers.                 Lu            sensär       ,    aram.    };san      ,   SYT.
               .                                                2
            aan                  (p. un)”.
          Dtsch.                  Sensal:                   (österr.)           mit         der       Bed.          "Vermittler,            Makler"            pers>>
          ar. >                   it. 3 B

 \                                                                                            4                                               9
Saw.        safad:!                    "Korb!               —       pers. zu sabad                , mand.             sapta,         syr.   Na®       «

                                                                      6
Au - safat                        =        safad            Q       Ve.


owe- safan:                            Pl.        v.         au,        safina.

Oz - sufün:                                Pl.         v.       au. saflna.

ala - saffiän:                                     "Ziegenleder"                  =     sahtiyän               q.    v.


Ge» - 
=== index 177 printed 163
sakbä;                                                                       163                                               sikanfabin


ee - sakbäß:                      "in Essig gekochtes                        eisen              pers.          ka           serkebä     1,
             Mp.ox33»                   serke          2, syr. Yasa °

u            - sakbinaf:                   "eine        Arznei"           arabisierte        Form v. pers. „JS. sakbina,
        lat.         sagapenum               4     aram.           Las.


owsle - sakdis:                       "more        canino",           syr.     ng         (p.owl          )

=. - sukkar:                 "Zucker"                       pers.
                                                                      .
                                                                      Au sekar             mp. Iyu Sakar
                                                                                                                    6 ”, mand.      Sikar
        (p. 2)               7, syr.               pa.                                             —.
        Sachar:             "Zucker"              a     skr.         > pers.        > griech.           9, frz.           sucre,    engl.
        sugar,          dtsch.             Zucker.


ge - sukurraß                     = sukurrußa                 q. v.

                                                                                                       
=== index 178 printed 164
sakühan                                                                      164                                                     samäsir

 ,    Pr
que        -        sakühanf:             "dreieckige              stachlige               Pflanze"          pers.,        syr.yuad!.


Ayo            -    salähdär:              "Schwertträger"                       pers.       2, eigentlich             nur    eine   Zusammen-
      setzung             v.       ar. ge). saläh                 u.    pers.         suff.           .) där.


su.    -       salähif:              PL.       v. Le.            sulhafä          go. v.


Se - salärl:                       "eine         Art Mantel"             Nisba v..YL,                   sälär     q. v.      3,

Sul -          salband:              "Kopfbedeckung"                    <        pers. Su               Sarband       s.   sarbad    a


er -       salfam:              "weiße           Rübe"          = pl Saldam                 a.    v.    5,


koals -        sulhafä:              "Schildkröte" << pers.                                kl,         sulähpä,       sürähpä     mw
      suräx          "Loch"              © +        p& "Fuß" —T mp. „u pay Caw.                                 päd.

got» - sulhafi:                      "Schildkröte"                 = sulhafä q. v.

asaal. -           sulhafiyya              =     sulhafä          q.    v.


a,» - salma               =     sarmag           q.    V.


Zrles - samarüh:
```


## [2026-09-06T21:14:16.113Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT sugar/crocodile ===\" && grep -n \"^SUGAR\\|^CROCODILE\\|^SACCHARINE\" SKT.txt | head && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor kw in ['SUGAR','CROCODILE']:\n    i=t.find('\\n'+kw)\n    print('---',kw); print(t[i:i+700])\nEOF",
 "description": "Grep Skeat for sugar and crocodile"
}
```


## [2026-09-06T21:14:17.045Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT Zucker ===\" && grep -n -i \"sakkara\\|sarkara\\|zucker\" LKT.txt | head -20",
 "description": "Grep Lokotsch for Zucker"
}
```


### [2026-09-06T21:14:17.848Z] TOOL RESULT

```
=== SKT sugar/crocodile ===
--- SUGAR

--- CROCODILE
```


### [2026-09-06T21:14:17.911Z] TOOL RESULT

```
=== LKT Zucker ===
315:44.  Ar.  'akida: 'Rosenkonserve,  Bonbon',  plr.  'akiVid; hieraus  tk.  akyde  sekeri  'Karamel),  Ger- stenzucker' [Kelökian  Kämos  855]  od. kurz  akede  [A.  Hindoglu,  Dictionnaire Turc-Fran(;ais.  Vienne  1838.  S.  329]. Wohl  aus  dieser  Form  rum.  acadea, acadele  'dass.'.
431:'Schweiß',  ^arak  at-lamr  'Schweiß  der Datteln',  d.  h.  Datlelsaft,  ein  berauschen- des Getränk.  In  Ostindien  heißt  'arak ein  starkes  Getränk,  das  aus  gegorenem Reis,  Zucker  und  Kokosnüssen  zube- reitet wird.  Nach  Europa  ist  das  Wort gekommen,  nachdem  im  mal.  Archipel Kolonien  errichtet  waren.  Daher  haben Italiener  und  Spanier,  die  dort  keine besaßen,  das  Wort  auf  anderem  Wege erhalten.  Sp.  arac,  altsp.  arrequi(n), frz.  arakj  rack,  pg.  araquc,  araca,  rak, engl,  arrack,  rack,  ndl.  arak,  dtsch. Arrak.  Aus  dem  ar.  Adjektiv  'araki wohl  das  frz.  Argot  woit  riquiqui 'Schnaps'.  Die  tk.  Form  ist  ebenso  raki, woraus  rum.  rachiü  'Branntwein',  rachier 'Branntweinbrenner',  racliierie  'Brenne- rei'. Russ.  arak.  [Kluge  22.  Hobson- Jobson  36/37.  DE  196/197.  Devic  DEt 33/34.  Gorjajew  5.  —  J.  de  Sousa,  Vesli- gios  da  lingua  arabiga  em  Portugal.  Col- lecijäo  etimologica  das  palavras  e  nomes portugueses  que  tem  origen  arabiga.  Lis-
635:Name  zweier  Feiertage,  nämlich  1.  das seket'  bairamy  'Zuckerbairam',  auch großes  Bairam,  als  Ende  des  Fasten- monats Ramadän  in  den  ersten  Tagen des  Monats  Sawvväl  und  2.  das  korban bairamy  'Opferbairam'  am  10.  Du'l-higge zur  Erinnerung  an  das  Opfer  der  Pilger in  Mekka.  Hieraus  rum.  bairam  'Fest, Bairamfest'.  Im  angloind.  beiramee, byraniee,  byrampaut  'ein  feiner  Woll- stoff, der  schon  von  IBN  BATTÜTA um  1343  erwähnt  wird  [IB  248].  [Hob- son-Jobson 81/8:2.
653:'Kuchen  aus  Mandeln  oder  Rosinen  mit Honig  und  Zucker  hergestellt' ;  hieraus rum.  baclava  'Honigkuchen,  Marzipan'.
1470:'Zuckerwerk'  [aus  pers.  pänid,  Vb.  fänl- dän' den  Zucker  rafSnieren',  s.  SCHWARZ in  ZDMG  LXXIV,  238  u.  245];  hieraus mit  ar.  Art.  und  häufigem  Wechsel  von t  und  k  sp.  alfenique,  pg.  alfenim  'Teig aus  Zucker  und  süßem  Mandelöl',  frz. alphenic  'Kandiszucker,  Teig  aus  Mandeln und  Zucker';  frz.  penid  'sucre  tors';  in der  alten  Pharmazie  saccharum  peni- dium.    [DE  112.    Devic  DEt  27.
1948:'Süßigkeit',  ebenso  tk.  hdwa  'Süßwerk; aus  Sesammehl,  Honig  und  Zucker  her- gestelltes Gebäck';  hieraus  rum.  halva, halvifä,  alva,  alvifä  'aus  Eiweiß,  Nüssen und  Zucker,  mit  Honig  oft  rotgelb  ge- machtes Zuckerwerk',  alvagiü  'Zucker- bäcker'; russ.  gal'wa,  hal'wa  'Zucker- werk'; angloind. /imZj«;«  'aus  Milch,  Zucker, Mandeln  und  mit  Kardamome  wohl- riechend gemachtem  ghee  [aus  gleich- bedeutendem hind.  Wort  'Butter  aus Büffelmilch,  die  in  eine  Art  Öl  verwandelt ist'] ;  mit  ar.  Art.  pg.  alfeloa  'Einmach- zucker', alfeloeiro  'Zuckerbäcker'.
2504:105!2.  Ar.  kandl: Adj.  zu  kand  nach  ar.  Originalwörter- büchern  'eingedickter  Zuckerrohrsaft', wahrscheinlich  durch  zweimaliges  Ko- chen erzielter  'Rohrzucker'  [SCHWARZ in  ZDMG  LXXIV,  244];  hieraus  it.  zuc- chero  candl,  frz.  sucre  candi,  sp.  azücar cando,  pg.  candil,  dtsch.  Kandiszucker, ndl.  kandij,  engl,  kandy,  Jcandtj-sugar ; dazu  die  Vb.  it.  candire,  frz.  candir  'über- zuckern', kat.  candir  'Früchte  ein- machen' ;  dtsch.  kandieren  'verzuckern', Konditor  'Zuckerbäcker'.  [DE  247. Eguilaz  358.    ML  (3899.
2590:'Merk,  Zuckerwurzel,  Sium  sisarum', eine  Umbellifere ;  hieraus  sp.  chirivid, pg.  cherivia,  alquirivia,  prov.  escaravi, afrz.  escherviz,  frz.  chervis,  chiroui; mlat.  cervüla.  [DE  254.  Eguilaz  374. ML  1697  a.
2810:N.  pr.,  Name  einer  Rasse  oder  Kaste  in den  West  Ghats  im  westlichen  Indien, deren  Angehörige  sich  oft  als  Arbeiter verdingten.  Hieraus  entstand  der  Name angloind.  engl,  coolg,  dtsch.  Kuli  'Ge- mieteter Arbeiter  oder  Lastträger',  bes. diejenigen  Arbeiter,  die  aus  Indien  oder China  in  überseeische  Pflanzungen  ver- schickt wurden.  Allerdings  verstand man  in  Westindien  nicht  chines.  Ein- wanderer darunter,  sondern  die  india- nischen Arbeiter,  die  in  den  Zucker- pflanzungen die  Stelle  des  Negersklaven annahmen  [vgl.  E.  G.  Bowra,  Notes  and Queries  on  China  and  Japan  1867.  S.  77]. Frz.  cooU,  couli;  dtsch.  auch  fig.  Tinten- kiili    'journalistischer  Lohnschreiber'
2945:Ursprünglich  *  'etwas  Rundes',  dann 'rundes  Brot'  [kurna  al-haläwl  'Marzi- pan' nach  Berggreen,  Guide  fran^ais- arabe  vulgaire.  ^Upsal  1844.  S.  266]; hieraus  sp.  alcorza,  pg.  alcorce,  alcorga 'sehr  heller  Zuckerteig,  aus  dem  man allerhand  Figuren  macht'  [DE  94].
3338:Jahrhundert  ist  siz.  marzapane,  neapol. marzapane  belegt.  Im  XIV.  Jahrhun- dert wurde  mit  diesem  Wort  der  Inhalt der  genannten  Kiste,  nämlich  ein  aus Zucker,  Mandeln  und  Rosenwasser  her- gestelltes Zuckerwerk  bezeichnet:  it. marzapane,  frz.  marsepain,  massepain, sp.  mazapän,  pg.  massapäo  [mit  offen- barer Anlehnung  an  pane,  pain,  pao <^  lat.  panis  'Brot'];  vgl.  noch  prov. massapan  'Schachtel'.  Engl,  marchpane [in  Anlehnung  an  March],  dtsch.  Mar- zipan, ndl.  marsepein,  schwed.  marsi- pan;  russ.  marcipan.  —  [Blarci  panis 'Markusbrot'  ist  nur  Volksetymologie; die  vorliegende  Ableitung  stammt  von A.  KLUYVER  in  ZfdWt  VI,  59/68  ]  [ML 5440.  MWiD  86.
3353:'Zucker'  [nach  DE  164];  hieraus  sp.  kat. almibar  'Sirup',  almibarar  'mit  Zucker- seim überziehen,  süße  Worte  geben', almibarado  'süßtuender  Mensch'.  — [Eguilaz  222  hat  als  Grundwort  miba.'
3704:'Fünf  [Horn  NpEt  S.  73,  Nr.  328;  vgl. päng-äb  'Pandschab',  engl.  Schreibung Punjaub  'FOnfstromland'] ;  hieraus  engl. punch,  dtsch.  Punsch,  ein  Getränk,  das aus  fünf  Zutaten  hergestellt  wird:  Arrak, Zucker,  Zitronensaft,  Wasser  (oder  Tee) und  Gewürz  (Zimt)  [SCHILLER  läßt  in seinem  Punschlied  das  letzte  aus  und singt:  ,Vier  Elemente  /  Innig  gesellt  / Bilden  das  Leben  /  Bauen  die  Welt."]; sp.  ponche,  rum.  punciü,  russ.  punS. [Ho'oson-Jobson  737/739.    Kluge  353.
3753:hieraus  bulg.  peksimit,  serb.  peksimet, peksimada;  rum.  pesmet  'Zwieback',  il. pasiimata  'pasta  con  zoflerano  e  cantucci Cotta  a  pane,  Zuckerbrot'  [v^l.  auch TToEn^olbi,  Jannarakis,  Deulsch-Neugr. Wörterbuch  S.  1361b].  [Miki  SlEtWb 236.    ML  6319.
3759:*Gelee'  [Kel6kian  Kämus324a;  vielleicht wie  tk.  paluze  'Gelee  aus  Stärke  und Zucker'  aus  pers.  pälüdä  'Süßspeise  aus Honig  und  Mandeln'];  hieraus  rum. peltea  'Obstgelee,  eingekochter  Frucht- satt'.
3849:dazu  rähat  hallfüm  'Erquickung  des Gaumeus',  tk.  korrumpiert  zu  rahat- lokum,  Name  einer  tk.  Süisspeise,  ge- wöhnlich in  Form  einer  Wurst,  die,  aus Konstantinopel  stammend,  sich  selbst  in europäische  Delikateßhandlungen  Ein- gang verschafft  hat;  hieraus  mit  Unter- drückung des  ersten  oder  zweiten  Be- standteiles bulg.  lokum  'Zuckerteig  mit Mandeln  und  Rosenöl',  serb.  lokuma 'Art  harter  Krapfen' ;  rum.  lucumä  'süße Pastete'  [wie  ngr.  \ouKOU)nac],  rahat 'Zuckerteig',  rahatlicnm  'dass.',  rahagiü 'Zuckerwarenverkäufer',  frz.  locoum  'Süß- speise'; dtsch.  Rahatlukum.  [Bern  Sl EtWb  730.
3934:'Fruchtsaft,  Obsthonig'  [vielleicht  selbst aus  dem  Pers.] ;  hieraus  sp.  rob,  arrope, kat.  rop,  arrdp,  pg.  robe,  arrobe,  frz.  rob, it.  robbo,  rob;  ndl.  rob,  engl,  rob  'Frucht- saft mit  Zucker  und  Honig'.  [DE  204. Devic  DEt  196.  Eguilaz  290.  484.  ML 7346.
4167:'Trank'  [Vb.  sariba  'trinken'],  hieraus mlat.  siröpus,  sirüpus,  it.  sciroppo,  si- roppo,  frz.  sirop,  syrop,  prov.  isarop, kat.  aixarop,  sp.  jnrope,  pg.  xarope, enxarope,  rum.  sirop,  sirup;  ndl.  siroop, stroop  [in  Südhmburg  dial.  sroep,  vgL GRM  V,  171],  dtsch.  Sirup,  engl,  syrop, syrup;  russ.  sirop,  serb.  sirup,  äech. syrup,  poln.  syrop.  —  Aus  der  gleich- bedeutenden ar.  Form  surba,  sarba wurde  zur  Bezeichnung  eines  kühlenden Trankes  über  tk.  serbet  'Kühltrank'  it. sorbetto  'süßes  Fruchteis'  [mit  Einwir- kung von  it.  sorbire  'schlürfen'],  frz. Sorbet,  sp.  sorbete,  pg,  sorvete,  rum.  ger- bet 'dicker  Obstsaft';  ndl.  sorbet,  engl. sherbet,  shrub,  dtsch.  Sorbet,  Scherbet 'ein  aus  Wasser,  zerstoßenen  Rosinen, Zucker,  Zitronensaft,  Ambra  und  ähn- lichen Zutaten  gemischter  Kühltrank'. [DE  218  und  417.  Eguilaz  495  und  513. ML  7675  und  7711.
4200:'Sand-  oder  Körnerzucker',  präkrt  sak- kara,  peis.  säkär;  hieraus  einerseits gr.  ödKxapov,  lat.  sacchartm,  anderer- seits ar.  sukkar.  Aus  dei-  letzteren Form  wurde:  it.  zucchero,  sard.  tuk- karti,  frz.  sucre,  sp.  azncar,  pg.  agucar; dtsch.  Zucker,  engl,  sugar,  ndl.  suiker, dän.  siikker,  schwed,  socker;  poln.  cu- kier,  cech.  cukr^  serb.  cukra,  cukara, klruss.  cukor,  cukur.  Dagegen  stammen aus  dem  Gr.  die  Formen  russ.  sahar, bulg.  zahar;  rurn.  zahär,  zähar;  aus dem  tk.  Seker  wurde  bulg.  seker,  serb. äecer.  Vgl.  ngr.  odKxap;  dtsch.  Saccharin. [DE  228.  Eguilaz  325.  ML  8058.  Bern SlEtVVb  131.    Devic  DEt  211/212.
4436:1965.  Ar.  tabäsir: 'Bamliuszucker',  d.  h.  zuckerhaltige  Kie- selknollen, die  an  den  Knoten  der  Bam- busstänime  abgeschieden  werden  [selbst aus  dem  Ind.  stammend,  ZDMG  L.  650, und  zwar  von  sskr.  tavakhshira];  hiei- aus  pg.  tabaxir  'Bambuszucker',  t.  dos alfaiates  [aus  ar.  al-liajjät  'der  Schnei- der'] 'Schneiderkreide',  frz.  tebachier, tabaschir  ;  engl,  tabasheer,  dtsch.  Taba- schir.  Über  tk.  tebesir  'Kreide'  wurde rum.  tibi^ir  'dass '  [DE  345.  Eguilaz 497.  Löbel  EITAP  95.  Hobson-Jobsou 887.    Lammens  Rem  231.
```


## [2026-09-06T21:14:30.307Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4195,4205p' LKT.txt && python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Sand-  oder  Körnerzucker' in p: print('LKT leaf',i,'printed',i-26)\n    if 'ödKxapov' in p or 'sukkar' in p and 'Körnerzucker' in p: pass\nEOF\necho \"=== SKT ===\"; grep -n -i \"sugar\\b\" SKT.txt | head -5; echo \"=== SKT croc ===\"; grep -n -i \"crocodile\" SKT.txt | head -5",
 "description": "Locate LKT leaf and Skeat entries"
}
```


### [2026-09-06T21:14:32.127Z] TOOL RESULT

```
Auch  asrafi  [beide  Wörter  mit  pers. Endung],  eine  Goldmünze,  einem  Denar gleich ;  hieraus  pg.  xarafim  'eine  Münze in  Ostindien  mit  wenig  wechselndem Werte,  etwa  300  reis'.  [Constancio Dicc  974.    DE  353/354.
1854.  Ar.  sarita:
'Seil,  Schiffstau  aus  Haifa-  oder  Palmen-
faser'; hieraus  sp.  jareta  'Saum,  Ein- schlag', pg.  xareta  'F'ischernetz',  sp. jaretas,  pg.  xaretas  'Netze,  die  vei'hin- dern  sollen,  daiä  die  Seeleute  über  Bord fallen'.  [Constancio  Dicc  974.  DE  354. Eguilaz  431.
1855.  Sskr.  särkarä:
'Sand-  oder  Körnerzucker',  präkrt  sak- kara,  peis.  säkär;  hieraus  einerseits gr.  ödKxapov,  lat.  sacchartm,  anderer- seits ar.  sukkar.  Aus  dei-  letzteren Form  wurde:  it.  zucchero,  sard.  tuk- karti,  frz.  sucre,  sp.  azncar,  pg.  agucar; dtsch.  Zucker,  engl,  sugar,  ndl.  suiker, dän.  siikker,  schwed,  socker;  poln.  cu- kier,  cech.  cukr^  serb.  cukra,  cukara, klruss.  cukor,  cukur.  Dagegen  stammen aus  dem  Gr.  die  Formen  russ.  sahar, bulg.  zahar;  rurn.  zahär,  zähar;  aus dem  tk.  Seker  wurde  bulg.  seker,  serb. äecer.  Vgl.  ngr.  odKxap;  dtsch.  Saccharin. [DE  228.  Eguilaz  325.  ML  8058.  Bern SlEtVVb  131.    Devic  DEt  211/212.
1856.  Ar.  sarkl:
'Östlich'  [Adj.  zu  sark  'Osten'] ;  hieraus a)  ar.  musarki,  vulg.  moserkt,  eine  Art Leder,  das  in  den  östlichen  Ländern Nordafrikas,  bes.  Marokko,  hergestellt und  zu  feinen  Stiefeln  verwendet  wurde; mit  dem  häufigen  Wechsel  von  m  >  h sp.  kat.  borcegul,  pg.  borceguim,  frz. brodequin  'Halbstiefel',  it.  borzacchino. [Die  Ableilung  von  Eguilaz  348  aus bagdädi  'bagdadisch'  ist  lautlich  nicht möghch.]
(b)  Bezeichnung  eines  Windes,  heut- zutage 'Südwind'  Mrklje;  hieraus  it. scirocco,  siz.  sciloccu,  sp.  siroco,  jaloque, pg.  xaroco,  frz.  siroc;  engl.  ndl.  sirocco, dtscb.  Sirokko  'heißer  Südwestwind'. [Aus  den  europäischen  Formen  mit  l haben  die  Araber  ihr  saJük,  saläk  zurück- genommen).
(c)  Auf  das  ar.  Grundwort  sarki  geht auch  sicherlich  der  aus  byzantinischen Quellen  bekannte  Name  eines  zwischen Ägypten  und  Syrien  zeltenden  Beduinen- stammes lapaKfivoi  zurück;  hieraus  zur Bezeichnung  aller  islamischen  Völker des  Orients  lat.  Saraceni,  Adj.  saracenus 'sarazenisch',  it.  saracino  'Stechpuppe oder  hölzerner  Mann,  nach  dem  die Reiter  mit  der  Lanze  stießen',  saracenüo 'sarazenisch',  saracwiffre 'seil  warz  werden (Weintraube)',  hz.  sarrasin  'Buchweizen' [nach  de  Candolle  im  XV.  Jahrhundert aus  der  Tartarei  und  Rufsland  nach Mittel-  und  Westeuropa  eingeführt:  Poly- gonum  fagopyrum],  sarassine  'Gatter', Sarrazin  im  Argot  der  Pariser  Setzer 'Streikbrecher',  sp.  sarraccino  'Buch- weizen', überall  in  der  Bedeutung  'Sa-
10*
LKT leaf 175 printed 149
=== SKT ===
2782:faruf/t  nuidc  of  sugar.  The  word  in  Aryan (Peri.)  ;  cl.  bit.  **A./nd«rr.w.  sweetmeat*, /kAanda.  a  broken  jiiccc.  Hex.  sngisr-iafu/y, Ital.  tmtMer»  4aniii.
10722:Xiozen^,  a  rhombus ;  a  small  cake  of flavoured  sugar,  Ac,  orig.  of  a  diamond shape.  (F.)  Formerly  ioien^^  esp.  a  shield of  a  diamond  shape  ^in  heraldry).— O.  F. losen^^  loungt  (.F.  losangi),  •  locenge. Origm  disputttt  Cf.Span./p/oy^ic,  a  loicnge, rhombus ;  prob.  from  ioia^  a  square  stone for  paving  (whence  /<»ar,  to  pave).  Per- haps from  L.  laud',  stem  of  Icnu,  praise; for  we  find  Span,  iauda^  a  VQBi\>^VAMb  <ii>>)Bk an  epitaph  (Uies).
11368:k  vynip  made  from  sugar. \  It  thould  rather  be  meiasses. molasses;  cf.  Span,  melata riiattuj,  made  with  honey.  *
15130:Punch  (3),  a  beverage.  ( Hindi. -SIct.) So  calloi  from  consisting  o\  fivt  inj^redients, spirit,  water.  Icmoo-juicc.  sugar,  %pice  ;  in- trodoccd  from  Indie,  b^  vk)  ot  Ocia,-«  mcxk.
15201:Purl  {7),  spiced  beer.  (F.  -  L.)  lo Fhillips,  ed.  1 70^1.  But  it  should  be  pearl. It  was  a  term  in  cookery;  thus  sue  re  per U is  sugar  boiled  twice,  bcuillen  perU^  jelly- broth.  Cf.  Q.  perleUy  to  pearl,  rise  in  small bubbles  like  pearls.     See  Pearl.
=== SKT croc ===
```


## [2026-09-06T21:14:36.727Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T21:14:36.734Z] TOOL RESULT

```


```


## [2026-09-06T21:14:40.985Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%B1",
 "prompt": "Give the Persian etymology of شکر (šekar/šakar) 'sugar': Middle Persian form, Sanskrit śarkarā, any mention of Pali/Prakrit, and the Arabic borrowing سكر. Quote exactly."
}
```


## [2026-09-06T21:14:42.495Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%85",
 "prompt": "Give the Persian etymology of شرم (šarm) 'shame': Middle Persian, Proto-Iranian, Proto-Indo-European reconstruction, and cognates (Avestan fšarəma-, Old English hearm, etc.). Quote exactly."
}
```


### [2026-09-06T21:14:48.701Z] TOOL RESULT

```
# Persian Etymology of شرم (šarm) 'shame'

## Etymology Chain

**Middle Persian:** 𐭱𐭥𐭬 (šʿm /šarm/)

**Proto-Iranian:** *fšarma- ("shame"), derived from *fšar- ("to shame, be ashamed")

**Proto-Indo-European:** *pḱormo- ("shame, suffering, pain"), from *pḱer- ("to suffer, feel grief and shame")

## Cognates

The entry specifies cognates including:
- Khotanese: kṣär- ("be ashamed")
- Avestan: 𐬟𐬱𐬀𐬭𐬆𐬨𐬀 (fšarəma, "shame")
- Proto-Slavic: *sȏrmъ ("shame")
- English: "harm"

The documentation notes these terms share common ancestry through the Proto-Indo-European root concerned with suffering and emotional pain.
```


### [2026-09-06T21:14:49.800Z] TOOL RESULT

```
# Persian Etymology of شکر (Sugar)

**Middle Persian Form:**
"From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[𐭱𐭪𐭥](/wiki/%F0%90%AD%B1%F0%90%AD%AA%F0%90%AD%A5#Middle_Persian "𐭱𐭪𐭥")_ (škʿ /⁠šakar⁠/)"

**Sanskrit Origin:**
"from [Sanskrit](https://en.wikipedia.org/wiki/Sanskrit "w:Sanskrit") _[शर्करा](/wiki/%E0%A4%B6%E0%A4%B0%E0%A5%8D%E0%A4%95%E0%A4%B0%E0%A4%BE#Sanskrit "शर्करा")_ (śárkarā, "ground or candied sugar, originally meaning grit, gravel")"

**Gandhari Intermediate:**
The etymology chain passes through "from [Gandhari](https://en.wikipedia.org/wiki/Gandhari_language "w:Gandhari language") _[𐨭𐨐𐨪](/wiki/%F0%90%A8%AD%F0%90%A8%90%F0%90%A8%AA#Gandhari "𐨭𐨐𐨪")_ (śakara)"

**Arabic Borrowing:**
The page documents Etymology 2 as "[Borrowed](/wiki/Appendix:Glossary#loanword "Appendix:Glossary") from [Arabic](https://en.wikipedia.org/wiki/Arabic "w:Arabic") _[شُكْر](/wiki/%D8%B4%D9%83%D8%B1#Arabic:_gratitude "شكر")_ (šukr)" but this refers to the "thankfulness" sense, not the sugar meaning.

No Pali reference appears in the provided content.
```


## [2026-09-06T21:15:08.850Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%AC%CE%BA%CF%87%CE%B1%CF%81%CE%BF%CE%BD",
 "prompt": "Etymology of Ancient Greek σάκχαρον 'sugar' — source language (Pali/Prakrit/Sanskrit/Middle Indic), earliest attestation, and Latin saccharon/saccharum. Quote exactly."
}
```


## [2026-09-06T21:15:11.034Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CF%81%CE%BF%CE%BA%CF%8C%CE%B4%CE%B5%CE%B9%CE%BB%CE%BF%CF%82",
 "prompt": "Etymology of Ancient Greek κροκόδειλος/κροκόδιλος 'crocodile, lizard' — the traditional derivation from κρόκη 'pebble' + δρῖλος 'worm', and what Beekes or modern scholars say (Pre-Greek?). Quote exactly. Also give the etymology of κρόκη 'pebble'."
}
```


### [2026-09-06T21:15:13.574Z] TOOL RESULT

```
# Etymology of σάκχαρον

Based on the Wiktionary content provided, I cannot supply the etymological details you've requested. The page shows that σάκχαρον (sákkhăron) is "an alternative form of σάκχαρ (sákkhar)" but does not include:

- Source language information (Pali, Prakrit, Sanskrit, or Middle Indic origins)
- Earliest attestation dates
- Details about Latin derivatives (saccharon/saccharum)

The "Further reading" section references Bailly's Greek-French Dictionary and the Logeion database, but these external sources are not quoted in the article itself. To obtain this etymological information, you would need to consult those reference works directly.
```


### [2026-09-06T21:15:16.846Z] TOOL RESULT

```
# Etymology of κροκόδειλος

## Traditional Derivation

The traditional etymology proposes: "perhaps from _κρόκη_ (krókē, 'pebble') + _δρῖλος_ (drîlos, 'worm'), because crocodiles like resting on flat stones."

The rationale suggests this compound describes the animal's behavior of resting on pebbles.

## Modern Scholarly View

Beekes dismisses this etymology entirely, stating it "should be forgotten." The Wiktionary article notes the etymology is of "Unknown" origin overall.

## Etymology of κρόκη

The document provided does **not** include the etymology of κρόκη itself. While the entry mentions κρόκη as meaning "pebble," no separate etymological information about that word is supplied in this Wiktionary page.

**Note:** A Sanskrit parallel is cited—_कृकलास_ (kṛkalāsa, "lizard, chameleon")—said to derive from words meaning "pebble" and "sit," offering typological support for the traditional Greek etymology, though Beekes rejects even this comparison.
```


## [2026-09-06T21:15:36.430Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sugar",
 "prompt": "Quote the full etymology of \"sugar\", including Old French/Medieval Latin succarum, Arabic sukkar, Persian shakar, Sanskrit sharkara, and the note about Prakrit/Pali."
}
```


## [2026-09-06T21:15:38.031Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/crocodile",
 "prompt": "Quote the full etymology of \"crocodile\": Greek krokodilos, kroke 'pebble' + drilos 'worm', Latin crocodilus, Medieval Latin cocodrillus, Old French cocodril, Middle English. Also any note on the folk-etymology status."
}
```


### [2026-09-06T21:15:41.338Z] TOOL RESULT

```
# Etymology of Sugar

According to the Online Etymology Dictionary, the word "sugar" originates from "Old French _sucre_ 'sugar' (12c.), from Medieval Latin _succarum_, from Arabic _sukkar_, from Persian _shakar_, from Sanskrit _sharkara_ 'ground or candied sugar,' originally 'grit, gravel.'"

The entry notes that the Sanskrit term is "cognate with Greek _kroke_ 'pebble'," indicating a shared linguistic root emphasizing the granular nature of the substance.

The word entered English in the late 13th century and subsequently spread throughout European languages via the Arabic borrowing. The entry explains that "Its Old World home was India" and that sugar remained a luxury item in Europe until Arab cultivation in Sicily and Spain, eventually becoming competitive with honey as a sweetener following the Crusades.
```


### [2026-09-06T21:15:43.475Z] TOOL RESULT

```
# Etymology of Crocodile

**Full Etymology Chain:**
The word traces back through multiple languages: Middle English *cokedrille/cocodril* (c. 1300) → Old French *cocodrille* (13c.) → Medieval Latin *cocodrillus* → Classical Latin *crocodilus* → Greek *krokodilos* (origin unknown).

**On the Proposed Compound Etymology:**
According to the source, Beekes dismisses the theory that the Greek term derived from *krokē* (gravel) plus *drilos* (worm), stating this etymology "should be forgotten." The document notes that Herodotus claimed it was "an Ionic name for a kind of lizard, transferred to the crocodile," though the true origin remains obscure.

**Folk-Etymology Status:**
The source does not explicitly classify this as folk-etymology. However, by documenting Beekes's rejection of the "gravel-worm" compound theory, it implicitly treats that proposed explanation as unreliable scholarship rather than an accepted etymological path.
```


## [2026-09-06T21:15:48.713Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"=== $f\"; grep -c \"\" $f 2>/dev/null; grep -n \"ساکار\\|سوخار\\|ساخار\" $f 2>/dev/null | head -10; done",
 "description": "Grep Moin for sakaroz and soxari"
}
```


### [2026-09-06T21:15:50.535Z] TOOL RESULT

```
=== MON_part1.txt
99339
21277:ساکارومیستاسه که هوازی است و در برابر 
33900:همچنین قندهای دیگر از قیل ساکارز و 
40202:ساکارز و ملزیتوز موجود است و آن در 
73496:ساخارین: 2277 (.) (شیم.) گرد سیار 
80886:سوخاری: 7 (.) قسمی نان شیرننی 
96079:محتوی ۲ 1,۵ مواد قندی شیرین از ساکارز و 
=== MON_part2.txt
94500
15036:التصاق بلورهای ریز ساکارز است (بلورهای 
15037:ریز ساکارز را در تداول عامه شکر نامند.) 
15066:ساکارز» جسمی است سفیدی و بلوری به 
17491:حرارت‌های زیاد از ساکارز یا قند معمولی 
18251:از قبیل گلوکز و سوولز و ساکارز است و به 
51085:ساکارمیستاسه‌ها. مخمر آب‌جو: یکی از 
51117:گونة ساخارویسس الیسوتیدتوس و کون 
51118:ساکارومیسس آییکولا توس را باید نام برد 
51122:ساکارو میسس سرویزیه که مخمر آبجو 
51125:بو جود می‌آورد. همجنین ساکارومیسس 
=== incoming/MON/MON_2vol_Adena_v1_djvu.txt
99339
21277:ساکارومیستاسه که هوازی است و در برابر 
33900:همچنین قندهای دیگر از قیل ساکارز و 
40202:ساکارز و ملزیتوز موجود است و آن در 
73496:ساخارین: 2277 (.) (شیم.) گرد سیار 
80886:سوخاری: 7 (.) قسمی نان شیرننی 
96079:محتوی ۲ 1,۵ مواد قندی شیرین از ساکارز و 
=== incoming/MON/MON_2vol_Adena_v2_djvu.txt
94500
15036:التصاق بلورهای ریز ساکارز است (بلورهای 
15037:ریز ساکارز را در تداول عامه شکر نامند.) 
15066:ساکارز» جسمی است سفیدی و بلوری به 
17491:حرارت‌های زیاد از ساکارز یا قند معمولی 
18251:از قبیل گلوکز و سوولز و ساکارز است و به 
51085:ساکارمیستاسه‌ها. مخمر آب‌جو: یکی از 
51117:گونة ساخارویسس الیسوتیدتوس و کون 
51118:ساکارومیسس آییکولا توس را باید نام برد 
51122:ساکارو میسس سرویزیه که مخمر آبجو 
51125:بو جود می‌آورد. همجنین ساکارومیسس
```


## [2026-09-06T21:15:54.162Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '73490,73500p;80880,80895p' MON_part1.txt && echo \"=== sakarz entries ===\" && sed -n '15030,15075p' MON_part2.txt",
 "description": "Print Moin entries for saxarin, soxari, sakarz"
}
```


### [2026-09-06T21:15:54.240Z] TOOL RESULT

```
ساحلی: آ-261ه [ع. ف.] (ص‌نس..) 
منسوب به ساحل. کسی که در ساحل دریا با 
رود اقامت دارد. بلاد (شهرهای) ساحلی: 
در بابار. 

ساخارین: 2277 (.) (شیم.) گرد سیار 
سفید و شیرینی است که در آب به دشواری 
و در الکل به خوبی حل گردد و مصرت 
طبی دارد. 

پارچه‌ای چهار گوشه که در زیر بغل جامه 
دوزند؛ بغلکك. پارچة مثلث متساوی الساقین 
که از سر تریز جامه ببرند تا خشتکک را بر آن 
دورند. 
سوخ: »۰0 (.) پیازه بصل. (گیا.) پیازی که 
زیر رمیت شنت ما نت نار تر کسن: 
سوخاری: 7 (.) قسمی نان شیرننی 
خشکت و سبکد» نکشمانتا, 
سوخت: ا: (مص خم.) سوختن. (ا.) 
ماد قابل احتراق مانند زغال» نفت» بنزین و 
جز آنها. از بین رفتن بخشی از محصول 
ملک يا تمام آن بر اثر کم آبی و جز آن. 
سوخت اما: قجقت۳: [- سوخت آماینده] 
(ص‌فا.) (نو.) (فر.) کاربوراتور. ضح.- ایین 
کلمه رواج نیافته و بسجای آن همان 
کاربوراتورمستعمل است. 
=== sakarz entries ===
(سلاح آتشین): 

فنتوره: (۵-)۵0۱۲۸ (۰۱) لباس کوتاهی با 
بندهای زیاد که مخصوص شاطران بود. 
قند: ۰0۵ [معر. - کند] (ا.) جسمی است 
جامد به رنگ سفید با طعم شیرین و آن از 
التصاق بلورهای ریز ساکارز است (بلورهای 
ریز ساکارز را در تداول عامه شکر نامند.) 
ضح.- سا کارز يکي از مواد گلوسیدی است 
که از ترکیب دو «از» ۲ کرنی یکی بنام 
لوولز و دیگری بنام گلوکز حاصل شده 
است و فرمول کلیش ,,0,,آ1, می‌باشد 
و بلورهایش بنام شکر خوانده 
3 الا عمل قندسازی عبارت از آن 
است که بلورهای ریز شکر را به یکدیگر 
ملصق کنند و نتیجه را به اشکالی که مایلند 
(از لحاظ عرضه به بازار) درآورند و معمولاً 
عمل التسصاق رابه وسبله ذوب کردن 
مسقداری از ببلورهای شکر و به حالت 
بی‌شکل درآوردن آنها که عمل چسب بین 
دک ذرات بلوری را به عهده دارد انجام 
می‌دهند. قندهایی که به بازار عرضه می‌شو ند 
به اشکال مخروطی (کله قند) و مکعبی با 
مکعب ستطیل یا کلوخه‌ای که از شکررهای 
مستخرج از نیشکر و چغندر قند حاصل 
می‌شو ند قند معمولی؛ تبرزد. قندها: (شیم.) 


فرهنگك فارسی معین 


۱۳۵ 
اجسامی هستند سه تایی مر کب از کرین و 
تیدروژن و اکسیژن که در طبیعت فراوان و 
در بدن جانوران و مخصوصاً در گیاهان زیاد 
دیده می‌شوند. قند معمولی: (شیم.) - 
ساکارز» جسمی است سفیدی و بلوری به 
فرمول ,,۵,, ۵,13 با طعم شیرین؛ از آب 
سنگین‌تر؛ در نصف وزاش آب ۰ درجه 
در طوزنش آب ۱۰۰ درجه حل می‌شود 
و بر اثر حرارت گداخته می‌گردد و مایم 
حاصل به وسیلةً برودت ناگهانی به جسم 
شیشه مانندی (آب نبات) و بر اثر سرد کردن 
ملایم جسم بلور مانندی (نبات) می‌دهد. قند 
در حدود صد درجه حرارت به کارامل یا قند 
توق شین 9 رح ی 95 ۱ تقریاً کربن
```


## [2026-09-06T21:16:18.609Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('sucrose,  n')\nprint(t[i-800:i+400])\nEOF",
 "description": "Print Klein sucrose entry"
}
```


### [2026-09-06T21:16:20.311Z] TOOL RESULT

```
  subst.  suff.  -ing.
suclat,  n.,  any  of  certain  woolen  stuffs;  specif,  the European  broadcloth  ( Anglo-Indian ).  —  Hind. suqlat,  fr.  Pers.  saqallat,  a  secondary  form  of saqirlat.  See  scarlet, suer-,  form  of  sucro-  before  a  vowel, sucramine,  sucramin,  n.,  ammonium  salt  of  sac¬ charin.  —  Coined  fr.  F.  sucre  (see  sugar)  and amine.
sucrate,  n.,  compound  of  sucrose  with  a  base (chem.)  —  A  hybrid  coined  fr.  F.  sucre,  ‘sugar’, and  chem.  suff.  -ate,  fr.  L.  -atus.  See  sugar  and cp.  words  there  referred  to. sucre,  n.,  the  monetary  unit  for  Ecuador.  — Named  after  Antonio  Josd  de  Sucre,  a  Vene¬ zuelan  general.
sucro-
su>
sucro-,  before  a  vowel  suer-,  combining  form meaning  ‘sugar’.  —  F.  sucre.  See  sugar, sucrose,  n.,  saccharose  ( chem .)  —  Formed  Ir.  F. sucre,  ‘sugar’,  with  subst.  suff.  -ose.  See  sugar and  cp.  saccharose.
suction,  n. ,  the  act  or  process  of  sucking. — Form¬ ed  with  suff.  -ion  fr.  L.  suctus,  pp.  of  siigere, ‘to  suck’.  See  suck  and  cp.  words  there  referred  to. Derivative:  suction-al,  adj.
Suctoria,  n.,  a  group  of  protozoans  (zool.)  —
```


## [2026-09-06T21:16:20.605Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%88%D8%AE%D8%A7%D8%B1%DB%8C/",
 "prompt": "Show the فرهنگ معین entry for سوخاری — its definition and any origin tag (e.g. [روس.] Russian). Quote exactly in Persian."
}
```


### [2026-09-06T21:16:24.940Z] TOOL RESULT

```
# فرهنگ معین entry for سوخاری

According to the فرهنگ معین section on this page:

**Definition and origin:** "[ روس . ] (اِ. ) برشته ."

This entry identifies سوخاری as a Russian loanword meaning "toasted" or "roasted."
```


## [2026-09-06T21:16:35.789Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (470,471,472):\n    print('=== 1-based leaf',i+1,'printed',i+1-9)\n    print(pages[i][:2500])\nEOF",
 "description": "Print Walde-Pokorny Bd I p.463"
}
```


### [2026-09-06T21:16:37.364Z] TOOL RESULT

```
leaves 895
=== 1-based leaf 471 printed 462
                                                                                                                 -




462                                             kor         qor-


wahracheinlich gr. Lw., mit Ausgang nach modius, so daB dafiir keine Wzf.
auf -gh- anzunehmen ist, Uhlenbeek IP. 13,217).      Unsicher lett. sence
„Huschel“ (Prellwitz 1 155, 2 232), da sence die richtigere Form scheint
(Bezzenberger BB. 27, 175 Anm. 1; seine zw. Anreihung yon nsloven. sence
„Schlafe“ ist mir wegen des Alleinstehens des Wortes im Slay, und bes.
wegen seiner Gdf. *semcb nicht glaublich).
   Gr. xoylog, y.oyXiag „Muschel, Schneckenhaus, Sehnecke" (von Thurneysen
H. Osthoff zum 14. August 1894, Karl II. Meyer IF. 35, 232 Anm. abwei-
chend zu kagh- „umfassen“, richtiger „Flechtwerk“, gestellt, was aber den
Sinn verfehlt), und kaum als nasallose Varianten anzureihen, die Nasal-
losigkeit auch kaum aus Kreuzung mit xayXrj £ „Stein, Kiesel, Uferkies"
(a.                      Fick II 1 i>9 verbindet sie mit ir. cuailen, angeblieh
       kaghlo-) zu verstehn.
„Krause, Haarlocke" (?), ebenfalls wenig glaubwiirdig.


kor- „Reiserbesen (und damit fegen); Reisigbiindel                                        (als   Fischreuse, als
        Seihvorrich tung)“ ?
   Gr. y.ogog „Besen", xogecn „auskehren, ausfegen, reinigen", veco-xogog
„Tempelaufseher“, (der ihn rein zu halten hat), ogxo-xogog „Stallknecht“?
xoaxivov „Sieb“ (Denominativ einea *xoay,a> = *x og-axml Wiirde aber altes
verbalea „fegen“ vorauaaetzen.     Lit. kos-iu, -ti, lett. hast „aeihen“ hat idg.
a, a. dariiber, sowie gegen die Yerbd. von xoaxivov mit *sqei- „acindere,
acheiden" Vf. LEWb 2 u. Boiaacq a. v.); lat. colum „Seihkorb, SeihgefaB,
                               .



Burchachlag, Fischreuse'", colo-, -are „durchseihen, reinigen, lautern" ( *cor
slo-J   Die Yerbindung mit canlae „Umfriedigung, Hiirde", cavea „Gehege,
Kafig, Bienenstock", cavella „Korb“, a. Yf LEWb 2 a. v., unter dem Be-              .



griff „Flechtwerk“ ist mindeatens gleichwertig); lett. sarvis „Getreidesieb“,
sarwc „Windaieb‘‘ aind eathn. Lw.
      Hirt IF. 17,391        will    xogeca     unter       Annahme von idg. k- neben ku- mit
lit.   svariis „sauber, rein, reinlich“, svarinu „reinige,                              saubere" verbinden.

qor- „Kriegsheer, Krieg".
  Gr. xoigavog „Heerfiihrer, Konig, Herr“ (Ableitung von *xoiga aus *xogta
mit Formans -no-, wie z. B. got piudans „Konig von pinda „Yolk“; eben-
                  
=== 1-based leaf 472 printed 463
                         korka (kroka?)    -ela   — kormno-, krmno-                             463

„Schlachtfeld“. Sind diese durch riicklaufige Ableitung aus *qor-{o- ent-
standen oder dessen Grundlage?
  Vgl. auBer Osthoff aaO. noch Zupitza Gutt. 109 (hier unter Vermengung
mit qar- „schmahen‘‘, wie auch bei Fiek I 4 377, und anderem), Berneker 578,
Trautmann Apr. 353, 362, Bsl. Wb. 118, Mfihlenbach-Endzelin II 166.

korka (kroka?) - e la ,,Kies, Kiesel“.
  Ai. gdrkara      (carkara-h)       „Gries, Kies, Geroll, Sandzucker“; gr.               y.goxij,

xooyAXr) ..Kieselstein^.         Cartius 5 144.
                                          Verbindung mit lat. calx usw. (siehe
Yf. LEWb. 2 s. y.) ist fur carkara trotz Pedersen KZ. 36,78 wegen des
anl. Palatals gewagt; ebenso ist andrerseits fur y.ooxrj, y.Qoy.aXrj die Yer-
bindung mit ygexco „schlage“, xgoy.rj „Einschlagfaden“ in der Bed. kaum
befriedigend (s. u. qrek-) vielleieht aber bat ein *y.ogxdXa carkara erst nach
                             ;
                                                                             :



letzterer Gruppe Umstellung zu xgoxaXt} erfahren.
   DaB ai krkalasa-, krkala- „Eideehse, Cbamaleon" einer ahnlichen An-
schauung wie gr. yQox6-d[o\ilog entspringe und eine velaranlautende Neben-
form Yon garkara voraussetze (Boisacq 520), ist nicht gestiitzt.

kormen- (karinen-?) „Wiesel“.
  Ahd. as .harmo, ags. hearrna „Wiesel“ (Demin, mhd. hennslln, mnd. herme-
                   = lit. sarmuo, scrmud „Hermelin“. Ein (kelt. ?) *karmon
en, holl. hernielijri)
vermutet Meyer-Liibke ZfromPh 19, 97 als Grundlage von rhatorom. car-
man „Wiesel“. Z. B. Kluge 8 202 f. Ygl. Trautmann Bsl. Wb. 300.
  Ursprgl. nach der Farbe benannt? s. u. kerem- „Eberesche“.


kornio- „Qual, Schmerz, Schmach“.
   Aisl. harmr „Betriibnis, Kummer, Harm, Krankung' ags. Tnearm „Kummer,
                                                                     1

                                                                         ,


Schmerz, Schade“, as. harm „Schmerz, Krankung“, mnd. harm „Schmerz“,
ahd. har(a)m „Leid, Harm, Schimpf", nhd. Harm, ags. hearm, as. harm
„8chmerzlich, verletzend"; abg. sramz „Seham“; vermutlich (trotz des un-
erklarten Anlauts) av. fsarama- m. Scham(gefuhl vor)“, mp. np. sarm ds.
                                                  ,


   Zupitza Gutt. 183 (Lit.), Falk-Torp u. harme. Nicht besser fiber Harm
Luft KZ. 36, 145 ( :sqer ^chneiden'*), und Bezzenberger BB. 27, 181 Anm
=== 1-based leaf 473 printed 464
464                                                 kol-   — qost-
kol- „spinnen“?              (:   sqel- „biegen“?).

  Gr. xXa'y&co, xXcooxco „spinne“, xXcodco eig. „die Spiimerin“, y.XojozrjQ, -fjoog
„Faden, Spindel“;
  lat. coins -us oder -l „Spinnrocken“.
               ,


  S.  Schradei Sprvgl. 2 480, 3 II 263, Osthoff Yerhandlungen der41.Philo-
logenvers. Miinchen 1891, 302, Yf. LEWb. 2 s. v., Boisacq s. v. m. Lit. (ai.
krnatti- „dreht den Paden, spinnt“ besser zu qert- „drehen“; unrichtig
deutet Dohring Progr. Konigsberg 1912, 5 auch Frau Holle als „Spinnerin“).
Gegen Yerb. von coins mit q“el- „sich drehend herumbewegen“ spricht, daB
der Rocken sich nicbt dreht.
  Formell kann xXco&co ein dh-Vva.es. von einer Set-Basis k(o)lo -, kola- sein
(*klo-dh-o oder kJa-dho)\ Yerwandtschaft zunachst mit xdXadog „Korb“
(„*Geflecbt“  Saussure Mem. 2H7, Bechtel Lex. 196) ist seitens der Bed.
                   ;


nicht zwingend („spinnen“ und „flechten“ sind verschiedene Dinge), und
auBerdem ist wegen yvgyadog „Korb“ -ados als Formans abzulosen (siebe
Boisacq; es miiBte dann letzteres erst nach xaXadog gebildet sein).

qol(6)i- „Leim“.
  Gr. xoXXa   „Leim“ (*xoXia) mndl. mnd. hclen „kleben“ (Vialjan ), aksl.
                                                ;



klejs, klejb „Leim“ (urslav. Formen *kzlejh, kzhjs, kzl'e, s. Berneker 659 f.;
lit. klejal „Leim“ aus dem SI., Bruckner SI. Fremdw. 94.        Slav, -zl- Re-
duktionsstufe zu             -ol-).     Fick I 4 389, Zupitza Gutt. 113.

koli- „junger Hund, Tierjunges“                       :    s.   u.   qd- „rufen“       am Schlusse.

kolaino-s, *kolaina „Halm, Rohr“.
   Gr. xaXajuog,             xaXd/ur]   „Rohr“ (aus kjomo-s ?
                                                Eher Assimilation in *xo-
Xaju-ov, -co,          und        obgleicb solcbe von J. Schmidt KZ. 32,
                              bes. in xaXa/ud,
390 f. nur fur anlautendes 6- zugestanden wird) lat. culmus „Halm“; ahd.         ;


halm, halani, anord. halmr, ags. healm ,Halm“; apr. salme „Stroh“, lett.
salms „Strohha]m“, aksl. slama, russ. soloma, serb. slama „Stroh“. Curtius 139,
Zupitza Gutt. 182, Trautmann Bsl. "Wb. 298, Miihlenbach-Endzelin III 675.
   Aus gr. xdXafxos entlehnt sind ai. kalama- m. „eine Reisart, Schreibrohr“
(8. Froehde BB. I, 328 f.), lat. calamus „Rohr“, woraus wieder (trotz Loth

Rc. 18, 90) cymr. usw. calaf „Rohr“.
  Beziehung zu kel- etwa „diinner Schaft,                                Pfeil,      steifer   Ha
```


## [2026-09-06T21:16:49.726Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\" && grep -n \"^korka\\|^kormo\\|^k.orka\\|sarkara\\|krokal\" IEC.txt | head -10; echo \"=== SYN sugar/shame ===\" && grep -n \"SUGAR\\|SHAME\\b\" SYN.txt | head -10",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-06T21:16:49.791Z] TOOL RESULT

```
=== IEC ===
=== SYN sugar/shame ===
9664:Europe generally until the introduction | Lett. medus, OPruss. meddo, Chs] | of sugar (5.85). From it was made the | medi, etc., general Slavic ; Skt. madhy,. oldest IE intoxicating drink, the ‘mead’ | Toch. mit. Elsewhere only as ‘mead! 5 ! (5.91). or for some other intoxicating drink { Most of the words for ‘honey’ belong | (5.91). : to one of two inherited groups. In Gmc. 3. ON hunang, OE hunig, ete., gen. one of these is represented in Gothic, the | eral Gmc. (except Goth.) : Skt, han- if other in words for ‘mead’, otherwise | cana- ‘golden’, kanaka- ‘gold’, Grk | ‘honey’ is expressed by a new word de- | xvnxés ‘pale yellow’ etc. Walde-p. 6 rived from its yellow color. 1.400; Falk-Torp 417. N 1. IE *melit- ‘honey’. Walde-P. 4. Av. *paéna-, implied by paénaéna- L : 2.296. Ernout-M. 602. Grk. pé\:; Lat. | ‘prepared from honey’, NPers. angubin : mel (> Romance words); Ir. mil, W., | ‘bee-honey’, prob. as (bee’s) ‘milk’ or gj Br. mel; Goth. milip (cf. OE mil-déaw | ‘juice’ : Av. payah-, paéman- ‘milk’, Skt, : ‘honey-dew, nectar’, milisc ‘honeyed’); | payas- ‘milk, juice’, Lith. pienas ‘milk’ ; Arm. meir, Alb. mjall. (5.87). Barth. 817. i B 5.85 SUGAR ; Grk. céxxapr, etc. (late) Goth. Lith.  cukrus NG = faxape ONEEE 28,2: Lett. cukurs , Lat.  saccharum (late) Dan.  sukker Cie 7 ) It. zucchero Sw. _socker SCr.  Seéer P Fr. sucre OE tet Boh. — cukr Sp. azticar ME _ sucere, sugure, etc. Pol. cukier Rum. zahdr NE sugar Russ. sachar m Ir. ay Du. —zucker Skt.  carkara- 0 NI. stilicre OHG zucura Av. et CE ie W. stwgr MHG zucker | Br. sukr NHG zucker a rk The home of sugar and its European | the article was then only an exotic ar names is India. The companions of | product used for medical purpose. The Ir : Alexander the Great told of the Indian | cultivation of the sugar cane was intro- BR : cane which produced ‘honey without | duced in Sicily and Spain by the Arabs, fl ? bees’ (wept r&v xadduor, dre mowfor wed. | and it was only after the crusades that 0 .! HedwooGy yx obcdv, Strabo 15.694). The | sugar became the common sweetening th 4 native Indian name appears in Greek | in place of the older honey. The major- 8 4 and Latin transcriptions in the first cen- ity of European forms of the name come or tury A.D. (wédAc 7d Kaddpuvoy 7d Xeyépevoyv | through Arabic via Spanish or Italian. ¥0 oakxapt, Peripl. 14; caxxyapoy eldos dy Schrader, Reallex. 2.705 ff. W Bédtros év "Ivdig xal rH ebdalporr ’ApaBig Skt. carkara- ‘gravel, grit? (AV +) W mennyoros, ebptoxouevoy éxl rOy xadduov, | later ‘sugar’ : Grk. xpdn, xpoxéd7 ‘peb- Y Diosc. 2.104; Saccharon et Arabia fert, | ble’. Walde-P. 1.463. th sed laudatius India, est autem mel in Hence, through a later Prakrit form *; harundibus collectum, Plin. 12.32), but | like Pali sakkhara-, the following: ur
28788:16.45 SHAME (sb.)
```


## [2026-09-06T21:16:57.716Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '5.85 SUGAR' in p: print('SUGAR leaf',i,'printed',i-24)\n    if '16.45 SHAME' in p:\n        print('SHAME leaf',i,'printed',i-24)\n        j=p.find('16.45 SHAME'); print(p[j:j+2500])\nEOF",
 "description": "Print Buck SHAME section"
}
```


### [2026-09-06T21:17:00.075Z] TOOL RESULT

```
SUGAR leaf 430 printed 406
SHAME leaf 1224 printed 1200
16.45 SHAME (sb.)
; Goth. gariudez (aiwiski, Lith. géda y, alba aloxuvn skanda) Lett. kauns Gt: (erp0™ ON kinnrodt ChSl. studi, sramit wpm] 5 Dan. skam SCr. __stid, sram . pudor, ver éoundia Sw.  skam Boh. stud It vergogna OE sceamu Pol. wstyd, wslydliwos¢ a honte ji ME _ shame Russ. styd, stydlivost’ Sp. el NE poke Skt. lajja-, hri-, vrida- um. Tut ire Du. _ schaamte Av. _—_ fiarama- i ane ae OHG coe sake Rite ockel d- MHG _scham(e), scham(e)de W. ane et NHG  scham
Br. mez
Most of the words listed ae used not oily for the subj. sense of ‘shame’, but also or even more commonly for the obj. shame, dishonor, disgrace’ (note the econdary differentiation in NHG scham ys, schande).
In some an earlier sense of ‘respect, reverence or modesty’ led to ‘shame’ in a good sense. In others, as shown by usage or etymology or both, ‘shame’ in a bad sense was the primary notion. Thus, for example, Grk. aldws and alcxtvy are contrasted in origin and in their prevail- ing usage. Several are connected with words for ‘red’ through ‘blushing’ as a sign of shame.
1. Grk. aléés, mostly ‘shame’ in good ny ee ipa modesty’, iG te Hat, eS be ashamed, a mee) respect’, prob. : Goth.
m Tevere’, Skt. id- ‘praise, suppli-
) ° ho ft. *ais-d-, extension of *ais- in Meco: NHG ehre ‘honor’, etc.
. I ee Boisacq 22. Feist 27 f. bona” na mx vn, beside aloxivw ‘dis- ; an pate dishonored, feel shame’, ‘ithe shame, disgrace’, prob. fr. race! aa ot - Mwiski ‘a shame, dis- Coe Bwisc ‘dishonor, offense’, Piz Ugly, Tepulsive’, etc. Walde- Gk. ae 30. Feist 30, tet : ne 7 in a Grk. Tespect, ‘ N ea, umiliation , NT OUP, algo ¢ ame’: &rpémw ‘turn
0 Put to shame’ (NT, etc.),
used mostly in mid. ‘hesitate’ and ‘give heed to, respect, reverence’ (Hom.+), later ‘feel shame’ (Polyb., NT), as reg. in NG.
2. Lat. pudor (also ‘modesty’ as most- ly the borrowed Romance words, It. pudore, Fr. pudeur, etc.), with vb. im- pers. pudet ‘feels ashamed’, prob. as orig. ‘feel repulsed or cast down’ : repudium ‘divorce, repudiation’, tri-pudiwm ‘a cer- tain dance’, etc., those fr. the root of’ pavire ‘beat, stamp’ (or: pés, pedis
‘foot’?). Walde-P. 2.12. Ernout-M. 761, 820. Lat. verécundia, also ‘bashfulness,
modesty’ (> It. vergogna, Sp. verguenza; Fr. vergogne obs.), beside verécundus ‘ashamed, bashful, modest’, fr. veréri ‘feel awe of, be afraid (religious sense)’ : OE wer ‘careful’, warian ‘preserve, pro- tect’, etc. Walde-P. 1.284. Ernout-M. 1089.
Fr. honie, fr. the Gmce., Frank. *hau- nipa fr. vb. *haunjan (> Fr. hon
```


## [2026-09-06T21:17:07.866Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (1224,1225):\n    p=pages[i]\n    for kw in ['sram','farama','Sarama','harm','fsarama']:\n        j=0\n        while True:\n            j=p.find(kw,j)\n            if j<0: break\n            print(i,kw,'::',p[max(0,j-350):j+350].replace('\\n',' '))\n            print('---')\n            j+=1\nEOF",
 "description": "Find Buck discussion of sram/fsarama"
}
```


### [2026-09-06T21:17:09.564Z] TOOL RESULT

```
1224 sram :: ‘be jealous, envy’, AV- ann ‘envious’, OS irri, OE trre ‘angry 1 (16.42). Walde-P. 1.150. a, u~ greizsirdigs gm oTION: TE Digitized by Arya Samaj Foundation Chennai and eGangotri MPERAMENTAL, MORAL, AESTHETIC NOTIONS 1141 16.45 SHAME (sb.) ; Goth. gariudez (aiwiski, Lith. géda y, alba aloxuvn skanda) Lett. kauns Gt: (erp0™ ON kinnrodt ChSl. studi, sramit wpm] 5 Dan. skam SCr. __stid, sram . pudor, ver éoundia Sw.  skam Boh. stud It vergogna OE sceamu Pol. wstyd, wslydliwos¢ a honte ji ME _ shame Russ. styd, stydlivost’ Sp. el NE poke Skt. lajja-, hri-, vrida- um. Tut ire Du. _ schaamte Av. _—_ fiarama- i ane ae OHG coe sake Rite ockel d- MHG _scham(e), scham(e)de W. ane et NHG  scham Br. mez
---
1224 sram :: , OS irri, OE trre ‘angry 1 (16.42). Walde-P. 1.150. a, u~ greizsirdigs gm oTION: TE Digitized by Arya Samaj Foundation Chennai and eGangotri MPERAMENTAL, MORAL, AESTHETIC NOTIONS 1141 16.45 SHAME (sb.) ; Goth. gariudez (aiwiski, Lith. géda y, alba aloxuvn skanda) Lett. kauns Gt: (erp0™ ON kinnrodt ChSl. studi, sramit wpm] 5 Dan. skam SCr. __stid, sram . pudor, ver éoundia Sw.  skam Boh. stud It vergogna OE sceamu Pol. wstyd, wslydliwos¢ a honte ji ME _ shame Russ. styd, stydlivost’ Sp. el NE poke Skt. lajja-, hri-, vrida- um. Tut ire Du. _ schaamte Av. _—_ fiarama- i ane ae OHG coe sake Rite ockel d- MHG _scham(e), scham(e)de W. ane et NHG  scham Br. mez Most of the words listed ae used not
---
1225 sram :: 1.330. Miuhl.-Endz. 2.176 f. 6. ChSI. studi (alcxivn, Lk. 14,9), Boh. stud, and Slavic *stydi in SCr. stid, Pol. wstyd, Russ. styd, and deriv. Pol. wstydliwosé, Russ. stydlivost' , beside ChSI. stydétt ‘be ashamed’, etc., fr. *steu-d- be- side *steu-g- in Grk. ortyos ‘hatred, abomination’, ozvyéw ‘hate, abhor’, Walde-P. 2.620. Briickner 635. ChSl. sramti, SCr. sram (Pol. srom not the usual word; Russ. sorom, and sram fr. ChSl., mostly obj. ‘disgrace’) : ON harmr ‘grief’, etc. (16.32), and prob. also Av. farama-, NPers. arm ‘shame’. Walde-P. 1.463. Meillet, tudes 228. 7. Skt. lajja-, beside 
---
1225 sram :: -Endz. 2.176 f. 6. ChSI. studi (alcxivn, Lk. 14,9), Boh. stud, and Slavic *stydi in SCr. stid, Pol. wstyd, Russ. styd, and deriv. Pol. wstydliwosé, Russ. stydlivost' , beside ChSI. stydétt ‘be ashamed’, etc., fr. *steu-d- be- side *steu-g- in Grk. ortyos ‘hatred, abomination’, ozvyéw ‘hate, abhor’, Walde-P. 2.620. Briickner 635. ChSl. sramti, SCr. sram (Pol. srom not the usual word; Russ. sorom, and sram fr. ChSl., mostly obj. ‘disgrace’) : ON harmr ‘grief’, etc. (16.32), and prob. also Av. farama-, NPers. arm ‘shame’. Walde-P. 1.463. Meillet, tudes 228. 7. Skt. lajja-, beside 
---
1225 sram :: oh. stud, and Slavic *stydi in SCr. stid, Pol. wstyd, Russ. styd, and deriv. Pol. wstydliwosé, Russ. stydlivost' , beside ChSI. stydétt ‘be ashamed’, etc., fr. *steu-d- be- side *steu-g- in Grk. ortyos ‘hatred, abomination’, ozvyéw ‘hate, abhor’, Walde-P. 2.620. Briickner 635. ChSl. sramti, SCr. sram (Pol. srom not the usual word; Russ. sorom, and sram fr. ChSl., mostly obj. ‘disgrace’) : ON harmr ‘grief’, etc. (16.32), and prob. also Av. farama-, NPers. arm ‘shame’. Walde-P. 1.463. Meillet, tudes 228. 7. Skt. lajja-, beside 
---
1225 farama :: , Russ. stydlivost' , beside ChSI. stydétt ‘be ashamed’, etc., fr. *steu-d- be- side *steu-g- in Grk. ortyos ‘hatred, abomination’, ozvyéw ‘hate, abhor’, Walde-P. 2.620. Briickner 635. ChSl. sramti, SCr. sram (Pol. srom not the usual word; Russ. sorom, and sram fr. ChSl., mostly obj. ‘disgrace’) : ON harmr ‘grief’, etc. (16.32), and prob. also Av. farama-, NPers. arm ‘shame’. Walde-P. 1.463. Meillet, tudes 228. 7. Skt. lajja-, beside 
---
1225 harm :: . wstyd, Russ. styd, and deriv. Pol. wstydliwosé, Russ. stydlivost' , beside ChSI. stydétt ‘be ashamed’, etc., fr. *steu-d- be- side *steu-g- in Grk. ortyos ‘hatred, abomination’, ozvyéw ‘hate, abhor’, Walde-P. 2.620. Briickner 635. ChSl. sramti, SCr. sram (Pol. srom not the usual word; Russ. sorom, and sram fr. ChSl., mostly obj. ‘disgrace’) : ON harmr ‘grief’, etc. (16.32), and prob. also Av. farama-, NPers. arm ‘shame’. Walde-P. 1.463. Meillet, tudes 228. 7. Skt. lajja-, beside 
---
```


## [2026-09-06T21:17:18.547Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT fsarema ===\" && grep -n \"fsarema\\|f%arema\\|fšarəma\\|fsar\" BRT.txt | head -10; echo \"=== PHD ===\" && grep -n \"^šarm\\|^sarm\\|^šakar\\|^sakar\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB ===\" && grep -n -i \"sarm\\|sakar\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep Bartholomae, MacKenzie, Nyberg"
}
```


### [2026-09-06T21:17:18.631Z] TOOL RESULT

```
=== BRT fsarema ===
15469:Folge  von  — ';  a)  mit  Abi.:  ysi  ..  ma&ya- nqm  (sd.)  'rB  :i^ar?iBit  *gä%ä  »Bit  srava- yeiti  N-  25;  —  mä  ..  kaine  masyanqm  'rB fsarpmät  x'atB  garrwfin  rai^ayät  V.  1^. strqni  .  .  yni  . .  harne gatvB  äarr/im  hilürüa  .  .  daSoanam  °rB tbaiiaahat  daBvanqm  'rS  (zu  b)  draomShu Yt /j.  57.  b)' mit   Lok.:    Yt  J^.  57
=== PHD ===
PHD_mackenzie.txt:4503:sarmag [slm'k ' 1 N sarma] coldness.
PHD_mackenzie.txt:9003:sarmag
=== NYB ===
6659:Husésarmah: Hušētar- māh
```


## [2026-09-06T21:17:20.022Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN sakar ===\" && grep -n -i \"sakar\\|zucker\" HRN.txt | head -20; echo \"=== HUB ===\" && grep -n -i \"sakar\\|zucker\\|sarm\" HUB.txt | head -20",
 "description": "Grep Horn and Hübschmann for sugar"
}
```


### [2026-09-06T21:17:20.088Z] TOOL RESULT

```
=== HRN sakar ===
3538:np. teberzed (arab. tabarzad) ist Zucker, 'der so hart
8097:LW. vnas, vnasakar,
9851:Geschichte des Zuckers, S. 10, 11), die Übernahme
22510:vnasakar 983.
=== HUB ===
2621:731. Np. sarma ^est forme par analogie siir garma'* Dar-
2623:bildung fand schon im Phi. statt [sarmok nach gar-
2810:'a hawk, falcon' = np. sikara, sakara 'Jagdhabicht'.
6038:schwankt aber 6fter (vgl. sakar, sikOr, sukar 'Kohle' ; saturg,
6566:(idg. pek^U'); sarm *Scham' = zd. fsarema-^); ap. fr ist im
8406:sarm *Scham' ^^ zd. fsarema-, osset. dfsarm; im In-
8544:p. 87. Nach Vokalen: sakav — sakkar *Zucker', das aber
9233:•Wurm' H. 850, sarm ^Scham* H. 780.
```


## [2026-09-06T21:17:27.810Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npages=t.split('\\f')\ndef leafof(lineno):\n    pos=sum(len(l)+1 for l in lines[:lineno-1])\n    return t[:pos].count('\\f')\nfor ln in (6566,8406,8544):\n    lf=leafof(ln)\n    print('line',ln,'leaf',lf,'printed',lf-10)\n    print('\\n'.join(lines[ln-4:ln+6]))\n    print('=====')\nEOF",
 "description": "Print Hübschmann contexts"
}
```


## [2026-09-06T21:17:28.231Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9840,9870p' HRN.txt",
 "description": "Print Horn sugar context"
}
```


### [2026-09-06T21:17:29.622Z] TOOL RESULT

```
line 6566 leaf 196 printed 186
heit* (zd. trp *8tehlen*), biShOfa *Biathe* (gr. axvtpoq) u. s. w.
^) Zd. fs auch ^=- pis in nc^su aus *napfsu, loc. pi. von napat-.— 186 --
175 von fsU' ^) (idg. pk^u-), schwache Form zu pasu- 'Vieh'
(idg. pek^U'); sarm *Scham' = zd. fsarema-^); ap. fr ist im
An- und Inlaut stets = np. fr {far u. s. w.), nur im Aus-
laut = rf {barf *Schnee' = zd. vafra-), siehe Kap. 32.
Ap. / ist also geschwunden im Anlaut vor s, Viel-
leicht auch inlautend in turvs *sauer (aus *trus -= Hrusf
= Hrufs = >/sa-? vgl. H. 385 und oben p. 48).
§ 82. Persisches / wird von den Armeniern, deren
=====
line 8406 leaf 245 printed 235
konig = syr. aptaxsd, gr. Tundirjg, lat. vitaxa,
§ 127. Idg. ps - ap. fff = np. s im Anlaut, fs im
Inlaut :
sarm *Scham' ^^ zd. fsarema-, osset. dfsarm; im In-
laut: dirafs 'Banner -= zd. drafsa-, arm. dram. Jungeren
Ursprungs ist fs (^= w-S) in afscindan H. 102, unsicheren
in banafsa 'Veilchen' H. 231, s. oben p. 31. Dunkel ist
das Verhaltniss von zd. fstdna- zu np. pistan 'Brust', siehe
oben p. 41.
§ 128. Idg. pk^ —^ zd. fs -^- arm. np. s im Anlaut:
=====
line 8544 leaf 249 printed 239
'Huhn , vgl. ossot. KarU fiir Uarg und die andern iran.
Formen mit k statt ^ bei Horn 848. Daneben steht np.
kurg, kas. karg und andere iran. Formen mit g, s. oben
p. 87. Nach Vokalen: sakav — sakkar *Zucker', das aber
indisches LW. ist; cakdd *ScheiteI, Gipfel' -- arm. cakat
'Stirn, Front'; cakus 'Hammer, H. 443, oben p. 52; sdk
'Aehre, Granne', skr. fjuka- *Granne, Stachel' H. 755; niku-
hidan 'tadeln, schmahen (aber niguhand A. M. 8, 5), siehe
oben p. 102.
Wahrend also ap. k im Phi. nach Vokalen und r blieb,
=====
```


### [2026-09-06T21:17:29.653Z] TOOL RESULT

```
sabellisch (Bersu, Die Gutturalen und ihre Ver-
bindung mit V im Lateinischen S. 139, vergl. auch
Stolz, Latein. Grammatik- S 47 Anm. 1), pahimhes,
popina, oskisch (Stolz, 55 46 Anm. 3), rüfns^ stßlus
etc. (Stolz, J5 54:^ '^5)» die mit / beginnenden Worte
lingiia, lacruma, levir etc., sabinisch (II. Seymour
Conway, Indog. Forsch. II, 157 folg.) u. a. m. ~
so ist vielleicht auch apis oskisch es Lehnwort. In
Bruttium, Lucania, Messana wurde oskiscli ge-
sprochen, Sicilien war das Honigland, der berühmte
Sitz der Bienenzucht (vergl. E. 0. von Lippmann,
Geschichte des Zuckers, S. 10, 11), die Übernahme
des oskischen Wortes in das Lateinische wäre also
durchaus nicht befremdlich. Allerdings bleibt -mp
sonst im Oskischen erhalten (vergl. R. von Planta,
Vocalismus der oskisch-umbrischen Dialekte, S. 307),
aber auch bei der Zusammenstellung mit spnl^^ ergiebt
*) Ai. admasäd' (G e 1 d n e r , Vedisohe Studien II, 1 79 folg ) passt
mehr auf die Fliege oder Wespe (wenn das ädnui- Obst ist) als auf
dip Biene.- - 2r>() —
sich für das Lateinische dieselbe Schwierigkeit, das
Schwinden des m zu erklären; Bu gge versucht dieses
letztere BB. XIV, 70. Ahd. imbi 'Bienenschwarm',
mhd. imhe *Biene* sowie gall. amella *Bienensug
(Wh. Stokes, BB. IX, 194) haben, wenn meine Ver-
mutung richtig ist, nichts mit np. eng, lat. (osk.) apis
zu schaffen; doch ist es bisher auch noch nicht
geglückt, dieselben in einer irgendwie befriedigenden
Weise mit apis zu vereinigen.
Zu np. eng etc. seien noch täl. äng und kauk.-
bergj. heng 'HummeV hinzugefügt.
```


## [2026-09-06T21:17:38.834Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Scham\" BRT.txt | head -20",
 "description": "Grep Bartholomae for Scham"
}
```


### [2026-09-06T21:17:38.880Z] TOOL RESULT

```
7550:Aus  ar.  *äilkaii-,  lum  V.  äs-;  Bthl.  "iF,  j. 215.  —  Pü.  (nach  DST.):  ka  e  iiii.tkt)  rau:^/ pa  bau  i  haxi  i  ian  i  "wenn  der  Igel  geht in  den  Grund  der  Schamteilfc  einer  Frau";  s. dazu  DsT.  ZA.  /.  347,  3.  195.  Die  PLiF.rl.  ist mit  ebenso  an  verständlich  wie  diese  selbst, Ton  der  nur  so  viel  deutlich  ist,  dass  sie  die Strophe  aufUniucht  vonWeibern  bezieht. — 0  SP.  hat:  amtainik.  V^l.  West  zu  Dk. g.  17.  S,  der  auch  anf  Av,  yo,  3  vervreisl.
18400:•  j.  ßarana-  m.  'Scham(gefÜhl)  vor  — ' (Gen.):  maiyättqm  pars  'ni3t"a.\is  Scham vor  den  Menschen"  V.  75, 9,  10.
20036:—  D  6aga^  *vatarkt^  .  .  Aya^  'yam  ad^ hye^  siyätim  ada/'  'yakyä  D.  6.  i,  7. 1,  X. /.  I,  G.\,  Ao-i,  i'>;ll  —  kB . .  ä%rs  taßtm darayal  fanaot  haia  'yeke  V.  20. 1 ;  —  avi imqm  lanüm  yqm  'yänqm  V,  20, 3,  5;  — ya^  Als  antar»  vots  fravaiti  barV.ba^ (sd.)  'yänqm  Ytij.46;  —  'yänam  parS fsanmäi  "aus   Scham   vor  den  Leuten"
```


## [2026-09-06T21:17:45.090Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:18399])\nlf=t[:pos].count('\\f')\nprint('leaf',lf)\npages=t.split('\\f')\np=pages[lf]\nprint(p[:600])\nprint('...')\nj=p.find('Scham(gef')\nprint(p[max(0,j-900):j+400])\nEOF",
 "description": "Find Bartholomae column for fsarema"
}
```


### [2026-09-06T21:17:46.657Z] TOOL RESULT

```
leaf 575
il  »nzajySi  frajyaitis (sd.)  nsit  fsuyenlt  dngvasB  pairl  Y. 2p.  5.  a)  mit  västrya-  (sd.):  ai zl'kwa fsuyaniaila  vaslryäicä  %wSrPstä  (sd.) tatasä  Y.  29.  6;  —  at  kl  aya  ß-avantä (sd.)  västrlm  afiyai  /luyanlimY. 31.  10; Yt  10. 60.  a)  als  Bezeichnung  für  den dritten  Stand  {'pi/tra-),  'der  viehzUchtende Bauer",  geg.  a^ravan-  (Stverz.),  ra%alitar- (und  Aatay-):  ä^rava  rdSialsta  vastryS fsuyqs  hüitis  Y-ig.  17  usw.;  —  väsfrtm fluyaniim  Vr.^.  2  usw.;  —  västryai fiu-
nie  YLij.  88  usw.;  —  vastryeke  fiw yanis  V.  13.  44  usw.;  —  fiuya  (VS
...
trya  V.  lÄ  21;  —  vostryasca  fsuyantö Y.  7^.  3  usw.
Et.?  —  PÜ.  (lU  F.)  i/wniÄI),  (EU  V.  4»^  -.ßäniniin, (lu  y.  2pä,  31):  ßöntmiär.  (ra  a):  vasityöli); s.  noch  No.  3.  Sü.  {lu  Y.  48):  sphUayitum, (in  Y.  39»):  vfddhiiarlä.  — 1>  Hds.  piyS,  aber unter  den  Wärtern  für  anlauL  /.  Wohl  von Y.  ^.  5  her  genomaen.  —  »)  Da«  Wort  vmrde volksetymologiEch  mit  V^ot^  in  Beziehung  ge- bracht Gani  unwahrscheinlich  iit,  was  Gdn. KZ.  jo.  51S  zur  Bedeutung  von  /cKVfi  be- merkL  —  J)  Pii.:  in  i  j*/i  husvün  ßsöninind
ob,Google
"nS
1030
Hai  an  i  a/ünermii.  —  4)  Lies/iwiSuin?  S. za  ßaonay-  anA /sümant-.  —  S)  So  Päs.  Eine Veralüramelung  von  -üäitryö fiuy^;  V.  /Ä  ai steht  n  a  ddt  r  dn  p  dah.
•  j.,  g.  "ßav-  m.:  s.  unter  pasav-  (mit No.  i).        VgL  auch  ^/ys.
KompA.,  E.;  Ableit.
•  j.  ßarana-  m.  'Scham(gefÜhl)  vor  — ' (Gen.):  maiyättqm  pars  'ni3t"a.\is  Scham vor  den  Menschen"  V.  75, 9,  10.
Et.  ?  —  mp.  {Pü.\  np.  Sana.
•  j.  ßah-"  n.  Tessel*:  ayaohainail fsibis atäibis  paiti  ava. pasilj  (Sp-S-jg  o.)  V.4.51.
Zum  V./3J-.  —  »i.  vgl.  faJ-  f.  [fia^im),  fäSa- ro.  —  Pü.:/Ja  (Lesung?).—  1)  Wohl  durch Dekomposition  entslanden.
•  g.  ßänghya-  Adj.  'fördernd,
```


## [2026-09-06T21:17:56.838Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^SUGAR\\|SUGAR,\" HJB.txt | head -5; python3 - <<'EOF'\nt=open('HJB.txt',encoding='utf-8',errors='replace').read()\ni=t.find('\\nSUGAR')\nprint(t[i:i+1800])\npages=t.split('\\f')\nfor k,p in enumerate(pages):\n    if '\\nSUGAR' in p: print('leaf',k,'printed ~',k-45)\nEOF",
 "description": "Print Hobson-Jobson SUGAR"
}
```


### [2026-09-06T21:17:58.522Z] TOOL RESULT

```
20785:SUGAR
20803:SUGAR,
20805:SUGAR.
20822:SUGAR.

SUGAR
18M.— '*  list  of  Chinese  articles  brought to  India.  .  .  .  Snklat,  a  kind  of  camlet  made of  camel's  hair." — Cunnijigham's  Ladak^  2ASL
1862. — "In   this   season  travellers   wear
Sarments  of  sheep-skin  with  sleeves,  the eeoy  side  inwards,  and  the  exterior  covered with  Sooklat,  or  blanket."— PuA;a&  Trode Report^  57.
„    '  *  Bboadoloth  (Europe),  < '  Snklat, '
*  Mahoot')."— 7&ui.  App,  p.  oozxx.
SUDDEN  DEATH.  Anglo-Indian fllang  for  a  fowl  served  as  a  spatchcock, the  standing  dish  at  a  dawk-bungalow in  former  oays.  The  bird  was  caught in  the  yard,  as  the  traveller  entered, and  was  on  the  table  by  the  time  he had  bathed  and  dressed.
[c.  1848.— "  * 8iidd«n  death'  means  a younff  chicken  about  a  month  old,  caught, killed,  and  grilled  at  the  shortest  notice." — BenuxutU,  Voyage  to  China,  i.  198.]
SUDDEB,  adj.,  but  used  as  s. Literally  *  chief,'  being  Ar.  itadr.  This term  had  a  technical  application  under Mahommedan  rule  to  a  chief  Judge, as  in  the  example  quoted  below.  The use  of  the  word  seems  to  be  almost confined  to  the  Bengal  Presidency. Its  principal  applications  are  the following :
a.  Sndder  Board.     This    is    the
*  Board  of  Revenue,'  of  which  there is  one  at  Calcutta,  and  one  in  the N.W.  Provinces  at  Allahabad.  There is  a  Board  of  Revenue  at  Madras,  but not  called  '  Sndder  Board '  there.
b.  Sndder  Oonrt,  i,e.  *Sudder  Ad- awlut  (sadr  ^addlat).  This  was  till 1862,  in  Calcutta  and  in  the  N.W. P.,  the chief  court  of  appeal  from  the  MoflLBSil or  District  Courts,  the  Judees  being members  of  the  Bengal  Civil  Service. In  the  year  named  the  Calcutta  Sud
leaf 906 printed ~ 861
leaf 907 printed ~ 862
leaf 908 printed ~ 863
```


## [2026-09-06T21:17:59.512Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%A7%DA%A9%D8%A7%D8%B1%D8%B2/",
 "prompt": "Show any dictionary entries (فرهنگ معین, دهخدا, عمید) for ساکارز — definition and stated origin language (French? saccharose). Quote in Persian."
}
```


### [2026-09-06T21:18:05.519Z] TOOL RESULT

```
# ساکارز - Dictionary Entries

## فرهنگ معین
**Origin:** French (فر.) / English (اِ.)

**Definition:** "ماده ای که از نیشکر تهیه شود و از نظر شیمایی شبیه چغندر است، قند نیشکر"

(A substance derived from sugarcane that is chemically similar to beets; sugarcane sugar)

## فرهنگ عمید
**Definition:** "ماده ای جامد، سفید، بی بو، بامزۀ شیرین که برای شیرین کردن مواد غذایی به کار می رود"

(A solid, white, odorless substance with a sweet taste used to sweeten food)

---

**Note:** The فرهنگ معین entry explicitly indicates French origin for this term, which corresponds to the French word "saccharose."
```


## [2026-09-06T21:18:16.699Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20800,20830p' HJB.txt",
 "description": "Print Hobson-Jobson SUGAR entry"
}
```


### [2026-09-06T21:18:16.741Z] TOOL RESULT

```
c.  1S40.— "The  Sadr-J^Od*  (< Chief  of the  Word  ')  i.e.  the  'KM£^-al-Kvdai  (<  Judge of  Judges')  (CAZEE)'.  .  .  poaseaaes  ten townships,  prodnciiig  a  revenae  of  about 60,000  tankaa.  He  is  also  called  Eadr-al- Isldjn."^Slukahtidd^  DimitkJbi,  in'^'blcteC ExU.  xiii.  185.
SUFEENA,  8.  Hind,  mfina.  This is  the  native  corr.  of  tubpoenei.  It  is shaped,  but  not  much  aistorted,  by the  existence  in  Hind,  of  the  Ar.  word safina  for  'a  blank-book,  a  note-book.'
SUGAB,  8.  This  familiar  wotd  ia of  Skt.  origin.  Sarkara  originally signifies  *grit  or  cravel,'  thence  crys- t^ulised  sugar,  ana  through  a  Prakrit form  takkara  gave  the  Pers.  sfcolJvr, the  Greek  vdicxflp  and  c^ixxapo^y  and  the late  Latin  tacdiarum.  The  Ar.  is sukkar,  or  with  the  article  cM-«icJbbcir, and  it  is  probable  that  our  modem forms.  It.  zucehero  and  suockeroj  Fr. iucre^  Germ.  Zuckery  £ng.  mgar,  came as  well  as  the  Sp.  oetioir,  and  Port. cuiucar,  from  the  Arabic  direct,  and not  through  Latin  or  Greek.  The Russian  is  aakhar;  Polish  zmkitr; Hung.  zuJnir,  In  fact  the  ancient knowledge  of  the  product  was  sli^t and  vague,  and  it  was  by  the  Arabs that  the  cultivation  of  the  su^tf-cane was  introduced  into  £ffil>t,  Sicily,  and Andidusia.  It  is  posaLDle  indeed  and not  improbable,  that  palm-sngar  (aee JAGOEBY)  is  a  much  older  product than  that  of  the  cane.  [This  ia  dis- puted by  Watt  {Eeon,  DtcL  vL  pi,  i p.  31 X  who  is  inclined  to  fix  the  home of  the  cane  in  £.  India.]  The  original habitat  of  the  cane  is  not  known  ; there  ia  only  a  slight  and  doubtful statement  of  Loureiro^  who,  in  speak- ing of  Cochin-China,  uses  the  words
SUGAR,
863
SUGAR.
•••habitat  et  colitur,"  which  may  imply its  existence  in  a  wild  state,  as  well  as Ainder  cultivation,  in  that  country. De  Candolle  assigns  its  earliest  pro- •dnction  to  the  country  extending  from Cochin-Ohina  to  Bengal.
Thou£^h,  as  we  have  said,  the  know- ledge which  the  ancients  had  of  sugar was  very  dim,  we  are  disposed  greatly to  question  the  thesis,  which  has  been so  confidently  maintained  bv  Salmasius and  later  writers,  tha^  the  ori^al .aoAxharon  of  Oreek  and  Roman  writers was  not  sugar  but  the  siliceous  con- •cretion  sometimes  deposited  in  bam- boos, and  used  in  medieval  medicine under  the  name  tabasheer  (q.v.) (where  see  a  quotation  from  Ro^le, taking  the  same  view).  It  is  just possible  that  Pliny  in  the  passage -quoted  below  may  have  jumbled  up two  different  things,  but  we  see  no sufficient  evidence  even  of  this.  In White's  Latin  Diet,  we  jead  that  by the  word  ioceharon  is  meant  (not  sugar but)  "a  sweet  juice  distilling  from  the joints  of  the  bamboo."  This  is  non- sense. There  is  no  such  sweet  iuice distilled  from  the  joints  of  the  bam- boo ;  nor  is  the  substance  tabashlr  at sll  sweet.  On  the  contrary  it  is slightly  bitter  and  physicky  in  taste, with  no  approach  to  sweetness.  It  is a  hydrate  of  siHca.  It  could  never have  been  called  "honey"  (see  Dios- corides  and  Pliny  below) ;  and  the name  of  bamnboo-sugar  appears  to  have been  given  it  by  the  Arabs  merely because  of  some  resemblance  of  its concretions  to  lumps  of  sugar.  [The .same  view  is  taken  m  the  EncycL  Brit. 9th  ed.  xxii.  625,  quoting  Not.  et  Extr.^ XXV.  267.]  All  the  erroneous  notices of  <r6.KxaLpo¥  seem  to  be  easily  accounted for  by  lack  of  knowledge ;  and  they are  exactly  paralleled  by  the  loose  and inaccurate  stories  about  the  origin  of camphor,  of  lac,  and  what-not,  that may  be  found  within  the  boards  of this  book.
In  the  absence  or  scarcity  of  sugar, honey  was  the  type  of  sweetness,  and hence  the  name  of  honey  applied  to .sug^r  in  several  of  these  early  extracts. This  phraseology  continued  down  to the  Middle  Ages,  at  least  in  its  appli- cation to  uncrystallised  products  of  the .sugar-cane,  and  analogous  substances. In  the  quotation  from  Pegolotti  we -apprehend  that  his  three  kinds  of honey  indicate  honey,  treacle,  and  a
syrup  or  treacle  made  from  the  sweet pods  of  the  carob-tree.
Su£»r  does  not  seem  to  have  been in  eany  Chinese  use.  The  old  Chinese books  often  mention  ski-mi  or  'stone- honey'  as  a  product  of  India  and Persia.  In  tne  reign  of  Taitsung (627-650)  a  man  was  sent  to  Qan^tic India  to  learn  the  art  of  sugar-makmg ; and  Marco  Polo  below  mentions  the introduction  from  Egypt  of  the  further art  of  refining  it.  In  India  now,  Gklnl (Cheeny)  (Cninese)  is  applied  to  the whiter  kmos  of  common  sugar  ;  Mvprl (Miaree)  or  Egyptian,  to  sugar-candy  ; loaf-sugar  is  called  hand,
C.  A.D.  60.— ^*  QoAque   ferena   rapidom    diviso   gurgito
fontem Vastb    Indiu   aquis   miztum  non  sentit
Hydaspen : Quique  bibunt  teneiA  dulcis  ab  amndiDO
succoe.  ..."  Lucanj  iii.  235.
„  **Aiunt  iDToniri  apud  Indos  mel in  anmdiniim  foliis,  quod  aut  nos  illius cceli,  aut  ipsius  arundinis  humor  duloiB  et pingoiB  giguat." — Seiuca^  EpiH,  Ixzxiv.    ,
c.  A.D.  65.—"  It  is  called  frdKxapop,  and is  a  kind  of  honey  which  solidifies  in  India, and  in  Arabia  Felix  ;  and  is  found  upon canes,  in  its  substance  resembling  salt, and  crunched  by  the  teeth  as  salt  is.  Mixed with  water  and  drunk,  it  is  good  for  the belly  and  stomach,  and  for  affections  of  the bladder  and  kidneys."— Z>toieoru^,  McU, Med.  ii.  c.  104.
c.  A.D.  70.— "Sacohanm  et  Arabia  fert, sed  laudatius  India.  Est  autem  mel  in harundinibus  coUectum,  cummium  mode candidum,  dentibus  fragile,  ampUssimum nuois  abellanae  magnitudine,  ad  medicinae tantum  usum." — PUn.  Bist,  Nat.  rii.  8.
c.  170.—"  But  aU  these  articles  are  hotter than  is  desirable,  and  so  they  aggrayate feyers,  much  as  wine  would.  But  oxymeli alone  does  not  a^rayate  feyer,  whilst  it  is an  actiye  purgatiye.  .  .  .  Not  undeservedly, I  think,  that  saochanun  may  also  be counted  among  things  of  this  <|UAlity.  ..." — Oalen,  Metkodua  Medcndif  via.
c.  636. — "  In  Indieis  stagnis  nasd  arun- dines     calamique     dicuntur,     ex     quorum radicibus   exprossum   suayissimum   suocum bibunt.    Vnae  et  Varro  ait : Indica  non  magno  in  arbore  crescit  arundo ; Illius  et  lentis  premitur  radicibus  humor, Dulcia  qui  nequeant  succo  ooncedere  mella." Itidori  HispaUntit  Onginum^ lib.  xyii.  cap.  yii.
c.  1220. — **  Sunt  insuper  in  Terra  (Sancta) eanameliae  de  quibus  nioohara  ex  compres- sione  eliquatur."  —  Jacobt  Vitriacif  MtH. Jkerosolym,  cap.  Izzxy.
12d8.— "Bangala  est  une  proyence  yers midi.  .  .  .  n  font  grant  merohandie,  car  il out  espi  e  galanga  e  gingiber  e  saocare  et
SUGAR.
864
SULTAN.
de  maintes  autres  ohieres  eepices.  "—Jtforco Poh,  Geog.  Text,  ch.  cxxvi.
1298.—"  Je  voz  di  que  en  ceste  provences  " (Quinflai  or  Chekiang)  "naist  et  se  fait pluB  lacar  que  ne  fait  en  tout  le  autre monde,  et  oe  est  encore  grandissime  rente." — Ibid.  ch.  cliii.
1298.— "And  before  this  city"  (a  place near  Fu-cbau)  "came  under  the  Great  Can Uiese  people  knew  not  how  to  make  fine 811^^  {zuccharo) ;  they  only  used  to  boil  and skim  the  juice,  which,  when  cold,  left  a black  paste.  But  after  they  came  under the  Great  Can  some  men  of  Babylonia" {i,e.  of  Cairo)  "who  happened  to  be  at the  Court  proceeded  to  this  city  and  taught the  people  to  refine  8ii£[ar  with  the  ashes of  certain  trees." — Idem,  in  RamutiOf  ii.  49.
c.  1343.  —  "In  Cyprus  the  following articles  are  sold  by  the  hundred-weight {a:intara  di  pe$o)  and  at  a  price  in  besants : Bound  pepper,  sugar  in  powder  {polvere  di mcchero)  .  .  .  sugars  in  loaves  (mooheri  in pafii)y  bees'  honey,  sugar-cane  honey,  and oarob-honey  {meh  d^ape,  meU  di  cannameliy mele  di  carrttbe).  .  .  ." — PegolotUf  ^.
„  "  Loaf  sugars  are  of  several  sorts, viz.  mcchero  mwMerOf  caffettinOf  and  hoM- hiUonta;  and  muaciaUo^  and  domnuucktno ; and  the  mucchera  is  the  best  sugar  there  is ; for  it  is  more  thoroughly  boiled,  and  its  paste is  whiter,  and  more  solid,  than  any  other sugar ;  it  is  in  the  form  of  the  bamoillonia sugar  like  this  A ;  and  of  this  mucckara kind  but  little  comes  to  the  west,  because nearly  the  whole  is  kept  for  the  mouth  and for  the  use  of  the  Soldan  himself.
"Zucohero  caffettino  is  the  next  best after  the  muccara  .  .  .
```


## [2026-09-06T21:18:30.320Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%B0%E0%A5%8D%E0%A4%95%E0%A4%B0%E0%A4%BE",
 "prompt": "Sanskrit शर्करा (śarkarā): give its meanings, earliest attestation, etymology (Proto-Indo-Aryan / PIE, cognate Greek κρόκη), and the list of descendants (Pali sakkharā, Prakrit, Persian شکر, Greek σάκχαρον). Quote exactly."
}
```


## [2026-09-06T21:18:32.016Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/saccharin",
 "prompt": "Quote the etymology of \"saccharin\" and \"saccharine\" and \"sucrose\" and \"saccharose\" if present: Modern Latin saccharum, Latin saccharon, Greek sakkharon, Pali sakkhara, Sanskrit sharkara; also who coined saccharin and when."
}
```


### [2026-09-06T21:18:37.281Z] TOOL RESULT

```
# Sanskrit शर्करा (śarkarā)

## Meanings
According to the Wiktionary entry, the Sanskrit noun has seven primary meanings:

1. Gravel, grit, pebbles, shingle, or gravelly mould/soil (mostly plural)
2. Gravel as a disease
3. Hardening of the flesh
4. Hardening of ear-wax
5. Ground or candied sugar
6. Fragment or piece of broken earthenware/potsherd
7. Cotton sugar or sugarmaple

## Etymology
The word derives from Proto-Indo-Aryan *śárkaraH, which comes from Proto-Indo-Iranian *ćárkaraH, ultimately from Proto-Indo-European *ḱorkeh₂ meaning "gravel, boulder."

The entry notes a cognate with Ancient Greek κρόκη (krókē, "pebbles"), "whence English crocodile."

## Descendants
The documented descendants include:
- **Pali**: sakkharā
- **Prakrit**: 𑀲𑀓𑁆𑀓𑀭𑀸 (sakkarā)
- **Gandhari**: 𐨭𐨐𐨪 (śakara)

The entry also lists borrowings into various modern languages but does not specifically mention Persian شکر or Greek σάκχαρον in the descendants section shown.
```


### [2026-09-06T21:18:37.318Z] TOOL RESULT

```
# Etymology of Saccharin and Related Terms

**Saccharin:**
"white crystalline compound, odorless but intensely sweet, used as a sugar substitute, 1885, from German, coined 1879 by Russian-born chemist Constantin Fahlberg"

**Saccharine:**
"of or like sugar, having the qualities of sugar," from Medieval Latin *saccharum* "sugar," from Latin *saccharon* "sugar," from Greek *sakkharon*, from Pali *sakkhara*, from Sanskrit *sarkara* "gravel, grit"

**Sucrose and Saccharose:**
These terms are not present in the provided content. Only the etymological chain for saccharin/saccharine is documented, tracing back through Greek and Sanskrit origins related to the concept of sweetness and sugar.

The page establishes that Constantin Fahlberg, a Russian-born chemist, discovered and named saccharin in 1879, with the term entering English usage by 1885.
```


## [2026-09-06T21:18:44.574Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/شکر' \\\n 'https://en.wiktionary.org/wiki/شرم' \\\n 'https://en.wiktionary.org/wiki/κροκόδειλος' \\\n 'https://en.wiktionary.org/wiki/शर्करा' \\\n 'https://www.etymonline.com/word/sugar' \\\n 'https://www.etymonline.com/word/crocodile' \\\n 'https://www.etymonline.com/word/saccharin' \\\n 'https://abadis.ir/fatofa/سوخاری/' \\\n 'https://abadis.ir/fatofa/ساکارز/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 273, roots Korkâ/Kormo: sugar chain and šarm/harm verification' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-06T21:18:51.885Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/abeab1dee8661631.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/27b6a1f711a3d673.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/221fafcb5a428f5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/472565208573de1e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/17322ea716683b33.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1c067b1e3099ed74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/194753d938ca67f5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/380725da83d10e11.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7451384566108d63.txt
```


## [2026-09-06T21:18:58.028Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg273.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/273.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3 && sed -n '1,60p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy page PNG and inspect verify_check"
}
```


### [2026-09-06T21:18:58.104Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
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


## [2026-09-06T21:19:00.511Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '60,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T21:19:00.557Z] TOOL RESULT

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


## [2026-09-06T21:19:32.494Z] AGENT

Now writing the verification file.


## [2026-09-06T21:26:53.089Z] TOOL CALL #62: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-273.json <<'JSONEOF'\n{\n  \"pdf_page\": 273,\n  \"book_page\": 243,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Korkâ\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱorkeh₂ (Pokorny ḱorkā / kroká?) 'gravel, pebble, boulder'\",\n      \"note\": \"Pokorny IEW p.615 has exactly 'Root/lemma: ḱorkā (ḱrokā?), -ā, Meaning: gravel, boulder' with Skt. śarkarā and Gk. κροκή, κροκάλη; Walde-Pokorny I 463 the same. Wiktionary reconstructs *ḱorkeh₂ 'gravel, boulder'. Nourai's root name, language label (Indo-European) and gloss 'gravel' are all correct; the citation POK:615 is exact. The only real weakness of the chart is at its two ends: the Persian chemical/bakery terms hung under French (nodes 7 and 13) and the 'pebble-worm' explanation of κροκόδειλος (node 14), which Beekes rejects.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱorkeh₂ «سنگ‌ریزه، شن» که پوکورنی در صفحهٔ ۶۱۵ فرهنگ ریشه‌شناختی خود با همین معنا و با شاهدهای سنسکریت śarkarā و یونانی κροκή/κροκάλη آورده و والده‑پوکورنی (جلد ۱ ص ۴۶۳) نیز همان را دارد. نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است و ارجاع POK:615 دقیق است. تنها حلقه‌های سست این نمودار در دو سرِ آن است: واژه‌های نوساختهٔ فارسی «ساکارز» و «ساخارین/سوخاری» که به فرانسوی sucre بسته شده‌اند، و تبیین «کرم سنگ‌ریزه» برای κροκόδειλος که بیکس آن را رد می‌کند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%B0%E0%A5%8D%E0%A4%95%E0%A4%B0%E0%A4%BE\",\n        \"https://www.etymonline.com/word/sugar\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:615\", \"status\": \"supports\", \"note\": \"Pokorny p.615 (POK_full.txt line ~51690): 'Root / lemma: ḱorkā (ḱrokā?), -ā | Meaning: gravel, boulder | Material: Old Indic śarkarā (śarkaraḥ) \\\"powder, gravel, stone, powder sugar\\\"; gr. κροκή, κροκάλη \\\"pebble\\\" ... References: WP. I 463. Page(s): 615.' Exactly Nourai's root box.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.463 (WLD_Bd1_pages.txt leaf 472)\", \"stance\": \"supports\", \"note\": \"'korka (kroka?)-ela \\\"Kies, Kiesel\\\". Ai. śárkarā (carkara-ḥ) \\\"Gries, Kies, Geröll, Sandzucker\\\"; gr. κροκή, κροκάλη \\\"Kieselstein\\\" ... vielleicht aber hat ein *κορκάλα : śarkarā erst nach letzterer Gruppe Umstellung zu κροκάλη erfahren.'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck §5.85 SUGAR (SYN.txt leaf 430)\", \"stance\": \"supports\", \"note\": \"'Skt. śarkarā- \\\"gravel, grit\\\" (AV+) later \\\"sugar\\\" : Grk. κρόκη, κροκάλη \\\"pebble\\\". Walde-P. 1.463. Hence, through a later Prakrit form like Pali sakkharā-, the following: ...'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, appendix\", \"stance\": \"silent\", \"note\": \"grep of AHD_watkins1985.txt for 'korka'/'krok' returns only krek-1 'to weave, beat' and gerbh-; Watkins has no *ḱorkā root (English has no native reflex), so the appendix is silent rather than contradicting.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"sarkarah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Skt. śárkarā f. (nom. sg.; the masc. by-form śarkaraḥ is what Nourai transliterates 'sarkarah') is attested from the Atharvaveda on in the concrete sense 'grit, gravel, pebbles, gravelly soil', and only later — with the spread of cane cultivation in the Ganges basin — in the transferred sense 'ground or candied sugar', i.e. sugar seen as sweet 'grit'. Phonologically it is the regular Indo-Aryan outcome of the root: PIE *ḱ > Proto-Indo-Iranian *ć > Old Indic ś, so *ḱorkeh₂ > PIIr. *ćárkaraH > Skt. śárkarā, with the o-grade of the root reflected as Indic a (Brugmann's law not applying in the closed syllable). Klein and Buck both give the Greek κρόκη 'pebble' as the exact cognate, which is Nourai's other branch (node 14).\",\n          \"derivation_fa\": \"سنسکریت śárkarā (گونهٔ مذکر śarkaraḥ که نورایی به‌صورت sarkarah آورده) از اتهرَوَوِدا به بعد به معنای «شن، سنگ‌ریزه، خاک سنگ‌ریزه‌دار» گواهی شده و تنها در دورهٔ متأخرتر، با گسترش کشت نیشکر در دشت گنگ، معنای «شکر، قند سابیده» یافته است؛ یعنی شکر را همچون «شنِ شیرین» دیده‌اند. از نظر آوایی این صورت بازتاب قانون‌مند ریشه است: kʲ هندواروپایی در هندوایرانی آغازین به *ć و در هندی باستان به ش (ś) بدل شده است. پوکورنی، والده‑پوکورنی، باک و کلاین همگی همین را می‌گویند؛ پس ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%B0%E0%A5%8D%E0%A4%95%E0%A4%B0%E0%A4%BE\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:615\", \"status\": \"supports\", \"note\": \"Pokorny p.615 s.v. ḱorkā: 'Old Indic śarkarā (śarkaraḥ) \\\"powder, gravel, stone, powder sugar\\\"' — the same word and the same two senses Nourai gives ('gravel, sugar').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.463\", \"stance\": \"supports\", \"note\": \"'Ai. śárkarā (carkara-ḥ) \\\"Gries, Kies, Geröll, Sandzucker\\\"' — 'Sandzucker' is precisely the 'gravel > sugar' shift.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §5.85 SUGAR\", \"stance\": \"supports\", \"note\": \"'Skt. śarkarā- \\\"gravel, grit\\\" (AV +) later \\\"sugar\\\"' — gives the Atharvaveda as the earliest attestation.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.863 s.v. SUGAR\", \"stance\": \"supports\", \"note\": \"'Sarkara originally signifies \\\"grit or gravel,\\\" thence crystallised sugar, and through a Prakrit form sakkara gave the Pers. shakkar, the Greek σάκχαρ and σάκχαρον, and the late Latin saccharum.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pali\",\n          \"words\": \"sakkara\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Middle Indic step is real and is the link every authority uses. Old Indic śarkarā gives Pali sakkharā: initial ś- > s- (Middle Indic loses the three-way sibilant contrast), and the cluster -rk- is assimilated to a geminate -kkh- with aspiration (the ordinary MIA treatment of a stop after r, cf. Skt. karkaṭa > Pali kakkaṭa). Nourai's spelling 'sakkara' without the aspirate is the Prakrit/Gandhari shape (Pkt. sakkarā, Gandhari śakara), which is in fact the form actually borrowed westwards; Wiktionary routes the Persian word through Gandhari śakara rather than Pali. The gloss 'sugar' is right: by the Middle Indic period the word means the commodity, not the gravel.\",\n          \"derivation_fa\": \"حلقهٔ هندی میانه واقعی است و همهٔ مرجع‌ها آن را می‌آورند: śarkarā هندی باستان در پالی به sakkharā بدل می‌شود؛ ش آغازین به س، و خوشهٔ ‑rk‑ بر اثر همگونی به ‑kkh‑ مشدد و دمیده تبدیل می‌گردد (همان تحولی که در karkaṭa > kakkaṭa دیده می‌شود). صورتی که نورایی نوشته، یعنی sakkara بدون دمیدگی، در حقیقت گونهٔ پراکریت/گاندهاری (sakkarā، śakara) است و همان است که به سوی غرب وام داده شده؛ ویکی‌واژه نیز واژهٔ فارسی را از گاندهاری śakara می‌گیرد. معنای «شکر» در این مرحله درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%B0%E0%A5%8D%E0%A4%95%E0%A4%B0%E0%A4%BE\", \"https://www.etymonline.com/word/saccharin\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; checked independently against Klein, Buck, Lokotsch, Hobson-Jobson and Wiktionary (all listed under consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1370 s.v. 'sacchar-' (KLN_1966.txt leaf 728, page marker '13/U-' = 1370)\", \"stance\": \"supports\", \"note\": \"'Fr. L. saccharon, fr. Gk. σάκχαρον \\\"sugar\\\", fr. Pali sakkharā, fr. OI. śarkarā, \\\"gravel, grit, sugar\\\".'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §5.85 SUGAR\", \"stance\": \"supports\", \"note\": \"'Hence, through a later Prakrit form like Pali sakkharā-, the following: ...' — Buck explicitly labels the intermediary Prakrit-like.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1855 (LKT.txt leaf 175)\", \"stance\": \"supports\", \"note\": \"'Sskr. śārkarā: \\\"Sand- oder Körnerzucker\\\", prākrt sakkara, pers. šākār; hieraus einerseits gr. σάκχαρον, lat. saccharum, andererseits ar. sukkar.' — Lokotsch spells the Middle Indic form exactly as Nourai does.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"šekar «شکر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP شکر šekar (older šakar) is a loan from Middle Indic into Middle Persian: MP šakar (Pahlavi 𐭱𐭪𐭥 škr), whence NP šakar > modern Tehrani šekar with the regular raising of the first short a to e. It is not inherited: Hübschmann says so in as many words ('šakar — šakkar \\\"Zucker\\\", das aber indisches LW. ist'), and the geminate -kk- of the Indic form is what the Arabic and the European forms preserve. The commodity and the word travelled together with cane cultivation into Sasanian Iran (Khuzestan) in the 5th-6th c. CE, from where the Arabs took both. Mo'in's own footnote in Borhan-e Qate' sets out the whole chain.\",\n          \"derivation_fa\": \"«شکر» در فارسی نو وام‌واژه‌ای است که از هندی میانه به فارسی میانه رسیده است: پهلوی šakar (نوشتهٔ 𐭱𐭪𐭥)، سپس فارسی نو šakar و در تلفظ تهرانی امروز šekar با بالارفتن قانون‌مند واکهٔ کوتاه نخست. این واژه ارثی نیست؛ هوبشمان در «مطالعات فارسی» ص ۲۳۹ صریحاً می‌نویسد شکر «وام‌واژهٔ هندی است». تشدید ‑کّ‑ صورت هندی همان است که در سکّرِ عربی و صورت‌های اروپایی نگه داشته شده. واژه و کالا با کشت نیشکر در سده‌های پنجم و ششم میلادی به ایران ساسانی (خوزستان) رسید و از آنجا به عرب‌ها. حاشیهٔ معین بر برهان قاطع همین زنجیره را می‌آورد؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%B1\", \"https://www.etymonline.com/word/sugar\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1279\", \"status\": \"partial\", \"note\": \"BQT:1279 = vol. 3 pdf p.70 (running head '۱۲۷۹' confirmed with tools/ref_page.py BQT:1279 --image): that page carries only شکر- compounds (شکرعقیق‌رنگ، شکرفنده، شکرلب، شکررنگ...). The main شکر headword with Mo'in's etymological footnote is three pages earlier, vol. 3 pdf p.67 = printed p.1276, footnote 6: 'پهلوی šakar «اونوالا ۱۵۷»، ... تهرانی shekar. یونانی sakxaron، لاتینی saccharum، معرّب آن سکّر، فرانسوی sucre، انگلیسی sugar، آلمانی Zucker، همه بلاواسطه یا مع‌الواسطه مأخوذ از سانسکریت śarkarā (هندوستان سرزمین باستانی شکر است)' — which supports Nourai's entire chain, just from p.1276 not p.1279.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.239 (HUB.txt leaf 249)\", \"stance\": \"supports\", \"note\": \"'Nach Vokalen: šakar — šakkar \\\"Zucker\\\", das aber indisches LW. ist' — Hübschmann classes NP šakar as an Indian loanword, not an inherited word.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p.163 s.v. سكّر sukkar\", \"stance\": \"supports\", \"note\": \"'sukkar: \\\"Zucker\\\" ← pers. شكر šekar, mp. šakar, mand. šikar' — gives the Middle Persian ancestor explicitly.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, no separate entry\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no numbered entry for šakar (he excludes obvious Indian loans); grep -i 'sakar|zucker' in HRN.txt returns only tabarzad (p.148) and an unrelated passage.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (MON_part2.txt) s.v. قند\", \"stance\": \"supports\", \"note\": \"'بلورهای ریز ساکارز را در تداول عامه شکر نامند' — Mo'in equates the everyday word شکر with the crystalline sugar of the chart.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"sukkar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic سُكَّر sukkar is a Persian loan of the Sasanian/early Islamic period, not a native Semitic root: the Arabic form keeps the Middle Persian geminate (šakar > sukkar) and substitutes s- for the Persian š- (a regular Arabic treatment of Persian š in this word, cf. the parallel Syriac and Mandaic forms with š-). The vowelling sukkar with u in the first syllable is the Arabic nominal pattern fuʿʿal imposed on the loan. From the Arabic form the word spread through the whole Mediterranean with the Arab introduction of cane cultivation into Egypt, Sicily and al-Andalus (8th-10th c.), giving It. zucchero, Sp. azúcar (with the article al-), Pg. açúcar.\",\n          \"derivation_fa\": \"سُکَّر عربی وام‌واژه‌ای فارسی از دورهٔ ساسانی/آغاز اسلام است، نه ریشه‌ای سامی: صورت عربی تشدید فارسی میانه را نگه داشته (šakar > sukkar) و ش فارسی را به س بدل کرده است (همان رفتاری که در صورت‌های سریانی و مندایی هم دیده می‌شود). واکهٔ ضمهٔ هجای نخست از قالب اسمی «فُعَّل» عربی می‌آید. از همین صورت عربی، همراه با گسترش کشت نیشکر به دست مسلمانان در مصر، سیسیل و اندلس (سدهٔ دوم تا چهارم هجری)، واژه به سراسر مدیترانه رفت: ایتالیایی zucchero، اسپانیایی azúcar (با «الـ» عربی) و پرتغالی açúcar. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sugar\"],\n          \"ref_check\": [\n            {\"ref\": \"PLA:163\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p.163 (PLA_pages.txt leaf 178): 'سكر - sukkar: \\\"Zucker\\\" ← pers. شكر sekar, mp. šakar, mand. šikar, syr. ... — Sachar: \\\"Zucker\\\" ← skr. → pers. → griech., frz. sucre, engl. sugar, dtsch. Zucker.' The cited page says exactly what the arrow says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1539 s.v. sugar (leaf 816)\", \"stance\": \"supports\", \"note\": \"'fr. ML. succarum, fr. Arab. sukkar, fr. Pers. shakar, fr. Pali sakkarā, fr. OI. śarkarā'.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1855\", \"stance\": \"supports\", \"note\": \"'... andererseits ar. sukkar. Aus der letzteren Form wurde: it. zucchero, ... frz. sucre, sp. azúcar, pg. açúcar; dtsch. Zucker, engl. sugar.'\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.863 s.v. SUGAR\", \"stance\": \"supports\", \"note\": \"'The Ar. is sukkar, or with the article al-sukkar, and it is probable that our modern forms ... came ... from the Arabic direct, and not through Latin or Greek.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"succarum\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Medieval Latin succarum (also zuccarum, zucchara) is the mercantile Latin rendering of Arabic sukkar taken over in the Italian trading cities from the 11th-12th c., after the Crusades and the Norman conquest of Sicily made cane sugar an article of European commerce. It is a fresh borrowing and is quite distinct from the learned Late Latin saccharum/saccharon (node 10), which had come through Greek a millennium earlier and denoted the medicinal 'Indian honey' of Dioscorides and Pliny; the two forms coexist in Latin, which is precisely why Nourai's chart has two Latin branches.\",\n          \"derivation_fa\": \"لاتینِ میانه succarum (و گونه‌های zuccarum، zucchara) صورت لاتینیِ بازرگانیِ سُکَّر عربی است که از سدهٔ یازدهم و دوازدهم میلادی در شهرهای تجاری ایتالیا رایج شد؛ پس از جنگ‌های صلیبی و فتح سیسیل به دست نورمن‌ها، شکر نیشکری کالای بازرگانی اروپا شد. این وام‌گیری تازه است و با saccharum/saccharon لاتین متأخر (گرهٔ ۱۰) که هزار سال پیش‌تر از راه یونانی آمده و «عسل هندی» داروییِ دیوسکوریدس و پلینیوس را می‌نامید، یکی نیست؛ همین دوگانگی است که نمودار نورایی را دو شاخه کرده است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sugar\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1287\", \"status\": \"not_checked\", \"note\": \"AHD:1287 is a page of the main A-Z text of the 1975/76 American Heritage Dictionary New College edition, which is not open online (only the Watkins Indo-European appendix, reprinted 1985, is on disk as AHD_watkins1985.txt, and it has no *ḱorkā root). The substance — 'Middle English sugre, from Old French sucre, from Medieval Latin succarum, from Arabic sukkar' — is standard in AHD and is confirmed word for word by Klein and Etymonline.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1539 s.v. sugar\", \"stance\": \"supports\", \"note\": \"'ME. suger, sugre, fr. OF. (= F.) sucre, fr. ML. succarum, fr. Arab. sukkar' — the ML form is spelled succarum exactly as in the chart.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (A-?)\", \"stance\": \"silent\", \"note\": \"Webster's 2nd vol. 1 does not reach S; vol. 2 is not open, so no independent Webster reading was possible.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.863\", \"stance\": \"partial\", \"note\": \"Yule gives 'late Latin saccharum' from the Greek and derives the European commercial words 'from the Arabic direct, and not through Latin or Greek' — i.e. he sees the Romance forms as taken straight from Arabic rather than through a Latin succarum, a looser picture than Klein's.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"sucre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French sucre (attested 12th c.) continues Medieval Latin succarum with the ordinary French treatment of the Latin ending (-arum > -re) and of intervocalic -cc- ([kk] > [k]); the Italian trade form zucchero is the same word with the affricate onset that Italian gave to Arabic s- in this word. French sucre then feeds English sugar (node 8) and the modern chemical prefixes sucro-/sucr- and the name sucrose.\",\n          \"derivation_fa\": \"فرانسوی کهن sucre (گواهی‌شده در سدهٔ دوازدهم میلادی) دنبالهٔ succarum لاتین میانه است، با رفتار معمول فرانسوی نسبت به پایانهٔ لاتینی (‑arum > ‑re) و ساده‌شدن ‑cc‑ میان‌واکه‌ای. صورت بازرگانی ایتالیایی zucchero همان واژه است با آغازهٔ سایشی‑انسدادی که ایتالیایی به س عربی داده است. از همین sucre فرانسوی، انگلیسی sugar (گرهٔ ۸) و پیشوندهای شیمیایی sucro‑/sucr‑ و نام sucrose پدید آمده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sugar\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given on this node; checked against Klein, Lokotsch and Etymonline instead (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1539 s.v. sugar; p.1433 s.v. sucro-\", \"stance\": \"supports\", \"note\": \"s.v. sugar 'fr. OF. (= F.) sucre, fr. ML. succarum'; s.v. sucro- 'combining form meaning \\\"sugar\\\". — F. sucre. See sugar.'\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1855\", \"stance\": \"supports\", \"note\": \"'Aus der letzteren [ar. sukkar] Form wurde: it. zucchero, sard. tukkaru, frz. sucre, sp. azucar, pg. açucar.'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"sâkâroz «ساکاروژ» (printed «ساکارُز»)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is genuine — Persian ساکارز sâkâroz/sâkârez is the chemical term for sucrose, and Mo'in tags it [فر.], i.e. a French loan — but the arrow is drawn from the wrong French word. Persian ساکارز renders French saccharose, which Klein (s.v. saccharose) says was 'formed fr. Gk. σάκχαρον \\\"sugar\\\", and subst. suff. -ose', i.e. it belongs to the learned Greek-Latin branch of this chart (node 10), not to the commercial word sucre. What does come from sucre is the English/international sucrose (Klein s.v. sucrose: 'Formed fr. F. sucre, \\\"sugar\\\", with subst. suff. -ose'), which Nourai correctly places under sucre in node 8. So node 7 should hang under Latin saccharon, and as drawn it is disputed. Separately, the JSON script is a misreading: the printed page shows «ساکارُز» (sin-alef-kaf-alef-re with damma-zā), while the extraction produced «ساکاروژ», inserting a واو for the damma and reading ز as ژ.\",\n          \"derivation_fa\": \"خودِ واژه واقعی است: «ساکارز» در فارسی اصطلاح شیمیایی «قند نیشکر» است و معین آن را با نشانهٔ [فر.] یعنی وام‌واژهٔ فرانسوی آورده است؛ اما پیکان از واژهٔ فرانسویِ نادرست کشیده شده. «ساکارز» برابرِ فرانسوی saccharose است و کلاین می‌گوید saccharose از σάκχαρον یونانی به‌اضافهٔ پسوند ‑ose ساخته شده، یعنی به شاخهٔ عالمانهٔ یونانی‑لاتینی همین نمودار (گرهٔ ۱۰) تعلق دارد، نه به sucre بازرگانی. آنچه از sucre آمده sucrose انگلیسی است که نورایی درست در گرهٔ ۸ زیر sucre نهاده است. بنابراین این پیوند به شکلی که کشیده شده پذیرفتنی نیست. افزون بر این، املای فارسیِ استخراج‌شده خطای خوانش اسکن است: صفحهٔ چاپی «ساکارُز» دارد و استخراج آن را «ساکاروژ» خوانده، یعنی ضمّه را واو و «ز» را «ژ» گرفته است.\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"ساکارُز\",\n          \"correct_form\": \"ساکارز (sâkâroz / sâkârez)\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%D8%A7%DA%A9%D8%A7%D8%B1%D8%B2/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1802\", \"status\": \"partial\", \"note\": \"Mo'in's Farhang-e Farsi does have ساکارز, and the vajehyab/abadis text of the Mo'in entry reads '[فر.] ... ماده‌ای که از نیشکر تهیه شود ..., قند نیشکر' — a French loan meaning cane sugar. Mo'in thus confirms the word and its French origin but gives no French etymon, and certainly not sucre; the OCR of MON_part1/part2 on disk carries no printed page numbers, so p.1802 itself could not be located.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1370 s.v. saccharose; p.1433 s.v. sucrose\", \"stance\": \"contradicts\", \"note\": \"'saccharose, n., cane or beet sugar. — Formed fr. Gk. σάκχαρον, \\\"sugar\\\" (see sacchar-), and subst. suff. -ose' vs 'sucrose, n., saccharose (chem.) — Formed fr. F. sucre, \\\"sugar\\\", with subst. suff. -ose.' Klein keeps the two words on the two different branches; the Persian ساکارز is the saccharose one.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. قند / ساکارز (MON_part2.txt lines 15036-15066)\", \"stance\": \"supports\", \"note\": \"'قند معمولی: (شیم.) - ساکارز، جسمی است سفید و بلوری به فرمول C12H22O11' — the word exists in Mo'in with exactly the sucrose sense.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary covers inherited Persian vocabulary only; grep for ساکار returns nothing.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"sugar, sucrose\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English sugar is first recorded late 13th c. as ME suger, sugre, borrowed from Old French sucre; the modern spelling with -g- and the pronunciation with /ʃ/ arise from the English palatalisation of s before the following u ([sju-] > [ʃu-]), the same development as in sure. Sucrose is a 19th-c. chemical coinage (1857, W. A. Miller) built on French sucre with the sugar-suffix -ose that Dumas had extracted from glucose; Klein derives it precisely so. Both words therefore hang correctly under French sucre.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی sugar نخستین بار در اواخر سدهٔ سیزدهم میلادی به‌صورت suger/sugre در انگلیسی میانه دیده می‌شود و از sucre فرانسوی کهن وام گرفته شده است؛ نگارش امروزی با «g» و تلفظ با /ʃ/ از کامی‌شدن s پیش از u در انگلیسی می‌آید (همان تحولی که در sure رخ داده). sucrose واژه‌ای نوساختهٔ شیمی سدهٔ نوزدهم (۱۸۵۷، ویلیام میلر) است که بر پایهٔ sucre فرانسوی و با پسوند قندیِ ‑ose ساخته شده و کلاین نیز همین را می‌گوید. پس هر دو واژه درست زیر sucre فرانسوی نشسته‌اند و ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sugar\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1539\", \"status\": \"supports\", \"note\": \"Klein 1966 p.1539 (KLN_1966.txt leaf 816; the file's leaf-to-page map is p ≈ 2·leaf − 90, which reproduces Nourai's KLN:324, KLN:1370 and KLN:1539 to within two pages): 'sugar, n. — ME. suger, sugre, fr. OF. (= F.) sucre, fr. ML. succarum, fr. Arab. sukkar, fr. Pers. shakar, fr. Pali sakkarā, fr. OI. śarkarā, śarkaraḥ, \\\"gravel, grit, sugar\\\"'. The same page has 'sucrose, n., saccharose (chem.) — Formed fr. F. sucre, \\\"sugar\\\", with subst. suff. -ose.' Both of Nourai's English words are on the cited page with the cited parent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's OCR is badly degraded in the S range; grep '^SUGAR' returns nothing and the surviving fragment at line 2782 ('...made of sugar. The word in Aryan (Pers.)...') is unusable as a quotation.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt\", \"stance\": \"silent\", \"note\": \"grep for the sugar headword in the Funk & Wagnalls volume covering S produced no clean entry text (very noisy OCR); no independent reading obtained.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.863\", \"stance\": \"supports\", \"note\": \"'It. zucchero and zuccaro, Fr. sucre, Germ. Zucker, Eng. sugar, came ... from the Arabic direct' — same immediate chain for English via French.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Greek\",\n          \"words\": \"sakkaron\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek σάκχαρον (also σάκχαρ, σάκχαρι) is a first-century AD borrowing of the Middle Indic word, brought back by the Indian Ocean trade: it first appears in the Periplus Maris Erythraei §14 (μέλι τὸ καλάμινον τὸ λεγόμενον σάκχαρι) and in Dioscorides, Mat. Med. 2.104 ('it is called σάκχαρον and is a kind of honey which solidifies in India'). The Greek geminate -κχ- renders the Middle Indic aspirated geminate -kkh- of sakkharā, and the neuter -ον is a Greek adaptation of the Indic feminine -ā. The route is thus independent of, and about eight centuries earlier than, the Arabic-Romance route of nodes 4-6.\",\n          \"derivation_fa\": \"σάκχαρον یونانی (و گونه‌های σάκχαρ و σάκχαρι) وام‌گیری سدهٔ یکم میلادی از واژهٔ هندی میانه است که از راه بازرگانی اقیانوس هند رسیده: نخستین گواهی‌ها در «پریپلوس دریای اریتره» بند ۱۴ (μέλι τὸ καλάμινον τὸ λεγόμενον σάκχαρι) و در دیوسکوریدس ۲٫۱۰۴ («آن را σάκχαρον می‌نامند و گونه‌ای عسل است که در هند می‌بندد») است. خوشهٔ ‑κχ‑ یونانی برابرِ ‑kkh‑ مشدد و دمیدهٔ sakkharā است و پایانهٔ خنثای ‑ον سازگارسازی یونانیِ ‑ā مؤنث هندی. این راه از راه عربی‑رومی گره‌های ۴ تا ۶ جداست و نزدیک هشت سده کهن‌تر. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/saccharin\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1370\", \"status\": \"supports\", \"note\": \"Klein 1966 p.1370 s.v. 'sacchar-, sacchari-, saccharo-, combining forms meaning \\\"sugar\\\". — Fr. L. saccharon, fr. Gk. σάκχαρον, \\\"sugar\\\", fr. Pali sakkharā, fr. OI. śarkarā, \\\"gravel, grit, sugar\\\".' The page number is confirmed by the OCR page marker '13/U-' (=1370) on that very leaf.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"Buck §5.85 SUGAR\", \"stance\": \"supports\", \"note\": \"Buck quotes the earliest witnesses: 'μέλι τὸ καλάμινον τὸ λεγόμενον σάκχαρι, Peripl. 14; σάκχαρον εἶδος ... Diosc. 2.104; Saccharon et Arabia fert, sed laudatius India, Plin. 12.32' and dates the Greek and Latin transcriptions to the first century AD.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1855\", \"stance\": \"supports\", \"note\": \"'prākrt sakkara ... hieraus einerseits gr. σάκχαρον, lat. saccharum'.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.863\", \"stance\": \"supports\", \"note\": \"'through a Prakrit form sakkara gave ... the Greek σάκχαρ and σάκχαρον'; Yule also defends (against Salmasius) that the ancient σάκχαρον really was cane sugar and not tabashir.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Latin\",\n          \"words\": \"saccharon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin saccharon (Pliny, Nat. Hist. 12.32 'Saccharon et Arabia fert, sed laudatius India, est autem mel in harundinibus collectum') is a direct transcription of the Greek neuter σάκχαρον, retaining the Greek -on ending; the Latinised by-form saccharum (with the Latin second-declension ending) is the one that becomes the standard scientific stem. This learned Latin word, unlike succarum of node 5, was never a commercial term: for a thousand years it named a rare medicinal 'Indian honey', and it is only in modern chemical Latin that it is revived as the base of saccharum, saccharin, saccharose.\",\n          \"derivation_fa\": \"لاتینی saccharon (پلینیوس، تاریخ طبیعی ۱۲٫۳۲: «Saccharon et Arabia fert, sed laudatius India، و آن عسلی است که در نی‌ها گرد می‌آید») آوانگاری مستقیم σάκχαρον خنثای یونانی است و پایانهٔ ‑on یونانی را نگه داشته؛ گونهٔ لاتینی‌شدهٔ saccharum (با پایانهٔ صرف دومِ لاتینی) همان است که ستاک علمی امروزی شده است. این واژهٔ عالمانه برخلاف succarum گرهٔ ۵ هرگز واژهٔ بازرگانی نبود: هزار سال نام «عسل هندیِ» کمیاب دارویی بود و تنها در لاتین شیمیاییِ نو دوباره پایهٔ saccharum و saccharin و saccharose شد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/saccharin\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; checked against Klein p.1370, Buck §5.85 and Lokotsch no. 1855 (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1370 s.v. sacchar-\", \"stance\": \"supports\", \"note\": \"'Fr. L. saccharon, fr. Gk. σάκχαρον' — Klein uses the same Latin form Nourai prints.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §5.85 SUGAR\", \"stance\": \"supports\", \"note\": \"Buck's table gives 'Lat. saccharum (late)' and quotes Pliny 12.32 for saccharon.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.863\", \"stance\": \"supports\", \"note\": \"'the late Latin saccharum'; Pliny and Dioscorides quoted in full in the entry's citation列.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"saccharin, saccharose\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are 19th-century scientific coinages on the Greek-Latin stem, so they do descend from Latin saccharon as drawn. Saccharin was coined in 1879 by Constantin Fahlberg (with Ira Remsen, at Johns Hopkins) on Modern Latin saccharum + the chemical suffix -in, and entered English about 1885; Klein describes it as 'Coined by Fahlberg and List in 1879 fr. ML. saccharum (fr. L. saccharon)'. Saccharose is 'formed fr. Gk. σάκχαρον, \\\"sugar\\\", and subst. suff. -ose' (Klein) and is the Continental name for what English chemistry more often calls sucrose. Nourai's placement of both under Latin saccharon is exactly Klein's.\",\n          \"derivation_fa\": \"هر دو واژه نوساخته‌های علمی سدهٔ نوزدهم بر ستاک یونانی‑لاتینی‌اند و بنابراین همان‌گونه که نورایی کشیده از saccharon لاتین می‌آیند. saccharin را در ۱۸۷۹ کنستانتین فالبرگ (با آیرا رمزن در دانشگاه جانز هاپکینز) از saccharum لاتین نو به‌اضافهٔ پسوند شیمیایی ‑in ساخت و حدود ۱۸۸۵ وارد انگلیسی شد؛ کلاین می‌نویسد «ساختهٔ فالبرگ و لیست در ۱۸۷۹ از ML. saccharum (از L. saccharon)». saccharose نیز «ساخته از σάκχαρον یونانی و پسوند اسمی ‑ose» است و نام قاره‌ای همان چیزی است که شیمی انگلیسی بیشتر sucrose می‌نامد. جای‌گذاری نورایی دقیقاً همان کلاین است.\",\n          \"sources\": [\"https://www.etymonline.com/word/saccharin\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1140\", \"status\": \"not_checked\", \"note\": \"p.1140 of the 1975/76 AHD New College edition (main A-Z text) is not available online; only the Watkins IE appendix is on disk. The claim is however verbatim in Klein p.1370 and in Etymonline, which give Modern/Medieval Latin saccharum < Latin saccharon < Greek sakkharon for saccharin(e).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1370 s.vv. saccharin, saccharose\", \"stance\": \"supports\", \"note\": \"'saccharin, saccharine, n. ... Coined by Fahlberg and List in 1879 fr. ML. saccharum (fr. L. saccharon)'; 'saccharose, n., cane or beet sugar. — Formed fr. Gk. σάκχαρον, \\\"sugar\\\" ... and subst. suff. -ose.'\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt\", \"stance\": \"silent\", \"note\": \"no usable entry recovered from the Funk & Wagnalls OCR for saccharin/saccharose.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"French\",\n          \"words\": \"saccharine\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The French word is real and does come from the Latin/Greek stem: French saccharin, -ine (adj., 18th c., 'of the nature of sugar') is built on Latin saccharum/saccharon with the suffix -in, and the noun la saccharine (1879-80) is the sweetener, taken over from Fahlberg's German Saccharin. So the arrow Latin saccharon > French saccharine is sound. What is not sound is the gloss Nourai attaches, 'sugar, sweet bread': French saccharine has never meant a kind of bread, and no French dictionary gives it that sense. The gloss has evidently been back-formed from the Persian entry of node 13, where the true 'sweet bread' word is the Russian loan سوخاری. Hence plausible rather than confirmed: right derivation, wrong meaning.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی واقعی است و به‌راستی از ستاک لاتینی‑یونانی می‌آید: صفت saccharin/‑ine در فرانسویِ سدهٔ هجدهم بر پایهٔ saccharum لاتین با پسوند ‑in ساخته شده و اسم la saccharine (۱۸۷۹‑۸۰) همان شیرین‌کنندهٔ مصنوعی است که از Saccharin آلمانیِ فالبرگ گرفته شده. پس پیکان «saccharon لاتین ← saccharine فرانسوی» درست است. آنچه نادرست است معنایی است که نورایی نوشته، یعنی «شکر، نان شیرین»: saccharine در فرانسوی هرگز نام نوعی نان نبوده و هیچ فرهنگ فرانسوی چنین معنایی نمی‌دهد. این معنا آشکارا از مدخل فارسیِ گرهٔ ۱۳ به عقب تعمیم داده شده، حال آنکه واژهٔ «نان شیرین» در آنجا «سوخاری» وام‌واژهٔ روسی است. بنابراین: ریشه‌شناسی درست، معنا نادرست.\",\n          \"sources\": [\"https://www.etymonline.com/word/saccharin\"],\n          \"ref_check\": [\n            {\"ref\": \"VOP:208\", \"status\": \"not_checked\", \"note\": \"VOP = Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371/1992). refs_online.json records kind 'none': the book was searched for on archive.org, ketabnak, noorlib and the open web and no copy was found, so p.208 cannot be read. It is Nourai's only support for both node 12 and node 13.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.1370 s.v. saccharine, adj.\", \"stance\": \"partial\", \"note\": \"'saccharine, adj., of the nature of sugar. — See sacchari- and adj. suff. -ine' — confirms the formation and the 'sugary' sense, and gives no bread sense.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale (DEV.txt)\", \"stance\": \"silent\", \"note\": \"Devic treats sucre among the Arabisms but has no article on saccharine (a learned modern derivative, outside his scope).\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan (PHN.txt)\", \"stance\": \"silent\", \"note\": \"Pihan likewise covers only the Arabic/Persian/Turkish loans in French; no saccharine entry.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"sâxârîn «ساخارین» (extra: سوخاری)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"This node conflates two different Persian words. (a) ساخارین sâxârin is a genuine European loan from French/German saccharine/Saccharin, but Mo'in defines it as 'گرد بلور سفید و شیرینی است که در آب به دشواری و در الکل به خوبی حل گردد و مصرف طبی دارد' — a white crystalline sweet powder with medical use, i.e. the artificial sweetener saccharin, NOT 'a type of sweet bread'. (b) The 'sweet bread' word is the second form printed in the box, سوخاری soxâri, and it has nothing to do with sugar: Mo'in glosses it 'قسمی نان شیرینی خشک و سبک' and tags it '[روس.]', a Russian loan — Russian сухарь sukhar' 'rusk, dried bread', from сухой 'dry', which entered Persian through 19th-century Russo-Persian contact in Azerbaijan and Gilan. Nourai himself records this in the chart's NOTE ('MON:1945 derives soxârî from Russian suxâr'), and modern scholarship takes that side unanimously: the resemblance of سوخاری to ساخارین is pure chance. The arrow French saccharine > Persian 'sweet bread' is therefore a folk etymology.\",\n          \"derivation_fa\": \"این گره دو واژهٔ جداگانهٔ فارسی را در هم آمیخته است. نخست «ساخارین» که به‌راستی وام‌واژه‌ای اروپایی از saccharine فرانسوی / Saccharin آلمانی است، اما معین آن را چنین تعریف می‌کند: «گرد بلور سفید و شیرینی است که در آب به دشواری و در الکل به خوبی حل گردد و مصرف طبی دارد» — یعنی همان شیرین‌کنندهٔ مصنوعی، نه «نوعی نان شیرین». دوم «سوخاری» که همان صورت داخل پرانتز در کادر چاپی است و هیچ پیوندی با شکر ندارد: معین آن را «قسمی نان شیرینی خشک و سبک» می‌داند و با نشانهٔ «[روس.]» وام‌واژهٔ روسی می‌شمارد؛ از сухарь روسی به معنای «نان خشک، پِکسیمِت» از сухой «خشک»، که در سدهٔ نوزدهم از راه داد و ستد ایران و روسیه در آذربایجان و گیلان وارد فارسی شده است. خود نورایی هم در یادداشت نمودار به این ریشه اشاره کرده («MON:1945 که soxârî را از suxâr روسی می‌گیرد») و پژوهش امروزی یکسره همان را می‌پذیرد: شباهت «سوخاری» و «ساخارین» تصادفی است. پس پیکان «saccharine فرانسوی ← نان شیرین فارسی» ریشه‌شناسی عامیانه است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%AE%D8%A7%D8%B1%DB%8C/\"],\n          \"ref_check\": [\n            {\"ref\": \"VOP:208\", \"status\": \"not_checked\", \"note\": \"Moshiri's Farhang-e Vazheha-ye Orupayi dar Farsi is not available in any open repository (refs_online.json: kind 'none', re-searched 2026-09), so Nourai's sole authority for this node cannot be examined.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. ساخارین (MON_part1.txt line 73496) and s.v. سوخاری (line 80886)\", \"stance\": \"contradicts\", \"note\": \"'ساخارین: (شیم.) گرد بلور سفید و شیرینی است که در آب به دشواری و در الکل به خوبی حل گردد و مصرف طبی دارد' — the sweetener; and separately 'سوخاری: قسمی نان شیرینی خشک و سبک' — the bread. Two distinct headwords, only the second meaning 'sweet bread'.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir/fatofa/سوخاری\", \"stance\": \"contradicts\", \"note\": \"the online Mo'in entry for سوخاری reads '[ روس . ] (اِ.) برشته' — explicitly flagged as a Russian loan, matching the chart's own NOTE at MON:1945.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots in Persian has no entry for either ساخارین or سوخاری (both being modern European/Russian loans).\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Greek\",\n          \"words\": \"kroke; krokodilos\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two claims, of very different standing. (a) Greek κρόκη 'pebble' (with κροκάλη 'shingle, beach pebbles') as a reflex of the root is acceptable but not straightforward: Pokorny p.615 and Walde-Pokorny I 463 both have to assume a metathesis, *κορκάλα being reshaped to κροκάλη under the influence of κρέκω 'strike, beat' — WP writes 'vielleicht aber hat ein *κορκάλα : śarkarā erst nach letzterer Gruppe Umstellung zu κροκάλη erfahren', i.e. explicitly tentative. (b) κροκόδειλος as 'pebble-worm' (κρόκη + δρῖλος 'worm', through a dissimilated *κροκο-δριλος, so Klein) is what modern scholarship rejects: Beekes says the etymology 'should be forgotten' and treats the word as of unknown, probably Pre-Greek, origin; Herodotus already reports it as an Ionic name for a kind of lizard transferred to the Nile animal. Walde-Pokorny had likewise dismissed the supporting Sanskrit parallel: 'Daß ai. kṛkalāsa-, kṛkala- \\\"Eidechse, Chamäleon\\\" einer ähnlichen Anschauung wie gr. κροκόδειλος entspringe ... ist nicht gestützt.' Because the node's second word is rejected by current scholarship, the node takes the worse verdict.\",\n          \"derivation_fa\": \"دو ادعا در یک کادر، با اعتبار بسیار متفاوت. نخست، κρόκη یونانی «سنگ‌ریزه» (و κροκάλη «ریگ ساحل») که بازتاب این ریشه دانسته شده؛ این پذیرفتنی است اما بی‌دردسر نیست: هم پوکورنی در ص ۶۱۵ و هم والده‑پوکورنی (ج ۱ ص ۴۶۳) ناگزیر «قلب» (metathesis) فرض می‌کنند، یعنی *κορκάλα زیر تأثیر κρέκω «کوفتن» به κροκάλη دگرگون شده، و خودِ والده این را با «vielleicht» یعنی «شاید» می‌آورد. دوم، κροκόδειλος به معنای «کرمِ سنگ‌ریزه» (κρόκη + δρῖλος «کرم»، از *κροκο‑δριλοςِ ناهمگون‌شده، به گفتهٔ کلاین) که پژوهش امروزی آن را رد می‌کند: بیکس می‌گوید این ریشه‌شناسی «باید فراموش شود» و واژه را ناشناخته و احتمالاً پیش‑یونانی می‌داند؛ هرودوت هم آن را نام یونیایی نوعی سوسمار می‌دانست که به جانور نیل منتقل شده است. والده‑پوکورنی نیز شاهد سنسکریت آن را رد کرده بود: «اینکه kṛkalāsa سنسکریت از تصوری همانند κροκόδειλος برخاسته باشد ... پشتوانه ندارد». چون واژهٔ دوم این گره را دانش امروز رد می‌کند، حکم بدتر بر کل گره نهاده شد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CF%81%CE%BF%CE%BA%CF%8C%CE%B4%CE%B5%CE%B9%CE%BB%CE%BF%CF%82\", \"https://www.etymonline.com/word/crocodile\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:324\", \"status\": \"supports\", \"note\": \"Klein 1966 p.324 s.v. crocodile (KLN_1966.txt leaf 207): 'ME. cocodrille, fr. OF. cocodrille, metathesized fr. L. crocodilus, fr. Gk. κροκόδειλος, \\\"lizard; crocodile\\\", dissimilated fr. *κροκο-δριλος, lit. \\\"stone worm\\\", fr. κρόκη, \\\"pebble\\\", and δρῖλος, \\\"worm\\\". Gk. κρόκη is cogn. with OI. śarkaraḥ, śarkarā, \\\"gravel, pebble, sugar\\\"; see sugar.' The cited page says exactly what Nourai's box says — but Klein (1966) predates Beekes and is here the older view.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.615 s.v. ḱorkā\", \"stance\": \"partial\", \"note\": \"'gr. κροκή, κροκάλη \\\"pebble\\\"; perhaps has a *κορκάλα : śarkarā previously after κρέκω \\\"hit\\\" metathesis experienced in κροκάλη' — supports κρόκη with an explicit 'perhaps', and says nothing at all about κροκόδειλος.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.463\", \"stance\": \"contradicts\", \"note\": \"on the crocodile parallel: 'Daß ai. kṛkalāsa-, kṛkala- \\\"Eidechse, Chamäleon\\\" einer ähnlichen Anschauung wie gr. κροκόδειλος entspringe und eine velaranlautende Nebenform von śarkarā voraussetze (Boisacq 520), ist nicht gestützt.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §5.85 SUGAR\", \"stance\": \"supports\", \"note\": \"Buck accepts only the κρόκη equation: 'Skt. śarkara- \\\"gravel, grit\\\" ... : Grk. κρόκη, κροκάλη \\\"pebble\\\". Walde-P. 1.463.'\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Latin\",\n          \"words\": \"crocodillus\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin took the Greek word directly as crocodīlus (Cicero, Pliny), with the by-form corcodilus in inscriptions and manuscripts; the geminated spelling crocodillus that the book prints is a medieval scribal variant, alongside the much commoner Medieval Latin cocodrillus, which shows the r-metathesis that produced the Romance and Middle English forms. The printed page has crocodillus exactly as the JSON has it, so this is the book's own (loose) spelling, not an extraction slip. The step Greek > Latin itself is uncontroversial.\",\n          \"derivation_fa\": \"لاتینی این واژه را یکسره از یونانی گرفت: crocodīlus (در سیسرون و پلینیوس)، با گونهٔ corcodilus در کتیبه‌ها و دست‌نویس‌ها؛ املای مشددِ crocodillus که در کتاب چاپ شده گونه‌ای کاتبانه از دورهٔ قرون وسطاست، در کنار صورت بسیار رایج‌ترِ لاتینِ میانه cocodrillus که «قلبِ» ر در آن رخ داده و صورت‌های رومی و انگلیسی میانه از همان آمده‌اند. صفحهٔ چاپی دقیقاً همان crocodillus را دارد، پس این املا از خود کتاب است نه خطای خوانش اسکن. گامِ «یونانی ← لاتینی» به‌خودیِ‌خود بی‌مناقشه است.\",\n          \"sources\": [\"https://www.etymonline.com/word/crocodile\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; checked against Klein p.324 and Etymonline (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.324 s.v. crocodile\", \"stance\": \"partial\", \"note\": \"Klein spells the Latin 'L. crocodilus' (single -l-) and adds that ME/OF cocodrille is 'metathesized fr.' it — so the single-l classical form, not Nourai's crocodillus, is the standard citation form.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etym. Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"grep produced no crocodilus headword in the 1910 OCR (Walde treats Greek loanwords only selectively).\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"crocodile\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English crocodile is attested c. 1300 as cokedrille, cocodril, borrowed from Old French cocodrille (13th c.), itself from Medieval Latin cocodrillus — the r-metathesized shape of Latin crocodilus. The modern English spelling crocodile is a 16th-century learned restoration on the classical Latin/Greek form, replacing the inherited popular cokedrille; the word thus reaches English by the ordinary Latin > Old French > Middle English route the chart draws.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی crocodile نخست حدود ۱۳۰۰ میلادی به‌صورت cokedrille و cocodril گواهی شده که از cocodrille فرانسوی کهن (سدهٔ سیزدهم) وام گرفته شده و آن خود از cocodrillus لاتینِ میانه، یعنی صورت «قلب‌شدهٔ» crocodilus لاتین. املای امروزی crocodile بازسازی عالمانهٔ سدهٔ شانزدهم بر پایهٔ صورت کلاسیک لاتینی‑یونانی است که جای صورت مردمیِ cokedrille را گرفت. پس واژه از همان راهِ «لاتینی ← فرانسوی کهن ← انگلیسی میانه» که نمودار می‌کشد به انگلیسی رسیده است.\",\n          \"sources\": [\"https://www.etymonline.com/word/crocodile\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; checked against Klein p.324 and Etymonline (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 p.324 s.v. crocodile\", \"stance\": \"supports\", \"note\": \"'crocodile, n. — ME. cocodrille, fr. OF. cocodrille, metathesized fr. L. crocodilus, fr. Gk. κροκόδειλος.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"grep -i 'crocodile' in the Skeat OCR returns no hit; the C range of this scan is defective.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Kormo\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱormo- 'pain, suffering, shame' (Pokorny); modern reconstruction *pḱormo-, to *pḱer- 'to suffer, feel grief and shame'\",\n      \"note\": \"Pokorny IEW p.615 has 'Root/lemma: ḱormo-, Meaning: suffering, pain', with Av. fšarəma-, MP šarm, ON harmr, OE hearm, OS harm, OHG haram, OCS sramъ — exactly the two branches of Nourai's chart. Watkins/AHD likewise: 'kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ḱormo- 615.]' So the root name, the language label and the gloss are all right and both cited references are accurate. The one modern refinement: because Avestan fš- cannot come from plain *ḱ- (Walde-Pokorny already flagged 'trotz des unerklärten Anlauts'), current work reconstructs *pḱormo- to a root *pḱer-, which explains the Iranian fš- (Hübschmann's §128, 'Idg. pḱ- → Av. fš- → NP š-') while leaving Germanic *harmaz and Slavic *sormъ untouched.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۶۱۵ ریشهٔ *ḱormo- را با معنای «رنج، درد» آورده و شاهدهای اوستایی fšarəma‑، فارسی میانه šarm، نورس کهن harmr، انگلیسی کهن hearm، اسلاوی کلیسایی کهن sramъ را برشمرده — یعنی همان دو شاخهٔ نمودار نورایی. واتکینز نیز در پیوست فرهنگ American Heritage می‌نویسد «kormo-: درد. ژرمنی *harmaz در انگلیسی کهن hearm، harm». پس نام ریشه، برچسب زبانی و معنا درست است و هر دو ارجاع دقیق‌اند. تنها اصلاح امروزی این است که «فش» اوستایی نمی‌تواند از *ḱ ساده بیاید — والده‑پوکورنی هم از «آغازهٔ توضیح‌ناشدهٔ» آن یاد کرده بود — و از این رو امروز ریشه را *pḱormo- از ستاک *pḱer- بازسازی می‌کنند؛ همان قاعده‌ای که هوبشمان در بند ۱۲۸ «مطالعات فارسی» آورده: «pḱ هندواروپایی در اوستایی fš و در فارسی نو ش می‌شود».\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%85\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:615\", \"status\": \"supports\", \"note\": \"Pokorny p.615 (POK_full.txt): 'Root / lemma: ḱormo- | Meaning: suffering, pain | Material: Avestan fšarəma- n. \\\"sense of shame before\\\", Middle Persian šarm ds.; Old Icelandic harmr \\\"sorrow, distress\\\", Old English hearm, Old Saxon harm ... Old Bulgarian sramъ. References: WP. I 463, Trautmann 299. Page(s): 615.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.463\", \"stance\": \"supports\", \"note\": \"'ḱormo- \\\"Qual, Schmerz, Schmach\\\". Aisl. harmr ... ags. hearm ... abg. sramъ \\\"Scham\\\"; vermutlich (trotz des unerklärten Anlauts) av. fšarəma- m. \\\"Scham(gefühl vor)\\\", mp. np. šarm ds.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kormo-\", \"stance\": \"supports\", \"note\": \"'kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ḱormo- 615.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck §16.45 SHAME, p.1141\", \"stance\": \"supports\", \"note\": \"'ChSl. sramъ, SCr. sram ... : ON harmr \\\"grief\\\", etc. (16.32), and prob. also Av. fšarəma-, NPers. šarm \\\"shame\\\". Walde-P. 1.463.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"fšarema\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Avestan word is real and correctly transliterated: Younger Avestan fšarəma- m., which Bartholomae (Altiranisches Wörterbuch col. 1030) glosses 'Scham(gefühl) vor —' with the Vidēvdād passage mašyānąm parə fšarəmāt 'out of shame before men' (V. 15.9-10). Two qualifications make this plausible rather than confirmed. First, the gloss: fšarəma- means 'shame, sense of shame', not 'pain'; 'pain, suffering' is the meaning of the reconstructed root as a whole (carried by the Germanic branch), and Nourai has copied the root gloss onto the Avestan box. Second, the attachment to *ḱormo-: Bartholomae himself writes only 'Et. ?', Pokorny and Walde-Pokorny attach it with 'vermutlich' and note that the initial fš- is unexplained under *ḱ-; the difficulty is resolved only by the modern *pḱormo- with Hübschmann's rule Idg. pḱ- > Av. fš-.\",\n          \"derivation_fa\": \"واژهٔ اوستایی واقعی است و آوانگاری آن نیز درست: اوستایی متأخر fšarəma‑ (مذکر) که بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۰۳۰ آن را «شرم، حیا از کسی» معنا کرده و شاهد وندیداد را می‌آورد: mašyānąm parə fšarəmāt «از شرم مردمان» (وندیداد ۱۵٫۹‑۱۰). دو نکته سبب می‌شود حکم «با احتیاط پذیرفتنی» باشد نه «تأییدشده». نخست معنا: fšarəma‑ یعنی «شرم، حیا»، نه «درد»؛ «درد و رنج» معنای کل ریشه است که شاخهٔ ژرمنی آن را نگه داشته و نورایی معنای ریشه را روی کادر اوستایی نشانده است. دوم پیوند با *ḱormo-: خود بارتولومه فقط می‌نویسد «ریشه‌شناسی؟»، و پوکورنی و والده‑پوکورنی آن را با قید «احتمالاً» می‌بندند و یادآور می‌شوند که آغازهٔ fš‑ با *ḱ توضیح‌پذیر نیست؛ این دشواری تنها با بازسازی امروزی *pḱormo- و قاعدهٔ هوبشمان (pḱ هندواروپایی ← fš اوستایی) حل می‌شود.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:615\", \"status\": \"partial\", \"note\": \"Pokorny p.615 does list 'Avestan fšarəma- n. \\\"sense of shame before\\\"' under ḱormo-, so the derivation is the cited page's — but the page glosses it 'shame', not 'pain', and Walde-Pokorny I 463, which Pokorny is condensing, hedges with 'vermutlich (trotz des unerklärten Anlauts)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiWb col. 1030 (BRT.txt leaf 575)\", \"stance\": \"partial\", \"note\": \"'j. fšarəma- m. \\\"Scham(gefühl) vor —\\\" (Gen.): mašyānąm parə fšarəmāt \\\"aus Scham vor den Menschen\\\" V. 15.9, 10. Et.? — mp. (Pü.), np. šarm.' Bartholomae confirms the form, the meaning 'shame' and the Persian continuation, but leaves the IE etymology open.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §128, p.186 and p.235\", \"stance\": \"supports\", \"note\": \"'Idg. pḱ- → Av. fš- → arm. np. s im Anlaut'; and 'šarm \\\"Scham\\\" = zd. fšarəma-, osset. äfsarm' — Hübschmann derives the fš- from an IE cluster pḱ-, which is what modern *pḱormo- formalises.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §16.45 SHAME p.1141\", \"stance\": \"supports\", \"note\": \"lists 'Av. fšarəma-' in the SHAME table (not under PAIN), and connects it with ON harmr 'grief'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"šarm «شرم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP شرم šarm 'shame, modesty' is the direct continuation of Middle Persian šarm (Pahlavi 𐭱𐭥𐭬 šʿm), from Old Iranian *fšarma- — the same word as Avestan fšarəma-. The Iranian development is regular: the initial cluster fš- is simplified to š- in Persian (contrast Ossetic äfsarm, which keeps the f-), while the anaptyctic vowel of Avestan fšarəma- is not represented in the West Iranian form. Horn's Grundriss no. 780 (p.172) sets the chain out exactly: 'šerm \\\"Schaam\\\". aw. fšarəma- \\\"Schaam\\\"; phlv. šarm \\\"Schaam\\\", šarm-gāh \\\"Genitalien\\\"', with the Ossetic, Balochi šarm and Kurdish šerm cognates. The extended senses in Persian — 'modesty, pudency' and, in the compound شرمگاه, 'private parts' — are already Middle Persian, and the Hâfez line quoted in the chart (شرمنده رهروی که عمل بر مجاز کرد) uses the derived شرمنده.\",\n          \"derivation_fa\": \"«شرم» فارسی نو دنبالهٔ مستقیم فارسی میانهٔ šarm است (نوشتهٔ پهلوی 𐭱𐭥𐭬)، از ایرانی باستان *fšarma‑ که همان واژهٔ اوستایی fšarəma‑ است. تحول ایرانی آن قاعده‌مند است: خوشهٔ آغازی fš‑ در فارسی به ش ساده می‌شود (برخلاف آسی äfsarm که «ف» را نگه داشته)، و واکهٔ میانجی صورت اوستایی در گونهٔ ایرانی غربی بازتاب ندارد. هرن در بند ۷۸۰ «دستور ریشه‌شناسی فارسی نو» صفحهٔ ۱۷۲ همین زنجیره را می‌آورد: «شرم؛ اوستایی fšarəma‑ «شرم»؛ پهلوی šarm، šarm‑gāh «اندام‌های تناسلی»» و آسی و بلوچی šarm و کردی šerm را نیز نام می‌برد. معنای گستردهٔ «حیا» و ترکیب «شرمگاه» هم از فارسی میانه به ارث رسیده و بیت حافظ که در کادر نقل شده («شرمنده رهروی که عمل بر مجاز کرد») صورت مشتق «شرمنده» را به کار برده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:172\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p.172 (HRN.txt leaf 194), entry no. 780: 'šerm \\\"Schaam\\\". aw. fšarəma- \\\"Schaam\\\"; phlv. šarm \\\"Schaam\\\", šarm-gāh \\\"Genitalien\\\" (vd. 16 (5) Gl.). oss. t. äfsärm, d. äfsärmi \\\"Schande\\\" (121); LW. afy. bel. (253) šarm \\\"Schaam\\\", kurd. šerm.' Exactly the arrow Nourai draws.\"},\n            {\"ref\": \"BQT:1264\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 3 printed p.1264 = pdf p.55 (BQT_v3_pages.txt leaf 54): headword 'شرم ۴ بر وزن ارم ... و ناموس ... و آلت تناسل را نیز گویند'; Mo'in's footnote 4 at the foot of that page reads 'اوستا Fšarema (حیا: عفت)، پهلوی šarm (تاوادیا ۱۰۵)، آسی äfsinmi ..., افغانی، بلوچی šarm (حیا)، کردی šerm' — the Avestan > Pahlavi > Persian chain in Mo'in's own words. The next footnote adds 'شرمگاه < پهلوی šarm-gāh'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.235 (§127) and p.186\", \"stance\": \"supports\", \"note\": \"'šarm \\\"Scham\\\" = zd. fšarəma-, osset. äfsarm'; index p.? cross-refers to 'sarm \\\"Scham\\\" H. 780', i.e. Horn's entry 780.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\", \"note\": \"grep '^šarm' / '^sarm' in PHD.txt and PHD_mackenzie.txt returns only 'sarmag [slm\\\\'k] coldness'; MacKenzie's short glossary does not list šarm, so no confirmation from him (Horn and Mo'in both cite the Pahlavi form from Vidēvdād glosses and Tavadia).\"},\n            {\"src\": \"BRT\", \"where\": \"AiWb col. 1030\", \"stance\": \"supports\", \"note\": \"the fšarəma- entry ends 'mp. (Pü.), np. šarm' — Bartholomae himself gives the Middle and New Persian continuants.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §16.45 SHAME p.1141\", \"stance\": \"supports\", \"note\": \"'ChSl. sramъ ... : ON harmr \\\"grief\\\" ... and prob. also Av. fšarəma-, NPers. šarm \\\"shame\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"harmaz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *harmaz m. 'grief, injury, insult' is the regular Germanic outcome of the o-grade *ḱormo-: PIE *ḱ gives Proto-Germanic *h by the satem-independent centum treatment plus Grimm's Law (*k > *h), and the thematic *-o-s becomes Germanic *-a-z. It is continued by Old Norse harmr 'sorrow, grief, injury', Old English hearm, Old Saxon harm, Old High German har(a)m, Modern German Harm. Watkins states the node in exactly these terms.\",\n          \"derivation_fa\": \"ژرمنی آغازین *harmaz «اندوه، آزار، توهین» برآیند قاعده‌مند درجهٔ o ریشه، یعنی *ḱormo-، است: kʲ هندواروپایی در ژرمنی (که زبانی کنتوم است) نخست k و سپس بر اثر قانون گریم h می‌شود، و پایانهٔ *‑o‑s به *‑a‑z ژرمنی بدل می‌گردد. دنبالهٔ آن نورس کهن harmr «اندوه، آسیب»، انگلیسی کهن hearm، ساکسون کهن harm، آلمانی علیای کهن har(a)m و آلمانی امروز Harm است. واتکینز دقیقاً همین را می‌گوید؛ ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins, AHD Indo-European Roots (1985 ed., AHD_watkins1985.txt): 'kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ḱormo- 615.]' — the Germanic form, its gloss and its parent root are all exactly Nourai's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.615 s.v. ḱormo-\", \"stance\": \"supports\", \"note\": \"'Old Icelandic harmr \\\"sorrow, distress, damage, injury\\\", Old English hearm m. \\\"distress, pain, damage\\\", Old Saxon harm \\\"pain, injury\\\", Middle Low German harm, Old High German haram \\\"affliction, damage, insult\\\", Modern High German Harm.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.463\", \"stance\": \"supports\", \"note\": \"'Aisl. harmr \\\"Betrübnis, Kummer, Harm, Kränkung\\\", ags. hearm \\\"Kummer, Schmerz, Schade\\\", as. harm \\\"Schmerz, Kränkung\\\" ... ahd. har(a)m \\\"Leid, Harm, Schimpf\\\", nhd. Harm.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"harm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English hearm 'hurt, injury, evil, grief' (with the West Saxon breaking of *a to ea before r + consonant) gives Middle English harm and modern harm, the vowel restored to /a/ by Anglian and Norse influence; the verb hearmian is equally old. The word is an ordinary inherited Germanic noun, not a loan, and its meaning has narrowed from 'grief, insult' to 'physical or material damage'.\",\n          \"derivation_fa\": \"انگلیسی کهن hearm «آسیب، بدی، اندوه» (با «شکستِ» واکه‌ای غرب‌ساکسونی که a را پیش از r + همخوان به ea بدل کرده) به harm انگلیسی میانه و امروزی رسیده و واکهٔ /a/ آن زیر تأثیر گویش انگلی و نورس بازگشته است؛ فعل hearmian نیز به همان کهنگی است. این واژه اسمی ارثی و ژرمنی است، نه وام‌واژه، و معنایش از «اندوه، توهین» به «آسیب مادی یا بدنی» تنگ شده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; the identical claim is on the cited AHD page of the parent node ('Germanic *harmaz in Old English hearm, harm: HARM').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index 'HARM kormo-'\", \"stance\": \"supports\", \"note\": \"the reverse index of the Watkins appendix lists 'HARM kormo-', confirming English harm as the sole English reflex of this root.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.615\", \"stance\": \"supports\", \"note\": \"'Old English hearm m. \\\"distress, pain, damage, pity\\\"' listed directly under ḱormo-.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-273.json > /dev/null && echo \"VALID JSON\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 273",
 "description": "Write and validate verification JSON"
}
```


### [2026-09-06T21:26:57.462Z] TOOL RESULT

```
VALID JSON
nodes verified: 20/20
node verdicts: {'confirmed': 14, 'disputed': 3, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_checked': 10, 'partial': 3}
books consulted: {'supports': 35, 'silent': 12, 'partial': 5, 'contradicts': 4} | by book: {'KLN': 10, 'SYN': 7, 'HJB': 6, 'LKT': 4, 'MON': 4, 'WLD': 3, 'HUB': 3, 'POK': 3, 'ARY': 2, 'SKT': 2, 'FSD': 2, 'BRT': 2, 'PLA': 1, 'HRN': 1, 'WEB': 1, 'DEV': 1, 'PHN': 1, 'LEW': 1, 'PHD': 1, 'AHD': 1}
```


## [2026-09-06T21:27:03.806Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -i \"s/citation列/citation list/\" data/verification/page-273.json && grep -c \"citation list\" data/verification/page-273.json && python3 -m json.tool data/verification/page-273.json > /dev/null && echo OK && python3 tools/verify_check.py 273 | tail -6",
 "description": "Fix stray character and revalidate"
}
```


### [2026-09-06T21:27:06.072Z] TOOL RESULT

```
1
OK
nodes verified: 20/20
node verdicts: {'confirmed': 14, 'disputed': 3, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_checked': 10, 'partial': 3}
books consulted: {'supports': 35, 'silent': 12, 'partial': 5, 'contradicts': 4} | by book: {'KLN': 10, 'SYN': 7, 'HJB': 6, 'LKT': 4, 'MON': 4, 'WLD': 3, 'HUB': 3, 'POK': 3, 'ARY': 2, 'SKT': 2, 'FSD': 2, 'BRT': 2, 'PLA': 1, 'HRN': 1, 'WEB': 1, 'DEV': 1, 'PHN': 1, 'LEW': 1, 'PHD': 1, 'AHD': 1}
```


## [2026-09-06T21:27:31.946Z] AGENT

Page 273 (book p. 243) verified. `verify_check.py 273` reports 0 PROBLEM lines.

**Counts** — 2 entries, 20 nodes: roots 2 confirmed; nodes 14 confirmed, 3 plausible, 3 disputed. Ref checks: 8 supports, 3 partial, 10 not_checked. 56 `consulted` readings (35 supports, 5 partial, 4 contradicts, 12 silent).

**Disputed / plausible items**
- **Korkâ #7 `sâkâroz` (Persian, ساکارُز)** — disputed: the word is real (Mo'in tags it `[فر.]`, = sucrose) but it renders French *saccharose*, which Klein derives from Gk. σάκχαρον + ‑ose, i.e. the Greek/Latin branch (node 10) — not from *sucre*. English *sucrose* is the one from *sucre*, and Nourai already has that right at node 8.
- **Korkâ #13 `sâxârîn` «ساخارین» (سوخاری)** — disputed: two words conflated. Mo'in: ساخارین = the artificial sweetener saccharin; سوخاری = "قسمی نان شیرینی خشک و سبک", tagged `[روس.]` (Russian сухарь 'rusk'). The chart's own NOTE (MON:1945) says so; modern scholarship agrees the resemblance is chance.
- **Korkâ #14 `kroke; krokodilos`** — disputed: κρόκη 'pebble' is fine (Pokorny/WP accept it only with a metathesis and a "perhaps"), but 'pebble-worm' for κροκόδειλος is rejected by Beekes ("should be forgotten"); Walde-Pokorny I 463 had already called the supporting Skt. *kṛkalāsa-* parallel "nicht gestützt". Klein (KLN:324) does say exactly what Nourai says — he is the pre-Beekes view.
- **Korkâ #12 French `saccharine`** — plausible: derivation from L. saccharon is right, but 'sweet bread' is not and never was a French sense (back-formed from node 13).
- **Korkâ #15 Latin `crocodillus`** — plausible: book's own loose spelling (classical *crocodīlus*, ML *cocodrillus*); page image confirms the extraction is faithful.
- **Kormo #1 Avestan `fšarema`** — plausible: form correct (Bartholomae col. 1030) but it means 'shame', not 'pain'; Bartholomae writes "Et.?" and Pokorny/WP attach it only "vermutlich… trotz des unerklärten Anlauts". Modern *pḱormo-* (Hübschmann §128 pḱ- > Av. fš-) fixes that.

**Extraction error for the owner to fix (1)**
- Entry 0, node 7: JSON has script `ساکاروژ`; the printed page (600 dpi crop) shows **`ساکارُز`** — the damma was read as و and ز as ژ. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/273.png`.

**Reference-page notes**
- `BQT:1279` marked *partial*: p.1279 (vol. 3 pdf p.70, running head confirmed via `ref_page.py`) carries only شکر- compounds; Mo'in's etymological footnote for شکر (Pahlavi šakar … Skt. śarkarā, Gk. sakxaron, Ar. سکّر, Fr. sucre, Eng. sugar) is on **p.1276** (pdf p.67).
- `BQT:1264` (شرم), `HRN:172` (no. 780), `PLA:163` (sukkar), `POK:615` (both roots), `KLN:324/1370/1539`, `AHD` (kormo-) all check out verbatim. Useful side-finding: for `KLN_1966.txt` the working leaf→page map is **p ≈ 2·leaf − 90** (verified by the OCR page marker "1370" on leaf 728); the anchors in `refs_online.json` are ~67 pages off.
- `VOP:208` (Moshiri) not checkable — no copy exists online; it is Nourai's only support for nodes 12 and 13. `AHD:1287` / `AHD:1140` are 1976 main-text pages, not open; substance cross-checked in Klein/Etymonline.

Nine web pages archived via `fetch_source.py` (Wiktionary شکر/شرم/κροκόδειλος/शर्करा, Etymonline sugar/crocodile/saccharin, abadis سوخاری/ساکارز).
