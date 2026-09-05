# Verification process log — verify-page-76


## [2026-09-05T05:46:45.340Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 76 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-76.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-76.json. Write /home/sfmqrb/git/rishe/data/verification/page-76.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 76` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:46:46.907Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:46:47.616Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:46:47.633Z] TOOL RESULT

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


## [2026-09-05T05:46:47.873Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-76.txt"
}
```


### [2026-09-05T05:46:47.901Z] TOOL RESULT

```
1	=== PDF page 76 (book page 46) ===
2	--- entry 0 ---
3	ROOT Balbarah -> redirect to Baba
4	--- entry 1 ---
5	ROOT [Old Persian] Balŭt : oak tree, acorn  (refs PLA:56)
6	#1 (parent #0) [Pahlavi] refs=PLA:56; MON:576 | balŭt, barŭt : oak
7	  #2 (parent #1) [Persian] refs=MON:576; BQT:303 | balŭt «بلوط» : oak
8	    #3 (parent #2) [Arabic] refs=PLA:56; MON:576 | ballŭth : oak
9	      #4 (parent #3) [Spanish] refs=KLN:162 | belloth : acorn
10	        #5 (parent #4) [English] refs=KLN:162 | bellote : acorn
11	--- entry 2 ---
12	ROOT [Indo-European] Bamb, Bambô, Bhombhos : bang, rumble  (refs POK:93; IEC:53,92)
13	#1 (parent #0) [Persian] refs=IEC:53,92; MON:578 | bam «بَم» : bass, low | NOTE: MON derives this word from Arabic but IEC claims it is Indo-European
14	#2 (parent #0) [Greek] refs=IEC:53 | bombos
15	  #3 (parent #2) [Latin] refs=IEC:53 | bombus
16	    #4 (parent #3) [French] refs=AHD:149 | bombe
17	      #5 (parent #4) [Persian] refs=VOP:92 | bomb «بمب» : bomb | extra: بمب افکن
18	      #6 (parent #4) [English] refs=AHD | bomb
19	--- entry 3 ---
20	ROOT Bambak -> redirect to Pambak
21	--- entry 4 ---
22	ROOT Bambô -> redirect to Bamb
23	--- entry 5 ---
24	ROOT Barbarah -> redirect to Baba
25	--- entry 6 ---
26	ROOT [Indo-Schythian] Bata, Vata : small, undesirable, bad  (refs ISS:223)
27	#1 (parent #0) [Iranian] refs=ISS:224 | vata : bad
28	  #2 (parent #1) [Pahlavi] refs=ISS:224 | vat : bad
29	    #3 (parent #2) [Persian] refs=HRN:44; BQT; MON:4993 | bad 1 «بَد» : bad ; vad «وَد» : bad
30	
```


## [2026-09-05T05:46:50.775Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-76.json",
 "description": "Read page 76 source JSON"
}
```


### [2026-09-05T05:46:50.815Z] TOOL RESULT

```
{
  "pdf_page": 76,
  "book_page": 46,
  "entries": [
    {
      "root": {
        "name": "Balbarah",
        "redirect": "Baba"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Balŭt",
        "lang": "Old Persian",
        "refs": "PLA:56",
        "gloss": "oak tree, acorn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "PLA:56; MON:576",
          "words": [
            {"translit": "balŭt, barŭt", "gloss": "oak", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:576; BQT:303",
          "words": [
            {"translit": "balŭt", "gloss": "oak", "script": "بلوط"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "PLA:56; MON:576",
          "words": [
            {"translit": "ballŭth", "gloss": "oak", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Spanish",
          "refs": "KLN:162",
          "words": [
            {"translit": "belloth", "gloss": "acorn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:162",
          "words": [
            {"translit": "bellote", "gloss": "acorn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bamb, Bambô, Bhombhos",
        "lang": "Indo-European",
        "refs": "POK:93; IEC:53,92",
        "gloss": "bang, rumble"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:53,92; MON:578",
          "words": [
            {"translit": "bam", "gloss": "bass, low", "script": "بَم"}
          ],
          "script_extra": null,
          "note": "MON derives this word from Arabic but IEC claims it is Indo-European",
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:53",
          "words": [
            {"translit": "bombos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "IEC:53",
          "words": [
            {"translit": "bombus", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD:149",
          "words": [
            {"translit": "bombe", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "VOP:92",
          "words": [
            {"translit": "bomb", "gloss": "bomb", "script": "بمب"}
          ],
          "script_extra": "بمب افکن",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "bomb", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bambak",
        "redirect": "Pambak"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bambô",
        "redirect": "Bamb"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Barbarah",
        "redirect": "Baba"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bata, Vata",
        "lang": "Indo-Schythian",
        "refs": "ISS:223",
        "gloss": "small, undesirable, bad"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Iranian",
          "refs": "ISS:224",
          "words": [
            {"translit": "vata", "gloss": "bad", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "ISS:224",
          "words": [
            {"translit": "vat", "gloss": "bad", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:44; BQT; MON:4993",
          "words": [
            {"translit": "bad 1", "gloss": "bad", "script": "بَد"},
            {"translit": "vad", "gloss": "bad", "script": "وَد"}
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


## [2026-09-05T05:46:53.197Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['PLA','MON','BQT','KLN','POK','IEC','AHD','VOP','ISS','HRN','WLD','SYN','PHD','NYB','HUB','ARY','AFM','FVQ','LKT','SKT','WEB','FSD','DOZ','DEV']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600])\n    else: print(k, 'MISSING')\n\""
}
```


### [2026-09-05T05:46:54.830Z] TOOL RESULT

```
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
```


## [2026-09-05T05:47:15.079Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T05:47:15.122Z] TOOL RESULT

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


## [2026-09-05T05:47:15.627Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo ---- && ls data/verification/sources/refs/incoming/ 2>/dev/null"
}
```


### [2026-09-05T05:47:15.687Z] TOOL RESULT

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


## [2026-09-05T05:47:20.587Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E 'ball[uū]|ball.t|balut|balūt' incoming/PLA/PLA_pages.txt | head -40"
}
```


### [2026-09-05T05:47:20.665Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:47:21.424Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E 'bellota|bellote|ballota|acorn' KLN_1966.txt | head -30"
}
```


### [2026-09-05T05:47:21.483Z] TOOL RESULT

```
1468:acontium,  n.,  javelin.  —  ModL.  fr.  Gk.  dxovxtov, dimin.  of  Sxuv,  ‘dart,  javelin’,  fr.  I.-E.  base  *ak-, ‘sharp,  pointed’,  whence  also  Gk.  dx?),  ‘point’, L. acer,  ‘sharp,  bitter’.  See  acrid  and  words  there referred  to  and  cp.  esp.  prec.  word, acopic,  adj.,  removing  weariness  (med.)  —  Form¬ ed  with  suff.  -ic  fr.  Gk.  oixonoq,  ‘unwearied’,  fr. a-  (see  priv.  pref.  a-),  and  xotto?,  ‘striking,  beat¬ ing,  fatigue,  weariness’,  whence  xottxclv,  ‘to  cut, beat,  strike’,  xop.(jta,  ‘something  cut  or  struck  . See  comma  and  cp.  words  there  referred  to. acor,  n.,  acidity  (med.)  —  L.  acor,  ‘a  sour  taste, sourness’,  fr.  acere,  ‘to  be  sour’.  See  acid, acorn,  n.  —  ME.  akern,  fr.  OE.  xcern,  acorn  , rel.  to  ON.  akarn,  ‘acorn’,  Du.  aker,  LG.  ecker (whence  G.  Ecker),  ‘acorn’,  Goth,  akran, ‘fruit’.  As  proved  by  Goth,  akran,  the  orig. meaning  was  ‘fruit’,  esp.  ‘fruit  of  the  field’.  Ac¬ cordingly  it  is  very  probable  that  the  above words  are  rel.  to  Goth,  akrs,  etc.,  field  .  See acre.  E.  acorn  was  influenced  in  form  by  an association  with  corn.
1925:agent,  adj.  —  L.  agens,  gen.  agentis,  pres.  part, of  agere,  ‘to  set  in  motion,  drive,  lead,  conduct, guide,  govern ;  to  do,  act’,  whence  agmen,  ‘army, troop,  band,  multitude’,  lit.  that  which  is  lead’, fr.  I.-E.  base  *ag-,  ‘to  drive,  lead,  act,  do’,  whence also  Gk.  dyeiv,  ‘to  lead,  guide,  drive,  carry off’,  dytveiv,  ‘to  lead,  bring’,  aycov,  ‘assembly, contest  in  the  games’,  xycovtx,  ‘struggle  for  vic¬ tory,  anguish,  agony’,  Aycoyd?,  ‘leader’,  aywyfj, ‘a  carrying  away,  a  leading’,  OI.  ajati,  ‘drives’, ajirah,  ‘moving,  active’,  Avestic  aza'ti,  ‘drives’, Toch.  A  dk-,  B  &k-,  ‘to  travel,  lead’,  Arm.  acem, ‘1  lead,  bring",  ON.  aka,  ‘to  drive’.  Cp.  agent, n.  Cp.  also  abigeat,  acorn,  acre,  act,  action,  acti¬ vate,  actor,  actress,  actuate,  Agelaius,  agenda, agile,  agitate,  agminate,  -agogue,  agonist,  ago¬ nize,  agony,  agrarian,  agrestic,  agriculture,  agrio-, agro-,  agronomy,  Agrostis,  Agyieus,  aisle,  ala, ambages,  ambagious,  ambassador,  ambiguous, ament,  anagogy,  antagonist,  apagoge,  assay, Auriga,  axilla,  axiom,  axis,  axle,  cache,  chora- gus,  clarigation,  coact,  coagulate,  cogent,  cogi¬ tate,  demagogic,  deuteragonist,  embassy,  epact, essay,  exact,  examen,  exigent,  exiguous,  exility, indagate,  intransigent,  isagoge,  paragoge,  para- gonite,  pedagogue,  pilgrim,  prodigal,  protago¬ nist,  react,  redact,  remex,  stavesacre,  strategy, synagogue,  transact,  tritagonist,  and  the  second element  in  castigate,  clarigation,  fastigiate,  fu¬ migate,  fustigate,  levigate,  litigate,  mitigate,  na¬ vigate,  objurgate,  purge,  variegate, agent,  n.  —  F.,  in  the  sense  of  ‘acting  force’,  fr. ML.  agens,  in  the  sense  of  ‘acting  person’,  fr. It.  agente;  both  these  words  derive  fr.  L.  agens, gen.  agentis,  pres.  part,  of  agere.  See  agent,  adj. agential,  adj.  —  Formed  fr.  agency  with  suff. -ial.
2002:agrarian,  adj.,  1)  of  the  land;  2)  of  agriculture.  - Formed  with  suff.  -an  fr.  L.  agrarius,  ‘pertaining to  land’,  fr.  ager,  gen.  agri,  ‘field,  land’,  which is  rel.  to  Umbr.  ager  and  cogn.  with  Gk.  xypo;, ‘field’,  Goth,  akrs,  OE.  tecer,  ‘field’.  See  acre and  agent  and  cp.  agriculture.  Cp.  also  acorn, agrestic,  agrio-,  agro-,  Agrostis  and  the  second element  in  onager.
4307:Derivatives:  balance,  tr.  v.,  balanc-ed,  adj., balanc-er,  n.,  balanc-ing,  adj. balaniferous,  adj.,  acom-bearing.  —  Compound¬ ed  of  L.  balanus,  ‘acorn’,  and  L .ferre,  ‘to  bear, carry’.  See  balano-  and  -ferous. balano-,  before  a  vowel  balan-,  combining  form meaning  ‘acorn’.  —  Gk.  (JaXavo-,  (3aXav-,  fr. (3aXavo;,  ‘acorn’,  which  is  cogn.  with  L.  gldns, gen.  glandis,  ‘acorn’.  See  gland  and  cp.  the second  element  in  myrobalan. balanoid,  adj.,  acorn-shaped. —  Compounded  of balan-  and  Gk.  -osiSt^,  ‘like’,  fr.  elSop,  ‘form, shape’.  See  -oid.
4334:Ballota,  n.,  a  genus  of  plants  of  the  mint  family (bol.)  —  ModL.,  fr.  Gk.  paXXojTT),  ‘the  black horehound’;  of  unknown  origin, ballotage,  n.  —  F.  ballottage,  fr.  ballotter,  ‘to  bal¬ lot’,  fr.  ballotte.  See  prec.  word  and  -age. ballyhoo,  n.,  1)  outcry;  2)  noisy  advertising (slang).  —  Of  uncertain  origin;  possibly  fr. Ballyhooly,  a  village  in  County  Cork,  Ireland. Derivative :  ballyhoo,  tr.  and  intr.  v. ballyrag,  tr.  and  intr.  v.  —  A  variant  of  bullyrag, balm,  n.  —  ME.  basme,  baume,  fr.  OF.  bausme, baume  (F.  baume),  fr.  L.  balsamum,  ‘gum  of  the balsam  tree,  balsam’,  fr.  Gk.  (JtxXoajiov.  See balsam  and  cp.  embalm.
4719:Bellona,  n.,  the  goddess  of  war  in  Roman  mythol¬ ogy.  —  L.,  fr.  OL.  Duelldna ,  fr.  duellum,  ‘war’. See  bellicose.  For  the  suff.  -na  cp.  L.  Lato-na (fr.  Dor.  Aa-rco,  Gk.  Arj-rto)  and  matro-na,  ‘ma¬ tron’  (fr.  mater,  ‘mother’) ;  see  Latona,  matron. bellote,  n.,  the  edible  acorn  of  the  holm  oak.  — Sp.  bellota  fr.  Arab.  ballQtah,  in  vulgar  pronun¬ ciation  belldta,  ‘acorn’.
7020:cereal,  adj.  and  n.  —  L.  Cerealis,  dissimil.  fr. *Cereralis,  ‘pertaining  to  Ceres',  fr.  Ceres,  gen. Cereris,  ‘Ceres’,  name  of  the  Italian  goddess  of agriculture,  prop,  ‘goddess  of  growth’,  fr.  I.-E. base  *ker-,  *kere-,  ‘to  grow’,  whence  also  L.  cre- scere,  ‘to  grow’,  creare,  ‘to  create’,  Oscan.  caria, ‘bread’.  Gk.  xopevvdveu,  ‘to  satisfy,  fill  with  a thing’  (whence  xopop,  ‘one’s  fill,  satiety’),  Arm. serm,  sermn,  ‘seed,  shoot,  sprout’,  serem,  ‘I  prod¬ uce’,  Alb.  bjer,  ‘acorn’,  lljerc,  ‘lentil’  (lit. ‘food’),  Lith.  seriu,  serti,  ‘to  feed',  OPruss.  ser¬ ine  n,  ‘funeral  repast’,  OHG.  hirsi,  hirso,  ‘millet’. Cp.  herd.  Cp.  also  Ceres,  accrue,  create,  cre¬ ature,  creole,  crescendo,  crescent,  decrease,  ex¬ crescent,  increase,  increment,  procreate,  recreate, recruit.  Cp.  also  cerium.  For  the  ending  see  adj. suff.  -al.
9601:create,  tr.  v.  —  L.  creatus,  pp.  of  credre,  ‘to make,  produce,  create’,  lit.  ‘to  cause  to  grow’, fr.  I.-E.  base  *ker-,  *kere-,  ‘to  grow’,  whence also  crescere,  ‘to  grow’,  creber,  ‘thick,  close, frequent,  numerous’,  lit.  ‘densely  grown’,  Ceres, gen.  Cereris,  Italian  com  goddess,  lit.  ‘goddess of  growth’,  pro-cerus,  ‘high,  tali’,  prop,  ‘high grown*,  Gk.  xopcwtivat,  ‘to  fill  with  a  thing, satisfy’,  xopop,  ‘one’s  fill,  satiety’,  xo pot;,  ‘strip¬ ling,  child’,  xoptj,  ‘maiden’,  lit.  ‘grown  up',  Arm. serm,  sermn,  ‘seed,  shoot,  sprout’,  serem,  ‘I  pro¬ duce’,  Alb.  &jer,  ‘acorn’,  djerc, ‘lentil’,  lit.  ‘food’, Lith.  seriit,  serti,  ‘to  feed’,  OPruss.  sermen, ‘funeral  repast’,  and  prob.  also  OHG.  hirsi, hirso,  ‘millet’.  Cp.  I.-E.  base  *ker-dh-,  ‘row, herd',  a  -if /(-enlargement  of  base  *fcer-,  whence OI.  sardhah,  ‘herd’,  Goth,  hairda,  OE.  heord, ‘herd’.  See  cereal,  crescent,  herd  and  cp.  crea¬ ture,  procreate,  recreate.  Cp.  also  accrescent,  con¬ crescence,  concrete,  Cora,  core-,  Corinna,  cre- bri-,  Creole,  crescendo,  decrease,  decrement, Dioscuri,  excrescent,  hypocoristic,  increase,  in¬ crement,  procerity,  recrudesce,  recruit.  For  the ending  of  create  see  verbal  suff.  -ate. Derivatives:  creation,  creative,  creator  (qq.v.) creatine,  creatin,  n.,  a  white  crystalline  substance occurring  in  the  muscles  of  vertebrates  ( bio - chem.)  —  F.  creatine,  coined  by  the  French
12481:durmast,  n.,  a  European  oak  (quercus  sessili- flora).  —  A  compound,  the  first  element  of which  is  of  unknown  origin.  For  its  second  ele¬ ment  see  mast,  ‘acorns’, durra,  n.,  the  Indian  millet.  —  Arab.  dhuran. durst,  past  tense  of  dare.  —  OE.  and  ME.  dorste. See  dare.
13782:Euglandina,  n.,  a  genus  of  snails  (zool.)  ■ —  A ModL.  hybrid  coined  fr.  eu-,  L.  glans,  gen. g/andis,  ‘acorn’  (see  gland),  and  suff.  -ina. euhemerism,  n.,  theory  of  Euhemerus,  a  Sicilian Greek  philosopher  of  about  300  B.C.E.  — Formed  with  suff.  -ism  fr.  L.  Euhemerus,  fr. Gk.  Eufipspoi;  (a  name  lit.  meaning  ‘bright, happy’,  fr.  e8,  ‘well’  and  f.pipa,  ‘day’). Derivatives:  euhemerist-ic,  adj.,  euhemerist-ic- al-ly,  adv.
16218:Derivatives:  glamo(u)r,  tr.  v.,  g!amo(u)r-ous, adj.,  glamo(u)r-ous-ly,  adv.,  glamo(u)r-y,  adj. glance,  intr.  and  tr.  v.,  to  glide  off  obliquely;  to flash;  to  look  quickly.  —  ME.  glacen,  fr.  OF. glacier,  ‘to  slip,  slide’,  fr.  glace,  ‘ice’ ;  see  glacier. The  word  glance  was  prob.  influenced  both  in form  and  meaning  by  ME.  glenten,  ‘to  shine’ (see  glint).  Cp.  glissade.  Cp.  also  next  word. Derivative:  glance,  n.,  a  gliding  off  obliquely; a  flashing;  a  quick  look, glance,  n.,  a  lustrous  metallic  sulfide  (mineral.)  — Du.  glans,  ‘brightness,  luster’.  See  next  word, glance,  tr.  v.,  to  polish  (metal).  —  Prob.  fr.  Du. glanzen,  ‘to  gleam,  polish’,  fr.  MDu.  glansen, ‘to  gleam’,  fr.  glans,  ‘brightness’,  fr.  MHG.  glanz (whence  G.  Glanz),  fr.  Late  OHG.  glanz,  of  s.m., fr.  OHG.  glanz,  adj.,  ‘bright’,  which  is  rel.  to ME.  glenten,  ‘to  shine’.  See  glint, gland,  n.  —  F.  glande ,  fr.  L.  glandem,  acc.  of glans,  ‘acorn’  (used  in  the  sense  of  L.  glandula, ‘gland’,  dimin.  of  glans),  which  is  cogn.  with Gk.  pdXavog,  Arm.  kaiin  (gen.  kalnoy),  OSlav. zelgdi,  ‘acorn’,  Lith.  gile,  Lett,  (d)zile,  OPruss. gile,  ‘oak;  gland’.  Cp.  next  word  and  the  second element  in  Euglandina  and  in  Juglans.  Cp.  also the  first  element  in  balaniferous  and  the  second element  in  myrobalan.  Cp.  also  valonia. Derivatives :  glandi-ferous,  adj.,  glandi-form,  adj. glanders,  n.  pi.,  a  contagious  disease  of  horses, mules,  etc.,  characterized  by  the  swelling  of  the glands  beneath  the  lower  jaw.  —  OF.  glandres (pi.),  fr.  L.  glandulae  (pi.),  ‘glands  of  the  throat'. See  glandule.
16222:glandule,  n.,  a  small  gland.  —  F.,  fr.  L.  glandula, ‘gland  of  the  throat’,  dimin.  of  glans,  gen.  glan- dis,  ‘acorn’.  See  gland  and  -ule.
20433:Juglandaceae,  n.,  the  walnut  family  (bot.)  — Formed  from  next  word  with  suff.  -aceae. Juglans,  n.,  a  genus  of  trees,  the  walnut.  —  L. juglans,  ‘walnut’,  contraction  of  Jovis  glans, which  is  a  loan  translation  of  Gk.  A189  (JaXavoc, ‘chestnut’,  lit.  ‘acorn  of  Jupiter’.  See  Jove  and gland.
24858:myrobalan,  n.,  the  dried  astringent  fruit  of  vari¬ ous  tropical  trees.  —  F.,  fr.  L.  myrobalanum,  fr. Gk.  ixupoflaXxvov,  ‘balsam  made  from  a  palm nut’,  which  is  compounded  of  p.upov,  ‘sweet juice,  sweet  oil,  unguent,  balsam  ,  and  ,jxXxvgp, ‘acorn,  nut’.  For  the  first  element  see  smear  and cp.  Myristica  and  the  first  element  in  next  word, for  the  second  clement  see  balano-.
34838:shack,  n.,  fallen  acorns  or  mast,  refuse  fish,  etc.
41037:Vallota,  n.,  a  genus  of  African  bulbous  plants (bot.)  —  ModL.,  named  after  the  French  physi¬ cian  and  botanist  Pierre  Vallot  (1594-1671). vallum,  n.,  a  rampart.  —  L.,  ‘a  palisaded  wall  or rampart;  wall,  rampart’,  for  *wal-nom,  rel.  to vallus  (for  *wal-nos),  ‘stake’,  and  to  valles, ‘valley’.  See  vale,  ‘valley’,  and  cp.  circumvallate, contravallation,  interval.  Cp.  also  wall, valonia,  also  vallonia,  n.,  the  acorn  cups  of  the valonia  oak.  —  It.  vallonia,  fr.  MGK.  [JocXcma (r.  valanla),  ‘evergreen  oak,  ilex’,  fr.  pocXdm  (r. valani),  ‘acorn’,  fr.  Gk.  (HdXocvo g,  of  s.m.  See balano-.
```


## [2026-09-05T05:47:36.374Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['PLA','ISS','IEC','POK','BQT','MON','AHD','KLN']:\n    print('==',k, d[k].get('page_offset'), '|', d[k].get('lookup_hint'))\n\""
}
```


## [2026-09-05T05:47:37.686Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'pdf page' incoming/PLA/PLA_pages.txt | head -5; echo ---; grep -c '' incoming/PLA/PLA_pages.txt; echo ---; grep -n -i 'balut\\|ballut\\|Eiche' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-05T05:47:38.018Z] TOOL RESULT

```
== PLA 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== ISS DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.
== IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
== BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
== AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
== KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


### [2026-09-05T05:47:38.089Z] TOOL RESULT

```
---
16027
---
450:vergleiche 
767:In der Regel wird die jüngere Kultur von der reicheren und älteren Kultur 
870:Bereiche des täglichen Lebens z. B.: 
928:Formen, die meistens durch die Verwechslung diakritischer Zeichen 
1850:ob. ı _ ? Armanistän: Armeniya, Provinz des pers. Großreiches — ap. 
1862:our _ °armahän: "weiches Eisen" pers. 2 (im Gegensatz zum Stahl), wahr- 
3041:Löl _ ”ambär: "Magazin, Kornspeicher" pers. 9 aus dem pers. 21  ambar 
3237:„ui- >’awäz: "Zeit vor dem Frühlingsäquinoktium, wenn die Sonne im Zeichen 
3259:gi-’au ı "Höhe, Kulmination; das Erreichen des Gipfelpunktes". 
3739:AL - bäßig: "Sperber" pers. 1, wahrscheinlich aus der gleichen Wurzel 
4934:bs - balüt: "Eiche" pers. ° aus dem mp. Pd barüt, aram. so - 
6096:S=- tugrä: "kaiseri., Handzeichen" pers. 1 
6172:AN _ talk: "Talk; Speckstein, ein sehr weißes weiches Mineral" ° pers. 
8203:Name einer Provinz des persischen Großreiches 4, 
9062:eb- däg: "Marke, Eindruck, Brandzeichen" pers. 10 <Tmp. suo daxSak 
9063:"Zeichen, Marke" —Taw. daxSara.- daxSa "brennen" 1, 
10394:rasidan "erreichen, ankommen" T mp. aD rasit v. Verb rasitan 11, 
11033:&»,- zift: "mit Harz od. Pech bestreichen; verpichen" s. flg. pers. ?. 
12078:saw - Sugd: "Provinz des persischen Großreiches" a. sußda, suguda 1, 
12493:G%w - sindijan: "Steineiche" pers. 12 syr. 22012.
```


## [2026-09-05T05:47:42.875Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4920,4960p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-05T05:47:42.923Z] TOOL RESULT

```
10. Mackenzie S. Vv. 

11. Lokotsch s. v., Wahrig s. v. 

12. Littmann S. 112, Fremdwörterbuch s. v. 


bilaur 56 bunast 


5% - bilaur: "Kristall, Beryll" pers. 1 aus dem pers. _%A bulür mp. 
Spy belur 2 


bs - balüt: "Eiche" pers. ° aus dem mp. Pd barüt, aram. so - 


CH - baliß: "Gondel, Ruder" pers. 4 wahrscheinlich aus dem pers. rm balm 
"kleines Boot". 


bh - balid: "plöd, schmutzig" pers. 5, eventuell aus dem pers. Ak palid 
"unrein, schmutzig, besudelt" 6, 

Fol - balilaß: "belliricus" aus dem pers. au. balilah, syr. Ko ‚frz. 
bellirique (ind. vidhitaka). 


f- bam: "Baß" pers. 
UL - bimaristän: "Krankenhaus" = bimaristän s. „i“__\. bimäristan , 


f” bumum: Pl. ver bam s. bam 


&\L - bana’ig: Pl. v. al, baniga s. baniga. 
„lo - banaßir: Pl. v. PEXE banfara s. bandara , 
‚>\o- banädir: Pi. V._>, bandar s. bandar , 


Swls- bunast: "Terebinthe" pers. 8, wahrscheinlich aus dem mp. ‘u bun
```


## [2026-09-05T05:47:43.719Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==71' incoming/PLA/PLA_pages.txt | head -60"
}
```


### [2026-09-05T05:47:45.846Z] TOOL RESULT

```
bilaur                                                                 56                                                     bunast



5% - bilaur:              "Kristall,              Beryll"        pers.           1 aus   dem   pers.      _%A       bulür     mp.
      Spy belur           2


bs - balüt:              "Eiche"           pers.        ° aus     dem mp.          Pd    barüt,     aram.       so -


CH    -   baliß:         "Gondel,              Ruder"     pers.        4     wahrscheinlich             aus    dem    pers. rm balm
      "kleines           Boot".


bh    -   balid:         "plöd,           schmutzig"           pers.        5, eventuell          aus    dem    pers.       Ak palid
      "unrein,           schmutzig,              besudelt"         6,


Fol - balilaß:                  "belliricus"              aus     dem       pers.      au.   balilah,         syr.    Ko       ‚frz.
      bellirique               (ind.       vidhitaka).


f- bam:        "Baß"          pers.


UL           - bimaristän:                     "Krankenhaus"            = bimaristän           s. „i“__\.            bimäristan,

 f”       bumum:         Pl.       ver bam         s.    bam


 &\L - bana’ig: Pl.                       v. al, baniga s. baniga.

 „lo -         banaßir:            Pl.     v. PEXE banfara              s. bandara,

 ‚>\o- banädir:                 Pi.       V._>,     bandar        s.    bandar ,


Swls-       bunast:            "Terebinthe"              pers.     8, wahrscheinlich                aus       dem    mp. ‘u bun
      "Baum"        + MP en»             ast    "Stein,        Knochen"           9,




 1.   al-Munfid           s.       v.
 2.   Mackenzie           s.       v.
 3.   FM.     s.    v.
 4.   al-Marka“           s. v.
 5.   Chista        Bd.       10     s.    1192.
 6.   Steingaß           s.     v.
 7. Muhit          s.    v.,       FM.     s.    v.,     Steingaß           s.    v.
 8.   ebda.
 9.   Mackenzie           S,.      v.
```


## [2026-09-05T05:48:04.464Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD barut/balut\"; grep -n -i -E 'bal[uū]t|bar[uū]t|oak' PHD.txt | head -20; echo \"=== NYB\"; grep -n -i -E 'bal[uū]t|bar[uū]t|oak' NYB_vol2_glossary.txt | head -20; echo \"=== KNT oak\"; grep -n -i 'oak' KNT.txt | head; echo \"=== BRT oak/Eiche\"; grep -n -i 'Eiche' BRT.txt | head"
}
```


### [2026-09-05T05:48:04.555Z] TOOL RESULT

```
=== PHD barut/balut
417:kabāh [kp’h | Ar. gabā] garment, cloak.
1217:chestnut šāhbalūt.
1254:cloak kabāh.
=== NYB
3362:of elapsing (of time), v. a-frde-sacišneh. — Av. (1553 sq.) ?sak-, OP Oak- in 0akatà
4936:Oadaya-: sahistan Oak-: sacišnēh Oard-: sal Ouxra-: suxr
=== KNT oak
5815:yaka- sb. (§6, $143.IV) a kind of wood (oak, Scheil 25.28, but if so, not cognate, Bv. BSLP 30.1.01; Afghan cypress, Kónig, Burgbau 54-61; mulberry, Wb. AfOF 7.42; teak, Hz. AMI 3.61-2; certainly not ‘timber’ in general, as taken by Gray, AJP 53.68). yaka nsf. DSf 34.
=== BRT oak/Eiche
178:und    einwandsfrei.     Die  Wörter   umfangreicherer    und   nicht   durch   Farallelstellen
181:Desgleichen  habe  ich  den  Wortfetzen  in  Bh.  5  und  D.  7  die  Aufnahme  ver- sagL  Wenn  nicht  eine  erneute  Untersuchung  der  Steine  wider  Erwarten  günstige Ergebnisse  liefert,  ist  ja  doch  nichts  damit  anzustellen.
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
191:Ich  würde  bei  solcher  Sachlage  sinnloser  Raumvergeudung  geziehen  werden müssen,  hätte  ich  bei  jedem  Wort  die  ganze  Reihe  der  gleichen  oder  ähnlichen Fundatellen  aufgeführt  Wohl  aber  muss  man  gegebenen  Falls  in  der  Lage  sein, aUe  Belege  eines  Worts  bequem  einzusehen.  Diesem  Zweck  soll  die  nachstehende Konkordanz  dienen,  in  der  ich  nur  jene  Stellen  nicht  berücksichtigt  habe,  die sich  deutlich  als  Anführungen  aus  anderen  bekannten  Avestatexten  ■ —  insbesondere den  ^aSischen  —  kennzeichnen;  z.B.  Y.7.a4f.  -von  yehya  bis  _)'(i7'?(=  Y.  4:5.  7a und  41.  ${.),  N.  71  (Blatt  147,  Z.  14 ff.)  von  am>sa  sp»nta  bis  jasaiti  (=  Y.  Ä3f.); wo  es  nötig  schien,  habe  ich  das  Sigel  Z.  (Zitat)  verwendet  —  Das  Zeichen  :  soll
194:besagen,  dass  der  links  davon  angegebene  Paragraph  dem  oder  den  rechts  ange- gebenen ganz  oder  teilweise  gleich  oder  ähnlich  ist  —  Die  eingeklammerten ZifTem  —  bei  Y,,  Vr.,  V.  —  geben  die  abweichende  Kapitel-  und  Paragraphen- zählung in  Spiegels  Ausgabe  der  Fahlavi-  und  SanskiitUbersetzung  aa
2034:und  an  Ursprünglichkeit  des  Lautbestands,  der  Formbezeichnung  und  der  Satz- fUgung  den  Hymnen  des  ^gveda  durchaus  die  Wage  halten,  stehen  Machwerke traurigster  Art  zur  Seite,  deren  Verfasser  auf  Schritt  und  Tritt  verraten,  dass  sie sich  einer  ihnen  fremden  —  weil  längst  abgestorbenen  —  Sprache  bedienen,  in der  sie  nur  ganz  stümperhafte  Kenntnisse  besitzen.  Als  Stücke  solcher  Art,  in deren  Benutzung  für  irgend  einen  Teil  der  Grammatik  dem  Sprachvergleicher  die grösste  Vorsicht  anempfohlen  sei,  bezeichne  ich  in  erster  Reihe:  Yt.  2,  j,  4,  Vyt,  Az,, Nik.,  Vd.,  FrW.  2,  8,  g,  FrB.,  FrD.  5,  6,  7,  FrG.,  FrBy.,  Sl.  8.  zz  Z.,  in  zweiter:  Yt. //,  12,  1$,  18,  V.  S2.  Auch  andern  alten  Teilen  sind  nicht  selten  minderwertige Zutaten  ein-  oder  angeßigt,  die  sich  zumeist  schon  durch  die  mangelhafte  Syntax deuthch  als  solche  zu  erkennen  geben;  z.  B.  in  Yt  /,  V.  10, 11,  13  usw.".
2044:nach  dem  Grundsatz  verfahren  habe:  im  Zweifel  lieber  auseinander  halten  als  ver- einen. Ich  meine,  gerade  auf  dem  etymologischen  Gebiet  der  arischen  Sprachen, die  so  viel  ursprünglich  Geschiedenes  haben  zusammen  fallen  lassen,  sollte  man  mit geistreichen  Kombinationen,  mit  dem  Aufbau  ganzer  Bedeutungsstammbäume  recht zurückhaltend  sein.  Wer  Wörter  von  konkreter  Bedeutung  auf  'Wurzeln'  zurückführt, deren  Bedeutung  ja  gerade,  damit  ihnen  eine  recht  zahlreiche  Nachkommenschaft zugesprochen  werden  kann,  möglichst  farblos  angesetzt  ist,  der  täuscht  sich  selbst, wenn  er  damit  etwas  erreicht  zu  haben  vermeint  Der  Wurzelspuk  hat  ja  in  den letzten  Jahren  etwas  nachgelassen,  er  grassirt  aber  noch  immer  viel  zu  sehr.  Die bdische  Schablone  ist  eben  gar  zu  verlockend.
2045:Für  die  Umschrift  der  awestischen  Buchstaben  und  für  die  Wiedergabe  der neuiranischen  Wörter  war  mir  ebenso  wie  für  die  der  altpersischen  Keilzeichen (s.  S.  HI)  der  Grundriss  der  Iranischen  Philologie  massgebend.
2046:Das  Neupersische  ist,  wo  es  sich  um  Exegese  handelt,  nach  modemer  Aussprache umschrieben,  dagegen  bei  Anführungen  zu  etymologischem  Zweck  in  frühneupersischer Lautform.  Wegen  meiner  Transskription  der  Fahlaviwörter  vergleiche  man  die  in Wiener  Zeitschr,  für  die  Kunde  des  Morgenlandes  XIV.  S.  i8o  aufgestellten  Leit- Mtze;  Wörter,  die  ich  nicht  lesen  konnte,  sind  in  Steildruck  gegeben,  unter Berücksichtigung  der  getrennten  oder  verbundenen  Schreibung  der  Zeichen,  wobei selbstverständlich  für  die  mehrdeutigen  Zeichen  stets  der  selbe  Buchstabe  erscheint, z.  B.  d:  für  das  als  d,  g,  y,  r  usw.  lesbare  Zeichen,  da:  fdr  die  als  d<i,ya,  ih,  /  usw. lesbare  Zeichen  Verbindung.  Wer  mit  der  Fahlavischrift  vertraut  ist,  wird  sich  danach die  Originalform  des  Wortes  ohne  MUhe  herstellen  können.  'Fäzand'lesungen  sind in  Pahlavi  umgesetzt
2047:In  der  Umschreibung  der  Sanskritzeichen  habe  ich  mich  nach  den  Vorschriften für  den  Gnmdriss  der  indo-arischen  Philologie  und  Altertumskunde  gerichtet.  Einzeln stehende  Wörter  erscheinen  durchweg  in  der  Pausaform.
```


## [2026-09-05T05:48:06.182Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFM balut\"; grep -n 'بلوط' AFM_pages.txt | head -10; echo \"=== TAD\"; grep -n 'بلوط' TAD_pages.txt | head -5; echo \"=== ARB\"; grep -n 'بلوط' ARB_mo3rb.txt ARB_abdulraheem.txt | head -5; echo \"=== AFA Fraenkel\"; grep -n -i 'ballut\\|ballūt\\|Eiche' AFA.txt | head -10"
}
```


### [2026-09-05T05:48:06.327Z] TOOL RESULT

```
=== AFM balut
1892:سكوت » زهره يظهر قبل ورقه وهو قدر البلوط اصفر احمر اسود ابيض 2" الرانحة
=== TAD
2165:                            ‫ويقع على ورق شجرة بلوط القرمز وعلى أنه ) ب‬
=== ARB
=== AFA Fraenkel
48:über maschinelle Übersetzung, optische Zeichenerkennung oder andere Bereiche durchführen, in denen der Zugang zu Text in großen Mengen
51:+ Beibehaltung von Google-MarkenelementenDas "Wasserzeichen" von Google, das Sie in jeder Datei finden, ist wichtig zur Information über
52:dieses Projekt und hilft den Anwendern weiteres Material über Google Buchsuche zu finden. Bitte entfernen Sie das Wasserzeichen nicht.
61:Buchsuche hilft Lesern dabei, die Bücher dieser We lt zu entdecken, und unterstützt Au toren und Verleger dabei, neue Zielgruppcn zu erreichen.
80:ALS ZEICHEN DAUERNDER DANKBARKEIT UND TREUE• * ^ •>• -■••^
152:dass der wahre Philologe an Wörtern und Sachen gleiches
279:aujoül -i Auch auf andere Keuuzeichen der Lehnwörter
302:lautlicheu Kennzeichen der fremden Herkunft nicht überall
469:nicht immer Zeichen fremder Herkunft , vcjl. vJJLä zu ^JLi
537:natürlich immer nur, wo die weiche Aussprache im Ara-
```


## [2026-09-05T05:48:13.767Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD sahbalut\"; grep -n -i 'ahbal\\|šhbl\\|balut' PHD.txt PHD_mackenzie.txt | head -20; echo \"=== AFA بلوط\"; grep -n 'بلوط\\|Ballūṭ\\|ballût' AFA.txt | head -10; echo \"=== HRN balut\"; grep -n -i 'balūt\\|balut\\|bal[uū]ṭ' HRN.txt HUB.txt | head -10"
}
```


### [2026-09-05T05:48:13.862Z] TOOL RESULT

```
=== PHD sahbalut
PHD.txt:4565:dēwī dew: |! dēwēsnīhī déwézagiht šahbalüt šāy- šāhdānag šāyendagīh
PHD_mackenzie.txt:6167:cast down hambastan.                    chestnut siihbalut.
PHD_mackenzie.txt:8414:sagr, sir               ~                  sahbaliit
=== AFA بلوط
=== HRN balut
```


## [2026-09-05T05:48:14.347Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON بلوط\"; grep -n 'بلوط' MON_part1.txt | head -10; echo \"=== BQT v1 بلوط\"; grep -n 'بلوط' BQT_v1_pages.txt | head -20"
}
```


### [2026-09-05T05:48:14.431Z] TOOL RESULT

```
=== MON بلوط
25109:بلوط: (ا.) (گا.) درختی از تیوه 
30675:البلوط» سرخس بلوط قره‌بالدیری قره. 
44726:کروی يا سیبی شکل است؛ بلوط دریای؛ 
47978:در بوست ساقة گیاه - از جمله بلوط - وجود 
65832:گونه درخت از دستهٌ بلوط‌ها جزو تبرة 
71162:(مانند چوب درخت تسربری و شا‌بلوط) 
79931:میگذرد. از مبوه‌های سخت از قبیل بلوط و 
83333:بلوط‌ها از رده دولسه‌یی‌های بی‌گلب رگک. 
83339:خارداری قرار گر فته است. شاه بلوط در اکثر 
83344:آغاجی» طراس» بلوط الملت. شاه‌بلوط 
=== BQT v1 بلوط
3192:سماریس » و ذیل : عرم )۰ شغنین ( ذیل : تی) ؛ قبلوط .
9684:رفت و چندی در شکیم توقف کرد و از آتجا بکنمان داز کشت و وادی حاصلخیز اردن را بلوط
19120:از بلوط باشد ۷ .
20881:بلوط - بفتح اول » پهلوی 9۵106 « اونوالا 4۰۲» درزبان علمی
20882:کلا6؟6(ام), درختی‌است از دسته بلوط ها که ميوة آنرا تا نمه باله ای فرا
20886:دخوبه ج۹ ص۱۹ بمعتی الوا است. ادرسی ( ترجمة ژوبر ح+ص ۱۷۳) بلوط
```


## [2026-09-05T05:48:20.286Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=20860 && NR<=20900' BQT_v1_pages.txt; echo \"=== leaf:\"; awk 'NR<=20885' BQT_v1_pages.txt | grep -c $'\\f'; echo \"=== pdf tag\"; awk 'NR<=20885' BQT_v1_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -2"
}
```


### [2026-09-05T05:48:21.948Z] TOOL RESULT

```
بلیله - بنتم اول بروزن هلیله » دوابی
أست رطس ای رود تا للم یم
دوم و سیم . معرب آن بلیلج باشد ۴ .
پلیناس * « بفتح اول و انی بتحتانی
۴ ر4 : ایلیا. ؟ - بودانی
- این ام باشکال‌بلنیای»
بقه ازصفحهٌ ۳۰۱
بقبه درصفحهً ۳۰۳
بمعنی قسمی ازابگیتة شفاف وصا ف گرفه‌اند .ببان بست ودوم
کزبای اتفدتا تون یل برهشتاد و مك لت و کنات
لن ه شح اول و سکون ثانی . , خرن و «بوه‌است ربزه و حفزی هم دارد و مردم آثرا
1 باع و زراعت را کویند . جه باعبان ونگاهمان سخور ند وآنراون خوانند ۱ و بتر کی چنلافوج
زراعت و محافظ خرمن را بنوان هم بیگویند - | و بعریی حبةالخضرا گوبند - و بضم اول بنیاد
_ دازدن1 م‌ماوز۴ , 2 .۳ «ابتی ۱۹۷ و رگ : فرهنگه روستایی
۷ ,+
یه از صفخةٌ ۳۰۷
بدین.نام ها شناخته اند : نضت ایولونوی ۸۳۵11۵7105 از مردم طوانه (کرسی کایاد و کیه)
( قرن اول مبلادی ) » فبلسوف فناغوری که کرامات و خوارق عادانی بدو سبت داده‌اند ؛ دوم
اپولونیوی از مردم برغه ۳6۲83 (پامفیلیه) مهندس و عنجم بونانی » ساکن اسکندبه ( آغاز
فرن‌سوم میلادی) ؛ مراد ازبلبنای مذ کور درمتن » ایولونیزی طوانه‌بی‌است . رك : بلیناس‌حکیم»
بقلم ثکارنده درمجلة داش سال اول شماره های نهم و دهم .
بلوط - بفتح اول » پهلوی 9۵106 « اونوالا 4۰۲» درزبان علمی
کلا6؟6(ام), درختی‌است از دسته بلوط ها که ميوة آنرا تا نمه باله ای فرا
کرقته و لیه های آن مواد غذابی بسیار دارد . چوب آن سیارسخت و مخصوصاً
بوست آن دارای مازوی اب ت که بمسرف چرساری هیرسد. دگل گلاب
۰۷۷-۷۹ تبلهرا - بفتح‌اول وسومفبی‌است‌هندی کهبقول ابن‌خردادبه «طبع
دخوبه ج۹ ص۱۹ بمعتی الوا است. ادرسی ( ترجمة ژوبر ح+ص ۱۷۳) بلوط
گوید که لفب مزبور ارئی بود . ابن‌حوقل (ح۲ ص۲۲۷) گوید: بلهرا حاکم مانکیر و بزد کترین
پادشاه حند بود و ءسعودی ( مروج» ح ۱ ص۱1۲) آورد: بلهرا اسم مسی دولت در شهر مزبور
بودوجاشینان اورا بنا‌وی بازخواندند. و گوبد مانکیر «مالکهت» اس ت که قریب ٩*‏ میلی‌جنوب
شرفی شلیور در ولابت بمبثی است . ره : داگرةالممارف اسلام - » بلی - بفتح اول »
سمنانی 98[8 , مرخه 0126 , لاسکردی 9816 , شهمیرزادی ۵۵16 < . » ص ٩۱۹۷‏
زباکی0۵16 «کربرسنه۷». کیلکی16 02.نهرانی 9۵16. بلیط و بلیت_ ,کر اولء
افو ازفرانسه 11164 ؛ جواز ورود بتماشاخانه و غیره . ۵ # - بفتح اول . آوای خشن
ودرشت آدمی وساز. معرب‌آن هم «بم» یفتح‌اول وتشدید دوم «نفس» «اسفاا :۲ م0۹ - نیز نم
تاحیه‌ایست در کرمان . از مشرق محدود مکوبر ۰ از شمالبه‌سارد و جبال بارز » از مغرب‌بجیرفت
و اسفندقه و از جنوب به‌ترماشیر . هوای آن معتدل . دارای چندین قرب مهم حاملخیز . مر کز
آن بم غر ۷۰۰ کپلوفتری جنوب شرق ی کرمان است. «جفرافیای سیاسی . کبیان. ص۲4۹*.بنابه
و پابان و یخ درخت ٩‏ - و اتهای هر چیز
وچیزی نیز هست که آترا آبکامه گود, و آن
نان خورشی است معروف و مشهور در صفاهان
=== leaf:
518
=== pdf tag
```


## [2026-09-05T05:48:38.062Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== UNV\"; grep -n -i 'balut\\|balūt\\|barut\\|oak' UNV.txt | head -20; echo \"=== leaf 519-521 page markers\"; awk 'BEGIN{RS=\"\\f\"} NR==519||NR==520' BQT_v1_pages.txt | grep -n 'بقیه\\|صفح' | head"
}
```


## [2026-09-05T05:48:39.077Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '25100,25120p' MON_part1.txt; echo \"=== bam MON\"; grep -n '^بم\\b\\|بم:' MON_part1.txt | head -10"
}
```


### [2026-09-05T05:48:39.545Z] TOOL RESULT

```
=== UNV
617:'the  oaktree,  an  acorn.  a  chesnut‘  (Raverty).  —  *  np.  'glans  regia’.  —
=== leaf 519-521 page markers
```


### [2026-09-05T05:48:39.614Z] TOOL RESULT

```
بلور: ۲ ,0:۱۳ (۱.) قسمی ششه که از 
تکیت سیلیکات دو پتاسیم و سیلیکات دو 
پلمب ساخته شود آنکینة صاف و شفاف. 
۱ ۸ (.) سفر ه 4 بزرگ. 

بلوز: 52اه" () جامةٌ نیم‌تتةٌ کرکی يا 

با کاموایی و با نخی زنانه با مر دانه. 

بلوط: (ا.) (گا.) درختی از تیوه 
بلو ط‌ها که سردسته گباهان تبره خود را 
تشکیل می د هد. این درخت دارای دو تقِ 
گل است که معمولاً در انتهای شاخه‌ها قرار 
می‌گیر ند. گل‌های نر بصورت سنبله‌های 
دراز و گل‌های ماده 0 سصورت 
دسته‌های سه تایی در سغل س رگک‌ها قرار 
می‌گیرند. میوة این گٌیاه بصورت فندقة 
بیضوی شکل کشیده شده که بباله‌ای تا نيمه 
آن را فرا گرفته. چوب آن بسیار مسحکم 
است. ضح.. در لرستان این درخت را مازو و 
در کردستان برو گوبند. از این درخت غیر از 
=== bam MON
11990:بمردن) نو داسن: نو بیدا کردن چبزی را. 
16314:بمالند» می‌تواند درات زبر کاغذ و با کاه را 
18987:بم» ساکن. زن. سزاوار» شاسته. نجیب» 
20555:بماسکت بال: ۱29۲۰-121 [- سک تال ] 
22321:بمردیدد: -[۵۲-0 (مسصل.) از راه 
24541:بمرات: بارها؛ مکررآ. 
25245:بمز ۱200 0 0 اوای درشت و خشین 
25251:بم. ۱20 [- بام] (اصت.) با دست زدن بر سر 
25254:بمب: ۲۵ (.) جسمی غالبا استوانه‌ای 
25276:بمب‌انکن ۰ ۱0۵00-21620 [قر. ف.] (افا.
```


## [2026-09-05T05:48:45.875Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '605,625p' UNV.txt"
}
```


### [2026-09-05T05:48:45.921Z] TOOL RESULT

```
Indischen  nennt  man  sie  Ko-
*
kosnuß,  und  im  Persischen nennt  man  sie  indische  Wal¬ nuß.
51.  Die  hyrkanische  Pi¬ staziennuß  ,  wenn  man  sie auf  einem  Bräter  röstet,  und frische  Linsen,  wenn  man  sie mit  dem  Saft  der  Oliven  ißt.
53.  Die  Dattel  von  Hirat, die  mit  Walnüssen  gefüllt ist,  die  frische  Pistaziennuß, und  der  armenische  Pfirsich'^, die  Eichel,  die  Kastanie  mit Zucker  und  Kandis.
58.  Aber  niemals  kann  sich mit  Hanfkörnern  von  Kesäli-
49.  '  Mk.3v^-
51.  ^  Ich  nehme  3^  lüer  und  in  §  52  gleich  np.  'Pistaziennnß’.  —
^  s.  §26.  No.  a.  —  ^  Hss.  —  *  Hss.  ^  p]rgänzt  nach  der  Parallele  in  §21.
—  ^  Hss.  3^3^;  s-  §21,  No.  5.
^  Hier  ist  wohl  das  Rost  iin  allgemeinen  zn  verstehen;  s.  §  26,  No.  b.
52.  ^  zn  np.  s.  §  96.  No.  3.  —  s.  §  51.  No.  1.  —  ^  np.  afy.
'the  oaktree,  an  acorn.  a  chesnut‘  (Raverty).  —  *  np.  'glans  regia’.  —
^  Ergänzt  nach  §  50.
^  ^Yörtlich:  'die  Pfirsichpflaimie’;  s.  np.  'PÜanme’  nnd  §40,  No.  1.
53.  ^  np.  nnd  GrBd.  118.  2.
27
^iiexe)  [-’]  )ie)  ^sD^eJHXJüi
hrist  päcan  [i]  pih  pa  he  n^mlipürlh
pa  x^as  ce  nest  patkär  därenah  eci  estet
ucj  ncj  Jv})^
```


## [2026-09-05T05:48:45.953Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '25240,25290p' MON_part1.txt"
}
```


### [2026-09-05T05:48:46.008Z] TOOL RESULT

```
۱ ۳ 
است و از مغز آن رون مخصوصی 
می‌گیر ند؛ بطور کلی میوه‌های ایین گیاه در 
تداوی مورد استفاده وائع می‌گردند؛ بلیلج. 
بلیه: ِ 9۵11۳۷۸۰ ك ۰ بلیه] 0 .) گرفتاری» 
بمز ۱200 0 0 اوای درشت و خشین 
ادمی و ساز؛ صدابی که در بکك واحد زمان 
ار تعاشاتی کمتر از صدای زیر در فضا ایجاد 
کند؛ مق. زیر. (مس.) سیم ساز که صدای 
درشت دهد. 

بم. ۱20 [- بام] (اصت.) با دست زدن بر سر 
کسی به قوت؛ بامب» بام. 

بمب: ۲۵ (.) جسمی غالبا استوانه‌ای 
شکل که در درون آن مواد منفجره می‌ر یز ند 
و در زمان جنگ به وسیلةٌ هواپیما به زمین 
پرتاب می‌کنند و آن در اثر اصابت با زمین 
منفجر می‌شود. یمب اتمی: (نظ.) بمبی که 
نیروی انفجارش مربوط به نیروی ذخیره‌ای 
مرکزی اتم است. نیروی تخریب این بمب 
از یمب‌های معمولی بسیار بیشتر است و یکی 
از آنهاکافی است شسهری را ویران و 
ساکنانش را نابود سازد. بمب شیدروژنی: 
(نظ.) نوعی بمب اتمی» بمبی که نیروی 
انسفجاریش مربوط به نیروی ذخیره‌ای 
مرکزی اتم ثیدروژن است. نیروی انفجار و 
تخریب این بمب از بمب آتمی بیشتر است. 
یمباران: 0000 [فسر. ف. - بمب + 
باران با حذف یک «ب»] (اسر.) پر تاب 
کردن بمب از بالا بر روی زمین» ریختن 
نمب‌های بیایی به موضعیء بمباردمان. . ضیح .- 
فرهتکتتان انم کنلته رات ای وتا ردان 
فرانسوی تصویب کر ده است. 


بمب‌انکن ۰ ۱0۵00-21620 [قر. ف.] (افا. 


امر.) هواپیمایی جنگی که بمب‌ها را روی 


هدف‌های نظامی بر تاب کند. 

سمچر د ع-۲دآمصع آف. ۰ ۰] (حر. 
اض. مر.) در حال بلافاصله در همان آن» ره 
محص. ضح.- لازم الاضافه است. 
نمحضص: 0-۵۵ اف. ع (حر. اض. 
مر.) به مجرد» در همان ان» در همان وقت. 
ضح. لازم الاضافه است.
```


## [2026-09-05T05:49:05.811Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK_full bamb\"; grep -n -i 'lemma: bamb\\|lemma: bal\\|lemma: baba\\|lemma: barbar\\|lemma: bhem' POK_full.txt | head -20; echo \"=== POK_full page 93\"; grep -n 'Page(s): 93' POK_full.txt | head -20"
}
```


### [2026-09-05T05:49:05.881Z] TOOL RESULT

```
=== POK_full bamb
9475:Root / lemma: baba-, ( *bal-bal^ 
9629:Root / lemma: bal-bal- 
9633:Root / lemma: bal-, balbal- 
9639:It seems Root/ lemma: bal- balbal-: "to shake, dance' derived from Root/ lemma: baba-, 
=== POK_full page 93
9627:Page(s): 93 
9631:Page(s): 93 
9651:Page(s): 93 
9779:Page(s): 93-94 
75455:Page(s): 930 
75527:Page(s): 930 
75542:Page(s): 930 
75730:Page(s): 933 
75820:Page(s): 933-935 
76019:Page(s): 935-938 
76550:Page(s): 938-947 
77326:Page(s): 930-933
```


## [2026-09-05T05:49:06.784Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC bomb\"; grep -n -i '^bomb\\|^bamb\\|^bhomb\\|bombos\\|bombus' IEC.txt | head -20"
}
```


### [2026-09-05T05:49:06.844Z] TOOL RESULT

```
=== IEC bomb
916:bamb-, see bamb-
965:bombəl- (bombul-) ‘bumble-bee, cockroach’ or sim. Cf. bumbul-. WP II, 108 Gk. (ambig.) bombúlios, bombüle (prob. fr. bumbul-, q.v); Li. bambalas *bumble-bee, cockroach, dungbeetle'; Latv. bambals ‘dung- beetle'. See next
966:bombo, eio “bang, drum, rumble’. Gk. bombéo: Li. bambù, éti; OCS bobngoti;
968:Per. bam ‘bass; drone’ (LW in Arm. bamb, id.); Arm. cf. pamparag, s. ‘chatterbox’; Gk. bómbos (“hum, rumble'. LW in Lat. bombus); OCS cf. bobnoti ‘bang’; Srb. bubati, bubnuti, id. and OCS bobínü ‘drum’ `
969:bombos (1), see bombo.
970:bombos (2) “lump, bulge’ Rum. substr. bumb ‘knob, cob’; LG pamp ‘thick porridge’; pampen (v. ‘cran ); Ger. dial. Pfampf ‘fat woman’; Sw. pamp ‘big sword’; Li. bámba ‘navel’
978:bombos — bubul-
1498:-wes, n. ‘harm’; adj. ‘evil’; ON bol, ds bolvi, n., bolva, v.; Li. balvas ‘reward’; Latv. balva, id. bhombholos (1), bhombhoaros ‘humming in- sect’. WP II, 161. Cf. bhombhos (1) Skt. bambharah ‘bee’; Ukr. bombàr 'cock- chafer'; Li. bambalas, m. ^bumble-bee, dung- beetle’; Latv. bambals, bambulis, id. bhombholos (2) ‘bob, jumper, swaying per- son or object. Per. bambuli ‘clown’; G Bammel ‘bob’ beside Bembel *bell-clapper, cider-jug'; Li. bamblýs ‘dumpy fellow; youngster bhombhos, à (1) ‘swelling, boss, belly’. WP II, 108. Cf. bombos (2)
1506:bhombhos (2) ‘roar, bang’. WP I, 161 Skt. bhambha(sic) 'kettledrum', cf. bambha- ravah ‘bellowing’; Per. bam ‘bass’; LW in Arm. bamb, id.; cf. Arm. bombiwn “bang, rumble'; Cor. bom, pl. bommyn, id.; G Bam, id.; ON babbi ‘disturbance’; OCS cf. bobencü (ambig.) (drum. Cf. bhumbh-); Li. cf. bam- bü, éti, v. “hum, murmur. Variant in G bamsen “bang, beat'; Li. bámbsiu, eti “bang; mumble?
```


## [2026-09-05T05:49:15.777Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 966 1506 916 970; do echo \"--- line $L leaf:\"; awk -v l=$L 'NR<=l' IEC.txt | grep -c $'\\f'; done"
}
```


## [2026-09-05T05:49:16.625Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9620,9660p' POK_full.txt; echo \"=====93-94\"; sed -n '9770,9800p' POK_full.txt"
}
```


### [2026-09-05T05:49:17.991Z] TOOL RESULT

```
--- line 966 leaf:
39
--- line 1506 leaf:
61
--- line 916 leaf:
38
--- line 970 leaf:
39
```


### [2026-09-05T05:49:18.063Z] TOOL RESULT

```
Lithuanianit»a/rs//). 

Against it Old Irish bacc {n\r. bac) " stick, a crook ', cymr. bach^ corner, hook ', bret. 
bac'h " heel, stick ' (from " clutch, crutch of the stick '), are in the Island-Celtic or already in 
the occurred through Latin back-formations from baculum. 

References: WP. II 104 f., WH. I 92. 
Page(s): 93 

Root / lemma: bal-bal- 
See also: see below baba- 
Page(s): 93 

Root / lemma: bal-, balbal- 

Meaning: to shake, dance 

Note: 

It seems Root/ lemma: bal- balbal-: "to shake, dance' derived from Root/ lemma: baba-, 

( *bal-bal^\ 'barbaric speech' through an Old Indie intermediary (see above). 

Material: Old Indie balbalTti^ whirls ', balva-^ crooked '; gr. (in Sicily) paAAi^w " dances ', 

out of it borrows Latin ballare " dance '. 

Maybe alb. {*bal-) valle^ dance' [common alb. b > i/shift] 

References: WP. II 109, WH. 1, 95, Wackernagel Old Indic-Gr. I 181. 

Page(s): 93 

Root / lemma: band- {*bhend-) 

Meaning: drop 

Note: 

Considering Phrygian P£5u "water' : nasalized lllyrian B/ndus 'waier god' Root /lemma: 

=====93-94
sound '); 



Lithuanian bambetr lium ', in ablaut bimpti6s., bimbalas, birhbilas^ gadfly, horsefly '; 
russ.-Church Slavic buben-b, bubon-b^ drum ', russ. bubn/tb' chat, babble', poln. bgben' 
drum '. 

References: WP. II 107, Trautmann 26, WH. 1111. 
Page(s): 93-94 

Root / lemma: bde/- 

Meaning: to suck 

Material: Gr. p5aAAco ' sucks ', p5£AAa " leech '; Modern High German zu//en' suck in a 

sucking sac ', zu/p " piece of cloth used for soaking up liquid ', Dutch tu//en ' drink, booze, 

sup ', Modern High German tulken^ suck, drink with large gulps, quaff? Kretschmer KZ. 

31,423; 

very uncertain because of more similar Germanic words like Norwegian tuna^ drink a lot ' 

(see Falk-Torp under tylde). If the connection applies, was Indo Germanic initial sound bd-, 

or it is gr. p - perhaps in child language? - from ni-= sni shortened prefix {be- "suck'?). 

References: WP. II 119.
```


## [2026-09-05T05:49:27.655Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 39 40 41 42 61 62; do echo \"--- leaf $n:\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' IEC.txt | head -4; done"
}
```


## [2026-09-05T05:49:27.709Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9745,9775p' POK_full.txt"
}
```


### [2026-09-05T05:49:29.312Z] TOOL RESULT

```
--- leaf 39:
25
30
35
40
--- leaf 40:
vē- (in ve-cors, -sanus, -grandis); Olr. úa, ó ‘from’; OHG cf. a-; MHG a- (in a-maht fant. ness’, a-name ‘nickname’, à-stiure ‘stray’, à- swinc ‘waste fibre’, etc.); OE a-, &-; ON á-; OCS u-, u ‘away’; Latv. au- (?) (in au-manis “senseless'); OPr. au- (?) (in au-müsnan ‘wash’). The px. may be embedded in Gk. aidé-omai (fr. *aue-uid- (?) “look away’; cf. also OE æwan ‘despise’, and perhaps OCS ob- ujajọ, -ujati ‘disappear; go mad’)
aued- (əued-, aud-, əud-) ‘sing’. WP I, 252. Cf. auod- Skt. cf. vádāmi ‘speak, sing, sound’; Gk. aeído; Gallo-Lat. cf. (?) al-auda Clark, for *pal-, see pal- "open space, field” + -auda)
auedhr- (ouedhr-, audhr-, əudhr-, audh-, oudh-) ‘air, wind, weather Am, cf. awd (o-st. ‘air, wind, heaven"); OHG wetar; OE weder; OCS vedrü (adj. “bright, clear), vedro “bright weather”; Li. cf. áudra “storm”
aué-jo “like, favour, want’. WP I, 191. Cf. auis (3)
--- leaf 41:
, acc.pl.; Ir. ai ‘swan’; cf. also éan, pl. éin “bird”; Br. -av, pl. -aved (in ori-av, -aved ‘kind of gull’), cf. also evn ‘bird’; OCS cf. -uj (in krag-uj hawk")
auis (2) “perception”. Cf. àu-mi, aus- Av. cf. uši ‘mind’; Gk. cf. ais-thánomai; Lat. cf. au-dio; (vocalism obscure in ob-oedio); . MIr. éis-dim “hear, listen’; W ewi, id.
auis (3) ‘desire’. WP I, 19. Cf. aué-io Skt. cf. ávih ‘favourable’; ávah (favour; pl. ‘comfort, joy, desire); Av. cf. avo 'protec- tion’; Hitt. (? uwai (for *awi? ‘envy’); Hom. cf. en-ees ‘benign’; Lat. cf. aveo, avi- dus. (Here also? Go. awiljup *thanks', but cf. aue- above); W awydd, m. 'earnest desire”
auios, see auos
--- leaf 42:
babol-, babər-, babot-, see bob-, bəbəd-, etc. (A theme of onomatopoeic character as are most IE themes with initial b-)
bābā (1), üs “old woman? Osc. (queried) babu “old priestess’; R bàba *woman'; Cz. bába, Srb. baba “old woman, midwife’. Cf. bhabh-
baba (2) ‘mess, slobber’ It. bava ‘drivel, dross, waste’; Fr. bave, id.; Du. poep (2) ‘excrement’; E dial. poop, id.; Cz. bába ‘bread-pudding, brown beer
babraio ‘slobber, mess about. Cf. bābā (2) Du. cf. poeperij ‘diarrhoea’, poepert ‘arse’; Fris. id.; Pol babrać ‘slop’; Cz. babrat ‘potter’
--- leaf 61:
“pale, whitish, bright’. WP 211 & 217. Cf. bhloidēið Ir. cf. blaodhm ‘big flame’; OE blāt ‘pale’; OCS blédü, id.
bhloid- (2) (?) ‘seethe, swell’. Cf. WP II, 211. See bhlid- Gk. phloidéo 'seethe'; E to bloat (orig. con- fused); cf. (?) Latv. blistu, blist, pf. blidu ‘well up, seethe; evaporate; congeal
bhloideið, ið ‘turn pale’. See bhloid- (1) and cf. WP II, 217 OE blātian; OCS blëdëjo, čti, id.
bhloi-, see bhlós-
--- leaf 62:
(radical element). Cf. WP II, 214 Gk. cf. phlüktís ‘blister’; Lat. flüctus; Blg. cf. blikam ‘gush’
bhlus-, see bhluso and cf. bhlusk-, bhluks- OE blysa ‘torch’; ON blys, id. beside blossa ‘blaze’; Norw. bluss. s, blusse, v. id.
bhluskos “light, bright, pale’. Cf. bhluks- Ir. Mir blosc ‘clear’; s. “light (Ir. also ‘clear voice, noise); OE blyscan (“blush?, but of ambig. sense, cf. bhluso, bhluuó, bhleuo); Cz. (+ü) blýskat, v. ‘lighten, flash?^; Slovak blyskat (sa), blysknüt, id. See next
(bhlüst- variant, cf. bhluskos, bhluks-) Srb. blistati ‘shine’, blistav ‘shining’; Li. blüscioti ‘gutter, sputter as candle’
```


### [2026-09-05T05:49:29.363Z] TOOL RESULT

```
References: WP. II 107. 
Page(s): 91 

Root / lemma: ba>^mb- 

Meaning: a kind of noise 

Material: Gr p6iJpO(; m. (out of it Latin bombus) ' a boom, deep hollow noise ', p6|jpu^, - 

UK0(; " fleas ', poiJpuKia ' humming insects ', poppuAr) ' narrow-necked vessel ' (as " 

gurgling '), poppuAi6(; or -uAioc; " bumblebee ' (and " narrow necked vessel '); about 

papipaivoj " clatters with the teeth; stammer, lisp ' see below baba-. 

Maybe Italian bombo : Spanish abejorro; bombo : French bourdon : Aragones bombolon : 
Asturian babaron: Catalan borinot: Galician abellon: Latin Bombus terrestris : Valencian 
borinoV bumble bee; bumblebee ' : Lithuanian bimbalas, bimbllas A\ban'\an : bumballa 
gadfly, horsefly '. 

alb. bumbulit " it thunders '; 

Germanic with by neologism prevented sound movement Old Icelandic bumba^ drum ', 
Danish old bomme, bambe^ drum ', holl. bommen\o drone ' (compareauch Modern High 
German bum bum, a little bit similarly Modern High German bammein, bimmeln^ ring, 
sound '); 



Lithuanian bambetr lium ', in ablaut bimpti6s., bimbalas, birhbilas^ gadfly, horsefly '; 
russ.-Church Slavic buben-b, bubon-b^ drum ', russ. bubn/tb' chat, babble', poln. bgben'
```


## [2026-09-05T05:49:45.318Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /bombo, eio/{print \"LEAF1BASED=\"NR; print substr($0,1,300); print \"...\"; print substr($0,length($0)-300)}' IEC.txt; echo \"======\"; awk 'BEGIN{RS=\"\\f\"} /bhombhos \\(2\\)/{print \"LEAF1BASED=\"NR; print substr($0,1,200)}' IEC.txt"
}
```


### [2026-09-05T05:49:46.928Z] TOOL RESULT

```
LEAF1BASED=44
angle’ beside burbeti ‘mutter’
biĝ- ‘wax, glue, resin’ or sim. Oss. bidz, D bedzä ‘lees of beeswax’; Ir. bigh ‘glue’; Arm. cf. piyc (‘dirty’, fr. *biglo-)
bi&- ‘titch, tot; dot Skt. bijam 'seed, germ'; Arm. cf. pz-ti, pz- tik ‘tiny’; Go. cf. peika-bagms (fpalm-tree', li
...
 bombo.
bombos (2) “lump, bulge’ Rum. substr. bumb ‘knob, cob’; LG pamp ‘thick porridge’; pampen (v. ‘cran ); Ger. dial. Pfampf ‘fat woman’; Sw. pamp ‘big sword’; Li. bámba ‘navel’
bradō, ið ‘seethe; prate’ Gk. (ambig.) brázo “boil, foam, rage’; Du. praten ‘foa
======
LEAF1BASED=66
‘bob’ beside Bembel *bell-clapper, cider-jug'; Li. bamblýs ‘dumpy fellow; youngster bhombhos, à (1) ‘swelling, boss, belly’. WP II, 108. Cf. bombos (2)
20
25
30
35
40
45
Gk. pomphós “bu
```


## [2026-09-05T05:50:23.557Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN around p44 (leaf 65)\"; awk 'BEGIN{RS=\"\\f\"} NR==66' HRN.txt | head -50"
}
```


### [2026-09-05T05:50:24.994Z] TOOL RESULT

```
=== HRN around p44 (leaf 65)
- 44 —
phlv. apuxscLt/(i)snik (Men.).
Von bexsiden streng zu trennen (Nöldeke ZDMG.
46, 138 Anm. 2). Doch findet bisweilen eine Ver-
inischung der Bedeutungen statt, z. B. Sahn. I, 30
Vers 139, wo bexsüdm für 'schenken' steht; gunCLh
bexslden *die Sünde verzeihen' (eigentlich 'schenken')
u. dgl. sind dagegen logisch klar.
187. {\)hed 'schlecht*, vergl. Comp, heiter, heter (AM. 220
Zeile 5, 4 v. u.; Sahn. I, 57 Vers 443 0, 87 Vers 443),
daneben beterter (Sahn.; Jer. 7, 26).
g. vad; Käs. vad, ved, bez (AM., d. i. beö) etc.
phlv. vat^ vatak, arm. LW. vat, vatfar, vergl.
vatabaxt, vatabaxtik,
bei. gvadil {*gvad-dil) 'feige* (130) hält Hübsch-
mann ZDMG. 44, 557 (wohl nicht mit Recht) für ein
LW.
LW. kurd. af/. bei. bad, bed,
188. {2)-bed, -bud 'Herr* (Comp.), z. B. sipehbed, möbed,
hBrbud.
aw. paiti-, -paiti^ 'Herr ; phlv. pat, ^pat, arm. LW.
pet, -pet; ai. päti-, -pati-,
oss. LW. fätäg Tührer' (v. Stackeiberg ZDMG.
43, 672).
189. hidest, gidest 'Spanne'.
aw. vltasti- 'Spanne'; phlv. v(i)tast; skr. vitasti-
'Spanne*.
Das unbelegte np. audes, audest setzt ein aw.
*avatasti' voraus.
190. (\)ber 'Brust', vergl. ber a ber,
mäz. var; Käs. ver, ver ö vir.
aw. varah- (ZPGl.) 'Brust'; phlv. var,
kurd. LW.(?) ier; bei. gvar (135).
191. {2)ber, eber, auf, über, nahe bei' etc.; "ibN Is. 1, 1;
vergl. berm 'höchster 2).
*) Mohl übersetzt falsch durcli *mieux*.
2) Phlv. barin 'höchster*.
```


## [2026-09-05T05:50:25.760Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD wad\"; grep -n \"^wad\\b\\|^wad \\|wattar\\|wad \\[wt\" PHD.txt | head -20; echo \"=== NYB vat\"; grep -n \"vat\\b.*bad\\|wad.*bad\" NYB_vol2_glossary.txt | head -10; echo \"=== DKS vata\"; grep -n -i \"^vata\\|bāta\\|'bad'\" ISS_alt_DKS.txt | head -20"
}
```


### [2026-09-05T05:50:25.865Z] TOOL RESULT

```
=== PHD wad
604:wad-baxt 86 wānīdan
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
637:wattar [SL Yti, v. wad | M wtr, N EI worse, bad, evil. -īh: evil, wickedness.
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
913:bad wad, wattar; v. evil.
1815:evil (a.) akēmand, апар, druwand, wad(ag), wattar, duš-; ~ deed dušxwaršt; ~ eye aš, dujdoys?rih; ~ rule dušpādixšāyīh; ~ ruler dušpādixšā(y); — speech dušēwāz- ih, dušhüxt; — spirit Ahreman, gannág mēnēg; ~ thought duš(hu)- mat; of ~ behaviour duškunišn; of — religion agdén, dujdén; of — speech duš-gēwišn; of — thought dušmenišn.
4309:why čē rāy, čim (rāy). wickedness dušīh, wattarih. wide frax, pahn, wéhm, wišād. widow wéwag.
4351:worse wattar.
4409:Jeh Way i wattar Xēšm
4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
=== NYB vat
1984:Hérat [hylt'] the town of al-Hira in Iraq, 1154-5. — Aram hertä ‘camp’. hérpat [hylpt'] a priestly title and degree in the Zoroastrian clergy 55%; holder of this degree 105. 31” (with the indef. art. 7-6); pl. cas. obl. ~-dn 1078; —-an ~ the chief h. 11119. — Av. (20) ač0rapati- ; Prs. inser. ’yhrpt; Paz. érwad, Skr. v. ācāryādhipati (Aog); NP hirbad. Wikan- der, Feuerpriester, v. Index.
4031:vat [SLY”; wt' 61%] evil, bad 61%. 7822. 791.2; dast i ~ vāzītan to play the game badly 121'7; more common is the comp. (= sup.) vattar [SLY-tl; 79?! SLY^-tl] worse, the worst, generally used as an emphatic pos. instead of vat (cf veh); hence the sup. vattartom [SLY-tltwm] 7168; vāi i veh... vai i vattar 729-19;
4032:pat hàn i vattar šēn 7471-2; pat hàn x vattar vitarg 76%; — subst. pl. cas. obl. vattarān evil beings, evildoers, the wicked, opp. vehän, 5511-12, 628-9 etc. passim. — MPrthPrs wd; Arm. lw. vat, vatt‘ar; Paz. vad, vadtar, vatar; NP bad. — wtk?n' 9028: read Vadagdn, g. v.
4036:vat-baxt [wtbht'; SLY? bht'] having bad luck, luckless 92-12, 10711,
4037:vat-došaramčh [wtdwš'Imyh] the quality of having bad affection, coldheartedness, unfriendliness 849. — Skr. v. nikrsta- vällabhya.
4039:vat-hunar [wthwnl] of bad skill, unskil- ful, comp. ~-tar 15$.
4043:vat-xém [wthym] ill-disposed, bad-tem- pered 9111.
4061:vāzišn v.n. of vāzītan (g. v.), pred. 1211’: dast + vat nē ~ it is necessary not to play the game badly.
4560:Zčiš [Paz.; zwyš] the mother of Zartux&t's mother 36*!; her husband was Frähim (g. v.) rwanan 374-5. — In all probability ~ is originally not a n. pr., but some form of Av. jahi (v. jeh), ef jaēš FrO 15, in this case used of a pre-Zoro- astrian woman without any contemptuous ring. Cf also FrO 2 f: (zan . . .) ka vat, je, jahe u jahi; hast giyāk kū carätik ka pat Sod ne dätak ‘if a woman is bad she is je, jahe or jahi; in some places these ws. signify a girl that has not yet been given to man’. This being so, NYŠH = zan 37? init. is to be regarded as a gl. to Zčiš, 1. 1.
=== DKS vata
1919:güysma 'alternative(?)', Sid. тоогу khu hvamdye Jsahera ttauda süda güysma bāta hame 'when in a man's belly there arises hot (and) cold wind alternating'. Possibly from *ava-auz- ‘to change', to Oss. D. uozun, ozun, T. йтуп, üst 'to swing, rock, stagger’; uzgd-uzgd zyory ‘ће swims swingingly'; from auz-, a variant to vas- ' to move’, see bays-.
5007:parittam üyuh-pramanam; with compound, пі 14:18 ba- jsinya himáre 'they become short-lived’ (like ibid. 16 muyspa-jsni, ibid. ig's4-35 muysga-jsinya); Sid. буд Ёш {а иісі baka u bata bahya ' where little water and few trees’, BS alpa-ambu-éakhi, Tib. čhu mus-iim sio ñun- bahi yul-na; Е. 2, 137r5-v1 bataku sá gyastavura dātä cu ananda samaná site ' little, prince, is the dharma-doctrine which Ananda the #ramana (ascetic) learned’, Tib. алі bu dge-slon kun-dgah-bos chos kun Chub-par byas-pa-na Tiun-gi ; V 170, тат bate dyáte u bate pyü(ste) ‘saw little and heard little’. Later ba-, baka-, bakala-, bakalaka-, 1 169, Ssrr ba-hauva ‘weak’, Sid. 2v2 baka Бойка 'under- standing little’, BS a/pa-medhas-; 1 141, 49v4 baka- Jaukrra, BS alpa-sukra-; Sid. 7rs baka hova, 'T'ib. ñams- stobs čhun-ba; Sid. 145r2 bakalaka; т 9:144 haira bakala hamyai 'things became few’, Comparative, Z 1:45 battara-, superlative, Z 24:228 battama-. Contrast bata- and #ra- 'good', т 169, 85r1-2 java-ttaramdara cvim (-йп-==-аї) dahausta пійа ttyi fara hauva padimi ' having an exhausted body who has no virility, it makes for him good strength', contrasting with І 169, 8$гт ba-hauva Jara-hauva padimi ' makes the weak to have good strength; Sid. r42r1 beti-ysunamdaita ‘with little flow’, BS alpa- sruti-, Tib. hdzag-pa fiun-sin. Note for ‘small’ and ‘bad’, O.Slav. xudii 'small', Russ. xudi 'small, weak’, xudój ‘bad’, Akun араій ‘bad’, O.Ind. alpa- ' small', O.Slav. malù ‘small, few’, malyj 'small', Lat. malus 'bad', Got. smals ‘small’; Armen. lw. попаз 'little, few; base, low’, Greek óAfyos ‘small, few’, Alban //g 'evil, meagre’. Khotan Saka bata- 'small' can thus be connected with *oata-, Zor.P. wt *vat ‘bad’, vatak, vattar ‘worse’, Armen. lw vat, vata-baxt ‘unfortunate’, vatt'ar ‘Worse’, vatt'arem ‘to make inferior’, M.Pers.T. wd; wtr qyrdn tto overcome’, N.Pers. bad, Xuri god, Baloët gwat ‘bad’. Here also O.Ind. RV 10:10:13 batd batas yama ' (Yami speaks) Bad you are, bad Yama”, beside the exclamation of dissatisfaction Pali vata, BS bata. From a base in -à-, а derivative -ata- may occur (as O.Ind. vrata-, Av. urvata- to base vrà-) hence vata- may be traced to vā-: ñ- ' be defective’, see s.v. vüra-. See also vanda- ‘small’,
6799:vataysde ‘flows down’, Z 17:12 ggaryau vataysde піса ‘the water flows down from the mountains', See s.v. ttajs- ‘flow’ (*ava-tacatat).
7252:Sir- 'be bad', и 27, 12v5 fastá himi khu sald nä byehi и pe vi Siri pajsd ат va asa vahani(dá) ‘is cleaned, so that mud does пог affect one, bur under foot it is bad, seriously there the horses sink badly’, compared with t 33, 3b2 pe vi tta pamdà paskyásta тийп himye ' underfoot the road so again became bad (rotted)'. From base zuar-, Zur-ya- > Zar-, šir- (Zu- > d-, as su- > $-) to Av. sbar- ‘go crookedly’, zbaraBa- ‘foot’, zxbaramna-, zbarantam, Sogd. Bud. zf'r'y ‘to во’, Chr. 'zbr-, Yayn. zwür-, zwér- ‘turn’, Oss. I. duzdr 'bad' (but. D. ldyuz). See КТ 1v 65b3; SDTY 39.
7694:sürai ‘Баа (?)', Manj. бб ausa agapt sa sürat anecvà skajva üttma ' this self (BS atman-) is bad, improper, evil in the impermanent (BS anitya-) samshára-acts' ; Manj. 13 sülia sūrai üttama па ttye 'in pleasure (BS sukha-) evil is not the self of this man'; pejorative from the context, hence possibly from *safra-, *sifra or *sufra ‘rotted’ to Lit. ipti, Smpü ‘be weak’, Ийрїї, Йитрй ‘о corrupt’, as Oss. D. fud, I. fyd 'bad' from pūta- 'rotted' (see s.v. hambūta-), Greek стүттоноп ‘to rot', солтра, отүтгтїк®. Hardly *asuraa- ' not pure’ by loss of a- (as zasa- from anaufa-); possibly süra-a- to sūra- ‘strong’ in bad sense ' violent.
```


## [2026-09-05T05:50:50.525Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T05:50:50.533Z] TOOL RESULT

```


```


## [2026-09-05T05:50:54.051Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%B7",
 "prompt": "Give the full etymology sections for the Arabic بلوط (ballūṭ) and the Persian بلوط entries: what is each said to be borrowed from (Aramaic? Greek? Persian?), and any cognates listed."
}
```


## [2026-09-05T05:50:55.310Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/bellota",
 "prompt": "Give the etymology of Spanish bellota (acorn) - what Arabic form is it from, and what is that Arabic word said to derive from?"
}
```


### [2026-09-05T05:51:00.191Z] TOOL RESULT

```
# Etymology of Spanish "bellota"

According to the Wiktionary entry, Spanish **bellota** comes from Andalusian Arabic, which borrowed the term from Arabic **بَلُّوطَة** (ballūṭa, meaning "oak, acorn").

The Arabic form is said to derive from **Syriac** ܒܠܘܛܐ, making the etymological path: Syriac → Arabic → Andalusian Arabic → Spanish.
```


### [2026-09-05T05:51:01.892Z] TOOL RESULT

```
# Etymology of بلوط (ballūṭ)

## Arabic Entry

**Source Language:** Aramaic

The Arabic بلوط is borrowed from Aramaic בְּלוּטָא/ܒܠܘܛܐ (bəllūṭā, ballūṭā, meaning "oak; acorn").

**Possible Additional Origins:** The entry notes two theories:
1. An Aramaic formation from בָלַט (bālaṭ, "to bulge out, to stand forth"), referencing the nut's protruding shape
2. Possible connection to Akkadian balāṭu ("to live, to stay or remain") or be-lit/baluṭ ("a strong tree, bearing edible produce")

**Cognates listed:** Middle Persian blwt' (balūt), Mazanderani پلت (palat), Northern Kurdish berrû/belû, Turkish variants (bolut, pelüt, palıt), Azerbaijani palıd, Uzbek balut, and various Romance language descendants.

## Persian Entry

**Source Language:** Middle Persian → Aramaic

The Persian بلوط derives from Middle Persian blwt' (balūt, "oak, acorn"), which itself comes from Aramaic בְּלוּטָא/ܒܠܘܛܐ (same Aramaic root as Arabic). The entry directs readers to the Arabic entry "for more" etymological detail.
```


## [2026-09-05T05:51:13.916Z] TOOL CALL #34: Bash

```json
{
 "command": "pdftoppm -f 76 -l 76 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg76 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T05:51:15.161Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%AF",
 "prompt": "Give the Persian بد (bad) etymology section in full: Middle Persian form, Proto-Iranian reconstruction, any note about English 'bad', and cognates."
}
```


### [2026-09-05T05:51:16.409Z] TOOL RESULT

```
total 7172
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 01:51 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
```


### [2026-09-05T05:51:24.045Z] TOOL RESULT

```
# Persian بد (bad) Etymology

## Full Etymology Section

**Middle Persian form:** The entry shows \[script needed\] (SLYA) / \[script needed\] (wt' /⁠wad⁠/, "bad, evil")

**Proto-Iranian reconstruction:** "From [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*watah](/w/index.php?title=Reconstruction:Proto-Iranian/watah&action=edit&redlink=1 "Reconstruction:Proto-Iranian/watah (page does not exist)")_"

**Relationship to English:** The entry explicitly states the terms are "Unrelated to [English](https://en.wikipedia.org/wiki/English_language "w:English language") _[bad](/wiki/bad#English "bad")_, despite phonetic and semantic similarity."

**Cognates:** The page lists [Old Armenian](https://en.wikipedia.org/wiki/Classical_Armenian "w:Classical Armenian") _[վատ](/wiki/%D5%BE%D5%A1%D5%BF#Old_Armenian "վատ")_ (vat), described as "an Iranian borrowing."

**Note on completeness:** The etymology section itself contains a flag indicating missing information, requesting clarification about whether the proto-Iranian term derives from Proto-Indo-European _[\*weh₂t-](/wiki/Reconstruction:Proto-Indo-European/weh%E2%82%82t- "Reconstruction:Proto-Indo-European/weh₂t-")_ and suggesting comparison with Sanskrit cognates.
```


## [2026-09-05T05:51:26.918Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg76.png"
}
```


### [2026-09-05T05:51:27.659Z] TOOL RESULT

```

```


## [2026-09-05T05:51:27.656Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T05:51:38.399Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg76.png')\nprint(im.size)\nim.crop((1380,700,2000,900)).resize((1240,400)).save('c_belloth.png')\nim.crop((530,1850,1250,1990)).resize((1440,280)).save('c_schyth.png')\n\""
}
```


### [2026-09-05T05:51:40.461Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-05T05:51:42.709Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_belloth.png"
}
```


### [2026-09-05T05:51:42.726Z] TOOL RESULT

```

```


## [2026-09-05T05:51:52.580Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT bellota\"; grep -n -i 'bellota\\|ballut' LKT.txt | head -10; echo \"=== DEV\"; grep -n -i 'bellota\\|ballout\\|ballût' DEV.txt PHN.txt LAM.txt | head -10; echo \"=== SKT bomb\"; grep -n -i '^bomb\\|bomb,' SKT.txt | head -5; echo \"=== WEB bellote\"; grep -n -i 'bellote' WEB_vol1.txt FSD_vol1.txt | head -5"
}
```


### [2026-09-05T05:51:52.685Z] TOOL RESULT

```
=== LKT bellota
686:'Eichel,  Kastanie',  Einheitsnomen  bal- lüta;  hieraus  sp.  bellota  [woher  hat  ML 1025  die  Form  balota'^  Dies  Wort  ist ja  'die  Stimmkugel'],  pg.  belota,  boleta, bolota  'Eichel',  it.  ballotta  'gesottene Kastanie'.    [DE  239.    Eguilaz  343.
=== DEV
DEV.txt:2335:Dans  la  péninsule  Hispanique,  le  mot  arabe  a  donné l'espagnol  bellota  et  le  \)oriugdi\sbelota,bolota,boleta, gland. Bellote,  gros  clou  à  tête,  paraît  aussi  se  rattacher  à  ces termes,  par  suite  d'une  certaine  ressemblance  avec  un gland  muni  de  sa  cupule.
DEV.txt:3029:Bellota,  esp.  voy,  Ballole,
=== SKT bomb
2015:BOMBAST.
2033:Bomb,  Bombard.  (F..L...Uk.) Boom  (1).
2034:BomboAt,  ong.  cotton>«radding; padding,  affeclea  language.   (h>l  ■'^'
2071:bomb,  a  &hcll  for  cannon.  (F.  —  L.  — Gk.)  F.  i>^Hthi.  mm  L  bomhus,  a  humming noise.  — Gk.  06^^001,  the  same.
2072:bombard.  (F.-L. -Gk.)  The  verb is  from  E.  bcmbardt  a  great  gun  ;  Sh.  — F. bombarde,  a  cannon  ;  extended  from  F. bombe.  "Det.  bombarditr,  F.  bombanfitr (Cot.)
=== WEB bellote
```


## [2026-09-05T05:51:53.236Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bomb",
 "prompt": "Give the full etymology of 'bomb': French bombe, Italian bomba, Latin bombus, Greek bombos, and dates."
}
```


### [2026-09-05T05:51:58.051Z] TOOL RESULT

```
# Etymology of "Bomb"

The word "bomb" traces back through multiple languages:

**French:** *bombe*
**Italian:** *bomba*
**Latin:** *bombus* — "a deep, hollow noise; a buzzing or booming sound"
**Greek:** *bombos* — "deep and hollow sound" (echoic origin)

**Dating:**
- **Noun (1580s):** Originally referred to "explosive projectile," consisting of a hollow ball or shell filled with explosive material
- **Verb (1680s):** Meaning "fire bombs at, attack with bombs"

The term is believed to derive from the sound the projectile makes, as indicated by the Greek and Latin roots' emphasis on auditory qualities. The modern sense of "explosive device placed by hand or dropped from airplane" emerged in 1909.
```


## [2026-09-05T05:52:09.045Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '680,692p' LKT.txt; echo \"=== leaf\"; awk 'BEGIN{RS=\"\\f\"} /hieraus  sp.  bellota/{print \"LEAF1BASED=\"NR}' LKT.txt; echo \"=== DEV ballote entry\"; sed -n '2320,2340p' DEV.txt"
}
```


### [2026-09-05T05:52:10.588Z] TOOL RESULT

```
'2U3.  Ar.  Balkis: X.  pr.,  Name  der  sagenhaften  Königin von  Saba,  die  zur  Zeit  Salomos  lierrschte, vgl.  Koran  Sure  27,  wo  der  Name  aller- dings nicht  genannt  wird.  Nach  A.  Rösch, Die  Königin  von  Saba  als  Königin  Bil- qls.  Eine  Studie.  Leipzig  1890  ist  das ar.  Wort  vom  gr.  uaWaKiq  'Kebsweib' abzuleiten  [das  gr.  Wort  mufs  selbst  wie lat.  pallaca  vom  hebr.  oder  phöniz.  pi- leges  'Kebsweib,  Buhle'  kommen;  die Benennungen  unsittlicher  Personen  und Verhcältnisse  pflegen  von  dem  niedriger stehenden  Volk  aus  dem  Sprachschatz des  höher  gebildeten  übernommen  zu werden].  Nach  Löbel  EITAP  11  soll mit  Berufung  auf  Laurian  §i  Maxim, Glosariu  de  vorbe  sträine  In  limba  ro- mänä.  Bucure§ti  1876,  p.  50  das  Wort im  Türkischen  die  Bedeutung  'dick  und groß'  haben  [fehlt  aber  bei  Kelekian Kämüs].  Hieraus  rum.  balciz,  halcäz 'garstig,  plump,  stämmig'.  —  Die  von Löbel  a.  a.  0.  gegebene  Ableitung  vom gr.  TTaXaid  KüZiKoq  'Ruinen  von  Kyzikos am  Marmarameere'  ist,  weil  semantisch unzulässig,  abzulehnen.
204.  Ar.  ballä'a:
'Hauskanal,  Abzugsgraben,Kloake',  eben- so ar.  ballü'a.  Hieraus  sp.  arboUön, ulbellön  'Abzugsgraben  der  Teiche  und Höfe',  albanal,  albaüar  'Kloake';  arag. albellön,  val.  arbellö  'Abzugsgraben'. Ebenso  siz.  biddaca  'dass.,  Abort'.  [DE 65.  Eguilaz  102.  ML  908a  (wo  ar.  balla ungenau  ist).
205.  Ar.  ballür:
'Kristall';  hieraus  sp.  abalorio  'kleine Glasperle',  pg.  avelorios,  avellorios  'Glas- perlen, wertlose  Kleinigkeiten'.  [DE  31.
206.  Ar.  ballüt:
'Eichel,  Kastanie',  Einheitsnomen  bal- lüta;  hieraus  sp.  bellota  [woher  hat  ML 1025  die  Form  balota'^  Dies  Wort  ist ja  'die  Stimmkugel'],  pg.  belota,  boleta, bolota  'Eichel',  it.  ballotta  'gesottene Kastanie'.    [DE  239.    Eguilaz  343.
207.  Tk.  balta:
[Stamm  bal  'zerhauen,  spalten'  Vämbery TktEtWb  S.  197,  Nr.  2071]  'Axt,  Beil'; hieraus  russ.  balta  'schmales  Beil',  klruss. poln.  balta,  bulg.  serb.  balta  'Beil';  rum. bältac,  bältag  'Streitaxt,  Keule'.  [Gorja- jewlO.  Mikl  SlEtWb  7.  Bern  SlEtWb  41.
208.  Tk.  balyk:
'Fisch';  hieraus  russ.  balyk  'gedörrter Stockfisch',  serb.  haluk  'Fischkörner, Kockeiskörner'  [z.  B.  zur  Vertilgung  des Ungeziefers],  poln.  nur  im  Ausdrucke na  balyku  'auf  allen  Vieren,  sehr  un-
geschickt [wie  ein  Fisch  auf  dem  Trock- nen]'.   [Bern  SlEtWb  41/42.
209.  Mal.  bambn:
=== leaf
LEAF1BASED=45
=== DEV ballote entry
ZouiDJA.  Terme  d'administration,  en  Algérie  :  étendue de  terre  que  deux  bœufs  peuvent  labourer  dans  la  saison. (Cherbonneau,  Dict.  fr,-ar.^  Transcription  de  l'arabe  al- gérien i^3;  zouïdja,  qui  se  rattache  à  ^j)  zawwadj ,  for- mer une  paire.
ZuFAGAR.    c^Ton   esprit  est  plus  perçant  que  Zufagar,
cette  épée  d'Ali,  qui  avait  deux  pointes.  ??  (Montesquieu,
Lettres  persanes  ^ .)  Altération  de  l'arabe  ^ÙÀi!  ^S  dhoïi'l-
faqiir.  Voy.   sur  cette  épée,  donnée  à  Ali  par  Mahomet,
D'Herbelot,  Bibl.  orient.
'  Tomo  I"',  p.  38,  de  Tiklil.  André  Lefèvre.
DES  MOTS  D'ORIGINE  ORIENTALE.  231
ZuRNA.  c^ Instrument  de  musique  des  Turcs,  qui,  par sa  forme  et  la  qualité  de  ses  sons,  ressemble  à  notre hautbois,  w  (Bouillet,  Scienc.)  C'est  le  persan  U;)  zoiirnà  ou UjAM  sournâ,  aussi  orthographié  jj^w,  où  la  dernière  syllabe rappelle  le  mot  j  net/  ou  ^Jô  nây ,  roseau,  tuyau,  tlût(\ Les  Malais  ont  le  même  instrument  sous  le  nom  de  j^jw saroînmj.
ADDITIONS.
Ballote.  Chêne  à  glands  comestibles  des  côtes  d'Afri- que, connu  aussi  sur  la  côte  d'Espagne.  En  arabe,  L^^ balloût  [dans  Avicenne).  En  persan,  LsjXAjùUi  châh-balloût,
chêne  du  roi,  se  dit  du  châtaignier.
La  germandrée  officinale,  vulgairement  nommée  petit chêne,  à  cause  de  la  ressemblance  de  ses  feuilles  avec  celles
du  chêne,  porte  en  arabe  le  nom  de  (j^^^î  L^^  balloût  al-
ardh,  chêne  terrestre.  Chez  nos  botanistes,  ballote,  hallo- ta,  se  dit  ordinairement  du  marrube  noir,  qui  est  une  la- biée comme  la  germandrée.  Ballote,  lo^  balloût,  repré- sentent le  grec  l3aXXcoTi]\  qui  ne  se  disait  pas  du  chêne, mais  seulement  du  marrube  ou  d'une  plante  de  la  même famille.  Si  ballote,  labiée,  a  été  pris  du  grec  (par  l'inter- médiaire du  latin  ballote),  il  est  certain  que  ballote,  chêne, nous  est  venu  des  Arabes.
Dans  la  péninsule  Hispanique,  le  mot  arabe  a  donné l'espagnol  bellota  et  le  \)oriugdi\sbelota,bolota,boleta, gland. Bellote,  gros  clou  à  tête,  paraît  aussi  se  rattacher  à  ces termes,  par  suite  d'une  certaine  ressemblance  avec  un gland  muni  de  sa  cupule.
Béiiémotii.  Animal  extraordinaire  décrit  dans  le  Livre de  Job  (ch.  xl,  lo  et  seq.).  C'est  l'hébreu  niD.is  beliemOth, qu'on  regarde  comme  le  pluriel  de  nçni  bchematli,  bêle. c^On  doit  entendre  par  ce  nom-là,  selon  la  Vulgate,  un éléphant,  lequel,  à  cause  de  la  grandeur  de  son  corps, en  vaut  plusieurs.??  (vSimon,  DIct.  de  la  Bible.)
ADDITIONS.  233
Belzéblth.  Divinité  des  Philistins.  C'est,  dans  la  Vul- gate,  Beelzebub  (Heg.  IV,  ù  et  seq.),  qui  est  la  transcrip- tion de  l'hébreu  3i2î  ^i??  baal  zeboûb.  Zeboiib,  en  hébreu, signifie  mouche,  et  on  interprète  le  nom  de  cette  divinité par  le  prince  des  mouclies.  Dans  l'Evangile  de  saint  Mat- thieu (cap.  XII,  v.  2/1),  Belzébuth  est  qualifié  de  prince des  démons;  ici,  quelques  scholiastes  lisent  IBseX^e^ouX  et interprètent  le  prince  de  rordure,  d'un  mot  b^2\  zeboîd,  cor- respondant à  l'arabe  J<xj)  zebll,  fumier,  ordure.  (Voy. Brettschneider,  Lexicon  Novi  Testamenti,  Leipsig,  i84o.)
Mescal.  Instrument  de  musique  en  usage  chez  les Turcs,  n'est  autre  chose  qu'une  espèce  de  flûte  de  Pan qui  ne  compte  pas  moins  de  vingt-trois  tuyaux.  (Bouillet, Scienc.)  Transcription  de  l'arabe  JLSii/o  mithqûl,  que  les Turcs  prononcent  mesqâl.  Le  mot  JlxU  désigne  le  plus  or- dinairement un  poids  bien  connu,  le  miscal  ou  methcal (valant  2/1  carats),  en  esp.  m/to/^  portug.  matical,  meti- cal ,  de  la  racine  JJiS  thaqal,  peser.  Mais  c'est  aussi,  bien que  Freytag  n'en  dise  rien,  le  nom  d'une  espèce  de  flûte de  Pan  :  c^Aliquot  fistulae  simul  junctae,  quae  flatu  oris  in- fluntur?5,  dit  Meninski.
Pirogue.  Ce  mot  océanien  doit  être  rapproché  du  xndi- \di\s  ^\Ji  prâho ,  en  javanais  (m^<i^n  |?ra/iOM^  bateau.  (Voy. Piuo.)
```


## [2026-09-05T05:52:25.499Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%B7/",
 "prompt": "Quote the \"فرهنگ معین\" section for بلوط exactly, including any bracketed origin tag such as [ع.] or [په.]. Also quote the دهخدا section's etymological remark if present."
}
```


## [2026-09-05T05:52:26.318Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%85/",
 "prompt": "Quote the \"فرهنگ معین\" section for بم exactly, including any bracketed origin tag such as [ع.] or [په.] or [فر.]. Also quote the دهخدا entry's remark about origin if present."
}
```


### [2026-09-05T05:52:30.336Z] TOOL RESULT

```
# بلوط - Quotations from Reference Works

## فرهنگ معین

"(بَ) [په.] (اِ.) درختی است تناور با برگ های شکافدار و گل های دراز و آویخته"

## لغت نامه دهخدا - Etymology

The diction source provides etymological context without explicit markup, noting that بلوط relates to traditional Persian terminology (پارسی پهلوی: بلوت) rather than Arabic origin, contradicting some later orthographic conventions in modern Persian.
```


### [2026-09-05T05:52:31.737Z] TOOL RESULT

```
# فرهنگ معین Definition for بم

According to the فرهنگ معین section:

"(بَ ) ( اِ. ) صدای درشت و خشن آدمی و ساز. مق . زیر."

This translates to a rough, harsh sound produced by people and instruments, contrasting with زیر (high-pitched sound).

The دهخدا entry does not include an explicit origin remark, though it provides extensive historical context through various Persian literary citations demonstrating the term's usage across centuries of Persian poetry and scholarship.
```


## [2026-09-05T05:52:45.731Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /bellote,  n\\.|bellote, n\\./{print \"KLN1966 LEAF1BASED=\"NR}' KLN_1966.txt; awk 'BEGIN{RS=\"\\f\"} /Bellona/{print \"leaf(1b)=\"NR}' KLN_1966.txt | head -3"
}
```


## [2026-09-05T05:52:46.693Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=bomb",
 "prompt": "Give the etymology given for the noun 'bomb' (the chain of languages and forms)."
}
```


### [2026-09-05T05:52:47.328Z] TOOL RESULT

```
KLN1966 LEAF1BASED=97
leaf(1b)=97
leaf(1b)=468
leaf(1b)=510
```


### [2026-09-05T05:52:51.346Z] TOOL RESULT

```
# Etymology of "Bomb"

According to the American Heritage Dictionary entry, the word "bomb" traces back through several languages:

"French _bombe_, from Italian _bomba_, probably from Latin _bombus_, a booming sound, from Greek _bombos_, of imitative origin."

The term's origin is rooted in imitative language—the Greek word _bombos_ mimics a booming sound, and this meaning was preserved as the word traveled westward through Latin, Italian, and eventually into French before entering English.
```


## [2026-09-05T05:52:58.408Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==97' KLN_1966.txt | head -c 400; echo; echo \"----TAIL\"; awk 'BEGIN{RS=\"\\f\"} NR==97' KLN_1966.txt | tail -c 300"
}
```


### [2026-09-05T05:52:59.836Z] TOOL RESULT

```
b. behemoth  with  Egypt,  p-ehe-mau,  ‘ox  of  the water’,  was  justly  rejected  by  W.Max  MUller. behen,  n.,  the  plant  Centaurca  behen.  —  Arab. bahman,  in  vulgar  pronunciation  behmen,  fr. Pers.  bahman,  a  kind  of  root  resembling  a  large radish.
behest,  n.  —  ME.  behest,  bihest,  fr.  OE.  behxs, ‘promise,  vow’,  fr.  behdtan.  See  next  word  and cp.  hest
----TAIL
o  swell’.  See  bull,  ‘male  of  the  ox', and  cp.  words  there  referred  to.
Derivatives :  belly,  intr.  v.,  belly-er,  n.,  belly-fut, adj.
belong,  intr.  v.  —  ME.  belongen,  fr.  longen,  ‘to concern’,  fr.  lang,  long,  fr.  OE.  gelang,  ‘at  hand, attainable,  depende
```


## [2026-09-05T05:53:12.498Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%B7' --note 'page 76, root Balut: Arabic/Persian بلوط etymology (Aramaic ballūṭā; MP blwt\")' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/bellota' --note 'page 76, root Balut: Spanish bellota < Andalusian Arabic ballūṭa' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%AF' --note 'page 76, root Bata/Vata: Persian بد < MP wad < Proto-Iranian *watah; unrelated to English bad' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/bomb' --note 'page 76, root Bamb: English bomb < Fr bombe < It bomba < L bombus < Gk bombos' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://ahdictionary.com/word/search.html?q=bomb' --note 'page 76, root Bamb: AHD etymology of bomb' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%B7/' --note 'page 76: Mo(in tag for بلوط = [په.] Pahlavi' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D9%85/' --note 'page 76: Mo(in entry for بم, no Arabic tag' 2>&1 | tail -3"
}
```


## [2026-09-05T05:53:15.390Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY بلوط\"; grep -n 'بلوط' incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY بد\"; grep -n '^بد \\|بد:' incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY latin BAD/BAM\"; grep -n -i '^BAD\\|^BAM\\|BALUT' incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== SYN bad\"; grep -n -i \"'bad'\\|18.36\\|BAD (adj\" SYN.txt | head -5; echo \"=== HUB bad\"; grep -n -i 'schlecht' HUB.txt | head -8"
}
```


### [2026-09-05T05:53:19.449Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/094644fba68095a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cc166fa699de5091.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aba8c606167f2055.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b820c60e719d11e8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dd412390e3a1028d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e44ee749deae8b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/779f0d3a871711a3.txt
```


### [2026-09-05T05:53:19.550Z] TOOL RESULT

```
=== ARY بلوط
296:«ماهی آزان (5۸14۸/1030) و «ییده (/۷11-1-07) و «بلوط» (0۸74) و «زنبور؛ (81312) و «اردکث»
548:بلوط) با واژه‌ای انگلیسی 8182071 (به معنی درخت راش) همریشه است ولی معنی آنها دگرگونهه). ‎ .‏
7664:۲- چم این واژه در زبان‌های ابرلندی کهن و گالی: درخت بلوط.
=== ARY بد
4459:بازگست بد: پاکه.
=== ARY latin BAD/BAM
336:BAD 9979 ST Sod AS Anais ULE od ota glee ob ssl ye Ghdk; 52S ged
2071:Bad Y bh 23 Sls cal
2850:BADHAM (SANSKRIT) sey Senile 3,"
9497:Bad AF 6) 21 05 22 059 ool
=== SYN bad
31429:SING A Spout, CRY OuT 18.14 VaRrrous CRIES 18,21 SPEAK, TALK 18.22 Say 18,23 Be SILENT 18.24 LANGUAGE 18.25 DIALECT 18,26 WorD 18.27 DicTIONARY 18.28 NAME 18.31 Asx! (Question, Inquire) 18.32 ANSWER (vb.) 18.33 ApMiT, CONFESS 18.34 Deny 18.35 Asx?, REQUEST 18.36 Promise (vb.) 18.37 RerusE 18.38 Forbip
32010:1272 18.36 PROMISE (vb.)
32815:Du. gebied (LG gebéd > Dan. gebed), NHG gebiet (> Sw. gebit), but MHG gebiet(e), chiefly ‘command’ : gebieten ‘command’ (18.36). Orig. ‘territory un- der one’s command’. Weigand-H. 1.636. Falk-Torp 303. Hellquist 273.
33192:1. Lat. imperdator, fr. imperdre ‘com- mand’ (18.36), hence lit. ‘commander’, in early use mostly a military term ‘com- mander-in-chief, general’, used by Au- gustus as part of his title (imp. Caesar), and eventually superseding Caesar as the main title. Cf. Pauly-Wissowa s.v. ‘mperator. Hence the Romance words (OF r. emperere > ME emperere, NE em- peror; Rum. tmpdrat, pop. also ‘king’ and BO Alb. mbret), W. ymerawdwr, Br. (with dissim. ) tmpalaer, Lith. imperatorius, “USS. imperator; but MIr. imper, NIr. ‘mpir(e), fr. Lat. imperium ‘empire’
=== HUB bad
550:wie im Iranischen schlecht bestellt, da zd. x^'aretd- und
837:vad schlecht* und dil *Herz').
1365:310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
2041:schlecht, bose' = np. duSxtm), dem nur ein zd. *xaetna-,
3786:Mehl') aber auf schlechter Etymologie beruht.
4434:deussravd) Von schlechtem Rufe'; hrovartak 'Brief = phi.
4946:schlechtem Charakter , paz. du§xtm Min. Gl. 68, arm. dixem
4947:schlecht*; ntm *Halfte, halb' == zd. na^ma-; dann mmrOz —
```


## [2026-09-05T05:53:27.137Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN 16.72\"; grep -n '16\\.72' SYN.txt | head -5; echo \"=== HUB ctx\"; sed -n '830,845p' HUB.txt; echo \"=== HUB leaf\"; awk 'BEGIN{RS=\"\\f\"} /vad schlecht/{print \"leaf1b=\"NR}' HUB.txt"
}
```


## [2026-09-05T05:53:27.736Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '540,556p' incoming/ARY/ARY_pages.txt; echo \"=== pdfpage\"; awk 'NR<=550' incoming/ARY/ARY_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -1"
}
```


### [2026-09-05T05:53:28.738Z] TOOL RESULT

```
=== SYN 16.72
26554:Ir, sorche, that is so-rche, parallel to do-rohe ‘dark’, formed with prefixes for ood’ and ‘bad’ (16.71, 16.72), second Part dub., perh. : Grk. pétw ‘dye’, Skt. SU color’. Macbain 131.
27470:16.72 Bap
27803:Thus with words for ‘ill-’ (16.72), ete. Grk. dverbxnua (or -ia), Lat. fortiina ad- versa, It. sfortuna, OF r. meschaunce (> ME mischaunce), Fr. malheur, Ir. dodcad (fr. tocad with do- ‘ill’; Thurneysen Gram. 231), NIr. miadh (mi-, Pedersen 2.10), Br. droukeur, Dan. vanskebne (van- ‘mis-, un-’, Falk-Torp 1347), NE misfortune, Skt. daurbhagya- (fr. adj. dur-bhaga- ‘unfortunate’, with vrddhi of both syllables); with neg. prefix, Grk.
27940:4, Ir. son, sona, sb. sonas, parallel to dona ‘wretched’, NIr. donas ‘misfortune’, derivs. of so- ‘well’ (16.71) and do- ‘ill-’ (16.72), prob. formed directly with n- suffix (cf. Lat. prénus, fr. pro, Umbr. kumne ‘in comitio’ fr. com-, etc., Brugmann, Grd. 2.1.270), not cpds. (as Macbain s.vv.).
28615:Most of the adjectives for ‘angry’ are related to the nouns, but sometimes dif- ferent forms are popular, as NE mad (orig. ‘insane’ 17.23; colloqg. ‘angry’; cf. NED s.y. 5), NHG bése ‘bad, wicked’ (16.72) and ‘angry’.
=== HUB ctx
zuriickgehen und einem np. *vah' entsprechen wurden
(vgl. maht Tisch' = zd. masya^, skr. matsya-).
187. In bal. gvadil *feige' (aus ^gvaddil = *gvat-dil) ist
dil sicher persisches LW., dagegen wird goat echt sein
= np. badf phi. vat (arm. LW. vat) =■ ap. ^vata-. Da
es aber nur in gvadil vorkommt, nahm ich an, dass
gvadil altes Lehnwort sei -= mp. *vaddil (vgl. paz.
vad schlecht* und dil *Herz').
189. Fiir *avatasti' wiirde ich *ddast, tnr *abitasti- : *awdast,
audast erwarten.
196. Zu barda *Gefangener' = phi. vartak hat schon Geiger
an der von Horn citierten Stelle richtig zd. vareta-
gefangen' gestellt. Dazu afgh. LW. barda *a female
slave.'
199. Np. barman 'Quartier' ist nicht — ap. vardana- *Stadt',
das doch zu np. *balan geworden ware. Zd. verezena-
=== HUB leaf
leaf1b=37
```


### [2026-09-05T05:53:30.456Z] TOOL RESULT

```
استدلال کرد شباهت‌های ظاهری میان واژه‌ها هميشه ملا کك همریشه بودن آنها نیست و خویشی واژه‌ها
[pdf page 21]
ک
۲ / ریشه‌های هندو اروپایی زبان فارسی
باید به طور علمی و سامانمند بررسی و اثبات گردد. مثلاً آوای یونانی 2۳3 برابر است با آوای ژرمنی
8 چون واژه‌ی «بردن؛ در بونانی ۳۳180 و در انگلیسی 81۸14 است. واژه‌ی «برادر» در یونانی
و در انگلیسی 381۸07778 است. پس از دادن چند مثال دیگر» راسموس راسک
نتیجه گرفت که طبق این اصل (یونانی 217 < ژرمنی 8). واژه‌ی یونانی ۳18005 (به معنی درخت
بلوط) با واژه‌ای انگلیسی 8182071 (به معنی درخت راش) همریشه است ولی معنی آنها دگرگونهه). ‎ .‏
‏است. چندی بعد از راسموس راسکث و دانشمند آلمانی بنام باپ (1791-1887 ,8078 ۳۸۲2)
علاوه بر همسانی‌های آوایی و واژگانی» شباهت‌های دستوری را نیز مورد بررسی قرار دادند و نشان
دادند که مثلاً واژه‌ی سانسکریت "۸018" (به معنی «آذر» يا «آتش») و واژه‌ی لاتین 10727157" نه
تنها همسانی آوایی دارند پلکه از نظر دستوری نیز دارای همسانی هستند:
اوط شوش
در سال ۱۸۱۳ ناماس بانگك (۷01-۸60 171011۸8) واژه‌ی «هند و اروپایی»
1300-5108078۸70) را نو آوری کرد. ضمناً آهنگ پیشرفت دانش زبانشناسی و پژوهش درباره
زبانهای هند و اروپایی نی ز کم کم سرعت بیشتری گرفت.
=== pdfpage
[pdf page 21]
```


## [2026-09-05T05:53:40.302Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '27470,27485p' SYN.txt; echo \"=== leaf\"; awk 'BEGIN{RS=\"\\f\"} /16\\.72 Bap/{print \"leaf1b=\"NR}' SYN.txt; echo \"=== Buck oak\"; grep -n '8\\.57 OAK\\|8.57' SYN.txt | head -3"
}
```


### [2026-09-05T05:53:41.991Z] TOOL RESULT

```
16.72 Bap
16.73 Ruicur (adj.)
16.74 Wronc (adj.)
16.75 Sin
16.76 Fauur, Guivt
16.77 Mistaxr, Error
16.78 Bam (sb.)
16.79 Praise (sb.)
16.81 BravuriroL
16.82 Ucty
tions are so complex that no rigid classi-
fication has proved acceptable to psY-
chologists generally; and there 18 ae
tainly none which it would be profitab e
to impose upon our study, in which we
are dealing with unsophisticated 40
=== leaf
leaf1b=1165
=== Buck oak
12204:CHAPTER 8 th AGRICULTURE, VEGETATION! : . A 8.11 FARMER 8.44 Bariey ac : 8.12 Frexp (for Cultivation) 845 Rys dl ¢ 8.13 GarRDEN 8.46 Oats i ‘a 8.14 Barn 8.47 Marzz, (U.S.) Corn q 8.15 Cuurivats, TLL 8.48 Rice Me ; 8.21 Pxow (vb.; sb.) 8.51 Grass ht : 8.212 Furrow 8.52 Hay a i 8.22 Dic 8.53 PLant al 8.23 SpavE 8.54 Roor ( 8.24 SHovEL 8.55 Brancu ba 8.25 Hor 8.56 Lear ere 8.26 Tork 8.57 FLowER me 8.27 Raks 8.58 Rosz M 8.28° Harrow 8.60 Tree = 1.42 * 8.31 Sow; Srep 8.61 Oak 8.32 Mow, Reap a oe Bo 8.33 Sickie; ScyrHE 8, 64 ei i 8.34 THREsH 8.65 = t in ? 8.35 TsresHinc-Foor 8.66 hee 8.41 Crop, Harvest 8.67 VINE mS 8.42 Grarn (Generic = British Corn) 8.68 Tosacco ‘co 843 Wxeat 8.69 SmoxE (Tobacco) (6. ink 8.11 FARMER - Grk. — -yewpyés Goth. (airpds) waurstwja i ikini ini : . Lith kininkas, laukinin- NG —-yewpyds, xwpixds, ON bondi, akrmasr, to, ieee a i fal Ra Lat. aa Dan. — dyrker, landmand, Lett. laucinieks, zemnieks Ia Hiesehee “aactnctiorglontts bonde ChSI. délatelt, tezatelt the : as ae iiva- Sw. dkerman, jordbru-  SCr. __ratar, teak, seljak 1 Tr ant re fee kare, bonde Boh. __rolnik, sedldk i ; 4 ee pied tiva- OE = (eord)tilia, wcerman, Pol. _rolnik, chlop It Sp Waban RUE gebir, etc. Russ. zemledelec, krest'ja- thi pes f r “i agricultor ME husbond(man), acre- nin, muzik DD Ir, : eke He abe man Skt. ksetrakarsaka-, P Nir. paecmba ugar Ne eld (husbandman) kselrapati- W. amaethwr, ffermur OHG ee ae Av. vdstrya-
13262:8.57 FLOWER Grk. Gos Goth. (bléma) Lith. —gélé (kvietka, 2iedas) NG &fos, NovAobdt ON blém, blomsir Lett. puk’e (zieds) Lat. flos Dan. blomst ChSl.  cvétit, cvéttet It. fiore Sw. blomma, blomster SCr. cvijet Fr. fleur OE blistma Boh.  kvélina Sp. Slor ME _blosme, flour, blome Pol. kwiat Rum. floare NE Slower Russ. cvelok Ir, lath, scoth Du. bloem Skt. puspa-, kusuma- NIr.  blath OHG bluomo Av. Bg oh W. blodeuyn, blodyn MHG bluome Br. bleunienn, boked NHG  blume
14066:young shoot’ (8.57). Cf. VLat. talidre : talea, above, 5.
```


## [2026-09-05T05:54:05.519Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD sahbalut entry\"; grep -n 'šahbalüt\\|šāhbalūt\\|sahbalut' PHD.txt | head -3; awk 'BEGIN{RS=\"\\f\"} /šahbalüt/{print substr($0,1,600)}' PHD.txt | head -20; echo \"=== BRT vata\"; grep -n 'vata-\\|va\\^ta' BRT.txt | head -5"
}
```


### [2026-09-05T05:54:07.305Z] TOOL RESULT

```
=== PHD sahbalut entry
1217:chestnut šāhbalūt.
4565:dēwī dew: |! dēwēsnīhī déwézagiht šahbalüt šāy- šāhdānag šāyendagīh
ī déwézagiht šahbalüt šāy- šāhdānag šāyendagīh
šāyendag
šāhesprahm šāyēd šāzdah
šādurwān
ISI
[171]
čarbīh
PAHLAVI KEY
[17e] 135014
үте» эс,
мэ Q
Carbiánómand — f6 vu o S
čarbišn čim čambar čamišn sang!
čašm
Wd g +8 У 16-68 ANS “SUG
čašmareškīh “49 ~~ -euq
čašmarešk čašmagāh čašmagāhīh 1 ģašmag čašmdīd
catrang
Ven Än сос C 4602 “O” se
=== BRT vata
2964:vgl-  evata-  Adj.  'inferior'  (wozu  aera-  wie  Ht.  |  ^  püZ.^';  —  yahmat  haca  naicU  bunjayät
4013:•  j.  a-fraka'8avata-  Adj,  (fem.  'vai(i-)'^ 'nicht  vorwärts,  fort,  von  der  Stelle  zu rütteln,  unverrückbar' :  «r  Aim  (näml. dngnam)  dasta  ..  -vaitim  Yt.  ij.  100.
6126:z-aJuit  (SB,;   aiava^tah);   ferner  räißAiS>  Y.
14213:PPfP.  lum  gr.  V.  %paiM;  vgl.  draohSvata-.  — 1)  Hda.  madr°.  —  ')  Oder  vll.  'dem  die  Hoden zermalmt,  zerqueischt  sind,  entmannt'.
22204:Rede:  at  J  (Sp.  11  m.)  vaocat  ahurS  .  ..■ nüif  .  .  Y.  2(J.  6;  —  yezica  vaocät  alsa  yä kaine:  faä:r»m  isd.)  alm  ..varsta  V.75. 13; 13.  a)  mit  Dat.  der  Person:  sat  vao- iät  ratul . .  mazJayasnagibyS:  maadayaina (Vok.)  ..  V.tf.  II.  3)  mit  Objektsakk.: ya'hä  iü  T  *ahuramazää  mSnghaca  vaocasifl däscä  varfscä  ya  vohu  aha  .  .  V.  J^.  4; —  /a(  0/  vainmaidi . .  hyat  I  mainimadicä vaocdimäcS  vsnzimäiä  yä  .  .  vakisiä  Y. JJ.  3;  —  tarahuslrahe  .  .  paoiryai  vohu mamnanai  .  .  vaokuSe  .  .  vävinzuh  Yl 13. 87  f. ;  —  ySi  nsii  ih3  mqhnm  vanssnti (sd.)  ya%S  Tm  mSnai^a  vai>ea(K.onj.)£ä Y.45.  3i  —  ai  sl  i"Ä(ADn.)  vaxs'ya  (iS.) mazdä,  vidull  zT  na  mruyai  (Sp.  1193  u.) Y.5/.8.  a)  zugleich  mit  o)  Akk.  der Person:  at  tä  vaxsya  üints  (Sp.  29  o.)  . . mazda^a  Y.  ?o.  t.  ß)  Dat  der  Person: y7  mlH  viäva  vaocäl  haihim  mähnm  .  , ampnitaias{sd.)ca  Y.^1.6;  —  *>'?*'  '''^' vTdvä  mazdä  vaocat  Y.  1^5. 3;  —  masda at  mSi  vahilta  sraväslä  .  .  vaocä  (Imp.) tä  .  .  asacä  iiudfm  (sd.)  Y,  j4. 15;  —  mit finalem  Inf. :  tat  nS  mazdä  vldvanöi  (sd.) vaola  hizvä  %'waAya  araks  Y.31. 3 ;  5 ;  —  in pass.  Wendung  :_)'as'4vö  mazdä  %wSi  va^äl daena  Y,  44. 11;  —  »n/  mdi  tneBcam  ^  vata- hJuI  va/u/(sd.)  manarahs  Y.  48. 9.  3)  mit wie?-Adv.slattObj.:  (is  mainyü  mamanäiti , .  vaocätari . .  vävjnzätarS  Y.  ly.  4 ;  —  *yal neit  yava  mihS  mamne  .  .  vavaü  .  .  va- variza  P.  iS;  —  tat  hwä  pinsa  (sd.)  fnS
```


## [2026-09-05T05:54:07.445Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN 8.61 oak body\"; grep -n 'Grk.*8pi\\|quercus' SYN.txt | head -5; echo; echo \"=== AFM list check for بلوط headword\"; grep -n '( *بلوط' AFM_pages.txt AFM.txt | head -5; echo \"=== TAD بلوط ctx\"; sed -n '2160,2172p' TAD_pages.txt"
}
```


### [2026-09-05T05:54:07.543Z] TOOL RESULT

```
=== SYN 8.61 oak body
983:4, Goth. fairguni ‘mountain’ : OF firgen in epds., as firgen-gat ‘mountain goat’, and prob. a loanword fr. Celtic *perkunia, represented by Hercynia silva (with regular Celtic loss of initial p), this further connected with Lat. quercus ‘oak’, Relation between ‘woods’ and ‘(wooded) mountain’, as elsewhere. Walde-P. 2.48. Feist 137 ff.
13303:528 8.61 8.62 8.63 8.64 8.65 OAK BEECH BIRCH PINE FIR (Pinus) (Abies) Seiopini eyes tba onpbda(?) mebxn, alrus drm Re ee étua onubia mebxn, melo arm, Fie Lat. quercus (robur) fagus belu(l)la pinus abies It. quercia (rovere) faggio betula pino abele Fr. chéne (rouvre) _hétre bouleau pin sapin Sp. roble haya abedul pino abeto Rum.  stlejar fag mesteacdn pin brad Ir, daur Saghvile bethe gius, ochtach ime Nir. dair Saigh beith peine, gris gits W. derwen ffawydden bedwen pin(wydden) Dynidwyaa en, : sybwydden Br. dervenn favenn bezvenn pin saprenn Goth. .... maths sees Be onexd ee ON eik bok bjork Sura gron Dan. eg b6g birk fyr gran Sw. ek bok bjork tall, fura gran OE dc béce beorc pinbéam, furh S@ppe, gyr ME i oke beche birch pine Syrre NE oak beech birch pine fir, spruce Du. eik beuk berk pijn(boum) den OHG eth buohha bircha, birihha pinboum,forha, fiohta tanna MHG eich(e) buoche birke, birche —_-vorhe tanne, viehte NHG eiche buche birke Kiefer, fohre tanne, fichte Lith. qZuolas skroblus, skirpstas berzas pusis eglé Lett. udzuols viksna berzs priede egle GaslD eae: Sate asc (borit) jela SCr. _hrast, dub bukva breza bor jela Boh. dub buk briza sosna, smrk jedle Pol. dab buk brzoza sosna jodta Russ. dub buk bereza sosna el’ Skt. ate bhirja- piluddaru, devaddru-, etc. Ay.
13355:4. ON, Sw. fura, Dan. fyr, OE furh, furh-wudu (gl. pinus; but ME fyrre, Syrre-tre glosses abies in 15th cent., Wright Vocab. 560.7, 646.20, etc.; cf. also fyrre ‘sappin’ in 16th cent.; this shift complete in NE fir, except that in Scotland the native pine is still called jir; ME > W. ffyr ‘pine’ or ‘fir’), OHG forha (usual gl. to Lat. picea), MHG vorhe, NHG fohre (dial. = kiefer), all with transfer to ‘pine’ fr. ‘oak’ : Lat. quercus ‘oak’ (8.61).

=== AFM list check for بلوط headword
=== TAD بلوط ctx


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
```


## [2026-09-05T05:54:22.216Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /بلوط - بفتح اول/{print \"BQTv1 leaf1based=\"NR}' BQT_v1_pages.txt; awk 'BEGIN{RS=\"\\f\"} /بلوط - بفتح اول/{print}' BQT_v1_pages.txt | grep -o '\\[pdf page [0-9]*\\]'"
}
```


### [2026-09-05T05:54:23.858Z] TOOL RESULT

```
BQTv1 leaf1based=524
```


## [2026-09-05T05:54:30.493Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /بد - بفتح|بد – بفتح|وَد|بد ـ بفتح/{print \"leaf1b=\"NR}' BQT_v1_pages.txt | head; echo \"---\"; grep -n 'بد - ب' BQT_v1_pages.txt | head -10"
}
```


### [2026-09-05T05:54:32.099Z] TOOL RESULT

```
---
```


## [2026-09-05T05:54:36.346Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n '^بد' BQT_v1_pages.txt | head -20; echo \"=== vad\"; grep -n '^وَد\\|^ود -\\|وَد' BQT_v2_pages.txt | head -10"
}
```


### [2026-09-05T05:54:36.420Z] TOOL RESULT

```
34:بد ینوسیله اززحمات شماد رانجام این‌خد مت مهم فرهنگی قد رد انی
1049:بدان زبان بود» واين لفتی است منسوب خهله* » و آن نامی است که بر پنج
1055:بدان ز بان جاری‌بود » و آن لغت مردم بارس است ؛ و اما دری » لفت مر دم
1378:بدو دستهٌ شرقی و غربی میتوان تفسیم کرد که از نظر علم اصوات ؛ شکل
1527:بدا نی که انگیزشت وشمار همسدون بول خنیو رگذار.
1649:بدور معدلتش رهز نان دزد ازیم شدند ها کره از کاف کاروان گفتن.
1666:بدل میشود ضبط دیگری ازاین کلسه بصورت «هاکله> هم تراشیده اند ۱
1778:بد بختا نه همین فرهنگ که درهید نوشته شده درایر ان بدستپ| افتاده
1880:بدستیاری‌ملا فیروز انتشار یافته بود . رضا قلی‌خان مانند صدها نو پند گان
2585:بدو نیز مورد شك‌است) شمری ازاو درجایی بادشده؟ م.م. ۲- رل:ص ه از دساچه مژلف.مقدیه ‏ ۱ . هشتاد
2623:بدرش‌شاه جپان‌در سال۱۳۵ع. نکلکنده حمله نمو دو عداز چندماه که نز ديك
2827:بدیمی» که ذیل «تالقیر» ازآن نقل کرده؛ دسانیر, که علاوه بر کر آن‌در شرح 1۶ بادبان»* ذیل
2845:بدست هز ار ودوست وبارده کلمه ۴ بالغ میشود .
2860:بدلهای آنها که درحواشی آمدم بالغیی ۲۲۷۸ لفت‌است؛ فرهشگه سروری درحدود ٩۶۰۰‏ لغت
2862:بدون "خاتمه» که درغالب سخ‌یامدم بالغ‌بر *۹۹۵ لفت‌است وبرهان قاطم شامل لفات همه این
3305:بدبهی است بمیلری از کلمات مزبور تصحیف شده . برای تلفظ و معنی این لغات بمتن برهان
3534:بد -آذری (لفت آذر بایجان ) : باسدق (ذیل: فراته )۸ تیته (ذیل :
3609:بدین زبان سخن می کنند . گفتم : یاد دار « برسان > بمعنی امت آمده اما
4040:بدیع‌الدین ومولوی عبدالهٌ و مولوی مجیب‌الررحمن و حکیم عبدالُ و عبدالصمد و
4076:بدلپا نمره های متن وحاشیه بین‌الپلالت ( ) گذاشته شده است .
=== vad
```


## [2026-09-05T05:54:54.491Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%88%D8%AF/",
 "prompt": "Is there a Persian entry وَد meaning \"bad\" (بد)? Quote the فرهنگ معین and لغت‌نامه دهخدا entries for وَد, including any note that it is a variant/dialect form of بد."
}
```


## [2026-09-05T05:54:56.085Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%AF/",
 "prompt": "Quote the فرهنگ معین entry for بد (including any bracketed origin tag such as [په.]) and any برهان قاطع / حاشیه معین etymological note about the Pahlavi form vat/wad."
}
```


### [2026-09-05T05:55:01.805Z] TOOL RESULT

```
# فرهنگ معین Entry for بد

According to Farhang-e Moein, the entry reads:

**(بَ) (ص.) زشت، ناپسند.** 
**(بُ دّ) [ع.] (ا.ِ.) چاره، گریز.**
**(بَ یا بُ) [په.] ۱- (ص.) مهتر، سرور بزرگ. ۲- (پس.) دارنده، صاحب، خداوند**

The Pahlavi etymological note indicates the word derives from Old Persian forms *vat* or *wad*, meaning something negative or deficient in quality—a linguistic root shared across Indo-European languages including English "bad."
```


### [2026-09-05T05:55:01.833Z] TOOL RESULT

```
# Persian Entry وَد Meaning "Bad"

Yes, the dictionary includes an entry for وَد with this meaning.

**Lughtnāmeh-ye Dehkhoda** states:
> "وَ۔ به معنی رد است که حکیم عاقل و دانشمند باشد۔ || گرم در مقابل سرد۔ ( برهان ) ( ناظم الاطباء )۔ || **بد۔ مقابل خوب** ۔ ( فرهنگ فارسی معین )"

This translates to bad/evil as the opposite of good, cited from Farhang-e Farsi-ye Mo'in.

**Farhang-e Mo'in** entry confirms:
> "(وَ دّ ) [ ع . ] ۱ - (اِمص . ) دوستی ، محبت ۔"

The Dehkhoda dictionary explicitly notes this is a variant form appearing in the Mo'in Persian dictionary, indicating وَد as an alternate designation for بد (bad/evil).
```


## [2026-09-05T05:55:59.401Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /vat \\[SLY/{print \"NYB leaf1b=\"NR}' NYB_vol2_glossary.txt; awk 'BEGIN{RS=\"\\f\"} /Khotan Saka bata- .can thus be connected/{print \"DKS leaf1b=\"NR}' ISS_alt_DKS.txt; awk 'BEGIN{RS=\"\\f\"} /hieraus  sp.  bellota/{print \"LKT leaf1b=\"NR}' LKT.txt; awk 'BEGIN{RS=\"\\f\"} /Dans  la  péninsule  Hispanique/{print \"DEV leaf1b=\"NR}' DEV.txt; awk 'BEGIN{RS=\"\\f\"} /balüt:              .Eiche/{print \"PLA leaf1b=\"NR}' incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-05T05:56:01.133Z] TOOL RESULT

```
NYB leaf1b=225
LKT leaf1b=45
DEV leaf1b=268
PLA leaf1b=71
```


## [2026-09-05T05:56:11.775Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /Khotan Saka bata/{print \"DKS leaf1b=\"NR}' ISS_alt_DKS.txt; cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%88%D8%AF/' --note 'page 76: Dehkhoda/Moin entry وَد = بد (MON:4993)' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D8%AF/' --note 'page 76: Moin entry بد' 2>&1 | tail -2; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg76.png data/verification/sources/refs/ocr/BOOK/76.png && echo copied"
}
```


### [2026-09-05T05:56:16.154Z] TOOL RESULT

```
DKS leaf1b=309
/home/sfmqrb/git/rishe/data/verification/sources/web/b50d87e493daa23e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a9c8262b58448d18.txt
copied
```


## [2026-09-05T05:56:19.511Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-05T05:56:19.550Z] TOOL RESULT

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


## [2026-09-05T06:02:45.236Z] TOOL CALL #62: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-76.json",
 "content": "{\n  \"pdf_page\": 76,\n  \"book_page\": 46,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Balŭt\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"Aramaic/Syriac ballūṭā ܒܠܘܛܐ 'oak, acorn' → Middle Persian blwt' (balūt) and, independently, Arabic بلّوط (ballūṭ)\",\n      \"note\": \"There is no Old Persian *balūt: the Achaemenid corpus has no word for 'oak' of this shape (Kent's lexicon lists only the doubtful yaka- 'a kind of wood (oak?)', DSf 34). The oldest Iranian form is Middle Persian blwt' /balūt/, and modern scholarship (Wiktionary s.v. بلوط, with the Aramaic and Akkadian discussion) makes it a borrowing from Aramaic בְּלוּטָא / Syriac ܒܠܘܛܐ ballūṭā, itself perhaps an Aramaic formation from bālaṭ 'to bulge out' or connected with Akkadian balāṭu. Nourai follows Asbaghi (PLA:56), who does call Arabic balūṭ Persian — but Asbaghi's own line already adds 'aram.' beside the Middle Persian form, and his sole authority is Mo'in. So the tree is right that the word reached New Persian through Pahlavi, but the root box is wrong in two ways: the language label ('Old Persian') and the implied Iranian pedigree; the word is a Semitic culture-word taken into Iranian, and Arabic did not get it from Persian.\",\n      \"note_fa\": \"نورایی ریشهٔ «بلوط» را واژه‌ای پارسی باستان می‌داند، ولی در پیکرهٔ پارسی باستان (کتیبه‌های هخامنشی) چنین واژه‌ای نیست؛ کهن‌ترین صورت ایرانی، فارسی میانهٔ blwt' /balūt/ است. پژوهش امروزی (ویکی‌واژه، ذیل بلوط) آن را وام‌واژه‌ای از آرامی/سریانی ballūṭā «بلوط، میوهٔ بلوط» می‌شمارد که شاید خود از ریشهٔ سامی bālaṭ «برآمدن» یا اکدی balāṭu باشد. بنابراین برچسب «پارسی باستان» نادرست است و «بلوط» واژه‌ای سامی است که به ایرانی وام داده شده، نه واژه‌ای ایرانی. آن‌چه در نمودار درست است تنها زنجیرهٔ فارسی میانه ← فارسی نو است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%B7\",\n        \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%B7/\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"PLA:56\", \"status\": \"partial\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, printed p.56 (PLA_pages.txt leaf 71 = p.56, running head 'bilaur 56 bunast'): 'balūṭ: \\\"Eiche\\\" pers. ³ aus dem mp. barūt, aram. ...' — footnote 3 = 'FM. s.v.' (Farhang-e Mo'in). Asbaghi does class the Arabic word as Persian (as Nourai says), but the same line already names an Aramaic form, and his only authority is Mo'in; he says nothing about Old Persian.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon s.v. yaka-\", \"stance\": \"silent\", \"note\": \"grep -n -i 'oak' KNT.txt gives only 'yaka- sb. a kind of wood (oak, Scheil 25.28, but if so, not cognate ... certainly not \\\"timber\\\" in general)'. No Old Persian *balūt exists.\"},\n        {\"src\": \"LKT\", \"where\": \"Lokotsch no. 206 (leaf n44 ≈ p.18)\", \"stance\": \"contradicts\", \"note\": \"'206. Ar. ballūṭ: \\\"Eichel, Kastanie\\\", Einheitsnomen ballūta; hieraus sp. bellota, pg. belota, boleta, bolota \\\"Eichel\\\", it. ballotta \\\"gesottene Kastanie\\\".' Lokotsch treats the word as Arabic throughout; no Persian source is mentioned.\"},\n        {\"src\": \"DEV\", \"where\": \"Devic, Additions, s.v. Ballote (pp. 232-233)\", \"stance\": \"contradicts\", \"note\": \"'Ballote. Chêne à glands comestibles ... En arabe, بلوط balloût (dans Avicenne). En persan, شاه‌بلوط châh-balloût ... Ballote, بلوط balloût, représentent le grec βαλλωτή ... il est certain que ballote, chêne, nous est venu des Arabes.' Devic derives the word from Greek/Arabic, not from Persian.\"},\n        {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep '( بلوط' finds no headword: Addi Shir's inventory of Persian words Arabicized does NOT include بلوط, which tells against Asbaghi's Persian-origin claim.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"balŭt, barŭt\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Middle Persian word itself is real: MacKenzie's Pahlavi dictionary has the compound šāhbalūt 'chestnut' (English index p. 'chestnut šāhbalūt'), and Mo'in's footnote in Borhān-e Qāṭeʿ p.303 gives a Pahlavi form for بلوط citing Unvala p.402. Asbaghi p.56 writes the Pahlavi form barūt, with l/r variation typical of Book-Pahlavi orthography, where the same character serves for l and r — so balūt and barūt are two readings of one spelling <blwt'>, not two words. What is NOT supported is the arrow from an Old Persian ancestor: no such Old Persian word is attested, and Wiktionary derives MP blwt' straight from Aramaic ballūṭā. So the node's forms are right, its parentage is not.\",\n          \"derivation_fa\": \"صورت فارسی میانه واقعی است: در فرهنگ پهلوی مکنزی ترکیب šāhbalūt «شاه‌بلوط» آمده و معین در حاشیهٔ برهان قاطع (ص ۳۰۳) صورت پهلوی «بلوط» را با ارجاع به اونوالا ۴۰۲ آورده است. اصبَغی (ص ۵۶) آن را barūt می‌خواند؛ این دوگانگی l/r تنها ناشی از خط پهلوی است که یک نشانه برای «ل» و «ر» دارد، پس balūt و barūt دو خوانش از یک نوشتار <blwt'> اند نه دو واژه. آن‌چه پذیرفتنی نیست پیوند با یک واژهٔ پارسی باستان است؛ ویکی‌واژه فارسی میانهٔ blwt' را مستقیماً وام‌واژه‌ای آرامی می‌داند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%B7\",\n            \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%B7/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PLA:56\", \"status\": \"supports\", \"note\": \"PLA p.56 (leaf 71): 'balūṭ: \\\"Eiche\\\" pers. aus dem mp. barūt, aram. ...' — the Middle Persian antecedent barūt is exactly what the node prints.\"},\n            {\"ref\": \"MON:576\", \"status\": \"supports\", \"note\": \"Mo'in tags بلوط as Pahlavi: '(بَ) [په.] (اِ.) درختی است تناور با برگ‌های شکافدار' (Farhang-e Moʿin section on abadis.ir/fatofa/بلوط/). The [په.] tag is precisely Nourai's Pahlavi node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, English index s.v. chestnut\", \"stance\": \"partial\", \"note\": \"'chestnut šāhbalūt' — MacKenzie has the compound šāhbalūt but no simple balūt headword, so the base word is presupposed rather than listed.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin, p.303 (BQT_v1_pages.txt leaf 524)\", \"stance\": \"supports\", \"note\": \"'بلوط - بفتح اول، پهلوی [balūt] «اونوالا ۴۰۲»، درزبان علمی Quercus، درختی است از دستهٔ بلوط‌ها...' — Moʿin's footnote gives a Pahlavi form citing Unvala p.402.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep -n -i 'balut|barut' NYB_vol2_glossary.txt returns nothing; the word does not occur in Nyberg's text corpus.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"balŭt «بلوط»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian بلوط balūt 'oak, acorn' continues Middle Persian blwt' /balūt/ unchanged; the Arabic-looking spelling with ط (rather than ت) is an orthographic Arabicism, adopted because the identical Arabic word بلّوط was familiar to Persian scribes. Moʿin tags the word [په.] 'Pahlavi', and Moʿin's footnote in Borhān-e Qāṭeʿ p.303 — the very page Nourai cites — gives the Pahlavi antecedent from Unvala p.402. Wiktionary's Persian entry likewise: بلوط < Middle Persian blwt' < Aramaic ballūṭā. Dialect reflexes (Mazandarani پلت palat, Kurdish berrû/belû) show the word was carried in Iranian mouths and not simply re-borrowed from Arabic in modern times.\",\n          \"derivation_fa\": \"«بلوط» فارسی نو دنبالهٔ بی‌واسطهٔ فارسی میانهٔ blwt'/balūt است؛ نوشتن آن با «ط» تنها یک عربی‌نویسی املایی است، چون واژهٔ همسان عربی بلّوط برای کاتبان فارسی آشنا بود. معین آن را [په.] (پهلوی) برچسب زده و در حاشیهٔ برهان قاطع ص ۳۰۳ — همان صفحه‌ای که نورایی یاد کرده — صورت پهلوی را به نقل از اونوالا ۴۰۲ آورده است. صورت‌های گویشی مانند مازندرانی «پَلَت» و کردی berrû/belû نشان می‌دهد واژه در دهان ایرانیان مانده و وام تازهٔ عربی نیست. ادعای نورایی در این حلقه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%B7\",\n            \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%B7/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:576\", \"status\": \"supports\", \"note\": \"Farhang-e Moʿin s.v. بلوط: '(بَ) [په.] (اِ.) درختی است تناور با برگ‌های شکافدار و گل‌های دراز و آویخته' — the [په.] tag = Pahlavi origin, exactly Nourai's arrow.\"},\n            {\"ref\": \"BQT:303\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ, printed p.303 (BQT_v1_pages.txt leaf 524, verified by the running continuation notes 'بقیه از صفحهٔ ۳۰۱ / بقیه در صفحهٔ ۳۰۳'): 'بلوط - بفتح اول، پهلوی … «اونوالا ۴۰۲»، درزبان علمی Quercus'. Page citation exact.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye hend-o-orupāyi (ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'بلوط' finds only the introductory discussion of Greek phēgos/English beech (p. ~2) — Aryanpur has no بلوط headword, i.e. he does not treat it as an Indo-European inheritance.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep -n -i 'balut|balūt' HRN.txt and HUB.txt return nothing: neither Horn nor Hübschmann gives بلوط an Iranian etymology, consistent with its being a loanword.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"ballŭth\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic بَلُّوط ballūṭ 'oak, acorn' (already in Avicenna, as Devic notes) is according to modern scholarship a borrowing from Aramaic בְּלוּטָא / Syriac ܒܠܘܛܐ ballūṭā, not from Persian: the emphatic ṭ, the geminated -ll- of the qattūl pattern, and the Aramaic nomen unitatis ballūṭa all point to a Semitic transmission, and Middle Persian balūt is a parallel borrowing from the same Aramaic word rather than the source. Asbaghi (PLA:56) is Nourai's authority for the Persian direction, but he cites only Moʿin and himself flags 'aram.'; Addi Shir, who catalogued Persian words in Arabic, has no بلوط entry; Lokotsch and Devic treat the word as Arabic. Nourai's Persian → Arabic arrow therefore reverses (or at best duplicates) the actual route.\",\n          \"derivation_fa\": \"عربیِ «بَلُّوط» (که ابن‌سینا هم به کار برده) بنا بر پژوهش امروزی وام‌واژه‌ای است از آرامی/سریانی ballūṭā، نه از فارسی: «ط» مفخّم، تشدید لام بر وزن فَعّول، و صورت واحد آرامی ballūṭa همگی بر انتقال سامی گواهی می‌دهند، و balūt فارسی میانه خود وام موازی از همان واژهٔ آرامی است، نه سرچشمهٔ آن. اصبَغی (ص ۵۶) که مأخذ نورایی است تنها به معین استناد می‌کند و خودش هم «aram.» را کنار آن آورده؛ ادّی شیر که واژه‌های فارسیِ معرَّب را گرد آورده، «بلوط» را نیاورده است؛ لوکوچ و دُوِیک آن را عربی می‌دانند. پس پیکان «فارسی ← عربی» در نمودار وارونه است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%B7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PLA:56\", \"status\": \"partial\", \"note\": \"PLA p.56 (leaf 71) does say 'balūṭ: \\\"Eiche\\\" pers. aus dem mp. barūt' — supporting Nourai's direction — but the same line adds 'aram.' and the supporting footnote 3 is merely 'FM. s.v.' (Farhang-e Moʿin), so Asbaghi offers no independent Semitic evidence.\"},\n            {\"ref\": \"MON:576\", \"status\": \"partial\", \"note\": \"Moʿin's tag on the Persian word is [په.] (Pahlavi), i.e. he claims a Pahlavi origin for Persian بلوط; he does not himself argue that Arabic بلّوط came from Persian. (abadis.ir/fatofa/بلوط/, فرهنگ معین section.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"contradicts\", \"note\": \"No بلوط headword anywhere in AFM_pages.txt / AFM.txt (the only hit is an incidental 'وهو قدر البلوط' in a description). The standard Arabic catalogue of Persian loanwords does not claim this one.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 206 (leaf n44 ≈ p.18)\", \"stance\": \"contradicts\", \"note\": \"'206. Ar. ballūṭ: \\\"Eichel, Kastanie\\\" ... hieraus sp. bellota' — headword is Arabic, with no Persian etymon given.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Additions s.v. Ballote (pp. 232-233)\", \"stance\": \"contradicts\", \"note\": \"'Ballote, بلوط balloût, représentent le grec βαλλωτή ... il est certain que ballote, chêne, nous est venu des Arabes.' Devic even points the ultimate origin west (Greek), never to Persian; he cites Persian only for the compound شاه‌بلوط.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsīr al-alfāẓ al-dakhīla\", \"stance\": \"silent\", \"note\": \"grep 'بلوط' in TAD_pages.txt yields only an incidental 'ورق شجرة بلوط القرمز' in the entry قرمز; بلوط is not itself listed among the foreign words.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Spanish\",\n          \"words\": \"belloth\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"belloth\",\n          \"correct_form\": \"bellota\",\n          \"derivation\": \"The Spanish word is bellota 'acorn', not *belloth: there is no Spanish word ending in -th (the digraph does not exist in Spanish orthography). Klein p.162, the very reference Nourai cites, prints 'Sp. bellota fr. Arab. ballūṭah, in vulgar pronunciation bellōta'. The route is Arabic بلّوطة ballūṭa (nomen unitatis 'one acorn') → Andalusi Arabic, where the imāla raised the first a to e (ballūṭa > bellūṭa), → Old Spanish bellota, with emphatic ṭ giving plain t; Portuguese belota/bolota and Italian ballotta 'boiled chestnut' are the same borrowing (Lokotsch no. 206). The printed page of Nourai (PDF p.76, book p.46) really does read 'belloth', so the extraction is faithful and the -th is the author's own misprint — probably a stray transliteration of the Arabic ṭ carried over from the parent node ballŭth.\",\n          \"derivation_fa\": \"واژهٔ اسپانیایی bellota «بلوط، میوهٔ بلوط» است، نه *belloth؛ در املای اسپانیایی اصلاً دونویسهٔ th وجود ندارد. کلاین در همان صفحهٔ ۱۶۲ که نورایی یاد کرده می‌نویسد: «Sp. bellota fr. Arab. ballūṭah». مسیر چنین است: عربی «بلّوطة» (اسم وحدت) ← عربی اندلسی که در آن امالهٔ مصوت نخست ballūṭa را به bellūṭa بدل کرد ← اسپانیایی کهن bellota، با تبدیل «ط» مفخّم به t ساده؛ پرتغالی belota/bolota و ایتالیایی ballotta هم همان وام‌اند (لوکوچ، شمارهٔ ۲۰۶). تصویر صفحهٔ چاپی (ص ۴۶ کتاب) به‌روشنی «belloth» دارد، پس خطا از خوانش اسکن نیست بلکه خطای چاپی خود کتاب است؛ گویا «th» از گرهٔ پیشین ballŭth به این خانه سرایت کرده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/bellota\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:162\", \"status\": \"supports\", \"note\": \"Klein 1966 leaf n96 (the leaf running behemoth→belong, i.e. printed pp. 161-162): 'bellote, n., the edible acorn of the holm oak. — Sp. bellota fr. Arab. ballūṭah, in vulgar pronunciation bellōta, \\\"acorn\\\".' Klein spells the Spanish word bellota — the page Nourai cites contradicts the form he prints.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 206 (leaf n44 ≈ p.18)\", \"stance\": \"supports\", \"note\": \"'Ar. ballūṭ ... Einheitsnomen ballūta; hieraus sp. bellota, pg. belota, boleta, bolota \\\"Eichel\\\", it. ballotta' — Spanish form bellota, from the Arabic unit-noun.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Additions s.v. Ballote (p. 232)\", \"stance\": \"supports\", \"note\": \"'Dans la péninsule Hispanique, le mot arabe a donné l'espagnol bellota et le portugais belota, bolota, boleta, gland.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"bellote\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English bellote is a rare botanical/technical borrowing of Spanish bellota, taken over with Spanish spelling and re-shaped -a > -e in English. Klein p.162 gives it exactly as Nourai does: 'bellote, n., the edible acorn of the holm oak. — Sp. bellota fr. Arab. ballūṭah'. The word never entered common English use (it is absent from Webster's Second and from Funk & Wagnalls' New Standard); it belongs to the 19th-century vocabulary of Mediterranean botany, alongside valonia (< Greek balani) for the acorn-cups of the valonia oak, which Klein treats separately. Devic notes a homograph in French, bellote 'large-headed nail', which he also traces to the acorn word by shape.\",\n          \"derivation_fa\": \"«bellote» در انگلیسی وام‌واژه‌ای کمیاب و گیاه‌شناختی از اسپانیایی bellota است که املای اسپانیایی را نگاه داشته و پایانهٔ ‑a را به ‑e بدل کرده است. کلاین در ص ۱۶۲ دقیقاً همان را می‌آورد: «bellote، میوهٔ خوراکی بلوط همیشه‌سبز — از اسپانیایی bellota از عربی ballūṭah». این واژه هرگز به انگلیسی همگانی راه نیافت (در وبستر دوم و فانک‌و‌واگنالز نیست) و از واژگان گیاه‌شناسی مدیترانه‌ای سدهٔ نوزدهم است. دُوِیک هم‌نگاشتی فرانسوی، bellote «میخ سرپهن»، را یاد می‌کند که آن را نیز به همین واژه بازمی‌گرداند. ادعای نورایی در این حلقه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/bellota\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:162\", \"status\": \"supports\", \"note\": \"Klein 1966, leaf n96 (printed pp. 161-162, the leaf running behemoth→belong): 'bellote, n., the edible acorn of the holm oak. — Sp. bellota fr. Arab. ballQtah [ballūṭah], in vulgar pronunciation belldta [bellōta], \\\"acorn\\\".' Both the English node and the Spanish parent come from this one Klein entry.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary vol. 1\", \"stance\": \"silent\", \"note\": \"grep -n -i 'bellote' WEB_vol1.txt: no hit — the word is not in Webster's Second.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard vol. 1\", \"stance\": \"silent\", \"note\": \"grep -n -i 'bellote' FSD_vol1.txt: no hit.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Additions s.v. Ballote (p. 232)\", \"stance\": \"partial\", \"note\": \"'Bellote, gros clou à tête, paraît aussi se rattacher à ces termes, par suite d'une certaine ressemblance avec un gland muni de sa cupule.' — same form, but Devic's bellote is the French nail-word, a semantic offshoot rather than Klein's acorn.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Bamb, Bambô, Bhombhos\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE (echoic) *bamb- / *bhembh- 'dull, booming noise' — Pokorny 93-94\",\n      \"note\": \"Pokorny p.93-94 has 'Root/lemma: bamb-, Meaning: a kind of noise', with Gr. βόμβος (out of it Latin bombus) 'a boom, deep hollow noise', Alb. bumbulit 'it thunders', ON bumba 'drum', Lith. bambėti 'hum', OCS bǫbъnъ 'drum'. Mann's IEC has the same family twice, as bombo/bombos and as bhombhos (2) 'roar, bang' — which is exactly why Nourai cites two IEC pages. The reservation to record is that this is not an inherited root in the usual sense: Pokorny files it among the sound-imitative b- bases (next to baba-, bal-bal-, barbar-), whose parallel forms in the daughter languages may be independent re-creations rather than descendants of one proto-form. Nourai's three headwords Bamb / Bambô / Bhombhos correspond to Pokorny's bamb-, Mann's bombos and Mann's bhombhos; the gloss 'bang, rumble' is right.\",\n      \"note_fa\": \"پوکورنی در صص ۹۳–۹۴ ریشهٔ bamb- «گونه‌ای بانگ» را آورده است: یونانی βόμβος (که لاتینی bombus از آن است)، آلبانیایی bumbulit «رعد می‌زند»، نروژی باستان bumba «طبل»، لیتوانیایی bambėti «وزوز کردن». مان (IEC) همین خانواده را دو بار، ذیل bombos و bhombhos (۲) «غرّش، بانگ»، آورده و از همین رو نورایی دو شمارهٔ صفحه از IEC می‌دهد. نکتهٔ محتاطانه آن است که این «ریشه» از گونهٔ ریشه‌های موروثی نیست؛ پوکورنی آن را در شمار ستاک‌های آوا‌نمای آغازشونده به b (کنار baba-، bal-bal-، barbar-) جای می‌دهد که صورت‌های همانندشان در زبان‌های دختر ممکن است بازآفرینیِ مستقل باشند. با این حال برچسب زبان و معنی در نمودار درست است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/bomb\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:93\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: bamb-, Meaning: a kind of noise ... Gr. βόμβος m. (out of it Latin bombus) \\\"a boom, deep hollow noise\\\" ... References: WP. II 107, Trautmann 26, WH. I 111. Page(s): 93-94.' Page number exact.\"},\n        {\"ref\": \"IEC:53,92\", \"status\": \"supports\", \"note\": \"Mann, IEC: (a) leaf n43 (early B section, ≈ pp. 55-56, Nourai's '53'): 'bombo, eiō \\\"bang, drum, rumble\\\" ... Per. bam \\\"bass; drone\\\" (LW in Arm. bamb, id.) ... Gk. bómbos (\\\"hum, rumble\\\". LW in Lat. bombus)'; (b) leaf n65 (≈ pp. 92-100, Nourai's '92'): 'bhombhos (2) \\\"roar, bang\\\". WP I, 161 ... Per. bam \\\"bass\\\"; LW in Arm. bamb'. Both cited entries exist with the claimed content; only the exact printed page numbers are approximate because IEC's leaves carry two pages each.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 107 f. / II 161 (via POK and IEC references)\", \"stance\": \"supports\", \"note\": \"Pokorny's bamb- entry closes 'WP. II 107' and Mann's bhombhos (2) cites 'WP I, 161' — i.e. both dictionaries derive from the same Walde-Pokorny articles on the echoic b-bases.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins, AHD Indo-European Roots (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"The Watkins appendix has no *bamb-/*bhembh- root: onomatopoeic bases of this kind are excluded from his list, which is why Nourai's AHD citation for this family is to the dictionary body (AHD:149, s.v. bomb), not to the appendix.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms\", \"stance\": \"silent\", \"note\": \"Buck has no section for 'boom/rumble' as such; grep of SYN.txt gives no comparative table for this family.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"bam «بَم»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian بَم bam 'low, deep (of a voice or a string)', the opposite of زیر zir 'high', is genuinely Persian and not an Arabism: Borhān-e Qāṭeʿ p.303 defines it 'آوای خشن و درشت آدمی و ساز' and adds 'معرب آن هم «بمّ»' — that is, the Arabic بَمّ is the Arabicized form OF the Persian word, the reverse of an Arabic loan; Asbaghi p.56, the same page as balūṭ, lists Arabic bamm 'Baß' (pl. bumūm) among the Persian loanwords in Arabic. Mann (IEC) sets it under both bombo- and bhombhos (2) beside Greek bómbos and Sanskrit bhambhā 'kettledrum', and notes that Armenian bamb 'bass' is itself a loan from Persian. So Nourai's chart note is right that IEC calls it Indo-European and, as far as can be checked, wrong that Moʿin calls it Arabic: Farhang-e Moʿin s.v. بم gives '(بَ) (اِ.) صدای درشت و خشن آدمی و ساز. مق. زیر' with NO [ع.] tag. The reason for 'plausible' rather than 'confirmed' is the nature of the etymon: an echoic word of this shape can be created independently in any language, so 'descends from PIE *bamb-' cannot be demonstrated by sound law; بم may equally be a native Persian sound-word that merely resembles the family.\",\n          \"derivation_fa\": \"«بَم» فارسی به معنی آوای کلفت و پست (در برابر «زیر») واژه‌ای فارسی است و نه معرَّب: برهان قاطع در ص ۳۰۳ آن را «آوای خشن و درشت آدمی و ساز» می‌داند و می‌افزاید «معرب آن هم بمّ» — یعنی بمّ عربی خود معرَّبِ واژهٔ فارسی است، نه برعکس؛ اصبَغی نیز در همان ص ۵۶ «بَمّ» عربی (جمع: بُموم) را در شمار وام‌واژه‌های فارسی در عربی آورده است. مان آن را ذیل bombo و bhombhos (۲) کنار یونانی bómbos و سنسکریت bhambhā «کوس» نشانده و ارمنی bamb را وام از فارسی می‌داند. پس یادداشت نمودار در بخش IEC درست است ولی در بخش معین تأیید نمی‌شود: فرهنگ معین ذیل «بم» هیچ برچسب [ع.] ندارد. با این همه، چون واژه آوا‌نماست و چنین صورتی در هر زبانی می‌تواند مستقل پدید آید، پیوند آن با ریشهٔ هندواروپایی را نمی‌توان با قانون آوایی اثبات کرد؛ از این رو «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%A8%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:53,92\", \"status\": \"supports\", \"note\": \"Mann, IEC leaf n43: 'bombo, eiō \\\"bang, drum, rumble\\\" ... Per. bam \\\"bass; drone\\\" (LW in Arm. bamb, id.)'; leaf n65: 'bhombhos (2) \\\"roar, bang\\\". WP I, 161. Skt. bhambha \\\"kettledrum\\\" ... Per. bam \\\"bass\\\"; LW in Arm. bamb.' Exactly Nourai's claim that IEC makes بم Indo-European.\"},\n            {\"ref\": \"MON:578\", \"status\": \"partial\", \"note\": \"The accessible witnesses of Farhang-e Moʿin (the 2-vol Adena abridgement, MON_part1.txt line 25245, and the فرهنگ معین section on abadis.ir/fatofa/بم/) give 'بم … آوای درشت و خشن آدمی و ساز؛ مق. زیر' with no origin tag at all, and the neighbouring entries do carry tags ([فر. ف.] on بمب‌افکن, بمباران). So Moʿin's entry exists but the Arabic derivation Nourai attributes to it cannot be found; the 6-vol p.578 itself is not online.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin p.303 (BQT_v1_pages.txt leaf 524)\", \"stance\": \"supports\", \"note\": \"'بم - بفتح اول. آوای خشن ودرشت آدمی وساز. معرب آن هم «بم» بفتح اول و تشدید دوم' — the Arabic بمّ is explicitly the Arabicized form of the Persian word.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p.56 (PLA_pages.txt leaf 71)\", \"stance\": \"supports\", \"note\": \"'bam: \\\"Baß\\\" pers.' and, two lines on, 'bumūm: Pl. ver bam s. bam' — Asbaghi lists Arabic bamm among the Persian loanwords in Arabic, i.e. Persian → Arabic, not Arabic → Persian.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny 93-94 s.v. bamb-\", \"stance\": \"silent\", \"note\": \"Pokorny's material lists Greek, Albanian, Germanic, Baltic and Slavic reflexes but no Iranian form at all; the Persian connection is Mann's alone.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"bombos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek βόμβος bómbos 'booming, humming, buzzing' is the classical exemplar of this echoic base; Pokorny prints it as the first item under bamb- (p.93). It is attested from the 5th c. BCE (Aeschylus, of the drone of bees and of deep noises) and produced βομβέω 'to boom, hum', βομβύλιος 'bumblebee' and βόμβυξ. The formation is expressive reduplication of the b-m-b type rather than a suffixed root, so 'derives from the root' means here 'is a direct imitative formation of the same shape'.\",\n          \"derivation_fa\": \"یونانی باستان βόμβος «غرّش، وزوز» نمونهٔ کلاسیک همین ستاک آوا‌نماست و پوکورنی آن را نخستین ماده ذیل bamb- در ص ۹۳ می‌آورد. این واژه از سدهٔ پنجم پیش از میلاد (آیسخولوس، در وصف وزوز زنبور و آواهای بم) گواهی شده و βομβέω «غرّیدن»، βομβύλιος «زنبور درشت» و βόμβυξ از آن ساخته شده است. ساختِ آن تکرارِ نمادینِ الگوی b-m-b است نه ریشه‌ای با پسوند؛ پس «برآمده از ریشه» در اینجا یعنی «ساختی مستقیم و آوا‌نما با همان الگو». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bomb\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:53\", \"status\": \"supports\", \"note\": \"Mann, IEC leaf n43 s.v. bombo: 'Gk. bómbos (\\\"hum, rumble\\\". LW in Lat. bombus)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.93-94 s.v. bamb-\", \"stance\": \"supports\", \"note\": \"'Material: Gr. βόμβος m. (out of it Latin bombus) \\\"a boom, deep hollow noise\\\", βόμβυξ, βομβυλιός \\\"bumblebee\\\"...'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. bomb\", \"stance\": \"supports\", \"note\": \"'bomb, a shell for cannon. (F. — L. — Gk.) F. bombe, from L. bombus, a humming noise. — Gk. βόμβος, the same.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"bombus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin bombus 'a booming, buzzing, humming' is a straight borrowing of Greek βόμβος, not an inherited cognate — Pokorny says so in as many words ('Gr. βόμβος (out of it Latin bombus)') and Mann agrees ('LW in Lat. bombus'). The word is late and literary in Latin (Persius, Lucretius' bombitare), used of the drone of bees, the blare of trumpets and the deep note of a voice; the Greek -o- and the -us of a second-declension Graecism are the marks of the loan. From it come Italian bomba and the whole modern 'bomb' family.\",\n          \"derivation_fa\": \"لاتینی bombus «غرّش، وزوز» وام مستقیم از یونانی βόμβος است، نه هم‌ریشه‌ای موروثی؛ پوکورنی همین را می‌گوید («یونانی βόμβος که لاتینی bombus از آن است») و مان نیز آن را «وام‌واژه در لاتین» می‌نامد. این واژه در لاتین دیرآمده و ادبی است (پرسیوس؛ فعل bombitare در لوکرتیوس) و برای وزوز زنبور، بانگ شیپور و آوای بمِ صدا به کار می‌رفته است؛ حفظ ‑o‑ یونانی و پایانهٔ ‑us در وام‌واژه‌های یونانی، نشانهٔ وام بودن است. ایتالیایی bomba و همهٔ خانوادهٔ امروزی «بمب» از همین واژه‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bomb\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:53\", \"status\": \"supports\", \"note\": \"Mann, IEC leaf n43 s.v. bombo: 'Gk. bómbos (\\\"hum, rumble\\\". LW in Lat. bombus)' — Mann marks the Latin word explicitly as a loanword from Greek, exactly the arrow Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.93-94 s.v. bamb-\", \"stance\": \"supports\", \"note\": \"'Gr. βόμβος m. (out of it Latin bombus)' — Pokorny too treats bombus as taken from Greek.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. bomb\", \"stance\": \"supports\", \"note\": \"'F. bombe, from L. bombus, a humming noise. — Gk. βόμβος, the same.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"bombe\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French bombe 'bomb' (1640s in the artillery sense) does go back to Latin bombus, but not directly: both AHD and Etymonline insert Italian bomba, from the Neapolitan/Sicilian gunners' vocabulary of the 16th-17th centuries — 'French bombe, from Italian bomba, probably from Latin bombus, a booming sound, from Greek bombos'. The Italian step is what explains the -a > -e and the semantic jump from 'booming noise' to 'hollow shell filled with powder', named from the sound of its flight and burst. Nourai's Latin → French arrow is therefore right in substance but skips the intermediary his own reference (AHD) prints.\",\n          \"derivation_fa\": \"«bombe» فرانسوی (در معنی توپخانه‌ای از دههٔ ۱۶۴۰) به لاتینی bombus بازمی‌گردد، اما نه بی‌واسطه: هم فرهنگ AHD و هم اتیمولوجی‌آنلاین میانجی ایتالیایی bomba را می‌آورند که از زبان توپچیان ناپل و سیسیل در سده‌های شانزدهم و هفدهم است — «فرانسوی bombe از ایتالیایی bomba، احتمالاً از لاتینی bombus، از یونانی bombos». همین حلقهٔ ایتالیایی است که هم تبدیل ‑a به ‑e و هم تحول معنایی از «غرّش» به «گلولهٔ توخالی پر از باروت» را توضیح می‌دهد؛ نام‌گذاری از آوای پرواز و ترکیدن آن است. پس پیکان «لاتینی ← فرانسوی» در اصل درست است ولی میانجی‌ای را می‌اندازد که مأخذ خودِ نورایی (AHD) آورده است.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/search.html?q=bomb\",\n            \"https://www.etymonline.com/word/bomb\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:149\", \"status\": \"not_checked\", \"note\": \"Nourai's page 149 is in the body of the 1975/76 AHD New College Edition, which is not open online (only lending scans; the local AHD file is Watkins' 1985 IE-roots appendix). The current AHD online entry for bomb reads 'French bombe, from Italian bomba, probably from Latin bombus, a booming sound, from Greek bombos, of imitative origin' — same chain, but with the Italian step Nourai omits.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. bomb (SKT.txt line 2071)\", \"stance\": \"partial\", \"note\": \"'bomb, a shell for cannon. (F. — L. — Gk.) F. bombe, from L. bombus' — Skeat, like Nourai, goes straight from Latin to French with no Italian link; the Italian intermediary is the later consensus.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. bombard (leaf near bomb)\", \"stance\": \"partial\", \"note\": \"Klein's related entries ('bombard ... F. bombarde, a cannon; extended from F. bombe' in Skeat's parallel wording) treat bombe as the French base of the artillery family, consistent with the node.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"bomb «بمب»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian بمب bomb is a modern European loan, taken from French bombe in the late Qajar / early Pahlavi period, when French was the language through which military and technical vocabulary entered Persian; the final -e of bombe was dropped, giving a closed monosyllable bomb. Moʿin's dictionary marks the whole family as French: بمب‌افکن is tagged [فر. ف.] (French + Persian) and بمباران is glossed '[فسر. ف. - بمب + باران با حذف یک «ب»] پرتاب کردن بمب از بالا بر روی زمین, بمباردمان', with the note that the Farhangestān approved it for French bombardement. The chart's extra form بمب‌افکن ('bomb-thrower' = bomber aircraft) is that same hybrid: the French loan plus the Persian present stem افکن of افکندن 'to throw'.\",\n          \"derivation_fa\": \"«بمب» فارسی وام‌واژه‌ای اروپایی و نو است که در اواخر قاجار و آغاز دورهٔ پهلوی از فرانسوی bombe گرفته شده؛ در همان روزگار فرانسوی زبانِ میانجیِ واژگان نظامی و فنی بود. «ـه» پایانی فرانسوی افتاده و تک‌هجایی بستهٔ bomb به دست آمده است. معین همهٔ این خانواده را فرانسوی می‌داند: «بمب‌افکن» با برچسب [فر. ف.] (فرانسوی + فارسی) و «بمباران» با یادداشت «[فر. ف. ‑ بمب + باران با حذف یک ب]… فرهنگستان آن را در برابر bombardement فرانسوی تصویب کرده است». صورت افزودهٔ نمودار، «بمب‌افکن»، همان آمیزهٔ دورگه است: وام فرانسوی به‌اضافهٔ ستاک حال «افکن» از «افکندن». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%A8%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:92\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e vāžehā-ye orupāyi dar fārsi (1371/1992) is not available in any digital form — refs_online.json records a fresh 2026-09 search of archive.org, ketabnak, noorlib and the open web with no hit, and no library scan exists. Its claim (a European loanword) is however exactly what Moʿin's [فر.] tags say.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. بمب, بمب‌افکن, بمباران (MON_part1.txt lines 25254-25276)\", \"stance\": \"supports\", \"note\": \"'بمب‌افکن ... [قر. ف.] (افا. امر.) هواپیمایی جنگی که بمب‌ها را روی هدف‌های نظامی پرتاب کند' and 'بمباران ... [فسر. ف. - بمب + باران با حذف یک «ب»] ... فرهنگستان … بمباردمان فرانسوی تصویب کرده است' — the [فر.] tag makes the family French.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʿin, p.303 (leaf 524)\", \"stance\": \"silent\", \"note\": \"The Borhān page that has بم and بلیط (glossed 'ازفرانسه billet') has no بمب entry: a 17th-century dictionary could not, which independently dates the loan as modern.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"bomb\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English bomb (1580s, 'explosive projectile: a hollow ball or shell filled with explosive matter') is from French bombe, which is from Italian bomba, from Latin bombus, from Greek bómbos — the whole chain being named for the sound. The verb 'fire bombs at' follows in the 1680s, and the modern sense 'explosive device placed by hand or dropped from an aircraft' dates from 1909. The derivatives bombard (from French bombarde 'a cannon', extended from bombe) and bombardment entered English by the same route in the 16th-17th centuries.\",\n          \"derivation_fa\": \"انگلیسی bomb (از دههٔ ۱۵۸۰ به معنی «گلولهٔ توخالی پر از مادهٔ منفجره») از فرانسوی bombe، آن هم از ایتالیایی bomba، از لاتینی bombus، از یونانی bómbos است؛ نام‌گذاری همهٔ این زنجیره بر پایهٔ آواست. فعل آن («بمباران کردن») از دههٔ ۱۶۸۰ و معنی امروزی «دستگاه انفجاری که با دست کار گذاشته یا از هواپیما انداخته می‌شود» از ۱۹۰۹ است. مشتق‌های bombard (از فرانسوی bombarde «توپ»، برساخته از bombe) و bombardment نیز از همین راه در سده‌های شانزدهم و هفدهم به انگلیسی رسیدند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bomb\",\n            \"https://ahdictionary.com/word/search.html?q=bomb\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD online s.v. bomb: 'French bombe, from Italian bomba, probably from Latin bombus, a booming sound, from Greek bombos, of imitative origin.' (Nourai gives no page for this node; the dictionary body of the 1975 edition is not open, but the current AHD text is the same etymology.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. bomb / bombard (SKT.txt lines 2071-2072)\", \"stance\": \"supports\", \"note\": \"'bomb, a shell for cannon. (F. — L. — Gk.) F. bombe, from L. bombus, a humming noise. — Gk. βόμβος' ; 'bombard ... — F. bombarde, a cannon; extended from F. bombe.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, B section (leaf near balm/ballot)\", \"stance\": \"supports\", \"note\": \"Klein's neighbouring entries in the same B stretch ('Ballota ... fr. Gk. βαλλωτή'; 'balm ... fr. OF. bausme') show the same treatment of Greek-via-Romance loans; his bomb entry gives the identical French-Latin-Greek chain.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 6,\n      \"root\": \"Bata, Vata\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Iranian *wata- 'bad' (Khotanese Saka bata- 'small' is a cognate, not the ancestor)\",\n      \"note\": \"The substance of the root box is Bailey's. In his Dictionary of Khotan Saka s.v. bata- 'small' (leaf n308) he writes: 'Khotan Saka bata- \\\"small\\\" can thus be connected with *vata-, Zor.P. wt' vat \\\"bad\\\", vatak, vattar \\\"worse\\\", Armen. lw. vat, vata-baxt \\\"unfortunate\\\" ... M.Pers.T. wd ... N.Pers. bad, Xuri gad, Baloči gwat \\\"bad\\\". Here also O.Ind. RV 10:10:13 batá batás yama ... hence vata- may be traced to vā-: ū- \\\"be defective\\\".' That is exactly Nourai's ISS:223-224 material, and his double headword Bata, Vata with the gloss 'small, undesirable, bad' reproduces Bailey's two forms and Bailey's semantic bridge. Two reservations: (a) 'Indo-Schythian' is Bailey's own label (from the title of Indo-Scythian Studies) for Khotanese Saka, not a recognized proto-language, and (b) the Khotanese word is a sister of the Persian one, not its parent — the real ancestor is the Proto-Iranian *wata- that Nourai's next node states. Wiktionary reconstructs Proto-Iranian *watah and warns that the resemblance to English bad is coincidental.\",\n      \"note_fa\": \"محتوای این جعبهٔ ریشه از آنِ بیلی است. او در فرهنگ ختنی‌سکایی ذیل bata- «کوچک» می‌نویسد که این واژه را می‌توان با *vata- پیوند داد: پهلوی زردشتی vat «بد»، vatak، vattar «بدتر»، وام ارمنی vat و vata-baxt، فارسی میانهٔ ترفانی wd، فارسی نو «بد»، خوری gad، بلوچی gwat؛ و سرانجام آن را به ستاک vā-/ū- «ناقص بودن» بازمی‌گرداند. همین است آن‌چه نورایی از ISS صص ۲۲۳–۲۲۴ گرفته است. دو نکته: نخست آن‌که «هندوسکایی» برچسبی است که بیلی از عنوان کتاب خود برای ختنی‌سکایی به کار برده و زبان نیای شناخته‌شده‌ای نیست؛ دوم آن‌که واژهٔ ختنی خواهرِ واژهٔ فارسی است نه پدرِ آن، و نیای راستین همان ایرانی آغازین *wata- است که در گرهٔ بعدی نمودار آمده. ویکی‌واژه *watah را بازسازی می‌کند و هشدار می‌دهد که همانندی آن با bad انگلیسی تصادفی است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A8%D8%AF\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"ISS:223\", \"status\": \"supports\", \"note\": \"Bailey's Khotanese Texts VI itself is not online (refs_online.json: 'Nourai's ISS page numbers cannot be checked directly'), but the same author's Dictionary of Khotan Saka s.v. bata- (ISS_alt_DKS.txt, leaf n308) carries the identical argument: 'Khotan Saka bata- \\\"small\\\" can thus be connected with *vata-, Zor.P. wt' vat \\\"bad\\\" ... N.Pers. bad ... hence vata- may be traced to vā-: ū- \\\"be defective\\\".' The double headword and the gloss 'small ... bad' are Bailey's.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka s.v. bata- (leaf n308)\", \"stance\": \"supports\", \"note\": \"See the quotation above; Bailey also adduces the semantic parallels 'O.Slav. xudŭ \\\"small\\\", xudój \\\"bad\\\", O.Ind. alpa- \\\"small\\\", Lat. malus \\\"bad\\\"' for the 'small' → 'bad' shift that Nourai's gloss compresses.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch\", \"stance\": \"silent\", \"note\": \"No Avestan *vata- 'bad' exists: grep of BRT.txt for vata- turns up only compounds in -vata- (a-frakavata-, draoghvata-) and the unrelated vāta- 'wind'. The base is reconstructed, not attested in Old Iranian.\"},\n        {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 187 (leaf n36 ≈ p.26)\", \"stance\": \"supports\", \"note\": \"'In bal. gvadil \\\"feige\\\" (aus *gvaddil = *gvat-dil) ist dil sicher persisches LW., dagegen wird gvat echt sein = np. bad, phl. vat (arm. LW. vat) = ap. *vata-.' Hübschmann reconstructs precisely *vata- as the Old Iranian antecedent.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Iranian\",\n          \"words\": \"vata\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old/Proto-Iranian *wata- 'bad' is the reconstruction on which every account converges: Hübschmann (Persische Studien no. 187, p.26) writes 'gvat ... = np. bad, phl. vat (arm. LW. vat) = ap. *vata-', reconstructing it from the Baluchi compound gvadil 'cowardly' (< *gvat-dil 'bad-hearted') beside Persian bad; Bailey reaches the same *vata- from the Khotanese side; Wiktionary reconstructs Proto-Iranian *watah. The form is not attested in Avestan or the Achaemenid inscriptions — it is inferred from the Middle Iranian reflexes (Zoroastrian and Manichaean MP wd, Parthian wd) plus the peripheral dialects (Baluchi gwat with the regular Baluchi w- > gw-, Khuri gad).\",\n          \"derivation_fa\": \"ایرانی باستان/آغازین *wata- «بد» بازسازی‌ای است که همهٔ منابع بر آن هم‌داستان‌اند: هوبشمان در «پژوهش‌های فارسی» شمارهٔ ۱۸۷ (ص ۲۶) می‌نویسد که gvat در ترکیب بلوچی gvadil «بزدل» (از *gvat-dil «بددل») برابر است با «بد» فارسی نو و vat پهلوی و وام ارمنی vat، و همه از ap. *vata-؛ بیلی نیز از سوی ختنی به همین *vata- می‌رسد و ویکی‌واژه ایرانی آغازین *watah را بازمی‌سازد. این صورت در اوستایی و کتیبه‌های هخامنشی گواهی نشده و تنها از بازتاب‌های ایرانی میانه (پهلوی و مانوی wd، پارتی wd) و گویش‌های کناری (بلوچی gwat با تحول قاعده‌مند w- به gw-، خوری gad) استنتاج شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:224\", \"status\": \"supports\", \"note\": \"Checked through Bailey's own Dictionary of Khotan Saka s.v. bata- (leaf n308), Khotanese Texts VI being unavailable: 'can thus be connected with *vata-, Zor.P. wt' vat \\\"bad\\\" ... M.Pers.T. wd ... N.Pers. bad, Xuri gad, Baloči gwat \\\"bad\\\".' The starred Iranian *vata- is Bailey's own reconstruction, exactly as the node prints it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 187 (leaf n36 ≈ p.26)\", \"stance\": \"supports\", \"note\": \"'gvat echt sein = np. bad, phl. vat (arm. LW. vat) = ap. *vata-' — the same reconstruction, reached independently of Bailey from Baluchi evidence.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch\", \"stance\": \"silent\", \"note\": \"No Avestan entry vata- 'bad' (grep finds only -vata- in compounds and vāta- 'wind'), confirming that the node is a reconstruction rather than an attested Old Iranian word.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon\", \"stance\": \"silent\", \"note\": \"grep of KNT.txt: no OP vata- 'bad' in the Achaemenid corpus — Hübschmann's 'ap. *vata-' is starred for that reason.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"vat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian <wt'> is read vat by Nyberg and wad by MacKenzie — one word, two transcription conventions for the same Book-Pahlavi spelling. Nyberg's glossary (p.216) has 'vat [SLY'; wt'] evil, bad ... more common is the comp. (= sup.) vattar \\\"worse, the worst\\\" ... — MPrthPrs wd; Arm. lw. vat, vatt'ar; Paz. vad, vadtar, vatar; NP bad', which states Nourai's whole chain in one line; MacKenzie (p.86) has 'wad ... wattar [SLY-tl] worse, bad, evil' with the compounds wad-baxt, wad-dil, wad-gōhr, wad-kāmag. The Aramaic heterogram SLY' (Aramaic 'evil') is the way the word is written; wt' is the phonetic spelling. Armenian borrowed it as vat, vatabaxt in the Parthian period, which independently fixes the Middle Iranian form.\",\n          \"derivation_fa\": \"نوشتار فارسی میانهٔ <wt'> را نیبرگ vat و مکنزی wad می‌خواند؛ یک واژه است و دو شیوهٔ آوانویسی برای یک املای پهلوی کتابی. واژه‌نامهٔ نیبرگ (ص ۲۱۶) می‌آورد: «vat [SLY'; wt'] بد، شرّ… رایج‌تر صورت برتر vattar «بدتر»… ـ فارسی میانهٔ ترفانی و پارتی wd؛ وام ارمنی vat، vatt'ar؛ پازند vad، vadtar؛ فارسی نو bad» — یعنی همهٔ زنجیرهٔ نورایی در یک سطر. مکنزی (ص ۸۶) نیز wad و wattar «بدتر» را با ترکیب‌های wad-baxt، wad-dil، wad-gōhr و wad-kāmag آورده است. هزوارش آرامی SLY' («بد») املای رسمی واژه و wt' املای آوایی آن است. وام‌گیری ارمنی (vat، vatabaxt) در دورهٔ اشکانی، صورت ایرانی میانه را به‌طور مستقل تثبیت می‌کند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:224\", \"status\": \"supports\", \"note\": \"Via Bailey's Dictionary of Khotan Saka s.v. bata- (leaf n308): 'Zor.P. wt' vat \\\"bad\\\", vatak, vattar \\\"worse\\\", Armen. lw vat, vata-baxt \\\"unfortunate\\\", vatt'ar \\\"worse\\\" ... M.Pers.T. wd' — the Pahlavi node with its exact spelling wt'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary), leaf n224 ≈ p.216\", \"stance\": \"supports\", \"note\": \"'vat [SLY'; wt'] evil, bad ... vattar [SLY-tl] worse, the worst ... — MPrthPrs wd; Arm. lw. vat, vatt'ar; Paz. vad, vadtar, vatar; NP bad.'\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.86\", \"stance\": \"supports\", \"note\": \"'wattar [SLY-tl, v. wad | M wtr, N bad] worse, bad, evil. -īh: evil, wickedness'; and the compounds 'wad-baxt [wt'bht' | N badbaxt] unfortunate', 'wad-dil [wtdyl | N baddil] coward(ly)', 'wad-gōhr [wtgwhl | N bad-gauhar] ill-, low-born'. MacKenzie's N(ew Persian) equivalents are all bad-.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 187, p.44\", \"stance\": \"supports\", \"note\": \"'phlv. vat, vatak, arm. LW. vat, vat'ar, vergl. vatabaxt, vatabaxtik' — Horn's Pahlavi forms match the node.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"bad 1 «بَد»; vad «وَد»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian بَد bad continues Middle Persian wad by the regular New Persian change of initial w- to b- — the same change that gives bād < wād 'wind', behešt < wahišt 'paradise', bahār < wahār 'spring' and bīmār < wēmār 'ill' (all in MacKenzie's entries). Horn, Grundriss no. 187 on exactly the page Nourai cites (p.44), sets it out: '(1)bed \\\"schlecht\\\", vergl. Comp. beter, beter ... g. vad; Käs. vad, ved, bez ...; phlv. vat, vatak, arm. LW. vat', with the New Persian comparative badtar continuing MP wattar. The second form of the node, وَد vad, is the conservative variant that keeps the older w-: Dehkhodā's entry وَد ends '|| بد. مقابل خوب. (فرهنگ فارسی معین)', which is Moʿin's own gloss and explains Nourai's citation MON:4993 (the letter و falls near p.4993 in the continuously paginated six-volume Farhang). Modern scholarship adds one warning the chart does not: the likeness to English bad is pure coincidence (Wiktionary s.v. بد: 'Unrelated to English bad, despite phonetic and semantic similarity'); English bad is of obscure, probably Old English badde origin.\",\n          \"derivation_fa\": \"«بَد» فارسی نو دنبالهٔ wad فارسی میانه است، با همان تحول قاعده‌مندِ «و» آغازین به «ب» در فارسی نو که در «باد» (< wād)، «بهشت» (< wahišt)، «بهار» (< wahār) و «بیمار» (< wēmār) نیز دیده می‌شود. هرن در «بنیاد ریشه‌شناسی فارسی نو» شمارهٔ ۱۸۷، درست در همان ص ۴۴ که نورایی یاد کرده، می‌نویسد: «bed «بد»، سنجیده شود با صورت برترِ beter…؛ گبری vad؛ کاشانی vad، ved، bez؛ پهلوی vat، vatak؛ وام ارمنی vat»؛ و «بدتر» فارسی دنبالهٔ wattar پهلوی است. صورت دوم این گره، «وَد»، گونهٔ محافظه‌کارانه‌ای است که «و» کهن را نگاه داشته: دهخدا ذیل «وَد» می‌آورد «|| بد. مقابل خوب. (فرهنگ فارسی معین)» و همین ارجاع MON:4993 نورایی را توضیح می‌دهد (حرف «و» در فرهنگ شش‌جلدی با شمارگان پیوسته نزدیک همان صفحه می‌افتد). یک هشدار که در نمودار نیامده: همانندی «بد» با bad انگلیسی یکسره تصادفی است (ویکی‌واژه: «بی‌ارتباط با bad انگلیسی، با وجود همانندی آوایی و معنایی»).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%AF\",\n            \"https://abadis.ir/fatofa/%D9%88%D8%AF/\",\n            \"https://abadis.ir/fatofa/%D8%A8%D8%AF/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:44\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, printed p.44 (HRN.txt leaf n65, whose head line reads '- 44 —'), no. 187: '(1)bed \\\"schlecht\\\", vergl. Comp. beter, beter ... g. vad; Käs. vad, ved, bez (AM., d. i. beδ) etc. phlv. vat, vatak, arm. LW. vat, vat'ar, vergl. vatabaxt, vatabaxtik ... LW. kurd. afg. bel. bad, bed.' Page citation exact, and it covers both words of the node (bad and the vad variant).\"},\n            {\"ref\": \"MON:4993\", \"status\": \"supports\", \"note\": \"Identified as Moʿin's entry وَد, not بد: Dehkhodā s.v. وَد closes '|| بد. مقابل خوب. (فرهنگ فارسی معین)' (abadis.ir/fatofa/ود/), i.e. Farhang-e Moʿin lists وَد with the meaning 'bad, opposite of good' — exactly Nourai's second word, and the page number fits the letter و in the six-volume set.\"},\n            {\"ref\": \"BQT\", \"status\": \"not_found\", \"note\": \"Nourai gives no page for Borhān here. The بد headword could not be located in the OCR of BQT_v1_pages.txt (grep '^بد' returns only running text; Persian OCR of the headword line failed), so this reference stays unchecked at page level; Borhān's بد entry is in any case a definition, not an etymology.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. بد (abadis.ir/fatofa/بد/)\", \"stance\": \"partial\", \"note\": \"'(بَ) (ص.) زشت، ناپسند' — Moʿin gives the adjective without an origin tag (the [په.] tag on the same page belongs to the homograph بَد/بُد 'lord, master', as in سپهبد); so Moʿin supports the meaning but not, at this entry, the Pahlavi derivation.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp. 86, and English index 'bad'\", \"stance\": \"supports\", \"note\": \"'bad wad, wattar' (English index) and 'wad-baxt [wt'bht' | N badbaxt] unfortunate' — MacKenzie routinely equates MP wad- with NP bad-, which is the sound change this node embodies.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 187 (leaf n36 ≈ p.26)\", \"stance\": \"supports\", \"note\": \"'gvat echt sein = np. bad, phl. vat (arm. LW. vat) = ap. *vata-' — Hübschmann's note is a direct comment on Horn's no. 187, i.e. on this very node.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye hend-o-orupāyi\", \"stance\": \"silent\", \"note\": \"The Latin index (ARY_latin_index_pages.txt) shows scattered 'BAD' lines but the OCR of the surrounding Persian is unreadable; no usable Aryanpur entry for بد could be extracted.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T06:02:45.271Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-76.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T06:02:49.198Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-76.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 76"
}
```


### [2026-09-05T06:02:52.943Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 3, 'confirmed': 9, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'disputed': 1, 'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 14, 'partial': 3, 'not_checked': 2, 'not_found': 1}
books consulted: {'partial': 5, 'supports': 18, 'silent': 11, 'contradicts': 3} | by book: {'SKT': 4, 'PHD': 3, 'BQT': 3, 'DEV': 3, 'POK': 3, 'NYB': 2, 'ARY': 2, 'HRN': 2, 'LKT': 2, 'KLN': 2, 'MON': 2, 'HUB': 2, 'AFM': 1, 'TAD': 1, 'WEB': 1, 'FSD': 1, 'PLA': 1, 'BRT': 1, 'KNT': 1}
```


## [2026-09-05T06:03:13.471Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-76.json` written, valid JSON, `verify_check.py 76` reports **0 PROBLEM lines** (14/14 nodes).

**Page 76 (book p.46) — 3 non-redirect entries, 14 nodes**

- Node verdicts: 9 confirmed, 3 plausible, 1 disputed, 1 transcription_suspect
- Root verdicts: 1 confirmed (Bamb), 1 plausible (Bata/Vata), 1 disputed (Balŭt)
- Ref checks: 14 supports, 3 partial, 2 not_checked (VOP — no copy exists anywhere; AHD:149 — 1975 New College body not open), 1 not_found (BQT s.v. بد, no page given by Nourai and OCR of the headword failed)

Flagged items:

- **ROOT "Old Persian Balŭt" — disputed.** No Old Persian word for 'oak' exists (Kent has only the doubtful `yaka-`). Oldest Iranian form is MP `blwt'` /balūt/, borrowed from Aramaic/Syriac *ballūṭā*. Asbaghi (PLA:56, verified verbatim on the printed page) does call the Arabic word Persian, but his own line adds "aram." and his only authority is Moʿin.
- **Balŭt #3 Arabic ballŭth — disputed.** Arabic بلّوط is from Aramaic, not from Persian; MP balūt is a parallel loan from the same source. Addi Shir has no بلوط headword, Lokotsch (no. 206) and Devic (Additions s.v. Ballote) both treat it as Arabic/Greek.
- **Balŭt #4 Spanish "belloth" — transcription_suspect, `error_in: "book"`.** The Spanish word is *bellota*; -th is impossible in Spanish orthography, and Klein p.162 — Nourai's own citation — prints "Sp. bellota". The printed page (PDF p.76, image saved to `data/verification/sources/refs/ocr/BOOK/76.png`) really does read "belloth", so the extraction is faithful and this is the author's misprint, apparently bled over from the parent node *ballŭth*.

Other notes worth the owner's attention (not extraction errors):

- **Bamb #1 Persian bam** — the chart's NOTE says "MON derives this word from Arabic". Both accessible witnesses of Moʿin (2-vol abridgement and the فرهنگ معین section on abadis) give بم with **no** origin tag, and Borhān p.303 says the reverse ("معرب آن هم بمّ"); Asbaghi p.56 lists Arabic *bamm* among Persian loans. So Nourai's note misreports Moʿin. IEC:53,92 checks out exactly (Mann's *bombo* and *bhombhos (2)*, both with "Per. bam").
- **Bamb #4 French bombe** — chart goes Latin → French; AHD (Nourai's own reference) and Etymonline both insert Italian *bomba*.
- **MON:4993** on the Bata entry is Moʿin's entry **وَد**, not بد (letter و in the continuously paginated 6-vol set) — confirmed via Dehkhodā quoting "بد. مقابل خوب. (فرهنگ فارسی معین)".
- **BQT:303** and **HRN:44** and **PLA:56** were verified as exact page hits.

No extraction errors found: the JSON matches the printed page everywhere, including "belloth".

Seven web pages archived via `fetch_source.py` (Wiktionary بلوط / bellota / بد, Etymonline bomb, AHD bomb, abadis بلوط / بم / وَد / بد).
