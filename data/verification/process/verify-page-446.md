# Verification process log — verify-page-446


## [2026-09-14T01:55:59.709Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 446 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-446.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-446.json. Write /home/sfmqrb/git/rishe/data/verification/page-446.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 446` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:00.716Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:01.682Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:01.696Z] TOOL RESULT

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


## [2026-09-14T01:56:02.187Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-446.txt"
}
```


### [2026-09-14T01:56:02.214Z] TOOL RESULT

```
1	=== PDF page 446 (book page 416) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ser 2 : protect  (refs POK:910)
4	#1 (parent #0) [Avestan] refs=POK:910; KLN:338 | haraiti, haurvaiti : protects ; haurva 2 : protecting
5	#2 (parent #0) [Latin] refs=KLN:724 | servâre : to keep, preserve
6	  #3 (parent #2) [French] refs=AHD | conserver, observer, etc.
7	    #4 (parent #3) [Persian] refs=MON:3097 | konserv «کنسرو» : conserve
8	    #5 (parent #3) [English] refs=AHD | conserve, observe, reserve, preserve
9	#6 (parent #0) [Greek] refs=KLN:724 | heros : protector ; Heracles : a legendary strong man
10	  #7 (parent #6) [French] refs=None | 
11	    #8 (parent #7) [Persian] refs=MON5:2269 | herkŭl «هرکول» : "protector"
12	  #9 (parent #6) [English] refs=AHD | hero, Hercules
13	--- entry 1 ---
14	ROOT [Indo-European] Ser 3, Serô : to line up, arrange, sort  (refs POK:911; IEC:1131)
15	#1 (parent #0) [Sanskrit] refs=IEC:1131; MON:5081 | sarat : thread ; hâra : string of beads
16	  #2 (parent #1) [Persian] refs=IEC:1131; MON:5081 | hâr «هار» : string of beads, necklace, neck
17	#3 (parent #0) [Avestan] refs=IEC:1131 | hara : mountain range
18	#4 (parent #0) [Latin] refs=AHD:1538 | serere : to arrange, join ; sors : lot, fortune
19	  #5 (parent #4) [English] refs=AHD | series, assert, insert ; sort, sorcerer, assort, consort
20	  #6 (parent #4) [French] refs=VOP:212 | seri, seriyal
21	    #7 (parent #6) [Persian] refs=VOP:212 | serî «سری ( سریال )» : series
22	--- entry 2 ---
23	ROOT Serô -> redirect to Ser 3
24	
```


## [2026-09-14T01:56:05.235Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-446.json",
 "description": "Read source JSON for page 446"
}
```


### [2026-09-14T01:56:05.279Z] TOOL RESULT

```
{
  "pdf_page": 446,
  "book_page": 416,
  "entries": [
    {
      "root": {
        "name": "Ser 2",
        "lang": "Indo-European",
        "refs": "POK:910",
        "gloss": "protect"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:910; KLN:338",
          "words": [
            {"translit": "haraiti, haurvaiti", "gloss": "protects", "script": null},
            {"translit": "haurva 2", "gloss": "protecting", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:724",
          "words": [
            {"translit": "servâre", "gloss": "to keep, preserve", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "conserver, observer, etc.", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:3097",
          "words": [
            {"translit": "konserv", "gloss": "conserve", "script": "کنسرو"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "conserve, observe, reserve, preserve", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:724",
          "words": [
            {"translit": "heros", "gloss": "protector", "script": null},
            {"translit": "Heracles", "gloss": "a legendary strong man", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON5:2269",
          "words": [
            {"translit": "herkŭl", "gloss": "\"protector\"", "script": "هرکول"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "hero, Hercules", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ser 3, Serô",
        "lang": "Indo-European",
        "refs": "POK:911; IEC:1131",
        "gloss": "to line up, arrange, sort"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:1131; MON:5081",
          "words": [
            {"translit": "sarat", "gloss": "thread", "script": null},
            {"translit": "hâra", "gloss": "string of beads", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:1131; MON:5081",
          "words": [
            {"translit": "hâr", "gloss": "string of beads, necklace, neck", "script": "هار"}
          ],
          "note": null,
          "quote": {
            "text": "گزیده سواران برون از شمار - بران باد پایان آهخته هار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "IEC:1131",
          "words": [
            {"translit": "hara", "gloss": "mountain range", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1538",
          "words": [
            {"translit": "serere", "gloss": "to arrange, join", "script": null},
            {"translit": "sors", "gloss": "lot, fortune", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "series, assert, insert", "gloss": null, "script": null},
            {"translit": "sort, sorcerer, assort, consort", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "French",
          "refs": "VOP:212",
          "words": [
            {"translit": "seri, seriyal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "VOP:212",
          "words": [
            {"translit": "serî", "gloss": "series", "script": "سری ( سریال )"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Serô",
        "redirect": "Ser 3"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:56:05.936Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:05.987Z] TOOL RESULT

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


## [2026-09-14T01:56:28.059Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','IEC','MON','VOP','BQT','HRN','HUB','BRT','SYN','WLD','LAT','LEW','SKT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700])\n    print('---')\n\""
}
```


## [2026-09-14T01:56:28.833Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ===; sed -n 1,80p /home/sfmqrb/git/rishe/data/verification/page-385.json"
}
```


### [2026-09-14T01:56:29.294Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
---
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
---
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
---
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
---
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
---
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
---
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
---
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
---
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
---
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
---
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
---
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
---
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
---
```


### [2026-09-14T01:56:29.364Z] TOOL RESULT

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
(eval):1: == not found
```


## [2026-09-14T01:56:33.019Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==567 || NR==568 {print \"=== leaf idx \"NR-1\" ===\"; print}' POK_02.txt | head -150"
}
```


## [2026-09-14T01:56:34.019Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ser-2\\|ser-4\\|3\\. ser-\\|4\\. ser-\" POK_full.txt | head -30"
}
```


### [2026-09-14T01:56:34.116Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-14T01:56:34.180Z] TOOL RESULT

```
73996:Root / lemma: ser-2 
74054:Root / lemma: ser-4 
82004:because of cymr. serch ds. rather as *sterka\r\ere, as to ser-2 or ser-^ belong; to Slavic
```


## [2026-09-14T01:56:36.917Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '73980,74120p' POK_full.txt"
}
```


### [2026-09-14T01:56:36.980Z] TOOL RESULT

```
also appellative (Mantua sa/7ic>7" stream, brook' etc.); cymr. FIN Sdr{*Sora)\ sor- a\so in den 
FIN Old Prussian Sar-ape, Lithuanian-poln. Szar-upa, Latvian Sarija; 



Middle Irish sirid {* serTtI) "durchwandert, sucht heim, loots, verlangt', verbal noun siriud, 
cymr. herw {*ser-uo-) 'Landstreicherei', Middle Irish serb^ theft '; 

Lithuanian a/7S//Y/"unnzingeln', Latvian sirt^ umherschwarmen, Raubziige make ', sira 
(compare Old Indie sira) "Umherstreifer, beggar'. 

References: WP. II 497 f., WH. II 525, Schwyzer Gr. Gr. 1, 727^; in addition sreu-'i\o\N\ 
after E. Fraenkel Gl. 32, 33 here gr. psGsa 'nostril, nose', p60O(; "Wogenschwall', as well 
as pi(;, pTv6(; "nose' as "die Triefende'. 
Page(s): 909-910 

Root / lemma: ser-2 

Meaning: to guard, watch over, support 

Material: Avestan hara/t/"\r\as acht, schijtzt'; haurva/t/ds., /75^n/5-"beschutzend, hijtend' in 

pasus-haurvo spa ' 6\e Schafe beschijtzender Hund, Schaferhund' (as Latin sen/d from an 

^/-extension); haratar-^ Hijter, Wachter', /75/'az?/'a- "nourishment, care, cultivation, 

Wartung'; hara- "achthabend, hiJtend', redupl. h/sara- ds.; 

gr. "Hpa "* Schutzerin ' from * "HpFa, npux;, -u)0(; (stem npojF-, see above) "* HiJter ' 

I 
(ripu)£(; " Landesschutzgeister '), "bulging, mighty man'; servo, -are^{den Wachter machen) 

erretten, receive, Linversehrt bewahren ', Oscan 5e/'eK/r/b'"auspicio, iussu'; Umbrian seritu 

"servato', anser/ato Sup\n. "observatum' compare oose/r/0/77 perhaps "*observaculum' 

from *ser-tlomr, 

unclear are Old Church Slavic chranjg, chran/t/look after, watch over, keep, preserve, 
protect', chrana'd\s\r\, food, nourishment, food' etc. (see Berneker397 f.); compare 
MachekSlavia 16, 191 f.; 

as guttural extension here Lithuanian serg-mi, -u, -iu^ behijte, guard ', sargas^ ^|yjj|| 
', ss/y^s "watchful, wakeful'. Old Prussian but-sargs^ Haushalter ', absergTsnan f\Vk. " 
protection'. 

References: WP. II 498 f., WH. II 525 f., Trautmann 257 f. 
Page(s):910 

Root / lemma: ser-3, sor- 
Meaning: red 

Material: Old Indie perhaps in sara- m. n. " marrow of a tree (compare Latin robur^ 
heartwood '), Festigkeit, power '; with formants -to- Lithuanian 5a?^55 "fuchsig (from 



horses'), Latvian sarts'red in face'; witli formants-bho- Latin sorbum'6\e rote berry of 
Sperber-, Vogelbeerbaumes', sorbus^Ms tree'; Swedish sarf^ roach, cockroach '; russ. 
sorobalina^ rosehip, dog rose, blackberry ', Lithuanian serbenta, serbentas^ black currant 
' (ass. from * sarbental); with formants -g(h)o-x\}ss. soroga^ roach, cockroach, Plotze'; 

with -k- Latvian saA/rs "reddish'; 

with -/77- Lithuanian sarmoties^ be ashamed'; 

with -p- Lithuanian serpes PI. 'ein gelbes Farberkraut, Serratula tinctoria', sirpstu, 
sirpau, sFrptT mature, ripe, mellow, seasoned become' (only from Beeren and 
SteinfriJchten, also actually "yellow or reddish become'). 

References: WP. II 499, WH. II 562, Specht Indo Germanic Dekl. 267. 
Page(s): 910-911 

Root / lemma: ser-4 

Meaning: to put together, bind together 

Material: Old Indie sarat-, sarit- ' filament ' (uncovered), perhaps sa/a "lichen, mane, 

bristle'; 

gr. dpci) {*serid) "reihe aneinander' (hom. only participle Perf. ££p|j£vo(;, 3. Sg. Plusqpf. 
sepTo), £V£ipu) "knijpfe an, reihe an' (: Latin in-sero^iuqe ein'), EvspoK; "das Hineinfijgen, 
Hineinstecken' (: Latin insertid; //-stem also in praesertim^\v\ previous Reihe, 
vorzugsweise'), sppa n. "Ohrgehange', oppoc; m. " necklace ', oppia f. "fishing line', 
oppaGoq m. "row, chain ', presumably also sipspov "in Gefangenschaft'; 

Latin sero, -ere, -/i//77 "fugen, put in a line, tie, bind, knot ', ser/ies "order, chain, row', 
se/77/a "Seile', soas "lot, fate' (probably of Aufreihen the Lose); sera^ as bar, bolt vorgelegter 
crossbar, crossbeam' (?); Oscan asem/77"asserere'; Old Irish serna/d^reM an, ordnet an', 
subjunctive seraid, verbal noun sreth{*srta) "Ausbreiten, row' etc. kann also *s/e/'-and 
*5pe/'- contain; Gothic sarwau. PI. "armament, armor, weapons ' (probably "geknoteter, 
geknijpfter Harnisch', compare Latin sertae loricae). Old Icelandic S0rviv\. "kostbares, 
collar, neckband'. Old High German Old Saxon saro "armament, armor'. Old English seam 
"armament, armor'; also "skillfulness, artifice', as s/e/'M/5/7"insidiari, planen'; 

Old Lithuanian seris^ filament, Pechdraht'; Hittite sa/ra- "break, rupture, divide' (?). 

Ein with unserem ser- ursprungsgleiches ser- for "geschlechtlichen Verkehr; wife, 
woman' seeks man in Old Icelandic serda siem V. " lubricity drive, push', sordenn av\6 



strodenn 'vnuWebna passus' (Old English seordan\s nord. loanword), Old High German 
se/Ya/7 "geschlechtlichen Umgang have', cymr. se/Y^'obscenus', serthedd ^obscena 
locutio'; if Irish se/r'love', bret. se/r77'Kebsweib' anzureihen is, is a West Indo Germanic 
ser- 'geschlechtlich verkehren' anzuerkennen; about unsicheres Indo Germanic *sor- 
"wife, woman' s. M. Mayrhofer by Brandenstein, Studien 32 ff. 

References: WP. II 499 f., WH. II 52 f., Pedersen Hittite 118. 
Page(s): 91 1 

Root / lemma: ser-5, extended serp- 

Meaning: sickle 

Material: Old Indie srnTi. "sickle', 5/77/5- 'sichelformig', srn/'-m. 'hookzum Antreiben of 

Elefanten'; Latin sand, -/re'6\e Saat behacken, weed ' {*Serid), sarcu/um ' Jatbacke' {*sar- 

tlom). 

Maybe alb. harr'to weed' similar to Latin sarr/o (sario) -ire -ui and -ivi\o hoe, weed'. 

[common alb. s >/? shift]; alb. seems to have preserved the old laryngeal. 

With yo-extension: 

Gr. apnri "sickle' and "a bird of prey', apTra^w "raffe, raube, despoil ', apiTayn f. 
"Plijnderung', apnayn f. ' rake ', apna^, -aYO(; 'rauberisch, greedy '; 

Latin 55/50/0 and sarpo, -ere, -si, -/^/77"beschneiteln, abschneitein', sarmen {*sarp-men), 
55/777^/7/^/77 "abgeschneiteltes rod, deadwood'; Old High German sarf. Middle High 
German 55/50/7 'sharp, rough, from herbem, zusammenziehendem Geschmacke, cruel, 
savage, wild'; Old Church Slavic srhpt, russ. 5e/X7b "sickle', Latvian 5//x?/5 "sickle'. 

References: WP. II 500 ff., WH. II 470 f., Trautmann 261 f.; J. Gonda Mnemosyne 6, 153 

ff.
```


## [2026-09-14T01:56:55.106Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','IEC','AHD','MON']:\n    print(k, d[k].get('page_offset'), '|HINT|', d[k].get('lookup_hint'))\n    print('local:', d[k].get('local_file'))\n    print('---')\n\""
}
```


### [2026-09-14T01:56:56.173Z] TOOL RESULT

```
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |HINT| Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
---
IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |HINT| Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
---
AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |HINT| Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
---
MON None |HINT| Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
---
```


## [2026-09-14T01:57:00.115Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"^hero,\" \"^Hera,\" \"^conserve,\" \"^serve,\" \"^observe,\" \"^series,\" \"^sort,\" \"^sorcerer,\" \"^assert,\" \"^insert,\"; do echo \"### $w\"; grep -n \"$w\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-14T01:57:01.255Z] TOOL RESULT

```
### ^hero,
17655:hero,  n.  —  MF.  heroe,  fr.  heroe  (F.  heros),  fr.  L. heroem,  acc.  of  herds,  ‘hero’,  fr.  Gk.  fjptoi ;  (for *-?]pojF-o^),  orig.  ‘defender,  protector’,  rel.  to "Hpa  (for  *"Hpfa),  ‘Hera’  (lit.  ‘tutelary  god¬ dess’),  and  cogn.  with  L.  servare,  ‘to  save,  deliver, preserve,  protect’.  See  conserve  and  cp.  Hera. Hero,  n.,  priestess  of  Aphrodite  in  Sestos;  loved by  Leander  of  Abydos  (see  Leander).  —  L. Herd,  fr.  Gk.  ‘Hpci;  of  uncertain  origin, heroic,  adj.  —  F.  heroique,  fr.  L.  herdicus,  fr.  Gk. •f)ptatx6?,  fr.  r|poK,  gen.  i)ptoo?,  ‘hero’.  See  hero and  -ic.  Derivatives:  heroic,  n.,  heroic-al,  adj., heroic-al-ly,  adv.,  heroic-al-ness,  n. heroin,  also  heroine,  n.,  a  poisonous  drug  ob¬ tained  from  morphium.  —  G.  Heroin,  coined by  H.Dreser,  who  prob.  formed  it  fr.  Gk.Tjpto?, ‘hero’,  and  chem.  suff.  -in,  resp.  -ine. heroine,  n.,  a  female  hero.  —  L.  heroina,  fr.  Gk. TjptotvY),  ‘a  heroine’,  fr.  ijpco<;,  ‘a  hero’.  See  hero and  -ine  (representing  Gk.  -fvr]). heroism,  n.  —  F.  herolsme.  See  hero  and  -ism. heron,  n.  —  ME.  heiroun,  heroun,  fr.  OF.  hairon, heron  (F.  heron),  fr.  Frankish  *haigiro,  which is  rel.  to  OHG.  heigir,  heiger,  heigaro,  ‘heron’, and  to  OE.  higera,  higere,  ‘magpie,  woodpecker’, ON.  hegri,  heri,  ‘heron’,  Swed.  hdger,  OHG. hehara,  MHG.  heher,  G.  Hdher,  ‘jay’,  OE.  hra- gra,  Du.  reiger,  OHG.  reigaro,  MHG.  reiger, G.  Reiher,  ‘heron’,  and  cogn.  with  OSlav.  kriku, ‘cry,  scream’,  kriiati,  ‘to  cry,  scream’,  Lith. kryksti,  ‘to  shriek’,  W.  cryg,  ‘hoarse’.  Gk. xpi^eiv,  ‘to  creak,  screech’.  All  these  words  are of  imitative  origin.  Cp.  next  word.  Cp.  also aigrette,  egret.
### ^Hera,
17596:Hera,  n.,  sister  and  wife  of  Zeus,  queen  of  the gods  (Greek  mythol.) ;  identified  by  the  Romans with  Juno.  —  L„  fr.  Gk.  "Hpd,  which  stands  for *"HpFd,  lit.  means  ‘protectress’,  and  is  rel.  to 7jpco9,  ‘hero’,  orig.  ‘defender,  protector’.  See  hero. Heracles,  Herakles,  n.  —  See  Hercules. Heracleum,  n.,  a  genus  of  plants,  the  cow  pars¬ nip  (bot.)  —  ModL.,  fr.  Gk.  T)pocxXela,  name of  a  plant,  prop.  fem.  of  the  adj.  ‘HpdxX.c1.09, ‘pertaining  to  Hercules’,  fr.  ‘HpaxXifc  (see  Her¬ cules).  Accordingly  Gk.  TjpaxXetd  lit.  means ‘the  flower  dedicated  to  Hercules’.
### ^conserve,
### ^serve,
### ^observe,
25930:observe,  tr.  and  intr.  v.  —  ME.  observen,  fr.  OF. (=  F.)  observer,  fr.  L.  observare,  ‘to  watch,  re¬ gard’,  fr.  ob-  and  servare,  ‘to  save,  deliver,  pre¬ serve,  protect’.  See  conserve.
### ^series,
34689:series,  n.  —  L.  series,  ‘a  row,  succession,  se¬ quence,  series’,  rel.  to  ser  ere,  ‘to  put  in  a  row,  join together,  connect,  combine’,  sermo,  ‘talk,  dis¬ course,  speech’,  and  in  gradational  relationship to  sors,  ‘lot’ ;  cogn.  with  OI.  sarat-,  ‘thread’,  Gk. etpeiv,  ‘to  fasten  together  in  rows,  to  insert’, epp.a,  ‘band,  noose,  earring’,  oppiop,  ‘necklace’, op[ta&6?,  ‘row,  chain’,  Goth,  sarwa  (pi.),  ‘ar¬ mor,  arms’,  OE.  searo  (gen.  searwes),  OHG. saro  (gen.  sarawes),  of  s.m.,  ON.  sorve,  ‘neck¬ lace  of  stringed  pearls’,  OIr.  sernaid,  ‘he  joins together’,  sreth,  W.  ystret,  ‘row’.  Cp.  assert, assort,  consort,  desert,  ‘to  leave’,  dcseTt,  ‘waste’, dissert,  exert,  exsert,  insert,  resort,  sear,  ‘the catch  in  the  lock  of  a  gun’,  sermon,  Sertularia, sorcerer,  sort,  the  first  element  in  sortilege  and the  second  element  in  Laertes, serif,  n.  —  See  ceriph.
### ^sort,
35985:sort,  tr.  and  intr.  v.  —  ME.  sorten,  fr.  sort.  See sort,  n.
### ^sorcerer,
35959:sorcerer,  n.  —  MF.  (=  F.)  sorcier,  fr.  OF.,  fr. VL.  *sortidrius,  ‘a  caster  of  lots’,  fr.  *sortiari,  ‘to cast  lots’,  corresponding  to  L.  sortiri,  fr.  sors, gen.  sortis,  ‘lot’.  See  sort,  n.  For  the  repetition of  the  suff.  -er  see  poulterer  and  cp.  words  there referred  to.
### ^assert,
3687:assert,  tr.  v.  —  L.  assertus,  pp.  of  asserere,  ‘to claim,  maintain,  affirm’,  lit.  ‘to  join  to  oneself’, fr.  ad-  and  serere,  ‘to  join  together,  connect, combine’.  See  series  and  cp.  dissert,  insert. Derivatives:  assert-er,  n.,  assertion  (q.v.),  assert¬ ive,  adj.,  assert-ive-ly,  adv.,  assert-ive-ness,  n.
### ^insert,
19519:insert,  tr.  v.  —  L.  insertus,  pp.  of  inserere,  ‘to  put in,  bring  in,  graft,  introduce,  insert’,  fr.  in-, ‘in’,  and  serere,  ‘to  put  in  a  row,  join  together, connect,  combine’.  See  series  and  cp.  words there  referred  to.
```


## [2026-09-14T01:57:07.366Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"conserve\" KLN_1966.txt | head -5; echo \"=== Hercules\"; grep -n \"^Hercules,\" KLN_1966.txt | head -2"
}
```


### [2026-09-14T01:57:07.490Z] TOOL RESULT

```
8332:Derivatives:  comet-ic,  adj.,  comet-ary,  adj. cometoid,  adj.,  resembling  a  comet.  —  Com¬ pounded  of  comet  and  Gk.  -oei8r;<:,  ‘like’,  fr. elSoc,  ‘form,  shape'.  See  -oid. comfit,  n.,  a  dry  sweetmeat.  —  F.  confit,  prop, pp.  of  confire,  ‘to  conserve,  candy,  pickle’,  fr. L.  conficere,  ‘to  put  together’,  fr.  con-  and  fa- cere,  ‘to  make,  do’.  See  confect  and  cp.  dis¬ comfit.  For  the  change  of  Latin  a  (in  fdeere )  to i  (in  con-ficere)  see  abigeat  and  cp.  words  there referred  to.
8677:confiteor,  n  ,  a  form  of  confession  ( eccles .)  —  L., ‘I  confess’,  1st  person  sing,  of  confiteri  (see  con¬ fess)  ;  so  called  from  the  first  word  of  the  formula, confiture,  n.,  a  confection;  sweetmeat.  —  F.,  fr. confit,  pp.  of  confire,  ‘toconserve, candy, pickle’. See  comfit  and  -ure.
8823:Derivatives:  consequential-ity,  n.,  consequential¬ ly,  adv.,  consequential-ness,  n. conservable,  adj.  —  L.  conservdbilis,  ‘that  which can  be  conserved’,  fr.  ednservare.  See  conserve,  v., and  -able.
8825:conservation,  n.  —  ME.,  fr.  L.  cdnservdtio,  gen. -onis,  ‘a  keeping,  preserving,  conserving’,  fr. cdnservdtus,  pp.  of  ednservare.  See  conserve,  v., and  -ation.
8828:conservative,  adj.  —  ME.,  fr.  MF.  conservatij (fem.  conservative),  fr.  L.  cdnservdtus,  pp.  of ednservare.  See  conserve,  v.,  and  -ative. Derivative:  conservative,  n. conservatoire,  n.,  a  school  of  music.  —  F.,  fr.  It.
=== Hercules
17620:Hercules,  n.,  a  hero,  son  of  Zeus  and  Alcmene (Greek  mythol.)  —  L.  Hercules,  fr.  earlier  Her¬ ds  s,  fr.  Gk.  'HpaxXCTj<;,  'HpaxXrjq,  lit.  ‘glory  of Hera’,  fr.  "Hpa,  ‘Hera’,  and  x/io;,  ‘glory’.  See Hera  and  loud  and  cp.  Clio,  cledonism,  the  first element  in  Clianthus  and  the  second  element  in Damocles,  Eteocles,  Euclea.
```


## [2026-09-14T01:57:10.020Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8830,8845p' KLN_1966.txt"
}
```


### [2026-09-14T01:57:10.087Z] TOOL RESULT

```
consternate
338
339
conservatorio,  orig.  ‘orphanage’,  fr.  ML.  con- servatorium,  ‘a  place  for  preserving’,  fr.  L.  con- servdre,  ‘to  preserve’  (the  first  Italian  musical schools  were  orphanages).  See  conserve,  v.,  and cp.  conservatory.
conservator,  n.  —  ME.  conservatour ,  fr.  MF. (=  F.)  conservateur ,  fr.  L.  cdnservatorem ,  acc.  of conservator,  ‘a  keeper,  preserver’,  fr.  conservare. See  conserve,  v.,  and  agential  suff.  -or. conservatory,  n.,  a  school  of  music.  —  ML.  conser- vatorium.  See  conservatoire  and  subst.  suff.  -ory. conserve,  tr.  v.  —  F.  conserver,  fr.  L.  conservare, ‘to  save,  keep,  protect’,  fr.  con-  and  servare,  ‘to save,  deliver,  preserve,  protect’,  which  is  prob. cogn.  with  Avestic  haraiti,  haurvaiti,  ‘takes  care of,  protects’,  haurva,  ‘protecting’.  Gk.  ^pco?  (for *7)pcoF-oi;),  ‘hero’,  lit.  ‘defender,  protector’, "Hpa (for  *''Hpfa),‘Hera’,  lit.  ‘defendress, protectress', and  perh.  also  with  5pp.Zvo<;,  ‘the  sage  plant’,  lit. ‘the  saving  plant’  (for  sense  development  cp. L.  salvia,  ‘the  sage  plant’,  fr.  salvare,  ‘to  save’; see  Salvia  and  sage,  the  plant).  See  hero  and  cp. observe,  preserve,  reserve.  L.  servus,  ‘slave’,  ser¬ vice,  ‘to  serve’,  are  not  rel.  to  servare. Derivatives:  conserve,  n.  (q.v.),  conserv-er ,  n. conserve,  n.  —  F.,  ‘preserved  fruit’,  fr.  conserver, ‘to  preserve,  keep,  maintain’,  fr.  L.  conservare. See  conserve,  v.
consider,  tr.  v.  —  ME.  consideren ,  fr.  MF.(=  F.) considerer,  fr.  L.  considerare,  ‘to  look  at  closely, observe,  contemplate,  meditate’,  orig.  ‘to  ob¬ serve  the  stars’,  fr.  con-  and  sidus,  gen.  sideris, ‘star’.  See  sidereal  and  cp.  desiderate,  desire. Derivatives:  consider-ed,  adj.,  considcr-er,  n., consider-ing ,  prep.,  consider-ing-ly,  adv. considerable,  adj.  —  ML.  consider  abilis  (whence also  F.  considerable),  fr.  L.  considerare.  See prec.  word  and  -able.  Derivatives :  considerable¬ ness,  n.,  considerabi-y,  adv. considerate,  adj.  —  L.  consideratus,  pp.  of  con- side  rare.  See  consider  and  adj.  suff.  -ate.  Deriv¬ atives:  considerate-ly,  adv.,  considerate-ness,  n. consideration,  n.  —  F.  consideration,  fr.  L.  con- siderationem,  acc.  of  ednsiderdtio,  ‘considera¬ tion,  contemplation,  reflection’,  fr.  consideratus, pp.  of  considerare.  See  consider  and  -ation. consign,  tr.  v.  —  F.  consigner,  fr.  L.  ednsignare, ‘to  mark  with  a  seal,  to  subscribe,  attest,  cer¬ tify’,  fr.  con-  and  signare,  ‘to  set  a  mark  upon, mark',  fr.  signum,  ‘a  mark’.  See  sign. Derivatives:  consign-able,  adj.,  consignation (q.v.),  consign-ee,  n.,  consign-er,  n.,  consign¬ ment,  n.,  consign-or,  n.
consignation,  n.  —  L.  ednsigndtio,  gen.  -onis,  ‘a written  proof,  document’,  fr.  ednsigndtus,  pp. of  consignare.  See  prec.  word  and  -ion. consilience,  n.,  concurrence,  coincidence.  —  Lit. ‘a  jumping  together’;  formed  from  next  word with  suff.  -ce.
consilient,  adj.,  concurring,  coincident.  —  Formed on  analogy  of  resilient  (q.v.)  fr.  con-  and  saltre, ‘to  leap’.
consist,  intr.  v.  —  L.  consistere,  ‘to  stand  still, stop,  halt,  endure,  subsist’,  fr.  con-  and  sistere, ‘to  cause  to  stand,  put,  place;  to  stand  still, stand’,  from  the  reduplicated  base  of  stare,  ‘to stand’.  See  assist  and  cp.  words  there  referred  to. consistence,  consistency,  n.  —  ML.  consistentia (whence  also  F.  consistance),  fr.  L.  consistens, gen.  -entis.  See  next  word  and  -ce,  resp.  -cy. consistent,  adj.  —  L.  consistens,  gen.  -entis,  pres, part,  of  consistere.  See  consist  and  -ent. Derivative:  consist ent-ly,  adv. consistory,  n.,  t)  a  council  chamber;  2)  the  papal senate.  —  ONF.  consistorie,  fr.  Late  L.  con- sistorium,  ‘place  of  assembly;  place  where  the emperor’s  council  met’  (whence  also  OF.,  F. consistoire ),  fr.  L.  consistere.  See  consist  and subst.  suff.  -ory.  Derivative:  consistori-al,  adj. consociate,  tr.  and  intr.  v.,  to  associate  together. —  L.  consociatus,  pp.  of  consociare,  ‘to  associate with’,  fr.  con-  and  sociare,  ‘to  join  together,  as¬ sociate’,  fr.  socius,  ‘companion’.  See  social  and verbal  suff.  -ate  and  cp.  associate,  dissociate, consociate,  n.  —  L.  consociatus,  pp.  of  consociare. See  consociate,  v.
consociation,  n.  —  L.  consocidtid,  gen.  -onis,  fr. consociatus,  pp.  of  consociare.  See  consociate, v.,  and  -ion.
consolation,  n.  —  F.,  fr.  L.  cdnsdldtidnem,  acc.  of cdnsdldtio,  fr.  cdnsdlatus,  pp.  of  consolari.  See console,  v.,  and  -ation.
consolatory,  adj.  —  L.  cdnsdlatdrius,  ‘pertaining to  consolation’,  fr.  cdnsdlatus,  pp.  of  consolari. See  console  and  adj.  suffixes  -ate  and  -ory. Derivatives:  consolatori-ly,  adv.,  consoiatori- ness,  n.
console,  tr.  v.,  to  comfort.  —  F.  consoler,  fr.  L. consolari,  ‘to  console,  comfort,  encourage’,  fr. con-  and  soldri,  ‘to  comfort'.  See  solace  and  cp. disconsolate.
Derivatives:  consol-able,  adj.,  consolatory  (q.v.), consol-er,  n.
console,  n.,  1)  a  bracket  supporting  a  shell,  cor¬ nice,  etc.;  2)  a  console  table;  3)  cabinet  of  an organ,  radio  or  phonograph.  —  F.,  ‘console, console  table’,  prob.  a  blend  of  consoler,  ‘to comfort’,  and  consolider,  ‘to  strengthen,  make firm,  consolidate’.  See  console,  v.,  and  conso¬ lidate.
consolidant,  adj.,  tending  to  heal;  n.,  a  consoli¬ dating  agent  ( med .)  —  L.  cdnsoliddns,  gen.  -an¬ tis,  pres.  part,  of  consolidare.  See  next  word and  -ant.
```


## [2026-09-14T01:57:15.743Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=17580 && NR<=17660 && /^[0-9]{3}$|^7[0-9][0-9]/ {print NR\": \"$0}' KLN_1966.txt; echo \"---context\"; sed -n '17648,17656p' KLN_1966.txt | cut -c1-200"
}
```


### [2026-09-14T01:57:16.986Z] TOOL RESULT

```
17614: 722
17615: 723
17653: 724
17660: 725
---context
Derivative :  hermetic-al-ly,  adv.
Hermia,  fern.  PN.  — -  Fern,  name  formed  fr.  L. Hermes,  fr.  Gk.  'Epprji;.  See  Hermes  and  cp. next  word.
Hermione,  fern.  PN.  —  Gk.  'EppuAvz],  fr.  ‘Epprj-;, ‘Hermes’.  See  Hermes.
hermit,  n.  —  ME.  ermit,  hermit,  fr.  OF.  ermite, hermite  (F.  ermite),  fr.  Eccles.  L.  eremita,  fr.  Gk. tp-r:{itx-rfi,  ‘hermit’,  lit.  ‘he  who  lives  in  the desert’,  fr.  
herniotomy,  n.,  operation  of  cutting  for  strangu¬ lated  hernia  (med.)  —  A  hybrid  coined  fr.  hemio- and  -Toufa,  ‘a  cutting  of’,  fr,  xopfj,  ‘a  cutting’.
724
See  -tomy.
hero,  n.  —  MF.  heroe,  fr.  heroe  (F.  heros),  fr.  L. heroem,  acc.  of  herds,  ‘hero’,  fr.  Gk.  fjptoi ;  (for *-?]pojF-o^),  orig.  ‘defender,  protector’,  rel.  to "Hpa  (for  
heronsew,  n.,  heron.  —  ME.  heronsewe,  fr.  OF. heroncel,  heronceau,  ‘a  young  heron’,  dimin. of  heron.  See  prec.  word, herpes,  n.,  an  inflammatory  disease  of  the  skin {med.)
```


## [2026-09-14T01:57:23.804Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ser-\\|^ser\\b\\|^serə\\|^ser\\.\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T01:57:23.865Z] TOOL RESULT

```
924:ser-1, To protect. 1. Extended form *serw- in Latin serudre, to keep, preserve: CONSERVE, OBSERVE, PRE- SERVE, RESERVE, (RESERVOIR). 2. Suffixed length- ened-grade form *sér-6s- perhaps in Greek hérés, “protector,” hero: HERO. [Pok. 2. ser- 910.]
925:ser-?, To flow. 1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM. 2. Basic form *ser- in Sanskrit sarati, sasarti, it flows, it runs: SAMSARA. 3. Extended roots *sr-edh-, *sr-et-, to whirl, bubble, in Germanic *stred- in Old High German stredan, to whirl, swirl, whence ablaut formation in Middle High German séru- del, whirlpool: STRUDEL. [Pok. 1. ser- 909; sr-edh- 1001.]
926:ser-3, To line up. 1. Latin serere, to arrange, attach, join (in speech), discuss: SERIES, SERTULARIAN; ASSERT, DESERT’, DISSERTATE, EXERT, INSERT. 2. Suffixed form *ser-mon- in Latin sermé (stem sermé6n-), speech, dis- course: SERMON. 3. Suffixed form *ser-d- perhaps in Latin sera, a lock, bolt, bar (? < “that which aligns”): SEAR?, (SERRIED). 4. Suffixed zero-grade form *sr-t- in Latin sors (stem sort-), lot, fortune (probably from the lining up of lots before drawing): SORCERER, SORT; ASSORT, CONSORT, SORTILEGE. [Pok. 4. ser- 911.]
```


## [2026-09-14T01:57:29.383Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sarat\" IEC.txt | head -10; echo \"=== hāra/hara\"; grep -n \"string of beads\" IEC.txt | head -10"
}
```


### [2026-09-14T01:57:29.635Z] TOOL RESULT

```
15240:sero, io (1) “join, range, arrange). Cf. srtis. WP II, 499 Skt. cf. sarat, m. ('thread?, fr. *sernt-); Av. cf. hara, f. ‘mountain range’; Per. har, s. (row, rank; string of beads’; Tokh. A. sar- ‘vein’; Hitt. cf. sariya(mi), v. (queried: “weave'); Gk. eíro, v. join’; Lat. sero, Ere, sup. sertum, v. ‘arrange’; series, f. ‘series’. Cf. further (*-e- or *-o-) Skt. saráh, m. ‘string’; saralah, adj. ‘straight, right’; Lat. cf. (?) sera, f. “lock? be- side servia, f. ‘garland’ (?), but cf. sero (2)
=== hāra/hara
15240:sero, io (1) “join, range, arrange). Cf. srtis. WP II, 499 Skt. cf. sarat, m. ('thread?, fr. *sernt-); Av. cf. hara, f. ‘mountain range’; Per. har, s. (row, rank; string of beads’; Tokh. A. sar- ‘vein’; Hitt. cf. sariya(mi), v. (queried: “weave'); Gk. eíro, v. join’; Lat. sero, Ere, sup. sertum, v. ‘arrange’; series, f. ‘series’. Cf. further (*-e- or *-o-) Skt. saráh, m. ‘string’; saralah, adj. ‘straight, right’; Lat. cf. (?) sera, f. “lock? be- side servia, f. ‘garland’ (?), but cf. sero (2)
15255:sert- “braid, twist; line, series, row'. Cf. seró, srt-. (Variant: sret-) Skt. sata, f. ‘braid of hair’; Gk. ertós, adj. ‘threaded’; érsis, f. “band, binding"; Lat. ser- tus, adj. ‘entwined, woven’; serta, f. ‘chaplet, rope’; sertum, n. ‘garland’; (z-gde in) sors, gs: sortis, f. (lot, destiny’. Cf. Gk. klóthó “spin, weave’ in relation to the goddess Klothó *Fate'); Oss. xal, Dig. xalá, s. (thread, cord, string of beads; fate, destiny’, pl. xàldtà: Skt. sata); Olr. cf. sreth, f. ("line, row, series’, fr. *sret- or *srt-); OE seoróan, sv. “lie with, con- sort with’; ON seróa, v. id.
```


## [2026-09-14T01:57:42.005Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport io\ndef leaf_of_line(path, lineno):\n    ff=0\n    with open(path, errors='replace') as f:\n        for i,l in enumerate(f,1):\n            if i==lineno: break\n            ff+=l.count('\\f')\n    return ff\nprint('IEC 15240 leaf', leaf_of_line('IEC.txt',15240))\nprint('IEC 15255 leaf', leaf_of_line('IEC.txt',15255))\nEOF"
}
```


### [2026-09-14T01:57:43.193Z] TOOL RESULT

```
IEC 15240 leaf 625
IEC 15255 leaf 626
```


## [2026-09-14T01:57:49.484Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==581 {print}' IEC.txt | head -20; echo \"=== leaf 626 head\"; awk 'BEGIN{RS=\"\\f\"} NR==626 {print}' IEC.txt | head -6"
}
```


### [2026-09-14T01:57:50.668Z] TOOL RESULT

```
 fr. *quornio-); Av. kaurvo, kaour- vð, adj. ‘black’; Per. kür ‘blind’; Gk. porós, adj. id.; Pol. kary “black — of a horse’; Ukr. karyj “black? (from Turkish kara, according to A Brückner:SEJP)
quorpos, à “turn, link, join'. Cf. querp-, qurp-. (Skt. Av. & Li. Latv. ambig.) Skt. kalpah ‘manner’; Av. cf. kahrpuno Cl zard', LW in Arm. Karb, Let 'basilisk"); Go. hwarbon, denom. or freq. “walk? beside (e- gde) hwaírban, id., ga-hwaírbs (obedient, lit. *flexible)); OS hwarbon, as Go.; MHG warp, gs: Warbes, sm. ‘turn’; warbe, wf. ‘circle; as- sembly'; OE hwearf, m. “turn, crowd, move- ment, distance, change, error, embankment’; E wharf; EMSwedish hvarf, Sw. varv, n. ‘time, order, series, camp, layer; ON cf. hvarfla, v. ‘roam; waver’; Li. cf. pa-karpa, f. *nape: of neck’: Latv. karpis and karpe, mf. (/boathook'. Ambig.)
quorquol- (quorquol-) (1) ‘twist, turn, curl, coil, wicker, weave’. Cf. qur-quol and the e-/o- gde simplex quel-/quol- Alb. (z-gde) kurkulloj, v. ‘nestle, curl up, lurk’; Lat. curculio, gs: -onis, m. (1) *corn-weevil'; ME wharwyl, wharwhil ‘whorl, swivel, pulley’; Li. kafklas, m. ‘sallow, willow’; karkles, pl. ‘wicker’; Latv. karkls, m. ‘scrub willow’. Vari-
1047
ants of uncertain cons. (*quorp- or *quoru-) in MHG warbel, adj. ‘mobile’, cf. Skt. kár- varah ‘variegated’; OFris. hwarvel, Du. wervel, m. ‘vertebra; swivel; pegtop; OHG hwirvil (sic), id.; G. dialect Warbel, m. *whorl'. (Iso- phone: Br. porbolen, f. ‘pimple, pustule, bud")
quorquol- (quorquol-) (2) *windpipe; hoarse- ness in the throat. Lat. curculió, gs: -onis, m. ‘windpipe’; Li. kar- kulys, gs: -io, m. *hoarseness'
quorquor- (quorquort-, quorquorbhit-) ‘curly plant or object, creeper’ Skt. karkatih, f. ‘gourd’; (variant: Carbhita, -am, fn. id. fr. *querbh-); Lat. cf. cucurbita *cucumber'; OE *hwerhwefte (*written -fette & -hwette, both once), id.
quorsio ‘drag, pull, til. See next. Cf. WP I, 429. i Skt. kársami, v. ‘draw, drag; plough; lead’; Av. karos-, v. as Skt.; Per. kašam, v. ‘draw; suffer beside kašam, inf: kāštan, kistan, v. ‘plough’; Arm. kašem, v. “pull, pluck’; Alb. cf. të-kurr, v. tr. contract’, fr. *ati-°); Extn. in Av. karstis, f. ‘ploughing’; (z-gde in) Skt. krstah ‘drawn, plowed’; Per. kišt (2) ‘plowing, sown field”
quorstis, iə ‘brushwood, brake’. Cf. qurst-. Welsh variant querkt- Alb. karthje, f. id.; cf. W perth, pl. -i, f. id. beside prys (z-gde), id.; R xvórost, f. id.; OCz. chvrast-, id. (Cosmas); mod. chrast, f. id.
quortos, is (1) (turn; time, occasion’. Cf. qurt- Skt. katah, m. ‘time; season’; Myc. cf. api-qo (r)to- (epithet of tables: ‘round’ or “turned”, fr. *ombhi-^?); Osc. cf. (prob. z-gde) petiro- pert, adv. (‘four times’. For er fr. *-r- cf. Osc. Mamers for Lat. Mamors); W porth, pl: pyrth, m. *help'; OCS kratü, gs: kratu, m. “time”; Cz. krát, id.; Pol. kroC, m. id. (i-st).; Li. kartas, m. id.; Latv. cf. vien-kartis “simple pattern of weaving’; vien-karss, adj. (/simple', fr. *-quortios)
quortos (2) ‘made; make, fabrication, shape’. Cf. quer-, quor-, qur- Skt. cf. kartum, inf. ‘to do, make’; Per. cf. kala ‘manufactures’; kalbad, s. “body, shape,
quorquol- (quorquol-) — quoteros, à
15
20
25
30
35
40
45
1048
=== leaf 626 head
nt of type septm, q. v. Olr. cf. secht, Ir. seacht; Go. sibun, OS sibun, OE seofon; MHG siben, seben and suben; Du. zeven; Lux. zivon; OFris. sigun, siugun; Fris. saun; OCS (and Com. Sl.) sedmt Cf. further Oss. avd; Tokh. spat, beside sáptànt
sento, ið — sequó
10
20
25
30
```


## [2026-09-14T01:57:56.292Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==625 {print}' IEC.txt | grep -n \"^1[01][0-9][0-9]$\" ; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==625 {print}' IEC.txt | tail -5"
}
```


### [2026-09-14T01:57:57.440Z] TOOL RESULT

```
6:1129
---
sentó, ið ‘track, trace, sleuth, proceed, fol- low’. WP II, 496. Cf. sentis Alb. gjej, mp: gjíndem, v. (find?^; mp. ‘find myself, be’); Lat. sentio, ire ‘sense, feel, find, deem’; Olr. senn, cpds. ‘drive, chase’; Br. henti, inf. ‘haunt, frequent; MHG sinden, sv. 3 ‘tend, go’; er-sinden, sv. 3. ‘reach, dis- cover’; OE sīðian, wv. ‘go’; ON sinna, v. (1) ‘travel’; cf. also sinni, n. ‘journey’; cf. also Ir. séis, f. (?) science, skill, if fr. *sentio)
senuå, see senouá, and cf. sneuá OHG sénwa ‘sinew’: Lat. sinus, üs (bay, lit. *bend"); sinuus ‘winding’ (formally also Hitt. senahhas, sinahhas *ambush")
sepelió (?) (cf. se-, pel- ). Cf. WP II, 487 Skt. sáparyàmi, v. ‘respect, honour’; saparyà, f. *worship'; OPer. hapariya-, v. id.; Lat. sepe- lið, ire, v. bury’, if not fr. *se- “apart? + *pel-?)
septm (sequdm-) ‘seven’. Cf. seque, du ‘with two extra'?. Cf. sequdm Skt. saptá; Av. hapta; Per. haft; Arm. eawt'n; Tokh. A spät B sukt; Hitt. cf. septamas 'se- venth'; Gk. heptá; Lat. septem; Olr. secht; Li. septyni, Latv. septini. Cf. Alb. shtatë; W saith; Br. seiz and Cor. seyth. The ordinal of type *septomos arises in Skt. saptamah; Hitt. septamas; Lat. septimus; OPr. septmas. Variants in Gk. hébdomos & Li. sekmas; OCS sedmyj
sequdm, sequdomos 'seven; seventh'. Vari- a
```


## [2026-09-14T01:58:06.625Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT_v5 (هـ)\"; grep -n \"هار\" incoming/BQT/BQT_v5_pages.txt | head -20"
}
```


### [2026-09-14T01:58:06.684Z] TOOL RESULT

```
=== BQT_v5 (هـ)
21:چاپ چهارم : ۱۳۶۲
34:دوره جدید برهان فاطم درپنج مجلد منتشر‌میشود ۰ چهار جلد اول‌هبانست
38:چهار جلد اول دوره حاضر - چنانکه در مقدمهٌ جلداول پاد آوری شد -
43:فر‌اهم گن‌دید که گنجا نیدن همه آنها در چهار جلد اول(با چاپ افست)امکان‌نداشت.
47:وچهار جلد اول بصورت‌افست طبع‌گردد » چنانکه بعضی داثرة‌المعارفهاوفرهنگهای
51:مطالب حواشی چهار جلد » بحت دربارهٌ لفات از نظی لغت‌شنامی و ریشه شناسی ۰
59:بعضی از افلاط چایپیکه‌دره‌تن وحواشی چهارمجلد اول روی داده وتصحیی
67:چهارم درج شده بود - در مجلد حاضر (صفحهٌ ۱۴-۱۳) تلخیص شده +
70:جلد چهارم ثبت شده بود - در پایان جلد حاضر جای داده شده‌است ۰
80:طبع اول درج شده بود » درمتن چهار جلد اول دوره‌کنئونی وبخش دیگن درافنای
89:صفحااچهارده, بی ازسطر ۱۳- استر| بون گوید : زبان‌مادها شبیه ذبان
206:سر اورل‌آشتین۸ است و قبلاتاریخآنهارااواسط قرن دوم میلادی میدانستند»
207:امااستاد هنینگه‌بدلایل‌مقنم ] نهارا بآغازقرن چهارم میلادی نسبت داده‌است۹.
233:در صفحةٌ چهل وسه و چهل وچهار مدمه آورده‌ايم ۰
266:صفحه بیست وچهار,پس ازسطر؟ - استاد هنینگ رساله‌ای بعنوان ذیل
380:صفحه سی وچهار» پس ازسطر٩‏ افزوده شود :
439:نویسانآنر| یکی ازچهارزبان متروك پادسی یاد کرده‌اند (رك. کتاب‌حاضر.
455:نویسان آنر| یکی ازهفت زبان فارسی ودرزمیء چهارزبان متروك آورده‌اند
484:صفحة چهلوچهار, س‌از سطرآخر افزوده شود :
561:تعليقهٌ مجلد چهارم‌برهان طبع‌اول نکارنده ششم - هشتم » که در مقّدمهٌ
```


## [2026-09-14T01:58:07.515Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FSF\"; grep -n \"هار\" FSF_pages.txt | head -20; echo \"=== FRS\"; grep -n \"هار\" FRS_pages.txt | head -10"
}
```


### [2026-09-14T01:58:07.594Z] TOOL RESULT

```
=== FSF
10:    ‫(فرهنگ واژه‌های دششاوهار‬
56:                                    ‫چاپ‪ :‬مهارت‬
257: ‫نسخه‌نویسان «گفت» را در بیت ششم ماضی گفتن دانسته‌اند و از چهار نسخهة‬
324:‫برای «نوا» به معنی چهارم از فردوسی است و به خاقانی نسبت داده شده است‪ .‬و يا‬
357:‫بعضی از آن‌هارا کهدر لفت فرس و صحاح الفرس ضبط است نگاه داشتم؛ و مستقیما از‬
381:                                         ‫یعنی جلد چهارم» صفحه ‪ ۷۴‬بیت ‪٩۸.‬‏‬
410:         ‫دو جادوش پر خواب و پر آب روی‬        ‫پهارنه]یز کن‬
567:‫مهرگان برتومبارک باد و ازگشت سپهر‬                        ‫آذرگشسب «دود» بکهار می‌رود]‬
661: ‫آذینبستند» بهار حدارشیه چنین می‌نویسد‪:‬‬                                  ‫(دیوان ‪۵۰۳‬و ‪:)۶۰۳‬‬
1401:‫[لهراسب] به بگلزخین شد بر آن نوبهار‬                     ‫ار‬        ‫ییک ان زمه‬
1574:                                                      ‫(بهار در حاشیة ه‪۳‬مان صفحه چنین‬
1686: ‫چکورباس آهار داده به خون‬                                                        ‫گوید‪:‬‬
1687: ‫(‪)۵-۰۸۲-۲۴۷‬‬                                                    ‫نیاید تو را پوزش اکنون بکهار‬
1689:‫ز خوی هر دو اهار داده شویم‬                                    ‫نشاید که باشی تو اندر زمین‬
1698:‫دفتر به سخن خوب شود جامه به آهار‬                          ‫برانگیخت از جای شبدیز را‬
1701:‫به حون دل اهار دارد‬           ‫ز مکسرش‬              ‫(‪)۴-۸۸۲۰-۵۱۳‬‬
1716:                               ‫‪:)۵۲۱--۱‬‬                                                   ‫آهار‬
1723:          ‫از حافظ (غزل ‪-۹‬بیت ‪:)۷‬‬                  ‫واژه امروز هم بکار می‌رود‪ :‬يخة آهاری»‬
1724:  ‫غمزۀ ساقی بهیغمای خرد آهخته تیغ‬                 ‫پیراهن آهارزده‪ ,‬و به معنای مسجازی‪ :‬نم‬
1952:   ‫زهار به معنی خایه بیرون کشیده» بریده‪:‬‬           ‫(‪-‬پرویز ‪)۳۶۱‬‬
=== FRS
63:              ‫و "دیبگر لغانی است کهآ نهارا‬         ‫لفتی‬
70:‫تألیف اسدی نست بلکه آنهارا دیگران ازروی فرهشکه اسدی باافزودن‬
89: ‫دو نسخه از چهار نسخه‌ای که ما در اختبار داشتیم توافق وحود داشته‬
151: ‫در طبع نسخه حاضر از نسح‌خطی و چاپی لغت فرس چهار نسخه‬
159:            ‫رده ایم ‪ .‬تزات این چهار نسخه سشفعبل ذبل است ‪:‬‬
643: ‫ون نیز بعلت مسافرت چهارسالهٌ نگارنده «جائی ترسید تا بارسوم درسال‬
686: ‫دانش‌سرای عالی تشگر میکنم که در تصحیح اوراق و تیه فهارس كمك‬
809:‫گروهی خوابکه جهارپایان گروایند گوروهی طاق بنارا چ|نانکه‬
816:                  ‫لمل [ظ ‪ :‬محل |شبگاه چهار بایانگ[وس‬
838: ‫بود که چهاربای درش کنند ‪ .‬ه ‪ -‬چ اضافه‌دارد ‪: :‬وآرام‌هم ‏ ‪ ۰‬معنی نابروا فقط در‬
```


## [2026-09-14T01:58:15.260Z] TOOL CALL #22: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:58:15.269Z] TOOL RESULT

```


```


## [2026-09-14T01:58:17.070Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT harā mountain\"; grep -n \"harā-\\|Harā\\|Berg\" BRT.txt | grep -i \"har\" | head -20"
}
```


### [2026-09-14T01:58:17.137Z] TOOL RESULT

```
=== BRT harā mountain
10224:•  j.  garay-  :  gairi-  m.  'Berg,  Gebirgszug, Gebirg"':  -rayi^^^.)  b^nzantB  Ytio.  14; ig.z,  7,  8,  16.  3;  —  'rayd  (als  AP.)"  aSa- ^ä^rä  Y.2.14;  /0.3,  7/.  10;  —  'rayasca (als  AP.)  ySi  hrnaniö  Yty.  9;  —  ma- sits  Urli{AP.)  Yt.j4.4ii  —  bar^dstaiibyö 'triiyS  V.  2.  aa;  —  'irl/c3'^  aßtaHnS  Y. 42.3; —  iarfshus  paiti  'irinam  Y.5.  26, JO.3,  V.2.23i>;  Y.j.14^, /o.  17.  YLÄ24, 14-  21.  iS.  6,  ig.  6,  Vr.  /.  6,  V.5.  I',  2, 10.28;  —  haoma  raose  'ra  (LS.)  paiti Y./0.4;  —  ytzi  ahi  'rS  (LS.)*'  dtr^hm (sd.)  \.2i.  5;  —  paoiryB  °iris  hqm.hiiial .  .  haraiii  bars  . ,  bitys  ztrihazB  HrU  Yt.
11783:•  j.   taera-  m.,   a   'Bergspitze,   Gipfel': 'rasca  barö.srayai0{%A.)\t.ig.6.       a)  sonst von  dem  Gipfel  der  Hara,  Haraitr.  upa 'nm  AarayiYtiS.T,  —  'nmcä  harai%ya hmS  Y.  42. 3;    —    upa    'r>m    Aarai'iya iarttS  yat    ml  aiwitö   vrvistnti   starasca masca  hvania  "auf  dem  Gipfel  desffaraitl- gebirgs,  um  den  meine  Sterne,  Mond  und Sonne  kreisen"  YL/2.  ss'^- Et?')  —  Vgl.  j/<wra-,  S  Sj.  a.   KZ.  29.  487. —  mp.  (Pu.)  tirai,  nbiL  fer  'Be^spitze',    afT. tir^  -spitz'.  —   ')  Vgl.  iSt.  Bd.  J.  4:    /Frai  i hatiurz  Ja  ölt  i  man  ^ariil  u  mäh  u  itäraiän kacpai  afäivartit.  — ')  Falsch  Go».  ABajrAW. so.  I.  189.
17015:•  j.  *bar»Z-  :  b»nz-^'>  i)  Adj.  'hoch,  er- haben': ratüm  Äj/vwm  Vr,  2.  10;  —  ratSuS hmlf{GS.)  Vt.i.%]  —  Hitrlm  . . yahmät haca  binzät^^  haosravanhtm  (sd.)  Vlä 4,  a)  von  Tönen  'hoch,  laut';  yas3  . . bsDBtn  barat  zaota  väHm  Yt.//.  61;  — yat  bsnism  barst  astra  ('die  Peitsche') vaHm  Yt. /o.  113.  2)  'Höhe;  Berg': haraiti  (sd.)  Äar/{NS.))>  Yt.ifj.  i;  —  upa upa.bdi  Aj«ya  (sd.)  i.wvÄ?(GS.)  Ytj?.  3, Jj.  24;  —  talrfincH  harai'hyä  btrpzö  Y. 42. 3;  —  lainm  harai^yä  barisö  (GS.) Ytr2. 15;  —  karai^yS  paiti  bar^zayä (GS.)*>  Y.io.  10,  57. 19,  Vt  10.  50,  90;  — vispkhu  paiti  öanzähu*''  Yt/o.4S.  [FrBy.: lies  °b?nts  als  Komp.]
17019:•  j.  barszah-  n.  'Höhe,  Berg':  *upa *tnaitlm  (sd.)  'zargAam  V.J.  30;  —  mihnm .  .  yS  vlsp)m  aham  .  .  Sdt6aili  haratkyät (sd.)  paiti  'zatakat  Yt  jo.  5 1 ;  —  barniste paiti  'zaÄi  haraihyS  .  .  Y.  ^y.  19;  — AuiaitJm  (sd,)  °zS  Ytj.  96,  12.  24;  —  ya (näml.  arfdvt)  .  .fratacaiti  hukairyät  haca 'zaftkat  Y.  65.  3 ;  Yt  5.  2  5.
17041:•  j.  barsäoav-  m.  'Erbebung,  Höhe, ctdmen';  i)  von  Bergen:  'nus  paiti  gairt- nqm..Jqfnu^a  raonam  V,  2.  33;  Y.  5. 36, 10.  y,  —  °tmha  gatrinam  Y.  JO.  1 7 ;  — am  'navS  (als  AP.)  gatrinam  V,5.  i,  3; Yt.i4''ij '&6;  —  Äaca  'navB  gairinqm V.5. 1;  —  mihr»n..yö..srlrä  °nava{v&aA. haraya)  gfrTuinäiti  Yt /o.  13.  3)  vom Himmel :  fravasayd  ..ya..  /raiOsitUe  'trvS (GS.)"  avaähe  oA?  ". ,  die  herankommen von  dem  Gipfel  her  des  Himmels  dort" Yt7J.  42;  —  kanjamaiumla  yat  as  .. °ttvS  (LS.)  *<tvaAhe  asns  y?matfm  G.  2. 8.  3)  vom  menschlichen  Kopf:  *°m>ö''' v3  paiti  var^Xanahe  N.öj;  —  °nüm  hl varfaarwm(;iA.)  pourvm  Y.S.^o;  41J  —  avi hz  'nümla  yaosdähaiti  Vd.  4.  a)  von Personen  'Spitze  sva.  an  der  Spitze stehend'^;  zara%uslrS  .  .  ratus  astvaihyö ga/^ayä  •nuf  Mpaitiaea11ayiYt.13.41;  — fravaiayS  yazamaide  'nsf&t  aiahe  yat vaMltahe  G.  2.  7.
17186:—  ca%!warJ  ■vastära  spaSa  .  .  *zatUa  Yt 5. 1 3.  b)  von  Bergen  usw.  'hochgelegen, hochragend':  garayu  *zant»  (NP.)  Yt  10. 14;  rj.  9;  —  staomi  garayS  'zants  (als AP.)  Y.JO,  3;  — ■  upairi  harqm  "zaitfm Ytio.  50;  118,  V.  jp.  30,  2/.  s;  —  har>- haya  (sd.)  *'zaitaaya  (LS.)"  Yt  J.  54;  — ainS  'zatö  sürahe  S.J.  27.  c)  von  der
21517:(auf  welchem,    näml.  Berg)  das  Han  -  oder der  Asphalt  -  (wächst)'.  —  VgL  «L  jälaii-  n. 'Gammi',    np.  iad  'Gummi',   angu-iad  'Harz', —  ■)  So,  ohne  Trennung,  alle  guten  Hds, j.  "yakva  Yt.  10.   2S:  s.  ya-,  Sp.   1304  O.
```


## [2026-09-14T01:58:21.923Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"haraiti-\\|hara-\\s*f\\|harä-\\|hara\\.\\|Haraitl\\|haraiti  \\|hara- \" BRT.txt | head -20; echo \"======= haurva\"; grep -n \"haurva\" BRT.txt | head -20"
}
```


### [2026-09-14T01:58:21.997Z] TOOL RESULT

```
8269:•  j.  upaoianh'va-  Adj.  (fem.  °vä-)  'im Osten  gelegen.  Östlich':  haraiti  barif  .  . päirisäite  fräpaya  (sd.)  datikul  S  'väs/a Ytig.i.
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päirisaile  .  . "das  jy.-Gebirg  . ,  umlagert  . . ;  . .  das  Z.- Gebii^,  auch  das  umlagert  . ."  Yt  ig.  i; y- 69;  —  Vlspe  ,.  tirKtnti  pfnmne  {%äj) avaia  mävayaiit.-tprisantu  Yt  14.38;  — *daSinqtn..Äaoyqm  h! paiayqm ..  dumtnüit Af  upa.%w^r^saym'V.i3.ai.;^vlsfe  haoma . . yaicit . .*upa  *dintäku{sA.)  V./0.17J  — Aazaignrn  maoirinqm  d3nS.karSanqm  ava.- jartyat  duye  hazanre  anyalsamat'-'^  V.  18. 73i  73i  —  ^y^  *gr}Amö  ä.ASi^Si  (sd.) «r  ksvayas^l  xratül  «r  dadat  ".  .  Gr., de^leichen  (sva,  und)  die  K.  richten  .." Y.  J2.  14; —  aSavatca  alsasät  ästärayeite (sd.)  N.72; — nava..anaiwyasHi  kunämi; hinti  (Sp.  370  o.)  .  .  mävayacit  ca^warS arsäna  V.lS.^j;  —  ksnti  anyäsät'^  (Sp. 137  in.)  asäs^a  /äi^ris^a  srIras/a..Y.l.2o; —  aam^i  akyS  . .  %wam  tUSökj  , .  vai- <hm  (sd.)  Y.  ig.  10;  —  mainya  .  .  yS  ä narSm(,sd.)ät.,Aäi>0  Y.^i.y  i — in  auffälliger Stellung:  mUca  paslaSa  mazdayasna  vXmä- oasHt*^  vTmSoayanta  "nicht  sollen  sie  dann auch  bei  M.  als  Ärzte  praktiziren"  V.  7, 38;  38,  40;  —  hinter  ula^^:  iavaj  aiwi.- vanyä  .  .  ta^ryävanttm  , .  ptiatamca  .  . Uta  anyäscit'^  ..  kyaon&tgkB  Wtig.ST, 89;  —  hasannm  aspä  uta  äsitqmHt /rastUntim  Yt  18.  5 ».  a)  Bei  hypotak- tischer Saufiigung  steht  das  mit  /■■  hervor- gehobene Wort  jeweils  an  zweiter  Stelle*', U2W.  a)  des  Hauptsatzes;  b)  im  Aw.: Sfit  MOra^uslrS  da^äU  sanm  vyämrvUä .  .  flS-a  *aspm^  .  .  vlinruyg  Y.  12.  6\  — ya'ha    . .    kvarsxiatä^m    .  .  fraca    Siti  .  .
13095:j,,  g.  dahyav-''  j  dahyu-^''  f  'Landgebiet, Landschaft,  Land',  oft  zugleich  auch  von den  Bewohnern;  a)  im  Aw.:  haraiti  bars .  .  hama  psirisäite  fräpayä  (sd.)  °rihus  ä upaola>ihvasca  Yt ig-\;  —  kahrkasS  .  . yS  naotnyä{sd.)cit  haca  'hihaot  .  .  xrUm aiwi.va&iaiti  Yt.  14.  33;  — par3  *S3mS  al- tanßta  *'iih3us^  anhat  b>rptd{s^)  7-i}sir?m V.  2. 24;  —  nSii  ..  asar?hal:a  /i^fyraf/a 33
14299:•  p.  S'üra'vähara-  n.,  GS.  mit  mäA-  m. Name  eines  Monate*';  'rakya  «a-iyj (sd.) JTO»i.^i/Bh.2.  7;  8,  11,^.6.
15638:•  j.  pairiSta-Bhara-  Adj.  'von  ausge- suchter Wohlgeoährtheit,  auserlesen  feisf : neil  pastiica  (statt  IS.)  . .  irista  (sd.)  riüu- frÜ  abanta  airiäa  *aiäya  'ra  raiußis S.56.
16917:KompA.  ■),  £.  —  Zum  V.  ^bar-.  —  sä.  'bharä- Adj.  (fem.  *rä-).  —  VgL  noch  >p.  'Apniißäpiii, IF.  p.  186.  —  t)  Zu  den  Komp.  mit  bard'  s. unter  6ardaaii%r5;
17015:•  j.  *bar»Z-  :  b»nz-^'>  i)  Adj.  'hoch,  er- haben': ratüm  Äj/vwm  Vr,  2.  10;  —  ratSuS hmlf{GS.)  Vt.i.%]  —  Hitrlm  . . yahmät haca  binzät^^  haosravanhtm  (sd.)  Vlä 4,  a)  von  Tönen  'hoch,  laut';  yas3  . . bsDBtn  barat  zaota  väHm  Yt.//.  61;  — yat  bsnism  barst  astra  ('die  Peitsche') vaHm  Yt. /o.  113.  2)  'Höhe;  Berg': haraiti  (sd.)  Äar/{NS.))>  Yt.ifj.  i;  —  upa upa.bdi  Aj«ya  (sd.)  i.wvÄ?(GS.)  Ytj?.  3, Jj.  24;  —  talrfincH  harai'hyä  btrpzö  Y. 42. 3;  —  lainm  harai^yä  barisö  (GS.) Ytr2. 15;  —  karai^yS  paiti  bar^zayä (GS.)*>  Y.io.  10,  57. 19,  Vt  10.  50,  90;  — vispkhu  paiti  öanzähu*''  Yt/o.4S.  [FrBy.: lies  °b?nts  als  Komp.]
17263:•  j.  bitya-'>,  g.  daibitya-'',  p.  duvitiya- Adj.  (fem.  'ya-)  'der  zweite':  paoirys gairil hqm.hiUat  ,  .  haraiti  barl  °iyS  T^r^azS gairi/ Yt.  ig.  1;  j.7,  14.7,  Y.(?.6,  7,  Y.4.3,
25541:•  j.  uruzdi-päka-  Adj.  'Fltissigkeilen kochend',  insbes.  'zum  Koches  der  aus dem  Leichnam  austretenden  Flüssigkeit verwendet',  vom  Feuer:  yS  ätr>m  -kirn daitim  ^Stam  avi  ava.haraiti  N.8.Z1.
25653:•  j.  'urvant-  Adj.  'fassend,  packead': m>rrjahe  , ,  värr/naAe  'vats  ahara.natmäl pisalö  upara-nagmat  "des  Vogels  V.,  der (seine  Beute)  von  unten  her  (d,  i.  mit den  Fängen)  fasst,  von  oben  her  (d.  i. mit  dem  Schnabel)  zerhackt"  Yti4-i9'*-
26195:mit  päiri  'umlagern,  herumgelageit  sein um  — '  (Akk.):  haraiti  bars  hä  kama päiri- sSitefräpayä  (sd.)  datihu^  ä  upaolatthväsca Ytig.i.
29153:•  j.  ha<!ö.gaedä-  Adj,  (maak.  °%d-)  'zum selben  Hausstand  gehörig;  Hausgenosse': cahwamd^wä  (näml.  asli  mihrs)  antar» *äa  (AD.)  Ytio.  116;  —  yim  vä  ainim **5a''  (NP.)  . ,  cayqn  "oder  wen  sonst die  Hausgenossen  . .  (dazu)  aussuchen" N.  J;  —  yö  alDö  '^anqm  yS  bar?smala */rastfnnte  gius'va  *paiti.haraiti  "wenn einer  von  den  Hausgenossen  (es  ist), der  . ,"  N,  Go.
29585:•  j.  haraiti-  f.  Name  eines  sagenhaften Gebirgs'*:  paoiryB  gairis  hqmMstat  . .  'ti baH  Yt.  /().  I ;  —  ta^rimcä  'raikya  b»r9zB Y,  42, 3;  —  upa  tamm  'raiHyä  banzS Yt  /2,  2  5 ;  —  'rai^ya  patti  bar?taya  Y, iO.  10,  57.19,  Yt./o,  50;  90;  —  mihr>m .  .  y5  vtsptm  aAum  astvantim  ädthäiti 'rai^yJi  paiti  bamankai  YL  10.  5 1.
29594:•  j.  harä-  £  Name  eines  sagenhaften  Ge- birgs:  mihrpm  .  .  yS  paoiryS  . .  tarö  'ram äsnaoili  Yt  /0. 1 3  ;  —  upa  upa.bdi  'rayä Yt.  5.  a  1 ;  —  upa  upa.bdi  -rayä  btrizS  Yt g.  3,  77.  24;  —  iipa  tainm  'rayä  yuxtayä paiti.ayaaÄs  (sd.)  Yt  ij-T,  —  sonst  mit  b;»^ zaiti-  lya^a  . .  Avarvx/atüm  farasca  'ram bfmainm  fraca  aiti..  Yt/0. 118;  V./p, 30,  2i,  5;  —  'rqm  bftvzaitlm  *pouru.' fraimrvaityain  bämyam  Yt.  10.  50.
======= haurva
3368:—  yaisa  ni  d.ltl  . .  ''i^a  nä  >rJedüm  V. 5^-5>35-^'> — yit^ä  iä^aca  dahms  staota yesnya  haurva  daoaiti  '%a  ratu/rii  N. 3~;  —  yd^a  . .  nminopaitlm  paiti  tard.- pi'iw>m  dai'hyat  'ia  astryäH  "als  ob  er
3397:•  j.  aihaurvan- '':a^a«r»n-,  äSravan-'' m,  'Priester'  im  Al!g e meinen ,  von  dem, der  Priestetqualität  besitzt  und  priester- liche Funktion  verrichten  kann  und  darf: uUa  nS  zlte  -va  .,  zara^uslrS  YLi_y.94;
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
4778:;von  Arn.  geschützten  Pflanzen",  in  Dual- verbindung mit  haurvatat-  (sva.  Wasser): 3^ar3%3m  myasdam  haurvatä  °r)tata  gäus huha  haomitnca para.haomamid Y.8.i;j.i, 4.1,  6.1T,  7.26.
6084:(als  Subj.)3>  ya  'sät  gSUs  taiä  (sd.)  mraet Y.4/i.g;'~  mq'ir^m  yim  haurvatatS  'iahyä amsntätaicä  (sd.)  Y.gi.d;  —  kä  "iswöi 'iä  (Vok.)  äka  (sd.)  arpdrfng  isyä  Y.48. 8;  —  daidl  'iä  (Volc)  tqm  ailm  vanhsui ayaptä  manaifhö  Y.  28. 7;  6;  —  yS  vi mazdii  ahurä  pairljasäi  .  .  maibyO  dävBi akvh..  Jj-iT/t/J  (sd.)  'iilihacaY.28.2;sj.i; —  yahä  'sät  hacä  gqm  vJäal  (sd.)  västryS Y.5:.5;  43.14;  —  a/M  ahmai  mazda  'iä a»haüT..  ys..  "und  dem  o  M.,  wird  es (das  Rind)  durch  A.  zu  teil  werden . ., der  .  ."  Y.50.  3;  —  yehya  mUi  'iät  haia vahistsm  . .  valdä  (sd.)  mazdä  Y.5J.  12; 27. 15;  —  yqm  da  . .  °säcä  cBü  raneibyä (sd.)  xinOiim  Y.^i.$;  —  yj  vlänaet  da- iipmcä  (sd.)  aäa'Samli  dangrä  mante  -ia (Instr.)  mazdä  ahurö  ".  .  durch  seinen kundigen  Berater  Aia,  er  MAh."  Y.  46. 17;  3^-  '3;  —  vahista  säsnanqm  (sd.) yqm  .  .  sästl  'sä  ahurJ  Y.  48.  3;  34.  12, 46.  2;  —  maxdä  *yä  da  'iä  vanhSui mayh  (sd.)  manauAs  Y.  4y.  a;  44- ij  — yezl  ahyä  °iä psi  mat  xiayehl  (sd.)  ..mazdä Y.44~  15;  —  at  ahyäi  'iä  mazdä  urvarS vaxiat{sA.)  Y.48. 6;  —  ätrJm  ..  aojSt»hvan- tsm  'iä  Y.34-4'i  —  ^^  adr'ärum  . .  dalnk saoiyantqm  yä  ^haJc?r?tll  'iäcTt  urväxsat (sd.)  y'34.\z;  —  ks  vä  'iä  äfraiiä  (sd.) Y.5/.  11;  44- S;  —  'sät  hacä..  vaidä (sd.)  yS  Im  dat  Y.  45.  4;  —  vidui  (sd.) 'iä  ySm  mazdqm  ahur?tn  Y.  4S-  8 ;  — va»kSui  'iä  Aaozq%7Väi  (sd.)  ä  mananhs Y.45.  9;  —  ärmatsii  kasilt  'sä  hutSntus (sd.)  Y.  49.  S;  —  tSm  vS  'sä  mShmaidt huiJiaxäim  (sd.)  Y.  46.  13;  —  mazdä ahurS  'iä  hui.haxä  ifmvatä  Y.  32.  2 ;  — mazdä  ..%wävqs..  at  ns  fryä  °iä  dazdyäi häkurmä  (sd.)  Y.  44.  i;  —  spmtaHyäiä tur?i.. yehya  urvä  'iä  haiaifl (sd.)  Y.34. 2 ;  44. 1  o,  46- 16;  —  neit  'iahyä  adlvyeintj (sd.)  *hacsna  Y.  44. 13;  —  'iä  vyqm  (sd.) yehyä  hihäui(sd.)  nä  spmtö  Y.4^.  7;  — ärmaitlm  ..hi%qm  (sd.)  'iahyä  Y. ^4- ro; 4ß.  16;  —  tqm  dainqm  .  .  yä  msi  gai'iih •iä  frädBit  haiSmnä\sA)  Y.  44. 10;  43. 6,  34.14,  44-to,  4o-i',  —  'iahyä..  sairJ (sd,)  'iahyä  Virszsm  Y.35.Z;  41.6;  — /praiaaiträi  urväzistqm  (sd.)  'iahyä  da. sarSm  Y.49-8;  5J.  3,  31. 2\;  —  'i^miä ^ fradat.gal%Jm  Y.  j;j.  1 1 ;  —  'ia  (Vok.) kal  %wä  dar}sänl  (sd.)  Y.2ÄS,  45.6,  ;^. 6;  —  humqsdrä  (sd.)  °ia  (Instr.)  yeiä  yä
6302:•  j.  *asa'vaat-'*  Adj.  i)  'rechtschaffen' (nur  Ableit).  i)  'der  das  (höchste) Anrecht  a)  besitzt':  haurvafsavS  .  .  drvä Maurva  -vantö  (NP.)  Y.jÄiS.  b)  'ver- schafft':  hadiiasca  (sd.)   'vaiS  vOstravatS
6869:Ikät^  'rynt    masdqm..aat  mr€oH^Xvtxz.,\ jnier  I  1)    "rö  mazda  V.  2.  if.;  usw.;    — j  dim  p9r^sat  sarai^uslrS  -rahe  (statt  Akk.) ' masdi    Nile  i ;    —    wii    mraot  (Stverz-,  [ nnter  1  3)      °rJ    masdä    V.iS.i;  usw.;  — miinm    .  .  y5   gimatte    'rät    mazdai  Yt. ' '''■53;    8.  to',   — frSmraot  °rS  mazda  Y. M.  1; — jiimäi ..paoiryS  maiyänqm  apsnse^ oum    y3     "rö    mazdä    V.  2.  2;  1 ;    —    äat ioxta   *rj  masds  V.  2.  21,  40,  42;  31,  Vr. 3.  3,  Y,  10.  9;  — paiti  sS  aoxta  'rS  mazds A.4.6,  H./.  2,  7,  P.27,  FrW./o.40,  Nik. 2;  —   aite  sl  vä^ . .  "rS  mazdn  främraot zara^ultrai  Y.  7/,  14;  ig.  i,  15;  —  rätayS ..*yqm    °rv  mazdil  xaraisuiträi /ravavaca frä    tara^uitrS  gaiHäiyö  ..  Y,6§.g;  — ja'ia    dim    isat    °rS    mazdh    V.2.32;  — jaia  . .  zaois  mana  yat  °rahe  masdä  Yt. ir).%z;    &35;    —    xmaoi:ra    (sd,    auch fdSt.)   'rahe  masdä  Yt.  7.0,  usw.;  — j;As- maitie  'rahe  mazda  Y._^.  i,  22.4,  23;  — frasasti  °rah*  mazdil  Y.  S.  i;  —  staotala .  .  yat  a^a  'rahe  mazda  Vt.i}.  6;  —  /ava 'ra  mazda  yasrum  . .  vahm>mca  Vr.  21.  a; P._3P;    —    ramasf    ti  'ra    mazda    "hrlsHt pars  anyäis  ääman  Ny,  /.  i ;  Y.6S.X2,  Yt. 7.1,  V.ig.25;    —  fumahl  iyiJmS    *'ra.- wiazdä'"'*    Y.  5>y.  3;    —   yat   zaota    'rsm ma-uiam  yazäiti  N.  70;  Y,  25. 4,  57.  a,  V. 7q.  19,  Vt  6.  4,  77. 18,  Vr.  jj.  I,  i8. 1,  23. 1, G.5.S;usw,;  —  kö  mqm  staoiti  yim  'r^m mazdqm  H.7. 3;    —    'rai  mazdäi  haomq äJoAayamahi  Y.  24- 1 ;  Vr.  //.  16,12.1;  — zbayamahi    JrJnämahi     mqm    ytm     °r>m mazdqm     Yt/2.3(?);    Vyt2.^(;    —    'nm mazdqm    danyo.yas/fmca  (si)    hqm.parl- timca  H-2, 14;    —    ks  itvqm  yim  °rgm mazdqm  . .  mazista  ibaisatiha  tbaisayeiti  V. /iS'.6i*;zitY.(?.8PiiZ.; — mä  zl  ahmt  nmane . .  fnm  i-aocata   mqm  yim  'nm  mazdqm yaia  ..  P.  17;    —    i^a    dim  ^ara-cinasti yim    'nm    mazdqm     .  .    damabyS    Y.  ig. la.        a)  in  Verbindung  mit  andern  Gott- heiten: 'rahe  mazda  . .  varahSus  mananks ..asahe  vahisiahe  .  ,  xia^rahe  vairyehe.. tpmtayB    ärmatöil .  .  haurvatä  amir^täta  , . .  ^ui  urune  gSUs    lalne  .  .  ä^re  °rahe  1 mazda  Y.  70.  z;  /.  if,,  57.24,  Vr.  i/.  16,  j ^-  5-  5«  V.  7p,  1 1 ;  —  -räica  mazdäi  srao- , s.Wa    a^.li    rasnvalta    razilläi   mt^räica Vr.  //.  6;  Y.  4. 2,  Vyt  i4;  —  «Äu  me  'ra , mazda   uäa    üpS  urvar&sca  usia  daine  .  . , VlÄ  29;  23.  a.)  bes.  häufig  mit  den
7140:—  yat  titarat  (sd.)  attrö  tnaittyus  duhjm alahe  . .  antar)  pairi.avsilim  vohula  tnanö "tarsca  ta  hc  taurvayattm  tba!sa  Yt.  13. 7 7 f.*';  —  asim  vahütim  'tnmca  Y.2.4; 7.4,  A.  4.2,  S.  7. 7,  2.7;  —  xmümaine  ahu- rahe mazdä  am»sanqm  spintaiiqm  sraosahe afyehe  °^riJ  Y.  22. 4;  —  mana/a  yastum yat  ahurahe  mazdä  'hrascd  "S.^ff;  — haurvata  anitrstätä  ,  .  gjui  tarne  gfus itrwie  ..    "'hre  Y.JO.2;    7.2,  Vr.p-S;  —
7233:drang'  V.  ('festhalten')  'an':  ysi  a  varshSus manaahS  didrayzS.duy!  Y.  4Ä  7.  b)  un- räumlich, zur  Angabe  a)  des  Mittels  'mit- telst, durch,  kraft':  yS  taots  as3  »rtzüs  hvS *mainySus  3  vaAist^i  kay3  (sd.) , .  v3stry3 ^■33-6;  —  masdh  dadät  .  .  haurvatö  .  . bßteis  ä  asa^alS  :x^3paüy3j (sd.)  ..  sarff \. 31. 21.  ß)  der  Veranlassung 'wegen, (zum  Dank,  in  Vergeltung)  für  — ':  gavSi 3rBii(sd.)  *ä  sindä (sd.)"'>  . .  yS  tlsSnghB.. V.  5/.  14;  '''4'-*';  —  väahius  as3  haozakw3t (sd.)  ä  manaahs  Y.^^j.g.  l)  des  Be- treffs S'on  wegen':  tat  '^wä  pansa  . . tiitnatahB  ä  ya'^a  tuinS  (sd.)  x^mävatS  Y. 44.1.  5)  akmat  *a  adv.-artige  Verb., sbes,  b)  '(bis)  hin  zu  — ,  usque  ad  — '; a)  räumlich:  /rasa  frayoit..a  zanga^byas- Hi  äps  a  inubyascii  V.  6.2T,  27';  —  astit 3  irtzäs  (sd.)  pa'iiS  \.33.$.  a.)  a  mit Abi.  und  mit  Akk.  nebeneinander:  pa'i'3 ■  ,  yJ  asti  razistö  ä  aiat  vakist»mca  ahum \.6S.\i.         ß)  blosser  Akk.  und  ä  mit
7424:fWit  sptntqm  dsn/ilsä.)  ahmäi  stöi -lim  tiaedä  voka  .  .  fra^tä  (sd.)  manauha Y.4.9-2;  —  fi-S  spinta  'maus  (VS.)  asa daf/iä  /radaxiaya(5d.)  Y. 3^.13.  2)  im jAw.,  stets  mit  j/^Wa- Adj.^':  akurake.. varfhSu^  mananks  ..  alahe  . .  xsa'^raAe  . . spintaya  °tsis  .  .  haurvatä  am^rslüta  Y. 70.2;  i.  2,  57.  24,  Yt  /.28,  S.2.2-7,  G. S.Sj  —  ahuräi  ..  as,li  ..  xsa'^räi  .. sptntayüi  'tJe  Y.i^.ii;  —  mazdä  .. haamnO  *mi^ra  rashuÜa  .  .  °ticä  (IS.) spmtaya  Yt.r>3;  r.27; — pita  /£' (näml. asöiS)  ahurö  mazda  .  .  m3ta  'lis  sp»nta Ytij,i6;  *SrB.j;  —  dämim  ..yqm  'tim sp3ntqm  yeke  däkre  asakeca  ..  Vr./p.  2  (?); 2.  5,  Y.16.3,  S.2.5,  Vyt.so;  —  'dm  spm- tqm  yäsca  t!  -/?nä,  ahura  Vr.^.4;  ^9-  i, Yt.4.1;  —  Hai  <toiäe  spitUayäi  'tleispmta 'matte  immt  tl  .  .  V.iS.^i;  —  sp3ntay&
8199:•  g.  'uta-yütay-  i)  Adj,  'perpetuus, dauernd,  beständig':  data  vi  amtr^tascä 'yUitl  (ASn.)  haurvatas  draonH  "schenkt, o  If.  und  A.,  euer  beständig  währendes Gut"  Y.JJ.8.  2)  f.  'perpctuitas,  Dauer, Beständigkeit':  aimrttäitl  *asaottö  urvä ais3  'yatä  (LS.  &v^  'immer')  ja  furqlsadm (sd.)  drfgvats  Y.  4$.  7;  —  ap  kshrpim 'yüitls  (AP.)  dadat  ärmaitii  qnmä  (sd.) ".  .  corponim  perpetuitates  .  ."  Y.jo. 7.  a)  mit  totfl"-  f.  verbunden:  ha  zi nS  husöi^»mä  (sd.)  Aa  «Jf  'yüitim  dat t^Tsim  Y.4S.6;  —  'yüitl  (IS.)  t^vlsim *gatJ/'i(s±)  vasfmTY.43. 1.  a)  in  Dual- verbindung damit:  Ayal..  M^t  (sd.)  . .  haur- väta  am}r?tata  .  .  ahmai  stsi  dqti  (sd.) iivin  'yBiiT(AD.)  Y.^lj.io;  Si.j^ 34.11.
10730:ntanauhl  '%r3J  hcUü  paitt.mraot  asä  kuL- haxa  Y.32.  2;  —  mazdä  , .  vokü  uxfya (sd.)  manavAä  °hr3  aiälä  ustä  tanüm Y._jj.  10;  —  yahmi  spfntJ  %wä  mainyU urvafse  jass  mafsds  "ärä  ahmt{s,A.)  voha mananha  Y.43.6;  —  aAmäicä  «ärJ  (als Sah].)  ^^ /asaj  (sA.)  mananha  voha  asaüä Y.3Q.  7;  —  ahmsi  dqn  (sd.)  .  .  mazdä •^rJ  armaitf  ahurS  Y.  47.  i;  —  kj  binx- 'iqm  täil  ''hrJ  mal  ärmaitim  ^..44.1;  — kada  masda  ala  mal  ärmai/i/ /imaj  (sd.) •^ra  Y.48.11;  — yqm  Asi  °'^ra  voAuäi cdiit  (sA)  tnananhi  Y.^o.y,  —  mazdi dadät . .  haurvat3  aminlätasca  . .  asahyica ..  •UraAyä  sarS  (sd.)  Y.^jj.ai.  a)  im YHapt,  mit  va^hav-K^y.as>m..vahist>m ..vohuia  maiid ..  vokucä  '"hrsm  \.3~.i,i.\ —  asäatcä  hacä  varahsuseä  mananhs  vatf- ksusca  'hrai  Y. J5. 10.  a)  im  jAw.,  mit va i rya- Adj. :  '^rtm  vairTm  amihm  sptn- hm  yazamaide  S. 2.  4 ;  Vr.  20.  i;  —  ahurS mazdä  . .  vohu  manö . .  ahm  vahist»m  .  . ''i:r>m  VairTm  .  ,  spmta  ärmaitis  .  .  Y. 57.  24;  1.1  f.,  /tf.  3,  Yt/.  25,  4.  i;  —  ahu- rake  maxdä  .  .  vanh^us  mananhB aiahe ..'"hrahe  vairyeke..  Y.70.2;  —  aku- rai  masdäi  . .  aläi  . .  °^rai  vairyät  armatSe V,  iff.  iii  G.J.  s;  —  vaAu  manauha  haH- mnS  aläca  .  .  '^r3ca  ya  vairya  FrW.  /, I ;  —  viscihnm  dim  ayasata  Syapta  (sd.) ■ira  vairyaY.2Q-^(J\  k)  xlaiirahe  vair- yeht  a)  (nämlich  mS)  heisst  der  6.  Monat im  Jahr:  pancaca  haptaitttn  *pailisJiahyehe (sd.)  '"hrahe  vairyehe  anayranqm  A.  3. 9.  ß>    (nämlich    ayani)    heisst    der  4.
11014:—  maitiyB  3%raiä  Y.  31.  y,  22;  — mainya  syaoianäis^ä  Y.  Ji.  ai;  —  pa- s?u/vTräat^äY.3i.i5;  —  haurvatB  amir^ tatascäY. 31.21;  32.5,  46.1,  18;  —  dra- /as/ä(Sp.$T3  ta.) pairimatöiscä  Y.J2.3;  — y^!ttg  *slrSmcS  Y.44- 3;  —  ^pl' >■«,'  ^äiayi W£«;>Ktfji-'äV.6'.33(s.  dagegen  36,  Sp.5680.);
11029:—  laimye  .  ,  uruiiaSca  Yt  i~.  22;  — kaittibyü  . .  xsmatbyaca  Y.  5y.  5 ;  —  haurva- tsts  ,  .  amfr.tälasca  Y.31.  6;  — jyai7u? ,. vasS-itdii^a  Y.5_j.9;  47.6;  —  yaää  hvB arf hat  yl.iyaoianasiäY  .31.16; — akurahya xratSiJ..aiaatca  Y._j2,4; —  yeMi  hatqm ..vanhs .. yärahqmlä ..  Y.2-.\y,  —  as>m  .. manasla  vohü  Y.  28.11;  —  aiaAya  .  . vaahSusca  manat^hs  Y.33.  3;  —  vanhSui manai3hs..syaokana . .  spmtqmia  armaitjm Y.34- 10;  —  Aatiuharyne  . .  hSyUmla  dH- ^nm  Y.ii.\;  —  tä  urvata  ..  :^Uicai> ^miti  Y.30. 11;  —  ;tarff  .  .  gju/cä  urz'a Yt/^S4;  —  masdä  yasrum^a  vahm9m?ä (beide  als  i.  Glied;  Sp.  567  u.)  ..  ^ulca västrpm  Y-33.  7 ;  —  vaahsui  xralüm nat9h3..gSusca*urvq>i»mY.28.\.  a)  in auffdlliger  Stellung:  yS  anhai  asul  . .  hu-
11041:Aw.;  i)  die  Glieder  sind  nominal;  im gAw.:  at  %wä  mSnghäi  taxm?inca  sßsn- t»m  Y.  43-  4 ;  —  dätil  v3  am>r)t  'iscä utayüitl  haurvatäs  draonS  Y .  j  j.  8 ;  — gjtämcij  ahurai  sn'l'tili  araohm  (sd.) Y.  28.  s;  —  asahyaca  .  .  xsairahya sarS  Y.^I.  21;  —  /fl^<J  vi  yaz^mnas^a urväidy^  isA.)  slavas  aymX paitl  \. 34.(1 ;
11042:—  im  jAw,  nur  beim  Zahlwort:  pancä/'a haptäitim  h.  3.  q,  12  (s,  dagegen  7 ;  Sp, 569  o.).  2)  die  Glieder  sind  verbal;  mit Tmesis:  m!ncä  T  [inaz\dazdäm  fsd.)  vafdd- dam  . .  Y.59.  5.  3)  bei  beiden;  b)  im Awf.;  i)  die  Glieder  sind  nominal;  a)  sie folgen  sich  unmittelbar:  uhi  kaurvascü amsritathscä  '^■34-  n;  32.  15;  —  van,ll haurvasca  ain»ntih'a  uva  SiPum^a  tar'- n^mca  Yt  /p- 96; —  *a:'a(ND.)  .  .  vyqsca vyänasca  Yty.  35;  —  twaSm  i^arfiimca vattnmca  Y.  55.  z ;  —  yais  ap3r»saH?m mazdiscä  zara^ultrascä  Y.  /2.  5 ;  —  at hv5  . .  Tsäcä    ataitilcä  Y.4^-5i  V.5. 53;
11071:Glieder  sind  verbal:  yBi  ztjvä  (nämL  hitOt) *ar»har3La  bvanticS{sA)\.4^.T.  3)bci allen;  a)  D  im  Ap.;  das  letzte  Mal  steht Uta  statt  cä:  pärsamcä  mädamcä  utä  aniyä dakyiivaf"  Bh.  /.  14.  b)  im  Aw,;  i)  die Glieder  sind  nominal ;  a)  sie  folgen  sich  un- mittelbar: nmänyasca  visyasca  santumasca Y.  if).  18  (s.  dazu  18  aA.);  —  aojasca  v»ty- 'inmca  j^armas^a  lavania  Y.  7/.  8 ;  —  sta- rasca  mäsca  >fe'<i/vi-'(7  YL72,25(s.dagegeni_j. 57);  —  vätftnca  vänmca  tnafy^mca  Jyau- humca  Yt  5.120; — hubprvtlmca  uslaMin- tlmca  vanta.bintTmca  Y.  61. 2  (s.  dagegen  7 ; Sp.  570U.);  —  maziUäsca  vahiitasca  srais- tas^a  asayS  Y.  52.  3;  —  apasca  urvaräsca xadirdsca  Y. A3;  —  asavafom  htnümca bavaniiinla  busyantimla  Yr.lS.i; — vTspayä ..slöis  haihyJica  bavqihyäica  büiyqi^yäica \.6S.i3i  —  nm3nanqmcä  vlsqm^a  satttu- nqmca  dahyunqmca  Y.  Ä  7 ;  —  damayä  anu- matayal'a  aiiuxtayaica  * aim.varstayai^a Y.Ä7;  —  d^aurunqscä  rä^aistiscä  väs- tryqscä  ßuyants  Y.  ig.  3;  Yt  ig.  8;  — ahamca  ratümca  paoirimca  tkaisim  Yt/^J. 152;  —  ha^ra  miiräca  rasnuta  uyraca dämSis  upamana  Yt/_J.  47;  —  vispss^a paiti  vansajls  vTspSsca  paiti  frasparrjJ i'JspSsca  paiti  fravaxsS  Y.  jo.  5 ; — haurva- tasca^  fiö  am)r>täta  gSuica  taSnB  gSusca urunS  ä%rasi-a  aoxtsjiämand  hadisasca  Vr. g.  5;  —  beim  Zahlwort:  navaia  navaittfca navaca  sota  navaca  Aazavra  navasSsca baivqn  Yl;_J.S9.  a)mitTmesis:*«ai/x
11420:dem  Leben  trachtet':  yS  saHe  haurvam tarasla  xsapansm  ayazimns  .  .  jayäi  (sd.) 'fam  V.  iS.  5.
```


## [2026-09-14T01:58:28.713Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^•  *j\\.\\s*haurva-\\|•  j\\.  haurva-\\|haurva-  Adj\\|haurvaiti\\|har-  '\\|•  har-\\|hara-  Adj\" BRT.txt | head -20"
}
```


### [2026-09-14T01:58:28.790Z] TOOL RESULT

```
15638:•  j.  pairiSta-Bhara-  Adj.  'von  ausge- suchter Wohlgeoährtheit,  auserlesen  feisf : neil  pastiica  (statt  IS.)  . .  irista  (sd.)  riüu- frÜ  abanta  airiäa  *aiäya  'ra  raiußis S.56.
29644:•  j.  haurva-ßav-  Adj.  'des  Haustiere unversehrt  sind';  pairX . .  dadrmahf  'fsavö (NP.)  Y.5Ä6.
```


## [2026-09-14T01:58:30.811Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '29560,29660p' BRT.txt | cut -c1-400"
}
```


### [2026-09-14T01:58:30.868Z] TOOL RESULT

```
Pü. :  iu/v^U  äälJr,  erl.:  Ia&  dilik;  vgl.  kva- ahaoya-.
•  j.  havaehva-"  n.  'gutes  Leben,  Selig- keit':   "vmfhum  ml  buyata  mävSya  haväi
urune  sbayemi  Y.  7/.  1 1 ;  —  'vatjhsi  urutK /radahäi  gaihanqm  Y.68.4;  —  sonst neben  aiavasta-  (sd.):  a/ttnakim  'vaau- Aäila  asavas/äica  W.  14.  1;  11.  10,  Vr.5. I ;  —  3ca  nS  Jamyat  'vaffksi  . .  asavastai Yt.  10.  5;  —  tu  nS  ama  .  .  tä  •var^ha  .  . tä  alavasta  .,  uejamyan  Y.55.  3; — yas? %w<l  yasämahi  .  .  'varg/tum  asavast?mca Yt/o. 
(ewige)  Seligkeit':  tanvaica  * kaosravanhtm urunaeca    darrf>tn    'vanh)m    F.^J  h;    — dätim  tl  tanuye  x"ann3  urunalca  darrjpm *vatih»m  Y\.i-].23;  —  vatihauca  sravahe urunag'a  danye  'vatihe  A.  i.  11;  —  aAeca aisliSus  dary/ai   Aaesrava^Asi    manahye- keca    aahlul  darrjai  'vatihäi  urune  asti vahistam  Vyt.js. KompA.  —    Ableit.  aus  *Av-aohav-  Adj.   
•  j.  havana-  m.  ('Auspresser,  Kelterer') Name  für  die  beiden  Teile  des  loi  Haoma- bereitung  verwendeten  Geräts,  spez.  beim ffaemamÖTsti  des  Trogs  und  Stössels*': fraiarfm{&A.)(it  tl  °»?m  . .  upa.staotni  . .  yö qsui * hanglurvayete  upanmat''  U  °n»m.. yahmi  niyne  nars  aojanha  "das  erstere (untere)  Stuck  deines  (des  Haoma-)bAÖt- sers  . .,  das  die  
'Mörser":  'na  däityBJarttaY  .14.%.  [N. lOj  aA.:  lies  hävanalibya;  —  N.47  aA.: lies  Aävanifiqm.]
*)  Abbildungen  des  heutzutage  üblichen  ans Kapfer  hergestellten  Mörsergerats  finden  sich allenthalben.  Früher  bestand  es  wobt  zumeist aus  Stein  und  der  Trog  war  demgemäss  wesent- lich flacher;  vgl.  H.  lOS,  wonach  der  kleinste zulässige  Morser  nur  drei  HaomaiMiex^t  fassen  tu kännen  brauchte.    Vgl.  auch  Aävaiia-  a.
KompE.  —  Zum  V.  'hav-.  —  ai.  vgl.  aähifä- vaifa-  Adj.  'lut  Somab ereil ung  dienend',  n. Du.  '  Somapressc'.  Vgl.  GON.  KZ,  tS-  526, Bthl.  IF.  5.  370.  —  Pü.j  kävan,  /riltum Aävan  -  aparlum'-'i  hävait  oder  afiar')  Aä^art (vgl.  PüErl.  zu  N.  /o/).  —  ■)  Vgl.  gr.  Ztipt; ■Mörserkeule'.
dby  Google
178?
havant-
•  j.ha'vant-Adj.'gleichgross, -viel, -wertig'; Plur.  'einander  gleichstehend':  ks  °vqs  datv5 "wer  ist  ein  (den  wirklichen)  gleichwertiger Z).?"  V.Ä  31;  32;  —  {tat  'vatqm  nana (sd.)  yahmi  .  .  N.ij;  *9'1;  —  _vaS<i  °va^ vag^at  N.  68{}).  a)  mit  Gen.:  yesi  .  . *'vanti(APa.)'^  ailahe  syao%nahe  v»r>syqn nsca  kainila  kanäca  "wenn  . .,  so  wirken gleichg
KompA.  —  Eig.  'wie  er,  ihm  ähnlich'.  —  tnp. havanii.  —  Vi.:/ävatiil,  (lu  N.  6S):  ka  ilön  äiäs käl.  —  >f  Hds.  M/a  Iqm;  s.  aber  Pü.  —  ')  So Jpl,  Mfi;  Bthi-  IF.  13.  116.
•  j.  yS  nSit  aiwyasti  (Sp.  278  o.)  aiaya *anäusa  "havayaDhsm  *axtlm  N.  15.
Tu.:  aannnd,  Var.;  aanada.
•  j.  '^yS  Aaxdira  havara  yim  aiwüvinat^ VyL/o".
■)  Vgl.  Vyt.  31,34,  43.
•  j,  har-  V.  'Acht  haben  auf  -'.  Praes. 3  hara-,  20  haurva-;  Perf.  i  hankar-.  — Inf.  har>tayat-ca,  Aankmi.
'Acht  haben  auf  — ,  wachen  Über  — ,  be- hüten'; hanhaurvah-  PPfA.,  nur  als  EN.
mit  m  i)  Akt.  dnwS.:  srao^fui  .  . yd  .  .  nisAaurvaili  matää  dätnqn  Y.57, 16.  a)    ohne  Obj.:    h3?ä    nä  fsUmä
nisanharatü  ■>  hi  aiwyäxsayatä  Y.  jÄ 4.  2)  Med.  'sich  behüten,  bewahren,
retten  vor  -'  {pairi  mit  AbL):  >u/  ..  vXspö atiAuI . .  «r  pairi  iti^yastatat  (sd.)  Aaraite Y.ig.io.
S.  noch  haiifar;  hiiära-,  hära-,  —  zEt.  mleWt OsTtlOFF  Pareiga  204;  s.  noch  unter  Imra-.  — Pü.:  sardärinäatt.  —  <1  Nach  S  2ötf.  48  für *nisAariitH.
•  p,  haraiva-,  j.  haröiva-'>  m.  Name eines  Lands,  Aria:  II  ima  dahyäv^  tyä riiana  paiiyäisa'  .  .  "»u*  Bh.  /.  6;  D.  5.  2, Ö.  3;  —  x/tUm  asatfhqmca  . .  frai'W»r»s>m . .  'rSySm  yim  vis.hantam>n  (sd.)  V.  t.  8.
AbleiL  (».  här'\  —  Vgl,  ai.  mtayü.  f.  Name eines  Ftu5Bes(?j,  np.  hati.  —  0  Vgl  lu  öiva; No.  1.
•  j.  haraiti-  f.  Name  eines  sagenhaften Gebirgs'*:  paoiryB  gairis  hqmMstat  . .  'ti baH  Yt.  /().  I ;  —  ta^rimcä  'raikya  b»r9zB Y,  42, 3;  —  upa  tamm  'raiHyä  banzS Yt  /2,  2  5 ;  —  'rai^ya  patti  bar?taya  Y, iO.  10,  57.19,  Yt./o,  50;  90;  —  mihr>m .  .  y5  vtsptm  aAum  astvantim  ädthäiti 'rai^yJi  paiti  bamankai  YL  10.  5 1.
•)  Auch  hatä-  (sd.)  genannt  Nach  Yt.  /p.  I umlagert   da»  Gebirg  alle  Länder  des  Westens
I  sind  nach
hanka-
und    Ostens.     Es    gilt    als    das    er:
nehmste  aller  Gebirge,  alle  ander Bd.  12.  i  (vgl.  unter  fianuru./raeun/aesa-j  aus  inm hervorgegangen.  Um  seinen  Gipfel  (/iKra-)  kreisen nach  Yt.  «.  25  Sleme,  Mond  und  Sonne.  VgL Ggr,  OK.  42.
Vgl.  lu  ia,J-.  -^  PÜ. :  Aar  iuri.
•  p.  hara''uvati-,  j.  harax^'aiti'  f.  Name eines  Lands,  Arachosien:  I  imä  daAyOva* tyä  adam  agarbäyam  .  .  'lis  ^atagtti  .  . D-Ö'3;  5-2,  Bh.J,6;  —  arsada  näm^ didä  'tiya  Bh.^.  11;  12;  —  vahyatdät^ . .  käram  /räiiayc^  'ii'm,  viväna*  . .  *tiyä xsa^''apsvä  abiy  avam  Bh.  J.  9;  I  — äas»m?m  osanAqmca  .  .  frä^wtnnm  . . 'x'aitim  srlrqm
«r.  *iaras^ath  f.  elg.  'die  reich  an  Seen  ist', fem.  £U  *sara^^ant',  —  ai.  särasvali'  f.  FlusS' nunc.  —  Pü.;  aramndO.  —  ')  Angeblich harahmand  (luletit  GIrPh.  /  h.  183).  Aber der  np.  Name  muss  doch  'iatoj^al  gevesen sein.  Dass  der  moderne  Flussname  af/andäb damit  lusammenhängt,  wie  Ggr.  GIrPh.  2. 393  will,  halte  ich  für  unwahrscheinlich.
•  j.  harä-  £  Name  eines  sagenhaften  Ge- birgs:  mihrpm  .  .  yS  paoiryS  . .  tarö  'ram äsnaoili  Yt  /0. 1 3  ;  —  upa  upa.bdi  'rayä Yt.  5.  a  1 ;  —  upa  upa.bdi  -rayä  btrizS  Yt g.  3,  77.  24;  —  iipa  tainm  'rayä  yuxtayä paiti.ayaaÄs  (sd.)  Yt  ij-T,  —  sonst  mit  b;»^ zaiti-  lya^a  . .  Avarvx/atüm  farasca  'ram bfmainm  fraca  aiti..  Yt/0. 11
Dnw,   iatäid;    id.    —    Et?    Faltcb  ZDMG.
•  j.  haroiva-  m.:  s,  unter  Aaraiva-.
•  j.  har»k- V. 'emitlcre'.  Praes.  30  (Itcr.) Aancaya-.
'weg,  bei  Seite  werfen,  fallen  lassen': .  .  yaval  aisa  caräitiia  "avi.mqm  kanks (sd.)  hancayat  V.  5.  60.
mit/rs  'ausschicken,  aussenden':  u^/ aste  franAancayat  äsiite  kataraseil:  spinis mainyus  aU^m  franhartlayat  voAuca  maiUl .  .  anrs  mainyus  franhan^ayai  ahmca manS  .  .  Yt.  ig.  46.
Pü.:  %.  bei  harika:
•  j.  harska-  m.  'was  abgestossen,  bei  Seite geworfen  wird,  Abfall';  nBit..aAurS  matdä ySnAuyanqm  avantanqm  *paitirilyiX  (sd.) dai%e  .  .  yavat  alsa  (Sp.  34  m.)  carai/iia *avi.mqm  'ks  Aanlayat;  yaica  alte  matda- yasna  upairi  aSttm  iristfm  *avi.mqm [•i*^]  "  Atrfzyäf  yavai  aiia  earäitika  *avi.-
dby  Google
1789
'hanta-
haurva'
1790
mqm   °k!  harfiayä^   "nicht  . .  soviel   an Mass,    als   eine  Frau   als  Abfälle   (beim Spinneo)     bei     Seite     wirft;     und    weun (sie)  . .  auf  dem  Toten  so  viel  an  Mass [als  Abfälle]  liegen   lassen,    als  .  ."    V.  5, 60  f.''. Zum  V.  harik:  —  ai.  »gl.  sj-kä-  m.  'Geschoss'. —  Pü. :  iand  äri  ke  carätii  apar  pa  an  patmä- Hak  pa  h
•  j.  'harata-  Adj.  'wohlgenährt,  feist': hatannm  aimmayanqm  °W*  vtspö-gaona- nqm  V,  22. 4.
Bed.  nach  Pü.  —  Ich  verbinde  das  Wort  mit pairiila-akara-  und  weiter  mit  ai.  jar/if-n.  — i'ü.;  i/iirw;  s.  zu  liaierämacu-.  —  >)  Statt anumayaitifm  hanlanum  v' ;  Abkürzung  mit der  Komp-  statt  Kasusform  im  mittleren  von drei  zusammengehörigen  Nomina  mit  gleichem Ka-susausgang;  S.  nocli  ahoUai'inakt  urvnti Jiaspaianahi  Yt,  14.  II,  varäzahe  paili
•  j.  'harsta-  Adj.  mit  einer  bestimmten Krankheit  behaftet 'h  ma  ml  aitayh  tao- ^rayä  fraaharmtu  'tS  *mil  tafts  *ma drusts  .  .  Yt.  5.  92.
Et.?  —  1}  DsT.  ZA.  2.  389:  '/sari,  Gdn,  KZ. sy.  395:  'Landstreicher'.
•  j.  haratar-  m.  'der  wacht  über  — ,  Acht hat  auf  — ,  Wächter':  'ta  aiwysxstaca vupaya  ..  gal'iiayä  Y. 57.15;  V,2.4,  5, F.  24;  —  °tär>mca  aiwyiJxsMr^tnca  .  . vJspayä  /rav^is{sA.)  gag^ayä  Yt.  lo.  103.
KompE.  —  Zum  V.  Aar-.  —  np.  hardär'S.^. — Pü.:  !ardär.
•  j.  har^Säspa-  m.  EH.  eines  Gläubigen: 'paAe  asaonS  Yt.  13.117.
Komp.;  *Aar/ia--\-aspa-,  eig.  'widerspenstige, stöniscbe  Rosse  besitzend' ;  np.  Aä/a,  s.  unter Aartiü:
•  j.  harwSiS-'>  n.  'Wahnsinn,  Verrückt- heit': ma  a^ra  frakavS  . .  "ois  V.  2.  ig.
VgL  mp.  <tj/iiX' 'mad,  lunatic,  insane' JJauaspji
Gloii.  367);  np.  iäla  'bomopravDs,  sediliosa*' (FrMüller  WZKM.  5.  297)").  —  Pü.:  kaiai, erl. !  äaslaauar  ni  dirit.  —  ')  Oder  •Jiy-.  — >)  Die  Etymologie  bei  HoRN  NpEt.  109,  Hbh. PSt.  56  ist  falsch,  da  Avr.  ard -^^  mp-,  np.  il ist.  S.  auch  karüäspa.. j.  har^i  Yt.  to.  34 ;  lies  hatmrAii.
•  j.  'haradra-  n,  'Pflege,  Wartung,  Unter- halt": yai  nsit  'nm  baraiti  (sd.)  altaia aiSa  yS  ap>r2n3yBkö  ataityS.ar)har^%rfm (sd.)  irifyäl  V.  75.16;  17;  —  aitahmäyus (sd.)  paiti  'rtm  V,  75. 21,  42;  —  duye navaiti  astanqm  a%aityll.anAar»%ranqm däitim  ahmaiHt  'nm  k»r»»uyat  V.  14. 17;  —  vTspanqm  valqm  uxiatiqmca  .  , 'nm  frabarat  (soll  heissen)
KompE.;  Ableit.    —    Zum  V.  Aui-.    —    PQ. : sardärTh.
•  j.  "haraOra-  n.  'Borte,  Saum*  des Rocks:  yat..nsil  avatfrasayät{'sd.)  alairt
*'raHiyS'^  'a.85. Eig.  etwa  'was  (unten)  um  den  Rock  herum-
I  läuft,  ihn  abschHcSäl';  lum  ai.  V.  sätali.  — I       Pü. :  ka/alar  Aar  3  pärak.  —  i)  Hds.  'rahibyd.
'  •  j.  haraSra'vatit-  Adj.  (fem.  'vaitl-) I 'Pflege,  Obhut  gewährend":  fäää  'vaiSÜca ■  pakravailisca  Y.  55.  2'.
j       Pü. !  sardär  iräyiSn.
j  •  j.  haradräi  Inf  'zu  wachen  über  — ,  Acht Jzu  haben  auf  — ':  'rai  asahe  gaehanqm Y-55-3;  V.7y.39;  —  gae'iäica  tanvasiS  . . niiatahantayaicä  'räica  aiwyaxstraica  Y. 5Äa,  71.  11;  Yt.5.6.
Zum  V.  har-%  vgl.  har3%ra:—  Pü. :  smd^rlli, sarJär  (,  gehändär  V.  /J  statt  !;ehin  sardär).
•  j-  (i  S)  haurva-,  p.  haniva-  Adj.  (fem. 'va-")  'ganz';  i)  sva.  'unverletzt,  unversehrt, heil';  dad)mahl  haurvafsavS  .  .  drva  *va (NPm.)  ttüvants  Y.  iß.  6.  2)  sva.  'ge- sammt,  vollständig':  \pasava''  kar<^  °va* /iami'äi''iya^  abava^  Bh.  i.  1 1 ;  1 6 ;  —  °v<^- iim  kära''  avaint/"  Bh.  2, 13,  14;  II  —  'vqm handaitlm  staotanqm  yesnyanqm  Y. 
.ausfüllen,  complere':  >'aSa  iaha/a  dahmB staota  yesfiya  'va  *daoaiii  "wie  immer  ein
dby  Google
J79J
hanrvatät-
hanz-  I
179a
D.  die  St.'Y.  (komplet  macht  d.  L)  voll-l ständig  anfeagt"  N.J7'>; — ydti  caüca  ..I dahme..*'vä^  *räfnI{S^.  1519  m.)  daiat
P.J2.
KompA.;  Ablcit.  —  iL  särva-  Adj.,  np.  Aar; i.  noch  No.  1.  —  \g\. /rahatavam.  —  Po.: kamäi;  %.  noch  N».  3^  —  ■)  Vgl  mp.  kar- viip.  —  ')  Pfi, :  ^gÖH  , .  JiÄf  _y(ifH  hamVäk JaAet.  —  3,1  Hdt.  Aaunn.
•  j-,  g.  haurvatat-,  baurvlt-'>  £  'Gani- heil, Vollkommenheit, Wohlfahrt"' :/5  Äaii- "^anä ..  armrftataiftn  astmcä  *taibyS  däahä (Sp.  744)  ..  xsahnmi^^.  544  \L)cä  •vatäts  Y. J4. 1 ;  — yf  msi . .  vaocät  katiim  ma^rpm yim  'vatäiö  asahyä  attantiliai(^A.)cä  Y. ^t.  6.  a)  bes.  in  Doalverbiodung  mit atmnttttat-:  diidl  mdi  .  .  ammtätä  'vä/ä s/J
der  6.  Monatstaf:  'tätB  ra%iDS  S.  1.  6;  vgL 2. 6,  Y,  16.  j.  A  i)  als  Bezeichnung  fBr das  vonÄ  geschützte  Wasser;  nur  in  Dnal- verbisdung  mit  amtntaiiU-  (sva.  Pflanzen)^' : :^ar>'i2m  myaxdfm  'vaia  am^rftala  gäus huda  haom^mca  paraJiaomimca  Y.  &  i ; J.1,4.1,  6^.17, -aö.
*>  Der  Gottheit  H.  ist  du  jämmerliche  Mach- werk Yt.  4  gewidmet.  VgL  im  CbiigcD  Jn. GIrPh.  3.  638.
mp.  hania/at  (Transikr.),  np.  xurdäd  (all MonUsname;  GlrPb.  rb.67);  ai.  TgL  sörva- tälay-  f.  —  Pü.  (inj/,6):  kamik  ratcisn,  Sü.: tarfafraij'lHki  (lonil):  Aarvalat.  —  •>  Dnreh H^)IoL,  S  306.  —  »)  Die  TCrschiedcnen  Be- deatangea  sind  nicht  immer  xchorf  la  trenneo- —  3'  S  393-  —  *1S.ta  amirilaläl-  No.  6.  — S)  VgL  za  amttitatät-  No.
j.  haurva-paoirya-  Adj.  —  7  — :  tUrS paoirys  yaxamaide  . .  tisra  paoirya  . .  H/ra 'ya  . ,  tisrattam  'yanam  (soll  heissen)  "die erste  der  drei  ersten  CJäJs . .  die  beiden ersten  der  drei  ersten  Gdhäs  . .  alle  drei ersten  Gä^äs  . .  von  allen  drei  ersten ffaSss  . ."  Vr.  13. 3'».
Pu.:  kamSi/ralum.  —  ")  DST.  ZA.  /.  475-
•  j.  haurva-ßav-  Adj.  'des  Haustiere unversehrt  sind';  pairX . .  dadrmahf  'fsavö (NP.)  Y.5Ä6.
PiL:  ^karA  ramak.  —  0  In  den  Hds.  »teht ik  als  Ideogiamm  für  an  'jener';  an  der  Stelle des  Urtextes  war   aber  an  n  vielmehr  har  in
•  j.,  g.  haurvSt-  f.:  s.  unter  haurvatät-.
•  j.  haurvo."päso  fralaostrs  naSrnS.- "paiwa  zardku/in>  N.  64.
A'  und  »'  ('gani-  . .  halb-')  sind  poss.Korop. mit  dem  nämlich«D  Schlassglied,  detsen  rich- tige Lesung  und  Bedeutung  nicht  la  ermitteln ist.     T  kaurvö.f<isä.  —  Pü.:  fehlt, j.,  g.  kaiirvis^i  s.  kaurvaläl: j.  kautvi  P.  33:  lies  kaurvi,  Sp.   179I   O.
•  j.  har^z-  V.  'entlassen'.  Praes.  J Aama-,  ^  hinza-,  1 7  (Ful.)  ^urj^a-",  14 kinzaya-,  27  htmya-,  —  PPfP.  'karsta-; Inf.  'harstayal-(a,  •harstSe,  'Airfzsm.
i)  'entlassen,  entsenden,  ausschicken': tä  (nämL  fravasayS)  htrjzntH  saiavaistm antarf  sam  asmammca  .  .  %rä%räi  Yt 13. 43.  '  a)  '(Wasser)  überlassen',  zur  Be- rieselung: mä^a  ..zqm  kärayin  (sd.)  mä  äpi> JarizayTn  yat  ahmt . .  V.  6'.  2 ;  a,  3.  s)  'mit Wasser    (usw.)    belassen,    benetzen':     s.
dby  Google
'harsia-.  2)  'an  seinem  Orte  belassen,,  la.         Undeutlich:  yä^a    dakmahe  fra-
liegen    lassen':    yezi   altim    iristpm    upa.-  nhanzdit  ii.ji''>{1).
b)r3'%wS.tarwt  (sd)  ava.zattan  ava  aitwt  ■  "'■  'ärjata^,  irjdli,  srjyäu  (Pass.).  j/-tffl*;  np, iristtm  baraym  ava^a  nmänim  h>may>n\  *'^'^'  ma.-V%.:  man,  (zu  N./5): /ö/övf. „  u-jT.  L-  'i^i    s-  noch  No.  2ff.    —    >)   GeeenOber  ai.
".  .  so  sollen  sie_  den  Toten  wegbringen,  .^aiffati.-')  Vh.-.  fa  an  i  hsm  {«})  parähim (und)  folglich  die  Behausung  belassen  |  n  pa /rahis»<'i  pa  raiJh  i  buland.  —  i)  HiiaXic^ (wo  sie  istj"  V.Ä2;3;  — yai,.matäa'  MurySjaoAa  Ata  JCavayb'saa; -v^.  Aaultn. yasna  upain  aitim  iristim  *avi.mam  kar>kS  \  ^-J"  3-  39-  —  <>  Pü.:  fehlt  -  s)  Pü  
seihen,  filtriren':  >4fl(.Ma«fl«ra  Aar-^/yflOT- ,  •  J-  ■»«"f  «««">  -^ar^^j««-  n.  O  Lassen, nanam    ysi    har>^ente'  rakwe    hr^zaitc^"^^^^-        a)  'Durchlassen,  Filtern'. „      j"  j  c,       j        rr  ■         j-  KompE.  ~  Zum  V.  kant-,  —  ai.  lajyaBo-n.,
"und  der  zu  filternden  ZTaöOTazwe ige,  die  j     1,^.  LW.  a/oror/j«  'divonio'. gefiltert  werden  sollen  für  ,."  Vr.  i2.  "" mit  aba:  s.  Inf.
mit  ava  'verzichten   auf  — ,  ablehnen': ,     „ avanhinzämi     *janySis     ünqm    (sd.)     Y. ' 10.  15,
•  j.  Aarsta-  Adj.  (fem.  'fä-),   PPfP.:   S.
ritayat-ca,  'AarftJe,  •hartStSe
```


## [2026-09-14T01:58:52.387Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hero",
 "prompt": "Give the full etymology of English \"hero\", including Greek ἥρως and any PIE root cited (e.g. *ser- \"to protect\" or *seh1- ), and note whether the connection with Latin servāre / Hera is accepted or disputed (Beekes?)."
}
```


## [2026-09-14T01:58:54.445Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%A5%CF%81%CF%89%CF%82",
 "prompt": "Full etymology of Ancient Greek ἥρως: what PIE root is proposed, what does Beekes say, is the link to Ἥρα and Latin servāre accepted or rejected?"
}
```


## [2026-09-14T01:58:55.625Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hero",
 "prompt": "Full etymology entry for \"hero\" — Greek heros, PIE root, relation to Latin servare and Hera."
}
```


## [2026-09-14T01:58:57.322Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/servo%23Latin",
 "prompt": "Etymology of Latin servō / servāre \"to keep, preserve\": what PIE root, what Avestan/Iranian cognates (haraiti, haurvaiti), and is it distinguished from servus?"
}
```


### [2026-09-14T01:58:58.180Z] TOOL RESULT

```
# Etymology of English "hero"

## Full Etymology Chain

According to the Wiktionary entry, English *hero* derives from:

**Middle English** *heroes* → **Old French** *heroes* → **Latin** *hērōs* → **Ancient Greek** *ἥρως* (hḗrōs, "demi-god, hero")

## Proto-Indo-European Root

The entry cites a possible PIE origin: *\*ser-* ("to watch over, protect"), noting this is potentially related to Latin *servo* ("protect").

## Important Caveat

The source states the PIE connection is uncertain: "possibly from Proto-Indo-European *\*ser-*" — the word "possibly" indicates this etymology remains speculative rather than definitively established.

## Note on Related Terms

The entry does not mention Hera or connections to *servāre* beyond the single reference to *servo*. The source also does not cite Beekes or discuss whether this PIE connection is disputed among contemporary etymologists. The reconstruction remains presented as a tentative proposal rather than consensus scholarship.
```


### [2026-09-14T01:58:59.935Z] TOOL RESULT

```
# Etymology of Ancient Greek ἥρως

**Beekes's Assessment:**
According to Beekes, the word is "probably from Pre-Greek," making the ultimate origin uncertain.

**Traditional PIE Root:**
Scholars historically proposed an original root "*ἡρωϝ-" (*hērōw-), comparing it with related Greek words like "πάτρως" and "μήτρως."

**Proposed Meaning and Connections:**
The reconstructed root was thought to mean "protector, defender," and scholars traditionally linked it to Latin "servō" (to protect, rescue) and Avestan "hauruuaiti" (to protect, defend).

**Status of These Connections:**
These etymological connections are **rejected**. Beekes explicitly states this theory "is not possible in view the lack of /w/ in Mycenaean Greek," where the word appears without the hypothesized /w/ sound.

**Link to Ἥρα:**
The connection to the goddess name Ἥρα remains mentioned but unresolved, listed as a comparison point rather than an established etymological relationship.
```


### [2026-09-14T01:59:01.457Z] TOOL RESULT

```
# Etymology of "Hero"

The word **hero** entered English in the late 14th century from Old French *heroe*, derived from Latin *heros* and Greek *hērōs*. 

## Original Meaning

The Greek origin remains uncertain, though scholars propose it may stem from a PIE root meaning "to protect." One theory suggests it originally meant "defender, protector," while others note it's "Probably a Pre-Greek word."

## Evolution of Meaning

In Homer's works, the term applied to Greek warriors at Troy. By classical mythology times (Hesiod, 8th century BCE), it referred to "man born from a god and a mortal," particularly those who served mankind.

The English sense shifted over time:
- **1660s**: "man who exhibits great bravery"
- **1690s**: "chief male character in a play, story, etc."
- **1713**: "Hero-worship" emerged in reference to ancient cults

## Secondary Meaning

A completely separate meaning developed in **1955** as a New York City term for a large sandwich (also called submarine, grinder, or hoagie). Its origin is unknown, possibly referencing the sandwich's impressive size.
```


### [2026-09-14T01:59:03.423Z] TOOL RESULT

```
# Etymology of Latin *servō*

Based on the Wiktionary entry, here's what's provided about the Latin verb *servō*:

## PIE Root

The source indicates the term derives from **Proto-Indo-European *ser-**, described as meaning "guard." The entry states: "Ultimately from Proto-Indo-European *[\*ser-](/wiki/Reconstruction:Proto-Indo-European/ser-#Proto-Indo-European:_guard)_."

## Distinction from *servus*

Yes, the entry distinguishes between the verb and noun. *Servō* is a denominative verb formed from the noun *servus* (slave/servant). The etymology explains: "By surface analysis, *servus* +‎ *-ō*."

According to Rix (cited in the source), the term may have originated from "an older noun *\*serwā* or *\*serwom*, both of which may have meant something akin to 'observation, heedance.'"

## Iranian Cognates

The provided text contains **no information** about Avestan or Iranian cognates like *haraiti* or *haurvaiti*. These comparisons are not discussed in this Wiktionary entry.
```


## [2026-09-14T01:59:15.138Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ser-",
 "prompt": "List all the PIE roots *ser- given on this page (guard/protect; to line up/bind; to flow), their glosses, and the descendants listed for each (Latin, Greek, Avestan, Sanskrit)."
}
```


## [2026-09-14T01:59:17.845Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%A9%CF%81%CE%B1%CE%BA%CE%BB%E1%BF%86%CF%82",
 "prompt": "Etymology of Ancient Greek Ἡρακλῆς (Heracles): is it Ἥρα + κλέος \"glory of Hera\"? What does the entry say about Ἥρα's own etymology?"
}
```


## [2026-09-14T01:59:19.138Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/series",
 "prompt": "Etymology of English \"series\" and Latin series/serō — which PIE root, and what cognates (Sanskrit sarat-, Greek eirein) are given?"
}
```


## [2026-09-14T01:59:20.275Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sort",
 "prompt": "Etymology of \"sort\" and Latin sors/sortis — PIE root and relation to serere \"to line up, arrange\". Also mention sorcerer if present."
}
```


### [2026-09-14T01:59:20.603Z] TOOL RESULT

```
# Proto-Indo-European *ser- Roots

The page documents four distinct PIE roots with the form *ser-:

## Root 1: "to flow"
- **Gloss:** "to flow"
- **Key descendants:** Latin *serum* ("serum, whey"); Ancient Greek *orós* ("serum, whey"); Sanskrit *sarít* ("river, stream")

## Root 2: "to guard"
- **Gloss:** "to guard, take care"
- **Key descendants:** Proto-Italic *serwos*; Proto-Slavic *sьrbъ*

## Root 3: "to bind"
- **Gloss:** "to bind, tie together; thread"
- **Key descendants:** Latin *sermo* ("discourse") and *sors* ("lot"); Ancient Greek *eírō* ("I say"); Sanskrit *sarat*; Armenian *orm* ("chain")

## Root 4: "to take/seize"
- **Gloss:** "to take, grasp, seize; steal, plunder; booty"
- **Key descendants:** Ancient Greek *hairéō* ("I take"); Latvian *sirt* ("to loot"); Hittite *sāru* ("booty, plunder"); Proto-Celtic *serwā* ("theft, plundering")
```


### [2026-09-14T01:59:22.025Z] TOOL RESULT

```
# Etymology of Ἡρακλῆς

Based on the Wiktionary entry, the Ancient Greek name **Ἡρακλῆς** (Heracles) derives from a compound: **"From Ἥρᾱ (Hḗrā, 'Hera') +‎ -κλῆς (-klês, 'glory')"**

The second component refers to glory or renown, making the name essentially mean "glory of Hera" or similar.

However, regarding Hera's own etymology, the entry provides **no information**. The page only documents the etymology of Heracles itself and does not trace the origins of the goddess Hera's name. To find that etymological detail, you would need to consult the separate Wiktionary entry for Ἥρα.
```


### [2026-09-14T01:59:24.292Z] TOOL RESULT

```
# Etymology of "Series"

## PIE Root

According to the etymology section, English "series" traces back to the Proto-Indo-European root **\*ser-** meaning "to bind, put together, to line up."

## Etymology Chain

The word follows this path:
- PIE **\*ser-** ("to bind")
- Proto-Italic **\*serō**
- Latin **serere** ("to join together, bind")
- Latin **seriēs** (with the suffix **-iēs**)
- English **series** (borrowed from Latin, attested from the 1610s)

## Related Cognates

The entry identifies these English relatives of the same root: "desert," "insert," "sermon," and "sorcerer."

## Sanskrit and Greek

The page does **not** mention Sanskrit *sarat-* or Greek *eirein* as cognates. These potential connections to the PIE root are absent from the provided content.
```


### [2026-09-14T01:59:25.446Z] TOOL RESULT

```
# Etymology of "Sort"

## Origin and Development

The word "sort" descends from Old French *sorte*, ultimately tracing to Latin *sortem* (nominative *sors*), meaning "lot; fate, destiny; share, portion; rank, category." The term evolved through Vulgar Latin from "what is allotted to one by fate" to "fortune, condition" and finally to "rank, class, order."

## PIE Root Connection

The Latin *sors* stems from the Proto-Indo-European root **\*ser-** (2), which signifies "to line up" or arrange in sequence. This foundational sense helps explain how the word developed its meaning related to classification and ordering.

## Related Terms

Several English words share this etymological heritage:

- **Assort**: "to distribute into groups or classes" (late 15c.)
- **Consort**: originally "partner" or "colleague," later referring to a spouse
- **Sorcery**: derived from Medieval Latin *sortiarius*, literally "one who tells fortunes by lot"

The computing sense referring to "arranging data in sequence" emerged around 1958, representing a modern application of the ancient classification concept.
```


## [2026-09-14T01:59:36.949Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%87%D8%A7%D8%B1/",
 "prompt": "Give the Dehkhoda (لغتنامه دهخدا) and Mo'in (فرهنگ معین) entries for Persian هار. List all senses. Is there a sense \"گردن، رشتهٔ مروارید، افسار/عنان\" (neck, necklace, rein)? Quote the Ferdowsi shahed verses given."
}
```


## [2026-09-14T01:59:38.666Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%86%D8%B3%D8%B1%D9%88/",
 "prompt": "Give the Dehkhoda and Mo'in entries for Persian کنسرو — what origin is given (French conserve)?"
}
```


## [2026-09-14T01:59:39.840Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%B1",
 "prompt": "What Persian entries exist for هار? Give etymologies and meanings for each."
}
```


## [2026-09-14T01:59:41.804Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B9%E0%A4%BE%E0%A4%B0",
 "prompt": "Sanskrit हार (hāra): meaning and etymology — from which root (hṛ / *ǵʰer-?) is it derived?"
}
```


### [2026-09-14T01:59:43.146Z] TOOL RESULT

```
# Origin of کنسرو

According to the dictionary entries provided:

**Dehkhoda**: States the word is "کُ سِرْوْ" with origin noted as "فرانسوی" (French), describing it as "ماده خوراکی که آن را به صورت استریلیزه در قوطی یا محفظه ای کاملاً مسدود نگهداری کنند" (a food item kept sterilized in sealed containers).

**Mo'in**: Lists it as "[فر.]" indicating French origin, defining it as "غذای آماده که در قوطی سربسته و فاقد هوا نگه داری می شود" (prepared food stored in airtight sealed cans).

Both entries confirm the word derives from French, relating to the concept of preserved/canned food products.
```


### [2026-09-14T01:59:44.332Z] TOOL RESULT

```
# Persian Entries for هار

The Wiktionary page lists two Persian entries for this word:

## Etymology 1: Adjective
**هار** (hâr) means "rabid." No further etymological information is provided for this sense.

## Etymology 2: Noun
**هار** (hâr) is an archaic noun meaning "string (of beads or pearls)."

This entry was "borrowed from Hindi हार (hār), from Sanskrit हारि (hāri)." The page notes that supporting quotations for this archaic usage are still needed.
```


### [2026-09-14T01:59:45.149Z] TOOL RESULT

```
# Persian Dictionary Entry for هار

## Dehkhoda (لغتنامه دهخدا)

The Dehkhoda entry lists multiple senses:

1. **Pearl necklace/ornament**: "رشته مروارید بود" (a string of pearls)
2. **Necklace/jeweled collar**: "گردن بند" and "گردن بند جواهر"
3. **String/chain**: "رشته" and "سلک"
4. **Neck**: Referenced in classical poetry contexts

Yes, the sense "گردن، رشتهٔ مروارید" (neck, pearl necklace) is clearly present.

**Ferdowsi verse cited**:
"از آن قبل را کردند هار مروارید / که درّ ضایع بودی اگر نبودی هار"
(They made a pearl necklace from it / so pearls wouldn't be wasted without the string)

## Mo'in (فرهنگ معین)

This entry focuses on different meanings:

1. **Rabid dog**: "سگ گزنده که گرفتار بیماری هاری باشد"
2. **Carnivorous animal** (generally)
3. **Foul/decaying meat**: "گوشت گندیده و بدبوی"
4. **Feces**: "فضلة انسان و حیوان"

The ornamental sense does not appear in Mo'in's entry.
```


### [2026-09-14T01:59:46.397Z] TOOL RESULT

```
# Sanskrit हार (hāra) Etymology

Based on the Wiktionary entry, **हार (hāra)** derives from the Sanskrit root **हृ (hṛ)**, meaning "to take."

According to the etymology tree presented, हार is "a vṛddhi derivative of हर (hara, 'bearing, taking')." The term ultimately traces back to the root हृ, which carries the semantic domain of taking, bearing, or removal.

The word developed multiple related meanings:
- As an adjective: "bearing, carrying, carrying away, stealing"
- As a noun: "taking away, removal, confiscation, waste, loss"

This Sanskrit root is ancient and may connect to Indo-European *ǵʰer- (to grasp), though the Wiktionary source provided doesn't explicitly confirm this deeper reconstruction.
```


## [2026-09-14T02:00:22.213Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"haraiti\\|haurvaiti\\|hauruua\" WLD_Bd2_pages.txt | head -10; echo \"=== sarat\"; grep -n \"sarat-\\|sarat \" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T02:00:22.286Z] TOOL RESULT

```
33104:                              schiitzt''; haurvaiti ds., haurva- „beschutzend,
=== sarat
33206:   Ai. sarat- ,,Faden"                  (unbelegt),        vielleicht sata .,Mahne, Borste" (Uhlen-
```


## [2026-09-14T02:00:23.153Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^series,\\|^sort,\\|^hero,\" SKT.txt | head; echo \"=== SKT hero\"; grep -n \"hero\" SKT.txt | head -5"
}
```


### [2026-09-14T02:00:23.222Z] TOOL RESULT

```
=== SKT hero
6284:perjidus^  tieacherous.  —  L.  ptr^  away  (cf. Skt.  /orj,  from)  ;  Jidts^  fnitK.
8509:ft  ballr.  CC^k.)  From  Gk.  ff*£tor, oelcbraied  hero  of  Troy.     Lit. &t ; '  bom  ix""'  ^  hold. sec  Haw.
8627:Hero.  (F.-L.-Gk.)  O.F.  4«nV.  -L. heroim,  flcc.  of  hercs,  a  hero.  —  Gk.  J$/wr,  a hero,  denii  gtnl.  +  Sit.  vt'ra,  a  hero^  L, uir;  AS  wer.  Allieil  to  VirilO.  Der. hero-ie,  O.  F.  lurvique^  L.  kertncus,
8628:heroine.  ^F— L.  — Gk)  F.  her^me, L.  heroine,  "(ji^'  ifputvfit  fcm.  of  ^pon,  a hero.
8629:Heron,  Hern,  a  bird.  (F.-O.H.G.) M  E.  kerouH,  AairOM,  hern.^O.  F.  hairoH (F.  h/mn,  Ital.  a^'hirone').  -  O.  H.  G. heigir,  heiger,  a  heron;  with  aufiixcd  •«! ^Iial.  'One\,  I'rob.  named  from  its  harsh voice ;  cf.  G.  hiikrr,  a  jack-daw  (lit. 'laugher'),  prov.  E.  kei^haw,  a  wood- pecker, Skt.  htkk,  (o  laugh.  (V  KAK.) 4^  Swcd.  h^grr,  Icel.  ke^,  Dan.  keirt^  a heron.
```


## [2026-09-14T02:00:30.940Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'NR<=33104 && /\\[pdf page [0-9]+\\]/ {p=$0} NR==33104{print \"line33104 page:\",p}' WLD_Bd2_pages.txt; awk 'NR<=33206 && /\\[pdf page [0-9]+\\]/ {p=$0} NR==33206{print \"line33206 page:\",p}' WLD_Bd2_pages.txt; echo \"--- ctx 33095-33115\"; sed -n '33095,33115p' WLD_Bd2_pages.txt; echo \"--- ctx 33195-33215\"; sed -n '33195,33215p' WLD_Bd2_pages.txt"
}
```


### [2026-09-14T02:00:32.495Z] TOOL RESULT

```
line33104 page: 
line33206 page: 
--- ctx 33095-33115

auf, 0 QjLnj‘^ mit der Bed.-Entw. zu ,,in seine Gewalt bekommen, kriegen“
anzureihen.
   Curtius Gdr. ^ 349, FickI ^ 140, 562, II ^ 291, Prellwitz ^ 336 f., Yf. LEWb.^
704 f.       —   S.   auch sreu-      „flie6en‘\


3.    ser- „sorgend Obacht geben, schiitzen, bewahren“.
      Av.     Jiaraiti    „hat acht,
                              schiitzt''; haurvaiti ds., haurva- „beschutzend,
hiitend'"        in          spa „das Eleinvieh, die Schafe beschiitzender
                      pasus-Jiaurvo
Hund, Schaferhund^* (wie lat. servus, servo von einer «i-Erw., vgl. Persson
Beitr. 563, Brugmann II ^ 3, 270 f.; sie wird wegen fjgcog, St.          nicht
aus einem -^o-St. "^ser-tio- herzuleiten sein); hardtar- „wer woriiber wacht,
darauf achthat^, haro&ra- „Pflege, Wartung, Unterhalt“; hara- „acht-
habend, hutend“, red. hisara- ds. lat. semis „Sklave'', ursprgl. „IIuter,
                                                   ;



--- ctx 33195-33215
Farbei'kraut, Serratula tinctoria'', sirpstu, sirpan, sirpti                                     ,,reif   werden^' (nur
von Beeren und             Steinfriichten,              also oder rotlich werden“j am
                                                                    eig. ,,gelb
beachtenswertesten             ;
                                    weniger einleuchtend hingegen die von arm. erp^n
..Parbe, Aussehen, Gestalt'', arp"" ..licht", „die Sterne", arpH „lichter
Ather, Himmel" (um derentwillen auch das p von lit. serpes als idg, ph
bestimmt wird).


4. ser-     „aneinander reihen. kniipfen".
   Ai. sarat- ,,Faden"                  (unbelegt),        vielleicht sata .,Mahne, Borste" (Uhlen-
beck Ai.Wb. s. v.j;
   gr.   eiQCo       aneinander" (horn, nur ppp. ieQpevog^ 3. sg. plqupf.
                 „reihe
hgTo)^          „knupfe an. reihe an" (: lat. in-sero ,,fuge ein"), evegoig
          ivetocjo

„das Hineinfiigen, Hineinstecken" (: leit insert to; tiSt. auch in prae-sertim
,,in erster Reihe, vorzugsweise"), egjua „Ohrgehange", ogpog „Halskette",
```


## [2026-09-14T02:00:40.782Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'NR<=33210 {if(/pdf page/) p=$0} END{}' WLD_Bd2_pages.txt; grep -n \"pdf page\" WLD_Bd2_pages.txt | head -3; echo \"---\"; awk 'NR>=33050 && NR<=33230 && /pdf page|^ *[45][0-9][0-9] *$|^[45][0-9][0-9]/ {print NR\": \"$0}' WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T02:00:42.010Z] TOOL RESULT

```
---
33079: 498                                                    ser-
```


## [2026-09-14T02:00:48.982Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%B1%DB%8C%D8%A7%D9%84/",
 "prompt": "Persian سریال and سری: what origin do Dehkhoda/Mo'in give (French sérial / série, or English serial)? Quote the origin tag."
}
```


## [2026-09-14T02:00:51.104Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%87%D8%B1%DA%A9%D9%88%D9%84/",
 "prompt": "Persian هرکول: what do Dehkhoda / Mo'in (فرهنگ اعلام) say — origin French Hercule / Greek Herakles, and meaning?"
}
```


## [2026-09-14T02:00:52.708Z] TOOL CALL #45: WebSearch

```json
{
 "query": "شاهنامه فردوسی \"آهخته هار\" \"گزیده سواران\""
}
```


### [2026-09-14T02:00:54.227Z] TOOL RESULT

```
# Etymology of سریال

Based on the content provided, the page does not include explicit origin tags from Dehkhoda or Mo'in dictionaries specifying whether the word derives from French or English sources.

However, the user suggestions section contains this relevant statement:

"واژه سریال فرانسوی است" (The word سریال is French)

A user also notes: "واژه سریال فرانسوی بوده که از واژه «سرره»در زبان لاتین و به معنای پیوستن و به صف کردن, و زنجیره گرفته شده" 

This indicates users attribute the term to French origins, derived from Latin *serre* (meaning connection or chaining), ultimately tracing to Sanskrit *ser*.

The formal dictionary sections (Dehkhoda, Mo'in, Amid) visible here do not explicitly cite origin sources with tags.
```


## [2026-09-14T02:00:54.402Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Alborz",
 "prompt": "Etymology of Alborz / Avestan Harā Bərəzaitī: what does Harā mean and from what root is it derived (har- \"to watch/guard\" or something else)?"
}
```


### [2026-09-14T02:00:57.267Z] TOOL RESULT

```
# هرکول (Hercules) - Etymology and Meaning

Based on the dictionary content provided:

## Origin
The term هرکول is the Persian rendering of the Latin **Hercules**, which itself derives from the Greek **Heracles** (هراکلس).

## Primary Meanings

According to Dehkhoda Dictionary:
- "نام رومی هراکلس قهرمان افسانه های ادبیات یونان و رم" — the Roman name for the Greek legendary hero of Greek and Roman literature

## Dictionary Definitions

**Mo'in Dictionary** describes it as:
- "رب النوع قدرت و نیرو در افسانه های یونان" — a mythological embodiment of power and strength in Greek legends

**Amid Dictionary** provides two meanings:
1. A strong man; hero (colloquial/figurative)
2. An astronomical constellation in the northern hemisphere

The term broadly represents "masculine prowess and heroic strength," referencing the legendary figure who became one of the gods after his mortal death.
```


### [2026-09-14T02:00:58.660Z] TOOL RESULT

```
# Etymology of Alborz

Based on the Wiktionary content provided, the entry shows that Alborz derives from Persian _alborz_, with an Avestan cognate listed as **harā.bərəzaitī**. However, the document does not explain the meaning of the Avestan component "harā" or identify its root etymology.

The page only notes that Alborz is a "Doublet of _Elbrus_" and references a Persian entry for further details, but those etymological specifics about the Avestan root (whether from "har-" meaning "to watch/guard" or another source) are not included in this particular Wiktionary entry.

To answer your question about Harā's meaning and derivation, you would need to consult the Persian entry or specialized historical linguistics sources on Avestan, which fall outside the scope of this webpage.
```


### [2026-09-14T02:00:59.635Z] TOOL RESULT

```
Web search results for query: "شاهنامه فردوسی "آهخته هار" "گزیده سواران""

Links: [{"title":"گنجور » فردوسی » شاهنامه","url":"https://ganjoor.net/ferdousi/shahname"},{"title":"گنجور » فردوسی » شاهنامه » داستان سیاوش » بخش ۱۰","url":"https://ganjoor.net/ferdousi/shahname/siavosh/sh10"},{"title":"معنی اخته زهار در شاهنامه | اسطوره ها و افسانه ها","url":"https://myth.tarikhema.org/article-4777/%D9%85%D8%B9%D9%86%DB%8C-%D8%A7%D8%AE%D8%AA%D9%87-%D8%B2%D9%87%D8%A7%D8%B1-%D8%AF%D8%B1-%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87"},{"title":"شاهنامه فردوسی","url":"https://shahname-ferdosi.blogfa.com/"},{"title":"گزیده بهترین اشعار فردوسی+ 50 شعر در مورد ایران، ادب و دانش","url":"https://payamedalat.com/%D8%A8%D9%87%D8%AA%D8%B1%DB%8C%D9%86-%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C/"},{"title":"گزیده ای از اشعار فردوسی","url":"https://www.beytoote.com/art/song/selection-poems-ferdowsi.html"},{"title":"اشعار شاهنامه فردوسی | گلچینی از شعرهای حکیم ابوالقاسم فردوسی","url":"https://www.talab.org/art/poetry/%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C.html"},{"title":"اشعار شاهنامه فردوسی + گزیده اشعار فردوسی با موضوعات مختلف","url":"https://roozaneh.net/fun/sms/%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C/"}]

I've completed a web search for your query in Persian about Ferdowsi's Shahnameh (شاهنامه فردوسی) with the terms "آهخته هار" and "گزیده سواران". 

The search results returned information about Ferdowsi's Shahnameh in general, including:

- The Shahnameh is Ferdowsi's most renowned work and one of the greatest writings of ancient Persian literature
- Ferdowsi completed the Shahnameh in 384 AH, three years before Muhammad of Ghazni became king, and produced a second edition in 400 AH at age seventy-one
- Information about various famous stories from the Shahnameh, including romantic tales

However, the search results don't contain specific detailed information about the particular passages you're looking for ("آهخته هار" and "گزیده سواران"). If you're looking for more specific information about these particular sections or passages from the Shahnameh, you might want to check specialized Persian literature resources or the Ganjoor website (ganjoor.net), which appears to be a comprehensive digital library of Persian poetry and literature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:01:04.793Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/alborz-index/",
 "prompt": "What is the etymology of Alborz / Avestan Harā Bərəzaitī given here? What does Harā mean and from what root?"
}
```


### [2026-09-14T02:01:06.034Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:01:06.977Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://vajehyab.com/dehkhoda/%D9%87%D8%A7%D8%B1",
 "prompt": "Give the full Dehkhoda entry for هار, all senses and shahed verses; especially any sense \"گردن\" (neck) or \"رشته مروارید\" and the Ferdowsi verse containing \"آهخته هار\"."
}
```


## [2026-09-14T02:01:07.745Z] TOOL CALL #49: WebSearch

```json
{
 "query": "\"هار\" دهخدا \"گردن بند\" فردوسی \"بر آن بادپایان\""
}
```


### [2026-09-14T02:01:13.258Z] TOOL RESULT

```
# Dehkhoda Entry for هار (Hār)

## Primary Senses

**1. Pearl Necklace/String of Pearls**
From Sanskrit "hāre" (pearl, pearl bracelet, necklace), the term denotes "a string of pearls" specifically, or more generally, "anything arranged in sequence."

**2. Neck**
Listed as a standalone meaning with multiple source citations (Burhan, Jahan­giri, Anan­daraj).

**3. Neck Vertebrae**
Described as "the vertebral bones of any animal's neck" or "cervical bones."

**4. Camel Halter**
Some sources interpret it as a camel's bridle or lead rope.

**5. Mad Animal (especially rabid dog)**
An animal afflicted with madness, particularly a rabid dog that transmits disease to humans, causing them to fear water and experience strange symptoms.

**6. Putrid Meat**
Rotten, foul-smelling flesh.

**7. Excrement**
Human or animal waste matter.

## Ferdowsi Verses

The entry includes two similar Ferdowsi couplets containing "آهخته هار" (swift-necked):

*"From the cavalry, he chose one thousand / Upon those wind-swift ones, [he rode with] swift neck."*

Both verses illustrate the neck sense of the term.
```


### [2026-09-14T02:01:14.978Z] TOOL RESULT

```
Web search results for query: ""هار" دهخدا "گردن بند" فردوسی "بر آن بادپایان""

Links: [{"title":"گنجور » فردوسی » شاهنامه » پادشاهی کیخسرو شصت سال بود » بخش ۳","url":"https://ganjoor.net/ferdousi/shahname/kkhosro/sh3"},{"title":"گنجور » فردوسی » شاهنامه » داستان رستم و اسفندیار » بخش ۱۸","url":"https://ganjoor.net/ferdousi/shahname/esfandyar/sh18"},{"title":"گنجور » فردوسی » شاهنامه » سهراب » بخش ۱۳","url":"https://ganjoor.net/ferdousi/shahname/sohrab/sh13"},{"title":"گنجور » فردوسی » شاهنامه » سهراب » بخش ۱۵","url":"https://ganjoor.net/ferdousi/shahname/sohrab/sh15"},{"title":"گنجور » فردوسی » هجونامه (منتسب)","url":"https://ganjoor.net/ferdousi/hajvname"},{"title":"معنی هار | لغت‌نامه دهخدا","url":"https://www.vajehyab.com/dehkhoda/%D9%87%D8%A7%D8%B1"},{"title":"فردوسی - دکتر حسین الهی قمشه ای","url":"https://www.drelahighomshei.com/%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C"},{"title":"گنجور » فردوسی » شاهنامه » ضحاک » بخش ۱۲ - بند کردن فریدون، ضحاک را","url":"https://ganjoor.vercel.app/ferdousi/shahname/zahak/sh12"},{"title":"اشعار شاهنامه فردوسی + گزیده اشعار فردوسی با موضوعات مختلف","url":"https://roozaneh.net/fun/sms/%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C/"}]

I've performed the web search for your query. The search results show references to Persian literature and the Shahnameh (Book of Kings) by Ferdowsi, which contains content related to your search terms. The results include:

1. References from Ganjoor (a Persian poetry repository) showing passages from Ferdowsi's Shahnameh
2. Content mentioning "گردن بند" (necklace/collar) and related terms
3. References to Dehkhoda dictionary entries for the word "هار" (necklace)
4. Passages from Ferdowsi's works discussing various characters and events

The search results primarily come from:
- **Ganjoor.net** - A comprehensive Persian poetry database with Shahnameh texts
- **Vajehyab.com** - The Dehkhoda Dictionary (لغتنامه دهخدا)
- **Dr. Elahi Qomshei's website** - Featuring Ferdowsi texts

These sources contain the Persian literary material you were searching for, particularly related to Ferdowsi's works and Persian classical poetry references to items like "هار" (haar/necklace) and "گردن بند" (gardan-band/necklace), with supporting dictionary references from the Dehkhoda Dictionary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:01:25.281Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BQT v4 هار\"; grep -n \"هار \\[\\|هار(\\|(هار)\\|گردن بند\\|رشته مروارید\" incoming/BQT/BQT_v4_pages.txt | head -20"
}
```


### [2026-09-14T02:01:25.345Z] TOOL RESULT

```
== BQT v4 هار
5246:پاشد و در دوا ها بکار وش و بر سر های دست وگردن بندند و صربان خرز
15687:-قی : ساسکریت 8878 ( مروارید , حلقةٌ مروارید , کگردن بند ) « ودلیامز
15736:و مرض آن سکه را «هاری» نامند .کردی 32۳ «عار » دارندة سرنام ) ؛ ۳ 81807 (هار) ؛
15770:۱ از : هار(ه.م.) ی (سبت و اتصاف) - نیزهاری » از : هار (دیوانه) + ی(حاصل
```


## [2026-09-14T02:01:28.110Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== MON کنسرو\"; grep -n \"کنسرو\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -5; echo \"== MON هرکول\"; grep -n \"هرکول\" MON_part*.txt incoming/MON/*djvu.txt 2>/dev/null | head -5; echo \"== MON سریال\"; grep -n \"سریال\" MON_part*.txt incoming/MON/*djvu.txt 2>/dev/null | head -5; echo \"== HRN hār\"; grep -n \"gardanband\\|Halskette\" HRN.txt | head -10"
}
```


### [2026-09-14T02:01:28.243Z] TOOL RESULT

```
== MON کنسرو
incoming/MON/MON_2vol_Adena_v2_djvu.txt:27198:کنسرو: ۷ (- کو نسرو ] (.) ماده‌ای 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:27201:کنسرواتوار: ۲ (.) مدرسه‌ای 
MON_part1.txt:71780:پرورده: سربای زنجبیل» کنسرو زنجییل. 
MON_part1.txt:73718:مزیور را جهت تغذیه و ساختن کنسرو صید 
MON_part2.txt:27198:کنسرو: ۷ (- کو نسرو ] (.) ماده‌ای 
== MON هرکول
== MON سریال
MON_part1.txt:76412:سریالا: 0218.: [- سرا بالا] (ص‌مر.) آنچه 
MON_part1.txt:77696:سریال: ۱021 (ص.) مطلبی که جزء به 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:76412:سریالا: 0218.: [- سرا بالا] (ص‌مر.) آنچه 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:77696:سریال: ۱021 (ص.) مطلبی که جزء به 
== HRN hār
```


## [2026-09-14T02:01:33.623Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15660,15700p' incoming/BQT/BQT_v4_pages.txt; echo \"=== page tag\"; awk 'NR<=15687 && /\\[pdf page/ {p=$0; n=NR} END{print p\" at line \"n}' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-14T02:01:34.692Z] TOOL RESULT

```
مردم بی‌سرو پا را گوبند که چوب‌داران وباولان | باشد با پروبالاو پهلوی هم درآرند9 -ومروازرید
سلاطین ابشان را ازسرراه دور کنند . و لعل و باقوت سفته و امثال آنرا کوبن د که در
هادی - بروزن خادی,نام ستنگی‌است. | یکرشت ه کشیده شده‌باشد خصوساً 8 -وکردن۹ -
گوبند هر که‌آن سنگه را باخود دارد سکه باو | و مغره‌های گردن حبوانات را نیز گفته‌اند 8 -
قرباد نکند - وبعربی هدایت کننده وراء‌نمایند. | و فثله و افکندکی اسان و حیوانات دیگی را
وآرام کیرنده و پیکان تیرراکوبند ۴ . هم میگویند ۷ - و بمشی متخیر و درمانده

۱ - 884071 (کدایان ) از فات مأٌخوذ ازآرامی است « اسفا ۲:۱ ص ‎٩‏ :

دعوی ده‌کنند ولیکن چو بنگری هادوربان کوی و کدایان خرهنند .

منالی غزنوی . دیوان ص ۱۵۰ .۰

معیشتی نه‌که با عزت قناعت آن بهر دری لروم چو ن کدای هادوری +

انیرالین اخپکنی* جهانگیری *.
رك : هادوریان .

۴ - جمع «هادوری» (.م.) ۴ - (عر) « هادی ؛ راه نما وییشوا وکردن‌خوادی
جمع - و پیکان تیر وکاوی که در مر‌کز خرمن کوبی است وشیر بیشه واول از شب و اول کل
شتران پیش رو که نمایان شود . خوادی جمع » « منتهی الارب > +

۴ - مخون از شمر خاقالی شروالی : ۰

گرچه همه دلکنند. ازهم هکل نفزتر ‏ کومرقءصطفاست.وان دگران‌خاك وآب
هادی مهدی غلام » امی سادق کلام خروهنتم بهشت . شحنةٌ چارم کناب +
دبوان خاقالی ص 244 * -
-قی : ساسکریت 8878 ( مروارید , حلقةٌ مروارید , کگردن بند ) « ودلیامز
۹ ازريشةٌ 872 ( بردن » پوشیدن »گرفتن ) « ایطاً ۱:۱۲۸۹ ؛ بشتو 82۸۲ (کردن
بند , حلقه ) ۸« بلیو س ۱۷۹ « هار , رشتهٌ مروارید بود. شم 5"
از آن قبل را کردند هار مروارید که در ضایم بودی اگر نبودی هار.»
« لغت فری ص ۴۱۹-۱۵۹ * صحاح‌الفری » نمض طاعتی : ار >
رك : یکدانه : # ولسخت تذ کره هدبه‌ها, چه هدیه‌هایی که اول‌روزییش خان روند وچه‌هدیه‌های
عقد تزویج» کردند سخت بسیار وبرسم » وآن دوجام زرین مرصع بجواهر بود با هارهای‌مروارید»
و جامه‌های بزر ... » « تاریخ بیپقی . مصحح دکتر فیاض ص ۲۲۰ .
‎٩‏ -کزید از سواران برون از شمار بر آن باد پایان آهخته هار ,
فردوسی طوسی « فرهنگه اظام >.
۷ - صورت بغل‌آنکه زر دار است تیز با هار وکون با هار است.
سنائی غزلوی .
ترش بچهره ودنداش چون تراشةٌ ار کره بروی و میان پاش پر گروهةٌ خار.
مختاری غزنوي « فرهنگه نام >.
=== page tag
[pdf page 388] at line 15653
```


## [2026-09-14T02:01:58.263Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(d.get('page_offset'));print(d.get('scans'))\n\" 2>&1 | head -20"
}
```


## [2026-09-14T02:01:59.096Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15640,15660p' incoming/BQT/BQT_v4_pages.txt | head -25"
}
```


### [2026-09-14T02:01:59.302Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
```


### [2026-09-14T02:01:59.365Z] TOOL RESULT

```
۰ 80۳2
چندی بعد دارمستتر درجزوترجمهٌ زند اوستای خود , هادخت سك را دیز ترجمه کرده‌است. رك:
8۰ - 646 .۶ ,]|۷۵ 08706816167۰ کقص ۸۷۵۵۸۵ - 2۸00 ما
تضیرپهلوی هادخت سك دارای ۱۵۳۰ کلمه است. درکتاب هشتم ولهم دیشکرد که ازآوستا خن
رفته , و اجزای‌آن بكايك شرح داده شده , هادخت سك بیستمین سك (کناب) اوستا بشماررفته
است . بنابرین هادخت سك حالیه قطمه ایست که از بیستمین سك کم شدء عهد ساسانیان بجای
مانده‌أست . علاوه برآن سروش بشت هادخت که امروزه بازدهمین پشت اوستا را تشکیل‌میدهد: از
عادخت‌سك قدیم بیادگار مانده است. هادخت سك کنونی دارای۳ فر کرد (فصل) است:فر گرداول
دارای ۱۷بند در فضیلت وتأئیر دعای « اشم وهو...» » فن کرد دوم راجع به تجسم دین ( وجدان)
مرد لیگوکار صورت دختری زیبا ( این قطعه بیار دلکش و قابل توجه است ) ۰ فن‌کرد سوم از
مجم شدن دی ن گناهکار جصورت زلی‌زشت گفتگومیکند . رد : پورداود . پشتها؟صس ۹۱۷۳-۱۹۵
پورداود . سنا ص۳۱ ؛ م . معین . حکمت اشراق س 4۱-۳۷ .. ۰
[pdf page 388]
سنه هار
هادوری ۱ - بن‌ناكك‌بروزنلاهوری, هادی مهدی غلام « اشارمییرور

لوعی از کدایان باشند در نهایت سماجت. کاینات محمد سلوات‌للط علیه وآله است ۴ ۰
هادوریان ؟ - بروزنلاهوریان جیع هار - بروزن مار » هرچیزی راگویند
هادوری‌است که کدابان مبرم باشند -ونیزجماعت |" عموماً که از پی‌هم بتوالی یعنی یی درهی درآمده
مردم بی‌سرو پا را گوبند که چوب‌داران وباولان | باشد با پروبالاو پهلوی هم درآرند9 -ومروازرید
```


## [2026-09-14T02:02:05.251Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '77696,77698p' MON_part1.txt; echo \"---سری\"; grep -n \"^سری:\" MON_part1.txt | head -3; echo \"---\"; sed -n '27196,27202p' MON_part2.txt"
}
```


### [2026-09-14T02:02:05.369Z] TOOL RESULT

```
سریال: ۱021 (ص.) مطلبی که جزء به 
جز و انتشار بابد) مسلسل. 

---سری
77679:سری: -۰27 (حامص.) سروری» ریاست. 
77682:سری: ۰۵7-1 (ص‌نسب.) منسوب به سر. آلتی 
77693:سری: آ-6۲۲ع8 [غ. آف.] (ص‌نست.) منسوب به 
---
مات ان تشعیل شو د. 

کنسرو: ۷ (- کو نسرو ] (.) ماده‌ای 
خوراکی که آن را بصورت استریلیزه در 
توطی يا محفظه‌ای کاملاً مسدود نگهداری 
کنسرواتوار: ۲ (.) مدرسه‌ای 
که در آنجا موسیقی تأتر و هنرهای نمایش را
```


## [2026-09-14T02:02:10.620Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '77690,77700p' MON_part1.txt"
}
```


### [2026-09-14T02:02:10.855Z] TOOL RESULT

```
ردیف» طبقه. . ضح. احتراز از استعمال این 
کلمه بیگانه اولی است؛. 

سری: آ-6۲۲ع8 [غ. آف.] (ص‌نست.) منسوب به 
سر؟ محفی؟ بو شیده. 

سریال: ۱021 (ص.) مطلبی که جزء به 
جز و انتشار بابد) مسلسل. 


نع فررهنگ فار سي معین ۸-3
```


## [2026-09-14T02:02:14.483Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '77678,77692p' MON_part1.txt"
}
```


### [2026-09-14T02:02:14.544Z] TOOL RESULT

```
سری: -۰27 (حامص.) سروری» ریاست. 
سالاری» سر داری. 

سری: ۰۵7-1 (ص‌نسب.) منسوب به سر. آلتی 
آهنین که در هنگام جنگ بر سر اسب 
مین سای : 

سسری: (0-)971: [ممال «سرا,] (.) سراه 
سرای» خانه. 

سسری: ۹6 (.) سلسله» رشته» دوره. 
ردیف» طبقه. . ضح. احتراز از استعمال این 
کلمه بیگانه اولی است؛.
```


## [2026-09-14T02:02:24.190Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/conserve",
 "prompt": "Etymology of \"conserve\" — Old French conserver, Latin conservare, servare, and the PIE root given."
}
```


## [2026-09-14T02:02:25.575Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%B3%D8%B1%D9%88",
 "prompt": "Persian کنسرو: etymology given (French conserve?) and meaning."
}
```


### [2026-09-14T02:02:26.923Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:02:28.344Z] TOOL RESULT

```
# Etymology of "Conserve"

The word "conserve" originates from Old French *conserver* (9c.), derived from Latin *conservare*, meaning "to keep, preserve, keep intact, guard."

The Latin term combines the prefix *com-* (functioning as an intensive) with *servare*, which means "keep watch, maintain." This root traces back to the Proto-Indo-European *\*ser-*, meaning "to protect."

**Verb usage** emerged in the late 14c. with the sense "to keep safe, preserve from loss or decay."

**Noun usage** developed from the same period, initially meaning "that which preserves," and by the early 15c. referred to "a confection, something preserved with sugar, etc."

Related words sharing this etymological lineage include preserve, reserve, observe, and conservation.
```


## [2026-09-14T02:02:37.329Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/hero\" \\\n\"https://en.wiktionary.org/wiki/%E1%BC%A5%CF%81%CF%89%CF%82\" \\\n\"https://www.etymonline.com/word/hero\" \\\n\"https://en.wiktionary.org/wiki/servo\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ser-\" \\\n\"https://en.wiktionary.org/wiki/%E1%BC%A9%CF%81%CE%B1%CE%BA%CE%BB%E1%BF%86%CF%82\" \\\n\"https://en.wiktionary.org/wiki/series\" \\\n\"https://www.etymonline.com/word/sort\" \\\n\"https://www.etymonline.com/word/conserve\" \\\n\"https://abadis.ir/fatofa/%D9%87%D8%A7%D8%B1/\" \\\n\"https://abadis.ir/fatofa/%DA%A9%D9%86%D8%B3%D8%B1%D9%88/\" \\\n\"https://abadis.ir/fatofa/%D9%87%D8%B1%DA%A9%D9%88%D9%84/\" \\\n\"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%B1\" \\\n\"https://en.wiktionary.org/wiki/%E0%A4%B9%E0%A4%BE%E0%A4%B0\" \\\n\"https://www.vajehyab.com/dehkhoda/%D9%87%D8%A7%D8%B1\" ; do\npython3 tools/fetch_source.py \"$u\" --note \"page 446, roots Ser 2 / Ser 3 (Serô): verification of heros/servare/conserve/series/sort and Persian har, konserv, herkul\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T02:02:48.735Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fefec4b76581c96d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d232a27aacabb91.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/698b61cbab19c279.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0bcd4e6e8eeeae2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9167be6b04c84557.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/654f48566597ad24.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b541d10361207096.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0b80345e1687b791.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5294bbab146650ff.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/abfb6dfcdcf0c1c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cc49641299f91410.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/774f2cd00128eb74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0b46034e89792bc0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ba616a034e3aa70.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/feead756dabca7bb.txt
```


## [2026-09-14T02:03:07.230Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LEW servo\"; grep -n \"^servo\\|servo,\" LEW_1910.txt | head -5; echo \"== LEW sero\"; grep -n \"^sero \" LEW_1910.txt | head -5; echo \"== IEC serṷ / servo\"; grep -n \"^serṷ\\|^serv\\|^seruo\\|^serouo\\|^seró\" IEC.txt | head -10"
}
```


### [2026-09-14T02:03:07.320Z] TOOL RESULT

```
== LEW servo
== LEW sero
== IEC serṷ / servo
15241:seró, ið (2) "watch, keep’. Cf. seruo (seruuo) Av. harai(mi), v. "keen": Umb. a-serio, seritu *watch; let him keep'; (isophonic: W herio, inf. "challenge, Here prob. Lat. sera, f. “lock?
15258:seruos, om, io (variant: soru-) *braid, string, mesh, weave'. Cf. ser- (1) Lat. servia, f. ‘garland’; OE searu, n. (1) “art, skill’. (For OE searu, n. ‘armour’, see seruó above)
15267:seruos, om, io — seutó, ið
18802:servanU. Cf. teren- (terun-) and WP I, 728 Skt. tarnah, m. ‘young of animal, cub’; Ro- mani terno, adj. ‘young’; Li. tafnas, m. "ser, vant
```


## [2026-09-14T02:03:09.881Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 446 -l 446 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg446 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg446.png"
}
```


### [2026-09-14T02:03:11.431Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 47049 Sep 13 22:03 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg446.png
```


## [2026-09-14T02:03:16.048Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15241,15260p' IEC.txt | cut -c1-600"
}
```


### [2026-09-14T02:03:16.105Z] TOOL RESULT

```
seró, ið (2) "watch, keep’. Cf. seruo (seruuo) Av. harai(mi), v. "keen": Umb. a-serio, seritu *watch; let him keep'; (isophonic: W herio, inf. "challenge, Here prob. Lat. sera, f. “lock?
seros, om (?) “fluid”. Cf. ksero-, selos, uoruos. Evidence ambig. (For Skt. saráh, adj. “fluid”; sarà, f. “stream; Per. gau-har 'essence', see sel-); (for Gk. ouros, orrós ‘whey’, see uoruo-); (for Lat. serum, n. ‘whey’, see also ksero-, in view of Skt. ksaram, n. ‘water’); Pol. (*-ē-) siara, f. ‘colostrum’; Blg. séra, f. ‘rinse for wool. Cf. WP II, 497. Cf. also: Hitt. sesariya(mi), v. (filter, a redup. of type *sísér-)
séros ‘protracted, longwinded, dreary, bleak’. WP II, 462 Skt. (?) sarah ‘repulsive, destructive’; Oss. cf. xárà, adj. & s. ‘gloomy; gloom’ beside xalas,
ser- — seruð (seruuó, soru-)
10
20
25
30
35
40
45
1132
xalasá, adj. ‘grey’; s. “hoarfrost'; Lat. sérus, adj. “late, backward; tiresome; sad’; serius, adj. ‘grave’; Alb. ambig. i gjorë (miserable, but cf. *gher- for Gk. khéros and SEM : AHG, p. 107); Ob & Ir., sír, sior, adj. (continuous, far-reaching; lasting; OBr. W Br. hir, adj. "Jong": Cor. hyr “long; tedious’; Latv. sers, adj. ‘sad’
serp- ‘creeper, creeping; reptile’. WP II, 502 Skt. sarpáh, sarpin, adj. ‘crawling’; sarpáh, m. ‘snake’; Gk. cf. herpetón, n. ‘reptile’ beside hérpullos, mf. (a creeping plant); Alb. gjarpën, T gjarpër, m. ‘snake’; Lat. serpens, gs: -entis, mf. id. beside OLat. serpulla, id.; cf. also serp-igō, f. ‘tetter, ringworm’; Gk. hérpēs, s. id.; ON serfr, m. ‘snake’; Li. seřpē, f. (‘ground ivy? or sim.). Verbal types: Skt. sár- pāmi ‘crawl, glide’; Gk. hérpō, id.; Alb. gjerp, id.; Lat. serpo, ére, id.
sert- “braid, twist; line, series, row'. Cf. seró, srt-. (Variant: sret-) Skt. sata, f. ‘braid of hair’; Gk. ertós, adj. ‘threaded’; érsis, f. “band, binding"; Lat. ser- tus, adj. ‘entwined, woven’; serta, f. ‘chaplet, rope’; sertum, n. ‘garland’; (z-gde in) sors, gs: sortis, f. (lot, destiny’. Cf. Gk. klóthó “spin, weave’ in relation to the goddess Klothó *Fate'); Oss. xal, Dig. xalá, s. (thread, cord, string of beads; fate, destiny’, pl. xàldtà: Skt. sata); Olr. cf. sreth, f. ("line, row, series’, fr. *sret- or *srt-); OE seoróan, sv. “lie with, 
seruó (seruuó, soru-) ‘watch, guard, keep’. Cf. soruos (1). WP II, 498 Av. -haurvai(mi), v. id. o-gde, as also -haurvo, adj. *-keeping'; Gk. erúð and eirüo, v. (2), wd: Myc. cf. ereuta(s) ‘inspector’; ereutere(s), pl. id. cf. Myc. (Palace of Nestor) epi-urutewe(s) (supervisors — of leather workers. Mabel Lang: 1964-5, and cf. Gk. epíouroi, id.); Lat. Servo, are, v. “keep, watch, guard’; servus, adj. ‘enslaved’; servus, a, mf. ‘slave’; Osc. cf. serev- kid (“under the care of or sim.); (o-gde in) Gk. oüros, m. ‘guard’ (: Av. -haurvo); S. Osc. (Lucanian) sorowum
1133
seruos, om, io (variant: soru-) *braid, string, mesh, weave'. Cf. ser- (1) Lat. servia, f. ‘garland’; OE searu, n. (1) “art, skill’. (For OE searu, n. ‘armour’, see seruó above)
seselos (flowing; flow? Cf. seld Vedic sasrah, adj. id. (redup. of type sel. q. v.); Arm. heyey, i, av ‘flood’
se-se-que ‘separately, dividedly, in two". Cf. seque, Sé-, sue- Lat. sesqui- "halt": cf. Gk. hekás & héka (‘far away’, fr. *sue-Kmt-)
```


## [2026-09-14T02:03:16.710Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg446.png"
}
```


### [2026-09-14T02:03:16.735Z] TOOL RESULT

```

```


## [2026-09-14T02:03:37.786Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LAT servo\"; grep -n \"seruo\\|servo :\\|servare\" LAT.txt | head -6; echo \"== LAT sero\"; grep -n \"sero,\\|sors, \" LAT.txt | head -6; echo \"== LEW\"; grep -n \"servare\\|seruare\" LEW_1910.txt | head -5"
}
```


### [2026-09-14T02:03:37.869Z] TOOL RESULT

```
== LAT servo
6447:e.g. dans TerHaut.38, neque semper seruos currens, iratus senex,\
16006:seruorum, e^c. M.L.3508; germ.: v. isl. dekor,- m.b.all.defeer, etc. De
17870:aut seruos aut liberos coegisset aut conduxisset . Applique ensuite auxdux
28856:parables aux graphies du type seruos, uolt, etc. Mais la graphie par
32295:'quos uocant Lares, putarent, quibus tot pilae quot capita seruorum,
41364:Tables, xa,aa: si seruos furtum faxit noxiamue noxit, cf. Fest.180,35;
== LAT sero
5524:asserculus (asserculum n.Caton). M.L.736; d£noainatif: inassero, -as.
11099:s'expliquer comae l*i de infans, consero, .Insero, etc.(cf. M. Leumann,
12363:A noter seulement recludo "ouvrir" (comme resero, -as) oppose a occludo,
13509:consors: y. sors, sera.cdnstemO
20976:sors, et en celt., dans britt. faud. - Ancien, usuel.
23742:Fors eat iaan d'un ancien *fortis, cf .sors, etc. Dn rapport - r 4 el on
== LEW
```


## [2026-09-14T02:03:42.041Z] TOOL CALL #66: WebSearch

```json
{
 "query": "Avestan Harā Bərəzaitī etymology \"watch\" har- guard mountain Alborz Hasandust"
}
```


### [2026-09-14T02:03:50.797Z] TOOL RESULT

```
Web search results for query: "Avestan Harā Bərəzaitī etymology "watch" har- guard mountain Alborz Hasandust"

Links: [{"title":"ALBORZ i. The Name - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/alborz-name/"},{"title":"Hara Berezaiti","url":"https://en.wikipedia.org/wiki/Hara_Berezaiti"},{"title":"Okar Research: Sacred Mountain of Balkh: Koh e Alburz & Harā Bərəzaitī","url":"http://balkhandshambhala.blogspot.com/2014/12/sacred-mountain-of-balkh-koh-e-alburz.html"},{"title":"Religion:Hara Berezaiti - HandWiki","url":"https://handwiki.org/wiki/Religion:Hara_Berezaiti"},{"title":"Hara Berezaiti | Detailed Pedia","url":"https://detailedpedia.com/wiki-Hara_Berezaiti"},{"title":"Hara Berezaiti – The Watchtower","url":"https://www.dttvpublications.com/post/hara-berezaiti-the-watchtower"},{"title":"Hara Berezaiti - Infogalactic: the planetary knowledge core","url":"https://infogalactic.com/info/Hara_Berezaiti"},{"title":"Hara Berezaiti","url":"https://en-academic.com/dic.nsf/enwiki/2557928"},{"title":"Hara Berezaiti — Grokipedia","url":"https://grokipedia.com/page/Hara_Berezaiti"}]

Based on the search results, here's information about the etymology of Avestan Harā Bərəzaitī:

## Etymology of Harā Bərəzaitī

The name of the range probably means "high watch/guard," a common designation all over the world for mountains and high places.

### The *harā* Component

The element harā– (meaning "watch, guard, defence") comes from Old Iranian har– "to pay attention to, watch over, protect," which derives from the Indo-European root 2ser–

### The *bərəzaitī* Component

The epithet bərəzaitī is *bṛzatī, feminine from Old Iranian *bṛzant- "high"

### Overall Meaning

They are generally interpreted to mean High Watch or High Guard.

### Historical Forms and Connection to Alborz

The earliest form of the name (Av. Harā bərəzaitī, Mid. Pers. Harborz) denotes in the Avesta and in Zoroastrian writings not the existing range, but a mythological mountain chain fulfilling a cosmological function at either end of the world. In Middle Persian, Harā Bərəzaitī came to be identified with Harborz, Modern Persian Alborz, a range in northern Iran, which parallels the southern edge of the Caspian Sea.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:03:57.892Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/alborz-name/",
 "prompt": "Quote exactly what is said about the etymology of harā- and bərəzaitī, including the Indo-European root number."
}
```


### [2026-09-14T02:03:59.011Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:04:01.423Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Hara_Berezaiti",
 "prompt": "Quote the etymology section: what does harā- mean, what Old Iranian verb and Indo-European root is it derived from, and what source is cited?"
}
```


### [2026-09-14T02:04:05.293Z] TOOL RESULT

```
Based on the Etymology section, here's what the article states about **harā-**:

**Meaning:** The term means "to keep watch" or "to guard."

**Old Iranian verb and Indo-European root:** The article explains that harā- is "assumed to be derived from Proto-Indo-European (PIE) *ser-" with the same meaning of "to keep watch" or "to guard."

**Source cited:** This etymological information is attributed to Pokorny 1959, p. 910, as indicated by the reference note.

The article provides comparative English examples (conserve, observe) to illustrate how this root appears in modern languages.
```


## [2026-09-14T02:04:49.601Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-14T02:04:49.699Z] TOOL RESULT

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


## [2026-09-14T02:04:54.825Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Hara_Berezaiti\" --note \"page 446, root Ser 3: etymology of Avestan Hara Berezaiti (harā- from PIE *ser- 'guard', Pokorny 910)\" 2>&1 | tail -1; python3 tools/fetch_source.py \"https://www.etymonline.com/word/series\" --note \"page 446, root Ser 3: Latin series/serere\" 2>&1 | tail -1"
}
```


### [2026-09-14T02:04:56.863Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1eb5e3e4ae849e97.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bf6f1a4741305f31.txt
```


## [2026-09-14T02:05:01.992Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg446.png data/verification/sources/refs/ocr/BOOK/446.png && ls -la data/verification/sources/refs/ocr/BOOK/446.png"
}
```


### [2026-09-14T02:05:02.287Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 47049 Sep 13 22:05 data/verification/sources/refs/ocr/BOOK/446.png
```


## [2026-09-14T02:11:42.485Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-446.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 446,\n \"book_page\": 416,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ser 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ser- 'to guard, watch over, protect' (Pokorny 2. ser- 910; Watkins/AHD ser-1)\",\n   \"note\": (\"Pokorny IEW p.910 'Root/lemma: ser-2, Meaning: to guard, watch over, support', with exactly \"\n            \"Nourai's material: Av. haraiti/haurvaiti/haurva-, Gk. Hera and heros, Lat. servo/servare. \"\n            \"Walde-Pokorny II 498 heads the same root '3. ser- \\\"sorgend Obacht geben, schuetzen, bewahren\\\"'. \"\n            \"Watkins (AHD) ser-1 'To protect' gives CONSERVE, OBSERVE, PRESERVE, RESERVE, HERO and refers to \"\n            \"'Pok. 2. ser- 910'. Language label (Indo-European) and gloss ('protect') are both right. \"\n            \"The only weak link in the box is the Greek one (see node #6): Beekes 2010 removes heros from this \"\n            \"root. The printed chart also contains one large EMPTY box to the right of the Avestan node; it has \"\n            \"no language label and no words, and the extraction correctly carries nothing for it.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *ser- به معنای «نگاهبانی کردن، پاسداشتن» است؛ پوکورنی در صفحهٔ ۹۱۰ فرهنگ \"\n               \"ریشه‌شناسی هندواروپایی خود همین ریشه (ser-2) را با همین مواد می‌آورد: اوستایی haraiti/haurvaiti/haurva-، \"\n               \"لاتین servāre و یونانی Ἥρα/ἥρως. والده-پوکورنی (جلد ۲، ص ۴۹۸) و واتکینز (پیوست AHD، ser-1) نیز همین را \"\n               \"تأیید می‌کنند. بنابراین نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است؛ تنها حلقهٔ سست، \"\n               \"بند یونانی است که بیکس آن را از این ریشه جدا می‌کند.\"),\n   \"sources\": [\n     \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ser-\",\n     \"https://www.etymonline.com/word/conserve\",\n     \"https://en.wiktionary.org/wiki/servo\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:910\", \"status\": \"supports\",\n      \"note\": \"POK_full.txt line 73996: 'Root / lemma: ser-2 | Meaning: to guard, watch over, support | Material: Avestan haraiti \\\"hat acht, schuetzt\\\"; haurvaiti ds., haurva- \\\"beschuetzend, huetend\\\" ... gr. \\\"Hpa ... npwc ... servo, -are ... Page(s): 910'. Exactly Nourai's root, page and gloss.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"IEW p.910, ser-2\", \"stance\": \"supports\",\n      \"note\": \"'ser-2 ... to guard, watch over, support ... Page(s): 910' (grep 'ser-2' POK_full.txt)\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. II p.498\", \"stance\": \"supports\",\n      \"note\": \"'3. ser- \\\"sorgend Obacht geben, schuetzen, bewahren\\\". Av. haraiti \\\"hat acht, schuetzt\\\"; haurvaiti ds., haurva- \\\"beschuetzend, huetend\\\"' (WLD_Bd2_pages.txt line 33104, running head '498 ser-' at line 33079)\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ser-1\", \"stance\": \"supports\",\n      \"note\": \"'ser-1, To protect. 1. Extended form *serw- in Latin servare ... CONSERVE, OBSERVE, PRESERVE, RESERVE. 2. ... Greek heros, \\\"protector\\\", hero: HERO. [Pok. 2. ser- 910.]' (AHD_watkins1985.txt line 924)\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, p.1132-1133 s.v. seruo (seruuo, soru-)\", \"stance\": \"supports\",\n      \"note\": \"'seruo (seruuo, soru-) \\\"watch, guard, keep\\\". WP II, 498. Av. -haurvai(mi), v. id. ... Lat. servo, are, v. \\\"keep, watch, guard\\\"' (IEC.txt line 15258 region)\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"haraiti, haurvaiti; haurva 2\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Young Avestan har- 'to pay attention to, watch over' (Bartholomae, AiWb col. 1787: 'j. har- V. \"\n                    \"\\\"Acht haben auf -\\\". Praes. 3 hara-, 20 haurva-') supplies two present stems: a thematic hara- \"\n                    \"(3sg. haraiti) and a -u-/-w- stem haurva- (3sg. haurvaiti, with the regular Avestan development \"\n                    \"of Proto-Iranian *sarwa- > haurva-: Proto-Indo-Iranian *s- > Iranian h- before a vowel, and *-ar- \"\n                    \"+ *w > -aur- by the Avestan 'epenthesis'/u-colouring rule). The verbal adjective haurva- 'protecting, \"\n                    \"guarding' is best known in the compound pasus-haurva- 'sheep-guarding (dog)', i.e. the shepherd's dog \"\n                    \"of Videvdad 13; the agent noun haratar- 'guardian' belongs here too. Nourai's 'haurva 2' is his \"\n                    \"homonym number, correctly distinguishing this haurva- from Bartholomae's other haurva- 'whole, entire' \"\n                    \"(= Skt. sarva-, NP har), which belongs to a different root. Both forms derive directly from PIE *ser- \"\n                    \"'guard' with the *-w- extension also seen in Latin servare.\"),\n     \"derivation_fa\": (\"در اوستایی ستاک فعلی har- «پاس داشتن، مراقبت کردن» دو ستاک حال دارد: hara- (سوم‌شخص haraiti) و \"\n                       \"haurva- (سوم‌شخص haurvaiti). صورت haurva- از ایرانی باستان *sarwa- است: س ایرانی باستان در آغاز واژه \"\n                       \"پیش از واکه به ه بدل شده و خوشهٔ ‑arw‑ بر اثر قاعدهٔ «آواگذاری» (epenthesis) اوستایی به ‑aur‑ تبدیل شده است. \"\n                       \"صفت haurva- «نگاهبان» در ترکیب pasus-haurva- «سگ گلّه‌بان» (وندیداد ۱۳) به کار رفته است. شمارهٔ «۲» که \"\n                       \"نورایی پس از haurva آورده درست است و این واژه را از haurva- دیگر به معنای «همه، تمام» (هم‌ریشه با سنسکریت \"\n                       \"sarva- و فارسی «هر») جدا می‌کند. بارتولومه (ستون ۱۷۸۷) و کلاین (ص ۳۳۸) همین را می‌گویند؛ ادعای نورایی درست است.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/servo\",\n                 \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ser-\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:910\", \"status\": \"supports\",\n        \"note\": \"Pokorny p.910 opens the ser-2 material with 'Avestan haraiti \\\"hat acht, schuetzt\\\"; haurvaiti ds., haurva- \\\"beschuetzend, huetend\\\" in pasus-haurvo spa' - word for word Nourai's node.\"},\n       {\"ref\": \"KLN:338\", \"status\": \"supports\",\n        \"note\": \"Klein 1966, page markers '338 / 339' immediately precede the entry: 'conserve, tr. v. - F. conserver, fr. L. conservare ... fr. con- and servare ... which is prob. cogn. with Avestic haraiti, haurvaiti, \\\"takes care of, protects\\\", haurva, \\\"protecting\\\"' (KLN_1966.txt line 8843).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch col. ~1787 s.v. har-\", \"stance\": \"supports\",\n        \"note\": \"'j. har- V. \\\"Acht haben auf -\\\". Praes. 3 hara-, 20 haurva-; Perf. 1 hankar-' and, further on, 'haratar- m. \\\"der wacht ueber -, Acht hat auf -, Waechter\\\"'; the separate entry 'j. (i S) haurva-, p. haruva- Adj. \\\"ganz\\\" ... ai. sarva-, np. har' is the homonym Nourai numbers away.\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II p.498\", \"stance\": \"supports\",\n        \"note\": \"'Av. haraiti \\\"hat acht, schuetzt\\\"; haurvaiti ds., haurva- \\\"beschutzend, huetend\\\" in pasus-haurvo spa \\\"das Kleinvieh ... beschuetzender Hund, Schaeferhund\\\"'\"},\n       {\"src\": \"IEC\", \"where\": \"Mann p.1132 s.v. sero (2) / p.1133 s.v. seruo\", \"stance\": \"supports\",\n        \"note\": \"'sero, io (2) \\\"watch, keep\\\". Cf. seruo (seruuo) Av. harai(mi), v. \\\"keep\\\"' and 'seruo ... Av. -haurvai(mi), v. id. o-gde, as also -haurvo, adj. \\\"-keeping\\\"'\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Latin\", \"words\": \"servâre\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin servare (1sg. servo) 'to keep watch over, save, preserve' continues the *-w- extended root \"\n                    \"*ser-w- (Pokorny: 'servo, -are \\\"(den Waechter machen) erretten, receive, unversehrt bewahren\\\"'), the \"\n                    \"same extension as in Avestan haurva-; the Italic cognates Oscan serevkid, Umbrian seritu 'servato', \"\n                    \"anseriato 'observatum' show the verb was already an Italic legal/augural term for 'keep watch'. \"\n                    \"Latin regularly loses initial PIE *s- only before *w in some positions; here *s- is kept, giving \"\n                    \"ser-. De Vaan/Rix reconstruct an underlying noun *serwa-/*serwom 'observation, heedance' from which \"\n                    \"the denominative verb was built. Klein warns explicitly, and correctly, that servus 'slave' and \"\n                    \"servire 'to serve' are NOT related to servare; Nourai keeps them apart too (they are absent from \"\n                    \"his box). Nourai's circumflex in 'servâre' is his notation for long a (servare).\"),\n     \"derivation_fa\": (\"فعل لاتینی servāre «نگاه داشتن، پاسداشتن، حفظ کردن» دنبالهٔ همان ریشهٔ *ser- است با افزودهٔ ‑w‑ \"\n                       \"(*ser-w-)، درست همان افزوده‌ای که در haurva- اوستایی دیده می‌شود. شواهد ایتالیایی کهن (اسکی serevkid، \"\n                       \"اومبری seritu «servato» و anseriato «observatum») نشان می‌دهد که این فعل از دیرباز اصطلاحی آیینی-حقوقی \"\n                       \"به معنای «مراقبت کردن» بوده است. کلاین تأکید می‌کند که servus «برده» و servīre «خدمت کردن» با servāre \"\n                       \"هم‌ریشه نیستند و نورایی هم آن‌ها را در این نمودار نیاورده است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/servo\", \"https://www.etymonline.com/word/conserve\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:724\", \"status\": \"supports\",\n        \"note\": \"Klein 1966 p.724 (page marker '724' at KLN_1966.txt line 17653, immediately before the entry) s.v. hero: 'Gk. heros ... orig. \\\"defender, protector\\\", rel. to \\\"Hpa ... and cogn. with L. servare, \\\"to save, deliver, preserve, protect\\\". See conserve and cp. Hera.' - the page Nourai cites does tie servare to this root.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ser-1\", \"stance\": \"supports\",\n        \"note\": \"'1. Extended form *serw- in Latin servare, to keep, preserve: CONSERVE, OBSERVE, PRESERVE, RESERVE, (RESERVOIR).'\"},\n       {\"src\": \"POK\", \"where\": \"IEW p.910\", \"stance\": \"supports\",\n        \"note\": \"'servo, -are (den Waechter machen) erretten, receive, unversehrt bewahren', Oscan serevkid, Umbrian seritu 'servato'\"},\n       {\"src\": \"KLN\", \"where\": \"1966 p.338 s.v. conserve\", \"stance\": \"supports\",\n        \"note\": \"'L. servus, \\\"slave\\\", service, \\\"to serve\\\", are not rel. to servare' - Klein separates the homonyms, as Nourai does.\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt)\", \"stance\": \"silent\",\n        \"note\": \"the OCR of Ernout-Meillet on disk has no usable headword line for servo/sero (greps 'seruo', 'servare', 'sero,' return only running text), so nothing could be read there.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"French\", \"words\": \"conserver, observer, etc.\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin conservare (con- intensive + servare) and observare (ob- 'towards, at' + servare) passed into \"\n                    \"Gallo-Romance with the regular loss of the post-tonic syllable and of intervocalic -v- weakening kept, \"\n                    \"giving Old French conserver (attested 9th c.) and observer; the infinitives kept the Latin -er (< -are). \"\n                    \"Latin reservare and praeservare gave reserver and preserver in the same way. The nominal French conserve \"\n                    \"'preserved fruit, preserve' is a deverbal back-formation from conserver and is first used of sugar- and \"\n                    \"then of tin-preserved food; it is that noun, not the verb, that was later exported to Persian (node #4).\"),\n     \"derivation_fa\": (\"واژه‌های فرانسوی conserver و observer بازماندهٔ مستقیم لاتینی conservāre (con- تشدیدی + servāre) و \"\n                       \"observāre (ob- + servāre) هستند؛ پایانهٔ مصدری ‑āre لاتین در فرانسوی به ‑er بدل شده است. اسم conserve \"\n                       \"«خوراک نگه‌داشته» گشتهٔ پسین همین فعل است و همان است که بعدها به فارسی راه یافته است (بند ۴). ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/conserve\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. ser-1 lists CONSERVE, OBSERVE, PRESERVE, RESERVE under the Latin servare branch; the French intermediary is the standard route for all four (AHD_watkins1985.txt line 924).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 p.338 s.v. conserve; p.~925 s.v. observe\", \"stance\": \"supports\",\n        \"note\": \"'conserve, tr. v. - F. conserver, fr. L. conservare' and 'observe ... - ME. observen, fr. OF. (= F.) observer, fr. L. observare, \\\"to watch, regard\\\", fr. ob- and servare' (KLN_1966.txt lines 8843, 25930)\"},\n       {\"src\": \"WEB\", \"where\": \"Etymonline s.v. conserve (used as the modern dictionary check)\", \"stance\": \"supports\",\n        \"note\": \"'from Old French conserver (9c.), from Latin conservare \\\"to keep, preserve, keep intact, guard\\\"'\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"konserv «کنسرو»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian کنسرو konserv 'tinned/preserved food, a tin of preserves' is a 20th-century loan of the French \"\n                    \"noun conserve [kɔ̃sɛʁv]. The French nasal vowel is resolved into n + vowel (kon-), and the final -e muet \"\n                    \"is dropped, giving the Persian shape kon-serv, spelt کنسرو with و for the final v. Mo'in tags the word \"\n                    \"[فر.] = French, and Dehkhoda likewise writes 'فرانسوی'. The word came in with the imported canning \"\n                    \"industry, i.e. through the same Reza-Shah-era channel as دوجین, پاکت, کارخانه vocabulary; it is not an \"\n                    \"Arabic-mediated loan and has no Middle Persian ancestor.\"),\n     \"derivation_fa\": (\"«کنسرو» وام‌واژه‌ای فرانسوی است از conserve (خوانده: کُنسِرو). واکهٔ خیشومی فرانسوی در فارسی به \"\n                       \"«ـن + واکه» تجزیه شده و «هـ»ی خاموش پایانی افتاده است؛ ‑v پایانی با «و» نوشته می‌شود. معین در برابر این \"\n                       \"واژه نشانهٔ [فر.] و دهخدا «فرانسوی» گذاشته‌اند. این واژه در سدهٔ چهاردهم خورشیدی همراه با صنعت قوطی‌سازی \"\n                       \"وارد فارسی شده و نه پیشینهٔ پهلوی دارد و نه از راه عربی آمده است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D9%86%D8%B3%D8%B1%D9%88/\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:3097\", \"status\": \"supports\",\n        \"note\": \"Mo'in has the headword: 'کنسرو: [conserve] (اِ.) ماده‌ای خوراکی که آن را بصورت استریلیزه در قوطی یا محفظه‌ای کاملاً مسدود نگهداری کنند' (MON_part2.txt line 27198 = the Adena 2-vol reprint; the 6-vol page number 3097 could not be checked because the print edition's pagination is not online, but the entry and the French tag are exactly as Nourai reports).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. کنسرو (MON_part2.txt line 27198)\", \"stance\": \"supports\",\n        \"note\": \"'کنسرو ... ماده‌ای خوراکی که آن را بصورت استریلیزه در قوطی ... نگهداری کنند'; the abadis rendering of the same entry shows the tag '[فر.]'\"},\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (Mo'in ed.)\", \"stance\": \"silent\",\n        \"note\": \"a 17th-century dictionary; the word did not exist then, so no entry - silence expected and not an argument.\"},\n       {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie (1893)\", \"stance\": \"silent\",\n        \"note\": \"Horn predates the loan; no entry.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"conserve, observe, reserve, preserve\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"All four are Middle English borrowings from Old/Middle French of the Latin compounds of servare: \"\n                    \"conserve (late 14c., 'to keep safe') < OF conserver < L. conservare; observe (late 14c.) < OF observer \"\n                    \"< L. observare 'to watch, regard'; reserve < OF reserver < L. reservare 'to keep back'; preserve < OF \"\n                    \"preserver < Med.L. praeservare 'to guard beforehand'. In every case the French infinitive -er was \"\n                    \"anglicised to -e and the stress shifted to the Latinate second syllable. Watkins lists exactly this set \"\n                    \"under ser-1.\"),\n     \"derivation_fa\": (\"چهار واژهٔ انگلیسی conserve، observe، reserve و preserve همگی در سدهٔ چهاردهم میلادی از فرانسوی \"\n                       \"میانه وام گرفته شده‌اند و در نهایت به ترکیب‌های لاتینی conservāre، observāre، reservāre و praeservāre \"\n                       \"باز می‌گردند. پایانهٔ ‑er فرانسوی در انگلیسی به ‑e بدل شده است. واتکینز (پیوست ریشه‌های هندواروپایی \"\n                       \"فرهنگ American Heritage) دقیقاً همین چهار واژه را ذیل ser-1 می‌آورد. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/conserve\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"'ser-1, To protect. 1. Extended form *serw- in Latin servare, to keep, preserve: CONSERVE, OBSERVE, PRE-SERVE, RESERVE, (RESERVOIR). [Pok. 2. ser- 910.]' (AHD_watkins1985.txt line 924)\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 pp.338, 925\", \"stance\": \"supports\",\n        \"note\": \"s.v. conserve: 'See hero and cp. observe, preserve, reserve'; s.v. observe: 'fr. ob- and servare ... See conserve.'\"},\n       {\"src\": \"WEB\", \"where\": \"Etymonline s.v. conserve\", \"stance\": \"supports\",\n        \"note\": \"'Related words sharing this etymological lineage include preserve, reserve, observe, and conservation.'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\", \"words\": \"heros; Heracles\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"Nourai follows the 19th/20th-century consensus (Pokorny 910, Klein p.724, Watkins ser-1), which takes \"\n                    \"Gk. heros (hḗrōs, stem *hērōw-, gen. hērōos) as *ser-os- 'protector' and Hera (Ἥρα < *Hērwa) as \"\n                    \"'protectress', with -w- matching Latin serv-are. Modern scholarship rejects this: Beekes (Etymological \"\n                    \"Dictionary of Greek, 2010) shows the reconstruction *hērōw- 'is not possible in view of the lack of /w/ \"\n                    \"in Mycenaean Greek' (Myc. ti-ri-se-ro-e /Trishērōei/ has no digamma), and concludes the word is \"\n                    \"'probably Pre-Greek'; Wiktionary and Etymonline both now give the *ser- link only as 'possible'. \"\n                    \"Heracles is a separate matter: Ἡρακλῆς is transparently Ἥρα + -κλῆς (κλέος) 'glory of Hera', so it \"\n                    \"belongs to this root only indirectly, through Hera, whose own etymology is itself unsettled; and \"\n                    \"Nourai's gloss 'a legendary strong man' describes the hero, not the name. Skeat (s.v. Hero) offers a \"\n                    \"third, now abandoned, etymology, linking Gk. heros to Skt. vīra, L. vir 'man'.\"),\n     \"derivation_fa\": (\"نورایی در این بند از دیدگاه کهن (پوکورنی ص ۹۱۰، کلاین ص ۷۲۴، واتکینز) پیروی می‌کند که ἥρως یونانی را \"\n                       \"*ser-os- «نگاهبان» و Ἥρα را «بانوی نگاهبان» می‌داند و آن را با servāre لاتینی هم‌ریشه می‌شمارد. اما \"\n                       \"پژوهش امروزی این را رد می‌کند: بیکس (فرهنگ ریشه‌شناختی یونانی، ۲۰۱۰) نشان می‌دهد بازسازی *hērōw- ممکن \"\n                       \"نیست، زیرا در یونانی مینوسی-میکنی نشانی از /w/ در این واژه نیست، و آن را واژه‌ای «پیشایونانی» \"\n                       \"(Pre-Greek) می‌داند. Ἡρακλῆς نیز ترکیب Ἥρα + κλέος «شکوهِ هرا» است و تنها از راه نام هرا — که خود \"\n                       \"ریشه‌اش روشن نیست — به این ریشه می‌پیوندد. پس ادعای نورایی با معیار امروزی مورد اختلاف است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%E1%BC%A5%CF%81%CF%89%CF%82\",\n       \"https://en.wiktionary.org/wiki/hero\",\n       \"https://www.etymonline.com/word/hero\",\n       \"https://en.wiktionary.org/wiki/%E1%BC%A9%CF%81%CE%B1%CE%BA%CE%BB%E1%BF%86%CF%82\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"KLN:724\", \"status\": \"supports\",\n        \"note\": \"Klein 1966 p.724 s.v. hero: 'fr. Gk. heros (for *hērōw-os), orig. \\\"defender, protector\\\", rel. to \\\"Hpa (for *\\\"Hpfa), \\\"Hera\\\" (lit. \\\"tutelary goddess\\\"), and cogn. with L. servare'. Klein p.723 s.v. Hercules: 'fr. Gk. Hērakleēs, lit. \\\"glory of Hera\\\", fr. \\\"Hpa, \\\"Hera\\\", and kleos, \\\"glory\\\"' - so Klein's own page makes Heracles a compound of Hera, not a direct derivative.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p.910\", \"stance\": \"supports\",\n        \"note\": \"'gr. \\\"Hpa \\\"*Schuetzerin\\\" from *\\\"HpFa, npwc, -woc (stem nprwF-) \\\"*Hueter\\\" (npwec \\\"Landesschutzgeister\\\")'\"},\n       {\"src\": \"KLN\", \"where\": \"1966 p.17596 s.v. Hera\", \"stance\": \"supports\",\n        \"note\": \"'Hera ... Gk. \\\"Hpa, which stands for *\\\"HpFa, lit. means \\\"protectress\\\", and is rel. to heros'\"},\n       {\"src\": \"SKT\", \"where\": \"Concise Etym. Dict. s.v. Hero\", \"stance\": \"contradicts\",\n        \"note\": \"'Hero. (F.-L.-Gk.) O.F. heroe. - L. heroem ... - Gk. heros, a hero, demi-god. + Skt. vira, a hero, L. vir; AS. wer. Allied to Virile.' - Skeat derives it from *wiHros 'man', not from *ser-.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann p.1133 s.v. seruo\", \"stance\": \"partial\",\n        \"note\": \"Mann puts only Gk. eruo/eiruo and ouros 'guard' under seruo; heros is not listed there - i.e. Mann already declines to attach heros to this root.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"French\", \"words\": \"\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"An unlabelled pass-through box: the French form of the name, Hercule [ɛʁkyl], taken from Latin Hercules \"\n                    \"(itself from Greek Ἡρακλῆς through Etruscan Hercle, which is why Latin has -cul- and not -cle-). Nourai \"\n                    \"gives it no word and no reference, but the shape of the Persian form in node #8 (herkul, with u for the \"\n                    \"French front rounded vowel and no final -s) shows that French, not Latin or English, is the transmitting \"\n                    \"language, so the box is justified even though nothing is printed in it.\"),\n     \"derivation_fa\": (\"این خانه در نمودار تهی است و تنها نقش واسطه دارد: صورت فرانسوی نام، یعنی Hercule (هرکول)، که خود از \"\n                       \"لاتینی Hercules و آن از یونانی Ἡρακλῆς از راه اتروسکی Hercle آمده است. نورایی هیچ واژه و هیچ مأخذی در \"\n                       \"این خانه نیاورده، ولی شکل فارسی «هرکول» در بند ۸ — بی ‑s پایانی و با «و» در برابر واکهٔ گردِ پیشین \"\n                       \"فرانسوی — نشان می‌دهد که زبان واسط همان فرانسوی است. با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/%E1%BC%A9%CF%81%CE%B1%CE%BA%CE%BB%E1%BF%86%CF%82\",\n                 \"https://abadis.ir/fatofa/%D9%87%D8%B1%DA%A9%D9%88%D9%84/\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"the chart gives this box no reference at all (refs=None in the source JSON and a blank reference slot on the printed page).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 p.723 s.v. Hercules\", \"stance\": \"partial\",\n        \"note\": \"'L. Hercules, fr. earlier Hercoles, fr. Gk. Hēraklēs ... lit. \\\"glory of Hera\\\"' - Klein gives the Greek-to-Latin step but says nothing about French.\"},\n       {\"src\": \"MON\", \"where\": \"Dehkhoda/Mo'in s.v. هرکول (via abadis)\", \"stance\": \"partial\",\n        \"note\": \"Dehkhoda: 'نام رومی هراکلس قهرمان افسانه‌های ادبیات یونان و رم' - names the Roman (Latin) form as the source of the Persian name but does not say through which modern language it reached Persian.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Persian\", \"words\": \"herkŭl «هرکول»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian هرکول herkul is the Greek/Roman hero's name taken over through French Hercule: French [ɛʁkyl] \"\n                    \"gives Persian her-kul, the French front rounded [y] being rendered by Persian u (و), and the Latin \"\n                    \"nominative -s being absent because French had already lost it. In Persian it is both the mythological \"\n                    \"name (Mo'in's a'lam volume: 'رب‌النوع قدرت و نیرو در افسانه‌های یونان') and a common noun for a very \"\n                    \"strong man ('مرد بسیار نیرومند، پهلوان' in Amid), plus the constellation Hercules. Nourai's gloss \"\n                    \"'\\\"protector\\\"' is not the meaning of the Persian word - it is his back-projection of the supposed root \"\n                    \"sense onto the name - and in any case the name means 'glory of Hera', but the borrowing itself is correct.\"),\n     \"derivation_fa\": (\"«هرکول» نام پهلوان اسطوره‌ای یونان است که از راه فرانسوی Hercule به فارسی آمده است؛ واکهٔ گردِ پیشین \"\n                       \"فرانسوی [y] در فارسی «و» شده و ‑s پایانی لاتینی، که در فرانسوی افتاده بود، در فارسی هم نیست. معین در \"\n                       \"جلد اعلام آن را «رب‌النوع قدرت و نیرو در افسانه‌های یونان» و عمید «مرد بسیار نیرومند، پهلوان» معنی \"\n                       \"کرده‌اند. معنایی که نورایی در نمودار آورده («نگاهبان») معنای واژهٔ فارسی نیست، بلکه بازتاب همان ریشه‌ای \"\n                       \"است که او فرض کرده؛ نام Ἡρακλῆς در اصل «شکوهِ هرا» است. با این حال وام‌گیری‌ای که نمودار نشان می‌دهد درست است.\"),\n     \"sources\": [\"https://abadis.ir/fatofa/%D9%87%D8%B1%DA%A9%D9%88%D9%84/\"],\n     \"ref_check\": [\n       {\"ref\": \"MON5:2269\", \"status\": \"supports\",\n        \"note\": \"MON5 = Mo'in's vol. 5 (a'lam / proper names), which is where a mythological name belongs; the entry is reproduced on abadis as 'فرهنگ معین: هرکول - رب‌النوع قدرت و نیرو در افسانه‌های یونان'. The printed 6-vol pagination is not online, so the page number itself could not be verified, but the volume assignment (vol. 5, proper names) is right.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Mo'in a'lam s.v. هرکول (via abadis)\", \"stance\": \"supports\",\n        \"note\": \"'رب النوع قدرت و نیرو در افسانه های یونان'\"},\n       {\"src\": \"ARY\", \"where\": \"Dehkhoda s.v. هرکول (via abadis, used as the second Persian dictionary)\", \"stance\": \"supports\",\n        \"note\": \"'نام رومی هراکلس قهرمان افسانه های ادبیات یونان و رم'; Amid adds 'مرد قوی هیکل؛ پهلوان' and the northern-sky constellation.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"hero, Hercules\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English hero is first attested late 14c. (Chaucer, 'heroes'), from Old French heroe, from Latin heros \"\n                    \"(acc. heroem), from Greek hḗrōs; in Homer it is the title of the Achaean warriors at Troy, in Hesiod \"\n                    \"the 'race of heroes' born of a god and a mortal, and the sense 'man of great bravery' is a 1660s English \"\n                    \"development, 'chief male character of a story' 1690s. Hercules is the Latin form of Ἡρακλῆς taken \"\n                    \"directly into English (Latin has -cul- through Etruscan Hercle). The Greek-to-English chain drawn here \"\n                    \"is uncontroversial; what is disputed is only its attachment to PIE *ser- (see node #6).\"),\n     \"derivation_fa\": (\"واژهٔ انگلیسی hero نخستین بار در پایان سدهٔ چهاردهم میلادی دیده می‌شود و از فرانسوی کهن heroe، از \"\n                       \"لاتینی herōs و آن از یونانی ἥρως آمده است؛ معنای «مرد دلیر» در انگلیسی سدهٔ هفدهم و معنای «شخصیت اصلی \"\n                       \"داستان» در دههٔ ۱۶۹۰ پدید آمده است. Hercules نیز صورت لاتینی Ἡρακλῆς است که یکراست به انگلیسی رفته \"\n                       \"است. این زنجیره بی‌گفت‌وگو درست است؛ آنچه مورد اختلاف است تنها پیوند آن با ریشهٔ *ser- است (بند ۶).\"),\n     \"sources\": [\"https://www.etymonline.com/word/hero\", \"https://en.wiktionary.org/wiki/hero\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"'2. Suffixed lengthened-grade form *ser-os- perhaps in Greek heros, \\\"protector,\\\" hero: HERO.' - note Watkins's own 'perhaps' (AHD_watkins1985.txt line 924).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 pp.723-724\", \"stance\": \"supports\",\n        \"note\": \"'hero, n. - MF. heroe, fr. heroe (F. heros), fr. L. heroem, acc. of heros'; 'Hercules ... L. Hercules, fr. earlier Hercoles, fr. Gk. Hērakleēs'\"},\n       {\"src\": \"SKT\", \"where\": \"s.v. Hero\", \"stance\": \"partial\",\n        \"note\": \"'O.F. heroe. - L. heroem ... - Gk. heros' - the same word-chain, but a different PIE attachment (Skt. vira, L. vir).\"},\n       {\"src\": \"WEB\", \"where\": \"Etymonline s.v. hero\", \"stance\": \"supports\",\n        \"note\": \"'late 14c., from Old French heroe, from Latin heros, from Greek heros ... Probably a Pre-Greek word.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ser 3, Serô\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ser- 'to put/bind together, line up' (Pokorny 4. ser- 911; Watkins/AHD ser-3 'to line up')\",\n   \"note\": (\"Pokorny IEW p.911 'Root/lemma: ser-4, Meaning: to put together, bind together', Walde-Pokorny II 499 \"\n            \"'4. ser- \\\"aneinander reihen, knuepfen\\\"', Watkins ser-3 'To line up ... [Pok. 4. ser- 911]', Mann IEC \"\n            \"pp.1129-1131 'sero, io (1) \\\"join, range, arrange\\\"'. The reconstruction, the language label and the gloss \"\n            \"are correct, and the page number 911 is Pokorny's. Nourai's serial number differs from Pokorny's (his 'Ser 3' \"\n            \"is Pokorny's ser-4; Pokorny's ser-3 is a root meaning 'red'), but that is only house numbering. The chart's \"\n            \"weak spots are the two words Nourai took over from Mann's entry: Skt. hara and Av. hara (nodes #1 and #3). \"\n            \"The printed chart also has one large unlabelled EMPTY box to the right of the Avestan node; nothing is lost \"\n            \"by the extraction not carrying it.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *ser- به معنای «به هم پیوستن، به رشته کشیدن، ردیف کردن» است؛ پوکورنی آن را در \"\n               \"صفحهٔ ۹۱۱ زیر ser-4 «to put together, bind together»، والده-پوکورنی در جلد ۲ صفحهٔ ۴۹۹ و واتکینز زیر ser-3 \"\n               \"«to line up» آورده‌اند و مان (فرهنگ تطبیقی هندواروپایی، ص ۱۱۲۹–۱۱۳۱) نیز مدخل sero (1) «join, range, \"\n               \"arrange» دارد. بازسازی و معنا و شمارهٔ صفحه درست است؛ شمارهٔ ریشه در کتاب نورایی («Ser 3») با شمارهٔ \"\n               \"پوکورنی (ser-4) یکی نیست ولی این تنها شماره‌گذاری داخلی است. نقطه‌های سست نمودار دو واژه‌ای است که نورایی \"\n               \"از مدخل مان برداشته است: hāra سنسکریت و harā اوستایی (بندهای ۱ و ۳).\"),\n   \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ser-\",\n               \"https://en.wiktionary.org/wiki/series\",\n               \"https://www.etymonline.com/word/sort\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:911\", \"status\": \"supports\",\n      \"note\": \"POK_full.txt line 74054: 'Root / lemma: ser-4 | Meaning: to put together, bind together | Material: Old Indic sarat-, sarit- \\\"filament\\\" ... Latin sero, -ere, -tum \\\"fuegen, put in a line, tie, bind, knot\\\", series ... sors \\\"lot, fate\\\" ... Page(s): 911'.\"},\n     {\"ref\": \"IEC:1131\", \"status\": \"supports\",\n      \"note\": \"Mann, An Indo-European Comparative Dictionary, the leaf beginning at printed p.1129 carries 'sero, io (1) \\\"join, range, arrange\\\". Cf. srtis. WP II, 499 Skt. cf. sarat, m. (\\\"thread\\\", fr. *sernt-); Av. cf. hara, f. \\\"mountain range\\\"; Per. har, s. \\\"row, rank; string of beads\\\" ... Lat. sero, ere ... series, f. \\\"series\\\"' (IEC.txt line 15240). This single entry is the source of Nourai's whole left-hand column.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"IEW p.911, ser-4\", \"stance\": \"supports\",\n      \"note\": \"'ser-4 ... to put together, bind together ... Page(s): 911'\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. II p.499\", \"stance\": \"supports\",\n      \"note\": \"'4. ser- \\\"aneinander reihen, knuepfen\\\". Ai. sarat- \\\"Faden\\\" (unbelegt) ... gr. eiro ... lat. sero' (WLD_Bd2_pages.txt line 33206)\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ser-3\", \"stance\": \"supports\",\n      \"note\": \"'ser-3, To line up. 1. Latin serere, to arrange, attach, join: SERIES, SERTULARIAN; ASSERT, DESERT, DISSERTATE, EXERT, INSERT ... 4. ... Latin sors (stem sort-), lot, fortune ... SORCERER, SORT; ASSORT, CONSORT, SORTILEGE. [Pok. 4. ser- 911.]'\"},\n     {\"src\": \"IEC\", \"where\": \"Mann p.1131 s.v. sert-\", \"stance\": \"supports\",\n      \"note\": \"'sert- \\\"braid, twist; line, series, row\\\". Cf. sero, srt- ... Lat. sertus, adj. \\\"entwined, woven\\\" ... (z-gde in) sors, gs: sortis, f. \\\"lot, destiny\\\"'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"sarat; hâra\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"Two words with two different fates. (a) sarat- 'thread, filament' is the form Pokorny (p.911), \"\n                    \"Walde-Pokorny (II 499), Klein (s.v. series) and Mann all cite as the Indic reflex of *ser-, with the \"\n                    \"-nt-/-t- suffix (Mann reconstructs *sernt-); Nourai's gloss 'thread' is theirs. It must be said that \"\n                    \"Walde-Pokorny mark it '(unbelegt)' and Pokorny '(uncovered)', i.e. the word is a lexicographers' form \"\n                    \"with no textual attestation - so the anchor of the whole Indic branch is weak. (b) hara 'string of \"\n                    \"beads' (Skt. hāra- m. 'necklace, pearl necklace') does NOT belong here. Monier-Williams derives hāra- \"\n                    \"as a vrddhi-derivative of hara- from the root hṛ 'to take, carry, wear' (PIE *ǵʰer- 'to grasp'), which \"\n                    \"gives the regular semantics 'that which is worn/carried (round the neck)'; Sanskrit h- from PIE *ǵʰ- is \"\n                    \"regular, whereas *ser- would have had to give Sanskrit s-, not h-, making Nourai's derivation \"\n                    \"phonologically impossible. Decisively, Mo'in himself, in his etymological footnote to Borhan-e Qate' \"\n                    \"s.v. هار, writes 'سانسکریت hāra ... از ریشهٔ hṛ (بردن، پوشیدن، گرفتن)' with a reference to \"\n                    \"Monier-Williams I:1289. Note also that Mann, Nourai's own source, does not list a Sanskrit hara at all: \"\n                    \"he lists 'Per. har', a Persian word, and Nourai appears to have moved it up into a Sanskrit box.\"),\n     \"derivation_fa\": (\"این بند دو واژه دارد با دو سرنوشت. نخست sarat- «رشته، نخ»: پوکورنی (ص ۹۱۱)، والده-پوکورنی (ج ۲ ص \"\n                       \"۴۹۹)، کلاین و مان همگی آن را بازتاب هندی ریشهٔ *ser- می‌دانند؛ ولی باید گفت که والده-پوکورنی در برابر \"\n                       \"آن «unbelegt» (بی‌شاهد) نوشته است، یعنی این صورت در هیچ متنی به کار نرفته و تنها ساختهٔ فرهنگ‌نویسان \"\n                       \"است. دوم hāra «گردن‌بند، رشتهٔ مروارید»: این واژه به این ریشه ربطی ندارد. مونیرویلیامز آن را \"\n                       \"برساختهٔ وریدی (vṛddhi) از hara- و از ریشهٔ hṛ «بردن، گرفتن، پوشیدن» (هندواروپایی *ǵʰer-) می‌داند؛ \"\n                       \"«ه» سنسکریت بازتاب قانونمند *ǵʰ است، حال آنکه *ser- در سنسکریت می‌بایست «س» بدهد نه «ه». از همه \"\n                       \"مهم‌تر، خود معین در حاشیهٔ ریشه‌شناختی برهان قاطع ذیل «هار» می‌نویسد: «سانسکریت hāra ... از ریشهٔ hṛ \"\n                       \"(بردن، پوشیدن، گرفتن)». پس پژوهش امروزی نیمهٔ دوم این بند را رد می‌کند.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B9%E0%A4%BE%E0%A4%B0\",\n                 \"https://en.wiktionary.org/wiki/series\",\n                 \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ser-\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1131\", \"status\": \"partial\",\n        \"note\": \"Mann s.v. sero (1) does have 'Skt. cf. sarat, m. (\\\"thread\\\", fr. *sernt-)' - so sarat is his; but the same entry has NO Sanskrit hara, only 'Per. har, s. \\\"row, rank; string of beads\\\"'. Nourai's Sanskrit hara is therefore not from the page he cites.\"},\n       {\"ref\": \"MON:5081\", \"status\": \"partial\",\n        \"note\": \"Mo'in's lexicon entry for هار is the Persian word (node #2); the Sanskrit hāra he gives there (repeated verbatim in his Borhan-e Qate' footnote, BQT vol. 4 printed p.2305) is explicitly derived from the root hṛ, not from *ser-, so the reference names the word but contradicts the arrow drawn from this root.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p.911\", \"stance\": \"partial\",\n        \"note\": \"'Old Indic sarat-, sarit- \\\"filament\\\" (uncovered)' - has sarat but qualifies it as unattested, and has no hāra.\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II p.499\", \"stance\": \"partial\",\n        \"note\": \"'Ai. sarat- \\\"Faden\\\" (unbelegt), vielleicht sata \\\"Maehne, Borste\\\" (Uhlenbeck)' - same reservation.\"},\n       {\"src\": \"KLN\", \"where\": \"1966 s.v. series\", \"stance\": \"partial\",\n        \"note\": \"'cogn. with OI. sarat-, \\\"thread\\\", Gk. eirein ... Goth. sarwa' - sarat yes, hāra no.\"},\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', Mo'in ed., vol. 4 printed p.2305 (pdf p.388), footnote 5 to هار\", \"stance\": \"contradicts\",\n        \"note\": \"'سانسکریت hāra (مروارید، حلقهٔ مروارید، گردن‌بند) «ویلیامز» از ریشهٔ hṛ (بردن، پوشیدن، گرفتن) «ایضاً ۱۲۸۹:۱»' - Mo'in derives Skt. hāra from hṛ, not from *ser-.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"hâr «هار»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"The Persian word is genuine and Nourai's gloss is accurate: Dehkhoda's هار (2) is 'رشتهٔ مروارید' \"\n                    \"(string of pearls), 'گردن‌بند' (necklace), and by metonymy 'گردن' (neck) and 'مهره‌های گردن' (the \"\n                    \"cervical vertebrae), whence also 'افسار شتر' (camel halter); Ferdowsi's line quoted by Nourai \"\n                    \"('... بر آن بادپایان آهخته هار', printed in Borhan-e Qate' as 'کزید از سواران برون از شمار') uses the \"\n                    \"'neck' sense - horses with outstretched necks. The route drawn (Indic > Persian) is also right: \"\n                    \"Dehkhoda and Mo'in both derive it from Sanskrit hāra, and Wiktionary makes it a loan from Hindi हार \"\n                    \"hār. What is wrong is the root: since Skt. hāra- is from hṛ 'carry, wear' (PIE *ǵʰer-), Persian hār \"\n                    \"does not descend from *ser- 'line up' at all. There is one alternative that would rescue the box: \"\n                    \"Mann himself (IEC, s.v. sero (1)) lists 'Per. har, s. \\\"row, rank; string of beads\\\"' as a native \"\n                    \"Iranian cognate of Skt. sarat-, i.e. not a loan - but that would require the arrow to come from the \"\n                    \"root box, not from the Sanskrit node, and no Iranian source (Horn, Hubschmann, Hasandust) supports a \"\n                    \"native *sāra- here. Verdict: the word and the Indic borrowing are confirmed, the root attachment is not.\"),\n     \"derivation_fa\": (\"واژهٔ «هار» فارسی راستین است و معنایی که نورایی داده درست: دهخدا آن را «رشتهٔ مروارید»، «گردن‌بند» و \"\n                       \"به مجاز «گردن» و «مهره‌های گردن» و «افسار شتر» آورده است؛ بیت فردوسی که نورایی شاهد آورده («... بر آن \"\n                       \"بادپایان آهخته هار») به همان معنای «گردن» است، یعنی اسبانی با گردنِ کشیده. راهِ وام‌گیری هم درست \"\n                       \"است: دهخدا و معین هر دو آن را از سانسکریت hāra می‌دانند و ویکی‌واژه آن را وام‌واژه‌ای از هندی हार \"\n                       \"می‌شمارد. آنچه نادرست است ریشهٔ بالادست است: چون hāra سنسکریت از hṛ «بردن، پوشیدن» (هندواروپایی \"\n                       \"*ǵʰer-) است، «هار» فارسی به ریشهٔ *ser- «ردیف کردن» نمی‌رسد. مان خودِ صورت فارسی har را واژه‌ای \"\n                       \"بومی و هم‌ریشه با sarat سنسکریت می‌داند، ولی در آن صورت باید پیکان از خانهٔ ریشه بیاید نه از خانهٔ \"\n                       \"سنسکریت، و هیچ منبع ایرانی‌شناختی این را تأیید نمی‌کند. پس با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\"https://www.vajehyab.com/dehkhoda/%D9%87%D8%A7%D8%B1\",\n                 \"https://abadis.ir/fatofa/%D9%87%D8%A7%D8%B1/\",\n                 \"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1131\", \"status\": \"supports\",\n        \"note\": \"'Per. har, s. \\\"row, rank; string of beads\\\"' stands in Mann's sero (1) entry exactly as Nourai reports the meaning - though Mann has it as a direct descendant of the root, not via Sanskrit.\"},\n       {\"ref\": \"MON:5081\", \"status\": \"supports\",\n        \"note\": \"Mo'in has the word; his etymological note, printed in full in his edition of Borhan-e Qate' (vol. 4, printed p.2305, footnote 5) reads 'سانسکریت hāra (مروارید، حلقهٔ مروارید، گردن‌بند) «ویلیامز» ... پشتو hār (گردن‌بند، حلقه) «بلیو ص ۱۷۹»؛ «هار، رشتهٔ مروارید بود»' - the Sanskrit source of the Persian word is Mo'in's own view, so the arrow Sanskrit > Persian is his.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', Mo'in ed., vol.4 printed p.2305 (pdf 388), headword هار and footnotes 5-6\", \"stance\": \"partial\",\n        \"note\": \"headword: 'هار - بروزن مار، هرچیزی راگویند عموماً که از پی هم بتوالی ... درآمده باشد ... و مروارید ... که در یک رشته کشیده شده باشد ... و گردن و مهره‌های گردن حیوانات را نیز گفته‌اند'; footnote 6 gives the Ferdowsi line 'کزید از سواران برون از شمار / بر آن باد پایان آهخته هار'. Supports word and meaning, contradicts the root.\"},\n       {\"src\": \"MON\", \"where\": \"Mo'in / Dehkhoda s.v. هار (via vajehyab & abadis)\", \"stance\": \"supports\",\n        \"note\": \"Dehkhoda: 'رشته مروارید بود', 'گردن بند', 'گردن', 'مهره‌های گردن هر حیوان', 'افسار شتر'; from Sanskrit hāra.\"},\n       {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (1893)\", \"stance\": \"silent\",\n        \"note\": \"greps for 'Halskette', 'gardanband' in HRN.txt return nothing; Horn has no article on هار.\"},\n       {\"src\": \"ARY\", \"where\": \"Wiktionary s.v. هار (used as the independent modern cross-check)\", \"stance\": \"partial\",\n        \"note\": \"'هار (hâr) ... archaic noun, string (of beads or pearls) ... borrowed from Hindi हार (hār), from Sanskrit हारि (hāri)' - Indic origin confirmed, *ser- not mentioned.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Avestan\", \"words\": \"hara\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"Avestan harā- f. is real: Bartholomae, AiWb col. 1788, 'j. harā- f. Name eines sagenhaften Gebirgs', \"\n                    \"usually with the epithet bərəzaitī, i.e. Harā Bərəzaitī, the mythical world-mountain of Yt. 10 and \"\n                    \"Y. 42.3, which in Middle Persian becomes Harborz and in New Persian البرز Alborz. But it does not \"\n                    \"belong to *ser- 'line up'. The standard etymology (Encyclopaedia Iranica, ALBORZ i; Wikipedia s.v. \"\n                    \"Hara Berezaiti citing Pokorny 910) makes harā- 'watch, guard, defence' a noun from Old Iranian har- \"\n                    \"'to pay attention to, watch over, protect' - that is, from Pokorny's ser-2, the root of Nourai's OWN \"\n                    \"previous entry on this very page - so that Harā Bərəzaitī is 'the High Watch', the mountain from whose \"\n                    \"summit (taēra-) the sun, moon and stars are watched circling. The error is inherited from Mann, who \"\n                    \"glossed Av. hara as 'mountain range' and filed it under sero 'join, range, arrange' - evidently misled \"\n                    \"by the English word 'range', which in 'mountain range' has nothing to do with ranging things in a row \"\n                    \"in the Iranian word. Nourai should have drawn this box under Ser 2.\"),\n     \"derivation_fa\": (\"واژهٔ اوستایی harā- راستین است: بارتولومه (ستون ۱۷۸۸) آن را «نام کوهی افسانه‌ای» می‌خواند که معمولاً \"\n                       \"با صفت bərəzaitī می‌آید، یعنی Harā Bərəzaitī، همان کوه اسطوره‌ای مهریشت و یسنا ۴۲ که در فارسی میانه \"\n                       \"Harborz و در فارسی نو «البرز» شده است. اما این واژه به ریشهٔ *ser- «ردیف کردن» تعلق ندارد. \"\n                       \"ریشه‌شناسی پذیرفته‌شده (دانشنامهٔ ایرانیکا، مدخل ALBORZ؛ و نیز ارجاع به پوکورنی ص ۹۱۰) harā- را به \"\n                       \"معنای «نگاهبانی، پاس» و برگرفته از فعل ایرانی باستان har- «پاس داشتن، نگاهبانی کردن» می‌داند؛ یعنی \"\n                       \"از همان ریشهٔ ser-2 پوکورنی که نورایی درست در بالای همین صفحه (Ser 2) آورده است. پس Harā Bərəzaitī \"\n                       \"«پاسگاهِ بلند» است. خطا از مان به نورایی رسیده است: مان این واژه را «mountain range» ترجمه کرده و \"\n                       \"به دلالت واژهٔ انگلیسی range آن را ذیل sero «ردیف کردن» گذاشته است. جای درست این خانه، ریشهٔ Ser 2 است.\"),\n     \"sources\": [\"https://en.wikipedia.org/wiki/Hara_Berezaiti\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1131\", \"status\": \"supports\",\n        \"note\": \"Mann s.v. sero (1) does contain 'Av. cf. hara, f. \\\"mountain range\\\"' (IEC.txt line 15240) - Nourai reports his source faithfully; the source itself is what is wrong.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch col. 1788 s.v. harā-, col. 1787 s.v. haraiti-\", \"stance\": \"partial\",\n        \"note\": \"'j. harā- f. Name eines sagenhaften Gebirgs' and 'j. haraiti- f. Name eines sagenhaften Gebirgs ... Pu.: har burz'; Bartholomae gives the meaning but files the word next to the verb har- 'Acht haben auf -', not under any 'row/line' root.\"},\n       {\"src\": \"POK\", \"where\": \"IEW pp.910 and 911\", \"stance\": \"contradicts\",\n        \"note\": \"Pokorny's ser-4 (p.911) has no Avestan material at all; the only Avestan words in either ser- entry are haraiti/haurvaiti/haurva- under ser-2 (p.910) - i.e. Pokorny would place harā- with the 'guard' root if anywhere.\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II p.499\", \"stance\": \"silent\",\n        \"note\": \"Walde-Pokorny's '4. ser- \\\"aneinander reihen, knuepfen\\\"' lists no Iranian word (Ai. sarat-, Gk. eiro, Lat. sero, Olith. seris, Hitt. sarra-).\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"serere; sors\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin serō, serere, sertum 'to join in a row, string together, plait, link' is the thematic present of \"\n                    \"*ser- (Greek eírō 'I string together' is its exact match, with initial *s- > h- lost in Greek psilosis \"\n                    \"before the digamma-less vowel); from its participle come serta 'garlands' and the abstract seriēs \"\n                    \"'row, succession'. sors, sortis 'lot, fate, share' is the zero-grade *sr-ti- of the same root, so \"\n                    \"named, as Pokorny puts it, 'probably from the stringing up of the lots' before they were drawn - a \"\n                    \"Roman divinatory practice (the sortes of Praeneste). Nourai's glosses 'to arrange, join' and 'lot, \"\n                    \"fortune' are exactly those of Pokorny and Watkins.\"),\n     \"derivation_fa\": (\"فعل لاتینی serō/serere/sertum «به هم پیوستن، به رشته کشیدن، بافتن» ستاک حالِ ثمه‌دار همین ریشه است و \"\n                       \"برابر دقیق آن در یونانی eírō «به رشته می‌کشم» است. از صفت مفعولی آن serta «گل‌آویز» و از آن اسم \"\n                       \"معنی seriēs «ردیف، رشته» ساخته شده است. واژهٔ sors/sortis «قرعه، بخت» صورت درجه‌صفرِ *sr-ti- از \"\n                       \"همین ریشه است؛ چنان‌که پوکورنی می‌گوید، نام آن از «به رشته کشیدنِ قرعه‌ها» پیش از کشیدن قرعه گرفته \"\n                       \"شده است. معناهایی که نورایی داده همان معناهای پوکورنی و واتکینز است؛ ادعای او درست است.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/series\", \"https://www.etymonline.com/word/sort\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:1538\", \"status\": \"supports\",\n        \"note\": \"Nourai's page is in the 1976 AHD appendix (not open online); the same root entry in the 1985 Watkins edition reads 'ser-3, To line up. 1. Latin serere, to arrange, attach, join ... 4. Suffixed zero-grade form *sr-t- in Latin sors (stem sort-), lot, fortune (probably from the lining up of lots before drawing) ... [Pok. 4. ser- 911.]' (AHD_watkins1985.txt line 926) - word for word Nourai's two Latin words and glosses.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p.911\", \"stance\": \"supports\",\n        \"note\": \"'Latin sero, -ere, -tum \\\"fuegen, put in a line, tie, bind, knot\\\", series \\\"order, chain, row\\\", ... sors \\\"lot, fate\\\" (probably of Aufreihen the Lose)'\"},\n       {\"src\": \"KLN\", \"where\": \"1966 s.v. series\", \"stance\": \"supports\",\n        \"note\": \"'L. series, \\\"a row, succession, sequence, series\\\", rel. to serere, \\\"to put in a row, join together\\\" ... and in gradational relationship to sors, \\\"lot\\\"'\"},\n       {\"src\": \"IEC\", \"where\": \"Mann pp.1129 and 1131\", \"stance\": \"supports\",\n        \"note\": \"'Lat. sero, ere, sup. sertum, v. \\\"arrange\\\"; series, f. \\\"series\\\"' (s.v. sero (1)) and '(z-gde in) sors, gs: sortis, f. \\\"lot, destiny\\\"' (s.v. sert-)\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt)\", \"stance\": \"silent\",\n        \"note\": \"the OCR on disk has no retrievable headword article for sero/sors (only running text such as 'consors: v. sors, sera' at line 13509).\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"series, assert, insert; sort, sorcerer, assort, consort\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Two sub-groups, both Latin. (a) From serere: series was taken straight from Latin in the 1610s; assert \"\n                    \"< L. assertus, pp. of asserere 'to join to oneself, claim'; insert < L. insertus, pp. of inserere 'to \"\n                    \"put in, graft'. (b) From sors, sortis: sort < OF sorte < L. sortem 'lot, share, rank, category' (the \"\n                    \"sense 'kind, class' via Vulgar Latin 'what is allotted > condition > rank'); assort (late 15c.) and \"\n                    \"consort are French compounds of the same noun; sorcerer < MF sorcier < Vulgar Latin *sortiarius 'one \"\n                    \"who casts lots, tells fortunes by lot'. Watkins lists precisely this set under ser-3.\"),\n     \"derivation_fa\": (\"این واژه‌ها دو دسته‌اند و هر دو از لاتین. نخست از serere: واژهٔ series در دههٔ ۱۶۱۰ یکراست از \"\n                       \"لاتین گرفته شده؛ assert از assertus (اسم مفعول asserere) و insert از insertus (اسم مفعول \"\n                       \"inserere). دوم از sors/sortis: واژهٔ sort از فرانسوی کهن sorte و آن از sortem لاتینی «قرعه، بهره، \"\n                       \"طبقه»، و assort و consort ترکیب‌های فرانسوی همان اسم‌اند؛ sorcerer از *sortiarius لاتینی عامیانه \"\n                       \"«کسی که با قرعه فال می‌گیرد» است. واتکینز دقیقاً همین فهرست را ذیل ser-3 آورده است؛ ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/sort\", \"https://en.wiktionary.org/wiki/series\",\n                 \"https://www.etymonline.com/word/series\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"'ser-3, To line up. 1. ... SERIES, SERTULARIAN; ASSERT, DESERT, DISSERTATE, EXERT, INSERT ... 4. ... SORCERER, SORT; ASSORT, CONSORT, SORTILEGE.' (AHD_watkins1985.txt line 926) - all seven of Nourai's English words are there.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 s.vv. series, assert, insert, sort, sorcerer\", \"stance\": \"supports\",\n        \"note\": \"s.v. series: 'Cp. assert, assort, consort, desert ... insert, resort ... sorcerer, sort'; s.v. sorcerer: 'fr. VL. *sortiarius, \\\"a caster of lots\\\", fr. *sortiari ... fr. sors, gen. sortis'\"},\n       {\"src\": \"WEB\", \"where\": \"Etymonline s.v. sort\", \"stance\": \"supports\",\n        \"note\": \"'from Latin sortem (nominative sors) \\\"lot; fate, destiny; share, portion; rank, category\\\" ... from PIE root *ser- (2) \\\"to line up\\\"'; assort, consort, sorcery listed as relatives.\"},\n       {\"src\": \"SKT\", \"where\": \"Concise Etymological Dictionary\", \"stance\": \"silent\",\n        \"note\": \"Skeat's entries for series/sort were not retrievable from the OCR headword lines in SKT.txt (greps '^series,', '^sort,' find nothing).\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"French\", \"words\": \"seri, seriyal\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"The French words meant are série 'series, set, row' (a learned 18th-century borrowing of Latin seriēs, \"\n                    \"with the Latin -ēs remade as French -ie) and sérial (the adjective/noun used of a story published in \"\n                    \"instalments, itself modelled on English serial < L. seriālis). The forms printed in the book, 'seri' \"\n                    \"and 'seriyal', are not French spellings: they are Nourai's transliteration of the shapes the words \"\n                    \"have once they are in Persian (seri, seriyâl), put into the French box. The page image (pdf p.446) \"\n                    \"confirms the book really prints 'seri, seriyal', so the extraction is faithful; only the labelling is \"\n                    \"loose. The chain Latin series > French série > Persian is otherwise standard. Nourai's reference \"\n                    \"VOP:212 (Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, 1371) could not be checked - no copy of that \"\n                    \"book exists online.\"),\n     \"derivation_fa\": (\"واژه‌های فرانسوی موردنظر série «رشته، دوره، ردیف» (وام‌واژه‌ای عالمانه از seriēs لاتینی در سدهٔ \"\n                       \"هجدهم، با بدل‌شدن ‑ēs لاتینی به ‑ie فرانسوی) و sérial (صفت/اسم برای داستان دنباله‌دار، خود به \"\n                       \"پیروی از serial انگلیسی) است. صورت‌هایی که در کتاب چاپ شده — «seri» و «seriyal» — املای فرانسوی \"\n                       \"نیستند بلکه آوانگاشت نورایی از شکل فارسیِ همین واژه‌ها («سری» و «سریال») است که در خانهٔ فرانسوی \"\n                       \"نشسته است. تصویر صفحهٔ چاپی نشان می‌دهد که همین صورت‌ها در کتاب آمده و پس خطای خوانش اسکن در کار \"\n                       \"نیست؛ تنها برچسب‌گذاری نمودار دقیق نیست. زنجیرهٔ لاتینی seriēs ← فرانسوی série ← فارسی درست است. \"\n                       \"مأخذ VOP:212 (مشیری، فرهنگ واژه‌های اروپایی در فارسی) در دسترس نبود.\"),\n     \"sources\": [\"https://en.wiktionary.org/wiki/series\", \"https://www.etymonline.com/word/series\"],\n     \"ref_check\": [\n       {\"ref\": \"VOP:212\", \"status\": \"not_checked\",\n        \"note\": \"refs_online.json records VOP (Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992) as kind 'none': 'Searched archive.org, ketabnak, noorlib, web: not found'. No copy could be consulted.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 s.v. series\", \"stance\": \"partial\",\n        \"note\": \"gives Latin series and its Romance/English progeny but does not treat French série separately.\"},\n       {\"src\": \"WEB\", \"where\": \"Etymonline / Wiktionary s.v. series\", \"stance\": \"supports\",\n        \"note\": \"'PIE *ser- \\\"to bind\\\" > Proto-Italic *sero > Latin serere > Latin series' - the Latin ancestor of French série is confirmed; French série is the regular learned reflex.\"},\n       {\"src\": \"MON\", \"where\": \"Mo'in s.v. سری (MON_part1.txt line 77689)\", \"stance\": \"supports\",\n        \"note\": \"'سری: [série] (اِ.) سلسله، رشته، دوره، ردیف، طبقه' - Mo'in prints the French etymon série in Latin script for the Persian word, confirming French as the transmitting language.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"serî «سری ( سریال )»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian سری seri 'series, set, batch, run (of a product)' is a 20th-century loan of French série; the \"\n                    \"final French -ie [i] is rendered by Persian -i (ی) and the acute accent disappears. Mo'in's entry \"\n                    \"prints the French etymon in Latin script and glosses it 'سلسله، رشته، دوره، ردیف، طبقه', adding the \"\n                    \"purist note 'احتراز از استعمال این کلمهٔ بیگانه اولی است' ('it is better to avoid this foreign word'), \"\n                    \"which is itself proof that Mo'in treated it as a European loan and not as the homonymous native سری \"\n                    \"'headship' (from سر) or سری 'secret' (Arabic سرّی). The parenthetic سریال seriyâl in Nourai's box is \"\n                    \"the related loan of French sérial / English serial, 'a work published or broadcast in instalments', \"\n                    \"for which Mo'in has a separate entry ('مطلبی که جزء به جزء انتشار یابد؛ مسلسل'); today it is the \"\n                    \"ordinary Persian word for a television series.\"),\n     \"derivation_fa\": (\"«سری» وام‌واژه‌ای فرانسوی است از série؛ پایانهٔ ‑ie فرانسوی در فارسی «ی» شده و نشانهٔ زیر و زبر \"\n                       \"فرانسوی از میان رفته است. معین در فرهنگ فارسی ریشهٔ فرانسوی را به خط لاتین آورده و آن را «سلسله، \"\n                       \"رشته، دوره، ردیف، طبقه» معنی کرده و افزوده است: «احتراز از استعمال این کلمهٔ بیگانه اولی است» — که \"\n                       \"خود گواه است او آن را وام‌واژه‌ای اروپایی می‌دانسته و نه هم‌آوای «سری» فارسی (از «سر») یا «سرّی» \"\n                       \"عربی. «سریال» که نورایی در کمانک آورده وام‌واژهٔ خویشاوند آن است از sérial فرانسوی/serial انگلیسی، \"\n                       \"و معین برای آن مدخل جداگانه دارد: «مطلبی که جزء به جزء انتشار یابد؛ مسلسل». ادعای نورایی درست است.\"),\n     \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%D8%B1%DB%8C%D8%A7%D9%84/\"],\n     \"ref_check\": [\n       {\"ref\": \"VOP:212\", \"status\": \"not_checked\",\n        \"note\": \"Moshiri's Farhang-e Vazheha-ye Orupayi dar Farsi is not available in any digital form (refs_online.json: kind 'none', 'Purchase second-hand only'), so Nourai's page could not be checked; the claim was verified instead against Mo'in.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سری and سریال (MON_part1.txt lines 77689, 77696)\", \"stance\": \"supports\",\n        \"note\": \"'سری: [série] (اِ.) سلسله، رشته، دوره، ردیف، طبقه. ضح: احتراز از استعمال این کلمهٔ بیگانه اولی است'; 'سریال: [sérial] (ص.) مطلبی که جزء به جزو انتشار یابد؛ مسلسل'\"},\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (Mo'in ed.)\", \"stance\": \"silent\",\n        \"note\": \"a 17th-century dictionary; neither سری 'series' nor سریال can be there.\"},\n       {\"src\": \"ARY\", \"where\": \"abadis compilation (Dehkhoda/Amid/user notes) s.v. سریال\", \"stance\": \"supports\",\n        \"note\": \"'واژه سریال فرانسوی است' - the Persian lexicographic tradition treats it as a French loan.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-446.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-446.py"
}
```


### [2026-09-14T02:11:47.108Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-446.json
```


## [2026-09-14T02:11:49.465Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-446.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 446"
}
```


### [2026-09-14T02:11:50.799Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 10, 'disputed': 3, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'not_checked': 3, 'partial': 2}
books consulted: {'supports': 27, 'silent': 8, 'contradicts': 3, 'partial': 11} | by book: {'KLN': 10, 'MON': 6, 'POK': 5, 'WEB': 5, 'BQT': 4, 'WLD': 3, 'IEC': 3, 'SKT': 3, 'ARY': 3, 'BRT': 2, 'LAT': 2, 'HRN': 2, 'AHD': 1}
```


## [2026-09-14T02:12:12.242Z] AGENT

Page 446 (book p. 416) verified — `/home/sfmqrb/git/rishe/data/verification/page-446.json`, `verify_check.py 446` reports 16/16 nodes, 0 PROBLEM lines.

**Counts:** roots 2 confirmed; nodes 10 confirmed / 3 plausible / 3 disputed. Ref checks: 14 supports, 2 partial, 3 not_checked. Entry 2 is a redirect (skipped).

**Disputed**
- Ser 2 · #6 Greek `heros; Heracles` — Pokorny 910, Klein 724 and Watkins do derive hḗrōs from *ser- "protect", but Beekes (2010) rejects it: *hērōw- is impossible given the missing /w/ in Mycenaean; "probably Pre-Greek". Heracles = Ἥρα + κλέος, so it hangs on Hera, whose etymology is itself unsettled. Skeat gives a third (obsolete) etymology, Skt. vīra / L. vir.
- Ser 3 · #1 Sanskrit `sarat; hâra` — sarat- is fine (though Walde-Pokorny mark it "unbelegt", unattested); hāra- "necklace" is from √hṛ "carry, wear" (*ǵʰer-), phonologically incompatible with *ser- (which would give Skt. s-). Mo'in's own footnote in Borhan-e Qate' (vol. 4, p. 2305) says so, citing Monier-Williams. Mann (Nourai's source) has no Sanskrit hāra at all — he lists "Per. har", which Nourai seems to have promoted into a Sanskrit box.
- Ser 3 · #3 Avestan `hara` "mountain range" — belongs under Nourai's *own* Ser 2 on the same page: harā- is "watch, guard" from Old Iranian har- "watch over" (Iranica ALBORZ i; Wikipedia citing Pokorny 910), Harā Bərəzaitī = "the High Watch". The error is inherited from Mann IEC:1131, who filed it under sero "join, range, arrange" — misled by English "mountain *range*".

**Plausible:** Ser 2 #7 (unlabelled French pass-through = Hercule; no refs, but Persian herkul's shape proves French mediation); Ser 3 #2 Persian هار (word, gloss and the Sanskrit→Persian loan all confirmed by Dehkhoda/Mo'in — only the root attachment fails); Ser 3 #6 French "seri, seriyal" (the book prints Persianized forms, not French *série/sérial*).

**Extraction errors for the owner:** none. The page image (copied to `data/verification/sources/refs/ocr/BOOK/446.png`) matches the JSON throughout, including "seri, seriyal". Two notes, neither an extraction fault: (1) each chart has one large *unlabelled, empty* box to the right of its Avestan node which the extractor does not carry — nothing is lost; (2) Nourai's Ferdowsi shāhed reads "گزیده سواران برون از شمار" where Borhan-e Qate' prints "کزید از سواران برون از شمار" — a variant in the book, faithfully extracted.

**Unavailable reference:** VOP:212 (Moshiri, *Farhang-e Vāzhehā-ye Orupāyi dar Fārsi*) — no digital copy exists; nodes #6/#7 of Ser 3 were checked against Mo'in instead. MON page numbers could not be confirmed (6-vol pagination is not online), but every cited entry was located and quoted.
