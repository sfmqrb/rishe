# Verification process log — verify-page-136


## [2026-09-05T20:07:18.959Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 136 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-136.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-136.json. Write /home/sfmqrb/git/rishe/data/verification/page-136.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 136` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:07:20.570Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:07:21.250Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:07:21.262Z] TOOL RESULT

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


## [2026-09-05T20:07:21.510Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-136.txt"
}
```


### [2026-09-05T20:07:21.523Z] TOOL RESULT

```
1	=== PDF page 136 (book page 106) ===
2	--- entry 0 ---
3	ROOT Dhumbhma -> redirect to Dumb
4	--- entry 1 ---
5	ROOT [Indo-European] Dhŭs : whir, whirring object, spindle  (refs IEC:224)
6	#1 (parent #0) [Persian] refs=IEC:224 | dŭk «دوک» : spindle
7	#2 (parent #0) [Latin] refs=IEC:224 | fŭsus : spindle | NOTE: POK:448 derives this word from root "Gheu 1 : to pour".
8	--- entry 2 ---
9	ROOT [Indo-European] Dhwer, Dhrugh, Dhwor : door  (refs POK:278; KNT:191)
10	#1 (parent #0) [Avestan / Old Persian] refs=BQT:828; KNT:191 | dvar, duvara : door
11	  #2 (parent #1) [Persian] refs=BQT; FVF:98,240 | dar «در (دروازه، دربان)» : door ; darband «دربند» : "enclosed area" ☞Bhendhe ; bandar «بندر (بنادر)» : "enclosed area", seaport ☞Bhendhe
12	    #3 (parent #2) [Arabic] refs=FVF:240 | darb : gate
13	      #4 (parent #3) [Persian] refs=MON:1503 | darb «درب» : door
14	  #5 (parent #1) [Sogdian] refs=SOD:138 | dbr : door
15	#6 (parent #0) [Germanic] refs=AHD | durunz : door
16	  #7 (parent #6) [English] refs=None | door
17	#8 (parent #0) [Greek] refs=AHD:1343 | thura : door ; thuroidĕs : door shaped (gland)
18	  #9 (parent #8) [French] refs=None | 
19	    #10 (parent #9) [Persian] refs=MON:1178 | tîroîd «تیروئید» : thyroid
20	  #11 (parent #8) [English] refs=None | thyroid
21	#12 (parent #0) [Latin] refs=AHD | foris, foras : outdoors, outside
22	  #13 (parent #12) [English] refs=AHD | forest, foreign
23	--- entry 3 ---
24	ROOT Dhwor -> redirect to Dhwer
25	--- entry 4 ---
26	ROOT Di -> redirect to Dâ 1
27	--- entry 5 ---
28	ROOT Dibbĕr -> redirect to D.b.r
29	
```


## [2026-09-05T20:07:24.739Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-136.json",
 "description": "Read source JSON for page 136"
}
```


### [2026-09-05T20:07:24.804Z] TOOL RESULT

```
{
  "pdf_page": 136,
  "book_page": 106,
  "entries": [
    {
      "root": {
        "name": "Dhumbhma",
        "redirect": "Dumb"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhŭs",
        "lang": "Indo-European",
        "refs": "IEC:224",
        "gloss": "whir, whirring object, spindle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:224",
          "words": [
            {"translit": "dŭk", "gloss": "spindle", "script": "دوک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "IEC:224",
          "words": [
            {"translit": "fŭsus", "gloss": "spindle", "script": null}
          ],
          "note": "POK:448 derives this word from root \"Gheu 1 : to pour\".",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dhwer, Dhrugh, Dhwor",
        "lang": "Indo-European",
        "refs": "POK:278; KNT:191",
        "gloss": "door"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "BQT:828; KNT:191",
          "words": [
            {"translit": "dvar, duvara", "gloss": "door", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT; FVF:98,240",
          "words": [
            {"translit": "dar", "gloss": "door", "script": "در (دروازه، دربان)"},
            {"translit": "darband", "gloss": "\"enclosed area\"", "script": "دربند", "see": ["Bhendhe"]},
            {"translit": "bandar", "gloss": "\"enclosed area\", seaport", "script": "بندر (بنادر)", "see": ["Bhendhe"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "FVF:240",
          "words": [
            {"translit": "darb", "gloss": "gate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:1503",
          "words": [
            {"translit": "darb", "gloss": "door", "script": "درب"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:138",
          "words": [
            {"translit": "dbr", "gloss": "door", "script": null}
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
            {"translit": "durunz", "gloss": "door", "script": null}
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
            {"translit": "door", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1343",
          "words": [
            {"translit": "thura", "gloss": "door", "script": null},
            {"translit": "thuroidĕs", "gloss": "door shaped (gland)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:1178",
          "words": [
            {"translit": "tîroîd", "gloss": "thyroid", "script": "تیروئید"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "thyroid", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "foris, foras", "gloss": "outdoors, outside", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "forest, foreign", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dhwor",
        "redirect": "Dhwer"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Di",
        "redirect": "Dâ 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dibbĕr",
        "redirect": "D.b.r"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:07:25.309Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:07:25.353Z] TOOL RESULT

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


## [2026-09-05T20:07:30.783Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','POK','KNT','BQT','FVF','FVQ','MON','SOD','AHD','SYN','WLD','KLN','SKT','LEW','LAT','BRT','PHD','NYB','HRN','HUB','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


## [2026-09-05T20:07:31.357Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo --- && head -60 data/verification/page-127.json"
}
```


### [2026-09-05T20:07:32.857Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_f
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnair
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


### [2026-09-05T20:07:32.895Z] TOOL RESULT

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
---
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


## [2026-09-05T20:07:41.452Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dhus\\|dhūs\\|dhŭs\" IEC.txt | head -40\necho \"=== fusus in IEC\"\ngrep -n \"fūsus\\|fusus\" IEC.txt | head -20\necho \"=== dhwer/dhuer POK\"\ngrep -n \"dhu̯er\\|dhuer\\|dhu̯ōr\\|dhver\" POK_01.txt POK_02.txt POK_full.txt | head -40"
}
```


### [2026-09-05T20:07:41.527Z] TOOL RESULT

```
681:ardus, uos (1) ‘high’. WP I, 83. Cf. ordhus, uordhos, ardis Av arədus; Lat. arduus (1); MIr.Ir. ard, árd; Gaul. ardu- (in a placename Ardu-enna 'Ar- dennes’)
682:ardus, uos (2) ‘sad, serious, careworn’. Cf. WP I, 83 and ordhus Lat. arduus (2) ‘serious, distressed"; Li. ardùs
2620:dusnos, à “evil, sad; evil, sadness, hate. Cf. dus-, dusa, etc. Gk. o-dune (grief, fr. o! interj. + ^; cf. kin- dünos ‘risk’; Arm. erkn, gs erkan ‘toil, labour in childbirth; EMAIb. &n-dhuné (in phr. qell — ‘mock, pér-dhuni *disgracefully"); OHG zorn ‘hate, rage’; MHG zorn (bitter, cruel; rage’. fr. *dusnó-); OE torn ‘cruel, “harsh; offence’; Du. toorn ‘anger’; Cz. dna ‘gout’. (For Cz. dma, Latv. dusmas, etc. see dhusm-)
3225:obscure; darkness' etc. Cf. dhusuos, dhuuos, etc. WP I, 840 Gk. tüphos “smoke, steam”: tüpho, fut. thüpso ‘smoke’; cf. kóssuphos, kót-tuphos *'black- bird", lit. *dark-head', cf. koto-); Olr. dub ‘black’; duibe ‘obscurity’; W du, Br. dü, OBr. du-; Cor dü adj. ‘black’; Du. dof ‘dull, misty’ beside duf ‘stuffy, dank’; NWG doóff “fog” (IE Sot OHG tūba; OS dupa; Du. duif; OE *dūfe ‘dove’ beside Du. (-ü-) doffer ‘male pigeon’. An extended form of type *dhubht- occurs in G (fr. LG) Duft ‘vapour’; ON dupt ‘dust
3273:dhūmāið, eið (ið) ‘steam, smoke, breathe, blow’. WP I, 835. See dhümos Skt. dhüumáyami, tr. ‘cloud over; Gk. cf. thumiáo Cemoulder", ambig. cf. dhusmo-); Lat. fümo, are ‘smoke, foam’; OHG *a-tumon (spelt àdhmon: “blow, breathe. See FK: atmen); OCz. dýmu, ati (and dymaju), v. “blow, sigh, swell’; Cz. dymám “smoke”, intr.; OCS dymiti se, intr. id. (: Skt. dhümye, mp. id.; Li. dümiju, yti, id.)
3296:dhümos “smoke, vapour, fog, spirit, breath. WP I, 835. Cf. dhusmos Skt. dhümáh also npl. dhümáàh: ‘smoke, vapour; Gk. (ambig.) thümós (/vapour, breath, spirit”, cf. dhusmos); Lat. fümus; OCS dymü; Li. dúmas & (pl.) dümai. See next
3297:dhumsos, om, à (dhusmos) ‘swell, vapour, enthusiasm, animus'. Cf. dhunmn-, dhüs-. (Some of the evidence is ambig.). See dhü- mos above Arm. dum, gs dmo “cold, catarrh, influenza”; Gk. cf. thüma ‘incense; sacrifice’ (ambig. also thumós ‘vapour, breath"); Ir. cf. dámas (fr. *dhümestis) ‘pretence’; Du. dons, EMDu. dons, EMDu. donst "down (uff: OHG cf. dunist ‘vapour’; G (fr. LG) Dunst, id.; Pol. dasy, pl. ‘sulks’; Latv. cf. dusmas, pl. “anger”; G (fr. LG) cf. dunsen, v. *puff up'
3307:dhunmn-, dhunno- (smoke-coloured, murky, dun, dim'. Cf. dhusmos. WP I, 846. (Some of the evidence is ambig.) Av. cf. dunman “cloud, vapour’; Gk. cf. thün- nos, thünné 'tunny'; Sequanian duman *over-
3331:dhurkos, å — dhuskos
3339:dhus- (1) ‘whirr, buzz; whirring object, spindle’. Cf. WP I, 564 & 844. See following entries Per. dük (‘spindle’. For -k cf. Per. xūk ‘pig’, fr. *sūs); Gk. cf. thus- thia, n. pl. “Bacchanalian rods’; Lat. fūsus ‘spindle’; MHG cf. tūsen ‘rush, roar, ring; Sw. düs 'carousal. (Iso- phonic: Latvian dūša *courage")
3340:dhüs- (2) ‘rest’. Cf. dhusos (1) and (2), and
3342:dhusəlos (dhuslos), is, iə ‘blow; breath; vapour; smell". See next Gk. cf. thuélla ‘storm, gale’ beside gé-thullís garlic or sim. cf. for semantics Fr. “fume- terre’); Alb. cf. dulli, gs dullini ‘juniper’; Ir. dúil (1) ‘desire’; ON (alleged) dusill “fire”; Li. dusulys, io ‘asthma’; Latv. dusulis, id. Isophonic forms include (?) Armenian doyam (shudder, start’, fr. dhusláà- 7); ON dusla, v. ‘potter round’; Li. duslüs ‘dull, heavy, of sound, Cf. dhüs- (2)
3343:dhusoros (1) ‘wild; rage; demon’. See dhus-,
3344:dhusolos, etc. Gk. cf. (?) a-thúrð “play, mock’, thustás; ‘priestess of sacrifice; Olr. (ambig.) dorr (anger. Cf. dus- and cpds.); MHG tuster ‘demor. (Isophonic are LG düren ‘moan’; Norw. dure 'roar, drone', and Sw. dial. dura ‘slumber, let slumber’)
3345:dhusəros (-ön) (2) ‘ferret, polecat, skunk’ Lat. füro, gs -onis (‘ferret’ or *weasel); OCS düxorí, OCz. dchoř ‘pole cat: Finn. LW tuhkuri ‘mink’
3346:(dhüsolos, dhüsoros. See next and dhusəlos) Skt. dhüsarab 'dust-coloured, grey’. (Iso- phonic: Du. duizelen "be dizzy'. Isophonic radical in OCS dy$o, dyxajo “blow, breathe’; Li. dusauju and düstu 'gasp)
3347:dhuskos "dark" Cf. dhus- and cpds. WP I, 846 Lat. fuscus; OE dox, dux ‘fallow’; E cf. dusk; G cf. ver-tuschen, v. *hush up'; Norw. cf.
3350:dhusmos ‘vapour, breath; anger. Cf. WP I, 835 & 846 Gk. (ambig.) thümós ‘soul, breath, life’; Alb. dufém, duhém, f. “breath, oppression’; OE cf. (alleged) dysm ‘steam, smoke’; Latv. dusmas, fpl. “anger”. (A parallel form is re- presented in OHG tusin, OS dosan, MHG tusen-var, -vech *mottled with yellow" fr. a type *dhusnos)
3351:dhusó, ið (1) blow, breathe, steam, smoke’. Cf. dhusos & cpds.
3355:dhüsos, à, iə (1) ‘roaring, raging; fury, demon’. Cf. WP I, 846 and next. Gk. cf. thúas, thuiás “sibyl, bacchante'; Gallo- Lat. dusius ‘demon’; Ir. cf. dos ((1) ‘froth; vigour’, fr. *dhust-); OHG tüsig, OE dysig ‘mad, foolish’ beside MHG tüsen ‘rush, roar, ring’; tuster ‘demon’; Li. düsë, düsia “water- beetle’ (semantics obscure)
3356:dhüsos, à io (2) ‘breathing; breath, fra- grance'. WP I, 846. (Same as (1) ?). Variant: dhusuos, io (or dhuuos, io). See dhuuos Gk. tháos, n. ‘sacrifice’; tháa, thuía ‘fragrant cyprus’; cf. Myc. tuwea, npl. (queried: ‘spices’: Gk. thúea, id.); cf. gé-thuon “garlic, welsh onion’ or sim.); W dywy ‘vapour, fog; MHG cf. toste, MLG doste (G Doste fr. LG) “wild thyme’ or ‘marjoram’; Cz. dech ‘breath’; Li. dusas ‘asthma’, Latv. dusa ‘breathing; slum-
3357:dhusmos — dhuer-
3368:dhuuos, io (variant of dhusuos (?). See dhusos (2)) Myc. cf. mara-tuwo- ‘fennel’; tuwea queried: ‘spices’; Gk. cf. géthuon, thüea, etc.; Sw. cf. dugg-regn ‘scotch mist’; dugga, v. ‘drizzle’; W dywy ‘vapour, fog
3378:dhuésimos (dhuesmos) ‘breathing; breath, gasp'. Cf. dhueso & dhus- Alb. i dejmé, adj. ‘drunk’; Li. dvesimas “death, of an animal’; Latv. dvésma “breath”
3379:dhuéslos, à “dying, becoming a ghost; wraith, spirit. Cf. dhueso, dhus- Skt. (ambig.) dhvasráh ‘decaying’; Gk. séllos ‘guardian of Dodona oracle’; Li. dveslà ‘de- crepit person; wraith’; Latv. cf. dvēsele ‘souľ. (The element *dhues- seems to be present in Gk. séseli ‘hartwort’, fr. *dhue-dhuesli-, and some other scented plants, cf. sélinon)
3380:dhuésnom, à (dhués-, dhuésmà) ‘wraith; spirit abode’. Cf. dhueso, dhuesos, dhus-. Cf. WP I, 867 OLat. fésiae; Lat. feriae, festus; cf. Féronia (epithet of Juno); Osc. fiíísnu ‘temple’; Li. dvesnà ‘wretch? beside dvésena ‘domestic animal that has died’; Latv. cf. dvesma ‘breath’
3418:Av. dvar(eimi), v. ‘rush’; Gk. thoüros “rush- ing’; Ir. duar ‘crowd’; cf. also Skt. a-dhvaráh (a religious ceremony); Sw. däre "Tool dhuoros “entrance, court. WP I, 871. Cf. dhuer-, dhur- Lat. (ambig.) forus *hatchway'; forum *mar- ket; OCS dvorü (and com. Sl.) ‘court, yard’; Li. dváras (farm. Perh. SI. LW) dhuos- *drooping, ailing; spirit, exhalation, expiry’. Cf. dhues-, dhus- Skt. cf. (ambig.) dhvasrah *withered"; MIr. dássaim *madden'; EME cf. dwas-light *will- o"-the-wisp'; Sw. dåse (“sluggard”, cf. E dial. dozy, fr. Scand.); dásig ‘sleepy’; Li. dvásas, dvasià ‘spirit’; dvasus ‘ailing, pining (dhuriə, a zero-formula to dhuer-, dhuor-, dhur- ‘door’. etc.) WP I, 870 Gk. thairós singularized: ‘hinge of door
5099:(guadhus ‘deep, low’ only in Gk. bathús, id. See guādh-)
10418:medəlos — medheuos (medhuos, medhus)
10434:medheuos (medhuos, medhus) ‘honeyed, soaked in honey or mead, tipsy’. Cf. medhu, etc. WP II, 261 Skt. cf. mádhavah “an intoxicating drink’; mádhuh “sweet'; Ir. meadhbh ‘fed on mead:
15069:sedh- (sedhos, -es-, sedhus) ‘manner, custom, way’. Cf. suedh-. (Gk. ambig.) WP IL, 456
20280:uidhus, u “wood, scrubland, thicket’. Cf. uidheuos “set aside? (?). WP I, 239 Skt. vidhüh, adj. ('isolated". Here? cf. ui- and dhe-, lit. “set apart"); Phrygian ida, íde, f. *for- est, wooded hill; timber' also (dial.) bída-, id. (but a place-name Idajo- occurs in a My- cenaean context at Knossos!); Olr. fid, gs: fedo, m. *wood, forest'; Ir. fiodh, m. *wood,
20282:see uidus); Gaul. vidu- ‘forest’; OBr. uiid- ‘wood, tree’; W gw$dd, coll. ‘trees’; gwydden, f. ‘tree’; Br. gwéz, coll. as W; gwézen, f. sg. as W; cf. gwéz, adj. ‘wild’; Cor. gwydh, coll. as W; gwedhen, f. sg. as W; OHG witu, m. *wood, timber; MHG wit, wite m. n. id.; OS widu, m. “wood, forest; timber; OE wudu, pl. wudas, m. as OS; ON viór, gs: viðar, npl. vióir, apl. vióu, m. as OE & OS; Norw. ved, mf. s. ‘firewood’; Sw. ved, m. (^wood' usu. in cpds.); (NB. The identity of type *uidhus, u, and type *uidus, q.v. is obscured by phono- logy in Ir. fiodán, m. ‘pith, marrow���: Latv. videnis *torso, rump' and Li. Latv. vidus, m. *middle)
20287:uidhus, u — ulio
=== fusus in IEC
3339:dhus- (1) ‘whirr, buzz; whirring object, spindle’. Cf. WP I, 564 & 844. See following entries Per. dük (‘spindle’. For -k cf. Per. xūk ‘pig’, fr. *sūs); Gk. cf. thus- thia, n. pl. “Bacchanalian rods’; Lat. fūsus ‘spindle’; MHG cf. tūsen ‘rush, roar, ring; Sw. düs 'carousal. (Iso- phonic: Latvian dūša *courage")
=== dhwer/dhuer POK
POK_01.txt:565:ai.  ddlivan  m.  =  av.  advan  m.  ;Weg,  Bahn'^;  wozu  ai.  adhvard-h  , religiöse Handlung^  (ui'sprüngl.  ^Gang*  —  ^feierlicher  Gang^)  aus  ^ndhuero-,  und wohl  auch  mit  Suffixablaut  (*ndhitro-)  isl.  gndurr  m.  ,eiiie  Art  Schneeschuh'.
POK_01.txt:1891:forö,  -äre  ,bohreu,  durchbohren*  (Bed.  wie  ahd.  borön,  aber  im  Ablaut verschieden;  Denominativ  von  einem  *bhorä  ,das  Bohren*), /o7'äme»  ,Loch*p forus,  -l  ,Schiffsverdeck;  Bretter,  Fächer  für  Bienenkörbe;  Sitzreihen  im Theater;  Spielbrett*;  aber  /o?'wm  (alat.  auch /orits)  ,Marktplatz*  nicht  als ,umplankter  Raum*  hierher  (umbr.  furo,  für u  ,forum*);  s.  unter  dhuer-.
POK_01.txt:3819:6.  r-Erw. :  dheuer-  (dhuer-,  dheur-)   ,wirbeln,  stürmen,  eilen;  Wirbel    ^
POK_01.txt:3967:Idg.  dhreugh-  ist  sehr  wahrscheinlich  verwandt  mit  dhuer-  , durch  Täu5 schung  zu  Falle  bringen',  indem  zur  Schwundstufe  *dhru-gh-  aus  *dhuY't sich  neue  Hochstufen  idg.  *dhreugh',  *dhrough-  einstellten.  Mit  dem  er- weiternden gh  wäre  das  von  nhd.  Zwerg  identisch,  wenn  dieses  Wort' nicht  auf  ein  verschiedenes  idg.  dhuergh- , zwerghaft,  verkrüppelt'  (s.  dort) zurückgeht.
POK_01.txt:3986:dbuer-,  dhuerQ-  , durch  Täuschung,  Hinterlist  zu  Fall  bringen,  schädigen* ( :  dhuf- :  ditru-).
POK_01.txt:3987:Ai.  dhvdrati  , beschädigt',  Partiz.  dhrutd-,  -dhrut  (und  -dhvft),  dhruti- f.  , Täuschung,  Verführung',  *dhvard-  , trügend'  in  dkvards-  f.  (Nom.  -äh) ,eine  Art  weiblicher  Dämonen';  dhürvati  , bringt  durch  Täuschung  zu Fall,  beschädigt'  (Tiefstufe  einer  schweren  Basis  dhuer9-),  dhurta-h  ,he- trügerisch',  m.  ,Betrüger',  dhürti-  f.  ,listige  Beschädigung' ;
POK_01.txt:4009:dhuergh'  :  drugh-  ,zwerghaft,  verkrüppelt'?
POK_01.txt:4011:Für  das  germ.  Wort  käme  andernfalls  die  Deutung  als  , Trugwesen'  in Betracht,  zu  ai.  dhvards-  ,eine  Art  weiblicher  Dämonen',  Wz.  dhuer-  , durch Täuschung  zu  Fall  bringen';  es  wäre  von  dhuer-  dann  mit  demselben  -gh abgeleitet,  das  auch  in  der  WutzqM.  dhreu-gh-  begegnet  {dhuer-gh- :  dhurgh- : dhrugh-y  dhreugh-)]  auch  letzterer  entstammen  Bezeichnungen  für  kobold- artige Trugwesen.
```


## [2026-09-05T20:07:42.784Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT duvara\"\ngrep -n \"duvara\\|duvarayā\\|dvar\" KNT.txt | head -30\necho \"=== AHD dhwer\"\ngrep -n -i \"dhwer\\|dhur\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-05T20:07:42.870Z] TOOL RESULT

```
=== KNT duvara
1072:dhardydms. pIE *dhyor- ‘door’, in OP loc. duvaraya, Av.
1073:dvar-, Skt. dhvar-, cf. Gk. бра. OP ba"daka ‘subject’, to pIE *bhendh-, $75.11. OP hadé ‘with’, Skt. sahá, from pIE *sm-dhe; same suffix in avadà, idä, ada-kary.
1600:$129, Hapiotogy is the loss of one of two similar sequences of sounds, each containing at least one consonant and one vowel, or one vowel and at least one consonant: thus English min- eralogy from *mineralology. OP has one certain example, hamátü from *hama-māiā ‘having the same mother’, cf. hama-pilà ‘having the same father’, where no haplology is possible. A second example, probable but less certain, is duvarfim from *dvar-varðim ‘door-cover’, = ‘colonnade’. Possibly also arštā- ‘rectitude’ from *arSta-td-, but cf. Lex. s.v.; and didiy ‘see thou’, if redupli- cated pres. imv. *dht-dhi-dht rather than aor. шту. *dhi-dhi.
1657:Locatives with postpositive à: -di(y) became -dy- before the à, as in duvarayd from *dvarai + à, Aturáyü from *Адит + à. But the script does not show whether locatives in -i changed the 7 to y before d, or kept the vowel by analogy: drayahyü (once -hiyà) may repre- sent either -hj- or -háj-.
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2702:A. Expressing place where, without a preposi- tion, as in DB 1.34f pasdva drauga dahyauvā vasiy abava щй Parsaty ша Madaty ша aniyãwā dah- yusued ‘afterwards the Lie waxed great in the country, both in Persia and in Media and in the other provinces’; DB 2.75 duvarayãmaiy basta аййттуа ‘he was held bound at my palace en-
3618:75 iy : І casam : avajam : duvarayamaiy : basta : adáriya : haruva$im : К
3632:89 dham : utd : gaušā : frājanam : utāšaiy : I casam : avajam : duvarayà
4976:-maiy gsm. (gen.-dat. GAv. mót, LAv. mé, Skt. me, Gk. dat. но, pIE *mot) enclitic to айа (nsn., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°; DPh 8, 10; DNa 50 (m° omitted, $52.VI), 52#, 544; DNb 13, 28, 28f, 31, 32f, 33, 48, 51, 52; DSe 51°, 52°; DSE 10, 19°, 20°, 58; Ds} 4°, 6°; DSk 5; DSI 4f; DSm 3°; D8s 7°; DSt 9°; DH 6, 8; Хра 15, 18f, 191; XPb 24, 29, 30; XPe 13 bis; ХРа 18f, 19; ХР 32, 38, 41, 45f, 47; XPg 14; XPh 32, 45, 58,
5568:duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
=== AHD dhwer
169:The house (deme-') included a dhwer- (DOOR), which probably referred originally to the gateway into the enclosure of the house- hold. The house would have had a central
396:dhwer-. Door, doorway (usually in plural). Originally an apophonic noun *dhwor-, *dhur-, in the plural, designat- ing the entrance to the enclosure (*dhwor-o-) surround- ing the house proper. 1. Zero-grade form *dhur- in suffixed forms *dhur-ns (accusative plural) and *dhur-o- (neuter) respectively in Germanic *durunz and *duram in Old English duru, door (feminine, originally plural), and dor, door (neuter): DooR. 2. Suffixed o-grade form
399:FORFEIT. 4, Suffixed o-grade form *dhwor-o- in Latin forum, marketplace (originally the enclosed space around a home): FORENSIC, FORUM. 5. Zero-grade form *dhur- in Greek thura, door (> thureos, shield): THYROID. 6. Per- sian dar, door, gate: DURBAR. [Pok. dhyér- 278.]
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1432:DOGE deuk- pocMa dek-1 pDoGMaTIC  dek-! DOIT twei- DOLABRIFORM del-3 DOLCE dik-u- DOLDRUMS_ dheu-t DOLE! dail- DOLE? del-3 DOLERITE del-2 DOLICHOCEPHALIC del-1 DOLICHOCRANIAL  del-1 DOLOR del-3 DOLPHIN gWelbh- Dott dheu-1 Dom deme-1, dhé-1 DOMAIN deme-! DOME deme-1 DOMESTIC deme-1 DOMICILE deme-! DOMINATE deme-1 DOMINICAL deme-1 DOMINIE deme-1 DOMINION deme-' DOMINO! deme-1 DOMINO2 deme-1 DONATION d6- DONATIVE d6- DONOR do- poom dhé-1 pooR dhwer- DOPE dub- DORMANT drem- DORMER drem- DORMITORY drem- DORSAL dorsum poRrsO- dorsum pory? aurum DOSE dé-
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
1503:FATE bha-2 FATHER peter- FATHOM pete- FATIDIC deik- FAUBOURG bhergh-?, dhwer- FAVA BEAN bha-bha- FAVOR ghow-é- FAVORITE ghow-é- FAWN! pek-t FAWN? dhé(i)- FAY} pag- FEALTY bheidh- FEAR per-4 FEASIBLE dhé-1 FEasT dhés- FEAT! dhé-1 FEATHER pet- FEATURE dhé-1 FEBRIFUGE bheug-! FECUND dh@(i)- FEDERAL bheidh- FEDERATE bheidh- FEE peku- FEEBLE bhlé-1 FEED pa-
1533:FORE- pert FORECLOSE dhwer- FOREFATHER per, peter- FOREGO! ghé- FOREIGN dhwer- FOREMOST per! FORENSIC dhwer- FOREST dhwer- FORESTALL | stel- FORFEIT dhé-1, dhwer- FORFICATE bherdh- FORGE! dhabh- FORGET ghend- FORGIVE ghabh- FORGO ghé- FORLORN leu-! FORLORN HOPE keu-?, leu-1 FORM merph- FORMAL merph- FORMER? per! FORMIC morwi- FORMICARY morwi- FORMICIVOROUS morwi- FORMULA merph- FoRNAX gWher- FORNICATE gWher- FORSAKE sag- ForT bhergh-2 FORTALICE bhergh-2 FORTE! bhergh-2 FORTE? bhergh-2 FORTH pert FORTIFY bhergh-2 FORTIS bhergh-2 FORTISSIMO bhergh-2 FORTITUDE bhergh-2 FORTRESS bhergh-2 FORTY kWetwer- FORUM dhwer- Fossa bhedh- FOSSE bhedh- FossIL bhedh- FOSSORIAL bhedh- FOSTER pa- FOUDROYANT bhel-1 FOUL pu-2
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
```


## [2026-09-05T20:07:52.361Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '392,402p' AHD_watkins1985.txt\necho \"=== POK Tür\"\ngrep -n \"Tür\\b\\|,Tür'\\|Türe\" POK_01.txt | head -30"
}
```


### [2026-09-05T20:07:52.420Z] TOOL RESULT

```
dhugheter-. Daughter. Germanic *dohtér in Old English dohtor, daughter: DAUGHTER. [Pok. dhug(hjeter 277.]
dhino-. Fortified, enclosed place. (Only in Celtic and Germanic.) 1. Possibly Germanic *diinaz, hill, in: a. Old English diin, hill: DowN!, Down’; b. Middle Dutch dine, sandy hill: DUNE. 2. Celtic *diin-o-, hill, stronghold, borrowed into Germanic as *tinaz, fortified place, in Old English tin, enclosed place, homestead, village: TOWN. [In Pok. 4. dheu- 261.]
dhwen-. To make noise. Germanic *duniz in Old English dyne, noise: DIN. [Pok. dhuen- 277.]
dhwene-. To disappear, die. Suffixed zero-grade form dhwna-tos in Greek thanatos, death: THANATOS; EUTHA- NASIA, TANSY. [In Pok. 4. dheu- 261.]
dhwer-. Door, doorway (usually in plural). Originally an apophonic noun *dhwor-, *dhur-, in the plural, designat- ing the entrance to the enclosure (*dhwor-o-) surround- ing the house proper. 1. Zero-grade form *dhur- in suffixed forms *dhur-ns (accusative plural) and *dhur-o- (neuter) respectively in Germanic *durunz and *duram in Old English duru, door (feminine, originally plural), and dor, door (neuter): DooR. 2. Suffixed o-grade form
dwo-
*dhwor-dns (accusative plural) in Latin fords, (toward) out of doors, outside: FOREIGN. 3. Suffixed o-grade form *dhwor-ois (locative plural) in Latin foris, (being) out of doors: FOREST; (AFFOREST), FAUBOURG, FORECLOSE,
FORFEIT. 4, Suffixed o-grade form *dhwor-o- in Latin forum, marketplace (originally the enclosed space around a home): FORENSIC, FORUM. 5. Zero-grade form *dhur- in Greek thura, door (> thureos, shield): THYROID. 6. Per- sian dar, door, gate: DURBAR. [Pok. dhyér- 278.]
digh-. She-goat. Germanic *tigon (with expressive conso- nantism) in Old Norse iik, bitch: TYKE. [Pok. digh- 222.]
dik-u-. Sweet. 1. Suffixed form *d/kw-i- in Latin dulcis (>
French doux), sweet: DOLCE, DOUCEUR, DULCET; BIL- LET-DOUX, DULCIFY. 2. Basic form *dlku- (with *dl- dissimilated to *gl- in Greek because of the following k) in: a. Greek glukus, sweet: LICORICE; b. Greek glukeros (with suffix *-ero-), sweet: GLYCERIN; Cc. Greek gleukos (with suffix -es-), must, sweet wine: GLUCOSE. [Pok. dlki- 222.)
=== POK Tür
580:Ai.  ätä  (gewöhalich  PI.  ätäh  wie  lat.  antae)  ^Umfassung-,  Rahmen  einer Tür^;  ar.  <ii^yä  Akk.  PI.  ,Türpfosten%  arm.  dr-and  ^Türpfosteii^  (HUbsch- mann  Arm.  Stud.  I  19);  lat.  antae  nach  Vitruv  3,  2,  2  ,die  frei  endigenden und  vorn  etwas  verstärkten  Wände,  die  den  Pronaos  eines  Tempels  oder die  Prostas  eines  Hauses  einschließen*  =  anord.  ond  ^Vorzimmer*  (Bugge KZ.  19,  401).
1320:\t  Ablaut  nhd.-bair.  pfotizer,  pf unzer  ^zugespitzter  KnütteF;  mit  den kolt  Formen  entsprechendem  /i-Suffix  (*penn-  aus  *bend-n-)  and.  pin Dixilhis^  nind.  piih  P"^^6  ^Pinne^  Spitze^  Nagel,  Pflock^,  mhd.  pfinne  f. Va^ol^  a^-s.  pinn  ^Pflock,  Stift^,  spätaisL  pinni  m.  ds.,  ablaut.  *pan7i- in  ostfries.  penne  =  pinne,  nd'd.  pennen  ,eme  Tür  (mit  einem  Bolzen) verrieo-eln'^;  ags.  on-pennian  ^öffnen^,  engl,  pen  ^schließen'^,  ags.  penn  m. ,Pferch^
3993:dhu^r-,  dhuor-f  dhur-,  dhur-  ,Tür^-  neben  diesem  kons.  St.,  der  ursprüno-j ein  Plurale  und  Duale  tantum  war  (s.  u.),  stehen  zum  Teil  Avohl schon  urspi-achli  he  -o-  und  -ä- Erweiterungen  teils  mit  zu  vermuten der  kollektiver  Bed.,  teils  (als  Neutrum)  in  der  Stellung  als  2.  Kompo- sitionsglieder.
3994:Ai.   Nom    PI.   dvnrah,  Akk.   PI.  durah,  durah,  Nom.   Du.  dvärä(u)  ,Tüpt (Verlust    der    Aspiration    ursprüngl.    in    den    5/j-Kasus   durch   Einfluß  von  M dvöu    jZwei'),    durönd-    n.    ^Wohnung-,    Heimat'    (-?io-A bleitung    vom  .Lok.  ij Du.  ar.  *dhuräu)]   o-St.    dväram   n.  (jung)   ,Tür*   in   Kompositis  satddura-  "^ n.  ,mit   100  Türen  verschlossener  Ort';   av.  Akk.   Sg.  dvardm,  Lok.  dvavd ,Tor,  Hof,  apers.  duvarayä  ,am  Tore';
3995:arm.  PI.  dur-lc,  Akk.  z-durs  (*-ws)  ,Tür',  t   durs  ,hinaus,   draußen',  Sg. dufn,  Gen.  dran  ,Tür,  Tor,  Hof   (die  n-Dekl.  vom  Akk.  Sg.  auf  -m  aus- egangen),  dr-and  ,Türpf()Sten,  Türschwelle'  (*dhtir  -j-  *andtä,  s.  dort);
3996:g-r.  vermutlich  vom  kons.  St.  noch  d-v()da'  e^o)  l^g-Aadsg  Hes.;  &vQa}^a jhinaus'  (d.  i.  ^vgcca-de^  entweder  ai.  durah,  arm.  diirs  oder  vom  ä-St. d-vgä,  so  daß  aus  -avg  über  -ävg),  als  1.  Komposiiionsglied  vielleicht  Ovq-I avlso)  ,habe  meinen  Aufenthalt  an  (vor)  der  Türe,  lagere  im  Freien'  von^ ■d-vQ-avXoq  (kann  aber  auch  von  d-voa  ausgegangen  sein),  sehr  altertümlich -d-aiQÖg  ,der  drehbare  Türpfosten'  (auch  , Wagenachse,  Eckpfosten  des Wagenkastens'  aus  *dhur-io-) ;
3997:o-St.  in  Ttgoi^vgov  ,Raum  vor  der  Tür,  Vorraum  des  Hauses'  (:ai.  satd- dura-  n.);
3998:ä-St.  ^vga  ,Tür'  (bom.  meist  PL),  att.  ^vgäai  ,draußen',  hom.  ^vgr^-d^i,  ^ -(pi;  vgl.  noch  d-vgiov  , Türchen'  (:ai.  dür{i)ya-  ,zur  Tür  oder  zum  Haus  W gehörig'),  d-vuiq,  -tdog  , Fenster'  (eig.  ,Türchen')  dvoergov  ,Tür',  ^ugsög  ,Tür-  # stein;  großer  langer  Schil  ',  dvgoiv  , Vorhalle,  Vorraum  im  Haus'  (:got.  ^^, daüröns  f.  PI.  ,zweiflügliges  Tor',  doch  kaum  in  geschichtlichem  Zusammen-  r- hang  damit);  E
3999:alb.  dcre  f.  ,Tür',  PL  diler  (kons.  St.  *dhuör-)]  ^
4000:lat.  Plur.  fores  f.  »zweiflüglige  Tür'  (alter  kons.  St.  *dhuor-  zum  i-St. umgebildet);  der  Sg.  foris,  -is  ist  sekundär;  ö-St.  in /oräs  , hinaus', /orw , draußen,  außerhalb'  (der  Vokal  nach  fores);  da.zu  forum  n.  , Vorhof  des Grabes,  Marktplatz,  Bretterkasten  für  die  Trauben';  umbr.  fui^o,  furu, jforum^]  über  lat.  forus  s.  oben  S.  134;
4001:cymr.  abret.  corn.  dor  f.  ,Tür'  {*dhurä  oder  *dhuorä',  letztere  Vokal- stufe sicher  in  air.  dorus  n.  ,Tür',  in-dorus  ,vor'  aus  kelt.  *duorestu-; damit  lautlich  nicht  vereinbar  cymr.  di'ws  ,Tür',  von  Thurneysen  lA.  33, 25  zu  mir.  drut,  druit  , schließen',  nir.  druidim  ,ich  schließe'  aus  *druzd- gestellt);  o-St.  gall.  doro  ,ostium',  Duro-,  -durum  in  ON,  air.  dor  m.  ds.; acorn.    darat,    mcorn.    daras  ,Tür',  bret.  PL  dorojou,    dial.  doredou    (Loth
4004:ahd.  ttiri,  anfränk.  duri  ,Tür',  anord.  dyrr  ,Türöffnung',  fem.  PI.  (Nom. pl.  *dhur-es)',  ags.  d^tru  ds.  (Akk.  PL  *dhur-nü,  germ.  *durunz,  der  auch ahd.  Dat.  PL  tur-nn,,  -on  nach  sich  zog);  o-iSt.  got.  daür  n.,  ahd.  tor^  as. dor^  d'^'^^1  3.gs.  dor  n.  ,Tor'  (*cZ/iwrom);  got.  dauröns  s.  oben  (:  d-vocjv)', aisl.  for-dyri  n.  , Vorraum';
4005:lit.  c?tm5  Akk.  PL  cZwr^  Gen.  PL,  dial.  und  alt  düres  Nom.  PL  (dann {-Flexion:  Nom.  PL  d'ärys)^  lett.  duris,  dürvis,  apr.  dauris  f.  PL  ,Tür* (rti<  Fehler);  hingegen  braucht  lit.  dväras  , Gutshof*  wegen  dverli  ,sich öffnen*  (also  dürys  ^Tüv''  aus  ,*Offnung'?)  nicht  unbedingt  poln.  Lw.  zu  sein;
4006:aksl.  dvbri  ,Tür*  (*Akk.  PL  auf  -ns;  Wurzelst,  dhuj--  aus  den  schwachen Kasus  mit  Kons. -Endung  z.  B.   Lok.  ''^dvbrchz);  o-St.  aksl.  dvorh  ,Hof*;
4007:toch.   B  tivere  ,Türe*.
4291:lat.  Jänus  ,altital.  Gott  der  Türen  und  des  Jahresanfangs*,  jänua  ,Türö*;^
```


## [2026-09-05T20:07:53.237Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"dhur-\\|dhuor-\\|dhuer-\" POK_full.txt | head -30; echo ---; grep -n \"^ *dhuer-\\|dhu̯er\" POK_02.txt | head"
}
```


### [2026-09-05T20:07:53.322Z] TOOL RESULT

```
---
```


## [2026-09-05T20:08:05.192Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=3960 && NR<=4010' POK_01.txt | grep -n \"^\\s*27[5-9]\\|^\\s*28[0-2]\" ; echo \"--- context lines 3985-3993\"; sed -n '3988,3993p' POK_01.txt"
}
```


### [2026-09-05T20:08:07.451Z] TOOL RESULT

```
2:276
18:277
32:278
43:279
--- context lines 3985-3993
lat.  fraus,  -dis  f.  , Betrug,  hinterlistige  Täuschung,  Schaden,  Strafe', frausus  sum  (Plaut.),  umbr.  frosetom  ,fraudätum*,  lat.  früstra  (jünger früsträ)  , irrtümlich,  vergeblich',  davon  früstror,  -äri  ,täusche,  hintergehe' gehören  wohl  als  c?-Erweiterung  unserer  Wurzel  hierher  (s.  darüber  unter dhreugh-)-^  unklar  ist  nur  das  a  (mot  populaire?  EM  382;  unglaubhaft WH.  I  543);
hierher  wohl  hitt.  du-wa-ar-na-ah-hu-un  (dwamahhun?)  ,ich  brach'.
WP.  I  869  f.,  874,  WH.  I  543  f.^  ^
278
f
dhu^r-,  dhuor-f  dhur-,  dhur-  ,Tür^-  neben  diesem  kons.  St.,  der  ursprüno-j ein  Plurale  und  Duale  tantum  war  (s.  u.),  stehen  zum  Teil  Avohl schon  urspi-achli  he  -o-  und  -ä- Erweiterungen  teils  mit  zu  vermuten der  kollektiver  Bed.,  teils  (als  Neutrum)  in  der  Stellung  als  2.  Kompo- sitionsglieder.
```


## [2026-09-05T20:08:07.648Z] TOOL CALL #12: Bash

```json
{
 "command": "pdftoppm -f 136 -l 136 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg136\" 2>/dev/null; SC=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 136 -l 136 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $SC/pg136 && ls -la $SC"
}
```


### [2026-09-05T20:08:10.152Z] TOOL RESULT

```
total 1420
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:08 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
```


## [2026-09-05T20:08:16.089Z] TOOL CALL #13: Bash

```json
{
 "command": "SC=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 136 -l 136 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf $SC/pg136_300 && ls -la $SC/pg136_300.png"
}
```


### [2026-09-05T20:08:18.850Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 68320 Sep  5 16:08 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg136_300.png
```


## [2026-09-05T20:08:20.914Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg136_300.png"
}
```


### [2026-09-05T20:08:21.772Z] TOOL RESULT

```

```


## [2026-09-05T20:08:21.764Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:08:41.897Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -rl \"Dhrugh\" data/extracted/batch/ | head; echo \"=== chart mentions\"; grep -rn \"Dhrugh\" data/verification/agent/charts/ | head"
}
```


### [2026-09-05T20:08:41.988Z] TOOL RESULT

```
data/extracted/batch/page-135.json
data/extracted/batch/page-136.json
=== chart mentions
data/verification/agent/charts/page-135.txt:28:ROOT Dhrugh -> redirect to Dhwer
data/verification/agent/charts/page-136.txt:9:ROOT [Indo-European] Dhwer, Dhrugh, Dhwor : door  (refs POK:278; KNT:191)
```


## [2026-09-05T20:08:43.502Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC page markers near 3339\"; sed -n '3320,3341p' IEC.txt | grep -n \"^[0-9]\\{2,4\\}$\\|page\"; echo \"--- raw\"; sed -n '3330,3340p' IEC.txt | cut -c1-120\necho \"=== POK 447-449 gheu\"; grep -n \"gheu-\\|ĝheu-\\|,gießen\" POK_02.txt | head -20"
}
```


### [2026-09-05T20:08:45.804Z] TOOL RESULT

```
=== IEC page markers near 3339
4:223
8:dhüro (2) (dhurn-, dhurs-) ‘rampage, rave’. Gk. cf. a-thüró ('play, fr. *sm-dhür-); MHG turren ‘tumble, stumble’; Srb. cf. drnem se, drnuti se ‘rage, rave’; Li. cf. *durnéju, éti, v. ‘grow stupid’; durnas ‘moonstruck’; Latv. durnët ‘drowse’; durns ‘numbstruck’; Norw. cf. dor-sk ‘sluggish’; cf. also Lith. (?) dursnoti ‘trip, trot
13:20
14:25
15:30
16:35
17:40
18:224
--- raw
dhurunkó, ið (dhrunk-) ‘rattle, clatter’. Cf. dhrun-
dhurkos, å — dhuskos
20
25
30
35
40
224
Arm. drnéim ‘tingle, ring’; Cz. drnkat, drnčet ‘clatter’; Blg. drănkam ‘jingle, rattle’
dhus- (1) ‘whirr, buzz; whirring object, spindle’. Cf. WP I, 564 & 844. See following entries Per. dük (‘spindle�
dhüs- (2) ‘rest’. Cf. dhusos (1) and (2), and
=== POK 447-449 gheu
1100:2.  ghe-  :  gho-  und  ghei- :  ghi-    (dazu    der    weitergebildete    Stamm    ghii-a) ,gähnen,  klaffen';    schallmalend   für  den  Gähnlaut  (s.  auch  u.  ghans- ,Gans';  ähnlich,  aber  mit  Velar,  gha  gha  für  gackern  und  dgl.,  s.  dort). Neben   ghei-  auch   gheu- :  ghdu-   (s.  dort),   entweder   als  andere  Auf- fassung  des   Gähnlautes,  oder   mit  ursprüngl.   formantischem  u.  Vgl. noch  1.  ghe-  ,leer  sein,  fehlen';   Specht  (Dekl.  282)  setzt  eine  Wurzel *agh-e-  usw.  an;  s.  oben  unter  ghan-, Gr.  x&oyux)    {ghd-skö)  , gähne,   klaffe'   (nur   Präs.  und  Impf. ;  später  von Xalvct)  abgelöst,  s.  unter  ghan-),  xdaiia  ,klaffende  Öffnung';  XVQ^^^g  ,Loch', XriQaf.Lvg   ,eine   große   Muschel',   nach   x^Q^i^^^'  ^  "^5?  7VS  ÖLdaxaGig   Hes., triXög  f.  ,Kiste,  Lade';  XW''^  ^das  Gähnen,  Gienmuschel'. Von  ghei-  aus:  aksl.  zejo  ,hio'  i^gheio). Von  §bii-ä-  aus:
1130:gheis-:  isl.  gisinn  ,von  Trockenheit  rissig,  undicht'  (Partiz.  von  *gisa norw.  dial.  glsa  ,^rinsen,  blinzeln';  norw.  dial.  gista  ,sich  öffnen,  du^ werden,  vom  Walde',  aschwed.  gistinn  ,von  Trockenheit  rissig';  aus  diese? Bed.  weiter  mnd.  gest,  afries.  gest,  gast  ,das  höhere  trockene  Land  i^ Gegensatz  zur  Marschniederung'  (zugehörige  tt-Formen  nd.  güste,  mjj^ gust  ,unfruchtbar,  trocken,  gelt'  von  der  Basis  gheu-??  S.  Persson Beitr.  318).
1568:gheu-  .gießen' ;  gheu-mn  , Opferguß'.
1581:got.  giutan  ,gießen',  aisl.  gjöta  , (Junge)  werfen',  ags.  geotan  ,gießen,^ fließen,  schütten',  afries.  jäta,  as.  giotan,  ahd.  giozzan  ds.,  nisl.  gjöut. ,Höhle,  enge  Gasse^,  aschwed.  giuta  , Gußform',  ahd.  giozo  ,fließende^ Wasser',  ags.  gyte  ,Guß,  Flut',  ahd.  guz  ,fusio',  ndd.  gete  ,niedrige  Wasser- straße', norw.  gota  , eingeschnittene  Rinne',  as.  gota  ,canalis',  holl.  gooi jGosse,  Rinne',  nhd.  Gosse,  ags.  gutt,  engl,  gut  ,Darm'.
1587:gheu-,  gheu-d-  ,verschwinden,  umkommen'.
1595:Ahd.  goumo  m.  (*ghdu-men-)^  giumo  (^gheu-men-)  , Gaumen',  ablaut.  anord. nömr  , Zahnfleisch,  Gaumen',  ags.  göma  (engl,  gums  , Zahnfleisch'),  ahd. guomo  (*^Äö[w]-m-)  ^Gaumen^ ]  über  lit.  gomurys  s.  unten;
1605:Norw.  dial.  güva  , zusammengesunken  sitzen^  schwed,  jordguhhe  , Garten,  - erdbeereS  alt.  dän.  guhhe  ,Kehlkopf,  Brust',  ndd.  (Estland)  guhhe  ^kleiner Heubaufen^;  ags.  geap  ,krumm,  listig'  (aber  gea]^  ,weit,  geräumig,  offea», aisl.  gaupn  ,hohle  Hand'  s.  unter  gheu-  ,gähnen,  klaffen'),  aisl.  gum^ (aus  ascbwed.  gumper),  scbwed.  gump,  dän.  gump  ,Steiß',  mbd.  guffe^  g^j^ ds.  (aber  über  mhd.  gupf  , Spitze  eines  Berges'  s.  unter  geu-  , biegen'), ags.  gupan  PL  ,clunes,  cloxae',  abd.  goffa  ,Steiß',  weiter  dazu  die  lutea- sivbildung  isl.  goppa,  scbwed.  guppa,  nbd.  gupfen  ,auf  und  nieder  hüpfen^ schaukeln' ;
2232:vielleicht  *ghu-el-  aus  einem  gheu-  ,schief'  erweitert;  vgl.  ^ghu-er-  in lit,  ziirU  ,eine  Rankenpflanze'  (*g^ur-lo-),  gv.  ^egfiog  m.  ,Feigenbohne^ (*guher-mo-).
5152:lit.  lieju,  lieti  , gießen'  (alt  leju,  idg.  *leio),  lija  lyti  , regnen,  strömen', lydau,  lyditi  , regnen  lassen,  Fett  zerlassen';  lytils  m.  ,Regen',  lytis  f. ,Form,  Gestalt'  (,*Gußform'),  ät-lajis  m.  , Abfluß ' ;  lett.  liet  ,gießen',  Mt , regnen',  lietus  m.  ,Regen';  lietas  und  lett.  liets,  vergossen',  supr.  pra-lieiton, pra-leiton  und  pra-liten  ds.;  is-liims  ds.;
5154:.  vielleicht  hierher  lit.  Lietuvä  , Litauen'  (»Küstenland'),  lett.  LeUis  , Litauer'; aksl.  Ujo  lijati  und  lijo  liti  ,gießen' ;  ablaut.  slav.  Hoj  ,Talg'  (lit.  ät-lajis Abfluß')  in  ksl.  loj  usw.:  slov.  pre-lit  , übergössen',  öech.  lity  , gegossen'; slav.  Präsens  Hhjg  ist  Neubildung.
```


## [2026-09-05T20:08:51.677Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=1500 && NR<=1600' POK_02.txt | grep -n \"^\\s*4[45][0-9]\\s*$\" ; echo \"---\"; sed -n '1560,1580p' POK_02.txt | cut -c1-200"
}
```


### [2026-09-05T20:08:53.390Z] TOOL RESULT

```
17:445
36:446
58:447
---
o-v.  x^iQ   f-  ,Hand^,   Gen.  xeiqdgj  dor.   xVQog,   Dat.  PI.  x^odt   (danach  die
Form  yjQ-)',
tocb.  A  tsa)%  B  sar  ,Hand^  (nach  Pedersen  Tochar.  236  aus  *kesar  =) bitt.    ki-es-sar    (kessa?-)    n.  und    ki-es-si-ra-as    (kesseras)    tu.,  i..    Dat.    Sg.
ki-ls-sa-ri  (kesri  =  gr.  x«^^^'?);
über  lat.  Jr,  hir  ,hohle  Hand^  (aus  osk.-umbr.  *Äer  <  ^ghesrä?)  s.  WH.  I  649.
2.  ghesto-  ;Hand;  Arm^
Ai.  hdsta-h  m.  ,Hand^,  av.  zasta-,  apers.  dasta-  ds. ; lat.  praestö  ,zur  Hand'  aus  ^^prae-liestod  (EM  805  f.)?;  anders  s.  unter  stä-] lit.  pa-zastZ,  pa-zastis  f.  ,Raum  unter
WP.  I  541,  603,  WH.  I  243,  Trautmann  367,  Duchesne-Guillemin BSL.  39,  211,  Schwyzer  Gr.  Gr.  I  446,  569,  Specht  Idg.  Dekl.  75.
gheu-  .gießen' ;  gheu-mn  , Opferguß'.
Ai.  juhöti,  juhuti  , gießt  ins  Feuer,  opfert',  Passiv  hüydte^  huid-h  , ge- opfert', höman-  n.  , Opferguß,  Opfer'  (=  gr.  x^v^a),  höma-h  m.  ds.,  hötar- , Opferer,  Priester', 
av.  zaotar,  zaod-r-  m.  , Priester,  Opferpriester',  mpers.  zöt,  av.  zaod-ra \\.,  zaod-rä  f.  , flüssige  Opferspende,  Opfertrank,  Opferguß',  npers.  zör ,Weihwasser',  av.  äzutay- 
arm.  joyl  , gegossen'  (<  gheulo-),  jeiv  ,Form,  Gestalt';  hierher  auch  Jor ,Tal'  (<  ghouero)  ?
phryg.  ^evLidy  rtrji^v  Hes.  (==  gr.  x^vi^a)',  thrak.  ^ergaia'  xvxqri  {*gheutr'\ FIN  Fsvöig,  -og]
gr.  xf(/)w  , gieße',  Aor.  hom.  ex^va  <  ^exsvaa,  Perf.  xf/vKoc,  x^'^oc;  , ge- gossen', xfr^/a  ,Guß,  Fluß,  Trankopfer',  x^^^^S»  X^^^g  , Schmelzgrube, Gußform',  x^V  ,Trankopfer  f
448  9
noU,    Ttlfjgeg   Hes. ;    x^^^tS   ,Guß\    x^^^S    .Saft'   (<  *ghuslo-,   W.  Schulze^t'^ mündl),   X'GiJLÖg   ds.   (<ghu-smo)',    weiter   hierher   xwo^iai   ,zürne,    bin   u^,  ^' wi
Lsitfä-tis  f.  , Gießkanne',  fü-tilis,  futtilis  gleicht  ausgießbar,  zerbrechlich, eitel,  unnütz',  eaj/«^i  =  effüsi,  effütiö  ,schwatze  heraus'.
Sehr  zweifelhaft  ist   die  Zugehörigkeit  von  mhd.  gül  ,männliches  Tier, Eber,  Pferd',  nhd.  Gaul  (im  Bayr.  ^Deckhengst',  Schweiz,  gül  ,Hahn',  vglj ndl.  guil  ,Stute,  die  noch  
"VVurzeler  Weiterungen:
gheud-:
lat.  fundö,  -ere,  füdl,  füsum  ,gieße,  lasse  fließen,  schütte  aus'  (übei füsus  ,Spindel'  s.  WH.  I  474)  ;
```


## [2026-09-05T20:09:04.846Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW fusus\"; grep -n \"fusus\\|füsus\\|fūsus\\|Spindel\" LEW_1910.txt | head -20\necho \"=== LAT fusus\"; grep -n \"fusus\" LAT.txt | head -20"
}
```


### [2026-09-05T20:09:04.927Z] TOOL RESULT

```
=== LEW fusus
=== LAT fusus
13200:aent, voir Rich. a.u. colus, fusus, ne 5 . Atteste depuis Plaute. Les
24865:repandre, s'£tendre au loin". Pcp.: fusus "qui se r^pand, diffus,
24877:fusus,-us a.: rare, ne seable pas attestO en dehors de Varr.,L.L.
24878:5,133, fons unde fund-itur e terra aqua uiua, ut fistula a qua fusus
25184:fusus, -Ia. (et plus tard fusum n.) : fuseau; eaploye surtout au
51260:fit pura: sic is sermo in quo pure disponuntur uerba, ne sit confusus
```


## [2026-09-05T20:09:05.679Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN duk\"; grep -n -i \"spindel\" HRN.txt | head -20\necho \"=== HUB\"; grep -n -i \"spindel\" HUB.txt | head -20\necho \"=== ARY duk\"; grep -n \"دوک\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T20:09:05.747Z] TOOL RESULT

```
=== HRN duk
=== HUB
=== ARY duk
```


## [2026-09-05T20:09:09.848Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25184,25205p' LAT.txt"
}
```


### [2026-09-05T20:09:09.896Z] TOOL RESULT

```
fusus, -Ia. (et plus tard fusum n.) : fuseau; eaploye surtout au
pl. Attest 4 depuis Catulle, mais sans doute ancien. - Panroman, M.L.
3Gqo. De la *fusdgo "fusain", M.L.3G08; *fuscellus, par contamination
avec *fusti ce Ilus? M.L.3615.
fitymologie inconnue.
futis, futio, futilis: v. fundo.
*f\ito, -as, -are?: attest 4 dans P.F.79,5, futare arguere est, unde
et confutare. Sed Cato hoc pro saepius fuisse posuit. La glose de
Festus confond deux verbes: i° un frequentatif du groupe de fu-am,
fu-i, eaploye par Caton; sj° un verbe futare (it 4 ratif-intensif de fundo?)
dont proviendraient con-futo, re-futo, non autreaent attest 4 et qui
est sans donte une reconstruction arbitraire faite sur les coapos 4 s.
D'autre part, on trouve dans le meae abr 4 g 4 de Festus, 347,3, refutare:
redarguere, compositum a fando (!) uersa a littera in u. Le sens premier
de confuto seable avoir ete "abattre; bouleverser, renverser"; cf.
Titin., Coa.138, cocus magnum ahenum quando feruit, paula confutatfUtuo
470 -
trua', Caton, Or. 95, ne quid in consulendo aduorsi eueniat, quod nostras
res confutet. Mais le verbe eat le plus sonvent pria at aena fignre
de conuincere, confundere avec lesqnels il allitere et finit par ae
confondre, et la Rhetor, k Herenn. oppoae la confutatis a la confir-
« 3 ti 5 . Ancien, class., maia aaaez rare; d^snet dana la 1 . iaperiale.
```


## [2026-09-05T20:09:10.867Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c . incoming/ARY/ARY_pages.txt; grep -n \"دوک\\|دوك\" incoming/ARY/ARY_pages.txt | head; echo \"=== ARY latin index DUK\"; grep -n -i \"DUK\\|spindle\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-05T20:09:10.954Z] TOOL RESULT

```
15706
=== ARY latin index DUK
7698:DUKTIE © {LATVIAN (3) 3.53 DAUHTAR GOTHIC) S$
```


## [2026-09-05T20:09:18.059Z] TOOL CALL #22: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T20:09:18.066Z] TOOL RESULT

```


```


## [2026-09-05T20:09:19.020Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1,20p' incoming/ARY/ARY_pages.txt; echo \"...\"; grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | head -3"
}
```


### [2026-09-05T20:09:19.085Z] TOOL RESULT

```
[pdf page 1]
6 و۵
هندواروبابی_ 1010 1۵ 1000]
۵9 (۸9ا

۲1۹۸۸۱
۱۸۸۵۱۱ ۸۵ ٩۵۱۱
۸:۱۸
۲۸۵۳۵۸۵
[pdf page 2]
نج ۰
۰ پیشگفتار ۳
پیش گفتار
هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب
۳۳۱ سس
ویژگی‌های زیر شده است:
۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها
واژه‌ی فارسی وجود دارد که ریشه‌پابی آنها تا حد پهلوی و اوستایی و حتی پارسی‌باستان پیگیری
شده است ولی ریشه‌ی هند و اروپایی آنها شناخته نیست. ممکن است برخی از آنها هند و اروپایی و
بسیاری از آنها غیر هند و اروپایی باشند. بهمین دلیل از آوردن اینگونه واژه‌ها خودداری کرده‌ام.
...
1:[pdf page 1]
10:[pdf page 2]
38:[pdf page 3]
```


## [2026-09-05T20:09:25.686Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%DA%A9",
 "prompt": "Give the full Persian entry for دوک: etymology, meaning (spindle), Middle Persian form, any Proto-Iranian/PIE reconstruction and cited sources."
}
```


## [2026-09-05T20:09:27.236Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/fusus",
 "prompt": "Give the Latin entries for fusus: both the participle of fundo and the noun fusus 'spindle'. Report the etymology given for the noun 'spindle' and any reconstruction/uncertainty statement."
}
```


### [2026-09-05T20:09:32.370Z] TOOL RESULT

```
# Latin Entries for "Fusus"

## Noun - Spindle (Etymology 1)

**fūsus** (m, second declension): means "spindle" or "spinning wheel"

**Etymology**: The source states the origin is "unclear" and notes it is "possibly from a non–Indo-European substrate."

## Participle (Etymology 2)

**fūsus** (perfect passive participle of *fundō*): carries meanings including "poured out," "founded," "moistened," "extended," "uttered," and in military contexts, "defeated" or "lost."

This participle also functions as a noun (fourth declension) meaning "a pouring" or "an outpouring."
```


### [2026-09-05T20:09:32.841Z] TOOL RESULT

```
# Persian Entry: دوک (duk)

## Etymology
The word derives from Middle Persian 𐭣𐭥𐭪 (dwk' /dōk/, "spindle").

## Primary Meaning
"Spindle" - a device used in spinning fiber into thread.

## Middle Persian Form
𐭣𐭥𐭪 (dwk') with pronunciation /dōk/

## Pronunciation Variants
- Classical Persian: /ˈduːk/
- Dari (formal): [d̪uːk]
- Iranian Persian (formal): [d̪uːkʰʲ]
- Tajik (formal): [d̪uk]

## Derived Terms
- دوکدان (dukdân)

## Descendants
The word passed into Khalaj as dûk.

## Note on Reconstructions
The provided source does not include Proto-Iranian or Proto-Indo-European reconstructions. The entry traces the term to Middle Persian but does not extend the etymology further back into deeper proto-language stages.
```


## [2026-09-05T20:09:38.724Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Tür\"; grep -n \"Tür\" HRN.txt | head -20\necho \"=== PHD dar door\"; grep -n \"^dar \\|dar \\[BBA\\]\\|door\" PHD.txt | head -20"
}
```


### [2026-09-05T20:09:38.778Z] TOOL RESULT

```
=== HRN Tür
395:Nur für einen Türken ist es aber begreiflich, wenn Südl, der
404:gelehrten Türken für falsche persische Keime handelt.
2412:*) Ich habe augenblicklich nur einen Beleg aus dem Türkischen
3328:354. perö^, arab. LW. ß:rüz 'siegreich' ; j^frö^e 'Türkis,
3444:weder Araber noch Türken sind' (vergl. phlv. Tajik
4711:522. (Tür 'Baumstamm, Holz', dann,
4873:545. (\)der 'Tür*; :^n (Is. 3, 26); vergl. derbar^), derhan,
4877:ap. duvar- Tür*, duvarayä ; aw. dvar- ; phlv. dar,
4878:dargas; ai. dvdr-^ duräs; arm. durn 'Tür (H. No. 86).
4884:Nominale von "^dvaram 'nach der Tür hin d. h.
4895:Tür hin*, konnte sowohl 'hinein' wie 'hinaus* bedeuten ').
7373:^) So bekanntlich im Türkischen immer geschrieben, aber k'ai/a
8008:gebildeten i/^Ci/O- -f vi, ursprüngl. etwa vom Türvorhang
10654:mittler*, Jätakgavlh d. i. Jatagav,nvlh Türbitte*, päz.
23052:Türkisch.
=== PHD dar door
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
1682:door dar.
```


## [2026-09-05T20:09:40.218Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT dvar\"; grep -n \"dvar\\|duuar\" BRT.txt | head -20\necho \"=== SOD dbr\"; grep -n \"δβr\\|dβr\\|dbr\" SOD.txt | head -20"
}
```


### [2026-09-05T20:09:40.294Z] TOOL RESULT

```
=== BRT dvar
2812:dvaraiii  bälyqsla  danyö^ava  V.1S.16;  — ä/  käu  as  .'.  yö  .  .i  .  .  hö  bü  'iö  äs  .  . abmairjö  anafava  yd  . .    "wer    ist   das,
3493:•  j.  apaosB-m.  Name  eines  Z>ii^'a*\  beson- ders des  Gegners  des  Tisiry a  {sd.):  a  dim (näml.  tistrim)  paiti.yas  nizdvaraiti  dalvd yö  °sö  aspake  k)hrpa  sämake  Yt.  tV.  21; 22';  —  ä  dim  bavaiti  aiwi.vanya  tistryö . .  daFnm  yim  °S>m  Yt  <.V.  28;  —  tauna- yeiti  dalum  "sjm  Yt  /Ä  2;  6.
3553:höchste,  höchstgelegene,  höchststehende':  •  j.  apayant-  AdJT  PPA.:  s.  ap-. upa  dvar»m  xsaiireMtiym{sA.) 'mstn  karj-\    j_    apayantama*    Adj,    'maxime    pro- Aaifl  "..dem  höchstgelegenen  in Ä:"yLj.  pellendus':   'maieca  a»rahe  mainysus  \\, 54.         a)  mit  alahe  und  aiät  'der  höchste  21.  i.
3636:•  j.  apäxtara-,  apIx^Ära-  Adj.  'rück- wärts, hinten  gelegen'  sva.  'nördlich'*^: Harat  haca  nafmst  'tara^byB  haca  naf- maiibya  fradvarat  aarö  mainyus  V.  ig.  i ; H.  2.25,  FrW.  70.42;  —  druxs  ya  nasus upaJvqsaid  'Xraäbyö  nalmaäbyB  V.  7.  s 8. 16;  —  °W''  apanasythe  "im  Norden sollst  du  verschwinden"  SrB.j.
4153:künftige  (jenseitige)  Leben':  disyäl  aAmai naire  oval  mlzd>m  parS.asn3i  °fguhe  vazd- fary  vahistahe  omAsusV. p. 44;  ij.8,  Y.55. a,  A.3.7.  d)  s.  zu  A  1  d.  3)  mit  a) vaAista-  Adj.,  b)  acisla-  Adj.;  a)  'das  beste Sein,  Dasein,  Leben;  Ort  des  besten  Daseins, Paiadies':  vahisfym  'hüm  asaonam  raoca- wAbb  (Stverz.)  vIspB.ci^iJ^rjm'^.g.iii  usw.; S./.a?;  —  nöithl. .  bi-at. .  vaAi/tJ  '»Aus ySmanayat  ahurahe  masdä  oval  vispanqm *aastpm  (sd.)  .  .  yat  srrfoi  daoiarihum P.  40, ;  Y,  (to.  1 1 ;  —  as^m  yS  ahurS .  .  aoi urune  uri'äsma  (sd.)  dalsayeni  vakUtimca 'hüm  P.  3S;  V. /<?.  2  9 ;  —  vazdvar»  vahisiahe 'ai^is  V.  5. 44;  —  vahistajtSs>m  (sd.) TohUtahe  'riASusV.  1S.6;  —  tarS p^r^tümcit hl  urvänmt  vahisl^m  'ham  fraparaymi  .  . it  vahistät  'tihapt  Y.  if),6;  7;  —  i'lsp^m asmanpm  vahtst^m  3  °hüm  baraiti'S.24; V.7.S2,  '^f^. 3.1"^;— vahistahe  'vASu^ vahistqm  ayanqm  yazamatde  Vr.  7. 2 ;  — yatJrS  paurrd  usshistaiti  paräiti  vahistahe •w>i7»/V.;Ä26;5.6i,Y.7/.i6,YLy.i34. P. 4:9;  —  vahislai  •r^heYyi.33;  —  ia^ä 'uhSuS  vaAistahyS  paourvJm  ku%S  (sd.) Y.  44. 3.  b)  'das  schlechteste  Sein,  Da- sein, Leben;  Ort  des  schlechtesten  Seins, HöUe':  vTspa  humaia  ..  vaAistpm*°tAlim"'' *asaiti  vispa  dusmala  acisl^m  *'ijhüm"^ *asaüt  FrW.  3. 2 ;  — ya^ääl  anhat  apsniim (sd.)  '»Aus  aaslS  ärygt'atqm  at  asäum vakistim  manö  Y.30. 4 ;  —  avi  lim  spayüt. . t)mS  .  .  äca  aastpm  äla  'hüm  ä  V.J. 35;
4412:•  j.  'an-äx§ta-  Adj.  'uDÜriedlich',  Plui-  n. 'friedlose  Zustände':  'ta  apa.dvarata  Yt. 3-S:  ...
6099:—  mazda  dadät  aAurö  Aaurvatö  amfntä' tasca  .  .  'sahyacä  xsairaAya  sarö  (sd.) vanhSus  vazdvari  mananAS  Y.  31.  21  \  — tä  vi  masdä  .  .  aAurä  'säi  yecä  taifyacä armaill  .  .  i/lffiS'  (sd.)  xsa'^rvm  .  ,  voAä manaaAa  Y.57,  2;  —  tat  vi  ni  Aasaosä^
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
6542:'  Sat  fradvarat  °iis  >riza/ii  äuldaaid  VL
6962:i)  die  Richtung  auf  den  Sprechenden  zu angebend  'her,  heran,  herzu',  nur  in  äca paraca  'her  und  fort'  sva.  'hin  und  her, hin  und  zurück'*':  'hrixsaparim  hahräkgm (sd.)  *xh'ai  xsa/nd  aca  paraia  N.4;  — pairika  ,  .  3ca  paraca  dvaraiH  YtÄ  54; —  v?r>^raynpm  ..  yö ..  äca  paraca  p}r?- saite  Yt.14.4-j.  ")  anschliessend  'dazu, dazu  auch,  und  auch':  a?s^  zi  vnxs  . . */ramrva»ö  a  vacO  afiunS  vairyö  fraoxtd .  .  spanvanti  H. /.4;  —  hä  hama  pairi- säiU  frapaya  (sd.)  daühus  ä  upaosatfh- väsca  Yt ig.\\  —  yS  H  axtÜ  akmäi  yJm axtsysi  (sd.)  dstihg  ^.36.  i ;  —  'kwSi  as *ärmaitis  ^w!  ä  gStt^  tasä  (sd.)  as  Y.31. 9.  a)  wiederholt  'et  ,  .  et',  nach- gestellt: akunm  mazdqm  amruyi  (sd.) nmänake  nmänS.patsis  ratüm  ä  viss  Tlspa- tsis  ratüm  ä'  .  .  daiähupatOts  ratüm  3 Y.  lg.  I.  a)  in  Verbindung  mit  (vor-
7147:aat  ,  ,  /radvarai  aii7  dahäkö  , .  daernnS: .  .fra  '^wijm  paiti  a/iifia  (sd.)  nait  apaya uzmoeayäi  .  .  'i^rilibrai  asahe  gaSiianqm Yt.  ig.  48;  49f.  A  a)  airö  (näinl.  ayar?) heisst  der  9.  Monatstag:  -'^rB  akurafu mazda  pii^ra  (statt  Gen.)  S. /.g;  vgl.  2.9, J6.4,  Anhang  zu  1.  Das  Feuer  (J5?a^J  °>
7222:\-,  g-",  P-'*.  ä,  j.  »flä),  j.,  g.  a"4>  I)  Adv. )  die  Richtung  auf  den  Sprechenden  zu ngebend  'her,  heran,  herzu',  nur  in  tua paraca  'her  und  fort'  sva.  'hin  und  her, hin  und  zurück''':  %rixsapar3m  hairähm (sd.)  *xsfas  xsafnö  äca  paraiä  N.4;  — pairika  .  .  Sca  paraca  dvaraiti  Yt.  Ä54;
7254:frabanm  .  .  ä'  yimai  xia'irai  "iirisats, zima  *Amjas?nta  il'  he  tm  za  bvat  psnne .  .  ä°  yim3i  paüi.vaäiaim  . .  ä'  yimS  fra- sBsaJ  .  .  ä°  yimS  tmam  zam  vlsSvaya^  V. 2.2— 11;  —  äat{s.2)  aoxla  ahurö  mazdä yimäi  .  .  avi  ahSm  .  .  *z3m5  Janhtntu  .  . 3°'  t>m  var?m  kgnnava  . .  ä°  mqsta  yimS . .  3°  aoxta  aAurS  mazdä  . ,  S°  yimS  ava'^a kinnaot . .  ä°  yimö  var)m  k^rmaot .  .ä° . . V.2.22-33;  —  3at  (s.  8)  .  .  mjrr/ff  y5 paröJari  .  .  airö  väbm  surunaoitt  3°  .  . fradvaraiti  büsyqsta  FrW./o.4if.;  —  tat y^arjnd  apatacat  .  .  ä°   us.patal  franrase
8686:•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya aiwi.surunvait(  N.  i'ö";  Uj;  —  *'sibya F.p'>*>;  —  drimts  .  .  asi  [-//Is)  karma gava  *dvari'^ra  zafan  Yt  jr.2;  —  pairi 'si  vSrayavw»m  kam  gava  nidanzaydmoMii Yt.  j.  27;  —  g?tirvaya  h?  päoave  züvar^ pairi  iS  'si  zvrpnäioi  sk)Hd?m  si  manS kirsnüioi  Y.9.28;  —  °//  ahuralu  mazda yazamaide  darp'^räi  (sd.)  maiirahe  .  . xratüm  .  .  mar>%räi  .  .  hisvqm  . .  fra^'äküi Yt. /.  28.  a)  von  Tieren;  °H  (näml. g>us)  pairi. dar ayänli  (sd.)  daSma  .  .  Vt. 14. 56.  b)  'Gehör*,  d.  i.  Fähigkeit  richtig zu  hören  und  zu  verstehen,  sva.  'Auf- fassungs-,  Verstandeskraft':  ava  pa'oS  ava zastS  ava  °/i  däraydiiwjm  .  .  däityanqm .  . syaoiinanqm  varpzäi  Vr.  75.  1;  —  d<lya ml . .  mastim  spilnö  xsviwrjm  (sd.)  hizi'qm uruiie  -si  xratBiH  .  .  Y.62.4.
9048:•  j.  kaoba-  m,  Name  eines  Lands*':  upa dvarnn  xsairö.sukjm  (sd.)  apanöJtmjm 'hitva  *birizantaya  asavanaya  "bei  dem Pass  -Vj^,  dem  liöchstgelegenen  in  dem hochragenden  heiligen  K."  Yt5.  54.
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
10770:•  j.  x§a9-rö.suka-  m.  Name  eines  Gebirgs- passes in  Kaaha :  upa  dvarjm  °k>m  apanS.- t^msm  iatfhaya  (sd,)  Yt5.  54,
11954:/0.8;  —  amäica  %wä  Vfn'hrarfnaica mävdya  upa.mruye  'nuygY.g.2T,Yti4-3S, 16.1J,  19;  —  yS  vö  aps  .  .  yazäite  . . ahmsi  'nvS  drvatätim  ,  .  'nvS  vazdvar? ..  'nvS  Vfrs^nm  ..Y.  68.11;  Yt.io.io8;
11955:—  "nvS  vlspayä  drvatätim  °nvS  vTspayä vazdvar)  Yt/4.39;  —  imfm  'hwqm  ..yänim haema  Jailyemi  drvatätim  atiiAas)  'nvS.. darrjB.jltlm  ustänahe  Y.p.19;  K.i.Z;  — 'nuyäsca  paiti  druaiats  Yt.  13. 134;  —  aha r0  tarn  sraos'a  . .  zävar»  daya  AitaHbyB drvatätitn  °nubyu  ".  ,  Kraft  unsem  Ge- spannen, Gesundheit  unsern  Leibern"  Y. j7,  i6;  —  däl»m  te  'nuye  ^annd  'Yt.iy. 12;  15;  — ya>a  tW . .  ifä'^ravaiils  'nvö +,iwi/J  (Sp.  274  IL)  Y.  60.  11;  —  vohü uxsyä  (sd.)  manan&ä  .  .  ui'tä  'nUm  Y. ^.10;  —  haomü.artharstahe  (sd.)  hizvS mq%rS.hitahe  (sd.)  °nvd  A.4-5i  —  im Gegensatz  zu  gaihä-  (Sp.  477  in.),  urvan- usw,:  akmäi  nfmaahl  ävaldayamaidi  gal- %^slä  'nvascä  nipätayaicä  , .  Y.  56".  2  j  —  yö nS  . .  iririx/äite  gaghanqm  .  .  °nunqm  Y. 65, 7 ;  —  frähatiia  asake  gaghä  .  ,  asahe °nuy!  Yt,  6.1;  —  forasayäi  (sd.)  aibi %waha  gai'iäAa  -nuHcä  Y.  43.  T,  — 'nvagca  * kaosravar3h»m  untnaija  dan^tm havanium  F.^h;  —  cim  ,  .  qst>m  isaiti 'rwa  cim  uruna  Aog,  4^;  —  vJspS  gai- %isca  -nvasia  azdsbisca  .  .  iistänqs^a urvätamca  . .  pairica   dad>mahl  Y.  55.
12057:•  g.  tarS-tnatay-,  j.  tarö.niatay-  f.  Svider- strebendes  Denken,  Widersetzlichkeit,  Auf- lehnung, Trotz',  spez.  in  Glaubenssacben: yö  gähä  asrävayd  ^qsta  (sd.)  vä  'inaiW^ vi  tanüm  *piryHH  N.  41;  —  kö  *tfj«(sd.) *ij  *'Maitis'?''>  yä  haca  damayäi  mifzda- yasnsif  a^sisiii/ (sd.)  "was  ist  Hass,  was Troti?  .  ."  Ii.41;  —  yl  %aia/  maidä asn^tlm  ak>mca  manB yazili  (sd.)  qfiä  ^aS- iSuscä  •maitlm  Y,  j_j.  4.  a)  ' satz  zu  armatay-:  vaittlt  ahmt  nmäiie armaitis  'maitim  V.  60.  5.  A)  als  Dä- mon*': 'mata  apa.dvarata  pairi.mata  aßa.- iharata  Yt_j.  8;  11,   15*,
=== SOD dbr
30701:3498  dbr   C  =»  5Pr-2 
30713:5Par   (dbr)  ©<Av.  duvara  ©nom.  -y;  ace.  ->v; 
53460:6793  pdbry  C  <oL  jL^. 
82240:10938  ydbry*   C  =  y-  +dbry>  =»  8j3r-2
```


## [2026-09-05T20:09:49.881Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30705,30725p' SOD.txt\necho \"=== SOD pages 138\"; grep -n \"\\[pdf page 13[0-9]\\]\" SOD_pages.txt | head"
}
```


### [2026-09-05T20:09:49.940Z] TOOL RESULT

```
hpr-   ©impf.  6>0n  inf.  -(})y  =»5[3rt->  6br-, 

5P'r- 
0o)give,  (ro)offer,  0o)put 
GMS  492,  592;  TSP  3.68,  71,  73 

3500  8pr-2  B,  M,  S  *j'j>><-P 
5Par   (dbr)  ©<Av.  duvara  ©nom.  -y;  ace.  ->v; 

abl.  ->(hk  loc.  -y';  pi.  -t\  ob.  pi.  -*y} 
door,  gate 
BBB  469,  676,  648,  669;  VJ;  TSP  3.228,  16.30, 

17.40;  SCE  109,  504;  BSTBL,  Vim.  185,  189, 

200;  Padm.  3;  Hen.  Cosm.  312.86,  88,  94,  95; 

KG  pl83;  MSP  bl31;  GMS  515,  936;  STi  39.5; 

STii  3.60,  71;  C2  gloss.;  Frag.  Len.  93.37,  100c 
=== SOD pages 138
```


## [2026-09-05T20:09:50.471Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4873,4900p' HRN.txt"
}
```


### [2026-09-05T20:09:50.516Z] TOOL RESULT

```
545. (\)der 'Tür*; :^n (Is. 3, 26); vergl. derbar^), derhan,
derwäze.
g. bar; Semn. bart; Käs. bar, ber; Vullers ber
wird auch dialektisch sein-).
ap. duvar- Tür*, duvarayä ; aw. dvar- ; phlv. dar,
dargas; ai. dvdr-^ duräs; arm. durn 'Tür (H. No. 86).
kurd. bar {der^ deri); af/. var; oss. dvar (114);
wa/. bär^ sar. divir, §iyn. dive, divSr, minj. labra,
546. {2)der Praeposition a) 'hinaus, draussen.
kurd. bar 'draussen ; bei. LW.(?) dar, dara 'draussen,
ausserhalb, hinaus' (72); lat. foras, foris.
Nominale von "^dvaram 'nach der Tür hin d. h.
'hinaus gebildete Praeposition. Vergl. berün (No. 252).
b) 'hinein, darin', derün.
phlv. dar, vereinzelt AV. (sonst immer pD).
An die allgemein angenommene Verkürzung aus
ender (No. 119) mag ich nicht gern glauben, ebenso
wie np. tä auch nicht aus päz. andak (s. No. 366)
Phlv. darhär? Vergl. Nöldeke, Kärnämak, 57 Note U
?) Arni. L^\ bar (Hübschmanp ZDMG. 35, 128),— 121 —
entstanden sein kann. Sollte nicht ebenfalls *(lvarain
die Urform zu der 'hinein, darin' sein? *(lraram *zur
Tür hin*, konnte sowohl 'hinein' wie 'hinaus* bedeuten ').
In Verbindung mit Verben, wie ämeden, bayistefi,
l/afte?i etc.
547. diräz 'lang, diräza; vergl. direng.
aw. drajah' 'Länge'; phlv. draj (vd. 5 (159) Gl.),
drajth^) (so ist wohl dränäT, wie immer geschrieben
```


## [2026-09-05T20:09:56.833Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la SOD_pages.txt; grep -n \"3500\" SOD_pages.txt | head -5; echo \"===\"; grep -n \"pdf page\" SOD_pages.txt | head -3"
}
```


### [2026-09-05T20:09:56.900Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3741182 Sep  4 14:06 SOD_pages.txt
13734:                                                               3500 8pr-2   - M, S
38069:disorder    8031                       door 3500                               duck    4824
38363:gate    3500                           glories    3916                         gold     11544, 11566
===
```


## [2026-09-05T20:09:59.652Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=13734' SOD_pages.txt | grep -c $'\\f'; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==158' SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:10:01.336Z] TOOL RESULT

```
202
---
 'zynt


                                                                   2324 >zn,ny C                                             92
                                                                                                                      ♦xJfol^l
       pl32 S =» 'zy'nt
 2311 >zynt                                                             azanne ©pi. -t ^z'nny
                                                                        confessor
 2312 vzyr S                            £^ «>j <f jj t/W                 BSTii 883.19; C2 gloss, n p86
      az/zy/zar ? ©ace. -w, ob. - >; pi. -f
      armour                                                       2325 Wptnym           B                            j>Jj<jj^
         MDii pi 52.5; MDiii                                             (o)zna-patnem
                                                                           =»jn}ptnym         Ozn'ptnym, 'nz'ptfym)

 2313 >zyrt S                                                (^          adviser
      (o)zyart (zyrt) =»jyrt
      quickly                                                            TSP 2.1155, 12.70; Gersh. Advice. 78bf; Hen.
      Hen. Tales. 475.11                                                   Tales. 480.13, 48ln 6

 2314 'zYw(h) B,S                          ^^'J^'J1^               2326 'zn^tnym         M(S) =* Wptnym
```


## [2026-09-05T20:10:05.638Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==203' SOD_pages.txt | head -30"
}
```


### [2026-09-05T20:10:07.482Z] TOOL RESULT

```
                                                                 i-■:&*. ;^-*i,W«i J J Vw^^tii>»irtt^i^vii^^:iA^4it^                     .A.-«i-:s&ift-.M*-*»-;:




 137
                                                                                                                                                         <0b i^ip i,


        BSTBL, Dhy. 89, 346; O2 32; Gersh. Minorsky                          3468 8p*nk S
          Mem. vol. 1971, 290 n47a; TSP 13.23; Benv.
                                                                                         (a)5Pane ^'SP'nk
          Sfi'z, n p228; S W, IIJ 1976, 55.23                                                                                                        4*sy
                                                                                         grain, seed
                                                                                         MDii pl99;MDiii  pll9
                                                                                                                                                                   i^
 3457 5p»r-     B -» 5p>r                                                                                                                                               6p't
 3458 8pwr Spr'yn'y B                           .ju^*^ «jui**                3469 5p}npn B, S => SP'mpnCw), Sp'mb'n
      8par- 8Parene «*8p,r                                                   3470 db'n(y) B
      giver of gifts                                                                                                                                               *j>j^
                                                                                         9/5Pan(e)
                                                                                         extension =»*8p>y-
      SCE 496; -Sprrik, SCE 46
                                                                                         STi 75.18; Sund. AoFiii 1975, 56
 3459 6p>Yst- B                      ( j&jji rJLJ-^j^-jJul
      Spaxst, Gfaxst (6Pj-) ©*0wax.?-; /"/wa^ ®pt.                          3471 5p>nz B, S
        st, =»9fyz-, 8p'yz-, 8pxsty(y), SPystc                                   SPanz ©<*debazah; Av. bazah
      GcOcollect, 0o)gain                                                        wide, coarse                     SPnstr
      GMS 293; Hen. LW 105; VJ 241, 243 pp., n p92;                              TSP 2.1018; Hen. Texts. 738; GMS 1310; MSP
        AVS 130                                                                              bl89; Frag. Len. 97a3
```


## [2026-09-05T20:10:13.475Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==203' SOD_pages.txt | grep -n \"^ *3[45][0-9][0-9] \" | tail -8; echo \"=== page 204 (printed 138) first entries\"; awk 'BEGIN{RS=\"\\f\"} NR==204' SOD_pages.txt | grep -n \"^ *3[45][0-9][0-9] \" | head -8; awk 'BEGIN{RS=\"\\f\"} NR==204' SOD_pages.txt | sed -n '1,8p'"
}
```


### [2026-09-05T20:10:15.481Z] TOOL RESULT

```
39:3462 fip'mb'n M                           j^a ^ '^                          3474 8p»r B, M, S                            c^^-u
46:3463 6p>mbn =» 5P,mb,n                                                     3475 6pV-gift B                                  (Jjzs ^r,f,,,, j->) q»lj<u-U *Jjb
48:3464 db>mn C, S                                                                         8Par, Gfar ©OP fra-bam Khwar. hfir-,
57:                                                                           3476 8pVt-                   B, M                                     &/+J* O^
59:3465 6p>mpn(w)      S, B                                                               8part, 9fart (8pwrt) ©pt. st. & pp. =»8p>r-,
70:3466 8p)n B
76:                                                                          3478 $p>t                                          ^li
80:3467 db>n C -> 8p>n                                                            VJ 3b, 1054; TSP 3.259; Frag. 2a.l6; MDii A17, 5;
=== page 204 (printed 138) first entries
6:3479 db>t C => 5pH
8:3480 *5p>y- B                                         o^^J
16:                                                               3493 8pnh *± 5pn->h
17:3481 Sp'ys B                                      jljT.^o      3494 8pnnh B =* 5Pn->h
23:3482 8p>ys-        M                         ^jocu. <jjbjljT
28:3483 5p»yz- B, S                        (j^i :Jj~>)j^^\
35:3484 8p>z     B =» 5p»n(h), 5p>n                                        hpr-   ©impf. 6>0n inf. -(})y =»5[3rt-> 6br-,
37:3485 SpSV B                           ((^j)^^jj^^                     0o)give, (ro)offer, 0o)put
db't
          Hen. Talcs. 472.37; STii 1.52, 6.11; Sund.           3492 8pn->h      B, M                         ^j.^JiJ^
          AoFviii 1981, 214, 21V16, 22V5; C2 gloss.;                  8Pana, Spana (SPnnh, dbn-\ §pnh) ©*</wa-n<2;
        db*tyt VJ 336                                                   Lat. du-bius ©f. n., nom. -'(Ti); ob. -y} =»pw
                                                                        dbn, >pw §pn
3479 db>t C => 5pH
                                                                      doubt, suspicion, fear
3480 *5p>y- B                                         o^^J
```


## [2026-09-05T20:10:23.309Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==204' SOD_pages.txt | grep -n \"3500\\|138\\|duvara\" | head; echo \"=== 205\"; awk 'BEGIN{RS=\"\\f\"} NR==205' SOD_pages.txt | grep -n \"^ *13[0-9] *$\\|3500\\|duvara\" | head"
}
```


### [2026-09-05T20:10:24.966Z] TOOL RESULT

```
40:                                                               3500 8pr-2   - M, S
43:                                                                    5Par (dbr) ©<Av. duvara ©nom. -y; ace. ->v;
=== 205
1:139
```


## [2026-09-05T20:10:31.732Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','FVF','SOD','IEC','KNT']:\n    print('###',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\" | head -80"
}
```


### [2026-09-05T20:10:33.859Z] TOOL RESULT

```
### BQT
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
### MON
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
### FVF
```


## [2026-09-05T20:10:38.891Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 287 288 289; do echo \"===== leaf $L (printed ~$((L+540)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -60; done"
}
```


### [2026-09-05T20:10:40.481Z] TOOL RESULT

```
===== leaf 287 (printed ~827)
  ‫دخمه فروژه‬                                                                                         ‫‪۲۲۴‬‬


‫کتدااوروآغمازعامله بکیا‌باشد و‪-‬تبره وتازيك‬
                                         ‫اب‬                 ‫باشد ‪-‬وبمعنیاندوختن‌وجمم کردن‌هم‌هست ‪۴‬‬
                                        ‫را نیز گفته‌اند ‪۰‬‬                        ‫ودوشیدن‌را نکیوزبند ‪. ۱‬‬
‫دحم ‪ ۹‬بروزن زخم ‪ ۰‬سردابه‌ای که‬                              ‫دخقنكد ‪ ۴‬ه بروزن سوزنگر» دختر‬
                               ‫لهمل‪.‬‬         ‫مرده را دران‬   ‫ودختر زان آزشوهر‬      ‫شوهر باشد از زنی دیگر‬
                                                                                                       ‫وگ‬
 ‫د حمه = بروزن زخمه» بمعنی‌دخم‌است‬
‫که صردابة مر د گان‌باشد؛وصندوق‌موتی را گویند‬
                                                            ‫دخقه ‪ ۴‬ه بروزن کفته‪ .‬مخف دوخته‬

 ‫عموماً وکورخالاً کبرانرا خصوصاً ‪ -۷‬وآن‌چیز‬                 ‫است که خیاطت کرده‌شده باشد‪ -‬وبه‌عنی دوشنده‬
                                                                                                 ‫هما مده ار‬


            ‫میا ورد و آیرا بعر بی شعععه خوانند ‪۰‬‬            ‫دخدار » بفتح اول و دال بی‌نقطه بر‬
 ‫دخمه راندیان س کنابه آاسزمان‬                               ‫وزن دستار» چادرسیاه وسفیدبرا گویند که برروی‬
                        ‫‪۰‬‬      ‫‪.‬و‬   ‫ه‬    ‫‪۵‬‬     ‫‪۰‬‬



                                                     ‫ا‬
                                                            ‫تخت پوشند ؛ وبعضی گویند معرب تخت داراست‬
                                                                                ‫که جام خواب باشد ‪.‬‬
                            ‫ات که آسمان باشد ‪.‬‬              ‫‪ = °‬بقتح اول بروزن رخش ‪۰‬‬             ‫دحش‬




  ‫از‪ :‬وخت ‪+‬‬       ‫‪۴‬‬            ‫» دوختن‪.‬‬            ‫و‪:‬ختن‬
                                                       ‫دکه‬
                                                         ‫ال ر‬
                                                            ‫‪۴‬‬             ‫‪.‬‬    ‫دوخئن‬   ‫رکه‬   ‫=‬   ‫‪۱‬‬

                                                            ‫اندر ) فظدر يسرأندرء پدراندر و مادراندر ) ‪:‬‬


       ‫ن بدارا ‪.‬‬
               ‫تچو‬
                 ‫خهم‬
                   ‫درد‬
                     ‫با پسندر کینه دا‬                         ‫جز بمادندر نماند این جهان گړبه روی‬
  ‫رود کی‌سمرقندی( تصحیحعلامهدهشدا) ‪.‬‬
  ‫© ‪ -‬رکه‪ :‬اسشق وهوبشمان ‪.4۲۵‬بهلوی‬         ‫‪ - ۴‬اسم مفعول از «دختن» (هم‪. ).‬‬
 ‫‪( 11520‬شفل‪,‬تکلیف) قی‪:‬ارستا هتکن (آلت‪,‬ایزار) «بارتولمه‪»٩۷۷‬‏ وممکن است از‬
             ‫‪( 01:2‬شان ‪ ,‬علامت) «بارتولمه ‪۹۷٩‬‏ مشتق باشد « نریبکه ‪٩4۰‬‏ ‪.‬‬ ‫اوستا ‪2‬شا‬
  ‫‪۰07۳1۵0‬‬                   ‫‪ - ۷‬اوستا‪amxad -‬‏ ؛ پهلوی‬                     ‫‪ - ۱‬رکه‪ :‬دخمه ‪.‬‬
  ‫م دخمة اوستابی بمعنی دافگاه است سنی محل یکه مردگان را‌وزانند» چهرة‬                              ‫«اسشق ‪۳‬‬
  ‫این‌کلمه که ‪ 821‬باشد بمعنی سوزانبدن است وکلمة داغ فارسی از همین ماده است ‪ .‬ازخوداوستا‬
  ‫هم مفهوم میشود که در قدم ابراننان لاشة مرد گان را می‌سوزآنیده| ندودر رندیداد از جرم‌سوختن‬
                  ‫اص ‪ ۵۰۵‬راجم بدخمة پارسیان'ر که‪:‬‬                 ‫لاشه در آش سخن رانده شده ‪ .‬بشت‬

            ‫‪J.M. Unvala, Report on the Dakhmas‬‬                                  ‫‏‪of Tena, Bombay‬‬
  ‫‪1951; ibid, Preliminary Report‬‬                            ‫‪on an Old Dakhma of Yazd,‬‬
 ‫‪Reprinted.‬‬         ‫‪Sanj Vartaman‬‬                    ‫‪Pateti Annual‬‬       ‫‪1951.‬‬

===== leaf 288 (printed ~828)
                                                       ‫يان بنحم‬

                    ‫بر دو لفت‬              ‫در دال بی‌نقطه بادال بی‌نقطه عفر‬



‫رانز گوند‪.‬‬      ‫وفلندر‬    ‫‪_۴‬‬       ‫جانوران‌درنده‌باشد‬   ‫که‬       ‫که جانور ان در نده باشدهمجو شبر و پلنگه‬         ‫گونند‬



‫وگ رکه ومانندآن ‪ - ۱‬ویبابان پرازشکار را نیز | ودرتر ککنیيزك را نیز کوبند که فرزندان کلان‬




   ‫در دال بی‌نقطه با رای بی‌نقطه مشتمل بریکصد ونود وپنج لفت و کنایت‬


 ‫مشمه ل بر صف‬      ‫هصست‬   ‫رردشت‬       ‫کتابی دراحکام ددن‬           ‫ثالی ‪ ۰‬در خانه‬   ‫»‪ -‬بفتح اول کون‬       ‫در‬



  ‫وسرای وامثال آن باشد وبعربی باب کویند ‪ ۴‬۔ | باب وآنرا «صد در نام‌نپاد‌اند ‪ -‬ونوع و جنس‬
 ‫ودره کوهرایز گفته‌الد‪ - 6‬وبمعتی کرت ومرتبه | را نیز گویند ‪ - ۷‬و بمعنی دربدن و پاره پاره‬
 ‫امر بر باره کردن هم‬           ‫و‬       ‫باشف‬    ‫کردن هم‬            ‫چنانکه‬    ‫‪ -‬وبایی که در کتابهامنوی ند‬          ‫همهت‬



    ‫‪ - ۱‬اوستا ‪( 2610124 -‬جانور وحشی)‪.‬پهلوی ‪.tad 64024 610۵1۰‬‏ «اسشقع‪4‬ه»‬
   ‫و گفت ‪ :‬مرا تشجیران و ددان بحکم اعتمادی‬                      ‫«رویاه بر حمدو له لام گفت ‪e‬‏‬        ‫«مناس ‪YT‬‏‬

   ‫ی‬    ‫‪5:۳‬‬   ‫ور‬    ‫ر کث‪ :‬دده‬        ‫رک‬            ‫‪۰‬‬    ‫‪۷:۰‬‬   ‫سند بادناه‬   ‫نزدىك تر فرستاده‌اند‪».‬‬   ‫وسفارت‬       ‫برمات‬



        ‫بی‬
         ‫اكك‬
           ‫نیز‬
             ‫غ کن‬
                ‫جشی‪.‬‬
                   ‫مرعکنیی‌جد پدری‌با مادری»خال (دائی) پبر» حبران وح‬
                                                                   ‫‪ - ۴‬دبرت‬
    ‫‪ - ۴‬پارسی باستان_ ‪( ۲3۷10‬در ‪.‬باب)‪ .‬اوستا‪ ۰ ۲2۷1 -‬پهلوی‬                                  ‫ور که ‪ :‬دادا ‪.‬‬         ‫‪۸‬‬
       ‫‪ ۳‬هندی باتان ‪ , 94۳1۷ ۰ ۲2۷‬ارمنی ‪( ۳۳1۱‬باب‪ .‬در) ‏ کردی ‪)red. ۲۵‬‏ „(‪îrad‬‬
       ‫افغانی ‪ ۰ ۲۵۷‬استی ‪. ۲2۷0‬وخی ‪۲20۰‬سر بکلی]‪ . 1۷11‬شفنی ‪ , ۲6۷۱. ۵۷14‬منجی ‪27021‬‬
   ‫سمنالی ولاسکردی ‪rab‬‏ «‬                  ‫‪ 3‬بارتولمه‪ ۷۰۲23۷0۰ ۹۹‬لیر گے بر‪ 3 » 6‬منای ‪۱‬‬                ‫»‪ 2‬اسشق ‪6 0‬‬
       ‫فنردییز‌ونطنزی ‪ ۳30‬برنی ‪٣‬ق‏‪0‬‬                     ‫‪.۲‬‬‫‪“3‬‏‬
                                                            ‫یص‪٩۹۸۱‬‬
                                                                 ‫ککے‪).‬‬
                                                                     ‫ل‪1‬ء‬
                                                                       ‫ک‌بی ‪3‬‬
                                                                            ‫شهمیرزادی ‪ . 81‬سرخه‬
                                                                                             ‫دک ‪۱ .‬ص‪٩ ۲٩۰۹‬‏ ‪:‬‬

                    ‫بی وسیلت گرد پیرامن ‪.‬‬                                  ‫درمیر و وزبر و سلطان را‬
       ‫هکلتان ‪. ۹۳۰‬‬
       ‫یز ‪ ۲۵34‬دربهلوی بهمتی باب و فصل کتاب آمده‌منای‬                      ‫‪٦‬‏‬          ‫رکه‪ :‬دره ‪۰‬‬     ‫‪- ۵‬‬

                     ‫‪ - ۷‬ه پنشتم و از هردری سخن در پیوستم ‪« ».‬کلتان*‪. 4‬‬                                      ‫‪.‬‬      ‫‪۱‬‬

===== leaf 289 (printed ~829)
  ‫دراز دستی کردن‬
 ‫هابلای مشدد ودال ابجد‬
                     ‫دارذودا ت‬                         ‫هت بعنی بدروفاعل‌دریدتراهم میگوبند وقتی‬
‫بوار رسیده و زای هوز بکالشفیده ‪ ,‬کی را‬                 ‫که مر کب شود همجو پرده در ‪٩‬‏ ‪ -‬و لوعی از‬
‫تجربه و دانا و عاقل باشد‪ .‬که‬       ‫حهب‬
                                     ‫اک‬‫صبند‬
                                          ‫گو‬           ‫مرغ صحراییرا کوبند و آترا سحرور خوانند‬
‫اکر احیااً کاری ناصواب ازو سرزند اصلاح آن‬              ‫باسین وحا ورای بی‌نقطه بروزن فغفور ‪ -‬ویشهرا‬
‫را بدانتگ ی تواند کرد ‪ -‬وکسی را یز گوبند‬               ‫نگیوزیند که صربی بق خوانند ‪ -‬وسمعنی درون‬
 ‫کنه‌یجکنکیه‌ووصلبحدویراباهم کند تورآایعربی‬            ‫باشد که نقبض ببرون استت چنانکه گوبند ‪«۶‬در‬
                         ‫مزبل خوانند ‪.‬‬                 ‫>عنی بدرون خاله رفت ‪ - ۴‬و نام‬
                                                                                   ‫خانه رفت ی‬
                                                       ‫موه وئمردرختی است کهآ نراتوت سه کل کویند‬

 ‫وقلتبانرا گویند ‪ -‬ودرعربی دو کی باشد که بدان‬      ‫وبعربی ثمرةالملیق خوانند وربکه و ثمرآنرا با‬
                                    ‫بشم رندد ‪٩‬‏‬        ‫بهجموشاننه وبدان ریش رنگ کنند ‪ -‬وضم اول‬
                                                                          ‫درعربی بمعنی کوهرباشدگ ‪.‬‬
  ‫در ار ‪ = ۲‬پروزن نماز ‪ .‬ضقکيوتاه‬                      ‫وزن سراء نمعنی درای است‬        ‫کی‬        ‫‪5‬‬
                                          ‫باشد ‪.‬‬
                                                        ‫که زنگ وجری باشد؟ ‪ -‬و امر بداخل شدن‬
 ‫بر وزن سوادخان ‪.‬‬           ‫وران»‬
                                ‫خرا‬
                                  ‫د‬                                                        ‫هم هت‪٥‬‏ ن‬
                 ‫باینشداز ودستار خوانرا گونند‪۶ .‬‬
                                                       ‫فرو شدن = کنایه از ناود‬         ‫دراب‬
 ‫درار دستی کر دن «کنابه‌ازغارت‬                                            ‫شدن وهعدوم گردیدن باشد ‪۰‬‬



   ‫‪ - ۴‬حرف‌اضافه» کردی ‪ ( ۲29‬در ببرون ) ‪.‬بلوچیع())‬                   ‫‪.‬‬   ‫رکه‪ :‬دربدن‬    ‫‪-‬‬    ‫‪۱‬‬

  ‫‪ ( 5۲21‬درببرون » بهبیرون)» لانننی‪.]51۲0* ]5210‬پهلوی ‪«۰.۲20‬اسشق ‪. ۹4۵‬قس‪ :‬اندره‬                     ‫‪۴‬‬
   ‫‪« - ۴‬دره (جضم اول وتشدید دوم) بمعنی مروارید‬
       ‫وزن‌صرد و درات‌بطماست ‪« ».‬شرح فاموس» و دفرارستخضة‬
                                                                 ‫وجمع‌ان در بضم ودرربر‬          ‫ت‬
                                                                                                ‫گزر‬
                                                                                                  ‫ب‬
   ‫‪ = ۴‬درای(ه‪.‬م‪).‬مژ لف اخبارالصن والهنددر وصف‬                   ‫دوم هم 'مده ومفرد گرفته دده است‪.‬‬

    ‫مملکت صين (چين)آرد‪* :‬وفى کل مدينة شثی بدعی الدرا وهوجری على رأى ملك تلكالمدينة‪.‬‬
   ‫مربوط بخیط ماد على ظهر الطریق للمامة کافة و بن الملك و ينه حور من فرمخ فاا حرك‬
   ‫الخیط الممدود ادلی حرکة تحرک الجرس ‪ .‬فمن کات له طلامة حرکک حذاالخ‌ط فبتحر که‬
   ‫الحری مه علی‌راس الملك فوژدن له بالدخول حتی هى حاله بنفه ویشر حطلامته و جمی‌للبلاد‬
                            ‫فیها ذلك‪« ».‬اخبارالسن والهند ص ‪( ۹۱6 - ۸۱‬از افادات علامه دهشدا) ‪.‬‬
       ‫معنی‌دو کث»است‬     ‫‪( -‬عر) «درارة بروزن جبانه‪.‬‬     ‫‪۱‬‬       ‫‪ -‬امر از «درآمدن؟ ‪.‬‬        ‫‪۵‬‬
     ‫‪ - ۷‬اوستا ‪( 012[800-‬طول) ‪.‬پپلوی [ک‪4‬ر‪۳‬د‪.9‬ی‪.121711‬بلوچی‬                            ‫«شرح قاموی» ‪.‬‬
    ‫‪۷۱۱٩۰‬‏‬     ‫‏‪ d۲8‬و ‪028۲0‬اسشق ‪ ۷4۵‬یز دریر‌لوی ‪«28۳10‬منای‪.»۱۷۲:۲‬استی ‪ «018۲20‬کث‪.‬است‬
     ‫کد‪ .‬اص ‪۲٩۰‬‏ »سمنالی‪2 .‬سنگسری»سرخه‌یی‬                      ‫فرىز لدی‪,‬و لطازی ‪zdread.‬‏ عرلی ‪27‬‬
                      ‫‪.‬یلکی ‪: 28۲81‬‬
                                  ‫وشهمیرزادی‪ .22۳64‬لاسگردی ‪« 28۳621‬که‪ ۲ .‬م‪ ۳۹۱۰‬ک‬
             ‫بدستهای د گر همچنین بخواهدرفت ‪.‬‬                  ‫چه سالهای فراوان و عمرهای دراز‬
      ‫‪‎‬ناتلک« ‪. 14٩‬‬
    ‫* درابر یی ‪ -‬از بونابی ‪( 00126۳2۲1‬نرده» شدکه)معرب‌آن درابزین ودربوز «دزی‬
    ‫‪#‬معحمدات عر مبه‌سامیه ص‪ » ۲ ۷۲‬و درابر ون «المتجد» رکف ‪ :‬داریز دنه دارآ فرین(‪)۱‬‬          ‫‪ ۱‬ص‪۶۳‬‬

     ‫بغيةٌ درصفحه ‪۳۸ ۰‬‬                                                                 ‫ودارفر بن (‪. )۱‬‬
```


## [2026-09-05T20:11:16.279Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<5568 && /^ *19[0-9] *$|^ *18[5-9] *$/{print NR\": \"$0}' KNT.txt | tail -8; echo \"--- after\"; awk 'NR>5568 && NR<5700 && /^ *19[0-9] *$/{print NR\": \"$0}' KNT.txt | head -4; echo \"=== line 5560-5570\"; sed -n '5560,5572p' KNT.txt | cut -c1-200"
}
```


### [2026-09-05T20:11:17.912Z] TOOL RESULT

```
4054: 186
5416: 185
5425: 186
5463: 187
5475: 188
5518: 189
5556: 191
--- after
5598: 193
5685: 197
5696: 198
=== line 5560-5570
Dubála- sb. ‘Dubala’, a district in Baby- lonia: Elam. du-ib-ba--- ($6, $107). Dubala пет. DB 3.79.
dūra- adj. ‘far (in time or space)’: Av. düra-, . NPers. dür, Skt. dürd- (5148.1). See also dürada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. du
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvara
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted b
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also duwilàáparanam. дилат, asn, as adv. ‘a second time’, DB 2.87f, 57, 3
duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
```


## [2026-09-05T20:11:38.911Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -rn \"Dhreugh\\|Dhrugh\" data/verification/agent/charts/ data/extracted/index* 2>/dev/null | head -20\necho \"=== search all batch for droogh/deceive roots\"\ngrep -rln \"دروغ\" data/extracted/batch/ | head"
}
```


### [2026-09-05T20:11:38.966Z] TOOL RESULT

```
(eval):2: no matches found: data/extracted/index*
=== search all batch for droogh/deceive roots
data/extracted/batch/page-135.json
data/extracted/batch/page-270.json
```


## [2026-09-05T20:11:41.278Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' data/verification/agent/charts/page-135.txt"
}
```


### [2026-09-05T20:11:41.325Z] TOOL RESULT

```
=== PDF page 135 (book page 105) ===
--- entry 0 ---
ROOT Dhont -> redirect to Dhen
--- entry 1 ---
ROOT Dhrâbh -> redirect to Dher 2
--- entry 2 ---
ROOT [Indo-European] Dhragh 1, Dhreg : to pull  (refs POK:257)
#1 (parent #0) [Russian] refs=AHD:400 | drožki : carriage
  #2 (parent #1) [Persian] refs=MON:1511; BQT:837 | doroškeh «درشکه» : horse driven carriage
  #3 (parent #1) [English] refs=None | droshky
#4 (parent #0) [Germanic] refs=AHD | dragan : to draw
  #5 (parent #4) [English] refs=None | draw, drag, draft
#6 (parent #0) [Germanic] refs=AHD | drinkan : draw into the mouth
  #7 (parent #6) [English] refs=None | drink, drown
--- entry 3 ---
ROOT Dhragh 2 -> redirect to Dher 2
--- entry 4 ---
ROOT Dhreg -> redirect to Dhragh 1
--- entry 5 ---
ROOT [Indo-European] Dhreugh : to deceive  (refs POK:276)
#1 (parent #0) [Avestan] refs=POK:276; BQT:845; SNS:324 | draoga,drauga : a lie, a demon ; dragvant, drvant : one who likes lies, atheist.
  #2 (parent #1) [Pahlavi] refs=BQT:846; SNS:324,325 | drôg : a lie ; druvand : non-believer
    #3 (parent #2) [Persian] refs=BQT:846; SNS:324; BQT:845; TZF:22 | dorŭğ «دروغ» : a lie ; dorvand «دُروند» : atheist
#4 (parent #0) [Old Persian] refs=KNT:191 | duruj : lie, deceive
#5 (parent #0) [Germanic] refs=AHD | drauma : illusion, vision
  #6 (parent #5) [English] refs=None | dream
--- entry 6 ---
ROOT Dhrugh -> redirect to Dhwer
--- entry 7 ---
ROOT Dhu -> redirect to Dheu 2
--- entry 8 ---
ROOT Dhu-bh -> redirect to Dheu 2
--- entry 9 ---
ROOT Dhugh -> redirect to Dheugh
--- entry 10 ---
ROOT Dhugh-tar -> redirect to Dheugh
```


## [2026-09-05T20:11:56.801Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T20:11:56.884Z] TOOL RESULT

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


## [2026-09-05T20:12:15.666Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT dvar Tuer\"; grep -n \"^• *j\\. *dvar\\|dvar- \\|'Tür'\\|,Tür'\\|Tür,\" BRT.txt | head -15\necho \"=== BRT search 766\"; grep -n \"duuara\\|dvarim\\|dvar»m\" BRT.txt | head -10"
}
```


### [2026-09-05T20:12:15.735Z] TOOL RESULT

```
=== BRT dvar Tuer
13975:•  j-,  g.  'dvar-  V.  'gehen',  uzw.  von ifoA^chen  Wesen".  Praes.  2  dvara-, 4  äväru:
13987:•  j.  dvarant-  Adj.  (fem.  'raitl-y*,  PFA.: s.  'dvar-.
23246:•  j.,  g.  vazdvar-  n.  'Beständigkeit';  a)  sva. 'Ausdauer':  tanvS  vlspayh  drvatätsm  lanvs vUpayh  °pffl«  Yt  14.29;  —  tanvS'vars.. tamis  vpr?%rfm  Y.6S.11.  b)  sva.  'un- unterbrochene Dauer':  disyJt  ahmai  naire avat  müdsm  . .  'var)  vakistakt  aithSus V.J. 44;  —  ma*dä  dadat  ahurS  hauniats atmrttätas^a . .  asahyäcä  . .  xia%rahy3  sarO vatfhSul  'varV^  manatahö  yS  .  .  "MAk. wird  . .  die  besändige  Gemeinschaft''  mit If.  und  Am.  und  mit  Asa,  mit  Xf.,  mit VM,  dem  gewähren,  der  .  ."  Y._;r.  21.
=== BRT search 766
3553:höchste,  höchstgelegene,  höchststehende':  •  j.  apayant-  AdJT  PPA.:  s.  ap-. upa  dvar»m  xsaiireMtiym{sA.) 'mstn  karj-\    j_    apayantama*    Adj,    'maxime    pro- Aaifl  "..dem  höchstgelegenen  in Ä:"yLj.  pellendus':   'maieca  a»rahe  mainysus  \\, 54.         a)  mit  alahe  und  aiät  'der  höchste  21.  i.
```


## [2026-09-05T20:12:17.485Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN thyroid\"; grep -n \"thyroid\" KLN_1966.txt | head -5\necho \"=== KLN door\"; grep -n \"^door\\b\\|door, n\\.\" KLN_1966.txt | head -5\necho \"=== KLN forest\"; grep -n \"forest\\b\" KLN_1966.txt | head -5\necho \"=== KLN foreign\"; grep -n \"foreign,\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T20:12:17.582Z] TOOL RESULT

```
=== KLN thyroid
1573:Adam’s  apple,  the  thyroid  cartilage.  —  A  name due  to  the  inexact  translation  of  Heb.  lappiiai 1 haaddm ,  lit.  ‘man’s  projection  (in  the  neck)’,  fr. tappOalf,  ‘anything  swollen  or  protruding; apple’,  from  the  base  of  tdphah,  ‘it  swelled’.  The rendering  of  this  Hebrew  term  by  ‘Adam’s apple’  is  due  to  two  popular  beliefs:  1)  that  the forbidden  fruit  eaten  by  Adam  was  an  apple; 2)  that  a  piece  of  this  apple  stuck  in  Adam’s throat.
9660:cretinism,  n.,  a  disease  caused  by  the  deficiency of  the  thyroid  gland  (med.)  —  F.  cretinisme, formed  fr.  cretin  with  suff.  -isme.  See  cretin and  -ism.
12080:doom  palm.  —  F.  doum,  fr.  Arab,  dawm,  daum, dum,  ‘a  large  Egyptian  palm  tree’, doomsday,  n.,  the  day  of  the  Last  Judgment.  — OE.  domesdxg,  ‘day  of  judgment’,  fr.  domes, gen.  of  dom,  ‘doom,  judgment’,  and  dxg,  ‘day’. See  doom  and  day  and  cp.  Domesday  (Book). Doomsday  Book.  —  See  Domesday  (Book), doomster,  n.,  judge.  —  A  var.  of  deemster,  demp- ster;  influenced  in  form  by  doom, door,  n.  —  ME.  dore,  dure,  fr.  OE.  dor,  ‘door, gate’,  duru,  ‘door’,  rel.  to  OS.  dura,  ON.  dyrr, Dan.  dor,  Swed.  dorr,  OFris.  dure,  dore,  OHG. turi,  MHG.,  G.  tur,  ‘door’,  OHG.,  MHG.,  G. tor,  Goth,  daur,  ‘gate’,  and  cogn.  with  OI. dvdrah  (nom.  pi.),  durah,  diiralt  (acc.  pi.), ‘door’,  durona-,  ‘dwelling,  home’,  Avestic  dvarlm (acc.  sing.),  ‘gate,  court’,  OPers.  duvaraya-, ‘at  the  door’,  Toch.  B  twere.  Arm.  durk'  (pi.), durn  (sing.),  Gk.  Silpa,  ‘door’,  ffupu;,  ‘window’, Trapa&upa,  ‘side  door,  wicket’,  npoDupov,  ‘front door,  doorway,  porch’,  Alb.  dere,  pi.  direr,  ‘door, house’,  L  .fores  (pi.),  ‘door’,  fords,  ‘out  of  doors, out’,  forts,  ‘out  at  the  doors,  out  of  doors’, OSlav.  dviri,  ‘door’,  dvoru,  ‘courtyard’,  Lith. diirys,  Lett,  duris,  ditrvis,  OPruss.  dauris,  ‘door’, W.,  Co.,  OBret.  dor,  OIr.  dorus,  OCo.  darat, ‘door’.  Cp.  dargah,  dehors,  doch-an-doris,  dur¬ bar,  durwaun,  foreclose,  foreign,  forisfamiliate, forjudge,  hors  de  combat,  hors  d’oeuvre,  Thyri- didae,  thyroid.
27363:thyme  and  1st  -ia  and  cp.  tbio-. parathyroid,  adj.,  pertaining  to,  or  lying  near,  the thyroid  gland  ( med .)  - —  Coined  by  Ivar  Sand- strom  of  Upsala  in  1879,  fr.  para-  and  thyroid. Derivative:  parathyroid-al,  adj. paratroop,  n.  —  Abbreviation  of  parachute  troop.
39203:meaning  ‘thyroid’.  —  Shortened  fr.  Gk.  ffupo- EiSr)?.  See  thyroid  and  cp.  thyro-.
=== KLN door
=== KLN forest
1869:afforest,  tr.  v.,  to  turn  into  a  forest.  —  ML. afforestare,  fr.  ad-  and  forestare,  fr.  Late  L. forestis  (scil.  silva),  ‘open  woodland’.  See  forest
1871:Derivatives :  afforest-ation,  n.,  afforest-ment,  n. affranchise,  tr.  v.  —  Fr.  F.  affranchiss-,  pres.  part, stem  of  affranchir,  ‘to  free,  set  free,  liberate’,  fr. a,  ‘to’  (see  a),  and  franc,  fern,  franche,  ‘free’.  See ad-  and  franchise.
5373:Boreas,  n.,  the  god  of  the  north  wind  in  Greek mythology.  —  L.,  fr.  Gk.  Bop &u.q,  fr.  (5op£ai;, ‘north  wind’,  which  is  of  uncertain  origin.  It possibly  stands  for  I.-E.  *gwore-yas  and  orig. meant  ‘mountain  wind’,  and  is  cogn.  with  OI. girth,  Avestic  gairi,  ‘mountain’,  Alb.  gur,  ‘rock’, OSlav.  gora,  ‘mountain’,  Lith.  g'tre,  ‘forest’.  Cp. bora,  Boreades,  boreal  and  the  second  element in  Hyperborean.  Cp.  also  Croat, borecole,  n.,  kind  of  cabbage.  —  Prob.  fr.  Du. boerenkool,  lit.  ‘peasant’s  cabbage’.  See  boor and  cole.
5400:Bostrychidae,  n.  pi.,  a  family  of  beetles  (entomol.) —  ModL.,  formed  with  suff.  -idae  fr.  Gk.  porr- -rpux°;>  ‘lock  of  hair,  curl,  foliage;  a  winged insect’,  which  is  of  uncertain  origin.  It  possibly stands  for  *gwostruchos  and  orig.  meant  ‘some¬ thing  twisted’,  and  is  cogn.  with  OSerb.  goozd, ‘forest’,  Czech  hvozd,  ‘mountain’,  MHG.,  G. quatt,  quaste,  ‘tuft,  knot',  Alb.  gett,  ‘foliage, branch’.
5443:bouquet,  n.,  1)  a  bunch  of  flowers,  nosegay; 2)  aroma.  —  F.,  orig.  meaning  ‘grove,  thicket’, dimin.  formed  fr.  ML.  boscus,  ‘wood’,  whence also  F.  bois,  ‘wood,  forest’;  see  bush  and  cp. bosket.  For  the  original  sense  of  bouquet  cp. bouquet  d'arbres,  ‘group  of  trees,  grove’. Bourbon,  n.,  a  member  of  the  royal  family  in France  which  reigned  1589-1792  and  1815- 1848.  —  F.,  from  Bourbon  l’Archambault,  chief town  of  a  lordship  in  central  France.  The  place name  Bourbon  is  traceable  to  Borvo,  name  of  a thermal  deity.  See  burbot.
=== KLN foreign
1281:acacia,  n.  —  L.  acacia,  fr.  Gk.  axaxia,  shittah tree’,  which,  like  axaxaXl s,  ‘gall  of  the  Oriental tamarisk’,  is  of  foreign,  prob.  Egyptian  origin. Both  axaxia  and  axaxaXii;  were  prob.  influenced in  form  by  oixavfta,  ‘thorn,  prickle’,  and  other Greek  derivatives  of  I.-E.  base  *ak-,  ‘sharp  . academe,  n.  academy  (poetic).  —  See  academy, academic,  adj.  —  L.  academicus,  fr.  academia. See  academy  and  -ic.
3488:‘lamb’,  and  to  Homeric  and  Ion.  Gk.  eipoc, ‘wool’;  see  erio-.  The  second  element  is  of  un¬ certain,  prob.  foreign,  origin, aroint,  intr.  v.  (used  only  in  the  imper.),  begone!
4221:babble,  intr.  and  tr.  v.  —  ME.  babelen,  from  the I.-E.  imitative  base  *bab-,  whence  also  ON. babba ,  Swed.  babbla ,  Norw.  babble,  LG.  bab- beln,  Du.  babbelen,  G.  babbeln,  ‘to  prattle',  L. babulus ,  ‘babbler’,  F.  babilter,  ‘to  stutter,  stam¬ mer’  ;  cp.  babe,  baboon,  bauble.  Cp.  the  related imitative  base  *balb-,  whence  L.  balbus,  ‘stam¬ merer’  ;  see  balbuties,  booby.  Cp.  also  the  related imitative  base  *barb-,  ‘to  stammer’,  whence  Gk. ^ap^apoi ;,  ‘foreign,  barbarous’;  see  barbaric, brave.
4426:Barbara,  fern.  PN.  —  L.,  prop.  fern,  of  barbarus, ‘strange,  foreign,  barbarous’,  fr.  Gk.  (3ap(3apop. See  barbaric.
4427:Barbarea,  n.,  a  genus  of  plants  of  the  mustard family  (bot.)  —  ModL.,  named  after  St.  Barbara. barbarian,  n.  and  adj.  —  Formed  with  suff.  -ian fr.  Gk.  fSapPapop.  See  barbaric, barbaric,  adj.  —  OF.  barbarique,  fr.  L.  barbari- cus,  ‘foreign,  strange,  outlandish’,  fr.  G.  pap- fJocpixop,  fr.  pippapop,  ‘non-Greek,  foreign, barbarous’,  which  is  cogn.  with  OI.  barbarah, ‘stammering  (designation  of  the  non-Aryan nations),  from  the  I.-E.  imitative  base  *barb-, ‘to  stammer,  stutter;  unintelligible’.  Cp.  brave. Cp.  also  Berber  and  the  second  element  in  rhu¬ barb.  For  *balb-,  a  collateral  base  of  *barh-,  see balbuties,  booby.  For  the  imitative  base  *bab- see  babble.
```


## [2026-09-05T20:12:28.877Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"thyroid,  adj\\|thyroid,  n\\|Thyreo\\|thyreos\\|ffupsoq\\|Oupsoi;\" KLN_1966.txt | head -10\necho \"=== 1971\"; grep -n \"thyroid\" KLN_1971.txt | head -8"
}
```


### [2026-09-05T20:12:28.945Z] TOOL RESULT

```
27363:thyme  and  1st  -ia  and  cp.  tbio-. parathyroid,  adj.,  pertaining  to,  or  lying  near,  the thyroid  gland  ( med .)  - —  Coined  by  Ivar  Sand- strom  of  Upsala  in  1879,  fr.  para-  and  thyroid. Derivative:  parathyroid-al,  adj. paratroop,  n.  —  Abbreviation  of  parachute  troop.
39205:thyro-,  before  a  vowel  thyr-,  combining  form meaning  ‘thyroid’.  —  Shortened  fr.  Gk.  fhipEo- eiSyii;.  See  thyroid  and  cp.  thyreo-. thyroid,  adj.,  pertaining  to,  or  designating  the ductless  gland  in  the  neck,  which  has  an  im¬ portant  effect  on  the  growth  of  the  body;  lit. ‘shield-shaped’  (anat.)  —  Medical  L.  thyreoi- deus,  fr.  Gk.  ffupEOEtSfjC,  ‘shield-shaped’,  com¬ pounded  of  ffopEo;,  ‘stone  put  against  a  door; oblong  shield’,  which  is  rel.  to  fKipa,  ‘door’, and  of  -oeiSif)i ‘like',  fr.  eISo;,  ‘form,  shape’. See  door  and  -oid.
39206:Derivatives:  thyroid,  n.,  the  thyroid  gland, thyroid-ism,  n.,  thyroid-iz-ation,  n.,  thyroid-less, adj.
=== 1971
7041:Adam’s apple, the thyroid cartilage. — A name 
59831:of the thyroid gland {med.) — F. cretinisme , 
75476:didae, thyroid. 
173776:parathyroid, adj., pertaining to, or lying near, the 
173777:thyroid gland ( med .) — Coined by Ivar Sand- 
173778:strom of Upsala in 1879, fr. para- and thyroid. 
173779:Derivative: parathyroid-al y adj. 
247701:meaning ‘thyroid’. — Shortened fr. Gk. Dupo-
```


## [2026-09-05T20:12:49.108Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | head -60; echo \"=== AFM/PLA/LKT files\"; ls | grep -i \"AFM\\|PLA\\|LKT\\|FVQ\\|DOZ\\|DEV\\|PHN\""
}
```


### [2026-09-05T20:12:49.158Z] TOOL RESULT

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
=== AFM/PLA/LKT files
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
DEV.txt
DOZ.txt
FVQ_pages.txt
FVQ.txt
LKT.txt
PHN.txt
```


## [2026-09-05T20:12:53.283Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM درب\"; grep -n \"درب\\b\" AFM.txt | head -10\necho \"=== AFM_pages\"; grep -n \"الدرب\\|درب (\" AFM_pages.txt | head -10\necho \"=== LKT darb\"; grep -n -i \"darb\\b\" LKT.txt | head -10\necho \"=== DOZ darb\"; grep -n -i \"^darb\\|darb \" DOZ.txt | head -10"
}
```


### [2026-09-05T20:12:53.381Z] TOOL RESULT

```
=== AFM درب
738:* (البربيطاء ) الثياب معرب ܨ ܢܝܐ ومعناها الصدربة وهي ثاب يلسها 
2526:ܩܡ 05 الدرب تعر برب در ند بجذف شطره الاخير وهو 23 
2527:١‏ الدربان») 6 ܐ من در اي باب ومن بان اي حافظ 
2590:ܢ الدرب بالفارسة وبدور علمها ܢܪ 
7235:دربا 5 
=== AFM_pages
1560:ܩܡ 05 الدرب تعر برب در ند بجذف شطره الاخير وهو 23
1561:١‏ الدربان») 6 ܐ من در اي باب ومن بان اي حافظ
1604:ܢ الدرب بالفارسة وبدور علمها ܢܪسس ܨܕ -
=== LKT darb
1273:488.  Ar.  darb:
1275:489.  Ar.  darb:
=== DOZ darb
```


## [2026-09-05T20:12:54.514Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ darb\"; grep -n -i \"darb\" FVQ.txt | head -10\necho \"=== MON part1 درب\"; grep -n \"تیروئید\\|تیرویید\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -10"
}
```


### [2026-09-05T20:12:54.583Z] TOOL RESULT

```
=== FVQ darb
=== MON part1 درب
incoming/MON/MON_2vol_Adena_v1_djvu.txt:27831:پار تیروئید: 0013( .( (بر.) دو زوج 
MON_part2.txt:773:فوق کلیوی و تیروئید. برخی غدد هم دارای 
MON_part2.txt:35586:9 اثر ازدیاد حجم غدة تیروئید در 
MON_part2.txt:35601:تیروئیدی کویند و يا با نقصان ترشح غده 
MON_part2.txt:35610:موضعی غده تیروئید است و به عبارت 
MON_part2.txt:35612:غده تیروئید می‌باشد. ا کر این تورم غده 
MON_part2.txt:35620:گواتر همراه با هیپرتیروئیدی: (پز.) این 
MON_part2.txt:35657:هیپوتیروئیدی: (پز.) اين نوع گواتر به دو 
MON_part2.txt:35663:انتظار تیروئیدها دچار صغر می‌شوند ولی 
MON_part2.txt:70538:نقصان ترشح غدهٌ تیروئید عارض می‌گردد.
```


## [2026-09-05T20:13:04.928Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1270,1285p' LKT.txt\necho \"=== AFM page marker for line 2526\"; awk 'NR<=2526 && /\\[pdf page/ {p=$0} END{print p}' AFM_pages.txt; grep -n \"\\[pdf page\" AFM_pages.txt | head -3\necho \"=== AFM_pages line 1560 page\"; awk 'NR<=1560 && /\\[pdf page/ {p=$0} END{print p}' AFM_pages.txt"
}
```


## [2026-09-05T20:13:05.439Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '27825,27840p' incoming/MON/MON_2vol_Adena_v1_djvu.txt; echo \"=== grep تیروئید as headword\"; grep -n \"^تیروئید\\| تیروئید:\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head"
}
```


### [2026-09-05T20:13:06.754Z] TOOL RESULT

```
Auch  daranag,  darünag  'eine  Pflanze aus  der  Familie  der  Seneeionen',  also eine  Komposite;  hieraus  der  botanische Name  lat.  dwonicum,  sp.  doronica,  pg. doronico,  frz.  doronic.  [Devic  DEt  104. Lammens  Rem  99.
487.  Ar.  daraka:
'Ledersc-hild' ;  hieraus  mit  ar.  Art.  sp. adarga,  pg.  adarga  'dass.',  frz.  adargue 'ein  kleiner  Schild,  der  an  einer  kurzen Lanze  angebracht  ist'.  —  [Dagegen  ge- hören frz.  targe,  sp.  tarja  usw.  trotz Lammens  Rem  236/237  zu  germanisch targa].   [DE  41.   Eguilaz  48    ML  2471.
488.  Ar.  darb:
'Weg,  enger  Weg';  hieraus  mit  ar.  Art. sp.  adarve  'der  Mauerkranz,  auf  dem die  Zimmer  ruhen',  pg.  adarve  [Con- stancio  Dicc  21  b]  'Befestigungsmauer, enger  Weg  darauf  mit  Schießscharten'. —  [Ar.  dirwa,  das  u.  a.  'Schießscharte' bedeutet,  kommt  wohl  trotz  asp.  adarves 'dass.'  nicht  in  Frage.]  [DE  41/43. Eguilaz  50.    ML  ■i47ü.
489.  Ar.  darb:
'Das  Prägen'  [subst.  Infinitiv  des  Vbs. daraba  'schlagen,  prägen'];  über  das tk.  tarab  wurde  hieraus  rum.  tarabä 'Ladentisch',  Ableitung  täräboiü,  tärä- bufä.  —  Mit  pers.  hänä  [s.  hier  Nr.  809] ergibt  sich  pers.  ar.  darbhäna  'Präge- stätte, Münze  (als  Gebäude)';  hieraus rum.  tarapana  'dass.'.  [Löbel  EITAP  92.
490.  Pers.  därbän:
'Türhüter'  [von  pers.  dar  'Tür'  Horn NpEt  S.  120,  Nr.  545  und  -bän  'Herr, hütend'  ebenda  S.  41,  Nr.  176];  hieraus angloind.  durwaun  'ein  Hausdiener  in den  größeren  Häusern  Kalkuttas,  der als  Portier  des  Compound  [s.  hier  Nr.  1045] dient',  rum.  derebant,  doroban^,  trabant [SBKAW  Wien  L,  591],  it.  sp.  pg.  tra- bante,  frz.  drabant,  trabant;  ndl.  tra- bant, dtsch.  Trabant  'Leibwächter',  eben- so poln.  daraban,  drab,  klruss.  grabant, russ.  drabant  [Gorjajew  XXXIX].  —  Die Ableitung  aus  böhni.  drdb  'Fufsvolk', wie  sie  Kluge  456  und  Bern  SlEtWb  219 geben,  ist  eine  unbegründete  Erschwe- rung; es  ist  zu  bedenken,  daß  schon Mikl  SIEtWb  49  richtig  derban  'Tor- wächter' als  Grundwort  angibt,  nicht wie  Berneker  ein  osm.-peis.  derbend 'leicht  zu  verteidigender  Ort,  Wacht- posten". Was  die  Bedeutung  angeht, so  liegt  nicht  die  geringste  Schwierig- keit vor,  da  ja  Übergang  von  'Torwart' zu  'Kriegsknecht'  als  Erweiterung  des Begriifs  leicht  anzunehmen  ist.  Auch lautlich  ist  wegen  des  langen  ä  des Grundworts  der  Übergang  zu  Trabant mit  Anlehnung  an  eine  latinisierende Endung  -ant,  ebenso  it.  trabante  usw. möglich.  Hobson-Jobson  333.  ML  8822. [Dagegen  A.  KLÜYVER  in  ZfdWf  IV, 1.53—160].
491.  Pers.  därbär:
[Aus  pers.  dar  s.  hier  Nr.  490  und  -bär nur  in  Kompositis  zur  Bezeichnung eines  Ortes,  Horn  NpEt  S.  36,  Nr.  158]; hieraus  angloind.  engl,  durbar  'Hof  eines indischen  Fürsten'  oder  'Empfang  an einem  solchen  Hofe,  Staatsempfang  beim Vizekönig'.    [Hobson-Jobson  331.
492.  Pers.  därbedär:
[Aus  pers.  dar  'Tür',  s.  hier  Nr.  490,  u.
I^ers.  därd.]
40
be  Präposition  'zu,  bei,  an',  Horn  NpEt S.  33,  Nr.  144]  'einer,  der  von  Tür  zu Tür  gellt;  Bettler,  Vagabund',  ebenso tk.;  hieraus  rum.  derbedeü,  derbeder '  Paugenichts,  Vagabund,  Bummler'.
=== AFM page marker for line 2526

=== AFM_pages line 1560 page
```


### [2026-09-05T20:13:06.825Z] TOOL RESULT

```
4 بارسال. 


رراعت آبی؛ مف. + دمم 

پبارابلوم: صمااق:2 (۰) نوعی اسلحه 
پار تیروئید: 0013( .( (بر.) دو زوج 
غده که در طرفین غده تیروئند قرار دارند» 


فرهنگ فارسی معیر پاراج 


بطوری که دو تا در بالا و دو تا در بایین قرار 
گرفته» عمل این غده‌ها تنظیم و بررسی 
متایو لیسم بدن است و حدذف غده‌های مزبور 
=== grep تیروئید as headword
27831:پار تیروئید: 0013( .( (بر.) دو زوج
```


## [2026-09-05T20:13:15.854Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86%D8%AF%D8%B1",
 "prompt": "Give the Persian entry بندر (bandar): meaning 'port/harbour' and the etymology stated (any analysis as band + dar, Middle Persian form, Hasandust or other cited sources), plus the Arabic entry if present."
}
```


## [2026-09-05T20:13:16.910Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A8",
 "prompt": "Give the Arabic entry درب (darb): meaning and etymology (is it said to be borrowed from Persian در dar / darband?), and the Persian entry درب if present."
}
```


### [2026-09-05T20:13:22.120Z] TOOL RESULT

```
# Persian and Arabic Entries for بندر (bandar)

## Persian Entry

**Meaning:** The Persian entry defines بندر (bandar) as meaning "port" or "harbour."

**Etymology:** The etymology section notes that it is incomplete, stating: "This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium." The page suggests a possible analysis of بند (band, "band, tie") + در (dar, "door"), noting this "makes phonetic and semantic sense, but is there literature to confirm this?" No definitive etymological source or cited scholars like Hasandust are provided.

## Arabic Entry

**Meaning:** The Arabic entry (بَنْدَر, bandar) carries the same meanings: "port" and "harbour." It is a masculine noun with the plural form بَنَادِر (banādir).

**Etymology Connection:** The Arabic entry was borrowed from Classical Persian بَنْدَر (bandar), establishing the Persian term as the etymological source for the Arabic usage.
```


### [2026-09-05T20:13:23.860Z] TOOL RESULT

```
# Arabic and Persian Entry: درب (darb)

## Arabic Entry (درب)

**Meaning**: The Arabic noun **دَرْب** (darb) means "path," "pass," or "way."

**Etymology**: Contrary to your question, the word is **not** borrowed from Persian. According to the Wiktionary entry, it was "borrowed from Ancient Greek _Δέρβη_ (Dérbē), a border town in Lycaonia at the Cilician Gates."

## Persian Entry (درب)

**Meaning**: The Persian noun **درب** (darb) means "gate."

**Etymology**: The Persian term derives from Middle Persian origins, traced back through Proto-Iranian to Proto-Indo-European *dʰwṓr* meaning "door." The etymological path shows: Middle Persian *darbās* → Proto-Iranian *dwā́r* → Proto-Indo-European *dʰwṓr*.

**Note**: The Persian and Arabic words, despite identical spelling and transliteration, have distinct etymological origins—the Arabic comes from Greek, while Persian has Indo-European roots.
```


## [2026-09-05T20:13:31.220Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor W in \"درب\" \"بندر\" \"در\" \"دوک\"; do echo \"########## $W\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$W\")&action=raw\" | grep -n \"Etymology\\|etyl\\|inh\\|bor\\|der|\" | head -40; done 2>&1 | head -120"
}
```


### [2026-09-05T20:13:34.314Z] TOOL RESULT

```
########## درب
4:===Etymology 1===
5:Borrowed from {{bor|ar|grc|Δέρβη|t=[[Derbe]]}}, a border town in [[Lycaonia]] at the {{w|Cilician Gates}}.
21:* {{desc|syc|ܕܰܪܒܳܐ|tr=darbā|t=way, path|bor=1}}
22:* {{desc|osp|adarve|adarbe|bor=1}}
24:* {{desc|kmr|rê u ''derb''|t=manner, way|bor=1}}
26:===Etymology 2===
47:===Etymology 3===
77:===Etymology 1===
78:From {{inh|shu|ar|دَرْب}}, from {{der|shu|grc|Δέρβη}}.
85:===Etymology 2===
86:{{ety|shu|:inh|ar:دَرَّبَ|text=+|tree=1}}
99:===Etymology===
100:From {{inh|fa|pal|dlpʾs|tr=darbās}}, a derivative of {{der|fa|ira-pro|*dwā́r}}, from {{der|fa|iir-pro| *dʰwā́r}}, from {{der|fa|ine-pro|*dʰwṓr|t=door}}.<ref>{{R:ira:ESIJa|vol=2|page=502}}</ref>
116:===Etymology===
117:{{ety|ajp|:inh|ar:دَرَّبَ|text=+|tree=1}}
########## بندر
11:===Etymology===
12:{{ety|ar|:bor|fa-cls:بَنْدَر|text=+|tree=1}}
28:* {{desc|sw|bandari|bor=1}}
39:===Etymology===
40:{{bor+|gwt|ps|بندر}} or {{bor|gwt|ur|بندر}}, from {{der|gwt|fa|بندر}}.
51:===Etymology===
52:{{ety|acx|:inh|ar:بَنْدَر|text=+|tree=1}}
67:===Etymology===
68:{{bor+|ota|fa-cls|بَنْدَر|t=port}}.
79:* {{desc|tr|Bender|inh=1}}
80:* {{desc|ro|Bender|g=m|bor=1}}
82:** {{desc|uk|Бенде́ри|g=m-p|inh=1}}
84:*** {{desc|lt|Bendèrai|g=m-p|inh=1}}
85:** {{desc|pl|Bendery|g=nv|bor=1}}
86:** {{desc|zle-mru||g=m-p|bor=1}}
87:*** {{desc|ru|Бенде́ры|g=m-p|inh=1}}
91:===Etymology===
92:{{bor+|ps|fa-cls|بَنْدَر}}.
98:# [[border]] {{gl|crossing}}
107:===Etymology===
125:* {{desctree|ar|بَنْدَر|bor=1}}
126:* {{desc|gu|બંદર|bor=1}}
127:* {{desc|inc-hnd|-|bor=1}}
130:* {{desctree|ms|bandar|bor=1}}
131:* {{desctree|ota|بَنْدَر|tr=bender|bor=1}}
132:* {{desc|ps|بَنْدَر|bor=1}}
133:* {{desctree|tk|bender|bor=1}}
139:===Etymology 1===
140:{{bor+|ur|fa-cls|بندر|tr=bandar}}. Compare {{cog|bn|বন্দর}}, {{cog|dv|ބަނދަރު}}.
151:===Etymology 2===
152:Contracted from {{der|ur|inc-ohi|बांदर}}, from {{der|ur|pra-sau|𑀯𑀸𑀡𑀭}}, from {{der|ur|sa|वानर}}. 
########## در
4:===Etymology 1===
6:From {{inh|ar|afa-pro|*dâr-|t=to increase}}. Cognate with {{cog|sem-srb|𐩵𐩧𐩧|t=abundance, harvest}}.
19:===Etymology 2===
40:===Etymology 3===
52:* {{desc|az|dürr|bor=1}}
53:* {{desc|uz|dur|bor=1}}
54:* {{desc|kmr|durr|bor=1}}
56:===Etymology 4===
73:===Etymology===
74:{{ety|gwc|:inh|sa:*द्वर<ety:from< द्वार्<tr:dvā́r>>>|tree=1|text=++}}
92:===Etymology===
93:{{bor+|inc-opa|fa-cls|دَر}}.
113:===Etymology 1===
120:===Etymology 2===
121:From {{bor|ota|fa-cls|در|tr=durr}}, from {{der|ota|ar|دُرّ}}.
129:===Etymology 3===
130:From {{bor|ota|fa|در|tr=dar}}.
138:===Etymology 4===
149:===Etymology 5===
175:===Etymology 1===
201:===Etymology 2===
202:{{ety|fa|id=door|:inh|pal:𐫅𐫡<ts:dar><t:gate, court, palace, chapter, subject><id:gate><ref:{{R:ira:ESIJa|vol=2|page=500}}>|tree=1|text=+}}
231:===Etymology 3===
232:{{ety|fa|:bor|ar:دُرّ|text=+|tree=1}}
243:===Etymology 4===
253:===Etymology 5===
273:===Etymology===
274:{{inh+|sd|sa|द्वार्}}
299:===Etymology===
300:{{ety|ur|:bor|fa-cls:دَر<id:door>|tree=1|text=++|doublet=دْوَار}}
313:===Etymology 1===
325:===Etymology 2===
326:From {{bor|ush|fa-cls|در|tr=dar}}.
########## دوک
13:===Etymology 1===
14:From {{inh|fa|pal|𐭣𐭥𐭪|tr=dwk' /dōk/|t=spindle}}
28:* {{desc|klj|dûk|bor=1}}
30:===Etymology 2===
31:{{bor+|fa|fr|duc}}.
```


## [2026-09-05T20:13:54.084Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%D8%B1%D8%A8/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for درب verbatim, including any origin tag such as [ع.] or [په.], and also quote the لغت‌نامه دهخدا entry's statement about the origin of درب."
}
```


## [2026-09-05T20:13:55.043Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%DB%8C%D8%B1%D9%88%D8%A6%DB%8C%D8%AF/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for تیروئید verbatim, including the origin tag (e.g. [فر.] French) and the definition."
}
```


### [2026-09-05T20:14:00.157Z] TOOL RESULT

```
# فرهنگ معین Entry for تیروئید

According to the Mo'in Dictionary section, the entry reads:

"[فر.] (اِ. ) غده ای است در زیر گلو که ماده ای به نام تیروکسین را در خون ترشح می کند."

This translates to a gland beneath the throat that secretes a substance called thyroxine into the blood. The entry also notes that enlargement of this gland is called goiter, and its deficiency can cause skin puffiness.
```


### [2026-09-05T20:14:00.166Z] TOOL RESULT

```
# Mo'in Dictionary Entry

From فرهنگ معین:

"(دَ رْ ) [ ع . ] (اِ. ) درِ بزرگ ، دروازة شهر یا قلعه . ج . دروب ."

The origin tag [ع.] indicates an Arabic origin.

# Dehkhoda Dictionary Statement on Origin

According to لغت‌نامه دهخدا, scholar Jawaliqi states in his work Al-Mu'arrab that "درب" is not originally Arabic in etymology. He explains that Arabs adopted this term to mean "gates," applying it similarly to narrow mountain passes in Roman territories that functioned as gateways.
```


## [2026-09-05T20:14:12.505Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/forest",
 "prompt": "Give the full etymology of 'forest', including the Medieval Latin forestis/foresta and Latin foris/foras discussion, and any alternative Germanic (*forhist) theory. Also quote the entry for 'foreign'."
}
```


## [2026-09-05T20:14:14.452Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%86%D8%AF%D8%B1/",
 "prompt": "Quote the فرهنگ معین entry for بندر (any origin tag) and the دهخدا entry's remarks on the origin/etymology of بندر (e.g. whether it is analysed as بند + در, or as a loan)."
}
```


### [2026-09-05T20:14:19.118Z] TOOL RESULT

```
# Etymology of Forest

## Primary Etymology

The word "forest" entered English in the late 13th century from Old French *forest*, meaning "extensive tree-covered district." The source traces to Medieval Latin *forestem silvam*, literally "the outside woods," a term from Charlemagne's Capitularies designating the royal forest.

The core theory suggests the word derives from Latin *foris* ("outside"), possibly through a Germanic intermediary similar to Old High German *forst*. This interpretation supports the meaning "beyond the park"—understanding the park as the central enclosed woodland, with the forest being the outer, uncontrolled territory.

An alternative etymology proposes Medieval Latin *forestis* (originally "forest preserve, game preserve") comes from Latin *forum* in its legal sense of "court" or "judgment," implying "land subject to a ban."

The word replaced the Old English *wudu*.

## Related Entry: Foreign

The adjective "foreign" emerged around 1300 from Old French *forain*, meaning "strange" or "outside the boundaries." It stems from Medieval Latin *foraneus* ("on the outside, exterior"), derived from Latin *foris* ("outside"). The term shares the same Latin root as forest, both ultimately connecting to PIE *\*dhwor-* ("door, doorway").
```


### [2026-09-05T20:14:22.413Z] TOOL RESULT

```
# Entries for بندر

## فرهنگ معین Entry

"(بَ دَ ) ( اِ. ) محلی است در ساحل دریا یا رودخانه که محل توقف و بارگیری است"

This concise definition describes a port as a location on a sea or river coast designated for stopping and loading cargo.

## دهخدا Entry – Etymology Notes

The دهخدا dictionary offers two key etymological perspectives:

1. **Compositional Analysis**: The entry states the word originates from "بُندَر" where "بار و بنه در آنجا نهند" (goods and cargo are placed there), with "اسکله" as its equivalent.

2. **Alternative Origin**: It notes this word "بهمین صورت معرب شده" (is borrowed in this form), with plural "بنادر," comparing it to the Turkish "اسکله" meaning "معبر بحر" (sea passage).

The دهخدا entry thus presents both a compositional reading (بند + در, suggesting a binding/stopping place) and acknowledges the term as a borrowed lexical item adapted into Persian.
```


## [2026-09-05T20:14:34.495Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 بندر\"; grep -n \"بندر\" BQT_v1_pages.txt | head -10\necho \"=== BQT v2 دوک\"; grep -n \"دوک\\|دوك\" BQT_v2_pages.txt | head -10"
}
```


### [2026-09-05T20:14:34.562Z] TOOL RESULT

```
=== BQT v1 بندر
1800:صحیفه ایست که برچپارده بزر گواد نازل‌شده و آنرا در بندر بمیثی چاپ
9396:بندر اسکندربه از شبه جزبرمای تشکیل شده , شامل جزبر* عمدژ فاری 118۲09 که
14186:| فك ر؟ » بروزن بندر » بسعثی در باشد
18683:نم شهری است از ولامت تی کستان . گوبندرویاء
21008:تلم » پاراوه خود این بندرا ست ۴ ۰ ثانی ورایع و زای قظمحار , جوال‌دوزرا گوشد,
21029:بسمتی جامگاه و مقام » مسل تجارت و معأملات پالکی و دستگاه ؛ شاه بندر بمعتی و کیل‌النجار
21030:است و علاطین عثمانی شاه بندر را بغنسول های خود در خارجه اطلاق کرده‌اند. هراثرةاامعارف
21033:اط «بندرو غ» خوانده‌اند. وندورغ مر کب‌است از؛: ند - ور غ(ه. م) «رهشدا» «شی.رو دکی.
24463:مدتی‌در جزایر خلیج فارس دست اندازی کرده برجزیر# هرمز و بندر کمبرون تسلط باقتند و شاه
=== BQT v2 دوک
620:                                                                                                ‫اقمتللدوکشاع‬
1803:    ‫که در وقت رشتن بر دوك پیچیده شود ت‬
1950:       ‫رشتن پنبه بردوكپیچیده‌شود ‪ ۴‬؛ وبا جیم‌فارسی‬                     ‫خانه را گونند ‪ -‬و طاق ابوان را همگفته انب‬
3141:  ‫جوژه ‪۵‬و لك رخنه و شککمرفدوك‬
3212:  ‫خورند بهندوی اثارکیل خواننه و بپارسيك کوچ ی هیندوك ( کوزهندی ) خواند ‪« ».‬اوبوالا‬
4108:‫چال است وهر دوکروه بك فرسنگه» پس‌چالی‬                      ‫کووی ومفاکیرا نکیزو" د که درآن‌توان‌ابتاد‬
5155: ‫ریلکی ‪ 3۸۲30‬قرقره(نخ ») ودر نبریز‪4۲۵۵٥‬‏ ( چرخ دوك‬
6101: ‫شه بردوك پیچیده شود ‪.‬‬     ‫که در وقت رشتن‬      ‫شیند و اورا کاروانك نگیوزبند وبا چرغ وباز‬
6354:                                                          ‫وسکون هردوکاف » صدای چکیدن آب وامثال‬
7231:                                     ‫بد‬     ‫‪ +‬درهر که این دوکوهر ( اصل وهنر ) با‬
```


## [2026-09-05T20:14:41.099Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nL=5155; F=$(awk -v L=$L 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v2_pages.txt); echo \"form feeds before: $F -> leaf $F printed $((F+540))\"; awk -v n=$((F+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -50"
}
```


### [2026-09-05T20:14:42.864Z] TOOL RESULT

```
form feeds before: 89 -> leaf 89 printed 629
   ‫رده‬                                                                                                           ‫‪- ۳۱‬‬
           ‫وآنچه زان بدان ریسمان رسند ‪۷‬‬                          ‫وزن ومعنی‌چرخست باشد وآن چرخی وحوضی‬
                                                             ‫باشد که انگور درآن ریزند و بمالند تاشیرءآن‬
                                                                                                                      ‫بر ید ‪٠‬‏‬
                ‫‪۰‬‬       ‫وفلك اولخسوا‬       ‫باشد نوفا ‌‬



‫جر خی ‪ 4‬بفتح اول و سکون ثالی‬
                                                            ‫چرخ صوقفی جامه ک‪-‬نابه از‬
 ‫والث سحتالی رسیده » هرچیز که چرخ زننده‬
                                      ‫ث‬
                                                                   ‫ن‪۹‬د‪۲۳‬ناگون‪ ۳ )۱(,‬ک‬
                                                            ‫‪-‬نانه از‬                ‫‏س گ ‪۱‬‬
                                                                                         ‫چر د‬
 ‫باشد مانند کبوتر چرخي واه‌ثال آن ‪ -‬وجنی از‬                                     ‫فلك اول باشد که فلك قمر است ‪.‬‬
‫جامة نازك ابریشمی ‪ -‬و نوعی ازاطلس نفیس هم‬
                                                             ‫چر حله ‪ -‬بر وزن مرحله » نباتی‬
  ‫هست‪ -‬وهرچیز نکرهاآامتادان ربخته کرومسگر‬
                                                             ‫باشد ست و ساق بارك ‪ ,‬و عرب آنرا شکاعی‬
 ‫چرخ کرده باشند ‪ -‬و ادبخانه و صتراح را نیز‬                                                                            ‫خوانند؟‬

                                                            ‫چرخ مقو س ‪ -‬کنابه ازفلك است‬
 ‫چر ك بفتح اول و ثانی مشدد و سکون‬                                       ‫وا‬             ‫گت‬        ‫ا‬   ‫فلكالبروح‬    ‫و‬       ‫عموماً ‪-‬‬


‫دال اعبجردب»ده و جنگ را گوبند ‪ -‬و بائانی‬
                                                             ‫چ رخو ك ‪ -‬بروزن مفلوك» چوبی باشد‬
  ‫مخفف ‪ ۰‬رنگی باشد مایل بسرخی ‪٩‬‏ مخصوص‬                       ‫مخروطی که طغلان ربمان برآن بندند ونوعی‬
  ‫باسب و استر و خر الاغ ‪ -‬وبسکون اآنسیتان‬
 ‫درخانه را گویند ‪ -‬و جابی رانیز که آمتان حررا‬
                                       ‫برآنجا نهند ‪.‬‬          ‫وکون‬  ‫ولث س‬  ‫چر حه ه بفتح اول ا‬
                                                             ‫ثانی » بمعنی چرخله است » وان رستنی ولباتی‬
 ‫رده اه بروزن زرده » بمعنی رنگه‬                              ‫باشد که بعربی‌شکاعی گوبند ببب آنکه بسیار‬
‫ولون باشد عموماً‪ -‬ورنگ بسیاهی مابلر!گویند‬                    ‫است» چه هر کاه کسی را بسار‬                    ‫وساقبارىك‬          ‫مت‬


 ‫خصوصاً ‪ -‬و پوست بدن ‪ -‬و روی آدمی را نیز‬                         ‫ضعیف ولاغرمینند گوبند « کانه عود شکاعی ‪٩‬‏ ‪-‬‬
  ‫مرادسه‌یوست‬   ‫مف‬         ‫گفته‌اند چنانکه سیه‌چرده‬                                                      ‫بمعنی دورهم آمده!‬



                                                                        ‫ینم ‪ :‬کندنا کون ‪.‬‬
                    ‫تىز ازرق فام انت‬       ‫وتان‬     ‫بدالسب که صوفیان خرقة ازرق بو شنت‬                       ‫‪5‬‬

    ‫‪۳۹۱‬‬    ‫رای‬                 ‫بخت جوانت ازفاك پیر ژنده پوش‬                 ‫‏‪ O‬قبول‬
   ‫چرخه‪.‬‬   ‫‪ ۳۳ ۴‬رکه ‪:‬‬               ‫‪ ۴‬کندناگون ( برتك گندنا ) بعنی سبز رنك ‪ .‬رك ‪:‬گندناگون ‪.‬‬
   ‫_ آنرا « کردنا»(«‪.‬م‪ ).‬نیز گوبند ‪ ۵ .‬رکه‪ :‬چرخله ‪ - ۷.‬ازدساتیر «فرهنك دسانیر ‪.» ۲۶۲‬‬
 ‫ریلکی ‪ 3۸۲30‬قرقره(نخ ») ودر نبریز‪4۲۵۵٥‬‏ ( چرخ دوك‬
                                                 ‫‪ ۷‬دک‬                                                           ‫رك چ‪:‬رخ ‪.‬‬
```


## [2026-09-05T20:14:52.662Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD dok\"; grep -n \"dōk\\|d5k\\|dwk\" PHD.txt PHD_mackenzie.txt | head -10\necho \"=== HRN duk\"; grep -n -i \"^[0-9]*\\. *dük\\|dük\\b\\|duk \" HRN.txt | head -10\necho \"=== HUB duk\"; grep -n \"dük\\|duk\" HUB.txt | head -10"
}
```


### [2026-09-05T20:14:52.738Z] TOOL RESULT

```
=== PHD dok
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD_mackenzie.txt:2007: -ganag [dwk'nk l 1M dwg'ng, N dugana] double; twin.
PHD_mackenzie.txt:2008:dok [dwk I N -] spindle.
PHD_mackenzie.txt:2898:hlndiig [hndwk l I M hyndwg, N hindu] Indian.
PHD_mackenzie.txt:5552:xayiig [he)dwk ' I N xayii] saliva, spittle.
=== HRN duk
4678:/adük, yadti lesen.
16280:laadük 617.
21516:w. dündük 574.
=== HUB duk
2213:eine iran. Wzl. duk, dud (also np. ddzam — phi. docem)— 64 —
7616:= phi. Hinduk^ arm. Hndik-K Indien', Hnduk Inder Mos.
8640:= zd. paresU' (oben p. 44); hindu = pM. hinduk {hindU-
8696:Inder , pi. hinduvdn (Indien A. M. 6, 10) — phi. hindukan
8697:Phi. Ys. 56, 11, 6, arm. hnduk Inder (bei Mos. Kalank.).
```


## [2026-09-05T20:15:02.933Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN spindle\"; grep -n -i \"spindle\" SYN.txt | head -10\necho \"=== WLD Bd1 fusus/Spindel\"; grep -n \"Spindel\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:15:03.401Z] TOOL RESULT

```
=== SYN spindle
10181:5. Lith. verpti, Lett. vérpt, with sbs. Lith. varpstis ‘spool’, varpsté ‘spindle’ : Grk. pamrw ‘sew’, fr. *wer-p-, an exten- sion of IE *wer- ‘turn, bend’. Walde-P. 1.276 f.
10184:Most of the words for ‘spindle’ are erbs for ‘turn’ or ‘spin’. One £ words for ‘twig, branch d application to the stick
10185:from V' cognate with with specialize forming the ‘spindle’. ce
10186:1. Grk. aérpaxros, NG pop. adpaxzt, kt, tarku-, fr. the root in Lat. torquere ‘twist, turn’ (10.18), OHG drahsil ‘roll- er’,ete. Walde-P. 1.735. 2, Lat. fisus (> Romance words), etym. dub. Connection with fundere ‘nour’ difficult semantically. Ernout-M. 405. Walde-H. 1.574. 3, Ir. fertas ‘distaff, spindle, axle’ (cf. Laws, Gloss. s.v.), NIr. fearsad (by me- tathesis), W. gwerthyd, Br. gwerzid, ChSl., SCr. vreteno, Boh. v¥eteno, Pol. urzeciono, Russ. vereteno : Skt. vartuld-, MHG wirtel ‘spinning-ring’ fr. IE *wert-
10189:6.32 SPINDLE
10191:Erpaxtos ON eh Lett. spréslica 1phxt" Sw. spindel ChSl.  vreteno jisus OE spinel SCr. —_vreteno uso ME _ spindle Boh. vieleno fuseau NE spindle Pol. wrzeciono puso Du. spil Russ. vereteno fus OHG  spinnila, spilla Skt. tarku- fertas MHG  spinnel, spindel fearsad NHG  spindel
10194:OE spinel, ME, NE spindle, Du. spil, spinnila, spilla, MHG spinnel, spindel, spillee NHG (> S8w.) spindel : Goth. spinnan, etc. ‘spin’ (6.31). NED s.v. spindle.
10196:Lett. spréslica ‘spindle’ beside préslica ‘distaff’ (cf. sprest beside prest ‘spin’), fr. Slavic, Pol. przeslica, Russ. prjaslica, etc. ‘distaff’, fr. the root in ChSl. prestz, etc. ‘spin’ (6.31). Mithl.-Endz. 3.1018. Briickner 440.
11077:Pol. szpilka, dim. of szpila, MHG spille ‘spindle’ (6.32), but confused with MHG spenel ‘pin’ (above, 2). Briickner 554.
12119:Lith. kédé, kedé, prob. as orig. ‘spin- ning stool’, with Lett. k’eda ‘spindle’ fr, Esth. kedr ‘spindle’. Leskien, Bildung der Nom. 265. On this and kréslas, cf. esp. Buga, Kalba ir Senové 136 ff. Both words are now used for the common ‘chair’ (Senn),
=== WLD Bd1 fusus/Spindel
3086:nadel“, aksl. ada „uyy.ioTgov Widerhaken, Haken an der Spindel**, ttdica 
5051:e’rliuls „Spindel; Wickel von Heede zum Spinnen“ (das fiir *arkids stehn 
10201:(gen. Hoy ) ^urgay-Tog. Spindel, Spille“ (*clo-), ilik ds. r Liden aaO.. Bugge 
15726:Scharpie", nhd. mdartl. ivicke „der um die Spindel gewickelte Flachs“, ahd. 
17412:Axenspindel". nir. mit Umstellung firirsaid. cymr. gwerthyd „Spindel‘ £ , acorn. 
17438:drehen, bobren", vratiti ,.drehen‘‘, vratt ..Hals”, vr'taio ..Spindel”. vtoshi 
17561:Lit. verpiii , verpti „spinnen“, carpste „Spule, Spindel; Welle, um die sich 
29214:„Faden, Spindel“; 
35525:lat. fundo ..gieBen, HieBen lassen, ausschlitten" (kaum fusus „Spindel“? 
45236:dehscn ,.Flachs brechen“, dehse „Spindel“ (dies wohl aus einer mit ags.
```


## [2026-09-05T20:15:11.155Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '35515,35535p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== page markers in WLD_Bd1_pages\"; grep -n \"dhu̯es\\|dheu-s\\|dhus-\" incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-09-05T20:15:11.213Z] TOOL RESULT

```
Eber, Pferd‘, nkd. Gaul (im Bayr. .,Deekkengst schweiz. Hahn", vgl. 
ndl. gull ..Stute, die noch nicht geworfen hat“ s. Sommer IF. 31, 362 ff.) 
als „Samengie8er‘ £ (Petersson LUA. 1920, 3, 107,; niekt wahrscheinlicher 
Sommers Erklarung aaO., wo auch iiber die unannehmbare Yerknupfung 
Charpentiers KZ. 40,441 von gill mit ai. ghoia ,,Pferd". 

AY urzeler weiter ungen: 

gheud-: 

lat. fundo ..gieBen, HieBen lassen, ausschlitten" (kaum fusus „Spindel“? 
s. Verf. LEWb. 2 330), got. giatan „gieBen- , aisl. giota . (Junge) werfen ‘, 
giota augum ..einen Blick werfern , ags. yeotan ..gieBen, fiiefien, sekiitten, 
werfen 1 -, afr. iilta, as. giolan , ahd. gioszan ds., nisi, gjota .,Hohle, enge 
Gasse", asekw. glut a ,.Gutiform‘ ; (weiteres aus nord. Mundarten bei Falk- 
Torp 363, Wessen L T UA. 1914, 39 , ahd. giozo ..flieBendes AYasser", ags. gyte 
„Guli, FluB, Flut \ ahd. gas .,fusio , yuzen „libare“, ndd. goto ,,niedrige 
AYasserstraBe ! , norw. gota „eingeschnittene Rinne, rinnenformiger Einscbnitt 
in der Landsckaft‘‘, as. gota „canalis", koll. goot ,.Gosse, Rinne £ ', nhd. 
Gossc, ags. yattas, innudas ,.receptaeula viscerum •, engl. gut ,.Darm £ . 

=== page markers in WLD_Bd1_pages
78953:                                          dheues-, dbues- dheus-, dhus-                                           843
79024:dheues-, dhues-, dheus-, dhus- „stieben, stiiuben, wirbeln (nebeln, regnen,
79061:Schulze Qu. ep. 313 Anm. 5, Ehrlich KZ. 39, 571) aus *dhus-id, wie Dina
79063:sicher aus *dhus-{a wegen -dvordSeg' Bay.%ai Hes. und 'dvotila „von den
79205:hunden werden, wiirde aber dann fur dies *dhus- die Bed. „Busch“ als
```


## [2026-09-05T20:15:19.218Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=78953 && NR<=79320' incoming/WLD/WLD_Bd1_pages.txt | grep -n \"fusus\\|Spindel\\|npers\\|duk\\|dük\" | head -10\necho \"=== WP I 564 region\"; grep -n \"^ *564 *$\\|  564$\" incoming/WLD/WLD_Bd1_pages.txt | head -3"
}
```


### [2026-09-05T20:15:21.314Z] TOOL RESULT

```
=== WP I 564 region
```


## [2026-09-05T20:15:28.576Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"DHWER\\|dhwer\\|DHUER\" incoming/ARY/ARY_latin_index_pages.txt incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY دروازه\"; grep -n \"دروازه\" incoming/ARY/ARY_pages.txt | head -6"
}
```


### [2026-09-05T20:15:28.631Z] TOOL RESULT

```
=== ARY دروازه
1096:هرگز به افتخار جاودانی نخواهم رسید. (412418 ,9 ,111۸0 آشیل به جنگ پشت دروازه‌های
7896:در دروازه / ۲۶۹
```


## [2026-09-05T20:15:31.608Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7880,7910p' incoming/ARY/ARY_pages.txt; echo \"=== pdf page\"; awk 'NR<=7896 && /\\[pdf page/ {p=$0} END{print p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T20:15:33.660Z] TOOL RESULT

```
خنی (27070/838): زرا 1 را ۳
سانسکریت (5۸(۷50777): : مر ها
17 328707 ,0۸82 ,3 133 هتقفتام ,1۵6 710قت2 ری
ارمنی (7ل072/82/14): 788۸881 ب۸ح327 برهان قاطع + ۸۳۷
یونائی (072520)+ 05070۸1 فرهنگ معین : ۱۳۹۸
لاتین (7700س): لفت‌نامه دهخدا: ۱.۳۹۵
بادداشت:
چم این و اجریشه در زبان سانسکریت : وضع» سرنوشت. َ
چم این و اجريشه در زبان لاتین : آموختن» آموزاندن,
چم این و اجریشه در زبان ایرلندی کهن : بهترین,
چم این و اجریشه در زبان آلبانی : برخورد کردن» ملاقات کردن.
چم این و اجریشه در زبان پرنانی : پذیرفت.
اوستایی (ل4287۸): 3 اد پهلری (1الم: ,0۸
پارسی باستان (۲8754۸1 صا0): 01۷۸ اوستی (0558716): 3
۹
[pdf page 268]
در دروازه / ۲۶۹
کردی (082130): 8۸۲ ,اج057 ب#(05 هلندی (0764): 3 راد
افغانی (پشت) (/4۳6[7۸/۷): اسلاوی کهن (ع۲7شا؟ تل#ناتتن طا0):
۸ بف0۸8 ,۷۸۹ اند
سانسکریت (5۸(877): 0۷98 لهستانی (۳07(3[7): رد
8مف00 ,0۷۸8 ,ناه0۷28 ,008۸5 روسی (531۸(4(#): ندید
ارمنی (۸2(48714): 0/0 چکه (280): ند دید
۱ یرنانی 0780): ق71۲7 برهمی (/807780140): 0
لانین (47770): 70۳7۸ ,۲015 ,۳0855 اسلواکی (81.0۲40): ی اد زرد
ِ فرانسه (۳2/)7): 07 لیتوانی (۵(71۵(۷ت727): 05
اسپانیایی (52۸۸]52): ای اد تونی (لتی) (7140۷ا): 20115
ایتالیایی (مللمتم: ۳07۸ ایرلندی کهن (تلدل[ صا0): 005
رومانی (26(74(7). ۳۸7۸ ولزی (۲588): ۴۵۳7۲ ,071۷5 ,00
پرتغای (۳077070183): ۳07۸ برتونی ((875670): 3 ۰
گرتبک (0077170): بال0۸ آلبانی (۸(7امقلم: ای دا
=== pdf page
[pdf page 268]
```


## [2026-09-05T20:15:40.809Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7896,7940p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T20:15:40.855Z] TOOL RESULT

```
در دروازه / ۲۶۹
کردی (082130): 8۸۲ ,اج057 ب#(05 هلندی (0764): 3 راد
افغانی (پشت) (/4۳6[7۸/۷): اسلاوی کهن (ع۲7شا؟ تل#ناتتن طا0):
۸ بف0۸8 ,۷۸۹ اند
سانسکریت (5۸(877): 0۷98 لهستانی (۳07(3[7): رد
8مف00 ,0۷۸8 ,ناه0۷28 ,008۸5 روسی (531۸(4(#): ندید
ارمنی (۸2(48714): 0/0 چکه (280): ند دید
۱ یرنانی 0780): ق71۲7 برهمی (/807780140): 0
لانین (47770): 70۳7۸ ,۲015 ,۳0855 اسلواکی (81.0۲40): ی اد زرد
ِ فرانسه (۳2/)7): 07 لیتوانی (۵(71۵(۷ت727): 05
اسپانیایی (52۸۸]52): ای اد تونی (لتی) (7140۷ا): 20115
ایتالیایی (مللمتم: ۳07۸ ایرلندی کهن (تلدل[ صا0): 005
رومانی (26(74(7). ۳۸7۸ ولزی (۲588): ۴۵۳7۲ ,071۷5 ,00
پرتغای (۳077070183): ۳07۸ برتونی ((875670): 3 ۰
گرتبک (0077170): بال0۸ آلبانی (۸(7امقلم: ای دا
ایسلندی کهن (7070۸/7۸07ف5 صام):
3رد دا پسگشت‌ها ات رد۲
ساکسونی کهن (8427۵0 ۵0): 3 8 و200
آلمانی کهن ((0820/۸ تزواتط صام: 1۵2 6 (0008) :8۸0/7
آلمانی (0870/(0): 8 ,707 0 (۳0۴78) :الق م۲2
انگلیسی کهن (دلا8(0ظ صاه): 1 (0008) دام ده ها
0080 ,208 5467 8
ی انگلیسی (8۸/037): 0008 4 (00073) :0۸70/5
* دانمارکی ‏ (للقةم0: 1 3 6 0008) 37 ۱
سوئدی (5[08275[7): ۹۵" 00 4 (0003) 1/0
نروژی (/707:5014): 0 برهان قاطع : ۸۸
[pdf page 269]
اوستایی (/4183740): 0۸30۸ ,0۸30 5 ,01170 , 121.010
پارسی پاستان (28۵407 0ا0): 0۸36۸ لیتوانی (//۸2 727 )+ 11۸0
پهلری (7ماتقهه): ۸7 ,0737 نوی (لتی) (/7۳4ا): 18
اوستی (0535776): دزد ۹ پروسی کهن (/(۲87554 صا0): 1161ب11.0۸
کردی (827577(): 0112 ولزی (للکا۴): 0۸3 مشت1۸
بلوچی (777عناتهه): ۸7 ,م08 برتونی (/۵7670): ,033801787 ,0۸1/07
افغانی (پشتر) (۸۳۵(7۵/1). 3 لدن ۱۱۳ آلبانی (1۸0(مقلم): فتاه
سانسکریت, (8(5777): 01678 هتیت (07777178): رخا ۷۱۸۱
یونانی 07280): 0۵005 2۸761 ,قمع تانت0۸
لاتین (/710ما)د 105
گوتیکه (007770): 718 پسگشت‌ها کر
انگلیسی کین (9س0/6ق هام همان |97 وم
اسلاوی کهن (۲71۴ما5 7ل#نابن) صا0), 1 (1۵(6) :2 ۸/(ماقط
061 2 (0۵76 2
لهستانی (87ل۳0): انا( 13 ۸
روسی (/175520): 00117 ۵335 :25 بل 2/07
چک (2807):. 05 :011105۸0۸5
صربی (۸07ق557): زر برهان قاطع : ۸۲۹
```


## [2026-09-05T20:15:55.049Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/thyroid",
 "prompt": "Give the etymology of 'thyroid' (Greek thyreoeides, thyreos, thyra) and also the entry for 'door' if shown."
}
```


## [2026-09-05T20:15:55.812Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://noorlib.ir/book/info/105056",
 "prompt": "What book is this? Give title, author, and whether the full text or page images are publicly readable."
}
```


### [2026-09-05T20:16:00.573Z] TOOL RESULT

```
# Etymology of "Thyroid"

The term **thyroid** originated in the 1690s from the Latinized Greek *thyreoeidēs*, meaning "shield-shaped." According to the source: "from _thyreos_ 'oblong, door-shaped shield' (from _thyra_ 'door,' from PIE root *dhwer- 'door, doorway') + _-eides_ 'form, shape'."

The anatomical reference initially described both the cartilage and gland, with the full phrase *khondros thyreoeides* referring to "shield-shaped cartilage" (the Adam's apple). The noun form meaning "thyroid gland" was recorded from 1849.

## Related to "Door"

The entry for **door** is not separately displayed on this page, but its etymology is embedded within the thyroid entry. The Greek *thyra* traces back to the Proto-Indo-European root **\*dhwer-**, which means "door, doorway."
```


### [2026-09-05T20:16:03.582Z] TOOL RESULT

```
# Book Information

**Title:** "فرهنگ واژه‌های فارسی در زبان عربی" (Dictionary of Persian Words in Arabic Language)

**Author:** Imam Shoshteri, Mohammad Ali (امام شوشتری، محمد علی)

**Publication:** Tehran, Iran; National Works Society; 1347 SH (Persian calendar)

**Accessibility:** The page indicates "مطالعه رایگان" (free reading) is available, and users can access both "نمایش تصویری" (image view) and download options. The site states it provides "دسترسی به کتابخانه‌ای با بیش از 147,000 جلد کتاب برای مطالعه، دانلود و پژوهش" (access to a library of over 147,000 volumes for study, download, and research), suggesting the full text/page images appear to be publicly accessible through this digital library platform.
```


## [2026-09-05T20:16:09.275Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 60 curl -s -L \"https://noorlib.ir/book/view/105056?pageNumber=240&viewType=text\" -H 'User-Agent: Mozilla/5.0' | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t)\nprint(html.unescape(re.sub(r'\\s+',' ',t))[:1500])\n\""
}
```


### [2026-09-05T20:16:12.391Z] TOOL RESULT

```
 فرهنگ واژه‌های فارسی در زبان عربی - بخش بخش 1 صفحه 240 فهرست کتابها | پدیدآوران | چاپ سنگی | شخصیت ها | گفتگوی هوشمند با کتاب‌ (آزمایشی - نسخه ۱) shopping_cart افزایش اعتبار ورود / عضویت ورود / عضویت فا فا فارسی ع العربية En English our websites بیشتر ... فهرست کتابها | پدیدآوران | چاپ سنگی | شخصیت ها | گفتگوی هوشمند با کتاب‌ (آزمایشی - نسخه ۱) پشتیبانی درباره ما ارتباط با ما قوانین و مقررات خدمات مراکز و موسسات صاحبان آثار وبلاگ محصولات نرم‌افزارهای ویندوزی نرم‌افزارهای اندرویدی ابزارهای اینترنتی پایگاه‌ها تندیس‌ها و افتخارات کسب نشان زرین سرآمد در ششمین جشنواره بین‌المللی رسانه‌های دیجیتال - 1391 کسب رتبه شایسته تقدیر در نخستین جشنواره کتاب مجازی - 1394 دریافت عنوان وب‌سایت برگزیده در یازدهمین جشنواره وب و موبایل ایران - 1397 کسب رتبه اول در دومین جشنواره ملی کتاب در فضای مجازی - 1398 حقوق مادی و معنوی این پایگاه متعلق به مرکز تحقیقات کامپیوتری علوم اسلامی است و نشر غیر مجاز محتوای آن پیگرد قانونی دارد.
```


## [2026-09-05T20:16:17.012Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://noorlib.ir/api/book/text/105056/240\" \"https://noorlib.ir/View/fa/Book/BookView/Text/105056/1/240\" \"https://noorlib.ir/api/v1/book/105056/page/240\"; do echo \"## $u\"; timeout 30 curl -s -o /dev/null -w \"%{http_code}\\n\" -L \"$u\" -H 'User-Agent: Mozilla/5.0'; done"
}
```


### [2026-09-05T20:16:21.281Z] TOOL RESULT

```
## https://noorlib.ir/api/book/text/105056/240
404
## https://noorlib.ir/View/fa/Book/BookView/Text/105056/1/240
404
## https://noorlib.ir/api/v1/book/105056/page/240
404
```


## [2026-09-05T20:16:23.728Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -30 tools/fetch_source.py"
}
```


### [2026-09-05T20:16:23.767Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "data", "verification", "sources", "web")
INDEX = os.path.join(WEB, "index.jsonl")
UA = "rishe-verification/1.0 (+https://github.com/sfmqrb/rishe; etymology source archiving)"


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
```


## [2026-09-05T20:16:31.593Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D9%88%DA%A9' --note 'page 136, root Dhus, node #1: Persian دوک duk < MP dwk /dōk/ spindle'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/fusus' --note 'page 136, root Dhus, node #2: Latin fusus \"spindle\" etymology unclear / non-IE substrate'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%86%D8%AF%D8%B1' --note 'page 136, root Dhwer, node #2: Persian بندر bandar, possible band+dar analysis unconfirmed; Arabic bandar borrowed from Persian'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A8' --note 'page 136, root Dhwer, nodes #3/#4: Arabic درب darb (from Gk Derbe per Wiktionary) vs Persian درب'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1' --note 'page 136, root Dhwer, node #2: Persian در dar < MP dar (ESIJa 2.500)'"
}
```


### [2026-09-05T20:16:36.741Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/07e27efcdfc6c56b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d10bcf37ddcc91e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5bd31a25265f4efc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cc05b2bfdc8e7347.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e3aa66e0ba86eb7.txt
```


## [2026-09-05T20:16:44.881Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AF%D8%B1%D8%A8/' --note 'page 136, root Dhwer, node #4: Mo in درب [ع.] \"در بزرگ، دروازهٔ شهر یا قلعه، ج دروب\"; Dehkhoda quotes Jawaliqi al-Mu arrab'\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AA%DB%8C%D8%B1%D9%88%D8%A6%DB%8C%D8%AF/' --note 'page 136, root Dhwer, node #10: Mo in تیروئید [فر.] = from French'\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D9%86%D8%AF%D8%B1/' --note 'page 136, root Dhwer, node #2: Mo in/Dehkhoda on بندر'\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/forest' --note 'page 136, root Dhwer, node #13: forest < ML forestis silva < L foris; foreign < OF forain'\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/thyroid' --note 'page 136, root Dhwer, node #8/#11: thyroid < Gk thyreoeides \"shield-shaped\" < thyreos < thyra'"
}
```


### [2026-09-05T20:16:52.629Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/70daa0f4022b5d93.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8cbe86dbb292730b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3dfc9d7374b4a1d9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d9c138b1629ae3e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/714c5dbcb7823a51.txt
```


## [2026-09-05T20:16:58.486Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 70daa0f4022b5d93 8cbe86dbb292730b 3dfc9d7374b4a1d9 6d9c138b1629ae3e 714c5dbcb7823a51; do echo \"#### $f\"; wc -c $f.txt; grep -o \"دروب\\|فر\\.\\|forestem\\|thyreoeides\\|بنادر\" $f.txt | sort -u | head -5; done"
}
```


### [2026-09-05T20:17:00.464Z] TOOL RESULT

```
#### 70daa0f4022b5d93
12779 70daa0f4022b5d93.txt
دروب
#### 8cbe86dbb292730b
6951 8cbe86dbb292730b.txt
فر.
#### 3dfc9d7374b4a1d9
17548 3dfc9d7374b4a1d9.txt
بنادر
#### 6d9c138b1629ae3e
7475 6d9c138b1629ae3e.txt
forestem
#### 714c5dbcb7823a51
6383 714c5dbcb7823a51.txt
thyreoeides
```


## [2026-09-05T20:17:05.715Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0wer-' --note 'page 136, root Dhwer: PIE *dʰwer- \"door\" reconstruction page'\npython3 tools/fetch_source.py 'https://www.ahdictionary.com/word/indoeurop.html' --note 'page 136: AHD/Watkins IE roots appendix front page (dhwer- entry consulted in the 1985 local text)'\ngrep -o \"dʰwer\\|dʰwṓr\\|door\" data/verification/sources/web/*.txt 2>/dev/null | tail -3"
}
```


### [2026-09-05T20:17:08.137Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/665fe5986736a8e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3735d75498a331a4.txt
data/verification/sources/web/f312f6f8d2bfa948.txt:door
data/verification/sources/web/fb963b4b7d56245c.txt:door
data/verification/sources/web/ff229b9e7713bf5e.txt:door
```


## [2026-09-05T20:17:10.857Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -c 1200 data/verification/sources/web/665fe5986736a8e0.txt | tr '\\n' ' ' ; echo; echo \"==== AHD\"; head -c 400 data/verification/sources/web/3735d75498a331a4.txt"
}
```


### [2026-09-05T20:17:10.902Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0wer- FETCHED: 2026-09-05T20:17:08Z STATUS: 200 TITLE: Reconstruction:Proto-Indo-European/dʰwer- - Wiktionary, the free dictionary  Reconstruction:Proto-Indo-European/dʰwer- - Wiktionary, the free dictionary    Jump to content    Main menu    Main menu   move to sidebar   hide    Navigation   Main page   Community portal   Requested entries   Recent changes   Random entry   Help   Glossary   Contact us   Special pages    Search    Search    Appearance    Donations    Create account    Log in    Personal tools    Donations    Create account    Log in    Contents   move to sidebar   hide    Beginning   1   Proto-Indo-European    Toggle Proto-Indo-European subsection    1.1   Root    1.1.1   Derived terms    1.2   References    Toggle the table of contents    Reconstruction:Proto-Indo-European/ dʰwer-    Add languages    Reconstruction    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Get shortened URL    Print/export 
==== AHD
URL: https://www.ahdictionary.com/word/indoeurop.html
FETCHED: 2026-09-04T19:47:47Z
STATUS: 200
TITLE: Appendix I - Indo-European Roots

Appendix I - Indo-European Roots 

 HOW TO USE THE DICTIONARY
 To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of us
```


## [2026-09-05T20:17:14.859Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -o \"Root.\\{0,600\\}\" data/verification/sources/web/665fe5986736a8e0.txt | sed -n '3,5p'; echo \"---\"; python3 - <<'EOF'\nt=open('data/verification/sources/web/665fe5986736a8e0.txt').read()\ni=t.find('Root')\nj=t.find('Derived terms')\nprint(t[t.find('Proto-Indo-European',3000):][:100])\nk=t.rfind('Root')\nprint(t[k-2000:k+800][-1500:])\nEOF"
}
```


### [2026-09-05T20:17:17.155Z] TOOL RESULT

```
---
Proto-Indo-European/dʰwer-&oldid=92171368 "

 Categories : Proto-Indo-European lemmas 
 Proto-Indo-E
```


## [2026-09-05T20:17:19.842Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nt=open('data/verification/sources/web/665fe5986736a8e0.txt').read()\ni=t.find('Proto-Indo-European[edit')\nprint(t[3000:6500])\nEOF"
}
```


### [2026-09-05T20:17:21.660Z] TOOL RESULT

```
y, Julius ( 1959 ), “ dhu̯ē̆r-, dhu̯ō̆r-, dhur-, dhur̥- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, pages 278-279 

 ^ Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), “*dhu̯ṓr”, in Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn Publishers, pages 168-169 

 ^ Wodtko, Dagmar S.; Irslinger, Britta; Schneider, Carolin ( 2008 ), “ *dʰu̯ór-, *dʰur- ”, in Nomina im indogermanischen Lexikon [ Nouns in the Indo-European Lexicon ]‎ [1] (in German), Heidelberg: Universitätsverlag Winter, pages 130-135 

 ^ Kloekhorst, Alwin ( 2008 ), “andurza”, in Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 5), Leiden, Boston: Brill, →ISBN , page 226 

 ^ Derksen, Rick ( 2008 ), “*dvьrь”, in Etymological Dictionary of the Slavic Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 4), Leiden; Boston: Brill, →ISBN , page 128 

 ^ Derksen, Rick ( 2015 ), “durys”, in Etymological Dictionary of the Baltic Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 13 ), Leiden, Boston: Brill, →ISBN , page 147 

 ^ Martirosyan, Hrach ( 2010 ), “duṙn”, in Etymological Dictionary of the Armenian Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 8), Leiden and Boston: Brill, pages 243-244 

 ^ Kroonen, Guus ( 2013 ), “*dura-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [2] , Leiden, Boston: Brill , →ISBN , page 110 

 ^ Kroonen, Guus ( 2013 ), “*durī-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [3] , Leiden, Boston: Brill , →ISBN , page 110 

 ↑ 10.0 10.1 Beekes, Robert S. P. ( 2010 ), “ θύρα ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), volume I, with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , pages 565-566 

 ^ De Vaan, Michiel ( 2008 ), “ foris ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 233 

 ^ Derksen, Rick ( 2015 ), “dvaras”, in Etymological Dictionary of the Baltic Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 13 ), Leiden, Boston: Brill, →ISBN , pages 148-149 

 ^ Derksen, Rick ( 2008 ), “*dvòrъ”, in Etymological Dictionary of the Slavic Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 4), Leiden; Boston: Brill, →ISBN , page 128 

 ↑ 14.0 14.1 Matasović, Ranko ( 2009 ), “*dworā, *duro-, *dworestu-”, in Etymological Dictionary of Proto-Celtic (Leiden Indo-European Etymological Dictionary Series; 9), Leiden: Brill , →ISBN , pages 111-112 

 ^ De Vaan, Michiel ( 2008 ), “ forum ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 237 

 ^ Adams, Douglas Q. ( 2013 ), “twere*”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , pages 344-345 

 ^ Orel, Vladimir ( 1998 ), “ derë ”, in Albanian Etymological Dictionary , Leiden; Boston; Cologne: Brill, →ISBN , page 60 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/dʰw
```


## [2026-09-05T20:17:31.813Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Tor,  Hof\\|'Tor, Hof'\\|Tor.  Hof\" BRT.txt | head -5; echo \"---\"; grep -n \"dvara-\\|duvarayä\\|dvarэm\" BRT.txt | head -8"
}
```


### [2026-09-05T20:17:31.904Z] TOOL RESULT

```
---
12845:1)  "halten,  festhalten,  zurückhalten':  yS vS  x^ayqs  adqs  drJtä  (Opt.)>>  ayantsm urvatsii  (sd.)  .  .  Y.  4^.  5 ;  —  ys  mqm (näml.  Aaomsm)  aiwishubm  därayehi  ya%a tsyüm  Y. //.  3;  —  vupe  haoma  . .  yaiäi qsaAu  dtritänks  Y.  10.  17;  —  ya%a v»krk5  vaysi  (sd.)  taile  *dramnB^1  hart- ääe  Vtf««'«  (sd.)  V.  73. 8;  —  IfravartÜ .  .  duvarayämaiy  bastir  adariy  Bh.a.  13; 15;  —  s.  noch  Inf.  därtys  und  dSra- yap.  a)  mit  Abi.  'zurUck-,  ab-,  fern- halten von  — ':  ke  paeiryS  .  .  ährB  tafmii därayat  tanaoi  haca  mafyehe  V,  20.  i ; I.  q)  mit  abL  Inf.  'halten,  wehren, dass  nicht  — ';  kasnil  dgrtta  samiä  . .  ava- pastsii  (sd.)    V.  44.  4.  b)    mit   Dat
13975:•  j-,  g.  'dvar-  V.  'gehen',  uzw.  von ifoA^chen  Wesen".  Praes.  2  dvara-, 4  äväru:
16703:—  D  hauv  basta^  anayatä  abty  mäm  Bh. /.  17;  —  duvarayämaiy  basta*  adäriy Bh.  2.  13,  14;  1  —  %wqmäi  "drvfimca *banadämi''^  .  .  niyne  .  .  nUbanm  Vt  4. 5.  z)  Med.  'sich  etwas  an-,  um-,  fest- binden': upairi  pusqm  (sd.)  bandayata YL5.  is8.  3)  'zusammenbinden,  an einander  befestigen':  *hqm.ivqmca  (sd.) smqmea    simSt^rqmca    dargta    huktnta
29472:naisim  vamavätaiy  duruxlam  (Sp.  767  m.)  mainySui  dSmqn  yat  ir/(APn.)  , .  anaä-ä- *maniyitaiy  Bh.  4. 8;  —  äh^ind' ..  *a>ia-  maide  Vt.  12. 4.  «)  Der  Begriff  auf  den ya/ä  abiy  mim  adamsim  avajaimm  Bh.  j  sich  h'  zurUckbezieht,  ist  zuvor  nicht  ge- /.  17;  ^-gaumäiam  .  .  kärJ' Hm . . atarsd'inxaoX,  aber  aus  der  Sachlage  eikenntlicb: EL  /.  13;  —  aniyaf'  apiyä  *äkyata  api- ,  mt^rfm  . .  yd  dai^hSus  rqxsyqihyi  para litn^''  paräbari^  Bh.  i.  19;  —  rtäV-  rausta  baraili  .  .  avar»%i  hls  (APm., taxmam  agariayi^ .  ■  duvarayätnaiy  basti/'  1  näml.  regionis  incolas)  fl/iwKCtCSp.  140710.) adilriy  haruvt^sim  kär^  avaifia*  pasä-  Ytio.i-j;  —  »oÄT/*^»'Sa  . .  jfl/{Sp.  1581  u.) va''iiin  arbairäyä  uzmayapatiy  akutMvam  yaia    Alm  (ASn,   'es')*'   ädar?    mafyäka
```


## [2026-09-05T20:17:39.676Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"dvar»m\\|dvarәm\\|dvarim\\|dvara  n\\|dvar-  n\\.\" BRT.txt | head -6; echo \"=== try 'Tor'\"; grep -n \"'Tor'\\|,Tor'\\|„Tor\" BRT.txt | head -8"
}
```


### [2026-09-05T20:17:39.733Z] TOOL RESULT

```
3553:höchste,  höchstgelegene,  höchststehende':  •  j.  apayant-  AdJT  PPA.:  s.  ap-. upa  dvar»m  xsaiireMtiym{sA.) 'mstn  karj-\    j_    apayantama*    Adj,    'maxime    pro- Aaifl  "..dem  höchstgelegenen  in Ä:"yLj.  pellendus':   'maieca  a»rahe  mainysus  \\, 54.         a)  mit  alahe  und  aiät  'der  höchste  21.  i.
23246:•  j.,  g.  vazdvar-  n.  'Beständigkeit';  a)  sva. 'Ausdauer':  tanvS  vlspayh  drvatätsm  lanvs vUpayh  °pffl«  Yt  14.29;  —  tanvS'vars.. tamis  vpr?%rfm  Y.6S.11.  b)  sva.  'un- unterbrochene Dauer':  disyJt  ahmai  naire avat  müdsm  . .  'var)  vakistakt  aithSus V.J. 44;  —  ma*dä  dadat  ahurS  hauniats atmrttätas^a . .  asahyäcä  . .  xia%rahy3  sarO vatfhSul  'varV^  manatahö  yS  .  .  "MAk. wird  . .  die  besändige  Gemeinschaft''  mit If.  und  Am.  und  mit  Asa,  mit  Xf.,  mit VM,  dem  gewähren,  der  .  ."  Y._;r.  21.
=== try 'Tor'
```


## [2026-09-05T20:17:51.971Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg136_300.png data/verification/sources/refs/ocr/BOOK/136.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T20:17:53.710Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r-- 1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:19:27.942Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM page for الدرب\"; awk 'NR<=1560{if(/\\[pdf page/)p=$0} END{print p}' AFM_pages.txt; grep -c \"\\[pdf page\" AFM_pages.txt; sed -n '1555,1565p' AFM_pages.txt\necho \"=== POK end of dhwer Tuer entry\"; sed -n '4007,4012p' POK_01.txt\necho \"=== LAT foris\"; grep -n \"^foris\\|foris, adv\\|fores, -ium\" LAT.txt | head -5"
}
```


### [2026-09-05T20:19:29.691Z] TOOL RESULT

```
=== AFM page for الدرب

0
( الد يدب والد يدبان» الرقيب والطليعة مركب من ديد اي نظ ومن بان اي
صاحب
+ ( الدوّدم والدوادم ) ܟ كالدم رج من السر اومن ܝ الغرز 93
من دود 3 ܝܗ ومن دم اي نشس :
# ( | ܝܢ ) باب السكّة الواسع وقيل هو المضيق في ܥ ܐ .ܙ ܐܬܘܢ الأخير
ܩܡ 05 الدرب تعر برب در ند بجذف شطره الاخير وهو 23
١‏ الدربان») 6 ܐ من در اي باب ومن بان اي حافظ
(الدر بنك غلق الدكان فارسي حض .ومعناة المضنيق: والوادي ܙ ]ܝ )ܢ
والباب المشبك وهو مركب من در ܼܦ باب ومن بند اي رباط وسد ٠‏ ومن در ند
بالتركية والكردبة
(الدر بين والدّرَابرُون ) قواغ مصفوفة تمل من خشب او حديد تحاط بها
=== POK end of dhwer Tuer entry
toch.   B  tivere  ,Türe*.
WP.  I  870  f.,  WH.  I  529  f.,  Trautmann  63,  EM  377  f.,  Schwyzer  Gr. Gr.  I  625 ^
dhuergh'  :  drugh-  ,zwerghaft,  verkrüppelt'?
Bartholomae  IF.  12,  131  Anm.  verbindet  av.  drva-  (d.  i.  driiyva-)^  das unter  anderen  Benennungen  körperlicher  Gebrechen  aufgezählt  ist  und vielleicht  , zwerghaft,  verkrüppelt'  bedeutet,  mit  anord.  dvergr,  ags.  dweorg, engl,  dioarfj  mnd.  dwerch,  nnd.  dwarf,  ahd.  twerCj  mhd.  twerc,  -ges,  nhd. Zwerg,  wozu  tiefstufig  *diirgi  in  anord,  dyrgja  , Zwergin',  ndd.  dorf]  nach Krogmann  (KZ.  62,  143)  dazu  lett.  drugt  ,zusammensiiiken'  (s.  oben 1.  dhreugh-).
Für  das  germ.  Wort  käme  andernfalls  die  Deutung  als  , Trugwesen'  in Betracht,  zu  ai.  dhvards-  ,eine  Art  weiblicher  Dämonen',  Wz.  dhuer-  , durch Täuschung  zu  Fall  bringen';  es  wäre  von  dhuer-  dann  mit  demselben  -gh abgeleitet,  das  auch  in  der  WutzqM.  dhreu-gh-  begegnet  {dhuer-gh- :  dhurgh- : dhrugh-y  dhreugh-)]  auch  letzterer  entstammen  Bezeichnungen  für  kobold- artige Trugwesen.
WP.  I  871  f.
=== LAT foris
833:foris. Mais les formes avec de sont plus frdquentes; v. de.
58012:foris est animus, sin foris sum, animus domist "si je suis a la
```


## [2026-09-05T20:19:44.042Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 870 dhuer Tuer\"; grep -n \"dhuer-, dhuor-\\|dhu̯er\\|dhuer-, dhur-\" incoming/WLD/WLD_Bd1_pages.txt | head -5\necho \"=== find Tuer entry\"; grep -n \"„Tür\\|,,Tür\\|Tür“\" incoming/WLD/WLD_Bd1_pages.txt | head -8"
}
```


### [2026-09-05T20:19:44.106Z] TOOL RESULT

```
=== WLD Bd1 870 dhuer Tuer
81256:dhuer-, dhuor-, dhur-, dhur- ,,Tfir“: neben diesem kons. St., der ursprgl.
81539: wird hingegen *dhreu auf idg. *dhuer-, dhur-               —
=== find Tuer entry
```


## [2026-09-05T20:19:45.194Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT fores\"; grep -n \"fores, -ium\\|fores,-ium\\|^fores\" LAT.txt | head -5; grep -n \"foras\" LAT.txt | head -5"
}
```


### [2026-09-05T20:19:45.253Z] TOOL RESULT

```
=== LAT fores
182:fores ivoquent l'habitation du chef, non une construction
23434:fores
23474:fores, cf. Thes. IV 1057,70; aais foris est la graphie courante et
832:(classique); 28 abinde, 39 abintro, 30 abintus, gib. ab ultra, a foras, a
17197:dare foras scripta comme edere librum (Cic., Att.13,33,3); haec ubi
23450:foras: v. fores.
23495:foras (accus.pl.) "dehors, au dehors" (sans louTeaent et ayec nou“
23497:4 poque, d' o 4 d foras, 5 foris-, .ie foras, de foris-, eaploy^s aussi
```


## [2026-09-05T20:19:49.141Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23434,23445p' LAT.txt; echo \"...\"; sed -n '23490,23520p' LAT.txt\necho \"=== WLD page\"; awk 'NR<=81256 && /^ *8[67][0-9] *$|  8[67][0-9]$/{p=$0;n=NR} END{print n\": \"p}' incoming/WLD/WLD_Bd1_pages.txt; sed -n '81250,81262p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-05T20:19:50.797Z] TOOL RESULT

```
fores
praefatio", praefatiuncula - , praefatus,-us, -men (tardifs).
profor : synonyae archalque et po^tique de proloqui", a aussi le
sens de praedicere. A l* 4 poque imperiale apparait profatus, -us "parole,
prononciation".
Le grec a nn pr^sent correspondant i fatur y k savoir dor.cpap,!,,
ion.-att. . Le proterit hoa.cfxxxo a dea d^sinences aoyennes com¬
ae lat./atwr. La racine se retrouve, en outre, dans v.angl.boian "se
vanter", y.r.baju "je raconte", basni "recit", arm. 6oy "dit-il", 6on
"discours" et bay "parole" (cf. gr. cpcxxiC., cpoujic). Une valeur religiense
apparait notaaaent dans v. sl. ba l ij i "sorcier" (d'o{i "m^decin"). Le
sens de "raconter" et "enoncer, declarer" domine dans la racine.
...
foricula f. (rare), foricularius (inscr.). Pas d'autres derives: pour
designer le "portier" Plaute dit ianitor, Varron, ostiarius, et on
lit dans la Vulgate portarius . Pour forensis, v. forum.
Compos^: biforis (-rus Vitr.), sans doute calque de 8 t, 9 upoC.
A un doublet *fora se rattachent les adverbes foris (abl.loc.pl.),
foras (accus.pl.) "dehors, au dehors" (sans louTeaent et ayec nou“
vernent) attestes dfes les plus anciens textes, et renforces a basse
4 poque, d' o 4 d foras, 5 foris-, .ie foras, de foris-, eaploy^s aussi
dans la 1 . vulgaire coaae pri^positions, e.g. Apul. Apol. 50 foras corporis
(avec le g^nitif d'aprfes gr. ef;<jo), Met. 1,31 foris urbem, ou iis ont
concurrenc^ extra', cf. foras murdneus (d'aprbs intra-, Greg. Tur. ). Foris
s'oppose a intus, de la forinsecus fora 4 sur intrin-, extrin-secus.
Cf, aussi forum, forus, affores (oculi) Orib.
Foris, fores, "porte" n'est pas repr^sente dans les 1 . roaanes,
ou ont surv 4 cu dstium et porta’, mais les adverbes foras, foris y sont
bien attestes, M.L.3431, de aeae que a et de foras, foris (esp. afuera,
ital. affuori, fr. dehors, etc., M.L.365), les derivas de labasse 4 poque:
foranus (-neus) " 4 tranger", M.L.3438-9, forasticus 3433; forestis
(Diploa. de Childebert.Mon.Gera.Dipl.iap. I n.5, p.7,43)» cf. fr. foret.
Cf. F. Brall, Lat. foris, foras ia Gallo-roaanischen, bes. ia Franzosischen,
Breslau, 1918.
Le thbae *dhwer- "porte" 3'employait essentielleaent au pluriel,
ainsi qu'on le voit par v.sl.dvtri, lit. diirys (g^n.pl. duru), v.b.a.
turi (et v.angl.durw, de dhur-ns, acc.pl.) et skr. dvdrah (avec- d,
par suite d'une alteration secondaire), acc. durhh. Le latin a g 4 n£ralis 4
le vocalisae *dhwor- du noainatif pluriel. Le singulier n'apparait
que secondaireaent, ainsi dans -r.al,dviri, lat./orts ou ara. dufn (pass£
aux theaes en -n-).
Le d 4 riv 4 en -o- a le vocalisae radical zero: hoa. 9 l)pCU (et post£~
rieurement un sg. 9 upa), gall. dor, arm.durk' (pluriel, avec valeur de
singulier; gen.abi. dat. drof). Lat./oros doit son vocalisae 4 fores.
=== WLD page
81155:                               dhueg    dhuer-                                  869


dt.    Zwerg (: ai. dhvards- „Damon“), da eher aus                                                 idg. *dhuergh-       ,zwerg-
haft, verkruppelt"                 (s. d.).    —     S. *dhrewjh- „trfigen“.


dhuer-, dhuor-, dhur-, dhur- ,,Tfir“: neben diesem kons. St., der ursprgl.
    ein Plurale und Duale tantum war (s. u.), stehn zum Teil wohl schon
    ursprachliche -o- und -«-Erweiterungen teils mit zu vermutender kol-
    lektiver Bed., teils (als Neutrum) in der Stellung als 2. Zsglieder.
   Ai.       Kom.        pi.   dvarah, Acc.           pi.          durcili ,       durah   ,
                                                                                               Yom. du. dvara(it             „Tiir“
(Verlust der Aspiration               den W.-Kasus nach v. Fierlinger KZ.
```


## [2026-09-05T20:20:00.281Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"δβr\\|dbr\\b\" HENNING_selected_papers.txt | head -5; echo \"=== GMS?\"; ls | grep -i \"gms\\|sogd\""
}
```


### [2026-09-05T20:20:00.340Z] TOOL RESULT

```
=== GMS?
```


## [2026-09-05T20:20:36.370Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:22:23.637Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build136.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 136,\n \"book_page\": 106,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": []\n}\n\n# ---------------- entry 1: Dhus ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Dhŭs\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Mann's *dhus- (1) 'whirr, buzz; whirring object, spindle' (IEC 224); no such root in Pokorny, Walde-Pokorny or Watkins/AHD\",\n \"note\": \"Nourai copies Mann faithfully: An Indo-European Comparative Dictionary p. 224 heads exactly 'dhus- (1) “whirr, buzz; whirring object, spindle”. Cf. WP I, 564 & 844' and lists under it 'Per. dük (“spindle”. For -k cf. Per. xūk “pig”, fr. *sūs); Gk. cf. thus-thia “Bacchanalian rods”; Lat. fūsus “spindle”; MHG cƒ. tūsen “rush, roar, ring”; Sw. düs “carousal”'. So the root box, its language label and its gloss reproduce a real (if idiosyncratic) reference. The reservation is that this root is Mann's alone. Walde-Pokorny I 843-846 does have a root 'dheues-, dhues-, dheus-, dhus- „stieben, stäuben, wirbeln“' (= Pokorny 268-271), but neither WP nor Pokorny nor Watkins lists any spindle word under it, and the two words Nourai hangs on it are exactly the two whose etymology the standard handbooks call unknown (Latin fūsus) or unstated (Persian dūk). Mann habitually creates such semantically narrow roots by abstracting from two or three isolated words; treat the box as a hypothesis, not an established PIE root.\",\n \"note_fa\": \"ریشهٔ «Dhŭs» ساختهٔ مان (S. E. Mann) است: در «فرهنگ تطبیقی هندواروپایی» ص ۲۲۴ سرواژهٔ dhus- (1) با همین معنای «وزوز کردن؛ چیز چرخان، دوک» آمده و همان‌جا «فارسی dūk» و «لاتین fūsus» ذیل آن ثبت شده است؛ پس نقلِ نورایی از مأخذش درست است. اما این ریشه در فرهنگ‌های معیار (پوکورنی، والده‑پوکورنی، واتکینز/AHD) وجود ندارد؛ آنچه هست ریشهٔ *dʰeus-/*dʰus- «گرد و خاک برخاستن، چرخیدن» (والده‑پوکورنی ج۱ ص۸۴۳ـ۸۴۶) است که هیچ واژه‌ای به معنای «دوک» زیر آن نیامده. بنابراین جعبهٔ ریشه با احتیاط پذیرفتنی است: نقل از مان درست، ولی خودِ ریشه فرضیهٔ شخصی مان است نه ریشه‌ای پذیرفته‌شده.\",\n \"sources\": [W + \"fusus\", W + \"%D8%AF%D9%88%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:224\", \"status\": \"supports\",\n    \"note\": \"IEC.txt line 3339, immediately after the page marker '224' (line 3338): 'dhus- (1) ‘whirr, buzz; whirring object, spindle’. Cf. WP I, 564 & 844. See following entries — Per. dük (‘spindle’. For -k cf. Per. xūk ‘pig’, fr. *sūs); Gk. cf. thus-thia, n. pl. ‘Bacchanalian rods’; Lat. fūsus ‘spindle’ …'. Root, gloss and both daughter words are Nourai's chart exactly.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 843-846 (WLD_Bd1_pages.txt lines 78953 ff., running head 'dheues-, dhues- dheus-, dhus- 843')\", \"stance\": \"silent\",\n    \"note\": \"the root Mann refers to as 'WP I 844' is 'dheues-, dhues-, dheus-, dhus- „stieben, stäuben, wirbeln (nebeln, regnen …)“'; grepping the whole section for 'Spindel', 'fusus', 'npers' or 'dük' returns nothing — Walde-Pokorny attaches neither the spindle words nor any Persian word to it.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 268-271 (dheu-s-) and 447-448 (ǵheu-)\", \"stance\": \"contradicts\",\n    \"note\": \"Pokorny has no 'whirring object, spindle' root; and at p.448, under the extension gheud-, he writes 'lat. fundō, -ere, fūdī, fūsum „gieße, lasse fließen, schütte aus“ (über fūsus „Spindel“ s. WH. I 474)' — i.e. he deliberately keeps the spindle word out of the etymology.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, dh- list (AHD_watkins1985.txt lines 390-400)\", \"stance\": \"silent\",\n    \"note\": \"the appendix runs dhugh(ə)ter- → dhino- → dhwen- → dhwenə- → dhwer-; there is no dheus-/dhus- root of any kind, and no English word is traced to one.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §6.32 'SPINDLE' (SYN.txt lines 10184-10191)\", \"stance\": \"contradicts\",\n    \"note\": \"'Most of the words for “spindle” are from verbs for “turn” or “spin” … 2. Lat. fūsus (> Romance words), etym. dub. Connection with fundere “pour” difficult semantically. Ernout-M. 405. Walde-H. 1.574.' Buck's table for 'spindle' contains no Iranian column and no *dhus- root.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Persian\",\n \"words\": \"dūk\",\n \"verdict\": \"plausible\",\n \"derivation\": \"New Persian دوک dūk 'spindle' is the regular continuation of Middle Persian dōk, written dwk' in Book Pahlavi and glossed 'spindle' by MacKenzie (Concise Pahlavi Dictionary p. 27: 'dōk [dwk' | N ~] spindle'); Wiktionary derives the Persian word from exactly that Middle Persian form. Middle Persian ō regularly gives New Persian ū (majhūl wāw > maʿrūf in classical NP, cf. MP rōz > NP rūz), so dōk > dūk is unproblematic. What is not established is the step drawn in the chart, root → Persian: no Old or Middle Iranian ancestor beyond MP dōk is attested, and neither Horn nor Hübschmann nor Aryanpur has an entry for the word. Mann's phonetic argument for the -k ('for -k cf. Per. xūk “pig”, fr. *sūs') is weak: xūk goes back to Old Iranian *hū-ka- with the productive suffix *-ka-, so the -k is a suffix, not a reflex of the root-final consonant — which means dūk would have to be *dū-ka-, an unattested stem. Verdict: the Persian word and its Middle Persian ancestor are real and correctly glossed; only the PIE affiliation is Mann's conjecture.\",\n \"derivation_fa\": \"«دوک» فارسی نو دنبالهٔ منظمِ فارسی میانهٔ dōk (نوشتهٔ پهلوی dwk′) است که مکنزی در «فرهنگ کوچک پهلوی» ص ۲۷ آن را «spindle/دوک» معنی کرده؛ ویکی‌واژه نیز فارسی «دوک» را از همین صورتِ پهلوی می‌گیرد. اوی مجهولِ فارسی میانه در فارسی دری به اوی معروف بدل شده (مانند rōz > rūz)، پس dōk > dūk دگرگونیِ آواییِ عادی است. آنچه اثبات‌نشده مانده پیوند این واژه با ریشهٔ هندواروپاییِ *dʰus- است: نه صورتی ایرانی باستان از آن به‌جا مانده و نه هرن و هوبشمان و آریان‌پور مدخلی برایش دارند. استدلالِ مان دربارهٔ ـک پایانی (قیاس با «خوک» از *sūs) هم سست است، زیرا کافِ «خوک» پسوندِ *-ka- ایرانی باستان است نه بازماندهٔ صامتِ ریشه. پس: خودِ واژه و صورتِ پهلویِ آن درست است، ولی ریشه‌شناسیِ هندواروپاییِ نورایی (به نقل از مان) تنها یک حدس است.\",\n \"sources\": [W + \"%D8%AF%D9%88%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:224\", \"status\": \"supports\",\n    \"note\": \"IEC.txt line 3339 s.v. dhus- (1): 'Per. dük (‘spindle’. For -k cf. Per. xūk ‘pig’, fr. *sūs)' — word, gloss and the derivation from the root are Mann's, exactly as drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 27 (PHD.txt line 312; PHD_mackenzie.txt line 2008)\", \"stance\": \"supports\",\n    \"note\": \"'dōk [dwk' | N ~] spindle' — the Middle Persian ancestor of NP dūk, which the chart skips.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie, whole text\", \"stance\": \"silent\",\n    \"note\": \"greps for 'dük', 'duk' and 'Spindel' in HRN.txt return only unrelated hits (yadūk 617, dündük 574); Horn has no article on the spindle word, i.e. he offers no Iranian etymology for it.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (ARY_pages.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for دوک / دوك across the OCR returns nothing: Aryanpur, who includes only Persian words with a known IE root, does not treat dūk — consistent with the root being Mann's private reconstruction.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §6.32 'SPINDLE' table (SYN.txt line 10191)\", \"stance\": \"silent\",\n    \"note\": \"the comparative table for 'spindle' lists Greek, Latin, Romance, Germanic, Balto-Slavic, Sanskrit tarku- and Irish fertas, but no Iranian form at all.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Latin\",\n \"words\": \"fūsus\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Latin fūsus, -ī m. 'spindle' (whence It. fuso, Sp. huso, Fr. fuseau) is real and correctly glossed, but no modern authority derives it from anything. Ernout-Meillet, Dictionnaire étymologique de la langue latine p. 470, s.v. fūsus: 'fuseau; employé surtout au pl. Attesté depuis Catulle, mais sans doute ancien. – Panroman … Étymologie inconnue.' Buck §6.32 says the same and adds that the obvious link with fundere is unusable: 'Lat. fūsus (> Romance words), etym. dub. Connection with fundere “pour” difficult semantically'; Wiktionary calls the origin 'unclear, possibly from a non-Indo-European substrate'. Mann's assignment to *dhus- founders on Latin phonology as well: PIE *dh- gives Latin f- only word-initially before a vowel, which is fine, but there is no trace of the *-s- of the root in a form whose -s- is intervocalic (*dhus-o- should give **fūror-/**fūr-, by rhotacism, not fūsus). The chart's own NOTE is also inaccurate: Pokorny p.448 does not derive the spindle from ǵheu- 'to pour'. Under the extension gheud- he writes 'lat. fundō, -ere, fūdī, fūsum „gieße …“ (über fūsus „Spindel“ s. WH. I 474)' — the fūsum on that page is the perfect participle of fundō, and Pokorny expressly refers the homophonous noun fūsus 'spindle' away to Walde-Hofmann; Walde-Pokorny I (s.v. gheud-) is even blunter: 'kaum fusus „Spindel“?'. So modern scholarship rejects both Nourai's derivation and the alternative he reports.\",\n \"derivation_fa\": \"لاتینِ fūsus «دوک» واژه‌ای واقعی است، اما ریشه‌شناسیِ پذیرفته‌ای ندارد: ارنو و مِیه در «فرهنگ ریشه‌شناختی زبان لاتین» ص ۴۷۰ صریحاً می‌نویسند «Étymologie inconnue» (ریشه ناشناخته)، باک در بخش ۶٫۳۲ آن را «مشکوک» می‌خواند و می‌افزاید پیوندش با fundere «ریختن» از نظر معنایی دشوار است، و ویکی‌واژه احتمال وام از زیرلایه‌ای غیرهندواروپایی را مطرح می‌کند. فرضِ مان (و به تبع او نورایی) از نظر آواییِ لاتین هم لنگ می‌زند، چون سینِ میان‌واکه‌ایِ *dhus-o- در لاتین باید به ر بدل می‌شد (قانون rhotacism) و **furus می‌داد نه fūsus. یادداشتِ خودِ نمودار هم نادرست است: پوکورنی در ص ۴۴۸ نه fūsus «دوک» بلکه fūsum (اسم مفعولِ fundō) را از ریشهٔ *ǵheu- «ریختن» می‌گیرد و دربارهٔ «دوک» می‌نویسد «برای fūsus به معنی Spindel نگاه کنید به Walde‑Hofmann ج۱ ص۴۷۴»؛ والده‑پوکورنی نیز می‌نویسد «به‌سختی fusus „Spindel“». پس پژوهش امروزی هر دو ریشه‌شناسی را رد می‌کند.\",\n \"sources\": [W + \"fusus\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:224\", \"status\": \"supports\",\n    \"note\": \"IEC.txt line 3339: 'Lat. fūsus ‘spindle’' does stand under Mann's dhus- (1) — Nourai's arrow is a faithful copy of his source, even though the source is a minority view.\"},\n   {\"ref\": \"POK:448\", \"status\": \"contradicts\",\n    \"note\": \"cited by Nourai in the node's NOTE. POK_02.txt lines 1568 ff. (page markers 447 at line 1558, 448 mid-entry): 'gheu- „gießen“ … Wurzelerweiterungen: gheud-: lat. fundō, -ere, fūdī, fūsum „gieße, lasse fließen, schütte aus“ (über fūsus „Spindel“ s. WH. I 474)'. Pokorny derives the participle fūsum, not the noun fūsus 'spindle', which he explicitly sets aside.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 470 s.v. fūsus (LAT.txt line 25184 ff.)\", \"stance\": \"contradicts\",\n    \"note\": \"'fusus, -i m. (et plus tard fusum n.): fuseau; employé surtout au pl. Attesté depuis Catulle, mais sans doute ancien. – Panroman, M.L. 3609 … Étymologie inconnue.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §6.32 (SYN.txt line 10186)\", \"stance\": \"contradicts\",\n    \"note\": \"'2. Lat. fūsus (> Romance words), etym. dub. Connection with fundere “pour” difficult semantically. Ernout-M. 405. Walde-H. 1.574.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I s.v. gheud- (WLD_Bd1 djvu line 35525)\", \"stance\": \"contradicts\",\n    \"note\": \"'lat. fundo „gießen, fließen lassen, ausschütten“ (kaum fusus „Spindel“? s. Verf. LEWb.² 330)' — Walde-Pokorny itself doubts the connection Nourai's note ascribes to Pokorny.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde, Lat. etym. Wörterbuch, 2nd ed. 1910 (LEW_1910.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'fusus', 'fūsus' and 'Spindel' in the local 1910 OCR returns nothing usable; the page Pokorny refers to (WH I 474) belongs to the 3rd ed. (1938-56), which is not on disk.\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\njson.dump(doc, io.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part1.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(doc[\"entries\"][0][\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build136.py"
}
```


### [2026-09-05T20:22:25.413Z] TOOL RESULT

```
ok 2
```


## [2026-09-05T20:28:57.945Z] TOOL CALL #86: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build136b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\nSC='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\ndoc = json.load(io.open(SC+'part1.json', encoding='utf-8'))\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = W + \"Reconstruction:Proto-Indo-European/d%CA%B0wer-\"\nETY_F = \"https://www.etymonline.com/word/forest\"\nETY_T = \"https://www.etymonline.com/word/thyroid\"\nAB = \"https://abadis.ir/fatofa/\"\n\ne2 = {\n \"entry\": 2,\n \"root\": \"Dhwer, Dhrugh, Dhwor\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *dʰwer- / *dʰwor- / *dʰur- 'door, doorway' (usually plural) — Pokorny IEW 278-279\",\n \"note\": \"The root itself, its language label and its gloss are exactly right. Pokorny IEW 278 (the very page Nourai cites; POK_01.txt line 3993, immediately after the page marker '278') heads 'dhu̯ē̆r-, dhu̯ō̆r-, dhur-, dhur̥- „Tür“', and Watkins/AHD has 'dhwer-. Door, doorway (usually in plural). Originally an apophonic noun *dhwor-, *dhur- … [Pok. dhu̯ér- 278.]'; Wiktionary's *dʰwer- page cites Pokorny 278-279, Mallory-Adams (EIEC 168 f. *dhu̯ṓr), NIL 130-135, Kroonen, de Vaan and Beekes for the same reconstruction. The defect is the middle name of the box: 'Dhrugh' does not belong to the door root. *dhrugh- is the zero grade of *dhreugh- 'to deceive' (Pokorny 276; POK_01 line 4011 sets out the series dhuer-gh- : dhurgh- : dhrugh- : dhreugh- under the homonymous root dhu̯er- 'durch Täuschung zu Fall bringen', IEW 277) — which Nourai himself heads as a SEPARATE root on the preceding page (pdf 135, 'Dhreugh : to deceive', refs POK:276) with Av. draoga-, OP duruj- and NP دروغ under it. So the same author files *dhrugh- twice, once correctly and once here. The slip is his own and deliberate enough to have generated the index redirect 'Dhrugh → Dhwer' on p. 105 of the book; its likely origin is Kent's lexicon, where duruj- 'lie, deceive' with 'pIE *dhrugh-' stands on the same opening (pp. 191-192) as duvara- 'door'. I rendered the printed page (pdf 136, saved as data/verification/sources/refs/ocr/BOOK/136.png) and the book does print 'Dhwer, Dhrugh, Dhwor : door' — the extraction is faithful; the error is the book's. No node on the page actually descends from *dhrugh-, so nothing else in the chart is affected.\",\n \"note_fa\": \"خودِ ریشه و برچسبِ زبان و معنای آن درست است: پوکورنی در همان صفحه‌ای که نورایی ارجاع می‌دهد (ص ۲۷۸) سرواژهٔ «dhu̯ē̆r-, dhu̯ō̆r-, dhur-, dhur̥- „Tür/در“» را آورده و واتکینز نیز ذیل dhwer- «در، درگاه (بیشتر به صورت جمع)» همین را با ارجاع به پوکورنی ۲۷۸ ثبت کرده است. اشکال در نامِ میانیِ جعبه است: *dhrugh- به این ریشه ربطی ندارد، بلکه صورتِ صفرِ ریشهٔ *dhreugh- «فریفتن» است (پوکورنی ۲۷۶) — همان ریشه‌ای که خودِ نورایی در صفحهٔ پیشین (۱۰۵) جداگانه با نامِ Dhreugh و با واژه‌های اوستاییِ draoga-، پارسی باستانِ duruj و «دروغ» فارسی آورده است. سرچشمهٔ این لغزش احتمالاً فرهنگِ کِنت است که در همان دو صفحهٔ ۱۹۱ـ۱۹۲ هم duruj- «دروغ گفتن» با ریشهٔ *dhrugh- و هم duvara- «در» را آورده. تصویرِ صفحهٔ چاپی را دیدم: کتاب واقعاً «Dhwer, Dhrugh, Dhwor : door» چاپ کرده، پس خطا از خوانشِ اسکن نیست، خطای خودِ کتاب است. چون هیچ گرهی روی این صفحه از *dhrugh- گرفته نشده، بقیهٔ نمودار آسیب نمی‌بیند.\",\n \"sources\": [PIE, \"https://www.ahdictionary.com/word/indoeurop.html\"],\n \"ref_check\": [\n  {\"ref\": \"POK:278\", \"status\": \"supports\",\n   \"note\": \"POK_01.txt line 3993, directly under the page number '278' (line 3991): 'dhu̯ēr-, dhuor-, dhur-, dhur̥- „Tür“: neben diesem kons. St., der ursprüngl. ein Plurale und Duale tantum war …'; the entry runs to p. 279 and closes 'WP. I 870 f., WH. I 529 f., Trautmann 63, EM 377 f., Schwyzer Gr. Gr. I 625'. It contains, in order, the Avestan/Old Persian, Greek, Latin and Germanic forms of the chart.\"},\n  {\"ref\": \"KNT:191\", \"status\": \"partial\",\n   \"note\": \"Kent's article is one page later: KNT.txt has the running head '192 OLD PERSIAN' just before 'duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. θύρα, Lt. forēs, NEng. door, Lith. dvāras “courtyard”, pIE *dhuor- dhur- and its extended forms *dhworo- etc.' (line 5568), while p. 191 (marker at line 5556) carries duruj- 'lie, deceive … pIE *dhrugh-' and duruva-. The page cited is thus off by one for 'door' — but it is exactly the page that carries *dhrugh-, which is probably how that form got into the root box.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I 869-870 (WLD_Bd1_pages.txt line 81256, running head 'dhueg dhuer- 869')\", \"stance\": \"supports\",\n   \"note\": \"'dhuer-, dhuor-, dhur-, dhur̥- „Tür“: neben diesem kons. St., der ursprgl. ein Plurale und Duale tantum war …' — the fuller entry that Pokorny 278 abridges; the immediately preceding paragraph assigns Zwerg/*dhuergh- to the other root, 'S. *dhreugh- „trügen“'.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, AHD_watkins1985.txt lines 396-399\", \"stance\": \"supports\",\n   \"note\": \"'dhwer-. Door, doorway (usually in plural). Originally an apophonic noun *dhwor-, *dhur-, in the plural, designating the entrance to the enclosure (*dhwor-o-) surrounding the house proper. 1. Zero-grade form *dhur- … in Germanic *durunz … 2./3. Suffixed o-grade forms *dhwor-n̥s / *dhwor-ois in Latin forās / foris … 5. Zero-grade *dhur- in Greek thura … 6. Persian dar, door, gate: DURBAR. [Pok. dhu̯ér- 278.]' — Watkins even has the Persian branch.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt lines 3418 and 3357 ff.\", \"stance\": \"supports\",\n   \"note\": \"Mann has 'dhuoros “entrance, court”. WP I, 871. Cf. dhuer-, dhur- — Lat. (ambig.) forus …; OCS dvorŭ “court, yard”; Li. dváras' and '(dhuriə, a zero-formula to dhuer-, dhuor-, dhur- “door” etc.) WP I, 870 — Gk. thairós “hinge of door”'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur p. 269-270, s.v. «در، دروازه» (ARY_pages.txt line 7896, [pdf page 268-269])\", \"stance\": \"supports\",\n   \"note\": \"the entry lists Avestan DVAR, Old Persian DUVARA, Pahlavi DAR, Ossetic, Kurdish, Pashto, Sanskrit DVĀR/DVĀRA, Armenian DURN, Greek, Latin FORIS/FORAS/FORES, Gothic DAUR, Old Irish DORUS, Welsh DOR, Lithuanian DURYS, Slavic and Albanian DERË — the same family the chart draws — and cites برهان قاطع ۸۲۸, the very Borhan page Nourai uses.\"}\n ],\n \"nodes\": []\n}\nN = e2[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"dvar, duvara\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both citation forms are correct. Avestan dvar- (consonant stem, acc. sg. dvarəm, loc. dvarə) means 'gate, court; mountain pass' — Bartholomae, Altiranisches Wörterbuch 766, and the phrase quoted throughout the AIW, 'upa dvarəm xšaθrō.sukəm apanōtəməm', 'at the pass Xšaθrō.suka, the highest-lying one' (Yt. 5.54, BRT.txt lines 3553, 9048, 10770). Old Persian duvara- 'door, gate, court' is attested in the locative-with-postposed-ā duvarayā, e.g. DB 2.75 duvarayā-maiy basta adāriya 'he was held bound at my court/gate' (Kent, Old Persian p. 192 and §191.I); the same stem gives duvarθi- 'portico, colonnade' < *dvara-varθi- by haplology (Kent §129). Phonetically both continue PIE *dʰwer-/*dʰwor-: Old Persian regularly breaks the initial cluster with an anaptyctic u (dv- > duv-, cf. duvitīya- 'second' beside Av. bitya-), while Avestan keeps dv-; Indo-Iranian *dhw- lost its aspiration early in the weak cases (Skt. nom. pl. dvā́raḥ beside acc. pl. duráḥ), which is why Sanskrit shows d- and not dh-.\",\n \"derivation_fa\": \"هر دو صورتِ نقل‌شده درست است. در اوستا dvar- (ستاکِ صامتی، رایی dvarəm، دری dvarə) به معنی «در، دروازه، حیاط؛ گذرگاهِ کوهستانی» است — بارتولمه، «فرهنگ ایرانی باستان» ستون ۷۶۶، با شاهدِ مکررِ «upa dvarəm xšaθrō.sukəm» «بر گذرگاهِ خْشَثْروسوکَ» (یشت ۵٫۵۴). در پارسی باستان duvara- «در، بارگاه» در صورتِ دریِ duvarayā آمده، چنان‌که در بیستون ۲٫۷۵ «duvarayā-maiy basta adāriya» «او را بسته بر درگاهِ من نگاه داشتند» (کِنت، ص ۱۹۲). از نظر آوایی هر دو دنبالهٔ *dʰwer-/*dʰwor- هندواروپایی‌اند: در پارسی باستان خوشهٔ آغازینِ dv- با واکهٔ میانجیِ u شکسته شده (duv-، مانند duvitīya-)، حال آنکه اوستایی dv- را نگه داشته است. ادعای نورایی در این گره کاملاً درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"BQT:828\", \"status\": \"supports\",\n   \"note\": \"BQT_v2_pages.txt leaf 288 (= printed p. 828, offset printed = leaf + 540), headword «در», Mo'in's footnote 4: «پارسی باستان duvara (در، باب). اوستا dvar-. پهلوی dar … هندی باستان dvār, dvāra، ارمنی durn (باب، در) … بارتولمه ۷۶۶ … اسشق ۵۴۵» (اسشق = اساس اشتقاق, i.e. Horn's Grundriss no. 545). Exactly the arrow drawn.\"},\n  {\"ref\": \"KNT:191\", \"status\": \"partial\",\n   \"note\": \"the duvara- article is on Kent p. 192, not 191 (KNT.txt line 5568, after the running head '192 OLD PERSIAN'): 'duvara- sb. “door”: Av. dvar-, Skt. dhvar-, Gk. θύρα, Lt. forēs, NEng. door … pIE *dhuor- dhur-'; p. 191 does however carry the grammar cross-reference §191.I under which duvarayā is listed.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 766 (quoted phrases in BRT.txt lines 3553, 9048, 10770)\", \"stance\": \"supports\",\n   \"note\": \"'upa dvarəm xšaθrō.sukəm (sd.) … “bei dem Pass Xš., dem höchstgelegenen in Kaŋha”, Yt. 5.54' — Av. dvar- acc. sg. dvarəm, and Kent and Mo'in both cite AIW 766 for it.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p. 192 and §§34, 129, 152.IV\", \"stance\": \"supports\",\n   \"note\": \"'duvara- sb. “door” … pIE *dhuor- dhur- and its extended forms *dhworo- etc.; see also duvarθi-. duvarayā-maiy lsn. (§186) DB 2.75; 89f.' and 'duvarθim from *dvar-varθim “door-cover” = “colonnade”' (§129 haplology).\"},\n  {\"src\": \"POK\", \"where\": \"IEW 278 (POK_01.txt line 3994)\", \"stance\": \"supports\",\n   \"note\": \"'av. Akk. Sg. dvarəm, Lok. dvarə „Tor, Hof“, apers. duvarayā „am Tore“' — the two chart forms, with their cases and glosses.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur p. 269-270\", \"stance\": \"supports\",\n   \"note\": \"AVESTAN: DVAR; OLD PERSIAN: DUVARA; PAHLAVI: DAR — listed for the headword «در، دروازه».\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"dar; darband; bandar\",\n \"verdict\": \"plausible\",\n \"derivation\": \"dar «در» is confirmed: Old Iranian *dwar- > Middle Persian dar (Book Pahlavi ideogram BBA < Aramaic bb', phonetic dl; MacKenzie 1971 p. 25 'dar [BBA; dl | M dr, N =] door; palace; chapter, subject') > NP dar; Horn, Grundriss §545 gives precisely 'der “Tür”; … ap. duvar- “Tür”, duvarayā; aw. dvar-; phlv. dar, dargas; ai. dvār-, durās; arm. durn' and adds the dialect forms (kurd. bar/der, oss. dvar, waχ. bār, šiγn. div/divēr). Wiktionary derives NP در from MP dar citing ESIJa II 500. The two words in the chart's parenthesis belong here too: darvāza «دروازه» 'city gate' (dar + -vāza, Horn §545) and darbān «دربان» 'doorkeeper' (dar + bān 'keeper'; Lokotsch no. 490 'Pers. dārbān “Türhüter” [von pers. dar “Tür” Horn NpEt S. 120, Nr. 545 und -bān]', whence Anglo-Indian durwaun and Rum./Ger. Trabant). darband «دربند» is likewise sound: dar + band 'bar, barrier' (√band, PIE *bhendh-, which is where the chart's ☞Bhendhe points), attested already in Middle Persian — MacKenzie p. 25 'darband [BBA bnd | N ~] gate' — and the name of the Caspian pass-city Darband/Derbent; Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, calls الدربند 'pure Persian … compounded of در i.e. door and بند i.e. bond and barrier'. bandar «بندر» 'seaport' is the weak link: Mo'in gives it no origin tag at all, Dehkhoda offers only a popular gloss ('where they set down goods and gear'), and Wiktionary's Persian entry marks the etymology as missing, noting that an analysis band + dar 'makes phonetic and semantic sense, but is there literature to confirm this?'. The alternative usually met with — band 'dam, dyke, mole' plus a suffix — is equally unproven. Arabic بندر / pl. بنادر (which the chart's parenthesis gives) is certainly borrowed from Persian, so the direction of that arrow is right; only the internal analysis is unsupported. Hence 'plausible' for the node as a whole.\",\n \"derivation_fa\": \"«در» بی‌گمان درست است: ایرانی باستان *dwar- > فارسی میانه dar (هزوارشِ BBA، آوانگاشتِ dl؛ مکنزی ص ۲۵: «dar … در؛ کاخ؛ باب و فصل») > فارسی نو «در». هرن در بندِ ۵۴۵ «اساس اشتقاق» دقیقاً همین را می‌آورد و صورت‌های گویشی (کردی bar/der، اُستی dvar، وخی bār، شغنی div/divēr) را می‌افزاید؛ ویکی‌واژه هم فارسیِ «در» را از پهلویِ dar می‌گیرد (به استنادِ فرهنگ ریشه‌شناختی زبان‌های ایرانی ج۲ ص۵۰۰). دو واژهٔ داخلِ کمانک هم درست‌اند: «دروازه» (در + ـوازه) و «دربان» (در + بان)، که لوکوچ (شمارهٔ ۴۹۰) آن را از «در» هرن ۵۴۵ می‌گیرد. «دربند» نیز استوار است: در + بند (از ریشهٔ *bhendh- که ارجاعِ ☞Bhendhe به آن است)؛ در فارسی میانه darband «دروازه» ثبت شده و ادّی شیر آن را «فارسیِ محض، مرکب از در یعنی باب و بند یعنی رباط و سد» می‌داند. حلقهٔ سست «بندر» است: معین هیچ نشانِ ریشه‌ای برای آن نمی‌گذارد، دهخدا تنها توضیحی عامیانه دارد و ویکی‌واژه تحلیلِ «بند + در» را از نظر آوایی و معنایی ممکن ولی بی‌پشتوانهٔ منبع می‌شمارد. بنابراین گره روی‌هم «با احتیاط پذیرفتنی» است.\",\n \"sources\": [W + \"%D8%AF%D8%B1\", W + \"%D8%A8%D9%86%D8%AF%D8%B1\", AB + \"%D8%A8%D9%86%D8%AF%D8%B1/\"],\n \"ref_check\": [\n  {\"ref\": \"BQT\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qateʿ ed. Mo'in, printed p. 828 (BQT_v2_pages.txt leaf 288), headword «در»: «بفتح اول، درِ خانه و سرای و امثال آن باشد و بعربی باب گویند»، with footnote 4 giving OP duvara, Av. dvar-, Pahl. dar and referring to Bartholomae 766 and Horn 545 — the Persian node's ancestry exactly.\"},\n  {\"ref\": \"FVF:98,240\", \"status\": \"not_checked\",\n   \"note\": \"FVF = Emam Shushtari, Farhang-e Vāzheha-ye Fārsi dar Zabān-e ʿArabi (Tehran 1347). Only copy located is noorlib.ir/book/info/105056, whose page viewer (…/book/view/105056?pageNumber=240) serves its text through JavaScript; plain fetches of the page and of three guessed API endpoints returned only the site chrome or 404. No other scan found.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 545, p. 120 (HRN.txt line 4873)\", \"stance\": \"supports\",\n   \"note\": \"'545. der “Tür”; … vergl. derbar, derbān, derwāze. … ap. duvar- “Tür”, duvarayā; aw. dvar-; phlv. dar, dargas; ai. dvār-, durās; arm. durn “Tür”' — covers dar, darbān and darvāza in one article.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 25 (PHD.txt line 308)\", \"stance\": \"supports\",\n   \"note\": \"'dar [BBA < A bb'; dl | M dr, N =] door; palace; chapter, subject' and, three entries on, 'darband [BBA bnd | N ~] gate', 'dargāh [dlg'h | N ~] doorway' — both the simplex and the compound are already Middle Persian.\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch nos. 490-491 (LKT.txt lines 1290 ff.)\", \"stance\": \"supports\",\n   \"note\": \"'490. Pers. dārbān “Türhüter” [von pers. dar “Tür” Horn NpEt S. 120, Nr. 545 und -bān “Herr, hütend”] … hieraus angloind. durwaun … rum. dorobanț, dtsch. Trabant'; '491. Pers. dārbār … hieraus angloind. engl. durbar'.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in s.v. بندر (via abadis.ir/fatofa/بندر, archived)\", \"stance\": \"silent\",\n   \"note\": \"«(بَ دَ) (اِ.) محلی است در ساحل دریا یا رودخانه که محل توقف و بارگیری است» — definition only, no origin tag and no band+dar analysis; Dehkhoda on the same page offers only the popular reading «بار و بنه در آنجا نهند».\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur p. 269-270 s.v. «در، دروازه»\", \"stance\": \"supports\",\n   \"note\": \"treats در and دروازه as one IE-inherited entry with the Avestan/OP/Pahlavi chain, and cites برهان قاطع ۸۲۸ for it.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Arabic\", \"words\": \"darb\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Arabic دَرْب darb 'narrow road, mountain pass; gate of a quarter' (pl. durūb) is not from the Arabic root d-r-b 'to train, accustom', and the Arab lexicographers themselves said so: Dehkhoda quotes al-Jawālīqī's al-Muʿarrab to the effect that darb is not originally Arabic and that the Arabs applied it to the narrow passes into Byzantine territory, which served as 'gates'. Nourai's specific source-tradition is Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, who says outright «الدرب تعریب درب(ند) بحذف شطره الأخیر» ('al-darb is the arabicised darband with its last part dropped') and, on the same page, «الدربان … من در ای باب ومن بان ای حافظ» and «الدربند … فارسیٌّ محض … مرکب من در ای باب ومن بند ای رباط وسدّ» — i.e. exactly the Persian → Arabic arrow drawn here. Modern scholarship is divided: Wiktionary derives Arabic دَرْب instead from Ancient Greek Δέρβη, the town in Lycaonia at the Cilician Gates (whence the plural al-durūb for the Taurus passes), with Syriac darbā 'way' and Old Spanish adarve as further offshoots; Lokotsch no. 488 lists 'Ar. darb “Weg, enger Weg”' as the source of Sp./Pg. adarve without assigning it any Persian origin. Since the Persian-origin view is that of the Arabic lexicographers and of the Persianist tradition Nourai follows, while the Greek-toponym view is the one now printed in Wiktionary, the node is best rated plausible rather than confirmed.\",\n \"derivation_fa\": \"«دَرْب» عربی به معنی «راهِ تنگ، گذرگاهِ کوهستانی، دروازهٔ محله» (جمع: دروب) از ریشهٔ عربیِ د-ر-ب «آموختن/عادت دادن» نیست، و خودِ لغویانِ عرب هم آن را عربیِ اصیل نمی‌دانستند: دهخدا از «المعرَّب» جوالیقی نقل می‌کند که این واژه اصلِ عربی ندارد و عرب آن را بر تنگه‌های مرزیِ روم که حکمِ دروازه داشتند اطلاق کرده است. سرچشمهٔ سخنِ نورایی سنّتِ ادّی شیر است که می‌نویسد «الدرب تعریبُ درب(ند) بحذف شطره الأخیر» و در همان صفحه «الدربند … فارسیٌّ محض، مرکب من در ای باب و من بند ای رباط و سدّ» — یعنی دقیقاً همان پیکانی که در نمودار کشیده شده. اما پژوهشِ امروزی یکدست نیست: ویکی‌واژه دَرْبِ عربی را وام از نامِ شهرِ یونانیِ Δέρβη در کنارِ «دروازه‌های کیلیکیه» می‌داند و لوکوچ (شمارهٔ ۴۸۸) هم آن را بی‌هیچ اشاره‌ای به فارسی، عربی می‌گیرد. پس این گره «با احتیاط پذیرفتنی» است نه قطعی.\",\n \"sources\": [W + \"%D8%AF%D8%B1%D8%A8\", AB + \"%D8%AF%D8%B1%D8%A8/\"],\n \"ref_check\": [\n  {\"ref\": \"FVF:240\", \"status\": \"not_checked\",\n   \"note\": \"Emam Shushtari's Farhang-e Vāzheha-ye Fārsi dar Zabān-e ʿArabi is on noorlib only behind a JavaScript page viewer (see node #2); p. 240 could not be read. Its claim is, however, the standard one of that genre and is independently attested in Addi Shir (see 'consulted').\"}\n ],\n \"consulted\": [\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, س.v. الدرب / الدربان / الدربند (AFM_pages.txt lines 1559-1563 = AFM.txt lines 2525-2529)\", \"stance\": \"supports\",\n   \"note\": \"«الدرب تعریب درب(ند) بحذف شطره الاخیر»؛ «الدربان … من در ای باب ومن بان ای حافظ»؛ «الدربند … فارسی محض ومعناه المضیق والوادی … وهو مرکب من در ای باب ومن بند ای رباط وسد».\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 488 (LKT.txt line 1273)\", \"stance\": \"partial\",\n   \"note\": \"'488. Ar. darb: “Weg, enger Weg”; hieraus mit ar. Art. sp. adarve “der Mauerkranz” …' — Lokotsch takes the word as Arabic and traces only its onward path into Ibero-Romance, without endorsing (or denying) a Persian source.\"},\n  {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (FVQ.txt)\", \"stance\": \"silent\",\n   \"note\": \"grep for 'darb' returns nothing: the word is not Qur'anic, so Jeffery has no article on it.\"},\n  {\"src\": \"DOZ\", \"where\": \"Dozy, Supplément / Glossaire (DOZ.txt)\", \"stance\": \"silent\",\n   \"note\": \"grep for 'darb' in the local text returns no headword.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"darb\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian درب darb 'door, large gate' is indeed the Arabic word taken back into Persian — the round trip the chart draws (Persian dar → Arabic darb → Persian darb). Mo'in's entry, the reference Nourai cites, tags it Arabic and gives the Arabic plural: «(دَ رْ) [ع.] (اِ.) درِ بزرگ، دروازهٔ شهر یا قلعه. ج. دروب.» ('[Arabic] (n.) a large door, the gate of a city or citadel; pl. durūb'). The tell-tale of the round trip is exactly that plural: a native Persian در could not form دروب. In modern usage darb is a formal/administrative synonym of dar (درب ورودی etc.) and is often criticised by Persian purists for that reason. A minority alternative exists: Wiktionary's Persian entry derives درب instead from Middle Persian darbās 'palace' (MacKenzie p. 25 'darbās [dlp's] palace'), citing ESIJa II 502 — that would make the word inherited rather than re-borrowed; but Mo'in, Dehkhoda and the Arabising tradition all treat it as the Arabic form, which is what the chart says.\",\n \"derivation_fa\": \"«درب» فارسی همان واژهٔ عربی است که دوباره به فارسی بازگشته — یعنی همان چرخهٔ «در ← عربیِ دَرْب ← درب» که در نمودار کشیده شده. معین، همان مأخذی که نورایی به آن ارجاع می‌دهد، آن را با نشانِ [ع.] می‌آورد: «(دَ رْ) [ع.] (اِ.) درِ بزرگ، دروازهٔ شهر یا قلعه. ج. دروب». نشانهٔ روشنِ این رفت‌وبرگشت همان جمعِ مکسّرِ «دروب» است که برای واژهٔ فارسیِ «در» ممکن نیست. (ویکی‌واژه صورتی دیگر پیشنهاد می‌کند و «درب» را از فارسی میانهٔ darbās «کاخ» می‌گیرد ـ به استنادِ فرهنگ ریشه‌شناختی زبان‌های ایرانی ج۲ ص۵۰۲ ـ ولی معین و دهخدا و سنّتِ معرّبات همان رأیِ نمودار را دارند.) ادعای نورایی درست است.\",\n \"sources\": [AB + \"%D8%AF%D8%B1%D8%A8/\", W + \"%D8%AF%D8%B1%D8%A8\"],\n \"ref_check\": [\n  {\"ref\": \"MON:1503\", \"status\": \"partial\",\n   \"note\": \"the entry text is confirmed verbatim from Mo'in via abadis.ir (archived): «(دَ رْ) [ ع . ] (اِ. ) درِ بزرگ ، دروازة شهر یا قلعه . ج . دروب .» — an Arabic-tagged word meaning exactly 'door/gate', as the arrow requires. The page number itself cannot be verified: the 6-volume Amir Kabir Farhang-e Fārsi is not online in any scan (see refs_online.json notes for MON), and the 2-volume Adena condensation on disk has no درب article.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"Mo'in s.v. درب, via abadis.ir/fatofa/درب (archived)\", \"stance\": \"supports\",\n   \"note\": \"«[ع.] (اِ.) درِ بزرگ، دروازة شهر یا قلعه. ج. دروب.»\"},\n  {\"src\": \"BQT\", \"where\": \"Dehkhoda's article on درب quoted on the same page (archived)\", \"stance\": \"supports\",\n   \"note\": \"Dehkhoda cites al-Jawālīqī's al-Muʿarrab that درب is not Arabic in origin and was used by the Arabs of the narrow frontier passes 'which are like gates' — the same round-trip picture.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 25 (PHD.txt line 308)\", \"stance\": \"partial\",\n   \"note\": \"'darbās [dlp's] palace' — the Middle Persian word from which Wiktionary (ESIJa II 502) derives NP درب, i.e. the competing, non-Arabic account of the same form.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Sogdian\", \"words\": \"dbr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The Sogdian word is δβr, read δβar, 'door, gate' — Gharib's Sogdian Dictionary entry no. 3500, which stands on printed page 138, exactly the page Nourai cites. Gharib gives it in Buddhist, Manichaean and Christian Sogdian with a full case paradigm (nom. -y, acc. -w, abl. -h, loc. -y', pl. -t', obl. pl. -ty) and states its origin as '<Av. duvara', i.e. the same Old Iranian *dwar- that gives Av. dvar- and OP duvara-. Phonetically the node is regular: Old Iranian *dw- becomes Sogdian δβ- (the Manichaean and Christian scripts write db/δβ), and the unstressed final vowel is lost, so *dwara- > δβar. The chart's transliteration 'dbr' is the Sogdian consonantal spelling as Gharib himself prints it in the alternative script column. The only quibble is the arrow's origin: Sogdian δβar continues Proto-Iranian *dwar- directly, not the Avestan/Old Persian form drawn as its parent (the chart hangs it under node #1, which is a convenience of the tree).\",\n \"derivation_fa\": \"واژهٔ سغدی δβr (خوانشِ δβar) «در، دروازه» است؛ در «فرهنگ سغدی» بدرالزمان قریب مدخلِ شمارهٔ ۳۵۰۰ در صفحهٔ ۱۳۸ — درست همان صفحه‌ای که نورایی ارجاع داده — با صرفِ کاملِ حالت‌ها (نهادی y-، رایی w-، ازی h-، دری y'-، جمع t'-) آمده و خودِ قریب اصلِ آن را «<Av. duvara» نوشته است. دگرگونیِ آوایی قاعده‌مند است: خوشهٔ *dw- ایرانی باستان در سغدی به δβ- بدل می‌شود و واکهٔ پایانیِ بی‌تکیه می‌افتد، پس *dwara- > δβar. تنها نکتهٔ کوچک آنکه سغدی مستقیماً دنبالهٔ ایرانی باستان است، نه فرزندِ صورتِ اوستایی/پارسی باستان که در نمودار پدرِ آن نشان داده شده. ادعای نورایی و ارجاعِ صفحه‌اش هر دو درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"SOD:138\", \"status\": \"supports\",\n   \"note\": \"SOD_pages.txt, the \\\\f-block whose running number is 138 (the next block opens '139'): '3500 δβr-2  B, M, S — δβar (dbr) ©<Av. duvara ©nom. -y; acc. -w; abl. -h; loc. -y'; pl. -t'; ob. pl. -ty; door, gate — BBB 469, 676, 648, 669; VJ; TSP 3.228, 16.30, 17.40; SCE 109, 504; …'. Page and content both exactly as cited.\"}\n ],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"Gharib nos. 3498 and 3500, p. 138\", \"stance\": \"supports\",\n   \"note\": \"'3498 dbr C = δβr-2' (the Christian-script spelling Nourai transliterates) and the main entry 3500 quoted above; the English index of the same volume lists 'door 3500 / gate 3500'.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 766 (Av. dvar-)\", \"stance\": \"supports\",\n   \"note\": \"supplies the Avestan duvara/dvarəm that Gharib names as the Sogdian word's cognate/etymon.\"},\n  {\"src\": \"HENNING\", \"where\": \"Selected Papers (HENNING_selected_papers.txt)\", \"stance\": \"silent\",\n   \"note\": \"grep for 'δβr' / 'dbr' returns nothing in the local text.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Germanic\", \"words\": \"durunz\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"*durunz is Proto-Germanic, and the form is quoted letter for letter from Nourai's own source: Watkins/AHD s.v. dhwer- has 'Zero-grade form *dhur- in suffixed forms *dhur-n̥s (accusative plural) and *dhur-o- (neuter) respectively in Germanic *durunz and *duram in Old English duru, door (feminine, originally plural), and dor, door (neuter)'. Pokorny 278 says the same in German: 'ags. duru ds. (Akk. Pl. *dhur-n̥s, germ. *durunz, der auch ahd. Dat. Pl. tur-un, -on nach sich zog)'. The derivation is the regular one: PIE zero-grade *dhur- + accusative-plural *-n̥s > Gmc. *-unz (syllabic nasal vocalised to -un-, *s > z by Verner/Germanic voicing), with *dh- > *d- by Grimm's law. The word was a plural in origin — a door was a pair of leaves — which is why Old English duru is a feminine plural in form.\",\n \"derivation_fa\": \"*durunz صورتِ ژرمنیِ آغازین است و نورایی آن را عیناً از مأخذِ خود، پیوستِ ریشه‌های هندواروپاییِ واتکینز، گرفته است: «صورتِ درجهٔ صفرِ *dhur- در ساختِ *dhur-n̥s (رایی جمع) … در ژرمنیِ *durunz و انگلیسی کهنِ duru “در”». پوکورنی نیز در ص ۲۷۸ همین را می‌گوید: «ags. duru … (رایی جمع *dhur-n̥s، ژرمنی *durunz)». دگرگونی‌ها قاعده‌مند است: *dh- هندواروپایی بر پایهٔ قانونِ گریم در ژرمنی d- می‌شود، نونِ هجایی به -un- بدل می‌گردد و *-s پایانی z- می‌شود. این واژه در اصل جمع بوده (در = دو لنگه)، و از این‌روست که duru در انگلیسی کهن صورتِ جمعِ مؤنث دارد. ادعای نورایی درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 396) s.v. dhwer-: '… in Germanic *durunz and *duram in Old English duru, door … and dor, door (neuter): DOOR.' The chart's spelling 'durunz' is Watkins's exactly.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 278 (POK_01.txt line 4004)\", \"stance\": \"supports\",\n   \"note\": \"'ahd. turi, anfränk. duri „Tür“, anord. dyrr „Türöffnung“, fem. Pl. (Nom. pl. *dhur-es); ags. duru ds. (Akk. Pl. *dhur-n̥s, germ. *durunz …); o-St. got. daúr n., ahd. tor, as. dor „Tor“ (*dhurom)'.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. door (KLN_1966.txt line 12080)\", \"stance\": \"supports\",\n   \"note\": \"'ME. dore, dure, fr. OE. dor “door, gate”, duru “door”, rel. to OS. dura, ON. dyrr, Dan. dør, Swed. dörr, OFris. dure, dore, OHG. turi, MHG., G. tür, OHG., MHG., G. tor, Goth. daur “gate”, and cogn. with OI. dvāraḥ …'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 870\", \"stance\": \"supports\",\n   \"note\": \"the Germanic paragraph of the same article Pokorny abridges, with the acc. pl. *dhur-n̥s > germ. *durunz.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"door\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English door continues Old English duru f. (originally a plural, 'the two leaves') and dor n. 'gate', which merged in Middle English dore/dure and gave modern door; the spelling with -oo- reflects the Middle English lengthened /oː/. Klein: 'door, n. — ME. dore, dure, fr. OE. dor “door, gate”, duru “door”', and Watkins ends his Germanic paragraph 'in Old English duru, door … and dor, door (neuter): DOOR'. Nothing in the step from node #6 is contested; door and Persian dar are the same word, both from *dʰur-.\",\n \"derivation_fa\": \"«door» انگلیسی دنبالهٔ duru (مؤنث، در اصل جمع) و dor (خنثی) در انگلیسی کهن است که در انگلیسیِ میانه در صورتِ dore/dure یکی شدند و به door امروزی رسیدند؛ املای -oo- بازتابِ واکهٔ کشیدهٔ /oː/ انگلیسیِ میانه است. کلاین: «ME. dore, dure, fr. OE. dor “door, gate”, duru “door”». این حلقه هیچ اختلافی ندارد و door انگلیسی و «در» فارسی در حقیقت یک واژه‌اند، هر دو از *dʰur-. ادعای نورایی درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; the claim is covered by the AHD reference of its parent node #6 (checked there) and by Klein s.v. door.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. door (KLN_1966.txt line 12080)\", \"stance\": \"supports\",\n   \"note\": \"'door, n. — ME. dore, dure, fr. OE. dor, “door, gate”, duru, “door” … Cp. dargah, dehors, doch-an-doris, durbar, durwaun, foreclose, foreign, forisfamiliate, forjudge, hors de combat, thyroid.' — Klein's cross-references cover almost the whole of this chart.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, dhwer- §1 and the index ('DOOR dhwer-', line 1432)\", \"stance\": \"supports\",\n   \"note\": \"'pooR [=DOOR] dhwer-' in the English index of roots.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. door\", \"stance\": \"supports\",\n   \"note\": \"same OE duru/dor etymology with the Sanskrit, Greek and Latin cognates.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Greek\", \"words\": \"thura; thuroidĕs\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"thuroidĕs : door shaped (gland)\",\n \"correct_form\": \"thureoeidēs (θυρεοειδής) 'shield-shaped'\",\n \"derivation\": \"The first word is right: Greek θύρα thúrā 'door' is the ā-stem of the zero grade *dhur- (Pokorny 278: 'ā-St. θύρα „Tür“ (hom. meist Pl.)'; Beekes, EDG s.v. θύρα), with the regular Greek development *dh- > th-. The second is not. There is no Greek word thuroidēs behind 'thyroid': the medical term is Modern/Medical Latin thyreoideus, from Greek θυρεοειδής thyreoeidḗs 'shield-shaped', a compound of θυρεός thyreós 'the stone put against a door; (hence) the oblong door-shaped shield' + -οειδής '-shaped' (from εἶδος 'form'). Galen's χόνδρος θυρεοειδής 'shield-shaped cartilage' is the Adam's apple, and the gland was named from the cartilage. Klein spells this out: 'thyroid … lit. “shield-shaped” (anat.) — Medical L. thyreoideus, fr. Gk. θυρεοειδής, “shield-shaped”, compounded of θυρεός, “stone put against a door; oblong shield”, which is rel. to θύρα, “door”, and of -οειδής, “like”, fr. εἶδος'; Watkins likewise writes 'Zero-grade form *dhur- in Greek thura, door (> thureos, shield): THYROID'. So the book's form has lost the -e- of thureo- and its gloss 'door shaped' skips the shield, which is the step that actually explains the anatomy. I rendered pdf page 136 at 300 dpi (saved as data/verification/sources/refs/ocr/BOOK/136.png): the printed box reads 'thuroidĕs : door shaped (gland)', so the extraction is faithful and the fault is the book's.\",\n \"derivation_fa\": \"واژهٔ نخست درست است: یونانیِ θύρα «در» صورتِ ستاکِ ـā از درجهٔ صفرِ *dʰur- است (پوکورنی ص ۲۷۸: «ā-St. θύρα „Tür“»)، با تبدیلِ قاعده‌مندِ *dʰ- به th- در یونانی. اما واژهٔ دوم چنین نیست: هیچ واژهٔ یونانیِ «thuroidēs» پشتِ «تیروئید» نیست؛ اصطلاحِ پزشکی از لاتینِ نو thyreoideus و آن از یونانیِ θυρεοειδής «سپرشکل» می‌آید، مرکب از θυρεός «سنگی که پشتِ در می‌گذاشتند؛ سپرِ درازِ درمانند» و ‑οειδής «به شکلِ». جالینوس غضروفِ حنجره را «χόνδρος θυρεοειδής» یعنی «غضروفِ سپرشکل» نامید و غده از نامِ همان غضروف نام گرفت. کلاین صریحاً همین را می‌نویسد و واتکینز نیز «θύρα > θυρεός “سپر” > THYROID» را می‌آورد. پس صورتِ کتاب هم واکهٔ e را در thureo- انداخته و هم معنایی که داده («در‑شکل») حلقهٔ «سپر» را جا انداخته است. تصویرِ صفحهٔ چاپیِ ۱۳۶ را با تفکیک ۳۰۰ دیدم: در کتاب هم «thuroidĕs : door shaped (gland)» چاپ شده؛ پس خطای خوانشِ اسکن نیست، خطای چاپیِ خودِ کتاب است.\",\n \"sources\": [ETY_T, PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD:1343\", \"status\": \"not_checked\",\n   \"note\": \"AHD:1343 is a page of the main dictionary of the AHD New College edition (1975/76), which is not available; only the Indo-European appendix (Watkins) is on disk, and it does carry the claim: 'Zero-grade form *dhur- in Greek thura, door (> thureos, shield): THYROID' (AHD_watkins1985.txt line 399), with 'THYROID dhwer-' in the index (line 2389). That is, the appendix supports 'thura' and the thyroid link but shows the shield step the book's gloss omits.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. thyroid (KLN_1966.txt line 39205)\", \"stance\": \"partial\",\n   \"note\": \"'thyroid, adj. … lit. “shield-shaped” (anat.) — Medical L. thyreoideus, fr. Gk. θυρεοειδής, “shield-shaped”, compounded of θυρεός, “stone put against a door; oblong shield”, which is rel. to θύρα, “door”, and of -οειδής, “like”, fr. εἶδος, “form, shape”. See door and -oid.' — same family, different form and gloss from the book's.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 278 (POK_01.txt line 3998)\", \"stance\": \"supports\",\n   \"note\": \"'ā-St. θύρα „Tür“ (hom. meist Pl.), att. θύρᾱσι „draußen“ … θυρεός „Türstein; großer langer Schild“' — Pokorny has both θύρα and θυρεός (with the -e-), never a *thuroidēs.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. thyro-/thyreo- (KLN_1966.txt line 39205, first paragraph)\", \"stance\": \"supports\",\n   \"note\": \"'thyro-, before a vowel thyr-, combining form meaning “thyroid” — Shortened fr. Gk. θυρεοειδής. See thyroid and cp. thyreo-.' — the modern combining form thyro- is a shortening of thyreo-, which is very likely how Nourai's 'thuroidĕs' arose.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"An empty pass-through box: it marks the language through which the Greek-Latin anatomical term reached Persian, and the book prints no word in it (confirmed on the page image). The word intended is French thyroïde (adj. and n. f.), taken into French anatomical usage in the 16th-17th century from Modern Latin thyreoides / (cartilago) thyreoidea; French then dropped the -e- of thyreo- and wrote the group -oï- with a diaeresis to keep the hiatus (thy-ro-ï-de). That French form, not the Greek or the English one, is what Persian borrowed (see node #10, where Mo'in tags the Persian word [فر.] 'French'). The step is therefore real; it is rated plausible only because the box itself is empty and the intermediate is unstated.\",\n \"derivation_fa\": \"این جعبه تهی است و تنها زبانِ واسطه را نشان می‌دهد؛ در کتاب هم هیچ واژه‌ای در آن چاپ نشده (از روی تصویرِ صفحه بررسی شد). واژهٔ موردِ نظر «thyroïde» فرانسه است که در سده‌های شانزدهم‑هفدهم از لاتینِ نو thyreoides وارد کالبدشناسیِ فرانسوی شد؛ فرانسه واکهٔ e را در thyreo- انداخت و برای نگه‌داشتنِ هجای جدا بر روی i نقطهٔ جدایی (تِرِما) گذاشت: thy‑ro‑ï‑de. همین صورتِ فرانسوی است که به فارسی وام داده شده، نه صورتِ یونانی یا انگلیسی — چنان‌که معین نیز واژهٔ فارسی را با نشانِ [فر.] آورده است. پس حلقه واقعی است و تنها به سببِ تهی بودنِ جعبه «با احتیاط پذیرفتنی» ارزیابی می‌شود.\",\n \"sources\": [ETY_T, AB + \"%D8%AA%DB%8C%D8%B1%D9%88%D8%A6%DB%8C%D8%AF/\"],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; it is an empty language box.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. thyroid / parathyroid (KLN_1966.txt lines 27363, 39205)\", \"stance\": \"supports\",\n   \"note\": \"Klein routes the term through 'Medical L. thyreoideus' and notes the 19th-century coinages built on it in French and German (e.g. parathyroid, coined 1879 by Ivar Sandström); the modern European forms are all from the Medical Latin, French thyroïde among them.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in s.v. تیروئید (via abadis.ir, archived)\", \"stance\": \"supports\",\n   \"note\": \"the Persian entry's origin tag is «[فر.]» = French, which is precisely the intermediate this empty box represents.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"tîroîd\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian تیروئید tirō'id 'thyroid (gland)' is a 20th-century medical loan from French thyroïde, exactly as drawn. Mo'in — Nourai's reference here — tags it «[فر.]», i.e. borrowed from French, and defines it «غده‌ای است در زیر گلو که ماده‌ای به نام تیروکسین را در خون ترشح می‌کند» ('a gland below the throat which secretes into the blood a substance called thyroxine'). The Persian spelling mirrors the French pronunciation rather than the English: French [tiʁɔid] gives تیروئید with a hamza on the wāw seat to render the -o-ï- hiatus, and the initial تی- reflects French ti-, not English thy- [θaɪ]. The same route gives پاراتیروئید, هیپرتیروئیدی and هیپوتیروئیدی, all of which appear in Mo'in's own text.\",\n \"derivation_fa\": \"«تیروئید» وام‌واژه‌ای پزشکی از فرانسهٔ thyroïde است که در سدهٔ بیستم وارد فارسی شده — دقیقاً همان مسیری که نمودار می‌کشد. معین، همان مأخذِ نورایی، آن را با نشانِ «[فر.]» آورده و چنین تعریف می‌کند: «غده‌ای است در زیر گلو که ماده‌ای به نام تیروکسین را در خون ترشح می‌کند». املای فارسی از تلفظِ فرانسوی پیروی می‌کند نه انگلیسی: در فرانسه [tiʁɔid] است، پس «تی‑» (نه «ثای» انگلیسی) و همزه روی واو برای نشان دادنِ گسستِ o‑ï. مشتقاتِ «پاراتیروئید» و «هیپرتیروئیدی» و «هیپوتیروئیدی» نیز از همین راه آمده‌اند و در متنِ خودِ معین دیده می‌شوند. ادعای نورایی درست است.\",\n \"sources\": [AB + \"%D8%AA%DB%8C%D8%B1%D9%88%D8%A6%DB%8C%D8%AF/\", ETY_T],\n \"ref_check\": [\n  {\"ref\": \"MON:1178\", \"status\": \"partial\",\n   \"note\": \"content confirmed verbatim from Mo'in via abadis.ir (archived): «[ فر . ] (اِ. ) غده ای است در زیر گلو که ماده ای به نام تیروکسین را در خون ترشح می کند» — the [فر.] tag is exactly the French → Persian arrow of the chart. The page number itself is unverifiable, the 6-volume edition not being online; but تیروئید falls in the ت section of vol. 1, which is consistent with p. 1178.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"Mo'in s.v. تیروئید (abadis.ir/fatofa/تیروئید, archived)\", \"stance\": \"supports\",\n   \"note\": \"«[فر.] (اِ.) غده‌ای است در زیر گلو …»\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in 2-vol. Adena condensation, v. 1 (MON_2vol_Adena_v1_djvu.txt line 27831) and v. 2 (MON_part2.txt lines 35586-35663)\", \"stance\": \"supports\",\n   \"note\": \"«پاراتیروئید: (بر.) دو زوج غده که در طرفین غدهٔ تیروئید قرار دارند» and the goitre articles «هیپرتیروئیدی / هیپوتیروئیدی» — the loan and its derivatives are fully naturalised in Mo'in's Persian.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"thyroid\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English thyroid, first attested in the 1690s, is from Modern Latin thyreoides / thyroides, itself the Greek θυρεοειδής 'shield-shaped'; Galen's phrase khondros thyreoeidēs, 'shield-shaped cartilage', named the Adam's apple, and the gland lying against that cartilage took the name in the modern anatomical sense from 1849 (Etymonline). So the English word does come from the Greek node, as the chart draws — via Medical Latin, an intermediate the chart leaves out — and the ultimate root is *dʰur- 'door', through θυρεός 'the stone set against a door; the oblong shield'. Watkins lists THYROID under dhwer-, and Klein under door.\",\n \"derivation_fa\": \"«thyroid» انگلیسی از دههٔ ۱۶۹۰ به کار رفته و از لاتینِ نو thyreoides/thyroides و آن از یونانیِ θυρεοειδής «سپرشکل» گرفته شده است؛ جالینوس غضروفِ حنجره را «غضروفِ سپرشکل» نامیده بود و غده‌ای که کنارِ همان غضروف است از سالِ ۱۸۴۹ به همین نام خوانده شد. پس واژهٔ انگلیسی همان‌گونه که نمودار می‌کشد از گرهِ یونانی می‌آید (البته از راهِ لاتینِ پزشکی که در نمودار نیامده) و ریشهٔ نهایی‌اش *dʰur- «در» است، از راهِ θυρεός «سنگِ پشتِ در؛ سپرِ دراز». واتکینز THYROID را زیر dhwer- و کلاین آن را زیر door آورده است. ادعای نورایی درست است.\",\n \"sources\": [ETY_T],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference in the book for this node; the claim is covered by AHD/Watkins s.v. dhwer- §5 and by Klein s.v. thyroid, both checked at node #8.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. thyroid (KLN_1966.txt line 39205)\", \"stance\": \"supports\",\n   \"note\": \"'thyroid, adj., pertaining to … the ductless gland in the neck …; lit. “shield-shaped” (anat.) — Medical L. thyreoideus, fr. Gk. θυρεοειδής … rel. to θύρα, “door”. See door and -oid.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, dhwer- §5 and index (AHD_watkins1985.txt lines 399, 2389)\", \"stance\": \"supports\",\n   \"note\": \"'5. Zero-grade form *dhur- in Greek thura, door (> thureos, shield): THYROID'; index: 'THYROID dhwer-'.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Latin\", \"words\": \"foris, foras\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin has forēs f. pl. 'the (two-leaved) door' — an old consonant stem *dhwor-, remade as an i-stem, the singular foris being secondary — and beside it the two adverbs the chart cites: forās 'out of doors, outwards' (an old accusative plural, *dhwor-n̥s) and forīs 'outside, out of doors' (locative/ablative plural, *dhwor-ois). Pokorny 278: 'lat. Plur. forēs f. „zweiflüglige Tür“ (alter kons. St. *dhuor- zum i-St. umgebildet); der Sg. foris, -is ist sekundär; ō-St. in forās „hinaus“, forīs „draußen, außerhalb“'. Watkins analyses the two adverbs exactly as the chart's parent-child relation needs: '*dhwor-n̥s (accusative plural) in Latin forās … 3. *dhwor-ois (locative plural) in Latin foris'. Ernout-Meillet add the semantic point: the door was the boundary of the household, so 'at the doors' came to mean simply 'outside' — which is why Nourai glosses the node 'outdoors, outside' rather than 'door'. Latin f- from PIE *dh- is the regular word-initial Italic outcome (*dh > *þ > f).\",\n \"derivation_fa\": \"لاتین forēs (جمعِ مؤنث) «درِ دولنگه» دارد — ستاکِ کهنِ صامتیِ *dhwor- که بعدها به ستاکِ i بدل شده و مفردِ foris ثانوی است — و در کنارِ آن دو قیدی که نمودار آورده: forās «به بیرون» (رایی جمعِ کهن، *dhwor-n̥s) و forīs «بیرون، در بیرون» (دری/ازیِ جمع، *dhwor-ois). پوکورنی ص ۲۷۸: «lat. Plur. forēs „zweiflüglige Tür“ … ō-St. in forās „hinaus“, forīs „draußen“». واتکینز نیز همین دو صورت را از *dhwor-n̥s و *dhwor-ois می‌گیرد. ارنو و مِیه نکتهٔ معنایی را می‌افزایند: «در» مرزِ خانه بوده، پس «بر درها» به معنیِ «بیرون» درآمده است — و به همین سبب نورایی این گره را «بیرون، در بیرون» معنی کرده نه «در». تبدیلِ *dh- هندواروپایی به f- در آغازِ واژه دگرگونیِ قاعده‌مندِ ایتالیایی است. ادعای نورایی درست است.\",\n \"sources\": [PIE, ETY_F],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. dhwer- §§2-3 (AHD_watkins1985.txt lines 397-399): '2. Suffixed o-grade form *dhwor-n̥s (accusative plural) in Latin forās, (toward) out of doors, outside: FOREIGN. 3. Suffixed o-grade form *dhwor-ois (locative plural) in Latin foris, (being) out of doors: FOREST; (AFFOREST), FAUBOURG, FORECLOSE, FORFEIT.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 278 (POK_01.txt line 4000)\", \"stance\": \"supports\",\n   \"note\": \"'lat. Plur. forēs f. „zweiflüglige Tür“ (alter kons. St. *dhuor- zum i-St. umgebildet); der Sg. foris, -is ist sekundär; ō-St. in forās „hinaus“, forīs „draußen, außerhalb“ (der Vokal nach forēs); dazu forum n. …'\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. forēs (LAT.txt lines 23490-23520)\", \"stance\": \"supports\",\n   \"note\": \"'À un doublet *fora se rattachent les adverbes foris (abl.loc.pl.), foras (accus.pl.) “dehors, au dehors” … attestés dès les plus anciens textes' and 'Le thème *dhwer- “porte” s'employait essentiellement au pluriel … Le latin a généralisé le vocalisme *dhwor- du nominatif pluriel.'\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. door (KLN_1966.txt line 12080)\", \"stance\": \"supports\",\n   \"note\": \"lists 'L. forēs (pl.), “door”, forās, “out of doors, out”, forīs, “out at the doors, out of doors”' among the cognates of door.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"forest, foreign\",\n \"verdict\": \"plausible\",\n \"derivation\": \"foreign is secure: c. 1300 ME forein, from Old French forain 'outside, alien', from Vulgar/Medieval Latin forānus < forāneus 'on the outside', a derivative of Latin forīs 'outside' — Watkins puts FOREIGN under *dhwor-n̥s/forās, Ernout-Meillet list 'forānus (-neus) “étranger”, M.L. 3438-9' among the late derivatives of foris/foras. forest is the standard but not the only account: English forest (late 13th c.) is from Old French forest, from Medieval Latin forestis (silva) 'the outside wood', first in the Capitularies of Charlemagne for the royal woodland outside the enclosed park; Ernout-Meillet cite the same document ('forestis, Diplom. de Childebert … cf. fr. forêt') under foris, and Klein s.v. afforest has 'Late L. forestis (scil. silva), “open woodland”'. But Etymonline records two live competitors: derivation from Latin forum in its legal sense 'court, judgement', i.e. 'land placed under a ban', and influence or origin from a Germanic *forhist / OHG forst 'wooded land'. So one of the two English words hangs on a link that modern scholarship treats as probable rather than settled — hence 'plausible' for the node.\",\n \"derivation_fa\": \"«foreign» بی‌اشکال است: از حدودِ ۱۳۰۰ میلادی در انگلیسیِ میانه به صورتِ forein، از فرانسهٔ کهنِ forain «بیرونی، بیگانه»، از لاتینِ مردمی/میانهٔ forāneus «بیرونی»، مشتق از forīs «بیرون»؛ واتکینز نیز FOREIGN را زیر forās می‌آورد. اما «forest» روایتِ رایج دارد نه روایتِ یگانه: از فرانسهٔ کهنِ forest، از لاتینِ میانهٔ forestis (silva) «جنگلِ بیرونی»، نخست در فرمان‌های شارلمانی برای بیشه‌های شاهیِ بیرون از پارکِ محصور — ارنو و مِیه همین سند را ذیلِ foris نقل می‌کنند و کلاین هم می‌نویسد «Late L. forestis (scil. silva) “open woodland”». با این حال اتیمانلاین دو نظرِ رقیب را ثبت کرده است: یکی اشتقاق از forum لاتین به معنای حقوقیِ «دادگاه/حکم» (یعنی «زمینِ زیرِ قُرُق») و دیگری تأثیر یا خاستگاهِ ژرمنیِ *forhist / forst در آلمانیِ کهن. پس یکی از دو واژهٔ این گره به حلقه‌ای بند است که پژوهشِ امروزی آن را «محتمل» می‌داند نه قطعی — و از این‌رو گره «با احتیاط پذیرفتنی» است.\",\n \"sources\": [ETY_F],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. dhwer- (AHD_watkins1985.txt lines 397-399) puts both English words under the root: '§2 … in Latin forās … : FOREIGN' and '§3 … in Latin foris …: FOREST; (AFFOREST), FAUBOURG, FORECLOSE, FORFEIT'; the index confirms 'FOREST dhwer-', 'FOREIGN dhwer-' (line 1533).\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. afforest (KLN_1966.txt line 1869) and door (line 12080)\", \"stance\": \"supports\",\n   \"note\": \"'ML. afforestare, fr. ad- and forestare, fr. Late L. forestis (scil. silva), “open woodland”. See forest'; and the cross-reference list under door includes 'foreclose, foreign, forisfamiliate, forjudge'.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. forēs/foris (LAT.txt line 23514 ff.)\", \"stance\": \"supports\",\n   \"note\": \"'les dérivés de la basse époque: forānus (-neus) “étranger”, M.L. 3438-9, forasticus 3433; forestis (Diplom. de Childebert. Mon.Germ.Dipl.imp. I n.5, p.7,43), cf. fr. forêt.'\"},\n  {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls Standard Dictionary (FSD_vol1-4.txt)\", \"stance\": \"silent\",\n   \"note\": \"no usable article located in the local OCR for either word.\"}\n ]\n})\n\ndoc[\"entries\"].append(e2)\nout = '/home/sfmqrb/git/rishe/data/verification/page-136.json'\nwith io.open(out, 'w', encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"wrote\", out, \"entries\", len(doc[\"entries\"]), \"nodes\", [len(e[\"nodes\"]) for e in doc[\"entries\"]])\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build136b.py"
}
```


### [2026-09-05T20:29:00.452Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-136.json entries 2 nodes [2, 13]
```


## [2026-09-05T20:29:04.636Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-136.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 136"
}
```


### [2026-09-05T20:29:06.664Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 5, 'disputed': 1, 'confirmed': 8, 'transcription_suspect': 1}
root verdicts: {'plausible': 2}
ref checks: {'supports': 8, 'contradicts': 1, 'partial': 3, 'not_checked': 6}
books consulted: {'supports': 33, 'silent': 9, 'contradicts': 3, 'partial': 3} | by book: {'KLN': 8, 'MON': 5, 'POK': 4, 'PHD': 3, 'ARY': 3, 'LAT': 3, 'HRN': 2, 'SYN': 2, 'WLD': 2, 'BRT': 2, 'LKT': 2, 'AHD': 2, 'LEW': 1, 'KNT': 1, 'AFM': 1, 'FVQ': 1, 'DOZ': 1, 'BQT': 1, 'SOD': 1, 'HENNING': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-05T20:29:13.064Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport io\np='data/verification/page-136.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('س.v. الدرب','s.v. الدرب').replace('MHG cƒ. tūsen','MHG cf. tūsen')\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\ngrep -c \"س.v.\\|cƒ\" data/verification/page-136.json; python3 -m json.tool data/verification/page-136.json >/dev/null && echo OK && python3 tools/verify_check.py 136 | tail -3"
}
```


### [2026-09-05T20:29:15.158Z] TOOL RESULT

```
0
OK
root verdicts: {'plausible': 2}
ref checks: {'supports': 8, 'contradicts': 1, 'partial': 3, 'not_checked': 6}
books consulted: {'supports': 33, 'silent': 9, 'contradicts': 3, 'partial': 3} | by book: {'KLN': 8, 'MON': 5, 'POK': 4, 'PHD': 3, 'ARY': 3, 'LAT': 3, 'HRN': 2, 'SYN': 2, 'WLD': 2, 'BRT': 2, 'LKT': 2, 'AHD': 2, 'LEW': 1, 'KNT': 1, 'AFM': 1, 'FVQ': 1, 'DOZ': 1, 'BQT': 1, 'SOD': 1, 'HENNING': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-05T20:29:33.073Z] AGENT

Page 136 (book p. 106) verified. `verify_check.py 136`: 15/15 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 2 plausible. Nodes: 8 confirmed, 5 plausible, 1 disputed, 1 transcription_suspect.
Ref checks: 8 supports, 3 partial, 1 contradicts, 6 not_checked. 48 `consulted` entries across 22 books.

**Flagged items**
- **disputed — Dhŭs #2, Latin `fūsus` "spindle"**: Ernout-Meillet 470 "Étymologie inconnue", Buck §6.32 "etym. dub.", Wiktionary "unclear, possibly non-IE substrate". The node's own NOTE is wrong too: Pokorny 448 derives the *participle* `fūsum` from *ǵheu-* and expressly sets the spindle aside ("über fūsus 'Spindel' s. WH. I 474"); WLD is blunter ("kaum fusus 'Spindel'?").
- **transcription_suspect — Dhwer #8, Greek `thuroidĕs` "door shaped"**: no such Greek word; the source of *thyroid* is θυρεοειδής *thyreoeidḗs* "shield-shaped" (< θυρεός "door-stone, oblong shield"), per Klein and Watkins. `error_in: book` — I rendered pdf p. 136 at 300 dpi and the page does print "thuroidĕs : door shaped (gland)"; the extraction is faithful. Image saved to `data/verification/sources/refs/ocr/BOOK/136.png`.
- **root Dhwer "Dhwer, Dhrugh, Dhwor"** rated plausible: *dʰwer-* "door" = Pokorny 278 exactly, but **Dhrugh does not belong here** — *dhrugh-* is the zero grade of *dhreugh-* "deceive" (Pok. 276), which Nourai himself heads as a separate root on pdf p. 135 (with draoga-, duruj-, دروغ). Again the book's own error (the printed page shows it), probably from Kent, where `duruj- … pIE *dhrugh-` sits on the same opening (pp. 191-192) as `duvara-`. No node on the page descends from it.
- **root Dhŭs** plausible: faithfully copied from Mann IEC 224, but the root is Mann's alone — absent from Pokorny, Walde-Pokorny and Watkins.

**Other notes**: KNT:191 is off by one (duvara- is on Kent p. 192); FVF:98,240 could not be checked (noorlib serves the book only through a JS viewer), but Addi Shir independently attests the same Persian→Arabic claim for درب/دربند; MON page numbers unverifiable (6-vol. Mo'in not online) though both entry texts were confirmed via abadis. `bandar` remains the weak word in node #2 — no source confirms the band+dar analysis. **No extraction errors found**: the JSON matches the printed page throughout.
