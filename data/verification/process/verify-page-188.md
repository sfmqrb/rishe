# Verification process log — verify-page-188


## [2026-09-06T02:13:13.541Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 188 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-188.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-188.json. Write /home/sfmqrb/git/rishe/data/verification/page-188.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 188` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:13:14.726Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:13:15.457Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:13:15.477Z] TOOL RESULT

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


## [2026-09-06T02:13:15.991Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-188.txt"
}
```


### [2026-09-06T02:13:16.010Z] TOOL RESULT

```
1	=== PDF page 188 (book page 158) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gher 1, Gherd; Ghordho : to grasp, enclose; an enclosed land, yard, garden  (refs POK:442, 444)
4	#1 (parent #0) [Avestan / Old Persian] refs=WLD1:603; HRN:6; HUB:6; FFD:25 | zar 1 : to harm ; â-zâr : harm ☞Apo ; âzâra : oppressed
5	  #2 (parent #1) [Persian] refs=WLD1:603; FFD:25 | âzâr «آزار ( آزارش )» : harm ; âzordan «آزردن ( آزاردن ، آزرده )» : to harm
6	#3 (parent #0) [Sogdian] refs=SOD:55 | `pz`rn : to harm
7	#4 (parent #0) [Greek] refs=AHD | xorus : an enclosed dancing group
8	  #5 (parent #4) [Latin] refs=None | 
9	    #6 (parent #5) [French] refs=None | 
10	      #7 (parent #6) [Persian] refs=MON:2927 | kor «کُر» : a singing group
11	      #8 (parent #6) [English] refs=None | chorus, choir
12	#9 (parent #0) [Greek] refs=KLN:284 | ğr-on-os, chronos, xronos : that which encloses all things, time
13	  #10 (parent #9) [Arabic] refs=TAD:56 | qarn : a century
14	    #11 (parent #10) [Persian] refs=MON:2665 | qarn «قَرن ( قرون )» : a century
15	  #12 (parent #9) [Latin] refs=AHD:240 | chronicus : time
16	    #13 (parent #12) [French] refs=AHD; KLN | chronique
17	      #14 (parent #13) [English] refs=AHD; KLN | chronic, chronicle, chronological, chronometer, synchronize
18	#15 (parent #0) [Germanic] refs=None | 
19	  #16 (parent #15) [English] refs=AHD | yard, orchard, garden, kindergarten
20	#17 (parent #0) [Latin] refs=AHD | hortus : garden
21	  #18 (parent #17) [English] refs=None | horticulture, court, courtesy, curtain
22	--- entry 1 ---
23	ROOT Gher 2 -> redirect to Ghlâd
24	
```


## [2026-09-06T02:13:19.180Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-188.json",
 "description": "Read source JSON for page 188"
}
```


### [2026-09-06T02:13:19.224Z] TOOL RESULT

```
{
  "pdf_page": 188,
  "book_page": 158,
  "entries": [
    {
      "root": {
        "name": "Gher 1, Gherd; Ghordho",
        "lang": "Indo-European",
        "refs": "POK:442, 444",
        "gloss": "to grasp, enclose; an enclosed land, yard, garden"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "WLD1:603; HRN:6; HUB:6; FFD:25",
          "words": [
            {"translit": "zar 1", "gloss": "to harm", "script": null},
            {"translit": "â-zâr", "gloss": "harm", "script": null, "see": ["Apo"]},
            {"translit": "âzâra", "gloss": "oppressed", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "WLD1:603; FFD:25",
          "words": [
            {"translit": "âzâr", "gloss": "harm", "script": "آزار ( آزارش )"},
            {"translit": "âzordan", "gloss": "to harm", "script": "آزردن ( آزاردن ، آزرده )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:55",
          "words": [
            {"translit": "`pz`rn", "gloss": "to harm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "xorus", "gloss": "an enclosed dancing group", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:2927",
          "words": [
            {"translit": "kor", "gloss": "a singing group", "script": "کُر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "chorus, choir", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:284",
          "words": [
            {"translit": "ğr-on-os, chronos, xronos", "gloss": "that which encloses all things, time", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Arabic",
          "refs": "TAD:56",
          "words": [
            {"translit": "qarn", "gloss": "a century", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:2665",
          "words": [
            {"translit": "qarn", "gloss": "a century", "script": "قَرن ( قرون )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "Latin",
          "refs": "AHD:240",
          "words": [
            {"translit": "chronicus", "gloss": "time", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "French",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "chronique", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "chronic, chronicle, chronological, chronometer, synchronize", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Germanic",
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
          "refs": "AHD",
          "words": [
            {"translit": "yard, orchard, garden, kindergarten", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "hortus", "gloss": "garden", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "horticulture, court, courtesy, curtain", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gher 2",
        "redirect": "Ghlâd"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T02:13:20.350Z] TOOL CALL #4: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; sed -n '1,200p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-06T02:13:20.408Z] TOOL RESULT

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


## [2026-09-06T02:15:13.421Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','WLD','WLD1','AHD','KLN','HRN','HUB','FFD','SOD','TAD','MON','BRT','PHD','CHEUNG','SKT','LEW','LAT','IEC','SYN','NYB','ARY','BQT','FSD','WEB','AFM','PLA','LKT','FVQ']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T02:15:13.824Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 /home/sfmqrb/git/rishe/data/verification/page-187.json 2>/dev/null || ls /home/sfmqrb/git/rishe/data/verification/ | tail -20",
 "description": "Peek at a prior verification file"
}
```


### [2026-09-06T02:15:15.004Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== WLD1 MISSING
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== CHEUNG MISSING
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt;
```


### [2026-09-06T02:15:15.079Z] TOOL RESULT

```
{
  "pdf_page": 187,
  "book_page": 157,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Ghen",
      "verdict": "confirmed",
      "modern_form": "PIE *gʰen- 'to gnaw, bite, scratch, grind' (Pokorny 436-437 ghen-2 'aufbrechen, zerreiben, kratzen'; Watkins/AHD ghen- 'to gnaw')",
      "note": "The root box is right on all three counts, and the page it cites is the right page. Pokorny's second ghen- runs pp.436-437 and is glossed 'zernagen, zerreiben, kratzen' ('to crack open, grind, scratch'); Watkins in the AHD appendix condenses this to 'ghen-. To gnaw' and cites '[Pok. ghen- 436.]', which is exactly Nourai's 'Ghen : to bite, chew / POK:436'. One qualification that Nourai does not make: the bare root is never attested — Pokorny writes 'Nur in den Erweiterungen ghnegh-, ghnad(h)-, ghnei-, ghneu-' ('only in the extensions'), so *gʰen- is an abstraction from a family of *gʰn- extensions, and the two branches Nourai draws come from two different extensions: the Avestan word from the guttural extension *gʰneǵʰ- and the gnat-word from the dental extension *gʰnad(h)-. The chart is otherwise a faithful and rather elegant reduction of the Pokorny article: both of the branches Nourai keeps (Avestan aiwi-γnixta-, Germanic gnag-/gnatt-) are the first two items Pokorny himself lists.",
      "note_fa": "ریشهٔ هندواروپایی آغازین *gʰen- «جویدن، گاز گرفتن، خراشیدن» واقعی است و ارجاع نورایی هم درست: پوکورنی در صفحات ۴۳۶–۴۳۷ مادّهٔ دوم ghen- را با معنای «شکافتن، ساییدن، خراشیدن» آورده و واتکینز در پیوست فرهنگ American Heritage همان را «to gnaw» می‌نویسد و به «Pok. ghen- 436» ارجاع می‌دهد. تنها نکته‌ای که نورایی نگفته این است که خودِ ریشه هرگز به‌تنهایی گواهی نشده؛ پوکورنی تصریح می‌کند که این ریشه «تنها در گسترش‌های ghnegh-، ghnad(h)-، ghnei-، ghneu-» دیده می‌شود. بنابراین دو شاخهٔ نمودار در حقیقت از دو گسترش متفاوت‌اند: واژهٔ اوستایی از *gʰneǵʰ- و واژهٔ ژرمنی gnatt از *gʰnad(h)-. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/gnat",
        "https://en.wiktionary.org/wiki/gnaw"
      ],
      "ref_check": [
        {
          "ref": "POK:436",
          "status": "supports",
          "note": "POK_full.txt: 'Root / lemma: ghen- / Meaning: to crack open, grind, scratch / Material: Only in den extensions ghnegh- : ghnegh-, ghna(dh)-, ghnei-, ghneu- ... References: WP. I 584 f. ... Page(s): 436-437'. The lemma begins on p.436, so Nourai's POK:436 is exact."
        }
      ],
      "consulte
```


## [2026-09-06T02:15:21.899Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 44[0-9]\" POK_full.txt | head -40",
 "description": "Find Pokorny pages 440-449 lemmas"
}
```


### [2026-09-06T02:15:21.953Z] TOOL RESULT

```
33132:Page(s): 440 
33157:Page(s): 445 
33173:Page(s): 445 
33189:Page(s): 446 
36764:Page(s): 444 
36821:Page(s): 440-441 
36836:Page(s): 441 
36879:Page(s): 441-442 
36923:Page(s): 442-443 
36966:Page(s): 443 
36997:Page(s): 443 
37002:Page(s): 443 
37094:Page(s): 445-446 
37125:Page(s): 446 
37153:Page(s): 446 
37190:Page(s): 447 
37233:Page(s): 447 
37344:Page(s): 447-448 
37362:Page(s): 448 
37724:Page(s): 449
```


## [2026-09-06T02:15:22.670Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"^ *gher-\\|ghordho\\|ghor-dho\\|ghortos\" AHD_watkins1985.txt | head -30",
 "description": "Grep AHD Watkins for gher"
}
```


### [2026-09-06T02:15:22.728Z] TOOL RESULT

```
521:gher-'. To grasp, enclose; with derivatives meaning “enclosure.” 1. Suffixed zero-grade form *ghr-dh- in: a. Germanic *gurdjan in Old English gyrdan, to gird: GIRD; b. Old English gyrdel, girdle: GIRDLE; c. Old Norse gjordh, girdle, girth: GirTH. 2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure, in: a. Germanic *gardaz in (i) Old English geard, enclosure, garden, yard: YARD?; ORCHARD (ii) Old Norse gardhr, garden, yard: GARTH (iii) Old High German garto, gar- den: KINDERGARTEN (iv) Old North French gardin, gar- den: GARDEN (v) compound *midja-gardaz, “middle zone,” earth (see medhyo-); b. Latin hortus, garden: HORTICULTURE, ORCHARD, ORTOLAN. 3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- (*ko(m)-, collec- tive prefix, “together”; see kom) in Latin cohors (stem cohort-), enclosed yard, company of soldiers, multitude: COHORT, CORTEGE, COURT, COURTEOUS, COURTESAN, (COURTESY), COURTIER, (CURTILAGE), (CURTSY). 4. Per- haps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing), dance, dramatic chorus: (CHOIR), (CHORAL), (CHORALE), CHORIC, (CHORISTER), CHORUS; CHORAGUS, TERPSICHORE. [Pok. 4. gher- 442, gherd- 444.]
522:gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grétan, to speak to, greet: GREET. [Pok. 1. gher- 439.]
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
```


## [2026-09-06T02:15:31.087Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36880,36970p' POK_full.txt",
 "description": "Print Pokorny lemmas around p.442"
}
```


### [2026-09-06T02:15:31.150Z] TOOL RESULT

```
Root / lemma: gher-4 
Meaning: to gripe, grab, enclose 
Note: extended gheirH^-isee below) 



Material: Old Indie haratT brings, carries, gets, takes ', harana-n. "the bringing, receiving, 
donation ' etc., haras-u. " receiving, griping, handle, grasp, power, force, might'; 

gr. xopTO(; m. " enclosed place (v. sub fin.), but always with collat. notion of a feeding- 
place: in II., farmyard, in which the cattle were kept, generally, any feeding-ground, 
pasturage, fodder, provender, esp. for horses and cattle, courtyard, meadowland '; 
doubtful, whether here xop6(; " dancing place, place for dancing ' as originally " inserted 
place'; about xopiov " placenta, afterbirth ', etc. see below gher-5, about xeip "hand' under 
ghes- 

Oscan heriiad^ furled, ', [hjerrfns^ wrinkled, to drawn together in wrinkles ', Latin cohors 
" fenced courtyard, stockyard, troop, multitude, crowd, cortege ', from *co+ Indo Germanic 
*ghrtfs^ summarization', in ablaut to /70/Y^s "garden as fenced place' (in old latin also villa), 
Oscan hurz^ hortus lucus '; dubious is Latin hTr, Tr^ palm of the hand ', s. WH. I 649; 

Irish gort^ cornfield, the standing corn, growing corn, crop in a field, a field, ground, soil 
', gall. ^o/Yo-and gortla^ hedge ' (v. Wartburg), cymr. garth ^corra\, pen, fold, hurdle, 
paddock ' (das aafterOld Icelandic loanword gardd), bret. garz^ hedge, fence', in addition 
Irish lub-gort^ garden', acymr. Plur. lulrd, ncymr. Iluarth, acorn. luworch-gult^\NM garden', 
mcorn. /on/a/f/? "garden', bret. liorz6s. 

Maybe Albanian gardh^ fence ' : Welsh garthlo\d, enclosure' common lllyrian Celtic -th 
suffix. 

Is not to be decided, whether Gothic garda' hurdle, stockyard ', Old Frisian garda. Old 
Saxon gardo. Old High German ^5/Yo "garden' in Indo Germanic *ghor-t6-ox in *ghopA^o- 
are based on (see below *ghe/6'^-). - Norwegian gaare " annual ring (in a tree) in wood', 
Swedish gara, nisi, garr co\, gap in wood' Ablauts form to YPpoc, as " place for dancing, 
choir, band of dancers and singers ', is incredible. 

Doubtful, whether here Lithuanian zaras^xuu, flow, way, circle, turn ' (Wackernagel 
AIGr. 251); compare above gr. xop6(;; 

Hittite ^^/-/as "fortress' (Benveniste BSL. 33, 139)?; s. also gherd"^-. 

References: WP. I 603 f., WH. I 242 f., 660, 857. 
Page(s): 442-443 

Root / lemma: gher-5, ghor-na 
Meaning: bowels 



Material: Old Indie hira-hxx\. "band, strap', hira\. 'vein'; 

Latin haru-spex^ a soothsayer, diviner among the Etruscans, who foretold future events 
from the inspection of the entrails of victims ' actually " intestinal beholder', hTra^ jejunum, 
middle part of the small intestine', PI. " intestines, entrails ', hillae^ the smaller and anterior 
intestines of animals (other than men and sheep), a kind of sausage, smoked sausage ' (/' 
Sabine for e), hernia " medical condition in which an organ protrudes through an opening 
in its surrounding walls, break'; 

Note: 

Common Old Indie : Latin gh-> h-. 

gr. xop5n f. " intestine, catgut, gut string, string made from animal intestines, sausage '; 
dubious xopiov ' placenta, afterbirth, meal from milk and honey, skin, leather'; 

Old Icelandic ggrni., PI. garnar^ intestine ', PI. " intestines, entrails ' {*ghorna). Old 
English micgernu. " fat, lard, suet'. Old Saxon midgarni. Old High German mitti(la)-garni 
ds.; Old Icelandic garnu. "thread, string, lift (in weaving)'. Old English gearnAs., Middle 
Low German garn. Old High German ^5/77 "thread, string'; 

Lithuanian zarna, Akk. zarnq^ intestine, small intestine', Latvian zarnat " intestine ', PI. 
" intestines, entrails '. 

Note: 

Maybe alb. zorre {*ghorna) "bowel', PI. " intestines, entrails'. 

Albanian proves that Root / lemma: g''er-1, g''era-\^ to devour; throat ' derived from Root/ 

lemma: gher-5, ghor-na\ " bowels '. [common alb. gh-> z\ 

whether Armenian ya/" twiddled, twisted, rotated, revved, revolved ' belongs here, to 
modify meaning according to the root. 

References: WP. I 604, WH. I 635 f., 869, Trautmann 367. 
Page(s): 443 

Root / lemma: gher-6 [ghera- : ghre-1) 

Meaning: short, small
```


## [2026-09-06T02:15:37.168Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36700,36770p' POK_full.txt",
 "description": "Print Pokorny p.444 lemma"
}
```


### [2026-09-06T02:15:37.243Z] TOOL RESULT

```
Meaning: to encircle, enclose 

Note: because of Latin hortus{see gher-4) extension from *gher-4^ caich'; 



Material: A. ghe/ti'^-{here also about the original aniaut nothing conclusive about words of 

the centum languages): 

here also about ursprijngl. Initial sound nothing to determining words of the Kentum spoke 



Old Indie ^rz-^a- {*grdha-) 'house, dwelling', PI. " rooms', Avestan garada- m. " Hohle als 
Behausungdaevischer Wesen ' (an older meaning 'house, dwelling' could be proven 
through fiugr. loanword, as wotj. gurt^ residence, village', syrjan. gort^house, dwelling' and 
" underground dwelling, vault, sepulchre, grave',); 

alb. garth, gardhT hedge ' {*ghordhos, Jokl Slavia 13, 297ff.); 

Phrygian -gordum 'town, city' in Manegordum' MannfiR|t|rjt ' (besides Manezordum); 

gr. (by Hes.) Kop0i(; awpoc;, KopGsAai auarpocpoi, awpoi; 

Gothic bigafrdan' cincture ', Old \ce\av\6\c gyrda. Old English gyrdan. Old Frisian gerda. 
Old High German gurten6s.; Gothic gafrdai.. Old Icelandic gJgrd'beW., girdle', ablaut. Old 
Icelandic gyrdell. Old English gyrdel. Old Frisian gerdel. Old High German gurtil(a)6s. 
(Middle High German gurt\s nomen post-verbal); Gothic gardsm. "house'. Old Icelandic 
gardrm. 'fence, paddock, courtyard, homestead ', Old English geard. Old Saxon gard' 
enclosed, fenced property ', Plur. "dwelling'. Old High German gartvn. " circle ' in miWIgarf 
circle; territory, region; sphere ', heimgart' forum ' etc.; Gothic garda' hurdle, stockyard ', 
Old Frisian ^a/'o'a "garden'. Old Saxon gardo. Old High German garto6s. (or from Indo 
Germanic *ghor-t6-, compare xopTO<; under gher-4), 

Lithuanian gardasm. "corral, pen, fold', gard/st " gate, trellis, grate '; 

Slavic *gordb in Old Church Slavic gradb "castle, town, city, garden', russ.- Church 
Slavic ogradb "garden' (therefrom Old Church Slavic grazdb m. "stall'), russ. g6rod'\.a\NV\, 
city', Bulgarian gradb, Serbo-Croatian grad, sloven, gradds., Czech hrad' castle, palace ', 
poln. grdd6s.; zero grade Slavic zbrdb in Old Church Slavic zrbdb "wood', russ. zerdb 
"long, thin shaft, pole', poln. zerdz, sloven, zrd' point tree '; 

Tocharian B /re/r/ye" "palace' absents (Pedersen Tocharian Sprachg. 34f.); 

Hittite ^^/-/55 "fortress' (Benveniste BSL. 33, 139)?; s. also gher-4. 

about Latin urbs'town, city', ostensibly from *ghorA'"os, s. Georgiev IF. 56, 200. 

B. gherS^-: 



Phrygian -zordum'{o\NV\, city' (in Manezordum, see above); 

Lithuanian zardas " rack for the drying of grain or flax sowing, pinfold, place for housing 
stray animals, animal pound ', Latvian zards ' rack for drying, wooden layer, pyre ', with 
intonation change Lithuanian zardis^ horse garden ' m., Prussian sard/slence' (= ' 
unfenced horse garden '); 

russ. zorod^barn, haystack', weiftruss. azorod^ dry hurdle '. 

References: WP. I 608 f., WH. I 242 f., Trautmann 78 f., 366. 
Page(s): 444 

Root / lemma: gher-1 

Meaning: to yearn for 

Note: partly with forms from a basis *ghere(i)- : gheri- (see Persson Beitr. 728)
```


## [2026-09-06T02:15:44.224Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; echo ---; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | head -5; echo ---; grep -n \"603\" WLD_Bd1_pages.txt | head -20",
 "description": "Locate WLD Bd1 page 603"
}
```


### [2026-09-06T02:15:44.294Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
---
---
30214:mann KZ. 26, 603; Fick I 4 556, II 4 256, Yf. LEWb. 2 u. lupus, volpes, und
55836:mayors g, yradoc lies, (makedonisch nach Hirtldg. II 603, Hoffmann Mak. 52                                              ,
63081:   Lit. bei       Zupitza GG. 88; Falk-Torp 603, 1504.
63756:   Fick III 1 60, Falk-Torp 600, 603, 610, 1505, Brugmann IF. 6, 103. Zu-
65200:79, Miihlenbach-Endzelin I 603 f.    weitere Lit. bei Berneker 371), gnnilo
```


## [2026-09-06T02:15:45.193Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"zar\" CHEUNG.txt | grep -i -n \"harm\\|offend\\|angry\" | head -20",
 "description": "Grep Cheung for zar"
}
```


### [2026-09-06T02:15:45.252Z] TOOL RESULT

```
67:30266:*AVESTAN: zar- ‘to hurt, wound’ || (+ *2-) ‘to hurt, wound, offend’ = Liste: 67 f.
```


## [2026-09-06T02:15:49.084Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '30240,30330p' CHEUNG.txt",
 "description": "Read Cheung *zar entry"
}
```


### [2026-09-06T02:15:49.142Z] TOOL RESULT

```
*zap/f ? ‘to become quiet, still’ 

*KHOTANESE: ysah- ‘to become still, quiet’, OKh. yseh- (caus.) ‘to make quiet’ 
=> SGS: 112 

The etymology of Khot. ysah- is unknown. The previously assigned meaning ‘to 
cease’ and the suggested connection with the postulated Av. root zah- ‘to abandon’, 
cited in SGS: (and DKS: 348a) are to be discarded, in light of the recently 
discovered form ysotta (Suv. 2.66). The hapax form ysotta translates Skt. tusnibhüto 
“became still’, Skjzerve, l.c. On account of -h- in the present forms and -ott/-autt in 
the past the Khot. forms would go back to a root *zap/f which cannot be supported 
by any cognates though: expressive ? The Avestan forms quoted in DKS: l.c. can be 
interpreted differently: for YAv. frazahit (Y 60.7) see *zaH, and OAv. zaxiia- (Y 
53.8), cf. Insler, Gathas: 326. 


*PIE— => LIV: - | Pok.: 
*REFERENCES: Skjervo, SVK III: 129 f. 


*zarH2 469 


*zarH! ‘to hurt, wound, anger’ 


*AVESTAN: zar- ‘to hurt, wound’ || (+ *2-) ‘to hurt, wound, offend’ = Liste: 67 f. 
Pres. them. nä-: OPT. 1р1. OAv. zaranaéma (Y 28.9); Caus.: med. 3pl. YAv. äzäraiiente (Yt 13.30), OPT. 
25р. Y Av. azaraiioi$ (FrD 4); Partic.: pres. ania- med. YAv. zaranimna- (Yt 10.47), perf. med. ҮАУ. 
zazarana- (Y 9.30, Yt 11.5), perf. pass. zarata- (Yt 11.5) 

*MIDDLE PERSIAN: (+ *ā-) MMP "z'r-, BMP el /azar-/ (orig. caus.) ‘to torment, 
offend; hurt" > DMMPP: 85a 

Caus.: pres. IND. 3sg. MMP "z'ryd, ’z’ryd, BMP cht /azaréd/, SUBJ. 3sg. MMP "z'r'd, IMPV. 2sg. 
BMP ’c’! /azar/; Inf: BMP ’c’Itn /azardan/; Partic.: pres. MMP ’’z’r’g, perf. pass. BMP ’clt /azard/, BMP 
‘см /azurd/ 


*PARTHIAN: zr- ‘to become angry’ || (+ *a-) ’z’r-, ’’z’r- ‘to injure’ = DMMPP: 
384a, 85a 

Partic.: perf. pass. П zr'd || (+ *a-) Pres.: IND. 3sg. ’z’ryd, 2р1. ’z’ryd, SUBJ. 25р. "z'r'h; Partic.: perf. 
pass. *’’zyrd 

*KHOTANESE: ysurra- ‘wrath’ 

*SOGDIAN: (+ *4-) BSogd. "z'yr ’’z’rt ‘to hurt, trouble’, MSogd. "zyr ‘to offend, 
hurt’ || (+ *upa-) BSogd. ’pz’rn ‘to disturb, afflict (?)’ || (+ *pati-) CSogd. ptzyr- ‘to 
afflict, torment’, MSogd. ptzrn ‘anger’ 

(+ *a-) Caus.: pres. IND. 159. MSogd. "om (BBB: 32), 35р. BSogd. ’’z’yrt, impf. 1sg. MSogd. m’zyrw 
(BBB: 34); Pass.: pres. SUBJ. 3sg. MSogd. "zyry (Sogd.Tales: 469) || (+ *upa-) Pres.: SUBJ. 35р. 
BSogd. ’pz’rn’t || (+ *pati-) Pres.: IND. 35р. dur. CSogd. ptzyrtq, CSogd. “ptzrtq; Impf.: OPT. 3pl. 
CSogd. ptyzyr.nt 

*CHORESMIAN: (+ *à-) m/’zry- ‘to be offended, feel offended’, (caus.) m/’z’ry- ‘to 
offend’, ’z’ryk ‘harm’ || (+ *upa-) pz’r- ‘to blame, rebuke’. 0 Samadi derives the 
Chor. formation pz’r- from *pa-zara(1a)-, with prev. *pa-, whose existence in Ir. was 
already doubted by Henning 1965: 246, fn. 29. The preverb may be rather *pati-, in 
view of CSogd. ptzyr (Sims-Williams 1989: 262). = Samadi: 11, 166 

*NWIR: Bal. zar ‘anger’ (but Bal. zar ‘lament’ < NP хаг, *zaHr) || (+ *а-) NP 
azurdan/azar- ‘to torment, injure’, NP azar ‘affliction, disease, grieve, vexation, 
injury; [in compounds] tormenting, reproaching’ (LW), Bal. 4zurt/azar- ‘to hurt, 
annoy, vex, molest’ (< NP ?) 

*NEIR: Pash. zor- ‘to vez, distress; blame’ 

*SANSKRIT: har ‘to be angry’ (RV+) > EWAia II: 805 


© No precise IE cognates of this Пг. root are attested. 
*REFERENCES: EVP: 103; DKS: 354a; Werba 1997: 448; NEVP: 102; Shahbakhsh: s.v. azar- 


*zarH? ‘to age, grow old’ 

*AVESTAN: Y Av. zar- ‘to age, grow old’ = Liste: 68 

Partic.: pres. s- (+ priv.) YAv. azarosant- (Yt 19.11, Yt 19.19, Yt 19.23), YAv. azarsant- (Yt 19.89); 
Partic.: perf. pass. zarata- ‘old’ (V 3.13, P 22) 


*MIDDLE PERSIAN: MMP zrd ‘infirm (from old age)’ > DMMPP: 384a 


470 *zarH3 


*KHOTANESE: ysir- (ysad-) ‘to become old’ => SGS: 113
```


## [2026-09-06T02:15:50.345Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} END{print NR}' WLD_Bd1_pages.txt; grep -n \"gher-\\|ghordho\\|ghordo\" WLD_Bd1_pages.txt | head -20",
 "description": "WLD Bd1 structure"
}
```


### [2026-09-06T02:15:51.780Z] TOOL RESULT

```
894
10360:Wz.) hierher, sondern wohl zu glier- „hervorstechen“ oder gher- „starren“.
56202:granka „Biischel“ und aksl. grozrh. grozm „Traube“ s. unter *gher- „her-
57033:    1. gher-          ..begehren, gern liaben' , z. T. mit Formen von einer Basis *gherc(i)
57110:602                                                        gher-
57113:2. gher- ,,kratzen, ritzen, seharren".
57121:spitze", Wz. gher- ,,hervorstechen“, gehoren sollte. Immerhin konnte ghei -
57125:3.   gher- und ghere- ,.strahlen, glanzen, schimmern".
57128:freude blitzend" zu *gher- „begehren, gern haben" (s. d.), aber germ.
57210:4.    gher- „greifen,         fassen, umfassen, einfassenA
57267:s.   u. 6.   *gher- „kurz, klein“.
57270:villa s. Paul. Fest. 73 ThdP.), osk. lmrz „hortus, lucus“.    (Nicht zu *gher-
57342: 6.    gher- (ghere-?)              ,
57359: ^gher- ,,fassen :i gebucht.                i
57433:2. gher- „hart woriiber streichen, reiben“; vgl. auch die Erw. ghrei-, ghreu-,
57482:606                                                     gher-      — gerbh-
57487:. gher- „hervorstechen", von Pflanzentrieben oder -stacheln, Borsten,
57496:         s  d.). Scheidung von gher- ,.reiben‘' empfiehlt sich, da eine Bed.-
57508:,,starren“)  auch ydga^'t (s. unter gher- kratzen");
57730:        umgiirten“ und dann Erweiterung von *gher- ..fassen? s. d.
57922:         neben ghers- kein ghers- nachgewiesen ist). Yerwandtsch. m. gher-
```


## [2026-09-06T02:16:05.625Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '57180,57275p' WLD_Bd1_pages.txt",
 "description": "Print WLD Bd1 gher-4 article"
}
```


### [2026-09-06T02:16:05.685Z] TOOL RESULT

```
.,Sehkraft, Gesicht”'; aksl.                      zncalo, skr. dial, zrcalo, cech. 2 raic?fo„Spiegel“
(vgl.   Trautmann BslWb. 366).
     Wurzelerweiterung gher ei -
   Afr. as. ahd. mhd. grts „grau", nhd. greis ,.grau, alt", wozu wohl auch
aisl. grtss „Ferkel“, aschw. grts ds., schw. gris „Ferkel, Schwein””, dan.
gris ds. (Falk-Torp 348 f. und 1473 Lit.; der alteren Kombination mit ai.
ghrSvi „Eber   gr. yoigog tritt Hellquist SvEO. 202 bei s. aber auch Persson
                                                                           ;



      304 A., der yoigog auch zu unsrer Wurzel ghcr ,strahlen“ ziehen
 Beitr.
mochte, vgl. unter *ghers- „starren“).
      [ghereu-], ghrii-.
   In aisl. gryiandi „Morgenrote“, aschw. gry „(vom Tage) grauen, dammern ',                      1




dan. gry ds., gry n. „das Grauen ', aisl. qsgrua „das Aschgraue ‘, <C*qsy.ogrua
s. Bugge Norr. Skrift. af sagnhist. indhold 339); hierber auch aisl. grey n.

„Hiindin, Feigling      greyhundr „Windhund', ags. grighund ..Windhund ‘?
  Vgl. im allgem. Vanicek 98, Fick I 4 418, III 4 142 f., 144, Falk-Torp 338,
348, 354, Persson aaO., Trautmann Bsl.Wb. 366.


4.    gher- „greifen,         fassen, umfassen, einfassenA

     Ai. harati      ,
                                  nimmt“ (nicht aus bhar- s. Wackernagel
                         bringt, tragt, holt,
AiGr. I 248, 251), hdrana n. „das Bringen, Nehmen, Spenden usw., haras n.
,
  Nehmen, Ergreifen, Griff, Energie, Ungestiim, Kraft, Gewalt‘.
     (Av. sara -, asara - Bedruckung“, die Wackernagel I 248 zu liar- stellt,
                                  ,



belegt         Avesta Handbuch 148 nur durch Imdsara- V. 13, 45, was
             Justi
Bartholomae Ai.Wb. 1856 mit leicht beleidigt“ iibersetzt; es gehort ebenso
wie *asnrdta in anasarata nicht erziirnt ‘, das Uhlenbeck 357 zw. heran-
                                        ,.


zieht, zu ai. lignite, vgl. np. azard ,.gekrankt und azardcin „kranken-‘ siehe
                                                                   :




Hiibschmann Pers. Stud. 6, 146.)
     Tochar.    tsar,     sar ,.Hand    "
                                             ;
                                                 arm. jern   ds.   (Hiibschmann Arm. Gr. I 470);
alb. dors ds. (< *?jhera s. G. Meyer Alb.         Wb. 72, Alb. Stud. Ill 86), plur. kon-
sonant. duar         (< *gheres       s. Thumb DLZ. 1913, 805,  Jokl lingu. kulturhist.
Unters. 90 f.).
  Gr. yeiQ „Hand    dor. gen. yrjQos, aeol. acc. pi. x s 8Q a s (<
                             ‘,                                       nach
Wackernagel KZ. 29, 134, Verm. Beitr. 15? s. Bechtel Gr.Dial. I 38, II 315
und die bei Brugmann-Thumb Gr. Gr. 141, 148,209 genannte Literatur),
evyegij? „leicht zu handhaben, leicht, leichtsinnig ", dvayegg? ,,schwer zu
handhaben, schwierig“, yogtos eingehegter Platz, Hof, Weideplatz ‘, hier-
                                                 ,


her auch yogos (nach Curtius 199) „Tanzplatz, Chortanz‘‘ als urspriinglich
..eingehegter Platz“ oder nach Froehde BB. 10, 301 als .,Reihenfolge,
Ordnung“ zu lit. zdras ,.Lauf, Weg, Runde, Wendung“ ? Vgl. Boisacq 1067,
Vf. LEWb. 2 311. Ganz zweifelhaft trotz Boisacq s. v. yooiov ,,Nachgeburt,
aus Milch und Honig bereitete Speise, Haut, Leder‘\        Kaum zutreffend     —
stellt endlich auch Brugmann IF. 37, 239 (im AnschluB an Curtius 199)
her ygfjodai „gebrauchen, benutzen“, yggya „Sache, die man gebraucht'
       :
                                                                                              -

                                                                                                  ,


ygrj ,,es ist notig  yged) „Bediirfnis, Bedarf ', ygecog, ygrjog „Bediirfnis,
Verlangen, Schuld*; wahrscheinlicher ist die Verbindung mit yeigwv usw>
s.   u. 6.   *gher- „kurz, klein“.
   Osk. heriiad „capiat“, herrins „ceperint“, lat. cohors „Hofraum, Gehege,
Viehhof, Haufe, Menge, Schar, Gefolge“, hortus „Garten‘-' (im Altlatein                      =
villa s. Paul. Fest. 73 ThdP.), osk. lmrz „hortus, lucus“.    (Nicht zu *gher-
gehort litres s. u. *ghei; zweifelhaft ist lat. hlr, fr ,/Mvag, vola“ s. Solm-
sen    KZ. 34, 3, vgl. Vf. LEWb. 2 366).
  Ir. gort „seges“, cymr. garth „Pferch, Hiirde, Gehege“, bret. gars ,,Hecke.

Zaun“ (s. Pedersen KGr. I 136, 180), dazu ir. lubgort .,Garten“, acymr. plur
```


## [2026-09-06T02:16:28.081Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf 27 (p.6) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==28' HRN.txt; echo; echo \"=== HUB leaf 16 (p.6) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==17' HUB.txt",
 "description": "Print Horn p.6 and Hübschmann p.6"
}
```


### [2026-09-06T02:16:29.650Z] TOOL RESULT

```
=== HRN leaf 27 (p.6) ===
6 -
phlv. evar (vd. 5 (146) Gl., Men.), päz. äwar^),
evarih (vd. 5 (146) Gl.). (Darmesteter, Et. ir. I, 251).
phlv. evar führe ich auf ap. *adi -+- [/'var- zurück;
adi (ai. adlii) kommt auch noch in estäden (und
vielleicht in evän, evar (^INZ^N Jer. 5, 6) vor (vergl.
KZ. 32, 581).
17. ärey 'Hass, Feindschaft*, rey,
ap. araika- Teind'; aw. ara^ka-.
Statt ärey ist vielleicht erey zu verbessern (dann
wäre rey die lautgesetzliche Form); die altpersische
Form könnte andernfalls natürlich auch äraika- gelesen
werden.
18. äz 'Begierde' (z. B. Vis und RämTn, Seite 47 Vers 14),
ahmend, azver {äzür),
aw. asi- 'Gier ; phlv. äs, äzmand, äzvar,
19. äzäd *frei', äzöde.
.^^x^^ aw. äzäta- *frei, edel*; phlv. azät, arm. LW. azat,
azatak, vergl. atarrj tXsv&soia sc. napd Ils()(T(ag (Hes.).
kurd. aza *brav, tapfer* (Houtum-Schindler).
20. äzär Xeid*, azärden^ azdris; äzerden^ äzerm^).
aw. a + [/'zar-j azärayeiMi sie peinigen' ; phlv. äzär,
äzartan etc.; ai. [/har- 'zürnen.
21. äzmUden 'erproben, versuchen', Praes. äzwäy-em,
äzmä, äzmäyis\ li'^NQilN (Is. 7, 12).
phlv. özmütan, özmay(i)sn es ist zu versuchen' (vd. 5
(146) GL), 'Versuch' (Men. 60, 14, K 43).
bei. äzmäyag (LW.), n. äzmainay (23).
aw. *a (oder nach dem Pehlevi wohl ava) + uz +
i/'mä'.
^) Np. aver *wahr, Wahrheit*, äverl brauchen nur Pazendworte
zu sein; doch bin ich über Sahn. I, 35 Vers 19 noch nicht im Klaren
{reftäwerl wäre eine sehr bedenkliche Bildung). Etwa: *"Wir müssen als
Köche zum Sah gehen — fürwahr! und dann ein Mittel ersinnen etc. ?
*) Im Pehlevi auch schon in der kaum hierher gehörenden Be-
deutung *Ehre, Achtung* (GF.), anäzarm (Men.), vergl. Vis und Kämln,
Seite 32 Vers 12, 86 Vers 3 v. u.

=== HUB leaf 16 (p.6) ===
— 6 ~
im 2. Gliede mit zd. avo-x^arena- = phi. apx^ar^)
(so, nicht avx^ar ist zunachst zu lesen!) deckt.
Zd. avdx^arena- miisste im Neupersischen den Laut-
gesetzen nach durch *dx^arr = *dxur vertreten sein.
9. Ap. A^Hna- kann nicht sicher als persisch gelten, da
der Mann ein Susier war, wie die Inschriften zweiter
Art ausdriicklich sagen.
14. Kurzes a im Aniaut hatte abfallen miissen, also wird
dran u. s. w. die Vichtigere' Form sein, vgl. die kas.
Dialectformen orinj u. s. w.
16. Ich wiirde np. art fiir contrahirt aus aoari (vgl. arad
aus avarad *bringt* halten), wenn das Wort nicht are
lautete, wie mir No Id eke aus Reimen (mit bar-e, mar-e
etc.) nachweist, vgl. kas. orE^ are,
Ueber das Vorkommen von np. avar certitudo',
avan 'flde dignus' vgl. Mann, ZDM6. 47, 701. Ist fur
phi. paz. evar 'certain , evarth 'certainty', evarik certain
(Shk. p. 243 etc.) avar u. s. w. zu lesen? An e = adhi
(das weder im Zd. noch im Ap. vorkommt) glaube ich
nicht.
17. Ist unsicher, da im Ap. ebensogut arika *feindlich* (zu
skr. ari' Teind*) gelesen werden kann, das im Np. zu
*rig geworden ware. Aw. ara^ka, Beiwort der Ameise,
ist dunkel. Die Form rey belegt Vullers aus Firdusi.
20. Fiige hinzu: np. dzard-a = zd. azareta- *beleidigt\
Sal. Shuk. geben freilich azurdan *kranken fiir
Vullers' Ozardan. Dazu stimmt afgh. LW. azurda
afflicted, sad*.
24. Zd. dstdrayettti ist mit Darmesteter, Le Zend-
Avesta II, p. 66, Anm. 7 durch *sundig, schuldig machen'
zu ubersetzen und als Denom. von *a8tara- = parsi
astar *Sunde' zu fassen; es geh5rt zu zd. anastareta--
ohne Schuld, ohne Siinde'. Ap. ma starava wird von
*) ^gl- jfid. tat. ovxur *Krippe* (Miller p. 75; «u qv 'Wasser'
= np. CUb.
```


## [2026-09-06T02:18:00.362Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD pz'rn ===\"; grep -n \"pz.rn\\|pz’rn\\|pz'rn\" SOD_pages.txt | head -10; echo \"=== SOD entry 55 area ===\"; grep -n \"^ *55 \\|^55 \" SOD_pages.txt | head",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-06T02:18:00.435Z] TOOL RESULT

```
=== SOD pz'rn ===
7803:1398 >py>stk B                                                             (o)pzarn =>ptzrn, pzrn
7808:                                                                      1411 'pz'rn-        B, S                   jj^ JL. O-^^ljl;
7809:1399 'py'sty => }py>stk                                                    (o)pzarn       Opzrn-)    ©Av. zar-
7829:                                                                      1414 >pzrn- =¥ 'pz'rn-
27206:     pu-apzarn                                                       pu-awaze ?
27919:      pazarn =>ptzrn, 'pz'rn                                             TSP 6.164; r'fitf "illness" MDii pl25.1
=== SOD entry 55 area ===
4013: 55 »8wr»yk     S(C)
```


## [2026-09-06T02:18:01.866Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hrnite\\|hrniite\\|hrnfte\\|hrn.te\" POK_full.txt | head -20; echo \"=== gher- yearn p440 ===\"; sed -n '36765,36830p' POK_full.txt",
 "description": "Pokorny gher-1 yearn and hrnite"
}
```


### [2026-09-06T02:18:01.944Z] TOOL RESULT

```
=== gher- yearn p440 ===

Root / lemma: gher-1 

Meaning: to yearn for 

Note: partly with forms from a basis *ghere(i)- : gheri- (see Persson Beitr. 728) 

Material: Old Indie /75/y5//"finds pleasure, desires'; Avestan zara- m. ' striving, purpose '; 

Oscan herest {^or * heriest}, Umbrian heriesV volet ', heris-heris^ conj. and adv. prop., 
will, choose, take your choice, hence, as disjunctive conjunction, to introduce an 
alternative as a matter of choice or preference, or as not affecting the principal assertion, 
either ... or, be it ... or, in general but where the alternatives are necessary and exclusive, 
that is, where one must be right and the other wrong ', Oscan heriam " a judgment, 
decision of an arbitrator, mastery, dominion, authority, power, will, free-will, choice, 
pleasure, denoting or containing power ', Herentatefs^ Veneris ', pralign. Herentas, sabin. 
hiretum^ a decree, decision, ordinance, vote, resolution, principle, doctrine, dogma '; Latin 
horior, -TrV actuate, encourage', horitor, syncopated hortor, -ands. 

Note: 

Common Old Indie : Latin gh-> h-. 

gr. xaipco (*xapi-iJi)), xapnvai " be pleased', xciP'<^f- pleasantness, agreeableness, 
favour ', xapa 'pleasure, joy', xc(pon6(; " glowing joy of battle ', xaPMCi n. 'pleasure, joy, 
pleasure'; also xaPMH "fight, struggle', originally ' joy of battle, lust of battle '? xapToq 
'joyful, gratifying' (?); after Pedersen 5® decl. Latin 73 here XPH etc. S. under ^^er-^ here 
after Leumann Homer. Worter 318''09f also 5uax£pn<; ' unfriendly, unpleasant', suxspHc; ' 
unworried, undisturbed, light' (previously later in x£ip 'hand' attribute); 

Old Irish ^c»/-'godly, pious', goire^ devoutness, piety'; Middle Irish do-gar^ unlucky ', so- 
gar'very lucky' (: gr. xapa); cymr. dyar^ sad ', /T/aA'pleasant' (I. Williams RC 40, 487); 



Maybe alb. gjore^ poor, wretched ' 

Old High German ger^ yearning', gerdn^\\}s\., crave'. Old High German ging. Old Saxon 
gerag^ greedy '; Gothic fafhu-gafrns^ avaricious, greedy'. Old Icelandic gjarn. Old English 
^eo/77 'wherefore willing, inclined, whereupon eager, avid'. Old High German Old Saxon 
gern^ eager, avid, eager after something'. Adv. Old High German gerno. Modern High 
German gern, Denom. Gothic gafrnjan. Old Icelandic girna. Old English giernan. Old 
Saxon g/rnean'\ust, crave'. 

Perhaps here as d^-formation from the basis gh(e)re-. Gothic ^/leo'i/s "hunger', gredags " 
hungry'. Old Icelandic ^rad/^ gradixx\. 'greed, lust, hunger'. Old English gnged^qxee(i, lust'. 
Modern High German y/a/ "hunger' (Berlin), Old English graedig. Old High German gratag^ 
greedy '. In addition as '(g/7/'ed^'- Germanic *grada-^ eager, avid, rutting, in heat' in Old 
Icelandic gradr^ not castrated ', gradungr^buWl In Middle High German gntm. " 
eagerness ', gntec' eager, avid'. Old Icelandic ^/"A^f. 'vehemency', gr/djungrm. "bull' ein 
ablaut. Indo Germanic *gh[e]rei-6^- or *gh[e]rM^- to search, could be possible. 

Middle Irish gradu. "love' is from Latin gratum facere alicuiav\6 similar change of 
direction or position borrowed (o'instead of th aiter grad^ step; position '). 

References: WP. I 600 f., WH. I 657 f. 
Page(s): 440-441 

Root / lemma: gher-2 
Meaning: to scratch, scrape 

Material: Gr. xapaSpa " Erdrift, crevice, gorge, ravine, gulch '; xapaaau), Attic -ttoj "whet, 
sharpen, notch, incise', xapa^. -OKoq "picket, pole, vine-prop, pole, pale, used in fortifying 
the entrenchments of a camp, cutting, slip, esp. of an olive, a seafish, one of the breams, 
Sargus', xapoKinp "engraver, one who mints coins', then "mark engraved, impress, stamp 
on coins and seals, distinctive mark or token impressed (as it were) on a person or thing,
```


## [2026-09-06T02:18:18.252Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN 1966 chronic ===\"; grep -n \"chron-ic\\|^chronic\\|chronic, adj\" KLN_1966.txt | head -10; echo \"--- 1971 ---\"; grep -n \"^chronic\\b\\|chronos\" KLN_1971.txt | head -10",
 "description": "Grep Klein for chronic"
}
```


### [2026-09-06T02:18:18.375Z] TOOL RESULT

```
=== KLN 1966 chronic ===
--- 1971 ---
45497:chronic, and the second element in Dashahara 
46535:chronic, adj., 1) lasting a long time; 2) habitual. 
46592:chronoscope, n., an instrument for measuring mi- 
46597:Derivatives: chronoscop-y y n., chronoscop-ic y 
60287:chronic. 
117324:chronic mercurial poisoning (med.) — Medical
```


## [2026-09-06T02:18:18.900Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== TAD leaf for p.56 ===\"; grep -n \"قرن\" TAD_pages.txt | head -20",
 "description": "Grep TAD for qarn"
}
```


### [2026-09-06T02:18:18.958Z] TOOL RESULT

```
=== TAD leaf for p.56 ===
2153:              ‫معناه قرن صغير ويطلق على حلي الأذن‬       ‫وناني ههه‬       ‫قرط‬
2328:‫اليوناني ومعناه قرن صغير ويطلق على قرن‬             ‫دوعا‬     ‫ل‬          ‫قراط‬
2400:‫كرنيتة ‪7‬س ايطالى هااءد‪.‬ده معناه قرن صغير وهو بوق تحيف ينفخ فيْه‬
2424:‫فاتدير سموا به وحيد القرن على سبيل المشاعبة أدذمهها ‪:50‬عتاوهاء فراسوه‬
2425:‫وعر وه كروكدحنأييد القرن الهنديويوز أنيكون الاسمفينيقي« قرنإحد»‬
2426:                                                        ‫أي وحيد القرن‬
2601: ‫حكاء ‪ .‬وقال أحد الملماء ان انظ مجوس منذ القرن‬           ‫أسباط مادي ‪0‬‬
2648:                   ‫‪ 50261000012‬معناه وحيد القرن وهو الىكدن‬                                  ‫نسا‪-‬نى‬
2976:‫الهجائية التّى اخترعها الفينيقيون فاىلقرن الخامس عشر قبل الميلاد وجمعت مهذه‬
```


## [2026-09-06T02:18:26.738Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '46530,46560p' KLN_1971.txt; echo \"=== 1966 khronos ===\"; grep -n \"khronos\" KLN_1966.txt | head -20",
 "description": "Read Klein chronic entries"
}
```


### [2026-09-06T02:18:26.825Z] TOOL RESULT

```
an electric current (physiol.) — F. chronaxie , 
coined by the French physiologist Louis La- 
picque (1866-1952) in 1909 fr. Gk. XP^ 0 ^ 
‘time’, and ‘worth, value’, which is rel. to 
££tos;, ‘worthy’. See chrono- and axiom, 
chronic, adj., 1) lasting a long time; 2) habitual. 

— F. chronique , fr. L. chronicus, fr. Gk. ypo- 

‘pertaining to time’, fr. xP^voc;, ‘time*, 
which prob. stands for *ghr-on-os and derives 
fr. I.-E. base *gher- y ‘to seize, take, hold, close, 
envelop*, whence also Gk. xs^P* ‘hand’; see 
chiro-. Time is regarded as ‘that which embraces 
all things’. See Hofmann, EWG., p. 424 s.v. 
Xp6vog. Cp. chronicle, crony, and the second 
element in isochronous, anachronism, metachro- 
nism, parachronism. 

Derivatives: chronic-al-ly, adv., chronic-i-ty y n., 
chronicle (q.v.), chron-ist y n. 
chronicle, n. — ME. cronicle , fr. cronique, cro- 
nike , fr. OF. cronique (F. chronique ), fr. L. chro- 
nica, neut. pi. mistaken for a fem. sing., fr. Gk. 
xa xpovixa., neut. pi. of xp ov ^?» ‘pertaining 
to time’, fr. xp6vo<;, ‘time’. See prec. word. 
Derivative: chronicl-er, n. 
chrono-, before a vowel chron-, combining form 
meaning ‘time*. — Gk. xpovo-, xpov-, fr* XP^ V °S» 
‘time*. See chronic. 

=== 1966 khronos ===
```


## [2026-09-06T02:18:33.969Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\"",
 "description": "TAD offsets"
}
```


### [2026-09-06T02:18:35.683Z] TOOL RESULT

```
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
```


## [2026-09-06T02:18:40.647Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 59 60 61 62; do echo \"===== leaf $n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' TAD_pages.txt | head -60; done",
 "description": "Print TAD leaves near p.56"
}
```


### [2026-09-06T02:18:42.302Z] TOOL RESULT

```
===== leaf 59 =====
                                      ‫سد‬    ‫اهم‬



                                           ‫‪2‬ك » وهو الحجل‬
                                                        ‫قب ‪ .-‬فارسي ك‬
     ‫معنأه حماس و ‪ 110 862‬ألاتزلاه‬   ‫قرس ل أخوة النحاسى ‏ لانيني امن‬

                                                                 ‫رسسي‬
                                                                    ‫بحا‬
                                                                      ‫أقين‬
                        ‫بعر يب ‪50]0/5‬ألء وهو اسممصر ف اليونانية‬
                                                              ‫قبط ت‬

 ‫ايطالي مطةالمةن معناه فى الاصل رئيس مرادقه ناك السفينة‬            ‫قبطان ف‬

                                            ‫وفائد الجيش وعميد القوم وعمدة وكش‬
     ‫قدوم ‪ -‬عبراني « كردُوم » تأدغت الراء بالدال فصار « قدوم » وهو‬
                                                   ‫مجر النجار وم‪:‬ته‬
      ‫وهو وع سن الهوخ كرة شه حب‬               ‫بوناني ‪8‬‬       ‫قراسيأ وقراصا‬

‫‪١‬‏‬                                         ‫االعلنباسود الا ان فىلبه عجمة واحدة‬
                       ‫قراغول ‪ -‬ترك « فراغول » معناهرييئةوطليعة وخفير‬
                                    ‫قرداحي ‪ -‬أرامي « قرداحا » وهو الحداد‬
                                                         ‫فرش س راجع غرش‬
                 ‫قرصان | ‪.‬يطالمي ‪ ©1350‬معئاه غازون وبراد به لصوص البحر‬

             ‫قرطاس ‏ وناني همارك معناه ما جرسم به مرادفه ورقة وصحيفة‬

              ‫معناه قرن صغير ويطلق على حلي الأذن‬       ‫وناني ههه‬       ‫قرط‬

         ‫قرطل ‪ 55‬أرامي د ترطلا» أي ‪ 71‬من قصب منقول مناليوناني ‪1‬‬

‫ثى الارمنية تتصعدى وى اللاتينية ‪5‬نم‪ *»:‬ومعنأه دودة وبي‬                ‫رمز‬

===== leaf 60 =====
                                        ‫ده‬     ‫ااه‬



‫اراق « كرميل »عد الإل الال وهو تدناظري 'تحوت دينكم أي |‬
‫دودة ول أي حراء وهزاكوقة عراء كرن ف ‪:‬ضوف اقاء مو نف ابيقة ‪1‬‬
‫اوتستعها وهو نوسود ف نينا ‪١١‬‏‬
                            ‫ويقع على ورق شجرة بلوط القرمز وعلى أنه ) ب‬
  ‫والهند والككيك وسائرالبلدان الحارةفيجمعفىحينهويصبغ به ولونه أحر قانر‬
                                   ‫فنقل قرمر منالعر ببة الى لغات اوريا بلفظ و‪6‬ممه؟‪1‬‬

                                            ‫قرقة © ‪ --‬تركي( غورق عريهارنقاء‬
    ‫قرميبدد ‪ -‬بوناني ‪5112:2, 8‬نع‪ 21‬معناه تراب محروق أي طهيشنوي” وهو‬
                                                               ‫الخزف والفخار والاجر‬
   ‫وزاك الذئ بال حل عالقا ستول سن انوناق وموم عرو اينرنيتاة‬
    ‫عندمم زمانووقت ومدة وستون و دكأبظا على الهالزمان مرادفه دهر أي مأئة سنة‬
   ‫قترفل ‪ -‬فى اليونانية مله رخفا وهو شجر قروئه أفضل الافاويه‬
   ‫وبطلق أيضاعلىنبات بستاني زغوه علتن الاقامتفاء وان مداوكه وقد‬
                                                               ‫ينجبتز فاىئر الانطيل‬
                                             ‫قن وخر" ‪ -‬لفظ فارسي براد بهالخرير‬

   ‫قس وقِسّهس ‪ -‬أرامي « قشيشا » معناه شيخ وقديم وقد يلقب به الكامن‬
                                                                          ‫عيدنا ازاما‬
                       ‫قشطة”” ‪ -‬عامي وهو مصكف قثدة أي الزبدة الرقيقة‬
                                        ‫ا‬    ‫قشلة ‪ -‬ترك » قشلاق ‪ 6‬معناه مسُتى‬

    ‫قصبار ‏ من اليوناني هفهطادءا أي طهر ونظاف وكازر فى الفارسية معناه‬
                                                                       ‫لض ‪:‬لوفان‬
           ‫‏(‪ )١‬الساحه ز او الفرخه ) اذا عدة علل بيضبا أخذ ووه من قرت الدحادة اى صونت‬
    ‫والصواب الؤشدة “وااةشادة‬   ‫‪ 50‬اللى الرا؛ب‬
                                            ‫في أيالةشاو ‪#‬منالسءن اطفو علي وحه الحأيت‬

===== leaf 61 =====
                                  ‫سالاع سد‬


 ‫اللانني شمعئاه حصن وقلعة‬        ‫‏‪ ٠‬عرني محض وهو الصرح أما مق‬

              ‫ومنه البلاط أي قصر الملك‬        ‫‪"3 00‬قِالأديية ا‬
                                                             ‫والقهعر‬

                     ‫قصدر ‪ -‬ونالى وم‪2‬ه‪1‬أ‪:55‬؟‪ 1‬وهو ممدن لين يطلى به‬
                                                                ‫ل‬
                       ‫ونه ‪ -‬فايليونانية ‪ 50421101‬معناه زنبيل من خلاف‬

 ‫غلاف اللكحلة ‏ فارسي مركب ون كف أي كلل ؤذا نوعو‬               ‫تدان ‪-‬‬

                                             ‫صيغة ظرف المكان تلصق بالاسياء‬
‫قفص ‪ -‬عرنيمحض وقفسالفارسي التركي مأخوذ منقفصالعربي و دومه)!‬
  ‫ميةدوع اللاتينية معناها عليةوخْرّانة مخنشب أما االقلفصيوفنانية‬
                                                               ‫هونان‬
                                                                   ‫الي‬
                                          ‫فبلفظ «ماءموه‪ 2‬وافلىلانينى وعحدء‬

                                      ‫ترى « قفتان » وهوالقاء‬    ‫قفطان ‪-‬‬


            ‫رولها؟‪ 1‬معناه متاح‬      ‫إقليد واكليل ومعلاد و ناني‪5‬‬

                                        ‫‪ - 3‬في اللاثينية ‪ 518‬معناه حياس‬

                                                  ‫اتلس انحظتركليس‬
 ‫قلقاس ‪ .-‬ووناني ‪ 5019850‬معناه مستدير ويطلق عندثم على اللفتعلى انه‬
                                                                    ‫مستدبر‬


                                   ‫قله في اليونائية ‪5022‬داة؟آ ممناه قصة‬

‫الارضية مرادفه دقع‬      ‫براد به منطقة م ن مناطق الك‬    ‫‪0‬‬         ‫اع‬

                                                               ‫وبتعة وفعي‬
   ‫‪3‬‬                                              ‫‪00‬‬
 ‫همععناه فى الاصل غطاء راس‬          ‫فلنسوة وقلسوة وقاوسهة ‪ -‬وناني ‪2‬‬

  ‫‪02‬‬        ‫بكري به زكروسهم مشتمًا من ‪1‬‬‫رأَةوهوالنصيفيغطيٍ‬
                                                        ‫الى‬

                                                           ‫ل !اس أي عا‬

===== leaf 62 =====
                                                       ‫لوش ‪ -‬اطلب كالوش‬
                          ‫كظورنت‬
                               ‫قس وقومس ‪ -‬أمير ورجل شريف ‪ -‬ان‬
 ‫قاش ‪ -‬في الفارسية ك«ش » معناه نسيج من قطن شن ثمنقل قاش الى‬
                                                            ‫الفارسية بلفظة فاش‬
      ‫ترك « قامش ‪ 6‬معناه قضيب وقصب و ( فجي » معناه سوط‬                     ‫‪2‬‬

 ‫وفي اللغة‬             ‫في الايطالية *‪01‬مهه وفي اللاتينية الركيكة‬       ‫فض‬
‫كا فعي منقولة من اللاتمنية الى العربية والى السسربانية ايضا‬        ‫اللعزنطية ‪805‬‬

                                                                   ‫‪6 05 2‬‬
                                                                           ‫َ ‪2‬‬
                             ‫قمهم‪ --‬فارسي «‪ ) 5‬وعرببه يعدروم‬
                    ‫معناه ‪1‬ون وموقد‬       ‫وق الخجام ب بوناني ‪5‬‬             ‫ثين‬

‫وفي اللاتينية دتاتاء معناه أعلىكل شيء مرادفه‬       ‫شه وهامة ‪ -‬بوناني ‪51‬‬
                                                                      ‫وك‬         ‫‪010‬‬

                                                            ‫قله وقلة وشعدفة‬
                                                                           ‫‪9‬‬

‫شريمتفازنى و كد ب و©أصل هذا النبات من بلاد الهند وفارس فتقل‬
             ‫الى اليونانية ونطهدسهة ومنها إلى الابطالية ‪#‬مقصد وسائر لغات اوربا‬
       ‫قكرذةف من المدفم مرادفهاقذيفة‬
                                   ‫قنبلةبتري « قومباره » وتهي‬
                                 ‫«ند» قرفن الب‬
                                             ‫ند ‪ -‬فارسي ك‬
 ‫فارسي «كندسك ‪ 6‬معنأه خصية الكاب وغو‬               ‫ا‬     ‫وفلدز دن‬          ‫‪5‬‬

                                          ‫كلب الماء وخصيته يقال لها جندييدستر‬
‫قندسة وكتدجة ‪ -‬فارسي «وكنده » وهوخشبة يستعملها البثساؤنفي‬
                                                                   ‫بنيان القناطر‬
```


## [2026-09-06T02:18:54.297Z] TOOL CALL #24: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py TAD:56 --image 2>&1 | tail -40",
 "description": "Render TAD page 56"
}
```


### [2026-09-06T02:18:56.279Z] TOOL RESULT

```
no scan of TAD covers printed page 56 (see 'scans' in refs_online.json)
```


## [2026-09-06T02:19:01.569Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"مائة سنة\\|مأئة سنة\\|دهر\" TAD.txt | head; echo ---; grep -n \"دهر\" TAD_pages.txt | head",
 "description": "Grep TAD for the qarn line"
}
```


### [2026-09-06T02:19:01.637Z] TOOL RESULT

```
135:|اكتشفه الفينيقيون في الدهر 2" الحامس عشر قبل المسيح فصيموا بدمه الاثواب 
167:)0( سى بالدهر مأئة سئة 
1865:)١(‏ قل التعالى في كتابه يتيمة الدهر لايقال مائدة الا اذاكان عليها طهاموالا فبى خوان. 
2295:عندمم زمانووقت ومدة وستون و دكأبظا على الهالزمان مرادفه دهر أي مأئة سنة 
---
169: ‫|اكتشفه الفينيقيون فيالدهر‪ "2‬الحامس عشرقبل المسيح فصيموا بدمه الاثواب‬
189:                                               ‫)‪ (0‬سى بالدهر مأئة سئة‬
1779:‫‏(‪ )١‬قل التعالى كفتيابه يتيمة الدهرلايقال مائدة الا اذاكاعنليهاطهاموالا فبى خوان‪.‬‬
2173:    ‫عندمم زمانووقت ومدة وستون و دكأبظا على الهالزمان مرادفه دهر أي مأئة سنة‬
```


## [2026-09-06T02:19:23.295Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2290,2300p' TAD.txt",
 "description": "Context of TAD qarn entry"
}
```


### [2026-09-06T02:19:23.339Z] TOOL RESULT

```
قرميد بد - بوناني 8 ,2:2115نع12 معناه تراب محروق أي طين هشوي” وهو 
الخزف والفخار والاجر 

وزاك الذئ بال حل عالقا ستول سن انوناق وموم عرو اين رنيتاة 
عندمم زمانووقت ومدة وستون و دكأبظا على الهالزمان مرادفه دهر أي مأئة سنة 

قر تفل - فى اليونانية مله رخفا وهو شجر قروئه أفضل الافاويه 
وبطلق أيضا على نبات بستاني زغوه علتن ال اقامتفاء وان مداو كه وقد 
ينبت فى جزائر الانطيل
```


## [2026-09-06T02:19:35.579Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T02:19:35.585Z] TOOL RESULT

```


```


## [2026-09-06T02:19:38.410Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; curl -s -o tad60.jpg -w \"%{http_code} %{size_download}\\n\" \"https://archive.org/download/TOB1932ARAR/page/n59_medium.jpg\"",
 "description": "Try fetching TAD page image"
}
```


### [2026-09-06T02:19:40.367Z] TOOL RESULT

```
302 0
```


## [2026-09-06T02:19:46.555Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%B1%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology section for آزردن (āzordan/āzurdan): Middle Persian form, Proto-Iranian root, any Proto-Indo-European root cited, and cognates (Avestan, Sanskrit)."
}
```


## [2026-09-06T02:19:49.432Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%87%CF%81%CF%8C%CE%BD%CE%BF%CF%82",
 "prompt": "Give the Ancient Greek etymology section for χρόνος (khrónos) verbatim: what origin is proposed, what does Beekes say, is it connected to *ǵʰer- 'to grasp/enclose'?"
}
```


### [2026-09-06T02:19:51.611Z] TOOL RESULT

```
# Persian Etymology for آزردن (āzordan)

Based on the Wiktionary entry provided, here is the available etymological information:

**Middle Persian Origin:**
The word derives from Middle Persian āzardan, āzārdan, or āzār, meaning "torment" or "injure."

**Related Form:**
The entry references آزار (âzâr), which means "trouble," indicating a semantic connection within the Persian lexical family.

**Source Documentation:**
The etymology cites D. N. MacKenzie's "A concise Pahlavi dictionary" (1971), specifically page 15, as the scholarly reference for this Middle Persian reconstruction.

**Limitation:**
The provided Wiktionary entry does not include information about Proto-Iranian roots, Proto-Indo-European origins, Avestan cognates, or Sanskrit cognates. Those etymological layers would require consulting more comprehensive historical linguistic resources beyond what appears on this particular dictionary page.
```


### [2026-09-06T02:19:55.701Z] TOOL RESULT

```
# Ancient Greek Etymology of χρόνος

**Origin Status:** The word has an unknown origin.

**Proposed Connection:** A derivation from Proto-Indo-European *\*gʰr-ono-*, stemming from *[\*ǵʰer-](/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0er- "Reconstruction:Proto-Indo-European/ǵʰer-")* ("to seize, enclose") has been suggested, carrying the original sense of "encompassing time-limit."

**Beekes Reference:** The etymology derives from Beekes, Robert S. P. (2010), "χρόνος", in *Etymological Dictionary of Greek* (Leiden Indo-European Etymological Dictionary Series; 10), Brill publishers, page 1651.

**Alternative Theory:** Other theories connect the word to *κορμός* (kormós) from Proto-Indo-European *[\*(s)ker-](/wiki/Reconstruction:Proto-Indo-European/\(s\)ker- "Reconstruction:Proto-Indo-European/(s)ker-")* meaning "to cut off."
```


## [2026-09-06T02:20:02.734Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%87%CE%BF%CF%81%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek etymology of χορός (khorós) verbatim: what PIE root is proposed, what does Beekes say about it, and is the 'enclosure' connection accepted?"
}
```


## [2026-09-06T02:20:04.457Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%86",
 "prompt": "For the ARABIC entry قرن (qarn): give the etymology, the Semitic root, the meanings including 'century/generation', and any cognates (Hebrew, Aramaic, Akkadian). Is any Greek origin mentioned?"
}
```


### [2026-09-06T02:20:13.379Z] TOOL RESULT

```
# Arabic قرن (qarn) - Etymology and Meaning

## Etymology
The word derives from Proto-Semitic *ḳarn- ("horn"). The root connects to meanings of "being doubled, opposed, or equal," with "century" potentially derived through "equal in age, people of the same age." 

The entry notes: "Otherwise, it could have been borrowed from Ancient Greek χρόνος (khrónos, 'time', also 'lifespan')."

## Meanings
1. Horn
2. Century

## Semitic Root
The root is listed as **ق ر ن** (q r n), encompassing 12 Arabic terms.

## Cognates and Other Languages
The Wiktionary entry documents descendants and related forms across multiple languages—Egyptian Arabic, Gulf Arabic, Hijazi Arabic, Maltese, Persian, Fula, Hausa, Hindustani, Indonesian, Malay, Ottoman Turkish, and Swahili—but **does not provide cognates in Hebrew, Aramaic, or Akkadian**.

## Greek Connection
Yes, a potential Greek origin is mentioned as an alternative etymology, suggesting borrowing from Ancient Greek rather than purely Semitic derivation.
```


### [2026-09-06T02:21:16.585Z] TOOL RESULT

```
# Ancient Greek Etymology of χορός

**PIE Root:** The proposed root is *\*ǵʰer-*, though its semantic identity "has been disputed."

**Beekes's Analysis:** According to the Etymological Dictionary of Greek (Beekes, 2010), the word derives from Proto-Hellenic *\*kʰorós*, "likely from a Proto-Indo-European *\*ǵʰeros*, from a root *\*ǵʰer-*."

**Enclosure Connection:** The "enclosure" interpretation is presented as one of three competing theories rather than established consensus. It proposes the root meant "to seize, catch, enclose," yielding an original meaning of "encircling/ring (dance)." However, the source explicitly notes the semantic identity remains disputed, indicating this connection is contested among scholars rather than universally accepted.
```


## [2026-09-06T02:21:27.238Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/curtain",
 "prompt": "Give the full etymology of 'curtain' verbatim: Old French cortine, Late Latin cortina, and whether it is connected to Latin cohors/cortem 'enclosure, court' and the Greek aulaia mistranslation story."
}
```


## [2026-09-06T02:21:29.398Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON قرن ===\"; grep -n \"قرن\" MON_part1.txt MON_part2.txt | head -15; echo \"=== MON کر (chorus) ===\"; grep -n \"کر\\b.*آواز\\|کُر\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Mo'in for qarn and kor"
}
```


### [2026-09-06T02:21:29.512Z] TOOL RESULT

```
=== MON قرن ===
MON_part1.txt:3151:قرنیه ( که کروی نباشد) و یا جلیدیه (که 
MON_part1.txt:3627:ابران در قرن‌های چهارم و پنجم مصطلح 
MON_part1.txt:8514:اختیال: اقرنده (ع.] (مصل.) تکبر کردن؛ 
MON_part1.txt:13008:اسلامی: قرن‌هایی که از آغاز اسلام به بعد 
MON_part1.txt:21677:بدگونیا: قرن«تع-۲ (ص‌مر.) (معم.) زمین با 
MON_part1.txt:26830:بسی خیال: اقرندآن آن. ع.] (ص‌مر.) 
MON_part1.txt:27544:بدلی که یکك قرن پیش زنان ابرانی در داخل 
MON_part1.txt:34011:می‌کند حالت بدهد. بیانو در اواخر قرن ۱۸ 
MON_part1.txt:34872:ضح.- این کلمه را در قرن حاضر در مقابل 
MON_part1.txt:49346:دسته. اهل بککك زمان. قرن؛ ج. اجیال» 
MON_part1.txt:50356:-صلبیه» که در قسمت جلو قرنیه را‎ ۱ 
MON_part1.txt:51601:باشند. ( گیا.) گیاهی از تیرة قرنفلیان که 
MON_part1.txt:64581:زردچوبه» زیره» قرنفل» دارچین» هل و 
MON_part1.txt:64814:دیوان‌سیاه: «قرنه.4 (ص‌مر.) آنکه دفتر 
MON_part1.txt:71350:فضای بین قرنیه و عدسی موجود است. این 
=== MON کر (chorus) ===
MON_part2.txt:1077:عراق و آذربایجان و موصل و کُرجستان و 
MON_part2.txt:1162:کردن با مهابت. آواز مهیب. به غرش در 
MON_part2.txt:1601:کردن؛ فرباد زدن» آواز بلندی برداشتن. 
MON_part2.txt:21515:کر: 0۲ (.) (مس.) آواز دسته جمعی (اپراه 
MON_part2.txt:22023:کرش: 5 (اصت.) آوازی که در وقت 
MON_part2.txt:22416:کرم خاکی دستگاه کُردش خون یک 
MON_part2.txt:24043:می‌کر دند به آواز می‌خواندند که «کفتار در 
MON_part2.txt:37131:3 نسطق. او | تقل کر (آواز)؛ 
MON_part2.txt:38846:و (.) کُرزء عمود. جماق. 
MON_part2.txt:48152:دشمنی کردن. دشنام دادن. آواز ند کردن. ستفعلن فاعلاتن؛ چهار بار مفاعلن فعلاتن
```


### [2026-09-06T02:21:33.954Z] TOOL RESULT

```
# Etymology of "Curtain"

The word traces back through Old French and Latin sources with an interesting semantic shift:

**Direct lineage:** "from Old French _cortine_ 'curtain, tapestry, drape, blanket,' from Late Latin _cortina_ 'curtain,' but in classical Latin 'round vessel, cauldron,' from Latin _cortem_ (older _cohortem_) 'enclosure, courtyard'"

**Connection to cohort:** Yes, the etymological record confirms the word derives from the same Latin root as cohort—both stem from _cortem_/_cohortem_ meaning an enclosed space or courtyard.

**Greek loan-translation account:** The semantic transformation occurred when "_cortina_ being used as a loan-translation of Greek _aulaia_ ('curtain') in the Vulgate" to render Hebrew _yeriah_ in Exodus. The Greek term itself connected to _aule_ meaning "court," possibly because a cloth hung at the doorway leading to a Greek house's courtyard functioned as a barrier.

This etymology reveals how a Latin word originally denoting a physical container acquired the meaning of a hanging cloth through religious translation practices, ultimately producing the modern English word for window and stage coverings.
```


## [2026-09-06T02:21:39.806Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '21505,21525p' MON_part2.txt; echo \"=== قرن headword ===\"; grep -n \"^قرن\\|قرن:\\|قرن .\" MON_part2.txt | head -20",
 "description": "Mo'in kor entry and qarn headword"
}
```


### [2026-09-06T02:21:39.891Z] TOOL RESULT

```
بود. (قد.) در اهواز یک کر گندم ۱۲۵۰ 
من و یک کر جو ۱۰۰۰ من بود. 

کر: :۱:۰ [شاخ] (.) (مسد.) یکی از سازهای 
بادی است صدای گرفتة آن حالت محزونی 
به آهنگ می‌دهد وغالباً نواهای محزون یا 
هیجانی را با این‌سازنوازند. 

کر: 0۲ (.) (مس.) آواز دسته جمعی (اپراه 
کلیسا و غیره)؛ مق. آریا؛ سلو. 

کراء: ۲۵2 (ع. ف. کرا] (مصم.) کرایه 
دادن ستور و جز آن را» به مزد دادن. (.) مزد 
مستاجر» کرایه. 

کراب: ۰۹0( [ع.] (مصل.) بارستن بر 
سنور. 

کرات: 0 کرت. حمله‌ها» 
=== قرن headword ===
6694:قرنفلی؛ ابرنجمشککه اقبلیس» حبق صعتری؛ 
10753:اواخر قرن شانزدهم م. تقریب مقارن با زمان 
12453:قرن: ۸5« |معر.] (.) (گیا.) زغال اخته. 
12466:قرناقان. 
12468:قرنطین: ۵ [- قر نطینه» معر.] (.) 
12500:قرنفل» قرنفل بستانی» قرنفل باغی» گل 
12507:قرنفل: (گیا.) در برخی کتب اشتباهاً درخت 
12512:قرنفل خودرو که در مراتم و چمنزارها 
12514:قرنفل بستانی: (گیا.) فرنجمشکث. قرنفل 
12546:قرنیه داخل آن می‌شوند. سطح خارجی 
12547:قرنیه به وسیلة یکك طبقةً بافت پوششی 
16913:قریب یکك قرن روش سیاست خارجی ایران 
18610:متعلق به اوایل قرن ششم ه. (دوازدهم م.) 
18632:نود ولی در اواخر فقرن ششم ۵ . . (دوازدهم 
18636:نیمه قرن هشتم ه. (چهاردهم م.) رونق 
19853:قاجار (نیمة دوم قرن ۱۳ ه.) وارد ایران شد 
24726:قرن اول هجری میان مسلمانان دربارة مسایل 
25623:قرنتت) کنند: 
29249:ناصرالدین شاه قاجار (نيمةٌ دوم قرن ۱۳ ه.) 
33496:قرنفل الشعراء و حسن یوسف و گل میخکثك
```


## [2026-09-06T02:21:46.345Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12420,12470p' MON_part2.txt",
 "description": "Mo'in qarn area"
}
```


### [2026-09-06T02:21:46.404Z] TOOL RESULT

```
فرموت: ۷۵۷ ا[تر .] (.) مخلو طی از گاه 
و جو و یونجه که به اسب دهند. 
قر مه: (۵-)۲۳۱۸ [تر . - قورمه ‏ قاورمه ] (.) 
شت ریز ریز کرده که آن را تف دهند و 
سپس از آن خوراکث سازند یا در کوزه‌ای 


کرده سر آن را محکم بندند و در مواقع 


۱۲۳ 
ضرورت از آن جهت تهیةٌ خوارک استفاده 
کنند و و اين عمل در در ده‌های ابران متداول 
است. گوشت بریان. 

فر مه سبزی: آ2تهع-. [تر. ف.] (امر.) نوعی 
خورش است که از گوشت و تره و جعفری 
و شنبلیله درست کنند. بوی قرمه‌سزی دادن 
سر (کلة) کسی: (عم.) بسیار متکبر بودن 
وی» افاده سیار داشتن او 

فرن: (ع.] )۱( 0 از زمان معادل 
سی سال. صد سال (اینکث بدین معنی 
متداول است.) سده. باره‌ای از زمان؛ عهد» 
دوران» دوره؛ ج. دوره. 

فرد: 7210 [ع.] )۱( شاخ» سرون. تندی سر 
مردم که به منزلةٌ جای سرون جانور است؛ 
زبر سر. گیسوء موی بافته. نوک مو. سر کوه. 
کرانه قرص آفتاب و بالای آن. آنجه 
نخست پیدا شود از شعاع آفتاب. رثیس 
قوم» مهتر 

قرن: ۸5« |معر.] (.) (گیا.) زغال اخته. 

فر د: 2 [ع.] (.) شتری که آن را با شتر 
دیگر بهم بسته باشند. ریسمانی که با آن دو 
شتر را می‌بندند. کیش از چرم» ترکش. 
شمشیر. تیر. 

رد 0 ((ص .) همدست و 
حریف در شجاعت و کشتی و جز آن. نظیر 
مانند» ج. اقران. 

قسرناق: ۳277۰ [تسر. - قرنق] () 
خدمتکار؛ کنیزکك» ج. (به سیاق فارسی) 
قرناقان. 

قرنطین: ۵ [- قر نطینه» معر.] (.) 
جایی که در آن مسافرانی را که از سرزمینی 
۱ وارد می‌شوند که در آنجا بیماریی ساری
```


## [2026-09-06T02:22:08.039Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FFD azordan ===\"; grep -n \"آزرد\\|آزار\" incoming/FFD/FFD_pages.txt | head -15; echo; echo \"=== BRT zar ===\"; grep -n \"azarəta\\|azarata\\|āzarəta\\|zar-\\|zara-\" BRT.txt | head -20",
 "description": "Grep FFD and Bartholomae"
}
```


### [2026-09-06T02:22:08.104Z] TOOL RESULT

```
=== FFD azordan ===
689:۱ آزاردن
690:آزارد + فارسی میانه 22374 < ایرانی باستان 3-227-12*. 8 پیشوند فعلی است >
692:آزار« فارسی میانه 2227 < ایرانی باستان 3-237-0*. برای 2 -> آرای.
693:«آرّرد»» که امروزه به ضم ز تلفظ می‌شودء» مخفف «آزار» است.

=== BRT zar ===
4180:•  j.  'anhuyav-  Adj.  'der  sich  (den  Anspruch auf)  das  (andere)    Leben  erwirbt':    zara-
4708:•  j.  anyö,  ainyö  Adv.  'ausser,  ausgenom- men, abgesehen  voa  — ',  mit  Abi.:  ^at  äs ma^änqm  ,  .  v3r>iravasl3mS  ain-  zara- %ulträ:  yt.jg.^6;  38;—  kakmai paoiryd malyänqm  "apir^si  (sd.)  tum  . .  an'  mana (statt  AbL)  yat  zaraittitnit  ,  .  ahntäi paoiryS  afi^Dse  (sd.)  az»m  an"  ^wat  yat tara>usträt  V.  2.  i  f.;  —  taii  also  s}a  .  , äamanqm  ham.rai'iviayeiti  . .  an'  ahmüt yS . .  "nicht  erstreckt  der  Hund  . .  auf  die Geschöpfe  . .  seinen  indirekten  EinBuss ausser  auf  den,  der  . ."  V.5.34;  —  kaf nä  *daivayasnai  vä  .  .  gSus  aiiiiitya  (sd.)
5480:kainlnö  kihrpa  srJrayh  Yt5.64;  —  bow- raini  vastrh  vat»hala  °dvl  süra  anilAi/a Yt.5. 129;  7,19,88,91,  95,96,  123,  127, laS;  —  avaj  nyapt^m  dazdi  me  vami/ii snisU  -dvliyS.)  süre  anil/iile  yäh  a  . .  Yt 5-  18;  9.  63.  77',  »S.  87,  90-  94.  130. 131,  Ny.  /.  19;  —  paili  dim  p»r>sal  zara- %uilrS  "dvltn  sürqnt  anahitqm  yt5.9o; I,  9,  62,  94,  Vr,2.  7,  Ny.4.9.
5830:•  j.,  g.  ast'vant-  Adj.  (fem.  'vaitt-)  'mit einem  stofflichen  Leib  versehen,  leiblich,  | stofflich,  materiell';  Ayat  'vant»m  dada uäatam  "als  du  Leben  mit  Leib  versahst" Y,_5/.  11;  —  tat  (näml.  mlidf/n)  er  mazdä vairlm  'vaits  ustänät  data  vatfhlus ^ttoiana  manar-ks ySi . .  "diesen  köstlichen (Lohn)  ja,  0  M.,  werdet  ihr  durch  das Wirken  des  VM.  dem  leiblichen  Leben (derer)  verschaffen,  die  . ,"  Y.54. 14;  — •vat  ahm  hyät  uslStiä  (sd.)  aojSrigAvat "^.43-  16;  —  ash-atjrmya%a  astva  *kqm ustanava  (sd.)  °vat  *ai^yeja/nm  paitisät Yt.  13. 1 29;  —  *vTjvähu  (sd.)  paiii  tanusti 'vh  gays  *däryeife  FTVf.4.2.  A)  sonst. nur  als  Beiwort  von  a)  stay-  (sd.) :  zara- , %ustrahe..yS paoiryö  stsis  'vadyä ..  Yt.ij.  1 Sgf«.  b)  gai^ä-  (sd.),  Sg.  und  Plur.J darfsca  (sd.)  da^at^amirixfyantim  vTspatn yam  "vaitlm  gae^qm  Yt  i<).  94;  Y.  g.  8, 37.23,  *Vd.£'>;  —  zarai:mtr5  ratus 'vai>ya  gaf^ayä  Yt.  73.  4r;  j.  89;  — kat»  %wqm  paoiryS  'vai^yäi  hunüta gai^yäi  Y.p.  3;  4;  —  m/l  m?m>cainTs gai>a  'vaitls  asake  SrB._j;  Yt/5.  41,  V. , ^^•SS;  —  "J  ^^  apqm  a'javö..  jasanli..' yavanqm  .  .  västranqm  ,  ,  gafianamüa 'vaitinqm  Yt  ^'.29;  —  V?'"  ■  ■  /rävavacä .  .  zara'iuströ  gae'iabyö  'vaiHbyS  Y.ö'j.g; P.  13;  —  ahura  mazda  mainyö  spinista däiar>  gad'^ariqm  'vaitinqm  asäum  ''" I.  7- 1.  9- 1,  lo- ".  "■  I.  '4-  I,  34,  K
6082:jrjmuibmS  Y.57.4;  7.1,  2^.2;  —  zara- ^BsTrvm  .  .  yat  as  °hm  alavasfornd  (sd.) .■V._y.  4;  — j'aia  °ä7/  x!a%tym  cinasti  (sd) Y.20,3"';  —  äat..  ah<  nmänahe fraf^wd gäus  .  .  'um  .  .  i-ästrpm  V.J.  3;  —  asis/a itä  airihat  haca  vlsat  gaul  buyat  asUbm •am  Y.  60.  3 ;  —  us  nü  aiAhäi  vXse  jamyät •ämca  x/a^nm/a,.Y.6o.2.  III) 'Recht, reditmässiger  Anspruch  (auf  — )'  und  zu- gleich 'Gegenstand  des  Rechts,  worauf  man Anspruch  ha^  was  einem  gerecht  ist';  spez. von  dem  ftir  die  Zugehörigkeit  zur  sara- l^u/jyischen  Religion  und  das  ihr  ent- sprechende Verhalten  zugesicherte  und  da- durch erworbene  (höchste)  Anrecht,  d.  i.  das auf  das  ewige  Gut  (Paradies)  und  dieses selbst  (S.  auch  vAbleit).  i)im  gAw.:  '/,/m 'dtrndyai  (sd.) . .  räyS  asts  vanfOui  galm (sd.)  manauhs  Y.  43-  •  "'j  —  .y?"»  i^am (sd.)  data  .  ,  ahurö  °sahyä  iizäyäi  (sd.) pmdim  Y.^i.ij;  —  käds..ysi  uxifinn (sd.)  asnqm  a»!iSu^  dar^%rai  (sd.)  frS •iahyä  /rar  iitzY.46.y,  —  ya  ^aohana.. awuntStim  "hmcä  *iaibys  dänAä  (sd.) natda  xsa>r»nca  Aaurvalät3  Y.S4- läis  yüs  g/ae^ORäis  'um  xsmmbyä  dadi^l (sd.)  Y.46.  is'J>;  —  ktßarä  yas5  (sd.) hyin  'liin  Y.  5/.  4.  2)  im  jAwr.:  tßit
6768:raütica  1 .  .  urvaiainarS  . .  tümc'a  ys  zara-  r*"^"t1'  1'  Ta    *'w''/v'"'""'  ^°- '  ^""l!
6863:'rahe    mazda    Yti^.pf.;   —   yazus  .'r5  mazdäY.22.9>;  —  eil  hau  a pu^rö  'rö  (statt  Gen.?)  mazdä  F. 4%;  —  lyJ  . .  /  äat  mraot  (Stverz,,  unter  I  i )  'rd ätars  (Stverz.)  'rahe  mazda  puira  Y.6$}mazdä  "Y.g.^it;    usw.;    ö.  44,  7.78,  Yt 1 2;  7.2 ;  usw.; — ätari  (Stverz.)  mazdä  'rahe]8.5J;  — pfrpsat  (Stvetz.,  unter  i  a),  zara-
7741:•  j.  9r«zvo  Adv."  'wahrlich,  fürwahr'; 1)  an  der  Spitze  des  Satzteils,  vor  Vok.: fr°  asäum  spitama  ^7vam  da^at  ahurB maidä  Yt.  5.  89;  91,  95,  12.3,  13.  i,  Ij. 31.  2)  hinter  dem  Wort,  das  hervor- gehoben werden  soll;  a)  hinter  dem  Pron. pers.:  yat  tum  hs  uzsayatjha  tum  3r° zarahultra  Y.g.13;  —  aez'alia  bä  zara- 'i^ustra  ya>a  tum  jf  vasanhe  V.5. 17; z\;  —  paiti  »lam  if  ptnsat^uha  yim ahursm  mazäam  V. /^.  7,  b)  sonst: mazilt»n  ..vispanqm  tr"  sravaahamYi^N. 4.1;  —  daliiqm  »r'  yaozdaii-Xta  a^a  zX. . asti  yaozdäili^  .  .  havaya  ir'  dasnaya  V. la.  1 9.
10318:•  j.  gäSS-  f.  'Lied'  uzw.  religiösen  Inhalts; 1)  insbes.  von  den  fünf  Hymnen,  bez. Hymnensammtungen,  die  in  Y.  28—34, 43—51,  59  erhalten  sind*':  sraobm  .  .  y5 paoiryd  "^.J  frasrävayatya panca  . .  zara- iu/traAe  *a/smaimvan  (sd.)  vacastastivaf malMzaintls  mal.paiti./rasä  Y.57,8;  7/. 6, G.  7.6;  —  akunavaitlm  (Stverz.)  °'i:qm aiaonlm  .  .  mai.afsmanam  mat.vaüäslallim map.äzaintim  matpjnsvlm  mat.paiti.p?r>s- Vlm  map  varfiibyjca  *pa^?byasca  kufra- mtrttqm  . .  küfrayaslqm  . .  Vr.  14.  o  f.;  usw.; — ahunafalca{^A.)  'Lariam  ^.46;  —  uita- vaitya  (Stverz.)  '"^aya  handatä  ya^amaide . .  haitiPca  afsmans^a  vacasca  vacaslal- llmca  /rasraa'knmca  ..'Vj.iS.y,  usw.;  — sp)ni:1.mainyBm  (Stverz.)  '"^qm  asaonzm  . . Vüiuxsa'irqm  (Stverz.)  '^qm  ..vaAisISistim (Stverz.)  'iqm\x.2.Zl;m-»i.  2)Bezeich- nung  für  alle  (anscheinend)**'  im  Gä^ä- dialekt  verfassten  Stücke  des  Awesta,  d.  s.  — ausser  den  eigentlichen  0<i>äs  —  AtxYHapt. und  die  vier  heiligen  Gebete  (V.  27. 13— 15, 54.  i  )'*'>;  nur  Plur-,  womit  entweder  die Gesammtheit  dieser  Li  tteratur  oder  einzelne Abschnitte  daraus  gemeint  sind  (s.  auch  A): imäsf  tg  haoma  °^ii  imä  h^nti  staomsyS'^. /0. 18;  — farS  amisä  sp>nta  ''ka  gJurvJin Y.2S.0;  —  tipma  vi  0(7  dcflö«/"/ Y.2(V.o, 430,  47-o,5io,S3°''  —  '"i'^byS  spintäbyd ratuxsa^räbyS  (Stverz.)  alaonibyö  Y.55.  i ; usw.;  —  tä  713  hmti  °äi7  har^'iravaitista
10467:5*9  'grab-  Noten  —  yzar-  mit  aiwi  530
10499:mp.  ä-granä-lum  Dk./.  6.  7  (West:  'the  most !      -prod- :  izar-  (sd.)  =  gr.  il^l-io  :  ai.  fi-par.d;
10514:/zar-  mit  a
10914:•  g.  *xkn3iV'  i)  Adj.  'Genüge  leistend,! zufriedea  stellend',  mit  Akk. :  yS  ,  ,  zara- ' "iiultnm  rääarfhä  . .  'näuiiüS.)  Y.4Ö'.  13;
11194:♦)  Nicht  fünf,  wie  die  übrigen  Länder;  es hat  keinen  besonderen  raiui  däKyumö,  dessen StellDng  Tielmehr  zusammen  mit  der  des  zara- %uJtr3.ümö  in  einer  Person  vereinigt  ist;  zuletzt Marqdakt  EranSahr  uz.
11753:—  tä  xsapanB  yä  *ß'äM  Y.öa.io;  — .  a)  adjektivisch;  a)  im  gAw.:  däidl  .  . ätiti  tä  ^ao^na  .  .  yä  anhus  . .  v»rft- '  tarn  aslm  vaahsus  äyaptä  (sd.)  manatgAs yäii  V.J5. 1;  4.41;  —  yat  ta  sravA  drm-  Y.  25.  7.  B)imjAw.:  *us  ^täai  späna jayqri  yä  pagurva  ,  .  'S,  4,  45;  —  ta  fryi  pat»titi  pasus.haurvqmca  . .  V.  /J.  4a;  43; , .  tä  isuds  .  .  ta  rätayo  *yam  (APn.)  —  pqscaUa  ava  ta  aiü  maya  ..  V.g.ii; oAurS  . .  frävavaca  Y.ö^.g; —  tä  daiA-\^2.  a)  mit  relativischem  Anschluss"; MävS  ..  nijayntnte .  .ydhra  /r<Mir!Hnti  ..^  k)  yai  %Pi}K.:  gavöi  aääisizA.)  iäis  ^ao- /mvafayuYtij.^Si  —  yasf  tarn  dahyüm  .'haiiäis  yäis  vahiitäis  Y.J5.4,  b)  im äcaraiti  yaia  {'wo')  huh3r?ts  *baraite  Yt-ijAiw.:  ttm  ratüm  yaxamaide  yim  zara- 10.112;  —  tä  (statt  NPf.)  daiMävS  ti  "ä-usinm  Y.70.IJ  i';  —  i?m  aküm  paik- ^hamtTT^e  yd^a  duzh?nni5  *baraite  mi~  yäite  yim  aiaoiiqm  V. 18.^6;  76,  5.62; ärff  Yt  10.  48;  41.  b)  substantivisch,  —  upa  tarn  ear?lqm  yqm  datvyqm  Yt  /'/. a)  im  gAw.:  «m  (ASm.)  ..  mimaysff  y!  77;  —  tqm  krhrffm  yqm  iristake  V.$.i; qnm3til(sd.)  mazda  srävl  ahursY.4$.io;  —  täia  vt'hü  yaxamaide  yä  antarpsta  Yt 9;  —  alca  töi  (NPm.)  vaim  hyäma  (Sp.  I3.\^y,~- tä  fravaiay5..aojiita  fuiiti  yä '75  0-)  y^^  ■  ■  ^^fDnaoit  . .  Y.30.  9;  —  paoiryanqm lialsanqm  Yt/J.17,  b)  sub- ai  tSi  at?h>n  saosyaiits  .  .  yH  .  .  htüänti  stantivisch;  A)imgAw.:(i//(i/  msi  daxstfm Y.dS.xi;  —  talcit  . .  ySi  /iisitms  \.  data:  ahyl  ar)ASu£  vTspä  atag^ä  (sd.)  Y. 32. 11;  —  t^ng  tfarayS (sd.)  yöi  vä  daibi-  34.6;  —  tatcä  .  .  'kwaAml  *ä  dqm{sA.) Alt/r  Y.  32.1;  44.11,  13;  —  maf  täis  nipäail:  man5  vofia  urunas^a  ..Y.4g.\o; vispais  yöi  .  .  marintl  Y.43. 14;  —  tal  —  yä  tat  upä.jamyjmä :  tavacä  haxfmä v»myädyäi  kyai  msi  mraota  (sd.)  i-aktstim  ,  asaAyl'ä  Y.  40.  a ; — y.J  tat  upä.jamyämä : 43. 1 1 ;  J/.  5 ;  —  vaida  tat  y''  "Ami  .  .  \  tavatä  sarSm  asafiyä/ä  Y.  4l-  6;  —  ta/a analiS  (sd)  Y.46',2;  —  ta  (APn.)  hwa'  vupä .  .htvaAml ..  xia%r?i  ä  voya'i  ra  (%A.) p^rysä  ..ya  aX  aiil(Sp.  14$  ZD.)  ..Y. 31.  i^l^Y.  34. 10;  —  tat  vJ  nJ  Aasaas Jr^Aj  (sd.)
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
12600:'lehren,  unterweisen',  mit  Akk.  der  Per- son: a^J  a^ä  cSii  (sd.)  aAurö  .  .  zara- 'hustnm  ataxsayaaa^^  (Augm.)*^  vJspa^ farasnt^la  Y.  iz.  5.  a)  mit  Inf.  als  Sach- objekt: kyat  mS  . .  daxsat  usyai  (sd.) *titsna.maiiis  vahistä  Y.  43.  r  5.
13326:•  j.  däityä-  f.  Name  eines  Flusses**  in AiryanaVa^ah  (sd.):  tarn  yazata  ..  zatri.- vairil  *pasne  apö  "yayh  Vt5. 112;  g.f), I/.61; — mmS ape  'yayaYti.21.  a)sonst mit  vatiuhi-:  äpS  vanuAli'  .  .  vaahuyh 'yayä  V.  ig.  2;  —  tarn  yazata  .  .  zara- ^uHrS  airyene  valjaki  vauhuyä  °yays  ". .  in dem  arischen  Vaijah  der  guten  D"  Yt 5.104;  17, /5-«.  V./.z,  2.20'.
14890:yaoiädhd  dakmayStparS  ä/ritstt.,  dairihu. paitlm yaozdd^ö  ustraAe'ti  arsnSV.Q.^T'^; 37  f.*.  a)  bes.  beim  V._>'a«-:  vanani^m .  .  yazamaide  amaheca  °ii  kuiastahe  Yt. Ä  I2J  12',  U- 133-135 '^  JJi;  —  yaf^a- maide  ^a/am  malfi^anahe  (sA)  °//*'  .  . drvaßaoi  Y.  7Ö'.  10;  —  ft«  yazata  . .  zara- %uitrS  v^fhraynaAe  'ti  manahi  Yt/^^aS; 78';  —  yqm  yasata  zard^uilrS  .  .  ava- he^a  'ti  yqnahe  yat  hi  da^a/  .  .  Yt.  16, 6f.  b)  aSahe  paiti  (Sp.  14  m.,  u.)  '(als
17233:•  j.  be  Part  zur  Hervorhebung  des  ersten Worts  im  Satz:  zätS  b'  yS  asava  zara- ^u/irS  V.  ig.  46.
```


## [2026-09-06T02:22:09.676Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD azar ===\"; grep -n \"azār\\|āzār\\|azar\" PHD.txt | head -15; echo; echo \"=== PHD_mackenzie ===\"; grep -n \"azār\\|āzār\" PHD_mackenzie.txt | head -15",
 "description": "Grep MacKenzie for azar"
}
```


### [2026-09-06T02:22:09.741Z] TOOL RESULT

```
=== PHD azar ===
59:The orthographic principles followed, in seemingly haphazard permutation, in the writing of Pahlavi, besides the ideographic, include the phonetic (within the limits of the alphabet), the his- torical, the pseudo-historical, and. others so indeterminable as scarcely to merit the name. The establishment of the original spelling of a word, therefore, very seldom reveals its pronuncia- tion. To determine this it is necessary to examine all the available comparative evidence.
224:ayabag 15 azarmigih
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
227:azbāy- [*2b*d-] invoke. ~išn: invocation. azd [zd | = M] known. Azdahag Pcydi’k' | M ?zdh?g, (N aždahā)] a legendary ‘dragon’ king, Dahāg. azdénidan, azdén- Pzdyn-ytn'] inform. azēr [%cdl | N zér] below, under. azg [22 | N аху) branch. aziš [hcf | М *cy$, 22у] from him, it; postposition (= az) from, ~-keh [-ks] inferior, subordinate. ~-meh [-ms] superior. āz-kāmaģ [?ck’mk'] greedy. ~ih: greediness. azmüdan, azmāy- ['zmwtn!,?zm'd- | N 2~] = uzmüdan. aznawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be extinguished. āzurdan [Pcwltn! | N ~] = āzārdan, āzwar [?*cwl | N ~] greedy. ~ih: greed.
396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
753:ageless azarman. aggression hénih. aggressive mustabarmand. agile čābuk.
2061:fuller gazar.
2205:harm (n.) ak, anāgīh, azarm, bei, bēšišn, wizend, zyàn.
2439:injure āzārdan, (āza/urdan), wizastan, (wizüdan), xastan.
2441:injury āzārišn, azarm, wizāyišn, wizend.
2734:market wāzār,
2783:merchant wāzāragān.
3994:thousand hazār.
4033:torment (n.) āzār(išn), bēšišn.

=== PHD_mackenzie ===
```


## [2026-09-06T02:22:23.918Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"peinigen\" BRT.txt | head -10; echo \"=== FFD page tag ===\"; awk 'NR>=600 && NR<=700 && /\\[pdf page/ {print NR\": \"$0}' incoming/FFD/FFD_pages.txt; echo \"--- lines 685-700 ---\"; sed -n '685,700p' incoming/FFD/FFD_pages.txt",
 "description": "Bartholomae peinigen and FFD page number"
}
```


### [2026-09-06T02:22:25.606Z] TOOL RESULT

```
=== FFD page tag ===
636: [pdf page 27]
662: [pdf page 28]
666: [pdf page 29]
685: [pdf page 30]
--- lines 685-700 ---
[pdf page 30]
ماده‌های ماضی و مضارع فارسی دری - ا اس ۲۵
8 صورت بالانلرهٌ ريشهٌ 7210 است. ريشةٌ 730 «استراحت کردن» معنی می‌دهد. از
ريشهٌ 1318 «آرمیدن» و «رامیدن» هم آمده‌اند.
۱ آزاردن
آزارد + فارسی میانه 22374 < ایرانی باستان 3-227-12*. 8 پیشوند فعلی است >
آراست. 237 ريشه است به معنی «تحریک کردن» و 12 پسوند است. برای 12 > آراست.
آزار« فارسی میانه 2227 < ایرانی باستان 3-237-0*. برای 2 -> آرای.
«آرّرد»» که امروزه به ضم ز تلفظ می‌شودء» مخفف «آزار» است.
آزدن, آژدن
آزد « ایرانی باستان ۴2-70-18 برای 18 -> آراست. 2 پیشوند فعلی است. 8[ صورت
ضعیف ريشةٌ 8/180 است. 8/188 به معنی «ازدن» است. «آژد» از پهلوی اشکانی وارد
فارسی دری شده است.[ ایرانی باستان در پهلوی اشکانی #ودر فارسی میانه 7 شده
است.
آزن « ایرانی باستان 20[-3*. آژن < پهلوی اشکانی 0ه37* < ایرانی باستان 80[-3*.
آزمودن
```


## [2026-09-06T02:22:38.680Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"zar-  'kränken\\|kränken\\|kranken\" BRT.txt | head -10; echo \"=== search columns 1685 ===\"; grep -n \"1685\\|1686\" BRT.txt | head -5; echo \"=== hu.azara ===\"; grep -n \"azara\\|äzara\\|äzarSta\\|azarSta\" BRT.txt | head -10",
 "description": "Bartholomae zar entry search"
}
```


### [2026-09-06T02:22:38.773Z] TOOL RESULT

```
2633:'vergewaltigen,  kränken':  ks'iwqmyim akurim  mazdam  "mazislayanti  isA.)  tnaotü V./i-.öi. aL  inMi,  'initak.  —  Pü. ;  tetümtan.  —  '5  Das  ^ n  ist  im  letzten  Grunde  praesentisch.  —
4466:•  j.  ainitay-  1)  f.  'Nichtvergewaltigen, -kränken'  sva.  "milde  Behandlung,  Milde': '■tsit  F,  7;  —  'Isis  F.  7;  —  hada  . .  'ticä Y.  5Ä'.  4.  a)  Adj,  'nicht  kränkend' ;  'tis ai^  *vaxs  P.  26.
16696:•  j.  banta-  Adj.  (fem.  °tä-)  'erkrankt; krank,  siech':  ä/riti  .  .  yä  .  .  avanhmHt bandayeiti  'hmca  drSm  k»rmaoiH  ".  .  die den  Nichtkranken  krank  werden  lässt  und den  Kranken  gesund  macht"  V.  22.  s  ;  — fravalayS  .  .  yä  .  ,  dä%rT/  'iäi  drvatättm Vl/J.  24;  —  Ha  F.  16.
16708:HB.  254.  — 3)  VgL  ai.oidi/fl-' Rauschtrank' und  •  j.  »band- V. 'kranken'.  Praes  30  (Kaus.) •Rausch'.  -  :.)  S.  dazu  West  Av.-Gloss,  220.  \  bandaya-.  —  PPfP.  bazda-  (sbes.).
16711:•  i-.g.ban-V. 'kranken'.  Praes.  30  (Kaus.)  '     ü«):  vimäreiiUa«;  %.  va  ban-.
=== search columns 1685 ===
28003:1685  zasta-
28011:1686
30092:KompA.  1  Ableit.  —  S.  auch  Aitvä-  l.  —  Vgl. np.  labäH,  3.1.  jiMia-  f.«.  —  Pü. :  Ausvän.  — ')  Das  muk.  Geschlecht  ist  i.uf^lig,  wiid »ber  durch  alle  entscheidenden  Sielleo  ver- bürgt;  IF,  lO.  20z.  —  »)  Unsicher,  da  der Anfang  des  Wort»  lersiört  ist;  BB.  14.  245.  — i)  GS.  —  4)  LS.  statt  IS. ;  S  409  mit  No.  3.  — S>  S.  tasUiiyä;  Sp,  1685  m.  —  *)  Der  LS. dient  als  IS.  {s.  No.  5)  und  wird  im  Sandhih nach  dem  Muster  des  gleichlautenden  GS. (».  N'o.  4)  behandelt;  Bthl.  IF.  10.  102.  — 7)  So  K4;  NA.  :fenJ.  —  S)  NA,  aJä.M!vi; s.  aber  Pt  4  usw.  —  9)  Worüber  luletit  Colutz OrStudies  of  iheOr.Cluh  of  Philadelphia  167, BLoouFtSLD  AJPh.  f6.  426,  Wn.  AiGr.  r.  161, 163,  Fay  JAOS.  i6-  ccxxvm,  Pederson  KZ. jÄ  201  und  -  mit  treffender  Kritik  -  Uhlem- BECK  WAiSpr.  101.
=== hu.azara ===
19060:—  dieKopulaistzuergänzen:  yai  hl  zasta tf  frasnätaY.8.40; — äai yezi  si  anya  aya .^afi^ria  rf  fravarstaV.^.^i.  3)inunge- wöhnlicher  Stellung  " ;  yj  naire  mmarthnite n°  fumS  paiti.baraiti  Y.4.1;  —  yöi  vö vai3uhil .  .  n'  paurva  äzarayenie  (sd.)  Yt '3-  3°»  —  y'^  asrut^aosS  vä  .  .  n'  Bim citam  (Sp.  595  m.)    väcim  *aiwyas  a.i4;\
25078:•  j.  'ra^-a-  m.  'Wagen'*':  gäui  frazarSta (sd.)  aiSqm  "i'äj'fl  (LS.)  YL70,38;  — paiti.- stayata  'ihya  aül  vat>uhi  "es  luelt  an  auf dem  Wagen  A.  . ."  YLr7. 17;  —  akmya 'äa  hvasäna  \yX.48;  —  nöit  ihra  ../ras hyat  .  .  halnyS  '%ö  nsit  uspnpts  draßs YlÄsö;  —  yat  janäni  kitäsptm  'i^e paiti  vagaihyai  (sd.)  YLi^.aS;  —  tarn caxnm  (sd.)  . .  asmatam  ''h3in  ktnnavane . . ti  mg  väitm  ^anjaySnte  spirdasca  mainyui' attrasca  Yt.J(j.  43f.
27782:mit  3  dnwS  i ;  Akt.  und  Med. :  mä  äaä- raydis^  '"zara%u!tra/te  mä  ^pourmaspahe (sd.)  FrD.  4;  —  anäzanta  oHbyS  tur?bys . .  yni  vS  . .  nSil  paurvh  (Sp.  871  u.)  . . azarayenie  Yt  y.  30;    —    s.    noch    ans-
28046:•  j.  zazaran-  Adj.  'zornig,  zornmütig'; gvtaÄe  .  .   'rattS  (GS.)  Y.p.  3o'>.
```


## [2026-09-06T02:22:46.338Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '27760,27800p' BRT.txt",
 "description": "Print Bartholomae zar- entry"
}
```


### [2026-09-06T02:22:46.389Z] TOOL RESULT

```
•  j.  'zavan-  m.  EN.  eines  Gläubigen: gaomatB  'vanS  . .  asaanif  "des  G.,  Sohns des  Z  .."  Yty.  125.
Wohl  KuTzname;  vgl.  'zaj/an-.
•  ').  tavana-  n.  'Ruf;  Anrufimg". KorapA.  —  Zum  V.  tor-,  —  ai.  Aävaiia-  n.
•  j.  zavanö.sästa-  Adj.  (fem.  Uä-)  'durch den  Ruf  belehrt,  angewiesen':  ana  buyä fsd.)  'ta  "so  mögest  du  dich  durch  den Ruf  weisen  lassen"  Yt,  5,  9.
Npü. :  an  bid  ba  ^ähis  mirä  pand.
•  j.  zavanö.sii-  Adj.  'der  auf  Anruf,  wenn gerufen,  hilft';  apqm  napättm  .  .  aHätam 'sunt  Yt/p.  52;  —  cihra  vB  buyänl  ma- sänä  n^ra  vS  *sav3  (VP.)"'  "offenbar sollen  eure  Grosstaten  werden,  offenbar die  von  euch,  die  ihr  auf  Anruf  helft" Ny.j.ii.
Vgi.  j-ii^<jwjt.fln-.  — t)  D.L  'sm,S,  \268.\3.
s.  Mf3. ■    j.  zavanö.svan-   Adj.  sva.  'su-.    mm (näml.  Mihra)  ..  'sva  (NS.)  aki  sürB  Yt. 10.  76.
an-Part.  zum  V.  sav-;  s.  Bthl.  IF.  10.  195.
•  j.  zavano.srüt- ''  Adj.  'auf  den  Anruf hörend':  satavaisS  ..  'srtUS  (NSm.)"'  Yt i3'  44J  —  satavals?m  . .  •srBt>m  Yt  i^. 43  j  —  mihnm  .  .  •srBhm  Yt.  io.  61.
ai.  havanairüt-  Adj.  —  ')  F  l  hat  zweimal  11.  —
•  j.  '"utyeiti  zavavaf  hyatiia  mazäyascil
voku"-  Vyt  ?o  '*.
Pü.:/fl  ;^äiiiht.  —  0  Wo.  will  avaval;  vgl. noch  Sp.  1 164  No.  3.
j.  ia-^a>->/a:  s.  nnler  :ävat:
•  g.  zavah-  n.  'Kraft,  Stärke':  äaiva  . . spSniStä  mainya  maida  vanhuyü  'vS  iida (Sp.  3210.)  Y..??.ia.
VgL  zävar;  —  Pü. :  vahumaii  gri/lär  haue  pa an  dahiin^  Sü. :  gvahman&sya  grahiläro  AAtwä' maii;  vgl.  zu  laalar-  No.  8.
•  j.,  g.  zar-  V.  'erzürnen',  Praea.  10  b sarariu-^\  11  b  zaran-",  13  zaranya-^'', 30  (Iter.)  zäraya-;  Perf.  i  zazar-'K  — PPfP.  tar^ia-,
1)  Akt  'erzürnen':  anäisvä  nöii  ahurä inazda  asimcä yän3ii zaratialntäi^  manascä kyal  vahistim  "um  dieser  Gunstbeweise willen    möchten    wir  euch,    o  AhM,  und
1670
A.  und  VM.,  nicht  erzürnen"  Y.  2Ä9;  — drva    zaritS   YtiJ.  5.  2)    Med.   'sich
erzürnen,  zornig,  ergrimmt  werden':  drvi zantS  zaranumanö*'*  zazarSnB'''  Yt II.  5;  —  mihrym  yim  ..  zaranimmm p3r3%ujafai3hs  vazmti  avi  kamayh  "M., den,  wenn  er  zUmt,  die  breithufigen  (Rosse) fahren  gegen  .  ."  Yt.  10. 47.
mit  3  dnwS  i ;  Akt.  und  Med. :  mä  äaä- raydis^  '"zara%u!tra/te  mä  ^pourmaspahe (sd.)  FrD.  4;  —  anäzanta  oHbyS  tur?bys . .  yni  vS  . .  nSil  paurvh  (Sp.  871  u.)  . . azarayenie  Yt  y.  30;    —    s.    noch    ans-
ai.  kpfül  \  h^näyän ,  h^Jyämäna^ ;  np.  äsjr- dan.  —  Pü.  (zu  Y.  38):  äiärem,  (zu  Yt.  //): äzirlär,  äzär  menün^i,  a!  Szärit.  —  ')  D.  i. ^rati'.  —  >)  Die  Bestimmung  von  laiatänö alsPPfM.  ist  nnsicher;  vll.  stammt  das  Wort aas  Y.  g.  30,  s,  sataran-.  —  J)  Them.  — <)  Die  Annahme  S  3'5  h  ist  nicht  unbedingt nötig.  —  i)  Ob  handschriftlich?  S.  Dst.ZA. 3.  151.  —  *)  Teilte  also  3aratm-\-miinS ;  ge- ringe Sletle.
•  g.  zara-  m.  'Streben,  Ziel' :  ka%ä  mazda °nm  carani  haca  ximat  *ashitlm  (sd.) x^ntäkqm  "ob  ich  wohl,  o  M.,  durch  euch mein    Ziel     durchsetzen     werde    .  ."    Y.
44.17. Vgl.  ai.  häryali    'er  strebt  nach  -'   usw.;    s. vonPlanta  OUD.  /,  438,  —  Pü.:   tigSn  ehr- mazd  iamän  ('Zeit')  iarläriA  i  iiriäi,    crl. :  ia- män  i  lOH  i  fasin  eigen  bovtl. j.  tara' :  s.  auch  bei  ira'.
•  j.  zarad-a'jnyäi  In£  'ins  Herz  zu  treffen': aZa  taicii  uzjasmti  (sd.)  yä  mtnn^äila 'ynyaica  ". .  die  (da  sind)  um  zu  zerstören und  ins  Herz  zu  treffen"  V,  r.  1 4  Gl.
Zum  V.  gan-  (mit  S).  —  Bed.  sehr  unsicher ; man  verlangte  doch  ««J*.  —  Pü. :  undeutlich.
•  j.,  g.  zaraO'uätra-  m.  EN.  des  Stifters der  mosi/ischen  Religion,  aus  der  Spitatna- (sd.)familie,  Sohns  des  Poumfaspa  und der  iJwySii.wa*);  a)  im  gAw.:  aim  möi idä  visiJ  (Sp.  1315  u.)  yf  n}  afvS  säsnä (sd.)  gäiatä  'rS  spitämö  hvS  ta  . .  vaHl . . iankirg^ra  {sA.)  iravayetihl  Y.2t>.  8;  — yS  mq%rä  (sd.)  *vaam  .  .  baraitT  urva%ö as'd  tumar?hs  'r3  Y.J0.6;  —  a^  ahurS hv5  mainyäm  'rS  V3rmtlmazda  yasß  Hlca spSnisiS  Y. 4?- 16;  —  at  höi  aoji{zA.)  'rS paourvim  ^hai^ys.dvaisa  .  .  Y.  4j,  8;  — at  ratqm  (sd.)  °r5  lanvascl£  ifaAyä  ustartsm dadäitl  paurvatatjm  (sd.)  ^.33.  14;  — hyal    mlidim    °rS    magavabyB  (sd.)    iBist
■  53'
dby  Google
i67i
zarait'ustra-  b
zara9u£tra-  b
1672
para  Y.5/.  15;  —  iai  Uli  asä  tbayenti (sA)  avanAs  *rai  Y.  4g.  12;  —  if  urvaha (sd.)  spifamäi  °rai  nä  Y.5/.  11;  —  'ra kastl  asava  urva^S  masSt  magäi  (sd.)  ¥. 1^.14;  —  y!  spitamim  'nm  rädavAä (sd.)  manlalsii  xsrtäu!  Y.4('.i3;  —  y3 mOi  aiai  hathim  hacä  var»saill  (sd.) hyai  vasnä  firasö.lim»m  Y.  4ß.  19; däidi  .  .  mhais  (sd.)  tu  uxtais  matdä °rai  aojöngkvat  rafinS  Y.  28.  6;  —  vahüiä r/ft'/(sd.)  srävX  •raAt'^  sfitSmahya  Y.jj.  1
—  nSil  ta  Im  xsnaul  vaipyS  (sd.)  . .  */v» spitävmtt  Y.  5/.  n ;  —  pourucista  kalcaf. aspätta(_sd.)  spitamTyaivJ  dugtärqm  'rahV ^■$3-Z'>  —  ^  airyima  (sd.)  isyS  ra/mräi fania  mribyascä  näiribyascä  'rakl^^  Y. S4.  i;  verwendet  FrW.i.  i.  b)  im  jAw. (unvollständig):  'rahe  .  .  yehe  zq%aeea vaxlaliB  uitatatfm  nimravanta  vUpa sptntdJäti  dämqn:  uHa  ra  zats  a%rava yS  spitamB  °rS  fra  nS  yatäite  zao%räbyS si3r3ts.bar3sma  °rS  Yt  '^.  93  f. ;  —  advarmla adaunta  dalva  .  .  sätB  bi  yS  a^ava  'rd timänake  pourusaspaAe;  kva  Ai  aosB  vin- datnai  Aau   dasvanam  sna%J  V.  75.45  f.j
—  yaia  aztm  Aacayene  pu%r>m  yat pouruiaspaAe  .  .  °nm  anumatse  dainayäi Yt5,  18;  Y.p.  13;  —  »13  äzärayöis  °raAe (slattVok.)ffiiJ>i»TOiß4/flÄ^(sd.;  statt  Akk.) «3  dirfdS.vqm  FrD.4;  —  srüts  airyei-.e vaeJaAe  tum  .  .  °ra  Y.  5.  14;  Yt  5.  104, 17.45;  —  'raAc  spitämaAe  paoiryai  voAu mamnätiäi  .  .  vaokule  .  .  vavansuse  .  .  yö paoiryS  ci'hrim  unaisayata  dafvaaica  Aao- tai  (sd.)  masyäatca  yö  paoiryS  .  .  staüj aAm  naist  daH'S  fraormata  mazdayasnü . , yaAmi  paiti  vup3m.fnq%rfm  *as>m.sra7'S (sd.)  vJsruyala  . .  yitn  is»n  amisa  spinta ..  a/iam  raiümea  ga^anqm  YL/J.S;».; 41,  148,  152,  Ä44,  Vr.2.*4,  i6.i,  Y.16.2, 70.1, G.4.6;  —  id^rt/ raius {sd.) raya  sara- "^tdiris.  kaya  aiAAa  ratavS?  nmanyasca vTsyasca  zanlumasäi  'rö  tairys  Y.ig.iZ; 18;  —  'r3m  Aa^a.mq%r?m  (sd.)  yasamaide Vr.  13.  1;  —  /Um  paoiryS  'ra  aAumm vairxm  frasravays  Y.g.  14;  Yt  ig.  81  (wo Akk.  statt  Nom.);  —  lüm  sunargazS *ak3rmvl!  vTspe  darva  'ra  ySt  para  aAmät virB.raola  apataysn  Y.  ^.  15;  —  ra2k5 (sd.)  »(^(nänil.  dem  AaraMahiyav)  Aaca atäAä  z)mat  vaAAs  kinnaeüi  yO  tnqm  aü/S JamayHH  yB  spitämd "röYx.lT.ZQ;  19;  —
■    ai,a  a^iä  cBi£ 'rd  dalväis  sanm  vyämrvitS
Y. /2. 6;  —  <£kä  a%ä  Mt  ahurB  mazd'i 'rim  a^axiayafta  vispaisü  *frasnaisfl  .  . yais  apsmaäsm  mazdascä  °rasca  Y.  12.  5 ;
—  m/'aö/(Stverz.,  Sp.  1 19z  u.)  aAurö  mazdä spitamai  'rai:  ..  V./.iusw.;  —  pirssai (Stvcrz.,  Sp.997m.)  *rB  aAursm  mazäqm:  .. Yt/,  1  usw.;  — paiti  dim  (näml. aÄ»r3»i tnazdam)  pgrssat  (Stverz.,  Sp.  999  m.)  'rB: . . Yt  Ä  57  usw.;  V.5.43,  Nik.j;  —  aaiaoxta (Stveiz.,  Sp.  37  m.)  "rS:  .  . /ramrüioi  .  . aAura  mazda  Yt.  /.  S  usw. ;  —  nizbayar/uAa tu  'ra  *fraia!iin  mana yat  aAurahe  masdä .  .  vaxiim  tnl  asqsat  'rd  V.  ig.  i4f.;  — a  dim  ta  vaca  rämayat  aAurö  ma:d.l  .  . °r?m  V.5.  21;  — yimäi , .  paoiryB  masyä- nqm  apinse  az3m  yS  ahurS  mazda  anyB %wai  yat  'räi  V,  2.  a;  i;  —  V?*'  ^^^'^ mazda  -rai  frävavaca  /ra  'rö  gai^äbye astvaiiibyB  Y.  Ö5.  9;  7J.  14,  Vr.  2.  3;  — s.  noch  YtJ_j.  95  (Sp.  1673  o.); —  mi^rU zayäl  (Sp.  1659  o.)  'r7m  Y.g.  i  SüZ.;  — AaomB  upait  'r3m  atnm  pairi.yaohda'^mttm ..a  dim pirssai  'rö:  kö  narj  aAl . .?  äat . . paityaoxia  AaomB . . :  attm  aAmi  'ra  Aaomö
```


## [2026-09-06T02:23:03.852Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /1411 .pz.rn-/ {print \"LEAF=\"NR; print substr($0,1,1500)}' SOD_pages.txt | head -40",
 "description": "Find SOD leaf for entry 1411"
}
```


### [2026-09-06T02:23:05.464Z] TOOL RESULT

```
LEAF=121
       (o)pu sfarme                                                    1404 'pys^r =» ps»pr
       sexless                                                                                                                  ^Uaji ij>}^
                                                                       1405 >pysm B.
       SCE 356
                                                        V^LSi
                                                                            pism ? ©<*pasca-ima           =»pysm
                                                                            according to
 1392 >pw ymwn B
      (o)pu y(i)man                                                         BSTBL; STii, GMS 373, 7.15, 22; Benv. Notesii
      faultless                                                               215
       BSTBL, Vim. 3
                                                                      1406 'pystr'yck1 B                                    JJtw.»x/
 1393 >pw zn'kh B                               jbU t^h JjJj               opistarick (pystycyk)
                                                                           future
      (o)pu znak
      ignorant                                                              SCE 489, 494; BSTBL, Dhu. 250; GMS 373, 1013
      SCE 43; BSTBL, Vim. 185
                                                                      1407 >pystrw        B
1394 'pxyyr- =* pcyyr-                                                      opistar(u
```


## [2026-09-06T02:23:11.444Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7800,7830p' SOD_pages.txt",
 "description": "Print Gharib entry 1411"
}
```


### [2026-09-06T02:23:11.516Z] TOOL RESULT

```
     (to)adorn, (fo)ornatc                                                  VJ 788, 791, 900; GMS 373
     EGSii 15; AVS 110                                                1410 »pzVn      B
                                                                                                                       O^jXl i ji 0" <^>lju
1398 >py>stk B                                                             (o)pzarn =>ptzrn, pzrn
                                          j_y<^J
     opyaste Opy'sty) ©pp. =»py}t-, pysty(y), py>stk                       trouble, sorrow
     ornate                                                                 VJ 82, 126 etc.; GMS 957
      SCE 311, 523
                                                                      1411 'pz'rn-        B, S                   jj^ JL. O-^^ljl;
1399 'py'sty => }py>stk                                                    (o)pzarn       Opzrn-)    ©Av. zar-
1400 »pyc,t B                                        -w^jUj                (to)disturb
                                                                           VJ 1458
     (o)p(D)cat =>pcyt(y)
     time
                                                                      1412 »pz»t(h) M                                     ji*j»^'j
      BSTBL, Vim. 121; GMS 179; Benv. Et. Oss. 28                          opzat ©<*upa-zata           ©ob. -yy; ob. pi. ~yt
                                                           ^J'
                                                                  ^
1401 'pyk      M
                                                    kSJ>.S l^                =»pz}t
                                                                           homeland, birth place(/?/ace of origin)
      apik =>»pyk
      aquatic                                                              GMS 99; *pzVykw, Hen. BSOAS 11; Giants. 70.4
      BBB 512; GMS      394
                                                                      1413 >pzn\vty7h S                                   ^>iT<^Li
1402 'pysp'y       B                                                       (o)pzanautya
     opospay =»*pspy-, pspy-                               la~%            acquaintance
     rcjection                                                             GMS 1079; KG 403
     BSTBL, Vim. 204; Benv. Notesi 33
                                                                      1414 >pzrn- =¥ 'pz'rn-
1403 >pys   B                                          ju,^           1415 >PZY B,S                     (Oj^^^jj)(y>)^^<j
```


## [2026-09-06T02:23:23.389Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ortos",
 "prompt": "Give the reconstruction *ǵʰortos: its meaning, the root it comes from, and the list of descendants (Latin hortus, Proto-Germanic *gardaz, Greek khortos, Old Irish gort, etc.)."
}
```


## [2026-09-06T02:23:24.524Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/yard",
 "prompt": "Give the etymology of 'yard' (the enclosure sense): Old English geard, Proto-Germanic *gardan, PIE root, and any mention of garden, orchard, Latin hortus."
}
```


### [2026-09-06T02:23:25.066Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:23:30.517Z] TOOL RESULT

```
# Etymology of "Yard" (Enclosure)

The enclosure sense of "yard" traces back through several language layers:

**Old English:** From Old English *geard*, meaning "fenced enclosure, garden, court; residence, house."

**Proto-Germanic:** The Old English form derives from Proto-Germanic *\*gardan-*, whose ultimate origin remains uncertain.

**Proto-Indo-European:** Scholars propose a connection to PIE *\*gher-* (1), meaning "to grasp, enclose," with the sense of "enclosure" developing from this root meaning.

**Related Germanic terms** show the widespread nature of this word family: Old Norse *garðr* ("enclosure, garden, yard"), Dutch *gaard*, Old High German *garto*, and German *Garten* ("garden").

Notably, the page does not explicitly connect this word to Latin *hortus* or discuss orchard etymology, though it does document how "yard" expanded semantically over time—from a simple fenced area around a dwelling to enclosed spaces for various industrial, commercial, and institutional purposes.
```


## [2026-09-06T02:23:35.921Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0er-",
 "prompt": "List the senses of the reconstructed PIE root *ǵʰer- given on this page (there may be several homophonous roots), especially the one meaning 'to grasp, enclose', with its derived terms (*ǵʰortos, Greek khoros, Latin hortus, cohors)."
}
```


## [2026-09-06T02:23:37.157Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/court",
 "prompt": "Give the etymology of 'court': Old French cort, Latin cortem/cohortem, its analysis as co- + hort- (from PIE *gher- 'to grasp, enclose'), and the relation to hortus and to courtesy."
}
```


### [2026-09-06T02:23:41.424Z] TOOL RESULT

```
# Proto-Indo-European Root *ǵʰer-

Based on the Wiktionary entry, this reconstructed root has the following sense:

**Primary meaning:** "to take, get"

The page lists one main sense with this definition, though there's a cleanup notice indicating some ambiguity about notation and missing descendants.

## Key Derived Terms

The entry documents several descendants from this root:

- **\*ǵʰér-e-ti** (thematic present) → Sanskrit hárati ("to take, bear")
- **\*ǵʰor-ó-s** → Ancient Greek khorós ("dance ring")
- **\*ǵʰórtos** ("enclosure") - possibly related to Latin hortus and cohors

The page acknowledges scholarly uncertainty about the root's exact form and completeness, noting: "Why is this \*ǵʰ and not \*gʰ? References and explanations are badly needed."

The entry cites the *Lexikon der indogermanischen Verben* (Rix 2001) as its primary reference source.
```


### [2026-09-06T02:23:42.411Z] TOOL RESULT

```
# Etymology of "Court"

The word **court** traces back through Old French *cort* to Latin *cortem* (earlier *cohors*), meaning "enclosed yard." The Latin term combines the prefix *com-* ("with, together") and the stem *hort-*, related to *hortus* ("garden, plot of ground"), which derives from the Proto-Indo-European root *\*gher-* meaning "to grasp, enclose."

This physical sense of an enclosed space evolved to mean "those assembled in the yard; company, cohort," eventually extending to the royal assembly itself. The word entered English in the late 12th century as "formal assembly held by a sovereign," and subsequently developed both concrete meanings (palace, residence) and legal meanings (tribunal for judicial investigation).

The connection to **courtesy** is direct: the adjective *courteous* (c. 1300) derives from Old French *curteis*, literally "having court bearing or manners," reflecting how "medieval courts were associated with good behavior."
```


## [2026-09-06T02:23:49.943Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=chronic",
 "prompt": "Give the American Heritage Dictionary etymology for 'chronic' verbatim (Middle English, Old French, Latin chronicus, Greek khronikos, khronos)."
}
```


## [2026-09-06T02:23:55.266Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%CF%87%CF%81%CF%8C%CE%BD%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%CF%87%CE%BF%CF%81%CF%8C%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%B1%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0er-\" \\\n \"https://www.etymonline.com/word/curtain\" \\\n \"https://www.etymonline.com/word/court\" \\\n \"https://www.etymonline.com/word/yard\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 188, root Gher 1/Gherd (Nourai p.158): verification of khronos, khoros, Arabic qarn, Persian azordan, PIE *gher- 'grasp, enclose', curtain/court/yard\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T02:24:13.205Z] TOOL RESULT

```
# Etymology of "Chronic"

Based on the dictionary entry provided, the etymology is:

"[French _chronique_, from Latin _chronicus_, from Greek _khronikos_, of time, from _khronos_, time.]"

The entry traces the word's origins from Greek through Latin and French into English, showing that the root meaning refers to "time" itself.
```


### [2026-09-06T02:24:16.933Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/34cd7dd1b06ddb0f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ec6b6b3c383b128.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/46cc6c74c37c6286.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0406c07f217ed40.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/825619dc4ee57a3d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2b87a0758d8f3f0f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a2b2e2b8839da219.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5bf10f61602c0be.txt
```


## [2026-09-06T02:24:29.598Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT chorus/choir ===\"; grep -n \"^Chorus\\|^Choir\\|Chorus, a band\\|choir\" SKT.txt | head -8; echo \"=== SKT chronicle ===\"; grep -n \"^Chronicle\\|Chronicle,\" SKT.txt | head -5; echo \"=== SKT court ===\"; grep -n \"^Court,\\|Court, a yard\" SKT.txt | head -5; echo \"=== SKT curtain ===\"; grep -n \"^Curtain\\|Curtain,\" SKT.txt | head -5; echo \"=== SKT yard ===\"; grep -n \"^Yard\\|Yard (1)\\|Yard, an enclosure\" SKT.txt | head -5; echo \"=== SKT garden/orchard ===\"; grep -n \"^Garden\\|^Orchard\" SKT.txt | head -5",
 "description": "Grep Skeat for the English words"
}
```


### [2026-09-06T02:24:29.746Z] TOOL RESULT

```
=== SKT chorus/choir ===
3029:Carol,  a  song.  (P.  — C.)  Formerly,  a kind  oi  dance  —  O.  F.  catttU.  a  (singing) dance.  Of  Ccliic  oiigin :  cf.  Bret.  ^i>/i>?y. a  dance,  movement  of  the  body  m  cadence; Manx  carvai,  a  carol ;  Corn,  carol,  a  choir, concert;  W.  carol,  a  song,  c^vii,  to  mouT in  a  circle,  daace  i  Gad.  cmruU,  melody.
3121:choir.  (F.  -  L.  -  Gk.)  M.  E.  ckaitt, chsure.^O.  F.  chaiere,  cluiett.  —  Low  L. cathedra^  a  throne,  raised  seat*  chair ;  see al.ove.
3414:Choir ;  see  Chortu.
7863:—  Low  l^gntdmilis,  only  in  neut. a  service  book  of  porlloas  sung  in i,e.  on  the  steps  (of  the  choir).— L. a  step.
22971:choir— chorus,  quire  1
=== SKT chronicle ===
20233:Troy-weight.  (F.  a/iJ  E.)  Orig.  a wcii^'ht  used  at  the  fair  of  Troyes,  a  town in  Frnuce,  S.  E.  of  Paiis.  See  Arnold's Chronicle,  ed.  181 1,  pp.  108,  191 ;  Haydn, Diet,  of  Dates,  &c.
=== SKT court ===
=== SKT curtain ===
4581:Curtain :  see  Court.
=== SKT yard ===
21736:Yard  (I  X  an  enclosed  space.  (E.)  M.  E. fn/,  A.  S.  gtard,  an  enclosure,  court. 4- [cd-  jpB'*'*  ^whence  E.  ^ariJk),  Dan.  UtL «?  Swcd.  ^n/,  G.  ^rtem,  a  garden  ; toss,  gprwf,  a  town ;  L.  kortus,  a  garden  ; 3k.  x^^fi^"*  ■  court  yard.  p.  The  Aryan bnn  U  G  HART  A,  liL  'a  place  sur- oonded  or  enclosed.'  (^GHAR.  to keixc:,  enclose.)  Allied  to  Oird  (i ). Doufaletl,  garden,  garth*  Dot,  court' fsrt/,  orchard  (  =  tvcrtyard). Yard  (a),  a  rod.  36  inches,  cross-bar  on ft  mast.  (E,)  M.  E.  lenU,  y^nte,  a  stick, tod.  A-  S,  gyrti.  ^ird.  a  nxl.+Du.  garde^ a  twig.  rod.  G.  gtrtt,  a  switch.  Allied  to 0.  M  G.  gart,  led  gaddr,  Goth,  gaids,  m {oad.
=== SKT garden/orchard ===
```


## [2026-09-06T02:24:40.462Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT Chorus ===\"; grep -n \"Chorus\" SKT.txt | head -8; echo \"=== LEW hortus ===\"; grep -n \"^hortus\\|hortus,\" LEW_1910.txt | head -6; echo \"=== LAT hortus ===\"; grep -n \"hortus\" LAT.txt | head -6; echo \"=== SYN garden ===\"; grep -n \"GARDEN\\|7\\.53\" SYN.txt | head -8",
 "description": "Grep Skeat chorus, Latin dicts, Buck"
}
```


### [2026-09-06T02:24:40.561Z] TOOL RESULT

```
=== SKT Chorus ===
=== LEW hortus ===
=== LAT hortus ===
12844:Y. hortus.
27495:qui se trouye dans hortus et cohors (v. cea aots); le sena serait
27761:nusquam nominatur uilla, semper in significatione ea hortus, in horti
28537:hortus, -i n. (ortus)’, enclos, propri 4 t 4 close de inrs (cf. la
28550:hortus, entre aatres, a et 4 concurrenc 4 par le aot geraaniqne, v.sax.
28551:gardo, etc. (peat-etre Etymologiqueaent apparente k hortus ), dont le
=== SYN garden ===
12313:8.13 GARDEN Grk. —xijwos Goth. aurtigards Lith. darzas NG kijwos, weptBodt ON -gardr Lett. darzs Lat. —horlus Dan. have ChSl.  vrittit, vriitogradit It. giardino; orto Sw. trddgdrd (ogradit) Fr. jardin OE ortgeard, wyritin SCr. ort, baSta Sp. jardin, huerta ME _ garden, orchard Boh.  zahrada Rum. grddiné NE gardin Pol. ogréd Ir. lubgort, garda Du. luin Russ. sad, ogorod Nir. garrdha, gairdin OHG  garto Skt. —-vatika-, udyana- W. gardd MHG arte Av. (pairidaéza-) Br. liorz NHG garten
```


## [2026-09-06T02:24:43.302Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '28537,28560p' LAT.txt; echo \"=== SYN 8.13 body ===\"; sed -n '12313,12360p' SYN.txt | head -40",
 "description": "Ernout-Meillet hortus and Buck garden"
}
```


### [2026-09-06T02:24:43.391Z] TOOL RESULT

```
hortus, -i n. (ortus)’, enclos, propri 4 t 4 close de inrs (cf. la
citation de Pline 19,50 s.u .hSrSs, et le sens da coapos 4 cohors ),
pais "jardin". Qaelquefois, d' aprfes le gr.xfjtroc, d 4 signe le pudendum,
muliebre. - Ancien, asael. Panroaan, sanf roaaain. M.L.4194; peut-
fctre got. aurtigards ; angi, orchard.
Derives et coapos 4 s: hortulus a., d'ou hortuld,-dnis', hortilio CGL
V 601,35; hortllia, M.L.4193; hortellus, horticellus; hortuldnus ;
hortudlis (Ps.Apal.), hortSnsis, M.1.4193, et hortSnsius (Pline),
horticola ; hortlnus', hortua,-Urum n .pl. ,tardif, d'aprbs pascua ?
Poar les noas propres Hortensius et Hortalus, v. Schnlze, Lat.Higenn.
p.176 et s. V. aussi cohors.
Hortus seni est conservi d'nne fagon gen« 5 rale dans les 1 . roaanes;
les derives ne snrvivent que dans des dialectes isol 4 s; en frangais,
hortus, entre aatres, a et 4 concurrenc 4 par le aot geraaniqne, v.sax.
gardo, etc. (peat-etre Etymologiqueaent apparente k hortus ), dont le
d 4 rive fr. jardin a 4 t 4 eaprante par 1'italien, 1'espagnol et le por-
tngais.
Cf. osq. hurz, hurtum "enclos sacr 4 " (dans la d 4 dicace d'Agnone);
cf. ^opTOC "enceinte (de conr, de bergerie)"; peut-Stre iri. gort "chaap",
lub-gort ",jardin". Lat. co-hors repose sans do ut e sar co-hortis, de
*-ghrti- ; gall.garth "jardin", bret. garz "haie" supposent *ghrta.
Comme ane racine *ghert- est impossible en indo-europ 4 en, on est
amen 4 k rapprocher la racine de osq. heriiad "capiat", skr .hdrati
"il prend" (intensif jarlharti), et de gr.)(ei,p "main", ara. jern et
=== SYN 8.13 body ===
8.13 GARDEN Grk. —xijwos Goth. aurtigards Lith. darzas NG kijwos, weptBodt ON -gardr Lett. darzs Lat. —horlus Dan. have ChSl.  vrittit, vriitogradit It. giardino; orto Sw. trddgdrd (ogradit) Fr. jardin OE ortgeard, wyritin SCr. ort, baSta Sp. jardin, huerta ME _ garden, orchard Boh.  zahrada Rum. grddiné NE gardin Pol. ogréd Ir. lubgort, garda Du. luin Russ. sad, ogorod Nir. garrdha, gairdin OHG  garto Skt. —-vatika-, udyana- W. gardd MHG arte Av. (pairidaéza-) Br. liorz NHG garten
‘Garden’ is often a specialization of ‘yard’, and several of the words entered here belong to groups already discussed under that head (7.15). Most of the others are from a similar notion of ‘en- closure’. There may be specialization of ‘garden’ to ‘flower garden’, ‘vegetable garden’, or ‘tree garden, orchard’. A converse generalization is seen in Sy. trédgdrd, lit. ‘tree-garden’.
1, Grk. fos, Dor. xazos : OHG huoba, ‘piece of land’ (NHG hufe, hube), Alb. kopsht ‘garden’, root connection? Walde-P. 1.345 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
NG zepiBdd, fr. dim. of Grk. zepl- BoXos ‘circuit, enclosure’ : repiBaddw ‘sut- round, put about’.
2. Lat. hortus (> It. orto ‘vegetable garden’, Sp. huerto ‘orchard’, huerta ‘vegetable garden’), Osc. hirz ‘hortus, lucus’ : Lat. cohors ‘yard, court’, Grk. xépros ‘farmyard’, Ir. gort ‘field’, lub-gort ‘garden’ (cpd. with Iuib ‘plant’), Br. liorz ‘garden’ (by contraction, cf. MCorn. lowarth id., Pedersen 1.116), prob. also OE geard ‘yard’ (7.15), OHG garto ‘garden’, ete. (below, 4), all as orig. ‘enclosure’ fr. IE *gher- in Ose.
et a ee
(pe ld’, etc. hr- ‘seize, hola, Ernout-M. 461.
no, Sp. jardin _a North Fr. NE garden) fr.
<i er d nN CP ig ME garain, 4), REW
arto ‘garden’ (below,
fain, fr. Slavic (below, 6). ed 4 ee liorz, see above, 2. ae INIT. garrdha, W. gardd, fr. : 4). Pedersen 1.110. _NE garden. 4, In Gme. mostly words for ‘yard’, ‘, epds. ON -gardr, as In NT an ' (NIcel. gardur jlgrtr ‘cabbage garden’ (Nce gar slone ‘garden’) ; Goth. aurtigards, O orlgeard, MIE orchard (OB, ME also and NE only ‘orchard’), first part prob. old loanword fr. Lat. hortus (Feist 68, Sten- der-Petersen 370 f.; otherwise, namely : Goth. waurts ‘root’, OE wyrt ‘plant’, Walde-P, 1.288, Falk-Torp 1336); Sw. fradgérd, epd. with trdd ‘tree’, and so orig. ‘a pleasure garden with trees, park’, like the NHG lustgarten (Hellquist 1233); OHG garto, MHG garte, NHG garlen (with the loanwords Fr. jardin, NE garden, ete.); all: Goth. gards ‘house, court,’ OR geard ‘yard’, etc., and Ptob,, fr. the same root as Lat. hortus, tle, See above, 2 and 7.15. yi Se hy dn in piece of bras pee edeed orp 386, (NE haw), ete. Falk- OF = lin eee ie of wyrt ‘plant’? and » also Du. tuin ‘garden’ :
5. Lith, goo Walde-P. 1.778,
ptccoua, « hreumference, border’, Grk ald 8tasp’, ete, (th : e-P. 07: € group in
1 but transposition fr.
AGRICULTURE, VEGETATION
Digitized by Arya Samaj Foundation Chennai and eGangotri
491
*Zardas is preferred, 1.859). Muhl.- Endz. 1.449. Trautmann 45 (: ON draga ‘draw’).
6. For the various ChSl. renderings of kios, cf. Jagié, Entstehungsgesch. 330, 428.
ChSI. vriitogradi, loanword fr. Goth. aurtigards (above, 4).
ChSI. vriitz, SCr. vrt, either abstracted fr. the preceding (Miklosich and others), or fr. a Goth. simplex. Stender-Peter- sen 371.
Late ChSI. ogradt, Pol. ogréd, Russ. ogorod (‘vegetable garden’), Boh. zahra- da, epds. of ChSl. gradii, ete. ‘city’ (19.15), reflecting an earlier meaning ‘enclosure’, regardless of whether or not this is a loanword fr. the Gmc. group (above, 4). Late ChSl. and Bulg. also deriv. gradina ‘garden’ (> Rum. grdd- ind). Berneker 330.
Russ. sad (Pol. sad ‘orchard’, Boh. sad ‘park, orchard, plantation’) = ChSl. sadi ‘plant, tree, shrub’ (late also for kfimos), fr. vb. saditi ‘plant’ : Skt. sad- aya-, Goth. satjan ‘set’, caus. of IE *sed- ‘sit’. Trautmann 258 f.
SCr. baséa fr. Turk. bahce ‘garden’ (orig. Pers.). Berneker 39. Lokotsch 169.
7. Skt. vatika-, vataka-, fr. vdta- ‘en- closure, enclosed piece of land’ : vrti- ‘hedge, fence’, vr- ‘cover, surround’, etc. Uhlenbeck 281 (Walde-P. 1.281 without valika-, etc.).
Skt. udydna-, udydnaka-, esp. ‘pleas- ure garden, park’, fr. ud-ya- ‘go out’, epd. of yd- ‘go, walk’.
Av. pairidaéza- ‘hedged-in place’, perh. ‘garden’ (cf. NPers. paléz ‘garden’, and loanwords Grk. rapédeoos, Arm. partéz ‘enclosed garden’) : pairi-daézaya- ‘wall about’, Skt. déhi-, Grk. retxos
‘wall’, etc. (7.27). Walde-P. 1.833. Barth. 865.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
if " “1 fi
ie NL ne ee? eo peas Ee leh mn a ee eons
Digitized by Arya Samaj Foundation Chennai and eGangotri
492 SELECTED INDO-EUROPEAN SYNONYMS
8.14 BARN
K troBohdy, &roFnK Goth. bansts Lith. — darziné, skuné Se La A hte ON hlada Lett. Sk'unis Lat. horreum, grandaria Dan, lade ChSI. Zittnica It. granaio Sw. ada SCr. —Stagelj, 2ilnica, ambqy ry. grenter, grange OE berern, beren Boh, stodola Sp. granero ME bern Pol. stodola Rum. surd, hambar NE barn Russ. Zitnica, ambar Tr. saball Du. schuur : Skt. kugila- Nir. _ sciobal OHG | sciura, scugin, stadal Av. yavan- W. ysgubor MHG schiur(e); schiune, Br. granch stadel
NHG - scheune, scheuer (stadel)
Words for ‘barn’, as a storehouse for grain or other farm produce, are partly specializations of ‘storehouse’ and partly from words for ‘grain’ (or some particu- lar kind of grain, as ‘barley’ in the case of NE barn). But since the farmer’s barn may also be the place where the farm animals are kept, there is some- times confusion with the notion of ‘stable’. So a few of the words for ‘barn’ probably rest on this latter no- tion (Goth. bansts, Ir. saball). Con- versely in NE barn in U.S. usage the secondary association with the place where the cattle and horses are kept is so strong that in the country it is the common word covering ‘stable’, and it is by this analogy (rather than the no- tion of ‘storehouse’) that one uses car barn of the place where street cars stand when not on their run.
Some of the words included in the list denote any storage place for grain, with no resemblance to our barn, for which there may be no good equivalent.
1. Grk. dzofjxn ‘storehouse’ in gen- eral, including one for grain (as reg. in NT, Mt. 6.26, ete.), fr. dmoriOnue ‘put away, store up’, epd. of ri@nuc ‘put,
```


## [2026-09-06T02:24:55.951Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN chorus ===\"; grep -n \"^chorus, n\\|^choir, n\\|^curtain, n\" KLN_1971.txt | head; echo \"=== IEC ghort ===\"; grep -n \"ghortos\\|ghorto-\\|ghr̥t\" IEC.txt | head -6",
 "description": "Klein chorus/choir/curtain, Mann ghortos"
}
```


### [2026-09-06T02:24:56.025Z] TOOL RESULT

```
=== KLN chorus ===
46217:chorus, n. — L., fr. Gk. yopop, ‘dance in a ru g, 
62080:curtain, n. — ME. cor tin, fr. OF. cor tine, cur tine, 
=== IEC ghort ===
4825:ghordhos, is 'fortified place, walled en- closure’. WP I, 608. Cf. ghortos Hindi garh ‘castle’, beside ghar ‘house’; Alb. gardh, pl. gjerdhe, m. ‘fence’; Go. gards, Lat. “house, family, yard; OCS gard ‘house’; OE geard ‘fence, yard’; ON garór ‘yard, fence, house, fort’; OCS gradü, id. and com. Sl.; R gòrod ‘town’; Li. gařdas ‘paddock; walled town’; gardis, gs -iés ‘grating, grille’, Finn. LW cf. kartano “yard, farm’; Thrac. cf. place- name Gordium; z-gde in Skt. grháh ‘house’
4828:ghoros (1) ‘enclosure, envelope’. Cf. ghortos Skt. *ghar- ((house', in ghar-inih ‘female house-owner'; Hind. Sind. ghar, Romani kher, id.) Myc. koro- (queried: “circle?); Gk. khorós *dancing-place'; khórion ‘skin, pod, caul’; Lat. (?) horia *fishing-smack'; OE gear (*millrace? or dam") (FH: AEEW)
4843:ghortos, is, us ‘enclosure’. Cf. ghordhos, ghoros. WP I, 603 Skt. cf. ghattah (“quayside landing’, fr. *ghor- tios); Tokh. B kerciye ‘palace’; Hitt. cf. gur- tan, acc. (‘citadel’, for *kurta-?); Gk. khór- tos “pen, enclosure'; Lat. hortus “garden, village" beside cohors, -hortis (1) "back yard’; LLat. cf. hortua ‘fences’; Osc. húrz, ds hürtüí ‘garden’; Olr. gort ‘battlefield’; MIr. & Mod. gort, m. ‘field, garden’; Gaul. gorto-; Br. cf. li-orz ‘herb-garden’
```


## [2026-09-06T02:24:57.729Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FVQ qarn ===\"; grep -n -i \"qarn\" FVQ.txt | head -8; echo \"=== AFM qarn ===\"; grep -n \"( قرن )\\|«قرن»\" AFM_pages.txt | head -5; echo \"=== KLN qarn/chronos->arabic ===\"; grep -n -i \"Arab. qarn\" KLN_1971.txt | head -5",
 "description": "Check Semitic refs for qarn"
}
```


### [2026-09-06T02:24:57.828Z] TOOL RESULT

```
=== FVQ qarn ===
=== AFM qarn ===
=== KLN qarn/chronos->arabic ===
```


## [2026-09-06T02:25:05.434Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '46212,46240p' KLN_1971.txt; echo \"=== curtain ===\"; sed -n '62080,62100p' KLN_1971.txt",
 "description": "Klein chorus and curtain entries"
}
```


### [2026-09-06T02:25:05.531Z] TOOL RESULT

```
(with a certain topic)’. See -logy. 

Derivatives: chorolog-ical , adj,, chorolog-ist, n. 
chortle, intr. and tr. v. and n. — A blend of 
chuckle and snort; coined by Lewis Carroll 
chorus, n. — L., fr. Gk. yopop, ‘dance in a ru g, 
festive dance, dance; band of dancers; chorus, 
choir; troop, band; place for dancing’. The first 
meaning was prob. ‘an enclosed place for danc- 
ing*, from I.-E. base *gher-, ‘to seize, take, hold, 
dose, envelop’, whence also Gk. xetp, ‘hand’, 
X^pTOG, ‘feeding place, courtyard*. See chiro- 
and cp. words there referred to. Cp. also choir, 
quire, chorea, choreus, the first element in carol 
and in choragus and the second element in 
Terpsichore. 

Derivatives: chorus , v., chorus-er, n. 
chose, past tense of choose. — ME. choos, formed 
on analogy of the pp. chosen. See chosen, 
chose, n., thing, property (used in the legal terms 
chose in action , chose in possession). — F. chose, 
‘thing’, fr. L. causa, ‘cause, reason’, in Late L. 
also ‘thing’. Cp. OProven$. cauza. It., Sp. cosa , 
Port, cousa, ‘thing’, which all derive fr. L. 
causa in its Late Latin sense, and see cause, 
chosen, pp, of choose. — ME. chosen , fr. OE. 
coren ; influenced in form by choose, 
cbou, n., an ornamental ribbon or knot in wom- 
=== curtain ===
curtain, n. — ME. cor tin, fr. OF. cor tine, cur tine, 
‘curtain’ (whence F. courtine , ‘fortified curtain’), 
fr. Eccles. L. cortina , ‘curtain’, rendering of Heb. 
y*rf*d* (Ex. 26:1 and passim) by the Vulgate. 
Eccles. L. cortina derives fr. L. cohors, edrs , 
‘court’ (see court), and is prop, a loan translation 
of Gk. auXouoc, ‘curtain’ ( = the Septuagint ren- 
dering of Heb. y*rV& h , see above), fr. Gk. auXVj, 
‘court, courtyard’. 

Derivatives: curtain, tr. v., curtain-ing, n. 
curtal, n., having the tail docked, curtailed (ob- 
sol.) — OF. cortald, courtald (F. courtaud ), 
‘docked, thick-set’, a hybrid formed with the 
Teut. suff. -aid fr. L. curtus, ‘short’. See curt 
and cp. curtail. Cp. also It. cortaldo, which is 
of the same origin and meaning as OF. cortald. 
Curtana, n., the pointless sword borne before 
English sovereigns at their coronation. — ML. 
curtana (scil. spdda), ‘a short sword*, fr. L. 
curtus, ‘short’. See curt.
```


## [2026-09-06T02:25:18.928Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%B1/",
 "prompt": "In the فرهنگ معین section, what does it say for the entry کر meaning آواز دسته‌جمعی (chorus)? Give the origin tag / foreign original form printed (e.g. Fr. chœur), verbatim."
}
```


### [2026-09-06T02:25:23.899Z] TOOL RESULT

```
Based on the فرهنگ معین section, the entry for کر meaning "آواز دسته جمعی" (chorus) shows the origin tag as:

**(کُ رْ ) \[ فر. \]**

This indicates the origin is French (فر. = فرانسوی), though the specific French original form is not explicitly printed in this dictionary entry.
```


## [2026-09-06T02:26:12.524Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 188 -l 188 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg188 && ls -la pg188.png",
 "description": "Render PDF page 188"
}
```


### [2026-09-06T02:26:14.847Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60458 Sep  5 22:26 pg188.png
```


## [2026-09-06T02:26:16.891Z] TOOL CALL #58: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg188.png"
}
```


### [2026-09-06T02:26:17.467Z] TOOL RESULT

```

```


## [2026-09-06T02:26:17.464Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:26:31.855Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T02:26:31.920Z] TOOL RESULT

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


## [2026-09-06T02:26:33.992Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://ahdictionary.com/word/search.html?q=chronic\" \"https://abadis.ir/fatofa/%DA%A9%D8%B1/\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 188, root Gher 1: AHD etymology of 'chronic'; Mo'in's entry for Persian کر [فر.]\" 2>&1 | tail -2; done",
 "description": "Archive remaining sources"
}
```


### [2026-09-06T02:26:36.560Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c137f9717acf5520.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14fbb08d4b0f465b.txt
```


## [2026-09-06T02:34:00.835Z] TOOL CALL #61: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-188.json <<'JSONEOF'\n{\n  \"pdf_page\": 188,\n  \"book_page\": 158,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gher 1, Gherd; Ghordho\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰer- 'to grasp, enclose' (Pokorny 442-443 gher-4 'to gripe, grab, enclose'), with the extension *ǵʰerdʰ- and the noun *ǵʰórtos / *ǵʰordʰos 'enclosure, yard, garden' (Pokorny 444 gherdh-)\",\n      \"note\": \"The root box is correct in all three parts and the two page numbers are exactly right. Pokorny's fourth gher- occupies pp.442-443 and is glossed 'to gripe, grab, enclose' (Gk. khórtos 'enclosed feeding-place', Lat. hortus, cohors, Skt. harati 'takes'); the derived noun family stands on p.444 under gherdh- 'to encircle, enclose', with *ǵʰordʰos > Goth. gards, OE ġeard, OCS gradŭ. Watkins in the AHD appendix condenses exactly this pair into one article — 'gher-1. To grasp, enclose; with derivatives meaning \\\"enclosure\\\" … [Pok. 4. gher- 442, gherd- 444.]' — the identical two pages Nourai cites, which is a strong sign he built this chart directly from Watkins. Nourai's split of the gloss (Gher/Gherd = the verb 'to grasp, enclose'; Ghordho = 'an enclosed land, yard, garden') matches Pokorny's own division between the verbal root and the *ghordho-s noun. One caveat that belongs on the chart and is missing: Pokorny explicitly says it 'is not to be decided' whether Gothic garda / OHG garto go back to *ghor-to- or *ghordho-, so the two branches Nourai draws from the same box are in reality a single unresolvable doublet. The chart's real problems are not in the root box but in two branches hung under it: the Iranian zar- 'to harm' family (nodes 1-3), which Nourai's own reference Walde-Pokorny I 603 explicitly REMOVES from this root, and Greek khrónos (node 9), which Klein assigns here but Beekes calls of unknown origin.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ǵʰer- «گرفتن، در بر گرفتن، محصور کردن» و اسمِ برگرفته از آن *ǵʰórtos / *ǵʰordʰos «جای محصور، حیاط، باغ» واقعی است و هر دو ارجاع نورایی دقیق است: پوکورنی در صفحات ۴۴۲–۴۴۳ مادّهٔ چهارم gher- را با معنای «گرفتن، در بر گرفتن» آورده (با یونانی khórtos، لاتینی hortus و cohors، سنسکریت harati) و در صفحهٔ ۴۴۴ گسترشِ gherdh- «حصار کشیدن» را. واتکینز در پیوست فرهنگ American Heritage همین دو صفحه را در یک مدخل «gher-1. To grasp, enclose» جمع کرده است، چنان‌که پیداست نورایی نمودار را از همان‌جا ساخته. ایراد کار نه در خودِ ریشه، بلکه در دو شاخه است: خانوادهٔ ایرانیِ zar- «آزردن» (گره‌های ۱ تا ۳) که والده-پوکورنی در همان صفحهٔ ۶۰۳ که نورایی به آن ارجاع می‌دهد صریحاً آن را از این ریشه بیرون می‌گذارد، و یونانی khrónos (گرهٔ ۹) که کلاین اینجا می‌نشاند ولی بیکس آن را بی‌ریشهٔ شناخته می‌داند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰer-\",\n        \"https://www.etymonline.com/word/yard\",\n        \"https://www.etymonline.com/word/court\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:442\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: gher-4 / Meaning: to gripe, grab, enclose … gr. χορτος m. \\\"enclosed place\\\" … Latin cohors \\\"fenced courtyard\\\" from *co + IE *ghrtis, in ablaut to hortus \\\"garden as fenced place\\\" … References: WP. I 603 f. … Page(s): 442-443'. The lemma begins on p.442, so POK:442 is exact.\"},\n        {\"ref\": \"POK:444\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Meaning: to encircle, enclose … Note: because of Latin hortus (see gher-4) extension from *gher-4 … Gothic gards m. \\\"house\\\", Old Icelandic garðr \\\"fence, paddock, courtyard\\\", Old English geard … Slavic *gordъ … References: WP. I 608 f. … Page(s): 444'. This is Nourai's 'Gherd; Ghordho'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gher-1\", \"stance\": \"supports\", \"note\": \"'gher-1. To grasp, enclose; with derivatives meaning \\\"enclosure.\\\" … 2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure … b. Latin hortus, garden: HORTICULTURE, ORCHARD … 3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- in Latin cohors … COURT, COURTEOUS, (COURTESY) … 4. Perhaps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground … [Pok. 4. gher- 442, gherd- 444.]' — Nourai's root box and his page citations reproduce this article.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I 603 f. (gher-4) and 608 f. (gherdh-)\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt line 57210: '4. gher- \\\"greifen, fassen, umfassen, einfassen\\\"', with 'gr. χορτος eingehegter Platz, Hof, Weideplatz', 'lat. cohors \\\"Hofraum, Gehege, Viehhof\\\", hortus \\\"Garten\\\"', 'ir. gort \\\"seges\\\", cymr. garth \\\"Pferch, Hürde, Gehege\\\"'.\"},\n        {\"src\": \"IEC\", \"where\": \"s.vv. ghordhos, ghoros (1), ghortos\", \"stance\": \"supports\", \"note\": \"Mann: 'ghortos, is, us \\\"enclosure\\\". Cf. ghordhos, ghoros. WP I, 603 … Gk. khórtos \\\"pen, enclosure\\\"; Lat. hortus \\\"garden\\\" beside cohors, -hortis \\\"back yard\\\"; Osc. húrz … Olr. gort'; and 'ghoros (1) \\\"enclosure, envelope\\\" … Gk. khorós \\\"dancing-place\\\"'.\"},\n        {\"src\": \"SYN\", \"where\": \"8.13 GARDEN, p.491\", \"stance\": \"supports\", \"note\": \"Buck: 'Lat. hortus … : Lat. cohors \\\"yard, court\\\", Grk. khórtos \\\"farmyard\\\", Ir. gort \\\"field\\\", lub-gort \\\"garden\\\" … prob. also OE geard \\\"yard\\\", OHG garto \\\"garden\\\", etc., all as orig. \\\"enclosure\\\" fr. IE *gher- … \\\"seize, hold\\\".'\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. hortus\", \"stance\": \"supports\", \"note\": \"'hortus, -i m. … enclos, propriété close de murs … puis \\\"jardin\\\" … Lat. co-hors repose sans doute sur co-hortis, de *-ghrti- … on est amené à rapprocher la racine de osq. heriiad \\\"capiat\\\", skr. hárati \\\"il prend\\\" … et de gr. χείρ \\\"main\\\".'\"},\n        {\"src\": \"SKT\", \"where\": \"s.v. Yard (1)\", \"stance\": \"supports\", \"note\": \"Skeat: 'Yard (1), an enclosed space … L. hortus, a garden; Gk. χορτος, court-yard. β. The Aryan form is GHARTA, lit. \\\"a place surrounded or enclosed.\\\" (√GHAR, to seize, enclose.) … Doublets, garden, garth. Der. court-yard, orchard.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"zar 1 : to harm; â-zâr : harm; âzâra : oppressed\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Iranian words themselves are real and correctly glossed, but the arrow from the 'grasp, enclose' root is wrong. Bartholomae (AiW col. 1669 f.) has 'j., g. zar- V. \\\"erzürnen\\\"', present stems zaraṇu-, zaran-, zaranya-, iterative zāraya-, perfect zazar-, ppp. zarəta-; with the preverb ā-: mā āzārayōiš zaraθuštrahe 'do not offend Zarathushtra' (FrD 4), anāzarəta- 'not offended', āzārayeinte (Yt 13.30), and he equates the root outright with Skt. hṛṇīte 'is angry' and NP āzurdan. The noun form Nourai writes 'âzâra' is Av. āzara- 'Bedrückung' (i.e. 'oppression', not 'oppressed'; the participle 'oppressed, offended' is āzarəta-), a form Walde-Pokorny quotes from Justi's Handbuch p.148. There is no Old Persian attestation at all, so the box label 'Avestan / Old Persian' overreaches. Decisively, Nourai's own reference Walde-Pokorny I 603 prints this family inside a parenthesis of EXCLUSION at the head of the gher- 'greifen, fassen' article: '(Av. zara-, āzara- \\\"Bedrückung\\\" … gehört ebenso wie *āzarəta in anāzarəta \\\"nicht erzürnt\\\" … zu ai. hṛṇīte, vgl. np. āzurda \\\"gekränkt\\\" und āzurdan \\\"kränken\\\": siehe Hübschmann Pers. Stud. 6, 146.)' — i.e. Walde-Pokorny says these words do NOT belong to this root. Cheung (2007) sets them up as an independent Proto-Iranian *zarH1 'to hurt, wound, anger' and states flatly 'No precise IE cognates of this Iir. root are attested.' The prefix ā- is the Old Iranian preverb ā- (Skt. ā), not Nourai's 'Apo' (*apo 'off, away'), whose Iranian reflex is apa-.\",\n          \"derivation_fa\": \"خودِ واژه‌های ایرانی درست‌اند، ولی پیوندشان به ریشهٔ «گرفتن، محصور کردن» نادرست است. بارتولومه (ستون ۱۶۶۹ به بعد) ستاک اوستایی zar- «خشمگین کردن، آزردن» را با ساخت‌های zaranya-، zāraya- و اسم مفعول zarəta- ثبت کرده و با پیشوند ā-: mā āzārayōiš zaraθuštrahe «زرتشت را میازار» و anāzarəta- «نیازرده»، و آن را یکسر با سنسکریت hṛṇīte «خشم می‌گیرد» و فارسی نوِ آزردن برابر نهاده است. صورتی که نورایی «âzâra» نوشته همان āzara- اوستایی به معنی «آزار، ستم» است (نه «آزرده»؛ صفت مفعولی āzarəta- است). هیچ گواهی پارسی‌باستانی در کار نیست، پس برچسب «اوستایی / پارسی باستان» بیش از اندازه است. مهم‌تر آنکه والده-پوکورنی در همان صفحهٔ ۶۰۳ که نورایی به آن ارجاع می‌دهد، این خانواده را در پرانتزی جدا می‌کند و می‌گوید که به ریشهٔ «greifen, fassen» تعلق ندارد بلکه با سنسکریت hṛṇīte هم‌ریشه است و به هوبشمان، مطالعات فارسی، صفحهٔ ۶ ارجاع می‌دهد. چونگ نیز آن را ریشهٔ مستقلِ ایرانی *zarH «آزردن، خشمگین شدن» می‌داند و تصریح می‌کند که هیچ هم‌ریشهٔ دقیق هندواروپایی برایش گواهی نشده است. پیشوند ā- هم پیشوند فعلیِ ایرانی باستان است، نه *apo که نورایی ارجاع می‌دهد. نتیجه: پژوهش امروزی این شاخه را از این ریشه بیرون می‌گذارد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/آزردن\"],\n          \"ref_check\": [\n            {\"ref\": \"WLD1:603\", \"status\": \"contradicts\", \"note\": \"WLD_Bd1_pages.txt, gher-4 article: '(Av. zara-, āzara- \\\"Bedrückung\\\", die Wackernagel I 248 zu har- stellt … es gehört ebenso wie *āzarəta in anāzarəta \\\"nicht erzürnt\\\" … zu ai. hṛṇīte, vgl. np. āzurda \\\"gekränkt\\\" und āzurdan \\\"kränken\\\": siehe Hübschmann Pers. Stud. 6, 146.)' — the very page Nourai cites removes these words from the root he hangs them on.\"},\n            {\"ref\": \"HRN:6\", \"status\": \"partial\", \"note\": \"Horn, Grundriss p.6 no.20: 'āzār \\\"Leid\\\", āzārden, āzāris; āzerden, āzerm. — aw. ā + √zar-, āzārayeiti \\\"sie peinigen\\\"; phlv. āzār, āzārtan etc.; ai. √har- \\\"zürnen\\\".' Horn gives the Iranian chain and the Sanskrit comparison but no IE root, and certainly not *gher- 'enclose'.\"},\n            {\"ref\": \"HUB:6\", \"status\": \"partial\", \"note\": \"Hübschmann, Persische Studien p.6 (note on Horn no.20): 'Füge hinzu: np. āzarda = zd. āzarəta- \\\"beleidigt\\\". Sal. Shuk. geben freilich āzurdan \\\"kränken\\\" für Vullers' āzardan. Dazu stimmt afgh. LW. āzurda \\\"afflicted, sad\\\".' Supports the Iranian equation only.\"},\n            {\"ref\": \"FFD:25\", \"status\": \"partial\", \"note\": \"Abolghasemi, Fe'lhā-ye Fārsi-ye Dari, printed p.۲۵ (FFD_pages.txt [pdf page 30]): 'آزاردن / آزارد ← فارسی میانه āzārd- < ایرانی باستان *ā-zār-aya-. ā پیشوند فعلی است … zār ریشه است به معنی «تحریک کردن» و aya پسوند است. آزار ← فارسی میانه āzār < ایرانی باستان *ā-zāra-.' The cited page is exactly right for the Old Iranian → Middle Persian chain, and is silent on any IE root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1669 f., s.v. zar-\", \"stance\": \"supports\", \"note\": \"'j., g. zar- V. \\\"erzürnen\\\", Praes. … 30 (Iter.) zāraya-; Perf. zazar-. — PPfP. zarəta- … mit ā … mā āzārayōiš zaraθuštrahe … anāzarəta … āzārayeinte Yt.13.30 … ai. hṛṇīte; np. āzurdan.' Confirms the Avestan verb and its Persian continuation — and its Indic, not 'enclosure', comparison.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 469-470, s.v. *zarH1\", \"stance\": \"contradicts\", \"note\": \"'*zarH1 \\\"to hurt, wound, anger\\\". *AVESTAN: zar- \\\"to hurt, wound\\\" || (+ *ā-) \\\"to hurt, wound, offend\\\" … *MIDDLE PERSIAN: (+ *ā-) MMP ʾzʾr-, BMP /āzār-/ … *SANSKRIT: har \\\"to be angry\\\" (RV+) … ⊗ No precise IE cognates of this Iir. root are attested.'\"},\n            {\"src\": \"PHD\", \"where\": \"p. 15\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'āzār [ʾcʾl | N ~] torment. āzardan [ʾcʾltn! | M ʾzyrdn] = āzārdan. āzārdan, āzār- [ʾcʾl-tn! | N ~] torment, injure.' The Middle Persian link Nourai's chart skips.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"âzâr «آزار ( آزارش )»; âzordan «آزردن ( آزاردن ، آزرده )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge Avestan → Persian is right, even though the root above it is not. Old Iranian *ā-zāra- (noun) and the causative stem *ā-zāraya- 'to cause pain' give Middle Persian āzār 'torment' and āzārdan/āzār- 'to torment, injure' (MacKenzie p.15, spelled ʾcʾl and ʾcʾl-tn'), attested also in Manichaean MP ʾzʾr- and Parthian ʾʾzʾr- 'to injure'. New Persian inherits both directly: آزار āzār, and the verb in two shapes — the regular آزاردن āzārdan (stem آزار-) and the shortened آزردن āzurdan (stem آزار-/آزُر-) with the past participle آزرده āzurda, which Hübschmann equates with Av. āzarəta-. Abolghasemi notes that «آزرد» is simply a contraction of «آزار». The bracketed آزارش of the chart is the present stem/verbal noun آزارش 'act of tormenting' (MP āzārišn).\",\n          \"derivation_fa\": \"پیوند اوستایی ← فارسی درست است، هرچند ریشهٔ بالادست نادرست باشد. از ایرانی باستان *ā-zāra- (اسم) و ستاک سببیِ *ā-zāraya- «آزردن»، فارسی میانه āzār «آزار» و āzārdan/āzār- «آزردن، رنجاندن» پدید آمده (مکنزی، صفحهٔ ۱۵) که در فارسی میانهٔ مانوی ʾzʾr- و پارتی ʾʾzʾr- هم گواهی شده است. فارسی نو هر دو را مستقیم به ارث برده: «آزار»، و فعل را در دو صورت — «آزاردن» با ستاک «آزار-» و صورت کوتاه‌شدهٔ «آزردن» با اسم مفعول «آزرده» که هوبشمان آن را برابر āzarəta- اوستایی می‌داند. ابوالقاسمی نیز می‌گوید «آزرد» مخفف «آزار» است. «آزارش» همان اسم مصدرِ āzārišn فارسی میانه است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/آزردن\"],\n          \"ref_check\": [\n            {\"ref\": \"WLD1:603\", \"status\": \"contradicts\", \"note\": \"Same parenthesis as node 1: Walde-Pokorny I 603 cites 'np. āzurda \\\"gekränkt\\\" und āzurdan \\\"kränken\\\"' precisely in order to say they belong with Skt. hṛṇīte and not with gher- 'greifen, fassen'.\"},\n            {\"ref\": \"FFD:25\", \"status\": \"supports\", \"note\": \"FFD_pages.txt [pdf page 30] = printed p.۲۵: 'آزار ← فارسی میانه āzār < ایرانی باستان *ā-zāra-' and '«آزرد» که امروزه به ضم ز تلفظ می‌شود، مخفف «آزار» است.' — exactly the Persian ← Middle Persian ← Old Iranian chain of this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 15\", \"stance\": \"supports\", \"note\": \"'āzār … torment. āzārdan, āzār- … torment, injure. ~išn: torment, injury.' and 'āzurdan [ʾcwltn! | N ~] = āzārdan' — MacKenzie gives both NP shapes.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 20, p. 6\", \"stance\": \"supports\", \"note\": \"'āzār \\\"Leid\\\", āzārden, āzāris; āzerden, āzerm … phlv. āzār, āzārtan etc.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 469, s.v. *zarH1\", \"stance\": \"supports\", \"note\": \"'*NWIR: … (+ *ā-) NP āzurdan/āzār- \\\"to torment, injure\\\", NP āzār \\\"affliction, disease, grieve, vexation, injury\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`pz`rn : to harm\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Sogdian word is real and the cited page is exact, but it is drawn from the wrong parent: it belongs under the Iranian *zar- of node 1, not under PIE *ǵʰer- 'enclose'. Gharib's Sogdian Dictionary p.55, entry 1411, reads 'ʾpzʾrn- B, S | (o)pzarn (ʾpzrn-) © Av. zar- | (to) disturb | VJ 1458' — Gharib herself derives it from Avestan zar-; entry 1410 gives the noun ʾpzʾrn (o)pzarn 'trouble, sorrow'. Morphologically it is the preverb *upa- + the root *zar-: Cheung lists 'BSogd. ʾpzʾrn \\\"to disturb, afflict (?)\\\"' beside ā-forms (BSogd. ʾʾzʾyr, MSogd. ʾʾzyr 'to offend, hurt') and pati-forms (CSogd. ptzyr- 'to afflict'), all under *zarH1. So the Buddhist Sogdian form is the *upa- compound of the same verb that gives Persian آزردن — a sibling of node 1/2, not an independent child of the PIE 'enclosure' root.\",\n          \"derivation_fa\": \"واژهٔ سغدی واقعی است و ارجاع نورایی هم دقیقاً درست، ولی از شاخهٔ نادرست آویخته شده: جای آن زیر ریشهٔ ایرانیِ *zar- (گرهٔ ۱) است، نه زیر *ǵʰer- هندواروپایی. قریب در فرهنگ سغدی، صفحهٔ ۵۵، مدخل ۱۴۱۱ می‌نویسد: «ʾpzʾrn- ب، س | (o)pzarn | © اوستایی zar- | to disturb | VJ 1458» و در مدخل ۱۴۱۰ اسم ʾpzʾrn «رنج، اندوه». ساختِ واژه پیشوند *upa- + ریشهٔ *zar- است؛ چونگ آن را در کنار صورت‌های ā-دار (ʾʾzyr «آزردن») و pati-دار (ptzyr-) زیر همان *zarH می‌آورد. پس این واژه خواهرِ «آزردن» فارسی است و ادعای نورایی دربارهٔ ریشه پذیرفتنی نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/آزردن\"],\n          \"ref_check\": [\n            {\"ref\": \"SOD:55\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 121 (printed p.55 = leaf − 66), entry '1411 ʾpzʾrn- B, S | (o)pzarn (ʾpzrn-) ©Av. zar- | (to)disturb | VJ 1458'. Nourai's SOD:55 is a page number and it is correct; note Gharib's gloss is 'to disturb', slightly weaker than Nourai's 'to harm'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"p. 469, s.v. *zarH1, Sogdian section\", \"stance\": \"partial\", \"note\": \"'|| (+ *upa-) BSogd. ʾpzʾrn \\\"to disturb, afflict (?)\\\" … Pres.: SUBJ. 3sg. BSogd. ʾpzʾrnʾt' — confirms the word and its analysis as *upa- + *zar-, and denies any IE cognate for the root.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 1669 f., s.v. zar-\", \"stance\": \"supports\", \"note\": \"Bartholomae's Avestan zar- 'erzürnen' is the etymon Gharib points to with '©Av. zar-'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"xorus : an enclosed dancing group\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word is Ancient Greek χορός khorós 'dancing-ground; ring-dance; band of dancers and singers' (Nourai's 'xorus' is his usual transliteration, x for χ, with the Latin ending of chorus). Deriving it from *ǵʰer- 'enclose' via an o-grade *ǵʰor-ó-s 'enclosed place (for dancing)' is a respectable but contested proposal: it goes back to Curtius (1869), is adopted by Klein ('The first meaning was prob. \\\"an enclosed place for dancing\\\", from I.-E. base *gher-'), by Watkins in the AHD appendix ('4. Perhaps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing)') — which is Nourai's cited AHD — and by Mann, who files khorós under 'ghoros (1) enclosure, envelope'. But Pokorny himself hedges on the same page Nourai cites for the root: 'doubtful, whether here χορός \\\"dancing place\\\" as originally \\\"inserted place\\\"', and adds that deriving it from the ablaut of χόρτος is 'incredible'. Beekes (2010) reconstructs Proto-Hellenic *kʰorós < *ǵʰeros from a root *ǵʰer- but says the semantic identity of that root 'has been disputed', listing 'enclosure' as only one of three competing accounts (another connects it with κορμός < *(s)ker- 'to cut off'). Nourai's gloss 'an enclosed dancing group' also conflates the two senses: the etymological sense is the dancing PLACE, the enclosure; 'group of dancers' is the later, derived sense.\",\n          \"derivation_fa\": \"واژه همان χορός khorós یونانی باستان است: «میدانِ رقص، رقصِ حلقه‌ای، دستهٔ رقصنده و آوازخوان» (نوشتار «xorus» شیوهٔ آوانگاریِ خودِ نورایی است، x به‌جای χ). بازبردنِ آن به *ǵʰer- «در بر گرفتن، محصور کردن» از راهِ صورت o-دارِ *ǵʰor-ó-s «جای محصور (برای رقص)» فرضی آبرومند اما مورد اختلاف است: از کورتیوس آغاز شده و کلاین، واتکینز در پیوست فرهنگ American Heritage (همان AHD که نورایی به آن ارجاع می‌دهد، با قید «شاید») و مان آن را پذیرفته‌اند، ولی خودِ پوکورنی در همان صفحهٔ ۴۴۲ می‌نویسد «مشکوک است که χορός اینجا جای داشته باشد» و بیکس می‌گوید هویتِ معناییِ این ریشه محلِ مناقشه است و «محصور کردن» تنها یکی از سه توضیح رقیب است. افزون بر این، معنای ریشه‌شناختی «جایِ محصورِ رقص» است، نه «دستهٔ رقصنده»؛ نورایی این دو را در هم آمیخته. در مجموع: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/χορός\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gher-1: '4. Perhaps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing), dance, dramatic chorus: (CHOIR), (CHORAL), CHORIC, (CHORISTER), CHORUS' — supports the arrow, though with two hedges ('Perhaps', '?') that Nourai's chart drops.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. chorus\", \"stance\": \"supports\", \"note\": \"'chorus, n. — L., fr. Gk. χορός, \\\"dance in a ring, festive dance … place for dancing\\\". The first meaning was prob. \\\"an enclosed place for dancing\\\", from I.-E. base *gher-, \\\"to seize, take, hold, close, envelop\\\", whence also Gk. χείρ, \\\"hand\\\", χόρτος, \\\"feeding place, courtyard\\\".'\"},\n            {\"src\": \"POK\", \"where\": \"p. 442-443, gher-4\", \"stance\": \"partial\", \"note\": \"'doubtful, whether here χορός \\\"dancing place, place for dancing\\\" as originally \\\"inserted place\\\"' — Pokorny keeps it, but flags it as uncertain; and he calls the alternative derivation from the ablaut of χόρτος 'incredible'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. ghoros (1)\", \"stance\": \"supports\", \"note\": \"Mann files 'Gk. khorós \\\"dancing-place\\\"' under 'ghoros (1) \\\"enclosure, envelope\\\"', cross-referring to ghortos.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for Latin chorus, a straight borrowing of Greek χορός taken over with the Greek theatre and its vocabulary in the Republican period (Plautus, Terence, then Horace's chorus of drama); Latin kept both the 'band of singers/dancers' and the 'ring-dance' senses. Klein: 'chorus, n. — L., fr. Gk. χορός'. Latin also formed the derivative choraula, chorea, and the adjective choricus, none of which the chart needs.\",\n          \"derivation_fa\": \"جعبهٔ خالیِ گذرگاهی برای لاتینی chorus است که وام‌واژهٔ مستقیمِ χορός یونانی است و همراه با تئاتر یونانی و اصطلاحاتش در دورهٔ جمهوری وارد لاتینی شد (پلاؤتوس، ترنتیوس، سپس «کُرِ» درام نزد هوراس). لاتینی هر دو معنیِ «دستهٔ آوازخوان» و «رقصِ حلقه‌ای» را نگه داشت. کلاین: «chorus از لاتینی، از یونانی χορός». ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/χορός\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this box; the Greek → Latin borrowing is covered by the AHD and KLN citations on the neighbouring boxes.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. chorus\", \"stance\": \"supports\", \"note\": \"'chorus, n. — L., fr. Gk. χορός' — the Latin word is simply the Greek one.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gher-1\", \"stance\": \"supports\", \"note\": \"CHORUS, CHORAL, CHORIC, CHORISTER are listed as the English reflexes of Greek khoros, i.e. via Latin chorus.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for French. Latin chorus gave two French words: the inherited/early-borrowed cuer (12th c., 'part of a church where the singers stand', modern chœur, pronounced [kœʁ]), and the learned Latinism chorus/chœur 'body of singers' re-imported in the 16th century with Renaissance music theory. Both are the ancestors of the two branches the chart draws from this box — Persian کر and English choir/chorus.\",\n          \"derivation_fa\": \"جعبهٔ خالیِ گذرگاهی برای فرانسه. لاتینی chorus دو واژهٔ فرانسوی داده است: cuer کهن (سدهٔ دوازدهم، «بخشی از کلیسا که خوانندگان در آن می‌ایستند»، امروز chœur با تلفظ [kœʁ]) و صورتِ عالمانهٔ chœur/chorus «دستهٔ آوازخوان» که در سدهٔ شانزدهم همراه با نظریهٔ موسیقی رنسانس دوباره از لاتینی وام گرفته شد. هر دو شاخه‌ای که نورایی از این جعبه می‌کشد — «کُر» فارسی و choir/chorus انگلیسی — از همین‌جا می‌آیند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/χορός\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given in the chart for this box.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. chorus, choir\", \"stance\": \"supports\", \"note\": \"Klein treats choir/quire as the French-mediated form and chorus as the direct Latin form of the same Greek word.\"},\n            {\"src\": \"MON\", \"where\": \"s.v. کر (via abadis.ir, فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"Mo'in tags Persian کر as [فر.] = French, which presupposes exactly this French intermediary.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"kor «کُر» : a singing group\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian کُر kor 'choir, choral singing' is a 20th-century European loan taken from French chœur [kœʁ], the French front rounded vowel [œ] being rendered by Persian short o (the same substitution as in مانور manovr, دکور dekor). Mo'in's entry is decisive: 'کر (کُ رْ) [فر.] (اِ.) (مس.) آواز دسته جمعی (اپرا، کلیسا و غیره)؛ مق. آریا؛ سلو' — a French loan, a musical term, 'group singing (opera, church etc.)', contrasted with aria and solo. That is exactly the chart's route Greek → Latin → French → Persian and exactly its gloss 'a singing group'.\",\n          \"derivation_fa\": \"«کُر» فارسی «آواز دسته‌جمعی» وام‌واژه‌ای اروپایی از سدهٔ چهاردهم خورشیدی است که از فرانسویِ chœur [kœʁ] گرفته شده؛ واکهٔ گِردِ پیشینِ فرانسوی [œ] در فارسی به ضمهٔ کوتاه بدل شده است، همان‌گونه که در «مانور» و «دکور». مدخل معین قاطع است: «کر (کُ رْ) [فر.] (اِ.) (مس.) آواز دسته جمعی (اپرا، کلیسا و غیره)؛ مق. آریا؛ سلو». پس همان مسیرِ نمودار — یونانی ← لاتینی ← فرانسه ← فارسی — و همان معنا. ادعای نورایی درست است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/کر/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2927\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi: MON_part2.txt line 21515 'کر: … (اِ.) (مس.) آواز دسته جمعی (اپرا، کلیسا و غیره)؛ مق. آریا؛ سلو' (the Latin-script origin tag is damaged in the OCR); the online text of the same entry at abadis.ir shows the tag '[ فر. ]' = French. Nourai's page number cannot be checked against the OCR (Mo'in's pagination is not mapped online), but the entry and gloss are exactly his.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. کر (abadis.ir, فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"'(کُ رْ) [ فر. ]' — Mo'in marks the word French, confirming Nourai's French parent box.\"},\n            {\"src\": \"BQT\", \"where\": \"grep of BQT_v2 for کر\", \"stance\": \"silent\", \"note\": \"Borhan-e Qāte' is a 17th-century dictionary and has no entry for this modern European loan, as expected.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"chorus, choir\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words go back to Greek khorós through Latin chorus, but by two different routes, and only one of them runs through French as the chart draws it. CHOIR is the French one: Middle English quer/quere (c.1300) from Old French cuer 'part of the church where singers stand', from Latin chorus; the spelling was refashioned in the 17th century after Latin chorus and French chœur, giving the modern hybrid spelling 'choir' pronounced /ˈkwaɪər/. CHORUS is a direct Latin borrowing of the 1560s ('band of singers and dancers' in Greek drama), taking the modern sense 'refrain sung by all' in the 1590s; it did not pass through French. Klein files both under the same head (chorus … 'Cp. also choir, quire').\",\n          \"derivation_fa\": \"هر دو واژهٔ انگلیسی سرانجام به khorós یونانی و لاتینیِ chorus می‌رسند، اما از دو راه، و تنها یکی از آن دو — چنان‌که نمودار می‌کشد — از فرانسه گذشته است. choir از راه فرانسه آمده: انگلیسی میانه quer/quere (حدود ۱۳۰۰ م.) از فرانسویِ کهن cuer «بخشی از کلیسا که خوانندگان در آن می‌ایستند»، از لاتینی chorus؛ املای آن در سدهٔ هفدهم به قیاسِ chorus لاتینی و chœur فرانسوی بازسازی شد. اما chorus وام‌واژهٔ مستقیم از لاتینی در دههٔ ۱۵۶۰ است و از فرانسه نگذشته است. کلاین هر دو را زیر یک مدخل می‌آورد. ادعای نورایی در کل درست است، با این تصحیح که chorus مستقیماً از لاتینی وام گرفته شده.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/χορός\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this box; the AHD citation on the Greek box lists (CHOIR) … CHORUS among the English reflexes of khoros.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. chorus\", \"stance\": \"supports\", \"note\": \"'chorus, n. — L., fr. Gk. χορός … Cp. also choir, quire, chorea, choreus, the first element in carol and in choragus and the second element in Terpsichore.'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Choir\", \"stance\": \"supports\", \"note\": \"Skeat cross-refers 'Choir; see Chorus', and his index line 'choir—chorus, quire' groups the two as the same word.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gher-1\", \"stance\": \"supports\", \"note\": \"'(CHOIR), (CHORAL), (CHORALE), CHORIC, (CHORISTER), CHORUS' listed as the English descendants of Greek khoros.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Greek\",\n          \"words\": \"ğr-on-os, chronos, xronos : that which encloses all things, time\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The node reproduces Klein p.284 almost word for word, including his reconstruction: 'chronic … fr. Gk. χρονικός \\\"pertaining to time\\\", fr. χρόνος, \\\"time\\\", which prob. stands for *ghr-on-os and derives fr. I.-E. base *gher-, \\\"to seize, take, hold, close, envelop\\\", whence also Gk. χείρ, \\\"hand\\\" … Time is regarded as \\\"that which embraces all things\\\". See Hofmann, EWG., p.424 s.v. χρόνος.' So Nourai's first 'word', ğr-on-os, is not a Greek form at all but Klein's PIE preform *gʰr-on-os, and his gloss 'that which encloses all things' is Klein's/Hofmann's semantic rationalisation, not an attested Greek meaning. The claim is a minority one. Beekes (EDG 2010, p.1651) files χρόνος under 'no etymology': he records the derivation from *ǵʰr-ono- < *ǵʰer- 'to seize, enclose' (sense 'encompassing time-limit') as a suggestion only, alongside a rival connection with κορμός < *(s)ker- 'to cut off'; Chantraine likewise leaves it unexplained. Watkins does not list khronos under gher-1 at all. So: an accepted-by-some derivation, not the modern consensus.\",\n          \"derivation_fa\": \"این گره تقریباً واژه‌به‌واژه از کلاین صفحهٔ ۲۸۴ گرفته شده، حتی با همان بازسازی: «χρόνος که احتمالاً *ghr-on-os بوده و از ریشهٔ هندواروپاییِ *gher- «گرفتن، در بر گرفتن» می‌آید … زمان همان چیزی انگاشته می‌شود که همه چیز را در بر می‌گیرد». پس نخستین «واژهٔ» نورایی، ğr-on-os، اصلاً صورتی یونانی نیست بلکه بازسازیِ هندواروپاییِ کلاین است، و معنیِ «آنچه همه چیز را در بر می‌گیرد» توجیهِ معنایی کلاین و هوفمان است نه معنایی گواهی‌شده در یونانی. این رأی اقلیت است: بیکس در فرهنگ ریشه‌شناختی یونانی (۲۰۱۰، صفحهٔ ۱۶۵۱) χρόνος را «بی‌ریشه‌شناسی» می‌داند و پیوند با *ǵʰer- را تنها در حدِ پیشنهاد می‌آورد، در کنار پیشنهاد رقیبِ پیوند با κορμός از *(s)ker- «بریدن»؛ واتکینز نیز khronos را زیر gher-1 نیاورده است. پس: با احتیاط پذیرفتنی است، نه اجماعِ امروزی.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/χρόνος\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:284\", \"status\": \"supports\", \"note\": \"Klein s.v. chronic: 'fr. Gk. χρόνος, \\\"time\\\", which prob. stands for *ghr-on-os and derives fr. I.-E. base *gher-, \\\"to seize, take, hold, close, envelop\\\" … Time is regarded as \\\"that which embraces all things\\\". See Hofmann, EWG., p.424 s.v. χρόνος.' The wording of Nourai's box (including the reconstruction ğr-on-os and the gloss) is taken straight from this entry, and p.284 is the right page for 'chronic' in Klein vol. I.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 442-443, gher-4\", \"stance\": \"silent\", \"note\": \"Pokorny's gher-4 article lists χορτος, χορός (doubtfully), χορίον and χείρ but says nothing at all about χρόνος — the root article Nourai cites does not carry this word.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gher-1\", \"stance\": \"silent\", \"note\": \"Watkins's list of Greek reflexes under gher-1 stops at khoros; chronos and its English family are absent from the appendix.\"},\n            {\"src\": \"IEC\", \"where\": \"s.vv. ghoros, ghortos\", \"stance\": \"silent\", \"note\": \"Mann files khorós under ghoros but has no entry connecting khrónos with this root.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Arabic\",\n          \"words\": \"qarn : a century\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic قَرْن qarn 'century; generation' is on the mainstream view a native Semitic word, not a Greek loan. The root is q-r-n, from Proto-Semitic *ḳarn- 'horn' (Hebrew קֶרֶן qeren, Aramaic qarnā, Akkadian qarnu, Ugaritic qrn), with the same root supplying qarana 'to join, couple', qarīn 'companion, peer', iqtarana 'to be coupled'. The temporal sense develops inside Arabic from 'those coupled/paired together, people of the same age' → 'generation' (the Qur'anic sense, e.g. Q 6:6 kam ahlaknā min qablihim min qarnin 'how many generations We destroyed before them') → the later fixed 'hundred years', a sense Arabic lexicographers themselves date after the Qur'an. Nourai's Greek etymology comes from his source al-Unaysi (TAD:56), who does list qarn among borrowed words 'transferred from Greek … meaning among them time, moment, duration … its synonym is dahr, i.e. a hundred years' — evidently χρόνος. Wiktionary records the same idea as a bare alternative ('Otherwise, it could have been borrowed from Ancient Greek χρόνος'), but the phonology is against it (Gk. khr- would not give Arabic q-r-, and Arabic has no other trace of the word) and the native root with its rich derivational family is against it too. Jeffery's Foreign Vocabulary of the Qur'an, which catalogues every suspected loan in the Qur'an, does not list qarn at all.\",\n          \"derivation_fa\": \"«قَرْن» عربی به معنی «سده، نسل» بنا بر رأیِ رایج واژه‌ای اصیلِ سامی است، نه وام‌واژهٔ یونانی. ریشهٔ آن ق-ر-ن از سامیِ آغازین *ḳarn- «شاخ» است (عبری qeren، آرامی qarnā، اکدی qarnu) و همین ریشه قَرَنَ «جفت کردن»، قَرین «همتا، همنشین» و اقترَنَ را داده است. معنای زمانی درونِ خودِ عربی پدید آمده: «هم‌سالان، مردمِ یک روزگار» ← «نسل» (معنای قرآنی، مانند «کم أهلکنا من قبلهم من قرن») ← سپس «صد سال» که فرهنگ‌نویسان عرب خود آن را متأخر می‌دانند. ریشه‌شناسیِ یونانیِ نورایی از مأخذش، طوبیا العنیسی (TAD صفحهٔ ۵۶) می‌آید که قرن را در شمار واژه‌های «منقول من اليونانية» آورده و توضیح داده «عندهم زمان ووقت ومدة … مرادفه دهر أي مائة سنة» که آشکارا همان χρόνος است. ویکی‌واژه هم این را تنها در حدِ احتمالِ جایگزین می‌آورد. اما آواشناسی با آن نمی‌خواند (خوشهٔ khr- یونانی در عربی ق-ر- نمی‌دهد) و جفری هم در «واژگان بیگانهٔ قرآن» قرن را اصلاً وام‌واژه نشمرده است. پس پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/قرن\"],\n          \"ref_check\": [\n            {\"ref\": \"TAD:56\", \"status\": \"supports\", \"note\": \"TAD.txt, the entry standing alphabetically between قرميد and قرنفل on the leaf that corresponds to printed p.56 (leaf 60, offset leaf−4): the surviving OCR reads '… منقول من اليونانية … عندهم زمان ووقت ومدة وستون … مرادفه دهر أي مائة سنة'. The headword line itself is badly damaged in the OCR but the position and the wording show al-Unaysi does class qarn as a Greek loan ('time, duration' among the Greeks), which is Nourai's claim. The page number is right; the claim is al-Unaysi's, and it is a minority one.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"grep of FVQ.txt / FVQ_pages.txt for qarn\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qur'an has no entry for qarn, although the word occurs repeatedly in the Qur'an in the sense 'generation' — i.e. the standard catalogue of Qur'anic loanwords does not regard it as borrowed.\"},\n            {\"src\": \"AFM\", \"where\": \"grep of AFM_pages.txt for قرن as a headword\", \"stance\": \"silent\", \"note\": \"Addi Shir's Kitāb al-Alfāẓ al-Fārisiyya al-Muʿarraba lists no قرن — consistent with the word being native Arabic rather than a loan.\"},\n            {\"src\": \"KLN\", \"where\": \"grep of KLN_1971.txt for 'Arab. qarn'\", \"stance\": \"silent\", \"note\": \"Klein, who routinely notes Greek words borrowed into Arabic, makes no such note at χρόνος/chronic.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"qarn «قَرن ( قرون )» : a century\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge Arabic → Persian is correct: قَرن qarn 'century' with the Arabic broken plural قُرون qorun is one of the very many Arabic learned loans that entered New Persian with the post-conquest chancery and religious vocabulary; the plural قرون is itself Arabic and is used unchanged in Persian (قرون وسطی 'the Middle Ages'). Mo'in's entry marks the origin unambiguously: 'قرن [ع.] (اِ.) … از زمان معادل سی سال. صد سال (اینک بدین معنی متداول است). سده. پاره‌ای از زمان؛ عهد، دوران، دوره' — '[ع.]' = Arabic, and note that Mo'in preserves the older 'thirty years' sense beside the now-usual 'hundred years'. Mo'in gives no Greek origin. The verdict is 'confirmed' for this arrow only; the ultimate Greek source claimed one box up (node 10) is disputed.\",\n          \"derivation_fa\": \"پیوند عربی ← فارسی درست است: «قَرن» به معنی «سده» با جمع مکسّرِ عربیِ «قُرون» یکی از انبوه وام‌واژه‌های عربی است که پس از اسلام همراه با زبان دیوانی و دینی وارد فارسی نو شد؛ جمعِ «قرون» نیز عربی است و دست‌نخورده در فارسی به کار می‌رود («قرون وسطی»). مدخل معین اصلِ آن را بی‌ابهام نشان می‌دهد: «قرن [ع.] (اِ.) … از زمان معادل سی سال. صد سال (اینک بدین معنی متداول است). سده. پاره‌ای از زمان؛ عهد، دوران، دوره» — «[ع.]» یعنی عربی، و جالب آنکه معین معنای کهن‌ترِ «سی سال» را هم در کنار «صد سال» نگه داشته است. معین هیچ اصلِ یونانی برای آن نمی‌آورد. این گره درست است؛ ولی ادعای اصلِ یونانی در گرهٔ بالاتر پذیرفتنی نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/قرن\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2665\", \"status\": \"supports\", \"note\": \"Mo'in, MON_part2.txt: 'قرن: [ع.] (اِ.) … از زمان معادل سی سال. صد سال (اینک بدین معنی متداول است.) سده. پاره‌ای از زمان؛ عهد، دوران، دوره؛ ج. دوره.' The entry is exactly Nourai's word and gloss and confirms the Arabic tag; the printed page number cannot be checked because Mo'in's pagination is not mapped in the available scan/OCR.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. قرن (MON_part2.txt)\", \"stance\": \"supports\", \"note\": \"Three separate قرن entries: '[ع.] … صد سال' (century), '[ع.] … شاخ، سرون' (horn) and '[معر.] (گیا.) زغال اخته' (cornel) — the century-word and the horn-word share the Arabic tag, i.e. Mo'in treats them as the same Arabic root, not as a Greek loan.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"Asbaghi's catalogue is of Persian words in Arabic, and قرن does not appear there — consistent with qarn being neither a Persian nor (for him) a foreign element in Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Latin\",\n          \"words\": \"chronicus : time\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin chronicus 'of or belonging to time' is a straight borrowing of Greek χρονικός khronikós, the adjective of χρόνος, taken over with Greek medical and historiographical vocabulary; the neuter plural chronica 'annals' (< τὰ χρονικά) is the source of 'chronicle'. The chart's edge is drawn from khronos directly, skipping the actual etymon khronikos, and its gloss 'time' belongs to the noun, not to the adjective ('pertaining to time'). The American Heritage Dictionary — Nourai's AHD:240 — gives precisely this chain: '[French chronique, from Latin chronicus, from Greek khronikos, of time, from khronos, time.]'\",\n          \"derivation_fa\": \"لاتینیِ chronicus «مربوط به زمان» وام‌واژهٔ مستقیمِ χρονικός یونانی است، صفتِ χρόνος، که همراه با اصطلاحات پزشکی و تاریخ‌نگاریِ یونانی وارد لاتینی شد؛ جمعِ خنثای chronica «سالنامه» (از τὰ χρονικά) خاستگاه chronicle است. نمودار پیکان را مستقیم از khronos می‌کشد و صورتِ واسطهٔ khronikos را جا انداخته، و معنیِ «time» هم از آنِ اسم است نه صفت («مربوط به زمان»). فرهنگ American Heritage — همان AHD:240 که نورایی به آن ارجاع می‌دهد — دقیقاً همین زنجیره را می‌آورد: «از فرانسویِ chronique، از لاتینیِ chronicus، از یونانیِ khronikos «مربوط به زمان»، از khronos «زمان»». ادعای نورایی درست است.\",\n          \"sources\": [\"https://ahdictionary.com/word/search.html?q=chronic\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:240\", \"status\": \"supports\", \"note\": \"The AHD entry for 'chronic' reads '[French chronique, from Latin chronicus, from Greek khronikos, of time, from khronos, time.]' — the Greek → Latin → French chain of nodes 12-14 exactly. (Checked in the current online AHD; the New College edition body, where p.240 would fall in the C's, is not available locally, but the etymology is the same one.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. chronic, chronicle\", \"stance\": \"supports\", \"note\": \"'chronic, adj. … — F. chronique, fr. L. chronicus, fr. Gk. χρονικός, \\\"pertaining to time\\\", fr. χρόνος, \\\"time\\\"'; 'chronicle, n. — ME. cronicle, fr. cronique … fr. OF. cronique (F. chronique), fr. L. chronica, neut. pl. mistaken for a fem. sing., fr. Gk. τὰ χρονικά.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"silent\", \"note\": \"Ernout-Meillet, being a dictionary of inherited Latin, has no article on the Greek technical loan chronicus.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"French\",\n          \"words\": \"chronique\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French cronique (13th c.), later respelled chronique after Latin, is both the noun 'chronicle, annals' (from Latin chronica, the Greek neuter plural τὰ χρονικά reinterpreted as a feminine singular) and the adjective 'chronic' (from Latin chronicus), the medical sense appearing in the 16th century. It is the immediate source of the English words in the next box. Klein: 'chronicle, n. — ME. cronicle, fr. cronique, cronike, fr. OF. cronique (F. chronique)'; AHD: '[French chronique, from Latin chronicus …]'.\",\n          \"derivation_fa\": \"cronique در فرانسویِ کهن (سدهٔ سیزدهم) و سپس با املای لاتینی‌شدهٔ chronique، هم اسم است به معنی «سالنامه، وقایع‌نگاری» (از لاتینیِ chronica، یعنی جمع خنثای یونانیِ τὰ χρονικά که مؤنث مفرد پنداشته شده) و هم صفت به معنی «مزمن» (از لاتینیِ chronicus) که کاربرد پزشکی‌اش در سدهٔ شانزدهم پیدا شده است. همین واژه مأخذ مستقیمِ واژه‌های انگلیسیِ جعبهٔ بعدی است. کلاین و فرهنگ American Heritage هر دو همین را می‌گویند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://ahdictionary.com/word/search.html?q=chronic\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. chronic: '[French chronique, from Latin chronicus …]'.\"},\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein s.v. chronic: '— F. chronique, fr. L. chronicus'; s.v. chronicle: 'fr. OF. cronique (F. chronique), fr. L. chronica'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. chronic, chronicle\", \"stance\": \"supports\", \"note\": \"See the quotations above; Klein makes French the immediate source of both English words.\"},\n            {\"src\": \"SKT\", \"where\": \"grep of SKT.txt for Chronicle\", \"stance\": \"silent\", \"note\": \"Skeat's Concise edition has no separate article on chronicle in the OCR text; nothing found for or against.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"chronic, chronicle, chronological, chronometer, synchronize\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five contain Greek khronos, but only the first two came through French as the chart's arrow implies. CHRONIC: 1550s, from French chronique, Latin chronicus, Greek khronikos, first of diseases 'lasting a long time'. CHRONICLE: Middle English cronicle (c.1300), from Anglo-French cronicle, Old French cronique, Latin chronica. The other three are learned coinages made in modern Europe out of Greek elements, not inherited words: CHRONOLOGICAL (1590s, Modern Latin chronologia, khronos + -logia), CHRONOMETER (1735, coined in English/Neo-Latin, khronos + metron), SYNCHRONIZE (1620s, from Greek synkhronizein/synkhronos 'contemporaneous', syn- + khronos). Nourai's box is therefore right about the ultimate Greek source of all five but hides the difference between the two French-mediated inheritances and the three Neo-Greek coinages.\",\n          \"derivation_fa\": \"هر پنج واژه khronos یونانی را در خود دارند، اما تنها دو تای نخست، چنان‌که پیکانِ نمودار می‌گوید، از راه فرانسه آمده‌اند. chronic (دههٔ ۱۵۵۰) از فرانسویِ chronique و لاتینیِ chronicus، نخست دربارهٔ بیماریِ دیرپا؛ chronicle از انگلیسی میانهٔ cronicle (حدود ۱۳۰۰ م.) از فرانسویِ کهن cronique. اما سه واژهٔ دیگر ساخته‌های عالمانهٔ اروپای نو از عناصر یونانی‌اند، نه واژه‌های موروثی: chronological (دههٔ ۱۵۹۰، از لاتینیِ نوِ chronologia)، chronometer (۱۷۳۵، khronos + metron)، و synchronize (دههٔ ۱۶۲۰، از یونانیِ synkhronos «هم‌زمان»). پس جعبهٔ نورایی دربارهٔ خاستگاهِ نهاییِ یونانیِ هر پنج درست است، ولی تفاوتِ دو واژهٔ فرانسه‌گذر و سه ساختهٔ نوساز را می‌پوشاند.\",\n          \"sources\": [\"https://ahdictionary.com/word/search.html?q=chronic\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. chronic: '[French chronique, from Latin chronicus, from Greek khronikos, of time, from khronos, time.]'\"},\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein s.v. chronic lists the family: 'Cp. chronicle, crony, and the second element in isochronous, anachronism, metachronism, parachronism'; s.v. chrono-: 'before a vowel chron-, combining form meaning \\\"time\\\". — Gk. χρονο-, χρον-, fr. χρόνος' — the element from which chronological and chronometer are built.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. chronic, chronicle, chrono-\", \"stance\": \"supports\", \"note\": \"Klein separates the inherited pair (chronic, chronicle, both via French) from the combining form chrono- used in modern coinages, exactly the distinction the chart elides.\"},\n            {\"src\": \"SKT\", \"where\": \"grep of SKT.txt\", \"stance\": \"silent\", \"note\": \"No chronicle/chronic article surfaced in the OCR of Skeat's Concise dictionary.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for Proto-Germanic. The root's noun derivative surfaces in Germanic as *gardaz m. 'enclosure, yard, dwelling' (Gothic gards 'house', ON garðr 'fence, yard', OE ġeard, OS gard) beside the weak *gardô 'garden, enclosed plot' (Gothic garda 'fold, stall', OHG garto, OS gardo, Old Frisian garda). Pokorny declares it undecidable whether these go back to *ǵʰor-tó- (with Gk. khórtos and Lat. hortus) or to *ǵʰordʰo- (with OCS gradŭ, Lith. gardas, Alb. gardh) — 'Is not to be decided, whether Gothic garda … Old High German garto in Indo Germanic *ghor-to- or in *ghordho- are based on' — which is precisely why Nourai's root box names both Gherd and Ghordho.\",\n          \"derivation_fa\": \"جعبهٔ خالیِ گذرگاهی برای ژرمنیِ آغازین. اسمِ برگرفته از ریشه در ژرمنی به صورت *gardaz «جای محصور، حیاط، خانه» درآمده (گوتیِ gards «خانه»، اسکاندیناویِ کهن garðr، انگلیسی کهن ġeard) در کنارِ صورتِ ضعیفِ *gardô «باغ، کرتِ محصور» (گوتیِ garda، آلمانی علیای کهن garto). پوکورنی می‌گوید تعیین اینکه این‌ها به *ǵʰor-tó- (همراه با khórtos یونانی و hortus لاتینی) بازمی‌گردند یا به *ǵʰordʰo- (همراه با gradŭ اسلاوی کهن و gardas لیتوانیایی) ممکن نیست — و همین است که نورایی در جعبهٔ ریشه هر دو صورتِ Gherd و Ghordho را آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/yard\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box; the AHD citation on the English box below covers the Germanic material.\"}],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 442-443 and 444\", \"stance\": \"supports\", \"note\": \"'Is not to be decided, whether Gothic garda \\\"hurdle, stockyard\\\", Old Frisian garda, Old Saxon gardo, Old High German garto \\\"garden\\\" in Indo Germanic *ghor-to- or in *ghordho- are based on' (gher-4); and under gherdh-: 'Gothic gards m. \\\"house\\\", Old Icelandic garðr … Old English geard'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gher-1\", \"stance\": \"supports\", \"note\": \"'2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure, in: a. Germanic *gardaz …'\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. ghordhos\", \"stance\": \"supports\", \"note\": \"Mann: 'ghordhos, is \\\"fortified place, walled enclosure\\\" … Go. gards; OE geard \\\"fence, yard\\\"; ON garðr \\\"yard, fence, house, fort\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"yard, orchard, garden, kindergarten\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are Germanic reflexes of *ǵʰortos/*ǵʰordʰos, though they reach English by four different roads. YARD 'enclosure' is directly inherited: OE ġeard 'fenced enclosure, garden, court, residence' < PGmc *gardaz (distinct from yard 'measure', OE gyrd 'rod'). ORCHARD is OE ortġeard 'fruit garden', a compound whose second element is ġeard and whose first, ort-, is generally taken as an early Latin loan of hortus (Buck, Feist; an older view derived it from OE wyrt 'plant'), so orchard contains this root twice over. GARDEN is a re-import: Old North French gardin (Central French jardin), itself from Frankish *gardo, i.e. the West Germanic weak noun, borrowed into Middle English as gardin after 1300. KINDERGARTEN is a wholesale borrowing of German Kindergarten 'children's garden', Fröbel's coinage of 1840, in English from 1852. Watkins lists exactly these under gher-1, and Skeat calls garden and garth doublets of yard.\",\n          \"derivation_fa\": \"هر چهار واژه بازتابِ ژرمنیِ *ǵʰortos/*ǵʰordʰos‌اند، اما از چهار راهِ متفاوت به انگلیسی رسیده‌اند. yard «حیاط» موروثی است: انگلیسی کهن ġeard «جای محصور، حیاط، خانه» از ژرمنیِ *gardaz (جدا از yard «یارد، واحد اندازه» که از gyrd «چوب» است). orchard از ortġeard انگلیسی کهن «باغِ میوه» است؛ جزء دوم همان ġeard است و جزء نخست ort- را معمولاً وام‌واژهٔ کهنِ hortus لاتینی می‌دانند (باک، فایست)، پس orchard این ریشه را دو بار در خود دارد. garden وام‌گیریِ دوباره است: از gardin در فرانسویِ شمالیِ کهن (jardin در فرانسویِ مرکزی) که خود از فرانکیِ *gardo، یعنی همان اسمِ ضعیفِ ژرمنیِ غربی، آمده و پس از ۱۳۰۰ م. وارد انگلیسی میانه شده است. kindergarten وام‌واژهٔ تمام‌عیارِ آلمانیِ Kindergarten «باغِ کودکان»، ساختهٔ فروبل در ۱۸۴۰، است که از ۱۸۵۲ در انگلیسی به کار رفته. واتکینز همین چهار را زیر gher-1 آورده و اسکیت garden و garth را دوگانه‌های yard می‌خواند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/yard\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gher-1: 'a. Germanic *gardaz in (i) Old English geard, enclosure, garden, yard: YARD1; ORCHARD (ii) Old Norse gardhr: GARTH (iii) Old High German garto, garden: KINDERGARTEN (iv) Old North French gardin, garden: GARDEN' — all four of Nourai's words, in the same order.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"s.v. Yard (1)\", \"stance\": \"supports\", \"note\": \"'Yard (1), an enclosed space. (E.) M.E. yerd, A.S. geard, an enclosure, court … L. hortus, a garden; Gk. χορτος, court-yard … (√GHAR, to seize, enclose.) … Doublets, garden, garth. Der. court-yard, orchard (= wortyard).' Skeat's parse of orchard as 'wortyard' is the rival view to the hortus-loan.\"},\n            {\"src\": \"SYN\", \"where\": \"8.13 GARDEN, p.491\", \"stance\": \"supports\", \"note\": \"Buck: 'Goth. aurtigards, OE ortgeard, ME orchard … first part prob. old loanword fr. Lat. hortus (Feist 68, Stender-Petersen 370 f.; otherwise, namely : Goth. waurts \\\"root\\\", OE wyrt \\\"plant\\\", Walde-P. 1.288)'; and 'OHG garto, MHG garte, NHG garten (with the loanwords Fr. jardin, NE garden, etc.)'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. ghordhos\", \"stance\": \"supports\", \"note\": \"'OE geard \\\"fence, yard\\\"; ON garðr \\\"yard, fence, house, fort\\\" … R górod \\\"town\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Latin\",\n          \"words\": \"hortus : garden\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin hortus 'enclosed ground, garden' is the o-grade thematic noun *ǵʰortos of this root — the exact formal match of Greek χόρτος 'enclosed feeding-place, farmyard' and Oscan hurz 'hortus, lucus', with the regular Italic change of PIE *ǵʰ- to Latin h- initially. Ernout-Meillet: 'hortus … enclos, propriété close de murs … puis \\\"jardin\\\" … cf. χόρτος \\\"enceinte (de cour, de bergerie)\\\"; peut-être irl. gort \\\"champ\\\", lub-gort \\\"jardin\\\"'; they add that Latin cohors goes back to co-hortis from *-ǵʰr̥ti-, and since a root *ghert- is impossible in IE one must connect the root of Oscan heriiad 'capiat' and Skt. hárati 'he takes'. Paulus ex Festo records that in Old Latin hortus meant villa, 'farmstead' — i.e. the 'enclosure' sense still visible. Watkins puts hortus under gher-1 with the same analysis.\",\n          \"derivation_fa\": \"لاتینیِ hortus «زمینِ محصور، باغ» همان اسمِ o-دارِ *ǵʰortos از این ریشه است — همتای دقیقِ χόρτος یونانی «آغل، حیاطِ چارپایان» و hurz اوسکی، با تحولِ قاعده‌مندِ *ǵʰ- هندواروپایی به h- در آغازِ واژه در لاتینی. ارنو-مِیه می‌نویسد: «hortus … محوطهٔ بسته، ملکی که دیوار گرداگردش کشیده‌اند … سپس «باغ» … سنجیده شود با χόρτος «محوطهٔ حیاط و آغل»» و می‌افزاید که co-hors لاتینی از co-hortis و از *-ǵʰr̥ti- است و چون ریشهٔ *ghert- در هندواروپایی ناممکن است باید آن را با heriiad اوسکی «بگیرد» و hárati سنسکریت «می‌گیرد» سنجید. پاؤلوس از فستوس نقل می‌کند که در لاتینیِ کهن hortus به معنی villa «مزرعه» بوده، یعنی همان معنیِ «محوطهٔ محصور». واتکینز نیز hortus را زیر gher-1 آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/court\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gher-1: '2. … b. Latin hortus, garden: HORTICULTURE, ORCHARD, ORTOLAN.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. hortus\", \"stance\": \"supports\", \"note\": \"'hortus, -i m. … enclos, propriété close de murs (cf. … le sens du composé cohors), puis \\\"jardin\\\" … Cf. osq. hurz, hurtum \\\"enclos sacré\\\" … cf. χόρτος \\\"enceinte (de cour, de bergerie)\\\" … Lat. co-hors repose sans doute sur co-hortis, de *-ghrti-.'\"},\n            {\"src\": \"POK\", \"where\": \"p. 442-443, gher-4\", \"stance\": \"supports\", \"note\": \"'Latin cohors \\\"fenced courtyard, stockyard, troop, multitude\\\", from *co + IE *ghr̥tis … in ablaut to hortus \\\"garden as fenced place\\\" (in old Latin also villa), Oscan hurz \\\"hortus, lucus\\\".'\"},\n            {\"src\": \"SYN\", \"where\": \"8.13 GARDEN\", \"stance\": \"supports\", \"note\": \"Buck derives Lat. hortus (> It. orto, Sp. huerto) from IE *gher- 'seize, hold', beside cohors, Gk. khórtos, Ir. gort, 'all as orig. \\\"enclosure\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"horticulture, court, courtesy, curtain\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All four belong to this root, but only the first descends from hortus as the chart's arrow says; the other three come from its compound cohors and so are the root's nephews rather than its children. HORTICULTURE is a 1670s Neo-Latin compound hortus + cultura 'cultivation', on the model of agricultura. COURT is Old French cort, from Vulgar Latin curtem, accusative of Latin cors, older cohors (stem cohort-) 'enclosed yard, farmyard', analysed by Watkins as *ko(m)-ghr̥-ti- 'that which is enclosed together'; the sense went 'enclosed yard' → 'those assembled in the yard, retinue' → 'royal household, tribunal'. COURTESY is c.1200 Old French curtesie, from curteis 'having court manners', a derivative of cort — one further step, not a separate descent. CURTAIN is the subtlest: Old French cortine, from Ecclesiastical Latin cortina 'curtain', which Klein explains as derived from cohors, cors 'court' and used in the Vulgate as a loan-translation of Greek aulaía 'curtain' (itself from aulḗ 'court') to render Hebrew yerīʿāh in Exodus 26:1. So the chart's grouping is etymologically sound but its single arrow from hortus is a shortcut: Watkins puts COURT, COURTEOUS, (COURTESY), CURTILAGE and CURTSY under the *ko(m)-ghr̥-ti- / cohors heading, separate from the hortus heading, and does not list CURTAIN at all.\",\n          \"derivation_fa\": \"هر چهار واژه به این ریشه تعلق دارند، اما تنها نخستین آن‌ها — چنان‌که پیکانِ نمودار می‌گوید — از hortus می‌آید؛ سه تای دیگر از ترکیبِ cohors آمده‌اند و بنابراین برادرزادهٔ hortus‌اند نه فرزندِ آن. horticulture ترکیبی لاتینیِ نو از دههٔ ۱۶۷۰ است: hortus + cultura، به قیاسِ agricultura. court از cort فرانسویِ کهن، از curtem لاتینیِ عامیانه، مفعولیِ cors/cohors «حیاطِ محصور، آغل» که واتکینز آن را *ko(m)-ǵʰr̥-ti- «آنچه با هم در بر گرفته شده» تحلیل می‌کند؛ تحول معنایی: «حیاطِ محصور» ← «گردآمدگانِ در حیاط، ملتزمان» ← «دربار، دادگاه». courtesy از curtesie فرانسویِ کهن (حدود ۱۲۰۰ م.) از curteis «دارای آدابِ دربار»، یعنی یک گامِ دیگر از court، نه شاخه‌ای جدا. curtain ظریف‌ترین است: از cortine فرانسویِ کهن، از cortina در لاتینیِ کلیسایی که کلاین آن را برگرفته از cohors/cors «حیاط» می‌داند و می‌گوید در ترجمهٔ ولگات گرته‌برداری از aulaía یونانی «پرده» (خود از aulḗ «حیاط») برای برگرداندنِ yerīʿāh عبری در سِفر خروج ۲۶:۱ بوده است. پس دسته‌بندیِ نورایی از نظر ریشه‌شناسی درست است، ولی کشیدنِ یک پیکان از hortus میان‌بر است: واتکینز court و courtesy را زیر عنوانِ جداگانهٔ cohors می‌آورد و curtain را اصلاً نمی‌آورد. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/court\",\n            \"https://www.etymonline.com/word/curtain\"\n          ],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box; the parent Latin box cites AHD, whose gher-1 article covers HORTICULTURE (under hortus) and COURT/COURTEOUS/(COURTESY) (under cohors), but not CURTAIN.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. curtain\", \"stance\": \"supports\", \"note\": \"'curtain, n. — ME. cortin, fr. OF. cortine, curtine … fr. Eccles. L. cortina, \\\"curtain\\\", rendering of Heb. yᵉrīʿāh (Ex. 26:1 and passim) by the Vulgate. Eccles. L. cortina derives fr. L. cohors, cors, \\\"court\\\" (see court), and is prop. a loan translation of Gk. αὐλαία, \\\"curtain\\\" … fr. Gk. αὐλή, \\\"court, courtyard\\\".'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gher-1\", \"stance\": \"partial\", \"note\": \"'3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- … in Latin cohors (stem cohort-), enclosed yard, company of soldiers, multitude: COHORT, CORTEGE, COURT, COURTEOUS, COURTESAN, (COURTESY), COURTIER, (CURTILAGE), (CURTSY)' — same root, but a separate branch from hortus, and curtain is absent.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Curtain, Yard (1)\", \"stance\": \"supports\", \"note\": \"'Curtain: see Court.' and, under Yard (1), 'Der. court-yard, orchard' — Skeat likewise groups curtain with court and both with this root.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-188.json > /dev/null && echo \"JSON OK\"; python3 /home/sfmqrb/git/rishe/tools/verify_check.py 188",
 "description": "Write and validate page-188.json"
}
```


### [2026-09-06T02:34:03.404Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'disputed': 3, 'confirmed': 12, 'plausible': 3}
root verdicts: {'confirmed': 1}
ref checks: {'contradicts': 2, 'partial': 3, 'supports': 14, 'not_checked': 5}
books consulted: {'supports': 31, 'contradicts': 1, 'partial': 3, 'silent': 11} | by book: {'KLN': 9, 'AHD': 5, 'SKT': 5, 'POK': 4, 'IEC': 4, 'CHEUNG': 3, 'MON': 3, 'BRT': 2, 'PHD': 2, 'LAT': 2, 'SYN': 2, 'HRN': 1, 'BQT': 1, 'FVQ': 1, 'AFM': 1, 'PLA': 1}
```


## [2026-09-06T02:34:12.179Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; ls | head -3; f=$(ls index* 2>/dev/null | head -1); echo \"index: $f\"; if [ -n \"$f\" ]; then tail -c 1500 \"$f\"; fi",
 "description": "Inspect web archive index"
}
```


### [2026-09-06T02:34:14.367Z] TOOL RESULT

```
0013bab04a208776.txt
003529da0fded286.txt
00446da837c05ca7.txt
index: index.jsonl
5dc.txt", "fetched": "2026-09-06T02:33:21Z", "status": 200, "bytes": 7926, "title": "جاه - معنی در دیکشنری آبادیس", "note": "page 202 node 9: Mo'in's entry for جاه (origin tag)"}
{"url": "https://abadis.ir/fatofa/زمان/", "file": "data/verification/sources/web/b0958b5544989892.txt", "fetched": "2026-09-06T02:33:24Z", "status": 200, "bytes": 67183, "title": "زمان - معنی در دیکشنری آبادیس", "note": "page 202 node 13: Mo'in's entry for زمان"}
{"url": "https://en.wiktionary.org/wiki/%D8%A2%D8%BA%D9%84", "file": "data/verification/sources/web/37160c414f9e0ac1.txt", "fetched": "2026-09-06T02:33:36Z", "status": 200, "bytes": 6007, "title": "آغل - Wiktionary, the free dictionary", "note": "post-pass: page 193, root Gheugh, Ghŭgh, node #3 âğol «آغل»"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0reh%E2%82%81d-", "file": "data/verification/sources/web/5d133a61e3cce76c.txt", "fetched": "2026-09-06T02:33:37Z", "status": 200, "bytes": 4535, "title": "Reconstruction:Proto-Indo-European/ǵʰreh₁d- - Wiktionary, the free dictionary", "note": "post-pass: page 193, root Ghlâd (root-level)"}
{"url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%87", "file": "data/verification/sources/web/7f8059588d21a1de.txt", "fetched": "2026-09-06T02:33:37Z", "status": 200, "bytes": 6112, "title": "زره - Wiktionary, the free dictionary", "note": "post-pass: page 193, root Ghlâd, node #2 zrih"}
```


## [2026-09-06T02:34:20.792Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; grep -o '\"https://en.wiktionary.org/wiki/[^\"]*\"' page-193.json | sort -u | head; echo ---; grep -o '\"https://abadis[^\"]*\"' page-19*.json | sort -u | head -3",
 "description": "Check URL style in existing verification files"
}
```


### [2026-09-06T02:34:20.896Z] TOOL RESULT

```
"https://en.wiktionary.org/wiki/%D8%A2%D8%BA%D9%84"
"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%AF"
"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%87"
"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0reh%E2%82%81d-"
---
page-191.json:"https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84/"
page-191.json:"https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84%DB%8C/"
page-194.json:"https://abadis.ir/fatofa/%D8%BA%DA%98%D9%85/"
```


## [2026-09-06T02:34:32.551Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; python3 - <<'EOF'\nimport io\np='page-188.json'\ns=io.open(p,encoding='utf-8').read()\nrep={\n 'https://en.wiktionary.org/wiki/آزردن':'https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%B1%D8%AF%D9%86',\n 'https://en.wiktionary.org/wiki/χορός':'https://en.wiktionary.org/wiki/%CF%87%CE%BF%CF%81%CF%8C%CF%82',\n 'https://en.wiktionary.org/wiki/χρόνος':'https://en.wiktionary.org/wiki/%CF%87%CF%81%CF%8C%CE%BD%CE%BF%CF%82',\n 'https://en.wiktionary.org/wiki/قرن':'https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%86',\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰer-':'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0er-',\n 'https://abadis.ir/fatofa/کر/':'https://abadis.ir/fatofa/%DA%A9%D8%B1/',\n}\nfor k,v in rep.items():\n    s=s.replace('\"'+k+'\"','\"'+v+'\"')\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\npython3 -m json.tool page-188.json >/dev/null && echo \"JSON OK\"; grep -c 'wiktionary.org/wiki/%' page-188.json; python3 /home/sfmqrb/git/rishe/tools/verify_check.py 188",
 "description": "Normalize source URLs and re-run check"
}
```


### [2026-09-06T02:34:34.246Z] TOOL RESULT

```
JSON OK
10
nodes verified: 18/18
node verdicts: {'disputed': 3, 'confirmed': 12, 'plausible': 3}
root verdicts: {'confirmed': 1}
ref checks: {'contradicts': 2, 'partial': 3, 'supports': 14, 'not_checked': 5}
books consulted: {'supports': 31, 'contradicts': 1, 'partial': 3, 'silent': 11} | by book: {'KLN': 9, 'AHD': 5, 'SKT': 5, 'POK': 4, 'IEC': 4, 'CHEUNG': 3, 'MON': 3, 'BRT': 2, 'PHD': 2, 'LAT': 2, 'SYN': 2, 'HRN': 1, 'BQT': 1, 'FVQ': 1, 'AFM': 1, 'PLA': 1}
```


## [2026-09-06T02:34:52.428Z] AGENT

Page 188 (book p.158) verified — `/home/sfmqrb/git/rishe/data/verification/page-188.json`, `verify_check.py 188` shows 0 PROBLEM lines (18/18 nodes).

**Counts:** root: 1 confirmed. Nodes: 12 confirmed, 3 plausible, 3 disputed. Ref checks: 14 supports, 3 partial, 2 contradicts, 5 not_checked (unreferenced pass-through boxes). 16 books consulted.

**Root** — POK:442 (gher-4 "to gripe, grab, enclose") and POK:444 (gherdh-/*ghordho-) are both exact; Watkins's AHD `gher-1` cites the identical page pair, so the chart is built straight from Watkins. Confirmed.

**Disputed:**
- **#1 Avestan/OP `zar 1, â-zâr, âzâra`** — Nourai's own ref Walde-Pokorny I 603 prints this family in a parenthesis of *exclusion* inside the gher- article ("gehört … zu ai. hṛṇīte"), i.e. it says these words do NOT belong to this root; Cheung *zarH1 adds "No precise IE cognates of this Iir. root are attested." Also: no Old Persian attestation, and Av. āzara- means "oppression", not "oppressed".
- **#3 Sogdian `ʾpzʾrn`** — real (Gharib p.55 no.1411, "©Av. zar-", "to disturb"), but it is *upa-* + *zar-*, a sibling of آزردن, not a child of PIE *ǵʰer- "enclose".
- **#10 Arabic `qarn`** — native Semitic q-r-n < *ḳarn- "horn" → "peers/generation" → "century". Nourai follows al-Unaysi (TAD:56), who does list it as a Greek loan from χρόνος; Wiktionary carries that only as a bare alternative, and Jeffery's *Foreign Vocabulary of the Qur'an* has no entry for it.

**Plausible:** #4 Greek khorós (AHD/Klein accept "enclosed dancing place", but Pokorny calls it "doubtful" on the very page cited and Beekes says the root's semantics are disputed); #9 khrónos (node reproduces Klein 284 verbatim, including his preform *ghr-on-os — Beekes: no etymology); #18 English `horticulture, court, courtesy, curtain` (only horticulture is from *hortus*; court/courtesy/curtain descend from *cohors*, a sibling branch — Watkins lists them separately and omits curtain).

**Extraction errors:** none. I rendered the printed page and compared every box: JSON is faithful (including `xorus`, `âzâra`, `ğr-on-os`, all refs and arrows).
