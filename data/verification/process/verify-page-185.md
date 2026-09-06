# Verification process log — verify-page-185


## [2026-09-05T20:56:12.440Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 185 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-185.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-185.json. Write /home/sfmqrb/git/rishe/data/verification/page-185.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 185` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:56:14.078Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:56:14.790Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:56:14.805Z] TOOL RESULT

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


## [2026-09-05T20:56:15.225Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-185.txt"
}
```


### [2026-09-05T20:56:15.241Z] TOOL RESULT

```
1	=== PDF page 185 (book page 155) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gheis, Gheizd : to frighten, to be angry  (refs POK:427)
4	#1 (parent #0) [Avestan] refs=POK:427; KLN:655 | zaěša, zaěšta : terrible, ugly ; zôišnu : shuddering ; zôižd-išta : most abominable ☞Isto
5	  #2 (parent #1) [Persian] refs=BQT:1021; HRN:147 | zešt «زشت» : ugly
6	  #3 (parent #1) [Sogdian] refs=SOD:472 | žyšt : ugly
7	#4 (parent #0) [Germanic] refs=AHD | gaistaz : a ghost
8	  #5 (parent #4) [English] refs=None | ghost
9	--- entry 1 ---
10	ROOT Gheizd -> redirect to Gheis
11	--- entry 2 ---
12	ROOT [Indo-European] Ghel : to shine, also a bright yellow color  (refs POK:429)  PART 1
13	#1 (parent #0) [Avestan] refs=POK:429; KLN:667; SOD:411 | zarena, zari, zaranya, zairita, zareta : golden, yellow
14	  #2 (parent #1) [Persian] refs=HRN:145; BQT:1012 | zar 1 «زر۱ ، زریر» : gold ; zard «زرد» : yellow ; zardak «زردک» : carrot ; zarnîx «زرنیخ» : arsenic
15	    #3 (parent #2) [Persian] refs=HRN:145; BQT:1012 | zargŭn «زرگون» : golden ☞Gěu 1
16	      #4 (parent #3) [French] refs=None | jargon : a yellow mineral
17	        #5 (parent #4) [English] refs=AHD:1489 | zircon ; zirconium
18	          #6 (parent #5) [Persian] refs=None |  «زیرکونیم»
19	    #7 (parent #2) [Arabic] refs=SKT:26; KLN:108 | az-zarnîx ☞Al 3
20	      #8 (parent #7) [Greek] refs=KLN:108 | arsenikon
21	        #9 (parent #8) [Latin] refs=None | 
22	          #10 (parent #9) [French] refs=None | 
23	            #11 (parent #10) [Persian] refs=VOP:41 | ârsenîk «آرسنیک» : arsenic
24	            #12 (parent #10) [English] refs=KLN:108 | arsenic
25	  #13 (parent #1) [Sogdian] refs=SOD:471 | zyrn : gold
26	#14 (parent #0) [Old Persian] refs=KNT:189 | daraniya : gold ; daraniya-kara : goldsmith ☞Kwer
27	#15 (parent #0) [Avestan / Old Persian] refs=POK:429 | zahr, zara 1 : bile
28	  #16 (parent #15) [Persian] refs=None | zahreh «زهره» : bile, courage
29	
```


## [2026-09-05T20:56:18.251Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-185.json",
 "description": "Read source JSON for page 185"
}
```


### [2026-09-05T20:56:18.285Z] TOOL RESULT

```
{
  "pdf_page": 185,
  "book_page": 155,
  "entries": [
    {
      "root": {
        "name": "Gheis, Gheizd",
        "lang": "Indo-European",
        "refs": "POK:427",
        "gloss": "to frighten, to be angry"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:427; KLN:655",
          "words": [
            {"translit": "zaěša, zaěšta", "gloss": "terrible, ugly", "script": null},
            {"translit": "zôišnu", "gloss": "shuddering", "script": null},
            {"translit": "zôižd-išta", "gloss": "most abominable", "script": null, "see": ["Isto"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1021; HRN:147",
          "words": [
            {"translit": "zešt", "gloss": "ugly", "script": "زشت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:472",
          "words": [
            {"translit": "žyšt", "gloss": "ugly", "script": null}
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
            {"translit": "gaistaz", "gloss": "a ghost", "script": null}
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
            {"translit": "ghost", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gheizd",
        "redirect": "Gheis"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ghel",
        "lang": "Indo-European",
        "refs": "POK:429",
        "gloss": "to shine, also a bright yellow color"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:429; KLN:667; SOD:411",
          "words": [
            {"translit": "zarena, zari, zaranya, zairita, zareta", "gloss": "golden, yellow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:145; BQT:1012",
          "words": [
            {"translit": "zar 1", "gloss": "gold", "script": "زر۱ ، زریر"},
            {"translit": "zard", "gloss": "yellow", "script": "زرد"},
            {"translit": "zardak", "gloss": "carrot", "script": "زردک"},
            {"translit": "zarnîx", "gloss": "arsenic", "script": "زرنیخ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:145; BQT:1012",
          "words": [
            {"translit": "zargŭn", "gloss": "golden", "script": "زرگون", "see": ["Gěu 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "jargon", "gloss": "a yellow mineral", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:1489",
          "words": [
            {"translit": "zircon", "gloss": null, "script": null},
            {"translit": "zirconium", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": null, "gloss": null, "script": "زیرکونیم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 2,
          "lang": "Arabic",
          "refs": "SKT:26; KLN:108",
          "words": [
            {"translit": "az-zarnîx", "gloss": null, "script": null, "see": ["Al 3"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Greek",
          "refs": "KLN:108",
          "words": [
            {"translit": "arsenikon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "VOP:41",
          "words": [
            {"translit": "ârsenîk", "gloss": "arsenic", "script": "آرسنیک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "English",
          "refs": "KLN:108",
          "words": [
            {"translit": "arsenic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:471",
          "words": [
            {"translit": "zyrn", "gloss": "gold", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:189",
          "words": [
            {"translit": "daraniya", "gloss": "gold", "script": null},
            {"translit": "daraniya-kara", "gloss": "goldsmith", "script": null, "see": ["Kwer"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:429",
          "words": [
            {"translit": "zahr, zara 1", "gloss": "bile", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "zahreh", "gloss": "bile, courage", "script": "زهره"}
          ],
          "note": null,
          "quote": {
            "text": "زهره ندارم که بگویم تو را - بی من بیچاره چرا بوده ای",
            "poet": "Molavî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:56:19.000Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:56:19.037Z] TOOL RESULT

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


## [2026-09-05T20:57:07.489Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','BQT','SOD','KNT','SKT','AHD','VOP','MON','BRT','PHD','NYB','ARY','HUB','LKT','FSD','WEB','IEC','SYN','WLD','ISS','CHEUNG','PLA','AFM','FVQ','DEV','PHN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\""
}
```


## [2026-09-05T20:57:08.619Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-124.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-05T20:57:09.289Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file ha
== CHEUNG MISSING
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
```


### [2026-09-05T20:57:11.041Z] TOOL RESULT

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
{
 "entry": 0,
 "root": "Dhě 2",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
 "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
 "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
 ],
 "ref_check": [
  {
   "ref": "AHD:1512",
   "status": "supports",
   "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ...
```


## [2026-09-05T20:57:17.209Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ĝheis\"; grep -n -i \"ĝhei-s\\|ghei-s\\|zaesa\\|zaēša\\|zōiš\\|zoiz\\|zaēšta\" POK_full.txt | head -30\necho \"=== POK page 427 area\"; grep -n \"427\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:57:17.276Z] TOOL RESULT

```
=== POK ĝheis
32621:Material: Avestan zaesa-' gruesome' 
32627:zoisnu-^ frightening, shuddering, shaking together (before frost)', zoizdisto^ of the 
32642:angry '; Avestan zoizdista- {see above); 
36122:have derived ' wound, hurt ' (group B) (root form ghei-s-). 
=== POK page 427 area
32559:Page(s): 426-427 
32611:Page(s): 427 
32653:Page(s): 427 
37378:compare S. 427; 
37552:S. 427. 
37909:Commentary: Delocatival formation, as per Kimball, Hittite Plene Writing 42720, NOT 
39370:'throat' (also krcum ' gnaw '?? Pedersen KZ. 39, 427); 
46429:References: WP. I 427, Trautmann 129, Specht Indo Germanic Dekl. 141, 169. 
50540:References: WP. I 427, Trautmann 305. 
56797:References: WP. II 427, Berneker 713 f. 
59090:References: WP. II 291 f., WH. II 370, 427 f.
```


## [2026-09-05T20:57:18.632Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 offset: leaf = p - 344\"; python3 - <<'EOF'\nimport io\np=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(p))\n# leaf = p - 344 -> printed 427 => leaf 83\nfor n in (82,83,84):\n    print('---- leaf',n)\n    print(p[n][:2500])\nEOF"
}
```


### [2026-09-05T20:57:20.702Z] TOOL RESULT

```
=== POK_02 offset: leaf = p - 344
434
---- leaf 82
Thurneysen  KZ.  59,  2,  8;  61,  253);  acymr.  gaem.^  ncymr. gauaf)  acorn.  goyf,  bret.  goaJW,  gall.  Wintermonat  Giamon\ios\,  Eigenname
426  ,
Giamülus,    weitergebildet   mir.   gem-rad   n.,   mcymr.   gaeaf-raicd   ,Wintei (*ghii,mo-röto-,  zu  ret-  ^laufen') ;  auch  ir.  gamuin  ^jähriges  Kalb';
aisl.  göi  f.  und  gx  t,  göi-mänadr  ,der  Monat  von  Mitte  Februar  bis Mitte  März^  isl.  göa,  u.  f.,  norw.  gje  L,  schwed.  göjemänad  (gö-  <  giö-  nach Bugge  Ark.  f.  nord.  Fil.  4,  123  ff.).
Fraglich  die  Anreihung  von  an.  gcmall  ,^\l',  gemlingr  .jähriges  Schaf« ags.  gamol  ,alt',  gamellan  ^altern',  as.  gigamalod  ,bejahrt'_,  ahd.  nur  in Ei<''ennamen  wie  Gamalholdy  Gamalherht,  Gamalbevga  usw.  als  , bejahrt* vffl.  lat.  annösiis.
C.  ghimo-  (aus  ghi-mn-o-?):
Ai.  himd-h  m.  J\älte,  Frost,  Schnee',  Mmä  f.  ,Winter',  av.  zdmaka-  m, ,Wintersturm'  (vgl.  den  Gen.  von  zyäizimö  unter  B.);
^v.  Svaxi^tog  ^winterlich,  stürmisch',  6  yjfxagog  , Ziegenbock',  gj  X^hCiQog ,die  einjährige  (Ziege)',  %ii.iaiQa  ;Ziege',  lat.  hlmus  (<  HiUmos),  trimui^ quadrimus  ,zwei-  usf.  jährig'  (vgl.  ved.  satd-hima-  ,hundertjährig'),  norw. dial.  gimber,  schwed.  dial.  gimber^  dän.  gimmerlam  , weibliches  Lamm', dial.  aber  ^einjähriges  Lamm'  (Pedersen  KZ.  32,  248),  andfrk.  (Lex  Salica) ingimus?  ,porcus  anniculus'.  Die  Formen  mit  y:  aisl.  gymbr  , ein  jährige Sau',  norw.  gymber,  schwed.  gymmer  ,Lamm'  beruhen  wahrscheinlich  au£ Einfluß  des  nicht  verwandten  —  übrigens  ungedeuteten  —  aisl.  gymhill^ PN  GumbuU,  aschwed.  guwmerlamb  ,Widder',  isl.  gummarr,  norw.  gumse, schwed.  gumse  ,Widder',  siehe  Hellquist  SvEO.  210.
WP.  I  546  ff.,  WH.  I  106,  645  f.,  Trautmann  367,  Specht  KZ.  53,  307  f.
gheidh-  , begehren,  gierig  sein';  gheidh-tlo-  , Bürgschaft,  Pfand';  vgl.  gheigh-,
Air.  glall  =  cymr.  givystl,  acorn.  guisfel  , Geisel',  bret.  goestl  ,gage, caution',  gall.  in  Congeistlus  MN.  (cymr.  cyngwystl  , Verpflichtung')  =  ahd. gisal,  nhd.  Geisel,  ags.  gisel,  aisl.  gisl  ds. ;  die  genaue  Übereinstimmung zw.  Germ,  und  Kelt.  spricht  vielleicht  für  Entlehnung  seitens  des  Germ.; got.  PN  Glsla-mun-dus  \  daneben  ohne  l:  got.  PN  Ända-gls,  ags.  Gls-ioulf, ahd.  Glsi-ulf,  vgl.  mnd.  glse  , Geisel'.
Mit  Ablaut  hierher  ir.  gell  , Einsatz,  Pfand'  {^ghistlo-),  wovon  das  Verbum air.  gel
---- leaf 83
se'  (3.  Sg.  Konj.  gellaid,  3.  PI.  Fut.  gillfit), mit  ad-  , schwören,  versprechen'  usw. ;  von  glall  , Geisel'  stammt  das  Verbum giall-,    geill-    , dienen,    gehorchen',   z.  B.  3.  Sg.  giallaid,  Fut.  3.  PL  geillfit.
Ahd.  mhd.  git  .Gierigkeit,  Habgier,  Geiz',  ahd.  gltag  , gierig,  habgierig, geizig',  mhd.  giten  und  gU{e)sen  ,gierig,  habgierig  sein'  (aus  letzterem  das z  von  mhd.  gize,  dt.   Geiz),  ags.  gitsian  , begehren',  gitsung  , Habgier' ;
lit.  geidziü  geisti  ,begehren,  verlangen,  wünschen',  geidduju,  -ti  ,wünschen, verlangen',  gaidas  ,heftiger  Wunsch,  Verlangen',  dial.  gidis  , gierig';  lett. gäidu,    gäidit    , warten'    (ursprgl.  Iterativ),    gaida    , Erwartung',  dzidris  (?)
427
Durst';    apr.   geidi,    gieide    ,sie    warten',    sengijdi    ,er    erlange',    sengidaut ^erlangen* ;
aksl.  zidQ,  Hdati  (danach  auch  zhdg)  , warten';  tmss.  zdu,  ^ddtb  , warten'.
WP.  I  553,  Trautmann  82,  Pokorny  Urillyrier  b6\  WH.  I  576,  632,  641.
gheigh-  , begehren,  gierig  sein'  (s.  auch  das  ähnliche  gheidh-)??
Ai.  jeh-  nur  in  jBhamäna-h  , gähnend,  den  Mund  aufsperrend,  klaffend, lechzend';  vielleicht  sekundär  zu  jiklte,  S.  418 ;
got.  faihu-geigan  , begehren',  ga-geigan  , gewinnen',  nasaliert  ahd.  gingen ,nach  etwas  verlangen',  g'mgo  ,das  Verlangen' ;  nach  Wissmann  Nom. postverb.  41  jedoch  zu  ghei-gh-,  oben  S.  421.
lit,  äpmandq  giezti  , Groll  hegen',  gieziüos  , heftig  verlangen',  pagiezti ,nach  Rache  verlangen',  pagiezä  , Rachgier';  falls  lit.  giezti,  pa- giezti  intr. ,im  Halse  kratzen'  damit  identisch  wäre,  müßte  obige  Zusammenstellung fortfallen.
WT.  I  552:  anders  Feist  136  f.
gbeis-  und  gheiz-d-  ,aufgebracht,  bestürzt,  erschreckt  (sein)' ;  gheizdbo-s , Erregtheit';  ursprüngliche  Gleichheit  mit  ghei-,  ghei-s-  in  ai.  hinöti usw.  ist  sehr  wahrscheinlich.
Av.  zaesa-  , schauderhaft',  zöisnu-  , zusammenschreckend,  schaudernd, bebend  (vor  Frost)',  züizdistö  ,der  schauderhafteste,  abscheulichste'  (Superl. zu  einem  Verbum  *zöizdä-  , schaudern  machen' ;  s.  unten  gheiz-d-) ;
got.  us-geisnan  , erschrecken  (intr.),  außer  Fassung  geraten',  Kaus. us-gaisjan  , erschrecken  (tr.),  außer  Fassung  bringen'  (aber  aisl.  geisa , hervordringen,  heranstürmen'  aus  *ga-eisa) ;
aisl.  geiski  n.  , Schreck,  Entsetzen'.
Wurzelform  gheiz-dh-:  ai.  hed-  , zürne
---- leaf 84
 as.  gest,  ags.  gast  {gcest)  m.  , Geist  (im  Ge- gensatz zum  Körper) ;  überirdisches  gespenstiges  Wesen'  (so  bes.  engl,  ghost , Gespenst'),  ags.  gcestan  (^gaistjan)  , erschrecken'  (tr.),  engl,  aghast  , auf- geregt, zornig',  ghastly  , gräßlich,  entsetzlich,  furchtbar'.
Das  in  der  Bed.  genau  stimmende  aksl.  zasnotl  , erschrecken  (intr.), stupefieri',  zasiti  , erschrecken'  (tr.),  ^Lzas^  , Schrecken'  aus  *^(Ä)ös-  stimmt im  Vokal  und  im  Guttural  nicht.
WP.  I  553  f.,   Feist  531  f.
428  •
g-liei-  .rufen,  schreien^  auch  in  Vogelnamen,  mit  -b-,  -hh-  und  -d-  erweitert
Vgl.  die  ähnlichen  Schallwurzeln  gal-,  qel-.  .^v
Ai.  pra-galbhd-h  .mutig,  entschlossen'  (:  ahd.  gelbön);  *^',:
gr.  xeliötbv  , Schwalbe',  älter  xelldfcDv]  das  den  hellen  Schall  malende -I-  erinnert  an  mhd.  glien  ,schreien,  bes.  von  Raubvögeln',  redupl.  gr.  -^^^^ syrak.  xi/tJA«  , Drossel';
aisl.  gjalla  (st.  V.)  ,ertönen',  ags.  giellan  (st. V.)  ,schreien',  ahd.  gellan  ,töaen, klingen,  schreien',  nhd.  gellen  (-11-  aus  -In-  oder  eher  rein  schallmalende Konsonantenschärfung) ;  anord.  gala  (Prät.  göT)  , schreien,  krähen,  singen*, ags.  as.  ahd.  galan  ,singen;  auch  incantare,  behexen,  bezaubern'  (germ. Präs.  mit  -a-  auf  Grund  eines  Perf.  mit  idg.  ö);  got.  göljan  ,grüßen' (eigentlich  ,*zurufen',  wie  afries.  gela  ,jagen'  eigentlich  ,das  Wild  durch Geschrei  aufstöbern';  dehnstufiges  Iterativ,  vermutlich  Denominativ)  anord. gela  ,vergnügt  machen,  trösten',  as.  göUan  , erfreuen';  ahd.  guol-llh  ,prah- lend',  ur-guol  ,berühmt' ;  ahd.  as.  galm,  mhd.  galm,  gelm  m.  , Schall,  Lärm', ahd.  nahti-gala  f.  ,Nachtigall',  aisl.  galdr  m.  ,das  Singen,  Zauberlied',  ags. gealdor  n.  , Zauberlied',  ahd.  galdar,  kalter  und  galstar  n.  ds.,  aisl.  gallv, gjallr  ,klingend' ;
ö-stufig  (wie  got.  göljan)  russ.  galitb-sja  , verspotten',  dial.  galücha,  gah  f. ,Spaß,  Gelächter',  nagdlith  , taktmäßig  schreien,  singen,  bei  der  Arbeit'  usw.
b-  und  bh-Erweiterung :
ags.  gleljpan  (st.  V.)  ,prahlen',  mhd.  gelpfen,  gelfen  , schreien,  singen, prahlen',  aisl.  gjalp  n.  , Prahlerei',  ags.  gielp  ds.,  as.  gelp  , Trotzrede,  Hohn', ahd.  gelph  , Trotzrede,  Prahlerei',  adj.  ,lustig,  übermütig',  ahd.  gelb^ ,jemd.  täuschen',  as.  galpön  (schw.  V.)  ,laut  schreien,  prahlen',  dän.  gylpe, gulpe  , schluchzen
```


## [2026-09-05T20:57:29.007Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '32600,32660p' POK_full.txt"
}
```


### [2026-09-05T20:57:29.074Z] TOOL RESULT

```
Gothic faihu-geigan'\\is\., crave', ga-geigan^ gain ', nasalized Old High German gingen 
"after etwas verlangen', ^//7^c»"das Verlangen'; after Wissmann Nom. postverb. 41 though 
to ghei-gh; above S. 421. 

Lithuanian apmaudqgiezti^ hold a grudge, nurse a grievance ', gieziuos' long, want 
violently ', pagiezti' ask for revenge ', pagieza^ thirst for revenge '; whether Lithuanian 
giezti, pa-giezti\x\\x. " im Halse kratzen ' would be with it. 

References: WP. I 552; different Feist 136 f. 
Page(s): 427 

Root / lemma: gheis- and gheiz-d- 



Meaning: confused, shocked 

Note: original resemblance with ghei-, ghe/-s-\n Old Indie h/not/ etc. is very probably 

Material: Avestan zaesa-' gruesome' 

Note: 

Reduplicated laryngeal in -h2™ahre- > Avestan -ae- 

zoisnu-^ frightening, shuddering, shaking together (before frost)', zoizdisto^ of the 

ghastliest, most hideous ones ' (Superl. to a verb *zdizda- ' make shudder '; see below 

gheiz-d-)\ 

Gothic us-geisnan^ erschrecken (intr.), au(ler£assung geraten ', Kaus. us-gaisjan^ 
erschrecken (tr.), aufter Fassung bringen ' (but Old Icelandic ^e/isa ' hervordringen, 
heranstijrmen ' from *ga-eisa)\ 

Old Icelandic geiskiu. " fear, horror '. 

root form gheiz-6^-:0\6 Indie hed- 'be angry with' {ahedant-, ahedamana-h, Perf. jihTda), 
heda-h rw., hedahu. "anger' (here also helate' is improvident ', helayati^ deride ', see 
be\o\N ghe/-' yawn '), hTdati^ excited, aroused, aggrieved ', Med. 'is excited, aroused, 
angry '; Avestan zoizdista- {see above); 

Old High German geist{= Old Indie heda-li) m.. Old Saxon gest. Old English gast 
{gsestj m. 'ghost (in contrast to the body); uberirdisches gespenstiges Wesen ' (so esp. 
engl. ^/7c»s/' ghost'). Old English gsestan {*gaistjan) 'frighten' (tr.), engl. aghasf agitated, 
angry, irate', ghastly^ grisly, terrible, dreadful'. 

That in the meaning exact attuning Old Church Slavic za5/7(?// "frighten (intr.). stupefied ', 
zas/// "frighten' (tr.), uzast 'fright' from *g(h)ds- aWuues in vowel and not in guttural. 

References: WP. I 553 f.. Feist 531 f. 
Page(s): 427 

Root / lemma: ghel(e)gh- 

Meaning: a kind of metal 

Material: Old Church Slavic *zelezo\x\ zelez(b)n-b ' iron', Serbo-Croatian zeljezo, russ.
```


## [2026-09-05T20:57:30.423Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD ghost/gheis\"; grep -n -i \"gheis\\|gaistaz\\|ghost\" AHD_watkins1985.txt | head -20\necho \"=== KLN 1971 ghost\"; grep -n \"^ghost\\|ghost, n\\.\" KLN_1971.txt | head"
}
```


### [2026-09-05T20:57:30.483Z] TOOL RESULT

```
=== AHD ghost/gheis
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
682:lem-2. Nocturnal spirits. 1. Suffixed form *lem-or- in Latin lemurés, ghosts: LEMURES. 2. Suffixed variant form *lam-ya- in Greek lamia, monster: LAMIA. [Pok. 2. lem- 675.]
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1557:GAST gheis- GASTRIC gras- GASTRO- gras- GASTRULA gras- GATHER ghedh- GAUCHE weng- GAUD gau- GAUDY! gau- GauDY? gau- GAUGE ghalgh- GAUNTLET? klou- GAUR gWou- GAVEL? ghabh- GAWK ghow-é- GAYAL gWou- _ GEANTICLINE gé GEAR garwian GEGENSCHEIN gagina, skeei- GELANDESPRUNG lendh-2, spergh- GELATIN gel-3 GELATION gel-3 GELD! ghel-3 GELD2 gheldh- GELDING ghel-3 GELID  gel-3 GELIGNITE egni- GELT! gheldh- GEM gembh- GEMINATE yem- GEMINI yem- GEMMA gembh- GEMMATE gembh- GEMMULE gembh- GEMOT mdéd- GEMSBOK bhugo- GEMUTLICH mé-1 GEMUTLICHKEIT mé-1 -GEN gene- GENDARME gene- GENDER gene- GENEALOGY genoe- GENERAL gene- GENERATE genoe- GENERATION geno- GENERIC gene- GENEROUS gene- GENESIS gene- -GENESIS gene- GENIAL! gene- GENIAL? genu-2 GENICULATE genu-1 GENITAL gene- GENITIVE gene- GENITOR gene- GENIUS gene- GENOCIDE gene- GENOTYPE gene- GENRE gene- GENS gene- GENT! gene- GENTEEL gene-
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
2114:POLICE pele-3 POLICLINIC pela-3 POLICY! pele-3 POLICY? deik- POLIOMYELITIS pel-2 POLIS pele-3 POLISH pel-6 POLITIC pele-3 POLITY pele-3 POLKA pele-2 POLLEN pel-1 POLLEX pol- POLLUTE leu-2 POLTERGEIST bhel-4, gheis- POLTROON pau- POLY- pele-1 POLYGALA melg- POLYGLOT glégh- POLYGYNY gWen- POLYHISTOR weid- POLYMATH mendh-! POLYNYA pele-2 POLYP ped-1 POLYPNEA pneu- POLYPOD ped-1 POLYTECHNIC teks- POLYTENE ten- POLYTHEISM dhés- POLYTOCOUS tek- POLYTROPHIC threph- POMACE pomum POMADE pomum POME pomum POND bend- PONDER (S)pen- PONDEROUS (S)pen- PONIARD peuk- PONS pent- PONTIFEX dhé-!, pent: PONTIFF pent- PONTIL peuk- PONTINE pent- PONTOON pent- PONY pau-
=== KLN 1971 ghost
102354:ghost, n. — ME. gast, gost, fr. OE. gdst, ‘breath, 
102367:ghostly, adj. — ME. gostly , fr. OE. gastlic , ‘spir- 
106275:ghost, specter’, ON. grima, MDu. grime, ‘soot; 
186458:ghost’, fr. poltern, ‘to make a noise or row’, and
```


## [2026-09-05T20:57:35.930Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '102354,102372p' KLN_1971.txt"
}
```


### [2026-09-05T20:57:35.993Z] TOOL RESULT

```
ghost, n. — ME. gast, gost, fr. OE. gdst, ‘breath, 
spirit, soul, life’, rel. to OS. gest, OFris. jSst, 
gdst, MDu. gheest, Du. geest , OHG., MHG., 
G. geist , ‘spirit, ghost’, OE. gxstan, ‘to frighten, 
alarm’, fr. I.-E. base *gheizd -, ‘to frighten; to 
be angry’, whence also OI., hfyali, ‘wrath’, 
hidati, ‘excites, vexes*, Avestic zoizdishta -, 'the 
most abominable’. Base *gheizd is a -^-enlarge- 
ment of base *gheis - , whence Avestic zaesha -, 
‘horrible’, zoishnu ‘shuddering’, Goth, us- 
gais-jan, ‘to frighten’, ON. geiski, ‘fright, terror’, 
geis-ka-fullr , ‘terrible*. Cp. aghast, ghastly. Cp. 
also the second element in Zeitgeist, 
ghostly, adj. — ME. gostly , fr. OE. gastlic , ‘spir- 
itual’. See ghastly. 

Derivatives: ghost-li-ly , adv., ghost-li-ness , n, 
ghoul, n., an evil demon who robs graves and 
feeds on the dead. — Arab, ghiil, fr. ghdla, ‘he
```


## [2026-09-05T20:57:37.683Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\n# two printed pages per leaf; find leaf containing \"ghost\" headword\nfor i,p in enumerate(t):\n    if re.search(r'\\bghost, n\\.', p) or 'gaisto' in p.lower():\n        print('leaf',i, p[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:57:39.739Z] TOOL RESULT

```
903
```


## [2026-09-05T20:57:50.001Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT zaesa\"; grep -n \"zaēša\\|zaesa\\|zōišnu\\|zoisnu\\|zōižd\\|zoizd\" BRT.txt | head -20\necho \"=== BRT zaranya/zairi/zāra\"; grep -n \"zaranya\\|zairita\\|zairi-\\|zāra-\\|zara-\" BRT.txt | head -30"
}
```


### [2026-09-05T20:57:50.078Z] TOOL RESULT

```
=== BRT zaesa
4754:—  yal:iä  ro  data  °/il  (VP.)  spsntä  a^iä na  >räzäa?n  Y.5#.  5;  II.  iZ,  14.  i,  42.1, • — ■  mai^amnt  . .  yat  ksrmlun  "la  (NS.) sp>nta  vispe  hazaesaYLio.$i;  7.3',  /0.92, y.ga,  Y. 57.^23,  60.6;  —  /ml  '/ä  (NP.) spmtä  gaiia  giurvain  Y.2S.0;  Ny.l.i, VyL^o;- —  spmtsttg  °s3ng  yava^yff  yavaSsvB Y.,J.')-3;  4-A\  —  °^^  sptrüa  huxiäi:ra hmfmhs  (Stverz.)  Vr. ;/.  12;  usw.;  —  -sS spints  vatihali  srlräi^  namqn  äebaya  Y. /  5. 1 ;  Vr.  6.1;  —  vlspqscä  'iq  spintq  yasa- maidsY.42.()\  —  °h  spinlS alaonam  yasa- maideY.yi.2,  G.  2. 6  (wo  'sJtca);''*  — 'sanqm  sp)ntanqm  xialtanqm  vinzidsi- %ranqm  Ötnzatqm  aiwyämanqm  taxmanqm ähuiryanqm  ySi  aihy^anhs  alwvanB  ysi hapta  iam^.manavAö.. Yt  lj.82f.;Y.j. 4, 20,3;  — y3i  hapta  'sä  spmta  Yt.2.3;  — ape  °ianam  spmtanqm  dähXtn  Y./9.8;  Yt. ;^.  8 1 ' ;  —  vankubyS  yazataiibyS  yat  'laii- byS  spmtaHbys  Vr. 8.\;  ff. 4, 13. \,Yt.4.y,
28149:zoizdiSta-
28987:v^  tyä  Aacäma''  Aami%'iya  abavcC  Bh. 2.  2;  s,  ?.  5,  13',  5.  I.  i)zeiUich'\Qn. -  an,  inde  ab';  a)  im  jAw.:  ana  niam yasnayazaesa..A°  hU  vaxsa^ ä  Aufräsrnd.- diitsil  Yt.  5.  91 ;  —  kaAmai  A'  usaAinanqm gähantim  ratu/ri^  frajasaiti  N.  46;  *4y, *48,  4g,  50,  *$! ;  —  A'  Au  vaxiat  a  *Aa ''frälmd.datdit  pairisacaiti  N.  48;  4Ö,  47i 4(7—573;  —  fravasayS  . .  yi  h'  gayät matyhnat  ä  saosyantst  v»r3%raynat  Y.  26, 10.  "c)  im  Ap.:     «(Va*   xiah^am    A'
=== BRT zaranya/zairi/zāra
4180:•  j.  'anhuyav-  Adj.  'der  sich  (den  Anspruch auf)  das  (andere)    Leben  erwirbt':    zara-
4708:•  j.  anyö,  ainyö  Adv.  'ausser,  ausgenom- men, abgesehen  voa  — ',  mit  Abi.:  ^at  äs ma^änqm  ,  .  v3r>iravasl3mS  ain-  zara- %ulträ:  yt.jg.^6;  38;—  kakmai paoiryd malyänqm  "apir^si  (sd.)  tum  . .  an'  mana (statt  AbL)  yat  zaraittitnit  ,  .  ahntäi paoiryS  afi^Dse  (sd.)  az»m  an"  ^wat  yat tara>usträt  V.  2.  i  f.;  —  taii  also  s}a  .  , äamanqm  ham.rai'iviayeiti  . .  an'  ahmüt yS . .  "nicht  erstreckt  der  Hund  . .  auf  die Geschöpfe  . .  seinen  indirekten  EinBuss ausser  auf  den,  der  . ."  V.5.34;  —  kaf nä  *daivayasnai  vä  .  .  gSus  aiiiiitya  (sd.)
5480:kainlnö  kihrpa  srJrayh  Yt5.64;  —  bow- raini  vastrh  vat»hala  °dvl  süra  anilAi/a Yt.5. 129;  7,19,88,91,  95,96,  123,  127, laS;  —  avaj  nyapt^m  dazdi  me  vami/ii snisU  -dvliyS.)  süre  anil/iile  yäh  a  . .  Yt 5-  18;  9.  63.  77',  »S.  87,  90-  94.  130. 131,  Ny.  /.  19;  —  paili  dim  p»r>sal  zara- %uilrS  "dvltn  sürqnt  anahitqm  yt5.9o; I,  9,  62,  94,  Vr,2.  7,  Ny.4.9.
5830:•  j.,  g.  ast'vant-  Adj.  (fem.  'vaitt-)  'mit einem  stofflichen  Leib  versehen,  leiblich,  | stofflich,  materiell';  Ayat  'vant»m  dada uäatam  "als  du  Leben  mit  Leib  versahst" Y,_5/.  11;  —  tat  (näml.  mlidf/n)  er  mazdä vairlm  'vaits  ustänät  data  vatfhlus ^ttoiana  manar-ks ySi . .  "diesen  köstlichen (Lohn)  ja,  0  M.,  werdet  ihr  durch  das Wirken  des  VM.  dem  leiblichen  Leben (derer)  verschaffen,  die  . ,"  Y.54. 14;  — •vat  ahm  hyät  uslStiä  (sd.)  aojSrigAvat "^.43-  16;  —  ash-atjrmya%a  astva  *kqm ustanava  (sd.)  °vat  *ai^yeja/nm  paitisät Yt.  13. 1 29;  —  *vTjvähu  (sd.)  paiii  tanusti 'vh  gays  *däryeife  FTVf.4.2.  A)  sonst. nur  als  Beiwort  von  a)  stay-  (sd.) :  zara- , %ustrahe..yS paoiryö  stsis  'vadyä ..  Yt.ij.  1 Sgf«.  b)  gai^ä-  (sd.),  Sg.  und  Plur.J darfsca  (sd.)  da^at^amirixfyantim  vTspatn yam  "vaitlm  gae^qm  Yt  i<).  94;  Y.  g.  8, 37.23,  *Vd.£'>;  —  zarai:mtr5  ratus 'vai>ya  gaf^ayä  Yt.  73.  4r;  j.  89;  — kat»  %wqm  paoiryS  'vai^yäi  hunüta gai^yäi  Y.p.  3;  4;  —  m/l  m?m>cainTs gai>a  'vaitls  asake  SrB._j;  Yt/5.  41,  V. , ^^•SS;  —  "J  ^^  apqm  a'javö..  jasanli..' yavanqm  .  .  västranqm  ,  ,  gafianamüa 'vaitinqm  Yt  ^'.29;  —  V?'"  ■  ■  /rävavacä .  .  zara'iuströ  gae'iabyö  'vaiHbyS  Y.ö'j.g; P.  13;  —  ahura  mazda  mainyö  spinista däiar>  gad'^ariqm  'vaitinqm  asäum  ''" I.  7- 1.  9- 1,  lo- ".  "■  I.  '4-  I,  34,  K
6082:jrjmuibmS  Y.57.4;  7.1,  2^.2;  —  zara- ^BsTrvm  .  .  yat  as  °hm  alavasfornd  (sd.) .■V._y.  4;  — j'aia  °ä7/  x!a%tym  cinasti  (sd) Y.20,3"';  —  äat..  ah<  nmänahe fraf^wd gäus  .  .  'um  .  .  i-ästrpm  V.J.  3;  —  asis/a itä  airihat  haca  vlsat  gaul  buyat  asUbm •am  Y.  60.  3 ;  —  us  nü  aiAhäi  vXse  jamyät •ämca  x/a^nm/a,.Y.6o.2.  III) 'Recht, reditmässiger  Anspruch  (auf  — )'  und  zu- gleich 'Gegenstand  des  Rechts,  worauf  man Anspruch  ha^  was  einem  gerecht  ist';  spez. von  dem  ftir  die  Zugehörigkeit  zur  sara- l^u/jyischen  Religion  und  das  ihr  ent- sprechende Verhalten  zugesicherte  und  da- durch erworbene  (höchste)  Anrecht,  d.  i.  das auf  das  ewige  Gut  (Paradies)  und  dieses selbst  (S.  auch  vAbleit).  i)im  gAw.:  '/,/m 'dtrndyai  (sd.) . .  räyS  asts  vanfOui  galm (sd.)  manauhs  Y.  43-  •  "'j  —  .y?"»  i^am (sd.)  data  .  ,  ahurö  °sahyä  iizäyäi  (sd.) pmdim  Y.^i.ij;  —  käds..ysi  uxifinn (sd.)  asnqm  a»!iSu^  dar^%rai  (sd.)  frS •iahyä  /rar  iitzY.46.y,  —  ya  ^aohana.. awuntStim  "hmcä  *iaibys  dänAä  (sd.) natda  xsa>r»nca  Aaurvalät3  Y.S4- läis  yüs  g/ae^ORäis  'um  xsmmbyä  dadi^l (sd.)  Y.46.  is'J>;  —  ktßarä  yas5  (sd.) hyin  'liin  Y.  5/.  4.  2)  im  jAwr.:  tßit
6768:raütica  1 .  .  urvaiainarS  . .  tümc'a  ys  zara-  r*"^"t1'  1'  Ta    *'w''/v'"'""'  ^°- '  ^""l!
6863:'rahe    mazda    Yti^.pf.;   —   yazus  .'r5  mazdäY.22.9>;  —  eil  hau  a pu^rö  'rö  (statt  Gen.?)  mazdä  F. 4%;  —  lyJ  . .  /  äat  mraot  (Stverz,,  unter  I  i )  'rd ätars  (Stverz.)  'rahe  mazda  puira  Y.6$}mazdä  "Y.g.^it;    usw.;    ö.  44,  7.78,  Yt 1 2;  7.2 ;  usw.; — ätari  (Stverz.)  mazdä  'rahe]8.5J;  — pfrpsat  (Stvetz.,  unter  i  a),  zara-
7741:•  j.  9r«zvo  Adv."  'wahrlich,  fürwahr'; 1)  an  der  Spitze  des  Satzteils,  vor  Vok.: fr°  asäum  spitama  ^7vam  da^at  ahurB maidä  Yt.  5.  89;  91,  95,  12.3,  13.  i,  Ij. 31.  2)  hinter  dem  Wort,  das  hervor- gehoben werden  soll;  a)  hinter  dem  Pron. pers.:  yat  tum  hs  uzsayatjha  tum  3r° zarahultra  Y.g.13;  —  aez'alia  bä  zara- 'i^ustra  ya>a  tum  jf  vasanhe  V.5. 17; z\;  —  paiti  »lam  if  ptnsat^uha  yim ahursm  mazäam  V. /^.  7,  b)  sonst: mazilt»n  ..vispanqm  tr"  sravaahamYi^N. 4.1;  —  daliiqm  »r'  yaozdaii-Xta  a^a  zX. . asti  yaozdäili^  .  .  havaya  ir'  dasnaya  V. la.  1 9.
10318:•  j.  gäSS-  f.  'Lied'  uzw.  religiösen  Inhalts; 1)  insbes.  von  den  fünf  Hymnen,  bez. Hymnensammtungen,  die  in  Y.  28—34, 43—51,  59  erhalten  sind*':  sraobm  .  .  y5 paoiryd  "^.J  frasrävayatya panca  . .  zara- iu/traAe  *a/smaimvan  (sd.)  vacastastivaf malMzaintls  mal.paiti./rasä  Y.57,8;  7/. 6, G.  7.6;  —  akunavaitlm  (Stverz.)  °'i:qm aiaonlm  .  .  mai.afsmanam  mat.vaüäslallim map.äzaintim  matpjnsvlm  mat.paiti.p?r>s- Vlm  map  varfiibyjca  *pa^?byasca  kufra- mtrttqm  . .  küfrayaslqm  . .  Vr.  14.  o  f.;  usw.; — ahunafalca{^A.)  'Lariam  ^.46;  —  uita- vaitya  (Stverz.)  '"^aya  handatä  ya^amaide . .  haitiPca  afsmans^a  vacasca  vacaslal- llmca  /rasraa'knmca  ..'Vj.iS.y,  usw.;  — sp)ni:1.mainyBm  (Stverz.)  '"^qm  asaonzm  . . Vüiuxsa'irqm  (Stverz.)  '^qm  ..vaAisISistim (Stverz.)  'iqm\x.2.Zl;m-»i.  2)Bezeich- nung  für  alle  (anscheinend)**'  im  Gä^ä- dialekt  verfassten  Stücke  des  Awesta,  d.  s.  — ausser  den  eigentlichen  0<i>äs  —  AtxYHapt. und  die  vier  heiligen  Gebete  (V.  27. 13— 15, 54.  i  )'*'>;  nur  Plur-,  womit  entweder  die Gesammtheit  dieser  Li  tteratur  oder  einzelne Abschnitte  daraus  gemeint  sind  (s.  auch  A): imäsf  tg  haoma  °^ii  imä  h^nti  staomsyS'^. /0. 18;  — farS  amisä  sp>nta  ''ka  gJurvJin Y.2S.0;  —  tipma  vi  0(7  dcflö«/"/ Y.2(V.o, 430,  47-o,5io,S3°''  —  '"i'^byS  spintäbyd ratuxsa^räbyS  (Stverz.)  alaonibyö  Y.55.  i ; usw.;  —  tä  713  hmti  °äi7  har^'iravaitista
10914:•  g.  *xkn3iV'  i)  Adj.  'Genüge  leistend,! zufriedea  stellend',  mit  Akk. :  yS  ,  ,  zara- ' "iiultnm  rääarfhä  . .  'näuiiüS.)  Y.4Ö'.  13;
11194:♦)  Nicht  fünf,  wie  die  übrigen  Länder;  es hat  keinen  besonderen  raiui  däKyumö,  dessen StellDng  Tielmehr  zusammen  mit  der  des  zara- %uJtr3.ümö  in  einer  Person  vereinigt  ist;  zuletzt Marqdakt  EranSahr  uz.
11753:—  tä  xsapanB  yä  *ß'äM  Y.öa.io;  — .  a)  adjektivisch;  a)  im  gAw.:  däidl  .  . ätiti  tä  ^ao^na  .  .  yä  anhus  . .  v»rft- '  tarn  aslm  vaahsus  äyaptä  (sd.)  manatgAs yäii  V.J5. 1;  4.41;  —  yat  ta  sravA  drm-  Y.  25.  7.  B)imjAw.:  *us  ^täai  späna jayqri  yä  pagurva  ,  .  'S,  4,  45;  —  ta  fryi  pat»titi  pasus.haurvqmca  . .  V.  /J.  4a;  43; , .  tä  isuds  .  .  ta  rätayo  *yam  (APn.)  —  pqscaUa  ava  ta  aiü  maya  ..  V.g.ii; oAurS  . .  frävavaca  Y.ö^.g; —  tä  daiA-\^2.  a)  mit  relativischem  Anschluss"; MävS  ..  nijayntnte .  .ydhra  /r<Mir!Hnti  ..^  k)  yai  %Pi}K.:  gavöi  aääisizA.)  iäis  ^ao- /mvafayuYtij.^Si  —  yasf  tarn  dahyüm  .'haiiäis  yäis  vahiitäis  Y.J5.4,  b)  im äcaraiti  yaia  {'wo')  huh3r?ts  *baraite  Yt-ijAiw.:  ttm  ratüm  yaxamaide  yim  zara- 10.112;  —  tä  (statt  NPf.)  daiMävS  ti  "ä-usinm  Y.70.IJ  i';  —  i?m  aküm  paik- ^hamtTT^e  yd^a  duzh?nni5  *baraite  mi~  yäite  yim  aiaoiiqm  V. 18.^6;  76,  5.62; ärff  Yt  10.  48;  41.  b)  substantivisch,  —  upa  tarn  ear?lqm  yqm  datvyqm  Yt  /'/. a)  im  gAw.:  «m  (ASm.)  ..  mimaysff  y!  77;  —  tqm  krhrffm  yqm  iristake  V.$.i; qnm3til(sd.)  mazda  srävl  ahursY.4$.io;  —  täia  vt'hü  yaxamaide  yä  antarpsta  Yt 9;  —  alca  töi  (NPm.)  vaim  hyäma  (Sp.  I3.\^y,~- tä  fravaiay5..aojiita  fuiiti  yä '75  0-)  y^^  ■  ■  ^^fDnaoit  . .  Y.30.  9;  —  paoiryanqm lialsanqm  Yt/J.17,  b)  sub- ai  tSi  at?h>n  saosyaiits  .  .  yH  .  .  htüänti  stantivisch;  A)imgAw.:(i//(i/  msi  daxstfm Y.dS.xi;  —  talcit  . .  ySi  /iisitms  \.  data:  ahyl  ar)ASu£  vTspä  atag^ä  (sd.)  Y. 32. 11;  —  t^ng  tfarayS (sd.)  yöi  vä  daibi-  34.6;  —  tatcä  .  .  'kwaAml  *ä  dqm{sA.) Alt/r  Y.  32.1;  44.11,  13;  —  maf  täis  nipäail:  man5  vofia  urunas^a  ..Y.4g.\o; vispais  yöi  .  .  marintl  Y.43. 14;  —  tal  —  yä  tat  upä.jamyjmä :  tavacä  haxfmä v»myädyäi  kyai  msi  mraota  (sd.)  i-aktstim  ,  asaAyl'ä  Y.  40.  a ; — y.J  tat  upä.jamyämä : 43. 1 1 ;  J/.  5 ;  —  vaida  tat  y''  "Ami  .  .  \  tavatä  sarSm  asafiyä/ä  Y.  4l-  6;  —  ta/a analiS  (sd)  Y.46',2;  —  ta  (APn.)  hwa'  vupä .  .htvaAml ..  xia%r?i  ä  voya'i  ra  (%A.) p^rysä  ..ya  aX  aiil(Sp.  14$  ZD.)  ..Y. 31.  i^l^Y.  34. 10;  —  tat  vJ  nJ  Aasaas Jr^Aj  (sd.)
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
12600:'lehren,  unterweisen',  mit  Akk.  der  Per- son: a^J  a^ä  cSii  (sd.)  aAurö  .  .  zara- 'hustnm  ataxsayaaa^^  (Augm.)*^  vJspa^ farasnt^la  Y.  iz.  5.  a)  mit  Inf.  als  Sach- objekt: kyat  mS  . .  daxsat  usyai  (sd.) *titsna.maiiis  vahistä  Y.  43.  r  5.
13326:•  j.  däityä-  f.  Name  eines  Flusses**  in AiryanaVa^ah  (sd.):  tarn  yazata  ..  zatri.- vairil  *pasne  apö  "yayh  Vt5. 112;  g.f), I/.61; — mmS ape  'yayaYti.21.  a)sonst mit  vatiuhi-:  äpS  vanuAli'  .  .  vaahuyh 'yayä  V.  ig.  2;  —  tarn  yazata  .  .  zara- ^uHrS  airyene  valjaki  vauhuyä  °yays  ". .  in dem  arischen  Vaijah  der  guten  D"  Yt 5.104;  17, /5-«.  V./.z,  2.20'.
14890:yaoiädhd  dakmayStparS  ä/ritstt.,  dairihu. paitlm yaozdd^ö  ustraAe'ti  arsnSV.Q.^T'^; 37  f.*.  a)  bes.  beim  V._>'a«-:  vanani^m .  .  yazamaide  amaheca  °ii  kuiastahe  Yt. Ä  I2J  12',  U- 133-135 '^  JJi;  —  yaf^a- maide  ^a/am  malfi^anahe  (sA)  °//*'  .  . drvaßaoi  Y.  7Ö'.  10;  —  ft«  yazata  . .  zara- %uitrS  v^fhraynaAe  'ti  manahi  Yt/^^aS; 78';  —  yqm  yasata  zard^uilrS  .  .  ava- he^a  'ti  yqnahe  yat  hi  da^a/  .  .  Yt.  16, 6f.  b)  aSahe  paiti  (Sp.  14  m.,  u.)  '(als
17233:•  j.  be  Part  zur  Hervorhebung  des  ersten Worts  im  Satz:  zätS  b'  yS  asava  zara- ^u/irS  V.  ig.  46.
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
17835:•  j.  fra-väka-  n,  i)  'Anrede,  Rede',  im Gegensatz  ZMpäitivaka- :  tPtn  yazata  . .  zara- 5wj?r?  . .  v?r»%ra-]nake  paiti  °ke . .  päifi- väit  Yt  14-  28.  i)  'Ausspruch,  Ver- kündigung;  Offenbarung' i^-fa^MÄ»  „alvahmi paiti  vacö  vTspanam  vohunqm  .  .  'k?m "cui  (est)  .  .  unam  per  vocem  omnium bonorum  .  .  proQuntiatio?"  H.  j.  1";  — mazdä  frsmraot . .  cvas  (sd.)  frsmraoi  'kim Y,  7p.  20'';  —  vTspjm  vacö  'k^m  haurum vacö  ahurahe  mazda  "der  gesammte  Spruch ist  eine  Offenbarung,  der  ganze  Spruch  (eine Offenbarung)  des^^J/."Y.75. 14.  Aa)DS. und  b)  LS.  als  Inf.  'edicere,  proountiare'; a)°iäi:  usi  ahurahe  mazdä yazamaide dar»- &rJi(sd.)  ..xratüm..  marn^räi  ..  hizi'qm.. •käi  mtfhrahf  spmtahe  Yt/.  28;  — yasnahe haptanhätSis  .  ,  yH  fravaoce  .  .  facqmca värfhrtrjninqm  °kaiyi.i$.%.  b)  'kas-ca-. yasnahe  haptanhaisii'  °haila  paitySstayalüa *masdataeca..  Vr.i5. 2.  3)  'Preis,  Ruhm': ahm/li . .  'häi  ula  ^framainyai  (sd.)  Yl  16. 3,
17882:m\Xä  i)dnwS.  la:  ä  dim  pimat  zara- %uärs:  kö  .J  Y.p.ijNik./.  i)Med. dnwS.  7:  kP  vS  asa  a^raiVj  "wer  wird  sich von  A.  beraten  lassen?"  ¥.57,11.
18245:•  j.  frä  V9r9ndyü  Inf.  'das  Glaubens- gelübde  abzulegen',  mit  Dat  'zu  Gunsten von  — ':  frä  gave  v*  tnatdayasna  zara- %uftray&  "zu  Gunsten  des  Rinds  wollen wir  das  Glaubensgelübde  ablegen  als  . ."
18905:•  j.,  g.  näiri-  f.  'Frau',  bes.  die  verheiratete, als  Mitglied  der  Familie, 'Ehefrau',  im  Gegen- satz za^nar-  und/»&ra-:  huxsa%Tas{^A^tü «7  nä  vä  °rf  vü  xsailä  Y.  41.  2;  35. 6;  —  na  va  'ri  va  Yl  ii.  4;  —  narasca *'rlsca''>  (NP.)  Vytjo;  —  3  airySmä (sd.)  .  .  janta  mDhyascä  'ribyasca  zara- %ustrahl  Y.  54.  i;  FrW.  /.  i;  —  vTspa- nam  naram  'rinamca  taoxma  Y .2. 2"];  30, &12,  iz,^-SS.i2,yfä.2;  —  frinyä  'ryi usimtnanhö  "der  Fr.,  der  Frau  des  U'' Yt. /J.  140;  140*;  —  aat  niqm  tarn  fsaona- yeke  (sd.)  'rya  va  pu%Tahe  va  haoya  vä mariiiyi  (sd.)  Y.  //.  i ;  N.  54.  a)  mit asavan-  (Sp.  250  m.):  naram  'rinam  ., a/atmam  asaonitiqm  Y.  26.  7;  8,  10,  Vr. rö'.a,  Yt.y,i43— 145*;  —  asäunqm  fravasls narqmCä  'rinqmiä  '^.g-j.y,  $g.2,  [V. 5.37:  lies  hqm.ttairmqm?\
19716:■  i)  'deoken,  meinen,  sich  vorstellen';  oft im  Gegensatz  zu  sprechen  {'vak-,  mrav-) und  handeln  {'vam-):  Y.  ^5.  3,  35.  3, 39-  4;  '3-  4.  70.  4,  Yt.  IQ.  106,  13.  88,  P.  18, 25,  Aog.  25,  Gkiö^;  a)  mit  wie?-Adverb: *yai  niJij  yava  mihS  mamne  .  .  vavala  . , vavanza  P.  i8\  —  s.  noch  c  a.  b)  das Gedachte  erscheint  im  Akk.i  y^s  tu  T *aAuramazda  mSngAäizSYffA.)^'^  vag^ascä däs^a  varti^ä  yä  voha  Y._jp.  4;  —  zara- %uitrai  .  .  paoiryäi  vohu  mamnanäi  .  . vaokule  .  .  vav7rpzuie  YL 13.  88;  —  tat  ai vainmaidl .  .  hyat  t  maininiaai(i¥OM.yä vaocSimä^a  v>Tvzimäca  yä  . .  /yac'hananqm vahii'iä  ..  Y,j5. 3j  —  ySi  Tm  vS  tOil ßsä  mqhr?m  vansMtT  (sd.)  ya^ä  im m»3j(i*SKM,)<?S  vaoU^aY.45-Z^''\  —  '^i masyS  .  .  aojs  manyete  äusmahm  yaka mi%rasaii  .  .  manyäe  humatim  .  .  mraoiti hBxhfn  .,  vintyeiii  hvarst?m  Vt/o,  106; —  äai..manya{i.^k^  mananka  humatsm Aog.  25*';  —  amit.maiti  *humata  mamne *anm.uxti  hoxta  {vava^a)^'*  anm.variti kvansta  {^avama)^  "mit  rechtem  Denken hat  ei  gut  gedachtes  gedacht,  mit  rechtem Sprechen  gut  gesprochenes  (gesprochen),
20809:51.16;  —  J3  dfhfnaots  mastm  itijyJtSif (sd.)  . ,  hyal  vh  ^aoiatum .  ,yä  (Sp,  1115 m.)  fraHnas  Y.^2. 5.  b)  im  jA'vr.;  das Relativ  ist  substantivisch:  t>m  yätum  ..yS .  .Jraviit3(sd.)  Y.ÖÄ21; — ttm  a<n..yS r  <Ä»fl  Y.Ö5.8;8,  YtJ?.  142,^.1*.  6;  — ta&t  ysi  . .  nasks/rasatths  ank>tae  Y.p.  1 aa;  S.g.\,^.4g,  \k.i4.  46',  ig.  19;  —  us taat  tpäna  patmti  . .  ta^t  yä  (als  NPm.) ^«iKK'«ft'.,V,jj.4j;43; — ta^itutjasmti  ya (als  NFm.)  m^rmfynica  iaraoiryt$yai{sA.)ca V,  z,  14  GL;  —  tasat  yä  kaininS  anhaire (sd.)  . .  ayrvH  Y.  5-  23 ;  —  upa  tarn  vanqm aätiyqm  hS  )n>rrfS{%A.;  näml.  'upajyäya) V. 5.  z;  —  tat  draom  .  .  yat  ml  äa^al a^ff  Y.J/.5;  55.30,  Yti-S,  ip-Sä',  V. 2.6  PüZ.(?);  —  /«/  ayaphm  yasf{h%\C) hwä  y3samaAi  yt  10.3s;  —  •-  li  a/a- ydnti  yq  *aoe  paskät  vyeinti  Y.57.  29;  — ti  naru'.  .  yöi  (als  APm.)  haeahi  Yt  ly. 7;  Vr.  2.3;  —  lä  xsapans  yä  *jvahi  Y. 6^2.10; — ta  fyao%tui..ya  atihus ..  v)rysyeiti V./5.  i;  V.4.4S  (vi; —  tinars  ..yahva (statt  maslc)  vfr>hra.btt<^S  Yt.  y.  1 46; — die Beziehung  ist  ungenau :  ta  fry S ..ta  ihtds t&  rätayS  *yqm  (APn.)'**  ahur^  .  .  zara- 'iuiirai  fravavala  Y.6'5.  9;  —  im  Sinn von  quantus{Sp.  I202  m.):  ih  rurpfsqstäts yä  Al  ux^qstatS  \l.j.2.  1)  'ay-,  nur a)  im  gAw,;  zu  i):  ya%ä  ta  tmSnghäca . .  ys  (NPn.)  voAb  Y.  _j'/.  4.  zu  3) : iyat  T maim'maäi^ä ..y3(SPa.)  Ä3tqm  ^ao- %aHanqm  vahUt3  hysl  Y.^.  3.  m)  day (Sp.  686  m.);  nur  b)  im  jAw.:  ma  dim p)r3s3  yim  ptrtsahi  H.2. 17;  —  nSttdim .  ,  ava.airiaoiti  .  .  yahmäi  .  .  mihrS  ja- laiti  avaijiAe  \t.jQ.  24.  2)  ohne  de-
20831:—  rasistqm  astim  .  .  yqm  yazata  zara- %ustrS  Yt  /tf .  S  f. ;  2 ;  ��  avaiAAäi  pairikayäi . .  y3  (s,  I)  duzy3irya  yqm  ..  huyäiryqm nqma  aojaite  Yt Ä 5 5 ;  —  aridvXm ..'*yim '*' aswits  mazdayasna  hist>nta  Ytf.  97f.;  — ISm.,  n.:  vanm  .  .  yä  mg  aoxta  ahurS V.2.31;  —  DSm,,  n,:  tislrim  ..yahmäi hazaar)m  yaoxstinqm  Jräda'^iat  ahurS  Yt 8. 4S;  —  mi'krsm  . .  yahmäi  maglian»m
21197:—  ttaota(sd.)ca  .  .y  aisa  ahurahe  Vr,  g.  6j  1 6f.';  —  s.  noch  Anhang.  d)  DSm.,  n.: ra%we  .  .  y  ahurai  mazdät  .  .  y  zara- %ulfräi  Vr.  12.1;  —  Primat  y  pouru.- baoxinahe  (statt  DaL)  Y,^.  37; —  huxla- hrSJfmai  ..hya^  mazdäi  ahuräi  Y.jj.  5, A.J.  6  {vioy);  —  kvävSya  y  sadhreY.^g. 30;  V.  jp.  47,VyL_jj';  —  maZsahe ..y  vars- fiSi/yU7.s6.  e)AblSm.,n.:  asätiStverz.) haca  y  vahiUät  Y.ip.  iiusw.; —  drvatat y  anrät  mainyaot  YL  /_J.  7 1 ;  —  %'wai  y eara'husträt  ^.2.3.  f)  GSra.,  ^.:  asoAe y  vahiitaÄeY.i.to;G.2.y,'Vtlj.9i,92;  — amp^ahe  hü y  aurvat.aspahe  Yt  10.  13;  67, J2.38,  S.J.  18;  —  k>r)säspahe y  *£ae%äus', gahavarahe  Yt.  /j.  6 1 ;  — ■  anhus  yS  mana (Stverz.)^"  ahurahe'?.43;\x%'v.\  —  manay zara%uUr3i  (statt  Gen.)  V.  2.  i ;  —  tava y  ahurahe  mazdä  V,  4.  3;  —  myaxdahe aoäiti  (sd.)  .  .  y  maiaySizanmayehe  A. J.7;  8— 12*,  7.  o):  aheca  kar^anS y i^anira%aht  Vr.  /o.  i;  —  aiMe  .  .  y° yasnaheca  vahmahtca  Y.  /.  2 1 ;  —  aRahe nars  .  .  y  irisfs.kasahe  V.  ^,  15;    18.  39;
21424:—  yS  yazaile  hvan  Yt.  6.  4;  4^;  —  yaslä va  mas' (sd.)  yazaiU  Y.j2. 3;  —  yS  Axi aha  frayazäite  yäha  hli . .  yazata , .  zara- %ultrS  YtJ^.  41;  —  ga^asca  srävayd apasca  vanuhTl  yazpmnS  H.2. 13;  — yS . .  nsit  g3%i  srävayäli  nStJ  apS .  .yaxaiti V.  18.^;  —  fUrim  ya-ialta  bansma  st)rf- naSa  V.  12.2;  —  k3  mqm  yazdtte  kö  druiäl Yt  jo.  108;  —  kd  mqm  stavat  kd  yazäite Yt.5. 8;  /J.  50;  —  at  vä  yazäi  stavas mazdä . .  hadä  (sd.)  a/j  Y.  ^o.  4;  —  ya^, va  yazpmnascä  urväidyM  (sd.)  stavas ayenj paitl  Y.34.6;  —  yy  .  ■  srulgaosS. t>mS  asti  yesimnü  (Pass.)  "der  am  besten hört,  wenn  man  zu  ihm  betet"  Yt.  ig.  5: tat  vS  nS  hazaolänhs  (sd.)  . .  daidyäi  savö ahm  vohu  mananha  ux}>3  (sd.)  ySis Srmaitis  yazpmnätfhS  mmaahä  mazdil raf^nm  cag)ds  ".  .  mit  denen  (vereint) Asa,  VM.,  Arm.,  M.,  wenn  demütig  ver- ehrt, ..  ihre  Stütze  leihen"  Y.5/.  20;  — ahurahl    mazda   yasnüi   .  .  y!    »ä    isiö
21440:yas3  ('wie  sva.  womit')  hwä  yazata vTstäsps  Yt77.  61;  61,  5.90,  91,  /5- 54, V.  75.  17,  Vyt.20,  3/;  — ka%a  zaota  xsäta apB ..yazäile  Y.ö^.g;  —  tim  yazät surunvata  yasna  sraol»m  . .  zaokrabyB  (DP. statt  IP.)  Y.57.  3;  Yt.>  18,  70.  31 ;  —  yö aHm  yjzäite  zaohräbyB  Yt/7.  2;  2,  8.\, 10.6,  Y.68.10;  —  yatal^a  mqm  zara- ^uära  ..  zaokrräbyS  Yt  /.  9 ;  mangelhaft  zitirt F.4g; — hvanx^aitim ..yazamaide  haomays gava  barismana  .  ,  zaohrabyasca  arsux- öaäbyasca  vayzibyS  (DP.  statt  IP.)  Ny.  7. 1 6 ; —  yazayania  %wqm  mazdayasna  pasubya staoraHbya  vayalibya  pataraialibya  (sd.)  Yt 10. 1  \(j;—ultaiaiiya  (LS.  statt \%.)ca  vTspnn asavamm  .  .yazamaide  Vr.  18, 2.  b)  Akk.; tarn  yazata  kaolyaahü . .  sat)m  aspanqm  . . hazaisr)m  gavqm  "ihr  opferte  ff. . .  hundert Rosse, .."  Yt. 5.  21;  p.  ag;  —  tarn  yaztnta .  .  hunavB  .  .  sat>m  aspanqm  Yt  5.  57; 72.  c)  paiti  mit  Gen.(?);  yqm  yazata zara'huitrS  humatahe  paiti  mananhS  Yt 16.  6.  2)  mit  Angabe  des  wozu?  durch
21962:—  apascä  Vä  asTsca  vä  mäfora/^a  vä  .  . avaecämä  Y.3S.5;  3.  Anhang,  vä, dem  ein  Vok.  folgt,  ist  dem  Akk.  eines (mit  /ä  angeschlossenen)  Subst  koordinirt (Sp.  565  u.,  571  m.,  u.);  zu  i):  anai/  vä nsii  ahurS  mazds  asfmca  yänäiS'  zara- mz^na  (sd.)  Y.2Ä9;  —  frB  v&  Jraisya mazdä  ahmca  mri!üe'(£d.)  Y.  4S-  6j  — yj  vä  aiä  u/yänf  manasca  vohä  Y.  2Ä 3.  n)  g.  »JGen.-Dat;  zu  i)l  Aaäat.- aspä  (sd.)  vaxfya  vS  spitamänAs  Y.  46. 15;  F.adj  —  data  vs  . .  draenS  Y.33. 8; —  a/ä  vJ  anyS  ainim  vivftighatü  (sd.) Y.  53-  S;  32.  2;  —  haää  (sd.)  vSstäO  .  . jwflc/J  Y.46.IJ;  —  a  v>  ^gSula  hsm- yantü  Y.^i.  3;  —  avä  vJ  vanuhXs  rätsis daiTgBMtau! {sA.)  Y.3S.5;  —  oäa  w? Uta  Äyaniä  .  .  räitr  (sd.)  Y.40.4;  —  ai vS  yaojä  ..  aurvatH   Y.jo.  7;  11,  53.  T,
22101:•  g.  vaepya-  Adj.  'der  sich  zur  Päderastie gebrauchen  lässt,  pathicus':  nsit  ta  Jm xlnäui  'yS  hvTnS  psrHS  (sd.)  ssmS  zara- %ustr>m  spitamsm  hyai . .  väzä  (sd.)  "nicht hat  ihn  zufrieden  gestellt  der  Buhllcnecht des  Kavay  an  der  Pforte  des  Winters, den  ZSp.,  indem  er  . ."  Y.  57. 12.
```


## [2026-09-05T20:57:50.897Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor n in (166,167,168):\n    print('==== leaf',n)\n    print(t[n][:3000])\nEOF"
}
```


### [2026-09-05T20:57:52.652Z] TOOL RESULT

```
leaves 412
==== leaf 166
— 145 —
phlv. aj war, vergl. nniS': 11 TN in (Is. 1, 7).
LW. kurd. zhrl 'Heftigkeit, heftig' : af/. zahar ober-
halb* ; bei. zahr mächtig (293).
652. »erftn *Wunde, Schlag*.
aw. vergl. za/ya- *zu Tod gehetzt' (y. 53, 8,
Geldner, KZ. 28, 193, 202), zahJt (y. 60, 7); ai. [/jas-,
jasyata 'erschöpft, todmüde sein, Caus. ^erschöpfen ;
verletzen, tödten, schlagen (Dhätup.)*; phlv. za/^m
bezw. zahm.
Wenn die Zusammenstellung richtig ist, so müsste
np. zextn für *zehm stehen.
LW. kurd. afy. za^m; bei. zahm, zäm 'Schwort,
Säber (296).
653. zeden schlagen*, Praes. zen-em.
Kä8. Q. fiden , bäjin , bemjida bü ; K. jindemün , Z.
bezint.
ap. [^jan',ajunam'töAien; aw. [/'Jan-, Jainti; phlv.
zatan^ zanet, zatär, zan(i)sn; ai. [/han-, Aawfi 'schlagen,
tödten'; arm. vergl. gan 'Schläge, Züchtigung, yunem
'schlagen, prügeln' (H. No. 63).
kurd. zenin 'schlagen (Feuer), schicssen'; af/.
va]zan-am; bei. janag, n. janay (175), LW. zaday,
n. zaday (294); si/n. zln-am, sar. zan-am, vi^zm-am,
654. {\)zer 'Gold', zetln (zerrm); zernl (LW. arab. zarnlq,
zarmxj syr. talm. yy)*) 'Arsenik'; zerJr, zifir 'gelbes
Färbholz, Gelbsucht' i).
ap. vergl. da(jHx6g {?)^); aw. zairi-, vergl. zaramja-
'Gold'; phlv. zar, zartn; ai. hdri-, hiranya-,
kurd. LW. zer, zir; afy. LW. zar; oss. d. suy]zärin(i,
t. sizyänn 'Gold, golden (234); bei. LW. zar (302).
*) Natürlich nicht aus aw. Zairivairi-, phlv. Zariver (?) (Hörn,
Mitth. aus d. er. Samml. d. K. Mus., Heft lY, S. 25), wie der Eigenname
Zerer (yergl. Nöldeke, Pers. Studien II, 2, Anra.).
') Trotz der Schwierigkeit, die Form mit ap. diivar- zu vereinigen,
erklärt G. Hoffmann, Zeitschr. f. Assyr. II, 49 folg. (JapHxds als
^königl. persische Hof- und Reichsmunze im Gegensatz zur ausser-
persischen Währung'.
Hörn, Grtindriss d. neup. Etymologie. 10
==== leaf 167
.._ 146 —
655. {2).'^er 'Greis, Greisin'.
aw. vergl. Zarad'lustra" ; ai. jdrant-; arm. cev
'Greis' (H. No. 135). Vergl. np. ^ol (No. 648).
oss. t. zärond alt' (129).
656. zerd gelb', vergl. zerd[ab^ zerde 'Galle'.
aw. zairita- 'gelb' ^) ; plilv. zart, zartth, syr. LW.
plDI; ai. hdrita-.
kurd. LW. zercl ; af/. ziyar; bei. LW. ;earf/ (303);
wa/. LW. 2;arrf, si;'n. ^f/Y?, sar. ^-^Vd.
657. ^nrd, zurt 'Art Hirse' (arab. LW. öurat)),
g. jurda 'Getreide'.
phlv. jtirtäk bezw. zurtäk 'Getreide'; bei. (LW.?)
zurf 'jowar'.
Die Vereinigung mit arm. gari (H. No. 65), lat.
hordeiim, gr. y.qiS?], ahd. gersta ist schwierig, zuletzt
V. Bradke, Methode S. 189 folg.
658. ziirfln, zirfm, zufrln 'Thürring (zum Schliessenj,
Kiegel*.
aw. zarant/ö,]zafrqm (yt. 10, 129) 'mit goldenem
Halse (Pfeile)', Geldner, KZ. 25, 530, Note 209.
Ganz unsicher.
659. xervän, zerban, zermän 'Zeit; Greis' •'•).
aw. zatirvan- (Bartholomae, BB. XVH, 132, Note 1)
'Alter'; phlv. zruvän (Genmie, Hörn, Mitteilungen,
Heft IV, 26), zarmän, zarmänih (P. Vend.), arm. LW.
zrvan — vergl. ZovQovdii Photius, Bibl. § 81, Zerovamis,
Berosus — ; ai. jarimdn- 'Alter'.
Ist etwa auch zemän (aus *<^ermöw), zemäne^ persisch
und nicht arabisch, wie man gewöhnlich annimmt?
660. ^irih 'Panzer.
aw. zraöa- 'Panzer'; phlv. zrai (päz. zareh) bezw.
zrad (aram. LW. n^T, arab. zarad, zarad[xäne).
*) Nöldeke, Pers. Studien, I, 38 üimmt eine Form ohne ;*, also
*zarta-, als Grundform für np. zerd an.
2) FR führt dieselben beiden Verse wie HQ an (Wiener Jahr-
bücher, Band 40, 176).
*) Später ist der zoroaatrische Zevfän zu dem Patriarchen
Abraham ^owonlon.
==== leaf 168
— 147 —
LW. kurd. zirt, zir/ * Panzer ; af;'. zira; bei. zirili
(306); arm. zrah.
Urverwandt mit afy. zyara * Kettenpanzer', oss. zyär
Tanzer (132) ?
%l, liieryiin gelbfarbig.
aw. zairi.gaona- gelbfarbig'; phlv. vergl. zarlnqün
(vd. 2 (67)).
Vergl. np. öün aus *cigün (No. 450) und aöenjiin,
G62. »ist 'schlecht, schimpflich*, zistür.
Kää. Z. jist (auch s. v. bed).
aw. jlstayamna- (y. 8, 3) Verachtend, vorspottend'
(Geldner, 3 Yasht, 128ji); phlv. zist 'hässlich' (Men.).
af/. LW. zl/t; sar. ir^ Verdorben, schlecht, hässlich'.
663. zefer, zefr *Mund' (8ähn. I, 195, 1189).
aw. zafar- 'Rachen ; phlv. znfar,
Muss dialektisch sein, da die reguläre Form np.
dehan (No. 589) ist.
664. i^elTi, zalü 'Blutegel', zerü (AM. 180 Zeile 2 v. u.).
skr. LW. (?) Jalüka-, jaluka-, Jalikä- 'Blutegel*
(Bütticher, Arica 67).
kurd. zdü, zuliil, zalüg, zürT; af/. LW. zallü 'Blut-
egel', echt zavara\ bei. zaray (417).
Gegen Curtius' Zusammenstellung mit lat. hirüdö,
air. gil vergl. Hübsch mann, ZDMG. 38, 424.
665. zelle^ ziUe 'Grille, Heimchen'.
skr. jhillikCL', jhillU Grille, Heimchen' (Hübsch-
mann, ZDMG. 38, 424).
666. xeni 'Kälte', zemistan 'Winter.
aw. zyao- 'Winter', Gen. ziniö; phlv. zam 'Winter'
(vd. 2 (20)), zam(i)stan; ai. himä- 'Winter ; arm. vergl.
jiun 'Schnee', jmern 'Winter', jmerem 'überwintern
(H. No. 178).
oss. d. zumägy t. zimag 'Winter' (135); af/. zimai;
wa;^. zam, zamin (Adj.), sar. zainän, zamämn (Adj.),
si/n. zimjy zinj 'Schnee'.
) vt. 19, 42 ]int die neuo AuRfj^abe harözuiiem.
10*
```


## [2026-09-05T20:59:32.823Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ghel-2\\|ghel-1\" POK_full.txt | head\necho ---\nawk 'NR>=32660 && NR<=32760' POK_full.txt"
}
```


### [2026-09-05T20:59:34.590Z] TOOL RESULT

```
20282:From Root / lemma: ghel-1 (and ghel-1), also as /-, u-or /7-stenn; ghela- : ghle- ghlo- : 
20320:From Root / lemma: ghel-1 (and ghel-1), also as /-, ^-or /7-stem; ghela- : ghle-, ghlo- : 
20345:From Root / lemma: ghel-1 (and ghel-1), also as /-, ^-or /7-stem; ghela- : ghle-, ghlo- : 
36328:From Root / lemma: ghel-1 (and ghel-1), also as /-, u-or /7-stem; ghela- : ghle-, ghlo- : 
36633:Root / lemma: ghel-2 
---

ze/&zc» 'iron'; 

Lithuanian ge/ez/'san6 zem. ^e/z/5 (therefrom gelezinis, gelzinis^ iron'), Latvian dzeizs. 
East Latvian dzelezs. Old Prussian gelsot 'iron'; 



Whether in connection with gr. xc(Ak6(;, Cretan Kauxot; " copper, bronze '? That k from 
XQAkoc; standing comparison not in the way, because Kouxoq in *xaAx6(; points as common 
primary grade. The word probably derives from a a foreign cultural circle; also the unique 
gradation of the 2nd syllable in Balto Slavic would be based on different substitution in the 
in the borrowed; xciAk6(; (£pu9p6(; llias I 365) as ' red metal ' perhaps to xaAKP), xaAxn. 
KaAxn ' murex, snail emitting purple dye ', which is likewise borrowed; in Balto Slavic the 
name would be figuratively transferred from bronze to the iron. 

References: WP. I 629, Specht Dekl. 27, Trautmann 83. 
Page(s): 435 

Root / lemma: gheled- 
Meaning: ice 

Material: Npers. zala{*zalda) "hail, hoarfrost'; 

gr. hom. xaAa^a 'hail'; 

Old Church Slavic z/e d/ca Irozen rain', sloven. z/ed^g\azed frost, ice', kir. ozeleda^ rain 
with snow, ice on trees ', poln. ziodz^ sleet, smooth ice '. 

References: WP. I 629 f., Specht Dekl. 17. 
Page(s): 435 

Root / lemma: ghelgh- 

Meaning: gland 

Note: 

Root/ lemma: gheigh-: "gland' derived from an extended Root/ lemma: gel-1\ "to curl; 

round, *gland, growth, ball'. 

Material: Armenian geij-kh " glands ' (the obvious aniaut can be explained through 

dissimilation, s. Meillet MSL. 13, 244f., Liden Arm. Stud. 71 under A. 1. 2); 

East Lithuanian gelezuones, gelezaunes, gelezunes " glands, craw '; 

Slavic *zelza\v\ Church Slavic zleza, russ. zeleza, sloven, zleza, acech. zleza, 
nowadays zlaza^ gland ' (about Czech hlfza^ abscess ' s. Meillet aaO.), poln. zo/zads. 

References: WP. I 612, 632, Trautmann 84. 
Page(s): 435 



Root / lemma: ghel-ond- ghol-ijd- 

Meaning: stomach; bowels 

Note: (A supposition about the old paradigm by Petersson Heteroklisie 228'') 

Material: Gr. xoAa5£(;f. PI. ' intestines, entrails, Gedarm', x6AiK£(;ds.; 

Maybe abbreviated alb. zorra " intestine, entrail ' common alb. gh- > d-, z-\ l/rs. 

Old Church Slavic *zelgd'bk-b " stomach ', russ. -Church Slavic zeludtk-b, Serbo-Croatian 
zeludac, Czech zaiudek, poln. zo/^o'e/rds. 

References: WP. I 631 f., Trautmann 82. 
Page(s): 435 

Root / lemma: ghel-ou-, ghelu- 

Meaning: tortoise 

Material: Gr. x^Kxic, 'turtle, tortoise. Lyre', xsAcbvp ds., Aeolic xsAuvva, x£A£U(; KiGapa Hes. 

(Kuiper Notes 48); 

Slavic zelu-i. 'turtle, tortoise' in: 

Church Slavic zeli^vb, russ. -Church Slavic zelva, Serbo-Croatian zelva, Czech zelva, 
russ. zolvbi., poln. zd/tv. 

References: WP. I 631, Trautmann 84, Specht Indo Germanic Dekl. 120. 
Page(s): 435 

Root/ lemma: p'^eA/i? (Germanic) and p'^eZ-d'^d (Slavic) 
Meaning: to cost, pay 

Material: Gothic fra-gildan^ repay, compensate ', us-gildan^ repay'. Old Icelandic gjalda^ 
defray, pay, repay, be worth ', Old English gieldan. Old High German geltan ' defray, 
repay, serve, sacrifice' (proto Germanic *je/dd), Old Swedish gja//a ds. {*je//=>d); Gothic 
g/7dn. 'tax, interest'. Old Icelandic 5/5/0'' payment, earnings, punishment'. Old English 
gield^ payment, tribute, tax, sacrifice, oblation, brotherhood ', Old Icelandic ^/M' 
membership ', Old English glide v\. ds., glldam. ' Gildenbruder ' (out of it Middle Irish gllda 
' squire '), Middle Low German glide, out of it Modern High German Glide; Old High 
German gelt^ payment, repayment, sacrifice, oblation etc.'. Modern High German Geld, 
QoVc\\c gllstru. 'tax'. Old High German gelstar{*geld-tra-) 'sacrifice, oblation, tax'; from 
ndd. gellen =gelfen derWes Lithuanian gelluotrbe valid';
```


## [2026-09-05T20:59:39.373Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 429\\|Page(s): 429-\\|429-434\" POK_full.txt | head\necho \"=== find ghel- 'to shine' lemma\"\ngrep -n \"gold, gleam\\|Meaning: to shine\\|golden, gleaming\\|shining metal\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:59:39.481Z] TOOL RESULT

```
36631:Page(s): 429-434 
=== find ghel- 'to shine' lemma
8302:Meaning: to shine; gold, dawn, aurora etc. 
10694:Meaning: to shine 
11312:Meaning: to shine (?) 
11433:Meaning: to shine 
12602:Meaning: to shine; white, *ash wood, ashen, birch tree, elm 
12668:Meaning: to shine 
14348:Meaning: to shine 
14423:Meaning: to shine 
14565:Meaning: to shine 
14607:Meaning: to shine 
14651:Meaning: to shine 
27795:Meaning: to shine; to praise 
36278:Meaning: to shine; green, gold, blue, yellow, moon 
36839:Meaning: to shine, shimmer 
38225:Meaning: to shine; star 
38251:Meaning: to shine, shimmer 
49283:Meaning: to shine, to flaunt 
50810:Meaning: to shine, glow 
50946:Meaning: to shine, bright 
79933:Meaning: to shine, shimmer
```


## [2026-09-05T20:59:43.270Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36270,36300p' POK_full.txt\necho \"..... searching zairi/zaranya/Galle within ghel entry (lines 36278-36640)\"\nawk 'NR>=36278 && NR<=36640' POK_full.txt | grep -n -i \"zairi\\|zaranya\\|zara\\|Galle\\|bile\\|gall\\|Avestan\\|Persian\" | head -40"
}
```


### [2026-09-05T20:59:45.329Z] TOOL RESULT

```
References: WP. 1 546 ff., WH. I 106, 645 f., Trautmann 367, Specht KZ. 53, 307 f. 
Page(s): 425-426 

Root / lemma: ghe/-1 {and ghe/-7), also as A, u-or /7-stem; ghela-: ghle-, ghlo-. ghla- 

{*ghwet-) 

Meaning: to shine; green, gold, blue, yellow, moon 

Note: 

Root / lemma: ghe/-1 {and ghe/-7), also as /-, u- or /7-stem; ghela- : ghle-, ghlo- : ghle- : to 

shine; green, gold, blue, *sun; derived from Root/ lemma: gel-, gela-, gle-, (also *gelel-.) 

g(e)lal-\ light, to shine; to be joyful. 

Material: In view of the frequent cases, where Indo Germanic palatals in Balto-Slavic are 

represented by velar, instead of through a concurrence of gel-, ghel- and ghel- agreeable 

with Persson (Beitr. 790) and Kretschmer (Gl. 21 , 115) the Balto-Slavic *gel- is defined 

through borrowing from a Centum language (Venetic-lllyrian?). 

Note: 

The enxtended root {*ghwel-)-nta, -na, -/aformants follow the model of lllyrian - Anatolian 

attribute nouns, adjectives, (see alb. numbers). 
..... searching zairi/zaranya/Galle within ghel entry (lines 36278-36640)
33:the normal development in Latin helvus^ honey-yellow, golden ' {*gheluos) = gallo- Latin 
34:g/7vus'\\g\r\t yellow' (with dial, /from gall. *gelvos)\ 
43:Avestan zari- 'yellow, yellowish, golden ', zaMa- "yellow, paled-yellow ', zaranya-. Old 
44:pers. daraniya-u. 'gold', zaranaena Irom gold, golden', zara- m. 'gall' (= gr. xoAn), named 
46:with velar root aniaut gsrado-karata-^ cutting out the gall '? (see Bartholomae Altiran. Wb. 
67:gr. xbkoQ, 'gall, rage, fury', xoAr) 'gall, rage, fury', xoA-£pa ' stomach disease ', xAwpoq ' 
70:Latin fel, fellis{*fel-n-is) n. 'gall' (older /7-stem as Old High German galla), /probably 
78:Latin fel, fellis {*fe/-n-/s) n. 'gall' derived from root *del because of common Latin d- > f-. 
95:Old Icelandic gallu. 'gall, poison ' ( *galldn-, Indo Germanic *ghol-n-). Old English gealla 
96:m.. Old Saxon galla, intense f.. Old High German galla, weakf. 'gall'; 
123:Trautmann Bsl. Wb. 364 f., 368, 372; Lithuanian /^/z/s"gall', through Metath. from *zu/t/s, 
141:Old Church Slavic z/bcb "gall' (*ghl-ki-s)\ Bulgarian z/bJAa "chicory' (zin folk etymology 
154:in addition Old Church Slavic zIbtb, zibcb "gall', russ. zolcb, Bulgarian zlbcka6s. and 
191:(verbal noun dfglaimm), bret. dilenn^ choose, select, pick ', gallorom. glennare^ Ahren 
257:Irish ^/ass "green, gray, blue', cymr. ^/a5"blue', bret. ^/az"green', gall, glastumn. 1. " 
259:plain -s- gallorom. *glasina^ blueberry ' (M.-L. 3779a); to Irish glasssKxW Old Irish glaisst 
308:Gall. gITso-margai. " bright marl ', gallorom. *glTso-, older *ig/e5C»-(lndo Germanic *ghlei-
```


## [2026-09-05T20:59:51.340Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=36315 && NR<=36335' POK_full.txt"
}
```


### [2026-09-05T20:59:53.307Z] TOOL RESULT

```
Note: 

Common Old Indie : Latin gh-> h-. 

Avestan zari- 'yellow, yellowish, golden ', zaMa- "yellow, paled-yellow ', zaranya-. Old 
pers. daraniya-u. 'gold', zaranaena Irom gold, golden', zara- m. 'gall' (= gr. xoAn), named 
after the color as gr. xoAoc;, Latin fe/, [common Latin ghw- > ph- > A], Old Norse ga// ust; 
with velar root aniaut gsrado-karata-^ cutting out the gall '? (see Bartholomae Altiran. Wb. 
523 with Lithuanian); 

Note: 

From Root / lemma: ghel-1 (and ghel-1), also as /-, u-or /7-stem; ghela- : ghle-, ghlo- : 
ghla-\ 'to shine; green, gold, blue, *sun' derived Root/ lemma: d^e/-/, d^o/o-: 'curve; 
hollow'. Root/ lemma: 6^61-2: 'light, shining'. Root/ lemma: 6}^el-3\ 'to tremble' [common 
alb.-lllyrian gh- > o'-]. 

thrak. ^n^Ta 'gold' (?), Phrygian ^sAkiq Aaxava Hes.; Phrygian YAoup6(; xpua6(; and 
yAoupsa xpuoea Hes. (borrowed from gr. xAu)p6(;??);
```


## [2026-09-05T20:59:53.754Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT daraniya\"; grep -n \"daraniya\" KNT.txt | head -20\necho \"=== PHD zišt/zard/zar\"; grep -n \"^zi[sš]t\\|zišt\\|zard \\|^zarr\\|zarnīg\\|zarnīk\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-05T20:59:53.817Z] TOOL RESULT

```
=== KNT daraniya
591:daraniya-, Av. zaranya-, Skt. Мтатуа-.
940:П. When у (of either origin) is expected to stand before a vowel, it must be either as con- sonant т, or as the reduced vowel + consonant т. The latter combination? appears in OP as -ar-: pIE *óhwl-enzo-, OP daraniya- ‘gold’, Skt. híranya-. pIE "e-kerWjonie, OP akariya"tà, cf. Skt. ákri-
1176:pIE *ghal- in OP daraniya- ‘gold’, Av. zaranya-, Skt. htranya-, c. Eng. gold.
2047:Nt. Nom. Sg. zsacam, dusiyaram, ardatam, darant- yam, aruvastam, dàtam, Sakatam, kartam, visam, kamnam; aec. xsagam, stánam, daraniyam, aru- vastam, kartam, visam, uvdipasiyam, uvaspam, probably casam.
4259:35 :abariya : utà : hacd : Karmànà : daraniyam : hacd
5522:daraniya- sb. ‘gold’: Av. zaranya- Ars. Phl.. zarén, NPers. zárr, Skt. htranya-m, pIE *ghj-enio- ($82, $66.П, $88, §126, §144.IV), cf. NEng. gold. See also dáranzyakara-. — daraniyam nsn. DSf 35. darantyam asn. DSf 49f. But Gk. $арекб, a Persian gold coin, is from the name of Darius (Bv. BSLP 30.1.59), and not from a short form of darantya- (as taken by Mt. Gr. $129, Hz. ApI 134-5).
5523:déraniyakara- sb. ‘goldsmith’: NPers. zärgär ‘goldsmith’; daraniya- with vriddhi, + kara- ‘maker’ ($126, §143.V, $160.18; König, Burgbau 65; Hz. AMI 3.73-4; Kent, ЈАО 53.21). dàrami- уакатӣ npm. DSf 49 (on Frag. Theta, Scheil 21, plate 11, see 544; Konig, Burgbau, Tafel 5; Kent, JAOS 53.21, against 51.195-6).
=== PHD zišt/zard/zar
PHD.txt:59:The orthographic principles followed, in seemingly haphazard permutation, in the writing of Pahlavi, besides the ideographic, include the phonetic (within the limits of the alphabet), the his- torical, the pseudo-historical, and. others so indeterminable as scarcely to merit the name. The establishment of the original spelling of a word, therefore, very seldom reveals its pronuncia- tion. To determine this it is necessary to examine all the available comparative evidence.
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:2223:hateful gizistag, zišt.
PHD.txt:2651:lizard karbaS, karbunag.
PHD.txt:5074:zāy-! zāyišnīgi zāyišnī! zādan! 1-2zrëh zarrën | zargónih - zargon zarigomand zarig zarr(i)gar kàr-! kistárt kištant zalüg zraw- zarwan zruftan zarmānīh zarmān zardālūg zardīh zard Zardu(x)št
PHD_mackenzie.txt:5482:wizard - wars                     93                              xan
PHD_mackenzie.txt:5772:zard [zit' I N -] yellow.
PHD_mackenzie.txt:5788:zarr [ZHBA < A zbb); DHBA < A dJ]h' I M zr-, N ......] gold•
PHD_mackenzie.txt:7013:lizard karbas, karbunag.                 maid kanig, kanizag, paristar.
PHD_mackenzie.txt:11077:zarr1                                        bijagan
PHD_mackenzie.txt:11079:zarren1                                      bazagih
```


## [2026-09-05T21:00:06.537Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    if 'daraniya- sb.' in p:\n        print('leaf',i)\n        print(p[:1200])\nEOF"
}
```


### [2026-09-05T21:00:08.362Z] TOOL RESULT

```
leaves 232
leaf 212
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis; XPb 3, 4, 5, 6; ХРе 2 bis, 3 bis; XPd 2, 3, 4 bis; XPf 2, 3 bis, 4; XPh 2 bis, 3 bis; XE 3f, 5, 5f, 6; XV 3, 4 bis, 5; A!P2 2°, 3°, 4°, 4f°; А?Не 2, 3, 4 bis; A?Pa 2, 3, 4 bis.
daiy, see -di-.
dawa- sb. (false) divinity, demon’ (cf. Hz. RHRel. 43:.32-7; AMY 8:74-5, ApI 126-30): Av.
^
-
УА $ " Aic hts КҮЧ - EUR EE EE ГЕНЕ ЗЕ, m aad ACCENT add Va, rA a Ra SENS un at Mom o "heat aai Тэ мә GIO Ate a ec ala ie
Rec tae ais 5g AAA, лса mia (n n m VRAT, ЁК te o rre ns"
- eS i.i Nai ie "e Loren чйр ло
LEXICON
daéva-, Skt. devd- ‘deity’, Lt. divos, deus, pIE *deiyo- (876.1IT, $114, 5148.11). See also data- dána-. ата npm. XPh 36, 38, 39.
dat»adàna- sb. ‘sanctuary of false divinities’ (8147.1, $160.Ib): daiwa- + dána- (in derogatory sense, ‘den’, ace. to Hz. AMI 8.75, ApI 181). dawadénam asm. XPh 37f (written -d'av*m? in second copy, cf. $51, Lg. 13.293).
daug- vb., see hadugà-.
dauStar- sb. ‘fri
```


## [2026-09-05T21:00:08.884Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,p in enumerate(t):\n    if re.search(r'zoizdiSta|zoizdižta|zaesa-|zoisnu', p):\n        print('---- leaf',i)\n        # print small window around\n        for m in re.finditer(r'zoizdiSta|zaesa-|zoisnu', p):\n            print(p[max(0,m.start()-600):m.start()+600])\n            print('~~~~')\nEOF"
}
```


### [2026-09-05T21:00:11.449Z] TOOL RESULT

```
leaves 1041
---- leaf 921
Et.  und  Bed.7  Wohl  Komp.  mit  oder  Ableit aus  z>iid-.  —  ')  Oder  Stamm  'at-7    S.  No.  a.
—  >)  Oder  GS.  lu  'm-?;  S  3S6-  —  J>  So  nach der  unlergeschri ebenen  /'Jsini/Iesung  in  K. Der  Pahlaviteit  hat  zrdli,  worin  man  da* letzte  Zeichen  fälschlich  für  'und'  genommen hat.
■  j.  z«r98ö.k3r9ta-  Adj.  'das  Herz  heraus- schneidend': taica  narS  g?r^SJifntäs- (sd.)rtr  '/Jj(NPm.)A  V.7.24.
Komp.  mit  CS.  loa  1.  Glied.  —  Pü. :  dil  hrrf-
«iinömand.
•  j.  zöiinav-,  g.  zöiS«nav-  Adj.  (fem. "«£-)   'zusammenschreckend,    schaudernd,
dby  Google
i693
zoizdiSta-
zi  2  A
1694
bebend',  vor  Frost:  avi  lanuye  'nuye(,DS{.) V,7.  70;  —  mit  Gen.  (Abi.)  der  Ursache: aodinscä  "»S  (NDm.)  r/Jss{sd.)  Y.jr.  12.
Za  ioiia-.  —  Pü.:  ialäifn,  ialaiäien,    (lu  V.)
erl.!  «man. ■  j.  zöizdiäta-  Adj.  'der  schau derhaßeste, abscheulichste',  von  den  xrafslra-:  ajaitala 'laca  .  .  xrafslra  Yt. 21.  \\  —  ya\ia  -fäis xrafstrsis  V.  7.  a.
Snperl.     lu     einem    V.    *sSiU5-    'schaudern
machen',  vgl.  zöilnav-  and  vasdä- :  xtasdüla;
—  Pü. :  *baiaklum,  erl. :  rtmatilum.
•  ].,  g.  z^O«-  n.  'Geburt,  Entstehung;
~~~~
```


## [2026-09-05T21:00:22.292Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[212]\ni=p.find('daraniya- sb.')\nprint(p[max(0,i-3000):i+1500])\nEOF"
}
```


### [2026-09-05T21:00:24.117Z] TOOL RESULT

```
XPh 2 bis, 3 bis; XE 3f, 5, 5f, 6; XV 3, 4 bis, 5; A!P2 2°, 3°, 4°, 4f°; А?Не 2, 3, 4 bis; A?Pa 2, 3, 4 bis.
daiy, see -di-.
dawa- sb. (false) divinity, demon’ (cf. Hz. RHRel. 43:.32-7; AMY 8:74-5, ApI 126-30): Av.
^
-
УА $ " Aic hts КҮЧ - EUR EE EE ГЕНЕ ЗЕ, m aad ACCENT add Va, rA a Ra SENS un at Mom o "heat aai Тэ мә GIO Ate a ec ala ie
Rec tae ais 5g AAA, лса mia (n n m VRAT, ЁК te o rre ns"
- eS i.i Nai ie "e Loren чйр ло
LEXICON
daéva-, Skt. devd- ‘deity’, Lt. divos, deus, pIE *deiyo- (876.1IT, $114, 5148.11). See also data- dána-. ата npm. XPh 36, 38, 39.
dat»adàna- sb. ‘sanctuary of false divinities’ (8147.1, $160.Ib): daiwa- + dána- (in derogatory sense, ‘den’, ace. to Hz. AMI 8.75, ApI 181). dawadénam asm. XPh 37f (written -d'av*m? in second copy, cf. $51, Lg. 13.293).
daug- vb., see hadugà-.
dauStar- sb. ‘friend’: NPers. dost, Skt. jostdr- ‘loving’; agent-noun ($154.IT) to root daus-, Av. zaos- ‘enjoy’, Skt. jus-, Lt. gustat ‘tastes’, NEng. choose, pIE *ĝeus- (S88). daustà nsm. (§124.5, 6186.1) DB 4.56, 69, 74; DNb 7,8, 12; DS} 4.
dacara-, see tacara-.
dáta- sb. ‘law’: Av. dáta-, NPers. dat; nt. ptc. to *dd- (8122, §242.1I). See also Vahyazdata-. dātam nsn. DNa 21; DSe 20°, 37; XPh 18f. dala isn. (less probably absn., §172) DB 1.23; XPh 49, 52. [d]ātā npn. DNb 58.
datasa, KT's reading, with first and third characters uncertain, DB 4.71f; read шаш, q.v.
Détuvahya- sb. (§164.V) ‘Datuvahya’, father of Megabyzus ($168.10): Elam. da-ad-du-man-za, АКК. 2a--tu--a; cf. Iz. AMI 1.84n. Dät[u]- vahyahyü gsm. DB 4.85.
Dàdar&- sb. 'Dadarsh?', (1) an Armenian, (2) а Persian, satrap in Bactria: Elam. da-tur-%-18, Akk. da-da-ar-5u. Репу. of darš- ‘dare’, with re- duplication; Skt. dadhyst- ‘bold’ ($30, §76.III, $152.1, §164.1V). Раат пет. DB 2.29, 31f, 48; 3.18, 15. Dédarsim asm. DB 2.33, 38, 44.
idan- vb. ‘flow’: Skt. dhdn-vati. датира] DZe 9 (or danu[taiy] mid., Wb. KIA 104, after al- ternative suggestion of Bthl. AiW 683); $216, §216.n1.
*dan- vb. ‘be acquainted with’, see z$nà-.
dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
ldar- vb. ‘hold; (intrans.) dwell’: Av. dar-, Skt. dhr-, Lt. fir-mus ‘firm’, Lith. daryti ‘to make’, pIE *dher- ($76.11, $122). See also Upadarma-, Dérayavau-, duruva-, Vidarna-. Present stem dàraya- and conj. 58215. dárayümiy Ist sg. (226.1) AmH 5f; AsH 11, 14; DB 1.26; DPh 4f;
189
DNb 14; DH 4. dárayatty DNd 2 (reading cer- tain, acc. to Wb.’s marginal note to AbkSGW 29.- 142). dàáraya"liy 3d pl. (82321) XPh 23f, 24f. adāraya imf. ($2281) DB 1.85;2.9,3.23; DNa 41; DSe 20Ї°; XPh 19; adáraiya DNa 22 ($48; Wb. AbkSGW 29.33, cf. Kent, JAOS 35.947n; wrongly Hz. ApI 132, as passive). adaá[rayat]à imf. mid. with passive meaning DB 4.90f ($235.II; JAOS 62.268). adaršiy Ist sg. aor. mid. (8218 T, 8233. V) DPe 8. adáüriya imf. pass. ($220, $228JT) DB 2.15, 90.
ham- + dar- ‘get hold of, obtain’: hamadárayaiy Ist sg. imf. (5233. TIT) DB 1.26.
*dar- vb. ‘be angry’, see daríana-.
daraniya- sb. ‘gold’: Av. zaranya- Ars. Phl.. zarén, NPers. zárr, Skt. htranya-m, pIE *ghj-enio- ($82, $66.П, $88, §126, §144.IV), cf. NEng. gold. See also dáranzyakara-. — daraniyam nsn. DSf 35. darantyam asn. DSf 49f. But Gk. $арекб, a Persian gold coin, is from the name of Darius (Bv. BSLP 30.1.59), and not from a short form of darantya- (as taken by Mt. Gr. $129, Hz. ApI 134-5).
déraniyakara- sb. ‘goldsmith’: NPers. zärgär ‘goldsmith’; daraniya- with vriddhi, + kara- ‘maker’ ($126, §143.V, $160.18; König, Burgbau 65; Hz. AMI 3.73-4; Kent, ЈАО 53.21). dàrami- уакатӣ npm. DSf 49 (on Frag. Theta, Scheil 21, plate 11, see 544; Konig, Burgbau, Tafel 5; Kent, JAOS 53.21, against 51.19
```


## [2026-09-05T21:00:32.297Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'schauderhaft', r'zairi-', r'zaranya-', r\"'Galle'\"]:\n    print('==========',pat)\n    for m in list(re.finditer(pat,t))[:6]:\n        print(t[max(0,m.start()-500):m.start()+400].replace('\\n',' '))\n        print('~~~~')\nEOF"
}
```


### [2026-09-05T21:00:34.157Z] TOOL RESULT

```
========== schauderhaft
tk,  ctL:   ünSi  ^apel  'er  schläft  wach'. •  g.  'zaeman-  n.  'Regsamkeit,  Munter-, Wachsein' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5. Zum  ai.  V.  MnlH  'incitat'.  —  Vgl.  *tainak; 'toimaii',  viaSäla-,  —  ai.  aiu-htaian-  Adj.  — Pü.:  imävxnälh,    eri.;  luxlSkih,    Sn.:  jägara- •  j,  'zaeman-  Adj.  'regsam,  wach*:  •matiB F.  4  f. Vgl.  ^xarmart:  —  Pü. ;  ttttävanä. g.  oMiinä  Y.  4/.  4:  s.  6ia-. •  j.  zaeäa-  Adj.  'schauderhaft':  •/ff  F.  20. S.  auch  sminav;  sSiidiila:  —  Vfil.  mp.  (Pü.), np.  ujV«)  'schauderhaft',  got.  ingtiman  'er- *ebrecken';  IJtt.i  IF.  2.4,%,  GGA.  tSg6.  961, Hbm.  PSI.  70.  —  0  Das  freilich  auch  dem ai.  hffii-  entsprechen  könnte ;  vgl.  unter  zat- Sayamna: •  ].,  g.  zaotar- ;  zaoSr-  m. 'Priester,  Ober- pricster';  y7  (näml.  zara'husirö)  *fä  a/ä tnzü/
~~~~
in' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5. Zum  ai.  V.  MnlH  'incitat'.  —  Vgl.  *tainak; 'toimaii',  viaSäla-,  —  ai.  aiu-htaian-  Adj.  — Pü.:  imävxnälh,    eri.;  luxlSkih,    Sn.:  jägara- •  j,  'zaeman-  Adj.  'regsam,  wach*:  •matiB F.  4  f. Vgl.  ^xarmart:  —  Pü. ;  ttttävanä. g.  oMiinä  Y.  4/.  4:  s.  6ia-. •  j.  zaeäa-  Adj.  'schauderhaft':  •/ff  F.  20. S.  auch  sminav;  sSiidiila:  —  Vfil.  mp.  (Pü.), np.  ujV«)  'schauderhaft',  got.  ingtiman  'er- *ebrecken';  IJtt.i  IF.  2.4,%,  GGA.  tSg6.  961, Hbm.  PSI.  70.  —  0  Das  freilich  auch  dem ai.  hffii-  entsprechen  könnte ;  vgl.  unter  zat- Sayamna: •  ].,  g.  zaotar- ;  zaoSr-  m. 'Priester,  Ober- pricster';  y7  (näml.  zara'husirö)  *fä  a/ä tnzü/  .  .  kaya  (Sp.  46a  m.)  S.. 33.it;  be- nutzt Yt.  4.T.  yi  °ta  sarähustrS.  A)  im jAw.
~~~~
========== zairi-
aX.  Aärita-  Adj.;  np.  vgl,  lard,  woiu  S  202 No.  —  Vgl.  'zairita-  EN.  —  Pü.r  zart,  SQ.; bkilah,  pS/alai. •  j.  zairita-  in.  EN.  eines  Gläubigen: datahahe  'Iahe  Yt  13.  98. Vgl.  'sairita-.  —  Eig.  'der  gelbüehe';  Kurt- name? —  ai.  harita-  m.  EN. •  j.  zairi.döiSra-"  Adj.  'mit  gelben,  gold- farbenen Augen':    haomü  frasmü'  .  .  'rS Y.57. 19. Pü.:  :arren  äiiir,  erL;  kus  (aim  latanak  [sva lar,  V.  3.  26;    Npü.!  Töin).    —    ■)  NA.  ima •  j.  zairi-päSna-  Adj.  'mit  gelber,  gold- farbener Ferse  (?):  gattdarswan  (sd.)  yim 'n>m  YL5.  38,  75.41- •  j.  zairina-  Adj,  (fem.  '«ä-)  'aufreibend, erschlaffend',  von  der  BsHyastä  (sd.): bU^yasia  yä  'na  V.U.  9;  —  ÖBsyashm 'mm  Yt  18.  2.^ Zum  ai.  V.  jiryaü,  jiiyati  'er  wird  gebrech- lich', yara/i  'er  macht  gebrechlich'.  S.  noch azarima;  azanianl-,  zaunira-,  '
~~~~
========== zaranya-
i  zavavaf  hyatiia  mazäyascil voku"-  Vyt  ?o  '*. Pü.:/fl  ;^äiiiht.  —  0  Wo.  will  avaval;  vgl. noch  Sp.  1 164  No.  3. j.  ia-^a>->/a:  s.  nnler  :ävat: •  g.  zavah-  n.  'Kraft,  Stärke':  äaiva  . . spSniStä  mainya  maida  vanhuyü  'vS  iida (Sp.  3210.)  Y..??.ia. VgL  zävar;  —  Pü. :  vahumaii  gri/lär  haue  pa an  dahiin^  Sü. :  gvahman&sya  grahiläro  AAtwä' maii;  vgl.  zu  laalar-  No.  8. •  j.,  g.  zar-  V.  'erzürnen',  Praea.  10  b sarariu-^\  11  b  zaran-",  13  zaranya-^'', 30  (Iter.)  zäraya-;  Perf.  i  zazar-'K  — PPfP.  tar^ia-, 1)  Akt  'erzürnen':  anäisvä  nöii  ahurä inazda  asimcä yän3ii zaratialntäi^  manascä kyal  vahistim  "um  dieser  Gunstbeweise willen    möchten    wir  euch,    o  AhM,  und 1670 A.  und  VM.,  nicht  erzürnen"  Y.  2Ä9;  — drva    zaritS   YtiJ.  5.  2)    Med.   'sich erzürnen,  zornig,  ergrimmt  werden':  drvi zantS 
~~~~
m  .  .  asüts .  .  aslffis  .  .  matdä  .  .  tarcßsuHrahe  . , ' °mahe  baiiata  kacimnanqm  Vr.p.  i;  — ithursis  dähyumahe  ShurSÜ  'mähe  Vr.  /.  9 ; — frädat.vupqmAujyätle  'mäila  aiaone  , . räiiwe  Y, /.  6;  — ftSdat.vTspam.hujylitJm 'rmmca  ..  Y.2.  6;  G.^.  6,  9*. *)  Die     ■  '        - anderseits NeubildDiig  auf  Gmnd  der  fem.  Formen,  ähn- lich wie  Ist.  suäves  geg.  ai.  ivädäva^i  vgl. unter  hama.nS/ama: ■  j.  zaranumant*  Adj.: mant-. s.  unter  targnu- •  j.  zaranya-  n.  'Gold':  carimh  (sd.)  . . bräziHta  .  .  }r3zai>m  'nim  Yt  5,  129;  17. 14,  Aog.  Ä^;  —  hakml  ^nzahm  hakmt 'nim;  ..  Ivat  yavai  'nim?  ..yaha  ultrahe .  .  arins  pmska  (sd.)  V.  z^,  11;  —    srvama ""^^"■f■'■''■''?^■''g*'?';f"-'>^''■''■;aB^«)    saßfthS  'ya  faiti.%warstä»la  Y. jiivrisruirtma  m  Beiiehnng   ge- ;        •  ■%_  _  r       ■* bracht  wird. Abiei
~~~~
gt  satrin  älat 'das  goldene  Gerät'  -  so  Tür  z*  s'  -  anf  den ^tx^Saugand  {^.  siu>k>Hla-)\  danach  dachte  man sich  :*  s'  als  eine  bis  zum  Fuss  des  Bergs hinabreichende  Irichterartige  ÖHhung,  durch  die das  Wasser  auf  dem  Erdboden  zum  Himmel sieigl  {pa  an  türäx  ab  t  iah  i  arniln  bat  äsrnän iälä  lavaJ). Vgl.  tarirtumalll:  —  Kpü.  (lu  A):    satrm ;  s. noch  No.  a.    —     ')  So  Vyt   —    »)  Werüos; Pü.:  wie  lu  Ai.  4  (s.  zetSna.). •  j.  *zaranya-'>  Adj.  'golden':  arfdvf  . . 'nya  ao'hra  (sd.)  *f>3iti.smaxta  Yt.5. 78; —  vatnm  .  .  zarSt/  (sd.)  ayan?td  fra- hixfym  .  .  *'n}-ehe  Yt.  10.  13z;  96,  I Ablcit.  aus  'zarina-;  vgl.  zar^naina-,  —  i)  So. Fl  m  Yt.5.  78.  10.   132. •  j.  *zannaya-'',  zarjmaya-  m.  'Früh-' ling':  misti  urvaranam  xatri^aonanam °malm  paiti  ztm^a  *uzuxsyänti  Yt.7.4. KoinpE.; 
~~~~
========== 'Galle'
 und   (ebensowenig)   die  Männer, ' die  die  Galle  und  die  das  Herz  (aus  dem' Jir/cJ/Csd.)  "ä^«  Y.5/.17;  —  ai*hudäi. Hunde-  oder  Menschenleichnam)  heraus-  iVa/w  (sd.)  'dJ  (LS.)  Ryim  Y.50. 9. schneiden,  und  (ebensowenig)  die  Männer, '     Zum  v.  ,i,™vfl^-i   %  S3}-    Kig. 'Antreten'.  — (die  ihnen)  die  Augäpfel  aus  der  Augen- 1     ^"-  (''K"-)'  .?"■■".  X''fl"'- höhle  herausreissen"  V./.isf.".  E-  S"-nm-%  lies,^«*™-. Vgl.  lat.  fei,  ßilis,  k<!.  iiüü  'Galle'.  —  Pü. : .  •  j.  gouru.zaoSra-  Adj.  (mask.  °ra-)  'des Hak  tirrcnihiSniouii ,  dam  als  Weihgüsse  schwer,  zähflüssig  Sind"':  ^»«•n'J "■■''*■"""'  t  Yt./o.ri3. Ansicht  ^/ura/s :  gtii/ak  sä»  ap2  ii Hohle  ist  in  zerstören".  S.  dazu  such  Sd. //.  2.  —  ')  Ich  kann  die  hergebrachte,  an Pu.  sich  an  sc  hl  i  einsende  Fassung  der  Stelle (DsT.  ZA.  2.  100; 
~~~~
g.  22. Vgl.  tavoA:  —  np,  vgl.  zör  (woiu  Hbm.  PSt. 273)-  —  P5-:  SÄ-«.  Sü.  :fräimii\  mit  der  Erl.: iti  pädayofi.  —  <)  Das  erste  a  nach  %  2g4.  3. —  1)  Die  selbe  Verbindung  auch  im  Mp., iB.  Bd.  7.  g;  ei  u  tlr.  —  3)  Vgl.  Sü.  und unter  aojah-.  —  *)  Wofür  auch  fälschlich z  n  a  r  (sÄÄr),  ebenso  wie  umgekehrt  i  n  r  (zSr) für  iohSjö-  vorkommt;  s.  DsT,  ZA.  /.  Lxxvi No.  3.     Vgl.  No.  5-    ~    5)  Wie  für  taArS-, •  j.  zära-  m.  'Galle':  'ras(HS.ya  F.^g. Vgl.  gr.  x»^»,-,  Bthl,  ZDMG.  j;.  155;  s.  noch No.  i.  —  Pü.:  zahrat.  —  ")  Oder  ist  das Wort  als  zSt's  a  lu  denken  und  j  lu  S  J04 n.  2  lu  stellen?  Der  idg.  NS.  *iA^/d  wUre wie  gr.  i.f^  gebildet  (BB.  //.  119,  125)  und verhielte  sich  zu  *j;jr^/-  (Sp.  523  o,)  wie  gr. afp  zu  lat.  i^rd-i  zur  Anlautsdilferenz  s.  Ugv. Grd
~~~~
```


## [2026-09-05T21:00:55.838Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[165][:3000])\nEOF"
}
```


## [2026-09-05T21:00:57.114Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD zyrn / zyst\"; grep -n \"zyrn\\|žyšt\\|zySt\\|zyst\" SOD.txt | head -20\necho \"=== SOD_pages hits\"; grep -n \"zyrn\" SOD_pages.txt | head"
}
```


### [2026-09-05T21:00:57.567Z] TOOL RESULT

```
— 144 —
bei. LW. zal 'Frau', spec. 'Ehefrau, Gattin (419);
af/. zör; yidg. zör 'alter Mann, Greis.
Hier stehen r und / im Neupersischen neben einander
(vergl. zer, No. 655). Nach den persischen Wörter-
büchern ist dieser Fall sehr häufig, doch läuft hier
viel Dialektisches mit unter. Meine Sammlungen über
den Gegenstand sind noch nicht abgeschlossen, so dass
ich über die Stellung des Neupersischen zu Brug-
mann's Erwartung (Grundriss I, 210, 211) noch kein
Urteil habe gewinnen können. Doch glaube ich nicht
an wichtige, positive Ergebnisse.
G48*^'« i^änü 'Knie .
aw. zänti' 'Knie' in zänu,[dräjao , vergl. frasnu-
(skr. prajUn-) ^) ; phlv. zünük, jfänäk (letzteres entweder
dialektisch oder auch zänük zu lesen); 2l\, jdnu- 'Knick-
arm, cunr 'Knie* (H. No. 138).
kurd. zCLna; af/. zangün^ cangün; bei. zän (421);
wa;^. zatij sar. zm^ sangl. zong.
649. t^äiv 'Spalt, Riss'.
Zu [/"gap" {Jap-) 'klaifen, tief sein , vergl. aw. Ja/ra-
jqfnH' (Nöldeke, mündliche Mitteihmg).
i)i}0, ^ehän, zuhän (AM.) 'Zunge*, zefan-),
g. izvFin (Käs. Q. ilzün ist natürlich arab. lisän).
ap. izavani'^) 'die Zunge*; aw. hizü'\ phlv. nzvän
bezw. huzDän, ziivän bezw. zavän ; ai. jikvä-,
kurd. azmän 'Zunge'; af/. ziha\ oss. t. äuzdg (4);
hol. LW. ztivan^ n. zavan (311); siyn. zev, sar. ziv,
wa/. zik.
Über die indogerm. Grundform hat zuletzt Johans-
son Indog. Forsch. II, 1 folg. gehandelt.
051. lieber 'über, darüber, auf, zewer, vergl. zehet'dest 'die
Oberhand besitzend'.
') Über znii' wird hoffentlich die neue Ausgabe Klarheit bringen.
2j z/f/. X^'ärezm. Fol. 656 r (Berliner Handschrift); jedenfalls
dialektisch, vielleicht ;^^'ärezmisch.
'j Vordflchti<»o Form; Bartholoniao, BB. XIV, 245 vermutet
hiznrani.
```


### [2026-09-05T21:00:57.626Z] TOOL RESULT

```
=== SOD zyrn / zyst
6116:/zirn/         zyrn  gold  Av.  zaranya- 
6185:/zirn/  zyrn  gold  Av.  zaranya- 
22956:^'nzyynt-,  'nzyst- 
27771:3070  *bz-  =»  bzyst 
27962:3105  bzyst   C  (U)^ 
31827:MDii  P120,  mzySts  "fifteenth  day";  Hen. 
38290:zist   ©<*zoisdista;  *zais—y  Parth.  zys-   =>zyst-, 
38314:zyst- 
38321:zistauc   (jystwc)  ^zyst'wc 
75401:wafc   ©f.  pp.  ^zyrnwfc,  wftyy,  wpt}k 
79723:10590  wzysth   M  f  j>^*<>* 
79724:wizest  ?   ©<Parth.  wzyst 
79728:Hen.  BBB  p  138,  wzystyh 
85683:11430  zst»   B=»  zyst- 
86450:zi/en   ©<zyrn   ©ob.  -y  =»zyrn 
86534:zyrn 
86609:11566  zyrn  ybtjj 
86621:zyrn'y 
86632:11567  zyrn'y  =*  zyrnyn'k 
86634:11568  zyrn'yn'y    B,  S  «4  zyrnyn*k 
=== SOD_pages hits
3249:  /zirn/      zyrn         gold          Av. zaranya-                 /zirn/           zyrn       gold              Av. zaranya-
32485:       GMS 857                                                                wafc ©f. pp. ^zyrnwfc, wftyy, wpt}k
37304:      zipate ©pp.                                                    zi/en ©<zyrn ©ob. -y =»zyrn
37306:¥                                                                                                                             zyrn
37366:          TSP 2.1065                                                 11566 zyrn                                            ybtjj
37376:zyrn'y
37380:11567 zyrn'y =* zyrnyn'k                                                 zi/ert(a) (*zyyrth) ©<Av. zardta ^zyrtk1
37382:11568 zyrn'yn'y       B, S «4 zyrnyn*k                                   GMS 985n 1; VJ 50, 79, 122; Benv. JA 1951,
37383:11569 zyrnp'm B                                   ^^^jj                     122
37389:11570 zyrnywn         B                        yjC^ *o£ jj
```


## [2026-09-05T21:01:05.236Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nraw=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nfor i,p in enumerate(pages):\n    if 'zyrn' in p and '11566' in p:\n        print('LEAF',i,'-> printed approx',i-66)\n        print(p[:60])\n    if 'zoisdista' in p or 'zoisdiSta' in p:\n        print('ZIST LEAF',i,'-> printed approx',i-66)\n        j=p.find('zoisdista')\n        print(p[max(0,j-800):j+500])\nEOF"
}
```


### [2026-09-05T21:01:07.243Z] TOOL RESULT

```
ZIST LEAF 249 -> printed approx 183
eleventh month of the year
4599 jwk M                              c-o^fJU                   GMS 1275; Hen. JRAS 1945, 149.12, 151.9
     zGk ©<*druka <*druvaka =»n}jwq, Sr'wk^,
                                                             4612 jyryft M                                    Jm'O:
       zwq, zwk()), 6rwk
     sound, complete                                              zirift ©<Parth.
     BBB 516 f23; GMS 285, 978                                    wisdom
                                                                  W-Lii: Gropp. p39
4600 jwky> M                                    ^<^^
     zukya ^Srwky*                                           4613 jyst M                                 ^lo>;<c^j
     health, greeting                                             zist ©<*zoisdista; *zais—y Parth. zys-      =>zyst-,

LEAF 538 -> printed approx 472
    471
¥
```


## [2026-09-05T21:01:13.245Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nfor i in (538,539):\n    print('======== LEAF',i)\n    print(pages[i][:3500])\nEOF"
}
```


### [2026-09-05T21:01:15.195Z] TOOL RESULT

```
======== LEAF 538
    471
¥                                                                                                                             zyrn
                                                                     11554 zynyw8 S                      Jj**jij ls^ ct^^t "-> ->
                                                                           zen-yoS
            gold102R18, 51R17, 69V14, 18; ob. zyny, C2,
           C2,
                                                                            harness
             51R19; BSTii 885.17, 19, 829.18, 847.48             x
                                                                            MDii p37, Nov. 1R5, 8, 12
    11545 zyn-1 M, S                            o>J^jy> «jx\z~*                                                          oJLJ^p <aJJj
          zin ©<Av. zind; OP dina-        ©pp. zyt-                  11555 zynt'k B
          GcOtake away, (to)remove                                         zi/ende
                                                                           ferocious
           GMS 579; Hen. BSOAS 11.68.9; TSP. 1727,
                                                                            SCE 232 n p38; BBB n512; zyndg, BBB
             zynty ?; MDii B-17R 14
                                                                     11556 zynt'k pyfih B                                   J^j
    11546 zyn-' S                                        j&-\j             zinde-pl6
          zan ? ©3sg. pres. zyrint =*zyt-3, zn-2                           angry elephant
          (ro)play
                                                                           TSP 6.8, 11.17, 18, Benv. nyzt'k
           KG 577; S W, IIJ 1978, 259 apud. Sund. KG
                                                                     11557 zyny     B =» zyn>y
           » pl93
                                                                     11558 zyny C                                   ojcj^tl^
    11547 zyn- B                                   ? o^y.j^^               zayne =»n}zyny
                                                                           speaking
          (to)be known ?
           TSP 17.27 n p231, zynty                                         ace. -/iw, C2, 51R20

    11548 zyn'kh    B                                       o±       11559 zyny Yw*ry B               £± jU^ < Jy~J*± j
                                                                           zene-xware ©Parth. zyrfyy xw*rg
           zinak
           body    ^zn'kh1, znw                                            truce breaker
                                                                           Benv. TSP 2.161-2, 2 n pl70; Hen. Texts. 716              .
           STii 7.21, 35; Benv. Notules. JA 1939, 275-6
                                                                     11560 zyny(h) »» zyn»y
    11549 zyn'y B                      G^-jJcjW^^
          zene (zynyy, zyny(h)) ©<Av. zaenah;                        11561 zynyy M =* zyn*y
                                                                     11562 zyr M                                      ^j.Ub
             zaeahvant\ Parth.z>7i(yy
§          deposit, trust, care                                            zir
                                                                           wise ©pL -r; ob. pi. -ty =*z*yrk
           TSP 1223, 25 n p324; VJ 1205, 1210n p98; BBB                      zyrtyy
                               
======== LEAF 539
                                                                                                                         472

zyrn'y

            5.9; Sund. AoFviii 1981, 25R5                          11581 zyrth     B                                Jj^Xb*

11567 zyrn'y =* zyrnyn'k                                                 zi/ert(a) (*zyyrth) ©<Av. zardta ^zyrtk1
                                                                         old, old woman
11568 zyrn'yn'y       B, S «4 zyrnyn*k                                   GMS 985n 1; VJ 50, 79, 122; Benv. JA 1951,
11569 zyrnp'm B                                   ^^^jj                     122
      zirn-fam
                                                                  11582 zyrtk1 M                                          ^
         gold-coloured                                                  old man, old
         BSTBL, Dhy. 216
                                                                         GMS 984, 988
11570 zyrnywn         B                        yjC^ *o£ jj
      zirn-yon                                                    11583 zyrtk2 -* zyrt'k
         gold-coloured                                            11584 zyrtr'p'k B                            J*jl*&jjJ*s
         BSTBL, Dhy. 140 & etc.                                         zirt-rafe

11571 zyrnywnc        B                       LsC&><oJfjj                TSP  2.34
                                                                         jaundice
      zirn-yonc       ©f. adj.
         gold-coloured                                            11585 zyrtyh       M =» zyrt}k         jai o\j>_3 'cP^oOiJ
         BSTBL, Dhy. 146 & etc. pl49                              11586 zyrys-       M

11572 zyrnkryy        M                                 J*jj             zires ©impf. ^zrys-1
      zirn-kare                                                          (roMestroy, OcObe destroyed
                                                                         GMS 627; TSP 2, 745, zyr'ysty
         gold-smith
         GMS 1122
                                                                  11587 zyst S=> zyst-
11573 zyrnp8>k B                                                  11588 zyst- B
      zirn-pa5e (zyrnp8}y)                                              zist ©-w, -> -*zyst-t jyst
      golden-legged, with golden leg                    iji->->
                                                                         ugly, 55,
                                                                         SCE    hateful
                                                                                   301
         VJ 324, 319; -P6>kw, VJ 797, 861, 864
11574 zyrnp8*y =* zyrnpS'k                                        11589 zyst- C                               jy^ccJ^j
11575 zyrnwfc C                                                         zist (zyst-) ©<*zais; Avzdisnu; zoizdista;
                                                  l£JJ *^*iJJ
      zirn-wafc                                                            Parth. zys- =»zyst-, jyst, zyst}y
         gold-woven                                                     ugly, hateful, hated
         STii 5.26                                                      GMS 451; BBB p77.633; Hen. Tales. 481.50; C2,
                                                                           gloss, f. zyst\ C2, 61R24; zysty, STi 45.8, 71.1
11576 zyrnyn'k B
```


## [2026-09-05T21:01:26.600Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nfor i in range(474,481):\n    head=pages[i][:300].replace('\\n',' ')\n    print(i, head[:200])\nEOF"
}
```


### [2026-09-05T21:01:28.391Z] TOOL RESULT

```
474                                                                                                                          wmstyy                                                                         
475                                                                                                                        408  wn-          spoiled                                                   10086
476 409           Gersh. Minorsky. Mem. p279; w7r, W-Li 85,                         winaxs ? (wxsn-) ©3sg. pres. wnxsytty            wp*rs         94                                                       
477                                                                                                                    410    wpVk            SCE 64; BSTBL, Dhu. 115, 236; TSP 5.1; C2,             6R12, 7
478     411                                                                    rosy                                                                                                                       wr
479                                                                                                                    412  wsn           quietness                                                   C2, 54
480            413                                                                                                                                 wrmzt              10183 wrtncyk S       *j*^ (<t ^jt^'^I
```


## [2026-09-05T21:01:28.905Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la BQT_v2_pages.txt 2>/dev/null; python3 - <<'EOF'\nimport re,io\np=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\ntags=re.findall(r'\\[pdf page (\\d+)\\]',p)\nprint('ntags',len(tags), tags[:5], tags[-5:])\n# find printed page numbers 1012 / 1021\nfor n in ('1012','1021'):\n    idx=[m.start() for m in re.finditer(r'\\b'+n+r'\\b',p)]\n    print(n, len(idx))\nEOF"
}
```


### [2026-09-05T21:01:30.877Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
ntags 0 [] []
1012 1
1021 0
```


## [2026-09-05T21:01:37.578Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nprint(pages[478][:2500])\nEOF"
}
```


## [2026-09-05T21:01:38.068Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T21:01:39.352Z] TOOL RESULT

```
    411                                                                    rosy

                                                                                                                     wrmyy'h
    10141 wrcwny} C                                                      war8-yon ©<*warda-gauna
          warcu/onya (wrc wnyO ©pi. wrcwnyt
            =^wrc}wny(h)                                                 GMS 1113; BSTBL, Dhy. 145, 146; Benv. Titres
          miracle, wonder                                                 et Noms Propres. 122; wrdYwn fiymy, Dhy.
          C2 gloss. p230; STi 21.18; GMS 939, 1088; BSTii                 145; "rose-colour" wrSYwn Twite,
            857.7, 861.57, 880.14                                         warSron-ronc, Dhy. 146; CII 1990 B15, 16
    10142 wrc wny* =4 wrcwny*                                     10154 wrg M                                (£^P
    10143 wrcxwndqy* M               uT* j*** (jJ^\cJ&,
          warc-xundakya                                                  warag
                                                                         Aries      =^wr*n
            ©*var?cahvant>*varcxwant>warcxund                            Hen. AM      1952, 203, 9
          miraculous
                                                                  10155 wryVY'nt ? B                                •l/(t^>)
          GMS 939; BBB; Hen. BSOAS 8.586, 12.307, 18,                    (wryVrY^t)
            (Cosm.)
                                                                         (name of a)plant
    10144 wrcy> B, M                     >l«*>J\flJ7                     TSP 3.286; S W, BSOAS 38, 1975, 133
          wo/iracya, wracya ? (wrcyh) ©*wi-rata-,
                                                                  10156 wryNvry'nt =» wrY}YJ*Y>nt?
          ^Sram- +usi-t wrt+sy} ?                                 10157 wryd'r- C                                           #*,mJ
          appeased
          BBB p67, 539; BSTBL, Dhy. 27, 94, 240; TSP                    wiraydar ®<*wrVt-6yr- ©trans, pret.
            3.217; Frag. Len. 44.10, 97b2; Gersh. Sogd.                    =»wrycd}r-
            Cpds. 145n 1; C2 p!48                                        (/o)pour
                                                                         STii 4.33; GMS 218; Sund. AoFviii 1981, 21V1
    10145 wrcy'str S                         JLjfJ'frJtW
          wiracyastar, wracyastar
```


### [2026-09-05T21:01:41.014Z] TOOL RESULT

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


## [2026-09-05T21:01:50.885Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nprint('leaves',len(pages))\nfor i in (472,481):\n    print('======== leaf',i,'printed',i+540)\n    print(pages[i][:3000])\nEOF"
}
```


### [2026-09-05T21:01:52.682Z] TOOL RESULT

```
leaves 684
======== leaf 472 printed 1012
    ‫—‬        ‫)‪0‬‬
                                                                                                                       ‫زراوه‬

 ‫ونفس ناطفه ‪ -‬و عقل فلك عطارد ‪ -‬ونورمجرد‪-‬‬                                 ‫تام خوای ابت که آن دونوع میباشد ‪ :‬یکی‬
        ‫وعفل فعال ‪ -‬ورب‌النوع انان وراست کوی‬
                                                                          ‫را زراوند طوبل میگوبند یمتی‌دراز وآترا شجرة‬
‫رالیز گوبن دکه‬               ‫ورردشت‬              ‫و لور ردان باشف ‪۷‬‬        ‫رستم و قتاءالحیه میخوانند » وآن نر باشد و از‬
                      ‫یشرو ویشوایا شس برستان است ‪.‬‬                         ‫انگشت بر گنده‌تر »گرم است در سیمو خشك‬
 ‫زر لك س با ای قرشت بر وزن‬                                                ‫است دردویم ؛ ودیگربرا زراوند مدحرج خوانند‬
‫کل کاو شه‬               ‫وخق‬      ‫باشف ‪۰‬‬          ‫خق‬     ‫آب‬   ‫که ‪۰‬‬   ‫زرد‬
                                                                           ‫است‬     ‫روف‬
                                                                                     ‫عو‬‫مشد‬
                                                                                         ‫بعتی هدور ؛ وآن ماده ای ما‬
                                                                           ‫»آن‬
                                                                             ‫مشامی(‪ .)۱‬بهترین‌آن زرد زعفرانی باشد و‬
                                                       ‫را لیز گفته‌اند‪.‬‬           ‫ودیرم و خشك است درسیم ‪.‬‬
                                                                                                        ‫کرم ادست‬
‫«کر انی فووقانی و لام‬
                    ‫رترلی؟ ب‬                                               ‫زاروه = بروزن کجاوه ‪ .‬پهلوالی است‬
                        ‫‪٠‬‏ زر طلا را گونند ‪۰‬‬            ‫بحتالی رصیده‬


 ‫زرر = بفتح اول وکسر انی و سکون‬
                                                                                       ‫گوبند وبعربی بحر خوانند ‪.‬‬
 ‫‪,‬بك راگوبند و آن پرنده ایت‬
                          ‫جیم فارسی ك‬
                                                                          ‫زراه ‪| ۲‬کفوده ؟ ‪ .‬بفتح همزه‬
 ‫ابی‌و آن دوقم میباشد‪ :‬دری و غیر دری ؟‬
                                                                           ‫وسکون‌کاف وضم فا پروزن افزوده » دربای خزر‬
                   ‫و دری بزر کت از غبر دری میشود ‪.‬‬
                                                                          ‫اکفوده نامآن در با است همحر دربای‬           ‫باشف جه‬

 ‫در جامی »با جیم بر وزن بدنامی‪,‬‬                                                             ‫عمان ودربای فازم وامثال آن ‪۰‬‬

                                         ‫لومی از انگور باشد ‪.‬‬              ‫دکر !ول و الك و سکون‬
                                                                                              ‫زرا لو ب‬
 ‫زجرعفری « بکرنانی» طلای‌خالس‬                                             ‫وبوند را‬
                                            
======== leaf 481 printed 1021
  ‫زربرا‬
                                                                                                   ‫—‬    ‫‪۵‬‬




 ‫واو بروزن ترخوان هم بتظرآمده است ؛ وشاید‬                                            ‫جنک وشند ‪۱‬و نام‬
 ‫لباشد چه‌این واوباند که معنوله‌باشه‬    ‫که درست‬                                              ‫یکی ‪ .‬از خبوتان‬
‫و واو معدوله السته بعد از خای شطه دار مفتوحم‬                                         ‫افراسیاب است‌واو سعی‬
                              ‫میباشد الله اعلم ‪٠‬‏‬                                        ‫ورن سیاوش‬          ‫تمام در‬


   ‫ن‬
   ‫زنربتتون ‪ ۵‬با ای فردشتوو‬                                                                  ‫کرد ‪ -‬و نام ولاب‬
 ‫فووقالی بروزن‌پربروفکن‪,‬بلفت زد وپلزند(‪)۱‬‬                          ‫ویا‬                   ‫‪۰‬‬       ‫ازن؟‬
                                                                                                    ‫ستت‪ ۴‬ا‬
                                                                                                         ‫ام‬

 ‫بمعنی کاشتن باشد ؛ و زریتولمی بکسر لون‌بمعنی‬                     ‫زره‬               ‫که‬       ‫ررهانتی‪۴‬‬


 ‫میکارم» وزریتولید بمنی بکارید و زراعت کنید ‪.‬‬               ‫بروزن صفرا شکن ‪ .‬بلغت‬                ‫ت‬‫شای‬
                                                                                                    ‫روت‬
                                                                                                      ‫قنون‬
                                                                                                         ‫با‬
                                                                        ‫زلد ویازلد(‪ )۱‬یمعثی زاسدن باشد ‪.‬‬
‫بفتح اول بروزن حربره تام‬       ‫=‬   ‫ددثر‬
‫برادر کشتاسب است ‪٩‬‏ ‪ -‬کویاهی باشد زرد که‬                     ‫زره پيچ ب بفتح اول وثالی و ظهور‬
 ‫جامه بدان رنگ کنند و آنرا اسپرك یز‬                          ‫الث وبای فارسی بنحتانی رسیده و بجیم فارسی‬
 ‫گوبند ‪ .‬و بعضی گوبند مرگے زرد چوبه است»‬                    ‫زده“ بلغت زد ویازند(‪ )۱‬بمعنی‌زمتان باشد که‬
 ‫و بعسی‌دیگرکونند کلی است وآن در کوهستان‬                                            ‫در مقابل تاستان است ‪.‬‬
‫حورجان بسیاراست‪ -‬و نام خلعلی هم هتکه‬                         ‫بقح اولرنالی وطهورها‬   ‫لشت ‪٩‬‏ =‬           ‫رره‬

 ‫آنراصفرا کوبند ہو برقاترا لیز کوبند و آن‬                    ‫فووقانی حضموم بشن و تای قرشت (‪ )۲‬زده '‬
    ‫ممد‬
      ‫آل ه‬
         ‫علتی است معروف ؛ و بکسر او‬                           ‫زردشت رگاوبند کهپیشوایآتش برستان باشد‪.‬‬
                                             ‫استخ‬

 ‫رر یرا = بروزن سرا ‪ .‬بلقت صربالی‬                            ‫بروزن و هنی زره تشت است که زردشت باشد ‪.‬‬

 ‫خرفه راگوبند و بعربی بقلةالمبار که وبقلةالحمقا‬              ‫‪ - ۳‬بپروزن مرهون» ببزان‬             ‫رهشون‬
                                        ‫خوانند ‪۹‬‬


                                    ‫‪.‬‬    ‫رشت‬
                                           ‫ق‪-‬‬‫(‪)۲‬چك ‪:‬‬
```


## [2026-09-05T21:02:01.014Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if 'زشت' in p:\n        print('leaf',i,'printed',i+540, p.count('زشت'))\nEOF"
}
```


### [2026-09-05T21:02:03.023Z] TOOL RESULT

```
leaf 16 printed 556 1
leaf 63 printed 603 1
leaf 64 printed 604 1
leaf 140 printed 680 1
leaf 158 printed 698 1
leaf 179 printed 719 1
leaf 182 printed 722 1
leaf 239 printed 779 1
leaf 311 printed 851 1
leaf 312 printed 852 1
leaf 325 printed 865 2
leaf 326 printed 866 1
leaf 327 printed 867 1
leaf 363 printed 903 1
leaf 380 printed 920 1
leaf 410 printed 950 1
leaf 443 printed 983 1
leaf 483 printed 1023 2
leaf 512 printed 1052 1
leaf 545 printed 1085 1
leaf 563 printed 1103 1
leaf 611 printed 1151 1
leaf 667 printed 1207 1
```


## [2026-09-05T21:02:07.334Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\np=pages[483]\ni=p.find('زشت')\nprint(p[max(0,i-2500):i+1500])\nEOF"
}
```


### [2026-09-05T21:02:09.110Z] TOOL RESULT

```
  ‫و‬
                                                          ‫بشدعروبی روت خوانند ‪.‬‬
                                                                              ‫بمعنی دیدن با‬


                                             ‫بیان هشتم‬
                 ‫در زای نقطه دار باعن بی نقطه مشتمل بر چهار لغت‬

‫خاله ای که باشد سام ابرص که لوعی از‬             ‫در‬    ‫با زای فرشت بروزن‌معذوره‬   ‫رعر ورد ‪-‬‬
‫در‬       ‫گرم است‬   ‫آن خاله‪ .‬نرود‪.‬‬   ‫چلیاسه امت در‬    ‫‪ ۴‬شیه‬    ‫صحرایی‬    ‫مبوه‌است‬    ‫مفرب‬   ‫بلغت اهل‬

                        ‫یکن از سیب بیارکوچکتر است وآنرا | دوم و خشك است در اول ‪.‬‬
                                                                               ‫ملیب‬
‫‪ ۰‬بمعنی‬         ‫جعفری‬     ‫زن‬
                           ‫رقو=‬
                              ‫‪,‬فر‬
                                ‫رع‬                                                 ‫افن‬
                                                                                     ‫بانرعل‬
                                                                                          ‫شراس‬
                                                                                             ‫درخ‬
          ‫زعفرانی باشد کهآن رنگه زرد است ‪٩‬‏ ‪.‬‬                                ‫و علف خرس کویند‬
‫زعیره بر وزن شعیر » در مجمم‌الفری‬                                            ‫و بعربی تفاح آلبری‬
  ‫سروری بمعنی تخم کتان نوشته اند ‪٩‬‏ ‪ ,‬و‬
 ‫آن‬                                                                              ‫رتءرالدب‬     ‫ود‬
                                                                                            ‫ارخ‬
                                                                                        ‫شتج |‬
‫دانه‌ای باشد که روغن ازآن گیرنده و باین‌معنی‬                                         ‫خوانند ‪.‬‬
‫در فرهنکک جهانگیری باغن نقطه دار آمدماست‬                          ‫ده‬         ‫رعفران مس‬
                                        ‫اله اعلم ‪.‬‬           ‫زعفران‬          ‫معروف‌است؟ ‪ .‬کونند‬
                                                                      ‫(‪ )۱‬چك ‪ - :‬کی ‪.‬‬

         ‫(خوف ‪ ,‬تفر آور ) «بارتولمه ‪٩ ۱۵۹۱‬‏ ‪-‬‬
                                            ‫م‬        ‫‪2‬تا‪36-4‬‬
                                                           ‫‪ - ۱‬پهلوی )‪ » 01562‬اوس‬
     ‫‪( 00121۵2 210151-‬مکروه » منفور) « بارتولمه ‪« ۳۹۹۱6‬ییبر کے ‪٩۵۲‬‏ افتانی ع ‪ 6532‬سریکلی‬
                             ‫‪( 612‬ماسد وخراب » بد » زشت) « اسشق ‪ “۲1‬وهروكی‪:‬شمان ‪۲٩1‬‏ ‪.‬‬
            ‫خوبی و بدی و زشت و زببا بگذشت ‪.‬‬            ‫‪ - ۴‬دوران بقاچو بادصحرا بگذشت‬
     ‫‪.‬‬     ‫«گلتان ‪۲‬‬
     ‫‪ < Mespilus‬لك ‪ ۲‬ص ‪sulipseM 201020۳۲68. » ۱۱۲‬‏ = از گیل‬                         ‫‪۳۴‬‏ =‬
     ‫‪nar = ۴‬‏‪« fas‬لك» ص‪ )/5160=۲ ۸۰۲‬کیاه زعفران کیاهی‌است یدازدار»‬                    ‫«ثایتی‪.*4۸۱‬‬
 ‫دارای گلهای بنفش روشن ودر مناطاق معتدل‌کاشته شود‪ .‬یامین‪-‬اقة آن برجستگی می بابد و این‬
         ‫والةٌ سرشاخه آن ارنجی رنك مایل بسرخی ومعطرست‬
                                                    ‫برجستگی همان‌پیاز زء‌فران‌میب‌اشد » کل‬
     ‫‪.‬‬     ‫؛ سنوده ‪۸8۱-۹۸۱‬‬    ‫و همین رشته‌هاست که بنام زعفرآن بمصرف مر سف ‪ .‬رك‪ :‬گل گلاب ‪۵‬‬

                ‫که کوبی قنیبی است از خیزران‪.‬‬           ‫© ‪ -‬هی زعفری خور ز دست بتی‬
     ‫« منوچهری دامغالی ‪۲٩٩‬‏ ‪.‬‬

 ‫ور غن ممجمه تخم کتان باشد که روغن چراغ از آن‬
                                            ‫‏‪ - ٩‬در سروری فزغیر بقتح را ک‬
                                    ‫گیرند وعربی کتان گویند ‪ .‬مثاش ‪ :‬سراح الدین راجی گوید ‪:‬‬

                ‫در زیر جراز چون زغیرامت ‪.‬‬               ‫هردل که ز رشك در زحیر امت‬
```


## [2026-09-05T21:02:28.775Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\np=pages[472]\nprint(p[2500:7000])\nEOF"
}
```


### [2026-09-05T21:02:30.543Z] TOOL RESULT

```
محر دربای‬           ‫باشف جه‬

 ‫در جامی »با جیم بر وزن بدنامی‪,‬‬                                                             ‫عمان ودربای فازم وامثال آن ‪۰‬‬

                                         ‫لومی از انگور باشد ‪.‬‬              ‫دکر !ول و الك و سکون‬
                                                                                              ‫زرا لو ب‬
 ‫زجرعفری « بکرنانی» طلای‌خالس‬                                             ‫وبوند را‬
                                                                                 ‫راب‬
                                                                                   ‫حتوانی مجهول وواو » نق‬
                                                                                                        ‫تنی‬
                                                                                                          ‫ثا‬
‫‪:‬‬           ‫پودمنسوب سعفر نامی کهکیمیا کر بوده اڪ‬                                                    ‫گوگ ‪.‬‬
 ‫وبعضی گوبند پیش ازجعفر برمکی زرقلب سکه‬                                   ‫را‬   ‫لب بروزن‌در بان» پیرسالشورده‬   ‫رربان‬

‫او وزير شد حکم فرمود که‬                                ‫میکردند چون‬        ‫گویند؟ ‪-‬ونام‌حضرت ابراهیمعله‌اللام‌است ‪۵‬؛‬
    ‫طلا را خالص کردند و سکه زدند و باو منسوپ‬                              ‫و باين معتی بجای بای ابجد فای سعقص و میم‬
                                                                    ‫قرف‬            ‫نیز آمده است که زرفان وزرمان باشد ‪۰‬‬
                                                                           ‫زر شت ‪٩‬‏ ‪ -‬بشم تای قرشت بوزرن‬
 ‫قطه‌دار وسکون شن وکاف » طلای خالص بی‌غل‬                                   ‫و نفس کل ‪-‬‬      ‫وبمعنی آفربدة اول ‪-‬‬    ‫‪۰‬‬    ‫ازنگشت‬


                                                                                            ‫(‪ )۱‬چش ‪ :‬بشاحی ‪.‬‬

             ‫اوستابی ‪2122‬‬                ‫‪۴‬‬                    ‫‪( 62100101510=2 ۱‬فر) « لك ‪ ۷‬ص ‪. » ۳۰۲‬‬
        ‫‪.‬‬    ‫‪ :‬اکفوده‬       ‫رك‬   ‫‪۴‬‬                     ‫(دربا) " پپلوی ‪ , 872‬بلوچی ‪ « 2۳12‬اسشق ‪۱٩۵‬‏ > ورك ‪ :‬درما ‪.‬‬
     ‫برائر وفق دادن نابجا‬                    ‫‪۴‬‬               ‫وك ‪ :‬زر » زال ‪۰‬‬
                                                                           ‫‪ - ۴‬مصحف «زرمان » (ه‪.‬م‪ ).‬ر‬
    ‫و تخلیط افکارابرالی بامعتقدات واساطیر سامی «زروان» ( که بهزر مان‌وزر بان صحصف شده) باابر اهیم‬

        ‫‪.‬‬      ‫زارت‬     ‫‪.‬‬    ‫زردشت‬   ‫‪:‬‬   ‫رك‬        ‫‪-‬‬   ‫‪۱‬‬            ‫‪. ۶۱۱‬‬
                                                                        ‫‪:‬زدستا ص ‪- ۳۱۱‬‬
                                                                                     ‫یپکنیداشته شده ‪ .‬رلا م‬
            ‫رکه ‪ :‬زرد کت » زرده‪.‬‬                 ‫‪۸‬‬               ‫ليه این معالی محمول است‪ .‬رك ‪ :‬زردشت‪.‬‬         ‫‪۷‬‬

                                                             ‫‏‪ ٩‬صحیح زر طلی وزر طلا است ‪ .‬ر کت‪ :‬زر طلی‪.‬‬
```


## [2026-09-05T21:02:38.547Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nimport re\nfor i in range(468,490):\n    p=pages[i]\n    for m in re.finditer(r'zaran|zairi|zarn|zart|zar\\b|Zar', p):\n        print(i, i+540, repr(p[max(0,m.start()-200):m.start()+200]))\n        break\nEOF"
}
```


### [2026-09-05T21:02:40.332Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:02:51.531Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=raw.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ('زرنیخ','زرنيخ','زردک','زرگون','زرگون'):\n        if w in p: print(w,'leaf',i,'printed',i+540)\nEOF"
}
```


### [2026-09-05T21:02:53.137Z] TOOL RESULT

```
زرنیخ leaf 227 printed 767
زردک leaf 228 printed 768
زرنیخ leaf 479 printed 1019
```


## [2026-09-05T21:02:53.422Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT arsenic\"; python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# printed 26 -> leaf 46\nfor n in (45,46,47):\n    p=t[n]\n    i=p.lower().find('arsenic')\n    if i>=0:\n        print('leaf',n)\n        print(p[max(0,i-700):i+700])\nEOF"
}
```


### [2026-09-05T21:02:55.163Z] TOOL RESULT

```
=== SKT arsenic
leaves 657
```


## [2026-09-05T21:02:58.485Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"arsenic\" SKT.txt | head -10\necho \"=== KLN 1971 arsenic\"; grep -n -i \"^arsenic\\|arsenic, n\" KLN_1971.txt | head\necho \"=== KLN zircon jargon\"; grep -n -i \"^zircon\\|^jargon\\|zargun\\|zargūn\" KLN_1971.txt | head"
}
```


### [2026-09-05T21:02:58.562Z] TOOL RESULT

```
1178:ifiShyw  ralpharrt  of  arsenic '  gold  ptint-'  F.  ot-timtnt. ifw.  gold  paint.  *  L.  Avn-. IxL  fismtnlum,  a  pigment, f»rr.  1     V— •
=== KLN 1971 arsenic
20091:arsenic, n., a chemical element. — OF. (= F.) 
20092:arsenic, ' fr. L. arsenicum, arrhenicum, fr. Gk. 
212887:arsenic and sulfur (mineral.) — Named after Sar- 
=== KLN zircon jargon
128326:jargon, n., confused speech. — OF., ‘chatter, 
128332:jargon, also jargoon, n., a variety of zircon. — 
128334:ult. fr. Pers. zargun, ‘gold-colored’, compound of 
128337:jargonelle, n., an early variety of pear. — F., 
270763:zircon, n. — F., a var. of jargon, ‘a variety of zir- 
270767:zircon-ic , adj., zirconium (q.v.) 
270769:zirconate, n., salt of zirconic acid (chem.) — 
270772:zirconia, n., zirconium dioxide (chem.) — ModL., 
270775:zirconium, n., name of a metallic chemical ele-
```


## [2026-09-05T21:03:01.167Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20091,20106p' KLN_1971.txt\necho \"----- jargon\"\nsed -n '128326,128342p' KLN_1971.txt\necho \"----- zircon\"\nsed -n '270763,270782p' KLN_1971.txt"
}
```


### [2026-09-05T21:03:01.288Z] TOOL RESULT

```
arsenic, n., a chemical element. — OF. (= F.) 
arsenic, ' fr. L. arsenicum, arrhenicum, fr. Gk. 
<£p<revix6v, dcppevtx6v, ‘yellow orpiment’, fr. 
MPers. *zarnik, ‘gold, golden ; orpiment’( whence 
ModPers.-Arab. zarntkh, ‘orpiment’), through 
the medium of a Semitic language; cp. Mish- 
naic Heb. zarntkh, Syr. zarnikhd, ‘orpiment’. 
Cp. Avestic zaranya, Pers. zar, ‘gold’, and the 
first element in zermahbub, and see yellow and 
words there referred to. Cp. also jargon, ‘a 
variety of zircon’. Gk. apaevtx6v, appevix6v, 
‘orpiment’, was influenced in form by apaevix6<;, 
dppevtxi?, ‘male’, fr. dpmqv, dppyjv, ‘male’. For 
the sense development of MPers. *zarnik, cp. L. 
auripigmentum , fr. aurum , ‘gold’ (see orpiment). 
Derivatives: arsenic, arsenic-al , adjs. 
----- jargon
jargon, n., confused speech. — OF., ‘chatter, 
warbling’, from the same base as E. gargle. This 
base means lit. ‘to make noise with the throat’. 
See gargle, gurgle. 

Derivative: jargon-ize, intr. and tr. v. 
jargon, also jargoon, n., a variety of zircon. — 
F., fr. Port, zarcao , fr. Arab, zarqdn, ‘minium’, 
ult. fr. Pers. zargun, ‘gold-colored’, compound of 
zar , ‘gold’ (sec arsenic), and gun- ‘color’, which 
is rel. to Avestic gaona-, ‘color’. Cp. zircon, 
jargonelle, n., an early variety of pear. — F., 
dimin. of prec. word; so called from its color. 
Jar!, n., a Scandinavian chieftain. — ON. jarl , 
‘a man of noble birth, chief’. See earl, 
jarool, n., the tree Lager stroemia reginae. — 
Hind, jarul. 
----- zircon
zircon, n. — F., a var. of jargon, ‘a variety of zir- 
con’ (q.v.) 

Derivatives: zirconate (q.v.), zirconia (q.v.), 
zircon-ic , adj., zirconium (q.v.) 

zirconate, n., salt of zirconic acid (chem.) — 
Formed with chem. suff. -ate fr. zircon (q.v.) 

zirconia, n., zirconium dioxide (chem.) — ModL., 
formed fr. zirconium. See next word and 1st -ia. 

zirconium, n., name of a metallic chemical ele- 
ment. — ModL., coined by the German chem- 
ist Martin Heinrich Klaproth (1743-1817) in 
1789 (on analogy of many other element names 
ending in -him) fr. zircon (q.v.); so called by 
him because it is found in the mineral zircon. 

zither, n., a musical instrument with twenty-five
```


## [2026-09-05T21:03:21.138Z] TOOL CALL #41: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T21:03:21.143Z] TOOL RESULT

```


```


## [2026-09-05T21:03:23.958Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/arsenic",
 "prompt": "Full etymology of arsenic: give the chain (Old French, Latin, Greek arsenikon, Syriac, Middle Persian zarnik) and any dates of attestation."
}
```


## [2026-09-05T21:03:25.143Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/zircon",
 "prompt": "Full etymology of zircon and jargon (the mineral): German Zirkon, French jargon, Italian giargone, Arabic zarqun, Persian zargun. Quote it."
}
```


### [2026-09-05T21:03:30.292Z] TOOL RESULT

```
# Etymology Chain of Arsenic

The word "arsenic" traces back through multiple language layers:

**Late 14th century English** → "yellow arsenic, arsenic trisulphide"

**Old French** *arsenic* 

**Latin** *arsenicum*

**Late Greek** *arsenikon* (documented by Dioscorides and Aristotle)

**Syriac** *(al) zarniqa* "arsenic"

**Middle Persian** *zarnik* "gold-colored" (referencing the lemon-yellow hue of arsenic trisulphide)

**Old Iranian** *\*zarna-* "golden"

The Greek term itself represents a folk etymology: "The form of the Greek word is folk etymology, literally 'masculine,' from *arsen* 'male, strong, virile'" — supposedly alluding to the substance's potent properties.

The ultimate origin connects to the Proto-Indo-European root *\*ghel-* (2), meaning "to shine," which generated terms for bright materials and gold across various ancient languages. The element designation dates from 1812.
```


### [2026-09-05T21:03:30.816Z] TOOL RESULT

```
# Etymology of Zircon

The word "zircon" has a fascinating multilingual journey. According to the Online Etymology Dictionary, the term entered English in 1794 from German *Zirkon* (coined by chemist Klaproth in 1789). 

The etymology traces back through: "18c. French *jargon*, a vague mineral word used of high-quality diamond-like gemstones." This French term derives from Medieval Latin *jargonce*, with parallels in Italian *giargone*. The Dictionary suggests a possible Arabic origin: *zarkun* meaning "cinnabar."

The word initially replaced an older gemstone name—*jacinth*—when chemistry needed a new designation for this yellowish crystalline mineral. Interestingly, the same root gave us "jargon" in its modern linguistic sense, though the mineral meaning is now archaic in that context.
```


## [2026-09-05T21:03:36.082Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B4%D8%AA",
 "prompt": "Persian زشت (zešt): give the full etymology section verbatim — Middle Persian, Proto-Iranian, Avestan forms, and any cited sources (Cheung, Hasandust, MacKenzie)."
}
```


## [2026-09-05T21:03:37.306Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1%D9%87",
 "prompt": "Persian زهره: give all etymology sections verbatim (the 'gall bladder / courage' sense and any Arabic-origin sense), with Middle Persian and Avestan forms."
}
```


### [2026-09-05T21:03:43.129Z] TOOL RESULT

```
# Etymology of Persian زشت (zešt)

Based on the Wiktionary article provided, here is the complete etymology section:

The word is **inherited from Middle Persian** _𐭦𐭱𐭲_ (zyšt' /⁠zišt⁠/, "hateful, ugly"), which itself was **a loanword from Avestan** _𐬰𐬀𐬉𐬱𐬀_ (zaēša). 

This traces back to **Proto-Indo-Iranian** _*ȷ́ʰáyždas_, which derives from **Proto-Indo-European** _*ǵʰéysd-os_, ultimately stemming from _*ǵʰeysd-_ ("anger, agitation").

The article notes this is **cognate with Proto-Germanic** _*gaistaz_ ("ghost, mind").

**Note on sources:** The article cites Hayyim, Sulayman (1934) in the *New Persian–English dictionary*, but does not include references to Cheung, Hasandust, or MacKenzie that you requested. The etymology section itself indicates it "lacks references or sources."
```


### [2026-09-05T21:03:44.265Z] TOOL RESULT

```
# Persian زهره Etymology Sections

## Etymology 1 (Gall/Courage)

Inherited from Middle Persian zʾhlk' (/zahrag/, "gall; bile"), suffixed from Proto-Iranian *jarHáH, from Proto-Indo-European *ǵʰolh₃-éh₂. Comparable forms include Avestan 𐬰𐬁𐬭𐬀 (zāra, "gall"), Northern Luri زںڵںە (zəłə), Ancient Greek χολή (kholḗ, "gall; bile"), and Old English ġealla ("gall").

The noun denotes:
1. Gallbladder; gall
2. (Figurative) Courage; gall

## Etymology 2 (Venus)

Borrowed from Arabic الزُّهَرَة (az-zuhara).

The proper noun designates: Venus, the second planet in the Solar system.
```


## [2026-09-05T21:03:54.711Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1",
 "prompt": "Persian زر (zar) 'gold': quote the etymology (Middle Persian zarr, Proto-Iranian *jaHrnya-, Avestan zaranya-, PIE root). Also any derived terms like زرگون, زرنیخ."
}
```


## [2026-09-05T21:03:56.356Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%86%DB%8C%D8%AE",
 "prompt": "Persian زرنیخ (zarnix) 'arsenic/orpiment': quote the etymology in full — Middle Persian *zarnīg, Arabic زرنيخ, Syriac, Greek arsenikon."
}
```


### [2026-09-05T21:03:58.211Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T21:04:01.339Z] TOOL RESULT

```
# زر (Zar) - Comprehensive Overview

## Primary Meanings Across Languages

The Arabic word **زر** carries multiple distinct meanings depending on etymological origin:

**In Persian and related languages:** "Gold" - derived from Middle Persian *zarr*, with roots tracing to Proto-Iranian *jaHrnya- and ultimately Proto-Indo-European *ǵʰelh₃- ("green, yellow").

**In Arabic:** 
- A verb meaning "to button," "to beam," or "to encroach"
- A noun denoting a "button" or "switch button"

**In Baluchi:** Both "gold" and "ocean/sea"

**In Central Kurdish:** "Heart" (anatomy) or "hearts" (card games)

**In Pashto:** The numeral "thousand" (zër) or the noun "metal" (zar)

## Linguistic Distribution

The term appears across nine languages in Wiktionary, with Persian and Arabic as primary sources. The gold-meaning variant demonstrates ancient Indo-European linguistic connections, appearing in cognates like English "gold" and Old Church Slavonic "zlato."
```


## [2026-09-05T21:04:06.785Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%86%D9%8A%D8%AE",
 "prompt": "Arabic زرنيخ (zirnīḵ): quote the etymology in full — from Middle Persian / Persian zarnīk, and any mention of Syriac or Greek."
}
```


## [2026-09-05T21:04:08.625Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%AF",
 "prompt": "Persian زرد (zard) 'yellow': quote the etymology (Middle Persian zard, Proto-Iranian *jarHita-, Avestan zairita-, PIE). Also, is زردک (zardak, carrot) listed as a derived term?"
}
```


### [2026-09-05T21:04:12.997Z] TOOL RESULT

```
# زرنيخ (Arsenic) Etymology

The Arabic term **زرنيخ** (zirnīḵ) meaning arsenic derives from Middle Persian sources. According to the Wiktionary entry: "From Middle Persian zarnīk or zarīk, 'golden'."

The word traces back through an extensive etymological chain:
- **Proto-Indo-European** root *ǵʰelh₃- (green/yellow)
- **Proto-Indo-Iranian** and **Proto-Iranian** forms
- **Old Median** *zaraniyakā*
- **Middle Persian** *zarnīk*
- **Classical Syriac** *zarnīḵā*
- **Arabic** زرنيخ

The Persian cognate زرنی (zarni) meaning "orpiment" (a yellow arsenic compound) reflects the shared origin—the name literally references the substance's golden-yellow color.

The word subsequently influenced other languages, including Middle Armenian and Maltese, demonstrating its importance in medieval scientific and trade terminology across multiple linguistic communities.
```


### [2026-09-05T21:04:14.686Z] TOOL RESULT

```
# Summary of the Wiktionary Entry for زرد (Zard)

## Etymology
The Persian word زرد (zard, "yellow") derives from Middle Persian, with the etymological path being: "From Middle Persian 𐭦𐭫𐭲𐭠 (zlt' /zard/, "yellow")" and relates to زر (zar, "gold").

The Proto-Indo-European root is *ǵʰelh₃- ("green, yellow"), connecting to cognates like Old Church Slavonic "zlato" (gold) and English "gold."

## Derived Terms Question
Yes, زردک (zardak) appears in the Persian section under "Related terms" rather than "Derived terms." The entry lists: "زردک (zardak)" as a related word, though the specific meaning (carrot) isn't explicitly stated in this excerpt. The distinction suggests these are semantically connected rather than morphologically derived forms.
```


## [2026-09-05T21:04:25.154Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (45,46,47):\n    p=t[n]\n    print('=== leaf',n, repr(p[:80]))\n    import re\n    for m in re.finditer(r'[Aa]rsenic|ARSENIC', p):\n        print(p[max(0,m.start()-500):m.start()+500])\n        break\nEOF"
}
```


## [2026-09-05T21:04:27.744Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT\"; grep -n -i \"zarnikh\\|zarnīḵ\\|arsenik\\|zarqun\\|zargun\\|zarkun\" LKT.txt | head -10\necho \"=== PLA djvu\"; grep -n \"زرنيخ\\|zirnīḫ\\|zarnīk\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10\necho \"=== AFM\"; grep -n \"الزرنيخ\\|زرنيخ\" AFM_pages.txt | head -5\necho \"=== DEV/PHN arsenic jargon\"; grep -n -i \"^ARSENIC\\|^JARGON\\|arsenic\" DEV.txt PHN.txt | head -10"
}
```


### [2026-09-05T21:04:47.117Z] TOOL RESULT

```
=== leaf 45 'gK awe,  fear:  Dan.azv.+AS.  tf;$T,  <>^;  Gom. tj^,  fear,  anguish ;  Irish  '
=== leaf 46 '.  which  is  allied  to  L.  ituum,  Gk. of^,  an  age.     Cf.  Gk.  altt,  it'
=== leaf 47 'ed,  jadeil micKKiV  <•  Icel biigr,aaeasy.biigr,^v>i.,. ,  ..<> to  hinder,  op'
```


### [2026-09-05T21:04:47.199Z] TOOL RESULT

```
=== LKT
3851:'Rotes  Schwefelarsenik'  [eigentlich  'Höh- lenpulver', aus  ra%"'Pulver',  ^är'Höhle', weil  man  das  Arsenik  aus  Minen  ge- wann]; hieraus  s^.rejalgar,  pg.resalgar, rosalgar,  it.  risigallo,  risogello,  (alt)  Pisa risalgado;  dtsch.  Realgar  'Rauschgelb', engl,  realgar  'red  orpiment'  [<;^  frz.  or- piment  <^  lat.  auri  piymentmn].  [DE 332/333.    Eguilaz  482.    ML  7011.
4384:'Gemisch  von  arseniger  Säure  und  Queck- silber, Arsenik'  [SANGUINETTI  in  JAs 1866,  I;  Adj.  zu  Sulaiman,  N.  pr.,  =
=== PLA djvu
=== AFM
=== DEV/PHN arsenic jargon
DEV.txt:325:2(j.  Azarnct,  adarnech,  zarmcli,  zarnec,zar ne,  ov[)\mQni\ esp.  azarnefe;  de  l'arabe-persan  ^^J^  az-zermhh,  qui  est le  même  mot  que  le  grec  àpcreviKos,  arsenic  jaune,  orpi- ment.
DEV.txt:1555:Jargon.  Gemme  de  couleur  jaune  tirant  sur  le  rouge, souvent  confondue  avec  VhyacintJie.  Le  minéralogiste  Haûy a  réuni  ces  deux  sortes  de  pierres  sous  le  nom  commun de  zircon.  Ital.  giargone.  Jargon  et  zircon,  dont  personne, à  ma  connaissance,  n'a  encore  établi  l'étvmoloffie,  sont certainement  identiques  à  l'espagnol  azarcon.  D'après  le Dictionnaire  de  l'Académie  espagnole,  azarcon,  en  pein- ture, signifie  orangé  vif  :  ^e\  color  naranjado  muy  encen- dido,  color  aureus;v  ce  qui  s'applique  très-exactement  à l'hyacinthe.  Azarcon  s'est  dit  aussi,  comme  le  portugais zarcâo,  zarquào,  azarcâo,  de  l'ocre  rouge.  Et  tous  ces  mots correspondent  à  un  terme  arabe,  ij^)';)  zarqoûn,  avec  l'ar- ticle az-zarqoûn,  qui  se  disait  du  minium  et  d'autres  sub-
DEV.txt:1975:Réalgar.  Vieux  franc,  réagal ,  riagal,  esp.  rejalgar,  ital. risigallo.  De  l'arabe  ^IxJi  ^^  rehdj  al-ghâr,  littéralement poudre  de  caverne,  nom  que  portait  l'arsenic  chez  les  Arabes du  Maghreb  ^.
DEV.txt:3690:Jargon.
PHN.txt:1845:ARSENIC, 8. m. (p.)
PHN.txt:1846:^JJ [i^erntM] oijnment, arsenic jaune, mot également usité chez
PHN.txt:1849:du latin arsenicum, dont nous avons fait arsenic. — - Les étymo-
PHN.txt:1850:logistes se sont trompés, je pense, en disant que arsenic vient
PHN.txt:1855:dont le sens n'a aucun rapport avec celui de Varsenic; et je
PHN.txt:10250:Arsenic, s. m. (p.) 45
```


## [2026-09-05T21:04:59.249Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHN arsenic\"; sed -n '1840,1870p' PHN.txt\necho \"== LKT zirkon/zarqun\"; grep -n -i \"zirkon\\|jargon\\|zarqun\\|zarq\" LKT.txt | head -10"
}
```


### [2026-09-05T21:04:59.304Z] TOOL RESULT

```
== PHN arsenic
r. Haçan ibn Norman de bâtir à Tunis un dâr cinâ^a pour la cons-
^ truction de tout ce qui est nécessaire à l'équipement et à l'ar-
^ mement des vaisseaux. C'est dans cette acception spéciale que
''le mot a passé dans presque toutes les autres langues euro-
^ prennes. Voyez Jal , Gloss. naut, y>ART /if)
ARSENIC, 8. m. (p.)
^JJ [i^erntM] oijnment, arsenic jaune, mot également usité chez
les Arabes, et qui, précédé de Tarticle Jl [al], donne ji^t^p!
[azzemikh]j prototype de la transcription grecque dpcreviKÔv et
du latin arsenicum, dont nous avons fait arsenic. — - Les étymo-
logistes se sont trompés, je pense, en disant que arsenic vient
de ipcmv, mâle, fort, et de vixçiv^ vaincre, dompter (littérale-
ment, qui dompte les forts), à cause de la propriété vénéneuse
de cette substance. Pour moi, je n'y reconnais qu'une analogie
dortbographe avec l'adjectif grec ipereviKés, tf, 6v^ masculin, e,
dont le sens n'a aucun rapport avec celui de Varsenic; et je
considère ce dernier mot comme une altération du persan,
dont la première syllabe jj) [zer], qui signifie or, sert peut-être
h indiquer la couleur de l'orpiment à l'état naturel. C'est de
jê^j^\ [azzemikhl^ que les Espagnols ont fait azamefe, sorte de
poison. En portugais, on trouve aussi le vieux mot azamete,
avec le même sens.
ARTICHAUT, s. m. composé, (a.)
Les dictionnaires ne sont pas d'accord sur l'origine de ce
mot : les uns disent qu'il vient du latin arsus carduus [chardon
cuit), ce qui est inadmissible, attendu que l'on mange aussi
l'artichaut à l'état naturel; d'autres lui donnent pour racine les
deux mots celtiques art [^épine) et chaulx (chou); M. Defrémery
le rapporte de préférence au grec àfmnixd, — Bien qu'en
arabe ^artichaut soit appelé spécialement Ul^j^ [/l'arc/ia/] ,
mot reproduit par l'espagnol alcachofa et alcarchofa, ainsi que par■\
== LKT zirkon/zarqun
2075:'Teil'  [Ave-L  IV,  o30],  hieraus  jüd.- dtsch.  Chelek  'Teil,  Anteil  an  der  Diebes- beute', ndl.  (Gaunerjargon)  cheilek:  Man spricht  von  einem  eh.,  wenn  bei  einem Verkaufe  oder  einer  Versteigerung  sich einige  Personen  ohne  Wissen  des  Ver- käufers heimlich  verbinden,  nicht  gegen- einander zu  bieten,  und  später  das  Ge- kaufte unter  sich  verteilen.  [Dozy  Oost  30.
```


## [2026-09-05T21:05:00.954Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== SKT ghost\"; grep -n -i \"GHOST\" SKT.txt | head -5\necho \"== IEC gheis\"; grep -n \"gheizd\\|ghoizdo\\|gaisto\" IEC.txt | head -10\necho \"== SYN gold/gall\"; grep -n -i \"zaranya\\|zar 'gold'\\|kholē\\|Av. zairita\" SYN.txt | head -10"
}
```


### [2026-09-05T21:05:01.039Z] TOOL RESULT

```
== SKT ghost
7553:GHOST.
8251:haggard  (a\  Inn,  meagre  (E.)  Orig kagg^d,  i.e.  hag-like,  from  hag.  'The ghostly  prudes  with  MaggtJ  face/  Gray, A  Lonfj  Story,  near  end.  Btisspelt  by  con- fusion with  the  word  below.
10149:Lemur,  a  noctonial  animaL  (L.)  I* lemur,  n  ghost :  so  nicknamed  by  oaSorai-- isls  from  Its  nocturnal  habits.
17998:spectre.   (F.  -  L)      F image,  ghost ;    Cot.^L.  s^etrum,  S
== IEC gheis
== SYN gold/gall
15393:pédaua Dan. guld ChSl. lato Lat.  aurum Sw. guld SCr. zlato It. oro OE gold Boh. _zlato Fy. or ME gold Pol. —_zlato Sp. oro NE gold Russ. zoloto Rum. aur Du. goud Skt. hiranya-, jalaritng. Ir. or OHG gold Av. zaranya-, OPers Nir. or MHG golt daranya- 4 W. awr NHG gold Br. dour
15395:Goth. gulb, OE gold, etc., general Gmc.; Lett. zelts, ChSI. zlato, etc., gen- eral Slavic; Skt. hiranya-, Av. zaranya-, OPers. daranya- (Dar. Sus. f. 35), all neuters.
```


## [2026-09-05T21:06:21.599Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1165,1195p' SKT.txt\necho \"=== which leaf is line 1178?\"\npython3 - <<'EOF'\nraw=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\npos=sum(len(l)+1 for l in lines[:1177])\nprint('leaf', raw[:pos].count('\\f'))\nEOF"
}
```


### [2026-09-05T21:06:23.373Z] TOOL RESULT

```
fvith  a  window)  in  a
E.   firicJ,   oryalt,    a
ctp.  a  room  for  a  lady,
—  Low  L  oriolum,  a portico ;  prob.  for B  omnmcnted  with
M,  gold.     ^  S«  F'liny.  b.
PHtom  of  gilding  apart- >td  standard  of  France. he,  the  sacrrd  standard L.  aMrifiamma,  lit bcoraw  the  banner  wu  cat rtrips  at  the  outer  edge,  nn-i
—  L.  fl*rr-,  for  o«/»-, ft  gold ;  and  yfciffi  ma,  a
Ihnrth.     (F.  -  L.)
?/«r,  golden.
r©f  brass.  (F.-L.)    F.
led  gold.'""F.  or,  from
'  mouiUt  pp.  oimoudrt,
in,  which    from  L.
ifiShyw  ralpharrt  of  arsenic '  gold  ptint-'  F.  ot-timtnt. ifw.  gold  paint.  *  L.  Avn-. IxL  fismtnlum,  a  pigment, f»rr.  1     V— •
;>itl  slnnc-crop.
od  M  'i>ut.     M   b.
l\u»,  *  orpiD,  or  lire'long ; *  Cot     A  docked  form  of
^UMUltAUon ;  seeAadi-
AVAST,
«3
Aurora,  the  dawn.  (L.)  L.  avrem,  the dawn  ;  put  for  an  oldtri  ausosa  *.+Gk.  ijif, ..4iolic  afaff  ;  Skt.  uikAsd,  dawn.    (^US.)
Auepioe.  (F.-L.)     See  Aviary.
Austere.  (F.-L.-Gk.)     '^A.'E.  amUrt.
—  O.  h' .  aujtfr:f.»h. aufUrvs,  harsh,  severe. ■•Gk.  a^Tij^r,  making  the  tongue  dry, harsh.  — Gk.  aSor,  parched;  aCur,  to  parch, dry.     See  8ere.
Austral.  (F.-L.;  *r  L.)  We  find  F, QMitraU,  ••outhcrly';  Cot.  — L.  j^iw/nr/w, southerly.  —  L.  Austtr,    the  South  wind.
(vus.)
Authentic.  (F.-I..-Gk.)  M.  E.  an. tifitujue,  auifnti'A.  —  O.  F.  anttntiqut.  later attikentiqut{}ZoX,')^  L.attMf«/#fTi*/,  original, written  with  the  author's  own  hand.  — Gk. oMtfTicvr,  vouched  for,  warranted.  —  Gk. o\AivTt\\.  one  who  docs  things  wilJi  his  own hand.     (Of  uncertain  origin.)
Author.  (U)     See  Auction.
Auto-,  prefix.  (Gk.)  Gk.  ayro-.  crude form  of  a\rTo%,  lelf.  Dor.  autO'hio^rafhy, a  biography  written  by  oneself  (see  Bio- grapby) ;  autogrttph,  something  in  one's own  handwriting,  from  Gk.  'ip&^uv,  to write  <scc  Oraphio).
automiLton,  a  self-moving  machine. (Gk.)  Gk.  airroiAarov,  neut.  of  avro/iaroi, self-moving.  —  Gk.  avrd-,  for  ovrdj,  self; and  a  stem  ftar-,  appearing  in  ^r-ti^,  I seek  after,  strive  to  do.  Cf.  Skt.  ma/d, desired,  pp.  of  mdn,  to  think.  (^MAN.) autonomy,  seU-govemmcnt.  (Gk.)  Gk. avjovo}ila,  independence.  —  Gk.  oiriivo^nr, ijtc,  living  by  one's  own  laws.  — Gk.  avru', self;  and  wifxoftat,  1  sway,  from  vifttty,  to distribute  (see  Nomad).
autopsy,  personal  inspection.  (Gk.) Gk.  avToif/ia,  a  seeing  with  one's  own  eyes.
=== which leaf is line 1178?
leaf 43
```


## [2026-09-05T21:06:31.981Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"zarnikh\\|zernikh\\|zar,  gold\\|al-zarnikh\\|orpiment\" SKT.txt | head -10\necho \"--- leaves 44-48 search rsenic\"\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor n in range(42,50):\n    for m in re.finditer(r'rsenic|rsenik|zarn|zern', t[n]):\n        print('leaf',n, repr(t[n][max(0,m.start()-400):m.start()+400]))\n        print('~~~')\nEOF"
}
```


### [2026-09-05T21:06:33.673Z] TOOL RESULT

```
12888:Orpiment.  Orpine ;  see  Aureate.
15701:Healgar,  red  orpiment.  (F.  -  Stan.  — Ar.%b.)  F.  rhtl^r.  —  Span,  rrja/gitr,  • Arab,  rahj  ol-gMr^  powder  of  llie  mine, mineral  i;>owder.  —  Arab.  roA/,  powder ;  a/, the :  ghdr,  a  cavern,  mine.
23109:orpiment- orpine.              ^^^B
--- leaves 44-48 search rsenic
leaf 43 '  b.\nPHtom  of  gilding  apart- >td  standard  of  France. he,  the  sacrrd  standard L.  aMrifiamma,  lit bcoraw  the  banner  wu  cat rtrips  at  the  outer  edge,  nn-i\n—  L.  fl*rr-,  for  o«/»-, ft  gold ;  and  yfciffi  ma,  a\nIhnrth.     (F.  -  L.)\n?/«r,  golden.\nr©f  brass.  (F.-L.)    F.\nled  gold.\'""F.  or,  from\n\'  mouiUt  pp.  oimoudrt,\nin,  which    from  L.\nifiShyw  ralpharrt  of  arsenic \'  gold  ptint-\'  F.  ot-timtnt. ifw.  gold  paint.  *  L.  Avn-. IxL  fismtnlum,  a  pigment, f»rr.  1     V— •\n;>itl  slnnc-crop.\nod  M  \'i>ut.     M   b.\nl\\u»,  *  orpiD,  or  lire\'long ; *  Cot     A  docked  form  of\n^UMUltAUon ;  seeAadi-\nAVAST,\n«3\nAurora,  the  dawn.  (L.)  L.  avrem,  the dawn  ;  put  for  an  oldtri  ausosa  *.+Gk.  ijif, ..4iolic  afaff  ;  Skt.  uikAsd,  dawn.  '
~~~
```


## [2026-09-05T21:07:17.393Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (45,46,47):\n    print('==== leaf',n)\n    print(t[n][:1600])\nEOF"
}
```


### [2026-09-05T21:07:19.514Z] TOOL RESULT

```
==== leaf 45
gK awe,  fear:  Dan.azv.+AS.  tf;$T,  <>^;  Gom. tj^,  fear,  anguish ;  Irish  ^agfiat^  fcar. terror;  Gk.  ix°'i  anguish,  afmctioa;  L anj;ffr,  choking,  anguish  ;  Skt.  ag^A,  fla 1'he  orig.  sense  ia 'choking.*  (<^  AGU.) See  Anffuiali.     Der.  aw-fuL
oil.   (E.)    A.S.  iglan,  to  paIn.-A& eg€,  fear,  orig.  pain  (above).
Awkwan£  clumsy.  (Scand.  and  E) Orig.  on  adv.,  signifying  '  transversely.'  or '  in  a  backhanded  manner.*  M .  E.  awhacx^i^ awkumrt\  *  owkwari  he  couth  htm  ta'> he  gave  him  a  backhanded  stroke,  Wallace, iii.  J  75.  p.  The  suflfix  -warJ  is  E.,  as  is fer-ward,  on-ward,  &c  The  prefix  i> M.  E.  auk,  ttwk,  contmryj  perverse,  wroitf  t this  is  a  contraction  of  Icel.  6/ug-t  13(C hatvk  from  AS.  ^a/**.  — Icel.  o/ugr,  oftca contracted  to  efgu^  adj.,  turning  the  *TaS way,  back  foremoit,  contrary,  v.  Hcre^ is  for  of,  off,  from,  away ;  and  -«f-  is  1 suffix.  Cf.  O.  H.  G.  <7/-hA.  M.  H.  G,  «*■ uh,  turned  away,  perverse;  from  4^»G. ab,  off,  away,  and  the  sufBx  -uh,  Al^ Skt.  0/rfi,  apaHch,  lomed  away ;  from  sp^ for  o/Si,  oH^  away,  and  aAch,  to  bend,  fll which  an  older  form  must  have  beea nasalised  for  ok.  6.  Thus  the  sense is  'bent  away  ' ;  from  Icel.  a/,  cogr £.  0/,  off;  and  a  sufhx,  from  the to  bend.     See  Of.
Awl.  (E.)    M.  E.  awv/,  ««/.  «/,  el. awe/,  also  ix/,  an  awl.  +  Icel.  a/r :  G. Skt.  JrJ;  lit.  'piercer.'     Cf.  Ski. to  pierce,  causal  of  n',  to  go.
Awn.  (Scand.)  ME.  (^t/ji/ C
==== leaf 46
.  which  is  allied  to  L.  ituum,  Gk. of^,  an  age.     Cf.  Gk.  altt,  itl.  ever.
Azimuth.  (Arab)  Azimufhal  circles are  great  circles  oo  the  sphere  that  pa» through  the  ufiith.  Properly,  azimuth  is a  pi.  form,  answering  to  Amb.  as-santtil^ ways,  or  points  (or  quarters)  of  the  hori/on  ; fronn  at  same,  sing.,  the  way,  or  point  (or quarter)  of  the  horiron.  —  Arab.  «/,  the; and  xamt,  a  way,  quarter,  direction ;  whence also  E.  ttmth.
Asote,  nitrogen.  (Gk.)    See  Zoology.
Axure,  blue.  (F.  —  Arab.)  M.E  asur, ature.  —  O.  F.  atur,  ft£ure  ;  a  corrupted form,  standing  for  laxur,  which  was  mis- taken for  I'atur,  as  if  the  initial  /  indicated the  def.  article.  —  Low  L.  iatur,  an  azure coloured  stone,  also  called  laptj  lazuli.^ Arab.  Idjward,  lapis  InzuU,  a  blue  colour. So  called  from  the  mine*  of  Lojwurd,  where the  lapis  tozuU  was  found  (Marco  Pulo, ed.  Yule).
B,
Ic^.
M  &  fa^.  earliest  form  6a-
W..  '  ■■'  .  '  ■'tt  nnd  Com.  ^Hihapi, ifln  '  -  I  ■  '1  luin.  of  VV.  m^'fif.  a lad.  Ufd  itx^ii  rmx^,a  (on,  from  Eaily ifptf, «  aoa  JWiy*)-    Or  due  to  tnfaolile
Baboon.  (F.  or  Low  L.)  F.  hahou we  ftl&o  find  M,  E.  babion,  hafnan,  btt^' wine. ^  Law  L.  habfwynus.  a  baboon  (a.o. 1205).     Origin  uncert.iin.
Bacchanal.  (L.-Gk.)  \^.  Barchanitiis, a  wo'shipper  of  Bfuehus,  god  of  wine.— Gk.  nri«\'oi,  'laifx*".  K*>*'  of  wine-  —  Gk. laxity,  to  shout,  from  the  shouting  of  wor- shippers  at  the  fcsttval  of  /
==== leaf 47
ed,  jadeil micKKiV  <•  Icel biigr,aaeasy.biigr,^v>i.,. ,  ..<> to  hinder,  oppress.  Prob. V.bcJ7^,  to  mock. Bag.  (E.)  Put  for  ba/f  ME.  hi O.  Northomfarian  b^fic*  ^g>  Loke^  I 35.+Goth.  balgs,  a  wine-sLin:  G  htk skin  ;  Icel.  Ar^,  a  skin,  a  bog.  So  j GaeL  ha!gt  ^/f,  also  ^^,  a  liTithem  \ Lit.  'that  which  swells  out.'  CTNJ BALG.)    See  Bulse.  1
bagatelle,  a  tride,  a  ^me.  (F.««Iti Teut,^  K.A:^-v;;^.atriflc-ItaLi«^|i<( a  tiille,  diinin.  of  Parmesan  bAgaia^  a| property  ;  from  Lombard  A^o,  a  wfaiM of  Teut.  origin  ;  sec  Bag,  ba^*Be(l]
>M«gag«  (0,  luggage.  (F.-C.)  1 bagj^age^ bagage.  —  O.  r.  bagagt,  a  coUed of  bundles.  •■  O.  F.  bague,  a  bundle. Celtic  origin;  Bret,  beoi'k,  a  b batch,  a  burden ;  Gael,  bag,  ba/g,  a see  Bag.
baggage  h),  a  worthless  woman. C.)  Corrupted  fiom  O,  F.  bagaste,  ' gage,  quean/  CoU  Cf.  Ital.  ba, worthless  woman,  p.  Perhaps  or^a camp-follower,  ba;;gagt-woman:  fionQ bague,  a  bundle ;  see  Bagc^e  ( i  \.  y.; Mumy  makes  it  the  lamc  as  Bagcag«j in  a  dcpia^-ed  sense.  ,1
bellowa.  (E.)  M.  E.  b^U,  btfy.  Id a  bag.  but  used  in  the  Kj^ecial  sobJ '  bellows.'  Btllawj  u  the  pL  oi  M t07v,  a  bog,  also  another  form  of  Mh\ beity  is  another  form  of  bag.  Cf-  G,  I bal^,  a  *  blow  bag,*  a  pair  of  bellows;.
belly.  (E.)     M.  E.  My.    A.  S. est  form  b^Hg,  lit.  a  ba^.  4-Du. belly;    SwcJ.  bdlg,   belly,   oellows; baig,  busk,  belly ;  Gael.  bo!g^  bog,  bti
bilge.  (Scand.)     Pro[)Cily  the ran
```


## [2026-09-05T21:07:35.330Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"arsenal\" SKT.txt | head -5\necho \"--- FSD/WEB zircon arsenic\"\ngrep -n -i \"zargun\\|zargūn\\|zarkun\" FSD_vol4.txt WEB_vol1.txt LKT.txt 2>/dev/null | head -5\necho \"--- WEB arsenic\"\ngrep -n -i \"zarnikh\\|Pers. zar, gold\" WEB_vol1.txt | head -5"
}
```


### [2026-09-05T21:07:35.425Z] TOOL RESULT

```
985:M.  F.  srj,  trx.     A.S.  *«. -     rab.)   Span,  tfrima/. I.   arsenal ;    Iohj^ ;.-  jMj,  wliere  the  a- •     -ude.     Cf.  Itnl. .V.    —  ,\iab.  (/*ir  suu£ai, iction,  place  for  mfilfing •-  Amb    dtir,  a   house; tnde,  construction. .— GW,)    Late  L,  arsemmm. ic  ;  lit.  a  male  prin- ul  the  Ktrnii^c  lancy dlfTcretkl  Kxc9.~Gk, ;r,  A  male. Ard«nt.      * ■.  {vcs.  of  verb.  (E.)    See
23698:SfKUiisk  from  Arabic;  alguozll.  arsenal, bonito,  colaba^  ?,  caiaway  (carraway), cannine,  maravctli.  minaret,
--- FSD/WEB zircon arsenic
--- WEB arsenic
```


## [2026-09-05T21:07:44.398Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\npos=sum(len(l)+1 for l in lines[:984])\nprint('leaf', raw[:pos].count('\\f'), '-> printed', raw[:pos].count('\\f')-20)\nEOF"
}
```


### [2026-09-05T21:07:46.204Z] TOOL RESULT

```
leaf 39 -> printed 19
```


## [2026-09-05T21:07:59.961Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB\"; grep -n \"zist\\|zer 'Gold'\\|zarnī\\|zairita\\|zaranya\\|zāra\" HUB.txt | head -15\necho \"=== ARY zar/zesht\"; grep -n \"زشت\\|زرنیخ\\|زهره\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T21:08:00.026Z] TOOL RESULT

```
=== HUB
2407:zaranya- golden)? Der in der Note angefUhrte Name
2416:(= zd. "^zareta- fiir zairita-) zu setzen. Dazu arm.
5722:so bei gazista u. s. w. Verflucht* (Shk. 246, Min. Gl. 91,
5991:Vgl. syr. hUz, arm. Xuzastan, np. xuzistUn 'Susiana'.
7631:— zd. husravah-; Xuzistan = arm. Xuzastan, ap. (A)w2?ia-;
7662:-=^ np. Xuzistdn, syr. Tin, ap. {h)uvza'. Somit ist wohl x
7862:haftesten* = zd. x^'arezista- (siehe § 9), dazu x^altdan
8170:jycL-; zistan 'leben', zd. skr. jiv\ zahr (oben p. 71), arm.
8210:jasta- neben paz. gazista verflucht' (§ 52, 1); bar^jan =
8217:dozax *H5lle' = zd. daozanuha-; Xuzistan = ap. (H)uvja-
8248:Z. 4 ; Xuiastan 'Susiana' = np. Xuzistdn^ ap. (Hjuvia- ;
9262:senik' (= ap. *zarnii/a ftir zd. zaranya- *6old*) neben- 259 -
9291:vgl. zd. zaranya- *6old', zarana^a 'golden ; harr^ kar 'taub',
9311:phi. sup. balist := zd. barezista-; phi. sup. x^alist am
9312:schmackhaftesten' = zd. x^arezista- ^ vgl. np. x^alfdan
=== ARY zar/zesht
11555:گوتیکد (007710): داد پسگشت‌ها زشتدت ۲
12924:۶ کست (به چم "بد *زشت» قبیح»)
```


## [2026-09-05T21:08:06.275Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9250,9275p' HUB.txt\necho \"--- leaf of line 9262\"\npython3 - <<'EOF'\nraw=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\npos=sum(len(l)+1 for l in lines[:9261])\nprint('leaf', raw[:pos].count('\\f'), '-> printed', raw[:pos].count('\\f')-10)\nEOF\necho \"=== HUB 2400-2420\"; sed -n '2400,2420p' HUB.txt"
}
```


### [2026-09-05T21:08:08.008Z] TOOL RESULT

```
*Wolke* = zd. awra- u. s. w.
Np. r = skr. 7: risk *Nisse' = skr. liksa^, afgh. rica,
osset. l^sk; robah *Fuchs* = phi. ropas, skr. Wpdga-, gr.
dkainf]^, arm. aluBs ; supar Tflug* = skr. phala-, afgh. spara
Tflugschar*.
Lautgruppen mit r.
§ 156. Ap. rn bleibt als rn oder wird assimilirt zu
rr, das zu r vereinfacht werden kann.
a) rn bleibt in: burna, barnd *Jungling', zd. apere-
nCLyU", phi. apurndi, paz. awarnai Shk. 233 (neben pur
Voir = zd. perena-l); zarnt 'Auripigment* , arab. zamfq,
zarnfx, aber arm. zarik (Mos. Geogr.) *Auripigment, Ar-
senik' (= ap. *zarnii/a ftir zd. zaranya- *6old*) neben- 259 -
starn in zarnavtcxt 'xgixanrov Ezech. 16, 13 (eigentlich:
golddurchwebt' ?) , vgl. np. zarr 'Gold', zamn golden*
(= ap. *2arna', ^zamaina- fur zd. zarana^ci') -, suguma
= sugur *Stachel8chwein , zd. sukurena^ (var. stdcuruna-),
afg. skGn, sku^ = ^skurna-, phi. sukur H. 744 ; arab. pers.
xavarnaq („bourg a un demi-farsakh de Balkh^, Barbier
de Meynard, Diction, p. 215), Tab. 79, pers. x(a)varna bei
VuIIers, vgl. np. xurrah, zd. x^arenah- H. 808, oben p. 83.
b) rn wird zu rr = r in : parr *Feder, Fliiger, parri-
dan *fiiegen {parran *fiiegend' Fird. I, 440, 126), zd. parena-;
xurrah 'Glanz, Majestftt', zd. x^arenah- (oben p. 83), dazu arm.
tsuar (tsvar) 'elend, ungliicklich' = phi. ^duivarr^ *dusx^arr
= zd. dusx^arenah-; farr, farrah *Glanz, Majestat' = ap.
--- leaf of line 9262
leaf 268 -> printed 258
=== HUB 2400-2420
652. Die Etymologie ist falsch, da hm schon im Altpers. zu
m wird.
654. Neben »ar 'Gold' steht zarr wie neben zann golden':
zarrJn, danach ap. *zama' (zd. *zarena-) und ^zarnaina-
(zd. ^zarena^na- fiir vorliegendes zarana^na-) anzu-
setzen ? Vgl. zarnlx 'Auripigment*, arm. zarik Auripig-
ment = phi. "^zarrik aus "^zamik = zd. ^zarenya- (fiir
zaranya- golden)? Der in der Note angefUhrte Name
Zar(5r ist nicht mit Noldeke = Zapiaigtg zu setzen,
da der Name dieses armenischen K5nigs (nach Sand-
berger, DeZadriade Armeniae minoris rege prime,
Frankfurt 1840) auf einer Miinze Zadriades lautet,
wahrend der ZarSr des Yatk. i. Zar. und Fir du si's
sachlich und formell dem Zairivairi- des Avesta ent-
spricht.
656. N6ldeke hat Recht, np. zard gelb = ap. ^zarta-
(= zd. "^zareta- fiir zairita-) zu setzen. Dazu arm.
zartagoin (gelb-farbig') gelbe Blume zum Farben
dienend'.
657. Wo findet sich np. zurd, zurt 'Art Hirse? Arab. Surat
geh5rt nicht hierher.
```


## [2026-09-05T21:09:04.755Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\nfor ln in (2399,):\n    pos=sum(len(l)+1 for l in lines[:ln])\n    print('line',ln+1,'leaf', raw[:pos].count('\\f'), '-> printed', raw[:pos].count('\\f')-10)\nEOF"
}
```


### [2026-09-05T21:09:06.433Z] TOOL RESULT

```
line 2400 leaf 79 -> printed 69
```


## [2026-09-05T21:09:07.053Z] TOOL CALL #62: Bash

```json
{
 "command": "ls site/pages/185.jpg 2>/dev/null; pdftoppm -f 185 -l 185 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg185 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T21:09:09.464Z] TOOL RESULT

```
site/pages/185.jpg
total 25088
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:09 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51583 Sep  5 17:08 build173.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3536 Sep  5 17:04 jang.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53414 Sep  5 17:03 pg183.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79537 Sep  5 17:09 pg185.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72425 Sep  5 17:08 pg186.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


## [2026-09-05T21:09:12.942Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg185.png"
}
```


### [2026-09-05T21:09:13.336Z] TOOL RESULT

```

```


## [2026-09-05T21:09:13.334Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:09:49.723Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n 'https://www.etymonline.com/word/arsenic' \\\n 'https://www.etymonline.com/word/zircon' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D8%B4%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%86%D9%8A%D8%AE' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%AF' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 185, roots Gheis/Ghel: zesht, zar, zard, zarnikh, zahre, arsenic, zircon' 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T21:09:53.188Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0cf3e23ff5e8626b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/33235a6910a8d53c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35e371f16f0c88b6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e66c3d233bb40cad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c5ab7a560ed68ad3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f9f0aa5b93a0fb0e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd7c997dbbdae6ef.txt
```


## [2026-09-05T21:10:02.058Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-05T21:10:02.096Z] TOOL RESULT

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


## [2026-09-05T21:10:19.336Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 gheis\"; grep -n -i \"gheis\\|zaesa\\|zoizd\\|gaista\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"=== WLD Bd1 ghel gold\"; grep -n \"zaranya\\|zairita\\|zara-.*Galle\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-05T21:10:19.414Z] TOOL RESULT

```
=== WLD Bd1 gheis
49851:„hindern“. Schwerlich hierher aber dt. Geisel usw., s. u. gheis- „biirgen“.
49893: schat't“ (aber iiber ahd. gisal „Geisel = Burgschaftsgefangener“ s. u. gheis
51893:l   = d zu hedale „argert sich“ (s. gheis- ,,aufgebracht“) zu gehoren (Mittel-
51971:  gheis       isl. gisinn „vor Trockenheit rissig, undicht" (Ptc. von *gtsa =)
52111:                                                   gheidh-   — gheis-, gheiz-d-                                        553
52147:usw.       s.   u. gheis-        ,burgen“.
52177:1.     gheis- und gheiz-d- „aufgebracht, bestiirzt, erschreckt (sein)“. Nach
52191:554                                                                             gheis-
52237:oder langdiphthongischen Wzansatz gheis- (: ghdis -, ghis-) fordern.       Die
52243:2.     gheis- „burgen, Pfand -t                          ,
=== WLD Bd1 ghel gold
59403:   Ay. zaray- „gelb, gelblich, goldfarben“, zairVa „gelb, fahlgelb", zaranya-
```


## [2026-09-05T21:10:20.733Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB\"; grep -n \"zišt\\|zi§t\\|zahr\\|zarr\\|zargōn\\|zarnīk\" NYB_vol2_glossary.txt | head -15\necho \"=== IEC ghel gold\"; grep -n \"zaranya\" IEC.txt | head -5\necho \"=== SYN gall\"; grep -n -i \"gall\\b\" SYN.txt | head -8"
}
```


### [2026-09-05T21:10:20.808Z] TOOL RESULT

```
=== NYB
809:aviš [?wbš] adv. l. used instead of the prep. 6 if it refers back to an encl. pron. in the beginning of the sentence: zahr i-š ~ fréstit the poison that was sent to her 918; kū-t... ~ ne rasét lest ... shall come upon thee 688-?; api-§ ... ~ barét bring for him! 7489 = bé-§ ~ barét 76’; puhr i-Š ... ~ mat the punishment that has come upon him 741^; cigón ka-šan... ~ hilénd as if one poured ... upon them 101291, — 2. as a substitute for the prep. 6 + the encl. pron. 3d p. sg. -&: 14-16, 413.15, 727, ete. passim; taking up the rel. pron. 4226, 7213 v.s. v. ke. — Ps. ’wbsy; MPrs ’wys, from an OP adv. *abišā or *abisah derived from Av. (87 sg.) adbi, aiwi = OP abiy, as patiš (q. v.) from pati (cf also haciš : hac). I maintain my opinion expressed in HP II, 212; a
903:bālist [b'lyst', b'lst'] 1. the highest, sup. of buland (g. v.) 389. — 2. subst. top 4015; zenith 9612, 9810, 9911; culmination point (of a star) 510, — MPrs b’ryst; < OP *bar- dista-, SW form of Av. (950) sup. barə- zišta-.
1287:distak [dystk'] *treated, manipulated, or the like: pat Hēšm zahr ~ "treated with (the demon) Wrath's poison 2516-17 = 2814, — In the edition the first letter is a marked d, hence the reading dystk' is cogent. Because of -ist- this must be a SW form corresponding to a NW form with -i$t-, but its meaning in this context make it impossible to combine it with NW dištan (v. next w.): a weapon is not “built” or “‘formed’’. It would be tempt- ing to connect it with Skr dih- ‘to daub, to smear', but the corresponding Av. (673) dačz- has other significations (cf diz), and the Phl. renderings of it (Vd 39.13.18, 733. 1536) have run wild and are no more recognizable (they can scarcely be brought together with dés-, v. the next w.).
1341:drayäp [dly’p'] the sea 621. 211, 1131, — SW form of Av. (1701 sq.) zrayah (v. zrah, zrài): OP drayah- -+ dp; the com- pound was guite clear to those who created the Aram. expression used later as ideogr. (FrP 3): YMYMY^, i. e. yammé mayyä ‘seas of water’, a purely mechan- ical transposition of dray(ah)-āp ‘sea- waters’. MPrs dry’b (A-H I); Paz. daryäv; Ps. has the bizarre spelling dlyw*w (cf s. v. niyandar); NP daryä.
1791:compounds, v. separately. — 2. joint, all together, whole: mok % ~ zarrén shoes all golden 294; pat ~ späh in a body 209-10; tö ~ yātūk you are a thorough wizard 2277; all those together (who) 10671; —-ic all 108%; 6 ~ together, pas- sim; — secondarily used as a prev.: ~- butan, —-bavišneh, ~-x"arisnéh, —-pur- sitan, ~ nipistan, to be distinguished from the old prev. ham-, which always appears as han- before a consonant. — Av. OP (1773) hama-. — My emendation PYK-t 2625 is not justified; probably the reading of the MSS is correct: ’YK-m = kü-am for kü ham.
1975:hazar [LP, with a P resembling the OAram. and Palmyr. forms of it; for Aram ’LP] thousand, — Av. (1796) hazagra- < *ha- zahra-, Skr sahasra-.
2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
2781:Nizišt [nzyšt'] n. pr. of a dev 721, — Paz. Nizist, Nīž(t)št.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3083:pat-sén [PWN syn'] breast bodice 5718, — DkM 63514-15: apar-ic 6 tē, Zartuxst, druž bē dvārēt mätak-karp, zarren-patsen (ku pistin-pin dārēt), v. pistan. — FrP 31 sénak, NP sinah ‘bosom, breast’.
3483:spas [sp’s] 1. thanks, gratitude 127%. 7026. 90°, — 2. service: vasdn vazurg ~-dn (cas. obl. as a subj.) many men serving in high positions (bahuvrihi) 1061; v. also šnās. — MPrth 'sp's ‘service’, Arm. lw. spas id.; MPrs ‘sp’s ‘service’ (S), ’sp’s ‘thanks’ (A-H II); Paz. spas with the bizarre Skr. v. tridhä-praharaka ‘threefold watch’ based on a popular etymology (sé ‘three’ + pds, g. v.); NP sipäs 1. ‘grace, favour’, 2. ‘praise, thanksgiving’; from Av. (1614) spas- ‘to observe, to attend’. — V. an-ispäs.
3716:tan ... paristém adak-tān dahém ... vas zarr ... 193-4; u api-tin ... kar framā- yēm 198; täi-tän man zīvišn + gētē pat miyān kunom 67-5; agent: ka-tän pursīt hat 214; kū-tān... dit ...? 39%; vinäs t-tān kart éstét 67°; referred to by a follow- ing prep.-adv.: āfrīn-tān + xvatāi apāk the benediction of the Lord (be) with you 1281-19; — independent form atän 451,
4006:~ zarr,
4269:embarrassment in dealing with these terms. The translator of Vd. 8%, who quite correctly felt that vačpyo is a pass., borrowed the Av. vb. (1322 sg.) vaēp- (otherwise not attested in Milr as far as I know) and formed from it the pass. pt. viftak, then, likewise correctly interpret- ing vaepayö (vačpayant-) as an act., form- ed from viftak the caus. vb. viftén-, but, by assimilating it formally to viftak: vifténitak, created a bizarre mixture of act. and pass. The same curious contra- diction is found in DD, purs. 719-7 which is, however, closer to the Av. original: viftak and vépénitak. Our passage 82° has chosen a mitigating vb. ‘to seduce’, *vr- dip-: MPrth pres. wdyfs- ‘to be cheated’, wdybyšn ‘error, aberration’, wdyb-gr ‘im- postor’, wdyftgyft ‘deceit’, Ghilain 81 sg.; Arm. lw. vrép < *vidép ‘oblique, pervert- ed; fault, error, depravation’; MPrs pres. wyyb- (viyéb- < "videp-), also contracted wyb-, pass. wyfs-, pt. wyft(g), abstr. wyyftgyh = viyiftageh (also wyf-), wdyb *deecit certainly borrowed from NW ; v. Verbum 173. 198; Ps. wydyptk’n "those who have gone astray’. BP wdypt >
4476:zahr [z’hl] poison 919-?!, 103. 2516, 2814, 76°. — MPrth jhr; Arm. lw. Zahr; MPrs zhr (A-H I); NP zakr; < *ja@ra- ‘means for killing’, v.s. v. zatan (because of -hr Prs zahr must have been borrowed from NW).
=== IEC ghel gold
=== SYN gall
757:3. Ir. domun, NIr. domhan, ‘world’ in sense a and b, fr. *dub-no- (cf. Gall. Dub- noreiz on coins, Dumnortz in Caesar, lit. ‘world-king’) : ChSl. dino (n from bn) ‘bottom, foundation’, Ir. domain, NI. domhain ‘deep’, NE deep, etc. The development was from ‘bottom, founda- tion’ to ‘earth’ (as in Rum. pamint ‘earth’ fr. Lat. pavimentum), then ex- tended to ‘world’. Walde-P. 2.847 ff. Pedersen 1.35.
758:W. byd, Br. bed, OCorn. bit, MCorn. bys used for world in all senses, Ir. bith ‘age’, also ‘world’ in senses b and e, fr. a Celtic *bi-tu- (cf. Gall. Bitu-riges) : Grk. ios ‘life’, Lat. vivus, Skt. jiva- ‘liv- ing’, etc. (4.74). Pedersen 1.41.
1035:3. Gall. -magus in Arganto-magus, etc., Ir. mag, NIr. magh, W. maes, Br. maez, prob. as orig. ‘expanse’ : Lat. magnus, Skt. mah-, etc. ‘large, great’ (12.55), Skt. mahi- ‘earth’. Pedersen 1.96. Stokes 198f. Walde-P. 2.258 (ad- versely).
1417:W. nant ‘brook’ also ‘valley, gorge, OBr. nant ‘gorge, brook’, Gall. nanto ‘valley’, fr. IE *nem- ‘bend’, Skt. nam-, ete. Walde-P. 2.302. Stokes 192. Otherwise (: Grk. voun ‘pasturage’, etc.) Benveniste, BSL 32.85. In either case, ‘brook’ fr. ‘valley’.
3882:4. ON gelda, Dan. gilde, Sw. galla, ME gelde (from ON), NE geld (formerly sometimes also used of females), lit. ‘make imperfect’ : ON geldr, Sw. gall, OHG galt ‘barren, giving no milk’, out-
4132:3.21. ‘Bull’. 1. Grk. radpos; Lat. taw- rus (>It., Sp. toro, Rum. taur, OF'r. tor, Fr. faureau), Osc. ravpoz, Umbr. toru; Gall. tarvos, Ir. tarb, NIr. tarbh, W. tarw, Br. taro (Celtic forms with cons. transposition); ON Ajorr, Dan. tyr, Sw. tjur (these influenced by the group ON stjorr, ete.) : OPruss. tauris, Lith. tauras ‘wild ox’, ChSI. turii ‘wild ox’(?). Perh. IE *tau-ro- fr. *téu- ‘swell, be strong’ in Skt. taut, taviti ‘is strong’, etc. (so Walde-P. 1.711, Brugmann, Grd. 2.1.353), but more prob. to be combined with OF stéor, etc. Ernout-M. 1018. Falk-Torp 1309. Feist 454.
4528:some unexplained phonetic features and taken as an Illyr. loanword by Kretsch- mer, Glotta 22.120); Lat. equus (with fem. equa ‘mare’); Ir. ech, Gall. *epo- in names Eporedia, etc. (W. ebol, Br. ebeul ‘colt?); ON jor (poet.), OK eoh ‘war- horse’ (Goth. aihwa-tundi ‘bramble bush’, lit. ‘horse-tooth’); Lith. (obs.) esva, asva ‘mare’; Skt. agva-, Av., OPers.
4630:W. ebol, Br. ebeul : Gall. *epo-, Lat. equus ‘horse’ (3.41).
```


## [2026-09-05T21:10:38.209Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"zahr[a-zë]*\\s*\\[[^]]*\\][^.]\\{0,80\\}\" PHD.txt | head -10\necho \"--- WLD page of line 59403\"\npython3 - <<'EOF'\nraw=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\nprint(lines[59390:59415])\nEOF"
}
```


### [2026-09-05T21:10:40.147Z] TOOL RESULT

```
538:zahr [p’tzhl | N pa(d)zahr] bezoar, antidote
673:zahr [zh] | M zhr, N ~] poison, venom
673:zahrag [z()Alk! | N ~a] bile, gall
--- WLD page of line 59403
['                                      denen Palatal und Yelar nicht zu             in', 'scheiden            ist,      die Sippe         gefunden hat, wird ghel-', '                                                             die      reichate Entfaltung', 'und ghel- hier zusammen behandelt. Abzuweisen ist Perssons (Beitr. 790)', 'Ansicht, dafi in ghel- Entlehnung aus einer Centum-Sprache vorliege.', '                                                                         11', '     Ai. hdri „blond, gelb, goldgelb, griingelb, falb“, harinah „ Gazelle ,                                                                                               Jiarit', '', '„falb“, hdrita „gelb, griin“,                                         Mranya n. „Gold, Geld“, hiranyaya „golden,', 'goldig“; auch h at aka n. „Gold“? (s. Petersson Studien zu Fortunatovs', 'Regel 5, 8, 91 mit Lit.); dazu auf velarer Wurzel beruhend ai. ghota „Pferd“', 'als ursprgl. „Fuchs“? (Sommer IF. 31, 364 u. A. 3).', '   Ay. zaray- „gelb, gelblich, goldfarben“, zairVa „gelb, fahlgelb", zaranya-', '    „Gold u earanaena „yon Gold, golden', '                                                                                                          11', 'n.                      ,', '                                                  zara m. „Galle“ (nach Bartho-                                ,', '', '', 'lomae Airan. Wb. 1690 < *ghehl wie lat. fell), nach der Farbe benannt', 'wie gr -/o?.°s, lat .fel, an. gall usf. mit velarem Wurzelanlaut gsrddoksrata', '           .', '                                                                                  ;', '', '']
```


## [2026-09-05T21:10:51.539Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nraw=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\n# find nearest standalone 3-digit numbers before line 59403\nfor i in range(59403,59340,-1):\n    if re.fullmatch(r'\\s*\\d{3}\\s*', lines[i] or ''):\n        print('page marker',lines[i].strip(),'at line',i+1); break\nfor i in range(59403,59470):\n    if re.fullmatch(r'\\s*\\d{3}\\s*', lines[i] or ''):\n        print('next page marker',lines[i].strip(),'at line',i+1); break\n# also for gheis 52177\nfor i in range(52177,52100,-1):\n    if re.search(r'\\b55[0-9]\\b', lines[i] or ''):\n        print('gheis page ctx:', lines[i].strip()[:120]); break\nEOF"
}
```


### [2026-09-05T21:10:53.209Z] TOOL RESULT

```
gheis page ctx: gheidh-   — gheis-, gheiz-d-                                        553
```


## [2026-09-05T21:10:57.861Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=raw.split('\\n')\nfor i in range(59340,59440):\n    l=lines[i]\n    if 'ghel' in l and any(c.isdigit() for c in l):\n        print(i+1, l.strip()[:140])\nEOF"
}
```


### [2026-09-05T21:11:00.182Z] TOOL RESULT

```
59367 624                                          ghel-          (gliel->.          ghele-          :   ghle-, ghlo- : ghla-
59385 besser auf *ghlan-, Wz. ghel-, zuriickzufiihren (Persson Beitr. 791).
59394 und ghel- hier zusammen behandelt. Abzuweisen ist Perssons (Beitr. 790)
```


## [2026-09-05T21:11:34.892Z] AGENT

Now I'll write the verification file.


## [2026-09-05T21:11:37.311Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg185.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/185.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/185.png"
}
```


### [2026-09-05T21:11:37.379Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79537 Sep  5 17:11 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/185.png
```


## [2026-09-05T21:11:37.907Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)


## [2026-09-06T02:13:04.973Z] INPUT

The coordinator sent a message while you were working:
You were cut off by a rate limit just as you were about to write /home/sfmqrb/git/rishe/data/verification/page-185.json. Please continue from where you stopped: write the file following AGENT_INSTRUCTIONS.md, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 185` (fix any PROBLEM lines), and reply with the short summary described in the instructions.

Address this before completing your current task.


## [2026-09-06T02:21:52.707Z] TOOL CALL #72: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-185.json",
 "content": "{\n  \"pdf_page\": 185,\n  \"book_page\": 155,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gheis, Gheizd\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰeys- / d-extension *ǵʰeysd- 'to be shocked, frightened, agitated; anger'\",\n      \"note\": \"Both the root name (two headwords, Gheis and Gheizd), the language label and the gloss are Pokorny's own. Pokorny p.427 heads the lemma 'gheis- und gheiz-d- „aufgebracht, bestürzt, erschreckt (sein)“', and Klein 1971 s.v. ghost writes 'fr. I.-E. base *gheizd-, „to frighten; to be angry“' — which is Nourai's gloss word for word, so his KLN:655 is where the wording comes from. Watkins (AHD appendix) has 'gheis-. Used of the emotion of fear or amazement ... Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost ... [Pok. gheis- 427]', which supplies both his Germanic box and its AHD citation. The whole chart is therefore a faithful abridgement of Pokorny 427 + Klein 655; the one form that no source knows is the Avestan 'zaěšta' of node #1. Wiktionary's Persian زشت page reconstructs the same tree independently (PIE *ǵʰeysd- > PII *ȷ́ʰáyždas > Av. zaēša- > MP zišt > NP zešt, cognate with PGmc *gaistaz).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ǵʰeys- و گونهٔ گسترش‌یافتهٔ آن *ǵʰeysd- به معنای «ترساندن، هراسان و آشفته شدن، خشمگین بودن» است. پوکورنی در صفحهٔ ۴۲۷ همین دو صورت را زیر یک ماده آورده («gheis- und gheiz-d-») و والده‑پوکورنی نیز در جلد یکم صفحهٔ ۵۵۳ همین را تکرار کرده است؛ کلاین در فرهنگ ریشه‌شناسی انگلیسی ذیل ghost عیناً می‌نویسد I.-E. base *gheizd- «ترساندن؛ خشمگین بودن»، که همان تعریف نورایی است. پس نام ریشه، برچسب زبانی و معنای آن هر سه درست است. تنها لغزش کوچک، صورت اوستایی zaěšta در خانهٔ ۱ است که در بارتولومه و پوکورنی سابقه ندارد. ویکی‌واژه هم همین زنجیره را مستقلاً می‌آورد: هندواروپایی *ǵʰeysd- ← هندوایرانی *ȷ́ʰáyždas ← اوستایی zaēša- ← فارسی میانه zišt ← «زشت».\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B2%D8%B4%D8%AA\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:427\",\n          \"status\": \"supports\",\n          \"note\": \"Pokorny IEW p.427 (local POK_02.txt leaf 83; POK_full.txt lines 32611-32653, 'Page(s): 427'): 'gheis- und gheiz-d- „aufgebracht, bestürzt, erschreckt (sein)“; gheizdho-s „Erregtheit“'. Nourai's root name and gloss are this lemma.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p. 553-554\",\n          \"stance\": \"supports\",\n          \"note\": \"Walde-Pokorny I 553 (incoming/WLD/WLD_Bd1_pages.txt line 52177, running head 'gheidh- — gheis-, gheiz-d- 553'): '1. gheis- und gheiz-d- „aufgebracht, bestürzt, erschreckt (sein)“' — Pokorny 427 is the reprint of this article.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins, IE appendix s.v. gheis-\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt line 510: 'gheis-. Used of the emotion of fear or amazement (original part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost ... [Pok. gheis- 427.]'\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"s.v. ghost (1971 ed., KLN_1971.txt line 102354)\",\n          \"stance\": \"supports\",\n          \"note\": \"'fr. I.-E. base *gheizd-, „to frighten; to be angry“ ... Base *gheizd is a -d-enlargement of base *gheis-.'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, searched for gheizd-/ghoizdo-/gaisto-\",\n          \"stance\": \"silent\",\n          \"note\": \"grep 'gheizd|ghoizdo|gaisto' in IEC.txt returns nothing; Mann has no entry for this root under those spellings.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"zaěša, zaěšta; zôišnu; zôižd-išta\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four forms are exactly Pokorny's and Bartholomae's. Av. zaēša- 'schauderhaft, gruesome' (Bartholomae, AiW col. 1691, attested Frahang 20) continues *ǵʰeys-o-, with Proto-Iranian *ȷ́ʰ- > z- (the regular Iranian outcome of the PIE palatal *ǵʰ, as in Av. zan- 'know' : Lat. cognoscere). zōišnav- 'zusammenschreckend, schaudernd, bebend (vor Frost)' (AiW cols. 1693-94) is a -nu- adjective on the reduplicated/o-grade stem, and zōiždišta- 'der schauderhaftest, abscheulichste' (AiW col. 1694, Yt. 21.1, V. 7.2) is the superlative of a lost verb *zōižda- 'make shudder', i.e. the *ǵʰeysd- extension with the superlative suffix -išta- (hence Nourai's cross-reference ☞Isto to his root for the superlative suffix). The one form no source knows is 'zaěšta': Bartholomae has no zaēšta-, and neither Pokorny 427 nor Klein 655 (Nourai's own two references here) list it — it looks like a doublet of zaēša- or a contamination with zōiždišta-. The printed page (pdf 185) really does read 'zaěša, zaěšta', so the extraction is faithful and the extra form is the book's.\",\n          \"derivation_fa\": \"سه صورت از چهار صورت این خانه دقیقاً همان است که بارتولومه و پوکورنی آورده‌اند. اوستایی zaēša- «هول‌انگیز، زشت» (بارتولومه، ستون ۱۶۹۱، از فرهنگ اویم) بازماندهٔ *ǵʰeys-o- است؛ «غ»/*ǵʰ کامی هندواروپایی در ایرانی باستان به z بدل می‌شود (همان دگرگونی که در zan- «دانستن» دیده می‌شود). zōišnav- «لرزان، ترسان (از سرما)» (ستون‌های ۱۶۹۳–۹۴) صفتی است با پسوند -nu-، و zōiždišta- «نفرت‌انگیزترین» (ستون ۱۶۹۴، یشت ۲۱٫۱ و وندیداد ۷٫۲) صیغهٔ عالی از فعلی گمشده *zōižda- «لرزاندن» است، یعنی همان گسترش *ǵʰeysd- با پسوند عالی -išta- (ارجاع نورایی به ریشهٔ Isto نیز به همین پسوند است). تنها صورت بی‌سند zaěšta است که نه در بارتولومه هست و نه در پوکورنی و کلاین؛ تصویر صفحهٔ چاپی نشان می‌دهد خودِ کتاب چنین آورده، پس خطا از خوانش اسکن نیست بلکه از کتاب است. در مجموع ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B4%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:427\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt leaf 83: 'Av. zaesa- „schauderhaft“, zöisnu- „zusammenschreckend, schaudernd, bebend (vor Frost)“, züizdistö „der schauderhafteste, abscheulichste“ (Superl. zu einem Verbum *zöizdä- „schaudern machen“)'. No zaēšta-.\"\n            },\n            {\n              \"ref\": \"KLN:655\",\n              \"status\": \"supports\",\n              \"note\": \"Klein s.v. ghost (KLN_1971.txt line 102354): 'whence also OI. hedati ..., Avestic zoizdishta-, „the most abominable“. Base *gheizd is a -d-enlargement of base *gheis-, whence Avestic zaesha-, „horrible“, zoishnu „shuddering“.' Nourai's three glosses ('terrible/ugly', 'shuddering', 'most abominable') are Klein's. No zaēšta- here either.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols. 1691, 1693-1694\",\n              \"stance\": \"partial\",\n              \"note\": \"BRT.txt: 'j. zaeša- Adj. „schauderhaft“: F. 20. S. auch zōišnav-, zōiždišta-; — Vgl. mp. (Pü.), np. زشت „schauderhaft“'; 'j. zōišnav-, g. zōišənav- Adj. „zusammenschreckend, schaudernd, bebend“, vor Frost'; 'j. zōiždišta- Adj. „der schauderhafteste, abscheulichste“, von den xrafstra-: Yt.21.1 ... Superl. zu einem V. *zōižda-'. Bartholomae has no zaēšta-, so 'partial'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 553\",\n              \"stance\": \"supports\",\n              \"note\": \"Same Avestan material as Pokorny 427, with the reference 'WP. I 553 f.' printed at the foot of Pokorny's article.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"zešt «زشت»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP زشت zešt 'ugly' goes back through Middle Persian zišt [zyšt'] 'hateful, ugly' (MacKenzie, CPD, s.v. zišt, with Manichaean and New Persian equivalents noted) to the Avestan superlative material of node #1; Bartholomae states the equation himself under zaēša-: 'Vgl. mp. (Pü.), np. زشت „schauderhaft“'. The Middle Persian ī is the regular contraction of Old Iranian *ai/*ay before the cluster -št- (Av. zōiždišta- / *zaišta- > MP zišt), and MP i in an open syllable is lowered to e in New Persian (MP zišt > NP zešt), exactly as MP dil > NP del. Wiktionary treats MP zišt as an Avestan loan into Middle Persian rather than a direct inheritance — a nuance, not a different origin. Horn's own paragraph (no. 662, p.147) instead compared Av. jīstayamna- 'verachtend', but Mo'in's footnote in the Borhān (the other reference Nourai cites) and Bartholomae both give the zaēša-/zōiždišta- etymology, which is the modern view.\",\n          \"derivation_fa\": \"«زشت» فارسی نو از فارسی میانهٔ zišt (نوشتهٔ zyšt') به معنای «نفرت‌انگیز، زشت» است — مکنزی در فرهنگ کوچک پهلوی همین را آورده — و آن از همان مادهٔ اوستایی خانهٔ پیشین می‌آید؛ بارتولومه خود ذیل zaēša- می‌نویسد «مقایسه کنید با پهلوی و فارسی نو زشت». دوگانه‌واکهٔ ایرانی باستان ai پیش از خوشهٔ -št- در فارسی میانه به ī بدل شده (zōiždišta-/*zaišta- ← zišt) و کسرهٔ فارسی میانه در فارسی نو به «ـِ» گراییده است (zišt ← zešt)، درست مانند dil ← دل. هرن در شمارهٔ ۶۶۲ صفحهٔ ۱۴۷ آن را با اوستایی jīstayamna- «خوارشمارنده» سنجیده بود، ولی حاشیهٔ معین بر برهان قاطع و بارتولومه هر دو ریشهٔ zaēša-/zōiždišta- را می‌دهند و همین دیدگاه امروزی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B4%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1021\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān-e Qāṭeʿ, Moʿin's edition; the زشت article with Moʿin's footnote sits on the leaf that this OCR places at printed p.1023 (BQT_v2_pages.txt leaf 483, printed = leaf + 540, ±2), i.e. Nourai's 1021 within the known offset drift. The footnote reads: '۱ - پهلوی zist ، اوس... (خوف، تفرآور) «بارتولمه ۱۵۹۱» - ... zoizdista- (مکروه، منفور) «بارتولمه ۱۶۹۳»' — Pahlavi zišt, Avestan (fear-inspiring), Bartholomae, and zōiždišta- 'abhorrent, detested' at Bartholomae col. 1693, which is exactly the column where I found the word.\"\n            },\n            {\n              \"ref\": \"HRN:147\",\n              \"status\": \"partial\",\n              \"note\": \"Horn, Grundriss p.147 (HRN.txt leaf 168) no. 662 is indeed 'zist „schlecht, schimpflich“, zistūr' — the right page and the right word — but Horn's etymology is different: 'aw. jīstayamna- (y. 8, 3) „verachtend, verspottend“ (Geldner); phlv. zist „hässlich“ (Men.)'. He confirms the Pahlavi zišt but not the zaēša-/zōiždišta- link.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD s.v. zišt (PHD.txt leaf with z- entries)\",\n              \"stance\": \"supports\",\n              \"note\": \"'zišt [zyst! | = P, N ~] hateful, ugly' — Pahlavi, Parthian and New Persian identical, so the NP form is inherited, not borrowed from Arabic.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'zist' in HUB.txt turns up only gazista/barəzišta-type superlatives; Hübschmann has no note on Horn no. 662.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1691 s.v. zaēša-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Vgl. mp. (Pü.), np. زشت „schauderhaft“' — Bartholomae himself draws the Avestan → New Persian line Nourai draws.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"žyšt\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian zyšt- / (Manichaean) jyst 'ugly, hateful, hated' is the East-Iranian cognate of MP zišt, from the same *ǵʰeysd- material: Gharib's dictionary derives it in so many words from *zaiš-/*zōiždišta-. Nourai's ž- is a transliteration variant (Gharib reads the Sogdian and Christian-script spellings as z-, the Manichaean j- spelling being the affricate/fricative alternation normal in Sogdian orthography). The word is quoted from the Christian Sogdian texts (C2) and the Sūtra of the Causes and Effects (SCE 301).\",\n          \"derivation_fa\": \"واژهٔ سغدی zyšt- (در خط مانوی jyst) به معنای «زشت، منفور» هم‌ریشهٔ فارسی میانهٔ zišt است و از همان مادهٔ *ǵʰeysd- می‌آید؛ غریب (قریب) در فرهنگ سغدی خود ریشهٔ آن را صریحاً «*zais؛ اوستایی zōišnu، zōiždišta؛ پارتی zys-» می‌نویسد. صورت žyšt نزد نورایی تنها گونه‌ای از آوانویسی است؛ غریب آن را zišt می‌خواند و اختلاف z/ž و j در خط‌های سغدی، مسیحی و مانوی معمول است. شاهدها از متون سغدی مسیحی (C2) و سوترهٔ علت و معلول است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:472\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian Dictionary, printed p.472 (SOD_pages.txt leaf 539, which carries the running number 472), entry 11589: 'zyst- C — zist (zyst-) ©<*zais; Av. zōišnu; zōiždista; Parth. zys- => zyst-, jyst, zystʾy — ugly, hateful, hated'. Entry 11588 'zyst- B ... ugly, hateful, SCE 301' is on the same page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"entry 4613 (Manichaean jyst), printed p. ~183\",\n              \"stance\": \"supports\",\n              \"note\": \"SOD_pages.txt leaf 249: '4613 jyst M — zist ©<*zoisdista; *zais—y Parth. zys- =>zyst-' — the Manichaean-script doublet, with the same etymology.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols. 1691, 1694\",\n              \"stance\": \"supports\",\n              \"note\": \"The Avestan bases (zaēša-, zōiždišta-) that Gharib cites are Bartholomae's, quoted above.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"gaistaz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *gaistaz 'ghost, spirit' is the suffixed o-grade *ǵʰoys-do- of the same root, i.e. the western sibling of Av. zōiždišta-: PIE *ǵʰoysd-o- > PGmc *gaista-z by Grimm's law (*ǵʰ > *g) and the regular *oy > *ai. It is directly attested in OHG geist, OS gēst, OE gāst 'spirit, ghost', with the causative denominative *gaistjan in OE gǣstan 'to frighten' (whence aghast, ghastly). The semantic bridge 'terror, agitation' → 'spirit' is Pokorny's and Watkins's; the exact Sanskrit correspondent héḍa- 'anger' shows the same *-d- stem.\",\n          \"derivation_fa\": \"ژرمنی آغازین *gaistaz «روح، شبح» صورت o-گرادِ پسوندداری از همین ریشه است، یعنی *ǵʰoysd-o-، و از این رو خواهرِ غربیِ zōiždišta- اوستایی به شمار می‌رود: بنا بر قانون گریم *ǵʰ به g و دوگانه‌واکهٔ *oy به ai بدل شده است. صورت‌های تاریخی آن آلمانی علیای کهن geist، ساکسونی کهن gēst و انگلیسی کهن gāst «روح» است و فعل مشتق *gaistjan در انگلیسی کهن gǣstan «ترساندن» (سرچشمهٔ aghast و ghastly). تحول معنایی از «آشفتگی و هراس» به «روح» را پوکورنی و واتکینز هر دو پذیرفته‌اند و سنسکریت héḍa- «خشم» همان ستاک -d- را نشان می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins, IE appendix (AHD_watkins1985.txt line 510): 'gheis- ... Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gāst, ghost: GHOST; AGHAST; b. Old High German geist, ghost: POLTERGEIST; c. Germanic denominative *gaistjan in Old English gǣstan, to scare: GAST. [Pok. gheis- 427.]' — Nourai's form 'gaistaz' and gloss 'a ghost' are copied verbatim from this line.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 427-428\",\n              \"stance\": \"supports\",\n              \"note\": \"POK_02.txt leaves 83-84: after 'Wurzelform gheiz-dh-: ai. hed- „zürne“' comes 'ahd. geist (= ai. hēda-) m., as. gēst, ags. gāst (gǣst) m. „Geist ...“ (so bes. engl. ghost „Gespenst“), ags. gǣstan (*gaistjan) „erschrecken“'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. ghost\",\n              \"stance\": \"supports\",\n              \"note\": \"'rel. to OS. gēst, OFris. jēst, gāst, MDu. gheest, Du. geest, OHG., MHG., G. geist „spirit, ghost“, OE. gǣstan „to frighten, alarm“, fr. I.-E. base *gheizd-.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"ghost\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE gāst 'breath, spirit, soul, life; supernatural being' > ME gast, gost > NE ghost, the Old English long ā giving ME/ModE ō (as in stān > stone). The parasitic gh- spelling is not native: it was introduced by Caxton and his Flemish compositors in the 1470s on the model of Middle Dutch gheest, and only that spelling separates the word visually from its cognates. Sense-wise English kept the 'spirit/soul' value (Holy Ghost) and developed 'apparition of a dead person' in the late Middle Ages; the older 'fear' sense of the root survives in the doublets aghast and ghastly, both from the same OE gǣstan.\",\n          \"derivation_fa\": \"انگلیسی کهن gāst «دم، جان، روح؛ موجود فراطبیعی» در انگلیسی میانه به gast و gost و سپس به ghost رسیده است؛ «آ»ی کشیدهٔ انگلیسی کهن در انگلیسی میانه به «ō» بدل شده (مانند stān ← stone). املای gh- بومی نیست و در دههٔ ۱۴۷۰ به دست کاکستون و حروف‌چینان فلاندری او به قیاس هلندی میانهٔ gheest وارد شد. معنای «روح» در ترکیب Holy Ghost «روح‌القدس» بازمانده و معنای «شبح» در پایان سده‌های میانه پدید آمده است؛ معنای کهن «ترس» در دو واژهٔ هم‌ریشهٔ aghast و ghastly (هر دو از gǣstan انگلیسی کهن) باقی مانده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai cites no reference on this node; the parent Germanic box carries AHD, which lists GHOST under gheis-.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. ghost (KLN_1971.txt line 102354)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ghost, n. — ME. gast, gost, fr. OE. gāst, „breath, spirit, soul, life“ ... Cp. aghast, ghastly. Cp. also the second element in Zeitgeist.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"s.v. Ghost (SKT.txt line 7553)\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat has a GHOST headword in the Concise; the OCR of the entry body is unreadable, but the headword confirms the standard OE gāst derivation is the one on offer.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"index of English words\",\n              \"stance\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 1560: 'GHOST gheis-'; line 1218: 'AGHAST gheis-'.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Ghel\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰel- / *ǵʰelh₃- 'to shine; yellow, green, gold'\",\n      \"note\": \"Pokorny's lemma at p.429 is 'ghel-1 (und ghel-1), also as i-, u- or n-stem; ghelə- : ghlē-, ghlō- : ghlā-, Meaning: to shine; green, gold, blue, yellow, moon', which is Nourai's 'to shine, also a bright yellow color' with his page number, and Walde-Pokorny I 624 is the same article. Modern reconstructions write the root *ǵʰelh₃-. The whole Iranian side of the chart is Pokorny's own paragraph on p.429: 'Avestan zari- „yellow, yellowish, golden“, zairita- „yellow, pale-yellow“, zaranya-, Old pers. daraniya- n. „gold“, zaranaena „from gold, golden“, zara- m. „gall“ (= gr. χολή), named after the color as gr. χόλος, Latin fel, Old Norse gall'. That single sentence underwrites nodes #1, #14 and #15 at once. Two things need correcting. (1) Node #8: Greek arsenikón cannot come from Arabic az-zarnīḵ — it is attested from the 4th c. BCE, a thousand years before Arabic; Klein (KLN:108, Nourai's own reference) says the Greek came from Middle Persian *zarnīk 'through the medium of a Semitic language', i.e. Syriac zarnīḵā. Nourai is following Pihan's 1866 dictionary, which really does call az-zernīkh the 'prototype de la transcription grecque'. (2) Node #15 labels 'zahr, zara 1' Avestan/Old Persian: only zāra- is Avestan; zahr is Middle Persian and, as a separate word meaning 'poison', Nyberg derives it from *jaθra- 'means of killing'. The 'gall' word is MP zahrag > NP زهره. Everything else on the page — zar, zard, zardak, zargūn, zyrn, daraniya, daraniya-kara, zahre, zircon, zirconium — checks out.\",\n      \"note_fa\": \"مادهٔ پوکورنی در صفحهٔ ۴۲۹ چنین است: «ghel-1 ... معنی: درخشیدن؛ سبز، زرین، آبی، زرد»، که همان تعریف نورایی («درخشیدن، و نیز رنگ زردِ روشن») با همان شمارهٔ صفحه است؛ در بازسازی‌های امروزی این ریشه را *ǵʰelh₃- می‌نویسند. تمام بخش ایرانیِ نمودار از همین یک بند پوکورنی برآمده است: «اوستایی zari- «زرد، زرگون»، zairita- «زردِ کم‌رنگ»، zaranya-، پارسی باستان daraniya- «زر»، zaranaēna- «زرین»، zara- «زهره» (= χολή یونانی)». دو نکته باید اصلاح شود: نخست آنکه yونانی arsenikón نمی‌تواند از عربی الزرنیخ آمده باشد، زیرا از سدهٔ چهارم پیش از میلاد گواهی دارد؛ کلاین — همان مأخذی که نورایی به آن ارجاع می‌دهد — می‌گوید یونانی آن را از فارسی میانهٔ *zarnīk «به میانجی زبانی سامی» (سریانی zarnīḵā) گرفته است. دوم آنکه در خانهٔ ۱۵ صورت zahr پهلوی است نه اوستایی یا پارسی باستان، و در معنای «زهر» بنا بر نیبرگ از *jaθra- «ابزار کشتن» می‌آید؛ واژهٔ «زهره» از zahrag پهلوی است. بقیهٔ نمودار درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1\",\n        \"https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1%D9%87\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:429\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 36278ff: 'Root / lemma: ghel-1 ... Meaning: to shine; green, gold, blue, yellow, moon ... Page(s): 429-434'; the Iranian paragraph at line 36318 is quoted in the note above.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p. 624\",\n          \"stance\": \"supports\",\n          \"note\": \"WLD_Bd1_pages.txt line 59367 running head '624 ghel- (ghel-), ghelə- : ghlē-, ghlō- : ghlā-'; line 59403: 'Av. zaray- „gelb, gelblich, goldfarben“, zairita „gelb, fahlgelb“, zaranya- „Gold“, zaranaena „von Gold, golden“ ... zāra m. „Galle“ (nach Bartholomae Airan. Wb. 1690 < *ghelə wie lat. fel), nach der Farbe benannt wie gr. χόλος, lat. fel, an. gall'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins, IE appendix s.v. ghel-²\",\n          \"stance\": \"supports\",\n          \"note\": \"Watkins splits the root into ghel-¹ 'to call' (Pok. 428) and ghel-² 'to shine; with derivatives referring to colors, bright materials, gold, and bile or gall' [Pok. ghel- 429]; Etymonline s.v. arsenic likewise files the word under '*ghel- (2) to shine'.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 9.63 'gold'\",\n          \"stance\": \"supports\",\n          \"note\": \"SYN.txt line 15395: 'Skt. hiranya-, Av. zaranya-, OPers. daranya- (Dar. Sus. f. 35), all neuters' — Buck's table has the same three Indo-Iranian words as Nourai's Avestan and Old Persian boxes.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"zarena, zari, zaranya, zairita, zareta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The core forms are all Bartholomae's: zairi- (Nourai's 'zari') 'yellow, gold-coloured', found in the compounds zairi-gaona- 'yellow-coloured', zairi.dōiθra- 'with golden eyes'; zairita- 'yellow, pale-yellow'; zaranya- n. 'gold' (Yt. 5.129, V. 3.11) with its adjective *zaranya- 'golden' and zaranaēna- 'made of gold'. All continue *ǵʰel-/*ǵʰelh₃- with the regular Iranian *ǵʰ > z and the *-r- suffix seen also in Skt. hári- 'yellow', híraṇya- 'gold'. The two remaining forms are reconstructions printed without an asterisk: Hübschmann (Persische Studien, notes on Horn nos. 654 and 656) posits Old Persian *zarna / Avestan *zarena- beside zairi-, and, following Nöldeke, Avestan *zareta- for the attested zairita- as the immediate base of NP zard. So 'zarena' and 'zareta' are legitimate scholarly reconstructions rather than attested Avestan forms — Nourai has simply dropped the asterisks.\",\n          \"derivation_fa\": \"صورت‌های اصلی این خانه همه در فرهنگ ایرانی باستانِ بارتولومه هست: zairi- (همان zari نزد نورایی) «زرد، زرگون» که در ترکیب‌های zairi-gaona- «زردرنگ» و zairi.dōiθra- «زرین‌چشم» دیده می‌شود؛ zairita- «زردِ کم‌رنگ»؛ و zaranya- «زر» (یشت ۵٫۱۲۹، وندیداد ۳٫۱۱) با صفت *zaranya- «زرین» و zaranaēna- «از زر». همهٔ اینها بازماندهٔ *ǵʰelh₃- با پسوند -r- هستند و «غ» کامی هندواروپایی طبق قاعده در ایرانی به z بدل شده است (سنسکریت hári-، híraṇya-). دو صورت دیگر بازسازی‌اند نه گواهی‌شده: هوبشمان در «مطالعات فارسی» (یادداشت بر شماره‌های ۶۵۴ و ۶۵۶ هرن) صورت‌های *zarena- و — به پیروی نولدکه — *zareta- را برای توضیح «زرد» فارسی بازسازی کرده است. پس نورایی تنها ستاره‌های بازسازی را انداخته است؛ در باقی موارد ادعای او درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:429\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt line 36318: 'Avestan zari- „yellow, yellowish, golden“, zairita- „yellow, paled-yellow“, zaranya-, Old pers. daraniya- n. „gold“, zaranaena „from gold, golden“.'\"\n            },\n            {\n              \"ref\": \"KLN:667\",\n              \"status\": \"supports\",\n              \"note\": \"Klein cross-refers Avestic zaranya, Pers. zar 'gold' under his 'yellow' article; s.v. arsenic he writes 'Cp. Avestic zaranya, Pers. zar, „gold“, and the first element in zermahbub, and see yellow and words there referred to' (KLN_1971.txt line 20101).\"\n            },\n            {\n              \"ref\": \"SOD:411\",\n              \"status\": \"not_found\",\n              \"note\": \"Gharib printed p.411 (SOD_pages.txt leaf 478, running number 411) is in the wr-/wrc- range (entries 10141ff, 'wrcwnyʾ miracle, wonder'); there is no gold or Avestan material there. The Sogdian gold entries are at pp.471-472 (nodes #13, #3). This citation appears to be mistaken.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"s.vv. zairita-, zairi.dōiθra-, zaranya-, *zaranya-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt: 'j. zaranya- n. „Gold“: Yt. 5.129; 17.14 ... V. 3.11'; 'j. *zaranya- Adj. „golden“: arədvī ... Yt. 5.78'; 'zairita- Adj. „gelb“ ... ai. hárita- Adj.; np. vgl. zard'; 'j. zairi.dōiθra- Adj. „mit gelben, goldfarbenen Augen“'.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien, notes on Horn nos. 654 and 656 (p. 69)\",\n              \"stance\": \"partial\",\n              \"note\": \"HUB.txt line 2402ff: '654. Neben zar „Gold“ steht zarr wie neben zarīn „golden“: zarrīn, danach ap. *zarna (zd. *zarena-) und *zarnaina- (zd. *zarenaēna- für vorliegendes zaranaēna-) anzusetzen?'; '656. Nöldeke hat Recht, np. zard „gelb“ = ap. *zarta- (= zd. *zareta- für zairita-) zu setzen.' — the source of Nourai's unasterisked 'zarena' and 'zareta'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 624\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. zaray- „gelb, gelblich, goldfarben“, zairita „gelb, fahlgelb“, zaranya- „Gold“, zaranaena „von Gold, golden“.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"zar 1 «زر۱ ، زریر»; zard «زرد»; zardak «زردک»; zarnîx «زرنیخ»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are Horn's paragraph 654-656. (a) زر zar 'gold' < MP zarr [ZHBA/DHBA, M zr-] < Old Iranian *zarnya- / *zarna- (Av. zaranya-, OP daraniya-); the -rn- of the Old Persian stage assimilates to -rr- in Middle Persian (Hübschmann, PSt §156: 'ap. rn ... wird assimilirt zu rr, das zu r vereinfacht werden kann'), whence MP zarr, zarrēn 'golden' and NP zar, zarrīn. زریر zarīr, the second word in the box, is Horn's 'zerīr, zifīr „gelbes Färbholz, Gelbsucht“', the yellow dye-wood, from the same stem. (b) زرد zard 'yellow' < MP zard [zlt'] < Av. zairita- / *zareta- (Nöldeke and Hübschmann's reconstruction), with -ita- > MP -ard. (c) زردک zardak 'carrot' is zard + the diminutive/individualising suffix -ak, i.e. 'the little yellow one'; MP already has zardak (glossed 'safflower' by MacKenzie) and zardag '(egg) yolk'. (d) زرنیخ zarnīx 'orpiment, arsenic sulphide' is zar + the adjectival -nīk 'gold-coloured' (MP *zarnīk, Old Median *zaraniyaka-); its modern Persian shape with -x is the Arabicised one that came back from Arabic زرنيخ, which is why Horn marks it 'LW. arab. zarnīq, zarnīx' — a Persian → Arabic → Persian round trip. Armenian zarik, borrowed early from Middle Persian, preserves the pre-Arabic form.\",\n          \"derivation_fa\": \"هر چهار واژه در بندهای ۶۵۴ تا ۶۵۶ هرن آمده است. «زر» از فارسی میانهٔ zarr است و آن از ایرانی باستان *zarnya-/*zarna- (اوستایی zaranya-، پارسی باستان daraniya-)؛ خوشهٔ rn در گذر به فارسی میانه همگون شده و به rr بدل گشته است (هوبشمان، بند ۱۵۶: «rn پارسی باستان به rr همگون می‌شود و گاه به r ساده می‌گراید»)، از این‌رو zarr و zarrēn پهلوی و «زر» و «زرّین» فارسی. «زریر» — واژهٔ دوم همین خانه — همان است که هرن zerīr «چوب رنگرزی زرد» می‌نامد. «زرد» از zard پهلوی و آن از zairita-/*zareta- اوستایی است. «زردک» از «زرد» با پسوند تصغیر/تخصیص -ک ساخته شده، یعنی «زردِ کوچک»؛ در پهلوی نیز zardak و zardag «زردهٔ تخم‌مرغ» هست. «زرنیخ» از «زر» با پسوند صفت‌ساز -نیک «زرین‌رنگ» است (پهلوی *zarnīk، مادی کهن *zaraniyaka-)؛ صورت امروزی با «خ» معرّب است و از عربی زرنيخ به فارسی بازگشته، چنان‌که هرن آن را «وام‌واژهٔ عربی» می‌داند؛ صورت ارمنی zarik شکل پیش از عربی را نگه داشته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:145\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss p.145 (HRN.txt leaf 166) no. 654: '(1) zer „Gold“, zerīn (zerrīn); zernī (LW. arab. zarnīq, zarnīx) syr. talm. זרניכא „Arsenik“; zerīr, zifīr „gelbes Färbholz, Gelbsucht“. ap. vergl. δαρεικός(?); aw. zairi-, vergl. zaranya- „Gold“; phlv. zar, zarīn; ai. hári-, hiranya-.' Horn p.146 no. 656: 'zerd „gelb“, vergl. zerdāb, zerde „Galle“. aw. zairita- „gelb“; phlv. zart, zartīh; ai. hárita-.'\"\n            },\n            {\n              \"ref\": \"BQT:1012\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān-e Qāṭeʿ, printed p.1012 (BQT_v2_pages.txt leaf 472) is the زر page: the OCR shows 'زر ... طلا را گویند' (zar: they call gold), with the neighbouring entries زرِ جعفری 'pure gold' and زرِ سرخ, and Moʿin's numbered footnotes at the foot of the page (the Latin-script etyma in them are not legible in this OCR).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD s.vv. zarr, zard, zardak, zargōn\",\n              \"stance\": \"supports\",\n              \"note\": \"'zarr [ZHBA < A zhbʾ; DHBA < A dhb | M zr-, N ~] gold. ~ēn [zlyn! | M zryn, N ~īn] golden. ~(i)gar [zlykl | N ~gar] goldsmith'; 'zard [zlt' | N ~] yellow. ~īh: yellowness. zardag [zltk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower.'\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien p. 258 §156 and p. 69 (note on Horn 654)\",\n              \"stance\": \"supports\",\n              \"note\": \"p.258: 'zarnī „Auripigment“, arab. zarnīq, zarnīx, aber arm. zarik (Mos. Geogr.) „Auripigment, Arsenik“ (= ap. *zarniya für zd. zaranya- „Gold“) ... vgl. np. zarr „Gold“, zarrīn „golden“ (= ap. *zarna, *zarnaina- für zd. zaranaēna-)'; the note on Horn 654 adds 'phl. *zarrīk aus *zarnīk = zd. *zarenya-'.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"printed p. 767-768 and 1019\",\n              \"stance\": \"supports\",\n              \"note\": \"BQT_v2_pages.txt leaves 227, 228, 479 carry the headwords زرنیخ and زردک, i.e. all four of Nourai's words are Borhān headwords.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"zargŭn «زرگون»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"زرگون zargūn 'gold-coloured, golden' is a transparent compound of زر zar 'gold' and گون gūn 'colour' (< Av. gaona- 'colour, hair' — hence Nourai's cross-reference ☞Gěu 1). It is not a New Persian coinage: Avestan already has the exact compound zairi.gaona- 'yellow-coloured', and Middle Persian has zargōn [zlgwn'], glossed by MacKenzie 'golden, green, fresh', with the abstract zargōnīh 'greenness'. Horn treats it in its own paragraph, no. 661: 'zerγūn „gelbfarbig“ — aw. zairi.gaona- „gelbfarbig“; phlv. vergl. zarīngūn'. The word is the source of the Western mineral names in nodes #4-#5.\",\n          \"derivation_fa\": \"«زرگون» ترکیبی روشن است از «زر» و «گون» (از gaona- اوستایی به معنای «رنگ، مو» — ارجاع نورایی به ریشهٔ Gěu 1 نیز به همین است) و ساختهٔ فارسی نو نیست: در اوستا همین ترکیب zairi.gaona- «زردرنگ» وجود دارد و در پهلوی zargōn هست که مکنزی آن را «زرین، سبز، تازه» معنی کرده و صورت مصدری zargōnīh «سبزی» را نیز آورده است. هرن آن را در بند جداگانهٔ ۶۶۱ آورده: «zerγūn زردرنگ — اوستایی zairi.gaona-؛ پهلوی zarīngūn». همین واژه سرچشمهٔ نام‌های کانی در خانه‌های ۴ و ۵ است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:145\",\n              \"status\": \"partial\",\n              \"note\": \"The right book and the right etymology, but two pages later: Horn treats zargūn at p.147 (HRN.txt leaf 168) as no. 661 — 'zerγūn „gelbfarbig“. aw. zairi.gaona- „gelbfarbig“; phlv. vergl. zarīngūn (vd. 2 (67))' — not at p.145 (no. 654), which is the zar entry.\"\n            },\n            {\n              \"ref\": \"BQT:1012\",\n              \"status\": \"partial\",\n              \"note\": \"p.1012 of the Borhān is the زر page; the زرگون headword falls a few pages later in the same z-r sequence. The page Nourai cites supports the first element only.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD s.v. zargōn\",\n              \"stance\": \"supports\",\n              \"note\": \"'zargōn [zlgwn' | P zrgwng, N zargūn] golden, green, fresh. ~īh: greenness.' — the Middle Persian ancestor of the New Persian word, Parthian zrgwng.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"s.v. zairi.gaona-\",\n              \"stance\": \"supports\",\n              \"note\": \"Bartholomae has the Avestan compound zairi.gaona- 'gelbfarbig' (cited by Horn no. 661), showing the compound is inherited, not new.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"jargon : a yellow mineral\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French jargon (also jargoon) 'a yellowish gem, a variety of zircon' is indeed ultimately Persian zargūn, but no source makes the loan direct. Klein routes it 'F., fr. Port. zarcão, fr. Arab. zarqān, „minium“, ult. fr. Pers. zargūn, „gold-colored“, compound of zar, „gold“ ... and gūn, „color“'; Devic reaches the same conclusion from the Romance side, identifying jargon and zircon with Spanish azarcón / Portuguese zarcão and 'un terme arabe zarqoûn, avec l'article az-zarqoûn, qui se disait du minium'; Etymonline records the medieval Latin jargonce and Italian giargone and the same possible Arabic zarkun. So the historical route runs Persian zargūn → Arabic zarqūn 'red lead, minium' → Ibero-Romance zarcão/azarcón → Italian giargone → medieval Latin jargonce → 18th-c. French jargon, the sense drifting from 'red lead' to 'gold-coloured gem'. Nourai's arrow is right in substance but omits the Arabic and Romance stages that every source insists on, and this is the same jargon that the identical-looking word for 'gibberish' (from the gargle root) is not related to.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی jargon (و jargoon) به معنای «گوهر زردرنگ، گونه‌ای زیرکن» سرانجام از «زرگون» فارسی است، اما هیچ منبعی وام‌گیری را مستقیم نمی‌داند. کلاین مسیر را چنین می‌دهد: فرانسوی از پرتغالی zarcão، از عربی زرقون «سُرنج»، و آن سرانجام از «زرگون» فارسی («زر» + «گون»). دِویک نیز از سوی زبان‌های رومی به همین نتیجه می‌رسد و jargon و zircon را با azarcón اسپانیایی و zarcão پرتغالی و «واژهٔ عربی زرقون با حرف تعریف: الزرقون» یکی می‌داند؛ اتیمانلاین هم صورت لاتینی میانهٔ jargonce و ایتالیایی giargone را می‌آورد. پس مسیر واقعی چنین است: فارسی «زرگون» ← عربی زرقون ← پرتغالی/اسپانیایی zarcão/azarcón ← ایتالیایی giargone ← لاتینی میانهٔ jargonce ← فرانسوی jargon، با تحول معنایی از «سُرنج» به «گوهر زرگون». ادعای نورایی در اصل درست است ولی حلقه‌های عربی و رومی را انداخته، پس با احتیاط پذیرفتنی است. (این jargon با jargon به معنای «زبان نامفهوم» هم‌ریشه نیست.)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/zircon\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference on this node; the English child node carries AHD:1489.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. jargon 'a variety of zircon' (KLN_1971.txt line 128332)\",\n              \"stance\": \"partial\",\n              \"note\": \"'jargon, also jargoon, n., a variety of zircon. — F., fr. Port. zarcão, fr. Arab. zarqān, „minium“, ult. fr. Pers. zargun, „gold-colored“, compound of zar, „gold“ (see arsenic), and gun, „color“, which is rel. to Avestic gaona-, „color“. Cp. zircon.' Same origin, extra stages.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic s.v. Jargon (DEV.txt line 1555)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Jargon. Gemme de couleur jaune tirant sur le rouge ... Ital. giargone. Jargon et zircon ... sont certainement identiques à l'espagnol azarcon ... Et tous ces mots correspondent à un terme arabe zarqoûn, avec l'article az-zarqoûn, qui se disait du minium.'\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'zirkon|jargon|zarqun|zarq' in LKT.txt returns only unrelated hits (Gaunerjargon s.v. Chelek); Lokotsch has no zircon/jargon entry in this OCR.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"zircon; zirconium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Klein derives zircon straight from the French: 'zircon, n. — F., a var. of jargon, „a variety of zircon“'. Etymonline adds the German step that is historically better documented: English zircon is recorded 1794 from German Zirkon, the form Martin Heinrich Klaproth used in 1789 when he analysed the Ceylon 'jargon' and found a new earth in it; Zirkon itself is a re-shaping of 18th-c. French jargon. Zirconium is Klaproth's own coinage of 1789 for the metal, zircon + the -ium ending used for metallic elements; the metal was first isolated by Berzelius in 1824. So Nourai's chain jargon → zircon → zirconium is right, with German as the unnamed intermediary for zircon.\",\n          \"derivation_fa\": \"کلاین zircon را یکسره از فرانسوی می‌گیرد: «zircon: فرانسوی، گونه‌ای از jargon». اتیمانلاین حلقهٔ آلمانی را که سند تاریخی بهتری دارد می‌افزاید: zircon انگلیسی در ۱۷۹۴ از Zirkon آلمانی گرفته شده، همان صورتی که مارتین هاینریش کلاپروت در ۱۷۸۹ هنگام تجزیهٔ «ژارگونِ» سیلان و کشف خاکِ تازه در آن به کار برد؛ و Zirkon خود دگرگون‌شدهٔ jargon فرانسوی سدهٔ هجدهم است. zirconium نیز ساختهٔ خودِ کلاپروت در ۱۷۸۹ است: zircon به‌علاوهٔ پسوند -ium که برای نام فلزها به کار می‌رود (فلز آن را برتسلیوس در ۱۸۲۴ جدا کرد). پس زنجیرهٔ نورایی درست است، جز آنکه حلقهٔ آلمانی نام برده نشده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/zircon\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:1489\",\n              \"status\": \"not_checked\",\n              \"note\": \"AHD:1489 is a page of the New College Edition's main word list (not the IE appendix); only the appendix is available locally (AHD_watkins1985.txt) and the New College scans on archive.org are lending-only. Klein and Etymonline, checked instead, both give the French jargon > zircon derivation Nourai draws.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.vv. zircon, zirconium (KLN_1971.txt lines 270763-270780)\",\n              \"stance\": \"supports\",\n              \"note\": \"'zircon, n. — F., a var. of jargon, „a variety of zircon“'; 'zirconium, n. ... coined by the German chemist Martin Heinrich Klaproth (1743-1817) in 1789 ... fr. zircon; so called by him because it is found in the mineral zircon.'\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic s.v. Jargon\",\n              \"stance\": \"supports\",\n              \"note\": \"'Le minéralogiste Haüy a réuni ces deux sortes de pierres sous le nom commun de zircon' — jargon and zircon are the same word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"«زیرکونیم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"زیرکونیم zirkoniyom is the modern Persian chemical term for zirconium, a 20th-century learned borrowing of the international scientific name (French/English zirconium), taken over with its Latin -ium ending and spelt phonetically. It is thus the far end of a full circle: Persian زرگون → Arabic/Romance → French jargon → German Zirkon → English/French zirconium → Persian زیرکونیم. Nourai's arrow from the English box is the shortest true statement of that return; in practice the Persian scientific vocabulary of the Reza Shah period took such element names mainly through French.\",\n          \"derivation_fa\": \"«زیرکونیم» اصطلاح شیمیایی فارسی امروز برای عنصر zirconium است: وام‌واژه‌ای دانشی از سدهٔ بیستم که از نام بین‌المللی عنصر (فرانسوی/انگلیسی zirconium) با همان پایانهٔ لاتینی -ium گرفته و آوانویسی شده است. بدین‌سان دایره کامل می‌شود: «زرگون» فارسی ← عربی و زبان‌های رومی ← jargon فرانسوی ← Zirkon آلمانی ← zirconium فرانسوی/انگلیسی ← «زیرکونیم» فارسی. پیکان نورایی از خانهٔ انگلیسی کوتاه‌ترین بیان درست همین بازگشت است، هرچند واژگان شیمی فارسی در دورهٔ پهلوی اول بیشتر از راه فرانسوی وارد شده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference given by Nourai; Moshiri's dictionary of European words in Persian (VOP), which he uses for such items elsewhere, has no accessible copy.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. zirconium\",\n              \"stance\": \"supports\",\n              \"note\": \"Confirms zirconium as Klaproth's 1789 ModL coinage, i.e. an international scientific term of the kind Persian borrows wholesale.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi vol. 4 (foreign compounds)\",\n              \"stance\": \"silent\",\n              \"note\": \"Not checkable: the local MON files are the 2-volume Adena abridgement and vajehyab carries no entry for زیرکونیم.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Arabic\",\n          \"words\": \"az-zarnîx\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic زِرْنِيخ zirnīḵ 'orpiment, arsenic sulphide' is a borrowing from Middle Persian zarnīk / zarīk 'golden' (< *zaraniyaka-, cf. Old Median *zaraniyakā), i.e. from the same zar 'gold' as node #2. Nourai writes it with the definite article assimilated to the sun-letter z (al- + zarnīḵ > az-zarnīḵ), which is why he cross-refers to his root Al 3; that assimilated shape is what Romance and Latin sources cite (Spanish azarnefe, Portuguese azarnete). Hübschmann notes the same set: 'zarnī „Auripigment“, arab. zarnīq, zarnīx, aber arm. zarik ... (= ap. *zarniya für zd. zaranya- „Gold“)'. Modern Persian زرنیخ, in turn, is the Arabicised form come home.\",\n          \"derivation_fa\": \"عربیِ زِرْنیخ «زرنیخ، سولفید آرسنیک» وام‌واژه‌ای است از فارسی میانهٔ zarnīk/zarīk «زرین» (از *zaraniyaka-، سنجیدنی با مادی کهن *zaraniyakā)، یعنی از همان «زر» خانهٔ ۲. نورایی آن را با حرف تعریفِ همگون‌شده با حرف شمسیِ «ز» می‌نویسد (الـ + زرنیخ ← الزرنیخ/az-zarnīḵ) و از این‌رو به ریشهٔ Al 3 ارجاع می‌دهد؛ همین صورت است که در زبان‌های رومی بازتاب یافته (اسپانیایی azarnefe، پرتغالی azarnete). هوبشمان نیز می‌نویسد: «zarnī «زرنیخ»، عربی zarnīq و zarnīx، اما ارمنی zarik ... = پارسی باستان *zarniya در برابر zaranya- اوستایی». «زرنیخِ» فارسی امروز همان صورت معرّبِ بازگشته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%86%D9%8A%D8%AE\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:108\",\n              \"status\": \"supports\",\n              \"note\": \"Klein s.v. arsenic (KLN_1971.txt line 20091): '...fr. MPers. *zarnik, „gold, golden; orpiment“ (whence ModPers.-Arab. zarnikh, „orpiment“)' — the Persian → Arabic direction Nourai draws.\"\n            },\n            {\n              \"ref\": \"SKT:26\",\n              \"status\": \"not_found\",\n              \"note\": \"Skeat's Concise, printed p.26 (SKT.txt leaf 46) is the end of A: the entries there are 'Azimuth. (Arab.) ... Arab. al, the; and samt, a way' and 'Azure. (F.—Arab.)'. No zarnīḵ. Skeat's own Arsenic entry is at p.19 (leaf 39) and reads '... Late L. arsen[i]cum ... lit. a male prin[ciple] ... Gk. [arsen], a male' — no Arabic at all, so this reference does not support the node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien p. 258 §156\",\n              \"stance\": \"supports\",\n              \"note\": \"'zarnī „Auripigment“, arab. zarnīq, zarnīx, aber arm. zarik (Mos. Geogr.) „Auripigment, Arsenik“ (= ap. *zarniya für zd. zaranya- „Gold“)'.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic s.v. Azarnec (DEV.txt line 325)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Azarnec, adarnech, zarnech, zarnec, zarne, orpiment; esp. azarnefe; de l'arabe-persan az-zernikh' — the Arabic form with the assimilated article, exactly as Nourai writes it.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'زرنيخ' in AFM_pages.txt returns nothing; the word is not in this OCR of Addi Shir's list of Persian loans in Arabic.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"arsenikon\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real — Gk. ἀρσενικόν 'yellow orpiment' — but it cannot descend from Arabic. Greek arsenikón is attested from the fourth century BCE (Theophrastus, then Aristotle and Dioscorides), roughly a thousand years before Arabic became a written source language for Greek, so the arrow reverses the chronology. Every modern account, including Klein — the very reference Nourai cites on this node — makes the Greek a borrowing of Middle Persian *zarnīk 'gold-coloured, orpiment' taken 'through the medium of a Semitic language', naming Mishnaic Hebrew zarnīkh and Syriac zarnīkhā; Etymonline gives the same chain (Syriac (al) zarniqa < MP zarnik < Old Iranian *zarna- 'golden'), and Wiktionary's Arabic entry likewise routes Classical Syriac zarnīḵā beside, not below, Arabic زرنيخ. The Greek shape with ars- is a folk etymology on ἄρσην 'male, virile' (Klein: 'was influenced in form by arsenikós, „male“'), because orpiment was held to have potent, 'masculine' powers. Nourai is reproducing the nineteenth-century view of Pihan, who wrote of az-zernīkh as the 'prototype de la transcription grecque ἀρσενικόν'; that view is now abandoned. The correct arrow is Persian/Middle Persian → Syriac → Greek, with Arabic a parallel, later borrowing from the same Middle Persian source.\",\n          \"derivation_fa\": \"خودِ واژه درست است — یونانی ἀρσενικόν «زرنیخ زرد» — اما نمی‌تواند از عربی آمده باشد. arsenikón یونانی از سدهٔ چهارم پیش از میلاد گواهی دارد (تئوفراستوس، سپس ارسطو و دیوسکوریدس)، یعنی حدود هزار سال پیش از آنکه عربی بتواند به یونانی واژه بدهد؛ پس پیکان نورایی ترتیب زمانی را وارونه کرده است. همهٔ پژوهش‌های امروزی — از جمله کلاین که خودِ نورایی به او ارجاع داده — یونانی را وام‌گیری از فارسی میانهٔ *zarnīk «زرگون، زرنیخ» «به میانجی زبانی سامی» می‌دانند و عبری میشنایی zarnīkh و سریانی zarnīḵā را نام می‌برند؛ اتیمانلاین نیز همین زنجیره را می‌دهد. صورت یونانی با ars- ریشه‌شناسی عامیانه بر پایهٔ ἄρσην «نر، نیرومند» است، زیرا زرنیخ را دارای نیروی «مردانه» می‌پنداشتند. نورایی در اینجا دیدگاه سدهٔ نوزدهمی پیهان را بازمی‌گوید که الزرنیخ را «نمونهٔ نخستینِ صورت یونانی» خوانده بود؛ این دیدگاه امروز رها شده است. پیکان درست چنین است: فارسی میانه ← سریانی ← یونانی، و عربی وام‌گیری موازی و دیرترِ همان سرچشمهٔ فارسی میانه است. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/arsenic\",\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%86%D9%8A%D8%AE\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:108\",\n              \"status\": \"contradicts\",\n              \"note\": \"Klein s.v. arsenic (KLN_1971.txt line 20091): 'fr. L. arsenicum, arrhenicum, fr. Gk. ἀρσενικόν, ἀρρενικόν, „yellow orpiment“, fr. MPers. *zarnik, „gold, golden; orpiment“ (whence ModPers.-Arab. zarnikh, „orpiment“), through the medium of a Semitic language; cp. Mishnaic Heb. zarnikh, Syr. zarnikha, „orpiment“ ... Gk. ἀρσενικόν ... was influenced in form by ἀρσενικός, „male“.' Klein routes the Greek through Semitic (Syriac), and puts Arabic zarnīkh on a side branch, not above the Greek.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHN\",\n              \"where\": \"Pihan p. 45 s.v. ARSENIC (PHN.txt line 1845)\",\n              \"stance\": \"supports\",\n              \"note\": \"'zernīkh, orpiment, arsenic jaune, mot également usité chez les Arabes, et qui, précédé de l'article al, donne azzernikh, prototype de la transcription grecque ἀρσενικόν et du latin arsenicum' — this 1866 statement is the source of Nourai's arrow, and it is the view modern scholarship has replaced.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic s.v. Azarnec\",\n              \"stance\": \"partial\",\n              \"note\": \"Devic only says the Arabo-Persian az-zernikh 'est le même mot que le grec ἀρσενικός' — same word, without asserting the direction of the loan.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Arsenic, p.19\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Skeat derives it purely within Greek: 'Late L. arsen[i]cum ... lit. a male prin[ciple] ... Gk. [arsēn], a male', with no Iranian or Semitic source at all.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box is Latin arsenicum (also arrhenicum), the straight transliteration of Gk. ἀρσενικόν with the neuter -um for Greek -on, current in Pliny and in the medical and alchemical Latin of late antiquity and the Middle Ages. Klein and Skeat both give 'Late L. arsenicum' as the immediate source of the French and English word, so as a link in the chain the box is correct; only its parent (node #8) is misdrawn.\",\n          \"derivation_fa\": \"این خانهٔ خالی همان arsenicum لاتینی (و گونهٔ arrhenicum) است، یعنی برگردان مستقیم ἀρσενικόν یونانی با پایانهٔ خنثای -um به جای -on یونانی، که در پلینیوس و در لاتینِ پزشکی و کیمیاییِ اواخر دورهٔ باستان و سده‌های میانه رایج بوده است. کلاین و اسکیت هر دو «لاتینی متأخر arsenicum» را سرچشمهٔ بی‌واسطهٔ صورت فرانسوی و انگلیسی می‌دانند؛ پس این حلقه درست است و تنها خانهٔ مادرِ آن (خانهٔ ۸) نادرست رسم شده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/arsenic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference on this pass-through node; the sibling nodes carry KLN:108.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. arsenic\",\n              \"stance\": \"supports\",\n              \"note\": \"'OF. (= F.) arsenic, fr. L. arsenicum, arrhenicum, fr. Gk. ἀρσενικόν.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat p.19 s.v. Arsenic\",\n              \"stance\": \"supports\",\n              \"note\": \"'Late L. arsen[i]cum' is Skeat's Latin link too.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box is Old French / French arsenic, the learned Latin word taken over unchanged in the twelfth-thirteenth century medical vocabulary; it is the immediate source both of English arsenic (node #12) and, much later, of modern Persian آرسنیک (node #11). Klein: 'arsenic, n., a chemical element. — OF. (= F.) arsenic, fr. L. arsenicum'; Pihan lists it among the French words of Persian/Arabic ancestry for the same reason.\",\n          \"derivation_fa\": \"این خانهٔ خالی همان arsenic فرانسوی (و فرانسوی کهن) است: واژه‌ای دانشی که در واژگان پزشکی سده‌های دوازدهم و سیزدهم بی‌تغییر از لاتینی گرفته شد و سرچشمهٔ بی‌واسطهٔ arsenic انگلیسی (خانهٔ ۱۲) و — بسیار دیرتر — «آرسنیک» فارسی (خانهٔ ۱۱) است. کلاین می‌نویسد: «arsenic، عنصری شیمیایی — از فرانسوی کهن و فرانسوی arsenic، از لاتینی arsenicum». پیهان نیز آن را در شمار واژه‌های فرانسویِ برگرفته از فارسی و عربی آورده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/arsenic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference on this pass-through node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. arsenic\",\n              \"stance\": \"supports\",\n              \"note\": \"'OF. (= F.) arsenic, fr. L. arsenicum, arrhenicum.'\"\n            },\n            {\n              \"src\": \"PHN\",\n              \"where\": \"Pihan p. 45\",\n              \"stance\": \"supports\",\n              \"note\": \"'du latin arsenicum, dont nous avons fait arsenic' — the French form is the Latin word naturalised.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"ârsenîk «آرسنیک»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"آرسنیک ārsenīk is the modern Persian chemical name of the element, a twentieth-century borrowing of French arsenic (the â- and the final -k reflect French pronunciation, not English 'arsenic'), used beside the inherited زرنیخ, which stayed with the mineral orpiment. It is therefore the second homecoming on this chart: Persian zar → MP *zarnīk → Syriac → Greek → Latin → French → Persian, with the modern loan no longer recognisable as a relative of the زرنیخ two boxes above it — a textbook doublet.\",\n          \"derivation_fa\": \"«آرسنیک» نام شیمیایی امروزی این عنصر در فارسی است: وام‌واژه‌ای از سدهٔ بیستم از arsenic فرانسوی (آغازِ «آ» و «ک» پایانی گویای تلفظ فرانسوی است، نه انگلیسی)، که در کنار واژهٔ کهن «زرنیخ» به کار می‌رود؛ «زرنیخ» همچنان نام کانی زرنیخ زرد مانده است. بدین‌گونه این دومین بازگشت در همین نمودار است: «زر» فارسی ← *zarnīk پهلوی ← سریانی ← یونانی ← لاتینی ← فرانسوی ← «آرسنیک» فارسی؛ و امروز کسی «آرسنیک» را هم‌ریشهٔ «زرنیخِ» دو خانه بالاتر نمی‌شناسد — نمونه‌ای آشکار از دوگانه (doublet).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/arsenic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"VOP:41\",\n              \"status\": \"not_checked\",\n              \"note\": \"Moshiri, Farhang-e vāže-hā-ye orupāyi dar fārsi (1371/1992) — refs_online.json records that no scan or ebook of this book has been found anywhere (archive.org, ketabnak, noorlib all searched); it can only be bought second-hand.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. arsenic\",\n              \"stance\": \"supports\",\n              \"note\": \"Establishes the French form that Persian borrowed, and notes 'ModPers.-Arab. zarnikh' as the separate, inherited branch.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi vol. 4\",\n              \"stance\": \"silent\",\n              \"note\": \"The local MON files are the 2-volume abridgement and carry no آرسنیک entry; vajehyab's Moʿin text likewise returns nothing for it.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"arsenic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English arsenic is first recorded in the late fourteenth century in the sense 'yellow arsenic, arsenic trisulphide' (orpiment), borrowed from Old French arsenic < Latin arsenicum; the modern chemical sense 'the element As' dates from 1812, after Brandt's isolation of the metalloid. The alchemical and medical vocabulary of Middle English is the channel, the word travelling with the substance itself as a pigment and a poison.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی arsenic نخستین بار در اواخر سدهٔ چهاردهم میلادی به معنای «زرنیخ زرد، سه‌سولفید آرسنیک» گواهی شده و از فرانسوی کهن arsenic و آن از لاتینی arsenicum گرفته شده است؛ معنای شیمیایی امروزی (عنصر As) از ۱۸۱۲ است، پس از جداسازی این شبه‌فلز. راه ورود، واژگان کیمیا و پزشکی در انگلیسی میانه بوده و واژه همراه خودِ ماده — به عنوان رنگ‌دانه و زهر — سفر کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/arsenic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:108\",\n              \"status\": \"supports\",\n              \"note\": \"'arsenic, n., a chemical element. — OF. (= F.) arsenic, fr. L. arsenicum, arrhenicum, fr. Gk. ἀρσενικόν' (KLN_1971.txt line 20091) — the English word's immediate ancestry, as drawn.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat p.19 s.v. Arsenic\",\n              \"stance\": \"partial\",\n              \"note\": \"Skeat gives the same Latin-Greek route but stops at Greek 'a male', with no Iranian origin.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins appendix\",\n              \"stance\": \"silent\",\n              \"note\": \"ARSENIC is not in Watkins's index of English words (it is a Wanderwort, not an inherited IE item).\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Sogdian\",\n          \"words\": \"zyrn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian zyrn /zirn/ 'gold' is the East-Iranian cognate of MP zarr and NP zar, from the same Old Iranian *zarnya- with the -rn- cluster preserved rather than assimilated as in Middle Persian. Gharib gives the Avestan etymon on the spot ('zyrn gold, Av. zaranya-'), and the page is full of the compounds that show the word was fully productive: zyrnkryy zirn-kare 'goldsmith', zyrnpδʾk 'golden-legged', zyrnywn zirn-yon 'gold-coloured' (the exact structural match of Persian zargūn), zyrnwfc 'gold-woven'.\",\n          \"derivation_fa\": \"سغدی zyrn /zirn/ «زر» هم‌ریشهٔ شرقی‌ایرانیِ zarr پهلوی و «زر» فارسی است و از همان *zarnya- ایرانی باستان می‌آید، با این تفاوت که خوشهٔ rn در سغدی برجا مانده و — برخلاف فارسی میانه — به rr همگون نشده است. غریب در فرهنگ خود ریشه را همان‌جا می‌آورد: «zyrn زر، اوستایی zaranya-». همان صفحه پر از ترکیب‌هایی است که زایایی واژه را نشان می‌دهد: zyrnkryy «زرگر»، zyrnpδʾk «زرین‌پای»، zyrnywn «زرگون» (که ساختمانش دقیقاً برابر «زرگون» فارسی است) و zyrnwfc «زربفت». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:471\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, printed p.471 (SOD_pages.txt leaf 538, which carries the running number 471), entry 11566: 'zyrn — gold 102R18, 51R17, 69V14, 18', and the dictionary's headword line '/zirn/ zyrn gold Av. zaranya-'. Nourai's page number is exact.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"printed p. 472, entries 11569-11576\",\n              \"stance\": \"supports\",\n              \"note\": \"'11570 zyrnywn B — zirn-yon, gold-coloured'; '11572 zyrnkryy M — zirn-kare, gold-smith'; '11575 zyrnwfc C — zirn-wafc, gold-woven' — the Sogdian counterparts of Persian zargūn and zargar.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"s.v. zaranya-\",\n              \"stance\": \"supports\",\n              \"note\": \"Bartholomae's zaranya- n. 'Gold' is the Avestan form Gharib cites as the etymon.\"\n            }\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Old Persian\",\n          \"words\": \"daraniya : gold; daraniya-kara : goldsmith\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian daraniya- 'gold' is the south-western Iranian match of Av. zaranya-: the PIE palatal *ǵʰ, which gives z- in Avestan and the rest of Iranian, appears as d- in Old Persian (the same correspondence as OP adam : Av. azəm 'I'), and the syllabic *l̥ of *ǵʰl̥-en-yo- surfaces as -ar-. Kent sets it out under §82, §66.II, §88, §126, §144.IV. The word is attested twice in the Susa foundation charter (DSf 35, 49f). daraniyakara- 'goldsmith' is the vṛddhi form of the same stem plus kara- 'maker' (hence Nourai's cross-reference ☞Kwer to the root of kar- 'to make'), attested at DSf 49 for the Sardian and Egyptian goldsmiths who worked on Darius's palace; it survives as NP زرگر zargar. Kent adds, correctly, that Greek dareikós (the daric) is from the name of Darius, not from daraniya-.\",\n          \"derivation_fa\": \"پارسی باستان daraniya- «زر» همتای جنوب‌غربیِ zaranya- اوستایی است: «غ»ی کامی هندواروپایی که در اوستایی و دیگر زبان‌های ایرانی z می‌شود، در پارسی باستان به d بدل می‌گردد (همان تناظری که در adam پارسی باستان در برابر azəm اوستایی «من» دیده می‌شود) و l̥ی هجایی *ǵʰl̥-en-yo- به -ar- تبدیل می‌شود. کنت این را در بندهای ۸۲، ۶۶٫۲، ۸۸، ۱۲۶ و ۱۴۴٫۴ توضیح داده است. واژه دو بار در منشور بنیادگذاری شوش (DSf ۳۵ و ۴۹) آمده است. daraniyakara- «زرگر» صورت وریدّهیِ همان ستاک به‌علاوهٔ kara- «سازنده» است (ارجاع نورایی به ریشهٔ Kwer نیز به همین kar- است) و در DSf ۴۹ دربارهٔ زرگران سارد و مصر که در کاخ داریوش کار می‌کردند به کار رفته و در فارسی نو «زرگر» شده است. کنت به‌درستی می‌افزاید که واژهٔ یونانی dareikós از نام داریوش است نه از daraniya-. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:189\",\n              \"status\": \"supports\",\n              \"note\": \"Kent, Old Persian, Lexicon p.189 (KNT.txt leaf 212, the page number '189' printed immediately above the entry): 'daraniya- sb. „gold“: Av. zaranya-, Ars. Phl. zarrēn, NPers. zarr, Skt. hiranya-m, pIE *ĝhl̥-enio- (§82, §66.II, §88, §126, §144.IV), cf. NEng. gold. See also daraniyakara-. — daraniyam nsn. DSf 35. daraniyam asn. DSf 49f.'; and 'daraniyakara- sb. „goldsmith“: NPers. zargar „goldsmith“; daraniya- with vriddhi, + kara- „maker“ ... daraniyakarā npm. DSf 49.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 429\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old pers. daraniya- n. „gold“' stands in Pokorny's own list beside Av. zaranya-.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 9.63 'gold'\",\n              \"stance\": \"supports\",\n              \"note\": \"SYN.txt line 15395: 'Skt. hiranya-, Av. zaranya-, OPers. daranya- (Dar. Sus. f. 35), all neuters' — with the same Susa attestation Kent cites.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"p. 189 and §66.II\",\n              \"stance\": \"supports\",\n              \"note\": \"KNT.txt line 940: 'pIE *ĝhl̥-enio-, OP daraniya- „gold“, Skt. hiranya-' — the sound law spelled out.\"\n            }\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"zahr, zara 1 : bile\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Avestan half of this box is right and is Pokorny's own: Av. zāra- m. 'Galle, gall' (Bartholomae, AiW col. 1690, from the Frahang, F.49, with the Pahlavi gloss zahrak) is the exact match of Gk. χολή and Lat. fel, named — as Pokorny and Walde-Pokorny both say — after its colour, from *ǵʰolh₃-. Nourai's 'zara 1' is that word (his '1' is his own homonym number, distinguishing it from zara- 'to be angry'). What does not fit the label is 'zahr': that form is neither Avestan nor Old Persian but Middle Persian, and in Middle Persian zahr and zahrag are two different words — MacKenzie lists 'zahr [zhl] poison, venom' beside 'zahrag [zʾhlk'] bile, gall' — with Nyberg deriving zahr 'poison' from *jaθra- 'means for killing' (root jan- 'to smite'), i.e. from a completely different root. Only zahrag belongs here. So: the derivation of 'bile' from *ǵʰelh₃- is confirmed, but the box mislabels a Middle Persian form as Avestan/Old Persian and, if 'zahr' is meant as the poison word, folds in an unrelated etymon.\",\n          \"derivation_fa\": \"نیمهٔ اوستاییِ این خانه درست است و از خودِ پوکورنی گرفته شده: اوستایی zāra- «زهره، صفرا» (بارتولومه، ستون ۱۶۹۰، از فرهنگ اویم، با برابرِ پهلوی zahrak) دقیقاً همتای χολή یونانی و fel لاتینی است و — چنان‌که پوکورنی و والده‑پوکورنی هر دو می‌گویند — بر پایهٔ رنگش از ریشهٔ *ǵʰolh₃- نام گرفته است. «zara 1» نزد نورایی همین واژه است (عدد ۱ شمارهٔ هم‌آواییِ خودِ اوست). آنچه با برچسب خانه نمی‌خواند صورت zahr است: این صورت نه اوستایی است و نه پارسی باستان، بلکه پهلوی است؛ و در پهلوی zahr و zahrag دو واژهٔ جداگانه‌اند — مکنزی «zahr زهر، سم» را در کنار «zahrag زهره، صفرا» می‌آورد — و نیبرگ zahr «زهر» را از *jaθra- «ابزار کشتن» (از ریشهٔ jan- «زدن، کشتن») می‌گیرد، یعنی از ریشه‌ای یکسره دیگر. تنها zahrag به این ریشه تعلق دارد. پس ریشه‌شناسی «صفرا» درست است، اما خانه یک صورت پهلوی را اوستایی/پارسی باستان نامیده و — اگر zahr را به معنای «زهر» بگیریم — واژه‌ای بی‌ربط را نیز در آن گنجانده است؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1%D9%87\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:429\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt line 36318f: 'zara- m. „gall“ (= gr. χολή), named after the color as gr. χόλος, Latin fel, ... Old Norse gall ... (see Bartholomae Altiran. Wb.)'. Pokorny lists it as Avestan, not Old Persian, and does not know a form zahr.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1690 s.v. zāra-\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. zāra- m. „Galle“: zāras (NS. ya) F.49. Vgl. gr. χολή, Bthl. ZDMG. 37.155 ... Pü.: zahrak' — Bartholomae's own Pahlavi gloss is zahrak, i.e. the MP form is zahrag, not zahr.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD s.vv. zahr, zahrag\",\n              \"stance\": \"partial\",\n              \"note\": \"'zahr [zhl | M zhr, N ~] poison, venom'; 'zahrag [zʾhlk' | N ~a] bile, gall' — two separate Middle Persian words; only the second is the 'bile' word of this node.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg II, glossary s.v. zahr\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'zahr [zʾhl] poison ... MPrth jhr; Arm. lw. žahr; MPrs zhr; NP zahr; < *jaθra- „means for killing“, v.s.v. zatan (because of -hr Prs zahr must have been borrowed from NW)' — for Nyberg zahr 'poison' belongs to the root 'to smite', not to *ǵʰelh₃-.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 624\",\n              \"stance\": \"supports\",\n              \"note\": \"'zāra m. „Galle“ (nach Bartholomae Airan. Wb. 1690 < *ghelə wie lat. fel), nach der Farbe benannt wie gr. χόλος, lat. fel, an. gall.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Persian\",\n          \"words\": \"zahreh «زهره»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP زهره zahre 'gall bladder, gall; (figuratively) courage' continues Middle Persian zahrag [zʾhlk'] 'bile, gall', itself Av. zāra- extended by the very common MP suffix -ag (< Old Iranian *-aka-), with the regular loss of final -g in New Persian and its replacement by the final -e (hē-ye ġayr-e malfūz), exactly as MP bandag > NP بنده. Wiktionary reconstructs the pre-form as Proto-Iranian *jarHáH < PIE *ǵʰolh₃-éh₂, the feminine of the colour root, and lists Av. zāra-, Gk. χολή and OE ġealla as the cognates — the same set as Pokorny's. The figurative 'courage' is a calque of the physiology of the humours (gall = boldness), and Nourai's Rumi line — «زهره ندارم که بگویم تو را» 'I have not the gall to tell you' — illustrates precisely that sense. The homonym زهره Zohre 'Venus' is unrelated: that one is an Arabic loan, الزُّهَرة az-zuhara.\",\n          \"derivation_fa\": \"«زهره» فارسی نو به معنای «کیسهٔ صفرا، صفرا» و به‌گونهٔ مجازی «دلیری» بازماندهٔ zahrag پهلوی است، و آن خود همان zāra- اوستایی با پسوند بسیار پرکاربردِ پهلویِ -ag (از *-aka- ایرانی باستان) است؛ «گ» پایانی در فارسی نو طبق قاعده افتاده و جای آن را «هـ»ی غیرملفوظ گرفته است، درست مانند bandag ← «بنده». ویکی‌واژه صورت پیشین را ایرانی آغازین *jarHáH و هندواروپایی *ǵʰolh₃-éh₂ (صورت مادینهٔ ریشهٔ رنگ) بازسازی می‌کند و اوستایی zāra-، χολή یونانی و ġealla انگلیسی کهن را هم‌ریشهٔ آن می‌شمارد — همان فهرست پوکورنی. معنای مجازی «دلیری» از طب اخلاط برآمده (صفرا = جسارت) و بیت مولوی که نورایی آورده — «زهره ندارم که بگویم تو را» — دقیقاً همین معنا را نشان می‌دهد. «زهرهٔ» به معنای سیارهٔ ناهید هم‌ریشهٔ این واژه نیست و وام‌واژه‌ای است از عربی الزُّهَرة. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1%D9%87\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference on this node; the parent box carries POK:429, which has the Avestan zara- 'gall'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD s.v. zahrag\",\n              \"stance\": \"supports\",\n              \"note\": \"'zahrag [zʾhlk' | N ~a] bile, gall' — MacKenzie explicitly equates the Middle Persian word with New Persian zahra.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1690 s.v. zāra-\",\n              \"stance\": \"supports\",\n              \"note\": \"Bartholomae's Pahlavi rendering of Av. zāra- is 'zahrak', i.e. the direct ancestor of زهره.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn p. 146, no. 656\",\n              \"stance\": \"partial\",\n              \"note\": \"'zerd „gelb“, vergl. zerdāb, zerde „Galle“' — Horn attaches the Persian words for bile (zardāb, zarde) to zard 'yellow' in the same root, but does not treat زهره itself in this paragraph.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T02:21:52.746Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-185.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T02:21:57.032Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-185.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 185"
}
```


### [2026-09-06T02:22:04.992Z] TOOL RESULT

```
JSON OK
nodes verified: 21/21
node verdicts: {'plausible': 3, 'confirmed': 17, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'partial': 3, 'not_checked': 8, 'not_found': 2, 'contradicts': 1}
books consulted: {'partial': 8, 'supports': 37, 'silent': 6, 'contradicts': 2} | by book: {'BRT': 8, 'KLN': 8, 'PHD': 5, 'HUB': 4, 'SKT': 4, 'DEV': 4, 'WLD': 3, 'SOD': 2, 'POK': 2, 'AHD': 2, 'MON': 2, 'PHN': 2, 'BQT': 1, 'LKT': 1, 'AFM': 1, 'SYN': 1, 'KNT': 1, 'NYB': 1, 'HRN': 1}
```


## [2026-09-06T02:22:20.916Z] AGENT

Written and validated: `data/verification/page-185.json` — `verify_check.py 185` reports 21/21 nodes, 0 PROBLEM lines.

**Page 185 (book p.155), 2 entries (1 redirect skipped), 21 nodes**
- Roots: 2 confirmed. Nodes: 17 confirmed, 3 plausible, 1 disputed.
- Ref checks: 14 supports, 3 partial, 1 contradicts, 2 not_found, 8 not_checked (no reference given, or VOP/AHD:1489 unobtainable).

**disputed**
- Ghel #8 Greek *arsenikon* ← Arabic *az-zarnīx*: chronology is reversed. Gk ἀρσενικόν is attested from the 4th c. BCE (Theophrastus/Aristotle/Dioscorides). Klein — the very reference Nourai cites (KLN:108) — routes it from Middle Persian \*zarnīk "through the medium of a Semitic language" (Syriac zarnīḵā); Arabic زرنيخ is a parallel, later loan from the same MP source. Nourai is following Pihan (1866), who literally called az-zernīkh the "prototype de la transcription grecque".

**plausible**
- Gheis #1 Avestan: zaēša-, zōišnu-, zōiždišta- all confirmed (Bartholomae cols. 1691/1693-94, Pokorny 427, Klein 655), but "zaěšta" is in no source — the printed page really has it, so it is the book's, not the extraction's.
- Ghel #4 French *jargon*: Persian zargūn is the ultimate source, but Klein and Devic both route it Arabic zarqūn → Port. zarcão/Sp. azarcón → It. giargone → Fr. jargon; the direct arrow skips those stages.
- Ghel #15 "zahr, zara 1" labelled Avestan/Old Persian: only Av. zāra- 'gall' is Avestan; zahr is Middle Persian, and MP zahr 'poison' is a different word (Nyberg: \< \*jaθra- 'means for killing'). The bile word is MP zahrag > NP زهره.

**transcription_suspect:** none. **Extraction errors:** none — the page image matches the JSON throughout (checked pdf p.185, copied to `data/verification/sources/refs/ocr/BOOK/185.png`).

**Two citation problems worth noting (data is fine, Nourai's page numbers are not):** SOD:411 on the Avestan Ghel node points at Gharib's *wrc-* page (no gold material there; the real gold pages 471/472 are cited correctly elsewhere); SKT:26 on the Arabic node is Skeat's *Azimuth/Azure* page, and Skeat's own *Arsenic* entry (p.19) has no Arabic at all.
