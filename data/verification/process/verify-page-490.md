# Verification process log — verify-page-490


## [2026-09-14T03:08:37.936Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 490 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-490.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-490.json. Write /home/sfmqrb/git/rishe/data/verification/page-490.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 490` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:38.896Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:39.679Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:39.694Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T03:08:40.181Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-490.txt"
}
```


### [2026-09-14T03:08:40.207Z] TOOL RESULT

```
1	=== PDF page 490 (book page 460) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sweid : sweat  (refs POK:1043)
4	#1 (parent #0) [Avestan] refs=POK:1043 | xvaeza : sweat
5	  #2 (parent #1) [Persian] refs=BQT:797 | xay, xoy «خوی» : sweat, saliva
6	  #3 (parent #1) [Sogdian] refs=SOD:180 | xwys : to sweat
7	  #4 (parent #1) [Persian] refs=HRN:114; BQT:805; MON:1472 | xeyŭ «خیو» : saliva | extra: خیوه ۲
8	#5 (parent #0) [Germanic] refs=AHD | swaidaz : sweat
9	  #6 (parent #5) [English] refs=None | sweat, sweater
10	--- entry 1 ---
11	ROOT [Indo-European] Sweks, Seks : six  (refs POK:1044)
12	#1 (parent #0) [Avestan / Old Persian] refs=POK:1044; GPL:41 | xšvaš : six ; xšvaš-dasa : sixteen ☞Dekm ; xšvašti : sixty
13	  #2 (parent #1) [Persian] refs=BQT:1266 | šeš «شِش» : six | extra: شانزده ، شَست
14	#3 (parent #0) [Germanic] refs=AHD | seks : six
15	  #4 (parent #3) [English] refs=None | six, sixteen, sixty
16	#5 (parent #0) [Latin] refs=None | sex : six
17	  #6 (parent #5) [English] refs=None | semester
18	#7 (parent #0) [Greek] refs=None | hex : six
19	  #8 (parent #7) [English] refs=None | hexagon, hexadecimal
20	--- entry 2 ---
21	ROOT [Indo-European] Swekwo : resin, juice  (refs POK:1044)
22	#1 (parent #0) [Greek] refs=AHD | hopos, opos : juice ; opion : poppy juice
23	  #2 (parent #1) [Persian] refs=BQT:86 | apyŭn «اپیون» : opium | extra: افیون
24	  #3 (parent #1) [Latin] refs=None | 
25	    #4 (parent #3) [English] refs=None | opium
26	
```


## [2026-09-14T03:08:43.088Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-490.json | head -200",
 "description": "Read source JSON for page 490"
}
```


### [2026-09-14T03:08:44.166Z] TOOL RESULT

```
{
    "pdf_page": 490,
    "book_page": 460,
    "entries": [
        {
            "root": {
                "name": "Sweid",
                "lang": "Indo-European",
                "refs": "POK:1043",
                "gloss": "sweat"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:1043",
                    "words": [
                        {
                            "translit": "xvaeza",
                            "gloss": "sweat",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "BQT:797",
                    "words": [
                        {
                            "translit": "xay, xoy",
                            "gloss": "sweat, saliva",
                            "script": "\u062e\u0648\u06cc"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0632\u067e\u06cc\u0634 \u062f\u0647\u0633\u062a\u0627\u0646 \u0633\u0648\u06cc \u0631\u06cc \u06a9\u0634\u06cc\u062f - \u0632\u0627\u0633\u0628\u0627\u0646 \u0628\u0647 \u0631\u0646\u062c \u0648 \u0628\u0647 \u062a\u06af \u062e\u0650\u0648\u06cc \u06a9\u0634\u06cc\u062f",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Sogdian",
                    "refs": "SOD:180",
                    "words": [
                        {
                            "translit": "xwys",
                            "gloss": "to sweat",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "HRN:114; BQT:805; MON:1472",
                    "words": [
                        {
                            "translit": "xey\u016d",
                            "gloss": "saliva",
                            "script": "\u062e\u06cc\u0648"
                        }
                    ],
                    "script_extra": "\u062e\u06cc\u0648\u0647 \u06f2",
                    "note": null,
                    "quote": {
                        "text": "\u0632\u062f\u06cc\u062f\u0627\u0631 \u067e\u06cc\u0631\u0627\u0646 \u0641\u0631\u0648 \u0645\u0627\u0646\u062f\u0646\u062f - \u062e\u06cc\u0648 \u0632\u06cc\u0631 \u0644\u0628\u0647\u0627 \u0628\u0631\u0627\u0641\u0634\u0627\u0646\u062f\u0646\u062f",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "swaidaz",
                            "gloss": "sweat",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "sweat, sweater",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Sweks, Seks",
                "lang": "Indo-European",
                "refs": "POK:1044",
                "gloss": "six"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:1044; GPL:41",
                    "words": [
                        {
                            "translit": "x\u0161va\u0161",
                            "gloss": "six",
                            "script": null
                        },
                        {
                            "translit": "x\u0161va\u0161-dasa",
                            "gloss": "sixteen",
                            "script": null,
                            "see": [
                                "Dekm"
                            ]
                        },
                        {
                            "translit": "x\u0161va\u0161ti",
                            "gloss": "sixty",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "BQT:1266",
                    "words": [
                        {
                            "translit": "\u0161e\u0161",
                            "gloss": "six",
                            "script": "\u0634\u0650\u0634"
                        }
                    ],
                    "script_extra": "\u0634\u0627\u0646\u0632\u062f\u0647 \u060c \u0634\u064e\u0633\u062a",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "seks",
                            "gloss": "six",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "six, sixteen, sixty",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": null,
                    "words": [
                        {
```


## [2026-09-14T03:08:44.494Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/agent/charts/page-490.txt && echo \"---SOURCE MATRIX---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read chart and source matrix"
}
```


### [2026-09-14T03:08:44.549Z] TOOL RESULT

```
=== PDF page 490 (book page 460) ===
--- entry 0 ---
ROOT [Indo-European] Sweid : sweat  (refs POK:1043)
#1 (parent #0) [Avestan] refs=POK:1043 | xvaeza : sweat
  #2 (parent #1) [Persian] refs=BQT:797 | xay, xoy «خوی» : sweat, saliva
  #3 (parent #1) [Sogdian] refs=SOD:180 | xwys : to sweat
  #4 (parent #1) [Persian] refs=HRN:114; BQT:805; MON:1472 | xeyŭ «خیو» : saliva | extra: خیوه ۲
#5 (parent #0) [Germanic] refs=AHD | swaidaz : sweat
  #6 (parent #5) [English] refs=None | sweat, sweater
--- entry 1 ---
ROOT [Indo-European] Sweks, Seks : six  (refs POK:1044)
#1 (parent #0) [Avestan / Old Persian] refs=POK:1044; GPL:41 | xšvaš : six ; xšvaš-dasa : sixteen ☞Dekm ; xšvašti : sixty
  #2 (parent #1) [Persian] refs=BQT:1266 | šeš «شِش» : six | extra: شانزده ، شَست
#3 (parent #0) [Germanic] refs=AHD | seks : six
  #4 (parent #3) [English] refs=None | six, sixteen, sixty
#5 (parent #0) [Latin] refs=None | sex : six
  #6 (parent #5) [English] refs=None | semester
#7 (parent #0) [Greek] refs=None | hex : six
  #8 (parent #7) [English] refs=None | hexagon, hexadecimal
--- entry 2 ---
ROOT [Indo-European] Swekwo : resin, juice  (refs POK:1044)
#1 (parent #0) [Greek] refs=AHD | hopos, opos : juice ; opion : poppy juice
  #2 (parent #1) [Persian] refs=BQT:86 | apyŭn «اپیون» : opium | extra: افیون
  #3 (parent #1) [Latin] refs=None | 
    #4 (parent #3) [English] refs=None | opium
---SOURCE MATRIX---
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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T03:08:49.198Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-490.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-14T03:08:50.176Z] TOOL RESULT

```
                        {
                            "translit": "sex",
                            "gloss": "six",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "semester",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": null,
                    "words": [
                        {
                            "translit": "hex",
                            "gloss": "six",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 7,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "hexagon, hexadecimal",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Swekwo",
                "lang": "Indo-European",
                "refs": "POK:1044",
                "gloss": "resin, juice"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "hopos, opos",
                            "gloss": "juice",
                            "script": null
                        },
                        {
                            "translit": "opion",
                            "gloss": "poppy juice",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "BQT:86",
                    "words": [
                        {
                            "translit": "apy\u016dn",
                            "gloss": "opium",
                            "script": "\u0627\u067e\u06cc\u0648\u0646"
                        }
                    ],
                    "script_extra": "\u0627\u0641\u06cc\u0648\u0646",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Latin",
                    "refs": null,
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "opium",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        }
    ]
}
```


## [2026-09-14T03:08:51.264Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','BQT','SOD','HRN','MON','AHD','GPL','WLD','IEC','SYN','KLN','HUB','PHD','CHEUNG','BRT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:500])\n\"",
 "description": "Check refs_online metadata"
}
```


### [2026-09-14T03:08:52.304Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (re
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); op
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp
GPL {"title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911", "edition_found": "1911", "kind": "archive_djvu", "url": "https://archive.org/details/grammarofpersian0000plat", "identifier": "grammarofpersian0000plat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt", "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf onli
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 6
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf onli
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.t
CHEUNG null
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan m
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qa
```


## [2026-09-14T03:08:57.058Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls POK* && grep -n \"sueid\\|su̯eid\\|sveid\\|sweid\" POK_full.txt | head -30",
 "description": "Grep Pokorny for sweid"
}
```


### [2026-09-14T03:08:57.212Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
8139:not better to Irish find' white ', see below sueid-' shine '); 
83367:Root / lemma: sueid-1 
83386:Root / lemma: sueid-2 
84337:Root / lemma: sueid- {* ksue/d- < g'^heid-) 
84351:See also: s. also sueid- above S. 1042, Z. 5. 
84399:sueid-) here?
```


## [2026-09-14T03:08:57.962Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1043\\|1044\" POK_full.txt | head -30",
 "description": "Find page markers in POK_full"
}
```


### [2026-09-14T03:08:58.045Z] TOOL RESULT

```
83509:Page(s): 1043-1044
```


## [2026-09-14T03:09:00.420Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '83360,83420p' POK_full.txt && echo \"=====2====\" && sed -n '83480,83560p' POK_full.txt",
 "description": "Read Pokorny sueid entries"
}
```


### [2026-09-14T03:09:00.492Z] TOOL RESULT

```
English meaning: to flow, to wet; water, etc.. 



References: WP. II 516 f., WH. II 611 f.. Frisk 104, 166, 184f. 
Page(s): 1039-1040 

Root / lemma: sueid-1 

Meaning: to shine 

Material: Avestan x'aena-^ burning, lohend' {*x'aedna-)\ Latin sTdus, -e/ys "stars', 

cc»/7s/o'e/'a/'e''betrachten', des/derare long, want'; 

Lithuanian siz/io'i/s "blank, gleaming', svyst/'to gleam begin', sv/du, -e//"gleam', Latvian 
SK/s/ "anbrechen, of days', SKa/b'/?" anoint' (actually "gleam make'); 

ein similar *sueit-, but in the meaning "singe, burn' in Old Icelandic svTda, Old High 
German swTdan^burVi; in addition probably as Aoristpras. Old High German swedan 
"schwelend burn ' and with ablaut derailment Old English swadur smoke'. Middle High 
German swadem ^Rauch schwaden, haze, mist' 

References: WP. II 520 f., WH. II 534, Trautmann 296. 
Page(s): 1 042 

Root / lemma: sueid-2 

Meaning: to sweat; sweat n. 

Material: Old Indie svfdyati, svedate ^ sc\\m\.z{\ sveda-m. = Avestan xvaeda-^Sc\r\\Ne\Q>' (= 

Germanic *swaita-); 

Armenian k'irt-n. Gen. -5/7"Schweift' {rtirom dr, compare gr. iSpux;, Latvian sviedri); gr. 
(£)l5o(; (Ionian) n. "Schweift', hom. etc. {z)\lb\ui, AtticlSiu) " sweat', 15pu)(;, -Gi^oo,, AtticlSpux; 



probably after supux;, -Giioq " mould, dank decay ' from the originally -05-stem from hom. 
Dat. i5pco, Akk. iSpw- (grown from Indo Germanic *suidro), iSpcbu) "sweat' (*i5pu)a-iu)); 

alb. {*jedros) dirse, djerse^ sweat ', djers^ to sweat ' (with 5 from //in present *suf- 
dro^tio); Common /7->y- Slavic Albanian; h->J-, y-0\6 Indie Tocharian. 

Rumanian sudoare 'sweat' 

Latin sudor, -o/7s'Schweifl' {*suoidds), sudd, -are'schwitzen'; 

kymr. chwys, corn, whys, bret. c'/7c»i/ez"Schweift' {*suidso-); 

Old English swat. Old Saxon swet. Old High German sweizm. 'Schweifl', Old Icelandic 
sveitim. ds.; Old High German swizzen{= Old Indie svfdyati) ^ schwitzeri , Kaus.-lter. Old 
High German sweizzan. Middle High German 5M/e/ze/7"Schweift shed, bluten, damp 
become'. Middle High German also "hot make, rosten, in Gluthitze aneinanderhammern, 
schweideri (= Old Indie sved ay ati ^ aWows schwitzen'); 

Latvian sviedriP\. 'Schweift', svTstu, si//s/ "schwitzen', 5i//b'e/ 'schwitzen make'. 

Basque izerdiu. " sweat' : Hungarian izzadniv. " sweat'. 

=====2====
skesur, gr. £Kup6^, £Kupa : Lithuanian sesuras. Old High German swehur, swagur: 
lAAupioi , oi, lllyrians, lAAupia , n, lllyria, also'lAAupi^ , n. Adj. lAAupiKO^ , n, 6v, lllyrian: -kp), 
the region or province of lllyria, 'lAAupi^ca , speak the lllyrian language, 'IAAupla:-hence 
Adv. 'lAAupiaii. 

gr. £Kup6(; "father-in-law, under between the father of Ehemanns', SKupa " mother-in-law '; 

alb. U7e/7e/r"father-in-law', vjeherre^ mother-in-law '; [common alb. shift sv- > v-, or drop of 
the initial s-] 

Latin socer, -e/7"father-in-law', socrus, -us' mother-in-law '; cymr. chwegr, corn, hweger' 
mother-in-law ', neologism cymr. chwegrwn, corn. /7by/ge/'e/7 "father-in-law'; Old High 
German swehur. Old English SM/ec»/'"Schwaher', Old High German swigar. Old English 
sweger{ *swes-rQ) ' mother-in-law '; 



Gothic swafhrd= Old Norse svsera^ mother-in-law ' {*swehrdn-), neologism Gothic 
5M/a/77/'a 'father-in-law' {*swehran-), as also Modern High German Schw/egervater aiter 
Schwieger(mutter) for Schwa her, 

Lithuanian ses^Aas "father-in-law'; Old Church Slavic svekry^ mother-in-law ' {-kr- 
through dissimilation against the aniaut has not changed to -sr-), whereupon m. svekrb 
"father-in-law'; 

lengthened grade: Old Indie svasura-' belonging to father-in-law ', Old High German 
swagur{*suekur6s) "brother-in-law (*son of father-in-law)', also "father-in-law, son-in-law'. 

References: WP. II 521 f., WH. 550 f., Trautmann 295 f., Vasmer2, 588. 
Page(s): 1043-1044 

Root / lemma: suek- 

Meaning: to smell (well) 

Note: only brit. and West Germanic 

Material: Cymr. chweg^sweei, pleasant', corn, whek, bret. c'houek, cymr. chwaeth 

{*suekto-) "taste'; Old High German 5M/e/7/75/7 "smell, stink, spring up, bubble'; with 

gemination Old High German swekhe, sueckiaP\. "odores'. Old Saxon sn^ec "smell, odor, 

fragrance ', Old English swecc, swaecc^iasie, smell, odor, fragrance ', sweccan^smeW. 

References: WP. II 521. 

Page(s): 1 043 

Root/ lemma: sueRs, seRs, RseRs, RsueRs, ueRs{\ uRs) {*ghe-ska) 

Meaning: six 

Material: Old Indie s5/(from sats), Avestan xsvas, Armenian i/ep(in vaf'sun '60' is a from 

eumgelautet); gr. £^, dial. Fs^ (knidisch ^sarpi^ " 6-lined barley', maybe from *^£^); alb. 

[attribute noun] gjashte's\x'; 

[common alb. gh- > gl- > gj- : Nth. gh- > dz-], hence alb. gjashte's\x' from an ordinal 
number {*gheks-ta) : Old Indie sa/"six', sastha- "sixth' was initially an ordinal number. 

Note: 

Anatolian languages show a pattern similar to alb. So Lycian aitata {* oktd(u)ta) "eight' : alb. 
/e/a "eight'; Lycian nuntata 'n\ne' : alb. nanda'n\ne'. Therefore alb. shtata 'seven' derived 
from a truncated *sa{pjtata ' seven' later Old Indie saptathah, Avestan hapta&a-. Old 
Saxon sivotho. Old English seofoda, Lithuanian septintas, also Old Indie saptatf-, Avestan 
haptaiti-lQ\ in alb. -ta, -teare attribute endings that were solidified in Anatolian and Indie 



cognates. The attribute /a (used in the genitive and adjectives) is unique to alb. language 

alone. 

Therefore alb. teta "eight' is a zero grade of Lycian aitata {*oRtd(u)ta) 'eight'. It was initially 

an ordinal number used as an attribute [compare Latin octuag/nta' 80']. 

Alb. Tosc nanta, Geg nanda^ nine ' derived from Lycian nuntata 'n\ne'.
```


## [2026-09-14T03:09:01.416Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: sue\" POK_full.txt | sed -n '1,60p'",
 "description": "List sue- roots in Pokorny"
}
```


### [2026-09-14T03:09:01.476Z] TOOL RESULT

```
83367:Root / lemma: sueid-1 
83386:Root / lemma: sueid-2 
83424:Root / lemma: suei-, sui- {*g"hei- : ksuel) 
83468:Root / lemma: suekru- {*RueRur-a) 
83511:Root / lemma: suek- 
83724:Root / lemma: suel-l(k-) 
83754:Root / lemma: suel-2 
83833:Root / lemma: suel-4 
83839:Root / lemma: sue-lo- suellio(n)- 
83878:Root / lemma: suelplo-s 
83894:Root / lemma: suem- 
83939:Root / lemma: sueng-, suenk- : sueg-, suek- {*g"heng- : ksueng-) 
83982:Root / lemma: suenk-, sunk- 
83996:Root / lemma: suento- sunto- 
84010:Root / lemma: suen- 
84037:Root / lemma: suep-1, sup- {* kuep-1) 
84086:Root / lemma: suep-2, sup-, sueb- 
84141:Root / lemma: suergh- {*g"hergh- : ksuergh-) 
84162:Root / lemma: suer-1 (also ser-?) 
84188:Root / lemma: suer-2 
84233:Root / lemma: suer-3 
84255:Root / lemma: suer-4 
84282:Root / lemma: suer-5 
84337:Root / lemma: sueid- {* ksue/d- < g'^heid-) 
84355:Root / lemma: sue(i)-
```


## [2026-09-14T03:09:06.567Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '83410,83425p' POK_full.txt && echo \"====sueks page====\" && sed -n '83560,83620p' POK_full.txt",
 "description": "Pokorny sueid-2 refs and sueks continuation"
}
```


### [2026-09-14T03:09:06.640Z] TOOL RESULT

```
Old English swat. Old Saxon swet. Old High German sweizm. 'Schweifl', Old Icelandic 
sveitim. ds.; Old High German swizzen{= Old Indie svfdyati) ^ schwitzeri , Kaus.-lter. Old 
High German sweizzan. Middle High German 5M/e/ze/7"Schweift shed, bluten, damp 
become'. Middle High German also "hot make, rosten, in Gluthitze aneinanderhammern, 
schweideri (= Old Indie sved ay ati ^ aWows schwitzen'); 

Latvian sviedriP\. 'Schweift', svTstu, si//s/ "schwitzen', 5i//b'e/ 'schwitzen make'. 

Basque izerdiu. " sweat' : Hungarian izzadniv. " sweat'. 

References: WP. II 521, WH. II 623, Trautmann 295. 
Page(s): 1 043 

Root / lemma: suei-, sui- {*g"hei- : ksuel) 

====sueks page====
Alb. Tosc nanta, Geg nanda^ nine ' derived from Lycian nuntata 'n\ne'. 

Slavic, Germanic, Baltic languages follow illyr-alb. attribute -/a ending. 

Latin sex, Old Irish 5e'6', seser'6 man', mor-feser ' magnus seviratus, 7 man', cymr. etc. 
chwech^Q"; Gothic saihs. Old Icelandic sex. Old High German sehs, Lithuanian inflectional 
ses'r. Old Church Slavic sestb (= Old Indie sastf-); Tocharian A sak, B skas; compare Latin 
sedec/m:0\6 Indie s^dasa^6 (Avestan xsvasdasa-'the 16.'). 

ordinals: Old Indie sastha-, Avestan xstva-; Armenian vecerord, gr. £kto(;; alb. /- 
gjashtete, i-gjashte, lllyrian Sestus; Latin sextus, sestus {Sestius, Oscan leoTieg, Umbrian 
se5/e/7/5S/5/'i/'sextantariarum'; Indo Germanic probably *s(u)ektos, in Latin and Germanic 
with Eindringen of 5 from the Grundzahl); gall, suexos. Old Irish sessed, cymr. chweched, 
Gothic safhsta. Old High German sehsto, sehto. Old Icelandic sette; Lithuanian sestas. 
Old Prussian m. zero grade uschts, compare Old Lithuanian usios 'Wochenbett' (Old 
Prussian loanword), genuine Lithuanian ses/os6s.: Old Church Slavic sestb; Tocharian A 
skast, B skaste. 

It seems from PIE root lemma for number six was spread to Semitic system: 
East: Akkadian+ shishshu. Central: Arabic sittah, Saud/ sWia, Yemen/ sltteh, Syr/an s^ie, 
Lebanese sett\, Cypr/otsltte, /raq/s\\.ta, Egyptian s\\.\.a, E Libyan 's\\.\.a, N African (Darja) 
sitta, Moroccan SQ'i\.a, Sudanese s\\\\a, Nigerian s\\.\.e, Zanzibaris\\.\.e, Maltese sitta, 
Phoenecian+ sh-sh, Ugaritic+ t-t, Moabite+: Classical Hebrew+ shesh. Modern Hebrew 
shesh. Classical Aramaic+ shitha:h. Modern: Aramaic she:'tta:. Classical Syriac+ "eshta:, 
Syriac 'ishta, Van\shia, South: Old S. Arabian+ s-d-th. South Arabian (l-larsusi)'\\a\.\.^\\, 
{SheriJsheH., Socotra yha J, N Ettiiopic: Geez+ stddtstu, Tigre s^s, Beni Amir s\ss, Tigrinya 
shuddushte, S Ethiopic: Amharic stddtst, Argobba seddest, Harari siddisti, E Gurage 
seddest, Gafat+ seddesta, Soddo seddest, Goggot s^dd^st, Muher seddest, Masqan 
seddest, CW Gurage s^d^st, Ennemor s^d^st. 

Egyptian. Egyptian+ s-y-s-w, (Recons.) sar'saw, Coptic+ sow. 



Indo-European 

Germanic: Old Germanic+ *seks, Western: 0\6 English+ sex, Middle English+ six, English 
six, Scots sax. Old Frisian+ sex, W.Frisian seis, Frisian (Saterland) saeks, Dutcli zes, W/S 
Flemish zesse, Brabants zes. Low Saxon s6Q>, Ems/and zes, Mennonite Plautdietsch sass, 
Afrilcaans ses, Gemnan sechs. Central Bavarian sechse, Swabian sechs, Alsatian sex, 
Cimbrian seks, Rimella zhakshe, Rheinfrankisch sechs, Pennsylvania sex, 
Luxembourgeois sechs, Swiss German sachs, Yiddish zeks. Middle High Gernnan+ sehs. 
Old High German+ sehs. Northern: Ruu\c+ saex. Old Norse+ sex, Norwegian seks, Danisli 
seks, Swedisli sex, Faroese seks. Old lcelandic+ sex, Icelandic sex. Eastern: Gothic+ 
saihs, Crimean+ seis, Italic: Oscan+ *sehs, Umbrian+ sehs-, Faliscan+ zex, Latin+ sex, 
Romance: Mozarabic+ xaix, Portuguese seis, Galician se\s, Spanish seis, Ladinosex, 
Asturian se'\s, Aragonese se\s, Catalan sis, Valencian s\s. Old French+ sis, French six, 
Walloon s\\\]\\, Jerriaiss\x, Poitevin s\s. Old Picard+ s\es, Picard s\s, Occitan (Provengal) 
sieis, Lengadocian s\e\s, Gascon s\\e\s, Auvergnats\e\, Limosins\e\, Franco-Provengal 
(Vaudois) sT, Rumantsch Grischun s\s, Sursilvan s\s, Vallader ses, Friulian sTs, Ladin sies, 
Dalnnatian+ si, Italian sei. Pied montese ses, Milanese ses, Genovesesex, Venetian s\e, 
Parmesan se-.s, Corslcan se'\, Umbriansex, Neapolitan se\e, Sicilian s\e, Romanian s,ase, 
Arumanian s,ase, Meglenite s,asi, Istriot s,ase, Sardinian ses, Celtic: Proto-Celtic+ svex, 
Gaulish+ suex, Brythonic (P-Celtic):y^e\s\\ chwech, Cardiganshire s\c\\, Breton c'hwec'h, 
Vannetaishueh, Unified Cornish+ whegh. Common hwegh, Modern\Nhee, Devonian+ 
hueh, Goidelic (Q-Celtic): 0\^ lrish+ se, Irish se, Scots Gaelic sia, Manx shey, Hellenic: 
Mycenean Greek+ we- (*wex-). Classical Greek+ hex, Greek eksi, Cyprioteks\, Tsakonian 
ekse, Tocharian: Tocharian A+ sak, Tocharian B+ skas, Albanian: Albanian gjashte, Gheg 
(Qosaj) gh'asht, 7c»s/r (7l^a/70'/7fea'y'g'ashte, Armenian: +Classical Armenian vec^, 
Armenian vec, Baltic West: Old Prussian+ *usjai. East: Lithuanian sheshi, Latvian seshi, 
Latgalian seshx, Slavic East: Russian shesth, shest'; Belarussian shesthh, shesc';
```


## [2026-09-14T03:09:08.115Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"suek\\\"uo\\|suekuo\\|sueku\\|opos\\|resin, juice\\|OTTO^\" POK_full.txt | sed -n '1,40p'",
 "description": "Grep Pokorny for the resin/juice root"
}
```


### [2026-09-14T03:09:08.188Z] TOOL RESULT

```
1105:The proposed solution 
1107:Ferdinand de Saussure proposed the existence of elements he called coefficients 
1215:for them outside the Indo-lranian branch including Sanskrit is slim. Kurytowicz proposed 
12069:argument, to maintain a proposition or statement; to sustain a part '; naGvr) (covers late, 
22428:order', Latin con-diti-oi. " an agreement, stipulation, condition, compact, proposition, 
22450:burial-place, common land, private burial-ground, something proposed as a prize, case 
22451:proposed for discussion, theme of an argument, proposition, premise, arbitrary 
37994:same kind especially xQwv : zeme, and a parallel proposed with k- '\K\\yoc, : cin. No quite 
54289:proposition for a law, motion, bill ', legare, legatus, Oscan llgud^ to bring together, gather, 
60843:propose openly, publish, promulgate '; mulctra' a milking-pail, milkpail '; 
60848:bring forward publicly, propose openly, publish, promulgate '; causative Middle Irish bluigid 
63572:OTTOJTTa 'have seen'; onlTTEuu) " gawk at, look after ', napGsvoniTTri^ " overseer of girls ' with 
65538:seasoned ' (f. nsnsipa after niwv : nisipa), nonavov ' pastry, cake'; *k"'opos in apro-Konog 
66515:precor, -a/7"bid, beg, ask', Umbrian pepurkurenfi. PI. Fut. 'poposcerint'; Gothic frafhnan^ 
74514:Schlagworten *suelio[n]-, suesor-, suekuro-s, suekru-) are: 
83506:swagur{*suekur6s) "brother-in-law (*son of father-in-law)', also "father-in-law, son-in-law'.
```


## [2026-09-14T03:09:16.370Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: sok\\|Root / lemma: sek\\|sakai\\|Harz, juice\\|resin\" POK_full.txt | sed -n '1,40p'",
 "description": "Search Pokorny for sokwos root"
}
```


### [2026-09-14T03:09:16.433Z] TOOL RESULT

```
10658:silva Bacenis " resin ' by Caesar and Middle Latin Boconia " Rhon -an area in Germany '), 
18677:loanword terva. Old English teoruu., tierwei., -avc\. "tar, resin' {*deruio-). Middle Low 
18725:pinewood; tar, resinous wood'; ablaut, Latvian darva^iaf. Old Prussian in PN Derwayn; 
20018:degotb 'tar' (from '* wood rich in resin '), as Lithuanian degutas' birch tar '; with Assimil. 
34185:zvakatb "chew', zi/a/r" larch resin as a tooth cleaning material '; 
34189:compare further g^Tu- "resin'. 
36543:Latin-Germanic glesum " amber ' = Old English giserm. " amber, resin ', Old High 
39713:Meaning: resin 
39724:ablaut Old Norse kvada\. "resin'. Old Danish kvade, Norwegian dial, kvaede^ birch juice ', 
40391:Meaning: resin 
40393:Material: Armenian A/Vm., Gen. kvoy^ resin, mastic ' ( *gfuo-), therefrom kvenT the pitch- 
40398:russ. zivfca. Lower Serbian zyiz/ica "resin'; 
60898:Germanic Mr|Ai-pOKOv opoc; "the resin'; changing through ablaut Armenian /77a/"sheep, 
65253:"resin' from: Old Indie pTtu-daru' a spruce kind ', actually " resinous tree ', and as short 
65258:Tath'c\. ("rich meadow, land' {*pei-tu-); the meaning "resin' also in the A'-derivative *pi-k-:<^'c. 
72754:saip(p)io. Old High German sei(p)fa^ soap '; also "resin'. Middle Low German sepe^ soap 
72791:Root / lemma: sek-1 
72799:Similar Root / lemma: sek-1 : to flow out, dry out (of water) : Root / lemma: seng"- : to fall, 
72933:Root / lemma: sek''-2 
73571:From Root / lemma: sek-1 : to flow out, dry out (of water) derived Root / lemma: seng"- : to 
74754:Root / lemma: sek-2 
74820:Root / lemma: sek-3 
83691:Material: Gr. onoq " plant juice, resin ', ottoek; "saftig", whereof the FN 'Ottosk; (inschr. 
83695:Latvian svakasi. PI., umgelautet svek'is, PI. si/e/r'/" resin, Gummi', Lithuanian sakaTP\.,
```


## [2026-09-14T03:09:17.983Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sweid\\|sweks\\|sekʷ\\|sekw-\\|swaidaz\" AHD_watkins1985.txt | head -40",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-14T03:09:18.043Z] TOOL RESULT

```
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
1043:swei-2. To bend, turn. 1. Germanic o-grade form *swaip- in Old English swdpan, to sweep, drive, swing: swoop. 2. Germanic zero-grade form *swip- in Old English swift, swift, quick (< “turning quickly”): swirtT. 3. Germanic full-grade form *swif- in Middle English swyvel, a swivel: SWIVEL. 4. Possibly Germanic *swih- in Middle Dutch swijch, bough, twig: SWITCH. 5. German schwappen, to flap, splash, akin to the source of Middle English swap- pen, to splash: swaP. [Pok. swei- 1041.] sweid-'. To shine. Possible suffixed form *sweid-es- in: a. Latin sidus, constellation, star: SIDEREAL; b. Latin augury terms considerdre, to examine, “observe the stars carefully” (con-, intensive prefix; see kom), and déside- rare, to long for, investigate (formed on analogy with considerdre; dé-, from; see de-): CONSIDER, DESIRE. [Pok. 1. sueid- 1042.] sweid-2. Sweat; to sweat. I.O-grade form *swoid-. 1. Germanic *swaitaz, sweat, with its denominative *swaitjan, to sweat, in Old English sw&tan, to sweat: SWEAT. 2. Suffixed form *swoid-os- in Latin sidor, sweat: SUDORIFIC; SUDORIFEROUS. 3. O-grade form *swoid-d- in Latin siddre, to sweat: SUDATORIUM, SUINT; EXUDE, TRANSUDE. II. Suffixed zero-grade form *swid-r-os- in Greek hidrds, sweat: HIDROSIS. [Pok. 2. sueid- 1043.]
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
1263:ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL  sel-4 ASSAY ag- ASSEMBLE sem-! ASSENT sent- ASSERT ser-3 ASSESS sed-1 ASSET sa- ASSEVERATE weéro- assIDUOUS_ sed-1 ASSIGN sekw-1 ASSIMILATE sem-1 ASSIST sta- ASSOCIATE sekw-1 ASSOIL feu-1 ASSONANCE swen- ASSORT ser-3 ASSUAGE swad- ASSUASIVE swad- ASSUME em- ASSURE cira ASTASIA sta- ASTATINE  sta- ASTER  ster-3
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1461:ENNEAD newn ENNUI od-2 ENORMOUS gn6- ENOUGH kom, nek-2 ENSEMBLE sem-! ENSIFORM nsi- ENSTATITE sta- ENSUE sekw-1 ENSURE cira
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1489:EXTRACT tragh- EXTREME eghs EXTROVERSION wer-3 EXTROVERT wer-3 EXTRUDE treud- EXUBERANT euedh- EXUBERATE euedh- EXUDE sweid-2 EXULT sel-4 EXUVIAE eu-! EYAS nizdo-
1605:HIDE! (s)keu- HIDE? (s)keu- HIDE? kei-1 HIDROSIS sweid-2 HIE kigh- HIEMAL = ghei-2 HIERARCH eis-! HIERARCHY eis-! HIERATIC  eis-1 HIERO- eis-1
1681:INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
1683:INTRA- en INTRADOS dorsum, en INTRANSIGENT ag- INTREPID  trep-1 INTRINSIC en, sekw-1 INTRO- en INTRODUCE deuk-, en INTROIT el-1, en INTROMIT en, (s)meit(a)- INTRORSE en, wer-3 INTROSPECT en, spek- INTROVERT wer-3 INTRUDE treud- INTUITION teu- INTUMESCE teue- INTUSSUSCEPTION en, kap- INULIN wel-3 INUNCTION ongw- INUNDATE wed-! INURE op-! INVADE wadh-2 INVAGINATE wag- INVALID! = wal- INVALID2  wal- INVEIGH wegh- INVEIGLE okw- INVENT gWa- INVERT wer-3 INVEST wes-4 INVETERATE wet-2 INVOKE wekw- INVOLVE wel-3 INWARD wer-3 IODOPSIN  okw-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2143:PURBLIND bhel-' PURCHASE per! PURE peue- PURFLE gWhi- PURGE peue- PURITAN peua- PURLOIN del-1 PURPORT per-2 PURSE bursa PURSLANE porko- PURSUE sekw-1 PURULENT pu-2 PUS pu-2
2180:REQUIEM kWeie-2 REQUIESCAT kWeia-2 REQUIRE quaerere REREDOS dorsum, re- RESCIND skei- RESCRIPT skribh- RESCUE kwét- RESEAU  era-2 RESECT sek- RESEMBLE sem-! RESENT sent- RESERVE ser-1 RESERVOIR ser-1 RESIDE sed-! RESIGN sekw-1 RESILE sel-4 RESIST sta- RESOLVE leu-1 RESORB srebh- RESOUND swen- RESPECT spek- RESPIRE spirare RESPITE spek- RESPLENDENT spel-2 RESPOND _spend- REST? sta- RESTITUTE sta- RESTIVE sta- RESTORE sta- RESTRICT  streig- RESULT sel-4 RESUME em- RESUSCITATE kei-3 RETAIN ten- RETALIATE telo- RETCH ker-2
2208:SAG sengw- SAGA sekw-3 SAGACIOUS sag- SAGE! sep-1 SAGE? sol- SAINFOIN dh@(i)-, sano- SAINT sak- SAKE! sag-
2221:SAY sekw-3
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2230:sEccO seikw- SECEDE ked-, s(w)e- SECERN krel-, s(w)e- SECLUDE kleu-%, s(w)e- SECOND2 sekw.-1 SECONDO sekw-1 SECRET krel-, s(w)e- -SECT sek-, sekw-1 SECTILE sek- SECTION sek- SECTOR sek- SECUND sekw-1 SECUNDINES sekw-1 SECURE cilirra, s(w)e- SEDATE! sed-1 SEDENTARY sed-1 SEDERUNT sed-1 SEDGE sek- SEDILIA sed-1 SEDIMENT sed-1 SEDITION ei-1, s(w)e- SEDUCE deuk-, s(w)e- SEE] sekw.2
2236:SEETHE seut- SEGMENT sek- SEGNO  sekw-1 SEGREGATE ger-1, s(w)e- SEGUE sekw-1 SEGUIDILLA sekw-1 SEICENTO dekm, s(w)eks SEIGNIOR sen- SEISIN sag-
2248:SEPTUPLE pel-3, septm SEPULCHER sep-2 SEPULTURE sep-2 SEQUACIOUS sekw-i SEQUEL sekw-1 SEQUENCE sekw-1 SEQUESTER sekw-1
2249:SEQUESTRUM sekw-1 SERAC ser-2 SERE! saus- SERENE ksero- SERF servus SERGEANT servus SERIES ser-3 SERIF skribh- SERIOUS swer-5 SERMON ser-3 SEROTINOUS sé@-2 SERPENT serp-2 SERPIGO serp-2 SERRIED ser-3 SERTULARIAN ser-3 SERUM ser-2 SERVAL_ ker-! SERVE servus SERVICE servus SERVILE servus SERVITUDE servus SESQUI- kwe, sémi- SESQUIPEDALIAN ped-! SESSILE sed-1 SESSION sed-1 SESTERCE sémi-, trei- SESTET s(w)eks SESTINA s(w)eks SET! sed-1 SETTLE sed-1 SEVEN septm SEVER pere-! SEVERAL pere-1 SEVERE WEér0- SEW syu-
2255:SIDE sé-2 SIDEREAL sweid-1 SIEGE sed-1 SIEGFRIED pri-, segh- SIEROZEM dhghem- SIEVE seib-
2257:SIGHT sekw-2 SIGN sekw-1 SIGNORY sen-1 SIKH kak-1 SILENT si-lo- SILL swel-3
2268:SITZMARK sed-1 SIX s(w)eks SKALD sekw-3 SKATOLE sker-4 SKEAN skei- SKEET skeud- SKELETON skele- SKEPTIC spek- SKI skei- SKIAGRAM skeei- SKIASCOPE skeei- SKIFF skipam SKIJORING geue- SKILL skel-1 SKIN sek- SKIPPER! skipam SKIRMISH sker-1 SKIRT sker-1 SKIVE skei- SKOAL skel-1 SKY (s)keu- SLAB? leb-1 SLACK! slég- SLAG slak- SLAM! leb-1 SLAP leb-1
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
2324:SUCK seue-2 SUCTION seue-2 SUCTORIAL seue-2 SUDATORIUM sweid-2 SUDDEN ei-1 SUDORIFEROUS sweid-2 SUDORIFIC sweid-2 suDs_ seut-
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
2402:TRANSIENT ei-1, tera-2 TRANSIT ei-1 TRANSITIVE ei-1 TRANSLATE tele- TRANSLITERATE deph- TRANSLUCENT leuk- TRANSMIT (s)meit(@)- TRANSMUTE mei-1 TRANSOM tere-2 TRANSPIRE § spirare TRANSPONTINE pent- TRANSPORT per-2 TRANSUDE sweid-2 TRANSVERSE wer-3 TRAP! der-1
```


## [2026-09-14T03:09:25.458Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '83680,83725p' POK_full.txt",
 "description": "Pokorny sekw/resin root"
}
```


### [2026-09-14T03:09:25.512Z] TOOL RESULT

```
Etruscan+ sa 

References: WP. II 522 f., WH. II 528 f., Wackernagel-Debrunner III 355 f., Ross TPS 
1944, 54 f. 
Page(s): 1 044 

Root / lemma: s(u)elro-s 

Meaning: sap, pitch, *blood 

Material: Gr. onoq " plant juice, resin ', ottoek; "saftig", whereof the FN 'Ottosk; (inschr. 

/TonovTiojv); 

Latvian svakasi. PI., umgelautet svek'is, PI. si/e/r'/" resin, Gummi', Lithuanian sakaTP\., 
Old Prussian sack/s6s. "juice, sap of the plant and FriJchte'; with transference aufs 
tierische russ. osoka^ blood pus ', kir. posoka^b\oo6 of an animal' and alb. gjak^b\oo6\ 

Note: 

Alb. {*sak) gJaku^b\oo(y [common alb. s- > 5/- shift]. Clearly alb. cognate derived from 
Latin sanguis -inism. (and sanguen, n.) 'blood. Transf. blood-relationship, race, family, 
progeny; life-blood, strength, vigor'. 

Also gr. {*sa/na) alpa "blood'. Old High German se/m^ honey ', Sansk. 50/773 "blood of 
animals, sap of plants, soma plant, intoxicating drink' 

From PIE the word for blood passed to Altaic languages: 

Protoform: *segu 
Meaning: healthy; blood 
Turkic protoform: *sag 
Mongolian protoform: *saji(n) 
Tungus protoform: *segV- 
Korean protoform: *sa'6-nab- 

Japanese protoform: *suku-jaka 

References: WP. II 515 f., WH. II 623, Trautmann 248, Vasmer2, 688. 
Page(s): 1 044 



Root / lemma: suel-l(k-)
```


## [2026-09-14T03:09:26.367Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"opium\\|OPIUM\" AHD_watkins1985.txt | head -10",
 "description": "Grep AHD for opium"
}
```


### [2026-09-14T03:09:26.428Z] TOOL RESULT

```
1988:OPINION op-* OPISTHOBRANCH epi OPISTHOGNATHOUS epi OPIUM s(w)ok"o- OPPORTUNE per-2 OPPOSE apo- OPPRESS per-5 OPPROBRIUM bher-1 OPPUGN peuk- OPSIN OkW-
```


## [2026-09-14T03:09:31.584Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"s(w)ok\" AHD_watkins1985.txt | head -5 && echo \"---\" && grep -o \"s(w)ok[^.]*\\. [^[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -5",
 "description": "AHD s(w)okwo- entry"
}
```


### [2026-09-14T03:09:31.671Z] TOOL RESULT

```
1057:swo-. Pronominal stem; so. Derivative of s(w)e-. 1. Ger- manic *swa- in: a. Old English swd, so: sol; b. Germanic compound *swa-lik-, “so like,” of the same kind (*/ik-, same; see lik-), in Old English swylc, such: sucH. 2. Ad- verbial form *swai in Latin si, if, in quasi (quam, as; see kWo- + si, if): NISI, QUASI. [In Pok. 2. seu- 882.] s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.] swombho-. Spongy. Germanic *swamba- in: a. Middle Low German sump, swamp: SUMP; b. Low German zwamp, swamp, akin to the Low German source of swamp. [Pok. suomb(hjo-s 1052.]
1988:OPINION op-* OPISTHOBRANCH epi OPISTHOGNATHOUS epi OPIUM s(w)ok"o- OPPORTUNE per-2 OPPOSE apo- OPPRESS per-5 OPPROBRIUM bher-1 OPPUGN peuk- OPSIN OkW-
---
s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.]
```


## [2026-09-14T03:09:59.170Z] TOOL CALL #18: Bash

```json
{
 "command": "ls tools/ && sed -n '1,40p' tools/ref_page.py",
 "description": "List tools"
}
```


### [2026-09-14T03:09:59.233Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
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
```


## [2026-09-14T03:10:00.736Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xvaeda\\|x'aeda\\|xvaeza\\|hvaeda\" BRT.txt | head -20; echo \"---xsvas---\"; grep -n \"xsvas\\|x'svas\\|xšvaš\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-14T03:10:00.807Z] TOOL RESULT

```
---xsvas---
4251:•  j.  anaiKm  Adv.  'in  der  Quere':  cvat. . äps  yat  frätal,car}tayä  .  .  druxi .  .  /ras- naoilit .  .  ^rigäim  nyäpim  navagaim  pait- ySp}m  xsvas^aim  an'  ".  .  drei  Schritte stromabwärts,  neun  stromaufwärts,  sechs quer  über  den  Strom"  V.  tf.40.
12661:—  xsvastlm  ^maibysihmahe  (sd.)  HstryAe •%uis  K3.Z^;  7^.
14504:a)  Am,'*:  nava  p^r^'^wS  (sd.)  ksrmava  .. xsvas. .  tisrS  V.  2.30 ;  — pairiJtanm  ^  pairi.- kärt^flis  iisrS  yat  vS  xsval  .  .  akummca vairXm^  frasravaySis  tisrS yat  vä  xsvaS .. V.i7.6.  ß)  als  An.^':  tisrS  sota  upa-
16617:auf  länger  als  — '  (Abi.);  ^cvat  *aiwiitJm parayal  .  .  ka^irakjm  (sd.)  *xsvas  xiafhS -  ■  y^  'y^  aitahmät  paräiti  ftöil  pascalia 1  anaiwisIXm  äsltyanti  ".  .  wenn  er  noch i  auf  länger  als  diese  Frist  weggehen  soll, . ."
20527:•  i-i  St  P-"  mi^ra-,  p.  "mitra-"'  m.  'Ver- trag, Abmachung,  Konliakt':  "rim  mä janyä  .  .  Mvaya  tT  asti  (Sp.  270  U.)  'rS drvataäa  asaona^a  Yt.  70.  a ;  —  laiti  aSe 'ra  tava  yat  ahurahe  masdsl  äat  mraot ahurS . .:  xsvas. .  vacaAind . .  sasf3.tnaräs . . pasu.mazS  .  .  staorö.mazB  .  .  vlrS.masS  .  . dai}ihu,mazS  V,  4L  2;  —  vacB paoirim  'nm karmaoiti  *zasts.maz3  alät  framansaiti *zastö.masö  atiät  antan  urvaitya^sA.)  /ra- daäiaiti  y.4-Z'i  —  Äaj'  agiO  'rB  aiwi- druxtö  ästäraili  yB  vacalünB  V.  4.5;  — yö  'nm  aiwt.druzaiti  ytm  vaeahimm  V, 4. 1 1 ;  —  s.  noch  Yt  10. 3,  45, 14. 47,  V. 4.  54  unter  A  n.  a)  im  gAw.  'reli- giöse Bindung,  Verpflichtung':  yS . .  drltä ayanUtn  urvätöis  (sd.)  vä  .  .  'rBibyS  vä \.46.  5.  A)  als  Gottheit*';  1)  im  Ap.: mSm  a'ura^maxdä  utä  °'^r<^  bage^  pätuv Ao.  /.  4;  —  J'urJ'mazdä''  ^anahitc^  utä "'trJ'  Am.4''i  i  i'>ra*).  II)  im  jAw. (yazata-) :  kö  'rtm  aiwi.drusaiti  ks  rasnüm paifijrinaxti  Yt  14-  47;  10.  45;  —  äsu.- aspim  dacäiH  'rö  .  .  ysi  'nm  nsit  aiwi.- druUnti  Yt  ro.  3 ;  —  rasnaoSca  paitLsanfam 'raheca  aiwi.drux/3m  (sd.)  V.  4. 54; — yai vä  dim  aiwLdrusaiti  . .  /rasa  upajcanda- yäti  'rB  grantB  upaJbUtB  Uta  nmämm  .  . Yt/0. 18;  19;  —  apa  HB  haca  azaaAat ,  .  'ra  barBis  anädruxtB  Yt  10.  23;  —  t^sa mainyete  dus:^ar3nä  nSit  vlsp?m  aiwi.- druxtse  'rB  vamaitt  apifma  Yt  70.105; — ■  satayus  antan  pitan  pu^rtmla  . .  asti 'rJYLio.  117;  116;  —  tOm  akB  vakUlasia 'ra  ahi  daiAhuby5..tBm  axstöii  anäxitBiita 'ra  xSayehe  dahyunqm  Yt70.  39;  29;  — tbiHahecil  axlnultahe  (sd.)  °ra  (IS.)  mata rämayeiti  huxsnüitlm  paiti  'rahe  , .  xsiiB- taAe^it  albiHahe  (sd.)  °ra  manB  yaozayäti ax/nßitlm  paiti  *raAeYtio.iog— 111;  120; —  'raAe  da&yunam  dai^hupatsU  Y.  /,  1 1 ; 2.  II,  Yt/0. 145,  75.35;  —  äea  nB  jamyät avahyäi  uyrB  aiwi'^Urd  ..'rB  ralva  dai^hu- paitii  Yt  10.  78;  —  'nm  aiwi.dahyüm  . . 'nm  antar».daRyüm  'rtm  ä.daRyäm  . .  Yt 10.  144;  144*;  —  ci>rä  'rahe/rayana  yasj tarn  da^Bm  slaraitt  ..  Yt  iO.  112;  — kaaa   nB   aria  gavai^im    apayst  paskst
21947:6av3t  V.J.  19;  —  nairyh  v  pu%raAe  v haeyh  V  marfuyä  Y.ii.i; — yesi  a/sAaf upaOPm  V  aiwinaptlm  v°  . .  V  .  .  f  V. 7,  la;  —  pä^a  ayantim  v'  taBnhm  V V  ..V  V.6.26;  —  tiraos  v°  paiii  sBinma umm  V'  kaiat  V  paiti  siäaranqm  N.  loo; —  vännti  V  snaszinti  v°  bannti  v'  tima- nAqm  V  *aiwi^ais (sd.)  ayqn  v ..vantö. vire  (sd.)  jas»nti  V.  iV.  4;  —  yS  tat  draons ainät  t/'  tn/yät  v° apa  v yäsäiüY.ii.S',  — yS  gatwqm  ..janaiti  v  vayät'i  »*,.  v'  ,.V V-Zj.  5;*—  ferner:  Y.  (j2.  9,  Yt.4.4,  8.\\, JO.18,  J/.4,  75.50,  V.^.  44,  5.5, 12,27,45, 57,  6.46,  8.2,  12,  ß.  II,  y.37,  i4. 17. ^5-9.  14.  z»y-53.N.J5,  26',  J7,  P.i'/,  VyLJO, 2^\  —  s.  noch  Anhang  2;  —  im  Wechsel mW.  yai  vä  (Sp.  1261  f.):  hris  v  /ämaa yat  vä  xsvas  yat  vä  nava  V.5.  51;  — andus  v3  ayryS.siaonm  v*  bistaorfm  V yat  matauhsm  v a  3^ar?m  N, 45^^-  zu  Z ) ; b)  im  gAw.:  yä  nsitv'  aaiat(Sp.  271  u.) aKiAain  V  Y.31.  5.  c)  im  jAw.:  Aatci^ (Sp.  592  u.)  V  nsit  v°  \t.l4.2o; — yaf apirmäyüks  sraoüi^^  v'  anu.tacaiti  aoxtö (sd.)  V  hl  aoxte  . .  N.  7;  —  y!J  gä^anqm anttmaiti  (sd.)  V  * anumainyete  ainyehs  V srävayantö  paitistanti  (sd.)  anyS  V  hi dahmS  . .  "wemi  einer  . .  oder  wenn  er  . . oder  wenn  ihm  . ."  N.  25;  —  in  weiter Trennung^);  yat  .  .  spä  avaci  (sd.)  V aonityS.xratu^  . .  yai . .  spä  ahqm.baöh>mnS (sd.)  v°  bavat  ähäityS.xratus  "wenn .  ■  einer- seits , .,  wenn  . .  anderseits  . ."  V.  j_j,  29 und  35.  Anhang.  /)  Eine  Ellipse  liegt vor  in:  katärSm  ä  angrH  (Sp.  104  u.)  väi hvB  v  ar^rö  yS ..  ". .  der  Feind?  (Ist  er auf  dieser  Seite)  oder  ist  der  der  Feind, der  . ."  Y.  44. 1 2.  2)  Ausgefallen  ( ) ist  »a  an  folgenden  jAw.Stelienj  zu  IUI  1: daSvayasnäi  v°  tanupirikät  (w)  'Ü.16;  — näirikqm  V  *apßrmäyBi^m  (v)  N.  105; —  pas/a  v* paiti {v) ..'H.gs.  zullll  a: pure  v°  puäiräi  {v)  brähre  v°  Yt  14. 46;  —  mit  ungleich  gebauten  Gliedern: AvSiitö  v° ydiste  {v')  yi/it  V  ainim..cayqn N.  J.  zu  m  2 :  yai  arastr^m  (sd.)  pairi.- a^a  v°  *vaca  (»•)  *apayaiiti  (Sp.  190  o.) aratufrya  N,_52.
22272:pars  vay&ibyö^'*  YLjo.88; —  *ao^rab}'B ariuxialibyasca  vSyiibyB^^  vufitn  .  . yazatitn  yasamaide  Y,i6.  i;  Vi.  6.  i,  Ny, J.  1 6;  —  Avamxiaft?m .  .yaxamaide  vacaca ^ao^naca  sao^rabyasca  N.1.16.  5)  Sing. JcaT*  K.  oder  mit  arsuxZa-,  miuxZa-  sva. mq'^ra-  (Sp.  1178  o.),  'das  Wort,  das wahlgesprochene  Wort':  yä^a  lia  väHm Milma  (Sp.  1067  o.)  ya'^a  vä  saoiyatits Y.  70. 4;  —  zara%uitrahe  .  .  yS  paoiryS vacim  aoxta  vldsyum  akurS.tkaistnt  Yt. y.go;  90;  —  ^TKuxlam  vacim  yat  frä- dai^gat^gm  yasamaide  S.  2.  iS'"';  G.  2.  6; —  uita  tl  nsii  pairi.frasa  (sd.)  >rpzuxhm *p?rgsahi  VäHm  Y.g.as.  6)  "Einzel- wort,  (Plur.)  Wörter'  uzw.  der  GiJhäs"'>: tiiranam  haurva.paoiryanqm  (sd.)  häiliSla afsmanäca  vacasca  va^astaslim{sA.)ca  Vr. y.  3;  —  *ey3mcit  .  .  väcitn  gä^anqm asrvUm  (sd.)  N.  103;  — yS  gä^anqm  Byam vScim  afayäiti  alvqnt  v3  vacastaltXm  N. 4s\  42;  — ys  asnitgaoia  v3  ajravaoco  va nBii  Sim  Smm  väcim  *aiwyHs  (Sp.  378  0.)  \ .  .  yezi  äat  Syumpt  *väam  *aiwyas  1 anaiwilfi  (sd.)  astryeite  N.  i4-  Undeut- liche oder  wertlose  Stellen:  sar^yO  vaxs FrW.fj.i;  —'kaityavaca  FrW.5.2; — yS kaca  damayät . .*apastv6it  '^rilvayzibis^'^ ^haktni. .  N. 41 "';  —  xsvas  vayeibis^i N. 6j,  /OJ'J';  —  aAunavaitim  gshqm  .  .yasa- maide..  mal  vay£iby3^Va'*>  *pdübyasca V1.14.1;  YLz,  II,  13  (vacqm).  S.  noch vacim  bes.
25912:—  'tun  iayalanqm  YtiO,  2;  —  -Dm paitiitanam  hatargrim  . .  baivari  V.j.31; Yt5.2i.'5.3,  ;j.7i,  H.j.s,  sVar„8,  Yt, ig.d;  —  %rii 'tat! käta.H%anqm  "mit  drei mal  hundert . ."  V.4.  5;  Wytig.  a)  mit attrib.  Einerzahlen":  ca'^warasca . . garays cahwarpsat3m(sd.)ia  dvaica  °ite  (ND.) dvaica  hazanre  Ytjp.  7;  —  %räyS  *°la (NP.)  F.  2j;  —  yä  ..  vazinH  xsvas  *°tais'' (ab  Nom.)  haxarfnnila  Yt  5.  95;  — navaca  yaskS  navaitlsca  navaca  °ta  navaia hatatira  rtavasJs(,sd.ya  baevqn  V.  22,  z;  Yt. ^.?-  S9-  ^)  ™''  Gen.:  duye  °ite  kakyä- Ht  .  .  xrafstranqm  V.  16.  12;  4.  2i';  — tisrS  'ta  upätananqm  V.  4. 1 1 ;  1 1 ;  — ia%w3rS  'tu  äirpjaokanqm  V.<?.  84;  ff.  21';
25913:—  panea  'ta  upäsananqm  V.J.  36;  36,  ä 83,  *F.  10;  —  xsvas  'taif  Aala.H'kanqm  V. 4-(>;  13';  —  hapita  'ta  us'tranqm  Ytg. 30; V.4.7,  13';  —  aita  'ta  upusananqm  V. 4. 14;  14,  8;  —  ye^ke  avavat  hatnanqtn (sd.)  «(wa  **W(/  (als  Nom.)  hasatirimea Yt.5. 120;  V.4.9,  15'.  b)  adjekL  ge- braucht: Äfl^ra.._yiisfl/'aÄ^jiT.,^anfaj(i/to"o Hailca  hazanraisca  Vr.  Ä  i.  a)  mit attiib.  Einerzahlen:  hazatanm  narqtn  .  . iaoxma  . .  xlvas  'ta  . .  tisrS  'ta  (als  Gen.) "den  Samen  von  1000  Männern  . .  von 600  . .  von  300"  V.  2. 30.
27343:(sd.)  möi  Y._57. 11;  ��  surunuyS  nd  .. yasnahe  xlnuya  nS  . .  yasnahe  YL 10. 3a; —  surunaoiti  saota  upa.sraotaranqm  N. 21.  Ausser  Zusammenhang:  smnaoiti, sravat  F. /2"*.  II)  Kaus,  ('etwas  zu Gehör  bringen'  sva.)  i)  'verkünden, predigen':  tnrüiti  yS  v3  xraffui  xsms- kakyS  a.mananhä  (sd.)  jr?/  vjHdyai (sd.)  yd^ä  r  srSvayaema  Y.  49.  6 ;  — s.  noch  In£  2)  'aufsagen,  rezitiren'; Med.  in  pass.  Sinn;  als  PPfP.  dazu  dient sruta-:  srävaylH! staola yesnya  P. /J;  —  yä ahmät  staoia  yasnya  srävaymi  ahuiam'a vairfm  srävayeni  astmca  vahist»m  ^husra- vSm  (sd. )  Ny.4. 8 ;  —  yeti . .  xsvas  vaAiärm {sA)*srävayätiü.^o; — yasca  ml..bayqm ahunake  vairyehe .  ./rä  vä  drsn/ayö  sräva- yäi  fra  va  srSvayS  {Sp.  1642  o.)  yatäite Y.lff.6;  —  srävayamnät  paiti  ahunät vairyat  A.  4.  j ;  —  Hä  ml  6aya  afatnahe vairyehe ..  anapyB^a  {&A)  anapisüta  srä- vayamna  Y.ig.y,  y,^yaozdä^r?m  srä- vaySil  "du  sollst  die  Purifikation  (auf- sagen sva.)  durch  Aufsagen  (der  dafilr vorgeschriebenen  Formeln)  vollziehen"  V, u.  2  '^.  insbes.  a)  vom  Au&agen  der Gä%ä%:  ahnyästa  matdayasna  gä^ä  srä- vaya/ nSii  anaiwyasta  (sA.)  N-A^;  — yBi .  .  matüyanqm  (sd.)  parä  s^arHöit  *gä^ä nöii  *sravayeinti  N.  25;  26",  *J7 '",  V./Äj;
28369:paoiryehe    *mt^Sxtaht    Jrf    *malsma.- samqn    asamst    bityeke    *xsvas  .  .   "beim
29801:Anfang  der  Vers  abschnitte  s.  Bthl.  af.  3.  i  Verdienst  im  Gedächtnis  hast,  O  M.,  du 23.  —  3) Tu.:  ia  iFnin  i  Jrvttm/än.. ei  daiänlvf sisst   CS    durch    den    besten    Sinn"   Y. ^ästär  .  .  atiänik'ik.     Undeutlich.  —  4)  Oder  |_^2.  6;  —  xsvas.dasa   'rmis"  Yt,  I.  8. ■^  larätiay-,    'martnay-   Adj.,   imn   V.  >
```


## [2026-09-14T03:10:07.702Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Schweiss\\|Schweiß\\|Schweifi\\|Schwei.\" BRT.txt | head -20",
 "description": "Grep BRT for Schweiss"
}
```


### [2026-09-14T03:10:07.754Z] TOOL RESULT

```
11210:•)  Sva.  paiuia-,  sÄ  und  vgl.  ratascarat:  — Als  Repräsentanten  dieser  Tiecklasse  werden Bd.  14.  6  fiock,  Schaf,  Kamel,  Schwein,  Pferd und  Esel  genannt;  s.  dazu  Yt.  14.  7,  9,  II,  15, 13,  aS-  Als  ihr  Ratav  gilt  nach  Pü.  zu  Vr.  /.  1 und  Bd.  34,  a  der  'weisse  Eselbock'  {xar  iüi  i
16417:•  j.  pisra-  m.  Bezeichnung  einer  Vor-  ^,^.^,^  ,^^  ^^J/^^^^aiW"  (sd.)  V.  5. nchtung  zum  Schweissen  von  MetaUen:  ^  ^)  '(Ausgequetschtes  sva.)  MehT: -rai  hüca  zaranyöaa!j,ät  . .  'rat  haca  ,r>-  ^^^  ,^^  ^  ^^  ia?  darva  «ru^J  "wenn ,aii^.sa^äi  'rat  haca  «ySsji^Pät .  .  'rai^;^  ^j^j^j  ^^^  Teiganmachen)  zurecht haca  haosaJnam5.,a^ilt  V.  8.  87-90.  ,  gelegt  wird,  dann  heulen  die  D."  V.  j.32.
20587:•)  Neben  jlsay,  dem  Dahia  der  Gier,  elwit als  Hexe  der  Habsucht  od.  dgl.  zu  fa^isen.  Bd. 5.  2,  28.  44  erscheint  duidin  müs  parlk  (so  28) 'die  diebische  P.  MüP,  die  als  dambömand  'mit einem  Schweif  verseben'(s,  ■Eapairikä-\  beieichnet wird,  in  Verbindung  mit  den  Planeten  als  Feind von  Sonn*,  Mond  und  Sternen.
22822:'varäza-  m.  'Männchen  des  Schweins, Verbindung  mit  dem  Namen  für
22824:Schwein"':  As(sd.)  k»hrpa  'zähe , .  arÜnS*''
23514:Vgl.  värin-gan-.  —  Eig.  Bed.?  Man^  hat  den Vogel  Damen  mit  'flügelschlagend'  überaetit nnd  für  *3i'J/'-  auf  np.  fj/ 'Feder,  Flügel'  nnd ai.  J-äta-  m.  verwiesen;  5.  Sp.  Komm.  3.  1Ö4, Heu.  KZ.  27.  607.  Aber  ai.  vära-  bedeutet 'Schweifhaar',  bes.  des  Kosses  (wie  lit.  ialtd), und  np,  bäl  ist  vielmehr  gleich  ai.  barha-  [v') 'Schwan ife der"  lu  seWen,  Ander»  jetii  Richtir IF.  p.  185.  —  Npü.:  fehlt.  —  II  Welche»? Falsch  Dst.  ZA.  z.  566;  vgl.  Hbm.  PSi.  87. HoRN  GlrPh.  7  b.  56.  —  '}  Them.
25778:•  j.  saipa-  m.  'Schweissen,  Schmelze' (von  Metallen).
30138:•  j.  hQ-  'Schwein,  Sau':  ahmai  . .  ajasai vinhrafnS  hü  (GS.)'^  kthrpa  varätahe (sd.)  .  .  arins  ".  .  in  der  Gestalt  eines Ebers  .  ."  Yt./rf.  15.
30174:VJ(AP.),  •ralibyU,  'ranqm  -.  Unklar: nSii  ^mairyeke  nSi^  Jahtkayh  tait  sünü  tOii 'rahe''>  V.io. Ableit  —  d.  lui/aträ-  Adj.  —  VgL  den  ^, EN. 'OJ«Vlt  1*- —  Pü. :  »"fl/üi ;  s,  noch  No.  3.— 0  iSt  s.  Bthl.  KZ.  aS.  11;  weitere  Litt,  bei JusTi  PrJ.  S8.  247,  woEu  noch  Gdn.  BB.  13. 9tS.  —  1)  Scheint  ein  andres  Wort  verdrängt lu  haben;  Pü.:  AüA  'Schwein'.  Dst.  ZA.  j. SS  vriU  freilich  "le  roi  des  porcs".  —  3)  S. übrigens  zu  uxsya{jr>la-.
30564:Zum  V.  sna:  —  Pü.;  husnjyinaklh  -  SQ.; msanmä»atänämni  ~,  mit  der  Erl.:  man  t^Ü kac    tan    api    ajiöl;     also  'Schweiss';    vgl.  zu
```


## [2026-09-14T03:10:08.776Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'sechs'\\|sechs\" BRT.txt | head -20",
 "description": "Grep BRT for sechs"
}
```


### [2026-09-14T03:10:08.873Z] TOOL RESULT

```
4251:•  j.  anaiKm  Adv.  'in  der  Quere':  cvat. . äps  yat  frätal,car}tayä  .  .  druxi .  .  /ras- naoilit .  .  ^rigäim  nyäpim  navagaim  pait- ySp}m  xsvas^aim  an'  ".  .  drei  Schritte stromabwärts,  neun  stromaufwärts,  sechs quer  über  den  Strom"  V.  tf.40.
10884:•  j.  xStva-  Adj.  (fem.  °tvl-)  'der  sechste': akmSi  'tvö  äjasat ..  vjr^iraynS'Yt.i4.iT, 1.7,  15.2,  V.4.2,  N.  102;  —  'tarn  astaiiqm syaoimanqm  V.4.28;  1.8,  5.29,  30,  p.';, 28,  Y.p.2i,N.i'2,  F.j  (wo  '/um);  —  'tia- ht'a  ..  myazdake  A.^.  12;  —  tüirya  'hart- var»  ,  .  puxZa  tainäus  .  .  °tvT  fradaxsana V. /.^.g;  Vd.  72'>.  a)  ASn.  'tum  als Adv.  'beim  sechsten  Mal':  V.4.19,  23, S.Tl-
10957:•  j.  "xävaä')  indekl  Zw.  'sechs':  i^aitt  aäe tnthra  .  .t  xfi  (als  Nom.)  V.4.1;  9.34, i(7.9«;  —  a^  (als  Akk.)  x^aßt5  ■^,  4; V.  2.  30,  J.51,  7.1S,  p.ii,  32  PüZ.  (?}, /3.8,  14-i-A,  15-45.  ^7-6",  YL4.6,  F./, N.50,  *P.9,  Vd._9;  —  *j^  (als  Instr.) vayzibii'V.6y,i03;  —  xi^  sota  V.2.30, 4.12';  —  xs'  sa/äis'V.4.6,  ■^t.j.gs'».
10959:•  j.  *xSva8  Adv.  'sechsmal' :  W/  frasnä- ^ym  maismaaa  . .  %ri^  . .  ca%ru/.  .  x/°
10961:•  j.  x$va$.aSi-  Adj.  'mit  sechs  Augen': ailm  äahskim  ..  "hrikamsr^im  'sXm  Y.g.8.
10963:•  j.  xSva$.karäa-  n.  'durch  sechs  parallele Furchstriche  hergestellte  Abgrenzung":  •«. /raiJraya/i  Yt4.6.
10965:•  j.  xiSvaä.gäya-  n.  'Längenausdehnung von  sechs  Schritten,  sechs  Schrittlängen': 'gäin  JhmJtffai/i  la%rusanqm'V,6.^i;AO.
10967:•  j.  xdvaS.xSapar-  n.  'Zeit  von  sechs Nächten,  d.  i.  Tagen  und  Nächten':  pasca 'Parst^^  "nach  Verlauf  von  sechs  Tagen und  Nächten"  V.ß.34.
10978:•  j.  xSvaä.mäbya-  Adj.  'sechs  Monate dauernd';  upas.puhrlm  . .  atvS.mäkim  (sd.)
10980:•  j.  x5va§.satö.-zyain-"  m.,  Pltir.  'sechs- hundert Winter':  aa$yimäi  xsakrai  *°zima (NP.)  *kmjas>nta  V.2.12.
10982:•  j.  x^vazaya  Adv.  'sechsmal':  spumm  . . iayaüil  tata    aai  pa%ä    vJväoayantu    V.
10985:•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
12711:•  j.  daiähu.maza-  Adj.  'durch  Verpfän- dung eines  Land(stiick)s  geschlossen',  von mihra-  m.  'Vertrag'*':  x^H  (nämU  mi^rS) '^  "die  sechste  (Art  des  Vertrags  wird) durch  Verpfändung  eines  Landstiicks  ge- schlossen" V.  ^.  2;  —  agsS  ntürS  .  .  yS 'iS  V.4.  10;  —  'gff  ahsi  framanzaiti  'tS aiiat  arttar?  urvaitya  (sd,)  fraddhaiH  V. ^.4; — yS  rni'hfvttt  aiwidiruiaili  yim  °sw» V.4.  16.
14558:VeI.  S  'J?  s  mit  No.  1  und  \y''kahe   sechs  Monate  muss  man  für  einen -  Pa.:  tatsiian,  (für  PPfP.)i  pa  I  (jungen)  Hund,  sieben  Jahre  fUr  ein  Kind
17822:sae^antätvirshraynaiY.  26. 10; — gSuicä hudätahs  gayehyäcä  mard^nB  .  .  °itm  Y. y-  7;  2j.  a,  26.  S,  Yt  13.  87;  —  «ÄM^ zar^uStrahe  ipitämahe  asaons  -sie  Y.  6S. 22;  3. 2,  4. 23, 16. 2,  23. 2,  24-  S,  7'-  2-  Vr. /ö,  2,  YtÄ  2,  J_J.  87,  Vd.(?;  —  ahe  nars aSaonS  'Jtm  yazamaide  yS  asmffj^ativä nqma  Yt,  /. 30;  13. 95 ff.  (oft),  Y. 23. 2, 26. 5% FrW.  2. 1,  3;  —  hvSuyä  asaonyä  'sim  Yt ''5-^39!  '39f-'*;  —  kanyä  *va}>uis  asaonya [. .]  °slm  Yt  13.  141 ;  141  f.'°;  —  auch  dem AÄM.  und  andern  Gottheiten  wird  eine Fr.  KUgeschrieben**':  vispanqmca  anAqm paoiryanqm  'Sinqm  .  .  °sm  avqm  yqm ahurahe  masda  .  .  °iay5  .  .  ya  ampsanqm spintanqm  .  .  yqmca  ährö  urväzistake  .  . yqmca  sraohhe..yqmca  alnSyqmca  apH.. YtJ^.  80-86;  Y.26.2i.,  V./»?.'4; — äyese yelti  *ä  *fravaM<y)'^  ahurahe  mazdä  am»- sanqm  sparUanqm  . .  Y.  25. 2 ;  —  gaom  (statt Gen.)  agvJS-dätahe  urunB  °Sim  S.2.  I2;i2; —  sogar  den  Fravalay  selber  (!) :  aSäunqm "sinqm  uyranqm  .  .  paoiryjJkaisanqm  'si- nqrrt  nabänazdistanqm  'ünqm  '/ayU  xihaiä ayantu  ahmya  nmaneYt.i3.1s6.  A)/ra- vaHnqm  a)  (näral,  mä)  heisst  der  i .  Monat  im Jahr^:  asäunqm  'sinqmY.i. 11.  ß)(näml, ayar?)  heisst  der  19,  Monatstag:  asäunam 'sinam  uyranam  S.j.  19;  vgl. 2. 19,  Y.10.5. •)*Nach  dem  GrBd.  (s,  DsT.  ZA.  3.  500, Blocket  RHR.J2. 104)  ist  der  Mensch  aus  fünf Bestandteilen lusammengesetit:  ian,yän,  nmän, äiinai  aad /ravakr.  Vom  letzten  heisst  es; y>ti- vahr  an  i  pcs  i  Öhrmazd  i  :^aiäl,  und  über  sein Verhältnis  mm  fiß/ö»  wird  geiagt:  ruvän  S/ra. vakr  pativast,  ku  iän  rm/ä»  marnjcmtan  ne  tiniän. S.  noch  DkB.  269  {218.  6):  io  (fravahr)  haf  lan yut  bavtt  lan  hil  lör  u  aiär  mänri.  Die  Schaffung der  fr.  (bei  West;  "prolotypes,  primary  ideas of  the  good  creations")  ist  nach  Bd.  /.  8, 34.  1 zu  Beginn  des  ersten  Mitleniums  erfolgt;  nach 2.  10  f.  entscheiden  sie  sich,  'lan  tariaiihä'  gegen die  Welt  der  Driig  zu  liämpfen.  Über  ihre,  ins- besondere  kiiegeiischeTäligkeitalsSchutzgeister und  Manen  gibt  das  ihnen  gewidmete  Yt  13 Auskunft.  Ihre  Zahl  wird  Yt.  13.  59  ff.  auf  99  999 eingegeben,  vgl.  jcludra-*)  and  Mx.  4g.  16,  52. 23,  29;  weniger  bestimmt  Yt.  13.  64,  66.  All- jährlich während  der  letzten  fünf  Tage  der sechsten  (letzten)  Jahreszeit  und  der  sich  an- schliessenden fünf  Schalttage  kommen  dieManen, ihre  frühere  Heimat  zu  besuchen  (Yt.  13.  49) und  werden  dann  besonders  gefeiert  (s.  hantas- pa%niae<iaya-)ii).  Vgl.  noch  Cld.  Totenverehrung 48,  BahadoorN.  D.  Khandalawala  Cama  Mem. Vol'  205,  JN.  GIrPh.  2.  643,  SÖDEftBLOM  RHR. 3g.  229,  373,  La  vie  future  7.  Das  Nichtauf- treten  der  fr.  in  den  (eig.)  Gä%äs  (s.  unten  No.  l) ist   bemerkenswert;    zum  Teil   aber   entspricht
18163:•  j.  frädatx*ar«nah-  m.  EN.  eines  der sechs  Genossen  des  Sao^yant  bei  der  Auf- erstehung, Äa/azi  &esKarsvarJi'rad<^a/sa'^: 'nanks  alaofUS  Yt  y.  12S.
18636:Pü.;  9  pai;  5  päl  yäi.  —  i)  Nüral,  des  Rei- nigungsraumt ;  vgl.  in  der  Tafel  bei  DsT.  ZA. 3.  163  die  mit  'pieires'  bezeichneten  ausge- füllten Kreise.  Zwischen  dem  ersten  Loch für  ßindsnrin  und  der  Nordseite,  zwiscUen dem  dritten  Loch  für  Wasser  und  der  Süd- seite des  ganzen  Raums,  sowie  twischen  dem sechsten  Loch  für  Rindsnrin  und  dem  ersten für  Wasser  ist  ein  Abstand  von  je  drei  Schritt- (tva.  neun  Fuss)längeni  s.  V.  g.  ö  ff.
19526:•  j.  'maj^-  m.,  mayä-  f.'>  'Loch  im  Erd- boden, Grube':  srvabya  (sd.)  'f»m  ava.- kanöis'V.iy.T,  5,  F.i7; —  baTvari  'yanqin (GPf)  irimaitinqm  aiühh  z?mö  aipt.kan- yät  V.  14. 6.  a)  insbes.  von  den  zu Zwecken  ritueller  Reinigung  gegrabenen Lochern":  mazdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsmana  giul  *Bim  äp3  "die  Mazday. sollen  in  der  Erde  drei  Löcher  graben, zwei  Löcher  —  da  sollen  sie  mit  Rindsurin waschen  — ,  eins  —  mit  Wasser  — "  V.  76'.  1 2 ; Ä37; — paoirtm  upa  'fim  nt^w^>söis . . iitim  Ufa  . .  xltUm  upa  . .  "hrayS  anya  'ya ni^TVinssis  "ein  erstes  Loch  sollst  du  aus- stechen, ein  zweites  . .  ein  sechstes  . .  drei weitre  Löcher  sollst  du  ausstechen"  V. p.  6  ff.;  70. 18;  —  ^rJyS  yim  antari  vlta (sd.)  atitan  %räyS  {xh/as,  novo)  'ya  fra^ iärayBisY.g.  ii>;  11',  12,31; — arttanca (sd.)  .  .  'ya  (NP.)  V.p.  11;  —  karsascit frakäraySiS . .  ^ai  hala  'yaHbya  V.p.io; 29;  — paoirJfn  upa  *yim  frä.nasui  nanm (statt  NS.)  bavaiii  "am  ersten  Loch  . ." V.p.  28;  3iJ;  —  US  tansm  snayaSa  us vasirät  (statt  AP.)  gius  maSsmana  qpäca nava  (sd.)  upa  °ypm  "er  soll  seinen  Leib und  seine  Kleider  bei  den  neun  Löchern , .  waschen"  V.5.  54.
19533:(zuvor  bezeichneten   sechs)  Löchern  ge- sondert ist"  V.p.29''.
19534:*)  Ein  nach  aussen  durch  dcei  parallele  Furcb- itriche  abgegrenztes  Rechteck  auf  dem  Bodeo, Von  6  zu  16  Schritt,  auf  der  langen  Mittellinie drei  Löcher  mit  Wasser  und  sechs  mit  Rinder- bam  enthaltend.  Der  Raum  ist  zunächst  in iwei  wieder  mit  je  drei  Furchstrichen  umzogene Abteilungen  getchiedeo,  eine  kleinere  mit  den Wasser-  und  eine  grössere  mit  den  Hamlöchern. In  der  letitem  Abteilung  ist  abermals  durch drei  Furcbstiiche  an  der  den  Wasserlöchern abgekehrten  Seite  eine  Unterabteilung  mit  drei Löchern  geschaffen.  Die  Furch  st  riebe  werden  zu je  dreien  gezogen  der  Reibe  nach  l)um  die  Unter' abteilung,  3)  um  die  grössere  Abteilung,  3]  um beide  Abteilungen,  4}  um  die  kleinere  Abteilung ; Tgl.  zu  antariiür.  Dann  werden  an  bestimmten Stellen  des  Raums  Steine  od.  dgl.  niedergelegt. Vgl.Sp.  10450.  und  dieZeichnungenbeiWESTSBE. /1J.43S  und  DsT.ZA.2.  l6z  (dessen  Erliulerungen aber  nicht  stimmen).  Abweichend  Sp.  Übers,  i, Tafel  Zur  Reinigungszeremonie  s.West  aO.431. Ableit.  aut  'BiaYo-(mit  Verschiebung  des  Wort- akzents?]!),  etwa  'Raum  mit  den  Lochern'. — Pü. :  msej.  —  ■)  D.  i.  er  soll  von  der  grossem Abteilung  (PüErL  pa  gömH)  in  die  kleinere gehen.  —  *)  Ob  etwa  miy"  zu  lesen?
```


## [2026-09-14T03:10:20.105Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['BRT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['HRN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['GPL'],ensure_ascii=False,indent=1))\n\"",
 "description": "Metadata for BRT, HRN, SOD, GPL"
}
```


### [2026-09-14T03:10:21.164Z] TOOL RESULT

```
{
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
 "identifier": "altiranischeswr00bartgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt",
 "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.",
 "notes": "Nourai's Table IV says 1979; that is the unchanged reprint.",
 "cites": "column number (the Altiranisches Wörterbuch is numbered by column, two per page)"
}
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
{
 "title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911",
 "edition_found": "1911",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grammarofpersian0000plat",
 "identifier": "grammarofpersian0000plat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt",
 "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Grammar organised by numbered paragraphs (§); grep the paragraph number or the Persian word in transliteration.",
 "notes": ""
}
```


## [2026-09-14T03:10:21.579Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xsvasti\\|xSvasti\\|x§vasti\\|xsvaS.dasa\\|xSvaS.dasa\\|xsvas.dasa\" BRT.txt | head -10",
 "description": "Grep BRT for xsvasti and xsvas.dasa"
}
```


### [2026-09-14T03:10:21.682Z] TOOL RESULT

```
10973:j.  xSvaS.dasa-  Adj.   'der   sechzehnte':
29801:Anfang  der  Vers  abschnitte  s.  Bthl.  af.  3.  i  Verdienst  im  Gedächtnis  hast,  O  M.,  du 23.  —  3) Tu.:  ia  iFnin  i  Jrvttm/än.. ei  daiänlvf sisst   CS    durch    den    besten    Sinn"   Y. ^ästär  .  .  atiänik'ik.     Undeutlich.  —  4)  Oder  |_^2.  6;  —  xsvas.dasa   'rmis"  Yt,  I.  8. ■^  larätiay-,    'martnay-   Adj.,   imn   V.  >
```


## [2026-09-14T03:10:25.861Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10950,11000p' BRT.txt",
 "description": "Read BRT xsvas region"
}
```


### [2026-09-14T03:10:25.932Z] TOOL RESULT

```
"xäviptyö
rasch  dahinfliegt,  . .  wie  der  Pfeil  .  ,"  Yt S.6.  2)   m.   'rascher   SchwuDg"    (dut
Komp.).
KompE.  —  Vgl  ta  xhiahiiayal.aSlrä:  —  Pü. :
iipäk  {wom  HB«.  PSt.  83).
•  j.  x^vaewayataäträ-  Adj.  (mask.  *ra-) 'der  die  Peitsche  kreisen  lässt,  schwingt': xsähra  . .  'ra  (APn.)  "Reiche,  wo  man die  Peitsche  schwingt"  Yt.5. 130.
PPA.,  aMt  *xivafwiiya-  Praes.  30  (Kaus.)  'in rasch  kreisende  Scbvringung  versetzen'.  — VgL  »bd.  nnfifan  usw.;  zuletzt  IF.  9.  ^^^.
•  j.  "xävaä')  indekl  Zw.  'sechs':  i^aitt  aäe tnthra  .  .t  xfi  (als  Nom.)  V.4.1;  9.34, i(7.9«;  —  a^  (als  Akk.)  x^aßt5  ■^,  4; V.  2.  30,  J.51,  7.1S,  p.ii,  32  PüZ.  (?}, /3.8,  14-i-A,  15-45.  ^7-6",  YL4.6,  F./, N.50,  *P.9,  Vd._9;  —  *j^  (als  Instr.) vayzibii'V.6y,i03;  —  xi^  sota  V.2.30, 4.12';  —  xs'  sa/äis'V.4.6,  ■^t.j.gs'».
KompA.;  Ableit.  —  aL  /ät  (Bthl.  ZDMG.jo. joil;  np.  ia/;  S  2'0.  —  Pü.:  &  —  O  Mehr- mall  xsianü  ^eichr.  —  >)  NA.  als  Komp.;  s. ■ach  V.  3.  38.
•  j.  *xSva8  Adv.  'sechsmal' :  W/  frasnä- ^ym  maismaaa  . .  %ri^  . .  ca%ru/.  .  x/°
V.7.7S;  7S',  IS*- VgL  'xhai.  —  Pu.:  6  Mr.
•  j.  x$va$.aSi-  Adj.  'mit  sechs  Augen': ailm  äahskim  ..  "hrikamsr^im  'sXm  Y.g.8.
Komp.  mil  AD.  am  Ende').  —  aX.  t^.dasam . .  jal/aifäiH  in'iJrtditara  RV,  10.  99-  6.  —  Pü. ; 6  OS.  —  ')  Nach  Mastern  wie  etwa  *kv-ali- •iii^%aX/c«(',  wo  der  Dual  berechtigt  war.
•  j.  xSva$.karäa-  n.  'durch  sechs  parallele Furchstriche  hergestellte  Abgrenzung":  •«. /raiJraya/i  Yt4.6.
VgL  hn'jhvia-.
•  j.  xiSvaä.gäya-  n.  'Längenausdehnung von  sechs  Schritten,  sechs  Schrittlängen': 'gäin  JhmJtffai/i  la%rusanqm'V,6.^i;AO.
Pü, :  6  gäm.
•  j.  xdvaS.xSapar-  n.  'Zeit  von  sechs Nächten,  d.  i.  Tagen  und  Nächten':  pasca 'Parst^^  "nach  Verlauf  von  sechs  Tagen und  Nächten"  V.ß.34.
Pi.:  >u  hol  6  iapak.   —  1)  Them.
•  j.  xävaStay-  fem.  Zw.  'sechzig':   °i auiS)ySis»mahe  (sd.)    tistryelie  da%usS    A. J.8.         3)  mit  Gen.  'tlm   ätn^aokanam V.Ä91;  J2.I-
Ableit  —  Ableit.  ans  'xivaj.  —  VgL  ai.  )a}!dy- U;  npw  iaiL  —  PQ,;  6b.
•  j,  x$va£ti'vant-  Adj.  'sechzigfach':  °vä
(nämL  asti  mi^rS)  antan  havisia  Yt  10. 6.
j.  xSvaS.dasa-  Adj.   'der   sechzehnte':
im  asanhqmca  .  .  vahisijm  V.J.  19;  — °sa  (statt  NSm.)   (nämL  yal  ahmt)  hata.-
armU  \t.  I.&.
Ableit  aus  *xhiai.da!a  indekL  Zw.  '16'.  —  ai.
lojaiä-  Adj.  —  Pü.:  iäidahuot.
•  j.  xSvaä.mäbya-  Adj.  'sechs  Monate dauernd';  upas.puhrlm  . .  atvS.mäkim  (sd.)
(  . .  'hlm  vä  V.5.45. Pü.:  sai  mähak.
•  j.  x5va§.satö.-zyain-"  m.,  Pltir.  'sechs- hundert Winter':  aa$yimäi  xsakrai  *°zima (NP.)  *kmjas>nta  V.2.12.
Pii. :  an  i  iahim  lai  i  tam.  —  VgL  ai.  iaiä- kima-  Adj.
•  j.  x^vazaya  Adv.  'sechsmal':  spumm  . . iayaüil  tata    aai  pa%ä    vJväoayantu    V.
'.17.    '
uänft'af
•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
Et.?  —  Pü.!  Sirimk,  Sü.:  ^aw^ai» 'Synlp';  s. noch  No.  1  ff.  —  i)  Pü.  (für  xiV  und  äi'): säen  u  ittrp;  (u  V.  /J  erl. :  nän  u  sfil  väi  'Brod und  Molke'.  —  >)  Pü. ;  vaxienel,  erl.:  trviä- yinei.  —  il  Stammt  aus  Y,  29. 7.  Pü.:  Aurdnn, S.  iu+BiJni/ä/rfj'öj'undNo,4.  —  4>  Pü-:  6.  Die Verwendung  des  Worts  in  diesem  Sinn  s,^^ auf  dessen  kabbalistische  Umdeutung  in  Y. //.  9  mrück;  s,  No.  3  und  lu  *min4d$ifyüi.
•  j.  xSvipta'vant-  Adj.  (fem.  'vaitl-)  'mit Melkmilch,  gemolkener  Milch  versehen'": pamtavaiti  *vaiti  (VSf.)  V.  21.  7.
PDa.  xewd,  PDS.  jvicrf'Milch'').  —  Pü.:  iirö- mand.  —  ')  Im  Gegensatz  zu  patmavant:  — ■)  VII.  ist  "ilvifla-  eig.  das  'herausge  sehn  eilte', d.i.  'gemolkene',  PPfP.[  vgl.  xivofpä-  und  ai.
1  j.  "xSviptyö  va  yyt.13. VgL  V.  31.  7,  wo  xSviftavaiti.
dby  Google
°£a  A  I  I  I  a
564
•  j.  x/vivi',  nur  KompA,:  sva.  xÜciw- ra-.
Vgl.  unter  bmii'.
•  j.  xSvtwi.i§av-  m.  Tfeilschiltze":  ir?xsd '^^  xsviwi.isvaUmB  airyanam  Yt  Ä6;  — •/ä«  parBMv^m  "den  ferntreffenden PfeilschUtzen"  Yl/o.ioz,  77.12.
Eig.i  'des  Pfeile  schnell  sind'.  —  Vgl,  xiviwi.-
•  j.  x§viwt.i§va't«ma-  Adj.  'der  beste Pfeilschlitze':  jrsxsd  (sd.)  xsviwi.isus  'mS airyanam  Yt.S.6.
Superl.  zu  xsvhvijSav:
•  j.  xi^viwi.väza-  Adj.  'schnell  dahin- fahrcnd,  fliegend':  ti^trjm  stänm  ..'växsm
•  j.  xSviwrra-  Adj.  'schnell,  flink,  ge- läufig': däya  me  . .  mastim  späiiB  'nm'^ kisvam  urune  usi  "gib  mir  . .  eine  flinke Zunge,  der  Seele  Auffassungskraft"  Y.  62.4.
```


## [2026-09-14T03:10:42.999Z] TOOL CALL #25: Bash

```json
{
 "command": "pdftoppm -f 490 -l 490 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg490 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg490.png",
 "description": "Render PDF page 490"
}
```


## [2026-09-14T03:10:44.006Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vaeda\\|waeda\\|xaeda\\|aeza-\" BRT.txt | head -20",
 "description": "Grep BRT for xvaeda"
}
```


### [2026-09-14T03:10:45.094Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 73288 Sep 13 23:10 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg490.png
```


### [2026-09-14T03:10:45.171Z] TOOL RESULT

```
2747:•  j.  aeza-'*Ad]'.'verlangend':aätf(s.°3aÄ-)  Feuer  will  er  Brennholz  haben"  V.5. 2; jasal?m  'sähe  Yt/p,  82.  —  vaAUtä    isasä    mananhä  maibyö   x/a-
4231:•  g.  an-aeäa-  Adj.  'der  nichts  (auszu- richten) vermag,  unvermögend,  unwirk- sam, einflusslos':  vaeda  tat yo.  ahmt  mazdn, °sS  "ich  weiss  das,  weshalb  ich,  o  M., nichts  (auszurichten)  vermag"  Y.46.2;  — y?  'um  x/qnm3ng(sd.)  radnn  *väcim'^  Turps asürahyä  ..  ^lla.xsa'^rlm  (sd.)  Y.  2^.9.
4993:•  j.  a-vaeza-  Adj.  'silndlos,  sich  keiner Sünde  schuldig  machend':  "«^  dim  pas- 'alta  . .  fraca  syazJaySii  (sd.)  A.  j.  13;  13; —  °zS  aSa^hh  *frab»nta  dastra.tnasö (sd.)  paitiAarö  N.67;  6j.
8636:•  j.  uz-daeza-  m.  i)  'Aufschütten  von Erde,  Aufmauerung' :  yat . .  paili  . .  daxma -za  kiryeinte  "wo  Leichenstätten  durch Erdaufechüttung  errichtet  werden"  V.j.9 —  y^t  ■  ■  P"'''  •  •  daxma  "-ta'l  *2'7kante
9545:•  j.,  g.  kahrp-,  ksr?/-^'^  f.,  n.'>  'das  sieht- ' bare  Äussere  jedes  Wesens  und  Dings, , äussere  Erscheinung,  sichtbare  Gestalt': sraliiqm  at  tSt  'p/m  (AS.)  -^pam  (GP.)  j ävaedayamakl  tnazdä  ahurä  iinä  raota  . . avat  y.ll  hvarS  aväcT  Y._J(*'.  6;  — para avtiiriAe  hü  "^warstö  (sd.)  'pya  (LS.)  Y. ' /p.  8;  —  asmamm  ,  ,  y3  hislaite  ayanhs 'pa  (IS.)  x^amahe  (sd.)  ".  .  mit  der  Er- scheinung von.,  (sva. ..  anzusehen  wie..)'' YL  13.  2.  A)  insbes.  von  lebenden Wesen;  auch  vom  gestalteten  Stoff  selbst 'Leib,  Körper';  i )  von  Menschen  und Göttern:  aj  'psm  (GP.)  utayuitil  dadat ärmaitis  qnmä  (sd.)  Y.jo.  7;  — ■  yd>!a varsnahe  'palie^^  dsus  (sd.)  N.  7o(7;  — paiti  ainii  .  .  'p^m  .  .  gaia/ie  .  .  °ppm  .  . säJiar/  .  .  "Pim  .  .  abmatr/aAe  .  .  'P^m ..jahikayüi  ..  -p.m  Y.//.  30-32;  32;  — avqm  'P^m  yazamaide .  -yqtn . .  k^r^säspahe Yt /?.  61;  Az._J;  —  üjasat . .  viriisra-fitä ..vätahe  'pa  (IS.)  Vt/4-2;  —  mi%nm..
9839:•  j.  gao-maeza-  m.  'Rindsharn',  als  rituelles Reinigungs-   und    als   Heilmittel'*:    'am
15604:•  j.pairi.daeza-m.,Plur.'einerings-,rundura gehende,  sich  zusamuienschliessende  Um- wallung, Ummauerung':  aSa^a  hl  aiie  ySi maxäayains  aiAhä  z»mö  'tan  pairi.dal- sayqn  V.^j.  18.
17788:•  j.  fra-vaedayamna-  Adj.,  PPM.:  s, 'vaed-,
18504:•  j.  'naeza-  n.  'Spitze',  spez.  der  Nadel: avavaieii  ya%a  sBkayä  (sd.)  'sim  Yt 14-  33-
18506:•  j.  'naeza-  m.  Name  einer  Krankheit: aüalfva  daxmalha  kamiavamU  axtiica gannusla  tafnusca  'zasca  sSrastisYaV.j.SJ ; —  paiHstätSe  gamiSusca  tafttaolca  'sahe^a sarastSisca  Yt/J.  131.
18508:•  j.  ^aeza-  m.  (etwa)  'Klumpen,  form- lose, breiige  Masse':  yaoBit  pu%raAe  Avä- zälahe  frä  °am  nasüm  palät  paiti  ä^re ü'hftn  barst  "als  ob  er  seines  eigenen Sohnes  Leichnam  zu  Brei  verkochte  (imd) das  Fett  dem  Feuer  darbrächte"  V./ö'.  17.
19503:j.  'tnaez-  V.  'harnen'.   Fraes.  3  maeza-.
22047:•  g.  vaeda-,  j.  'vae3a-  i)  m.  'Finden,  Er- langen, Erwerben':  raäitahe  pdhs  aistnüa 'Itmca  "das  Suchen  und  Finden  des  ge- radesten Pfads"  Y.  68. 13;  —  apayeHrfsd.) ra&anaaÄd  'd>m  Y,_J2.  u;  —  yat  usnam aiiti  'oya  (LS.)  "wenn  er  sich  (in  der  Er- langung sva.)  am  Ziel  seiner  Wünsche befindet"  Y.  10. 13  '>.  2)  Adj.  'der  etwas (Gen.)  verschafft,  zu  erwirken  weiss':  atSm- clt  ahyä  masda  "hwqm  mSAhl  paeurvim 'ihm  "auch  ich  (ja)  habe  erkannt,  dass du  das,  o  M.,  als  erster  zu  erwirken vermagst"  Y.  2g.  i  o  ".
22057:•  g.  vaedamna-  Adj.,  PPfM.  r  s.  vaiä^mna-. '
22064:•  g.  vaedana-  Adj.,  PPfM.:  s.  'vaid-.
22065:•  g.  vaedamna-  j.  vag%)mna-,  g.  vae- damna- Adj-,  PPfM.:  s.  'valä:
25552:•  j.  urvaedant-  Adj.,  PPA.:  s.  urvaid-.
```


## [2026-09-14T03:11:00.286Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aeda\" BRT.txt | grep -i \"schwei\\|sweat\" | head -5; echo \"--- all x^ headwords near end ---\"; grep -n \"x\\^a\\|x'a\" BRT.txt | sed -n '1,15p'",
 "description": "Search BRT xv- section"
}
```


### [2026-09-14T03:11:00.366Z] TOOL RESULT

```
--- all x^ headwords near end ---
2483:—  para  ahtnSi  .  .  cinasti  ya%a  ^aitavS x'aitäifm  (sA)  Y.20.  i,  3)  auf  ein Relativum  als  dessen  Korrelat;  a)  adjek- tivisch: ahmili  naemäi  uzjasäitt  mtiro  .. yahtnai  naimanqm  mOiröJruxl  nai-ia  .  . paiti.päiti  Yt  /0. 1 9 ;  —  aÄ  . .  alsam  narqm yöi  kacahi  Yt/7.6;  —  mffirpm  ahyä *madahyä  (sd.)  yä  .  .  uräpayHntl  (sd.)  Y. Jt^.io;  —  Svat  A3  nü  ankuyaite  .  .  cvat ahmäi  naire  m^tm  aahat  yÖ  .  .  frama- r,UU\.4-4t;  Y.62. 1,  Yt.  10.137;  —  "^^ dussar^hahe  . .  manö  3at  ahe  .  .  mane  yö ml  dussatahö  hutaite  Y./0.12  (s.b);  — ipas  vloaSa  .  ./rS  *aAhe  vXsaiti  mt>rö ..
2524:•  j.  "acta-  Adj.  'schimmernd,  schillernd',  1^^/   i,j   -'^     _   x^ania   ..  V.i^.sC;   
2937:•  j.  aoSa-  m.  'Quelle"',  nur  in  upa  'liailu raahaya  (sd.)  "an  der  Quelle  der  R": yatäl  ahi  upa  'laf^u  ranhayh  . .  upa sanaie{sd.)  ratahaya  Yt  J2.  i8£  a)  als Name  eines  Landes*':  x^asJasam  asav- hqmHa  ..  frä^w^rmm  ..  upa  '%al^  raa- hayä  yö  asarB  (sd.)  atwyaxiayänti  " . .  schuf ich  (das  Land)   UAR. . ."  V./.19.
3119:biitaorsm  vä  .  .  x^anm  (sd.)  N.  4S-
3174:Zu  einer  w.  Basis  *t'äxs-  (mit  ö);  i  aas  > '}.  — VgL  mp.  (äil,  eäilai  'Mahl'  (N.  64),  np.  !ä!t, xna.  LW.  r'aL  —  fu.-./nt  i  fuxt  pa  kämak  x^a- rii>/^Vi\  pa  iirVi.  —  ')  Uhlenbeck's  Elyroo- logie  WAiSpr.  90  ist  falsch.
3183:•  y  'aiie  yaza  aji9^  smm  . ."  FrD.  7. ■  j.  a-Jyamna-  Adj.  'sich  nicht  ver- roincicmd,  unvereieglich':  x^airyqn  (sd.) J^arp^fm  *'ium  Y.i*.4''; — "wot  (näml.
3185:x'ars^^m)  Yl  y.so,  V.  2.26;  —  uye  x^a- r^'^e  'ne  Yt/9. 32;  —  te  k>r>nava  mi'i- 7f'fl/«(sd.)  'n»m  "diese  mach  ..  zu  etwas unversieglichem"  V.  2.28.
3339:yj  "ha.k^rftä  ..  urvilx^a^  {%d.)  Y.j4. 13;
3466:•  g-  at  va  Part',  zur  Anknüpfung  eines Satzteils;  1)  'oder  aber,  oder(vel)'  '>,  parallel mit  vä''':  vacaah3  vS  at  vä  manat»hä zastsiiya  {sd.)  vä  Y.33.2;  —  x^aitB  (sd. vil  at  v3  vsrpzSnyS  airyamnä  vä  Y. 33- Z-  2)  'und,  und  auch':  yamsm ,.  xsmävats  {^d)  al  vJ  . .  staomyä{sd.) vacä  Y.33.Z.
3481:mit  ä  1)  'erreichen,  einholen':  yöi  vups t!  apayeinH{s^)  . .  nsit  *aoe  paskäl  äfinie Y.57.29.  2)  'hingelangen  zu  —  (Akk.): yastl  .  .  apänS  darvgs.jyjülm  ä  (näml. apans)  x^a'krtm  vaahSus  manat?hs  astll ä  (näml.  apänd)  »nsQi  (sd.)  paiiS  .  . ". .  wenn  ich  zu  dem  dauernden  Leben gelange,  hin  zu  dem  Reich  des  VM.,  zu  .," Y.J^.5*^
3492:—  ai.  äpa,  np.  af-gandan  ('wegwerfen',  Bthl. IF.  //.  il6)JJ.  —  Pü.:  ii;tf,  (Komp.  auch): ape  hac,  apäl;  s.  nocli  No.  1.  —  "J  apa  F2d (Pü.:  <?^i-'und<t//)ist  aus  Komp.  losgeschält. — apa  x'aitju!  VyC.  44  stammt  aus  Y.  JJ,  4,  — »)  Pü.!  mideuilich.  —  J)  S.  noch  ^bar-  No.  19.
3742:•  j.  apiäma.x'ar-  Adj.  'blindlings  essend': 'rS  (NSm.",  näml.  'ist  der  Hund')  yaia  |     "'  '  '■ t3yus  V.  /J.47;  47-  I  •  j-  aipy-öxSay-  f  'Hineinsprechen,  Ein-
3769:das  Narkotikum  banha-  hervorgerufenen) , Betäubungszustand,  durch  Narkotika  nicht ' zu  betäuben':  ax^aßiS  aAi  "tihö  tSm  y5 ahurs  V.ig.20.  I
3944:•  j.  aiwiä.x^arsUa-  Adj.  (fem.  '5*)  'zum Genuss  geeignet':  aü~a  äfs yaoidya  bavaiii vaiS  'ia  foiubya  vlraiibya  V.ö'.32.
3946:•  j.  'aiwi.x'aninah-  Adj.  'sehr  hoheits- voll':  Marina  nqma  ahmi  'nä  nqma  ahmt Vt.J5.48.
```


## [2026-09-14T03:11:02.461Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB Schweiss ===\"; grep -n \"Schweiss\\|Schweiß\\|xoi\\|ẋōi\\|xai \" HUB.txt | head -20; echo \"=== HRN p114 area ===\"; awk 'BEGIN{RS=\"\\f\"} NR==136' HRN.txt | head -60",
 "description": "HUB and HRN lookups"
}
```


### [2026-09-14T03:11:03.519Z] TOOL RESULT

```
=== HUB Schweiss ===
741:Frauen, arm. varsamak 'Schweisstuch'.
1422:*Haarschopf, gr. 7raxoi;*Vliess', tio xog *Schaf wolle, Vliess',
2018:512. Np. xoi *Helm' ist die lautgesetzliche Form, aber
2021:Dazu arm. xoir *Kopf band, Diadem'. Horn vermeidet
2026:xoi 'Gewohnheit, Sitte, Charakter = gr. sd^og, skr.
2242:zeichnet R a v e r t y doxoiac, doj^ax und doya^ *H5lle\
5612:gurz\ varsamak ^Schweisstuch' = np. bfisclma , vdsama
7069:*Schweiss* = zd. x^'a^da- (also x'ai aus x'aiy); pai {pa) 'Fuss*
7076:raoda-; xoi *Helm' (unbelegt) neben xDd, arab. xudat, arm.
7079:xoir '^DiademV ^p. xaudc^, zd. xaoda-; mOi *Haar = paz.
7124:deutet arm. xoir 'Diadem* auf parth. *a*5tT = ap. xauda-
7168:xoir, ap. xaxiSa-.
7739:skr. svan *tonen' ; x^ai 'Schweiss' = zd. x^a^a-, skr. svBda- ;
8945:khara-; xoi, xdd 'Helm' = ap. xauda-, zd. xao^a-, SLvm.xoir;
9344:Tab. 139, syr. Chron. 9; arm. varsamak *Schweisstuch' =
=== HRN p114 area ===
- 114 -
vd. 3 (105)), /i'lstak (vd. 13 (13) GL, (22), (24) (aw.
roya-)), ynstahlh (vd. 9, (109) — der Commentar denkt
falschlich an np. y ästen, /ez-em): ai. svvda-; arm. l^irtn
(H. Xo. 291).
kurd./«, /öh, /oi 'Schweiss'; af/. yyale (f. pl.); oss.
yed (300, 2); bei. hed, n. ÄtJ (158); wa/. yß, sar. y«/().
514. /''^Ä ^verwandt, angehörig; selbst (eigen)', y^esävend^
yj^estefi, yyeskär^).
aw. vergl. y^aefU" angehörig, verwandt'; phlv. /«'es,
y^esih^ yHslmtan, y^'äskär, y^eskänh.
wa/. /is, sar. yeiy 'Verwandtschaft, Familie*.
Fr. Müller nimmt (WZKM. 5, 187) sehr unwahr-
scheinlich die Instrumentalform aw. ^/^aetusa als Grund-
form für np.y^es an. — Bartholomae (briefl. Mitteilung)
denkt dagegen an ein ap. *kwäisiija' als Grundform;
zum Suffix 'ttja- vergl. ai. -tya-, Whitney, § 1245, b.
515. -^f^en (dialektisch yec) 'Pflug'.
aw. aem- (vd. 14, 10 (43)); phlv. /es(?).
Darmesteter, Et. ir. I, 77.
51G. ^j!lm 'Naturanlage, Charakter'-), vergl. hed^hn^ dns/lm,
duzyim {Vis und Ramm S. 32 V. 5 v. u.).
aw. vergl. haya-^ haem vd. 13 (124), pancö^\hya-
(Geldner, KZ. 30, 514 Note 1); phlv. /I?« bezw. /n;j
(vd. 13 (124), 5 (117) Gl.), huyjm (Gemme, ZDMG. 44,
068 No. 105), dus/wu
Anders und falsch Fr. Müller, WZKM. 5, 187; die
Bedeutung der aw. Worte steht jedenfalls fest.
517. x^?/'^» yJ^ 'Speichel', ylin (Gazophyhicium s. v.
saliva, Vullers s. v. ylm No. 3).
aw. gereöi.']yava'^ yt. 15, 47 (?); plilv. ;^ay?7Ä; (y. 38
(13) GL), yaya (Bund.).
Justi, Bund. s. v. yayü,
AM. gebraucht die Form yeön (208 Zeile 3 v. u., 209
*J Bedeutet auch bei Firdüsi 'fleissig, rechtschaffen* wie im
Pehlevi; ein np. ^^'es *Pflug' statt j^es (No. 515) giebt es nicht.
2) Reimt auf htm (Via und Rämln S. 51 Vers 9; 166 Vers 13),
dns sohon damals nicht mc»]ir bem gesprochoii wurde.
```


## [2026-09-14T03:11:20.150Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==135' HRN.txt | tail -30",
 "description": "HRN p.113"
}
```


## [2026-09-14T03:11:20.715Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7060,7085p' HUB.txt; echo \"===7730===\"; sed -n '7730,7745p' HUB.txt",
 "description": "HUB context around xᵛai 'Schweiss'"
}
```


### [2026-09-14T03:11:21.164Z] TOOL RESULT

```
509. yiiisnüdj x^snü zufrieden, fröhlich*.
aw. *huxsnüta' vergl. hu/rnüiti- 'Befriedigung'; phlv.
/iisnüt, /usnütik (AV.).
510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
aw. hü kehrpa in Ebergestalt'; phlv. /ük (Bund.),
yßköak hezw, /übadak (Payprus, Ilorn ZDMG. 43, 51);
skr. siikard- 'Eber, Schwein*.
kurd. /ü (H.-Sch.); B>fy.xilg; oss. d. t. yiä (310);
bei. hlk, n. hJy (157) ; wa;r. /äg, sar. y^ug,
511. //rn 'Blut', yümn.
aw. vohuni' *Blut'; phlv. yün, yUnömaud,
kurd. ;^("n (ll.-Sch.); af}'. vTne (f. pl.); bei. LW. hün,
hon (162); wa/. vu/c^n, Uyn. vlyTn, sar. va/ln, sangl.
vain,
512. xöl Helm', yöd.
ap. yauda- *Helm*; aw. ayö],yaoda'.
arab. LW. yu^at 'Helm'; Sify.yöl; oss. d. yodäy t. yüd
(302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'.
513. yi^'ei 'Schweiss .
aw. yya^öa- 'Schweiss' (ZPGl.), vergl. aw. y'^'Tsctt,
ynseu] phlv. yj^ai bezw. y^'ede, vergl. ynst (y. 9 (37),
») Z. B. xöst (I, 117 Vers 962).
*) Np. ves, das ich Mitteilungen, Heft IV, S. 25 No. 6 fälschlich
neben phlv. reh gesetzt habe, lässt sich nicht zu np. '/us stellen, da die
Vertretung von altem sv durch v wohl kurdisch und belucisch aber nicht
neupersisch ist. Nöldeke (mündliche Mitteilung) sieht r^s als Doppel -
form zu ges an, dessen Aussprache durch jüd.-per8. "»;^;j (Is. 10, 12) voll-
stündig sicher gestellt ist.
') Der bei diesem Worte auch Gberlie forte Majliril vokal if^t falsch.
II o !• n , Grundriss d. noiip. Ktymolojrio. S
```


### [2026-09-14T03:11:21.224Z] TOOL RESULT

```
skr. nidra-^), Mit Verlust des h nach langem Vokal: np. sar
'Schmerz, Leid' aus *sahr = zd. sadra- Xeid, Elend'. Vgl.
sdhar 'Gatte' durch Anlehnung an pidar u. s. w. aus *s5Ar
= zd. ^xsaodra- entstanden? Siehe oben p. 82.
b) zu y = i: mai 'Wein', paz. mai Min. Gl. 132, Shk.
257, zd. maiit- *Wein (nach Darmesteter); fcai Vann,
wie?' = zd. kada; Dai *der zehnte MonatV zd. dadvd; nai
*Rohr , g. nad 'Rohr = skr. nada-, vgl. nai TlOte' aus
^nada-; pai Tussspur = zd. paia-, ap. nipadiy; x^ai
*Schweiss* = zd. x^'a^da- (also x'ai aus x'aiy); pai {pa) 'Fuss*
= zd. pada- ; -ra Casuspartikel = paz. ra, phi. rai wegen',
ap. radiy Vegen*; x^ai {x^a) *Wohlgeschmack' = skr. svada-;
boi {ho) *Geruch* = zd. baoidi- (arm. buidenik Moses, Geogr.
616, wohl boyicenik zu lesen = np. boy i ctnt 'chinesisches
Parfum'); roi {ro) 'aes vel stannum fusum' = bal. rDd 'Kupfer ,
arm. avoir 'Messing, skr. loha-; roi {rd) 'Gesicht' = zd.
raoda-; xoi *Helm' (unbelegt) neben xDd, arab. xudat, arm.
^) Dazu np. kahar = skr. kadrxi- *rotlibraun*, zd. kadrv0'{a3pa')^
Geiger, Idg. P. IV, Anz. p. 23.— 200 —
xoir '^DiademV ^p. xaudc^, zd. xaoda-; mOi *Haar = paz.
mU Min. Gl. 140, g. frnd, bal. mUd^ mid, nb. mldy also ap.
*muda' ? ; sSi 'Gatte = ap. *xSauSa- ? ; maig *Heuschrecke
(neben malax) = phi. maig (und malak Bdh. 47, 10), bal.
maday, madax, arm. marax, zd. mataxd-; patg *Bote* =
syr. W^B, phi. paik, arm. payik, skr. padika- (s. oben p. 45
— 46)Vjp»y^rfa *Pussganger' = skr. paddti-y padatika-; miyan
===7730===
Ahmatan also fiir *Hahmatan, Vgl. § 143, a.
Im Inlaut zwischen Vokalen scheint A = ap. A nicht
geschwunden zu sein, selten h = ap. &, siehe § 60.
§ 108. Ap. uv (fiir huv ?= zd. a;", ^uh = idg. sv)
wird im Np. zu x^\ inl. nach a zu x:
a) im Anlaut: x^arazm =^ ap. uvarazmis; x^ahar
'Schwester = zd. x^a/ihar- ; x^ob 'Schlaf , zd. x^afna- ; x^ar
'leicht' = zd. x^a&ra-; x^astan Vunschen', x^ai *Wohl-
geschmack' (oben p. 57), skr. svad; x^andan *rufen, lesen',
skr. svan *tonen' ; x^ai 'Schweiss' = zd. x^a^a-, skr. svBda- ;
x^'ar, spater xur 'Sonne', gewohnlich x^arsBd, xurSed = zd.
"^x^are, gen. x^eng (neben hor 'Sonne' = zd. hvare, hvare-
rsa^tem, gen. hu und hUro =- skr. siiar, gen. suras); x^ar-
dan^ xurdan 'essen, trinken' = zd. x^ar-; x^'ad, xud 'selbst'
= zd. x^ato; x^'as , xus gut, schon', siehe H. 508, oben
p. 57 ; xtisrii 'Schwiegermutter = skr. gvagru- (idg. svek^ru^) ;
```


## [2026-09-14T03:11:32.560Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg490.png"
}
```


### [2026-09-14T03:11:33.436Z] TOOL RESULT

```

```


## [2026-09-14T03:11:33.422Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T03:11:58.655Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt; do echo \"=== $f ===\"; grep -c \"\" $f; grep -n \"\\[pdf page\" $f | head -3; done",
 "description": "Inspect BQT page files"
}
```


### [2026-09-14T03:11:59.652Z] TOOL RESULT

```
=== BQT_v1_pages.txt ===
32486
=== BQT_v2_pages.txt ===
41071
```


## [2026-09-14T03:11:59.655Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "BQT metadata"
}
```


### [2026-09-14T03:12:00.527Z] TOOL RESULT

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


## [2026-09-14T03:12:05.715Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v2 leaf257 (p797) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==258' BQT_v2_pages.txt | head -70",
 "description": "BQT p.797"
}
```


### [2026-09-14T03:12:06.622Z] TOOL RESULT

```
=== v2 leaf257 (p797) ===
 ‫خوید‬                                                                                                                        ‫‪۷۷‬‬


  ‫ابلای‬
      ‫تشدح‪۷‬ت‪-‬و‬
             ‫با‬                  ‫ن‬
                                 ‫دنیهآب‬
                                      ‫تحتالی ‪ ۰‬بمع‬                       ‫خوه = بفتح‌اول وئالی » بروزن ومعنی‬
‫مجهول کلاه خودی که درروزهای جنگ بر سر‬                                    ‫‪-‬‬           ‫دا‬
                                                                                      ‫شلو‬
                                                                                        ‫بردان ک‬
                                                                                              ‫خبه است که خفه کردن و فش‬
‫گذارند ‪ - ۸‬وبا تحتالی مشددهبعریی زمین دشت‬                                ‫و بسکون ثالی بمعنی خوی است که عرق آدمی‬

‫وهامون و زمین لرم باشد ‪٩‬‏ ‪ -‬وبا ثانی معدوله‬                              ‫وحیوانات دیگرباشد ‪ - ۴‬ویضم اول وسکون‌نالی‬
‫بروزن‌می»عرق‌انسان وحوانات دمگر باعد(‪٩*)۷‬‏‬                               ‫مجپول گ؛یاهی‌است که‌درمیان گندم‌روبد و کندم‬
‫وضم اول وئالی مجپول » خصلت وطبیعت وعادت‬                                  ‫را زبان رساند ‪ -‬وخواهر را نیز گوبند و بعریی‬
‫کروابند ‪۱٩-‬‏ وبمعنی کلاه خود هم بنظر آمده‬                                                  ‫‪۷‬‬
                                                                                                                    ‫اخت خوانند ‪. ۴‬‬
                                                                                                                                  ‫‪1‬‬
                                                     ‫است ‪. ۸‬‬             ‫حو هل ‪ -‬با انی معدوله‌بروزن سهل‪,‬‬
‫‪-‬نابه‬ ‫خوی‌ار بغل رو ان‌شدن ک‬                                             ‫بمعنی کج وناراست باشد ‪ - ۴‬و با ثالی مجهول‬
‫ازشرمنده شدن وخجالت کشیدن باشد ‪ -‬کونابه‬                                  ‫بروزن‌فوفل » هم باینمعتی وهم بمعنی حیوانیکه‬
                          ‫از مسنت ومشقت هم هت‪2 .‬‬                             ‫ویای اوکج )‪ ۱‬باشد ننظر مده امتت‪> :‬‬                          ‫دست‬

‫»ندم‬
   ‫حو یبد = بفتح اول‌بروزن دوید گ‬                                            ‫خوهله ‪ - °‬باانی معدوله بورزن‬
‫وجوی را گویند که سبزشده باشد کن خوشه‬                                     ‫وناراست باشد‪.‬‬             ‫جهی‬
                                                                                                     ‫کت ک‬
                                                                                                        ‫بهله نمعنی خوهل اس‬
‫آن هنوز نرسیده باشد ‪ -۴۱‬وبمعنی غله زار هم‬
‫بنظر آهده انت هتکس اون نیز معنی غله وجو‬                                  ‫خو هلگی‪ = ۱‬با ثالی معدوله بروزن‬
‫ارس بود » وبائانی معدوله گهفمته‌اند که بروزن‬                                             ‫استی باشد ‪.‬‬
                                                                                                   ‫نیاکرجی‬
                                                                                                         ‫وعن‬
                                                                                                           ‫سلکی » بم‬
                                                 ‫وسرانی وسکون | صید باشد ‪.‬‬
                                                                         ‫خوی ‪ -‬بفتح اول ک‬

                                 ‫باشد ‪.‬‬    ‫(‪)۲‬خم ‪- : ۱‬‬                       ‫‪.‬‬    ‫و ناراست‬     ‫‪+‬‬    ‫‪:‬‬       ‫؛ چس‬   ‫چك‬    ‫(‪)۱‬‬


 ‫خواهر‬             ‫‪12۷‬‬   ‫پهلوی‬      ‫‪۴‬‬                ‫‪.‬‬   ‫خوی‬       ‫رک‪:‬‬           ‫‪۴‬‬         ‫خبه وخیه ‪.‬‬         ‫‪:‬‬    ‫رک‬        ‫‪۱‬‬


  ‫) و تىز (‪ãK‬‏‬           ‫کهآ نرا ‪hux‬‏‬      ‫‪ ۳‬خاتمر ؛ اما هز وارشی‌در رسم‌الخط بهلوی هت‬                             ‫‏‪ oe‬رک‬             ‫«بوتکر‬

  ‫؛ کلبود‬             ‫هل‬
                       ‫خو«‬
                         ‫‪۴‬‬                       ‫‪.‬‬        ‫خوانده ویپهلوی ‪tarb‬‏ تلفط کنند معنتی پرادر «بولکر ‪۶‬‬

                                                                                       ‫ضف راست ‪ .‬بوشکور (بلخی) کوید ‪:‬‬
              ‫‪».‬‬    ‫باسح دهد ببرزن‬        ‫خوهل‬       ‫همت‬                              ‫دش من‬        ‫س ار ار وخوهل آوری‬
  ‫لفت فرس ‪ ۳۱۳6‬ور کث‪ :‬خوهله» خهل'خپله ‪.‬‬
  ‫‪ - ۱‬از ‪ :‬خوهله(خوهلکه) ی‬                                     ‫‪۲‬‬   ‫خوهلی* لغت فری ‪ ۹۳‬و‬                  ‫¬‬    ‫خوهل‬       ‫»‪-‬‬   ‫‪۵‬‬

      ‫(اب دهان) «واژه‌نامه‪ ۹۱۳‬ار کت ‪ 2‬خبو‪,‬خدو‪.‬و رکف ‪ 0‬جح‬                                  ‫‪10‬‬       ‫‪ ۹۳ ۷‬طنری‬                     ‫(مصدری) ‪۰‬‬
                                            ‫و هوشمان اس ‪:‬‬                    ‫خور (ھ‪.‬م‪ (.‬ورك‪ :‬امشق ‪۲‬‬                     ‫=‬    ‫‪۸‬‬

  ‫فریدون است پنداری‌بز بردرع وخوی اندره‬                                          ‫سباوش است پنداری‌میان شپرو کوی‌اندر‬
      ‫دقیقی طوسی ‪« .‬لغت فری ‪۱۲۵‬‬
  ‫‏‪( - ٩‬عر) «خوی ‪ ۰‬زمین پت ميان دکووه است » وخوی نرم از زمین است ‪« ».‬شرح‬
      ‫‪ - °‬بهلوی ‪ . ) 12۷1 ( 12۷2‬اوستا ‪ . :21062۷-‬هندی باستان ‪20۵۷5‬‬                                                               ‫قاموس؛ ‪.‬‬
      ‫‪,‬ردی ‪161 ۰ ×۵‬‬
                  ‫(عرق) «اسفا‪۲ :۱‬ص‪,»۸۳‬بلوچی ‪ 1۵21‬ایا ‪ , ۳۲۰‬وخی أنظ «ایضاً ‪ 5۹۲6‬ک‬
  ‫‪.‬‬    ‫رك‪ :‬خوه ورك ‪ :‬لفت قرس ‪۵ ۴۲‬‬                        ‫(عرق) ‪ ۱‬استی ‪dex‬‏ ‪ ۰‬سربکلی ‪hdiax‬‏ «اسشق ‪۳:۰‬‬                                     ‫‪101‬‬

          ‫سنگدلی خوی تست ومهرمرا خوی ‪.‬‬                                               ‫‪- ۱‬خوی تو باخوی‌من بنیز نسازد‬
  ‫‪.>۵0‬‬    ‫‪۹‬‬        ‫‪«۰‬لفت فری‬   ‫خسروی‬
```


## [2026-09-14T03:12:06.712Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v2 leaf265 (p805) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==266' BQT_v2_pages.txt | head -70",
 "description": "BQT p.805"
}
```


### [2026-09-14T03:12:07.723Z] TOOL RESULT

```
=== v2 leaf265 (p805) ===
                                                                                     ‫‪=A‬‬‫و‪‎‬‬




‫خیناگر = باکاف فارسی‌بروزن تیرآور‪.‬‬                ‫کردن وباد دربوق انداختن باشد‪ .‬که آنهم کنابه‬
                  ‫و‬    ‫ساز نده ومغنی را گومند ‪۳‬‬
                                                    ‫از برخاستن و برپایشدن آلت تناسل است ‪-‬‬
‫= بفتح واو بروزن بی‌خبر »‬        ‫حینو ر‬            ‫کونابه از فرودآمدن ومقیم شدن ولزول کردن‪.‬‬
                           ‫پل صراط رگاویند ‪.‬‬                           ‫ولشکر کشیدن و نوت نا‬
‫حو ‪ = ۴‬بسراول وسکون‌ثانی وواو‪,‬‬                      ‫خیم نزگادی ‪ -‬کنابه از آسمان‬
‫آب‌دهن راگوبند؛ وبفتح اول وضم ثانی‌هم‌درست‬
                                                                                         ‫است ‪.‬‬
                                        ‫اكت ‪::‬‬      ‫خیمه کبوه = بعنی خيمة زنکاری‬
                                                                           ‫است که آسمان باشد ‪.‬‬
‫حیوق * ‪ -‬بکراولبروزن زببق ‪.‬نام‬
          ‫ولاسی جک ازاولعای )‪ (۱‬خوارزم ‪¥.‬‬         ‫ن ینا سرودونغه هرا کومند ‪١.‬‏‬
                                                                               ‫خینا ‪ 5‬روز‬




                                                                  ‫)‪ ۱‬چك چش‪:‬الکای ‪.‬‬

   ‫(ھ‪ .‬م‪(0‬‬   ‫«چینود»‬    ‫_ مصحف‬   ‫‪۴‬‬         ‫خنبا کر‪.«(.‬م‪).‬‬   ‫سس‬          ‫رك‪ :‬خنبا ‪۵‬‬   ‫‪۱‬‬

   ‫= یوخ » یولهب ‪ ‹ 120016‬نامشیوه ‏‪٩۵۱۷‬و ‪12101‬‬                   ‫‏‪= X۷. e0 _ ۴‬ودخ‬
   ‫‪ - ۵‬کدثرب‌اسلامی‬                  ‫|تال‪ « 6708‬اسشق ‪۷۱‬ه»› رك‪ :‬خدو‪.‬‬
                                                                  ‫و‪. 25‬اوسا _ ‪ ۵۷۵2‬ن‬
                             ‫‪« xiwaq‬دائرة المعارف اسلام‪ .‬فراشه ج ‪ ۲‬ص ‪۳٩٩‬‏ ستون ‪.*۱‬‬
                                                                                   ‫خیوق ‏‬
                                                                  ‫‪ #‬خيوه ‏ رك‪ :‬خیوق ‪.‬‬
```


## [2026-09-14T03:12:30.455Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD xwys ===\"; grep -n \"xwys\\|xwyδ\\|sweat\" SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian dict"
}
```


### [2026-09-14T03:12:30.514Z] TOOL RESULT

```
=== SOD xwys ===
16514:                                                                    xwest, xwetst, xoyst (Ywyst) ~*xwystk, Ywyst>k
16574:        OcOperspire, Go)sweat                                       BSTBL; TSP 6.40, 50, 62
16586:         ywycst, xwystk
16596:         ob. -y, -w, ->; pi. -t; ob. pi. -ty =*xwystr             and, also
34972:            xusm, xosm =^xwysm                                             n2
34990:10790 xwsp'ny C                             J^io^                      10800 xwsty =» xwystk
35002:      sixteen                                                                   ^ywys^k, xwystk
35031:        =>xwystr                                                             reservoir ?, clay jar ?
35120:                                                                                                                  xwystk
35136:                                                                     xoynstar ©nom. -yy; ob. pi. -tyy ^xwystr
35165:                                                               10849 xwysm C                      C& 'j^h^ < jW «*rj>
35175:      Sund. MHC p27.8 p28 n 50                                 10850 xwysm brync C                                 *Vgj
35181:      HuyadagmanOzame of Manichean hymns)                      10851 xwystk S                                         ^L
35192: xwystr
35194: 10852 xwystr      M                      j£ J ^Ujj i^j              C2, 102V30
39587: (/c)sweat      4503                           taking 249, 1533                        ten million     5045, 5068
```


## [2026-09-14T03:12:31.816Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON خیو ===\"; grep -n \"خیو\" MON_part1.txt MON_part2.txt | head -20; echo \"=== MON خوی ===\"; grep -c \"خوی\" MON_part1.txt MON_part2.txt",
 "description": "Grep Mo'in for خیو"
}
```


### [2026-09-14T03:12:31.931Z] TOOL RESULT

```
=== MON خیو ===
MON_part2.txt:31943:آن تتخیول زا در رف سم کت. کر 
MON_part2.txt:39529:خیو. آب فلیظ که از بعض داروهای 
MON_part1.txt:93530:خیا؛ طین خیوس طین رومی. طین اکل: 
MON_part1.txt:93567:اقریطس. طین خیوس: (زه.) طین اقریطس. 
=== MON خوی ===
MON_part2.txt:139
MON_part1.txt:232
```


## [2026-09-14T03:12:37.782Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16540,16600p' SOD_pages.txt",
 "description": "SOD around xwys"
}
```


### [2026-09-14T03:12:37.831Z] TOOL RESULT

```
     TSP 2.427
                                                              4499 Ywyr-3 B, S                                  jxs.«j>-
4487 Ywyc(h)     B ^ Yw>yc                                         xwer ©<*xwarya ©intrans. v.
4488 Ywyck»w>k   B                 JkUf ^j i^l/T                   0o)be eaten
     xoyckawe, xweckawe (xwycq'wyyh, Ywyck'wy,                     TSP 2.346; MDiii 3sg. impf. xwyr>
       Ywyck>wy, ywyck'w'k) ©f. n.                            4500 Ywyr^rSyn^ B          (s-^y <Ot**l j>) jj^ JL*
     liberation
                                                                   xuwar-arOene ? ^Ywvr» *r5
       BSTBL, Vim. 79, 80, 94, Dhy. 360, 361, Dhu. 98,             rock crystal
         253 & etc.; TSP 7.95, 103, 9.113; Sogdica. 61.31;         BSTBL, Dhy. 45, 337
         -*V*w, TSP 9.118; W-Li, ii: Gropp. p39               4501 Ywyr pY B                                 ^jy^d<&-
4489 YwyckVy       =* Ywyck»w}k                                    xoyr-PaY, xuwar-{3aY
                                                                   Sun-god
4490 Ywyckc» B, S          (jjS, ^          ^,/f <*£ 0l
     xweck, xoyck ? =»xwycq, Ywck>                                 VJ 7, 40
     open, free
                                                              4502 Ywyrsny B, S                         ^UaT ^^L <j^
       VJ; TSP; SCE; BSTBL; MDii p201-f Frag. Len.                 xoyr/xuwor-sane =»xwyrsny
                                                                                                                   11



                                                                                                                   (J*


  ywys-
       east, sunrise                                         4512 ywy z*k(w) B           >^    j->)Ji-^ «U «j*r- «*=-W^
       TSP 17.4, 16, 20, 26, 31, 3.144; Hen. JRAS 1944,
          138.20; Frag. Len. 82 a 26                              xwezak(u), x5yze ? (ywzky ) ©adv.
                                                                  very, very much, extremely
  4503 ywys- B                          o>/is^'o>/3S
                                                                  GMS 234; Bcnv. Notcsi 36-7; BSTBL; VJ; TSP;
        xwes, xoys ©<Av. xvisa—, *xwisa\ MP xwyd
                                                                    SCE; STii 7.33; rwyz'w, VJ 1044; STii 7.30;
        OcOperspire, Go)sweat                                       BSTBL; TSP 6.40, 50, 62
        GMS 228, 539; TSP 2.295; Hen. Texts. 718;
          Bailey. Prolexis. 23; S W, MIS 1984, 206; AVS      4513 ywyz*y =* ywyz*y
          71                                                 4514 ywz- B,S                                      ^^
                                                                  xoz (ywz-) =^ywst-, xwj-, xwz-, ywyz-
  4504 ywyst    S(MD) ** ywycst
                                                                  (fo)demand, (f<?)wish
  4505 ywyst'k B, S              ^j^a i(jU* <*j&>J t^j            TSP 5.107, 13.13; BSTBL, Dhy. 40, 74, 145; Frag
       xoyste, xweste (ywystk) ©<Av, hvoista; Khot.
                                                                    Len.; MDii; trans, pret. VwStffir-, VJ 1077; l*L
         hva$ta\ Oss. xistan Munj. xusci =»xwsty(y),
                                                                    >Ywsty, Frag. Len. 93.36; AVS 138
         ywycst, xwystk
       chief, superior, teacher, honoured                    4515 ywz- =4 ywz-
      _ GMS 230; SCE 92; BSTBL, Dhy. 7, b9 etc.; Intox.      4516 ywzky B =$ ywy z*k(w)
                                                             4517 ywzn M                                          j^
          32; TSP 5.59, 8.200, 17.22; MDiii; Bailey.
          Prolexis. 435                                           yawazn ©<Av. gavasna ©ob. -yh -^wzn
                                                                  deer
  4506 ywystk ==» ywyst'k                                         GMS 375, 1230
  4507 ywystr B, S        (J>> y-t-x j->)j^jj* «>j;l>J t^j   4518 yy C                                             ^%$
       xoystar, xwestar ©<*xwa(y)ista-tara ©nom.
         ob. -y, -w, ->; pi. -t; ob. pi. -ty =*xwystr             and, also
       chief, superior, head                                      Yl/8?4.5, 10, 5, 21 & etc.; BSTi 61 etc.
                                                                  STii
       GMS 230, 1301; VJ; TSP; BSTBL; SCE; STii 7-40,
                                                             4519 yy- S                             cp/^^/^
```


## [2026-09-14T03:12:39.199Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /4503/ && /xwys/ {print NR\": \"substr($0,1,1500)}' SOD_pages.txt | head -40",
 "description": "Find SOD entry 4503"
}
```


### [2026-09-14T03:12:40.177Z] TOOL RESULT

```
246:                                                                                                                    11



                                                                                                                   (J*


  ywys-
       east, sunrise                                         4512 ywy z*k(w) B           >^    j->)Ji-^ «U «j*r- «*=-W^
       TSP 17.4, 16, 20, 26, 31, 3.144; Hen. JRAS 1944,
          138.20; Frag. Len. 82 a 26                              xwezak(u), x5yze ? (ywzky ) ©adv.
                                                                  very, very much, extremely
  4503 ywys- B                          o>/is^'o>/3S
                                                                  GMS 234; Bcnv. Notcsi 36-7; BSTBL; VJ; TSP;
        xwes, xoys ©<Av. xvisa—, *xwisa\ MP xwyd
                                                                    SCE; STii 7.33; rwyz'w, VJ 1044; STii 7.30;
        OcOperspire, Go)sweat                                       BSTBL; TSP 6.40, 50, 62
        GMS 228, 539; TSP 2.295; Hen. Texts. 718;
          Bailey. Prolexis. 23; S W, MIS 1984, 206; AVS      4513 ywyz*y =* ywyz*y
          71                                                 4514 ywz- B,S                                      ^^
                                                                  xoz (ywz-) =^ywst-, xwj-, xwz-, ywyz-
  4504 ywyst    S(MD) ** ywycst
                                                                  (fo)dema
```


## [2026-09-14T03:13:02.282Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39500,39560p' MON_part2.txt",
 "description": "MON context for خیو"
}
```


### [2026-09-14T03:13:02.339Z] TOOL RESULT

```
پوشیده باشد. 
لطیفه: )۱۸۱1 (ع. لطیفة | (ص.) مژنث 
لطیف (همه.) (.) گفتاری نغزه مطلبی 
باریک و نیکو نکته. بذله. شوخی. نکتة 
بار یکت دقبقه. (تص.) اشارت دقبقی که از 
آن معنیی در ذهن خطور کند که آن را نتوان 
انسانی (انسانیه): (فد.) نفس ناطقه. (تص.) 
دل» روح. 

جر 21 [ع. .| (ص.) اسب سید روی. 
(. ) اسب نهم در مسابقه. . (رص.) ) آنکه پدر و 


یناشن کمن 


مادرش مر ده باشنك. 


لظی: نها (ع.) (اخ.) طبقةٌ پنجم از طقات 


لعات 


دوزخ. (اخ.) جهنم» دورح. 

لعات: 0 اق ] (ص.) باز یگر بازی‌کن. 
لعاب: طا9 [ع. ۰] (.) ون دهن. حد وه 
خیو. آب فلیظ که از بعض داروهای 
خیسانیده برآید (مانند لعاب بزر قطونا) با 
بعض جانوران آن را تولید کنند (مانند لعاب 
عنکبوت). درخشش و جلای روی سفال و 
کاشی که علاوه بر جنبهٌ تزیینی باعث نفود 
ناپذیری آنسچه لعاب داده شده است. 
می‌گردد و آن در اصل عبارت است از شيشة 
مذاب؛ يا سنک چخماق شیشه‌یی که به 
وسیلهًٌ حرارت بصورت مایع در آمده است. 
لعاب ممکن است شفاف يا مات حا کی 
وراه نا ات هاووان‌سافت تعات‌های 
رنگین را ه وسیلةٌ افزودن اکسیدن‌های فلزی 
مانند سرب و قلع و غیره تهیه می‌کنند. ۱ ۳ 
برف. . لعات حنبه: زهر مار. لعاب روان: ( کد.) 
شراب: می. لعاب زمرد نقاب: ( کد.) شراب 
می. لعات سحات: (کذ.) باران. لعاب شمس: 
چیزی که چون تار عنکبوت در صحراها به 
وقت گرمی هوا پدید اید؛ خیط باطل» 
مخاط شمس؛ مخاط شیطان؛ ریق الشیاطین 
(لف.) لعاب عنکبوت: تار عنکبوت. (کد.) 
طراحیء نقش کاری. لعاب گاو (کوهی): 
یز دهان گاو (کوهی). (کد.) کاغذ سفید. 
( کد.) روشنی و سفیده صبح. [ کات فان 
(کد.) شنمی که روی زمین را سفید سازد. 
لعاب گوزن: لیزابة دهان گوزن. (کد 
روشنی و سفیدهٌ صبح. (کذ.) برف. (کن.) 
شبنمی که روی زمین را سفید سازد. لعاب 
شمس. لعاب لعل: (کد.) شراب سرخ. لعاب 
و عسلء لعاب نحل. ( کن.) شراب 
انگوری. 

لعاع: ۱0۹3 [ع.] .( (کما.) کماه نورسته؛
```


## [2026-09-14T03:13:03.687Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1472\\|۱۴۷۲\" MON_part2.txt | head -10; echo \"---\"; ls -la MON_part1.txt MON_part2.txt; grep -c $'\\f' MON_part2.txt",
 "description": "MON page markers"
}
```


### [2026-09-14T03:13:04.723Z] TOOL RESULT

```
---
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0
```


## [2026-09-14T03:13:12.753Z] TOOL CALL #42: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T03:13:12.760Z] TOOL RESULT

```


```


## [2026-09-14T03:13:16.713Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C",
 "prompt": "Give the full etymology sections for the Persian entries خوی — especially the one meaning \"sweat\" (and any meaning \"habit/temperament\"). Quote Middle Persian, Avestan and Proto-Iranian forms and cited sources."
}
```


## [2026-09-14T03:13:18.606Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swoyd-",
 "prompt": "What does this page say about the PIE root for sweat (*sweyd-/*swoyd-)? List the descendants including Proto-Iranian, Avestan, Proto-Germanic, Latin, Greek."
}
```


### [2026-09-14T03:13:22.427Z] TOOL RESULT

```
# Etymology of Persian خوی

## Etymology 1 (Sweat)

**Middle Persian source:** Inherited from Middle Persian /⁠xwēy⁠/ meaning "sweat, perspiration"

**Proto-Iranian:** *hwáydah

**Proto-Indo-Iranian:** *swáydas ("sweat")

**Proto-Indo-European:** *swóyd-o-s, from root *sweyd- ("sweat, to sweat")

**Cognates:** Baluchi ہید (hed) and English "sweat"

**Citation:** Müller, Friedrich (1894) and Steingass, Francis Joseph (1892) documented this term in their etymological works.

## Etymology 4 (Habit/Temperament)

**Related form:** Otherwise خو (xô)

**Sanskrit cognate:** स्वधा (svadhā́)

This etymology section is notably brief in the source material, with the Sanskrit connection noted but limited additional detail provided compared to Etymology 1.
```


### [2026-09-14T03:13:24.529Z] TOOL RESULT

```
# PIE Root *sweyd-/*swoyd- and Its Descendants

The page documents the Proto-Indo-European root **\*sweyd-**, meaning "sweat" (noun) and "to sweat" (verb).

## Key Descendants Listed:

**Proto-Iranian Branch:**
- Proto-Indo-Iranian: \*swáydati
- Sanskrit: स्वेदते (svédate)

**Proto-Germanic:**
- \*swaitaz, \*swaitą, \*swaitô

**Latin:**
- sūdor ("sweat, moisture")
- sūdō (denominative verb)

**Ancient Greek:**
- ῑ̓δίω (īdíō)
- ῑ̔δρώς (hīdrṓs)

The page notes that Avestan is not explicitly mentioned among the descendants. The reconstruction shows various morphological formations, including causatives and heteroclitic forms (r/n variations), with attestations across multiple Indo-European language families spanning from ancient Sanskrit and Greek to later Germanic and Romance languages.
```


## [2026-09-14T03:13:29.475Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D9%88",
 "prompt": "Give the Persian entry خیو: meaning and full etymology (Middle Persian, Proto-Iranian forms, cited sources). Also any alternative forms like خدو."
}
```


## [2026-09-14T03:13:31.367Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%B4",
 "prompt": "Give the Persian entry شش (šeš) \"six\": full etymology — Middle Persian, Proto-Iranian, Old Persian/Avestan, Proto-Indo-European forms and cited sources. Also anything on شانزده and شصت."
}
```


### [2026-09-14T03:13:35.619Z] TOOL RESULT

```
# Persian شش (šeš) "six" - Etymology

## Etymology Chain

**Middle Persian:** šaš (script not provided in source)

**Proto-Iranian:** *šwáš

**Proto-Indo-Iranian:** *šwáćš

**Proto-Indo-European:** *swéḱs

## Cognates Cited

The entry provides extensive Indo-European comparisons including Sanskrit षष् (ṣáṣ), Russian шесть (šestʹ), German sechs, Spanish seis, Greek έξι (éxi), and Lithuanian šeši, demonstrating the deep ancestry of this numeral across language families.

## Note on Related Terms

The source document provided covers only شش. It does not include etymological information for شانزده (sixteen) or شصت (sixty), though both appear in the Persian number system reference table within the article.
```


### [2026-09-14T03:13:35.757Z] TOOL RESULT

```
# Persian Entry: خیو (xayu)

## Meaning
An archaic term for "spit" or "saliva." Synonyms include تُف (tof), آب دهان (âb-e-dahân), and بُزاق (bozâq).

## Etymology
The word derives "From Middle Persian" with the form listed as xayug, meaning "spit, saliva." The entry notes a script is needed for the Middle Persian representation. No Proto-Iranian forms are provided in this source.

## Alternative Forms
- خَدو (xadu)

## Cited Example
Saʿdī used the term around 1260 in his obscene poetry collection. The example reads: "Wherever you see a tall cypress[-like beauty], Look at his face and spit in your fist!"

## References
The entry cites the Dehkhoda Dictionary (1931–), compiled by Ali-Akbar Dehkhoda at the University of Tehran Press, as the primary reference.

**Note:** The Wiktionary entry indicates Middle Persian etymology but does not provide detailed Proto-Iranian etymological reconstruction beyond the immediate Middle Persian ancestor.
```


## [2026-09-14T03:13:51.777Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD xay ===\"; grep -n \"xayōg\\|xayog\\|xay \\|spittle\\|saliva\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD xwēy sweat ===\"; grep -n \"xwēy\\|xwed\\|xwēd\\|sweat\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "MacKenzie for xayōg and xwēy"
}
```


### [2026-09-14T03:13:51.852Z] TOOL RESULT

```
=== PHD xay ===
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:3504:saliva xayüg.
PHD.txt:3779:spittle xayūg.
PHD_mackenzie.txt:5552:xayiig [he)dwk ' I N xayii] saliva, spittle.
PHD_mackenzie.txt:7627:  sophist sofista.                      spittle xayug.
=== PHD xwēy sweat ===
PHD.txt:665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
PHD.txt:2042:fresh sabz, tarr, xwēd, zargón.
PHD.txt:2043:freshness xwēdīh.
PHD.txt:2523:kin-marriage xwēdēdah.
PHD.txt:2839:moist naft, tarr, xwēd.
PHD.txt:3908:sweat (n.) xwēy.
PHD.txt:3909:sweat (v.) xwistan.
PHD_mackenzie.txt:5662:xwed [hwyt' I M xwyd, N ......] moist, fresh.
PHD_mackenzie.txt:5664:xwedodah [hwytw(k)ds, -d't' = Av. xV aetwada8a-] kin-marriage.
PHD_mackenzie.txt:5673:xw~y [hwyd I N xway] sweat, perspiration.
PHD_mackenzie.txt:5674:xwistan [hwystn ] sweat, perspire.
PHD_mackenzie.txt:6626:forbearance siixtiirih, wixsayisn(ih).       fresh sabz, tarr, xwed, zargon.
PHD_mackenzie.txt:6627:forbearing wixsayisnig.                      freshness xwedih.
PHD_mackenzie.txt:6916: investigate wizostan.                     kin-marriage xwedodah.
PHD_mackenzie.txt:7121:moist naft, tarr, xwed.
PHD_mackenzie.txt:7122:moisture nam, xwedih.
PHD_mackenzie.txt:7718:stuff iigandan.                            sweat (n.) xwey.
PHD_mackenzie.txt:7719:stumble skarwidan.                         sweat (v.) xwistan.
PHD_mackenzie.txt:12013:xwedodah          ,.vu "ta lA'                 handarz                         ~t"'
```


## [2026-09-14T03:13:53.921Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n \"xayōk\\|xayok\\|xwēy\\|xvēy\\|Schweiss\\|Speichel\" NYB_vol2_glossary.txt | head -20; echo \"=== CHEUNG hwaid ===\"; grep -n \"HWAID\\|hwaid\\|xwēy\\|sweat\" CHEUNG.txt | head -20",
 "description": "Nyberg and Cheung"
}
```


### [2026-09-14T03:13:53.990Z] TOOL RESULT

```
=== NYB ===
=== CHEUNG hwaid ===
10078:*huaid ‘to sweat’ 
10080:*AVESTAN: ҮАУ. x’is- ‘to sweat’ c» Liste: 18 
10084:*MIDDLE PERSIAN: BMP hwyd /xwéy/ ‘sweat’ 
10088:*KHOTANESE: ОКЪ. hv! ‘sweat’ || (+ *a-) LKh. ähus- ‘to sweat? = SGS: 13 
10091:*SOGDIAN: BSogd. xwys (inch.) ‘to sweat’ 
10095:*CHORESMIAN: m/xs- ‘to sweat’? = Samadi: 242 
10098:‘to make wet, moisten’, NP (obs.) x'ay, Bal. héd, Kurd. xwih (f.) ‘sweat’ 
10101:soaked’, Oss. І. xid, D. xed, Pash. xwala, M. xala, Yzgh. x" 10 ‘sweat’, Sh. x&6, Bart. 
10102:хід ‘dirt’, Sariq. xeyó ‘dirt; sweat’ || (+ *pati-) Pash. parxél, рахе! (m.) ‘causing (an 
10103:invalid) to sweat’ 
10105:*SANSKRIT: sved ‘to sweat’ (RV+) = EWAia II: 798 
10113:«PIE *sueid- ‘to sweat’? — LIV: 607 f. | Pok.: 1043 
10115:*IE COGNATES: Latv. svíst ‘to sweat’, Gr. tpos (m.), Lat. südor (m.), Toch. B 
10116:syelme, Latv. sviédri, OHG sweiz, Engl. sweat, etc. 
53765:sweat, 144 
58030:to sweat
```


## [2026-09-14T03:14:16.093Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==297' BQT_v1_pages.txt | head -60",
 "description": "BQT vol1 p.86 (اپیون)"
}
```


## [2026-09-14T03:14:16.932Z] TOOL CALL #50: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1266 2>&1 | head -60",
 "description": "BQT p.1266 via ref_page"
}
```


### [2026-09-14T03:14:17.375Z] TOOL RESULT

```
بچهُ با رسیده را گویند که از شکم ۱
و حبوان دمگر بیفتد .
اپرنداخ است که نیماح وسختیان باشد .
ایسان « بروزن یکان» سنگه فان‌را
گوینه . و آن منگی است که چبزها بدان
تیز کنند وسربی «مسن» خوانند .
ایشا « بان قرشت بر وزن تفزلد »
شبم را گویند » و آن رطوبتي است که شبها
بر سبزه و غیره نشیند ۷ . ۱
ایگافه » با کاف فارسی بروزن افانه,
بیان چهارم
در همزه با تای قرشت مشتمل بر نه لفت
شراز را اتابك ازآن‌جهت م یگفتند که سمدین
زنگی اتابك سلطان سنجر بود و سلطان او را
حاکم فاری کرد‌بود و اویمد ازفوت سنجرخطاب
اتابکی جخود قرار داد ۵ . کویند این‌لفت‌تر کی
است و (۱) اتاسك است یعنی پدر بز رک چهاءا
. پدر است وسك بز رکه ٩‏ ۰
ا ییون بروزن و معتی افیون است که
ترباك باشد ؟ .
ات « بفتح اول و سکون ثانی » نمیر
مشاطب‌است بمحنی‌نو, چنادکه کویند « خاندات »
و «کاشانهات» بمنی خانة تو و کاشانة نو ۴ *
اقا باث س با بای ابجد بروزن چکوكه »
نگاه دارنده - و ادب آموژنده را کوند وملو2
(۱) چك :-
۳ رلك: مشلشه. ۳ ۳ ر4: اپرنداخ,پر نداخج. ۳ ازیونانی 0010۳ مبدل
5 لانینی 60۳1110 ( بمعنی مایم ) » وآن‌شیرة مه تخمدانهای ناری‌خشضاش ۳۵۳۲۵۷6۲
0 است: دا ثرا لمعارف اسلام: افبون» «تفی:افیون»دردیوان‌ناص خسروص۳۲۹«هییون»
باه شدم. . ۴ رثلء ص : 2 از دسباچه مولف . ۵ دولت سلجوقی براسای لشکری فائم‌بود
وفرماندهی لسکرها را یز غلامان در دست داشتند وچون مردم آزاد در دولت‌سلجوفی‌نمتوادتند
بمقامات عالِهُ لشکری وحکومت ولابات دوردست برسند . غلامان زرخرید. راکه دیگران بدربار
سللاجقه بعنوان‌هد به‌فیستاده‌بودند. وامتحان وفاداری‌نت بمضدومان‌خودداده ماین‌مقامات میگماشتند ۰
حربك از ملاجفه عد کثری از این مماليك همراه داشت ت که بیشتر این را هم از دشت
قبجاق آورده بودند وامیر سلجوقی ادار؛ امور درباری و لشکری خود را بمهده آنان وام ی گذاشت
شبجه آن شد که عده‌ای از غلامان تازه نفی جای امرای فرسود؛ قدیم را کرفتند وچون ضعف
سلاجقه مشهود شد وقوام دولت ایشان درهم شکت ۰ اين مماليك که بنام مضومان خود جنگها
کرده بودند بانابکی بعنی سریرستی شاهزادگان جوان ملجوقی برقرارشدند و شد بتدریج در این‌ثفل
بنفع شاهزادکانی که تحت للکی امان‌بودند یم کی دند و ملسله‌هايی درنقاط مختلف کشوریهناور
سلجوقی تشکیل دادند از آن جمله اتابکان دمشق باآد بوری ( ۱۹۷-۵6۹ ) ؛ اتابکان الجزبره
و ما امرای زنگی (4,۲۱؟) , اتایکان موصل (1۳۱-۵۲۱) واتابکان شام (۵4۱ - ۵۷۷)
بقیه در صفعة ۸۷
```


### [2026-09-14T03:14:18.789Z] TOOL RESULT

```
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1266.txt]
[Borhan-e Qate', ed. Mo'in, printed p. 1266 (running head شستگانی; vol. 3 pdf p. 57).
Read from the page image by a vision model, 2026-09-06.]

بیان یازدهم
در شین نقطه‌دار با شین نقطه‌دار مشتمل بر بیست و نه لغت و کنایت

شش ● بفتح اول عددی است معروف ۵ ـ وضم اول چیزیست سفید بسرخی مایل مانند
گوشت وبجگر متصل است ۶ وبادزن ومروحهٔ دل باشد ـ وکنایه از پستان نرم وسست
وآویخته هم هست .        [a woodcut of a pair of lungs, captioned شش]

شش آماسیده ـ بضم اول ، کنایه از مردم بددل وبدد اندرون ونامرد باشد .

شش انداز ـ بروزن پس انداز، کسی را گویند که شش بجول بازی میکرده باشد …

--- footnotes (bottom of p. 1266) ---
(۱) چنی : شنجة(۱) .   (۲) چك : ـ نقطه دار .   (۳) چك: گویند.
۱ ـ رك: شستن (ح) .   ۲ ـ از: شت (نشت) + گانی (پیوند نبت) .
۳ ـ ز قلب درکه اوساز شستگانی عمر / که قلب کعبه‌بود شستگانی محراب . «ابوالفرج رونی ۲۰» .
۴ ـ اسم مفعول از «شستن»(بضم اول، ونیز وبفتح آن بمعنی نشسته) .
● ـ وآن شمار است بین پنج وهفت، دو برابر سه؛ اوستا xshvash (خشوش) ، پهلوی shash ،
هندی‌باستان shásh ، ارمنی veç ، کردی shesh ، افغانی shpazh ، استی äxsäz ، وخی shâdh, shâl
بقیه در صفحهٔ ۱۲۶۷
```


## [2026-09-14T03:14:33.705Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==54' GPL.txt | head -50",
 "description": "GPL p.41"
}
```


### [2026-09-14T03:14:34.978Z] TOOL RESULT

```
the adjective precede the substantive the ی‎ or * of indefiniteness must be affixed to the noun; ۰.8. بندی دادی‎ ASS ‘good counsel hast thou given’; tS eB سکی‎ استخوانی می خورد‎ ‘a hungry dog was eating a dry bone’. Similarly, if the substantive is in the plural, it alone takes the زی‎ e.g. مردمانی خوب‎ ‘(some) good men’; بندگانی صادق‎ ‘ true (or loyal) servants’.
§ 39. Adjective used as a Subst. An adjective, whether Persian or Arabic, may be used substantively, and in that case it will be treated in every respect as a substantive; e.g. bls a learned man’; دانایان عصر‎ ‘the learned men of the age’; Jol» ‘an ignorant man’; yw ele ‘ignorant men’ ; بدهای آشعارش‎ ‘the bad things in (lit, of) his poems’,
In the rare cases which occur of a noun in the plural number in construction with what appears to be an adjective also in the plural it is generally considered that the ‘ adjective’ is used substantively in apposition. Such instances are—
Faithful servants بندگان مخلصان‎ Worldlywise sages asin پیران‎ Valiant heroes مردانن دلاوران‎
DEGREES OF COMPARISON §40 a. The comparative degree of adjectives (Persian or Arabic) is formed by adding the suffix ثر‎ tar to the positive, and the superlative by adding ین‎ in to the comparative ; e.g. ده‎ ‘good’, بهتر‎ ‘better’, بهترین‎ ‘best’; wo ‘bad’, بدتر‎ (generally contracted to بثر‎ battar, and often to بتر‎ batar) ‘worse’, بدترین‎ (contrac
```


## [2026-09-14T03:14:37.077Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AE%DB%8C%D9%88/",
 "prompt": "What do the Dehkhoda (لغت‌نامه دهخدا) and Mo'in (فرهنگ معین) entries say for خیو? Quote the definitions and any etymological bracket such as [پهلوی ...] or a footnote from برهان قاطع."
}
```


### [2026-09-14T03:14:41.752Z] TOOL RESULT

```
# Definitions from Persian Dictionaries

**Dehkhoda (لغت‌نامه دهخدا):**
"تف ، آب دهن ، خلشک" (spit, saliva, dryness) with the notation [پهلوی: xadūk] [قدیمی] indicating Pahlavi origins.

**Mo'in (فرهنگ معین):**
"آب دهان ، تف . خدو و خوی نیز گویند" (saliva, spit; also called خدو and خوی) marked with the grammatical note [په . ] (اِ. ) for category classification.

Both entries present the word as a noun denoting oral secretion, with Mo'in additionally documenting regional variant forms.
```


## [2026-09-14T03:14:48.816Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"shash\\|shāsh\\|CARDINAL\\|NUMERALS\\|Numerals\" GPL.txt | head -20",
 "description": "Find numerals in Platts grammar"
}
```


### [2026-09-14T03:14:48.874Z] TOOL RESULT

```
54:NoumERALS, 41. Words used Idiomatically in Numbering, 43. Dis- tributive Numerals, 44. Multiplicative Numerals, 45. Approxi- mate Numbers, 45. Fractional Numbers, 46. Adverbial Numbers, 46. Pronoun, 46. Independent Personal Pronouns, 47. Affixed Personal Pronouns, 50. Reflexive Pronouns, 52. Demonstrative Pronouns, 54. Relative Pronouns, 58. Inter- rogative Pronouns, 62. Indefinite Pronouns and Nouns, 65.
64:DrnominativE Nouns. Noun of Unity, 169. Noun denoting Vessel or Receptacle, 170. The Relative Adjective, 170. The Abstract Noun of Quality, 171. The Diminutive, 172. Formation of Feminines from Masculines, 172. Number, 173. The Dual, 173. Regular Plurals, 173. Broken Plurals, 174. The Plural of the Plural, 180. The Declension of Nouns, 180. The Numerals, 181.
66:Construction of the Numerals, 182. Fractional Numbers, 183. Pronominal Suffixes, 183. The Demonstrative Pronoun, 183.
520:Numerals—The Cardinal Numbers Al
523:IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
539:60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
571:C: Disrrisutive NUMERALS § 52. Distributives are formed 1) by the repetition of a simple ~
2550:Tar NUMERALS I. The Cardinal Numbers
2565:ConsTRUCTION OF THE NUMERALS
2575:DistRIBUTIVE NUMERALS
3270:§ 15. Rules for the Agreement of the Verb with the Subject. Rule. A Singular Subject takes a Verb in the Singular and a Plural Verb follows a Plural Subject when that is animate :— بزد و گفت‎ yd pw pisar na‘ra bizad va guft ‘the boy shouted and said ’, Bod مدتران مشورت‎ mudabbiran mashwarat kardand ‘the ministers took counsel together ’. * a sz بر‎ _ بر و گذرا ند‎ Ge و‎ va khala@ig bart guzarand ‘and people would pass over them’. و مان برو شاشند‎ va sagan bara shashand ‘and dogs would micturate upon it’. In the case of animals, however, a Plural Subject sometimes takes the verb in the Singular :— نمی توانستم دانستن که‎ rami tavanistam danistan ki gusfandan az ns beg فندان‎ Si chi kamtar mishavad ‘I could not divine
```


## [2026-09-14T03:14:54.419Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '518,545p' GPL.txt",
 "description": "GPL cardinal numbers p.41"
}
```


### [2026-09-14T03:14:54.474Z] TOOL RESULT

```
$45. The adjective of astonishment also belongs distinctly to the class of intensive adjectives. It is formed by adding the suffix تا‎ (sdle (الفب‎ to the simple adjective; as بدا‎ ‘how bad! or very bad’ (is) ; Te ‘how great, very great’ (is); Ly ‘how many’! خوشا‎ ۴ pleasant! how lovely’! In construction it usually precedes the sub- stantive, which often has a redundant |, called کلام‎ oe call ‘alif of ornamentation of speech’, or صوت‎ Se الف‎ ‘alif of extension of sound of the voice’, affixed to it; e.g. بدا سلطانیا که‎ ‘how bad (or very bad) is the king who . a0 1 بزرگا غلطا‎ “how great (is) the error’! خوشا شیرازا‎ ‘how beautiful (is) Shiraz’! ۱
Rem. The alif at the end of the adjective is by some termed ws? will ‘the .alif of astonishment’, and کثرت‎ will ‘the 0/7 of
Numerals—The Cardinal Numbers Al
excess’; while that at the end of the substantive is called زائد‎ Call ‘the redundant alzf’. It is the latter alzf that also occurs in the
word گفتا‎ (= wa) ‘he said’, This use of alifis not found in Phl. or O.P., it has its origin in modern Persian, and is probably derived from the Arabic: cf. the final ali in the Ar. وا زیدا‎ ‘Oh Zaid’ ! وا امیر الوم تن‎ 8 for the Conumander of the Belvo? ! This alif is called 433231 eet, or in Persian .الف ندیه‎
IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
Units (احاد)‎ 1.1 eb (Phi. gvak; O.P. aiva). 5.0 5%) (O.P. paiicha).
2. ۲ 49 (OP. dea). 6. 4 شش‎ (O.P. khshvash). 3. ۳ sw (O.P. thre). 7. ۷ هفت‎ (O.P. hapta).
4. ۴ چهار‎ or le (O.P. ۲ 8. ۸ هشت‎ (O.P. ashta), 9. 4 35 (O.P. nava).
۱ Tens (عشرات)‎
0 دهد‎ (poet. also) sls (O.P. dasa).
11. ۱۱ یازده‎ (dialec.) 3335, (O.P. aivadasa).
12. ۳ دوانزده . وو دوازده‎ (O.P. dvadasa). 13. ۱۳ وو سیزده:‎ .  هدزنیس‎ (O.P. thridasa).
14. ۱۴ چهارده‎ or چارده‎ ) ۰ chathrudasa).
15. 10 بانزده‎ )0.۳۰ paiichadasa).
16. ۱۰ شانزده‎ )۰ khshvashdasa).
17, ۱۷  هدتفه‎ or هفده‎ (O.P. haptadasa).
18. ۱۸ هزده رهشتده‎ or رتجدة‎ (O.P. ashtadasa).
19. 44 $9353; ,وا زده‎ dialec. نوانزده‎ )۰ navadasa). 20. ۲۰ بیست‎ (Phl. vist; O.P. 0190860
30. r- سی‎ (Phi. sth O.P. thrisat).
40. ۰ 2 Je (Phl. chahal ; O.P. chatvaresata). 50. 0+ Ash (Phi. panchah ; O.P. patichasat).
60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
80. a. هشتاد‎ (Phi. hashtat; O.P. ashtaittt).
90. ۰ - نود‎ (Phi. navat ; O.P. ۵۵۵۸۸(۰
42 A ccidence
Hunpreps (متات)‎ 100. 1.. صد‎ (orig. Jw; Phi. sat; 0:۳, sata), plural les. 200. ۲۰۰ دویست‎ (O.P. duye saite) and to 59. 300 ۳ شیک‎ 500. 6. wah,
THOUSANDS (آلوف)‎ ۱
1000. ۱۰۰۰ هزار‎ (Phi. hazar; O.P. hazanra), plural هزاران‎ or .هزارها‎ 10,000. _\j@ ده‎ or UJ, obs. بیور‎ (Phi. 0200۴ و‎ O.P. baévar).
```


## [2026-09-14T03:15:06.244Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%DB%8C%D9%88%D9%86",
 "prompt": "Give the etymology of Persian افیون and of Arabic أفيون — from Greek ὄπιον? via which language (Syriac, Arabic)? Quote cited sources."
}
```


## [2026-09-14T03:15:09.200Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN opium ===\"; grep -n \"opium\" KLN_1966.txt | head -5; echo \"=== KLN semester ===\"; grep -n \"semester\" KLN_1966.txt | head -5; echo \"=== KLN hexa ===\"; grep -n \"hexagon\" KLN_1966.txt | head -3; echo \"=== LKT afyun ===\"; grep -n -i \"opium\\|afyun\\|afiun\" LKT.txt | head -10",
 "description": "Klein and Lokotsch lookups"
}
```


### [2026-09-14T03:15:09.347Z] TOOL RESULT

```
=== KLN opium ===
8094:codeine,  n.,  an  alkaloid  obtained  fr.  opium  ( chem .) —  Formed  with  chem.  suff.  -ine  fr.  Gk.  xcoScia, ‘poppy  head’,  which  is  rel.  to  x£5o;,  ‘prison’ (lit.  ‘a  hollow  place’),  xcoScov,  ‘bell,  mouth  of a  trumpet,  trumpet’,  xoiXoc  (for  ’xofiXo q), ‘hollow’,  fr.  I.-E.  base  *kew-,  *ku-,  ‘vault;  to be  hollow;  to  swell’,  whence  also  L.  cavus, ‘hollow’.  See  cave,  n.,  and  cp.  codon, codetta,  n.,  a  short  coda  (mus.)  —  It.,  dimin.  of coda  (q.v.)
13839:europium,  n.,  name  of  a  rare  metallic  element (chem.)  —  ModL.,  named  by  its  discoverer,  the French  chemist  Eugene  Demarpay  (1852-1903) in  1896  after  the  continent  Europe.  For  the  end¬ ing  of  europium  see  suflf.  -ium.
17491:heliotrope,  n.,  orig.  a  plant  that  turns  to  the  sun; now  any  plant  of  the  borage  family,  with  frag¬ rant  purple  or  white  flowers.  —  F.  heliotrope, fr.  L.  heliotropium,  fr.  Gk.  vjXioxpoTUov,  ‘helio¬ trope’,  lit.  ‘that  which  turns  toward  the  sun’, fr.  Tpxoc,,  ‘sun’,  and  -xporox;,  ‘turning’,  fr. xpsbreiv,  ‘to  turn’.  See  helio-  and  trope, heliotropic,  adj.,  characterized  by  heliotropism. —  See  next  word  and  -tropic.
17493:Heliotropium,  n.,  a  genus  of  plants,  the  turnsole ( bot .)  —  ModL.  See  heliotrope, heliotype,  n.,  picture  produced  by  heliotypy.  — Compounded  of  helio-  and  type, heliotypography,  n.,  a  process  of  photoengraving.
21243:Derivatives:  laudable-ness,  n.,  laudabl-y,  adv. laudaninc,  n.,  a  poisonous  alkaloid  (chem.)  — Formed  from  next  word  with  subst.  suff.  -ine. laudanum,  n.,  a  tincture  of  opium.  —  A  ModL. word  used  by  the  Swiss  alchemist  and  physician Paracelsus ;  prob.  a  var.  of  L.  ladanum.  See  lada- num,  labdanum.
=== KLN semester ===
24365:* me(n)s -,  ‘moon;  month’,  which  is  traceable  to I.-E.  base  me-,  ‘to  measure’,  the  moon  being  re¬ ferred  to  as  ‘the  measurer  (of  time)’.  See  mete, ‘to  measure’,  and  cp.  month.  Cp.  also  meniscus, meno-,  ‘month’,  menses,  menstrual,  menstruum, bimestrial,  trimester,  semester.
34338:seamster,  also  sempster,  n.,  a  person,  esp.  a man,  employed  in  sewing.  —  ME.  semester, semster,  fr.  OE.  seamestre,  formed  fr.  seam (see  seam)  with  fem.  agential  suff.  -estre  (see -ster).
34519:Semele,  n.,  the  daughter  of  Cadmus  and  the mother  of  Dionysus  (Greek  mythol.)  —  L.,  fr. Gk.  SsuiXr,,  a  Thraco-Phrygian  earth  goddess, fr.  Phrygian  ZsqcXco,  ‘mother  of  the  earth’.  See Franz  Altheim,  Geschichte  der  lateinischen Sprache,  p.  132.  Phryg.  Ze|zeXo>  is  prob.  cogn. with  OSlav.  zemlja,  ‘earth’,  L.  humus,  ‘earth, ground,  soil'.  See  humus, semen,  n.  —  L.  semen,  ‘seed’,  cogn.  with  OSlav. simg,  OPruss.  semen,  ‘seed’,  Lith.  semens  (pi.), ‘seed  of  flax’,  OS.,  OHG.  samo,  ‘seed’,  MHG. same,  G.  Same,  of  s.m. ;  fr.  I.-E.  base  *se(i)-,  ‘to sow’.  Cp.  L.  serere,  ‘to  sow’,  which  derives  fr. *si-sd,  reduplication  of  the  original  base  *se-. See  sow,  v.,  and  cp.  seme,  seminal,  seminary, semination,  disseminate,  inseminate.  Cp.  also season.  For  the  ending  of  semen  see  suff.  -men. semester,  n.,  a  period  of  six  months.  —  G.  Se¬
=== KLN hexa ===
17729:hexad,  n.,  a  group  of  six  things.  —  Late  L.  hexas, gen.  hexadis,  fr.  Gk.  spdcc,  gen.  sljaSop,  T‘a  group of  six’,  fr.  & %.  See  hexa-  and  -ad. hexagon,  n.,  a  plane  figure  with  six  angles  and six  sides  (geom.)  —  L.  hexagonum,  fr.  Gk. E^aytavoc,  ‘having  six  angles’,  which  ,  is  com¬ pounded  of  ifja-  (see  hexa-)  and  -ywvop,  from the  stem  of  ytovla,  ‘angle’.  See  -gon. Derivative:  hexagon-al,  adj. hexagram, n. — Compounded  of  hexa-  and  -gram, hexahedral,  adj.,  having  the  form  of  a  hexa¬ hedron.  —  See  next  word  and  adj.  suff.  -al. hexahedron,  n.,  a  solid  figure  with  six  plane  faces.
34808:sexangle,  n.,  a  hexagon.  —  A  hybrid  coined  fr.  L. sex,  ‘six’  (see  sex-),  and  E.  angle, sexangular,  adj.,  having  six  angles.  —  Com¬ pounded  of  sex-  and  angular.
=== LKT afyun ===
273:[Selbst  aus  gr.  öiriov  entstanden]  'Opium', ebenso  tk.  Hieraus  rum.  afion  'dass.'; bulg.  afion,  serb.  afijun.  Aus  dem  Ar. entstand  der  alte  pharmazeutische  Aus- druck: frz.  affion,  sp.  afion  'Opiumlat- werge'. Ferner  ndl.  amfioen;  pg.  anfiäo 'Opium'.  [DE  191.  Devic  DEt  4. Lammens  Rem  4.  Bern  SiEtWb  24. De  Gids  (1867)  I,  428/9.
```


### [2026-09-14T03:15:11.969Z] TOOL RESULT

```
# Etymology of افیون and أفيون

Based on the Wiktionary source provided:

## Persian افیون

The Persian word derives from multiple pathways. According to the etymology section, "The forms with /f/ and /b/ are from Arabic _أَفْيُون_ (ʔafyūn)" while "that with /p/ is via Middle Persian directly from Ancient Greek _ὄπιον_ (ópion)."

## Arabic أفيون

The Arabic أفيون ultimately traces back to Ancient Greek ὄπιον (ópion), as indicated in the Persian etymology tree showing the Greek term as the source.

## Language Path

The documented transmission route shows:
- **Ancient Greek** ὄπιον → **Arabic** أفيون (and variants أبيون) → **Persian** افیون
- Alternatively: Ancient Greek → **Middle Persian** → Persian (for the /p/ variant)

The source does not explicitly mention Syriac as an intermediary language in this etymological chain. The etymology tree provided traces the word back to Proto-Indo-European _*sokʷós_ (juice) through ancient Greek.
```


## [2026-09-14T03:15:18.596Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '268,276p' LKT.txt; echo \"=== KLN semester full ===\"; sed -n '34519,34523p' KLN_1966.txt; echo \"=== KLN opium headword ===\"; grep -n \"opium,  n\\.\\|opium, n\\.\" KLN_1966.txt KLN_1971.txt | head -5",
 "description": "Lokotsch afyun + Klein semester/opium"
}
```


### [2026-09-14T03:15:18.720Z] TOOL RESULT

```
22.  Berber,  afarag: 'Umzäunung,  eingezäunter  Raum,  Hof eines  Duar'  [s.  hier  Nr.  502].  Hieraus sp.  alfanegue  'Zelt',  worin  also  al  nicht ar.  Art.  ist!    [DE  105/107.
23.  Pers.  äfärin : [Zusammenhängend    mit    pers.  äfrin 'Lob'  Horn  NpEt  S.  10,  Nr.  39,  2];  eben- so ik.  aferin,  woraus  rum.  aferim  'aus- gezeichnet! bravo!'.
24.  Ar.  'äflja:
'Wohlbefinden,  Verzeihung'.  Hieraus sp.  alafia  in  der  Redensart:  pedir  alafia 'um  Pardon  bitten'.  —  Sizil.  lafia,  [in Verbindung  mit  romanischem  7mlle 'tausend']  millafia  od.  millaffia  'über- triebene Liebkosung,  Schmeichelei'. [DE  53.    GrSVociSic  239.
25.  Ar.  aflün :
[Selbst  aus  gr.  öiriov  entstanden]  'Opium', ebenso  tk.  Hieraus  rum.  afion  'dass.'; bulg.  afion,  serb.  afijun.  Aus  dem  Ar. entstand  der  alte  pharmazeutische  Aus- druck: frz.  affion,  sp.  afion  'Opiumlat- werge'. Ferner  ndl.  amfioen;  pg.  anfiäo 'Opium'.  [DE  191.  Devic  DEt  4. Lammens  Rem  4.  Bern  SiEtWb  24. De  Gids  (1867)  I,  428/9.
26.  Berber,  afüs:
'Handgriff  eines  Werkzeuges'.  Aus  dem plr.  ifässen  wurde  pg.  alfeizar  'Griff einer  Säge'.  Etymologie  zweifelhaft. [DE  112.
27.  Bind,  äg:
=== KLN semester full ===
Semele,  n.,  the  daughter  of  Cadmus  and  the mother  of  Dionysus  (Greek  mythol.)  —  L.,  fr. Gk.  SsuiXr,,  a  Thraco-Phrygian  earth  goddess, fr.  Phrygian  ZsqcXco,  ‘mother  of  the  earth’.  See Franz  Altheim,  Geschichte  der  lateinischen Sprache,  p.  132.  Phryg.  Ze|zeXo>  is  prob.  cogn. with  OSlav.  zemlja,  ‘earth’,  L.  humus,  ‘earth, ground,  soil'.  See  humus, semen,  n.  —  L.  semen,  ‘seed’,  cogn.  with  OSlav. simg,  OPruss.  semen,  ‘seed’,  Lith.  semens  (pi.), ‘seed  of  flax’,  OS.,  OHG.  samo,  ‘seed’,  MHG. same,  G.  Same,  of  s.m. ;  fr.  I.-E.  base  *se(i)-,  ‘to sow’.  Cp.  L.  serere,  ‘to  sow’,  which  derives  fr. *si-sd,  reduplication  of  the  original  base  *se-. See  sow,  v.,  and  cp.  seme,  seminal,  seminary, semination,  disseminate,  inseminate.  Cp.  also season.  For  the  ending  of  semen  see  suff.  -men. semester,  n.,  a  period  of  six  months.  —  G.  Se¬
mester,  fr.  F.  semestre,  fr.  L.  seme(n)stris  (for *sex-mens-tris),  ‘of  six  months,  half-yearly’,  fr. sex,  ‘six’,  and  mensis,  ‘month’.  Cp.  L.  menstruus, ‘pertaining  to  a  month,  monthly’,  interme(ri)- stris,  ‘between  two  months’,  and  see  six  and moon.  Cp.  also  menses,  trimester, semi-,  combining  form  meaning  ‘half’.  —  ME., fr.  L.  semi-,  ‘half’,  which  is  cogn.  with  OI.  sami, ‘half’,  a-samih,  ‘not  a  half,  complete’,  Gk. ‘half-’,  (for  *'qjxi-TUi;),  ‘half’,  OE.  sam-,
OHG.  sami-,  ‘half’  (cp.  e.g.  OE.  sam-ewieu, OHG.  sami-quek,  ‘half-alive’).  Cp.  hemi-  and the  first  element  in  sesqui-,  sesterce.  Cp.  also  the first  element  in  sandblind. semi-annual,  adj.,  half-yearly.  —  Compounded  of semi-  and  annual.
semibreve,  n.,  a  note  equivalent  to  half  the  length of  a  breve  (music).  —  Compounded  of  semi-  and breve.
semicha,  also  semichah,  n.  —  See  semikah. semicircle,  n.,  a  half  circle.  —  Compounded  of semi-  and  circle.
=== KLN opium headword ===
KLN_1971.txt:86761:europium, n., name of a rare metallic element 
KLN_1971.txt:111722:Heliotropium, n., a genus of plants, the turnsole 
KLN_1971.txt:167769:opium, n., the solidified juice of the opium poppy, 
KLN_1966.txt:13839:europium,  n.,  name  of  a  rare  metallic  element (chem.)  —  ModL.,  named  by  its  discoverer,  the French  chemist  Eugene  Demarpay  (1852-1903) in  1896  after  the  continent  Europe.  For  the  end¬ ing  of  europium  see  suflf.  -ium.
KLN_1966.txt:17493:Heliotropium,  n.,  a  genus  of  plants,  the  turnsole ( bot .)  —  ModL.  See  heliotrope, heliotype,  n.,  picture  produced  by  heliotypy.  — Compounded  of  helio-  and  type, heliotypography,  n.,  a  process  of  photoengraving.
```


## [2026-09-14T03:15:22.319Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '167769,167780p' KLN_1971.txt; echo \"=== SKT six ===\"; grep -n \"^six\\|six, adj\\|six (\" SKT.txt | head -5",
 "description": "Klein opium entry"
}
```


### [2026-09-14T03:15:22.409Z] TOOL RESULT

```
opium, n., the solidified juice of the opium poppy, 
Papaver somniferum. — L., fr. Gk. 07uov, ‘pop- 
py juice’, fr. ‘vegetable juice’, which is 

prob. cogn. with OSlav. sokd, ‘juice of plants 
and fruits’, Lith. Sakai (pi.), OPruss. sackis, 
Lett, svakas , ‘resin’. Cp. opo-, opodeldoc, 
opiumism, n., the habitual use of opium. — 
Formed from prec. word with suff. -ism. 
opo-, combining form meaning ‘juice’. — Gk. 

6no-, fr. 6tz6<;, ‘juice’. See opium, 
=== SKT six ===
17363:six/ij^.     Sec  BaxageDari&Q.
```


## [2026-09-14T03:15:23.565Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/opium",
 "prompt": "Give the full etymology of \"opium\" — Latin opium, Greek opion, opos, and the PIE root. Also any note about Arabic/Persian afyun."
}
```


### [2026-09-14T03:15:28.119Z] TOOL RESULT

```
# Etymology of "Opium"

Based on the provided source, here is the documented etymology:

**Latin & Greek Origins:**
The word traces back to Latin *opium*, which derives from Greek *opion* ("poppy juice, poppy"). The Greek term is a diminutive of *opos*, meaning "vegetable juice, plant juice, fig curd."

**Proto-Indo-European Root:**
The ultimate source is PIE *\*sokwo-*, denoting "juice, resin." This root also appears in Old Church Slavonic *soki* and Lithuanian *sakaī* (plural, meaning "resin").

**Historical Usage:**
The term entered English in the late 14c., specifically referring to "inspissated juice of the poppy plant" used medicinally from the 17th century onward for pain relief and sleep induction.

**Note on Arabic/Persian:**
The provided source material does **not** contain any information about Arabic or Persian terms for opium (such as *afyun*). To obtain that etymology, you would need to consult additional linguistic sources beyond this etymological dictionary entry.
```


## [2026-09-14T03:15:35.132Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN sweat ===\"; grep -n \"4.57\\|SWEAT\" SYN.txt | head -8; echo \"=== SYN six ===\"; grep -n \"13.16\\|'six'\" SYN.txt | head -8; echo \"=== IEC sweid ===\"; grep -n \"sueid\\|svidos\\|sueidos\" IEC.txt | head -8; echo \"=== IEC seks ===\"; grep -n \"seks-\\|sueks\" IEC.txt | head -8",
 "description": "Buck and Mann lookups"
}
```


### [2026-09-14T03:15:35.459Z] TOOL RESULT

```
=== SYN sweat ===
6785:4.55 SWEAT (sb.)
6826:4.57 VOMIT (vb.)
7092:ON skita, OE scitan, etc., the reg. Gme. vb., and the corresponding sbs., ON skitr, etc., orig. ‘separate’ (as 10 Lat. excrémentum, above) : Lith. skeislt, Lett. gk’iest ‘separate, divide’, Lat. scindere, Grk. oxitw ‘split’, etc., fr. IB *skei-d- beside *skei-t- in Ir. sceithim ‘vomit? (4.57), Goth. skaidan ‘sepa rate’, etc. Walde-P. 2.544. Falk-TorP 992.
12541:Sp. laya, loanword fr. Basque. REW 4957.
32416:Lett. véstule (recent), deriv. of vésts ‘news, message, messenger’, fr. Russ. vest’ ‘news’ (: vedat’ ‘know’, etc.). Mithl.-Endz. 4.571.
=== SYN six ===
13908:wm foul, skoulm 13 e, cord, etc., 1S & pa a ie words are mostly means a Pics denoting ‘tie, fasten’ cognate ee Pefnstening: The applica- Sa jump or protuberance in the body or on a tree is clearly secondary in at, nodus. For the Gme. group as @ whole the view that the latter sense 1s the earlier (cf, Paul, Deutsches Wtb. s.v. Knoten, “bedeutet urspriinglich ‘riind- liche Anschwellung an einem Gegen- stand’”) is favored by the nearest cog- nates like OHG knopf ‘knob, knot’, OF cnoll ‘hilltop’, etc. But in the history of OE cnotta—NIE knot, this sense is chronologically later (NED s.v. knot, sb!, 13-16) and for the prevailing earlier use, cf. the derivative OE cnytta ‘tie with a knot’ (NE knit). i Gre Guua (anything for tying, cov- a te opr),
23356:13.16 More
23561:924 SELECTED INDO-EUROPEAN SYNONYMS 13.16 MORE Grk. —-rAclwy, zAbwy Goth. managiza (maizo, Lith. daugiaus NG meptoadrepos mais adv.) Lett. vairak Lat. _pliis ON metri; fleiri (pl.) ChSl.  bolzjt, MUNOzZE;t, vedte It. pitt Dan. mer; flere (pl.) SCr. vide Fr. plus de Sw. mer; flere (pl.) Boh. _ vic(e) Sp. mas OE ma Pol. —- wiecej Rum. maz mult ME mo; more (sg.) Russ. _bol’Se Ir. mo; lia (pl.) NE more Skt. bhilyas-, bahutara- NIr. —tuilleadh; lia (pl.) Du. meer Av. Srayah- W. mwy OHG = mér, méro; manigiron Br. mut, mutoc’h (pl.)
23595:13.162. Words for the superlative ‘most’ generally go with those for ‘more’, as Grk. mdéicros beside mAciwv, Lat. plirimus beside plis, Goth. managists beside managiza, ON flestr beside fleiri, OE mé@st beside m4, etc.
25160:OHG iomér (iamér, iemér), MHG, NHG immer, fr. eo, io (= OF a, above) and mér ‘more’ (13.16), hence at first only with reference to fut. time, but ac- tually not so restricted. Weigand-H. 1.918. Kluge-G. 262.
25178:A times’ parallel to those for ‘three times’ | (13.44). Grk. woAddxis, with same suffix ¥ | as in zprdxs ‘three times’, NG zoAXés gopés, Fr. bien de fois, Sp. muchas veces, W. llawer gwaith, Br. alies (i.e. a lies) and lies gwech (lies ‘several’ : Ir. lia ‘more’, etc. 13.16), NE many times, etc. Most of these and other similar phrases are omitted from the list. Cf. also Ir. menic (below, 4).
=== IEC sweid ===
17921:sueidh- (1) (suïdh-) ‘dash, fling, hasten’. Cf. suidh- Gk. cf. eithar, adv. "at once? beside ithüs, adj. (1) ('straight, immediate" fr. *suidh-); z-gde in Lat. subitus, adj. ‘sudden’ and per. haps also in in-subidus, adj. (silly, fr. *nsuidh-. For subidus ‘filthy’, see süs ‘pig’, etc.); It. cf. séidim, v. (2) ‘incite’; Li. sviedinys, io, m. ‘missile’ beside svýdis, gs: svydZio, m. ‘fling’; Latv. sviežu, sviest, p. t. sviedu, v. ‘throw, fling’; sviesties, refl. ‘succeed’; (o-gde in) svaidu, inf: -it, v. (1) ‘fling’; ON cf. sviða, f. ‘cutlass’
17922:sueidh- (2) (suidh-) ‘burn, itch, smart’. (For Gk. ídé: Li. svidùs, etc. cf. suid-) Lat. subo, ére, v. (“be in heat fr. *suidh-); OHG (Frankish: Otfr.) swidan, sv. 1. “burn, smart'; Sw. svida, sv. 1. id.; ON svíða, sv. 1. ‘singe, roast’; intr. ‘smart’; *suidh- in sviða, f. “burn, singed object’; sviði, n. ‘smart, burn’; (o-gde in) Cz. svědět, inf. (“itch, fr. *suoidh-)
18048:suidh- “dash, rush, impulse; dashing, impul- sive, quick; forth, straight, immediately'. Cf. sueidh- (1) Oss. cf. xàd, Dig. xwüd, adv. (“at once’. Con- sonantism as in xádág 'selP); Gk. ithús, adj. “straight, direct’; ithüs, gs: -àos, f. "impulse,
18057:attack’; itháo, v. ‘rush, dash, attack’; a-isso, v. id. (*sm-syidhio); cf. har, adv. ‘quickly’. and perh. lék-ithos (‘hasty dish’, i.e. *scram- bled egg'?); Arm. cf. an kujt, adj. ('calm', if for *n-syidhst- ‘not hasty’); Lat. subitus, adj. (*sudden'. Vocalism of dubito, sudus, surus, etc.); cf. also *subidus, adj. (*quickwitted', in the cpd. in-subidus 'slow-witted'; Lat. subo, are & ére "be in heat" is ambig. Cf. suib-. Not as WH); (long-gde in) Li. svystu, inf: svysti, p. t. svydau, v. “fly through the air, whizz’; svydis, gs: svydZio, m. ‘fling’; Olr. side, Ir. sidhe, s. (1) ‘dash, rush’; E dial. to swither ((fling, sweep away”, if fr. OE *swiderian); (e-gde in) Li. sviedZiu, sviesti, v. ‘fling’; sviedis, gs: -dZio, m. id. Cf. sueidh- (1)
18058:suidhlo-, cf. suidh- and sueidh- (1). Onomat. Lat. sübulum, n. queried: ‘reed’ or ‘pipe’; cf. sübulo, gs: -onis ‘piper; Ir. siolla, m. ‘puff, gust
18124:suoidh- (suoidheio) ‘dash, fling’. Cf. sueidh- (1) and suidh- ON sveið, f. ‘swing, impulse’; Li. sváidau, yti, v. ‘fling’; Latv. svaidu, svaidit, v. ‘fling around'
18134:(suoit- (2) ‘smart, burn, itch’. Uncertain variant of type sueidh- (2), q. v.)
=== IEC seks ===
8241:ksueKs (ksueKsti-) ‘six’. Cf. sueks, and WP IT, 522. (Initial uncertain) Skt. cf. sat, sas; Av. x3vas, id. beside xsvasti *60^; Oss. äxsäz; Per. šaš; Arm. vec; Tokh. A sák, B skas; Myc. wek-, we-; Gk. wéks, héks; Hes. cf. (dial.?) xéstrix (with six rows of grains’ of barley); Alb. gjashtë ‘six’; Lat. sex;
```


## [2026-09-14T03:15:37.315Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM افیون ===\"; grep -n \"افيون\\|افیون\" AFM.txt AFM_pages.txt TAD_pages.txt 2>/dev/null | head -10; echo \"=== PLA opium ===\"; grep -n -i \"afyun\\|afyūn\\|Opium\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10",
 "description": "Addi Shir / Asbaghi for afyun"
}
```


### [2026-09-14T03:15:37.404Z] TOOL RESULT

```
=== AFM افیون ===
AFM.txt:6567:ابدان ١"‏ ارمغان ܀ | ܐ افيون ١١‏ 
AFM_pages.txt:4107:ابدان ١"‏ ارمغان ܀ | ܐ افيون ١١‏
=== PLA opium ===
2836:Just - ’ afyün: "Opium, Mohnsaft" pers. 3 wahrscheinlich aus dem pers. 
6063:SAL} - tiryäk: "Opium" = tiryäg, mand. tiriak 4
```


## [2026-09-14T03:15:44.162Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6785,6800p' SYN.txt; echo \"=== PLA ===\"; sed -n '2830,2845p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
 "description": "Buck 4.55 SWEAT and Asbaghi afyun"
}
```


### [2026-09-14T03:15:44.249Z] TOOL RESULT

```
4.55 SWEAT (sb.)
Gtk. 4554, NG Hass Goth. Lith. prakattas Lat. siidor ON  sveiti Lett.  sviedri It, sudore Dan.  sved ChSl.  potit i, ie Sw. _—svelt SCr. — znoj (pot) ae sudor Ris swat Boh. pot eee eae om Sven feet ee Ms, allus Du. —_zweet Skt.  sveda- BR. chtoys Saw sueiz Av. —_-z"atéa-
Oue, Sweiz
NHG _ schweiss
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
on aa’ ee
—— ee eee ee
Digitized by Arya Samaj Foundation Chennai and eGangotri
The majority of the words for ‘sweat’ belong to an inherited group pointing to an IE word for this notion. In most of the others ‘sweat’ is a specialization of ‘heat’. Noun and verb are regularly parallel, and in this case it is the nouns that are listed.
1. Derivs. of IE *sweid- (in part with r-suffix). Walde-P. 2.521. Ernout-M. 997.
Grk. tdpas, NG idpwras (for accent, ef. Hatzidakis, Meo. 1.190, 2.91); Lat. sudor (> It. sudore, Fr. sueur, Sp. sudor, Rum. sudoare); W. chwys, Br. c’houez; ON sveiti, OE swat, etc., general Gme. (ME swet, NE sweat fr. the vb. ME swete, OF sw@tan); Lett. sviedri (pl.); Skt. sveda-, Av. x*aéda-; Arm. k‘trtn, Alb. dirsé, djersé.
2. Rum. nddugeald, fr. nddugi ‘make Sweat, sweat’, fr. ndduf ‘sultriness,
264. SELECTED INDO-EUROPEAN SYNONYMS
closeness, asthma’, this a loanword fr Slavic, SCr. neduh ‘asthma’, etc. 4 ne-+duh beside dah ‘breath’, 4.51), Tiktin 774, 1030. :
3. Ir. allas, NIr. allus, etym.? (Mac. bain 162 as *yas-l- : W. tas ‘boiling seething’, Grk. téw ‘boil’, ete.; not in Walde-P. 1.208, Stokes 228).
4. Lith. prakaitas : kaisti, Lett, kaist ‘become hot’, etc., OHG heiz, ON heitr, OE hat ‘hot’ (parallel ¢- and d- extensions of an IE *kdi-). Walde-P. 1.327,
=== PLA ===

.$ _ - - 
Öbi- ’asyal: PL. v.wfils. fil. 


3 - 
Just - ’ afyün: "Opium, Mohnsaft" pers. 3 wahrscheinlich aus dem pers. 
4 


ab "Wasser, Saft" + mp. „» hom "Ephedra" a. homikan . 


Pe 2 
Jusı - ”agfäl: Pl. v5 qufl.
```


## [2026-09-14T03:15:58.049Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -B3 -A6 \"afyün\\|afyūn\" incoming/PLA/PLA_pages.txt | head -40",
 "description": "PLA pages version of afyun"
}
```


### [2026-09-14T03:15:58.170Z] TOOL RESULT

```
1744-       .$                    _                                       -                  -
1745-Öbi- ’asyal: PL. v.wfils.                                                          fil.
1746-   3                         -
1747:Just            -       ’ afyün:               "Opium,             Mohnsaft"                pers.           3         wahrscheinlich               aus       dem   pers.
1748-                                                                                                                                                         4
1749-         ab "Wasser,                            Saft"          + mp. „»            hom           "Ephedra"                     a.           homikan          .
1750-
1751-       Pe 2
1752-Jusı - ”agfäl:                                 Pl.       v5         qufl.
1753-
```


## [2026-09-14T03:16:16.366Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM p11 ===\"; awk 'BEGIN{RS=\"\\f\"} /افيون/ {print NR\": \"$0}' AFM_pages.txt | head -5 | cut -c1-800",
 "description": "Addi Shir afyun"
}
```


### [2026-09-14T03:16:17.379Z] TOOL RESULT

```
=== AFM p11 ===
164: ® ̄ ® ÷ - 1و
̄ܨ
(010.050:)
الشروحة في هذا اتكتاب
أت 5 1 عب اطاط ܙ ܙ
```


## [2026-09-14T03:16:19.543Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 sueid ===\"; grep -n \"sueid\\|sueid-\\|sṷeid\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== WLD Bd2 seks ===\"; grep -n \"s(u)ek̂s\\|sueks\\|sek̂s\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== Buck SIX ===\"; grep -n \"13.14\\|SIX$\\|13\\.1 \" SYN.txt | head -10",
 "description": "Walde-Pokorny and Buck"
}
```


### [2026-09-14T03:16:20.572Z] TOOL RESULT

```
=== WLD Bd2 sueid ===
34568:520                                              sueid-
34596:1.   sueid- „glanzen, schimmern".
34631:                                     sueid-   — suekuro-s, snekru-s                             521
34635:       sueid- „schwitzeii‘‘.
34666:(s.   *sueid- „Milch‘').
34668:sueid(k)- „Milch“.
=== WLD Bd2 seks ===
34734:     (vermutet fiirs Bsl. Ar. und Arm. idg. *sueks, docb ist eber mit Assi-
=== Buck SIX ===
2563:ly meaningless infantile syllables pa and ma, with suffix added after the analogy of other pairs of contrasted relations, while the simpler forms with or without reduplication, like NE pa, ma, papa, mama, continued in use as pet names. Such infantile syllables or nursery words play a considerable role in the words of relationship. They give rise to pet names of loose application which may become specialized in various directions. A similar use of infantile syllables, es- pecially for ‘father’ and ‘mother’, is ob- served in languages from all over the world. Cf. Kretschmer, HFinleitung 353 ff., and, for Latin, Heraeus, Die Sprache der rémischen Kinderstube, Arch. lat. Lex. 13.149 ff.
17323:ON krjipa, Dan. krybe, Sw. krypa, OE créopan, ME crepe, creep, NE creep, Du. kriupen, fr. IE *greu-b- (: Lith. grubineti ‘stumble’); OHG chriochan, MHG, NHG kriechen, fr. IE *greu-g- (: Ir. grug ‘wrinkle’); extensions of LE *ger- in Lett. griezt ‘turn’ (10.13-14), Lith. greati ‘turn around, bore’, etc. Walde- P. 1.597f. Falk-Torp 585.
18314:Av. vaga- : varat- ‘turn’ (10.13-14). Barth. 1418.
23354:13.14 Every; Au (pl.)
23478:13.14 EVERY; ALL (pl.)
23523:Ty, beaucoup, epd. of beau beautiful, ne and -coup ‘blow’, replaces OFr. nou in 13/14th century. Gamillscheg 92, Wartburg 2,868.
23612:neb ‘any, none’ = Ir. nech ‘any(one)’, fr *ne-k”os (neg. and pron. stem *k9., of. Ir. cach ‘every’, 13.14). Pedersen 2.212,
25143:1. Derivs. or epds. of words for ‘all’ (13.14).
25750:1013 14.76 14.77 SUMMER AUTUMN Oépos POtvérwpov xadoxalpt P0tvorwpo aestas aulumnus estate aulunno été automne verano, estio otono vara toamnd sam, samrad fog(a)mar samhradh foghmhar haf hydref (cynhaeaf) haziv diskar-amzer, dilost-hanv asans Re sumar haust sommer efteraar (h¢st) sommar hést sumor herfest sumer hervest, autum(p)ne summer autumn, fall zomer herfst sumar herbist sumer herb(e)st sommer herbst vasara ruduo vasara rudens Zetva, léto jesent ljeto jesen. leto podzim, jesen lato jester leto osen’ grisma-, nidagha- ¢arad- ham-
```


## [2026-09-14T03:16:27.555Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34635,34670p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD sueid- schwitzen"
}
```


### [2026-09-14T03:16:27.612Z] TOOL RESULT

```
       sueid- „schwitzeii‘‘.
      Ai. svidyati, svedate „schwitzt‘*, svtda- m.            = av. xvaeda- „Schwei6‘‘ (= germ.
"^sivaiia -)
  arm. Hirt-n^ gen. -an „Schwei6“ (rt aus dr^ vgl. gr.       lett. ^imdri\

Gdf. suidro-m^ vgl. zur Uberfiihrung in die ^^-Dekl. Brugmann II ^ 1,313);
gr. Idog (jon.) n.           „Schwei6“,       horn. usw. /dtco, att. ^dtoy ,,schwitze“, ^doc6c,
-wrog^     att.    Idgchg     wohl nach evQcbgj -cbxog „Moder“ aus dem ursprgl. -&-St.
von horn.          dat.    Idgw, acc. Idgoa^ erwachsen aus idg. "^siddro- o-St., Brug-
mann II ^ 1, 531), ldQ(X)(jL) ,,schwitze“ (HdQCjog-i(o)\
  alb. (Pedersen KZ. 36, 288, Jokl SBAk. Wien 168,                            I 92),   dirse^ djerss
„SchweiB‘‘,                     (nach Pedersen mit 5 aus ti im Praes.
                       djers „schwitze‘^
droHio; ist der gr. ^-St. dann doch z. T. altererbt?);
   lat. sudor -oris „Schwei6“ {^suoidos^ de Saussure Msl. 5, 418; vgl. den
                   ^


gr. Os-St)j sUdOy -cLre „schwitzen‘^; kymr. chivys, corn, whys^ bret. cliouez
„Schwei6“ {s aus -d-i-^ oder eher -d-s- mit Schwundstufe des Formans -05?);
ags. swat^   as. swet^ ahd. sivei^ m. ,,Schwei6“, anord. sveiti m. ds.      ahd.            ;


sivizzen (= ai. svidyati) „schwitzen“, Kaus.-Iter. ahd. sicei^^on, mhd. sivei^en
„SchweiB vergieBen, bluten. naB werden*^, mhd. auch „heiB machen, rosten,
in Gluthitze aneinanderhammern, schweifien*' (= ai. sveddyati        schwitzen";
lett. sviedri pi.         „SchweiB'^, svidu^ svlst „schwitzen“.          Curtius ^ 242.   Ai. Jcsvi-
dyati^ MvMate (Lex.) „wird feucht, schwitzt aus, entlaBt einen Saft“ be-
rechtigt nicht zur Annahme eines ursprgl. Anlauts ksu- (Kretschmer KZ.
31, 419), ebensowenig av. xsvXd- „Milch“, das wegen der Bed. fernzubleiben
hat (Charpentier IP. 28, 179f. Anm. 5), iibrigens wohl xsv- aus su- hat
(s.   *sueid- „Milch‘').

sueid(k)- „Milch“.
      Av. xsvM- m. „Milch;             fliissige   Nahrung uberhaupt“, vermutlich zu lit.
sviestas „Butter“,           lett. sviests^   svieJcsts ds.Liden IP, 19, 321 (auch gegen
```


## [2026-09-14T03:16:28.517Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34700,34760p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD six region"
}
```


### [2026-09-14T03:16:28.577Z] TOOL RESULT

```
ist trotz Sommer Hdb.^ 97 unnotig), socrits^ -us „Scbwiegermutter“; cymr.

chivegr, corn, hweger „Schwiegermutter‘', darnach neugebildet cymr. chwegrwn,
corn, hivigeren „Scbwiegervater“; abd, swehur, ags. sweor „Scliwiegervater“,
ahd. swigar^ ags. stveger {^siveyru) „Schwiegermutter‘^;
  got. sivaihro     =
                  anord. sv^ra „Schwiegermutter‘^ (zu ^swehrdn- umgebil-
detes "^swehrU, mit h statt g aus dem im Ost- und Nordgerm. aufgegebe-
nen m.), wozu neugebildet got. sivaihra „Scbwiegervater“ {^stvehran-\ wie
aucb dt. Schiviegervater nacb Schwieger(fnuUer) fiir Scliwdher; lit. sesuras
„Scbwiegervater'‘; aksl. svehry „Schwiegermutter“ {-hr- durcb Diss. gegen
den Anlaut nicbt zu -sr- geworden, Scbulze KZ. 40, 400 Anm. 5), wornach
m. svehr^ „Schwiegervater^^
   Dehnstufig ai. gvagura- „zum Scbwiegervater geb6rig“, abd. stvagur
„Scbwager (*Sobn des Scbwiegervaters), auch Scbwiegervater, Scbwieger-
sobn‘‘ (s. dazu, wie iiberbaupt zu den germ. Formen bes. Scbulze KZ. 40,
400 ff., aucb Falk'Torp u. svoge^'), vielleicht aucb gloss, lat. svecerio {*e);
Jacobsobn KZ. 44, 11, Hartmann Gl. 4, 380.
   Ygl. Curtius^ 136, Fick    152, 578, HI^ 544, Delbruck Yerw. 142, 157,
Schulze aaO. m. Lit.       —
                         Das Wort enthalt den Keli.-St. sue-; Yermutungen
liber den Ausgang bei Berneker IF. 10, 155 (: aksl. surh, hirim „Scbwager“,
das     aber eber als *sieuro zu lat. stiere), Brugmann I^, 260 f., Leumann

ZfdtWtf. 11, 62, Sommer IF. 36, 198 Anm. 2 {-kru als -kur mit -kuro-s zu
vereinigen, was jedenfalls erwagenswerter als Siitterlins IF, 25, 70 Annabme
von t/“Scbwund in -kru- angeblicb aus -^kuru-                 ;
                                                                   ein al testes *suekwr- batte
an *daiuer- formal en AnscbluB).


sneks, seks, neks (;uks) „secbs“.        Zur scbwierigen Anlautfrage vgl. bes.
     Kretschmer KZ. 31, 417 f. (m. Lit), Pedersen IP. 5, 77, KZ. 38, 229
     (vermutet fiirs Bsl. Ar. und Arm. idg. *sueks, docb ist eber mit Assi-
     milationen des Anlauts s- an die s-baltige Auslautsgruppe zu recbnen,
     im einzelnen aber nocb erst Klarbeit zu schaffen), Solmsen Unters. 197,
     206, Cbarpentier IF. 25, 243, Brugmann II ^ 2, 1 7, 55 m. Lit. ; zum Ausl.
     vgl. Bartbolomae ZdMG. 50, 702 Anm. 3 (nicbt iiberzeugend setzt
     Cbarpentier aaO. ~kt an).
  Ai. sat (kis), av.            arm. vec (Hiibscbmann KZ. 27, 106f., Arm. St.
I 51, Pedersen, Cbarpentier aaO.; -c           ks, nicbt nacb Cbarpentier aus
suekts; in vatsun „60‘‘ ist a durcbs flgde. u aus e umgelautet, Pedersen KZ.
39, 416 f.); gr. e^ u. zw. teils urgr.    (boot, ef), teils *s-e^ (lak. kret. delpb.
pamph. j:e^), s. Solmsen KZ. 32, 278 Anm. 1 und am aaO. (knidiscb ^eotqi^
„8echszeilige Gerste” braucht auf keine 3. gr. Form            bezogen zu werden,
Boisacq s. v. m. Lit.); alb. gaste {^gjeste, G. Meyer, Alb. Wb. 138; von
                                                               8uep“, sup-                                                 523

Pedersen KZ. 36, 284 im Auslaut nicht mit ai. sasii-, av. xsvasti^s „60                                                     =
Sechsheit von Zehnem‘‘ gleichgesetzt, sondem wie die 7—9 als Nach-
ahmung von djeie         betrachtet) lat. sex\ air. se, 6. seser „6 Mann“,
                                                                      ;



mor-feser „magnus seviratus, 7 Mann“, cymr. usw. chivech „6‘‘; got. saihs^
anord. sex,                   ahd*
                  seJiS) lit. flektiert     aksl, sesth h (= ai.        Ygl.
lat.            sodaqa 16 ;     xsvaMasa^- „der 16.“). Ordinale: ai. sa^hd-,
                              ai.                      ,
```


## [2026-09-14T03:16:38.886Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"515\\|opos\\|Harz\" incoming/WLD/WLD_Bd2_pages.txt | sed -n '1,20p'",
 "description": "WLD find sekwos entry"
}
```


### [2026-09-14T03:16:38.945Z] TOOL RESULT

```
4898:poi-^ pi „von Feuchtigkeit, Saft, Fett, Milch,                           Harz strotzen, hervorquellen
4978:III^ 241).      Hieher von der Bed. „Harz'' aus ai. plfu-dant „eine Fichten-
4979:art'',   eig. „Harzbaum", und nach Kretschmer KZ. 31,328 als Kurzformen
4984:      Die Bed. „Harz“ auch         in    der ^-Abteilung                  :
18021:   Vgl. Fick KZ. 22, 382, Wb,        108, 515 (aber got. mers usw. s. u. mv-
18240:son     Beitr. 945);        z.   B. Curtius^331, Fick I^ 107f., 285, 515,                                    II‘^   211, III^
18303:u. *mregJiii- „kurz“),  s. Pick    107f., 515 (in Yerbindung mit der wohl ur-
18678:I^ lOS. 515: Lit. zur abweichenden Verb, von pdgnxay mit pagg „Hand“
18729:s. Palk-Torp 699 f., 1515, 1516;  Znpitzas GG. 164 Yerbindung \oxi Marke
18747:109, 285, 515, BB. 28, 98, Chlenbeck Ai.Wb. 229) in gr. djuoQ^og (mit d-
27173:bei Ifacht arbeiten‘‘ (it Each Meyer-Liibke B,om. Wb. Nr. 5150, 5151 gegen
29735:Stamm abgeleitet ist SanquaVts „zum Sancus gehorig'*, Fest. 462, 515 Thd. P.
31074:Harz‘S, mnd. sepe „Seife“, ags. sape f, (daraus nord. sCtpa) „Seife" (sap
31075:„Harz, Pomade'"), vgl. Yf. LEWb.^ u. sapo (germ, Lw.), Schrader RL. 761,
31078:seicJi „Harn“ von Wz. seiJc) oder ein „Eesinat“ (vgl. as. drupil „Harz‘' dt.                :
32234:(idg. *soil6-              de Saussure Msl. 6,217, Li den PBrB. 15,515,
34231:                                                                                                                   515
34267:s(u)aq?o-s „pflanzlicher Saft; Harz“,
34268:     Lett, svakas pL,umgelautet sveh^ is, pi. svek^i „Harz, Gummi“, lit. sakad
34277:36, 285) alb. gak „Blut‘‘. DaS slav. sokh einst auch „Harz“ bedeutet hat,
```


## [2026-09-14T03:16:42.160Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34267,34290p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD s(u)ekwo-s entry"
}
```


### [2026-09-14T03:16:42.214Z] TOOL RESULT

```
s(u)aq?o-s „pflanzlicher Saft; Harz“,
     Lett, svakas pL,umgelautet sveh^ is, pi. svek^i „Harz, Gummi“, lit. sakad
PI.,    apr. sachis              wie in lit, sdpnas
                         ds. (I’-Yerlust                    siiefn\ ob    trotz                            —
des Lett.       —
              ein so alter dial. Yorgang, daB noch der einst labiovelare
Guttural dissimilatorisch wirkte? 'W-los gewesen oder geworden ist auch:)
abg. sokh (skr. sok, g. soka usw., alte Anfangsbetonung) „Saft der Pflanzen
und Friichte'^ mit Ubertragung aufs tierische russ. osoka „Bluteiter‘^, klr.
posoka „Blut eines Tieres“ und (G. Meyer Alb. \Yb. 136, Pedersen KZ.
36, 285) alb. gak „Blut‘‘. DaS slav. sokh einst auch „Harz“ bedeutet hat,
kann man aus der Bed. „Harzbaum'‘ in der gall.-brit. Sippe erschlieBen;
(Meyer- Liibke KZ. 28, 172, E\Yb. Nr. 7592) cymr. syh-ivydd (^: givydd
,,Baume“) „F6hre“, corn, sih-uit „abies“ (allerdings stammen syb-^ sib- aus
Ags.         \^i. sapplmis ,Art Tanne oder Fichte; der untere knorrenlose
                                      3


Teil der Tanne oder Fichte‘‘ mit gallischem 1. Gliede, iibersetztem 2. Gliede
{plniis),      woraus frz. usw. sapin, riickgebildet frz. prov. sap, mlat. sap{p)us
(ags.    Lw. S(Bppe    „Tanne‘^; auch mbret. sap^ nbret. nach prenn „Baum^^;
saprenn „Fichte“ ist ruckentlehnt aus mlat. sappus),                                   Ob dieses *sapos dis-
similatorisch aus "^smpos, "^sunq^os entstanden                               ist,   das einer alten 'Z^-losen
Nebenform entstammt, ist nicht entschieden.                                 —      In der Bed. stimmt eng-
```


## [2026-09-14T03:16:56.242Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%80%CF%80%CF%8C%CF%82",
 "prompt": "Ancient Greek ὀπός: meaning and etymology — PIE reconstruction, cognates (Lithuanian sakai, OCS sokъ), and any note by Beekes. Also is ὄπιον a diminutive of it?"
}
```


### [2026-09-14T03:17:02.446Z] TOOL RESULT

```
# ὀπός: Meaning and Etymology

## Meaning
The Ancient Greek word ὀπός (opós) denotes "juice, vegetable/plant juice," with particular reference to fig-juice used as rennet in cheesemaking.

## Etymology
According to the Wiktionary source, ὀπός derives "From earlier *ὁπός (*hopós), which underwent Ionic psilosis, from Proto-Indo-European *sokʷos ("juice, resin")."

## Cognates
The entry identifies these related words across languages:
- Russian сок (sok, "juice")
- Albanian gjak ("blood") 
- Latin sūcus ("juice")

However, the source notes that "Beekes doubts the pertinence of the Latin" connection.

## Note on ὄπιον
The Wiktionary entry lists ὄπιον (ópion) as a derived term from ὀπός, but doesn't explicitly state whether it functions as a diminutive. The structural relationship suggests a derivative form, though the specific diminutive classification isn't confirmed in the provided content.
```


## [2026-09-14T03:17:13.776Z] TOOL CALL #71: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C|page 490 entry Sweid, node 2: Persian خوی 'sweat' etymology (MP xwēy, PIr *hwaydah, PIE *swóyd-o-s)\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swoyd-|page 490 root Sweid: PIE *sweyd-/*swoyd- 'sweat', Proto-Germanic *swaitaz\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D9%88|page 490 entry Sweid, node 4: Persian خیو 'saliva' from MP xayūg, alt. form خدو\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%B4|page 490 entry Sweks, node 2: Persian شش 'six' from MP šaš, PIr *šwáš, PIE *swéḱs\" \\\n \"https://abadis.ir/fatofa/%D8%AE%DB%8C%D9%88/|page 490 entry Sweid, node 4: Dehkhoda and Mo'in entries for خیو (Pahlavi xadūk)\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%DB%8C%D9%88%D9%86|page 490 entry Swekwo, node 2: Persian افیون/اپیون from Greek ὄπιον via Arabic / MP\" \\\n \"https://www.etymonline.com/word/opium|page 490 entry Swekwo, nodes 3-4: Latin opium < Greek opion < opos, PIE *sokwo-\" \\\n \"https://en.wiktionary.org/wiki/%E1%BD%80%CF%80%CF%8C%CF%82|page 490 entry Swekwo, node 1: Greek ὀπός < *hopós < PIE *sokʷos 'juice, resin'\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-14T03:17:18.374Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d6dc6efee6dae5f8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7d87fcff6a4c5f82.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a088dfc130a5323.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/45bfcf25854c8f39.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8a91d3c1db432286.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0afa1b4103febce9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/86e1898da7f065c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6286e7bdc3f28a77.txt
```


## [2026-09-14T03:17:23.706Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg490.png data/verification/sources/refs/ocr/BOOK/490.png && ls -la data/verification/sources/refs/ocr/BOOK/490.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-14T03:17:23.781Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 73288 Sep 13 23:17 data/verification/sources/refs/ocr/BOOK/490.png
```


## [2026-09-14T03:17:25.977Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY خوی ===\"; grep -n \"خوی\" incoming/ARY/ARY_pages.txt | head -6; echo \"=== ARY شش ===\"; grep -n \"^شش\\|شش‌\" incoming/ARY/ARY_pages.txt | head -6; echo \"=== ARY latin sweid/seks ===\"; grep -n -i \"SWEID\\|SEKS\\|SWEKS\\|SOKWO\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Aryanpur lookups"
}
```


### [2026-09-14T03:17:26.066Z] TOOL RESULT

```
=== ARY خوی ===
25:نیز آورده‌ام تا خویشی زبان‌های ایرانی امروز و رابطه‌ی آنها با پهلوی و اوستایی و پارسی‌باستان و
27:۴- برای نشان دادن خویشی زبان‌های هند و اروپایی و ریشه گیری آنها از یک سرچشمه‌ی
164:شامل سرزمین‌های شمال دریای سیاه و دریای خزر می‌شد. همین خوی کوچگری و تحرکك (به
437:(1767 7۸7۳77 08 880/۸7375 1175) نه تنها خویشی برخی زبانها را نشان داد بلکه
535:رو با زبانهاي یافثی اروپا خویشی دارند. این وضع ادامه داشت تا اینکه دیدمان فرگشت چارلز داروین
540:استدلال کرد شباهت‌های ظاهری میان واژه‌ها هميشه ملا کك همریشه بودن آنها نیست و خویشی واژه‌ها
=== ARY شش ===
863:شش میلیون نفر به این دو زبان سخن می‌گویند.
1256:سوم -بخش دیگری از کوشش‌های من در این کناب صرٍف یافتن ریشه‌های هند و اروپایی
11210:ششم / ۳۷۹
=== ARY latin sweid/seks ===
473:Tg seks | six szese shesht chay
10969:SEKS NORWEGIAN) $95 sik -(TOKHARIAN A) A. jis
10995:SEKS DANISH) jails
11038:SEKSTI NORWEGIAN) (5$55 SHAST PAHLAVI) 5 3h,
```


## [2026-09-14T03:17:31.985Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"SHESH\\|SHASH\" incoming/ARY/ARY_latin_index_pages.txt | head -8; echo \"---\"; sed -n '470,480p' incoming/ARY/ARY_pages.txt",
 "description": "ARY shesh entry"
}
```


### [2026-09-14T03:17:32.076Z] TOOL RESULT

```
6951:POKORNY, = ~~*~*~*«US LO UOSHVIS, SHESHURAS , SHESHIURE
10959:SHESH (KURDISH) 53,5 SHASH s(PAHLAYT) 5 shy
10975:a oP asm SHASH, SHAT, SAS., SAT
10983:SHESHI (LITHUANIAN) gl 3 SEL AUTALIAN) glu!
11017:SAIHSTA GOTHIC) S36 SHASHUM. A(PAHLAVD) 5 Sy,
11042:SHEDESAT (CZECH) So SHASHTI, SASTI:(SANSKRIT) cy Site
13763:‘REFERENCES Wena MICAC, MISHASH, MIZHAGHAN |
---
لصف ها سل هه
[pdf page 19]
۰ / ریشه‌های هندو اروپایی زبان فارسی

8 را ات6 6 6 ۱

00 ی 0 ندید 6 ۲

ل 0 را ۱۵ ۵ ۳

ون ان دت ره وت ۱ ۶۲ | 8۴۵ ۴
```


## [2026-09-14T03:17:38.859Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"خیو\" FSF.txt FRS.txt 2>/dev/null | head -8; echo \"=== HJB opium ===\"; grep -n -i \"afioon\\|afyun\\|opium\" HJB.txt | head -5",
 "description": "Shahnameh glossary + Hobson-Jobson"
}
```


### [2026-09-14T03:17:38.936Z] TOOL RESULT

```
FRS.txt:1555:«أفت را ندارد ۰ نس ۱ زگاب‌خیو [محاف حبر ] باشد ۰ چ: صبر [تجر یف خبر | بأشد 2 
FRS.txt:3217:خیودهان مردم باشد » شید گفت : 
FRS.txt:3324:خیوح باشد و غارجی صبوحی ۳ شا کربخاری ۱ گوید: 
FSF.txt:15277:خیو (بر وزن کدو) 
=== HJB opium ===
1927:1659. — "  I  saw  in  this  month  of  February at  Batavia  the  breasts  torn  with  red-hot tongs  off  a  black  Indian  by  the  executioner ; and  after  this  he  was  broken  on  the  wheel from  below  upwards.  This  was  because through  the  evil  habit  of  ealing  opium (according  to  the  godless  custom  of  the Indians)  he  had  become  mad  and  raised the  cry  of  Amoele  (misp.  for  Amook)  .  .  . in  which  mad  state  he  had  slain  five  per- sons. .  .  .  This  was  the  third  AnKxdc- cryer  whom  I  saw  during  that  visit  to Batavia  (a  few  months)  broken  on  the  wheel for  murder."
1954:1803.— "We  cannot  help  thinking,  that one  day  or  another,  when  they  are  more full  of  opium  than  usual,  they  (the  Malays) will  ran  a  mnek  from  Cape  Comorin  to  the CasmsLti."— Sydney  Smithy  Works,  3rd  ed., iii.  6.
2203:1719. — "We  exchanged  some  of  our  wares for  opium  and  some  axnick.  .  .  .** — Robiiuor^ Cntsoe,  Ft.  II.
2767:1578. — "Baojnie  is  a  plant  resembling hemp,  or  the  Cannabis  of  the  Latins  .  .  . the  Arabs  call  this  Bangne  *Axi**"  (i.e. Hashish).— C.  Aeosta,  860-61. '  1598.— "They  have  ....  also  many  kinds of  Drogues,  as  Amfion,  or  Opium,  <>imfora> Bangne  and  Sandall  Wood." — Linschoten, IdTlBak,  Soc.  i.  61 ;  also  see  ii.  115].
2769:16S8. — "  II  se  fit  apporter  vn  petit  cabinet d'or  ....  dont  il  tira  deux  layettes,  etprit dans  Tvue  de  Vo^on,  ou  opium,  et  dans I'autre  du  bengi,  qui  est  vne  certaine  drogue ou  poudre.  dont  lis  se  seruent  pour  s'exciter  k la  hix.\ire.^*—Mandeltlo,  Paris,  1659,  150.
```


## [2026-09-14T03:17:43.139Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15275,15285p' FSF.txt; echo \"=== FSF خوی ===\"; grep -n \"^خوی\" FSF.txt | head -5",
 "description": "FSF خیو entry"
}
```


### [2026-09-14T03:17:43.208Z] TOOL RESULT

```
دل من ز فرزند خود تیره کرد 
(۳۴۰-۱۵۷-۶) 
خیو (بر وزن کدو) 
آب دهن: 
ز دیدار [گیسوی شیرین ] پیران فرو ماندند 


)۵۳۷ هیوریش٩(‎ 


داد 
=== FSF خوی ===
1329:خویشی با قیصر «پرهیزگار»باش. پرهیز 
3161:خویشتن رابه زه بهمان و احسنت فلان 
11107:خویشی و پیوستگی با فریدون باشد) 
15136:خوی (با زیر اول و واو معدله» بر وزن می) 
15141:خوید (با واو معدله بر وزن بید)
```


## [2026-09-14T03:17:47.152Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15136,15145p' FSF.txt",
 "description": "FSF خوی entry"
}
```


### [2026-09-14T03:17:47.212Z] TOOL RESULT

```
خوی (با زیر اول و واو معدله» بر وزن می) 
عرق تن: 
ز پیش دهستان سوی ری کشید 
ز اسپان به رنج و به تنگ خوی کشید 
(۴۵۰۱-۳۷-۲) 
خوید (با واو معدله بر وزن بید) 
علف نورسته: 
جهان سر به سر سبز گردد ز خوید 
به هامون سراپرده باید کشید 
(۱۰۳-۱۲-۲)
```


## [2026-09-14T03:18:31.151Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN sweat ===\"; grep -n \"sweat,  n\\.\\|sweat, n\\.\" KLN_1971.txt | head -3; echo \"=== KNT xsas ===\"; grep -n \"xsas\\|xšaš\\|xsvas\" KNT_full.txt | head -8; echo \"=== PHD sas ===\"; grep -n \"šaš\\|sas \\[\" PHD.txt | head -5",
 "description": "Klein sweat, Kent, MacKenzie šaš"
}
```


### [2026-09-14T03:18:31.239Z] TOOL RESULT

```
=== KLN sweat ===
238279:sweat, n. — ME. swet, a collateral form of swot, 
238286:sweaty, adj. — ME. swety, fr. swet. See sweat, n., 
=== KNT xsas ===
=== PHD sas ===
564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
3676:six šaš.
4522:> šabestān šafšēr šiftālūg šiftēnag šaš!
```


## [2026-09-14T03:18:39.615Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '238279,238292p' KLN_1971.txt; echo \"=== KNT six ===\"; grep -n \"'six'\\|sixty\\|sixteen\" KNT_full.txt | head -5",
 "description": "Klein sweat entry, Kent six"
}
```


### [2026-09-14T03:18:39.700Z] TOOL RESULT

```
sweat, n. — ME. swet, a collateral form of swot, 
fr. OE. swat , ‘sweat’. See sweat, v. 

Derivatives: sweaty (q.v.), sweat-less, adj. 
sweater, n. — Formed fr. sweat, v., with agential 
suff. -er. 

sweaty, adj. — ME. swety, fr. swet. See sweat, n., 
and adj. suff. -y. 

Derivatives: sweat-i-ly , adv., sweat-i-ness, n. 
Swede, n., a native of Sweden. — LG., fr. MLG. 
Swede. Cp. OE. Sweon , ON. Sviar, OSwed. 
Sviar, Svear, ‘Swedes’. 
=== KNT six ===
```


## [2026-09-14T03:18:42.667Z] AGENT

Now I have everything I need. Writing the verification file.


## [2026-09-14T03:25:10.810Z] TOOL CALL #80: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-490.json",
 "content": "{\n  \"pdf_page\": 490,\n  \"book_page\": 460,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Sweid\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sweyd- / o-grade *swoyd-o- 'to sweat; sweat'\",\n      \"note\": \"Pokorny's 2. sueid- 'to sweat; sweat n.' is printed on p. 1043 — exactly Nourai's citation — and Watkins/AHD has sweid-2 'Sweat; to sweat' [Pok. 2. sueid- 1043]. Language label (Indo-European) and gloss ('sweat') are both right. The one real problem on this chart is the shape of the Avestan word: every source (Pokorny, Walde-Pokorny, Buck, Horn, Hübschmann, Mo'in's footnote in Borhan) writes xᵛaēδa-, with δ, not the chart's 'xvaeza'. The second problem is node #4: Persian خیو 'saliva' is not a member of this family at all but continues MP xayūg (cf. خدو), a separate word. The Germanic reconstruction is also misprinted (swaidaz for *swaitaz).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sweyd- «عرق کردن، عرق» (پوکورنی، ص ۱۰۴۳؛ واتکینز/AHD، sweid-2). برچسب زبانی و معنای ریشه در نمودار درست است. اما صورت اوستایی در کتاب «xvaeza» چاپ شده، حال آنکه همهٔ منابع (پوکورنی، والده-پوکورنی، باک، هرن، هوبشمان و حاشیهٔ معین بر برهان قاطع) آن را xᵛaēδa- با «ذ/δ» می‌نویسند؛ این خطای چاپی خودِ کتاب است نه خطای خوانش اسکن. همچنین «خیو» (آب دهان) از این خانواده نیست و دنبالهٔ فارسی میانهٔ xayūg (همریشه با «خدو») است، و صورت ژرمنی نیز باید *swaitaz باشد نه swaidaz.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swoyd-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:1043\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 83386 'Root / lemma: sueid-2 | Meaning: to sweat; sweat n.' ends 'References: WP. II 521, WH. II 623, Trautmann 295. Page(s): 1 043' — Nourai's page number is exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 521 (incoming/WLD/WLD_Bd2_pages.txt line 34635)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sueid- „schwitzen“. Ai. svidyati, svedate „schwitzt“, svéda- m. = av. xvaeda- „Schweiß“ (= germ. *swaita-)' — the very lemma Pokorny 1043 abbreviates.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. sweid-2 (AHD_watkins1985.txt line 1043)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sweid-2. Sweat; to sweat. I. O-grade form *swoid-. 1. Germanic *swaitaz … [Pok. 2. sueid- 1043.]'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 4.55 SWEAT (sb.), p. 263 (SYN.txt line 6785ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'1. Derivs. of IE *sweid- (in part with r-suffix). Walde-P. 2.521 … Skt. sveda-, Av. xᵛaēδa-; Arm. kʿtrtn, Alb. dirsë, djersé.'\"\n        },\n        {\n          \"src\": \"CHEUNG\",\n          \"where\": \"s.v. *huaid 'to sweat', p. 144 (CHEUNG.txt line 10078ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'*huaid \\\"to sweat\\\" … «PIE *sueid- \\\"to sweat\\\" — LIV: 607 f. | Pok.: 1043'.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.vv. sueidh- (1)/(2), suidh- (IEC.txt lines 17921-18134)\",\n          \"stance\": \"silent\",\n          \"note\": \"Mann lists only the homonymous aspirated roots sueidh- 'dash, fling' and sueidh- 'burn, itch' and suoit- 'smart, burn'; grep for 'sueid' turned up no separate 'sweat' lemma, so Mann is silent on this root.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"xvaeza\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"xvaeza\",\n          \"correct_form\": \"xᵛaēδa-\",\n          \"derivation\": \"The Avestan noun for 'sweat' is xᵛaēδa- (Younger Avestan; PIE o-grade *swoyd-o- > Proto-Indo-Iranian *swáydas > Proto-Iranian *hwáydah, with Iranian *sw- > *hw- > Avestan xᵛ-, and PIE *d preserved as the Avestan voiced fricative δ between vowels). It stands beside the Avestan verb xᵛis- 'to sweat' (the zero-grade *swid-). The chart's 'xvaeza' has z for δ; this is not a form any source knows. The printed page (pdf 490, upper chart) really does read 'xvaeza', so the extraction is faithful and the misprint is Nourai's own — probably a transliteration of the Avestan letter 𐬜 (δ) misread as 𐬰 (z). Everything else about the node is right: Pokorny 1043, Walde-Pokorny II 521, Buck 4.55, Horn no. 513 and Hübschmann all put Av. xᵛaēδa- directly under the root and make it the ancestor of the Persian word.\",\n          \"derivation_fa\": \"واژهٔ اوستایی «عرق» xᵛaēδa- است: از هندواروپایی آغازین *swoyd-o-، از راه هندوایرانی *swáydas و ایرانی باستان *hwáydah؛ در ایرانی *sw- به *hw- و در اوستایی به xᵛ- بدل شده و «د» هندواروپایی میان دو واکه در اوستایی همان δ (ذ) مانده است. در کنار آن فعل اوستایی xᵛis- «عرق کردن» (درجهٔ صفر *swid-) هست. اما کتاب «xvaeza» چاپ کرده که هیچ منبعی چنین صورتی نمی‌شناسد؛ تصویر صفحهٔ چاپی (ص ۴۶۰) نشان می‌دهد خطا از خودِ کتاب است نه از خوانش اسکن — ظاهراً حرف اوستایی δ با z اشتباه گرفته شده. جز همین یک حرف، پیوند ریشه با اوستایی درست و مورد تأیید پوکورنی، والده-پوکورنی، باک، هرن و هوبشمان است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swoyd-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:1043\",\n              \"status\": \"partial\",\n              \"note\": \"Pokorny p. 1043 does put the Avestan word under the root — 'Old Indie svidyati, svedate \\\"schwitzt\\\", sveda- m. = Avestan xvaeda- \\\"Schweiß\\\" (= Germanic *swaita-)' (POK_full.txt line 83390) — but spells it xᵛaēδa-, not the chart's xvaeza.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch, xᵛ- section (BRT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Could not locate a headword for xᵛaēδa- in the OCR: grepped 'vaeda', 'waeda', 'xaeda', 'aeza-', 'hvaeda' and the German glosses 'Schweiss/Schweiß/Schwei.' — only 'Schweissen, Schmelze' (saipa-, col. ~1560) and unrelated hits came back. The xᵛ- entries in this scan are badly garbled, so this is a limitation of the OCR, not evidence against the form.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 521 (incoming/WLD/WLD_Bd2_pages.txt line 34636)\",\n              \"stance\": \"supports\",\n              \"note\": \"'av. xvaeda- „Schweiß“ (= germ. *swaita-)' — δ, not z.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 4.55, p. 263\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. sveda-, Av. xᵛaēδa-' in the list of derivatives of IE *sweid-.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *huaid, p. 144\",\n              \"stance\": \"partial\",\n              \"note\": \"'*AVESTAN: YAv. xᵛis- \\\"to sweat\\\"' — Cheung's Avestan lemma is the verb xᵛis-; he treats the noun under MP xwēy.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien pp. 199-200 and §108 p. ~223 (HUB.txt lines 7069, 7739)\",\n              \"stance\": \"supports\",\n              \"note\": \"'xᵛai \\\"Schweiss\\\" = zd. xᵛaēδa- (also xᵛai aus xᵛaiy)'; and '§108 … xᵛai \\\"Schweiss\\\" = zd. xᵛaēδa-, skr. svēda-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"xay, xoy «خوی»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP خوی (xway/xōy, older xᵛai) 'sweat' continues Middle Persian xwēy [hwyd] 'sweat, perspiration' (MacKenzie, CPD 96), from Proto-Iranian *hwáydah = Av. xᵛaēδa-. The Avestan diphthong aē gives MP ē; intervocalic *-d- is lost in the New Persian outcome so that xᵛaēδa- > MP xwēy > NP xᵛai/xōy, the final -y being what Hübschmann describes as 'xᵛai aus xᵛaiy'. The verb is preserved in MP xwistan 'to sweat'. Nourai's second gloss 'saliva' is not an error: Mo'in himself notes under خیو that 'خدو و خوی نیز گویند', i.e. خوی is also used for spittle. The Ferdowsī line the chart quotes ('ز پیش دهستان سوی ری کشید / ز اسپان به رنج و به تنگ خوی کشید') is given for خوی 'عرق تن' in Nūshīn's Vāzhe-nāmak.\",\n          \"derivation_fa\": \"«خوی» فارسی نو (xᵛai/xōy) «عرق» دنبالهٔ فارسی میانهٔ xwēy است (مکنزی، فرهنگ کوچک پهلوی، ص ۹۶)، و آن از ایرانی باستان *hwáydah = اوستایی xᵛaēδa-. دوواکهٔ اوستایی aē در فارسی میانه به ē بدل شده و «د/δ» میان دو واکه از میان رفته است؛ پس xᵛaēδa- > xwēy > خوی. فعل هم‌خانوادهٔ آن در پهلوی xwistan «عرق کردن» است. معنای دوم «آب دهان» هم نادرست نیست: معین در ذیل «خیو» می‌نویسد «خدو و خوی نیز گویند». بیت فردوسی که نورایی آورده در واژه‌نامک نوشین نیز ذیل «خوی: عرق تن» آمده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:797\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 797 (BQT_v2_pages.txt leaf 257, running head خوید): entry 'خوی - بفتح اول … صید باشد' with the sense 'بروزن می، عرق انسان وحیوانات دیگر باشد'; Mo'in's footnote 5 reads (OCR garbled but legible in pattern) 'پهلوی xvay (xvēy) . اوستا: -xvaēδa . هندی باستان svēda' — i.e. exactly Nourai's chain, and with δ in the Avestan form.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 96 s.v. xwēy (PHD.txt line 665)\",\n              \"stance\": \"supports\",\n              \"note\": \"'xwēy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire.'\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 513, pp. 113-114 (HRN.txt leaf 134-135)\",\n              \"stance\": \"supports\",\n              \"note\": \"'513. xᵛai \\\"Schweiss\\\". aw. xᵛaēδa- \\\"Schweiss\\\" (ZPGl.), vergl. aw. xᵛīsat, xᵛīsaŋ; phlv. xᵛai bezw. xᵛēde … ai. svēda-; arm. kʿirtn … kurd. xā, xōh, xōi \\\"Schweiss\\\"; afg. xwale; oss. xed; bel. hed, n. hīd; wax. xē, sar. xēδ.'\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien §108 (HUB.txt line 7739)\",\n              \"stance\": \"supports\",\n              \"note\": \"'xᵛai \\\"Schweiss\\\" = zd. xᵛaēδa-, skr. svēda-' in the section on ap. uv- / zd. xᵛ- > np. xᵛ-.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *huaid, p. 144\",\n              \"stance\": \"supports\",\n              \"note\": \"'*MIDDLE PERSIAN: BMP hwyd /xwēy/ \\\"sweat\\\" … NP (obs.) xᵛay, Bal. hēd, Kurd. xwih (f.) \\\"sweat\\\"'.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Nūshīn, Vāzhe-nāmak s.v. خوی (FSF.txt line 15136)\",\n              \"stance\": \"supports\",\n              \"note\": \"'خوی (با زیر اول و واو معدوله، بر وزن می) عرق تن: ز پیش دهستان سوی ری کشید / ز اسپان به رنج و به تنگ خوی کشید' — the identical Ferdowsī couplet the chart prints.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"xwys\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian γwyš- /xwēš, xōyš/ 'to perspire, to sweat' is an inchoative stem in -s- built on the zero grade *swid- of the same root (Proto-Iranian *hwaid- / *hwais-), i.e. the exact counterpart of the Avestan verb xᵛis- rather than of the noun xᵛaēδa-; Gharib himself writes '< Av. xᵛisa-, *xᵛisa; MP xwyd', so the arrow drawn from the Avestan box is what Nourai's own source draws. The word is attested in the Vessantara Jātaka and other Buddhist texts (TSP 2.295) and is discussed in Gershevitch, GMS §§228, 539.\",\n          \"derivation_fa\": \"سغدی بودایی γwyš- (خوانش xwēš/xōyš) «عرق کردن» ستاکی است با پسوند آغازی -s- بر درجهٔ صفر همین ریشه (ایرانی باستان *hwaid-/*hwais-)، یعنی دقیقاً برابر فعل اوستایی xᵛis- و نه اسمِ xᵛaēδa-. خودِ قریب در فرهنگ سغدی می‌نویسد «< Av. xᵛisa-, *xᵛisa؛ MP xwyd»، پس پیکانی که نورایی از جعبهٔ اوستایی کشیده همان چیزی است که منبع خودِ او می‌گوید. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:180\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian Dictionary, entry 4503 on printed p. 180 (SOD_pages.txt leaf 246; printed ≈ leaf − 66): '4503 γwyš- B | xwēš, xōyš © <Av. xᵛisa—, *xᵛisa; MP xwyd © (to) perspire, (to) sweat | GMS 228, 539; TSP 2.295; Hen. Texts. 718; Bailey. Prolexis. 23 …'. The English-Sogdian index also gives 'sweat 4503'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *huaid, p. 144 (CHEUNG.txt line 10091)\",\n              \"stance\": \"supports\",\n              \"note\": \"'*SOGDIAN: BSogd. xwys (inch.) \\\"to sweat\\\"' — listed under PIE *sueid-, Pok. 1043, beside Khotanese hvī 'sweat' and Chorasmian m/xs-.\"\n            },\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib, English index (SOD_pages.txt line 39587)\",\n              \"stance\": \"supports\",\n              \"note\": \"'(to) sweat 4503' — cross-checks the entry number against the headword.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"xeyŭ «خیو» (extra: خیوه ۲)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"خیو (xēw/xayū) 'spittle, saliva' does not belong to the 'sweat' root. It continues Middle Persian xayūg [h(y)dwk'] 'saliva, spittle' (MacKenzie, CPD 96), whence also the doublet خدو (xadū); Dehkhoda tags it '[پهلوی: xadūk]' and Mo'in '[په.]'. The two Persian words happen to converge in use — Mo'in notes under خیو that 'خدو و خوی نیز گویند', and that overlap is presumably what led Nourai to hang خیو on Av. xᵛaēδa- — but they are formally distinct: خوی has MP xwēy with initial xw- < *hw- < *sw-, while خیو has MP xayūg with plain x- and a -g suffix, and nothing in it can come from *swoyd-. Nourai's own reference is against him here: Horn's no. 517 on the cited page 114 derives xēw 'Speichel' from 'phlv. xayōk … xaya' and only tentatively compares Av. garəδō.xᵛava-, not xᵛaēδa-; Horn's sweat word is a separate entry (no. 513). The Ferdowsī couplet quoted ('ز دیدار پیران فرو ماندند / خیو زیر لبها برافشاندند') is correctly glossed 'آب دهن' in Nūshīn.\",\n          \"derivation_fa\": \"«خیو» (آب دهان) به خانوادهٔ «عرق» تعلق ندارد. این واژه دنبالهٔ فارسی میانهٔ xayūg «آب دهان» است (مکنزی، ص ۹۶) که صورت دوگانهٔ «خدو» نیز از همان است؛ دهخدا آن را «[پهلوی: xadūk]» و معین «[په.]» می‌نویسد. دو واژه در کاربرد به هم نزدیک شده‌اند — معین خود ذیل «خیو» می‌آورد «خدو و خوی نیز گویند» — و همین همپوشانی سبب شده نورایی «خیو» را زیر اوستایی xᵛaēδa- بگذارد؛ اما از نظر آوایی جدایند: «خوی» از xwēy با xw- (< *hw- < *sw-) و «خیو» از xayūg با x- ساده و پسوند -g. جالب آنکه مرجعِ خودِ نورایی، هرن، در همان صفحهٔ ۱۱۴ (شمارهٔ ۵۱۷) «خیو/خیو» را از پهلوی xayōk/xaya می‌گیرد و نه از xᵛaēδa-. پژوهش امروزی ادعای نورایی را در این گره رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D9%88\",\n            \"https://abadis.ir/fatofa/%D8%AE%DB%8C%D9%88/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:114\",\n              \"status\": \"contradicts\",\n              \"note\": \"Horn, Grundriss p. 114 no. 517 (HRN.txt leaf 135): 'xēw, xēv \\\"Speichel\\\", xīm (Gazophylacium s. v. saliva, Vullers s. v. xīm No. 3). aw. vergl. garəδō.xᵛava- yt. 15, 47 (?); phlv. xayōk (y. 38 (13) Gl.), xaya (Bund.). Justi, Bund. s. v. xayū.' — the page Nourai cites derives the word from Pahlavi xayōk/xaya, not from the sweat word.\"\n            },\n            {\n              \"ref\": \"BQT:805\",\n              \"status\": \"partial\",\n              \"note\": \"Borhan-e Qate' printed p. 805 (BQT_v2_pages.txt leaf 265) has the headword 'خیو - بکسر اول وسکون ثانی وواو، آب دهن را گویند؛ وبفتح اول وضم ثانی هم درست است' — the word and the sense 'saliva' are there, and Mo'in's footnote 4 cross-refers to 'رك: خدو'; the Latin transliterations in the footnote are too garbled in the OCR to read, but nothing on the page connects it to خوی 'sweat'.\"\n            },\n            {\n              \"ref\": \"MON:1472\",\n              \"status\": \"partial\",\n              \"note\": \"Mo'in, Farhang-e Farsi s.v. خیو (vol. 1, near the end of خ; read via abadis.ir which reproduces the Mo'in entry): 'خیو [په.] (اِ.) آب دهان، تف. خدو و خوی نیز گویند.' The Pahlavi tag is there but Mo'in gives no derivation from the sweat word; Dehkhoda on the same page-lookup gives '[پهلوی: xadūk]'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 96 s.v. xayūg (PHD.txt line 661)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'xayūg [h(y)dwk' | N xayū] saliva, spittle' — a separate lemma from 'xwēy … sweat, perspiration' four lines below; the Pahlavi spellings (hdwk' vs hwyd) rule out a common origin.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in via abadis.ir (archived)\",\n              \"stance\": \"partial\",\n              \"note\": \"'آب دهان، تف. خدو و خوی نیز گویند' — records the synonymy of خیو and خوی that presumably produced Nourai's arrow, without asserting a common etymology.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Nūshīn, Vāzhe-nāmak s.v. خیو (FSF.txt line 15277)\",\n              \"stance\": \"supports\",\n              \"note\": \"'خیو (بر وزن کدو) آب دهن: ز دیدار [گیسوی شیرین] پیران فرو ماندند …' — confirms word, sense and the exact Ferdowsī hemistich Nourai prints (the gloss only, not the etymology).\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *huaid, p. 144\",\n              \"stance\": \"silent\",\n              \"note\": \"Cheung's Persian reflexes of *huaid are 'NP (obs.) xᵛay' only; خیو does not appear anywhere under this root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"swaidaz\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"swaidaz\",\n          \"correct_form\": \"*swaitaz\",\n          \"derivation\": \"The Proto-Germanic noun is *swaitaz 'sweat' (with its denominative *swaitjan), from the PIE o-grade *swóyd-o-s: Grimm's law turns PIE *d into Germanic *t, so *swoid- must give *swait-, not *swaid-. Watkins (AHD), the very reference Nourai cites for this box, prints 'Germanic *swaitaz, sweat, with its denominative *swaitjan … in Old English swǣtan'; Walde-Pokorny II 521 likewise writes 'germ. *swaita-'. The chart's 'swaidaz' with -d- is not a form any handbook uses, and the printed page (pdf 490) shows 'swaidaz', so the slip is the book's, not the extraction's. Apart from the one consonant the node is right: OE swāt, OS swēt, OHG sweiz, ON sveiti all continue it.\",\n          \"derivation_fa\": \"صورت ژرمنی آغازین *swaitaz «عرق» است (با فعل برساختهٔ *swaitjan)، از درجهٔ ـُ هندواروپایی *swóyd-o-s؛ بنا بر قانون گریم، «د» هندواروپایی در ژرمنی به «ت» بدل می‌شود، پس *swoid- ناگزیر *swait- می‌دهد نه *swaid-. واتکینز در همان AHD که نورایی ارجاع داده می‌نویسد «Germanic *swaitaz»، و والده-پوکورنی (ج۲ ص۵۲۱) نیز «germ. *swaita-». صورت «swaidaz» در نمودار در هیچ منبعی نیست و تصویر صفحهٔ چاپی نشان می‌دهد خطا از خودِ کتاب است. جز همین یک همخوان، گره درست است: انگلیسی باستان swāt، آلمانی علیای باستان sweiz و ایسلندی باستان sveiti همه دنبالهٔ آن‌اند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swoyd-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 s.v. sweid-2 (AHD_watkins1985.txt line 1043): 'I. O-grade form *swoid-. 1. Germanic *swaitaz, sweat, with its denominative *swaitjan, to sweat, in Old English swǣtan, to sweat: SWEAT.' The reference has the node but with -t-, so it contradicts the chart's spelling while supporting the derivation.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 521\",\n              \"stance\": \"partial\",\n              \"note\": \"'av. xvaeda- „Schweiß“ (= germ. *swaita-)' and 'ags. swāt, as. swēt, ahd. sweiʒ m. „Schweiß“, anord. sveiti m. ds.' — *swaita-, not *swaida-.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 1043 (POK_full.txt line 83403ff.)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Old English swat, Old Saxon swet, Old High German sweiz m. \\\"Schweiß\\\", Old Icelandic sveiti m. ds.; Old High German swizzen (= Old Indie svidyati)' — all with -t-/-z- (< *t).\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"sweat, sweater\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE swāt 'sweat' (n.) and the weak verb swǣtan 'to sweat' < PGmc *swaitaz / *swaitjan; the modern noun is ME swet, refashioned on the verb (Klein: 'sweat, n. — ME. swet, a collateral form of swot, fr. OE. swāt'). 'Sweater' is a 19th-century American formation, 'sweat, v.' + agent suffix -er, first of a garment worn to induce sweating while training (Klein: 'sweater, n. — Formed fr. sweat, v., with agential suff. -er').\",\n          \"derivation_fa\": \"انگلیسی باستان swāt «عرق» و فعل ضعیف swǣtan «عرق کردن» از ژرمنی آغازین *swaitaz/*swaitjan؛ اسم امروزی از انگلیسی میانهٔ swet است که بر پایهٔ فعل بازسازی شده (کلاین ذیل sweat). «sweater» ساختی است آمریکایی از سدهٔ نوزدهم: sweat + پسوند فاعلی -er، نخست به معنی جامه‌ای که ورزشکار برای عرق کردن می‌پوشید. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no refs in the chart; checked against Klein and Watkins instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1971 s.vv. sweat, sweater (KLN_1971.txt line 238279ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'sweat, n. — ME. swet, a collateral form of swot, fr. OE. swāt, \\\"sweat\\\". See sweat, v.' / 'sweater, n. — Formed fr. sweat, v., with agential suff. -er.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, index 'SWEAT sweid-2' (AHD_watkins1985.txt line 2328)\",\n              \"stance\": \"supports\",\n              \"note\": \"English SWEAT is filed under sweid-2, together with SUDORIFIC, SUDATORIUM, SUINT, EXUDE, TRANSUDE, HIDROSIS.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Sweks, Seks\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *s(w)eḱs 'six' (Pokorny sueks, seks, k̂seks, k̂sueks, ueks)\",\n      \"note\": \"Pokorny's lemma 'sueks, seks, k̂sek̂s, k̂suek̂s, ueks (uks)' really is on p. 1044, and Watkins prints 's(w)eks. Six. I. Form *seks … II. Form *sweks in Greek hex. [Pok. sueks 1044.]' — so Nourai's double heading 'Sweks, Seks' reproduces the standard handbook practice of setting up both an s-initial and an sw-initial variant (the initial is notoriously unstable: Pokorny devotes a paragraph to 'Zur schwierigen Anlautfrage'). All four branch nodes are routine and correct. The only thing worth qualifying is the box label 'Avestan / Old Persian': the three forms printed there are Avestan; Old Persian has no attested word for 'six', 'sixteen' or 'sixty' (nothing in Kent's lexicon), and Platts — Nourai's source — simply labels the Avestan forms 'O.P.'\",\n      \"note_fa\": \"مدخل پوکورنی «sueks, seks, k̂sek̂s, k̂suek̂s, ueks» دقیقاً در ص ۱۰۴۴ است و واتکینز نیز «s(w)eks. Six» را با همان ارجاع می‌آورد؛ پس عنوان دوگانهٔ «Sweks, Seks» در نمودار همان شیوهٔ متعارف فرهنگ‌نویسان است (آغازهٔ این عدد در هندواروپایی مشهور به دشواری است). چهار شاخهٔ نمودار همه درست‌اند. تنها نکته برچسب «اوستایی/پارسی باستان» است: هر سه صورت اوستایی‌اند و پارسی باستان هیچ واژهٔ ضبط‌شده‌ای برای شش، شانزده و شصت ندارد (در واژه‌نامهٔ کنت نیست)؛ پلاتس، منبع نورایی، همان صورت‌های اوستایی را «O.P.» برچسب زده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B4%D8%B4\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:1044\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 83568ff.: 'Root/lemma: sueks, seks, k̂sek̂s, k̂suek̂s, uek̂s (: uk̂s) | Meaning: six | Material: Old Indie ṣáṣ (from ṣáṭs), Avestan xšvaš, Armenian vecʿ … Latin sex, Old Irish sé … Gothic saihs …' with 'Page(s): 1044'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. s(w)eks (AHD_watkins1985.txt line 1044)\",\n          \"stance\": \"supports\",\n          \"note\": \"'s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(i)ex, six: SIX. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER … II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.]' — it even supplies the SEMESTER and HEXA- branches Nourai draws.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 522 (incoming/WLD/WLD_Bd2_pages.txt line 34732ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sueks, seks, k̂seks (uks) „sechs“. Zur schwierigen Anlautfrage vgl. … Ai. ṣáṭ (ṣáṣ), av. xšvaš, arm. vecʿ … lat. sex; air. sé …; got. saihs, anord. sex, ahd. sehs …'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. k̂suek̂s (IEC.txt line 8241)\",\n          \"stance\": \"supports\",\n          \"note\": \"'ksueKs (ksueKsti-) \\\"six\\\". Cf. sueks, and WP II, 522. (Initial uncertain) Skt. cf. ṣaṭ, ṣaṣ; Av. xšvaš, id. beside xšvašti \\\"60\\\"; Oss. äxsäz; Per. šaš; Arm. vecʿ; Tokh. A ṣäk, B ṣkas; Myc. wek-, we-; Gk. wéks, héks … Lat. sex;'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"xšvaš; xšvaš-dasa ☞Dekm; xšvašti\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three forms are good Avestan. xšvaš 'six' is the indeclinable numeral (Bartholomae, AirWb col. 562: 'xšvaš indekl. Zw. \\\"sechs\\\"'), from PIE *(k̂)sweḱs with the Indo-Iranian treatment *ćš > Av. xš and *sw > xv. xšvaš.dasa 'sixteen' is the additive compound 'six-ten' (cf. Skt. ṣóḍaśa, Lat. sēdecim); Bartholomae lemmatises the attested ordinal 'xšvaš.dasa- Adj. \\\"der sechzehnte\\\"' and notes it is 'Ableit. aus *xšvaš.dasa indekl. Zw. \\\"16\\\"'. xšvašti- 'sixty' (Bartholomae's xšvaštay- fem. Zw. 'sechzig') is the decad noun in *-ti-, i.e. 'a sixness of tens', exactly parallel to Skt. ṣaṣṭí-. The chart's cross-reference ☞Dekm (PIE *deḱm̥ 'ten') for the second element of 'sixteen' is right. The one qualification is the label: none of the three is attested in Old Persian — Kent's lexicon has no word for six/sixteen/sixty — and Platts, whom Nourai cites, prints the Avestan forms under the heading 'O.P.'\",\n          \"derivation_fa\": \"هر سه صورت اوستایی‌اند. xšvaš «شش» عدد بی‌صرف است (بارتولومه، ستون ۵۶۲: «xšvaš indekl. Zw. sechs»)، از هندواروپایی *(k̂)sweḱs؛ در هندوایرانی *ćš به xš و *sw به xv بدل شده است. xšvaš.dasa «شانزده» ترکیب افزایشی «شش‌ده» است (سنجیدنی با سنسکریت ṣóḍaśa و لاتین sēdecim)؛ بارتولومه صورت ترتیبیِ ضبط‌شدهٔ «xšvaš.dasa- صفت، شانزدهمین» را می‌آورد و می‌افزاید که مشتق از *xšvaš.dasa عدد اصلی «۱۶» است. xšvašti- «شصت» اسم دهگانی با پسوند *-ti- است، یعنی «شش‌تایی از ده‌ها»، درست مانند سنسکریت ṣaṣṭí-. ارجاع ☞Dekm برای جزء دوم «شانزده» درست است. تنها نکته برچسب «پارسی باستان» است که در واژه‌نامهٔ کنت شاهدی ندارد؛ پلاتس نیز همین صورت‌های اوستایی را «O.P.» نامیده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:1044\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny p. 1044: 'Old Indie ṣáṣ (from ṣáṭs), Avestan xšvaš' and, in the ordinals paragraph, 'compare Latin sedecim : Old Indie ṣóḍaśa \\\"16\\\" (Avestan xšvašdasa- \\\"the 16.\\\")'.\"\n            },\n            {\n              \"ref\": \"GPL:41\",\n              \"status\": \"supports\",\n              \"note\": \"Platts & Ranking, Grammar of the Persian Language I, p. 41, the cardinal-numbers table (GPL.txt lines 520-539): '6. ۶ شش (O.P. khshvash)', '16. ۱۶ شانزده (O.P. khshvashdasa)', '60. ۶۰ شصت for orig. شست (Phl. shasht; O.P. khshvashti)' — all three of Nourai's forms, and the two Persian words he prints as 'extra' under the Persian node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AirWb cols. 562-564 (BRT.txt lines 10957-10975)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. xšvaš indekl. Zw. \\\"sechs\\\" … ai. ṣáṭ; np. šaš'; 'j. xšvaštay- fem. Zw. \\\"sechzig\\\" … Ableit. aus *xšvaš. — Vgl. ai. ṣaṣṭí-; np. šast'; 'j. xšvaš.dasa- Adj. \\\"der sechzehnte\\\" … Ableit. aus *xšvaš.dasa indekl. Zw. \\\"16\\\". — ai. ṣóḍaśa- Adj. — Pü.: šāzdahom.'\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon (KNT_full.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for 'six', 'sixteen', 'sixty', 'xšaš', 'xšvaš' in the full lexicon returns nothing — Old Persian has no attested word for these numerals, so the 'Old Persian' half of the box label has no support.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. k̂suek̂s (IEC.txt line 8241)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. xšvaš, id. beside xšvašti \\\"60\\\"; … Per. šaš' — Mann's headword k̂sueKs (k̂sueKsti-) covers both the cardinal and the decad noun.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II pp. 522-523\",\n              \"stance\": \"supports\",\n              \"note\": \"'av. xšvašti-s \\\"60 = Sechsheit von Zehnern\\\"' and 'lat. sēdecim : ai. ṣóḍaśa, av. xšvašdasa- \\\"der 16.\\\"'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"šeš «شِش» (extra: شانزده ، شَست)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP شش (šeš, older šaš) continues Middle Persian šaš [Aramaeogram ŠTA] 'six' (MacKenzie, CPD 80), from Old Iranian *xšvaš: the Avestan-type cluster xšv- is simplified in Middle Persian to š- (as regularly, cf. Av. xšapan- > MP šab 'night'), and the Early NP šaš is raised to šeš in later New Persian. The two 'extra' words follow the same line: شانزده < MP šāzdah < *xšvaš-dasa (Av. xšvaš.dasa), and شصت/شست (šast) < MP šast < Av. xšvaštay- 'sixty' — the modern spelling with ص is a purely orthographic Arabicism, as Platts already noted ('شصت for orig. شست').\",\n          \"derivation_fa\": \"«شش» فارسی نو (کهن‌تر šaš) دنبالهٔ فارسی میانهٔ šaš است (مکنزی، ص ۸۰)، از ایرانی باستان *xšvaš؛ خوشهٔ xšv- در فارسی میانه ساده و به š- بدل شده است (مانند اوستایی xšapan- > پهلوی šab)، و šaš در فارسی نوِ متأخر به šeš برکشیده شده است. دو واژهٔ افزودهٔ نمودار نیز از همین راه‌اند: «شانزده» از پهلوی šāzdah < *xšvaš-dasa، و «شصت/شست» از پهلوی šast < اوستایی xšvaštay-؛ نوشتن آن با «ص» تنها یک املای عربی‌مآبانه است، چنان‌که پلاتس هم یادآور شده «شصت به‌جای صورت اصلی شست». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%D8%B4\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1266\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 1266 (vol. 3; transcription saved at data/verification/sources/refs/ocr/BQT/1266.vision.txt): headword 'شش ● بفتح اول عددی است معروف' with Mo'in's footnote '● ـ وآن شمار است بین پنج وهفت، دو برابر سه؛ اوستا xshvash (خشوش)، پهلوی shash، هندی‌باستان shásh، ارمنی veç، کردی shesh، افغانی shpazh، استی äxsäz، وخی shâdh, shâl' — Avestan xšvaš > Pahlavi šaš > NP شش, exactly Nourai's arrow.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 80 (PHD.txt line 583)\",\n              \"stance\": \"supports\",\n              \"note\": \"'šast [60 | M šst, N ~] sixty. šaš [ŠTA < A št | M š, N ~] six. … šāzdah [c dh | M ?zdh, N šānzdah] sixteen.' — the Middle Persian links for all three Persian words on the chart.\"\n            },\n            {\n              \"src\": \"GPL\",\n              \"where\": \"Platts & Ranking p. 41\",\n              \"stance\": \"supports\",\n              \"note\": \"The cardinal table gives شش, شانزده and 'شصت for orig. شست (Phl. shasht; O.P. khshvashti)'.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Latin index (incoming/ARY/ARY_latin_index_pages.txt lines 10959-11042)\",\n              \"stance\": \"supports\",\n              \"note\": \"The index to the Persian entry for شش lists 'SHESH (KURDISH) … SHASH (PAHLAVI)', 'SHASH, SHAT, SAS., SAT', 'SHASHTI, SASTI (SANSKRIT)', 'SEKS (NORWEGIAN)', 'SAIHSTA (GOTHIC)' — the same comparative set.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"seks\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *seks 'six' from the s-initial variant *seḱs (with the PIE palatal *ḱ giving Gmc *h/x before the cluster simplifies, hence Gothic saihs, OHG sehs, but *seks is the conventional pre-form Watkins prints). Nourai's 'seks : six' is copied straight from AHD.\",\n          \"derivation_fa\": \"ژرمنی آغازین *seks «شش» از گونهٔ آغازه‌دار با s-، یعنی *seḱs؛ «ک» کامی هندواروپایی در ژرمنی به h/x بدل شده و از همین‌روست گوتی saihs و آلمانی علیای باستان sehs، هرچند واتکینز همان *seks را به‌عنوان صورت پیشین می‌نویسد. صورت نمودار عیناً از AHD گرفته شده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. s(w)eks: 'I. Form *seks. 1. Germanic *seks in Old English s(i)ex, six: SIX.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 523\",\n              \"stance\": \"supports\",\n              \"note\": \"'got. saihs, anord. sex, ahd. sehs' under the lemma sueks, seks.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 1044\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gothic saihs, Old Icelandic sex, Old High German sehs' and, in the appended survey, 'Old Germanic+ *seks'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"six, sixteen, sixty\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE siex/six > ME six > NE six; OE sixtīene (six + -tīene 'ten') > sixteen; OE siextig (six + -tig, the decad suffix) > sixty. All three are native Germanic formations parallel to the Iranian set in node #1, not borrowings.\",\n          \"derivation_fa\": \"انگلیسی باستان siex/six > انگلیسی میانه six > انگلیسی نو six؛ sixtīene (six + پسوند -tīene «ده») > sixteen؛ siextig (six + پسوند دهگانی -tig) > sixty. هر سه ساخت‌های بومی ژرمنی‌اند، درست همتای مجموعهٔ ایرانی گرهٔ نخست، و وام‌واژه نیستند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs on the node; checked against Watkins and Klein instead.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, index 'SIX s(w)eks' (AHD_watkins1985.txt line 2268)\",\n              \"stance\": \"supports\",\n              \"note\": \"English SIX is filed under s(w)eks.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. sexangle, hexad (KLN_1966.txt lines 17729, 34808)\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein derives the whole family from L. sex / Gk. hex / OE six, all from the same IE numeral.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"sex\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin sex 'six' < PIE *seḱs, the s-initial variant; Italic cognates Oscan *sehs, Umbrian sehs-, Faliscan zex. It gives Italian sei, French six, Spanish seis.\",\n          \"derivation_fa\": \"لاتینی sex «شش» از هندواروپایی *seḱs، گونهٔ آغازه‌دار با s-؛ هم‌ریشه‌های ایتالیکی: اسکی *sehs، اومبریایی sehs-، فالیسکی zex. بازماندهٔ آن در ایتالیایی sei، فرانسوی six و اسپانیایی seis است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs on the node; checked against Pokorny/Watkins (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 1044\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin sex, Old Irish sé, seser \\\"6 man\\\" … Italic: Oscan+ *sehs, Umbrian+ sehs-, Faliscan+ zex, Latin+ sex'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. s(w)eks\",\n              \"stance\": \"supports\",\n              \"note\": \"'2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"semester\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English semester is a 19th-century borrowing of German Semester (the academic half-year), itself from French semestre, from Latin sēmestris (for *sex-mens-tris) 'of six months, half-yearly', a compound of sex 'six' and mēnsis 'month'. The -x-s- cluster is simplified and the vowel lengthened by compensatory lengthening, giving sē-. The word thus contains the Latin reflex of the numeral drawn in node #5, exactly as the chart has it.\",\n          \"derivation_fa\": \"«semester» انگلیسی وام‌واژه‌ای است از آلمانی Semester (نیم‌سال دانشگاهی) در سدهٔ نوزدهم، و آن از فرانسوی semestre، از لاتینی sēmestris (< *sex-mens-tris) «شش‌ماهه»، مرکب از sex «شش» و mēnsis «ماه»؛ خوشهٔ -xs- ساده شده و واکه به جبران کشیده شده و sē- به دست آمده است. پس این واژه بازماندهٔ عدد لاتینی گرهٔ پیشین را در خود دارد، درست چنان‌که نمودار نشان می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs on the node; checked against Klein and Watkins.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. semester (KLN_1966.txt lines 34519-34520)\",\n              \"stance\": \"supports\",\n              \"note\": \"'semester, n., a period of six months. — G. Semester, fr. F. semestre, fr. L. seme(n)stris (for *sex-mens-tris), \\\"of six months, half-yearly\\\", fr. sex, \\\"six\\\", and mensis, \\\"month\\\" … see six and moon.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. s(w)eks and me- 'to measure'\",\n              \"stance\": \"supports\",\n              \"note\": \"SEMESTER is listed among the Latin sex derivatives under s(w)eks.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Greek\",\n          \"words\": \"hex\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek ἕξ (héx) 'six' shows the sw-initial variant *sweḱs: *sw- > Greek h- (rough breathing), with dialectal Fέξ (wex) in Laconian, Cretan, Delphian and Pamphylian and Mycenaean we- preserving the digamma. This is the branch for which Watkins explicitly sets up 'Form *sweks'.\",\n          \"derivation_fa\": \"یونانی باستان ἕξ (héx) «شش» بازتاب گونهٔ *sweḱs است: *sw- در یونانی به h- (دم درشت) بدل شده، و در گویش‌های لاکونیایی، کرتی، دلفی و پامفیلی صورت Fέξ (wex) و در میسنی we- «واو» کهن را نگه داشته‌اند. واتکینز همین شاخه را «Form *sweks» می‌نامد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs on the node; checked against Pokorny, Walde-Pokorny and Watkins.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 522\",\n              \"stance\": \"supports\",\n              \"note\": \"'gr. ἕξ u. zw. teils urgr. *hek̑s (boot. ϝεξ), teils *s-ek̑s (lak. kret. delph. pamph. ϝέξ)'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. s(w)eks\",\n              \"stance\": \"supports\",\n              \"note\": \"'II. Form *sweks in Greek hex, six: HEXA-, HEXAD.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"hexagon, hexadecimal\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Hexagon comes through Latin hexagōnum from Greek ἑξάγωνον 'having six angles' (ἑξα- + -γωνος, from γωνία 'angle'). Hexadecimal is a mid-20th-century computing coinage (IBM, c. 1954) and a hybrid: the Greek combining form hexa- 'six' prefixed to the Latin-derived decimal (< L. decimus 'tenth'), for base sixteen — so the chart's Greek arrow accounts for the first element only.\",\n          \"derivation_fa\": \"«hexagon» از راه لاتینی hexagōnum از یونانی ἑξάγωνον «شش‌گوشه» (ἑξα- + -γωνος از γωνία «زاویه») آمده است. «hexadecimal» برساختهٔ میانهٔ سدهٔ بیستم در رایانه (شرکت IBM، حدود ۱۹۵۴) و واژه‌ای دورگه است: پیشوند یونانی hexa- «شش» بر سرِ decimal که ریشهٔ لاتینی دارد (از decimus «دهم»)، برای مبنای شانزده؛ پس پیکان یونانی نمودار تنها جزء نخست را توضیح می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs on the node; checked against Klein.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. hexagon (KLN_1966.txt line 17729)\",\n              \"stance\": \"supports\",\n              \"note\": \"'hexagon, n., a plane figure with six angles and six sides (geom.) — L. hexagonum, fr. Gk. ἑξάγωνος, \\\"having six angles\\\", which is compounded of ἑξα- (see hexa-) and -γωνος, from the stem of γωνία, \\\"angle\\\".' Klein also has 'hexad … fr. Gk. ἑξάς, gen. ἑξάδος, \\\"a group of six\\\", fr. ἕξ'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. s(w)eks\",\n              \"stance\": \"supports\",\n              \"note\": \"'HEXA-, HEXAD' listed under the Greek hex branch; hexadecimal is too recent for the 1985 appendix.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Swekwo\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *s(w)ekʷ-o-s / *sokʷ-o-s 'sap, juice, resin'\",\n      \"note\": \"Pokorny's lemma 's(u)ekʷo-s | Meaning: sap, pitch' is on p. 1044, immediately after the numeral, which is why Nourai cites POK:1044 twice on this page. Watkins states the root in the o-grade — 's(w)okʷo-. Resin, juice. Variant form *sokʷo- in Greek opos (< *hopos), juice: OPIUM. [Pok. s(u)ekʷo-s 1044.]' — and Nourai has taken his gloss 'resin, juice' verbatim from that entry while keeping Pokorny's e-grade citation form. Root, label and gloss are therefore all correct; the only caveat is that the Greek word's connection to the Baltic/Slavic 'resin' words, while standard, is not unanimous (Beekes is sceptical of the Latin sūcus comparison).\",\n      \"note_fa\": \"مدخل پوکورنی «s(u)ekʷo-s، معنی: شیره، صمغ» در ص ۱۰۴۴ و بی‌درنگ پس از عدد «شش» است؛ از همین‌رو نورایی در این صفحه دو بار به POK:1044 ارجاع داده است. واتکینز ریشه را در درجهٔ ـُ می‌آورد: «s(w)okʷo-. Resin, juice … یونانی opos (< *hopos) \\\"شیره\\\": OPIUM»، و نورایی معنای «resin, juice» را عیناً از همان‌جا گرفته و صورت استنادی پوکورنی را نگاه داشته است. پس ریشه، برچسب زبانی و معنا هر سه درست است؛ تنها باید افزود که پیوند واژهٔ یونانی با واژه‌های بالتی و اسلاوی به معنی «صمغ» هرچند متعارف است، همگانی نیست (بیکس در سنجش با sūcus لاتینی تردید دارد).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E1%BD%80%CF%80%CF%8C%CF%82\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:1044\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 83686ff.: 'Root / lemma: s(u)ekʷo-s | Meaning: sap, pitch, *blood | Material: Gr. ὀπός \\\"plant juice, resin\\\", ὀπόεις \\\"saftig\\\" … Latvian svakas f. Pl., umgelautet svek'is … Lithuanian sakaī Pl., Old Prussian sackis … abg. sokъ \\\"juice, sap of the plant\\\" … References: WP. II 515 f. … Page(s): 1044'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. s(w)okʷo- (AHD_watkins1985.txt line 1057)\",\n          \"stance\": \"supports\",\n          \"note\": \"'s(w)okʷo-. Resin, juice. Variant form *sokʷo- in Greek opos (< *hopos), juice: OPIUM. [Pok. s(u)ekʷo-s 1044.]' — the source of Nourai's gloss and of the Greek box.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 515 (incoming/WLD/WLD_Bd2_pages.txt line 34267)\",\n          \"stance\": \"supports\",\n          \"note\": \"'s(u)ekʷo-s „pflanzlicher Saft; Harz“. Lett. svakas pl., umgelautet svek'is, pl. svek'i \\\"Harz, Gummi\\\", lit. sakaī pl., apr. sackis ds. … abg. sokъ \\\"Saft der Pflanzen und Früchte\\\"'.\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"Klein 1971 s.v. opium (KLN_1971.txt line 167769)\",\n          \"stance\": \"supports\",\n          \"note\": \"'… fr. Gk. ὀπός \\\"vegetable juice\\\", which is prob. cogn. with OSlav. sokъ, \\\"juice of plants and fruits\\\", Lith. šakai (pl.), OPruss. sackis, Lett. svakas, \\\"resin\\\".'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"hopos, opos : juice; opion : poppy juice\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek ὀπός 'vegetable juice, plant sap' (especially fig-juice used as rennet) goes back to *hopós, from PIE *sokʷos, with the regular *s- > h- and then Ionic psilosis giving the smooth breathing of the attested form — which is why Watkins and Nourai print both 'hopos' and 'opos'. Its diminutive ὄπιον 'poppy juice, opium' is already in Dioscorides and the medical writers of the 1st c. CE. Cognates are Lithuanian sakaī, Old Prussian sackis, Latvian svakas 'resin' and OCS sokъ 'juice'; Beekes doubts the further comparison with Latin sūcus.\",\n          \"derivation_fa\": \"یونانی باستان ὀπός «شیرهٔ گیاه» (به‌ویژه شیرهٔ انجیر که مایهٔ پنیر می‌کردند) به *hopós بازمی‌گردد، از هندواروپایی *sokʷos؛ *s- آغازی طبق قاعده به h- بدل شده و سپس در گویش یونی افتاده است (psilosis) و از همین‌روست که واتکینز و نورایی هر دو صورت «hopos» و «opos» را می‌آورند. مصغّر آن ὄπιον «شیرهٔ خشخاش، افیون» است که در دیوسکوریدس و پزشکان سدهٔ نخست میلادی آمده. هم‌ریشه‌ها: لیتوانیایی sakaī، پروسی باستان sackis، لتونیایی svakas «صمغ» و اسلاوی کهن sokъ «شیره». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BD%80%CF%80%CF%8C%CF%82\",\n            \"https://www.etymonline.com/word/opium\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. s(w)okʷo-: 'Variant form *sokʷo- in Greek opos (< *hopos), juice: OPIUM' — the parenthesis *hopos is exactly the double form Nourai prints.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 1044 s.v. s(u)ekʷo-s\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gr. ὀπός \\\"plant juice, resin\\\", ὀπόεις \\\"saftig\\\", whereof the FN Ὀπόεις'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1971 s.vv. opium, opo- (KLN_1971.txt line 167769ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'L., fr. Gk. ὄπιον, \\\"poppy juice\\\", fr. ὀπός \\\"vegetable juice\\\"' and 'opo-, combining form meaning \\\"juice\\\". — Gk. ὀπο-, fr. ὀπός, \\\"juice\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"apyŭn «اپیون» (extra: افیون)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian word is a Greek loan, as Nourai's arrow says, but it reached Persian by two routes and only one of them is direct. The form with p, اپیون (apyūn) — which Nourai makes the headword — is the direct borrowing of Greek ὄπιον, taken over in the Sasanian/early Islamic period through Graeco-Syriac medical literature and keeping Greek π as p; Nāser-e Khosrow still writes هپیون. The everyday form افیون (afyūn), which Nourai prints as the variant, is the same Greek word returned through Arabic أَفْيُون, where Greek π was rendered f, so it is an Arabic-mediated round trip. Borhan's footnote gives just 'از یونانی opion مبدل' and so covers the loan but not the Arabic leg; Lokotsch treats Arabic afyūn as itself 'aus gr. ὄπιον entstanden' and traces the onward spread to Turkish, Romanian, Bulgarian, Serbian and the old pharmaceutical French affion / Spanish afion. Verdict 'plausible' rather than 'confirmed' only because the chart draws a single direct Greek→Persian arrow for both forms.\",\n          \"derivation_fa\": \"این واژه چنان‌که نمودار می‌گوید وام‌واژه‌ای یونانی است، اما از دو راه به فارسی رسیده و تنها یکی از آن دو مستقیم است. صورتِ با «پ»، یعنی «اپیون»، وام‌گیری مستقیم از یونانی ὄπιον است که در دورهٔ ساسانی و آغاز اسلامی از راه طب یونانی‌ـ‌سریانی وارد شده و «π» یونانی را همچنان «پ» نگاه داشته است (ناصرخسرو هنوز «هپیون» می‌نویسد). صورت رایج «افیون» همان واژه است که از راه عربی «أَفْیون» بازگشته و در عربی «π» به «ف» بدل شده؛ یعنی معرّبی که دوباره به فارسی وام داده شده است. حاشیهٔ معین بر برهان تنها می‌نویسد «از یونانی opion مبدل» و به حلقهٔ عربی نمی‌پردازد؛ لوکوچ نیز «أفيون» عربی را «برآمده از یونانی ὄπιον» می‌داند و پراکندگی بعدی آن را در ترکی، رومانیایی، بلغاری، صربی و صورت داروشناسی کهنِ فرانسوی affion و اسپانیایی afion نشان می‌دهد. داوری «با احتیاط پذیرفتنی» است، چون نمودار برای هر دو صورت یک پیکان مستقیم از یونانی کشیده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%DB%8C%D9%88%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:86\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 86 (BQT_v1_pages.txt leaf 296): headword 'اپیون بروزن ومعنی افیون است که تریاک باشد' with Mo'in's footnote 3 'از یونانی opion مبدل … لاتینی opium … وآن شیرهٔ … تخمدانهای نارس خشخاش Papaver … است: دائرة المعارف اسلام: افیون؛ … در دیوان ناصر خسرو ص ۳۲۹ «هپیون»' — Greek ὄπιον, and even the Latin opium of nodes 3-4.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 25, Ar. afyūn (LKT.txt line 273)\",\n              \"stance\": \"supports\",\n              \"note\": \"'25. Ar. afyūn: [Selbst aus gr. ὄπιον entstanden] \\\"Opium\\\", ebenso tk. Hieraus rum. afion \\\"dass.\\\"; bulg. afion, serb. afijun. Aus dem Ar. entstand der alte pharmazeutische Ausdruck: frz. affion, sp. afion \\\"Opiumlatwerge\\\". Ferner ndl. amfioen; pg. anfião \\\"Opium\\\". [DE 191. Devic DEt 4. Lammens Rem 4 …]'\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen s.v. أفيون (incoming/PLA/PLA_pages.txt line 1747)\",\n              \"stance\": \"partial\",\n              \"note\": \"'أفيون - ʾafyūn: \\\"Opium, Mohnsaft\\\" pers. … wahrscheinlich aus dem pers. āb \\\"Wasser, Saft\\\" + mp. hōm \\\"Ephedra\\\"' — Asbaghi lists the Arabic word among Persian loans (supporting a Persian→Arabic leg) but floats a native āb+hōm etymology that no other source accepts against the Greek origin; the OCR line may also have run two entries together.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, index (AFM_pages.txt line 4107)\",\n              \"stance\": \"partial\",\n              \"note\": \"The index of Kitāb al-alfāẓ al-fārisiyya al-muʿarraba lists 'افيون ١١', i.e. Addi Shir treats Arabic أفيون as a Persian loanword and discusses it on p. 11; the page itself is not legible enough in the OCR to quote.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in via Borhan footnote p. 86 (see ref_check)\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in's own note derives اپیون from Greek opion and equates it with افیون/تریاک.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box standing for Latin opium, the medical Latin borrowing of Greek ὄπιον (2nd declension neuter, current in Pliny and the Latin medical tradition), through which the word reached the western European languages.\",\n          \"derivation_fa\": \"جعبهٔ خالیِ میانی است و نمایندهٔ لاتینی opium، وام‌گیری طبی از یونانی ὄπιον (خنثای صرف دوم، در پلینیوس و سنت پزشکی لاتین)، که واژه از راه آن به زبان‌های اروپای غربی رسیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/opium\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Empty pass-through node with no refs; checked against Klein and Etymonline.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1971 s.v. opium\",\n              \"stance\": \"supports\",\n              \"note\": \"'opium, n., the solidified juice of the opium poppy, Papaver somniferum. — L., fr. Gk. ὄπιον, \\\"poppy juice\\\" …' — Latin is the intermediary, exactly as the empty box implies.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. s(w)okʷo-\",\n              \"stance\": \"supports\",\n              \"note\": \"The single English outcome listed under the root is OPIUM, via Greek.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"opium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English opium is attested from the late 14th century (Chaucer's medical vocabulary) as a direct loan of Latin opium, the sense narrowing from 'inspissated poppy juice' to the medicinal drug used from the 17th century for pain and sleep. The chain Greek ὄπιον → Latin opium → English opium is uncontroversial.\",\n          \"derivation_fa\": \"«opium» انگلیسی از اواخر سدهٔ چهاردهم میلادی (در واژگان پزشکی چاسر) گواهی شده و وام مستقیم از لاتینی opium است؛ معنای آن از «شیرهٔ غلیظ‌شدهٔ خشخاش» به داروی مسکّن و خواب‌آور سدهٔ هفدهم به بعد باریک شده است. زنجیرهٔ یونانی ὄπιον ← لاتینی opium ← انگلیسی opium مورد اختلاف نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/opium\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No refs on the node; checked against Klein and Etymonline.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1971 s.v. opium\",\n              \"stance\": \"supports\",\n              \"note\": \"'opium, n., the solidified juice of the opium poppy, Papaver somniferum. — L., fr. Gk. ὄπιον …'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline s.v. opium (archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"'late 14c., from Latin opium, from Greek opion \\\"poppy juice, poppy\\\", diminutive of opos \\\"vegetable juice\\\" … PIE *sokwo- \\\"juice, resin\\\"'.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T03:25:10.852Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-490.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T03:25:13.194Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-490.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 490",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T03:25:16.814Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'transcription_suspect': 2, 'confirmed': 14, 'disputed': 1, 'plausible': 1}
root verdicts: {'confirmed': 3}
ref checks: {'partial': 4, 'supports': 8, 'contradicts': 1, 'not_checked': 8}
books consulted: {'silent': 3, 'supports': 39, 'partial': 6, 'contradicts': 1} | by book: {'KLN': 7, 'AHD': 7, 'WLD': 5, 'CHEUNG': 4, 'POK': 4, 'PHD': 3, 'BRT': 2, 'HUB': 2, 'FSF': 2, 'MON': 2, 'SYN': 1, 'HRN': 1, 'SOD': 1, 'KNT': 1, 'IEC': 1, 'GPL': 1, 'ARY': 1, 'LKT': 1, 'PLA': 1, 'AFM': 1, 'WEB': 1}
```


## [2026-09-14T03:25:35.512Z] AGENT

Page 490 verified — `data/verification/page-490.json` written, `verify_check.py 490` reports 18/18 nodes, 0 PROBLEM lines.

**Counts** — roots: 3 confirmed. Nodes: 14 confirmed, 1 plausible, 1 disputed, 2 transcription_suspect. Ref checks: 8 supports, 4 partial, 1 contradicts, 8 not_checked (nodes with no refs). 21 books consulted (39 supports).

**Flagged items**
- *Sweid* #1 **transcription_suspect** — Avestan "xvaeza"; every source (Pokorny 1043, Walde-Pokorny II 521, Buck 4.55, Horn 513, Hübschmann §108, Mo'in's footnote in Borhan 797) writes **xᵛaēδa-**. `error_in: book` — the printed page really reads "xvaeza"; δ misrendered as z.
- *Sweid* #5 **transcription_suspect** — Germanic "swaidaz"; the AHD entry Nourai cites has **\*swaitaz** (Grimm's law requires -t-). `error_in: book`.
- *Sweid* #4 **disputed** — Persian خیو "saliva" is not from the sweat root: it continues MP *xayūg* (MacKenzie CPD 96; Dehkhoda "[پهلوی: xadūk]"), doublet خدو. Nourai's own citation HRN:114 contradicts him — Horn no. 517 on that very page derives xēw from Phlv. xayōk/xaya, not from xᵛaēδa-.
- *Swekwo* #2 **plausible** — اپیون is a direct Greek loan, but the usual form افیون came back via Arabic أفيون; the chart draws one direct Greek→Persian arrow for both.

**No extraction errors** — the JSON matches the printed page everywhere, including the Persian scripts, the two Ferdowsī couplets (both confirmed verbatim in Nūshīn's Vāzhe-nāmak) and the "extra" words شانزده/شصت, افیون.

**Notable positives**: SOD:180 resolves exactly to Gharib's p. 180 entry 4503 γwyš- "<Av. xᵛisa-; MP xwyd"; GPL:41 is precisely Platts' cardinal table giving khshvash / khshvashdasa / khshvashti; BQT:1266 already had a saved vision transcription confirming "اوستا xshvash، پهلوی shash". One caveat recorded: the box label "Avestan / Old Persian" overstates — Kent's lexicon has no Old Persian word for six/sixteen/sixty; Platts merely labels the Avestan forms "O.P."

Page image for the two flags copied to `data/verification/sources/refs/ocr/BOOK/490.png`; 8 web pages archived via `fetch_source.py`.
