# Verification process log — verify-page-466


## [2026-09-14T02:27:47.876Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 466 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-466.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-466.json. Write /home/sfmqrb/git/rishe/data/verification/page-466.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 466` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:49.011Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:49.800Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:49.813Z] TOOL RESULT

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


## [2026-09-14T02:27:50.240Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-466.txt"
}
```


### [2026-09-14T02:27:50.265Z] TOOL RESULT

```
1	=== PDF page 466 (book page 436) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Spek : to look, examine  (refs POK:984)
4	#1 (parent #0) [Avestan] refs=POK:984 | spasyeiti : to observe, watch, wait on (serve) ; spas, spasânô : guard, watcher
5	  #2 (parent #1) [Pahlavi] refs=HRN:154 | spâs : to serve, wait on
6	    #3 (parent #2) [Persian] refs=BQT:1086 | sepâs «سپاس» : thanks
7	  #4 (parent #1) [Pahlavi] refs=SNS:117 | pâsbân : guard, police
8	    #5 (parent #4) [Persian] refs=SNS:117 | pâsbân «پاسبان» : policeman
9	#6 (parent #0) [Latin] refs=AHD | specere : to look at
10	  #7 (parent #6) [English] refs=None | respect ; suspect ; expect ; inspect ; specimen ; spectrum ; special ; species
11	#8 (parent #0) [Greek] refs=AHD | skopos : one who watches ; epi-skopos : one who oversees, a bishop ☞Epi
12	  #9 (parent #8) [Old Persian] refs=MON:1901; FSF:228 | skuba : bishop, priest
13	    #10 (parent #9) [Persian] refs=MON:1901; FSF:228 | sekubâ «سکوبا» : a Christian bishop
14	    #11 (parent #9) [Arabic] refs=MON:270 | osqof : bishop
15	      #12 (parent #11) [Persian] refs=MON:270; FSF:44 | osqof «اسقّف» : bishop
16	#13 (parent #0) [Latin] refs=AHD | micro-scopium : showing small objects ☞Gwei ; tele-scopium : showing far objects ☞Kwel ; peri-scopium : showing around ☞Per 1
17	  #14 (parent #13) [French] refs=None | 
18	    #15 (parent #14) [Persian] refs=MON |  «تلسکوپ» ;  «میکروسکوپ»
19	  #16 (parent #13) [English] refs=AHD | scope ; microscope ; telescope ; periscope
20	#17 (parent #0) [Germanic] refs=AHD | spehôn
21	  #18 (parent #17) [English] refs=None | spy ; espionage
22	
```


## [2026-09-14T02:27:52.996Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-466.json",
 "description": "Read source JSON for page 466"
}
```


### [2026-09-14T02:27:53.039Z] TOOL RESULT

```
{
  "pdf_page": 466,
  "book_page": 436,
  "entries": [
    {
      "root": {
        "name": "Spek",
        "lang": "Indo-European",
        "refs": "POK:984",
        "gloss": "to look, examine"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:984",
          "words": [
            {"translit": "spasyeiti", "gloss": "to observe, watch, wait on (serve)", "script": null},
            {"translit": "spas, spasânô", "gloss": "guard, watcher", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:154",
          "words": [
            {"translit": "spâs", "gloss": "to serve, wait on", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1086",
          "words": [
            {"translit": "sepâs", "gloss": "thanks", "script": "سپاس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:117",
          "words": [
            {"translit": "pâsbân", "gloss": "guard, police", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "SNS:117",
          "words": [
            {"translit": "pâsbân", "gloss": "policeman", "script": "پاسبان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بیار باده که در بارگاه استغنا - چه پاسبان و چه سلطان چه هوشیار و چه مست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "specere", "gloss": "to look at", "script": null}
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
            {"translit": "respect", "gloss": null, "script": null},
            {"translit": "suspect", "gloss": null, "script": null},
            {"translit": "expect", "gloss": null, "script": null},
            {"translit": "inspect", "gloss": null, "script": null},
            {"translit": "specimen", "gloss": null, "script": null},
            {"translit": "spectrum", "gloss": null, "script": null},
            {"translit": "special", "gloss": null, "script": null},
            {"translit": "species", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "skopos", "gloss": "one who watches", "script": null},
            {"translit": "epi-skopos", "gloss": "one who oversees, a bishop", "script": null, "see": ["Epi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Old Persian",
          "refs": "MON:1901; FSF:228",
          "words": [
            {"translit": "skuba", "gloss": "bishop, priest", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:1901; FSF:228",
          "words": [
            {"translit": "sekubâ", "gloss": "a Christian bishop", "script": "سکوبا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نوشتند نامه به هر کشوری - سکوبا و بطریق و هر مهتری",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "Arabic",
          "refs": "MON:270",
          "words": [
            {"translit": "osqof", "gloss": "bishop", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:270; FSF:44",
          "words": [
            {"translit": "osqof", "gloss": "bishop", "script": "اسقّف"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "به اسقف چنین گفت کای دستگیر - زایران یکی نام جویم دبیر",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "micro-scopium", "gloss": "showing small objects", "script": null, "see": ["Gwei"]},
            {"translit": "tele-scopium", "gloss": "showing far objects", "script": null, "see": ["Kwel"]},
            {"translit": "peri-scopium", "gloss": "showing around", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": null, "gloss": null, "script": "تلسکوپ"},
            {"translit": null, "gloss": null, "script": "میکروسکوپ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "scope", "gloss": null, "script": null},
            {"translit": "microscope", "gloss": null, "script": null},
            {"translit": "telescope", "gloss": null, "script": null},
            {"translit": "periscope", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "spehôn", "gloss": null, "script": null}
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
            {"translit": "spy", "gloss": null, "script": null},
            {"translit": "espionage", "gloss": null, "script": null}
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


## [2026-09-14T02:27:55.554Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','SNS','BQT','AHD','MON','FSF','WLD','KLN','PHD','NYB','BRT','KNT','HUB','ARY','IEC','SYN','SKT','FSD','WEB','CHEUNG','FVQ','AFM','PLA','LKT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-14T02:27:57.229Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

CHEUNG null

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries:
```


## [2026-09-14T02:28:13.469Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T02:28:13.512Z] TOOL RESULT

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


## [2026-09-14T02:28:15.478Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-385.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:1500]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2000])\"",
 "description": "Check example verified file"
}
```


### [2026-09-14T02:28:16.626Z] TOOL RESULT

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
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ر
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "pakša",
 "verdict": "plausible",
 "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
 "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
 ],
 "ref_check": [
  {
   "ref": "AHD",
   "status": "partial",
   "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 792 (POK_03 leaf 25)",
   "stance": "partial",
   "note": "'Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"' — shoulder/wing/side, not breast."
  },
  {
   "src": "KLN",
   "where": "1966 ed. p.1272 s.v. punka (leaf 678)",
   "stance": "partial",
   "note": "'fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\", which is possibly cogn. with Lett. paksis, \"corner of a house\", Russ. pach, \"flank\".' Klein too has no 'breast'."
  },
  {
   "src": "WLD",
   "where": "WP II 3-4",
   "stance":
```


## [2026-09-14T02:28:24.877Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','SNS','BQT','FSF','AHD','MON','PHD','NYB','BRT','WLD','KLN','SKT','IEC','SYN','HUB','ARY','FVQ','AFM','PLA','LKT','KNT','FSD','WEB']:\n  v=d.get(k) or {}\n  print('==',k,'| local:',v.get('local_file'),'| offset:',v.get('page_offset'),'| hint:',str(v.get('lookup_hint'))[:300])\n\"",
 "description": "Print offsets and local files"
}
```


## [2026-09-14T02:28:25.682Z] TOOL CALL #8: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80",
 "description": "List refs dir"
}
```


### [2026-09-14T02:28:25.979Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== SNS | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== FSF | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt'] | offset: 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking | hint: grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== FVQ | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== AFM | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== PLA | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== LKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
```


### [2026-09-14T02:28:26.020Z] TOOL RESULT

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
KNT_full.txt
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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
```


## [2026-09-14T02:28:31.947Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full spek ===\"; grep -n -i -A12 \"lemma: spek\" POK_full.txt | head -60\necho \"=== POK_03 spek- ===\"; grep -n \"spek̂-\" POK_03.txt | head -20; grep -n \"^spek\" POK_03.txt | head\necho \"=== AHD watkins spek ===\"; grep -n -i -A25 \"^spek-\" AHD_watkins1985.txt | head -60",
 "description": "Grep Pokorny and Watkins for spek-"
}
```


### [2026-09-14T02:28:32.054Z] TOOL RESULT

```
=== POK_full spek ===
=== POK_03 spek- ===
3040:spek-   ,spähen,   scharf   hinsehen';   spek-s,   spek-ön-,   spek-tor-  ,Spähef^ spek-to-  ,erspäht*,  spok-o-s  , Späher'.
=== AHD watkins spek ===
```


## [2026-09-14T02:28:35.056Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD spas/pas ===\"; grep -n \"^spās\\|^spāh\\|^pās\\|^pāsbān\\|^pahikār\" PHD.txt | head -20\necho \"=== NYB spas ===\"; grep -n -i \"spās\\|spas-\\|pāsbān\\|pās \" NYB_vol2_glossary.txt | head -30\necho \"=== BRT spas ===\"; grep -n \"spasyeiti\\|spas-\\|spasan\\|spaš\" BRT.txt | head -40",
 "description": "Grep Pahlavi/Avestan dictionaries"
}
```


### [2026-09-14T02:28:35.193Z] TOOL RESULT

```
=== PHD spas/pas ===
567:spās dástan 76 sród
4779:spāh ALY Q335 dēbahr, spihr, Nay LAKE spaxr spahbed VP OR 0335 spas ts” суз? spāsdār Nee es. spāsdārīh uA a soda) spāsešnās TO Put 0335 debàg VW ett spāsūmand ? v€ Pus” q335 spāš AV суз?
=== NYB spas ===
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
455:an-ispās [’nsp’s] disobedient 901% (andar to). — Paz. anaspäs, v. spas; ispds with prothetic vowel is NW form.
2151:8513 in such wise that; pat hàn äivenak ka so that 1127; — final: i ka... mē lest 895; — ; ka explicative: wiz. that’ 824; — han i ka forms substitutes for an inf. or an abstr. vb. n.: né matan + čišan 6 den u...hānika... anispās būt hénd their not coming to the Religion and their having been disobedient 9015-16; hac han tka... bé brinénd from their cutting it (the Haoma) 947-3; hac hàn 4 ka-ščin ... bē kušēnd from slaughtering them (the cattle) 9412-13; — in some cases ka seems to be pleonastic: hakar né ka dyét if he does not come 20%7; kāc ka would that
2734:the pronunciation nikér- < *ni-karyati (of the same type as the syn. spas-: spasyeiti ‘he espies, finds out’, cf also Skr pasyati), which also accounts for Paz. NP nigar-, niger-, ci men(itan) < *manyati: Paz. manidan, minidan. Hübschmann, PSt. 102, no. 1038, nikir- < *nikriya- (better *nikrya-), accepted by Bthl; I disagree. - Arm. lw. *nkirt- (< *ni-kirt-) in nkrt-em ‘to strive for, to care for’ in the N. T., Ep. ad Philipp. 31%. — To be combined with 2kartan; cf also Skr kal- ‘to observe, to mean, to consider’.
3483:spas [sp’s] 1. thanks, gratitude 127%. 7026. 90°, — 2. service: vasdn vazurg ~-dn (cas. obl. as a subj.) many men serving in high positions (bahuvrihi) 1061; v. also šnās. — MPrth 'sp's ‘service’, Arm. lw. spas id.; MPrs ‘sp’s ‘service’ (S), ’sp’s ‘thanks’ (A-H II); Paz. spas with the bizarre Skr. v. tridhä-praharaka ‘threefold watch’ based on a popular etymology (sé ‘three’ + pds, g. v.); NP sipäs 1. ‘grace, favour’, 2. ‘praise, thanksgiving’; from Av. (1614) spas- ‘to observe, to attend’. — V. an-ispäs.
3654:šnas [Sn’s] pres. st. of šnāxtan, in com- pounds: spās-šnāsān (pl. cas. obl.) those understanding service = having service as their profession 71!, v. späs.
4005:frasang many parasangs 7%; ~ simén, ~ asp névak 1965; — with a personal subst.: —-än martöm (cas. obl.) 418, but also ~ frazänak martom (cas. obl.) 455; ~ āzātān u vazurgän (cas. obl.) 16°; ~-dn vazurg-spāsān (for cas. rect.) 1061; — less often placed after its subst. without or with the izGfat: névakéh ~ 351; anākēh ~ 95* (as against pat ~ andkéh 761); hesm i ~ 4815; gāvān + ~ 483-26; aspān i ~ 4013, — 2. as a pred.: numerous, great 41, 201? sq. 871; — in a compound: hesm ~ quick to anger 1074. — 3. subst. pl. cas. obl: 6 ~-dn to many people 3643 and passim. — 4. adv. very: ~ vazurg 8’; ~ pahréc 55°; — ka —-ic however much 463, 8122-23, 9112. — OP vasiy; MPrthPrs ws; Paz. vas; NP bas.
5344:spas-: spas
6355:anaspās: anispās
=== BRT spas ===
7025:frasüsat  ar?dvT  . .  J"  aoxta  ar)dvi  Yt5. 8;  V.  :ji.\2  2St;  —  äat  (s.  8)  ml paoiryäi risväi  xsafne  atars  .  .  nmSnS.paitim yHsaiti  .  .  iV  ml  bityiii  . ,  v<lstrlm  /suyan- t>m  yasaiti  .  .  ä'  tnl  ^rityäi  . .  sraosfm yäsaiti  V.JtV.iS— 22;  —  itir&  mt^rahe frayana  (sd.)  ,  .  ä°  hva  pasu  vfra  vasö.- xsa^rö  fracaraitt  (sd.)  Yt/0.  112;  — miiir^m  .  .ynihe..frada%at  ahurö  mazJit balvari  döthiariqm  .  .  ii°  nbyö  döiiräbyö ..spasyeiti ..  ä'  '..\Llo.Zz;  28,101  (vor j-a/), /J.68,  H.2.10,  i4iSt,P.jiS'2St(vor
13320:Undeutlich:  aiväcina  "Um  'vTn/tn'^al N.5^';  —  f^i!  avacinS  'Um  "vTnifl  i^.^^*, —  yaia  'tya  spasanya  N.  8. KompA.,  E-i  Ableit,  —  Ableit.  aus  'däla-.  — mp.  vgl.  däßi.  —  Fa.:  Jälthä,  (10  V.  65)  erl.: iaiid  afäyfl;  (zu  N.  /qf  l.  St.):  dälUlM.  ' Vt /);  auigelassen;  a.  noch  No.  3. —  O aiäiiyöi  s.  aber  Pü.  —  ')  NA,  'tyayäi;  s,  iber K  1  usw.  —  3)  Pü.;  fehlt.
16493:•  j.  baevar«.spasan-  Adj.  'der  zehn- tausend Späher,  Wächter  hat',  von  Mikra: mi%rs  .  .  yS  'sanS  (NS,)"'  Yt  to.  24;  — mi^rB  .  .  yS  'sänö  (NS.)"  Yt  10.  60.
20531:*drazimnö  Yt70.  gsf.;  15;  —  aat  äbyB döi^mbyS  .  .  a<,aoyB  asti  °rff  yB  balvar^.- spasanB  ,  .  Yt/o.  81;  —  'mm  y7  paoiryB tarö  harqm  asnatiiti (sd.)  paurva.natmäi.. kü  yat  auniatjtspa/ie  . .  ahäi  vüptm  ädi- haiti  Yt;o.  13;  — gairinqm  asasflüfrattqm *äsnaeiti  (sd.)  'rsm  (statt  NS.)  AuzaOum V,  7p.  28;  — yttiAf  asta  rätayB  vupahu paiti  banzahu  spasB  äahäire  'rahe  Yt 70.45;  —  ''^"^  -  ■  yeÄhe  paurva.nal>i>3t vazaite  vrn^rayt^  ahur«i'MltBY\.io.-;o;  — yat  duzdä  fradvaraiti  . .  %wäs>m  *yi//yeiie vahm  'rB  Vt70.  52; — yal  'rö  fravazaite avi  haüiayä  xrri/yäti/  .  .  a^ra  narqm mi^rBJrujqm  apql  gavö  darfzaydti  Yt 70.48;  —  ui^ojanä  'räi  .  .:  äi  'ra  .  . ime  HB  .  .  aspa  para  *'ra  *i3a'*  aayetite ime  nB  *wyra  bäzava  karata  'ra  sHnda- yeinti;  pascalta  dis  fraspayäti  'rB  Ytio. 4a  f.;  —  'r^m  .  ,  yetihe  ,  ,  bäzava  fra- griwmü  "mi^rBMüjauhB  (sd.)  .  .yatHt  vi- maibJm  (sd.)  airiha  zamS  t?mat  'rö  han- gn/simiiö  *pairi.apaya  (sd.)  Yt/0.  I04£; I —  'rB  zayüt  (iÄ^  sara%u3r?m  Y.g.i PUZ.         a)  bes.  mit  dem  Beiwort  z'ouru-
20892:*kay  und  /a  (Sp.  426  o.)j  a)  im  %P^vi .■,\vahistäii  Y._J5.4.  b)  im  jAw.;  I)  im zu  2  A  i:  mainyQm  .  .  Virmli  .  .  yasti^'' ,  Nominativ  oder  dem  ihm  gleichen  Akku- ciscä  spsiiiitö  Y.  4;^.  16;  ■ —  zu  2  B: !  sativ;  alte  hier  verzeichnetenStellenkÖnnen yöi  tnsi  ahmäi  straehm  datt  layas-  auch  zu  I  gestellt  werden ;  a)  NSm.:  mvhrd (sd,)<?ii  upä-jimmisA.)  Y.45.  5;  —  asaum\y5  vouru.gaoyaoitü  (Stverz.)  Vt/0.3;  V. cöiS  (Sp.430  o.)  yS  »X  cläl  vahüta  'Y.47-  32. 19,  zo;  —  mihrö yö  bafi'Orp.spasanB 5;  verwendet  Y./2. 1.  B)imjAw.;  zu  sSrffvtspif.v^vä  alaayamfisYi.10. 24;  gS^; I  2  k:  *spayeiH  vTspa  t3  syaokna  yä  cua\  —  mi^rS  ys  vouru.gaoyaoiti^ yS  srut^aosS virtzyäti  V.J.  41;  —  zu  1  /  g;  yS  ciica\y.X.  ip.3S;  —  paurvS  ys  vifrS  navazS  Vt. ahmt  nmaiie  yö^  .  .  ama»hä  asti  masyi\^,(ii\  —  mq%r5  spititS  yS  as^annä  V. ..pairi  :lfusi  pjr)asili  Y.g.aS.  4)mit|22.2;  —  datvasÜa  yö  apaosS  Yt8.23; fönendem  ka-  und  üt  (Sp.  426  o.);  nur.  21,  23;  —  ätari ys  upasuxtö  Yt.  10.  127; a)  im  gAw.;  zu  I  2  a:  Äf3  .  .  ^?  . . '  52,  100,  127,  5.76,81.93,  ä  34,  ^2.  6, dalnqm  .  .  *sär3stä  .  .  kascll  Y.  4^.  J;  —  z^.  3,  4,  21,  17.  16^,  V,  2.  29;  —  masda zu  l  2  e:  siraesS  JantB  ahmät  y ahmäi xys  siviits  vtr?^raja  ..  Y-S^-y,  —  vairü vasi  kahmaicit  Y.  44. 16;  43.  i;  —  zu|^5  haosravä  nqma  Yt.  ig.  56;  59,  66, I  2kl  ^yaöhamU . .  paityaogst  ta  ..ya  Im    V.  18.  15;    —    azfm  (Stverz.)    yS    ahurU
26861:•  j.,  g.  'spas-  V.  'spähen'.  Praes.  s hispas-,  10  '^spasu-Q)'^,  11  spaln-,  26 sparya:   —    PPfP.    'spasta-.  [S.   noch
26883:•  j.  'spas-  m.  'Späher,  Wächter':  spai INS.)  viftaHa  .  ,  mihrS  Yt  10.  46;  — iiii'irfm  ..  zamarthunt3m  spastm  Vt.  70. 61;  —  ydAhe  asta  rJtayS  .  .  spasS  (NP.) atühnirt  mihrahe  YL/0.  45.
26884:Zum  V.  spas-.  —  ai.  späi-  m.
26885:•  j.  spasan-  Adj.  Iiinspähend  (auf  — )';
26888:"spasanya
26894:•  j.  ya%a  daitya  "spasanya  N.  6":  -  ?  -. PO, :  ta  dätihä  fäipätt.
26895:•  j.  spasyant-  Adj.,  PPA.:  s.  spas-.
29703:mihrasca  .  .  yö  baivanspasanS  'ra^aosö  mihrS)  antan  dakyu  Yt  10.  117.
```


## [2026-09-14T02:28:41.963Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_03 around 3040 ===\"; sed -n '3010,3075p' POK_03.txt\necho \"=== which leaf ===\"; python3 -c \"\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 3040\nimport re\nidx=sum(1 for l in lines[:3040] for _ in [1] if False)\npre='\\n'.join(lines[:3040])\nprint('leaf(0-based ff count):',pre.count('\\f'))\n\"",
 "description": "Print Pokorny spek- entry"
}
```


## [2026-09-14T02:28:42.931Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD spek ===\"; grep -n \"spek\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins for spek"
}
```


### [2026-09-14T02:28:43.089Z] TOOL RESULT

```
=== POK_03 around 3040 ===
z.  T.  auf  einem  Präs.  *sp9-nö  und  sp9-nu6  beruht  wohl  die  germ.  SippA ahd.  spanan  ,locken,  reizen'  (,*anziehen*),  as.  spanan  ,locken,  veranlassei antreiben',  ags.  spanan  ds.,  ahd.  spannen  {*spanjan)  ,verlocken,  anreize* =  aisl.  spenja  ,verlocken,  überreden*,  norw.  spana  (*spanön)  ,spaiin£ strecken',  span  m.  , Spannung*,  ahd.  spanst  , Antrieb,  Reiz,  Lockung*»  \ gi-spanst , Verlockung,  Trug',  mhd.  {ge)-spenst , Verlockung,  teuflisches  Truf» bild,  Gespenst',  nhd.  abspenstig  machen,  widerspenstig]  mhd.  spän  ,Zwi|i Streit,  contentio'  (*spe-n-),  widerspän  ds.,  lüiderspmne  , widerspenstig*;  ahi  i spannan  (*sp9nuö)  , spannen,  anspannen';  intr.  ,sich  dehnen,  gespannt  io  i erwartungsvoller  Spannung  sein',  mhd.  spannen  ds.;  ags.  spannan  ^spannen, festbinden,  anfügen*,  mhd.  span,  -nnes  , Spannung,  Zerwürfnis,  Zwist*,  ahi spanna,  ags.  spann  f.,  aisl.  spqnn  f.  , Spanne',  Kaus.  aisl.  spenna  ,uia*  -* spannen,  umschließen,  drängen*,  mhd.  spennen  , spannen,  dehnen';  ein* germ.  Gutturalableitung  dazu  in  nhd.  Spange-^  ahd.  spanga,  ags.  spang  dt^ aisl.  spgng  , dünne  Platte,  Eisscholle';  spanst  wird  germ.  Bildung  von  spanan aus  sein.
Auf  einem  ^o-Partiz.  *spd't6s  mit  der  Bedeutung  von  lat.  tenuis  ,dünn, auch  wässerig,  von  Flüssigkeiten'  beruht  wahrscheinlich  aschwed.  spcedhir , schmächtig,  zart,  jung',  schw.  späd,  dän.  spced  ,zart',  aisl.  spa^, dünne  Suppe*;
dieselbe  Bedeutung  ,tenuis'  mit  z-Vokalismus  in:
gr.  GTZL-vög  ,mager';   air.   seim  (*sptimi-)  ,exilis,  macer*,  seime  ,Dünn0'|
mit  Gutturalerweiterung:  gr.  anUavov'  GrtdvLOv  Hes.,  GjtLyy6fl fiiXQÖv,  ßgaxv  Hes.;  aisl.  spiki  m.  ,Meise';  schwed.  dial.  spikjin  ,dün% schmächtig,  mager*,  schwed.  dial.  spink  , schmächtiger  Mensch*,  norw.  spikm ,dürr,  mager,  geräuchert*  (aisl.  spiki-lax  ,gedörrter  Lachs*),  isl.  speikjß , dörren',  schwed.  spink  ,Splitter',  mnd.  spik  ,trocken*  (nhd.  Spick-aal  usw.)»
WP.  II  655 f.;  dazu  3.  sp{h)ti-,  1.  {s)pen-{d-)  und  {s)p{K)eu-d-.
w
983
p(/2)e(i)-,  spi-  und  spbe- :  spho-  ^gedeihen,  sich  ausdehnen  =  dick  werden, vorwärtskommen^  Erfolg  haben,  gelingen^,-  sphe-ko-  , Kraft',  sphe-ti- ,das  Gedeihen*,  sphs-ro-  , ergiebig^,  sphid-to-  , dicht  gedrängt', ^i.  sphäyate  ,wird  feist,  nimmt  zu',  Partiz.  spJiitd-  , geschwollen,   wohl- habend, dicht,  voll',  sphäta-  ,groß,  stark',  sphlti-  f.  ,das  Gedeihen',  sphäti-  f. Mästung,    Gedeihen',    Kaus.   sphävdyati  ,mästet,  verstärkt',   sphärd-   , aus- gedehnt, weit,  groß',  sphird-  , feist*  (idg.  *sphd-rö-  ==  aksl.  spoi-b,  ahd.  spar)] 0iit  Formans  -ko-  (wie  lett.  speks):  plva-sphäkd-  ,von  Fett  strotzend'; ai.  vi-spitdm  ist  strittiger  Bedeutung;
von  der  aspir.  Form  spAg-:  iQL-oq)r]Xov  „iQLa&evfj"^  HacpriXoi'  dad-evetg]  acprj'kdv yäg  '^0  ia')(yQ6v  Hes.;  ohne  s-  arm.  p'-artam  ,reichlich';
lat.  spatium  ,Raum,  Zeit,  Weite,  Strecke,  Dauer';  spesj  -el,  Fl.  speres  f. ^Erwartung,  Hoffnung',  sperö,  -äre  ,hoffe';  ursprüngl.  ,von  Hoffnung  ge- schwellt'; prosperus  ,günstig,  glücklich'  (*pro-spd-ro-) -^
mcymr.  ffysgiaw,  corn.  fesky  , Eilen'  (*spid-sk-) ;
got.  spediza  , späterer',  spedumists  , spätester',  ahd.  späti,  Adv.  späto ^jpät'  (eig.  ,*sich  hinziehend');
ags.  spöwan  , gedeihen,  glücken',  ahd.  spuon  ,gelingen*,  germ.  "^spödi- im  ahd.  spuot,  as.  spöd,  ags.  sped  ,Gedeihen,  Beschleunigung,  Eile',  nhd. sich  sputen]  ahd.  usw.  spar  s.  unten;
lit.  spki  ,Muße  haben,  schnell  genug  sein,  imstande  sein',  sperus  ,flink', spUas  m.  ,Muße',  speml  f.  ,Eile';  splkas  und  spekä  , Kraft';
lett.  spet  ,vermögen,  können',  speks  ,Kraft,  Stärke,  Macht'  (wohl  auch lett.  spXte  , Trotz',  spitigs  , trotzig');
aksl.  spSjg^  speti  , Erfolg  haben';  sp^ch^  m.  , Studium',  spesiti  , eilen';
aksl.  sporz  (=  ai.  sphird-  usw.)  , reichlich',  in  neueren  slav.  Sprachen auch  (und  wohl  das  ursprünglichere)  ,lange  dauernd,  lang  ausreichend', so  Tuss.  spöryj,  serb.  spor  ,lang  dauernd',  daher  anderseits  auch  ,lange ausreichend,  sparsam',  dech.  spory  , ergiebig,  ausgiebig*  und  ,sparsam,  spär- lich', spofiti  ,sparen'  (dt.  Einfluß?),  ahd.  spar  , sparsam,  knapp',  ags.  spcer, aisl.  sparr  ,sparsam,  karg'  (:  spor^) ;
hitt.  ispäi  ,ißt  sich  satt',  3.  PL  Upiianzi.
Von  spi'  (:  spei-)  aus :
mit  der  Bedeutung  ,fett,  dick'  und  ^-Formans :  ai.  sphij-  (Nom.  Sg.  sphik, Du.  sphijäu\  sphicäu  durch  Entgleisung  nach  d.  Nom.  Sg.?),  sphigl  , Arsch- backe, Hüfte';  aisl.  spik  n.,  ags.  spie  n.,  ahd.  spec,  -ckes  ,Speck' ]
Mit  Dentalformantien:  gr.  aftldvoq  , ausgedehnt,  weit,  eben',  otzi- ^dsLg,  OTtiövög  (Hes.)  ds.,  amdöd-sv  ,von  weitem',  sXsa-la'j^Lg,  -crtidog ,Sumpffläche',  äoTtidrig  {^av-üTtiörig  mit  Präp.  äv)  , geräumig',  äoTtlg,  -Idog ,Schild',  (,*dem  Körper  entlang  gebreitete  Fläche'  ?),  otzl^o)  '  „^xTfitVw" ;
984  •
lat.  spissvs  (*spid'to-)  , dicht,  dick,  langsam,  zögernd*;
mit  dh:  artL^ci^r}  , Spanne  (der  Hand)S  omd-lai'  oaviöeg  vedyg  Hes.*^-
mit  t:  lit.  speiHü,  spetsti  ,umringen',  spiesti  ^schwärmen',  spintü^  l^L .  ,in  Schwärmen  ausbrechen,  von  Bienen*^,  lett.  sjpiets  »Bienenschwarm*  fpw^  j tiz.  lit.  sputas  ^gedrängt*,  lat.  spissus) ;  vgl.  auch  lett.  spaile,  spailis  ,Stri*L  \ Schwaden  des  Mähers^  {-l-  vielleicht  aus  -dl-),  lit.  spielöti  ,in  den  J^  ^ rahmen  einspannen^  lett.  spailes  ^gespaltener  Stecken  zum  Einklemme spihj  spUis  ,eine  Zwicke,  Zwickeisen;  Holznägel;  Not,  Verlegenheit  (n>tj* Lw.?),  spilis  auch  ,zeltartig  ausgespannte  Leinwand'^  spilet  ,klemmeiK. zwicken,  spannen*.
Mit  ^--Formantien :
gr.  acplyyiü  ^schnüre  ein,  klemme  ein^,  aq)Lyy,Ti^Q  , Schnur,  Band;  Musk^J*.
lett.  spaiglis,  spaigle  , Krebsgabel';  germ.  mit  der  Bedeutung  ,ausspannti =  spreizen* :  nhd.  dial.  spaichen  ,ausschreiten^;  ausspaichen  ,mit  Schrittii oder  ausgespannten  Fingern  ausmessen',  norw.  speika  ,mit  steifen  fe». spannten)  Beinen  gehen',  splka  , widerspenstig  sein*.
WP.  II  656  ff.,  WH.  II  568  f.,  576,  Trautmann  274  f.,  Vendrjes  RQ. 50,  92,  Vasmer  2,  707,  710;  dazu  2.  spei-  und  1.  spen-.
spek-   ,spähen,   scharf   hinsehen';   spek-s,   spek-ön-,   spek-tor-  ,Spähef^ spek-to-  ,erspäht*,  spok-o-s  , Späher'.
Ai.  spdsati  (Dhätup.),  pd^yati  , sieht',  Partiz.  spastd-  (=  av.  spaHa-^  \gi spectus)^  spat  ,Späher*  (=  av.  spas,  lat.  au-,  haru-spex)^  spdsa-  ds.  (:  p.  . aM7i6g)y  av.  spasyeiti  ,späht^  (==  lat.  speciöy  gr.  ayisnro^aL),  spas  ,Spähei^  ^ spaSiar-  ds.  (=  lat.  -spector^  umb.  spetur-e),  spasan-  ,hinspähend  auf*  (=  ahd. speho  ,Späher*);  arm.  spasem  ,ich  erwarte'  ist  iran.  Lw. ;
gr.  aneTttoiiai  ,schaue'  {av.En-  umgestellt  aus  *sjpeÄ:-);  ayi.oitog  ,Späher| Ziel*,  G-aorteTv  »beobachten,  zielen,  untersuchen',  ayconrj,  G^ionid  ,Wart«\ axhpig  ,Betrachtung* ;  alb.  pashe  ,ich  sah'  (*[s]pok-s-  ?);
lat.  speciö,  -ere,  -xi,  -dum  ,sehen*  (con-spiciö  usw.),  spectö,  -äre  ,anschauen*, species  , Anblick,  Ansehen,  Aussehen,  Erscheinung*,  au-,  haru-spex]  specu$, -WS  , Höhle*,  speculum  , Spiegel',  speculor,  -ärl  ,spähen*;  umbr.  speture  jSpec- töri*,  speturie  ,spectöriae' ;
ahd.   spehön  ,spähen',    dazu  speha  f.   , aufmerksames  Betrachten,  Unte^ suchung.  Auskundschaftung,  Aufpassen*;  aisl.  spä  ,Wahrsagung*  {*spa1ai gr.  ayiOTtrj  ?  doch  weist  spä-  auf  Wurzelbetonung  und  ist  postverbalen  Ür Sprungs  verdächtig,  s.  Wissmann  Nom.  postv.  1,  41);  spä  , wahrsagen*  (*sp^  '^ hön,  s.  Wissmann  a.  a.  0.  1, 110),  spar  ,wahrsagend,  prophetisch*  {^spaha-iYf  - as.  ahd.  spähi  ,klug,  geschickt*.
WP.  II  659 f.,  WH.  II  570 f.;  vgl.  spe^-  , hinsehen*.
985
)pel'  J3,^t>  nachdrücklich  sprechen^;  (s)pel-no-  , Erzählung'. ^      ^rm.  afa-spel  jQsige,  Sprichwort,  Rätsel^;
got.  spül  n.  .Erzählung,  Sage,  FaheP,  aisl.  spjall  n.  , Erzählung,  Rede^, ^.  spell  n.  , Erzählung,  Rede,  Predigt^  (engl,  gospel  =  ags.  göd-speU)  ,Evan- t^elium';  ahd.  spei,  -les  n.  , Erzählung,  Rede,  Märchen',  ahd.  mhd.  bl-spel belehrende  Erzählung,  Fabel,  Gleichnis*,  nhd.  Beispiel]
davon  got.  spillön  ,verkündigen,  erzählen',  aisl.  spialla  ,reden,  erwäh- nend ags.  spellian  , reden,  erzählen'  (engl,  spell),.  ahd.  got-spellön  ,evan- (relizare^  mhd.  spellen  ,erzählen,  reden,  schwatzen^-
damit  sind  als  s-lose  Formen  vereinbar  gr.  ärteilrj  , Drohung ;  prahlerische Versprechung'  ((J/rfidfcu, drohe;  gelobe,  verheiße;  rühme  mich,  prahle^), falls  aus  "^äTvelvia,  worin  ä-  am  ehesten  die  Präp.  *ri  „h"]  (auch  germ.  -II- ^ohl  aus  -In-)  lett.  pett  ,schmähen,  lästern,  verleumden^,  paVas  (Plur.)  ,Ta- del,  Schmähung',  iz-paVu6t  ,tüchtig  ausschmähen^,  sowie  toch.  päl-,  päl- ,preisen'.
WP.  II  676  f.,  WH.  I  59,  Frisk  119  f.
l.  (s)p(-&)ei-  ,spalten,  abspalten,  absplittern,  abreißen';  sp(h)el-tä  , Brett'.
Ai.  sphatati  (Dhätup.)  , reißt,  springt  auf^,  sphatita-  ,gesprungen,  zerfetzt*, sphatikä-  ,Bergkristall'  (,sich  blättrig  abspaltend*),  *sphätdyati  ,spaltet*, belegt  das  Partiz.  sphatita- ;  sphutdti  , spaltet  sich,  springt  auf,  platzt,  reißt* (sek.  sphötati) ;  neben  diesen  ^-Präsentien  (:  ahd.  spaltan)  das  ^o-Partiz. sphuta-  ,aufgeblüht,  offen*  (:  got.  spilda)]  ai.  patati  , spaltet  sich,  birst*, pätayati  , spaltet,  bricht,  zerreißt*  (:  paiü-  ,scharf*.  gr.  ftXazvg  ,salzig*?  s.  u. *pltü-s) ;
phdlati  ,birst,  springt  entzwei*,  phdlakam  ,(*gespaltenes  Holz)  Brett,  Latte, Blatt,  Schild,  Holzbank*,  phäla-  m.  , Pflugschar'  (,zugespitztes  Aststück*?); apers.  Glosse  GTvaqa-ßaQai '  oi  ysQQoq)6QOi  Hes.  , schildtragend',  npers.  ispar, sipar  , Schild*  (ai.  jpharam,  spharam  , Schild*,  unbelegt,  wohl  aus  dem  Iran, und  im  Anlaut  nach  phdlakam  gerichtet);
gr.  acpaXdaasiv  xifiveiv,  yievtetv  Hes.,  acpdXa^  , Stechdorn*,  äonaXad^og m.  ds.  (,*woran  man  sich  reißt,  ritzt*),  ocpdXa^,  dacpäla^,  anaXa^,  doTtäXa^ ,Maulwurf*  (,die  Erde  aufreißend*),  GTcaXiGGSTai'  GTragaGGezai,  ragaGGSTai Hes.,  ^GTtaXov'  GzvTog  Hes.,  GJtdXavd-QOv  ,Schüreisen*;  GnöXia'  xa  itaqa- TdXöj^eva  igidia  drcb  rCov  gy^Xcjv  xibv  TtQoßaTwv  Hes.  (:  lat.  spolium),  att. OfcoXdg  , abgezogenes  Fell*  und  ,Überwurf  von  Leder,  Brustharnisch,  Mantel*, äol.  GTcaXlg,  att.  ipaXig  ,Schere*;  zu  Gq^aX&GGsiv  auch  GcpaXög  ,Fußblock  für Gefangene;  Wurfscheibe*  und  GcpdXXw  ,werfen  (ursprüngl.  mit  ,Prügeln*), schleudern,  stoßen'  und  , (zunächst  beim  Ringen)  ein  Bein  stellen,  im  Kampf behindern*,  woraus  ,zu  Fall  bringen,  schädigen,  täuschen,  betrügen'.  Med. ,wanken,  fallen,  sich  irren*,  dGcpaXrjg  »unerschütterlich,  ohne  sich  fortstoßen
986
zu  lassen'  —  ,T\ihig,  sicherS  a(paX€gög  ^schlüpfrig,  aq)(xXfxa  »falscher  Schritt»* Gcpüag  »Holzscheit,  Knüppel;  ausgehöhlter  Block,  Bank';  J  ■
aus  dem  Alb.  vielleicht  pale  ,Seite,  Partei'  {*polnä,  vgl.  aksl.  po?^  ,Seit» Ufer,  Geschlecht,  Hälfte') ;  popele  ,Felsstück,  Scholle^  plis  (*pZi-«iV)  ^^ schölle*,  plish  ,Schilfrohr'  (*pU-s{o-):
lat.  spolium  »abgezogene  oder  abgelegte  Tierhaut;  dem  Feinde  aW nommene  Rüstung,  Beute';
mit  ^Erweit. ;  ahd.  spaltan,  mnd.  spalden  ,spalten%  got.  spilda  {*8ptUi) ,Schreibtafel',  aisL  spjald  (*speltos)  ,Brett',  ags.  speld  ,Splint;  Holzsttlck* mhd.  spelte  ^abgespaltenes  Holzstück,  Handgerät  der  Weberei';  aisl.  spj^ spell  »Schaden'  {*spelpa-,  -i-),  ags.  spM,  spild  ,Vernichtung,  Ruin',  wotqö aisl.  spilla,  spella  ,verderben,  töten'  (*spelpjan^  *spelpön),  as.  spüdian,  j^ spildan  , vernichten',  ahd.  spildan,  spilden  , vergeuden,  verschwenden*,  ai^ spildi , freigebig';  germ.  t  in  mnd.  spelte  »gespaltenes  Stück*,  ostfries.  «poldr ds.,  germ.  *speltö  (daraus  lat.  spelta)  in  ahd.  spelza  vlat.  spelta  (woramt^ , Spelt';  engl,  spelter  ,Zink'  (*spaldiz-) -,  ags.  spaldur  ,Balsam'  (*spaldut^ , Ausfluß  aus  gespaltenen  Pflanzen') ;  n-Präs.  ags.  spillan  mhd.  spülen  ,spÄl. ten'  {*spelljan)j  wozu  ohne  s-  schwed,  fjäll  ,Schinnen  im  Haar'; spqlr  ,dünne  flache  Stange',  mengl.  spale  ds.,  mhd.  spale  , Leiterspros wahrscheinlich  (als  ,dünnes,  flaches  Holzstück')  ahd.  spuolo  m.,  isl. , Weberschiffchen',  norw.  spöle  , Spule'  (germ.  '^spölan-)-^  ahd.  spuola  (gen *spölön-)  ySpule^j  ,Röhre,  Federkiel';  ohne  anl.  s-i  aisl.  fjql  ,Brett'  (*|?e24)S
mit  <-Erweit.,  aber  ohne  s-  wohl  ir.  alta{i)n,  cymr.  ellyn,  acymr.  eli^ , Schermesser',  abret.  altin  gl.  ,ferula',  mbret.  autenn,  nbret.  aotenn  ,Sch( messer*  {^paltina)]  mcymr.  allaw  ,rasieren'  (^altä-mu-)]  J.  Loth  RC.  45,  171
lit.  spälisj  PI.  späliai,  lett.  spaVi  ,Flachsschäben';  lett.  spals  »Griff,  Hand- habe' ;  apr.  spelanxtis  , Splitter* ;
aksl.  ras-platiti  ,spalten'  {*poltiti,  vgl.  nhd.  spalten,  ai.  sphatafi),  plai%] „QocKog"  ,Fetzen',  poUno  ,Scheit  Holz',  polica  , Brett',  palica,  aruss.  paVAa, ,Stock',  russ.  ras-polöth  »entzweischneiden',  pöloth,  polth  »(abgeschnittene)! Speckseite',  poltina  , Hälfte',  aksl.  poh,  Gen.  -u  ,Hälfte,  Seite,  Ufer,  Q( schlecht';  abg.  plevq,  pUti  (russ.  polöt^)  ,jä.ten\  pUv eh  »Unkraut*;  *o-peli^ in  ßech.  oplen,  oplin  ,Gipf stock,  Rungenstock',  sloven.  opV^n  ,Wagengipfefr holz'  usw.;
mit  dem  v  von  pUoq  (*pelu5)  ist  zusammenzuhalten:  lett.  spalva  »Feder,'' Gefieder,    Haar',    spüva    , Hülse,    Samenwolle,   Wollgras',    spilv^ns   ,Bett- kissen'  usw. ;
toch.  A  spälik-j  B  spalk-  ,sich  anstrengen';
mit  {s)p{h)el-  ,spalten'  hängen  möglicherweise  zusammen:  pel-  ,Haut|l Fell',   spelg-  ,spalten',    splei-   ,spalten*,  plei-   ,kahl',  piek-  pleik-,   ,reißen'J
987
pleu(s-,  -k-)  ,ausrupfen',  plas-  ,abspalten'.
WP.  n  677  ff.,  WH.  II  571  f.,  577  f.,  Trautmann  204,  Vasmer  2,  398, flasdieck  Zink  u.  Zinn,  157  ff.
j  fs^p(h)el-  ,glänzen,  schimme^n^
Ai.  sphuliTdga-  m.  ,Funke^  (Erweiter,  eines  *sphuli  ==  arm.  pail,  idg. *sphcU-),  vi- sphuliTdga-  ds.,  vi-spulmgakd-  , Funken  sprühend^;  arm.  pail, Gen.  paüic  , Glanz,  Schimmer',  pailem  ,glänze,  schimmere^;  paipaiim, poipoUm  jglänze'.
^-Erweiterung  sp(h)el-g-,  nas.  (s)p{h)Ieng~:
lett.  spulguot  , glänzen,  funkeln*,  spulgis  ,der  Funkelnde  =  der  Morgen- stern^, spulgans,  spilgans  , schillernd,  glänzend';  nas.  germ.  *flinka-  ,flim- inernd,  auch  von  rascher  Bewegung'  in  nd.  (nhd.)  flink  ,rasch,  schnell', flinkem  , glänzen,  schimmern',  mhd.  kupfervlinke  ^Kupfererz',  ablautend (vielleicht  sekundär)  nhd.  flunkern  ,flimmern;  einem  etwas  vormachen', und  vielleicht  lett.  plafiga,  plunga,  pleüga  ,Brandblase'.
d- Er  Weiterung,  nas.  (s)p]end-,  (s)pl9nd-:
Gr.  GftXrjöög  m.  {afcXrjöd)  f.  Hes.)  ,Asche';  lat.  splendeö,  -ere  , glänzen, schimmern',  alit.  splend^iu,  splendeti  ,leuchten';  vielleicht  auch  air.  less {*lanssu-   aus    *phnd-tu-)    , Licht* ;    mir.    lainnech    ,glänzend'    {^phndiäko).
=== which leaf ===
leaf(0-based ff count): 225
```


### [2026-09-14T02:28:43.141Z] TOOL RESULT

```
=== AHD spek ===
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
979:in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
991:spreg-. To speak. Germanic *sprek-, *spek- (with Ger- manic loss of r) in: a. Old English specan, to speak: SPEAK; b. Germanic compound *bisprekan (*bi-, about; see ambhi) in Old English bisprecan, besprecan, to speak about: BESPEAK; c. Old English spréc, spéc, speech: SPEECH. [In Pok. (s)p(h)ereg- 996.]
1263:ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL  sel-4 ASSAY ag- ASSEMBLE sem-! ASSENT sent- ASSERT ser-3 ASSESS sed-1 ASSET sa- ASSEVERATE weéro- assIDUOUS_ sed-1 ASSIGN sekw-1 ASSIMILATE sem-1 ASSIST sta- ASSOCIATE sekw-1 ASSOIL feu-1 ASSONANCE swen- ASSORT ser-3 ASSUAGE swad- ASSUASIVE swad- ASSUME em- ASSURE cira ASTASIA sta- ASTATINE  sta- ASTER  ster-3
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1306:BISCUIT dwo-, pekw- BISHOP spek- BISHOPRIC reg-! BISON weis-
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1468:EPIBOLY gWele-1 EPIC wekw- EPICARDIUM kerd-1 EPICENE kom EPICRITIC krei- EPIDEMIC da- EPIDERMIS der-2 EPIDIDYMIS dwo- EPIDOTE do- EPIGASTRIUM gras- EPIGEAL gé EPIGENE gene- EPIGONE gene- EPIGRAM gerbh- EPIGRAPH gerbh- EPILEPSY (s)lag- EPILOGUE leg-1 EPIMYSIUM mis- EPIPHANY bha-1 EPIPHYSIS bheue- EPISCOPAL spek- EPISODE en, sed-2 EPISTASIS sta- EPISTAXIS stag- EPISTEMOLOGY sta- EPISTLE  stel- EPISTYLE sta- EPITAPH dhembh- EPITASIS ten- EPITHELIUM dhé@(i)- EPITHET dhé-1 EPITOME tem- EPOCH segh- EPODE wed-2 EPONYM nd-men- EPONYMOUS nd-men- EPOS wekw-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1486:EXxO- eghs EXOCRINE krei- EXODUS sed-2 EXOERGIC werg- EXONERATE en-es- EXOPHTHALMOS okw- EXORDIUM ar- EXOSTOSIS ost- EXOTERIC eghs EXOTIC eghs EXPAND pete- EXPATRIATE peter- EXPECT spek- EXPECTORATE peg- EXPEDITE ped-! EXPEL pel-6 EXPEND (s)pen- EXPERIENCE per-4 EXPERIMENT per-4 EXPERT per-4 EXPIATE pius EXPIRE spirare EXPLAIN pele-2 EXPLETIVE pela-1 EXPLICATE plek- EXPORT per-2
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1648:HORN ker-1 HORNBEAM ker-1 HORNBLENDE ker-1 HORNET ker-1 HORNITO gWher- HOROLOGE yér- HOROLOGY yér- HOROSCOPE spek-, yér- HORROR ghers- HORST kert- HORTATIVE gher-5 HORTICULTURE gher-1 HOSE (s)keu- HOSPICE ghos-ti- HOSPITAL ghos-ti- HOSPITALITY ghos-ti- HosT! ghos-ti-
1681:INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
1683:INTRA- en INTRADOS dorsum, en INTRANSIGENT ag- INTREPID  trep-1 INTRINSIC en, sekw-1 INTRO- en INTRODUCE deuk-, en INTROIT el-1, en INTROMIT en, (s)meit(a)- INTRORSE en, wer-3 INTROSPECT en, spek- INTROVERT wer-3 INTRUDE treud- INTUITION teu- INTUMESCE teue- INTUSSUSCEPTION en, kap- INULIN wel-3 INUNCTION ongw- INUNDATE wed-! INURE op-! INVADE wadh-2 INVAGINATE wag- INVALID! = wal- INVALID2  wal- INVEIGH wegh- INVEIGLE okw- INVENT gWa- INVERT wer-3 INVEST wes-4 INVETERATE wet-2 INVOKE wekw- INVOLVE wel-3 INWARD wer-3 IODOPSIN  okw-
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2180:REQUIEM kWeie-2 REQUIESCAT kWeia-2 REQUIRE quaerere REREDOS dorsum, re- RESCIND skei- RESCRIPT skribh- RESCUE kwét- RESEAU  era-2 RESECT sek- RESEMBLE sem-! RESENT sent- RESERVE ser-1 RESERVOIR ser-1 RESIDE sed-! RESIGN sekw-1 RESILE sel-4 RESIST sta- RESOLVE leu-1 RESORB srebh- RESOUND swen- RESPECT spek- RESPIRE spirare RESPITE spek- RESPLENDENT spel-2 RESPOND _spend- REST? sta- RESTITUTE sta- RESTIVE sta- RESTORE sta- RESTRICT  streig- RESULT sel-4 RESUME em- RESUSCITATE kei-3 RETAIN ten- RETALIATE telo- RETCH ker-2
```


## [2026-09-14T02:28:58.836Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT column context ===\"; sed -n '26840,26900p' BRT.txt | grep -n \"^[0-9]\\{3,4\\}$\\|161[0-9]\\|spas\" | head -20\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(26780,26900):\n    l=t[i].strip()\n    if l and (l.isdigit() or 'spas' in l.lower()):\n        print(i,repr(l[:120]))\nEOF",
 "description": "Find Bartholomae column numbers near spas-"
}
```


### [2026-09-14T02:29:00.096Z] TOOL RESULT

```
=== BRT column context ===
22:•  j.,  g.  'spas-  V.  'spähen'.  Praes.  s hispas-,  10  '^spasu-Q)'^,  11  spaln-,  26 sparya:   —    PPfP.    'spasta-.  [S.   noch
23:spasitay-^
24:1)  'hinspähen  auf—,  beobachten,  aus- spähen nach  — '  (Akk.);  spass  . .  mt^rahe *mikrS4rtijim  *hisps.s»mna''>  Yt/0.45; —  vispsng  anySng*mainy}us  spasya  dvaßa- nka  "alle  andern  beobachte  ich  mit  Feind- seligkeit des  Geistes"  Y.  44~  1 1 ;  —  tUlrJm .  .yim  ..  *uzyS.r>nt>m  *hisps.smti'^i'*  "den T.  . .,  nach  dem  sie  ausspähen,  wenn  er im  Aufgehen  ist"  Vt.  8.  36,  2)  'Acht haben  auf-'  (Akk.):  sraohm  ..ys äxsHüca urvaitiica  drujö  spasyS  spSnütahe  "den Sr.,  der  auf  Frieden  und  Verträge  der Dr.  und  des  heiligsten  (Geists)  Acht  hat" Yt.  i/,  14*'.  3)  'erspähen,  erblicken': aiwyas'a  yaoxsHbys  (sd.)  spasyäti  mi^rS.- zyam  Yl/o.  82;  —  dra/ir  hacä  rä'^pvis (sd.)  y^mp  'spas'uiä  (2PPA.)'I  fraidXm '"welch  Glück  ihr  bei  dem  Anhänger  der Drug  erblickt"  Y.  S3-  ^'
25:mit  aoi  und  ava  'erspähen':  nSit  dim  . . drva  .  .  ava.spa/tiäna  aoi  *ava,spasnsiti> "nicht  soll  ihn  der  Ketzer . .  durch  keinerlei Erspähen  erspähen"  Yt  11.  5.
44:•  j.  'spas-  m.  'Späher,  Wächter':  spai INS.)  viftaHa  .  ,  mihrS  Yt  10.  46;  — iiii'irfm  ..  zamarthunt3m  spastm  Vt.  70. 61;  —  ydAhe  asta  rJtayS  .  .  spasS  (NP.) atühnirt  mihrahe  YL/0.  45.
45:Zum  V.  spas-.  —  ai.  späi-  m.
46:•  j.  spasan-  Adj.  Iiinspähend  (auf  — )';
49:"spasanya
55:•  j.  ya%a  daitya  "spasanya  N.  6":  -  ?  -. PO, :  ta  dätihä  fäipätt.
56:•  j.  spasyant-  Adj.,  PPA.:  s.  spas-.
26825 '1612'
26860 "•  j.,  g.  'spas-  V.  'spähen'.  Praes.  s hispas-,  10  '^spasu-Q)'^,  11  spaln-,  26 sparya:   —    PPfP.    'spast"
26861 'spasitay-^'
26862 "1)  'hinspähen  auf—,  beobachten,  aus- spähen nach  — '  (Akk.);  spass  . .  mt^rahe *mikrS4rtijim  *hisps.s»mna''>  "
26863 'mit  aoi  und  ava  \'erspähen\':  nSit  dim  . . drva  .  .  ava.spa/tiäna  aoi  *ava,spasnsiti> "nicht  soll  ihn  der  '
26882 "•  j.  'spas-  m.  'Späher,  Wächter':  spai INS.)  viftaHa  .  ,  mihrS  Yt  10.  46;  — iiii'irfm  ..  zamarthunt3m  s"
26883 'Zum  V.  spas-.  —  ai.  späi-  m.'
26884 "•  j.  spasan-  Adj.  Iiinspähend  (auf  — )';"
26887 '"spasanya'
26893 '•  j.  ya%a  daitya  "spasanya  N.  6":  -  ?  -. PO, :  ta  dätihä  fäipätt.'
26894 '•  j.  spasyant-  Adj.,  PPA.:  s.  spas-.'
26898 '•  j.  spaSitay-"  £  \'Beobachten,  Be- trachten\': yaXsqmia  . .  mafyaka  aiwila^a- (sd)fa  \'ta^a^a  gairinam  nätnam  '
```


## [2026-09-14T02:29:01.134Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN sipas ===\"; grep -n -i \"sipās\\|sipas\\|spās\\|sp&s\\|sipäs\" HRN.txt | head -20\necho \"=== HRN pāsbān ===\"; grep -n -i \"pāsbān\\|pasban\\|päsbän\\|pās \" HRN.txt | head -20",
 "description": "Grep Horn"
}
```


### [2026-09-14T02:29:01.228Z] TOOL RESULT

```
=== HRN sipas ===
=== HRN pāsbān ===
1936:-wäne, z. B. päsbän^ suturwün, engust^wdtie,
2716:274. päs 'Schutz*, pasban^ päsTden,
```


## [2026-09-14T02:29:07.900Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:2716])\nprint('leaf for line2716 (0-based):',pre.count('\\f'), '-> printed p.', pre.count('\\f')-21)\nprint('\\n'.join(lines[2705:2745]))\nEOF",
 "description": "Print Horn entry 274 pās"
}
```


### [2026-09-14T02:29:08.994Z] TOOL RESULT

```
leaf for line2716 (0-based): 83 -> printed p. 62
mäde-gävän-t päde-es her yeh
mh^perver huved cn hirmäyün— 62 ~
271. päre ^ück, Teil'.
ai. pärd- *das Letzte' ; (^w, para- SchulaX?) ^) ; phlv.
pärak 'Stück; Geschenk (behufs Bestechung)', AV.
272. päzen *Bergziege*, päzen,
phlv. pacm (Bund.) ; bei. pädin, n. päsin 'Ziegenbock,
männliche wilde Ziege* (290).
273. päzehr 'Gegengift, Bezoar.
paiti + zehr (s. zehr No. 678).
274. päs 'Schutz*, pasban^ päsTden,
aw. pädra- 'Schutz'; phlv. pas (Bund.), pOspäti, vd.
13 (77); ai. pätra-.
274*»^* päsäyt 'bereit'.
paiti + sagten (s. No. 688) ; phlv. pasa/tan^ pasaxtak
(AV.).
phlv. palsäytan könnte auf die Praeposition pa (tipa)
deuten, doch vergl. phlv. j^^^^X (No. 275).
275. päsu% 'Antwort'.
aw. ^paitisahva- [paiti + [/'safih- hat zwar im Awesta
nur die Bedeutung 'beschwören') ; phlv. pasu/ ; arm.
patas/ani 'Antwort*.
276. päSne 'Ferse'.
aw. päsna- 'Ferse'; phlv. päsnak*^ ai. pdrsni-,
kurd. päsüne, päm, päme (ZDMG. 38, 55), päm (JJ.);
af/. pünda ; bei. pünzig, ptnz, n. pTz, pid (306) ; wa/.
päsna, sar. pu/nä 'Ferse'.
syr. LW. j^li/^B 'der Bimstein, mit welchem man
sich im Bade die Fersen reibt', de Lagarde, Ges.
Abh. 73.
277. päk 'rein', paktze,
ai. pavakd- 'rein, klar ; phlv. pak, päkih,
278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
paiti + alüden (s. älüden^ No. 42) ; phlv. pälüt (Bund.),
päz. pälJdan, pälaidan (West, Sik. gum.-Gl.).
bei. LW. palayag^ pälenay 'seihen, worfeln, reinigen'
(292).
^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
Mitteilung) verweist mich aber auf aw. parendi- (Indog. Forsch. I, 184)
mit der Grundbedeutung 'Füllser.— 63 —
```


## [2026-09-14T02:29:09.730Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# printed 154 -> leaf 175\nfor n in (174,175,176):\n    print('==== leaf',n,'(printed p.',n-21,')')\n    print(pages[n][:3000])\nEOF",
 "description": "Print Horn page 154"
}
```


### [2026-09-14T02:29:10.872Z] TOOL RESULT

```
==== leaf 174 (printed p. 153 )
— 153 —
bei. LW. sazag (237). Np. nüxte, säz sind vielfach
entlehnt, vergl. auch np. sä^t lieitzeug in arm. sa/teal
gesattelt*, ansa/t *ungesattelt' (Noldeke bei Hübsch -
mann, ZDMG. 35, 132 No. 37).
np. sd/ten ist eine Causativbildung zum Stamme sac-
(np. seztden).
689. {i)8är ^Schmerz, Leid*.
aw. sddra- 'Wehe, Leid*.
690. (2)-ÄÄr 'Kopf in nigün]sar^ sebuk]sar etc.
aw. sära-, särah- *Kopf*; phlv. vergl. sar[var 'Helm\
Vergl. No. 726.
691. 8äl 'Jahr*.
aw. sare^a- 'Jahr*; phlv. sal, sälak *alt\ arm. LW.
nava]8ard, graecisirt (nicht lydisch, vergl. G. Meyer,
Indog. Forsch. I, 326) i'for adodiv (Job. Lydus), chald.
LW. "»TlDli (de Lagarde, Öemitica I, 65), ;K''ärezm.
nau^arjT (Nöldeke, Pers. Stud. I, 34); skr. gardd-
'Herbst, Jahr (mit Zahlen)'.
oss. d. särdä, t. särd 'Sommer* (223).
Allg. entlehnt: kurd. af/. bei. (235) säl; wa/. sdl,
sar. säL
692. sälär 'Anführer'.
aw. *särö,dära' ; phlv. sälar, \idQa(jTaöa()av\öaXdvrji^
(Procop. Pers. I, 7, 11 u. ö.), arm. LW. s(dar, spajsalar,
np. serdär (phlv. sardär) ist eine junge Bildung, da
man sonst seryär erwarten müsste.
Vergl. No. 726.
693. sämän 'Ordnung, Grenze; Hausgerät etc.'.
phlv. sämän, bezw. sahmän (z. B. AV. 'boundary-
mark'), arm. LW. sahman o()ocj oQ^o/ndc^ -nQoacayua (de
Lagarde, No. 1934).
Zu ai. [/'gad' etc. (Fr. Müller, WZKM. 5, 262).
(\)8än 'Wetzstein.
Siehe efsan (No. 98) 0.
*) Nachträglich sei hier noch np. sumhäde (goschr. sunb"), Käs.
K. sunbötä, arab. LW. sunbäSaj^ sunhäSat (Bibl.' geogr. arab. IV, 277)
'"Wetzstein* erwähnt
■}\*m^t!/*m.^i
==== leaf 175 (printed p. 154 )
— 154 -
694. (2)säii 'Teil, Stück; Art und Weise'; -$an gleich,
ähnlich, -sä.
Die Deutung von aw. sü^ia- (yt. 19, 44) als *Stück'
(Studien, I, 148) hat Geldner BB. XV, 254 wider-
rufon.
LW. kuid. säriy z. B. kH\sän *öü; wie?', va]suna auf
diese Weise'; afy. San; bei. sang (236).
Np. -sä^) hat das auslautende n verloren, wie äsuid,
a (No. 52), senrjso (Käs. Z. zu 1. süh) u. a. ni. Gehört
np. 'äsan 'äsä gleich, ähnlich* auch hierher?
695. säf/e 'Schatten, Schutz'.
ai. chayd' 'Schatten'; plilv. sayak,
kurd. se^ si\ bei. säig, n. saJ (340); wa;^. LW. sayd,
sar. suyä,
696. supär Tflug .
ai. phdla- Tflugscliar*, zu l^phal-, splial- *aufreissen'.
sar. spur 'Pflug .
697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
supiirden, sipäris (sifärls).
g. vaspartmün.
aw. tis-\- 2. l/'par-; phlv. avspärtan, avspurtan. (vd. 5
(77)), spiirtltan (AV.); ai. iid -{- "lA^par- 'hinüber-
führen', utpdrana- 'Übersetzen*; vergl. lat. portäre.
af/. späral übergeben'; kurd. sipärtin.
Die Etymologie stammt von de Lagarde, ist aber
sehr unsicher. Bei siperl (No. 703) passt die An-
knüpfung an l^par- ausfüllen* besser.
698. »Ipäs 'Dank*.
phlv. späs, späsdär; arm. spas-em aufwarten, dienen',
spas 'Dienst'.
^) Np. sä *Tribut* ist dagegen au8 *sävaka- entstanden, vergl. die
Form säv (Nöldeko, Pers. Stud. II, 20 Anm. 4). In der Bedeutung
'kostbare Art Stoff* (Vis und Rämln 52 Vers 7 v. u.) wird es ebenfalls
hierher gehören.
==== leaf 176 (printed p. 155 )
— 155 —
Also zu aw. [/^spas'y spast/eiti *spälien'? Sehr un-
sicher, Hübschmann, Armen. Stud., S. 50, No. 257^).
699. »ipah *Heer , sipeh^ ispeh\hed (arab. isbah[hu(/), jüd.-
pers. HNDID (Is. 13, 4).
ap. Ta/ma]späda- ; aw. spaöa- *Heer ; phlv. späh,
spühpat, arm. LW. späh, aspalmhet-),
oss. d. t. afsady t. ä/sud grosse Menge, xVbteilung
von Personen, Heer, Regiment* (40).
700. sljßer, isper *Schild'.
ap. anaoa^ßdgai' oi ye()()0(p6(}0i Hesyeh ; aw. spüra-
'Schild* in sparö.\dästa' ; phlv. spar (Men.); skr. phara-,
phalaka- (Mbh.) 'SchikV, daneben LW. sphara-^spharaka-
(Nöldeke, Monatsber. BAW. 1883, 1100).
arm. LW. aspar.
701. seperden, siperden auf etwas treten*.
aw. l^spar-^ vi\spara; phlv. spurtan (Bund.); ai.
[^sphur-^ sphurdti 'schnellen, treten; plötzlich er-
scheinen* (in letzter Bedeutung spät).
Nicht durchaus einwandsfrei.
wa/. na-spar-am, §i;'n. ni-^par-am, sar. na-xitor-am
^stampfen, treten*.
702. supurz Milz', uspurz.
Käs. espül^ espol, osböl (setzen ein "^esbäl voraus)'^).
. ') Rückert'8 Erklärung des Wortes (ZDMG. 8, 240) ist, wie
immer, geistreich aber doch unmöglich.
2) Zu arm. sparapet oQx^^^Qa^nyoi vergl. Hübschmann, ZDMG.
35, 133 Note 2.
') In diesem Falle gehen die np. Dialekte mit dem Pehlevl zusammen
und setzen eine ap. Grundform ohne r- Vokal voraus. Die Einstimmig-
keit der Dialekte in der Verwerfung des r- Vokals — alle Ausnahmen
beruhen auf Übertragungen aus der Schriftsprache — haben mich —
zusammengenommen mit dem Material, welches die modernen iranischen
Sprachen liefern sowie einer Vorliebe des Neupersischen für Trübung
ursprünglicher a, 6 in u ~ veranlasst, KZ. 32, 572 folg. dem Altpersischen
den r- Vokal abzusprechen. Ich möchte jetzt jedoch an dieser Meinung
nicht mehr festhalten, zumal da auch das Beläcl noch deutliche Spuren
eines einstigen Besitzes des r- Vokals aufweist.
```


## [2026-09-14T02:29:26.777Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD pās ===\"; grep -n \"pās\\b\\|pāsbān\\|pāspān\\|pāhr\" PHD.txt | head -20\necho \"=== PHD spās ===\"; grep -n \"spās\" PHD.txt | head -20\necho \"=== CHEUNG spas ===\"; grep -n -i \"spas\\|\\*pā-\\|pāsbān\" CHEUNG.txt | head -30",
 "description": "Grep MacKenzie and Cheung"
}
```


### [2026-09-14T02:29:26.863Z] TOOL RESULT

```
=== PHD pās ===
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
541:pardāxtan 65 pāsbānīh
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
567:spās dástan 76 sród
568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
887:attendant kardespās, P hámharz.
2140:grateful burdešnēhr, huspās, spās- dār, spāsešnās, spāsūmand.
2170:guard panig, pas; nigāstār; keep ~ pās dāštan.
2172:guardian pāsbān; (legal) star.
2432:ingratitude anespāsīh.
3591:servant bandag, kadagīg, kardespās, paristag, pēškār.
3593:service paristagīh, paristišn, spās,
3965:thank āzādīh, spās + dāštan, hangār- dan, etc.
3967:thanks āzādīh, spās; v. gratitude.
4272:watch (n.) pās.
4273:watch (v.) nigāh dāštan, pādan, pās dāštan.
4275:watcher pāsbān.
4746:pāyag pānāgīh pānāg -bān pänagīh panag pānzdah pākīzag pāk pālāy- pālūdan pālūdag 1-2pärag pārsīg pāsox pāsbānīh pāsbān pazen pāzand pazen pāšnag pāšom
=== PHD spās ===
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
567:spās dástan 76 sród
568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
887:attendant kardespās, P hámharz.
2140:grateful burdešnēhr, huspās, spās- dār, spāsešnās, spāsūmand.
2141:gratitude āzādīh, spas, spāsdārīh, šnāyišn, šnēhr.
2432:ingratitude anespāsīh.
3591:servant bandag, kadagīg, kardespās, paristag, pēškār.
3593:service paristagīh, paristišn, spās,
3965:thank āzādīh, spās + dāštan, hangār- dan, etc.
3966:thankful burdešnēhr, spāsdār.
3967:thanks āzādīh, spās; v. gratitude.
4779:spāh ALY Q335 dēbahr, spihr, Nay LAKE spaxr spahbed VP OR 0335 spas ts” суз? spāsdār Nee es. spāsdārīh uA a soda) spāsešnās TO Put 0335 debàg VW ett spāsūmand ? v€ Pus” q335 spāš AV суз?
5007:kandan, kardan kardagān kardagār *kardag, kūdak kardespās
=== CHEUNG spas ===
568:П Traces of the IE “eat”-root have been preserved in a few nominal forms, notably NP aspast ‘lucerne’, 
10380:preserved in several nominal formations: NP aspast ‘lucerne (Medicago sativa)’, 
20048:*KHOTANESE: (+ *ati-) LKh. tvasd- ‘to transfer’ || (+ us-) LKh. uspasd- ‘to produce, 
20049:cause’ || (+ *niš-) LKh. naspasd- ‘to remove’ = SGS: 41, 18, 51 
20310:‘twitch of pain, cramp, spasm’, ? Sh. biréj ‘a worm dangerous for sheep’ (< 
23073:*spas 353 
23112:*spas ‘to attend to; to serve’ 
23114:*AVESTAN: spas- (spas-, spös-) ‘to attend to; to serve’ || (+ *abi-) ‘to set one’s sight 
23117:Pres. {1} ia-: IND. 15р. OAv. spasiiä (Y 44.11), 3sg. Y Av. spasiieiti (Yt 10.82); Pres. {2} nu-: IND. 2pl. 
23118:OAv. “spasnuda (Y 53.6), INJ. 3sg. YAv. auua.spasnaot (Yt 11.5); Partic.: pres. {1} YAv. spasiiant- (Yt 
23120:Y Av. auui.spasta- (Yt 13.69). 0 For YAv. hisposant- cf. Kellens 1974: 115f. 
23157:*MISC: Arm. (LW) spasem ‘to serve’ (« WIr.), Toch. (LW) spaktam ‘service’, A 
23160:*SANSKRIT: spas ‘to observe, watch, spy’ (RV) || ("s-less" var.) pas ‘to see’ (RV+) 
31544:Jamaspa — Humbach: Kaikhusroo M. JamaspAsa — Helmut Humbach, Pursisniha. A 
33730:spas-, spas-, spös-, 353 
36663:uspasd-, 304 
36985:naspasd-, 304 
37758:spas(s)- (sas-, s(p)as-), 
40723:aspast, 148 
52024:spas, 354 
52420:spasem, 354 
55201:(s.v.), *sand, *spas (s.v.), 
55313:*iam (s.v.), *spas, *xaiz (s.v.) 
57787:*spas
```


## [2026-09-14T02:29:29.140Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS pasban ===\"; grep -n -i \"pasban\\|pāsbān\\|pāspān\\|pāhrak\\|spas\" SNS_pages.txt | head -20\necho \"=== SNS file info ===\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read();print('leaves',t.count(chr(12)))\"",
 "description": "Grep Shayast ne Shayast glossary"
}
```


### [2026-09-14T02:29:30.274Z] TOOL RESULT

```
=== SNS pasban ===
1386:                                                                                                                                                          Spas^UcJU,,    L lUiVb. 325-329) api- ^:ap- t.                                 s.
5162:     p^b'n t^^Ui^fc.           1614)     spasSnO,         ,/spas       : .jl   tuF^           I       ^'^c^'^C **'.)^ :p3dixsa:
7256:                                                         .j-V-       :spas:o"e>JJ            "-JjIj^a^-jVJU^jI^^j.i^^i^Ujj^"                                             .jL   :sar:\<o»
7257:                  (AiJ/fc.    1614) spas i&SiS**             /spas-          :&-
14886:                                                                   spas 175/4
14969:                                Spas/apas 12/9-10    kusnati 218/6                     ch3ya 174/21
=== SNS file info ===
leaves 242
```


## [2026-09-14T02:29:39.063Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (5162,7256):\n    pre='\\n'.join(lines[:target])\n    leaf=pre.count('\\f')\n    print('=== line',target,'leaf',leaf)\npages=t.split('\\f')\nprint(len(pages))\nEOF",
 "description": "Find SNS leaf numbers"
}
```


### [2026-09-14T02:29:40.126Z] TOOL RESULT

```
=== line 5162 leaf 74
=== line 7256 leaf 103
243
```


## [2026-09-14T02:29:46.036Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (74,103):\n    print('===== leaf',n)\n    print(pages[n][:2500])\n    print()\nEOF",
 "description": "Print SNS leaves 74 and 103"
}
```


### [2026-09-14T02:29:47.132Z] TOOL RESULT

```
===== leaf 74
      IVY                           Lu^L:*.L.5 lj
                                                                                                                             l£^       i~^L ^ L *jU

                               •
                                   oU^ <j*J*i «o^V :pasb3n: «tP*-«j
     p^b'n t^^Ui^fc.           1614)     spasSnO,         ,/spas       : .jl   tuF^           I       ^'^c^'^C **'.)^ :p3dixsa:
                                                                                                                             1
                                                                                                                                                             ^ou--^*
                      •n/YT**       1Y/T**      {Mir. Han.      II,    63.      )


                                                                                              I                                             -r/i^ -Yr-n-ir-r/A^
                    .j3*aijla4& <j3ol*"l« rpasfcan-tar:            Vv* w w,,
                                                                    •ir/f ^                             •J-t'y^'w.j*!*,^^ :p a dyab: o^^e

                                                                                              UiWb. 840)paity-a P 3m                     U Hodi. pp. 83-90.
                                                           .^:pak:              iw|j]                                              :



       cu-loijjl^Uunfccr.     10)       oVjV'J^^Vi^U
                                         -«oS*                                                                                               -tt-u/a^
                                                                                              I                                                          u-u/rv5
     (Mr. Han.      p*k :>;* CGiVPS. 62)pavaka- i^^^m
                      •   T/U^ .To/|o ^ -UY-rf/T^                 11,       63)               I            -J-^'^.ojy, :pady abih: -<uexr>o*ej
                                                                                                                           •YT-YY/IY^           U/A^ WA-AY/T^
                                                       •O sl*:pakan:        **"!
                                                                   rr/io-^                    ^^vV^^.^i,^^ :padyabdan:                                  *3U<t*,iey*>
                                                               

===== leaf 103
                                                         '       :


                                       tu^tn-L.jlj                                                                                 c-^Lul-^L^U^Ij                                                       \Vt
YA


                                                      .(Kotwai.       P- 169)                                                                  (Jlb.jfi^-,       :sast5r:        1a*»«*xx_w
                   .Y-p-6-T-l/" ** -6/T^
                                             *                                              !.P$           •(/Kk'fc.       1573)sastar-                   :   i^tf-**    sastar-:*5"
                                                                                                                      U/1fl^           (Mir. Man.             Ill, 61)-;s*st*r                      :




                                                         .j-V-       :spas:o"e>JJ            "-JjIj^a^-jVJU^jI^^j.i^^i^Ujj^"                                             .jL   :sar:\<o»
                  (AiJ/fc.    1614) spas i&SiS**             /spas-          :&-


                                                                                                                                                              .JL.aJL :salag: l9J-*<_v

^^.T^V^^^                 ***<* :x v ast ? :                            ,*mvW
 T4j^ffj.A.T
                               v
             w«*m*>o nsjlwO * x astanam :         1                          ^W           (Mir. s'rtjsU (AiWb.                   1567)         saracfa-: L.              [4V0"* •'*&)
                   V splitcorn -
                                  falhhanast                                         \>
                                                                                                                      »Y—) /A <5 .*/?<* -A/Y«£                    #sn.        III.
Corn separated                                                                   :                                                                                                           61).

=x
     v ast:l
             j0T
                     ^t^^^U^^fc^^^from kusks.                                                 •   T/ir-^ .JLijjii^            rpanzdah salag:                       i5^-o» -*oCef«J                           lo
                                         .«u-l*AJ»y-     trashed straw

>ahlavi VendidZd V. 35.
```


## [2026-09-14T02:30:08.993Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF sekuba ===\"; grep -n \"سکوبا\\|سقف\" FSF_pages.txt | head -20\necho \"=== AFM osqof ===\"; grep -n \"أسقف\\|الأسقف\\|اسقف\" AFM_pages.txt | head -10\necho \"=== FVQ usquf ===\"; grep -n -i \"usquf\\|asquf\\|bishop\" FVQ_pages.txt | head -10\necho \"=== MON sekuba ===\"; grep -n \"سکوبا\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Persian/Arabic refs"
}
```


### [2026-09-14T02:30:09.179Z] TOOL RESULT

```
=== FSF sekuba ===
2327:                ‫‪- 5000510‬پارسی‪ :‬سکوبا‪:‬‬                ‫باشد» (صحاج) «معتمد و امین»‬
2328:         ‫به اسقف چنین گفت کای دستگیر‬                              ‫(جهانگیری ‪-‬رشیدی ‪-‬برهان)‪:‬‬
2333:         ‫سقف گفت کاین نیست کاریگران‬                   ‫‏(‪٩‬رویز ‪)۹۱۴۱‬‬
2371:           ‫از ناصر خسرو (دیوان ‪:)۲۳۳-۳‬‬                ‫اسقف (باپیش اول و سوم و سکون دوم) س=قف‬
3068:                                                           ‫سکوبا بدو گفت کای نامدار‬
5188:‫سکوبا و بطریق و هر مهتری‬
12744: ‫(‪)۶-۸۷۲-۳۱۰۰۱‬‬                                         ‫به اسقف چنین گفت کای دستگیر‬
15223: ‫«سگزی‪ ,‬یعنی سیستانی‪ .‬چه مردم سیستان‬                                ‫به وا اسقف نگاه کنید‪.‬‬
15225:                               ‫سسخ‬‫به‬                                        ‫سکوبا (با پیش اول)‬
15227:‫در تاریخ سیستان بارها از «سجستان» که‬              ‫ان سقف اسقف» لاتینی ‪ 50۲0050‬به‬
15228:  ‫معرب سگستان است نامبرده شده است‪.‬‬                                   ‫واژ؛ اسقف نگاه کنید)‪.‬‬
15230:‫ص ‪ ۲۲‬چنین می‌نویسد‪« :‬آنچه معتقد‬                   ‫سکوبا و بطریق و هر مهتری‬
17164:                                                            ‫سکوبا بدو گفت کای نامدار‬
19871:           ‫‪-۱‬کاخ و بنادارای سقف گرد‪:‬‬        ‫‏(‪)٩۲-۱۲-۵‬‬
=== AFM osqof ===
=== FVQ usquf ===
1176:p. 191). Assemani, liibl. Or., iii, 2, 606, mentions Monophysite Bishops of al-Hira.
1207:occasion he listened to a sermon by Quss, Bishop of Najran, 4 at the
1219:4 That he was Bishop of Najran we learn from LA, vni, 58. From al-Baihaqi's
=== MON sekuba ===
```


## [2026-09-14T02:30:11.462Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN bishop ===\"; grep -n \"^bishop,\" KLN_1966.txt | head\necho \"=== KLN episcopal ===\"; grep -n \"^episcopal\\|^scope,\\|^spy,\\|^espionage,\\|^-scope\\|^species,\" KLN_1966.txt | head\necho \"=== NYB pas ===\"; grep -n \"^pas \\|pās \\[\\|pāsbān\\|pāspān\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep Klein and Nyberg"
}
```


### [2026-09-14T02:30:11.573Z] TOOL RESULT

```
=== KLN bishop ===
=== KLN episcopal ===
13647:espionage,  n.  —  F.  espionnage,  ‘spying’,  fr.  espion, ‘spy’,  fr.  It.  spione.  Sec  espy  and  -age. esplanade,  n.,  a  level  place;  esp.  one  serving  as  a promenade.  —  F.,  fr.  It.  spianata,  ‘leveling;  es¬ planade’,  prop,  subst.  use  of  the  fern.  pp.  of spianare,  ‘to  level’,  fr.  L.  explanare,  ‘to  flatten, level’,  whence  also  explain  (q.v.) espousal,  n.  —  OF.  espousailles  (F.  epousailles), fr.  L.  sponsdlia,  ‘betrothal,  espousal’  (whence also  OProvenq.  espozalha,  OSp.  esposayas,  Sp. esponsales),  prop.  neut.  pi.  of  the  adjective  spon-
36462:spy,  tr.  and  intr.  v.  —  ME.  spien,  espien,  fr.  OF. espier  (F.  epier),  fr.  Frankish  *spehon,  which  is rel.  to  OHG.  spehon,  MHG.  spehen,  ‘to  examine closely’,  G.  spdhen,  ‘to  spy’,  MLG.  speen,  MDu. spien,  ‘to  spy’,  ON.  spa,  v.,  ‘to  prophesy’,  spa, n.,  ‘prophesy’,  OHG.  speho,  ‘spy’,  spahi,  -Ida, ‘wisdom’,  OHG.,  OS.  spahi,  ‘wise,  prudent’,  fr. I.-E.  base  *spek-,  ‘to  look  at,  examine,  spy’, whence  also  L.  specere,  ‘to  see,  look  at’,  species, ‘a  seeing,  sight,  look,  appearance,  shape,  form, kind,  quality,  aspect’.  See  species  and  cp.  words there  referred  to.  It.  spiare,  Sp.  espiar,  ‘to  spy’, are  also  Teut.  loan  words, spy,  n.  —  ME.  spie,  fr.  OF.  espie  (whence  F.  epie), fr.  espier,  ‘to  spy’.  Cp.  It.  spia,  ‘spy’,  fr.  It.  spi¬ are,  ‘to  spy’,  Sp.  espia,  ‘spy’,  fr.  Sp.  espiar,  ‘to spy’.  Cp.  also  F.  espion,  ‘spy’,  which  is  a  loan word  fr.  It.  espione,  augment,  of  spia,  and  see spy,  v.  Cp.  also  espy.
=== NYB pas ===
455:an-ispās [’nsp’s] disobedient 901% (andar to). — Paz. anaspäs, v. spas; ispds with prothetic vowel is NW form.
2980:pas PHL; B’TL 5726], with -c: pas-ic PHL-c] adv. 1. behind: bē raft hend... Vahuman pes, Zartuxšt pas they went away, V. first, Z. behind 5712-33; ~ ~ one after the other 11012; ~ andarg haxt on her back between her thighs 572%; hac ~ from behind 25%. 2817; 6 peš... 6 ~ forwards ... backwards 6811-12; — hac ~ + prep. behind 31%; api-šan ... hac ~ behind them 717-18; õi . . . hac m in her footsteps 3718-19, — 2. afterwards, then: ~, or u ~, or ~-ic, pursuing a narration, passim; introducing the apo- dosis after a subordinate clause 243-8, 27273, 4411-13, 914-5; ka vas-ic ... ~ -ic however much yet 9112-13; apäk
2983:pas [p's] watch, guard 65°. — OP *päga-, SW form of padra-, v. pahr. - MPrs p’sb’n ‘watchman, guardian’.
```


## [2026-09-14T02:30:23.440Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npages=t.split('\\f')\nfor target in (2371,15225):\n    pre='\\n'.join(lines[:target]); leaf=pre.count('\\f')\n    print('=== line',target,'leaf',leaf)\n    print(pages[leaf][:3000])\n    print()\nEOF",
 "description": "Print Noushin glossary entries"
}
```


### [2026-09-14T02:30:24.584Z] TOOL RESULT

```
=== line 2371 leaf 54
 ‫اشنان‬                                          ‫‪۵۱‬‬


                   ‫(با پیش اول و دوم ‪-‬تازی)‬          ‫گمارند و او را استوار گویند و اینشغل را‬
‫یی ‪ :‬لانیش‬        ‫در این‬     ‫بشو ان مده‬                 ‫یسشن‬
                                                           ‫رانح‬
                                                              ‫وو‬‫یند‬
                                                                  ‫اغو ا‬
                                                                      ‫رای‬
                                                                        ‫اور‬
                                                                          ‫تی‬
                ‫‪- 5000510‬پارسی‪ :‬سکوبا‪:‬‬                ‫باشد» (صحاج) «معتمد و امین»‬
         ‫به اسقف چنین گفت کای دستگیر‬                              ‫(جهانگیری ‪-‬رشیدی ‪-‬برهان)‪:‬‬
 ‫ز ایسران یکی نامجویم دبسیر‬                                       ‫فرستاد بااو یکی استوار‬
 ‫(‪)۶-۷۱-۴۵۱‬‬                                            ‫یک آن کسووار‬    ‫زندبه‬
                                                                           ‫نیوا‬
                                                                              ‫زا‬
         ‫سقف گفت کاین نیست کاریگران‬                   ‫‏(‪٩‬رویز ‪)۹۱۴۱‬‬
                                                                 ‫پ‬
 ‫که پیش از تو بودند چندی سران‬                        ‫مهندس رومی برای خسرو پرویز کاخ‬
 ‫(‪)۶-۳۲-۶۵۲‬‬                                          ‫نوی بنا نهاده ولی برای ساختن ایوان به‬
                                       ‫اشتاب‬          ‫خسرو می‌گوید شتاب نکن چون ممکن‬
                                    ‫شتات‪:‬‬            ‫است ایوان فرو ریزد‪ .‬خسرو شتاب دارد‬

           ‫کاهین باره را نیست پایاب اوی‬              ‫و گفتة او را نمی‌پذیرد‪ .‬مهندس چهار سال‬
‫اوی‬      ‫شرتاب‬
             ‫درنگی شزوداشی‬                           ‫ناپدید می‌شود‪ .‬وقتی نزد خسرو می‌آید‬
 ‫(‪)۲-۲۹۱-۶۹۲‬‬                                         ‫خسرو از او می‌پرسد نایدید شدنت برای‬

                      ‫اشقر (بروزن استر)‬                                ‫بچوهد؟ رومی می‌گوید‪:‬‬
   ‫اسب قهوه‌ای رنگ کهر‪ .‬و مطلق اسب‪:‬‬                         ‫چنین گفت رومی که گرشهریار‬
                ‫برینگونه تا برگزید اشقری‬              ‫فرستد مرابایکی استوار‬
 ‫یکی بادپایی گشاده بری‬                                        ‫بگویم بدان کاردان پسوزشم‬
 ‫(‪)۷-۲۷۲-۰۴۱‬‬                                          ‫به پوزش بجا آید افروزشم‬
                                      ‫اشکردن‬          ‫‏(‪٩‬رویز ‪۹۱۷۳6‬‬
                                                                ‫پ‬
                 ‫به واه شکردن نگاه کنید‪:‬‬              ‫رومی به استوار نشان می‌دهد که بنا فرو‬
                           ‫اشنان (با پیش اول)‬        ‫نشسته است و اگر در آن زمان ایوان را‬
 ‫گیاهیست که در رخت‌شویی و شست‌و‬                               ‫می‌ساخت بنااز بن فرو می‌ریخت‪.‬‬
‫شوی بدن بکار می‌رود مانند جوبک که‬                     ‫از تاریخ سیستان (‪« :)۸۰۲‬یع

=== line 15225 leaf 306
 ‫سگزی‬                                       ‫‪۳.۳‬‬

                          ‫سکزی (با زبر اول)‬                                        ‫ماه سال‪:‬‬

    ‫منسسوکبسبتهان (عربی؛ سجستان؛‬                            ‫زچین روی یکسر به ایران نهاد‬
 ‫در فرهنگ‌ها مطالب نادرستی دربارة‬                 ‫به روز سفندارمذ بامداد‬
 ‫سگزی و سگستان آمده است (از آنجمله‬                ‫(پ‪۹‬رویز ‪)۷۵۴۲‬‬

  ‫برای نمونه‪ :‬رشیدی چنین می‌نویسد‬
 ‫«سگزی‪ ,‬یعنی سیستانی‪ .‬چه مردم سیستان‬                                ‫به وا اسقف نگاه کنید‪.‬‬
 ‫وگری مشهورند و‬        ‫‌یج‬‫ختتجان‬
                               ‫سسخ‬‫به‬                                        ‫سکوبا (با پیش اول)‬
            ‫لهذا سیستان راسگستان گویند»)‪.‬‬         ‫پیشوای مذهبی در آیین مسیحی (معرب‬
‫در تاریخ سیستان بارها از «سجستان» که‬              ‫ان سقف اسقف» لاتینی ‪ 50۲0050‬به‬
  ‫معرب سگستان است نامبرده شده است‪.‬‬                                   ‫واژ؛ اسقف نگاه کنید)‪.‬‬
 ‫بهار مصحح تاریخ سیستان در زیرنویس‬                           ‫نوشتند نامه به هر کشوری‬
‫ص ‪ ۲۲‬چنین می‌نویسد‪« :‬آنچه معتقد‬                   ‫سکوبا و بطریق و هر مهتری‬
 ‫علمای علم لغت است سیستان مصحف‬                    ‫(‪)۶-۶۳-۹۵۴‬‬

 ‫سگستان است که مملکت سکه‌ها باشد و‬                                ‫سگالش (اسم مصدر از سکالیدن)‬
 ‫این «سکه» مردمی بوده‌اند از عشایر‬                                               ‫اندیشیدن‪:‬‬

 ‫آریایی که بعد از انقراض دولت‬                                   ‫نشستند بیدار هر دو به هم‬
  ‫هخامنشی در حدود ‪ ۰۳۱‬ق ‪.‬م‪ .‬ادوراییل‬              ‫وم‬
                                                   ‫سگالش گرفتند بر بیش ک‬
‫عهد اشکانیان وارد آن سرزمین شده و تا‬              ‫(‪)۳-۶۵-۲۳۴۸‬‬
 ‫خود‬      ‫فتات‬
             ‫ر تح‬
                ‫ص را‬
                   ‫تنجاب‬
                       ‫موپ‬
                         ‫سند‬                                                         ‫سکالیدن‬
 ‫قدرااردند و قبل از آن نامسیستان «زرنگا»‬                                         ‫اندیشیدن‪:‬‬

‫بوده است کهنامشهر «زرنگ» از آن گرفته‬                            ‫کسی کو بود شهریار زمین‬
                              ‫شده است‪».‬‬           ‫نه بازیست بااو سگالید کین‬
‫پروفسور هرتسفلد درین‌باره چنین گوید‪:‬‬              ‫)‪(1-۵۸-۷۰1‬‬

 ‫«از زمان سیروس (تقریباً ‪۵‬ق‪0‬بل از میلاد)‬                                   ‫(ناصر ‪:)۹۳۲-۵۱‬‬
 ‫تادور؛ اسکندر‪ .‬این ساکاها در آن طرف‬                     ‫مرتو رانیکی سگالد یار تو‬
 ‫سغد یعنی در فرغانه سکونت داشتند‪ .‬در‬              ‫چون مر او را توشوی نیکوسگال‬
 ‫سالنامه‌های دولت چين اسم آنها در‬                                    ‫(ویس ‪:)۲۹۲-۲۷۱‬‬
 ‫اواسط مائهدوم قبل از میلاددر آن حدود‬                   ‫بدان روزی که از تو شد چه نالی؟‬
  ‫هها‬
    ‫برده می‌شود‪ .‬هدمران موقع اآستن ک‬              ‫وز آن روزی که نامد چه‌سگالی؟‬
 ‫مورد تهاجم سایر ملل آسیای مرکزی‬                    ‫(سیاست‌نامه ‪ :)۸۸‬تدبیر کار او بسگالند‪.‬‬
```


## [2026-09-14T02:30:45.426Z] TOOL CALL #24: Bash

```json
{
 "command": "pdftoppm -f 466 -l 466 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466.png",
 "description": "Render PDF page 466"
}
```


## [2026-09-14T02:30:45.900Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:30:46.928Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 53053 Sep 13 22:30 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466.png
```


### [2026-09-14T02:30:46.935Z] TOOL RESULT

```


```


## [2026-09-14T02:30:48.834Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466.png"
}
```


### [2026-09-14T02:30:48.861Z] TOOL RESULT

```

```


## [2026-09-14T02:31:05.293Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 466 -l 466 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg466hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg466hi.png'); print(im.size)\nim.crop((500,1050,1500,1750)).save('pg466-crop1.png')\n\"",
 "description": "Render and crop page region"
}
```


### [2026-09-14T02:31:07.833Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T02:31:09.858Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466-crop1.png"
}
```


### [2026-09-14T02:31:09.879Z] TOOL RESULT

```

```


## [2026-09-14T02:31:23.594Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg466hi.png')\nim.crop((500,420,2050,1000)).resize((1550,580)).save('pg466-crop2.png')\nim.crop((500,1550,2050,2050)).save('pg466-crop3.png')\n\"",
 "description": "Crop top and bottom regions"
}
```


### [2026-09-14T02:31:24.995Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:31:26.998Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466-crop2.png"
}
```


### [2026-09-14T02:31:27.015Z] TOOL RESULT

```

```


## [2026-09-14T02:31:32.225Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466-crop3.png"
}
```


### [2026-09-14T02:31:32.243Z] TOOL RESULT

```

```


## [2026-09-14T02:31:40.796Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/spe%E1%B8%B1-",
 "prompt": "Give the reconstructed root, its gloss, and the list of descendants (Indo-Iranian, Greek, Latin, Germanic). Quote the Avestan and Sanskrit forms."
}
```


## [2026-09-14T02:31:42.515Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%A7%D8%B3",
 "prompt": "Give the Persian entry سپاس: etymology (Middle Persian form, Proto-Iranian root, cognates), meaning. Quote the etymology text."
}
```


### [2026-09-14T02:31:46.828Z] TOOL RESULT

```
# Persian Entry: سپاس

**Etymology:**
The word derives from Middle Persian spʾs (spās), tracing back through Proto-Iranian *spácati and Proto-Indo-Iranian *spáćati to Proto-Indo-European *speḱ-. The entry notes it is "Unrelated to Russian спасибо (spasibo)."

**Meaning:**
As a noun, سپاس means "thanks" or "gratitude." As an interjection, it expresses "thanks."

**Etymology Quote:**
"From Middle Persian [script needed] (spʾs /⁠spās⁠/), from Proto-Iranian *spácati, from Proto-Indo-Iranian *spáćati, from Proto-Indo-European *speḱ-"
```


### [2026-09-14T02:31:46.885Z] TOOL RESULT

```
# Proto-Indo-European Root: *speḱ-

**Reconstructed Root:** *speḱ-

**Gloss:** "to see, to look, to observe"

**Major Descendant Language Groups:**

1. **Proto-Indo-Iranian** - descendants include Sanskrit and Avestan forms
2. **Proto-Hellenic** - Ancient Greek reflexes
3. **Proto-Italic** - Latin descendants
4. **Proto-Germanic** - Northern European language family

**Key Ancient Forms:**

- **Avestan** (Old Avestan): "𐬯𐬞𐬀𐬱𐬥𐬎𐬚𐬁" (spašnuθā)
- **Sanskrit:** "स्पष्ट" (spaṣṭá, meaning "clear" or "distinct")

The root demonstrates the characteristic metathesis in Greek forms, appearing as *sḱep- in Greek derivatives, while maintaining *speḱ- in other branches. This ancient root ultimately generated numerous modern English words related to vision and observation.
```


## [2026-09-14T02:31:49.942Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3",
 "prompt": "Give the Persian entry پاس: etymology (Middle Persian, Proto-Iranian root), meanings, and any derived terms such as پاسبان. Quote the etymology text exactly."
}
```


## [2026-09-14T02:31:51.380Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%B3%D9%82%D9%81",
 "prompt": "Give the Arabic entry أسقف: etymology (Greek/Syriac source), meaning, plural. Quote the etymology text exactly."
}
```


### [2026-09-14T02:31:58.097Z] TOOL RESULT

```
# Arabic Entry: أسقف

**Etymology:** The word derives from Classical Syriac ܐܦܣܩܘܦܐ (ʾeppisqoppā), which itself comes from Ancient Greek ἐπίσκοπος (epískopos). As the text states: "From Classical Syriac ܐܦܣܩܘܦܐ (ʾeppisqoppā) or a variant thereof...a borrowing of Ancient Greek ἐπίσκοπος (epískopos)."

**Meaning:** In Christian contexts, this term refers to a bishop—a high-ranking member of the clergy.

**Plural Forms:** The word has two plural variations:
- أَسَاقِفَة (ʔasāqifa) 
- أَسَاقِف (ʔasāqif)
```


### [2026-09-14T02:31:58.539Z] TOOL RESULT

```
# Persian Entry: پاس (pâs)

## Etymology
The first Persian entry traces back through Middle Persian to Proto-Iranian roots. According to the text: "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[Book Pahlavi needed\] (pʾs /⁠pās⁠/), from [Old Persian](https://en.wikipedia.org/wiki/Old_Persian "w:Old Persian") _[\*pāçah](/w/index.php?title=Reconstruction:Old_Persian/p%C4%81%C3%A7ah&action=edit&redlink=1 "Reconstruction:Old Persian/pāçah (page does not exist)")_, from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*páHθrah](/w/index.php?title=Reconstruction:Proto-Iranian/p%C3%A1H%CE%B8rah&action=edit&redlink=1 "Reconstruction:Proto-Iranian/páHθrah (page does not exist)")_"

The root etymology ultimately derives from Proto-Indo-European *peh₂- ("to protect").

## Meanings (Etymology 1)
1. Guard, watch
2. Watch of the night
3. Consideration, considering (chiefly as "به پاس")

## Derived Terms
- پاسبان (pâsbân)
- پاسدار (pâsdâr)
- پاسداشت (pâsdâšt)
- پاس دادن (pâs dâdan)
```


## [2026-09-14T02:32:05.698Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bishop",
 "prompt": "Give the full etymology of 'bishop', including Greek episkopos, Latin episcopus, and the note about the word spreading to other languages. Quote key phrases."
}
```


## [2026-09-14T02:32:08.749Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DA%A9%D9%88%D8%A8%D8%A7/",
 "prompt": "Give the dictionary entries for سکوبا, especially the فرهنگ معین (Mo'in) and دهخدا entries, including any origin tag (e.g. [یونانی], [سریانی], [ع.]) and the definition. Quote the Persian text."
}
```


### [2026-09-14T02:32:11.613Z] TOOL RESULT

```
# Etymology of Bishop

The word "bishop" traces back through multiple languages. In Old English, it appeared as *bisceop*, meaning "bishop, high priest (Jewish or pagan)." This derived from Late Latin *episcopus*, which came from Greek *episkopos*.

The Greek root is particularly revealing. According to the source, *episkopos* means "watcher, (spiritual) overseer," originally "a title for various government officials." The term combines *epi-* ("over") with *skopos* ("one that watches, one that looks after; a guardian, protector").

## Geographic Spread

The word diffused widely across European languages with fascinating variations. As noted, "Late Latin *episcopus* in Spanish became *obispo*, in Italian *vescovo*, in Welsh *esgob*." Germanic languages adopted it as well: Old Saxon *biscop* and Old High German *biscof*. More distant linguistic cousins include Lithuanian *vyskupas*, Albanian *upeshk*, and Finnish *piispa*.

The most striking comparison involves English and French: both descended from the same root, yet through independent sound changes they "not [have] a letter in common"—bishop versus évêque.

## Later Developments

Beyond ecclesiastical use, the chess piece received this name around 1560, and by 1746, the term denoted "an alcoholic punch."
```


### [2026-09-14T02:32:14.719Z] TOOL RESULT

```
# Dictionary Entries for سکوبا

## Dehkhoda Dictionary Entry
The entry identifies سکوبا as a male name meaning "fearful" and specifically references a monk. It notes: "نام راهبی است که حضرت عیسی مسیح بدیر او رفته به آسمان صعود کرد" (a monk to whose monastery Jesus Christ went before ascending to heaven). The entry also mentions it may derive from سکوپا and lists it as a bishop or metropolitan.

## Mo'in Dictionary Entry
This dictionary provides the briefest definition: "(سُ) (اِ.) اسقف" — indicating the word means "bishop" with notation for pronunciation.

No etymological origin tags (such as [یونانی], [سریانی], or [ع.]) appear in these entries on this page.
```


## [2026-09-14T02:32:31.457Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg466hi.png')\nim.crop((1750,1370,2000,1470)).resize((1000,400)).save('pg466-osqof.png')\n\"",
 "description": "Crop osqof script"
}
```


### [2026-09-14T02:32:32.744Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:32:35.059Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466-osqof.png"
}
```


### [2026-09-14T02:32:35.077Z] TOOL RESULT

```

```


## [2026-09-14T02:32:54.702Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor n in range(538,549):\n    p=pages[n]\n    if 'سپاس' in p:\n        print('=== leaf',n,'(printed ~',n+543,')')\n        # print lines containing سپاس\n        for ln in p.split('\\n'):\n            if 'سپاس' in ln: print('   ',ln.strip()[:300])\nEOF",
 "description": "Grep Borhan-e Qate vol2 for sepās"
}
```


### [2026-09-14T02:32:55.905Z] TOOL RESULT

```
leaves 684
=== leaf 548 (printed ~ 1091 )
    ‫‪ - ۴‬پهلوی ‪» 8805‬ارمنی ‪(P5 010-84‬خدمت‏ کردم ‪ ۰‬سپاس‌داشتم) ‪(52۳5 ,‬خدعت)‬
    ‫بدو بر سپاسه لینداشتم ‪.‬‬                            ‫وزآن پس که بدکرد بگذاشتم‬        ‫‪9‬‬
    ‫‪ ۲‬رك ‪ :‬سپاسی ‪۸- .‬ازبرساخته‌های‬                         ‫‪ - 1‬از‪ :‬سپس ‪ +‬ی (ست) ورك ‪:‬صاسی ‪(0‬‬
    ‫فرقة آذر کیوان ‪ « :‬دختین نظر در بیان اعتقادات علمی و عملی سپاسیان"‪ .‬آغاز ذکر هذهب‬
```


## [2026-09-14T02:32:57.189Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC spek ===\"; grep -n \"^spek-\\|^spek\\b\\|^skop\" IEC.txt | head\necho \"=== HUB sipas ===\"; grep -n \"sipäs\\|spās\\|spas-em\\|257\\.\" HUB.txt | head -20\necho \"=== SYN see ===\"; grep -n \"15.51 SEE\\|SEE (v\" SYN.txt | head",
 "description": "Grep Mann, Hübschmann, Buck"
}
```


### [2026-09-14T02:32:57.282Z] TOOL RESULT

```
=== IEC spek ===
15789:skopeið, skopio ‘cut, strike’. Cf. skopos. (Vo- calism of Balto-S1. ambig.) Br. skei, pp: skoet, v. “beat, strike’; OCS sko- pljo, skopiti, v. ‘castrate’; R skopit,, inf. id.; Li. cf. skaptas, m. ‘carver’ (vocalism ambig. cf. skap-)
15792:skopos ‘castrated; gelding, eunuch’. Cf. sko- peið Arm. Xoj, gs: Xo, ab. s. xov, s. fram"; EMBr. sko, m. ‘cut, blow’; Pol. skop, m. ‘wether’; Cz. also: tram; eunuch’; Li. skapas, m. 'cas- trated animal, eunuch’; OCS cf. skopíci, m. ‘eunuch’
15797:skopelos, skopolos — skortos, is
16774:spek- (1) “look, see, observe’. WP II, 659 Skt. spas, m. ‘beholder’; (long-gde in) spåsa- yàmi, v. ‘show’: Av. spas, m. ‘spy’: spasya, 1sg. ‘wish to watch’; Gk. cf. (metath.) sképtomai, v, tr. ‘view, spy, consider’; Lat. specio, specére, v. ‘see, look at: OHG spéhon, MHG spëhen, wv. ‘spy, watch’; ON. Sw. speja, f. ‘spy’; (long- gde in) OHG, OS spáhi, MHG spzhe, adj. *wise, comely'; sf. *wisdom, comeliness'. Cf. also Lat. specium, n. ‘probe’; species, f. form, likeness, vision”
16775:spek- (spekos, spokos, us) (2) ‘cave’ (?). (Arm. a LW from Lat. fossa via Gk.?)
=== HUB sipas ===
1130:257. Ich kann np. bel, bll *Spaten' (nach Vullers auch =
3505:nend, befindlich' Bdh. 61. 241, Min. 61. 132, Shk. 257.
10163:p. 204, 210, 212—213, 219, 236-237, 257.
10181:p. 170, 206-208, 216-219, 257.
10380:Damavand 257.
10494:hamUr 105, 257.
=== SYN see ===
```


## [2026-09-14T02:33:05.316Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (542,543,544,547,548):\n    p=pages[n]\n    print('==== leaf',n,'(printed ~',n+543,') has سپاس:', 'سپاس' in p)\nprint(pages[548][:2500])\nEOF",
 "description": "Print Borhan leaf 548"
}
```


### [2026-09-14T02:33:06.562Z] TOOL RESULT

```
==== leaf 542 (printed ~ 1085 ) has سپاس: False
==== leaf 543 (printed ~ 1086 ) has سپاس: False
==== leaf 544 (printed ~ 1087 ) has سپاس: False
==== leaf 547 (printed ~ 1090 ) has سپاس: False
==== leaf 548 (printed ~ 1091 ) has سپاس: True
  ‫رک ها‬

‫گوبند « سپای دارم»‬                   ‫که‬‫نست‬
                                         ‫ام ه‬
                                            ‫نه‬‫چمنت‬
                                                 ‫و‬                                                  ‫‪# .‬‬       ‫هت‬
‫پعنی قبزل دارم و منت پذیرم ‪ -‬و بمعنی لطف‬                       ‫سبارو ‪ = ۵۱‬بفتحاولوالی‌بالف کشیده‬
                      ‫است‪.‬‬     ‫نزآمده‬    ‫ومرحمت‬      ‫وشففت‬
                                                               ‫وثالت بواو رسیده وبکاف زده » بمعنی کبوترباشد‬
‫‏‪ ٣‬گرا اول‌رفتح رابع ‪:‬منت‬                    ‫سیاسه‬
                                                                                       ‫وجربی حمام گوبند ‪.‬‬
 ‫برکسی نهادن باشد ‪ -‬وبمعتی لطف لمودن‌وشفقت‬                      ‫آشاره‪,‬مخفف‬    ‫ولزن‬
                                                                                 ‫راو‬
                                                                                   ‫ببکر‬      ‫سیاره‬
                                      ‫کردن هم هت ‪. ۵‬‬
                                                                 ‫سی پاره است وآن بك جزو باشد اجزسزیو‬
‫=کر اول بروزن قیاسی ؛‬
                    ‫سیاسی ‪ 1‬ب‬                                         ‫و‬
                                                                      ‫ک زا‬
                                                                         ‫کلام خدا ‪ - ۴‬و بفتح اول کے‬
                                                               ‫بدان یز‬       ‫ویر‬
                                                                               ‫مش‬‫شرد‬
                                                                                   ‫که فان سازدد عنی کا‬
 ‫سیاسیان ‪ -‬بر وزن قیاسیان ک»دایدن‬
 ‫و گیابی کنند کان‌باشند‪- ۷‬وامتان‌اولین بیغمبری‬                 ‫یک اول بر وزن شکاری ‪.‬‬         ‫سیاری‬
‫را لیزکوبند که بعجم مبموث شد ‪ - ۸‬و او را‬                       ‫ماقکندم و جو را کویند ‪ ,‬وآن علفی‌باشد ميان‬
  ‫میم و کتاب اورا دساتر‪.‬‬             ‫مهآ بار می‌ناه‌ند کے‬
                                                               ‫خالی کهبخوشة کندم پیوسته است ‪ -‬و بمعنی‬
 ‫سیاناح *‪ -‬بکر اول و اتی با الف‬                                 ‫خوشءٌ کندم وجو همبنظر آمده است ‪ -‬وبهندی‬
 ‫ممتي‬     ‫ونون بالف کشده وبخای تةطه‌دار )‪ ۱‬رده‬                  ‫ینزمت شبیه بفندق و در‬   ‫چآ‬‫قوفل باشد و‬
‫‪ ۳‬وبلاو‬      ‫وآن سمز نی باشد که در‬             ‫اسفناح است»‬
```


## [2026-09-14T02:33:22.024Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%90%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82",
 "prompt": "Give the Ancient Greek entry ἐπίσκοπος: etymology (epi + skopos), meanings (overseer, guardian, bishop), and descendants/borrowings into other languages (Latin, Syriac, Arabic, Persian, Armenian). Quote key text."
}
```


## [2026-09-14T02:33:23.683Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%BF%CF%80%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek entry σκοπός: etymology (from PIE *speḱ- with metathesis), meanings. Quote the etymology text."
}
```


### [2026-09-14T02:33:29.227Z] TOOL RESULT

```
# ἐπίσκοπος (epískopos)

## Etymology
The term combines two Greek elements: the prefix "ἐπι-" (epi-, "upon") plus "σκοπός" (skopós, "watcher, lookout, guardian").

## Primary Meanings
As a noun, this word carries several related senses:

1. **"watcher, guardian"** and **"scout, watch"**
2. **"overseer, supervisor, inspector"**
3. In Christian contexts: **"an ecclesiastical superintendent, bishop"**

There's also an adjectival form meaning "hitting the mark, target" or "successful."

## Linguistic Descendants
The word spread widely through borrowing:

- **Latin**: *episcopus* (which generated further Romance language descendants)
- **Aramaic**: אפיסקופא
- **Arabic**: أسقف (*ʔusquf*)
- **Old Armenian**: եպիսկոպոս (*episkopos*)
- **Persian**: سُکوبَا (*sukōbā*)
- **Slavic languages**: Old Church Slavonic ѥпискоупъ (*jepiskupŭ*), Russian епископ, Ukrainian єпископ

The term's travels across multiple language families reflect Christianity's expansion through the Mediterranean and beyond.
```


### [2026-09-14T02:33:29.781Z] TOOL RESULT

```
# Ancient Greek σκοπός

**Etymology:**
The entry derives from the root of σκέπτομαι (sképtomai, "to observe") combined with the deverbal suffix -ός. The Wiktionary page states: "From the root of _σκέπτομαι_ (sképtomai, 'to observe') + _-ός_ (-ós)."

The word ultimately traces to the Proto-Indo-European root *speḱ- (meaning "to observe" or "look at"), though this connection appears in the categorical metadata rather than the main etymology section.

**Meanings:**
1. Watcher, lookout
2. Protector, guardian
3. Spy, scout
4. Mark, target
5. Goal, aim

The noun is masculine, second declension, and appears in classical texts like the Homeric Hymns.
```


## [2026-09-14T02:33:36.721Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/telescope",
 "prompt": "Give the etymology of 'telescope', including the Modern/New Latin telescopium, Galileo, Greek teleskopos, and the French télescope. Also anything on 'microscope' and 'periscope' if mentioned. Quote key phrases."
}
```


## [2026-09-14T02:33:38.737Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/specio",
 "prompt": "Give the Latin entry speciō / specere: etymology (Proto-Italic, PIE *speḱ-), meaning, and derived terms (respectus, suspectus, expecto, inspicio, specimen, spectrum, specialis, species). Quote the etymology."
}
```


### [2026-09-14T02:33:42.198Z] TOOL RESULT

```
# Etymology of Telescope

**Origin and Development:**
The term "telescope" entered English around 1640s, derived from Italian *telescopio* (Galileo, 1611) and Modern Latin *telescopium* (Kepler, 1613). Both versions trace back to Greek *tēleskopos*, meaning "far-seeing."

**Greek Roots:**
The word combines two Greek elements: *tēle-* meaning "far" plus *-skopos* meaning "watcher." As the source notes, "far-seeing," from *tēle-* "far" plus "-skopos" "watcher" (from PIE root *spek-* "to observe").

**Coinage Credit:**
The term was "said to have been coined by Prince Cesi, founder and head of the Roman Academy of the Lincei" where Galileo held membership.

**Earlier English Usage:**
Before "telescope" became standard, English speakers used "trunk" (1610s) as a shorthand for "perspective trunk" to describe the instrument.

**Note on Related Terms:**
The page does not discuss *microscope* or *periscope* etymology, focusing exclusively on *telescope* and related compounds like *kaleidoscope*.
```


### [2026-09-14T02:33:45.170Z] TOOL RESULT

```
# Latin Entry: speciō / specere

**Etymology:**
Inherited from Proto-Italic *spekjō, derived from Proto-Indo-European *spéḱyeti. The entry states: "Inherited from Proto-Italic *spekjō, from Proto-Indo-European *spéḱyeti."

**Meaning:**
In Old Latin (rare usage), speciō means to observe, watch, or look at.

**Derived Terms:**

The entry lists numerous prefixed verbs including:
- aspiciō, cōnspiciō, dēspiciō, īnspiciō, perspiciō, prōspiciō, respiciō, suspiciō

Other related word forms include:
- speciālis (special/relating to species)
- speciēs (appearance, form, species)
- specimen (example, sample)
- spectō (to watch/behold)
- spectrum (image, appearance)
- speculum (mirror)

**Note:** The document does not include "respectus," "suspectus," or "expecto" in its derived terms listings, though suspiciō (from which suspectus would derive) appears among the prefixed verbs.
```


## [2026-09-14T02:33:51.059Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/",
 "prompt": "Give the dictionary entries for اسقف, especially فرهنگ معین (Mo'in) with its origin tag (e.g. [ع.] or [یونانی]) and دهخدا, including any statement about Greek/Syriac origin. Quote the Persian text."
}
```


## [2026-09-14T02:33:52.825Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN look/see ===\"; grep -n \"15\\.51\\|15\\.52\\|SEE$\\|LOOK\" SYN.txt | head -20",
 "description": "Grep Buck for see/look"
}
```


### [2026-09-14T02:33:57.384Z] TOOL RESULT

```
# Dictionary Entries for اسقف

## Farhang-e Mo'in (معین)
**Etymology tag:** [معر.] (borrowed/arabicized), [اِ.] (foreign)

"از یونانی گرفته شده به معنای پیشوای عیسوی که مرتبه اش از کشیش بالاتر است"

*Translation: Derived from Greek, meaning a Christian leader whose rank is higher than a priest.*

---

## Dehkhoda Dictionary
The entry traces the word through multiple classical Persian lexicons. It notes the term originates from Greek *episcopus* (یونانی اپیسکوپوس) and represents "رئیس اسقفیه" (head of a bishopric). 

A significant excerpt states: "گویند این لغت عربی است" (they say this word is Arabic), yet simultaneously confirms its ultimate Greek source: "اسقف النصاری ، اعجمی معرّب" (the Christian bishop is a foreign word that has been arabicized).

The Dehkhoda entry extensively documents ecclesiastical hierarchy in Islamic lands, listing the ranking from patriarch down through bishops and priests.
```


### [2026-09-14T02:33:58.462Z] TOOL RESULT

```
=== SYN look/see ===
5648:1. Grk. rpdcwzov (in Hom. always pl.), fr. wpos ‘toward’ and deriy. of é7- (IE *ok*-) in dpouat fut. of dpaw ‘see, look’, doce ‘eyes’, dp also ‘face’, etc. (15.51). Hence orig. the ‘appearance, look’.
5667:Goth. wlits, andawleizn, ON andlit (Sw. anlete arch.), OK anduilita, MHG antlitze, NHG anilitz, fr. the root seen in ON lita, OF wilttan ‘see, look’ (15.51). Walde-P. 1.293. Falk-Torp 28. Feist 48, 571f. Weigand-H. 1.78.
5668:OE ansjn (usual word), OHG anasi- uni (‘face’ in Notker, etc.; cf. Goth. anasiuns ‘visible’), OHG, MHG gesiht, NHG gesicht, also (but less: common’ in this sense) OHG anastht, MLG ansichte (> Dan. ansigt, Sw. ansikte) and MHG angesthte, NHG angesicht, all fr. the Toot of OE ston, OHG sehan ‘see’ (15.51). Weigand-H, 1.61, 704. Paul, Deutsches
5673:5. Lith. veidas, fr. the root *wetd- in Grk. déov ‘saw’, eldos ‘appearance, form, kind’, Lat. vidére ‘see’, Lith. veizdéti ‘look’, etc. (15.51). Walde-P. 1.239.
5677:7. Skt. antka- (RV ‘face’ lit. and fig.), Ay. ainika- (Barth. 125), also Skt. prattka- ‘front’ and sometimes ‘face’ epds. with -tka-, fr. a form of IE *okv- ‘see’ as in Skt. zks- ‘see, look’ (15.51). Cf. Grk. rpécwrov (above, 1).
5902:Br. skouarn, Corn. scovarn, W. ysgy- farn (obs.), etym. dub., but perh., fr. a *skeu- beside IE *keu- in Grk. xotw ‘per- ceive, hear’, Lat. cavére ‘beware’, Goth. hausjan ‘hear’, OF scéawian ‘look at’, etc. (15.41, 15.52). Henry 243. Win- disch ap. Ernault, Dict. étym. 377. Less probably Pedersen 2.53.
6952:4. Ir. atsling, etym. dub., perh. cpd. : sellaim ‘look’ (15.52). Stokes ap. Mac- bain 12.
11443:2. Lat. speculum, fr. *spec- ‘look’ in epds. -spicere, etc. (15.52). Hence It. specchio, Sp. espejo, OHG spiegal, MHG, NHG, Du. spiegel, MLG spégel (> ON spegill, Dan. spejl, Sw. spegel, Lett. Spiegelis). Ernout-M. 961. REW 8133. Falk-Torp 1115.
11444:OFr. miradoir, mireor, mirour (> ME mirour, NE mirror), Fr. miroir, fr. *mirdtorium, deriv. of Lat. mirare (mirarz) ‘wonder at’ in the later sense of ‘look’ as in It. mirare, Fr. mirer, etc. (15.52). REW 5603. NED s.v. mirror.
11447:W. drych (also ‘sight, appearance’) : Ir. drech ‘face, appearance’, Grk. dé¢pxo- Hat, Skt. dr¢- ‘see’, etc. (15.51). Walde- P. 1.807. Pedersen 1.42,
11456:6. ChSl. zricalo (Supr.), SCr. 2rcalo, Boh. zrcadlo, Pol. zwierciadto, Russ. zer- kalo, fr. the root of ChSl. ziréti, etc. ‘look’ (15.52).
11457:ChSI. *ogledalo (not quotable, but cf. Rum. oglindd), SCr. ogledalo, fr. ChSl. gledati, ete. ‘look’ (15.52). Berneker 302.
11458:7. Skt. ddarca-, fr. a-drg- epd. of arg ‘see’ (15.51). Also ditmadarca- with atman- ‘self’. ;
13113:SEE
16484:7. Skt. pariks-, lit. ‘look around’, hence ‘inspect, examine, try’, cpd. of iks- ‘see, look’ (15.51).
19403:Boh. hledati = ChSI. gledati, SCr. gledati ‘look at’, etc. (15.52). Berneker 302.
23331:1, Grk. ofa, Dor. cayua, fr. *dyd-~men- : Skt. dyad-na- (the oft quoted dya-man- seems to be a ghost word) ‘thought, re- flection’, but orig. ‘observation’, fr. dh, dhya- ‘think’, orig. ‘observe’ : Av. di- ‘look at, observe’ (15.51). Walde-P. 1.832. Boisacq 861.
25854:15.51 SEB
25855:15.52 Loox (vb.), Loox at
26319:15.51 15.52 SEE LOOK (vb.), LOOK AT
```


## [2026-09-14T02:34:03.248Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\n# find section 15.52 LOOK discussion\nfor i,l in enumerate(lines):\n    if 'spek' in l or ('specere' in l and 'Lat' in l) or 'skeptomai' in l.lower():\n        if 13000 < i < 14000:\n            print(i, l[:400])\nEOF\ngrep -n \"Lat. specere\\|IE \\*spek\\|\\*spek-\" SYN.txt | head -10",
 "description": "Find Buck discussion of spek-"
}
```


### [2026-09-14T02:34:04.528Z] TOOL RESULT

```
26377:3. IE *spek-. Walde-P. 2.659f. Er- nout-M. 960 ff.
26378:Lat. specere, spicere, mostly in cpds., of which for simple ‘look’ esp. aspicere, whence aspectus sometimes for subj. ‘sight’, usually obj. ‘look, appearance’, as also speciés; Grk. oxérrouat (for *orexrouat) ‘look carefully’, later ‘con- sider’; OHG spehon ‘look at carefully’, NHG spdhen, etc. (NE spy through OFr. espier); Skt. pag- (spac- in some forms), usual word for ‘see’ in present, Av. spas- ‘look upon, observe, regard’.
30550:OHG spahi, MHG spahe : ON spar ‘prophetic’, spd ‘prophesy’, OHG spehon ‘look at, spy’, Lat. specere ‘look at, be- hold’. Walde-P. 2.660.
```


## [2026-09-14T02:34:12.547Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:26377]); leaf=pre.count('\\f')\nprint('SYN leaf',leaf,'printed p.',leaf-24)\nEOF\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor n in (663,664,665):\n    p=pages[n]\n    if 'spek' in p or 'spe k' in p:\n        print('=== leaf',n,'printed ~',n-5)\n        idx=p.find('spek')\n        print(p[max(0,idx-1500):idx+2500])\n        break\nEOF",
 "description": "Find Buck page and Walde-Pokorny II 659"
}
```


### [2026-09-14T02:34:13.744Z] TOOL RESULT

```
SYN leaf 1120 printed p. 1096
leaves 725
=== leaf 663 printed ~ 658
                                   speud- — spek-                           659

„lfager‘ 118 W.         anderer Anschauung entsprungen, s. u. spei- „spitz“) ;
                  ist wohl

Tielleicht mir. sen „Netz“ (wenn *spig-no- „das ausgespreitete'^ Stokes BB.
19, 108).


spend- „drucken, pressen; iibertragen: mit STachdruck betreiben (urgere
     opus), eilen (s’empresser).
   Gr. onsvdco „spute mich, eile; bemuhe mich, bin emsig, strenge mich
an, strebe; trans, treibe an, beschleunige, arbeite auf etwas eifrig hin‘^,
Gdbed. „drangen, driicken^" noch in anovda^' alexQt^avog Hes. („Morser-
keule" als „Zerdrucker“) ; ojcovdr] „Eile, Hast; Eifer, Bestrebung‘‘, gjtov-
daiog „eilig, eifrig, tatig, fleiBig^,   onovddCco „sich sputen, emsig sein, mit
Eifer betreiben, jemandes Interesse fordern^^;
  Lit. spdiidziu, spdusti „drucken“, iter, spdudyti, spaudd „Presse^‘ usw.,
spudinti „eilen, sich davonmachen^, paspudeti „sicb qualen, sich abmiihen'*
(Pick BB. 29, 197, Bechtel Lexil. 302);
   alb. piine „ Arbeit, Geschaft“ (^spudna, G. Meyer Wb. 357) ; wohl auch
arm. poif^ gen. putoy „Eifer“ (Hiibschmann Arm. Gr. I 501 ; t statt t            =
idg. d durch Ass, an den aspirierten Anlant?      Zw. bei Meillet Msl. 10,
277, Pedersen KZ. 38, 200; Perssons Beitr. 416 Verb, als phouqdo-           mit
gr. G(pvC(o befriedigt nicht).
   Yielleicht 6?-Praes. einer AYz. speti-\ wie zu spei- „sich ausdehnen“   auch
bait. spaid‘ ,,drucken,  drangen“ gehort, konnte auch speti- denselben Bed.-
TJmfang wie spei- gehabt haben (s. Persson AVzerw. 144, 290, Beitr. 4l4f.^
717): dann ware (mit dem Sinne von sA, sphdvdyati                 sigs, spdwan-

gelingen, welche nicht mit Zuversicht unserer AYz. speu- zuzuteilen sind)
anzureihen, gr. iocpvdcopevog „vollgestopft mit Essen“, o(pvdd)v      *
                                                                        loxvQog,
evQcoorog^ oxlrjQog Hes., diaa(pvdd)oai      avg^oat Hes. (aber nicht dopvg
                                             *




„Hufte“, s. u. odego-) mit asp, Anl. (s. u. spei)\
   AV'egen der Bed. viel unsicherer opvl^co „zucken, heftig schlagen (vom
Blute), sich heftig bewegen, fiebern, eifrig streben^^, opvypog, opvgig
„Zuckung, Pul8.“ Ohne anl. s- (allenfalls durch Hiss, eines '^{s)pmd-s-ol,y
dan. f^ire ,jemanden hinauswerfen, mit Larm und Hast fortjagen“, norw.
mdartl. f^yra „treiben'‘, schwed. fdsa ds., fos „Eile‘‘ („*drucken“; Liden
PBrB. 15, 520 f., s. auch Falk-Torp s. v,), auch engl.
   AVie Persson spei- „8pitz“ als „langgestreckt'‘ mit spei- „z
```


## [2026-09-14T02:34:17.918Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[664]\nprint('=== leaf 664 printed ~659-660')\ni=p.find('spek')\nprint(p[:4000])\nEOF",
 "description": "Print WP II p.659-660 spek-"
}
```


### [2026-09-14T02:34:19.007Z] TOOL RESULT

```
=== leaf 664 printed ~659-660
                                                                                             ;




660                                         speg-    — {s)pen-
      Gr. ox£7tToiJ.at   5
                             ,schaue‘^   (oxen- umgesfcellt aus
                                                            s. zuletzt Hirt
IF. 21, 172;         nicht nach Fick137 zu axenag)^ oxonog „Spaher; ZieP,
oxojielv jjbeobachten, zielen, untersuchen“, oxonij^ oxomd „Warte“, oxeyjig
„Betracbtung, tTberlegung, Untersucbung“ ; alb.                               „icli   sah“ (*(5)poi-s-;
G. Meyer Wb. 323.
      Lat. speciOj -ere^  -ctum „sehen“ [coyi-spicio usw.), epecio, -are „an-
                               -cci,

schaueii“, species „das Seben,  Aublick, Gesicht, Anseben, Ausseben, Er-
scheinung“, au-y harii-spex^ specus^ -as .,H6ble‘‘ (vgl. onri „Lucke, Offnung,
Locb“, ir. dtrc „Auge'‘ und ,jHohle“), speculum „Spiegel“, speculor^ -arl
„spaben^^ (s, zu dessen Bildung Samuelsson Gl. 6, 246)           umbr. speture        ;


3
    ,spectori“;

  Abd. speJion „spabeii“ von speJia f, „prufendes, aufmerksames Betracb-
ten, Untersucbung,   Auskundscbaftung, Aufpassen*'; aisl. spa „Wabrsagung“
{*spaho:gr, oxonrj)^ spa „wabrsagen“ {^spalion^ Denominatio), spar „wabr-
sagend, prophetiscb“ (^spalca-s)]              as.    abd. spalii „klug, geschickt“.
      Anm. spasem „warte auf etwas‘' (Hubscbmann Arm. St. I 50, Arm. Gr.
I 492,    an Urverwandtscbaft zweifelnd) ist Iran. Lw.  Uber slav. pasti^      —
aucb „scbarf binseben“ s. u. poi-, pa- „Yieb weiden“. Vgl. Curtins 168,
Fick III ^ 506. Abnlicb *spey- (oder spay-^ spog-)^ s. d.


             (oder spdg- oder spog- j.scbarf bin-, zuseben“.
     Aisl.   spahr „weise, king, rubig,              sanft'^,   speki   f,   „Verstand, Weisbeit^^,
spekt (^spakipd)         f.   „Weisbeit'^, spehja „weismacben, besanftigen“
      abg. pazq, pa^iti „achten auf ^ mit sq „sicb                biiten''.

     Fick KZ, 22, 94, Falk-Torp             u. spag.       Abnlicb spek- „spahen'", s. d.


1.    (s)p6n- .jzieben, spannen“   und „spinnen“, indem die zu flecbtenden, spin-
        nenden, webenden Paden zuerst ausgespannt wurden, yfie aucb nach
        neuerer Weise der Aufzug des Gewebes ausgespannt ist, s. Liden
        IP. 19, 332f., Persson Beitr. 41 Iff., und vgl. dieselbe Anwendung von
        *ten- „dehnen, spannen'* fiir „spinnen, flechten^'. {s)pen- spe(i)- „ziehen“  :


        ==29a-„Vieb weiden, futtern“ :pen- „futtern“                =
                                                            ihd - hhen- „sprechen“?
                                                                                :



        (Persson aaO.). Vgl. das anders vokalisierte pdn- „Gewebe“.
      1. Formen obne -s-:

      Arm. Jianumy aor. hanay und henum, aor. Jieni „weben, zusammennahen";
erstere       Form    scbeint nacb den J2M-Yerben aus                   ^hanem^Wi. pmii urage-
bildet (wegen des feblenden s               —
                                     kaum mit germ, spannan aus *sp 9-nu-o
vergleicbbar, s. u. spei- „zieben‘^; nicht nacb Scheftelowitz BB. 29, 57 zum
bloB nominal belegten *pdn- „Gewebe“), letztere halt Scheftelowitz aaO.
fur aus hanum nach Jiesum „webe“ umvokalisiert, wabrend Pedersen KZ. 39,
414 die Kichtverwandlung von -en- zu -in- in nichtletzter Silbe fiir laut-
gesetzlich bait, wie in y-enum „stemme, stiitze mich mit Schultern oder
Handen an etwas*' (als „8ich anspannen^ Zs. mit henuml ebenso z-enum
jjscblachte, ziehe die Haut ab“ mit einer Bed. wie poln. od~piqc „ab-
schnallen“? konnen im Yokal jedenfalls nicht vom ganz bedeutungsver-
schiedenen hesum beeinfluBt sein).
```


## [2026-09-14T02:34:25.070Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[663]\ni=p.rfind('spek-')\nprint(p[-1800:])\nEOF",
 "description": "Print end of WP II p.659"
}
```


### [2026-09-14T02:34:26.153Z] TOOL RESULT

```
en, welche nicht mit Zuversicht unserer AYz. speu- zuzuteilen sind)
anzureihen, gr. iocpvdcopevog „vollgestopft mit Essen“, o(pvdd)v      *
                                                                        loxvQog,
evQcoorog^ oxlrjQog Hes., diaa(pvdd)oai      avg^oat Hes. (aber nicht dopvg
                                             *




„Hufte“, s. u. odego-) mit asp, Anl. (s. u. spei)\
   AV'egen der Bed. viel unsicherer opvl^co „zucken, heftig schlagen (vom
Blute), sich heftig bewegen, fiebern, eifrig streben^^, opvypog, opvgig
„Zuckung, Pul8.“ Ohne anl. s- (allenfalls durch Hiss, eines '^{s)pmd-s-ol,y
dan. f^ire ,jemanden hinauswerfen, mit Larm und Hast fortjagen“, norw.
mdartl. f^yra „treiben'‘, schwed. fdsa ds., fos „Eile‘‘ („*drucken“; Liden
PBrB. 15, 520 f., s. auch Falk-Torp s. v,), auch engl.
   AVie Persson spei- „8pitz“ als „langgestreckt'‘ mit spei- „ziehen“ und „sich
ausdehnen*' gleichsetzt, zieht er zu unserm speud- auch ahd. spio^^ aisl.
spjdt „Spie6‘‘, aisl. spyta „Pflock, ^Tagel zum Befestigen“, norw. mdartl.
spjdte „spitzer Keih‘ (mit anderem Dental norw. spaud „dunne Stange“,
schwed. spo, alter spade „Rute, Gerte“; s. auch AV'ood a* No. 560, Falk-
Torp u. spyd; SpieB ist nicht mit otievSco und f^ysa unter einer Gdbed.
„Stachel    —anstacheln*^ zu verb, nach Liden aaO. und Noreen Ltl. 192)?.,


spek- „spahen, scharf hinsehen‘^
  Ai. spdcati (Dhatup.), pagyati „sieht“, ptc. spastd-Ji (= av. spasta-^        lat*
spectus\ spat „Spaher“ (=av. spas^ lat. au-, haru-spex\ spaga-h ds.             gr.
                                                                           (:
oxo7tog)y av. spasyeiti „spaht*’ (= lat. specio^ gr. axhuojaai)^ ‘Syas „SpaheP‘,
spastar ds. (= lat. -spector^ umb. spetur-e) spasan- „hinspahend auf“ (= ahd.
speJio „Spaher“).
```


## [2026-09-14T02:34:37.018Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%84%D8%B3%DA%A9%D9%88%D9%BE",
 "prompt": "Give the Persian entry تلسکوپ: etymology (source language, e.g. French télescope or Russian), and meaning. Quote the etymology exactly."
}
```


## [2026-09-14T02:34:38.180Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/t%C3%A9lescope",
 "prompt": "Give the French entry télescope: etymology (New Latin telescopium / Greek), and meaning. Quote the etymology exactly. Also mention microscope if present."
}
```


### [2026-09-14T02:34:39.854Z] TOOL RESULT

```
# Persian Entry: تلسکوپ

**Etymology:** The word is "Borrowed from English _telescope_."

**Source Language:** English

**Meaning:** According to the entry, تلسکوپ (teleskop) means "telescope" in Iranian Persian.
```


### [2026-09-14T02:34:43.532Z] TOOL RESULT

```
# French Entry: télescope

**Etymology:** From _[télé-](/wiki/t%C3%A9l%C3%A9-#French "télé-")_ +‎ _[\-scope](/wiki/-scope#French "-scope")_.

The page does not provide the New Latin or Greek origins explicitly; it only indicates the word combines the prefix "télé-" with the suffix "-scope."

**Meaning:** The entry provides two definitions:
1. An archaic term for a spyglass
2. An astronomical instrument used for observing distant objects in astronomy

**Microscope:** Microscope is not mentioned on this page.
```


## [2026-09-14T02:34:50.030Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D9%84%D8%B3%DA%A9%D9%88%D9%BE/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for تلسکوپ including its origin tag (e.g. [فر.] French or [انگ.] English) and definition. Also any دهخدا note on origin. Quote the Persian text."
}
```


### [2026-09-14T02:34:55.576Z] TOOL RESULT

```
# فرهنگ معین Entry for تلسکوپ

**Origin Tag:** [فر.] (French)

**Definition:** "(تِ لِ) [فر.] (اِ.) دوربین بزرگ که با آن ستارگان را رصد می کنند."

This translates to: a large optical instrument used for astronomical observation of stars.

**Dehkhoda Note on Origin:**

According to the Dehkhoda dictionary section, the word entered Persian from French. The comprehensive entry explains that specialists employ two types: the refracting telescope (منکسرکننده) with lenses, and the reflecting telescope (منعکس کننده) utilizing mirrors. The refracting variety features an objective lens positioned at the upper end of a metal tube, which gathers light rays to form an image viewed through an eyepiece lens positioned at the lower end.
```


## [2026-09-14T02:35:07.092Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/spe%E1%B8%B1-\" \\\n\"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%A7%D8%B3\" \\\n\"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3\" \\\n\"https://en.wiktionary.org/wiki/%D8%A3%D8%B3%D9%82%D9%81\" \\\n\"https://en.wiktionary.org/wiki/%E1%BC%90%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82\" \\\n\"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%BF%CF%80%CF%8C%CF%82\" \\\n\"https://en.wiktionary.org/wiki/specio\" \\\n\"https://en.wiktionary.org/wiki/%D8%AA%D9%84%D8%B3%DA%A9%D9%88%D9%BE\" \\\n\"https://en.wiktionary.org/wiki/t%C3%A9lescope\" \\\n\"https://www.etymonline.com/word/bishop\" \\\n\"https://www.etymonline.com/word/telescope\" \\\n\"https://abadis.ir/fatofa/%D8%B3%DA%A9%D9%88%D8%A8%D8%A7/\" \\\n\"https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/\" \\\n\"https://abadis.ir/fatofa/%D8%AA%D9%84%D8%B3%DA%A9%D9%88%D9%BE/\" \\\n; do python3 tools/fetch_source.py \"$u\" --note \"page 466, root Spek: verification of *speḱ-, sepās/pāsbān, sekubā/osqof, telescope/microscope\" 2>&1 | tail -2; done",
 "description": "Archive all consulted web pages"
}
```


### [2026-09-14T02:35:16.537Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3431fb000748a316.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e1b1282cb4d6b34f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/059f7be629586a25.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d00de371dde26c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a0148b42f0da0f99.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b1d90ae35077719.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5465ecfc710b4b17.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ffc28e171c73b4c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/31eec251e2fc6412.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9619e70c6866e11c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ea3ffeca59653da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/afa4cdb125b9d9f9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70f7bc6e05a1d642.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/824947dba031ecce.txt
```


## [2026-09-14T02:35:26.890Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN bishop/episcopal/scope ===\"; grep -n \"bishop,  n\\|episcopal,  adj\\|scope,  n\\|species,  n\" KLN_1966.txt | head\necho \"--- KLN line with 'Gk. episkopos' ---\"; grep -n \"episkopos\" KLN_1966.txt | head -5\necho \"=== SKT spy/bishop ===\"; grep -n \"^SPY\\|^BISHOP\\|^SCOPE\\|^SPECIES\" SKT.txt | head\necho \"=== LKT bischof ===\"; grep -n -i \"usquf\\|bischof\\|episkopos\" LKT.txt | head",
 "description": "Grep Klein, Skeat, Lokotsch"
}
```


### [2026-09-14T02:35:26.995Z] TOOL RESULT

```
=== KLN bishop/episcopal/scope ===
3333:archbishop,  n.  —  ME.  archebischop ,  fr.  OE.  arce- biscop,  fr.  Eccles.  L.  archiepiscopus,  fr.  Eccles. Gk.  apxt£mcnco7ro?,  lit.  ‘chief  bishop’,  fr.  Gk. apyi-  (see  archi-)  and  Imaxonoc,  ‘bishop’.  See
4476:baroscope,  n.,  an  instrument  showing  the  changes of  the  pressure  of  the  atmosphere. — Compound¬ ed  of  baro-  and  Gk.  -cntimov,  fr.  oxorreiv,  ‘to look  at,  examine’.  See  -scope.
5049:bioplast,  a  particle  of  bioplasm  (biol.)  —  Com¬ pounded  of  bio-  and  Gk.  -7rXa<JTog,  fr.  TrXaairo?, ‘molded,  formed’.  See  -plast. bioscope,  n.,  a  biograph.  —  Compounded  of  bio- and  Gk.  -oxAmov,  fr.  ctxotteTv,  ‘to  look  at, examine’.  See  -scope.
5065:bisect,  tr.  v.,  to  cut  in  two.  —  Formed  fr.  bi-  and L.  secare,  pp.  sect  us,  ‘to  cut’.  See  section. Derivatives:  bisect-ion,  n.,  bisect-or,  n. bisexual,  adj.  —  Formed  fr.  bi-  and  sexual, bishop,  n.  —  ME.  biscop ,  bischop,  fr.  OE.  bis- ceop,  biscop,  fr.  L.  episcopus,  ‘overseer,  super- intendant’,  in  Eccles.  L.,  ‘bishop’,  fr.  Gk.  £-1- axottoq,  ‘overseer’,  fr.  km,  ‘on,  over’,  and  ctxottoc, ‘watcher’.  See  epi-  and  -scope  and  cp.  episcopal. Cp.  also  obispo.
7586:chromatophore,  n.,  a  pigment  cell.  —  Compound¬ ed  of  chromato-  and  -phore. chromatoscope,  n.,  an  instrument  for  combining light  rays  of  different  colors  into  one  compound color.  —  Compounded  of  chromato-  and  Gk. -oxo-tov,  fr.  crxoTreiv,  ‘to  look  at,  examine’.  See -scope.
7606:Derivatives :  chronometr-ic,  chonometr-ic-al, adjs.,  chronometr-ic-al-ly,  adv.,  chronometr-y,  n. chronopher,  n.,  an  instrument  used  to  broadcast time  signals  by  electricity.  —  Compounded  of Gk.  ypovoc,  ‘time’,  and  the  stem  of  <p£peiv,  ‘to bear,  carry’.  See  chrono-  and  bear,  ‘to  carry’, chronoscope,  n.,  an  instrument  for  measuring  mi¬ nute  intervals  of  time.  —  Compounded  of chrono-  and  Gk.  -oxomov,  fr.  oxottsTv,  ‘to  look at,  examine’.  See  -scope.
8857:consound,  n.,  a  plant  supposed  to  have  healing qualities;  the  comfrey.  —  OF.  consolde,  con- soulde,  fr.  L.  ednsolida,  ‘comfrey’,  lit.  ‘the strengthening  plant’,  fr.  consolidare,  ‘to  make firm  or  solid’.  See  consolidate,  v. conspecies,  n.,  a  fellow  species  of  the  same  genus. —  Formed  fr.  con-  and  species, conspecific,  adj.,  of  the  same  species.  —  Formed fr.  con-  and  specific.
10096:cymophane,  n.,  a  wavy  variety  of  chrysoberyl {mineral)  —  Compounded  of  Gk.  xupa,  ‘wave’, and  the  stem  of  ipalvsiv,  ‘to  show’,  (paivcoOat, ‘to  appear’.  See  cyma  and  phantasm, cymoscope,  n.,  a  device  for  detecting  electric waves.  —  Compounded  of  Gk.  xupia,  ‘wave’, and  -onimov,  fr.  oxotteiv,  ‘to  look  at,  examine’. See  cyma  and  -scope.
12583:ebullient,  adj.,  boiling  up,  exuberant.  —  Lit. ‘bubbling  over’,  fr.  L.  ebulliens ,  gen.  -entis,  pres, part,  of  ebuliire,  ‘to  boil  up,  bubble  over’,  fr.  -e and  bullire,  ‘to  boil,  bubble’.  See  boil,  v. ebullioscope,  n.,  an  instrument  for  indicating  the boiling  point  of  liquids.  —  A  hybrid  coined  fr. L.  ebuliire,  ‘to  boil  up’,  and  Gk.  -oxornov,  fr. oxotteIv,  ‘to  look  at,  examine’.  See  prec.  word and  -scope.
13131:endoscope,  n.,  an  instrument  for  examining  the interior  of  cavities  in  the  body  (med.)  —  Coined by  its  inventor  Desormeaux  in  1852  fr.  endo-
--- KLN line with 'Gk. episkopos' ---
=== SKT spy/bishop ===
16645:SCOPE.
17959:SPECIES.
=== LKT bischof ===
2403:1006.  Ar.  kä'id: 'Befehlshaber'  [vom  Vb.  käda  'leiten, regieren'];  hieraus  mit  ar.  Art.  sp.  al- caide  'Kommandant  einer  Festung',  pg. 'dass.,  Richter'  [infolge  Kontamination mit  al-kadiy  s.  hier  Nr.  984],  engl,  al- caide,  alcalde  'Festungskommandeur, höchster  Zivilbeamter  einer  Stadt;  Ge- fängniswärter'; siz.  caJiiM 'Rädelsführer' [alt  gaitu  'Richter'],  kat.  sp.  cayado, gayato,  pg.  cajado  'Hirten-  oder  Bischofs- stab' [da  der  Hirle  das  Haupt  oder  der Führer  seiner  Herde  ist].  |DE  79. Eguilaz  126.  ML  6898.  GrSVociSic 229.  GIBBS  in  American  Journal  of Science  &  Arts  XXXIII,  324.
```


## [2026-09-14T02:35:28.478Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY ===\"; grep -n \"پاسبان\\|سپاس\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY latin index ===\"; grep -n -i \"spek\\|spas\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-14T02:35:28.555Z] TOOL RESULT

```
=== ARY ===
40:باسپاس از ۴۰۱ دب
1230:است و من با سپاسمندی و ذ کر هر یک از مراجع خود از این پژوهشها بهره گرفنه‌ام. ولی چون بیشتر
12645:۱- چم‌های گوناگون این واژه در زبان‌های این فهرست؛ خوشایند» تعریف» نحسین» لطف» سپاس؛ عزیز
=== ARY latin index ===
2371:THE AMERICAN HERITAGE DICTIONARY) ASPAST s(PAHLAVI) 5 hq
3176:cast eals 'BABR" 20 4 1, oly gg! MACKENZIE (PV spas Kia icon 02
4296:ESPY, SPY (0:1) j!}(ENGLISH) g-lS\ PATHRA, SPASYEITI
4303:‘REFERENCES aenthag sPASATI, PASYATI, SPAS., PAS-
4305:POKORNY: 984 SPASEM ARMENIAN) .¢s,l
10238:SPASOX, PASSOX :aT 5) cel vst SS "gre! y "3h" lat aly 5I feel” pos Godly “A
```


## [2026-09-14T02:35:35.672Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('\\n'.join(lines[4285:4320]))\nEOF",
 "description": "Print Aryanpur index context"
}
```


### [2026-09-14T02:35:36.806Z] TOOL RESULT

```
SKEAT: = (PART) 431 (PART) 759, (PROPORTION) 850
| AMINDAROV: (PART) 265 DELAMARRE:
i) ebb oby (PART, SALAIRE) 203
MACKENZIE: (PART 126
7 teetloa
ap Hal ee Sale OU 42 05a ol
OF glad Ob5 2 5 cal ee
PPI i, OU5 09 0319 gal oe
eS
SPAHEN ~ (GERMAN) glast AAVESTAN) glues!
ESPY, SPY (0:1) j!}(ENGLISH) g-lS\ PATHRA, SPASYEITI
SPAA (DANISH) \ails *PASA (OLD PERSIAN) shee!)
SPA (SWEDISH) So yo (PAHLAVI) «53h
SPA NORWEGIAN) 5335 PAS, PASBAN
SPIEDEN (DUTCH) sacha PAS-, PASVAN (KURDISH) 52,5
PASHE: ALBANIAN) giT PAK s(TOKHARIAN B) B (5 ,\os
(SANSKRIT) cy Sie
‘REFERENCES aenthag sPASATI, PASYATI, SPAS., PAS-
pale ne Sncimanehiane
POKORNY: 984 SPASEM ARMENIAN) .¢s,l
BARNHART: (SPY) 1053} GREER) lin 3
DELAMARRE: SKOPEIN, SKEPTQMAL ; © “8
(OBSERVER, EPIER) 283 SPECIO, SPECERR” = LATIN) ag
MACKENZIE: (PAS, PASBAN) 65 EPIER (gla jIMPRENCH) «J
ONIONS: (SPY) 858 (OLD SCANDINAVIAN) 4S.ghes!
SKEAT: (SPY) 593 SPA, SPEJA
ror i gbU bly OLD HIGH GERMAN) op glalT
SPEHON
|
[pdf page 151]
pre eet | oy
ig'e FIERSIN' HOLD ENGLISH) 7S gS PASHNA AVESTAN) glee 3h
PASHNAG, PASHNAK:(PAHLAVI) 5 jy
‘REFERENCES . bethany KURDISH) 53,5
DELANARRE: ===S=S*~*~« PENI, PENI, PASUNE
```


## [2026-09-14T02:35:52.056Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nlast=None\nfor i,l in enumerate(lines[:4300]):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: last=m.group(1)\nprint('pdf page for line 4296:',last)\n# also look for the Persian headword lines just above\nprint('\\n'.join(lines[4270:4296]))\nEOF",
 "description": "Find ARY pdf page"
}
```


### [2026-09-14T02:35:53.140Z] TOOL RESULT

```
pdf page for line 4296: 150
PARTE (RUMANIAN) ley) PART 4BALUCHI) gh
PARTE, PARTIR:(PORTUGUESE) Jl PARAY AFGHAN) (2-4) lai)
PART (1 D(ENGLISH) Si} PORTA, SANSKRIT) ty Sue
PERK, PIRKTI :(LITHUANIAN) gi} PURTI-, PURTIS
RANN HOLD IRISH) aS 5414! s(GREEK) gy
PHAN WELSH) «5 5 PERASO, EPERASA
RANNOU H(BRETON) 5.2 PARS, PARTIS, PORTIO <(LATIN) SY
PARSH., PARSIYA — (HITTITE) ca» (FRENCH) «il
PART, PARTIE, PARTIR
[pdf page 150]
—
YOY f_glassty 2 4) nl
BUCK: (PART)933-934 ‘REFERENCES beth
ONIONS: “powory; SSsS~S~S~«SY
(PART) 653-654, (PORTION) 698 BARNHART:
SKEAT: = (PART) 431 (PART) 759, (PROPORTION) 850
| AMINDAROV: (PART) 265 DELAMARRE:
i) ebb oby (PART, SALAIRE) 203
MACKENZIE: (PART 126
7 teetloa
ap Hal ee Sale OU 42 05a ol
OF glad Ob5 2 5 cal ee
PPI i, OU5 09 0319 gal oe
eS
SPAHEN ~ (GERMAN) glast AAVESTAN) glues!
ESPY, SPY (0:1) j!}(ENGLISH) g-lS\ PATHRA, SPASYEITI
```


## [2026-09-14T02:37:34.146Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndef leaf(fn, lineno):\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    return '\\n'.join(lines[:lineno]).count('\\f')\nprint('IEC leaf',leaf('IEC.txt',16774),'-> printed ~',(leaf('IEC.txt',16774)-15)*2)\nfor ln in (3483,2983):\n    l=leaf('NYB_vol2_glossary.txt',ln); print('NYB line',ln,'leaf',l,'printed',l-8)\nfor ln in (5065,36462):\n    l=leaf('KLN_1966.txt',ln); print('KLN line',ln,'leaf',l,'printed ~',(l-12)*2)\nEOF\necho \"--- CHEUNG page for *spas ---\"\nsed -n '23070,23080p' CHEUNG.txt",
 "description": "Compute printed page numbers"
}
```


### [2026-09-14T02:37:35.562Z] TOOL RESULT

```
IEC leaf 691 -> printed ~ 1352
NYB line 3483 leaf 194 printed 186
NYB line 2983 leaf 167 printed 159
KLN line 5065 leaf 103 printed ~ 182
KLN line 36462 leaf 795 printed ~ 1566
--- CHEUNG page for *spas ---
efserun/efsarst, aefsard ‘to kick with the feet’ || (+ *upa-) Sh. bispär, Khf. bispar, 


*spas 353 


Rosh. bispar, Yzgh. baspur ‘a kick’ || (+ *ni-) Sh. nixpar-/nixpud, Sariq. naxpe(j)-/ 
naxig, (Shaw) naxpor-/naXpug ‘to tread down, trample with the foot’, Wa. nasp(a)r-/ 
naspard- ‘to kick (with the feet)’. 0 The existence of Wa. bisper ‘to kick’ as cited by 
Lorimer has not been confirmed by Wa. informants, v. Steblin-Kamenskij 1999: 
250, s.v. пәѕр(ә)г-.
```


## [2026-09-14T02:37:40.501Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23110,23165p' CHEUNG.txt\nmkdir -p ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg466hi.png ocr/BOOK/466.png && ls -la ocr/BOOK/466.png",
 "description": "Print Cheung *spas and save page PNG"
}
```


### [2026-09-14T02:37:41.626Z] TOOL RESULT

```
*spas ‘to attend to; to serve’ 

*AVESTAN: spas- (spas-, spös-) ‘to attend to; to serve’ || (+ *abi-) ‘to set one’s sight 
on, aufs Korn nehmen?’ || (+ *aua-) ‘to catch the sight of, erspähen’ = Liste: 65 

Pres. {1} ia-: IND. 15р. OAv. spasiiä (Y 44.11), 3sg. Y Av. spasiieiti (Yt 10.82); Pres. {2} nu-: IND. 2pl. 
OAv. “spasnuda (Y 53.6), INJ. 3sg. YAv. auua.spasnaot (Yt 11.5); Partic.: pres. {1} YAv. spasiiant- (Yt 
11.14), pres. (a)them. red. ? YAv. hisposant- (Yt 8.36), med. YAv. hispdsomna- (Yt 10.45), perf. pass. 
Y Av. auui.spasta- (Yt 13.69). 0 For YAv. hisposant- cf. Kellens 1974: 115f. 


*MIDDLE PERSIAN: MMP ons ‘to serve’, MMP ‘sp’s, ВМР sp’s /späs/ ‘service, 


gratitude, thanks’ (LW) = DMMPP: 86 

Pres.: IND. 3sg. ‘spsyd 

*PARTHIAN: ‘sps- ‘to serve’, ’sp’s, sp’s ‘service’ || (+ *pati-) ? pdysp’s- ‘to pay 
attention’ — Ghilain: 51 f., 69 | DMMPP: 86 

Pres.: IND. 3р]. ‘spsynd; Partic.: perf. pass. ‘spyst 

*KHOTANESE: späs(S)- (sas-, s(p)as-) ‘to see; appear = SGS: 135 

*SOGDIAN: BSogd. ’sp’ys, BSogd. ’spys, CSogd. spys/spxs, MSogd. ’spys ‘to serve, 
honour, pay respect’, BSogd. ’sp’s, sp’s ‘service, honour’ || (+ *ham-) MSogd. 
"nspstqy, MSogd. ’spstky’, SSogd. ’nsp’st’ky’kh, SSogd. ’nspst’kyh ‘zeal, 


354 *spauc ? 


willingness to serve’. 9 The pret. stem (’)spxst- has given rise to a secondary pres. 
stem (CSogd.) sp(’)xs- (GMS: par. 599). 

Well attested Pres.: IND. 3sg. BSogd. 'sp'ysty,'spysty, 3р1. dur. SSogd. ’spys’nt ’skwn, SUBJ. 35р. 
BSogd. ’spys’t, etc. 

*BACTRIAN: OTIO-, MOTLO-, CATO- ‘to serve, worship’, «слтосо, OTAGO ‘service’ 
c» S-W, Bact.: 224b 

*NWIR: NP sipas ‘kindness, favour, thanksgiving’, NP sipasidan/sipas- (denomin.) 
*to praise (God) for benefits received; to implore assistance, grace, favour? 

*MISC: Arm. (LW) spasem ‘to serve’ (« WIr.), Toch. (LW) spaktam ‘service’, A 
spaktanik, B spaktanike ‘servant’ (< Bactr., cf. Schwartz 1974: 411). 

*SANSKRIT: spas ‘to observe, watch, spy’ (RV) || ("s-less" var.) pas ‘to see’ (RV+) 
= EWAia II: 107 

«PIE *speK- ‘to look around, take notice’ = LIV: 575 f. | Pok.: 984 

*IE COGNATES: Gr. скёлторол ‘I look around, look at’, Lat. speciö ‘to see’, OHG 
-rw-rw-r-- 1 sfmqrb sfmqrb 77713 Sep 13 22:37 ocr/BOOK/466.png
```


## [2026-09-14T02:37:54.740Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:46:36.871Z] AGENT

I'll write the verification file now.


## [2026-09-14T02:55:51.230Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-466.json <<'JSONEOF'\n{\n  \"pdf_page\": 466,\n  \"book_page\": 436,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Spek\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *speḱ- 'to look at, observe, spy' (Pokorny 984 spek- 'spähen, scharf hinsehen'; Walde-Pokorny II 659-660; Watkins/AHD spek- 'to observe'; LIV 575f.)\",\n      \"note\": \"Root, language label and gloss are all correct and the page reference is exact. Pokorny's IEW p. 984 has the headword 'spek- ,spähen, scharf hinsehen'; spek-s, spek-ōn-, spek-tor- ,Späher', spek-to- ,erspäht', spok-o-s ,Späher'' — Nourai's gloss 'to look, examine' is a fair English rendering. The chart's five primary branches (Avestan, Latin specere, Greek skopos, New Latin -scopium, Germanic *spehōn) reproduce Watkins's own arrangement of the root almost item for item. The one structural problem on this page is not the root but the reading of the arrows in the lower half: on the printed page the Arabic osqof box and the Latin micro-scopium box both hang off the GREEK box (a single line drops from the bottom-left corner of the Greek box and elbows into Old Persian skuba, Arabic osqof and Latin micro-scopium in turn), whereas the extracted JSON gives node #11 the parent #9 and node #13 the parent #0. See the per-node notes and the summary.\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ آغازین *speḱ- به معنی «نگریستن، پاییدن، دیده‌بانی کردن» ریشه‌ای است پذیرفته و استوار: پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» صفحهٔ ۹۸۴ آن را با همین صورت و همین معنا («spähen, scharf hinsehen») آورده و والده-پوکورنی (جلد دوم، ص ۶۵۹-۶۶۰) و واتکینز در پیوست ریشه‌های AHD نیز همان را تکرار کرده‌اند. بنابراین نام ریشه، برچسب زبانی «هندواروپایی» و معنایی که نورایی داده هر سه درست است و ارجاع POK:984 دقیقاً بر همان صفحه می‌نشیند. پنج شاخهٔ اصلی نمودار (اوستایی spas-، لاتینی specere، یونانی skopos، لاتینی نو -scopium و ژرمنی *spehōn) نیز همان تقسیم‌بندی واتکینز است. تنها اشکال ساختاری این صفحه در خوانش پیکان‌ها در نیمهٔ پایین نمودار است: در متن چاپی، جعبهٔ «عربی osqof» و جعبهٔ «لاتینی micro-scopium» هر دو از جعبهٔ «یونانی» منشعب می‌شوند، نه از «فارسی باستان skuba» و نه مستقیماً از ریشه.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/spe%E1%B8%B1-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:984\",\n          \"status\": \"supports\",\n          \"note\": \"Pokorny IEW p. 984 (POK_03.txt line 3040, between the printed page markers '984' and '985'): 'spek- ,spähen, scharf hinsehen'; spek-s, spek-ōn-, spek-tor- ,Späher', spek-to- ,erspäht', spok-o-s ,Späher'.' The page number Nourai gives is exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny II 659-660 (WLD_Bd2_pages.txt leaves 663-664)\",\n          \"stance\": \"supports\",\n          \"note\": \"'spek- ,spähen, scharf hinsehen'. Ai. spáçati (Dhatup.), paçyati ,sieht', ptc. spaṣṭá-ḥ (= av. spašta-, lat. spectus); spaṭ ,Späher' (= av. spas, lat. au-, haru-spex) ... av. spasyeiti ,späht' (= lat. specio, gr. skeptomai)' — the same material Pokorny 984 later condensed.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. spek- (AHD_watkins1985.txt line 979)\",\n          \"stance\": \"supports\",\n          \"note\": \"'spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon ... 2. Suffixed form *spek-yo- in Latin specere ... II. Extended o-grade form *spoko- metathesized in Greek skopos ... [Pok. spek- 984.]' Watkins cites exactly Pokorny 984.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IE Comparative Dictionary, s.v. spek- (1) (IEC.txt line 16774, p. ~1352)\",\n          \"stance\": \"supports\",\n          \"note\": \"'spek- (1) \\\"look, see, observe\\\". WP II, 659. Skt. spas, m. \\\"beholder\\\" ... Av. spas, m. \\\"spy\\\"; spasya, 1sg. \\\"wish to watch\\\"; Gk. cf. (metath.) sképtomai ...; Lat. specio, specére ...; OHG spéhon, MHG spëhen, wv. \\\"spy, watch\\\".'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 15.52 LOOK (vb.), paragraph 3 (SYN.txt line 26377, printed p. ~1096)\",\n          \"stance\": \"supports\",\n          \"note\": \"'3. IE *spek-. Walde-P. 2.659f. ... Lat. specere, spicere ...; Grk. sképtomai (for *spektomai) \\\"look carefully\\\" ...; OHG spehon \\\"look at carefully\\\", NHG spähen, etc. (NE spy through OFr. espier); Skt. paś- (spaś- in some forms) ...; Av. spas- \\\"look upon, observe, regard\\\".'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"spasyeiti; spas, spasânô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three Avestan forms are real and belong to one paradigm. The root is Av. spas- 'to spy out, watch, attend to' < PIIr. *spać- < PIE *speḱ-; the present stem is the *-ya- formation *spaś-ya-ti, whence 3sg. spasiieiti (Yt 10.82) — the chart's 'spasyeiti', a standard older transliteration. 'spas' is the root-noun spas- m. 'Späher, Wächter' (Yt 10.45, 46, 61), the exact counterpart of Skt. spaṭ and of the Latin second member in au-spex, haru-spex. 'spasânô' is not a separate lexeme but the nom. sg. masc. spasānō of the participial stem spasan- 'looking out for, watching over', best known from the Mihr Yašt epithet baēvarə.spasan- 'having ten thousand watchers' (Yt 10.24, 60, 82) — so the chart's gloss 'guard, watcher' fits both. The Old Avestan present spasiiā (Y 44.11) and the nu-stem spašnuθā (Y 53.6) show the same root in the Gathas, so the word is attested from the oldest layer of the language.\",\n          \"derivation_fa\": \"هر سه صورتی که نورایی در این گره آورده اوستایی و درست‌اند. ریشهٔ اوستایی spas- «پاییدن، دیده‌بانی کردن، در خدمت بودن» بازماندهٔ هندوایرانی آغازین *spać- و آن خود از *speḱ- هندواروپایی است. ستاک حالِ آن با پسوند *-ya- ساخته شده و صورت سوم‌شخص مفرد آن spasiieiti (یشت ۱۰ بند ۸۲) است که نورایی به شیوهٔ کهن‌تر spasyeiti نوشته است. «spas» نامِ ریشه‌ای spas- به معنی «دیده‌بان، پاسور» است (یشت ۱۰ بندهای ۴۵ و ۴۶ و ۶۱) و هم‌ارز دقیق spaṭ سنسکریت و جزء دوم au-spex و haru-spex لاتینی است. «spasânô» واژه‌ای جداگانه نیست، بلکه حالت فاعلی مفرد مذکرِ ستاک اسم فاعلی spasan- «نگرنده، پاینده» است که در ترکیب baēvarə.spasan- «دارندهٔ ده هزار دیده‌بان» (لقب میثره) بارها آمده است. چون این ریشه در گاهان نیز گواهی دارد (spasiiā در یسنا ۴۴ بند ۱۱)، کهنگی آن قطعی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/spe%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:984\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny 984 lists precisely these forms: 'av. spasyeiti ,späht' (= lat. speciō, gr. sképtomai), spas ,Späher', spaštar- ds. (= lat. -spector, umbr. spetur-e), spasan- ,hinspähend auf' (= ahd. spehō ,Späher')' (POK_03.txt line 3040).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW cols. 1613-1614 (BRT.txt lines 26860-26894; the column numeral '1612' stands at line 26825)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j., g. spas- V. \\\"spähen\\\". Praes. ... spasya- ... PPfP. spasta-'; then 'j. spas- m. \\\"Späher, Wächter\\\": spas (NS.) ... Yt 10.46 ... spasō (NP.) ... Yt 10.45. Zum V. spas-. — ai. spáś- m.'; and 'j. spasan- Adj. \\\"hinspähend (auf —)\\\"'. Nyberg independently cites this passage as 'Av. (1614) spas-'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung, Etym. Dict. of the Iranian Verb, s.v. *spas, pp. 353-354\",\n              \"stance\": \"supports\",\n              \"note\": \"'*spas \\\"to attend to; to serve\\\". *AVESTAN: spas- (spas-, spōs-) ... Pres. {1} ia-: IND. 1sg. OAv. spasiiā (Y 44.11), 3sg. YAv. spasiieiti (Yt 10.82) ... «PIE *speḱ- \\\"to look around, take notice\\\" = LIV: 575f. | Pok.: 984'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 659 (WLD_Bd2_pages.txt leaf 663)\",\n              \"stance\": \"supports\",\n              \"note\": \"'av. spasyeiti ,späht' (= lat. specio, gr. skeptomai), spas ,Späher', spastar ds. ... spasan- ,hinspähend auf' (= ahd. spehō ,Späher')'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"spâs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian spās [spʾs] is real and very well attested; MacKenzie's Concise Pahlavi Dictionary p. 76 has 'spās dāštan, ~ hangārdan: thank, give thanks. spās-dār [spʾsdʾl | N sip~] grateful, thankful.' Nyberg's glossary (II, p. 186) glosses it '1. thanks, gratitude ... 2. service' and derives it explicitly 'from Av. (1614) spas- \\\"to observe, to attend\\\"'. So the chart's arrow Avestan spas- → Pahlavi spās is what the Pahlavi lexicographers themselves draw. Formally MP spās continues an Old Iranian abstract *spāsa- (lengthened-grade *spās- to the root *spas-), and Cheung marks the Book-Pahlavi noun (LW), i.e. probably taken over from the Parthian ʾspʾs / spʾs 'service' of the north-west, which is why Manichaean MP also has ʾspʾs with the prothetic vowel that Nyberg calls 'the NW form'. One caveat on the chart's gloss: spās is a NOUN, 'service, gratitude' — 'to serve, wait on' belongs to the compound verb spās dāštan, and to the Armenian loan spasem 'I serve'.\",\n          \"derivation_fa\": \"واژهٔ فارسی میانهٔ spās (به خط پهلوی spʾs) واژه‌ای کاملاً گواهی‌شده است؛ مکنزی در «فرهنگ کوچک پهلوی» صفحهٔ ۷۶ ترکیب spās dāštan «سپاس داشتن، سپاسگزاری کردن» و مشتق spās-dār «سپاسگزار» را آورده و نیبرگ در واژه‌نامهٔ خود (بخش دوم، ص ۱۸۶) آن را «۱. سپاس، شکر ۲. خدمت» معنی کرده و صریحاً می‌نویسد که «از ریشهٔ اوستایی spas- (بارتولومه ستون ۱۶۱۴) \\\"پاییدن، در خدمت بودن\\\"» است. پس پیکانِ «اوستایی spas- ← پهلوی spās» همان چیزی است که پهلوی‌شناسان خود می‌کشند. از دید ساخت، spās بازماندهٔ نامی انتزاعی در ایرانی باستان به صورت *spāsa- (با واکهٔ کشیدهٔ ستاک) است؛ چونگ صورت پهلوی کتابی را «وام‌واژه» نشانه‌گذاری کرده، یعنی احتمالاً از پارتی ʾspʾs / spʾs «خدمت» به فارسی میانه راه یافته است، و از همین رو در فارسی میانهٔ مانوی نیز ʾspʾs با واکهٔ آغازینِ افزوده دیده می‌شود. یک نکتهٔ باریک: spās اسم است («خدمت، سپاس») و معنای «خدمت کردن» که نورایی نوشته، از آنِ فعل مرکب spās dāštan است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%A7%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:154\",\n              \"status\": \"partial\",\n              \"note\": \"Horn, Grundriss p. 154 (HRN.txt leaf 175) no. 698: 'sipās \\\"Dank\\\". phlv. spās, spāsdār; arm. spas-em \\\"aufwarten, dienen\\\", spas \\\"Dienst\\\".' The cited page therefore supports the Pahlavi form and its Armenian loan exactly. But Horn's continuation at the top of p. 155 is sceptical about the very arrow this node draws: 'Also zu aw. √spas, spasyeiti \\\"spähen\\\"? Sehr unsicher, Hübschmann, Armen. Stud., S. 50, No. 257.' Modern Iranian scholarship (Nyberg, Cheung, Wiktionary) has since settled on the connection Horn doubted.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 76 (PHD.txt leaf 97, running head 'spās dāštan 76 srōd')\",\n              \"stance\": \"supports\",\n              \"note\": \"'spās dāštan, ~ hangārdan: thank, give thanks. spās-dār [spʾsdʾl | N sip~] grateful, thankful. ~īh: gratitude.' The English-Pahlavi half adds 'thanks āzādīh, spās' and 'service paristagīh, paristišn, spās'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) p. 186 (NYB_vol2_glossary.txt leaf 194)\",\n              \"stance\": \"supports\",\n              \"note\": \"'spas [spʾs] 1. thanks, gratitude 127⁵ ... 2. service ... MPrth ʾspʾs \\\"service\\\", Arm. lw. spas id.; MPrs ʾspʾs \\\"service\\\" (S), ʾspʾs \\\"thanks\\\" (A-H II); ... NP sipās 1. \\\"grace, favour\\\", 2. \\\"praise, thanksgiving\\\"; from Av. (1614) spas- \\\"to observe, to attend\\\".'\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung s.v. *spas, p. 353\",\n              \"stance\": \"supports\",\n              \"note\": \"'*MIDDLE PERSIAN: MMP ʾsps- \\\"to serve\\\", MMP ʾspʾs, BMP spʾs /spās/ \\\"service, gratitude, thanks\\\" (LW)'; '*PARTHIAN: ʾsps- \\\"to serve\\\", ʾspʾs, spʾs \\\"service\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"sepâs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian سپاس sepās/sipās 'thanks, gratitude' continues Middle Persian spās without change of substance; the only development is the anaptyctic vowel that New Persian regularly inserts to break the inherited initial cluster sp-, exactly as in MP spāh > NP sipāh 'army', MP spihr > NP sipihr 'sky', MP spurdan > NP sipurdan. Semantically the Iranian word moved 'watching over, attendance' → 'service' → 'gratitude for service received', a shift already complete in Book Pahlavi (Nyberg glosses the MP noun 'thanks' first). The same Western Iranian word was borrowed into Armenian as spas 'service', spasem 'I serve, wait upon' — a loan Horn, Hübschmann and Mo'in all cite as proof of the Iranian pedigree. Wiktionary derives the modern word 'From Middle Persian spʾs (spās), from Proto-Iranian *spácati ... from Proto-Indo-European *speḱ-', which is the chart's chain.\",\n          \"derivation_fa\": \"«سپاس» فارسی نو دنبالهٔ بی‌واسطهٔ spās فارسی میانه است و تنها دگرگونی آوایی آن، افزوده شدن واکهٔ میانجی برای شکستن خوشهٔ آغازینِ sp- است؛ همان قاعده‌ای که spāh پهلوی را به «سپاه»، spihr را به «سپهر» و spurdan را به «سپردن» بدل کرده است. از نظر معنایی، راه واژه چنین بوده است: «پاییدن، در خدمت بودن» ← «خدمت» ← «شکرگزاری در برابر خدمت»، و این تحول در همان پهلوی کتابی به پایان رسیده بود، چنان‌که نیبرگ نخستین معنای spās را «سپاس، شکر» می‌آورد. همین واژهٔ ایرانی غربی به ارمنی نیز وام رفته است: spas «خدمت» و spasem «خدمت می‌کنم» — گواهی که هرن و هوبشمان و معین هر سه به آن استناد کرده‌اند. ویکی‌واژه نیز همین زنجیره را می‌دهد: فارسی نو ← فارسی میانهٔ spās ← ایرانی آغازین ← *speḱ- هندواروپایی. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%A7%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1086\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 2: the سپاس entry with Mo'in's etymological footnote is on BQT_v2_pages.txt leaf 548 (printed page ≈ 1088-1091 by the running-head formula; Nourai's 1086 is within the ±3 drift of this scan's offset plus the length of the entry). The footnote reads: '۴ - پهلوی spās، ارمنی spas-em (خدمت کردم، سپاس داشتم)، spas (خدمت)' — i.e. exactly the Pahlavi → Persian arrow Nourai draws, with the Armenian loan as corroboration.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 698, p. 154\",\n              \"stance\": \"supports\",\n              \"note\": \"'sipās \\\"Dank\\\". phlv. spās, spāsdār; arm. spas-em \\\"aufwarten, dienen\\\", spas \\\"Dienst\\\".'\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 76\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. spās-dār the New Persian continuation is marked '| N sip~', i.e. MacKenzie equates MP spās-dār with NP sipās-dār and therefore MP spās with NP sipās.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung s.v. *spas, p. 354\",\n              \"stance\": \"supports\",\n              \"note\": \"'*NWIR: NP sipas \\\"kindness, favour, thanksgiving\\\", NP sipasidan/sipas- (denomin.) \\\"to praise (God) for benefits received\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"pâsbân\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Pahlavi word is genuine — MacKenzie p. 65: 'pās [pʾs | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [pʾspʾn | M pʾsbʾn, N ~] guardian, watcher. ~īh: defence, protection.' It is pās 'watch' + the agent suffix -bān (< OIr. *-pāna- 'protecting'). What is disputed is the arrow: deriving pās/pāsbān from Avestan spas-. The standard Iranian handbooks derive pās from the root *peh₂- 'to protect' instead: Nyberg's glossary (II p. 159) states flatly 'pās [pʾs] watch, guard. — OP *pāça-, SW form of pāθra-, v. pahr. — MPrs pʾsbʾn \\\"watchman, guardian\\\"', i.e. MP pās goes back to an Old Persian *pāça- that is the south-western reflex of Avestan pāθra- 'protection'; Horn (no. 274, p. 62) has the same: 'pās \\\"Schutz\\\", pāsbān, pāsīden. aw. pāθra- \\\"Schutz\\\"; phlv. pās (Bund.), pāspān ... ai. pātra-.' Wiktionary follows them: 'From Middle Persian pʾs /pās/, from Old Persian *pāçah, from Proto-Iranian *páHθrah', ultimately PIE *peh₂- 'to protect'. On that view pās has nothing to do with spas- at all; the s of pās is from *-θr-, not the -s- of the spy-root, and the absence of initial s- is original, not a loss. Nourai is not alone, however: his source Tavoosi (SNS) does derive it from spas-, and Aryanpur's Persian IE dictionary (p. 151) files pās/pāsbān under Pokorny 984 while listing both PĀTHRA and SPASYEITI as Avestan comparanda — so a minority of Persian etymologists conflate the two roots. Modern scholarship prefers *pāθra-.\",\n          \"derivation_fa\": \"خودِ واژهٔ پهلوی جای تردید ندارد: مکنزی در صفحهٔ ۶۵ می‌آورد «pās [pʾs] پاس، نگهبانی؛ pāsbān [pʾspʾn] نگهبان، پاسدار»، و ساخت آن pās «پاس» + پسوند فاعلیِ -bān (از *-pāna- ایرانی باستان به معنی «نگاهدارنده») است. آنچه مورد اختلاف است، خودِ پیکان است، یعنی بازبردنِ pās و pāsbān به ریشهٔ اوستایی spas-. مرجع‌های معتبر ایرانی‌شناسی pās را نه از spas- بلکه از ریشهٔ *peh₂- «نگاه داشتن، پاییدن» می‌دانند: نیبرگ (بخش دوم، ص ۱۵۹) می‌نویسد «pās: پاس، نگهبانی — از *pāça- پارسی باستان، صورت جنوب‌غربیِ pāθra- اوستایی»، و هرن نیز در شمارهٔ ۲۷۴ (ص ۶۲) همین را دارد: «pās \\\"نگاهبانی\\\"، pāsbān، pāsīdan؛ اوستایی pāθra- \\\"پاسداری\\\"؛ پهلوی pās؛ سنسکریت pātra-». ویکی‌واژه هم همین زنجیره را می‌دهد: فارسی «پاس» ← پهلوی pās ← پارسی باستان *pāçah ← ایرانی آغازین *páHθrah ← *peh₂- هندواروپایی. بر این پایه، سینِ pās دنبالهٔ خوشهٔ *-θr- است نه سینِ ریشهٔ «پاییدن/جاسوسی»، و نبودِ s آغازین اصیل است نه حاصلِ افتادگی. البته نورایی تنها نیست: مأخذ خودش، یعنی واژه‌نامهٔ «شایست ناشایست» طاووسی، pāsbān را از spas- می‌گیرد و آریان‌پور نیز (ص ۱۵۱) پاس و پاسبان را ذیل پوکورنی ۹۸۴ آورده و هر دو صورت PĀTHRA و SPASYEITI را در کنار هم نشانده است. با این همه، پژوهش امروزی صورت *pāθra- را ترجیح می‌دهد و ادعای نورایی را در این گره رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SNS:117\",\n              \"status\": \"supports\",\n              \"note\": \"Tavoosi, Vāženāme-ye Šāyast ne Šāyast, s.v. pāsbān (SNS_pages.txt leaf 74): 'pāsbān: ... pʾsbʾn ... (AiWb. 1614) spasānō, √spas' — the glossary does refer the Pahlavi word to Bartholomae col. 1614 spasān-/√spas, exactly as Nourai's arrow does. (The leaf's printed numeral is in Persian digits and OCRs badly, so I could not confirm that this is printed p. 117; the entry is where Nourai says it is in content.) Note that this is a specialised text-glossary, not a general etymological authority, and that Horn and Nyberg contradict it.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II p. 159 (NYB_vol2_glossary.txt leaf 167)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'pās [pʾs] watch, guard 65⁹. — OP *pāça-, SW form of pāθra-, v. pahr. — MPrs pʾsbʾn \\\"watchman, guardian\\\".' Nyberg files pās under the *pā- 'protect' root and keeps it entirely separate from his spas entry on p. 186.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 274, p. 62 (HRN.txt leaf 83)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'274. pās \\\"Schutz\\\", pāsbān, pāsīden. aw. pāθra- \\\"Schutz\\\"; phlv. pās (Bund.), pāspān, vd. 13 (77); ai. pātra-.' No mention of spas-, which Horn treats 400 entries later (no. 698) as a different word.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 65 (PHD.txt leaf 86, running head 'pardāxtan 65 pāsbānīh')\",\n              \"stance\": \"partial\",\n              \"note\": \"'pās [pʾs | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [pʾspʾn | M pʾsbʾn, N ~] guardian, watcher.' MacKenzie gives no etymology but lists pās/pāsbān under p- with no cross-reference to spās (p. 76), and his English-Pahlavi index keeps 'guard ... pās' and 'gratitude ... spās' apart.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi, p. 151 (ARY_latin_index_pages.txt, entry after pdf page 150)\",\n              \"stance\": \"partial\",\n              \"note\": \"The entry lists together 'PATHRA, SPASYEITI (AVESTAN) | *PASA (OLD PERSIAN) | PAS, PASBAN (PAHLAVI) | PAS-, PASVAN (KURDISH) | SPASATI, PASYATI, SPAS-, PAS- (SANSKRIT) | SPASEM (ARMENIAN) | SKOPEIN, SKEPTOMAI (GREEK) | SPECIO, SPECERE (LATIN) | SPEHON (OHG) | ESPY, SPY (ENGLISH)' with 'POKORNY: 984' and 'MACKENZIE: (PAS, PASBAN) 65' — i.e. Aryanpur too runs pās/pāsbān into the *spek- root, but hedges by citing pāθra- alongside.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"pâsbân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The step drawn here — Pahlavi pāsbān → New Persian پاسبان pāsbān — is beyond doubt: the word passes from Middle to New Persian unchanged (MacKenzie p. 65 marks the New Persian continuation with '| N ~', i.e. identical), and it is pās 'watch, guard' + -bān, the ordinary Persian agent/keeper suffix (bāġbān, darbān, sāyebān). Its classical sense is 'watchman, night-watchman', which is the sense in the Hāfez line the chart quotes (بیار باده که در بارگاه استغنا / چه پاسبان و چه سلطان چه هوشیار و چه مست); the gloss 'policeman' is the modern administrative sense the word acquired in the late Qajar period, when پاسبان became the official title of the ordinary constable of the نظمیه, and it survives in پاسگاه, پاسدار, پاسداری. What is disputed is not this arrow but its grandparent: see node #4 — Horn, Nyberg and Wiktionary take pās back to *pāθra- 'protection' (PIE *peh₂-), not to Avestan spas-.\",\n          \"derivation_fa\": \"گامی که در این گره کشیده شده — پهلوی pāsbān ← فارسی نو «پاسبان» — تردیدناپذیر است: واژه بی هیچ دگرگونی از فارسی میانه به فارسی نو رسیده (مکنزی در ص ۶۵ دنبالهٔ نوفارسی را با نشانهٔ «| N ~» یعنی «همان» می‌آورد) و ساخت آن «پاس» + پسوند «-بان» است، همان پسوندی که در «باغبان»، «دربان» و «سایبان» دیده می‌شود. معنای کلاسیک آن «نگهبان، شب‌نگهبان» است و بیت حافظ که در نمودار آمده («بیار باده که در بارگاه استغنا / چه پاسبان و چه سلطان چه هوشیار و چه مست») نیز همین معنا را دارد؛ معنای «پلیس» که نورایی نوشته، معنایی نو و اداری است که در اواخر دورهٔ قاجار، هنگامی که «پاسبان» عنوان رسمی مأمور نظمیه شد، پدید آمد و بازماندهٔ آن در «پاسگاه» و «پاسدار» هست. آنچه مورد اختلاف است این پیکان نیست، بلکه پیکانِ پیش از آن است (گرهٔ ۴): هرن و نیبرگ و ویکی‌واژه «پاس» را به *pāθra- «پاسداری» برمی‌گردانند نه به spas- اوستایی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SNS:117\",\n              \"status\": \"partial\",\n              \"note\": \"Tavoosi's glossary (SNS_pages.txt leaf 74, s.v. pāsbān) documents the Pahlavi word and its Avestan referral ('(AiWb. 1614) spasānō, √spas') but, being a glossary of the Pahlavi text Šāyast ne Šāyast, says nothing at all about the New Persian continuation; that step has to be taken from MacKenzie and the Persian dictionaries instead.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 65\",\n              \"stance\": \"supports\",\n              \"note\": \"'pāsbān [pʾspʾn | M pʾsbʾn, N ~] guardian, watcher' — the '| N ~' means New Persian has the identical form.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 274, p. 62\",\n              \"stance\": \"supports\",\n              \"note\": \"Horn's headword group is the New Persian one: 'pās \\\"Schutz\\\", pāsbān, pāsīden', with 'phlv. pās (Bund.), pāspān' as the Middle Persian antecedent — so the MP → NP step itself is Horn's too.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur p. 151\",\n              \"stance\": \"supports\",\n              \"note\": \"lists 'PAS, PASBAN (PAHLAVI)' as the direct antecedents of the Persian headword, with the Kurdish cognates 'PAS-, PASVAN'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"specere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin speciō, specere 'to look at' is the regular Italic reflex of the PIE *-ye/o- present *spéḱ-ye-ti: Proto-Italic *spekjō, with *-kj- > Latin -ci-, giving the same formation as Avestan spasiieiti and Greek sképtomai. In historical Latin the simplex is already archaic (Plautus, Ennius, and the grammarians) and the verb lives on almost entirely in prefixed compounds — aspicere, cōnspicere, dēspicere, īnspicere, perspicere, prōspicere, respicere, suspicere — plus the frequentative spectāre and the nominal family speciēs, specimen, spectrum, speculum, speculārī, and the -spex of auspex, haruspex. The chart's gloss is right and the form is the standard citation form.\",\n          \"derivation_fa\": \"فعل لاتینی speciō / specere «نگریستن» بازتابِ قاعده‌مندِ ستاک حالِ *spéḱ-ye-ti هندواروپایی در شاخهٔ ایتالیک است: ایتالیکِ آغازین *spekjō که در آن خوشهٔ *-kj- در لاتین به -ci- بدل شده؛ یعنی درست همان ساختی که در spasiieiti اوستایی و sképtomai یونانی می‌بینیم. در لاتینِ تاریخی، صورت ساده کهنه و کم‌کاربرد است (پلاوتوس، انیوس و دستورنویسان) و فعل تقریباً همیشه با پیشوند به کار می‌رود: aspicere، cōnspicere، dēspicere، īnspicere، perspicere، prōspicere، respicere، suspicere؛ و در کنار آن‌ها فعل تکراری spectāre و خانوادهٔ اسمیِ speciēs، specimen، spectrum، speculum و جزءِ -spex در auspex و haruspex. معنا و صورتی که نورایی آورده هر دو درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/specio\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. spek-: '2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTACLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUSPICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 984 (POK_03.txt line 3040)\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. speciō, -ere, -xi, -ctum ,sehen' (con-spiciō usw.), spectō, -āre ,anschauen', speciēs ,Anblick, Ansehen, Aussehen, Erscheinung', au-, haru-spex; specus, -ūs ,Höhle'; speculum ,Spiegel'; speculor, -ārī ,spähen'; umbr. speture ,spectōrī'.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 660\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. speciō, -ere, -xī, -ctum ,sehen' (con-spiciō usw.), spectō, -āre ,anschauen', speciēs ...; umbr. speture ,spectōrī'.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 15.52, paragraph 3 (p. ~1096)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. specere, spicere, mostly in cpds., of which for simple \\\"look\\\" esp. aspicere, whence aspectus ... as also speciēs.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"respect; suspect; expect; inspect; specimen; spectrum; special; species\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All eight are Latin words on Latin's own root specere, taken into English between the 14th and 17th centuries, some through Old French, most straight out of learned Latin. respect < L. respectus (respicere 'look back at'), through OF respect, in English from c.1300 in the sense 'relation, regard'; suspect < L. suspectus (suspicere 'look up at, mistrust'), ME suspect 14th c.; expect < L. exspectāre 'look out for' (1550s, with the sense 'await'); inspect < L. īnspectāre / īnspicere 'look into' (1620s); specimen < L. specimen 'mark, token, example' (1610s, 'pattern, model'; the scientific sense 1690s); spectrum < L. spectrum 'appearance, apparition' (1610s; Newton's optical sense 1670s); special < OF especial < L. speciālis 'of a particular kind', from speciēs; species < L. speciēs 'appearance, kind', in English as a logical term 1550s and as the biological rank from Ray and Linnaeus. Watkins lists this exact set (minus SPECIAL, under which he prints ESPECIAL) under spek-.\",\n          \"derivation_fa\": \"هر هشت واژه، واژه‌هایی لاتینی‌اند که بر پایهٔ همان ریشهٔ specere ساخته شده‌اند و میان سدهٔ چهاردهم تا هفدهم میلادی، گاه از راه فرانسهٔ کهن و بیشتر یکراست از لاتینِ دانشورانه، وارد انگلیسی شده‌اند. respect از respectus لاتین (از respicere «به پشت سر نگریستن») از راه فرانسهٔ کهن؛ suspect از suspectus (از suspicere «از پایین نگریستن، بدگمان شدن») در سدهٔ چهاردهم؛ expect از exspectāre «چشم به راه بودن» (حدود ۱۵۵۰م)؛ inspect از īnspicere «در چیزی نگریستن» (حدود ۱۶۲۰م)؛ specimen از specimen «نشانه، نمونه» (۱۶۱۰م، معنای علمی‌اش ۱۶۹۰م)؛ spectrum از spectrum «نمود، شبح» (۱۶۱۰م؛ معنای نوریِ آن از نیوتن، ۱۶۷۰م)؛ special از speciālis از راه especial فرانسهٔ کهن؛ و species از speciēs «نمود، گونه» که نخست اصطلاح منطق بود (۱۵۵۰م) و سپس با ری و لینه رتبهٔ زیست‌شناختیِ «گونه» شد. واتکینز نیز همین فهرست را ذیل ریشهٔ spek- آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/specio\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives this node no citation of his own. Checked instead against Watkins/AHD s.v. spek-, which lists RESPECT, SUSPECT, EXPECT, INSPECT, SPECIMEN, SPECTRUM, ESPECIAL and SPECIES among the English descendants of Latin specere/speciēs — see the consulted array.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. spek-, and the English index\",\n              \"stance\": \"supports\",\n              \"note\": \"The index lines confirm each item individually: 'RESPECT spek-', 'EXPECT spek-', 'INSPECT spek-', 'CIRCUMSPECT spek-', 'PERSPECTIVE spek-', 'ESPECIAL spek-', and the root entry lists SPECIMEN, SPECTRUM, SPECIES, SUSPECT.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966, s.v. conspecies / species (KLN_1966.txt line 8857)\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's species family is built on L. speciēs from specere; his cross-references ('See species and cp. words there referred to', quoted s.v. spy) tie the whole English set to the same Latin verb.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict., s.v. SPECIES (SKT.txt line 17959)\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat has SPECIES as a headword in the Latin (L.) class, i.e. a direct learned borrowing, consistent with the chart's Latin → English arrow.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"skopos; epi-skopos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek is the branch in which *speḱ- underwent the well-known metathesis of the root-initial cluster: *spek- > *skep-, whence σκέπτομαι sképtomai 'I look about, examine' (for expected *σπέκτομαι), and the o-grade *spoḱ-ós > σκοπός skopós 'watcher, lookout, scout; mark, target, aim', with the denominative σκοπέω/σκοπεῖν 'to look at, consider' and σκοπιά 'watch-tower'. ἐπίσκοπος epískopos is ἐπί 'over, upon' + σκοπός, literally 'overseer' — in classical usage a title for inspectors and magistrates (Athenian officials sent to allied cities), then in the Septuagint and the New Testament the officer of a Christian congregation, whence the modern 'bishop'. Both glosses in the chart are accurate, and the cross-reference to the Epi root is correct.\",\n          \"derivation_fa\": \"یونانی همان شاخه‌ای است که در آن خوشهٔ آغازینِ ریشهٔ *speḱ- دچار قلب (metathesis) شده است: *spek- به *skep- بدل شده و از آن σκέπτομαι «می‌نگرم، وارسی می‌کنم» (به جای صورت مورد انتظار *σπέκτομαι) پدید آمده، و از درجهٔ o‌ی ریشه یعنی *spoḱ-ós صورت σκοπός «دیده‌بان، پاسور، پیشرو؛ و نیز نشانه و هدف» ساخته شده که فعل σκοπεῖν «نگریستن، سنجیدن» و σκοπιά «دیده‌بانگاه» از آن گرفته شده‌اند. ἐπίσκοπος نیز ترکیب ἐπί «بر، فراز» و σκοπός است، تحت‌اللفظ «فرانگرنده، ناظر»؛ در یونانیِ کلاسیک عنوان بازرسان و کارگزاران دولتی (از جمله مأموران آتن در شهرهای هم‌پیمان) بود و سپس در ترجمهٔ سبعینی و عهد جدید به معنی سرپرست جماعت مسیحی به کار رفت و «اسقف» امروزی از همان است. هر دو معنایی که نورایی داده درست است و ارجاع او به ریشهٔ Epi نیز به‌جاست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%BF%CF%80%CF%8C%CF%82\",\n            \"https://en.wiktionary.org/wiki/%E1%BC%90%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. spek-: 'II. Extended o-grade form *spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE.' Watkins also has '6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 984\",\n              \"stance\": \"supports\",\n              \"note\": \"'gr. sképtomai ,schaue' (skep- umgestellt aus *spek-); skopós ,Späher, Ziel', skopeîn ,beobachten, zielen, untersuchen', skopḗ, skopiá ,Warte', sképsis ,Betrachtung'.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 660\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gr. sképtomai ,schaue' (skep- umgestellt aus spek-, s. zuletzt Hirt IF. 21, 172 ...), skopós ,Späher; Ziel', skopeîn ,beobachten, zielen, untersuchen', skopḗ, skopiá ,Warte'.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. bishop, p. ~182 (KLN_1966.txt leaf 103)\",\n              \"stance\": \"supports\",\n              \"note\": \"'bishop, n. — ME. biscop, bischop, fr. OE. bisceop, biscop, fr. L. episcopus, \\\"overseer, superintendant\\\", in Eccles. L., \\\"bishop\\\", fr. Gk. epískopos, \\\"overseer\\\", fr. epí, \\\"on, over\\\", and skopós, \\\"watcher\\\". See epi- and -scope and cp. episcopal.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Old Persian\",\n          \"words\": \"skuba\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word itself is real, but the language label makes this node impossible as drawn, and the printed page (checked at 300 dpi) shows that the label is the book's own, not a misreading: Nourai really does print 'Old Persian ... skuba: bishop, priest'. Old Persian is the language of the Achaemenid inscriptions, extinct as a written idiom by the late 4th century BCE — three centuries before there were any Christian ἐπίσκοποι to name. سکوبا is a Persian word of the Islamic period, known from the Shāhnāme (the very verse the chart quotes at node #10) and from the lexicographers; it is a borrowing of Greek ἐπίσκοπος, almost certainly through Syriac ܐܦܣܩܘܦܐ ʾep(p)isqōpā, the form in which the Church of the East carried the title into Iran, with loss of the unstressed first syllable(s) and Greek π rendered by Persian ب. Wiktionary's descendants list for ἐπίσκοπος accordingly files 'Persian: سُکوبَا (sukōbā)' as a direct borrowing from Greek, with no Old Persian stage. So node #9 and node #10 are the same New Persian word listed twice, once under a chronologically impossible label. (The gloss 'bishop, priest' is fine: Dehkhoda glosses سکوبا 'اسقف، مطران' and also records its use for a monk.)\",\n          \"derivation_fa\": \"خودِ واژه راست است، اما برچسب زبانیِ این گره آن را ناممکن می‌کند، و بررسی تصویر صفحهٔ چاپی (با تفکیک ۳۰۰ نقطه بر اینچ) نشان می‌دهد که این برچسب از خودِ کتاب است نه خطای خوانشِ اسکن: نورایی به‌راستی نوشته است «فارسی باستان ... skuba: اسقف، کشیش». فارسی باستان زبان سنگ‌نبشته‌های هخامنشی است و در پایان سدهٔ چهارم پیش از میلاد از نوشتار افتاد، یعنی سه سده پیش از آنکه اسقفی مسیحی در کار باشد. «سکوبا» واژه‌ای فارسیِ دورهٔ اسلامی است که از شاهنامه (همان بیتی که در گرهٔ ۱۰ آمده) و از فرهنگ‌ها می‌شناسیم و وام‌واژه‌ای است از ἐπίσκοπος یونانی، به احتمال بسیار زیاد با میانجیِ سریانیِ ʾep(p)isqōpā که کلیسای شرق این عنوان را با همان صورت به ایران آورد؛ هجای آغازینِ بی‌تکیه افتاده و پِ یونانی در فارسی به «ب» بدل شده است. ویکی‌واژه نیز در فهرست بازماندگان ἐπίσκοπος صورت «سُکوبا»ی فارسی را یکراست ذیل یونانی آورده و هیچ مرحلهٔ «فارسی باستان» نمی‌شناسد. پس گرهٔ ۹ و گرهٔ ۱۰ یک واژهٔ واحدِ فارسی نو‌اند که دو بار آمده، یک بار با برچسبی که از نظر تاریخی ناممکن است. خطا از کتاب است، نه از استخراج.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%90%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82\",\n            \"https://abadis.ir/fatofa/%D8%B3%DA%A9%D9%88%D8%A8%D8%A7/\"\n          ],\n          \"error_in\": \"book\",\n          \"book_prints\": \"Old Persian | skuba : bishop, priest\",\n          \"correct_form\": \"(New) Persian سکوبا sekubā, a Syriac-mediated borrowing of Greek epískopos — there is no Old Persian stage\",\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1901\",\n              \"status\": \"partial\",\n              \"note\": \"Mo'in's entry for سکوبا (read via abadis.ir, which reproduces the Farhang-e Mo'in text) is simply '(سُ) (اِ.) اسقف' — 'bishop'. Mo'in gives the word and the meaning but attaches no origin tag at all here, and certainly no Old Persian claim; the Dehkhoda column on the same page adds 'رئیس اسقفیه' and a note that it may stand for سکوپا.\"\n            },\n            {\n              \"ref\": \"FSF:228\",\n              \"status\": \"partial\",\n              \"note\": \"Noushin, Vāženāmak (FSF_pages.txt leaf 306, printed page numeral OCRs as ۳۰۳, not 228 — this scan is evidently a different printing from Nourai's): 'سکوبا (با پیش اول): پیشوای مذهبی در آیین مسیحی (معرب آن «اسقف»، لاتینی episcopo؛ به واژهٔ اسقف نگاه کنید)', followed by the same Ferdowsi couplet. Noushin therefore supports a Greek/Latin episcopus origin — but as a New Persian word of the Shāhnāme, not as Old Persian.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon pp. 164-215 (KNT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"No headword skuba- or anything like it; the Old Persian lexicon contains no Christian vocabulary of any kind, as expected for a corpus that closes in the 4th c. BCE.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Noushin, Vāženāmak, leaf 306 s.v. سکوبا\",\n              \"stance\": \"partial\",\n              \"note\": \"'معرب آن «اسقف»، لاتینی episcopo' — Noushin treats سکوبا as the Persian form beside the Arabicised اسقف, i.e. as a New Persian word, and it is from him that Nourai's 'skuba → Arabic osqof' link evidently comes.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in via abadis.ir, s.v. سکوبا\",\n              \"stance\": \"partial\",\n              \"note\": \"'(سُ) (اِ.) اسقف'; the Dehkhoda section on the same page identifies it as 'اسقف، مطران' and as the name of a monk, with no Old Persian attribution.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"sekubâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian سکوبا sekubā 'a Christian bishop' is genuine and is exactly where Nourai says it is: Ferdowsi, in the Christian episodes of the Shāhnāme, نوشتند نامه به هر کشوری / سکوبا و بطریق و هر مهتری, where it stands beside بطریق (< Gk. πατρίκιος / patriarch) in a list of Byzantine dignitaries. The source is Greek ἐπίσκοπος, and the shape of the Persian word shows that it did not come straight from Greek but through Aramaic/Syriac: Classical Syriac ܐܦܣܩܘܦܐ ʾep(p)isqōpā (also ʾesqōpā) lost its unstressed opening syllable in Iranian mouths, the Greek/Syriac π/p appears as Persian ب, and the Syriac emphatic-state ending -ā is kept as the final ا of سکوبا — the same ending that betrays Syriac mediation in many Persian church words. Wiktionary lists Persian سُکوبَا among the borrowings of ἐπίσκοπος alongside Aramaic אפיסקופא, Arabic أسقف and Armenian եպիսկոպոս. The arrow drawn to this node is therefore right in substance; only the intervening 'Old Persian' box (node #9) is a phantom.\",\n          \"derivation_fa\": \"«سکوبا» در فارسی نو به معنی «اسقف مسیحی» واژه‌ای راستین است و درست همان‌جاست که نورایی می‌گوید: فردوسی در بخش‌های مسیحیِ شاهنامه می‌سراید «نوشتند نامه به هر کشوری / سکوبا و بطریق و هر مهتری»، و در همین بیت در کنار «بطریق» (از πατρίκιος یونانی) در فهرست بزرگان رومی نشسته است. خاستگاه واژه ἐπίσκοπος یونانی است، اما ریختِ فارسیِ آن نشان می‌دهد که یکراست از یونانی نیامده بلکه از راه آرامی/سریانی رسیده است: صورت سریانیِ ʾep(p)isqōpā (و نیز ʾesqōpā) در دهان ایرانیان هجای آغازینِ بی‌تکیه را از دست داده، پِ یونانی-سریانی به «ب» بدل شده، و پایانهٔ «حالت مطلق» سریانی یعنی ā همچون الفِ پایانیِ «سکوبا» بر جای مانده است — همان پایانه‌ای که در بسیاری از واژه‌های کلیساییِ فارسی نشانهٔ میانجیگری سریانی است. ویکی‌واژه نیز «سُکوبا»ی فارسی را در کنار אפיסקופא آرامی، «أسقف» عربی و եպիսկոպոս ارمنی در شمار وام‌گرفتگان ἐπίσκοπος آورده است. بنابراین محتوای این پیکان درست است و تنها جعبهٔ میانیِ «فارسی باستان» (گرهٔ ۹) ساختگی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%90%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82\",\n            \"https://abadis.ir/fatofa/%D8%B3%DA%A9%D9%88%D8%A8%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1901\",\n              \"status\": \"supports\",\n              \"note\": \"Farhang-e Mo'in s.v. سکوبا: '(سُ) (اِ.) اسقف' — the word and the gloss 'bishop' are Mo'in's, matching the chart's 'a Christian bishop'. (Read through abadis.ir, which carries the Mo'in text; the print volume's page 1901 could not be paged directly, so the page number itself is unverified.)\"\n            },\n            {\n              \"ref\": \"FSF:228\",\n              \"status\": \"supports\",\n              \"note\": \"Noushin, Vāženāmak (FSF_pages.txt leaf 306): 'سکوبا (با پیش اول): پیشوای مذهبی در آیین مسیحی (معرب آن «اسقف»، لاتینی episcopo؛ به واژهٔ اسقف نگاه کنید)' followed by the identical Ferdowsi couplet 'نوشتند نامه به هر کشوری / سکوبا و بطریق و هر مهتری'. Content matches exactly; the scan's printed page is ۳۰۳, so Nourai's 228 belongs to a different printing.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in and Dehkhoda via abadis.ir, s.v. سکوبا\",\n              \"stance\": \"supports\",\n              \"note\": \"Dehkhoda: 'رئیس اسقفیه'; also 'نام راهبی است که حضرت عیسی مسیح بدیر او رفته...', and the remark that the word may stand for سکوپا — i.e. an ecclesiastical title of foreign origin.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Noushin, Vāženāmak leaf 306\",\n              \"stance\": \"supports\",\n              \"note\": \"Explicitly refers the word to Greek/Latin episcopus and cross-refers to اسقف.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. bishop, p. ~182\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein documents the Greek → Latin/ecclesiastical spread of epískopos that underlies every borrowed form of the title, Persian included.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Arabic\",\n          \"words\": \"osqof\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic أُسْقُف usquf 'bishop' (pl. أساقفة asāqifa, أساقف asāqif) is certainly a form of Greek ἐπίσκοπος, but not a direct one and not one that came through Persian. The route recognised by Arabists is Greek ἐπίσκοπος > Classical Syriac ܐܦܣܩܘܦܐ ʾeppisqōpā (with variants ʾesqōpā) > Arabic usquf, the loss of the initial syllable and the u-u vocalism being characteristic of the Syriac-mediated Christian vocabulary of pre-Islamic Arabia (the bishops of al-Ḥīra and Najrān). Wiktionary: 'From Classical Syriac ܐܦܣܩܘܦܐ (ʾeppisqoppā) or a variant thereof ... a borrowing of Ancient Greek ἐπίσκοπος'. Two corrections to the chart as extracted: (a) on the printed page this box hangs off the GREEK box, not off 'Old Persian skuba' — a single line drops from the bottom-left corner of the Greek box and elbows into Old Persian, Arabic and Latin in turn, so the JSON's parent=9 is an extraction error; (b) even the printed Greek → Arabic arrow passes over the Syriac stage that actually shaped the Arabic word. Hence 'plausible': right ultimate source, compatible but incomplete route.\",\n          \"derivation_fa\": \"«أُسْقُف» عربی (جمع: أساقفة و أساقف) بی‌گمان صورتی از ἐπίσκοπος یونانی است، اما نه یکراست از یونانی و نه از راه فارسی. راهی که عربی‌دانان می‌پذیرند این است: ἐπίσκοπος یونانی ← سریانیِ کلاسیک ʾeppisqōpā (و گونهٔ ʾesqōpā) ← «أسقف» عربی؛ افتادن هجای آغازین و واکه‌آراییِ u-u از ویژگی‌های همان گنجینهٔ واژگان مسیحیِ سریانی‌تبار است که پیش از اسلام از راه حیره و نجران به عربی رسیده بود. ویکی‌واژه می‌نویسد: «از سریانی کلاسیک ʾeppisqoppā یا گونه‌ای از آن ... که خود وام‌گرفته از ἐπίσκοπος یونانی است». دو نکتهٔ اصلاحی دربارهٔ نمودار: نخست آنکه در صفحهٔ چاپی این جعبه از جعبهٔ «یونانی» منشعب می‌شود نه از «فارسی باستان skuba» (خطی از گوشهٔ پایینِ چپِ جعبهٔ یونانی فرود می‌آید و به ترتیب به «فارسی باستان»، «عربی» و «لاتینی» می‌رسد)، پس ثبتِ parent=9 در داده‌های استخراج‌شده خطای خوانش است؛ دوم آنکه حتی پیکانِ چاپیِ «یونانی ← عربی» نیز از مرحلهٔ سریانی که شکل واژهٔ عربی را ساخته چشم می‌پوشد. از این رو حکم «با احتیاط پذیرفتنی» است: خاستگاه نهایی درست، ولی مسیر ناتمام.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A3%D8%B3%D9%82%D9%81\",\n            \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:270\",\n              \"status\": \"supports\",\n              \"note\": \"Farhang-e Mo'in s.v. اسقف (via abadis.ir) tags the word '[معر.]' (mu'arrab, arabicised) and glosses it 'از یونانی گرفته شده به معنای پیشوای عیسوی که مرتبه‌اش از کشیش بالاتر است' — 'taken from Greek, a Christian leader ranking above a priest'. Mo'in thus gives Greek as the source and Arabic as the mediating shape, which is what this node claims; he does not route it through Persian skuba.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. bishop, p. ~182\",\n              \"stance\": \"supports\",\n              \"note\": \"'fr. L. episcopus, \\\"overseer, superintendant\\\", in Eccles. L., \\\"bishop\\\", fr. Gk. epískopos' — the Greek etymon and the ecclesiastical sense-development that every borrowed form, Arabic included, presupposes.\"\n            },\n            {\n              \"src\": \"FVQ\",\n              \"where\": \"Jeffery, Foreign Vocabulary of the Qur'ān (FVQ_pages.txt, searched for usquf/asquf)\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry: أسقف is not a Qur'ānic word, so Jeffery does not treat it, though he repeatedly mentions the Christian bishops of al-Ḥīra and Najrān (p. ~174 'Assemani ... mentions Monophysite Bishops of al-Hira'; 'Quss, Bishop of Najran'), the milieu in which the Syriac title entered Arabic.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM_pages.txt, searched أسقف/الأسقف)\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry — Addi Shir's dictionary covers Persian words arabicised, and he does not claim أسقف among them, which is itself evidence against the chart's Persian → Arabic route.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs (LKT.txt, searched usquf/Bischof/Episkopos)\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry; Lokotsch catalogues Oriental words that entered European languages, and 'bishop' travelled the other way, so his silence is expected.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"osqof\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The derivation is sound: Persian اسقف osqof 'bishop' is an Arabic loan (Arabic أسقف usquf), and since the Arabic word is itself Greek by way of Syriac, the Persian form is the Arabic-mediated doublet of the older, directly borrowed سکوبا of node #10 — a classic round trip in which the Greek title reaches Persian twice, once through Syriac (سکوبا) and once through Arabic (اسقف). Ferdowsi already uses it: به اسقف چنین گفت کای دستگیر / ز ایران یکی نام‌جویم دبیر. Mo'in marks it '[معر.]' and traces it to Greek; Dehkhoda quotes the lexicographers' 'اسقف النصاری، أعجمی معرّب' — 'the Christian bishop, a foreign word arabicised'. The flag is on the script, not the etymology: the JSON gives «اسقّف», with a shadda over the qāf, which would be read usqqof and is not a form any dictionary knows. The printed page (rendered at 300 dpi and read directly) shows a ḍamma, not a shadda: «اسقُف». This is an extraction error, not the author's.\",\n          \"derivation_fa\": \"ریشه‌شناسی این گره درست است: «اسقف» فارسی وام‌واژه‌ای از عربیِ «أسقف» است و چون واژهٔ عربی خود از یونانی و با میانجی سریانی آمده، صورت فارسیِ آن دوگانهٔ (doublet) واژهٔ کهن‌ترِ «سکوبا» در گرهٔ ۱۰ است؛ یعنی همان عنوان یونانی دو بار به فارسی رسیده، یک بار از راه سریانی («سکوبا») و یک بار از راه عربی («اسقف»). فردوسی نیز آن را به کار برده است: «به اسقف چنین گفت کای دستگیر / ز ایران یکی نام‌جویم دبیر». معین آن را «[معر.]» نشانه زده و به یونانی بازبرده، و دهخدا از فرهنگ‌نویسان نقل می‌کند: «اسقف النصاری، أعجمی معرّب». اما نکتهٔ نشانه‌گذاری‌شده در اینجا خطِ واژه است نه ریشهٔ آن: در داده‌های استخراج‌شده «اسقّف» با تشدید روی «ق» آمده که خوانشِ usqqof می‌دهد و در هیچ فرهنگی چنین صورتی نیست. تصویر صفحهٔ چاپی (با تفکیک ۳۰۰ نقطه بر اینچ و خوانش مستقیم) نشان می‌دهد که آنچه بر «ق» نشسته ضمه است نه تشدید: «اسقُف». پس این خطای خوانشِ اسکن است، نه خطای کتاب.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/\",\n            \"https://en.wiktionary.org/wiki/%D8%A3%D8%B3%D9%82%D9%81\"\n          ],\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"اسقُف\",\n          \"correct_form\": \"اسقُف\",\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:270\",\n              \"status\": \"supports\",\n              \"note\": \"Farhang-e Mo'in s.v. اسقف (abadis.ir): tagged '[معر.]', glossed 'از یونانی گرفته شده به معنای پیشوای عیسوی که مرتبه‌اش از کشیش بالاتر است'. The Dehkhoda column adds 'یونانی اپیسکوپوس' and 'اسقف النصاری، أعجمی معرّب'.\"\n            },\n            {\n              \"ref\": \"FSF:44\",\n              \"status\": \"supports\",\n              \"note\": \"Noushin, Vāženāmak (FSF_pages.txt leaf 54, printed numeral ۵۱ in this scan — again a different printing from Nourai's 44): 'اسقف (با پیش اول و سوم و سکون دوم) ... (تازی) ... پارسی: سکوبا', immediately followed by the same Ferdowsi couplet 'به اسقف چنین گفت کای دستگیر / ز ایران یکی نام‌جویم دبیر' that the chart quotes. Noushin marks the word تازی (Arabic) and gives سکوبا as its Persian counterpart — exactly the pair of nodes #10 and #12.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in + Dehkhoda via abadis.ir, s.v. اسقف\",\n              \"stance\": \"supports\",\n              \"note\": \"'گویند این لغت عربی است' beside 'اسقف النصاری، أعجمی معرّب' — the Persian lexicographical tradition itself registers it as an Arabic-shaped foreign word.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Noushin, Vāženāmak leaf 54\",\n              \"stance\": \"supports\",\n              \"note\": \"'(تازی) ... پارسی: سکوبا' — Arabic, with سکوبا named as the native-route equivalent.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir (AFM_pages.txt, searched أسقف)\",\n              \"stance\": \"silent\",\n              \"note\": \"Not listed among the Persian words arabicised — consistent with a Greek/Syriac, not Persian, source for the Arabic word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Latin\",\n          \"words\": \"micro-scopium; tele-scopium; peri-scopium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"These three are not Latin but New Latin (Neo-Latin) coinages of the scientific revolution, built by European scholars out of Greek material: telescopium is Kepler's Latinisation (1613) of Italian telescopio, the name coined in 1611 in the Accademia dei Lincei — Prince Federico Cesi's circle, to which Galileo belonged — from Greek τηλεσκόπος 'far-seeing' (τῆλε 'far' + -σκοπος 'watcher'); microscopium was made on the same model by Giovanni Faber of the Lincei in 1625 for Galileo's compound lens instrument (Gk. μικρός 'small'); periscopium is a 19th-century formation (Gk. περί 'around'), the English periscope dating from 1899. Because the second element is Greek -σκόπιον / σκοπεῖν, the arrow the printed page actually draws — from the GREEK box, not from the root — is the right one. Two things to correct: the label should read 'New Latin', since Classical Latin had none of these words; and the JSON records this node's parent as #0 (the root), whereas on the page the line into it descends from the Greek box together with the lines into Old Persian and Arabic — an extraction error.\",\n          \"derivation_fa\": \"این سه واژه لاتینی به معنای کلاسیک نیستند، بلکه ساخته‌های «لاتینِ نو» در دورهٔ انقلاب علمی‌اند که دانشمندان اروپایی از مصالح یونانی برساخته‌اند: telescopium لاتینی‌کردهٔ کپلر (۱۶۱۳م) از telescopio ایتالیایی است، نامی که در ۱۶۱۱م در آکادمیای لینچئی — حلقهٔ شاهزاده فدریکو چزی که گالیله نیز عضو آن بود — از τηλεσκόπος یونانی «دوربین، دورنگر» (τῆλε «دور» + -σκοπος «نگرنده») ساخته شد؛ microscopium را جووانی فابرِ همان آکادمی در ۱۶۲۵م بر همین قیاس برای دستگاه عدسیِ مرکبِ گالیله ساخت (μικρός «خرد»)؛ و periscopium ساختهٔ سدهٔ نوزدهم است (περί «پیرامون») که صورت انگلیسیِ periscope آن به ۱۸۹۹م بازمی‌گردد. چون جزء دومِ هر سه، -σκόπιον / σκοπεῖν یونانی است، پیکانی که صفحهٔ چاپی در واقع می‌کشد — یعنی از جعبهٔ «یونانی» و نه از ریشه — درست است. دو اصلاح لازم است: برچسب باید «لاتین نو» باشد، زیرا لاتین کلاسیک هیچ‌یک از این واژه‌ها را نداشت؛ و در داده‌های استخراج‌شده پدرِ این گره ۰ (ریشه) ثبت شده، حال آنکه در صفحه خطِ ورودی آن همراه با خطوطِ «فارسی باستان» و «عربی» از جعبهٔ یونانی فرود می‌آید — خطای خوانشِ اسکن.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/telescope\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 s.v. spek- ends its Greek section 'SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE', and the index has 'HOROSCOPE spek-, yēr-'. So AHD confirms that telescope and the -scope words belong to this root and are Greek-based, but it posits no Latin telescopium/microscopium stage; that stage is real but is Neo-Latin, and is not what Nourai's 'AHD' reference documents.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966, the -scope compounds (e.g. baroscope, bioscope, chronoscope, KLN_1966.txt lines 4476, 5049, 7606)\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's formula for the whole family is 'Compounded of ... and Gk. -skópion, fr. skopeîn, \\\"to look at, examine\\\". See -scope.' — the second element is Greek, as this node assumes, and the compounds are modern coinages.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline s.v. telescope (archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"'1640s, from Italian telescopio (Galileo, 1611) and Modern Latin telescopium (Kepler, 1613), both from Greek teleskopos \\\"far-seeing\\\" ... said to have been coined by Prince Cesi, founder and head of the Roman Academy of the Lincei.' Note 'Modern Latin', i.e. New Latin, not Latin.\"\n            }\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box standing for the French instrument names that carried the Neo-Latin coinages into the modern European languages and thence into Persian: télescope (1611, in Peiresc's circle, from telescopium), microscope (1656), périscope (19th c.). French analysed them as télé- / micro- / péri- + the productive suffix -scope, which is how Wiktionary still parses télescope ('From télé- + -scope'), and it is in this French shape — with the stress-final, -scope ending — that the words reached Persian, Turkish and Russian in the 19th century. The box carries no words and no reference, so nothing in it can be wrong; the step it represents is well documented.\",\n          \"derivation_fa\": \"این جعبهٔ خالی، حلقهٔ واسطِ فرانسوی را نشان می‌دهد که نام‌های لاتینِ نو را به زبان‌های نوین اروپایی و از آنجا به فارسی رسانده است: télescope (۱۶۱۱م، در حلقهٔ پِیرِسک، از telescopium)، microscope (۱۶۵۶م) و périscope (سدهٔ نوزدهم). فرانسوی این واژه‌ها را به صورت télé- / micro- / péri- به‌علاوهٔ پسوند زایای -scope تحلیل می‌کرد، چنان‌که ویکی‌واژه هنوز هم télescope را «télé- + -scope» می‌شکافد؛ و واژه‌ها با همین ریختِ فرانسوی، یعنی با پایانهٔ -scope، در سدهٔ نوزدهم به فارسی و ترکی و روسی راه یافتند. چون این جعبه نه واژه‌ای دارد و نه ارجاعی، چیزی در آن نمی‌تواند نادرست باشد و گامی که نشان می‌دهد مستند است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/t%C3%A9lescope\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Empty pass-through node with no citation of Nourai's own; checked against Wiktionary's French entry and etymonline instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline s.v. telescope (archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"Traces telescope to Italian telescopio and Modern Latin telescopium; the French télescope is the same Neo-Latin word in French dress and is the form Persian took over.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in s.v. تلسکوپ via abadis.ir\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in's origin tag is '[فر.]' — French — which is precisely the intermediary this empty box represents: '(تِ لِ) [فر.] (اِ.) دوربین بزرگ که با آن ستارگان را رصد می‌کنند.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Persian\",\n          \"words\": \"تلسکوپ; میکروسکوپ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"تلسکوپ teleskop and میکروسکوپ mikroskop are modern European loans in Persian, taken over with the instruments themselves during the Qajar period (Dār al-Funūn, from 1851, taught astronomy and medicine from French textbooks and its staff were largely French-trained). Mo'in tags تلسکوپ '[فر.]', i.e. French, and defines it 'دوربین بزرگ که با آن ستارگان را رصد می‌کنند'; the Dehkhoda article likewise says the word entered Persian from French and distinguishes the refracting (منکسرکننده) from the reflecting (منعکس‌کننده) type. میکروسکوپ is the same story, beside the calque ریزبین and the Academy's coinage درشت‌نما. The Persian spelling with پ for the final -pe and the stress pattern point to French rather than English transmission, as does the whole Qajar scientific vocabulary (لوکوموتیو, تلگراف, ژنرال); Wiktionary's claim that تلسکوپ is 'Borrowed from English telescope' is the minority view and does not fit the chronology. Nourai's French route is right.\",\n          \"derivation_fa\": \"«تلسکوپ» و «میکروسکوپ» وام‌واژه‌های نوِ اروپایی در فارسی‌اند که همراه با خودِ ابزارها در دورهٔ قاجار وارد شدند؛ دارالفنون (از ۱۲۳۰ خورشیدی) نجوم و پزشکی را از روی کتاب‌های فرانسوی می‌آموخت و آموزگارانش بیشتر فرانسه‌دان بودند. معین «تلسکوپ» را با نشانهٔ «[فر.]» یعنی فرانسوی آورده و چنین تعریف کرده است: «(تِ لِ) [فر.] (اِ.) دوربین بزرگ که با آن ستارگان را رصد می‌کنند»؛ دهخدا نیز می‌نویسد واژه از فرانسه به فارسی آمده و میان گونهٔ «منکسرکننده» و «منعکس‌کننده» فرق می‌گذارد. سرگذشت «میکروسکوپ» نیز همین است، در کنار گرته‌برداریِ «ریزبین» و برساختهٔ فرهنگستان «درشت‌نما». نوشتنِ پایانهٔ واژه با «پ» و الگوی تکیهٔ آن، مانند دیگر واژگان علمیِ دورهٔ قاجار («لوکوموتیو»، «تلگراف»، «ژنرال»)، بر میانجیگری فرانسوی گواهی می‌دهد نه انگلیسی؛ آنچه ویکی‌واژه دربارهٔ وام‌گیری «تلسکوپ» از انگلیسی می‌گوید دیدگاهی اقلیتی است و با گاه‌شماری سازگار نیست. مسیر فرانسویِ نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%AA%D9%84%D8%B3%DA%A9%D9%88%D9%BE/\",\n            \"https://en.wiktionary.org/wiki/%D8%AA%D9%84%D8%B3%DA%A9%D9%88%D9%BE\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON\",\n              \"status\": \"supports\",\n              \"note\": \"Farhang-e Mo'in s.v. تلسکوپ (abadis.ir): '(تِ لِ) [فر.] (اِ.) دوربین بزرگ که با آن ستارگان را رصد می‌کنند.' The bracketed [فر.] is Mo'in's origin tag for French — exactly the French → Persian arrow of this node. Nourai gives no volume/page, so only the entry itself could be checked.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in and Dehkhoda via abadis.ir, s.v. تلسکوپ\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in '[فر.]'; Dehkhoda's long article likewise derives it from French and describes both telescope types.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Wiktionary, Persian تلسکوپ (archived)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Borrowed from English telescope' — a different intermediary from Mo'in's French. Given the Qajar transmission history and Mo'in's explicit tag, the French route is the better supported one; either way the Greek/Neo-Latin origin is untouched.\"\n            }\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"scope; microscope; telescope; periscope\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"telescope (1640s) and microscope (1650s) come into English from the Neo-Latin/Italian names of the instruments — telescopium/telescopio, microscopium — and periscope is a 19th-century formation (1899 in the optical sense). All three therefore continue Greek -σκόπιον, from σκοπεῖν 'to look at', and the arrow from the Neo-Latin box is right. scope is the odd one out and deserves a note: English scope 'aim, purpose, extent' (1530s) is not from the instrument family at all but from Italian scopo 'aim, purpose', from Latin scopus, from Greek σκοπός 'mark to shoot at, target' — a different sense of the same Greek noun, and hence a doublet route rather than a derivative of -scopium. Since Greek σκοπός itself is the node's ultimate parent either way, the chart is not wrong, only compressed. Watkins lists 'SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE' together under spek- in the same way.\",\n          \"derivation_fa\": \"واژه‌های telescope (حدود ۱۶۴۰م) و microscope (حدود ۱۶۵۰م) از نام‌های لاتینِ نو و ایتالیاییِ همین ابزارها (telescopium/telescopio و microscopium) به انگلیسی رسیده‌اند و periscope ساختهٔ سدهٔ نوزدهم است (معنای نوریِ آن از ۱۸۹۹م). پس هر سه دنبالهٔ -σκόπιον یونانی از σκοπεῖν «نگریستن»اند و پیکانی که از جعبهٔ لاتینِ نو کشیده شده درست است. اما scope از این میان بیرون است و نیاز به توضیح دارد: scope انگلیسی به معنی «هدف، دامنه، گستره» (حدود ۱۵۳۰م) اصلاً از خانوادهٔ نام ابزارها نیست، بلکه از scopo ایتالیایی «هدف، غرض» و آن از scopus لاتین و σκοπός یونانی به معنی «نشانه، آماج» آمده است؛ یعنی معنایی دیگر از همان اسم یونانی و در نتیجه دوگانه‌ای (doublet) است نه مشتقی از -scopium. چون σκοπός یونانی در هر دو حال پدرِ نهاییِ این گره است، نمودار نادرست نیست و تنها فشرده است. واتکینز نیز «SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE» را به همین شیوه ذیل ریشهٔ spek- کنار هم آورده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/telescope\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. spek-, Greek section: 'skopos, one who watches ... and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE.' All four of this node's words (periscope under -SCOPE) are covered.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline s.v. telescope (archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"'1640s, from Italian telescopio (Galileo, 1611) and Modern Latin telescopium (Kepler, 1613), both from Greek teleskopos \\\"far-seeing\\\", from tele- \\\"far\\\" + -skopos \\\"watcher\\\" (from PIE root *spek- \\\"to observe\\\").'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict., s.v. SCOPE (SKT.txt line 16645)\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat carries SCOPE as a headword in the Italian/Latin/Greek class, i.e. through Italian scopo from Gk. skopós — the doublet route noted in the derivation.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966, the -scope entries\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gk. -skópion, fr. skopeîn, \\\"to look at, examine\\\". See -scope.' repeated across baroscope, bioscope, chromatoscope, chronoscope, ebullioscope, endoscope.\"\n            }\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Germanic\",\n          \"words\": \"spehôn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The form Nourai prints is the Old High German verb spehōn 'to spy, watch closely' (MHG spehen, modern German spähen), which is conventionally used — as Watkins uses it — to stand for the Proto-West-Germanic *spehōn. Its kin are OHG speha f. 'attentive observation, reconnoitring', OHG/OS spāhi 'wise, skilful', ON spá 'prophecy' and spá 'to prophesy', MDu spien, MLG spēen 'to spy'. All continue PIE *speḱ-: Germanic *sp- is the regular outcome of PIE *sp- (Grimm's law does not affect a stop after s), and the *-ḱ- gives Germanic -h- by Grimm's law, so *speḱ-ōn > *spehōn exactly as expected. Only the label deserves a footnote: 'Germanic' here means the OHG citation form, not a reconstruction, and Nourai's circumflex ô renders the long ō of the weak-verb suffix.\",\n          \"derivation_fa\": \"صورتی که نورایی آورده، فعل آلمانیِ علیای کهن spehōn «پاییدن، به دقت نگریستن» است (در آلمانی میانه spehen و در آلمانی امروز spähen) که — چنان‌که واتکینز نیز می‌کند — معمولاً به نمایندگی از ژرمنیِ غربیِ آغازین *spehōn به کار می‌رود. خویشاوندان آن عبارت‌اند از speha «نگریستنِ دقیق، شناسایی» در همان زبان، spāhi «دانا، چیره‌دست» در آلمانی و ساکسونی کهن، و spá «پیشگویی» و فعل spá «پیشگویی کردن» در نورس کهن، و spien هلندی میانه. همهٔ این‌ها بازماندهٔ *speḱ- هندواروپایی‌اند: خوشهٔ آغازینِ *sp- در ژرمنی دست‌نخورده می‌ماند (قانون گریم بر انسدادیِ پس از s کارگر نیست) و *-ḱ- بر پایهٔ همان قانون به -h- بدل می‌شود؛ پس *speḱ-ōn به *spehōn می‌رسد، درست چنان‌که انتظار می‌رود. تنها نکته آن است که برچسب «ژرمنی» در اینجا صورتِ گواهی‌شدهٔ آلمانی علیای کهن است نه بازسازی، و «ô» در نوشتار نورایی همان ōی کشیدهٔ پسوندِ فعل ضعیف است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/spe%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. spek-: 'I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-on-, watcher, in Old Italian spione, spy: ESPIONAGE.' Watkins uses the identical citation form *spehon.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 984\",\n              \"stance\": \"supports\",\n              \"note\": \"'ahd. spehōn ,spähen', dazu speha f. ,aufmerksames Betrachten, Untersuchung, Auskundschaftung, Aufpassen'; aisl. spá ,Wahrsagung' ...; as. ahd. spāhi ,klug, geschickt'.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 660\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ahd. spehōn ,spähen' von speha f. ,prüfendes, aufmerksames Betrachten, Untersuchung, Auskundschaftung, Aufpassen'; aisl. spá ,Wahrsagung' (*spahō : gr. skopḗ), spá ,wahrsagen' ...; as. ahd. spāhi ,klug, geschickt'.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. spy, p. ~1566\",\n              \"stance\": \"supports\",\n              \"note\": \"'... Frankish *spehon, which is rel. to OHG. spehon, MHG. spehen, \\\"to examine closely\\\", G. spähen, \\\"to spy\\\", MLG. speen, MDu. spien, \\\"to spy\\\", ON. spá ... OHG. speho, \\\"spy\\\" ... fr. I.-E. base *spek-, \\\"to look at, examine, spy\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"spy; espionage\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words do go back to the Germanic verb, but not down the straight Germanic line the arrow suggests: English received them back from Romance. spy is ME spien, espien, from Old French espier 'to watch' (modern épier), itself from Frankish *spehōn — i.e. a West Germanic verb borrowed into Gallo-Romance and then re-borrowed into English in the 13th century; the noun spy is ME spie from OF espie. espionage is later still and doubly Romance: French espionnage, from espion 'spy', which French took from Italian spione, an augmentative of spia, itself a Germanic loan in Italian. Buck states the route in one line — 'NE spy through OFr. espier' — and Watkins likewise files SPY and ESPY under 'Germanic *spehon in: a. Old French espier'. So the ultimate etymon in the chart's Germanic box is right, and both English words are genuinely from *speḱ-; what the single arrow hides is that the transmission is Frankish → Old French → English (and Germanic → Italian → French → English for espionage).\",\n          \"derivation_fa\": \"هر دو واژه به‌راستی به همان فعل ژرمنی بازمی‌گردند، اما نه از راه مستقیم ژرمنی که پیکان نشان می‌دهد؛ انگلیسی آن‌ها را از زبان‌های رومانس پس گرفته است. spy از انگلیسی میانهٔ spien / espien است و آن از espier فرانسهٔ کهن (امروز épier) «پاییدن»، و این خود از *spehōn فرانکی؛ یعنی فعلی ژرمنیِ غربی که نخست به رومانسِ گل وام رفته و سپس در سدهٔ سیزدهم به انگلیسی بازگشته است؛ اسمِ spy نیز از spie انگلیسی میانه و آن از espie فرانسهٔ کهن است. espionage دیرتر و دو بار رومانسی است: از espionnage فرانسوی، از espion «جاسوس»، که فرانسوی آن را از spione ایتالیایی — صورت بزرگ‌ساختِ spia — گرفته و spia خود وام‌واژه‌ای ژرمنی در ایتالیایی است. باک این مسیر را در یک سطر آورده است: «NE spy through OFr. espier»، و واتکینز نیز SPY و ESPY را ذیل «ژرمنی *spehon ← فرانسهٔ کهن espier» نشانده است. پس ریشهٔ نهایی در جعبهٔ ژرمنیِ نمودار درست است و هر دو واژهٔ انگلیسی به‌راستی از *speḱ- می‌آیند؛ آنچه این پیکانِ یگانه پنهان می‌کند، مسیر فرانکی ← فرانسهٔ کهن ← انگلیسی است (و برای espionage: ژرمنی ← ایتالیایی ← فرانسوی ← انگلیسی).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/spe%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai cites nothing for this node; checked against Klein, Watkins and Buck instead (see consulted), all three of which insert Old French between Germanic and English.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. spy (v. and n.), p. ~1566 (KLN_1966.txt line 36462)\",\n              \"stance\": \"partial\",\n              \"note\": \"'spy, tr. and intr. v. — ME. spien, espien, fr. OF. espier (F. épier), fr. Frankish *spehon ...'; 'spy, n. — ME. spie, fr. OF. espie (whence F. épie), fr. espier'; and 'espionage, n. — F. espionnage, \\\"spying\\\", fr. espion, \\\"spy\\\", fr. It. spione. See espy and -age.' The Germanic etymon is confirmed, the route is Romance.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. spek-\",\n              \"stance\": \"partial\",\n              \"note\": \"'1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-on-, watcher, in Old Italian spione, spy: ESPIONAGE.' Watkins too routes both English words through Romance.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 15.52, paragraph 3 (p. ~1096)\",\n              \"stance\": \"partial\",\n              \"note\": \"'OHG spehon \\\"look at carefully\\\", NHG spähen, etc. (NE spy through OFr. espier)' — the parenthesis is exactly the qualification this node needs.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-466.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 466",
 "description": "Write verification JSON and run check"
}
```


### [2026-09-14T02:55:52.705Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 12, 'disputed': 2, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 5, 'not_checked': 3}
books consulted: {'supports': 38, 'contradicts': 2, 'partial': 8, 'silent': 5} | by book: {'KLN': 8, 'MON': 5, 'WLD': 4, 'PHD': 4, 'WEB': 4, 'CHEUNG': 3, 'HRN': 3, 'POK': 3, 'FSF': 3, 'NYB': 2, 'ARY': 2, 'SYN': 2, 'AHD': 2, 'SKT': 2, 'AFM': 2, 'BRT': 1, 'KNT': 1, 'FVQ': 1, 'LKT': 1}
```


## [2026-09-14T02:56:11.779Z] AGENT

0 PROBLEM lines. Page 466 (book p. 436) verified — one entry, root **Spek**, 18 nodes.

**Verdicts:** root confirmed · nodes: 12 confirmed, 3 plausible, 2 disputed, 1 transcription_suspect.
**Ref checks:** 13 supports, 5 partial, 3 not_checked. **Books consulted:** 19 distinct (POK, WLD, AHD/Watkins, IEC, SYN, BRT, CHEUNG, PHD, NYB, HRN, HUB-route via Horn, BQT, MON, FSF, ARY, KLN, SKT, FVQ, AFM, LKT), 2 contradicting.

**Disputed / flagged**

- **#4 Pahlavi `pâsbân`** — Nourai (following his source SNS/Tavoosi, who cites AiWb 1614 √spas) derives pās/pāsbān from Avestan *spas-*. Nyberg II 159 ("pās — OP \*pāça-, SW form of pāθra-"), Horn no. 274 ("aw. pāθra- 'Schutz'") and Wiktionary all derive it instead from PIE \*peh₂- 'protect'. Aryanpur p. 151 hedges, listing both. Modern view: unrelated to \*speḱ-.
- **#9 "Old Persian" `skuba`** — chronologically impossible label (printed that way in the book, `error_in: book`). سکوبا is a New Persian word of the Shāhnāme, borrowed from Greek ἐπίσκοπος via Syriac ʾep(p)isqōpā; Wiktionary lists it as a direct Greek borrowing with no Old Persian stage. Nodes #9 and #10 are the same word twice.
- **#12 Persian `osqof`** — `transcription_suspect`, `error_in: extraction` (see below). Etymology itself fine.
- Plausible: #11 (Arabic *usquf* omits the Syriac stage), #13 (these are New Latin, not Latin), #18 (spy/espionage reach English via Old French/Italian, not straight from Germanic).

**Extraction errors for the owner to fix** (JSON differs from the printed page; verified on a 300 dpi render, copied to `data/verification/sources/refs/ocr/BOOK/466.png`):

1. **Node #11 parent is wrong** — JSON has `parent: 9`; the page draws the Arabic box off the **Greek** box (#8). A single line drops from the Greek box's bottom-left corner and elbows into Old Persian, Arabic and Latin in turn.
2. **Node #13 parent is wrong** — JSON has `parent: 0`; the page draws the Latin `micro-scopium` box off the same **Greek** line (#8), not off the root.
3. **Node #12 script** — JSON has `"اسقّف"` (shadda over qāf, reading *usqqof*); the page prints `اسقُف` (ḍamma).

Also noted, not errors: Nourai's FSF page numbers (228, 44) don't match our scan's printing (entries are at leaves 306 and 54, printed ۳۰۳ and ۵۱) — evidently a different printing of Noushin's Vāženāmak; BQT:1086 lands on vol. 2 leaf 548 (≈ printed 1088–1091), within this scan's offset drift.
