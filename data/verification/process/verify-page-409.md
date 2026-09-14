# Verification process log — verify-page-409


## [2026-09-14T01:07:03.157Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 409 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-409.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-409.json. Write /home/sfmqrb/git/rishe/data/verification/page-409.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 409` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:07:04.362Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:07:05.206Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:07:05.227Z] TOOL RESULT

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


## [2026-09-14T01:07:05.702Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-409.txt"
}
```


### [2026-09-14T01:07:05.718Z] TOOL RESULT

```
1	=== PDF page 409 (book page 379) ===
2	--- entry 0 ---
3	ROOT [Sanskrit] Pulâka : ball of rice  (refs KLN:1185)
4	#1 (parent #0) [Persian] refs=KLN:1185; HJB:710; MON:810 | polow «پلو ( پلاو ، پلا )» : cooked rice
5	  #2 (parent #1) [Turkish] refs=KLN:1185; DEV:186 | pilâw : cooked rice
6	    #3 (parent #2) [English] refs=LKT:132 | pilau, pilaf, pilaff
7	    #4 (parent #2) [French] refs=DEV:186 | pilau
8	--- entry 1 ---
9	ROOT [Sogdian] Pwt : Buddha, also used to mean an idol. According to SLW:94, this word has a Chinese / Indian root.  (refs SOD:332; SLW:94)
10	#1 (parent #0) [Pahlavi] refs=BQT | bôt : idol
11	  #2 (parent #1) [Persian] refs=MON:472; BQT:234; SLW:94 | bot «بُت ( بت پرست )» : idol ; bot-kadeh «بتکده ( بتخانه )» : idol house, prayer house | NOTE: See "Bheu 3" for another possible root.
12	    #3 (parent #2) [Hindustani] refs=None | 
13	      #4 (parent #3) [Portuguese] refs=None | 
14	        #5 (parent #4) [English] refs=SKT:366; LKT:30; AID:233 | pagoda : prayer house | NOTE: See HJB:652 for a discussion on this word.
15	
```


## [2026-09-14T01:07:07.064Z] AGENT

I'll read the source JSON and reference materials.


## [2026-09-14T01:07:08.364Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-409.json",
 "description": "Read source JSON for page 409"
}
```


### [2026-09-14T01:07:08.428Z] TOOL RESULT

```
{
  "pdf_page": 409,
  "book_page": 379,
  "entries": [
    {
      "root": {
        "name": "Pulâka",
        "lang": "Sanskrit",
        "refs": "KLN:1185",
        "gloss": "ball of rice"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "KLN:1185; HJB:710; MON:810",
          "words": [
            {"translit": "polow", "gloss": "cooked rice", "script": "پلو ( پلاو ، پلا )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Turkish",
          "refs": "KLN:1185; DEV:186",
          "words": [
            {"translit": "pilâw", "gloss": "cooked rice", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "LKT:132",
          "words": [
            {"translit": "pilau, pilaf, pilaff", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "French",
          "refs": "DEV:186",
          "words": [
            {"translit": "pilau", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pwt",
        "lang": "Sogdian",
        "refs": "SOD:332; SLW:94",
        "gloss": "Buddha, also used to mean an idol. According to SLW:94, this word has a Chinese / Indian root."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT",
          "words": [
            {"translit": "bôt", "gloss": "idol", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:472; BQT:234; SLW:94",
          "words": [
            {"translit": "bot", "gloss": "idol", "script": "بُت ( بت پرست )"},
            {"translit": "bot-kadeh", "gloss": "idol house, prayer house", "script": "بتکده ( بتخانه )"}
          ],
          "note": "See \"Bheu 3\" for another possible root.",
          "quote": {
            "text": "این همه جنگ و جدل حاصل کوته نظری است - گر نظر پاک کنی کعبه و بتخانه یکیست",
            "poet": "Emâd Khorâsânî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Hindustani",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Portuguese",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "SKT:366; LKT:30; AID:233",
          "words": [
            {"translit": "pagoda", "gloss": "prayer house", "script": null}
          ],
          "note": "See HJB:652 for a discussion on this word.",
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:07:10.718Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','HJB','MON','DEV','LKT','SOD','SLW','BQT','SKT','AID','PHD','NYB','HRN','HUB','ARY','FSD','WEB','TTS','PLA','AFM']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online.json keys"
}
```


### [2026-09-14T01:07:11.847Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SLW {"title": "W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) pp. 93-106", "edition_found": "reprint in W. B. Henning Selected Papers I (Acta Iranica 14, 1977) - different pagination; original in JSTOR", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers (also w.-b.-henning-selected-papers_2021
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
```


## [2026-09-14T01:07:17.154Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','HJB','DEV','LKT','SOD','SLW','SKT','AID','PHD','NYB','HRN','HUB','ARY','MON','BQT','FSD','WEB','TTS']:\n    v=d.get(k)\n    print('===',k)\n    print(json.dumps({kk:v.get(kk) for kk in ['local_file','page_offset','lookup_hint','scans','cites']},ensure_ascii=False,indent=1)[:1200])\n\"",
 "description": "Get local files and offsets"
}
```


## [2026-09-14T01:07:17.903Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80",
 "description": "List reference files"
}
```


### [2026-09-14T01:07:18.285Z] TOOL RESULT

```
=== KLN
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "scans": null,
 "cites": "page number, continuous across the two volumes (1966–67)"
}
=== HJB
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt",
 "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.",
 "scans": null,
 "cites": "page number of Hobson-Jobson (1903 ed.)"
}
=== DEV
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt",
 "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start.",
 "scans": null,
 "cites": null
}
=== LKT
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt",
 "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.",
 "scans": null,
 "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"
}
=== SOD
{
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "scans": null,
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
=== SLW
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt",
 "page_offset": "Selected Papers scan: leaf = p + 12 for the front matter; reprinted articles keep the ORIGINAL journal page numbers in the margins, so grep 'Sogdian Loan' then the original page number (93-106). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Original: JSTOR https://www.jstor.org/stable/608123 (BSOAS 10.1) - search jstor for 'Sogdian Loan-Words in New Persian'. In the local text grep -n -i 'sogdian loan' to find the article, entries are numbered Persian words with Sogdian etyma.",
 "scans": null,
 "cites": null
}
=== SKT
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
 "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.",
 "scans": null,
 "cites": "page number of Skeat, Concise Etymological Dictionary"
}
=== AID
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt",
 "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start; grep -n '^Word'.",
 "scans": null,
 "cites": null
}
=== PHD
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).",
 "scans": null,
 "cites": "page number of MacKenzie, A Concise Pahlavi Dictionary (1971)"
}
=== NYB
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
 "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.",
 "scans": null,
 "cites": "page number of Nyberg, A Manual of Pahlavi, Part II Glossary (1974)"
}
=== HRN
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "scans": null,
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
=== HUB
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "scans": null,
 "cites": "page number of Hübschmann, Persische Studien (1895)"
}
=== ARY
{
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "cites": null
}
=== MON
{
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR dow
=== BQT
{
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
 "page_offset": "v
=== FSD
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.",
 "scans": null,
 "cites": "page number of Funk & Wagnalls New Standard Dictionary (1940)"
}
=== WEB
{
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt",
 "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.",
 "scans": null,
 "cites": "page number of Webster's New Twentieth Century Dictionary, 2nd ed."
}
=== TTS
{
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"
 ],
 "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.",
 "lookup_hint": "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.",
 "scans": null,
 "cites": null
}
```


### [2026-09-14T01:07:18.328Z] TOOL RESULT

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
SIN.txt
```


## [2026-09-14T01:07:25.045Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'pilau\\|pulaka\\|pilaf' KLN_1966.txt | head -30; echo \"--- SKT\"; grep -n -i 'pilau\\|pagoda' SKT.txt | head -20; echo \"--- LKT\"; grep -n -i 'pilau\\|pilaw\\|pagod' LKT.txt | head -20; echo \"--- DEV\"; grep -n -i 'pilau\\|pilaw\\|pagod' DEV.txt | head -20; echo \"--- HJB\"; grep -n -i '^PILAU\\|^PALANQUIN\\|^PAGODA' HJB.txt | head -20; echo \"--- AID\"; grep -n -i 'pagoda\\|pilau' AID.txt | head -20",
 "description": "Grep pilau/pagoda in western refs"
}
```


### [2026-09-14T01:07:25.178Z] TOOL RESULT

```
28811:pikul,  n.  —  See  picul, pilaf,  n.  —  See  pilau.
28812:pilar,  adj.,  hairy.  —  Formed  with  adj.  suff.  -ar fr.  L.  pilus,  ‘hair’.  See  pile,  ‘hair’, pilau,  pilaf,  pilaw,  n.,  an  Oriental  dish  of  rice boiled  with  meat,  etc.  —  Turk,  pilaw,  fr.  Pers. palav.
28814:Derivatives:  pilaster-ed,  adj .,  pilaster-ing,  n. Pilate,  n.,  a  Roman  surname,  esp.  surname  of Pontius,  a  governor  of  Judaea.  —  L.  Pildtus,  lit. ‘armed  with  javelins’,  fr.  pilum,  ‘javelin’  (see pile,  ‘pointed  stake'), pilaw,  n.  —  See  pilau.
--- SKT
23625:Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
--- LKT
1017:373.  Pers.  batkädä: 'Götzentempel'  [aus  pers.  but  'Götzen- bild' Horn  NpEt  S.  42,  Nr.  182  und kädä  'Haus'  ebenda  S.  188,  Nr.  844; käd,  kädä  ist  in  Zusammensetzungen der  Ort,  wo  sich  etwas  dauernd  befindet, untergebracht  oder  aufbewahrt  wird, vgl.  BARTHOLOMAE  in  ZfdWf  VI,  354] ; hieraus  ergab  sich  durch  Kontamination mit  präkrta  bhagodi  'göttlich,  heilig' [aus  sskr.  bhaga-vatl,  d.  h.  'Gott-begabt', also  'göttlich',  vgl.  Ascoli,  Studi  orien- tali  e  linguistici  S.  268/269,  Nr.  5,  wo auch  gesagt  ist,  daß  zuerst  die  Münzen mit  dem  Bilde  der  Pärvati,  Sivas  Gattin, so  hießen]  der  pg.  Ausdruck  pagoda, eugl.  pagoda,  pagode,  dtsch.  Pagode,  it. pagodo,  rum.  pagoda,  poln.  pagoda. Hierunter  versteht  man  jetzt  einen  Tem-
1020:pel,  besonders  in  China  solche  von  ganz bestimmtem  Äußeren,  für  das  der  nun zerstörte  Porzellanturm  von  Nanking als  typisch  angesehen  werden  kann; zahlreiche  vorzügliche  Abbildungen  von Pagoden  s.  bei  Ernst  Boerschmann, Baukunst  und  Landschaft  in  China. Berlin  s.  a.  (1923),  z.  ß.  S.  7—9,  45.  — [Zahlreiche  andere  Ableitungen,  wie Verdrehung  eines  ind.  Wortes  dagoha oder  aus  pg.  pagäo  aus  lat.  paganus oder  aus  chines.  pai-ku-td  'Turm  der weißen  Knochen',  sind  weniger  wahr- scheinlich.] [Hobson-Jobson  652/657. Hirth  ChinFW  200.
3079:Ebenso  tamul.  Ungarn  'membrum  virile', das  buddhistische  Emblem  des  Mahä, Deva  (Siva),  das  sich  als  Kegel  aus schwarzem  Stein  in  den  Pagoden  dieser Gottheit  findet.  In  den  Reisebeschrei- bungen über  Indien  häufig  als  Lingam, engl,  lingam  erwähnt.
3780:1656.  Tk.  pilaw:
3781:'Mit  Fett  abgekochter  Reis';  hieraus  in derselben  Bedeutung  rum.  pilaf,  frz.  pi- laf,  pilau;  engl,  pilau,  pillau,  pilaw, pillaw;  russ.  jyilaw,  plow.
6122:pagoda  373
6143:i  pilaw  1656
7150:pagodo  373
7691:pagoda  373
8731:pacea  1601 paciaurä  1602 padi^a(c)h  1604 pafta  165 pagodä  373 paiantä  1611 paic  1608 pa/a  1615 pahnac  1636 ^?a/o^'  1615 pambria  1617 pangea  1621 pajjucßj  1625 2>ar«  1626 paradis  1631 paraleü  1626 parmac(lic)  1636 pastramä  261 ^Jasi»  1652 pälämar  1616 pärälujä  1626 pätlägea  161 pehlivan(ie)  1607 i^eZie«  1645 j>e/<»c  1646 pemheü  1617 perciun(at)  1629 perrfaf  1637 i>errfea  1630 perdeluß  1630 i^er^Äe/  1635 peruzea  609 2)ervaz  1638 pesmet  1642 pe^ches  1663 peschir  1660 pesim  1662 1662 pestimun  1674 pezevenche  1658 pezevenchm  1658 pezevencl'ic  1658 ^f'c«"«  1653 i>jf^/c  1670 ^tVaf  1656 pivgea  1620 pingelui  1620 pisicä  1661 /)?7ar  1654
--- DEV
1898:Pagode.  Du  persan  «<^XiL)  boutkedè  ou  jjoutkoudè,  temple d'idoles,  formé  de  oo  bout  ou  pont,  idole,  et  de  »*x^  kedè ou  koudè,  maison.
1931:PiLAU.  Mets  au  riz,  chez  les  Turcs.  Du  persan ^^j  pi- laou,  même  sens.  On  dit  aussi  pilaf  ,  d'après  la  pron.  turque.
4080:Pagode.
4108:PiLAU.
4606:»jJo:j  pers.  voy.  Pagode.
4681:ji^U  pers.  voy.  Babouche. ^^IxIjLj  pers.  voy.  Aubergine. sISsIjIj  pers.  voy.  iVubergine. yû;^Lj  pers.  voy.  Bézoard. sLi^Upej's.  voy.  Chah. ^^Xjpers.  voy.  Parsis. »>Lj  pers.  voy.  Para. (jkLj  pers.  voy.  Bézoard. ivolj  pers.  voy.  Alphénic. i^yj  pers.  voy.  Péri. HDD  voy.  Pâques. ^"ikj  pers.  voy.  Pilau. ^  pers.  voy.  Punch. □  "«"nS  voy.  Purim. fjj^^^,  pers.  vov.  Babouch,  Tar- bouch.
5039:nùS pers.  voy.  Pagode.
--- HJB
16191:PAGODA.
16214:PAGODA,  s.  This  obacure  and remarkable  word  is  used  in  three different  senses.
16216:PAGODA.
16218:PAGODA.
16232:PAGODA.
16234:PAGODA,
16243:PAGODA.
16245:PAGODA.
16262:PAGODA,
16264:PAGODA.
16297:PAGODA.
17494:PILAU,  PILOW,  PILAF,  &c,  &
17510:pilauB; Things  which  in  hungry  mortals'  eyes find  favour." — Don  Juan^  v.  47. 1848.— "'There's  a  pillau,  Joseph,   just •ns  you  like  it,  and  Papa  has  broiu^ht  home the  best  turbot  in  Bulingsgate."  — Vdai^y Fair,  i.  20.
--- AID
562:Archdka.  [Kanarese.]  The  officiating priest  of  a   pagoda.
1089:Bhatta.  [Sanskrit.]  A   title  used  in addressing,  01  affixed  to  the  name of,  a   learned  Brdhman.  In  Tamil it  denotes  the  officiating  priest  in  a pagoda.
2869:Hoon.  [Hindi  huny  from  the  Kana- rese  honnu^  gold.]  A   gold  coin,  the star  pagoda.
5145:Pagoda.  [According  to  Webster  from the  Persian  but,  an  idol,  and  kodak , a   house ;   but  perhaps  only  a   corrup-
5147:Pagoda.  A   gold  or  silver  coin,  for- merly coined  at  Madras,  and  worth about  three  and  a   half  or  four  rupees. It  used  to  be  thought  that  the  coin was  so  called  from  the  device  of  a temple  which  it  bore,  but  the  name seems  to*be  older  than  the  device, and  the  derivation  from  Bhagawati (said  to  be  a   name  of  Pdrwati)  is now  generally  accepted.  The  pa- goda was  divided  into  forty-five fanams.
5480:Pilau.  [Persian.]  A   dish  consisting of  boiled  fowl  with  rice  highly seasoned  with  cinnamon,  cardamoms, mace,  and  ghee.
7090:Varahd.  [Tamil.]  The  gold  coin commonly  called  by  Europeans pagoda.
```


## [2026-09-14T01:07:46.073Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==605{print NR\": \"substr($0,1,300)}' KLN_1966.txt; echo \"=== find leaf of line 28812\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"pilau,  pilaf,  pilaw\")>0) print \"leaf(1-based)=\"n}' KLN_1966.txt",
 "description": "Locate KLN pilau leaf"
}
```


## [2026-09-14T01:07:46.591Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28805,28815p' KLN_1966.txt",
 "description": "Read KLN pilau context"
}
```


### [2026-09-14T01:07:47.178Z] TOOL RESULT

```
605: ic,  paraesthetic,  adj.  —  See  prec.  word and  adj.  suff.  -ic.
paretic,  adj.,  pertaining  to,  or  affected  with  pa¬ resis,  n.,  a  person  having  paresis.  - —  See  paresis and  adj.  suff.  -ic.
Derivative :  paretic-al-ly,  adv. par  excellence,  preeminently.  —  F.  See  par
=== find leaf of line 28812
leaf(1-based)=633
```


### [2026-09-14T01:07:47.236Z] TOOL RESULT

```
pigment,  n.,  paint,  dye.  —  L.  pigmentum,  ‘col¬ oring  matter,  paint’,  from  the  stem  of  pingere,  ‘to paint’.  See  paint  and  -ment  and  cp.  pimento, pimiento  and  the  second  element  in  orpiment. Derivatives:  pigment,  tr.  and  intr.  v..  pigmentary (q.v.),  pigment-ation,  n.,  pigment-ize,  tr.  v. pigmentary,  adj.  —  L.  pigmentarius,  'pertaining to  paints’,  fr.  pigmentum.  See  prec.  word  and adj.  suff.  -ary. pigmy,  n.  —  See  pygmy.
pignorate,  tr.  v.,  to  pledge.  —  L.  pignerdrus  (pig- noratus),  pp.  of  pignerdre  ( pignorare ),  ‘to  give as  a  pledge,  to  pledge’,  fr.  pignus.  gen.  pignoris, ‘pledge,  gage,  security’,  which  is  of  uncertain origin.  For  the  ending  see  verbal  suff.  -ate. pike,  n.,  a  sharp  point.  —  ME.  pie,  pike,  pyke,  fr. OE.  pic,  ‘point,  pike’,  fr.  OF.  ( =  F.)  pic,  ‘pick, pickax;  peak  (of  a  mountain)',  which  is  prob. verbal  n.  of piquer,  ‘to  prick,  sting'  (see  Dauzat,
DELF.,  p.  556  s.v.  2nd  pic),  fr.  VL.  *piccdre,  ‘to prick,  pierce’  (whence  also  It.  piccare,  OPro- veng.,  Sp.  picar,  ‘to  prick,  sting’),  fr.  VL.  *pic- cus,  fr.  L.  picus,  ‘woodpecker’,  which  is  rel.  to pica,  'magpie’.  See  pie,  ‘magpie’,  and  cp.  peak, ‘a  sharp  point’.  Cp.  also  picador,  picaresque, picaroon,  picayune,  pickax,  picket,  picnic,  picot, picotee,  pinch,  pink,  ‘to  pierce’,  pique,  piquet, pitch,  ‘to  throw'.  Cp.  also  pick,  v. pike,  n.,  a  weapon  with  a  long  shaft.  —  F.  pique, fr.  piquer,  ‘to  prick,  pierce’.  See  pike,  ‘a  sharp point’,  and  cp.  pick,  ‘pointed  instrument’. Derivative:  pike,  tr.  v.,  to  pierce  with  or  as  with a  pike.
pike,  n.,  a  voracious  fresh-water  fish.  —  Short  for pikefish,  lit.  'the  fish  with  a  pointed  beak’,  fr. pike,  ‘a  sharp  point’.  Cp.  pickerel.  For  sense development  cp.  F.  brochet,  ‘pike’,  fr.  broche,  ‘a spit’.
pike,  n.,  top  of  a  mountain.  —  Of  Norse  origin;
rel.  to  E.  pike,  ‘a  sharp  point’, pike,  n.,  toll  bar.  —  Abbreviation  of  turnpike, pikelet,  n.,  a  crumpet  ( Local  English).  —  Short¬ ened  fr.  obsolete  bara-picklet,  fr.  W.  bara- pyglyd.
pikul,  n.  —  See  picul, pilaf,  n.  —  See  pilau.
pilar,  adj.,  hairy.  —  Formed  with  adj.  suff.  -ar fr.  L.  pilus,  ‘hair’.  See  pile,  ‘hair’, pilau,  pilaf,  pilaw,  n.,  an  Oriental  dish  of  rice boiled  with  meat,  etc.  —  Turk,  pilaw,  fr.  Pers. palav.
pilaster,  n.,  a  square  column.  —  MF.  (=  F.)  pi- lastre,  fr.  It.  pilastro,  fr.  ML.  pilastrum,  fr.  L. pita,  'pillar'.  See  pillar  and  -aster.
Derivatives:  pilaster-ed,  adj .,  pilaster-ing,  n. Pilate,  n.,  a  Roman  surname,  esp.  surname  of Pontius,  a  governor  of  Judaea.  —  L.  Pildtus,  lit. ‘armed  with  javelins’,  fr.  pilum,  ‘javelin’  (see pile,  ‘pointed  stake'), pilaw,  n.  —  See  pilau.
pilch,  n.,  1 )  orig.  an  outer  garment  made  of  skin; 2)  a  light  saddle;  3)  an  infant’s  triangular wrapper,  worn  over  the  diaper.  —  OE.  pylece, fr.  ML .  pellicea,  'furred  garment’,  prop.  fem.  of L.  peliiceus.  made  of  skins’,  fr.  pellis,  ‘skin’.  See fell,  ‘hide',  and  cp.  pelisse, pilchard,  n.,  name  of  a  fish  of  the  herring  family. —  Fr.  earlier  pilcher,  a  word  of  uncertain  origin, pile,  n.,  a  heavy  timber  or  beam  driven  into  the ground  to  serve  as  a  support.  —  ME.,  ‘dart, stake',  fr.  OE.  pit,  ‘pointed  stake,  prickle’,  fr.  L. pilum,  ‘javelin;  pestle’  1  whence  also  ON.  pita, OHG.,  MHG.  pfil  (G.  Pfeil),  ‘arrow’],  which  is rel.  to  L.  pita,  ‘mortar’.  See  pestle  and  cp.  words there  referred  to.
```


## [2026-09-14T01:07:56.013Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'pulāka\\|pulaka\\|pilau' KLN_1971.txt | head -20; echo \"=== leaf of hit in 1971\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (tolower($0) ~ /pilau/) print \"leaf=\"n}' KLN_1971.txt | head",
 "description": "Check KLN 1971 for pilau"
}
```


### [2026-09-14T01:07:57.538Z] TOOL RESULT

```
182443:pilaf, n. — See pilau. 
182447:pilau, pilaf, pilaw, n., an Oriental dish of rice 
182460:pilaw, n. — See pilau. 
=== leaf of hit in 1971
leaf=1
```


## [2026-09-14T01:07:58.665Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=630 && NR<=636 {print \"---LEAF \"NR\"---\"; print substr($0,1,200)}' KLN_1966.txt | head -40; echo \"=== search page numbers near\"; awk 'BEGIN{RS=\"\\f\"} NR>=628 && NR<=636 {print NR\": \"$0}' KLN_1966.txt | grep -o '1[12][0-9][0-9]' | head -20",
 "description": "Check KLN page numbering near pilau"
}
```


### [2026-09-14T01:07:59.802Z] TOOL RESULT

```
---LEAF 630---
he  brain,  delirium (med.)  —  Medical  L.,  formed  fr.  Gk.  9p7)v,  gen. 9psvo 9,  ‘diaphragm,  heart,  mind’  (see  phrenet¬ ic),  with  suff.  -itis.
Derivative:  phrenit-ic,  adj. phreno
---LEAF 631---
  ‘strength,  power,  rule’.  See physio-  and  -cracy.
1180
1181
physiocrat,  n.  —  F.  physiocrate,  back  formation from  prec.  word ;  see  -crat.
Derivative:  physiocrat-ic,  adj. physiog
---LEAF 632---
  prec.  word  and
-oon.
Derivative:  picaroon,  intr.  v. picayune,  n.,  name  of  a  small  coin.  —  F.  picaillon, fr.  OProven?.  picaioun,  ‘a  small  copper  coin’, derived  fr.  picaio,
---LEAF 633---
tra,  ‘rock, stone’,  fr.  Gk.  7r£xpoc.  See  petro-.
Derivatives:  pier,  tr.  v.,  pier-age,  n. pierce,  tr.  and  intr.  v.  — ■  ME.  percen,  fr.  OF. percer,  percier  (F.  percer),  
---LEAF 634---
pyrewink.es,  of  unknown  origin, pillory,  n.  —  ME.,  fr.  OF.  (=  F.)  pilori,  fr.  ML. pildrium,  of  s.m.,  a  derivative  of  L.  pila,  ‘pillar’. See  pillar  and  subst.  suff.  -ory
---LEAF 635---
 leaf  (bot.)-,  2)  fin  ( zool .);  3) the  external  ear  ( anat .)  —  L.  pinna,  ‘feather, wing;  fin  of  a  fish;  battlement,  pinnacle’,  which, according  to  F.  S.  Sommer  (in  Kri
---LEAF 636---
’,  and  F.  girouette, ‘weathercock’.
pirouette,  intr.  v.,  to  whirl  about  on  tiptoe.  —  F. pirouetter,  fr.  pirouette.  See  pirouette,  n. Derivatives:  pirouett-er,  ti.,  pirouett
=== search page numbers near
1176
1177
1178
1179
1180
1181
1101
1182
1183
1190
```


## [2026-09-14T01:08:07.223Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==633{print}' KLN_1966.txt | grep -o '^.\\{0,80\\}' | head -3; echo \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==633{print}' KLN_1966.txt | grep -nE '^11[0-9][0-9]$' ; echo \"=== full leaf 633 numbers\"; awk 'BEGIN{RS=\"\\f\"} NR==633{print}' KLN_1966.txt | grep -oE '\\b11[0-9][0-9]\\b' | head",
 "description": "Verify KLN leaf 633 page numbers"
}
```


## [2026-09-14T01:08:08.049Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17494,17515p' HJB.txt",
 "description": "Read Hobson-Jobson PILAU entry"
}
```


### [2026-09-14T01:08:08.349Z] TOOL RESULT

```
tra,  ‘rock, stone’,  fr.  Gk.  7r£xpoc.  See  petro-.
Derivatives:  pier,  tr.  v.,  pier-age,  n. pierce,  tr.  and  intr.  v.  — ■  
Derivatives:  pierc-ing,  adj pierc-ing-ly,  adv. Pierian,  adj.,  pertaining  t
...
=== full leaf 633 numbers
```


### [2026-09-14T01:08:08.396Z] TOOL RESULT

```
PILAU,  PILOW,  PILAF,  &c,  &
Pers.  puldo,  or  pildv,  Skt.  p\ddka,  'a ball  of  boiled  rice.'  A  dish,  in  origin purely  Mahommedan,  consisting  of meat,  or  fowl,  boiled  along  wth  rice and  spices.  Recipes  are  given  by Herklots,_  ed.  1863,  App.  xxix. ;  and in  the  Ain-i-Akbarl  (ed.  BUKhmann^ \.  60),  we  have  one  for  hima  puldo (i(r2ma==*hash')  with  several  others  to which  the  name  is  not  given.  The name  is  almost  as  familiar  in  England as  curry,  but  not  the  thifig.  It  was an  odd  circumstance,  some  45  years ago,  that  the  two  surgeons  of  a dragoon  regiment  in  India  were  called Currie  and  Pilleau.
1616. — "Sometimes  they  boil  pieces  of flesh  or  hens,  or  other  fowl,  cut  in  pieces  in their  rice,  which  dish  they  call  pillkw.  As they  order  it  they  make  it  a  very  excell^it and  a  very  well  tasted  food." — Terry,  in Purchas,  ii.  1471.
c.  1630. —  "The  feast  begins:  it  was compounded  of  a  hundred  sorts  of  pelo  and canciied  dried  meats." — Sir  T.  Herbert,  ed. 1638,  p.  138,  [and  for  varieties,  p.  310],
PINANG,
711
PINDARBY.
fuhy
[e.  1660. — ".  .  .  my  elegant  hosts  were lUy  employed  in  cramming  their  mouths with  as  much  Pelau  as  they  oould  oontain. .  .  ."—Bernier,  ed.  ConstahU,  121.]
1673. — "The  most  admired  Dainty  where- with they  stuff  themselves  is  Fallow, whereof  they  will  fill  themselves  to  the 'Throat  and  receive  no  hurt,  it  being  so well  prepared  for  the  Stomach." — Iryer, 899.  See  also  p.  93.  At  p.  404  he  gives a  recipe.
1682.— "They  eate  their  pilaw  and  other spoone-meate  withoute  spoones,  taking  up their  pottage  in  the  hollow  of  their  fingers. — Evelyn,  IHaryy  June  19.
1687.— "They  took  up  their  Moss  with their  Fingers,  as  the  Moors  do  their  Pilaw, using  no  Spoons." — Dampier,  i.  430.
1689.— "Palau,  that  is  Rice  boH'd  ...  . with  Spices  intermixt,  and  a  boil'd  Fowl  in the  middle,  is  the  most  common  Indian. Dish."— (M'n^tow,  397.
1711.— "They  cannot  go  to  the  Price  of a  1*11106,  or  boil'd  Fowl  and  Rice ;  but  the better  sort  make  that  their  principal  Dish." —Lochyer,  231.
1793.— "On  a  certain  day  ...  all  the Musulman  officers  belonging  to  your  depart- ment shall  be  entertained  at  the  charge  of the  Sirccur,  with  a  public  repast,  to  consist of  Pnllao  of  the  first  aort,— Select  Letters ofTippoo  S,t  App.  xlii.
c.  1820.— **  And  nearer  as  they  came,  a  genial  savour Of  certain  stews,  and  roast-meats,  and
pilauB; Things  which  in  hungry  mortals'  eyes find  favour." — Don  Juan^  v.  47. 1848.— "'There's  a  pillau,  Joseph,   just •ns  you  like  it,  and  Papa  has  broiu^ht  home the  best  turbot  in  Bulingsgate."  — Vdai^y Fair,  i.  20.
PINANG,  s.  This  is  the  Malay word  for  Areca,  and  it  is  almost always  used  by  the  Dutch  to  indicate that  article,  and  after  them  by  some Continental  writers  of  other  nations. The  Chinese  word  for  the  same  pro- duct— mn-Uing — is  probably,  as  Bret- schneiaer  says,  a  corruption  of  the Malay  word.     (See  PENANG.)
[1603.— "They  (the  Javans)  are  very  great eaters — and  they  haue  a  certaine  hearbe called  bfttaile  (see  BETEL)  which  they vsually  have  carryed  with  them  wherosouer they  goe,  in  boxes,  or  wrapfied  vp  in  a cloath  like  a  sugar  loafe:  and  also  a  nut called  Pinange,  which  are  both  in  operation very  hott,  and  they  eate  them  continually to  warme  them  within,  and  keepe  them from  the  fluxe.  They  do  likewise  take much  tahacco,  and  also  opium."— A'.  Scott, All  Exact  I>i»com'8e,  &c.,  of  the  Ecut  Indies, lt)06,  Sig.  N.  2.
[1665.— "Their  ordinary  food  ...  is  Rice, "Wlieat,  •  Pinang6.  .  .  "—Sir  T.  Herbert, TraceU,  1677,  p.  365  (Stanf.  JJid.).]
1726.— "But  Shah  Sousa  gave  him  (viz. Van  der  Broek,  an  envoy  to  Rajmahal  in 1655)  good  words,  and  regaled  him  with Pinang  (a  great  favour),  and  promised  that he  shoula  he  amply  paid  for  everything." — VcUentijii,  v.  165.
PINBABBY,  s.  Hind.  pinddHy pinddrd,  but  of  which  the  more original  form  appears  to  he  Mahr. pendhdri,  a  member  of  a  l)and  of plunderers  called  in  that  language pendhdr  and  pendhdrd.  The  ety- mology of  the  word  is  very  obscure. We  may  discard  as  a  curious  coinci- dence only,  the  circumstance  observed by  Mr.  H.  T.  Prinsep,  in  the  work quoted  below  (i.  37,  note),  that  "  Pin- dara  seems  to  have  the  same  reference to  Pandour  that  Kuzdk  has  to  Cossack." Sir  John  Malcolm  observes  that  the most  popular  etymology  among  the natives  ascribes  the  name  to  the  dis- solute habits  of  the  cla^  leading them  to  frequent  the  shops  dealing in  an  intoxicating  drink  called  pinda, (One  of  the  senses  of  pendhd^  accord- ing to  Moleswor til's  Mahr.  Diet,  is  *  a drink  for  cattle  and  men,  prepared from  Holcxis  sorghum*  (see  JOWAUB) *  by  steeping  it  and  causing  it  to  fer- ment.') Sir  John  adds  :  *  Kurreem Khan'  (a  famous  Pindarry  leader) *told  me  he  had  never  heard  of  any other  reason  for  the  name  ;  and  Major Henley  had  the  etymology  confirmed by  the  most  intelligent  of  the  Pin- darries  of  whom  he  enquired '  {Central India,  2iid  ed.  i.  433).  Wilson  again considers  the  most  probable  derivation to  be  from  the  Mahr.  pendhd,  but  in the  sense  of  a  *  bundle  of  rice-straw,* and  hara^  *who  takes,'  because  the name  was  originally  applied  to  horse- men -^ho  hung  on  to  an  army,  and were  employea  in  collecting  forage. We  cannot  think  either  of  the  etymo- logies very  satisfactory.  We  venture another,  as  a  plausible  suggestion merely.  Both  pind-parnd  in  Hindi, and  pindd^-hasTieh  in  Mahr.  signify '  to  follow ' ;  the  latter  being  defined '  to  stick  closely  to ;  to  follow  to  the death ;  used  of  the  adherence  of  a disagreeable  fellow.'  Such  phra.ses would  aptly  apply  to  these  hangers-on of  an  army  in  the  field,  looking  out for  prey.  [The  qiiestion  has  been discussed  by  Mr.  W.  Irvine  in  an elalx)rate  note  published  in  the  Indian Antiq.  of  1900.  To  the  above  three suggestions  he  iidds  two  made  by  other
```


## [2026-09-14T01:08:20.653Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if '1656.  Tk.  pilaw' in l or \"373.  Pers.  batkädä\" in l:\n        print('leaf(0-based)=',i,'-> printed page =',i-26)\n        print(l[:60].replace('\\n',' | '))\nEOF",
 "description": "Find LKT leaf/page for entries 373 and 1656"
}
```


### [2026-09-14T01:08:21.960Z] TOOL RESULT

```
leaf(0-based)= 57 -> printed page = 31
 h.  Stoff  für  Schleier]; hieraus  rum.  burungiuc  'Gaze'
leaf(0-based)= 160 -> printed page = 134
wieback',  il. pasiimata  'pasta  con  zoflerano  e  cantucc
```


## [2026-09-14T01:08:23.324Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'pagoda' in l.lower():\n        print('leaf=',i,'printed=',i-20, repr(l[:80]))\nEOF\necho \"=== AID pagoda leaf\"\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AID.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'Pagoda.' in l:\n        print('leaf=',i,'printed=',i-18)\nEOF",
 "description": "Find SKT and AID pagoda pages"
}
```


### [2026-09-14T01:08:24.641Z] TOOL RESULT

```
leaf= 639 printed= 619 ' Curiously  enough,  there  Is  only  om Iglilh  word  which  can  be  traced  t'
=== AID pagoda leaf
leaf= 251 printed= 233
```


## [2026-09-14T01:08:30.526Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'pagod' SKT.txt | head; echo \"=== PAGODA entry\"; grep -n -iE '^ *pagoda' SKT.txt | head",
 "description": "Grep SKT for pagoda entry"
}
```


### [2026-09-14T01:08:30.591Z] TOOL RESULT

```
23625:Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
=== PAGODA entry
```


## [2026-09-14T01:08:32.508Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (384,385,386,387):\n    print('--- leaf',i,'printed~',i-20)\n    print(leaves[i][:400].replace('\\n',' '))\nEOF",
 "description": "Inspect SKT leaves near p.366"
}
```


### [2026-09-14T01:08:33.634Z] TOOL RESULT

```
657
--- leaf 384 printed~ 364
 Ptump^  verb,  to  fall  heavily  down  ;  so  also G.  plumpeu^  Swed.  piumpa,  &c.,  to  fall plump,  are  all  due  to  L.  plumbum,  lead, plunge.   (F.  -  L.)     F.  plouf^er,   'tc E lunge,  dive;'  Cot.  Formctl  from  a  Low ,.  piumbicart  •,  not  found,  but  verified  by Picard /iifrt^w/r,  to  plunge:  *ee  Diet,  «.  v. piombaf^.  A  frequentative  form  from  L. plumbum^  lead  
--- leaf 385 printed~ 365
 (.F.-L).    O.F. employ.  — L.  imflUatf,  to  impll employ^ :  see  tmplicatc  below. explicate,  to  explain.  tL* of  L.  explicare,  to  unfold,  ex] out :  pluan,  to  fold. explicit.  (L.)  L.  t^piuin of  ex piuart,  to  unfold,  make exploit.   tF.-L.)     M.E. cess.  Gower,  C.  A.  ii.  JgS.^Oj revenue,  profit;  later,  m  *" txpiieitum,  a  thing played  ;  neut.  of  *-xj Low  L.  tx
--- leaf 386 printed~ 366
cf.  mod.  E.  to  Afljf.  to  pxktt.^V.  poeAr,  a bag  ;  see  pouoh,  sv.  Poko  (i). Pock  (I),  a  pustule.  (E. ;  ptrhaps  C.) Smali  pes  «  small  /«'*'.  where  pwki  ii pi.  of  poek,  M.  E.  pokke,  a  pock,  pi. Pekkes.  A.  S.  pec,  a  pustule.  +  Du.  pock, Gpcckit  a  (KKk.  ^.  Prob.  of  Celtic  origin, and  allied  to  poki  (i),  a  hag:  cf.  Gael. pMcaid,  a  pimple.  Iris
--- leaf 387 printed~ 367
wards  extended  to /fiuttrr-er;  fcuUr'jf  (foe f>CMit'fr-y\ X 3<53 POOP. pullet  (F.-L.)  M.  E. f^fete,  later  pouUtte^  fcra. a  chicken  (above). of   F.  poultt» Poop. ship. Poor; Pop. Levini- (F.  -  L,)      F.  foH^.  poH/fe,  -  L. ace.  of  fu/'f'is,  hinder  part  of  a I I p |i I ire  Pauper. (E.)       "To   poppi.    cooicctare;* Of  imitative   origin ;    allied    to M.  E  poup
```


## [2026-09-14T01:08:46.833Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE 'agod|Pag[o0]' SKT.txt | head -20; echo \"===\"; python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'PAGAN' in l.upper() or 'Pagan' in l:\n        print('leaf',i,'printed~',i-20, l[:150].replace('\\n',' '))\nEOF",
 "description": "Search SKT for pagan/pagoda entries"
}
```


### [2026-09-14T01:08:48.022Z] TOOL RESULT

```
10218:Leviathan.  (L.  -  Hcb.)  Late  L. viaihan.  Job  xl.  JO  (Vulgate).  -  \UhJivy4- thiin,  an  aquatic  animal,  dragOD,  kerpctitt named  from  its  twisting  itself  in  curves  — Heb.  root  /JvdA,  to  cleave ;  Arab,  loot larva*,  to  bend,  whence  Unod,  the  twutmjf or  coiling  of  a  serpent
12993:pageant,  an  exhibttioii,  spectacle.  (Low L.wL.)  Oiig.  the  moveable  scafTold  on which  the  old  'mysteries'  were  acted. M.  E./*a.eyw/ (Prompt  Parv.)  ;  formed,  with excrescent  t  after  m,  from  Low  h.  pagiMa, a  scafTold,  stage  for  shews,  made  of  wooden plankft,  —  L.  pagina,  a  page  of  a  book,  also a  plank  of  wooii  Nanied  from  being  faa> tencd  together:  see  pago  (x),  "Dtt. pagt^ ant-r^Y.
15016:llier.«L.  pr9paginem,  ace.  of  propago,
23625:Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
===
leaf 347 printed~ 327 ety  entitled  Congrtgatie  dt  p» fide,  constituted  at  Rome,  a.d,  i6ai, see  Prune  (i). repay.  (F.-L.)    O.V.rrpaytr.^^ rt-  (L.  «-),  back 
leaf 362 printed~ 342 ec  pika  ^beluw). v.F.i«  L,>     Not  an  axe  at  alt, p"  *   *  f  E.  pikin'j,  pikiii,  a l  ,    later  picq^uois,   a L  M.  pierce,  thrust
```


## [2026-09-14T01:08:58.004Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(350,362):\n    print('--- leaf',i,'printed~',i-20)\n    print(leaves[i][:260].replace('\\n',' '))\nEOF",
 "description": "Scan SKT leaves 350-361"
}
```


### [2026-09-14T01:08:59.202Z] TOOL RESULT

```
--- leaf 350 printed~ 330
  find  also  O.  "DvL.paU,  a  fragment,  Fnesic palt,  a  rag.     Cf.  G.  xpalten.  to  split Pampas,  plains  m  S,  Amcnca.  (Pcm- vian).  The  linal  s  is  the  Span.pl.  suffix. •> Peruvian /a#j/a,  a  plain. Pamper;  see  Fap  (i). Pamphlet,  a  smal
--- leaf 351 printed~ 331
onic,  bat  borrowed  from] see    pawn    (1)  above.     The Mittle  pledge,'  i.e.  a  token,  1 penning,   Iccl.  penmngr,  Dan. mng\  G.p/ennig.O.  H.  G./J oi  p/ani  \  all  similarly  formed, Fanegyrie.  (I>.-Gk.)    L., a  eulogy;  from  h, panmn'nu, 
--- leaf 352 printed~ 332
  vocative  of  rdvor,  niv* wot.  papa,  father  (above). pope,  the  father  of  a  church,  bishop  of Rome.   (.L.  —  Gk.)      M.  E.  poptx    formed from  A,  S.  fkifa,  pope,  by  the  usual  change from  d  to  long  0.-L. /a/a,  pope,  father: sec 
--- leaf 353 printed~ 333
  «  L. •atoriitm ;  so  that  par/our  answers  to  a Low  L.  ifiijn  parabolatonum  *  i.not  found), a  place  to  talk  in.  vGf.  F.  dortoir  —  L. eionrtitoriHm.)    Sec  above. parole.  (F.-L.-Gk.)  F.  /afv//,  a von^  esp.  a  promiMi  the  same  wo
--- leaf 354 printed~ 334
IvfrfAort  a  plane  surface, ;.  af  lafovAor,  on  the  giouod,  from  Jni. sad  «i8or,  the  grcfcnd. MlOjK^BXllt  a  cxmclusioo  unwarranted ep»«miK«.  (F.-U-Ck.^     F. /am- ■c  «>  L,  pamleeismus. »  Gk.  va/NiAo7t- a  false  reckoning  or  concluiion.^
--- leaf 355 printed~ 335
m,  an  empire; see  omptro  (above). parachute,  an  apparatus  for  breaking «  fall  from  a  balloon.  (F.  —  L.)  F.  pam- thute.  put  for  pat^  ^  ehtU,  lit.  that  which parries  or  guards  against  a  fall.  —  F.  par<r, 10  deck,  U50  to  guard
--- leaf 356 printed~ 336
ritory,  a  wild  flower R^on  walU.  (F.-L.)  PtUilory trit&ry,  M.  E  pariiorii.—O,  F. ,  •pcllttofjr;'  Cot.  vL.  parUtaria, \  kul  oi pariftariur,  belonging  to m  faruf;  Stem  oi paries  (above). u  (F.-U-Gk.)  M.£./aW/fA/. MJW.^L.  jltsnrrMi.*Gk.  
--- leaf 357 printed~ 337
t,  a  partition;  Cot.  — F.  csmpartir,  to divide  into  equal  parts;  Low  X^comparlirt. —  L.  com-  {cum),  together;  partire,  to part,  from  parti;  crude  form  of  pars.,  a part. depart,  (F.  -  L.)  O.  F.  departir,  to diviile,  to  part  fro
--- leaf 358 printed~ 338
  OD  whom  all  libels  are 1*1000.  From  ihs  oaiuc  of  a ome,  whose  atall  was  frerjucnted his  name  was  iransfcrrcd  to  a nesT  his  stall  a1  his  death,  on dts  of  the  time  secretly  affixed lee  Haydn.  " see  Paton' Paasiv-e ;  see  Patien
--- leaf 359 printed~ 339
/vz/m/r,  a  patent  ;  so  called  because open  to  general  inspection.  —  O.Y,  pa/^nt (fern.  pcUenie),  patent,  wide  open.  —  L. pattnt-,  stem  of  pr.  pt.  of  patert,  to  lie open.  Cf.  Gk.  vtrafrv/u,  1  spread  out. (VPAT.) compass.  (F.  * 
--- leaf 360 printed~ 340
 high  road.  (Du.^ /&v^/a•/     Formerly  a  paJUif, I  00  tllB/«J^    LC.  foo(-^th.  - PATROL. 335 Da.  /a/,  a  path  ;  see  above.  (Many  catit words  are  Dutch.)  Der./o^,  a  nag,  orig. pad-nag,  a  road-nag. Pathos.  (Gk.)  Gk.  irtiOof,  sufTerin
--- leaf 361 printed~ 341
 pav-i-cr icf.  iarthy-*r)t  ixom  O.  F.paveurj  '  a  paTcr/ Cot. PavUlon.  (F.  -  L.)  M.  E.  pavi'/att.  - F.  pavWcn,  a  tent  ;  so  called  because spread  out  like  the  wingii  of  a  butterfly  — \».papitionem,  occ.  oipapitio^  ( l)  a  butterf
```


## [2026-09-14T01:09:15.928Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'kadah\\|kada\\b\\|but-\\|bhagavat\\|idol' SKT.txt | head -20; echo \"=== leaves w/ PAIL/PAIN\"; python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if re.search(r'\\bPail\\b|\\bPaint\\b|Palanquin|Pagan', l):\n        print(i, i-20, re.sub(r'\\s+',' ',l[:120]))\nEOF",
 "description": "Search SKT for pagoda-adjacent entries"
}
```


### [2026-09-14T01:09:17.315Z] TOOL RESULT

```
3021:oaniago.  (F.-L.)  F.  eama^,  flesh- lime,  slaughter  of  animals,  —  Low  L. camaticum,  a  liibut---  of  animals;  cf.  car- nafum,  time  for  eating  Hesh.  — 1*  cam-, stem  of  caro,  flesh.
5561:Dull,  stupid.  (E.)    M.  E.  ./«/     A?; fooliikb ;  put  for  dztvl*  ;  cf.  ^\ fal^  god,  idoL— A.  S.  dwoi , of  ktroug  vb.  dvf/an,  lo  err,  be  ^luJ.i:l.  + Du.   do/,    mad ;    Goth,    dtivtis,  fuCtli^,  (a ioii.  mad.     (^OJnWAR.)     See  DwalL
6223:fetich,  fetish,  an  object  of  su[«rsi worshio    vF.  -  Port.  -  L.)     F.  A*  " Port. yr/Vi'pp.  borcery,  lil.  artificial; name  given  by  the  Fori,  to   the made  idols  of  Afnc-a.  —  l^facdtiuj, ^\,  fact-uj,  pp.  offaccrt,  lo  make.
9078:*,— ,-   ^Tfltja,  Krvice  lo  idols  i^wherc
9095:Idol.  Idyll ;  see  Idea.
13039:M.  E.  pi^e. ^     ■-  Low  I-  fagium,  ace.  oi  pagius, Bnal.     Cf.  ^pan.  /(Sfr,  Port,  pagtm, ^^fcph*,  a  page     Ejym.  disputed;  but ^PEtav  is  a  mere  Tarianl  oipagtmsij, W/^fa^  to  a  village ;    from  L.  Pagus,  a Xftt  liiatarict ;    kc    Paffaa.     p.    Diet a  tbat   Ital. /W^Titf  was  formed  from a  little  w>y,  dimin.  of  »o«,  a Thfa   does   Dot    account    for   Port. which  certainly  points  to  L./»- (5c«  Dies,  Littr^,  Scheler.) \i\  one  ^de  of  a  leaf;  ace  Paol. t ;  see  Pact. an  Indian  Idol's  temple.  (Port. .)    From  Port./^(MSi,/^pMSr,  a  pa- t^Perv  ^wHln^bA,  ao  iaol*tcm]>le. — iatf,  idoU  image ;  kuioA,  habitation. I  Udal  Pen.  letter  is  sometimes  ren- bf  /,  a*  m  Devic's  Supp^  to  Littre.) ,.  Hm  Pai«ii(. <F. .  U)    M.  E.  p4iii4.  -  P.  /tf>W.
19406:Teraphim,  idols,  hoi'  %
19417:(VTAR.) itermlno.  ( F.  —  L.>  O.  F.  deUrminer. '  dttfrminart,  to  bound,  end.— L.  d£, U  fully ;  ttrminare,  to  bound,  from inus  ^abovc),  "Dvt.  prt-detcrmine, ;tenaiiiate.  (L.)  From  pp.  of  L. mimare,  to  put  or  diivc  beyond  bounds. £ff,  out ;  ttrmintu,  boundary. rmination.  (K,  —  L.)  F.  termina- »Lh  ojCc  ttrminationtm^  A  bounding, )g,_L.  terminatWt  pp.  of  itrminare, lund,  end.  —L.  ttrvtinus^  boundary. nninPB.end.(L.)L./frfflriwwj(abQve). nnA£:aiit.  (F.  •  Itnl.  -  L.)  M.  £. tagant^  %  (supposed)  Saracen  idol, t  %  raoting  character  in  old  moralities «}.  and  6nalty  a  scolding  woman.— .  TV/T.J.cifrt/.  7€rvaj;an,  a  (supposed) Sen  idol.«>IlaL  7rhng\inte,  the  same »to,  xii.  59).  Probably  for  Triva- },  the  moon,  wanderiri^  under  the  three Ef  of  StUnt  (or  Luna)  in  heaven, mis  {Diana)  in  earth,  rentthone Hrfina')  in  the  lower  world.  — L./^, e ;  magant;  stem  of  prcs.  pt.  of  uagari, LTHler.
=== leaves w/ PAIL/PAIN
348 328 mpuniti.^ L. Acc. impunitattm, ace of imputtifaj, impunity. * L. impum-s, without punuih* mcnt.oL. iiM- (*M-
362 342 ec pika ^beluw). v.F.i« L,> Not an axe at alt, p" * * f E. pikin'j, pikiii, a l , later picq^uoi
```


## [2026-09-14T01:09:23.853Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if \"an  Indian  Idol's  temple\" in l:\n        print('leaf',i)\n        print(re.sub(r'\\s+',' ',l)[:1500])\nEOF",
 "description": "Locate SKT pagoda leaf and page number"
}
```


### [2026-09-14T01:09:25.101Z] TOOL RESULT

```
leaf 347
ety entitled Congrtgatie dt p» fide, constituted at Rome, a.d, i6ai, see Prune (i). repay. (F.-L.) O.V.rrpaytr.^^ rt- (L. «-), back ; payer, to pay : see Fad (i), a soft cushion. (ScaDd.«>C1 C?) Also in the sense of 'saddle* (1 1570); also in the sense of (Halliwell). The same word as a bag ; see below. Der. pad, pod, a husk. ^.Scand. — C. I Orig. a leather bottle, a bag ; a pad stuffed bag, a cushion. •• SweiL dial. a cushion ; Dan. pude, a cushion. • * puf, a lar(;e buoy, iuHated sbeepskuL from the Celtic directly.) pudding, an intestine filled with a sausage ; hence, a sort kind of meat, 1 of flour, eggs, &c. (C.) Of Celtic cf. Irish putog, a podding, Gs W. pcten, a paunch, a pudding ; a bag, pudding, p. Further pwiyn. a short round body. large buoy, inflated skm ; all (aj from a base PUT, Co swell out. as dial, puta, to be inflated. Ct E. fa^t. Pad <a), a thief on the high road Path. Paddle (i), to finger, dabble; Pat (I). Paddle (9), a little spade Paddock (i). a toad. <Scanl> padfUk, dimin. of M. E. foddt^ m Icel padda, Swed. padJm^ Vm toad, frog. 4 Dn. pakdi, pad, UtZ' i.e. 'lumper;* cf. Gk. 9pohpit^ actifc.^ spand, to vibrate, whence fparfm- frog. (VSPAD.) Paddock (a), a small enclouuc: Park. Padlock, a loose- hanging U A lock for hampers, &c ; prob>. adding iacJk to prov. E. pad, • (Norfolk). This word is al*o wtil ICC Pedlar. Paan. a hymn to Apollo. (I*.«»Gk /tfaff.-Gk. n«iaa»,ZU(^, (1) Twmj' physician of the gods, (a) 4kfUk^ hymn to Apollo. p^oay, pieony. a flowYi
```


## [2026-09-14T01:09:34.548Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16214,16240p' HJB.txt",
 "description": "Read Hobson-Jobson PAGODA entry"
}
```


### [2026-09-14T01:09:34.602Z] TOOL RESULT

```
PAGODA,  s.  This  obacure  and remarkable  word  is  used  in  three different  senses.
a.  An  idol  temple ;  and  also  specifi- cally, in  China,  a  particular  form  of religious  edifice,  of  which  the  famous "Porcelain  tower"  of  Nanking,  now destroyed,  may  be  recalled  as  typical. In  the  17th  century  we  find  the  word sometimes  misapplied  to  places  of Mahommedan  worship,  as  by  Faria-y- Sousa,  who  speaks  of  the  ""ncoda  of Mecca."
PAGODA.
653
PAGODA.
b.  An  idol.
C.  A  coin  long  current  in  S.  India. The  coinB  so  called  were  both  gold  and silver,  but  generally  gold.  The  gold pagoda  was  the  vardha  or  htln  of  the natives  (see  BOON) ;  the  former  name (f r.  Skt.  for  *  boar ')  being  taken  from the  Boar  avatar  of  Vishnu,  which  was ■figured  on  a  variety  of  ancient  coins  of the  South ;  and  the  latter  signifying *gold,'  no  doubt  identical  with  sond, :and  an  instance  of  the  exchange  of  h And  8,    (See  also  PABDAO.)
Accounts  at  Madras  down  to  1818 were  kept  in  pagodas,  fanaTtis,  and  kds (see  Cash)  ;  8%^ = 1  fanam,  42  fanams =  1  pagoda.  In  the  year  named  the Tiipee  was  made  the  standard  coin.* The  pagoda  was  then  reckoned  as «(^uivalent  to  3^  rupees.
In  the  suggestions  of  etymologies for  this  wora,  the  first  and  most })rominent  meaning  alone  has  almost tilways  been  regaraed,  and  doubtless justly ;  for  the  other  uses  are  de- duceable  from  it.  Such  suggestions have  been  many.
Thus  Chinese  origins  have  been propounded  in  more  than  one  form  ; e.g,  Pao-t^ahy  'precious  pile,'  and  Poh- Jeuh-fah  (*  white-bones-pile ').t  Any- thing can  be  made  out  of  Chinese monosyllables  in  the  way  of  etymology  ; though  no  doubt  it  is  curious  that  the first  at  least  of  these  phrases  is  actually applied  by  the  Chinese  to  the  polygonal towers  which  in  China  foreigners  speci- ally call  pagodas.  Whether  it  be possible  that  this  phrase  may  have ()een  in  any  measure  formed  in imitation  of  pagoda,  so  constantly  in the  mouth  of  foreigners,  we  cannot say  (though  it  would  not  be  a  solitary example  of  such  borrowing  —  sea IfEELAM)  ;  but  we  can  say  with  confi- dence that  it  is  impossible  pagoda should  have  been  taken  from  the Chinese.  The  quotations  from  Corsali and  Barbosa  set  that  su^^^tion  at  rest.
Another  derivation  is  given  (and adopted  by  so  learned  an  etymologist as  H.  Wedgwood)  from  the  Portuguese pagao,  *&  pagan.'  It  is  possible  that this  word  may  have  helped  to  facili- tate the  Portuguese  ado|)tion  of  i7a^o(2a; it  is  not  possihle  that  it  should  have given  rise  to  the  word.  A  third  theory makes  pagoda  a  transposition  of  da-
*  f^naep's  Uuful  Tablet,  by  E.  ThGmM,  p.  19. t  Giles,  Glo$$aiTf  ofltefennee,  8.  v.
goba.  T]ie  latter  is  a  genuine  woid, used  in  Ceylon,  but  known  in  Conti- nental India,  since  the  extinction  of Buddhism,  only  in  the  most  rare  and exceptional  way.
A  fourth  suggestion  connects  it  with the  Skt.  bhagavat,  'holy,  divine,'  or Bhagavatiy  applied  to  Durga  and  other goddesses ;  and  a  fifth  makes  it  a corruption  of  the  Pers.  but-kadah, *  idol-temple ' ;  a  derivation  given below  by  Ovington.  There  can  be little  doubt  that  the  origin  really  lies l>etween  these  two.
The  two  contributors  to  this  book  are somewhat  divided  on  this  subject : —
(1)  Against  the  derivation  from hhagavaty  *holy,'  or  the  Mahr.  form bhagavant,  is  the  objection  that  the word  pagode  from  the  earliest  date  has the  final  e,  which  was  necessarily  pro- nounced. Nor  is  bhagavant  a  name for  a  temple  in  any  langua^  of  India. On  the  other  hand  but-kadan  is  a  phrase which  the  Portuguese  would  constantly hear  from  the  Mahommedans  with whom  they  chiefly  had  to  deal  on their  first  arrival  in  India.  This  is the  view  confidently  asserted  by  Rei- naud  (M^moires  sur  VInde,  90),  and  is the  etymology  given  by  Littre.
As  regards  the  coins,  it  has  been supposed,  naturally  enough,  that  they were  called  pagoda,  because  of  the figure  of  a  temple  which  some  of  them bear ;  and  which  indeed  was  borne  by the  pagodas  of  the  Madras  Mint,  as may  be  seen  in  Thomas's  Prinsep,  pi. xlv.  But  in  fact  coins  with  this  im- press were  first  struck  at  Ikkeri  at  a date  after  the  word  pagode  was  already in  use  among  the  Portuguese.  How- ever, nearly  all  bore  on  one  side  a  rude representation  of  a  Hindu  deity  (see e,g,  Krishnaraja's  pagoda,  c.  1520),  and sometimes  two  such  images.  Some  of these  figures  are  specified  bv  Prinsep (Useful  Tables,  p.  41),  and  Varthema speaks  of  them;  "These  pardai  .  .  . liave  two  devils  stamped  upon  one  side of  them,  and  certain  letters  on  the other"  (115-116).  Here  the  name may  have  been  appropriately  taken from  bhagavat  (A.  B.l.
On  the  other  hana,  it  may  be  urged that  the  resemblance  between  btU- kadah  and  pagode  is  hardly  close enough,  and  that  the  derivation  from but-mdah  does  not  easilv  account  for all  the  uses  of  the  word.  Indeed,  it seems  admitted  in  the  preceding  para-
PAGODA.
654
PAGODA,
graph  that  bhagavat  may  have  had  to do  with  the  origin  of  the  word  in  one of  its  meanings.
Now  it  is  not  possible  that  the  word in  all  its  applications  may  have  had its  origin  from  hkagavai,  or  some current  modification  of  that  word? We  see  from  Marco  Polo  that  such  a term  was  currently  known  to  foreign visitors  of  S.  India  in  his  day— a  term almost  identical  in  sound  with  pagodoy and  bearing  in  his  statement  a  religious application,  though  not  to  a  temple.* We  thus  have  four  separate  applications of  the  word  pacatUa,  or  pagoda^  picked \xp  by  foreigners  on  the  shores  oi  India from  the  13th  century  downwards,  viz. to  a  Hindu  eiaculatory  formula,  to  a place  of  Hindu  worship,  to  a  Hindu idol,  to  a  Hindu  coin  with  idols  repre- sented on  it.  Is  it  not  possible  that  all are  to  be  traced  to  hhagavaJt^  ^sacred,' or  to  Bhapavat  and  Bhcigavati,  used  as names  of  divinities — of  Buadha  in Buddhist  times  or  places,  of  Krislma and  Durga  in  Brahminical  times  and places?  (uses  which  are  fact).  How common  was  the  use  of  Bhagavaii  as the  name  of  an  object  of  worship  in Malabar,  may  be  seen  from  an  ex- ample. Turning  to  Wilson's  work  on the  Mackenzie  MSS.,  we  find  in  the list  of  local  MS.  tracts  belonging  to Malabar,  the  repeated  occurrence  of Bhagavati  in  this  way.  Thus  in  this section  of  the  book  we  have  at  p.  xcvi. (vol.  ii.)  note  of  an  account  "of  a temple  of  Bhagavati '' ;  at  p.  ciii. "Temple  of  Mannadi  Bhagavati  god- dess .  .  .";  at  p.  civ.  "Temple  of Mangombu  Bhagavati  .  .  . "  ;  "  Temple of  Paddeparkave  Bhagavati  .  .  . " ; "Temple  of  the  goddess  Panndyennar Kave  Bhagavati  .  .  .";  "Temple  of the  goddess  PatdU  Bhagavati  .  .  ." ; "  Temple  of  Bhagavati  .  .  .  "  ;  p.  cvii., "Account  of  the  goddess  Bhagavati  at, &c.  .  .  . " ;  p.  cviii.,  "  Ace.  of  the goddess  Yalanga  BhagavaHy"  "Ace.  of
♦  "  The  prayer  that  they  say  daily  oonaists  of these  words :  '  Paeauta  !  PaccnUa!  PaomUa/ '  And this  they  repeat  104  times.  "—(Bk,  lii.  ch- 17.)  The word  is  printed  in  Ramusio  fMcauoa ;  but  no  one fomiliar  with  the  constant  conftiHion  of  e  and  t  in medieval  manuscript  will  reject  this  correction  of M.  Fauthier.  Bishop  Caldwell  obeerves  that  the word  was  probably  Bagavd,  or  Pagava^  the  Tamil form  of  Bhaaavata^  "  Lord  " ;  a  word  reiterated  in their  sacred  formulie  by  Hindus  of  all  sorts, especially  Vaishnava  devotees.  The  words  given by  Marco  Polo,  if  written  ** Pagoda/  Pagoda f Pagoda/"  would  be  almost  undistingoishable  In sound  from  PaeatUa,
the  goddess  Vallur  Bhaaavati,"  The- term  Bhagavati  seems  uius  to  have been  very  commonly  attached  to objects  of  worship  in  Malabar  temples (see  also  Fra  Paolinoy  p.  79  and  p.  57, quoted  under  c.  below).  And  it  is- very  interesting  to  observe  that,  in  & ^per  on  "Coorg  Superstitious,"  Mr. Kittel  notices  parenthetically  that Bhadra  Kali  {i,e.  Durga)  is  "also called  Pogddi,  Pavodiy  a  tOidbhava  of Bagavati"  (Ind.  Antiq,  ii  170)— an incidental  remark  that  seems  to  brin^ us  very  near  the  possible  origin  of pagode.  It  is  most  probable  that  some form  hkepogodi  or  pagode  was  current in  the  mouths  of  foreign  visitors  be- fore the  arrival  of  the  Portuguese ; but  if  the  word  was  of  Portuguese origin  there  may  easily  have  oeen some  confusion  in  their  ears  between BagavcUi  and  hut-kadah  which  shaped the  new  word.  It  is  no  sufficient  ol>> jection  to  sav  that  bhagavati  is  not  a term  applied  by  the  natives  to  a temple ;  the  (question  is  rather  what misunderstanding  and  mispronuncia- tion by  foreigners  of  a  native  term may  probably  have  given  rise  to  the term?-(H.Y.)
Since  the  above  was  written.  Sir Walter  Elliot  has  kindly  fumi^ed  a note,  of  which  the  following  is  an extract : —
"I  took  some  pains  to  get  at  the origin  of  .the  word  when  at  Madras, and  the  conclusion  I  came  to  was  that it  arose  from  tbe  term  used  cenerally for  the  object  of  their  worsSin,  viz., Bhagavat^  '^od' ;  bhagavatiy  'goadess.'
```


## [2026-09-14T01:09:41.368Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E '\\bpwt\\b|pwt[^a-z]' SOD_pages.txt | head -30",
 "description": "Grep Gharib Sogdian dictionary for pwt"
}
```


### [2026-09-14T01:09:41.420Z] TOOL RESULT

```
11915:2858 btmyk C                                                        pwt(y), Pwy, Pw'n, Pwt>y, PwtkWn, bwq\PwS'k'm
12110:                                                                          ps'bwty, pwt-1
12120:       MDiii p37.13 n p39, 10                                           butane   ^pwtWk
12128: 2932 pwt>y                                                              2950 bxt C =» n>bxt
12144: 2936 pwt(y)                                                                    pron,, SCE 418; TSP; STii 9.12; Frag. Len.
12148:2937 bwty M -> pwt-1                                                              you
12149:2938 bwt(y) =* Pw-, pwt(y)
12153:      butist ©pi. ^pwt'yst
12726:     below, downwards, situated below                                  caw, zaw ©Parth. pwt ybgyw
13234:     caxsapaS (sks}pwt, cxs'pt) ©Parth. cx?byd-y                3328 cym- C
27411:                                                                     MSP b 153                                    pwt
27470:      Sogdica. 21.3; KG 23.36; GMS 1164; Hen. Cosm.          8238 pwt     M                               Ojijjk)>j>r
27480:  pwt-
27483:8239 pwt-' B, S, M                 (j>> >^ j.»)b*                         >y$tty, Dhu. 313; -ysty, SCE 510, 513;
27485:           pwty; ace. pwtw\ voc. pwt\ pi. pwt(})yst\ ob. pi.
27486:           pwOysty =»bwt, pwtty                                   8251 pwth B =» pwt-2
27487:         Buddha                                                   8252 pwtks'ytr =* pwt'k^ytr
27488:         GMS 36, 44                                               8253 pwtksytr =» pwt>ks>ytr
27490:8240 pwt-2
27499:                                                                  8256 pwtt}yst B, M =» pwt>yst, pwtty
27500:8241 pwt} B                                (<jjj> jlL~> jj>)hj>
27502:     Buddha                                                            (pwttyst)     =*pwt-\ pwty(y), pwt*
27511:8243 pwt'ks'ytr B                                                 8258 pwtty'kh      S(M) =* pwty>k(h)
27513:     (pwtksytr, pwt>ksytr, pwtksytr)        ©<Skt.                8259 pwtty*!!    B                                 \^moLl
27518:8244 pwt}ksytr =» pwt'k^ytr                                       8260 pwttyst     B, M =* pwt>yst, pwtty
27519:8245 pwt'kt'k B                              (o-lXo)bjj ^s^^~     8261 pwty      B => pwt-1, pwtty
27522:                                                                       putyak, butyak (pwtty'kh, pwt'ykh) ©ob. -y
27524:8246 pwtWk          B                     hji(<j Jajj^^hji             VJ; BSTBL; TSP; Frag. Len. 71.8, 88.3; -y, STii
27525:      p/butane (pwt^y) =»bwt}ny                                          8.10; pwufkhsKG       438
27531:8247 pwt}n())y =» pwt*!!*                                              silkworm     -ty
```


## [2026-09-14T01:09:42.469Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'sogdian loan' HENNING_selected_papers.txt | head",
 "description": "Find Henning Sogdian Loan-Words article"
}
```


### [2026-09-14T01:09:42.533Z] TOOL RESULT

```
11763:we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
11770:milar Sogdian loan-words in Pe nd-wif, ete,
```


## [2026-09-14T01:09:48.065Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if '8239 pwt' in l or '8238 pwt' in l:\n        print('leaf',i,'printed~',i-66)\n        import re\n        print(re.sub(r'\\s+',' ',l)[:200])\nEOF",
 "description": "Find SOD leaf/page for pwt entries"
}
```


## [2026-09-14T01:09:49.024Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11740,11800p' HENNING_selected_papers.txt",
 "description": "Read Henning context"
}
```


### [2026-09-14T01:09:49.235Z] TOOL RESULT

```
leaf 398 printed~ 332
331 TSP 21 ii 1, 17 8227 pwskfty M jUb icJd\s^A{J> ijo\j&\ d^> 8215 pwrny'nyh B fys ^Ujl <0^-' pu-skafte ©<*pw-skfs-, Skamp- =^skfty unobjecting purnyanya (pwrny^yfy)*) ^pwny'nyh piety GMS 369; BBB 68
leaf 399 printed~ 333
 332 pwt- woof GMS 1186; VJ; TSP; BSTBL; Frag. Len.; SCE; Sogdica. 19.15b STii 9.7; BBB; KG; ->yftf, Dhy. 163, 347; ob. pi. 8239 pwt-' B, S, M (j>> >^ j.»)b* >y$tty, Dhu. 313; -ysty, SCE 510, 513; put
```


### [2026-09-14T01:09:49.286Z] TOOL RESULT

```
Initial »- in a foreign word in Turkish can
 
 
 
  
  
 
 
161 Tmawsac 1945
 
OF THE PEILOL
  
 
ca
 
 
represent original s- or 2- that stab
As Turkish did not possess initial 2-,
        
nd was regularly replaced by #. ‘This is so well
hed that there is no need to quote examples; but
 
we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
tanduval “ nightingale" (see Kiya
 
   
entu'ch (‘mry’) = zandiedé gale” as see BSOS,, x, 104 sq.) prove, Thus suburyan may represent
nging (bind) ”, but also “ nightin
   
milar Sogdian loan-words in Pe nd-wif, ete,
   
tan earlier *zburyan, Its initial 2b- can perhaps be explaine
 
 
1s the outcome of an original zm-. Such groups of consonants
 
 
 
often subject to changes, especially when a word has to be adapted to an alien tongue. A good parallel for this par- by the Arabic for ibarjad form zmargad. The who
 
tioular change in a loan-word is provid
 
“emerald” structure of wargad clost maryan which, I think,
nal word that the Turkish tongue transformed into
   
resembles that of *So
 
dian *zmuryan or
 
 
are entitled to claim was the
 
 
ori
 
uburyan
 
‘Thus there was an Iranian word for tom!
 
or sepulohre” which consisted of a final
```


## [2026-09-14T01:09:55.620Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE 'loan-?words in new persian|LOAN-WORDS' HENNING_selected_papers.txt | head -20",
 "description": "Find Henning article title"
}
```


### [2026-09-14T01:09:55.746Z] TOOL RESULT

```
1094:rixo 'kdn’ (but Syr. loan-words in Tranian usually have -d).—(11) " Astrologers," of. Nyberg, i, p.7, and Buddh. snp(r VJ, 22, 27, 69, 9, 12%, sq., SCE., 264, I should like to take this opportunity to explain a Sogdian word from a closely related sphere namely mySBy, pl. myBBt’ (NB. a “Ii toRosnberg, I
3649:'y or yy in Jewish type of Aram by Mani, Rel. of the Man, pp. 111199.) Ha loan-words-'y replaces Aram. ay, ane.g. in remy, Of, also Man, MPeorn. mgin'yi’n * Menenians'” = mdindy-ip.An with a Persian suffix (os in Publ, HRWAMDYK) ; in Pal. both forms ocear: myln'y Pall, Vil, 1, and myindyl'n, Gr, 207%
11133:Tux study of “cultural loan-words” is perhaps the most fascinating of philolo from nation to nation, often undergo considerable phonetical
11770:milar Sogdian loan-words in Pe nd-wif, ete,
23150:changed, but did so without system and allowed adequate representa tions of current speech to stand beside antiquated forms. The Middle Persian disguise is sometimes so perfect that only an occasional Arabic word betrays the true character of the language. The word for “and”, pronounced 1, is still written ‘wd (23!), the Idafe-particle f appears as ‘yg (St) or 'y, the abstract ending -Fia -yh or singular of presents ends in -yd but was pronounced in ~dd (or perhaps ~éd), words in final -e and -d are still spelt in -g and ~'g, and this on ‘occasion even affects Arabic loan-words, e.g. jomlg—alax. Influence of Sogdian orthography may be detected in x’n'g “house” (for the expected x’ng), kten’nd “they do” (beside heennd), stos'ndg “burning”, and the like. Quite modern forms abound, e.g. 2-, in st, a'ym ‘from beside "c (and 'z) “from”, j’y or j’ “place"* (MPers, beside 'b'g, K’—ke for MPers. ka, ku, and hé, etc In metrical passages the spelling takes little notice of the form of the words required by the verse: the metre is not meant for the eye
```


## [2026-09-14T01:09:58.740Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11133,11230p' HENNING_selected_papers.txt",
 "description": "Read Henning Sogdian loanwords pp.93-94"
}
```


### [2026-09-14T01:09:58.796Z] TOOL RESULT

```
Tux study of “cultural loan-words” is perhaps the most fascinating of philolo from nation to nation, often undergo considerable phonetical
| pursuits, Such words, passed on
 
 
changes; but th rignifica- tions. So the me the leas we should arrogate to ourselves in the matter of
y possess very precise and limit e latitude we may claim in regard to form,
   
 
A. Dawasx Niya th twice a word prigha (Nos, 316, 318) which Liders, Teztilien ten Turkistan (Abh.P.A.W., 1936), p. 30, combined with Skt. priga in the Mahdeyutpatti, & Hi" thin flowe with figures”, In Doe. No. 318 (line 6) Liders corrected the text given by B speta-prigha“ whi which we shall be able to confirm with fresh n that prigha meant “‘unicoloured figured silk (= damask)” ean be fully sub-
In the Kharogthi documents found
    
 
 
there explained as
  
d silk”, Tib. dar ri-mo-can “ silk marked
 
 
, Rapson, and Senart, and proposed
 
damask”, an admirable suggestion
 
 
conclusion (based on his dat
   
stantiated now. His emendation has been approved by 1. Burrow, Transl. of the Kharosthi Doc., 140, p. 59, who nal
In the Mahieyutpatti prigha is spelt priga, with variants pringu and pringa. be pringa, ‘Thus spelt the word is found in yet another y of Buddhist fol. 382, of. Bagohi, Deux Leriques p. 280, No. 541.1 It is there exp thin silk material, damask ”.*
 
 
 
pest Sanskrit form would presumably
 
    
diction Fan-yw-ts'ien
   
anskrit-Chinois, i (1929), ed by & ling “fine and
    
         
                   
    
* We (el Laders 21 999); av Iranian anj’inakira (cf. Léders 31
+ Properly thin silken satia fabric, also thin
(Pall
   
in pasting tbat tacasa ibid, No tian, is thavoya
2 of
 
 
 
igored tallota"”
 
 
259)
 
151 TRANSACTIONS OF THE PHILOLOGICAL SocrETY 1945
 
*pring occurs only in Central Asian Sanskrit; it is unknown to Sanskrit proper, or indeed to any Indian dialect. However, it is found also in several Iranian languages, notably in those spoken in Chinese Turkestan ; it also appeared in Western Iranian, in Pablavi and Persian, whence it migrated to Aramaic and Arabic. We shall deal with Sogdian and Manichmean Middle Persian first Among the Sogdian manuscripts discovered by M. Pelliot at Tun-huang and published by M. Benveniste in 1940 (Mission Pelliot en Asie Centrale, série in-quarto, vol. ii, Testes Sogliens,
      
 
Paris, Geuthner) there is a shamanistic text (P 3) which describes th
application. ‘The poor “‘rain-maker ” (Jade-kare) needed an
 
rious types of “ rain-stones ” (Jade) and their
 
enormous number of utensils for his performance, enough to
 
discourage anyone from taking up his profession. Amongst ther duties he had to paint several pictures, one of the a kp'wtk pr'ynk = kapite pring " a dark-blue piece of damask " 3, 128), an mn Kp'uth pr’ynk “a light blue piece of damask” (P 3, 148). M. Benveniste, who tentatively suggested “rideau”, did not reco
 
   
   
 
ne our word,
 
We know next to nothing of
 
dian poetry. But among
 
the unpublished Manichwan Sogdian fragments there are at least two which seem to contain poems written in that language ; both are ir
stand. The contents of M 137! are described in its caption
 
unfortunately difficult to read and w
 
 
     
       
as a zndp'iyk = song-hymn ; its last lines are spytyy prymg myrcBn Garment of white damask, Brrvy mpyk "t By book in the hands Sryy 2'r wftyy kwrd'k Three thousand woven jackets, uynk'h 00 ive thousand ziinkas,
       
ng "t Baty’ jolden pen in the hi n'ktyne [end of fragment] Sil ‘The translation adi But the passage is valuable for at least tw Firs kind of
his is surely the snme as the 353 v2! “aut of inks”,
   
 
  
much sense,
 
ittedly not mi
 
of its words,
```


## [2026-09-14T01:10:05.983Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'in New Persian' HENNING_selected_papers.txt | head -20; echo \"=== bwt/idol\"; grep -n -iE \"\\bbut\\b.*idol|idol.*\\bbut\\b|Buddha\" HENNING_selected_papers.txt | head -20",
 "description": "Locate Henning SLW article"
}
```


### [2026-09-14T01:10:06.059Z] TOOL RESULT

```
=== bwt/idol
349:T ii D 94. Oblong piece of paper, eut from a Chin. roll, Obv. Chin,, part of a Buddhandmasiiira, Rev. Sogd., two complete and two frag. columns. The beginning of the text, with the title, is preserved. — In the preparation of this edition © not wholly satisfactory photo- graphic copy only could be used.
959:20 soapica time to time Buddhas ( e, and in the name of [ ] they revealed stories (#) 4)—(19) “He is inactive, workless.”” For MPers., ef. Nyberg, ii, p. 6.—(20) “More sorrowful, depressed,” see BBB., p. 60. The etymology proposed by Nyberg, ii, p. 100, for NP. Sogd. ’nl'wye (Man. “ndwze), which proves Or. --—(21) Sogd. clearly tive of of “heavy stem”, -eé-), theref
2386:Also the name of the Kuchean (‘kweyk, see BSOS., ix, p. 566) monk who translated the text from Kuchean (‘hwe'n'y) into Sogdian (eyeby/w), is incomplete : Ja-raksita of, Buddharakgita, Sarvaralgita, Adokarakzita, three famous teschers of Buddhism, from Kucha (see Miller, Sb.P.A.W., 1918, p. 581); Prajfirakgita, the translator of the Maitrisimit (born at Il-Balig, near Kulja); Punyaraksita (piony’rli’yt, in an unedited Sogd. colophon, T.M. 450), ete. His further epithet, myrn'tk ot myrs'th, is also not clear. The reading myrn’'tk (with Skt. ‘natha') is perhaps less satisfactory than myrz’tk: this might be an additional Sogdian name (** Mithra-son””, “ Sun-son,” “ Sunday-son", Mikr-sid), or else a patronymic, i.e. “the son of Mir”. Similarly, the name of the father is mentioned in the brief note at the end of the “ Tntoxicating Drink Reviling Sutra”, which indicates the proprietor of the manuscript : sremyk BRY putty’n eyitk = the Master P., son of S. For Sogdian names with mir, see above, p. 6, and BSOS., ix,
2427:Verso (First lines broken away) (18) writ (19) [.- - 12H mync:Brm'yk tp" -telated Dharma seal (?) (20) [.... -J'y1e rtyy rm yypd tu'n it is, And with his life ‘yj my'wen s'ct Bry’y (punctuation-marks) hemusthold . .. . completely. (22) [...- yon’ dm'r'Rh pBkth This) Sarpjfi-Dharmah- (23) [8 pust}(k’) "yo “Fnooyk — myrf'th Sitra(!) the Kuchean Mir-son (?) (24) [.... Jrk’yt dmnyonn—hee'n'y rakgita, the Sramapa, from the Kuchean ‘B'k] 3’ pro sywbyw sp'k language into the Sogdian language (26) [prw's|(uo 8'rt cum woyspyin has [translated], out of (21) [w't8'r "Hendy Syrywetyh friendship for all living beings (28) [ZY cen putl(y) Rh pn "yyS'k and the wish for the rank of Buddhaship. (29) (py8'r tow ZY pro pikh L’ 'krt'k [And whatever has] not [been] done lawfully (30) [. Vike spoty w8'yr5" - you yourself should put it in onder, (B1) [about 10 + £ve)'nyh yreyek’ ey freedom from the life of. (82) (about 11] eft blank (you will obtain). (End of page)
2440:—(26-7) For the restoration, of, Reichelt, ii, 70%—(28) Cf. S.7., ii, p. 548 (viii, 10), where we have ”yby against ”yy8'k (see BBB., p. 91), The translation “ Buddha-laksana” is, perhaps, not. satisfactory Of. also: ZKw ry/nty’ pen yr * He (ic. 2yt = Jeta) obtained the rank of Arhat-ship” (7a, unpublished). In Uyyur we have: buryan quit and aryant qutt (in Sogd. the abstract is used).—(90) BBB., p. 87 (on 736); ef. also Weller, on Dhyina, 18. w(y)8'yr- = ie = regulate, arrange, adjust, repair, Man, m'’n wyr'mndyyh = mental adjustment
2526:(Title) This is the Samgha (?) Khwastwaneft. Oh God, forgive my sins, Failing am I and sinning, indebted and a debtor, instigated by the greed-breeding (2), shameless Greediness, in thoughts, words ‘and deeds, by the looking of the eyes, the hearing of the ears, the speak- ing of the tongue, the grasping of the hands, the walking of the feet, since at every moment I hurt and injure the five elements . . . . the Buddhagotra (which is) in the dry and the wet ground, the five-fold plant beings, the five-fold animal beings.
5653:in each epoch, sends apostles: Sit{, Zarathushtra,] Buddha, Christ, (Fry. b)..» ovibintentioned ... from where... he camo. ‘The Misguided
6342:standable, it may be worth while to recapitulate the Manichean lation. The object of the divine inspirations he had received, was to make known the true state of the world to mankind. God had granted tions to earlier prophets, Adam, Zoroaster, Buddha, Christ, and
6551:the ten adversities in the world. (24-9) The second calumniator was Zimisp who slandered Azrué (Zarathushtra), and (so did) King Naksintar (= Aloxander)* who committed the murder of the Magi, and Kayfine, the son of Ahriman, who (= Ktiyiine) spoilt the Magian religion. (29-33) The third calumniator was WPRTT Upagupta ?),3 the éramaya,—and King Soks (=Afoka)* who slandered Buddha Sikman,* and further the sinner Devadatta who spoilt the Buddha's religion.* (83-7) The fourth calumniator was Iscariot who slandered Christ, and the (fourth) sinner‘=- (was) Satante=- the hard-hearted (#)7 onefe™
6593:who spoilt the Christian religion. (37-45) There were still other sinners whom Greed and Ahriman kept as their mounts and who slandered the Buddhas and the Arhants, the Righteous Déndirs and the Pious Men. All these many sinners shall be bound in the eternal prison, together with Ahriman, and they shall be .
6615:Restore: (rly tym 2K td Jw p'eny (bt it should be "esp. p's'y), oF {1ty tym can 'yerSlise pizny (however, thero shoald bo ZK before Sema). Pouibly Srm'ye jefe formed merly the end of «longer compound, * the cita-dharma-ria."" The introdection of rach Boddhist terms may be due 10 the translator; ef Hino 40, “tho Buddhas and Arhanta””—" the apostlon". In Any cas, the chapter bogianing in ine 48 need not have bwen joined originally with the preceding text
7556:0 he goes to and fro amidst those cruel ones, but always keops his consciousness so that his spiritual welfare is not perverted. And later on, ents, and Buddhas (apostles)? he is honoured and cheered
8897:«+. is finished, When the “ New God” is accomplished (11), on Sunday and Monday, the Mar Sisin Yimki takes place. In the morning when the people assemble, it is necessary to comfort and .. . the people in the beginning. Also, the great Buddhas (= apostles) of the Church, and the“ after-Buddhas” ...., the chief
9254:kings and rulers, grandees and noblemen, queens and ladies, princes and princesses. He fully exposed the Buddhaship of the Prophet of He completed and fulfilled all orders and injun tious that (had been given ] him by { Mani ]”, ‘The which aro omitted in the Middle Persian version, conclude the
9411:Caves of the Thousand Buddhas” at
9768:1203/6. “The Buddha was still living at that time, but this (fact) did not help those people not to become subjected to that action,” i.e. the effect of the evil deed was stronger even than the power of the Buddha.
10289:“pity is used of the Buddha, These Sogdian words make it po ‘© new explanation for the name of the “* Avesta": Apasdk/Abastég = The
10699:Jewels adered (and said) it was not taught by the Buddha". fT should have... and kept and hidden it... without the commandments and keeping the commandments... if I should have slandered and detracted . . ., hurt 1h life. .., kept sorvants . . ., split the unfted community into two parties,
10803:texts, 305 ZKuyh. 307 peny. 323 piché, read meurire 159 nt (also gloss.) read ZK. 361 'nbBy, cf. Gersheviteh, § 203. 363 ZK read ZKv. 966 cf. Sogdica, 16, 18, “stability 1 station 1”. 390 On 2 Geraheviteh, § 880. 401 eytk from koéta-, Gauthiot, Gramm. i, 97. 419 (as Skt. pac, BR. meaning 3). 492 teilaryidhi, ef. Pers. bad... 28208 (often in Muw). 433 knpy'strh “ particularly short” (¢ knpy). 467 pn'yit, 500 y'tyn’'k. B13 pyr'y'nt, 523 aybri, no doubt copyist’s mistake for sriyt, 46 m'th, S61 ‘dl’yrly (also gloss) BST yuy'r read yey/rstr. 582 “‘on the morrow, to-morrow " rather than tt 600 insert ZNH after *PZY. 621 ‘po wad ’kw; “how could I dare. . . not tolisten.” 635 uyrkyh. 689 ak'rn'k. G41 -dkr'h, Gt ticle 1 665 ZN read yh. 672/3 “so that you shall eat it, all you monks, as if”, 689 rldy. 713 poyred! (also gloss). 785 ef, also Parth. tyitym, BSO! 815 the MS. has pér'ySry, corrected into -Sty (or vice versa); was -Brky intended = pir yiky 458 1850/1 from 3+ karl, ef. also Sogdiea, 29 (0 11). 866 “except for a Buddha's or Bodhisattva's expedient (upiya)"; Chin, differs 8 1 copyist's mistake
11581:W. B. HENNING—TWO CENTRAL ASIAN WoRDS 158 as Buddhist term, suduryan is the equivalent of Skt. stiipa, ie. a mound or tower or pyramid or dome in which relios of the Buddha are preserved. It is found already in Uyyur ‘Turkish where in the hendiadys with either sin “tomb, grave "? (sce F. W. K. Miller, Uigurioa, i, 68; ii, 58; Bang-Gabain- Rachmati, Tiirkische Turfantezte, vi, p. 128, line 290 var.), or sitavan = SI a, &- (Vigurica, iii, 19, 21%) it in lace” in general. By itself it is met with in a Manichwan story (LeCoq, Tiirkische Manichaica, i, 6%, spelt
```


## [2026-09-14T01:10:13.507Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:10:13.515Z] TOOL RESULT

```


```


## [2026-09-14T01:10:17.252Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 بت ===\"; grep -n 'بت پرست\\|بتکده\\|بت‌کده' BQT_v1_pages.txt | head -10; echo \"=== leaf 234 area check\"; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nimport re\nfor i,l in enumerate(leaves[:20]):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: print(i,m.group(1), l[:60].replace('\\n',' '))\nEOF",
 "description": "Explore BQT v1 for بت"
}
```


### [2026-09-14T01:10:18.417Z] TOOL RESULT

```
=== BQT v1 بت ===
8587:اند ترسا ومردمانی بت پرستند و مردمان وی گروهی کوهی اند و گررهی دشتی . » « حدودالعالم
=== leaf 234 area check
leaves 777
```


## [2026-09-14T01:10:23.714Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(repr(leaves[300][:200]))\nprint('---')\nprint(repr(leaves[301][:200]))\nEOF\necho \"=== refs_online BQT page_offset\"\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['BQT']['page_offset']);print(d['BQT'].get('lookup_hint'))\"",
 "description": "Check BQT page structure and offsets"
}
```


### [2026-09-14T01:10:25.041Z] TOOL RESULT

```
'ست و 4 سب\n#احر یض « بکر اول و دای بی نقطه\nو سکون ثانی وتحتانی و صاد تقطه دار ء دآروبی\nاست که کلف را زابل کند » و انرا صفاهانی\n«گل\u200cکافشه» (۱) کوبند وحربی «عصفر» خوانند .\nاحب ۵ » بکسر اول و سکون تانی\nو '
---
'« ری الافی » خوانند ؛ و بجای بای بجد بای\nاخت - حم اول وسکون ثالی وفوقانی»\nبممنی مثل\u200cومانند و قرین ولظیی باشدب وددعریی\nخواهر را گویند » و بی بممنی اول نیزعریی\nمیدانتد ۴ .\nاختر ۴ ه بر وزن افر » رابت وعل'
=== refs_online BQT page_offset
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-14T01:10:30.493Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(450,460):\n    print('=== leaf',i,'~p',i-220)\n    print(leaves[i][:700])\nEOF",
 "description": "Read BQT v1 leaves 450-459"
}
```


### [2026-09-14T01:10:31.794Z] TOOL RESULT

```
=== leaf 450 ~p 230
ِ باور ۱ عم بر وزن خاور » بمعنی قبول
و دیق سخن باشد - و بمعثی اسئواد و راست
- واستوار داشتن هم‌بنظن آمده است .
باوره ۲ بفتح واو و سکون زا و دال
کاورزعینی ساوردین کودرز بافطاع مقرر فرهء‌وده
بود , ار اين شهر را در آن زمين بنا نمود ونام
خود کرد .
باوددی - ی پامردی . حنسوب
ساورد را گوبند.- نومی از آش‌آرد ح‌هست .
پاول - بنتم ثاث و سکون لام » نام
موضمي است که آ:جا جامةٌ ابریشم بفایت خوب
بافتد ۴ .
باون - بروزن کابین . سبد کوچکی
باشد که زنان پنبه ای که خواهند بربسند دد
از کف ۱
یاههار - بر وزن تاهار , ظرف و انا را
کوبند - و نوعی از خوانندگی و گوند گی‌هم
هم حست که آرا پهلوی و رامندی خوانند ..
باهت یزوزن أقو و تک باخسقل
برنگ مرفشیشای فضی, وچون نظر مردم بر آن
افتد بی‌اختار بخنده درا ید ومنیع آن‌دریاست»

=== leaf 451 ~p 231
الو خوداست چنانکه‌شاسته حشتیو اجب‌الو حجو د(۱)
را گونند .
و
بایگان ۴ باکاف فارسی بر وزن
آسمان » بمی‌حافظ ونگاهدارنده بات وخزانه
دار رایز
با بروزن صبا , درخانه و در سرا را
کوبند ۴ - و آشیرا نیز کون دکه از من یز ند»
و بن را بعربی حبةالخضرا گویند .
ببال دیگری ی پر یدن"- یعنی به
حمات دیگری کاری کردن .
بیقلث س بروزن خشتك : باره‌ای ازخوشة
انگور و خوشهٌ خرصا باشدکه چند دائة مانند
خوشهةٌ کوچکی بکجا جمم شده باشد .
لهر مه یتح اول‌وثانی وسکون رای شت»
جانوری باشد صحرایسی شبیه بگربه لیکن
دم نبارد و از بوست آن پوستن سازیه #۶
ونانی باشد که در ميان روغن بربانکرده باشند
و بسکون:ثانی نام درنده‌یست مشهور 6 -.وجیبه
بوشیده است و عصی, بند که آن ازپوست | کوان
دیو بوده -
و یکی اول
موشوا اکو, رذف
و بعریی فاره
. خوان
=== leaf 452 ~p 232
سموده
رستم اندر کوههای ۰ و پوست آبرا
جیبه جامه ساخت . خاصیتش آنست که درآتش
سیب درآب غرق شود و هیچ حربه مر آن‌کار
؛ وکویند وقتی‌درزمان الوشیروانآ نجالور
آن جاتور در مبان] نجماعت افتادم‌همه رامجروح
سلخت و کشت و خورد - و دسای منقش رومی‌را
نیز گفته‌اند که هر ساعت برنگی نماید .
یسوده ۱
با سین بی فطه بر وزن .
لیلسی ه بفتح اول و سکون ثانی و ضم
لام و سن بی‌قطهٌ ساکن. ریتی باشد که ازنان
خشك با روغن و دوشاب کنند , و ببای فارسی‌حم
بای - بکس اول, امربایستادن وتوقف
کردن باشد بمنی باست وتوفف کن ۴- وامربه
در نظر‌داشتن هم هست که از پاییدن ۴ باشك .
لیر یش » بکسر اول وسکون ثانی‌ورای
بی‌هطه بتحتانی رسیده وشین نقطه‌دار مفتوح بدال
ابجدزده» یعتی پریثان کند ویر کنده مازد ۴
بعمنی سودن و ساوبدن باشد .
پیسودان ۴ با د
=== leaf 453 ~p 233
لت » بفتح اود و سکون ثانی. آهار
جولاهگان را گوینده بمتی ه بردوی کار
مالئد ودر عربی نیز همین‌معنی دارد ۷ - ربمعنی
لیف جولاهکان هم آهفه است- و مرغابی را نز
کویند و معرب آن بط است - و چشم اول‌حعبود
وهسجوو کافران باش دکه‌بعربی صنم خوانند
و کثابه ازممشوق هم هست .
ِا - بختح اول بروزن‌عطا ۰ دوعی ازطمام
باشد که عربان هط و مات گویند» وباین عمنی
با نشدید ثانی هم آمده است - وبکس اول ام
بگذاشتن یمنی بگذار .
زتاده ه بروزن شراره , لیف جولاهگان
و شومالان بائد » وآن جاروب مانندی اس تکه
بدا آش و آهار بر تار مالند .
بتاو اد ه بروزن سزاوار . عافت‌رانجام
و آخر کار باشد .
بتاییدن بکسراول وبای حطی‌بروزن
گرایدن ؛ بمعنی گذاشتن باشه
تخاگ - بنم اول و سکون الی وخای
تقطهرار بالف کشده ویکاف زده » نام موضعیاست
ترديك بکاب
=== leaf 454 ~p 234
وتیردانی را کوبندک» پر از نبر باشد » ومعنی
تر کیبی آن‌بت ماننداست چه‌بت لِف‌جولامگان
و کیش ماننه را گومه .
تقالاب »با لام بر وژن محراب » غلاف
کل خرما را گود .
تلخ و ترش دضادادن کنایه
از راضی شدن بمحئت ء مشقت و قمت رزق از
قلیل ‏ و کثیروقناعت وسیری و کرسنگی وفقررفافه
و سختی و نرمی رو زکار باشد ۰ ۱
نج س بنتح اول و ثالی و سکون نون
و جیم » » بمعنی افگردن و فشردن - و بکنراول
اعر است به‌بتنجیدن » نی درهم بیج و بفثار
و از پی‌درآی .
لتی « بفتح اول و انی و سکون واو .
پیمتی مشرق باشد که در مفال مغرب است. -
و جابی را نز کون که هميشه آفتاب درآنجا
بتابد و آن نقیض تسا است - و جضم ثانی-قیف‌را
کوبند و آن بیاله‌ای باشدکه در زیرآن‌لوله‌ای
تصب کرده باشند ولولهٌ آن را بردهن شیشه‌نهاده
کلاب و روغن و اعثال آن درشی
=== leaf 455 ~p 235
و۳ مب
و فرویزدن چیزی در جابی باشف ۷ .
بتو ر ال ‌ حتح اول و ثالی_ بواررسیده
و رای بی‌نقطه بالف کشیده و.یعاف ده . چاحی
باشد که غله و امثال. آن در آن‌کنند و خلاشه
هم آخده است ؛ و بمعنی آخر بتفدیم تای‌فرشت
بربای آیجد هم هست .
تو لك « بنتح اول و ثانی مضوم بواو
و کاف زده » طبنق چوبینی باشد برمتال دف‌بزر که
که بقالان‌اجنای در آن کنند ۰ و باینه‌عنی‌بتقديم
تانی بر اول هم اه ات
و آفاشنگی اعد که نان فلرو فا سایتهت
و بیمتی خشکه پلاو هم آمده‌انت؛ وبمعنی اول
با تالی مشدد نیز بنظ آمده است
هیا - م ی و سکن نمی
بالف کشیده » بمی مینه باشد و آنرا مری
صد کوش , و بکر اژل هم امه ات ۲
مبار » بکسر اول‌پروزن بیار » بمعنی
مششت و رنج وححنت باشد ب و شيشةٌ قلرورةییمار
شت و قبیح تماید ؟ .
بتیاره بکر اول وفتح خامی برنج
و م
=== leaf 456 ~p 236
پجشلث ‏ بکر اول بی وزن سرتك »
بسنی‌حکیم و داشندبود ٩‏ - و مخفف‌بنجشك
هرهت که کنبجدكث باشدوحريي عصفورخوانند ۴ -
. بجل این اول و انی بر وزن دهل »
استضوان ای وت بان بندگاه
سای پای عیباشه » و بتاز ی کعب مبگویند ۴.
4حم س بنم ارل و سکون ثانی و میم »
کرمازاه است که مبو؟ درخت کز باشد» وبعربی
شمرقالطر فا خوانشد » و بکسر اول‌هم آمدماست .
در بای ابچد باجیم فارسی
چ - بش او و سکون ثانی , ادرون
لنبوی دهن باشد ۷ - و موی پیش سر را تیز
کنتماند .
بچ‌بج « ینم دو بای ابجد وسکون دو
جیم فارسی؛ حرف‌زدنی باشد در نهایت آهستگی»
و سرکوشی را دز کویند ۸ - و لقظی اس تکه
شباهان بزرا بدان نوازش کنند وییش خودخوانند.
پچر اعد سیدن - کنابه از رسیدن
بدواشی باشد با رسیدن بشدمت دولتمندی .
‌
پچ رگ ه بکر اول بر وزن خشتك »
بمعئی سخر
=== leaf 457 ~p 237
بچکم - بفتح اول و کاف بروزن شبتم»
خانة 7 اطراف آن را شکه
کرده بشند ۱ - و ابوان و سفه و بارکده را
نیز گویند - و بمعتی کر که هم آهده است که
بعربی ذئب‌خوانند » وبکسر اول هم درست‌است
بچل - بر وزن کچل . شخصی را گویند
که پیوسته لیای خود راضایم کند و چرلگوملوث
گرهاند .
چم ع بکر اول بروزن شکم » کاریرا
وید که با نظام و آراستگی بود ۴ - و اعر
بچمیدن هم هست که خرامدن بناز باه یعنی
بخرام ۴ #۶ .
بچه‌جود ۰ کنابه ازلمل و بافوت
و طلا و نقرء و دیگر جواهرکانی و فلز ات‌باشد .
بچه حور شید - بممنی ,چخوراست
بحر خوارزم
بجة خو فی - کنابه از اعك
ماش . ۱
بچة طاوس علوی « کنابه از
آفتاب - و روزروشن - و آتش - و لملتییاقوت
باشد .
بچ کو ۴ جنم کاف و سکون واو .
شخصی که او را درطفلی ازرایگنر‌داشته باشند»
و بعربی لقیط خوانند .
=== leaf 458 ~p 238
سه؛: روزة خوارزم که ای آنجا جمع حود و کنابه از دمت صاحب همتان هم هست .
پحردمان مق عمل - یب از | بحری که دم آنرا برکزدن اسبان و برد سر علم
ی بندند ۰ و بعضی کوبنذ کاوی است که در کوههای
۳0 بح - بکراول و شم تالی و قتح‌قاف
که بیم حلاك نزدیعان باشد . و مسکون دال ۰ یمنی فوثق کند ۴ .
بحر نهنگ) بار عد و بحر نهنك آسا پجیر | - بروزن‌صیرا » نلمراهبی‌وزاهشی
کنابه از تیغ و شمشیر آبدار است. . بوزه است که صرالی و قسد شناختن او ییفمبر
بجر و سيع ه کت‌ابد از فلك است - | آخرالزمان را درتاریش هست ۴ .
بیان هشتم
دربای بجد باخای تقطه‌دارمشتمل برچهل و سهلفت و کنایت
است بمعنی بیار علم » و چون درآن شهر علما
و فضللا بسیار بوده‌اند بثابر آن‌بدین نام موسوم‌شده
۱
بخالذافکندن کن‌ابه از مظلوم
ءخواروتظلم کردن٩‏ وبخواری‌وزاری
=== leaf 459 ~p 239
--- 1۳۵
باکت .- بروزن‌سخت؛ بمعتی‌طالع باشد ۷ -
و سیاهی را نیز گویند که در خواب بر مرم‌افتد
و آنرا بمربی کابوی وعدالجنه خوانند ۴ سونام
جاتور کی است‌شبیه بملخ - ویضم اول‌نفام‌پادشا‌ی
بت د ندان‌خای کنابه از طالم
نا موافق و بخت ناماعد .
بختنگاو - منم ارد وسکون نانی‌وئاك
۳1 کاف قارسی بالف کشیده و بواو زده ۰ تطول
را کوبند و آن‌دوایی چند است که باهم‌بجوشانند
و بدن بمار را بدان شو ند .
بحتو ت- سم بضم اول و سکون‌نافی وفوفانی
بواو رسیده . هر چبز ریدم ماشد عموماً .- ورعد
را کویند خصوصاً ؛ و ختح اول هم آمده است
بحتور چم اول‌بروزن عزدور ؛بمعنی
ستتو باشد که رعد است - و شس غرنده را نیز
بخود
اول و رایع بمعنی صاحب بخت باشد ۴ و باین ۱
ممنی بروزن فغفور نیز درست است ٩‏ .
تقو ه منم اود و ثاك و سکون‌ثانی
و رعدرا
```


## [2026-09-14T01:10:45.423Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && grep -n 'بتکده' MON_part1.txt MON_part2.txt | head -5; echo \"=== polow\"; grep -n 'پلو ' MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Mo'in files"
}
```


### [2026-09-14T01:10:45.617Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
MON_part1.txt:21193:بتستان: 00۱-۵)6۵(۲ (امر.) تخانه» بتکده. 
MON_part1.txt:21196:بتکده: (ع-)۵02(-00۱ (امر .) ستخانه» شستان. 
MON_part2.txt:5965:بتکده. بتخانه. (.) هر شهر حسن‌خیز: جایی 
MON_part2.txt:7941:فعستان: 0 ] (امر.) ستخانه» بتکده. 
=== polow
MON_part1.txt:32565:پلو ان: مامح [- پلون] (.) بلندی اطراف 
MON_part1.txt:32572:پلو س: ۲0۱5 [- پلواس] (ا.) فریب دادن به 
MON_part1.txt:56618:و در صبحانه خورند. پلو (بلاو) بدون 
MON_part1.txt:79666:پلو دم کنند و پس از دم کشیدن بردارند و 
MON_part2.txt:11343:پلو که از برنج و باقلا تر تیب دهند.
```


## [2026-09-14T01:10:46.522Z] TOOL CALL #35: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:234 --image 2>&1 | tail -40",
 "description": "Render BQT page 234"
}
```


### [2026-09-14T01:10:47.755Z] TOOL RESULT

```
no scan of BQT covers printed page 234 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:10:50.645Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21180,21200p' MON_part1.txt; echo \"=== polow headword\"; grep -n '^پلو' MON_part1.txt | head -20",
 "description": "Read Mo'in بت area"
}
```


### [2026-09-14T01:10:50.734Z] TOOL RESULT

```
بت. ۱ نام دیوی است که مردم را به 
بت‌پرستی وا می‌دارد؛ يا - بد - بودا. (.) 
پیکری که از سنگگ یا چوب يا فلز به شکل 
انسان با حبوان سازند و آن را پرستش کنند؛ 
بغ» ف ؛ صنم. معشوق» محبوب؟ ج. بتأن. 
بتاو ر: 92۱5۷2 (.) عاقست» انجام. 
بتخانه: (0-)۳۰۰«۵۴۵ (امر.) جایی که بت‌ها 
را گذارند» معید بت پرستان» صنم خانه؛ 


ستگده. حرم» ح مسرا» متام رنان و 
معشو قگان شاهان و بزرگان) فغستان. 
بتر : ۲ |[ - بد تر ] (ص تفضد.) بد تر. 
بتستان: 00۱-۵)6۵(۲ (امر.) تخانه» بتکده. 
بتفوز: ۳۷۲02 [پتفوز] (.) پیرامون دهان 
اسان و حوان. منقار مرغان» نو کث. 
بتکده: (ع-)۵02(-00۱ (امر .) ستخانه» شستان. 
بتو: 02-۷ (.) جایی که غالا آفتات در 
آنجا بتابد) مق. نسا. مشرق؛ مق. مغرب. 
بتو: ۲۸45 (.) قیف. قبه و گوی سر عصا و 
دمجتی: سر 
=== polow headword
1217:پلور. شمشیر (در غلاف). 
1767:پلور. این زجاجی. ظرف شیشه‌یی؛ ظرف 
11320:پلویی که از برنج و گوجه‌فرنگی پزند. 
32559:پلو: 0۷ [- پلاو - پلا] (.) غذایی که با 
32565:پلو ان: مامح [- پلون] (.) بلندی اطراف 
32572:پلو س: ۲0۱5 [- پلواس] (ا.) فریب دادن به 
79666:پلو دم کنند و پس از دم کشیدن بردارند و 
85813:پلو. طرز تهیه آن چنین است که شکر را
```


## [2026-09-14T01:10:55.982Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32555,32572p' MON_part1.txt",
 "description": "Read Mo'in پلو entry"
}
```


### [2026-09-14T01:10:56.054Z] TOOL RESULT

```
که صفات پلنگ دارد. پلنگ گوزن‌افنکن: 
کته الا وه ره دی تب فک 
خاریدن: بکار پر خط پرداختن؛ به امر خطیر 
مشغول شدن. چرم پلنگ: پوست پلنگك. 
پلو: 0۷ [- پلاو - پلا] (.) غذایی که با 
برنج جوشیده شده در آب تهیه کنند و با 
کره یا روغن به انضمام اغذيةٌ گوشتی دیگر 
(بصورت قیمه» خورش» کباب) صرف 
می‌شود؛ پلاو. 

پلو ان: مامح [- پلون] (.) بلندی اطراف 
زمینی را گویند که در میان آن زراعت کرده 
باشند و مزارعان بر بالای آن آمد و شد کنند 
تا زراعت بایمال نگردد و آب در زمین 
بایستد؟ بطلندی گردا گرد زمین کاشته» بلون» 
مرز. بشتوارة کامل. 

پلو س: ۲0۱5 [- پلواس] (ا.) فریب دادن به
```


## [2026-09-14T01:10:57.255Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/pilaf",
 "prompt": "Give the full etymology of pilaf: the chain through Turkish, Persian, and any Sanskrit pulāka mention. Quote exactly."
}
```


### [2026-09-14T01:11:02.332Z] TOOL RESULT

```
# Etymology of Pilaf

The word "pilaf" traces through multiple languages in this chain:

**English ← Ottoman Turkish ← Classical Persian ← Hindi/Urdu ← Sauraseni Prakrit ← Sanskrit**

According to the Wiktionary entry, the word was "Borrowed from Ottoman Turkish _پلاو_ (modern Turkish _pilav_), from Classical Persian _پلاو_ (pilāw), from Hindi _पुलाव_ (pulāv)/Urdu _پُلاؤ_ (pulāo), from Sauraseni Prakrit _\*𑀧𑀼𑀮𑀸𑀕_ (\*pulāga), from Sanskrit _पुलाक_ (pulāka)."

The entry notes that the Sanskrit term is "probably of Dravidian origin," and it's "Akin to Tamil _புழுக்கு_ (puḻukku, 'cooked rice')." The word is listed as "Doublet of _pulao_."
```


## [2026-09-14T01:11:07.019Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pagoda",
 "prompt": "Quote the full etymology of pagoda, including Portuguese pagode, Persian butkada, Tamil pagavadi / Sanskrit bhagavati."
}
```


## [2026-09-14T01:11:09.178Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%AA",
 "prompt": "Give the Persian entry for بت (but/bot) 'idol': full etymology — Middle Persian, Sogdian, Parthian, Sanskrit buddha; any citations (Henning, Hasandust, MacKenzie). Quote exactly."
}
```


### [2026-09-14T01:11:11.430Z] TOOL RESULT

```
# Etymology of Pagoda

The word "pagoda" entered English in the 1580s, referring to "a sacred tower, richly adorned" in Burma, India, Siam, and China. The term derives from Portuguese *pagode* (early 16th century).

The Portuguese term likely came from "a corruption of Persian *butkada*, from *but* 'idol' + *kada* 'dwelling.'" Alternatively, it may derive from Tamil *pagavadi*, meaning "house belonging to a deity," which traces to Sanskrit *bhagavati*, the feminine form of *bhagavat* meaning "blessed, adorable."

The Sanskrit root *bhagah* connects to the Proto-Indo-European root *\*bhag-*, signifying "to share out, apportion; to get a share."
```


### [2026-09-14T01:11:14.961Z] TOOL RESULT

```
# Persian Entry for بت (but/bot) 'idol'

## Etymology

The Persian term derives from Middle Persian *bwt'* (/but/, "Buddha, idol"), ultimately tracing to Sanskrit बुद्ध (buddha). The entry notes this is a "doublet" of بد (bud/bod).

## Etymology Statement from Source

"Inherited from Middle Persian [Book Pahlavi needed] (bwt' /⁠but⁠/, 'Buddha, idol'), ultimately from Sanskrit बुद्ध (buddha)."

The source indicates the classical Persian meaning expanded beyond religious artifacts to encompass "beauty; beautiful person; the beloved" in early ninth-century sources.

## Citation References

The Wiktionary entry lists three reference works but provides no direct quotations from Henning, Hasandust, or MacKenzie. The entry includes a classical citation from Firdawsī's *Shahnameh* (circa 1011) demonstrating usage, but lacks the specific scholarly sources you requested for etymology documentation.
```


## [2026-09-14T01:11:23.566Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n -iE \"^but|^bwt|idol|Buddha\" PHD.txt | head -20; echo \"=== NYB\"; grep -n -iE \"^but|bwt|idol|Buddha\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg for but/idol"
}
```


### [2026-09-14T01:11:23.701Z] TOOL RESULT

```
=== PHD
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
1107:Buddha but.
1125:but bē.
1126:butter kär, rdyn.
1127:buttermilk, dried ~ kašk.
1128:buttock kin.
2354:idol but, uzdés.
2355:idolater uzdésparist. i
2356:idolatry déw-ésnih / -ézagih, uzdés- paristišnīh.
=== NYB
359:; forms a unit with bütan: MPrs wnybwt
805:avinn-biiteh [~-bwtyh or -YHWWN-tyh] abstr. of the preceding w.: waste, loss 420-21; the state of one defeated 638. — As to formation cf MPrs hy’rbwdyh ‘friend- ship’ (A-H II).
978:but (also) 455-5; — b) but, however, contin- uing the narration: HajB:8 (second BL") [= bes HajA:7, v. below]; 197-24. 2115 ete. — MPrs by only with the enel. --c: byc ‘but’ (v. 4b) and in by-rwn (v. beron), in all other cases 5b’, to be read bd, shortened form in proclitic position (cf k? = ka, v.s.v. ka); MPrth byh ‘outside’, ^ byh, ^w byh ’rg; conj. byc, byž ‘but, however’, Prth. inscr. bes (v. below). Paz. be, bi, be; NP only prev. bi-. Original form *bét, cf bēt-ānak ‘an outsider, foreigner’; MPrs bydwm ‘outermost’ (S) = Paz. bétum (SGV). [MPrth byd ‘again, further’ (= MPrs dwdy) belongs to the numeral ‘two’, and not to this w.] — BR? 19% is a wrong ideogr. for beh, opt. of bütan.
1058:bütak [bwtk'] produced from material substance, pdoct, opp. āfrītak (g. v.): 6218. — Cf bavišn.
1059:bitan [bwtn'; YHWWN-tn'; forms v. I, 176] bav-: supplements the wanting inf., modal pres. and fut., imp. and pret. of
1070:būtēh [bwtyh; YHWWN- tyh] v. avinn- büteh.
1808:ham-biitan to be together with, to follow: či kanārak i... apar hambüt [hmbwt'] hom I kept on together (with him) all
1816:hamé-bitéh [hm’y bwtyh] abstr. of the sentence hamé bit ‘he has always been’, thus: the quality of having existed from eternity (Arab ?azaliya) 63°; cf also hastéh.
2124:but we are here in a part of Iran where Greeks reigned for about 200 years after Alexander (v. Tarn, The Greeks in Bactria & India, 1951). There is every reason to believe that their kings and magnates erected monumental buildings over their tombs, with which the Yvy1 of the de- ceased was in some way connected. The Greek Yvx1 could, however, only be ren- dered in Iranian by jän, as the ruvān belonged to a quite different sphere. Prob- ably these seven jdnakdns were built in the seven cities which Alexander founded in Bactriana and Sogdiana (Justin XII, 5, 8). The later attribution of such ancient monuments to the primordial heroes of East Iranian antiquity is a phenomenon too well known to need comment, cf Taxt + Jamsid, Nags 1 Rustam and the like. — Strictly speaking the reading HY?-d’n' = jän-dän 're- captacle of the jan’ would be admissible (cf uvnuciov Ļvxījg of the cinerary urn Sophocles, Electra 1126-1127), but this interpretation is perhaps too hazardous. — jānakān has a parallel in MPrs rw’ng’n, MPrth ’rw’ng’n ‘belonging to, serving the ruvan’, of pious works.
3059:patkar [ptkly, Prth ptkr]image ŠPrs: 3. 14. Prth:4. — OP pati-kara-; MPrs phykr; Arm. lw. patker ; Syr. Talm. lw. ptakrä ‘an idol’, Mand. lw. patikrä; NP paikar.
3867:uzdaés-tacar [^wed?ystc?l] temple of idols, heathen temple 1131. — Av. *uzdaēsa- (not attested in our texts) ‘monstruous phenomenon, monster, idol’, from Av. (673) daésa- ‘sign, omen’, + OP tacara- ‘palace’; very archaic form of wzdes-cor, q. v.
3870:uzdés [^wzdys] idol 71%. 82U, — V.s. v. uzdaés-tacar.
3871:uzdés-car [^wzdysc?l, >wedyse’l] temple of idols 7133. 9918, — < uzdēs-tacār, v. uzdaēs-
3876:uzdés-parist [^wedys plst'] idol-worship- per 71”. — MPrs ’wzdyspryst (A-H II). V. paristätan.
3877:uzdēs-paristišnēh [—-šnyh] idol-worship, idolatry 711°.
6175:wnybwt: äkasi
```


## [2026-09-14T01:11:31.657Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"*but [bwt\" in l or \"* but [bwt\" in l:\n        print('leaf',i,'printed p.',i-21)\nEOF\necho \"=== HRN but\"; grep -n -iE 'Götzen|but .Götze|182\\.' HRN.txt | head -20",
 "description": "Find PHD page for but; grep Horn"
}
```


### [2026-09-14T01:11:33.195Z] TOOL RESULT

```
leaf 43 printed p. 22
=== HRN but
1991:W82. but ^Götzenbild; Liebchen.
8287:freuen , ergötzen ; sich ergötzen' (N ö 1 d e k e , mündliche
10736:182. ftiaslnitan (aw. [/^maet- , mi^naitl entsprechend ;
11010:182. spaxff *verleumderisch', spazgth 'Verleumdung' (Men.,
11113:20Ii. nxd{i)st (meist uj' geschrieben) *), uzd{i)stäv 'Götzen-
11114:bild', nzd{i)stparast(i)&nlh 'Götzenanbetung (Men.),
11115:uzdejär (päz. uzdezdr) *Götzentemper.
11521:(«f» 7, 182.
11930:6m/ 182.
13625:sipergt 182.
13630:8ipezg% 182.
15073:5i7«7i- 182.
15376:spat'ia- 182.
15774:m 182.
17505:nvapürnn- 182.
```


## [2026-09-14T01:11:38.432Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1985,2005p' HRN.txt; echo \"=== leaf\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"182. but\" in l or \"W82. but\" in l:\n        print('leaf',i,'printed p.',i-21)\nEOF\necho \"=== HUB but\"; grep -n -iE '\\bbut\\b' HUB.txt | head -20",
 "description": "Read Horn 182 and grep Hübschmann"
}
```


### [2026-09-14T01:11:39.687Z] TOOL RESULT

```
(Men., Bund.); vergl. ai. babhrü- *braun, Ichneumon.
Das np. Wort bezeichnet den *Biber' nicht, es scheint
aber lautlich identisch zu sein. Ob Biber heute in
Fersien vorkommen, ist nach Blanford, Seite 51,
zweifelhaft.
r
W82. but ^Götzenbild; Liebchen.
aw. Büiti- N. pr. ; phlv. Büt, Bütjan (Gemme, Hörn,
Mitteilungen, Heft IV, S. 40, Note).
Wenn die Zusammenstellung richtig ist, so gehört
np. but in dieselbe Kategorie wie gStl^ ätes, petyäre
u. a. m.
188. hiziSk, bijisk (*bishk) 'Arzt* (Sahn. I, 32 Vers 180,
182), bmski (Sahn. I, 25 Vers 43).
aw. baesaza^ 'Arzenei, Arzt'; phlv. bBsazak (PPGl.),
*) Tiger kommen in den kaspischen Provinzen Persiens vor.
Vergl. W. T. Blanford, The Zoology and Geology, Vol. II von Easteni
Persia, An account of the journeys of the Persian boundary com-
mission 1870—1-2, London 1876, Seite 34, ein Werk, das ich für ähn-
liche Fälle öfter zu Rate gezogen habe. Leider führt es meist die
persischen Worte selbst nicht an.
=== leaf
leaf 63 printed p. 42
=== HUB but
821:182. Np. hut ^Gotzenbild, Idol' (afgh. LW. but) nach Fr.
6378:Haus' oben p. 24; banu *Herrin (?) H. 178; but Idol' s. oben
6445:= phi. syr. talmud. xarbuz 'Esel-ziege*; Xoroh-but N. pr.
6446:= phi. FarraxV'bUt] Sebuxt N. pr. (Elise) = pers. Ssbuxt
6704:Persian writers used the letter S for d (nach Vokalen, but never after
10358:but 2i.
```


## [2026-09-14T01:11:46.252Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '818,835p' HUB.txt; echo \"=== leaf\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"182. Np. hut\" in l or \"182. Np. but\" in l:\n        print('leaf',i,'printed p.',i-10)\nEOF",
 "description": "Read Hübschmann 182"
}
```


### [2026-09-14T01:11:47.548Z] TOOL RESULT

```
Nach Noldeke ist vabr 'Klippdachs* „wohl echt
arabisch**.
*) Also falsoh ftir vavar, vgl. avar oben Nr. 53.- 26 -
182. Np. hut ^Gotzenbild, Idol' (afgh. LW. but) nach Fr.
Miiller = Buddha, nach H o r n ~ zd. buiti 'Name eines
Damons' (vd. 19, 1). Beides schon im grossen Bunde-
hesh, vgl. Darmesteter, le Zend-Avesta II, p. 259.
184. Np. haSa, haSSa Munges, Kind' = phi. vacak (aus
*vaccak = vaUcaK*^) ist zunachst zu trennen von osset;
vdss *Kalb', bal. gvask *Kalb, Kalbchen (Geiger, Lautl.
p. 26), wax. vusk, sar. vi^k *Kalb', die auf iran. "^vasa^
-~ skr. vatsd' *KaIb' (vgl. skr. vatsaka- 'Kalbchen')
zuriickgehen und einem np. *vah' entsprechen wurden
(vgl. maht Tisch' = zd. masya^, skr. matsya-).
187. In bal. gvadil *feige' (aus ^gvaddil = *gvat-dil) ist
dil sicher persisches LW., dagegen wird goat echt sein
= np. badf phi. vat (arm. LW. vat) =■ ap. ^vata-. Da
es aber nur in gvadil vorkommt, nahm ich an, dass
=== leaf
leaf 36 printed p. 26
```


## [2026-09-14T01:11:59.146Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE 'LOAN-?WORDS|LOANWORDS' HENNING_selected_papers.txt | head -20; echo \"=== TOC\"; sed -n '1,60p' HENNING_selected_papers.txt | head -60",
 "description": "Check Henning Selected Papers contents"
}
```


### [2026-09-14T01:11:59.216Z] TOOL RESULT

```
1094:rixo 'kdn’ (but Syr. loan-words in Tranian usually have -d).—(11) " Astrologers," of. Nyberg, i, p.7, and Buddh. snp(r VJ, 22, 27, 69, 9, 12%, sq., SCE., 264, I should like to take this opportunity to explain a Sogdian word from a closely related sphere namely mySBy, pl. myBBt’ (NB. a “Ii toRosnberg, I
3649:'y or yy in Jewish type of Aram by Mani, Rel. of the Man, pp. 111199.) Ha loan-words-'y replaces Aram. ay, ane.g. in remy, Of, also Man, MPeorn. mgin'yi’n * Menenians'” = mdindy-ip.An with a Persian suffix (os in Publ, HRWAMDYK) ; in Pal. both forms ocear: myln'y Pall, Vil, 1, and myindyl'n, Gr, 207%
11133:Tux study of “cultural loan-words” is perhaps the most fascinating of philolo from nation to nation, often undergo considerable phonetical
11770:milar Sogdian loan-words in Pe nd-wif, ete,
12201:and classical spelling is p'askwn|i alone.—The following two are loanwords
12482:Pazend, e.g, SGV., xvi, 25, 38 loanwords in Aramaic that ap Tn the homilies of Aphraat
13264:). ‘There are forms with & and s, Persian d6r(-), but Bakhtiari str (Lorimer, p. 69), Gabri of Yexd sir (Lorimer, JRAS., 1916, 437), Baluchi sir, Brabui sbr, and last but not least Pahlavi sir. ‘The word is unknown to Oh to be restricted (loanwords from Persian excepted) to the area of Persia and Baluchistan. Could it belong to a substrate language and be connected with Dravidian ‘ewoar (Gondi savor, GondiM. hovar “salt, Tatil, Malayalam wear * salt quoted by T. Burrow, BSOAS., XI, 352) has the common Iranian na/imadka (Sogdica, 8, and Add.; na/imadka cannot ed) ; a8 nmydk it occurs in M 377 R 5. In additio nd for “salty” in Parthian, sol = wal! Th
20591:loanwords in Armenian, which entered Armenian from the of Azerbaijan, prove the existence of these changes. Now the first, hr from fr, is satisfactorily
21147:As confusing as the treatment of 8r and fr is that of postvocalic =f It remains in a few words, pethaps throughout loanwords, pw «cat», pupiyk «hoopoe» (Pers. pipas), ’Swk «target» (cf. Arm. néavak?), but normally becomes -s, €. ‘ws «attention» Ows «intelligent» (Ba- + ‘ws), etc.; ef. also sry «lion» for initial
23150:changed, but did so without system and allowed adequate representa tions of current speech to stand beside antiquated forms. The Middle Persian disguise is sometimes so perfect that only an occasional Arabic word betrays the true character of the language. The word for “and”, pronounced 1, is still written ‘wd (23!), the Idafe-particle f appears as ‘yg (St) or 'y, the abstract ending -Fia -yh or singular of presents ends in -yd but was pronounced in ~dd (or perhaps ~éd), words in final -e and -d are still spelt in -g and ~'g, and this on ‘occasion even affects Arabic loan-words, e.g. jomlg—alax. Influence of Sogdian orthography may be detected in x’n'g “house” (for the expected x’ng), kten’nd “they do” (beside heennd), stos'ndg “burning”, and the like. Quite modern forms abound, e.g. 2-, in st, a'ym ‘from beside "c (and 'z) “from”, j’y or j’ “place"* (MPers, beside 'b'g, K’—ke for MPers. ka, ku, and hé, etc In metrical passages the spelling takes little notice of the form of the words required by the verse: the metre is not meant for the eye
=== TOC
 
 
 
 
ACTA IRANICA
DEUXIEME SERIE
VOLUME VI
 
                                      
SOUS LE HAUT PATRONAGE DE S.M.I. LE SHAHINSHAH ARYAMEHR
ACTA IRANICA
ENCYCLOPEDIE PERMANENTE DES ETUDES IRANIENNES FONDEE A L'OCCASION DU 2500" ANNIVERSAIRE DE LA FONDATION DE L'EMPIRE PERSE PAR CYRUS LE GRAND
 
DEUXIEME SERIE
HOMMAGES ET OPERA MINORA
Acta Iranica 15
BIBLIOTHEQUE PAHLAVI E, J. BRILL TEHERAN-LIEGE LEIDEN
HOMMAGES ET OPERA MINORA
W.B. HENNING SELECTED PAPERS
Tt
EJ. BRILL BIBLIOTHEQUE PAHLAVI LEIDEN TEHERAN-LIEGE
 
 
COMITE INTERNATIONAL
Prof. Sir Harold Bauey (Grande-Bretagne); Prof. George CaMERon (EU): §, Exe, Prof. Enrico CeRULLI (Italie); tS. Exc. Dr Tara CHAND (Inde); Prof. Henri Conny (France); Prof. Jacques DUcnesne-Guniemin (Belgique): Prof. Namio Eoas (Japon); Prof. Dr, Wilhelm
S. Edman Enzi (Turquie); Prof. Richard ErmicHausen (E-U,); Acad BG. Garunov (URSS):
Garcia Gomez (Espagne); Pr Walther Hinz (Allemagne); Prof. Yat Dr. Franz Konia (Autriche): Pr
S. Nvaexc (Suéde); Pir Husams
 
 
ns (Allemagne); Prof,
f. Roman Gwnsiaa (France); S. Exe, Prof
    
Janos HarMatra (Hongrie); Prof: Dr. a AL-Kuasnan (Egypte); S. Em. Ca Georg Monoenstieane (Norvége); tProf. Henrik
in RASHDI (Pakistan)
 
        
 
DIRECTION
Le Conseil Culture! Impérial de "ran SE. Shodjaeddin Snara, Vice-miniswe de lx Cour Impériale, Directeur dela Bibliotheque Pahlavi
REDACTEUR EN CHEF
1. Due Pierre Lecoa, assistant Universite d
SNE-GUILLESUIN, professeur ordinaire A I'Université de Likge, assisié de
 
 
Lidge et de Jean KELLENS, assistant & Universit
 
nes Gutenberg, Mayence
 
Université de Ligge. Place 16, B 4000 Lidge
 
ISBN 90
 
 
© 1977 by Bibdlothique Pahlavi, Tehran-Liége
All rights reserved, No part of this book may be reproduced or fiche
viii permission from the’ publisher
```


## [2026-09-14T01:12:00.583Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY 2>/dev/null && ls && grep -n 'پلو\\|بت‌کده\\|بتکده' ARY_pages.txt | head -10",
 "description": "Grep Aryanpur for polow/bot"
}
```


### [2026-09-14T01:12:00.683Z] TOOL RESULT

```
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
987:حرکت ناوگان یسونان بسوی تروا بفرستند. دو مورخ کهن» لیوی (17۷9) و پلوتارکكه
1571:پپلوی (4۲7الت۸): 6,۴۳۸۷۲ ۳82۸۸ بف8 فرانسه (۳5۷)[4): لد ید ان
2007:پپلوق (۳1ماط۸م: ۰ 2۱/1020457۸ 319۸0
2075:پپلوی (1/ماتلم۳): 6 ب۸822 ,ات۶0۲۴ ,3۸86
2909:پپلوی (تماتلهم: ۰ ۸826 م۸۳ لیترانی (4۸1۸2ا 777 ): ‎٩‏ ,85
3426:پپلوی (/اماتله۳: 88۵2 ,88۸22710۸0۷ یونانی (07285/4): ۳00
3499:پپلوی (,4۲تت۸): 877۸۸۷ ,8172۸ 0 ,818۸7
3622:پپلوی (1مالهم: (۸۲۲۵185) 852 لیتوانی (۸(1۸/4ل 4 7/.): 8 و817]8
3803:پپلوی (۷/1ماللم: 8۸ ,8۸613 ,)8۸ برهمی (8074824149): 21
5312:پپلوی (/تماتنمم: ۰ ۳0۷1911۲10 ,20 نروژی (077501۸/: ۳05۸
```


## [2026-09-14T01:12:08.891Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -nE '^بت|^ *بت |^پلو|^ *پلو ' ARY_pages.txt | head -10; echo \"--- done\"; grep -c '' ARY_pages.txt",
 "description": "Grep ARY for بت/پلو headwords"
}
```


### [2026-09-14T01:12:08.963Z] TOOL RESULT

```
3663:بتوانگلیسی سرواژای اس 3088
6193:پلوچی (/7للانام8): 1 رای دا روسی (/8-5514)(شاید)
8816:پلوچی (8۸6/1): لد سوئدی (57780157)(شاید) ۸
8834:پلوچی (۸-671ه): ات ۱ سوئدی (817215/1): لا
9239:پلوچی (/007/: ۰ 338۸0 ,۸35۸617 9 (8187) :۸4200
14635:پلوچی (8۸11۳771): 1 لاتین (710مل): 0
--- done
16204
```


## [2026-09-14T01:12:09.511Z] TOOL CALL #48: WebSearch

```json
{
 "query": "Henning \"Sogdian Loan-Words in New Persian\" 1939 but \"idol\" Sogdian pwt Persian"
}
```


### [2026-09-14T01:12:16.648Z] TOOL RESULT

```
Web search results for query: "Henning "Sogdian Loan-Words in New Persian" 1939 but "idol" Sogdian pwt Persian"

Links: [{"title":"The Sogdian Sound-System and the Origins of the Uyghur Script","url":"https://dergipark.org.tr/en/pub/iutded/article/369178"},{"title":"SOGDIAN LANGUAGE ii. Loanwords in Persian - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sodgian-language-i-loanwords/"},{"title":"Sogdian Loan-words in New Persian | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sogdian-Loan-words-in-New-Persian-Henning/96f750fcd406f9dc986286dcda90e927701ea0ef"},{"title":"Bactrian Loanwords in New-Persian","url":"https://languagestudy.ihcs.ac.ir/article_451.html?lang=en"},{"title":"Sogdian Loan-words in New Persian | Bulletin of SOAS | Cambridge Core","url":"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2CE640EC43EF3DF612D3B344626E0FE6/S0041977X00068245a.pdf/sogdian-loan-words-in-new-persian.pdf"},{"title":"Sogdian Loan-words in New Persian - Walter Beresford Henning - كتب Google","url":"https://books.google.com.sa/books/about/Sogdian_Loan_words_in_New_Persian.html?id=L2ufPgAACAAJ&redir_esc=y"},{"title":"(PDF) The Myth of Sogdian Lambdacism","url":"https://www.academia.edu/35344474/The_Myth_of_Sogdian_Lambdacism"},{"title":"Buddhist Indian Loanwords in Sogdian and the ...","url":"https://er.ceres.rub.de/index.php/ER/article/download/9279/8830/7049"}]

I found several results related to your search. Here are the key findings:

W. B. Henning published "Sogdian loan-words in New Persian" in BSOS, Volume X, Issue 1, in 1939, pages 93-106.

Regarding the specific word you mentioned, Henning's work included examples such as "fuy" meaning "idol", which is a Sogdian loanword in New Persian.

The search results also reveal scholarly discussion about Sogdian loanwords in Persian. Most examples in comparative linguistic lists are first mentioned in Henning's 1939 work.

Regarding the Sogdian "pwt" you mentioned, the search results do reference related forms. Forms like "pwt" for "idol" appear in Book Pahlavi and New Persian, though the results suggest these forms may have more complex etymological origins involving Buddhist Sanskrit loanwords.

If you need more specific information about the "pwt/idol" etymology or other details from Henning's 1939 article, I can search for additional sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:12:20.069Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/sodgian-language-i-loanwords/",
 "prompt": "Does this list Persian بت but 'idol' as a Sogdian loanword? Quote what it says about but/idol and about Henning 1939's list of Sogdian loanwords in New Persian."
}
```


### [2026-09-14T01:12:21.449Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:12:21.652Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2CE640EC43EF3DF612D3B344626E0FE6/S0041977X00068245a.pdf/sogdian-loan-words-in-new-persian.pdf",
 "prompt": "What is discussed on page 94? Does the article discuss Persian but 'idol' from Sogdian pwt? Quote the relevant passage."
}
```


### [2026-09-14T01:12:27.390Z] TOOL RESULT

```
I cannot access the specific content of page 94 in this PDF document. While the file contains a scholarly article titled "Sogdian Loan-words in New Persian" by W. B. Henning from the Bulletin of the School of Oriental and African Studies, the PDF content provided is primarily raw technical data (PDF object definitions and encoded image streams) rather than readable text.

To answer your question about whether the article discusses Persian "idol" derived from Sogdian *pwt*, I would need access to the actual rendered text of page 94, which is not legibly available in the format provided.

I recommend:
- Viewing the PDF directly in a PDF reader
- Consulting an academic database with this article
- Checking university library resources for this BSOAS publication

[Binary content (application/pdf, 768.8KB) also saved to /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/webfetch-1789348344037-2so6ut.pdf]
```


## [2026-09-14T01:12:31.517Z] TOOL CALL #51: Bash

```json
{
 "command": "P=/home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/webfetch-1789348344037-2so6ut.pdf; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; mkdir -p $S; pdftotext -f 1 -l 3 \"$P\" - 2>/dev/null | head -60; echo \"=== PDFINFO\"; pdfinfo \"$P\" | head -20",
 "description": "Extract text from Henning PDF"
}
```


### [2026-09-14T01:12:32.731Z] TOOL RESULT

```
Sogdian Loan-words in New Persian
By W. B. HENNING

T T is well known what an extraordinary power of absorbing foreign
-*- words Persian possesses. In addition to the innumerable Arabic
words which since the creation of the New Persian literary language
have formed an integral part of Persian speech, we have a fair number
of Aramaic words 1 on the one hand, and of Eastern Iranian words
on the other; in later times, there is also considerable borrowing
from Turkish. It is, I think, proper to regard Eastern Iranian words
in Persian as " loan-words " in the same way as, say, Arabic or Aramaic
words; for no Eastern Iranian language is amongst the constituent
dialects of Modern Persian, which can perhaps best be defined as the
descendant of the current language of culture and commerce which
developed in Persia during the Sasanian era.
So far, little attention has been paid to the Eastern Iranian words
in Persian. Horn, in his excellent paper on the New Persian literary
language,2 quoted examples such as Balaysan, Hilmand, fits " mane ",
fay,fuy " idol ", malax " locust ", bilist " span ", loytdan " to milk ",
etc., words whose phonetic habitus does not agree with the normal
Persian development. To-day we are in a much more fortunate
position since the Sogdian language has gradually become known
to us: seen from Persia, Sogdian was by far the most important
Eastern Iranian language, a language of culture, literature, and
commerce, whose territory bordered on the area of Persian speech
and extended towards the frontiers of China. Moreover, if we consider
the important role which the Sogdian mother-country, Bukhara and
Samarkand, played in the development of early Persian literature,
we must expect a considerable number of Sogdian words to have
entered the Persian language. It may be true that several amongst
the words which I am going to mention might have been borrowed
also from some Eastern Iranian language other than Sogdian;
1

See Noldeke, Pecs. Stud., ii, pp. 34 seqq. Several additions to his collection are
possible now, e.g. liLJ " natura ", Asadi, p. 5, Sams-i Fakhrl, p. 7 (i, 4 0 ; 15 ibid.,
p. 4 = i, 10, is of course wrong), from Syriac [1 »^> kyana ; Lj^^ " square ", from
Syr. f»ii"» • = ywvia, etc.
2

Die Neupersische Schriftspmche (Grdr. Ir. Phil.), pp. 8, 14 seq., 57, 69.

Downloaded from https://www.cambridge.org/core. University of Toronto, on 14 Sep 2026 at 01:12:23, subject to the Cambridge Core terms
of use, available at https://www.cambridge.org/core/terms. https://doi.org/10.1017/S0041977X00068245

94

W. B. HENNING—

however, the historical and cultural preponderance of Sogdian makes
it a priori more likely that Sogdian was the lending language.
It is not intended to discuss at length those Persian words which
have already been recognized as Sogdian loan-words, e.g. fay, fuy
" idol " / or faypur (also baybur and fayfur) " Chinese emperor ", 2
or those Indian and Chinese words which have passed into Persian
through the medium of Sogdian, e.g. but " Buddha, idol " from Sogdian
pwt-,3 faryar " Vihara " from Sogdian firy'r 4 (beside which we have
Pers. bahdr), or *° tint " Karavanserai, Bazaar " from Sogdian tym =
Chinese Jjjj tien " inn, shop ". 5
With a number of words which are homophones in Sogdian and
=== PDFINFO
Title:           Sogdian Loan-words in New Persian
Subject:         Bulletin of the School of Oriental and African Studies
Author:          W. B. Henning
Creator:         ABBYY FineReader
Producer:        University of Toronto
CreationDate:    Wed Dec  3 12:14:50 2008 EST
ModDate:         Sun Sep 13 21:12:23 2026 EDT
Custom Metadata: no
Metadata Stream: yes
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           14
Encrypted:       no
Page size:       408.24 x 627.84 pts
Page rot:        0
File size:       787281 bytes
Optimized:       no
```


## [2026-09-14T01:12:43.645Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'PiLAU.  Mets  au  riz' in l or 'Pagode.  Du  persan' in l:\n        print('leaf',i,'printed~',i-30, repr(l[:100]))\nEOF",
 "description": "Find Devic leaf/pages"
}
```


### [2026-09-14T01:12:44.960Z] TOOL RESULT

```
leaf 215 printed~ 185 "net  e\\  alka-\nna'-.  Enfin  Bocthor  traduit  orcanète  par  Jytl\\  u=*^  hlnna al-ghoul,  ce  que "
leaf 220 printed~ 190 'on  génie,  chez  les  Orientaux,  correspondant  à nos  bonnes  fées.  Du  persan  <^jj  peri.  Nou'
```


## [2026-09-14T01:12:50.040Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/pilaf' --note 'page 409, root Pulaka, Wiktionary chain Skt pulaka > Prakrit > Hindi pulav > Persian pilaw > Ottoman Turkish > English pilaf' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/pagoda' --note 'page 409, root Pwt, pagoda < Port. pagode < Pers. butkada or Tamil pagavadi' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%AA' --note 'page 409, root Pwt, Persian بت but < MP bwt < Skt buddha' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2CE640EC43EF3DF612D3B344626E0FE6/S0041977X00068245a.pdf/sogdian-loan-words-in-new-persian.pdf' --note 'page 409, Henning SLW p.94: but Buddha, idol from Sogdian pwt-' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:12:53.626Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/39c037eb9b3a47a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94fc3e84fa3260cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5fa53052e7ca5ebf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1cb19e527f84a842.txt
```


## [2026-09-14T01:13:06.486Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('DEV.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# count formfeeds before line n\nimport itertools\ndef leafof(n):\n    txt='\\n'.join(lines[:n])\n    return txt.count('\\f')\nfor n in (1898,1931):\n    print('line',n,'leaf',leafof(n), 'printed~', leafof(n)-30, repr(lines[n-1][:90]))\nEOF",
 "description": "Compute DEV leaf for Pagode and Pilau lines"
}
```


### [2026-09-14T01:13:07.498Z] TOOL RESULT

```
line 1898 leaf 215 printed~ 185 "Pagode.  Du  persan  «<^XiL)  boutkedè  ou  jjoutkoudè,  temple d'idoles,  formé  de  oo  "
line 1931 leaf 220 printed~ 190 'PiLAU.  Mets  au  riz,  chez  les  Turcs.  Du  persan ^^j  pi- laou,  même  sens.  On  dit'
```


## [2026-09-14T01:13:13.429Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in (214,215,219,220,221):\n    l=leaves[i]\n    nums=re.findall(r'\\b1[5-9][0-9]\\b', l)\n    print('leaf',i,'nums',nums[:6])\n    print(re.sub(r'\\s+',' ',l)[:120])\nEOF",
 "description": "Find DEV printed page numbers"
}
```


### [2026-09-14T01:13:14.612Z] TOOL RESULT

```
leaf 214 nums ['180']
, alhinde, alfindo, qui signifiait autrefois acier, miroir métallique, et qui vient de l'arabe ù^] al-hind, les Hindous.
leaf 215 nums ['181', '182']
net e\ alka- na'-. Enfin Bocthor traduit orcanète par Jytl\ u=*^ hlnna al-ghoul, ce que nous rendrions par le henné du d
leaf 219 nums ['185']
ppelé les piastres esjiagnoles sur lesquelles étaient figurées les co- lonnes d'Hercule, ces colonnes représentant pour 
leaf 220 nums ['186']
on génie, chez les Orientaux, correspondant à nos bonnes fées. Du persan <^jj peri. Nous avons fait le mot du féminin. E
leaf 221 nums ['187']
ien, pour désigner toute espèce d'embarcations. Du malais yû-ï praho ou ^\yi prâo, que les Européens appliquent plus spé
```


## [2026-09-14T01:13:19.605Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in (56,57,58,159,160,161):\n    l=leaves[i]\n    nums=re.findall(r'^\\s*(\\d{1,3})\\s*$', l, re.M)\n    print('leaf',i,'standalone nums',nums[:8],'|', re.sub(r'\\s+',' ',l)[:90])\nEOF",
 "description": "Find LKT printed page numbers"
}
```


### [2026-09-14T01:13:20.977Z] TOOL RESULT

```
leaf 56 standalone nums ['30'] | erantwoi'tlich war'; hieraus rum. buluba^a, früher 'Gardehauptmann', jetzt 'Zigeunerhauptm
leaf 57 standalone nums ['31'] |  h. Stoff für Schleier]; hieraus rum. burungiuc 'Gaze', borangic 'ungezwirnte Rohseide'. 3
leaf 58 standalone nums ['32'] | um. ciobota, it. ciabatta, frz. savate, sp. zapata 'Schuh'. [Gorjajew 415. Bern SlEtWb 159
leaf 159 standalone nums ['132'] | b232. 1629. Pers. pärcäm: 'Haarlocke', ebenso tk. periem 'Haar- locke auf der Stirne'; hie
leaf 160 standalone nums ['133'] | wieback', il. pasiimata 'pasta con zoflerano e cantucci Cotta a pane, Zuckerbrot' [v^l. au
leaf 161 standalone nums [] | ze, dtsch. Bronze, Prinzmetall [mit vcjlksetymologischer Umgestallung, POTT in ZKM IV, 264
```


## [2026-09-14T01:13:33.807Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[160]\nidx=l.find('\\n133\\n')\nprint('len',len(l),'pos of 133:',idx)\nprint('--- first 200:',repr(l[:200]))\nprint('--- around:',repr(l[max(0,idx-150):idx+60]))\nl2=leaves[57]\ni2=l2.find('\\n31\\n')\nprint('leaf57 len',len(l2),'pos 31:',i2)\nprint(repr(l2[max(0,i2-150):i2+60]))\nprint('pos of 373 entry:', l2.find('373.  Pers.  batk'))\nprint('pos of 1656 entry in leaf160:', leaves[160].find('1656.  Tk.  pilaw'))\nEOF",
 "description": "Locate page numbers within LKT leaves"
}
```


### [2026-09-14T01:13:35.085Z] TOOL RESULT

```
len 4770 pos of 133: 4678
--- first 200: "wieback',  il. pasiimata  'pasta  con  zoflerano  e  cantucci Cotta  a  pane,  Zuckerbrot'  [v^l.  auch TToEn^olbi,  Jannarakis,  Deulsch-Neugr. Wörterbuch  S.  1361b].  [Miki  SlEtWb 236.    ML  6319"
--- around: "ilaw, pillaw;  russ.  jyilaw,  plow.\n1657.  Pers.  piring:\nAuch  hiring  'Kupfer'  [Horn  NpEt  S.  48, Nr.  208 bis];  hieraus  mlat.  bronzium,  it.\n133\n[Pers.  pis-ahäng.\nhronzo,  frz.  sp.  hronce,  frz.  b"
leaf57 len 4772 pos 31: 2556
'.  Ausdruck  pagoda, eugl.  pagoda,  pagode,  dtsch.  Pagode,  it. pagodo,  rum.  pagoda,  poln.  pagoda. Hierunter  versteht  man  jetzt  einen  Tem-\n31\n[Ar,  butum.\npel,  besonders  in  China  solche  von  ga'
pos of 373 entry: 1748
pos of 1656 entry in leaf160: 4379
```


## [2026-09-14T01:13:44.194Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3778,3790p' LKT.txt; echo \"=== TTS\"; grep -n -i 'pilaw\\|pilav\\|palav' incoming/TTS/TTS_pages.txt | head",
 "description": "Read LKT 1656 and grep Vambery"
}
```


### [2026-09-14T01:13:44.258Z] TOOL RESULT

```
1655.  Mal.  piknl:
'Eine  über  der  Schulter  getragene  Last' [Pijn  168],  'Gewicht',  dessen  Höhe  in den  verschiedenen  mal.  Ländern  variiert, z.  B.  in  Sumatra  60  kg;  hieraus  frz. pikoul,  engl,  pihul,  picul,  dtsch.  Pikid. [MMM  43.
1656.  Tk.  pilaw:
'Mit  Fett  abgekochter  Reis';  hieraus  in derselben  Bedeutung  rum.  pilaf,  frz.  pi- laf,  pilau;  engl,  pilau,  pillau,  pilaw, pillaw;  russ.  jyilaw,  plow.
1657.  Pers.  piring:
Auch  hiring  'Kupfer'  [Horn  NpEt  S.  48, Nr.  208 bis];  hieraus  mlat.  bronzium,  it.
133
[Pers.  pis-ahäng.
hronzo,  frz.  sp.  hronce,  frz.  bronze;  ndl. brons,  engl,  bronze,  dtsch.  Bronze, Prinzmetall  [mit  vcjlksetymologischer Umgestallung,  POTT  in  ZKM  IV,  264]; russ.  hronza,  klruss.  bronza,  öecli.  poln. bronz,  serb.  bronac;  bulg.  pernio,  serb. pirinac  'Messing'.  —  [Die  anderen  Ab- leitungen sind  weniger  wahrscheinlich:
1.  Ahd.  *brunizzo  'bräunliches  Metall' -<  dtsch.  bruno  'braun',  mlat.  brunitius.
2.  Mlat.  obryzum  sc.  aurum  =  gr.  XP'J" afov  ößpuCov  'Gold,  das  die  Feuerprobe bestanden  hat';  also  Bronze  nach  der goldenen  Farbe.  3.  Mgr.  ßpovxriaiov  < lat.  aes  brumlisium,  da  nach  Plin.  Hist. nat.  XXXIII,  9,  45;  XXXIV,  17,  40  in Brundisiuni,  heute  Brindisi,  bronzene Spiegel  hergestellt  wurden;  Etymologie von  Berthelot,  Sur  le  nom  du  bronze chez  les  alchimistes  grecs  in  Revue archeologique  1888,  S.  294.  Übrigens ist  der  Ortsname  Brundisium,  gr.  Bpcv- Tr)aiov,  nach  Strahns  Geographie  das niessapische  Woit  für  'Hirschkopf'.  In der  Tat  springt  die  Ähnlichkeit  der  Ge- stalt des  Hafens  mit  dem  Geweih  eines Hirsches  in  die  Augen ;  dazu  weist  Meyer, Essays  und  Studien  II,  311  auf  das albanesische  Wort  brin  'Geweih,  Horn' hin.]  [DozyOost26.  Kluge  70.  ML  1113. Bern  SlEtWb  87.
1658.  Pers.  pis-äliäng:
'Führer,  Zuhälter'  [aus  pers.  pes  'zuerst' Horn  NpEt  S.  79,  Nr.  356  und  ähäng. Präsensstamm  zu  ahängldän  'ziehen' ebenda  S.  14,  Nr.  58],  tk.  umgestaltet zu  pezeivenk  'dass.'  [Kelekian  Kämüs 321  b];  hieraus  rum.  pezeoenchm  'Kupp- ler', pezevenche  'Kupplerin',  pecevenclic 'Kuppelei'.
=== TTS
```


## [2026-09-14T01:13:45.544Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/pilav",
 "prompt": "What is the etymology of Turkish pilav? Quote the entry, including the Persian source form and any Sanskrit mention and first attestation date."
}
```


### [2026-09-14T01:13:48.590Z] TOOL RESULT

```
I apologize, but the web page content provided does not contain the etymology entry for "pilav." The page only shows the header and navigation elements of Nişanyan Sözlük (Nişanyan Dictionary), but not the actual dictionary entry with etymological information.

To obtain the etymology including the Persian source form, Sanskrit mention, and first attestation date, you would need to access the full entry page for "pilav" on the Nişanyan Sözlük website directly.
```


## [2026-09-14T01:13:57.124Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol3 (P)\"; grep -n -i 'pagoda' FSD_vol3.txt | head -5; echo \"=== KLN pagoda\"; grep -n -i 'pagoda' KLN_1966.txt | head -5; echo \"=== KLN pilau already\"; echo \"=== WEB\"; grep -n -i 'pagoda' WEB_vol1.txt | head -3",
 "description": "Grep FSD, KLN, WEB for pagoda"
}
```


### [2026-09-14T01:13:57.225Z] TOOL RESULT

```
=== FSD vol3 (P)
33374:word, e g , padoga lor pagoda ( < Gr metatlagi, change ]
100939:white elephant on a gold ground with a Jeweled gold pagoda
112266:Image 2. A pagoda
112276:the CJreat Pagoda, the larseMt in the world
112290:ures fancifully likened to pagodas, due to fossil nrthneeratftes ;
=== KLN pagoda
4884:Bhaga,  n.,  a  god  of  wealth  (Vedic  mythol.)  — OI.  Bhagah,  lit.  ‘allotter,  distributer,  master, lord’,  fr.  bhdjati,  ‘assigns,  allots,  apportions,  en¬ joys,  loves’,  rel.  to  Avestic  haya,  OPers.  baga, ‘master,  lord,  god’.  See  baksheesh  and  cp.  next word.  Cp.  also  pagoda.
18048:hoon,  n„  a  gold  pagoda  (coin).  —  Hind,  hiin, prob.  fr.  Canarese  honnu,  ‘gold’, hoondy,  n.  —  A  variant  of  hundi. hoop,  n.,  a  circular  band.  —  ME.  hop,  fr.  OE. hop,  rel.  to  OFris.  hop,  MDu.,  Du.  hoep,  'hoop', ON.  hop,  ‘a  small  bay’,  and  cogn.  with  Lith. kabl,  ‘hook’.  Cp.  hope,  ‘a  small  bay’. Derivative:  hoop,  tr.  v.,  to  bind  with  a  hoop, hoop,  intr.  v„  to  shout,  whoop.  —  ME.  houpen, fr.  OF.  houper,  fr.  interj.  houp,  call  to  dogs  or horses.  Cp.  whoop,  which  is  a  later  spelling of  hoop.
26936:Derivative:  paginat-ion,  n. pagoda,  n.,  a  temple  in  India  or  China.  —  Port. pagoda,  fr.  Tamil  pagavadi,  prop,  ‘house  be¬ longing  to  a  deity’,  fr.  OI.  bhagavati,  fem.  of bhagavat,  ‘blessed,  adorable,  sublime,  divine’, fr.  Bhagah,  ‘a  god  of  wealth’.  See  Bhaga. pagurian,  adj.,  pertaining  to  the  Paguridae;  n.,  a member  of  the  Paguridae.  —  See  next  word  and -ian.
38380:tee,  n.,  an  umbrella-shaped  ornament  on  the  top of  a  pagoda.  —  Fr.  Burmese  h'ti,  ‘umbrel¬ la’.
=== KLN pilau already
=== WEB
15756:ban’yăn, x. [so called (orig. by Euro: Jia allusion to a tree of this kind at Gambroon on the Persian Gulf, under which the banta: had built a pagoda.]an East Indian fig tree fri whose branches grow shoots that take
```


## [2026-09-14T01:13:58.481Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/pagoda",
 "prompt": "Quote the full etymology section of English pagoda, including Portuguese pagode, Persian butkada, Tamil/Sanskrit bhagavati, and any mention of Hindustani."
}
```


### [2026-09-14T01:14:04.598Z] TOOL RESULT

```
# Etymology of English "Pagoda"

Based on the Wiktionary entry, here's the full etymology section:

The word "pagoda" originates from Portuguese *pagode* ("Hindu temple, Hindu idol, pagoda coin"), which derives from Dravidian language words including Malayalam *പകോതി* (pakōti, "Durga temple"), Kannada, and Tamil *பகவதி* (pakavati, "Durga, Parvati"). These ultimately trace to Sanskrit *भगवती* (bhagavatī, "Holy One," used for goddesses).

**Key note on alternative theories:** The entry states that the word was "possibly corrupted under the influence of Portuguese *pagão* ('pagan')," and mentions that "Previously but mistakenly connected with various other languages from Persia to China."

However, I should note that **the provided text does not mention Persian "butkada" or Hindustani** in the English etymology section. Those terms may appear in translation sections for other languages, but they are not part of the documented etymology for the English word "pagoda" in this source.
```


## [2026-09-14T01:14:23.963Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if 'pagoda,  n.,  a  temple' in l:\n        print('KLN pagoda leaf(1-based idx0)',i)\n        nums=re.findall(r'^\\s*(11\\d\\d)\\s*$', l, re.M)\n        print('nums',nums)\nEOF\necho \"=== FSD vol3 pagoda entry\"; sed -n '112260,112280p' FSD_vol3.txt",
 "description": "KLN pagoda page; FSD pagoda entry"
}
```


### [2026-09-14T01:14:25.245Z] TOOL RESULT

```
KLN pagoda leaf(1-based idx0) 594
nums ['1113']
=== FSD vol3 pagoda entry
liooiicuvallo Bee
OPERA
pa 'go, 1 pfl'go. 2 pk'ffo,
fi (Guam ] Hume os
RALIHAUO
pa'godt»a 1. An Idol,
Image 2. A pagoda
PE*go'd», 1 p»-g5'-
de, 2 pa-g(Vda, n.
l,Arch luthu(*(mii-
tnes of the iar East,
a sacred U)W(»r, usii-
ally pyramidal in general outline, of several stones,
profusely carved or adorned, and ennnoeied with a
temple. Se« plate of architbctdue, hg 14.
Am we approach it (Rangnnnl. the moat ronapicuoua object Is
the CJreat Pagoda, the larseMt in the world
H M FuttiP Pram Egypt to Japan p 203 (a 1877 1
2> An old East*Tndian gold coin having a figure of a pa-
goda on the reverse
suh* See f oin S. A
```


## [2026-09-14T01:14:29.036Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '112280,112300p' FSD_vol3.txt",
 "description": "More FSD pagoda"
}
```


### [2026-09-14T01:14:29.104Z] TOOL RESULT

```
suh* See f oin S. A
pagodo^sleeve po*
dyt. 4t. An Oriental
Idol ( < F papodt < Hp
papoda < l*er. butkadah,
< but. Idol, 4- kadah,
temple 1 — pa-go'da •
sliH»ve*t* n Same as
n"Trhto»U.SiS?n*; »«“•<* ‘•y the Indl.
‘--“•“"y (A««»18Ue)
ures fancifully likened to pagodas, due to fossil nrthneeratftes ;
agalmatollte-p.itrM, n. Any one of several trees of a
pagudo-llkc form, as the baniaa*treeof India and the Chinese
or Japanese pagoda-tree (Sophora Japanica) . also, the West*
Indian noscgayolrev {Plumtera acuti/olia)
pa'godet, n 1. Same as paood 2. A funnel-shaped outer
sleeve turned back over an uuderslceve of lace or the like:
worn bv both sexes In the lieglnnlng of the 18th century
pa-go 'dite, 1 pe-gO'dalt, 2 pa-gO'dlt, a Mineral A soft
variety of pluite or agalmatolltn out ol which the Chinese
carve Agures of pagodas Idols, etc
```


## [2026-09-14T01:14:29.942Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=pagoda",
 "prompt": "Quote the American Heritage Dictionary etymology of pagoda."
}
```


### [2026-09-14T01:14:33.169Z] TOOL RESULT

```
# Pagoda Etymology

According to the American Heritage Dictionary, the etymology is:

"[Portuguese _pagode_, perhaps from Tamil _pagavadi_, from Sanskrit _bhagavatī_, goddess]"

The entry traces the word's origins back through Portuguese to Tamil and Sanskrit roots, with the Sanskrit term ultimately deriving from _bhagavat-_ (blessed) and _bhagaḥ_ (good fortune).
```


## [2026-09-14T01:14:55.622Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/pagoda' --note 'page 409, node 5 pagoda: Wiktionary derives from Port. pagode < Dravidian pakavati/Skt bhagavati, Persian link called mistaken' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://ahdictionary.com/word/search.html?q=pagoda' --note 'page 409, node 5 pagoda: AHD Port. pagode, perhaps Tamil pagavadi < Skt bhagavati' 2>&1 | tail -2; pdftoppm -f 409 -l 409 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg409 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg409.png",
 "description": "Archive sources and render page 409"
}
```


## [2026-09-14T01:14:57.537Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%84%D9%88",
 "prompt": "Give the Persian entry for پلو: etymology and meaning. Also any Classical Persian پلاو pilāw. Quote exactly."
}
```


### [2026-09-14T01:14:58.111Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9367b52910e7feef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2535007c823117ee.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 37449 Sep 13 21:14 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg409.png
```


### [2026-09-14T01:15:04.159Z] TOOL RESULT

```
# Persian Entry: پلو (Pilaf)

## Etymology
The word derives from Classical Persian پِلَاوْ/پَلَاوْ (pilāw/palāw), which was borrowed from Hindustani. According to the source: "borrowed from Hindustani (Hindi पुलाव (pulāv) / Urdu پُلاؤ (pulāo)), from Sauraseni Prakrit *pulāga, from Sanskrit पुलाक (pulāka, 'lump of boiled rice')."

The term is also said to have Dravidian origins, with comparisons to Kannada, Malayalam, Tamil, and Telugu words for rice dishes.

## Meaning
**پلو** (pulaw, palaw / polov, palov) is defined as: "a dish made by browning grain, typically rice, in oil and then cooking it with a seasoned broth, to which meat and/or vegetables may be added" — essentially pilaf.

## Classical Persian Form
The classical form **پِلَاوْ** (pilāw) appears in the descendants section, demonstrating how this spelling historically gave rise to numerous modern language variants across Turkish, Central Asian, Slavic, and other linguistic traditions.
```


## [2026-09-14T01:15:06.083Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg409.png"
}
```


### [2026-09-14T01:15:06.111Z] TOOL RESULT

```

```


## [2026-09-14T01:15:11.797Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T01:15:11.851Z] TOOL RESULT

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


## [2026-09-14T01:15:23.171Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 پلاو\"; grep -n 'پلاو' BQT_v1_pages.txt | head -6; echo \"=== HRN pilaw/palaw\"; grep -n -iE 'pilav|pilaw|palav|palaw' HRN.txt HUB.txt | head; echo \"=== FSD vol3 pilau\"; grep -n -iE 'pilau|pillau' FSD_vol3.txt | head -5; echo \"=== SKT pilau\"; grep -n -iE 'pilau' SKT.txt | head -3",
 "description": "Grep BQT/HRN/HUB/FSD/SKT for pilau"
}
```


### [2026-09-14T01:15:23.320Z] TOOL RESULT

```
=== BQT v1 پلاو
4482:۱- -ژیپلاوا» ۱۳۳۰ شسی.
8329:با خشکه و پلاو در عبان آن ریزند و با قاشق رو
13059:ونان را درآن تربت کنند با خشکه پلاو در آن
17565:و بیمتی خشکه پلاو هم آمده‌انت؛ وبمعنی اول
18049:پلمه » بنتح اول و ثانی» خشکه پلاو را
19053:بود که پیوسته شبها برسرراهی تشستیو زردپلاوی
=== HRN pilaw/palaw
=== FSD vol3 pilau
151935:pl-laT* n. Same as pilau. pl-lalPtt pMno't.
175462:strong bush-tea - p. and stall (Minlny), same os pillau
=== SKT pilau
```


## [2026-09-14T01:15:29.147Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '151930,151945p' FSD_vol3.txt; echo \"=== search pilau entry\"; grep -n -iE 'pers.*pilau|pilau.*pers|p.law' FSD_vol3.txt | head -8",
 "description": "Find FSD pilau entry"
}
```


### [2026-09-14T01:15:29.291Z] TOOL RESULT

```
Bcmbling ping-pong, played with tho back of the hand in-
stead of a bat.
pl'ln, 1 pril. 2 pT'ie, n pf. Conch. Circular ridges occurring
on the aboUs of ammonold oepbalopods. [PI. of L pfia,
pillar]
pl-laT* n. Same as pilau. pl-lalPtt pMno't.
pl"la*ipllMprki-plF, 2prUir|)Il',n. [P.I] 1. An embank-
ment made In rioe-flelds to assist Irrigation 2. A Pblllp-
pine tree of considerable height a Tagalog term,
pi tar, 1 iMU'ler . 2 pl'lar, a Of. pertaining to. or covered with
hair, as, the pilar muscles or erectora. [< L. pUua, hair]
pi'ia-ryf.
plf'ar-lte, 1 plFer-olt; 2 pll'ar-lt, n. Mineral An alumi-
nous variety of chrysocoUa
pl-lA8'tcr* I pi-lasTbr, 2 pi-lUs'ler, n. 1. Arch A right-
angled ooluiuuur projootxon, with catntal and base, from
=== search pilau entry
7873:an impeaohnieut. 8. £np Law. A person appointed
53362:Juluun. huluan, Palawan, cu (Hp . L A/auruii, a Mimr 1
53413:province In Palawan, one of tho Plilllpplne Islands
98644:tlip law riHiuin'N lo bo in wntiiiv
108839:Synj sec master - overseer of the pmir, a guardian of tho overman 2. Scop Law An umpire in an arbitration
119703:Palawan.
135838:femit.— pe-o'nl-B* n Bp Law A fim-soldler’s apportion-
172822:popularts Hfo populaw |
```


## [2026-09-14T01:15:33.023Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E 'pi.lau|pl.lau|pilaw' FSD_vol3.txt | head -8",
 "description": "Find FSD pilau headword"
}
```


### [2026-09-14T01:15:33.097Z] TOOL RESULT

```
98378:nobles Compare popiilaurn
151977:pl-lan't 1 pi-lau'; 2 pl-lou', n A mixed dish of boiled rice,
175462:strong bush-tea - p. and stall (Minlny), same os pillau
215038:fest admiration of apiilaud exUd
```


## [2026-09-14T01:15:34.954Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '151977,151985p' FSD_vol3.txt",
 "description": "Read FSD pilau entry"
}
```


### [2026-09-14T01:15:35.025Z] TOOL RESULT

```
pl-lan't 1 pi-lau'; 2 pl-lou', n A mixed dish of boiled rice,
raisins, spice, and some kind of meat or fowl much used
among Mohamnuxloiis lu oriental countries. (< Turk
pUaw, < Per pUdw ] pl-law't.
plleb* 1 pllCh . 2 pilch, rf . [Prov. Eng 1 To pUfer or fllch.
pUcIi, 1 pUtiU, 2 pilch, n. 1. A saddle atthout a rocker or
seat: a trade term. 2. [Prov Eng 1 (1) An Infant's diaper
cover of flannel (2) A thick apron worn by peat-diggers
St. A fur coat, any coarse garment worn for warmth I <.
```


## [2026-09-14T01:16:25.149Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%81%E0%A4%B2%E0%A4%BE%E0%A4%95",
 "prompt": "Give the Sanskrit entry पुलाक (pulāka): meanings and etymology. Quote exactly."
}
```


### [2026-09-14T01:16:31.276Z] TOOL RESULT

```
# Sanskrit Entry: पुलाक (pulāka)

## Meanings

The word has two distinct etymologies with different meanings:

**Etymology 1:** "a lump of boiled rice"

**Etymology 2:** Multiple meanings including "shriveled or blighted or empty or bad grain," "a particular species of grain," "brevity, abbreviation, compendium," and "celerity, dispatch."

## Etymology

According to the source: "Probably borrowed from Dravidian languages; compare Tamil புறுக்கல் (puṟukkal, 'coiled rice')."

Etymology 2 is described as "A post-Vedic form of पूल्य (pūlya)."
```


## [2026-09-14T01:16:39.336Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%D9%84%D9%88' --note 'page 409, node 1 entry 0: Persian پلو/پلاو borrowed from Hindustani pulav < Prakrit *pulaga < Skt pulaka' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%81%E0%A4%B2%E0%A4%BE%E0%A4%95' --note 'page 409, root Pulaka: Sanskrit pulaka a lump of boiled rice, probably Dravidian' 2>&1 | tail -2",
 "description": "Archive remaining sources"
}
```


### [2026-09-14T01:16:41.253Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8607445c04419e43.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ddb8c07b2a1efedd.txt
```


## [2026-09-14T01:22:02.041Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write409.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndata = {\n \"pdf_page\": 409,\n \"book_page\": 379,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Pulâka\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit पुलाक (pulāka) m. 'a lump/ball of boiled rice'; a second homonym means 'shrivelled, blighted grain'\",\n   \"note\": \"The root box is right in substance: Sanskrit pulāka 'a lump of boiled rice' is the accepted ultimate source of the pilaf word-family. Nourai's own citation KLN:1185 does not in fact reach Sanskrit — Klein's entry stops at 'Turk. pilaw, fr. Pers. palav' — but Hobson-Jobson p.710, which Nourai also cites on the Persian node, states the root verbatim: 'Pers. pulāo, or pilāv, Skt. pulāka, \\\"a ball of boiled rice.\\\"' Modern lexicography (Wiktionary, after Turner/CDIAL) adds that Sanskrit pulāka is itself probably a Dravidian loan (cf. Tamil puḻukku / puṟukkal 'cooked rice') and that the word reached Persian through Middle Indo-Aryan (Śaurasenī Prakrit *pulāga) and Hindustani पुलाव / پلاؤ pulāv, rather than straight from Sanskrit.\",\n   \"note_fa\": \"ریشهٔ سنسکریت «پُلاکَ» (pulāka) به معنی «گلولهٔ برنج پخته» واقعی است و همان سرچشمهٔ خانوادهٔ واژگانی پلو/pilaf به شمار می‌رود؛ هابسن‌جابسن (ص ۷۱۰) عیناً همین را می‌آورد. اما ارجاع خودِ نورایی، یعنی کلاین ص ۱۱۸۵، تا سنسکریت پیش نمی‌رود و تنها می‌گوید «ترکی pilaw از فارسی palav». ریشه‌شناسی امروزی دو نکته می‌افزاید: نخست آنکه pulāka در خود سنسکریت احتمالاً وام‌واژه‌ای دراویدی است (سنجیده با تامیلی puḻukku «برنج پخته»)، و دوم آنکه راه ورود آن به فارسی از میانِ زبان‌های هندی میانه و هندوستانی (پُلاو) گذشته است، نه مستقیم از سنسکریت. ادعای نورایی دربارهٔ ریشه درست است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%81%E0%A4%B2%E0%A4%BE%E0%A4%95\",\n    \"https://en.wiktionary.org/wiki/pilaf\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KLN:1185\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 633 (running numbers 1184/1185), s.v. 'pilau, pilaf, pilaw, n., an Oriental dish of rice boiled with meat, etc. — Turk. pilaw, fr. Pers. palav.' The page is the right one, but Klein gives no Sanskrit etymon at all, so it does not support the root box itself.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"p. 710 s.v. PILAU, PILOW, PILAF\", \"stance\": \"supports\", \"note\": \"'Pers. pulāo, or pilāv, Skt. pulāka, \\\"a ball of boiled rice.\\\" A dish, in origin purely Mahommedan, consisting of meat, or fowl, boiled along with rice and spices.' (grep '^PILAU' HJB.txt, line 17494; the next page marker reads 'PINANG, 711').\"},\n    {\"src\": \"KLN\", \"where\": \"p. 1185 s.v. pilau\", \"stance\": \"partial\", \"note\": \"only 'Turk. pilaw, fr. Pers. palav' — no Sanskrit.\"},\n    {\"src\": \"FSD\", \"where\": \"vol. III s.v. pilau\", \"stance\": \"partial\", \"note\": \"'pi-lau, n. A mixed dish of boiled rice, raisins, spice, and some kind of meat or fowl much used among Mohammedans in oriental countries. [< Turk. pilaw, < Per. pilāw]' (FSD_vol3.txt line 151977) — stops at Persian.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"polow\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP پلو polow, older/literary پلاو pilāw ~ palāw and the clipped پلا pilā, 'rice boiled and finished in fat with meat'. The dish and its name are late — there is no Middle Persian antecedent, and Horn's Grundriss and Hübschmann's Persische Studien, which cover the inherited Iranian vocabulary, both pass it over in silence. Hobson-Jobson p.710 gives exactly Nourai's arrow ('Pers. pulāo, or pilāv, Skt. pulāka'), and the earliest recipes are Indo-Persian (Āʾīn-i Akbarī, c. 1590, has a būrāna pulāo). Modern work refines the route: Sanskrit pulāka → Śaurasenī Prakrit *pulāga → Hindi पुलाव pulāv / Urdu پلاؤ pulāo → Classical Persian پلاو pilāw, i.e. the word entered Persian from Indo-Aryan in the Timurid/Mughal period rather than directly out of Sanskrit; the shift -ā- > -o- in the modern clipped form polow is the regular NP majhūl/colloquial development of final -āw > -ow (cf. کاو > گاو type, تاو > تو). Semantically the Indian 'ball of boiled rice' widened to 'rice cooked with fat and meat'. Nourai's Sanskrit→Persian arrow is therefore compatible but skips the Indo-Aryan intermediary.\",\n     \"derivation_fa\": \"واژهٔ «پلو» (صورت کهن‌تر و ادبی «پلاو»، کوتاه‌شدهٔ «پلا») در فارسی پیشینهٔ ایرانی ندارد: نه هرن در «دستور ریشه‌شناسی فارسی نو» و نه هوبشمان در «پژوهش‌های فارسی» آن را می‌آورند، زیرا وام‌واژه است. هابسن‌جابسن (ص ۷۱۰) درست همان زنجیرهٔ نورایی را می‌دهد: فارسی pulāo/pilāv از سنسکریت pulāka. پژوهش امروزی یک حلقهٔ میانی می‌افزاید: سنسکریت pulāka ← پراکریت شورسنی ‎*pulāga ← هندی/اردوی pulāv ← فارسی کلاسیک «پلاو»؛ یعنی وام‌گیری در دورهٔ تیموری–گورکانی و از راه هند بوده است. تبدیل «پلاو» به «پلو» در فارسی نو دگرگونی آوایی منظمِ ‎-āw > -ow است. معین نیز «پلو [= پلاو - پلا]» را با همین صورت‌ها ضبط کرده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%BE%D9%84%D9%88\",\n      \"https://en.wiktionary.org/wiki/pilaf\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1185\", \"status\": \"partial\", \"note\": \"Klein p.1185 s.v. pilau: 'Turk. pilaw, fr. Pers. palav' — confirms that the Persian word is the source of the Turkish one, but says nothing about where Persian got it.\"},\n      {\"ref\": \"HJB:710\", \"status\": \"supports\", \"note\": \"Hobson-Jobson p.710: 'Pers. pulāo, or pilāv, Skt. pulāka, \\\"a ball of boiled rice\\\"' — Nourai's arrow verbatim.\"},\n      {\"ref\": \"MON:810\", \"status\": \"partial\", \"note\": \"Mo'in's lexicon does carry the headword in exactly Nourai's shape — 'پلو: polow [- پلاو - پلا] (ا.) غذایی که با برنج جوشیده شده در آب تهیه کنند و با کره یا روغن به انضمام اغذیهٔ گوشتی دیگر ... صرف می‌شود؛ پلاو' (MON_part1.txt line 32559) — but Mo'in gives no origin tag here, and the 6-vol. pagination cannot be checked from the online/OCR copies, so p.810 itself is unverified.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. پلو\", \"stance\": \"partial\", \"note\": \"'پلو: [- پلاو - پلا] (ا.) غذایی که با برنج جوشیده شده در آب تهیه کنند...' — the three variants of Nourai's box, but no etymology.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 1, s.v. پلمه and بتولک (grep 'پلاو' BQT_v1_pages.txt lines 17565, 18049)\", \"stance\": \"supports\", \"note\": \"Borhan-e Qate' knows the word only in the form پلاو: 'پلمه، بفتح اول و ثانی، خشکه پلاو را [گویند]' — i.e. the 17th-c. Persian form is pilāw, as the chart's parenthesis has it.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie, whole text\", \"stance\": \"silent\", \"note\": \"grep -iE 'pilav|pilaw|palav|palaw' HRN.txt returns nothing — Horn has no entry, consistent with a late loan rather than an inherited Iranian word.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, whole text\", \"stance\": \"silent\", \"note\": \"same grep on HUB.txt: no hit.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Turkish\",\n     \"words\": \"pilâw\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Ottoman Turkish پلاو pilāw (modern Turkish pilav) 'rice cooked in fat' is a straightforward borrowing of Persian پلاو pilāw, taken over with the Persian vowels intact and only later shifting to the Turkish stem pilav-. Klein p.1185 states the direction explicitly ('Turk. pilaw, fr. Pers. palav'), and Funk & Wagnalls repeats it ('[< Turk. pilaw, < Per. pilāw]'); Devic p.186 likewise makes the Persian word primary and calls pilaf 'la pron. turque'. Lokotsch no. 1656 (p.132) heads the entry simply 'Tk. pilaw' because his dictionary classifies European orientalisms by their immediate donor, not by ultimate origin.\",\n     \"derivation_fa\": \"ترکی عثمانی «پلاو» (pilāw، ترکی امروز pilav) وام‌واژه‌ای است مستقیم از فارسی «پلاو»، با حفظ واکه‌های فارسی؛ تنها بعدها ستاک ترکی pilav- شکل گرفت. کلاین (ص ۱۱۸۵) جهت وام‌گیری را صریح می‌گوید: «ترکی pilaw از فارسی palav»؛ فانک و واگنالز نیز همین را تکرار می‌کند. دُویک (ص ۱۸۶) هم واژهٔ فارسی را اصل می‌داند و pilaf را «تلفظ ترکی» می‌خواند. لوکوچ (شمارهٔ ۱۶۵۶) مدخل را «تُرکی pilaw» عنوان کرده، زیرا فرهنگ او واژه‌های اروپایی را بر پایهٔ واسطهٔ بی‌واسطه رده‌بندی می‌کند نه سرچشمهٔ نهایی. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/pilaf\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1185\", \"status\": \"supports\", \"note\": \"'pilau, pilaf, pilaw, n., an Oriental dish of rice boiled with meat, etc. — Turk. pilaw, fr. Pers. palav.' (KLN_1966.txt line 28812, leaf 633 = pp.1184/1185).\"},\n      {\"ref\": \"DEV:186\", \"status\": \"supports\", \"note\": \"Devic p.186 (DEV.txt line 1931; leaf 220 carries the printed numeral 186): 'PILAU. Mets au riz, chez les Turcs. Du persan pilaou, même sens. On dit aussi pilaf, d'après la pron. turque.' — Persian word, Turkish pronunciation.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1656, p. 132\", \"stance\": \"partial\", \"note\": \"'1656. Tk. pilaw: \\\"Mit Fett abgekochter Reis\\\"; hieraus in derselben Bedeutung rum. pilaf, frz. pilaf, pilau; engl. pilau, pillau, pilaw, pillaw; russ. pilaw, plow.' Lokotsch takes Turkish as the donor of the European forms but does not trace the Turkish word back to Persian.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III s.v. pilau\", \"stance\": \"supports\", \"note\": \"'[< Turk. pilaw, < Per. pilāw]' (FSD_vol3.txt line 151980).\"},\n      {\"src\": \"TTS\", \"where\": \"Vámbéry, Etym. Wb. der turko-tatarischen Sprachen\", \"stance\": \"silent\", \"note\": \"grep -i 'pilaw|pilav|palav' incoming/TTS/TTS_pages.txt returns nothing — Vámbéry has no entry, as expected for a non-Turkic word.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"pilau, pilaf, pilaff\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English pilau (1610s) comes from Ottoman Turkish pilāw, picked up by English travellers in the Levant and Mughal India: Terry in Purchas (1616) 'they boil pieces of flesh or hens ... in their rice, which dish they call pillaw', then pelo (Herbert, c.1630), pelau (Bernier 1660), pallow (Fryer 1673), pilaw (Evelyn 1682), pullao (Tipu's Select Letters 1793), pilaus (Byron, Don Juan v.47), pillau (Thackeray 1848) — Hobson-Jobson's dossier on p.710. The doublet pilaf/pilaff is the same Turkish word taken in with the devoiced final of Turkish pilav/pilaf, reinforced in the 20th century by Modern Turkish and by Greek/Balkan pilafi. Klein and Funk & Wagnalls both give 'Turk. pilaw' as the immediate source, so the chart's Turkish→English arrow is exactly the standard account.\",\n     \"derivation_fa\": \"انگلیسی pilau (از حدود ۱۶۱۰ م.) وام‌واژه‌ای است از ترکی عثمانی pilāw که سیاحان انگلیسی در شام و هندِ گورکانی با آن آشنا شدند؛ هابسن‌جابسن (ص ۷۱۰) زنجیرهٔ شواهد را می‌آورد: pillaw (تری، ۱۶۱۶)، pelo (هربرت، ۱۶۳۰)، pallow (فرایر، ۱۶۷۳)، pilaw (اِولین، ۱۶۸۲)، pullao (۱۷۹۳)، pillau (تاکری، ۱۸۴۸). صورت دوگانهٔ pilaf/pilaff همان واژه است با پایانهٔ بی‌واکِ ترکی pilav/pilaf که در سدهٔ بیستم از راه ترکی امروز و یونانی/بالکانی تقویت شد. کلاین و فانک و واگنالز هر دو منبع بی‌واسطه را «ترکی pilaw» می‌دانند؛ پس پیکان ترکی ← انگلیسیِ نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/pilaf\"],\n     \"ref_check\": [\n      {\"ref\": \"LKT:132\", \"status\": \"supports\", \"note\": \"Lokotsch no. 1656 stands on printed p.132 (LKT.txt leaf 160, whose page numeral '133' falls after the entry): 'Tk. pilaw ... hieraus ... engl. pilau, pillau, pilaw, pillaw' — the English forms derived from Turkish, exactly the chart's arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1185 s.v. pilau, pilaf, pilaw\", \"stance\": \"supports\", \"note\": \"'an Oriental dish of rice boiled with meat, etc. — Turk. pilaw, fr. Pers. palav'; also 'pilaf, n. — See pilau' and 'pilaw, n. — See pilau', covering all three of Nourai's spellings.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III s.v. pilau / pilaf\", \"stance\": \"supports\", \"note\": \"'pi-laf, n. Same as pilau' (line 151935) and 'pilau ... [< Turk. pilaw, < Per. pilāw]' (line 151980).\"},\n      {\"src\": \"HJB\", \"where\": \"pp. 710-711 s.v. PILAU, PILOW, PILAF\", \"stance\": \"supports\", \"note\": \"gives the English attestations from 1616 on and the Persian/Sanskrit etymology.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"French\",\n     \"words\": \"pilau\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"French pilau (also pilaf, 19th c.) is a table-word of the Ottoman Levant, taken into French from the same Eastern source as the English word. The chart routes it through Turkish, and that is what Lokotsch no. 1656 says ('hieraus ... frz. pilaf, pilau'). Nourai's own citation, however, says something slightly different: Devic p.186 derives French pilau directly 'du persan pilaou, même sens', and treats the variant pilaf as merely reflecting 'la pron. turque' — i.e. for Devic only the -f form is Turkish-mediated. Both accounts are compatible in practice (the word reached French through Ottoman usage, whether the transmitters heard it as Persian or as Turkish), so the arrow is acceptable but not identical to the source Nourai cites for it.\",\n     \"derivation_fa\": \"فرانسوی pilau (و گونهٔ pilaf در سدهٔ نوزدهم) واژه‌ای است که از راه خوان و سفرنامه‌های عثمانی به فرانسه رسیده است. نورایی آن را از ترکی می‌گیرد و لوکوچ (شمارهٔ ۱۶۵۶) نیز همین را می‌گوید: «از این [ترکی pilaw] ... فرانسوی pilaf، pilau». اما مأخذی که خود نورایی آورده، یعنی دُویک ص ۱۸۶، آن را مستقیماً «از فارسی pilaou» می‌داند و تنها گونهٔ pilaf را بازتاب «تلفظ ترکی» می‌شمارد. این دو روایت عملاً ناسازگار نیستند (واژه از رهگذر کاربرد عثمانی به فرانسه رسیده)، ولی پیکانِ ترکی ← فرانسوی همان چیزی نیست که ارجاعِ ذکرشده می‌گوید؛ پس با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/pilaf\"],\n     \"ref_check\": [\n      {\"ref\": \"DEV:186\", \"status\": \"partial\", \"note\": \"Devic p.186: 'PILAU. Mets au riz, chez les Turcs. Du persan pilaou, même sens. On dit aussi pilaf, d'après la pron. turque.' — the reference is on the right page and has the right word, but derives French pilau from Persian, not from Turkish.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1656, p. 132\", \"stance\": \"supports\", \"note\": \"'Tk. pilaw ... hieraus in derselben Bedeutung rum. pilaf, frz. pilaf, pilau' — Lokotsch does route the French forms through Turkish.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1185 s.v. pilau\", \"stance\": \"silent\", \"note\": \"Klein treats only the English word and its Turkish/Persian source; no French link.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Pwt\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sogdian pwt- /but/ 'Buddha' (Buddhist, Manichaean and Christian Sogdian), extended to 'idol' in Islamic-period usage\",\n   \"note\": \"Both of Nourai's citations check out. Gharib's Sogdian dictionary p.332 has entries 8238-8239 'pwt M / pwt-' glossed 'Buddha', with the paradigm pwty, acc. pwtw, voc. pwt', pl. pwt(y)yst. Henning, 'Sogdian Loan-words in New Persian', BSOS 10/1 (1939) p.94, is the source of the chart's remark about a Chinese/Indian root: 'those Indian and Chinese words which have passed into Persian through the medium of Sogdian, e.g. but \\\"Buddha, idol\\\" from Sogdian pwt-, farxār \\\"Vihāra\\\" from Sogdian βrγ'r ..., or tīm \\\"Karavanserai\\\" from Sogdian tym = Chinese tien.' Strictly, but- is in Henning's Indian group (ultimately Sanskrit बुद्ध buddha, through a Gāndhārī/Central Asian form budh-); only tīm in that sentence is Chinese, so 'Chinese / Indian root' is a loose paraphrase of Henning's heading, not a claim that the word is Chinese.\",\n   \"note_fa\": \"هر دو ارجاع نورایی درست است. فرهنگ سغدی قریب (ص ۳۳۲، مدخل‌های ۸۲۳۸–۸۲۳۹) صورت pwt- را با معنی «بودا» و صرف pwty، مفعولی pwtw، ندایی pwt' و جمع pwt(y)yst ثبت کرده است. هنینگ در مقالهٔ «وام‌واژه‌های سغدی در فارسی نو» (BSOS، ۱۰/۱، ۱۹۳۹، ص ۹۴) می‌نویسد که واژه‌های هندی و چینی‌ای هستند که «به میانجی سغدی» به فارسی رسیده‌اند، از جمله but «بودا، بت» از سغدی pwt-. پس یادداشت کتاب دربارهٔ «ریشهٔ چینی/هندی» برگردانی آزاد از همان جملهٔ هنینگ است؛ دقیق‌تر آنکه but در دستهٔ هندی جای می‌گیرد (سرانجام از سنسکریت بودا buddha، از راه صورت گاندهاری/آسیای میانه)، و در آن جمله تنها tīm چینی است.\",\n   \"sources\": [\n    \"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2CE640EC43EF3DF612D3B344626E0FE6/S0041977X00068245a.pdf/sogdian-loan-words-in-new-persian.pdf\",\n    \"https://en.wiktionary.org/wiki/%D8%A8%D8%AA\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"SOD:332\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 399, whose running head is '332': '8238 pwt M ... 8239 pwt-' with gloss 'Buddha' and 'pwty; acc. pwtw', voc. pwt', pl. pwt(})yst'', GMS 36, 44'. Nourai's SOD number is a page here, not an entry number.\"},\n    {\"ref\": \"SLW:94\", \"status\": \"supports\", \"note\": \"Henning, BSOS 10.1 (1939), p.94 (the printed page number appears in the Cambridge Core scan immediately before the passage): '... those Indian and Chinese words which have passed into Persian through the medium of Sogdian, e.g. but \\\"Buddha, idol\\\" from Sogdian pwt-'. Exactly the chart's root and its note. Not in the local HENNING_selected_papers.txt, which is Selected Papers II; fetched from Cambridge Core instead.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"p. 22\", \"stance\": \"supports\", \"note\": \"MacKenzie: '*but [bwt' | = M, N ~] Buddha; idol' — the same word in Middle Persian (attested in Manichaean MP and NP; the asterisk marks the Book Pahlavi spelling as reconstructed). English-Pahlavi index p.~1107: 'Buddha but'; p.~2354: 'idol but, uzdēs'.\"},\n    {\"src\": \"SOD\", \"where\": \"p. 332, nos. 8238-8243\", \"stance\": \"supports\", \"note\": \"besides pwt- 'Buddha' the page has the compounds pwt'ks'ytr (© < Skt.) and pwt'k't'k, showing the Buddhist-Sanskrit stratum the word belongs to.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"bôt\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian but (written bwt'), 'Buddha; idol'. The word is a Buddhist-missionary term that entered Western Iranian from the Buddhist East — Gāndhārī budh- / Bactrian βοδδο / Sogdian pwt- — where Sanskrit buddha 'the Awakened One' had already lost its final -a and shortened; Iranian rendered the Indian aspirate dh as plain d/t, whence but. It is well attested in Manichaean Middle Persian (bwt) and stands in MacKenzie's Concise Pahlavi Dictionary p.22 as '*but [bwt'] Buddha; idol'. The semantic step 'Buddha' → 'idol, statue of a god' happened already in Iranian Central Asia, where images of the Buddha were the idols Zoroastrians and later Muslims saw. Nourai's transcription bôt is the older Iranist notation for the long vowel of but/bōt; the length is genuine (NP بُت but with short u is the later Persian development).\",\n     \"derivation_fa\": \"فارسی میانه but (نوشتهٔ bwt')، «بودا؛ بت». این واژه اصطلاحی بودایی است که از شرق ایرانی به ایرانی غربی راه یافته است: گاندهاری budh-، بلخی βοδδο، سغدی pwt-؛ در همهٔ اینها «بُدّهَ»ی سنسکریت (buddha «بیدارشده») پایانهٔ -a را از دست داده و همخوان دمیدهٔ dh در ایرانی به d/t بدل شده است. مکنزی در «فرهنگ کوچک پهلوی» (ص ۲۲) آن را چنین ثبت کرده است: «*but [bwt'] Buddha; idol»؛ در فارسی میانهٔ مانوی نیز bwt گواهی شده است. تحول معنایی «بودا» ← «بت، پیکرهٔ معبود» در همان آسیای میانه رخ داده، جایی که پیکره‌های بودا برای زردشتیان و سپس مسلمانان نمونهٔ «بت» بودند. ضبط bôt در کتاب نویسه‌نگاری کهن‌تر همان but/bōt است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%AA\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT\", \"status\": \"partial\", \"note\": \"Nourai cites Borhan-e Qate' without a page for the Pahlavi form. The بت entry is in vol. 1 at pp. 233-234 (BQT_v1_pages.txt leaf 453): 'بت ... معبود و مسجود کافران باشد که به عربی صنم خوانند و کنایه از معشوق هم هست' — the meaning matches, but this OCR of the Amir Kabir scan drops Mo'in's numbered etymological footnotes, so no Pahlavi form could be read from it; there is no page-level scan of BQT p.234 in the local library (tools/ref_page.py BQT:234 reports 'no scan covers printed page 234').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 22 s.v. but\", \"stance\": \"supports\", \"note\": \"'*but [bwt' | = M, N ~] Buddha; idol' — MacKenzie's '= M' means the form is directly attested in Manichaean Middle Persian, 'N ~' that New Persian has the same shape.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary\", \"stance\": \"silent\", \"note\": \"grep '^but|bwt' NYB_vol2_glossary.txt finds only būtan 'to be', būtak, hambūtan etc.; Nyberg's word for 'idol' in the Zoroastrian texts he glosses is uzdēs (p. 3870 'uzdēs [ʾwzdys] idol') — his corpus simply has no Buddhist but.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"bot; bot-kadeh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP بُت bot 'idol' continues MP but with the regular NP shortening of the vowel, and by the 10th-11th century it had also acquired the poetic sense 'beautiful one, beloved' (Ferdowsī; whence بت‌پرست bot-parast 'idolater'). بتکده bot-kadeh 'idol-temple' is bot + the productive place-suffix -kadeh (MP kadag 'house', from OIr. *kata-, cf. Av. kata- 'chamber'), the same formation as میکده, آتشکده; the synonym بتخانه bot-xāneh, which the chart puts in parentheses, uses Persian xāne instead. Bartholomae showed that -kadag marks the place where something is permanently kept (cited by Lokotsch no. 373). The NOTE 'See Bheu 3 for another possible root' points at the old attempt to attach bot to the PIE root *bheuH- 'to be, grow' (via Av. Būiti-, the name of a demon, Vd. 19.1): that is Horn's suggestion (Grundriss no. 182, p. 42, 'aw. Būiti- N. pr.; phlv. Būt, Būtjān ... wenn die Zusammenstellung richtig ist'), already reported as one of two options by Hübschmann (p.26: 'nach Fr. Müller = Buddha, nach Horn ~ zd. būiti \\\"Name eines Dämons\\\"'). Modern scholarship has dropped the Būiti- connection and takes the Buddha etymology as certain; the chart's main line is therefore the right one.\",\n     \"derivation_fa\": \"«بُت» در فارسی نو دنبالهٔ but فارسی میانه است با کوتاه‌شدن قاعده‌مندِ واکه، و از سدهٔ چهارم–پنجم هجری معنای شاعرانهٔ «زیبارو، معشوق» را نیز یافته است (شاهنامه)، از همین‌جاست «بت‌پرست». «بتکده» ترکیب «بت» است با پسوند مکانِ زایای «-کده» (فارسی میانه kadag «خانه»، از ایرانی باستان ‎*kata-، اوستایی kata- «اتاق»)، همانند «میکده» و «آتشکده»؛ مترادف آن «بتخانه» است که در پرانتز نمودار آمده. بارتولومه نشان داده که ‎-kadag جای نگهداری همیشگی چیزی را می‌رساند (به نقل لوکوچ، شمارهٔ ۳۷۳). یادداشت «Bheu 3» به کوشش کهنه‌ای اشاره دارد که «بت» را به ریشهٔ هندواروپایی ‎*bheuH- «بودن، بالیدن» و به اوستایی Būiti- (نام دیوی در وندیداد ۱۹٫۱) می‌بست؛ این پیشنهاد از آنِ هرن است (شمارهٔ ۱۸۲، ص ۴۲) و هوبشمان (ص ۲۶) آن را در کنار نظر فریدریش مولر («= بودا») می‌آورد. ریشه‌شناسی امروزی پیوند با Būiti- را رها کرده و اشتقاق از «بودا» را قطعی می‌داند؛ پس خط اصلی نمودار درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%AA\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:472\", \"status\": \"partial\", \"note\": \"Mo'in s.v. بت: 'بت. ۱ نام دیوی است که مردم را به بت‌پرستی وا می‌دارد؛ یا - بد - بودا. (ا.) پیکری که از سنگ یا چوب یا فلز به شکل انسان یا حیوان سازند و آن را پرستش کنند؛ بغ، صنم. معشوق، محبوب؛ ج. بتان.' (MON_part1.txt line 21180) — Mo'in gives both the demon and the Buddha etymology, and s.v. بتکده: '(امر.) بتخانه، بتستان'. The 6-vol. pagination cannot be verified from the online/OCR copies, so p.472 itself stays unchecked.\"},\n      {\"ref\": \"BQT:234\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 1, pp. 233-234 (BQT_v1_pages.txt leaves 453-454): 'بت ... معبود و مسجود کافران باشد که به عربی صنم خوانند و کنایه از معشوق هم هست' — headword, meaning and the 'beloved' sense as the chart has them; the page number is right.\"},\n      {\"ref\": \"SLW:94\", \"status\": \"supports\", \"note\": \"Henning p.94: 'but \\\"Buddha, idol\\\" from Sogdian pwt-' — this is the New Persian word, so the reference supports precisely this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 182, p. 42\", \"stance\": \"contradicts\", \"note\": \"'182. but \\\"Götzenbild; Liebchen.\\\" aw. Būiti- N. pr.; phlv. Būt, Būtjān (Gemme...). Wenn die Zusammenstellung richtig ist, so gehört np. but in dieselbe Kategorie wie gētī, ātaš, petyāre u.a.m.' — Horn proposes the Avestan demon-name Būiti-, not Buddha; this is the 'Bheu 3' alternative the chart's NOTE refers to, and it is no longer accepted.\"},\n      {\"src\": \"HUB\", \"where\": \"no. 182, p. 26\", \"stance\": \"partial\", \"note\": \"'182. Np. but \\\"Götzenbild, Idol\\\" (afgh. LW. but) nach Fr. Müller = Buddha, nach Horn ~ zd. būiti \\\"Name eines Dämons\\\" (vd. 19,1). Beides schon im grossen Bundehesh, vgl. Darmesteter, le Zend-Avesta II, p.259.' Hübschmann records both derivations without choosing.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 373, p. 30\", \"stance\": \"supports\", \"note\": \"'373. Pers. batkädä: \\\"Götzentempel\\\" [aus pers. but \\\"Götzenbild\\\" Horn NpEt S. 42, Nr. 182 und kädä \\\"Haus\\\" ebenda S. 188, Nr. 844; käd, kädä ist in Zusammensetzungen der Ort, wo sich etwas dauernd befindet ... vgl. BARTHOLOMAE in ZfdWf VI, 354]' — exactly the chart's bot + kadeh analysis.\"},\n      {\"src\": \"MON\", \"where\": \"s.v. بت, بتخانه, بتکده, بتستان\", \"stance\": \"supports\", \"note\": \"'بتخانه: (امر.) جایی که بت‌ها را گذارند، معبد بت‌پرستان، صنم‌خانه'; 'بتکده: (امر.) بتخانه، بتستان' — both of the chart's Persian compounds are in Mo'in with the chart's glosses.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Hindustani\",\n     \"words\": \"\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"An empty pass-through box: Nourai routes the Persian compound but-kada into Portuguese through the Indo-Muslim vernacular. The word itself is real in Hindustani/Urdu (بت‌کدہ but-kada 'idol-temple', a Persian loan in the Persianate vocabulary of Mughal India, alongside but 'idol'), and the historical setting is right — the Portuguese who coined pagode from the 1500s heard their Indian vocabulary largely from the Muslim traders and interpreters of Gujarat and Malabar, which is Burnell's and Reinaud's argument in Hobson-Jobson ('but-kadah is a phrase which the Portuguese would constantly hear from the Mahommedans with whom they chiefly had to deal on their first arrival in India'). But no source actually posits a separate Hindustani stage: Skeat, Devic, Littré, Lokotsch and Funk & Wagnalls all take Portuguese pagode straight from Persian, so the box is an inference of Nourai's rather than a sourced link.\",\n     \"derivation_fa\": \"این جعبه تهی و تنها حلقهٔ میانی است: نورایی ترکیب فارسی «بتکده» را از راه زبان هندوستانی به پرتغالی می‌رساند. خودِ واژه در هندوستانی/اردو واقعی است (بت‌کدہ، وام‌واژه‌ای فارسی در واژگان فارسی‌تبارِ هند گورکانی، در کنار «بت»)، و زمینهٔ تاریخی نیز درست است: پرتغالیان که از سدهٔ دهم میلادی/شانزدهم م. واژهٔ pagode را ساختند، بیشترِ واژگان هندی خود را از بازرگانان و مترجمان مسلمان گجرات و مالابار می‌شنیدند — همان استدلال برنل و رینو در هابسن‌جابسن. با این همه، هیچ مأخذی حلقهٔ جداگانهٔ هندوستانی را نمی‌آورد؛ اسکیت، دُویک، لیتره، لوکوچ و فانک و واگنالز همگی pagode پرتغالی را یکراست از فارسی می‌گیرند. پس این حلقه استنباط نورایی است، نه پیوندی مستند؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://www.etymonline.com/word/pagoda\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no refs= in the book; nothing to check.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"pp. 652-654 s.v. PAGODA\", \"stance\": \"partial\", \"note\": \"Burnell (A.B.): 'but-kadah is a phrase which the Portuguese would constantly hear from the Mahommedans with whom they chiefly had to deal on their first arrival in India. This is the view confidently asserted by Reinaud (Mémoires sur l'Inde, 90), and is the etymology given by Littré.' — supports the Indo-Muslim transmission setting, but names no Hindustani form.\"},\n      {\"src\": \"AID\", \"where\": \"p. 233 s.v. Pagoda\", \"stance\": \"partial\", \"note\": \"Whitworth's Anglo-Indian Dictionary: 'Pagoda. [According to Webster from the Persian but, an idol, and kodak, a house; but perhaps only a corruption of [Bhagavati]]' — again Persian direct, no Hindustani stage.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Portuguese\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The Portuguese stage itself is not in doubt: Port. pagode 'Hindu temple; Hindu idol; the gold coin' is first recorded in the Indian narratives of the early 16th century (Corsali 1515, Barbosa c. 1516 — the quotations with which Hobson-Jobson disposes of the rival Chinese etymologies), and every dictionary from Skeat to Klein to the OED derives English pagoda and French pagode from it. What is disputed is where the Portuguese got it (see node 5). Skeat's Concise Etymological Dictionary states Nourai's version: 'From Port. pagode, pagoda, a pagoda ... Pers. but-kadah, an idol-temple. — [Pers.] but, idol, image; kadah, habitation. (The final Pers. letter is sometimes rendered by /h/, as in Devic's Supp. to Littré.)'\",\n     \"derivation_fa\": \"خودِ حلقهٔ پرتغالی تردیدناپذیر است: pagode پرتغالی به معنی «پرستشگاه هندو؛ بت هندو؛ سکهٔ زرین» نخستین بار در سفرنامه‌های هندِ آغاز سدهٔ شانزدهم میلادی دیده می‌شود (کورسالی ۱۵۱۵، باربوسا حدود ۱۵۱۶ — همان شواهدی که هابسن‌جابسن با آنها ریشه‌شناسی‌های چینی را رد می‌کند)، و همهٔ فرهنگ‌ها از اسکیت و کلاین تا آکسفورد، pagoda انگلیسی و pagode فرانسوی را از آن می‌گیرند. آنچه محل اختلاف است، سرچشمهٔ خودِ واژهٔ پرتغالی است (نگاه کنید به گرهٔ بعدی). اسکیت همان روایت نورایی را می‌آورد: «از پرتغالی pagode ... فارسی but-kadah «بتکده» از but «بت» و kadah «خانه»».\",\n     \"sources\": [\"https://www.etymonline.com/word/pagoda\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no refs= in the book; nothing to check.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"s.v. Pagoda (SKT.txt line 13039)\", \"stance\": \"supports\", \"note\": \"'[Pagoda,] an Indian Idol's temple. (Port. ...) From Port. pagode, pagoda, a pagoda ... Pers. but-kadah, an idol-temple. — but, idol, image; kadah, habitation.'\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1113 s.v. pagoda\", \"stance\": \"partial\", \"note\": \"'pagoda, n., a temple in India or China. — Port. pagoda, fr. Tamil pagavadi ... fr. OI. bhagavati' — Klein keeps the Portuguese stage but gives it a Dravidian, not a Persian, source.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 373, p. 30\", \"stance\": \"partial\", \"note\": \"'... hieraus ergab sich durch Kontamination mit prākṛta bhagodi \\\"göttlich, heilig\\\" ... der pg. Ausdruck pagoda, engl. pagoda, pagode, dtsch. Pagode, it. pagodo, rum. pagoda, poln. pagoda' — Portuguese as the hub, but Lokotsch needs a blend of Persian but-kada with Prakrit bhagavatī to get the form.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"pagoda\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"English pagoda 'a tiered temple-tower of India, Burma, Siam or China' (1580s, also 'idol' and 'the S. Indian gold coin') is beyond doubt Portuguese pagode; the dispute is one step further back, and the chart takes only one side of it. Nourai's own references are the old school: Skeat derives Port. pagode from Persian but-kadah; Funk & Wagnalls has '[< F. pagode < Sp. pagoda < Pers. butkadah, < but, idol, + kadah, temple]'; Whitworth (AID p.233) reports the Persian derivation 'according to Webster' but adds 'but perhaps only a corruption of [Bhagavati]'; Lokotsch (no. 373) needs a contamination of Persian batkädä with Prakrit bhagodi to produce the form; and Hobson-Jobson pp.652-654, which the chart's NOTE sends the reader to, is the locus classicus of the disagreement — Burnell defends but-kadah (with Reinaud and Littré), Yule answers that 'the resemblance between but-kadah and pagode is hardly close enough' and that Malayalam/Kannada pagōdi, pavodi (a tadbhava of Bhagavatī) 'seems to bring us very near the possible origin of pagode'. Modern reference works have gone with Yule: AHD 'Portuguese pagode, perhaps from Tamil pagavadi, from Sanskrit bhagavatī, goddess'; Klein p.1113 the same; Wiktionary derives Port. pagode from Dravidian (Malayalam പകോതി pakōti 'Durga temple', Tamil பகவதி pakavati), 'possibly corrupted under the influence of Portuguese pagão \\\"pagan\\\"', and says the word was 'previously but mistakenly connected with various other languages from Persia to China'. Only Etymonline still puts the Persian etymology first ('probably from a corruption of Persian butkada, from but \\\"idol\\\" + kada \\\"dwelling\\\"'), and offers the Tamil one as the alternative. So: the arrow is a respectable minority view, not the current consensus, and the chart states it as fact; hence disputed. The gloss 'prayer house' is also loose — pagoda in English is a temple-tower, and its two other senses (an idol; a coin) are what make the Dravidian bhagavatī account attractive.\",\n     \"derivation_fa\": \"انگلیسی pagoda «برج‌معبد طبقه‌طبقهٔ هند، برمه، سیام و چین» (از دههٔ ۱۵۸۰ م.؛ نیز به معنی «بت» و «سکهٔ زرین جنوب هند») بی‌گمان از pagode پرتغالی است؛ اختلاف یک گام عقب‌تر است و نمودار تنها یک سوی آن را می‌آورد. مأخذهای خود نورایی از مکتب کهن‌اند: اسکیت pagode پرتغالی را از «بتکدهٔ» فارسی می‌گیرد؛ فانک و واگنالز نیز همین؛ ویتورث (ص ۲۳۳) اشتقاق فارسی را «به نقل از وبستر» می‌آورد ولی می‌افزاید «شاید تنها تحریفی از Bhagavati باشد»؛ لوکوچ (شمارهٔ ۳۷۳) ناچار است آمیزش «بتکده» را با bhagodi پراکریتی فرض کند؛ و هابسن‌جابسن (ص ۶۵۲–۶۵۴) که یادداشت نمودار به آن ارجاع می‌دهد، خاستگاه همین کشمکش است: برنل از «بتکده» دفاع می‌کند و یول پاسخ می‌دهد که «شباهت but-kadah و pagode چندان نزدیک نیست» و صورت‌های مالایالمی/کنّری pagōdi، pavodi (دگرگون‌شدهٔ Bhagavatī) ما را به سرچشمهٔ محتمل نزدیک‌تر می‌کند. ریشه‌شناسی امروزی جانب یول را گرفته است: فرهنگ میراث آمریکایی «پرتغالی pagode، شاید از تامیلی pagavadi، از سنسکریت bhagavatī «الهه»»؛ کلاین (ص ۱۱۱۳) همین؛ ویکی‌واژه آن را از زبان‌های دراویدی می‌داند و پیوند با فارسی را «نادرست» می‌خواند. تنها اتیمانلاین هنوز اشتقاق فارسی را نخست می‌آورد. پس پژوهش امروزی این پیکان را رد می‌کند و به جای آن bhagavatī دراویدی/سنسکریت را می‌گذارد؛ افزون بر این، معنای «نیایشگاه» برای pagoda دقیق نیست، چون در انگلیسی «برج‌معبد» است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/pagoda\",\n      \"https://ahdictionary.com/word/search.html?q=pagoda\",\n      \"https://www.etymonline.com/word/pagoda\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"SKT:366\", \"status\": \"partial\", \"note\": \"the entry exists and says what Nourai wants — 'an Indian Idol's temple. (Port. ...) From Port. pagode, pagoda ... Pers. but-kadah, an idol-temple. — but, idol, image; kadah, habitation' (SKT.txt line 13039) — but the page number cannot be confirmed: the local 1911 Concise scan is badly column-jumbled (the entry sits on leaf 347, whose other columns run from 'repay' to 'Paean'), and in that scan the P-entries around 'papa/pope' carry printed page numbers in the 330s, not 366. Skeat's appendix list of borrowings also has 'Portuguese from Persian: pagoda, veranda(?)'.\"},\n      {\"ref\": \"LKT:30\", \"status\": \"supports\", \"note\": \"Lokotsch no. 373 begins on printed p.30 (LKT.txt leaf 57: the entry starts at offset 1748, the page numeral '31' at offset 2556): 'Pers. batkädä: \\\"Götzentempel\\\" [aus pers. but ... und kädä \\\"Haus\\\"]; hieraus ergab sich durch Kontamination mit prākṛta bhagodi ... der pg. Ausdruck pagoda, engl. pagoda, pagode ... [Zahlreiche andere Ableitungen ... sind weniger wahrscheinlich.] [Hobson-Jobson 652/657.]' — supports the Persian origin, but only as a blend with the Indic word.\"},\n      {\"ref\": \"AID:233\", \"status\": \"partial\", \"note\": \"Whitworth p.233 (AID.txt leaf 251 = printed 233): 'Pagoda. [According to Webster from the Persian but, an idol, and kodak, a house; but perhaps only a corruption of ...]' and, for the coin, 'the derivation from Bhagawati (said to be a name of Pārwati) is now generally accepted.' The page is right; the reference itself hedges and prefers Bhagavatī for the coin.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"pp. 652-654 s.v. PAGODA\", \"stance\": \"partial\", \"note\": \"'a fifth makes it a corruption of the Pers. but-kadah, \\\"idol-temple\\\" ... There can be little doubt that the origin really lies between these two. The two contributors to this book are somewhat divided on this subject.' Burnell for but-kadah, Yule for Bhagavatī/pagōdi.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1113 s.v. pagoda\", \"stance\": \"contradicts\", \"note\": \"'Port. pagoda, fr. Tamil pagavadi, prop. \\\"house belonging to a deity\\\", fr. OI. bhagavati, fem. of bhagavat, \\\"blessed, adorable, sublime, divine\\\", fr. Bhagah' — no Persian at all, in the very dictionary Nourai uses elsewhere on this page.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III s.v. pagod\", \"stance\": \"supports\", \"note\": \"'An Oriental Idol (< F. pagode < Sp. pagoda < Pers. butkadah, < but, idol, + kadah, temple)'.\"},\n      {\"src\": \"AHD\", \"where\": \"online, s.v. pagoda\", \"stance\": \"contradicts\", \"note\": \"'[Portuguese pagode, perhaps from Tamil pagavadi, from Sanskrit bhagavatī, goddess]'.\"},\n      {\"src\": \"DEV\", \"where\": \"p. 181-182 s.v. Pagode\", \"stance\": \"supports\", \"note\": \"'Pagode. Du persan boutkedè ou poutkoudè, temple d'idoles, formé de bout ou pout, idole, et de kedè ou koudè, maison.' (DEV.txt line 1898) — Devic, and after him Littré, for the Persian etymology.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-409.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write409.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-409.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 409",
 "description": "Write and validate page-409.json"
}
```


### [2026-09-14T01:22:03.562Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 9/9
node verdicts: {'plausible': 3, 'confirmed': 5, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 7, 'supports': 7, 'not_checked': 2}
books consulted: {'partial': 8, 'supports': 12, 'silent': 5, 'contradicts': 3} | by book: {'LKT': 4, 'KLN': 4, 'FSD': 3, 'HJB': 3, 'MON': 2, 'HRN': 2, 'HUB': 2, 'BQT': 1, 'TTS': 1, 'PHD': 1, 'NYB': 1, 'AID': 1, 'SKT': 1, 'AHD': 1, 'DEV': 1}
```


## [2026-09-14T01:22:23.763Z] AGENT

Page 409 (book p. 379) verified — `data/verification/page-409.json` written, `verify_check.py 409` reports 9/9 nodes, **0 PROBLEM lines**.

**Verdicts:** roots 2 confirmed; nodes 5 confirmed, 3 plausible, 1 disputed. Ref checks: 7 supports, 7 partial, 2 not_checked (the two empty pass-through boxes carry no refs).

**Disputed**
- *Pwt* → #5 English **pagoda**: chart asserts Portuguese pagode < Persian بتکده but-kada as fact. Modern standard (AHD, Klein p.1113, Wiktionary, Yule in HJB) derives it from Dravidian pakōti/pakavati < Skt. *bhagavatī*; Wiktionary calls the Persian link "mistakenly connected". Nourai's own refs are the older school (Skeat, Lokotsch, Whitworth hedges, F&W); Etymonline still leads with Persian. Genuine minority view, not consensus.

**Plausible (not disputed, but the cited ref says something else)**
- *Pulâka* → #1 Persian **polow**: HJB:710 gives Nourai's arrow verbatim, but modern work routes Skt. pulāka → Prakrit *pulāga → Hindi pulāv → Cl. Persian pilāw (i.e. borrowed from Indo-Aryan, not direct).
- #4 French **pilau**: Nourai cites DEV:186, but Devic derives French pilau "du persan pilaou" directly; only Lokotsch 1656 routes it through Turkish.
- #3 Hindustani (empty box): no source posits a Hindustani stage; every dictionary takes Portuguese straight from Persian.

**Notable ref findings**
- KLN:1185 is the right page but Klein stops at "Turk. pilaw, fr. Pers. palav" — it does **not** support the Sanskrit root box; HJB:710 does ("Skt. pulāka, 'a ball of boiled rice'").
- SLW:94 confirmed from the Cambridge Core scan: Henning, "…Indian and Chinese words which have passed into Persian through the medium of Sogdian, e.g. **but 'Buddha, idol' from Sogdian pwt-**". (Not in local HENNING_selected_papers.txt — that file is Selected Papers **II**; fetched and archived instead.)
- SOD:332 exact (Gharib leaf 399, nos. 8238–8239 pwt- "Buddha"); LKT:30 and LKT:132 both exact once the mid-leaf page numerals are used; DEV:186 and AID:233 exact; HJB:652 exact.
- SKT:366 unconfirmable: the entry text matches Nourai, but the local 1911 Concise scan is column-jumbled and puts the P-entries in the 330s.
- BQT:234 confirmed for بت (vol. 1 pp. 233–234); the bare "BQT" on the Pahlavi node stays partial — that OCR drops Mo'in's footnotes and no page scan of BQT p.234 exists locally.
- Horn no. 182 (p. 42) *contradicts*: he ties بت to Av. Būiti-, the "Bheu 3" alternative the chart's NOTE flags; Hübschmann p. 26 reports both. Modern scholarship has dropped Būiti-.

**Extraction errors:** none — checked against the rendered page image; JSON matches the printed chart (words, scripts, refs, the Emād Khorāsānī couplet).
