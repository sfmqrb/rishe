# Verification process log — verify-page-313


## [2026-09-07T01:36:58.997Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 313 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-313.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-313.json. Write /home/sfmqrb/git/rishe/data/verification/page-313.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 313` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T01:37:01.064Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T01:37:01.842Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T01:37:01.858Z] TOOL RESULT

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


## [2026-09-07T01:37:02.591Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-313.txt"
}
```


### [2026-09-07T01:37:02.612Z] TOOL RESULT

```
1	=== PDF page 313 (book page 283) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Leup : to break, peel off  (refs POK:690)
4	#1 (parent #0) [Avestan / Old Persian] refs=FFD:55 | rup,rupâ : to rob
5	  #2 (parent #1) [Pahlavi] refs=HRN:135 | rôp 1 : to rob ; kah-rupâti : amber ☞Kuâtos
6	    #3 (parent #2) [Persian] refs=BQT:938 | robŭdan «ربودن (ربایدن)» : to steal ; -robâ «-ربا» : attracting | extra: آهنربا ، کهربا
7	#4 (parent #0) [Sanskrit] refs=HRN:135; POK:690 | lôp : to rob ; lôtan : booty
8	  #5 (parent #4) [English] refs=KLN:905 | loot
9	#6 (parent #0) [Germanic] refs=AHD |  | NOTE: A group of words meaning bark peeled off trees, roofs made of bark, roof or top of a high place
10	  #7 (parent #6) [English] refs=None | leaf, lodge, loft
11	#8 (parent #0) [Latin] refs=None | 
12	  #9 (parent #8) [English] refs=None | lobby
13	--- entry 1 ---
14	ROOT Leuqos -> redirect to Leuk
15	--- entry 2 ---
16	ROOT Liginnu -> redirect to Lignu
17	--- entry 3 ---
18	ROOT Ligittu -> redirect to Lignu
19	--- entry 4 ---
20	ROOT [Akkadian] Lignu, Liginnu, Ligittu : a pot for measuring wheat  (refs AKD:21; BQT:1904)
21	#1 (parent #0) [Aramaic] refs=AKD:21; BQT:1904 | laqna, lakan, lagînâ : tub
22	  #2 (parent #1) [Arabic] refs=BQT:1904 | laqan : tub, basin
23	    #3 (parent #2) [Persian] refs=MON:3621 | lagan «لگن» : tub
24	  #4 (parent #1) [Greek] refs=BQT:1904 | lekaně : tub
25	--- entry 5 ---
26	ROOT Limŭ -> redirect to Nîmbû
27	
```


## [2026-09-07T01:37:06.433Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-313.json",
 "description": "Read source JSON for page 313"
}
```


### [2026-09-07T01:37:06.474Z] TOOL RESULT

```
{
  "pdf_page": 313,
  "book_page": 283,
  "entries": [
    {
      "root": {
        "name": "Leup",
        "lang": "Indo-European",
        "refs": "POK:690",
        "gloss": "to break, peel off"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:55",
          "words": [
            {"translit": "rup,rupâ", "gloss": "to rob", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:135",
          "words": [
            {"translit": "rôp 1", "gloss": "to rob", "script": null},
            {"translit": "kah-rupâti", "gloss": "amber", "script": null, "see": ["Kuâtos"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:938",
          "words": [
            {"translit": "robŭdan", "gloss": "to steal", "script": "ربودن (ربایدن)"},
            {"translit": "-robâ", "gloss": "attracting", "script": "-ربا"}
          ],
          "script_extra": "آهنربا ، کهربا",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "HRN:135; POK:690",
          "words": [
            {"translit": "lôp", "gloss": "to rob", "script": null},
            {"translit": "lôtan", "gloss": "booty", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:905",
          "words": [
            {"translit": "loot", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": "A group of words meaning bark peeled off trees, roofs made of bark, roof or top of a high place",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "leaf, lodge, loft", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "lobby", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Leuqos", "redirect": "Leuk"},
      "nodes": []
    },
    {
      "root": {"name": "Liginnu", "redirect": "Lignu"},
      "nodes": []
    },
    {
      "root": {"name": "Ligittu", "redirect": "Lignu"},
      "nodes": []
    },
    {
      "root": {
        "name": "Lignu, Liginnu, Ligittu",
        "lang": "Akkadian",
        "refs": "AKD:21; BQT:1904",
        "gloss": "a pot for measuring wheat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "AKD:21; BQT:1904",
          "words": [
            {"translit": "laqna, lakan, lagînâ", "gloss": "tub", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "BQT:1904",
          "words": [
            {"translit": "laqan", "gloss": "tub, basin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:3621",
          "words": [
            {"translit": "lagan", "gloss": "tub", "script": "لگن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Greek",
          "refs": "BQT:1904",
          "words": [
            {"translit": "lekaně", "gloss": "tub", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Limŭ", "redirect": "Nîmbû"},
      "nodes": []
    }
  ]
}
```


## [2026-09-07T01:37:08.524Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','FFD','HRN','BQT','KLN','AHD','MON','AKD','WLD','PHD','NYB','HUB','ARY','IEC','SYN','BRT','KNT','SKT','FSD','WEB','CHEUNG','FVQ','AFM','PLA','LKT','SOD','TTS']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T01:37:10.091Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verif
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
CHEUNG MISSING
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf",
```


## [2026-09-07T01:37:22.528Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T01:37:22.572Z] TOOL RESULT

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


## [2026-09-07T01:37:22.941Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo ---- && ls tools/"
}
```


### [2026-09-07T01:37:22.991Z] TOOL RESULT

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
----
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


## [2026-09-07T01:37:31.680Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"leup\" POK_full.txt | head -40; echo ===; grep -n \"leub\" POK_full.txt | head -40"
}
```


### [2026-09-07T01:37:31.724Z] TOOL RESULT

```
Exit code 1
34281:Old Prussian gleuptene^ mouldboard, curved metal blade on the front of a plow which 
49036:assumption secondary lengthened grade *kleup/b-ov\e has added Gothic hiaupan'ruvi, 
78065:in Germanic also *slub-{\u6o Germanic *sleup- or * sleu b'^ -): Old English sITefan 
78126:Root / lemma: (s)leup- (s)leub(h)- 
(eval):1: == not found
```


## [2026-09-07T01:37:32.868Z] TOOL CALL #8: Bash

```json
{
 "command": "ls data/verification/ | head -40; echo ===; python3 -c \"\nimport json;d=json.load(open('data/verification/page-309.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-07T01:37:34.063Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-07T01:37:41.513Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma\" POK_full.txt | grep -in \"leu\" | head -30"
}
```


### [2026-09-07T01:37:41.566Z] TOOL RESULT

```
269:14441:Root / lemma: b^leu-(k)-, (s-) 
270:14465:Root / lemma: b'^leus- 
271:14481:Root / lemma: b'^leu- 
274:14649:Root / lemma: b^leu-1: b^lau-: b'^lu-{*b'^\e\^-^) 
275:14725:Root / lemma: b^leu-2: b^lau-. b^lu- 
578:30429:name' see Root / lemma: Rleu-1, RIeua-. Rlu-\ to hear, cry). 
632:33365:Root / lemma: ghleu- 
657:34252:Root / lemma: gleUd^- 
943:47419:Root / lemma: klem-, klem-, kleUi- 
1075:51526:Root / lemma: Rleu-2: *Rld[u]- : Rlu- 
1076:51531:Root / lemma: Rleu-2. *Rld[u]-. Rlu-\ to rinse, clean, tear, derived from Root/ lemma: Rleu- 
1550:68259:Root / lemma: pleuk- 
1551:68283:Root / lemma: pl(e)u-mon-, pleu-tio- 
1552:68289:Root / lemma: pl(e)u-mon-, pleu-tio- : lung, derived from Slavic alb. prefix pe- + Root / 
1553:68308:Root / lemma: pleus- 
1554:68336:Root / lemma: pleu- 
1586:69225:Root / lemma: pi-lo- : hair' : Root / lemma: pu-lo- : hair' derived from Root / lemma: pleuk- 
1627:70479:Root / lemma: reuA^-{*uereuA'^^ (zero grade of *hieleuRh-) 
1795:78047:Root / lemma: sleub(h)- 
1796:78072:Root / lemma: (s)leug-, (s)leuk- 
1797:78100:Root / lemma: (s)leug-, (s)leuR- 
1798:78126:Root / lemma: (s)leup- (s)leub(h)- 
1799:78148:Root / lemma: (s)leu- 
2231:93753:Root / lemma: keleu-
```


## [2026-09-07T01:37:42.310Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lumpati\\|lumpáti\\|lupti\\|lopayati\\|lopáyati\" POK_full.txt | head -30"
}
```


### [2026-09-07T01:37:42.361Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T01:37:48.668Z] TOOL CALL #11: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['POK'],ensure_ascii=False,indent=1))\""
}
```


## [2026-09-07T01:37:49.759Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sleup\\|(s)leup\" POK_full.txt | head; echo ===; sed -n '78120,78160p' POK_full.txt"
}
```


### [2026-09-07T01:37:49.877Z] TOOL RESULT

```
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
```


### [2026-09-07T01:37:49.917Z] TOOL RESULT

```
Exit code 1
78065:in Germanic also *slub-{\u6o Germanic *sleup- or * sleu b'^ -): Old English sITefan 
78126:Root / lemma: (s)leup- (s)leub(h)- 
(eval):1: == not found
```


## [2026-09-07T01:37:54.139Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 690\\|Page(s): 690-\" POK_full.txt | head; echo === ; awk 'BEGIN{RS=\"\\f\"} NR>=345 && NR<=348 {print \"=== leaf idx \" NR-1; print}' POK_02.txt | head -160"
}
```


### [2026-09-07T01:37:55.351Z] TOOL RESULT

```
Exit code 1
56344:Page(s): 690-691 
(eval):1: == not found
```


## [2026-09-07T01:37:57.850Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '56290,56350p' POK_full.txt"
}
```


### [2026-09-07T01:37:57.908Z] TOOL RESULT

```
With bh/ 



Latin liber^basi, book' {*luber, *lLt!^-ro-s); 

Alb. liber, libri: Furlan //M" book ' Latin loaword. 

alb. labe^bark, cork' {VoiJci^-); 

Old Irish luib, nir. luibht 'herb', Old Irish /ub-gorf' garden', acymr. PI. /u/rd' gardens '; 

Gothic A/i&y5-/e/5 "poison-expert', Old Icelandic /yfi. ' medicinal herbs ', Old English /ybb 
n. " poison, charm, spell', lyfesni. "charm, spell'. Old Saxon lubbi. Old High German luppi^ 
plant juice, poison, charm, spell'; Gothic laufsm., laufu. " foliage, leaf. Old English leaf. 
Old High German loubu. ds., loubai. " shelter of bark'. Modern High German Laube; 

Lithuanian /i//75 "board', Latvian luba^ shingle ', Old Prussian lubbo^. "board', ablaut. 
Lithuanian luobasm. " bark, outer covering of a tree ' {*ldUb^os), Latvian luobsm. "bowl'; 
Lithuanian lubena' fruit bowl '; 

russ. lub^ bark, bast', etc.. Church Slavic /b/ji. "cranium', serb. Iublna6s.; 

With p: 

Old Indie lumpatr breaks, damages, loots ', lopayatr injures ' (= Slavic lupitl, 
Lithuanian laupyti), ldptra-v\. "swelling, blister'; 

gr. Aunri f. "injury', Aunsu) " sadden ', etc.; 

Lithuanian lupu, luptF skin, peel ', Latvian lupVds., mug, rob', Lithuanian laupyti, 
Latvian laupiC peel, exfoliate; rob', Lithuanian lupena^ fruit bowl ', A/yOS/7/s ^^eschalte 
Tannenrinde '; 



31 



russ. luplju, lupftb " schalen, abschalen; aufpicken Eier; die Augen aufreiflen, glotzen' 
schlagen, prugein ', lupa^ dandruff, flaky scales of skin ', Church Slavic lupezb " robbery ' 
(etc.); 

unclear is the labial {b, b^ or p) in Middle Irish luchtar^boat' (from bark). Old High 
German lofujff^bark, bast'. Old Icelandic loptr\. " ceiling, attic ' and "air' ("sky, heaven as 
top cover '), Gothic luffust, ahd Old Saxon luftm. f., ags lyftm. f. n. Luft^a\r, sky, heaven', 
Middle Low German lucbf upstairs, loft '; also unclear in Old Irish lomm, cymr. Ilwm "bare, 
naked' {*lup-smo- or * lub{h)-smo-), (common Albanian Celtic abbreviation) Middle Irish 
lommralm^ peel '; unclear is Middle Irish /i//77/775/7 "covering'. 



References: WP. II 417 f., WH. I 790 f., Trautmann 150 f. 
Page(s): 690-691 



Root / lemma: lehb- lohb- lahb-, leb- 

Meaning: to hang down loosely; lip
```


## [2026-09-07T01:38:00.450Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '56255,56292p' POK_full.txt"
}
```


### [2026-09-07T01:38:00.500Z] TOOL RESULT

```
get lost ', Old Icelandic losna^ loose, become lax ', /osa 'loosen', postverbal losu. " lysis, 
dissolution, disintegration ', Old English losian^ get lost ', Denomin. to losu. 'loss'; lysu 
"evil, bad, mad, wicked, evil' {Vahusiwa-), Gothic fralusts. Old High German for/ust '\oss'; 
Gothic /aus loose, empty, lacking'. Old Icelandic /auss'free, loose, scattered ', Old High 
German /oslree, stolen; looted, loose ', Old English /eas' empty, bare, lacking, stolen; 
looted, deceitful ', Old Icelandic lausungi. " Unzuverlassichkeit ', Old English /easung'We, 
falsity', /eas/an'We'; Gothic lausjan. Old High German losian, loson ' draw lots for '; 
perhaps Old Danish liuskem. " flank ' > Old Icelandic Ijdski, Middle Low German lesche. 
Middle Dutch liesche. Modern Dutch lies. Old English leosca "flank', as well as Middle 
Dutch liesche ^\.\\\v\ skin', Swiss losch^ lax '; with a meaning" hit, knock ' probably also Old 
Icelandic IJosta^hW., prick, meet', IJdstr^ Gabel zum Fischstechen ', nisi. /^s//'"cudgel, club' 
("*chopped branch piece' ); 

as old this application is proved, if Middle Irish /oss "tail, end', cymr. //cs/"spear, javelin', 
llosten'taW, bret. /c»s/"tair are to be added; 

here (Specht Indo Germanic Dekl. 56) Latvian lauska'spWnter, shard', ablaut. Lithuanian 
luskos'rag', luzgana'husk, scale, husk ', lusna'husW, bowl', russ. lusta ds., etc. Possibly 
related is Ve/?:/- "stone', see there. 

References: WP. II 407 f., WH. I 830, 834 f., Wissmann Nom. postverb. 84 ff.; from 
vorrom. and proto Germanic *leiska, *leuska, *laska\n Modern High German Lische, 
French laTcheeic. " a reed grass, sedge ' reconstructs J. Hubschmid ZcP 24, 81 ff. an Indo 
Germanic elehi-, elehu-, e/a-"cut, clip'. 
Page(s): 681-682 

Root / lemma: /ehup- and lehub-, lehilo^- 
Meaning: to peel, cut off, harm, etc.. 
Note: probably extensions from leu-2. 
Material: With b: 

Old Icelandic lauprrw., -leypiu., -leypai. " basket, woodwork ', Old English leapm. 
"basket, trunk'. Middle Low German Idpxu. " wooden vessel', laepenu. "basket'; the Balto- 
Slavic examples under can contain bas b^'just as well. 

With bh/
```


## [2026-09-07T01:38:24.073Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==347' POK_02.txt | head -60"
}
```


## [2026-09-07T01:38:24.754Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT raop/urup\"; grep -n \"raop\\|urup\\|rufra\" BRT.txt | head -30; echo \"== CHEUNG raup\"; grep -n \"raup\\|\\*rup\" CHEUNG.txt | head -30"
}
```


### [2026-09-07T01:38:25.338Z] TOOL RESULT

```
scheinlich lüma  , Minze (?)'  aus  *l^g(s)mä'^
air.  fo'long-  ,(er)tragen'  (aus  *-lung-)',
lit.  lilgnas  ,geschmeidig,  biegsam';
ahd.  loc,  nhd.  Locke,  ags.  locc,  aisl.  lokkr  ds.,  aisl.  lykna  ,die  Knie beugen' ;
mit  Abtönung  daneben  vielleicht  ahd.  louh,  nhd.  Lauch,  and.  lök,  ags. Uac,  aisl.  lauki'  , Lauch';  aus  , biegen,  zusammenbiegen'  scheint  die  Be- deutung , zumachen,  schließen'  entstanden  zu  sein(?)  in  got.  ga-lakan , einschließen',  us-lükan  , aufschließen',  aisl.  lüka  , schließen,  aufschließen, beendigen',  ags.  lücan  , schließen,  öffnen',  ahd.  lühhan  , schließen',  ant- lühhan  ,aufschließen';  aisl.  lok  n.  , Schluß,  Verschluß,  Deckel',  loka  f.  ,Ver- .  Schluß,  Riegel',  lykja  ,schließen',  ags.  loc  n.  , Verschluß,  Riegel,  Gefängnis',
686
ahd.   loh  n.   , Verschluß,  Versteck,  Höhle,  Loch',  got.  us-luk  n.  ,Öffnuno-^. ahd.  lucka  (*lukkja)  ,Lücke^,  ndd.  Luke. WP.  II  41 3  f,  WH.  I  826  f.,  831.
2.  leu-g-  :  lu-g-  :  lü-g-  , schwärzlich ;  Sumpf'  (nach  der  Farbe).
Gr.  Xj)ya.iog  , dunkel,  finster',  wozu  (mit  Präf.  ij-,  vgl.  ai.  ä-nlla-  ,schwär2. lieh')  '?jV6yrj  , dunkel',  infjXv^  , (wobei  Dunkel  ist  =)  schattengebend',  ^^,. Xv/d^oi-iaL,  -L^o^ai  , überschatte,  bedecke';
illjr.  lugas  m.  oder  luga  f.  , Sumpf  (Strabo  314:  eXog  ^ovyeov  xcyjlotj." fiEvov  bei  TsQyeats),  wovon  mit  dem  lat.  Formans  -ätum  abgeleitet  alb. legale  ,Lache,  Pfütze,  Sumpf;  lit.  liugas  , Morast',  daneben  lügas,  lett.; FIN  Ludze  (*lugj,a);  idg.  Hougiä  in:  russ.-ksl.  lu^a  , Sumpf,  Pfütze',  usw.»*
vielleicht  hierher  gall.  Xovyog  ,Rabe'  im   ON  Lugu-dünon  ,Lyon',  usw.'
WP.  II  414,  Trautmann  163;  zu  1.  leu-.
leug-  ,brecben',   im  Ar.  mit  ^,    im  Balt.  mit  ^;   ar.  g  wohl  durch  Einfluß^ von  leug-  ,biegen'.
Ai.  rujdti  , zerbricht,  peinigt',  rugnd-  , zerbrochen',  -ruj  f.  , Schmerz, Krankheit',  rujä  ds.,  röga-  m.  , Gebrechen,  Krankheit',  logd-  ,Erdkloß, Scholle';
av.  uruxti-  ,Brechen,  Zerreißen';
arm.  lucanem  ,löse  los,  breche  auf,  loic  ,losgelöst,  frei';
gr.  ä-Xv'KTO-Ttidr]  ,unzerreiß bares  Band',  XevyaXiog,  Xvygög  ,traurig,  schreck- lich';
alb.  lunge  , Geschwür';
lat.  lügeö,  -ere
```


### [2026-09-07T01:38:25.395Z] TOOL RESULT

```
== BRT raop/urup
2105:GnmpQjBk.:  Gurupfljakaumudl.     Festgabe  ..  AWEBEK  dargebracht     Leipzig  1895. H.:  Haicxt  Nash;  s.  S.  ix.  4,
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
6037:j.  azina'vant-  Adj.  'wachsam,  regsam"': iaxmS  urupa   'vä  Yt  75. 11 ;   —  taxm?m
8836:yazäite  kö^  .  .  kahmäi  raisca  s^armasea kahmai . .  dnatät)m  ..  baxsäni . .  kahmai"  . . Yt  i0.io8-iio;  —  kü  nd  stavat  kff*  .  . kahe  nS  i',a  nama  äfairyüt  kakmäi  nö  tat dii>nm  dayiit' yal  ..  Yt./j.So;  5.8-",  A*. 15',  /./.473;  —  k5  'i'Wam  . .  inaoili  ks .  . /iaesayati  \.iX6i;  Y.^.SPUZ.,  V.;.'.4a; —  kasp  "iwqm  paoiryö  . .  masyö . .  hunüta ;Y.»),3;  V.J.12,  20.1;  —  kahmai  tnit .  'iwarözdüm  k3  mä  iasat  Y,  29.  i ;  —  kS  . . raocascä  däi  t^mäs/ä  V.44.S}  $',  3.  4% I  7',  46^.14,  5/.  11^;  —  kasil  7'oha  manaukä •yi  T  däyät  (sd.)  ^'.-.iff-T,  —  köi  ^drjgTl-.- dtbis  . .  nlmqm  dtiiili  "wer  sind  sie,  die  . ." V.  4Ä  1 1 ;  — '  k3m  nS  mavaite  (sd.)  priyum dadäty.4J).T,  —  *kaAe'>  *nä  *ga-.'a  ratu- fris  N.  54 :  —  ksm  hsi  ustä  (sd.)  ahunm Y.  251.2;  —  \ctm  i(\Sia.)  främraop  asa- .van3m  .  .  Y.ig.20;  20. n;  —  kat  faslY.
12283:•  j.  tizi.daä-  Adj.  (mask.  'ta-)  'mit scharfem  Gebiss':   urupii  (sd.)   'iahe  V,
15273:KompE.  —  Vgl  pa%i:  fa%ii-  und  J  3/3.  1  b, 3iß.  1,  3gi.—  a.\.pBiUkäk,  pathäh;  l'Di.punJ, oosi.  fändäg  'Weg',  np.  fand  'Rit'.  —  Pfi. : rät;  s,  noch  No,  3.  —  ")  Nur  YL  13.  53. — ')  Sp.  232  o.  VgL  pinikä  j-täsya  RV.  /^.  136. 2  a.  Ö.  —  3>  Falsch  %  331.  V^.:  pa  an  i vahuman  fiatü,  erL ;  frärön  latJärlA  röi  ya! alt.  —  4)  Vgl.  ai.  palhas.  n.  (woiu  fccÜich Sie«  GurupDjsk.  97 ;  aber  dagegen  wieder Oldenbbkg  ZDMG.  $4.  599).
20661:mit  paiti  und  a  'ankündigen'  (etwas: Akk.,  Jemandem:  Akk.,  fiir  -:  Dat)^: cfm  aSaya  paiti.vaca  paityämraop  usta- tätfm  paityamraot  ustataityaca  vTsp>m  asa- vatum  .  .  vahistim  paityimraoi;  vahistB mazdä  paityämraot  vahistsm  aiavanjm vahistäi  alaone  "vias  hat  er  mit  diesem Spruch  angekündigt?  Das  'Nach wunsch- gehen' hat  er  angekündigt  und  mit  dem Worte  'nach  Wunsch'  hat  er  jedem  Gläu- bigen . .  das  Beste  angekündigt.  Der  beste J/.  hat  es  dem  besten  Gläubigen  (d.  i. Zar.)  für  (je)den  besten  Gläubigen  ange- kündigt" Y.  21. 4.
20781:—  ayä  ..yayH  kaantl  urvqnS  Y.jj.g;  — ahy/t  *Madahyä  .  .  yä  (ISm.)  karapanö urupayeintl yäcä  ..  duhxsa^rä  Y.4S.J0;
24751:para.iri^yeiti  V.  /j.  50;  —  yat  ahmi  spa- 1  mit  paiti  'mittelbar,  indirekt  in  Beriih- nas^'a  narasca  para.iri>inti  V.6.i;  —  i  rung  treten  mit  -,  Einfluss  üben  auf  -'*> sBnS  vä  para.iristahe  masyehe  vä  V.  G.  \  (Akk.):  cvai  alls  spä  yö  urupis  spmtahe 10,42,  7-24;  —  vJspanqm  ahmya  nmäne\tnaiHy3ui  dämanqm  hqm.rat%wayeiti  cvat fiabänazdisianam  para.iristanqm  ,  .  fravO' \paiti.ra€%wayeiti  "auf  wie  viele  von  den sayB  V.2Ö".7;  —  pasca  /ura./rij/a/r«' Geschöpfen  ..  erstreckt  der  Hund  .  .seinen ma^yeie  pasca  /rasaxtahe{^ä.)  masyehe  V, ;  Einfluss  direkt,  auf  wie  viele  indirekt?"  V, ir).2&;  —  ä  dirn  aoxta..pourvü{%^.iTi  u.)  J.  33.  a)  insbes,  von  ansteckender,  ver-
24960:•  j.  raopay-  ra.  Name  einer  Art  des Hundegeschlechts:  hnu  'pis  (statt  GS.) yaoni>.x''alaAe  hSu  vTspanam  .  .  spaa'hra- nqm  .  .  V./?.  16.
25526:•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
26822:paiti  irista  bazaiti  V.ij.g;  — spanaÄe'\ V.y.48  PüZ.;  —  Sing,  in  koUekL  SbnJ äal . .  ahe  tunanahe  . .  /rapi'iwS  (sd.)  spä  ! V.^.j;  —  taiHl  ya  bavainti  aos5.tarash .  .  yäha  anya  spa  V.  13.  42  (?).  a)  im Gegensalz  zu  Menschen  und  zu  andern Tieren :>'((/ii>4mi  spanasca  narasta  para.- irtiinti  V.5.  ij^.s,  u,  36,  8. 14;  —  yai ahmi  nmäne..spa  va  na  va  iri^yai  V.Ä  4; '>  5-  39;  —  y^  asiim  upanhanzaiii  sBnS va  para.irittahe  maryehe  vä  y.6.  10;  12, 7.23; —  *näirikayä  hhrpa  ..sunü  kihrpa N.jp;  —  pasvamca  slaoranqmca  masya- nqmca  saiiamla  vayqmca  V.  2.  8; — pasca . .  nasäum  ava.kar>i>nti  spstum  vä  raoz»m va  v>hrk3m  va  V,  5.  5;  6.50;  —  yahöit dim  . .  avaxanan  süns  (NP.)  va  hnß.- ifardvayB  va  V.ö.^s;  46,7.29,  30;  — j/J vä..vay5vä  hn/sji^aroFr'W.li.  A)  mit Bezeichnung  der  besonderen  Art:  spä pasusJtaurvS^''  .  .  spä  vU.kaurvS''''  .  .  spa vohuna^B^^ ..spa  taurunö'''^..spa  sukurmd*''> . .  spa  jaiui^^ . .  spa  aiwinu/'''' . .  spa  vltus''^ ..spa  urupis"'^'  V.  5,  29-33;  —  späntm slidnm  urvUarsm  yim  vat»hapar>m^^  V. 13.3;  —  ys  aSa^qm  sünam  Jainti  yim pa^us.kaurvqmca  viLhaurvqmca  vohuna- sgqtnea  draxtS.hunaranqmia^^  V.  13. 8,  42 ;
== CHEUNG raup
13248:*Hraup 195 
13280:*Hraup ‘to tear, break; to suffer from pain’ 
13302:see *raup. = EWAia II: 469 f., 482 
13304:© To the root *raup a number of forms with a wide range of meanings has been 
13384:<-r->, also in MMP hrwb- ‘to collect, gather; receive’ (< *ham-raup). Incorrect 
14684:similar Skt. connection is semantically implausible (*raup?). The root *jaup may be 
16615:the Pth. verb ywb- ‘to suffer, complaint, lament’ (*raup'), which is semantically not 
20938:*raup 1 319 
20981:*raup! ‘to take away, up, rob, cueillir 
21001:320 *raup2 
21014:Ó In view of the semantic similarity, the root *raup? is perhaps connected with Skt. 
21015:yop. The initial r- of *raup^ should therefore be regarded secondary and may have 
21025:*raup2 ‘to sweep’ 
21058:This root is probably originally identical to *raup', which has developed a more 
23977:may be explained differently, v. *raup, *jaup?. 
55795:*braj,*(H)raud, *Hraup, 
56034:(s.v.), *raup! (s.v.), *skar 
57649:*HuarH, *raup! 
58093:*baid (s.v.), *Hraup, *rais, 
58105:*raup’, *star 
58116:*raup', *zaiH 
58136:*Hraup, *xrau
```


## [2026-09-07T01:38:31.603Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20938,21065p' CHEUNG.txt"
}
```


### [2026-09-07T01:38:31.653Z] TOOL RESULT

```
*raup 1 319 


additional -d- of MMP rwzd- may point to denominative origin or reflect a pres. 
stem in *-d-, cf. CSogd. sxwrd- ‘to shout’ (*huar?). || According to Henning 1945: 
487, fn. 2, the Persian and Parthian ‘desire, lust’ forms derive from *barj, which is 
semantically implausible. A more suitable root is *rauf. The Manichaean and 
Pahlavi forms perhaps reflect the different outcomes of syncope of the zero grade 
stem vowel: *á-ruj? > *ar"z° > MMP /awrz?, BMP /ärzY. Alternatively, MMP 


/awrz’/ reflects a Pth. development (or pronunciation). > DMMPP: 303b, 70b 

Partic.: pres. MMP rwzd’n, perf. pass. MMP rwzdyst, rwzdyst 

*PARTHIAN: (+ *а-) 'Wrjwg, "wrjwq ‘desire, lust’ (see above) || (+ *ui-) wrws- ‘to 
desire, sigh’ = Ghilain: 70a, 49 f. | DMMPP: 345b 

Pres.: IND. 3sg. wrwsyd, IMPV. 2sg. wrws 

*KHOTANESE: rrauta- (Ё), (with palatalisation) LKh. r(r)is’a- ‘desire’, LKh. a-risai’ 
(+ neg. a-) ‘stinking’, LKh. rais’a- ‘appetite’ || (+ *a-) ? araus- ‘to please’ (Bailey, 
KT III: 58,26) 

*SOGDIAN: CSogd. rwZ ‘to desire’, CSogd. rwzty’ (Е) ‘desire’, also with palatal- 
isation (GMS: $187), SSogd. ryz, BSogd. ryz, CSogd. гуў (denomin., impers., only 
3rd pers.) ‘to be pleasing, be desirable’, BSogd. ryz, ryzh, CSogd. гу? (m.) ‘will, 
wish, desire’ || (+ *a-) MSogd. ’’rwytky’ ‘greed’, MSogd. ’’rwxst (Apl.) ‘greeds, 
desires’ 

Pres.: IND. 2sg. dur. CSogd. rwZysq, 3sg. CSogd. rwžt, Partic.: pres. CSogd. rwZnyt (pl.) ‘desiring’ || 
denomin.: Pres.: IND. 35р. SSogd. "ryzt skwn, BSogd. ryzt, CSogd. ryzt, SUBJ. 3sg. BSogd. ryz’t, 
SSogd. ryz’t, CSogd. ryZt, etc. 

*NWIR: NP rez ‘desire’ (< Sogd., Henning 1939: 99) || (+ *a-) NP ärzö ‘desire, wish’ 

9 An IE provenance for this root cannot be established. 

*PIE — = LIV: — | Pok.: 

*REFERENCES: BBB: 566; DKS: 369 


*raup! ‘to take away, up, rob, cueillir 

*MIDDLE PERSIAN: BMP Iwpk /robag/, BMP Iwp /rob/ ‘pillage, plundering’ || (+ 
*ham-) MMP hrwb- ‘to collect, gather; receive’. 0 The cluster *-mr- in MMP hrwb- 
has been assimilated: MMP -rr- <-r->. > DMMPP: 185a 

(+ *ham-) Pres.: IND. 3sg. MMP hrwbyd, SUBJ. 152. MMP hrwb’’n, 2р1. MMP hrwb’d-, IMPV. 25р. 
MMP hrwb; Partic.: perf. pass. I MMP hrwpt, hrwpt, П MMP "hrwbyhyst 

*KHOTANESE: rrv- ‘to remove, peel off? || (+ *ш-) LKh. bur(r)v- (burtivafi-) ‘to 
destroy’ — SGS: 117, 101 

*SOGDIAN: BSogd. гур ‘to gather’, CSogd. гур ‘Өғрібо’, MSogd. гур ‘to harvest? 
Pres.: IND. dur. 1sg. CSogd. rwpmsq, 2sg. CSogd. гуру ‘OepiCetc’, SUBJ. 3р1. MSogd. "rwp’ndt, Impf.: 
IND. 3sg. BSogd. rwp’ 

*CHORESMIAN: rwby- ‘to rob; take away [of horse]’, ? m/rwBY- ‘to take with one’s 
fingertips’ > Samadi: 173 f. 


320 *raup2 


*NWIR: NP rubodan/rubay- ‘to rob, seize, carry off; to withdraw from sight’, (opp) 
rubödah ‘seized, plundered, robbed’, Bal. rupt/röp- ‘to collect’, Gz. rübä-/rübä, ? 
Kurd. fifanin, бгапіп, Awrom. arfáy/-rfán- ‘to snatch’, Gur. (Kand.) rifanin ‘to rob’ 
|| (+ *ш-) Kurd. (Kurm.) guramgure-, gurö-, (Sor.) gurun/guru- ‘to skin, remove 
(skin)’ 

*NEIR: Yghn. rup-, rub-/rüpta, rübda ‘to harvest’ 

*SANSKRIT: ? yop ‘to wipe out, efface, remove, erase’ (RV+) = EWAia II: 420 

Ó In view of the semantic similarity, the root *raup? is perhaps connected with Skt. 
yop. The initial r- of *raup^ should therefore be regarded secondary and may have 
been imported from (for instance) *rauH. As for an IE provenance, Skt. yop is 
connected to Gr. үзү ‘vulture’, which is analysed as a compound *g”u-jup- ‘taking 


away cows’ by Thieme 1954: 569, n. 2, but this analysis remains rather conjectural. 
*REFERENCES: KPF II: 199; Andreev — PeSéereva: 316a; MacKenzie 1966: 88; DKS: 367a; 298a f.; WIM 
II/1: 82; Kümmel 2000: 410 f.; Cabolov 2001: 405 


*raup2 ‘to sweep’ 
*MIDDLE PERSIAN: MMP “rwb-, BMP Iwp- /röb-/ ‘to rub, sweep’ || (+ *ui-) MMP 


wrwb- ‘to sweep down, away’ = DMMPP: 297b, 345b 

Inf.: MMP *rwptn || (+ *ui-) Pass.: pres. IND. 35р. wyrwbyhyd; Inf.: MMP wrwptn 

*PARTHIAN: rwb- ‘to sweep’ (Sundermann 1997: 62, line 40k). Ф On rwbysn 
‘change, Wandel (Mir. Man. III: 875) see *jaup^. > Ghilain: 65 f. | DMMPP: 297b 
Pres.: IND. 35р. *rwbyd {hapax} 

*KHOTANESE: (+ *4-) OKh. arüh- (ärau-) ‘to move, shake’ = SGS: 11 

*SOGDIAN: (+ *upa-/apa-/pari-) BSogd. pr’wp- ‘to sweep’ 

Pres.: SUBJ. 35р. pr’wp’t (Dhy. 1); Inf.: BSogd. pr’wp’y (Dhy. 68) 

*CHORESMIAN: rfš (f.) ‘broom’ 

*NWIR: NP röb-/ruftan ‘to sweep, dust’, Bal. rupt/röp- ‘to sweep up’, Kurd. (Abd.) ti- 
ruf- (supplet. inf. mestén < *Hmarz), Anar. ha-..-ruft/ (impv.) ha-ru, Gz. rön-/ruft, 
rona, Kesh. rutmiin/a-rov-, Khuns. rü-/ruft, Qohr. rüten (supplet. a-reg-, impv. bä- 
rug < *rauj'), Sang. hö-ründen/hö-rün-, Shamerz. be-rüten/rüm-, Von. ruften/er-rü-, 
Zef. bo-ruft/rov- ‘to sweep, wipe’ || (+ *ui-a-) NP jaru ‘broom’ (dial. ?) 

*NEIR: Sh. rüb-/rüvd, Rosh. rub-/rubt ‘to sweep up, shovel’, Pash. rabaj, Bart. rafc 
(Ё) ‘broom’, Yzgh. гаі ‘broom; name of a plant’, Yzgh. rabag ‘wooden shovel’, 
Sangl. ref ‘broom’, Yi. rufó ‘small, soft broom’, M. réfiko ‘mill-broom’, Wa. ropk 
‘trash, garbage’ || (+ *fra-) Yi. faru ‘mill-broom’ 

*MISC: Par. rüy-/rüt ‘to sweep’ 

This root is probably originally identical to *raup', which has developed a more 
specialised meaning ‘to sweep’. 


*rauxsn 321 


*REFERENCES: Zhukovski I: 134a f.; Zhukovskij II: 234b f.; Ivanow 1926: 421; IIFL I: 285b; IIFL II:
```


## [2026-09-07T01:38:46.853Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13240,13320p' CHEUNG.txt"
}
```


### [2026-09-07T01:38:46.905Z] TOOL RESULT

```
*SANSKRIT: rav ‘to roar’ (RV+) > EWAia II: 439 

9 In some East Iranian languages an unexpected labial fricative *B (< *-b-) is found, 
which perhaps points to contamination with *uab/f'. 

«PIE *НзгеиН- ‘to roar’ = LIV: 306 | Pok.: 867 


*Hraup 195 


*IE COGNATES: Gr. фрдорол ‘I howl, roar’, Lat. rumor (m.) ‘muffled noise, 


mumbling(?)’, OCS revo (mun) ‘I roar’ 
*REFERENCES: IIFL II: 244b; Abaev, Slovar’ I: 57; Andreev — Pe&éereva: 312b; EVS: 86b; Gharib: 341a; 
Werba 1997: 371 f. 


*Hrauj ‘to belch’ 

*KHOTANESE: rujai ‘bursting, ejecting, belch’ 

*CHORESMIAN: (+ *uz-) m/wzrzy- ‘to belch’ > Samadi: 229 

*NWIR: NP rug (тоё ?) *eructation' || (+ *а-) NP arogidan/ardg- ‘to belch’, NP arog, 
Gz. ardq ‘belch’ 

*NEIR: Sariq. re(w)y ‘hiccup’, rey ‘belch’ || (+ *а-) Pash. arZai (m.) ‘eructation’ (< 
*4-rux-S° ) = argay (m.) ‘belch, sour eructation’, argamdy (f.) ‘yawning’, (Wan.) irZa 
‘fart’, Yi. araröy, M. yoruya, Sangl. arok ‘eructation’ 

«PIE *H,reug- ‘to belch, vomit’ => LIV: 509 | Pok.: 871 

*IE COGNATES: Gr. epev yopar ‘I vomit’, Lat. e-rügö ‘I burp’, OCS rygajo se, OLith. 
raugmi, Lith. riáugiu (ridugéti) ‘I belch’, OHG ita-rucken ‘to ruminate’ 

*REFERENCES: Horn 1893: 5; EVP: 12; IFL П: 1916, 381b; EVS: 66b; DKS: 365b; МЕУР: 10 


*Hraup ‘to tear, break; to suffer from pain’ 


*AVESTAN: OAv. rüp- ‘to have/cause physical pain’ — Liste: 60 

Caus.: pres. IND. 3р1. OAV. urüpaiieinti (Y 48.10) 

*MIDDLE PERSIAN: MMP ywb- ‘to suffer, complaint, lament’. > The initial y- may 
point to contamination with a semantically related form, e.g. MMP yask ‘sickness’ 
{hapax}, Pth. ywz- ‘to agitate’. = DMMPP: 374b 

Pres.: IMPV. 2pl. MMP ywbyd 

*PARTHIAN: ywb- ‘to suffer, complaint, lament’ = Ghilain: 65 | DMMPP: 374b 

Pres.: IND. 15р. ywb’m, 35р. ywbyd, 3р1. ywbynd; Partic.: pres. П ywbyndg’n (pl.), perf. pass. ywb’d 
*KHOTANESE: OKh. rruh- ‘to harm, injure’ {hapax}. Ф Perhaps not ‘to attack’, as 
translated by Emmerick. = SGS: 117 

*SANSKRIT: rop ‘to suffer (from abdominal, stomach pain)’ (AV+ ?) || lop ‘to break 
up, injure’. Ф The Skt. is compared to the Ir. ‘to take away, rob’ forms (NP 
rubödan/rubäy-, etc.) in EA Waia, Le, which is semantically improbable, on which 
see *raup. = EWAia II: 469 f., 482 

© To the root *raup a number of forms with a wide range of meanings has been 
assigned, not all of which can be linked so easily or naturally. Although it is 
generally assumed that Skt. гор ‘to suffer from pain’ and lop ‘to break up, injure’ go 
back to the same root originally (IE *(H)reup -), which would consequently also 
apply to the Ir. forms, this is semantically not further explained. The meaning 
apparently depends on the stem formation (LIV: l.c.). The *ia-formation rupyati 
expresses the state of the subject (cf. Kellens 1984: 125), whilst the nasal formation 


196 *Hraxs 


(lumpati) expresses the external harm caused by the subject. This semantic 
distribution is comparable to *darH. 

«PIE *Hreup- ‘to break, tear’, i/,-formation *Hrup-i°/,- ‘to suffer pain’. 0 The recon- 
struction of an initial laryngeal is based on the premise that IE roots cannot begin
```


## [2026-09-07T01:38:48.357Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=155 && NR<=158' HRN.txt | grep -n \"\" | sed -n 1,10p; echo \"== grep robudan/rubud\"; grep -n \"rubüdan\\|rubudan\\|robudan\\|ruböd\\|rubäy\" HRN.txt | head -20"
}
```


### [2026-09-07T01:38:49.575Z] TOOL RESULT

```
1:— 138 —
2:596. dltn i^dem) ') *Geöiclit, Waiigun , dliue,
3:aw. daeman- ; plilv. andemän\kar 'empfangend,
4:führend', päz. andlmdnl 'entgegen, vor; arm. LW.
5:dem, det, y-andman (Hübschmann, No. 88).
6:kurd. LW. djm\ bei. LW. dem (80); afy. leina
7:'Pupille.
8:597. dtn 'Glaube, Religion*.
9:aw. dafwö-; phlv. diu bezw. den, paz. diu, dlmk,
10:arm. LW. den.
== grep robudan/rubud
5438:np. rubäyem geht auf älteres *rupäyati zurück.
```


## [2026-09-07T01:38:57.704Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5420,5450p' HRN.txt; echo \"=== which leaf\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"rubäyem geht auf\")>0) print \"leaf record\", n}' HRN.txt"
}
```


### [2026-09-07T01:38:59.021Z] TOOL RESULT

```
Phlv. rayinTtan, räyma, räyln(i)sn, räymitärih (Men.),
jüd.-pers. pJN^NI (Is. 63, 17) sind nicht klar.
607. rah^ ras ^), reh *Weg ; espyes.
skr. vergl. rathyd- Xandstrasse' (spät) 2); phlv. reis,
aspjräs; af/. lär^),
LW. kurd. rl; bei. ra, n. rah (219); af/. räh;
arm. rah.
Gehört hierher auch np. reste^i (phlv. rastan, Men.),
Praes. reh-em^ rehlden u. s. w. 'befreit werden, ent-
kommen', wörtl. 'sich auf den Weg machen'?**)
608. rubüden 'wegnehmen, rauben', Praes. rubay-em,
riibäyende ; ruften 'fegen , gäten', Praes. röb-em,
ai. V^löp' (älter röp-) 'zerbrechen, packen, plündern,
rauben''^); phlv. röp 'Raub' (AV.-GL), kah]rupäl 'Bern-
stein (Säy. näsay. II, 115); got. biyaubön 'berauben'.
bei. röpcifj 'fegen, kehren' (329).
ö hat noch Kää. Z. böröw (Impt.), börowön (Aor.),
rowon (Praes.).
np. rubäyem geht auf älteres *rupäyati zurück.
^) BQ. Rückert bei do Lagarde, Ges. Abh. 51, Note l.
^) Aw. hizvö raiHm (y. 50, 6) beisst iiacb Bartholomae,
KZ. 28, 34 *Lenker der Zunge*, siehe aber Geldncr, KZ 28, 259.
') Aus *ral (Trunipp, Graramar of the Tastö § 7); //är,
Darmesteter, Ch. pop., p. CLXXV, Note 2.
*) AM. 183 Zeile 1 hat aUerdings biriheS,
^) Aw. urüpay^intl (y. 43, lÜJ muss als unsicher bei Seite ge-r
lasäcn werden.— 136 -
609. reje^ reze *Reihe\
aw. razista- ^geradester ; ai. räjistha- (Nöldeke,
mündliche Mitteilung). Jüd.-pers. T]T\ dagegen dürfte
zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
=== which leaf
leaf record 157
```


## [2026-09-07T01:39:23.413Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD\"; grep -n \"rōb\\|lwp\\|rwb\\|rubāy\\|kāh\\b\\|kahrubā\\|kah-rub\" PHD.txt PHD_mackenzie.txt | head -30; echo \"== NYB\"; grep -n \"rōp\\|lwp\\|kahrup\\|kah-rup\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T01:39:23.476Z] TOOL RESULT

```
== PHD
PHD.txt:227:azbāy- [*2b*d-] invoke. ~išn: invocation. azd [zd | = M] known. Azdahag Pcydi’k' | M ?zdh?g, (N aždahā)] a legendary ‘dragon’ king, Dahāg. azdénidan, azdén- Pzdyn-ytn'] inform. azēr [%cdl | N zér] below, under. azg [22 | N аху) branch. aziš [hcf | М *cy$, 22у] from him, it; postposition (= az) from, ~-keh [-ks] inferior, subordinate. ~-meh [-ms] superior. āz-kāmaģ [?ck’mk'] greedy. ~ih: greediness. azmüdan, azmāy- ['zmwtn!,?zm'd- | N 2~] = uzmüdan. aznawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be extinguished. āzurdan [Pcwltn! | N ~] = āzārdan, āzwar [?*cwl | N ~] greedy. ~ih: greed.
PHD.txt:386:e--rób [-lwp | N jārē(b)] broom. geän [HY A < А hy’; yn! | M gy’n, N jan] soul, ghost. ~ kandan: give up the ghost; moment of death. ~-abespar [-^5sp?! | N jān-sipār] reckless, desperate; devoted. ~ig [-yk! | M -yg] spiritual; vital. | ~war [-wl | (P -br), N jánwar] animate; animal.
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD.txt:561:rdz-Saban [YWM, lwc sp’n' | N šabān(a)rēz] day and night. rózwürag [/zvcw?/k!] daily, everyday. róz-ward [/wcwlt'] changeable, fickle. rubüdan, rubāy- [/pwtn!, lp d- | M rbwdn, rb’y-, N ~] snatch, rob. rüdan, rün- [/win', lwn- | (N rūda)] pluck, pull out. rürag [/wlk'] medicinal plant, herb. rustan, rdy- [lwstn', lwd- | M rwst, rwy-, N ~] grow. ~išn: growth. ruwān [lwbn'! | M rwn, N ~] soul. ~ig [-yk! | N ~7] spiritual. ruzd [lwzd | M rwzd, N таза] greedy. ~ih : greed.
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:1189:chaff kāh.
PHD.txt:2604:lessen kāhēnīdan, kastan.
PHD.txt:3836:straw kāh, P wāš; giyáhizag, nāyizag.
PHD.txt:4914:lab «rubāy- lipī, rabih rapihwin
PHD.txt:5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
PHD.txt:5066:kāh- kāhēn- kāhēnīdan kāhīdan kāhišn kāskēnēn kāskēn
PHD_mackenzie.txt:1439:azruftan, azraw- [C)zlwp-tn l I M Czrw-] go out, be extinguished.
PHD_mackenzie.txt:2855:·harrob- [hlwp- I M hrwb~] collect, gather.
PHD_mackenzie.txt:3150:kah-rubay [khlp)d I N --TUba] amber.
PHD_mackenzie.txt:4407:r6b [lwp] robbery.
PHD_mackenzie.txt:4408:r6b- [lwp- I N ruJtan, ,....,] rub, sweep.
PHD_mackenzie.txt:4409:robah [TALE < A tCl'; lwp)h IN,....,] fox.
PHD_mackenzie.txt:5018:truftag [tlwptk ' ] stolen; intercalary (days).
PHD_mackenzie.txt:5857:zruftan, zraw- [zlwp-tn ] = azruftan.
== NYB
314:ahräm- [’hl’m-] pres., to raise, to lift up, to lead upwards; pres. pass. dd p. sg. ahrāmiyēt ['hPmydyt']: fratom gam pat humat ... apar ~ at the first step he is lead up to (the stage called) Good Thought 7326-27, but Paz. ārāmed, Skr. v. nivesayati (West: ‘he rests the first footstep on Humat’). — Ps. pret. ’hl’pty, pres. ’hl’m-, pt. 'hlwpty ‘elevated’; MPrs hr'ptn, ’hr’m-; MPrth pt. ’hr’m’d; Paz. aharām- išni, Skr. v. ākarsgana, aharämihed, Skr. v. krsyate SGV XVI, 22. 26, treat- ing of Manichean theology. Etymological attempts HP II, 5; Verbum 190; Ghilain 73; Ps. Gloss. As to -m-: -ft- cf ayinaftan, hanžaftan. Cf also Gxrdm-.
3029:patigriftan [ptglptn', MKBLWN-], pati- gruftan [ptglwptn'] pačir- [MKBLWN-, ptyl-], pt. = pret. pass. 3d p. sg. patigrift [ptglpt'; MKBLWN.t, MKBLWN-x, 2876, 299. 611; -x, 21, 18%] patigruft [ptglwpt'] 5811. 6015: to receive, to ac- cept, to take up, often with the prev. frac: 1. Bastvar (PLK”) pat dast fräc patigrift B. caught *the battle-axe (just swung by the attacking enemy) with his hand 2875-26; barak xvēš pat dast frac patirét he himself takes command of the steed (by grasping the reins) with his hand 299. — 2. en den i mäzdesnän hac Ohurmazd patigrift he received the Maz- dayasnian religion from O. 18%2?sq. 1919, ete.; hàn 4 Evak frāc patigrift u apārīk hac dastavar hist the one (doctrine) he accepted and the other he excluded from the canon 10954. — 3. to agree 215; to accept, to comply with 381; göbiön ~ to receive the (divine) command 5811, 6028. — 4. pat fradandeh ~ to adopt as one's son 275; pat zanēh ~ to espouse 161; pat nikühdareh ~ to take charge of 8213. — 5. kē hac šmāh hàn patirét marnjénitan ? who among you takes it upon himself to slay this man? 4217; oišan-ic . . . baxtan
3341:rop [lwp'] pillage, plundering 108%. — Cf NP ruftan rob- ‘to sweep’.
3799:neh u burtäreh u ~ 11214. — Av. (643) tarop- ‘to steal’. subju. trofyāt (Y.115; a hapax) < *trpydt with secondary develop- ment of -r- to -ra- (tr- is only secondary in Olr) Cf NP tarb, tarfand ‘deceit, fraud, lie’. As the BP derivatives of this root semantically agree with Av., whereas the derivatives outside this group have other, non-technical significations, the former must be regarded as borrowed from Av., and consequently tlpt is best interpreted as trift, not as tirft as Bthl has it. This is confirmed by the parallel form tlwpt = truft with -ri- > -ru- be- cause of the labial. I give here the BP forms known to me: 1. inf. tlwptn! = truftan DkM 364U (+ bwrtan, cf 11214 just quoted); 2. tlpt'l = triftär Phl. Y 291: 3. tlwptk = truftak BAA p. 2418; 4. tlptkyh = triftakéh, v. above; 5. tlp- tynytn' = trifténitan "to commit theft’ Phl Y. 115 (translation of trofyāt); 6. tlpt = trift ‘theft’ explaining Av. (638) taya-.
3881:*uzruftak [wzlwptk'] *decayed, ruined? 112%, — Seems to be uz- (written wz- instead of "wz-, v. uspurrikihà) + ruftak from *rup-, Skr lup- (lumpati, Lat rum-
```


## [2026-09-07T01:39:24.407Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ربودن\\|ربایدن\" BQT_v2_pages.txt | head -20; echo \"== page markers near\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5"
}
```


### [2026-09-07T01:39:24.504Z] TOOL RESULT

```
7250: ‫مرادربودند»‬          ‫جند‬   ‫‪.‬‬    ‫دهند‬         ‫دادی یا شوهر‬          ‫رحصت‬
7884: ‫هرچه موجود باشدهربودنی» امور ظاهری وباطنی‪ «:‬وچیزهاء پنهانی والهی همیشه غالب‌تر وقوی‌نر‬
23405:                        ‫بتازی عنب‌الثعلب خوانند ‪. ۴‬‬                      ‫یعنی‬      ‫و امر بربودن هم هت‬
23434:        ‫" بهلوی‬   ‫هز ‪29(2)۲ ۰‬‬      ‫‪۴‬‬          ‫مخفف « رباینده » اسم فاعل از « ربودن؟ ‪.‬‬        ‫‪- ۱‬‬
23519:                                                           ‫مانوی (یهلوی) ‪ndwbr‬‏ ( ربودن غ*ارت ) ‪.‬‬
24959: ‫ذاقی‪۱‬اخوانند‪ -‬وربودن ودزد‪:‬دن راهممیگویند‬
== page markers near
```


## [2026-09-07T01:39:35.530Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v2_pages.txt | head -3; echo ===; awk 'NR>=23380 && NR<=23540' BQT_v2_pages.txt | grep -n \"page\" ; echo \"=== context 23400-23530\"; sed -n '23395,23440p' BQT_v2_pages.txt"
}
```


### [2026-09-07T01:39:36.736Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-07T01:39:39.132Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v2_pages.txt; echo \"-----\"; grep -n \"\\[\" BQT_v2_pages.txt | head -5"
}
```


### [2026-09-07T01:39:39.204Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
-----
195: ‫خوارزمی ‪.‬فر(هنگ عربی بفارسی) با اضافات باهتمام وزماو‪. [ . 6 . ¥ 20۵‬لبسيك‬
234:‎62‫ و[ و‬۰۳       .601-39
343: ‫‪ * ۸۷‬زباکی‪« [2‬کربرسن‪ »۱۸‬اورامان‪8082‬ز « ك ‪ .‬اورامان‪ ۰» ۳۲۱‬کردی از ‪ ,‬اففالی‪۰ 81‬‬
344:                            ‫بلوچی ‪ 2۰‬کیلکی ‪ [882‬؛ بجای ‪ ....‬بمعنی درحق ‪ ...‬درباره ‪...‬‬
383:         ‫هز‪ .- )03]2[,02 .‬پپلوی)‪:2223۷‬‬           ‫‪۴‬‬          ‫‪ - ۴‬رتکی‌چاناق « جفنابی ‪.» ۳۷۲‬‬
```


## [2026-09-07T01:39:43.279Z] TOOL CALL #26: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:938 2>&1 | head -60"
}
```


### [2026-09-07T01:39:44.663Z] TOOL RESULT

```
no scan of BQT covers printed page 938 (see 'scans' in refs_online.json)
```


## [2026-09-07T01:39:46.782Z] TOOL CALL #27: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));b=d['BQT'];print(json.dumps(b,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T01:39:48.000Z] TOOL RESULT

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


## [2026-09-07T01:39:52.813Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==399' BQT_v2_pages.txt"
}
```


### [2026-09-07T01:39:54.063Z] TOOL RESULT

```
  ‫—‪—Ara‬‬                                                                                                         ‫ربوسه‬

 ‫برون؟ ‪ -‬بفتح اول بر وزن زبون ‪.‬‬                              ‫ومجاممت بهم رسد خصوصاً ؛ و باینه‌عنی با زای‬
‫پیش مزد وبیعانه راکوبند » وآن زری باشد که‬                                   ‫‪¥.‬‬         ‫تقطمرار وجیم هم ‪E‬‏‬

 ‫بش ازکار کردن نمز دوردهند؛ ویعضی گونند رری‬
‫باشد که درقیمت متاعی‌داده‌باشند مشروط بابنکه‬                 ‫‏‪e‬‬                                     ‫‏‪ EEE‬باشد‬

‫بد نگاهدار ندوألا یس دهند و زر‬
                             ‫اکر خوش آ‬                       ‫امتال‬   ‫و روباك و‬    ‫د هفنعه‬      ‫وچادر‬    ‫کویندعموما‬


‫خود را بگیرند و درخربزه وهندوانه بشرط کارد‬
   ‫ون‬‫ر)بکه‬‫یضیگر گفته اند (‪۲‬‬    ‫دبع‬
                                 ‫کویند و‬
                                                             ‫باشین ننةقطه دار(‪ ۱)۰‬بر‬            ‫‪8‬‬       ‫ور‬
 ‫زری است که ژ باده از | نجه نمز دور قرار داده‌اند‬
                                                             ‫وچادروهقلعه‬         ‫است که میروش‬          ‫ورال وهعنی‌ربوسه‬
                                                ‫‪.‬‬   ‫ضف‬
                                                     ‫بت‬
                                                             ‫ورویاك زنان باشد وآن دراصل رویوشه بود که‬
 ‫ر ثا = با نای مثلئه(‪ )۳‬بروزن مسیحاء‬                         ‫باکثسرتتعمال ربوشه شده ؛ و بقتح اول هم‬
 ‫بلفت سربانی نوعی از ماهی کوچك باشد ‪ ۴‬که‬                                                                     ‫گفته‌اند ‪.‬‬

‫ازجااب هرموز آورند وآ نرادر گرسیر (‪ )4‬ماهی‬                   ‫ر بوله = بنتح اول وآخر که لام باشد‬
 ‫ادنه گوبند وماهیانه اآنز‌پزند وهمجذان خشك‬                  ‫وثانی بواو رسیده" بلفت اندلس رستذیی باشد که‬
                      ‫لزخورند ‪ .‬فوت باه دهد ‪.‬‬                               ‫خ<ورند ‪۱‬‬    ‫آ برا کنگرکوبند وبا ماست‬




                                                     ‫بیان سوم‬

                    ‫فارسی مشتمل بدرو لغت‬                         ‫ای‬
                                                                  ‫بقطه‬
                                                                     ‫این‬
                                                                       ‫بی م‬
                                                                          ‫در را‬
              ‫قدری ازآن خورند مت گردند ‪۲‬‬
                                  ‫‪۹‬‬
                                                             ‫رل ‪ = °‬بفتح اول وئانی سوکون دال‬
                                                                                           ‫و‬
‫= بروزن کبود بمعنی ریداست‬                 ‫ر ود‬              ‫أسحد > گیاحی باشد که چون حبوانات چر نده ای‬


                 ‫(‪ )۳‬باٿا ‪.‬‬                ‫)‪ (۲‬چك‪ -:‬کفته‌اند ‪1‬‬                    ‫دار‬   ‫چك‪-:‬نقطه‬        ‫)‪۱‬‬


                                                                        ‫‪۳‬‬    ‫کرمیرات‬      ‫در‬    ‫)‪ (4‬چش‪:‬‬


      ‫نت نا‪٤‬‏‬    ‫ار یون = اربان‬       ‫‪e‬‬    ‫‪۳‬‏‬         ‫‪.‬‬   ‫رك ‪ :‬ریوسه‬        ‫‪۴‬‬           ‫‪ - ۱‬رك‪ :‬ریوشه‬

                                                                                                  ‫(‪:‬‬     ‫رمون ( «‪.‬م‪.‬‬

            ‫بن و جان و مپر داده ربون ‪.‬‬                               ‫ای خریدار من ‪:‬را بدو چیز‬
   ‫“‪LA‬‏‬   ‫فرن‬   ‫رود کی سمرقندی دلت‬

  ‫‏‪۹۹٤۰‬ص‪۱‬‬
       ‫‏‪) condiment de poisson = ۴‬رف( كل« ‪ ۲‬ص ‏‪٩۱۱۷‬رو‪:‬هک یزدج‬
  ‫بهو ی‪۸‬ا‪ ۲‬ها¡ا» همان « آپرو نتن “است رك‪ .‬بو نکر ص‪٣‬‏ (د کتر‬                                         ‫'‬
                                                                                                    ‫‪8‬م‪NV۸‬‏‬
                                                                                                         ‫‪ -۵‬هز‬
 ‫باستان‬   ‫رودن ‪ -‬سم اول‌ودوم وفتح چهارم‪ .‬از‪ :‬ربو ‪٣‬‏ دن ( پوند مصدری) ‪ ۰‬هندی‬
                                                                          ‫فره دشی ( * ب‬
  ‫»رت کردن‪ ,‬بغما بردن)‪ ۰‬پهلوی‌‪8۵۲‬‬
                                ‫ره ‪«۲۵1‬قدستر ‪( 0۵۲۰ -‬شکتن »ستن » یچیدن ‪۰‬ا‬
 ‫(غلرت » یغما )‪ ۰‬بلوچی‪( 820۵۲‬جاروب کردن) «اسشق ‪۸۰٩‬‏ وکره‪ :‬هوبشمان ابضاً ؛ در اوراق‬
                                                           ‫مانوی (یهلوی) ‪ndwbr‬‏ ( ربودن غ*ارت ) ‪.‬‬
           ‫‪Henning, A list of Middle‬‬                         ‫‪Persian..., BSOS, IX, 1, p. 87.‬‬
```


## [2026-09-07T01:40:09.246Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lagin\\|laginn\\|laqna\\|lekane\\|Aekavr\\|ligin\\|lignu\\|ligittu\\|laqan\" AKD.txt | head -20; echo \"== page 21 offset?\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['AKD'],ensure_ascii=False,indent=1))\""
}
```


## [2026-09-07T01:40:10.104Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"pdf page 5[0-9]\" FFD_pages.txt | head; echo ===; awk '/\\[pdf page 55\\]/,/\\[pdf page 57\\]/' FFD_pages.txt | head -80"
}
```


### [2026-09-07T01:40:10.556Z] TOOL RESULT

```
283:akk.    lignu,    liginnn  u.  ligittu   ein    Getreidemaß  :  >>  aram.    hg^nri
586:hgettä  (arab.  .lugnat)  Saatfeld  s.  oben  S.  21  f.  unter  akk.  lignu,  ligittu.
== page 21 offset?
{
 "title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)",
 "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/akkadischefremdw00zimmuoft",
 "identifier": "akkadischefremdw00zimmuoft",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt",
 "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.",
 "notes": "39 citations; check that the 1st-ed. page is within a page or two of Nourai's."
}
```


### [2026-09-07T01:40:11.779Z] TOOL RESULT

```
Exit code 1
1249:[pdf page 50]
1274:[pdf page 51]
1298:[pdf page 52]
1320:[pdf page 53]
1344:[pdf page 54]
1375:[pdf page 55]
1398:[pdf page 56]
1422:[pdf page 57]
1446:[pdf page 58]
1470:[pdf page 59]
(eval):1: == not found
```


## [2026-09-07T01:40:13.664Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '275,300p' AKD.txt"
}
```


### [2026-09-07T01:40:13.710Z] TOOL RESULT

```
akk.  parsu  Halbmine  (von  par(7isu  teilen)  :  >  neuhebr.  parüs,  alt- aram. prs,  auch  p^-s  (auch  parsin  Dan.  5,25.28.  urspr.  vorliegend).
akk.  haUüru'-,  ein  Unterteil  des  Sekel  :  >>  ägypt-aram.  [ilr.
akk.  girü,  ein  Unterteil  (V24)  des  Sekel  :  >-  wohl  liebr.  gerä  i/,o Sekel.
Ob  etwa  auch  das  Wort  für  Talent,  hebr.  hiMär,  phön.  hkr,  aram. kakharä  (ägypt. -aram.  knJcr)  (]>  armen.  ¥ank'ar),  südarab.  Jcrkr,  griech. xiyxccQ-eg  (Josephus),  auf  ein  alck.  *kaJckaru  zurückgeht,  ist  noch  unsicher. -
[Ob  griech.  Sagstxög  (Bez.  für  eine  persische  Goldmünze),  hebr. 'ädarkön,  später  darkön,  syr.  dsrikönci,  auf  eine  babyl.  Vorlage,  etwa  ein akk.  dariku^  zurückgeht,  ist  sehr  fraglich.  Das  Wort  ist  vielmehr  wohl pers.  Ursprungs,  hat  aber  andererseits  auch  nichts  mit  dem  Namen  Darius zu  tun.     Ebensowenig  darf  es  mit  S^axfn'i  zusammengebracht  werden.]
akk.  zfisu  wohl  (Silber)stück  od.  ä.  :  >  aram.  mzä  eine  kleine Silbermünze.     Dazu  ^oiiaai  (bei  Hesych),  durch  S^axf^ai  glossiert.
akk.  kurru  ein  Getreidemaß  (wohl  <1  sum.  gur)  :  >  hebr.  kör, aram.  km-ä  (>>  arab.  kurr),  griech.  xögos  (LXX,  Josephus).
akk.  se'u,  se'atu  Getreide,  ein  Getreidemaß  «  sum.  se)  :  ^  hebr. S9'ä,  PI.  so'mi,  aram.  sa'tä,  sä{^)ta,  PI.  S3'm  u.  sam  (altaram.  s'A,  s'<), griech.  aäxov  (NT,  Josephus).
akk.    lignu,    liginnn  u.  ligittu   ein    Getreidemaß  :  >>  aram.    hg^nri
1)  Urspr.  gewiß  identisch  mit  hällüru  Platterbse  =  hebr.  härül,  aram.  hurlri,  arab. hullar.     S.  dazu  unteu  S.  56.
2)  Die  ausschließliche  Lesung  des  fast  stets  ideogi-aphisch  geschriebenen  "Wortes für  Talent  als  hiltri  ei-soheint  mir  nicht  so  sicher  wie  allgemein  angenommen  wii'd.  "Wohl in  der  Bed.  „Scheibe"  (vgl.  hebr.  hiJckar)  begegnet  gaggaru  einmal  in  den  Amai-nabriefen.
3)  Das  allerdings  nur  als  Name  eines  Gefäßes  nachweisbar  ist.
  22      
irdenes  Faß,  Krug,  wie  auch  aram.  lignd,  hgettfi  i.  d.  Bed.  Stück  Saatfeld O  arab.  lugnat).  —  Ob  hierzu  auch  hebr.  log  ein  kleines  Maß  für  Flüssig- keiten, svr.  laggatä  Schüssel  und  Maßbezeichnung,  gehört,  ist  weniger sicher.  S.  auch  unten  S.  40  zu  akk.  kinibü.
Ob  etwa  auch  hebr.  hömer  ein  größeres  Hohlmaß  für  Trockenes, auf  Anlehnung   au   akk.   imn-n  dass.   (eig.  Eselslast?)  beruht,   ist  unsicher.
Auch  ein  akk.  qabbn  als  etwaige  Vorlage  des  hebr.  qah,  aram.  qabhfi Hohlmaß  für  Trockenes  O  arab.  qabb),  griech.  xäßog  (LXX,  Hesyclij, ist  nicht  gesichert.
[Umgekehrt  ist  das  pers.  Getreidemaß,  die  äpräßri,  wie  ins  Aram. als  'ar(bbä,  \uidbä,  so  auch  bereits  ins  spätere  Aklc.  als  arf(d)ahi  aufge- nommen worden.]
Das  "Wort  für  Elle,  akk.  ammatu,  hebr.  ^amniä,  aram.  'ammatd.  süd- arab.  'mt,  äth.  'enimaf,  wird  ja  wolil  als  ein  Urwort  in  den  einzelnen semit.  Sprachen  (im  Arab.  fehlt  es)  anzusprechen  sein.  Auffällig  ist  aller- dings, daß  es,  wenigstens  im  Hebr.  u.  Aram.,  fast  nur  als  Maßbezeichnung, nicht  auch  in  der  urspr.  Bed.  des  akk.  ammatu  als  Körperteil  üblich  ist'
akk.  qann  Rohr,  Rute  (Längenmaß  von  6  bezw.  7  Ellen)  :  davon jedenfalls  abhängig  hebr.  qäne  Rohr,  auch  als  Längenmaß  von  6  Ellen (bei  Ezech.).  Ebenso  wird  auch  das  auf  qanü  zurückgehende  xavwv  im späteren  Griech.  für  Meßrute  gebraucht.  Dagegen  liängt  äxaiva  Längen- maß von  6  Fuß,  kaum  damit  zusammen.     S.  weiter  zu  qanfi  unten  S.  56.
Zu   akk.  oAlu  Strick,  als  Längen-  bezw.  Flächenmaß   s.  unten  S.  35.
Endlich  ist  viell.  auch  griech.  arädiov  (von  2TASi)  zur  Bez.  eines Längenmaßes  entstanden  als  Übersetzung  von  babyl.  Z7»S,  wohl  mit  der akk.   Lesung    Iniäu   (von    eniedu  stellen),   als    entsprechendem   Längenmaß.
akk.  iiiasähu  messen,  w!e.?J/*iMMaß  :  ]>  wahrsch.  aram.  nidsah  messen, mishä,    ndSlwta,    mdsuhtn   Messen,  Maß  (>  arab.   misähat);   auch   viell.  in
1)  So  ganz  selbstverständlich  erscheint  es  keineswegs,  den  der  „Elle"  entsprechen- den Teil  des  Unterarms  als  natürliche  Maßeinheit  zu  verwenden.  Es  könnte  daher,  zumal auch  der  tatsächUche  Betrag  der  Maße  hier  einen  historischen  Zusammenhang  aufzuweisen scheint,  recht  wohl  dieser  Gebranch  des  Wortes  Elle  (Köi-perteil)  als  Maßeinheit  von Babylonien  ausgegangen  und  von  da  zu  den  westsemit.  Völkern,  den  Griechen  (tt/;/«?) und  Römern  (cubitus,  ulna)  und  weiter  in  alle  neueren  europäischen  Sprachen  gewan- dert sein.
      23      
hebr.  mishä,  moshä  (Priester)anteil,  vorliegend.  S.  auch  noch  unten  S.  26 zu  maSihu  Feldmesser.
aklv.  madndu  messen  :  hier  könnte  die  spez.  techn.  Bed.  von  hebr. (auch  phön.)  madad  messen,  »t'uldd  Maß  auf  Entlehnung  bezw.  Anlehnung au  den  liabyl.  Sprachgebrauch  beruhen,  während  die  allgemeinere  Bed. sti-ecken,  sich  ausdehnen,  die  z.  T.  im  Hebr.,  besonders  aber  in  arab.  madda vorliegt,  auf  Urverwandtschaft  beruhen  wird.
```


## [2026-09-07T01:40:14.324Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && sed -n '1344,1400p' FFD_pages.txt"
}
```


### [2026-09-07T01:40:14.373Z] TOOL RESULT

```
[pdf page 54]
ماده‌های ماضی و مضارع فارسی دری ‏ سا ی ۴۹
پهلوی اشکانی و ایرانی باستان» «دویدن» معنی می‌دهد.

از 2۵۳47422 فارسی میانه در فارسی دری «چندش» آمده است.

0 فارسی میانه مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده
است.< 2224 ایرانی باستان ۵۵4-۵ت*. برای 2 > آرای. ريشةٌ ۸4 به معنی
«هیجان‌داشتن» و 2۵۵414۵8 به معنی «لرزیدنْ» است.

چیدن

چید < فارسی میانه 67 < ایرانی باستان ۵۲-1۵*. برای 18 > آراست. ۲ صورت

ضعیف ريشةٌ ۵7و آن ريشه به معنی «گُزیدن» است. «گُزیدن) هم از اغ آمده است ->
گزیدن.

چین < فارسی میانه 278 < ایرانی باستان ۴۵۲-۵ 3 نشانه‌ای که برای ساختن
مادهٌ مضارع از ريشه به کار می‌رفته است.

خاستن

خاست < فارسی میانه 3391 < ایرانی باستان ۴۸315-12۵ برای 12 -> آراست. 232
صورت اصلی 5ل88 است» 2 پیش از 1به 5 بدل شده است. 1312 صورت بالاندةٌ 822 و آن
به معنی «خاستن» است.

خیز + فارسی میانه 82 < ایرانی باستان 8۵12-2*. برای 2 > آرای.

خاییدن
«خایید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خای چ ایرانی باستان 304-2 برای 3 > آرای. ريشةٌ 40 به معنی «جویدنُ» است.
[pdf page 55]
وا فعلهای فارسی دری
خرامیدن
«خرامید» ماد ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
: «خرام» < فارسی میانه 337370 < ایرانی باستان 3+737-8*. برای ۵ > آرای. 3
پیشوند فعلی است. ۳370 صورت بالاندةٌ ريشهٌ 77870 است و 77870(«گامبرداشتن» معنی
می‌دهد.
خریدن
خرید < فارسی میانه 7770 < ایرانی باستان 3۳7-1۵*. برای 14 -> آراست. 77 صورت
ضعیف 727 است و آن به معنی «خریدن» است.
خر + فارسی‌میانةٌ مانوی 37. 77 در فارسی‌میانهٌ مانوی و «خر» در فارسی دری‌به این
سبب به وجود آمده‌اند که تصور شده «خرید» مادهٌ ماضی جعلی است و با حذف ۲4مادة
مضارع به وجود می آید. مادةٌ مضارع 3374 در فارسی میانه 778 است» از ایرانی باستان
8 83 نشاته‌ای بوده که برای ساختن ماده مضارع از ريشه به کار می‌رفته است ->
بریدن,
خزیدن
«خزید» ماده ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خز < پهلوی اشکانی 382. فارسی میانهٌ مانوی 782 < ایرانی باستان ۶۵2-۵
3-2 برای 2 > آرای. 2 صورت افزوده و 7 صورت ضعیف ريشه هستند. 1817 به
معنی «خزیدن» است.
خست + فارسی‌میانه 3881 < ایرانی باستان 3۵9-1۵*. برای 18-> آراست. 740 صورت
اصلی 8 است. 4 پیش از 1به 8 بدل شده است. ريشةٌ 24 به معنی «پاره کردن» است.
خفت < فارسی میانه 911 < ایرانی باستان ۳۵۶-۵". برای 1۵ -> آراست. 1:۸0
[pdf page 56]
ماده‌های ماضی و مضارع فارسی دری --___شش ۵۱
صورت اصلی 3 است.» 0 پیش از ۲ به ۶ بدل شده است.
```


## [2026-09-07T01:40:26.759Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"ربودن\\|ربای\" FFD_pages.txt | head -20"
}
```


### [2026-09-07T01:40:26.808Z] TOOL RESULT

```
1505:ربودن
1507:ربای + فارسی میانه 1003 +« ایرانی باستان ۵رقم۳*, 2رقم" از ۳803: اسم
1508:به‌معنی «ربودن» و 8نشانه‌ای که برای ساختن مادةٌ جعلی از اسم به کار می‌رفته» ساخته
1512:3 از ریشةٌ 780 به معنی «ربودن» و پسوند 3 ساخته شده است.
2515:۴۴4 70 (ريشه - ربودن) ۵۵
```


## [2026-09-07T01:40:30.231Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && sed -n '1495,1520p' FFD_pages.txt; echo \"=== which pdf page\"; awk 'NR<=1505 && /\\[pdf page/ {p=$0} END{}' FFD_pages.txt; awk 'NR<=1505 && /\\[pdf page/ {p=$0} NR==1505{print p}' FFD_pages.txt; echo \"=== line 2515 ctx\"; sed -n '2505,2525p' FFD_pages.txt; awk 'NR<=2515 && /\\[pdf page/ {p=$0} NR==2515{print p}' FFD_pages.txt"
}
```


### [2026-09-07T01:40:31.443Z] TOOL RESULT

```
بین < فارسی میانه ۷۷68 + ایرانی باستان ۹/۵۱-3* 23 نشانه‌ای بوده که برای ساختن
مادهٌ مضارع از ريشه به کار می‌رفته است. ريشةٌ ۷۵ به معنی «دیدن» است.
«دیدن» و «بین» چون «آمدن) و «آی» دو ریشه‌ای است.
رامیدن
۰ آرامیدن
راندن
راندن مخفف «روانیدن» است و آن فعل واداری از «رفتن» است. در فارسی دری
فعل واداری از مادةٌ مضارع + «ان» و «(عن» ساخته می‌شود. «۵۶) در متون کهن آمده
مادهٌ ماضی فعل واداری هميشه جعلی است و به جای «انید» ممکن است («اند» به
کار رود.
ربودن
ربود + فارسی میانه 1010.
ربای + فارسی میانه 1003 +« ایرانی باستان ۵رقم۳*, 2رقم" از ۳803: اسم
به‌معنی «ربودن» و 8نشانه‌ای که برای ساختن مادةٌ جعلی از اسم به کار می‌رفته» ساخته
شده است.
مادهٌ ماضی باید «رّفت» < فارسی میانه ۳۵۶۲ < آیرانی باستان ۵۵ می آمد. به قیاس
با 573 و 5736 «ربود» آمده است.
3 از ریشةٌ 780 به معنی «ربودن» و پسوند 3 ساخته شده است.
رّستن
رّست + فارسی میانه 7291 < فارسی باستان ۴۶۵۶-1۵ برای 1۵ -> آراست. 724
صورت اصلی 78 است» ‎٩‏ پیش از 1به 9بدل شده است.
[pdf page 61]
ان 111 0 اه ی ی ار ان نار اه
ره ج فارسی میانه ۲۵10 ج فارسی باستان ۹۳۵-۵ برای 2 -> آرای. اس <ایرانی
باستان 182: گریختن.
رُستن
=== which pdf page
[pdf page 60]
=== line 2515 ctx
َ باستان) ۲۹
54 ۴۰۱۰ مارد
8 ۰ 8 : ۶ + رشتن
8أق: (ريشة ضعیف + قنةم) ۷۸ دس
1 31۵" : ۷۶ + لشتن
8 ؛ (ريشه < پرسیدن) ۴۲ َ 8
3 2 : (ريشةٌ ضعیف ۰ 2۷اه) ۵۶
4--053): ۴۲ 2 : (ريشه ضعیف + (۵12۳) ۷۶
3 (ريشه + 021) ۲۹ 40 (ريشةٌ ضعیف + ۲20) ۵۶
8 (ريشةٌ ضعیف + 02) ۴۴ 72: ۵۵
۴۴4 70 (ريشه - ربودن) ۵۵
8 (ريشه > 02) ۴۴ 3 ۵۵
2 : ۴۴ 4 ۵۵
2 (ريشه < حرکت کردن) ۵۶ 4 ۵۶
0 (ريشه < حرکت‌کردن) ۵۶ ۵۷ 8 (ريشه < آلوده بودن) ۰۲۶ ۲۷
42 ۵۷ 8 (ريشهٌ ضعیف + 8278) ۲۸ ۶۰ ۶۷
۵ ۵۶ 0 (ريشه < بریدن) ۷۴
4 ۵۷ 2 (ريشه - توانابودن) ۵۸ ۰
[pdf page 96]
فهرست واژه‌ها سا 00
4 (ريشه < به نظرآمدن) ۳۳ : (ريشه < فشاردن) ۵۹
[pdf page 95]
```


## [2026-09-07T01:40:47.293Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN loot\"; grep -n \"^loot\\|loot, n\\| loot \" KLN_1966.txt | head -10; echo \"== KLN 1971 loot\"; grep -n \"lūṭ\\|lu.t.*plunder\\|Hindi lūṭ\" KLN_1971.txt | head -10"
}
```


### [2026-09-07T01:40:47.381Z] TOOL RESULT

```
== KLN loot
22125:loot,  n.,  plunder,  booty.  —  Hind.  Hit,  fr.  OI.  16- tam,  lotram,  ‘booty’,  which  is  rel.  to  luntati, ‘robs,  plunders’,  and  prob.  cogn.  with  L.  lu¬ crum,  ‘gain,  profit,  advantage’.  See  lucre.
== KLN 1971 loot
140920:luntati , ‘robs, plunders’, Gk. Xeia, Dor. Xata,
```


## [2026-09-07T01:40:48.263Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD leup\"; grep -n \"leup\\|leubh\\|leub-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T01:40:48.320Z] TOOL RESULT

```
== AHD leup
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
697:leug-2. To break. Suffixed form *Jeug-é- in Latin ligére, to mourn (? < “to break down mentally”): LUGUBRIOUS. [Pok. leug- 686.] leugh-. To tell a lie. 1. Germanic *leugan in: a. Old English /Zogan, to lie: WARLOCK; b. Old English beléog- an, to tell lies about (be-, about; see ambhi): BELIE. 2. Germanic */ugiz in Old English lyge, a lie, falsehood: LIE’. [Pok. leugh- 686.] leuk-. Light, brightness. I. Basic form */euk-. 1. Suffixed form *leuk-to- in Germanic */euhtam in Old English léoht, liht, light: LicHT). 2. Latin lix, light: Lucrna, LUCULENT, LUX; LUCIFER, LUCIFERIN. 3. Suffixed form *leuk-smen- in Latin limen, light, opening: LIMN, LU- MEN, LUMINARY, LUMINOUS; ILLUMINATE, PHILLUMEN- 1st. 4. Suffixed form *leuk-snd- in Latin lina, moon: LUNA, LUNAR, LUNATE, LUNATIC, LUNE, LUNULA; DEMI- LUNE, SUBLUNARY. 5. Suffixed form */euk-stro- in: a. Latin listrum, purification: LUSTER, (LUSTRUM); b. Latin lastrdre, to purify, illuminate: ILLUSTRATE. 6. Suffixed form *leuko-dhro- in Latin licubrdre, to work by lamplight: LUCUBRATE. II. O-grade form *louk-. 1. Suffixed form *louk-o- in Germanic *lauhaz in Old English /éah, meadow (< “place where light shines”): LEA. 2. Suffixed (iterative) form *lowk-eyo- in Latin liicére, to shine (> licidus, shining): LUCENT, LUCID; ELUCIDATE, NOCTILUCA, PELLUCID, RELUCENT, TRANS- LUCENT. III. Zero-grade form *luk-. 1. Suffixed form *luk-sno- in Greek lukhnos, lamp: LINK?, LYCHNIS. 2. At- tributed by some to this root (but more likely of obscure origin) is Greek lunx, lynx (as if from its shining eyes): LYNX, OUNCE? [Pok. leuk- 687.] leup-. To peel off, break off. 1. Germanic *laubaz in Old English Jéaf, leaf: LEAF. 2. Germanic *laubja, “roof made from bark,” shelter, in: a. Old French loge, lodge: LODGE, (LOGE); b. Medieval Latin lobium, lobia, laubia, monas- tic cloister: LOBBY. 3. Attributed by some to this root is Germanic */uftuz, sky (traditionally explained as < “roof of the world,” vault of heaven), but probably a separate Germanic root, in: a. Old Norse opt, air, attic, sky: LOFT; ALOFT; b. Germanic */uftjan, to hold up in the air, in Old Norse /ypta, to lift: Lirt. [Pok. leup- 690.]
955:5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
1230:ALOFT an!, leup- ALONE oi-no- ALONG §ant- ALOPECIA wip-é- ALPENHORN ker-1 ALPENSTOCK (s)teu- ALPHOSIS albho- ALSO al-5
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1283:BELFRY bhergh-? BELIE leugh- BELIEF feubh- BELIEVE leubh- BELL! bhel-4 BELL? bhel-4 BELLADONNA deu-2 BELLE deu-? BELLICOSE duellum
1371:CLAY gel-1 CLAYMORE kel-1, mé-3 CLEAN gel-2 CLEANSE gel-2 CLEAR kele-2 CLEAT gel-1 CLEAVE! gleubh- CLEAVE? gel-! CLEAVERS gel-1 CLEF kleu-3 CLEISTOGAMOUS_ kleu-3 CLEISTOTHECIUM dhé-1, kleu-3 CLEMATIS kel-1 CLENCH gel-1 CLEPSYDRA klep-, wed-! CLERK kel-1 CLEVER gleubh- CLEVIS gleubh- CLEW! gel-1 CLIENT klei- CLIMATE klel- CLIMAX Klei- CLIMB gel-1 CLINAL klei- CLINANDRIUM klei- CLINCH gel-1 CLINE klel-
1376:CLOTH peie- cLoup  gel-1 cLouT gel-1 CLOVE! kleu-3 CLOVE? gleubh- cLoy kleu-3 CLOZE kleu-3 CLUB) gel-1
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1546:FURBISH prep- FURL leig-1 FURLOUGH leubh- FURNACE gWher- FURNISH per! FURROW perk-2 FURTHER per! FURTIVE bher-1 FURUNCLE bher-1 FURUNCULOSIS_ bher-1 FURZE piiro-
1563:GLOWER ghel-2 GLUCAGON ag- GLUCOSE dlk-u- GLUE gel-1 GLUME gleubh- GLUT gWel-3 GLUTEN gel-! GLUTEUS gel-1 GLUTINOUS  gel-1 GLUTTON gWel-3 GLYCERIN dik-u- GLYPH gleubh- GLYPTIC gleubh- GNAT ghen- GNATHIC genu-2 -GNATHOUS genu-2 GNAW ghen- GNOCCHI gen- GNOME? gno- GNOMON gno- GNOSIS gnd-
1607:HIEROGLYPHIC  eis-', gleubh-
1719:KITTLE tit- KLEPTOMANIA klep- KLIPSPRINGER spergh- KLOOF gleubh- KLUTZ gel-! KNACKER ken-5 KNACKWURST gen- KNAP! §gen- KNAP2 gen- KNAPSACK gen- KNAR gen- KNEAD gen- KNEE genu-1 KNEEL genu-! KNELL gen- KNIFE gen-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1741:LETHAL ol- LETHARGY |adh- LETHE ladh- LETTER deph- LETTUCE melg- LEVEL [ithra LEVER leg’h- LEVIGATE ag-, leg’h- LEVIRATE daiwer- LEVITY leg¥h- LEVo- laiwo- LEVOROTATION laiwo- LEVOROTATORY laiwo- LEX leg-1 LEXICON leg-1 LIABLE leig-1 LIBATION Iéi- LIBERAL leudh-2 LIBERATE leudh-2 LIBERTINE leudh-2 LIBERTY leudh-2 LIBIDO leubh- LIBRA fithra
1746:LIEF leubh- LIEGE 16-2
1748:LIFT leup- LIGASE leig-1 LIGATE leig-1 LIGHT! = leuk- LIGHT2 legwh-
1757:LITHE lento- LITHOTRITY dhreu- LITIGATE ag- LITMUS meu-, wel-1 LITOTES lei- LITTER legh- LITTLE leud- LITTORAL [éi- LITURGY werg- LIVE! leip- LIVELIHOOD leit-2 LIVELONG leubh- LIVELY leip- LIVER! leip- LIVERWURST wers-! LIVERY leudh-? LIVID — sfi-
1760:LOATH leit-1 LOATHE leit-1 LOBBY leup- LOBE leb-1 LOBO wikwo- LOBSTER lek- LocH laku- LOCHIA legh- LOCK! leug-1 Lock? leug-1 LOCKET leug-1 Locust lek- LOCUTION  tolkw- LODE leit-2 LODGE leup- LOEss leu-1 LOFT leup- LOGARITHM ar-, leg-1 LOGE leup- Locic leg-1 LOGISTIC leg-1 Loco- leg-1 Locos leg-1
```


## [2026-09-07T01:41:13.805Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"loot,  n.,  plunder\")>0) print \"leaf\",n-1}' KLN_1966.txt; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['KLN'].get('page_offset'))\""
}
```


### [2026-09-07T01:41:15.145Z] TOOL RESULT

```
leaf 487
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-07T01:41:16.177Z] TOOL CALL #38: Bash

```json
{
 "command": "pdftoppm -f 313 -l 313 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg313 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T01:41:17.781Z] TOOL RESULT

```
total 184
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 21:41 .
drwx------ 3 sfmqrb sfmqrb  4096 Sep  6 21:35 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   175 Sep  6 21:37 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     0 Sep  6 21:39 iec_pages.json
-rw-rw-r-- 1 sfmqrb sfmqrb 56809 Sep  6 21:41 pg313.png
-rw-rw-r-- 1 sfmqrb sfmqrb 64584 Sep  6 21:40 pg314.png
-rw-rw-r-- 1 sfmqrb sfmqrb 49502 Sep  6 21:37 pg315.png
```


## [2026-09-07T01:41:29.070Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==488' KLN_1966.txt | head -c 1200; echo; echo \"###### leaf 465\"; awk 'BEGIN{RS=\"\\f\"} NR==466' KLN_1966.txt | head -c 600"
}
```


### [2026-09-07T01:41:30.246Z] TOOL RESULT

```
ongitudinis,  ’length’.  See  prec. word.
Derivatives :  longitudinal,  n.,  longitudinal-ly,  adv. longshoreman,  n.  —  Aphetic  for  along-shore-man. long-suffering,  n.  —  First  used  by  Tyndale. Lonicera,  n.,  a  genus  of  plants,  the  honeysuckle (bot.)  —  ModL. ;  so  called  after  the  German  bo¬ tanist  Adam  Lonitzer  (Latinized  into  Lonicerus ) (1526-86).
loo,  n.,  a  card  game.  —  Short  for  earlier  lanterloo, fr.  F.  lanturelu,  orig.  the  refrain  of  a  song. Derivative:  loo,  tr.  v.
looby,  n.,  a  clumsy  fellow.  —  ME.  toby,  possibly derived  fr.  lob  (q.v.),  or  from  the  French  PN.
905
Lubin,  which  was  an  abusive  name  for  the  monk in  the  Middle  Ages.  The  former  sense  of  looby 1  was  ‘loafer’, oof,  n.  — -A  variant  of  luff, loofah,  n.  —  Fr.  Arab.  l6fah.  See  luffa. look,  intr.  v.  —  ME.  loken,  fr.  OE.  locian,  rel.  to OS.  lokon,  MDu.  loeken,  ‘to  look’,  OHG.  lu- ogen,  MHG.  luogen,  G.  lugen,  ‘to  look  out’, and  perh.  cogn.  with  Toch.  A  Idk-,  ‘to  see’, and  with  OCorn.  lagat,  Bret,  lagad,  ‘eye’.  Cp.  lo. Derivatives:  look,  n.,  look-er,
###### leaf 465
adj.,  and  verbal  suff. -ate.
Derivatives:  lapidat-ion,  n.,  lapidat-or,  n. lapidification,  n.,  the  state  of  being  converted  into stone.  —  See  next  word  and  -ation. lapidify,  tr.  v.,  to  convert  into  stone;  intr.  v.,  to  be converted  into  stone.  —  F.  lapidifier,  fr.  ML. lapidificare,  ‘to  convert  into  stone’,  which  is compounded  of  L.  lapis,  gen.  lapidis,  ‘stone’, and  -ficare,  fr.  -fleer  e,  unstressed  form  of  facer  e, ‘to  make,  do’.  See  lapidary,  adj.,  and  -fy. lapilli.  n.  pi.,  small  stones;  specif,  small  stones
```


## [2026-09-07T01:41:38.622Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T01:41:38.628Z] TOOL RESULT

```


```


## [2026-09-07T01:41:43.447Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A8%D9%88%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology section for ربودن (robudan): Middle Persian form, Proto-Iranian and PIE reconstruction, cognates cited, and any cited authorities."
}
```


## [2026-09-07T01:41:44.063Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/loot",
 "prompt": "Give the full etymology of English \"loot\": Hindi/Sanskrit forms, PIE root, and any cited sources."
}
```


### [2026-09-07T01:41:47.971Z] TOOL RESULT

```
Based on the provided Wiktionary page, **there is no etymology section for ربودن (robudan)**. 

The page contains only:
- Pronunciation information for various Persian dialects
- Verb definitions (to seize, snap; to rob, steal; to abduct; to ravish)
- Extensive conjugation tables for literary Iranian Persian, colloquial Tehrani, literary Dari Persian, and colloquial Kabuli
- Derived terms (آهنربا and دلربا)
- References to historical dictionaries by Steingass (1892) and Hayyim (1934)

The entry lacks any discussion of Middle Persian forms, Proto-Iranian reconstructions, PIE etymology, or cognates in other languages.
```


### [2026-09-07T01:41:51.903Z] TOOL RESULT

```
# Full Etymology of English "Loot"

## Primary Origin
English "loot" was borrowed from Hindi लूट (lūṭ, meaning "booty"), which derives from Sanskrit in two possible paths:

1. **Sanskrit लोप्त्र** (loptra) = "booty, stolen property"
2. **Sanskrit लुण्ट्** (luṇṭ) = "to rob, plunder"

## Indo-European Root
The Sanskrit forms trace back to Proto-Indo-European **\*kleh₂-**, meaning "to lay down, deposit, overlay."

## Secondary Etymology (Scoop Sense)
A separate "loot" meaning a scoop or shovel derives from:
- Middle Dutch *loet/loete* → Old Dutch *\*lōta* → Old Frankish *\*lōtija* → Proto-Germanic *\*hlōþþijō* (all meaning "scoop")
- This also connects to Proto-Indo-European *\*kleh₂-*

## Semantic Development
According to the source: "The figurative meaning developed in American English in the 1920s, resulting in a generalized meaning by the 1950s," expanding from plundered goods to any valuable items received free or money itself.

The word entered English dictionaries during British colonial India, as documented in the 1788 *Indian Vocabulary*.
```


## [2026-09-07T01:41:57.817Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/loot",
 "prompt": "Full etymology of \"loot\" including Hindi and Sanskrit forms and any PIE root given."
}
```


## [2026-09-07T01:41:59.852Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BB%CE%B5%CE%BA%CE%AC%CE%BD%CE%B7",
 "prompt": "Give the etymology of Ancient Greek λεκάνη (lekanē): its derivation, related λέκος, whether it is Pre-Greek or a Semitic loan, and descendants/borrowings into Aramaic, Arabic, Persian."
}
```


### [2026-09-07T01:42:01.936Z] TOOL RESULT

```
# Etymology of "Loot"

The word "loot" entered English in 1802 as an Anglo-Indian term. It derives from Hindi *lut*, which traces back to Sanskrit *loptram* or *lotram*, meaning "booty, stolen property." 

The ultimate source is the Proto-Indo-European root *\*reup-*, which means "to snatch." This same root also connects to the English verb "rip."

The verbal form "to loot" (meaning to plunder or carry off as loot) emerged later in 1821. Related words include "looting" (1842) and "looter" (1858), with the latter preserving the original Anglo-Indian agent noun form *looty*.
```


### [2026-09-07T01:42:06.609Z] TOOL RESULT

```
# Etymology of Ancient Greek λεκάνη (lekanē)

## Derivation
The word combines "λέκος" (lékos, meaning "dish; pot; pan") with the suffix "-άνη" (-ắnē), "a suffix for utensil names." The suffix's origin is uncertain.

## Pre-Greek vs. Semitic Origins
The etymology section indicates ambiguity about whether this is Pre-Greek or borrowed. It states the suffix is "alleged to be from Pre-Greek substrate; however, see λάγυνος (lắgūnos, 'flask')," suggesting the origin remains debated rather than definitively established.

## Descendants and Borrowings
The word spread widely through borrowing:

- **Aramaic**: לַקְנָא (laqnā) and variants
- **Arabic**: لَقَن (laqan) and لَكَن (lakan), derived from Aramaic
- **Persian**: لَگَن (lagan), which spawned further descendants
- **Coptic, Armenian, Georgian**: All borrowed the Greek term
- **Slavic languages**: Entered Old East Slavic as лоханꙗ (loxanja), eventually reaching Russian, Ukrainian, and Belarusian
- **Polish and related languages**: Adapted the Slavic form

This borrowing pattern suggests the Greek term became a regional standard for describing large vessels across Mediterranean and Near Eastern cultures.
```


## [2026-09-07T01:42:23.072Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page 699\\]/,/\\[pdf page 701\\]/' BQT_v3_pages.txt | head -70"
}
```


### [2026-09-07T01:42:24.294Z] TOOL RESULT

```
[pdf page 699]
[NOT OCRED - use tools/ref_page.py]
[pdf page 700]
[NOT OCRED - use tools/ref_page.py]
[pdf page 701]
```


## [2026-09-07T01:42:27.170Z] TOOL CALL #46: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1904 --image 2>&1 | tail -60"
}
```


### [2026-09-07T01:42:33.542Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1904.png
REF: BQT:1904  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 701  OCR-lang: fas

[هاات -۱۹۸-
باغد ‎٩‏ ۳ لبون . طشت بی‌آفتابه راگوبند وآن طبق‌دبواره
هلگ ؟- بت هردو لام و سکون‌هر داری است که از مس یا چم
دوکاف فارسی » پرنده‌است معروف و «عرب آن بر نج‌سازند وهم دست‌درآن
لقلق باشد : شونند وهم خمیرنان درآن یست ۳
لگمله ؟ » بنتح اول ونانی ونالت. بمعنی کنند 9 و بکارهای دیگر لگن
نگد کوب باشد وآن کنك ولنی است که بابلی | نیز ید «
بزنند نه با دست . لگود - بروزن سبور . جمعی ازسحرا
لگن ؟ - بنتح ارل و نانی و سکون نعینان‌اند که در حوالی هرات میباشند ‎٩‏ .
بیان هیجدهم
در لام با میم مشتمل 0 ند لغت
لم - بفتح اول و سکون ثانی » بمعنی باشد ۸ .
رحمت و بخشایش باشد - و بمعنی آمایش هم . لما - بنتح اول و ثانی بالف کشیده :
هت ۷ - ودرعربی بمعنی نه است که لا دوائی است ‎٩‏ که آنرا عنب الثملب خوانند .
‎٩‏ - میرخت از لجام براقش چو برق اور زبشان لگام ریز شه آمد پشهر در .
امیرخسرو دهلوی ای اندراج له
۴ «لکلك. ۴ - ر4 : لکد (ح) .
۴ - بونانی 16162۵86 » عربی لقن » سربانی81828 »کردی 1685068 (لگن,طفتك).
6082 . 12848 ( دوری بزرکه. برای غذا ) ؛ ثرکی « لگن > « ژابا ص ۳۸۰ در آرامی
« لقنا > » ممرب‌آن لفن ( بفتح اول و دوم ) و لکن ( بفتح اول ودوم ) « تفی » » اصلا ازبابلی
0 , 1181000 ۰ 118746۵ (ظرف ۰ پیمانه کندم) ( ۰0:158 82521.۸99[7 ,807014)
- و نیز شمه‌دان » طشت شمع :
کوکبی‌آری ولیکن آسمان تست موم عاشفی‌آری ولیکن هت معشوقت لگن.
« منوچهری دامغانی ( درلغز شمع ) ص ۹4 ن
۹ - طابفه‌ای از طوایف ناحیهٌ مکران است ۶« کیپان . جغرافیای سیاسی ی ۱۰۰ *.
۷ - لم دادن » لم زدن » لمیدن » حالتی‌است میان نشتن و درا ز کشیدن برای آسودن
و استراحت کردن :
کام دل مرا چه شودگر برآورد شیرین لبت که لم زده برمتکای ماچ .
ملا فرقی بزدی « آنندراج » ۰
۸ - بکدم بکش فندیل را . بیرون کن اسرافیل را پر برافتر جبریل را
نه لاگذار آنجا نه لم. سنائی غزتوی « لغت نامه » .
‎٩‏ <علب‌الملب . سکه انگور . تاج ریزی « لغت نامه ».
لد - بفتح اول و دوم ,گیلکی 128080 . طبری «لو» ( نگد ) « واژه‌نامه۹۹۲»:
و فس : لگکه ؛ ضرب با پا - طپانچه , لطمه .
```


## [2026-09-07T01:42:45.089Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg313.png"
}
```


### [2026-09-07T01:42:45.438Z] TOOL RESULT

```

```


## [2026-09-07T01:42:45.434Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T01:43:14.132Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SNS kahrup\"; grep -n \"kahrup\\|kah-rup\\|kahrub\\|khlp\" SNS.txt SNS_pages.txt 2>/dev/null | head; echo \"== AFA laqan\"; grep -n \"laqan\\|lakan\\|Lakan\\|lekane\\|Aexdvrj\\|laqna\" AFA.txt | head -20; echo \"== AFM\"; grep -n \"لقن\\|لكن\" AFM_pages.txt | head -10; echo \"== LKT\"; grep -n \"lekane\\|lagan\\|laqan\\|lakan\" LKT.txt | head -10"
}
```


### [2026-09-07T01:43:14.224Z] TOOL RESULT

```
== SNS kahrup
SNS.txt:32519:kahrubay 209/7 
SNS_pages.txt:16120:hu-mat 73/9                                                   judtar 340/20             kahrubay 209/7
== AFA laqan
== AFM
476:* (البردي ) فارسي مخض وهو ضرب من اجود القن
571:» ( ܐܢܝܟ ) الكندر معرب بِسْتَك وهو الككندر الابيض وقيل صمغ سجر
1138:له بالعر بسة الريحان السلمالي 18039 فسلكن وسلوالى فسلكن »
1284:اتكلية ܚܐܪ ܒܗ اي الناظر اليه اي الى الشمس ٠‏ ولكن ܨ 2 اللفظة مركّة
1470:والمنطقة والقنطرة
1730:| سيعت بان سعد القن يرحل لملا فاعلم 3 ܢܘ في مكانه ( حيط ܐܬܝܐ ) ٠‏
1743:( الدهليز) ما بين الباب والدار تعريب دهله 5 القنطرة والعقدة
2458:ܡ القناه فعر بة عن 29 01101
2659:قال في البرهان القاطع : « شاه إسبرغم > الهمزة هو « فسلكن › !ܐ رياأا
2835:0 ܟ 7 دواء 8 في حوف القنا المندي اوهو رماد ܟܕܬ | معرب
== LKT
667:einer  Feslunii'.  Wenn  Löbel  EITAP  11 diese  Ableitung  mit  mehr  als  einem Schein  von  Recht  elimologia  indoiosä nennt,  so  sind  die  folgenden  Wörter aus  semantischen  Gründen  unzweifel- haft aus  dem  angegebenen  Grundwort abzuleiten  und  Annahme  eines  ahd. palco  'Balken'  als  Grundwort  abzuleh- nen: it.  balcotie,  frz.  balcon,  rum.  halcon, sp.  balcÖH,  pg.  balcäo;  dtsch.  Balkon, engl,  balconi/;  russ.  bulg.  serb.  poln. balkon,  6ech.  bulkön.  —  Auf  direkterem Wege,  höchstens  über  tat.  bälahane  ist russ.  balagan  'Marktbude  aus  Brettern, Schaubude'  entstanden.  —  Andere  Ab- leitungen s.  DE  60.  Eguilaz  97.  ZfromPh V,  244;  XXX,  557.  [Gorjajew  9  u.  10. ML  890.
1253:'Tropfen'  [Stamm  dam  'tröpfeln',  s.  hier Nr.  478],  auch  'SchlaganfaU' ;  hieraus rum.  dambla,  damla  'dass.',  damblagiü; bulg.  damla  'dass.'.
3006:1290.  Ar.  lakan:
3007:Auch  lakan  'Schale'  [aus  gr.  XaKÖvr) ZDMG  LI,  303],  ebenso  tk.  ;eÄ;m 'Wasch- schüssel'; hieraus  rum.  lighian  'Wasch- becken', serb.  ledjen  'Becken',  h\i]g.lihen, lejen,  klruss.  lochann,  russ.  lohan  'dass.'; öech.  lihanec  'Art  Kuchen'  [wegen  der Form].    [Mikl  SlEtWb  163  b  und  168  b.
5304:lagania  657
```


## [2026-09-07T01:43:16.396Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC leup\"; grep -n \"leupō\\|leup-\\|laubos\\|loptron\\|laubh\" IEC.txt | head -20; echo \"== WLD band3 leup\"; grep -n \"leup\\|leub\" WLD_band3.txt | head -20; echo \"== WLD Bd2\"; grep -n \"leup\\|abschälen, entrinden\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T01:43:16.478Z] TOOL RESULT

```
== IEC leup
9745:(leup- notional e-grade of radical lup-, see also loup-. WP IT, 417)
10110:loupos 'stripping, plunder; stripper; stripped thing, peel. leaf. WP II, 417. Cf. loupeio, lup-, lump- Skt. lopah “violence, robbery’; Av. raopis ‘kind of dog, *towser'^; Per. rubà-, cpds. trobbery-'; Lat. lüpus (wolf: Av. raopis. Not to type *ulquos!; also = ‘hops; kind of bean; lupus — a wasting disease', also here); Go. lauf, n. ‘greenery’; laubos, mpl. ‘leaves’; MHG loup, gs loubes, sn. «leaf; OE leaf, n. id.; ON lauf, n. id.; Sw. lof, n. id. Cf. also MHG louft, sm. ‘pod, rush, reed; Cz. lup, m. ‘loot; scale’; lupy ‘dandruff; cf. lupen, m. “leaf”; Li. laüpas “bark, rind, skin, flake'; laupüs, adj. “peeling”
14574:reupó (rup-) 'téar, break, burst, plunder. Cf. rüp-, leup-. (Skt. ambig.) WP II, 354 Skt. (ambig.) rupyàmi, v. (“ violate; be racked'. Cf. leup-, lup-); Av. rup- v. “attack, rob” (am- big. as Skt.); Lat. cf. (rumpo, ére), pf: rupi, sup: ruptum, v. ‘burst, têar, violate, beat, tire’; MHG riefen, wv. ‘quarrel; OE reofan, sv. 2. 'téar, break’; ON rjúfa, v. “break in’;
== WLD band3 leup
3063:baachen spes- — hochkommen- fensth— 935 hen saps O90", | hell ecin Meuy- 378. been 2, syeud- 554". ie jiu- B20). hemmen glen. 402 402. | heucheln — feud- 415*. 3, gel- 438, web 22%, | heulon ul- piu- 12%, om- G25" hilfreich sein 4. ay-, ayé-, mai- 222%, | Henkel keg- 382, | ai. 10. Haute panies ae pie af 42. A hin, hinan 4. an, amd, nd = H- aU. ern Z , Be~ LL = inflen- 1 | herabfallen Arews 872, | hinnuf. pad err LL = Le hern hiingen 43 a = ol emaiinemancene ec lonliheneend iat die nie es fd 189. : Puro 147 falleup 7108 hinbreiten (fluch) 2. ater. Li: pel- GB". hera 2, adi~ 450". nile i gett (abgespaltenc) (*em- | herabtraufein 2, gue G00, | Hinderu — 1. qom- viet ng, | Restate ar, | Mn a &e fraube) 1.(@)g6r~ 305%. | eee e ener ee eee, |, hineinschiipien weag. 253° Hautbentel HET 205* arb athhuro- @ hinfahren Aber Bred a. ei a 308 pl _ (von Geschimack) .'| ‘oye Reig TNB | ptm SBR | flggabe User 88, Gbh- 177. : Fea [are Pa | eae es ghovor 834. | Herr arjo 80, breit) wla- 48%:
3069:hocken leup 714. Hode negith-rde 134 in die Hahe in ne in die Hohe gehen sqand- ) Hobie 3. mere 304%. hibion == L.Bed~ 110°. fajgep- H50*, Hohinng : sie Fae Oe (langliobe “ eae qteiat } ; biem) Sau 17. | Blew 404, eg etw.) L. geu- 308, oie i xl 411. hohl 332. _ oo aD
3095:; en | - | leuchtend igi at Tauber powgoa TT.) | adh faded tar =) Laben aiy-, dpa 6. | 4 . leben géeno)} 663. | leugnen B. aie ee ! feibh- 404%. | lith kaet- SOL Leber jet 205. | wg bMoidos 217" lobbatt sein cudh- 270%, | eat Lemay .. lieve 7 fem 4354" lichtechwach maure- 22a" L lah- SH9*, | 1. Met- 358. Feige 400 leubh- AL9%, (sthnalrend) fiog-- 380", | lieben wen 20S. Lado o 428°, | itery- H42*. Laxderboutel mag- 225%. liebreich 8. mex 344°. eens re 425. Lidegeeta "et- S58. ie Soe ct Peete ales, S06". gee - leer lL. eu-,eya- 108.) feyh- 42e*, | leer sein ghé(a}- 542 Lin rege dO2*. feeren ree 7. link jou AT2*. lezen 2. dhe S26. DADE « rei}. Legh- 424%, | links 79%. lehnen Vie. 490. Lippe 1b*.. Ishren = Le dene THR, | tobe 6 Leib 1. grep- 436. | - 410° Lad besf Louke r- 413. or rare eens | ih) 41d" | donk 5. nr dae. | Sua eee Liwe ongho- G05*. inde 3 iG, Lehn veatactd oy Leichen (aut Schlachtfeld) | loven gas dt. ei 304. ay oe put» 107. lede bit wah ot gre, aud 3. yer 225. leicht und echonil renghwe lustassen sorry: leiden oes 513. ne
== WLD Bd2
27335:252, Kluge s. v., Falk-Torp u. los^ Boisacq s. v. (Fiir ein neben leup reap  :
27648:                                                     leup-,    leub(h?)-                                                417
27718:418                                               leup-, leubli(?)-
28596:wird.            dock    s.    u. sleup „schlafF herabhangen^*'); da auch als „schlafF‘^ auf
28599:da sie auch bei der Parallelwz. ^leup-, -h- die Bedd. „schalen, Bart, Frucht^
28608:    doch s. sleup-     daB auch lep- „schalen“ und ,,schlaff herabhangen^^
28615:                             wohl triigerisch (s. sleup-), und zudem in der
47117:710                                   (s)leup-, (s)leub(h)-    — sleag-
47138:woriiber u. leup- ,.abschalen“), mnd. lobbe j,hangende Lippe, Manschette“,
47159:von ursprunglicher Gleichheit mit leup-^ letibh- „abschalen" (etwa zunachst
```


## [2026-09-07T01:43:28.282Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27648,27720p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T01:43:28.353Z] TOOL RESULT

```
                                                     leup-,    leub(h?)-                                                417

bait. Worte             widerlegen Hirts PBrB. 23, 335 Aimahme,
                                                         daB slav. ljudhje
aus     dem Germ, eatlehnt sei).Die Bed. „Gemeinfreier'‘ von burg, leudis
und aksl. Ijiidim ist aus „Angehoriger des eigenen Volkes, gegeniiber den
Unterworfenen“ entwickelt; ebenso beruht auf einem idg.            „Yolk“
nach Schrader lA. 9, 172 gr. EXev'&eQoq „frei (^Yolksangeh6riger)“ == ital.
Hotifero- in            lat.   Vihei',   -era^ -ertim „frei“, fal.            loferta „liberta“ (usw.,             s.   Yf.
LEWb.2 s. V., Herbig Tit. Fal. 8).
     Diesem Ursprung des gr.-lat. Wortes fiir „frei“ fiigt sich nicht van Heltens
ZfdtWtf. 11,56 Deutung von got. *lmis „leer,                                    frei von, nichtig“             usw. aus
verwandtem               *loudJi-to-; es bleibt bei Heu-s- „los®n“.
     Kaum richtig wird vielfach unter einer Bed. „hervorkomnien oder steigen“
— „kommen, gehn‘^ angereiht gr. elevooixat „werde kommen“ Pf., elXrj-
Xov'&a, elkyilovdiiEv {el- metr, Dehnung), att. elr\lv^-a^ -afxev                                ^ Aor. IjXv^ov
(^X'&ov, iX'&eiv daraus rein lautlich oder durch Kreuzung mit^r^ov? s. "^enedh-
„gehn“), deren      bloBes Praesensformans scheint wegen iX'ijiv-juev, -rt,
enriXv-rog,          „Ank6mmling“, ngooijXvTog „im Lande ansaBig ge-
                    ejirjXvTfjg

wordener PremdeF', eniqXvg, -'jjXvdog „fremd“ (s. Brugmann 11^ 3, 373,
Boisacq s. v.); mit l]Xv'dov ist gleichzusetzen air. sg. lod^ 3. sg. luid^
dolluid „ich, er ging“ (perfektisch geworden, 1 pi. -lodmar^ 3. pi. lotar,       .


-Idatar)^ Pick            H
                 534 (nicht nach Pick II* 253 als "^pludo zu ^pleu-d-^ dt.
fliefien) und vielleicht als Kausativ auch zu verbinden air. imluadi „setzt in
Bewegung^', farltiadi „schwenkt‘', hiaid- „be wegen, erwahnen, au6ern“ (Brug-
mann II ^ 3, 262; von Pick II* 253, Pedersen KG. II 572 hinwieder zu
'^pleti-d- gestellt).           —
                        Uber arm. ehimnem s. vielmehr u. eld- „treiben“.
 . S. Pick I* 122, 298, 534^ III * 375, Hirt Abl. 116f., Falk-Torp u. lod III,
lodde^ ladd^ lyd II.
  Cymr. llwdn „Junges von Tieren'', mbret. lozn, loezn (d. i. Zom), nbret.
loeyids. (wozu nach Schlutter AJPh. 21, 192 ludaris „steor“ CGIL. Y 369,

30) haben wie ir. loth „Fullen“ vielmehr Wzausl. -Z- und bleiben fern
(Pedersen KG. I 135 denkt an *plot-^ Yariante neben slav, plodz „Prucht'‘,
8.   phel „schwellen“; eher ursprgl.                     «).      Hierher air. luss        (s.   S. 418).


lenp- und leub(h?)- „abschalen, entrinden, abbrechen, beschadigen^; ob
    richtiger mit -ou- (; o in lit. luhas):du {-au- in alb. Vahe; doch vgl.
    t^aps „wunsche“ zu leuhk- j.gem haben^') anzusetzen?      Ob die zweite
    Wzf. mit h oder hh auslautet, ist unsicher; aisl. laupr kann idg. h
    haben, wobei dt. Lauh der Wzf. auf -p- zuzuteilen ware wenn Laiib                              ;


    hingegen idg. hli enthalt, kann aisl. laupr p aus -hhn- haben letzteres                                ;


    mir wahrscheinlicher (und gesichert, wenn zu Laub auch die Gruppe
        got. luhja-leis'Av, luib gehort,                  s.   u.).

     Mit p-:
     Ai. lumpdti „zerbricht, beschadigt, pliindert^, lopdyati „verletzt''                                      (= slav.
lupiti^   lit.     laiqyyti\ Idptra- n. „Beule‘';                lit.   lupu^ lupti „abhauten, schalen“,
lett.   lupt „ds.,             berauben'S     lit.    laupyti^        lett.   Idupit   „schalen,           abblattern;
rauben‘‘,        lit.   lupinod, -nos PI. ,jObstschalen'‘, lupsnis „abgeschalte                                Tannen-
rinde“; mss.                       Zi/p/Zt „8chalen,     abschalen; aufpicken (Pier)                   ;
                                                                                                           die Augen
aufreiBen,         glotzen;         schlagen,        prugeln“, lipa „H^iutschuppe“,                        ksl.   lupezh
„Raub‘‘ (usw.,            s.    Berneker 746f.);
              :




418                                               leup-, leubli(?)-
```


## [2026-09-07T01:43:29.075Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kahrubay\" -A4 -B4 SNS.txt | head -30"
}
```


### [2026-09-07T01:43:29.139Z] TOOL RESULT

```
32515-kaskSnag 208/9 
32516-ka/kad 50/3 
32517-kadara 211/1 
32518-kadar 210/17 
32519:kahrubay 209/7 
32520-ka-iz 50/12 
32521-ka-iz-is 50/15 
32522-
32523-kalSnd6nd(?) 215/3
```


## [2026-09-07T01:43:42.003Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON لگن\"; grep -n \"لگن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"== HUB rup\"; grep -n \"rubūden\\|rubuden\\|rupäy\\|kah-rup\\|kahrub\" HUB.txt | head -10"
}
```


### [2026-09-07T01:43:42.083Z] TOOL RESULT

```
== MON لگن
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15851:قاصره‌یی لگنی: (پز.) قولون سینی شکل. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15857:فوقانی لگن را از چپ به راست به شکل 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15858:قوسی می‌پیماید و بعدا در لگن فرو می‌رود 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15861:خاصره‌یی لگنی. قولون صاعده: (پز.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:30941:میان. لگن خاصره. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:37493:تولید قولنج کلیوی می‌نماید؛ لگنچه؛ لنچ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40234:لگن: «مودا (۱.) تشتی فلزی که در آن دست 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40244:دهنده لگن محسوب است. لگن در حقیقت 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40247:لگن بزرگ و دیگر لگن کوچک در پایین 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40248:تنگه. در حفرة لگن خاصره قسمت‌هایی از 
== HUB rup
```


## [2026-09-07T01:43:43.477Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT lobby/loft/leaf\"; grep -n \"^LOBBY\\|Lobby\\|lobby\" SKT.txt | head -5; grep -n \"lobia\\|laubia\\|lobium\" SKT.txt KLN_1966.txt FSD_vol3.txt 2>/dev/null | head -10; echo \"== ARY ربودن\"; grep -n \"ربودن\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T01:43:43.580Z] TOOL RESULT

```
== SKT lobby/loft/leaf
10068:lobby,  a  small  hall,  passoge.  (Low  L.
10548:LOBBY.
23128:lobby — lodge.
SKT.txt:10072:cf.  Ital.  loggia.  Low  L.  lobia,  a  pallerj', O.  H.G.  l»ubd,  M.H.G.  hude,ua  arbour (above).
KLN_1966.txt:2980:antilobium,  n.,  the  tragus  (anat.)  —  Medical  L., fr.  Gk.  avxiX6|8iov,  ‘the  upper  edge  of  the  ear’, fr.  avxt,  ‘opposite,  in  front  of’  (see  anti-),  and Xo|36;,  ‘lobe  of  the  ear’.  See  lobe, antilogarithm,  n.,  the  number  corresponding  to  a logarithm  (math)  —  Formed  fr.  anti-  and  lo¬ garithm.
KLN_1966.txt:4706:believe,  tr.  and  intr.  v.  —  ME.  bileven,  fr.  OE. beiifan,  belefan,  rel.  to  gelyfan,  gelefan,  OS.  gi- lobian,  Du.  geloven,  OHG.  gilouben,  MHG.  ge- louben,  glouben,  G.  glauben,  Goth,  galaubjan , ‘to  believe’,  and  to  OE.  geleafa,  ‘belief’.  See prec.  word.
KLN_1966.txt:8250:and  cp.  allusive  and  words  there  referred  to. Derivatives:  collusive-ly,  adv.,  collusive-ness,  n. Collybia,  n.,  a  genus  of  agarics  ( bot .)  —  ModL., fr.  Gk.  xoXX'jpo;,  ‘coin’,  orig.  ‘(small)  change’, which  stands  for  *ypKk\s<poq,  and  derives  fr.  Heb. hdldph,  fr.  haldph,  ‘he  changed’.  Mishnaic  He- brew  qolbon,  ‘rate  of  exchange’,  has  been  rebor¬ rowed  fr.  Gk.  x6XXu(3o<;.  Cp.  caliph, collyrium,  n.,  an  eye  salve  ( med .)  —  L.,  fr.  Gk. xoXXijptov,  ‘poultice,  eye  salve’,  dimin.  of xoXXopa,  ‘a  loaf  of  coarse  bread’,  which  is  rel. to  xoXXi!;,  °f  s.m. ;  of  unknown  origin.  The  eye salve  was  called  xoXXfjpiov  (‘a  little  loaf’),  be¬ cause  it  was  made  up  in  small  loaves, colo-,  before  a  vowel  col-,  combining  form  de¬ noting  the  colon  (med.)  —  Fr.  Gk.  xoXov.  See colon,  ‘part  of  the  larger  intestine’, colobium,  u.,  a  sleeveless  or  short-sleeved  tunic, formerly  used  by  the  clergy.  —  Late  L.,  fr.  Gk. xoX63iov,  fr.  xoaoSgc,  ‘docked,  curtailed,  muti¬ lated’,  fr.  xoXop,  of  s.m.,  whence  also  xoXousiv, ‘to  cut  short,  curtail’ ;  rel.  to  xXoiv,  ‘to  break’, fr.  I.-E.  base  *qel(a)-,  *qol(a)-,  ‘to  strike,  beat’. See  clastic  and  cp.  the  next  two  words  and  the first  element  in  colure.
KLN_1966.txt:8251:coloboma,  n.,  a  defect  of  the  eye  (med.)  —  Medical L.,  fr.  Gk.  xoXo^ojpa,  ‘the  part  taken  away  in mutilation’,  fr.  xoXo(3oi3v,  ‘to  mutilate’,  fr. xoXopop,  ‘mutilated’.  See  colobium.
KLN_1966.txt:8253:—  ModL.,  fr.  Gk.  xoXofio:,  ‘docked,  curtailed, mutilated’  (see  colobium);  so  called  in  allusion to  the  thumbs.
KLN_1966.txt:8300:Derivatives:  columnar  (q.v.),  column-ed,  adj. columnar,  adj.,  formed  in  columns.  —  L.  colum- naris,  ‘rising  in  the  form  of  a  pillar’,  fr.  columna. See  prec.  word  and  -ar. columniform,  adj.  —  See  column  and  -form, colure,  n.,  one  of  the  two  celestial  circles  intersect¬ ing  each  other  at  the  poles  ( astron .)  —  Late  L. coluri  (pL),  fr.  Gk.  al  xoXoupot  (scil.  ypanpou), ‘the  colures’,  lit.  ‘the  truncated  (lines)’,  pi.  of xoXo’jpo;,  ‘dock-tailed’,  which  is  compounded of  xoXo?,  ‘docked,  mutilated,  curtailed’,  and oupd,  ‘tail’  (see  colobium  and  uro-,  ‘tail-’);  so called  because  in  Greece  their  lower  part  is always  ‘cut  off’  (i.e.  beneath  the  horizon). Colutea,  n.,  a  genus  of  plants  of  the  pea  family (hot.)  —  ModL.,  fr.  Gk.  xoXouteS,  xoXoit££, xoXcoTed,  name  of  a  tree.
KLN_1966.txt:17961:colobium,  coloboma,  Colobus,  coup,  gladiator, glaive,  Procellaria.  Cp.  also  the  first  element  in colure.
KLN_1966.txt:22012:lobby,  n.,  a  hall;  a  vestibule.  —  ML.  laubia, lobia,  fr.  OHG.  *laubja.  See  lodge,  which  is  a doublet  of  lobby.
KLN_1966.txt:22013:Derivatives:  lobby,  tr.  and  intr.  v.,  lobby-er,  n., lobby-ism,  n.,  lobby-ist,  n. lobe,  n.  —  MF.  (=  F.),  fr.  Late  L.  lobus,  fr.  Gk. Xo(3o?,  ‘lobe  of  the  ear;  lobe  of  the  liver;  lobe  of the  lung;  seed,  pod’,  prob.  rel.  to  Gk.  X^pivS-oi, ‘peas’,  Xep-qpii;,  ‘husk  of  fruits’;  fr.  I.-E.  base *leb-,  which  is  ret.  to  base  *lep-,  ‘to  peel’, whence  Gk.  kir.ew,  ‘to  peel’.  See  leper  and  cp. lobule  and  the  second  element  in  bilobate,  trilo¬ bate,  antilobium,  Gonolobus.
== ARY ربودن
```


## [2026-09-07T01:43:57.211Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^leaf,  n\\|leaf,  n\\.\\|lodge,  n\\.\\|loft,  n\\.\" KLN_1966.txt | head; echo \"-----\"; grep -n \"loft,  n\" -m1 -A3 KLN_1966.txt | head -20"
}
```


### [2026-09-07T01:43:57.275Z] TOOL RESULT

```
21324:Derivative:  leaden-ness,  n. leaderette,  n.,  a  short  editorial  paragraph.  —  Lit. ‘a  short  leading  article’,  a  hybrid  formed  fr. leader  and  -ette,  a  suff.  of  French  origin, leading,  n.,  leadwork.  —  Formed  fr.  lead,  ‘a metal’,  with  subst.  suff.  -ing. leading,  n.,  guidance.  —  Formed  from  the  verb lead  with  -ing,  suff.  forming  verbal  nouns, leading,  adj.,  directing,  guiding.  —  Formed  from the  verb  lead  with  part.  suff.  -ing. leaf,  n.  —  ME.  leef,  lef,  fr.  OE.  leaf,  rel.  to  OS. lof  ON.  lauf  Dan.  lev,  Swed.  lof,  OFris.  laf,  Du. loof,  OHG.  hub,  MHG.  loup,  loub,  G.  Laub, ‘foliage",  Goth,  lauf,  ‘foliage’,  laufs,  ‘leaf",  and cogn.  with  Lith.  lupit,  lupti,  ‘to  shell,  peel",  Lett. lupt,  ‘to  peel;  to  rob,’  Russ,  luplju,  lupit',  ‘to peel’,  OSlav.  luhU,  ‘bark,  rind",  Lith.  luba, OPruss.  lubbo,  ‘board',  Lith.  luobas,  ‘bark,  rind". All  these  words  prob.  derive  fr.  I.-E.  base *leub(h)-,  *leup-,  ‘to  strip,  to  peel",  whence  prob. also  L.  liber  (fr.  *luber),  ‘bast,  book’;  see  library and  cp.  alypin.  I.-E.  base  *leub(h)-,  *leup-  is  rel. to  base  *lep-,  ‘to  peel",  whence  Gk.  Xcnetv,  ‘to strip  off  the  rind,  peel,  bark’;  see  leper  and  cp. lodge.
21353:leaf,  n.,  an  open  water  trench.  —  ME.  leet,  fr. OE.  gelset,  geliete,  ‘junction  of  roads,  outlet’, from  pref.  ge-  (see  y-)  and  the  stem  of  Hetan,  ‘to leave’.  See  let,  ‘to  leave’.
22044:lodestar,  also  loadstar,  n.  —  Compounded  of lode  and  star;  lit.  ‘a  leading  star’, lodestone,  n.  —  See  loadstone, lodge,  n.  —  ME.  loge,  logge,  fr.  OF.  loge,  ‘arbor, hut’  (whence  F.  loge,  ‘hut,  cabin,  lodge,  box  at a  theater'),  fr.  OHG.  *laubja,  louba,  ‘porch.
22050:loft,  n.  —  ME.,  fr.  Late  OE.  loft,  fr.  ON.  lopt,  ‘air, sky,  upper  room’,  which  is  rel.  to  OE.  lyft  (dial. E.  lift),  Du.  lucht,  OHG.,  MHG.,  G.  luft,  Goth. luftus,  ‘air’.  Cp.  aloft,  lift.  Cp.  also  lodge,  n. Derivatives:  loft,  tr.  v.,  loft-er,  n.,  loft-i-ly,  adv., loft-i-ness,  n.,  loft-ing,  n.
22057:loge,  n.,  box  in  a  theater.  —  F.  See  lodge,  n. logged,  adj.,  made  heavy.  —  Formed  with  suff.
22060:loggerhead,  n.,  a  blockhead.  —  Fr.  obsol.  log head,  compounded  of  log,  ‘a  piece  of  wood’,  and head.  For  sense  development  cp.  blockhead. Derivative:  loggerhead-ed,  adj. loggia,  n.,  a  roofed  gallery  used  as  an  open-air room.  —  It.,  fr.  F.  loge.  See  lodge,  n.,  and  cp. lobby.
36350:splodge,  n.  —  A  var.  of  splotch, splotch,  n.,  blot;  stain.  —  Prob.  a  blend  of  spot and  splash.
-----
22050:loft,  n.  —  ME.,  fr.  Late  OE.  loft,  fr.  ON.  lopt,  ‘air, sky,  upper  room’,  which  is  rel.  to  OE.  lyft  (dial. E.  lift),  Du.  lucht,  OHG.,  MHG.,  G.  luft,  Goth. luftus,  ‘air’.  Cp.  aloft,  lift.  Cp.  also  lodge,  n. Derivatives:  loft,  tr.  v.,  loft-er,  n.,  loft-i-ly,  adv., loft-i-ness,  n.,  loft-ing,  n.
22051-log,  n.,  a  heavy  piece  of  wood.  —  ME.  logge,  of Scand.  origin.  Cp.  ON.  lag  (whence  Dan.  laag, Norw.  log),  ‘felled  tree’,  orig.  ‘that  which  lies’, from  the  stem  of  ON.  liggja,  ‘to  lie’.  See  lie,  ‘to recline’,  and  cp.  the  first  element  in  loggerhead. Derivatives:  log,  tr.  v.,  to  cut  into  logs;  intr.  v., to  fell  trees  and  transport  the  logs  to  a  sawmill, adj.,  logged  (q.v.),  logg-er ,  n.,  logg-ing,  n. log,  n„  a  liquid  measure,  the  12th  part  of  a  hin. —  Heb.  logh,  rel.  to  Syr.  lagga,  laggitha,  ‘a  (des¬ sert)  dish’,  and  prob.  also  to  Arab.  Idjja,  ‘was deep’,  Iqij,  ‘depth,  abyss’,  Akkad,  lignu,  ‘vase, vessel’.  Cp.  also  Copt,  lok,  ‘a  liquid  measure', and  see  lagena.
22052-log,  n.  —  Abbrev.  of  logarithm, log-,  form  of  logo-  before  a  vowel, loganberry,  n.,  a  kind  of  dewberry.  —  So  called after  the  American  jurist  James  Harvey  Logan (1841-1928),  who  first  cultivated  it.
22053-Logania,  n.,  a  genus  of  plants  (bot.)  —  ModL., named  after  James  Logan  (1614-1751),  an  Irish botanist,  secretary  to  William  Penn.  For  the ending  see  1st  suff.  -ia.
```


## [2026-09-07T01:43:58.353Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%DA%AF%D9%86/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for لگن verbatim, including any etymological note (e.g. Greek, Aramaic, Babylonian origin), and also the Dehkhoda entry's etymology if present."
}
```


### [2026-09-07T01:44:03.879Z] TOOL RESULT

```
# Farhang-e Mo'in Entry

The Farhang-e Mo'in provides this concise definition:

"(لَ گَ ) (اِ. ) ظرف بزرگ لبه دار."

(A large-edged vessel)

# Dehkhoda Entry Etymology

The Dehkhoda entry does not provide an explicit etymological note linking the word to other languages. However, user suggestions within the page propose connections: one commenter states the term shares roots with Greek "lekanē" and Akkadian "lakānu," and another notes it is an Akkadian word that entered Persian and Turkish languages, with the Turkish form being "Ləyən."
```


## [2026-09-07T01:44:13.227Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lagena\\|Aexavr\\|lekane\\|laqna\\|lagynos\" KLN_1966.txt | head -10"
}
```


### [2026-09-07T01:44:13.285Z] TOOL RESULT

```
4306:Worterbuch  der  russischen  Sprache,  I,  p.40, Heidelberg,  1908-13,  is  rel.  to  Russ,  balabolit’, ‘to  chatter,  babble',  from  the  I.-E.  imitative  base *balb-,  whence  also  L.  balbus,  ‘stammering’.  See booby  and  cp.  words  there  referred  to. balan-,  form  of  balano-  before  a  vowel, balance,  n.  —  OF.  (=  F.)  balance,  fr.  L.  bi-, ‘two,  twice’,  and  VL.  *lancia,  fr.  L.  lanx,  gen. lands,  ‘plate,  dish;  scale  of  weighing  machine’, which  prob.  stands  for  *llnk-s,  fr.  I.-E.  base *iliq~,  ‘to  bend’,  whence  prob.  also  Gk.  k&aoq, Xexovt),  ‘dish’,  lt/pwc„  ‘slanting,  crosswise’, Xo E,6<;,  ‘slanting,  crooked,  bent’;  see  Walde- Hofmann,  LEW.,  I,  p.761  s.v.  lanx.  See  bi-  and loxo-  and  cp.  the  second  element  in  auncel.  Cp. also  Lecanium,  Lecidea,  lekane.  The  first  a  in balance  is  prob.  due  to  an  association  of  this word  with  F.  bailer,  ‘to  dance’,  fr.  Gk.  paXXeiv, ‘to  throw’  (see  ballistic).
21010:lag,  n.,  retardation.  —  Fr.  lag,  ‘last’, lag  (slang),  tr.  v.,  1)  to  transport  as  a  convict;  2) to  arrest;  n.,  1)  a  convict;  2)  a  term  of  transpor¬ tation.  —  Of  unknown  origin, lag-,  form  of  lago-  before  a  vowel, lagan,  n.,  cargo  sunk  in  the  sea.  —  OF.  lagand, lagan,  of  Teut.  origin  and  lit.  meaning  ‘that which  is  lying’.  See  lay,  ‘to  place’,  lie,  ‘to  recline’, lagena,  n.,  flask,  bottle.  —  L.,  fr.  Gk.  Xayuvoc,  a loan  word  fr.  Heb.  logh,  ‘a  liquid  measure’  (cp. Copt,  lok),  to  which  the  Syriac  suff.  -ena  has been  added;  see  Noldeke,  Syrische  Grammatik, §  132.  See  log,  ‘a  liquid  measure’, lager  (beer),  n.,  a  kind  of  beer  which  is  kept  on store  for  some  months  before  being  drunk.  — G.  Lager,  ‘camp;  storehouse",  rel.  to  OE.  leger. See  lair  and  cp.  laager,  leaguer,  ‘camp’, laggard,  adj.  and  n.  —  Formed  with  suff.  -ard  fr. lag,  ‘to  walk  behind’.
21363:Lecanium,  n.,  a  genus  of  scale  insects  ( entomolo¬ gy ).  —  ModL.,  fr.  Gk.  Xsxaviov,  dimin.  of Xexccv7],  ‘dish,  pan’.  Seelekane  and  cp.  Lecidea. lecanomancy,  n.,  divination  by  the  inspection  of water  in  a  basin.  —  Compounded  of  Gk.  Xs- xctvrj,  ‘dish,  pan’,  and  [iavreia,  ‘oracle,  divina¬ tion’,  See  lekane  and  -mancy.
21369:Lecidea,  n.,  a  genus  of  crustacean  lichens  (but.)  — ModL.,  fr.  Gk.  Xexi;,  gen.  XsxiSo;,  dimin.  of Xsxo;,  ‘dish’.  See  lekane  and  cp.  Lecanium. lecithin,  n.,  a  waxy  substance  found  in  tissues  of the  brain  and  the  nerves  (biochem.)  —  Coined  by Gobley  fr.  Gk.  Xexi&o?,  ‘the  yolk  of  an  egg", which  is  of  uncertain,  prob.  foreign,  origin,  and chem.  suff.  -in.
21440:leitneriaceous,  adj.  —  See  prec.  word  and  -aceous. lekane,  n.,  a  large  dish  or  bowl  ( Greek  antiq.)  — Gk.  XocotvT),  ‘dish,  pot,  pan’,  fr.  Xsxoc,  of  s.m. prob.  meaning  lit.  ‘something  bent’,  and  cogn. with  L.  lanx,  gen.  lands,  ‘plate,  dish;  scale  of weighing  machine’.  See  balance  and  cp.  words there  referred  to.
22051:log,  n.,  a  heavy  piece  of  wood.  —  ME.  logge,  of Scand.  origin.  Cp.  ON.  lag  (whence  Dan.  laag, Norw.  log),  ‘felled  tree’,  orig.  ‘that  which  lies’, from  the  stem  of  ON.  liggja,  ‘to  lie’.  See  lie,  ‘to recline’,  and  cp.  the  first  element  in  loggerhead. Derivatives:  log,  tr.  v.,  to  cut  into  logs;  intr.  v., to  fell  trees  and  transport  the  logs  to  a  sawmill, adj.,  logged  (q.v.),  logg-er ,  n.,  logg-ing,  n. log,  n„  a  liquid  measure,  the  12th  part  of  a  hin. —  Heb.  logh,  rel.  to  Syr.  lagga,  laggitha,  ‘a  (des¬ sert)  dish’,  and  prob.  also  to  Arab.  Idjja,  ‘was deep’,  Iqij,  ‘depth,  abyss’,  Akkad,  lignu,  ‘vase, vessel’.  Cp.  also  Copt,  lok,  ‘a  liquid  measure', and  see  lagena.
22212:Loxia,  n.,  a  genus  of  birds,  the  crossbill  ( ornithol .) —  ModL.  See  prec.  word, loxo-,  before  a  vowel  lox-,  combining  form meaning  ‘oblique’.  —  Gk.Xo^o-, XoJ-,  fr.  X040C, ‘slanting,  crosswise,  oblique’,  rel.  to  XF/pm?, ‘slanting,  crosswise’,  and  prob.  also  to  Xsxo c, Xexavr),  ‘dish,  pot,  pan’.  See  lekane. loxodrome,  n.,  rhumb  line.  —  Back  formation  fr. loxodromlc.
```


## [2026-09-07T01:44:22.186Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewp-",
 "prompt": "Does this reconstruction page exist? Give its meaning, derived terms and descendants (Sanskrit, Iranian, Germanic, Baltic, Slavic)."
}
```


## [2026-09-07T01:44:23.255Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%DA%AF%D9%86",
 "prompt": "Give the Persian etymology of لگن (lagan): what is it borrowed from, and the chain of languages given."
}
```


### [2026-09-07T01:44:23.818Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T01:44:27.889Z] TOOL RESULT

```
# Persian Etymology of لگن (lagan)

According to the Wiktionary entry, the Persian word لگن (lagan) is "Ultimately from Ancient Greek _λεκᾰ́νη_ (lekắnē)."

The document traces the word's journey through multiple languages via its descendants section. The Persian term spread to numerous languages including:

- Turkic languages (Turkish, Uzbek, Kyrgyz, Tatar, Turkmen)
- Slavic languages (Bulgarian, Macedonian, Romanian, Serbo-Croatian)
- Other languages like Armenian, Albanian, and Pashto

However, the entry does not explicitly detail the intermediate language chain between Ancient Greek and Persian. It only indicates that Persian borrowed this word ultimately from Ancient Greek, showing the word's long historical transmission across Mediterranean and Asian languages.
```


## [2026-09-07T01:44:36.584Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A5%8B%E0%A4%AA%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0",
 "prompt": "Give the Sanskrit entry for लोप्त्र (loptra): meaning, etymology (root lup-), and descendants (Hindi lūṭ, English loot)."
}
```


## [2026-09-07T01:44:37.410Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lobby",
 "prompt": "Give the full etymology of \"lobby\": Medieval Latin lobia/laubia and its Germanic source, plus any relation to lodge and leaf."
}
```


### [2026-09-07T01:44:43.833Z] TOOL RESULT

```
# Etymology of "Lobby"

**Medieval Latin Origins:**
The noun "lobby" traces back to the 1550s, deriving from Medieval Latin *laubia* or *lobia*, meaning "covered walk in a monastery."

**Germanic Root:**
This Medieval Latin term comes from a Germanic source, with parallels to Old High German *louba*, meaning "hall" or "roof."

**Architectural Evolution:**
The meaning shifted from "cloister, covered walk" (1550s) to "large entrance hall in a public building" (1590s), then to its reference in the House of Commons (1630s).

**Political Development:**
By the 1790s in American English, "lobby" acquired its political sense, referring to "those who seek to influence legislation"—arising from the custom of influence-seekers "gathering in the large entrance-halls outside legislative chambers."

**Related Words:**
"Lobby" connects etymologically to both "lodge" and "leaf" through their shared Germanic root *laubja-*, which originally may have meant "shelter of foliage" or "roof made from bark."

**Verb Form:**
The verb form emerged later, in 1826, from the noun's political sense, describing the act of seeking to influence legislation.
```


### [2026-09-07T01:44:46.319Z] TOOL RESULT

```
# Sanskrit Entry: लोप्त्र (loptra)

**Meaning:** This neuter noun denotes "stolen property; loot; booty," according to the Wiktionary entry.

**Etymology:** The word derives from the root लुप् (lup) combined with the suffix -त्र (-tra), as indicated in the etymological section.

**Linguistic Note:** The entry documents the word across multiple writing systems (Devanagari, Bengali, Tamil, Telugu, and others) and provides detailed declension patterns for the neuter a-stem noun category in both Vedic and Classical Sanskrit pronunciations.
```


## [2026-09-07T01:45:01.480Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/loot' \\\n 'https://www.etymonline.com/word/loot' \\\n 'https://en.wiktionary.org/wiki/%CE%BB%CE%B5%CE%BA%CE%AC%CE%BD%CE%B7' \\\n 'https://en.wiktionary.org/wiki/%D9%84%DA%AF%D9%86' \\\n 'https://abadis.ir/fatofa/%D9%84%DA%AF%D9%86/' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A5%8B%E0%A4%AA%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0' \\\n 'https://www.etymonline.com/word/lobby' \\\n 'https://en.wiktionary.org/wiki/%D8%B1%D8%A8%D9%88%D8%AF%D9%86' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 313: roots Leup (robudan, loot, leaf/lodge/loft/lobby) and Lignu (lagan, lekane)' 2>&1 | tail -2\ndone"
}
```


## [2026-09-07T01:45:03.433Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg313.png data/verification/sources/refs/ocr/BOOK/313.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-07T01:45:06.668Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/405e98d9ed0137af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1499836f96bc841b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7a6232cd67f02269.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9c25a2968bd1887.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e2608248c2bd240.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bda0bfaed74924cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec483f572f93eb69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49106270eff8b11f.txt
```


### [2026-09-07T01:45:06.729Z] TOOL RESULT

```
total 14068
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 21:45 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-07T01:45:23.087Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"لگن\" incoming/ARY/ARY_pages.txt | head -5; echo \"== ARY latin index lekane/leup\"; grep -n \"LEUP\\|LEUBH\\|RAUP\\|RUP\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T01:45:23.147Z] TOOL RESULT

```
== ARY latin index lekane/leup
4068:TRAUPMAN: (TWENTY) 677 HOLD HIGH GERMAN), fg * ‘
4437:TRAUPMAN: " (FIFTEEN) 529 YUFTIEN (DUTCH) «sacle
4453:TRAUPMAN: 297 FUTTER (4ul2}(GERMAN) glalT
5565:UTRUPETI (SERBIAN) «ype TRUSHP, TRUPSH-(BALUCHI) gz 3h
8909:REV (NORWEGIAN) «5335 URUPI, RAOPL HAVESTAN) gem 3)
12426:POKORNY. —=~SO*~*~S~S~*~«a URUPIS SANSKRIT) 2 Sila
15915:‘TTRAUPMAN, JOHN. THE BANTAM NEW COLLEGE LATIN AND ENGLISH DICTIONARY.
```


## [2026-09-07T01:45:23.755Z] TOOL CALL #64: WebSearch

```json
{
 "query": "Akkadian \"liginnu\" CAD Chicago Assyrian Dictionary vessel measure lignu ligittu"
}
```


### [2026-09-07T01:45:29.896Z] TOOL RESULT

```
Web search results for query: "Akkadian "liginnu" CAD Chicago Assyrian Dictionary vessel measure lignu ligittu"

Links: [{"title":"The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD)","url":"http://www.aina.org/cad.html"},{"title":"The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD) | Institute for the Study of Ancient Cultures","url":"https://isac.uchicago.edu/research/publications/chicago-assyrian-dictionary"},{"title":"Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD) | USC Libraries","url":"https://libraries.usc.edu/databases/assyrian-dictionary-oriental-institute-university-chicago-cad"},{"title":"Chicago Assyrian Dictionary","url":"https://en.wikipedia.org/wiki/Chicago_Assyrian_Dictionary"},{"title":"The Chicago Assyrian Dictionary (CAD)","url":"https://www.atour.com/library/cad/"},{"title":"Dictionaries and Lexica 📖 — eAkkadian","url":"https://digitalpasts.github.io/eAkkadian/bibliography/dictionaries.html"},{"title":"The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD) : Oriental institute of Chicago : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/Assyrian_cad"},{"title":"Chicago Assyrian Dictionary — Grokipedia","url":"https://grokipedia.com/page/chicago_assyrian_dictionary"},{"title":"The Chicago Assyrian Dictionary Project","url":"https://isac.uchicago.edu/research/projects/chicago-assyrian-dictionary-project"},{"title":"cad h","url":"https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/cad_h.pdf"}]

The search results provide general information about the Chicago Assyrian Dictionary (CAD), but they don't contain specific information about the Akkadian word "liginnu" or the related variant forms (lignu, ligittu) that you mentioned. The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD) is a dictionary of Akkadian (Assyrian), compiled over a 90 year period by scholars at the Oriental Institute of the University of Chicago. The CAD is a dictionary of 21 volumes (1956-2010) that presents Akkadian words in context with references to the cuneiform texts.

To find the specific entry for "liginnu" and its related vessel measure terminology, you would need to access the CAD directly. The dictionary is available online, which would be your best resource for looking up this specific Akkadian term and its variations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T01:45:40.504Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ربود\" incoming/ARY/ARY_pages.txt | head -5; echo \"== SYN rob/leaf\"; grep -n \"9.26 STEAL\\|STEAL\\b\" SYN.txt | head -5"
}
```


### [2026-09-07T01:45:40.565Z] TOOL RESULT

```
== SYN rob/leaf
18720:11.56 STEAL
20045:SSESSION, PROPERTY, COMMERCE 739 PO 11.56 STEAL Goth. hlifan, stilan Lith. vogtt ON stela ae ea q ie Nigro Dan. sijale 7hSI. rastt at Sw. stjdla SCr. krasti gs Ou stelan, stalian Boh. —krdsti tes ME stele Pol. kragé Ca robar NE steal Russ. krast , vorovat! a Du. stelen Skt. mug- (cur-) : anim OHG _ stelan Av. —_tarap- idim MHG stelen + Foy, Uadrata NHG _ stehlen
```


## [2026-09-07T01:45:40.639Z] TOOL CALL #66: WebSearch

```json
{
 "query": "Akkadian laganu vessel Aramaic laqna Greek lekane loanword direction Zimmern"
}
```


### [2026-09-07T01:45:47.659Z] TOOL RESULT

```
Web search results for query: "Akkadian laganu vessel Aramaic laqna Greek lekane loanword direction Zimmern"

Links: [{"title":"λάγυνος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BB%CE%AC%CE%B3%CF%85%CE%BD%CE%BF%CF%82"},{"title":"(PDF) Aramaic Loanwords in Akkadian - A Reassessment of the Proposals","url":"https://www.academia.edu/28622616/Aramaic_Loanwords_in_Akkadian_A_Reassessment_of_the_Proposals"},{"title":"Aula Orientalis 23 (2005) 191-198 191 Loanwords in Semitic","url":"https://www.ub.edu/ipoa/wp-content/uploads/2021/09/200512AuOr12Watson.pdf"},{"title":"Akkadian Loanwords in Biblical Hebrew - Paul V. Mankowski - Google Books","url":"https://books.google.com/books/about/Akkadian_Loanwords_in_Biblical_Hebrew.html?id=72gOAAAAYAAJ"},{"title":"Foreign Words in Tanach - The Jewish Link","url":"https://jewishlink.news/foreign-words-in-tanach/"},{"title":"List of loanwords in Classical Syriac","url":"https://en.wikipedia.org/wiki/List_of_loanwords_in_Classical_Syriac"},{"title":"Lakaina","url":"https://en.wikipedia.org/wiki/Lakaina"},{"title":"BIBLICAL ANTHROPOLOGY: Akkadian Lexicon","url":"http://biblicalanthropology.blogspot.com/2017/10/akkadian-lexicon.html"},{"title":"Akkadian language","url":"https://en.wikipedia.org/wiki/Akkadian_language"}]

Based on the search results, I found relevant information about these related vessel terms and their etymological connections:

Akkadian laganu (laḫannu, meaning "flask, bottle of clay, glass or metal") is compared to Aramaic ligna and leginut (meaning "a unit of square measure" and "jug for wine and oil"), and Ancient Greek lekane (meaning "basin"). These terms appear to be related across these ancient languages.

However, I should note that the search results do not specifically mention Zimmern's work on the direction of these loanwords (i.e., whether the Greek word was borrowed from Semitic languages or vice versa). The Wiktionary entry indicates the Greek term is "Probably Pre-Greek," suggesting it may have Semitic origins, but it doesn't provide details about Zimmern's specific scholarly analysis regarding the direction of the borrowing. To get more precise information about Zimmern's conclusions on this etymological question, you may need to consult his original scholarly work or more specialized academic sources on ancient Near Eastern linguistic influences on Greek.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T01:45:57.817Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-07T01:45:57.863Z] TOOL RESULT

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


## [2026-09-07T01:46:39.678Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"loot,\\|loot  \" SKT.txt FSD_vol3.txt WEB_vol1.txt 2>/dev/null | head -6; echo \"== lekane in LKT/DEV\"; grep -n \"1290\" -A2 LKT.txt | head -8"
}
```


### [2026-09-07T01:46:39.758Z] TOOL RESULT

```
SKT.txt:10123:Intolloot  (F-L.1  O.  F.  iff///&f/.- L.  infeiUctus,  perception,  discernment.  — L.  inUlUctus,  pp.  of  inUliigire^  to  dis- cern—L  intei-,  lor  inUr,  between  ;  U^re^ to  choose.
SKT.txt:10664:louse,  an  insect.  (E.)  M.  E.  lotu,  pL fyt.  A.S.  ids,  pi.  lys  (lice).  +  Du.  luis, Dan.  luui,  Swed.  /mj,  loci,  fiii,  G.  /sm/. The  orig.  sense  is  'destroyer;*  from  the base  LUS ;  Kc  Loose  (above),  Cf.  Goth. lamjan,  to  make  of  none  effect Xjoot.  plunder.  (Hindi.  -•  Skt.)  Hindi Itit  (with  cerebral  t),  loot,  plunder.  The cerebral  /  shews  that  r  is  elided. »Skt. /tf/m,  shorter  form  of  tepti-a,  booty,  s)>oil, «SkL  luft,  10  break,  apoil.  allied  to  L. rum/nre,  to  break.  SecBupiore.  (yKUP.) which  is  Tabbed, Da.)    O.  Da  lupftHt  to  auim,
SKT.txt:14017:PUot,  one  who  conducts  ^^ of  harbour.  (F.-Du.)     O.  J F./iVw«.«0.  ¥.  pilotfT,  to  \%K^  iiouu' (Palsgrave).  —  O.  Du.  peilh^  (mod. ptUiaod,  but  Untt  (or  /<W  ocean  in  Heil U.  Du.  Diet.),  a  sounUing-kad.  •O. ptyUn.  contracted  form  oi pegtltH^lom (rem  the  &b.  pegtl,  a  guatje  .    and  O loot,  mod.  Du.  ioixl  (ci.  G.  l»tk\  ea| with  E.  lead,  a  lead  or  plunimel  far  sc iog:    see  Lead  ij>.      ti.    The  form is,    however,  rather  Danish  than  Di the  Do.  word  seems  borrowed  frets pagtl,  a  holf-pinl  measure,  in  which  <M were    measured    hy   pegs    in    the   «i Dan.  p€ft,   to    point :    allied    to  S ptka,  to  point  (and  perhaps  to  £./g
SKT.txt:19589:'ic  sAaniian*  (pt  t  thahta). tkinM^  with  piefix  />€•  =  hy, links.  (E.)  Lii,  •  it  seems  lo  mc ; ' r  is  the  daL  case,  nnd  thinks  is  an verb,  M.  E.  ^/w/yw,  to  secro,  A.  S. r^,  it  SCCIU5  to  me ;  from  ^yruan, ,  +  0.  Six.  thuncioM,  Icel.  \ykkja^ kugkiam.  i.c.  tAhnJ^jan' ,  G.  auftXen, ,.  A  secondary  verb,  allied  to  A.  S. thou^rhl ;  icc  below. Lk.  thanka.  \,E.)  M.E.  \>anJi,  a I;,  kindly  rctnembrsnce,  goodwill; Jtanki,  pi.  expressions  of  goodwill. %Hf,  Jvtc,  ftbu,  thought^  favour,  con- tank.  +  Du.  i/an^,  Iccl.  t>^^'(,  Dan. ifd,  /a^*»  Goth,  thagks,  i.  e.  thanks*^ >nuioe>  thaak.  From  a  Teut.  base .,  to  think,  suppose  ;  ct  O.  Lnt. think,  to  know,  LItb.  tikiti,  to loot  TAG,  prob.  allied  to  V sr.  thank,  verb.
WEB_vol1.txt:20872:‘tained by blood or slaughter. blos’sém, n., [ME 2 > s . [ME. blossome; AS. bléstma blood’y war’riér (yčr), the wallflower, or blosthma, a bloss rer, f w ; ; blou bleeding heart [Cheiranthus Cheiri). blow] _ Eao oni ewan, to PE ie . to gather in at the water Pp.; i bloom, n. [ME. blome, a blossom; AS. bléstma, 1. a flower or bloom, especially of a fruit- blow, n. (ME. blaw, a blo ges tl a blossom, from blõwan, to blow, bloom.] bearing plant. 1. a hit or strok ; yl 1, a blossom; the flower of a plant; an ex- 2. a state or time of flowering, literally and impact of the ha ae fis sudden and Viol e panded bud. _ s figuratively. against an object nd, fist, or an instrument d While opening blooms diffuse their sweets 3. the peculiar color of a horse, when bay or 2. an act of hostility: ae ay G around. | A —Pope. sorrel hairs are mixed freely with white; a forcible effort; as the | a sudden attack 2. the opening of flowers in general; state kind of peach color. ; the first blow.’ € nation which strikes K or Gime Of blossoming. , i in blossom; in the period of blossoming; 3. a sudden calamity or misf S | A weer Y time o most beauty, vigor, applied to plants or trees. or severe evil; as, the Hows: P panes sudden fi 4 Mite fine gray dust Be Peer cotame ond blos’sdm, v.i.; blossomed, 2t., pp.; blossoming, too hard for him,’ Of SOHNE are 3 grapes newly, gathered; also, figuratively, Ae eer a: aeeee ee effort; in one ween: oe te sti with a single | ; Er- aea t e e to erence 2. to flourish and prosper. at a blow. j SS) VO gan a kingdom Í p Pee aout , healthy glow; as, the bloom on her The desert shall rejoice, anid bossom as the to come io blows; to engage in combat bl Ey- no p 3 A rose. —lIsa. xxxv. 1 yn.—stroke, inflicti “is us ~ ay ie cc ot cloudiness Ben pols: blos’s6m-less, a. without blossoms. affliction, knock, shock, calamin poimtment, i given to a picture by varnish. S SR blos’som-y, a. 1. having many blossoms. blow, v.i.; blew, pl.; blown, pp.; blowing: a G (E tr yellow powder found on leather after blot, Be a PDR pp.; blotting, ppr. [ME ee oraw: AS. blawan to blow} y a complete tanning. PAFOS > Dt., PP.-; z, ppr. [ME. : stir or speed up a cu $ ae 8 any of several minerals of a bright color, blolten, to blot, from Ice. bletir, a blot, spot.) move, as air; particularly, to ore i © oe, found in a powdery state. a aS aine perator (0) Blur} meae PR rth oe wind blows : f bloom, v.i.: bloomed, pl., pP.; ee A a papcr. . to send forth air witl EPPA D cee eae eS z oe a Fe Ome Per 2, to obliterate; to cancel or efface (usually mouth; hence, to pant; to pub i ba the £ 2. to be in a state of healthful, growing with out); as, to blot out a sentence; to blot hard or quick. $ 7 MP Mereaina i & 3 | youth and vigor; to DeO prune: out a crime. | 3 A 3. to give forth sounds or tones by blowi 4c 3. to glow with color, health, etc. eres goe DIO Line paper, as er BADE rE E E ea Sa | fi a A É Dh A s ript. j . to eject a stream of wa i F | a bioom ne camel flow er; to give a bloom to; 4. to stain (a reputation); to tarnish; to dis- and air, as a whale of EET or other fluid | [ = Charitable affection bloomed them. grace; to disfigure; to impair; to damage. 5. to be carried about or along by the wind; | bi 7 + sr ecicer. Blot not thy innocence with soiets blood. as, the dust blows throughout August in that | bli oom, n. [AS. blõma, a lump of metal, in a de- ; nO region- flected sense from biewan, T blow.] ay to darken; to eclipse; to obscure (with p: to tal loudly or boastingly. [Colloq.] | bl 1. in metallurgy, a ry. - i J eats ) tively nore eek a TOEN han n pnd pele Sve oe erase, efface, cancel, obliter- 8: to lay eggs: z of flies, | ; Eemadali Ei econ aa . to go away; to leave. [Slang. epa daa Teoma As bis i d to make biote aspina | br A ol A E | into bars. 2. tO iffuse, as ink; as, this paper o be favorable toward and then opposed to. 1 oe à 3 blots nicely. : to blow in; (a) to squa . bac j bl rolling Or Hammering an got.. obtained by Barcoibecome:blotted: [Slang] ; (a) quander; (b) to arrive. 1 ploom/a-ry, n. same as bloomery. blot, n. [ME. blot, blotte, a blot, probably from to blow off; (a) to emit a stream of water or 7 f : Ice. blettir, a stain. steam; to let off pressu iler; | : bloom/ér, n. [named for Mrs. Amelia Bloomer, i 1 n ; t pressure, as a boiler; (b) Z Re New Work who in 1849-50 attempted to . a spot or stain: usually applied to ink. [Colloq.] to let one’s emotions or thoughts j ' introduce this type of dress for general use.] A obliteration of something written or ora bie by Uae yt long talking. | f 1. a costume for women, consisting of a ; SRE, i o blow out; (a) to burst suddenly, as a tire; | Beer ate $ z 3. a spot on the reputation; a stain; a dis- (b) in electricity, to be melted or b ; EA pending to ee sees lonse grace; a reproach; blemish. 7 i too much electric current, as a r aneen i ieuailycallarge, low hat. i , 4. a disgraceful person. i to fail, as an electrical apparatus; (c) to come | 2. a woman dressed in a bloomer costume 5. an unsightly thing, especially one out of Out suddenly or violently, as steam or air. | bl 3. a slip of the tongue; a mistake. [Slan j place; as, that building is a blot on the land- to blow over; to pass away; to cease or be | | bigom’ers. n.pl. [see bloomer, 1.] ‘1, leases isa [prob. f: D. bloot, b ked goru il asi blo clouds heye Ko | | aggy trousers worn by women or girls for Doe romeo EDATE na seca Escan Star rae | athletics: ieually they reach to the k posed.] to blow up; (a) to be disrupted byan explosion; | e EANA worn D a 1. in backgammon, (a) an exposure of an 45, 8 powder magazine blows up; (b) to arise | hi i made of silk, cotton, or wool, fitting tightly at paprorected piece KO) a gSngleimaniso ex GIRE 4 ae a tea as a Saag | i = Enea 5 oq.] to lose one’s temper. | 5 SR oe aes a cuddling 2. an unprotected point; a weak spot; a blow, oe 1. to throw or deve a current of air i bl furnace or forge in which meore s made place inviting attack; a failing. upon; also, to fan. N into wrought-iron blooms. blotch eee plorche dapa pp.; blotch- 2. to SENG by a current of air; as, the | ploom/ing, a. 1. opening i A _ ing, p$r. to disfigure with blotches; to put tempest blew the s ip ashore. ; sae = pening in blossoms; flower totes ona 5 3. to breathe upon; as, to blow the fingers I Ae ap bean beaty: „and vigor; SADE a e ots oubrokensous patch Cre ak (a wind instrument) by blow- b] ; e freshness anı i A 4 = A eee taal £ ; = eauties of youth; 2, any large, irregular blot or spot, as an 108; âs, blow the trumpet. , ; a eget cece + How ink oleh, or a paint Weich; ence a disiguee $” to make Grae ey or soothe by blowing | : ing fool. : ; as, 5 . a b ; —flourishing, fair, flowerin: = blotched, a. covered with blotches. on or toward. A i Sanne, essen eee ering, blossom- plotch/y, a.; comp. blotchier; superl. blotch- 7. to intensify (a fire) by blowing. f m’? n. in metallurgy, the process of 3 tike marked with blotches B. N93 pone | ng blooms. _2. like a blotch. . to sprea report. g S e ae appearance blote, v.t. to bloat. [Obs And EESAN ET his courtesy was lik grapes or plums, sometimes blot/less; a. having no blot. blown. : — Dryden, pe a A as on the cuctace of a blot/tér, n. 1. a piece of blotting paper; a 10. to deposit eggs on, as flies do on aee j b EE moar of removing an excess of liquid ink 11. to form by inflating, as glass ape b | dyeing, the bright appearance of rom the surface of paper by absorption. plastic state is formed into a desired shap i due to the addition of some substance 2. a book for recording events or transac- the breath, or as soap bubbles are forme ro j b the dyeing proper is completed. tions as they occur; as, a police blotter is a 12. to put out of breath from fatigues | b ing ly, adv. in a flourishing or thriving record of arrests and charges. cause to pant; as, to blow a horse. . fluid | blot-tesque’ (-tesk’), a. in painting, charac- 13. to clean or clear by forcing aif On piler ess, n. a flourishing condition; Rois y plots or heavy touches; blotchy. torough; as, to blow the nose; to blow | g state. ot-tesque’ (-tesk’), n. a bl ES: ed ane al/ly, the willow herb, Epilobium , Piece of work. ) gredor diuby 14. to destroy; to explode; usually fo Tse | b ifolium, f blot/ting, n. the making of blots; a staining or by up, down; as, the wind, blew t | lacking bloom or flowers. obliterating; also, the act of absorbing blots down; the steam blew the boiler 12: | b n oomier; superl. bloomiest, blot’ting pa’pér, a kind of thick, sof : 15. to melt (a fuse, etc). ] of bloom; flowery; flourishing with serving to absorb wet ink. ea eee 16. to spend (money) fredi ork ir of youth; as, a bloomy spray, bloomy blot/to, a. [perhaps from blot (to absorb) ] very w $ aa Ke something): [/(siang:] h i ; F c > N o away Ir ; D it í bloom, as pre plums. canals, Se because of drinking too fo blow ‘away; to dissipate; to scatter W! b : , to howl, as bl $ t aa ind; as, 18 b owl, as b. loune (r plone g E (18th c.) workman’s ae Hee off. ; (a). to remove, any x ne he t bloops. i 7 i ow off fruit, from trees; et b und produced by a Feo ee, by certain whole He part of a fuid ma pre hrough ‘under the inf oe escape from (a receptacle 5 der the influence 2. a loose outer garment extending to the an opening; e to tow i a boiler. pook ü
WEB_vol1.txt:34725:léat, ”.- (ME. clete, clyle, a wedge; from same clea) is D. kloot, a ball; G. kloss, lump, clod.]
== lekane in LKT/DEV
3006:1290.  Ar.  lakan:
3007-Auch  lakan  'Schale'  [aus  gr.  XaKÖvr) ZDMG  LI,  303],  ebenso  tk.  ;eÄ;m 'Wasch- schüssel'; hieraus  rum.  lighian  'Wasch- becken', serb.  ledjen  'Becken',  h\i]g.lihen, lejen,  klruss.  lochann,  russ.  lohan  'dass.'; öech.  lihanec  'Art  Kuchen'  [wegen  der Form].    [Mikl  SlEtWb  163  b  und  168  b.
3008-1291.  Ar.  lakk:
--
5316:;aA;aw  1290
5317-manära  1 463  a
5318-kaum  747
--
```


## [2026-09-07T01:52:51.954Z] TOOL CALL #69: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-313.json",
 "content": "{\n  \"pdf_page\": 313,\n  \"book_page\": 283,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Leup\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *lewp- / *lewb(ʰ)- 'to peel off, strip the bark from, break off, damage' (Pokorny 690–691 leup-, leub-, leubh-; Watkins/AHD leup-)\",\n      \"note\": \"Pokorny IEW 690–691 has exactly this root: 'leup- und leub(h?)- \\\"abschälen, entrinden, abbrechen, beschädigen\\\"', with the p-forms Skt. lumpáti, lopáyati, Lith. lupti, Russ. lupitь and the b-forms ON laupr, OE lēap, Goth. laufs 'leaf'. Nourai's language label (Indo-European), his headword shape 'Leup' and his gloss 'to break, peel off' are all correct, and POK:690 is the right page. Cross-cutting caveat: the root has always been hard to keep apart from the near-homophonous *Hrewp- 'to break, tear' (POK 868 reup-, Lat. rumpō); Pokorny, Walde-Pokorny and Mann keep the two apart, while Cheung (2007) assigns the Iranian 'rob' verb to a separate root *raup¹ of unclear IE pedigree. That is why the Iranian branch (nodes #1–#3) is graded 'plausible' rather than 'confirmed', while the Indic and Germanic branches are secure.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *lewp- / *lewb(ʰ)- به معنی «پوست/پوسته کندن، کندن، شکستن، آسیب رساندن» است؛ پوکورنی در فرهنگ ریشه‌شناسی هندواروپایی (ص ۶۹۰–۶۹۱) همین ریشه را با صورت leup-, leub(h)- و همین معنا آورده و شواهد آن را سنسکریت lumpáti «می‌شکند، غارت می‌کند»، لیتوانیایی lupti «پوست کندن» و گوتی laufs «برگ» می‌داند. برچسب زبانی، صورت ریشه و معنایی که نورایی داده است درست است و ارجاع او به POK:690 نیز دقیق است. تنها نکتهٔ احتیاطی این است که این ریشه با ریشهٔ نزدیک‌آوای *Hrewp- «شکستن، دریدن» (پوکورنی ص ۸۶۸، لاتینی rumpō) آمیخته می‌شود و چونگ (۲۰۰۷) فعل ایرانی «ربودن» را به ستاک جداگانهٔ *raup می‌برد؛ از این رو شاخهٔ ایرانی این نمودار با احتیاط پذیرفته شده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/loot\",\n        \"https://www.etymonline.com/word/lobby\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:690\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt (line 56281 ff.) 'Root / lemma: leup- and leub-, leubʰ- / Meaning: to peel, cut off, harm, etc. … Page(s): 690-691'; the printed German (POK_02.txt, same entry) reads 'leup- und leub(h?)- „abschälen, entrinden, abbrechen, beschädigen“'. Nourai's gloss 'to break, peel off' is a fair rendering and the page is right.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II 417–418 (incoming/WLD/WLD_Bd2_pages.txt line 27648 ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'leup- und leub(h?)- „abschälen, entrinden, abbrechen, beschädigen“ … Mit p-: Ai. lumpáti „zerbricht, beschädigt, plündert“, lopáyati „verletzt“ (= slav. lupiti, lit. laupyti), lōptra- n. „Beule“' — Pokorny's own source (he cites WP. II 417 f.).\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. leup- (AHD_watkins1985.txt line 697)\",\n          \"stance\": \"supports\",\n          \"note\": \"'leup-. To peel off, break off. 1. Germanic *laubaz in Old English lēaf, leaf: LEAF. 2. Germanic *laubja, \\\"roof made from bark,\\\" shelter … [Pok. leup- 690.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. leup- and loupos (IEC.txt lines 9745, 10110)\",\n          \"stance\": \"supports\",\n          \"note\": \"'(leup- notional e-grade of radical lup-, see also loup-. WP II, 417)'; 'loupos \\\"stripping, plunder; stripper; stripped thing, peel, leaf\\\" … Skt. lopah \\\"violence, robbery\\\"; Per. rubà- \\\"robbery\\\"; Go. lauf … OE leaf'. Mann puts both the Persian and the Germanic material under this root.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"rup,rupâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"No Avestan or Old Persian verb 'to rob' of this shape is actually attested: what Nourai's source (Abolqasemi, FFD p. 55) gives is a RECONSTRUCTED Old Iranian present stem *rup-aya-/*rup-ya- built on a nominal *raupa- 'robbing', which yields MP rōbāy- and NP robāy-/robūdan. Phonologically the step is regular: PIE *l merges with r in Indo-Iranian, so *lewp- > Proto-Iranian *raup-, zero grade *rup-, and the *-aya-/-ya- present gives *rupaya- > MP rōbāy- (intervocalic *-p- > -b-). Bartholomae's dictionary has only raopay- (a kind of dog), the royal name Urupi/Taxma Urupa and OAv. urūpaiieinti 'they cause pain' (Y 48.10); Horn himself footnotes that the Avestan form 'muss als unsicher beiseite gelassen werden'. Cheung 2007 sets up *raup¹ 'to take away, rob' with no Avestan/OP attestation at all and doubts its IE pedigree. So the derivation Nourai draws is a legitimate reconstruction, but the language label 'Avestan / Old Persian' overstates the evidence — 'Old Iranian (reconstructed)' is what the sources say.\",\n          \"derivation_fa\": \"در اوستایی و پارسی باستان هیچ فعلی به معنی «ربودن» با این صورت گواهی نشده است؛ آنچه منبع نورایی (ابوالقاسمی، مادّه‌های فعل‌های فارسی دری، ص ۵۵) می‌دهد ستاک بازسازی‌شدهٔ ایرانی باستان *rup-aya- / *rup-ya- از نام‌واژهٔ *raupa- است. تحول آوایی قاعده‌مند است: «ل» هندواروپایی در هندوایرانی به «ر» بدل می‌شود، پس *lewp- > ایرانی باستان *raup- و در درجهٔ صفر *rup-؛ سپس «پ» میان دو واکه در فارسی میانه به «ب» نرم می‌شود و *rupaya- به rōbāy- می‌رسد. بارتولومه فقط raopay- (نوعی سگ)، نام شاهی Urupi و اوستایی گاهانی urūpaiieinti «درد می‌آورند» را دارد و هرن خود در پانوشت می‌نویسد که صورت اوستایی را باید «نامطمئن» به کنار گذاشت؛ چونگ نیز ستاک *raup را بی هیچ گواه اوستایی می‌آورد. پس ادعای نورایی به عنوان بازسازی پذیرفتنی است، ولی برچسب «اوستایی/پارسی باستان» بیش از گواهی موجود است و درست‌تر آن است که «ایرانی باستان (بازسازی‌شده)» نوشته شود.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"FFD:55\",\n              \"status\": \"supports\",\n              \"note\": \"Abolqasemi p. 55 (= FFD_pages.txt pdf page 60; the book's own index at pdf p. 96 lists 'raup (ريشه - ربودن) ۵۵'), s.v. ربودن: «ربای ← فارسی میانه rwbʾy ← ایرانی باستان *rup-aya-, *rup-ya- از raupa: اسم به‌معنی «ربودن» … raupa از ریشهٔ raup به معنی «ربودن» و پسوند a ساخته شده است». The page supports the forms rup-/raupa- but labels them 'ایرانی باستان' (Old Iranian), not Avestan/Old Persian.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, Altiranisches Wörterbuch cols. s.v. raopay-, urupay-, rup- (BRT.txt lines 24960, 25526, 20781)\",\n              \"stance\": \"partial\",\n              \"note\": \"'j. raopay- m. Name einer Art des Hundegeschlechts'; 'j. urupay- m. EN. des zweiten iranischen Königs'; and Y 48.10 'karapanō urupayeintī'. Bartholomae has no Avestan verb meaning 'to rob' — only these forms, which belong with 'cause pain' / animal names.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon (KNT.txt, grep 'rup', 'raup')\",\n              \"stance\": \"silent\",\n              \"note\": \"No Old Persian entry rup-/raup- in Kent's lexicon; the Old Persian half of Nourai's label has no attestation.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007 pp. 319–320 s.v. *raup¹ (CHEUNG.txt line 20981 ff.)\",\n              \"stance\": \"partial\",\n              \"note\": \"'*raup¹ \\\"to take away, up, rob, cueillir\\\"' — lists BMP lwp /rōb/, NP rubōdan/rubāy-, Sogd. rwp, Khwar. rwby-, but NO Avestan or Old Persian form, and adds 'The initial r- of *raup should therefore be regarded secondary … As for an IE provenance …' i.e. he does not derive it from *leup-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"rôp 1; kah-rupâti\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"kah-rupâti\",\n          \"correct_form\": \"kāh-rubāy (Pahlavi khlpʾd, Horn's 'kah-rupāi')\",\n          \"derivation\": \"The first word is right: Book Pahlavi lwp = rōb 'robbery, pillage' (MacKenzie: 'rōb [lwp] robbery'; Nyberg: 'rōp [lwpʾ] pillage, plundering 108⁸'), the noun to *raup-, with Old Iranian *-p- still written p in Pahlavi orthography but pronounced b intervocalically in the derived verb rubūdan/rubāy- [lpwtn, lpʾd-]. The second word is a misprint: the Pahlavi compound is kāh-rubāy 'amber', literally 'straw-attracting' (kāh 'straw' + rubāy- 'snatching'), attested in Šāyest nē Šāyest — MacKenzie prints 'kah-rubāy [khlpʾd | N ~rubā] amber' and Tavoosi's Šāyest glossary indexes it as 'kahrubay 209/7'. Horn (no. 608) writes it 'kah-rupāi'; the printed page 283 of Nourai shows 'kah-rupâti', i.e. Nourai (or his typesetter) read Horn's final -āi as -āti. The page image confirms the JSON is a faithful copy of the book, so the error is the book's. Semantically the compound is the source of NP کهربا kahrobā and of the calque آهن‌ربا āhan-robā 'magnet'.\",\n          \"derivation_fa\": \"واژهٔ نخست درست است: در پهلوی کتابی lwp = rōb «غارت، ربایش» گواهی شده (مکنزی: rōb [lwp] «غارت»؛ نیبرگ: rōp [lwpʾ] «چپاول، غارت»)، که نام‌واژهٔ همان ستاک *raup است؛ در فعل مشتق rubūdan/rubāy- «پ» میان دو واکه به «ب» بدل شده است. واژهٔ دوم خطای چاپی است: صورت درست پهلوی kāh-rubāy «کهربا» است، تحت‌اللفظ «کاه‌رُبا» از kāh «کاه» و rubāy- «ربایَنده»، که در «شایست نه‌شایست» آمده؛ مکنزی kah-rubāy [khlpʾd] «amber» و واژه‌نامهٔ شایست نه‌شایست kahrubay ۲۰۹/۷ ثبت کرده‌اند. هرن (شمارهٔ ۶۰۸) آن را kah-rupāi نوشته و نورایی «ـāi» پایانی را «ـāti» خوانده است؛ تصویر صفحهٔ ۲۸۳ نشان می‌دهد که خطا از خودِ کتاب است، نه از استخراج داده‌ها. همین ترکیب سرچشمهٔ «کهربا» و الگوی «آهن‌ربا» در فارسی نو است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:135\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss no. 608 (printed pp. 135–136, HRN.txt leaf record 157): 'rubūden „wegnehmen, rauben“, Praes. rubāy-em … ai. √lup (älter rōp-) „zerbrechen, packen, plündern, rauben“; phlv. rōp „Raub“ (AV.-Gl.), kah-rupāi „Bernstein“ (Šāy. nāsāy. II, 115); got. biraubōn.' Exactly Nourai's two Pahlavi words — including the same odd transliteration of the amber word — so the citation is right and the misprint is inherited from Horn's final -i being read as -ti.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971 s.v. rōb, rubūdan, kah-rubāy (PHD.txt lines 559, 561, 422)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rōb [lwp] robbery'; 'rubūdan, rubāy- [lpwtn, lpʾd- | M rbwdn, rbʾy-, N ~] snatch, rob'; 'kah-rubāy [khlpʾd | N ~rubā] amber' — confirms rōb but shows the amber word is kāh-rubāy, not *kah-rupāti.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) s.v. rop; *uzruftak (NYB_vol2_glossary.txt lines 3341, 3881)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rop [lwpʾ] pillage, plundering 108⁸. — Cf NP ruftan rob- \\\"to sweep\\\".' and, s.v. *uzruftak, 'ruftak from *rup-, Skr lup- (lumpati, Lat rum[pere])' — Nyberg explicitly ties Pahlavi *rup- to Sanskrit lup-, i.e. to Nourai's root.\"\n            },\n            {\n              \"src\": \"SNS\",\n              \"where\": \"Tavoosi, Glossary of Šāyest nē Šāyest, index s.v. kahrubay (SNS.txt line 32519)\",\n              \"stance\": \"supports\",\n              \"note\": \"'kahrubay 209/7' — the very text Horn cites (Šāy. nē Šāy.) reads kahrubāy, confirming the correct Pahlavi form.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"robŭdan «ربودن (ربایدن)»; -robâ «-ربا»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP ربودن robūdan / present ربای- robāy- 'to snatch, carry off, rob' continues MP rubūdan, rubāy- [lpwtn, lpʾd-], Manichaean MP rbwdn, rbʾy- (Henning, BSOS IX/1, 87), from Old Iranian *rupaya-/*rupya- (see node #1); intervocalic *-p- has become -b-, and the past stem was remodelled analogically (Abolqasemi: the expected past would be *ruft, but robūd was formed on the pattern of the -ūd preterites). The bound form ـربا -robā is the present stem used as an agent adjective 'attracting, snatching', productive in آهن‌ربا āhan-robā 'magnet' (lit. 'iron-attracting') and کهربا kahrobā 'amber' (lit. 'straw-attracting', < Pahl. kāh-rubāy) — precisely the two examples the book prints in the box. Sense: the Iranian branch specialises 'peel/tear off' > 'snatch away, rob', whence in the compounds the weakened 'attract'.\",\n          \"derivation_fa\": \"«ربودن» با ستاک حال «ربای-» دنبالهٔ فارسی میانهٔ rubūdan / rubāy- است (در فارسی میانهٔ مانوی rbwdn، rbʾy-؛ هنینگ، BSOS جلد ۹، ص ۸۷)، و آن از ایرانی باستان *rupaya-/*rupya- می‌آید؛ «پ» میان دو واکه به «ب» بدل شده است. ابوالقاسمی یادآور می‌شود که مادهٔ ماضی قاعده‌مند باید «رُفت» می‌بود و «ربود» به قیاسِ ماضی‌های ـود ساخته شده است. صورت مقیّد «ـربا» همان ستاک حال در نقش صفت فاعلی «رباینده، جذب‌کننده» است که در «آهن‌ربا» (آهن‌رباینده) و «کهربا» (کاه‌رباینده، از پهلوی kāh-rubāy) به کار رفته — همان دو مثالی که کتاب در همین خانه آورده است. از نظر معنایی، شاخهٔ ایرانی معنی «کندن/دریدن» را به «ربودن» و در ترکیب‌ها به «جذب کردن» تخصیص داده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%A8%D9%88%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:938\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qateʿ (ed. Moʿin) printed p. 938 = BQT_v2_pages.txt leaf 398, Moʿin's footnote s.v. ربودن: «ربودن … از: ربو + دن (پیوند مصدری). هندی باستان *lup … (رُبت کردن، یغما بردن). پهلوی rōp … *rup- (شکستن، ستدن، ربودن) … بلوچی rōpag (جاروب کردن) … هوبشمان ایضاً؛ در اوراق مانوی (پهلوی) rbwdn (ربودن، غارت). Henning, A list of Middle Persian…, BSOS, IX, 1, p. 87.» Exactly the chain Old Indic lup- / Pahlavi rōp / NP ربودن that Nourai draws.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971 s.v. rubūdan (PHD.txt line 561)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rubūdan, rubāy- [lpwtn, lpʾd- | M rbwdn, rbʾy-, N ~] snatch, rob' — the MP ancestor with the same present stem.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007 p. 320 s.v. *raup¹, NWIR section\",\n              \"stance\": \"supports\",\n              \"note\": \"'NP rubodan/rubay- \\\"to rob, seize, carry off; to withdraw from sight\\\", (opp) rubōdah \\\"seized, plundered, robbed\\\", Bal. rupt/rōp- \\\"to collect\\\"' — the Persian verb and its Middle Persian base are secure even for a sceptic about the IE root.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn 1893 no. 608, p. 135 (HRN.txt line 5438)\",\n              \"stance\": \"supports\",\n              \"note\": \"'np. rubāyem geht auf älteres *rupāyati zurück' — Horn's reconstruction of the present stem, matching Abolqasemi's *rup-aya-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"lôp; lôtan\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"lôtan\",\n          \"correct_form\": \"lōtam / lōtra- (लोत्र), full form lōptra- (लोप्त्र) 'booty'\",\n          \"derivation\": \"The derivation itself is textbook: Skt. root lup- (lumpáti 'breaks, damages, plunders', causative lopáyati) with the o-grade lop-, from PIE *lewp- (Indo-Iranian *l is preserved in Vedic here); from it the instrument noun loptra- / lotra- (lup- + -tra) 'stolen goods, booty', whence Prakrit/Hindi lūṭ (see node #5). Pokorny and Walde-Pokorny cite exactly lumpáti, lopáyati and lōptra- on p. 690 / II 417. But the form printed in the box, 'lôtan', is not a Sanskrit word: Klein (Nourai's source at node #5) prints 'OI. lōtam, lōtram, \\\"booty\\\"', i.e. the accusative/neuter lōtam and the stem lōtram, and the page image shows Nourai wrote 'lôtan' with -n for Klein's -m. The printed page 283 matches the JSON, so this is the book's slip, not an extraction error; the underlying claim (Skt. 'booty' noun from lup-) is confirmed.\",\n          \"derivation_fa\": \"خودِ اشتقاق بی‌گفت‌وگو درست است: ریشهٔ سنسکریت lup- (lumpáti «می‌شکند، غارت می‌کند»، سببیِ lopáyati) با درجهٔ o یعنی lop-، بازمانده از هندواروپایی آغازین *lewp-؛ و از آن نام‌واژهٔ ابزاری loptra-/lotra- «مال ربوده، یغما» ساخته شده که خود سرچشمهٔ لوټ/lūṭ هندی است. پوکورنی (ص ۶۹۰) و والده-پوکورنی (جلد ۲، ص ۴۱۷) همین صورت‌ها را می‌آورند. اما صورتی که در کتاب چاپ شده، یعنی «lôtan»، واژهٔ سنسکریت نیست: کلاین (منبع خودِ نورایی در خانهٔ بعد) «lōtam, lōtram» می‌نویسد و نورایی «م» پایانی را «ن» خوانده است. تصویر صفحه نشان می‌دهد خطا از چاپ کتاب است، نه از خوانش اسکن؛ محتوای ادعا تأیید می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A5%8B%E0%A4%AA%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:690\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny 690 under leup-: 'Old Indic lumpáti \\\"breaks, damages, loots\\\", lopáyati \\\"injures\\\" (= Slavic lupiti, Lithuanian laupyti), lōptra- n.' (POK_full.txt line ~56313).\"\n            },\n            {\n              \"ref\": \"HRN:135\",\n              \"status\": \"supports\",\n              \"note\": \"Horn no. 608: 'ai. √lup (älter rōp-) \\\"zerbrechen, packen, plündern, rauben\\\"' — Nourai's 'lôp : to rob' is Horn's older variant rōp-/lop-.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II 417 s.v. leup-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Mit p-: Ai. lumpáti „zerbricht, beschädigt, plündert“, lopáyati „verletzt“ … lōptra- n.' — WP glosses lōptra- 'Beule', but the 'booty' sense is the standard one in Monier-Williams and Wiktionary.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict. s.v. Loot (SKT.txt line 10664)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. lotra, shorter form of loptra, booty, spoil, ← Skt. lup, to break, spoil' — confirms the noun and its derivation from lup-, and confirms that the correct form has -tr-/-tam, not -tan.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. loupos (IEC.txt line 10110)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. lopah \\\"violence, robbery\\\"' listed under the same root as Germanic *lauf- 'leaf' — the same grouping Nourai draws.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"loot\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English loot is an Anglo-Indian borrowing of the British-India period: Hindi लूट lūṭ 'plunder, booty' (already in the 1788 Indian Vocabulary, as a noun in English from 1802, as a verb from 1821), from Sanskrit lōtra-/lōptra- 'stolen goods' (see node #4); the Hindi retroflex ṭ shows the loss of the -r- of -tr- (Skeat: 'the cerebral ṭ shews that r is elided'). The route Sanskrit > Hindi > English is not in dispute; the only difference between authorities is the ultimate root: Nourai (with Pokorny and Skeat's lup-) puts it under *leup-, whereas Etymonline files it under PIE *reup- 'to snatch' (with rip, rumpō) and Klein compares Lat. lucrum. The Sanskrit evidence (lumpáti beside loptra-) favours *lewp-, so Nourai's arrow stands.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی loot وام‌واژه‌ای از دورهٔ هند بریتانیا است: از هندیِ لُوټ lūṭ «یغما، مال غارت» (نخست در واژه‌نامهٔ ۱۷۸۸، در انگلیسی از ۱۸۰۲ به‌عنوان اسم و از ۱۸۲۱ به‌عنوان فعل)، و آن از سنسکریت lōtra-/lōptra- «مال ربوده»؛ «ټ» بازپیچیدهٔ هندی نشان حذف «ر» خوشهٔ -tr- است (اسکیت). زنجیرهٔ سنسکریت ← هندی ← انگلیسی مورد اختلاف نیست و تنها اختلاف در ریشهٔ نهایی است: نورایی همراه پوکورنی آن را به *lewp- می‌برد، در حالی که Etymonline آن را زیر *reup- «ربودن» (هم‌ریشه با rip و rumpō لاتینی) می‌آورد و کلاین با lucrum لاتینی می‌سنجد. گواهی سنسکریت (lumpáti در کنار loptra-) جانب *lewp- را می‌گیرد، پس پیکان نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/loot\",\n            \"https://www.etymonline.com/word/loot\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:905\",\n              \"status\": \"partial\",\n              \"note\": \"Klein 1966 p. 905/906 (KLN_1966.txt leaf 487, which carries the printed page number 905): 'loot, n., plunder, booty. — Hind. lūt, fr. OI. lōtam, lōtram, \\\"booty\\\", which is rel. to luṇṭati, \\\"robs, plunders\\\", and prob. cogn. with L. lucrum, \\\"gain, profit, advantage\\\".' The page is exactly right for the word and the Sanskrit source, but Klein relates it to luṇṭati and lucrum rather than to *leup-, so it is only partial support for the arrow as drawn.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Loot (SKT.txt line 10664)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Loot, plunder. (Hindi. — Skt.) Hindi lūṭ (with cerebral ṭ) … ← Skt. lotra, shorter form of loptra, booty, spoil, ← Skt. lup, to break, spoil, allied to L. rumpere' — supports the chain, with the *reup-/*leup- ambiguity noted.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. leup- and the English index\",\n              \"stance\": \"silent\",\n              \"note\": \"Watkins lists only LEAF, LODGE, LOGE, LOBBY, LOFT, LIFT under leup-; LOOT does not appear in his index under this root, i.e. the AHD appendix neither supports nor contradicts the Indic branch.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A pass-through node standing for the Germanic reflexes of the b-variant of the root: Proto-Germanic *laubaz/*lauban 'leaf, foliage' (Goth. laufs, OE lēaf, OHG loub, G. Laub) and the derived *laubjō 'shelter of foliage, roof made from bark' (OHG louba, MHG loube, G. Laube). The note Nourai puts in the box — 'a group of words meaning bark peeled off trees, roofs made of bark, roof or top of a high place' — is a paraphrase of Watkins's AHD entry, which is also the reference he cites; the semantics ('what is peeled off a tree' > 'leaf' / 'bark roof') is the standard explanation, and the '(roof or) top of a high place' half covers the disputed loft/luft group.\",\n          \"derivation_fa\": \"این خانه گرهی گذری است و شاخهٔ ژرمنی صورت b-دار ریشه را نمایندگی می‌کند: ژرمنی آغازین *laubaz/*lauban «برگ، شاخ‌وبرگ» (گوتی laufs، انگلیسی باستان lēaf، آلمانی علیای باستان loub، آلمانی Laub) و مشتق آن *laubjō «سرپناهِ برگ، بامِ پوست‌درخت» (آلمانی علیای باستان louba، آلمانی Laube). توضیحی که نورایی در این خانه آورده، بازگفت مدخل واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage است — همان مرجعی که خود ارجاع داده — و معناشناسی آن («آنچه از تن درخت کنده می‌شود» ← «برگ» / «بامِ پوست») تبیین پذیرفتهٔ همگان است. بخش «بام یا بلندی» به گروه مورد تردید loft/Luft اشاره دارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. leup-: '1. Germanic *laubaz in Old English lēaf, leaf: LEAF. 2. Germanic *laubja, \\\"roof made from bark,\\\" shelter, in: a. Old French loge, lodge: LODGE, (LOGE); b. Medieval Latin lobium, lobia, laubia, monastic cloister: LOBBY. 3. Attributed by some to this root is Germanic *luftuz, sky (traditionally explained as \\\"roof of the world\\\", vault of heaven) …' — Nourai's box note is a condensation of this.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. leaf (KLN_1966.txt line 21324)\",\n              \"stance\": \"supports\",\n              \"note\": \"'leaf, n. — ME. leef, lef, fr. OE. lēaf, rel. to OS. lōf, ON. lauf … Goth. lauf, \\\"foliage\\\", laufs, \\\"leaf\\\", and cogn. with Lith. lupti, \\\"to shell, peel\\\" … All these words prob. derive fr. I.-E. base *leub(h)-, *leup-, \\\"to strip, to peel\\\".'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II 417 s.v. leup-/leub(h?)-\",\n              \"stance\": \"supports\",\n              \"note\": \"The entry opens by weighing whether German Laub belongs to the p- or the bh-variant ('aisl. laupr kann idg. b haben, wobei dt. Laub der Wzf. auf -p- zuzuteilen wäre…'), i.e. the Germanic 'leaf/basket' group is the core evidence for the root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"leaf, lodge, loft\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two of the three are secure, the third is doubted. (a) leaf < ME leef < OE lēaf < PGmc *laubaz, directly from the root — confirmed by Watkins and Klein. (b) lodge < ME loge < Old French loge 'arbour, hut' < Frankish/OHG *laubja 'shelter of foliage' — a Germanic word that re-entered English through French, hence a doublet of lobby (Klein says so explicitly). (c) loft < late OE loft < Old Norse lopt 'air, sky, upper room', with OE lyft, Du. lucht, G. Luft, Goth. luftus 'air'; Watkins flags this group as 'attributed by some to this root … but probably a separate Germanic root', and Klein files it with Luft 'air' without an IE root. So the loft link is the weak member and pulls the node down to 'plausible'.\",\n          \"derivation_fa\": \"دو واژه از سه واژه استوارند و سومی مورد تردید است. «leaf» از انگلیسی میانهٔ leef و انگلیسی باستان lēaf از ژرمنی *laubaz می‌آید و پیوند آن با ریشه مسلّم است. «lodge» از فرانسهٔ باستان loge «آلاچیق، کلبه» و آن از فرانکی/آلمانی علیای باستان *laubjā «سرپناه برگ» است، یعنی واژه‌ای ژرمنی که از راه فرانسه به انگلیسی بازگشته و دوگانهٔ lobby است (کلاین صریحاً همین را می‌گوید). اما «loft» از نورسی باستان lopt «هوا، آسمان، اتاق بالا» است و هم‌ریشه با Luft آلمانی؛ واتکینز آن را «به گمان برخی از این ریشه، ولی احتمالاً ریشه‌ای ژرمنی و جداگانه» می‌داند. پس همین حلقه سست است و حکم این خانه «با احتیاط پذیرفتنی» می‌شود.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lobby\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"(none cited)\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no refs= in the book; it inherits AHD from the Germanic parent node #6, which was checked there and supports leaf and lodge while explicitly hedging on loft.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. leaf, lodge, loft (KLN_1966.txt lines 21324, 22044, 22050)\",\n              \"stance\": \"partial\",\n              \"note\": \"'leaf … prob. derive fr. I.-E. base *leub(h)-, *leup-'; 'lodge, n. — ME. loge, logge, fr. OF. loge, \\\"arbor, hut\\\" … fr. OHG. *laubja, louba, \\\"porch\\\"'; but 'loft, n. — ME., fr. Late OE. loft, fr. ON. lopt, \\\"air, sky, upper room\\\", which is rel. to OE. lyft … Goth. luftus, \\\"air\\\"' — no IE root given for loft.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. leup-, §3\",\n              \"stance\": \"partial\",\n              \"note\": \"'Attributed by some to this root is Germanic *luftuz, sky … but probably a separate Germanic root, in: a. Old Norse lopt, air, attic, sky: LOFT; ALOFT; b. Germanic *luftjan … LIFT.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. lobby / lodge (SKT.txt lines 10068–10072)\",\n              \"stance\": \"supports\",\n              \"note\": \"'lobby, a small hall, passage. (Low L.) … cf. Ital. loggia. Low L. lobia, a gallery, O.H.G. laubâ, M.H.G. loube, an arbour' — the same Germanic *laubja for both lodge and lobby.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty pass-through node standing for Medieval Latin lobia / laubia / lobium 'covered walk in a monastery, gallery'. The form is real and well attested from the early Middle Ages, but it is not an inherited Latin descendant of the PIE root: it is a loan from Germanic (Frankish/OHG *laubja, louba 'porch, arbour'), exactly as Watkins arranges it (Germanic *laubja > Medieval Latin lobium, lobia, laubia) and as Klein and Skeat state. Classical Latin has no reflex of *leup- here (its own possible member of the family is liber < *luber 'bast, book'). So the arrow root → Latin is correct only if read as 'root → Germanic → Medieval Latin'; drawn straight from the root box it short-circuits the Germanic stage.\",\n          \"derivation_fa\": \"این خانهٔ تهی نمایندهٔ لاتینی میانه (سده‌های میانه) lobia / laubia / lobium «راهروِ سرپوشیدهٔ دیر، رَواق» است. این صورت واقعی و از آغاز سده‌های میانه پرگواه است، اما بازماندهٔ موروثیِ ریشهٔ هندواروپایی در لاتینی نیست، بلکه وام‌واژه‌ای از ژرمنی (فرانکی/آلمانی علیای باستان *laubjā، louba «رواق، آلاچیق») است؛ واتکینز، کلاین و اسکیت هر سه همین را می‌گویند. در لاتینی کلاسیک بازماندهٔ این ریشه در این معنا نیست (تنها عضو ممکن آن liber از *luber «پوستِ درون، کتاب» است). پس پیکان «ریشه ← لاتینی» تنها به معنی «ریشه ← ژرمنی ← لاتینی سده‌های میانه» درست است و در نمودار مرحلهٔ ژرمنی نادیده مانده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lobby\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"(none cited)\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs= printed on this node; the claim was checked against Watkins (AHD, cited on the sibling Germanic node), Klein and Skeat instead.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. leup-, §2b\",\n              \"stance\": \"partial\",\n              \"note\": \"'Germanic *laubja … b. Medieval Latin lobium, lobia, laubia, monastic cloister: LOBBY' — the Latin word belongs to the root, but as a borrowing from Germanic, not as a direct descendant.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. lobby (KLN_1966.txt line 22012)\",\n              \"stance\": \"partial\",\n              \"note\": \"'lobby, n., a hall; a vestibule. — ML. laubia, lobia, fr. OHG. *laubja. See lodge, which is a doublet of lobby.'\"\n            },\n            {\n              \"src\": \"LEW\",\n              \"where\": \"Walde, Lateinisches etym. Wörterbuch (LEW_1910.txt, grep lobia/laubia)\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry lobia/laubia — as expected, since it is a medieval Germanic loan and not part of the inherited Latin lexicon.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"lobby\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English lobby (1550s 'cloister, covered walk', 1590s 'entrance hall of a public building', 1630s of the House of Commons, and from the 1790s in American English the political sense 'those who seek to influence legislators', who gathered in such halls) is taken directly from Medieval Latin laubia/lobia (node #8), itself from Germanic *laubja; Italian loggia and English loge/lodge are the parallel Romance reflexes, so lobby and lodge are doublets. The edge Latin → lobby as drawn is exactly right; only the Latin word's own Germanic pedigree is left implicit.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی lobby (از دههٔ ۱۵۵۰ به معنی «رواق، راهروِ سرپوشیده»، از دههٔ ۱۵۹۰ «تالار ورودی بنای عمومی»، از دههٔ ۱۶۳۰ در مجلس عوام و از دههٔ ۱۷۹۰ در انگلیسی امریکایی در معنای سیاسی «کسانی که در تالار ورودی برای اثرگذاری بر نمایندگان گرد می‌آیند») مستقیماً از لاتینی سده‌های میانه laubia/lobia گرفته شده و آن خود از ژرمنی *laubjā است؛ loggia ایتالیایی و loge/lodge انگلیسی بازتاب‌های رومانسِ همان واژه‌اند، پس lobby و lodge دوگانه‌اند. پیکانی که نورایی از لاتینی به lobby کشیده کاملاً درست است و تنها خاستگاه ژرمنیِ خودِ واژهٔ لاتینی در نمودار ناگفته مانده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lobby\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"(none cited)\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs= on this node; verified against Etymonline, Klein and Skeat instead.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. lobby, loge, loggia (KLN_1966.txt lines 22012, 22057, 22060)\",\n              \"stance\": \"supports\",\n              \"note\": \"'lobby … ML. laubia, lobia, fr. OHG. *laubja. See lodge, which is a doublet of lobby'; 'loggia … It., fr. F. loge. See lodge, n., and cp. lobby.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. lobby (SKT.txt line 10068)\",\n              \"stance\": \"supports\",\n              \"note\": \"'lobby, a small hall, passage. (Low L.) … Low L. lobia, a gallery, O.H.G. laubâ, M.H.G. loube, an arbour.'\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"Lignu, Liginnu, Ligittu\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Akkadian lignu / liginnu / ligittu (also laganu, laḫannu) 'a jar; a grain measure'\",\n      \"note\": \"Zimmern (AKD:21–22) does list 'akk. lignu, liginnu u. ligittu ein Getreidemaß' and derives Aramaic lig(e)nā 'earthen barrel, jug' from it, and Klein independently cites 'Akkad. lignu, \\\"vase, vessel\\\"' s.v. log; so the Akkadian headword, the three variants and the gloss 'a pot for measuring wheat' are faithfully taken from Zimmern (via Moʿin's footnote in BQT:1904, which cites Zimmern by name). What is NOT secure is that this Akkadian word is the fountainhead of the whole family drawn below it. Modern scholarship separates two Aramaic words: lignā/ligettā (with g, Zimmern's Akkadian loan, whence Arabic lugnat 'plot of seed-field') and laqnā (with q) 'basin', which Klein, Lokotsch and Wiktionary all derive from Greek λεκάνη — and Greek λεκάνη is itself explained from λέκος 'dish' (+ utensil suffix -άνη), not from Semitic. So the root box is 'plausible' as an Akkadian entry but the direction of the arrows below is partly reversed (see nodes #2 and #4).\",\n      \"note_fa\": \"زیمرن در «وام‌واژه‌های اکدی» (ص ۲۱–۲۲) به‌راستی «اکدی lignu, liginnu, ligittu، پیمانه‌ای برای غله» را آورده و آرامی lig(e)nā «خمرهٔ سفالین، کوزه» را از آن گرفته است، و کلاین نیز جداگانه زیر مدخل log از «اکدی lignu «ظرف، خمره»» یاد می‌کند؛ پس سرواژهٔ اکدی، سه صورت آن و معنای «ظرفِ پیمانهٔ گندم» درست از زیمرن (به واسطهٔ حاشیهٔ معین در برهان قاطع ص ۱۹۰۴ که نام زیمرن را می‌آورد) گرفته شده است. آنچه استوار نیست این است که همین واژهٔ اکدی سرچشمهٔ همهٔ خانه‌های زیر آن باشد: پژوهش امروزی دو واژهٔ آرامی را از هم جدا می‌کند؛ lignā/ligettā (با «گ»، همان وام‌واژهٔ اکدیِ زیمرن، که عربیِ لُجنة از آن است) و laqnā (با «ق») «طشت»، که کلاین، لوکوچ و ویکی‌واژه هر سه آن را از یونانیِ λεκάνη می‌دانند؛ و λεκάνη یونانی خود از λέκος «کاسه» به‌همراه پسوند ابزارسازِ -άνη توضیح داده می‌شود، نه از سامی. بنابراین خانهٔ ریشه «با احتیاط پذیرفتنی» است، ولی جهت برخی پیکان‌های زیر آن (خانه‌های ۲ و ۴) وارونه است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%BB%CE%B5%CE%BA%CE%AC%CE%BD%CE%B7\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"AKD:21\",\n          \"status\": \"supports\",\n          \"note\": \"Zimmern, Akkadische Fremdwörter, printed pp. 21–22 (AKD.txt line 283, leaf = printed + 8): 'akk. lignu, liginnu u. ligittu ein Getreidemaß : > aram. lig(e)nā … irdenes Faß, Krug, wie auch aram. lignā, ligettā i. d. Bed. Stück Saatfeld (> arab. lugnat). — Ob hierzu auch hebr. log ein kleines Maß für Flüssigkeiten, syr. laggatā Schüssel und Maßbezeichnung, gehört, ist weniger sicher.' Nourai's three Akkadian forms and his gloss come straight from this page; note that Zimmern says nothing about Greek lekanē or Arabic laqan.\"\n        },\n        {\n          \"ref\": \"BQT:1904\",\n          \"status\": \"supports\",\n          \"note\": \"Borhan-e Qateʿ (ed. Moʿin) printed p. 1904 = vol. 3 pdf p. 701 (rendered/OCRed to data/verification/sources/refs/ocr/BQT/1904.png), footnote 6 s.v. لگن: «یونانی lekáne، عربی لقن، سریانی laqnā، کردی legen (لگن، طشتک) … ترکی «لگن» (ژابا ص ۳۸۰)؛ در آرامی «لقنا»، معرّب آن لقن (بفتح اول و دوم) و لکن … اصلاً از بابلی lignu, liginnu, ligittu (ظرف، پیمانهٔ گندم) (Zimmern, Akkad. Fremdw.)». This footnote is demonstrably Nourai's template for the whole entry.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"KLN\",\n          \"where\": \"Klein 1966 s.v. log 'a liquid measure' (KLN_1966.txt line 22051)\",\n          \"stance\": \"supports\",\n          \"note\": \"'log, n., a liquid measure, the 12th part of a hin. — Heb. logh, rel. to Syr. lagga, laggitha, \\\"a (dessert) dish\\\", and prob. also to Arab. lājja, \\\"was deep\\\", lujj, \\\"depth, abyss\\\", Akkad. lignu, \\\"vase, vessel\\\".' Independent confirmation that Akkadian lignu 'vase, vessel' is a real word.\"\n        },\n        {\n          \"src\": \"AFA\",\n          \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt, grep laqan/lakan/laqna)\",\n          \"stance\": \"silent\",\n          \"note\": \"No entry for laqan/lakan — Fraenkel does not treat this vessel name among the Aramaic loans in Arabic.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Aramaic\",\n          \"words\": \"laqna, lakan, lagînâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Nourai's box conflates two Aramaic vessel words. (a) lagînā (lig(e)nā, with g) 'earthen barrel, jug' is the form Zimmern derives from Akkadian lignu/liginnu; the -īnā ending is the ordinary Aramaic nominal suffix and the sense 'grain measure' > 'jar' is a normal metonymy, so for this word Nourai's arrow is supported by his reference. (b) laqnā (with q, Syriac lqnʾ) 'basin, tub' is the form that actually stands behind Arabic laqan and Persian lagan, and Klein, Lokotsch and Wiktionary all take it to be a borrowing of Greek λεκάνη into Aramaic in the Hellenistic period (Greek -κ- rendered by Aramaic q, -η- by -ā). Note also that the middle form Nourai lists, 'lakan', is Arabic/Turkish rather than Aramaic. So the node is half right: the g-form descends from Akkadian, the q-form is a Greek loan and does not.\",\n          \"derivation_fa\": \"نورایی در این خانه دو واژهٔ آرامی را یکی گرفته است. نخست lagīnā (یا lignā، با «گ») «خمرهٔ سفالین، کوزه» که زیمرن آن را از اکدیِ lignu/liginnu می‌گیرد؛ پسوند ـīnā پسوند معمول اسمی آرامی است و گذارِ معنایی «پیمانهٔ غله ← ظرف» گذاری عادی است، پس برای همین واژه پیکان نورایی با ارجاع خودش پشتیبانی می‌شود. دوم laqnā (با «ق»، سریانی lqnʾ) «طشت، تاس» که در حقیقت پشتوانهٔ عربیِ «لقن» و فارسیِ «لگن» است؛ کلاین، لوکوچ و ویکی‌واژه هر سه آن را وام‌گیریِ λεκάνη یونانی در دورهٔ هلنیستی می‌دانند (κ یونانی با «ق» آرامی و η با ـā بازنمایی شده). ضمناً صورت میانیِ «lakan» که نورایی آورده عربی/ترکی است نه آرامی. پس این خانه نیم‌درست است: صورت «گ»دار از اکدی است و صورت «ق»دار وام یونانی و نه بازماندهٔ اکدی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BB%CE%B5%CE%BA%CE%AC%CE%BD%CE%B7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AKD:21\",\n              \"status\": \"partial\",\n              \"note\": \"Zimmern pp. 21–22 supports 'aram. lig(e)nā … irdenes Faß, Krug' and 'aram. lignā, ligettā' from the Akkadian, i.e. Nourai's third form lagînâ; he has no laqnā with q and no lakan.\"\n            },\n            {\n              \"ref\": \"BQT:1904\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin's footnote: «در آرامی «لقنا»، معرّب آن لقن … اصلا ازبابلی lignu, liginnu, ligittu (ظرف، پیمانهٔ گندم)» — this is precisely the Aramaic → Akkadian chain Nourai reproduces (and the source of his 'laqna').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. lekane and lagena (KLN_1966.txt lines 21440, 21010)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'lekane … Gk. λεκάνη, \\\"dish, pot, pan\\\", fr. λέκος, of s.m., prob. meaning lit. \\\"something bent\\\", and cogn. with L. lanx' — Klein makes the Greek word Indo-European, so an Aramaic laqnā matching it must be the borrower, not the lender.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch 1927 no. 1290 s.v. Ar. lakan (LKT.txt line 3006)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'1290. Ar. lakan: Auch lakan \\\"Schale\\\" [aus gr. λακάνη, ZDMG LI, 303], ebenso tk. leǧen \\\"Waschschüssel\\\"; hieraus rum. lighian, serb. ledjen, bulg. lihen, russ. lohan' — Lokotsch derives the Semitic form from Greek.\"\n            },\n            {\n              \"src\": \"AFA\",\n              \"where\": \"Fraenkel, Aramäische Fremdwörter im Arabischen (grep laqan, lakan, laqna)\",\n              \"stance\": \"silent\",\n              \"note\": \"Not treated.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"laqan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic لَقَن laqan (also لَكَن lakan) 'tub, basin, wash-basin' is a real word and is indeed an Aramaic/Syriac loan, as Nourai draws: Syriac lqnʾ laqnā > Arabic laqan, with the Aramaic determinate ending dropped and the noun fitted to the faʿal pattern; the doublet with k (lakan) is the later, colloquial shape that Turkish leğen and the Balkan words reflect. What is doubtful is the further step back to Akkadian: Lokotsch (no. 1290) and Wiktionary derive the Aramaic source itself from Greek λεκάνη, so the Arabic word would be Greek > Aramaic > Arabic, not Akkadian > Aramaic > Arabic. Zimmern's Arabic reflex of the Akkadian word is a different one, lugnat 'plot of seed-field'.\",\n          \"derivation_fa\": \"عربیِ «لَقَن» (و گونهٔ «لَکَن») به معنی «طشت، تاس» واژه‌ای واقعی است و همان‌گونه که نورایی کشیده، وام‌واژه‌ای آرامی/سریانی است: سریانی laqnā ← عربی laqan، با افتادن پایانهٔ معرفهٔ آرامی و ریختن واژه در وزن «فَعَل»؛ گونهٔ «کاف»دار (لکن) صورت متأخر و گفتاری است که «لگن» ترکی و واژه‌های بالکانی بازتاب آن‌اند. آنچه مورد تردید است گام پس‌تر به اکدی است: لوکوچ (شمارهٔ ۱۲۹۰) و ویکی‌واژه خودِ صورت آرامی را از λεκάνη یونانی می‌گیرند، پس زنجیره «یونانی ← آرامی ← عربی» می‌شود، نه «اکدی ← آرامی ← عربی». بازتاب عربیِ واژهٔ اکدی در نزد زیمرن واژهٔ دیگری است: «لُجنة» به معنی «قطعه‌ای از کشتزار».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BB%CE%B5%CE%BA%CE%AC%CE%BD%CE%B7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1904\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin's footnote 6 on p. 1904 lists «عربی لقن … معرّب آن لقن (بفتح اول و دوم) و لکن (بفتح اول ودوم)» beside the Aramaic لقنا, exactly the Aramaic → Arabic step Nourai draws.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch 1927 no. 1290 (LKT.txt line 3006)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Ar. lakan \\\"Schale\\\" [aus gr. λακάνη ZDMG LI, 303]' — Arabic from Greek, not from Akkadian.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Muʿarraba (AFM_pages.txt, grep لقن / لكن)\",\n              \"stance\": \"silent\",\n              \"note\": \"Only unrelated hits (القنطرة, القناة…); Addi Shir does not list لقن as a Persian loan, consistent with a Aramaic/Greek rather than Iranian origin.\"\n            },\n            {\n              \"src\": \"AKD\",\n              \"where\": \"Zimmern pp. 21–22\",\n              \"stance\": \"partial\",\n              \"note\": \"Zimmern's Arabic descendant of akk. lignu is 'arab. lugnat' in the sense 'Stück Saatfeld', not laqan 'basin'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"lagan «لگن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP لگن lagan 'basin, tub, large rimmed vessel' (also 'pelvis' in anatomical usage, لگن خاصره) is a borrowing of Arabic لَكَن/لَقَن lakan/laqan, with the expected Persian voicing of the k of the colloquial Arabic variant to g (lakan > lagan); Moʿin's footnote in Borhan-e Qateʿ sets the Persian form in the same family as Kurdish legen and Turkish leğen, all from the same Aramaic-Arabic word. Nourai's arrow Arabic → Persian is right; the only correction is further upstream (the family's ultimate source is Greek λεκάνη rather than Akkadian, see nodes #1 and #4).\",\n          \"derivation_fa\": \"«لگن» در فارسی نو به معنی «طشت، ظرف بزرگ لبه‌دار» (و در کاربرد پزشکی «لگن خاصره») وام‌واژهٔ عربیِ «لکن/لقن» است؛ «ک» گونهٔ گفتاری عربی در فارسی به «گ» بدل شده است (lakan > lagan). معین در حاشیهٔ برهان قاطع صورت فارسی را در کنار «legen» کردی و «لگن» ترکی و همان واژهٔ آرامی-عربی می‌نشاند. پیکان «عربی ← فارسی» نورایی درست است و تنها اصلاح لازم در حلقه‌های بالاتر است: سرچشمهٔ نهایی این خانواده λεκάνη یونانی است نه اکدی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%84%DA%AF%D9%86\",\n            \"https://abadis.ir/fatofa/%D9%84%DA%AF%D9%86/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:3621\",\n              \"status\": \"partial\",\n              \"note\": \"Moʿin, Farhang-e Farsi s.v. لگن (read via abadis.ir, section فرهنگ معین): «(لَ گَ) (اِ.) ظرف بزرگ لبه دار» — the headword and gloss 'tub' are confirmed, but the lexicon entry itself gives no etymology (Moʿin's etymology for this word is the Borhan footnote, BQT:1904).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qateʿ p. 1904, Moʿin's footnote 6 (ocr/BQT/1904.png)\",\n              \"stance\": \"supports\",\n              \"note\": \"«یونانی lekáne، عربی لقن، … کردی legen (لگن، طشتک) … ترکی «لگن» … در آرامی «لقنا»، معرّب آن لقن و لکن … اصلا ازبابلی lignu…» — Moʿin puts Persian لگن in exactly this chain.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang, other entries with لگن (incoming/MON/MON_2vol_Adena_v2_djvu.txt lines 40234 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"«لگن: … تشتی فلزی که در آن دست [می‌شویند]» plus the anatomical لگن خاصره — the word and both senses are standard Persian.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rishe-ha-ye Hend-o-Orupayi (incoming/ARY/ARY_pages.txt, grep لگن)\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry — consistent with لگن being a Semitic/Greek loan rather than an Indo-European inheritance.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"lekaně\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Greek word is real — λεκάνη lekánē 'dish, pan, basin' (Attic, from the 5th c. BCE; diminutive λεκάνιον, whence ModL Lecanium, lecanomancy) — but the arrow is drawn the wrong way round. Modern scholarship analyses λεκάνη as a Greek formation from λέκος 'dish, pot' plus the utensil suffix -άνη (Wiktionary; Beekes treats λέκος as Pre-Greek, while Klein and Walde-Hofmann make it cognate with Latin lanx, lancis 'plate, dish, scale-pan', from a base meaning 'to bend'), and it is λεκάνη that was borrowed eastwards: into Aramaic/Syriac as laqnā, thence Arabic laqan/lakan, Persian lagan, Turkish leğen, Armenian, Georgian, Coptic and (via Byzantine Greek) Old East Slavic loxanja > Russian лохань. Nourai (following Moʿin's footnote, which lists the Greek form first but derives the family from Babylonian) makes the Greek word a descendant of Aramaic; no independent source consulted supports that.\",\n          \"derivation_fa\": \"واژهٔ یونانی واقعی است — λεκάνη «کاسه، تاس، طشت» در آتیک از سدهٔ پنجم پیش از میلاد، با مصغّرِ λεκάνιον — اما جهت پیکان وارونه است. پژوهش امروزی λεκάνη را ساختی یونانی از λέκος «کاسه» به‌همراه پسوند ابزارسازِ -άνη می‌داند (ویکی‌واژه؛ بیکس λέκος را پیش‌یونانی می‌شمارد، در حالی که کلاین و والده-هوفمان آن را هم‌ریشهٔ lanx لاتینی «کاسه، کفهٔ ترازو» می‌دانند)، و همین واژهٔ یونانی است که به شرق وام داده شده: به آرامی/سریانی laqnā، از آن به عربیِ لقن/لکن، سپس فارسیِ لگن، ترکیِ leğen، ارمنی، گرجی، قبطی و از راه یونانی بیزانسی به اسلاوی شرقی باستان loxanja و روسیِ лохань. نورایی به پیروی از حاشیهٔ معین (که صورت یونانی را نخست می‌آورد ولی همهٔ خانواده را از بابلی می‌گیرد) واژهٔ یونانی را برگرفته از آرامی نشان داده است؛ هیچ‌یک از منابع مستقلی که بررسی شد این را تأیید نمی‌کند. پژوهش امروزی این ادعا را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BB%CE%B5%CE%BA%CE%AC%CE%BD%CE%B7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1904\",\n              \"status\": \"partial\",\n              \"note\": \"Moʿin's footnote does open with «یونانی lekáne» and ends «اصلا ازبابلی lignu, liginnu, ligittu», so Nourai's reading of it is faithful; but Moʿin merely lists the Greek form in the family without arguing that Greek borrowed it from Aramaic, and he cites Zimmern, who does not mention Greek at all.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. lekane, Lecanium, Lecidea, balance (KLN_1966.txt lines 21440, 21363, 21369, 4306)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'lekane, n., a large dish or bowl (Greek antiq.) — Gk. λεκάνη, \\\"dish, pot, pan\\\", fr. λέκος, of s.m., prob. meaning lit. \\\"something bent\\\", and cogn. with L. lanx, gen. lancis' — an Indo-European, not Semitic, etymology (and note that Klein's separate s.v. lagena does posit a Semitic loan for λάγυνος, so his verdict here is deliberate).\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch 1927 no. 1290\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Treats Greek λακάνη/λεκάνη as the source of Arabic lakan and of the whole Balkan/Slavic group — the reverse of Nourai's arrow.\"\n            },\n            {\n              \"src\": \"AKD\",\n              \"where\": \"Zimmern pp. 21–22 s.v. lignu\",\n              \"stance\": \"silent\",\n              \"note\": \"Zimmern's entry mentions hebr. log, syr. laggatā and arab. lugnat but never Greek λεκάνη, so Nourai's own primary reference offers no support for this node.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T01:52:51.994Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-313.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T01:52:55.086Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-313.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 313"
}
```


### [2026-09-07T01:52:56.508Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 5, 'transcription_suspect': 2, 'confirmed': 5, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 8, 'partial': 4, 'not_checked': 3}
books consulted: {'partial': 7, 'silent': 7, 'supports': 17, 'contradicts': 5} | by book: {'KLN': 6, 'SKT': 4, 'AHD': 3, 'LKT': 3, 'CHEUNG': 2, 'PHD': 2, 'WLD': 2, 'AKD': 2, 'BRT': 1, 'KNT': 1, 'NYB': 1, 'SNS': 1, 'HRN': 1, 'IEC': 1, 'LEW': 1, 'AFA': 1, 'AFM': 1, 'BQT': 1, 'MON': 1, 'ARY': 1}
```


## [2026-09-07T01:53:01.705Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"lobia\\|laubia\\|lobium\" LEW_1910.txt; grep -n \"laqan\\|lakan\\|laqna\\|laqnā\" AFA.txt | head -3; grep -n \"لگن\" incoming/ARY/ARY_pages.txt | head -3; grep -ci \"rup-\\|raup\" KNT.txt"
}
```


### [2026-09-07T01:53:01.794Z] TOOL RESULT

```
0
0
```


## [2026-09-07T01:53:20.294Z] AGENT

Done — page 313 verified, `verify_check.py 313` reports 13/13 nodes and **0 PROBLEM lines**.

**Verdict counts (pdf 313 / book 283)**
- Roots: 1 confirmed (Leup), 1 plausible (Akkadian Lignu)
- Nodes: 5 confirmed, 5 plausible, 2 transcription_suspect, 1 disputed
- Nourai's own refs: 8 supports, 4 partial, 3 not_checked (the three un-referenced English/Latin nodes)

**disputed**
- Lignu #4 Greek `lekaně` — arrow reversed: λεκάνη is a Greek formation (λέκος + -άνη; Klein: cognate with Lat. *lanx*), and it is the **source** of Aram. laqnā → Ar. laqan → Pers. lagan, not a borrowing from Aramaic. Lokotsch no. 1290 and Wiktionary agree; Zimmern (Nourai's own AKD:21) never mentions Greek.

**transcription_suspect (both `error_in: "book"`, extraction is faithful — page image copied to sources/refs/ocr/BOOK/313.png)**
- Leup #2 Pahlavi `kah-rupâti` → correct `kāh-rubāy` (MacKenzie *kah-rubāy [khlpʾd]*; Šāyest glossary *kahrubay* 209/7). Nourai misread Horn's "kah-rupāi".
- Leup #4 Sanskrit `lôtan` → correct `lōtam / lōtra- (loptra-)`; Klein p.905, Nourai's own source, prints "OI. lōtam, lōtram".

**No extraction errors** — the JSON matches the printed page everywhere I checked.

Other notable findings: Leup #1 "Avestan / Old Persian rup, rupâ" is graded plausible — FFD:55 supports the forms but labels them *ایرانی باستان* (reconstructed Old Iranian); no such verb is attested in Avestan or OP (Bartholomae has only *raopay-* 'a dog', PN *Urupi*, OAv. *urūpaiieinti* 'cause pain'; Horn himself sets that aside as uncertain; Cheung's *\*raup¹* lists no Avestan and doubts the IE link). Leup #7 is plausible because Watkins/Klein detach *loft* (Gmc \*luftuz 'air'); #8 Latin is plausible because Med.Lat. *lobia/laubia* is a Germanic loan, so the root→Latin arrow skips the Germanic stage. Mo'in's BQT:938 footnote (ربودن) and BQT:1904 footnote (لگن) turn out to be the direct templates for both entries; BQT p.1904 was rendered/OCRed and cached. Eight web pages archived via fetch_source.py.
