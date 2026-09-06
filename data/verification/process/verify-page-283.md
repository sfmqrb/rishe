# Verification process log — verify-page-283


## [2026-09-06T21:37:31.847Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 283 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-283.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-283.json. Write /home/sfmqrb/git/rishe/data/verification/page-283.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 283` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:37:33.645Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T21:37:34.235Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:37:34.251Z] TOOL RESULT

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


## [2026-09-06T21:37:34.488Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-283.txt"
}
```


### [2026-09-06T21:37:34.517Z] TOOL RESULT

```
1	=== PDF page 283 (book page 253) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kŭ 1, Kĕu 5 : to burn  (refs POK:595)
4	#1 (parent #0) [Greek] refs=POK:595; WLD1:376; KLN:223 | Kalo : to burn, firewood ; kalo-podein : wooden foot, mold ☞Ped
5	  #2 (parent #1) [Pahlavi] refs=BQT:1095 | kal-pâd : fabrication mold, shape, body | NOTE: IEC:1049,1051 derives this word from Avestan "kehrp: flesh", from Indo-European root "Kwrp, Kwerp: shape, form body".
6	    #3 (parent #2) [Persian] refs=MON:2858; IEC:1047 | kâlâ «کالا» : manufactured good, merchandise | NOTE: References not clear on the exact path of derivation
7	#4 (parent #0) [Persian] refs=BQT:1075; MON:2859 | kâleb «کالب» : mold, body ; kâlbod «کالبد» : body
8	  #5 (parent #4) [Arabic] refs=KLN:223; PLA:215 | qâlib : mold ; q.l.b : to make, turn around
9	    #6 (parent #5) [Persian] refs=MON:2621; FVA:337 | qâleb «قالب» : mold | extra: قلب ، انقلاب ، منقلب
10	مقلوب ، تقلب ، قلاب
11	    #7 (parent #5) [Italian] refs=KLN:223 | calibro : mold, size
12	      #8 (parent #7) [French] refs=None | 
13	        #9 (parent #8) [Persian] refs=MON:2621 |  «کالیبر»
14	        #10 (parent #8) [English] refs=None | caliber
15	#11 (parent #0) [Greek] refs=KLN:252 | kau : burning, shining ; kau-casos : (mountains) shining with ice ☞Kreu
16	  #12 (parent #11) [Latin] refs=None | caucasus : a very mountainous area between Caspian and Black seas
17	    #13 (parent #12) [Arabic] refs=None | 
18	      #14 (parent #13) [Persian] refs=MON5:1474 | qafqâz «قفقاز» : Caucasia
19	    #15 (parent #12) [English] refs=KLN:252 | Caucasian
20	#16 (parent #0) [Greek] refs=KLN:253; POK:595 | kauma : burning heat ; holo-kaustos : burnt whole ☞Sol
21	  #17 (parent #16) [Latin] refs=AHD:191,629 | cauma : heat of the day, resting period ; holocaustum : burnt whole
22	    #18 (parent #17) [English] refs=None | calm ; holocaust
23	
```


## [2026-09-06T21:37:37.316Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-283.json",
 "description": "Read source JSON for page 283"
}
```


### [2026-09-06T21:37:37.352Z] TOOL RESULT

```
{
  "pdf_page": 283,
  "book_page": 253,
  "entries": [
    {
      "root": {
        "name": "Kŭ 1, Kĕu 5",
        "lang": "Indo-European",
        "refs": "POK:595",
        "gloss": "to burn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:595; WLD1:376; KLN:223",
          "words": [
            {"translit": "Kalo", "gloss": "to burn, firewood", "script": null},
            {"translit": "kalo-podein", "gloss": "wooden foot, mold", "script": null, "see": ["Ped"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1095",
          "words": [
            {"translit": "kal-pâd", "gloss": "fabrication mold, shape, body", "script": null}
          ],
          "script_extra": null,
          "note": "IEC:1049,1051 derives this word from Avestan \"kehrp: flesh\", from Indo-European root \"Kwrp, Kwerp: shape, form body\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2858; IEC:1047",
          "words": [
            {"translit": "kâlâ", "gloss": "manufactured good, merchandise", "script": "کالا"}
          ],
          "script_extra": null,
          "note": "References not clear on the exact path of derivation",
          "quote": {
            "text": "چو کالا بر فراز عرصه چیدی - عیان تا آخر بازی بدیدی",
            "poet": "Assâr"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1075; MON:2859",
          "words": [
            {"translit": "kâleb", "gloss": "mold, body", "script": "کالب"},
            {"translit": "kâlbod", "gloss": "body", "script": "کالبد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "این من و این من که در این کالب است - هیچ مگو جنبش این قالب است",
            "poet": "Nezâmî"
          }
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": "KLN:223; PLA:215",
          "words": [
            {"translit": "qâlib", "gloss": "mold", "script": null},
            {"translit": "q.l.b", "gloss": "to make, turn around", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:2621; FVA:337",
          "words": [
            {"translit": "qâleb", "gloss": "mold", "script": "قالب"}
          ],
          "script_extra": "قلب ، انقلاب ، منقلب\nمقلوب ، تقلب ، قلاب",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "Italian",
          "refs": "KLN:223",
          "words": [
            {"translit": "calibro", "gloss": "mold, size", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:2621",
          "words": [
            {"translit": null, "gloss": null, "script": "کالیبر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "caliber", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:252",
          "words": [
            {"translit": "kau", "gloss": "burning, shining", "script": null},
            {"translit": "kau-casos", "gloss": "(mountains) shining with ice", "script": null, "see": ["Kreu"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "caucasus", "gloss": "a very mountainous area between Caspian and Black seas", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "MON5:1474",
          "words": [
            {"translit": "qafqâz", "gloss": "Caucasia", "script": "قفقاز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 12,
          "lang": "English",
          "refs": "KLN:252",
          "words": [
            {"translit": "Caucasian", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:253; POK:595",
          "words": [
            {"translit": "kauma", "gloss": "burning heat", "script": null},
            {"translit": "holo-kaustos", "gloss": "burnt whole", "script": null, "see": ["Sol"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Latin",
          "refs": "AHD:191,629",
          "words": [
            {"translit": "cauma", "gloss": "heat of the day, resting period", "script": null},
            {"translit": "holocaustum", "gloss": "burnt whole", "script": null}
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
            {"translit": "calm", "gloss": null, "script": null},
            {"translit": "holocaust", "gloss": null, "script": null}
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


## [2026-09-06T21:37:38.147Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:37:38.191Z] TOOL RESULT

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


## [2026-09-06T21:38:08.653Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','WLD','MON','BQT','PLA','IEC','AHD','FVA','FVQ','SYN','LKT','SKT','LEW','LAT','ARY','PHD','HRN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online metadata"
}
```


## [2026-09-06T21:38:09.493Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kēu-\\|keu-\\|kāu-\\|kau-\" POK_full.txt | head -50",
 "description": "Grep Pokorny for keu root"
}
```


### [2026-09-06T21:38:10.460Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the
```


### [2026-09-06T21:38:10.498Z] TOOL RESULT

```
3249:"hears' as *aK-ou(;- "having sharp ear' here, see, however, 1. keu-; alb. a//7e/e "sharp, 
31761:lemma: (s)keu-2, (s)keua : (s)ku- : to cover, wrap 
32071:*gou-ro-\ besides Germanic *kau-ara-\x\\) Old Norse karrm. "frizzy curl ', kari^ the gust of 
43677:Old High German /7Ji75 "bonnet' etc. (compare keu-2) respective words; Cretan Kucpspov n 
44054:Root / lemma: kau-/-, ku-l- 
44068:References: WP. I 332, WH. I 188 f., Trautmann 122; compare under 2. keu-. 
44083:Root / lemma: kau- 
44293:Root / lemma: kau- kau- 
44315:nud-kaut^s\a)/, kill', /rai/a'blow, knock, layer' {*kau-), Lithuanian /r^/5 "hammer' = Old 
44322:Bulgarian kbznb "shrewdness' ("forge a conspiracy') etc.; Tocharian A ko, B kau- "slay'. 
44330:Root / lemma: kau- keu-, ku- 
44368:kavcaty' screech, shriek, scream, squawk, cackle, croak, yell '; ablaut. {*keu-) Bulgarian 
46660:Root / lemma: keu-1, skeu-, lengthened grade keu- 
46664:Note: heavy basis koua-\ s-extension keu-s-, about forms with aniaut. 5-s. at the end; 
46682:from the basis keu-s-: aKouw "hear' (*aKouqi(jo), aKori, horn. aKoun " ear, hearing ' 
46698:German horfrjen 'hear' (see above); lengthened gradees *keu-\n Old English hawian 
46705:" feel, mark, perceive, hear ', serb. cujem cuti'heax, feel ' (etc.; *keu-)\ 
46707:Old Bulgarian cudo, -ese 'wonder, miracle', cuditi s§' to wonder at, be surprised ' {*keu- 
46721:keu-s-\r\ russ. dial, cuchatb 'percewe, hear', sloven, cuha-m, -//"feel, foresee, predict ', 
46730:show ' {skeu-sRd); 
46749:Root / lemma: keu-2, keua- 
46757:with fsjkeu-' cover' see there. 
46788:B. I. keu-g-: 
46802:B. II. keu-k-: 
46839:C. I. keu-b-: 
46878:(also). Middle High German huste{see above under keu-p-). 
46919:cm. keu-p-: 
46960:German hOfoav\6 appears like this probably rather to belong to keu-b-io (see there); is 
52221:whistle, fizz ' (from *soyl= keu-lo-or kou-lo-)\ Lithuanian 5i/-5/7/rs//" breathe, wheeze, pant, 
74817:See also: s. also (s)k(h)ed-, skei-, sken-, skeu-6. 
76607:maybe from skeu-k-\r\ere as "gehetzf: Germanic *skeuhwa-^ shy' in Old English sceoh, 
76670:See also: s. also under skeu-5 and skeub-. 
76674:Root / lemma: (s)keu-1 
76692:Root / lemma: (s)keu-2, (s)keu9 : (s)ku- 
76756:(s)keu-t-: 
76814:B. guttural extension (s)keu-R-: 
76826:C. 5-extension (s)keu-s-: 
76859:Root / lemma: (s)keu-4 
76863:See also: see above S. 587 f. {(s)keu-4). 
77377:Root / lemma: skeu-3, kseu- 
77403:Root / lemma: skeu-5 
77411:Root / lemma: skeu-6(t-) 
77417:Material: Old Indie skau-ti, skunati, skunot/ ^stori, stobert, stochert', with a- 'zerkleinert 
77818:See also: s. also under skeu-5.
```


## [2026-09-06T21:38:17.447Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 59[0-9]\" POK_full.txt | head -30; echo ---; grep -n \"kau-\\b\" POK_full.txt | head",
 "description": "Find Pokorny page 595 lemma"
}
```


### [2026-09-06T21:38:17.502Z] TOOL RESULT

```
46658:Page(s): 595-596 
47062:Page(s): 596-597 
47323:Page(s): 598 
47335:Page(s): 599 
47349:Page(s): 599 
47361:Page(s): 599 
47394:Page(s): 599 
47591:Page(s): 599-600 
50806:Page(s): 595 
50833:Page(s): 597 
50849:Page(s): 597 
50942:Page(s): 592-594 
50991:Page(s): 594-595 
51115:Page(s): 595 
51133:Page(s): 595 
51187:Page(s): 597 
51242:Page(s): 598 
51269:Page(s): 598 
51283:Page(s): 598 
51295:Page(s): 598 
51308:Page(s): 598 
---
32071:*gou-ro-\ besides Germanic *kau-ara-\x\\) Old Norse karrm. "frizzy curl ', kari^ the gust of 
77417:Material: Old Indie skau-ti, skunati, skunot/ ^stori, stobert, stochert', with a- 'zerkleinert
```


## [2026-09-06T21:38:18.312Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=250 && NR<=252' POK_02.txt | head -120",
 "description": "Print POK_02 leaves around p595"
}
```


### [2026-09-06T21:38:20.374Z] TOOL RESULT

```
hd.  dial.  hoppen  ^hüpfen',  engl,  hobble  , hinken*  (Wissmann  Nom.  postverb. 174f.).
b.  Mit  nicht  aufs  Biegen  des  Körpers  gewendeten  Bedeutungen :
ai.  Jcubra-  n.    ^Höhlung   in    der   Erde,    Grube ;    Ohrring^ ;    gr.  xvßog  .  .  . ndq)ioL  d^  TÖ  tQvßXlov  Hes. ;
[aber  ags.  höpig  ,in  hills  and  hollows',  höp  m.  ,Reifen',  engl,  hoop,  ndl. hoep  jRing,  Reifen^,  aisl.  höp  n.  ,Bucht^  zu  lit.  kabe  ^Haken^  ?] ;
ags.  heap   m.  f.,   as.  höp,    ahd.  houf  , Haufe;    Schar',    mnd.    hupe,   ahd. hüfo,  nhd.  Haufe  (ebenso),  mhd.  huste  (s.  oben  unter  Jceu-p-).
C.  II.  keu-bh-   (einschließlich   von  Worten,    die    bh   oder   b   enthalten können).
Ai.  Jcubhanyü-  etwa  ,sich  drehend,  tanzend';
redupl.  ai.  hakübh-  f.  , Kuppe,  Gipfel',  hakubhd-  ,hervor-,  emporragend' (erst  nach  haküd-  umgebildet?);
im  Auslaut  doppeldeutig  bakhi  (pämird.)  Icubün  ,hölzerne  Trinkschale' ( :  poln.  hubeh  ,Becher',  gr.  yivßoq  ,rQvßXiov^,  nas.  gr.  Kvußog  usw. ;  Uhlen- beck  Ai.  Wb.  59);
gr.  yivcpög  ,gebückt,  gekrümmt',  yivq)og  n.  ,Buckel',  yi{}cpa)  ,biege  vor- wärts, krümme',  wohl  auch  xü/ttw  ,beuge  mich,  ducke  mich',  KVfttög , demütig',  y,vßda  ,geduckt'  (ursprünglicher  Labial  nicht  objektiv  fest- stellbar); 7ivg)SQov  ^  xvcpTjv'  X6q)alriv  KqfjTsg  Hes. ;  vielleicht  aus  der  Sprache nördlicher  (thrak.,  maked.)  Gaukler  stammen  daher  wohl  yivßrj  .-Kscpa^  \ EM.,  '/.vßrjßog  ,ö  xarayivtpag'  EM.,  -avßrjßäv  ,%vqioig  xd  irct  ttjv  yiecpal^v QtTtTSiv'  EM.,  ,von  Raserei  ergriffen  sein'  Hes.  PolL,  sowie  xvßiardo)  - ,schlage  einen  Purzelbaum,  stürze  kopfüber';
zu  einer  der  Labialerweiterungen  in  der  Bed.  von  xvTtr] '  TQwyXrj  u.  dgl.
591
wohl  y,vxp€l7]  ^Kasten,  Kiste;  Bienenzelle;  Ohröffnung^^  xvxpeXog  ,die  in Erdlöchern  nistende  Uferschwalbe* ;
ahd.  hüba,  as.  hüva^  ags.  hüfe,  aisl.  hüfa  , Haube,  Kappe';
russ.  hubarh  , Brummkreisel',  küharerm  , kopfüber',  Jcubec^  , Brummkreisel', huheh  mdartl.  ^hölzerne  Kugel  zum  Spielen',  küboJc^  ,Becher,  Pokal',  klr. Jcub  ,aus  Holz  ausgehöhltes  Geschirr',  JcüboJc  ,Napf,  bauchiges  Gefäß, kleines  Geschirr',  poln.  Icubelc  ,Becher,  Schoppen,  Obertasse'.
C.  III.  keu-p-:
a.  Ai.  Jcüpa-  m.  , Grube,  Höhle';
gr.  :iV7Tr]'  ZQcbyXrj  Hes.  (v?),  xv/rat*  sldög  tl  vewg,  xat  al  i§  i^Xrjg  ytat XOQTOv  olxrjaELg',  xißrtsXXov  , Becher',  xvugog  m.  , Getreidemaß';
lat.  cüpa  f.  ,Kufe,  Tonne',  roman.  auch  , Wanne'  (daneben  gloss.  und roman.  cüppa  ,Becher'  scheint  späte  Kurzform  mit  Konsonantenverdopplung neben  KvnsXlov  zu  sein);  über  Lehnformen  aus  dem  Lat.  und  Rom.  orien- tiert Berneker  645  f. ;
aisl.  hüfr  m.  , Schiffsrumpf',  ags.  hyf  , Bienenstock';  hierher  (oder  zur Wurzelf.  auf  -bk-  oder  -
b-)  wohl  auch  ags.  gehopp  ,folliculus',  hoppe  f. ,bulla,  Kapsel',  mengl.  hoppe  , Samenkapsel  des  Flachses';
allenfalls  slav.  *k^p^,  öech.  Jeep  ,vulva',  poln.  kiep  ,ds.;  Narr,  Tauge- nichts' (Berneker  664  f.  zw.).
b.  Bedeutungsgruppe  ,Wölbung  nach  oben,  Haufe  u.  dgl.':
Apers.  kaufa-  ,Berg',  av.  Jcaofa-  ,ds. ;  Kamelbuckel',  npers.  köh  ,Berg' (setzen  -ph-  voraus);
alb.  (südtosk.)  Jcjipi  ,Haufe'  (*Jcüp-ija) ;  ^
mir.  cüan  f.  , Trupp,  Haufe'  (*koup-na) ;
ahd.  hovar  ,Buckel'  (:  lit.  kuprä),  ags.  hofer  m.  ds.,  ahd.  hubil  ,Hügel', as.  huvil  ds.  (davon  nhd.  hobeln  als  ,die  Unebenheiten  entfernen');  vielleicht ahd.  hüfila,  hiufila  , Wange',  nhd.  Schweiz,  hüfelin  ,unter  den  Augen  liegen- der Teil  der  Wange';  norw.  hov  n.  , Anhöhe,  kleiner  Hügel',  aisl.  hof  n. , Tempel',  ags.  hof  n.  , Gehege,  Haus,  Tempel',  as.  hof,  ahd.  hof  m.  , um- schlossener Raum  beim  Haus,  Hof,  Gut'  (ursprüngl.  von  der  Lage  auf Anhöhen);  mhd.  huste  ,auf  dem  Felde  zusammengestellter  Getreidehaufen, Hauste'  {-Ait.  küpstas)  ]  *hüfsto  ist  ablautgleich  mit  ahd.  hüfo  und  scheint wie  dieses  wohl  eher  zu  keu-b-  zu  gehören  (s.  dort);  wird  auch  mit  russ. kust^  , Busch,  Strauch,  Staude',  klr.  kust  , Strauch,  Staude'  verbunden;
lit.  kaüpas  ,Haufen'  =  abg.  kupz  ds.  (serb.  küp  freilich  mit  anderer Intonation  als  kaüpas  ]  s.  Berneker  646);  lit.  kaupiü,  kaüpti  ,häufeln', kuplüy  küpti  ,auf  einen  Haufen  legen,  ordnen',  kuprä  , Höcker',  küpstas , Hügel',  küpeta  , Heuhaufen',  küpinas  ,gehäuft',  lett.  kupt  ,sich  ballen', kupenis  , Schneehaufen',  kuprs  , Hocker';
592  »
mit  Dehnstufe  *kö[u]p-:  Ut.  Icuopiü,  huöpti  ,häufeln  (Getreide)^,  lett. Jcuops  ,Haufe^,  Jcuopina  ^Garbe';
russ.  (Berneker  646)  Jcup7i>,  hüper  ^Steißbein;  Bürzel^  poln.  huper  ,BurzeI, Hinterer'.
D.  Nasaliert  kum-hh-,  meist  kum-b-:
Ai.  humha-  m.  ^das  dicke  Ende  (eines  Knochens^;  humbha-  m.  ,Topf, Kruo-^;  Du.  _,die  beiden  Erhöhungen  auf  der  Stirn  des  Elefanten'  =  av. xumba-  m.  ,Topf,  Vertiefung',  npers.  xumb,  xum  ,Topf,  Krug'  (diese  mit anlaut.  Tenuis  asp.);
gr.  ytvfMßrj  ^Becken,  Schale^  Kahn'^  KVfxßog,  y,v^ßLOv  ^Gefäß',  ^vfxßalovj meist  PL  ^cymbalum,  Becken'  (nac
h  Banateanu  REtlE.  1,  120  aus  semit. quhbäh-,  Van  Windekens  Lexique  48  vergleicht  toch.  A  kumpäc  , Trommel');
Tiv^ßj]  ;Kopf,  'Avq}r]^  EM.,  Suid.;,  hom.  xvußaxog  ^Spitze  eines  Helmes' (vgl.  yiv(,ißrj),  s.  Leumann  Hom.  Wörter  231  ff.;
lat.  (mit  präsentischer  Nasalierung)  -cumbö  (s.  oben  S.  590);
mir.  comm  , Gefäß',  cummal  , Becher,  Schale',  cymr.  cwmm  ,Tal'  (m.), bret.  komm  ,Trog'  (m.);  aus  urbrit.  *kumbos  stammen  ags.  cumb  ,Tal', engl,  coomb,  combe  , Talmulde',  hingegen  ist  gall.-rom.  cumba  ,Tal,  Trog' Fem.;  aus  dem  Frz.  stammt  bret.  komb  ,Tal';  vgl.  die  unnas.  Gefäßbe- zeichnungen pam.  kubun,  poln.  kubek,  auch  gr.  y,vßog  jTQvßXtov']
aisl.  aptr-huppr,  norw.  mdartl.  hupp  und  hump  ,die  Weichen  beim  Vieh', nhd.  humpeln^  mnd.  humpelen  ,hinken'  und  in  nicht  speziell  auf  das  Biegen des  Körpers  gewendeter  Bed. :
norw.  hump  m.  , Unebenheit,  Knorren  (ndd.  Lw.),  engl,  hump  ,Buckel', ndd.  humpe  f.  , dickes  Stück',  humpel  , niedriger  Erdhügel',  ndl.  homp ,dickes  Stück  Brot';  vielleicht  nhd.  (ndd.)  Humpen  (vgl.  ycvfxßog).
WP.  I  370  ff.,  WH.  1 127,  297  f.,  298,  305,  306,  310  f.,  859,  Trautmann  121  f.
I.  keu-,  keuQ-:  kü-,  kuä-  ,schwellen,  Schwellung,  Wölbung'  und  , Höhlung,
hohl',   gemeinsame   Anschauung  ,Wölbung   nach   außen   oder  innen';
kouo-s     ,hohl',     kou9-ro-s  :  kü-ro-s    ,geschwollen,     stark,     Held',
kouQlo-s  ,hohl,  tief,  kü-nö-s  ,geschwollen',  kuä-nt-  ,g8iJiz%  ku-s-i-s
,Hohlstengel'(?),  kuu^  ,Loch'.
Ai.  §v-dyati  ,schwillt  an,   wird  stark,  mächtig'  (Perf.  sü-§uv-uK)\  su-nd-
^n.  ^Wachstum,    Gedeihen,    Glück,   Heil';    Sävas-  n.  , Stärke,    Heldenkraft',
§dvira-  , stark,  mächtig'  (l  wohl  sekundär  für  i,  so  daß  =  gall.  -Aavaqog),
saviX^Äa- , übermächtigst',  sünd-  ,gesch wollen,  aufgedunsen'  (aisl.  hünn  usw.;
über  ai.  ituna-m  ,Mangel'  s.  Tliieme  KZ.  69,  172 f.);  sünyd-  ,leer'  (und  arm.
sun   ,sehr  gering,   entblößt   von');    snra-    ,kräftig.',    meist    ,Held'    (=    av.
süra-,    gr.    H-WQog    usw.);     §ö-tha-    m.    .Anschwellung,    Aufgedunsenheit',
593
^ö-pha-  m.  , Geschwulst,  Geschwür^ ;  säva-  m.  ,das  Junge  eines  Tieres^, ai.  ^i-su-  m.  ,Kind,  Junges';
§vä-trd-  ^gedeihlich,  kräftigt,  n.  ,Kraft,  Stärkung^;  sd-svant-  ,jeder^, s.  unten ;  von  einer  s-Erweiterung  wahrscheinlich  Susi-  m.  , Höhlung^  (=  ags. hyse  , Jüngling^),  susird-  (aus  Sus-?)  ;hohl^;  n.  , Höhlung,  ein  Blasinstru- ment^ ;
av.  spä{y),  redupl.  Präs.  Partiz.  sispimna-  ^aufschwellen',  süra-  (=  ai
```


## [2026-09-06T21:38:30.827Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '50795,50845p;51105,51145p' POK_full.txt",
 "description": "Print POK_full lines near page 595 entries"
}
```


### [2026-09-06T21:38:30.877Z] TOOL RESULT

```
Meaning: thorn 

Material: Asachs. /7/b/7c» "briar'. Old High German h/ufo ds., Old English heopam., heope 

f., engl. hip, Norwegian hjupa^ rosehip, dog rose '; 

Old Prussian kaaubri^Vc^oxv!. 

Maybe alb. {*Reub-) thumb'thorn' common alb. s- > th-. 

References: WP. I 380 f. 
Page(s): 595 

Root / lemma: Reuk- 

Meaning: to shine, glow 

Material: Old Indie socati, sucyati^ lights, shines, glows, burns, suffers violent pain, 

mourns ', socayat/" kindles, saddens; it is sad, deplores ', soka-rc\. "blaze, glow, flame, 

pain, mourning, grief, si/c/- "luminous, gleaming, pure', sukra-, sukla-^ light, white, pure', 

sukti-t " shell, pearl mussel, mother of pearl, iridescent lining of a mollusk shell ' (if 

"*gleaming'), perhaps sukta- "sour' (if " burning from taste') ; 



Avestan saocint-^ burning ', saocayeitr set on fire, light up, kindle = set in rapid motion, 
urge on, hurry, hasten, accelerate, quicken ', npers. soA-Za/? "kindle, inflame, burn ', 
Avestan upa-suxta-^ kindled ', atrs-saoka-m. ' firebrand ', np. so^ "mourning, grief, 
distress ' (Armenian s^^ "mourning, grief is Iran, loanword); Avestan sovra- "luminous (of 
fire)', np. surx' red'; 

gr. KUKvoq "swan' as "the white'. 

References: WP. I 378. extension from Reu-2. 
Page(s): 597 

Root / lemma: /ceuR- RuR- 

Meaning: to mix, to whirl 

Note: very doubtful. 

Material: Gr. kukewv " mixed drink ', kukqco " stir in, mix in, mix into, mingle', KUKri6pov 

"Rijhrkelle'; 

Lithuanian saukstas "spoon', siuksmes " a rubbing away, sweepings ', siukstus " mixed 
Meaning: to sway 

Material: Latin ceved, -ere "wobble, sway; to agitate one's self, (the figure taken from the 

wagging of the tail of a dog), to fawn, flatter '; 

Old Bulgarian po-kyva-Jg, -//(mainly with glavg) " shake the head, nod ', Czech kyvati 
"wave, beckon, nod, wag, move, shake' (etc.). 

References: WP. I 376. 
Page(s): 595 

Root/ lemma: Reu-2{. Rau- Ru-) 
Meaning: to light, to burn 
Note: Only gr. and Lithuanian 

Material: Gr. Kaiw (Ionian), kqu) (Attic) from *KaF-i(jo "to light, kindle', Aor. hom. £Kr|Fa, Old 
Attic Gen. Sg. keqvtoc; (*Kr|FavT-), New Attic CKauaa, Med. Epic Kr|afjr|v, Pass. £KC(r|v, 
£Kau9r|v, delph. Kr|ua, Guaia', Kpia KaGappara and keTq ds. Hes., hom. Kr|cb5r|<; " smelling 
as of incense, fragrant ' (from a *Kr|Fo(; "blaze, incense '), kqugk;, Kaupa n. "blaze', kqAov " 
dry wood' (*KaF-£Aov), Aeolic KauaA£0(; " burning hot', hom. KriA£0(; {*mFaktoq) etc.; 

Lithuanian kOleti^ become blight-ridden, of corn, grain ', kule^ smut, blight '. (common 
Celtic alb. abbreviation) 

Maybe alb. kule^ hernia '. 

References: WP. I 376 f. 
Page(s): 595 

Root / lemma: Reuero-, Rouero- (also sRuro-1) 



Meaning: north, north wind 

Material: Latin caurus {corns) "northerly wind' {*Rauero-)\ 

Lithuanian siduret "north', siaurysm. "northerly wind'; 

Old Bulgarian severb {*Reuero-) "north';
```


## [2026-09-06T21:38:31.764Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"brennen\\|anzünden\" POK_full.txt | sed -n '1,80p' | grep -n \"\" | head -80",
 "description": "Grep Pokorny burn lemmas"
}
```


### [2026-09-06T21:38:31.824Z] TOOL RESULT

```
1:12580:b'^re-n-u- {present wib nasal infix, compare Modern High German brennen) with 
2:45290:Material: Old Indie karjksati^ longs for' (' brennend verlangen '), /r5/ra/e(Dhatup.) " covets, 
3:73630:Sengen', sungen, s^/7/re/7'anbrennen', sungein, sunkeln^ rustle ', Norwegian dial, sengra, 
4:78512:black', kir. prysmafyty 'anbrennen'. 
5:81662:Auseinanderstochern the brennenden Scheite); 
6:83926:verschwenden{\Nas\.e] dial. " through Verbrennen of Grases urbar machen', Old High
```


## [2026-09-06T21:38:46.004Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN caliber ===\"; grep -n -i \"calibre\\|caliber\\|kalopod\\|qalib\\|qālib\" KLN_1966.txt | head -20; echo \"=== KLN 1971 ===\"; grep -n -i \"kalopod\\|calibre\" KLN_1971.txt | head -20",
 "description": "Grep Klein for caliber"
}
```


### [2026-09-06T21:38:46.071Z] TOOL RESULT

```
=== KLN caliber ===
6183:Derivative:  Caliban-ism,  n. caliber,  calibre,  n.,  the  diameter  of  the  bore  of  a gun.  —  F.  calibre,  fr.  It.  calibro,  fr.  Arab,  qdlib, ‘mold,  model’,  fr.  Gk.  xxXo ttoSlov,  ‘shoemaker’s last’,  dimin.  of  xxXomiuc,  gen.  x5X6jro8o?,  of s.m.,  lit.  ‘a  foot  of  wood’,  fr.  xxXov,  ‘wood’,  esp. ‘wood  for  burning’,  and  -064,  gen.  720864,  ‘foot’, Gk.  xiXov  is  contracted  fr.  *xaf-sXn-v  or  *xAF- aXo-v,  a  derivative  of  xaietv  (for  *xAfiav),  ‘to bum’;  see  caustic.  For  the  second  element  see foot  and  cp.  -pod.  Gk.  xAXo7t68lov  came  into Arabic  through  the  medium  of  the  Aramaic, calibrate,  tr.  v.,  to  determine  the  caliber  of.  — A  hybrid  coined  fr.  caliber  and  -ate,  a  suff.  of Latin  origin.
6192:caliper,  calliper,  n.  —  Variant  spellings  of caliber.  Derivatives:  cal(l)iper ,  tr.  and  intr.  v., cal(l)iper-er ,  n.
6855:Derivative:  causeway,  tr.  v, causey,  n.,  a  causeway  (dial.)  —  ME.  cauce,  fr. ONF.  cauciee,  corresponding  to  F.  chaussee, ‘causeway’,  fr.  VL.  (via)  calctata,  lit.  ‘a  road paved  with  limestone’,  fern.  pp.  of  calciare,  ‘to pave  with  limestone’,  fr.  L.  calx,  gen.  calcis, ‘lime, limestone’.  See  calcareous  and  cp.  chaussee. caustic,  adj.,  burning,  corrosive.  —  F.  caustique, fr.  L.  causticus,  fr.  Gk.  xookttixoc,  ‘capable  of burning,  corrosive’,  fr.  xxocrro?,  ‘burnt’,  verbal adj.  of  xcciEiv,  which  stands  for  *xif-ts'.v,  ‘to burn,  set  on  fire’,  fr.  I.-E.  base  *keu-,  *kii-,  ‘to burn,  heat’,  whence  also  Lith.  kttle,  ‘blight,  mil¬ dew',  kiileti,  ‘to  become  blighted’.  Cp.  caeoma, caliber,  calm,  catacaustic,  Caucasian,  cautery, diacaustic,  encaustic,  holocaust,  hypocaust,  ink, Nausicaa.
15110:foot,  n.  —  ME.  fat,  fr.  OE.  fat,  rel.  to  OS.  fat, ON.  fa tr,  Swed.  fat,  Dan.  fad,  Du.  voet,  OHG. fuo3,  MHG.  VU03,  G.  Fuji,  Goth./o/u.s,  ‘foot’,  and cogn.  with  Ol.  pit,  acc.  pidam,  ‘foot’,  Avestic pad-,  ‘foot’,  Toch.  A  pe,  B  pai,  ‘foot’,  A  pent,  B paine,  ‘both  feet’.  Arm.  ot-n,  ‘foot’,  ot-k\  ‘feet’. Dor.  Gk.  7rtii ;,  Att.  7101)9  (formed  on  analogy  of 009,  ‘ear’),  gen.  770809,  L.  pes,  gen.  pedis,  ‘foot’, Ol.  paddm,  ‘step,  track’.  Arm.  het,  gen.  he  toy, ‘track,  footmark’,  Gk.  rtiSt),  ‘fetter’,  TreSav,  ‘to bind  with  fetters’,  7t£Sov,  ‘ground,  earth’,  h.peda, ‘footstep \pedica,  ‘shackle,  fetter’,  impedire,  ‘en¬ tangle,  ensnare’,  expedire,  ‘to  extricate,  disen¬ gage’,  Lith.  peda,  ‘footstep,  trace’,  OSlav.  podii, ‘loft’,  Russ,  pod-oshva,  ‘sole  of  foot’.  All  these words  derive  fr.  I.-E.  base  *pdd-,  *pid-,  ‘foot’. Cp.  fetch,  fetlock,  fetter,  fit,  ‘part  of  a  song’.  Cp. also  antipodes,  apod,  babouche,  biped,  breviped, caliber,  cap-a-pie,  charpoy,  expedient,  expedite, impeach,  impede,  impedimenta.  Lycopodium, millepede,  multiped(e),  octopus,  oppidan,  palmi¬ ped,  pawn  (in  chess),  parallelepiped,  pajama, pedal,  pedate,  -pede,  pedesis,  pedestal,  Pedetes, pedicel,  pedicle,  pedigree,  pedology,  ‘the  study  of soils’,  peduncle,  peon,  pes,  petiole,  pew,  Peziza, pie,  ‘a  small  coin’,  piepoudre,  pilot,  podagra, podal,  podium,  podo-,  pug,  ‘footprint’,  puy,  seer- paw,  Taliped,  Tarsipes,  teapoy,  trapezium,  triped, tripos,  vamp,  ‘front  part  of  the  foot’,  velocipede. Cp.  also  pejorative,  pessimism.
=== KLN 1971 ===
37310:caliber, calibre, n., the diameter of the bore of a 
37311:gun. — F. calibre, fr. It. calibro, fr. Arab, qdlib,
```


## [2026-09-06T21:38:47.400Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN caucas ===\"; grep -n -i \"caucas\" KLN_1966.txt | head -20; echo \"=== KLN cauma/calm/holocaust ===\"; grep -n -i \"^.*holocaust\\|cauma\" KLN_1966.txt | head -20",
 "description": "Grep Klein caucasian/calm/holocaust"
}
```


### [2026-09-06T21:38:47.503Z] TOOL RESULT

```
=== KLN caucas ===
6830:Caucasian,  adj.  and  n.  —  Formed  with  suff.  -ian fr.  L.  Caucasus,  fr.  Gk.  Kauxaau;,  fr.  Scythian Kpoo-xxcu.?,  ‘Caucasus’,  a  compound  meaning lit.  ‘(the  mountain)  shining  with  ice’;  see  Walde- Hofmann,  LEW.,  I,  pp.  295-96,  s.v.  criista.  The first  element  of  this  compound  is  a  derivative  of I.-E.  base  *qreu-,  ‘to  be  icy’.  For  derivatives  of *qrus-,  an  enlarged  form  of  base  *qreu-  see crust,  crystal.  The  second  element  is  rel.  to  Gk. y.odsiv  (for  "xifieiv),  ‘to  burn’ ;  see  caustic, cauchemar,  n.,  incubus.  —  F.,  a  hybrid  coined from  the  blend  of  OF.  chaucer  and  Picard  cau- quer,  ‘to  trample’  (both  derived  fr.  L.  calcare, of  s.m.,  fr.  calx,  gen.  calcis,' heel'),  and  fr.  MDu. marc,  incubus'.  See  Calceolaria  and  mare,  ‘in¬ cubus',  and  cp.  the  first  element  in  caltrop, caucus,  n.,  private  meeting  of  the  leaders  of  a  poli¬ tical  party.  —  A  word  of  Algonquian  origin,  lit. meaning  ‘counselor’.
6855:Derivative:  causeway,  tr.  v, causey,  n.,  a  causeway  (dial.)  —  ME.  cauce,  fr. ONF.  cauciee,  corresponding  to  F.  chaussee, ‘causeway’,  fr.  VL.  (via)  calctata,  lit.  ‘a  road paved  with  limestone’,  fern.  pp.  of  calciare,  ‘to pave  with  limestone’,  fr.  L.  calx,  gen.  calcis, ‘lime, limestone’.  See  calcareous  and  cp.  chaussee. caustic,  adj.,  burning,  corrosive.  —  F.  caustique, fr.  L.  causticus,  fr.  Gk.  xookttixoc,  ‘capable  of burning,  corrosive’,  fr.  xxocrro?,  ‘burnt’,  verbal adj.  of  xcciEiv,  which  stands  for  *xif-ts'.v,  ‘to burn,  set  on  fire’,  fr.  I.-E.  base  *keu-,  *kii-,  ‘to burn,  heat’,  whence  also  Lith.  kttle,  ‘blight,  mil¬ dew',  kiileti,  ‘to  become  blighted’.  Cp.  caeoma, caliber,  calm,  catacaustic,  Caucasian,  cautery, diacaustic,  encaustic,  holocaust,  hypocaust,  ink, Nausicaa.
9800:crust,  n.  —  ME.,  fr.  OF.  crouste  (F.  croute),  fr. L.  crusta,  ‘the  hard  surface  of  a  body,  rind, crust,  shell’,  which  stands  for  *crus-ta,  and  lit. means  ‘that  which  has  been  hardened  by  freez¬ ing’,  and  is  cogn.  with  Gk.  xpuop  (prob.  for *xp')aoc),  ‘icy  cold,  frost’,  xpusp6c;,  ‘icy,  chilling’, xpu(i6?  (for  *xpua|i6c),  ‘frost’,  xpiiaraXXop,  ‘ice, crystal’,  Toch.  A  kuras,  B  krost,  ’cold’,  Lett. kruvesis,  ‘mud  frozen  in  the  field;  roughness  of the  soil’,  Lith.  at-krusti,  ‘to  revive’  (said  of frozen  people),  OHG.  (h)rosa,  (h)roso,  ‘ice,  crust’, ON.  hriosa,  ‘to  shudder’,  OE.  hruse,  ‘earth, ground’.  All  these  words  derive  fr.  I.-E.  *qreus-, *qrus-,  *qruwes-,  enlarged  forms  of  base  *qreu-, ‘icy,  solid,  coagulated,  congealed’,  whence  also L.  crudus,  ‘raw’.  See  crude  and  cp.  Crustacea, encrust.  Cp.  also  crouton,  crystal,  custard  and the  first  element  in  Caucasian.
16042:Georgian,  adj.,  pertaining  to  the  country  of  Geor¬ gia  in  the  Caucasus.  —  Formed  fr.  Georgia with  suff.  -an.
18568:Iberia,  n.,  the  ancient  name  of  the  Spanish  pen¬ insula.  —  L.  Hiberia,  Iberia,  ‘Spain’,  prop, ‘country  of  the  Hiberes  or  Iberes’,  fr.  Gk. "I^pec/the  Spaniards’,  also  name  of  an  ancient Asiatic  people  near  the  Caucasus.  Cp.  next word.
23363:Melanochroi,  n.  pi.,  members  of  the  Caucasian race  having  black  hair  and  pale  complexion.  — ModL.,  lit.  ‘black  and  pale’,  compounded  of melan-  and  Gk.  ro^pO?,  ‘pale’.  See  ocher  and  cp. Xantochroi.
24913:nail,  n.,  1)  the  horny  substance  on  the  ends  of  the fingers  and  toes;  2)  a  small  spike  of  metal  or wood.  —  ME.  naile,  neil,  fr.  OE.  nsegl,  ntegel, ‘fingernail;  metal  nail,  peg’,  rel.  to  OS.,  OHG. nagal,  OFris.  neil,  MDu.  naghel,  Du.,  MHG., G.  nagel,  ‘fingernail;  metal  nail’,  ON.  nagl,  ‘fin¬ gernail’,  nagli,  ‘metal  nail’,  Goth,  ganagljan,  ‘to nail’,  fr.  I.-E.  base  *nogho-.  *ngho-,  *ongho-, ‘nail’,  whence  also  OI.  ahghrih,  amhrih,  ‘foot’, Gk.  ovu^,  L.  unguis,  ‘nail,  claw’,  OSlav.  noga, Russ,  noga,  Czech  and  Slovak  noha,  ‘foot’,  Lith. naga,  ‘hoof’,  ndgas,  Lett,  nags,  ‘nail’,  OPruss. nage,  ‘foot’,  OSlav.  nogiiri,  ‘nail,  claw’,  Lith. nagiitis,  OPruss.  nagutis,  ‘fingernail’,  OIr.  ingen, OW.  eguin,  W.,  Co.,  ewin,  Bret,  twin,  ‘nail,  claw’. Cp.  OI.  nakhdft,  Pers.  naxun,  ‘nail,  claw’,  where qh-  (for  gh-)  is  prob.  due  to  Caucasian  influence. —  Cp.  agnail.  Cp.  also  onyx,  ungual. Derivatives:  nail,  v.  (q.v.),  nail-less,  adj.
38644:terebra,  n.,  1)  borer;  2)  ovipositor  of  certain  in¬ sects  ( entomol .)  —  L.  terebra,  borer,  drill,  auger  , formed  fr.  terere,  ‘to  rub,  grind,  wear  away’, with  instrumental  suff.  -bra.  See  throw  and  cp. words  there  referred  to.  Cp.  also  Terebella. terebrate,  tr.  v.,  to  perforate.  —  L.  terebratus,  pp. of  terebrare,  ‘to  bore,  pierce,  perforate’,  fr.  tere¬ bra.  See  prec.  word  and  verbal  suff.  -ate. teredo,  n.,  shipworm.  —  L.  teredo,  ‘a  worm  that gnaws  wood’,  fr.  Gk.  xspTjScov,  lit.  ‘a  boring worm’,  from  the  base  of  -relpetv,  ‘to  rub’,  tege- xpov,  ‘borer’.  See  throw  and  cp.  terebra. terek,  n.,  a  sandpiper  ( Terekia  cinerea)  —  Named after  the  river  Terek  in  the  Caucasus.
=== KLN cauma/calm/holocaust ===
6855:Derivative:  causeway,  tr.  v, causey,  n.,  a  causeway  (dial.)  —  ME.  cauce,  fr. ONF.  cauciee,  corresponding  to  F.  chaussee, ‘causeway’,  fr.  VL.  (via)  calctata,  lit.  ‘a  road paved  with  limestone’,  fern.  pp.  of  calciare,  ‘to pave  with  limestone’,  fr.  L.  calx,  gen.  calcis, ‘lime, limestone’.  See  calcareous  and  cp.  chaussee. caustic,  adj.,  burning,  corrosive.  —  F.  caustique, fr.  L.  causticus,  fr.  Gk.  xookttixoc,  ‘capable  of burning,  corrosive’,  fr.  xxocrro?,  ‘burnt’,  verbal adj.  of  xcciEiv,  which  stands  for  *xif-ts'.v,  ‘to burn,  set  on  fire’,  fr.  I.-E.  base  *keu-,  *kii-,  ‘to burn,  heat’,  whence  also  Lith.  kttle,  ‘blight,  mil¬ dew',  kiileti,  ‘to  become  blighted’.  Cp.  caeoma, caliber,  calm,  catacaustic,  Caucasian,  cautery, diacaustic,  encaustic,  holocaust,  hypocaust,  ink, Nausicaa.
7514:chololith,  n.,  a  gallstone.  —  Compounded  of cholo-  and  Gk.  Xiftog,  ‘stone’.  See  -lith. Derivative:  chololith-ic,  adj. chomage,  n.,  stoppage,  cessation  from  work.  — F.,  fr.  chomer,  ‘to  cease  from  work’,  fr.  Late L.  caumare,  fr.  cauma,  ‘tranquillity’.  See  calm and  -age.
17952:holocaust,  n.,  1)  a  burnt  offering;  2)  complete destruction  by  fire;  3)  a  great  destruction.  — - F.  holocauste,  fr.  L.  holocaustum,  fr.  Gk.  6X6- xauoxov,  lit.  ‘a  thing  wholly  burnt’,  neut.  of  the adj.  6X6x0010x04,  which  is  compounded  of  8X0?, ‘whole’  (see  holo-),  and  xouctt6 4,  verbal  adj.  of xodciv  (for  *xifiEiv),  ‘to  bum’.  See  caustic. Derivatives:  holocaust-al,  holocaust-ic,  adjs. holograph,  n.,  a  document  written  entirely  by  the person  from  whom  it  proceeds.  —  Late  L.  holo¬ graphs  (whence  also  F.  holographe),  fr.  Gk. oXdypocqiop,  ‘written  in  full,  written  entirely  by the  same  hand’,  which  is  compounded  of  6X04, ‘whole’  (see  holo-),  and  -ypatpo;,  fr.  Ypa<peiv,  ‘to write’.  See  -graph.
```


## [2026-09-06T21:38:54.014Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor ln in [6183,6830,6855,17952]:\n    pre='\\n'.join(lines[:ln])\n    print(ln, 'leaf(0-based ff count)=', pre.count('\\f'))\nEOF\necho \"=== calm ===\"; grep -n \"^calm,\" KLN_1966.txt | head; grep -n \"calm,  adj\\|calm,  n\" KLN_1966.txt | head",
 "description": "Compute Klein leaf numbers"
}
```


### [2026-09-06T21:38:55.819Z] TOOL RESULT

```
6183 leaf(0-based ff count)= 129
6830 leaf(0-based ff count)= 143
6855 leaf(0-based ff count)= 144
17952 leaf(0-based ff count)= 397
=== calm ===
6221:calm,  n.  —  F.  calme,  ‘tranquil,  quiet’,  fr.  It.  cal- ma,  ‘absence  of  wind,  tranquillity’,  fr.  Gk.  xau- p.a,  ‘burning  heat  of  the  sun’,  whence  arose  the meaning  ‘tranquillity  of  the  sea  during  oppres¬ sive  heat’.  Gk.  xaupa  derives  fr.  *xaf-,  the  stem of  xaleiv,  ‘to  burn'.  See  caustic  and  cp.  words, there  referred  to.  Cp.  also  chomage.
6221:calm,  n.  —  F.  calme,  ‘tranquil,  quiet’,  fr.  It.  cal- ma,  ‘absence  of  wind,  tranquillity’,  fr.  Gk.  xau- p.a,  ‘burning  heat  of  the  sun’,  whence  arose  the meaning  ‘tranquillity  of  the  sea  during  oppres¬ sive  heat’.  Gk.  xaupa  derives  fr.  *xaf-,  the  stem of  xaleiv,  ‘to  burn'.  See  caustic  and  cp.  words, there  referred  to.  Cp.  also  chomage.
6222:Derivatives:  calm,  adj.  and  v.,  calm-er,  n.,  calm¬ ly,  adv.,  calm-ness,  n.
```


## [2026-09-06T21:38:59.699Z] TOOL CALL #14: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));import sys\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "Print KLN and BQT offsets"
}
```


### [2026-09-06T21:39:01.226Z] TOOL RESULT

```
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
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
  "/home/sfmqrb/git/rishe/data/
```


## [2026-09-06T21:39:12.523Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (128,129,143,144,397):\n    L=leaves[i]\n    print('--- leaf',i,'---')\n    print(L[:200].replace('\\n',' | '))\n    print('...tail:', L[-200:].replace('\\n',' | '))\nEOF",
 "description": "Inspect Klein leaf headers for page numbers"
}
```


### [2026-09-06T21:39:14.298Z] TOOL RESULT

```
--- leaf 128 ---
ia and  adj.  suff.  -ate  and  cp.  discalceate. | calced | calccd,  adj.,  calceate.  —  Formed  with  stiff,  -ed fr.  L.  calceus ,  ‘shoe’.  See  next  word. | Calceolaria,  n.,  a  genus  of  plants  
...tail: ,  gen.  720864,  ‘foot’, Gk.  xiXov  is  contracted  fr.  *xaf-sXn-v  or  *xAF- aXo-v,  a  derivative  of  xaietv  (for  *xAfiav),  ‘to bum’;  see  caustic.  For  the  second  element  see foot  and 
--- leaf 129 ---
 cp.  -pod.  Gk.  xAXo7t68lov  came  into Arabic  through  the  medium  of  the  Aramaic, calibrate,  tr.  v.,  to  determine  the  caliber  of.  — A  hybrid  coined  fr.  caliber  and  -ate,  a  suff
...tail: calomel,  n.,  mercurous  chloride,  HgCl  (chem.)  — F.,  prop,  ‘beautiful  (i.e.  white)  substance  de¬ rived  from  black',  fr.  Gk.  xaXop,  ‘beautiful,  fair  , and  puXx S,  ‘black’.  See  ca
--- leaf 143 ---
,  ‘to  rob’). | Derivative:  caterpillar,  intr.  v. caterwaul,  intr.  v.  —  ME.  caterwrawen,  cater- wawen,  fr.  LG.  katerwaulen,  ‘to  cry  like  cats’, fr.  kater,  ‘male  cat’,  and  wauten,  
...tail: ing,  stormy’,  OSlav. severu,  'north  wind’,  Goth,  skura  ( windis ), ‘storm’,  OE.  scur,  ‘shower’.  See  shower, causalgia,  n.,  a  burning  sensation  (tried.)  —  Medi¬ cal  L.,  lit.  ‘a  b
--- leaf 144 ---
urning  pain’,  coined  by  the  Ameri¬ can  physician  Silas  Weir  Mitchell  (1829-1914) fr.  Gk.  ‘burning  heat’  (which  derives  fr. | *xx~-,  the  stem  of  xxtsiv,  ‘to  burn’),  and  iXfoc, pai
...tail:   the  solar  disk  ( astrol .)  — - Arab .jismjesm,  ‘body’,  in  the  term  ‘ala jismi'sh- shamsi,  ‘on  the  disk  of  the  sun’.  Sec  Devic’s Supplement  to  Littre’s  Dictionary,  p.  13. | -ce,  
--- leaf 397 ---
  holen,  ‘holly’.  See holly. | holo-,  before  a  vowel  hoi-,  combining  form  mean¬ ing  ‘whole,  entire,  complete’.  — ■  Gk.  0X0-,  6X-, fr.  8X0?,  ‘whole,  entire’,  which  stands  for *8Xfo<
...tail: ,  fr.  cae¬ dere,  ‘to  kill’.  See  human  and  -cide,  ‘killing’, homiletic,  adj.,  pertaining  to  sermons  or  homi¬ letics.  —  Gk.  opiTX-rjTixop,  ‘conversable’,  fr. 6puX7)To<;,  verbal  adj
```


## [2026-09-06T21:40:00.139Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD kalbod ===\"; grep -n -i \"kalbod\\|kalbad\\|kālbad\\|kālbod\\|klpwt\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"kalbad\\|kalbod\" NYB_vol2_glossary.txt | head -10; echo \"=== HRN ===\"; grep -n -i \"kalbud\\|kālbud\\|kalbad\\|kālbad\" HRN.txt HUB.txt | head -20",
 "description": "Grep Pahlavi dictionaries for kalbod"
}
```


### [2026-09-06T21:40:00.215Z] TOOL RESULT

```
=== PHD kalbod ===
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:1036:body kālbod, kirb, tan.
PHD.txt:2010:form (n.) brahm(ag), čihr, dēs(ag), éwén(ag), gēn(ag), jadag, kālbod, kirb; of the same — hamdēsag.
PHD.txt:3616:shape čihr, kālbod.
PHD.txt:5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
PHD_mackenzie.txt:3154:kalbod [k)lpwt ' I (M k)lbyd), N ~] body, shape, form.
PHD_mackenzie.txt:6074:bestowal baxsisn.                           body kalbod, kirh, tan.
PHD_mackenzie.txt:9702::!kay                                    ..tg   kalbod                    \lDl~~
=== NYB ===
2168:kālpa6 [k*lpt'], kalpu& [k’Ipwt'] shape, external bodily form 892%, 9026, 10127, — MPrs k’lbyd (List 84); Paz. kälbud, Skr. v. kaya sundara (Aog.); NP kalbad, kälbud ‘the body of a man or an animal’, ‘a model, a last for shoes" which is the original sense, the w. being borrowed from Gr xadronddtov..
=== HRN ===
HUB.txt:6282:LW. kathad, kalbud *Modeir, paz. kaibud, -phi, kalput^ kalpat,
HUB.txt:9471:*Kohr = gr. x()diu(it] ; kdlbad, kalbud *Modeir, phi. kolput =
```


## [2026-09-06T21:40:02.501Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC 1047-1051 ===\"; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor p in (1047,1049,1051):\n    leaf=p//2+15\n    print('=== printed',p,'leaf',leaf,'===')\n    print(leaves[leaf][:1500])\nEOF",
 "description": "Print Mann IEC pages 1047-1051"
}
```


### [2026-09-06T21:40:05.248Z] TOOL RESULT

```
=== IEC 1047-1051 ===
858
=== printed 1047 leaf 538 ===
nd com. Gmc.)
pnt- (pnts-) ‘go, track; passage, way’. Cf. pent-, pont-. WP II, 26 Skt. cf. patháh, gen.sg. of pánthah, m. ‘way’; Av. paða-, id.; Ober, paði- f. id.; Oss. cf. fätäg (Cleader" Here: Abaev); Gk. pátos, m. ‘path’; cf. patéo, v. ‘tread, walk’; MIr. éiss, s. (Cpath', fr. *pnts-) beside étaim, v. “find”; éit, f. (“herd?. Background ambig.); OHG cf. funs, OS. OE fus, adj. “eager, ready’; R cf. o-pjàt', Cz. z-pét, adv. ‘back’; Cz. pata, f. ‘heel’; OPr. pintis ‘path, track’; Finn. LW (here?) pato “dam, weir’
putrom Du. vonder, m., Fris. fonder, m. ‘footbridge, bridge of planks’; OCS petro, n. (‘ceiling’, esp. ‘coffered ceiling’); Pol. pietro, Cz. patro ‘storey’
(po, aphetic form of apo and upo, q.v. Arm. v-; Arcad. Cypr. po-; OCS po, po-; Li. pa-; Latv. pa, pa-. Prob. also in Lat. synthetic cpds. as follow, but ambiguously *po- or *pod-, since WSP -d is lost in pro-pe for *pro- ped ‘near’, but not in apud, for *ad-pod, id. OLat. poplicod: publico, etc. Cf. pono fr. *po(d)-sino): *pons ‘decree’ in the cpd. ponti- fex, cf. G Gesetz, and E law for the sense; pudeo "am ashamed’, fr. *po(d)-uidejo, cf. R
969
po-zor ‘disgrace’ for the sense; po-moerium, n. “space round city wall, moat’; and perh. paene, if for *po-jó-ne or *po-jà-ne ‘nearly’, cf. Li. kuo-ne, id. forsense. Cf. also WH:LEW on polio, porceo & po-lübrum)
(pó- radical ‘drink’, see pótos, in Gk. pó-ma, n. (2) ‘beverage’; Cz. na-pájet, inf. "water — animals")
pod-, pód- radical: “foot: ground, base’. See ped-, pods 
=== printed 1049 leaf 539 ===
r, slab’ beside Cz. půda, f. “ground”; Li. pádas, m. ‘sole of foot’; pádis, gs: padio, m. ‘base’ (Li. pádas also “bottom, floor of hearth, threshing-floor' under infl. of Russian); Latv. pads, m. ‘clay floor
poi (?) "at Gk. (Arg. Phoc. Locr.) poi, id.; Alb. pe ‘from, to’; Latv. pie, px. pie-, prp. “aP
poigh- “mark; marked, motley, doomed'. Cf. poiK-, peigh, peiK- Umb. cf. peia-, peiu, adj. “a colour’; cf. Lat. pio, are, v. (2) ‘defile’; OHG feigi; Du. veeg; OE fag, adj. ‘motley, gay’ beside fæge “marked, doomed, fey’; OCS pégü, adj. ‘motley’; R pégij, id.; Srb. pjega, Cz. piha, f. ‘freckle’; Li. cf. piegma, f. id. ON feigr ‘fated’; Sw. feg ‘cow- ardly, (as OHG and Du.) display extn. of sense “marked?” > ‘doomed’.
poikos (?) ‘trivial, diminutive’ LLat. cf. *piculus (implied in It. piccolo "Dt. tle’); G fee, adj. ‘meek, shy, modest’; cf. Icel. peiminn, id. (if fr. *poikmen-); Li. paikas ‘silly’. (Finn. poika “boy? and poju, id., LW in Sw. pojke, id. unrelated)
poikeið ‘paint, decorate’. See next and poi- Kos, and cf. peik- (pik-) OPer. cf. a-paišam 'I have written’; Tokh. B paik- ‘write’; MHG vehen, wv. tr. & intr. (1) ‘decorate, colour; become coloured"; Li. pai- šau, -yti, v. ‘draw, sketch"
poiKolos (poikKilos) “painted, bright, gay, motley’. See next Skt. peSaláh, adj. ‘decorated’; Gk. poikilós, adj. ‘variegated’
poiKos, om (1) “mark, paint, drawing, writ- ing; marked, decorated’. WP II, 9. Cf. poikeio,
971
peik- (pik) and next Skt. pé$ah, m. 'ornament'; Av. paešō, m. id. (a
=== printed 1051 leaf 540 ===
king; drink’. Cf pt-, etc. Skt. páyas, n. “fluid, sap, juice, milk’ beside peyah, adj. & s. ‘drinkable; drink’; payam, pt. (while drinking: (radical of) OCS na-paj-ati, v. ‘give to drink’); Av. payo, m. ‘pasture’ be- side payas, -áh-, n. ‘milk’; Gk. cf. poi-mandría *milk-pail'; Cz. cf. ná-poj, m. ‘beverage’
poksos, is, ios, üs ^wing, side, flank, wall, partition, pigeon-hole'. WP II, 3 Skt. paksáb, m. “wing, side, half, party’; Oss. faxs, pl. fäxstä ‘side’ beside fáxs ‘strip, board’; Gk. puxís, gs: -idos, f. (box. Vocalism as nüx, see noktis above); Myc. cf. pukso(1) (parts of a table, perh. *drawers, flaps"); Latv. paksis, pl "nterlocking beams, tenon-and-mortise joint, corner of box, side’. Cf. also OE fzes, n. ‘border’; Swiss Fácke, f. ‘wing’. Long-gde in R pax, Cz. pach, m. ‘groin’; Cz. also pachy “loose sleeves’; Ukr. paxa, f. ‘armpit’; Blg. pàxove, pl. (^waist': Skt. pāksah “of half, side or party’: Oss. faxs ‘side’)
poKos, us (poKmos, poktos) ‘fleece, wool, hair; (combed, kempt)'. WP II, 16, Cf. peko Per. pa$m *^wool'; Oss. fásm, id. beside fasín, v. ‘comb’; Arm. asr, gs. & ab. s. asu ‘fleece’; Gk. pókos, m. id., cf. pó-gon, -gonos ('kempt chin”, hence ‘beard’, or fr. aphetic *(a)po-8on- 2); OHG fahs, sn. ‘hair; MHG vahs, sm. & sn. id.; OE feax, n. ‘hair of the head’; ON fax, n. ‘mane’; Du. cf. vacht, f. ‘fleece’; Li. cf. pá$ymas, m. ‘combing, carding’; pašaŭ, -ýti, v. ‘comb, card’
pol- (1) ‘much, many; abundance’. Cf. po- luos (polu), pelu (1), peluð (1) & (2), plë-,
```


## [2026-09-06T21:40:28.614Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC kwerp ===\"; grep -n \"kwerp\\|kwrp\\|kerp-\\|kehrp\\|karp-\" IEC.txt | head -20; echo; echo \"=== IEC kal- ===\"; grep -n \"^kal\\|kālā\\|kala-\" IEC.txt | head -20",
 "description": "Grep Mann for kwerp and kal"
}
```


### [2026-09-06T21:40:28.672Z] TOOL RESULT

```
=== IEC kwerp ===
5018:ghrbh- ‘seize’ (?) Cf. gurbh-, and cf. WP I, 595 Vedic grbhnami; cf. Skt. grbhab ‘handle’; Per. inf. giriftan, beside girav ‘pledge’; Hitt. karp (mi) “take, lift, complete'. Ambig. cf. karp-. A parallel form karap- 1sg. karaphi = *devour
7032:A variant arises in Skt. Sardhah *troop") kerep-, kerop- see kerp-
7049:kerp-, kerep- (korp-, korop-; kereps-) 'skull, tile, pan, ladle, bowl, potsherd’ Skt. cf. karparah ‘skull, potsherd’; Arm. Serep, i-st ‘ladle? beside karapn & karap, gs. karapin ‘skull’; Ligurian substr. in Rumansch (?) creppa ‘skull’; OCS érépü (tile, also **ladle' in view of Crépiti, v. ‘draw water); R cérep ‘skull’; Cerepók, dim. ‘potsherd’; Cz. střep, id.; z-gde in OCS Crüpljo, érüpati ‘draw water’;
7697:korops-, korpor-, cf. kerp- (kerep-) and krp- Skt. cf. karparah ‘skull, tortoise-shell; cup, bowl; Arm. karap and karapn, gs karapin ‘skull
7702:korpos, å ‘cut, cutter; cutting, sharp; spike, point, crag’. Cf. kerp-, krp- Skt. (ambig.) cf. karparah (‘pot, sherd’. Cf. kerep-); Alb. karpë ‘rock, cliff; LW in Big. kàrpa, id.; Ligurian substr. in Rumansh crap, m. (‘boulder’, w. metath, as in cravun *carbonem', crapenda 'carpenta"); LW (?) in Alb. krep (‘crag’, as doublet of karpë?). Cf. WP II, 581. Here also prob. Ir. corr ‘peak, tip, corner, snout, bill, corn on foot"; W cor, pl. od m. (1) ‘point’; ON herfi ‘harrow’; Sw. harv, f. id. beside hárv, pl. -ar, f. ‘rake’; cf. EMSw. härvel ‘buckle’; Blg. krap, adi ‘short’; Li. karpas ‘cutting, clearing’; karpà ‘slice’; kárpa ‘wart; Latv. kārpa, id.
7704:(korp-, korop-, see kerp-, kerep-)
8112:krpiios (krpios, io, krpitio) 'foot-wrapping, clout, shoe’. WP I, 425. (Loanword movement had distorted some of the expected phono- logy) (1) cf. Gk. karpaía (a Thessalonian dance); krēpís (shoe'. LW in Lat. crepida “sandal”, via Etrusc.); LLat. carpia lint? beside *scarpa in It. ‘shoe’; LW in W carp, pl. iau, m. ‘clout, rag’; Ir. cf. caire-amh, m. ‘shoemaker’; Br. céré- ur, id.; W crydd, pl. ion, m. id.; Cor. cf. kerija, v. “mend shoes’; OCS krüpa “cloth, textile’; Srb. Slovene, Blg. krpa, krápa, kárpa ‘rag’ beside Blg. krăpka ‘patch’ and Srb. ktplje, fpl., Slovene: kfplja, f. and Cz. krpě ‘snow- shoe’; R kórpija "Int" (2) For the extn. in *krpitio cf. Skt. karpatam (o-gde: ‘rag’) (LW in Gk. kárpasos, f. “linen, hemp’; cf. karpátinai ‘rawhide shoes? beside karbátinai); Alb. LW in këpucë ‘shoe’; various LW forms in Lat. carpisculum *kind of snow- shoe’; LLat. carpasia ‘shoe’; Sard. crappitta, f. (Cshoe', via Etrusc.? since Gk. -d- repre- sented by -tt-); MIr. ceirt, f. ‘rag? beside es- cart ('tow', fr. *peds-karpt- or sim.); W carth, pl ion, m. ‘hemp, tow, oakum'; Cz. krpec *bast- or hide-shoe"; Pol. kierpce f. id.; Slovene krpica ‘rag’. A ^wanderword' of uncertain pro- venance, w. variant vocalism in the radical (*krp-: *korp- or *karp-). A further variant vo- calism is indicated in Li. kurpe ‘slipper’; Latv. kurpe ‘shoe’ beside karpà *offcut of cloth’; Sw. harva ‘shred, strand’; LW fr. Li. in Pol. kurp 'bast-shoe'. Cz. kfáp ‘slipper’ indicates a nasal infix.
15493:skarp- (skrap-) ‘rough, rugged, sharp; crack, split, splinter. (Evidence ambiguous. Cf. skars-) Br. skarr, pl. -u, m. (crack, chink’. But cf. skars-); Du. scherf, f. ‘sherd, potsherd’; scher- ven, v. ‘be shattered’; MHG scharben, v. ‘hack, pare’; Swiss scherb, scherp, adj. ‘hard, dry, brittle’; cf. Blg. Srb. xrapa, hrapa ‘roughness’; Slovene hrapa, f. ‘rough patch in leather’; Srb. hrápav, adj. ‘uneven, rough, knotty’; Blg. xrapav, Slovene hrapav, adj. trough; hoarse’; Cz. chrapěti, v. ‘be hoarse; snore beside chrápat, inf. ‘snore’; Pol. cf. chropowaty, adj. ‘tough, uneven’. Cf. also G Scharbe, f. (2) ‘sod, clod’?
15494:skars- ‘scrape, roughen; rough, harsh’. Cf. skors-, skers- & skarp- Arm. xaf, s. ‘briar’; xarem, v. ‘wrench’; Alb.
15587:skerbh- (skerbho, skerbhos) "(bei harsh, hard, rough'. (Gmc. ambig. cf. skerp-) MHG schirben, wv. ‘shatter’; OE sceorfan, sv. 3. ‘shred, scrape, gnaw’; sceorf, n. 'scurf, dermatitis, gripes'; Swiss scherp, scherb, adj. ‘dry, hard, brittle; R cf. u-SCérb, m. ‘harm, damage’ beside (z-gde) o-skorbit, v. ‘insult’; Cz. skrb-it, inf. (“be stingy’. Cf. E ‘to scrape in this sense); Latv. cf. Skerbelains, adj. ‘rough, hoarse’
15596:skerp- (1) ‘cut, cutting; cutter’. (Gmc. forms ambig., see skerbh-). Cf. skirp- OHG scirbi, fn. ‘sherd, pot; G Scherbe, f. id.; Sw. skårva, f. id.; — sig, v. “split off, lami- nate'; OCz. cf. (?) stfepné, f. “department, office’; (ambig.) Cz. střep, m. (“potsherd?, but cf. kerp-); Latv. Skërpis *plow-share. See next. (NB. If the Cz. form belongs here, then fr. *sKerp-)
15605:skerp- (2) “hard, harsh, painful; pain’. Same as (1) (?). (Gmc. ambig.) Oss. cf. kerppa, s. (? “gall, sore’); OE (ambig.) sceorf, n. (2) ‘gripes’, beside sceorfan, sv. 3 (1) ‘gnaw’; OCz. cf. střepně, f. (1) ‘anxiety’.
15606:skerp- (3) (?) ‘reed, rush, sedge’. (Cz. vari- ant: *skerpinà) Lat. scirpus, gs: -1, m. id.; Cz. skřípina, f. id.; isophonic in Li. skérpes, fpl. ‘bladder-wrack’
15683:skir-bhà “break, cut, separation'; skir-bhos *cut, lopped, detached'. Cf. sKir- and deriva- tives. (Gmc. forms ambig. Cf. skerp-) OHG skirbi, fn., MHG schirbe, wm. & sf. (‘earthen pot; sherd’. MHG also ‘fragment. Cf. skerp-); OCS Stríbü, adj. *maimed'; Str. bina, f. ‘chink; fragment’; Pol. szczerb, szczer- ba, mf. ‘chink, gap’; Slovak Strba, f. id.; cf. Strbit, v. ‘shatter; R cf. SCerbina, f. “crack, gap; cog; Latv. Skirba, f. ‘chink’; (Li. iso- phone: skirbti, inf. “turn sour)
15686:skirp-, see skrīp- (2) and skerp- (3)
15810:skors- ‘scrape, dig’. Cf. skars-, skers-, skarp-, skoró (2) Arm. xorem, v. ‘dig, excavate’; MHG schar- ren, v. “scratch, as fowls’; Norw. skarre, v. (sound *-r^ with a burr’, cf. Bergen dial. verka “jeg vet ikke’). (Gmc. forms ambig., cf. skars- if to Br. skarr, pl. -u, m. “crack, chink’); ON skarr, n. ‘skirmish’ (isophonic, but possibly here)

=== IEC kal- ===
3326:dhuro, io (1) ‘pierce, penetrate’. Cf. WP I, 799 & 868. See dhuros Arm. cf. dur, gs dro “tool, gimlet'; Gk. cf. skala-thüro (obscene); Lat. (?) fuscina Char poon’, if for *dhur-skin-); R dyrà ‘hole’; Li. duriü, dürti ‘pierce’; Latv. duru, durt, id.
6653:kal- (1) (kalt-) ‘slope’. Cf. WP I, 430 and kalt- Skt. cf. katakah 'slope'; Go. wilja-halpei, f. ‘favour’; OHG hald, adj. ‘inclined’; G Halde ‘slope’; Du. cf. hellen, v. ‘tilt’; ON hella *de- cant’; R cf. po-kolét ‘die off”; Li. kaliuos, kal- tis ‘lean’; üZ-kaliu, -kalti ‘lean’; at-kaltis, f. “back of chair; LW in Finn. kaltto, kalteva ‘sloping’
6654:kal- (2) ‘bright, white’. Cf. WP I, 429 Gk. kalós (‘bright, beautiful’. Despite Boeot. kalwós?); cf. kállos, n. ‘beauty’; (-a- in) kelás, gs -ádos ‘goat w. white blaze’; Lat. cf. calidus (or calidus) *white-blazed'; Latv. cf. kaleju, et ‘bleach’. (Link w. Lat. caleo, ere "be bot, and w. LG hellig ‘thirsty’ uncertain). Cf. kali-
6665:kal- (3) (kalaio, kaleio) “call, name, summon, invite, accuse'. Skt. cf. usa-kalah ‘cockerel’; Hitt. cf. kalles- “invite, entice’; Gk. kaléo; Alb. kall ‘slander’; OLat. caló, are ‘call’, cf. concilium ‘council; Mir cf. cailech, mod. coileach ‘cockerel’ be- side Ir. caileachas (‘cocksfoot’, bot.); W cei- liog ‘cockerel’; OHG halon, v. ‘call, invite’; MHG haln, id.; Li. cf. kal-bà ‘speech’, kaltas, adj. ‘accused’; kaltis, ies, f. ‘accusation’; cf. also kalenti ‘gabble, as cranes’
6666:kal- (4) ‘fix, fasten, hold’. Cf. WP I, 437. Same as (5) and (6)? Skt. kalami, kalayami, id.; Arm. kalnum, ka- lanem, id.; kalank ‘arrest’; Alb. cf. ngel (“hold, stop”, fr. *en-kalio); Lat. cf. inter-calō, -calāre (2) “delay, stop’; Li. ap-kalinti ‘imprison’
6667:kal- (5) ‘thrust’. (Same as (4) and (6)?). Cf. WP I, 437, but cf. kol- Skt. kalāmi, kalayāmi (2) ‘thrust, drive’; Arm. cf. kal, o-st. ‘threshing floor” (fr. *kalios); Alb. kall (2) ‘thrust, insert, bung’; Lat. cf. inter- calo, are (1) “insert”; OCS (here or under (6)) koljọ, klati ‘stab’; Li. kalù, kálti ‘drive in; forge’; Latv. kaļu, -t, id.
6668:kal- (6) ‘strike’. Same as (4) and (5)? Cf. WP I, 437 Per. cf. kaland ‘spade’; Arm. cf. kal, o-st. (‘threshing floor’, but equally to kal- (5)): Gk. kalís *adze'; Lat. cf. hordi-calia (for *fordi-°: ‘sacrifice of cows in calf; ON heljast (toil but equally to kal- (5); OCS koljo, klati (‘stab’, equally to (5))
6669:kal- (kaleio, -āið) “lure, deceive’. WP I, 446 Gk. kéléo (allure, if w. IE *-a-); Go. holon ‘curse’; OHG huolian, v. ‘cheat’; ON hoela ‘flatter, praise’; Du. heulen ‘conspire’
6671:kaldhos “firm, tight; firmness, strength'. See next and kadlos Lat. (ambig.) callus ‘hardness; hard skin’; MHG halt (Cholding; condition, place’; adv. ‘rather, moreover’; OS hald, id. beside Go. (and com. Gmc.) haldan ‘hold’; Dan. Norw. Sw. cf. hellere, heller, hellre ‘rather’; Sw. helst ‘preferably’; Ukr. kolod-ka ‘padlock’. Cf. Norw. helle, Sw. hälla ‘hobble, an animal’
6673:kaletos (kalət-, kalit-) “firm, brave; firmness, lock, enclosure’. Cf. kal- and kaldhos, and see WP I, 357 & 442 MIr calath, calad “hard, firm, solid’; m. “har- bour; sound of water, shore; Ir. calad, id.; Gaul. caleto- “hard, brave’; W caled ‘hard’; Br. kalet, Cor. calez, id.; DW in Sp. caleta "bar, bour’; OHG helid, OS helith ‘hero’; OE haelep, id.; ON holdr *man, squire'
6674:kalitero-, extn. of kal- (2), q. v. Alb. i kaltër ‘blue’; Du. helder ‘bright, dear
6675:kalk- ‘bend, corner; knee, hock’. Cf. WP II, 599 and kələk- Lat. calx, gs calcis ‘heel; butt-end; kick’; OE healh ‘nook, recess, small hollow’; Finn. LW kolkka (‘corner’. Vowel? See kolquos)
6676:kalos (kāl-) (1) “dry, leap’. Per. (ambig.) kar ‘deaf; Gk. cf. kēlós ‘parched’; këlon, Dor. -ã- ‘timber’; Lat. (ambig.) callus & callum (‘hardness’, but cf. kaldh-); OHG hal ‘withered’; LG haal, id. beside halig ‘ripe; dead-tired'; R (*-à-) kalit (2) ‘dry’; Srb. kaliti ‘temper steel: Pol. cf. kal-eki ‘crippled’; Ukr. kal-ika, f. ‘cripple’; Li. cf. kalstu, kalsti ‘go dry”: Latv. kalst, id.; R cf. za-kal ‘tempering, hard- ening' (*-à-)
6677:kalos (2) ‘sagacious’. Variants: kalios, kalis. Cf. WP I, 356 l Skt. kalyáh “fit; clever’; Gk. cf. peu-kálimos ‘sagacious’; Lat. callidus ‘wise’ (-11- unex- plained); Umb. kalefu- ‘tame, of oxen’; W call ‘wise, sly’; Cz. cf. ne-kolný ‘stubborn’
6678:kalos, is (1) “black, blackened, stained; stain’. WP I, 441. Cf. qual- (Slav & Skt. am- big.) Skt. (ambig.) kalah ‘black’; Romani kalo, id.; Lat. cf. calo, gs -onis 'camp-follower'; cal-1go ‘darkness’; càl-umnia ‘blackening of a charac- ter”; Ir. cf. caile (stain, fr. *kal-i-); Gk. kelís, id.; Cz. R kal, Pol. kat (ambig. ‘dung’. Cf. qual-); OE cf. hol *calumny'; cf. Li. kólioti, v. ‘abuse’; dim. extn. in Lat. caliculus *inkpot
6680:kals- (1) *hard paving'. Cf. kal-, kalos Lat. callis, m. f. “track, path’; Norw. helle *flag- stone'
6681:kaletos (kalot-, kalit-) — kam- (kom-?)
6690:kals- (2), form of kal- "hard etc. see kal- (4) and kalos (1) Lat. cf. callus “hard”; calleo, Gre ‘be hard, be tough”; Latv. kalstu, kaist ‘dry, wither; grow lean’; kalsens ‘emaciated’; Li. cf. kalstyti, v. ‘buttress’; Du. cf. be-helzen ‘enclose, contain’
6691:kaltos, à (1) “pile, heap' Skt. cf. kattayami ‘pile up”; Br. kalzen ‘heap’; kalza, v. ‘pile’; Cor. calz, calj (-£), id.; G Halde (2) “pile of ore?
6692:kaltos, à (2) (koltos?) ‘leaning; lean, slope, declivity'. Cf. WP I, 430 Skt. cf. katakab (dim. type: ‘slope’); OHG hald ‘inclined’; MHG halt (1) id.; G Halde (1) ‘slope’; Du. cf. hellen ‘tilt; ON halla, v.id.; MHG sich halden ‘sink’; ON hallr leaning, slope’; Li. kaltas ‘sloping, inclined"; káltis, v. “slope, lean’
```


## [2026-09-06T21:40:29.033Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6275,6290p;9465,9478p' HUB.txt",
 "description": "Print Hübschmann context"
}
```


### [2026-09-06T21:40:29.080Z] TOOL RESULT

```
wird zu b:
anbostan anfullen , anhaufen', 3. pr. anbdrad = skr.
sampurayati 'flillt an'; dazu anbar 'Speicher, phi. anbdr,
arm. ambar\ canbar 'Kreis' (? H. 446); siinbada *Wetzstein*
= arm. smpatak (wo aber mp auch fiir mb stehen kann);
darb *fett' = phi. carp; kurpa, kulba *Bude' = arm. krpak;
HUbichmann, Persitche Studien. 12- 178 —
LW. kathad, kalbud *Modeir, paz. kaibud, -phi, kalput^ kalpat,
gr. xaAo770()ioi^, arm. kalapar. Aber kirpas *ein femes 6e-
webe' = arm. kerpas *feines Linnen', gr. auQnaooq, skr. kar-
pasa-: erst in jiingerer Zeit entlehnt?
§ 71. Nach dem (tonlosen) s ist p als p geblieben
(gleichviel ob sp = ap. sp auf idg. sp oder k^v zurtickgeht);
asp *) 'Pferd' = zd. aspa-, dazu aspist Xuzerne' H. 79 ; as-
pand *Raute* H. 80, gospand Kleinvieh' H. 942 ; supar Tflug
H. 696; supurdan 'anvertrauen H. 697; sipas Dank, Lob'
*garu- (vgl. zd. garah-) ^) wahrscheinlich ist.
/ aus d in malax 'Heuschrecke* Fird. I, 252, 148 = zd.
madaxa-; almas *Diamant', gr. LW. = ddd/Mxc; I aus t in
(afgh.) Hilmand, s. § 94 und 88. Mehrfach findet sich / in
Lehnw5rtem: sayal ^Schakal* = skr. grgala^; lakan, lagan
'Becken, Leuchter = gr. kt^dvrj; kalam = karanb, arm. kalamh
*Kohr = gr. x()diu(it] ; kdlbad, kalbud *Modeir, phi. kolput =
gr. aaXonddiov; ddl *Einier , nach Noldeke aus dem Semi-
tischen, syr, daula u. s. w. ; pilpil 'Pfeffer = skr. pippall;
piyala *Becher = gr. (pidXri; kiltd *Schlusser = gr. xXsTda
(ace.) u. s. w. (NSldeke, Pers. Stud. II, p. 38 fig.).
Kapitel 31: Konsonantenvorschlag.
Einigen vokalisch anlautenden WSrtern wird h oder
cr vorgeschlagen.
```


## [2026-09-06T21:40:41.563Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"krep\\|korpos, es\\|corpus\" IEC.txt | head -20; echo \"=== find leaf of kerp-/krep ===\"; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor ln in (7049,8112,6653):\n    pre='\\n'.join(lines[:ln]); print(ln,'leaf',pre.count('\\f'))\nEOF",
 "description": "Grep Mann for krep root"
}
```


### [2026-09-06T21:40:43.420Z] TOOL RESULT

```
4372:grubolos ‘lumpy, rough, knotty; lump, hump’. WP I, 598 and see next MLG krüpel (> HG in G krüppel 'cripple); OE crypel; OFris. kreppel; Cz. Slovak hrbol, hrbof ‘hump’; Li. grüblas, id.; gniblüs ‘rug- ged'
7061:kerpó, ið (2) ‘be fit, be strong, thrive’. Cf. kroip-. WP I, 486 and II, 595. (Evidence am- big.) Skt. (o-gde) kálpe “be fit, succeed'; z-gde in klptáh “arranged, fit, ready’; Tokh. AB kilp-, B (also) käll «reach, obtain’; OCS cf. krépü, adj. ‘strong’; krépljo, krépiti ‘strengthen’; OCz. cf. stfépné, f. “responsibility”; Li. kerpiü, "ti join, mate’ (Various interpretations of Lat. corpus in EM:DELL & WH:LEW)
7702:korpos, å ‘cut, cutter; cutting, sharp; spike, point, crag’. Cf. kerp-, krp- Skt. (ambig.) cf. karparah (‘pot, sherd’. Cf. kerep-); Alb. karpë ‘rock, cliff; LW in Big. kàrpa, id.; Ligurian substr. in Rumansh crap, m. (‘boulder’, w. metath, as in cravun *carbonem', crapenda 'carpenta"); LW (?) in Alb. krep (‘crag’, as doublet of karpë?). Cf. WP II, 581. Here also prob. Ir. corr ‘peak, tip, corner, snout, bill, corn on foot"; W cor, pl. od m. (1) ‘point’; ON herfi ‘harrow’; Sw. harv, f. id. beside hárv, pl. -ar, f. ‘rake’; cf. EMSw. härvel ‘buckle’; Blg. krap, adi ‘short’; Li. karpas ‘cutting, clearing’; karpà ‘slice’; kárpa ‘wart; Latv. kārpa, id.
7844:krekos — krep-
7860:krep- ‘rumble, roar, resound’ Skt. cf. krape, mp. ‘lament’; a-krapista ‘he
7862:roared?; Av. cf. xraf$-, as Skt. krape; Lat. crepo, are, pf. -ui ‘bang, burst’; OE cf. *hriftan (belch', only as n. hriftung); Scots to rift, id. (Isophonic: Srb. krepati "die off. Prob. infl. by G krepieren, fr. Lat.; Slovene krép- niti, krepáti, id.)
8110:Skt. cf. krpà (instr. “by the figure"); Av. kerofs, gs: kohrpo “figure, body, belly’; Lat. corpus, gs corporis, n. “body, flesh, substance, part, group’; Mir crí ‘belly’. (The initial is implied in OHG hréf, g. sg. hréves ‘body; womb’ be- side hr&p, gs hrébes: OE hrif “belly”, cf. E midriff). Cf. WP I, 486
14265:qurp- “turn, shape, form, body'. Cf. querp-, quorp- Skt. krp, f. “form, beauty’; Av. kohrp “flesh, body’; Per. cf. kalbad, s. “form, body’; Gk. prapís, f. “bosom, heart, diaphragm’; OLat. qurpus, Lat. corpus, gs: -oris, n. “body, flesh, substance, mass’; Olr. & mod. Ir. crí, m. ‘body, shape, frame’; (Olr. also = “life*); OHG cf. href, OE hrif, n. (belly, womb’, fr. *qurep-); Icel. horf, n. “trend, relation, condition); hor- fur, fpl. ‘outlook’; cf. ON horfa, v. ‘turn, ap- pear’. (Isophones: Slovene krp-elj, s. ‘mite, tick, crablouse’; Slovak krpelec, m. ‘dwarf;
15830:skrăb- ‘scrape; sharp, grating; sharpness, roughness’. W ysgraf, pl. -ion, m. ‘scrape; scrapings’; ys- grafu, inf. ‘scrape, grate’; Ir. (long-gde) “scrá- bhaim, v. ‘scrape’; Br. skraba, inf. (‘scrape’. LW in view of -b- for *-v-?); MHG schraf, sm. ‘crag; scree; bitter cold; pungency'; schraf- fen, schrapfen, v. “lop, pol; Du. schrap, f. ‘scratch, line, mark’; schrapen & schrappen, v. ‘scrape; cross out’; Fris. skraepje, v. as Du. beside skreppe, v. ‘toi; OE scrapian, v. (‘scrape’. E. fr. ON skrapa, id.); (long-grade in expressive) Cz. škrabu-, -ati, v. ‘scrape, scratch’; as also in Eng. dial. to scroop; and in Ir. scrábhaim. Isophonic in ON skræpa, v. *pretend"); Pol. skrobac, v. ‘shave, scrape, scale’; Latv. skrabu, et, id. cf. also skrablis, s. ‘scraper’
15865:skremb- (2), variant: skromb- “shrivel, shrink crumple'. (Var. skrmb-). WP II, 588 OHG, MHG schrimpfen, MLG schrimpen, sv. id.; schrimpf, e s & wf, ‘sore, chapped skin'; Fris. skrimpe, LG schrimpen, id.; E shrimp and (Norse) skrimp, s.; Arm. xamrim, vb. « *skrmb-; (o-gde in) ON skreppa, v. ‘crumple’. Cf. Li. skrémblys, m. ‘grub, dwarf
15883:skrep- ‘hawk, rasp, scrape, rustle’. (Variant in Cz.) ON cf. skrjáfa, v. ‘rustle’; Cz. chfapét, v. “be hoarse, crackle, crack’; cf. chfaplavy, adj. ‘hoarse, cracked — of voice’; (mod. chrap-); Li. skrepsiu, -sēti, v. ‘creak, grate’; cf. skrep- liai, mpl. ‘phlegm’
=== find leaf of kerp-/krep ===
7049 leaf 281
8112 leaf 323
6653 leaf 266
```


## [2026-09-06T21:40:59.688Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:14265]); leaf=pre.count('\\f')\nprint('qurp- line 14265 leaf',leaf)\nleaves=t.split('\\f')\nimport re\n# find printed page numbers (standalone 3-4 digit lines) near\nfor i in range(leaf-2,leaf+3):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',leaves[i])\n    print(i,nums, leaves[i][:80].replace('\\n',' '))\nEOF",
 "description": "Locate Mann qurp- page"
}
```


## [2026-09-06T21:41:01.305Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PLA qalab ==\"; grep -n -i \"qālab\\|qalab\\|qālib\\|kālbad\\|kalbud\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep Asbaghi for qalab"
}
```


### [2026-09-06T21:41:01.704Z] TOOL RESULT

```
qurp- line 14265 leaf 582
580 ['1047', '1048']  fr. *quornio-); Av. kaurvo, kaour- vð, adj. ‘black’; Per. kür ‘blind’; Gk. poró
581 ['1049', '1050']  type *qusio-); MHG wes, OE hwæs, gs. “whose? quos-né, cpd. prn. cf. quos & ne A
582 ['1051', '1052'] en, see uidh-, be- low). (The phonology is that of Gk. hung: Lat. serra, see sri
583 ['1053', '1054'] OPr. kirsnan, acc. id.; Lat. cf. corrus ‘tawny? and Li. kirslys, m. 'grayling'. 
584 ['1055'] t. ‘desire’; MIr. saint, f. id.: W chwant, m. id.; Br. chwant, Cor. chwans, id.;
```


### [2026-09-06T21:41:01.741Z] TOOL RESULT

```
== PLA qalab ==
```


## [2026-09-06T21:41:09.329Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (580,581):\n    print('=== leaf',i,'===')\n    print(leaves[i][:2200])\nEOF",
 "description": "Print Mann pp.1047-1050"
}
```


### [2026-09-06T21:41:10.895Z] TOOL RESULT

```
=== leaf 580 ===
 fr. *quornio-); Av. kaurvo, kaour- vð, adj. ‘black’; Per. kür ‘blind’; Gk. porós, adj. id.; Pol. kary “black — of a horse’; Ukr. karyj “black? (from Turkish kara, according to A Brückner:SEJP)
quorpos, à “turn, link, join'. Cf. querp-, qurp-. (Skt. Av. & Li. Latv. ambig.) Skt. kalpah ‘manner’; Av. cf. kahrpuno Cl zard', LW in Arm. Karb, Let 'basilisk"); Go. hwarbon, denom. or freq. “walk? beside (e- gde) hwaírban, id., ga-hwaírbs (obedient, lit. *flexible)); OS hwarbon, as Go.; MHG warp, gs: Warbes, sm. ‘turn’; warbe, wf. ‘circle; as- sembly'; OE hwearf, m. “turn, crowd, move- ment, distance, change, error, embankment’; E wharf; EMSwedish hvarf, Sw. varv, n. ‘time, order, series, camp, layer; ON cf. hvarfla, v. ‘roam; waver’; Li. cf. pa-karpa, f. *nape: of neck’: Latv. karpis and karpe, mf. (/boathook'. Ambig.)
quorquol- (quorquol-) (1) ‘twist, turn, curl, coil, wicker, weave’. Cf. qur-quol and the e-/o- gde simplex quel-/quol- Alb. (z-gde) kurkulloj, v. ‘nestle, curl up, lurk’; Lat. curculio, gs: -onis, m. (1) *corn-weevil'; ME wharwyl, wharwhil ‘whorl, swivel, pulley’; Li. kafklas, m. ‘sallow, willow’; karkles, pl. ‘wicker’; Latv. karkls, m. ‘scrub willow’. Vari-
1047
ants of uncertain cons. (*quorp- or *quoru-) in MHG warbel, adj. ‘mobile’, cf. Skt. kár- varah ‘variegated’; OFris. hwarvel, Du. wervel, m. ‘vertebra; swivel; pegtop; OHG hwirvil (sic), id.; G. dialect Warbel, m. *whorl'. (Iso- phone: Br. porbolen, f. ‘pimple, pustule, bud")
quorquol- (quorquol-) (2) *windpipe; hoarse- ness in the throat. Lat. curculió, gs: -onis, m. ‘windpipe’; Li. kar- kulys, gs: -io, m. *hoarseness'
quorquor- (quorquort-, quorquorbhit-) ‘curly plant or object, creeper’ Skt. karkatih, f. ‘gourd’; (variant: Carbhita, -am, fn. id. fr. *querbh-); Lat. cf. cucurbita *cucumber'; OE *hwerhwefte (*written -fette & -hwette, both once), id.
quorsio ‘drag, pull, til. See next. Cf. WP I, 429. i Skt. kársami, v. ‘draw, drag; plough; lead’; Av. karos-, v. as Skt.; Per. kašam, v. ‘draw; suffer beside kašam, inf: kāštan, kistan, v. ‘plough’; Arm. kašem, v. “pull, pluck’; Alb. cf. të-kurr, v. tr. contract’, fr. *ati-°); Extn. in Av. karstis, f. ‘ploughing’; (z-gde in) Skt. krstah ‘drawn, plow
=== leaf 581 ===
 type *qusio-); MHG wes, OE hwæs, gs. “whose?
quos-né, cpd. prn. cf. quos & ne Av. kas-nà, emph. interr. pn. ‘who’; Li. cf. kas-ne-kas “something; whatever
quos-quis, cpd. prn. (neut. type: quod-quid) *whoever; any who'. Cf. the simplices. Vari- ants in Gk. & Lat. Skt. cf. kaśčid “anyone”; Av. kasCit, fn: kacit, id.; Ober kaSciy, id.; Oss. käsi, kåsi “who, which; any’; Arm. ok “somebody; anybody’; cf. oğ (not, fr. *quodquid); Gk. cf. hóstis, neut. hóti (^whoever; whatever', fr. *jos-quis, iod-quid); Lat. cf. quisquis, neut. quicquid, id.
quoteros, à, compar. extn. of type quo-, q.v. *which of two, which, who; either' WP I, 521 Skt. kataráh “which of two”; Av. katàro, id.; Oss. kadär ‘someone’; Gk. póteros, dial. kó- teros, as Skt.; Lat. uter, fn: utra, utrum, (by ‘false’ division of necuter ‘neither’), as Skt.; Osc. cf. pútúrús-pid, mpl. (^whoever', fr. *quo- teros-quid); Umb. cf. -podruh- beside putres; Olr. cf. cechtar, Ir. ceachtar (‘either of two, each; any’ fr. *quis-, quid^); Go. hwapar, as Skt.; OE hwaóer, id.; OFris. hwedder, id.; ON hvárr, id. (also "each of two"); OHG cf.
1049
(e-gde) hwëdar, id.; OCS koteryj, kotoryj, id., (also *anyone^), and com. SL: Li. katrás ‘who which; each'; Latv. katrs *each, every'
(quótorn-, see quóktorn-)
quoti (quotio-) “how much, how many”. Cf. toti. WP I, 521 Skt. káti, Av. kat (introduces a qn.); ha-kat (at once”, fr. *sm-quoti); beside Cat & cvat (Chow much, how many”, w. induced palatal- ism); Oss. cas, id.; Tokh. À kos-, cpd. B kos ‘how’ (kos-prem = “how much"); cf. also Tokh. A kac, B keç ‘number’; Arm. oč, Let and o-st. “style, method’; Myc. qoso-, Gk. pósos and ho- pósos (“how much, how many”. Gk.: Lat. Ains- worth: 1736); Alb. (Gjakovo) kasa, id.; Lat. quot, id.; Osc. cf. puz, Umb. puze ‘so that, so as to. . ?; MIr. caiti, caite, ceti ‘what, how many’; Br. pét, ped “how much, how many’; Cor. pes, id.; Li. kac, kacei, cj. ((though', lit. “however much). Extn. of type *quotitos in Skt. katithab, adj. "of what size’; Gk. póstos *which of several'. Extn. of type *quotomos in Skt. katamah “which of several; Lat. quo- tumus *what number
(quóuk-, sce quosà. Evidence ambig. Gk. cf. póux, f. a croaking bird; Cz. kavka ‘ja
```


## [2026-09-06T21:41:11.695Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PLA search ==\"; grep -n \"alab\\b\\|Qālib\\|qalib\\|kalopod\\|Kalopod\" incoming/PLA/PLA_pages.txt | head -30; echo \"== PLA page 215 ==\"; python3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\ni=215+15\nprint(leaves[i][:1800])\nEOF",
 "description": "Print Asbaghi p.215"
}
```


### [2026-09-06T21:41:13.643Z] TOOL RESULT

```
== PLA search ==
14034:u              - maslüb:            pass.          pt.           v.w      salab      q.    V.
== PLA page 215 ==
302
qubäd                                                                             216                                                         garastün


ls -        qubäd:              "ein           iranischer              König"          Io      pers.         „L; qubäd T               mp. yarıa kavät        5
                  aw.         kaväta               "der     Gründer          v.    Kavi       Dynastie".


>15- gibgär = kibär q. v.
     -                  -                                                                      4         _      3

oLs - qibbän:                       "Schnellwaage"                     pers.             oyly kapän                 ”, syr.       bis       ?.

&-         gabaß:             "Rebhuhn'                         pers.            kapk mp.                3013       kupk      4


gl         - garätig:                     Pl.       v..3b5           gartaq       q.    v.


lb-         garäf:             Pl.         v.        ss garf.


822 9.200 garbädin:                                "Zusammensetzung                    verschiedener                 Medikamente"
          pers.         >     ?.

om                                                                              v4
> - qurbuz:                         "Betrug"               pers.             2, kirbuz             6 ?.


o*»,3-           garbüs:              "Sattelbogen"                    pers.                 ui,    har-puSt               — mp.           xar     "Esel"
          cc      aw.         Xara         +    MP.       Kol        PuSt     "Rücken"         am.              parSta,           mand.     garbasaia
          (p.oxr>)                  7 möglicherweise                         aus       pers.       up harpüs.


2, -       gard:            "Hals"
```


## [2026-09-06T21:41:21.999Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[229][:2500])\nEOF",
 "description": "Print Asbaghi printed p.215"
}
```


### [2026-09-06T21:41:24.121Z] TOOL RESULT

```
                                                                              [E>}




sl      -    gäbüs:          "Eigenname"                 <        pers.» / käwus                mp.            ıy-ug     käayus au.
       kavi-usan             ı        mand.        gaiqubas              .


oub     -    gasän:          eine          Stadt     in       der       Nähe         v.    Isfahan    <       pers. „li        ka$an    3   syr.
            s*.

uläl - gäSän                = gasän           a.    v.

                                                             u.                                =9»5
sliLb - gäßäni:                   Nisba        v.    qäßän             q. v.,         syr.     =),

BRIH -        gäfür:         "Kampfer"              pers.          ec         MP. Yıa;»s kapur            7    aram,    $,85,        Yuan sus      »
       mand.        gapur             °, ar.       Lw.       käfür,          engl.         camphor,       dtsch.    Kampfer.


eU-         gäqum:          "Hermelin"              pers.          9 <T mp. +a.3 käkem                    "Name    der Gattung
       Musterlina"                10,


—IV- gälib: "Gußform, Model" pers.                                                        »Wkalbod !!              mp. >10%            kälpüs 12,
    mand. galib 1°,

     IL - gatlibgi
           gälibgi:                   "Gießer"           s. galıb
                                                             galib.

U       - galibi:                 "gegossen,             geformt".


&2 - gibäf: Pl. v. & aögabag
                      gabag q. v.

1.    Addai       Scher          s.    v.,     Nyberg             Bd.    II      s.       v.
2.    Macuch        s.      v.
3.    Ernst       S.     101.
4.    Brockelmann                s.    v.
5.    ebda.
6.    as-Suyütl             Ita.       al-MuCarrab                 s.    Ve;         TaCalivl        figh     al-luga     s.    v.
7.    Mackenzie             s.    v.
8.    Macuch        s.      v.,       Brockelmann                 s.    v.
9. TaCalibl Figh al-luga s. v.
10.    Bundahifn             s.       v.
11.    BQ.     s.      v.
12.    Nyberg          Bd.       II    s,     v.
13.    Macuch          s.    v.
```


## [2026-09-06T21:41:55.936Z] TOOL CALL #26: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py; echo ...; sed -n '1,40p' tools/verify_check.py",
 "description": "Inspect fetch_source and verify_check tools"
}
```


### [2026-09-06T21:41:55.986Z] TOOL RESULT

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
...
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
```


## [2026-09-06T21:42:06.440Z] TOOL CALL #27: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/کالبد\" \\\n \"https://en.wiktionary.org/wiki/قالب\" \\\n \"https://en.wiktionary.org/wiki/کالا\" \\\n \"https://en.wiktionary.org/wiki/κᾶλον\" \\\n \"https://en.wiktionary.org/wiki/καίω\" \\\n \"https://en.wiktionary.org/wiki/Caucasus\" \\\n \"https://en.wiktionary.org/wiki/قفقاز\" \\\n \"https://en.wiktionary.org/wiki/calibro\" \\\n \"https://www.etymonline.com/word/caliber\" \\\n \"https://www.etymonline.com/word/calm\" \\\n \"https://www.etymonline.com/word/holocaust\" \\\n \"https://www.etymonline.com/word/Caucasian\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 283, root Ku/Keu 'to burn' — kalopodion/kalbod/qalib/caliber/calm/holocaust/Caucasus chain\" ; done",
 "description": "Archive web sources for page 283"
}
```


### [2026-09-06T21:42:15.107Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e047e996ed23b5f8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee76ab0ca7206695.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2590861ca5065db3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0339f549ea712c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aa842158638dee7d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88d176f47f298486.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f5e440951e767e3a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a20fd2d1fac3fb84.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ea1221b6a9ba9cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/285a7cd3773746ef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/563b83ac86bdbb7c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f6b97d7200a747e3.txt
```


## [2026-09-06T21:42:18.121Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in e047e996ed23b5f8 ee76ab0ca7206695 2590861ca5065db3; do echo \"########## $f\"; sed -n '1,10p' $f.txt; echo \"-----\"; grep -n -i -A14 \"Etymology\" $f.txt | head -70; done",
 "description": "Read Wiktionary kalbod/qaleb/kala"
}
```


### [2026-09-06T21:42:19.995Z] TOOL RESULT

```
########## e047e996ed23b5f8
URL: https://en.wiktionary.org/wiki/کالبد
FETCHED: 2026-09-06T21:42:08Z
STATUS: 200
TITLE: کالبد - Wiktionary, the free dictionary

کالبد - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
-----
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
73- 1.3.2 
74- Descendants 
75-
76- 1.4 
--
146: Etymology
147- [ edit ] 
148-
149- From Middle Persian [script needed] ( kʾlpwt' /⁠kālbod⁠/ , “ body, shape, form ” ) , from Ancient Greek καλοπόδιον ( kalopódion , “ shoemaker’s last ” ) . Akin to Manichaean Middle Persian 𐫐𐫀𐫓𐫁𐫏𐫅 ( kʾlbyd /⁠kālbid⁠/ ) and Old Armenian կաղապար ( kałapar ) , գաղափար ( gałapʻar ) , Iranian loanwords. Doublet of قالب ( qâleb ) , the same Greek word via Arabic.
150-
151- Pronunciation
152- [ edit ] 
153-
154- ( Classical Persian ) IPA ( key ) : /kaːl.ˈbud/ 
155-
156- ( Dari, formal ) IPA ( key ) : [kʰɑːl.bʊ́d̪] 
157-
158- ( Dari, formal ) IPA ( key ) : [kʰɑːl.bʊ́d̪] 
159- ( Kabuli ) IPA ( key ) : [kʰɑːl.bʊ́d̪] 
160-
########## ee76ab0ca7206695
URL: https://en.wiktionary.org/wiki/قالب
FETCHED: 2026-09-06T21:42:09Z
STATUS: 200
TITLE: قالب - Wiktionary, the free dictionary

قالب - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
-----
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Descendants 
75-
76- 1.4 
--
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
92-
93- 2.4 
94- Participle 
95-
96- 3 
97- Ottoman Turkish 
98-
99- Toggle Ottoman Turkish subsection 
--
102: Etymology 
103-
104- 3.2 
105- Noun 
106-
107- 3.2.1 
108- Derived terms 
109-
110- 3.2.2 
111- Descendants 
112-
113- 3.3 
114- References 
115-
116- 4 
--
122: Etymology 
123-
124- 4.2 
125- Pronunciation 
126-
127- 4.3 
128- Noun 
129-
130- 4.3.1 
131- Descendants 
132-
133- Toggle the table of contents 
134-
135- قالب 
136-
--
212: Etymology
213- [ edit ] 
214-
215- From Classical Syriac ܩܠܒܝܕ ( /⁠*qālobīḏ⁠/ , “ last ” ) , from Ancient Greek καλοπόδιον ( kalopódion , “ last ” ) , diminutive of καλόπους ( kalópous , “ last ” ) , compound of κᾶλον ( kâlon , “ wood ” ) and πούς ( poús , “ foot ” ) .
216-
217- Pronunciation
########## 2590861ca5065db3
URL: https://en.wiktionary.org/wiki/کالا
FETCHED: 2026-09-06T21:42:11Z
STATUS: 200
TITLE: کالا - Wiktionary, the free dictionary

کالا - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
-----
70: Etymology 
71-
72- 2.2 
73- Adjective 
74-
75- 3 
76- Persian 
77-
78- Toggle Persian subsection 
79-
80- 3.1 
81- Alternative forms 
82-
83- 3.2 
84: Etymology 
85-
86- 3.3 
87- Pronunciation 
88-
89- 3.4 
90- Noun 
91-
92- 3.5 
93- References 
94-
95- 4 
96- Punjabi 
97-
98- Toggle Punjabi subsection 
--
101: Etymology 
102-
103- 4.2 
104- Pronunciation 
105-
106- 4.3 
107- Adjective 
108-
109- 4.3.1 
110- Declension 
111-
112- 4.3.2 
113- See also 
114-
115- 4.4 
--
124: Etymology 
125-
126- 5.2 
127- Pronunciation 
128-
129- 5.3 
130- Noun 
131-
132- 5.4 
133- Adjective 
134-
135- 5.4.1 
136- Declension 
137-
138- 5.4.2 
--
235: Etymology
236- [ edit ] 
237-
238- Inherited from Sanskrit काल ( kāla ) . Cognate with Marathi काळा ( kāḷā ) , Punjabi کالا ( kālā ) and Urdu کالا ( kālā ) .
239-
240- Adjective
241- [ edit ] 
242-
```


## [2026-09-06T21:42:23.533Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Persian$/{f=1} f' 2590861ca5065db3.txt | sed -n '1,60p'",
 "description": "Read Persian section of kala wiktionary"
}
```


### [2026-09-06T21:42:25.234Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 کاله ( kâle ) 

 Etymology
 [ edit ] 

 Ultimately a derivative of Proto-Iranian *kar- ( “ to do, make ” ) , from Proto-Indo-European *kʷer- ( “ to make ” ) . See Old Armenian կահ ( kah ) for more.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /kaː.ˈlaː/ 

 ( Dari, formal ) IPA ( key ) : [kʰɑː.lɑ́ː] 

 ( Dari, formal ) IPA ( key ) : [kʰɑː.lɑ́ː] 
 ( Kabuli ) IPA ( key ) : [kʰɑː.lɑ́ː] 

 ( Hazaragi ) IPA ( key ) : [kʰɔː.lɔ́ː] 

 ( Iran, formal ) IPA ( key ) : [kʰɒː.lɒ́ː] 

 ( Tajik, formal ) IPA ( key ) : [kʰɔ.lɔ́] 

 Rhymes: -aː 

 Readings

 Classical reading ? 

 kālā

 Dari reading ? 

 kālā

 Iranian reading ? 

 kâlâ

 Tajik reading ? 

 kolo

 Noun
 [ edit ] 

 کالا • ( kâlâ ) ( plural کالاها ) 

 things ; goods ; commodity ; article 
 Synonym: اجناس ( ajnâs ) 
 حمل و نقل کالا ― haml o naql-e kâlâ ― transportation of commodities 
 c. 1011 , Abu'l-Qāsim Firdawsī , “The reign of Gushtāsp”, in شاهنامه [ Book of Kings ]‎ [1] : سواران جنگی همی تاختند
به کالا گرفتن نپرداختند sawārān jangē hamē-tāxtand
ba kālā giriftan na-pardāxtand The riders were charging for a battle;
```


## [2026-09-06T21:42:34.388Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 88d176f47f298486 f5e440951e767e3a a20fd2d1fac3fb84 e0339f549ea712c1 aa842158638dee7d; do echo \"########## $f\"; sed -n '4p' $f.txt; grep -n -A10 \"^ Etymology$\" $f.txt | head -50; done",
 "description": "Read Caucasus/qafqaz/calibro/kalon/kaio etymologies"
}
```


### [2026-09-06T21:42:36.434Z] TOOL RESULT

```
########## 88d176f47f298486
TITLE: Caucasus - Wiktionary, the free dictionary
186: Etymology
187- [ edit ] 
188-
189- Via Latin Caucasus , from Ancient Greek Καύκασος ( Kaúkasos ) .
190-
191- Pronunciation
192- [ edit ] 
193-
194- IPA ( key ) : /ˈkɔːkəsəs/ 
195-
196- Audio ( US ) : ( file ) 
--
437: Etymology
438- [ edit ] 
439-
440- Borrowed from Ancient Greek Καύκασος ( Kaúkasos ) .
441-
442- Pronunciation
443- [ edit ] 
444-
445- ( Classical Latin ) IPA ( key ) : [ˈkau̯.ka.sʊs] 
446-
447- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈkaːu̯.ka.s̬us] 
########## f5e440951e767e3a
TITLE: قفقاز - Wiktionary, the free dictionary
155: Etymology
156- [ edit ] 
157-
158- Ultimately from Middle Persian *Kaf kōf ( “ Mount Qaf ” ) .
159-
160- Pronunciation
161- [ edit ] 
162-
163- ( Classical Persian ) IPA ( key ) : /qaf.ˈqaːz/ 
164-
165- ( Dari, formal ) IPA ( key ) : [qäf.qɑːz] 
########## a20fd2d1fac3fb84
TITLE: calibro - Wiktionary, the free dictionary
########## e0339f549ea712c1
TITLE: κᾶλον - Wiktionary, the free dictionary
155: Etymology
156- [ edit ] 
157-
158- Connected with καίω ( kaíō , “ to burn ” ) as "firewood", by comparison with the synonymous δᾱλός ( dālós , “ firebrand ” ) . However, according to Beekes, a Pre-Greek origin is much more likely. [ 1 ] 
159-
160- Pronunciation
161- [ edit ] 
162-
163- IPA ( key ) : /kâː.lon/ → /ˈka.lon/ → /ˈka.lon/ 
164-
165- ( 5 th BCE Attic ) IPA ( key ) : /kâː.lon/ 
########## aa842158638dee7d
TITLE: καίω - Wiktionary, the free dictionary
207: Etymology
208- [ edit ] 
209-
210- From Proto-Hellenic *káwyō , likely from Proto-Indo-European *keh₂w- ( “ to burn ” ) , with cognates such as Lithuanian kūlė̃ ( “ smut fungus ("burnt fungus") ” ) , Latvian kūla ( “ old; dry; grass of last year ” ) , [ 1 ] and possibly Persian سو ( su , “ light ” ) .
211-
212- Pronunciation
213- [ edit ] 
214-
215- IPA ( key ) : /kǎi̯.ɔː/ → /ˈcɛ.o/ → /ˈce.o/ 
216-
217- ( 5 th BCE Attic ) IPA ( key ) : /kǎi̯.ɔː/ 
--
2053: Etymology
2054- [ edit ] 
2055-
2056- Inherited from Ancient Greek καίω ( kaíō ) ; the form καίγω ( kaígo ) , from Medieval καίγω ( kaígō ) , from Proto-Hellenic *kawyō . Also see καύση ( káfsi , “ burning ” ) .
2057-
2058- Pronunciation
2059- [ edit ] 
2060-
2061- IPA ( key ) : /ˈce.o/ 
2062-
2063- Hyphenation: καί‧ω
```


## [2026-09-06T21:42:47.616Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== caucasus scythian ==\"; grep -n -i \"scythian\\|kroy\\|krou\\|ice\\|Kaukasos\\|unknown\" 88d176f47f298486.txt | head -20; echo; echo \"== qafqaz full ==\"; sed -n '140,200p' f5e440951e767e3a.txt; echo; echo \"== calibro ==\"; sed -n '100,190p' a20fd2d1fac3fb84.txt",
 "description": "Inspect Caucasus/qafqaz/calibro details"
}
```


### [2026-09-06T21:42:47.685Z] TOOL RESULT

```
== caucasus scythian ==
654: Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

== qafqaz full ==

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: قفقاز 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 قفقازیه ( qafqâziyye ) , قفقاسیه ( qafqâsiyye ) ( dated ) 

 Etymology
 [ edit ] 

 Ultimately from Middle Persian *Kaf kōf ( “ Mount Qaf ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /qaf.ˈqaːz/ 

 ( Dari, formal ) IPA ( key ) : [qäf.qɑːz] 

 ( Dari, formal ) IPA ( key ) : [qäf.qɑːz] 
 ( Kabuli ) IPA ( key ) : [qäf.qɑːz] 

 ( Hazaragi ) IPA ( key ) : [qäf.qɔːz] 

 ( Iran, formal ) IPA ( key ) : [qæf.ɢɒːz] 

 ( Tajik, formal ) IPA ( key ) : [qäf.qɔz] 

 Rhymes: -aːz 

 Readings

 Classical reading ? 

 qafqāz

 Dari reading ? 

 qafqāz

 Iranian reading ? 

 ġafġâz

 Tajik reading ? 

 qafqoz

 Proper noun
 [ edit ] 

 قَفْقَاز • ( qafqāz  / ġafġâz ) ( Tajik spelling Қафқоз ) 


== calibro ==
 calibro 

 14 languages 

 Català 
 Español 
 Suomi 
 Français 
 Magyar 
 Ido 
 Italiano 
 한국어 
 Malagasy 
 Nederlands 
 Polski 
 Português 
 Türkçe 
 中文 

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

 See also: calibró and calibrò 

 Italian
 [ edit ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈka.li.bro/ 

 Rhymes: -alibro 

 Hyphenation: cà‧li‧bro 

 Etymology 1
 [ edit ] 

 Possibly from Arabic قَالِب ( qālib , “ mold ” ) , itself from Ancient Greek καλαπούς ( kalapoús ) , a term related to shoemaking. Or, possibly a derivation of Latin qua libra , "of what dimensions, weight."

 Noun
```


## [2026-09-06T21:42:54.161Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3ea1221b6a9ba9cf 285a7cd3773746ef 563b83ac86bdbb7c f6b97d7200a747e3; do echo \"########## $f\"; sed -n '4p' $f.txt; grep -n -m1 -A25 \"caliber\\|calm (n\\|holocaust (n\\|Caucasian\" $f.txt | head -40; done",
 "description": "Read etymonline entries"
}
```


### [2026-09-06T21:42:55.855Z] TOOL RESULT

```
########## 3ea1221b6a9ba9cf
TITLE: Caliber - Etymology, Origin & Meaning
1:URL: https://www.etymonline.com/word/caliber
2-FETCHED: 2026-09-06T21:42:13Z
3-STATUS: 200
4-TITLE: Caliber - Etymology, Origin & Meaning
5-
6-Caliber - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- Advertisement Remove Ads 
19- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
20-
########## 285a7cd3773746ef
TITLE: Calm - Etymology, Origin & Meaning
28: calm (n.) 
29-
30- c. 1400, "absence of storm or wind," from the adjective or from Old French calme , carme "stillness, quiet, tranquility," or directly from Old Italian calma "quiet, fair weather" (see calm (adj.)). The figurative sense of "peaceful manner, mild bearing" is from early 15c.; that of "freedom from agitation or passion" is from 1540s.
31-
32- Aftir the calm, the trouble sone Mot folowe. ["Romance of the Rose," c. 1400]
33- also from c. 1400 
34-
35- calm (v.) 
36-
37- late 14c., "to become calm," from Old French calmer or from calm (adj.). Also transitive, "to make still or quiet" (1550s). Related: Calmed ; calming .
38- also from late 14c. 
39-
40- Entries linking to calm 
41-
42- caustic (adj.) 
43-
44- c. 1400, "capable of burning or destroying organic tissue, corrosive," from Latin causticus "burning, caustic," from Greek kaustikos "capable of burning; corrosive," from kaustos "combustible; burnt," verbal adjective from kaiein , the Greek word for "to burn" (transitive and intransitive) in all periods, which is of uncertain origin with no certain cognates outside Greek.
45-
46- The figurative sense of "sarcastic, severely critical" is attested from 1771. As a noun "a caustic substance," early 15c., from the adjective.
47-
48- becalm (v.) 
49-
50- 1550s in the nautical use, "deprive a ship of wind," from be- + calm . The meaning "make calm or still" is from 1610s. Related: Becalmed ; becalming .
51-
52- calmative 
53- calmly 
########## 563b83ac86bdbb7c
TITLE: Holocaust - Etymology, Origin & Meaning
23: holocaust (n.) 
24-
25- mid-13c., "sacrifice by fire, burnt offering," from Old French holocauste (12c.), or directly from Late Latin holocaustum , from Greek holokauston "a thing wholly burnt," neuter of holokaustos "burned whole," from holos "whole" (from PIE root *sol- "whole, well-kept") + kaustos , verbal adjective of kaiein "to burn" (see caustic ).
26-
27- Originally a Bible word for "burnt offerings," given wider figurative sense of "massacre, destruction of a large number of persons" from 1670s. The Holocaust "Nazi genocide of European Jews in World War II," first recorded 1957, earlier known in Hebrew as Shoah "catastrophe." The word itself was used in English in reference to Hitler's Jewish policies from 1942, but not as a proper name for them.
28-
29- English chronicler Richard of Devizes in his contemporary account of the coronation of Richard I in 1189 used the word holocaust when he described the mass murder of the Jews of London, although he meant it as "a sacrificial offering."
30-
31- also from mid-13c. 
32-
33- Entries linking to holocaust 
34-
35- caustic (adj.) 
36-
37- c. 1400, "capable of burning or destroying organic tissue, corrosive," from Latin causticus "burning, caustic," from Greek kaustikos "capable of burning; corrosive," from kaustos "combustible; burnt," verbal adjective from kaiein , the Greek word for "to burn" (transitive and intransitive) in all periods, which is of uncertain origin with no certain cognates outside Greek.
38-
39- The figurative sense of "sarcastic, severely critical" is attested from 1771. As a noun "a caustic substance," early 15c., from the adjective.
40-
41- *sol- 
42-
43- also solə-, Proto-Indo-European root meaning "whole, well-kept." 
44-
45- It might form all or part of: catholic ; consolidate ; consolidation ; holism ; holo- ; holocaust ; Holocene ; hologram ; holograph ; insouciant ; safe ; safety ; sage (n.1) kind of herb; salubrious ; salutary ; salute ; salvage ; salvific ; salvo "simultaneous discharge of guns;" save (v.) "deliver from danger;" save (prep.) "except;" solder ; soldier ; solemn ; solicit ; solicitous ; solid ; solidarity ; solidity ; sou .
46-
47- It might also be the source of: Sanskrit sarvah "uninjured, intact, whole;" Avestan haurva- "uninjured, intact;" Old Persian haruva- ; Greek holos "whole;" Latin salvus "uninjured, in good health, safe," salus "good health," solidus "solid;" Armenian olj "whole, healthy."
48-
########## f6b97d7200a747e3
TITLE: Caucasian - Etymology, Origin & Meaning
1:URL: https://www.etymonline.com/word/Caucasian
2-FETCHED: 2026-09-06T21:42:15Z
3-STATUS: 200
```


## [2026-09-06T21:43:02.989Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### caliber\"; sed -n '20,60p' 3ea1221b6a9ba9cf.txt; echo \"### Caucasian\"; sed -n '20,60p' f6b97d7200a747e3.txt",
 "description": "Print etymonline caliber and Caucasian bodies"
}
```


### [2026-09-06T21:43:03.046Z] TOOL RESULT

```
### caliber

 Origin and history of caliber 

 caliber (n.) 

 "inside diameter of a gun barrel," 1580s, from French calibre (by mid-16c., perhaps late 15c.), often said to be ultimately from Arabic qalib "a mold for casting." Barnhart remarks that Spanish calibre , Italian calibro "appear too late to act as intermediate forms" between the Arabic word and the French.

 But English Words of Arabic Ancestry finds that the idea of an Arabic source "comes with no evidence and no background historical context to support it. It is far more likely that the word was formed in French" from Medieval Latin qua libra "of what weight" (a theory first published 19c. by Mahn), from fem. ablative of quis (from PIE root *kwo- , stem of relative and interrogative pronouns) + ablative of libra "balance" (see Libra ).

 In U.S., expressed in decimal parts of an inch ( .44-caliber = ".44-inch caliber"). The earliest sense in English is a figurative one, "degree of merit or importance" (1560s), from French. Later, figuratively, "the capacity of one's mind, one's intellectual endowments."
 also from 1580s 

 Entries linking to caliber 

 Libra (n.) 

 zodiac constellation represented by a pair of scales, late Old English, from Latin libra "a balance, pair of scales," also "pound (unit of weight)," from Proto-Italic *leithra- "pound." De Vaan compares Greek litra "name of a Sicilian coin," which "was probably borrowed from an Italic language at the stage containing [ -thr- ]."

 Not a separate constellation in ancient Greece, where it was khelae , "the claws" of adjacent Skorpios. Nativized in Old Norse as skala-merki . Meaning "person born under the sign of Libra" is from 1894. Related: Libral ; Libran .

 calibrate (v.) 

 "determine the caliber of," 1839, verb formed from caliber + -ate (2). Also "determine the relative value of" different parts of an arbitrary scale (1869). Related: calibrated ; calibrating .

 calibre 
 caliper 
 subcaliber 
 *kwo- 
 See All Related Words (6) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 quality 

 c. 1300, qualite, "temperament, character, disposition," from Old French calite, qualite "quality, nature, characteristic" (12c., Modern French qualité), from Latin qualitatem (nominative qualitas) "a quality, property; nature, state, condition" (said [Tucker, etc.] to have been 

 bore 

 "pierce or perforate with a rotatory cutting instrument, make a circular hole in by turning an auger, drill, etc.," Old English borian "to bore through, perforate," from bor "auger," from Proto-Germanic *buron (source also of Old Norse bora, Swedish borra, Old High German boron, 
### Caucasian

 Origin and history of Caucasian 

 Caucasian (adj.) 

 1807, of or pertaining to the Caucasus Mountains (q.v.), with -ian . Applied to the "white" race 1795 (in Latin) by German anthropologist Johann Friedrich Blumenbach (1752-1840), who in his pioneering treatise on anthropology distinguished mankind into five races: Mongolian, Ethiopian, Malay, (Native) American, and Caucasian. In the last group he included nearly all Europeans (except Lapps and Finns), Armenians, Persians, and Hindus, as well as Arabs and Jews. His attempt at division was based on physical similarities in skulls.

 Blumenbach had a solitary Georgian skull; and that skull was the finest in his collection: that of a Greek being the next. Hence it was taken as the type of the skull of the more organised divisions of our species. More than this, it gave its name to the type, and introduced the term 
 Caucasian . Never has a single head done more harm to science than was done in the way of posthumous mischief by the head of this well-shaped female from Georgia. [Robert Gordon Latham, M.D., "The Natural History of the Varieties of Man," London, 1850]

 The word has long since been abandoned as a historical/anthropological term. Compare Aryan .
 also from 1807 

 Caucasian (n.) 

 "resident or native of the Caucasus," 1843; see Caucasian (adj.). Meaning "one of the 'white' race" is from 1830.
 also from 1843 

 Entries linking to Caucasian 

 Aryan 

 c. 1600, as a term in classical history, from Latin Arianus , Ariana , from Greek Aria , Areia , names applied in classical times to the eastern part of ancient Persia and to its inhabitants. Ancient Persians used the name in reference to themselves (Old Persian ariya- ), hence Iran . Ultimately from Sanskrit arya- "compatriot;" in later language "noble, of good family."

 Also the name Sanskrit-speaking invaders of India gave themselves in the ancient texts. Thus it was the word early 19c. European philologists (Friedrich Schlegel, 1819, who linked it with German Ehre "honor") applied to the ancient people we now call Indo-Europeans, suspecting that this is what they called themselves. This use is attested in English from 1851. In German from 1845 it was specifically contrasted to Semitic (Lassen).

 German philologist Max Müller (1823-1900) popularized Aryan in his writings on comparative linguistics, recommending it as the name (replacing Indo-European , Indo-Germanic , Caucasian , Japhetic ) for the group of related, inflected languages connected with these peoples, mostly found in Europe but also including Sanskrit and Persian. The spelling Arian was used in this sense from 1839 (and is more philologically correct), but it caused confusion with Arian , the term in ecclesiastical history.

 The terms for God, for house, for father, mother, son, daughter, for dog and cow, for heart and tears, for axe and tree, identical in all the Indo-European idioms, are like the watchwords of soldiers. We challenge the seeming stranger; and whether he answer with the lips of a Greek, a German, or an Indian, we recognize him as one of ourselves. [Müller, "History of Ancient Sanskrit Literature," 1859]

 Aryan was gradually replaced in comparative linguistics c. 1900 by Indo-European , except when used to distinguish Indo-European languages of India from non-Indo-European ones. From the 1920s Aryan began to be used in Nazi ideology to mean "member of a Caucasian Gentile race of Nordic type." As an ethnic designation, however, it is properly limited to Indo-Iranians (most justly to the latter) and has fallen from general academic use since the Nazis adopted it.

 Caucasus (n.) 

 mountain range between the Black and Caspian seas, separating Europe and the Middle East, from Latin Caucasus , from Greek kaukasis , said by Pliny ("Natural History," book six, chap. XVII) to be from a Scythian word similar to kroy-khasis , literally "(the mountain) ice-shining, white with snow." But possibly from a Pelasgian root *kau- meaning "mountain."

 Caucasoid 
 -ian 
 See All Related Words (4) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
```


## [2026-09-06T21:43:37.072Z] TOOL CALL #34: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/قلب\" \\\n \"https://www.nisanyansozluk.com/kelime/Kafkas\" \\\n \"https://en.wiktionary.org/wiki/Кавказ\" \\\n \"https://abadis.ir/fatofa/کالا/\" \\\n \"https://abadis.ir/fatofa/کالبد/\" \\\n \"https://abadis.ir/fatofa/قالب/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 283: Arabic q-l-b root, Kafkas/Kavkaz transmission, Mo'in entries for kālā/kālbod/qāleb\"; done",
 "description": "Archive more sources"
}
```


### [2026-09-06T21:43:44.835Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a07acd81618dd0e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c925fca0ac7163b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1432a10844d9273.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc77dd0c4928d951.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a00262bb979c7d55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34ee3685af824f51.txt
```


## [2026-09-06T21:43:48.914Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### qalb\"; grep -n -m3 -A8 \"^ Etymology\" a07acd81618dd0e6.txt | head -50; echo \"### nisanyan\"; sed -n '1,6p' 9c925fca0ac7163b.txt; grep -n -i -m5 -B2 -A8 \"Kafkas\" 9c925fca0ac7163b.txt | head -40; echo \"### kavkaz\"; grep -n -m2 -A8 \"^ Etymology\" f1432a10844d9273.txt | head -30",
 "description": "Read qalb / Kafkas / Кавказ"
}
```


### [2026-09-06T21:43:49.006Z] TOOL RESULT

```
### qalb
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.1.2.1 
--
101: Etymology 2 
102-
103- 1.2.1 
104- Pronunciation 
105-
106- 1.2.2 
107- Noun 
108-
109- 1.2.2.1 
--
124: Etymology 1 
125-
126- 2.1.1 
127- Noun 
128-
129- 2.2 
### nisanyan
URL: https://www.nisanyansozluk.com/kelime/Kafkas
FETCHED: 2026-09-06T21:43:40Z
STATUS: 200
TITLE: Kelime bulunamadı - Nişanyan Sözlük

Kelime bulunamadı - Nişanyan Sözlük 
1:URL: https://www.nisanyansozluk.com/kelime/Kafkas
2-FETCHED: 2026-09-06T21:43:40Z
3-STATUS: 200
4-TITLE: Kelime bulunamadı - Nişanyan Sözlük
5-
6-Kelime bulunamadı - Nişanyan Sözlük 
7-
8- Nişanyan Sözlük 
9-
### kavkaz
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
79: Etymology 
80-
81- 2.2 
82- Noun 
83-
84- 3 
85- Russian 
86-
87- Toggle Russian subsection
```


## [2026-09-06T21:43:53.895Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### qalb bodies\"; grep -n -A4 \"^ Etymology 1$\" a07acd81618dd0e6.txt | grep -v \"^\\s*[0-9]*-\\s*$\" | head -40; echo; echo \"=== search Proto-Semitic in qalb\"; grep -n -i \"proto-semitic\\|Aramaic\\|Hebrew\\|to turn\" a07acd81618dd0e6.txt | head -20; echo; echo \"### kavkaz russian\"; awk '/^ Russian$/{f=1} f' f1432a10844d9273.txt | sed -n '1,30p'",
 "description": "Extract qalb and Kavkaz etymologies"
}
```


### [2026-09-06T21:43:55.482Z] TOOL RESULT

```
### qalb bodies
484: Etymology 1
485- [ edit ] 
487- Root 
--
2109: Etymology 1
2110- [ edit ] 
2112- Inherited from Arabic قَلْب ( qalb ) .
--
2163: Etymology 1
2164- [ edit ] 
2166- Inherited from Arabic قَلَبَ ( qalaba ) .
--
2367: Etymology 1
2368- [ edit ] 
2370- Inherited from Arabic قَلْب ( qalb ) .
--
2415: Etymology 1
2416- [ edit ] 
2418- Inherited from Arabic قَلْب ( qalb ) .
--
2637: Etymology 1
2638- [ edit ] 
2640- Inherited from Arabic قَلْب ( qalb ) .
--
2908: Etymology 1
2909- [ edit ] 
2911- Inherited from Arabic قَلَبَ ( qalaba ) .

=== search Proto-Semitic in qalb
493: Derived from قَلَبَ ( qalaba , “ to turn ” ) .
494:Alternatively, from Proto-Semitic *libb- ( “ heart ” ) , with the initial ق possibly being a phonological insertion to break a biconsonantal cluster and avoid * ∅alb or * ∅ulb , thus * lb → * ∅alb → qalb . See also Arabic لُبّ ( lubb ) , "core, heart, intellect", without q- as well.
501: ( to turn ) : IPA ( key ) : /qa.la.ba/ 
788: to turn (clarification of this definition is needed) 
1284: to turn , to flip , to roll over repeatedly
1997: While it could be thought as from the root ق ل ب ( q l b ) due to being “ turned over ” or “ warped ” around the arm, Classical Syriac ܩܘܠܒܐ ( qulbā , “ bracelet ” ) is attested early and suggested as a source for this Arabic word, and as Aramaic lacks this root, Akkadian 𒄑𒆪𒌌𒁍 ( GIŠ qu 3 -ul-pu /⁠qulpu⁠/ , “ encasement, bark of wood ” ) is suggested as its source. The later sense may also be reflected in a different homophonic Akkadian 𒆰𒁍 ( qul-pu /⁠qulpu⁠/ , “ a type of barley ” ) .
2089: “ qwlbˀ ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986– 
2133: ( transitive ) to turn over 
2178: to flip , to turn over 
2399: to turn , to flip 
2455: to turn , to flip 
2549: to mix , to stir , to turn , to flip 
2673: to turn , to flip 
2927: to flip , to turn over 
3081: Arabic terms inherited from Proto-Semitic 
3082: Arabic terms derived from Proto-Semitic 

### kavkaz russian
 Russian
 [ edit ] 

 Etymology
 [ edit ] 

From Ancient Greek Καύκασος ( Kaúkasos ) , ultimately of Iranian origin.

 Russian Wikipedia has an article on: Кавказ 

 Wikipedia ru 

 Was already attested in Old East Slavic as Кавкасийскыѣ горы ( Kavkasijskyjě gory ) , a calque of Καυκάσια ὄρη , however according to Vasmer and Trubachyov the current form Кавказ ( Kavkaz ) stems from French Caucase and German Kaukasus .

 Pronunciation
 [ edit ] 

 IPA ( key ) : [kɐfˈkas] 

 Audio : ( file ) 

 Proper noun
 [ edit ] 

 Кавка́з • ( Kavkáz )  m   inan ( genitive Кавка́за ) 

 Caucasus (a region in Eurasia)
 на Кавка́зе ― na Kavkáze ― in the Caucasus 

 Declension
```


## [2026-09-06T21:44:10.089Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"== $f\"; grep -c \"کالبد\" $f 2>/dev/null; done",
 "description": "Find kalbod in Borhan volumes"
}
```


### [2026-09-06T21:44:11.696Z] TOOL RESULT

```
Exit code 1
== BQT_v1_pages.txt
3
== BQT_v2_pages.txt
1
== incoming/BQT/BQT_v3_pages.txt
2
== incoming/BQT/BQT_v4_pages.txt
1
== incoming/BQT/BQT_v5_pages.txt
0
```


## [2026-09-06T21:44:17.370Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['incoming/BQT/BQT_v3_pages.txt','incoming/BQT/BQT_v2_pages.txt' ,'incoming/BQT/BQT_v4_pages.txt']:\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(f,e); continue\n    leaves=t.split('\\f')\n    for i,L in enumerate(leaves):\n        if 'کالبد' in L:\n            m=re.search(r'\\[pdf page (\\d+)\\]',L)\n            print(f,'leaf',i,m.group(0) if m else '', L[:150].replace('\\n',' '))\nEOF\nls incoming/BQT/",
 "description": "Locate kalbod page in Borhan v3"
}
```


### [2026-09-06T21:44:19.794Z] TOOL RESULT

```
incoming/BQT/BQT_v3_pages.txt leaf 367 [pdf page 368] [pdf page 368] ‎—\eve—‏ کالجوش کویندکه ‎Ge‏ باشد ‎ASE ASH, ٩‏ | ‎oly!‏ مقدار باشد که اسب وآدم لتواند چست - و تخته سنك تنك و ‎SW‏ را ‎SaaS js‏ بر روی م
incoming/BQT/BQT_v3_pages.txt leaf 474 [pdf page 475] [pdf page 475] - ونان بزرکه روغنی را ‎5a‏ گفته‌اند؟ .  ‎LS‏ 2 بر وزن حلوا » بمعنی رخته کرفتن ووصل ‎OS‏ چیزی‌باشد بچیزی ‎Ss‏ ۴ - ودر مژیدالفضلا بمعنی غ
incoming/BQT/BQT_v2_pages.txt [Errno 2] No such file or directory: 'incoming/BQT/BQT_v2_pages.txt'
incoming/BQT/BQT_v4_pages.txt leaf 490 [pdf page 491] [pdf page 491] هیگل نها هیکل۱ - باکاف بروزن سبقل » بتخانه | وقالب آدمیزاد باشد - راکوبند؟ - وهر بنا ی که عظیم ورفیع باشد - هیکل رضوآن - کنایه از هیأت 
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
```


## [2026-09-06T21:44:23.144Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 900 incoming/BQT/BQT_v3_pagemap.json; echo; python3 -c \"\nimport json;d=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))\nprint(type(d), list(d)[:5] if isinstance(d,dict) else d[:5])\n\"",
 "description": "Inspect Borhan v3 pagemap"
}
```


### [2026-09-06T21:44:24.977Z] TOOL RESULT

```
{
"pdf": "data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
"pdf_pages": 721,
"offset_mode": 1203,
"anchors": 34,
"map": {
"1210": 1,
"1211": 2,
"1212": 3,
"1213": 4,
"1214": 5,
"1215": 6,
"1216": 7,
"1217": 8,
"1218": 9,
"1219": 10,
"1220": 11,
"1221": 12,
"1222": 13,
"1223": 14,
"1224": 15,
"1225": 16,
"1226": 17,
"1227": 18,
"1228": 19,
"1229": 20,
"1230": 21,
"1231": 22,
"1232": 23,
"1233": 24,
"1234": 25,
"1235": 26,
"1236": 27,
"1237": 28,
"1238": 29,
"1239": 30,
"1240": 31,
"1241": 32,
"1242": 33,
"1243": 34,
"1244": 35,
"1245": 36,
"1246": 37,
"1247": 38,
"1248": 39,
"1249": 40,
"1250": 41,
"1251": 42,
"1252": 43,
"1253": 44,
"1254": 45,
"1255": 46,
"1256": 47,
"1257": 48,
"1258": 49,
"1259": 50,
"1260": 51,
"1261": 52,
"1262": 53,
"1263": 54,
"1264": 55,
"1265": 56,
"1266": 57,
"1267": 58,
"1268": 59,
"1269": 60,
"1270": 61,
"1271": 62,
"1272": 63,
"1273": 64,
"1
<class 'dict'> ['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
```


## [2026-09-06T21:44:32.648Z] TOOL CALL #40: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1075 2>&1 | head -60",
 "description": "Fetch Borhan printed page 1075"
}
```


### [2026-09-06T21:44:35.165Z] TOOL RESULT

```
no scan of BQT covers printed page 1075 (see 'scans' in refs_online.json)
```


## [2026-09-06T21:44:39.000Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\n\"; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v2_pages.txt | cut -c1-200; grep -o \"\\[pdf page [0-9]*\\]\" BQT_v2_pages.txt | tail -2",
 "description": "Check BQT scan coverage"
}
```


### [2026-09-06T21:44:40.491Z] TOOL RESULT

```
[
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
]
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
```


## [2026-09-06T21:44:52.418Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nfor i,L in enumerate(leaves):\n    if 'کالبد' in L or 'کالب' in L:\n        print('leaf',i, L[:200].replace('\\n',' '))\nEOF",
 "description": "Search Borhan v2 for kalb"
}
```


### [2026-09-06T21:44:54.184Z] TOOL RESULT

```
leaves 684
leaf 486                                                   ‫يان دهم‬                           ‫در زای نقطه دار بافا مشتمل برده لغت‬   ‫سياه و‬   ‫چویآزنیست‬                   ‫® »‬             ‫شد‬
```


## [2026-09-06T21:45:04.784Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,collections,re\nc=collections.Counter(); ex=[]\nfor f in glob.glob('data/verification/page-*.json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        objs=[e]+e.get('nodes',[])\n        for o in objs:\n            for r in o.get('ref_check',[]) or []:\n                if str(r.get('ref','')).startswith('BQT:'):\n                    c[r.get('status')]+=1\n                    if len(ex)<8 and r.get('status') in ('supports','not_found','partial'):\n                        ex.append((f,r['ref'],r['status'],r['note'][:220]))\nprint(c)\nfor x in ex: print(x); print()\nEOF",
 "description": "Survey prior BQT ref_check results"
}
```


### [2026-09-06T21:45:07.028Z] TOOL RESULT

```
Counter({'supports': 472, 'partial': 146, 'not_found': 34, 'not_checked': 11, 'contradicts': 8})
('data/verification/page-345.json', 'BQT:1997', 'partial', "BQT_v4_pages.txt pdf page 80 = printed p. 1997, Mo'in's footnote 5 to مروارید: «مروارید ... پهلوی MORVĀRĪD ... از یونانی MARGARITES ... بعربی لؤلؤ» — Mo'in has the headword with the Pahlavi form as Nourai draws it, but d")

('data/verification/page-345.json', 'BQT:1981', 'supports', "BQT_v4_pages.txt pdf page 64 = printed p. 1981, Mo'in's footnote 10 to مرجان: «مرجان کلمهٔ مخفف عربی از لغت سریانی MARGANITA «دزی ج ۲ ص ۵۷۸» که لغت بمعنی مروارید بوده و سپس به بسد اطلاق شده است. Fleischer در «تعلیقات در ")

('data/verification/page-243.json', 'BQT:1571', 'supports', "Fetched with tools/ref_page.py BQT:1571 (BQT_v3_picofile.pdf pdf-page 364; the running number ‑۱۵۷۱‑ is printed at the head of the page). The page carries the entry «کافور، بر وزن ناسور، معروف» with Mo'in's numbered foot")

('data/verification/page-243.json', 'BQT:1571', 'supports', "ref_page.py BQT:1571 (BQT_v3 pdf-page 364): the headword «کافور، بر وزن ناسور، معروف» with the definition «رستنیی است و آن دو قسم می\u200cباشد: یکی از درخت حاصل می\u200cشود …», and Mo'in's footnote 4 «نام فارسی ـ عربی مأخوذ از سان")

('data/verification/page-90.json', 'BQT:270', 'supports', "BQT_v1_pages.txt leaf 490 (printed p.270), Mo'in's footnote 5 on بریدن: '… پهلوی …، سانسکریت …«بارتولمه»؛ قطع کردن، جدا کردن' — an etymological footnote that cites Bartholomae for the Old-Iranian antecedent.")

('data/verification/page-90.json', 'BQT:270', 'supports', "BQT_v1_pages.txt leaf 490 = printed p.270, Mo'in's footnote 5: 'بریدن — بضم اول و فتح چهارم و تخفیف و تشدید دوم (هردو) … سانسکریت … «بارتولمه» ؛ قطع کردن، جدا کردن — عبور کردن، گذشتن'.")

('data/verification/page-90.json', 'BQT:231', 'partial', "BQT_v1_pages.txt leaf 451 = printed p.231 is the ببر entry ('… جانوری باشد صحرایی شبیه بگربه لیکن دم ندارد و از پوست آن پوستین سازند … و بسکون ثانی نام درنده\u200cای است مشهور'), i.e. babar 'beaver-like animal' vs babr 'tiger")

('data/verification/page-90.json', 'BQT:314', 'supports', "BQT_v1_pages.txt leaf 534 = printed p.314, Mo'in's footnote 2 on بور: 'روباه، اسب سرخ قهوه\u200cای؛ سانسکریت babhru- (سرخ قهوه\u200cای) «اسفا ۱:۲ ص ۴۹»؛ اوستا bawra اساساً بمعنی سرخ (در تداول عوام بور شدن، یعنی سرخ و خجل شدن) است ")
```


## [2026-09-06T21:45:11.877Z] TOOL CALL #44: Bash

```json
{
 "command": "grep -ho \"BQT_v2_pages.txt leaf [0-9]* = printed p\\. *[0-9]*\" data/verification/page-*.json | sort -u | head -20",
 "description": "Find BQT v2 leaf offset from prior work"
}
```


### [2026-09-06T21:45:11.930Z] TOOL RESULT

```
BQT_v2_pages.txt leaf 173 = printed p.715
BQT_v2_pages.txt leaf 283 = printed p.823
BQT_v2_pages.txt leaf 298 = printed p.838
BQT_v2_pages.txt leaf 305 = printed p.845
BQT_v2_pages.txt leaf 307 = printed p.847
BQT_v2_pages.txt leaf 308 = printed p.848
BQT_v2_pages.txt leaf 311 = printed p. 851
BQT_v2_pages.txt leaf 333 = printed p.873
BQT_v2_pages.txt leaf 336 = printed p.876
BQT_v2_pages.txt leaf 338 = printed p. 878
BQT_v2_pages.txt leaf 348 = printed p.888
BQT_v2_pages.txt leaf 362 = printed p.902
BQT_v2_pages.txt leaf 368 = printed p.908
BQT_v2_pages.txt leaf 374 = printed p. 914
BQT_v2_pages.txt leaf 378 = printed p. 918
```


## [2026-09-06T21:45:17.527Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (535,555):\n    print('=== leaf',i,'printed',i+540,'===')\n    print(leaves[i][:700])\nEOF",
 "description": "Print Borhan printed pages 1075 and 1095"
}
```


### [2026-09-06T21:45:19.429Z] TOOL RESULT

```
=== leaf 535 printed 1075 ===
  ‫سالار‬                                                                                         ‫س‬
                                                                                                ‫باباه‬
                                                                                                    ‫سم‬
          ‫ررشد را لگزوبند ‪.‬‬
                          ‫مپی‬
                            ‫وو‬‫صادق ‪-‬‬
‫ساك ‪ - ۴‬بروزن پاك‪ .‬بمعنی فسخ‌باشد‬                                                     ‫قوت ناه دهف‪.‬‬

 ‫معتی جپل وضمف وفاد رای‬
                      ‫و فخ در لبفت‬                 ‫ساطل ‪ -‬بکر طای‌حطی ‪ ۰‬مفرب‌ساتل‬
 ‫وتسان است ؛ و درطریق اهل تناسخ آن‌است که‬          ‫با
=== leaf 555 printed 1095 ===
  ‫سییفه‌داز‬                                                                                                ‫‪۱۱۳‬‬
                            ‫د‪.‬‬
                             ‫نرا‬
                               ‫یتال‬
                                  ‫وابس‬
                                     ‫گل ت‬
                                        ‫کر‪ .‬قص‬            ‫بیاش خواند ‪ - ۱‬و نام قلعه و حصاری باشد از‬

                                                          ‫توران که سهراب ين رستم گرفت ت وتامدیوی که‬
‫سپیف بر = بابای فارسی بر وزن سفید‬
                                                               ‫رستم کشت ‪ -‬ورنوادمخانه‌ای هم هت ‪. ۴‬‬
         ‫نقند‪.‬‬
             ‫ا پثش
```


## [2026-09-06T21:45:26.627Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nL=leaves[367]\nimport re\ni=L.find('کالبد')\nprint(L[max(0,i-1500):i+1500])\nEOF",
 "description": "Read Borhan kalbod entry OCR"
}
```


### [2026-09-06T21:45:28.366Z] TOOL RESULT

```
[pdf page 368]
‎—\eve—‏ کالجوش
کویندکه ‎Ge‏ باشد ‎ASE ASH, ٩‏ |
‎oly!‏ مقدار باشد که اسب وآدم لتواند چست -
و تخته سنك تنك و ‎SW‏ را ‎SaaS js‏ بر
روی مردروهای(۱) زیرحمام وجوبهایآب‌پوشند.
کالاشکن ۴ ه بسکون شین تقطمدار
وفتح‌کاف بروزن وا داشتن » لوعی از حلواباشد .
کالب ۴ » بر وزن و معنی قالب است

‏که آنرا کالبد نیز گویند .
‎gee TAIT‏ با وسکون‌دال ‎ion!‏
‏بمعنیکالب (۲) است که قالب هر چیز باشد -
وبمعنی تن وبدنآدمی وحیوانات دیگرنیزهست؛

‏ویفتح بای ابجد هم گفته‌اند .
کالبوی ‎٩‏ - با بای ابجد بواورسیده

‏(۱) چش: مروررودهای . (۲) چش : قالب .

‏وتحتانی زده ؛بععنی س رکشته و متحیر و حیران
باشد - و بمعنی نادان وهیجمبان همآمدماست؛
وبحذف نحتالی‌هم درست‌است که بروزن هزبوباشد.
کالچاه ۱ = باجي ‎BL‏ کید ,
بلفت ‎OS‏ بروزن ومعنی‌کارزار است که ‎Kee‏
‏وجدال ‎ath‏ - ومزرعةً برج را نی زگوبند۷ .
کال‌جوش - باجم بروزن‌تالپوش,
‎gy!‏ ازماحض باشد که دروبشان پزند وآن‌چنان
باشد که تالرا ریزه کنند همجتان که پرای‌اکنه
ریزه میکنند وکشك باب نرم کرده رابا روغن
‎duly‏ قلفل وزیرء و منز کردکان و ‎Bal‏ ریزء
کرده درديك ریز ند ودوسه جوشی داده‌فرود آرند
وخورند ۸ .

‏۱ « درمیان مردم خراسان مثل است که جابی که کالار است هیزم نیست و ‎ile‏ که
هیزم است کالارنیست» ‎only‏ مثل بدان میکوبند که هرجا که کالار باشد هیزم زودتر کنده‌میشود.»
« جهانگیری » ورك : فرهنگ نظام . ۴ کلاشکن ‎Cea)‏
‏برافراختند از قفایش چو باد از کالاشکن سنجق ‎Jue‏ وداد . . بحاق‌اطعمه «فرهنگه تظام».

‏۴ ره :کالید ۰ ۴ - پهلوی 1220 (شکل » صورت) »پازنت2[000ع1,
مستمار از بوتانی ‎kalopédhion‏ (قالب) . ارمتی ‎kalapar‏ از ‎kalapadh‏ ۵ سریبانی ع
0 عربی قال * نیب رکك ص۱۱۸ ۰« اسشق ص ۲۸۲ ۲ در اوراق مانوی بیهلوی 1۳10/0
‎IG)‏ » وضم ۰ جم) . ( هنینگ . فهرست لفات پارسی‌میانه. 13505 ‎Cty . 1 TX.‏

‏۵ _ مسحف «کالیو» س کالیوه (هیم.) ...۰ ‎"٩‏ کالیجار ‏ کالنجار . موستی در
نام ‎be‏ ابر آفی (ی ۱۵۳ ) «کالنجار» را ازاصل « کالجار» کیلکی و 2۳108۲ پهلوی و کارزار
فارسی و ‎kalinjarai‏ سانس
```


## [2026-09-06T21:45:45.110Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['MON'],ensure_ascii=False,indent=1))\" | head -40",
 "description": "MON offsets"
}
```


### [2026-09-06T21:45:47.032Z] TOOL RESULT

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


## [2026-09-06T21:45:52.540Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in dc77dd0c4928d951 a00262bb979c7d55 34ee3685af824f51; do echo \"########## $f\"; sed -n '1,5p' $f.txt; grep -n -A12 \"فرهنگ معین\" $f.txt | head -30; echo; done",
 "description": "Read abadis Mo'in entries"
}
```


### [2026-09-06T21:45:54.501Z] TOOL RESULT

```
########## dc77dd0c4928d951
URL: https://abadis.ir/fatofa/کالا/
FETCHED: 2026-09-06T21:43:41Z
STATUS: 200
TITLE: کالا - معنی در دیکشنری آبادیس

46: فرهنگ معین
47-
48- (اِ. ) اسباب ، متاع . 
49-
50- فرهنگ عمید
51-
52- ۱. (اقتصاد ) متاع، مال التجاره.
53-۲. [قدیمی] مال.
54-۳. [قدیمی] مجموع مهره های شطرنج. 
55-
56- گویش مازنی
57-
58- /kaalaa/ کلاه
--
178: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
179-
180- لینک ها 
181-
182- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
183-
184- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
185-
186- © 2006-2026 abadis.ir

########## a00262bb979c7d55
URL: https://abadis.ir/fatofa/کالبد/
FETCHED: 2026-09-06T21:43:43Z
STATUS: 200
TITLE: کالبد - معنی در دیکشنری آبادیس

57: فرهنگ معین
58-
59- (بُ یا بَ ) [ په . ] (اِ. ) ۱ - قالب هر چیز. ۲ - تن و بدن آدمی . ۳ - نمونه ، سرمشق . 
60-
61- فرهنگ عمید
62-
63- ۱. طرحی که چیزی در آن شکل می گیرد، قالب، تن، بدن.
64-۲. [قدیمی] قالبی برای ساختن خشت و آجر: از تن چو برفت جان پاک من و تو / خشتی دو نهند بر مغاک من و تو و آنگاه برای خشت گور دگران / در کالبدی کشند خاک من و تو (خیام: ۱۰۳ ). 
65-
66- جدول کلمات
67-
68- جسد 
69-
--
148: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
149-
150- لینک ها 
151-
152- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
153-
154- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
155-
156- © 2006-2026 abadis.ir

########## 34ee3685af824f51
URL: https://abadis.ir/fatofa/قالب/
FETCHED: 2026-09-06T21:43:44Z
STATUS: 200
TITLE: قالب - معنی در دیکشنری آبادیس

67: فرهنگ معین
68-
69- (لِ ) [ معر. ] (اِ. ) ۱ - پیکر، هیکل . ۲ - شکل ، هیئت . ۳ - آلتی که جسمی شکل پذیر را در داخل یا خارج آن نهاده به صورت آن آلت درآورند، قالب کفش . ۴ - واحدی برای قطعات بریدة معین ، قالب پنیر. ۵ - جزو، رکن (علم عروض ). ، ~تهی کردن الف - بی نهایت ترسیدن . ب 
70-
71- فرهنگ عمید
72-
73- ۱. ظرفی که در آن فلز گداخته یا چیز دیگر را می ریزند تا به شکل و اندازۀ آن درآید.
74-۲. تکۀ چوب تراشیده به اندازۀ پای انسان که درون کفش می گذارند.
75-۳. شکل، هیبت.
76-۴. جسم، تن، بدن، کالبد.
77-۵. واحد شمارش برای قطعات بریده شده از قبیل صابون و کره.
78-* قالب تهی کردن: [مجاز] مردن.
79-* قالب زدن: (مصدر متعدی )
--
268: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
269-
270- لینک ها 
271-
272- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
273-
274- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
275-
276- © 2006-2026 abadis.ir
```


## [2026-09-06T21:46:08.713Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/کالیبر/\" \"https://abadis.ir/fatofa/قفقاز/\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 283: Persian kālibr (French loan) and Qafqāz\"; done",
 "description": "Archive abadis kalibr and qafqaz"
}
```


## [2026-09-06T21:46:10.884Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN kalb ==\"; grep -n -i \"kalbud\\|kalbad\\|kalput\\|kalopod\" HRN.txt | head; echo \"== ARY latin index ==\"; grep -n -i \"KALBOD\\|KALBAD\\|KALA\\b\" incoming/ARY/ARY_latin_index_pages.txt | head; echo \"== ARY persian ==\"; grep -n \"کالبد\\|کالا \" incoming/ARY/ARY_pages.txt | head",
 "description": "Grep Horn and Aryanpur"
}
```


### [2026-09-06T21:46:13.872Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/62974c6c76407ba8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9e150cad084c0e5.txt
```


### [2026-09-06T21:46:13.938Z] TOOL RESULT

```
== HRN kalb ==
10693:kalput^ vd. 5 (32) Gl., ys. 9 (46), Bhmyt., kürpat bezw.
== ARY latin index ==
691:02S ES Ue ead 99 pd oben WT AUT 5 JS Kala hee aula J feeb ose 4
5169:PYSK, PYKAC (POLISH) ging) PUSTI-, PUSKALA-
11924:CORNACCHIA A(TALIAN) gids! KALA KURDISH) 62
12242:HWAN — (OLD SAXON) pS ig Se KALA AFGHANI) (4) gli}
== ARY persian ==
```


## [2026-09-06T21:46:18.802Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10685,10700p' HRN.txt; echo \"=== leaf\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read();lines=t.split('\\n')\nprint('leaf',('\\n'.join(lines[:10693])).count('\\f'))\"",
 "description": "Read Horn kalput context"
}
```


## [2026-09-06T21:46:20.435Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 62974c6c76407ba8 b9e150cad084c0e5; do echo \"#### $f\"; sed -n '1,5p' $f.txt; grep -n -A8 \"فرهنگ معین\\|لغت نامه دهخدا\" $f.txt | head -40; done",
 "description": "Read abadis kalibr and qafqaz"
}
```


### [2026-09-06T21:46:20.766Z] TOOL RESULT

```
122. karlnttan 'schneiden; schaffen (von Anröniainyuä)',
karm(i)sn (Aw.-Komm., Bund.), päz. /arnldaii.
aw. iXAar^-, kerentaiti 'schneiden; schaffen'; ai.
\/^kart-, kpitäti.
Hierher wohl auch phlv. kartak 'Capitel, Ahschnitf.
123. karp 'Körper* (päz. karaf), arm. LW. kerp fiogtfi}.
aw. kerp- 'Körper*; ai. kfp-; lat. corpus.
np. kcUbud, kälbed 'Form, Körper , phlv. kärf)ut bezw.
kalput^ vd. 5 (32) Gl., ys. 9 (46), Bhmyt., kürpat bezw.
kälpat, Men. (päz. kälbüd) ist gr. ^aXonodioi' 'Schuster-
^) West: *broken', doch scheint 'gefallen* besser zu passen.— 283 —
leisten', wie Fleischer schon längst gesehen hat
(vergl. Nöldeke, Pers. Stud. II, 38)^).
124. ha» 'Glocke, nur vd. U (48).
aw. kqstra^ 'Glocke*.
125. katär 'welcher von beiden?' (AW.-Komm., AV.).
=== leaf
leaf 303
```


### [2026-09-06T21:46:22.649Z] TOOL RESULT

```
#### 62974c6c76407ba8
URL: https://abadis.ir/fatofa/کالیبر/
FETCHED: 2026-09-06T21:46:12Z
STATUS: 200
TITLE: کالیبر - معنی در دیکشنری آبادیس

17: لغت نامه دهخدا
18-
19- کالیبر. ( فرانسوی ، اِ ) بمعنی قطر درونی استوانه. قطر درونی احجام استوانه ای : کالیبر لوله تپانچه ، کالیبر لوله تفنگ و توپ و غیره. 
20-
21- فرهنگ فارسی
22-
23- اندازه، قالب، قطردهانه لوله، دوره دهانه لوله توپ یاتفنگ یاتپانچه
24-( اسم ) ۱ - قطر درونی احجام استوانه یی . ۲ - قطر دهان. لول. اسلح. گرم ( تپانچه تفنگ توپ ) . 
25-
26: فرهنگ معین
27-
28- (بْ ) [ فر. ] (اِمر. ) قطر دهانة لولة توپ یا تفنگ . 
29-
30- فرهنگ عمید
31-
32- قطر داخلی لولۀ اسلحه. 
33-
34- دانشنامه عمومی
--
157: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
158-
159- لینک ها 
160-
161- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
162-
163- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
164-
165- © 2006-2026 abadis.ir
#### b9e150cad084c0e5
URL: https://abadis.ir/fatofa/قفقاز/
FETCHED: 2026-09-06T21:46:13Z
STATUS: 200
TITLE: قفقاز - معنی در دیکشنری آبادیس

17: لغت نامه دهخدا
18-
19- قفقاز. [ ق َ ] ( اِخ ) نام ناحیه ای است بین دریای سیاه و بحر خزر که در حدود 154250 میل مربع مساحت دارد و جمعیت آن بالغ بر 14410000 تن است. فاصله آن از منتهی الیه جنوب شرقی تا منتهی الیه شمال غربی 750 میل است ، یعنی از شبه جزیره اپشرون تا دهانه رودخانه کوبان در ساحل دریای سیاه منطقه ٔقفقازیه را سلسله جبال قفقازیه فراگرفته و این سلسله جبال آن را به دو ناحیه این سوی قفقاز و آن سوی قفقاز تقسیم می کند. ناحیه قفقازیه از زمان بسیار قدیم مسکن مردمانی از نژاد قفقازی بوده که مهاجمان بعدی به این مردمان عناصر متعدد دیگری را اضافه کرده است. در قرون وسطی مسیحیت یونانی به این ناحیه نفوذ کرد و قفقاز شرقی بعدها به دین اسلام درآمد، با وجودی که در تحت نفوذ ظاهری ایران و ترکیه بود کم کم مجبور شد که با روسیه پیوند بیابد، روسیه ای که به دست آوردن هشترخان او را به دریای خزر آورده بود، این ناحیه به وسیله روسیه تا کوبان و تِرِک به سال 1774 م. اشغال شد، و سپس فتوحات روس در آنجا ادامه یافت. دربند 1706 م.، باکو 1806 م.، گرجستان 1801 م.، شیروان و قراباغ 1813 م. و ارمنیه 1828 م. اشغال شدند. قبایل کوهستانی قفقاز پس از توقیف فرمانده ِ خود شامیل در 1859 م. تابع دولت روس شدند. ناحیه ای از قفقاز که به حدود دریای سیاه بود به سال 1846 به وسیله روسها محاصره شد. قارص و اردهان و باطوم از طریق ترکیه به روسیه در 1878 واگذار گردید. ناحیه قفقاز جنوبی به واسطه منابع سرشار نفت خود درجنگ بین الملل دوم هدف پیشروی آلمانها بود و آنها تانزدیکی این منابع پیشروی کردند که بعدها قشون آلمان به سال 1943 م. از این منطقه و به طورکلی از ناحیه قفقاز رانده شدند. ( از فرهنگ جغرافیایی وبستر ). اراضی ماوراء قفقاز عبارتند از سه جمهوری آذربایجان ، گرجستان و ارمنستان شوروی و ملحقات آنها که در پانزدهم دسامبر 1922 م. مشترکاً جمهوری فدرال ماوراء قفقاز شوروی سوسیالیستی را به وجود آوردند، و در شانزدهم ژانویه 1923 کنگره ماوراء قفقاز شوروی یک قانون اساسی بدین منظور تنظیم و اتخاذ کرد ولی در سال 1936 این سه جمهوری از یکدیگر مجزا شدند و هر کدام دارای قانون اساسی جداگانه ای گردیدند که در ذیل بیان میشود:
20-جمهوری آذربایجان شوروی : دیر زمانی نیست که یک قسمت از عمده ترین و مهمترین اراضی ماوراء رودخانه ارس از ایران منتزع شده و به حکومت تزاری روسیه واگذار گردیده است. چندین شهر قفقاز در این جریان از دست ایران بیرون رفت و امروز آذربایجان شوروی یکی از جمهوریهای مشخص اتحاد جماهیر شوروی سوسیالیستی میباشد. در 28 ماه مه 1918 مجلس مؤسسان تاتارها که زیر نفوذ حزب ملی آن کشور بود استقلال آذربایجان را اعلام داشت و پایتخت آن را شهر گنجه مقرر داشت که بعداً به باکو منتقل گرداندند. در 28 آوریل 1920 آذربایجان به عنوان یک جمهوری سوسیالیستی و شوروی اعلام گردید و با گرجستان و ارمنستان جمهوری فدرال ماوراء قفقاز را تشکیل دادند ولی در 1936 به عنوان یکی از جمهوریهای اتحاد جماهیر شوروی رسمیت یافت و یک قانون اساسی جداگانه مطابق جماهیر شوروی اتخاذ کرد. آذربایجان شامل 85700 کیلومتر مربع از اراضی بین دو دریای خزر و دریای سیاه می باشد و جمعیت تقریبی آن به چهارمیلیون بالغ میگردد که بیش از دومیلیون آنان ده نشین و بقیه شهرنشین هستند. باکو با جمعیت تقریبی یک میلیون تن از زیباترین و بزرگترین شهرهای قفقاز و یکی از مهمترین بنادر نظامی و اقتصادی دریای خزر محسوب است. آذربایجان شامل جمهوری خودمختار نخجوان و اراضی خودمختار قره باغ است.35 مردم آذربایجان ترک آذربایجانی و بقیه ارامنه و گرجی و روسی هستند. آذربایجان چون در شرق ماوراء قفقاز قرار گرفته از طرف مغرب کوه های سرسخت قفقاز آن را محفوظ داشته و کرانه های سرسبز آن را از جنوب و شرق دریای خزر احاطه کرده است. آب وهوای آذربایجان معتدل است. محصول عمده آن حبوب ، پنبه ، برنج ، شراب و محصولات حیوانی و نباتی است. محصول نفت سالیانه باکو در 1940 در حدود 25میلیون تُن بوده است. مهمترین قسمت نفت خیز آذربایجان در کرانه باختری دریای خزر در شمال و در جنوب باکو میباشد. در نزدیکی شبه جزیره آپشرون چاههای نفت بزرگی در وسط دریا حفر گردیده است. چاههای نفت باکو به وسیله لوله های ضخیم به بندر باطوم در دریای سیاه منتقل می شود و نفت خام آذربایجان در نقاط مختلف قفقاز و در سایر جمهوریهای شوروی مانند اوکراین شرقی تصفیه میگردد. و درعین حال در باکو تمام کارخانجات نفت الکتریکی شده است. صنایع دیگر آذربایجان شامل بهره برداری از معادن مس و نمک و تهیه منسوجات و ماهیگیری در خزر است. از لحاظ نظامی آذربایجان اداری اهمیت کم نظیری است. از ارتفاعات قفقاز میتواند بزرگترین خطوط دفاعی طبیعی را برای اراضی وسیع شمالی به وجود آورد. بیشتر بخوانید ... 
21-
22- فرهنگ فارسی
23-
24- ناحیه ایست واقع بین بحر خزر و بحراسود و آن از جنوب به ایران و ترکیه متصل و از شمال به روسیه محدود است . سرزمینی است کوهستانی که از مغرب تا مشرق کشیده شده (از بحر اسود تا بحر خزر ) و بلندترین قله آن ۵۶۳٠ متر ارتفاع دارد . آب و هوای قفقازیه در زمستان بسیارسرد و در تابستان ملایم و معتدل است . ناحیه مذکور قرنها جزو سرزمین ایران بود و در زمان فتحعلی شاه قاجار بر اثر دو جنگ که منجر بدو معاهده گلستان و ترکمان چای شد ( ۱۲۲۸ و ۱۲۴۳ ه ق . ) خاک قفقازیه بروسیه تزاری واگذار گردید . پس از واژگون شدن حکومت تزاری و تشکیل حکومت شوروی سه جمهوری در قفقازیه بوجود آمده ازین قرار : ۱ - جمهوری آذربایجان ( شوروی ) . ۲ - جمهوری گرجستان . ۳ - جمهوری ارمنستان . مساحت قفقاز ۵٠٠٠٠٠ کیلومتر مربع و جمعیت آن بالغ بر ۱۲ میلیون تن است که مخلوطی از نژادهای ترک و تاتار چرکس لزگی گرجی ایرانی و روسی است . 
25-
--
181: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
182-
183- لینک ها 
184-
185- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
186-
187- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
188-
189- © 2006-2026 abadis.ir
```


## [2026-09-06T21:46:36.406Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Kafkas\" \"https://en.wiktionary.org/wiki/قوقاز\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 283: transmission of Caucasus name into Turkish/Arabic/Persian\"; done",
 "description": "Archive Kafkas and qawqaz"
}
```


## [2026-09-06T21:46:39.436Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD watkins keu burn ==\"; grep -n -i \"keu-\\|kau-\\|caustic\\|holocaust\\|calm\" AHD_watkins1985.txt | head -20; echo \"== LEW cauma ==\"; grep -n -i \"cauma\" LEW_1910.txt LAT.txt | head; echo \"== SKT calm/caustic ==\"; grep -n -i \"^calm\\|^caustic\\|^holocaust\" SKT.txt | head",
 "description": "Grep AHD/LEW/SKT"
}
```


### [2026-09-06T21:46:39.633Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/d2952c1c477e2775.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84d35323ab86d633.txt
```


### [2026-09-06T21:46:39.708Z] TOOL RESULT

```
<persisted-output>
Output too large (30.4KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bnk5o9lll.txt

Preview (first 2KB):
== AHD watkins keu burn ==
100:VENT, CONVENTION, etc.) or Germanic be- (BECALM, BECLOUD) can be shown to be a development of the individual languages af- ter the breakup of the common language. In Indo-European, such “compounds” repre- sented two independent words, a situation still reflected in Hittite and the older San- skrit of the Vedas (the sacred books of the ancient Hindus) and surviving in isolated remnants in Greek and Latin.
590:kau-'. To howl (imitative). 1. Reduplicated suffixed form *ka-kau-ro- in Sanskrit cakorah, partridge: CHUKAR. 2. Reduplicated form *k6-kii-o- in Greek kdkuein, to wail, lament: Cocytus. [Pok. kau- 535.]
591:kau-2, To hew, strike. 1. Germanic *hawwan in: a. Old English héawan, to hew: HEW; b. Old Norse héggva, to cut: HAGGLE; c. Old ‘French hove, a hoe: HOE. 2. Ger- manic *hawwé6 in Old Norse hégg, a gap, a cutting blow, akin to the source of HAG?. 3. Germanic *haujam in Old English hieg, hay, cut grass: HAY. 4. Suffixed form *kau-do- in Latin ciidere (< *caudere), to strike, beat: incus. [Pok. kdu-, 535.]
592:kaul-. Stalk, stem. Latin caulis, stalk, stem, cab- bage-stalk, cabbage: CAULICLE, CAULINE, COLE, KALE; AMPLEXICAUL, CAULESCENT, CAULIFLOWER, COLCAN- NON, COLESLAW, KAILYARD SCHOOL, KOHLRABI. [Pok. kau-l- 537.)
622:keu-?
...
</persisted-output>
```


## [2026-09-06T21:46:43.182Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"kaustos\\|kaiein\\|caustic\" AHD_watkins1985.txt | head -10; echo \"---- keu2 area\"; sed -n '620,626p' AHD_watkins1985.txt; echo \"==== LEW/LAT cauma\"; grep -n -i \"cauma\" LEW_1910.txt LAT.txt | head",
 "description": "Look for kaiein in Watkins"
}
```


### [2026-09-06T21:46:43.254Z] TOOL RESULT

```
626:kéu-. To burn, Zero-grade form *kau- becoming *kaw- in suffixed form *kaw-yo- in Greek kaiein, to burn: CALM, CAUSTIC, CAUTERY; ENCAUSTIC, HOLOCAUST, (INK). [Pok. 2, kéu- 595.]
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
---- keu2 area
ker-*
hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
keu-?
(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
kéu- 31
DECUMBENT, INCUMBENT, PROCUMBENT, RECUMBENT, SUCCUMB (ii) Greek kumbé, boat, bowl: (CEMBALO), (CHIME!), CYMBAL, CYMBIDIUM; d. aspirated long-vowel form *kiibh- in Greek Ruphos, bent: KYPHOSIS. II. Ex- tended o-grade form *kouk-. 1. Suffixed form *kouk-o- in: a. Germanic *hauhaz, “arched,” high, in Old English héah, high: HIGH; b. Germanic *hauhitho in Old English héhthu, héahthu, height: HEIGHT. 2. Germanic *huk- in: a. Middle Low German héken, to bend, squat, bear on the back, peddle: HAWKER; b. Old Norse hokra, to crouch, akin to the Scandinavian source of HUNKER; c. Middle Dutch hokester, “one who squats,” peddler, perhaps akin to the source of Middle English hukster, peddler: HUCKSTER. III. Reduplicated form *ka-ku-bh- in Latin caciimen, summit, point (< “arch, vault’): CACUMINAL. [Pok. 2. keu- 588.]
kéu-. To burn, Zero-grade form *kau- becoming *kaw- in suffixed form *kaw-yo- in Greek kaiein, to burn: CALM, CAUSTIC, CAUTERY; ENCAUSTIC, HOLOCAUST, (INK). [Pok. 2, kéu- 595.]
==== LEW/LAT cauma
LAT.txt:10578:cauma, -atls n.: forte chaleur. Emprunt fait par la 1 . de l']£gl.
```


## [2026-09-06T21:46:52.267Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10576,10582p' LAT.txt; echo \"== leaf\"; python3 -c \"\nt=open('LAT.txt',encoding='utf-8',errors='replace').read();lines=t.split('\\n');print('leaf',('\\n'.join(lines[:10578])).count('\\f'))\"\necho \"########\"; cd ../web && for f in d2952c1c477e2775 84d35323ab86d633; do echo \"#### $f\"; sed -n '4p' $f.txt; grep -n -m4 -A6 \"^ Etymology\" $f.txt | grep -v \"^\\s*[0-9]*[-:]\\s*$\" | head -30; done",
 "description": "Read Ernout-Meillet cauma and Kafkas/qawqaz"
}
```


### [2026-09-06T21:46:53.764Z] TOOL RESULT

```
lette kauls "tige, oa", v. pruss. kaulan et lit. kdulas "os". Un emprunt
au grec (Varr. L.L.5,103) est peu vraisemblable.
cauma, -atls n.: forte chaleur. Emprunt fait par la 1 . de l']£gl.
au gr. xaup/x. M.1.1779.- ,
caupo, -onls m .(copo, et tardif cupo; cf. aussi Isid., Or.30,6,7,
cupos et cupas a capiendo, i.e. accipiendo aquas uel uinum uocatas,
unde et copones); cabaretier, aubergiste. Atteste depuis Plaute.
== leaf
leaf 209
########
#### d2952c1c477e2775
TITLE: Kafkas - Wiktionary, the free dictionary
73: Etymology 1 
75- 2.1.1 
76- Noun 
78- 2.1.1.1 
79- Declension 
--
85: Etymology 2 
87- 2.2.1 
88- Proper noun 
90- 2.3 
91- References 
--
175: Etymology 1
176- [ edit ] 
178- Inherited from Ottoman Turkish قافقاس ( kafkas ) .
180- Noun
181- [ edit ] 
--
249: Etymology 2
250- [ edit ] 
252- From West Circassian Къэфкъас ( Qɛfqas ) , from Ancient Greek Καύκασος ( Kaúkasos ) . This is a modern neo-Circassian name adopted by the diaspora in Turkey to honor their homeland. Its specific usage as a personal given name is a modern phenomenon unique to the Caucasian diaspora, rather than a historical or traditional Circassian name.
254- Proper noun
255- [ edit ] 
#### 84d35323ab86d633
TITLE:
```


## [2026-09-06T21:47:11.298Z] TOOL CALL #57: Bash

```json
{
 "command": "ls site/pages/283.jpg 2>/dev/null; pdftoppm -f 283 -l 283 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg283\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\"",
 "description": "Render PDF page 283"
}
```


### [2026-09-06T21:47:13.456Z] TOOL RESULT

```
site/pages/283.jpg
total 24340
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:47 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     528 Sep  6 17:44 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb   97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1174 Sep  6 17:16 c_empty.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb   41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51778 Sep  6 17:32 mk276.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3647 Sep  6 17:34 p279_xsaeta.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74784 Sep  6 17:47 pg283.png
```


## [2026-09-06T21:47:16.374Z] TOOL CALL #58: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg283.png"
}
```


### [2026-09-06T21:47:16.704Z] TOOL RESULT

```

```


## [2026-09-06T21:47:16.699Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:47:43.152Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"Calm\" \"Holocaust\" \"Caliber\" \"Calibre\" \"Caustic\"; do echo \"== $w\"; grep -n -i -m2 \"^$w[,.]\\| $w[,.] *\\(s\\.\\|adj\\|n\\.\\)\" SKT.txt | head -3; done; echo \"=== SKT loose\"; grep -n -i -m3 \"calm\\b\" SKT.txt | head -5; echo \"=== WEB cauma/calibre\"; grep -n -i -m2 \"cauma\" WEB_vol1.txt | head -3",
 "description": "Grep Skeat and Webster"
}
```


### [2026-09-06T21:47:44.756Z] TOOL RESULT

```
== Calm
(eval):1: bad math expression: empty string
== Holocaust
(eval):1: bad math expression: empty string
== Caliber
(eval):1: bad math expression: empty string
== Calibre
(eval):1: bad math expression: empty string
== Caustic
(eval):1: bad math expression: empty string
=== SKT loose
613:Amber.   (F.  -  Span.  —  Arab (iw/«^nr.  — F.flwi5«f.— Span.  dmAar.  —  Anfc. 'as^bar  (prcMiounced  'aminxr'],  om!tr';;n*.  a rich  pcrlume.    ^Thc  resinous  .ti so  called  from  a  resemblance  to  .-^^ which  is  really  quite  a  cUffercnt  suM-...in.r. ambergris,  i.e.  gray  amber.    CalM gris  amber  in  Milton,  P.  K.  ii.  344.     ^ F.  gris,  gray,  is  from  O-  H.  G,  /rtx,  ptjf cf.  G.  grtis,  hoary.
5336:1  ill  dorrcr^  a .-•Irtl.  j'.ii/',  tcnumbefl, alumber,  diita^  to  ••U-cp. '  calm ;  Mtid  »cc  Duae. .— L)  F.  dorsal,  belonging •Xx>w  L>  dMrsalU,^  L.  dptium,
8267:Halcyon,  a  kingfisher;  as  adj.  serene. (L.  —  Gk,)  Halcyon  days  =  calm  days; it  was  supposed  lliat  (be  weather  was  calm when  king'lUbers  were  breeding.  «i  L. halcyon,  aUyon,  a  king-fi!)ber.«*Gk.  aAiruwr, dAxvan*,  a  king  fisher.  Allied  to  L.  akeJo, ihe  true  L.  name.
=== WEB cauma/calibre
26644:cal’lus, v.i. to develop a callus. cilm (kim), n. [Fr. calme; LL. cauma, the heat
```


## [2026-09-06T21:47:50.191Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26644p' WEB_vol1.txt | cut -c1-600; echo \"=== caliber\"; grep -n -i -m2 \"cal’i-ber\\|caliber (kal\\|cal’i-bre\" WEB_vol1.txt | cut -c1-600; echo \"=== holocaust\"; grep -n -i -m2 \"hol’o-caust\\|holocaust (hol\" WEB_vol1.txt | cut -c1-500",
 "description": "Read Webster entries"
}
```


### [2026-09-06T21:47:50.287Z] TOOL RESULT

```
cal’lus, v.i. to develop a callus. cilm (kim), n. [Fr. calme; LL. cauma, the heat
=== caliber
26452:cal/i-bér, cal’i-bre, n. [Fr. calibre, perh. from L. qua libra, what pound, weight, size.]
=== holocaust
```


## [2026-09-06T21:47:53.563Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26645,26647p' WEB_vol1.txt | cut -c1-500; echo \"=== 26452\"; sed -n '26452,26453p' WEB_vol1.txt | cut -c1-500",
 "description": "More Webster context"
}
```


### [2026-09-06T21:47:53.650Z] TOOL RESULT

```
of the sun; Gr. kauma, from kaiein, to burn; probably from the period of rest, during mid- day.] lack of motion, agitation, or disturb- ance; stillness; tranquillity; quiet.
The soul as even as a calm. —Shak.
cilm, a.; comp. calmer; superl. calmest, 1.
=== 26452
cal/i-bér, cal’i-bre, n. [Fr. calibre, perh. from L. qua libra, what pound, weight, size.]
1. the size of a bullet or shell as measured by its diameter.
```


## [2026-09-06T21:48:17.675Z] TOOL CALL #62: Bash

```json
{
 "command": "SD=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 - <<EOF\nfrom PIL import Image\nim=Image.open(\"$SD/pg283.png\")\nprint(im.size)\nim.crop((330,380,900,700)).resize((1140,640)).save(\"$SD/p283_arrow.png\")\nEOF\nls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p283_arrow.png",
 "description": "Crop arrow region"
}
```


### [2026-09-06T21:48:19.775Z] TOOL RESULT

```
(1700, 2200)
-rw-rw-r-- 1 sfmqrb sfmqrb 130651 Sep  6 17:48 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p283_arrow.png
```


## [2026-09-06T21:48:22.268Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p283_arrow.png"
}
```


### [2026-09-06T21:48:22.287Z] TOOL RESULT

```

```


## [2026-09-06T21:48:38.298Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\n# find leaf containing 'kaFsAov' or 'brennen' with kau\nfor i,L in enumerate(leaves):\n    if 'xaico' in L or 'kaiein' in L or ('kule' in L and 'brenn' in L):\n        print(i, L[:120].replace('\\n',' '))\nEOF\ngrep -n \"376\" /dev/null",
 "description": "Locate Walde-Pokorny Bd I p.376"
}
```


### [2026-09-06T21:48:40.039Z] TOOL RESULT

```
leaves 895
```


## [2026-09-06T21:48:46.555Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\n# guess offset: find leaf whose text contains standalone page number 376\nfor i,L in enumerate(leaves):\n    if re.search(r'(?m)^\\s*376\\s*$',L) or L.strip().startswith('376'):\n        print('cand leaf',i, L[:100].replace('\\n',' '))\nEOF",
 "description": "Find WLD Bd1 page 376"
}
```


### [2026-09-06T21:48:48.390Z] TOOL RESULT

```
cand leaf 384 376                                       qeu-   — ken-,   (:   kau-, ku-)      ai.   kumba-h „das d
```


## [2026-09-06T21:48:52.442Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nL=leaves[384]\ni=L.find('kau-')\nprint(L[:2600])\nEOF",
 "description": "Print WLD Bd I p.376"
}
```


### [2026-09-06T21:48:54.222Z] TOOL RESULT

```
376                                       qeu-   — ken-,   (:   kau-, ku-)



  ai.   kumba-h „das dicke Ende (eines Knochens); hervorragendes, weib-
licher   Kopfputzi?)“; ai. kiimbha-li „Topf, Krug“, Du. „die beiden Er-
hohungen auf der Stiru des Elefanten“ = av. xmnba- m. „Topf, Yertiefung“,
np. xitmb, xum ./Topf, Krug“ (diese mit aril. Tenuis asp.);
   gr. y.vuBy .Beeken, Schale, Kahn“, xvufiog .,GefaB“; xvpftiov „GefaB,
                       ,


Fahrzeug“ trotz Petersson IP. 34, 249 nicht mit einem Formans -mho- zu
                   ,




y.vag usw., Wz. keu-\ xvf.ipa.Xov, meist PI. „cymbalum, Beeken, das mit
einem andern zusammengeschlagen einen gellenden Ton gibt“, avaxvfx^a-
X.i^etv „klirrend umkippen, yon \Yagen“ (Curtius 158'.

   xv/xfii} ,.Kopf, y.v<ptf‘ EM., Suid., xv/.ipayog (£ 586;
                                                                                                                        1'
                                                            kopfiiber fallend                        ,


(vgl. dvaxv ypaXtgetv) und (0 536) „Spitze eines IIelmes“ (als ,,der sich
iiberneigende“? oder „Helm“ = ,,topfformiges“? zur Bildung s. Bechtel Lex.
209)    ;
            lat.   (mit praesentischer Nasalierung) -cumbo                             (s. o,).

   Mir. comm „GefiiB“, cummal „Beeher, Schale“, cymr. cwrnm „Tal“ (m.),
bret. komb, kombunt koumbant „Tal“, komm ,,Trog“ (m., gall, cumba ON.,
                                 ,


eigentlieb „Tal“ (vgl. zu     den kelt. AYorten Fickll 4 93, wo aber an die
Bed. von lat. cumbere, sab. cumba ,,lectiea“ erinnert wird vielmehr,, *Mulde“;                   ;


Pedersen KZ. 39, 3S0, KG. I 119, Stokes KZ. 40, 247 gall, cumba c. cwmm                     ;                       ,

nicht nach Zupitza Gutt. 55 zu aisl. haammr „Abhang, Tal“, aschwed. hwam -
ber ds., ags. hwamm „Winkel, Eeke", hivemman „biegen, kriimmen" und
lit. dtkvampte „Seitenlehne“, deren Yerwandtschaft auch untereinander nicht

feststeht).  Ygl. die unnas. GefaBbezeichnungen pam. kubun, poln. kubek
auch gr. y.vpjog „TOvftfaov“.

qeu- „wackeln“.
   Lat. ecceo, -ere ,wackeln; wie ein wedelnder Hund schmeicheln"; abg.
po-kyva-jq.      (hauptsachlich mit glavq) „den Kopf scbiitteln, nicken“,
                           -ti

cech. kyvati „winken, nicken, wedeln, bewegen, schiitteln" (usw. s. Ber-
neker 679 f.), W. Meyer(-Liibke) KZ. 28, 173. Aber ganz fraglich got,
skewjan „wandern“, aisl. skeeva „gehn“, abl. holl. schooien „umherwandern,
fortlaufen; betteln" (*skaujan ;germ. Zubehor noch bei Falk-Torp u. sktfi),
Schroder Abl. 64 f.
```


## [2026-09-06T21:49:00.915Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[385][:1500])\nEOF",
 "description": "Print WLD Bd I p.377"
}
```


### [2026-09-06T21:49:03.141Z] TOOL RESULT

```
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
LEWb. 2 307 nicht wahrscheinlicher stellt Thurneysen Thes. fur caurus
                       ;


Zugehorigkeit zu caurio zur Wahl, wodurch fiirs Bsl. auch Anlaut
```


## [2026-09-06T21:49:08.484Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[384][2500:5200])\nEOF",
 "description": "Print rest of WLD p.376"
}
```


### [2026-09-06T21:49:10.276Z] TOOL RESULT

```
ern,
fortlaufen; betteln" (*skaujan ;germ. Zubehor noch bei Falk-Torp u. sktfi),
Schroder Abl. 64 f., da in der Bed. wenigstens nicht unmittelbar ent-
sprechend und auch im s- zur Yorsicht mahnend (s. iiber diese noch nicht
zuverlassig gedeutete germ. Sippe auch unter sqeq- ,springen“). Auch die                ;

Beziehung zu lit. kuteti aufiiitteln“, dt. scJiiitteln usw. (s. sqeut-; Zupitza
                                     ,;

Gutt. 56, 121, Vf. LE\Yb. 2 u. ceveo )                 ist      mindestens ganz fraglich.

keu-        (:   kau-, ku-) ,,anziinden, verbrennen'               1
                                                                       .


    Gr. yarn (jon.), y.dw (att.) aus *xaf-ia> ,.ziinde an, brenne an“, aor. horn
e >irl(f) a t altatt. Gen. sg. xidvxog                                med. episch
                                       ( *y.t]favT -), neuatt. exavoa                                       ,


y.rjdiirjv ,     pass, ixayv, sxav&rjv , delph. xrjia „§ooia“,
                                                           xadaouaxa und                        xi'/ta'

y.Eta ds. Hes., bom. xycbdyg „duftig,  wohlrieehend“ (von einem *xrjfog
 Brand, Rauchenverk“ Solmsen Unt. 124 f.) xavmg xav/ua, xdXov „trockenes
                                                                   ,              ,

Holz“ (*xa^-eXov), aol. xavaXeog „brennend heifi“; hom. xyXeog ( *y.a$aXeog )
usw.,       s.   Boisacq 393 f. ; dazu wahrscheinlich                      lit.       kiilcti            „brandig werden,
vom Getreide*’, kulS „Getreidebrand“ (Uhlenbeck Ai. Wb. 63; aber ai. kH~
Idyuti,k tulayat i „versengt‘ als *kr-d- zu ker- „brennen“, s. Wackernagel
                                          £




Ai. Gr. I 169, Boisacq aaO. und vgl. ai. knvlayali Jrrennt")     zu den auf                                     ;
```


## [2026-09-06T21:50:08.110Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFM qalib ==\"; grep -n \"قالب\\|كالبد\" AFM_pages.txt | head -5; echo \"== LEW crusta/Caucas ==\"; grep -n -i \"caucas\" LEW_1910.txt LAT.txt | head -5; echo \"== FVQ qalib ==\"; grep -n -i \"qalib\\|qālib\" FVQ.txt | head -3; echo \"== LKT kaliber ==\"; grep -n -i \"kaliber\\|calibre\" LKT.txt | head -5",
 "description": "Grep Addi Shir, Walde LEW, Jeffery, Lokotsch"
}
```


### [2026-09-06T21:50:08.197Z] TOOL RESULT

```
== AFM qalib ==
== LEW crusta/Caucas ==
== FVQ qalib ==
== LKT kaliber ==
674:Aus  tk.  hal  'Honig'  und  bas  'Kopf, eigentlich  'Honigkopf',  hieraus  rum. balba^,  baba§  'Honigwasser'.  —  Aus  tk. balgy  'Honigverkäufer'  wird  rum.  balgiü 'dass.'.  —  Tk.  bal-jemez  'der  nicht  Honig ißt  oder  frißt'  ist  Bezeichnung  für  ein Geschütz  großen  Kalibers,  vgl.  v.  Moltke, Briefe  über  Zustände  und  Begebenheiten in  der  Türkei.^  1876.  S.  260  im  Briefe vom  12.  Mai  08.  Hieraus  rum.  balimez, baliemez  'großkalibriges  Geschütz'.  Hier- von kommt  sicherlich  auch  der  luia. Ausdruck  a  face  talme§  bahiief  'krumm und  lahm  schlagen'.
2454:'Leisten  eines  Schusters',  ebenso  tk. kalyh,  Icahjp  'Modell,  Form';  hieraus rum.  calib,  calip,  calup  'Gießform,  Mo- dell, Leiste',  calupciü  'Betrüger';  aus dem  Ar.  unmittelbar  sp.  gälibo  'Schiffs- modell', frz.  gabarit;  asp.  calibo,  sp. calibre,  frz.  calibre  'Durchmesser  der Mündung  eines  Geschützes,  Gewicht  der Kugel';  it.  coUbro  'Maßinstrument,  um die  Zusammengehörigkeit  von  Geschütz und  Geschoß  zu  bestimmen';  dtsch. Kaliber,  engl,  calibre  [amerikanische Schreibung  caliber,  s.  Herrigs  Archiv CXLI,  194],  bei  Shakespeare  l.HenrylVth IV,  2,  21.  2.  Henry  IVth  III,  2,  292 und  295  caliver  'kleine  Muskete'  [wenn nicht  aus  frz.  coiileuvre  <^  lat.  coluber 'Schlange'] ;  russ.Ä:«?«/^ 'Gießform, -löffel', kaliber  'Geschützweite',  bulg.  kahp,  serb. kalup  'Gußform,  Schuhleisten'.  [Devic DEt  79/80.  Gorjajew  129.  Sain  48. SCHUCK ARDT  in  ZfromPh  XXIV,  571. A.  KLUYVER  in  ZfdWf  XI,  219/224.
2876:'Tiefer  Korb,  Tragkorb'  [aus  gr.  KÖqpivoq, lat.  cophinus  <C  lat.  cuppa,  vgl.  Lammens Farak  Nr.  1037];  hieraus  nach  der  vulg. Aussprache  mit  o  nach  einem  empha- tischen Laute  sp.  cofa,  cofe,  it.  coffa 'Mastkorb',  pg.  alcofa  'Korb',  cofo  'Kü- bel', siz.  coffa  'Marktkorb',  [mit  rom.  En- dung] it.  cöfano,  sp.  cuibano;  rum.  cofä 'Eimer,  Holzkanne'.  Afrz.  cofre,  frz. coffre,  engl,  coffer,  dtsch.  Koffer  [mit Anfügung  eines  -r  wie  in  Kaliber,  s.  hier Nr.  1030,  und  Kassiber,  hier  Nr.  1168]. Serb.  kofa  'Korb,  Mastkorb',  kofan  'Tru- he', öech.  kufr,  poln.  kufr,  klruss.  kufer 'Koffer'.  [DE  94.  Eguilaz  140.  StGlIt n,281.  GrSVociSic  232.  ML  2207  u.  4730.
5787:Äafta?e  977 iCrtöajg  993 iCa^eZ  766 Zaö(//e  979 ^Tad«  984 ifßtZjne  989 i:fl/f  992 Kaffee  4005 ^^//fe;-  992 Ka filier  j.  1150 Kaftan  774 Kaj>'put(öl)  1142 Kakadu  1Ü17 Kolbehasit  St.  1026 Kalbelazguar  St.  1025 Kalbolacrab  St.  1026 kalekutischer  Hahn  1031 kalemine  mhd.  1149 Kalender  1024 Kalenter  1024 kalfatern  1022 Kaliber  1030 ifaZ//"  798 A'rtZiX-o  1031 Kalium  1029 ifaZ/e  j.  1035 ifaZo«^  1038 Ar<?jjrtfc  1039 Kamel  653 Kamelie  653 Kamelhaut  653 Kamelot(t)  653 Kampfer  1100 Kandare  1051 kandieren  1052 Kandis  fzuckerj  1052 Kantschu(k)  1042 iCao/in  1060 Kap(p)ern  978
6403:calibre  1030
```


## [2026-09-06T21:50:14.973Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2450,2455p' LKT.txt | cut -c1-900; python3 -c \"\nt=open('LKT.txt',encoding='utf-8',errors='replace').read();lines=t.split('\\n');print('leaf',('\\n'.join(lines[:2454])).count('\\f'))\"",
 "description": "Read Lokotsch entry 1030"
}
```


### [2026-09-06T21:50:16.383Z] TOOL RESULT

```
[Ar.  kali.
1029.  Ar.  kali:
Tüttasche,  Aschensalz';  mit  ar.  Art.  in alle  europäischen  Sprachen  als  Fach- ausdruck der  Chemie  übergegangen:  sp. pg.  alcali,  frz.  alcali,  als  alchemistischer Ausdruck  algali  'Salpeter',  dial.  (Süd- frankreich) caliou  'Asche  aus  den  Reb- stöcken', engl,  alhdi,  dtsch.  Alkali  usw. Auch  der  Namen  des  Elementes  Kalium, Calium  gehört  hierhin,  [Devic  DEt  7. Lammens  Rem  7.
1030.  Ar.  kälib:
'Leisten  eines  Schusters',  ebenso  tk. kalyh,  Icahjp  'Modell,  Form';  hieraus rum.  calib,  calip,  calup  'Gießform,  Mo- dell, Leiste',  calupciü  'Betrüger';  aus dem  Ar.  unmittelbar  sp.  gälibo  'Schiffs- modell', frz.  gabarit;  asp.  calibo,  sp. calibre,  frz.  calibre  'Durchmesser  der Mündung  eines  Geschützes,  Gewicht  der Kugel';  it.  coUbro  'Maßinstrument,  um die  Zusammengehörigkeit  von  Geschütz und  Geschoß  zu  bestimmen';  dtsch. Kaliber,  engl,  calibre  [amerikanische Schreibung  caliber,  s.  Herrigs  Archiv CXLI,  194],  bei  Shakespeare  l.HenrylVth IV,  2,  21.  2.  Henry  IVth  III,  2,  292 und  295  caliver  'kleine  Muskete'  [wenn nicht  aus  frz.  coiileuvre  <^  lat.  coluber 'Schlange'] ;  russ.Ä:«?«/^ 'Gießform, -löffel', kaliber  'Geschützweite',  bulg.  kahp,  serb. kalup  'Gußform,  Schuhleisten'.  [Devic DEt  79/80.  Go
1031.  Uiud.  köHködn:
leaf 110
```


## [2026-09-06T21:50:26.731Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg283.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/283.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T21:50:26.800Z] TOOL RESULT

```
total 12656
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 17:50 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-06T21:58:04.783Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build283.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_KALBOD=\"https://en.wiktionary.org/wiki/کالبد\"\nW_QALEB=\"https://en.wiktionary.org/wiki/قالب\"\nW_KALA=\"https://en.wiktionary.org/wiki/کالا\"\nW_KALON=\"https://en.wiktionary.org/wiki/κᾶλον\"\nW_KAIO=\"https://en.wiktionary.org/wiki/καίω\"\nW_CAUC=\"https://en.wiktionary.org/wiki/Caucasus\"\nW_QAFQAZ=\"https://en.wiktionary.org/wiki/قفقاز\"\nW_CALIBRO=\"https://en.wiktionary.org/wiki/calibro\"\nW_QALB=\"https://en.wiktionary.org/wiki/قلب\"\nW_KAFKAS=\"https://en.wiktionary.org/wiki/Kafkas\"\nW_KAVKAZ=\"https://en.wiktionary.org/wiki/Кавказ\"\nE_CALIBER=\"https://www.etymonline.com/word/caliber\"\nE_CALM=\"https://www.etymonline.com/word/calm\"\nE_HOLO=\"https://www.etymonline.com/word/holocaust\"\nE_CAUCASIAN=\"https://www.etymonline.com/word/Caucasian\"\nA_KALA=\"https://abadis.ir/fatofa/کالا/\"\nA_KALBOD=\"https://abadis.ir/fatofa/کالبد/\"\nA_QALEB=\"https://abadis.ir/fatofa/قالب/\"\nA_KALIBR=\"https://abadis.ir/fatofa/کالیبر/\"\nA_QAFQAZ=\"https://abadis.ir/fatofa/قفقاز/\"\n\nPOK_QUOTE=(\"POK_full.txt line 51115 ff.: \\\"Root/lemma: keu-2 (: kau-, ku-) | Meaning: to light, to burn | \"\n \"Note: Only gr. and Lithuanian | Material: Gr. kaiw (Ionian), kaw (Attic) from *kaF-iwo 'to light, kindle' ... \"\n \"kausis, kauma n. 'blaze', kalon 'dry wood' (*kaF-elon), Aeolic kaualeos 'burning hot' ... \"\n \"References: WP. I 376 f. | Page(s): 595\\\"\")\n\nWLD_QUOTE=(\"WLD_Bd1_pages.txt leaf 384 = printed p. 376: \\\"keu- (: kau-, ku-) 'anzuenden, verbrennen'. \"\n \"Gr. kaiw (jon.), kaw (att.) aus *kaF-iw 'zuende an, brenne an' ... kausis, kauma, kalon 'trockenes Holz' \"\n \"(*kaF-elon), aol. kaualeos 'brennend heiss'\\\" (entry runs on to p. 377).\")\n\nKLN_CAL=(\"KLN_1966.txt leaf 128-129 (= printed p. 223 by Klein's own spacing: Caucasian and caustic fall 29 pp. later, \"\n \"matching Nourai's KLN:252/253) s.v. caliber: \\\"F. calibre, fr. It. calibro, fr. Arab. qalib, 'mold, model', \"\n \"fr. Gk. kalopodion, 'shoemaker's last', dimin. of kalopous, gen. kalopodos, of s.m., lit. 'a foot of wood', \"\n \"fr. kalon, 'wood', esp. 'wood for burning', and -pous, gen. podos, 'foot'. Gk. kalon is contracted fr. *kaF-elo-n \"\n \"... a derivative of kaiein (for *kaF-iein), 'to burn'; see caustic. ... Gk. kalopodion came into Arabic \"\n \"through the medium of the Aramaic.\\\"\")\n\nNYB_QUOTE=(\"NYB_vol2_glossary.txt line 2168: \\\"kalpad [k'lpt'], kalpud [k'lpwt'] shape, external bodily form ... \"\n \"MPrs k'lbyd (List 84); Paz. kalbud ... NP kalbad, kalbud 'the body of a man or an animal', 'a model, a last for \"\n \"shoes' which is the original sense, the w. being borrowed from Gr. kalopodion.\\\"\")\n\nPHD_QUOTE=(\"PHD.txt line 422 / PHD_mackenzie.txt line 3154 s.v.: \\\"kalbod [k'lpwt' | (M k'lbyd), N ~] body, shape, form\\\"; \"\n \"PHD.txt line 1036 'body kalbod, kirb, tan', line 2010 'form (n.) ... kalbod, kirb'.\")\n\nHRN_QUOTE=(\"HRN.txt leaf 303 = printed pp. 282-283, no. 123 (karp 'Koerper'): \\\"np. kalbud, kalbed 'Form, Koerper', \"\n \"phlv. karput bezw. kalput, vd. 5 (32) Gl., ys. 9 (46), Bhmyt., kurpat bezw. kalpat, Men. (paz. kalbud) ist \"\n \"gr. kalopodion 'Schusterleisten', wie Fleischer schon laengst gesehen hat (vergl. Noeldeke, Pers. Stud. II, 38).\\\"\")\n\nHUB_QUOTE=(\"HUB.txt lines 6282 and 9471 (Persische Studien, pp. ~177-178 and the chapter on l < d): \"\n \"\\\"LW. kalbad, kalbud 'Modell', paz. kalbud, phl. kalput, kalpat, gr. kalopodion, arm. kalapar\\\" and \"\n \"\\\"kalbad, kalbud 'Modell', phl. kalput = gr. kalopodion\\\".\")\n\nBQT_QUOTE=(\"BQT_v3_pages.txt leaf 367 = pdf page 368 = printed p. 1577 (printed = pdf + 1209 per BQT_v3_pagemap.json): \"\n \"headwords «کالب - بر وزن و معنی قالب است که آنرا کالبد نیز گویند» and «کالبد ... بمعنی کالب است که قالب هر چیز \"\n \"باشد - و بمعنی تن و بدن آدمی و حیوانات دیگر نیز هست», with Mo'in's footnote 4: «پهلوی kālbad (شکل، صورت)، \"\n \"پازند kālbud، مستعار از یونانی kalopódhion (قالب)؛ ارمنی kalapar ...؛ عربی قالب ... در اوراق مانوی پهلوی k'lbyd \"\n \"(هنینگ، فهرست لغات پارسی میانه)».\")\n\nPLA_QUOTE=(\"PLA_pages.txt leaf 229 = printed p. 215 (printed = leaf - 14; the next leaf carries the running head '216'): \"\n \"\\\"qalib: 'Gussform, Model' < pers. kalbod (n. 11 = BQ. s.v.), mp. kalpud (n. 12 = Nyberg Bd. II s.v.), \"\n \"mand. galib (n. 13 = Macuch s.v.)\\\".\")\n\nIEC_QUOTE=(\"IEC.txt leaf 582 = printed cols. 1051-1052: \\\"qurp- 'turn, shape, form, body'. Cf. querp-, quorp- \"\n \"Skt. krp, f. 'form, beauty'; Av. kehrp 'flesh, body'; Per. cf. kalbad, s. 'form, body'; ... \"\n \"Lat. corpus ... 'body, flesh'\\\"; the cross-referenced quorpos- 'turn, link, join' stands on leaf 580 = pp. 1047-1048.\")\n\nAHD_QUOTE=(\"AHD_watkins1985.txt line 626: \\\"keu-. To burn. Zero-grade form *kau- becoming *kaw- in suffixed form \"\n \"*kaw-yo- in Greek kaiein, to burn: CALM, CAUSTIC, CAUTERY; ENCAUSTIC, HOLOCAUST, (INK). [Pok. 2. keu- 595.]\\\"\")\n\ndata = {\n \"pdf_page\": 283,\n \"book_page\": 253,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Kŭ 1, Kĕu 5\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *keh₂w- / Pokorny *kēu- (: kāu-, ku-) 'to kindle, burn'\",\n   \"note\": (\"Pokorny IEW p. 595 has exactly this root — 'keu-2 (: kāu-, ku-), Meaning: to light, to burn' — so the \"\n     \"language label (Indo-European), the gloss ('to burn') and the page citation are all correct; Nourai's \"\n     \"'Kŭ 1, Kĕu 5' is his own double numbering of Pokorny's kēu-/kū- variants. Watkins/AHD lists the same root as \"\n     \"'kēu-. To burn' with the descendants CALM, CAUSTIC, CAUTERY, ENCAUSTIC, HOLOCAUST. The caveat that must be \"\n     \"recorded: Pokorny himself notes 'Only gr. and Lithuanian', i.e. the root rests on Greek καίω plus Lithuanian \"\n     \"kūlė 'smut, blight'; Beekes (via Wiktionary s.v. κᾶλον/καίω) and Etymonline call καίω 'of uncertain origin \"\n     \"with no certain cognates outside Greek'. The root is therefore real as a lemma but thinly attested, and the \"\n     \"whole page hangs on the single Greek verb.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *keh₂w- «افروختن، سوختن» (پوکورنی، فرهنگ ریشه‌شناختی هندواروپایی، ص ۵۹۵، ذیل \"\n     \"keu-2) واقعی است و برچسب زبانی و معنایی که نورایی آورده درست است؛ واتکینز نیز همین ریشه را با صورت *kēu- «سوختن» \"\n     \"آورده و واژه‌های calm، caustic و holocaust را از آن گرفته است. اما باید توجه داشت که خودِ پوکورنی می‌نویسد این \"\n     \"ریشه تنها در یونانی و لیتوانیایی بازتاب دارد؛ بیکس و اتیمولاین فعل یونانی καίω را «با خاستگاه نامعلوم» \"\n     \"می‌دانند. بنابراین ادعای نورایی دربارهٔ خودِ ریشه پذیرفتنی است، ولی پشتوانهٔ آن باریک و تک‌شاخه است.\"),\n   \"sources\": [W_KAIO, W_KALON],\n   \"ref_check\": [\n    {\"ref\": \"POK:595\", \"status\": \"supports\", \"note\": POK_QUOTE}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p. 595, lemma keu-2\", \"stance\": \"supports\", \"note\": POK_QUOTE},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 376 f.\", \"stance\": \"supports\", \"note\": WLD_QUOTE},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kēu-\", \"stance\": \"supports\", \"note\": AHD_QUOTE},\n    {\"src\": \"IEC\", \"where\": \"Mann, searched for a *keu- 'burn' lemma\", \"stance\": \"silent\",\n     \"note\": \"grep of IEC.txt for kal-/kau- lemmas returns kal- (1)-(6) 'slope, bright, call, fix, thrust, strike' and kalos (kāl-) 'dry, leap' — Mann has no 'burn' root matching Pokorny 595 and does not connect κᾶλον with καίω.\"},\n    {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. caustic (printed p. 253)\", \"stance\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 143-144 s.v. caustic: \\\"fr. Gk. kaustikos ... verbal adj. of kaiein, which stands for *kaF-iein, 'to burn, set on fire', fr. I.-E. base *keu-, *kū-, 'to burn, heat', whence also Lith. kūlė, 'blight, mildew', kūlėti, 'to become blighted'.\\\"\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Greek\", \"words\": \"Kalo; kalo-podein\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"Kalo : to burn, firewood / kalo-podein : wooden foot, mold\",\n     \"correct_form\": \"κᾶλον (kâlon) 'dry wood, firewood' beside καίω/κάω (kaíō/káō) 'to burn'; καλοπόδιον (kalopódion), dimin. of καλόπους (kalópous) 'shoemaker's last'\",\n     \"derivation\": (\"The Greek material is right but the forms as printed are not. (a) Ionic καίω / Attic κάω 'to kindle, \"\n       \"burn' goes back to *kaw-yō (Pokorny 595, Walde-Pokorny I 376), with καῦσις, καῦμα 'blaze, burning heat' and the \"\n       \"verbal adj. καυστός beside it; Nourai's headword 'Kalo' fuses this verb with the noun κᾶλον 'dry wood, firewood', \"\n       \"which is a distinct word contracted from *kaw-elon (so Pokorny and Klein; Beekes 2010 argues for a Pre-Greek \"\n       \"origin of κᾶλον instead). (b) 'kalo-podein' is not a Greek form at all: the shoemaker's last is καλόπους, gen. \"\n       \"καλόποδος, with the diminutive καλοπόδιον, literally 'little wooden foot' (κᾶλον 'wood' + πούς, gen. ποδός 'foot' \"\n       \"— hence Nourai's ☞Ped cross-reference). I rendered PDF page 283 at 300 dpi and read it: the printed page itself \"\n       \"shows 'kalo-podein', so the extraction is faithful and the impossible form is the book's own misprint for \"\n       \"καλοπόδιον.\"),\n     \"derivation_fa\": (\"مادهٔ یونانی درست است ولی صورت‌های چاپی کتاب نادرست‌اند. καίω (گویش ایونی) / κάω (آتیکی) «افروختن، \"\n       \"سوزاندن» از *kaw-yō است و καῦσις و καῦμα «سوز، گرمای سوزان» از همان ستاک‌اند؛ اما κᾶλον «هیزم، چوب خشک» واژه‌ای \"\n       \"جداست از *kaw-elon (پوکورنی ص ۵۹۵، والده‑پوکورنی ج ۱ ص ۳۷۶)، و بیکس آن را پیش‑یونانی می‌داند. نورایی این دو را در \"\n       \"یک سرواژه («Kalo») در هم آمیخته است. صورت «kalo-podein» در یونانی وجود ندارد: واژهٔ درست καλόπους (رایی: \"\n       \"καλόποδος) و مصغّر آن καλοπόδιον «پای چوبین، قالبِ کفشگری» است، از κᾶλον «چوب» + πούς «پا». تصویر صفحهٔ ۲۸۳ چاپی \"\n       \"را دیدم: همان «kalo-podein» چاپ شده است، پس خطا از کتاب است نه از خوانش اسکن.\"),\n     \"sources\": [W_KALON, W_KAIO, E_CALIBER],\n     \"ref_check\": [\n      {\"ref\": \"POK:595\", \"status\": \"supports\", \"note\": POK_QUOTE},\n      {\"ref\": \"WLD1:376\", \"status\": \"supports\", \"note\": WLD_QUOTE},\n      {\"ref\": \"KLN:223\", \"status\": \"supports\", \"note\": KLN_CAL}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kēu-\", \"stance\": \"supports\", \"note\": AHD_QUOTE},\n      {\"src\": \"SYN\", \"where\": \"Buck, searched 'firewood'/'to burn'\", \"stance\": \"silent\",\n       \"note\": \"grep of SYN.txt turns up no entry connecting κᾶλον with καίω; Buck treats 'burn' under the Greek verb only.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. κᾶλον\", \"stance\": \"partial\",\n       \"note\": \"\\\"Connected with καίω (kaíō, 'to burn') as 'firewood' ... However, according to Beekes, a Pre-Greek origin is much more likely.\\\" — the composition κᾶλον + πούς for καλόπους/καλοπόδιον is not in doubt, only the ultimate root.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"kal-pâd\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Middle Persian kālbad / kālpat (Book Pahlavi k'lpwt', Manichaean k'lbyd, Pazand kālbud) 'shape, \"\n       \"external bodily form, mould' is a straight loan from Greek καλοπόδιον, taken over in the Sasanian period through \"\n       \"the Aramaic-writing scribal milieu: Greek -π- appears as Pahlavi -p-/-b- and the Greek diminutive ending -ódion \"\n       \"was reshaped as -ad/-uδ. Nyberg, Horn (§123), Hübschmann, MacKenzie and Mo'in (in his footnote to Borhān-e Qāṭeʿ) \"\n       \"all say so explicitly; Nyberg adds that the concrete sense 'a last for shoes' \\\"is the original sense\\\", the \"\n       \"abstract 'body, form' being the later Iranian development. Nourai's 'kal-pâd' matches Nyberg's kālpaδ. His own \"\n       \"NOTE, that Mann (IEC 1049/1051) instead derives the word from Av. kəhrp- 'body' under a root *kʷerp-, is \"\n       \"accurately reported (Mann's lemma qurp- 'turn, shape, form, body' does list 'Per. cf. kalbad'), but modern \"\n       \"Iranian scholarship rejects that: kālbad cannot come from kəhrp- (which gives NP karp/kirb, cf. Horn no. 123 \"\n       \"itself, where the two are kept apart), and Nourai is right to prefer the Greek route.\"),\n     \"derivation_fa\": (\"فارسی میانه kālbad / kālpat (پهلوی کتابی k'lpwt'، مانوی k'lbyd، پازند kālbud) «شکل، پیکر، قالب» \"\n       \"وام‌واژه‌ای است از یونانی καλοπόδιον که در دورهٔ ساسانی وارد شده است؛ π یونانی در پهلوی به p/b و پایانهٔ تصغیر \"\n       \"-ódion به -ad/-uδ بدل شده است. نیبرگ (فرهنگ ج ۲، ذیل kālpaδ)، هرن (بند ۱۲۳)، هوبشمان، مکنزی و حاشیهٔ معین بر برهان \"\n       \"قاطع همگی همین را می‌گویند و نیبرگ می‌افزاید که معنای نخستین واژه «قالبِ کفش» بوده و معنای «تن و پیکر» متأخّر است. \"\n       \"یادداشت خود نورایی نیز درست نقل شده: مان در فرهنگ تطبیقی هندواروپایی این واژه را به اوستایی kəhrp- «تن» و ریشهٔ \"\n       \"*kʷerp- می‌برد؛ ولی ریشه‌شناسی امروزی این را نمی‌پذیرد، زیرا بازماندهٔ kəhrp- در فارسی karp/kirb است نه kālbad. \"\n       \"ادعای نورایی درست است.\"),\n     \"sources\": [W_KALBOD, A_KALBOD],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1095\", \"status\": \"not_found\",\n       \"note\": (\"Printed p. 1095 of the Moʿin edition is not the کالبد entry: BQT_v2_pages.txt leaf 555 (printed = leaf + 540, \"\n        \"calibrated against earlier checks in this project, e.g. leaf 173 = p. 715) carries «سپیدبر»/«سپیده‌دار», i.e. the \"\n        \"س section. The کالب/کالبد entries with Moʿin's Greek footnote stand at printed p. 1577 (BQT vol. 3, pdf p. 368) — \"\n        \"see the 'consulted' entry for BQT below. So the reference supports the claim, but not at the page Nourai cites.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. kālpaδ\", \"stance\": \"supports\", \"note\": NYB_QUOTE},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 49 s.v. kālbod\", \"stance\": \"supports\", \"note\": PHD_QUOTE},\n      {\"src\": \"HRN\", \"where\": \"no. 123, pp. 282-283\", \"stance\": \"supports\", \"note\": HRN_QUOTE},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien pp. ~177-178\", \"stance\": \"supports\", \"note\": HUB_QUOTE},\n      {\"src\": \"BQT\", \"where\": \"printed p. 1577 (vol. 3, pdf p. 368), Moʿin's footnote 4\", \"stance\": \"supports\", \"note\": BQT_QUOTE},\n      {\"src\": \"IEC\", \"where\": \"Mann cols. 1047-1052, lemma qurp-\", \"stance\": \"contradicts\", \"note\": IEC_QUOTE}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"kâlâ\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"NP کالا kālā (also کاله kāle) 'goods, merchandise', already in Ferdowsi (Shāhnāme, Goshtāsp), cannot be \"\n       \"shown to descend from MP kālbad/kālpat: no source known to me derives kālā from the Greek loanword, and the loss \"\n       \"of the whole second syllable -bad/-pad would be unexplained. Wiktionary, following the Iranian-etymology \"\n       \"literature, takes کالا as 'ultimately a derivative of Proto-Iranian *kar- \\\"to do, make\\\" (PIE *kʷer-)', i.e. \"\n       \"'the made thing, manufacture' — the same base as کردن and as Old Armenian կահ kah 'implements, gear' (an Iranian \"\n       \"loan); the semantic fit with the gloss 'manufactured good' is exact. Moʿin's own dictionary gives کالا with no \"\n       \"origin tag at all («(اِ.) اسباب، متاع»), and Mann's column 1047, cited by Nourai, is the lemma quorpos-/quorquol- \"\n       \"'turn, link, join' and says nothing about kālā. Nourai's own note ('References not clear on the exact path of \"\n       \"derivation') concedes the point; on present evidence the arrow Pahlavi kal-pād → kālā should be dropped.\"),\n     \"derivation_fa\": (\"«کالا» (و گونهٔ «کاله») از سدهٔ چهارم در شاهنامه به‌کار رفته است، اما پیوند آن با کالبد/kālbad پهلوی \"\n       \"پشتوانه‌ای ندارد؛ افتادن یکبارهٔ هجای -بد نیز توجیه آوایی ندارد. دیدگاه امروزی (ویکی‌واژه بر پایهٔ ادبیات \"\n       \"ریشه‌شناسی ایرانی) «کالا» را در نهایت مشتقی از ستاک ایرانی آغازین *kar- «کردن، ساختن» (هندواروپایی *kʷer-) \"\n       \"می‌داند، یعنی «آنچه ساخته شده»، هم‌ریشه با «کردن» و با وام‌واژهٔ ارمنی کهن kah؛ این با معنای «متاع ساخته‌شده» \"\n       \"کاملاً می‌خواند. معین نیز در برابر «کالا» هیچ نشانهٔ اصل و منشأ نمی‌گذارد. خود نورایی هم در یادداشت گفته است که \"\n       \"«منابع دربارهٔ مسیر دقیق اشتقاق روشن نیستند». پژوهش امروزی این پیکان را رد می‌کند.\"),\n     \"sources\": [W_KALA, A_KALA],\n     \"ref_check\": [\n      {\"ref\": \"MON:2858\", \"status\": \"not_checked\",\n       \"note\": (\"The six-volume Farhang-e Fārsi is not digitised (refs_online.json: 'no scan of the 6-vol Amir Kabir edition'), \"\n        \"so p. 2858 cannot be opened. The entry text via abadis.ir (فرهنگ معین section) reads «(اِ.) اسباب، متاع» — a bare \"\n        \"gloss with no origin tag, i.e. Moʿin does not support a Greek/Pahlavi derivation.\")},\n      {\"ref\": \"IEC:1047\", \"status\": \"not_found\",\n       \"note\": (\"IEC.txt leaf 580 = Mann's printed cols. 1047-1048 (the running numbers 1047/1048 are printed on that leaf); \"\n        \"the entries there are quorpos- 'turn, link, join', quorquol- 'twist, turn, curl' and quorquor-. There is no kālā \"\n        \"and nothing bearing on 'merchandise'.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. کالا, Persian section\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"Ultimately a derivative of Proto-Iranian *kar- ('to do, make'), from Proto-Indo-European *kʷer- ('to make'). See Old Armenian կահ (kah) for more.\\\" — with the Shāhnāme citation 'ba kālā giriftan na-pardāxtand'.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. کالا\", \"stance\": \"silent\", \"note\": \"«(اِ. ) اسباب ، متاع .» — no bracketed origin tag (contrast کالبد, which Moʿin tags «[په.]»).\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 3, pdf p. 368 = printed p. 1577\", \"stance\": \"silent\",\n       \"note\": \"The page carries the کالا-family headwords کالار and کالاشکن with lexical footnotes only (جهانگیری، فرهنگ نظام); Moʿin adds no etymology for کالا itself, while he does for کالبد on the same page.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep for کالا / KALA in Aryanpur's index returns only the Kurdish and Afghani KALA cross-entries of unrelated words; no Persian کالا headword surfaced in the OCR.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"kâleb; kâlbod\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"NP کالبد kālbad/kālbod 'body, frame; mould of anything' and its shortened variant کالب kāleb continue MP \"\n       \"kālbad/kālpat directly: Pazand kālbud > NP kālbud/kālbad, with the ordinary Middle→New Persian retention of the \"\n       \"cluster -lb- and the ā of the first syllable. Moʿin tags کالبد «[په.]» (Pahlavi) in Farhang-e Fārsi, and in his \"\n       \"footnote to Borhān-e Qāṭeʿ (printed p. 1577) spells the whole chain out: «پهلوی kālbad (شکل، صورت)، پازند kālbud، \"\n       \"مستعار از یونانی kalopódhion (قالب)». Borhān itself defines کالب as «بر وزن و معنی قالب است که آنرا کالبد نیز \"\n       \"گویند», exactly Nourai's two glosses. Horn no. 123 and Hübschmann give the same. NOTE ON THE CHART: on the \"\n       \"printed page the arrow into this box comes out of the bottom-left corner of the Pahlavi box (I cropped and read \"\n       \"that part of the 300-dpi render), i.e. the book derives kāleb/kālbod from node 2, not from the root; the \"\n       \"extracted JSON records parent 0, which is an extraction error.\"),\n     \"derivation_fa\": (\"«کالبد» و گونهٔ کوتاه‌شدهٔ «کالب» دنبالهٔ مستقیم kālbad/kālpat فارسی میانه‌اند؛ پازند kālbud در فارسی \"\n       \"نو به kālbud/kālbad بدل شده و خوشهٔ -لب- و کشیدگی آ در هجای نخست دست‌نخورده مانده است. معین در فرهنگ فارسی «کالبد» \"\n       \"را «[په.]» (پهلوی) نشانه‌گذاری کرده و در حاشیهٔ برهان قاطع (ص ۱۵۷۷) همهٔ زنجیره را می‌آورد: «پهلوی kālbad (شکل، \"\n       \"صورت)، پازند kālbud، مستعار از یونانی kalopódhion (قالب)». خودِ برهان می‌نویسد «کالب: بر وزن و معنی قالب است که \"\n       \"آنرا کالبد نیز گویند» که دقیقاً دو معنای نورایی است. هرن (بند ۱۲۳) و هوبشمان نیز همین را دارند. ادعای نورایی درست \"\n       \"است. نکته: در صفحهٔ چاپی، پیکانِ ورودی این خانه از خانهٔ پهلوی می‌آید، نه از ریشه؛ در استخراج JSON به‌اشتباه \"\n       \"«والد ۰» ثبت شده است.\"),\n     \"sources\": [W_KALBOD, A_KALBOD],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1075\", \"status\": \"not_found\",\n       \"note\": (\"BQT_v2_pages.txt leaf 535 = printed p. 1075 (printed = leaf + 540) is in the س section — the page carries \"\n        \"«سالار», «ساک», «ساطل» — not کالب. The کالب/کالبد entries are at printed p. 1577 (vol. 3, pdf p. 368), where \"\n        \"Moʿin's footnote does support Nourai's chain; the page number as cited is wrong.\")},\n      {\"ref\": \"MON:2859\", \"status\": \"not_checked\",\n       \"note\": (\"6-vol Farhang-e Fārsi not digitised, so p. 2859 cannot be opened. The entry as served by abadis.ir \"\n        \"(فرهنگ معین) reads «(بُ یا بَ ) [ په . ] (اِ. ) ۱ - قالب هر چیز. ۲ - تن و بدن آدمی . ۳ - نمونه ، سرمشق» — the \"\n        \"Pahlavi tag and both of Nourai's glosses are there.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"printed p. 1577 (vol. 3, pdf p. 368)\", \"stance\": \"supports\", \"note\": BQT_QUOTE},\n      {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. کالبد\", \"stance\": \"supports\", \"note\": \"«[ په . ] (اِ. ) ۱ - قالب هر چیز. ۲ - تن و بدن آدمی . ۳ - نمونه ، سرمشق .»\"},\n      {\"src\": \"HRN\", \"where\": \"no. 123, pp. 282-283\", \"stance\": \"supports\", \"note\": HRN_QUOTE},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien pp. ~177-178\", \"stance\": \"supports\", \"note\": HUB_QUOTE},\n      {\"src\": \"PHD\", \"where\": \"s.v. kālbod\", \"stance\": \"supports\", \"note\": PHD_QUOTE},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. کالبد\", \"stance\": \"supports\",\n       \"note\": \"\\\"From Middle Persian kʾlpwt' /kālbod/, 'body, shape, form', from Ancient Greek καλοπόδιον (kalopódion, 'shoemaker's last'). Akin to Manichaean Middle Persian kʾlbyd ... Doublet of قالب (qâleb), the same Greek word via Arabic.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Arabic\", \"words\": \"qâlib; q.l.b\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"Two different claims are packed into this box and they do not fare alike. (a) Arabic قالَب/قالِب qālab/qālib \"\n       \"'mould, model, last' IS a loan of the Iranian word, and Nourai's own reference Asbaghi says exactly that: \"\n       \"\\\"qālib: 'Gußform, Model' < pers. kālbod, mp. kālpuδ\\\" (Persische Lehnwörter im Arabischen p. 215); Moʿin's Borhān \"\n       \"footnote likewise ends its chain with «عربی قالب». The competing account keeps the same Greek source but routes it \"\n       \"through Aramaic rather than Persian: Klein (Nourai's other reference) writes \\\"Gk. καλοπόδιον came into Arabic \"\n       \"through the medium of the Aramaic\\\", and Wiktionary derives قالب from Classical Syriac ܩܠܒܝܕ *qālobīḏ < καλοπόδιον. \"\n       \"Both routes are respectable; Nourai's is Asbaghi's, so (a) is at worst 'plausible'. (b) The second word, the root \"\n       \"q.l.b 'to make, turn around', is a different matter: قَلَبَ qalaba 'to turn over' and its noun قلب qalb 'heart' are \"\n       \"inherited Arabic/Semitic material (Wiktionary classes them under Arabic terms inherited from Proto-Semitic), not \"\n       \"something generated by a Middle Persian loanword. What actually happened is the reverse of the arrow: the foreign \"\n       \"qālab was naturalised by being fitted to the pre-existing triliteral root q-l-b, an ordinary case of Arabic \"\n       \"root-assimilation (folk etymology). By the worst-word rule the node is therefore 'disputed', although the \"\n       \"borrowing of qālib itself stands.\"),\n     \"derivation_fa\": (\"در این خانه دو ادعا کنار هم آمده که سرنوشتشان یکی نیست. نخست، «قالَب/قالِب» عربی به‌راستی وام‌واژه‌ای \"\n       \"ایرانی است و مرجع خودِ نورایی، اصغی در «وام‌واژه‌های فارسی در عربی» ص ۲۱۵، همین را می‌گوید: qālib < فارسی kālbod، \"\n       \"فارسی میانه kālpuδ؛ حاشیهٔ معین بر برهان نیز زنجیره را با «عربی قالب» به پایان می‌برد. در برابر، کلاین و ویکی‌واژه \"\n       \"همان اصل یونانی را می‌پذیرند ولی واسطه را سریانی می‌دانند (ܩܠܒܝܕ). هر دو مسیر پذیرفتنی است. دوم، ریشهٔ «ق‑ل‑ب» \"\n       \"«گرداندن» مادّهٔ اصیل سامی است (قَلَبَ، قلب، انقلاب…) و از وام‌واژهٔ ایرانی زاده نشده است؛ آنچه رخ داده وارونهٔ پیکانِ \"\n       \"نورایی است: واژهٔ بیگانهٔ «قالب» را به ریشهٔ از پیش موجودِ ق‑ل‑ب چسبانده‌اند، یعنی ریشه‌شناسی عامیانه و همسان‌سازی \"\n       \"با ریشهٔ سه‌حرفی. از این رو داوری این خانه «رد‌شده» است، هرچند خودِ وام‌گیری «قالب» برجاست.\"),\n     \"sources\": [W_QALEB, W_QALB, W_KALBOD],\n     \"ref_check\": [\n      {\"ref\": \"KLN:223\", \"status\": \"partial\", \"note\": KLN_CAL + \" — Klein has the Greek source and Arabic qālib, but routes the word through Aramaic, not Persian, and says nothing that would derive the Arabic root q-l-b from it.\"},\n      {\"ref\": \"PLA:215\", \"status\": \"supports\", \"note\": PLA_QUOTE}\n     ],\n     \"consulted\": [\n      {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p. 215\", \"stance\": \"supports\", \"note\": PLA_QUOTE},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. caliber (p. 223)\", \"stance\": \"partial\", \"note\": KLN_CAL},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030 (printed p. 84, leaf 110)\", \"stance\": \"partial\",\n       \"note\": \"\\\"1030. Ar. kālib: 'Leisten eines Schusters', ebenso tk. kalyb, kalyp 'Modell, Form' ... asp. calibo, sp. calibre, frz. calibre ... it. calibro ... dtsch. Kaliber, engl. calibre\\\" — Lokotsch takes the Arabic word as the source of the European ones but gives it no Persian etymology.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, grep for قالب\", \"stance\": \"silent\",\n       \"note\": \"grep of AFM_pages.txt for قالب returns nothing in the OCR (Asbaghi's footnote 11 cites 'BQ. s.v.' and elsewhere 'Addai Scher s.v.', but I could not locate the entry in this scan).\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, grep for qalib\", \"stance\": \"silent\", \"note\": \"not a Qurʾanic word; grep of FVQ.txt for qalib/qālib returns nothing.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. قالب (Arabic)\", \"stance\": \"partial\",\n       \"note\": \"\\\"From Classical Syriac ܩܠܒܝܕ (*qālobīḏ, 'last'), from Ancient Greek καλοπόδιον (kalopódion, 'last'), diminutive of καλόπους (kalópous), compound of κᾶλον (kâlon, 'wood') and πούς (poús, 'foot').\\\"\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. قلب (Arabic)\", \"stance\": \"contradicts\",\n       \"note\": \"قَلْب qalb 'heart' is \\\"Derived from قَلَبَ (qalaba, 'to turn')\\\" and the page files these under 'Arabic terms inherited from Proto-Semitic' — the root q-l-b is native, not a back-formation from the loanword.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"qâleb\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian قالب qāleb 'mould, form; the body' is the Arabic-mediated return of the same word: the Iranian \"\n       \"kālbad, once Arabicised as قالَب (with k > q and the loss of the final dental in the Arabic shape), was re-borrowed \"\n       \"into New Persian in its Arabic dress, so that Persian now has the doublet کالبد ~ قالب. Moʿin marks قالب «[معر.]» \"\n       \"(muʿarrab, 'Arabicised'), which is precisely a Persian→Arabic→Persian round trip, and Wiktionary calls کالبد a \"\n       \"\\\"doublet of قالب (qâleb), the same Greek word via Arabic\\\". The extra family Nourai prints in the box — قلب، \"\n       \"انقلاب، منقلب، مقلوب، تقلب، قلاب — belongs to the native Arabic root q-l-b 'to turn' and reached Persian as ordinary \"\n       \"Arabic loans; those words are NOT descendants of kālbad (see node 5), and only قالب itself is.\"),\n     \"derivation_fa\": (\"«قالب» فارسی بازگشتِ همان واژه از راه عربی است: kālbad ایرانی در عربی معرّب شد (ک > ق و افتادن دالِ \"\n       \"پایانی) و سپس در جامهٔ عربی دوباره به فارسی درآمد؛ از این رو فارسی امروز دوگانهٔ «کالبد ~ قالب» دارد. معین در برابر \"\n       \"«قالب» نشانهٔ «[معر.]» گذاشته است که همان چرخهٔ فارسی → عربی → فارسی است، و ویکی‌واژه «کالبد» را دوگانهٔ «قالب» \"\n       \"می‌خواند. اما خانوادهٔ «قلب، انقلاب، منقلب، مقلوب، تقلب، قلاب» که نورایی در همین خانه آورده از ریشهٔ اصیل عربی \"\n       \"ق‑ل‑ب «گرداندن» است و وام‌واژه‌های عربی معمولی‌اند، نه بازماندگان kālbad. ادعای نورایی دربارهٔ خودِ «قالب» درست است.\"),\n     \"sources\": [A_QALEB, W_QALEB, W_KALBOD],\n     \"ref_check\": [\n      {\"ref\": \"MON:2621\", \"status\": \"not_checked\",\n       \"note\": (\"6-vol Farhang-e Fārsi not digitised (no scan on archive.org/HathiTrust per refs_online.json), so p. 2621 \"\n        \"cannot be opened. Via abadis.ir the Moʿin entry reads «(لِ ) [ معر. ] (اِ. ) ۱ - پیکر، هیکل . ۲ - شکل ، هیئت . \"\n        \"۳ - آلتی که جسمی شکل پذیر را ... قالب کفش ...» — the tag [معر.] 'Arabicised' is exactly Nourai's claim.\")},\n      {\"ref\": \"FVA:337\", \"status\": \"not_checked\",\n       \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi (1368/1989): refs_online.json records that no digital copy exists on any permitted platform (catalogue record only, OpenLibrary OL2012991M).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. قالب\", \"stance\": \"supports\", \"note\": \"«(لِ ) [ معر. ] (اِ. ) ۱ - پیکر، هیکل . ۲ - شکل ، هیئت . ۳ - آلتی که جسمی شکل پذیر را ... به صورت آن آلت درآورند، قالب کفش .» — note the surviving 'shoe-last' sense.\"},\n      {\"src\": \"BQT\", \"where\": \"printed p. 1577 (vol. 3, pdf p. 368)\", \"stance\": \"supports\", \"note\": \"Borhān s.v. کالب: «بر وزن و معنی قالب است که آنرا کالبد نیز گویند», and Moʿin's footnote ends «... عربی قالب» — the two Persian forms are explicitly identified.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p. 215\", \"stance\": \"supports\", \"note\": PLA_QUOTE},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. کالبد\", \"stance\": \"supports\", \"note\": \"\\\"Doublet of قالب (qâleb), the same Greek word via Arabic.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Italian\", \"words\": \"calibro\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Italian calibro 'calibre, gauge, mould' is derived from Arabic qālib by Klein (s.v. caliber: \\\"F. calibre, \"\n       \"fr. It. calibro, fr. Arab. qālib\\\") and by Lokotsch (no. 1030, which lists it together with Sp. calibre and Fr. \"\n       \"calibre among the Romance offspring of the Arabic word) — the borrowing would belong to the 15th-16th c. gunnery \"\n       \"vocabulary of the Mediterranean. But the derivation is not secure: Barnhart objects that Spanish calibre and \"\n       \"Italian calibro \\\"appear too late to act as intermediate forms\\\" between Arabic and French; Webster's New \"\n       \"Twentieth Century s.v. calibre gives only \\\"Fr. calibre, perh. from L. qua libra, what pound, weight, size\\\", and \"\n       \"Wiktionary's Italian entry hedges: \\\"Possibly from Arabic قَالِب ... Or, possibly a derivation of Latin qua libra\\\". \"\n       \"So the word is real and the Arabic source is the majority opinion, but a Medieval-Latin qua libra origin is a \"\n       \"live alternative.\"),\n     \"derivation_fa\": (\"ایتالیایی calibro «قُطر، اندازه، قالب» را کلاین (ذیل caliber) و لوکوچ (شمارهٔ ۱۰۳۰) از عربی «قالب» \"\n       \"می‌گیرند؛ وام‌گیری در واژگان توپخانهٔ سدهٔ نهم–دهم هجری/پانزدهم–شانزدهم میلادی مدیترانه رخ داده است. با این همه، \"\n       \"این اشتقاق قطعی نیست: بارنهارت می‌گوید صورت‌های اسپانیایی و ایتالیایی برای واسطه‌شدن میان عربی و فرانسه «بیش از \"\n       \"اندازه دیر» پدیدار شده‌اند، وبستر تنها «شاید از لاتینی qua libra» را می‌آورد و ویکی‌واژه هر دو احتمال را کنار هم \"\n       \"می‌نهد. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W_CALIBRO, E_CALIBER],\n     \"ref_check\": [\n      {\"ref\": \"KLN:223\", \"status\": \"supports\", \"note\": KLN_CAL}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030 (printed p. 84)\", \"stance\": \"partial\",\n       \"note\": \"\\\"Ar. kālib ... it. calibro 'Maßinstrument, um die Zusammengehörigkeit von Geschütz und Geschoß zu bestimmen'\\\" — Arabic source confirmed, but Lokotsch makes Spanish/French the route, not Italian→French.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. cal'i-ber, cal'i-bre\", \"stance\": \"contradicts\",\n       \"note\": \"WEB_vol1.txt line 26452: \\\"[Fr. calibre, perh. from L. qua libra, what pound, weight, size.]\\\" — no Arabic.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. calibro (Italian)\", \"stance\": \"partial\",\n       \"note\": \"\\\"Possibly from Arabic قَالِب (qālib, 'mold'), itself from Ancient Greek καλαπούς (kalapoús) ... Or, possibly a derivation of Latin qua libra, 'of what dimensions, weight.'\\\"\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"French\", \"words\": \"\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Empty pass-through box for French calibre, first attested in the mid-16th c. (perhaps already late 15th c.) \"\n       \"in the sense 'internal diameter of a gun barrel', the form from which English caliber and Persian کالیبر come. \"\n       \"Klein has it from Italian calibro, which is the arrow Nourai draws; but Lokotsch (no. 1030) makes French calibre a \"\n       \"direct or Spanish-mediated taking from Arabic qālib, and Barnhart holds that the Italian and Spanish forms are too \"\n       \"late to be intermediaries, so that the word may have been shaped in French itself (from Medieval Latin qua libra). \"\n       \"The node's existence is certain; only the Italian → French step is uncertain.\"),\n     \"derivation_fa\": (\"خانهٔ واسطهٔ بی‌واژه برای فرانسویِ calibre که از میانهٔ سدهٔ شانزدهم میلادی (شاید از اواخر سدهٔ پانزدهم) \"\n       \"به معنای «قطر درونی لولهٔ سلاح» گواهی شده و سرچشمهٔ caliber انگلیسی و «کالیبر» فارسی است. کلاین آن را از ایتالیایی \"\n       \"calibro می‌گیرد — همان پیکانی که نورایی کشیده — ولی لوکوچ آن را یکسره یا از راه اسپانیایی از عربی «قالب» می‌داند و \"\n       \"بارنهارت صورت‌های ایتالیایی و اسپانیایی را برای واسطه‌شدن دیرهنگام می‌شمارد. وجود این حلقه قطعی است؛ تنها گام \"\n       \"«ایتالیایی ← فرانسه» تردیدآمیز است.\"),\n     \"sources\": [E_CALIBER],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; the French link is covered by KLN:223 on the neighbouring boxes.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. caliber (p. 223)\", \"stance\": \"supports\", \"note\": \"\\\"F. calibre, fr. It. calibro, fr. Arab. qālib\\\" — exactly the Italian → French → English order of the chart.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030\", \"stance\": \"partial\", \"note\": \"\\\"aus dem Ar. unmittelbar sp. gálibo ...; asp. calibo, sp. calibre, frz. calibre 'Durchmesser der Mündung eines Geschützes'\\\" — French from Arabic/Spanish, not from Italian.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. caliber\", \"stance\": \"partial\",\n       \"note\": \"\\\"1580s, from French calibre (by mid-16c., perhaps late 15c.), often said to be ultimately from Arabic qalib ... Barnhart remarks that Spanish calibre, Italian calibro 'appear too late to act as intermediate forms'.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"Persian\", \"words\": \"«کالیبر»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian کالیبر kālibr 'bore, calibre of a gun barrel' is a modern European loan taken from French calibre, \"\n       \"not from any older Iranian form: the French final -re is rendered -بر and the stress-final French vowel is kept, \"\n       \"which is the regular treatment of 19th-20th c. French technical vocabulary in Persian (cf. متر، لیتر، مانور). \"\n       \"Moʿin tags the word «[فر.]» (French) and Dehkhoda opens the entry «کالیبر. (فرانسوی، اِ) بمعنی قطر درونی استوانه»; \"\n       \"so the arrow French → Persian is exactly right, and the word is the far end of the round trip that began with \"\n       \"Middle Persian kālbad.\"),\n     \"derivation_fa\": (\"«کالیبر» وام‌واژه‌ای نو از فرانسویِ calibre است، نه بازماندهٔ صورتی ایرانی: پایانهٔ -re فرانسوی در \"\n       \"فارسی «-بر» شده و این همان رفتار معمول با واژگان فنی فرانسوی در سدهٔ سیزدهم–چهاردهم خورشیدی است (مانند متر، لیتر، \"\n       \"مانور). معین آن را «[فر.]» نشانه‌گذاری کرده و دهخدا می‌نویسد «کالیبر. (فرانسوی، اِ) بمعنی قطر درونی استوانه». پس \"\n       \"پیکان «فرانسه ← فارسی» درست است و این واژه پایانِ همان چرخه‌ای است که با kālbad فارسی میانه آغاز شد.\"),\n     \"sources\": [A_KALIBR],\n     \"ref_check\": [\n      {\"ref\": \"MON:2621\", \"status\": \"not_checked\",\n       \"note\": \"6-vol Farhang-e Fārsi not digitised; via abadis.ir the Moʿin entry for کالیبر reads «(بْ ) [ فر. ] (اِمر. ) قطر دهانة لولة توپ یا تفنگ .» — the [فر.] (French) tag is Nourai's claim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. کالیبر\", \"stance\": \"supports\", \"note\": \"«[ فر. ] (اِمر. ) قطر دهانة لولة توپ یا تفنگ .»\"},\n      {\"src\": \"Dehkhoda\", \"where\": \"abadis.ir, لغت‌نامهٔ دهخدا s.v. کالیبر\", \"stance\": \"supports\", \"note\": \"«کالیبر. ( فرانسوی ، اِ ) بمعنی قطر درونی استوانه. قطر درونی احجام استوانه ای : کالیبر لوله تپانچه ...»\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"English\", \"words\": \"caliber\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English caliber/calibre is borrowed from French calibre; the earliest English use is the figurative one, \"\n       \"'degree of merit or importance' (1560s), the technical 'inside diameter of a gun barrel' following in the 1580s, \"\n       \"and the American spelling -er replacing -re later. The immediate French > English step drawn here is not in \"\n       \"dispute anywhere (Klein, Webster, Etymonline and Lokotsch all give it); what is disputed further upstream is \"\n       \"whether French got the word from Arabic qālib through Italian (Klein, Nourai) or coined it on Medieval Latin qua \"\n       \"libra (Barnhart, Webster).\"),\n     \"derivation_fa\": (\"انگلیسیِ caliber/calibre وام از فرانسویِ calibre است؛ نخستین کاربرد انگلیسی معنای مجازی «پایه و مرتبه» \"\n       \"(دههٔ ۱۵۶۰م) و سپس معنای فنی «قطر درونی لولهٔ سلاح» (دههٔ ۱۵۸۰م) است و املای آمریکایی -er بعدها جای -re را گرفت. \"\n       \"این گامِ «فرانسه ← انگلیسی» نزد کلاین، وبستر، اتیمولاین و لوکوچ یکسان و بی‌مناقشه است؛ آنچه محل اختلاف است حلقه‌های \"\n       \"بالادست است (عربی قالب یا لاتینی qua libra). ادعای نورایی در این خانه درست است.\"),\n     \"sources\": [E_CALIBER],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed in this box; KLN:223 on the Italian box covers the English word ('F. calibre, fr. It. calibro').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. caliber (p. 223)\", \"stance\": \"supports\", \"note\": KLN_CAL},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. cal'i-ber\", \"stance\": \"partial\", \"note\": \"\\\"[Fr. calibre, perh. from L. qua libra...] 1. the size of a bullet or shell as measured by its diameter.\\\" — French source agreed, Arabic denied.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. caliber\", \"stance\": \"supports\", \"note\": \"\\\"'inside diameter of a gun barrel,' 1580s, from French calibre ... The earliest sense in English is a figurative one, 'degree of merit or importance' (1560s), from French.\\\"\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1030\", \"stance\": \"supports\", \"note\": \"\\\"dtsch. Kaliber, engl. calibre [amerikanische Schreibung caliber] ... bei Shakespeare 1. Henry IVth IV, 2, 21 ... caliver 'kleine Muskete'.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"Greek\", \"words\": \"kau; kau-casos\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Klein (Nourai's reference) does attach Καύκασος to this root, but not in the way the box draws it: he \"\n       \"derives Gk. Καύκασος from a Scythian *Kroy-kasis, 'the mountain shining with ice', in which the FIRST element is \"\n       \"from I.-E. *kreu- 'to be icy' (Nourai's ☞Kreu) and the SECOND, -kasis, is the one related to Gk. καίειν 'to burn, \"\n       \"shine' — Nourai's segmentation 'kau- (burning, shining) + -casos' reverses the two halves, since the Greek kau- of \"\n       \"Καύκασος is an adaptation of the Scythian kroy-/krou- 'ice', not of the burn-root. The Scythian gloss itself comes \"\n       \"from Pliny (Nat. Hist. VI.xvii), who says the Scythians called it Croucasim, 'nive candidum'. Modern handbooks \"\n       \"treat this as unproven: Etymonline adds \\\"But possibly from a Pelasgian root *kau- meaning 'mountain'\\\", and \"\n       \"Wiktionary gives Καύκασος with no etymology. Also note that there is no free Greek word kau 'burning, shining': the \"\n       \"Greek forms are καίω, καῦσις, καῦμα, καυστός. The connection is thus defensible on Klein's authority but the \"\n       \"analysis as printed is wrong in its parts and the name is very likely non-Greek.\"),\n     \"derivation_fa\": (\"کلاین — همان مرجعی که نورایی آورده — Καύκασος را به این ریشه می‌بندد، اما نه آن‌گونه که در نمودار آمده \"\n       \"است: او این نام را از سکاییِ *Kroy-kasis «کوهِ درخشان از یخ» می‌گیرد که در آن جزء نخست از ریشهٔ *kreu- «یخ» است و \"\n       \"جزء دوم (-kasis) با καίειν «سوختن، درخشیدن» پیوند دارد. پس تجزیهٔ نورایی («kau» = سوزان/درخشان + «-casos» با ارجاع \"\n       \"به Kreu) جای دو جزء را عوض کرده است؛ kau- یونانی در Καύκασος برگردانِ krou- سکایی «یخ» است. سرچشمهٔ این تفسیر \"\n       \"پلینی (تاریخ طبیعی ۶/۱۷) است که می‌گوید سکاها آن را Croucasim یعنی «سپید از برف» می‌خواندند. پژوهش امروزی این را \"\n       \"اثبات‌نشده می‌داند؛ اتیمولاین احتمال ریشهٔ پیش‑یونانی/پلاسگی *kau- «کوه» را نیز می‌آورد و ویکی‌واژه هیچ ریشه‌شناسی \"\n       \"نمی‌دهد. افزون بر این، واژهٔ مستقلِ «kau» در یونانی وجود ندارد. با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W_CAUC, E_CAUCASIAN],\n     \"ref_check\": [\n      {\"ref\": \"KLN:252\", \"status\": \"partial\",\n       \"note\": (\"KLN_1966.txt leaf 143 (= Klein's printed p. 252, one page before the caustic entry Nourai cites as KLN:253) \"\n        \"s.v. Caucasian: \\\"Formed with suff. -ian fr. L. Caucasus, fr. Gk. Kaukasos, fr. Scythian Kroy-kasis, 'Caucasus', \"\n        \"a compound meaning lit. '(the mountain) shining with ice'; see Walde-Hofmann, LEW., I, pp. 295-96, s.v. crusta. \"\n        \"The first element of this compound is a derivative of I.-E. base *qreu-, 'to be icy'. ... The second element is \"\n        \"rel. to Gk. kaiein (for *kaFiein), 'to burn'; see caustic.\\\" — supports the link to the burn root, but assigns it \"\n        \"to the SECOND element, the opposite of the chart's 'kau-casos'.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p. 595, lemma keu-2\", \"stance\": \"silent\", \"note\": \"Pokorny's burn-root entry lists only καίω, καῦσις, καῦμα, κᾶλον, καυαλέος and Lith. kūlėti; Καύκασος is not mentioned.\"},\n      {\"src\": \"LEW\", \"where\": \"Walde(-Hofmann) s.v. crusta, cited by Klein\", \"stance\": \"silent\",\n       \"note\": \"The local copy is the 2nd ed. of 1910 (LEW_1910.txt); grep for 'Caucas' returns nothing, so Klein's reference to Walde-Hofmann I 295-96 (3rd ed.) could not be verified in this scan.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. Caucasus (under Caucasian)\", \"stance\": \"partial\",\n       \"note\": \"\\\"from Greek kaukasis, said by Pliny ('Natural History,' book six, chap. XVII) to be from a Scythian word similar to kroy-khasis, literally '(the mountain) ice-shining, white with snow.' But possibly from a Pelasgian root *kau- meaning 'mountain.'\\\"\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. Caucasus\", \"stance\": \"silent\", \"note\": \"\\\"Via Latin Caucasus, from Ancient Greek Καύκασος (Kaúkasos).\\\" — no further etymology offered.\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"Latin\", \"words\": \"caucasus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin Caucasus is a straight literary borrowing of Greek Καύκασος, current in Latin from the late Republic \"\n       \"(Cicero, Vergil, Pliny) as the name of the range between the Black and the Caspian Seas — Nourai's gloss is the \"\n       \"standard geographical one. The Greek name itself was known to the Greeks from Aeschylus onward, and Pliny (VI.17) \"\n       \"reports the Scythian equivalent. Wiktionary's Latin section: \\\"Borrowed from Ancient Greek Καύκασος (Kaúkasos)\\\"; \"\n       \"Klein derives English Caucasian 'fr. L. Caucasus, fr. Gk. Kaukasos'. Only the ultimate origin of the Greek name \"\n       \"(node 11) is in doubt, not this step.\"),\n     \"derivation_fa\": (\"لاتینیِ Caucasus وام ادبیِ سرراست از یونانیِ Καύκασος است و از اواخر دورهٔ جمهوری (سیسرون، ویرژیل، \"\n       \"پلینی) نام رشته‌کوه میان دریای سیاه و دریای خزر بوده است؛ معنایی که نورایی آورده همان معنای جغرافیایی متعارف است. \"\n       \"ویکی‌واژه در بخش لاتینی می‌نویسد «وام‌گرفته از یونانی باستان Καύκασος» و کلاین نیز Caucasian انگلیسی را «از لاتینی \"\n       \"Caucasus، از یونانی Kaukasos» می‌گیرد. تنها خاستگاه نهاییِ نام یونانی (خانهٔ ۱۱) محل تردید است، نه این گام.\"),\n     \"sources\": [W_CAUC],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed in this box; the neighbouring KLN:252 covers the Greek → Latin step.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. Caucasus, Latin section\", \"stance\": \"supports\", \"note\": \"\\\"Borrowed from Ancient Greek Καύκασος (Kaúkasos).\\\" with Classical Latin pronunciation [ˈkau̯.ka.sʊs].\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. Caucasian (p. 252)\", \"stance\": \"supports\", \"note\": \"\\\"fr. L. Caucasus, fr. Gk. Kaukasos\\\".\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, grep for Caucas\", \"stance\": \"silent\", \"note\": \"grep of LAT.txt returns no Caucasus entry — Ernout-Meillet excludes proper names of this kind.\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"Arabic\", \"words\": \"\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"An empty pass-through box standing for the Arabic form of the name. Arabic does have القوقاز al-Qawqāz \"\n       \"(and the older جبل القبق Jabal al-Qabq) for the Caucasus, and it is ultimately the Graeco-Latin name; so a \"\n       \"Latin/Greek → Arabic step is possible in principle. But nothing in the local library or in Wiktionary documents \"\n       \"an Arabic transmission specifically to the Persian form قفقاز, and the medieval Arabic geographers' usual word \"\n       \"is al-Qabq, not Qafqāz. The likelier immediate transmitter of the modern Persian form is Ottoman Turkish/Russian \"\n       \"(see node 14). The box is therefore possible but undocumented.\"),\n     \"derivation_fa\": (\"خانهٔ واسطهٔ بی‌واژه که جای صورت عربی نام را نگاه می‌دارد. در عربی «القوقاز» (و در متون کهن‌تر «جبل \"\n       \"القبق») به‌کار رفته و در نهایت همان نام یونانی‑لاتینی است، پس گامِ لاتینی/یونانی ← عربی از نظر اصولی شدنی است. با \"\n       \"این حال هیچ منبعی در کتابخانهٔ محلی یا ویکی‌واژه انتقالِ عربی را به‌ویژه برای صورت فارسی «قفقاز» گواهی نمی‌کند و \"\n       \"واژهٔ رایج جغرافی‌نویسان عرب «القبق» بوده است نه «قفقاز». واسطهٔ محتمل‌تر برای صورت فارسی امروزی، ترکی عثمانی و \"\n       \"روسی است. این حلقه ممکن است ولی سند ندارد.\"),\n     \"sources\": [W_QAFQAZ, W_KAFKAS],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. قوقاز\", \"stance\": \"silent\", \"note\": \"The page was fetched but returned no Arabic entry (no content), so the Arabic form could not be documented from Wiktionary.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. Kafkas (Turkish)\", \"stance\": \"partial\", \"note\": \"\\\"Inherited from Ottoman Turkish قافقاس (kafkas)\\\" and, for the given name, \\\"from West Circassian Къэфкъас (Qɛfqas), from Ancient Greek Καύκασος (Kaúkasos)\\\" — a non-Arabic route into the Islamic East.\"}\n     ]\n    },\n    {\n     \"id\": 14, \"lang\": \"Persian\", \"words\": \"qafqâz\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Persian قفقاز qafqāz 'the Caucasus' is certainly, at some remove, the Graeco-Latin Caucasus, so the top of \"\n       \"Nourai's chain is right; the disputable link is the Arabic mediation he inserts. The Persian shape with initial \"\n       \"q-, medial -f- and final -z matches Ottoman Turkish قافقاس Kafkas (< Circassian Qɛfqas < Gk. Καύκασος) and \"\n       \"especially Russian Кавказ Kavkaz, which is how the region's name entered 19th-c. Persian usage after the \"\n       \"Golestān (1813) and Torkamānchāy (1828) treaties, rather than any classical Arabic form (the Arab geographers \"\n       \"write al-Qabq). Wiktionary offers yet another account — \\\"ultimately from Middle Persian *Kaf kōf ('Mount Qāf')\\\" \"\n       \"— which looks like the Islamic-era reinterpretation of the name as the mythical Mount Qāf rather than a real \"\n       \"etymology, and is given without a source. Dehkhoda's long article (via abadis.ir) describes the region at length \"\n       \"but offers no etymology. So: right ultimate origin, unproven Arabic step.\"),\n     \"derivation_fa\": (\"«قفقاز» فارسی بی‌گمان در نهایت همان Caucasus یونانی‑لاتینی است و بالادستِ زنجیرهٔ نورایی درست است؛ آنچه \"\n       \"محل تردید است حلقهٔ عربی است که او افزوده. صورت فارسی با «ق» آغازین، «ف» میانی و «ز» پایانی با ترکی عثمانی «قافقاس» \"\n       \"(از چرکسی Qɛfqas از یونانی Καύκασος) و به‌ویژه با روسی Кавказ می‌خواند؛ همین راه است که پس از عهدنامه‌های گلستان \"\n       \"(۱۲۲۸ ق) و ترکمانچای (۱۲۴۳ ق) نام این سرزمین را در فارسی سدهٔ سیزدهم رواج داد، نه صورتی عربی (جغرافی‌نویسان عرب \"\n       \"«القبق» می‌نویسند). ویکی‌واژه روایت دیگری می‌آورد — «در نهایت از فارسی میانه *Kaf kōf، کوه قاف» — که بیشتر \"\n       \"بازتفسیر اسلامیِ نام بر پایهٔ کوه اسطوره‌ای قاف می‌نماید تا ریشه‌شناسی، و بی‌مأخذ آمده است. دهخدا نیز شرح مفصل \"\n       \"جغرافیایی می‌دهد ولی ریشه‌شناسی ندارد. خاستگاه نهایی درست است؛ گامِ عربی اثبات‌نشده.\"),\n     \"sources\": [W_QAFQAZ, A_QAFQAZ, W_KAFKAS, W_KAVKAZ],\n     \"ref_check\": [\n      {\"ref\": \"MON5:1474\", \"status\": \"not_checked\",\n       \"note\": (\"MON vol. 5 is the اعلام (proper-names) volume of the six-volume Farhang-e Fārsi, which refs_online.json \"\n        \"records as not digitised anywhere and not served by vajehyab/abadis (their Moʿin data has no proper-name entries). \"\n        \"Cross-checked instead against Dehkhoda via abadis.ir, whose قفقاز article gives the geography but no etymology.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. قفقاز (Persian)\", \"stance\": \"contradicts\", \"note\": \"\\\"Ultimately from Middle Persian *Kaf kōf ('Mount Qaf').\\\" — an unsourced rival account that bypasses Greek/Latin/Arabic altogether.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. Кавказ (Russian)\", \"stance\": \"partial\",\n       \"note\": \"\\\"From Ancient Greek Καύκασος (Kaúkasos), ultimately of Iranian origin ... according to Vasmer and Trubachyov the current form Кавказ (Kavkaz) stems from French Caucase and German Kaukasus.\\\"\"},\n      {\"src\": \"Dehkhoda\", \"where\": \"abadis.ir, لغت‌نامهٔ دهخدا s.v. قفقاز\", \"stance\": \"silent\",\n       \"note\": \"«قفقاز. [ ق َ ] ( اِخ ) نام ناحیه ای است بین دریای سیاه و بحر خزر ...» — a long geographical/historical article with no word-origin note.\"}\n     ]\n    },\n    {\n     \"id\": 15, \"lang\": \"English\", \"words\": \"Caucasian\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English Caucasian is Latin Caucasus + the adjective suffix -ian: 'of the Caucasus mountains' from 1807, \"\n       \"'native of the Caucasus' from 1843. The racial sense is a separate, datable coinage: J. F. Blumenbach applied \"\n       \"Caucasian (in Latin, 1795) to the 'white' race because the finest skull in his collection was a Georgian one, and \"\n       \"the term entered English in that sense by 1830; it has since been abandoned as an anthropological term. The \"\n       \"formation and the Latin/Greek source are exactly as the chart draws them.\"),\n     \"derivation_fa\": (\"انگلیسیِ Caucasian از لاتینیِ Caucasus با پسوند صفت‌ساز -ian ساخته شده است: به معنای «وابسته به کوه‌های \"\n       \"قفقاز» از ۱۸۰۷م و «بومی قفقاز» از ۱۸۴۳م. کاربرد نژادی آن ساخته‌ای جداگانه و تاریخ‌دار است: بلومنباخ در ۱۷۹۵م (به \"\n       \"لاتین) این واژه را بر نژاد «سفید» نهاد، چون زیباترین جمجمهٔ مجموعه‌اش گرجی بود؛ این معنا از ۱۸۳۰م به انگلیسی راه \"\n       \"یافت و امروزه در انسان‌شناسی متروک است. ساخت واژه و خاستگاه لاتینی‑یونانی آن دقیقاً همان است که نمودار نشان \"\n       \"می‌دهد. ادعای نورایی درست است.\"),\n     \"sources\": [E_CAUCASIAN],\n     \"ref_check\": [\n      {\"ref\": \"KLN:252\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 143 s.v. Caucasian: \\\"Formed with suff. -ian fr. L. Caucasus, fr. Gk. Kaukasos ...\\\" — the Latin → English step exactly as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Etymonline\", \"where\": \"s.v. Caucasian\", \"stance\": \"supports\",\n       \"note\": \"\\\"1807, of or pertaining to the Caucasus Mountains (q.v.), with -ian. Applied to the 'white' race 1795 (in Latin) by German anthropologist Johann Friedrich Blumenbach ... 'Caucasian' (n.) 'resident or native of the Caucasus,' 1843.\\\"\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. Caucasian (p. 252)\", \"stance\": \"supports\", \"note\": \"See ref_check; Klein also cross-lists Caucasian under caustic among the derivatives of I.-E. *keu- 'to burn'.\"}\n     ]\n    },\n    {\n     \"id\": 16, \"lang\": \"Greek\", \"words\": \"kauma; holo-kaustos\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both Greek words are regular formations on the same root. καῦμα, gen. καύματος 'burning heat, the heat of \"\n       \"the sun' is *kaw-mn̥, the -mα noun of καίω (Pokorny 595 lists καῦσις, καῦμα beside κᾶλον under keu-2). ὁλόκαυστος \"\n       \"'burnt whole', neuter ὁλόκαυστον used as a noun, is ὅλος 'whole' (PIE *sol-, Nourai's ☞Sol cross-reference) + \"\n       \"καυστός, the verbal adjective of καίω; it is the Septuagint's technical word for the whole burnt offering of \"\n       \"Leviticus, which is how it passed into Christian Latin and thence into the European languages. Klein's caustic \"\n       \"entry, which is Nourai's KLN:253, gathers exactly this family (calm, caustic, cautery, encaustic, holocaust, \"\n       \"hypocaust) under I.-E. *keu-, *kū- 'to burn'.\"),\n     \"derivation_fa\": (\"هر دو واژهٔ یونانی ساخت‌های قاعده‌مند همین ریشه‌اند. καῦμα «گرمای سوزان، تفِ آفتاب» از *kaw-mn̥ است، \"\n       \"یعنی اسمِ -ma از καίω (پوکورنی ص ۵۹۵ همراه καῦσις و κᾶλον آورده است). ὁλόκαυστος «به‌تمامی سوخته» (خنثی: \"\n       \"ὁλόκαυστον در کارکرد اسم) از ὅλος «همه» (هندواروپایی *sol-، همان ارجاع ☞Sol نورایی) و καυστός، صفت فعلی καίω، \"\n       \"ساخته شده و اصطلاح ترجمهٔ سبعینی برای «قربانی تمام‌سوز» سِفر لاویان است؛ از همین راه به لاتینی مسیحی و سپس به \"\n       \"زبان‌های اروپایی رفته است. مدخل caustic در کلاین (همان KLN:253) دقیقاً همین خانواده را زیر ریشهٔ *keu- گرد \"\n       \"می‌آورد. ادعای نورایی درست است.\"),\n     \"sources\": [E_HOLO, E_CALM, W_KAIO],\n     \"ref_check\": [\n      {\"ref\": \"KLN:253\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 143-144 s.v. caustic: \\\"fr. Gk. kaustikos ... fr. kaustos, 'burnt', verbal adj. of kaiein ... fr. I.-E. base *keu-, *kū-, 'to burn, heat' ... Cp. caeoma, caliber, calm, catacaustic, Caucasian, cautery, diacaustic, encaustic, holocaust, hypocaust, ink, Nausicaa.\\\"; and leaf 397 s.v. holocaust: \\\"fr. Gk. holokauston, lit. 'a thing wholly burnt', neut. of the adj. holokaustos, which is compounded of holos, 'whole' (see holo-), and kaustos, verbal adj. of kaiein (for *kaFiein), 'to burn'.\\\"\"},\n      {\"ref\": \"POK:595\", \"status\": \"supports\", \"note\": POK_QUOTE + \" — καῦσις and καῦμα 'blaze' are listed there by name.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I p. 376\", \"stance\": \"supports\", \"note\": WLD_QUOTE + \" — καῦσις, καῦμα appear in the same list.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kēu-\", \"stance\": \"supports\", \"note\": AHD_QUOTE},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. holocaust\", \"stance\": \"supports\",\n       \"note\": \"\\\"from Greek holokauston 'a thing wholly burnt,' neuter of holokaustos 'burned whole,' from holos 'whole' (from PIE root *sol- 'whole, well-kept') + kaustos, verbal adjective of kaiein 'to burn'.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 17, \"lang\": \"Latin\", \"words\": \"cauma; holocaustum\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both Latin words are borrowings of the Greek ones, and both are Late/Church Latin. cauma, gen. caumatis \"\n       \"'the great heat (of the day)' is a straight take-over of καῦμα by the language of the Church (Ernout-Meillet p. 191: \"\n       \"\\\"cauma, -atis n.: forte chaleur. Emprunt fait par la langue de l'Église au gr. καῦμα\\\"); from Vulgar/Late Latin it \"\n       \"gave Old Italian calma and Old French calme, and the 'resting period' component of Nourai's gloss is the received \"\n       \"explanation of the semantic slide — Webster puts it as \\\"LL. cauma, the heat of the sun ... probably from the \"\n       \"period of rest, during mid-day\\\", i.e. midday heat > the stillness of the siesta > 'calm'. holocaustum is the \"\n       \"Vulgate's rendering of ὁλόκαυστον for the burnt offering, whence Old French holocauste (12c.). Nourai's \"\n       \"AHD:191,629 are pages of the main American Heritage dictionary (calm, holocaust), which is not on disk, but \"\n       \"Watkins's IE appendix to the same dictionary lists CALM and HOLOCAUST under kēu- exactly as drawn.\"),\n     \"derivation_fa\": (\"هر دو واژهٔ لاتینی وام از یونانی‌اند و هر دو لاتینیِ متأخر/کلیسایی‌اند. cauma «گرمای سخت (نیمروز)» \"\n       \"برگردانِ بی‌واسطهٔ καῦμα است که زبان کلیسا وارد کرده است (ارنو–مییه، ص ۱۹۱: «وامی که زبان کلیسا از یونانی καῦμα \"\n       \"گرفته است»)؛ از لاتینی عامیانه/متأخر به ایتالیایی کهن calma و فرانسویِ کهن calme رسیده و جزءِ «هنگام آسودن» در \"\n       \"معنایی که نورایی آورده همان توضیح پذیرفته‌شدهٔ تحول معنایی است: گرمای نیمروز ← آرامش خوابِ نیمروز ← «آرامش» \"\n       \"(وبستر: «شاید از دورهٔ آسایش در میانهٔ روز»). holocaustum نیز برگردان ὁλόκαυστον در ترجمهٔ ولگات برای «قربانی \"\n       \"تمام‌سوز» است و از آن فرانسویِ کهن holocauste (سدهٔ دوازدهم) برآمده. ارجاع AHD:191,629 به صفحات فرهنگِ اصلی \"\n       \"American Heritage است که در دسترس نیست، اما پیوست ریشه‌های هندواروپایی واتکینز در همان فرهنگ CALM و HOLOCAUST را \"\n       \"دقیقاً ذیل kēu- می‌آورد. ادعای نورایی درست است.\"),\n     \"sources\": [E_CALM, E_HOLO],\n     \"ref_check\": [\n      {\"ref\": \"AHD:191,629\", \"status\": \"not_checked\",\n       \"note\": (\"Nourai's AHD numbers are pages of the main text of the American Heritage Dictionary, New College Edition \"\n        \"(1975/76) — p. 191 would be the calm entry, p. 629 holocaust — and only the Watkins IE appendix is available \"\n        \"locally (AHD_watkins1985.txt) plus the online appendix; the New College scans on archive.org are lending-only. \"\n        \"The appendix does list both words under the root: \" + AHD_QUOTE)}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 191 (LAT.txt leaf 209)\", \"stance\": \"supports\",\n       \"note\": \"\\\"cauma, -atis n.: forte chaleur. Emprunt fait par la l[angue] de l'Église au gr. καῦμα. M.1.1779.\\\"\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. calm (n.)\", \"stance\": \"supports\",\n       \"note\": \"WEB_vol1.txt line 26644-26645: \\\"[Fr. calme; LL. cauma, the heat of the sun; Gr. kauma, from kaiein, to burn; probably from the period of rest, during mid-day.]\\\" — supports both the Greek→Latin borrowing and Nourai's 'resting period' gloss.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. calm (p. 223) and chomage\", \"stance\": \"supports\",\n       \"note\": \"\\\"calm, n. — F. calme ... fr. It. calma, 'absence of wind, tranquillity', fr. Gk. kauma, 'burning heat of the sun', whence arose the meaning 'tranquillity of the sea during oppressive heat'\\\"; and s.v. chomage: \\\"fr. Late L. caumare, fr. cauma, 'tranquillity'.\\\"\"},\n      {\"src\": \"LEW\", \"where\": \"Walde 1910, grep for cauma\", \"stance\": \"silent\", \"note\": \"grep of LEW_1910.txt for 'cauma' returns nothing — the 2nd edition does not carry the Late-Latin loan.\"}\n     ]\n    },\n    {\n     \"id\": 18, \"lang\": \"English\", \"words\": \"calm; holocaust\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"calm entered English c. 1400 as a noun, 'absence of storm or wind', from Old French calme / Old Italian \"\n       \"calma 'quiet, fair weather', i.e. from Late Latin cauma; the figurative 'freedom from agitation' is 1540s. \"\n       \"holocaust is attested from the mid-13c. in the Biblical sense 'sacrifice by fire, burnt offering', from Old French \"\n       \"holocauste (12c.) or directly from Late Latin holocaustum; the sense 'massacre, destruction of a large number of \"\n       \"persons' is from the 1670s, and 'the Holocaust' as the name for the Nazi genocide only from 1957 (used of \"\n       \"Hitler's policies in English from 1942). Both are the ordinary Latin → Old French → Middle English route, and \"\n       \"both are listed under the burn-root by Klein and by Watkins.\"),\n     \"derivation_fa\": (\"«calm» حدود ۱۴۰۰م به‌عنوان اسم به معنای «نبودِ توفان و باد» از فرانسویِ کهن calme / ایتالیاییِ کهن \"\n       \"calma وارد انگلیسی شد، یعنی از لاتینیِ متأخر cauma؛ معنای مجازی «آرامش درونی» از دههٔ ۱۵۴۰م است. «holocaust» از \"\n       \"میانهٔ سدهٔ سیزدهم به معنای کتاب‌مقدسیِ «قربانی سوختنی» گواهی شده است، از فرانسویِ کهن holocauste (سدهٔ دوازدهم) یا \"\n       \"یکسره از لاتینیِ متأخر holocaustum؛ معنای «کشتار بزرگ» از دههٔ ۱۶۷۰م و کاربرد «The Holocaust» برای نسل‌کشی نازی \"\n       \"تنها از ۱۹۵۷م است. هر دو همان مسیر معمول لاتینی ← فرانسویِ کهن ← انگلیسیِ میانه را پیموده‌اند و کلاین و واتکینز \"\n       \"هر دو را ذیل ریشهٔ «سوختن» آورده‌اند. ادعای نورایی درست است.\"),\n     \"sources\": [E_CALM, E_HOLO],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed in this box; AHD:191,629 on the Latin box covers calm and holocaust, and Klein's caustic entry (KLN:253) lists both.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Etymonline\", \"where\": \"s.v. calm (n.)\", \"stance\": \"supports\",\n       \"note\": \"\\\"c. 1400, 'absence of storm or wind,' from the adjective or from Old French calme, carme 'stillness, quiet, tranquility,' or directly from Old Italian calma 'quiet, fair weather'.\\\"\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. holocaust (n.)\", \"stance\": \"supports\",\n       \"note\": \"\\\"mid-13c., 'sacrifice by fire, burnt offering,' from Old French holocauste (12c.), or directly from Late Latin holocaustum ... 'The Holocaust' ... first recorded 1957.\\\"\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. s.vv. calm, holocaust\", \"stance\": \"supports\",\n       \"note\": \"calm: \\\"F. calme ... fr. It. calma ... fr. Gk. kauma\\\"; holocaust: \\\"F. holocauste, fr. L. holocaustum, fr. Gk. holokauston\\\".\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. calm\", \"stance\": \"supports\", \"note\": \"\\\"[Fr. calme; LL. cauma, the heat of the sun; Gr. kauma, from kaiein, to burn ...]\\\"\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-283.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build283.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-283.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 283",
 "description": "Write and validate page-283.json"
}
```


### [2026-09-06T21:58:07.510Z] TOOL RESULT

```
written
JSON OK
nodes verified: 18/18
node verdicts: {'transcription_suspect': 1, 'confirmed': 10, 'disputed': 2, 'plausible': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'not_found': 3, 'not_checked': 12, 'partial': 2}
books consulted: {'supports': 37, 'silent': 13, 'partial': 12, 'contradicts': 5} | by book: {'Wiktionary': 13, 'KLN': 7, 'Etymonline': 7, 'BQT': 4, 'MON': 4, 'LKT': 4, 'WEB': 4, 'AHD': 2, 'PHD': 2, 'HRN': 2, 'HUB': 2, 'PLA': 2, 'Dehkhoda': 2, 'LEW': 2, 'LAT': 2, 'SYN': 1, 'NYB': 1, 'IEC': 1, 'ARY': 1, 'AFM': 1, 'FVQ': 1, 'POK': 1, 'WLD': 1}
```


## [2026-09-06T21:58:33.086Z] AGENT

Done. `data/verification/page-283.json` written; `verify_check.py 283` reports 18/18 nodes, 0 PROBLEM lines.

**Page 283 (book p. 253) — root Kŭ 1 / Kĕu 5 "to burn" (one entry, 18 nodes)**

Verdicts: root `confirmed`; nodes — 10 confirmed, 5 plausible, 2 disputed, 1 transcription_suspect.

Disputed / flagged:
- **#3 Persian کالا kālā** — `disputed`. Cannot come from MP kālbad; Wiktionary (and the Iranian literature behind it) derives it from Proto-Iranian *kar- "to make". Moʿin gives it no origin tag, and the cited IEC:1047 (Mann cols. 1047–48) is the lemma *quorpos-/quorquol-*, nothing about kālā. Nourai's own note concedes the path is unclear.
- **#5 Arabic qālib; q.l.b** — `disputed` by the worst-word rule. The borrowing قالب < Persian kālbod is confirmed by Nourai's own PLA:215 (Asbaghi p. 215, verbatim); but the root q-l-b "to turn" is inherited Semitic — the loanword was fitted to it, not the reverse. Klein routes the Greek word into Arabic via Aramaic instead of Persian (both routes defensible).
- **#1 Greek "Kalo / kalo-podein"** — `transcription_suspect`, `error_in: book`. I rendered PDF p. 283 at 300 dpi: the page really prints "kalo-podein", an impossible Greek form for καλοπόδιον (dimin. of καλόπους); "Kalo" also fuses καίω "burn" with κᾶλον "firewood". Extraction is faithful; page image copied to `data/verification/sources/refs/ocr/BOOK/283.png`.

**Extraction error the owner must fix** (`data/extracted/batch/page-283.json`): node **#4** (Persian kâleb/kâlbod) has `"parent": 0`, but on the printed page the arrow into that box comes out of the bottom-left of the **Pahlavi** box — parent should be **2**. (Cropped and read that region to confirm.)

Reference-page problems: **BQT:1095** and **BQT:1075** are both `not_found` — printed pp. 1075/1095 of the Moʿin edition are in the س section (سالار، سپیدبر). The کالب/کالبد entries with Moʿin's decisive footnote («پهلوی kālbad … مستعار از یونانی kalopódhion … عربی قالب») are at **printed p. 1577** (vol. 3, pdf p. 368), and they do support Nourai's chain. **IEC:1047** `not_found`; MON pages `not_checked` (6-vol edition still undigitised — cross-checked via abadis: کالبد «[په.]», قالب «[معر.]», کالیبر «[فر.]», کالا untagged). FVA has no digital copy.

Strong corroboration for the Greek → Pahlavi → Persian → Arabic core came from Nyberg II s.v. kālpaδ, MacKenzie, Horn no. 123 (pp. 282–83), Hübschmann, Moʿin's Borhān footnote, and Asbaghi p. 215. #11 (kau-casos) is `plausible` but Nourai reverses Klein's segmentation: per Klein/Pliny the *first* element is *kreu- "ice" and the *second* (-kasis) the "shining" one. #13/#14 (Arabic → Persian قفقاز) `plausible`: ultimate Greek origin right, but the modern form more likely came via Ottoman Turkish/Russian.

19 web sources archived via `fetch_source.py`.
