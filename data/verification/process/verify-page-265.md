# Verification process log — verify-page-265


## [2026-09-06T20:34:22.669Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 265 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-265.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-265.json. Write /home/sfmqrb/git/rishe/data/verification/page-265.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 265` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:34:24.283Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:34:24.993Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:34:25.008Z] TOOL RESULT

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


## [2026-09-06T20:34:25.178Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-265.txt"
}
```


### [2026-09-06T20:34:25.202Z] TOOL RESULT

```
1	=== PDF page 265 (book page 235) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Keuk 1 : to shine, be white  (refs POK:597)
4	#1 (parent #0) [Avestan] refs=POK:597; HRN:161,165; IRN:128 | saoč, sauk, saux : to light up ; saoka : flame ; suxra : glowing red ; suxra-vard : red rose ☞Wrdho ; aiwi-saoka : burn in regret ☞Ambhi ; upa-suxta, âtra-saoka, saočint
5	  #2 (parent #1) [Persian] refs=BQT:1183,1189,1195; DRM:131; IRN:128; FFD:61 | sŭxtan «سوختن» : to burn ; sŭk «سوک ۱ ( سوگ ۱ )» : sorrow, mourning ; sorx «سرخ ( سرخاب ، سهراب )» : red ; Sohrvard «سُهروَرد» : a town near Tehran (Red Rose) ; afsŭs «افسوس» : regret | extra: سوزش ، سوزان ، سوزاک ، سوز ، جانسوز
6	  #3 (parent #1) [Avestan] refs=HRN:167 | saokenta : a burning substance, sulfur ; saokenta-vant : a drink mixed with sulfur
7	    #4 (parent #3) [Persian] refs=BQT:1190 | sogand «سوگند» : oath | NOTE: Originally "sogand" was a sulfur filled drink given to defendants to determine the truth based on their body reaction to sulfur.
8	    #5 (parent #3) [Sogdian] refs=SOD:365 | swgnd, swk`nt : oath
9	#6 (parent #0) [Greek] refs=POK:597 | kuknos : white, white swan
10	  #7 (parent #6) [English] refs=None | cygnet : young swan
11	--- entry 1 ---
12	ROOT Keuk 2 -> redirect to Gěu 1
13	--- entry 2 ---
14	ROOT Keup -> redirect to Gěu 1
15	--- entry 3 ---
16	ROOT [Armenian] Khâč, Xâč 2 : cross  (refs MON:1384)
17	#1 (parent #0) [Persian] refs=HUB:227; BQT:696; MON:1384 | xâj «خاج» : cross, club suit in cards
18	--- entry 4 ---
19	ROOT [Indo-European] Khâd, Qhâd : to bite  (refs POK:634; WLD1:341)
20	#1 (parent #0) [Sanskrit] refs=POK:634 | xâd : to bite
21	  #2 (parent #1) [Avestan] refs=HRN:104 | xad 1
22	    #3 (parent #2) [Persian] refs=BQT:712 | xâyîdan «خاییدن ( خای )» : to grind with teeth, chew
23	--- entry 5 ---
24	ROOT Khai -> redirect to Ghei 1
25	
```


## [2026-09-06T20:34:31.873Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-265.json",
 "description": "Read source JSON page 265"
}
```


### [2026-09-06T20:34:31.910Z] TOOL RESULT

```
{
  "pdf_page": 265,
  "book_page": 235,
  "entries": [
    {
      "root": {
        "name": "Keuk 1",
        "lang": "Indo-European",
        "refs": "POK:597",
        "gloss": "to shine, be white"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:597; HRN:161,165; IRN:128",
          "words": [
            {"translit": "saoč, sauk, saux", "gloss": "to light up", "script": null},
            {"translit": "saoka", "gloss": "flame", "script": null},
            {"translit": "suxra", "gloss": "glowing red", "script": null},
            {"translit": "suxra-vard", "gloss": "red rose", "script": null, "see": ["Wrdho"]},
            {"translit": "aiwi-saoka", "gloss": "burn in regret", "script": null, "see": ["Ambhi"]},
            {"translit": "upa-suxta, âtra-saoka, saočint", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1183,1189,1195; DRM:131; IRN:128; FFD:61",
          "words": [
            {"translit": "sŭxtan", "gloss": "to burn", "script": "سوختن"},
            {"translit": "sŭk", "gloss": "sorrow, mourning", "script": "سوک ۱ ( سوگ ۱ )"},
            {"translit": "sorx", "gloss": "red", "script": "سرخ ( سرخاب ، سهراب )"},
            {"translit": "Sohrvard", "gloss": "a town near Tehran (Red Rose)", "script": "سُهروَرد"},
            {"translit": "afsŭs", "gloss": "regret", "script": "افسوس"}
          ],
          "script_extra": "سوزش ، سوزان ، سوزاک ، سوز ، جانسوز",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan",
          "refs": "HRN:167",
          "words": [
            {"translit": "saokenta", "gloss": "a burning substance, sulfur", "script": null},
            {"translit": "saokenta-vant", "gloss": "a drink mixed with sulfur", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1190",
          "words": [
            {"translit": "sogand", "gloss": "oath", "script": "سوگند"}
          ],
          "script_extra": null,
          "note": "Originally \"sogand\" was a sulfur filled drink given to defendants to determine the truth based on their body reaction to sulfur.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Sogdian",
          "refs": "SOD:365",
          "words": [
            {"translit": "swgnd, swk`nt", "gloss": "oath", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:597",
          "words": [
            {"translit": "kuknos", "gloss": "white, white swan", "script": null}
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
            {"translit": "cygnet", "gloss": "young swan", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Keuk 2", "redirect": "Gěu 1"},
      "nodes": []
    },
    {
      "root": {"name": "Keup", "redirect": "Gěu 1"},
      "nodes": []
    },
    {
      "root": {
        "name": "Khâč, Xâč 2",
        "lang": "Armenian",
        "refs": "MON:1384",
        "gloss": "cross"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "HUB:227; BQT:696; MON:1384",
          "words": [
            {"translit": "xâj", "gloss": "cross, club suit in cards", "script": "خاج"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "صلیب و خاج بسوزد کلیسیا - بنای مدرسه بر گنبد گران آرد",
            "poet": "Kamâl Esmâîl"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Khâd, Qhâd",
        "lang": "Indo-European",
        "refs": "POK:634; WLD1:341",
        "gloss": "to bite"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:634",
          "words": [
            {"translit": "xâd", "gloss": "to bite", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "HRN:104",
          "words": [
            {"translit": "xad 1", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:712",
          "words": [
            {"translit": "xâyîdan", "gloss": "to grind with teeth, chew", "script": "خاییدن ( خای )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همی لب به دندان بخاييد شاه - همی کرد خیره بدیشان نگاه",
            "poet": "Ferdowsî"
          }
        }
      ]
    },
    {
      "root": {"name": "Khai", "redirect": "Ghei 1"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T20:34:32.140Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T20:34:32.185Z] TOOL RESULT

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


## [2026-09-06T20:34:36.271Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T20:34:36.320Z] TOOL RESULT

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


## [2026-09-06T20:34:38.110Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','WLD1','HRN','HUB','IRN','FFD','BQT','MON','SOD','DRM','SKT','KLN','AHD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T20:34:40.227Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

WLD1 null

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

DRM {"title": "J. Darmesteter, Études iraniennes, 2 vols., Paris 1883", "edition_found": "1883 both tomes in one scan", "kind": "archive_djvu", "url": "https://archive.org/details/etudesiraniennes00darm", "identifier": "etudesiraniennes00darm (t.1 alone: tudesiranienne01darmuoft; t.2 alone: darmesteter-etudes-sur-la-langue-la-litterature-les-croyances-de-la-perse-ancienne)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt", "page_offset": "Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say w

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
```


## [2026-09-06T20:35:09.567Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==253' POK_02.txt | head -60\necho \"=====POK 634 (leaf 290)=====\"\nawk 'BEGIN{RS=\"\\f\"} NR==290' POK_02.txt | head -60",
 "description": "Print Pokorny pages 597 and 634"
}
```


## [2026-09-06T20:35:10.286Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"keuk\" POK_full.txt | head -20; echo ---; grep -n \"khād\\|khad-\" POK_full.txt | head -20",
 "description": "Grep Pokorny for keuk and khad"
}
```


### [2026-09-06T20:35:11.409Z] TOOL RESULT

```
. §üra-)  , stark,  gewaltig',  Superl.  sdvista-  (=  ai.  sdvistha-)]  süra-  m.  ,Loch, lacuna',  npers.  süräx  ,Loch^  ( :  ytvag  =  ilögog  :  ijöcoQ ;  s.  auch  arm.  sor^ allenfalls  lat.  caver-na)]
arm.  sun  (s.  ohen  zu  ai.  süna-  , Leere');  sor  ,Loch'  (*so[v]oro-  aus  *sovaro- =  ai.  *savira-j  gr.  -nvag),  soil  , Höhle'  (*keu-lo-)',
alb.  thele  ,tief'  (=  xd(/)tAog;  o  zu  a  und  durch  Umlaut  zu  e) ;  thane ,Kornelkirsche'  {*kousna)j  tosk.  i  thante  ,kerngesund'  (Jokl  hei  WH.  I  277);
gr.  v,6oi '  TU  xdo}iaTa  rrjg  yfjgy  xat  rä  yiOLXcbfxara  Hes.  ( :  lat.  cavus, mir.  cüa),  %olXog  ,hohl'  (Y.6fiXog  ==  alb.  thele),  dehnstufig  xwog  ,Höhle, Gefängnis';  "Kvaq  (*kuur)  ,Loch'  (s.  oben  zu  av.  süra-  ,Loch',  arm.  sor)] (vielleicht  Fremdwörter  -Kvad-og  , Becher'  und  xw^wv  ,lakon.  bauchiges Trinkgeschirr'  aus  *xo/ai^a>v?);  Y.vXa'  xä  uTroxaro»  tmv  ßXscpdQwv  y.od(b- fiUTa  Hes.  (auch  y.vXov  ,Td  y-drco-d^sv  ßXe(paQOv^  Poll.,  Suid. ;  auch  xvXdösg, %vXi6eg ;  dazu,  wie  es  scheint,  %oly,vXIo)  , gaffe  umher',  KoLycvXliov  eigentlich ,Gaffer';
mit  der  Bed.  ,sch wellen'  usw. :  xvew,  (iy)'Kva),  Aor.  e^vaa  ,schwanger sein',  y.vog  n.  ,foetus'  (:  cymr.  cyw),  ey-avog  , schwanger',  i'yy,'6^ü)v(?)  ds. ; xv^a  ,Woge';  Kvdgrj'  fj  Ad^iqva  Hes.  (,*die  starke',  ablaut.  mit  ai.  savlra-, gall.  Kavagog) ;  U-y.vQog  ,ungültig'  (=  ai.  süra-),  x'ÖQtog  , Kraft,  Macht  habend, herrschend,  maßgebend;  Herr',  ycvgog  n.  , Macht,  Kraft,  Einfluß,  Entschei- dung'; dazu  von  der  Stufe  *kuä-  (wie  ai.  svätrd-)  dor.  Aor.  TT&octod-ai^ Perf.  Ttejtaixai , Verfügung,  Gewalt  über  etwas  bekommen',  Trä^a  ,Besitztum', PN  Qi6-7t7taaTog  {Ttit  <  ku),  ion.  e^rctjg,  dor.  efXTtag  , gleich,  jedenfalls,  über- haupt'; dazu  i(,Lftd^o{j.aL  ,kümmere  mich  um  etw^as',  -/.axei-LTcaCo)  , ergreife, überfalle'  (,*nehme  in  Besitz'),  e^rcaiog  , erfahren,  kundig'  (,*im  Besitz  von etwas') ;
Ttag  ,ganz'  (*7tä-vr-  aus  *kuä-nt-)j  auch  =  ä-näg  ,jeder',  ai.  sd-ävant- {*sa-svant-)  ,jeder  der  Reihe  nach,  vollständig';
lat.  cavus  ,hohl,  gewölbt  (konkav)'  aus  "^couos  (vgl.  port.  covo  usw.), caverna  , Höhle';  cumulus  (*ku-me-los  , Anschwellung')  , Haufe';  inciens ,trächtig'  (*en-cuiens,  ähnlich  ai.  svayate)
=====POK 634 (leaf 290)=====
ty-anc  ,giänzend',  av.  spiti-doid-ra-  , helläugig' ;
unsicher  gr.  rlravog  f.,  m.  ,Kalk,  Gips,  Kreide'  {*kidt-^no-s),  -aizTavog Jg.,  dissimil.  aus  *kuit-u-3no-s  ON  TLrdvrj,  äol.  lakon.  TLitavT}]  Bergname Tiragog ;
lit.  sviecHij  sviesti  , leuchten' :  sveiciü,  svelsti , reinigen',  svitH,  smfeti  , immer- zu glänzen,  flimmern',  svintü^  svhti  ,hell  werden*,  Kaus.  §vaitaü,  svaityti jhell  machen' ;  svltras  m.  , Glaspapier',  svytruoti  ,flimmern' ;
aksl.  svhtiH  se^  svhUti  se  , leuchten'  und  slav.  "^svhng  (aus  *ävitnö  neben lit.  svintil)  in  russ.-ksl.  svbnuti]  Kaus.  aksl.  svätiti  ^jemandem  leuchten'; slav.  svaita-  m.  ,Licht'  in  aksl.  sv^h  ,Licht,  Welt';  dazu  slav.  *svaitja  in aksl.  ävSäta  ,Licht,  Kerze';
daneben  mit  westidg.  k-:
lett.  kvitUj  kvitet  ,flimmern,  glänzen',  Kaus.  kvitinät;
slav.  ^kvbtq,  *kvisti  ,blühen'  in  aksl.  pro-cvhtg,  -cvisti  ,erblühen,  blühen', acech.  ktvu,  kvisti-^  ablaut.  aksl.  cveH,  öech.  kvH  usw.  , Blüte';  daneben  slav. *kv'btHi  in  russ.-ksl.  cvtteti  ^blühen'  und  skr.  cävtjeti  , blühen'  (=  lett.  kvitet).
WP.  I  469  f.,  Trautmann  147  f.,  310  f..  Osthoff  ZONF.  13,  3  ff.
f.
\    kuek-  (nasaliert  kuenk-) :  kuk-  , klaffen'.
Ai.  svdncate  , öffnet  sich,  tut  sich  auf,  ucclivaidkd-  m.  ,das  Aufklaffen, Lücke,  Scherbe,  Sichauftun';
lit.  §üke  f.  , Scharte',  sixkos  PI.  ,Kamm',  lett.  suka  f.  ,Bürste,  Striegel' (wohl  aus  ,*Kamm'),  suk'is  m.  , Scherbe',  sukums  m.  ,Lücke;  Scharte';
slav.    *s^ceth   f.    in   polab.    sacet   ,Borste,   Bürste',    sloven.    sc^t   , Bürste', russ.  S^eth  ,Borste'. I  WP.  I  470,  Trautmann  309  f.,  Kuiper  Nasalpräs.  142.
kuel-  ,schlammig'?
Arm.  §alem  ,feuchte,  benetzte,  bereitete  Mörtel',  äaiax  ,Lehm,  Schlamm, Mörtel'  {-al-  =  l  oder  ^l)  ]  lit.  svelnüs  ., weich,  sanft  anzufassen*  ? WP.  I  473.
630  •
kuelQk-  oder  kelok-,  koldk-  , Ballen,  Büschel,  Polster*.
Ai.  kürcd-h  m.  ,Büiidel,  Ballen,  Büschel',    lat.  culcita  ,Kissen,  Polster«. : s.  2.  kuelp-  , wölben'. WP.  I  473,  WH.  I  302.
I.  kuelp- j  kuelb- :  kulpl b- :  klup/b-  ,mit  den  Knien  einknicken,  stolpern, traben'.
Gr.  ytdXTtf]  ,Trab'  (*x/c«X^a,  *kulpä)',
nhd.  holpern^  mdartl.  holpeln,  liülpen,  holpel  ,ungeschickter  Mensch'* unter  Annahme  sekundärer  Hochstufe  ^Ideupjh-  hat  man  got.  h
```


### [2026-09-06T20:35:11.468Z] TOOL RESULT

```
34174:lower jaw bone '; derived: Old English ceace. Old Frisian ziakei. {*keukdn) and Old Frisian 
77407:skeUti^-, skeud-, skeug-, skeuk-. 
---
47261:*) According to WP. I 341 , 348 f., 399 mentioned roots khad- "bite', khabh- : khobh-
```


## [2026-09-06T20:35:18.236Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== POK_02 leaf 257 ==\"; awk 'BEGIN{RS=\"\\f\"} NR==257' POK_02.txt | head -50",
 "description": "Print POK_02 leaf 257"
}
```


## [2026-09-06T20:35:18.571Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '47240,47290p' POK_full.txt",
 "description": "Print POK_full khad- context"
}
```


### [2026-09-06T20:35:20.272Z] TOOL RESULT

```
== POK_02 leaf 257 ==
 bloßes  k-  wohl  durch  bereits  uridg. Vereinfachung;  kup-ro-s  , erwünscht';  kuQpo-s  ^Dunst^ Ai.   hüpyati   (=  lat.  cupiö)   , gerät   in  Wallung,    zürnt',    Jcöpa-   m.  , Auf- wallung, Zorn',  Tzöpdyati  , erschüttert,  erzürnt';  cöpati  ,bewegt  sich,  rührt sich';  hapi-  (unbelegt)  , Weihrauch',  wozu  als  ,*rauchfarben'  Jcapild-,  hapUd- ,bräunlich,  rötlich',  auch  Tcapi-  m.  ,Affe';
alb.  hapitem  ,atme  schwer'  (wie  lit.  hüpuoti)]
gr.  "^aTtvög  , Rauch',  hom.  dcTtd  de  ipvx^v  iy.d7tvaaev  , hauchte  aus'  :  ytdjtvg und  KdftOQ'  Ttvev^a  Hes.,  y^y,7]q)s'  TsdT7jy,s  Hes.,  v.eyiaq)7]ÖTa  Hom.  ,aushau-  -, chend' ;  zur  Dissimilation  von  *Jcuap-no-s  zu  TcaTtvög  vgl.  Schwyzer  Gr. ' '' Gr.  I  302;
lat.  cupiö,  -ere  ,begehren'  (=  ai.  Jcüpyati),  cuppedo  =  ,cupldo',  auch cuppes  ,lüstern,  bes.  auf  Leckereien',  cuppedium  ,Näscherei,  Leckerbissen'; umbr.  Cubrar  ,Bonae^  sabin.  cuprum  ,bonum'  (,*erwünscht,  begehrens- wert' mit  passivischem  Formans  -ro-  wie  clärus  usw.) ;  vapor  , Dunst, Dampf,  Brodem',  alt  uapös  (*huapös) ;
air.  ad-cohra , wünscht'  (*-]cuprat)j  Verbaln.  accobor  (^ad-kupro-)  ,  Wunsch', Thurneysen  Gr.  139;
got.  afhapjan  (*kudb-  neben  sonstigem  *kudp-)  , ersticken,  auslöschen', afhapnan  , erlöschen'  ( :  äno-Y.aTtvo)),  mhd.  verwepfen  , kahmig  werden,  vom Wein',  nisl.   hvap  ,dropsical  flesh';
lit.  kväpas  m.  ,Hauch,  Dunst,  Wohlgeruch'  (:  lat.  vapor),  kvepiü,  -Ui , duften'  (-g-  kann  balt.  Ablautneubildung  sein),  kvepiü,  kvlpti  ,hauchen', lett.  kvept  ,qualmen',  kvepes  PI.  ,Hauch,  Qualm,  Ruß',  kvepet  ,räuchern', ablautend    lit.    küpüoti    ,schwer    atmen',    lett.    küpet    , rauchen,    dampfen.
597
stäuben^  kuplnäties  , aufgehen  (vom  Teig)',  Jcupt  ,gären',  apr.  hupsins  ,Nebel' (Ableitung  von  einem  es-St.  wie  lat.  vapor);
aksl.  hypljg,  kypeti  , wallen,  überlaufen',  JcypTb  ,locker,  porös',  cech. hyp'ry  alt  , strebsam,  emsig,  frisch';  klr.  Jcväpyty  ia  ,sich  sputen,  eilen'; mit  (idg.)  geschwundenem  u  russ.  Jcöpoth  {^Tcojput-)  f.  , feiner  Ruß,  Staub', Icoptith  , mit  Rauch  schwarz  machen,  räuchern';  vielleicht  aksl.  hopr^  ,Dill' (riechende  Pflanze;  s.  Berneker  564).
WP.  I  379  f.,  WH.  I  312  f.,  Trautmann  147.
kejjero-,  köuero-  (auch  sküro-?)  ,Nord,  Nordwind'.
Lat.  caurus  (cörus)  ,Nordwind'  {*kduero-)]
lit.  sidure  f.  ,Norden',  Haurys  m.  , Nordwind';
abg.  sever^  (*keuero-)  ,Norden';
hierzu  vielleicht  ablautend  und  mit  anlaut.  s-:
arm.  curt  ,kalt;  Kälte,  Schauer'  (*skür-do-) ;
aisl.  ahd.  skür  ,Ungewitter',  nhd.  Schauer ^  afries.  as.  ags.  scür,  sceor , Schauer',  got.  sküra  windis  , Wirbelwind',  norw.  dial.  skeyra  (*skauriön-) , Windschauer',  skjera  (*skeurön-)  ds.,  norw.  skeyra,  sküra  ,blindlings  auf etwas  losfahren',  aisl.  skyra  , schnell  dahinrennen'.
WP.  I  377,  WH.  I  190,  0.  Szemerenyi  KZ.  70,  65.
keuk-  , leuchten,  hell,  weiß  sein,  glühen'.
Ai.  söcatij  iucyati  ,leuchtet,  glänzt,  glüht,  brennt,  leidet  heftigen  Schmerz, trauert',  iocdyati  ^entzündet,  betrübt;  ist  traurig,  beklagt',  s
```


### [2026-09-06T20:35:20.316Z] TOOL RESULT

```
Meaning: interjection of laughter 

Note: with partly einzelsprachlicher neologism 

Material: Old Indie /ra/r/75//(Gramm.) 'laughs'; Armenian xaxank^ laughter', gr. Kaxa^w 

(from *xaxa^u)) ' laugh loudly'; Latin cachinno, -are'io laugh aloud, laugh immoderately', 

cachinnus ' laughter '; (under the influence of common Celtic -ns-, -nt- > -nn-), Old High 

German kachazzen, kichazzen. Old English ceahhettan^ laugh loudly '; Old Church Slavic 

etc. chochotati6s.; compare Lithuanian kikenti, kiknotT giggle '. 

Similar to onomatopoeic words kak-^ flout, show scorn, mock ' in gr. kpikq^u) " abuse, 
revile '; Old High German huohon^ mock, scoff. Old Saxon hohi-ITk^ laughable'; with 
Germanic -Ar-: Old English hocoru. " derision '. 



*) According to WP. I 341 , 348 f., 399 mentioned roots khad- "bite', khabh- : khobh- 
"feeble', khend^6\g' are not to be proved as Indo Germanic, just as little as those from 
Specht (Indo Germanic Dekl. 263, Anm. 4) set /r/7a-/77c»- "crooked'; 

those mentioned by him (see 256) Old Indie Beispiele khalati-, kharva-, khara-, khanda-, 
khora-axe all not of Indo Germanic origin. Old Indie khadati' bites to pieces, chews ', 
npers. xayadti^s., could belong to Armenian xacanem^\i\\.Q\ but also with secondary 



expressive Aspiration as *knd-\.o Lithuanian kandu'b\\.e' (somewliat different above S. 
560). 

To the same root root Ae/7- (above 559 ff.) could belong Old Indie khanatT digs ', Inf. 
khani-tum, participle khata-{*khn-to-), together with the neologisms kha-v\. "cave', a-khu-^ 
mole ', /r/7a- "stream, brook'= Avestan Nom. Akk. PI. xa6s.\ Old Indie khanf-^ burrowing ', 
f. " mousehole, entrance to the burrow of a mouse ' = Avestan Aa/7/- "ditch, trench, 
channel'; Avestan Old pers. /ra/7/7-"dig' (/r-from /r/7-from the compounds with us-, ham-). 

Maybe in -m- formant etymology in alb. Tosc f. {*kamur-is) hamuridhe " mole ' > Geg m. 
urithi^ mole ' ; common alb. Avestan k- > h-. 

Note: 

The inanimate suffix -ur- . alb. Tosc {*kamur-is) hamuridhe^ mole ' : UAupioi , oi, lllyrians, 
lAAupia , n, lllyria, also'lAAupi^ , n. Adj. 'lAAupiKO^ , n, 6v, lllyrian: -kx\, the region or province 
of lllyria, 'lAAupi^io , speak the lllyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 

The aniautfrom gr. Kocpav, Kncppv "drone', K(j0(p6(; "dull, deaf is doubtful, also from Church 
Slavic chab/t/" spoW , chabenb " woeful, wretched, miserable ', as also the from Church
```


## [2026-09-06T20:35:29.199Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== leaf 258 ==\"; awk 'BEGIN{RS=\"\\f\"} NR==258' POK_02.txt | head -40",
 "description": "Print POK_02 leaf 258 (p.597-598)"
}
```


## [2026-09-06T20:35:30.208Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 292 293 294 295; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt | grep -n \"khad\\|63[0-9]\\|xayad\\|kandu\" | head -20; done",
 "description": "Locate Pokorny p.634 khad footnote"
}
```


### [2026-09-06T20:35:30.779Z] TOOL RESULT

```
== leaf 258 ==
öka-  m.  ,Glut, Flamme,  Schmerz,  Trauer',  suci-  , leuchtend,  glänzend,  rein',  ,^ukrd-,  sukld- ,licht,  weiß,  rein',  sukti-  f.  , Muschel,  Perlenmuschel,  Perlmutter'  (wenn ,*glänzend'),   vielleicht  siüctd-  , sauer'  (wenn  ,brennend  von  Geschmack') ;
av.  saoSint-  , brennend',  sao^ayeiti  ,inflammat  =  incitat',  npers.  söxtan , anzünden,  verbrennen',  av.  upa-suxta-  , angezündet',  ätrd-saoka-  m.  ,Feuer- brand',  np.  sog  , Trauer,  Kummer'  (arm.  sug  , Trauer'  ist  iran.  Lw.);  av. suxra-  ,leuchtend  (vom  Feuer)',  np.  surx  ,rot';
gr.  xuxvog  , Schwan'  als  ,der  Weiße'.
WP.  I  378.    Erweiterung  von  2.  keu-.
keuk-y  kuk-  , durcheinandermischen,  wirbeln'??
Gr.  -avüsd)}'  , Mischtrank',  xüxcrw  , rühre  ein,  mische',  v,vx7]-d^Qov  ,Rührkelle' ; lit.  §dukstas  , Löffel',  siUksmes  , Geröll,  Auskehricht',  HukHüs  ,mit  Spreu oder  Kleie  gemischt'.    Sehr  unsicher. WP.  I  377,  WH,  1  218  f.
598  9
kik-  ,Häher';  Schall wurzel.
Ai.  Ä;iH-,  hihidlvi-  m.  , blauer  Holzhäher'  {l  nicht  zu  c  zur  Festhaltung der  Schallnachahmung) ;
gr.  yiioaa,  att.  x/rra  (*xfXA-a)  , Häher':
ags.  Mgora  m.,  higore  f.  ,picus  (Elster  oder  Holzhäher)',  mnd.  heger n.  , Häher',  ahd.   hehara  , Häher'.
WP.  I  451.
I.  kik-  etwa  ,Riemeii'.
Ai.  sie-  f.,  sikya-  n.  , Schlinge,  Tragband',  säiTcya-  ,damasziert,  eigentl. mit  Schlingen  versehen';
gr.  üiGaaqog  und  xiacfdg  ,Efeu'(?),*
lit.  siJcsnä  , feines  Leder  zur  Verfertigung  von  Riemenwerk,  Riemen'.
WP.  I  451.
2.  kik-  , tröpfeln'.
Ai.  §lkdra-  m.  , feiner  Regen',  silcäyati  ,tröpfelt';   norw.  higla  ,tröpfeln', higl  , feiner  Regen'. WP.  I  451.
kiker-  u.  dgl.  , Erbse';  kaum  indogermanisch.
Arm.  sisefn  , Kichererbse'  (scheint  Jceiker-  oder  Jcoiker-  fortzusetzen);
gr.  (maked.)  y,UeQQOL  (so  für  überliefertes  mßsQQOt  durch  die  alph. Reihenfolge  gefordert)'  (bxQol.  May.sdöveg;  gr.  xgLÖg  , Kichererbse'  (wird aus  ^KLXQiög  dissimil.  sein);
lat.  cicer  , Kichererbse';
[lit.  Jceke  , Traube',  lett.  h'ekars  ds.  scheinen  dagegen  mit  lett.  h'eUis , Dolde,  Traube',  Lituanismus  zu  lett.  cekulis  ,Zopf,  Troddel,  Quaste, Strauß,  Büschel',  cecers  , Krauskopf'  und  cech.  ^eceriti  , struppig  machen, kräuseln'  eine  verschiedene  Sippe  zu  bilden.]
WP.  I  451  f.,  WH.  I  212.
klon-  (kison-?)  , Säule';  nur  arm.  und  griech. Arm.  siun  =  gr.  xlcüv  , Säule'. WP.  I  451.
kiph-  , dünner  biegsamer  Zweig  oder  Wurzelteil'?
Ai.   siphä   ,dünne  Wurzel,    Rute';   gr.  messenisch   xicpog   n.    ^arecpavog'] allenfalls  auch  lett.  sipsna  ,starke  Rute',  lit.  Hpulys  ,Holzspan,  Holzscheit'. WP.  I  452.
599
Jcistä  .geflochtener  Behälter'?
Gr.  y.LGT7]  , Kisten,  Kasten'  (daraus  lat.  cista,  cisterna)] ==  air.  cess  f.  ,Korb,  Hürde'  (vgl.  ro-cess  , wurde  gefloch
```


### [2026-09-06T20:35:32.636Z] TOOL RESULT

```
=== leaf 292 ===
13:632
=== leaf 293 ===
14:633
=== leaf 294 ===
=== leaf 295 ===
```


## [2026-09-06T20:35:39.123Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==294' POK_02.txt | head -30",
 "description": "Print POK_02 leaf 294"
}
```


### [2026-09-06T20:35:40.820Z] TOOL RESULT

```
*  (zum  i-St.  geworden  in  lit.  dial.  sunis,  lett.  suns, apr.  sunis  ,Hund*) ;  ^Form  lett.  suntana  ,großer  Hund' ;  lett.  kuna  ,Hündin' wohl  mit  westidg.  Gutt.,  Trautmann  Bsl.  Wb.  310?  oder  das  Ä  von  kuca ds.  (Lockruf);  vgl.  Büga  Kalba  ir  s.  I  196;  ganz  fraglich  aber  russ. poln.  suka  , Hündin';
toch.  A  kuj  Obl.  korij  B  Nom.  ku.
Die  Bedeutung  von  lat.  canis  als  ,unglücklicher  Wurf  beim  Würfelspiel' kehrt  in  gr.  xvcov  wieder,  sowie  in  ai.  Sva-ghnin-  eigentlich  ,Hundetöter', d.  i.  ,der  die  schlechten  Würfe  vermeidende,  gewerbsmäßige,  auch  unred- liche Spieler' ;  vgl.  auch  gr.  y,ivdvvog  , Gefahr  (*Hundswurf)'  aus  *y,vv-dvvogy zu  ai.  dyütd  , Spiel'?  Schwyzer  Gr.  Gr.  1,  335  oben.
WP.  I  465 f.,  WH.  I  152 f.;  Kurylowicz  Accentuation  19;  nach  Specht Idg.  Dekl.  32,  121  f.  Ableitung  von  der  Farbwurzel  2.  keu-,  S.  594.
ktires-,  kuers-,  kurs-  , Gehölz,  Baum'??
Gr.  TtqXvog  , Steineiche',  falls  aus  *Ä;wfs-7io-s(?)  :  ^aX\.  prenne  ,arborem  gran- dem',  cymr.  corn.  bret.  prenn  ,Baum'  (*ku7'es-no-)',  ablaut.  air.  crann (*kurs-no-),  Gen.  cruinn  ds.,  cymr.  prys  (prysg)  , Gehölz'  (*kurs-to-)  ]  ags. hyrst  , Gebüsch,  Gehölz',  as.  ahd.  mnd.  hörst,  hurst  ds.,  nhd.  Horst ,Raubvogelnest'  (*ku2's-to-',  weniger  wahrscheinlich  oben  S.  548);  slav. *chvorst^,  ksl.  chvrastije,  russ.  chvörost  ,Reisig,  Strauch',  slov.  hrdst  , Eiche* (*kuors-to-?),  mit  unerklärtem  Anlaut.
WP.  I  524,  Morris- Jones  Welsh  Gr.  128,  Machek  Slavia  16  (1939),  182  f., Mikkola  ürslav.  Gr.  177.  J.  B.  Hofmann  (Etym.  Wb.  des  Gr.  284)  be- trachtet gr.  TZQLvog  wegen  des  kar.  ON  nglraaaog  als  vorgriechisch-klein- asiatisch.
Kh.'
kba  kha!  Interjektion  des  Lachens;  mit  z.  T.  einzelsprachlicher  Neu- schöpfung.
Ai.  hdkhati  (Gramm.)  ,lacht';  arm.  xaxank  , Gelächter',  gr.  xcr^d^cü (aus  *xax«?w)  flache  laut';  lat.  cachinnö,  -äre  ,hellauf  lachen',  cachinnus , Gelächter';  ahd.  kachazzen,  kichazzen,  ags.  ceahhettan  ,laut  lachen';  aksl. usw.  chochotati  ds. ;  vgl.  lit.  kikenti,  kiknoti  ,kichern'.
Ähnliche  Schallwurzel  käk-  ^auslachen'  in  gr.  xijxa^w  ,schmähe';  ahd. huohön  , spotten,  höhnen',  as.  höhi-llk  ^lächerlich';  mit  germ.  -k-:  ags. hocor  n.  , Spott'.
WP.  I  336,  WH.  I  126.  Vgl.  oben  S.  497  Jia  ha.
^  Die  bei  WP.  I  341,  348  f.,  399  angeführten  Wurzeln  khäd-  ,beißen',  khähh-  :  khöbh- jkraftlos',  kherw  ,graben'  sind  nicht  als  idg.  zu  erweisen,  ebensowenig  das  von  Specht (Idg.  Dekl.  263,  Anm.  4)  angesetzte  khä-mo-  , krumm';  die  von  ihm  (S.  256)  angeführten ai.  Beispiele  khalati-,  kharva-f  khara-.  khanda-,  khora-  sind  säm
```


## [2026-09-06T20:35:55.945Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p.161,165,167 (leaf = printed+21 -> 182,186,188) ===\"\nfor n in 182 186 188; do echo \"--- leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done",
 "description": "Print Horn pages 161,165,167"
}
```


## [2026-09-06T20:35:56.794Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p.104 (leaf 125) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==125' HRN.txt\necho \"=== HUB p.227 (leaf 237) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==237' HUB.txt",
 "description": "Print Horn 104 and Hübschmann 227"
}
```


### [2026-09-06T20:35:57.498Z] TOOL RESULT

```
=== HRN p.161,165,167 (leaf = printed+21 -> 182,186,188) ===
--- leaf 182 ---
- 160 —
kurd. stün, istün\ af/. stan.
Die indogermanische Grundform ist nach Hübsch-
mann, ZDMG. 39, 93, "^'sthlnä-; dagegen siehe zuletzt
J. Schmidt, KZ. 32, 385 folg.
722. fiite^ *Kampf, Krieg*, süeziden,
aw. vergl. stij- *Kampf, Streit'; phlv. stej 'Kampf*
(Bund.).
Wohl zu ai. l/^t^J-, tejate 'scharf sein, scharf werden',
vergl. Desid. titiksati *sich scharf zu machen suchen,
sich zu stählen suchen gegen Etwas, d. h. Wider-
stand entgegensetzen ; gr. ötCQm, lat. in\stigärey
germ. i^stek-^) (as. stekaUy ahd. stehhan, got. staks
'Mal, Wunde').
723. sey(t 'hart, fest; sehr, se/ß.
ai. [/^^ak-, gaknoti 'vermögen, können*, skr. qaktä-
'vermögend*; phlv. sayt^ saxtak]tum (vd. 19 (47)).
bei. sak 'hart, stark, fest' (383); yidg. sukt.
V
72 t. sw/un, SU/m (Sahn. I, 29 V. 117 neben -ww, ebendas.
V. 109) 'Wort, Rede*.
Käs. K. siixan[6ni,
aw. sax'Ore (Y. 29, 4), säx^em (y. 53, 5) ('Plan, Rat,
Rede' (Bartholomae, Ar. Forsch. III, 36, 37); phlv.
sa/wi 'Wort, Rede'.
725. sed (heute geschrieben sed; AM. sed, S. 7 Zeile 15,
aber sed, S. 8 Zeile 4) 'hundert'.
aw. safa- 'hundert*; phlv. sat; ai. gatd-,
kurd. sed; af/. sal, sil; oss. sädä (218); wa;^. sar.
LW. sad.
720. ser 'Kopf; vergl. serapa 'Ehrengewand' ^).
aw. Sarah' 'Kopf; phlv. sar^ asar 'endlos' (aw.
anayra-); ai. ciras- 'Kopf; arm. sar 'Höhe, Gipfel,
Abhang' (H. No. 247).
'J Übertritt in die e-lleihe Ca. bei Feist, No. 531).
^) oiiottnts (llesycb), de Lagarde, Ooa. Abb. 208 (?); vergl.
Miklosiob,' Dcnksobr. WAW. Band 3S, 20.
--- leaf 186 ---
- 164 —
743. seg *Hund'; vergl. arab. sij[ihistan d. i. np. seglpistän
'Fructus Cordiae Myxae , Sebestenen , Brustbeere*
(AM. 155).
g. saha^ sewä; Semn. eshe (vergl. Vullers ispnh,
ispehj isbähy Isbeh) ;täl. sipä'^); Käs. eshd^ espa.
niedisch^) (Snd^a (r^yr y,vva y.dkhovöi anuna M^Jb/),
Herod. I, 110; aw. span- Hund'; phlv. aak^ sag; ai.
cvdn-; arm. sun (H. No. 224).
kurd. seh (d. i. se) *Hund', Plur. sän, seiän; afy. spai.
744. »ffgtir^ sngvrne, stiyvr 'Stachelschwein'. Si/uL sJ/ttr,
g. si/ttr.
aw. sukuruna- (zu den Hundearten gezählt); phlv.
sukur (Thonnelier).
kurd. LW. st/ör; af}'. sktlnr, skön (Dar niest et er,
Ch. pop. 8 45 ; ebendaselbst baragsta (Dialekt des
Distrikts VazTrl) snkal); bei. sikun^ n. sl/un \Stachel-
schwein' (345).
745. {\)fiuniy sumh^) *Huf.
aw. vergl. safa- 'Huf; phlv. suinb, arm. LW. smhak;
ai. vergl. QapUä' 'Huf*; an. hüfr, nhd. Hüf,
kurd. LW. shn; af;. sioa gespaltener Huf, LW.
sum; oss. säffäg *Huf, Klaue' (224); wa;^. sar. LW.
süm.
Eine Urverwandtschaft ist sicher zwischen aw.
safa-, ai. (japhd-, afy. swa^ oss. säffäg einerseits und
np. surn^ snmh andererseits anzunehmen.
746. {2)sumi^ sunb 'Höhle, Loch*, smnhiden^).
kurd. so7ifin^ LW. sümb^)^ stitfib^) (H.-Sch.),
sumbtden^); bei. LW. (?) sumb Xoch', snmhag, n.
sumbay *bohren, stechen (351, 352).
Zu np. sufte^i (No. 740).
*) Vergl. hyrkän. spas bei de Lagarde, Ges. Abh. 226, 227.
*) D. i. wohl auch ap. (vergl. Hörn, Indog. Forsch. II, 137), da
die dialektischen Formen doch nicht sämmtlioh medisch sein kennen.
') Sieho vorige Seite Note 2.
--- leaf 188 ---
- 16() -
Käs. Q. bdsüy, Causat. sujünüden, K. bisiij^ Z. bosot,
aw. l/'saoc-, saoöayähi 'anzünden', atare. |saofca- Teuer-
brand', saocant' 'brennend'; phlv. sö/tan, Praes. söcem
(päz. sözet), söc(i)sn, söcäk (vd. 8, 253), söclmtan ; ai.
l/"(;öc-, gocati.
kurd. sötm^ ez disuzim brennen* ; afy. sezal, sejal '),
smjavul; oss. d. sojun^ t. s^/i« Verbrennen (226);
bei. sucarj^ n. s?«5ay intr. 'brennen (349), söcag ^ n.
sösay trans. 'brennen* (358) ; wa/. LW. säz^ sar. srfw^
'Brand'.
751. 8üd 'Nutzen, Vorteil'.
g. sid 'Zinsen*.
aw. [/'saV' 'nützen'; phlv. süt , sütih, sütömand,
sütlnUa/L
bei. sät, Sit (357); sonst allgemein entlehnt.
752. Süden 'reiben', Praes. säy-em, sät/lden.
ai. l/'cd' 'wetzen, schärfen .
kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
Die Bedeutung ist im Neupersischen verblasst ;
vergl. aber das Kurdische.
753. sür *Fest, Gelage'. •
aw. süirya- 'Morgenessen* (Darniesteter, Et. ir.
II, 161 und Geldner, KZ. 25, 531 Note 228); phlv.
5/Tr 'Morgenmahl, Mahl'.
bei. LW. slr 'Hochzeit, Verlobung' (241) ; siyn. sur
'Gelage, Hochzeitsfest* (die Bedeutung ist hier noch
mehr als im Np. specialisirt).
754. sTirfii, sülax, ^Nt^lD (Is. 11, 8) 'Loch'.
Darmesteter's Etymologie (Et. ir. I, 62) aus
aw. *siifräka' , phlv. "^sufräk , "^suhräk , ^süräk in
säräk]öniand bezw. süläk]ömand ist unmöglich, da im
Aw. nur suwrä- ('Ring' oder Pfeil') vorkommt (vergl.
oben No. 740).
kurd. LW. särä/; afy. sürai^ LW. süläy.
*) Vergl. bezüglich des Vokals Kas. V. bdslz, bäalzün neben
Inf. Hüten, hafilznv (Oftusat.), g. lie.^(Ji(J (3. Sg.), sejeuph 'Tripper*.
```


### [2026-09-06T20:35:59.474Z] TOOL RESULT

```
=== HRN p.104 (leaf 125) ===
— 103 —
(7) Gl.), rTstjayee, ä/ezJt (Phlv.-Vend. für aw. [^ha/s-;
AV.), päz. d/ezed (Men.).
oss. ra]xlzai *du willst herabsteigen', d. s^ezun 'hinauf-
steigen' (301).
Das awestische Wort ist nicht sicher; die Päzend-
lesung mit z beweist nichts.
463. xäm *roh, ungekocht'.
ai. amd' *roh*; arm. huni 'roh' (H. No. 171; vergl.
Bartholomae, Studien II, 44. Daneben LW. /aw)5
gr. (Ojiwc; air. 6w.
kurd. xäv; oss. LW. /öm (Hübschniann, S. 133);
afy. öm, um; bei. hämag, n. häniay, liänvcuj (155);
wa/. yüng,
464. yritnös^) ^schweigend, still*, /ämösl.
skr. a + \/^marS' geduldig ertragen' ; vergl. fcrämös
(No. 812).
465. ^Jiän, yßne 'Haus , xänef/T.
phlv. /ßnak, /an, /änaklk (n''Nn"*2, Nöldeke,
ZDMG. 46, 142).
Von i^khan- 'graben'. Vergl. np. (arab.) yendeq
neben kenden,
466. yi^miT 'Quelle, Wasserbassin , x^^ (unbelegt und un-
sicher 2)).
aw. x^fw-, Nom. ;^äo 'Quelle'; phlv. ;fäw, /ßnlk (Bund.) ;
ai. khiin- [khä-),
kurd. känT, kahm,
467. xäwer {/"äwer) 'Herr.
aw. /'äpara- 'gnädig, barmherzig*; phlv. y^äpar
(Darmesteter, Et. ir. I, 60 Note).
468. ^äye 'Ei*.
phlv. xäyak *Ei' (Men.); arm. Jw *Ei' (unsicher; H.
No. 179); lat. öoiim; gr. rJov; ksl. aje^ jaje *Ei*.
kurd. haik, hl, liek; afy. hä; oss. t. aik, d. aißä
(12); bei. haik (159).
») Reimt auf hös Sahn. I, 429 V. 730.
*J Auch an SteUen wie AM. 240 Zeile 4 v. u. wird man nicht
etwa ;^ä»e *eine Quelle*, sondern ^^änl *die Quelle* (allg.) lesen müssen.
=== HUB p.227 (leaf 237) ===
— 226 —
rdz == ap. raucah-, dazu arm. Roc-vehan (Sebeos 79, 94),
phi. rdcveh 61. and Ind. 140 = np. rozbih gliicklich'; arm.
rocik = np. rdz% *das tagliche Brot'; razan Tenster =
zd. raocana- ; rezam 'giesse aus* , zd. raecay- ; sdzam
*mache', zd. sac H. 688; sazad *ziemt sich', zd. sac? H.
738 ; sdzam ziinde an', zd. saocay- ; sDzan 'Nadel', bal. sucin
u. s. w. H. 755 ; faraz Vorwarts , aufwarts* , skr. prac- ;
kavtz, havnz = arab. qaflz = phi. kapic = arm. kapic
*ein Mass fiir Getreide*, ap. xani&i^ (oben p. 89); gudazam
*schmelze', zd. vi-tac-^ gurezam 'fliehe', zd. vi-ric; giizaram
'vollziehe, bezahle' =^ arm. vcareni, skr. vi-car; guzinam 'suche
aus*, zd. vi'Ci ; guzlr 'Hilfsmittel' = "^vicfya- (oben p. 94) ;
maztdan 'saugen , bal. micag 'saugen ; maviz ^) 'Rosinen' =
hdX.mamc (Geiger, Lautlehre p. 28); moza *Schuh' = arm.
mucak 'kleiner Schuh' ; namaz *Gebet' aus '^namac H. 1040, oben
p. 102 ; namzam 'spiele' (ein Instrument) H. 1046, unsicher,
oben p. 102; ciz etwas aus *czc = *acc, urspr. "^cid-cid,
ap. cisciy; vazlr (arab. LW.) 'Vezir', zd. vlcira- *der die
Entscheidung hat', phi. v{i)c%r , arm. vcir 'Entscheidung,
Richterspruch' (oben p. 94), vgl. Noldeke, Tab. 53, 444;
dihltz, dahliz 'Vorhalle, Halle* = arm. dahlic 'Zelle' (5. Jhd.),
s. p. 263; Vahriz N. pr. Tab. 223 — arm. Vahric (Laz.
Pharp.); Suff. zi in sagzt 'Sake' (s. p. 240), razT Von Rai'
(davon 'Pa^inrfvrj 'Rai' bei Theophylact), tctzi 'arahiscli =
arm. sagcik, phi. racik West, PT. II, 329, arm. tacik (5. Jhd.),
phi. tactk Bdh. Gl. 107 (oben p. 46). Nach r: arztz *Blei,
Zinn = arm. arcic; hargiz = hagirz *jemals' (oben p. 105)
= phi. hakard? H. 1092.
Statt z erscheint jf, in : vaj *sprich !' (dialektisch),
haji = v€l,0 *das leise Recitiren religioser Formeln (der
Parsen !) zu skr. zd. vac 'sprechen , guvctsa 'Schelten' ^= skr.
vivad- (oben p. 104) ; amdj 'Pflugsterz , g. mCLtk, arm. mac (?);
tajar *heizbares Winterhaus', arab. tazar 'Sommerhaus* =
ap. tacara-, arm. tadar 'Tempel, Palast, Haus'; varj 'Grosse,
Wiirde' = zd. varecah-; hujXr — - xujlr = hum' schon' =
zd. hucidra^; noj , noz , noz pinus' = arm. noc, noci
*Cypresse* ; mum, pi. muzgan Augenwimper , bal. micac, also
*) Bei B loch ma nil JASB. XXXVII, 1, 52: mavlz.
```


## [2026-09-06T20:36:09.346Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 183 187 189 126; do echo \"--- HRN leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done",
 "description": "Print Horn leaves 183,187,189,126"
}
```


### [2026-09-06T20:36:10.982Z] TOOL RESULT

```
--- HRN leaf 183 ---
— 161 —
kurd. afj'. bei. (884) sar; oss. sär (220) ; wa/. sangl.
minj. sar.
121. se^'üT, sera *PaIast*.
Wohl zu aw. l/^i^rcl-, ^h'äyeinfi 'schützen , ai. yträ-^
trdyate; phlv. srWitan.
Hierher gehört wohl auch jüd.-pers. HNID 'Vorhof'
(Is. 62, 9), arm. LW. sr»/*, srahak^ arab. LW. surädiq
(de Lagarde, Pers. Stud. 72), aber nicht der lydische
Stadtnanie Sardes (vergl. 6. Meyer, Indog. Forsch.
I, 827).
Allgemein entlehnt.
728. sut% usmh Blei', "P)nD (Jer. 6, 29).
g. aurob.
aw. srn' 'Blei'; phlv. srpin 'bleiern'.
kurd. sirift (H.-Sch.); bei. surup, suruf (855).
729. serhär, sertvär 'Last, die man auf dorn Kopfe trägt .
aw. ^sara.hära- *Kopflast', vergl. sarnharn 'capitum
tegmina' (Isid. t&, 23).
Vergl. No. 726.
730. stir-^ Vot', Suhr[äbj Suhr]esp; vergl. sur/tce^ sur/tze
llöteln'.
ap. Ou/ra- (N. pr.) ; aw. sii^/ra- rot ; phlv. sii/r ;
ai. gukrä' 'klar, licht, hell'.
kurd. sör ; afy. sür ; oss. d. sur/, t. sir/ rot, schön'
(286) ; bei. suhr^ sohr Vot, glühend' (350) ; wa/. sökr.
731. serd 'kalt', sermä 'Kälte'.
g. sart,
aw. sareta- 'kalt'; phlv. sarty sarmäk (Bund.); skr.
vergl. gigira- 'Kälte'; arm. sarn 'Eis*, sahium., sarcim
'gefrieren, erfrieren' (H. No. 245) ; lit. szdlfas 'kalt'.
kurd. sür; afy. sör; oss. t. sald 'Kälte' (219); bei.
.sa/d, n. särf (336) ; wa;^. sür, süri.
np. sei'ma erklärt Nöldeke (mündliche Mitteilung)
überzeugend als Analogiebildung nach germä 'Wärme' ').
*j Lit. szarmä kann ihm also nicht gleichgeaetzt werdon
(Bezzonberger, Beitr. z. Gesch. der lit. Sprache, Ol).
II r II , (jiunUriüM tl. iioup. Ktyiuologpie. 11
--- HRN leaf 187 ---
- 165 -
747. Aeny 'Stein ; Gewicht, Würde', senrjin.
ap. ad^a(n)(jaina' steinern'; phlv. sa{n)(j (P.-V. z. B.
vd. 19 (13)), sang (AV.)
Allgemein entlehnt, z. B. kurd. senk^ seng; af/.
sang ; bei. sing (289) ; sangL. song,
Np. senjJdm (mit sekundärem Infinitiv se/ten —
phlv. sa/tan, sanßt , PP61. ; g. satnmn, Käs. örsaten,
örsatman, verset — PPP. sf?;^^e, Sahn. I, 1 Vers 10)
^wiegen* ist ein sekundäres Denominativum von seng,
Nöldeke (mündliche Mitteilung) schlägt vor, das
altpersische Wort (wie Spiegel, (jlossar) mit an-
lautendem d zu lesen, indem er dieses a in np.
murd]aseng 'Bleiglätte' und must\aseng \Schleuderstein'
wiederfindet. Auch denkt er an Zusammenhang mit
ai. ägman- 'Stein* (vergl. np. rts, No. 22) und (mit
Spiegel und Darmestete r) dem schwierigen aw.
asengöl.gäum (yt. 19, 43)^).
748. sün Stil 'Richtung, Seite', "^ID (Jer. 17, 1).
phlv. sük *Seite, Richtung' 2).
Eine ältere Form ist nicht vorhanden; das np. l
•ff
beruht auf Übertragung (vergl. No. 373). Ursprüng-
lich soft, wie skr. LW. söya- beweist (Weber, Pär.
des Kpn.).
749. suwär, eswär (Lex.) 'Reiter'.
ap. as(s)a]bära- 'Reiter' (doch wohl = *aspabara- ^) ;
phlv. (tsbär 'Reiter, aspwar Ritter (Nöldeke, Karn.
39 Note 2)4).
LW. kurd. suvär ; afy. spör, swör ; bei. sawär (232).
750. sötten 'anzünden, verbrennen, Praes. söz-em^ söz,
nw-^^yü (Qiss. Dan.).
') Zu derselben Auffassung über aw. aaehyö.gäum ist soeben auch
Burtholomae, Indog. Forsch. II, 268 gelangt (Correkturnote).
^) Arab. LW. cahärsüj *Markt', syr. LW. "^IDlNnii^ scheinen
herher zu gehören (ursprünglich *Vierseit, Viereck'); dann etwa auch
die mit s beginnenden, zuletzt von Hübschmann, ZDMG. 46, 247
No. 90 zusammengestellten Worte?
^) Aspa- auch in aw. A8(s)a\hana- {ß. pr.)?
^) Savärdk (vd. 1 (24 J) kann nicht *Reiter* sein.
--- HRN leaf 189 ---
— 167 —
755. Hözen 'Nadel'.
g. sejen ; Käs. Z. sö^ö,
aw. vergl. snlca- 'Nadel'; plilv. säcau (päz. süzan,
sözan) (Bund.); skr. rüka- '(jetreidegranne , Stachel
eines Insekts'.
kurd. mzin^ hezüzin {*sü£in) 'Nadel'; oss. LW. d.
sojine, t. sujtn ^Nadel' (S. 181); bei. sücin, slöin^ n.
slsin^ sisan^ sisin (356) ; wa/. s/c, sar. s'ic.
Das Wort bietet in seinen verschiedenen Formen
mehreres Auffällige. Der np. Majhfilvokal wird durch
Kä§. Z. sözo, oss. sojine neben supn, süjln etc. gestützt,
während die sänimtlichen anderen Formen (besonders
auch das 7, vergl. aber auch S. KiG Note 1) gegen ihn
sprechen. Skr. siict-^ tmöU (schon Ait.-Br., ^at.-Br.)
stehen isolirt. Wenn man mit Tomaschek (Central-
asiat. Stud. 11, 8().'ij Entlehnung aus dem Sanskrit
annehmen will, so dürften aw. snka-, skr. güka-y
np. sök *Ähre, Granne* nicht herangezogen werden.
756. sog 'Trauer, Kummer.
aw. vergl. atare,]saoka' 'Feuerbrand'; ai. röku- ciber
schon in der übertragenen Bedeutung 'Qual, Schmerz,
Trauer neben '(ilut, Brand*'); arm. sug Trauer* (H.
No. 254, nach Bartholomae, Studien II, 17, LW.).
757. söf/end *Eid'.
aw. saokenta]vant' 'Schwefel enthaltend' (vergl.
Geldner, Studien I, 103).
LW. kurd. sö7id 'Eid* ; bei. sauylnd^ sögind (359).
V
758. sTilT, snl 'Pflug* (unbelegt, nur im FS).
Von Justi (Handbuch s. v. sufra-) mit aw. sufrd-
'Pflug* zusammengebracht, was aber nicht vorkommt
(s. oben No. 740).
759. si (geschrieben sih) 'drei', siyum^ seyum (AM.), poiHD
(Is. 37, 30).
ap. I^Httya- dritter'; aw. ^n- 'drei'; phlv. s(i)\tigar
'dritter*, päz. sl ; ai. tri- ; arm. ereU (H. No. 100).
') Vergl. np. ä/efi'i säg (»Sälin. T, 16 Vers 42).
--- HRN leaf 126 ---
1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
«ar. cer, üer, sangl. //tr, minj. xara.
*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
•; Vcrgl. Barthol oniao, ZDMG. 44, 550.
```


## [2026-09-06T20:36:23.814Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"khäd\\|khadati\\|xäyten\\|xäyiden\\|xdyiden\\|/äyiden\\|kauen\" HRN.txt | head -20\necho \"=== awk find page containing 'kauen' ===\"\nawk 'BEGIN{RS=\"\\f\"} /kauen/{print NR\": \"substr($0,1,400)}' HRN.txt | head -20",
 "description": "Grep Horn for chew/xayidan"
}
```


### [2026-09-06T20:36:25.421Z] TOOL RESULT

```
3890:415. Jävf^den 'kauen, zäviden,
3892:phlv. vergl. jütan 'kauen, verzehren' (West: jaldanö),
3894:kurd. /Miw, jün 'kauen'; afy. Sövul, zöyal; he], jfayag,
17609:ly'khäd-, khdilaU 469.
=== awk find page containing 'kauen' ===
115: — 93 —
412. jäme 'Kleid, Gewand'.
ai. V^yam- mit chardis- etc. *ein Dach, einen Schirm,
Schutz überhalten , lett. ju^m-f *dachdecken*, ksl. /)o-
jata 'Dach' (Fick); phlv. jämak bezw. yamak (z. B.
vd. 6 (71) Gl.)i).
kurd. yüma 'grobes baumwollenes Zeug (H,-Sch.);
LW. afy. jama, bei. jfämag (113).
Hörn, KZ. 32, 583 No. 11.
413. Jan 'Leben, Seele', Janver.
aw. daenä' 'Seele, zu [/'dliay-,
```


## [2026-09-06T20:36:42.893Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==125||NR==126' HRN.txt | grep -n \"46[89]\\|xäy\\|/äy\\|khäd\\|kau\" \necho \"--- raw tail of leaf125 / head 126 ---\"\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(repr(t[124][-600:]))\nprint(\"=====\")\nprint(repr(t[125][:900]))\nEOF",
 "description": "Inspect Horn 469 entry region"
}
```


### [2026-09-06T20:36:44.841Z] TOOL RESULT

```
31:468. ^äye 'Ei*.
32:phlv. xäyak *Ei' (Men.); arm. Jw *Ei' (unsicher; H.
--- raw tail of leaf125 / head 126 ---
'belegt und un-\nsicher 2)).\naw. x^fw-, Nom. ;^äo \'Quelle\'; phlv. ;fäw, /ßnlk (Bund.) ;\nai. khiin- [khä-),\nkurd. känT, kahm,\n467. xäwer {/"äwer) \'Herr.\naw. /\'äpara- \'gnädig, barmherzig*; phlv. y^äpar\n(Darmesteter, Et. ir. I, 60 Note).\n468. ^äye \'Ei*.\nphlv. xäyak *Ei\' (Men.); arm. Jw *Ei\' (unsicher; H.\nNo. 179); lat. öoiim; gr. rJov; ksl. aje^ jaje *Ei*.\nkurd. haik, hl, liek; afy. hä; oss. t. aik, d. aißä\n(12); bei. haik (159).\n») Reimt auf hös Sahn. I, 429 V. 730.\n*J Auch an SteUen wie AM. 240 Zeile 4 v. u. wird man nicht\netwa ;^ä»e *eine Quelle*, sondern ^^änl *die Quelle* (allg.) lesen müssen.'
=====
'1-4 -\nHüb.sohniann. Zr»Mü. :>. 42o.\n47<.». \'/jtjeffte *^\'e^tÄ\'i>.-T. jiüoklich". ver^l. fer[jriijeste.\naw. \'\'h*\'i:t.<t\'i\'. Yrr^\'l. aj\'i^f\'t\'. p^hlv. 4/a^ (Gemme\n.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).\n471. \'/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür\nitürk. /itnL\'für. v.-ii:]. NOMtrkt: bei Uübschmann.\n<>^at\'t. Elvi]]., r!^. l:\'.:\'.!. //tC\'.ni, /i\'Uc,\naw. vt-ri:l. x\'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.\n/\'td\'iiw ai. Ytriji. >cj*iiid\' Selbst I-Hrstininiung\'.\nLW. kiipi. ;f<^\'r: af;. x\'*\'inii Oss. ;rwföi: bei. /*«*\'*»\nn. /»»(t*\'!. /i \'<»>\'// i\'..«oi.\nDie Diirchsichtiirktrit Jt.-s Zusammenhanges mit l\'^</*\'\nhat wohl Jas d i:eschützt : als Grundform ist etwa *?**\naw. /\'adöffii\' löder */»iit)\'.*y\'i-| anzusetzen. Nöldeic ^\'\nG^\'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^\nEtvmoloKit\' vielleicht nicht mit L\'nreeht.\nFr. Müllers Erklärung jWZKM. 5. 6b) aus av^\n*/'
```


## [2026-09-06T20:36:59.432Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^469\\|469\\.\" HRN.txt | head -20; echo ---; sed -n '17600,17615p' HRN.txt",
 "description": "Grep Horn for entry 469 references"
}
```


### [2026-09-06T20:36:59.491Z] TOOL RESULT

```
9930:469. Dazu se/üden zerkratzen' (Sahn. I, 222 Vers 1659,
17609:ly'khäd-, khdilaU 469.
19365:/«/w 469.
---
H-, ijniiiti 833,
irs-, karsaii 859.
aj-8-, frj-srfii 83ft
l^khm
■ 83l', 832, 884.
;-, fcäfo/g 40.
+ e> 940.
kbdn- (khä) 46«.
fc;-oj-a- 461, 473.
ly'khäd-, khdilaU 469.
I i/'gad- 934 ADm.
Iffnrfa- .92.
. gnndhd- 934.
l^y,™- + ni 10G3.
1 ll/j/oi--, yrnöfi 916.
. +jH-»ii 358.
```


## [2026-09-06T20:37:04.082Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19355,19372p' HRN.txt",
 "description": "Print Horn NP index context"
}
```


### [2026-09-06T20:37:04.126Z] TOOL RESULT

```
Arn 84a
A-mZ/im- 863.
ktut 874.
^•M^A• 848.
kuruM 850.
A;</j<ä>i 694.
Aviii 489 Anm.
kustin 855.
A-üti^i 875.
qiu 852.
/«/w 469.
Xän 498.
/ö/- 496.
Xitsrü 487.
;f<'«U 487.
;fCiMr 486.
j((iv 463.
xevin 495.
```


## [2026-09-06T20:37:13.647Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT saokenta ===\"; grep -n \"saoket\\|saokent\\|saokənt\\|saoka\\b\" BRT.txt | head -20\necho \"=== BRT suxra ===\"; grep -n \"suxra\" BRT.txt | head -10\necho \"=== BRT xad ===\"; grep -n \"^xad\\|xad-\\|1xad\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T20:37:13.716Z] TOOL RESULT

```
=== BRT saokenta ===
21447:yazamaiäe  amaheca  paitt  hutälfahe  Yt.S. 12;  y-i35f-.  '4-2S,  15. 1,  16.  s,  V.16. 10.  n)  mit  sachlichem  Objekt  '(tin Gebet)  beten,  den  Göttern  weihen,  (ein Opfer)  darbringen,  weihen';  von  yasna- (Sp.  ia7i  m.,  Stverz,):  yasmm  *yazäiti N.  23;  —  yJ  yasmm  *yaanti . .  ham.irut.- väeayä^a  (sd.)  *yaa?nti  *va  .  .  N,  24;  — yasmm  yas?ntfm  N.  22;  —  *yasmm *yax3mnahe^.20;  —  äar^yjmca  yasmm yazänB  Yt.  so.  138;  —  y^  •  ■  mazist?m yasmm  yataUe\X.i.ti\;  —  sonst:  paitt  nö eati%rä  vTsanuha  paitt  Aisyastä  vTsanuha YL  /O.  32;  —  yasca  .  .  bayqm  ahvnaht vairyehe  . .  yazüite  Y.  ig.  6.  III)  ohne Objekt  'beten':  yasäi  saoka  (Vok.)  vanuhi V.  22.  3 ;  —  da%ai  ahmai  tat  avaj  äyaptam aridi'i  .  .  arfdrai  yaz^mnsi  Jaihyantai Yt  5.  19;  if.  ai,  Ny.^.  11;  —  gakäbyJ spmtäbyS  . .  zbayems  yizamadaica  nipäta- yaica  .  .  Y.ji.ii;  11;  —  dä^rls  ahmäi venu  :^armS  yö  hls  yazänS  .  .  zbayetti Yx..  13.24.  a)  insbes.  vom  Zaotar  svr. 'Gottesdienst  tun':  apu  gätava  rämUihioim yavata  zaota  yazüite  Y.  %.  9;  —  ktikra baväl  hitö.kizvä  yezi  anarike  (sd.)  yazüite (näral.  zaota)  Y.  6j.  9;  —  yazata  zaota üsu.yasnS  b?r»zi.gä%rS  btrizata  vaca  Yt. /o.  89;  —  müvayaca  zao^re  yazimnäi Y.6S.I2;  —  aei  zaotanm  yaztmn)m YLj.  132;  —  mit  Dat.  comm.:  ahmäi naire  .  .  yahmüi  zaota  .  .  frastgratüt  paitt iansmm  ..yazaite  Yt.  JO.  137.  Undeut- liche Stellen:  yat  yazanti  yai  vä  hqm.- rashwayanti  N.  62;  61;  —  tarö  yasmm haptar^häitlm  *yazfntfm  N.  65; —  *ya- Zimna  kat  nü  kakat  SI.Ä22.
23743:■  j.  vsrazi.saoka- Adj. 'wirksamen  Nutzen schaffend,  tatkräftig  fördernd':  'ka  (statt NSm.)"'  nqma  ahmi  Yt,  t.  15.
25806:saoka-
25816:•  j.  saoka-  n.,  saokä-  f.  'Nutzen,  Vorteil': ya'&a  azsm  uzbaräni  haca  datvaiihyB  uyl Istiica  •iJi-a  YL5.  a6;  —  •kqmca  barat.- avarftqm  baratäyaptqm  asaonJm  Yt  rj. 4j;  —  'ka  ahmt   saokavastamS  YtJ4l.3J
25822:•  j.  saoka'vant-  Adj.  'Nutzen  bringend, nuUvoU':  mhnhtm  .  .  'va/iüm  .  .  baytm ^^  7-  5j  —  'vant?m  bavahi  ya%a  müahitn Vyt4.
25824:•  j.  saokavaa'tema-  Adj.  'der  am  meisten Nutzen  bringt,  schafft':  saoka  ahmi  Hims
=== BRT suxra ===
9395:•  ].  karsvar-,  -van-  n. 'Kreis' der  Erde,  vgl  iasuxra%',i,an:  —  V\,tkctdiakxraihimi 'Erdteü'":  />//«/  -^.^r»  j-«/  x^aniraiim\  ■  feasu.xraO-wan-  Adj.  (auch  fem.) Yt.i£.i5,^o.i5,67,i33,Y.57-3i.y./p.39,  -der  geringe  Einsicht  besitzt':  noit  ia H.  /.  I4i  -  't'^rp  yat  ar.>zahi  Yt.  i2.  9;  „^i^^a  -^wa  (NSf.)  "nicht  darum  (?)  ein ,„_,..  _  .„./   .,..„  j.^/  vouru.bar»iU:^^^^  ^„„  geringer  Einsicht"  N.40'>.
14297:Vgl.  suxra:  —  ai.  Sukra-  m.  EN.
20223:iß.  19;  28.  7,  34-  11;  —  yqni  xsnstsm ■anöibyä  (sd.)  dk  %ws  a^rä  suxra  'da ayaaha  xSusiS  Y.  57.  9;  —  tat^  'da iiwahml  ä  *dqm  (Sp.  684  o.)  nipanhi manS  vohü  urunasca  ..  Y.4g.  ^o',  34-^i a^qmili  a  ahmt  "^waAml  'da  vTn^si (sd.)  a'ipi  Y._J2. 8;  —  yei  *srasdä  anhen 'däi  Y.31. 1;  —  atca  hui  scantü . .  xlnBm '--'.)  'da  (Gen.)  vahmäi  a  Y.5_j.  2;  45.8; yj  %wat  'da  asmälm  ahinlä  manö yazäi  (sd.)  upa  Y.33.4;  —  andrO  %wävqs (sd.)  ..  'da  Y.43-y,  48.3;  —  'da  '. . %waAya  mq%raris  dStTm  (sd.)  Y.^2.  13; 33.10,34-9,  43-^,  6; —  hada  °da  a/a  maj ärmaitis /imat {sd.)  Y. 48.11;  4,  10,31.10, 3.  J2.  II,  j^.  9,  4^.20,46^.4.  8.  47-3.  4, 49-  2,  3,  50.  3.  5'- 1.  8,  10,  1 1 ;    —    sara-
26357:suxra-  1 583
26373:•  j.,  g.  suxra-  Adj.  'rot',  vom  Feuer:  äal he  Jm  zh  bvat  pirane  .  .  ährqmca  'rqm  " saoantqm  "voll . .  und  von  roten  flammen- den Feuern"  V.  2. 8;  —  Sica  S'hrS  'rä (IS.)  .  .  vaahau  vidäta  rqnayä  (sd.)  Y. 5/.  r9;5/.9.
=== BRT xad ===
10531:•  j.   xad-  V.,   nur  mit   vi  'auseinander quetschen'.     Praes.  2  xala-.
```


## [2026-09-06T20:37:14.906Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n -i \"sōxtan\\|soxtan\\|sōg\\|suxr\\|sōgand\\|sogand\\|xāy\" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "Grep MacKenzie"
}
```


### [2026-09-06T20:37:14.965Z] TOOL RESULT

```
=== PHD ===
PHD.txt:572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
PHD.txt:1740:egg Xāyag.
PHD.txt:3013:oval xāyagdēs.
PHD.txt:3349:red karmīr, suxr.
PHD.txt:3907:swear (oath) sogand xwardan.
PHD.txt:5530:dēnār, dēwār, suxr
PHD_mackenzie.txt:4570:sOgand [S'lvknd I M swgnd, N saugand] oath.
PHD_mackenzie.txt:4581: sOxtan, soz- [swhtn , swe- I M swxt, swe-, N ......] bum.
PHD_mackenzie.txt:4722:suxr [swhl I N surx] red.
PHD_mackenzie.txt:6113:brassard bazabanag.                    burn (vt.) dazidan, soxtan, taftan,
PHD_mackenzie.txt:7195:oath sogand, war.                      ordeal war; heat'" garrnowar(ih).
PHD_mackenzie.txt:7396:quake tandidan, wizandidan.                    red karmir, suxr.
PHD_mackenzie.txt:7717:study (v.) osmurdan.                       swear (oath) sogand xwardan.
PHD_mackenzie.txt:10900:sogand
PHD_mackenzie.txt:10905:                                       suxr
```


## [2026-09-06T20:37:23.856Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== Schwefel ==\"; grep -n \"Schwefel\" BRT.txt | head -10\necho \"== saoc ==\"; grep -n \"saoc-\\|saoč\\|sauk-\\|saocaya\\|saocint\\|saocant\" BRT.txt | head -15\necho \"== xad ctx ==\"; sed -n '10520,10545p' BRT.txt",
 "description": "Grep Bartholomae for sulfur, saoc, xad"
}
```


### [2026-09-06T20:37:23.925Z] TOOL RESULT

```
== Schwefel ==
25827:•  j.  saok«nta'vant-  Adj.  (fem.  'vaiti-) ■Sdiwefel  enthaltend,  mit  Schwefel  ver- setzt: äpim  •vaitim  zaranyavattlm  vT^u/a- vaitm  (sd.)  V.4.S4.  55-
== saoc ==
5692:asaocant-
11539:•  g.  Jaidyäi  Inf.  'ni  töten':  kyat  vTsJnta (sd.)  dnfgvartt>m  avs  hyatcS  gäus  j°  mraoT yS  düraosjm  saocayat  (sd.)  avS  ".  .  und dass  es  heisse:  das  Kind  ist  zu  töten,  da- mit es  . ."  Y.J2. 14".
17086:•  j.  bänav-  m.  'Lichtstrahl,  Strahl':  tifirim .  .  darat  vyävant^m  (sd.)  -«aJj'ff  (alslnstr.) *raoxSmbyS  anahitaHbyS  Yt*.  2;  —  as? srire . .  bänummti  säiti  vyävaiti  (sd.)  °nubyS (alslnstr.)  Yt/7.6;— df^ra/  hala  'nuwe^y^ aisma  frasaocayahi  {sA)  V.  Ä  75.
20649:Objekts-  und  praedik.  Akk,  'nennen,  be- zeichnen als  ~,  sagen  von  — ,  dass dim  mruyä  ä%ravan}m  V.lS.i.  a)  mit Dat  der  Person:  airyamamm  ti  i/f\ mazistam  mraomi  . .  sravatfham  FrW.  4. ) V.  /i*.  Ö5;  —  at  fravaxsyä  kyat  möi  mraot spfTiiö.tsm3  vac!  srStdyäi  (sd.)  "ich  will reden  von  dem,  was  der  heiligste  mir genannt  hat  als  das  Wort  . ."  Y.  45.  5 ;  — tat  vfrjsyädyai  hyat  mBi  mraotä  (aP.) vahill^m  ".  .  wovon  ihr  mir  sagtet,  dass es  das  beste  sei"  Y.45. 11,  a)  statt  des praed.  Akk.  ein  Inf.:  a/avamm  li  aSaonat ä/yeioyai  (sd.)  mraomi  Y.  7;.  13.  aa)  ' pass.  Wendung  (ohne  Dativ):  hyatlä  gSus jaiifysi  mraoi'^  yS  dBraos>m  saocayal  (sd.) ava  Y.  J2.  14.  s)    ohne  Obj.  'Kunde,
22105:(sd.)  vainantS  (AP.)  braianta  . .  »mabm zaranim  Yt.5. 129.  a)  mit  ergänzendem Partizip '':_yff/i'tfOT  ainim  avaSiai/(2SPiA.; Augm.)  saocayaca  kirmavanttm  "wenn  du leben  andern  .  .  treiben  sahst"  H. 2. 13; —  \ya'h3  avaina'  imäm  bümim  *yauda'tim (sd.)  D.ö'.4.  2)  AkL  'es  einer  Sache (Akk.)  ansehen  (können)':  vansim  . .  vae- naiti  kalarS  ayravU  (sd.)  vi!  *bunavs  vä Yt.  14-  31,  iG.  10.  3)  Akt  'ansehen für  — '  (Akk.):  ySi  %wS  vam»n  .  .  aham rff/Bwc'fl"diedidi  für  denj4.und^.  ansehen" YL  10.  92;  — yim  dim  vaEnät  *rvistaäva (sd.)  *vindatum  N.  16.  4)  Med.  'videri, gesehen  werden,  scheinen':  a6da(sd,ya i  (sd.)  ioa  . .  sadayät  yat  iha  pasSuS .  .paa?m vaSnäite  V.  2.  24;  —  haksrit  ir  irixtahe I  (sd.)  .  .  valnaite  (statt  Plur.)  itarasca  . . V,  2. 40;  —  \tya'paüy  iariam  vainataiy naibam  (sd,)  X.i.  ^;—~  tanOm  yä  mi  val- naite Auraeoa  ".  .  quae  mihi  vtdetur  for- mosa"  Y.io.14.
22675:Zum    V.    ivoB'.    —    Vgl.  ^vanta-.    —    ^.■.  .pasüttt    *ava^^.vTnaoi/i  pasca    hü  frasms.- /w»,  m^tk?  dssi  i  i^ä™^»)  «  */  dilti  zfa-  ^^,-„^  asaocantat  paiti  a^irai  N.  5S. A/>ut/<,n    bivii  -   aiäv  gSn  -  vihapi  bavil.        mit >a 'schlachten  ,  alsOpfer:  ^«Mw^M Mangelhaft   übeiliefert.    —    ')  S  368.  35.    ~\anumayanqm  frävinuysl  V.  m,  70. '^  Vgl,  Bd,  sr.  4,  iLSTi  NB.  385.  —  3)  S,  dazu        D  Et.?     Vgl,  S  317.   —    PS,  (in  V,):   Ixlla», Bthl.  LG&kPb.  lyOi.  61.  (lu  N.):  fehlt.  —  ')  Hds,  aväi.
22835:•  j.    saocayaca     kfnnvB    .  .    "varö.jinö urvarS.strqmca  ktnnvS  Vyt  J7.
25810:"saocaya>italibyS.
25811:'in  lichter  Flamme  brennen,  flammen': saoHntai paiii  ä^ratV.g.^ö; — a%rqmca suxrqm  saocintqm  V.  2.  8,  a)  Kaus. '(inflammare  sva.)  incitare':  gaus  jaidyäi (sd.)  . .  yi  däraohm  saolayat  avS  "das Rind  ist  zu  töten,  damit  es  den  Tod- wehrer'  {d.  i.  Haoma)  ansporne  zu  helfen" Y.^2.i4'>.
25831:•  j,  saocant-'l  Adj.,  PPA.:  s.  saok-. KompE.  —  >)  Auch  'anf,  %  2g8.  4.
== xad ctx ==
—  ai.  kfärali,  gr.  ^üpa;  s.  dam  Wn.  AiGr.
I.  241,  Bgu,  GrGr.J  ug.  —  Pü.  (lu  V.  32)-.
afic  äUnjäi  kunll,   (lu  V.  5.  19,  52,    ig.  40);
adadat,  lu  V.  5.  19  mit  der  &1.;  ^wr.  —
'>  S  joj.  7,  33S.
•  j.  yzarfl-yzarant-  Adj.,  PPA.:  s,  -fiar-.
•  j.  j-zärayant-  Adj.  (fem,  'yeinn-),V'PA,: s.y=a
KompE.
X.
•  j.  xao^a-  (,  p.  xauda-)  m.  'Hut,  Kappe Helm'.
KompEI.  —  woss.  xodä  'Mülie,  Hut',  arm LW.  xoir  'Kopfband';  s.  noch  Hbm.  AGr.  i iGo,  Bthl.  Stud.  3.  57;  falsch  FiCKVglWb.' 3.  89.
•  j.   xad-  V.,   nur  mit   vi  'auseinander quetschen'.     Praes.  2  xala-.
airihä  zimS  (sd.)  päsnalibya  vTspara aslaäbya   vixala  (aS.)  V,  2.  31;  32    (wo
Vgl.  ai.  khSdati,  np.  xäyad  'er  kaut';  %  136. S.  poch  Pü.  —  Pü.;  »padddt,  lies  a/xSsl.
•  j.  xa^vza-  m.  Bezeichnung  dessen,  der (aktiv)  Päderastie  treibt,  'pedicator':  iö daSvanqtn  'zS  .  .  xumbs . .  kü.näirls  "wer ist  ein  pedicator  .  .  ein  patkicus  . .  eine Hure  der  DaSvaT'  V.Ä31;  32.
Die  Bedeutung  ist  vermutlich  eine  übertragenfi wie  bei  xumba-  (sd.).  —  np.  xafj  'incubus, Alp',  s.  Hbm.  PSt.  s6-  Wie  ist  aber  die  iran. Grundform  anzusetzen  und  wie  das  z  (gegen %  38.  \  b)  zu  erklären?  —  Pü. !  ki  Jh(i<i xamizah  (Transskr.)  »  kt  devän  xumbak,  erl.; däfän  kär  i  narih  u  mälailh  ke  hinend.
•  j.  xan-  f.  'Quelle,  Brunnen':  xä  (NP.) aspS-stdoyehl^  apam  Vt.  Ä  5 ,  42;  —  apamui xä  (AP.)  Y..,^2.'i;  V.y.si;  —  xa  'paiti afrajyamna  Yt.  ;_J.  14^;  —  vupa  äp5  x'i paiti  '^raoid.siätascü  (sd.)  Y.  Ji.  9 ;  —  »nzöis (sd.)  xh  Ytj^ag;  —  m^rtzuca  (sd.)  xa u^tünahe  Yl  /0. 7 1 ;  —  frä  tl  hazat^rsin xqm  (GP.)  .  .  gaoiaiDin  (sd.)  avi  hanta- una'^.21.'};  —  fiaoma..  hai'hlmca  asahe xa  (NS.)  ahi  "o  H.  .  .  und  wahrlich  des
heiligen  Rechtes  Brunnen  bist  du"  Y. 10. 4'>,
Ableit.  (s.  xqnya;  xayaria-].-^  Zum  ar.V.  ikan-  ? ;
E.  ^kan-  mit  No.  I.  —  ai.  ihaii-  f.  {ihi-);  mp.
(Pü.)  vyl.  x3h.  —  ■)  Vgl,  RV,  2.  28.  5;  ihdn
•  j.  xayana-  Adj.  (fem.  -na-)  'fontanus': apfm  °nqm  . .  apim  zrayanqm  "das  Quell- wasser .  ."  Yt,().2.
Ableit.  am  xan-  (vgl.  xqnya^*\  —  FQ. :  äp  i xänlk,  äp  pa  x3ti.  —  ")  Wie  ist  die  Bildung zu  Stande  gekommen?  Wohl  einfach  durch Reimen  auf  das  (folgende)  irayana-i  s.  lu gaimai-anl-.
•  j.  puirS  zayante  tanu-kihrpa  kikrpa "xay^us'*  Vyt,  /,
Pü.:  x'is;  s.Var.  —  ■)  Var.  j*jh/.  Dst.  ZA, 2.  666    lieht   das  Wort   lum  folgenden  Sati
j.  hafrsne  apno  xavä  F.  2l.\    verkehrte  Um- schrift statt  iapa%fit  (sd.)  a/nanuhä.
```


## [2026-09-06T20:37:25.842Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHD sog mourning ==\"; grep -n \"sōg\\|sog \\|mourning\" PHD.txt PHD_mackenzie.txt | head -20\necho \"== NYB ==\"; grep -n -i \"sogand\\|sōgand\\|swgnd\\|sōxtan\\|swhtn\\|suxr\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep PHD/Nyberg"
}
```


### [2026-09-06T20:37:25.910Z] TOOL RESULT

```
== PHD sog mourning ==
PHD.txt:131:sneh ... for sword read club, weapon. ?sog ... add N ~ ‘grief’. for Sēšyans ... read Sēšāns (|swkš ns...
PHD_mackenzie.txt:611:       2 sog       add N '" 'grief'.
PHD_mackenzie.txt:4568:ssog [swh I N so(y)] side, direction.
== NYB ==
1725:*guhrāyēnītan [gwh'Pynytn'] to awake, to rouse a p. from sleep 321’. — Caus. of guhräy- < gufräy-, cf gwpl’dt' = gufräyet rendering Av. (511) frāyrāyrāyetti ‘rouses (him) from sleep’ Vd. 1823 and Nir. Waag p. 46 (= Sanj. fol. 275), gwpl'dšnyh (this is the correct reading) = gufrayisneh rendering fräyräraye (inf. of the same vb.), Nir. ibd; frac gufradyisnéh rendering Av. (977) fra-yrāti- ‘the awakening’. gu-fray- may be explained from vi + frayrāyrāy-, from Av. (511) !gar- : fra-yrayräy- > frayräräy (dissimilation of y) > frayräy (first haplology) > fräräy- > fräy- -(se- cond haplology); vifrdy- > gufräy- > guhräy-; the spelling gwh’r- is analogous to spellings such as gwh?l = göhr, swh’l suxr, perhaps denoting a glide vowel: guher-, göher, sux*r. — V. also vi-gräs-.
3460:sökand [swknd] oath; ~ xtartan to swear an oath (pat by) 2118-23, 2225, 2322. — Ps. swkndy; MPrs swgnd; Paz. sawagand (SGV); NP saugand.
3465:söxtan [swhtn'] söc- 1. trans. to burn 19". 302. 4816, 10712-13, 11313, — 2. intr. to burn 375 (v. x"at-sócak&h). 9674. 9818. — Av. (1548 sq.) saok-; MPrs pres. swe- (8), swcyšn, adj. swc'gyn (A-H I); Paz. sēžā < sócük; NP sóxtan soz-. |
3574:suxr [swhl, swh'I] red 9%. 1188; 1218 read ~ instead of dyml. — Av. (1582) suxra-; OP cf n. pr. Ouzra-; Paz. suhr (Aog.); NP sure.
3708:tak [t’k'], tai [7D] 1191?: unit, piece, after numerals: 76 ~ hac uzmuburt u 16 — hac yükind i suxr sixteen pieces of emerald and sixteen of ruby 1187; gartānāk & ~ one (piece of) die 120°; cand mode ~... nč not a hairbreadth 7222; cand ~ dānā- kan i hindūkān some Indian learned men 11919-20, — Paz. tak (Mx), syn. with NP tāli), v.s. v. tähe-kar and tāyītan. The form täi in MiPrs is attested by the wrong ideogr. *D, v. tät.
4936:Oadaya-: sahistan Oak-: sacišnēh Oard-: sal Ouxra-: suxr
```


## [2026-09-06T20:37:38.994Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v2_pages.txt; echo ---; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5; echo ---; grep -c \"\" BQT_v2_pages.txt",
 "description": "Inspect BQT v2 pages file"
}
```


### [2026-09-06T20:37:39.054Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
---
---
41071
```


## [2026-09-06T20:37:39.846Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "Full BQT ref info"
}
```


### [2026-09-06T20:37:41.530Z] TOOL RESULT

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


## [2026-09-06T20:37:46.906Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 156 172; do echo \"=== leaf $L (printed $((L+540))) ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -70; done",
 "description": "Print BQT pages 696 and 712"
}
```


### [2026-09-06T20:37:49.054Z] TOOL RESULT

```
=== leaf 156 (printed 696) ===
    ‫ره‬                                                                                        ‫خارخك‬
             ‫راکش منوب بدوست ‪.‬‬
                             ‫که سرود خ‬                                                        ‫گفته اند ‪.‬‬
‫خار کن‪ -‬بروزن بادزن» معروف امست‬                   ‫‪ 4‬وآن‬    ‫است‬    ‫ممروف‬   ‫ت‬   ‫‪۱‬‬   ‫خك‬          ‫جار‬


 ‫وآندخصی باشد که ببوسته خاراززمن بکند ‪۹‬‬           ‫خاری باشد سه پهلو ‪ .‬بهترین آن بتالی بود‬
‫و ام نوایی وصوتی است از موسیقی ‪ - ۷‬و نام‬           ‫وآنرا مفرییان (‪ )۱‬حمص‌الامیر خوانند گ‪.‬ویند‬
 ‫تدوصتب‬
                           ‫‪۰‬‬
            ‫است که سرود خار کن منوب‬        ‫شخصی‬
                                                  ‫كك بهار‬
                                                        ‫است وعصارة آ را درجامی که ‪-‬‬                 ‫معمتدل‬

                ‫وبوته برخار را نز کفته‌اند ‪۰ ۸‬‬                   ‫باشد مفانند همه (‪ )۲‬بمیرند ؟ ‪.‬‬

‫خار مهك = بفتح میم و سکون ها‬                      ‫خار درراه شکستی د کنابه از‬
 ‫وکاف » حشیشی است کوهی ودر زمن سدگتان‬             ‫محافظت کردن باشد ‪ - ۴‬و خار چدن را قىز‬

‫رود ؛ و هترین آن سبز باشد ‪ .‬گرم و خعك‬
‫اکر قدری از آن در زیر‬          ‫ند‬
                                ‫ب‪۰‬‬‫ویم‬
                                    ‫است دگر س‬       ‫خارشتر ‪ -‬ممروفت » و آجننی‬
 ‫بالینطفلی کهازدهن اوآب میرفته‌بشد بگذارد‬         ‫ر ازخوردن آن فربه شود ‪.‬‬
                                                                        ‫تکه‬
                                                                          ‫شار‬
                                                                            ‫ماشد ازخ‬
 ‫برطرف شود » وآنرابعریی کشهوالمربیه وشکاعی‬
                                                   ‫خار لد ‪sa‬‏ بروزن‌تارك‪ .‬تصضر خاراست‪-‬‬
                                       ‫خوائند ‪.‬‬
                                                              ‫و لوعی از خرما هم هت ‪.‬‬
‫و کنانه‬    ‫ممروف‌است ^‬    ‫خار نهادن ‪-‬‬
                                                  ‫ماف و سکرن شین‬‫خار کش‪ -.‬ک‬
    ‫از نافرمانی تمودن ‪ -‬وجفاکردن هم هت ‪.‬‬
                                                  ‫» سر موزه را گوبند » و آن کفشی باشد‬               ‫قرشت‬
‫باره ‪ 4‬نمعتی خار است‪.‬‬    ‫ت‌ بروزن‬   ‫جاره‬
                                                  ‫که بر بالای موزه پوشند وآن در ماوراء النهر‬
‫وآن یارچه‌ای باشد موج دار وقمتی ‪ -‬وسنگه‬
                                                   ‫یشتر متعارفست » و بعربی جرموق خوانند =‬
 ‫‪-‬زرا‬
    ‫خارا رایز گونند که منک مخت باشد و‬              ‫ویفتح‌کاف شخصی را کونند که سوسته خاربکشد‪-‬‬

‫گهفمته‌اند کهنقیض مرد است ‪ -‬وبمعنی خاده‬            ‫ونام سرودی ونوابی‌است ازموسیقی ‪٩‬‏ وشخصی‬
                                    ‫(‪ )۲‬خم ‪ -: ۳‬همه ‪.‬‬            ‫(‪ )۱‬خم ‪ :۳‬اهل مغرب ‪.‬‬


  ‫‪ . ٩20015‬کیاهی از تبر چتربان ‪56۴۳6]1]]60000‬‬              ‫‪۴‬‏ =‬       ‫‪:‬حك‪.‬‬        ‫رك‬     ‫‪۱‬‬

  ‫که دارای ساقه های دراز و چترحابی کم کل ودانه هابی است که برجست‌گیهای روی آ نهابصورت‬
                            ‫هکل کلاب ‪+۹۳‬‬      ‫خارهای کوچك وم‌حنی درمی آ بد و بلای هی ‪ +‬د‬
               ‫کمان دز کار ده ده ها کی‬                   ‫مرا تاخار در ره‌می‌شکستی‬        ‫‪۴‬‬

  ‫نظامی گنجوی‪ .‬ک«نجینه ‪.*۸4‬‬
  ‫و دارای خار بسیار است‬        ‫‪ Hedysarum‬از دته اسپرس ها ‪5۵66۲۵506۱۳‬‬                   ‫‪۴‬‏ =‬
  ‫»‪ .‬رك‪ :‬خاراشتر واشترخار‪.‬‬     ‫مآید‪ «.‬گل گلاب ‪۱‬‬   ‫دست‬     ‫همروید و ازآن تلرحدن‬         ‫و در تقاط خعك‬

                     ‫ش‪.‬‬
                      ‫کراه‬
                         ‫رگفت‬
                            ‫ا می‬
                               ‫خ کل‬
                                  ‫یش‬                    ‫بلیل شوریده میگردیدخوش‬            ‫‪۵‬‬
  ‫عطار یشابوری ‪« .‬فرهنك‌تظام»‪.‬‬
          ‫‪-‬خارکتی را دیدم ( حاتم طابی ) پشتةٌ خارفراهم آورده ‪...٩‬‏ گ«لتان ‪.۶۰۱‬‬
                                                                             ‫‪« ۱‬‬
          ‫که مدتی سرو کارش لبوده جز با خار‪.‬‬             ‫نندالزیب تست عجب‬
                                                                       ‫‪۷‬و‪-‬ای خعارک‬
                                                                                 ‫ن‬
  ‫ظپیر فاربابی‪« .‬فرهنك نظام»‪.‬‬
        ‫که اقلم کلتان را بات خار کن دارد‪.‬‬           ‫‪ - ۸‬برون کن ازبخور هی زمغزسربخار وی‬
=== leaf 172 (printed 712) ===
 ‫‪۷‬‬                                                                                                        ‫خیدن‬

                ‫بجایم وبای فارسی گهفمته‌اند ‪.‬‬                   ‫باشد‪ -‬وساخته ویرداخته شده‬        ‫بمعن یجمع حاب‬


‫بفتح اول وثانی سَحتالی زرسده‬              ‫خییو م‬                ‫وییچیده را نگیوزبند ‪ -‬وبمعنی‌تل‌ریگه ونود‬
                                                               ‫؛ وبسای رای قرش تت واو هم‬        ‫رنگ همآمده است‬
‫ونودء‬   ‫ت‬   ‫‪ 0‬سامان‌کار کے ورجمع حاب‬            ‫وواومفتوح‬
                                                                                                      ‫گفته‌اند ‪٩‬‏‬
‫ریگ راکوبند ؛ و با بای فارسی گهفمته‌اند ؛‬
‫وماضافةً رای بینقطه‌هم بنظرآ مده است که خبنوره‬
                                                                 ‫ون‬
                                                                  ‫سیکو‬
                                                                     ‫ان‬            ‫ور‬
                                                                                    ‫حیین س بنم اول ک‬
                      ‫بروزن مستوره باشد(‪. ۴ )۱‬‬                 ‫تحتانی و نون » طبق چوبن باشد ؛ و باين »عنی‬


                                                        ‫بیان سیم (‬
                      ‫بای فارسی مشته‌ل برشش لغت‬
                                              ‫نقطه‌دار با‬                                ‫درخای‬


                                          ‫ا"‬     ‫هم درست‬       ‫< جح اول و سکوننی ‪ .‬پمنی‬
‫خيك = بر وزن نمك » نان بز ر گے را‬
‫گویند وبمعنی گلوفشردن‌وخفه کردن وخفه‪- ۴‬‬                                                 ‫یمنی خاموش بش ودم نزن ‪.‬‬
                                     ‫هم همست ‪۰‬‬          ‫وفت‬     ‫»ار دبواری‬
                                                                         ‫مفاك چ‬           ‫خباه؟ = بورزن‬
 ‫که فشردن‬     ‫ومعنی‌خفه‌است‬        ‫روزن‬    ‫»‬    ‫حه‬              ‫که شبهاکوسفند و خر وگاورا درآن‬              ‫باش‬
                                           ‫کلو بائد © ‪.‬‬                                                    ‫کنند‪.‬‬
‫ورزن ومعنی خمیده و خم‬
                    ‫خبیل ه ‪ -‬ب‬                                  ‫جیچه د بفتح اول بروزن کفجه ‪ ,‬شاخ‬
                                               ‫باشد ‪۷‬‬    ‫شده‬     ‫درخت باربك وراست رسته راگویند؛ وبکراول‬




                  ‫‪.‬‬   ‫‪ :‬سوم‬    ‫چش‬     ‫»‬    ‫چك‬    ‫(‪)۲‬‬           ‫(‪ )۱‬چش‪ :‬خبیوره باشد بروزن متوره‪.‬‬

                                                                                ‫‪ _ ۱‬رك ‪ :‬خير وخبره ‪.‬‬
                                               ‫مصسحف‌خییره‪ .‬رك‪:‬خبیره» خبس» خبارموخبره ‪۱‬‬           ‫ظ‬   ‫‪€‬‬

                       ‫خیگه‪ .‬ور که ‪ :‬اسفاا ‪۲ :‬ص‪٥‬‏ ‪.۷‬‬                  ‫رکه ‪ :‬خبك » خبه » خفه =‬         ‫‪۴‬‬

                              ‫‪..‬‬    ‫رك‪ :‬ميف‬       ‫‪۷‬‬               ‫‪.‬‬   ‫خبه‬   ‫‪,‬‬   ‫› خيك‬   ‫‪ :‬خبك‬   ‫رکه‬   ‫®‬
```


## [2026-09-06T20:37:59.542Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    for pat in ['خاج','صلیب','خایید','خاژ','خائید']:\n        if pat in p:\n            print(i, i+540, pat, p.count(pat))\nEOF",
 "description": "Search BQT v2 for خاج and خاییدن"
}
```


### [2026-09-06T20:38:02.161Z] TOOL RESULT

```
23 563 خاج 1
82 622 خاج 1
107 647 خاج 1
114 654 صلیب 4
115 655 صلیب 1
154 694 خاج 2
154 694 صلیب 3
157 697 خایید 1
168 708 خایید 1
168 708 خائید 1
169 709 خایید 1
170 710 خایید 1
319 859 صلیب 1
384 924 صلیب 1
486 1026 خایید 1
```


## [2026-09-06T20:38:08.613Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nimport re\nfor i in (154,):\n    p=t[i]\n    for ln in p.split('\\n'):\n        if 'خاج' in ln or 'صلیب' in ln or 'ارمن' in ln or 'خاچ' in ln:\n            print(i,'|',ln.strip())\nprint('=== full leaf 154 tail (footnotes) ===')\nprint(t[154][-1500:])\nEOF",
 "description": "Print BQT خاج entry"
}
```


### [2026-09-06T20:38:10.589Z] TOOL RESULT

```
154 | ‫خاج " = بر وزن تاج » بمعتی چلیپا‬                                 ‫وژن صابون » بزر که‬          ‫=ر‬
154 | ‫باشد که صلیب نصاری است و آن‌باین‌شکل بود‬                                         ‫وبی‌بی کودباتوی خانه را گوبند ‪.‬‬
154 | ‫‪ - ۳‬ازکلمة‌قدیم خاج ‪0 06‬از ارمنی ‪( 621‬صلیب) « هوبتمان ص ‪« ۷۲۲۰‬اسفا ‪: ۱‬‬
154 | ‫مدرسه بر گید گران آرد ‪.‬‬                 ‫ای‬                      ‫صلیب و خاح بوزد کلبیا بکند‬
=== full leaf 154 tail (footnotes) ===
<( خم‪ :۳‬گفته‌آند ‪۰‬‬       ‫(‪ )۱‬چش‪ :‬کنانه بود ازشراب ناب ‪.‬‬
                              ‫(‪ )4‬خم ‪ : ۳‬علها السلوة واللام‪.‬‬        ‫کو نند ‪۰‬‬    ‫(‪ )۳‬خم ‪۳‬‬


 ‫‪ - ۱‬تر کی درجغتابی * خاتول؛ به‌عتی بانوی ءلی نب «جفتایی‪ .*۲۱۳‬امروز بتر کی‬
  ‫کوند الادراكللان الانراك ‪ .‬ابن مهنا ص ‪ ۹۸۱‬و دیوان لفات الترك کاشفری ‪ .‬ج ‪۱‬‬ ‫‪0‬‬
                                              ‫ص‪ » ۳۳‬معرب آن نز «خاتون» «تفی» ‪:‬‬
           ‫خود زبانم هتیجنبد اینچذین ‪.‬‬                                     ‫گفت آن خاتون کزین ننک مهبن‬
  ‫‪۳‬‬   ‫‪۶۹‬‬    ‫‪٩07‬ص‏‬    ‫‪ 64 ۷6‬س ‪ » ۸۲‬ورك ‪ :‬نداب ‪:۳‬‬            ‫س‬    ‫مولوی چاپ (‪yop‬‏‬      ‫«مثنوی‬

  ‫‪ - ۳‬ازکلمة‌قدیم خاج ‪0 06‬از ارمنی ‪( 621‬صلیب) « هوبتمان ص ‪« ۷۲۲۰‬اسفا ‪: ۱‬‬
                                                                                                          ‫‪: ° ۸‬‬     ‫‪ ۲‬ص‬

           ‫مدرسه بر گید گران آرد ‪.‬‬                 ‫ای‬                      ‫صلیب و خاح بوزد کلبیا بکند‬

  ‫‪ = ۴‬خات («‪.‬م‪« : ).‬خاد » زغن باشد یمنی هرخ گوشت‬                                     ‫‪.‬‬    ‫صلب‬   ‫‪:‬‬   ‫رك‬    ‫‪۴‬‬

                                                            ‫خسته کفت ‪:‬‬         ‫ربای» واورا پند وظیواج نیزکون‬
           ‫رنود ازکش کوعت ویرد و کریز ‪۴‬‬                                  ‫درآمدیکیخادچنگال تیز‬
   ‫> ‪.‬‬     ‫فرسع‪۰۱‬‬    ‫غت‬

                                         ‫‪.‬‬        ‫‪۲‬‬      ‫مذین معنی درت رکی قفر «خارم»‪ «.‬جشتایی‬           ‫‪_ ۵‬‬
```


## [2026-09-06T20:38:23.670Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==238' HUB.txt | head -40\necho \"=== grep xac in HUB ===\"; grep -n \"xac\\|/ac\\|Kreuz\" HUB.txt | head -20",
 "description": "Print Hübschmann leaf 238 and grep for xač"
}
```


### [2026-09-06T20:38:26.388Z] TOOL RESULT

```
- 227 —
fhl, *micak; dd0, ddza*Lsick\ arm. dod (medic. Schriften) in
doci xez = Xack-gummi'; pazan = pdzan, kavtz = kavHz
s. oben, raja^ raza oben p. 66 ^). Np. ocaj *Kreuz' aus alterem
"^xac = arm. xac *Kreuz* ist arm. LW.
•
§ 117. Wenn nun 6 nach tonenden Lauten zu z, Zyj
geworden ist, so sollte 6 nach Vokalen und r im Np. nicht
mehr vorkommen. Dies ist dennoch der Fall in: ha6a =
ha66a (oft bei Firdusi) Junges', das auf phi. *va66ak (aus
vat'Cak oder ahnl.) zuriickgeht und sein cd erst in neuerer
Zeit zu d vereinfacht hat ; xarcang 'Krebs* = phi. kardang
(volksetym. an xar 'Esel' und 6ang angeiehnt ? oben p. 54),
vgl. gr. yapyivog (Lehnwort?); ga6 *Kalk' = paz. gac, aus
phi. *gacc?y vgl. arab. ja?s 'Gips, syr. gessa, gr. yvxpog
(Lehnwort ?) ; hed^ ex *irgend ein', erst im Mp. aus g = gr =
ap. aiva- ein* und 6 = ci ^= ap. ciy zusammengesetzt^),
vgl. agat'ci, mamc (dial.) u. s. w. H. 451.
Aus jiingerer Zeit muss auch das Deminutivsuffix ^)
(fa, tea (VullerS; Gram. p. 234) stammen: bayda 'GtSiTtchen,
aluca 'Mirabelle* [dlu Tflaume'), baztca 'res lusoriae', darlca
'Thiirchen, Fenster, Gussform' = arm. daricak *Gussform'
(11.— 13. Jhd.), huzUa a kid' JRAS. 1894, 448, suroi^ca
*R5theln (auch surxtza, vgl. turbzza *Radieschen' *) von turb
'Rettich' bei Rosen, Np. Sprachf. p. 36).
Geschwunden ist c vielleicht in kas *jemand' = zd.
kascit, ap. kasciy, Vgl. pas *hinter = zd. pasha {paskCU),
dem aber schon im Ap. pasa (nicht *pasca u. dgl.) gegen-
iibersteht.
Ueber anl. eg = ap. sg = np. S siehe Kap. 23.
*) Vgl. auoh i in vazun = vazgun, bSzgun u. s. w. Verkehrt* aus
apac -f- gun Horn, KZ. 33, 437. Doch weist nigun Verkehrt* = phi.
n{i)kiLn Gl. and Ind. 246 auf -kun als 2. Glied des Eompositums.
') Vgl. dagegen ciz (ap. ciSciy) mit z au8 c (= d-c), well die
Zusammensetzung schon im Altpersisohen bcstand.
') Vgl. das Deminutiy suffix np. ak.
*) Dazu auch Iza in p&kiza *rein* von pclk *rein*P Aber kantzak
ist duroh das Suff. ak von kanw abgeleitet (oben p. 89).
15*
=== grep xac in HUB ===
7893:in uzmaydpatiy *an das Kreuz' und in paruzana- Von vielen StUmmen^
8092:s. oben, raja^ raza oben p. 66 ^). Np. ocaj *Kreuz' aus alterem
8093:"^xac = arm. xac *Kreuz* ist arm. LW.
8226:bazban (Fird. II, 740, 1053), bazvan ^exactor vectigalium' ; ba-
```


## [2026-09-06T20:38:33.674Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if i<600: continue\n    for pat in ['سوختن','سوگند','سوگ','افسوس','سرخ']:\n        if pat in p:\n            print(i, pat, p.count(pat))\nEOF",
 "description": "Locate BQT pages for sukhtan/sogand"
}
```


### [2026-09-06T20:38:36.123Z] TOOL RESULT

```
684
605 سرخ 2
615 سرخ 1
618 سرخ 1
619 سرخ 1
622 سرخ 1
623 سرخ 1
624 سرخ 1
626 سرخ 1
637 سرخ 2
639 سرخ 1
644 سرخ 2
647 سوختن 5
648 سرخ 1
649 سرخ 4
650 سرخ 2
654 سوگند 1
654 سوگ 3
655 سوگ 1
659 سرخ 5
660 سرخ 1
663 سرخ 2
664 سرخ 1
668 سرخ 1
677 سرخ 1
```


## [2026-09-06T20:38:57.321Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (647,654):\n    print('======= leaf',i,'=======')\n    print(t[i][:900])\n    print('---- tail ----')\n    print(t[i][-1600:])\nEOF",
 "description": "Print BQT leaves 647 and 654"
}
```


### [2026-09-06T20:38:59.852Z] TOOL RESULT

```
======= leaf 647 =======
                                                                                                         ‫اه‬      ‫ی‬

         ‫کوچك و اندك وناقص آهمده است ‪.‬‬                                                  ‫و غیرآن برددانپا مالند ‪٩‬‏ ‪.‬‬
‫سو ‪٩‬‏ = بضم اولیر وزن عوج»بمعلی‬                                   ‫وای‬ ‫سلکوون ثانی ب‬  ‫سوپ ه نم او‬
‫دشردفچاهرسی جيم‬  ‫سوز است که اسزوختن با‬                            ‫فارسی » بزبان خیوق که یکی از العای خوارزم‬
      ‫ابجد بزای هوز وبررعکس تبدیل می‌باید‪.‬‬                        ‫است آبراکوینه همچنان کهپکند بابای‌فارسی‬
                                                                  ‫وکاف بر وزن سمند الرا ‪۴‬و سوپ ویکند آب‬
‫سو جرو نتن ‪ ۲‬د با اول بثانی رسیده‬                             ‫ت ؛ و بعضی گویندطلب آب وناناست‬
 ‫و فتح جیم و رای قرشت بواو کشیده وکرنون‬                                                      ‫و بان اس‬
‫وفوقانی
---- tail ----
‬‬            ‫(‪ )۱‬چك ‪ :‬وبا ‪.‬‬
                                                                         ‫(‪ )4‬چك‪ :‬ژند ویاژند ‪.‬‬                ‫صفرجق ‪.‬‬
 ‫صد وشش‬      ‫ص‬   ‫پکند » ورك‬        ‫‪:‬‬   ‫رك‬   ‫‪۴‬‬             ‫‪ :‬شرح قاموی » منتهی الارب ‪.‬‬               ‫‪- ۱‬رك‬

                                                                  ‫رك ‪ :‬ژر ژوره ‪.‬‬        ‫‪۴‬‬              ‫ا ‪.‬‬     ‫مقدمه‬

    ‫سوختن‬   ‫رك ‪:‬‬   ‫‪.‬‬   ‫سوز‬     ‫>‬   ‫‪۹‬‬            ‫ھ_ رکه ‪ :‬شابپار ‪.‬‬                      ‫‪ .‬امد «بونکر ‪. ۰۸‬‬          ‫‪4‬‬
    ‫‪- ۷‬هز‪ . 8261۵0۵۳(8)6۵5 65۰۰ 68)(۵)۵06۲.‬پپلوی ‪ , 0۵1۲1108‬آوردن «بوتکر ‪. ۰۸‬‬
  ‫‪ ۶‬اسم مقمول از «سوختن» ‪.‬‬      ‫‪ = 4‬سوزه ‪ ۳۳‬سوجه ‪.‬‬            ‫‪ - ۸۵‬سوزش ‪.‬‬
  ‫‪ #‬سوختی ‪ -‬بم اول وفتح چهارم ‪ ,‬اوستا ربشة‪(1112186025. 6035 -‬روشن کردن)»‬
  ‫[‪ 67212.‬ش(ملة آش) ‪( 6520029 - ,‬سوخته) ؛ پهلوی ‪. 005(1)6۵5, 820265‬‬                                             ‫‪2‬‬
   ‫) » افتانی ‪1289 . 12285‬‬              ‫و‪8‬خ(تن‬
                                             ‫س‪10‬‬
                                               ‫‪ 1420۵2 .‬؛ کردی ‪۵5‬‬                           ‫‪6‬ش‪6-۵‬‬
                                                                                                ‫حهندی بامتان ری‬
  ‫وللا‪ , ۷2[۵۷‬استی ‪ ۵۵5‬و ‪( 005‬سوختن) » بلوچی ‪ ( 08224119 8263‬سوختن) ›‬
  ‫‪ 8268,‬ر ‪( 0820/5۵5‬سوزاندن)‪,‬وخیم ‪ , 205‬سربکلی ‪Z0146‬‏ (سوز) «اسشق ‪ .»۰۵۷‬کیلکی‬
         ‫؛ آنش کرفتن چیزی (لازم) » آش دگریراندن در چرزی » افروختن (متمدی) ‪.‬‬                                     ‫‪0‬‬

======= leaf 654 =======
  ‫=( =‬                                                                                         ‫سکوك‬

‫شخصی باشد که چند موی برسر زنخ داشته باشد | لام » بمعنی س وکك است » و آن زردیی‌باش دکه‬
                                              ‫وسج است ‪ -‬و بمعنی‌خوشۀ گندم‬ ‫آن‬‫و معرب ک‬
 ‫سو گواد ‪ - ۴‬بروزن گوشوارمصیبت‬                       ‫کندم وجورا لز گوبنده‬     ‫و جوهم گفته‌اند‪ -‬وداس‬

‫چه صو که بمعنی‬     ‫زده وصاحب مانم را گویند‬          ‫و آن خهای سر تیزبود که برسرهای گندم‌وجو‬
                 ‫باشد‪.‬‬   ‫مانم و وار بحعنی صاحب‬                                       ‫باشد ‪٩‬‏ ‪.‬‬
‫بنتح کاف » هرسوراخ را‬       ‫سو که * ه‬                ‫خو يك ‪٠‬‏ زردیی‬    ‫سو كك ‪ = ۳‬بر وزن‬

                                                     ‫آفتی‌در کشت وزراعت افتد ؛ وباین‬       ‫باشد که سب‬
 ‫وسوراخ فبل ودبر بعنی‌پیش وپس‬       ‫گوبند و‬
‫را خصوصا‪.‬ودرمجمم‌الفری سروری بجای کافلام
---- tail ----
 شدن آن ازشکم با ماندن آب‌درشکم تقصبر وی تقصری‬
              ‫اورا معلوم مبکردند ‪ .‬استعمال فعل «خوردن» با سوگند بادکار همین مفهوم است ‪:‬‬
  ‫ورامین ‪۶۱۲٩‬‏ ‪.‬‬   ‫‪ ۶‬وس‬      ‫خردمند ‪.‬‬   ‫بدن روشن و جان‬                ‫بشورد آنگاه با مادرش سو گندن‬
   ‫بقیه در صفحهٌ ‪۱۹۱۱‬‬

                                                                                 ‫بقیه ازصفحهٌ ‪۹۸۱۱‬‬
  ‫درهم‌ریخته ومجزی نکرده‌اندو«ملوك» چاپ اسدی غلط است وعطف «ملوك» بر «امیر» درست با‬
    ‫فصیح نبت ‪ .‬بجای «ملو کٹ“ در مر رود کی «ببوکه" است بعنی عروس » وشمراوچنین است ‪:‬‬
       ‫چنانکه جاه من افزون بداز امیر وبگه‬               ‫باکه مت دراین خانه بودم وشادان‬
      ‫مرا بگوگی کز چه‌شده‌است شادی‌سوگك ؟‬                ‫کون همانم و خانه همان وشهرهمان‬
                             ‫و رود کی درشمر دنر باز همین مضمون را آورده است باهمین کلمه ‪:‬‬
         ‫اندرین خاله بان نو بو که ‪.‬‬              ‫بس عزیزم بگسراهی سال وماه‬
 ‫و « بویگه“ را در فرهنگها باکاف فارسی ضبط کرده‌اند ؛ بی ظاهرا ضبط فرهتگها که‬
  ‫سوگه باکاف فارسی است صحیح است ‪١ .‬ا‏ اءتهمه اطمینان کامل ندارم زبرا قدما کاف و گاف را‬
   ‫گاهی فافه کرده‌آند ‪.٩‬‏ «بادداشت ابی دربارة اشمار حافظ ‪ .‬مجلة داتس سال ‪ ۲‬شمار؟ ‪۸‬ص‪-۲*8‬‬
  ‫‪ ۳‬هرن این کلمه را درفارسی ‪ 805‬ضبط کرده » قی‪ :‬ارستا ‪( 20025167202 -‬هملةٌآ س)‬
  ‫هندی باستان ‪ 2606 -‬بمعنی اذت » درد » الدوه و عزا‪.‬قریب بممنی ( حرارت شدید » شمله )‬
  ‫(قی ‪ :‬آتش وگه " در شاهنامه ‪٩۱‬‏ بیت ‪ » )۲4‬ارمتی ‪80‬ا‪( 5‬اندوه وعزا) «اسشق ‪٩٥۷٩‬‏ ورك‬
                                                                                   ‫‪.‬‬   ‫‪۹‬‬     ‫هوشمان‬

‫( برهان قاطع ‪) ۴۵۱‬‬
```


## [2026-09-06T20:39:29.840Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef dig(s): return ''.join(str(fa.index(c)) for c in s)\nfor i,p in enumerate(t):\n    for m in re.finditer(r'بقیه\\s*(?:در|از)\\s*صفح\\S*\\s*([۰-۹]+)', p):\n        print(i, m.group(0).replace('‌',''), '->', dig(m.group(1)), 'rev', dig(m.group(1))[::-1])\nEOF",
 "description": "Calibrate BQT v2 leaf-to-page offsets"
}
```


### [2026-09-06T20:39:31.441Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:39:36.875Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re,unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef clean(s):\n    return ''.join(c for c in s if unicodedata.category(c)!='Cf')\ndef dig(s): return ''.join(str(fa.index(c)) for c in s)\nfor i,p in enumerate(t):\n    p=clean(p)\n    for m in re.finditer(r'بقیه[^\\n]{0,20}?صفح\\S*\\s*([۰-۹]+)', p):\n        print(i, repr(m.group(0)), '->', dig(m.group(1)), 'rev', dig(m.group(1))[::-1])\nEOF",
 "description": "Calibrate BQT v2 offsets (cleaned)"
}
```


### [2026-09-06T20:39:38.915Z] TOOL RESULT

```
85 'بقیه از صفحهٌ ۹۲' -> 92 rev 29
149 'بقیه از صفحةٌ ۰' -> 0 rev 0
187 'بقیه در صفحةً ۰۳۷' -> 037 rev 730
244 'بقیه از صفحهٌ ۵۸۷' -> 587 rev 785
257 'بقیه در صفحةٌ ۸۹۷' -> 897 rev 798
314 'بقیه در صفحهٌ ۵۵۸' -> 558 rev 855
367 'بقیه درصفحةٌ ۸۰' -> 80 rev 08
388 'بقیه از صفحهٌ ۷۲' -> 72 rev 27
389 'بقیه در صفح ۰۳' -> 03 rev 30
433 'بقیه از صفحة ۷۲' -> 72 rev 27
434 'بقیه در صفحهٌ ۵۷' -> 57 rev 75
441 'بقیه در صفحٌ ۶۸' -> 68 rev 86
442 'بقیه از صفحهٌ ۹۷' -> 97 rev 79
588 'بقیه در صفحهٌ ۷۲۱۱' -> 7211 rev 1127
598 'بقیه از صفحةٌ ۰۳۷۱۷' -> 03717 rev 71730
628 'بقیه در صفحٌ ۵۹۱۱' -> 5911 rev 1195
629 'بقیه از صفحهٌ ۶۹۱۱' -> 6911 rev 1196
654 'بقیه در صفحهٌ ۱۹۱۱' -> 1911 rev 1191
654 'بقیه ازصفحهٌ ۹۸۱۱' -> 9811 rev 1189
```


## [2026-09-06T20:39:59.203Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (659,653):\n    print('======= leaf',i,'=======')\n    print(t[i][:700])\n    print('--- tail ---')\n    print(t[i][-1200:])\nEOF",
 "description": "Print BQT leaves 659 and 653"
}
```


### [2026-09-06T20:40:01.644Z] TOOL RESULT

```
======= leaf 659 =======
  ‫صهراب‬                                                                                       ‫‪٩‬‬      ‫‪-‬ي‪‎‬‬


                                                     ‫سه خواهران‪ *۰.‬کنابه‌ازبنات‌باشد‪.‬‬
‫تحتالی‬        ‫ن‬
              ‫وو‬‫کالك‬
                   ‫سفتح‬
                      ‫سشهر =ب‬                       ‫وآن سه ستاره است بهلوی حم از حجملهعت متارء‬
‫ورای فرشت » عمارلی بوده مشتمل‌برسه گنبد که‬           ‫بنات‌النمش که آنرا هفت اورنکه و دبا کبرلیز‬
‫نعمان‌بن منذر بجهت معبد بهرام گور ساخته بود‬                   ‫گوبند » وچهار دیگ رکه‌صور ت کرسی‬
‫و چون بزبان پهلوی کنید را دیرمیگویند آبرا‬                                                           ‫خوانند ‪.‬‬
 ‫بدا
--- tail ---
 ‫بب‬‫چو‬
   ‫د شاهنامة بخ ج ‪٩‬ص ‪6۳۷۲٩‬‏ ‪.‬‬
   ‫؛پراب ) اوصل « سکهارو »‬  ‫‪:‬رخ س‬  ‫س‬
    ‫ک(اوسرخ) ‪ ۷‬وصف تت بای ءوصوف لته ‪( « :‬آفربدون) اول خروح بکراو شت تا پادشاهی‬
  ‫نامها برحکم آنك شبالی میکردند ‪ :‬سیدد کاو ‪ ۰‬وصاه گاو ‪ .‬وسهر گاو‬               ‫بروی مقرر شد » وگ‬
  ‫افریدون بیرون آمد سلاح اوکرز بود‬            ‫یعنی سرح کاو و ماننده اين نهادند وازاین جهت چون‬
   ‫بعنی سلاح چویانان چوب بائد چون عصا و مانند آن ‪ ۰‬و سرکرز اگواو ساربود بمثال نامپا ‪» .‬‬
   ‫‪۵۲۱٩ _ ۴‬‏ = سرخاب ‪0۵5۲٩‬‏ («‪.‬م‪ , ).‬از ‪:‬‬                    ‫« فارسنامه ‪ .‬ابن البلخی ‪. ۲۱‬‬
   ‫؛ب‪+‬ممنی دارندةآب ورنگ‌سرخ (چنانکه باقوت‌باشراب )«بوستی ‪.‬‬  ‫ب‪)۰‬‬
                                                               ‫آ‪.‬م‬
                                                                 ‫‪ = ۲‬سرخ (ه‬
   ‫دام نامه ابرانی ص ‪ .»۳۱۳‬درسلله ملو که طبرستان دوتن راسرخاب ویکی راسهراب لوشته الد‬
                                                   ‫«مرزبان نامه ‪ .‬تهران ‪ . ۷۱۳۱‬مقدمه ص ‪2‬؟ ‪.‬‬
                                                   ‫= سدلي رك ‪ :‬سه در ‪.‬‬                 ‫‪¥‬ەدله‬
                                                                                           ‫س‬

======= leaf 653 =======
 ‫وحیله باشسوکرم کندم خوار رایز گوینده ‪.‬‬           ‫سو‌سه ‪ = ۱‬بروزن بوسه ‪ ۰‬کرمی باشد‬
 ‫سوفچه ت بفتح جیم فارسی بر ون‬                                     ‫که در گندم افتد وضایم کند ِ‬
 ‫دو کچه » ریز هرچیز راگوبند ‪ -‬وبه‌نیشوشة‬          ‫وین قطه دار »‬
                                                              ‫سوغه ‪ -‬بنتح اول غ‬
                          ‫زر وسیم همآ هده است‪.‬‬
                                                   ‫مرسومی باشد‪ .‬کهمپاهیان از علوفه وماهیانخود‬
 ‫قرا‪ -‬بقتح اك ورای بی‌طه‌بالف‬       ‫سو‬                                        ‫بنوبند گان دهند ‪.‬‬
 ‫کشیده‪ .‬تاموزبر کیقبادبن فیروز پدر انوشیروان‬      ‫سوق ‪ - ۴‬بن‪ ,‬اول و سکون ثالی وفاء‬
       
--- tail ---
( 4۲×65‬موسوم به زرهر ‪ )۲011017222‬از دودمان قارن ومسقط‬
  ‫رای وی بلوك اردشیر خوره و از مردم پاری بوده است « کربستنمن ‪ .‬ساسان ‪ * ۵۰۱‬وی در زمان‬
  ‫داشته« کرستنسن‬        ‫پادشاهی هیروزساسالی حکمران ابالت سکتان بود ولقب هزارفت ‪(06-۱‬‬
  ‫‪ ۷‬ب‪-‬ونالی ‪ 5۵05100۹‬بدعنی استاد » زبردست ‪.‬کیکه دارمور‬                     ‫ابا ‪. ۸۹۷-۵۹۲‬‬
‫زلد کی هوشمند وزیرك است » خردمند‪.‬حکمای سبعهٌ ولان را ‪latsihpoS‬‏ میتاهید لد ‪ -‬درآتن‬

  ‫باستاد دستور زبان » معالی ویبان س»پاست و رباضیات اطلاق میشد ‪« .‬فرهنگه بودالی‪ -‬انگلیسی‪.‬‬
 ‫‪ - 6‬مرحوم قزوینی در حاشيةٌ « دبوان‬         ‫رك ‪ :‬سوف (متن وحاشیه) ‪.‬‬       ‫‪۸‬‬      ‫لدل واسکات»‪ .‬‏‬
‫حافظ ص ‪ » ۰۲۳‬نوشته ‪ :‬سوك بضم سین بمعنی ماتم ومصیبت * طاحراً باکاف عربی است ‪ :‬چه در‬
 ‫فرهنکه سروری آنرا در باب سین باکاف تازی کذر کرده است قبل از باب سین باکاف فلرسی و‬
  ‫علاوه برین رود کی در دو بیتی که در فرهنکه اسدی (چاپ اقبال ص ‪ )۳۸۲-4۸۲‬مکذوراست‬
  ‫آترا با «ملوك» قافبه بسته‌است» ولی درفرهنگهایی که درهند تألیف شده است از قبیل جهانگیری‬
 ‫و غیاث اللغات وموید الفضلاء اکیلنمه را باکاف فارسی ضبط کرده‌اند و ظاهراً اين تلفظ » تلفظ‬
‫هندی بايد باشد ‪ » .‬آقای دهخدا درین مورد نوشته اند ‪ « :‬در لفت نامه اسدی کاف و کاف را‬
  ‫قبهد رفح ‪۰۹۱۱‬‬
```


## [2026-09-06T20:40:20.848Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'سهرورد' in p or 'سهروَرد' in p: print('SOHRVARD leaf',i)\nfor i in (170,):\n    print('=== leaf',i,'===')\n    print(t[i][:1200]); print('--- tail ---'); print(t[i][-900:])\nEOF",
 "description": "Print BQT leaf 170 and search Sohrvard"
}
```


### [2026-09-06T20:40:22.420Z] TOOL RESULT

```
SOHRVARD leaf 248
SOHRVARD leaf 402
=== leaf 170 ===
     ‫س پات‬                                                                                            ‫خاییسن‬

‫خابیده ‪ = ۴‬بروزن و معتی جاویده‬                            ‫خالیدن ‪» ۱‬بر وزن ساییدن » بمعنی‬
                            ‫وبدندان نرم شده باشد ‪.‬‬                    ‫بدسان نرم کردن وجاوبدن باشد ‪. ۴‬‬

                                                 ‫ليان دو یم )‬

                  ‫درخای نقطه دار بابای ایح مشتمل بر هجده (‪ )0‬لفت‬

‫چهار دبوار‬       ‫وزن مغاك ‪.‬‬     ‫بر‬        ‫خباك‬               ‫چت وچللاله‬    ‫خیاره ‪ = ۴‬بروزن‌هزاره‪.‬‬
‫س رکشاده را گویند که شبها گوسفند و کاو وخر‬                                  ‫وجلد وهار در کارها را گونند ‪۱‬‬



     ‫همآمده الست ‪۷‬‬      ‫ریسی‬
                           ‫فاابا‬
                               ‫نگیفزته‌اند ؛ وب‬                                           ‫‪E‬‬            ‫‪۳‬‏‬
                                      ‫‪۲‬‬                                                 ‫وز خطه‌وار بتحتالی‬
‫دال ابچد‬       ‫‪ 2‬سکون‬   ‫خیا یدتب بفتح اول‬                                                ‫نوعی از خطم‬     ‫رسف‬

‫بروزن روایت » بعنی" بخاید ودر زبر دلدان نرم‬                                             
--- tail ---
م مفتوح) وخبیزه"(بضم اول ودوم مشددمکسور‬
     ‫رچبارم مقتوح) وخبازه (بضم اولو تشدید دوم مفتوح وچهارم مفتوح) د المنجد » = بونالی‬
     ‫هرفاح ‪ » (6‬فرانمه ‪ 6۷21201‬دك ‪۲‬س ‪ - ۷۰‬خبازی‌الملوك ‪ « 2۷121۷1 2610012‬دزی‌ج‪+‬سص‬
                                                                          ‫‪ -‬كابخ )‪(«..‬‬        ‫‪٦‬‬        ‫‏‪eA‬‬

                  ‫کمندی دشت بر گوران خباک‬                      ‫خدنگش بیشه برشیران قفص کرد‬
     ‫دقدفی‌طوسی‪« -.‬لفت فری ‪Yo“.‬‏‬

                                     ‫‪ - ¥‬فيز « خباك ‪ ۰‬خناق بود » رود کی (سمرفندی) کوید ‪:‬‬
            ‫تا بمنت احسان باذد احسن اله جزاك ‪.‬‬                 ‫بدوزسه بوسه رهاکن‌این دل ازگرم خباله‬
     ‫«لفت فرس ‪4۹۲‬؟‪.‬‬                   ‫‪۱‬‬                                          ‫‪۱‬‬
       ‫‪٩‬‏ = ‪۹۷۱ ila < sudniramaT acidni‬‬                               ‫‪ - ۵‬تلفظی در «خاید»‪ .‬رك‪ :‬خاییدن‪.‬‬
```


## [2026-09-06T20:40:40.652Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== BRT suxra-var ==\"; grep -n \"suxra.var\\|varada-\\|var»da\\|Rose\" BRT.txt | head -15\necho \"== SOD swgnd ==\"; grep -n \"swgnd\\|swkn\\|oath\" SOD.txt | head -20",
 "description": "Grep BRT for suxra-varəda and SOD for oath"
}
```


### [2026-09-06T20:40:40.711Z] TOOL RESULT

```
== BRT suxra-var ==
22893:•  j.  varaSa-  m.  i)  'Mehren,  Grossmachen' (nur  Komp.).  2)  Name  einer  Pflanze, vll.  "Rose':  yS  bar^smqtt  *frast)rmte  hae- mqsca   'iss:a  "hanvasca   antar).d3ta    "wer
22894:B.  spreitet  und  Haoma-  und  Rosen-  und .  .  Stengel  dazwischen  tut"  N.97.
22896:—  KDs.  väli  -Blurae',  arm.  LW.  vard  'Rose';
22897:Tgl.  np.  ^/ 'Rose'i    s.   daza    Bthl.   WklPh.
== SOD swgnd ==
62502:loathing,  disgust 
62507:loathing,  disgust 
68963:oath 
69037:oath 
79026:promise,  oath 
91385:loathing    8117,8118 
92169:oath  9044,  9053,  10486
```


## [2026-09-06T20:40:41.742Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== DRM leaf 153 (p.131 t.1) ==\"; awk 'BEGIN{RS=\"\\f\"} NR==153' DRM.txt | head -40",
 "description": "Print Darmesteter p.131"
}
```


### [2026-09-06T20:40:43.599Z] TOOL RESULT

```
== DRM leaf 153 (p.131 t.1) ==
ms  en  persan  est  d’une  façon  indubitable formé  de  l’ancien  génitif  perse  (§§  127 — 128)  :   on  est  donc  con- duit a   se  demander  s’il  n’en  serait  pas  de  même  du  substantif. Or,  le  génitif  pluriel  est  en  ânâm  :   baya,  dieu,  bagânâm,  des  Dieux (H.  1;  F.  2;  K.  2).  Donc,  quelle  que  soit  la  raison  logique  qui a   pu  faire  choisir  le  génitif  du  pronom  pour  forme  unique  et générale  du  pronom,  comme  cette  raison  doit  et  peut  avoir  existé pour  le  substantif  aussi  bien  que  pour  le  pronom;  comme,  d’autre part,  le  génitif,  avec  sa  terminaison  ânâm,  offre  précisément  la forme  que  l’on  cherchait  dans  l’accusatif  pluriel  et  qui  n’y  est  pas puisque  cet  accusatif  n’existe  pas,  il  faut  conclure  que  le  pluriel en  ân  est  le  résidu  de  la  désinence  du  génitif  des  thèmes  en  a 1   : ânâm,  en  perdant  régulièrement  sa  finale  âm,  devait  donner  ân.
1.  Vullers  ( Institutiones ,   §   195)  ramène  le  pluriel  ân  au  génitif  âm  : mais  âm  final  est  précisément  tombé  en  persan  :   il  faut  partir  du  thème général  en  a,  génitif  ân-âm.
125
La  langue  moderne  a   conservé  une  expression  unique  qui nous  a   transmis  d’une  façon  irrécusable  cet  ancien  génitif  en ânâm  et  où  le  sentiment  moderne  reconnaît  pourtant  un  simple pluriel.  C’est  le  titre  de  shâhinshâh  sLi~L*>là,  Roi  des  Rois;  or, ce  composé  qui,  pour  la  grammaire  moderne,  est  la  combinaison de  shâhân,  pluriel  de  shah,  avec  le  singulier  shah,  et  correspon- drait h   la  construction  shah  i   shâhân,  rex-d e-reges,  n’est  que  la reproduction  du  vieux  juxtaposé  des  inscriptions  de  Darius  : khshayathiyânâm  khshâyathiya,  regum-  rex.
§   99.  Origine  des  pluriels  en  hâ.  —   Le  pluriel  en  hâ  (voir les  exemples  §   96)  est  rare  dans  les  textes.  Il  ne  paraît  pas dans  le  Commentaire  de  l’Avesta;  il  paraît  dans  le  Bundehesh et  dans  la  transcription  parsie  du  Minokliired  :   la  forme  entière du  suffixe  est  là,  non  pas  hâ  comme  en  persan,  mais  ihâ.  On trouve  ainsi  :
kôfihâ,
rôtihâ,
cashmakihâ,
pôçtihâ,
les  montagnes,  pluri
```


## [2026-09-06T20:40:53.430Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== SOD_pages swgnd ==\"; grep -n \"swgnd\\|swknd\\|swk'nt\\|swknt\" SOD_pages.txt | head -20\necho \"== SOD oath ctx ==\"; sed -n '68955,68975p' SOD.txt; echo ...; sed -n '69030,69045p' SOD.txt",
 "description": "Grep Gharib Sogdian for oath"
}
```


### [2026-09-06T20:40:53.514Z] TOOL RESULT

```
== SOD_pages swgnd ==
16320:                xur ©*hvan IE *swel -»swk'nt                          4425 Ywrmzt rwc     S                 jjj-*^^ "u Jj' jjj
29832:                                                                 9053 swk'nt B, S
29849:      soyand    ©<Av. saokdnta    =*swqnt xwr-, swk'nt
== SOD oath ctx ==
*»j 


5  ixf ■ 


soyand   ©<Av.  saokdnta   =*swqnt  xwr-,  swk'nt 

oath 

BBB  p97  b47;  GMS  250 

9045  swys-    B,  M  o^co-ljl;  ij^^ 
suxs   ©Yaghn.  suxs  =»syws-,  swc-,  swxs- 
(fcObe  burned 

VJ  20b;  SCE  151;  BSTBL,  Vim.  117;  Hen.  JRAS 
1944,  138.14;  GMS  647 

9046  swyst-  =*  ^ywst- 

...

iXS  > 


sokand  ©Av.  saokdnta-,  Khwar.  sknt  =»swqnt 

xwr-,  swynd 
oath 
GMS  250;  TSP  3.220;  STi  31.2;  BSTi  188,  296; 

BSTii  846.17,  18,  854.24:  C2,  23R24,  69R15,  16; 

Frag.  Len.  65.1,  10;  Schwartz.  SI,  Cahier  7, 

293-5
```


## [2026-09-06T20:40:54.181Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==159' DRM.txt | head -30",
 "description": "Print Darmesteter leaf 159"
}
```


### [2026-09-06T20:40:55.836Z] TOOL RESULT

```
de  là  *kôfkhâ,
kôfhâ.
C’est  à   la  première  de  ces  deux  phases  que  nous  reporte  la forme  pehlvie  qui  a   dû  se  lire  anciennement,  non  pas  ihâ,  mais ikhâ  ;   l’t  est  une  insertion  euphonique  amenée  parla  rencontre de  khd  et  de  la  consonne  finale;  par  le  seul  fait  que  l’on  déplace I   nspirée  une  voyelle  s’intercale  entre  la  consonne  finale  et  l’as- piration :   la  filière  est  kôfâkh,  kôf(e)-khâ,  kîf-iliâ.
§   100.  Pluriels  arabes.  —   L’influence  croissante  de  l’arabe a   amené  dans  la  langue  littéraire  une  formation  nouvelle,  mi- arabe,  mi-persane.
Tandis  que  le  pluriel  en  hâ  s’appliquait  à   un  grand  nombre de  substantifs  arabes  (ce  qui  d’ailleurs  n’est  pas  plus  étonnant que  de  voir  un  substantif  anglais  ou  russe  emprunté  par  le  fran- çais prendre  le  s   du  français  au  pluriel),  il  arrivait  que  le  plu- riel propre  à   la  langue  arabe  pénétrait  la  langue  persane  et empiétait  sur  ses  désinences,  même  dans  le  domaine  du  voca- bulaire persan.  Le  pluriel  des  féminins  arabes  en  âit  Oî  donna  :
Obto  dahât.  villages OUI)  b   agitât,  jardins
farmâyishât,  ordres
de  a
9
130
Quand  le  thème  est  terminé  en  s,  par  imitation  des  pluriels en  du  persan,  l’on  intercale  le  représentant  arabe  de  S, c’est-à-dire  r*.  et  l’on  dit  :
OLsrusJüs.  qala  jât,  forteresses  de
nâmajât,  lettres  de  ^b
Ces  formations  appartiennent  d'ailleurs  h   la  langue  des  sa- vants et  des  pédants  plus  qu'à  la  langue  populaire.  Une  influence arabe  qui  a   pénétré  plus  avant  dans  la  langue  du  peuple,  mais sans  l'altérer  parce  qu’elle  n’y  introduit  pas  un  procédé  de  for- mation nouveau  et  n’agit  que  sur  le  vocabulaire,  c’est  l’addi- tion du  pluriel  persan  à   des  pluriels  arabes  pris  pour  des  sin- guliers :   il  s’agit  naturellement  des  pluriels  b
```


## [2026-09-06T20:41:07.133Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=29860 && /\\[pdf page/ {p=$0; n=NR} END{}' SOD_pages.txt\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<29860' | tail -3\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1>29820' | head -3",
 "description": "Find SOD page tag for oath entries"
}
```


### [2026-09-06T20:41:09.773Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:41:13.610Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if \"swk'nt\" in p or 'swynd' in p or 'saokdnta' in p:\n        print('leaf',i,'-> printed ~',i-66)\nEOF",
 "description": "Find SOD leaf for sogand"
}
```


### [2026-09-06T20:41:15.245Z] TOOL RESULT

```
leaf 241 -> printed ~ 175
leaf 432 -> printed ~ 366
```


## [2026-09-06T20:41:21.396Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['IRN','FFD']:\n    v=d[k]; print(k, v.get('page_offset'), '|', v.get('cites'), '|', json.dumps(v.get('scans'),ensure_ascii=False)[:400])\"",
 "description": "Check IRN/FFD offsets"
}
```


### [2026-09-06T20:41:23.004Z] TOOL RESULT

```
IRN 222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368. | None | [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "first_printed": 1, "last_printed": 210, "pdf_offset": 11, "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"}]
FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | None | null
```


## [2026-09-06T20:41:26.498Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IRN p.128 = pdf 139 ===\"\npython3 - <<'EOF'\nt=open('incoming/IRN/IRN_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(len(t))\nimport re\nfor i,p in enumerate(t):\n    if '[pdf page' in p[:60]: pass\nprint(t[138][:2500])\nEOF",
 "description": "Print Iranvij p.128"
}
```


## [2026-09-06T20:41:27.845Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD p.61 = pdf 66 ===\"\npython3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[65][:2000])\nEOF",
 "description": "Print FFD p.61"
}
```


### [2026-09-06T20:41:28.377Z] TOOL RESULT

```
=== IRN p.128 = pdf 139 ===
222
[pdf page 139]
۱۳۸ ایرانویج
2 چندین بار در اوستا آمده‌است از آنجمله است در وندیدادف رگرد و ر بند۲ .
معادل فارسی‌باستان این واژه درکتیبه‌های فارسی باستان نیامده است ولی آنرا
می‌توانیم از رو ی کلمدٌ اوستایی آن وبنا بر قواعد زبانشناسی ایرانی باز ساز ی کنیم .
این کلمه در فارسی‌باستان می‌بایستی ۷۵۳۵4۶ بوده باش د که در دورءٌ فارسی میانه در
پهلوی‌ساسانی)۷27و 4 می‌دهد و درفرهنگهای فارسی‌نیز بصورت «ورد» باقی مانده
است . وا ورد بمعنای گل در نام بسیاری از آبادیهای ایران باقی مانده‌است ,ورد
آورد 202۳4 - ۷2۲4 که روستایی است نزدیک تهران » نامش مرکب است از
40 و 20270 بمعنی گلآور و نام سهرورد که روستایی است از روستاهای زنجان‌و
محل تولد شیخ اشراق شهاب‌الدین‌سهروردی است نیز از همین ريشه است .جزء اول
کالم سهرورد 5057272۳4 واه 9108۴ یا 3137۴ اس ت که صورت صحیح كلم سرخ
است ووازهٌ سرخ فارسی‌شکل قلب شدةٌ 857 است و سهرورد بمعنی
سرخ گل است .

واه ورت ۷27 در دورهٌ اشکانیان به ارمنستان راه می‌یابد و بصورت ۷2۲۳
بمعنی گل سرخ استعمال می‌شود. از مشتقات این کلمه در ارمنی می‌توان نامخاص
نوارت ۸76۷3۶1 را یاد آور ش دکه از دو واه ایرانی 86۷ بمعنی نو و ۷371 بمعنی
گل‌سرخ مرکب شده است و معنی آن نوگل يا غنچةٌ گل سرخ است ونام زنان
ارمنی است. همچنین نام خاص وارتوهی ۷370۵01 از واژ ۷3۶4 و پسوند تأنیث

فا ترکیب یافته ونام وارتوش نیز از همین ريشه است.

واژهٌ ورد ۷2۳۵ ازسوی دیگر بزبان آرامی‌راه یافته و از آنجا بزبانهای دیگر
سامی از جمله به‌عربی رفته است وورد در فرهنگهای عربی بمعنی گل سرخ ورنگك
سرخ یاشکوفه وگل زعفران و اسب گلرنگه‌آمده است . واژورد ۷2۳4 پهلوی دردوران

پارسی میانه ونیز در زبان پارسی و لهجه‌های گونا گون آن تحولات گونا گون یافت .
واژهٌ ۷2۶۲۵ درفارسی ببورت ورتا دربرهان قاطع بعنوان وارْهٌ زند وپازند (هزوارش)
آیده است و چون این واژه در زمان ساسانیان به زبان آرامی راه یافته بوده است» از
```


### [2026-09-06T20:41:30.257Z] TOOL RESULT

```
=== FFD p.61 = pdf 66 ===
115
[pdf page 66]
ماده‌های ماضی و مضارع فارسی دری _ ۶

سرای < فارسی میانه 8737 + ایرانی باستان ۹73۷-۵98*. 272 نشانه‌ای بوده که برای
ساختن مادهٌ مضارع از ريشه به کار می‌رفته است. ۶739 صورت بالاندةٌ ريشهٌ 872۷ است.

امروزه مشتقات «سرای» را به ضم «س»» به قیاس با «سرود»» تلفظ می‌کنند. این
قیاسی نادرست است. «س)» را باید به فتح خواند.

دا :

سفت < فارسی میانه 8011 < ایرانی باستان ۶۷1-1۵*. برای 12 -> آراست. 0اه صورت
اصلی 9۷۶ است» 0 پیش از به ۶ بدل شده است. ۶0 صورت ضعیف 820 است و آن به
معنی «آراستن» است.

ستب ه فارسی میانه 5010 + ایرانی باستان ۴*۹8 پیش از آخرین صامت ريشه:
برای ساختن مادهٌ مضارع.از ريشه» افزوده شده است. «نهفتن» هم از ريشةٌ 9۷0 آمده
است > نهفتن.

سکالیدن

«سگالید» ماد ماضی جعلی است. از مادةٌ مضارع ساخته شده است.

سگال + فارسی میانه 913۶ < ایرانی باستان ۶-137-۵*. برای 2 > آرای. 8 پیشوند
فعلی است. 137 صورت بالاندةٌ ریشه است. صورت افزودهٌ آن 187 است» به معنی
«اندیشیدن». ۱

مادهٌ ماضی ۶27۲ در فارسی میانه 81370 است» از ایرانی باستان ۶۵-۷3۶-12. برای
> 12 آراست.

سوختن ِ

سوخت + فارسی میانه 9071 + ایرانی باستان ۶۵-۱۵*. برای 2 > آراست. 521
صورت اصلی ۶27 است» ۴ پیش از ابه # بدل شده است. ريشةٌ 920 به معنی
(سوختن) است.

سوز <فارسی میانه 952 « ایرانی باستان 8۵06-۵*. برای 2-> آرای. تبه جای ۲ آمده
است.
```


## [2026-09-06T20:41:51.967Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== WLD Bd1 khad ==\"; grep -n \"khād\\|khad-\\|khadati\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"== AHD keuk ==\"; grep -n -i \"keuk\\|kuknos\\|cygnet\" AHD_watkins1985.txt | head -20\necho \"== CHEUNG ==\"; grep -n \"sauk\\|\\*xād\\|xād-\" CHEUNG.txt | head -20",
 "description": "Grep WLD, AHD, Cheung"
}
```


### [2026-09-06T20:41:52.031Z] TOOL RESULT

```
== WLD Bd1 khad ==
21562:Der Yergleich von khadati als *q,no-do ( qndo ) mit lit. kandu ,beiBe“, gr. 
24743:Aber ai. khadati „zerbeiBt, kaut, iBt“ wobl nicht als *q t nad- hierher, 
== AHD keuk ==
628:keuk-. To be white, be bright, shine. Suffixed zero-grade form *kuk-no- in Greek kuknos, swan: CYGNET, CYGNUS. [Pok. keuk- 597.]
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
== CHEUNG ==
22279:*IE COGNATES: Lith. Saükti, Latv. saukt ‘to call’, Toch. B sausäm ‘calls’ 
52829:saukt, 340
```


## [2026-09-06T20:41:53.742Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== KLN cygnet ==\"; grep -n -i \"cygnet\\|kyknos\\|cycnus\" KLN_1966.txt KLN_1971.txt | head -20\necho \"== SKT cygnet ==\"; grep -n -i \"cygnet\\|swan\" SKT.txt | head -10",
 "description": "Grep Klein and Skeat for cygnet"
}
```


### [2026-09-06T20:41:53.813Z] TOOL RESULT

```
== KLN cygnet ==
KLN_1971.txt:62627:cygnet, n., a young swan. — Dimin. of F. cygne, 
KLN_1971.txt:62629:of cycnus), fr. OF. cisne , fr. VL. cicinus (which 
KLN_1971.txt:62630:occurs in the Salic law), fr. L. cycnus, fr. Gk. 
KLN_1971.txt:62637:‘swan’. See cygnet. 
KLN_1966.txt:10070:cyesis,  n.,  pregnancy.  —  Medical  L.,  fr.  Gk. xurjoip,  ‘conception,  pregnancy’,  fr.  xusiv,  xueiv, ‘to  be  pregnant’,  whence  also  xOfrx,  ‘anything swollen;  a  wave’.  See  cyma  and  cp.  cyathus. cygnet,  n.,  a  young  swan.  —  Dimin.  of  F.  cygne, ‘swan’  (refashioned  after  L.  cygnus,  a  variant
KLN_1966.txt:10071:of  cycnus),  fr.  OF.  cisne,  fr.  VL.  cicinus  (which occurs  in  the  Salic  law),  fr.  L.  cycnus,  fr.  Gk. xuxvo?,  ‘swan’,  which  is  prob.  of  imitative  ori¬ gin.  Cp.  Russ,  kykii,  ‘swan’s  cry’.  Cp.  also Cygnus.
KLN_1966.txt:10072:Cygnus, n.,  i)theSwan  (name  of  a  constellation); 2)  the  genus  of  swans  (ornithol.)  —  L.  cygnus, ‘swan’.  See  cygnet.
== SKT cygnet ==
2266:brose,  pottage.  (C.)  Gad.  bntkoi brose.  From  the  same  root  as  K.  Brew. broth.  (£.)  A.  S.  br^.  -  A.  S.  br^^wen pp.  of  brtSwan,  to  brew.  +  Icel.  ArvB M.  H.  G.  brot;  cf. G.gibraudt,  as  msdi « is  faRwed  at  once.   And  see  Bread,
4464:Cud.  (E.l  M.  £.  cudt.  code,  guide.  That which  i»  chewed.  Peihaps  from  the  same base  a*;  A.  S.  eeSwan,  to  chew ;  but  net  — P|j.  chewed,  because  ibc  verb  was  orig. strong-     Cf.  sudi,  uUied  lo  seethe.
4608:CYGNET.
4609:cnetv  K  young  twan  (F.  -  L.) of  O.  F  ri^nt,  %  swan.  Strangely ikit  O.  ¥.  word  is  mot  from  L. a  avian ;  but  the  oUlest  0.  F. wmt  ritnf,  from  Low  L,  UiinuSj See  Uiti;  4tli  cil  p-  ;I4. ^liadar.<F.-L.-Gk.)  O.V.d/in^fn, r  tyiimdwt-  ••  L.  cyliruirus.  —  tilt. irSfM,  a  roUrr,  c^'liniler  —  Gk.  wA/fStfir, |oU ;  from  ovAf^i*'.  to  roll.    CC.  Kuss.
17850:Sound  (3),  a  noise.  (F.  —  L) </  ii  added.     M.  E.  so»/n    — >  F.   lou ro/tum,  accof /tfMi/.f,A*sou(id.-fSkt sound.     (^  SWAN.)
18983:E.  use).  4*  ^1-  H-  G.  rwatH,  sm schtvamm,  a  sponge,  fungus;  Dt Goth.  nvamfHj,  sponge;  Low  G. rzvamf;  funpus ;  A.  S.  swam,  funr from  v'lsWAM,  loswim.  0.  FarS lo  Gk.  co^iKf>ii%,  spong)',  Goth^ swamp ;  and  even  tu  Sponi also  prov.  E.  swank,  stvau^.  a as  E.  swank :  £.  swamp ::  Gk.
18988:'muh  ;  I  ui  ,iuanH  ts  from  a  toUlly source ;  »ec  QuelL .dler.achcat.  (G.)    XVIII  ccnt.- tekwtHJUr,  ui  extravagant  projector,  a U'JIei.  — G.  schwindiiH,  to  be  diz^y,  act ughllcMly.  —  G.  sihwindtH,  to  decay, k.  vanish,  fail.  4*  A. S.  sufinJaM,  pt  t. tm^,  to  bui£iiifib. irine ;  see  Sow  (t). Wing,     (E.)       M.  E.  jwingtn,    pt    t. \Mg,  pp.  ntfUM^n.     A.  S.  swingan,  pt.  t. M^,   pp.  rufungen,   to  scourge,  also   to j  flutter,    flap  with    the  wingv -4- Swed. pi,    Dan.  JMffxv,  to  swing,  whirl;    0. vii^gm.    ^Base  SWANG,  nasalised  form WAG.)    Allied  to  Svay. pHnge,  to  beat,    whip.    (£.)      M.  K. iTjKW.      A.  S.  su'cnffan,  to  shake,   to^  ; ■f,  A  blow ;  the  causal  form  of  Swing. k  *  to  flourish  a  whip.* Prln^le.  a  slafiT  for  dressing  flax.   (£.) C.  nt'tM^Un,   to  beat   flax  ;    rmmgU,  a Hglc.    This  answers  loan  A. S.  nvingti*, tcr,   from    nvingan^   to   beat ;    see Cf.  A,  S,  sivi»£(U,  a  scourging. rixk^e-tree,  the  bar  that  swings  at keels  of  harnessed  horses.    (£.)     M.£. {ie-/r/.  «  M.  E.  rwirt^r,  a  bcnter,  but .a  swinger,*  or  that  which  swings;  fr^, of  wood ;  we  Tree.
22667:whence  ^SWAIj,  to  agitate,  boil  up, swell:  VSWAP.  to  move  swiftly;  alw TeuL  v^SWAM,  to  swim,  Tcut  ^SS^'KG. to  sway:  and  Tctit.  VSWANG,  to  swing.
22737:f  For  roots  SWA,  SWAL,  SWAP^ and  the  Teutonic  bases  SWAM,  SWAGj^ SWANG,  sec  no.  ^ga.
22739:453.  VSWAN,  to  resound,  sound. 464.  y^SWAP(.V'SWAB),toslecp» slumber.
```


## [2026-09-06T20:42:09.779Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== CHEUNG sauk/xad ==\"; grep -n -i \"saok\\|sauk\\|sōxtan\\|soxtan\\|xāy\\|xay-\\|HAD\\b\" CHEUNG.txt | head -25\necho \"== WLD Bd1 p.341 ==\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(len(t))\nimport re\n# find leaf containing 'khadati'\nfor i,p in enumerate(t):\n    if 'khadati' in p or 'khādati' in p: print('leaf',i, p[:80].replace('\\n',' '))\nEOF",
 "description": "Grep Cheung and locate WLD p.341"
}
```


### [2026-09-06T20:42:11.924Z] TOOL RESULT

```
== CHEUNG sauk/xad ==
147:many records of the database and incorporated (recent) literature that I had 
188:important references which I had overlooked sofar. His contributions have been 
244:Europaea, Ravenna 2003. Since 2003 many important works, which had to be included in my Dictionary, 
284:Finally, with regard to modern Iranian languages I had to limit myself to a 
3127:*ni-daja- < *ni- + *daH? and *ni- + *had respectively. 
3131:from a nasal pres. formation *Ci-naH-. Naturally, interference with the root *had ‘to 
3132:sit, be seated’ or its corresponding prefigated formation *ni-s/had ‘to sit down, 
8914:*had 125 
8937:*had ‘to sit, be seated’ 
9647:Sh. (Baj.) wixi(y)-/wixid, Rosh. wixay-/wixid, Bart. wixi-/wixid, Yzgh. wix"ay-/ 
10057:ua-suff.), Sh. xay-/xüst, (Baj.) xi-/xust, Khf. xay-/xost, Rosh. xöy-/xost, Bart. xiy-/ 
10379:(LIV:230; Pokormy: 287 ff.). The Ir. continuation *Had appears to have been 
10726:*NWIR: (?) Qohr. ah-/aha(d)- ‘to be seated, remain’ (rather from *had ?) 
12864:(Y Av. zadanha (pl.) ‘backside, anus’, cf. Skt. had, EWAia Ш: 532). 
20058:morphologically impossible (*pa-zd- ‘absitzen’, from *had), on which see *pazd'. 
21432:35р. BMP /abesihéd/, SUBJ. 3sg. MMP ’bysyh’d, BMP ’bysyh’t /abesihad/ || (+ *fra-) Pres.: SUBJ. 3sg. 
22188:sweynyt /sozened/; Inf.: BMP swhtn /soxtan/ 
22220:*NWIR: Widely attested: NP soxtan/söz-, Kurd. (Kurm.) sotin/soZ-, (Sor.) sutan/suté-, 
22279:*IE COGNATES: Lith. Saükti, Latv. saukt ‘to call’, Toch. B sausäm ‘calls’ 
22387:*SANSKRIT: chad ‘to cover, to conceal’ (RV+), chattra (n.) ‘parasol’ (Br.+) 
22622:IND. 3sg. BSogd. ’nskrt’y wm’t ‘had been collected’ 
23225:wiXay-/wixid, Bart. wixi-/wixid, Yzgh. x"ay-/x'ad ‘to open, unlock’, Wa. 
24209:*NWIR: © NP nisém ‘nest’ is rather from the root *had, cf. Pth. nsdm ‘seat’. 
28396:*KHOTANESE: khad- ‘to wound, hurt’ || (+ *aua-) OKh. vahas- ‘to smite’ || (+ *pati-) 
28397:páha- (pihei-) ‘to strike’ || (+ *ui-) gguhad- ‘to harm, wound’ > SGS:25,121, 83, 30 
== WLD Bd1 p.341 ==
895
leaf 349                                          qad   kadh-                            
leaf 401
```


## [2026-09-06T20:42:19.153Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '22150,22290p' CHEUNG.txt",
 "description": "Print Cheung sauk entry"
}
```


### [2026-09-06T20:42:19.193Z] TOOL RESULT

```
*AVESTAN: Y Av. sauruua- (m.) name of a daeuua (V 19.43) 

*KHOTANESE: (+ *fra-) hasura-, hasura- ‘quarry, hunted beast’ 

*NEIR: Oss. I. suryn/syrd, D. sorun/surd, Yzgh. sard/sar- ‘to track, hunt’ 

*MISC: Toch. (LW) A saru, B serwe ‘hunter’ 

*SANSKRIT: sarvä- (m.) name of Rudra (= Siva) > EWAia II: 621 

9 Pinault 2006 is shedding more light on the connection of the Tocharian form with 
the (Indo-)Ir. forms, as made by Bailey, DKS, l.c. Pinault further notes that Sarva is 
called ästar- ‘archer’ in some Vedic texts. The evidence for this root is limited. The 
root is exclusively Ilr. 


“PIE LIV: — | Pok.: 
*REFERENCES: Edel’man 1971: 232 f.; Abaev, Slovar’ III: 171 f.; DKS: 474a 


*saut! ‘to burn, emit flames’ 

*AVESTAN: saoc- ‘to burn’ || (+ *fra-) ‘to extinguish, put out’ = Liste: 63 

Partic.: pres. them. YAv. saocint- (V); Caus.: pres. INJ. 3sg. OAv. saocaiiat (Y 32.14), SUBJ. 2sg. YAv. 
frasaocaiiähi (V 8.75) 

*OLD PERSIAN: ? "Hauc- ‘to burn’ (Werba 2006: 276 ff.) > Kent: — 

Impf.: IND. 3sg. 'aauca' (A Sa) 

*MIDDLE PERSIAN: MMP swc-, ВМР swc- /söz-/ ‘to burn’, (caus.) MMP swcyn-, 
BMP swoyn- /sozen-/ ‘to cause to burn, set ablaze’ > DMMPP: 310a 

Pres.: IND. Ipl. BMP swcym /sozem/, 35р. BMP swoyt /sozed/, 3р1. MMP swcynd, BMP swcynd 
/sozend/, SUBJ. 3р1. MMP “swc nd; Partic.: pres. MMP *swe’n, MMP swcyndg, BMP swe’k /sozag/, 
perf. pass. BMP swht /soxt/, caus. BMP swcynyt /sozenid/; Caus.: pres. IND. 3sg. MMP swcynyd, BMP 
sweynyt /sozened/; Inf.: BMP swhtn /soxtan/ 

*PARTHIAN: swc- ‘to burn, emit flames’ — Ghilain: 63 | DMMPP: 309b f. 

Pres.: IND. 3sg. *swcyd {hapax} 


*sauc | 339 


*KHOTANESE: süjs- (sus-, sü-) ‘to burn [intr.]’ || (+ *apa-) pasüs- ‘to burn’, LKh. 
pasüj- (caus.) ‘to light lamp)’ || (+ *аџа-) vasus- (vasus-) ‘to become pure’, OKh. 
vasüj- (caus.) ‘to purify’ = SGS: 133, 78, 121 

*SOGDIAN: SSogd. swy- (intr.), BSogd. swc, CSogd. swe ‘to burn, kindle’, BSogd. 
swxs- (intr./inch.) ‘to burn [intr.]’ || (+ *apa-) BSogd. ’ps’wc, MSogd. pswe ‘to 
purify, cleanse’, BSogd. ()pswxs-, MSogd. ’ps’wxs- (intr./inch.) ‘to be purified, 
cleared’ || (+ *aua-) BSogd. ’wswxs-, SSogd. ’ws’wxs- ‘to be cleansed, become 
pure’ || (+ *a-) BSogd. ’’s’wys- ‘to burn, be consumed by fire’ || (+ *pati-) BSogd. 
pts’we ‘to set light, kindle’, CSogd. ptswy- (pret. stem) ‘to burn’, BSogd. ptswxs- 
(intr./inch.) ‘to be lit, kindled’ || (+ *fra-) CSogd. fswc- ‘to sacrifice’ (rather *sau&?) 
Well attested: Pres.: IND. 35р. BSogd. swet, dur. CSogd. swctsqwn, SUBJ. 3sg. BSogd. swe’tw, etc. || (+ 
*apa-) Pres.: SUBJ. 1sg. BSogd.1sg. ’ps’wen, IMPV. 2sg. MSogd. pswe, etc. || (+ *aua-) Pres.: IND. 3sg. 
BSogd. ’ws’wxst; Impf.: IND. 350. SSogd. w’s’we; Fut.: IND. 3pl. SSogd. ’ws’wxs’nt k’m; Partic.: perf. 
pass. BSogd. ’wswxtk, ’ws’xtk, etc. || (+ *pati-) Pres.: IND. 35р. BSogd. pts'wct, OPT. 3sg. BSogd. 
pts’we’y; Impf.: IND. 3sg. BSogd. ptyswe, etc. || (+ *fra-) Partic.: perf. pass. CSogd. fswytyt (pl.) 
‘sacrificed’ 


*CHORESMIAN: (+ *abi-) m/fsxs- (inch./intr.) ‘to become pure, clean’, m/fswcy- 
(caus.) ‘to purify, cleanse’ > Samadi: 71 f. 

*NWIR: Widely attested: NP soxtan/söz-, Kurd. (Kurm.) sotin/soZ-, (Sor.) sutan/suté-, 
Bal. sutk/suc- (intr.), sotk/soc- (tr.), Anar. sote/suj-, Abz. sóta/suj-, Abyan. sótta/süj-, 
Ard. süziya/süziy-, Awrom. sotáy/soc- (intr.), Fariz. -sut-/-suj- (intr.), -sujin- (tr.), 
Gz. süz-/süt(ä), sot, Gil. (Rsht.) soyteen/suj- (intr.), Gur. (Kand.) sücián ((in)tr.), 
Ham. sujayän (sot-)/suj-, Jow. bam-sot/-sydz-, -sud3- (intr.), Meim. bem-so:d/ 
be-sot- (intr.), a-sud3- (tr.), Khuns. siz-/süt ((in)tr.), Nn. sote/suj- (intr.), sot, süin- 
(tr), Qohr. sóta/süj-, Sang. -süt-/suzoen- (intr.), Shamerz. -süt-am-/suz-äm-, Soi 
stiht-/a-suj-, Sorkh. -sut-/süz- (intr.), Tr. söta/söj-, Varz. sote/sij- ‘to burn’, (caus.) 
Ard. sünnahe/sünn-, Awrom. soénay/soén-, Gz. süzn-/süznä, Khuns. sizn-/siznà ‘to 
burn [tr.], heat’, Sang. -suzeni-/suzcencen-, Shamerz. suzánám-, Sorkh. -suzán-/ 
suzán- ‘to burn [tr.]’ || (+ *a-) NP asugdah ‘half-burnt firewood’. 0 NP äsugdah is 
from Sogd., cf. Henning 1939: 103. 

*NEIR: Oss. I. suzyn/sygd, D. sozun/sugd ‘to burn; to kindle’, Yghn. suc-, soc-/sücta 
‘to burn [tr.]’, Pash. sw-/swaj-, Yghn. stixs-, suxs-/süxta ‘to burn [intr.]’, Yzgh. soyd 
(vraxti) ‘white (flour)’ || (+ *fra-) Oss. D. reesugd ‘beautiful, beauty’ 

*MISC: Par. sit(u) ‘sour’, Arm. (LW) sug ‘lament’ 

*SANSKRIT: Soc ‘to light, glow, burn’ (RV+) = EWAia II: 655 

The IE origin of *sauc’ cannot be ascertained, perhaps it is a "Reimbildung" with 
*rauc ? 

*PIE — = LIV: 331 f. | Pok.: 597 


*REFERENCES: КРЕТ. 141b, 246b; Ivanow 1926: 422; IIFL I: 289a; EVP: 71; КРЕП: 204; Christensen, 
Contributions I: 68, 165; Christensen, Contributions II: 58, 115 f., 160; Abrahamian 1936: 120; Lambton 


340 *sauc2 


1938: 42a, 78a; Andreev — PeSéereva: 323b f., 324b; MacKenzie 1966: 108, 107; EVS: 72b; WIM I: 72; 
Abaev, Slovar’ II: 380; WIM II/1: 82; DKS: 426b f.; Abaev, Slovar’ III: 165 ff.; Cabolov 1997: 72; 
Werba 1997: 243 f.; Lecoq 2002: 122, 125, 127 (passim); Shahbakhsh: s.v. söc'-; Korn 2005: 87, 382, 
384 (passim) 


*sau ‘to call’ 

Y Av. saocaiia(-ca) ‘mockery, [BMP] ’psws’ (Vyt 37, Vyt 59, H 2.13) 

*KHOTANESE: LKh. such- ‘to call, name’ = SGS: 133 

*NEIR: Sh. stig (f.), Rosh. sug (f.), Bart. sug (f.), Sariq. sewg, M. sugo, Yi. süyiko 
‘tale’ 

*MISC: Par. suy ‘word, affair’ 

*SANSKRIT: Süka- ‘parrot? (RV+)  EWAia П: 644 

© On the Iranian expression for ‘to swear, take an oath’, as in Sogd. swk’nt xwr-, 
MMP swgnd xwrdn, NP saugand xurdan, Kurd. sont xarin, etc., see Schwartz 1989: 
293 ff. 

«PIE *Keuk- ‘to call, cry’? = LIV: 332 | Pok.: 536 

*IE COGNATES: Lith. Saükti, Latv. saukt ‘to call’, Toch. B sausäm ‘calls’ 

*REFERENCES: IIFL I: 287a; IIFL II: 246a; EVS: 72b; DKS: 426b. 


*sauH! ‘to rub, wear, whet’ 

*MIDDLE PERSIAN: BMP s'd- /say-/ ‘to rub, wear, tire, tear’ || (+ *ham-) MMP hswd 
(ppp.) ‘whetted’ (Henning 1947: 45) = DMMPP: 186a 

Inf.: BMP swtn /südan/
```


## [2026-09-06T20:42:20.935Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"to chew\" CHEUNG.txt | head -20\necho \"=== WLD leaf 349 ===\"; python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(t[349][:3000])\"",
 "description": "Cheung chew + WLD page"
}
```


### [2026-09-06T20:42:22.799Z] TOOL RESULT

```
557:second millennium BCE (p. 306). Iranian verbs, such as *baru” ‘to chew, swallow’ 
2014:*Баги? (*barHu ?) ‘to chew, swallow’ 
2016:*AVESTAN: YAv. as.baouruua- '(place) where there is a lot to chew he to eat]’ (Yt 
2032:*SANSKRIT: bharv ‘to chew, devour, eat’ (RV) = EWAia II: 252 
3697:0 On *&iaH’/eiH < (?) PIE *Ki-, cf. *jiauH ‘to chew’ < PIE *gieuH-, see Rasmussen 
4759:*NWIR: ? Bal. dajit/daj- ‘to bite, sting’. 0 With -j- from j30-/jä- ‘to chew’, s. *jiauH ? 
7955:*NWIR: Gz. Zara/Zar-, Tr. Zarta/Zar- ‘to chew’, NP Zard ‘gluttony’ (LW) || (+ *aua-) ? 
7956:Bal. ugarit/ugar- ‘to chew the cud, swallow, devour, devastate, misspend’. © The 
7959:tion with Si. ugaranu ‘to chew the cud’ seems quite likely, as observed by Shah- 
13529:compares the Chor. forms to Skt. bhas ‘to chew’, is less likely. = Samadi: 228 
15160:*fiauH ‘to chew’ 
15162:*MIDDLE PERSIAN: MMP jw- ‘to chew’, BMP ywd- /joy-/ ‘to chew; devour (daevic)’ 
15166:*PARTHIAN: J ’w- ‘to chew (?)” = DMMPP: 197b 
15178:Jawin/jaw-, Zaz. jawitiS//awen-, (LW) Siv. gav-/Zavi, Tal. jüye ‘to chew’, Abz. 
15181:*NEIR: Pash. Zowul, Zoyol/Zoy- ‘to chew’, (LW ?) Yghn. Zav-/Zafta ‘to eat (liquid 
15184:masticate, munch, to fight together [of dogs, etc.]’, ? Ishk. Saw-/Sawod ‘to chew’ (S- 
15185:< ?), ? Yi. Zaf-/Zaft- ‘to chew, masticate; to light a fire’ (why -f ?) 
15187:*MISC: Orm. zay-ék ‘to chew, mastigate’ = zay-/zayók 
15194:«PIE *gieuH- ‘to chew, bite” => LIV: 168 | Pok.: 400 
15199:OHG kewa, OE céowan, Engl. to chew, Lith. (f. pl.) Ziáunos ‘jaws’, etc. 
=== WLD leaf 349 ===
                                         qad   kadh-                             341

Verhaltnisse nichts aus,     s.   Yf. LEWb. 2 u. calamitas   gegen III 4 68 f., Falk-
Torp u. hacl\ sie begriinden aucb nicht Zuteilung zu qad- „schadigen“).
   Z. B. Fick I 4 32, 42, 420 (mit fernzuhaltendem), II 4 68, III 4 68 f., Zu-
pitza Gutt. 184 m. Lit.


qad- „schadigen, berauben, verfolgen".
  Ai. Jcadana- n. „Vernichtung“, cakada kadanam „habe eine Yernichtung
angerichtet“;
  gr. hom. xsxadcov „beraubend“, Fut. xexad/joei „wird berauben“, xexadfjoai            •




flMymi, xaxuxjai, ozeQrjoai Hes., in medial-pass. Bed. bom. xe xadovzo „sie
                                     -
wichen“, ixexijdei (Konjektur) v7iex£%coqy)x£i Hes., otTCOxadim ao&sveco Hes.;
                                                                      '



  vielleicht xrjdm, dor. xadco „verletze, schadige“ (wenn nicht = xijdco „be-

triibe",zu had- „seelische Yerstimmung", von welchem die obige gr. Sippe
trotz Bechtel Lex. 190 aber jedenfalls zu trennen ist, Bersu Gutt. 169 f.,
s. auch v. Planta I 327).

   Femzubleiben hat lat. cado (Fick I 3 56, I 4 43; siehe Yf. LEWb. 2 s. v.,
und had- „fallen“); desgleichen cedo (siehe u. *sed- „sitzen“); ebenso
auch lat. calamitas „Schaden“ (urspriinglieh landwirtschaftlich „Hagelschlag,
Kornbrand, Mifiwachs", dann allgemein „Unheil, Yerderben“), denn fiir
„sabin.“ l — d (Conway IF. 2, 166) bietet die nach Marius Victorinus Gr. L.
VI 8, 15 von Pompeius gebrauchte Form cadamitas keine Gewahr, da als
Yolksetymologie nach cado verstandlich (s. Yf. LEWb. 2 s. v.), und gegen
sekundares l aus d spricht das sicher nicht dialektische incolmnis aus *en-
calamis (Thurneysen Thes.), das bereits zur Zeit der urlat. Anfangbetonung
vorhandenes l voraussetzt; daher zu Wz. qol-, qola- ,,schlagen, eludes (Fick
I 4 387, Vf. aaO. als Alternative, Reichelt KZ. 46, 330 f.). Das bei Ableitung
aus altem *cadamitas *en-cadumis formell in Rechnung gesetzte xdda,uog
                         ,
                                                                                            •




rvrpXog. ZaXafxhioi Hes. (Ehrlich KZ. 40, 380, Thurneysen Thes.) begegnet
Zweifeln (s. Schmidt zur Stelle und Herwenden Lex. gr. suppl. s. v.).

qhad- „beiflen“.
                                                                  £
      Ai. khddati „zerbeiBt, kaut, ibt“,       khddan m. „Zahn‘ , npers. xayidan
„essen, kauen“ (Hiibschmann ZDMG. 38, 423, Horn Np. Et. 104, Uhlen-
beck Ai. Wb. 75), arm. xacanem „beiBe, pungo“ (Bugge KZ. 32, 46; Pedersen
KZ. 38, 206; 39, 424, wonach -c- aus d -f- s); unsicherer norw. mdartl. hatra
„jucken, die Haut reizen, stechen (von Miicken und Fliegen)“, Bugge BB. 3, 1 02 f.
  G. Meyer Alb. Wb. 144 (Alb. St. Ill 59 nur mehr zw.) vergleicht mit
ai. khud- unter Annahme einer Gdf. skad-, der aber der vorzuziehende
Yergleich mit arm. xacanem im Wege ist (hochstens [sjqhad- bliebe gang-
bar) alb. ha „esse“, Passiv hahem; nicht uberzeugend stellt Brugmann
```


## [2026-09-06T20:42:39.696Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== CHEUNG xayidan ==\"; grep -n \"xayidan\\|xāyidan\\|xāy\\b\\|\\*xād\" CHEUNG.txt | head\necho \"== IEC keuk/swan ==\"; grep -n -i \"keuk\\|kuknos\\|kuk-no\" IEC.txt SYN.txt | head\necho \"== MON خاج ==\"; grep -n \"خاج\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head",
 "description": "More greps: Cheung, Mann/Buck, Mo'in"
}
```


### [2026-09-06T20:42:39.789Z] TOOL RESULT

```
== CHEUNG xayidan ==
41647:xayidan/xay-, 445 
== IEC keuk/swan ==
IEC.txt:7101:keto, ið — keukos, à
IEC.txt:7110:keugā, iə ‘top. peak, head'. Cf. keukolos, keukos (1) Av. cf. kaožda ‘corner; tip, spike’; Slovene cf. čužka “topknot'; Li. kiaugē ‘rick, stack’; Latv. cauga ‘head; pot; blockhead’
IEC.txt:7112:keukolos, à ‘topknot, tuft, crest. Cf. keukos (1) and keugà Oss. cokora ‘tuft, tassel’; Alb. cf. cukél ‘lad’; cuk&l-tar ‘tufted lark’; Rum. substr. ciucur, ciucure ‘tuft, tassel’; ciucurá, adv. ‘tufted’; Blg. čùkla ‘peak’; éCukàr, čukàra, id.; Latv. cf. Cukurs, id.
IEC.txt:7113:keukó ‘curl up, cower; curl; lurking, hud- dled’. Cf. WP I, 372 Skt. cf. čokam (name of a root); čočam *cinna- mon-bark’; cf. kočāmi, o-gde (2) ‘bend, curve’; Alb. çuk, v. ‘lurk’; cyc, adj. ‘huddled, crouch- ing’; MIr. & Ir. cuach ‘lock, curl’; cuachaim ‘curl, roll up, cuddle’; OHG. cf. hiuhma (crowd?, lit. "buddlet Srb. Cučati, Slovak čučať, Cz. & Slovene Cuceti, Blg. čuča ‘squat, crouch’; Blg. cf. tücka “pile of earth’; R cf. čùčelo ‘stuffed animal, scarecrow’, Li. kiáu- klas ‘snail shell’; Latv. kaukis (‘toad; arctic puffiw’. Semantics of E lurk, v. & G Lurch “toad'). Cf. also Ir. cuachán ‘bundle’
IEC.txt:7114:keukos, à (1) “top, tip, crest, topknot'. Cf. keukolos, keugà, teuqu- Alb. cuk ‘crown of head’; cuké ‘top, tip, penis, beak, hillock’: Rum. substr. ciuc ‘peak’; Ble. čuka, id.; cf. Blg. čučul *topknot'; čučurka “ici- cle’; čùkla ‘peak, summit’; Oss. cokora ‘tuft, tassel'; Latv. cf. čukurs ‘peak, gable’; Rum. subst. also ciucă ‘target; bullseye’
IEC.txt:7116:keukos (2), see keukó
IEC.txt:7117:keuks- (1) ‘crease, wrinkle’ Ir. cuach (2) ‘plait, fold; W cuch, pl. -iau ‘frown’; Ukr. cf. Cuxrij ‘kink’
IEC.txt:7118:keuks- (2) ‘cunnus (variant: keuKs-) Per. cüz (phonol. of rüz light"); Big. cf. čuška, id.
IEC.txt:7119:keuks- (3) ‘howl, screech’ | Cz. (ambig.) čišet ‘howl, of wind”; Li. kiauksiu, kiaukSiu, eti ‘howl, screech’; Latv. Caukstu, -stét, inchoat. ‘chatter’ beside kaukis “reed- warbler’. (The isophone in Slovak čušat "be silent is a riming parallel to type teuks-, q. v. Skt. éoksah, Cauksah “clean, pure? is without parallel)
IEC.txt:7127:keukos — kéuos, à, io
== MON خاج ==
incoming/MON/MON_2vol_Adena_v2_djvu.txt:13697:است. چهارم - ناحیه خاجی که شامل ۵ مهره 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:13699:مهره است. (مهره‌های نواحی خاجی و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15859:و تا مقابل سومین مهرة خاجی می‌رسد و پس 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26358:خاجی کمری و پوست بدن در این قسمت 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:34203:خح؛ خاخاجه و و تلکاء 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:36328:حدفاصل بین دو سطح داخلی و خاجی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40241:استخوان خاصره و خاجی تشکیل می‌شود و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40243:خاجی است نیز جزو استخوان‌های تشکیل 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:62315:خاجی مفصل می‌شود و به علاوه دو 
MON_part2.txt:13697:است. چهارم - ناحیه خاجی که شامل ۵ مهره
```


## [2026-09-06T20:42:48.488Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xāy-\\|xay-/\\|xāyid\\|xayid\" CHEUNG.txt | head -20\necho \"---\"; grep -n \"^\\*x[aā]d\\|\\*xād\\|xad ‘\" CHEUNG.txt | head -20",
 "description": "Find Cheung xāyidan root"
}
```


### [2026-09-06T20:42:48.555Z] TOOL RESULT

```
9647:Sh. (Baj.) wixi(y)-/wixid, Rosh. wixay-/wixid, Bart. wixi-/wixid, Yzgh. wix"ay-/ 
10057:ua-suff.), Sh. xay-/xüst, (Baj.) xi-/xust, Khf. xay-/xost, Rosh. xöy-/xost, Bart. xiy-/ 
29343:wixay-/wixuxt, Bart. wiXaw-/wixuxt, Orosh. wuXod ‘to comb’, Sh. wixüy], Rosh. 
41647:xayidan/xay-, 445 
48184:xay-/xüst, 143 
48682:xay-/xost, 143 
48910:wixay-/wixid, 136, 355 
---
28355:*xad 439 
28377:*xad ‘to beat, strike, inflict a wound, hurt’ 
28769:*xad ‘to injure’. The reconstruction of the final consonant(s) is uncertain: *xad or 
56911:*xad, *xšan, *zarH! 
56920:*xad
```


## [2026-09-06T20:42:55.459Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"445\" CHEUNG.txt | sed -n '1,40p'",
 "description": "Find Cheung page 445"
}
```


### [2026-09-06T20:42:55.510Z] TOOL RESULT

```
4200:WIM III: 310; Werba 1997: 299; Cabolov 2001: 291; ESIJa II: 445 f. 
8879:Werba 1997: 343; Steblin-Kamenskij 1999: 445; Jamison, Fs Rix: 237 ff. 
9857:along’. © LIV: 445 | Pok.: 743 
12656:*REFERENCES: EVS: 66b, 53b; DKS: 358, 362b; Gharib: 342b; Werba 1997: 445 f.; Häusler 2000: 143 ff. 
15611:*SANSKRIT: khan’ ‘to dig’ (RV+) > EWAia I: 445 
17965:«PIE? c LIV: 445 | Pok.: 743, 753 
18091:«PIE *mieuH;- ‘to set into motion’ = LIV: 445 f. | Pok.: 743 
18200:«PIE *mleuH- ‘to speak’ = LIV: 445 f. | Pok.: — 
19398:*AVESTAN: YAv. pər- ‘to fight, struggle’. Ф Strunk 1986: 445 ff. compares the Av. 
19680:*REFERENCES: Strunk 1986: 445 ff.; Kiimmel 2000: 648 
28727:*хӣ7 445 
30428:«PIE *g”ers- ‘to be delighted’ > LIV: 178, 198 | Pok.: 445 f. 
32942:*k"eHod-, 445 
32956:#k H;eg-, 445 
35956:"X"z-, 445 
36482:X'z-, 445 
36726:khas-, 445 
37191:parchas-, 445 
38088:”y’ns (B), 445 
38133:*Ux's (S), 445 
38386:"xs (C), 445 
38872:pry 'yz- (B), 445 
39295:txyz (M), 441, 445 
41644:xazidan, 445 
41647:xayidan/xay-, 445 
41963:k'a6i0-/k'a6-, 445 
42283:Каут/Кау(е)-, 445 
42532:xizan (Sul.), 445 
42731:xizian (Sina), 445 
43026:xızäy/-xız-, 445 
47395:cxedol, 445 
51558:khad, 445 
52458:xacanel, 445
```


## [2026-09-06T20:43:00.273Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28700,28775p' CHEUNG.txt",
 "description": "Print Cheung p.445 root entry"
}
```


### [2026-09-06T20:43:00.320Z] TOOL RESULT

```
green’, Yi. xalaryo ‘wet clay, mud, bog’ 

*SANSKRIT: Кага ‘to defecate’ (in AVP, cf. Griffiths 2004) 2 EWAia: — 

© The root may be of IE origin, but obviously it may have undergone tabooistic 
change, compare for instance *sard. 

«PIE ? *ker-d-/*kre-d- (or *Kerd-/*Kred- ?) ‘to defecate’. © Liable to tabooistic 
change and semantic contamination. = LIV: 328 | Pok.: 573 

*IE COGNATES: Lat. -cerda ‘excrements (of mice, pig, cow and sheep)’, (with mobile 


s-, without d-enlarg.) ON skarn, OE scearn, OFris. skern ‘dung’ 
*REFERENCES: EVP: 97; IIFL II: 266b; Andreev — PeSéereva: 359a; EVS: 78b, 79a; DKS: 417a; 
Steblin-Kamenskij 1999: 412; NEVP: 96 


*xaz ? ‘to creep, crawl’ 

*MIDDLE PERSIAN: MMP xyz- ‘to creep? = DMMPP: 371b 
Partic.: pres. MMP "xyzyndg, MMP xyz’n 

*PARTHIAN: xz- ‘to creep’ => Ghilain: — | DMMPP: 371b 
Pres.: IND. 3sg. xzyd {hapax} 


*хӣ7 445 


*SOGDIAN: Q There is no firm evidence for a verb xyz- ‘to crawl’ in Sogd., "пог need 
the compound MSogd. z’yxyzyy [attested in BBB: 61 ad 512] imply its existence", 
Sims-Williams 1983: 47. In other words, z’yxyzyy can be translated not only as 
‘crawling on earth’, but also as ‘setting on earth’ (*xaiz), also MSogd. txyz ‘setting 
(of sun and moon)’. 

*CHORESMIAN: m/xsy- ° to creep’ = Samadi: 242 

*NWIR: NP xazidan ‘to crawl, creep’, Kurd. (Sul.) xizan, (Sina) xizian, Awrom. 
xizáy/-xiz- ‘to slip, slide’ 

*NEIR: ? Pash. cxedol ‘to creep’ 

9 The IE origin of this root cannot be ascertained: exclusively Iranian ? The root 
may have been influenced by the (near-)synonym *xaiz ‘to rise’. 


*PIE— > LIV: — | Pok.: 
*REFERENCES: EVP: 19; Gershevitch 1952a: 488 ff.; MacKenzie 1966: 113 


*xäd ‘to devour, eat, gorge’ 

*PARTHIAN: X’z- ‘to devour’ = Ghilain: 39 | DMMPP: 363b 

Pres.: IND. 3pl. x’zynd; Partic.: pres. x’zyndg ‘devouring’, x’zyndg’n (pl.) ‘devouring (monsters)’, perf. 
pass. II x’z’d 

*KHOTANESE: khäs- (denomin. ?) ‘to eat, drink’ || (+ *pari-) OKh. parchäs- ‘to make 
consume’ — SGS: 26, 75 

*NWIR: NP xäyidan/xäy- ‘to chew, gnaw, eat’, Bal. k'aói0-/K'aó- ‘to chew’, Kurd. 
(Kurm.) Kayin/Kay(e)- ‘to chew the cud, ruminate’ (< PKurd. *xada-) 

*SANSKRIT: khäd ‘to chew, to bite, to eat’ (R V+). 0 I find the separation of Skt. khad, 
which has been assigned to the semantically unlikely root *k“”eHbd- ‘to squeeze 
out’ in LIV: 359, from the Ir. forms incomprehensible. = EWAia I: 451 

9 In view of the differences in meaning, *xad (or *xadz ?) should be separated from 
*xad ‘to injure’. The reconstruction of the final consonant(s) is uncertain: *xad or 
with ingressive *s-suffix *xad-z, cf. *urad vs *uraz (Kümmel 2000: 623) ? An IE 
provenance for this Ur. root is uncertain: the IE preform *k'"H;eé- (cf. Arm. 
xacanel 'to bite") reconstructed by Klingenschmitt 1982: 210 and Kümmel, LIV: 


360 has little to recommend.
```


## [2026-09-06T20:43:12.567Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28377,28420p' CHEUNG.txt",
 "description": "Print Cheung *xad injure entry"
}
```


### [2026-09-06T20:43:12.614Z] TOOL RESULT

```
*xad ‘to beat, strike, inflict a wound, hurt’ 
*AVESTAN: (+ *ui-) ? YAv. vixaö- ‘to beat (the earth) apart’ (not ‘auseinander 


quetschen’ ?, AIW: 531) = Liste: 16 
Pres. them.: INJ. 3sg. YAv. vixadat (V 2.32), IMPV. 2sg. YAv. vixada (V 2.31) 


*MIDDLE PERSIAN: MMP xst (ppp.) ‘wounded’ > DMMPP: 365a 

Partic.: perf. pass. MMP xst 

*PARTHIAN: xd- ‘to injure’, xdm ‘wound?’ || (+ *ui-) w(y)xs- (inch.) ‘to be wounded’, 
wxs’’g, wyxs’g ‘thrust, stab’ = Ghilain: 81 | DMMPP: 363b 

Pres.: IND. 3pl. "xdynd (Sundermann 1981: 175b), SUBJ. 25р. xd’h; Partic.: pres. xdyndg || (+ *ui-) 
Inch.: pres. IND. 3pl. wyxsynd, wxsynd 


*KHOTANESE: khad- ‘to wound, hurt’ || (+ *aua-) OKh. vahas- ‘to smite’ || (+ *pati-) 
páha- (pihei-) ‘to strike’ || (+ *ui-) gguhad- ‘to harm, wound’ > SGS:25,121, 83, 30 
*SOGDIAN: CSogd. yd- (f.) ‘wound, wounding, beating’, BSogd. yök’yn ‘wounded’ || 
(+ *ham-) BSogd. "nyó- ‘to prick, pierce’ 

(+ *ham-) Pres.: IND. 3sg. BSogd. ’nyött, OPT. 35р. BSogd. ’nyö’y; Partic.: perf. pass. BSogd. "ny'stk, 
MSogd. ’nxst- ‘stuck, having pierced’ 

*CHORESMIAN: xô- ‘to stab, hurt" = Samadi: 234 

*NWIR: NP xastan (obs.) ‘to wound’, xastah '[obs.] wounded, sad; tired, bored’, 
borrowed into: Kurd. xistin/xe- ‘to strike, hit’, Gz., Nn., Varz. xasse, Qohr. xasta 
‘tired’ 

*NEIR: ? Wa. kas-/kast (old inch. ?) ‘to thresh’, Sh. (Baj.) $05 (m.), Rosh. sud, Sariq. 
Sid, Sud, Yzgh. xoónag ‘thorn, spine, bramble’ (*xad-na-(ka-)) || (+ *apa-) ? Oss. I. 
efxalyn/efxeld, D. efxalun/efxeld ‘to be damaged [of skin, Боду]? (with sec. -/-) 
*SANSKRIT: ? kadana- ‘destruction, killing’ (Ep. +) = EW Aia Ш: 53 

© This root should be separated from Skt. khad ‘to eat, chew’, which rather corres- 
ponds to an Ir. root *xad (q.v.). On the other hand, we may consider the late Skt. 
formation kadana-, which is obscure though and the initial velar would need to be 
explained as well. Ir. *xad has no certain IE cognate forms, the comparison to Gr.
```


## [2026-09-06T20:43:38.101Z] TOOL CALL #56: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py",
 "description": "Read fetch_source.py"
}
```


### [2026-09-06T20:43:38.143Z] TOOL RESULT

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
    note = ""
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
        print(__doc__); return 2
    url = args[0]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    # IRI -> URI: percent-encode non-ASCII path/query characters so urllib accepts them
    parts = urllib.parse.urlsplit(url)
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-06T20:43:45.481Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AE%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%AE\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%DA%AF%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 265 verification (Keuk 1 / Khac / Khad)\"; done",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-06T20:43:47.415Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/05f376e66f1abbbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3e99c33ea33af17.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5f766234e4e6cca7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1a9e26b236457153.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccbdf43b60a5d316.txt
```


## [2026-09-06T20:43:48.993Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CE%BA%CE%BD%CE%BF%CF%82\" \\\n \"https://www.etymonline.com/word/cygnet\" \\\n \"https://en.wiktionary.org/wiki/%D5%AD%D5%A1%D5%B9\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 265 verification (Keuk 1 / Khac / Khad)\"; done",
 "description": "Archive more sources"
}
```


### [2026-09-06T20:43:52.307Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/69a4d3c146db7b4b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9bd7a6cbf80e9a0f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8017f5e7b99cc686.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b6e8895a251a872d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ae529aabf1bedd3c.txt
```


## [2026-09-06T20:44:00.905Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 05f376e66f1abbbf f3e99c33ea33af17 5f766234e4e6cca7 1a9e26b236457153 ccbdf43b60a5d316 69a4d3c146db7b4b 9bd7a6cbf80e9a0f 8017f5e7b99cc686 b6e8895a251a872d ae529aabf1bedd3c; do echo \"--- $f ---\"; head -3 $f.txt; done",
 "description": "Verify fetched file identities"
}
```


### [2026-09-06T20:44:03.374Z] TOOL RESULT

```
--- 05f376e66f1abbbf ---
URL: https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AE%D8%AA%D9%86
FETCHED: 2026-09-06T16:37:04Z
STATUS: 200
--- f3e99c33ea33af17 ---
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%AE
FETCHED: 2026-09-06T16:37:02Z
STATUS: 200
--- 5f766234e4e6cca7 ---
URL: https://en.wiktionary.org/wiki/%D8%B3%D9%88%DA%AF%D9%86%D8%AF
FETCHED: 2026-09-06T16:37:01Z
STATUS: 200
--- 1a9e26b236457153 ---
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D8%AC
FETCHED: 2026-09-06T16:37:04Z
STATUS: 200
--- ccbdf43b60a5d316 ---
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-06T16:37:06Z
STATUS: 200
--- 69a4d3c146db7b4b ---
URL: https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CE%BA%CE%BD%CE%BF%CF%82
FETCHED: 2026-09-06T16:37:05Z
STATUS: 200
--- 9bd7a6cbf80e9a0f ---
URL: https://www.etymonline.com/word/cygnet
FETCHED: 2026-09-06T16:37:05Z
STATUS: 200
--- 8017f5e7b99cc686 ---
URL: https://en.wiktionary.org/wiki/%D5%AD%D5%A1%D5%B9
FETCHED: 2026-09-06T16:37:04Z
STATUS: 200
--- b6e8895a251a872d ---
URL: https://en.wiktionary.org/wiki/%D8%B3%D9%88%DA%AF
FETCHED: 2026-09-06T20:43:51Z
STATUS: 200
--- ae529aabf1bedd3c ---
URL: https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3
FETCHED: 2026-09-06T20:43:52Z
STATUS: 200
```


## [2026-09-06T20:44:11.226Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 05f376e66f1abbbf f3e99c33ea33af17 5f766234e4e6cca7; do echo \"=========== $f ===========\"; grep -n -A12 -i \"Etymology\" $f.txt | head -60; done",
 "description": "Read Wiktionary etymologies (suxtan, sorx, sogand)"
}
```


### [2026-09-06T20:44:13.081Z] TOOL RESULT

```
=========== 05f376e66f1abbbf ===========
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- Derived terms 
--
148: Etymology
149- [ edit ] 
150-
151- From Middle Persian [script needed] ( swhtn' /⁠sōxtan⁠/ ) ; ultimately from Proto-Indo-European *ḱewk- ( “ white ” ) . Cognates with Northern Kurdish sotin , Gilaki سوتن ( sutən ) , Talysh سوته ( sute ) , Baluchi سوچگ ( sóčag ) , Mazanderani بسوتن ( basuten ) , Central Kurdish سووتان ( sûtan ) and Pashto سوختېدل .
152-
153- Also related to سرخ ( sorx , “ red ” ) , and سوگ ( sug , “ sadness, mourning ” ) .
154-
155- Pronunciation
156- [ edit ] 
157-
158- ( Classical Persian ) IPA ( key ) : /soːx.ˈtan/ 
159-
160- ( Dari, formal ) IPA ( key ) : [soːx.t̪ʰán] 
=========== f3e99c33ea33af17 ===========
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
69-
70- 1.3.1 
71- Inflection 
72-
73- 1.3.2 
74- Derived terms 
--
96: Etymology 
97-
98- 3.2 
99- Pronunciation 
100-
101- 3.3 
102- Adjective 
103-
104- 3.3.1 
105- Synonyms 
106-
107- 3.3.2 
108- Derived terms 
--
194: Etymology
195- [ edit ] 
196-
197- From an earlier metathesis of سهر ( suhr ) , Southern Luri سوهر ( sohr ) (cf. سهراب ( suhrāb , “ literally a person who has red face ” ) ), from Middle Persian [Book Pahlavi needed] ( swhr /⁠suhr⁠/ , “ red ” ) , from Manichaean Middle Persian 𐫘𐫇𐫍𐫡 ( swhr /⁠suhr⁠/ ) , from Old Persian *θuxrah ( “ red, bright ” ) , from Proto-Iranian *cuxráh from Proto-Indo-Iranian *ćukrás . Compare Sanskrit शुक्र ( śukra , “ bright, resplendent ” ) , Parthian 𐫘𐫇𐫟𐫡 ( swxr /⁠suxr⁠/ , “ red ” ) , Northern Kurdish sor ( “ red ” ) , Ossetian сырх ( syrx , “ red ” ) and Avestan 𐬯𐬎𐬑𐬭𐬀 ( suxra ) .
198-
199- Pronunciation
200- [ edit ] 
201-
202- ( Classical Persian ) IPA ( key ) : /ˈsurx/ 
203-
204- ( Dari, formal ) IPA ( key ) : [sʊɾx] 
205-
206- ( Dari, formal ) IPA ( key ) : [sʊɾx] 
--
428: Etymology
429- [ edit ] 
430-
431- Borrowed from Classical Persian سرخ ( surx ) . Doublet of شکر ( śukra , “ bright ” ) .
432-
433- Pronunciation
434- [ edit ] 
435-
436- ( Standard Urdu ) IPA ( key ) : /sʊɾx/ 
437-
438- Audio : ( file ) 
439-
440- Adjective
=========== 5f766234e4e6cca7 ===========
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Inflection 
72-
73- 1.3.2 
74- Derived terms 
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
95-
96- 2.3.1 
97- Synonyms 
98-
99- 2.3.2 
100- References 
--
173: Etymology
174- [ edit ] 
175-
176- From Middle Persian swknd ( sōgand , “ oath ” ) , [ 1 ] from Avestan [Term?] ( /⁠saokanta⁠/ , “ sulphur ” ) , [ 2 ] from Proto-Indo-European *ḱewk- ( “ white ” ) . Related to سوختن ( sōxtan , “ to burn ” ) , and سوگ ( sōg , “ sadness, mourning ” ) .
177-
178- Pronunciation
179- [ edit ] 
180-
181- ( Classical Persian ) IPA ( key ) : /saw.ˈɡand/ 
182-
183- ( Dari, formal ) IPA ( key ) : [säw.ɡán̪d̪] 
184-
185- ( Dari, formal ) IPA ( key ) : [säw.ɡán̪d̪] 
--
335: Etymology
336- [ edit ] 
337-
338- Borrowed from Classical Persian سَوگَنْد ( sawgand ) .
339-
340- Pronunciation
341- [ edit ] 
342-
343- ( Standard Urdu ) IPA ( key ) : /sɔː.ɡənd̪/ 
344-
345- Noun
346- [ edit ] 
347-
--
388: Urdu entries with etymology texts 
389- Pages using etymon with no ID 
390-
391- This page was last edited on 29 August 2026, at 02:52.
```


## [2026-09-06T20:44:23.954Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 1a9e26b236457153 ccbdf43b60a5d316 8017f5e7b99cc686; do echo \"=========== $f ===========\"; grep -n -A10 \"^ Etymology$\" $f.txt | head -50; done",
 "description": "Read khaj, khayidan, xach etymologies"
}
```


### [2026-09-06T20:44:25.476Z] TOOL RESULT

```
=========== 1a9e26b236457153 ===========
=========== ccbdf43b60a5d316 ===========
138: Etymology
139- [ edit ] 
140-
141- Per Derksen, from Proto-Indo-Iranian *kʰād- , from Proto-Indo-European *k(ʷ)end- or *k(ʷ)enHd(ʰ)- .
142-
143- Compare Sanskrit खाद् ( khād ) and खादति ( khādati , “ to chew, to bite ” ) , Ancient Greek κνώδων ( knṓdōn , “ sword, spear spikes ” ) and Khotanese khays- ( “ to drink ” ) .
144-
145- Pronunciation
146- [ edit ] 
147-
148- ( Classical Persian ) IPA ( key ) : /xaː.jiː.ˈdan/ 
=========== 8017f5e7b99cc686 ===========
184: Etymology
185- [ edit ] 
186-
187- Inherited from Old Armenian խաչ ( xačʻ ) .
188-
189- Pronunciation
190- [ edit ] 
191-
192- ( Eastern Armenian ) IPA ( key ) : /χɑt͡ʃʰ/ [χɑt͡ʃʰ] 
193-
194- ( Western Armenian ) IPA ( key ) : /χɑt͡ʃ/ [χɑt͡ʃʰ] 
--
365: Etymology
366- [ edit ] 
367-
368- The origin is uncertain.
369-
370- Lidén connects with Persian خاده ( xâda , “ pole; stake; gibbet ” ) , Lithuanian kótas ( “ broomstick ” ) , Latvian kāts ( “ handle, shaft ” ) , and derives all from Proto-Indo-European . [ 1 ] [ 2 ] This is accepted by Ačaṙean, who adduces also Old Armenian խոչ ( xočʻ , “ a piece of wood, stone protruding from ground upon which one may stumble, an obstacle ” ) and խէչ ( xēčʻ ) , խեչ ( xečʻ , “ prop, stay, on which plants are supported ” ) as ablaut grades. [ 3 ] If this is correct, the initial meaning of խաչ ( xačʻ ) was "stake, stick, upright pile". For the sense development compare Georgian ჯვარი ( ǯvari ) , Ancient Greek σταυρός ( staurós , “ upright stake or pile; crucifix ” ) , Gothic 𐌲𐌰𐌻𐌲𐌰 ( galga , “ stake; cross; gallows ” ) , Manichaean Parthian 𐫅𐫀𐫡 ( dʾr /⁠dār⁠/ , “ tree, gallows, cross; wood ” ) .
371-
372- Olsen rejects the above etymology on phonetic grounds. [ 4 ] 
373-
374- Note also dialectal Georgian ხაჭა ( xač̣a , “ long, thick stick ” ) which is probably somehow related.
375-
```


## [2026-09-06T20:44:26.795Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 69a4d3c146db7b4b 9bd7a6cbf80e9a0f b6e8895a251a872d ae529aabf1bedd3c; do echo \"=========== $f ===========\"; grep -n -A10 -i \"^ Etymology\" $f.txt | head -40; done",
 "description": "Read kuknos, cygnet, sug, afsus"
}
```


### [2026-09-06T20:44:28.767Z] TOOL RESULT

```
=========== 69a4d3c146db7b4b ===========
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Inflection 
72-
--
88: Etymology 
89-
90- 2.2 
91- Noun 
92-
93- 2.2.1 
94- Declension 
95-
96- 2.2.2 
97- Derived terms 
98-
--
188: Etymology
189- [ edit ] 
190-
191- Perhaps from a Proto-Indo-European *ḱewk- ( “ white ” ) , with cognates including Sanskrit शोचति ( śócati , “ to shine, suffer ” ) and शुक्र ( śukrá , “ bright, white ” ) , [ 1 ] and possibly Old Norse Hǿnir ( “ god associated with swans and storks ” ) . Compare typologically Proto-Slavic *olbǫdь < Proto-Indo-European *h₂elbʰós , Tatar аккош ( aqqoş ) ( ак ( aq ) + кош ( qoş ) ). Could also be onomatopoeic from the sound of the swan's call (compare Russian кы-кы ( ky-ky , “ cry of a swan ” ) ).
192-
193- Pronunciation
194- [ edit ] 
195-
196- IPA ( key ) : /ký.knos/ → /ˈcy.knos/ → /ˈci.knos/ 
197-
198- ( 5 th BCE Attic ) IPA ( key ) : /ký.knos/ 
--
334: Etymology
335- [ edit ] 
336-
337- From Ancient Greek κύκνος ( kúknos ) .
=========== 9bd7a6cbf80e9a0f ===========
=========== b6e8895a251a872d ===========
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- 2.3.1 
91- Declension 
92-
--
168: Etymology
169- [ edit ] 
170-
171- Inherited from Middle Persian swk' ( sōg , “ burn, burning ” ) , from Old Persian *θauga(h) , from Proto-Iranian *cawkah , from Proto-Indo-Iranian *ćawkas (compare Sanskrit शोक ( śoka , “ burning; grief ” ) , whence Hindustani सोग ( sog ) / سوگ ( sog ) and Punjabi ਸੋਗ ( sog ) / سوگ ( sog ) ), ultimately from Proto-Indo-European *ḱewk- .
172-
173- Related to سوختن ( sōxtan , “ to burn ” ) , سرخ ( surx , “ red ” ) , and سوگند ( sawgand , “ oath ” ) ; and also to Old Armenian սուգ ( sug , “ grief ” ) , an Iranian borrowing.
174-
175- Pronunciation
176- [ edit ] 
177-
178- ( Classical Persian ) IPA ( key ) : /ˈsoːɡ/ 
--
242: Etymology
243- [ edit ] 
244-
245- Inherited from Sauraseni Prakrit 𑀲𑁄𑀕 ( soga ) , from Sanskrit शोक ( śoka ) . Also influenced by Classical Persian سوگ ( sōg ) . Doublet of شوک ( śok ) .
=========== ae529aabf1bedd3c ===========
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 2 
68- Persian 
69-
70- Toggle Persian subsection 
71-
72- 2.1 
73: Etymology 
74-
75- 2.2 
76- Pronunciation 
77-
78- 2.3 
79- Interjection 
80-
81- 2.4 
82- Noun 
83-
--
96: Etymology 
97-
98- 3.2 
99- Pronunciation 
100-
101- 3.3 
102- Noun 
103-
104- 3.4 
105- Interjection 
106-
--
116: Etymology 
117-
118- 4.2 
119- Pronunciation 
120-
```


## [2026-09-06T20:44:53.622Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== afsus persian ===\"; sed -n '150,230p' ae529aabf1bedd3c.txt\necho \"=== khaj persian ===\"; grep -n -i \"persian\" 1a9e26b236457153.txt | head -20",
 "description": "Read afsus and khaj pages"
}
```


### [2026-09-06T20:44:53.676Z] TOOL RESULT

```
=== afsus persian ===
 Noun 

 Toggle the table of contents 

 افسوس 

 14 languages 

 বাংলা 
 فارسی 
 Magyar 
 Bahasa Indonesia 
 日本語 
 ქართული 
 Kurdî 
 Кыргызча 
 Malagasy 
 پښتو 
 Português 
 Русский 
 سرائیکی 
 Türkçe 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Gawar-Bati
 [ edit ] 

 Etymology
 [ edit ] 

=== khaj persian ===
57: Persian 
59: Toggle Persian subsection 
152: Persian
158: ( Classical Persian ) IPA ( key ) : /ˈxaːd͡ʒ/ 
232: Steingass, Francis Joseph ( 1892 ), “ خاج ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 
237: ^ Hübschmann, Heinrich ( 1895 ), Persische Studien [ Persian Studies ] (in German), Strasbourg: K.J. Trübner, page 227 
241: ^ Horn, Paul ( 1898–1901 ), “Neupersische Schriftsprache [ New Persian written language ]”, in Wilhelm Geiger, Ernst Kuhn , editors, Grundriß der iranischen Philologie [ Outline of Iranian Philology ] (in German), volume I, part II, Strassburg: K. J. Trübner, page 8 
249: ^ Asatryan, Gaṙnik ( 1990 ), “Ardyokʻ ka ? n haykakan pʻoxaṙutʻyunner nor parskerenum [ Are There Armenian Borrowings in New Persian? ]”, in Patma-banasirakan handes [ Historical-Philological Journal ]‎ [3] (in Armenian), number 3, page 144 of 139–144 
255: Categories : Persian terms with IPA pronunciation 
256: Rhymes:Persian/aːd͡ʒ 
257: Rhymes:Persian/aːd͡ʒ/1 syllable 
258: Persian terms borrowed from Middle Armenian 
259: Persian terms derived from Middle Armenian 
260: Persian terms derived from Old Armenian 
261: Persian lemmas 
262: Persian nouns 
265: Persian dated terms
```


## [2026-09-06T20:44:55.096Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '1,60p' 9bd7a6cbf80e9a0f.txt; echo \"=== grep cygnet ===\"; grep -n -i \"swan\\|cycnus\\|kyknos\" 9bd7a6cbf80e9a0f.txt | head -20",
 "description": "Read etymonline cygnet"
}
```


### [2026-09-06T20:44:55.153Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/cygnet
FETCHED: 2026-09-06T16:37:05Z
STATUS: 200
TITLE: Cygnet - Etymology, Origin & Meaning

Cygnet - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of cygnet 

 cygnet (n.) 

 "a young swan," c. 1400, also signet before 17c., from Anglo-French cignet (mid-14c.), Anglo-Latin cygnettus , diminutives of Old French cigne , cisne "swan" (12c., Modern French cygne ), from Latin cygnus , from Greek kyknos , which has been the subject of "abundant discussion" (Beekes) and is perhaps from PIE *(s)keuk- "to be white" (compare Sanskrit socati "to lighten, glow," sukra- "light, clear, white"). Spanish, Portuguese cisne , Italian cecero are from Medieval Latin cecinus, cicinus , a corruption of the classical Latin word.
 also from c. 1400 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 swan 

 large, web-footed swimming bird, stately and graceful in the water, noted for its long neck and white down; Old English swan "swan," from Proto-Germanic *swanaz "singer" (source also of Old Saxon swan, Old Norse svanr, Danish svane, Swedish svan, Middle Dutch swane, Dutch zwaan, 

 quarantine 

 1660s, "period a ship suspected of carrying contagious disease is kept in isolation," from Italian quaranta giorni, literally "space of forty days," from quaranta "forty," from Latin quadraginta "forty" (related to quattuor "four," from PIE root *kwetwer- "four"). The name is fro

 reason 

 c. 1200, resoun, "the intellectual faculty that adopts actions to ends," also "statement in an argument, statement of explanation or justification," from Anglo-French resoun, Old French raison "course; matter; subject; language, speech; thought, opinion," from Latin rationem (nom

 Peter 

 masc. proper name, 12c., from Old English Petrus (genitive Pet(e)res, dative Pet(e)re), from Latin Petrus, from Greek Petros, literally "stone, rock" (see petrous), a translation of Syriac kefa "stone" (Latinized as Cephas), the nickname Jesus gave to apostle Simon Bar-Jona (Matt

 sophomore 

 1680s, "student in the second year of university study," literally "arguer," altered from sophumer (1650s), from sophume, an archaic variant form of sophism, ultimately from Greek sophistēs "a master of one's craft; a wise or prudent man, one clever in matters of daily life." The

 milk 

 "opaque white fluid secreted by mammary glands of female mammals, suited to the nourishment of their young," Middle English milk, from Old English meoluc (West Saxon), milc (Anglian), from Proto-Germanic *meluk- "milk" (source also of Old Norse mjolk, Old Frisian melok, Old Saxon

 avail 

 c. 1300, availen, "to help (someone), assist; benefit, be profitable to; be for the advantage of; have force or efficacy, serve for a purpose," apparently an Anglo-French compound of Old French a- "to" (see ad-) + vaill-, present stem of valoir "be worth," from Latin valere "be s

 commission 
=== grep cygnet ===
25: "a young swan," c. 1400, also signet before 17c., from Anglo-French cignet (mid-14c.), Anglo-Latin cygnettus , diminutives of Old French cigne , cisne "swan" (12c., Modern French cygne ), from Latin cygnus , from Greek kyknos , which has been the subject of "abundant discussion" (Beekes) and is perhaps from PIE *(s)keuk- "to be white" (compare Sanskrit socati "to lighten, glow," sukra- "light, clear, white"). Spanish, Portuguese cisne , Italian cecero are from Medieval Latin cecinus, cicinus , a corruption of the classical Latin word.
32: swan 
34: large, web-footed swimming bird, stately and graceful in the water, noted for its long neck and white down; Old English swan "swan," from Proto-Germanic *swanaz "singer" (source also of Old Saxon swan, Old Norse svanr, Danish svane, Swedish svan, Middle Dutch swane, Dutch zwaan,
```


## [2026-09-06T20:45:01.374Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '150,235p' 1a9e26b236457153.txt",
 "description": "Read Wiktionary خاج Persian section"
}
```


### [2026-09-06T20:45:01.419Z] TOOL RESULT

```
 See also: حاج , چاچ , and خاچ 

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈxaːd͡ʒ/ 

 ( Dari, formal ) IPA ( key ) : [xɑːd͡ʒ] 

 ( Dari, formal ) IPA ( key ) : [xɑːd͡ʒ] 
 ( Kabuli ) IPA ( key ) : [xɑːd͡ʒ] 

 ( Hazaragi ) IPA ( key ) : [xɔːd͡ʒ̥] 

 ( Iran, formal ) IPA ( key ) : [xɒːd͡ʒ̥] 

 ( Tajik, formal ) IPA ( key ) : [χɔd͡ʒ] 

 Rhymes: -aːd͡ʒ 

 Readings

 Classical reading ? 

 xāj

 Dari reading ? 

 xāj

 Iranian reading ? 

 xâj

 Tajik reading ? 

 xoj

 Etymology 1
 [ edit ] 

 Borrowed from Middle Armenian խաչ ( xačʻ , “ cross ” ) , from Old Armenian խաչ ( xačʻ , “ crucifix; cross ” ) . [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] 

 Noun
 [ edit ] 

 خاج • ( xâj ) 

 ( card games ) club (♣)

 ( Christianity , dated ) cross 

 Alternative forms
 [ edit ] 

 خاچ ( xâč ) 

 Derived terms
 [ edit ] 

 خاج‌شویان ( xâj-šuyân ) , خاچ‌شویان ( xâč-šuyân ) 

 خاج‌پرست ( xâj-parast , “ Christian ” ) 

 خاج‌پرستی ( xâj-parasti , “ Christianity ” ) 

 Etymology 2
 [ edit ] 

 Noun
 [ edit ] 

 خاج • ( xâj ) 

 the soft part of the ear 

 Further reading
 [ edit ] 

 Steingass, Francis Joseph ( 1892 ), “ خاج ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 

 References
 [ edit ]
```


## [2026-09-06T20:45:17.078Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== BRT aiwi.saoka ==\"; grep -n \"aiwi.saoka\\|aiwi\\.sao\\|afsos\" BRT.txt | head\necho \"== HRN afsos ==\"; grep -n \"afsös\\|afsös\\|afsos\\|afsüs\" HRN.txt | head\necho \"== HUB afsos ==\"; grep -n \"afsös\\|afsos\" HUB.txt | head\necho \"== SYN swan ==\"; grep -n -i \"kyknos\\|kuknos\\|swan\" SYN.txt | head",
 "description": "Grep for afsus and swan"
}
```


### [2026-09-06T20:45:17.157Z] TOOL RESULT

```
== BRT aiwi.saoka ==
== HRN afsos ==
1288:phlv. afsös 'Spott, Scherz'.
== HUB afsos ==
496:101. Np. afsos (afgh. LW. afsos 'sorrow, regret') wird auch
6128:surdan H. 100; afsos *Spott* — fisds H. 101; afscLndan *aus-
6470:afsos *Spott' H. 101 (?), paz. aw(a)sd8; afsandan ausstreuen'
== SYN swan ==
4786:. Grk. xiv, Dor. xév; Lat. anser (for hanser) ; (Ir. géis ‘swan’) ; ON gas, OF ie OHG gans, etc., general Gmc. ; Lith. ass, ChSl. *gqsi, (gust), ete., general
4787:Palto-Slavie (Slavic g fr. Gme.?); Skt Lansa- (also ‘swan’, etc.). :
5498:MHG zagel, swanz, sterz schwanz (schweif)
5515:MHG swanz, MLG swans (> Dan., Sw. svans; Dan. in secondary uses), NHG schwanz, fr. MHG swanzen ‘move to and fro’, intensive of swanken beside swingen ‘swing, throw’, etc. (Walde-P. 2.526). Weigand-H. 2.812. Kluge-G. 549. Hellquist 1121.
7260:4.73 PREGNANT Goth. inkilpo, pat es pees vos <2 ieee ON unguo, Ulett, hafan- ett. gr Grk. (yyvearpane” tb a id A di, med barni ChSl. neprazdtna NG pracgnans, GRE Dan.  frugtsommelig, svan- SCr. _trudna, breda, nose¢a lat. inciéns | iatoreg: ger; dreglig Boh. téhotna; brezt gravida, ncn a, P Sw. havande; draktig Pol. brzmienna, ciezarna te na Deine OE getacnod, bearn-éacen, Russ. beremennaja Fr encernle, 9” pee 4 med cilde Skt.  garbhini-, garbhavati-, Sp. prenada, Pets ME with childe, with barne etc. Rum. insdr Fie ut NE pregnant, with child Avy. pubra- lorrac . ; drachti Ir. ‘i hea- Du. zwanger; 9g Nir. bruinneach, tourch GHik. smaieee sach MHG _ swanger, trehtec, w. _ beichtog swere : razez, dougerez eee Breese eraeees NHG  schwanger; trdchtig
7295:Du. zwanger, OHG swangar, MHG swanger, NHG schwanger (> Dan. svan- ger) = OE swangor ‘heavy, slow’ : Lith. sunkus ‘heavy’, sunkti ‘become heavy’, older Lith. sunkinga ‘pregnant’. Walde- P. 2.525. Falk-Torp 1210.
7684:etc.) : Norw. dial. svaga ‘vacillate’, ON sveggja ‘turn (a ship)’, (with nasal) OHG etc. swingan ‘swing’, OF swancor, MHG swank ‘pliant, slender’, Skt. svaj- ‘embrace’, fr. a root meaning ‘bend, pliant’ or the like. Walde-P. 2.527. Falk-Torp 1208.
26689:2. Lat. albus (> Rum. alb), Umbr. alfu ‘alba’ : Grk. ad¢és ‘dull-white lep- rosy’, dAdots* evxobs (Hesych.), OHG albiz, ON elpir ‘swan’, etc., IE *albho-. Walde-P. 1.93. Ernout-M. 31f. Walde- H. 1.26 f.
```


## [2026-09-06T20:45:19.452Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ewk-\" --note \"page 265, root Keuk 1, PIE *ḱewk- reconstruction\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/c%CA%BCauka%C4%A7\" --note \"page 265, sog\" 2>/dev/null | tail -1",
 "description": "Fetch PIE root pages"
}
```


### [2026-09-06T20:45:21.691Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b6f89cb20becb486.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7279dcb8e8775f96.txt
```


## [2026-09-06T20:45:27.796Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== HRN ctx 1280-1300 ==\"; sed -n '1280,1300p' HRN.txt\necho \"== HUB ctx 490-510 ==\"; sed -n '488,512p' HUB.txt",
 "description": "Read Horn/Hübschmann afsos"
}
```


### [2026-09-06T20:45:27.849Z] TOOL RESULT

```
== HRN ctx 1280-1300 ==
99. efser 'Krone'.
aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
100. efsurden 'frieren', gefrieren, fusurden^ ßsurden
(Sahn. I, 78 Vers 211).
phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
surf, 'Kälte'.
Siehe np. serd (No. 731).
101. efsös 'Spott, Scherz', fisös,
phlv. afsös 'Spott, Scherz'.
Darmesteter's Erklärung, Et. ir. II, 131 aus aw.
*aiwisaoca' ist unhaltbar, da aw. d im Np. nicht zu s
werden kann.
*) ewsün (Vullers).
*) Zu dem n vergl. Joh. Schmidt, KZ. 32, 385.
*J West*, S. 175: awüar; ZPGl. 24, 10; awavBar.— 24 —
102. ef San den ausschütten', ^'sawrfew.
aw. aiwi + ßünayeinü *sie weiden aus , yt. 14, 56
(Geldner, 3 Yasht, 88) (?); phlv. aßäntan,
103. ef gen den 'wegwerfen', ßgenden^ ewgenden (AM.),
jn::5x (Is. 14, 12).
Kaum etwas anderes als aw. aiwi + [^kan-, wenn-
== HUB ctx 490-510 ==
(fiir afgh. -ww).
99. Np. afsar *Krone' — ap. ^abisarah- *um den Kopf liegt
im Sanskrit vor als abhigiras-, aber mit der Bedeutung :
*den Kopf richtend nach-, zum Kopfe gerichtet'. Horn
vergleicht mit Recht phi. aparsar (= auf dem Kopfe'
d. i.) *Diadeni, Krone' fiir zd. pws5- ZPQI. 24 (= arm.
psak 'Diadem, Krone, Kranz').
100. Arm. j^surt" in ^rt *kalt' zu verbessern.
101. Np. afsos (afgh. LW. afsos 'sorrow, regret') wird auch
von Fr. Mtiller, WZKM. 7, 367 nicht befriedigend
erklart.
102 — 106. Nicht einwandfrei, besonders der Bedeutung
wegen.
108. In der Note wird bemerkt, dass nb wie mh gesprochen
werde. Das gilt aber nur fiir die modernste Aus-
sprache. Friiher wurde n + labiodentales b fiir
ursp. m + b gesprochen.^) Nachdem fe jetzt bilabial
geworden ist, spricht man w6, ebenso wie die Armenier,
die bilabiales b haben, das persische nb in mb umsetzten.
Nur so erklart sich die persische Schreibweise, die der
heutigen Aussprache nicht, der friiheren voUkommen
entspricht. Im Zend war b bilabial, daher mb {kam-
bista- etc.) geschrieben wird, im Altpersischen lasst
die Schrift die Aussprache unentschieden, da der Nasal
vor Verschlusslauten (A, d, t, pi 9, /» ^, i) iiberhaupt
```


## [2026-09-06T20:45:29.253Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A25 \"Proto-Indo-European \\[ edit \\]\" b6f89cb20becb486.txt | head -50\necho \"=== root desc ===\"; grep -n -i \"shine\\|white\\|Root\\b\" b6f89cb20becb486.txt | head -20",
 "description": "Read PIE *ḱewk- page"
}
```


### [2026-09-06T20:45:29.308Z] TOOL RESULT

```
=== root desc ===
```


## [2026-09-06T20:45:42.285Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\nhead -8 web/b6f89cb20becb486.txt; echo \"....\"; sed -n '40,90p' web/b6f89cb20becb486.txt\necho \"=== DRM afsos ===\"; grep -n \"afsôs\\|afsos\\|aiwi-saoca\\|çaoca\" refs/DRM.txt | head",
 "description": "Check PIE page and Darmesteter afsos"
}
```


### [2026-09-06T20:45:42.356Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ewk-
FETCHED: 2026-09-06T16:37:01Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found....
=== DRM afsos ===
1165:çaocant-,  brûlant
4245:\   z.  upa-çukhta,  allumé  z.  çaocayâhi,  que  tu  allumes.
6656:af-car couronne,  de  *abi-çara,  tour  de  tête;  af-çôç raillerie,  de  *abi-çaoca  (vol.  II,  p.  loi).
8461:duit le  zend  çaoca  dans  le  Hâdhôkht  Nosh  (II,  28,  ed.  Haug)  : z.  vat  tum  ainim  avâenôish  çaocaya  kerenavantem', pli.  amat  lak  zaki  zak  anâ  khazîtûnt  havmaud  amatshân afçôç  kart  :
8462:«quand  tu  voyais  un  homme  qui  se  livrait  a   la  raillerie». afçôç  suppose  une  forme  zende  * aiwi-çaoca ;   c   médial  devient régulièrement  z   (vol.  I,  §   27,  1”),  *   afçôz  :   il  y   a   eu  seulement durcissement  de  la  consonne  finale.
8470:Çaoca,  raillerie,  vient  de  la  même  racine  que  çaoca,  combus- tion :   l’insulte  brûle.  Par  une  métaphore  analogue,  la  même  ra- cine çuc  a   donné  le  sanscrit  çoka,  «flamme»  et  «chagrin»;  le zend  çaoka,  flamme,  a   eu  sans  doute  aussi  le  sens  de  chagrin; car  c’est  le  sens  du  persan  çôg,  ^ cf.  l’article  çaokenta.
8472:«Nâméni  aêshâm  drujanâm  naçîïm  kereta1  paiti  janaiti  jata karapanô  cithrâim  jâmâca  meretô  çaoca  yé  zaota  Zarathushtrô ereghatacit  duzhavât  hvàm  hûishtîm  zaoshemca  yatha  kathaca hê  zaosliô.
```


## [2026-09-06T20:45:54.054Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('DRM.txt',encoding='utf8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if 'afçôç  suppose' in p or 'aiwi-çaoca' in p or 'çaokenta' in p:\n        print('leaf',i, '|', re.findall(r'\\n\\s*(\\d{2,3})\\s*\\n', p)[:6])\nEOF",
 "description": "Find Darmesteter leaf for afsos"
}
```


### [2026-09-06T20:45:55.663Z] TOOL RESULT

```
leaf 517 | ['132']
leaf 528 | ['143']
leaf 529 | ['144']
```


## [2026-09-06T20:46:08.017Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%AE%D8%A7%D8%AC/\" --note \"page 265, Mo'in/Dehkhoda entry خاج (MON:1384 check)\"\npython3 tools/fetch_source.py \"https://vajehyab.com/moein/%D8%AE%D8%A7%D8%AC\" --note \"page 265, Mo'in خاج\"",
 "description": "Fetch Mo'in entry for khaj"
}
```


## [2026-09-06T20:46:10.357Z] TOOL CALL #73: Bash

```json
{
 "command": "pdftoppm -f 265 -l 265 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg265 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 265"
}
```


### [2026-09-06T20:46:11.565Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/050ba15f3b410285.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/17c932b1a88d7b7e.txt
```


### [2026-09-06T20:46:13.869Z] TOOL RESULT

```
total 1096
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 16:46 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    132 Sep  6 16:34 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb  11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb  14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb 105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb  92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82276 Sep  6 16:46 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79922 Sep  6 16:42 pg266.png
```


## [2026-09-06T20:46:20.329Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg265.png"
}
```


### [2026-09-06T20:46:20.680Z] TOOL RESULT

```

```


## [2026-09-06T20:46:20.677Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T20:46:39.373Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nhead -6 050ba15f3b410285.txt; grep -n -i \"ارمن\\|خاج\" 050ba15f3b410285.txt | head -20\necho \"===== vajehyab =====\"; head -6 17c932b1a88d7b7e.txt; grep -n \"خاج\\|ارمن\" 17c932b1a88d7b7e.txt | head -10",
 "description": "Check Mo'in fetch results"
}
```


### [2026-09-06T20:46:39.439Z] TOOL RESULT

```
URL: https://abadis.ir/fatofa/%D8%AE%D8%A7%D8%AC/
FETCHED: 2026-09-06T20:46:11Z
STATUS: 200
TITLE: خاج - معنی در دیکشنری آبادیس

خاج - معنی در دیکشنری آبادیس 
4:TITLE: خاج - معنی در دیکشنری آبادیس
6:خاج - معنی در دیکشنری آبادیس 
10: خاج
13: مترادف خاج : چلیپا، صلیب، نرمه گوش، گشنیز
20: خاج. ( ارمنی ، اِ ) بر وزن تاج بمعنی چلیپا باشد که صلیب نصاری است. ( برهان ) ( آنندراج ) ( جهانگیری ). رجوع بصلیب شود. || نرمه گوش یعنی جائی که گوشواره در آن کنند. ( برهان ) ( آنندراج ) : 
21:دولت از خاج گوش بنده تو
22:بنده را حلقه درکشند بخاج. سوزنی.
28:( اسم ) صلیب چلیپا . یا خاج اعظم . صلیبی که عیسی را بدان دار کشیدند . 
32: [ ارمن . ] (اِ. ) ۱ - صلیب ، چلیپا. ۲ - یکی از خال های ورق ، گشنیز. 
53: حد وسط، خاج، صلیب، چلیپا، اختلاف، نا درستی
55: گوشه، لخته، خاج، اویز، نرمه، بخشی از عضله یا مغز
57: انجمن، چماق، باشگاه، کانون، گرز، باتون، مجمع، خال گشنیز، خاج، عمود
59: خاج، خاج کوچک، صلیب کوچک
61: خاج
63: خاج
65: خاج، نرمه گوش، قسمت اویزان گوش
67: خاج، صلیب، چلیپا
87: در گفتار پارسی به مناسک مسیحی از شرقی غربی تفاوت کلام گذاشته میشه برای تشخیص گونه آن خاج کشیدن ازین مورد است. 
88:خاج کشیدن یعنی صلیب کشیدن بر سینه ولی بیشتر این را به مسیحیان ارتدکس در ادبیات میگن ویا در ترجمه کتاب های برآمده از فرهنگ دینی ارتدکس مثل روسیه ، ارمنستان ، گرجستان و دیگر. .
===== vajehyab =====
URL: https://vajehyab.com/moein/%D8%AE%D8%A7%D8%AC
FETCHED: 2026-09-06T20:46:11Z
STATUS: 200
TITLE: معنی خاج | فرهنگ انتشارات معین | واژه یاب

'
4:TITLE: معنی خاج | فرهنگ انتشارات معین | واژه یاب
9: معنی خاج | فرهنگ انتشارات معین | واژه یاب 
17: خاج
20: [ ارمن . ] (اِ.) 1 - صلیب ، چلیپا. 2 - یکی از خال های ورق ، گشنیز.
```


## [2026-09-06T20:47:13.947Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== WLD Bd1 keuk (p.378) ==\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (385,386,387):\n    print('--- leaf',i,'---'); print(t[i][:1400])\nEOF",
 "description": "Find WLD keuk- entry"
}
```


## [2026-09-06T20:47:15.194Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHD afsos ==\"; grep -n \"afsōs\\|afsos\\|abgws\\|mockery\" PHD.txt PHD_mackenzie.txt | head\necho \"== NYB afsos ==\"; grep -n -i \"afsos\\|’psws\" NYB_vol2_glossary.txt | head",
 "description": "Grep MacKenzie/Nyberg for afsos"
}
```


### [2026-09-06T20:47:15.676Z] TOOL RESULT

```
== WLD Bd1 keuk (p.378) ==
--- leaf 385 ---
                                             keuero               keuk-. kuk-                                       377

*ku-los „verbrannt
                              £
                                  ‘
                                      beruhenden lit. Worten stellt Petersson LUA. 1916 48
48 Anm.          1     auch   lett.     kvclet   „gliihen“,          kvele „Entziindung einer                Wunde“
(   *kuu-el °~, vielleicht zu einem
    :




                                                   Yerbum *k(u)wetit).
        Die Sippe von         aksl. kuriti se          „rauehen“,                  lit.   kuriu, kiirti „heizen“   (s. u.

*ker- „brennen“) hat    dagegen wzhaftes r, widerstrebt auch nach Berneker
651 f. in der slav. Intonation der Ankniipfung an *keu- (nicht ganz zwingen-
der Einwand, da die Reduktionsstufe *Lni- und die Wirkung des r in der
Gruppe *kaur- in Rechnung zu setzen wiire), ebenso (s. Yf. LEWb. 2 u. carlo )
in der Kiirze des                 u in lit. kuriu      ,
                                                               got. liauri.


keuero- „Nord, Nordwind".
   Lat. caurus (corns) „Nordwind“ (nach Hirt IF. 37, 224 mit lat. Wandel
von -eu- zu -dv- aus keuero- ? andernfalls ware Ablaut *kdiiero- anzunehmen);
lit. sidure „Norden“, siaurys „Nordwind“, abg. seven „Norden“. Yanicek
LEWb. 2 307 nicht wahrscheinlicher stellt Thurneysen Thes. fu
--- leaf 386 ---
                                                                              ;                                            g




37S                                                                tenq           qeud-


keuq-           ,   leuchten, hell, weiB sein. gliihen".
        Ai. cb^ati, euryati, coclti „leuchtet, gliinzt, gliiht, brennt, leidet heftigen
                                                                                                                                                                ££
Schmerz, trauert'*, cocayati „entziindet. betriibt; 1st traurig, beklagt gdk'i                                                                                       ,



m. „Glut, Fbiniine, Qual, Sclimerz, Trailer*, cuci- „leuchtend, glanzend,
blank, rein, lauter,                   tadellos“,                  ctikru- ,,licht,             klar, hell, weiB, rein'*, cukti-
f. „Huschel, Perlenmusehel, Perlmutter" (wenn .,*glanzend“), vielleicht
                                                                             £
 ukta- „sauer (wenn ,,brennend von Geschmack“) av. saoeant- „brennend‘
              ££
<
                                                                                                              ;                                                                       ,


saocayciti ..inflammat = incitat", npers. srxtan „anziinden, verbrennen
 
--- leaf 387 ---
                  g                                                                                              ;




                                                     qegep-                                                   :(79


„dummer              Schaden, Yerlust; Schelm", kndv f. „Schwarzkunst“,
                  Streich;
bulg. kud'x, „schelte,schmahe“, skr. kudvn, -iti ,,tadeln, verleumden“, slov.
kdditi „riigen, tadeln; verschmahen“, poln. mdartl. prsc-, przy-kmhic „ver-
derben, langweilen“.
   Zupitza Gutt. 117, Johansson IF. 19, 125ff. (aber unter Zugrundelegung
eines (s)qeu- „spitz sein, stechen, bohren“), Holthausen AfnSpr. Ill, 4l8f.,
Berneker 637 (halt mit Recht die bait. Sippe von skaudcti ,.schmerzen“,
skundd „Anklage“ fern, s. u. sqeud- „unwillig sein“), Persson Beitr. 1 S6 f.
   Gr. xvdo    „Ruhm“ (von Persson als „Ruf‘‘ angereiht) besser zn slav.
nudo, s. *qeu- „worauf achtenA                   —
                                      Lat. cm sn , das Holthausen IF. 25, 149
anreiht (vgl. crimen eig. ,Geschrei“, ags. inca „Klage, Klagegrund, Groll,
Yerdacht, Ursache“), widerspricht dem Yok. von mhd. hiityn freilich
zeigt die vielleicht unserm qeiul- zugrunde liegende Schallwz. Mu-, keti-
ebenfalls a und e im Wechsel), und kann aucb andere Gdbed. haben (siebe
Vf. LEWb. 2 s. v.; Ehrlichs BPhAV. 1911, 1576 Yerb. m. lit. skundd s. o.,
```


### [2026-09-06T20:47:15.735Z] TOOL RESULT

```
== PHD afsos ==
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD.txt:2833:mocker afsosgar.
PHD.txt:2834:mockery afsēs, riyahrih.
PHD_mackenzie.txt:888:   afsos [,psws I N -] scorn, mockery.
PHD_mackenzie.txt:4406:riyahrih [ld)hlyh] scorn, mockery.
PHD_mackenzie.txt:7115:mocker afsosgar.                               mutability wardisn(ig)ih.
PHD_mackenzie.txt:7116:mockery afsos, riyahrih.                       muzzle poz(ag).
PHD_mackenzie.txt:7502:    tabahihistan.                          scorn afsos, riyahrih.
PHD_mackenzie.txt:11493:afsos                    -(,)t'C:'4l)I     abauyawanu            ~ , t"'O' te.,)' V'
== NYB afsos ==
536:apa-sös [’psws] derision, mockery, scorn 6616, 7527. — Ps. ?pswsy; Paz. awasos; NP afsós; < OP apa-cauga- < Olr "apa- sraudra- from apa + Av. (1639 sqq.) srav-
```


## [2026-09-06T20:48:46.581Z] AGENT

Now I have everything I need. Let me write the verification file.


## [2026-09-06T20:56:13.206Z] TOOL CALL #78: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk265.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SUX = \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AE%D8%AA%D9%86\"\nW_SORX = \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%AE\"\nW_SOG = \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%DA%AF\"\nW_SOGAND = \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%DA%AF%D9%86%D8%AF\"\nW_KHAJ = \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D8%AC\"\nW_XACH = \"https://en.wiktionary.org/wiki/%D5%AD%D5%A1%D5%B9\"\nW_XAY = \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\"\nW_KUK = \"https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CE%BA%CE%BD%CE%BF%CF%82\"\nE_CYG = \"https://www.etymonline.com/word/cygnet\"\nAB_KHAJ = \"https://abadis.ir/fatofa/%D8%AE%D8%A7%D8%AC/\"\nVY_KHAJ = \"https://vajehyab.com/moein/%D8%AE%D8%A7%D8%AC\"\n\ndoc = {\n \"pdf_page\": 265,\n \"book_page\": 235,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n\n # ------------------------------------------------------------------ entry 0\n {\n  \"entry\": 0,\n  \"root\": \"Keuk 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ḱewk- (Pokorny keuk-) 'to shine, be bright, be white; glow, burn'\",\n  \"note\": \"Pokorny IEW 597 has the root under exactly this shape and gloss — 'keuk- \\u2018leuchten, hell, wei\\u00df sein, gl\\u00fchen\\u2019' — and its material is almost literally Nourai's chart: 'av. sao\\u010dint- \\u201ebrennend\\u201c, sao\\u010dayeiti, npers. s\\u014dxtan, av. upa-suxta-, \\u0101tr\\u0259-saoka- m. \\u201eFeuerbrand\\u201c, np. s\\u014dg \\u201eTrauer\\u201c (arm. sug ist iran. Lw.); av. suxra-, np. surx \\u201erot\\u201c; gr. \\u03ba\\u03c5\\u03ba\\u03bd\\u03bf\\u03c2 \\u201eSchwan\\u201c als \\u201eder Wei\\u00dfe\\u201c'. Watkins/AHD gives the same root ('keuk-. To be white, be bright, shine'), and Wiktionary reconstructs *\\u1e31ewk- for the Persian words. Language label and gloss are therefore both right; the only reservation is that Cheung (2007: 339 s.v. *sauc\\u2081) warns 'The IE origin of *sauc cannot be ascertained, perhaps it is a \\u201cReimbildung\\u201d with *rauc', i.e. the Iranian branch of the root is safer than the PIE reconstruction itself.\",\n  \"note_fa\": \"ری\\u0634هٔ هندواروپایی آغازین *\\u1e31ewk- «درخشیدن، سپید و روشن بودن، سوختن»؛ پوکورنی (ص ۵۹۷) دقیقاً با همین صورت و همین معنی آن را آورده و مواد آن (اوستایی saok-/sao\\u010d-، suxra-، \\u0101tr\\u0259-saoka-، upa-suxta-، فارسی نو س\\u0648ختن، سوگ، سرخ و یونانی k\\u00fdknos) همان است که نورایی در نمودار آورده است. واتکینز (فرهنگ ریشه\\u200cهای هندواروپایی) نیز همین ریشه را با معنی «سپید بودن، درخشیدن» ثبت کرده است. تنها احتیاط این است که چونگ (۲۰۰۷) خاستگاه هندواروپایی ستاک ایرانی *sauc را قطعی نمی\\u200cداند. در مجموع ادعای نورایی دربارهٔ ریشه درست است.\",\n  \"sources\": [W_SUX, W_SORX, W_SOG, W_SOGAND],\n  \"ref_check\": [\n    {\"ref\": \"POK:597\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt \\u21b5-page 257/258 (printed 597): 'keuk- \\u201aleuchten, hell, wei\\u00df sein, gl\\u00fchen\\u2018. Ai. \\u015b\\u00f3cati ... av. sao\\u0161int- \\u201abrennend\\u2018, sao\\u010dayeiti \\u201ainflammat = incitat\\u2018, npers. s\\u014dxtan \\u201aanz\\u00fcnden, verbrennen\\u2018, av. upa-suxta- \\u201aangez\\u00fcndet\\u2018, \\u0101tr\\u0259-saoka- m. \\u201aFeuerbrand\\u2018, np. s\\u014dg \\u201aTrauer, Kummer\\u2018 (arm. sug \\u201aTrauer\\u2018 ist iran. Lw.); av. suxra- \\u201aleuchtend (vom Feuer)\\u2018, np. surx \\u201arot\\u2018; gr. \\u03ba\\u03c5\\u03ba\\u03bd\\u03bf\\u03c2 \\u201aSchwan\\u2018 als \\u201ader Wei\\u00dfe\\u2018. WP. I 378.' Grep: awk RS=\\\"\\\\f\\\" NR==257,258 POK_02.txt.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 378 (WLD_Bd1_pages.txt leaf 386)\", \"stance\": \"supports\",\n     \"note\": \"'keuq- \\u201aleuchten, hell, wei\\u00df sein, gl\\u00fchen\\u2018. Ai. \\u015b\\u00f3cati ... av. saocant- \\u201abrennend\\u2018, saocayati \\u201ainflammat = incitat\\u2018, npers. s\\u014dxtan \\u201aanz\\u00fcnden, verbrennen\\u2018' \\u2014 the entry Pokorny 597 refers back to (WP. I 378).\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 628\", \"stance\": \"supports\",\n     \"note\": \"'keuk-. To be white, be bright, shine. Suffixed zero-grade form *kuk-no- in Greek kuknos, swan: CYGNET, CYGNUS. [Pok. keuk- 597.]'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p. 339 s.v. *sauc\\u2081\", \"stance\": \"partial\",\n     \"note\": \"Gives the Iranian root ('*sauc\\u2081 to burn, emit flames', Av. saoc-, MP swc-/s\\u014dxtan, NP soxtan/s\\u014dz-, Skt. \\u015boc) with 'Pok.: 597', but adds 'The IE origin of *sauc cannot be ascertained'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, keuk- section (IEC.txt lines 7101-7127)\", \"stance\": \"silent\",\n     \"note\": \"Mann's keuk-/keukos entries are all 'top, peak, tuft', 'curl up', 'howl' \\u2014 no 'shine/white' root; grep 'keuk' in IEC.txt returns nothing relevant.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Avestan\",\n    \"words\": \"sao\\u010d, sauk, saux; saoka; suxra; suxra-vard; aiwi-saoka; upa-suxta, \\u00e2tra-saoka, sao\\u010dint\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"The Avestan verb is saok-/sao\\u010d- 'to burn, be in bright flame' (Bartholomae AiW col. 1548: 'in lichter Flamme brennen, flammen', pres. part. saocint- V.9.56 sao\\u010dint\\u0259 paiti \\u0101\\u03b8r\\u0259, caus. sao\\u010dayat Y.32.14); Nourai's three shapes sao\\u010d / sauk / saux are the full grade, the k-variant of the same root, and the zero grade *suk- > sux- that appears in suxra- and upa-suxta-. suxra- 'red, glowing (of fire)' is real (AiW 1583, V.2.8 '\\u0101\\u03b8r\\u0259m\\u010da suxr\\u0259m sao\\u010dint\\u0259m'), and upa-suxta- 'kindled', \\u0101tr\\u0259-saoka- 'firebrand' and saocant-/sao\\u010dint- 'burning' are all listed together at Pokorny 597. Two items are not attested Avestan words, however: (a) 'suxra-vard \\u201ared rose\\u201d' is nowhere in Bartholomae \\u2014 Av. var\\u0259\\u03b4a- is itself only a doubtful plant name (AiW 1362 '2) Name einer Pflanze, vll. \\u201aRose\\u2018'); the compound is Farahvashi's reconstruction *suxra-varda- posited to explain the toponym Sohravard (IRN 128). (b) 'aiwi-saoka \\u201aburn in regret\\u2018' is Darmesteter's conjecture *aiwi-\\u00e7aoca- (\\u00c9t. ir. II 131, 'af\\u00e7\\u00f4\\u00e7 suppose une forme zende *aiwi-\\u00e7aoca'), and Horn (Grundriss no. 101) rejected it outright. Also, the simplex saoka- glossed 'flame' is in Bartholomae only saoka- n./saok\\u0101- f. 'Nutzen, Vorteil' (advantage); the 'flame' sense belongs to the compound \\u0101tr\\u0259-saoka-.\",\n    \"derivation_fa\": \"ستاک اوستایی saok-/sao\\u010d- «سوختن، شعله\\u200cور بودن» (بارتولومه، ستون ۱۵۴۸؛ اسم فاعل sao\\u010dint- و سببی sao\\u010dayeiti) از ریشهٔ هندواروپایی *\\u1e31ewk- است؛ سه صورتی که نورایی آورده (sao\\u010d / sauk / saux) به\\u200cترتیب پایهٔ کامل، گونهٔ k\\u200c\\u200cدار و پایهٔ صفر *suk- > sux- است که در suxra- «سرخ، فروزان» و upa-suxta- «افروخته» دیده می\\u200cشود؛ این\\u200cها همه در بارتولومه و پوکورنی (ص ۵۹۷) گواه دارند. اما دو مورد در نمودار واژهٔ اوستایی گواهیده نیست: «suxra-vard» (گل سرخ) در فرهنگ بارتولومه نیامده و بازسازی فره\\u200cوشی برای نام سهرورد است، و «aiwi-saoka» تنها حدس دارمستتر (مطالعات ایرانی، ج ۲، ص ۱۳۱) برای توضیح «افسوس» است که هرن آن را رد کرده است. افزون بر این، saoka- در اوستا به معنی «سود، بهره» است و معنی «شعله» تنها در ترکیب \\u0101tr\\u0259-saoka- دیده می\\u200cشود. بنابراین این گره «با احتیاط پذیرفتنی» است.\",\n    \"sources\": [W_SUX, W_SORX, W_SOGAND],\n    \"ref_check\": [\n      {\"ref\": \"POK:597\", \"status\": \"supports\",\n       \"note\": \"Printed p.597 lists 'av. sao\\u0161int- \\u201abrennend\\u2018, sao\\u010dayeiti ... av. upa-suxta- \\u201aangez\\u00fcndet\\u2018, \\u0101tr\\u0259-saoka- m. \\u201aFeuerbrand\\u2018 ... av. suxra- \\u201aleuchtend (vom Feuer)\\u2018' \\u2014 four of Nourai's six items verbatim.\"},\n      {\"ref\": \"HRN:161,165\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss, no. 730 (p.161) 'sur\\u1e35, Suhr\\u0101b, Suhr-esp ... ap. \\u041euxra- (N. pr.); aw. su\\u1e35ra- \\u201arot\\u2018; phlv. su\\u1e35r; ai. \\u015bukr\\u00e1-' and no. 750 (p.165/166) 's\\u014dxten \\u201aanz\\u00fcnden, verbrennen\\u2018 ... aw. \\u221asaoc-, sao\\u010dayahi \\u201aanz\\u00fcnden\\u2018, \\u0101tar\\u0259-saoka- \\u201aFeuerbrand\\u2018, saocant- \\u201abrennend\\u2018'. (leaf = printed + 22 in HRN.txt)\"},\n      {\"ref\": \"IRN:128\", \"status\": \"partial\",\n       \"note\": \"Farahvashi, Iranvij p.128 (IRN_pages.txt pdf 139) has the vard/rose material and reconstructs 'جزء اول کلمهٔ سهرورد suxra-varda ... و سهرورد بمعنی سرخ گل است', i.e. he posits the compound rather than citing an attested Avestan suxra-vard.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW cols. 1548 (saok-), 1551 (saok\\u0259nta-vant-), 1583 (suxra-), 1362 (var\\u0259\\u03b4a-), 1546 (saoka-)\", \"stance\": \"partial\",\n       \"note\": \"Confirms 'j. saok- \\u201ain lichter Flamme brennen, flammen\\u2018: sao\\u010dint\\u0259 paiti \\u0101\\u03b8r\\u0259 V.9.56; \\u0101\\u03b8r\\u0259m\\u010da suxr\\u0259m sao\\u010dint\\u0259m V.2.8' and 'j., g. suxra- Adj. \\u201arot\\u2018, vom Feuer', but has no compound suxra-var\\u0259\\u03b4a- and no aiwi-saoka-; saoka- is glossed 'Nutzen, Vorteil'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 730 p.161, no. 750 p.165-166, no. 101 p.23-24\", \"stance\": \"partial\",\n       \"note\": \"Supports suxra- and saoc-, but at no. 101 explicitly kills the aiwi-saoka etymology: 'Darmesteter's Erkl\\u00e4rung, \\u00c9t. ir. II, 131 aus aw. *aiwisaoca- ist unhaltbar, da aw. \\u010d im Np. nicht zu s werden kann.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 339 s.v. *sauc\\u2081\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: saoc- \\u201ato burn\\u201d ... Partic.: pres. them. YAv. saocint- (V); Caus. ... OAv. saocaiiat (Y 32.14)' \\u2014 the same paradigm Nourai charts.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Persian\",\n    \"words\": \"s\\u016dxtan \\u00abسوختن\\u00bb; s\\u016dk \\u00abسوک ۱ ( سوگ ۱ )\\u00bb; sorx \\u00abسرخ ( سرخاب ، سهراب )\\u00bb; Sohrvard \\u00abسُهروَرد\\u00bb; afs\\u016ds \\u00abافسوس\\u00bb (+ سوزش ، سوزان ، سوزاک ، سوز ، جانسوز)\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"Four of the five words are sound; the fifth (afs\\u016ds) and one gloss are not. (1) سوختن s\\u016dxtan/s\\u016dz- < MP s\\u014dxtan, s\\u014dz- [swhtn', swc-] (MacKenzie 78; Nyberg II 3465 's\\u014dxtan [swhtn'] s\\u014dc- to burn \\u2014 Av. saok-') < Old Iranian *sauk-ta- / pres. *sauk-a-; Abolghasemi (FFD 61) states it exactly so: 'سوخت \\u2190 فارسی میانه s\\u014dxt \\u2190 ایرانی باستان *sauk-ta ... ریشهٔ sauk به معنی سوختن است' and 'سوز \\u2190 فارسی میانه s\\u014dz \\u2190 ایرانی باستان *sauk-a'; the -k- + -t- > -xt- development is the regular Iranian one, and the extra words سوز، سوزش، سوزان، سوزاک، جانسوز are all built on that present stem. (2) سوگ/سوک s\\u014dg 'mourning' < MP s\\u014dg [swk'] < OP *\\u03b8auga(h) < PIr *cawkah, cognate with Skt \\u015b\\u00f3ka- 'flame; grief' \\u2014 the 'burning > grief' shift is already Indo-Iranian; Arm. sug 'grief' is an Iranian loan (Pokorny 597; Mo'in's footnote at BQT 1190 gives exactly this, citing Horn). (3) سرخ sorx < earlier سهر suhr < MP suxr/suhr [swhl] < OP *\\u03b8uxra- (cf. the Achaemenid PN Ou\\u03c7ra-), sister-form of Av. suxra-; NP sorx shows metathesis of suhr, while سرخاب and سهراب Sohr\\u0101b keep the older shape \\u2014 Borhan-e Q\\u0101te\\u02bf p.1195 s.v. سهراب: 'اصل سُهراو (او سرخ)' and 'سرخاب Surx\\u0101b = سرخ suxra + آب'. (4) سهرورد Sohrvard is indeed *suxra-varda- 'red rose', but Nourai's gloss 'a town near Tehran' is wrong: his own source Farahvashi (IRN 128) says 'نام سهرورد که روستایی است از روستاهای زنجان و محل تولد شیخ اشراق شهاب\\u200cالدین سهروردی است' \\u2014 Sohravard is in Zanjan; the rose-village near Tehran that Farahvashi mentions on the same page is وردآورد Vard-\\u0101vard. (5) افسوس afs\\u016ds: Nourai follows Darmesteter (\\u00c9t. ir. II 131, *aiwi-\\u00e7aoca- 'the insult burns'), but Horn (no. 101) rejects it because Avestan \\u010d cannot yield NP s, H\\u00fcbschmann (PSt. 101) calls the word unexplained, and Nyberg (Manual II, p. 536) derives MP afs\\u014ds/apa-s\\u014ds [\\u02beapsws] 'derision, mockery' from apa- + Av. srav- 'to speak' instead. MacKenzie also glosses MP afs\\u014ds 'scorn, mockery', not 'regret' \\u2014 the sense 'alas, regret' is a later New Persian development.\",\n    \"derivation_fa\": \"چهار واژه از پنج واژهٔ این گره درست است و یکی نه. «سوختن» از فارسی میانهٔ s\\u014dxtan (ستاک حال s\\u014dz-) و آن از ایرانی باستان *sauk-ta-؛ ابوالقاسمی در «فعل\\u200cهای فارسی دری» (ص ۶۱) همین را می\\u200cگوید: «سوخت \\u2190 فارسی میانه s\\u014dxt \\u2190 ایرانی باستان *sauk-ta». مشتق\\u200cهای سوز، سوزش، سوزان، سوزاک و جانسوز همه بر ستاک حال s\\u014dz- < *sauk-a- ساخته شده\\u200cاند. «سوگ» از فارسی میانهٔ s\\u014dg، از ایرانی باستان *\\u03b8auga-، هم\\u200cریشه با سنسکریت \\u015b\\u00f3ka- «شعله؛ اندوه»؛ تحول معنایی «سوختن ← اندوه» از دورهٔ هندوایرانی است و «سوگ» ارمنی (sug) وام\\u200cواژهٔ ایرانی است. «سرخ» شکل قلب\\u200cشدهٔ suhr است، از فارسی میانهٔ suxr/suhr و ایرانی باستان *\\u03b8uxra-؛ صورت کهن\\u200cتر در «سرخاب» و «سهراب» مانده است (حاشیهٔ برهان قاطع، ص ۱۱۹۵). «سهرورد» به\\u200cدرستی از *suxra-varda- «گل سرخ» است، اما توضیح نورایی که آن را شهری «نزدیک تهران» خوانده نادرست است؛ خودِ منبع او (ایرانویج، ص ۱۲۸) می\\u200cگوید سهرورد روستایی از روستاهای زنجان و زادگاه شهاب\\u200cالدین سهروردی است و روستای نزدیک تهران «وردآورد» است. سرانجام «افسوس»: نورایی از دارمستتر پیروی کرده که آن را از *aiwi-\\u00e7aoca- می\\u200cگیرد، ولی هرن این را رد کرده است («\\u010d اوستایی در فارسی به s بدل نمی\\u200cشود») و هوبشمان نیز آن را توضیح\\u200cناشده می\\u200cداند؛ نیبرگ آن را از apa- + srav- «گفتن» می\\u200cگیرد و معنی فارسی میانهٔ afs\\u014ds «ریشخند، تمسخر» است نه «دریغ». پس پژوهش امروزی این بند را رد می\\u200cکند.\",\n    \"sources\": [W_SUX, W_SORX, W_SOG, W_SOGAND],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1183\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Q\\u0101te\\u02bf p.1183 (BQT_v2_pages.txt leaf 647), Mo'in's footnote on سوختن: 'اوستا ریشهٔ suk / saok- (روشن کردن)، saoka- (شعلهٔ آتش)، suxta- (سوخته)؛ پهلوی s\\u014dc(i)\\u0161n, s\\u014dxtan؛ هندی باستان \\u015boca-؛ کردی s\\u014dtin' \\u2014 exactly Nourai's arrow.\"},\n      {\"ref\": \"BQT:1189\", \"status\": \"supports\",\n       \"note\": \"p.1189/1190 (leaves 653-654), Mo'in on سوگ: 'هرن این کلمه را در فارسی s\\u014dg ضبط کرده، قی: اوستا \\u0101tar\\u0259-saoka- (شعلهٔ آتش)، هندی باستان \\u015boka- بمعنی اذیت، درد، اندوه و عزا ... ارمنی sug (اندوه و عزا)'. (page fixed by the catch-line 'بقیه در صفحهٔ ۱۱۹۰' at the foot of leaf 653)\"},\n      {\"ref\": \"BQT:1195\", \"status\": \"supports\",\n       \"note\": \"p.1195 (leaf 659, headword سهراب): 'سهراب ... اصل سُهراو (او سرخ)' and footnote 'سرخاب Surx\\u0101b (م.م.) از: ۱ سرخ (suxra) + ۲ آب' \\u2014 supports sorx/سرخاب/سهراب, but has no entry سهرورد.\"},\n      {\"ref\": \"DRM:131\", \"status\": \"supports\",\n       \"note\": \"Darmesteter, \\u00c9tudes iraniennes II p.131 (DRM.txt leaf 517): 'af\\u00e7\\u00f4\\u00e7 suppose une forme zende *aiwi-\\u00e7aoca ... \\u00c7aoca, raillerie, vient de la m\\u00eame racine que \\u00e7aoca, combustion : l'insulte br\\u00fble ... le zend \\u00e7aoka, flamme, a eu sans doute aussi le sens de chagrin; car c'est le sens du persan \\u00e7\\u00f4g'. So the reference does say what Nourai's arrow says \\u2014 but it is a claim Horn rejected two pages of scholarship later.\"},\n      {\"ref\": \"IRN:128\", \"status\": \"contradicts\",\n       \"note\": \"Iranvij p.128: 'ورد\\u0622ورد Vard-\\u0101varda که روستایی است نزدیک تهران' vs 'نام سهرورد که روستایی است از روستاهای زنجان و محل تولد ... سهروردی'. Nourai has transferred 'near Tehran' from Vard\\u0101vard to Sohravard.\"},\n      {\"ref\": \"FFD:61\", \"status\": \"supports\",\n       \"note\": \"Abolghasemi, Fe\\u02bfl-h\\u0101-ye F\\u0101rsi-ye Dari p.61 (pdf 66): 'سوخت \\u2190 فارسی میانه s\\u014dxt \\u2190 ایرانی باستان *sauk-ta ... ریشهٔ sauk به معنی (سوختن) است' and 'سوز \\u2190 فارسی میانه s\\u014dz \\u2190 ایرانی باستان *sauk-a'.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 6, 78\", \"stance\": \"partial\",\n       \"note\": \"'s\\u014dxtan, s\\u014dz- [swhtn', swc- | M swxt, swc-] burn', 'suxr [swhl | N surx] red', 's\\u014dg [swh | N so(y)] ... add N \\u2018grief\\u2019' \\u2014 all confirmed; but 'afs\\u014ds [\\u02beps\\u0175s | N ~] scorn, mockery', not 'regret'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual II, nos. 3465, 3574, 536\", \"stance\": \"partial\",\n       \"note\": \"'s\\u014dxtan [swhtn'] s\\u014dc- ... Av. (1548 sq.) saok-; NP s\\u014dxtan s\\u014dz-' and 'suxr [swhl] red ... Av. (1582) suxra-; OP cf n. pr. Ou\\u03c7ra-; NP surx' support Nourai, but 'apa-s\\u014ds [\\u02beapsws] derision, mockery, scorn ... NP afs\\u00f3s; < OP apa-cauga- < OIr *apa-srau\\u03b8ra- from apa + Av. srav-' contradicts the afs\\u016ds arrow.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 101 (p.23-24), no. 730 (p.161), no. 750 (p.165-166), no. 756 (p.167)\", \"stance\": \"partial\",\n       \"note\": \"Supports s\\u016dxtan, sorx and s\\u014dg ('756. s\\u014dg \\u201aTrauer, Kummer\\u2018 ... aw. \\u0101tar\\u0259-saoka- \\u201aFeuerbrand\\u2018; ai. \\u015b\\u00f3ka-; arm. sug'), but rejects afs\\u016ds < *aiwi-saoca-.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien no. 101\", \"stance\": \"contradicts\",\n       \"note\": \"'Np. afsos (afgh. LW. afsos \\u2018sorrow, regret\\u2019) wird auch von Fr. M\\u00fcller, WZKM. 7, 367 nicht befriedigend erkl\\u00e4rt.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 339-340 s.v. *sauc\\u2081\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: Widely attested: NP soxtan/s\\u014dz-, Kurd. sotin/so\\u017e- ... *MIDDLE PERSIAN: MMP swc-, BMP swc- /s\\u014dz-/ ... Inf.: BMP swhtn /soxtan/'.\"},\n      {\"src\": \"IRN\", \"where\": \"Iranvij p.128\", \"stance\": \"partial\",\n       \"note\": \"Supports Sohrvard = suxra-varda 'red rose' but places it in Zanjan, not near Tehran.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Avestan\",\n    \"words\": \"saokenta; saokenta-vant\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Young Avestan saok\\u0259nta-vant- is attested twice, in the Vendidad passage on the ordeal-water: Bartholomae AiW col. 1551 's. j. saok\\u0259nta-vant- Adj. (fem. -vaiti-) \\u201aSchwefel enthaltend, mit Schwefel versetzt\\u2018: \\u0101p\\u0259m -vaitim zaranyavaitim v\\u012b\\u0161uxavaitim V.4.54, 55'. The base saok\\u0259nta- 'sulphur' is not separately attested in the Avesta but is guaranteed both by this -vant- derivative and by the Sogdian and Middle Persian nouns (Sogd. swk\\u02bcnt, MP s\\u014dgand), so it is a legitimate reconstruction, not an invention. Morphologically it is a -nt- formation on the same saok- 'to burn' as node #1 \\u2014 sulphur is 'the burning stuff' \\u2014 and Horn (no. 757, p.167) gives exactly this chain: 's\\u014dgend \\u201aEid\\u2018 \\u2014 aw. saok\\u0259nta-vant- \\u201aSchwefel enthaltend\\u2018 (vergl. Geldner, Studien I, 103)'. Nourai's gloss for the compound ('a drink mixed with sulfur') is a paraphrase of the Vendidad context (it qualifies \\u0101p- 'water'), not of the word itself, which means only 'containing sulphur'.\",\n    \"derivation_fa\": \"صفت اوستایی نو saok\\u0259nta-vant- «دارای گوگرد، آمیخته به گوگرد» دو بار در وندیداد (۴.۵۴ و ۵۵) دربارهٔ آبِ سوگند به\\u200cکار رفته است (بارتولومه، ستون ۱۵۵۱). خودِ اسم saok\\u0259nta- «گوگرد» در متن\\u200cهای اوستایی به\\u200cتنهایی نیامده، اما هم از همین مشتق و هم از صورت\\u200cهای سغدی swk\\u02bcnt و فارسی میانهٔ s\\u014dgand بازسازی\\u200cشدنی است. ساخت واژه پسوند -nt- بر ستاک saok- «سوختن» است، یعنی «مادهٔ سوزان». هرن (شمارهٔ ۷۵۷، ص ۱۶۷) نیز همین زنجیره را می\\u200cآورد. ادعای نورایی درست است؛ تنها معنی\\u200cای که برای ترکیب داده («نوشیدنی آمیخته به گوگرد») برگرفته از بافت وندیداد است نه از خودِ واژه.\",\n    \"sources\": [W_SOGAND],\n    \"ref_check\": [\n      {\"ref\": \"HRN:167\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss no. 757, p.167 (HRN.txt leaf 189): 's\\u014dgend \\u201aEid\\u2018. aw. saok\\u0259nta-vant- \\u201aSchwefel enthaltend\\u2018 (vergl. Geldner, Studien I, 103). LW. kurd. s\\u014dnd \\u201aEid\\u2018; bel. sau\\u0121ind, s\\u014dgind.'\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1551\", \"stance\": \"supports\",\n       \"note\": \"'j. saok\\u0259nta-vant- Adj. (fem. -vaiti-) \\u201aSchwefel enthaltend, mit Schwefel versetzt\\u2018: \\u0101p\\u0259m -vaitim zaranyavaitim v\\u012b\\u0161uxavaitim V.4.54, 55'. (grep 'Schwefel' BRT.txt)\"},\n      {\"src\": \"SOD\", \"where\": \"Gharib nos. 9044/9053 (p. ~365-366)\", \"stance\": \"supports\",\n       \"note\": \"Gharib himself derives the Sogdian word from the Avestan one: 'so\\u0263and \\u00a9<Av. saok\\u0259nta ...' and 'sokand \\u00a9Av. saok\\u0259nta-, Khwar. sknt'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 340 s.v. *sau\\u010d 'to call'\", \"stance\": \"partial\",\n       \"note\": \"Notes the Iranian oath-phrase family ('Sogd. swk\\u02bcnt xwr-, MMP swgnd xwrdn, NP saugand xurdan, Kurd. sont xarin, etc., see Schwartz 1989: 293 ff.') without deciding the root.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Persian\",\n    \"words\": \"sogand \\u00abسوگند\\u00bb\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"NP س\\u0648گند sogand/sawgand 'oath' < MP s\\u014dgand [swknd], Manichaean MP swgnd, Pazand sawagand (Nyberg II 3460; MacKenzie 78 's\\u014dgand [swknd | M swgnd, N s\\u014dgand] oath', with the collocation 's\\u014dgand xwardan to swear an oath') < Old Iranian *saukanta- 'sulphur (water)' = Av. saok\\u0259nta- of node #3. Phonetically the chain is regular: Av. -nt- > MP -nd- after a long vowel, Av. sao- > MP s\\u014d- > NP saw-/so-. Semantically the word is a fossil of the sulphur ordeal: the accused drank sulphurous water (Av. \\u0101p- saok\\u0259nta-vaiti-, V.4.54-55) and was judged by the effect \\u2014 which is why Persian still says سوگند خوردن 'to eat/drink an oath'. Nourai's NOTE says just this, and it is exactly Mo'in's footnote at BQT 1190: '... اورا معلوم می\\u200cکردند. استعمال فعل \\u00abخوردن\\u00bb با سوگند یادگار همین مفهوم است.' Wiktionary gives the same derivation ('From Middle Persian swknd (s\\u014dgand), from Avestan saokanta \\u201csulphur\\u201d, from PIE *\\u1e31ewk-').\",\n    \"derivation_fa\": \"\\u00abسوگند\\u00bb از فارسی میانهٔ s\\u014dgand [swknd] (فارسی میانهٔ مانوی swgnd، پازند sawagand؛ نیبرگ ۳۴۶۰، مکنزی ص ۷۸) و آن از ایرانی باستان *saukanta- «گوگرد» یعنی همان saok\\u0259nta- اوستایی است. دگرگونی آوایی قاعده\\u200cمند است: nt اوستایی پس از واکهٔ بلند در فارسی میانه به nd نرم می\\u200cشود و sao- به s\\u014d- و سپس saw-/so- بدل می\\u200cگردد. از نظر معنایی، واژه یادگار «وَرِ گوگرد» است: متهم آبِ آمیخته به گوگرد می\\u200cنوشید و از واکنش تنش دربارهٔ راستگویی\\u200cاش داوری می\\u200cکردند؛ به همین سبب هنوز می\\u200cگوییم «سوگند خوردن». یادداشت نورایی درست است و عیناً همان چیزی است که معین در حاشیهٔ برهان قاطع (ص ۱۱۹۰) نوشته است. ادعای نورایی درست است.\",\n    \"sources\": [W_SOGAND],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1190\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Q\\u0101te\\u02bf p.1190 (BQT_v2_pages.txt leaf 654; fixed by its own catch-lines 'بقیه در صفحهٔ ۱۱۹۱' / 'بقیه از صفحهٔ ۱۱۸۹'): the س\\u0648گند footnote describes the sulphur ordeal \\u2014 '... شدن آن از شکم با ماندن آب در شکم تقصیر وی ... اورا معلوم می\\u200cکردند. استعمال فعل \\u00abخوردن\\u00bb با سوگند یادگار همین مفهوم است' \\u2014 i.e. the source of Nourai's NOTE.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.78 and Engl.-Pahl. p.114\", \"stance\": \"supports\",\n       \"note\": \"'s\\u014dgand [swknd | M swgnd, N s\\u014dgand] oath'; 'swear (oath) sogand xwardan'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual II no. 3460\", \"stance\": \"supports\",\n       \"note\": \"'s\\u014dkand [swknd] oath; ~ x\\u0342artan to swear an oath ... Ps. swkndy; MPrs swgnd; Paz. sawagand (SGV); NP saugand.'\"},\n      {\"src\": \"HRN\", \"where\": \"no. 757, p.167\", \"stance\": \"supports\",\n       \"note\": \"'s\\u014dgend \\u201aEid\\u2018. aw. saok\\u0259nta-vant- \\u201aSchwefel enthaltend\\u2018.'\"},\n      {\"src\": \"BQT\", \"where\": \"p.1190, Mo'in's footnote\", \"stance\": \"supports\",\n       \"note\": \"Gives the ordeal explanation quoted above.\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"Sogdian\",\n    \"words\": \"swgnd, swk`nt\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Both forms are real Sogdian and both mean 'oath': Gharib's Sogdian Dictionary has no. 9044 'so\\u0263and \\u00a9<Av. saok\\u0259nta = *sw\\u0263nt xwr-, swk\\u02bcnt \\u2014 oath \\u2014 BBB p97 b47; GMS 250' and no. 9053 'sokand \\u00a9Av. saok\\u0259nta-, Khwar. sknt = *sw\\u0263nt xwr-, sw\\u0263nd \\u2014 oath', with references to the Buddhist, Manichaean and Christian Sogdian corpora (C2 23R24, 69R15-16; TSP 3.220; Schwartz, StIr Cahier 7, 293-5). swk\\u02bcnt is the Buddhist/Sogdian-script spelling of the same word whose Manichaean spelling is sw\\u0263nd, the \\u0263 being the lenited voiced continuant of intervocalic k. One correction to the arrow: Sogdian does not descend from Avestan \\u2014 Sogdian s\\u014dkand and Avestan saok\\u0259nta- are parallel Old Iranian inheritances of *saukanta-, and Sogdian preserves the older -nt-. The Sogdian idiom swk\\u02bcnt xwr- 'to eat an oath' matches MMP swgnd xwrdn and NP sogand xordan (Cheung 2007: 340, after Schwartz 1989).\",\n    \"derivation_fa\": \"هر دو صورت سغدی راست است و هر دو «سوگند» معنی می\\u200cدهد: در فرهنگ سغدی قریب مدخل ۹۰۴۴ so\\u0263and و مدخل ۹۰۵۳ sokand [swk\\u02bcnt] هر دو با ارجاع «\\u00a9 اوستایی saok\\u0259nta-» و با شاهد از متن\\u200cهای بودایی، مانوی و مسیحی سغدی آمده\\u200cاند. swk\\u02bcnt نگارش سغدیِ خط بودایی و sw\\u0263nd نگارش مانوی همان واژه است (\\u0263 صورت نرم\\u200cشدهٔ k میان دو واکه). یک نکتهٔ اصلاحی: سغدی از اوستایی نمی\\u200cآید؛ sokand سغدی و saok\\u0259nta- اوستایی هر دو بازماندهٔ مستقلِ ایرانی باستان *saukanta- هستند و سغدی خوشهٔ nt کهن را نگاه داشته است. ترکیب سغدی swk\\u02bcnt xwr- «سوگند خوردن» دقیقاً با فارسی میانهٔ swgnd xwrdn و فارسی نو برابر است.\",\n    \"sources\": [W_SOGAND],\n    \"ref_check\": [\n      {\"ref\": \"SOD:365\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 432 (printed \\u2248 leaf \\u2212 66 = 366, i.e. Nourai's p.365 \\u00b11) carries both entries: 'so\\u0263and \\u00a9<Av. saok\\u0259nta =*sw\\u0263nt xwr-, swk\\u02bcnt / oath / BBB p97 b47; GMS 250' (no. 9044) and 'sokand \\u00a9Av. saok\\u0259nta-, Khwar. sknt =*sw\\u0263nt xwr-, sw\\u0263nd / oath' (no. 9053).\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"p. 340\", \"stance\": \"supports\",\n       \"note\": \"'On the Iranian expression for \\u201cto swear, take an oath\\u201d, as in Sogd. swk\\u02bcnt xwr-, MMP swgnd xwrdn, NP saugand xurdan, Kurd. sont xarin, etc., see Schwartz 1989: 293 ff.'\"},\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1551\", \"stance\": \"partial\",\n       \"note\": \"Gives the Avestan saok\\u0259nta-vant- that Gharib refers the Sogdian word to, but of course says nothing about Sogdian.\"}\n    ]\n   },\n   {\n    \"id\": 6, \"lang\": \"Greek\",\n    \"words\": \"kuknos\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Greek \\u03ba\\u03cd\\u03ba\\u03bd\\u03bf\\u03c2 k\\u00fdknos means 'swan' (Homer+); 'white' is not a meaning of the word but the etymological sense Pokorny assigns to it. Pokorny 597 closes the keuk- article with 'gr. \\u03ba\\u03cd\\u03ba\\u03bd\\u03bf\\u03c2 \\u201aSchwan\\u2018 als \\u201ader Wei\\u00dfe\\u2018', and Watkins/AHD formalises it as a suffixed zero-grade *kuk-no- \\u2014 so Nourai's arrow is exactly his source's. Modern opinion is more reserved: Klein derives \\u03ba\\u03cd\\u03ba\\u03bd\\u03bf\\u03c2 not from *keuk- at all but calls it 'prob. of imitative origin. Cp. Russ. kyk\\u00fa \\u201aswan\\u2019s cry\\u2019', Beekes (quoted by Etymonline) says the word 'has been the subject of \\u201cabundant discussion\\u201d', and Wiktionary hedges: 'Perhaps from PIE *\\u1e31ewk- \\u201awhite\\u2018 ... Could also be onomatopoeic'. The formation *kuk-no- with -no- suffix is unobjectionable, but there is no Greek verb or adjective of the *keuk- family beside it, which is why the onomatopoeic account keeps its adherents.\",\n    \"derivation_fa\": \"واژهٔ یونانی k\\u00fdknos تنها به معنی «قو» است (از هومر به بعد)؛ معنی «سپید» معنیِ ریشه\\u200cشناختی\\u200cای است که پوکورنی به آن نسبت داده، نه معنی واژه. پوکورنی در پایان مدخل keuk- (ص ۵۹۷) می\\u200cنویسد «یونانی k\\u00fdknos \\u201aقو\\u2018 یعنی \\u201aسپید\\u2018» و واتکینز آن را صورت پسوندیِ درجهٔ صفر *kuk-no- می\\u200cداند؛ پس نمودار نورایی دقیقاً برگرفته از منبع خودِ اوست. اما دیدگاه امروزی محتاط\\u200cتر است: کلاین آن را برخاسته از تقلید آوایی (بانگ قو) می\\u200cداند و بیکس آن را واژه\\u200cای پر\\u200cبحث و بی\\u200cریشهٔ روشن می\\u200cشمارد؛ ویکی\\u200cواژه هر دو احتمال را در کنار هم می\\u200cآورد. ساخت *kuk-no- ایرادی ندارد، ولی چون در یونانی هیچ فعل یا صفت هم\\u200cخانوادهٔ *keuk- در کنار آن نیست، تبیین آوا\\u200cبنیاد همچنان طرفدار دارد. پس این بند «با احتیاط پذیرفتنی» است.\",\n    \"sources\": [W_KUK, E_CYG],\n    \"ref_check\": [\n      {\"ref\": \"POK:597\", \"status\": \"supports\",\n       \"note\": \"Printed p.597, last line of the keuk- article: 'gr. \\u03ba\\u03c5\\u03ba\\u03bd\\u03bf\\u03c2 \\u201aSchwan\\u2018 als \\u201ader Wei\\u00dfe\\u2018. WP. I 378. Erweiterung von 2. keu-.'\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins, s.v. keuk-\", \"stance\": \"supports\",\n       \"note\": \"'Suffixed zero-grade form *kuk-no- in Greek kuknos, swan: CYGNET, CYGNUS.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. cygnet\", \"stance\": \"contradicts\",\n       \"note\": \"'... fr. Gk. \\u03ba\\u03cd\\u03ba\\u03bd\\u03bf\\u03c2, \\u201aswan\\u2019, which is prob. of imitative origin. Cp. Russ. kyk\\u00fa, \\u201aswan\\u2019s cry\\u2019.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 378\", \"stance\": \"silent\",\n       \"note\": \"The keuq- article as OCRed on leaf 386 lists the Indo-Iranian material; the Greek swan is not visible in the surviving text of that page.\"}\n    ]\n   },\n   {\n    \"id\": 7, \"lang\": \"English\",\n    \"words\": \"cygnet\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"English cygnet 'young swan' is first attested c.1400 (also spelt signet before the 17th c.); it is Anglo-French cignet (mid-14c.) / Anglo-Latin cygnettus, a diminutive in -et of Old French cigne, cisne 'swan' (12c., ModFr. cygne), which was refashioned after Latin cygnus (a spelling variant of classical cycnus) from Vulgar Latin cicinus (attested in the Lex Salica) \\u2014 hence Spanish and Portuguese cisne. Latin cycnus is itself the Greek loanword \\u03ba\\u03cd\\u03ba\\u03bd\\u03bf\\u03c2. The chart's arrow Greek \\u2192 English is therefore right in substance but skips two obligatory stages, Latin and (Anglo-)French, and the English word is a French diminutive formation, not a borrowing of the Greek word as such. The node carries no reference of its own in the book. Watkins/AHD lists CYGNET under keuk-.\",\n    \"derivation_fa\": \"واژهٔ انگلیسی cygnet «قوی جوان» از حدود ۱۴۰۰ م. گواهی شده است و وام\\u200cواژه\\u200cای است از انگلیسی-فرانسویِ cignet (میانهٔ سدهٔ ۱۴)، صورت تصغیر با پسوند -et از فرانسویِ کهن cigne/cisne «قو» (فرانسوی امروز cygne)، که خود به\\u200cپیروی از لاتینی cygnus (گونهٔ نوشتاری cycnus) بازآرایی شده و از لاتینی عامیانهٔ cicinus می\\u200cآید؛ و cycnus لاتینی وام\\u200cگیری از k\\u00fdknos یونانی است. پس پیکان «یونانی \\u2190 انگلیسی» در نمودار از نظر محتوا درست است، ولی دو حلقهٔ ضروری (لاتینی و فرانسوی) را نادیده می\\u200cگیرد و در واقع واژهٔ انگلیسی ساختی تصغیریِ فرانسوی است نه وام مستقیم از یونانی. این بند پذیرفتنی است.\",\n    \"sources\": [E_CYG, W_KUK],\n    \"ref_check\": [\n      {\"ref\": \"(none cited in the book)\", \"status\": \"not_checked\",\n       \"note\": \"The node carries refs=None; the claim is nevertheless covered by Nourai's root reference POK:597 and by AHD s.v. keuk- ('CYGNET, CYGNUS').\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966/1971, s.v. cygnet\", \"stance\": \"supports\",\n       \"note\": \"'cygnet, n., a young swan. \\u2014 Dimin. of F. cygne, \\u201aswan\\u2019 (refashioned after L. cygnus, a variant of cycnus), fr. OF. cisne, fr. VL. cicinus (which occurs in the Salic law), fr. L. cycnus, fr. Gk. \\u03ba\\u03cd\\u03ba\\u03bd\\u03bf\\u03c2.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. CYGNET\", \"stance\": \"supports\",\n       \"note\": \"OCR is damaged but legible in outline: 'cygnet, a young swan (F. \\u2212 L.) ... of O.F. cisne, a swan ... that O.F. word is not from L. [cycnus] ... but the oldest O.F. form was cisne, from Low L. cicinus.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins, s.v. keuk- and index\", \"stance\": \"supports\",\n       \"note\": \"'CYGNET keuk- / CYGNUS keuk-'.\"}\n    ]\n   }\n  ]\n },\n\n # ------------------------------------------------------------------ entry 3\n {\n  \"entry\": 3,\n  \"root\": \"Kh\\u00e2\\u010d, X\\u00e2\\u010d 2\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Old/Middle Armenian \\u056d\\u0561\\u0579 xa\\u010d\\u02bf 'cross, crucifix'\",\n  \"note\": \"The root box is right as a statement about where Persian خاج comes from: Old Armenian \\u056d\\u0561\\u0579 (xa\\u010d\\u02bf) 'crucifix, cross' is a well attested Armenian word, continued by Middle and Modern Armenian, and Mo'in tags the Persian word simply '[ارمن.]'. What the box does not say \\u2014 and need not \\u2014 is that the Armenian word's own origin is unsettled: Lid\\u00e9n connected it with Persian خاده x\\u0101da 'pole, stake', Lith. k\\u00f3tas, Latv. k\\u0101ts and derived them all from PIE (so the original sense would be 'stake, upright pile', typologically like Gk \\u03c3\\u03c4\\u03b1\\u03c5\\u03c1\\u03cc\\u03c2, Goth. galga, Parth. d\\u0101r); A\\u010da\\u1e5b\\u0435an accepts this and adds Arm. \\u056d\\u0578\\u0579 xo\\u010d\\u02bf and \\u056d\\u0565\\u0579 xe\\u010d\\u02bf as ablaut grades, while Olsen rejects it on phonetic grounds. Nourai's numbering 'X\\u00e2\\u010d 2' distinguishes it from a homograph elsewhere in the book.\",\n  \"note_fa\": \"این ریشه\\u200cجعبه به\\u200cعنوان بیانِ خاستگاه واژهٔ فارسی «خاج» درست است: \\u056d\\u0561\\u0579 (xa\\u010d\\u02bf) در ارمنی کهن به معنی «صلیب، چلیپا» واژه\\u200cای گواهیده و پرکاربرد است و در ارمنی میانه و امروزی نیز مانده است؛ معین هم در فرهنگ فارسی برای «خاج» تنها برچسب [ارمن.] گذاشته است. آنچه در جعبه نیامده (و نیازی هم نبوده) این است که خاستگاه خودِ واژهٔ ارمنی روشن نیست: لیدن آن را با «خادهٔ» فارسی (چوب، تیرک) و kótas لیتوانیایی سنجیده و همه را از هندواروپایی گرفته است \\u2014 در این صورت معنی نخستین آن «تیرک، چوبِ برافراشته» بوده \\u2014 و آچاریان این را پذیرفته، اما اولسن آن را از نظر آوایی رد می\\u200cکند. شمارهٔ «۲» در نام ریشه برای جدا کردن آن از هم\\u200cنگاشتِ دیگری در همین کتاب است. ادعای نورایی درست است.\",\n  \"sources\": [W_XACH, W_KHAJ, VY_KHAJ, AB_KHAJ],\n  \"ref_check\": [\n    {\"ref\": \"MON:1384\", \"status\": \"supports\",\n     \"note\": \"Mo'in, Farhang-e F\\u0101rsi s.v. خاج (read through vajehyab.com/moein and abadis.ir, both archived): '[ارمن.] (اِ.) ۱ - صلیب، چلیپا. ۲ - یکی از خال\\u200cهای ورق، گشنیز.' \\u2014 the Armenian tag and both senses Nourai gives.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.227\", \"stance\": \"supports\",\n     \"note\": \"'Np. x\\u0101j \\u201aKreuz\\u2018 aus \\u00e4lterem *x\\u0101\\u010d = arm. xa\\u010d \\u201aKreuz\\u2018 ist arm. LW.' (HUB.txt leaf 238; leaf = printed + 11)\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Q\\u0101te\\u02bf p.696, Mo'in's footnote 3\", \"stance\": \"supports\",\n     \"note\": \"'خاج \\u2014 بر وزن تاج، بمعنی چلیپا باشد که صلیب نصاری است'; footnote: 'از کلمهٔ قدیم خاج ... از ارمنی (صلیب)، هوبشمان ص ۲۲۷' \\u2014 Mo'in's own note points at exactly Nourai's HUB:227.\"},\n    {\"src\": \"MON\", \"where\": \"vajehyab / abadis, s.v. خاج\", \"stance\": \"supports\",\n     \"note\": \"'[ارمن.] (اِ.) ۱ - صلیب، چلیپا. ۲ - یکی از خال\\u200cهای ورق، گشنیز.'\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Persian\",\n    \"words\": \"x\\u00e2j \\u00abخاج\\u00bb\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"NP خاج x\\u0101j 'cross' (also خاچ x\\u0101\\u010d) is a loan from Armenian xa\\u010d\\u02bf, taken over as *x\\u0101\\u010d and then subject to the Persian voicing of post-vocalic \\u010d to j that H\\u00fcbschmann discusses in the same paragraph (\\u00a7\\u00a7116-117 of Persische Studien, where x\\u0101j stands beside n\\u014dj/n\\u014dz 'pine' = Arm. no\\u010d\\u02bf and am\\u0101j = Arm. ma\\u010d). H\\u00fcbschmann p.227 states it in one line: 'Np. x\\u0101j \\u201aKreuz\\u2018 aus \\u00e4lterem *x\\u0101\\u010d = arm. xa\\u010d \\u201aKreuz\\u2018 ist arm. LW.' Wiktionary agrees, specifying the intermediary: 'Borrowed from Middle Armenian \\u056d\\u0561\\u0579 (xa\\u010d\\u02bf, \\u201ccross\\u201d), from Old Armenian \\u056d\\u0561\\u0579', with eight references including H\\u00fcbschmann 1895:227, Horn's Grundriss der iranischen Philologie I/2:8 and Asatryan 1990. The card-suit sense that Nourai adds is genuine and secondary: the trefoil of the French clubs suit was read in Persian as a little cross, so Mo'in glosses '۲ - یکی از خال\\u200cهای ورق، گشنیز' and Wiktionary lists '(card games) club (\\u2663)' first. Borhan-e Q\\u0101te\\u02bf p.696 also records the further sense 'lobe of the ear' (نرمهٔ گوش), which is a separate word.\",\n    \"derivation_fa\": \"\\u00abخاج\\u00bb (و گونهٔ \\u00abخاچ\\u00bb) وام\\u200cواژه\\u200cای است از ارمنی xa\\u010d\\u02bf «صلیب»؛ نخست به\\u200cصورت *x\\u0101\\u010d وارد فارسی شده و سپس \\u010d پایانی پس از واکه \\u2014 بنا بر همان قاعده\\u200cای که هوبشمان در بندهای ۱۱۶ و ۱۱۷ «مطالعات فارسی» می\\u200cآورد (مانند n\\u014dj/n\\u014dz در برابر no\\u010d\\u02bf ارمنی) \\u2014 به j بدل شده است. هوبشمان در ص ۲۲۷ به یک جمله می\\u200cنویسد: «فارسی نو x\\u0101j \\u201aصلیب\\u2018 از صورت کهن\\u200cتر *x\\u0101\\u010d = ارمنی xa\\u010d \\u201aصلیب\\u2018؛ وام\\u200cواژهٔ ارمنی است.» ویکی\\u200cواژه نیز همین را می\\u200cگوید و واسطه را ارمنی میانه می\\u200cداند. معنی دومی که نورایی افزوده (خالِ گشنیزِ ورق) نیز راست و ثانوی است: نقشِ سه\\u200cبرگِ گشنیز در فارسی «خاج» یعنی صلیب کوچک خوانده شده است؛ معین هم آن را ثبت کرده است. ادعای نورایی درست است.\",\n    \"sources\": [W_KHAJ, VY_KHAJ, AB_KHAJ, W_XACH],\n    \"ref_check\": [\n      {\"ref\": \"HUB:227\", \"status\": \"supports\",\n       \"note\": \"'Np. x\\u0101j \\u201aKreuz\\u2018 aus \\u00e4lterem *x\\u0101\\u010d = arm. xa\\u010d \\u201aKreuz\\u2018 ist arm. LW.' \\u2014 verbatim, HUB.txt leaf 238 (printed p.227).\"},\n      {\"ref\": \"BQT:696\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 154 (printed 696, offset checked against the catch-lines at leaves 187/244): headword 'خاج \\u2014 بر وزن تاج، بمعنی چلیپا باشد که صلیب نصاری است و آن باین شکل بود'; Mo'in's footnote 3: 'از کلمهٔ قدیم خاج ... از ارمنی (صلیب)، هوبشمان ص ۲۲۷'; the same page carries the Kam\\u0101l Esm\\u0101\\u02bf\\u012bl verse Nourai quotes.\"},\n      {\"ref\": \"MON:1384\", \"status\": \"supports\",\n       \"note\": \"Mo'in s.v. خاج: '[ارمن.] (اِ.) ۱ - صلیب، چلیپا. ۲ - یکی از خال\\u200cهای ورق، گشنیز.'\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"p.696 and Mo'in's footnote\", \"stance\": \"supports\",\n       \"note\": \"See ref_check; Borhan also gives the homonym 'نرمهٔ گوش'.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/خاج and abadis.ir s.v. خاج\", \"stance\": \"supports\",\n       \"note\": \"'خاج. (ارمنی، اِ) بر وزن تاج بمعنی چلیپا باشد که صلیب نصاری است. (برهان) (آنندراج) (جهانگیری)' (Dehkhoda quoting Borhan) and Mo'in '[ارمن.] ... ۲ - یکی از خال\\u200cهای ورق، گشنیز'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.227, \\u00a7\\u00a7116-117\", \"stance\": \"supports\",\n       \"note\": \"Places x\\u0101j among the Armenian loans whose \\u010d became j in Persian, beside n\\u014dj 'pine' = arm. no\\u010d and am\\u0101j.\"}\n    ]\n   }\n  ]\n },\n\n # ------------------------------------------------------------------ entry 4\n {\n  \"entry\": 4,\n  \"root\": \"Kh\\u00e2d, Qh\\u00e2d\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Indo-Iranian *kh\\u0101d- 'to chew, bite' (Walde-Pokorny's qhad-); PIE status contested\",\n  \"note\": \"Nourai's double name 'Kh\\u00e2d, Qh\\u00e2d' comes straight from his two references: Walde-Pokorny I 341 sets up a root 'qhad- \\u201abei\\u00dfen\\u2018' with precisely his material \\u2014 'Ai. kh\\u0101dati \\u201azerbei\\u00dft, kaut, i\\u00dft\\u2018, kh\\u0101dan m. \\u201aZahn\\u2018, npers. x\\u0101y\\u012bdan \\u201aessen, kauen\\u2018 (H\\u00fcbschmann ZDMG. 38, 423, Horn Np. Et. 104, Uhlenbeck), arm. xacanem \\u201abei\\u00dfe\\u2018' \\u2014 and it even cites Horn p.104, which is Nourai's reference on the Avestan node. But his other reference, POK:634, is the place where Pokorny withdrew the root: footnote 1 on that page reads 'Die bei WP. I 341, 348 f., 399 angef\\u00fchrten Wurzeln kh\\u0101d- \\u201abei\\u00dfen\\u2018, khabh- : khobh-, khen- sind nicht als idg. zu erweisen ... Ai. kh\\u0101dati \\u201azerbei\\u00dft, kaut\\u2018, npers. x\\u0101yad ds., k\\u00f6nnte zu arm. xacanem \\u201abei\\u00dfe\\u2018 geh\\u00f6ren, aber auch mit sekund\\u00e4rer expressiver Aspiration als *k\\u021dnd- zu lit. kand\\u00f9 \\u201abei\\u00dfe\\u2018'. So the two references Nourai stacks contradict each other, and the label 'Indo-European' is the one his own POK:634 denies. Modern opinion is split rather than settled: Cheung (2007: 445) says 'An IE provenance for this Ir. root is uncertain', LIV assigns Skt kh\\u0101d to *k\\u02b7eh\\u2082d- 'to squeeze out' (which Cheung finds 'semantically unlikely'), while Wiktionary, following Derksen, does give a PIE preform but a quite different one \\u2014 *k(\\u02b7)end- or *k(\\u02b7)enHd(\\u02b0)- (the nasal shape Pokorny mentioned as the alternative). Verdict: the etymon 'to chew' is real and Indo-Iranian at least; its IE status and shape are contested, so 'plausible' rather than 'confirmed'.\",\n  \"note_fa\": \"نام دوگانهٔ «Kh\\u00e2d, Qh\\u00e2d» یکسره از دو ارجاع خودِ نورایی می\\u200cآید: والده-پوکورنی (ج ۱، ص ۳۴۱) ریشه\\u200cای با صورت qhad- «گاز گرفتن» می\\u200cسازد و دقیقاً همین مواد را می\\u200cآورد: «سنسکریت kh\\u0101dati \\u201aمی\\u200cجَوَد، می\\u200cخورد\\u2018، فارسی نو x\\u0101y\\u012bdan \\u201aخوردن، جویدن\\u2018 (هوبشمان؛ هرن، ریشه\\u200cشناسی فارسی نو، ص ۱۰۴)، ارمنی xacanem \\u201aمی\\u200cگزم\\u2018». اما ارجاع دیگرِ او، پوکورنی ص ۶۳۴، همان جایی است که پوکورنی این ریشه را پس می\\u200cگیرد: در پانوشت همان صفحه می\\u200cنویسد ریشه\\u200cهای kh\\u0101d- «گاز گرفتن» و مانند آن «هندواروپایی بودنشان اثبات\\u200cپذیر نیست» و می\\u200cافزاید kh\\u0101dati سنسکریت و x\\u0101yad فارسی شاید به xacanem ارمنی مربوط باشند یا با «دمیدگیِ ثانوی» به kand\\u00f9 لیتوانیایی. پس دو ارجاعِ نورایی یکدیگر را نقض می\\u200cکنند و برچسب «هندواروپایی» همان است که منبع خودش رد کرده است. پژوهش امروزی نیز یکدست نیست: چونگ (۲۰۰۷، ص ۴۴۵) خاستگاه هندواروپایی این ستاک ایرانی را نامسلم می\\u200cداند و ویکی\\u200cواژه به پیروی از درکسن صورت هندواروپاییِ دیگری (*k(\\u02b7)enHd-) بازسازی می\\u200cکند. در مجموع: خودِ ریشه (به معنی «جویدن») دست\\u200cکم هندوایرانی است، ولی هندواروپایی\\u200cبودن و صورت آن محل اختلاف است \\u2014 با احتیاط پذیرفتنی.\",\n  \"sources\": [W_XAY],\n  \"ref_check\": [\n    {\"ref\": \"POK:634\", \"status\": \"contradicts\",\n     \"note\": \"POK_02.txt leaf 294 (printed 634), footnote: 'Die bei WP. I 341, 348 f., 399 angef\\u00fchrten Wurzeln kh\\u0101d- \\u201abei\\u00dfen\\u2018, khabh- : khobh- \\u201akraftlos\\u2018, khen- \\u201agraben\\u2018 sind nicht als idg. zu erweisen' \\u2014 i.e. Pokorny's page 634 explicitly denies the Indo-European status Nourai's root box asserts.\"},\n    {\"ref\": \"WLD1:341\", \"status\": \"supports\",\n     \"note\": \"WLD_Bd1_pages.txt leaf 349 (printed 341): 'qhad- \\u201abei\\u00dfen\\u2018. Ai. kh\\u0101dati \\u201azerbei\\u00dft, kaut, i\\u00dft\\u2018, kh\\u0101dan m. \\u201aZahn\\u2018, npers. x\\u0101y\\u012bdan \\u201aessen, kauen\\u2018 (H\\u00fcbschmann ZDMG. 38, 423, Horn Np. Et. 104, Uhlenbeck Ai. Wb. 75), arm. xacanem \\u201abei\\u00dfe, pungo\\u2018'. This is the source of Nourai's 'Qh\\u00e2d' and of the whole chart.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.634 n.1 (and p.630 ff. context)\", \"stance\": \"contradicts\",\n     \"note\": \"See ref_check: the root is listed only to be rejected, with the alternatives arm. xacanem or lit. kand\\u00f9.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 341\", \"stance\": \"supports\",\n     \"note\": \"Sets up qhad- 'bei\\u00dfen' with Skt, NP and Armenian.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p. 445 s.v. *x\\u0101d\", \"stance\": \"partial\",\n     \"note\": \"'An IE provenance for this Ir. root is uncertain: the IE preform *k\\u02b7H\\u2081ed- (cf. Arm. xacanel \\u201cto bite\\u201d) reconstructed by Klingenschmitt 1982: 210 and K\\u00fcmmel, LIV: 360 has little to recommend.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots\", \"stance\": \"silent\",\n     \"note\": \"No root kh\\u0101d-/qhad- 'to bite' in the appendix (grep 'khad', 'qhad' in AHD_watkins1985.txt: nothing).\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Sanskrit\",\n    \"words\": \"x\\u00e2d\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Sanskrit \\u0916\\u093e\\u0926\\u094d kh\\u0101d-, 3sg. kh\\u0101dati 'chews, bites to pieces, eats' is attested from the Rigveda onward (EWAia I 451), with the agent noun kh\\u0101dana- and, per Walde-Pokorny, kh\\u0101dan- m. 'tooth'. Nourai's spelling 'x\\u00e2d' is simply his own transliteration convention, in which x stands for the aspirate kh; the word and gloss are correct. It is the anchor of the whole chart: every source in the file \\u2014 WP I 341, Pokorny 634, Horn 104, Bartholomae AiW 531, Cheung 445 \\u2014 starts from Skt kh\\u0101dati and adds the New Persian verb to it.\",\n    \"derivation_fa\": \"\\u0641عل سنسکریت kh\\u0101d- (سوم\\u200cشخص kh\\u0101dati) «می\\u200cجَود، گاز می\\u200cگیرد، می\\u200cخورد» از ریگ\\u200cودا به بعد گواهیده است و صورت\\u200cهای مشتقی مانند kh\\u0101dana- دارد؛ والده-پوکورنی kh\\u0101dan- «دندان» را نیز به آن می\\u200cافزاید. نگارش «x\\u00e2d» در نمودار تنها شیوهٔ آوانگاری خودِ نورایی است که در آن x برابر kh دمیده است؛ واژه و معنی هر دو درست\\u200cاند. این واژه لنگرگاه کل نمودار است: همهٔ منابع (والده-پوکورنی ج۱ ص۳۴۱، پوکورنی ص۶۳۴، هرن ص۱۰۴، بارتولومه ستون ۵۳۱، چونگ ص۴۴۵) از kh\\u0101dati آغاز می\\u200cکنند و فعل فارسی را به آن می\\u200cپیوندند. ادعای نورایی درست است.\",\n    \"sources\": [W_XAY],\n    \"ref_check\": [\n      {\"ref\": \"POK:634\", \"status\": \"partial\",\n       \"note\": \"Pokorny p.634 n.1 does cite the word \\u2014 'Ai. kh\\u0101dati \\u201azerbei\\u00dft, kaut\\u2018, npers. x\\u0101yad ds.' \\u2014 so the Sanskrit form and gloss are supported there, but only inside the note that denies the root Indo-European status.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 341\", \"stance\": \"supports\",\n       \"note\": \"'Ai. kh\\u0101dati \\u201azerbei\\u00dft, kaut, i\\u00dft\\u2018, kh\\u0101dan m. \\u201aZahn\\u2018.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 445\", \"stance\": \"supports\",\n       \"note\": \"'*SANSKRIT: kh\\u0101d \\u201cto chew, to bite, to eat\\u201d (RV+) ... EWAia I: 451', and Cheung insists it belongs with the Iranian forms: 'I find the separation of Skt. kh\\u0101d ... from the Ir. forms incomprehensible.'\"},\n      {\"src\": \"BRT\", \"where\": \"AiW col. 531\", \"stance\": \"supports\",\n       \"note\": \"Under Av. xad-: 'Vgl. ai. kh\\u0101dati, np. x\\u0101yad \\u201aer kaut\\u2018.'\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Avestan\",\n    \"words\": \"xad 1\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"There is an Avestan xad-, but it is not the ancestor of the Persian 'chew' verb. Bartholomae (AiW col. 531) records 'j. xad- V., nur mit vi \\u201aauseinander quetschen\\u2018. Praes. 2 xa\\u03b4a-', attested only in Vendidad 2.31-32 (v\\u012bxa\\u03b4a, v\\u012bxa\\u03b4at, of pressing/breaking the earth apart with the heel), and it is Bartholomae himself who adds the comparison Nourai relies on: 'Vgl. ai. kh\\u0101dati, np. x\\u0101yad \\u201aer kaut\\u2018.' That 1904 comparison is what modern Iranian etymology has undone. Cheung (2007: 439) puts YAv. vixa\\u03b4- under a root *xad 'to beat, strike, inflict a wound, hurt' (with Parth. xd- 'to injure', Khot. khad- 'to wound', MP xast 'wounded', NP xastan 'to wound') and states flatly: 'This root should be separated from Skt. kh\\u0101d \\u201cto eat, chew\\u201d, which rather corresponds to an Ir. root *x\\u0101d (q.v.)'. Neither Horn 104 (Nourai's own reference for this node) nor Walde-Pokorny I 341 cites any Avestan form at all \\u2014 both go straight from Sanskrit to New Persian. The node also carries no gloss in the book, which is symptomatic: the form was inserted to bridge Sanskrit and Persian rather than because a suitable Avestan word was found.\",\n    \"derivation_fa\": \"در اوستا فعلی به\\u200cصورت xad- هست، اما نیای فعل فارسیِ «جویدن» نیست. بارتولومه (ستون ۵۳۱) می\\u200cنویسد: «اوستایی نو xad-، تنها با پیشوند vi، \\u201aاز هم فشردن/شکافتن\\u2018؛ ستاک حال xa\\u03b4a-»، که تنها در وندیداد ۲.۳۱-۳۲ گواه دارد؛ و همو در همان\\u200cجا سنجهٔ مورد اتکای نورایی را می\\u200cافزاید: «قس سنسکریت kh\\u0101dati، فارسی نو x\\u0101yad \\u201aمی\\u200cجود\\u2018». همین سنجهٔ ۱۹۰۴ است که ایران\\u200cشناسی امروزی کنارش گذاشته است: چونگ (۲۰۰۷، ص ۴۳۹) v\\u012bxa\\u03b4- اوستایی را ذیل ستاک *xad «زدن، زخم زدن» می\\u200cآورد (با پارتی xd-، ختنی khad-، فارسی میانه xast «زخمی»، فارسی نو «خستن») و صریح می\\u200cگوید: «این ریشه باید از kh\\u0101d سنسکریت \\u201aخوردن، جویدن\\u2018 جدا شود که در ایرانی با *x\\u0101d برابر است». افزون بر این، نه هرن (ص ۱۰۴، همان ارجاع خودِ نورایی) و نه والده-پوکورنی هیچ صورت اوستایی\\u200cای نمی\\u200cآورند و مستقیم از سنسکریت به فارسی نو می\\u200cروند. اینکه این گره در کتاب حتی معنی هم ندارد نشانه\\u200cٔ همین است. پژوهش امروزی این حلقه را رد می\\u200cکند.\",\n    \"sources\": [W_XAY],\n    \"ref_check\": [\n      {\"ref\": \"HRN:104\", \"status\": \"partial\",\n       \"note\": \"Horn's entry no. 469 (printed p.104; the OCR of HRN.txt leaf 126 has lost the entry body, but both of Horn's indexes point to it \\u2014 the Sanskrit index line '\\u221akh\\u0101d-, kh\\u0101dati 469' and the New Persian index line for the verb, and Walde-Pokorny I 341 cites 'Horn Np. Et. 104' for exactly npers. x\\u0101y\\u012bdan). Horn's chain there is Skt kh\\u0101dati \\u2192 NP x\\u0101y\\u012bdan with no Avestan link, so the reference supports the Persian word but not the Avestan node.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 531 s.v. xad-\", \"stance\": \"partial\",\n       \"note\": \"'j. xad- V., nur mit vi \\u201aauseinander quetschen\\u2018. Praes. 2 xa\\u03b4a-. ai\\u0303hh\\u0101 zim\\u014d p\\u0101\\u0161naibya v\\u012bspara ar\\u0259\\u0161t\\u0101ibya v\\u012bxa\\u03b4a V.2.31; 32 ... Vgl. ai. kh\\u0101dati, np. x\\u0101yad \\u201aer kaut\\u2018.' The word exists and Bartholomae does make Nourai's comparison, but glosses it 'squeeze apart', not 'bite/chew'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 439 s.v. *xad 'to beat, strike, inflict a wound, hurt'\", \"stance\": \"contradicts\",\n       \"note\": \"'*AVESTAN: (+ *ui-) ? YAv. vixa\\u00f6- \\u201cto beat (the earth) apart\\u201d (not \\u201aauseinander quetschen\\u2018 ?, AIW: 531) ... This root should be separated from Skt. kh\\u0101d \\u201cto eat, chew\\u201d, which rather corresponds to an Ir. root *x\\u0101d (q.v.).'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 341\", \"stance\": \"silent\",\n       \"note\": \"The qhad- article lists Sanskrit, New Persian and Armenian only \\u2014 no Avestan form.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Persian\",\n    \"words\": \"x\\u00e2y\\u00eedan \\u00abخاییدن ( خای )\\u00bb\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"The Persian verb itself is beyond doubt: خاییدن x\\u0101y\\u012bdan, present stem خای x\\u0101y-, 'to chew, grind with the teeth', in Borhan-e Q\\u0101te\\u02bf p.712 'خاییدن \\u2014 بر وزن ساییدن، بمعنی بدندان نرم کردن و جاویدن باشد', with the participle خاییده and the 3sg خاید on the same page, and with the Ferdowsi line Nourai quotes. Its history is equally clear: Cheung (2007: 445) sets up a Proto-Iranian root *x\\u0101d 'to devour, eat, gorge' \\u2014 Parthian x\\u02bcz- 'to devour', Khotanese kh\\u0101s- 'to eat, drink', 'NP x\\u0101yidan/x\\u0101y- \\u201cto chew, gnaw, eat\\u201d', Balochi k\\u02bca\\u03b4i\\u03b8-, Kurdish kayin \\u2014 whose direct cognate is Skt kh\\u0101d; the New Persian -y- is the regular outcome of intervocalic Old Iranian *-d-, exactly as in \\u0101y\\u012bdan/\\u0101yad or z\\u0101y\\u012bdan. What is not right is the route drawn in the chart: x\\u0101y\\u012bdan does not come through the Avestan xad- of node #2 (a different root, 'to strike, wound') but continues the parallel Iranian *x\\u0101d-, and both Horn (no. 469, p.104) and Walde-Pokorny (I 341) in fact connect it straight to Sanskrit kh\\u0101dati without any Avestan intermediary. Wiktionary, following Derksen, states the same relationship in PIE terms: 'From Proto-Indo-Iranian *kh\\u0101d-, from PIE *k(\\u02b7)end- or *k(\\u02b7)enHd(\\u02b0)-. Compare Sanskrit \\u0916\\u093e\\u0926\\u0924\\u093f (kh\\u0101dati, \\u201cto chew, to bite\\u201d) ... and Khotanese khays- (\\u201cto drink\\u201d).' So: right word, right ultimate source, wrong intermediate step.\",\n    \"derivation_fa\": \"خودِ فعل فارسی تردیدناپذیر است: «خاییدن» با ستاک حال «خای» به معنی «به دندان نرم کردن، جویدن»، در برهان قاطع (ص ۷۱۲): «خاییدن \\u2014 بر وزن ساییدن، بمعنی بدندان نرم کردن و جاویدن باشد»، در کنار «خاییده» و «خاید» در همان صفحه و بیت فردوسی که نورایی آورده است. تاریخچهٔ آن هم روشن است: چونگ (۲۰۰۷، ص ۴۴۵) ستاک ایرانی باستان *x\\u0101d «خوردن، بلعیدن» را بازسازی می\\u200cکند \\u2014 پارتی x\\u02bcz-، ختنی kh\\u0101s-، «فارسی نو x\\u0101yidan/x\\u0101y-»، بلوچی و کردی \\u2014 که هم\\u200cریشهٔ مستقیم kh\\u0101d سنسکریت است؛ y در فارسی نو حاصلِ قاعده\\u200cمندِ d میان\\u200cواکه\\u200cای ایرانی باستان است (مانند زاییدن، آییدن). آنچه نادرست است مسیرِ ترسیم\\u200cشده است: «خاییدن» از xad- اوستایی (که ریشه\\u200cای دیگر به معنی «زدن، زخم زدن» است) نمی\\u200cآید، بلکه دنبالهٔ *x\\u0101d ایرانی است؛ هرن (شمارهٔ ۴۶۹) و والده-پوکورنی (ج۱ ص۳۴۱) نیز آن را یکراست به kh\\u0101dati سنسکریت می\\u200cبندند و هیچ واسطهٔ اوستایی نمی\\u200cآورند. پس: واژه درست، سرچشمهٔ نهایی درست، حلقهٔ میانی نادرست \\u2014 با احتیاط پذیرفتنی.\",\n    \"sources\": [W_XAY],\n    \"ref_check\": [\n      {\"ref\": \"BQT:712\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 170 (printed 712): 'خاییدن ۱ \\u2014 بر وزن ساییدن، بمعنی بدندان نرم کردن و جاویدن باشد'; also 'خاییده \\u2014 بروزن و معنی جاویده و بدندان نرم شده باشد' and 'خاید \\u2014 بروزن روایت، یعنی بخاید و در زیر دندان نرم [کند]' on the same page \\u2014 the headword and the alternative stem خای that Nourai brackets.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"p. 445 s.v. *x\\u0101d 'to devour, eat, gorge'\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP x\\u0101yidan/x\\u0101y- \\u201cto chew, gnaw, eat\\u201d, Bal. k\\u02bca\\u03b4i\\u03b8-/k\\u02bca\\u03b4- \\u201cto chew\\u201d, Kurd. (Kurm.) kayin/kay(e)- ... *PARTHIAN: x\\u02bcz- \\u201cto devour\\u201d ... *KHOTANESE: kh\\u0101s- \\u201cto eat, drink\\u201d ... *SANSKRIT: kh\\u0101d.'\"},\n      {\"src\": \"HRN\", \"where\": \"no. 469, p.104\", \"stance\": \"supports\",\n       \"note\": \"Horn's Sanskrit index '\\u221akh\\u0101d-, kh\\u0101dati 469' and NP index both point to entry 469 (p.104) for the verb; Walde-Pokorny I 341 cites 'Horn Np. Et. 104' for npers. x\\u0101y\\u012bdan 'essen, kauen'. (The body of the entry is missing from the OCR of HRN.txt leaf 126.)\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 341\", \"stance\": \"supports\",\n       \"note\": \"'npers. x\\u0101y\\u012bdan \\u201aessen, kauen\\u2018 (H\\u00fcbschmann ZDMG. 38, 423, Horn Np. Et. 104, Uhlenbeck Ai. Wb. 75)'.\"},\n      {\"src\": \"BQT\", \"where\": \"p.712\", \"stance\": \"supports\",\n       \"note\": \"See ref_check.\"}\n    ]\n   }\n  ]\n }\n ]\n}\n\nwith io.open(\"data/verification/page-265.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk265.py && python3 -m json.tool data/verification/page-265.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 265",
 "description": "Write and validate page-265.json"
}
```


### [2026-09-06T20:56:19.114Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'plausible': 3, 'disputed': 2, 'confirmed': 6}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 15, 'partial': 3, 'contradicts': 1, 'not_checked': 1}
books consulted: {'partial': 9, 'supports': 23, 'contradicts': 3, 'silent': 2} | by book: {'CHEUNG': 7, 'BRT': 5, 'HRN': 4, 'WLD': 4, 'BQT': 3, 'PHD': 2, 'NYB': 2, 'HUB': 2, 'AHD': 2, 'KLN': 2, 'IRN': 1, 'SOD': 1, 'SKT': 1, 'MON': 1}
```


## [2026-09-06T20:56:49.516Z] AGENT

Verification complete for PDF page 265 (book page 235). `verify_check.py 265` reports **0 PROBLEM lines**: 11/11 nodes, 3 roots.

**Counts** — nodes: 6 confirmed, 3 plausible, 2 disputed. Roots: 2 confirmed, 1 plausible. Ref checks: 15 supports, 3 partial, 1 contradicts, 1 not_checked. 14 different books consulted (POK, WLD, AHD, IEC, BRT, HRN, HUB, PHD, NYB, CHEUNG, SOD, BQT, MON, IRN, FFD, DRM, KLN, SKT).

**Disputed / problem items**
- **Keuk 1, #2 Persian «افسوس» afsūs** — Nourai follows Darmesteter (Ét. ir. II 131, his DRM:131) deriving it from Av. *aiwi-saoča-; Horn no.101 rejects it outright ("aw. č im Np. nicht zu s werden kann"), Hübschmann calls it unexplained, Nyberg derives MP afsōs from *apa-srau- 'speak'. MP afsōs = 'scorn, mockery', not 'regret'. (This drags node #2's verdict to disputed; its other four words — sūxtan, sōg, sorx, Sohrvard — are sound.)
- **Keuk 1, #2 «سُهروَرد» Sohrvard glossed "a town near Tehran"** — wrong; his own source Farahvashi (IRN:128) says Sohravard is a village of **Zanjan** (birthplace of Sohravardī); the rose-village *near Tehran* on that same page is **وردآورد Vardāvard**. The etymology (*suxra-varda- 'red rose') itself is fine.
- **Khâd/Qhâd, #2 Avestan "xad 1"** — Av. xad- exists (Bartholomae AiW 531, only vi-xaδ- 'squeeze apart') and Bartholomae does make Nourai's comparison, but Cheung 2007:439 assigns it to *xad 'to strike, wound' and says it "should be separated from Skt. khād 'to eat, chew'". Neither HRN:104 nor WLD1:341 cites any Avestan form.
- **Root Khâd, Qhâd (plausible)** — Nourai's two refs contradict each other: WLD1:341 sets up "qhad- 'beißen'" (source of his "Qhâd"), while POK:634 n.1 explicitly withdraws it ("nicht als idg. zu erweisen"). Cheung: IE provenance uncertain; Wiktionary/Derksen reconstruct a different *k(ʷ)enHd-.
- **Keuk 1, #1 (plausible)** — `suxra-vard` and `aiwi-saoka` are not attested Avestan words (nothing in Bartholomae); they are Farahvashi's and Darmesteter's reconstructions. Also Av. `saoka-` means 'benefit', not 'flame'.
- **Keuk 1, #6 kuknos (plausible)** — Pokorny 597/AHD support *kuk-no- 'the white one', but Klein calls κύκνος imitative and Beekes/Wiktionary leave it open.

No transcription_suspect nodes. **One minor extraction error for the owner:** in entry 3 the Kamāl Esmāʿīl quote drops a word — the printed page reads «صلیب و خاج بسوزد کلیسیا **بکند** ـ بنای مدرسه بر گنبد گران آرد», the JSON has «…کلیسیا - بنای…» (confirmed against BQT p.696, which prints the same line).

Notable positive finding: Nourai's page references check out unusually well here — POK:597 reproduces almost his whole Keuk 1 chart verbatim, BQT:696's Moʿin footnote cites HUB:227 (his own next reference), BQT:1190 is the source of his sulphur-ordeal note, and WLD1:341 cites Horn p.104, his Avestan-node reference. BQT vol-2 leaf↔page offset drifts (+542 near p.696, +536 near p.1190); I pinned both with the volume's own «بقیه در صفحهٔ …» catch-lines.
