# Verification process log — verify-page-131


## [2026-09-05T20:02:43.263Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 131 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-131.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-131.json. Write /home/sfmqrb/git/rishe/data/verification/page-131.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 131` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:02:45.104Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:02:45.806Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:02:45.890Z] TOOL RESULT

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


## [2026-09-05T20:02:46.118Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-131.txt"
}
```


### [2026-09-05T20:02:46.161Z] TOOL RESULT

```
1	=== PDF page 131 (book page 101) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dheu 3 : to shine  (refs POK:261)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:261; BQT:172,1008; FFD:32,58 | dav 2, dŭ : to wipe, clean ; han-du, ham-dŭ : to smear together ☞Sem 1 ; uz-dâvayati, uz-dŭ : wipes off
5	  #2 (parent #1) [Persian] refs=BQT:1008 | andŭdan «اندودن ( اندا ، اندای )» : to smear, mix ; zodŭdan «زدودن ( زدا ، زدای )» : to wipe out
6	#3 (parent #0) [Sanskrit] refs=POK:261 | dhâv : to smear
7	--- entry 1 ---
8	ROOT [Indo-European] Dheugh, Dhugh : to milk  (refs POK:271,277; WLD:847,868)
9	#1 (parent #0) [Iranian] refs=POK:271; SYN:386 | dhauğ, daux, dauxš : to milk
10	  #2 (parent #1) [Pahlavi] refs=HRN:129 | dŭxtan, dôxtan : to milk ; dŭšitan : to milk
11	    #3 (parent #2) [Persian] refs=BQT:892,899; POK:271; SYN:386; AEF:273; FFD:54 | dŭšîdan «دوشیدن ( دوش ۴ ، شیردوش )» : to milk ; dŭšîzeh «دوشیزه» : "milker" of the family. See "doxtar" ; dŭxtan 2 «دوختن ۲» : to milk ; dŭğ «دوغ» : diluted yogurt | NOTE: "dŭšîzeh" has lost its original meaning as "milker" and, in some prints of this poem, has been changed to "dŭšandegân"
12	#4 (parent #0) [Indo-European] refs=SHP:329; POK:277; WLD:868 | Dhugh-tar : milker (of the family), daughter ☞Ter 3
13	  #5 (parent #4) [Avestan] refs=KLN:404; POK:277; BQT:333 | dugeda, duğdâr : daughter (milker) ; bağa-duğdâr : God's daughter ☞Bhag ; â-zarema-dugedâ : non-aging woman ☞Ger 2
14	    #6 (parent #5) [Persian] refs=BQT:333,826; WLD:868 | doxtar «دختر ( دخت )» : daughter, girl ; Bîdoxt «بیدخت» : "daughter of God" ; Âzarmîdoxt «آزرمیدخت» : "ageless woman"
15	  #7 (parent #4) [Germanic] refs=AHD; PEI:45 | dohter, dohtor
16	    #8 (parent #7) [English] refs=None | daughter
17	  #9 (parent #4) [Sanskrit] refs=CEL3:321 | duhi-tar : one who milks the cow, daughter
18	
```


## [2026-09-05T20:02:49.336Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-131.json",
 "description": "Read source JSON for page 131"
}
```


### [2026-09-05T20:02:49.386Z] TOOL RESULT

```
{
  "pdf_page": 131,
  "book_page": 101,
  "entries": [
    {
      "root": {
        "name": "Dheu 3",
        "lang": "Indo-European",
        "refs": "POK:261",
        "gloss": "to shine"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:261; BQT:172,1008; FFD:32,58",
          "words": [
            {"translit": "dav 2, dŭ", "gloss": "to wipe, clean", "script": null},
            {"translit": "han-du, ham-dŭ", "gloss": "to smear together", "script": null, "see": ["Sem 1"]},
            {"translit": "uz-dâvayati, uz-dŭ", "gloss": "wipes off", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1008",
          "words": [
            {"translit": "andŭdan", "gloss": "to smear, mix", "script": "اندودن ( اندا ، اندای )"},
            {"translit": "zodŭdan", "gloss": "to wipe out", "script": "زدودن ( زدا ، زدای )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:261",
          "words": [
            {"translit": "dhâv", "gloss": "to smear", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dheugh, Dhugh",
        "lang": "Indo-European",
        "refs": "POK:271,277; WLD:847,868",
        "gloss": "to milk",
        "note": "Compare with the root \"Dhě 1:to suckle milk\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Iranian",
          "refs": "POK:271; SYN:386",
          "words": [
            {"translit": "dhauğ, daux, dauxš", "gloss": "to milk", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:129",
          "words": [
            {"translit": "dŭxtan, dôxtan", "gloss": "to milk", "script": null},
            {"translit": "dŭšitan", "gloss": "to milk", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:892,899; POK:271; SYN:386; AEF:273; FFD:54",
          "words": [
            {"translit": "dŭšîdan", "gloss": "to milk", "script": "دوشیدن ( دوش ۴ ، شیردوش )"},
            {"translit": "dŭšîzeh", "gloss": "\"milker\" of the family. See \"doxtar\"", "script": "دوشیزه"},
            {"translit": "dŭxtan 2", "gloss": "to milk", "script": "دوختن ۲"},
            {"translit": "dŭğ", "gloss": "diluted yogurt", "script": "دوغ"}
          ],
          "script_extra": null,
          "note": "\"dŭšîzeh\" has lost its original meaning as \"milker\" and, in some prints of this poem, has been changed to \"dŭšandegân\"",
          "quote": {
            "text": "بز و میش بد شیرور همچنین - به دوشیزگان داده بد پاکدین",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "SHP:329; POK:277; WLD:868",
          "words": [
            {"translit": "Dhugh-tar", "gloss": "milker (of the family), daughter", "script": null, "see": ["Ter 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Avestan",
          "refs": "KLN:404; POK:277; BQT:333",
          "words": [
            {"translit": "dugeda, duğdâr", "gloss": "daughter (milker)", "script": null},
            {"translit": "bağa-duğdâr", "gloss": "God's daughter", "script": null, "see": ["Bhag"]},
            {"translit": "â-zarema-dugedâ", "gloss": "non-aging woman", "script": null, "see": ["Ger 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:333,826; WLD:868",
          "words": [
            {"translit": "doxtar", "gloss": "daughter, girl", "script": "دختر ( دخت )"},
            {"translit": "Bîdoxt", "gloss": "\"daughter of God\"", "script": "بیدخت"},
            {"translit": "Âzarmîdoxt", "gloss": "\"ageless woman\"", "script": "آزرمیدخت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "Germanic",
          "refs": "AHD; PEI:45",
          "words": [
            {"translit": "dohter, dohtor", "gloss": null, "script": null}
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
            {"translit": "daughter", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 4,
          "lang": "Sanskrit",
          "refs": "CEL3:321",
          "words": [
            {"translit": "duhi-tar", "gloss": "one who milks the cow, daughter", "script": null}
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


## [2026-09-05T20:02:49.883Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:02:49.929Z] TOOL RESULT

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


## [2026-09-05T20:03:24.688Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','HRN','KLN','BQT','SYN','PEI','CEL3','SHP','AEF','FFD','AHD','BRT','PHD','NYB','CHEUNG','MON','ARY','IEC','SKT','FSD','WEB','HUB','IRN']:\n    v=d.get(k)\n    print('---',k)\n    print(json.dumps(v,ensure_ascii=False,indent=1)[:900] if v else 'MISSING')\n\""
}
```


## [2026-09-05T20:03:25.208Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -60 data/verification/page-127.json"
}
```


### [2026-09-05T20:03:26.695Z] TOOL RESULT

```
--- POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); e
--- WLD
{
 "title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32",
 "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_B
--- HRN
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decen
--- KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0
--- BQT
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofi
--- SYN
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the con
--- PEI
{
 "title": "M. Pei, The Families of Words, New York 1962",
 "edition_found": "1962 (open copy)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/familiesofwords00inpeim",
 "identifier": "familiesofwords00inpeim (lending copies: familiesofwords00peim, bwb_FS0-ABP-200)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt",
 "page_offset": "leaf = printed + 18 (e.g. leaf 21 = p.3). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Popular prose; grep the word.",
 "notes": "1 citation."
}
--- CEL3
MISSING
--- SHP
{
 "title": "J. T. Shipley, Dictionary of Word Origins, New York 1945",
 "edition_found": "1945 (lending-only)",
 "kind": "hathitrust_fullview+archive_restricted",
 "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.32106001576476 (1945 ed., rightsCode pd = FULL VIEW, catalog record 001441050) ; archive.org dictionaryofword00ship and 15 others = lending only",
 "identifier": "dictionaryofword0000jose_n4p8 (also dictionaryofword0000jose_n6p4, dictionaryofword0000ship_d0v5)",
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.",
 "notes": "RE-SEARCH 2026-09: the 1945 edition is public-domain full view on HathiTrust (copyright evidently not renewed) — download the PDF in a browser (HathiTrust IP-blocks this host: curl/WebFetch get 403). Google: no view for 1945, partial preview for the 2021 Open Road reissue only."
}
--- AEF
{
 "title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence",
 "kind": "catalog",
 "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog",
 "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitle
--- FFD
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF pa
--- AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins 
--- BRT
{
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
 "identifier": "altiranischeswr00bartgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt",
 "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLU
--- PHD
{
 "title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971",
 "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-concise-pahlavi-dictionary",
 "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://ww
--- NYB
{
 "title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)",
 "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg",
 "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
 "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.",
 "notes": " local_files: /ho
--- CHEUNG
MISSING
--- MON
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pag
--- ARY
{
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page 
--- IEC
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An I
--- SKT
{
 "title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)",
 "edition_found": "1911 'new and corrected impression' (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/aconciseetymolo01skeagoog",
 "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
 "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.",
 "notes": "Nourai says '1882-
--- FSD
{
 "title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)",
 "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.147439",
 "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f betwe
--- WEB
{
 "title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)",
 "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w",
 "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt",
 "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword bold at line
--- HUB
{
 "title": "H. Hübschmann, Persische Studien, Strassburg 1895",
 "edition_found": "1895 (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/persischestudie00hbgoog",
 "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "notes": "Built from djvu.xml (no hocr); OCR quality moderate.",
 "cites": "page number of Hübschmann, Persische Stud
--- IRN
{
 "title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)",
 "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"
 ],
 "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same sett
```


### [2026-09-05T20:03:26.735Z] TOOL RESULT

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


## [2026-09-05T20:03:32.032Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dheu-\\|dheu̯-\\|dheu̯-3\\|dheu-3\" POK_01.txt | sed -n '1,60p'"
}
```


### [2026-09-05T20:03:32.086Z] TOOL RESULT

```
2961:Im   Germ,  außerdem    mit    i-Vokalismus    mnd.    trlseln,   westfäl.    trids^ly^      i ,rollen,  taumeln^,  holl.  trillen  ,zittern^  (woraus  ital.  trillare  ^beben,  Trillep schlagen')  usw.  Gegen  Verbindung  von  ai.  drdvati  mit  av.  dvaraiti  ,geht* s.  unter  *dheu-y  *dheuer-  ^stieben^
3395:In  allen  Gliedern  etwas  zweifelhafte  Verbindung.  Über  air.  de'd(a). vgl.  Pedersen  KG.  II  504  f.  (von  einem  Perf.  *dhe-doue  aus  zu  got.  diwans , sterblich'?  s.  dheu-  , hinschwinden',  wo  auch  über  air.  dlth,  arm.  di).  Die germ.  Sippe  endlich  erinnert  z.  T.  an  die  unter  "^dheues-  ,stieben'  bespro- chene von  ndd.  dösig  und  könnte  nicht  bloß  in  der  5-Erw.,  sondern  auch in  der  Bed.  sich  z.  T.  nach  dieser  gerichtet  haben;  immerhin  ist  mit  einer alten  Verwandtschaft  von  anord.  dcesask  usw.  und  ir.  -deda  zu  rechnen.
3528:inwieweit  die  s-Formen  schwed.  mdartl.  stimma,  stimha  , dampfen^,  norw. mdartl.  stamma,  stamha  ,stinken^  einen  idg.  Hintergrund  haben  oder  nur nach  dem  Nebeneinander  von  ahd.  toum :  ags.  stEam,  dt.  toben :  stieben (s.  unter  dheu-,  dkeu-bh-  ,stieben^)  neugeschaffen  sind,  ist  fraglich;
3731:Got.  diwans  (*dheu-ono-) , sterblich*,  ablaut.  ahd.  touiven,  as.  döian  , sterben*, anord.  deyja,  dö  (*döw),  däinn  ,sterben';  got.  daups  ,tot*,  auch  af-dauipt ,geplagt',  ahd.  töt^  ags.  dead,  anord.  daudr  ,tot*,  got.  dau^us  ,Tod',  ahd. töd,  ags.  deaj)^  anord.  daud-r,  -ar  und  daude  ,Tod*;
3733:vielleicht  lat. /wnws  (fönus?)  n.  , Leichenbegängnis,  Bestattung',  fallsaus *dheu{e)-nos  ,auf  den  Tod  bezügliche  Erweisung';  formell  jedoch  genau =  air.  n.  5-Stamm  dün  , Festung',  wohl  ursprüngl.  ,Burghügel'  (s.  unter 4.  dheu-  S.  263);
3745:4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  riechen,  stinken;  stürmen,  in  heftiger, wallender  Bewegung  sein,  auch  seelisch;  in  heftige,  wirbelnde  Bewe- gung versetzen,  schütteln';  Nominalbildungen:  dhü-li-,  dhü-mo-.
3781:Vgl.  noch  das  vielleicht  ursprungsgleiche  *dheu-  ,laufen,  rinnen'.
3846:Ob  hierher  als  *dheu-g-:   germ.  *du-k-j  *du-kk-  ^tauchen,  sich  ducken"',
3852:dheues-,  dhues-,  dheus-,  dhas-  ,stieben,  stäuben,  wirbeln  (nebeln,  regnen, Dunst,  Staub;  aufs  seelische  Gebiet  angewendet:  gestehen,  verwirrt sein,  betäubt, .  dösig,  albern),  stürmen  (vom  Wind  und  aufgeregtem Wesen),  blasen,  wehen,  hauchen,  keuchen  (Hauch,  Atem,  Geist,  Ge- spenst, animal;  riechen,  Geruch)'.  Erweiterung  von  4.  dheu-',  auch Ausdrücke  für  , dunkle  Farben'  scheinen  als  ,nebelgrau,  staubfarben' angereiht  werden  zu  sollen. Ai.  dhvamsati  , zerstiebt,  zerfällt,  geht  zugrunde',  Partiz.  dhvastd-j Kaus.  dhvamsdyati,  dhvasdyati  ,bestäubt,  vernichtet',  dhvasmdn-   m.  ,Ver-
3854:dunkelung^;  dhvasird'  ,hestii\iht,  besprengt^,  dhvasrd-  ^bestaubt,  unkenntlich^, dhüdsti-  f.  ;das  Zerstäuben^  (=  ahd.  tunist,  dun{i)st  ,Wind,  Sturm,  Hauch, punst';  ags.  afries.  düst  ,Staub^),  dhüsara-  , staub  farbig^;  zur  Bilduno- (*dhi-es-mi,  Konj.  dheu-s-5  neben  "^dhu-n-es-mi,  Konj.  *dhu-m-s-o)  vgl. Kuiper  Nasalpräs.  41;
```


## [2026-09-05T20:03:32.689Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==269||NR==270' POK_01.txt | head -120"
}
```


### [2026-09-05T20:03:34.279Z] TOOL RESULT

```
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
Npers.  darz,  darza  ,Naht*,  darzmän,  darznän  , Faden*,  darzan  ,NadelV pehl.  darzik  , Schneider';
arm.  dafnam  (*darjnam),  Aor.  darjay  ,sich  wenden,  sich
```


## [2026-09-05T20:03:41.402Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^[0-9]\\. *dheu\\|^ *[0-9]\\.  *dheu\\|dheu-  ,\\|dheu-,\\|dheu-  ,\" POK_01.txt | sed -n '1,40p'"
}
```


### [2026-09-05T20:03:41.465Z] TOOL RESULT

```
3395:In  allen  Gliedern  etwas  zweifelhafte  Verbindung.  Über  air.  de'd(a). vgl.  Pedersen  KG.  II  504  f.  (von  einem  Perf.  *dhe-doue  aus  zu  got.  diwans , sterblich'?  s.  dheu-  , hinschwinden',  wo  auch  über  air.  dlth,  arm.  di).  Die germ.  Sippe  endlich  erinnert  z.  T.  an  die  unter  "^dheues-  ,stieben'  bespro- chene von  ndd.  dösig  und  könnte  nicht  bloß  in  der  5-Erw.,  sondern  auch in  der  Bed.  sich  z.  T.  nach  dieser  gerichtet  haben;  immerhin  ist  mit  einer alten  Verwandtschaft  von  anord.  dcesask  usw.  und  ir.  -deda  zu  rechnen.
3528:inwieweit  die  s-Formen  schwed.  mdartl.  stimma,  stimha  , dampfen^,  norw. mdartl.  stamma,  stamha  ,stinken^  einen  idg.  Hintergrund  haben  oder  nur nach  dem  Nebeneinander  von  ahd.  toum :  ags.  stEam,  dt.  toben :  stieben (s.  unter  dheu-,  dkeu-bh-  ,stieben^)  neugeschaffen  sind,  ist  fraglich;
3745:4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  riechen,  stinken;  stürmen,  in  heftiger, wallender  Bewegung  sein,  auch  seelisch;  in  heftige,  wirbelnde  Bewe- gung versetzen,  schütteln';  Nominalbildungen:  dhü-li-,  dhü-mo-.
3781:Vgl.  noch  das  vielleicht  ursprungsgleiche  *dheu-  ,laufen,  rinnen'.
```


## [2026-09-05T20:03:41.724Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3700,3760p' POK_01.txt"
}
```


### [2026-09-05T20:03:41.765Z] TOOL RESULT

```
russ.  dereuj  deren  , Hartriegel,  Kornelkirsche',  skr.  drijen,  öech.  drin  ds. poln.  (alt)  drzon  jBerberitze',  kaschub.  drbn  , Dornen',  polab.  dren  ,Dorn'.
Germ.-sl.  Grundf.    kann   "^dherghno-   sein    und    stünde    dem   freilich   in seiner   Bed.    , Schößling,    Zweig',    PL  ,junges    Gebüsch'    erheblich    anders- gefärbten gr.  TQ€xyog  (Hes.,  anthoL),  tsqxvoq  (Maximus),  kypr.  t«  zsQxvija  ^  • sehr  nahe.
WP.  I  862  f.,  Pedersen  KG.  I  97,  M.-L.  2762.
dheregh-  {dhrgh-nä-)  , drehen,  winden,  wenden'  (auch  , spinnen,  nähen*).
Npers.  darz,  darza  ,Naht*,  darzmän,  darznän  , Faden*,  darzan  ,NadelV pehl.  darzik  , Schneider';
arm.  dafnam  (*darjnam),  Aor.  darjay  ,sich  wenden,  sich  drehen,  sich kehren;  zurückkehren*,  dafn  , bitter,  herbe*  (vgl.  oivog  zgerrsTac  u.  dgl.), darj  jWendung,  Umkehr,  Rückkehr*,  Kaus.  darjucanem  ,verto,  averto, converto,  reddo*;
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
Arm.  di'Jt  , Götter*  (PI.  *dheses)',  lat./eWae  (alat. /esiae)  ,Tage,  an  denen keine  Geschäfte  vorgenommen  wurden,  Feiertage*,  festus  ,f estlich,  feier- lich, ursprüngl.  von  den  der  religiösen  Feier  gewidmeten  Tagen',  osk. fiisnam  Akk.  ,templum',  umbr.  fesnaf-e  ,in  fanum'*,  tiefstufig  lat.  fänum {*fas-no-m)  , heiliger,  den  Göttern  geweihter  Ort'  und  ai.  dhisnya-  , an- dächtig, fromm,  heilig'  (unsicherer  dhisanyant-  u.  dgl.,  s.  unter  dheid- , sehen');  über  gr.  d-eog  ,Gott'  s.  unter  dheues-,  über  lat.  fäs,  fästus  oben S.  105f.
WP.  I  867,  WH.  I  453,  3 f.;  EjVP  333,  347 f.
X.  dbeu-  ,laufen,  rinnen*.
Ai.  dhdvate  , rennt,  rinnt',  dehnstufig  dhdvati  ds.,  dhäuti-h  f.  , Quelle, Bach*;  mpers.  davfidan  ,laufen,  eilen*,  päm.  dav-  ,laufen,  rennen';
17*
260
gi\   ^€w,   ep.   auch   x^siu),  Fut.   d^£vaoy,ai  , laufen*;   lak.    af]'  rqixe   Hes; ^oög  , schnell',  ßorj-^öog  ,auf  einen  Anruf  schnell  zur  Hand,  helfend*,  daznl ßotjd-iü)   (statt   *ßorjdo€Cü)  , helfe',    ^oaCu)   ,versetze  in  schnelle  Bewegun, bewege  mich  schnell';
gr.-illjr.  dvdv'  ytgrjvrjv  Hes.;
anord.  dgggy  Gen.  dggguar  {*dawwo),  ags.  deatü,  as.  dau^  ahd.  to\i^  n} Tau  (*dawioa-)',
unsicher  mir.  döe  ,Meer'  (*dheuiä)  als  ,das  heftig  Bewegte';
hierher  wohl  *dhu-rO'  im  thrak.  FIN  ^A-d^vqag  (^n-dhu-r-)  und  in reichen  ven.-illyr.  FIN,  so  illyr.  Duria  (Ungarn),  nhd.  Tyra,  Thur,  äh Dura   (Elsaß,  Schweiz),    oberital.  Dora,  Doria,    frz.   Dore,    Doire,   Don iber.  Durius,    Turia  usw.   (Fokorny  Urill.  2,  10,  79,  105,  113,  127,  145^ 160,  165,  169  f.);
nach  Rozwadowski  (Rev.  Slav.  6,  58  ff.)  hierher  der  FIN  Düna,  wes slav.  Dvina  (*dhueinä),  als  finn.  väinä  ,breiter  Fluß*,  estn.  väin(a)  ,Sund* syrj.  'dyn  »Mündung*  entlehnt. .   WP.  I  834.
2,  dbeu-,  dbu-ei-  , hinschwinden,  bewußtlos  werden,  sterben*.
Got.  diwans  (*dheu-ono-) , sterblich*,  ablaut.  ahd.  touiven,  as.  döian  , sterben*, anord.  deyja,  dö  (*döw),  däinn  ,sterben';  got.  daups  ,tot*,  auch  af-dauipt ,geplagt',  ahd.  töt^  ags.  dead,  anord.  daudr  ,tot*,  got.  dau^us  ,Tod',  ahd. töd,  ags.  deaj)^  anord.  daud-r,  -ar  und  daude  ,Tod*;
air.  duine  (*dliu-n-io-),  PI.  döini  (*dheuen-{o-),  cymr.  dyn,  corn.  bret. den  , Mensch*  (.Sterblicher*,  Brugmann  ZfceltPh.  3,  595 ff.);  s.  auch  unter ghdem-]
vielleicht  lat. /wnws  (fönus?)  n.  , Leichenbegängnis,  Bestattung',  fallsaus *dheu{e)-nos  ,auf  den  Tod  bezügliche  Erweisung';  formell  jedoch  genau =  air.  n.  5-Stamm  dün  , Festung',  wohl  ursprüngl.  ,Burghügel'  (s.  unter 4.  dheu-  S.  263);
nach  Marstrander  Pres,  a  nasale  inf.  15^  hierher  air.  -deda  , seh  windet dahin'  aus  *dhe-dhu-ä-t]  vgl.  auch  oben  unter  3.  dhe-]
im  Germ,  auch  die  Bed.  , fühllos,  ohnmächtig  werden*,  awnord.  da {*dawa)  , Bewußtlosigkeit,  Ohnmacht*,  Prät.  dö  auch  , wurde  gefühllos' (von  Gliedern),  aschwed.  däna  ,in  Ohnmacht  fallen*,  norw.  daana  , steif, lahm  werden  (von  Gliedern),  in  Ohnmacht  fallen'  (Ableit.  vom  Partiz. dainn),  isl.  dodl  , Gefühllosigkeit*,  dodna  ,gefühllos  werden*,  got.  usdaupt ,im-piger,  eifrig',  ahd.  tawalön  ,hinschwinden,  hinsterben*,  ndl.  dauwel jträges  Weib*;  ferner  anord.  cZä  auch  »Entzückung  der  Seele*  (,*Betäu bung'),  da  (*dawen)  , bewundern';  anord.  dan  f.  ,Tod'.
3'
261
Erweiterung-  dhu-ei-  :  dhu-i-  in:
arm.  di^  Gen.  dioy  , Leiche,  Leichnam',  air.  dlth  {*dhuUu-)  ,Ende, Tod';  ag-s.  dwlnan  (st.  V.)  ,abnehmen;  schwinden',  neben  dem  7iöM-Verb anord.  duma  und  duena  ds.;  ags.  dwcescan  , auslöschen'  (*dwaiskjan),  lit. (/i?i5<i  ,erlöschen'  (Büga  bei  Endzelin  KZ.  52,  123).
WP.  I  835,  WH.  I  451,  568.
dbeu-  , blank,  glänzen'.
Ai.  dhavald-  ,glänzend  weiß',  dJiävatl  ,macht  blank,  reinigt,  spült',  av. fraöavata  ,rieb  sich  (reinigend)  ab';
gr.  ^oög' . . .  Xa^TtQÖg^  d^owaau  •  . . .  XaiinQvvai  Hes.,  ddoVreg  X«t;xci:  -^iovreg Ps.-Hsd.,  S^alsiov  xad-agöv.   xal  d-coUov  Hes.  (Kontr.  aus  *^oJ^aUog).
WP.  I  835,  Schulze  KZ.  29,  260  f.  =  Kl.  Sehr.  369.
4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  riechen,  stinken;  stürmen,  in  heftiger, wallender  Bewegung  sein,  auch  seelisch;  in  heftige,  wirbelnde  Bewe- gung versetzen,  schütteln';  Nominalbildungen:  dhü-li-,  dhü-mo-.
Mit  lü-Formantien:
Ai.  dhUmd-h  m.  ,Rauch,  Dampf,  dhümäyati  , raucht,  dampft'  =  lat. fümäre,  formell  auch  =  ahd.  tümön  ,sich  im  Kreise  drehen*;
gr.  d^vixog  ,  Gemüts  Wallung,  Leidenschaft,  Mut*  (dvi^iao)  noch  rein  sinn- lich , rauche,  räuchere';  ■d-Vf.idX-ajip  , Kohlenmeiler',  d-^i.av.ög  , leidenschaftlich*, d^v^aivo)  , zürne*  usw.);
lat.  fümus  , Rauch,  Dampf,  Qualm,  Brodem'  (fümäre  s.  oben);
lit.  dnmai  PI.  , Rauch',  lett.  dumi  PL,  apr.  dumis  ds.;
aksl.  dyrm  , Rauch*;
mit  ü:  mir.  duynacha  PL  ,Nebel'  (nir.  dumhach  aus  *dhumuko-  , neblig, dunkel');  gr.  d-^^og,  -ov  , Thymian'  (starkriechende  Pflanze  wie  auch O^vußgay  d-vi^ßgov  ,Satureja  thymbra  L.'  s.  Boisacq  m.  Lit.;  nach  Nieder- mann Gl.  19,  14  zu  russ.  dubrdvka,  dubrövka  ,Potentilla  Tormentilla', das  nach   Berneker  215  zu    aksl.  dgmh^  , Eiche'  [s.  unten  S.  264]  gehört).
Lat.  ßmus  ,Mist,  Dünger'  (als  *dhu-i-mos  auf  Grund  von  suffio^  -Ire erwachsen);
mit   idg.  ou:    ahd.    toum    , Dampf,    Dunst,  Duft',   as.   dömian   , dampfen'.
Dazu  Farbenadjektive  der  Bed.  ,rauchfarben,  nebelgrau,  düster*:  ai. dhümrd-  ,rauchfarben,  grau,  braunrot,  trüb  (auch  vom  Verstand)',  dhümala- .rauchfarben,  braunrot';
lit.  dumhlas  , Schlamm,  Moor  auf  dem  Grund  eines  Teiches',  lett.  duhl'i , Schlamm,    Kot'    (vermutlich  =  ai.  dhümra-]    vgl.  aber  unten  S.  268  und
262
Mühlenbach-Endzelin  I  509),  lett.  dümal'§  , dunkelfarbig,  braun',  düma% ,rauchfarben',  dumjs,  fem.  dumja  , dunkelbraun,  fabl,  trüb  (von  den  Auge^! dumm*,  dumühsnis   , Sumpf,  dumhra  zeme   ,schwarzes  Moorland',   duThhr^ duffibrs  , Quelle,  Moor,  Morast'  (vgl.  Mühlenbach-Endzelin  I  514;  ausfübrlic}^ über  solche  Moorbezeichnungen  nach  der  Farbe  Schulze  Kl.  Sehr.  X\^,
vgl.  mit   dem   Farbnamensuffix  -no-:   lett.    duni,   dünas  PL    , Schlamm''
mit  'ko-,  bzw.  von  der  Wurzelerw.  mit  -k-:  lett.  düksne,  dükste  , Sumpf Pfuhl,  MovsisV  :  dükans  , Schweißfuchs,  dunkelfarbig';
```


## [2026-09-05T20:03:56.760Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG dau ===\" && grep -n \"^\\*dau\\|^\\*dauH\\|\\*dau̯\\|andūdan\\|andudan\\|zudūdan\\|zudan\" CHEUNG.txt | head -40"
}
```


### [2026-09-05T20:03:56.825Z] TOOL RESULT

```
=== CHEUNG dau ===
5241:*dau2 65 
5253:*dau! *to speak, chat' 
5286:*dau? ‘to run’ 
5323:*dau? ? ‘to be skilful’ 
5335:*daub ‘to strike, hit, pick ?” 
5358:*dauč! (*dauj ?) ‘to milk, traire (< **to draw’ ?)’ 
5371:*dauHl 67 
5422:*dauH! ‘to burn’ 
5489:*dauxs 69 
5506:zadudan/zaday- ‘to polish, clean’ || (+ *ham-) NP andudan/anday- ‘to smear, 
5538:*dauxš ‘to suck, suckle, milk’ 
8208:*NWIR: (+ *abi-) NP afzudan/afzäy- ‘to increase’ 
9457:*dauH?. 
40697:afzudan/afzay-, 113 
55510:*dau’, *Hnar 
55999:*dau, *zrad 
57205:*dauc', *daux 
57361:*daub 
57657:*dauH’, *garš, *marH!, 
57661:*dau', *dram, *drau’, *duar, 
57930:*dauH’, *raip, *sard 
57951:*dau, *far’, *HaH(a)d, 
58075:*daub, *gan, *huah, *jan, 
58127:*dau, *zrad
```


## [2026-09-05T20:03:58.174Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG dau2/dauc ===\" && grep -n \"dauš\\|dauxš\\|daug\\|dug\" CHEUNG.txt | head -40"
}
```


### [2026-09-05T20:03:58.228Z] TOOL RESULT

```
=== CHEUNG dau2/dauc ===
5368:óüy (Е), Bart. óoy, Yzgh. day ‘buttermilk’ (< *dauga-, EVS: 30b), Pash. Iwayza 
5374:‘cow in milk’ (< *dauga-zä-, EVP: 40 f.) ? Pash. salwäya ‘bucket for drawing water 
5375:from a well’ (< *usa-dauga-, EVS: 31a) || (+ *pari-) Yzgh. pardis- (inch.) ‘to give 
5383:© Both *daué and *dauxš are problematic: they may have either a different origin or 
5389:connected with Gr. tuyxavo ‘to reach the goal’, Goth. daug ‘it was good for, es 
5396:*IE COGNATES: Gr. eum ‘I prepare’, Goth. (pret.) daug ‘was useful’, NHG taugen. 
5538:*dauxš ‘to suck, suckle, milk’ 
8692:cf. notably *d’ugHbter- ‘daughter’ (Gr. Өоү@&ттр vs. Skt. duhitär-) and *megH)- 
10979:‘daughter-in-law’ (< *snusa-), "mh ‘ewe’ (< *maisi-). = Samadi: 110 
13275:raugmi, Lith. riáugiu (ridugéti) ‘I belch’, OHG ita-rucken ‘to ruminate’ 
13625:*NWIR: NP bayo ‘bride’, Kurd. Бок ‘bride, daughter-in-law’, Zaz. veyv (Ё) ‘bride’, 
13626:Bakht. bahig ‘bride, daughter-in-law’ 
20084:from I. fadyg, D. fadug ‘piece of cloth, stripe; trouser-leg’, which are suffixed 
24910:zidug, Sariq. zidor-/zidug, Ishk. zdar-, M. stor-/stor-, Yi. 'stör-/stär- ‘to sweep’ 
30092:Bart. razen, Orosh. rizin, Sariq. rajen ‘daughter’ 
46539:fadug (D), 305 
49428:zidor-/zidug, 382 
52647:riáugiu (ridugéti), 195 
53399:daug, 67
```


## [2026-09-05T20:04:01.544Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5480,5580p' CHEUNG.txt"
}
```


## [2026-09-05T20:04:01.560Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5355,5400p' CHEUNG.txt"
}
```


### [2026-09-05T20:04:01.612Z] TOOL RESULT

```
* dauH? ‘to smear, rub (on)’ 

*AVESTAN: (+ *fra-) YAv. fradauu- ‘to be rubbed off with’ = Liste: 31 
MED .; Pres. them.: IND. 3sg. YAv. “fradauuaite (V 5.24), INJ. 3sg. YAv. fraóauuata (V 9.29) 
*MIDDLE PERSIAN: (+ *8-) MMP *’rwdg ‘pollution, dir" > DMMPP: 53a 


*dauxs 69 


*KHOTANESE: (?) LKh. du- ‘to strike, beat; clean’ (also from *daub ?) || (+ *uz-) 
LKh. uysdu- ‘to remove’ = SGS: 44 f., 15 

*SOGDIAN: BSogd. ó w ‘to smear, plaster’ || (+ *ham-) BSogd. ’nö’w, MSogd. ’nöw 
‘to smear, anoint’ 

Pres.: SUBJ. 3sg. BSogd. 6’w’t; Inf.: BSogd. ö’w’y || (+ *ham-) Pres.: IND. 3sg. BSogd. "nd'wt; Inf.: 
BSogd. ’nö’w’y, pret. MSogd. ’nöwt 

*CHORESMIAN: m/6’w- ‘to rub in, smear’ || (+ *apa-) bö’w- ‘to polish’ = Samadi: 63 
f., 16 

*NWIR: ? Gil. (Rsht.) vaseen/vasin- (sec. inch.-caus. ?) ‘to rub’ || (+ *à-) NP 
aludan/alay- ‘to soil, pollute, stain’, Khuns. ali (ppp.) ‘stained, soiled’ || (+ *uz-) NP 
zadudan/zaday- ‘to polish, clean’ || (+ *ham-) NP andudan/anday- ‘to smear, 
(re)cover, attach’, Tt. (Xia.) m-andevmun ‘we plaster’, b-andev(n) ‘plaster!’. o The 
original meaning of NP 4ludan/alay- appears to be ‘to smear’, v. Horn 1893: 10. The 
formation is influenced by the antonym (M)MP p’rw-, NP palüdan ‘to filter’, on 
which see *harz. 

*NEIR: Oss. I. dawyn/dawd, D. dawun/dawd ‘to smooth, polish’, Yghn. dou-/dóuta 
‘to plaster’, Wa. ôbrw-/ôowd ‘to rub, smear’ || (+ *uz-) Pash. zdoyol ‘to rub, grind, 
polish’ (< Pers. ?) || (+ *fra-) Oss. I. raedyjyn/reedyd, D. raedujun/reedud ‘to err, to sin 
against’ || (+ *ham-) Yi. da-/davd- ‘to smear’ 

*SANSKRIT: ? dhav ‘to shake, stir? (RV+) > EWAia I: 782 f. 

Ó It is difficult to reconcile the Ir. root and Skt. dhav ‘to shake, stir’ (as assigned in 
EW4Aia, l.c.) semantically. They may rather suggest a different etymology. Skt. does 
have a good IE etymology (ON dyja ‘to shake’, Gr. Өоуёо ‘to storm, to move fast’), 
whereas IE cognates cannot be cited in support of Ir. *dauH! ‘to smear, rub (on)’. It 
is more likely a "Reimbildung", cf. *sauH!. A.L. points out though that in Vedic 
there are, from the same root, some (synchronically separate) present forms that are 
much closer in meaning to the Ir. ones: pres. 3sg. à dhavati (RV+), pass. 3du. 
sam-dhavyete (KS), pass. partic. ä-dhüyamäna- (TS^) ‘to rinse, clean, rub, polish’. 
These forms are rather unrelated to dhav’ and may therefore be the genuine Skt. 
correspondences of Ir. *dauH'. 


*PIE — — LIV: 149 f. | Pok.: 261 

*REFERENCES: EVP: 101; Christensen, Contributions I: 74 f.; HFL II: 204b; Andreev — PeSéereva: 248b Ё; 
Abaev, Slovar’ I: 349; Yarshater 1969: 211, 216; Abaev, Slovar’ II: 362 f.; WIM I: 342; DKS: 171a, 6b; 
Werba 1997: 352 f.; Steblin-Kamenskij 1999: 168; NEVP: 101; ESIJa II: 380 ff. 


*dauxš ‘to suck, suckle, milk’ 
*MIDDLE PERSIAN: BMP dws- /dös-/ ‘to milk’ 
Pres.: IND. 3р1. BMP dwsynd /dosend/; Partic.: pass. perf. BMP dwht /doxt/, BMP dwsyt /dosid/ 


*SOGDIAN: ? BSogd. ówš- ‘to peck, nibble’ (š needs an explanation) 
BPres.: IND. 3pl. BSogd. öws’nt (SCE 400) 


70 *daxS 


*CHORESMIAN: (+ *ati-) čx- ‘to suck (milk)’, (caus.) Ew’xy- ‘to breastfeed (baby)’ 
= Samadi: 59 

*NWIR: NP doxtan/dos-, Bal. dosag, Kurd. (Kurm.) dötin/605-, (Sor.) dosin/dos-, 
Zaz. dotis, dosnayis, Abyan., Abz. döta/düs-, Ard. dotte/dos-, Anar., Nn. dote/dos-, 
Gil. dustan, Tal. düse, Khuns. dus-/dusa, Varz. dote/dos-, Qohr. dóta/dus-, Tr. döta/ 
dös-, Shamerz. bedostan, Lasg. bedusaon, Sorkh. bedüston, Semn. bedüsiyon, Sang. 
bedüs diyetan ‘to milk’, Bakht. dun ‘milking, process of milking’ ( *dauxsna- ?) 
*NEIR: Pash. Iwas-/lwasal ‘to milk’, Sangl. des-/doyd, Ishk. des-/dest ‘to milk’ || (+ 
*ati-) ? Yzgh. cax-/coxt ‘to milk’ 


0 This root is a so-formation of IE *d'eug"- ‘to prepare’. See *daud!. 
*REFERENCES: EVP: 41; IIFL II: 391b; WIM I: 68; Vahman — Asatrian 1991: 92 f.; Paul 1998: 296a; 
Cabolov 2001: 329; Lecoq 2002: 121, 123, 125 (passim) 


*daxš ‘to show, teach, reveal, mark’ 

*AVESTAN: daxs- ‘to instruct, show’, daxsta- (orig. ppp., n.) ‘sign, revelation [BMP 
/daxsag/]; menstruation [= BMP /dastan/]’ (Y 34.6, Y 51.9, V, etc.), ? OAv. daxsära- 
(m.) ‘mark, sign’ (Y 43.7) || (+ *fra-) ‘to instruct, teach’, also YAv. fradaxStar- 


‘teacher’ — Liste: 27 

Pres. {1} them.: INJ. 3sg. OAv. daxsat (Y 43.15); Pres. {2} aia-: OPT. med. 3sg. YAv. aóaxsaiiaeta (Y 
12.5), IMPV. 25р. OAv. «fra»daxsaiia (Y 33.13) 

*MIDDLE PERSIAN: MMP dxsg, ВМР dhsk /daxsag/ ‘sign, mark, characteristic; 
memory’ (Nyberg II: 61b), BMP dst’n /dastan/ ‘menstruation; menstruous’ (Cantera
```


### [2026-09-05T20:04:01.622Z] TOOL RESULT

```
*REFERENCES: Andreev — PeSéereva: 233b; ELO: 41; Abaev, Slovar’ П: 361 Ё; EVS: 32b; ESIJa II: 398ff. 


*dauč! (*dauj ?) ‘to milk, traire (< **to draw’ ?)’ 

*MIDDLE PERSIAN: ? BMP dws- /dös-/ (inch.) ‘to milk’ (Nyberg II: 65a) 
*CHORESMIAN: óws- (inch.) ‘to milk’ = Samadi: 67 

*NWIR: NP dog 'butter-milk, whey; a dairy drink of diluted yoghurt and water’, 
Kurd. (Kurm.) daw (m.), (Sor.) do, Tal. dü, Kash. dü ‘butter-milk’ 

*NEIR: Oss. I. ducyn/dygd, D. docun/dogd, Sh. öüj-, (Baj.) óüz-/óuyd, Rosh. 
6uz-/dawd, duzd, Sariq. dewz-/dewd, Yi. lüz-/lüyd-, Wa. dic-/Soyn- ‘to milk’, Sh. 
óüy (Е), Bart. óoy, Yzgh. day ‘buttermilk’ (< *dauga-, EVS: 30b), Pash. Iwayza 


*dauHl 67 


‘cow in milk’ (< *dauga-zä-, EVP: 40 f.) ? Pash. salwäya ‘bucket for drawing water 
from a well’ (< *usa-dauga-, EVS: 31a) || (+ *pari-) Yzgh. pardis- (inch.) ‘to give 
milk’ || (+ *ш-) Sh. wióüj-/wióuyd ‘to peel, strip, skin, pluck, cleanse (nuts, peas) 
from husk and pods’ (< archaic *‘to draw’ ?) 

*MISC: Par. duc- ‘to milk’ 

*SANSKRIT: dogh ‘to milk’ (RV+) = EWAia I: 747 f. 

© Both *daué and *dauxš are problematic: they may have either a different origin or 
show (mutual) influence of another root: *dauc may have acquired the specialized 
meaning ‘to milk’ from ‘to draw’, as hinted by Morgenstierne (EVS, ibid.), whence 
from IE *deuk- ‘to draw’. Or is *dauc merely contaminated with this IE root ? 
Nominal variants with voiced velar *-g are also attested in Iranian. As for *dauxs-, 
-§ has not been accounted for sofar. The Skt. correspondence dogh- is usually 
connected with Gr. tuyxavo ‘to reach the goal’, Goth. daug ‘it was good for, es 
taugte', NHG taugen, etc., despite the apparent semantic difficulties (cf. EWAia, 
l.c.). Perhaps the Skt. stative duhé ‘(cow) gives milk’ may be the starting point: > ‘is 
useful’, i.e. ‘sie taugt’ ? (Lubotsky) 

“PIE ? *d'eug"- ‘to prepare’ = LIV: 153 | Pok.: 271 

*IE COGNATES: Gr. eum ‘I prepare’, Goth. (pret.) daug ‘was useful’, NHG taugen. 


*REFERENCES: EVP: l.c.; IFL Т: 247b; IFL II: 225b; Abaev, Slovar’ I: 371 Ё; EVS: 30b f., 40 f., 88b; 
Werba 1997: 196 f.; Steblin-Kamenskij 1999: 163; Cabolov 2001: 284; ESIJa II: 405 ff.
```


## [2026-09-05T20:04:15.655Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dheugh-\\|dhugh\\|dhugh(9)ter\\|dhugh(ə)ter\" POK_01.txt | head -20"
}
```


### [2026-09-05T20:04:15.702Z] TOOL RESULT

```
3567:slav.  degz :  dgg^  ,Stärke,  Kraft,  Gelingen'  in  russ.-ksl.  djag^  , Zugriemen', russ.  djdga  , Ledergurt',  djdglyj  ,kräftig,  gesund',  djdgnuh  ,wachseu,  stark    ;, ; werden';    ablaut.    abulg.    ne-dogh    ,Krankheit'     (aber    russ.    düzij   ,stark,  ^ kräftig'   gehört  vielmehr  zu  dheugh-,  unten  S.  271);  der  Bedeutung  nach hat  wohl  eine  Vermischung  mit  slav.  teg-  ,ziehen,  spannen'  stattgefunden (Brückner  KZ.  42,  342  f.).
3878:dheugh-  ^berühren  (sich  gut  treffen),  drücken,  ausdrücken,  melken,  reichlich spendend
3881:ir.  düa7i  ,Gedicht'  (^dhughna),  dual  ,passend'  {*dhughlo-)]
```


## [2026-09-05T20:04:18.285Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3876,3900p' POK_01.txt"
}
```


### [2026-09-05T20:04:18.332Z] TOOL RESULT

```
271
grau');  mir.  do7in  ,dunkeP^  cymr.  dwnn  ^subfuscus^  aquilus',  gall.  PN  Donnos usw.  i^dhuosnos). WP.  I  843  f.,  AVH.  I  102,  386,  472  f.,  570  ff.,   Trautmann  64  f.
dheugh-  ^berühren  (sich  gut  treffen),  drücken,  ausdrücken,  melken,  reichlich spendend
Indo-iran.  *dhaugh-  ,melken'  in  ai.  duhdti,  athem.  dögdhi  ,melkt,  milcht*^, die  Wunschkuh  Kama-duh{a)  ,die  reichlich  Spendende'  (=  gr.  Tvxr^,  pers. döy,  döxtän  usw.,  apers.   han-duga  ,Proklamation'  (vgl.  lat.  pro-midgäre)  j
gr.  tvyxdvo)  (rsv^oiiai,  ervxov,  hvxrjffa,  lExvxrf^a)  ,treffen,  antreffen,  zu- fällig begegnen;  ein  Ziel  oder  einen  Zweck  erreichen;  intr.  sich  vorfinden, gerade  wobei  sein,  zufallen',  tu/?;  ,Gelingen,  Glückszufall,  Schicksal, Los',  Göttin  Tv%ri  (wohl  ursprüngl.  eine  Wunschkuh?);  ts^xw  (tsv^w,  Aor. srsv^a,  hom.  tstvasIv,  Med.  TezvyiovzOj  TSTVAsad^ai  —  mit  sek.  k  — ,  Perf. Tsrsvxojg,  TSXvArai,  tsTsvxaTai)  ,tauglich  herrichten,  verfertigen,  herstellen, veranlassen,  hervorbringen',  TixvGv.oi.iai  ,mache  zurecht,  ziele',  xsvxog  n. ,alles  Gemachte,  Gerät,  Geschirr,  Zeug,  bes.  Rüstung,  Rüstzeug,  Waffen; Schiffsgerät;  Geschirr,  Gefäß';
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
Ob  hierher  auf  Grund  eines  *dh9-ro-  ,gespitzt^  (:  ai.  dhä-ra)  auch  agg. darod  m.  ,Spieß,  Wurfspieß^,  ahd.  tart  m.  ,Spieß^,  anord.  darrad-r  m.,  darr n.  ,Spieß^?  Und  allenfalls  dazu  als  ,mit  einem  Spieße  verwunden^  weiter die  germ.  Sippe  von  as.  ags.  derian  ,verletzen,  kränken^,  ahd.  terren neben  tarörij  -en  ,schaden,  verletzen',  ags.  daru  f.  ,Schade,  Verletzung', ahd.  tara  f.  ,Verletzung' ?
```


## [2026-09-05T20:04:18.663Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=3900 && NR<=4050' POK_01.txt | grep -n \"dhugh\\|Tochter\\|277\\|276\\|278\" "
}
```


### [2026-09-05T20:04:20.195Z] TOOL RESULT

```
62:276
78:277
81:Ai.  duhltdr-  {duhitd),  av.  dugddar-,  duySar-  (aus  *dughter-),  npers. duxtar,  duxt,  arm.  (mit  s  aus  k  nach  w)  c?w5^r,  Gen.  dster,  gr.  &vy(XTr^Q (Akzentverschiebung  wie  in  iirjTr^Q,  aber  noch  dvyaTeqa  wie  (.irjzega),  osk. yii^iV;  Dat.  fu{u)trei  (Vetter  Gl.  29,  242),  got.  daühtar,  anord.  c^ö^^iV  (run. Nein.  PI.  dohtriR),  ahd.  ioÄ^er,  lit.  dukü,  -efs,  apr.  ducktij  aksl.  c^?>5<i,  -ere, toch.  A  ckäcar,  B  tkäcer  ,Tochter^ WP.  I  868,  WH.  I  557.
92:278
```


## [2026-09-05T20:04:28.109Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3970,3985p' POK_01.txt"
}
```


### [2026-09-05T20:04:28.150Z] TOOL RESULT

```
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
Ai.  duhltdr-  {duhitd),  av.  dugddar-,  duySar-  (aus  *dughter-),  npers. duxtar,  duxt,  arm.  (mit  s  aus  k  nach  w)  c?w5^r,  Gen.  dster,  gr.  &vy(XTr^Q (Akzentverschiebung  wie  in  iirjTr^Q,  aber  noch  dvyaTeqa  wie  (.irjzega),  osk. yii^iV;  Dat.  fu{u)trei  (Vetter  Gl.  29,  242),  got.  daühtar,  anord.  c^ö^^iV  (run. Nein.  PI.  dohtriR),  ahd.  ioÄ^er,  lit.  dukü,  -efs,  apr.  ducktij  aksl.  c^?>5<i,  -ere, toch.  A  ckäcar,  B  tkäcer  ,Tochter^ WP.  I  868,  WH.  I  557.
dbucn-,  dbun-  , dröhnen,  tönend
Ai.  dhvdnati  ,tÖnt,  rauscht',  dhvani-  m.  ,Laut,  Hall,  Donner,  Wort', dhvand'  m.  ^Laut,  ein  bestimmter  Wind'^  dhvanita-  n.  ,Ton,  Hall,  Donner^, dhuni-  , rauschend,  brausend,  tosend',  dhundyati  , rauscht^;
anord.  dynr  m.  ,Gedröhne',  ags.  dyne  n.  ds.,  engl.  c?m,  ahd.  tuni  ds.; anord.  dynia  (Prät.  dunda)  , dröhnen,  lärmen',  ags.  dynnan,  as.  dunnian mhd.  tünen  ,dröhnen';  germ.  Erweiterungen  davon  scheinen  anord.  dynkr ,Lärm,  Schlag',  mengl.  dunchen,  engl,  dunch  ,puffen'  und  ndd.  dunsen , dröhnen,  stampfen',  schwed.  dial.  dunsa  ,krachen,  schlagen'.
Einmischung  neuerlicher  Schallnachahmungen  kommt  für  die  germ« Worte  ebenso  wie  für  lit.  dundeti  , heftig  pochen,  dröhnen'  in  Ji'rage.
WP.  I  869.
```


## [2026-09-05T20:04:30.472Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT dav ===\" && grep -n \"duγδar\\|dugadar\\|duyodar\\|dugəda\\|duyoda\\|dug∂da\" BRT.txt | head -20; echo \"=== BRT dav- ===\"; grep -n \"^dav-\\|frada\\-\\|uzdav\\|uz-dav\" BRT.txt | head -20"
}
```


### [2026-09-05T20:04:30.546Z] TOOL RESULT

```
=== BRT dav ===
=== BRT dav- ===
7543:a.  a)  bes.  neben  Isä-  (sd.):  aj  Äv5 mazda  tzäcä  "zBitisca  yS  . .  *särjs/a  (sd.) "der,  o  M.,  -  Glück  und  Fülle  (wird  ihm), wer.."  ¥.415.5*';  —  P^ra  ..  ahmst  haca Oianhatca . .  axstat . .  iiäca  'sUitUla .  .frada- %>inca  var3da>:?mca  vaxsaifmca..V.g.^3.
13227:mit  /rä  i)  'Jemandem  (DaL)  N.  N. (Akk.)  als  Namen  (Akk.)  beilegen':  äat hl  nama  fradai^ya  ätr».dätim  (sd.)  v3  . . V.  A  52.  2)  'etwas  (Akt.)  schaffend verleihen',  von  AhM. ;  a)  mit  Dat  der  Person : tisirtm  .  .  yahiiiäi  hazavrsm  yaoxstinam frada'iap^  ahurö'^t.S.^S  (s- b).  b)  mit Gen.  der  Person:  miinm  . .  yeähe  hazan- r?in  yaoxstinqm  frada^at^'^  ahurd  Yt  70. 82  (s.  a).  3) 'hervorbringen, schaffen',  von AhM.  und  den  AmSf.:  yal  mür^m  .  . /rädaöqm  az»n  (näml.  AhM.)  äat  dim dalqm '. .  Yt.  70.  i ;  —  ana  vaca  . .  da'iat sppnts  mainyui ../rada'kitt^^  (jäm\.väcitti) avusa  sp3ida  V.  ig.  9;  —  apqm  .  .ya  para ahmät  histmta  fra^Utä  a/ratatjiusis  (sd.) ". ,  nachdem  sie  geschaffen  waten"  Yt  79. 53)  55-  ä)  mi'  praed.  Akk.  '(schaffend) bestimmen,  machen  zu  — *:  t»m  . .  i-Tspanqm sravanhqm  uparö.iairim  frada^qm  yim airyamanim  Ulm  FrW.  4.  i ;  Yt /^.  35; —  tiStrim  . .  yim  ratUm  .  .  stärqm  frada- :j<r/5>  ahurB  YtA'.44;  70.  ro3;  —  dazu ^Mi^:  fradai'i^Tla  Vt.j.i ;  — frad^htsi})  Vt 4)  '(schaffend)  bestimmen  für  — ',
17606:Ableit.  aas  /radaxSaiiä-.  —  Vgl.  /rai/ax!/aaä- —    Pü.!    langc'a  i  k  n  p  dn  n    (s.  unter  frada-
19253:•  j.  iiiiaofaar^tayae-::!!  Inf.  '(und)  Acht zu  haben  auf  — ,  zu  wachen  über  — ':  frada- hai  nmanahaa . .  hani^räila  aiwyaxitraica nipsiayaüa  'ya^a  Yt.j.6;  Y. 77.11;  — mit  Akk.:  gaihiscä  tanvaiüä  nipätayaica 'yaica  Y.5Ä  a.
25623:Menschen;  a)  im  gAvr.:  spiniahyacä n?ni  . .  yehyä  'vä  afö  kahitl  (sd.)  Y. 34.2; — yi  'vqn>m'^  »iÄ(^fl»>?(Sp.5i4m.) voAs  dadi  Aa%ra  (sd.)  manaiaha  V.  28.  4; —  iat  möi  °va  isl  (Sp.  26  o.)  caAyl avanh^  Y.50. 1 ;  —  aläunqm  Ja/  'unsyasa- maide  kudsaUaniim^t  narqm/ä  ttsirinqmeä Y.jp.  z;,;^.  i(s.bei3).  B)imjAw.:«ÄV cahmi  »awa  (sd.)  yS  rfit  °une  tatva  FrD.j; *j'';  —  ävsya  ^druzantt  .  .yS  fraurvatxH (Sp.  996  u.)  kavahe  'um  druiaite  N.  Ärf; *84^'i  —  SvBya  . .  dahäiti  .  .yaihe  d/l%rahe daiti  *ndit  *AavS  'va  ^vauräta  (Sp.  1544 u.)  N.*,^;  F.p; —  vJspfm  amm paiH sruä- mm  astanm  °va  käSayat  (sd.)  P.  J7;  — hazaiarim  .  .  datnunqm  .  .  asaya  vankuya 'uru  paraJaihyV  Ä.J.J;  V.  r^.  3;  —  /ä nS  A>nti  'une  »valm  sfari^itnca  vastnm^a Y.  55.  3;  2,  Vyt.  J2;  —  AaemS  . .  ydha kannte  vakütö  'unalia  pii%mainys.hmlf Y.g.  16;  —  havahe  °unö  haomq  ävaeaa- yamahl  Vr.  ri.  1 ;  —  xsnamaine  havakeca \°unS  Y.J. 4;  —  %at3  (sd.)  buye  vatshäu^a \miide  ..  'unai'a  darr/e  havanhe  A. 7. 11; iY.7j.11; — fravaHbyS  yä  nS  isla  'vSibyS Y.  55.  a;  —  yU  yazaite  hvan  . ,  yazaite 1  haom  °vämm  Yt.  6.  4;  —  kake  VB  'va  frä- ,yetyat  YL  /j.  50;  —  nava.»apiyai(sd.)^ij  hl I  'vätam para.itar9ncaiU  V.  13.%.  a) neben oder  im  Gegensatz  zu  tanü-  und  zu  anderen .menschlichen  Kräften  usw.:  tanval?a  *hao- sravankitn  'unalca  darrfim  havanA>m F.jh;  —  cim  .  .  qstjm  isatti  tanva  Hm °una  Aog.4S{?);  —  havaj)häi  °une  frada- 5j«  galhanqm  Y.6S.4;  —  amaheca  vin- %ra-fnahtca  'unala  damaca  spanvanti  (sd.) H.I.4; — (ha  alaonqm  a^aoninqtnca  ahümca damqmca  iaotasca  °vän?m'a  frai-ailmca yatamaidt  Y-sd.  4;  —  vUpa  gafisisca tanvasla  azdihxi^a  ustänqsia  kikrpas^a t/vlMca  baooasia  'vansmia  fravaiimh pairica  dad>mahJ. .  Y.55.  i ;  —  aläunqmca 'unasca  /ravasisca  yazamaide^.']0,Y.63.%; — aläunamia  fravaHbyS  ailwiqmi'a  'vöibyS Y.4.2;  —  vlspanqmia  ankam  O'aonqm alaoninqmla  .  .  yat/qm  *yasii%waca  'vqnö taoySsla  /ravai'ayS  Yty.  148;  ~  Aaom 'vänim  .  .  kavqm  fravalsm  yazamaide  V. 7/.  i8j  —  havahe  °und  fravalse  Y, /. 1 8.  3)  von  der  Seele  nach  dem  Tode  des Menschen;  a)  imgAw.:  kä  me  *vä  vshu *urvaxidt  *Sg?maUJ  (Sp.  497  m.)  Y.  44. 8 ;  —  a>mr>tnitT  *a!aon5  'va  alsS  (sd.)  Uta-
```


## [2026-09-05T20:04:41.059Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Tochter\" BRT.txt | head -30"
}
```


### [2026-09-05T20:04:41.108Z] TOOL RESULT

```
6915:•  ].,  g.  ahuräni-  fem,  patr.  Adj,  'von Akura  stammend,  Ahs  Tochter',  als  Bei- wort des  Wassers;  mit  GS.  aAuraAyä, °rahe:  aps  at yazamaidl tna^aintls'ä  (sd.) .  .  'ränis  akura/iyä  Y.jÄ  3'';  —  yd  vö sps  vanuhis  yazäiie  ..  'ränls  ahurahe  Y. 68. 10.  A)  als  Gottheit  des  Wassers: %ioqm  'ranim  yaiamaide  Y.  68.  6;  14;  — sonst  mit  GS.  ahurahe:  surutit^a  nS  yas- tum    'räne  (VS.)  ahurahe  Y.  68.9;  9,  i%
12357:•  j.  *tüirya.du/()ar-'>  f.  Tochter  der Vatersschwester':  yat  *taiTyB./iu^rS. .  'dujla va  para.iriiiyäH  V.  72.  17.
13200:kva  f:l  liäi^ra  (sd.)  paiti  *hinjasmte  maryS astZ'ainH  at)hvS  km'äi  urune  para.daioyi1t V,  75.  27.  3)  '(die  Tochter)  verloben', vom  Vater:  s.  paratläta-.
13645:^"fdtnäni  N   ,ro-  lies  ,arSJ.nä^  "  S-   dug»dM-,  j.   do^^r-  C  Tochter':
13657:Ubergeht,  fem  wird  dem  künftig  bleiben !  r»'irS'  oder  die  Tochter  der  Tocht«  der des  Elends  lange  Dauer  .."  Y.W.  2o'>.     I     Vate^chw«ier     aUo     'ti:.rya,Arii^^^^„
14605:•  j.  Sriti-  t  EN.  der  zweiten  Tochter Zaraiustras'^:  'lyS  asaonyä  Yt/J.  139.
16234:•  j-i  g-  pouru'dtstä-  £  EN.  der  dritten und  jüngsten  Tochter  Zara^uäras'^,  die er  dem  Jämäspa  zur  Ehe  gab**':  tsmca (B  'lä  (NS.  als  VS.)  ha&ai.aspanä  (sd.) jpitäml  y^ivfisd.)  dt^sdram  zarä^uslraAi . .  ^paityasttm  (sd.)  taibys  äai ..  V.jj.  3; —  'iayä  asaonyä  Yt/J.  139.
18294:Tochter  Zara^ttstras:  'nyi  alaonyä  Yt 13.  139.  3)75)    voa    vier    gläubigen
22394:oder  Tochter . .  zur  Ehe  gegeben  werden"
23511:I»  j.  *väri8kanä- ■'  EN.  einer  Tochter Vl/taspas:  ya^a  .  .fraourvaisaymi  kumaya
23512:Eig.  Bed.?—  '}i36S.$o.  ÜA.  varAatarufmca  ; s.dieVat.  injm4  und  Fl.  —  *)  Vgl.  lu  <W- mayä-.  Im  Sn.  fühlt  diese  Tochter  /'s  den Namen  Bihö/arJd.
27039:*)  Zu  der  Zara%Hhta  gehfirt.  Sie  heisst  SO nach  dessen  neunten  Vorfahren;  vgl.Jionid..  Die Annahme,  Sp.  sei  ein  Titel,  wird  -  an  sich  schon wenig  wahrscheinlich  -  durch  Y,  5J.  3  wider- legt, wo  PouruHstä,  eine  Tochter  ZardiMilra%, als  spitämt  beielcbnet  wird.  Zur  Genealogie vgl.  Jh.  Zor.  13,  19.
27827:*>  Ich  halte  es  fär  sicher,  dut  Zart&uSira eine  geichichtlicbe  PersöoUcbkeiE  ist,  sowie  dass die  Gä%äs  im  wesentlichen  auf  ihn  lurückgehen. TiELB  GeschRelAIt.'  3.  275  CTklärt  mit  Recht den  Zar.  des  jüngeren  Awesla  (ül  "eine  vSIlig mflhische  Person",  aber  dnss  er  «chon  in  den Gä%äs  "eine  legendarischc  Penon"  sei,  mnss ich  ihm  bestreiten.  Ich  finde  vielmehr,  dass er  uns  hier  darcba,as  körperlich  nnd  meaichlich entgegenicitt.  Sein  Reformationswcrli  ist  noch in  den  ersten  Anlangen  begriffen.  Nur  ent wenige  einflussreiche  Männer  sind  dafür  ge- wonnen, nm  es  aU  Soosyanl  {lA.)  zu  nnterstütien : SD  ausser  dem  Sohn  Iial.väslra{i.  lara^tütray- a) nnd  dem  Vitersbruder /ftiiyöt.m^wAa  inibeson- dere der  Fürst  yäiäipa,  sodann  Jämäiftt,  dessen Minister,  und  Fralaoslra,  deren  beider  Interesse durch  Knüpfung  verwandtschaftlicher  Bande  ge- festigt, wird  -  Zar,  beiratet  Frai.z  Tochter  und gibt  Jim.  seine  jüngste  Tochter  ßimraaslä lar  Ehe  -,  femer  der  TKrer  Fryäna-  (s.  Ntr.}. Auf  der  andern  Seite  setzen  die  den  alten Göttern  iäana-)  wie  Mi^ra,  Haoma  usw.  und ihrem  Kult  treu  bleibenden  Fürsten  {kaii)^-, säslar-)  nnd  Priesler-Lehrer  [kivapan;  uäg-')  wie Bindva,  Grlhma  dem  Neuerer  heftigen  Wider- sland entgegen,  lo  dass  er  häufig  genug  in  bittere Klagen  Bosbrieht  und  der  Besorgnis  Ausdruck gibt,  ob  er  seine  Mission  werde  fortfuhren  können (vgl.  iB.  Y.  46.  i).  Beieichnend  ßr  die  ■Wirk- lichkeit der  Verhältnisse,  unter  denen  die  (7ü^s entstanden  sind,  ist  die  Strophe  Y.Jf.  iz.  Haite ich  sonach  an  Zar.  als  historischer  Figur  durch- aus fest,  so  sehe  ich  doch  anderseits  jeden  Ver- such, die  Zeit  seines  Auftretens  genauer  zu  be- stimmen, für  aussichtslos  an.  Nach  der  heimischen Chronologie  (s.  West  SBE.  47.  xxvm)  würde Zar.%  Geburt  in  das  Jahr  660  v.  Chr.  fallen, und  Jh.  Zor.  174  hält  das  für  wesentlich treffend :  "the  period  . .  just  before  the  Achae- menian  power  [is]  the  approximate  date  of Zoroaster's  life".  Ich  glaube,  wir  werden  wesent- lich weiter  zurückzugreifen  haben,  und  urteile über  Jn.s  Ausführungen  wie  Tiele  GeschRelAlt.> 2.275,430.  Einer  Chronologie,  die  damit  rechnet, dass  ein  Lehrer  des  Glaubens,  der  als  erster 100  Schüler  um  sich  versammelte  (s.  ^sarna-\ 100  Jahre  nach  der  ersten  Verkündigung  der neuen  Lehre  geboren  wird  und  100  Jahre  att stirbt,  kann  ich  kein  Vertrauen  schenken.  S.  auch No.  I  zu  vüläspa-.  —  Die  Angabe,  Zar.  sei  im Weslen  von  Irin  geboren  (s.  rayay-),  ist  mit  der Tatsache,  das«  alle  entscheidenden  Stellen  de* Awesta  (insbes.  Yt.  ig.  66  f.)  auf  Entstehung  im Osten,  in  der  Gegend  des  //äiniinsees  hinweisen, keineswegs  unvereinbar.  Es  lisst  sieb  sehr  wohl begreifen,  dass  der  Reformator  seine  Heimat verlies!,  weil  er  keinen  Anklang  fand,  oder  auch verlassen  musite.  So  mag  sich  auch  seine  starke Betonung  wirtschaftlicher  Giundsätie  (s.  väilrya-) erklären.  Der  Westen  Irans  stand  zweifellos auf  einer  wirtschaftlich  wesentlich  höheren  Stufe als  der  Osten,   wo  man  sich  noch  lange   nicht
30213:Pourucislä,  die  jüngste  Tochter  Zara%uilras\
30435:•  j.  'hu'mäyä-,  "hu'mayä-  f.  EN.  einer Tochter  Vl/täspas:  tarn  yazata  ..  visiäipS .  .  dazdi  ml  .  .  ya'ha  .  .  uta  azfm fraourvaaayeni  'maya  (IS.)  *värioJianqm (sd.)  hyaonya  haca  daiAAävs  ".  .  und dass  ich  wieder  heimbringe  sammt  der H.  die  V..."  Ytp.  29ff.'>;  —  'mayä (GS.)  aSaonyi  Yt/J.  139.
30565:•  j.  'hu-äyaoSna-,  g.  hu-syaoS^na-  Adj. (fem.  •nä-)  i)  jAw."  'des  Tun  gut  ist': yvamm  humanaraA^m  (sd.,  auch  fdSt.) h%-alat»h>m  °%mm  hudaimm  Vr.^.  3;  — ySttB  . .  '"knaAe  H.  2.  1 8,  Vyt.  ij  \  —  yünat haca  .  .  °^nai  P.JSi  —  ^'""  •  ■  ''"^"^ H.  2.  II,  12;  —  kaxaye  .  .  '%nanhe  Yt, ^9-  95-  2)  gAw.  'wohlwirkend,  guttätig": at  köi  dtigidä  °^anä  ärmaiiis  "sbei  seine Tochter  ist  die  guttätige -fr»«."  ¥.45. 4.
```


## [2026-09-05T20:04:42.708Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"azarama\\|zarama\\|zar\\?ma\\|dugda\\|duyda\\|Bagaduxt\\|baya\\-duy\" BRT.txt | head -30"
}
```


### [2026-09-05T20:04:42.771Z] TOOL RESULT

```
2460:—  afyö  räläbyö  saoirälyö  .  .  yasatrm  io.T^i.;—gunäö ..aitihli gumiay3i{fiA.)\. yazamaiäeY.16. 1 ;  —  shü^  at  paitl  adähü  ^.j,z',~~vät»m  ..atihä  viltay^ /rinnta\i.2. ..büiricä  k>r»hia  xrapaitl (sd.)  ..  Ayat..  g;  —  zugleichauf ein  Relativiim  als  dessen "bei  diesen  Heimzablungea  jetzt  . ."  Y,  1  Korrelat  vorausweisend :  flt^aw^(7»i..(7S'^m 40.1''.  a)  mit  einem  aläMteradea  amanAam  ..ya£/am  tß  ..  irixb/n(sd.)..  V. oder  ergänzenden  Relativ:  ai^/a  at»hsus\^2.'j.  aa)  Der  Begriff  ist  zwar  zuvor yB  astvatS  yasca   asti  manahyö  Y.  57.25;  nicht  ausdrucklich  genannt,  hat  aber  dem
2469:—  lia  yaoilayö  .  .  ärmalayö  vatiuhxm iibls  ahm  . .  yazamaidl  ". .  sammt  denen die  gute  A.  .  ."  \.^8.2;  —  ttm  yaz>nia kainina  . .  äa>al  aibyasHt  (DPf.)  tat  avat •lyaftim  YL/j.41;  —  Hwqm  iaininö  .  . "iwam  earilitis  . .  jaioyante  . .  tum  tä aiibyö^  nisirinaväki  Yt.  5. 87 ;  —  mit  Nu- merus Wechsel**:  yeii  arskat  anästUtS  vä anaiwijravanS  (sd.)  v3  dalnqm  aitäeit aäbyS   *s^aaAaiti   3stavanalil>yS  V.J.  40;
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
2923:•  Jt  g.  ao5ista-  Adj.  (fem.  °ta-)  "der  stärkste ; sehr  stark':  uyranqm  °to  Yt  ig.  38;  — iCfrpm  'um  bavähi  Az.j;  —  w/ra  ^aja- maide  'tä  {/ravasayd)  yazamaide  Yt  y. 75;  —  •/a«tfM  «A'  'Um  (statt  NS.)  Yt /Q.141; —  hitqnt  Avö  °tö  Y.29.3;  5.15, 'N't  10,98;  —  srao-hm  ,  ,  yünam  'tim  Y. ,T7-'3i  —  f ravasayd  . .  yä  °ta  vazintqm \x,  13.  a6;  17;  —  yei  hyqn  *asti.aoJaT?ha (sd.)  'ta  YtÄss; —  k»m  'ta  mahrka.. Oi'sd  (sd.)  yaxäite  V.  //.  2.  a)  ASn.  -tim als  Adv, ;  'bmca  . .  vaRiye,t»napiea  (sd.)  V. 3.30.
3446:et':  at  hama  at  z<^eney.,l6.\o.  B)  in andrei  Stellung;  I)  hinter  dem  ersten  (hoch- betonten) Wort  des  Satzes^',  a)  zur  Her- vorhebung: sptniitn  at  %iDa  .  .  mSngAX  Y. 43.$;  —  sraistam  at  töi  kihrpsm  ..  ävalda- yamahl  Y.36.6;  3~-4,  3^.3;  — %wqm  at ..  paity3stäriimcä{%A.)  ..  dadsmaidl  \.3^. 9;  —  tsm  al  ..yazamaidl  y.3y,2,  y,  3§. 3,  7j  —  huxsalirS.t3mai  (sd.)  *63  *ap^ . . äad»mahilä  Y._jj.5;  A._j.6; —  ahttrahya ii  al    .  .   yasn?m    .  .    am^Amaidl    Y.  3^.
3457:•  j.  at-tävaxiyä-  fem.  Adj.  'die  Worte  a/ tJ  vaxsyä  enthaltend,  damit  beginnend': 'yqm  Aäitim (sd.)'^  yazamaide  Y.jo.  la;  — ••ya  häitis'''  Y.30  Überschr.
3461:•  j.  at.fravax5yä-  fem.  Adj.  'die  Worte atfravaxlyä  enthaltend,  damit  beginnend': -yqm    kaittm  (sd.)'*  yazamaide  V.4^5. 12;
3464:•  j.  at.mäyavä-  fem.  Adj.  'die  Worte  at mä  yavil  enthaltend,  damit  beginnend': °vqm    Aäitrrn  (sd.)"  yazamaide   Y.4r).\y,
3675:•  j.  apänk-  :  apak-  Adj.  (fem.  apacl-)  'nach hinten,  rückwärts  gewendet':  "^//(NSf)" vazaili  arstiS  yqm  . .  "rückwärts  fliegt  die Lanze,  die  . ."  Yt.  10.  ao.  a)  NSm. als  Adv.'>:  °Pq^  ^avS  damayäti  "nach hinten  (auf  den  Rücken)  fesselt  er  ihre Hände"  Vt.70. 48.  b)  IS.  als  Adv. 'zurück': *'pasa^'>  vi  *zamar?  ana  duye*  {%A.)\i.i. 2g;  —  uzg?r>pt3mHt  saa'^pm  -pasa  apa.- j^anvainti  (sd^  Yt  14.46.
4153:künftige  (jenseitige)  Leben':  disyäl  aAmai naire  oval  mlzd>m  parS.asn3i  °fguhe  vazd- fary  vahistahe  omAsusV. p. 44;  ij.8,  Y.55. a,  A.3.7.  d)  s.  zu  A  1  d.  3)  mit  a) vaAista-  Adj.,  b)  acisla-  Adj.;  a)  'das  beste Sein,  Dasein,  Leben;  Ort  des  besten  Daseins, Paiadies':  vahisfym  'hüm  asaonam  raoca- wAbb  (Stverz.)  vIspB.ci^iJ^rjm'^.g.iii  usw.; S./.a?;  —  nöithl. .  bi-at. .  vaAi/tJ  '»Aus ySmanayat  ahurahe  masdä  oval  vispanqm *aastpm  (sd.)  .  .  yat  srrfoi  daoiarihum P.  40, ;  Y,  (to.  1 1 ;  —  as^m  yS  ahurS .  .  aoi urune  uri'äsma  (sd.)  dalsayeni  vakUtimca 'hüm  P.  3S;  V. /<?.  2  9 ;  —  vazdvar»  vahisiahe 'ai^is  V.  5. 44;  —  vahistajtSs>m  (sd.) TohUtahe  'riASusV.  1S.6;  —  tarS p^r^tümcit hl  urvänmt  vahisl^m  'ham  fraparaymi  .  . it  vahistät  'tihapt  Y.  if),6;  7;  —  i'lsp^m asmanpm  vahtst^m  3  °hüm  baraiti'S.24; V.7.S2,  '^f^. 3.1"^;— vahistahe  'vASu^ vahistqm  ayanqm  yazamatde  Vr.  7. 2 ;  — yatJrS  paurrd  usshistaiti  paräiti  vahistahe •w>i7»/V.;Ä26;5.6i,Y.7/.i6,YLy.i34. P. 4:9;  —  vahislai  •r^heYyi.33;  —  ia^ä 'uhSuS  vaAistahyS  paourvJm  ku%S  (sd.) Y.  44. 3.  b)  'das  schlechteste  Sein,  Da- sein, Leben;  Ort  des  schlechtesten  Seins, HöUe':  vTspa  humaia  ..  vaAistpm*°tAlim"'' *asaiti  vispa  dusmala  acisl^m  *'ijhüm"^ *asaüt  FrW.  3. 2 ;  — ya^ääl  anhat  apsniim (sd.)  '»Aus  aaslS  ärygt'atqm  at  asäum vakistim  manö  Y.30. 4 ;  —  avi  lim  spayüt. . t)mS  .  .  äca  aastpm  äla  'hüm  ä  V.J. 35;
4606:asahe  ratäm  Y.2.8;  —  'mSahai'^  Y.1.8; —  •mämAäsca  ■'  (als  AP.)  p»ntü!.mär»häsca .  .  yazamaide  Yt  7.4.
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
5727:Gottheit  (i'asa/o):  'smaium  yazamaide  zqm hu'iatfhiin  yazatim ..  Y.  16.  6;  —  'smaugm :^anvaiil3m  yazamaide  S.  2.17;  —  tqm'ä 'smamm^ä  yazamaidi\.42.y,  —  s.  noch Y.  7. 16   und  A  a.  A  a)    avig  (näml.
5815:•  j.  a-st9n»ta-  Adj.  'nicht  niederzuwerfen': 'taca  amuyamna  yazamaide  Vr.  7.  i.
5847:•  j.  a*Sp^-  Adj.  'nutzbringend':  'pjnäcd (als  APm.)  ypvlftff  \.42.2;  —  ßaonTm Tq'iwqm  .,  *'panilai''>  ypvtnö  yazamaide S.  2. 7;  — ßaoiiibya  (sd.)  va'iiwaiya  *°pani- fya'^'>  yaffmöya  8,7.7.
5989:•  j.  a-zarama-  Adj.  (fem,  'mä-)  'nicht
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
6189:Gen.  subj.  und  obj.:  alsm  *d>nidyäi{iA.) .  .  rayS  'st/  ". .  jrXoiiTOU  fioi'pai"  Y.  4J.  i ; —  abifra  (sd.) . .  ya  vaahsus  'sis  mananha Y._3i5.i3;  —  aiahya  yasa  {%A:)  'slm  y am iiyam  Y.  54.1;  —  °M/a  ^ae^ananqm viäu/(sd.)  ahurakya  mazdS  ".  .  des  AhM. Belohnungen  fiir  die  Taten  . ."  Y.2<V,4; — ■  nöit  kl  "M  *^ao^nanqm  vimysit  N. 16  ij);  —  zard>!ustrahe  .  .  asatinS  'itmia fravaiimca  yazamatde  Vr.  16. 2 ;  2,  Yt  13. 95;  —  tti  ahmt  nmane  Jamyarps  yh  asao- nqm  xshätas/a  'sayasca  . .  paitisatitayasla Y.  60. 2.  a)  mit  vanAav-  Adj.  und  aka^ Adj.  näher  bestimmt:  vatfkttyascä  °Ssi/ .. yS  ns  ara^ä  (sd.)  irmavaia^a  asanhäxs ^■5^-3't  —  syao^ana  mizdavqn  (sd.)  .. akfm  akai  vamthlm  'stm  vanhaavi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya  ahm  vaaAuya 'st  gaui  (sd)  Y.5/.  10«;  —  xmBth  afn- n>ntu  ahmya  nmsne  vawtklm  °/lm  i^a- parqm  Yt.  /J. i  S 7 ;  —  vaauAlsca  aöa  vaau- klsca  'sayS  Y.53.3;  —  yhca  tsi  gmh *aiura.mazda  ..  iSä  . .  vanukim  iihl/  'lim . .  ihm  .  .  *panndlm  yazamaidi  Y.^S. if  b)  Du.  'die  beiden,  beiderlei  Lose', d.  i.  (das)  gute  und  (das)  böse:  tmnanha (sd.) y5  dä%alibyd  priLratüm  xsayqs  'äfä*"^ üista  ". .,  der  über  beiderlei  Lose  gebietend den  Klugen  den  wahren  Ratav  versprochen hat"  Y.57.5.  A)  als  Gottheit,  die  die Lose,  insbesondere  die  guten  verteilt,  im jAw.  als  Göttin  des  durch  Frömmigkeit  ver- dienten Wohlstands*';  I)  im  gAw,:  Siraosö 'sfi  mqza.raya  (sd.)  Aacimnif  ya  vT  altl *ran3ibya  savlfi(sd.)  vldayäi  \ .  4j.  1 2 ; -^ sraosS  .  .  yU  *'li^  haiaiti  *mqxaraya  V. 27.6,  Vr. /2.1;  —  ya  vldayaf  'sts' (HS.) räshqm  (sd.)  Y.j^.  la;  —  ys  fta  'sSis aojaifha  var>dayaita  yqm  ,  .  gai^qm  .  . Y.  so.  3.  a)  Du,  in  Verbindung  mit armaiay-  Du.  ^A.  und  Arm.':  yads  ahm zivlm  (sd.)  .  ,  mazdasca  .  .  'sicil  armaitl Y.31.^.  II)  im  jAw.:  yö  'lim  yazäite ..k5  mihnm  yazaiieY\..i-j.2;  —  -/j  (VS.) srlre  'si  banumaili  .  .  °li  dä'ire  vehäm i^arifiilYt.sy.^;  6of.*;  —  hm  hacSl  'Hl pourvsj^ä'iira'Yt  /j?.54;  — /rä  mqm  aiwt.- urvalsayatfuha  marsdik?m  'al  (als  VS.) hnzaiti  Yl  77. 1 5 ;  —  'lim  . .  darr/S.- variiman3m..bartntltn  vispä  baSlazsY.S'i. 2;  —  sraohmla  'lim  nairXmca  sauh>m IVyt.40;   —  fravalays   .  .    'Isil  balsaza
6427:•  j.  asiä.hak-  Adj.  'der  Asay  anhängend, ergeben':  tDttß . .  'JiSgit  (NSn.)  Srmaili/.- hägtt  Y.  $8- 1-  a)  NSn.  'kägst  als  Adv. 'in  Ergebenheit  gegen  A':  vTspaica  alte 'hsgst  ärmaitii.hägft  (zbayemify  yazama- daEca  "und  all  diese  (rufe  ich  an)  in  Er- gebenheit gegen  A.  und  Ä.,  und  wir  beten sie  an"  Y.  -]!.  ii.
6780:•  j.  a-huta-  Adj,  'nicht  ausgepresst',  vom ,  '^"'  "■  •  das  was  unter  den  G.  den  ^Ä. Haoma:  mit  haomö  hul5  axtis  .  .  nöit  enthält  .  ."  ti.46;  —  'z-aiffm  g.l>qm  V. *nasus.ava.hrjiö  (sA.)  ava  alte  ahuia yaiia  34-I-6,  Vr.2.7,  14.0,  Vd./2;  —  'i-ai/yä ?a%wars  anzavB  Y.6.^3.  S''^>aya  hatidstä  yazamaide  \. 34.16,  Vr.
6801:yät K.4.%;  ■''N.  (iS;  —  'nahe  vairyehe  asaya frasrütahe  Y.27.7,  Vr.72.2;  7,4,  2.6,  Y. 7p.  2 1 ;  —  'nahe  vairyehe  arsuxoahe  växs y.^.i;  Vr.  70.2;  —  'nanqm  vairyanqm N.  702;  —  'n^m  vairlm  yazamaide  Y.  13. 8;  7.26,  61,1,  Vr.74.3;  —  'nJ  vairyS vacqm  j'irUrajqst^mäYl.  il.y,  —  sraohm .  .  yeAlie  'ns  vairyg  snatiis  vuata  Y.  57. 22;  — jainti   mqm   'na    vairy.
6860:'rS  maaiä y7  mazistJ yjzatanqm yJ  vaAi^^  yt,i^.  ^T  \t%v.;  —  cattt  alte  mi^ra  tava  yit yazatanqm  Yt.J7.16; —  °r>m  tnazäqm  ..'.°ra  ma3äaV.4-3;  —  ahm  äuyoarfm 'rahe hudanfam  mazishm  yjzalim  yim  sjvisi?iH  \  mazdii  3^ai>karpm  ain>sanqm  spmtanam /rädat^ali:}m  dätänmvohunam  damanqm\'^K.i-j.z;  16,  V.  79.  13;  —  us  mg  fita \,  16.  i;  —  nh'afiayemi..daiusj(StvcTZ.)iAaomäi  draond  frSnnaoi  °rS  mazdh  ..  V. °rahe  mazdä  ralvatS  c^annarmAalS  (Sl-  /j,  4;  —  astvatintä  .  .  asts  mazda  °rahe verz.)  mazistahe'a  vahistahe^a  sralHahecaYlx.ig.f)-i;  I3.\\f>,  V./(7.34;  —  buyama xraoMistake'a  xraiwistaheÜa  kukinpttma- ,  'rahe  mazda  frya  väsiita  astayJ  (sd.)  V, he'a  aSät  apanSJtmahe'a  hwiHmanS  vouru.- 1  70. 4;  —  haomö  . .  zaota  °räi  (statt  Gen.) ra/na»/i^  y7  nS  daöa  yd  lata^aylltu^ruy?\mazdai  Vty.88f.;  —  ySs^a  t!  y?na  'ra yj  mainyus  ipmtSJimB  V.  /.  i ;  usw. ;  —  mazda  Vr.  7.  4 ;  —  fravasTm  avqm  yqm pQuru^ar)na)3ha  'ra  mazda  VyL  2^^;  —  °raAe  mazdä  Y.  26.  2;V. 1^.14;  —  vXsp»mca °raki  mazdh  ..  STvUtah!  \.  56.  1;  — ^k^rs/s  'rahe  mazdä  Y.ji,^; —  ««  'rahe ax^aßis  ahi  abai>hJ!  tum  yS  °rD  maxdä  1  mazda  yazamaide  dar?ir3i  (sd.)  mq^rahtr V,  jp.  20;  —  'rät  mazält  .  .  vpr/irayne ■  sp^ntaAe  xralüm  'rahe  masdi  ..  marjirrüi frädat^aliai  yat  huxla'iräi  .  .  ratu-l..  hievam  ° rahe  matdä  . .  fravSkäi  .  .  Yt. xla%rai  Vr.ll.i;  —  huxsa'irSJ^mli.'if  1.2%;  —  gayehe  marP^nS  .  .  yS  paoiryd at  xsa'ir?m  eiyJt  yat  'rät  masdäi  A.^.  °räi  (stitt  Gen.)  mazdJi  manlscä  *git/ta 6;  s.  Y.J5.5;  —  'rät  masdäi  fanhavl  säsnasca  Yt./_J.87;  Y.jp.14;  —  nazdys vohumaill  Y.  I2.\;  "V,  tg.  11;  —  vaAists\ahmi  az>m  (Stverz.,  unter  3)  yö  'rS 'ra  mazda  Y.  /p.  1 5 ;  —  xsayat?  "rahe  I  mazda  vispahe  aukSul .  .  ya^a  .  .  P.  2(.?; mazda  YX.13.-jZ;  —  ise  ^wqm  'ra  mazda ..\  usw.;  Vyt.j^';  —  pascasta  azim  ya  'rS aoaoyf  ahi  a'iaoyS.xratul ..vTsps.viwS  Yi.'mazdil  aoi  urune  urväsma  (sd.)  dassayeni /2,  i;  70.  III,  V.  ig.  20,  a6,  Vr.jp.  i;  — Ivahi/ipmea  ahüm  .  .  V.38;  Y.ig.6,  7;  — °rJ  mazda  hvapis  Yt  5.  85;  Y.  7/.  10  (wo  vasas^a  tu  'ra  mazda  . .  x/ag/a  havanqm ab  Vok.) ;  —  'ra  mazda  mainyl  spinUta  1  däinanqm  Y.  Ä*.  5 ;  —  imat  dqma  yat  "rahe dätar?  gai^anqm  astvaitinqm  asäum  {^\.-\  mazdh  V.jy.14,  17,  34;  Vyt  20,  Vd.  i, verz.,  unter  I  2  a.);  usw.;  —  tsm  bay?m\YX.i(f.iZ,\.22.Z;  —  irrj/^/^-rJ (statt Vok.) t)m  ratüm  ,  .yim  'ram  mazdqm  daovätih?m  \  mazdä  vanuhti  dämqn  .  .  yazamaide  yäü i^t^vcz)  rapant3mtarh'a»h?mt'üpa*voh[i^dadä'ia  pouruca  vanhuia  Y.  7;.  10;  ;.  1, Y.70.1;  usw.;  fo.  9;  —  'rim  mazdqm\  12.  7, Yt  ig.  10,  58,V.  21. 4;  —  azmi  daoqm mainyaem  mainyavanqm  dämanqm  main-...tistrim..ya'ia  mqmcit  yim  'nm  mazdam yaoyä  stSts  ahUm;a  ratümca  Vr.  2.  4;  7,IVlÄ'.5o;  —  ttstrlm  .  .  yahmäi  hazaitnm ^'■57-4j  —  allat  dim  vlspanqm  mazih?m\yaoxstinqm  fradd^at  °rS  mazda  Yt^.45; dazdyäi  (sd.)  ahUm^a  ratUmca  yim  °r}m\iQ.Z%; —  tistrim  ..yim  ratüm  frada'hat masdqm  Y.  27.  i;  Vr.  /;.  21;  —  imimca'  'ro  mazdä  YL<?.  44;  5-  89,  70.103,^5.35; isi"^ rahe paitim ..yim  'rsm  mazdqmY.2.i6;\  —  arpdvjm  . . yeiihe  ca'^wärB  arSäna  ham.- 13.1,  ^.I03{?);  —  ySvaram  °rS  mazdä ..^tlsaX  'rJ  mazdä  Yt. 5.120;  —  ya'ia  vs tä  varmScä  .  .  ahmi  Y.12.  7;  —  mi^rpm  '  'rS  mazdä  fradaiim  haxsat  F.  ^Ib;  —  tä ..yim  yazata  'rS  mazdä  raoxsnlt  paiti  (frava^ayS)  ii3..'ä^rayente  ..aomna  'ra{lS^ gars  nmänlt  Yt.  10.12s;  5- '7!    —    avi\  mazda  Yt  13. 146;  S.7,  $&;  —  äyaptj/r.
6871:Am?l'a  (^tvm.,va.ttx A. R-a.)  Sp^nta:  rumas» ts  'ra  mazda  ,  .  rumS  vS  amiiä  spsntä  . . allal  *jih<tt  'r)m  mazdqm  astat  am»si spjnts  Ny.  1. 1;  Y.  68.22;  usw.  b)  im Gegensatz  zu  A/jra(sd.)Mainyav:  xihae- ^ra  "rahe  mazdh  laröidtti  anrahe  main- ySus  Yt./.o;  —  sna>ai  attrahe  maittySuL. /rada%äi  'rahe  mazdiY.2-j.\(.  2  K)aAu- rahe  ma-id?!  (näml.  ayarg)  heisst  der  i. Monatstag:  'rahe  mazda  raivatS..  S,/,i, Y.j.  ii;vgL/6:i,S.2. 1.  3)inGHapt.; 'ra-  ist  einmal  Ci-3S-l)  von  mazdäh-  ge- trennt, sonst  steht  es  unmittelbar  davor oder  dahinter:  huxsa'irS.timüi  ..  xla'hnm .  .  *hvqnmahicii  kyat  mazdäi  'rat  Y.J5. S;  s.  A,_j.  6;  —  mazdil  'rä  . .  kätqm  hu- dsslfmä  \.4i.  2, 4;  —  'rä  mazda.. vaahuda YjA'.4;—  vohü  xsa'hr»m  tsi  mazdä  'rä apaSmä  Y.^/.  a;  —  sralstqm  at  tSi  k»hr- pSm  .  .  ävaSdayamahJ  masdä  'rä  . .  avat yät  hvar!  aväcl  V.j6.6;  — yäsctJ  tsi gmä  *'ra.mazdä^''>  Y.  j8.  i;  ^5.  3,  9;  — hyat  mizdjm  *mafai^im  (sd.)  Jradadfiä .  .  masdä  'rä  V.40.  i;  i,  4;  —  läa  äl yazamaide  'rtm  mazdqm  y}  gqmlä  ahmiä dat..  Y.3-J.  i;  —  BitJ  yä  v3  ..  '1^  mazdh *nämqm  dadät  ..  Y.  ^JÄ  4;  —  dätdl  a/.. mazdä  'rä  . .  västryJng .  .  akmaj-afonat>hs (sd.)  Y,  4a.  3;  —  ya^ä  tu  l  *'ra.mazdä^^ minghäcä  .  .yä  vohü  diä  tSi  dadunahi . . a^ä  iiSidyämahl  ^wä  mazdä  'rä  Y.yp.4; j6.  5,  I ;  —  'rakyä  :l  at  vi  mazda  yas- n»mcä  .  .  amSAmaidt  . .  Y.J5. 7;  —  ^wDi staotarascä  ..  ^''ra.mazdä"'^  aggitnadailä  .. Y. 41.%;  —  ätari  vSi (sd.)  mazdä  'rahyä ahi  Y.J6.3; — äiar^  mazdä  akurahyäY. 36.1,  3.  a)  in  Verbindung  mit  n)  Asa (sd,,  unter  A  1  a)  und  ß)  Asa  (sd.,  unter A  1  0,  VohuManah  ua.:  a)  *'ra.mazdä"'^ d/ä  srTrä  Y.  J^.  $;  — stets  garS  vahmSrtg 'rät  mazdäi  asäicä  vahiääi  dadtmahicä Y.  41.  I ;  _95.  s;  —  mazdä  'rä  .  .  iava/ä sar)iit  asaliyäcä  Y.  41. 5  f. ;  40.  i  f.  ß)  yaza- maide 'rillt  mazdqm  . .  ahm  ..  vahislmt  .. 7ighucä  inanö  . .  vohttcä  xiäi^rim  . .  Y.  ^-j. I— 5-  4)  im  gAw.  (ausser  GHapt,), Es  sind  hier  die  Strophen  herangezogen, die  ^ahura-  und  'mazdäh-  im  gleichen Kasus  enthalten;  s.  dagegen  I  z.  Die Stellung  der  Wörter  ist:  ah'..m',  m'..ah' (in  beiden  Fällen  ist  die  Trennung  oft erheblich);  m°  ah",  ah' m'  (im  letzten  Fall trifft  stets  die  Zäsur  dazwischen:  Y.  2^.  9,
6915:•  ].,  g.  ahuräni-  fem,  patr.  Adj,  'von Akura  stammend,  Ahs  Tochter',  als  Bei- wort des  Wassers;  mit  GS.  aAuraAyä, °rahe:  aps  at yazamaidl tna^aintls'ä  (sd.) .  .  'ränis  akura/iyä  Y.jÄ  3'';  —  yd  vö sps  vanuhis  yazäiie  ..  'ränls  ahurahe  Y. 68. 10.  A)  als  Gottheit  des  Wassers: %ioqm  'ranim  yaiamaide  Y.  68.  6;  14;  — sonst  mit  GS.  ahurahe:  surutit^a  nS  yas- tum    'räne  (VS.)  ahurahe  Y.  68.9;  9,  i%
6958:•  j.  ahyäsä-"  fem.  Adj,  'die  Worte  ahyä '  •  j.  a-x'^sa-  n.  'Nichtessen':  s^älaya  vispö yäsä    enthaltend,    damit    beginnend':    'ia  '  afvhtts  .  .  jvaiti  "se  fi-amiryeite  V.^.33. Äaiii/ (sd.)'i   Y.  2<S'  Überschr.;    —    'sqm       Fa.:  Aa^  ax'arü-  - AaUlm  yazamaide  V,  a.S' is,
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surunvaiH N.  26;  60,  _jtV,  3Q,  iV(V,  g6,  100,  101, 104, 105,  54*>,  26  aSt.*',  (J5'>,  97S>; — yu  nBit öim  .  .  vääm  *aiwy<Is  . .  yezi  S°  öyum.pe väcim  *aiwyas  anaiwisH  (sd.)  .  .  N.  74; IQ.  4)  zur  Anknüpfung  eines  begrün- denden oder  erläuternden  Satzes  'denn; nämlich';  minyö  yö  parö.dari  .  ,  ä°  hS msrrfS  väcim  baraiti  Y.iS.i^;  —  sasta he  .  .  /rasnsoay^n  ä°  yat  he  zasta  mit framata  äat  (s.  7)  ,.  V.  1^.40;  —  mä  äi barg  (sd.)  agvS  yat  irisUm  ä°  yezi  sS  barai aivö ..  V.5.14.  5)  in  Säuen,  die  eine Aufforderung  oder  Wülensäusserung  ent- halten, 'so  .  .  denn',  oder  unübersetzbar: a°  mS  ahe  .  .  paräca  vaepaya  Y.  /o.  12; ra,  Yt5,77;  —  ä°  tum  ,.  nava  rnaya ni^wjnsöis  Y.iO.iS;  22.2,  9;  —  3°  vS kascil  .  .  isalta  Yt/5.53;  —  ä°  tbaHä taurvayeni  Yt. /4-4;  —  a° .  .yasami  Yt^. '3o>  131;  —  ä°  dis  avaioayamahi  Y. 4.aff.,  24.Z,  5.  55-^^  Yt.ii.i6,  ai;  ^.5, 11.31.  a)  hinter  dem  ersten  Wort  des Satzes:  imqm  ä'  sqm  .  .  yazamaidiY.^H. 1 ;  gg.  1 ,  a ;  —  alahya  a°  sairl  .  .  ädä (sd.)  Y.  JJ.8;  —  aZsmanqmat  3°  .  .  /ra- näsayata  A.  j,  s^  b)  in  anderer  Stellung: paoirlm  upa  may>m  haktrit  äpö  ä° kvqm  tanüm  pairtyaozdai'^Tia  V.p.31; 31.  6)  hinter  dem  Pron.  interrog.  wie
7137:werden  in  der  Theologie  fünf  Arten  von Feuer  geschieden;  s.  unter  den  einzelnen Adj.:  °tr>m  b3r3zisavat3h3m..vohu.fryämm . .  urvOzist^m  (s.  A  und  2)  . .  väzist^m  (s.  A und  2)..  j/7«/i"ö/n  V. /7.11;  V.  75.40,  Yt 7J.85.  A)  als  Gottheit  (Vazata;  s.  aber Y.7.2)"':  tumas}  ti  °tars  .  ..huiiH  mazi^ta ^a;o/flNy.5.4;  V.51V.  7; — '7ire..yaltusl)mäi aiiinsanqm  spmtanqm  Y. /.  2;  —  a  html 'hnm  gärayemi  .  .  zaohraSyS  Any.  2^;  — hwqm  'tnm  akurahe  inazda  pu^rpm  asa- vamm  asahe  ratam  .  .  vtspe  "tarS  (AP.) yazamaidey.ss.T,  J'-io,  S. 2. 9,  Vyt, 26(?) ;
7199:•  j.  ahyasa-"  fem.  Adj.  'die  Worte  ahyä yäsä  enthaltend,  damit  beginnend':  "sa Aaitir  {sd.)'<  y.  2A'  Überschr.;  —  's^m Aainm  yazamaide  Y.  2iV.  1 2.
7264:12,  Yt5.77;  —  ä'  tum  ..  nava  maya ni^wprtsjis  V.  10.18;  22.2,  9;  —  ä'  vS kasUl  ..  isalta  Yt/().53;  —  ä'  liaeiä taurvayeni  VtJ4.4;  —  ä°  .  .yäsami  Yt5, 130,  131;  —  ä'  dls  ävai'jayatnahi  Y, 4-iS.,  24.3,  5-  55-^'  Vi.n.16,  21;  3.5, 11.21.  a)  hinter  dem  ersten  Wort  des Satzes:  imqm  ä"  zqm  .  .  yazamaideX.^H. i;  Jp.  I,  2;  —  asahyH  W  satrT  .  .  ädä (sd.)  Y.  j!5.8;  —  alsmanamal  ä°  .  .  frä- näsayala  A.  3.  5 ".  b)  in  anderer  Stellung : paoirlm  upa  may»m  kakirit  äpö  ä' hvqm  tanüm  pairi.yaozdai'^lta  V.().3i; 31.  6)  hinter  dem  Pron.  interrog.  wie unser eDkl.'(dann,) denn': fiTVöci"  aäe  raoäi (sd.)  owÄj«  .._j'^. .  V.  2.  39;  —  Aijm  aste maistna  baray?n  yaltbyö  .  .  cay5  ä°  aSte maisma  atahsn  . .  V.  Ä 1 1  f-  7)  im  Nach- satz'so,  dann;  da':  _>'ffl/ ('wenn')  a^j'/oars'ii,- naemät  ä°  mam  avi.iimrmaya  (sd.)  Yt./6, 2;  2,  J.3,  V:2.43,  Ä36,  103,  /Ö.ii.Nik. 3,  Vd.  /j';  —  yat  ('wenn')  yavö  dayät ii"  dadva  :^Ts9n  (sd.)  V.j.32;  331,  H.  2.
```


## [2026-09-05T20:04:50.788Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13640,13665p' BRT.txt; echo \"=========== 5985\"; sed -n '5985,5998p' BRT.txt"
}
```


### [2026-09-05T20:04:50.856Z] TOOL RESULT

```
er  sich  >£  nennen    \,/<T.i.  ».,,__  ,*^  „»,_  .„/;„,_  k^  ^'      "j_
Zcm  Pnn.  16  .Äa-:!!-  des  \.  'da*-.    —     Pu.;,,      -',        f,  ."^.^
hoffr/fihi.  Kessel  sollen  sie  zerstören,    den   Aafbau
•  g.  diwzaidyäi  Inf. 'zu  betrügen,  auschen':  ■^'"'*'^.°"V ';''■'-„  ...  ,-  ^  . «5(/  1^  vispäAuas  ahur!  nicht  zn  betrugen  i^pf,  „hd.  tiraL  —  Pi.:  d«  .geichr.  dddi; ist  der  allwahrnehmende  Ahr  ¥.45,4.          ».  dam  Hbm.  psu  65.
Zaro  Praes.  16  oia'ii.  de»  V.    'ja*-.    —    Pö.:  ^  j_  ,/,;,g.  p_  j,.  j;^  Jjiji.
^"fdtnäni  N   ,ro-  lies  ,arSJ.nä^  "  S-   dug»dM-,  j.   do^^r-  C  Tochter':
...       _  ,    ,      .,  ,    .  /"»'*  *7''J  ^'i^  "^-'S.  3;  (,  4:  —  j^atfha
•  j.  Oim  Part  1)  der  Hervorhebung:  /.in  ,,j  .  -     ^.jy         ,c-F  ■■£-   ,0/  'firam
f  «'«>"^£«''"^  ■-."'■■  "d^n  sollst  'k^(s^'^f,:^]^XA_2',-asim..'TL;^m du  einen  Pnester  oennen.  .  .  der  . ."  \ .  „^^^^^^  ^^j  y^  _  _  ^  ^„^'  ^^ iÄ6;  -  <7/^r^  (^)  .  .  m  d'a2-a>a  f„^^  sr»,«/i,7)  -y«»  <»>l«r<7^  »,«,/J  V. /«/,««  fsd.)  y.75.48;  -  yat  hanö  -  .,,^.,3.  _  ^^  ^^^  .nämL  maUh)  'g^ä bm-äl  aojjst^mca  d-  pascaaa  mazdayama  ^^^„„^^„3  s„naitis  Y.J3.4;  —  Pm.ru- tanast,mca    .  .  pastö.fra^a»,h^   (sd.)    h!    .^^^.  .^,^   ,^^^^    far^i^^^  Y.
'r'^'^T**'-''""'.-'-'""'^^'^''-'  "^'""V.^2..9:sbes.       "         '     -■      "^
^a^Mj-w  V.#.37;  38,  39.          a)  ohne  er-  XompE.  -  «i.  d>.h,!dr.  f..  tnp,  Tu.) uktr/.  np.
kennbare  Bedeutung,  hinter  dem  Relativ:  Juxt,  dunar.    Vgl.  daio  Bthl  .\f. /.9,  KZ.
yalsam  d"  fräyö  vohunam  V.j.  29;  —  yat  v-  so*,    IF.  ,-.  53.    ZD>fG.  ^a  69S.   Hb.m.
IC-    .„.  v,„         Vnl    v.v        P^-  /_   A-  „„^        *""£   '^**  «Orts    als   'Melkenn',    inletit   bei aäeÜSel^-^;rv   ft  1s7™V.  v;  ^^"^  FeMsr.Ro,h.35.  i.t  ohne  Wert;  des-
ausgelassen,  za  v.  /,.  45  s.  ™j-  >o.  1.         j      gi^^^hen  die  bei  LMevek  GrEt  3.  442.
.  g.  divammi-  Adj.   'sich  fem  haltend,;,    -  ^..  ^^^_,  ..^^        5.^.
fem   bleibend:  j-^  <i><i/  ^«-a,,,«.   """"  '  ,w  W  «'O"  dur»am  V. /=.  i9(?)^. (namL   «w-M   ÄJ/    apanm    xsyö   dang}m\      ..d«,  sinnsoll  sein:   ■Wenn  der  Sohn   des ayü    "wer    zum    ^^Äjanhänger    (d.    i.    Zar.)'      Sohns  des  Valersbniders    also  *lüirfa./v%rä.-
Ubergeht,  fem  wird  dem  künftig  bleiben !  r»'irS'  oder  die  Tochter  der  Tocht«  der des  Elends  lange  Dauer  .."  Y.W.  2o'>.     I     Vate^chw«ier     aUo     'ti:.rya,Arii^^^^„
   —      °        .  .  ...  -'..  -  stirbt  :  Ttfl.  nnler  naruHazaiila-  No_  a_ —  IVi  ■
PPM-,  am  Ptms.  3  *diva-.  —  Vgl-  dura-,  JN.  '
A  hyiin  53.  PeRMOK  Wurielerw   i54,  .59.  ^  >      '""  ^ie  strittigen  Wörter  a Vii.:  pa  frfpiin.  —  •)  iEl  s.  Gds,  BB.  /*  13.   •  j-  dujTO.va-   f.  EN.   der  Frau  Pouru- .  j.  disav-  m.  Name  eines  nächtlichen  t ^^^-^   ^^    ^^fV  /«^f**^";    "'^ Raubtieres:/«ifJÄ?(nämL  ist  der  Hund)  l'!"^"'{''"   »"'"^'"fr''*^  (sd-)    mä  pouru- ya>a  'su/V.ij.at,  473;  —  atH  SiAami""/"^  '7  2^'\F^^^t>      ■  ^^,-
■',    ,,         ,  j-ir  ■  -    .    .  Komp.:  »d/irii- i.Adi.,  PPfP.;  ai-abirrf*^-;  np.
j-ai^a  *°JJki  (GS.)   V.  IJ.  47.  IF.  12.  131X   —    ■'  Zu   den   nip.   Formen   des
Fi.:  tnniskr.,  Npü. :  dad.  S.  auch  Jcsn  N"B.  85. '      Namens  s.  JusTi  NB.  86  und  SBE.  4p-  Index.
g.  dUä  Y.  43-  T-  s.  rf^x-.  !,  j  ka/imäi  ainistim  ""duciSrim"  (ASf.)
•  j.  kaia  suraya  ayaca   tl  diiänaya"'    .  baxsätii  Yl/o.iio.
=========== 5985
Hilirikaca  apprmäyükasla  varai'i^lm  (sd.) pantam  azöil  V.j.ii;  — gäui . .  varaülm {sd.) pantam  azaifeXt  10.3S.  4  a)  Akt '(als  Strafe,  Busse)  auferlegen',  b)  Med. 'auferlegt  bekommen,  auf  sich  zu  nehmen haben':  a)  tairyehe  5:rt  vä  Ozaiti , .  aslraya
kada  mazda  yöi  uxsand  "snam  . .  /rärmtg
Y.46-7,.
Abkit.  —  ai.  ähnäm  usw.  (NS.  ihar).  —  Pü. : rS^.  —  ''S  3S.  1.  Doch  beruht  dei  Ansati azan-  lediglich  auf  dem  au  ähan-.  — ")  Thcm.
•  j.  a-zarama-  Adj.  (fem,  'mä-)  'nicht
V
ob,Google
"S
azarsäant-
az^m  4
326
abnehmend'  (an  Stärke,  von  der  Stimme) : fra  staotfi»  v<ü5  yesnitn  °mya  (ISt)  vaca mneyä  FrW./.  i.
*amma-  m. 'Verkommen',  lum  ai.  V.j'frya/i;
•  j.  a-zanäant-  Adj.  'nicht  alternd':  jiat
```


## [2026-09-05T20:05:14.347Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nv=d['BQT']\nprint(json.dumps({k:v[k] for k in v if k!='url'},ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-05T20:05:15.973Z] TOOL RESULT

```
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
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


## [2026-09-05T20:05:20.211Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 468; do echo \"###### v2 leaf $L (printed ~$((L+540)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -80; done"
}
```


### [2026-09-05T20:05:21.765Z] TOOL RESULT

```
###### v2 leaf 468 (printed ~1008)
                                                 ‫بیان سوم‬
                     ‫در زای نقطه دار باجیم مشتمل بر چپار لغت‬

                     ‫عنکبوت را گویند ‪۱‬‬       ‫مال‬        ‫* رج ‪ -‬بضم اووسلکون انی » تیر‬
                                                                        ‫پرتاب‌باشدکه پیکانآ براازاستخوان‬
‫رجمول ‪ -‬با میم بر وزن معقول ‪.‬‬
                                                                        ‫فیل وشاخ‌قوج کواومیش وامثال آن‬
‫حبی امت دوابی و آلرا بفارسی یخم کشوث‬
                                                                        ‫مازید ‪ _ ۱‬و کوتاه ثرین نیرها را‬
‫خواند ‪ .‬طبیمت آن معتدل امت در گرمی‬
                                                                        ‫و بمعنی چیزی باشد‬           ‫نکیوزبند ‏‬
                                         ‫‪۰‬‬   ‫وسردی‬
                                                                         ‫کهآ راازدوغ ترش سازند وبتر کی‬
 ‫زجه ‪ = ۴‬بفتح‌اول وثانی» زلی گروابند‬                                      ‫قراقروت خوانند؟ ؛ وباجیم فارسی‬
‫که زاییده (‪ )۱‬باشد و او را تا چهل روز زجه‬                                    ‫یز همه معانی آمده است ‪.‬‬
‫میتوان گفت ‪ :‬وباجیم فارسی‌هم درست امت ‪.۶٩‬‏‬                               ‫بفتح‌اول بروزن‬        ‫رجال‬


                                              ‫يان چهارم‬

          ‫کتنوات‬
               ‫دزرای نقطه دار با خای نقطه دار مشتمل بر هفت لغ‬
‫و اسب را بهم میرسد و آنرا ازخ فيز گونند‬                  ‫رخ = بفتح اول و سکون ثالی‪ ۰‬آواز‬
‫ولالةٌ حزین راگویند؟ ‪ -‬وبانگ وصدای زنگه | و بعربی تژلول خوانند © ‪ -‬و مخفف زخم هم‬
                                             ‫تن ‪۱‬‬        ‫و جرس را همگفته‌اند ‪ - ۴‬و فرو بردن چیزی‬
‫بر وزن شراره » شاخ‬            ‫رخاره ‪= ۲‬‬                  ‫باشد بزور وعنف درمة‌اك ‪ -‬وعلتی باشد کهآ دمی‬

                                                                          ‫(‪ )۱‬چسش ‪ ۲ :‬شده ‪.‬‬

  ‫‏‪( - ٩‬عر) زح (بضم اول وتشدید دوم) «نیزی آرنج » آهن بن لیزه وپیکان تیر ‪ .‬زجاح‬
  ‫‪_ ۴‬طبری سرج (کشك سیاء [قرقوروت] )» مازندرانی‬                          ‫وزججه ‏‪ ٠‬جمم» «منتهی الارب؟ ‪.‬‬
                             ‫رك ‪ :‬زاح » زادن ۔‬   ‫‪- ۴‬‬            ‫‪.‬‬   ‫‪۸۲4‬‬     ‫کتوی زهك ‪ « 15» .‬واژه نامه‬

         ‫رك‪ :‬زخم ‪.‬‬   ‫‪-‬‬   ‫‪۱‬‬           ‫ازخ ‪ ۰‬آزخ » ژخ ‪.‬‬       ‫_رك‪:‬‬    ‫‪۵‬‬         ‫‪.‬‬   ‫ژخار‬    ‫رك‬    ‫‪۴‬‬


                                              ‫‪-‬ك‪ :‬زخناره » ازغ » اژغ » آزغ ‪ 7‬آژغ ‪.‬‬
                                                                                 ‫‪ ۷‬ر‬
                                                       ‫تتفرقة پابان کتاب ‪.‬‬
                                                                         ‫لمخا‬            ‫‪:‬‬
                                                                                         ‫ك‪-‬‬‫رزپ‬
                                                                                             ‫‪#‬‬
                                                     ‫‪#‬چه ‏ رك ‪ :‬لغات متفرقهٌ بایان کتاب ‪.‬‬
                                                                                        ‫ر‬

  ‫‪)۱۳۱‬‬     ‫طع‬
            ‫اای‬
              ‫فبره‬
                 ‫(‬
```


## [2026-09-05T20:05:30.676Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زدودن\\|زدود\" BQT_v2_pages.txt | head -10; echo \"--- which leaf:\"; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'زدودن' in p or 'زدو' in p:\n        print('leaf',i,'printed~',i+540)\nEOF"
}
```


### [2026-09-05T20:05:32.749Z] TOOL RESULT

```
17910:                   ‫درون عاقت بر کن ‪۰‬‬     ‫که رش‬                      ‫حذر کن زدود دروتهای رش‬
21000:  ‫ناکهی بای وجودش بگل رقت و دود فراق ازدودمانش برآهد‪€, .‬‬                                   ‫‪۱‬‬                 ‫> ‪.‬‬              ‫«اسشق‬
25984:‫روهینا ‪ -‬بروزن بوسیناه بمعنی زدوده‬               ‫نت » و بعضی گویند‬         ‫آکی‬‫رل م‬
25989:         ‫است که از ياك کردن وزدودن باشثد ‪.‬‬
27752:               ‫رك ‪ :‬از در ‪.‬‬    ‫‪۴‬‬        ‫رك ‪ :‬زدودن ‪.‬‬     ‫‪۴‬‬        ‫‏‪e‬‬
32156:       ‫‪ #‬ساو یدن = سابیدن »‪ ,‬سوهان کردن ‪ -‬زدودن » صیقل کردن ‪ -‬ارهکردن ‪-‬خرد‬
35962: ‫آنار ابن لهجه نسبة متأخر است » آثار پیشن آرامی را رفته رفته از بادها زدوده » جاندین آن‪‎‬‬
--- which leaf:
leaf 13 printed~ 553
leaf 24 printed~ 564
leaf 39 printed~ 579
leaf 74 printed~ 614
leaf 171 printed~ 711
leaf 178 printed~ 718
leaf 202 printed~ 742
leaf 203 printed~ 743
leaf 222 printed~ 762
leaf 241 printed~ 781
leaf 251 printed~ 791
leaf 304 printed~ 844
leaf 321 printed~ 861
leaf 344 printed~ 884
leaf 354 printed~ 894
leaf 360 printed~ 900
leaf 370 printed~ 910
leaf 379 printed~ 919
leaf 395 printed~ 935
leaf 400 printed~ 940
leaf 401 printed~ 941
leaf 408 printed~ 948
leaf 439 printed~ 979
leaf 441 printed~ 981
leaf 461 printed~ 1001
leaf 468 printed~ 1008
leaf 469 printed~ 1009
leaf 470 printed~ 1010
leaf 499 printed~ 1039
leaf 505 printed~ 1045
leaf 507 printed~ 1047
leaf 515 printed~ 1055
leaf 520 printed~ 1060
leaf 534 printed~ 1074
leaf 540 printed~ 1080
leaf 545 printed~ 1085
leaf 573 printed~ 1113
leaf 597 printed~ 1137
leaf 628 printed~ 1168
leaf 655 printed~ 1195
```


## [2026-09-05T20:05:35.878Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==470' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-05T20:05:37.581Z] TOOL RESULT

```
 ‫زدن‬                                                                                ‫و ‪—| ۵ ۵‬‬




‫چویکی باشد که سنادزهابدان سازنوازند ویعربی‬                                  ‫درخت رگاوند ‪۶.‬‬
                              ‫مراب خوانند ‪.‬‬      ‫زخم بریان س بمعنی دم پفت است‪.‬‬
‫رخناره ‪ = ۴‬بانون پروزن انگاره »‬                                      ‫‪۱‬‬   ‫وآن طعامی باشد معروف‬

      ‫بمعنی زخاره است که شاخ درخت باشد ‪۰‬‬         ‫زخم ناخ د بمنی باناخن رش‬
                                                 ‫ونابه از رفوم منجمان هم‌هت‪.‬‬
                                                                           ‫کردن باشد ک‬

                ‫وبی‌خرد وی‌خود شدن باشد ‪.‬‬



                                        ‫يان بنحم‬

                                                       ‫در زای نقطه دار با دال بی‬
‫بکر اول بر وزن جگر »‬          ‫ردر ‪= ۴‬‬            ‫ردای‪ = ۴‬بکر اول بر وزن فزای »‬
             ‫زدابنده و پاکیزه کننده را گویند ‪ -‬وامر | بمعنی درخور راق وسزاور باشد ‪.‬‬
‫رشن * = بروزن‌بدن‪.‬عمروف است ‪١-‬‏‬                  ‫بابن معنی هم هت بعنی بزدای وپاکیزه ساز‬
‫وکنابه از چیزی خوردن ‪ - ۷‬و مباشرت کردن‬           ‫و زدایدن وصان کردن وبا کیزه ساختن باشد ‪.‬‬

                                              ‫‪۰‬سوند اسم آلت) ‪:‬‬
                                                             ‫‪ -‬از ‪ :‬زخم (پ‬
    ‫رکه بدر آوازش‪.‬‬
                 ‫ناخوشتر از آواز‪ :‬م‬               ‫کفتی رکه جان میگلد زخمه‌ناسازش‬
  ‫«کلتان ‪۲۷‬‬
               ‫رك ‪ :‬از در ‪.‬‬    ‫‪۴‬‬        ‫رك ‪ :‬زدودن ‪.‬‬     ‫‪۴‬‬        ‫‏‪e‬‬
 ‫‪-‬هلوی ‪ 12122‬و ‪ 02682‬از رة ابرانیقدیم ‪. 2421 . [02 -‬ار ‪nag‬‏‬        ‫پ‬
 ‫که ‪ ۸۵۲‬بارسی‌باستان ر‪٫‬عةٌ‏ ‪ 0712032 ۰ [12-‬ک(شتن)‪ .‬هندی‌باستان‬
                                                             ‫د بارتولمه ‪ ۰۹4‬نربب‬
  ‫رثة ‪ ( 4261 . 022 -‬مضروب کردن‪ .‬کشتن ) قس‪ :‬ارمنی ‪( 028‬ضرب ‪ .‬تادب) و‪۳۳6088‬‬
 ‫(مضروب کردن ‪ ,‬كتك زدن) » کردی ‪( 8106012‬زدن (آش)‪ .‬تیر الداختن)» افقانی‪۵۷ |۳202-‬‬
 ‫‪ ..4‬بلوچی ‪ [8202‬و ‪. [18202‬ع ‪ 82022‬ر ‪ . 0821022‬شغنى ‪"1Z - 0۳2‬‏ ‪,‬سریکلی‬
 ‫[‪ « 1۷‬اسنق ‪ ۳۹۰۰‬طبری ‪ ( 20- 72112‬زدن ) « ساب طبری‬                  ‫‪0-102‬‬
                                                                        ‫و ‪12‬‬       ‫‏‪0-2am‬‬
                                                                                      ‫‪2‬‬
  ‫‪ -‬کوفتن» وارد آوردن‌صدمه‪,‬‬             ‫)‪( 2022-80 .‬بزند) ‪.‬‬        ‫ن‬
                                                                   ‫د(‬‫ز‪06‬‬
                                                                       ‫‪» ۶‬گیلکی ‪62‬‬
   ‫‪۳‬ه*‪.‬‬
      ‫ات»ن«‬
          ‫سراتکف‬
               ‫ل‌چ‬
                 ‫ضرب ‪ « :‬ملك فرمود بنزدش (شیاد را ) وفی کنند تا چندین دکرهم‬
                                    ‫‪ -‬اکنونکوبند ‪ :‬کیلاسی( مشروب ) بزیم ‪.‬‬
 ‫‪.‬هلوی ‪ 01522‬ب‪2‬ا‪. 01012‬کردی واففانی ‪ ۰ 0122‬بلوچی‬
                                               ‫اول پ‬                     ‫فمت‪-‬ح‬
                                                                             ‫بزخ‬
                                                                               ‫‪#‬‬
‫‪ 0‬و ‪( 7182‬شمشیر) «استق ‪ ۲04‬ورك ‪ :‬هوبشمان ابضاً ‏ گیلکی ‪ 00122‬؛ جراحتی که‬
                                ‫بوسیلةٌ آلات جارحه با ناخن ودتدان ومافند آن بهم رسد » رش‪:‬‬
         ‫‪.‬‬   ‫که تماید بچشم همردم دوست‬                        ‫ر خم دادان دشمتی شرت‬
 ‫«کلتان ‪۰۲۱٩‬‏ ‪.‬‬
                                               ‫‪ -‬ضرب ‪ ۰‬صدحه ‪ -‬شکستگی ‪ ۰‬کسر‬
```


## [2026-09-05T20:05:46.990Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(470,478):\n    p=t[i]\n    if 'زدو' in p or 'زدای' in p:\n        print('=== leaf',i,'printed~',i+540)\n        print(p[:3000])\nEOF"
}
```


### [2026-09-05T20:05:48.767Z] TOOL RESULT

```
=== leaf 470 printed~ 1010
‫—‬        ‫‪۵۵‬‬
                                                                                                      ‫زدوار‬

‫ردو نتن ‪» ۴‬با نون و تای قرشت مر‬                          ‫وجماغ باشد‪ -.‬و چون مرکب شود معنی بیار‬
‫وزن سبوشکن » بلغت زند و یازند (‪ )۱‬بمعنی‬                                                       ‫اهل‬         ‫دارو‬
                                       ‫خریدن باشث ‪.‬‬
                                                          ‫= بر وزن ومعنی‌جدواراست‬         ‫ردوار‪۱‬‬
‫زده ‪ - ۴‬بنتح‌اول وثالی» بمعنی خورده‬                                                  ‫که ماه پروین باشد ‪.‬‬
‫بداتکه ازچیزی خوردن است‪ -‬وآراسته ومزین‬
‫وزینت داده را هم‌میگویند‪ -‬وپبراسته وبربدرا‬                ‫ردودن ‌ ت بکراول بروزن‌فزودن»‬
‫نیز کوبند که از قطم کردن باشد ‪-‬‬
                                                          ‫بمعنیازالهکردن وبالساختن باشدعموماً چنانکه‬
                                                          ‫دل را از غم وآيعنه وشمشیر وامثال آنرا اززدگه‬
‫وهرچیزی کهنه وفرسوده راهمکفته‌اند ‪ -‬وچون‬
‫»مسعتییار دارد ‪.‬‬
               ‫ترکیب کنند بالفظدیگر ب‬                                    ‫واعضنا را اچزرك وملك را از فتنه ‪.‬‬


                                                  ‫بیان ششم‬
         ‫ایت‬
           ‫کتنو‬
              ‫وفت لخ‬
                   ‫در زای نقطه دار بارای بی‌نقطه مشتمل بر مکصد ه‬
                          ‫‪٩‬‏ ‪.‬‬       ‫ومخقف زرد همهت‬      ‫زر = بنتح اول ‪ ,‬طلا راکونده وآنرا‬
    ‫ار‬         ‫سراب‪ ,‬ا‬
                            ‫‪۱‬‬
                                ‫زن‬
                                 ‫ربو=‬
                                    ‫زبرا‬
                                              ‫‪۰‬‬

                                                         ‫را‬    ‫کے‬
                                                                    ‫ورت‬
                                                                      ‫نپی‬
                                                                        ‫ردم‬
                                                                          ‫فومر‬
                                                                             ‫نند ‪- ۷‬‬
                                                                                   ‫اهب‬
                                                                                     ‫وذ‬
                                                                                      ‫‪۹‬‬
                                                                                       ‫خبی‬
                                                                                         ‫حر‬
                                                                                          ‫ا‬   ‫‪0‬‬       ‫‪۰‬‬


‫م کوهی‌است‬           ‫کک‬          ‫‪2‬‬                        ‫‪-‬‬   ‫لیز گفته‌اند عموما خواه مر دباشد وخواه زن‪۷‬‬
‫و کنابه از شراب زردرنگ‬                ‫درئواحی بقداد ‪۰‬‬
                                                          ‫وییرسفید م
```


## [2026-09-05T20:05:57.164Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==471' BQT_v2_pages.txt | tail -40"
}
```


### [2026-09-05T20:05:58.790Z] TOOL RESULT

```
                                                                                     ‫وذ‬
                                                                                      ‫‪۹‬‬
                                                                                       ‫خبی‬
                                                                                         ‫حر‬
                                                                                          ‫ا‬   ‫‪0‬‬       ‫‪۰‬‬


‫م کوهی‌است‬           ‫کک‬          ‫‪2‬‬                        ‫‪-‬‬   ‫لیز گفته‌اند عموما خواه مر دباشد وخواه زن‪۷‬‬
‫و کنابه از شراب زردرنگ‬                ‫درئواحی بقداد ‪۰‬‬
                                                          ‫وییرسفید موی سرخ رنگرا کوبند خصوصا ‪-۷‬‬
‫باشد ‪ -‬و طلای حل کرده ومالیده را قىز گویذه‬               ‫و پدر رستم را ازین جهت زال زگرفتندیکه با‬
                  ‫ادسفریدمتولد شده بود ‪ | ۸‬که استادان ناش بکار برند ‪٩۹.‬‏‬
                                                                       ‫موی‬
                                                                         ‫زوم‬
                                                                           ‫اخ‌‬
                                                                             ‫رنگ سر‬

                                                                         ‫وژند ‪.‬‬
                                                                              ‫(‪ )۱‬چك ‪ :‬ژد ر‬

    ‫‪ - ۴ .‬از‪(:‬ز دوج دن‬                  ‫‪ ۱‬ج=دوار (‪.‬م‪( 67120062 ).‬فر)«لك» ص‪.»۰۰۲‬‬
    ‫‪ .# 12-۷20-21111‬هندی باستان ربشهٌ ‪ ( ۷80 -‬مالیدن »‬
                                                     ‫(پوند مصدری )‪ .‬پارسی‌باستان ‪2‬‬
    ‫‪ - ۴‬هز « ‪nat‬‏ ‪. _ natan . )i(nêd)a(Z‬‬              ‫منق)ا ‪۲ : ۱‬ص‪. > ۰۳۴۱‬‬      ‫«كک‬
                                                                              ‫ارو‬    ‫پا‬
                 ‫‪ - ۴‬اس‌مفعول از« زدن > ‪.‬‬     ‫» خربدنه بوتکر ‪. > ۸۰۱‬‬ ‫‪0‬‬ ‫‪2‬‬ ‫‪1‬‬ ‫‪۲‬‬ ‫‪1‬‬  ‫ی‬ ‫و‬ ‫ل‬ ‫پپ‬
     ‫‪ ۲2-‬و ‪AZ‬‏ (طلا) فارسی ‪ ۰‬ماد ‪ 01782‬و ‪(01۳۳22‬طلابی) هر دو وجه‌آمنه‪.‬‬‫® ‪2‬‬
     ‫یارسی باستان ‪( © 201۳32 -‬اوستا‪( 4 80۳120۲82 )۵ 8066۲22 -‬اوستا «(‪_aneanerazo‬‏‬
     ‫‪ ,‬کردی ع‬        ‫‪0‬ن‪17-4‬‬
                          ‫‪1‬ستا‬
                             ‫قی ‪ :‬زرلیخ «هوبشمان ‪ , 4۵۱۰‬پهلوی ‪ . 01722 » 22‬هندی با‬
     ‫‪ ۴‬و ‪ . ۲2‬اقنانی ع ‪ , 722‬استی ‪ [ 81782‬طعنء رصا ةطعےء (طلاء طلابی) ‪,‬بلوچیع‬
     ‫‪ < 782‬اسشق ‪ , ۶۵۱۰‬سفدی ‪ 0۲5۰‬ختنی ‪ « ۳2۳۷22‬برلی ‪ .‬رو ز کار نو ج‪٤‬‏ شمارء س‪۲‬ه *‪.‬‬
           ‫‪ ۱‬رك ‪ :‬دائرتالمعارف اسلام ‪ :‬ذهب ‪.‬‬           ‫اورامانی ‪ . 4« 8782‬اورامان ‪. ۷۲۱‬‬
     ‫هندی باستان ‪ , [60274 -‬ارمنی ‪( ۲60‬پیر مرد) » استی ‪( 000۳82‬پیر) اقی‪:‬‬                          ‫‪۲‬‬
              ‫© ‪ -‬رك‪ :‬زرد ‪.‬‬                  ‫رك‪ :‬زال » زال زر‪.‬‬      ‫‪۵۸‬‬         ‫رال («‪.‬م‪ ۶ ).‬اسشق ‪۵6٩‬‏ ‪-‬‬

     ‫ول درممجم البلدان زراب موضعی در راه تبوك بمدینه( که مسجد رسولص بدانجاست)‬
                            ‫‪ -0‬از ‪ :‬زر( آب ‪.‬‬                  ‫و کوههای مرتفع بینفید وجبلین‪ ,‬پادشده ‪.‬‬
```


## [2026-09-05T20:06:15.082Z] TOOL CALL #29: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-05T20:06:15.123Z] TOOL RESULT

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


## [2026-09-05T20:06:23.131Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nprint(len(t))\nfor i in range(380,405):\n    if 'اندود' in t[i]:\n        print('=== leaf',i)\nEOF"
}
```


### [2026-09-05T20:06:24.791Z] TOOL RESULT

```
777
=== leaf 383
```


## [2026-09-05T20:06:27.169Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==384' BQT_v1_pages.txt"
}
```


### [2026-09-05T20:06:29.129Z] TOOL RESULT

```
سب ی ٩5‏
| بودن بروزن افزودن, بربالای حم
چیدن باشد .
اثبوذن س با زال قطه‌دار بروزن‌اندودن,
بمعنی اسل‌کاینات و آفرینش باشد .
ایوس » بروزن اضوی , تخمی باشد
بنظر آحده است ۰
| بو سیدن - بانستانی مجپول بروزن
افزوییدن , بمعنی پدید آمدن و ظاهر شدن -
و موجود گردبدن باشد .
اثبوه » بروزن اندره » بمعنی‌فرورختن
دبوار باشد - و بمعتی پر و عملو و بسیار نیز
امده خواه بساری مردم و خواه چیزی دیگر
باشد - و دم قصبه است در بالای کوهی از
مضافات دیلمان .
اثبوی « بر وزن بدبوی » بعنی بوی
کردن باشد ٩‏ - و چیزی‌را نیز گوبند که ببوی
آهده و کندیده باشد - و مطلق‌بوی رانیز گونشد
خواه بوی خوب و خواه بوی بد باشد - و بوی
کننده را نیز کوش که فاعل باشد - و اهر باین
معنی هم هست عنی بوی کن و سوی ۰
) بو ی (۱) » بکربایحطی‌وسکون
دال ؛ یمنی بوی کرد -- و امر بجمم هم هست
بعتی بوی کنید و ببوید .
انبوییدن 0)- ممدر ابوی باشد
سعتی بوی کردن و بوبیدن .
انتو هن
اثبه ه بش ثاكث و طپور ها بروزن‌انده ,
مخفف انبوه است که فروریختن دبوار - و عملو
و پر و بسیاری چیز ها باشدخواه از مردم وخواه
از حیوانات دیگر - و بفتح ثالث و خفای ها
هبوه‌است معروف در هندوسنان ۴ .
۱ ثییر بروزن زنجیر » بمعن ی گل‌خشك
وگل تر هر دو نوشته‌اند - و بمعنی پرکردن
هم هست - و بمعنی کیش و مذهب ودین وین
هم باظر آهده است . ۱
اثییره بروزنزنجیره» خلاشه‌وخاشا کی
راکوند, که بعد از پوشش خانه بر بام اندازند
تا بربالای آن خاكك و کل ریزند و بیتدایند .
آثییس » بر وزن نلبیس , خرمن غله
فییالا - بلام کشیده ,کر که (۳)جنگی
را کویند و آن جالورست درهندوستان شبیه به
کاومیش و برسریینی شاخی دارد .
ء ءِ‌
| نتله‌سو۵ا - بنتح اود و سکون ثانی
و کسر فوقانی و لام مقتوح و های مکسور وفتح
سین ی تفطه و سکون واو و دال ابجد بالف
کئبده » بلفت سربانی جدوار باشد که آنرا ماه
فرفن گونند ۴ .
ا فتق قتن؟ - با نون و نای‌قرشت بروزن
پهلوشکن ۰ بلفت زند و پازند (۶) بمعنی داشتن
باشد که از دارند کی است .
۴ هز ۵017)1(127 , پهلوی
۶ حاسوشن » است . 2 : هم ‌کمه .
```


## [2026-09-05T20:06:38.429Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'ندود' in p or 'ندای' in p or 'اندا ' in p:\n        print('leaf',i, 'printed~', i-220)\nEOF"
}
```


### [2026-09-05T20:06:39.914Z] TOOL RESULT

```
leaf 51 printed~ -169
leaf 85 printed~ -135
leaf 92 printed~ -128
leaf 138 printed~ -82
leaf 259 printed~ 39
leaf 265 printed~ 45
leaf 315 printed~ 95
leaf 326 printed~ 106
leaf 336 printed~ 116
leaf 383 printed~ 163
leaf 387 printed~ 167
leaf 389 printed~ 169
leaf 430 printed~ 210
leaf 432 printed~ 212
leaf 493 printed~ 273
leaf 511 printed~ 291
leaf 580 printed~ 360
leaf 594 printed~ 374
leaf 673 printed~ 453
leaf 683 printed~ 463
leaf 702 printed~ 482
leaf 709 printed~ 489
leaf 762 printed~ 542
```


## [2026-09-05T20:06:42.932Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 387 389; do echo \"##### leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n \"ندود\\|ندای\\|^۱\\|هز\\|پهلوی\\|هندی\" | head -20; done"
}
```


### [2026-09-05T20:06:44.552Z] TOOL RESULT

```
##### leaf 387
25:)ندایش بر وزن افزاش ؛ بسسنی
59:۱ .رك : اندروای.
##### leaf 389
33:) ندودن۱ - بروزن‌فرمودن . کاهگل
51:۴ پهلوی 12702۷ (کم »کمی)
```


## [2026-09-05T20:06:46.763Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==390' BQT_v1_pages.txt | sed -n '25,70p'"
}
```


### [2026-09-05T20:06:48.437Z] TOOL RESULT

```
کرداند . آنرا بعربی قوباکویشد .
افو ج -بروزن محلوج» بمعنی‌اندوب
است وآن جوششی است با خارش که عرب قوبا
شف
] ند و خقی* - بروزن‌افروختن» بمعنی
جمم کردن وفراهم آوردن باشد - بمعئی قرض
و ایس دادن ‌‌ زد ابیت
اند‌و.- وزن مقصود ۰ کاهمگل
) ندودن۱ - بروزن‌فرمودن . کاهگل
و کلابه مالیدن باشد - ومطلا وملمع کردن دا
نیز کوید .
ا فك و ۷ - بروزن سردوز؛ بمعنی‌فراهم
آورده وجمم کرده شده باشد - وامر باین حمنی
همست عنی جمع کن وفراه آور .
اندول بروزن ممقول ۰ کلیمی باشد
کهآنرا برچهارچوب بامیخها سکم کنندوبجهت
استراحت برآن نشینند . و این در ملك زنگبار
مصمول است »
| ندو ف » بنتح رابع وسکون نون‌ودال
ابجد » از انباع است بمعنی تار وعار که زبروزس
شده رازهم باشدم باشد .
آف‌وه٩‏ - بروزن انبوه , گرشکی ول
ودلگیربرا اگوبند ف
| زد و۸ چم ثالث » مخفف اندوه است
» و اوزن ۳6000۲ ومادر ۸5۷۵۵
۴ - نیز اندیرما, در اوستا
۴ پهلوی 12702۷ (کم »کمی)
فعه در صفحة ۱۷
```


## [2026-09-05T20:06:54.693Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==390' BQT_v1_pages.txt | tail -30"
}
```


### [2026-09-05T20:06:56.356Z] TOOL RESULT

```
«مناس۹ ۲۷ .راد: ۳
اند
کرداند . آنرا بعربی قوباکویشد .
افو ج -بروزن محلوج» بمعنی‌اندوب
است وآن جوششی است با خارش که عرب قوبا
شف
] ند و خقی* - بروزن‌افروختن» بمعنی
جمم کردن وفراهم آوردن باشد - بمعئی قرض
و ایس دادن ‌‌ زد ابیت
اند‌و.- وزن مقصود ۰ کاهمگل
) ندودن۱ - بروزن‌فرمودن . کاهگل
و کلابه مالیدن باشد - ومطلا وملمع کردن دا
نیز کوید .
ا فك و ۷ - بروزن سردوز؛ بمعنی‌فراهم
آورده وجمم کرده شده باشد - وامر باین حمنی
همست عنی جمع کن وفراه آور .
اندول بروزن ممقول ۰ کلیمی باشد
کهآنرا برچهارچوب بامیخها سکم کنندوبجهت
استراحت برآن نشینند . و این در ملك زنگبار
مصمول است »
| ندو ف » بنتح رابع وسکون نون‌ودال
ابجد » از انباع است بمعنی تار وعار که زبروزس
شده رازهم باشدم باشد .
آف‌وه٩‏ - بروزن انبوه , گرشکی ول
ودلگیربرا اگوبند ف
| زد و۸ چم ثالث » مخفف اندوه است
» و اوزن ۳6000۲ ومادر ۸5۷۵۵
۴ - نیز اندیرما, در اوستا
۴ پهلوی 12702۷ (کم »کمی)
فعه در صفحة ۱۷
```


## [2026-09-05T20:07:04.232Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 150 (p.129) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==151' HRN.txt | head -60"
}
```


### [2026-09-05T20:07:05.861Z] TOOL RESULT

```
=== HRN leaf 150 (p.129) ===
- 129 -
af/. dvalas; oss. d. duades, t. duädäs.
Die neupersische Form (eine Analogiebildung) ist
entlehnt in kurd. duänzdih (hier findet sich noch
ausserdem das n von np. sänzdeh), hol. duäzdeh,
oll. (\)dö%ten *anheften, durchbohren, nähen', Praes.
döz-em, döz, dözene, kun\döz grosse Nadel' (AM. 52
ZeUe 6, 116 Zeile 2 v. u.).
maz. düj, düjene,
phlv. döc *Speer (Dat. d. 21, 8), phlv. pjiz. dö/tav,
dözEm (PPGl.)
oss. än-düzün, d. än-dozun ^befestigen (von
Stackeiberg, ZDMG. 43, 671); bei. dööag , n.
dösay *nähen (91).
578. (2)döy(ten 'melken', Praes. dös^em, dösTden, döy saure
Milch' (AM. 216 Zeile 5) ').
ai. [/"döh-, dogdhi 'melken', dögha^; phlv. dö/fan
(Bund.), dösUan (Bund., PPGL).
kurd. dötifiy düsim, di-dösim melken'; afy. Ivasal;
oss. d. docufiy t. dücifi (111); bei. dösay (94); wa;^.
dtc-am^ dögnam, sar. dauz-am.
579. dFfd 'Rauch', diidmän 'Familie.
phlv. dfit 'Rauch', dütahnan (AV.), vorgl. dütal'
'Familie' Bahmyst (Spiegel, Trad. Lit. S. 4()G); ai.
vergl. dhümä' 'Rauch'; lat. //7mMs, lit. diima-s, ksl.
dymü,
kurd, du; af/. lü; bei. düt, dlt (90); wa;^. dit, sijn.
öud, sar. düt.
580. dür 'fern'.
ap. dura- 'fern'; aw. dura''; phlv. dür\ ai. dum-,
kurd. dür; af/. liri; bei. d/lr, dJr (89); wa;^. JJr,
yidg. lüro,
581. dö»eyi 'Hölle*.
aw. (anMtis) daozaMahe, vergl. duzah" 'Hölle';
phlv. dömx (päz. diiza/, dorn/), dö^a/ (PPGl.) —
dusähü darf man das Pchlevivvort nicht losen; denn
*J Wa/. dayOWj sar. diiyoic *Molke*.
Hör II, Qrundriss d. neup. Etymologie. 9
```


## [2026-09-05T20:07:12.656Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==411' SYN.txt | head -70"
}
```


### [2026-09-05T20:07:14.318Z] TOOL RESULT

```
macellaro, beccaio OE hyldere, cwellere Boh. fezntk
Fr, boucher ME bo(u)cher, slaghter- Pol. rzeznik
Sp. carnicero man Russ. injasnik
Rum. mdcelar NE butcher Skt.  mdnsika-
Ir. ea Du. slager Av. Siaiais
Nir. —_ baiistéir OHG | slahtari
W. cigydd MHG_ vleischslachter, vleisch-
Br. kiger houwer, meizjere
NHG fleischer, metzger, schlachter
The ‘butcher’ was primarily the one who slaughters large domestic animals for their meat, then the one who cuts up the meat in the shop and sells it, simply a dealer in ‘meat’.
Several of the words are derived from verbs for ‘slaughter’ or ‘cut’ (a ‘cutter’ may be specialized to ‘butcher’ or ‘tail- or’). The majority are derived from words for ‘flesh, meat’ (4.13, 5.61). A small group shows generalization from
‘one who slaughters goats or deals in goat’s flesh’.
1. Grk. ogayets (: obatw ‘slaughter’, esp. animals for sacrifice) is used for ‘slayer, murderer’ and technically for the one who slaughters the sacrificial victims, but is not quotable as a trades- man’s name. Instead we have xpé@ xémos, -7otds (both rare), and esp. Lia? 1 kpew-rbdns (as in NG), epds. of xpéas
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
5 ee a ee ee eee
fooD AND
with words for ‘cut’,
inake' and Lae Turk. kasap ‘butcher’. ius, late lanid, beside vb.
ie es f ; mangle’, perh. of
‘sin, Walde-P. 2.434. Er- Walde-H. 1.759 f.
llarius (> It. macellaro, ma-
icelar, NG paxeddapns), fr.
nout-M. Lat. mace
this fr. 421.102, etc., Flesych.; late wéxe at,), this again Of P© Hebr. mikla ‘inclosure ). 515, Walde-H. 2. :
Tr, boucher (OF r. bochier, bouchier > ME bocher, boucher, NE butcher), fr. boue, OFr. boc ‘he-goat’, hence orig. ‘one who slaughters he-goats’ (young he- goats were regularly killed for their meat except for a few reserved for breeding). REW 1378. Wartburg 1.587 f. Other- wise Gamillscheg 125.
It, beccaio, fr. becco ‘he-goat’.
Sp. carnicero, fr. carne ‘flesh, meat’.
3. Nir, biistéir, fr. NE butcher (for transposition of tg, cf. Pedersen 1.230). W. cigydd, Br. kiger, fr. W. cig, Br. kig ‘flesh, meat?, em Hee Sw. slaktare, ME iller a. tia Tee ae victims), 1] tleischslahter, NHG schlachter (or schlachy-
dros as ‘market’ after f Semitic orig. (ef. Ernout-M.
DRINK; COOKING AND UTENSILS
Digitized by Arya Samaj Foundation Chennai and eGangotri
365
ter), all fr. vbs. for ‘slaughter’ (: Goth. slahan, etc. ‘strike, slay’ 9.21).
OE hyldere (fr. hyldan ‘flay’, 9.29) and cwellere (: cwellan ‘kill’, 4.76) occur as glosses to Lat. lani6, macellarius.
ME bo(u)cher, NIE butcher, fr. OFr. bo(u)chier (above, 2).
MHG vleischhouwer, NHG fleischer (locally also fletschhauer, fleischhacker), fr. fleisch ‘flesh, meat’.
MHG metze
```


## [2026-09-05T20:07:19.064Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"5\\.87\\|5\\.86 MILK\\|MILK (sb\\.)\\|MILK, vb\\|To MILK\" SYN.txt | head -20"
}
```


### [2026-09-05T20:07:19.122Z] TOOL RESULT

```
748:2. Lat. mundus is the result of se- mantic borrowing, starting as a literary imitation of Grk. xécpos. It is the same word as mundus used of a woman’s ‘ornaments, dress’, this being related to the adj. mundus ‘clean, elegant’ (15.87). This was a synonym of Grk. xécpos in one of its frequent uses (see above), one that was probably more familiar to the
8314:CHAPTER 5 FOOD AND DRINK; COOKING AND UTENSILS 5.11 Eat 5.57 Minn 5.12 Foop 5.61 Mezar 5.13 Drink (vb.) 5.612 Burcurr 5.14 Hunexr (sb.) 5.62 Brrr 5.15 Turrsrt (sb.) 5.63 Sausace 5.16 Suck (vb.) 5.64 Sour, Brots 5.17 Mrx 5.65 VEGETABLES ' 5.21 Cook (vb.) 5.66 Bran ? 5.22 Bor 5.67 Pra 5.23 Roast, Fry 5.68 Onion 5.24 Baxe 5.69 CaBBAGE 5.25 Oven 5.70 Porato 5.26 Por 5.71 Fruir 5.27 Kerrin 5.72 APPLE 5.28 Pan 5.73 PEAR 5.31 Disx 5.74 Pracu 5.32 Prats 5.75 Wie : 5.33 Bown 5.76 Grape 5.34 Pircuer, Jue 5.77 Nur 5.35 Cup 5.78 OLIvE 5.36 Saucer 5.79 Om 5.37 Spoon 5.80 Berry 5.38 Kyire 5.81 Saur 5.39 Fork 5.82 Prpprr 5.41 A Mua, 5.83 VINEGAR 5.42 BReakFast Bi Rdeer ona 5.43 Luncx 585 § 544 Dinner een Base Sucnbn. 5.86 Mixx (sb.) 5.51 Breap 5.87 Minx (vb.) 5.52 Caxn 5.88 CHEESE 5.58 Dover 5.89 Burrer 5.54 Kwrap 5.91 Merap 5.55 Mzau, Frour 5.92 Wine 5.56 Grinp 5.93 Brrr
8473:Grk. aor. Gycaro, Ofjc8a. (Hom.+, poet.), with sb. 6nA7 ‘teat’, whence @nrdtw ‘suckle’ and ‘suck’ (usual prose word, Aristot., etc.); Lat. félare; Ir. denim, Corn., Br. dena, also W. dyfnu (R. A. Fowkes, Language 21.96); Goth. dad- djan (in one occurrence = @7\détw as ‘suckle’, but the passage Lk. 11.27, where @nAdtw is ‘suck’, is lacking), OHG taen (rare and only ‘suckle’), MHG dien, Dan. die, Sw. dia; Lett. dét; ChSl., SCr. dojiti ‘suckle’ (but ‘milk’ vb. in Boh., Pol., Russ.; 5.87); Skt. dha- (3 sg. pres. dhayati, 3 sg. aor. adhdt, pple. dhita-).
9664:Europe generally until the introduction | Lett. medus, OPruss. meddo, Chs] | of sugar (5.85). From it was made the | medi, etc., general Slavic ; Skt. madhy,. oldest IE intoxicating drink, the ‘mead’ | Toch. mit. Elsewhere only as ‘mead! 5 ! (5.91). or for some other intoxicating drink { Most of the words for ‘honey’ belong | (5.91). : to one of two inherited groups. In Gmc. 3. ON hunang, OE hunig, ete., gen. one of these is represented in Gothic, the | eral Gmc. (except Goth.) : Skt, han- if other in words for ‘mead’, otherwise | cana- ‘golden’, kanaka- ‘gold’, Grk | ‘honey’ is expressed by a new word de- | xvnxés ‘pale yellow’ etc. Walde-p. 6 rived from its yellow color. 1.400; Falk-Torp 417. N 1. IE *melit- ‘honey’. Walde-P. 4. Av. *paéna-, implied by paénaéna- L : 2.296. Ernout-M. 602. Grk. pé\:; Lat. | ‘prepared from honey’, NPers. angubin : mel (> Romance words); Ir. mil, W., | ‘bee-honey’, prob. as (bee’s) ‘milk’ or gj Br. mel; Goth. milip (cf. OE mil-déaw | ‘juice’ : Av. payah-, paéman- ‘milk’, Skt, : ‘honey-dew, nectar’, milisc ‘honeyed’); | payas- ‘milk, juice’, Lith. pienas ‘milk’ ; Arm. meir, Alb. mjall. (5.87). Barth. 817. i B 5.85 SUGAR ; Grk. céxxapr, etc. (late) Goth. Lith.  cukrus NG = faxape ONEEE 28,2: Lett. cukurs , Lat.  saccharum (late) Dan.  sukker Cie 7 ) It. zucchero Sw. _socker SCr.  Seéer P Fr. sucre OE tet Boh. — cukr Sp. azticar ME _ sucere, sugure, etc. Pol. cukier Rum. zahdr NE sugar Russ. sachar m Ir. ay Du. —zucker Skt.  carkara- 0 NI. stilicre OHG zucura Av. et CE ie W. stwgr MHG zucker | Br. sukr NHG zucker a rk The home of sugar and its European | the article was then only an exotic ar names is India. The companions of | product used for medical purpose. The Ir : Alexander the Great told of the Indian | cultivation of the sugar cane was intro- BR : cane which produced ‘honey without | duced in Sicily and Spain by the Arabs, fl ? bees’ (wept r&v xadduor, dre mowfor wed. | and it was only after the crusades that 0 .! HedwooGy yx obcdv, Strabo 15.694). The | sugar became the common sweetening th 4 native Indian name appears in Greek | in place of the older honey. The major- 8 4 and Latin transcriptions in the first cen- ity of European forms of the name come or tury A.D. (wédAc 7d Kaddpuvoy 7d Xeyépevoyv | through Arabic via Spanish or Italian. ¥0 oakxapt, Peripl. 14; caxxyapoy eldos dy Schrader, Reallex. 2.705 ff. W Bédtros év "Ivdig xal rH ebdalporr ’ApaBig Skt. carkara- ‘gravel, grit? (AV +) W mennyoros, ebptoxouevoy éxl rOy xadduov, | later ‘sugar’ : Grk. xpdn, xpoxéd7 ‘peb- Y Diosc. 2.104; Saccharon et Arabia fert, | ble’. Walde-P. 1.463. th sed laudatius India, est autem mel in Hence, through a later Prakrit form *; harundibus collectum, Plin. 12.32), but | like Pali sakkhara-, the following: ur
9677:; cre. hese ofr. $4 ic, NE sugar), Fr. su- | s.v. sugar. snr, sures 5.86 MILK (sb.) Goth. miluks Lith. pienas yada ON mjolk Lett. piens edo Dan. melk ChSl. mléko lac Sw.  mjolk SCr.  mlijeko latte OE meole, mile Boh. mléko lait ME  melk Pol. —-mleko ee NE milk Russ. moloko aple Du. melk Skt.  payas-, ksira- milicht, 288, Bx OHG miluh Ay. payah-, xbvid- Drath, Buth MHG milich, milch : NHG_ milch
9688:5.87 MILK (vb.)
11079:6.71 ADORNMENT i (Personal) b Grk. — xdcpos ON skraul, pryoi Lith. papuoSalas J NG arodtét Dan. smykke, prydelse Lett. ruota, greznums f Lat. mundus, Grndlus, or- Sw. prydnad, smycke ChSl. ukraSentje q namentum OE gearwe SCr.  nakit, ures, ukras It. ornamento ME ornement Boh. okrasa Fr. parure NE adornment Pol. ozdoba, okrasa k Sp. adorno Du. versiering Russ. ukraSenie ¢ Rum. podoabi OHG  garawi Skt. bhigana-, alarikara- } Ir. cumlach, ornaid MHG gerwe, gesmuc Ay. pis-, pacsa- Nir. Grnaidhedcht, sciamh- NHG schmuck 6 acht W. addurnaid, trwsiad I Br. kinklou, bragerezou 0 Collective terms for articles of ‘adorn- 1.1) : adj. mundus ‘clean, elegant’ | ment’ are mostly based on still more (15.87).
14678:7. Skt. mrj- ‘wipe off, cleanse’, Av. maraz- ‘touch’ (: Grk. énédyw ‘milk’, etc., 5.87) serve for ‘sweep away’. Cf. BR s.v. and Barth. 1152 (fra-maraz-), also Skt. sammdrjana- ‘sweeping’ and esp. sammarjani- ‘broom’ (BR s.v.).
19098:UW ft NG xaorPe ! 15.87), eas ei : ‘preserve’. Tiktin 1131. ‘a sim (K. Meyer, Contrib.
22488:Du., MHG, NHG klein, in MHG mostly ‘pure, neat, fine, pretty’ (cf. NHG kleinod ‘jewel, gem’), OHG kleinz ‘shining, slender, fine’, etc., OE cline ‘pure, clean’ (NE clean), prob. : Grk. yawol* apmrptopara Hesych., yAnvea ‘bright things, trinkets, stars’, yAnv7n ‘pupil of the eye’, yeAetv’ Aapumerv, avOetv Hesych., and other words with common notion of ‘bright, shining’. ‘Bright’ > ‘clean, neat’, as in Lat. nitidus > Fr. net, etc. (15.87), hence through ‘fine, delicate’ to ‘small’. Walde-P. 1.623.
25727:4. Grk. eénavrés, orig. ‘anniversary’ as in Hom. and early inscriptions (Cre- tan law-code, etc.), but also (Hom.-+) simply ‘year’, etym. disputed. Hither fr. phrase él at76 ‘in the same (time)’, for which cf. Boh. tyden, etc. ‘week’, fr. ‘this day’ (14.61); or perh. as orig. ‘sol- stice, resting place of the sun’, deriv. of evabw ‘rest, sleep in’, cpd. of latw ‘rest, sleep, pass the night’. Walde-P. 1.20. Brugmann IF 15.87 ff., 17.319.
25880:15.87 CLEAN
27322:s 15.87 CLEAN kabapd XBaphs Goth. hrains Lith. Svarus, Gystas mundus Aas ON hreinn Lett. firs, glits Bulilo, netio Dan. ren ChSl.  Sistit Propre, net Sw. ren SCr. ist limpig OE cl@ne Boh. Gisty curat ME lene Pol. czysty glan NE clean Russ. éistyj glan Du. rein, zuiver Skt.  cuddha- glan OHG  reini, subar Av. ‘ ue MHG reine, siiber
27367:NG dacrpos, neg. : racrpixds ‘clean’ (15.87).
27371:Lat. immundus, neg. cpd. of mundus ‘clean’ (15.87).
27378:Fr. malpropre (esp. of persons ‘habit- ually dirty’), epd. of mal ‘bad’ with neg. force and propre ‘clean’ (15.87).
27402:g.vV- : il ee of fre clean! (15.87). ja ne
30014:W. glan ‘clean’ (15.87), also ‘beau- tiful’.
30063:Skt. ¢ubha- : gubh- ‘adorn, deck, beau- tify’, perh. fr. a root *feu-bh- beside *keu-dh in Skt. ¢uddha- ‘clean’, etc (15.87). Walde-P. 1.368.
```


## [2026-09-05T20:07:21.965Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9688,9700p' SYN.txt"
}
```


### [2026-09-05T20:07:22.016Z] TOOL RESULT

```
5.87 MILK (vb.)
Grk.  épéyw Goth. Lith. milzti NG éuédyaw, applyw ON mjolka Lett. slaukt Lat. mulgére Dan. =malke ChSl.  mléstz It. mungere Sw. mjolka SCr.  musti Fr. tratre OE melcan, meolcian Boh. — dojiti Sp. ordenar ME mylke Pol. doié Rum. mulge NE milk Russ. dojit’ Tr. bligim, crudim Du. melken Skt.  duh- NIr.  criidhaim, blighim OHG~ melchan Av. sheen W. godro MHG melchen
Br. goro NHG~ melken
The verbs for ‘milk’ are unrelated to the nouns for ‘milk’ in the same lan- guage, except in Irish and the Gmc. group.
1. Grk. auayw (> NG pop. dppeyw through 4\yéyw with transposition) ; Lat. mulgére (> It. mungere, Rum. mulge, OFr. moudre); Ir. mligim, bligim; OE melcan, OHG melchan, etc., general Gme. (but OE meolcian, ME mylke, NE milk, fr. the sb. OE meolc, etc.); Lith. milzti, melzu; ChSl. mlésti, mliiza, SCr. mustt, muzem; Alb. mjellé; the old gen- eral Eur. vb. for ‘milk’ : Skt. mrj- ‘wipe, stroke’, Av. maraz- ‘touch’, IE *mel@-, with Eur. specialization of ‘wipe, stroke’ or the like to ‘milk’, Walde-P. 2.298 ff. Ernout-M. 637.
2. Fr. traire, fr. Lat. trahere ‘draw’.
Sp. ordefiar, fr. VLat. *ordiniare be- side *ordinium ‘implement’, fr. Lat. ordinare ‘arrange’. Development prob. through ‘manipulate’. REW 6091.
3. Mir. crudim, cruthaim, with sb. crud ‘milk’ (cf. K. Meyer, Contrib. 535, 538), NIr. criidhaim, etym.?
W. godro, MBr. gozro, Br. goro, cpd. *go-dro : W. troi ‘turn, twist’, Lat. tra- here ‘draw’ etc. Walde-P. 1.752. Peder- sen 1.97.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
4. Lett. slaukt : Lith. Saukt; ‘sweep’, both fr. a common notion of ‘wipe, stroke’. Miuhl.-Endz. 3.919.
Boh. dojiti, Pol. doié, Russ. dojit' : ChSI. dojiti ‘suckle’, Skt. dhayati ‘sucks’, etc. (5.16). Berneker 205.
5. Skt. duh-, NPers. duztan, duSidan, the Indo-Iranian verb for ‘milk’ (though not quotable fr. Av.). Connection with Grk. rebxyw ‘make, build’, rvyxave ‘hit the mark, meet, happen’, Goth. daug, OE déag, OHG toug ‘is of advantage, avails’, etc. is generally rejected on se- mantic grounds. Walde-P. 1.847. Feist 128. But in view of the perfect for- mal correspondence, one must consider the possibility of deriving the divergent meanings (which even in the Eur. group offer some problems) from some common source, even if the attempt involves speculation falling short of conviction. For example, the Indo-Iranian ‘milk’ may be from ‘stroke’, like the Eur. ‘milk’ (above, 1); ‘stroke’ and ‘strike’ may be from a common source (cf. NE strike : NE stroke, NHG streicheln); and ‘strike’ may lead to ‘hit, hit the mark’, the earliest use of Grk. rvyxavw (whence also ‘meet, happen, be fortunate’, ete.), from which ‘suit, be good for, avail’, etc. in Gme.
```


## [2026-09-05T20:07:29.494Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^daughter\\|daughter, n\" KLN_1966.txt | head -10; echo ---; grep -n \"duhita\\|dugədar\\|dugdar\\|duxtar\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T20:07:29.558Z] TOOL RESULT

```
---
```


## [2026-09-05T20:07:33.111Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dauhtar\\|Ovyarnp\\|thugater\\|dohtor\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== 1971 daughter\"; grep -n \"daughter, n\\.\\|^daughter\" KLN_1971.txt | head"
}
```


### [2026-09-05T20:07:33.196Z] TOOL RESULT

```
KLN_1971.txt:64592:Tochter , Goth, dauhtar , ‘daughter’, and cogn. 
KLN_1966.txt:10382:OFris.,  Du.  dochter,  OHG.,  MHG,  tohter,  G. Tochter,  Goth,  dauhtar,  ‘daughter’,  and  cogn. with  OI.  duhitd,  Avestic  dugeda-,  duydar-,  Toch. A  ckacar,  B  tkacer ,  Arm.  dustr,  Gk.  -&uyaTr,p, OSlav.  duSti,  OPruss.  duckti,  Lith.  dukte, ‘daughter’.
=== 1971 daughter
64589:daughter, n. — ME doghter , dohter , fr. OE. doh- 
64599:daughter-li-ness, n. 
105332:granddaughter, n. — Formed on analogy of 
128572:daughters. — Heb. Y e mimd h , lit. ‘dove’; rel. to 
131035:daughters. — Heb. QltzVd h , lit. ‘cassia’. See 
161416:daughter’, in Late L., ‘niece’, which is rel. to 
161423:daughter, stepdaughter’, OHG. tiift, of s.m. 
179093:daughter of Zeus and Demeter (Greek mythol.) 
199091:daughter of Laban and wife of Jacob. — Late
```


## [2026-09-05T20:07:37.002Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10375,10392p' KLN_1966.txt; echo \"=== leaf check\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt',encoding='utf-8').read()\nidx=t.find('OFris.,  Du.  dochter')\nprint('leaf', t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-05T20:07:40.999Z] TOOL RESULT

```
dation,  n.,  the  act  of  giving  (law).  —  L.  dal  id, gen.  -dnis,  ‘a  giving’,  fr.  datus,  pp.  of  dare,  ‘to give’.  See  date,  ‘point  of  time’,  and  -ion. Datisca,  n.,  a  genus  of  plants  (bot)  —  ModL.,  of unknown  origin.
dative,  adj.  and  n.  —  L.  dativus  (casus),  loan translation  of  Gk.  Botixy)  (nrCxnc),  ‘the  dative case’;  fr.  dativus,  ‘pertaining  to  the  act  of giving’,  fr.  datus,  pp.  of  dare,  ‘to  give’.  See  date, ‘point  of  time’,  and  -ive.
Derivatives:  dativ-al,  adj.,  dative-ly,  adv. datolite,  n„  a  translucent  calcium  borosilicate (mineral.)  —  Formed  from  the  stem  of  Gk. Saxetc&ai,  ‘to  cut  in  two,  divide,  distribute’, and  X1&04,  ‘stone’.  Gk.  Saxeiahai  prob.  derives fr.  I.-E.  base  *dl-t-,  a  -/-enlargement  of  base *dai-,  *dl-,  *d1-,  ‘to  cut  off,  separate,  divide, distribute’,  whence  OI.  ddti,  dyati,  ‘cuts,  sepa¬ rates,  divides’,  da-yate,  ‘divides’,  Gk.  SodeaOai, ‘to  divide,  distribute;  to  feed  on’,  Salpcov,  "god, goddess’,  lit.  ‘divider,  distributor  (of  men’s destinies)’.  See  demon  and  -lite. datum,  n,,  something  given  or  assumed.  —  L. datum,  neut.  pp.  of  dare,  'to  give’.  See  date, ‘point  of  time’,  and  cp.  data.
Datura,  n,,  a  genus  of  plants  of  the  potato  family (hot.)  —  ModL.,  fr.  Hind,  dhatura,  fr.  OI.  dhat- turah ,  dhusturah,  ‘thorn  apple’,  which  is  cogn. with  the  second  element  in  OE.  dweorge-dwostle, ‘penny  royal’,  and  possibly  also  with  L.  festuca, ‘stalk,  stem,  straw’.  See  festuca. daub,  tr.  and  intr.  v.  —  ME.  dauben,  fr.  OF. (=  F.)  dauber,  ‘to  plaster’,  fr.  L.  dealbdre,  ‘to whiten,  whitewash,  plaster’,  fr.  de-  and  albare, ‘to  whiten’,  fr.  albus,  ‘white’.  See  alb. Derivatives:  daub,  n.,  daub-er,  n.,  daub-ery,  n., daub-ing,  n.,  daubster,  n.,  daub-y,  adj. dauberite,  n.,  basic  uranium  sulfate  (mineral.) Named  after  H.  Dauber,  who  analyzed  it.  For the  ending  see  subst.  suff.  -ite. daubreeite,  daubreite,  n„  a  hydrous  bismuth  oxy¬ chloride  (mineral.)  —  Named  after  the  French mineralogist  Gabriel-Auguste  Daubree  (1814- 96).  For  the  ending  see  subst.  suff.  -ite. daubreelite,  n.,  a  chromium  iron  sulfide  (mineral.) —  Named  after  Daubree.  See  prec.  word  and the  combining  form  -lite.
Daucus,  n.,  a  genus  of  plants,  the  carrot  (bot.)  — L.  daucus,  daucum,  fr.  Gk.  Bauy.oq,  SaOxov,  a kind  of  parsnip',  which  is  rei.  to  Thessalian  Gk. Sauxya,  Gk.  Bacpw],  ‘laurel’.  See  Daphne, daughter,  n.  —  ME  doghter,  dohter,  fr.  OE.  deb¬ tor,  dohter,  rel.  to  OS.  dohtar,  ON.  dottir.
uaunt
debarrass
OFris.,  Du.  dochter,  OHG.,  MHG,  tohter,  G. Tochter,  Goth,  dauhtar,  ‘daughter’,  and  cogn. with  OI.  duhitd,  Avestic  dugeda-,  duydar-,  Toch. A  ckacar,  B  tkacer ,  Arm.  dustr,  Gk.  -&uyaTr,p, OSlav.  duSti,  OPruss.  duckti,  Lith.  dukte, ‘daughter’.
Derivatives :  daughter-hood,  n.,  daughter-ly,  adj., daughter-li-ness,  n.
daunt,  tr.  v.  —  ME.  daunten,  fr.  OF.  danter,  don- ter  (F.  dompter),  fr.  L.  domitdre ,  ‘to  tame,  sub¬ due’,  freq.  of  domare  (pp.  domitus),  ‘to  tame, subdue,  vanquish,  conquer’,  lit.  ‘to  accustom to  the  house’,  fr.  domus,  ‘house’.  See  dome, ‘building’,  and  cp.  indomitable.  Cp.  also  tame. Derivatives:  daunt-er,  n.,  daunt-ing,  adj.,  daunt- ing-ly,  adv.,  daunt-ing-ness,  n.,  dauntless  (q.v.). dauntless,  adj.  —  Formed  fr.  the  ME.  noun  daunt, fr.  daunten  (see  daunt)  with  suff.  -less;  first  used by  Shakespeare.
Derivatives:  dauntless-ly,  adv.,  daunt!ess-ness,n. dauphin,  n.,  the  title  of  the  eldest  son  of  the  king of  France.  —  F.,  lit.  ‘dolphin’,  translation  of L.  Delphinus,  lit.  ‘dolphin’,  orig.  a  name  borne by  Guigo  IV,  count  of  Vienne  (died  in  1142) and  by  his  successors.  The  name  Delphinus  was chosen  in  allusion  to  the  three  dolphins  repre¬ sented  in  the  coat  of  arms  of  the  lords  above mentioned.  Hence  the  province  owned  by  them came  to  be  known  as  Delphinatus  in  Latin (whence  F.  Dauphine).  See  dolphin, dauphine,  n.,  a  dauphiness.  —  F.  dauphine,  fern, of  dauphin.  See  dauphin.
dauphiness,  n.,  the  wife  of  a  dauphin.  —  Formed fr.  dauphin  with  suff.  -ess. davenport,  n.,  a  kind  of  writing  desk.  —  So  called from  the  name  of  its  first  maker.
David,  masc.  PN.;  in  the  Bible,  the  second  king of  Israel  and  Judah,  the  writer  of  the  Psalms. —  Heb.  Dawtdh,  lit.  ‘beloved,  friend’,  rel.  to  dddh, ‘beloved,  uncle’,  and  to  dudha'tm,  ‘mandrake’, prop,  ‘love-exciting  (plant)’.  Cp.  dudaim. daviesite,  n.,  a  lead  oxychloride  (mineral.)  — Named  after  Thomas  Davies,  of  the  Minera- logical  Dept,  of  the  British  Museum  (1837-91). For  the  ending  see  subst.  suff.  -ite. davit,  n.,  a  projecting  piece  of  vessel  for  suspend¬ ing  or  lowering  a  boat.  —  OF.  daviet,  daviot (whence  F.  davier,  with  change  of  suff.),  dimin. of  the  PN.  David;  so  called  in  allusion  to  the slaying  of  Goliath.  See  David  and  cp.  -et. davy,  n.,  safety  lamp.  —  Shortened  fr.  Davy  lamp; named  after  its  inventor,  the  English  chemist Sir  Humphrey  Davy  (1778-1829). davy,  n.  (slang).  —  Short  for  affidavit.
Davy  lamp.  —  See  davy,  ‘safety  lamp’, daw,  n„  a  kind  of  crow,  a  jackdaw.  —  ME.  dawe, rel.  to  OHG.  tdha,  MHG.  tdhe,  also  tahele, tale,  idle  (diminutives  of  tdhe),  G.  Dohle;  cp. OPruss.  doacke,  ‘starling’,  ML.  tacula.  It.  tac- cola,  ‘jackdaw’,  which  are  German  loan  words, dawdle,  intr.  and  tr.  v.,  to  waste  (time).  —  Perhaps a  var.  of  dial.  E.  doddle,  ‘to  walk  unsteadily’.
404
Derivatives:  dawdl-er,  n.,  dawdl-ing,  n.
dawk,  dak,  n.,  transport  by  relays  of  men  and horses,  mail  (Anglo-Ind.)  —  Hind,  dak,  ‘post, mail*.
dawn,  intr.  v.  —  ME.  dawening,  of  Norse  origin ; cp.  Swed.  and  Dan.  dagning,  'a  dawning’,  fr. dag,  ‘day’.  Cp.  also  OE.  dagian,  ‘to  dawn’,  fr. dxg,  ‘day’,  Du.  dagen ,  ‘to  dawn’,  fr.  dag,  ‘day’, G.  tagen,  ‘to  dawn’,  fr.  Tag,  ‘day’,  and  see  day. Derivatives:  dawn,  n.,  dawning  (q.v.)
=== leaf check
leaf 222
```


## [2026-09-05T20:07:52.101Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"dheugh\\|duhitár\\|dhug(h)əter\\|dhug\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-05T20:07:52.167Z] TOOL RESULT

```
51913:u. zw. mit der Bed. „stechen, stecken", wahrend fiir dhug- „schiirfen“ kein 
53361:dheugh- — dheub-, dheup- 
53378:dheugh- „taugen, tiichtig (kraftig) sein, sich gut treffen, gliicken; taug- 
53390:schirr, Gefafi"; ir. diian „Gedicht“ ( *dhughna , s. Strachan BB. 20, 16 m. 
53392:schreien"), dual „passend" ( *dhughlo -, Strachan BB. 20, 29) ; aisl. inf. dug a, 
54720:dhug(h)ater-, dhug(h)t(e)r- (a in den endbetonten Kasus geschwunden, 
54729:gegen weitere Ankmipfung an ai. duh- „melken“ oder idg. *dheugh- „taugen“
```


## [2026-09-05T20:07:55.050Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '54715,54745p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== dheugh ===\"; sed -n '53375,53400p' WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:07:55.122Z] TOOL RESULT

```
aus U (Vf. LEWb. 2 s. v.) ; die Yerbindung gewanne an Wahrscheinlichkeit, 
wenn funis aus *fumis dissimiliert sein konnte; wobei die Stellung des 
m vor i (gegeniiber fumus ) als mitbedingender TJmstand in Rechnung zu 
ziehen ware. 

dhug(h)ater-, dhug(h)t(e)r- (a in den endbetonten Kasus geschwunden, 
siehe Bartholomae IF. 7, 53ff.) „Tochter“; Guttural wie bei *egQi)om 
„ieh“, s. d. 

Ai. duhitdr-, ( duhita ), av. dugadar-, duydar-, npers. duxtar , duxt, arm. 
(mit s aus Jc nach u ) dustr , Gen. dster , gr. 'dvydrrjo (Akzentverschiebung 
wie in firjxrjQ , aber noch -dvyarega wie /urjreQa), got. dauhtar , anord. dottir 
(run. nom. pi. dohtrin ), ahd. tohter , lit. dukte, -ers, apr. duckti , aksl. dusti, 
-ere „Tochter“. Lit. bei Bartholomae Airan. Wb. 748, Boisacq 355, auch 
gegen weitere Ankmipfung an ai. duh- „melken“ oder idg. *dheugh- „taugen“ 
(letzteres bei Fick I 4 74). Eber tochar. B tkcicer s. Pokorny Berichte d. 
Forschungsinst. f. Osten u. Orient in Wien, Bd. 3, S. 23 des S. A. 

dhlgh- , ; Schuld, Yerpflichtung“? 

Air. dligim „habe worauf Anspruch, verdiene“, mcymr. dlyu , dleu, dytyu 
„debere“, corn, dylly ds., mbret. dellit ds., air. dliged „Pflicht, Gesetz, 
Recht“, cymr. died, dyled, dyled , me. dylyet ; ,Pflicht“ ; got. dulgs „8chuld < ‘ 
(an Geld); aksl. dhgz „Schuld“ (aus dem Germ.? s. Hirt PBrB. 23, 332, 
Berneker 244). Fick KZ. 22,373, D’Arbois de Jubainville Msl. 7, 293 f., 
Fick 1 4 464, II 4 155, Pedersen KG. I 100, 333, 528, Morris-Jones Welsh 
Gr. 379. 

Die got. Bed. ,,Geldschuld i£ und die brit. Bed. „debere, debitum" sowie 
die gemeinkelt. Bed. „Pflicht a (ir. „verdiene“ ware etwa „ich treibe die 
Schuld eines anderen gegen mich ein £ ‘) stehn sich so nahe, daB Trennung 
=== dheugh ===
Persson Wzerw. 56, 81 f„ Beitr. 555, 588, 653 Anm. 3, Hirt Abl. 134 (Basis 
*dheues-), usw. 

dheugh- „taugen, tiichtig (kraftig) sein, sich gut treffen, gliicken; taug- 
lich herrichten". 

Gr. Tvyydvo) (rev go uni, szvyov, ezvygoa , tet vygy.a) „treffen, antreffen, zu- 
fallig begegnen; ein Ziel oder einen Zweck erreicben; intr. sich vorfinden, 
gerade wobei sein, zufallen“, zvyg „Ge]ingen, Gliickszufall, Schicksal, Los" 
(nicht nach Pedersen KG. I 151 zu ir. tocad „Gliick“, s. u. tenq- „sich zu- 
sammenziehen") ; zei<ya> (zsvgco, Aor. sieved, hom. r ezvy.Eiv, med. zezvy.ovzo, 
zezvy.Eodai — mit sek. k, s. Osthoff Pf. 304 ff. — , Pf. zezevycbg, zhvy.zai, 
zszevyazat ) „tauglich herrichten, verfertigen, herstellen, veranlassen, her- 
vorbringen , zizvoy.opai „mache zurecht, ziele", zsvyog n. ,,alles gemachte, 
Gerat, Geschirr, Zeug, bes. Riistung, Riistzeug, Waffen; Schiffsgerat ; Ge- 
schirr, Gefafi"; ir. diian „Gedicht“ ( *dhughna , s. Strachan BB. 20, 16 m. 
Lit.; nicht besser nach B. bei Fick II 4 153 zu lett. dugdt „wie ein Kranich 
schreien"), dual „passend" ( *dhughlo -, Strachan BB. 20, 29) ; aisl. inf. dug a, 
Praes, dugi, Praet. dug da „von Nutzen sein, taugen, gliicken", Praeterito- 
praesens got. dang, ags. deag, as .dog, ahd. long „es tangt, niitzt‘, Kaus. 
mnd. dbgen „aushalten", as. a-dogian „ds., ordnen", ags. gedlegan „ertragen 
iiberstehn" ; ahd . tuht „Tiichtigkeit, Kraft", mhd. tuhtec nhd. tiichtig = ags. 
dijhUg „kraftig" ; (iiber got. dauhts ,.Gastmahl“ s. Feist GWb. 62 m Lit 
fiber aisl dyggr „treu‘ Fick III 4 207, Falk-Torp u. due m. Lit.); 

lit. daug „viel" ; strittig russ. duzij „stark, fest", poln. duzy .,groti. stark",
```


## [2026-09-05T20:08:04.893Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"pdf page\" WLD_Bd1_pages.txt | head -3; echo ---; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'dhug(h)ater-' in p or 'dheugh- „taugen' in p:\n        print('=== block',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T20:08:07.062Z] TOOL RESULT

```
---
=== block 855                                         dheugh-    — dheub-, dheup-                                                            847 |  | 56 f.), mir. down „dunkel“, cymr. dicnn „subfuscus, aquilus" *dhusno
=== block 876 868                                                dho[u]- : dhu-     — dtalgh- |  | daru f. ,,Schade, Verletzung". ahd. tara f. „Yerletzung“? (Fick III 4 202 | sueht darin kaum besser eine Wz. dher -, aus
```


## [2026-09-05T20:08:10.922Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhugh\\|dheugh\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-05T20:08:10.974Z] TOOL RESULT

```
154:A large number of kinship terms have been reconstructed. They are agreed in pointing to a society that was patriarchal, patrilocal (the bride leaving her household to join that of her husband’s family), and patrilineal (de- scent reckoned by the male line). “Father” and “head of the household” are one: peter-, with his spouse, the mater-. These terms are ultimately derived from the baby-talk sylla- bles pa(pa) and ma(ma), but they had a socio- logical significance in the Indo-European family over and above this, which is marked by the kinship-term suffix -ter-. Related terms are found for the grandfather (awo-) and the maternal uncle (*awon-), and corre- spondingly the term nepét- (feminine *nepti-) applied to both grandson (perhaps originally daughter’s son) and nephew (sis- ter’s son). English soON and DAUGHTER clearly reflect Indo-European *siénu- (from seue-') and dhughater-.
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
392:dhugheter-. Daughter. Germanic *dohtér in Old English dohtor, daughter: DAUGHTER. [Pok. dhug(hjeter 277.]
1409:Dart dhabh- DAINTY dek-1 DAIRY dheigh- DAISY agh-2, okw- DALE dhel- DALLES dhel- DAMAGE dap- DAME deme-! DAMN dap- DAMNIFY dap- Dan? deme-! DANDELION dent- DANE dan- DANEGELD gheldh- DANELAW dan-, legh- DANGER deme-1 DaNIsH dan- DAPPER dheb- DARE dhers- DARK dher-! DASTARD dhé-2 DASYURE dens-2 DATE do- DATIVE do- DATUM do- DAUB _albho- DAUGHTER dhugheter- DAUNT deme-2 DAWN agh-2
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1597:HENCE ko- HENDECASYLLABIC sem-1 HENDIADYS dwo-, sem-1 HENOTHEISM sem-1 HEPARIN yekwr HEPATIC yekwr HEPATITIS yek"r HEPATO- yekwr _ HEPATOGENIC yekr HEPTA- septm HEPTAD septm HeEpPTaTEuCH dheugh- HER ko-
1603:HEXA- s(w)eks HEXAD s(w)eks HEXATEUCH dheugh- HIATUS ghai- HIBERNACULUM ghei-2 HIBERNATE ghei-2.
2075:PENNA pet- PENNATE pet- PENNON pet- PENOLOGY kvej-1 PENSILE (s)pen- PENSION! (S)pen- PENSIVE (s)pen- PENSTEMON sta- PENTA- penkWe PENTACLE penkwe PENTAD penkve PENTADACTYL penkve PENTAGON penkwe PENTAMETER penkwe PENTARCHY penkWe PENTASTICH penkwe PENTATEUCH dheugh-, penkwe PENTATHLON penkWe PENTECOST dekm, penkwe PENTHOUSE (Ss)pen- PENUCHE pa-
```


## [2026-09-05T20:08:12.356Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dwš\\|dwšydn\\|doš\\|dōš\\|duxt\\|dwxt\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-05T20:08:12.404Z] TOOL RESULT

```
PHD.txt:314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:1494:daughter duxt(ar).
PHD.txt:5468:gūhragdānāg gohrag dwāzdahān dwāzdah duxt, Just 1-*dūxtun duxtar ldaw-, gūw- gūwāg 12а} dwàr- dwārīdan dwiristan dwārišn jy)
PHD_mackenzie.txt:2161:duxt [BRTE < A brt-h; dwht l 1M dwxt, N ......] daughter.
PHD_mackenzie.txt:6317:cruc~on dargardih.                         daughter duxt(ar).
PHD_mackenzie.txt:10767:juyisn                                                  l'-~duxt,m
PHD_mackenzie.txt:10772:                           "'U~~t"                      duxtar
PHD_mackenzie.txt:11128:brch                               duxt                          \6~\)
```


## [2026-09-05T20:08:25.300Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint([k for k in d if k.startswith('CEL')])\nfor k in ['CEL','CEL3','SHP','PEI']:\n    if k in d: print(k, d[k].get('title'), '|', d[k].get('kind'), '|', d[k].get('local_file'))\n\"; echo ---; grep -rn \"CEL\" data/verification/sources/refs_online.json | head -5"
}
```


### [2026-09-05T20:08:27.156Z] TOOL RESULT

```
['CEL']
CEL S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997 | catalog | None
SHP J. T. Shipley, Dictionary of Word Origins, New York 1945 | hathitrust_fullview+archive_restricted | None
PEI M. Pei, The Families of Words, New York 1962 | archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt
---
data/verification/sources/refs_online.json:837: "CEL": {
```


## [2026-09-05T20:08:33.979Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==64' PEI.txt | head -40"
}
```


### [2026-09-05T20:08:35.477Z] TOOL RESULT

```
 hyios,  "son",  in  Indo- Iranian,  in  Celtic,  and  in  Slavic  (the  form  represented  by  Russian
44
*de[]  ONE-BRANCH     FAMILIES  45
syn).  In  Anglo-Saxon,  it  produces  sunu,  which  becomes  son  (with sonship,  son-in-law,  sonny,  etc.).  Close  cognates  of  son  are  in  evidence throughout  the  Germanic  branch  (German  Sohn,  Scandinavian  son, sen,  etc.).
The  family  tree  for  the  English  word  is  extremely  simple :
IE  *su,  seu,  sunu  ("to  bear,  bring  forth;  son")
AS  sunu
I Eng.  son,  etc.  (Table  xv,  1)
Another  root  with  extensive  outside  connections,  but  a  single  line of  English  descent,  is  that  of  *dhug{h)9ter,  "daughter".  The  root appears  in  Indo-Iranian  (Sanskrit  duhitd,  Persian  duhitar) ;  in  Armen- ian; in  Oscan  (but  not  in  Latin);  in  Slavic  (Russian  doc\  with  root docer-) ;  in  Greek  {thygater) .  Anglo-Saxon  dohtor,  which  gives  us daughter,  daughter-in-law,  daughterly,  etc.,  has  cognates  in  all  the  Ger- manic languages  (German  Tochter,  Icelandic  dottir,  etc.).  Again,  the English  family  tree  is  extremely  simple :
IE  *cihug(h)3ter  ("daughter")
AS  dohtor
I Eng.  daughter,  etc.  (Table  x,  2,  4)
One  Indo-European  root,  *bhel,  "sound,  roar,  bellow",  has  an extremely  simple  Germanic  development  that  leads  to  Anglo-Saxon and  English  forms.  From  AS  belle  comes  bell  {bell  buoy,  bellwether, bellboy  or  bellhop  are  compound  forms),  while  the  verb  form,  bellan  or bylgan  in  Anglo-Saxon,  goes  on  to  English  bellow.  The  only  thing  bell and  bellow  have  in  common  semantically  is  that  both  refer  to  sounds. The  tree:  jg  ^^-^^^  ("sound;  to  roar,  bellow")
■  \  \
AS  belle  bellan,  bylgan
I  I
Eng.  bell,  etc.  bellow  (Table  ix,  4)
There  is  a  Germanic  root  derived  from  IE  *del,  "to  reckon,  count", which,  appearing  in  Anglo-Saxon  as  tM  (noun)  and  tellan  (verb), gives  rise  to  English  tell  and  its  derivatives,  such  as  teller  and  telltale. From  the  same  root  comes  Anglo-Saxon  talu,
```


## [2026-09-05T20:08:35.737Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"pdf page\" FFD_pages.txt | head -3; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt',encoding='utf-8').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if 'اندودن' in p or 'زدودن' in p or 'دوشیدن' in p:\n        print('=== block',i, p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:08:37.329Z] TOOL RESULT

```
1:[pdf page 1]
24:[pdf page 2]
59:[pdf page 3]
115
=== block 36 [pdf page 37] انا ی فعلهای فارسی دری می‌گوید: نباید سخن گفت ناساخته نشاید بریدن نینداخته  < ایرانی باستان 12-13-1۵*. 120
=== block 58 [pdf page 59] چا انا نا فعلهای فارسی دری دوختن (۱) دوخت + فارسی میانه 4071 < ایرانی باستان 4203-1۵*. برای 2 > آراست. 42 
=== block 62 [pdf page 63] ها فعلهای فارسی دری زدن زد < فارسی میانه 240 + ایرانی باستان ۵-12[*. برای ۵ > آراست. 3[صورت : ضعیف 20[ است
=== block 89 [pdf page 90] نهرست واژه‌ها ۸۵ 406 (ريشه < بوی بردن - پی بردن) ۳۹ ۴۰ ۵ ۴۹ 2 ۳۹ 7 (ريشه < حرکت کردن) ۰۴۸ ۷۳ 8 (ريشه < نجا
```


## [2026-09-05T20:08:44.731Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['FFD'].get('page_offset')); print(d['FFD'].get('cites'))\nprint('---AEF'); print(d['AEF'].get('cites'))\nprint('---SHP'); print(d['SHP'].get('cites'))\nprint('---CEL'); print(json.dumps(d['CEL'],ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-05T20:08:46.415Z] TOOL RESULT

```
115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
None
---AEF
None
---SHP
None
---CEL
{"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Haus printing is not digitised anywhere found. HathiTrust full-text search (search-only volumes) can confirm whether a word occurs, via a browser."}
```


## [2026-09-05T20:08:55.034Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf-8').read().split('\\f')\nt2=open('FFD_pages_faseng.txt',encoding='utf-8').read().split('\\f')\nfor i in (36,58,62):\n    print('========== fas block',i)\n    print(t[i][:1400])\n    print('---------- faseng')\n    print(t2[i][:1400])\nEOF"
}
```


### [2026-09-05T20:08:56.799Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'FFD_pages_faseng.txt'
```


## [2026-09-05T20:08:59.389Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls && python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (36,58,62):\n    print('========== block',i)\n    print(t[i][:1500])\nEOF"
}
```


### [2026-09-05T20:09:01.337Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
========== block 36
[pdf page 37]
انا ی فعلهای فارسی دری
می‌گوید:
نباید سخن گفت ناساخته نشاید بریدن نینداخته

< ایرانی باستان 12-13-1۵*. 1200 پیشوند فعلی است. برای 13 > اراست. 131
صورت اصلی 13 است» # پیش از 1 به #بدل شده است. 13 صورت بالاندة 12۴است»
به معنی «دویدن». از 12 در فارسی دری «گداختن» و «پرداختن» و «تاختن» هم آمده‌اند
ی گداختن و پرداختن و تاختن.

انداز ج فارسی میانه ۳23۵437 < ایرانی باستان 8۵۳-130-۸*. برای ۵ > آرای. 5
به‌جای ا آمده است.

اندوختن

اندوخت < فارسی میانه 1304071 < ایرانی باستان 827۳-120-1۵*. برای 18 >
آراست. 1200 پیشوند فعلی است. 408 صورت اصلی 127 استء 8 پیش از ۲ به * بدل
شده است. ريشةٌ 1208 به معتی «پرداختن» است.

اندوز <ج فارسی میانه 2 جح ایرانی باستان 2۵-4۵-8۵ *. برای ۵ > آرای.[
به‌جای 8 آمده است.

اندودن

اندود < فارسی میانه 132480 < ایرانی باستان ۴۳۵۳-4-16 برای 1۵ -> آراست.
0 پیشوند فعلی است. ربشهٌ 7 به معنی «پاک کردن» است. > زدودن.

اندای < فارسی میانه 12437 + ایرانی باستان 27-43-۵2 *.

2 نشانه‌ای بوده است که برای ساختن مادةٌ مضارع از ريشه به کار می‌رفته. 430
صورت بالانده و 5 صورت ضعیف ريشةٌ 42۷ هستند.

اند یشیدن
اندیشید + فارسی میانه 82048374. 1248310 مادءٌ ماضی جعلی است. از مادة

========== block 58
[pdf page 59]
چا انا نا فعلهای فارسی دری
دوختن (۱)
دوخت + فارسی میانه 4071 < ایرانی باستان 4203-1۵*. برای 2 > آراست. 42
: صورت اصلی 42 است. 3 پیش از 1 به #بدل شده است.
دوز + فارسی میانه 432 + ایرانی باستان 4۵-۸*. برای 2 > آرای. 6 به جای ۴ آمده
است. ريشةٌ 1421 به معنی «دوختن» است.
دوخمن(۲)
دوخت + فارسی میانه 457 « ایرانی باستان 4۵-1*. برای 1۵ > آراست. ۵28
صورت اصلی 4205 است. 8 پیش از ۲ به #بدل شده است.
دوش + فارسی میانه 435+ ایرانی باستان 5.۶42۵ برای ساختن ريشةٌ جدید به ريشه
افزوده شده است. 8 پیش از دبه #بدل شده است. ريشهٌ 4208 به معنی «دوشیدن» است.
دوشیدن
دوشید + فارسی میانه 45810. 0 مادهٌ ماضی جعلی است از 465. مادهٌ مضارع
به معنی «دوشیدن» است.
دویدن
دوید < فارسی میانه 48۷۲۵. ماد ماضی جعلی است از 7 و ۲۵. 489 مادةٌ مضارع
است.
دو < فارسی میانه هل + ایرانی باستان *-42۷۷*. برای 2 > آرای. ريشهٌ 40۷ به
معنی (دویدن» است. ۱
دیدن
دید <ج فارسی میانه 474 « ایرانی باستان ۵۲-1۵*. برای 48 > آراست. ريشة 7
به‌معنی «دیدن» است.

========== block 62
[pdf page 63]
ها فعلهای فارسی دری
زدن
زد < فارسی میانه 240 + ایرانی باستان ۵-12[*. برای ۵ > آراست. 3[صورت
: ضعیف 20[ است» به معنی «زدل).
زن < فارسی میانه 227 < ایرانی باستان «۵[*. به 48[ چیزی برای ساختن مادهٌ
مضارع افزوده نشده است > اوژدن.
زدودن
زدود < ایرانی باستان ۶2-43-12 برای 1۵ -> آراست. ۳۶ پیشوند فعلی است. ريشهٌ
تا به معنی «پاک کردن» است.
زدای + ایرانی باستان 8ر12-437-2* 22 برای ساختن مادهٌ مضارع از ريشه به کار
می‌رفته است. 413۷ صورت بالانده و ۵5 صورت ضعیف ريشةٌ 4۵۷ هستند > اندودن.
زیستن
زیست < فارسی میانه 2731» صورت کهنتر ۰.2۷181 27181 مادةٌ ماضی جعلی است.»
از 27۷ مادةٌ مضارع.
زی + فارسی میانه ۰27 صورت کهنتر 27۷« ایرانی باستان ۷۵[*. 7۷2[ صفت است
که مادةٌ مضارع گرفته شده و از ریشهٌ ۲[: زیستن» و پسوند 2 ساخته شده است.
ساختن
ساخت < فارسی میانه ۶371 + ایرانی باستان ۹21۵". برای 1۵ -> آراست. ‎٩3‏
‏صورت اصلی 835 است» ۴ پیش از ۲ به #بدل شده است. 83 صورت بالاندةٌ 82۴ است و
ريشهٌ 8۵ به معنی «توانابودن» است.
ساز < فارسی میانه 932 < ایرانی باستان ۹30-۵". برای 2 > آرای. ۴ به 6 بدل شده
```


## [2026-09-05T20:09:15.527Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n \"dōxtan\\|doxtan\\|dōšītan\\|duxt\\b\\|dwht\" NYB_vol2_glossary.txt | head -10; echo \"=== HUB ===\"; grep -n \"duxtar\\|dōxten\\|döxten\\|andūdan\\|zudūdan\" HUB.txt | head -10"
}
```


### [2026-09-05T20:09:15.700Z] TOOL RESULT

```
=== NYB ===
1413:duxt [dwht'; BRTH] daughter 2%. 917, 1518.25 259, 261, 11629; with the indef. art. duxt-ē [BRTH-y] 14%; cas. obl. duxtar [dwhtl] 152°; 6 duxt [BRTH] 957; hac pus tài ~ both sons and daughters 24?3, Av. (748) dugedar-, duydar- nom. dugodā, duyča; MPrs dwat (dwxš, v. Benveniste, BSL 47, 1951, 21; KZSPrs 1. 26 dwhSy); NP duxtar, archaic also duzt.
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1895:handóxtan [hndwhtn'] to collect, to ac- quire, to gain 73°12, — MPrs pres. pass. 3d p. pl. ’ndweyhyynd (Sogd 165. 17); Paz. NP andodtan, NP also andozidan; < ham + tóxtan (g. v.). :
2103:(1249) yada yat. — B. Izäfat. Relative clauses are often nominal without the copula, e.g. hàn + hac tō kas he who is thy inferior 685; han fradand +-$ andar aškamb this child that is in her womb 123; hence the :izäfat construction de- veloped: by means of 4, originally the subj. of a nominal clause without the copula, a subst., an adj., a prepositional attribute or an adv. is added to a subst. as its qualifier; I shall call these qualifiers relative attributes. A subst. added to a subst. in this way is the equivalent of our genitive, or it is in apposition. The relative attribute is 1. placed after its headw.: duxt % en varzekar the
2401:pret. pass.: ~ en dam dāt 10312313 (on 3%: ~ kart AWH-wm v. s. v. k- and -m); — my: a) izdfat + ~: kanicak i ~ 7!; b) placed before its headw.: cif i ~ fradandčin the conditions of my children 559; Hamāk i ~ duxt 261; ē (lo) ~ pit u € ~ brat 10018; c) definite rel. attr.: ēt i ~ zan 3215; õi 4 ~ mart i ahlav 3914-15, Ot i ~ pus 5118-19; elliptically: han i ~ my house (family) 3717-18; én i ~ my religious duty 535; — after prepositions: apük, apar, hac, 6, pat ~; ~ rād. — 2. the form normally used as the cas. rect. ‘I’: man Šāhpuhr hom 1514; ~ dānēm 21? etc. — 98° STHn-yt' (imp.) L: if an imp. has
3385:sälak [s?lk' ; SNT-k'] adj. of the preceding w. used in composition with a numeral: duxt-é ... 3-— a three year old daughter 14%; dāt + 15-— the age of 15 years 3! etc. ; ka Zartuxšt 7-~ būt 5217-18, 7-~ homänäk about seven years old 26°; — in repe- titions the suff. -ak may be added to the last sal only: hac 10 sal tai 90 ~ 201; — used for sal: hac 7 ~ apäc since seven years 16%; cf. sih-sälak, sih-säleh.
3642:širčnak [šylynk'] sweet, pleasant, gentle 1710, _ MPrs.šyryn (A-H II); NP širin. Šišin-duxt [šyšyndwht'] n. pr. fem. ‘the daughter of Š” 116°. 11711, — Cf the names Ltolvng, Žiotvviog and Sissi, Justi 303b sq. (Cat. 19-21. 96-98 emends with- out sufficient reason to Šošan).
5140:dugedar-, duydar-: duxt Duydö.vä-: Dugdäv
5779:'ndweyhyynd: handoxtan
5955:dwxt: duxt
=== HUB ===
4099:ap. *duxtd neben duxtar -— ap. *diixtaram (vgl. auch pad-andar *Stief-
```


## [2026-09-05T20:09:17.464Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC dheugh/dhugh ===\"; grep -n \"^dheugh\\|^dhugh\\|dhugəter\\|dhugh\" IEC.txt | head -10; echo \"=== IEC dheu ===\"; grep -n \"^dheu-\\|^dhāu\\|^dhōu\" IEC.txt | head -10"
}
```


### [2026-09-05T20:09:17.544Z] TOOL RESULT

```
=== IEC dheugh/dhugh ===
2857:dheugho “make, fashion, mould, fit; be fit- ting, be fit, be useful’. Cf. dhugh-. WP I, 847 Skt. dóhàmi ‘exploit’; Ober cf. ha-dugà *in-
2869:dheugho (dhou&h-, dhugh-) ‘beat, strike, bully’. Skt. dóhāmi (2) ‘pain’; Av. duz- ‘torment, cheat’; Gk. cf. tugkhánō: tukhé; Li. (o-gde) daužiu, -ti ‘strike, beat, thrust; Latv. dauzu, -t, id.
3036:dhough- ‘avail WP I, 847. See dhugh-, dhughno-, dheughó Myc. (ambig.) touka (epithet of garments); Venet. fougont- (epithet of Rehtiia); OHG toug, OE deéag, pret-pres. ‘avail’; MHG tougen ‘bear’; OE diegan, id. and ‘survive, benefit; Pol. duży ‘big’; dużo, adv.; Li. daug, Latv. daudz ‘much, many”
3242:dhugh- “good, adequate, proper, acceptable. Cf. dhough- Ober cf. ha(m)-dugà ‘feat, record, statute’; Myc. cf. opi-suko- “an operative subject to tribute’; Olr. cf. dual, Ir. dual ‘due, proper’; OHG tugan; OE dugan; ON duga 'avail, suf- fice beside OE dogian ‘endure’; ON dugr ‘strength’; cf. also OHG tugida, tugund; OE dugup “virtue”; Venetic fugont-, fougont-; Li. cf. džiuga ‘joy’. Extn. in Gk. sukhnós “long, numerous, frequent’; OLat. duenos, Fest duo- nus; Lat. bonus. (Go. daühts ‘feast’ is of ambig. origin. See dhu£gh-)
3244:dhughó (dhungh-) ‘strike; meet’. (The Hitt. and Li. evidence is ambig.) Hitt. tukka- (/befall; be of importance’. Cf. tuk-); Gk. tugkháno, aor. étukhon; tükhe, Cret. thükha ‘luck’; Li. dunZu & dūžtu, inf. düZti ‘burst, break’; düZis “blow?
=== IEC dheu ===
2872:dheu- (1) “flow. Cf. dhouos, dheunt. WP I, 834 Skt. dhávate, 3s.; Gk. théo, théwo ‘run, scud'; Gallo-Brit. Deva (n. of River Dee); Lat. cf. fons: fontis (fr. *dheunts fountain); Gaul. cf. divona ‘fountain’. (Isophonic w. Go. diwan 'to die")
2873:dheu- (2) “bright; shine, daytime’ Skt. cf. dhavalah ‘glistening’; Gk. cf. theion 'sulphur, theo (2) ‘shine’. Perh. also in theiló-pedon 'sunny spot'; cf. also leuka-théa (ambig.) beside théā ‘view, sight; OS cf. (?) -digu, -du in hiu-digu, -du ‘today’: OHG hiu-tu, -to; uncertainly Arm. -Éean in tunfean ‘of the daytime’
```


## [2026-09-05T20:09:29.912Z] TOOL CALL #56: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:09:29.918Z] TOOL RESULT

```


```


## [2026-09-05T20:09:35.451Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0ugh%E2%82%82t%E1%B8%97r",
 "prompt": "Give the full etymology section: what is the reconstruction, what does it mean, and what does the page say about the traditional derivation from *dʰewgʰ- \"to milk\" (i.e. \"milker\")? Quote any statement about whether that connection is accepted or rejected, and list the descendants for Indo-Iranian (Sanskrit, Avestan, Old Persian) and Germanic/English."
}
```


## [2026-09-05T20:09:36.750Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full Persian entry: etymology of دوشیدن (to milk), Middle Persian forms, Proto-Iranian and PIE reconstruction cited, and any related forms mentioned (دوغ, دوشیزه)."
}
```


### [2026-09-05T20:09:42.192Z] TOOL RESULT

```
# Etymology of Proto-Indo-European *dʰugh₂tḗr

## Reconstruction and Meaning
The reconstructed form is **\*dʰugh₂tḗr**, meaning "daughter."

## Traditional Derivation
The page proposes a derivation from **\*dʰewgʰ-** ("to produce"), with the original meaning being "the (potential) suckler, the one that draws milk." This etymology is presented as a hypothesis: "Perhaps from *[\*dʰewgʰ-](/wiki/Reconstruction:Proto-Indo-European/d%CA%B0ewg%CA%B0- 'Reconstruction:Proto-Indo-European/dʰewgʰ-')* ("to produce"), originally meaning 'the (potential) suckler, the one that draws milk.'"

The connection is supported by comparative evidence from Sanskrit दुहे (duhé) and दुग्धे (dugdhé), combined with the agentive nominal suffix **\*-tḗr**.

## Selected Descendants

**Indo-Iranian:**
- Sanskrit: दु॒हि॒ता (duhitā́)
- Avestan: dugədar- (Gathic)
- Old Persian: *duhçī

**Germanic:**
- Gothic: dáuhtar
- English: daughter (descended from Proto-Germanic **\*duhtēr**)
```


### [2026-09-05T20:09:43.953Z] TOOL RESULT

```
# دوشیدن (dōšīdan) - Persian Entry

## Etymology
The word derives from Middle Persian *dwšytn'* (dōšīdan, "to milk"), inherited from Old Persian *dauxšatī*, which comes from Proto-Iranian *dáwxšati* ("to milk"). The ultimate source is Proto-Indo-European *dewk-*, as seen in Latin *duco*.

## Meaning
**Definition:** "to milk"

## Related Forms
The entry mentions comparative forms across related languages:
- Baluchi: *دوشگ* (dōšag, "milk")
- Northern Kurdish: *dotin*/*doşîn*

## Alternative Forms
- Literary/archaic: *دوختن* (dōxtan/duxtan)
- Colloquial (Kerman, Rochan): *دوشتن* (dōštan/duštan)

## Linguistic Note
The verb shows inheritance through multiple ancient language stages, demonstrating continuity from Proto-Indo-European through Middle Persian to modern Persian dialects. The etymological chain illustrates how this agricultural term traveled through millennia of language development across the Iranian language family.
```


## [2026-09-05T20:09:55.359Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%AE%D8%AA%D8%B1",
 "prompt": "Give the Persian entry's etymology for دختر (doxtar): Middle Persian, Old Persian, Avestan, Proto-Iranian and PIE forms cited, plus any note on the meaning \"milker\". Also anything on دخت (doxt)."
}
```


## [2026-09-05T20:09:56.070Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%BA",
 "prompt": "Give the Persian entry for دوغ (doogh): etymology, Middle Persian form, Proto-Iranian reconstruction, and meaning."
}
```


### [2026-09-05T20:10:01.118Z] TOOL RESULT

```
# Etymology of دختر (doxtar)

## Etymology Chain
The word derives from **Middle Persian** *dwhtl* (/duxtar/), which came from **Old Persian** *duxçī-*, ultimately from **Proto-Iranian** *dúgdā*.

## Proto-Indo-European Origin
The page traces the lineage back to PIE *dʰugh₂tḗr*, showing cognates across Indo-European languages including English "daughter" and Sanskrit *duhitā*.

## Note on "Milker" Meaning
The provided content contains no discussion of a "milker" meaning for this term.

## Related Term: دخت (doxt)
The entry lists *doxt* as a related term but provides no detailed etymological information about it separately. It appears to be the oblique case stem from which the fuller form *duxtar* developed.
```


### [2026-09-05T20:10:02.648Z] TOOL RESULT

```
# Persian Entry for دوغ (Doogh)

**Etymology:** Borrowed from Parthian *dwwg*, derived from Proto-Iranian *\*dáwgah*. The term relates to Persian verbs meaning "to milk."

**Middle Persian Form:** Not explicitly provided in the source document, though Parthian *𐫅𐫇𐫇𐫃* (dwwg) is identified as the immediate ancestor.

**Proto-Iranian Reconstruction:** *\*dáwgah*

**Meanings:**
1. Buttermilk
2. Doogh—"a carbonated or noncarbonated yoghurt drink"

The entry notes cognates in Kurdish and Northern Luri languages, plus a connection to Sanskrit *dugdhá* (milk-related term).
```


## [2026-09-05T20:10:10.247Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4%DB%8C%D8%B2%D9%87",
 "prompt": "Give the Persian entry for دوشیزه (dušize): etymology, Middle Persian form, meaning, and any statement about a connection to دوشیدن \"to milk\"."
}
```


## [2026-09-05T20:10:10.578Z] TOOL CALL #62: WebSearch

```json
{
 "query": "Azarmidukht name etymology Middle Persian āzarm daughter Sasanian queen"
}
```


### [2026-09-05T20:10:14.995Z] TOOL RESULT

```
# Persian Entry: دوشیزه (dušize)

**Etymology:** The term derives from Middle Persian _dwšyck'_ (dōšīzag).

**Meanings:** The word functions as a noun with two primary definitions: (1) a virgin, and (2) a girl, damsel, or maiden.

**Middle Persian Form:** _𐭣𐭱𐭰𐭪_ (dwšyck' /⁠dōšīzag⁠/)

**Connection to دوشیدن:** The provided Wiktionary entry contains no information establishing any relationship between دوشیزه and the verb "to milk" (دوشیدن). The etymology section only traces the word back to its Middle Persian ancestor.
```


### [2026-09-05T20:10:18.884Z] TOOL RESULT

```
Web search results for query: "Azarmidukht name etymology Middle Persian āzarm daughter Sasanian queen"

Links: [{"title":"Azarmidokht","url":"https://en.wikipedia.org/wiki/Azarmidokht"},{"title":"Talk:Azarmidokht - Wikipedia","url":"https://en.wikipedia.org/wiki/Talk:Azarmidokht"},{"title":"User-submitted name Azarmidokht - Behind the Name","url":"https://www.behindthename.com/name/azarmidokht/submitted"},{"title":"Persian Submitted Names - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/persian"},{"title":"Adur-Anahid","url":"https://en.wikipedia.org/wiki/Adur-Anahid"},{"title":"Khwarranzem","url":"https://en.wikipedia.org/wiki/Khwarranzem"},{"title":"Boran","url":"https://en.wikipedia.org/wiki/Boran"},{"title":"Banbishn","url":"https://en.wikipedia.org/wiki/Banbishn"},{"title":"Azarmidokht facts for kids","url":"https://kids.kiddle.co/Azarmidokht"},{"title":"What Does The Name Azarmidokht Mean?","url":"https://www.names.org/n/azarmidokht/about"}]

Based on the search results, here's what I found about the etymology of Azarmidukht:

Her original name was Middle Persian Āzarmīgdukht, meaning "daughter of the respected one", referring to her father Khosrow II. 

More specifically, the name was possibly derived from Persian āzarm meaning "modesty, shame; honour, respect" and dokht meaning "daughter".

Azarmidokht was a Sasanian queen of Iran from 630 to 631, and she was the daughter of king Khosrow II.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:10:33.338Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'بیدخت' in p:\n        print('leaf',i,'printed~',i-222)\nEOF"
}
```


### [2026-09-05T20:10:35.018Z] TOOL RESULT

```
leaf 56 printed~ -166
```


## [2026-09-05T20:10:37.867Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(548,566):\n    p=t[i]\n    if 'یدخت' in p or 'بید' in p:\n        print('=== leaf',i)\n        print(p[:2500])\nEOF"
}
```


### [2026-09-05T20:10:39.663Z] TOOL RESULT

```
=== leaf 552
که پس رکیوین کودرز باشد .
یحو هر - کنابه از مردم بی هنرویی
عفل و هیچمکاره باشد .
کنابه ازگوشت است که بتازی لحم کوند .9
لیکستن « بکر اول بروزن دلبستن»
بمعنی درماندن و عاجز شدن باشد .
و عاجز شده - و محبوس و بندیرا گویند.
بیکشت مه بنتح اول وضم ثالث بر وزن
زردشت » هر چیز کهآ نرا از یخ بر کنده باشند
ماشد درخت و امثال‌آن » ومجای شین قطه دار
صین ی نقطه هم آمده استه وف ورست ات
چه در فارسی هر دو بهم تبدیل می‌بابند چنانکه
ور فواید گذشت .
بیخ کوهی - بر کاف بواو رسیده
شو کران باشد و آنرا بیونانی نودربون کوشده
و بپترین آنرا از تفت آورند و تفت از اعمال
بزد است .
(۱) چك : خا.
( رن
۱۳۳ ت
ی خویش ه با واو ممدوله‌پروزن
بی دیش ؛ بی خود و بی‌هوش را کوبند .
لی خی لسن با :ای فرشت » بمعنی
ی خیله » با خای نقطه دار بر وزن بی
حیله . خرفه را کونند و جربی بقلة الحمقا
خوانند .
فيك بکسر ارل و سکون ثانی ودال»
نام درختی است مشهور و آنر! بعر ی صفصافی
خوانند ۴ - و تام دیوی بوده در مازسران که
رستم او را کشت - و بمعنی «باشید» و «بوید»
ضت؟ - و کرهکی را نیز گویند که کاغذ
وجاههای شمین‌را
و تباه مازد؟ -
و بمنی ببهوده
و می فایده و نا
سودمند باشد یه
وفتی که مرادف بادباشدچت‌انکه گونند «بادویید»
بمنی بی فایده و ناسودمند - و بزبان حندی تلم
کتایی است6 مشثمل‌براحکام‌دین حندوان وباعتقاد
ص ۷۲۹ ۰ .
۴ - بایراییان کفت بیدار بد
۴ - رف : بت (یکسر اول).
زییکار دشمن عشوار ببد. فر دوسی‌طوسی.
قبه در سفحه ۳۳۳
=== leaf 553
ابثان کتاب آسمانی است ت - و ممعنی حوش وشمور
هم بنظرآعده است و در مویدالّلاء موش‌لوشته
بودند که عربان فاره خوانند» وا اعلملا .
يفاك « ممروف است ی که طلم و سم
باشد؟ - و نام شهری است تب از تر کستان وبادشاه
آن‌شهر کافورنم جادوبی‌بوده آ دمی‌خوار. رستم‌او را
کرفت و کشت رآن شهر را عفتوح سلخت ۰
بید‌ار مقر - کنابه از هردم عافل
و هوشیار و خبر دار باشد .
ید بر که - برآوزن دبکه ب رکه, نوعی
از پیکان تبر باشد شبیه ببر که بید.
بیدخج ه بفتح اول بر وزن برزخ» اسب
جلد و نند و تیز خیز را کویند. وبکر اول هم
هت ات ۲ ۹
ید خام - بکر اكث . عود خام را
گو مد .
بید خت ؟ - با بای مجهول بر وزن
کمخت , ستار؛ زهره را گویند که صاحب فلك
(۱) چك : تا .
لید‌ستر * ع_ با ثانی مجهور و ثای
فرشت(۱) بر وزن بی مسطر ء نام حیوانی است
بحری که هم در
آد نوی نت
خوانند .
دید ست و باشدن ژتابه‌ازس اسبه
کردیدن باشد .
بیك‌ طبر ی « نوعی از بید باشد وبعضی
س مق و۱ مس طبری: کرشة ۷ و بستی
پید موله را کویند که بید مجنون باشد .
لیفق ح_بروزن احمق, ببادة شطرنج‌را
کویند وآن مهره ای باشد از حملةٌ مپره حای
شطرنج. و ععرب‌یاده است ۸ .
یدق سیم - کنابه از کو کب و سثاره
باشد .
۳ ت رد 7 فوروز نامه ۹۱۳ ۵ص۵/.
بضی اسای ی بدوح ۰ ای وی
هزدسنا ۰ و۳۲۹
۷ .2680011868 #«نأه۹:ناتی۱5:۹*.
۱ رگ : آش بجگان .
فهرست مزدسنا .
بقیه ازصفحهٌ ۳۳۲
=== leaf 554
بید کیا
بید گیا - بکر کاف فارسی و نحتانی
بالف کشیده . نوعی از حرشف است که کنگی
باشد. سرد دخشك است در اول. جراحتهای‌نازمرا
غافع باشد .
ثيل لا - پکس اول وئالث وسکون‌نانی
مجپول و لام بالف کشیده . سخنان بی ربط
و حذبانرا گونند .
بیدمال - با میم کشیده بر وزن تيك
فال » با کردن زنگه باشدازرو ی آیینه وشمشیر
و سایر اسلحه بچوب_بید با چوب دیگر که
این کار را شایف.
دیل مشاث - نوعی ازیید است که بهار
آن عنی شکوفه‌آن بغایت خوشبوی هبباشد (۱)
و عرق را یجهت نفریح دل و تبرید
باشامند ۷ .
نید موش « بروزن فبل گوش, بععنی
بیدمشك‌باشد وآنراکرية بید هم میگوند.
لیدواد - با ثانی مجهول بر وزن
یشواز. نام کوهی است از ولات ماوراد النهر.
بیلو فك - با واو بروزن ربشخند » نام
داروبی است که آنرا شادنه گویند و بجهت
داروی چشم بکار برند .
لهر ح کر اول و مکون ثانی و رای
فرشت ۰ جامه خواب را گویند مانند نهالی
ونوشك» وآنجه کتردنی باشد بجهت خواییدن
خصوصا - و ماه و طوفان را نیز گفته اند -
و بمعنی حفظ و از بر کردن هم آمده است ۴
و در عربی چاء را کویند ۴ - و بهندی بمعنی
برادر و پهلوان و شجاع باشد- و بش کی يك را
)0 ث ۳ خوشو باشد.
۱ رك : صفحه قبل ح ۷.
گویند که عدد اول است.
لیر اد - - باثانی مجهول بروزن شیرازه
شاخ حیوانات را گوشد.
ثبر ان « بروزن ومعنی ویران باش دکه
نقیضی آماد است * .
یر انه « بروزن ومعنی ویرانه است که
خرابه بائد ٩‏ .
ثیر ا۵ ۱ س دوطرف راء را گوشد که در
آن جاده نناشد و کنابه از عردم نا هشخص -
وکارهای ناشاسته باشف ‏
ثیر بو شا ۷ - با بای ابجد بواو رسیده
وشین قرشت بالف کشیده, بلفت زند وپازند (۷)
خبار بادرنگ را کویند.
یر رگ - بفتح زای تفطه دار و سکون
دال بی‌نقطه. صمفی باشد مانتد مصطکی . سبك
وخشك و بوی یزی دارد ۰ و طبیمت آن گرم
و خشك است » علاج عرق النساء و نقری کند
وحیض را براند ؛ و بچه مرده از شکم بیندازد
ودر مرهمها نیز داخل کنند »و ممرب آن بارزد
باشد ۸ - و براده‌ای رائیز گوبندکه روبگران
ازسوش سوهان جمم کنند - و براد فلزات را
کتهاند مطلقا - و دارویی باش که بردمید کیها
مالئد تامگس برآن ننشیند وبه کند - و چیززبرا
فیز وتا کته رویگران بجپت لحیم کردن
ووصل نمودن چیزها بکار برند .
ثبر ۵2 « با ها ء بر وت و ممنی اول
برزد باشد؛ وآن صمفی است بفایت گنده ومنتن
تن انتف ۳
1 اوسنابی ۵۷1۳۸ (اطلاع) «اسفا ۱: ۲ ص۲۹ درپهلوی ۷۱۲111 بمعنی خردمندی‌وهشیاری
ی . گودی ۱۷۹۲ ومکری و1 .۰ و13 (آموخته وباد گرفته) ۰ رل ارداو بر افنامه بقلم نگارنده
ف .2۲ (: - شش ( چاه) . و۲ و فان : ۵ د رظ : ویرالد .
۱ - بپاوی 2۳6725 « منای ۰۲۹۷ . - هز, 0۷۵۱15 بادرنک « بوستی .
شدهش. ۳« ۸ ره : برزه و سرزی . - ره : سرزد وببرزی -
=== leaf 555
- ۳۳ 7
یر دک بنتم رابع بر وزن نك بی »
بمعئی برژه انته ات صمفی‌باشف منتو, که‌بارزد
گوشش ٩‏ .
یرگ ؟ « بنتح اول و ثالث بر وزن
سنجق ؛ علم را گوشد - و یمعتی شقه جر مر
رنگین هم‌آعده است که برسر علم و نیزه و کللاه
خود بشدند.
یی د که - بکسر اول و سکون نانی
وفتح ثالث وکاف فارسی سا کن» بیدل‌وبی‌غیرترا
بیر گند ب یفتح کاف فارسی بروزن
زیر بند . نام شهرست که معرب آن بر جند
است ۴
لیر ۵ « بفتح اول و ثالث بروزن ضیغم »
نوعی‌از بارچة رسمانی باشد شبیه بمثقالی عراق»
لیکن ازاو بازیکتر وناز کتر است ۴
بیرون است که تقض اندرون باشد 8
وسکون انی و رابع و جیم بالف کشیده و بسن
بی‌نفطه وبای اسجد ژده : کاهی است که آن را
بوی مادران گویند ۳
پر نگ - با انی مجهول بر وزن
نبررنگه» نان و (۱) هیولابی باشد که نقاشان
ومصوران عرتهة اول مر کاعف و دیوار بکشنشویعد
از آمیزی نسانند»
وت ونزد محتقان ظهور احدت است 7
الم وحدت که عباوت از عرنبةٌ بی‌مرتبه بود که
آن اسفاط اضافات ذات معر! ازلای اسما وصفات
است تعالی ونقدس .78
لی‌دو - بر ورن ک
وا بظه زوا مول و غیرآن عافت.-. و کضایه از
هردم بی انفعال )۳( و بی‌آزرم وک یکه مخنان
ناخوش بروی کی بگوید ۷
ار ود ح بر وزن فیروز ۰ سنگی باشد
سبز رنگه شبیه بزمرد» لیکن بسیار کم بها و کم
شمت ۸ . چ
که
۲( چجش: تس و
۱ 5 سرزد و ببرزه.
میدان اسب دوانی اصب کننش. «حفادی
, جرج
میکند «جغرافیای سیاسی . کیپان ۲*۵ -۹».
۴ - یربا سپرگر که ومنفر پولاد
۵ رك: بیرون.
۷ - امروز «بی‌چشم ورو؟ و
سیستّان
برای شهر بیرجند آب تهیه
۸ - رگ : قیروژه .
چونکه بیرنگی اسیر رنگگ شد
0 «اعذا ۱
مه درصفحة ۳۳۹
```


## [2026-09-05T20:10:53.749Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqt553.jpg \"https://archive.org/download/borhan-ghate-v1/page/n553.jpg\" -w \"%{http_code} %{size_download}\\n\" && file bqt553.jpg"
}
```


### [2026-09-05T20:10:57.358Z] TOOL RESULT

```
200 512022
bqt553.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-09-05T20:11:01.793Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && (command -v convert && convert bqt553.jpg -crop 2479x800+0+2650 +repage -resize 200% bqt553_foot.png && file bqt553_foot.png) || echo \"no imagemagick\""
}
```


### [2026-09-05T20:11:07.836Z] TOOL RESULT

```
/usr/bin/convert
bqt553_foot.png: PNG image data, 4958 x 1600, 8-bit grayscale, non-interlaced
```


## [2026-09-05T20:11:09.952Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt553_foot.png"
}
```


### [2026-09-05T20:11:10.248Z] TOOL RESULT

```

```


## [2026-09-05T20:11:10.246Z] INPUT

[Image: original 4958x1600, displayed at 2000x645. Multiply coordinates by 2.48 to map to original image.]


## [2026-09-05T20:11:34.684Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && convert bqt553.jpg -crop 2479x750+0+2150 +repage -resize 180% bqt553_foot2.png && echo ok"
}
```


### [2026-09-05T20:11:37.531Z] TOOL RESULT

```
ok
```


## [2026-09-05T20:11:39.880Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt553_foot2.png"
}
```


### [2026-09-05T20:11:40.143Z] TOOL RESULT

```

```


## [2026-09-05T20:11:40.141Z] INPUT

[Image: original 4462x1350, displayed at 2000x605. Multiply coordinates by 2.23 to map to original image.]


## [2026-09-05T20:12:07.407Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && mkdir -p ocr/BQT && cat > ocr/BQT/333.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 333 = archive.org borhan-ghate-v1 leaf n553; read from the page image 2026-09-05]\n\nHeadword (main text):\nبیدخت ۴ - با بای مجهول بر وزن کمخت، ستارهٔ زهره را گویند که صاحب فلک ...\n\nMo'in's footnote 4 (bottom of p. 333), verbatim as read from the scan:\n«۴ - = بغدخت؛ بقول شفتلوویتز اصل آن «بغدخت» است یعنی دختر بغ (خدا). و آن به ستارهٔ\nزهره اطلاق شده «ستارهٔ ناهید بقلم نگارنده. مقدمه» بعضی اساس «بدوح» Budûh اسلامی را\nهمین نام آرامی ایرانی ستارهٔ زهره ـ یعنی بیدخت ـ میدانند «دائرةالمعارف اسلام: بدوح»،\nرک: مزدیسنا ۳۳۰ و ۳۲۹.»\n\nNeighbouring footnotes on the same page (for orientation):\n۳ - پهلوی apēdāt «معنای ۲۶۷».\n۷ - Salix aegyptiaca «نباتی ۱۶۹».\n۵ - بیدرفش - پهلوی Vēdarafsh، پاتکار زریران، پهلوان لشکر ارجاسب، رک: فهرست مزدیسنا.\nبیختن - بفتح چهارم، در پهلوی vēxtan «تاوادیا ۱۶۶ : ۲»، از ریشهٔ اوستایی vaēg\n(تاب دادن، جنباندن) «بارتولمه ۱۳۱۳» «نیبرگ ۲۳۹».\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt553.jpg ocr/BQT/333.png 2>/dev/null; ls -la ocr/BQT/ | head"
}
```


### [2026-09-05T20:12:09.389Z] TOOL RESULT

```
total 8840
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 16:12 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 368375 Sep  4 13:39 0001.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1684 Sep  4 13:39 0001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 534367 Sep  4 13:39 0049.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2677 Sep  4 13:39 0049.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1076 Sep  4 15:27 103.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 446843 Sep  4 13:39 1225.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4412 Sep  4 13:39 1225.txt
```


## [2026-09-05T20:12:12.746Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(280,295):\n    if 'دختر' in t[i]:\n        print('=== leaf',i,'printed~',i+540)\n        print(t[i][:1800])\n        break\nEOF"
}
```


### [2026-09-05T20:12:14.966Z] TOOL RESULT

```
=== leaf 286 printed~ 826
                                            ‫بیان جهارم‬



                      ‫* دځ بدفتح‌اول وسکون ثانی‪ .‬بمعنی | کشهراب انگوری باشد ‪.‬‬
‫انیت‬    ‫ع‬    ‫و‬     ‫ام ق‬           ‫دحتر‬              ‫خوب ولیکوباشد ‪ -‬وفوج صف را بیزکوبند ۔‬
 ‫وسره وخلاصة هرچیزهم‌هست ‪ -‬وضم اول بمعنی | که‌کنایه از شراب لمل باشد ‪ - ۵9‬و بمعنی‬
 ‫انگور ودانه انگورهم آمفه است که بعربی علب‬         ‫گاهی را‬        ‫دختر باشد ‪۴‬‬        ‫است که مخقف‬         ‫دخت‬

                             ‫| خواشد ‪.‬‬       ‫ر‬  ‫یآن‬  ‫صاز‬   ‫حد و‬ ‫نیز گویند که درمیان اب روی‬
 ‫د ختر رور گار ‪ -‬کنابه از حوارت‬        ‫ه‬ ‫ز‬ ‫ب‬ ‫ر‬ ‫خ‬ ‫ن‬ ‫ا‬ ‫د‬ ‫ب‬ ‫و‬ ‫د‬ ‫ن‬ ‫ی‬ ‫بافند آونرا درخراسان اوخ کو‬
                                 ‫کزار است ‪.‬‬
                                          ‫| رو‬        ‫آرنگه کنند؟ ‪-‬وبه‌منی لیبو باهم! مده‌است ‪/‬‬
‫بارت‬    ‫بتکده ‪.‬‬    ‫» بر وزن‬
                                     ‫‪۱‬‬
                               ‫دختره ‏‬
                                                     ‫وتهیررآسمانی س زراا نسزر کدوونند که تءنرششپیاابین ‪,‬باشد ‪.‬‬
                                                             ‫کر‬          ‫‪۱‬‬                   ‫ج‬
                                                    ‫= هم اول وسکون ثالی ونای‬                 ‫د حت‬
‫ودخت رکی ودوشیز گی باشلب ومهر برا نیزکوبند‬
                         ‫که بر که لهند ‪. ۷‬‬                             ‫قرشت » مخقف دختر است ‪#*.‬‬

 ‫ینری ‪٬‬بمعنی‏‬ ‫دختری ^ گبر‬
            ‫لوز‬                                    ‫از شراب لملی‬           ‫ااببه‬
                                                                              ‫کنفت‬
                                                                                 ‫‪-‬تر‬
```


## [2026-09-05T20:12:18.916Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==287' BQT_v2_pages.txt | tail -18"
}
```


### [2026-09-05T20:12:20.396Z] TOOL RESULT

```
                              ‫مصحف «رخ» ‏ روخ ‪.‬‬       ‫‪۴‬‬            ‫رك‪ :‬دخت ؛دختر ‪.‬‬             ‫‪۴‬‬
                                          ‫‪ - ۴‬بپلوی ‪txud‬‏ نیم رگ ‪ ۰۶‬ورك‪ :‬دختر ‪.‬‬
        ‫که دم وحمت ماکرد ز بند آزادت ‪.‬‬              ‫® ‪ -‬برسان بندگی دختر رز کو بدرآی‬
  ‫«حافط شبرازی ‪۵۱٩‬‏ ‪.‬‬
  ‫‪ - ۷‬امروز دختره ( از‪:‬‬                  ‫‪- ۱‬از‪ :‬دختر ‪( ۲-۰‬یسوند دبت)» رکك‪ :‬دختری ‪.‬‬
                        ‫دختر ‪ ۳-۰‬پود تصفیر و تعریف) را بمعنی دختر کے معین استعمال کنند ‪.‬‬
                                                  ‫‪- ۸‬از‪ :‬دختر ‪ +‬ی (یوند مصدری) ‪.‬‬
                                ‫‪ ۵‬دچار ‪ -‬رك‪ :‬یابان کتاب ‪.‬لفات متفرقه‪ .‬ور کک‪ :‬دوچار‪.‬‬
  ‫‪ ۵‬وختر ‪ -‬منم !ول وفتح سوم (مخفف آن دخت)‪.‬اوستا ‪( ۲208110.‬دختر)؛پهلری‬
  ‫‪.. 6‬هندى بامتان ‪ .41114‬ارمنی‪ ,۲452‬کردی ‪, 6010 , 6601‬وخی ‪.082010‬سنگلیجی‬
   ‫‪ 0‬منجی ‪ « 20801‬اسشق» هوبشمان ‪ ۱4۵۰‬نز در یهلوی ‪« 7201۱0‬منای ‪۷۲:۲‬‬
  ‫کیلکی ‪ ( 762001‬در حوالی لاهیجان ‪ .) 62124‬فریزندی ‪ 8101‬برنی ‪ .640‬نطنزی ‪106‬‬
  ‫که‪.‬‬             ‫د کہ اص ‪ ۹۸۲۰‬سمانی الا سنکری‌اهانل لاسگردی‪ .101‬شهمیر زادی ‪۲‬‬
  ‫‪۲‬ص ‪. ۷۸۱‬طبری ‪« ۲216‬نسصاب‌طبری ‪. ۰8۳‬خواناری ‪ €‬سالنامة فرهنكکلپایگان ‪۷٤».‬‏‬
  ‫ادنیشکارهان اڭ وکره‪ :‬دخت ؛ فرزند مادبنة انان »ینت ابنه ‪ -‬زن‬
                                                            ‫دزفولی ‪» 78060‬مکر‬
                                                                          ‫می‌دئدیده »دوشیزه» باکره ‪.‬‬
```


## [2026-09-05T20:12:29.379Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(348,364):\n    p=t[i]\n    if 'دوشیدن' in p or 'دوشیزه' in p or 'دوغ' in p:\n        print('=== leaf',i,'printed~',i+540)\n        print(p[-1600:])\nEOF"
}
```


### [2026-09-05T20:12:30.987Z] TOOL RESULT

```
=== leaf 351 printed~ 891
باش » پس بباشد ‪) .‬‬
                                  ‫لو = لخت ( عور ) رك ‪:‬‬                     ‫_ ممحف ‪ :‬روخ =‬
                                   ‫‪ :‬دوخ چکاد و روخ و روخ‬                ‫لفت‌نامةٌ دهشدا ‪ :‬لخت و لوخ ورك‬

                                                                            ‫رك‪ :‬دوختن ‪.‬‬           ‫‪۷‬‬                  ‫جکاد‪.‬‬

                                  ‫‪#‬دو چرخه ‪ -‬صم اول وفتح‌سوم و کس ينجم (درلهجة‬
                                   ‫چورخ ‪٣‬ه‏ (نبت وانصاف) » ترجمهٌ درست‬
                                                                     ‫مکرزی) » از‪ :‬د‬
                               ‫‪ ,‬که‬     ‫لاك‬            ‫وسله نقله د'رایدوچرخ‬              ‫‪elcycib‬؛‏‬          ‫ازفرانوی‬


                                                       ‫بوسلهٌ دورکاب براثرفشار یاها بحر کت درآ مند ‪.‬‬
                                                                                           ‫‪۰٩۸‬‏‬            ‫حه‬
                                                                                                            ‫صبهفاز‬
                                                                                                                 ‫بق‬
  ‫«ایشان (خوارزمیان) جوزاء را درجملةٌ بروج بجای « نوأمان» محسوب دارند واين جوزاء صورت‬
  ‫(ذوجر كرك ‪ .‬ن ل) کونند‬  ‫جبار است و اهل خوارزم اين برح (جوزا) را« اذويچگريك » ا‬
                          ‫‪ ۱‬ومعنای آن د زوالصذمین» ‪ ,‬و این معنی مقتضای با «توامان» است ‪>.‬‬
                                                              ‫‪.‬‬   ‫‪ :‬دویرادران‬    ‫رك‬   ‫برار ‪-‬‬      ‫دو‬

=== leaf 352 printed~ 892

             ‫‪ - ۱‬در اراك (سلطان آباد) ‪٤×٥‬‬                        ‫‪۶‬وختن» ‪.‬‬
                                                                        ‫مفعول از د‬       ‫_م‬
                                                                                          ‫اس‬‫©‬
  ‫‪ - ۷‬مصحف ‪ ۶‬روح چکاد» [رك‪ :‬روخ » درخ‌چکاد ]دراغت فری (ص‪ )۹۰۱‬آمده ‪:‬‬                                  ‫ژاد» ‪.‬‬
                                                         ‫« روخ چکاد » املع باشد » حكاك (مرغزی) كەت ‪:‬‬
                 ‫این سفر ین سناه روخ چکاد ‪¢.‬‬                          ‫ایتاده بخدم بر در او‬
  ‫درضخة چاپ هرن‪« :‬روخ چکاد ‪.‬کامتی است فولوی ‪ .‬روخ روده باشد «چکادبالای پیشالی‬
 ‫و پهلوی‌روخ چکاد اصلم ود » در نسخه نخجوانی‪ « :‬دوخ چکاد‪ .‬مرد اصلم باشد بپپلوی » رك ‪:‬‬
 ‫‪ - ۵‬نی هرد بیموی پیش سر‬               ‫لضت فری اسدی ‪ . ۹۰۱‬برای جزو دوم رك‪ :‬چکاد ‪.‬‬
 ‫)‬      ‫لب؟ق(رة‬
              ‫اور‬
                ‫از م‬              ‫لفة به‌عنی دو نخ رنگین » اشاره بای ‪۳۸۱‬‬    ‫‪٩‬‏‬           ‫«منتهی الارب؟ ‪.‬‬
      ‫مانلفجر‪.‬‬
             ‫در مورد محر ماه ره‌ضان ک‪:‬لوا واشربوا حتی بتبین لکم‌الخیط ایض من الخيط الاسود ‌‬
                                ‫( مخورید ویاشامید تا رش مید از رشتة ساه فجر شمارا آشکار گردد ) ‪.‬‬
  ‫کردی‬       ‫(دخان)‬             ‫‪:۲٩‬‏ قس ‪ :‬هادی تامتان ‪8 -‬‬         ‫‪, - ۰‬هلوی ‪tûd‬‏ *منای ‪۲۷۲‬‬

  ‫‪ .‬وخی ‪ . 6120‬شغنی ‪ . 4۱‬سرءکلی انا «اسشق‬                             ‫‪ . 0‬اففانی ‪ ۰ ۵۱‬بلوچی ‪1444‬و‪4‬‬
                                                                                       ‫ورك‪ :‬دوده ‪.‬‬      ‫‪۹‬‬

=== leaf 354 printed~ 894
      ‫ك‬    ‫‪۳‬‬

  ‫‪2‬‬    ‫آهتگد»‪‎‬‬   ‫دود‬       ‫مخفف‬        ‫‪o‬‬           ‫مخفف « دود آهنج» ‪۴‬‬             ‫‪۴‬‬        ‫‪۰‬‬     ‫‪6‬‬          ‫ی استق وهویشمان‬

      ‫‪ - ۱‬بهلوی ‪۲0d‬‏ (بعید) «اسشق ‪« ۸۵‬منای ‪ > ۲ : ۲۷۲‬از ابرانی باستان ‪2۳84 -‬‬
  ‫« بارتولمه ‪ »۰۵۷‬دیبرکه ‪ » ۶‬پارسی باستان و اوستا‪ .3۲00-‬هندی باستان _ ‪arûd‬‏ ‪ .‬کردی‬
  ‫‪۲‬ففانی ‪ 1۳11۰‬بلوجی ‪ ۲04‬و ‪ ۲11۰‬وخی ‪ . ۲1‬بودغا ‪« 0701‬اسدق ابا »‪ .‬کیلکی ‪. ۲110‬‬
                                                                            ‫ا‬
      ‫‪ .‬سنگری‬         ‫* سمنانی ‪rid‬‏ و ‪۲1‬‬                ‫ص‪۳۹‬‬
                                                          ‫» نطنز ی ‪rûd‬‏ ‪ °‬ك ‪۲ ۱ .‬‬                     ‫فریزندی و برلی ‪۲0‬‬
                                ‫› ‪.‬‬    ‫« ك‪ .‬ص‪۳۰۱‬‬              ‫وشهمیرزادی ‪ . ۳1‬سرخه‌بی ‪ . ۲114‬لاسگردی ‪۲‬‬
                       ‫‪( - ۷‬مر) بسن گردیدن* منتهی الارب * کردکتن « غیات اللغات» ‪.‬‬
      ‫بدست رسانیدن پیاله های شراب در مهمانی « نام الاطا > مأخوذاز(عر)‪.‬‬                                 ‫‪ - ۸‬از دست‬

  ‫"‪« .‬دو؟ بمعنی دوغ‬                            ‫رك‪ :‬دودان سرون ‪.‬‬         ‫‪۶‬‬             ‫مأخوذ از (عر)‪. ‎‬‬                    ‫‪٩‬‬
      ‫که درنسخ‌مروج‬        ‫ات‬   ‫دور اسروب» ‪bêrsarûD‬‏‬              ‫ابن نامم صحف(‬       ‫ظ›‬         ‫‪۳۱‬‬                  ‫(ه‪.‬م ) آهده‪۰ ‎‬‬
      ‫النهب « دورشرین؟ و«دوسر؟ ودرتاریخ طبری «خوراسرو؟آمده واو سر منوش چیپر (منوچهپریادشاه‪‎‬‬
      ‫بشدادی) وجد سیزدهمین زرتشت است طبق‌سنت (رك‪ :‬مزدینا جدول برایر ص ‪ )۸1‬نه دشمن‌او‪.‬‬
          ‫( برهان فاطع ‪) ۷۱۱‬‬

=== leaf 358 printed~ 898
 1564‬اسشق ایضا» ‪.‬‬
                 ‫از ‪ :‬دوش ‪( ۳۱‬لیاقت بمعنی دوشیدتی » نظیر خوانا بمعنی خواندنی) ‪.‬‬                                      ‫‪۵‬‬
         ‫‪ - ۶‬رك‪ :‬دوشند ‪ ,‬دراراك (‪-‬لطان آناد) ‪8915۱-۷28‬‬                                     ‫‪.‬‬    ‫دوشه‬   ‫رك‪:‬‬           ‫‪۹‬‬


                                                                            ‫«مکی نژاد › ‪.‬‬              ‫یردن)‬
                                                                                                           ‫وفششی‬
                                                                                                               ‫دظر‬
                                                                                                                 ‫(‬
                                                                                                        ‫‪۷٩۸‬‏‬        ‫حزهٌ‬
                                                                                                                       ‫فا‬‫صبه‬
                                                                                                                           ‫بق‬
                                                                       ‫‪.‬‬     ‫د کل کلاب ‪۵‬‬                 ‫مرو‬             ‫و سردسر‬

 ‫‪۳‬‬       ‫‪» ۷۲‬‬   ‫«مناس‪۲‬‬   ‫‪60‬‬    ‫‪ ۲‬بهلوی‬   ‫(مصدری)‬        ‫دی‬      ‫بت سم اول ‪ 4‬ار ‪ ۳‬دوست‬                  ‫ستی‬   ‫دو‬      ‫‪#‬‬


                                                     ‫عدق‬    ‫ت‬   ‫خبرخواهی‬       ‫‪-‬‬   ‫مودت‬         ‫‪ 6‬باری ‪.‬‬       ‫› رفاقت‬       ‫معت‬

=== leaf 359 printed~ 899
و سکون‬

  ‫‪ ۱‬از ‪ :‬دوش ( دوشیدن ؟) ‪ +‬ایزه ( ایو ‪ .‬يولد صفیر ) ؛ لغة دختر دوشنده‬
  ‫از‪ :‬دوغ ‪ +‬با‬            ‫‪۴‬‬            ‫‪ - ۴‬بقتح عن ولام (اقرب‌الموارد) ‪.‬‬                     ‫(کاو و گوسیند) ()‬
       ‫‪ ۵ - ۴‬مخفی لماند که درلفظ‬                  ‫(آشی) («‪.‬م‪ ).‬معرب آن (دوغباج ) « دزیج ‪۱‬ص ‪۰ ۷4۹‬‬
   ‫دوقص ازصاحب برهان سهوی عظیم واقع شده ‪ .‬وآن اینکه فاراکه حرف سوم است‪ .‬قاف خواند‬
   ‫و حرف اول وسوم راکه مفتوح باید‪ .‬مضموم نوشت چه کولیی وصاحب قاموس تصریح نموده‌اند‬
   ‫که دوفص بدین معنی بفتح اول وسکون الی وفتح فاست‪« ».‬چك ص‪ 44۳‬ح» لکلرك ایز دوفص‬
                          ‫رك ‪ :‬دوقوی ‪.‬‬          ‫‪9‬‬           ‫‪( 80081‬فر) «(ك؟ ص ‪. ۰ ۸۳۱‬‬                          ‫آورده =‬
       ‫‪- ۷‬طبری ‪ 60‬صاب طبری ‪. ۳۸۳۰‬‬                           ‫‪ - ۱‬بونانی ‪« 50040‬اشتینگای» ‪.‬‬
  ‫‪ #‬دوشیدی ‪ -‬م اول وفتح ينم ‪[ ,‬رك‪ :‬دوختن ]؛ خارج کردن شیر ازپستان‪ -‬گرفتن‪.‬‬
                                                                      ‫رك ‪ :‬دوقص (!)‬      ‫_‬        ‫٭‪ #‬دوفص‬

   ‫‪.‬ریزندی و طنزی له «برنی‬
                         ‫‪۰‬یلکی ‪٩81‬‏ ف‬
                                    ‫[ك‪ :‬دوختن ] ک‬
                                                ‫* دوغ ‪ -‬جنم اول ر‬
       ‫‪۱ . 1:‬ص ‪ ۱۹۲‬سمنانی ‪. 00‬سنگری ‪ » 0‬سرخه‌بی »لاسگردی شوهمیرزادی‬                                                   ‫‪9‬‬
       ‫ول دك ‪ .‬بص ‪ ۰۹۱۰‬طبری ‪« 0‬صاب طبری ‪ ۳۹۳۰‬معرب آن (دوغ) «دزی ج اص ‪۹۷4۰‬‬
   ‫‪.‬‬     ‫ته‬
          ‫رسفکه‬
              ‫گآبس‬
                 ‫و (دو) «اضاص‪»۲ : :۸۱‬؛ شیرترش مسکه گرفته ‪.‬آب ماست» ماست مخلوط با‬
```


## [2026-09-05T20:12:42.738Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(345,356):\n    p=t[i]\n    if 'دوختن' in p:\n        print('=== leaf',i,'printed~',i+540)\n        import re\n        for ln in p.split('\\n'):\n            if 'دوختن' in ln or 'دوش' in ln: print('   ',ln.strip()[:300])\nEOF"
}
```


### [2026-09-05T20:12:44.308Z] TOOL RESULT

```
=== leaf 351 printed~ 891
    ‫دو حت » بروزن‌سوخت‪ .‬ماضی دوختن‬                                         ‫کس باشد بیکدیگر بی‌خس ‪.‬‬                  ‫دو‬    ‫رین‬
    ‫و دوشیدن باشد ب»عنی پاره را بهم وصل کرد‬                 ‫=نابه اکزاف ونون‌باشد که‬
    ‫وشیر را دوشید‪ - ۷‬مواضی اداکردن و کزاردن‬                                     ‫> است ‪۳ 89‬‬    ‫ازآن لفط کر‬                ‫مقصود‬
    ‫رك‪ :‬دوختن ‪.‬‬           ‫‪۷‬‬                  ‫جکاد‪.‬‬
=== leaf 352 printed~ 892
    ‫= دو ستارء شعرآی شاه‌ی‬           ‫خواهر‬          ‫دو‬           ‫لت که دوختن جامه باشد بوزن ‪٩‬‏ و دوختن‬
    ‫میگوبند » و بعربی اختامهیل خوانند و عبور‬                     ‫وبمعنی اندوختن ومال جمع کردن هم هست‪- ۴‬‬
    ‫وغیه‌صاء نیز گویند‪.‬‬                  ‫و شیر دوشیدن را یزگوبند ‪ - ۴‬و بمعنی ادا‬
    ‫است ‏ ودوشیده ‪ ۱‬و‪-‬ادا کرده و گزارده رائیز‬
    ‫(محکم کردن)‪ .‬بلوچی ‪ 82661‬و‪( 1584 82‬دوختن)‪ .‬مدارزانی ‪« 606[0. 0‬اسذق ‪. ۷۷۵‬‬
    ‫‪ ۴‬ره ‪ :‬اندوختن‌وح‪. ۱‬‬    ‫(لیزدرفارسی ‪ 712200‬پهلوی ‪ 0۲6660‬ااست رك‪« :‬هوبدمان ‪۲۷۵».‬‏‬
    ‫‪.‬‬      ‫‪02‬‬          ‫) دوشیدن )‪ 2‬بهلر ی‬              ‫هندی بتاان » رسه ‪hod -‬‏ ‪ihdgéd .‬‬         ‫‪۴‬‬
    ‫باين معنی ‏ نوختن («‪.‬م‪. ).‬‬        ‫‪۴‬‬              ‫(شیر دوشیدن) «»کی‌نژاد»‬
```


## [2026-09-05T20:12:55.407Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT daughter ===\"; grep -n \"^DAUGHTER\" SKT.txt | head -3; grep -n -A3 \"^DAUGHTER\" SKT.txt | head -12"
}
```


### [2026-09-05T20:12:55.460Z] TOOL RESULT

```
=== SKT daughter ===
4734:DAUGHTER.
4734:DAUGHTER.
4735-:
4736-dau&er,  to  planter ;  answering  to  an  o\*ltt fbriD  da:L\i'*.  _  L.  deaib^rtt  lo  wh)t4.n. pluter.  «  L.  i/<r.  down,  rery;  aJhan.  lo wbiicn.  from  a/^»j,  white;  mc  Alb.  Cf. Span./a/A<4Txr  ^■=l^a*7l4:d/^r•J,  to  plaster. (Not  from  W.  d^tf6,  GacL  and  ir.  ^ plaster.)    Der.  hedauh.
4737-Daughter  (E.>  M.  E.  da^kUr^  iehter. A.  S.  tlJitor.  4"  Dii.  dockter,  Dan.  daiUr, dotUr,  SweJ.  iAtf//r.  IceU  i6V/»V,  Goth. daukiar^  G.  tackier,  Kuh.  dacJu^  Gk. «i/Y(fn}^.  Slit,  duhitH,  The  SkL  ^Mii/ri seems  to  have  meant  'milker'  of  the  cows; from  t/wA  (  =4£lv^\  to  milk.
```


## [2026-09-05T20:12:56.935Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    for w in ('دوشیدن','اندودن','زدودن','دختر'):\n        if w in p:\n            print('block',i,w)\nEOF"
}
```


### [2026-09-05T20:12:58.639Z] TOOL RESULT

```
block 35 دختر
block 37 دختر
block 56 دختر
block 249 دختر
block 265 دختر
block 315 دختر
block 457 دوشیدن
```


## [2026-09-05T20:13:03.733Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (265,457):\n    print('=== block',i)\n    print(t[i][:1200])\nEOF"
}
```


### [2026-09-05T20:13:05.483Z] TOOL RESULT

```
=== block 265
[pdf page 266]
دخت, دختر | ۲۶۷
اسلاری کهن: شیردادن.
چم این واژه در زبان آلبانی: شیرترش.
ٍ
ا
ارستایی (475374/4): دانمارکی (0۸2/1874): 3 دب ۱۱۸
01650۸ سرئدی (8178215): 2007
۱ پپلری (نماتله): ۰ 017 ,20177۸8 نروژی (/07775014/): 3 ی
ٍ کردی (80/5[7): 7 ,0177 هلندی (00762): ان ۷ درا
تخاری ۸ (۸ (4ل/7071۸): ۲۵۸ اسلاوی کهن (1شا5 674 #ناتل) 2ا0):
تخاری 8 (8 ۸4۸ل70727۸7): 7 ۰ ط8ط005117 ,018137
سانسکریت (54۸/50/7): 021 لهستانی (0/[54): ان ۱۸۵
اف 8ة 211117 روسی (/(7354): ۰ 20071881 ,200273
ارمنی ((40/80/1۸): 27 چکه (7ل28): 75 بش2۳
یونانی (072820): لیتوانی (۸۸]۵2تال7ل):
717۷0۸788۸ ,717۷02758 ۸ ش28۳5
گرتیکه (007[4/0): 0۸ لنونی (لتی) (0لفل ۰:7 01678
ایسلندی کهن 50/0/0۸14 صا0):
20۳ پسگشت‌ها . : ۸5
نورس کهن (۸0852 00): 230 7 ۸00520
ساکسونی کهن (//2400 ۰:01 00117۸ 52 (0۸16153787) مزر
فریزی کهن (۳۶4/0 صبا0):: 00073728 8( 052
آلمانی کهن ((5701۸ 470 012): 9 (0۸167771۳) :۸/۸۲25
تست 3 1106 80
آلمانی ۰.680۸0 تا 7 700878 5 (0۸68787) :0/05
انگلیسی کهن 80280 ص0): 5 (0۸611783) +57
200 برهان قاطع + ۸۶
انگلیسی (3ل5لا8۸0): ان ۷ ۱۱۳۹۹۵

=== block 457
[pdf page 458]
تج
مام مامی» ماما (به چم *مادن) / ۴۵۹
آلمانی (4(۷ان027): ۰ ۱/1765 ,۸1812689
انگلیسی کهن (80//80 ۵۲۵): 1/8۸0 پسگشت‌ها کرت
انگلیسی (باقلاه(8): 5 2225 ۶008۳
دانمارکی (0۸۸1874): 8 بای امین ان
سرئدی (81750150): 8 5 مته0)5) ,دککاکه تاج
نروژی (/(۵۷08804): ۱7016 ,3/8 269 هط
هلندی (7ظع007)+ دا 1 (۲8) :2/3
اسلاوی کهن (76هما؟ 64 ناه صا0): 69 ,385-386 ماه
1 ,۸/1۲70 6 (01۵) :00/5
لیتوانی ((414تا734/): ۸2 5 (041134) +357
ایر دی کهن (للفلقا .ا0): را 0 برهان قاطع + 1۹۳۸
آلبانی (/(4ا7لمقته): انا
یادداشت:
۱ چم این واژه در کردی: جاروب کردن,
چم واژه‌های این فهرست (به جز اوستایی و پهلوی و فارسی و کردی و بلوچی و سانسکریت): شیر» شیر دوشیدن
(شاید بدین علت که شبر دوشیدن ستلزم "مالش " با "مالیدن" است.)
۲ میان این واجربشه و واجریشه‌ی م۱187 (716-1717 :۳07۳01079) خویشی نزدیکی وجود دارد.
| تمانگلیس سروازای ارس ۱۷۸۷۸2۸۸
پهلوی (/ا2۸۶):(پازند) 3 ایسلندی کهن (9420/0۸ 0):
اد اففانی (پشتر) (//4۳0۸0): ۹ ۸
ساننکریت )1 ‎٩24۸‏ ,۷2 آلمانی کهن (0570/(0 04 0ا0):
ارمنی (۷۵/8(/4(۷ ۶ ‎٩۸۸۲‏ ,۸۸۵۲۸ 0۸۸
بونانی 028/0): ۰ ۸12۸/۸/5 ,۸180181۸ آلمانی (08//۸(0): ۰ ۱۸/۵/8 بفاق۸
لاتین (/712م): ۸۹۸۸ انگلیسی کهن راتوناه/20 ام : ۸ااحا
فرانسه (۳۳8/4): 11/۸ انگلیسی (8001870): ۱
اسپانیایی (52۸/184): ۸۸ ۸ ,۱۱/۸59 ,36تا34 ,3۸۵10۸
```


## [2026-09-05T20:13:18.841Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/daughter",
 "prompt": "Give the full etymology entry for \"daughter\": Old English form, Proto-Germanic, PIE reconstruction, and what it says about the derivation from a root meaning \"to milk\" (the \"milker\" theory) — quote exactly."
}
```


## [2026-09-05T20:13:20.805Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AF%D9%86",
 "prompt": "Give the Persian entry for اندودن (andudan): etymology, prefix analysis, Middle Persian form, Proto-Iranian root cited, and meaning. Also mention if زدودن is listed as related."
}
```


### [2026-09-05T20:13:23.907Z] TOOL RESULT

```
# Etymology of "Daughter"

Based on the provided content, here is the etymological progression:

**Old English:** "dohtor" — defined as "female child considered with reference to her parents"

**Proto-Germanic:** *dokhter, earlier *dhutēr (also appearing in Old Saxon, Old Norse, Dutch, German, and Gothic forms)

**PIE Reconstruction:** *dhugheter (the Proto-Indo-European root, also found in Sanskrit, Avestan, Armenian, Old Church Slavonic, Lithuanian, and Greek)

**Regarding the "milker" theory:**

The provided text does not mention or discuss any theory connecting the word's derivation to a root meaning "to milk." There is no reference to a "milker" etymology in this entry. The document traces the word's linguistic ancestry through Germanic and Indo-European language families but does not explore alternative semantic theories about its original meaning.
```


### [2026-09-05T20:13:26.344Z] TOOL RESULT

```
# Persian Entry for اندودن (andudan)

Based on the provided Wiktionary page, here's what is documented:

**Meaning:** The verb اندودن has three definitions: "to besmear," "to plate," and "to coat."

**Pronunciation:** [ʔænduːˈdæn] in IPA notation.

**Present Stem:** اندا (andâ)

**Etymology, Prefix Analysis, and Proto-Iranian Roots:** The page does not provide etymological information, prefix breakdowns, or Proto-Iranian root citations.

**Middle Persian Form:** No Middle Persian form is listed on this entry.

**Related Term (زدودن):** The word زدودن is not mentioned as related. The only derived terms listed are زراندود (zar-andud) and روغن‌اندود (rowġan-andud), both appearing to be compound forms using andudan rather than standalone related words.

The Wiktionary entry provides minimal linguistic depth beyond definitions and pronunciation.
```


## [2026-09-05T20:14:43.540Z] TOOL CALL #80: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0ugh%E2%82%82t%E1%B8%97r\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%AE%D8%AA%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%BA\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4%DB%8C%D8%B2%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AF%D9%86\" \\\n \"https://www.etymonline.com/word/daughter\" \\\n \"https://en.wikipedia.org/wiki/Azarmidokht\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 131 (Dheu 3 / Dheugh): verification of dušidan, doxtar, dug, andudan, Azarmidoxt\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:14:48.476Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4a97e666d66237b5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/62b39aa42af61cda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5659416d39237d9f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8724fcc52d58cc54.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2328859689bc1c29.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/843aa331f5d79bba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfbc94cdb2d47b55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1658c7edf418ab0.txt
```


## [2026-09-05T20:14:58.230Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 131 -l 131 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg131 && ls -la pg131.png"
}
```


### [2026-09-05T20:15:00.377Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 80793 Sep  5 16:15 pg131.png
```


## [2026-09-05T20:15:02.924Z] TOOL CALL #82: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg131.png"
}
```


### [2026-09-05T20:15:03.344Z] TOOL RESULT

```

```


## [2026-09-05T20:15:03.340Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:15:21.229Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"âzarm\\|äzarm\\|azarm\\|āzarm\" HRN.txt HUB.txt PHD.txt NYB_vol2_glossary.txt | head -15"
}
```


### [2026-09-05T20:15:21.272Z] TOOL RESULT

```
PHD.txt:196:~ih: disbelief. an-āštīh [?n’styh] discord, enmity; disquiet, unrest. ānay-, v. ānīdan. an-ayād [?7’byd’t'] forgotten. an-āzarm [cim] without respect, dishonoured.
PHD.txt:224:ayabag 15 azarmigih
PHD.txt:225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
PHD.txt:753:ageless azarman. aggression hénih. aggressive mustabarmand. agile čābuk.
PHD.txt:2205:harm (n.) ak, anāgīh, azarm, bei, bēšišn, wizend, zyàn.
PHD.txt:2304:honour (n.) āzarm, āzarmīgīh, burzišn.
PHD.txt:2441:injury āzārišn, azarm, wizāyišn, wizend.
PHD.txt:3407:respect āzarm, àzarmigih, gramigih, tars, tarságáhih.
PHD.txt:3408:respected āzarmīg.
PHD.txt:4108:unaging azarmān.
PHD.txt:4139:unhonoured anāzarmīg.
HRN.txt:661:deutung *Ehre, Achtung* (GF.), anäzarm (Men.), vergl. Vis und Kämln,
NYB_vol2_glossary.txt:438:an-āžarmīk dishonoured 7514-21, comp. ~-tar-ic 15%, — V. āžarmīk. Paz. andzarm, but comp. anäzarmitar, anāžarm (SGV).
NYB_vol2_glossary.txt:882:aZarm [clm] honour, renown 723; fa. vouring, respect of persons 72%, — MPrs »zrm ‘honour’ (BBB 53); Paz. NP äzarm. From Av. (512) abi-?gar- ‘to praise, to assent to with cheers’; < *abi-jarman- (HP II, 28: *ā-); as to abt-:ā- v.s. v. ästenitan. Cf apa-žirišnik, in which api- (and secondarily apa-) has been substi- tuted for abi-, v. s. v. apa-.
NYB_vol2_glossary.txt:5696:Pgd: āzāt ’P)z’dyy: āzātēh »zrg: azar »zrm: azarm
```


## [2026-09-05T20:15:34.782Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دوشیزگان\\|دوشیزه\\|شیرور\" FSF.txt FRS.txt MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T20:15:34.840Z] TOOL RESULT

```
MON_part2.txt:1368:دوشیزه به شوهر دهند و دوشیزه نباشد. 
MON_part2.txt:14235:(کد.) دختر دوشیزه. قلعهٌ کهر با گون: (کن.) 
MON_part2.txt:78941:دقیق. مضمون باریک (شعر). نکنةٌ دوشیزه: 
MON_part2.txt:80670:این آب را دختران دوشیزه از زیر آسیاب‌ها 
MON_part1.txt:28060:نادوشیزه» بکارت شده. جزو؛ مق. کل» 
MON_part1.txt:30365:اولین مقاربت دوشیزگان پاره می‌شود و 
MON_part1.txt:30366:گاهی در نزد بعضی از دوشیزگان دارای 
MON_part1.txt:30372:دوشیزگان اصو لا این برده موجود نیست. 
MON_part1.txt:40084:دوشیزه. حلوایی که از قند و نشاسته و تخم 
MON_part1.txt:46419:ببوه؛ مقّ. دوشیزه» عدراء» با کر ه؛ ج. سات.
```


## [2026-09-05T20:15:42.958Z] TOOL CALL #85: WebSearch

```json
{
 "query": "\"بز و میش\" \"شیرور\" شاهنامه فردوسی \"دوشیزگان\" یا \"دوشندگان\""
}
```


### [2026-09-05T20:15:51.788Z] TOOL RESULT

```
Web search results for query: ""بز و میش" "شیرور" شاهنامه فردوسی "دوشیزگان" یا "دوشندگان""

Links: [{"title":"گنج تاریخ ما» فردوسی » یکی مرد بود اندر آن روزگار","url":"https://tarikhema.org/ganj/ferdousi/shahname/jamshid/2"},{"title":"سقوط مرداسِ نیک‌نهاد به دست ضحاک - ایبنا","url":"https://www.ibna.ir/news/518819/%D8%B3%D9%82%D9%88%D8%B7-%D9%85%D8%B1%D8%AF%D8%A7%D8%B3-%D9%86%DB%8C%DA%A9-%D9%86%D9%87%D8%A7%D8%AF-%D8%A8%D9%87-%D8%AF%D8%B3%D8%AA-%D8%B6%D8%AD%D8%A7%DA%A9"},{"title":"نهفته های داستان ضحاک ماردوش - 2","url":"https://farhangi-sanati.blogspot.com/2022/06/2.html"},{"title":"بخش ۲- داستان ضحاک با پدرش - مستانه","url":"https://mastaneh.ir/ferdosi/jamshid/jamshid-2/"},{"title":"گنجور » فردوسی » شاهنامه » جمشید » بخش ۲ - مرداس تازی و فرزند ناخلفش ضحاک","url":"https://ganjoor.vercel.app/ferdousi/shahname/jamshid/sh2"},{"title":"شاهنامه خوانی قسمت هفتم وهشتم - ویرگول","url":"https://virgool.io/@msadeghmokhtarii/%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%D8%AE%D9%88%D8%A7%D9%86%DB%8C-%D9%82%D8%B3%D9%85%D8%AA-%D9%87%D9%81%D8%AA%D9%85-%D9%88%D9%87%D8%B4%D8%AA%D9%85-sqav7kkm5mik"},{"title":"فردوسی:\"یکی مرد بود اندر آن روزگار ز دشت سواران نیزه گذار\"","url":"https://www.nabavi.co/blog/42974"},{"title":"شاهنامه فردوسی - جمشید | PDF کافه کتاب","url":"https://ketab.cafe/%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C-%D8%AC%D9%85%D8%B4%DB%8C%D8%AF/"},{"title":"نمونه اشعار فردوسی _ شاهنامه - شعرگان : وبلاگ رسمی قاسم کریمی","url":"https://ghasemkarimi.ir/2024/10/13/24023/"}]

یافته‌های جستجو نشان می‌دهد که این بخش از شاهنامه فردوسی در داستان مرداس و پسرش ضحاک آمده است.

در شاهنامه فردوسی آمده است: "بز و شیرور میش بود همچنین" که این بیت بخشی از توصیف داستان مرداس پادشاه عادل است.

در مورد واژگان "دوشیزگان" و "دوشندگان"، پژوهشگران متعددی به این موضوع اشاره کرده‌اند: کلمه دوشندگان بجای دوشیزگان بکار رفته که به نظر با توجه به کلمه شیرور به معنی شیر ده درست‌تر می‌باشد. 

دوشیزه بچم دوشنده نیز است؛ دوشیزه هم بز و میش و هم دوشنده را گویند و هم کسی که آن‌را می‌دوشد، بنابراین هر دو واژه از نظر لغوی به هم مرتبط‌اند.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:15:59.274Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://ganjoor.net/ferdousi/shahname/jamshid/sh2\" --note \"pdf page 131: Ferdowsi verse quoted in the dushizeh node (Mardas/Zahhak episode), dushizegan/dushandegan variant\" 2>&1 | tail -2; grep -o \"بز و میش[^<]*\" data/verification/sources/web/*.txt 2>/dev/null | head -5"
}
```


### [2026-09-05T20:16:02.410Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e1d458e599b962ff.txt
data/verification/sources/web/e1d458e599b962ff.txt:بز و میش بد شیرور همچنین
data/verification/sources/web/e1d458e599b962ff.txt:بز و میش
data/verification/sources/web/e1d458e599b962ff.txt:بز و میش بد شیرور همچنین
data/verification/sources/web/e1d458e599b962ff.txt:بز و میش و هم دوشنده را گویند و هم  کسی که انرا می دوشد و دوشیز نیز همینگونه است
data/verification/sources/web/e1d458e599b962ff.txt:بز و میش بد شیرور همچنین
```


## [2026-09-05T20:17:05.699Z] TOOL CALL #87: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T20:17:05.779Z] TOOL RESULT

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


## [2026-09-05T20:17:10.319Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"blank, glänzen\\|blank, glanzen\\|dhavala\\|glänzend weiß\" WLD_Bd1_1930_dli_70244_djvu.txt | head -5"
}
```


### [2026-09-05T20:17:10.372Z] TOOL RESULT

```
29625:lit. svicbis ,, blank, glanzend“ ist eine zw. Form iiber germ .hwJtta- s. o. 
52637:3. dheu- blank, glanzen".
```


## [2026-09-05T20:17:14.467Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '52637,52650p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"--- page:\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if '3. dheu- blank' in p or 'dheu- blank, glanzen' in p:\n        print('block',i,'|',p[:160].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:17:16.667Z] TOOL RESULT

```
3. dheu- blank, glanzen". 

Ai. dhavald- „glanzend weifi", dhdvati „maeht blank, reinigt, spult" fnur 
zufallige Bedeutungsannaherung an dhdvati „rinnt“, Wz. *dheu- „laufen, 
rinnen"), av. fradavata „rieb sich (reinigend) ab“ ; gr. doog ... Xa/.mQog, 
■dowcat ' . . . /.a/iTiyuvai Hes., odovreg Xevy.a deovreg Hsd., daXeiov • y.ada- 
qov. xai dioXeov Hes. (Kontr. aus *dofaXeog). — Schulze KZ. 29, 260 f., 
Solmsen Unters. 85, Bechtel Lex. 167. Des letzteren Anreihung auch von 
deog „Gott“ ist unsicher, s. *dhes- „religios“. 

dheu-, dhena- x (vermutlich *dheue-, vgl. die Erw. *dheue-h-, *dheue-s-) 
„stieben, wirbeln, bes. von Staub, Rauch, Dampf; wehen, blasen, Hauch, 
Atem; daher dampfen, ausdiinsten, riechen, stinken; stiirmen, in hef- 
tiger, wallender Bewegung sein, auch seelisch; in heftige, wirbelnde 
--- page:
```


## [2026-09-05T20:17:19.939Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'blank, glanzen' in p:\n        print('block',i,'|', p[:150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:17:21.849Z] TOOL RESULT

```
block 478 | 470                                                                        kueit           kueq-          formantisckem                               
block 843 |                                   :                                            dheu       dheu-, dheua x -                               835  2.  dheu
```


## [2026-09-05T20:26:06.643Z] TOOL CALL #91: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk131.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_DHUG = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0ugh%E2%82%82t%E1%B8%97r\"\nW_DUSH = \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4%DB%8C%D8%AF%D9%86\"\nW_DOXT = \"https://en.wiktionary.org/wiki/%D8%AF%D8%AE%D8%AA%D8%B1\"\nW_DUGH = \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%BA\"\nW_DUSHIZE = \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4%DB%8C%D8%B2%D9%87\"\nW_ANDUD = \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AF%D9%86\"\nE_DAUGH = \"https://www.etymonline.com/word/daughter\"\nWK_AZARM = \"https://en.wikipedia.org/wiki/Azarmidokht\"\nGANJ = \"https://ganjoor.net/ferdousi/shahname/jamshid/sh2\"\n\ndoc = {\n \"pdf_page\": 131,\n \"book_page\": 101,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Dheu 3\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE 3. *dʰeu- 'blank, glänzen' (to be bright/clean, to polish); Proto-Iranian *dauH¹ 'to smear, rub on; to wipe clean' (Cheung 2007)\",\n   \"note\": \"Pokorny IEW p.261 really does carry, between '2. dheu-, dhu-ei- \\\"hinschwinden, bewußtlos werden, sterben\\\"' and '4. dheu-, dheuə- \\\"stieben, wirbeln...\\\"', a short third entry 'dheu- \\\"blank, glänzen\\\"' whose whole material is: 'Ai. dhavalá- \\\"glänzend weiß\\\", dhāvati \\\"macht blank, reinigt, spült\\\"; av. fradavata \\\"rieb sich (reinigend) ab\\\"; gr. θοός· λαμπρός ... WP. I 835.' So Nourai's root box — number, language label, page and the gloss 'to shine' — is a fair rendering of Pokorny's 'blank, glänzen'. Two caveats worth carrying to the nodes: (a) the Iranian branch never means 'shine', it means 'smear / wipe / polish', and Cheung 2007 (s.v. *dauH¹) leaves the PIE column empty ('*PIE — — LIV: 149 f. | Pok.: 261'), i.e. he regards the Iranian root as having no secure IE etymology and possibly being a Reimbildung to *sauH¹; (b) Nourai's chart has no Avestan verb attested outside the compound fra-dauu-.\",\n   \"note_fa\": \"ریشهٔ نمودار همان مدخل کوتاه سوم صفحهٔ ۲۶۱ فرهنگ پوکورنی است: «dheu- بلَند/درخشیدن (blank, glänzen)» که همهٔ شواهدش این است: سنسکریت dhavalá- «سپیدِ درخشان» و dhāvati «برّاق می‌کند، می‌شوید، می‌زداید»، اوستایی fraδauuata «(برای پاکیزگی) خود را سترد»، و یونانی θοός «درخشان». پس شمارهٔ ریشه، برچسب «هندواروپایی»، شمارهٔ صفحه و برگردانِ «درخشیدن» همه درست است و ادعای نورایی در این حد پذیرفتنی است. تنها باید توجه داشت که شاخهٔ ایرانی این ریشه هرگز معنای «درخشیدن» ندارد و همیشه «اندودن، مالیدن، زدودن، صیقل دادن» است؛ چونگ نیز در فرهنگ فعل ایرانی، ذیل *dauH¹ «اندودن، مالیدن»، ستونِ هندواروپایی را خالی گذاشته و آن را واژه‌ای بدون ریشه‌شناسی مطمئنِ هندواروپایی می‌داند.\",\n   \"sources\": [W_ANDUD],\n   \"ref_check\": [\n    {\"ref\": \"POK:261\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt (grep 'dbeu-  , blank,  glänzen'), IEW p.261 — the page number is printed in the OCR two lines above: '3'/'261'. Entry text: 'dheu- ,blank, glänzen'. Ai. dhavalá- ,glänzend weiß', dhāvatī ,macht blank, reinigt, spült', av. fradavata ,rieb sich (reinigend) ab'; gr. θοός·...λαμπρός ... WP. I 835, Schulze KZ. 29, 260 f.' Exactly the root box as drawn.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 835 (WLD_Bd1 djvu line 52637; page block 843)\", \"stance\": \"supports\",\n     \"note\": \"'3. dheu- ,blank, glänzen\\\". Ai. dhavalá- „glänzend weiß\\\", dhāvati „macht blank, reinigt, spült\\\" (nur zufällige Bedeutungsannäherung an dhāvati „rinnt\\\", Wz. *dheu- „laufen, rinnen\\\"), av. fradavata „rieb sich (reinigend) ab\\\"' — the source Pokorny 261 abridges; note WP's explicit warning that the resemblance to dhāvati 'runs' is accidental.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. dheu- (2) (IEC.txt line 2873)\", \"stance\": \"supports\",\n     \"note\": \"'dheu- (2) \\\"bright; shine, daytime\\\". Skt. cf. dhavalaḥ \\\"glistening\\\"; Gk. cf. theion \\\"sulphur\\\", theo (2) \\\"shine\\\".' Mann keeps the same third *dheu- with the same gloss Nourai gives.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, d-list (AHD_watkins1985.txt line 382)\", \"stance\": \"silent\",\n     \"note\": \"Watkins has dheu-¹ 'dust, vapour, smoke' [Pok. 4. dheu- 261], dheu-² 'to flow' [Pok. 1. dheu- 259] and dheu-³ 'to become exhausted, die' [Pok. 2. dheu- 260] — no 'shine' root at all, because no English word reaches Pokorny's third dheu-. Silence, not disagreement.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *dauH¹ (CHEUNG.txt lines 5480-5535)\", \"stance\": \"partial\",\n     \"note\": \"'*dauH¹ \\\"to smear, rub (on)\\\" ... *PIE — — LIV: 149 f. | Pok.: 261' — Cheung files exactly the Iranian family of this chart under the root, and points the reader to Pokorny 261, but leaves the PIE reconstruction blank: 'IE cognates cannot be cited in support of Ir. *dauH¹. It is more likely a \\\"Reimbildung\\\", cf. *sauH¹.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"dav 2, dŭ; han-du, ham-dŭ; uz-dâvayati, uz-dŭ\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Old Iranian verb is real and is exactly the ancestor of node 2, but the box overstates the attestation. What is actually attested in Avestan is only the compound fra-dauu- 'to be rubbed/wiped off with': Younger Avestan fraδauuata (Vd. 9.29) 'rieb sich (reinigend) ab', 3sg. fraδauuaite (Vd. 5.24) — Cheung 2007 s.v. *dauH¹ and Pokorny 261 both quote just this form. Nothing of the sort is attested in Old Persian; Nourai's 'han-du, ham-dŭ' and 'uz-dâvayati, uz-dŭ' are reconstructed pre-forms, and they are correct as such: Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p.32 derives اندودن from OIran. *ham-dau-ta- with present stem *ham-dāv-aya- (> MP handūd / handāy), and p.58 derives زدودن from OIran. *uz-dau-ta- with present stem *uz-dāv-aya-, glossing the root dav- as «پاک کردن» 'to clean'. So the preverbs ham- and uz- and the -āvaya- causative/present stem are right; only the form 'uz-dâvayati' (a Sanskrit-shaped 3sg. present) and the language label 'Avestan / Old Persian' are Nourai's own. The gloss 'to wipe, clean' for the simple root matches Abolghasemi and Cheung; 'to smear together' for ham-dū matches Cheung's Sogdian ʾnδʾw 'to smear, anoint'.\",\n     \"derivation_fa\": \"ریشهٔ ایرانی باستان dav-/dāv- «اندودن، مالیدن، پاک کردن» واقعی است و به‌درستی مادرِ گره ۲ است، اما آنچه در اوستا به‌جا مانده تنها فعلِ پیشوندیِ fra-dauu- است: fraδauuata (وندیداد ۹٫۲۹) «(برای پاکیزگی) خود را سترد» و fraδauuaite (وندیداد ۵٫۲۴)؛ چونگ ذیل *dauH¹ و پوکورنی در صفحهٔ ۲۶۱ هر دو تنها همین صورت را می‌آورند. در پارسی باستان هیچ نمونه‌ای از این فعل ثبت نشده است، پس «han-du / ham-dŭ» و «uz-dâvayati / uz-dŭ» صورت‌های بازسازی‌شده‌اند نه صورت‌های گواهی‌شده. با این حال بازسازی درست است: ابوالقاسمی در «فعل‌های فارسی دری» (ص ۳۲) «اندودن» را از ایرانی باستان *ham-dau-ta- و مادهٔ مضارع *ham-dāv-aya- می‌گیرد و (ص ۵۸) «زدودن» را از *uz-dau-ta- و *uz-dāv-aya-، و معنای ریشهٔ dav را «پاک کردن» می‌نویسد. بنابراین پیشوندهای ham- و uz- و ستاکِ -āvaya- درست‌اند و تنها ریختِ سنسکریت‌گونهٔ «uz-dâvayati» و برچسبِ «اوستایی/پارسی باستان» از خودِ نورایی است؛ پس ادعا با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_ANDUD],\n     \"ref_check\": [\n      {\"ref\": \"POK:261\", \"status\": \"supports\",\n       \"note\": \"IEW 261 s.v. 3. dheu-: 'av. fradavata ,rieb sich (reinigend) ab\\\"' — the one Avestan form the chart's root rests on.\"},\n      {\"ref\": \"BQT:172\", \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt leaf 389 (identified as printed p.172 by its catch-line 'بقیه در صفحهٔ ۱۷۳'): headword «اندودن ۱ - بر وزن فرمودن، کاهگل و گِلابه مالیدن باشد - و مطلا و ملمع کردن را نیز گویند». Mo'in's footnote 1 is cut off by the djvu OCR of this leaf, so only the headword and gloss could be read.\"},\n      {\"ref\": \"BQT:1008\", \"status\": \"partial\",\n       \"note\": \"BQT_v2_pages.txt leaf 470 (printed ≈1010, i.e. ±2 of Nourai's 1008): headword «زدودن - بکسر اول بر وزن فزودن، بمعنی ازاله کردن و بالساختن باشد» and Mo'in's footnote 4 «از: (ز دو دن) ... (پسوند مصدری). پارسی باستان *uz-dav- ... هندی باستان ریشهٔ dhāv- (مالیدن)». Mo'in thus gives exactly Nourai's *uz-dav- and Skt dhāv- 'مالیدن = to smear'; the page number is off by about two.\"},\n      {\"ref\": \"FFD:32\", \"status\": \"supports\",\n       \"note\": \"FFD_pages.txt pdf page 37 = printed p.32 (printed = pdf−5): «اندودن. اندود < فارسی میانه handūd < ایرانی باستان *ham-dau-ta-. ham پیشوند فعلی است. ریشهٔ dav به معنی «پاک کردن» است. > زدودن. اندای < فارسی میانه handāy < ایرانی باستان *ham-dāv-aya-.»\"},\n      {\"ref\": \"FFD:58\", \"status\": \"supports\",\n       \"note\": \"FFD_pages.txt pdf page 63 = printed p.58: «زدودن. زدود < ایرانی باستان *uz-dau-ta-. uz پیشوند فعلی است. ریشهٔ dav به معنی «پاک کردن» است. زدای < ایرانی باستان *uz-dāv-aya- ... > اندودن.»\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *dauH¹ (CHEUNG.txt lines 5480-5520)\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: (+ *fra-) YAv. fradauu- \\\"to be rubbed off with\\\" ... INJ. 3sg. YAv. fraδauuata (V 9.29)'; '*NWIR: ... (+ *uz-) NP zadūdan/zadāy- \\\"to polish, clean\\\" || (+ *ham-) NP andūdan/andāy- \\\"to smear, (re)cover, attach\\\"'; '*SOGDIAN: BSogd. δʾw \\\"to smear, plaster\\\" || (+ *ham-) BSogd. ʾnδʾw, MSogd. ʾnδw \\\"to smear, anoint\\\"'. The preverbs, the root and the route are exactly Nourai's.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.v. dav- / fra-dav- (BRT.txt, OCR of the columns around 741)\", \"stance\": \"partial\",\n       \"note\": \"Bartholomae's Avestan lexicon has no independent verb dav- 'to wipe'; the OCR of this stretch of the book is too damaged to quote cleanly, but the form the whole tradition cites (fraδauuata, Vd. 9.29) is the one Pokorny takes from him. No Avestan 'han-du' or 'uz-dav-' compound exists.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 (PHD.txt), s.v. andūdan/handūdan\", \"stance\": \"silent\",\n       \"note\": \"MacKenzie's Pahlavi dictionary carries handōxtan 'to collect, acquire' (< ham + tōxtan) but no *handūdan; the Middle Persian handūd/handāy of Abolghasemi is a reconstruction from the New Persian verb, not a Book-Pahlavi attestation.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 835\", \"stance\": \"supports\",\n       \"note\": \"'av. fradavata „rieb sich (reinigend) ab\\\"' — Walde-Pokorny cites the same single Avestan form under 3. dheu-.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"andŭdan «اندودن ( اندا ، اندای )»; zodŭdan «زدودن ( زدا ، زدای )»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both verbs are the regular New Persian continuants of the Old Iranian root of node 1 with two different preverbs. اندودن andūdan 'to smear (with mud-plaster), to coat, to plate' = *ham- 'together, on' + past stem *dau-ta- > MP handūd- > NP andūd-, with present stem اندا/اندای andā(y)- < *ham-dāv-aya-; the initial h- of ham- is lost in New Persian as in andām, andarz. زدودن zodūdan/zudūdan 'to wipe off, scour, polish' = *uz- 'up, out, away' + the same stems, uz- appearing in New Persian as z- (compare زدن, زفت, and the Ossetic and Pashto uz- compounds Cheung cites). The semantic split is the preverb's: 'smear ON' vs 'wipe OFF'. Cheung 2007 lists both under *dauH¹ in exactly these shapes ('(+ *uz-) NP zadūdan/zadāy- \\\"to polish, clean\\\"; (+ *ham-) NP andūdan/andāy- \\\"to smear, (re)cover, attach\\\"'), and Abolghasemi (FFD 32, 58) cross-references the two entries to each other. Borhan-e Qāṭeʿ glosses اندودن 'to plaster with kāh-gel; also to gild' and زدودن 'to remove, to make bright — the heart of grief, the mirror and the sword of tarnish, the limbs of dirt, the realm of sedition', which is precisely the 'wipe clean / polish' semantics of the root.\",\n     \"derivation_fa\": \"هر دو فعل دنبالهٔ منظمِ همان ریشهٔ ایرانیِ باستانِ گرهٔ ۱ با دو پیشوندِ متفاوت‌اند. «اندودن» از *ham- (بر، روی هم) + ستاکِ گذشتهٔ *dau-ta- است: فارسی میانه handūd > فارسی نو اندود، با ستاکِ حالِ «اندا/اندای» از *ham-dāv-aya-؛ های آغازینِ ham در فارسی نو افتاده است، چنان‌که در «اندام» و «اندرز». «زدودن» از پیشوندِ *uz- (بیرون، بر) با همان ستاک‌هاست و uz در فارسی نو به «ز» بدل شده است. پس تفاوتِ معنایی از پیشوند می‌آید: «اندودن» یعنی مالیدنِ چیزی بر روی چیزی، و «زدودن» یعنی سترودن و پاک کردن. چونگ ذیل *dauH¹ هر دو را با همین صورت‌ها آورده و ابوالقاسمی نیز در «فعل‌های فارسی دری» این دو مدخل را به یکدیگر ارجاع داده است. حاشیهٔ معین بر برهان قاطع هم زیر «زدودن» آن را از *uz-dav- و ریشهٔ سنسکریتِ dhāv- «مالیدن» می‌گیرد. ادعای نورایی در این گره کاملاً درست است.\",\n     \"sources\": [W_ANDUD],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1008\", \"status\": \"partial\",\n       \"note\": \"BQT_v2_pages.txt leaf 470 (printed ≈1010, two pages off Nourai's citation): «زدودن ... بمعنی ازاله کردن و بالساختن باشد عموماً چنانکه دل را از غم و آیینه و شمشیر و امثال آنرا از زدگی و اعضا را از چرک و ملک را از فتنه»; Mo'in's footnote derives it from پارسی باستان *uz-dav- and هندی باستان ریشهٔ dhāv- (مالیدن). It supports the derivation; اندودن is not on this page but on p.172 (see node 1).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *dauH¹, NWIR section (CHEUNG.txt line 5506)\", \"stance\": \"supports\",\n       \"note\": \"'(+ *uz-) NP zadūdan/zadāy- \\\"to polish, clean\\\" || (+ *ham-) NP andūdan/andāy- \\\"to smear, (re)cover, attach\\\", Tt. (Xia.) m-andevmun \\\"we plaster\\\"' — same two verbs, same two preverbs, same root.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie (HRN.txt), s.v. ālūdan / andūdan\", \"stance\": \"partial\",\n       \"note\": \"Horn treats the sister-verb ālūdan (Horn 1893: 10, cited by Cheung as the parallel *ā- compound of the same root) but has no separate numbered entry for andūdan/zudūdan; his evidence therefore supports the root without covering these two compounds.\"},\n      {\"src\": \"FFD\", \"where\": \"Abolghasemi pp.32 and 58\", \"stance\": \"supports\",\n       \"note\": \"p.32 «اندود < فارسی میانه handūd < ایرانی باستان *ham-dau-ta-» and p.58 «زدود < ایرانی باستان *uz-dau-ta-», each ending with a cross-reference to the other («> زدودن» / «> اندودن»).\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ ed. Mo'in, pp.172 and ~1010\", \"stance\": \"supports\",\n       \"note\": \"«اندودن ... کاهگل و گِلابه مالیدن باشد - و مطلا و ملمع کردن را نیز گویند» (p.172) and «زدودن ... ازاله کردن و بالساختن» (p.~1010).\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"dhâv\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Sanskrit dhāv- is real and is the cognate Pokorny puts under this root, but its meaning is 'to rinse, wash, cleanse, polish', not 'to smear'. Pokorny 261 quotes 'ai. dhavalá- \\\"glänzend weiß\\\", dhāvati \\\"macht blank, reinigt, spült\\\"'. Nourai's gloss 'to smear' comes from Mo'in, who renders the root مالیدن ('to rub, to smear') in his Borhan footnote on زدودن — a rendering aimed at the Persian outcome, not at the Vedic sense. Modern Indo-Aryan scholarship complicates the picture: Mayrhofer (EWAia I 782 f.) assigns Vedic dhav to 'to shake, stir', and Cheung, quoting him, says 'It is difficult to reconcile the Ir. root and Skt. dhav \\\"to shake, stir\\\" semantically'; but he adds Lubotsky's observation that Vedic has, from the same root-shape, present forms 'ā́ dhāvati (RV+), sam-dhāvyete (KS), ā-dhūyámāna- (TS) \\\"to rinse, clean, rub, polish\\\"' which 'may therefore be the genuine Skt. correspondences of Ir. *dauH¹'. So the cognation is defensible — it is exactly the form Pokorny and Lubotsky pick — but the gloss on the chart is wrong in direction, and the equation is not certain.\",\n     \"derivation_fa\": \"ستاکِ سنسکریتِ dhāv- واقعی است و همان همریشه‌ای است که پوکورنی زیر این ریشه می‌آورد، اما معنای آن «شستن، پاکیزه کردن، صیقل دادن» است نه «اندودن». پوکورنی در صفحهٔ ۲۶۱ می‌نویسد: «سنسکریت dhavalá- «سپیدِ درخشان»، dhāvati «برّاق می‌کند، می‌شوید، می‌زداید»». معنای «اندودن» که نورایی داده از حاشیهٔ معین بر «زدودن» گرفته شده که ریشهٔ سنسکریت را «مالیدن» ترجمه کرده است ــ ترجمه‌ای که به فرجامِ فارسیِ واژه نظر دارد نه به کاربردِ ودایی. پژوهشِ امروزی نیز یکدست نیست: مایرهوفر فعلِ ودایی dhav را «جنباندن، تکان دادن» می‌داند و چونگ می‌گوید سازگار کردنِ آن با ریشهٔ ایرانی از نظر معنایی دشوار است؛ اما لوبوتسکی یادآور می‌شود که صورت‌های ودایی ā́ dhāvati و ā-dhūyámāna- به معنای «شستن، ساییدن، صیقل دادن» می‌توانند همتای راستینِ *dauH¹ ایرانی باشند. پس این پیوند پذیرفتنی است ولی قطعی نیست و معنایی که در نمودار آمده نادرست است.\",\n     \"sources\": [W_ANDUD],\n     \"ref_check\": [\n      {\"ref\": \"POK:261\", \"status\": \"partial\",\n       \"note\": \"IEW 261 gives 'ai. dhavalá- \\\"glänzend weiß\\\", dhāvatī \\\"macht blank, reinigt, spült\\\"' — the form is there, but glossed 'polishes, cleans, rinses', not 'to smear'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 835\", \"stance\": \"partial\",\n       \"note\": \"'Ai. dhavalá- „glänzend weiß\\\", dhāvati „macht blank, reinigt, spült\\\" (nur zufällige Bedeutungsannäherung an dhāvati „rinnt\\\", Wz. *dheu- „laufen, rinnen\\\")' — WP explicitly warns that this dhāvati must be kept apart from the homonym 'runs'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *dauH¹, Sanskrit section and the following note\", \"stance\": \"partial\",\n       \"note\": \"'*SANSKRIT: ? dhav \\\"to shake, stir\\\" (RV+) > EWAia I: 782 f. ◊ It is difficult to reconcile the Ir. root and Skt. dhav \\\"to shake, stir\\\" ... semantically. ... A.L. points out though that in Vedic there are, from the same root, some (synchronically separate) present forms that are much closer in meaning to the Ir. ones: pres. 3sg. ā́ dhavati (RV+) ... \\\"to rinse, clean, rub, polish\\\". These forms ... may therefore be the genuine Skt. correspondences of Ir. *dauH¹.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, s.v. dheu- (2) (IEC.txt line 2873)\", \"stance\": \"supports\",\n       \"note\": \"'Skt. cf. dhavalaḥ \\\"glistening\\\"' — Mann keeps the Sanskrit adjective, not the verb, under the 'shine' root.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Dheugh, Dhugh\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *dʰewgʰ- 'to produce, be productive/useful' (Pokorny 271 'berühren, drücken, ausdrücken, melken, reichlich spendend'), specialised to 'to milk' only in Indo-Iranian\",\n   \"note\": \"Two of the root box's three claims stand and one does not. (1) POK:271 is right: Pokorny's headword is 'dheugh- \\\"berühren (sich gut treffen), drücken, ausdrücken, melken, reichlich spendend\\\"' and the entry opens 'Indo-iran. *dhaugh- \\\"melken\\\" in ai. duháti, athem. dógdhi \\\"melkt\\\" ... pers. dōγ, dōxtan usw.' — so the Iranian and Persian nodes are literally Pokorny's own examples. (2) WLD:847 is the same root in Walde-Pokorny I 847, but there the gloss is only 'taugen, tüchtig (kräftig) sein, sich gut treffen, glücken; tauglich herrichten' with no 'melken' and no Indo-Iranian at all: the milk sense is Pokorny's 1959 addition. Buck (SYN 5.87, p.386) is blunter still: 'Skt. duh-, NPers. duxtan, dušīdan, the Indo-Iranian verb for \\\"milk\\\" ... Connection with Grk. τεύχω ... Goth. daug ... is generally rejected on semantic grounds.' So 'to milk' is a legitimate Indo-Iranian gloss, but a contested one for the IE root. (3) POK:277 / WLD:868 are NOT this root: they are the separate word-family dhug(h)ǝter- 'Tochter', and Walde-Pokorny there cite the literature expressly 'gegen weitere Anknüpfung an ai. duh- \\\"melken\\\" oder idg. *dheugh- \\\"taugen\\\"'. Nourai's chart hangs 'Dhugh-tar' under 'to milk' anyway; that arrow (node 4) is where the entry breaks. The root box's own cross-note, 'Compare with the root \\\"Dhě 1: to suckle milk\\\"', is a sound warning: PIE *dʰeh₁(y)- 'to suckle' (Pokorny 241) is a genuinely different root, and Buck 5.16/5.87 keeps them apart.\",\n   \"note_fa\": \"از سه ادعای جعبهٔ ریشه دو تا درست است و یکی نه. نخست، ارجاع به پوکورنی ۲۷۱ درست است: سرواژهٔ پوکورنی «dheugh- لمس کردن، فشردن، دوشیدن، فراوان بخشنده» است و مدخل با این جمله آغاز می‌شود: «هندوایرانی *dhaugh- «دوشیدن» در سنسکریت duháti و dógdhi ... فارسی dōγ و dōxtan». پس گره‌های ایرانی و فارسیِ نمودار عیناً شواهدِ خودِ پوکورنی‌اند. دوم، در والده‑پوکورنی (جلد ۱ ص ۸۴۷) همین ریشه هست ولی معنایش تنها «به کار آمدن، توانا بودن، درست درآمدن» است و هیچ نشانی از «دوشیدن» و از شواهد هندوایرانی ندارد؛ معنای «دوشیدن» افزودهٔ چاپ ۱۹۵۹ پوکورنی است. باک نیز (فرهنگ مترادف‌ها، بند ۵٫۸۷) صریح می‌گوید پیوندِ فعلِ هندوایرانیِ «دوشیدن» با τεύχω یونانی و daug گوتی «عموماً از نظر معنایی رد شده است». سوم، ارجاع‌های POK:277 و WLD:868 به این ریشه نیستند بلکه به خانوادهٔ جداگانهٔ *dhug(h)ǝter- «دختر» تعلق دارند، و والده‑پوکورنی همان‌جا منابع را «در ردِّ پیوند دادنِ بیشترِ آن با duh- سنسکریت «دوشیدن» یا *dheugh- هندواروپایی» یاد می‌کند. نورایی با این حال «Dhugh-tar» را زیر ریشهٔ «دوشیدن» آویخته است و همین پیکان (گرهٔ ۴) نقطهٔ ضعفِ این نمودار است. یادداشتِ خودِ نورایی («با ریشهٔ Dhē ۱ «شیر مکیدن» بسنجید») هشدارِ درستی است: *dʰeh₁(y)- هندواروپایی «شیر خوردن» (پوکورنی ۲۴۱) ریشهٔ دیگری است.\",\n   \"sources\": [W_DUSH, W_DHUG],\n   \"ref_check\": [\n    {\"ref\": \"POK:271\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt line 3878, IEW p.271 (page numeral printed just above): 'dheugh- \\\"berühren (sich gut treffen), drücken, ausdrücken, melken, reichlich spendend\\\". Indo-iran. *dhaugh- ,melken' in ai. duháti, athem. dógdhi ,melkt, milcht', die Wunschkuh Kāma-duh(a) ,die reichlich Spendende' (= gr. Τύχη), pers. dōγ, dōxtan usw., apers. han-duga ,Proklamation'.'\"},\n    {\"ref\": \"POK:277\", \"status\": \"contradicts\",\n     \"note\": \"IEW p.277 is a separate headword: 'dhug(h)ǝter- \\\"Tochter\\\"; Guttural wie bei *eĝ(h)om \\\"ich\\\", s. dort. Ai. duhitár-, av. dugədar-, duγδar- ... WP. I 868, WH. I 557.' Pokorny neither glosses it 'milker' nor cross-refers it to dheugh- on p.271 — it is not a derivative of the milking root in his book.\"},\n    {\"ref\": \"WLD:847\", \"status\": \"partial\",\n     \"note\": \"WLD_Bd1 (page block 855, printed p.847): 'dheugh- \\\"taugen, tüchtig (kräftig) sein, sich gut treffen, glücken; tauglich herrichten\\\"' followed by Greek τυγχάνω/τεύχω, Irish dúan, ON duga, Goth. daug, Lith. daug. The root is there at the cited page, but with no 'melken' sense and no Indo-Iranian material at all.\"},\n    {\"ref\": \"WLD:868\", \"status\": \"contradicts\",\n     \"note\": \"WLD_Bd1 (printed p.868): 'dhug(h)ater-, dhug(h)t(e)r- ... \\\"Tochter\\\" ... Lit. bei Bartholomae Airan. Wb. 748, Boisacq 355, auch **gegen** weitere Anknüpfung an ai. duh- \\\"melken\\\" oder idg. *dheugh- \\\"taugen\\\" (letzteres bei Fick I⁴ 74).' The very page Nourai cites is the page that argues against his arrow.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"SYN\", \"where\": \"Buck 5.87 MILK (vb.), printed p.386 (SYN.txt line 9688 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'Skt. duh-, NPers. duxtan, dušīdan, the Indo-Iranian verb for \\\"milk\\\" (though not quotable fr. Av.). Connection with Grk. τεύχω \\\"make, build\\\", τυγχάνω ..., Goth. daug ... is generally rejected on semantic grounds. Walde-P. 1.847.' Buck confirms the Indo-Iranian verb and the Persian forms, but is sceptical of the IE root equation and notes there is no Avestan attestation.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, d-list (AHD_watkins1985.txt lines 382, 392)\", \"stance\": \"contradicts\",\n     \"note\": \"Watkins has two unconnected entries: 'dheugh-. To produce something of utility. ... [Pok. dheugh- 271.]' and 'dhugheter-. Daughter. Germanic *dohtēr in Old English dohtor, daughter: DAUGHTER. [Pok. dhug(h)eter 277.]' — no derivational link between them, and 'to milk' is not even given as the sense of dheugh-.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *dauč¹ and *dauxš (CHEUNG.txt lines 5358, 5538)\", \"stance\": \"partial\",\n     \"note\": \"'*dauč¹ (*dauǰ ?) \\\"to milk, traire (< **to draw ?)\\\" ... *PIE ? *dʰeugʰ- \\\"to prepare\\\" = LIV: 153 | Pok.: 271' and '*dauxš \\\"to suck, suckle, milk\\\" ... ◊ This root is a s-formation of IE *dʰeugʰ- \\\"to prepare\\\". See *dauč¹.' Cheung reaches Pokorny 271 too, but with a question mark, and notes 'Both *dauč and *dauxš are problematic: they may have either a different origin or show (mutual) influence of another root ... whence from IE *deuk- \\\"to draw\\\".'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. dheughō, dhough-, dhugh- (IEC.txt lines 2857, 3036, 3242)\", \"stance\": \"partial\",\n     \"note\": \"'dheughō \\\"make, fashion, mould, fit; be fitting, be fit, be useful\\\". Cf. dhugh-. WP I, 847. Skt. dóhāmi \\\"exploit\\\"' — Mann keeps the 'be useful' sense as primary and has no *dhug(h)ǝter- headword linking 'daughter' to it.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Iranian\",\n     \"words\": \"dhauğ, daux, dauxš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Iranian inherited the Indo-Iranian milking verb, and the chart's three shapes are the three stems the Iranian evidence actually requires. (a) *daug-/*dauǰ- (Nourai's 'dhauğ') survives in the noun *dauga- 'buttermilk' — Shughni δūy, Bartangi δoy, Yazghulami day, and Persian دوغ — and in the East Iranian verbs Ossetic ducyn/dygd, Shughni δūj-, Wakhi δic- 'to milk'; Cheung sets it up as *dauč¹ (*dauǰ?) 'to milk'. (b) *daux- is the past stem (*dauxta- > MP dōxt) behind دوختن ۲. (c) *dauxš- is the present stem behind MP dōš- / NP دوش-, which Cheung files as a separate s-extension, '*dauxš \\\"to suck, suckle, milk\\\" ... a s-formation of IE *dʰeugʰ-'. Abolghasemi (FFD 54) gives exactly this pair: «دوخت < فارسی میانه dōxt < ایرانی باستان *dauxta-» and «دوش < فارسی میانه dōš < ایرانی باستان *dauxš-، ریشهٔ dauš به معنی «دوشیدن»». Buck's caveat that the verb is 'not quotable fr. Av.' is worth keeping: 'Iranian' is the right label precisely because no Avestan form is attested.\",\n     \"derivation_fa\": \"ایرانیِ باستان فعلِ دوشیدنِ هندوایرانی را به ارث برده است و سه صورتی که نورایی آورده همان سه ستاکی است که شواهدِ ایرانی می‌طلبد. نخست *daug-/*dauǰ- (همان «dhauğ») که در نامِ *dauga- «دوغ» زنده مانده است ــ شغنی δūy، بَرتَنگی δoy، یَزغُلامی day و «دوغ» فارسی ــ و در فعل‌های ایرانیِ خاوری مانند اُسِتی ducyn، شغنی δūj- و وخی δic- «دوشیدن»؛ چونگ آن را *dauč¹ «دوشیدن» بازسازی می‌کند. دوم *daux- که ستاکِ گذشته است (*dauxta- > فارسی میانه dōxt) و «دوختن ۲» از آن است. سوم *dauxš- که ستاکِ حال است و فارسی میانه dōš- و «دوش-» فارسی نو از آن می‌آید؛ چونگ آن را صورتی با پسوندِ s از ریشهٔ هندواروپاییِ *dʰeugʰ- می‌داند. ابوالقاسمی (ص ۵۴) دقیقاً همین دو صورت را می‌آورد. یادآوریِ باک هم مهم است: این فعل در اوستا گواهی نشده، و به همین سبب برچسبِ «ایرانی» (نه «اوستایی») درست است.\",\n     \"sources\": [W_DUSH, W_DUGH],\n     \"ref_check\": [\n      {\"ref\": \"POK:271\", \"status\": \"supports\",\n       \"note\": \"IEW 271: 'Indo-iran. *dhaugh- ,melken' in ai. duháti, athem. dógdhi ... pers. dōγ, dōxtan usw.' — Pokorny reconstructs precisely Nourai's *dhaugh- and names the Persian dōγ/dōxtan outcomes.\"},\n      {\"ref\": \"SYN:386\", \"status\": \"supports\",\n       \"note\": \"Buck 5.87 (p.386): 'Skt. duh-, NPers. duxtan, dušīdan, the Indo-Iranian verb for \\\"milk\\\" (though not quotable fr. Av.).'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *dauč¹ and *dauxš\", \"stance\": \"supports\",\n       \"note\": \"'*dauč¹ ... *NWIR: NP dōγ \\\"butter-milk, whey\\\" ... *NEIR: Oss. I. ducyn/dygd ... Sh. δūy (Ё), Bart. δoy, Yzgh. day \\\"buttermilk\\\" (< *dauga-)'; '*dauxš ... *MIDDLE PERSIAN: BMP dwš- /dōš-/ \\\"to milk\\\" ... *NWIR: NP dōxtan/dōš-, Bal. dōšag, Kurd. (Kurm.) dotin/doš-'.\"},\n      {\"src\": \"FFD\", \"where\": \"Abolghasemi p.54 (pdf page 59)\", \"stance\": \"supports\",\n       \"note\": \"«دوختن (۲): دوخت < فارسی میانه dōxt < ایرانی باستان *dauxta- ... دوش < فارسی میانه dōš < ایرانی باستان *dauxš-. s برای ساختن ریشهٔ جدید به ریشه افزوده شده است ... ریشهٔ dauš به معنی «دوشیدن» است.»\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch\", \"stance\": \"silent\",\n       \"note\": \"No Avestan verb daog-/dauxš- 'to milk' is entered; Buck's 'not quotable fr. Av.' is confirmed by the absence.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"dŭxtan, dôxtan; dŭšitan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Book Pahlavi has both stems and both infinitives. MacKenzie's Concise Pahlavi Dictionary p.27 gives '¹dōxtan, dōš- [dwhtn', dwš- | N ~] milk' (kept apart from '²dōxtan, dōz- [dwhtn', dwc-] sew'), and Horn's Grundriss §578 (p.129) — the very page Nourai cites — reads: '(2) dōxten \\\"melken\\\", Praes. dōšem, dōšīden, dōγ \\\"saure Milch\\\" ... ai. √dōh-, dógdhi \\\"melken\\\", dōgha-; phlv. dōxtan (Bund.), dōšītan (Bund., PPGl.)', naming the Bundahišn and the Pahlavi-Pazand Glossary as the sources for the two Pahlavi infinitives. dōxtan continues *dauxta-, dōšītan is the secondary infinitive built on the present stem dōš- (< *dauxš-) with the productive -īt-/-īd- past-stem suffix, the same formation that gives NP دوشیدن. Nourai's 'dŭxtan' and 'dôxtan' are just two transcriptions of the one form (Book Pahlavi ō is often written ū in his system).\",\n     \"derivation_fa\": \"در پهلویِ کتابی هر دو ستاک و هر دو مصدر گواهی شده‌اند. مکنزی در «فرهنگ کوچک پهلوی» می‌نویسد «dōxtan، dōš- [dwhtn', dwš-] دوشیدن» و آن را از «dōxtan، dōz- [dwhtn', dwc-] دوختن (جامه)» جدا می‌کند. هرن نیز در «مبانی ریشه‌شناسی فارسی نو» بندِ ۵۷۸ (ص ۱۲۹) ــ همان صفحه‌ای که نورایی به آن ارجاع داده ــ می‌نویسد: «dōxten «دوشیدن»، حالِ dōšem، dōšīden، dōγ «شیر ترش» ... پهلوی dōxtan (بندهش)، dōšītan (بندهش، فرهنگ پهلوی‑پازند)». صورتِ dōxtan دنبالهٔ *dauxta- است و dōšītan مصدرِ ثانویِ ساخته‌شده بر ستاکِ حالِ dōš- (از *dauxš-) با پسوندِ زایای -īt- است، همان ساختی که «دوشیدن» فارسی نو را می‌سازد. «dŭxtan» و «dôxtan» در نمودار دو آوانگاریِ یک صورت‌اند. ادعای نورایی درست است.\",\n     \"sources\": [W_DUSH],\n     \"ref_check\": [\n      {\"ref\": \"HRN:129\", \"status\": \"supports\",\n       \"note\": \"HRN.txt leaf 150 = printed p.129 (page header '- 129 -'), §578: '(2)dōχten \\\"melken\\\", Praes. dōš-em, dōšīden, dōγ \\\"saure Milch\\\" ... ai. √dōh-, dogdhi \\\"melken\\\", dōgha-; phlv. dōχtan (Bund.), dōšītan (Bund., PPGl.). kurd. dōtin, dušim, di-dōšim \\\"melken\\\" ...' — exactly the two Pahlavi infinitives of the node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. dōxtan (PHD.txt line 314)\", \"stance\": \"supports\",\n       \"note\": \"'¹dōxtan, dōš- [dwhtn', dwš- | N ~] milk. ²dōxtan, dōz- [dwhtn', dwc- | N ~] sew.' and '*dōšīdan [dwšytn'] = *dōxtan' — MacKenzie asterisks dōšīdan (reconstructed for Book Pahlavi), while Horn cites it from the Bundahišn.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n       \"note\": \"Nyberg's glossary (a glossary to his selected texts, not a full lexicon) has duxt 'daughter' but no dōxtan 'to milk' — the verb does not occur in his text selection.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien 275 (via BQT p.892 fn.)\", \"stance\": \"supports\",\n       \"note\": \"Mo'in's Borhan footnote on دوختن refers to «هوبشمان ۲۷۵» for Pahlavi dōxtan; Hübschmann's page is the standard reference for the Pahlavi form behind the New Persian verb.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"dŭšîdan «دوشیدن ( دوش ۴ ، شیردوش )»; dŭšîzeh «دوشیزه»; dŭxtan 2 «دوختن ۲»; dŭğ «دوغ»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Three of the four words are straightforward, the fourth is more complicated. دوشیدن dūšīdan 'to milk' and دوختن ۲ dūxtan 'to milk' are the two New Persian continuants of the Pahlavi pair of node 2 (dōšīdan from the present stem dōš- < *dauxš-, dōxtan from the past stem *dauxta-), the second now obsolete and homographic with دوختن 'to sew'; Mo'in's Borhan (p.892, fn. on دوختن ۲) glosses it «شیر دوشیدن» and refers it to هندی باستان ریشهٔ doh-, dugdhá and Pahlavi dōš-. دوغ dūğ is NOT a direct descendant of that Middle Persian verb: Wiktionary, following the standard treatment, makes it a borrowing from Parthian 𐫅𐫇𐫇𐫃 (dwwg) < Proto-Iranian *dáwgah- (cognate Skt dugdhá-), i.e. a north-western Iranian noun taken into Persian, whose g/γ is the *dauga- stem of node 1 rather than the *dauxš- stem of node 2 — so its place under the Pahlavi box is one step askew, though the root is right and Pokorny 271 himself writes 'pers. dōγ'. دوشیزه dūšīzeh is the one real crux. The word is already Middle Persian — MacKenzie: 'dōšīzag [dwšyck' | (M dwškyzh), N ~a] maiden, virgin. ~īh: maidenhood, virginity' — so it is not a New Persian coinage from دوش-. Mo'in's own footnote in Borhan-e Qāṭeʿ p.899 gives exactly Nourai's analysis: «۱ - از: دوش (دوشیدن) + ایزه (ایو + پسوند تصغیر)؛ لغةً دختر دوشندهٔ (گاو و گوسفند)» — 'literally the girl who milks (cow and sheep)'; Wiktionary's دوشیزه entry gives only the Middle Persian ancestor and no root etymology, so the milking analysis is Mo'in's and Nourai's, not the consensus. The chart's NOTE is sound and checks out: the verse quoted, «بز و میش بد شیرور همچنین / به دوشیزگان داده بد پاکدین» (Shāhnāme, Jamshid/Zahhāk section, the Mardās episode), does appear in the Ganjoor text with دوشیزگان, and the manuscript variant دوشندگان is a known and much-discussed reading, argued for precisely because شیرور 'milk-giving' in the first hemistich calls for 'milkers' rather than 'maidens' in the second.\",\n     \"derivation_fa\": \"از چهار واژهٔ این گره سه تا روشن‌اند و یکی پیچیده. «دوشیدن» و «دوختن ۲» دو دنبالهٔ فارسیِ نوِ همان جفتِ پهلویِ گرهٔ ۲اند: «دوشیدن» بر ستاکِ حالِ dōš- (از *dauxš-) و «دوختن» بر ستاکِ گذشتهٔ *dauxta-؛ دومی امروز متروک است و با «دوختنِ» جامه هم‌نویسه شده. حاشیهٔ معین بر برهان قاطع (ص ۸۹۲) آن را «شیر دوشیدن» معنی می‌کند و به ریشهٔ سنسکریتِ doh- و dugdhá و پهلوی dōš- بازمی‌گرداند. اما «دوغ» دنبالهٔ مستقیمِ آن فعلِ فارسیِ میانه نیست: ویکی‌واژه آن را وام‌واژه‌ای از پارتی dwwg از ایرانیِ باستان *dáwgah- (هم‌ریشه با dugdhá سنسکریت) می‌داند، یعنی نامی شمال‌غربی که به فارسی راه یافته و به ستاکِ *dauga-ی گرهٔ ۱ می‌پیوندد نه به *dauxš-؛ پس جای آن زیر جعبهٔ پهلوی یک پله جابه‌جاست، هرچند خودِ پوکورنی هم در ص ۲۷۱ «pers. dōγ» را زیر همین ریشه آورده است. گرهٔ اصلیِ بحث «دوشیزه» است: این واژه پیش‌تر در فارسی میانه هست ــ مکنزی: «dōšīzag دوشیزه، باکره» ــ پس ساختِ فارسیِ نو از «دوش-» نیست. با این حال معین در حاشیهٔ برهان قاطع (ص ۸۹۹) دقیقاً همان تحلیلِ نورایی را می‌دهد: «از: دوش (دوشیدن) + ایزه (ایو + پسوند تصغیر)؛ لغةً دختر دوشندهٔ (گاو و گوسفند)». ویکی‌واژه هیچ ریشه‌شناسیِ فراتر از فارسی میانه نمی‌دهد، پس این تحلیل از آنِ معین و نورایی است نه اجماعِ پژوهشی. یادداشتِ نمودار هم درست از آب درآمد: بیتِ «بز و میش بد شیرور همچنین / به دوشیزگان داده بد پاکدین» در شاهنامه (بخشِ مرداس و ضحاک) با «دوشیزگان» ضبط شده و ضبطِ «دوشندگان» نسخه‌بدلی شناخته و بحث‌شده است، درست به این دلیل که «شیرور» در مصراع نخست «دوشنده» می‌طلبد.\",\n     \"sources\": [W_DUSH, W_DUGH, W_DUSHIZE, GANJ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:892\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 352 (printed 892): «دوختن ... و شیر دوشیدن را نیز گویند» with Mo'in's footnote 4: «هندی باستان ریشهٔ doh-، dugdhá (دوشیدن)؛ پهلوی dōš... (شیر دوشیدن) «مکی‌نژاد»»; footnote to دوختن ۱ 'to sew' separately: «نیز در فارسی dōxtan پهلوی dōxtan است رک: هوبشمان ۲۷۵».\"},\n      {\"ref\": \"BQT:899\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 359 (printed 899): «دوشیدن - ضم اول و فتح پنجم، [رک: دوختن]؛ خارج کردن شیر از پستان» and «دوغ ... [رک: دوختن]»; and, decisively for this node, Mo'in's footnote 1 on دوشیزه: «از: دوش (دوشیدن؟) + ایزه (ایو، پسوند تصغیر)؛ لغةً دختر دوشندهٔ (گاو و گوسفند)» — literally Nourai's '\\\"milker\\\" of the family'.\"},\n      {\"ref\": \"POK:271\", \"status\": \"supports\",\n       \"note\": \"IEW 271 names 'pers. dōγ, dōxtan usw.' among the Indo-Iranian reflexes of *dhaugh- 'melken'.\"},\n      {\"ref\": \"SYN:386\", \"status\": \"supports\",\n       \"note\": \"Buck 5.87: 'NPers. duxtan, dušīdan, the Indo-Iranian verb for \\\"milk\\\"'.\"},\n      {\"ref\": \"AEF:273\", \"status\": \"not_checked\",\n       \"note\": \"Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsi (the Persian translation/expansion of Horn with Hübschmann's notes) is not digitised anywhere (see refs_online.json); its content for this word is Horn §578 = HRN:129, which was checked and supports.\"},\n      {\"ref\": \"FFD:54\", \"status\": \"supports\",\n       \"note\": \"FFD_pages.txt pdf page 59 = printed p.54: «دوختن (۲): دوخت < فارسی میانه dōxt < ایرانی باستان *dauxta- ... دوش < فارسی میانه dōš < ایرانی باستان *dauxš- ... ریشهٔ dauš به معنی «دوشیدن» است. دوشیدن: دوشید < فارسی میانه dōšīd.»\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. dōšīzag (PHD.txt line 314)\", \"stance\": \"partial\",\n       \"note\": \"'dōšīzag [dwšyck' | (M dwškyzh), N ~a] maiden, virgin. ~īh: maidenhood, virginity.' — the word is Middle Persian, so it cannot be a New Persian derivation from دوشیدن; MacKenzie offers no root etymology.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss §578, p.129\", \"stance\": \"supports\",\n       \"note\": \"'dōγ \\\"saure Milch\\\"' is entered by Horn under the milking verb itself, together with 'waχ. dayōw, sar. dūγoic \\\"Molke\\\"'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *dauč¹ (CHEUNG.txt line 5362)\", \"stance\": \"partial\",\n       \"note\": \"'*NWIR: NP dōγ \\\"butter-milk, whey; a dairy drink of diluted yoghurt and water\\\", Kurd. (Kurm.) daw, (Sor.) do, Tal. dü' — Cheung files دوغ under the *dauč/*daug root, not under *dauxš, i.e. beside the Pahlavi verb rather than under it.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi (MON_part2.txt), s.v. دوشیزه\", \"stance\": \"partial\",\n       \"note\": \"Mo'in's own dictionary entries for دوشیزه give only the sense 'virgin, unmarried girl' («دوشیزه به شوهر دهند و دوشیزه نباشد»); the 'milker' analysis appears only in his Borhan footnote (BQT 899).\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā (ARY_pages.txt pdf p.458 = printed p.459)\", \"stance\": \"partial\",\n       \"note\": \"Aryanpur's page for the milking family notes that the meaning of the cognates outside Iranian is 'شیر، شیر دوشیدن' and adds «شاید بدین علت که شیر دوشیدن مستلزم «مالش» یا «مالیدن» است» — i.e. he too derives 'milk' from 'stroke, rub', as Buck does.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Indo-European\",\n     \"words\": \"Dhugh-tar\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"This is the weak arrow of the page. The word itself is beyond doubt: PIE *dʰugh₂tḗr 'daughter', continued by Skt duhitár-, Av. dugədar-/duγδar-, Arm. dustr, Gk. θυγάτηρ, Osc. futír, Goth. daúhtar, Lith. duktė̃, OCS dŭšti, Toch. A ckācar / B tkācer. What is disputed is Nourai's gloss 'milker (of the family)', i.e. deriving it from the *dʰewgʰ- of the root box. Against it: (a) Bartholomae, Altiranisches Wörterbuch s.v. dugəda-/duγδar-, says flatly that 'die Deutung des Wortes als \\\"Melkerin\\\" ... ist ohne Wert'; (b) Walde-Pokorny I 868 cite the literature (Bartholomae AiW 748, Boisacq 355) expressly 'gegen weitere Anknüpfung an ai. duh- \\\"melken\\\" oder idg. *dheugh- \\\"taugen\\\"'; (c) Pokorny 1959 puts the word on p.277 as an independent root and adds only the phonological remark 'Guttural wie bei *eĝ(h)om \\\"ich\\\"' — that is, the guttural is anomalous (*gʰ vs *ǵʰ), which is itself an argument against the equation; (d) Watkins/AHD lists dhugheter- as its own root with no cross-reference to dheugh-. The decisive modern argument is the laryngeal: the word is reconstructed *dʰugh₂tḗr (Greek θυγατέρα, Vedic duhitā́ with its metrical -i-), and *dʰewgʰ- has no h₂, so the two cannot be related as parent and derivative without special pleading. Wiktionary still records the old idea, but only as a hypothesis: 'Perhaps from *dʰewgʰ- (\\\"to produce\\\"), originally meaning \\\"the (potential) suckler, the one that draws milk\\\"'. The 19th-century sources Nourai follows (Skeat: 'The Skt. duhitṛ seems to have meant \\\"milker\\\" of the cows; from duh (=dugh), to milk') are exactly the ones later scholarship set aside.\",\n     \"derivation_fa\": \"این پیکان ضعیف‌ترین حلقهٔ صفحه است. خودِ واژه بی‌تردید است: *dʰugh₂tḗr هندواروپاییِ آغازین «دختر»، که در سنسکریت duhitár-، اوستایی dugədar-/duγδar-، ارمنی dustr، یونانی θυγάτηρ، گوتی daúhtar، لیتوانیایی duktė̃ و تخاری ckācar/tkācer بازمانده است. آنچه مورد اختلاف است معنایی است که نورایی می‌دهد، یعنی «دوشندهٔ خانواده» و گرفتنِ آن از ریشهٔ *dʰewgʰ-. در ردِّ این نظر: نخست، بارتولومه در «فرهنگ ایرانی باستان» ذیل dugəda-/duγδar- صریح می‌نویسد «تفسیرِ این واژه به «دوشنده» ... بی‌ارزش است»؛ دوم، والده‑پوکورنی (جلد ۱ ص ۸۶۸) منابع را «در ردِّ پیوندِ بیشتر با duh- سنسکریت «دوشیدن» یا *dheugh- هندواروپایی» یاد می‌کند؛ سوم، پوکورنی در چاپ ۱۹۵۹ آن را ریشهٔ مستقلی در صفحهٔ ۲۷۷ می‌آورد و تنها می‌افزاید «همخوانِ پسکامیِ آن مانندِ *eĝ(h)om «من» است»، یعنی خودِ این همخوان با ریشهٔ dheugh- نمی‌خواند؛ چهارم، واتکینز در پیوستِ فرهنگِ میراثِ آمریکایی dhugheter- را ریشه‌ای جداگانه و بدون ارجاع به dheugh- می‌آورد. دلیلِ قاطعِ امروزی حنجره‌ای است: صورتِ بازسازی‌شده *dʰugh₂tḗr است (با گواهیِ θυγατέρα یونانی و duhitā́ ودایی) و *dʰewgʰ- هیچ h₂ ندارد. ویکی‌واژه هنوز نظرِ کهن را می‌آورد ولی تنها با قیدِ «شاید». پس پژوهشِ امروزی ادعای نورایی را در این گره نمی‌پذیرد، هرچند منابعِ سدهٔ نوزدهمی که او پی گرفته (مانند اسکیت) همین را می‌گفتند.\",\n     \"sources\": [W_DHUG, E_DAUGH],\n     \"ref_check\": [\n      {\"ref\": \"SHP:329\", \"status\": \"not_checked\",\n       \"note\": \"Shipley, Dictionary of Word Origins (1945) is not on disk and the HathiTrust full-view copy IP-blocks this host (see refs_online.json s.v. SHP); the page could not be read. Shipley is a popular work and would in any case not settle the question.\"},\n      {\"ref\": \"POK:277\", \"status\": \"contradicts\",\n       \"note\": \"IEW 277: 'dhug(h)ǝter- \\\"Tochter\\\"; Guttural wie bei *eĝ(h)om \\\"ich\\\", s. dort. Ai. duhitár- (duhitā́), av. dugədar-, duγδar- (aus *dhughter-), npers. duxtar, duxt ... WP. I 868, WH. I 557.' A standalone root with no link to dheugh- 271 and no 'milker' gloss; the note on the guttural flags the irregularity.\"},\n      {\"ref\": \"WLD:868\", \"status\": \"contradicts\",\n       \"note\": \"Walde-Pokorny I 868: '... Lit. bei Bartholomae Airan. Wb. 748, Boisacq 355, auch gegen weitere Anknüpfung an ai. duh- \\\"melken\\\" oder idg. *dheugh- \\\"taugen\\\" (letzteres bei Fick I⁴ 74).'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.v. dugəda-/duγδar- (BRT.txt line 13645 ff., col. ~748)\", \"stance\": \"contradicts\",\n       \"note\": \"The entry's footnote, as read in the OCR: '... die Deutung des Worts als \\\"Melkerin\\\", zuletzt bei ... Festschr. Roth 35, ist ohne Wert; desgleichen die bei L. Meyer GrEt 3, 442.' Bartholomae rejects the 'milker' etymology outright.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt line 392)\", \"stance\": \"contradicts\",\n       \"note\": \"'dhugheter-. Daughter. Germanic *dohtēr in Old English dohtor, daughter: DAUGHTER. [Pok. dhug(h)eter 277.]' — an independent root entry; Watkins's dheugh- entry (line 382) gives only 'To produce something of utility' and yields HEPTATEUCH, DOUGHTY.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.v. Daughter (SKT.txt line 4737)\", \"stance\": \"supports\",\n       \"note\": \"'Skt. duhitri. The Skt. duhitri seems to have meant \\\"milker\\\" of the cows; from duh (=dugh), to milk.' This is the 1880s view Nourai reproduces — useful as the source of the claim, not as a modern confirmation.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 2.42 / 5.87\", \"stance\": \"partial\",\n       \"note\": \"Buck notes at 5.87 that the connection of Indo-Iranian duh- with Gk τεύχω / Goth. daug 'is generally rejected on semantic grounds', which removes the very IE root Nourai needs as the parent of 'daughter'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann (IEC.txt, d- section)\", \"stance\": \"silent\",\n       \"note\": \"Mann's dictionary has dheughō, dhough-, dhugh- and dhughno- but no *dhug(h)ǝter- headword and no derivation of 'daughter' from them.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Avestan\",\n     \"words\": \"dugeda, duğdâr; bağa-duğdâr; â-zarema-dugedâ\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Only the first pair is Avestan. dugəda- (Gathic nominative dugədā) and duγδar- 'daughter' are the real forms — Bartholomae s.v. 'dugəda-, j. duγδar- \\\"Tochter\\\"' (col. ~748), Klein p.404 'Avestic dugəda-, duγδar-', Nyberg II s.v. duxt 'Av. (748) dugədar-, duγδar-, nom. dugədā, duγδa'. The oblique stem duγδar- < *dugətar- shows the regular Avestan syncope of the unstressed medial vowel in the end-stressed cases (Bartholomae IF 7, 53 ff., cited by Walde-Pokorny) and the assimilation t > δ after γ; the gloss 'daughter' is right, but 'milker' is not (see node 4). The other two 'words' are not attested Avestan compounds. baγa-duγδār- is Nourai's Avestanisation of the name behind Persian بیدخت: Mo'in's own footnote in Borhan-e Qāṭeʿ p.333 says «بقول شفتلوویتز اصل آن «بغدخت» است یعنی دختر بغ (خدا)» — Schaeftelowitz reconstructed a Middle Persian *Baγ-duxt 'daughter of the god', not an Avestan form, and the name is not in Bartholomae. ā-zarəma-dugədā- is likewise unattested: Bartholomae has a simplex a-zarəma- (col. 326) but glosses it 'nicht abnehmend (an Stärke, von der Stimme)' — said of the voice at FrW. 1.1, not of a woman — and the adjective for 'unaging' is a-zarəšant-. There is no Avestan compound with dugədā in either case.\",\n     \"derivation_fa\": \"از سه «واژه»ی این گره تنها جفتِ نخست اوستایی است. dugəda- (فاعلیِ گاهانی dugədā) و duγδar- «دختر» صورت‌های واقعی‌اند: بارتولومه ذیل «dugəda-، جوان‌اوستایی duγδar- «دختر»» (ستون ۷۴۸)، کلاین (ص ۴۰۴) و نیبرگ (ذیل duxt) همه همین‌ها را می‌آورند. ستاکِ غیرفاعلیِ duγδar- از *dugətar- است و افتادنِ واکهٔ میانیِ بی‌تکیه در حالت‌های پایان‌تکیه‌ای قاعدهٔ شناخته‌شده‌ای است (بارتولومه، IF ۷ ص ۵۳ به بعد) و t پس از γ به δ همگون شده است؛ معنای «دختر» درست است ولی «دوشنده» نه (نگاه کنید به گرهٔ ۴). اما دو «واژه»ی دیگر ترکیب‌های اوستاییِ گواهی‌شده نیستند. baγa-duγδār- ساختهٔ خودِ نورایی است بر پایهٔ نامِ فارسیِ «بیدخت»؛ حاشیهٔ معین بر برهان قاطع (ص ۳۳۳) می‌نویسد «بقول شفتلوویتز اصل آن «بغدخت» است یعنی دختر بغ (خدا)» ــ یعنی بازسازیِ *Baγ-duxt در فارسی میانه، نه صورتی اوستایی، و چنین نامی در بارتولومه نیست. ā-zarəma-dugədā- نیز گواهی نشده است: بارتولومه صفتِ سادهٔ a-zarəma- را دارد (ستون ۳۲۶) ولی آن را «کاستی‌ناپذیر (در نیرو، دربارهٔ آوا)» معنی می‌کند که در FrW. ۱٫۱ دربارهٔ صدا به کار رفته نه دربارهٔ زن، و صفتِ «پیرنشدنی» در اوستا a-zarəšant- است. پس دو ترکیبِ این گره را پژوهشِ امروزی نمی‌پذیرد.\",\n     \"sources\": [W_DOXT, W_DHUG],\n     \"ref_check\": [\n      {\"ref\": \"KLN:404\", \"status\": \"partial\",\n       \"note\": \"KLN_1966.txt leaf 222, printed p.404 s.v. daughter: '... cogn. with OI. duhitā, Avestic dugəda-, duγδar-, Toch. A ckācar, B tkācer, Arm. dustr, Gk. θυγάτηρ, OSlav. dŭšti, OPruss. duckti, Lith. duktė, \\\"daughter\\\".' Klein confirms the two Avestan forms exactly as printed in the chart, but gives no 'milker' etymology and no compounds.\"},\n      {\"ref\": \"POK:277\", \"status\": \"partial\",\n       \"note\": \"IEW 277: 'av. dugədar-, duγδar- (aus *dhughter-)' — the forms, but again no compounds and no 'milker'.\"},\n      {\"ref\": \"BQT:333\", \"status\": \"partial\",\n       \"note\": \"Read from the page image (archive.org borhan-ghate-v1 leaf n553; transcription saved as data/verification/sources/refs/ocr/BQT/333.vision.txt). Mo'in's footnote 4 on بیدخت: «= بغدخت؛ بقول شفتلوویتز اصل آن «بغدخت» است یعنی دختر بغ (خدا). و آن به ستارهٔ زهره اطلاق شده ... رک: مزدیسنا ۳۳۰ و ۳۲۹.» It supports the sense 'daughter of God' but reconstructs a Middle Persian *baγ-duxt, not the Avestan baγa-duγδār- of the chart.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 326 and ~748 (BRT.txt lines 5989, 13645)\", \"stance\": \"contradicts\",\n       \"note\": \"col. ~748: 'g. dugəda-, j. duγδar- \\\"Tochter\\\"' with the footnote rejecting the 'Melkerin' reading; col. 326: 'a-zarəma- Adj. (fem. -mā-) \\\"nicht abnehmend\\\" (an Stärke, von der Stimme): frā staotr̥bīš yesnīm °mya (IS.) vaca mruiiā FrW. 1.1', immediately followed by 'a-zarəšant- Adj. \\\"nicht alternd\\\"'. Neither a baγa- nor an ā-zarəma- compound with dugədā is in the dictionary.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. duxt (NYB_vol2_glossary.txt line 1413)\", \"stance\": \"supports\",\n       \"note\": \"'duxt [dwht'; BRTH] daughter ... Av. (748) dugədar-, duγδar-, nom. dugədā, duγδa; MPrs dwγt ...; NP duxtar' — the Avestan forms and the reference to Bartholomae col. 748.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 (PHD.txt lines 225, 318)\", \"stance\": \"contradicts\",\n       \"note\": \"MacKenzie has both 'āzarm [clm | M ʾʾzrm, N ~] honour, respect' / 'āzarmīg [clmyk'] honoured, respected' and, separately, 'a-zarmān [ʾzlmn'] ageless, unaging'. The name Āzarmīgduxt belongs to the first, not the second — so the Avestan ā-zarəma- 'non-aging' base of this node is the wrong ancestor (see node 6).\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 868\", \"stance\": \"supports\",\n       \"note\": \"'av. dugədar-, duγδar-' listed among the cognates; no compounds.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Persian\",\n     \"words\": \"doxtar «دختر ( دخت )»; Bîdoxt «بیدخت»; Âzarmîdoxt «آزرمیدخت»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"دختر doxtar and its short form دخت doxt are impeccable: Av. duγδar- > MP duxt / duxtar (Book Pahlavi dwht', dwhtl; MacKenzie 'duxt ... daughter. ~ar ... daughter') > NP doxtar, with Avestan/Old Iranian γδ regularly giving MP/NP xt (compare Av. draoγa- : NP دروغ, Av. uγra- : ...) and the -tar suffix retained in the fuller form. Mo'in's Borhan footnote at p.826 gives just this: «اوستا duγδar (دختر)، پهلوی duxt ...، هندی باستان duhitā، ارمنی dustr ...، هوبشمان ۱۴۵». بیدخت Bīdoxt, the name of the planet Venus (Anāhitā), is likewise well supported: Mo'in (Borhan p.333, fn. 4) writes «= بغدخت؛ بقول شفتلوویتز اصل آن «بغدخت» است یعنی دختر بغ (خدا)» — MP *Baγ-duxt 'daughter of the god' > بغدخت > بیدخت with the regular loss of the intervocalic γ and compensatory lengthening; Mo'in adds that the Islamic magic-square word بدوح Budūḥ has been identified with this Iranian-Aramaic name of Venus. آزرمیدخت Āzarmīdoxt is the one that fails. She is the Sasanian queen of 630-631, daughter of Khosrow II, and her Middle Persian name is Āzarmīgduxt = āzarmīg 'honoured, venerated' + duxt 'daughter', i.e. 'daughter of the venerated one' (MacKenzie: 'āzarmīg [clmyk'] honoured, respected'; Nyberg derives āzarm from Av. abi-gar- 'to praise', < *abi-jarman-). Nourai's 'ageless woman', via an Avestan ā-zarəma- 'non-aging', is a folk-etymology built on the accidental resemblance of āzarm 'honour' to the negated root zar- 'to grow old' — Middle Persian does have azarmān 'ageless, unaging', but it is a different word from āzarm and is not the first element of the queen's name.\",\n     \"derivation_fa\": \"«دختر» و کوتاه‌شدهٔ آن «دخت» بی‌عیب‌اند: اوستایی duγδar- > فارسی میانه duxt/duxtar (نگارشِ پهلوی dwht' و dwhtl؛ مکنزی: «duxt دختر، duxtar دختر») > فارسی نو «دختر»، و تبدیلِ قاعده‌مندِ γδ ایرانی به xt در فارسی میانه و نو (قس اوستایی draoγa- : «دروغ») و ماندنِ پسوندِ -tar در صورتِ بلندتر. حاشیهٔ معین بر برهان قاطع (ص ۸۲۶) دقیقاً همین را می‌آورد: «اوستا duγδar (دختر)، پهلوی duxt، هندی باستان duhitā، ارمنی dustr، هوبشمان ۱۴۵». «بیدخت»، نامِ ستارهٔ زهره (ناهید)، نیز پشتوانهٔ خوبی دارد: معین در ص ۳۳۳ می‌نویسد «= بغدخت؛ بقول شفتلوویتز اصل آن «بغدخت» است یعنی دختر بغ (خدا)»؛ یعنی *Baγ-duxt فارسی میانه با افتادنِ غِ میانِ دو واکه به «بیدخت» رسیده است، و معین می‌افزاید که «بدوح»ِ اسلامی را همین نام دانسته‌اند. اما «آزرمیدخت» نادرست است: او ملکهٔ ساسانی (۶۳۰–۶۳۱ م.) و دخترِ خسروپرویز است و نامِ فارسیِ میانه‌اش Āzarmīgduxt یعنی āzarmīg «ارجمند، گرامی‌داشته» + duxt «دختر»، یعنی «دخترِ آن ارجمند» (مکنزی: «āzarmīg گرامی‌داشته، محترم»؛ نیبرگ āzarm را از اوستایی abi-gar- «ستودن» می‌گیرد). معنای «زنِ پیرنشدنی» که نورایی از اوستایی ā-zarəma- ساخته ریشه‌شناسیِ عامیانه‌ای است بر پایهٔ شباهتِ تصادفیِ «آزرم» با ریشهٔ zar- «پیر شدن»؛ فارسی میانه azarmān «پیرنشدنی» را دارد، اما آن واژهٔ دیگری است و جزءِ نخستِ نامِ این ملکه نیست.\",\n     \"sources\": [W_DOXT, WK_AZARM],\n     \"ref_check\": [\n      {\"ref\": \"BQT:333\", \"status\": \"supports\",\n       \"note\": \"Mo'in's footnote 4 on بیدخت (read from the page image, transcription in refs/ocr/BQT/333.vision.txt): «= بغدخت؛ بقول شفتلوویتز اصل آن «بغدخت» است یعنی دختر بغ (خدا). و آن به ستارهٔ زهره اطلاق شده ... بعضی اساس «بدوح» Budûh اسلامی را همین نام آرامی ایرانی ستارهٔ زهره ـ یعنی بیدخت ـ میدانند «دائرةالمعارف اسلام: بدوح»، رک: مزدیسنا ۳۳۰ و ۳۲۹.» Exactly Nourai's gloss '\\\"daughter of God\\\"'.\"},\n      {\"ref\": \"BQT:826\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 286 (printed 826), headwords «دختر» and «دخت ... مخفف دختر است»; Mo'in's footnote 5: «دختر - (مخفف آن دخت). اوستا duγδar (دختر)؛ پهلوی duxt...؛ هندی باستان duhitā؛ ارمنی dustr؛ کردی dot، keç؛ وخی δəγd؛ ... هوبشمان ۱۴۵ ... نیز در پهلوی duxtar «معنای ۲۷۲»».\"},\n      {\"ref\": \"WLD:868\", \"status\": \"supports\",\n       \"note\": \"Walde-Pokorny I 868 lists 'npers. duxtar, duxt' among the reflexes of dhug(h)ater- — the Persian forms of this node exactly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 (PHD.txt lines 225, 318)\", \"stance\": \"contradicts\",\n       \"note\": \"'duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter' — supports doxtar; but 'āzarm [clm] honour, respect', 'āzarmīg [clmyk'] honoured, respected' vs. the separate 'a-zarmān [ʾzlmn'] ageless, unaging' show that Āzarmīg-duxt belongs to āzarm 'honour', not to the 'ageless' word.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.vv. duxt and āžarm (NYB_vol2_glossary.txt lines 1413, 882)\", \"stance\": \"contradicts\",\n       \"note\": \"'āžarm [clm] honour, renown; favouring, respect of persons. — MPrs ʾzrm \\\"honour\\\" (BBB 53); Paz. NP āzarm. From Av. (512) abi-gar- \\\"to praise, to assent to with cheers\\\"; < *abi-jarman-' — a completely different etymon from a- + zar- 'to grow old'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie (HRN.txt line 661)\", \"stance\": \"partial\",\n       \"note\": \"Horn treats آزرم with the meaning 'Ehre, Achtung' and the negated anāzarm, i.e. the 'honour' word, not an 'ageless' one.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, printed p.267 (ARY_pages.txt pdf p.266)\", \"stance\": \"supports\",\n       \"note\": \"Entry «دخت، دختر» with the cognate list (Avestan, Pahlavi, Kurdish, Tocharian A/B, Sanskrit, Armenian, Greek, Gothic, Old Norse, OHG, OE, English, OCS, Lithuanian, Latvian) and a reference to برهان قاطع; the OCR of the Latin-script forms is too damaged to quote, but the cognate set is the standard one.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Germanic\",\n     \"words\": \"dohter, dohtor\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The Germanic branch of *dʰugh₂tḗr is Proto-Germanic *duhtēr, with the regular Grimm's-Law outcomes (*dʰ > d, *gʰt > *ht) and the -ter kinship suffix preserved: Gothic daúhtar, Old Norse dóttir (runic nom. pl. dohtriR), Old Saxon dohtar, Old English dohtor/dohter, Old High German tohter, Old Frisian/Dutch dochter, German Tochter. The two forms Nourai prints, 'dohter, dohtor', are in fact the Old English (and Old Saxon) spellings rather than a Proto-Germanic reconstruction — Watkins gives 'Germanic *dohtēr in Old English dohtor' — but as a stage between the IE word and English they are correctly placed. Etymonline gives the same chain: Old English dohtor, Proto-Germanic *dokhter, earlier *dhutēr, from PIE *dhugheter.\",\n     \"derivation_fa\": \"شاخهٔ ژرمنیِ *dʰugh₂tḗr صورتِ ژرمنیِ آغازینِ *duhtēr است، با دگرگونی‌های قاعده‌مندِ قانونِ گریم (*dʰ > d و *gʰt > ht) و نگاه‌داشتنِ پسوندِ خویشاوندیِ -ter: گوتی daúhtar، نورس کهن dóttir، ساکسونِ کهن dohtar، انگلیسیِ کهن dohtor/dohter، آلمانیِ علیای کهن tohter، فریزی و هلندی dochter، آلمانی Tochter. دو صورتی که نورایی چاپ کرده («dohter، dohtor») در واقع املای انگلیسیِ کهن (و ساکسونِ کهن) است نه بازسازیِ ژرمنیِ آغازین ــ واتکینز می‌نویسد «ژرمنی *dohtēr در انگلیسیِ کهن dohtor» ــ اما به‌عنوانِ مرحله‌ای میانِ واژهٔ هندواروپایی و انگلیسی درست جای گرفته است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [E_DAUGH, W_DHUG],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 392): 'dhugheter-. Daughter. Germanic *dohtēr in Old English dohtor, daughter: DAUGHTER. [Pok. dhug(h)eter 277.]' — the Germanic step exactly as drawn (though from a root Watkins keeps separate from dheugh-).\"},\n      {\"ref\": \"PEI:45\", \"status\": \"supports\",\n       \"note\": \"PEI.txt leaf 64, printed p.45: 'Another root with extensive outside connections, but a single line of English descent, is that of *dhug(h)əter, \\\"daughter\\\". ... Anglo-Saxon dohtor, which gives us daughter, daughter-in-law, daughterly, etc., has cognates in all the Germanic languages (German Tochter, Icelandic dottir, etc.)', with the tree 'IE *dhug(h)əter → AS dohtor → Eng. daughter'. Pei's page carries an error of his own ('Sanskrit duhitā, Persian duhitar'), but the Germanic line is Nourai's.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p.404 s.v. daughter (KLN_1966.txt leaf 222)\", \"stance\": \"supports\",\n       \"note\": \"'ME doghter, dohter, fr. OE. dohtor, dohter, rel. to OS. dohtar, ON. dóttir, OFris., Du. dochter, OHG., MHG. tohter, G. Tochter, Goth. dauhtar, \\\"daughter\\\"'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Daughter (SKT.txt line 4737)\", \"stance\": \"supports\",\n       \"note\": \"'M.E. doughter, dohter. A.S. dohtor. + Du. dochter, Dan. datter, Swed. dotter, Icel. dóttir, Goth. dauhtar, G. tochter, Russ. dochere, Gk. θυγάτηρ, Skt. duhitā.'\"},\n      {\"src\": \"POK\", \"where\": \"IEW 277\", \"stance\": \"supports\",\n       \"note\": \"'got. daúhtar, anord. dóttir (run. nom. pl. dohtriR), ahd. tohter' — the Germanic set.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"English\",\n     \"words\": \"daughter\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old English dohtor > Middle English doghter, dohter > Modern English daughter. The spelling with -gh- is a Middle English scribal rendering of the surviving velar fricative /x/, which was later lost in the south (the /x/ still audible in Scots dochter), leaving the diphthong that gives the modern /ˈdɔːtər/. The node carries no references in the book, which is reasonable: this is one of the least controversial chains in the language.\",\n     \"derivation_fa\": \"انگلیسیِ کهن dohtor > انگلیسیِ میانه doghter/dohter > انگلیسیِ امروز daughter. نگارشِ gh در انگلیسیِ میانه نشانهٔ سایشیِ کامیِ /x/ است که بعدها در جنوبِ انگلستان افتاد (و هنوز در اسکاتسیِ dochter شنیده می‌شود) و از آن واکهٔ مرکبِ امروزی برجای ماند. این گره در کتاب هیچ ارجاعی ندارد و این پذیرفتنی است، چون یکی از کم‌اختلاف‌ترین زنجیره‌های زبانِ انگلیسی است. ادعای نورایی درست است.\",\n     \"sources\": [E_DAUGH],\n     \"ref_check\": [\n      {\"ref\": \"(none in the book)\", \"status\": \"not_checked\",\n       \"note\": \"The node prints no reference (refs=None). The chain is covered by Klein p.404 and by Etymonline, both checked under 'consulted'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p.404 s.v. daughter\", \"stance\": \"supports\",\n       \"note\": \"'daughter, n. — ME doghter, dohter, fr. OE. dohtor, dohter ...'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Daughter\", \"stance\": \"supports\",\n       \"note\": \"'Daughter (E.) M.E. doughter, dohter. A.S. dohtor.'\"},\n      {\"src\": \"PEI\", \"where\": \"Pei p.45\", \"stance\": \"supports\",\n       \"note\": \"'Anglo-Saxon dohtor, which gives us daughter, daughter-in-law, daughterly, etc.'\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"duhi-tar\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The form is right and its descent from the IE word is certain: Vedic duhitár- (nom. duhitā́) 'daughter', with the -i- that Indo-Iranian shows for the laryngeal of *dʰugh₂tḗr (Vedic metrics require a disyllabic reading, which is the main evidence for the h₂). Pokorny 277 heads the entry with 'Ai. duhitár- (duhitā́)'. What is disputed is Nourai's gloss and analysis, 'one who milks the cow': that is the segmentation duh- 'to milk' + -tar agent suffix which Skeat (1911) still printed and which Bartholomae dismissed as 'ohne Wert' and Walde-Pokorny I 868 recorded the literature as being 'gegen'. Formally the agent noun of duh- is dógdhar-/duh-tár-, not duhi-tár-, and the accent and the -i- both point elsewhere. The homophony with duh- is real but is now taken as accidental; the connection survives in Wiktionary only as 'perhaps'. The node's reference, CEL3:321 (Gupta, A Comparative Etymologic Lexicon, vol. 3), is not digitised anywhere and could not be consulted.\",\n     \"derivation_fa\": \"صورتِ واژه درست است و پیوندِ آن با واژهٔ هندواروپایی قطعی: duhitár- ودایی (فاعلی duhitā́) «دختر»، با همان i که در هندوایرانی جانشینِ حنجره‌ایِ *dʰugh₂tḗr شده است (وزنِ اشعارِ ودایی خواندنِ دوهجاییِ آن را می‌طلبد و همین اصلی‌ترین گواهِ وجودِ h₂ است). پوکورنی نیز مدخلِ صفحهٔ ۲۷۷ را با «سنسکریت duhitár- (duhitā́)» آغاز می‌کند. آنچه مورد اختلاف است معنایی است که نورایی داده، یعنی «آنکه گاو را می‌دوشد»: این تجزیهٔ duh- «دوشیدن» + پسوندِ فاعلیِ -tar همان است که اسکیت در ۱۹۱۱ می‌نوشت و بارتولومه آن را «بی‌ارزش» خواند و والده‑پوکورنی (ج ۱ ص ۸۶۸) منابع را در ردِّ آن یاد کرد. از نظرِ ساختی، اسمِ فاعلِ duh- در سنسکریت dógdhar-/duh-tár- است نه duhi-tár-، و جایگاهِ تکیه و آن i هر دو به جای دیگری اشاره می‌کنند. هم‌آواییِ آن با duh- واقعی است ولی امروز تصادفی دانسته می‌شود و ویکی‌واژه هم آن را تنها با قیدِ «شاید» می‌آورد. مأخذی که نورایی داده (گوپتا، جلد ۳ ص ۳۲۱) هیچ‌جا دیجیتالی نشده و بررسی نشد.\",\n     \"sources\": [W_DHUG],\n     \"ref_check\": [\n      {\"ref\": \"CEL3:321\", \"status\": \"not_checked\",\n       \"note\": \"S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words — catalogue records only; HathiTrust has the 1986- edition as search-only and no copy is downloadable (refs_online.json s.v. CEL). The page could not be read.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 277\", \"stance\": \"partial\",\n       \"note\": \"'Ai. duhitár- (duhitā́) ... \\\"Tochter\\\"' — the form, glossed only 'daughter', with no milking analysis.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 868\", \"stance\": \"contradicts\",\n       \"note\": \"'Ai. duhitár-, (duhitā) ... auch gegen weitere Anknüpfung an ai. duh- \\\"melken\\\" oder idg. *dheugh- \\\"taugen\\\".'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Daughter (SKT.txt line 4737)\", \"stance\": \"supports\",\n       \"note\": \"'The Skt. duhitri seems to have meant \\\"milker\\\" of the cows; from duh (=dugh), to milk.' — the source of the chart's gloss, and a superseded one.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.87 (p.386)\", \"stance\": \"partial\",\n       \"note\": \"Buck confirms 'Skt. duh-' as the Indo-Iranian verb 'to milk' but does not derive duhitár- from it, and rejects the wider IE connection on semantic grounds.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-131.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk131.py"
}
```


### [2026-09-05T20:26:09.399Z] TOOL RESULT

```
written
```


## [2026-09-05T20:26:14.002Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-131.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 131"
}
```


### [2026-09-05T20:26:16.065Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 3, 'confirmed': 5, 'disputed': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 17, 'partial': 6, 'not_checked': 4, 'contradicts': 2}
books consulted: {'supports': 22, 'partial': 12, 'silent': 4, 'contradicts': 7} | by book: {'CHEUNG': 5, 'PHD': 5, 'BRT': 4, 'WLD': 4, 'SKT': 4, 'HRN': 3, 'NYB': 3, 'FFD': 2, 'IEC': 2, 'ARY': 2, 'SYN': 2, 'KLN': 2, 'POK': 2, 'BQT': 1, 'HUB': 1, 'MON': 1, 'AHD': 1, 'PEI': 1}
```


## [2026-09-05T20:26:40.682Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-131.json`; `verify_check.py 131` reports **12/12 nodes, 0 PROBLEM lines**.

**Counts** — nodes: 5 confirmed, 3 plausible, 4 disputed. Roots: Dheu 3 confirmed, Dheugh/Dhugh plausible. Ref checks: 17 supports, 6 partial, 2 contradicts, 4 not_checked (SHP:329, CEL3:321, AEF:273 — none digitised; node 8 has no refs).

**Disputed items**
- *Dheugh #4 `Dhugh-tar` "milker (of the family)"* — the arrow from "to milk" is rejected by Nourai's own cited pages: WLD I 868 cites the literature "**gegen** weitere Anknüpfung an ai. duh- 'melken' oder idg. *dheugh-", POK 277 is a separate root, and Bartholomae (s.v. dugəda-) calls the "Melkerin" reading "**ohne Wert**". Modern *dʰugh₂tḗr has an h₂ that *dʰewgʰ- lacks.
- *#5 Avestan `bağa-duğdâr`, `â-zarema-dugedâ`* — neither is an attested Avestan compound. Mo'in (BQT 333) reconstructs MP *baγ-duxt, not Avestan; Bartholomae col. 326 glosses a-zarəma- "nicht abnehmend (von der Stimme)", of the voice, not a woman.
- *#6 Persian `Âzarmîdoxt` "ageless woman"* — MP Āzarmīgduxt = āzarmīg "honoured, venerated" + duxt (MacKenzie; Nyberg derives āzarm < Av. abi-gar- "to praise"). MP azarmān "ageless" is a different word.
- *#9 Sanskrit `duhi-tar` "one who milks the cow"* — form certain, gloss is Skeat's 1911 analysis, superseded.

**Notable confirmations** — Pokorny 261 really does carry a third `dheu- "blank, glänzen"`; Abolghasemi (FFD 32/58) gives exactly *ham-dau-ta- / *uz-dau-ta- for اندودن/زدودن; Horn §578 p.129 gives both Pahlavi infinitives; Mo'in (BQT 899) does literally analyse دوشیزه as «لغةً دختر دوشندهٔ (گاو و گوسفند)»; the Ferdowsi verse and the دوشندگان variant of the chart's NOTE both check out (Ganjoor). Caveat recorded: دوغ is a Parthian loan (*dáwgah-), so it sits one step askew under the Pahlavi box.

**Extraction errors: none.** I read the printed page (pdftoppm p.131) — the JSON is faithful to the book throughout. Two page-number drifts in Nourai's own citations: BQT:1008 (زدودن is at printed ~1010) and BQT:892 is دوختن-2, both close enough to count as his.

New audit files: `data/verification/sources/refs/ocr/BQT/333.vision.txt` + `333.png` (Mo'in's بیدخت footnote, read from the scan), and 9 archived web sources.
