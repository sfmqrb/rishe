# Verification process log — verify-page-495


## [2026-09-14T03:08:51.548Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 495 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-495.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-495.json. Write /home/sfmqrb/git/rishe/data/verification/page-495.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 495` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:52.579Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:53.415Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:53.433Z] TOOL RESULT

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


## [2026-09-14T03:08:53.927Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-495.txt"
}
```


### [2026-09-14T03:08:53.947Z] TOOL RESULT

```
1	=== PDF page 495 (book page 465) ===
2	--- entry 0 ---
3	ROOT Tafrîq -> redirect to F.r.q
4	--- entry 1 ---
5	ROOT Tâi -> redirect to Stâi 1
6	--- entry 2 ---
7	ROOT [Indo-European] Tâl : to grow, growth, twig, wood, a piece of wood used as a unit of length  (refs POK:1055; WLD1:705)
8	#1 (parent #0) [Latin] refs=POK:1055; ISS:88 | tâlea : a (wooden) rod
9	#2 (parent #0) [Persian] refs=ISS:88 | tâlâr «تالار» : a roof or room on top of (wooden) pillars
10	#3 (parent #0) [Armenian] refs=ISS:88 | talauar : tent
11	#4 (parent #0) [Sanskrit] refs=WLD1:705 | tâla : vine
12	--- entry 3 ---
13	ROOT [Persian] Talk : a mineral, talc, talcum powder  (refs MON:1133; BQT:509)
14	#1 (parent #0) [Arabic] refs=MON:1133; SHP:349; AHD:1312 | talq : talc
15	  #2 (parent #1) [Persian] refs=MON:2232; BQT:1358 | talq «طلق» : mica
16	  #3 (parent #1) [Middle Latin] refs=AHD:1312 | talcum
17	    #4 (parent #3) [French] refs=AHD:1312 | talc
18	      #5 (parent #4) [Persian] refs=VOP:135 | tâlk «تالک» : talcum powder
19	      #6 (parent #4) [English] refs=AHD:1312 | talc ; talcum
20	--- entry 4 ---
21	ROOT Tannŭr -> redirect to Tanŭr
22	
```


## [2026-09-14T03:08:55.598Z] AGENT

I'll read the source JSON and the reference index.


## [2026-09-14T03:08:56.950Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-495.json",
 "description": "Read source JSON page 495"
}
```


### [2026-09-14T03:08:57.024Z] TOOL RESULT

```
{
  "pdf_page": 495,
  "book_page": 465,
  "entries": [
    {
      "root": {
        "name": "Tafrîq",
        "redirect": "F.r.q"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Tâi",
        "redirect": "Stâi 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Tâl",
        "lang": "Indo-European",
        "refs": "POK:1055; WLD1:705",
        "gloss": "to grow, growth, twig, wood, a piece of wood used as a unit of length"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:1055; ISS:88",
          "words": [
            {"translit": "tâlea", "gloss": "a (wooden) rod", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Persian",
          "refs": "ISS:88",
          "words": [
            {"translit": "tâlâr", "gloss": "a roof or room on top of (wooden) pillars", "script": "تالار"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Armenian",
          "refs": "ISS:88",
          "words": [
            {"translit": "talauar", "gloss": "tent", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "WLD1:705",
          "words": [
            {"translit": "tâla", "gloss": "vine", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Talk",
        "lang": "Persian",
        "refs": "MON:1133; BQT:509",
        "gloss": "a mineral, talc, talcum powder",
        "script": "تَلک"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "MON:1133; SHP:349; AHD:1312",
          "words": [
            {"translit": "talq", "gloss": "talc", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:2232; BQT:1358",
          "words": [
            {"translit": "talq", "gloss": "mica", "script": "طلق"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Middle Latin",
          "refs": "AHD:1312",
          "words": [
            {"translit": "talcum", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD:1312",
          "words": [
            {"translit": "talc", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "VOP:135",
          "words": [
            {"translit": "tâlk", "gloss": "talcum powder", "script": "تالک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:1312",
          "words": [
            {"translit": "talc", "gloss": null, "script": null},
            {"translit": "talcum", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Tannŭr",
        "redirect": "Tanŭr"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T03:09:00.315Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','ISS','MON','BQT','SHP','AHD','VOP','ARY','KLN','HRN','HUB','PHD','NYB','IEC','SYN','AFM','PLA','FVQ','SKT','WEB','FSD','LKT','DKS','ISS_alt_DKS']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-14T03:09:01.255Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SHP {"title": "J. T. Shipley, Dictionary of Word Origins, New York 1945", "edition_found": "1945 (lending-only)", "kind": "hathitrust_fullview+archive_restricted", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.32106001576476 (1945 ed., rightsCode pd = FULL VIEW, catalog record 001441050) ; archive.org dictionaryofword00ship and 15 others = lending only", "identifier": "dictionaryofword0000jose_n4p8 (also dictionaryofword0000jose_n6p4, dictionaryofword0000ship_d0v5)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

DKS MISSING
ISS_alt_DKS MISSING
```


## [2026-09-14T03:09:04.456Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ---; ls ocr 2>/dev/null | head"
}
```


### [2026-09-14T03:09:04.521Z] TOOL RESULT

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
---
AFM
ARY
BLY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
```


## [2026-09-14T03:09:05.050Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T03:09:05.112Z] TOOL RESULT

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
```


## [2026-09-14T03:09:19.221Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"talea\" POK_full.txt | head -30; echo \"=== POK03 ===\"; grep -n \"talea\" POK_03.txt | head -20"
}
```


### [2026-09-14T03:09:19.315Z] TOOL RESULT

```
66359:Saxon for(a)ht. Old English /oa/?/ "timorous'; Old High German Old Saxon forhtalear'; 
=== POK03 ===
```


## [2026-09-14T03:09:20.108Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"talea\\|tālea\" LEW_1910.txt LAT.txt | head -20"
}
```


### [2026-09-14T03:09:20.165Z] TOOL RESULT

```
LAT.txt:11858:tainea formes dialectalea italiennes remonteraient a *cillicare (?).
LAT.txt:36729:45,3, cum taleam demittes, pede taleam opprimito. Si parum descendet,
LAT.txt:48051:platalea, -ae) platea, -ae f.: sorte d'oiseau de ner, spatule,
LAT.txt:48052:butor, ou pdlicaa? Platalea est dans Cic., N.D.a, 194 , platea dane
LAT.txt:62777:talea, -ae (talia Gloss.) f.: rejeton, bouture; piquet, pointe.
```


## [2026-09-14T03:09:22.992Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['POK'],ensure_ascii=False,indent=1))\""
}
```


## [2026-09-14T03:09:23.623Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62770,62800p' LAT.txt"
}
```


### [2026-09-14T03:09:24.126Z] TOOL RESULT

```
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
```


### [2026-09-14T03:09:24.175Z] TOOL RESULT

```
talas(s)ius, -J et talas(s)io, —Onis m.: ancienne diyinit 4 in—
■voqude dans les 'cdrdmonies du mariage. Le sens et 1 'emploi en sont x
perdus a 1 'dpoque historique. Cf.Roscher , Lexicon, s.u.; et P.F.
479,13: Talassionem in nuptiis Varro ait signum esse lanificii.
Talassionem enim uocabant quasillum, qui alio mddo appellatur calathus,
uas utique lanificiis aptum. Cf.Funaioli, Gr. Rom.fgm., p.369, n°457.
La grAphie a-vec th- est un faux helldnisme (d 1 apros GaAoqioc?).
talea, -ae (talia Gloss.) f.: rejeton, bouture; piquet, pointe.
Ancien (Cat. ), technique. M.L.8538. Dim.: taleola (Coi.), M.L.8541.
II faut y rattacher sans doute tSlid,-dre "tailler, couper", verbe
attest£ a basse <?poque chez les gromatici, et qui est panroman,
M.L.8543, d'ob. tdliatura; intertdlidre "diuidere uel excidere ramum"
Non.414,30^
L'indo-durop^en n'admettant pas de racines de la forme *tal~, -
les rapprocbements propos<?s, qui comporteraient pareille forme radicale>
sont A 4 carter. Iis sont du reste rares et vagues pour le sens.
Terme technique, sans doute empruntd.
talentum, -I n.: talent. Emprunt ancien au gr.xaXavTov. Ddrivd:
talentdrius (Sisenna). M.L.8540. Celt.: iri .tali and.
t&llO, -Onis m. : talion, terme juridique, attestd depuis la loi
des XII Tables, cf. F.4y<», 15: talionis mentionem fieri in XII (8,a)
ait Verrius hoc modo: ”si membrum rup<s>ii, ni cum eo pacit, talio
esto". Neque id quid significet indicat, puto, quia notum est; per¬
mittit enim lex parem uindictam. Rare et technique. Non roman. Sur
tali 5 , rattachd k talis, a < 5 td fait duplis.
On a rapprochd des mota celtiques, de forme tal- (arec a bref),
notamment ▼.iri .tale "paie", gall.tolu "payer". Si 1 'dtymologie
vaut, l'o serait du k un rapprochement arec talis par dtymologie
populaire.
talipedO: y.talus.
1 * talis., -e: tel, de telle espbce, ou de telle nature. A pour
```


## [2026-09-14T03:09:30.128Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: tāl\\|lemma: tal\" POK_full.txt | head -20; echo \"=== pages ===\"; grep -n \"1055\" POK_full.txt | head -20"
}
```


### [2026-09-14T03:09:30.196Z] TOOL RESULT

```
84819:Root / lemma: tal- 
=== pages ===
84668:Page(s): 1054-1055 
84934:See also: see above S. 1013 f. under (s)teg- and S. 1055. 
87011:See also: see above S. 1055.
```


## [2026-09-14T03:09:31.465Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 288 289 290 291 292 293 294; do echo \"---- leaf $n (printed ~$((n+764))) ----\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_03.txt | head -6; done"
}
```


### [2026-09-14T03:09:32.480Z] TOOL RESULT

```
---- leaf 288 (printed ~1052) ----
hte*;  mit  ÜbertrÄ^f  il|[ tierische  russ.  osoka  ,Bluteiter',  klr.  posoJca  ,Blut  eines  Tieres'  os«   ' gjak  ,Blut'.
WP.  II  515  f.,  WH.  II  623,  Trautmann  248,  Vasmer  2,  688,
1045
^y^el^(k-), schlingen,  essen,  trinken*?  Nur  iran.  und  germ.? ^v.  x^'ar-  ^genießen,  verzehren* ;  engl,  swül  ,verschlingen,  gierig  trinken' Uüch  jSpülen',  wie  ags.  swillan,  swillian),  mnd.  swellen  ,üppig  leben',  isl. ^llr  ,Trinkgelage' ;  norw.  soll  ,Milch  mit  Brotbrocken*,  aisl.  hräsollr  ,Blut* /  ♦naßklumpiges*) ;  aisl.  sollr  , Spültrank  für  Schweine'  (welche  Bed.  auch gijo-1.  sivill  hat);
yon  einer  Erweiterung  suelk- :  ahd.  swelhan  und  swelgan  ,verschlucken, trinken',  ags.  swelgan,  aisl.  svelga,  nhd.  schwelgen-,  aisl.  svelgr  , Stromwirbel, fresser';  mnd.  mhd.  swalch  ^Schlund',  nhd.  Schwalch  ^Öffnung  des  Schmelz- ofens^  nd.  swalgen  ^ersticken';  schwed.  svalg,  svulg  , Schlund',  aisl.  sylgr ^Schluck'. '  WP.  11  530,  Specht  KZ  66,  25 f.;  vgl.  oben  S.  901  und  unten  s.  v.  uelk-.
Süd-  , schwelen,  brennen'.
---- leaf 289 (printed ~1053) ----
s.,  sweltan jt.  V.  »sterben',  mndl.  swelten,  aisl.  svelta  st.  V.  ,hungern,  sterben',  got. [tmltan  st.  V.  ,hinsterben*,  tiefstufig  got.  swulta-wairpja  ,der  sich  zum Tode  neigt',  aisl.  sultr  m.  , Hunger',  ags.  swylt  m.  ,Tod';  vielleicht  zu |lrm.  kaic-nu-m  ,hungern*,  kaic  ,Hunger*  (^*suld-sk-ö)]
Ht.  svilii,  svilti  , sengen  (intr.),  ohne  Flamme  brennen*,  Kausat.  svUinti [y»engen  (tr.)',  zem.  svtlis  ,Hitze,  Fieber',  svelti  ,schwelen*,  lett.  sveVu,  svelt jjBengen  (tr.)',  svelme  f.  ,Dampf,  Glut*,  svals  m.  ,Dampf',  svelains  ,scharf, rkalt'  (vgl.  die  Bed.  von  anord.  svalr).
WP.  II  531  f..  Scherer  Gestirnnamen  49 f.,  Trautmann  296,  Frisk  65 f.; ».  oben  S.  881  f.  sauel-.
1046  •
3.  (suel-),  suol-,  sul-  , Fußsohle,  auch  Grundlage,  Unterstes*      {]
Lat.    solea   , Schnürsohle,   Sandale^;   solum   ,Boden,   Grund  n  il^ Grundfläche,  Fußsohle*;
---- leaf 290 (printed ~1054) ----
len,  klingen,  rauschen*,  sonus  (*su>
1047
son  ,Laut*  lat.  Lw.);  wahrscheinlich  air.  senn-,  Prät.  sephainn  ,sonäre
ielen  (ein  Instrument)'^  das  nn  wohl  nach  to-senn-  ^verfolgen',  das  (aus
'^em-d-ne-  entstanden)  zur  Wz.  suem-  gehört;  air.  senim  (d.  i.  seinm)  ,das
§pielen;   Tönen';   ags.   swinsian    ,singen,    Musik    machen',    swinn    ,Musik,
---- leaf 291 (printed ~1055) ----
en' (?),  ags.  swengan  ,sich  schwingen',  mhd.  swanc,  swunc
ib)   , schwingende    Bewegung,    Schwang,    Schwung' ;    mnd.    mhd.   swengel
Schwengel';   aisl.    svangr   ,dünn,    schmal',   mhd.   swanger   ,schlank';    aisl.
tangi  m.  ,die  Leisten,  Weichen'  (,Einbiegung') ;
nasallos:  norw.  svaga,  svagra  »schwanken,  schlenkern',  sva^r^o  ,schwan-
Bnd  gehen',   aisl.   sveggja   ,(ein    Schiff)   wenden';    mnd.    swak   ,biegsam.
---- leaf 292 (printed ~1056) ----
 Kaus.  aisl.  IS^^t«  , schläfern,  stillen,  besänftigen',  ags.  swefian  ds.,  ags.  swehban  ,einsf töten*,    as.    answebbiarij   ahd.    antswebben,   mhd.    entsweben  ds.,  mb , schläfrig  werden,  einschlafen'  (*swopeiö);  aisl.  sefa  ,töten*  i*tU^k^jji  t«»^ sucefa  ,einschläfern*  {*suepeiö),  syfja  unpers.  ,schläfrig  machen'i^wrtÄUf sufien  ,schläfrig  werden'  (ndl.  suf  ,schwindlig,  dumm');  aisl.  softiaH^"^ , einschlafen* ;  mhd.   swep,  -bes  ,Schlaf',  ags.  sioeofot  n.   ds.;  alm. Iter.  sypati  ,schlafen*,  us^nqt^  ,einschlaf en' ;
ai.  svdpna-  ,Schlaf,  Traum',  av.  x^'afna-  m.   ds. ;   arm.  Ttun,^^ jSchlaf  (^suopnos)]  gr.  ^Ttvog  ,Schlaf'  (=  aksl.  s^n^  und:)  alb." somnus  ,Schlaf'  (*suepno8  oder  *su(ypnos) ;  air.  süan,  cymr.  com.  br^ , Schlaf  (*sopnos  =  lit.   säpnas)]  aisl.  sve/n,  ags.  swefn  ,Schlar, (aus  *suepnös) ;  lit.  säpnas,  sapnys  ,Traum*,  lett.  sapnis  ,Trauin'j  %s^m^  ' ,Schlaf,  Traum* ;  vgl.  ai.  asvapna-  ,schlaflos*,  av.  ax^afna-  ds.,  lat  nw««* gr.  UvTtvog  ds.  und  die  lo- Ableitung  ai.  svdjpnyam  ,Traumgesicbt ,  u*
I
1049
t0  ,TraumS  zem.  sapnis  ,Schlaf,  Traum',  aksl.  s^nije  ,Traumgesicht';  gr. Hov  (nachgebildet  lat.  insomnium)  ds.,  cymr.  anhunedd  ,insoinnia*;  toch. ^^9^  B  ?P^'^^  ,Schlaf,  Traum^;  hitt.  sup-  (Medium),  suppariia-  ^schlafen'. Vf.  II  ^^^^''  ^H-  II  öö'^^v  Trautmann  292  f.,  Vasmer  2,  694.
'g^ep-,  sup-,  sueb-  _,werfen,  schleudern,  schüttend ^i.  ^apü  ,Besen';  aksl.  svepiti  se  ,agitari';  schwundstuf,  s^pg,  suti  ^schütten, juenS   Iter.   sypati  ,schütten',   rasypati  »ausstreuen' ;   sunqti  ,effundere',
---- leaf 293 (printed ~1057) ----
.   sveria,  ags.   as.   siceriarij  ahd.   sicerierij  swerren  ds.,   aisl.
Nom.  PL  , Schwur,  Eid',  mhd.  siouor  , Schwur',  aisl.  svara  ,anworten, rgschaft  leisten',  svqr  PI.  ,Antwort',  and-svar  ^gerichtliche  Entscheidung',
and-swaru  , Antwort',  as.  aw^stcör , Antwort,  Verantwortung';  aksl.  svarb
k*(Hin-  und  Widerrede),  svar^  , Kampf,  svariti  , schmähen,  bekämpfen';
,  ssora  ,Zank'  aus  *s^sora?
tuer-  , sprechen,   reden'  ist  vielleicht  (aber  nicht  sicher)  eine  Anwen-
---- leaf 294 (printed ~1058) ----
uer-uo-)j  ursprüngl.  wohl  ,' stechend' ;  cymr.  chwarren  f.  , Drüse'  (*suorsina) ;  .,
ahd.   sioeran   st.  V.  ^schmerzen,  schwären,  schwellen',   swero  ,! Schmerz,  bes.  Geschwür',  nhd.  Schioäre,  Geschivür,  ahd.  swer(a)do Schmerz',  ags.  sioeornian  ,gerinnen';  ahd.  sivei^t  ,Schwert^,  ags. sverd  aus  *swe)^-da-  ,stechende  Waffe';  -p
urslav.  *suara-  ,kränklich'  in  russ.  chvöryj,  acech.  chvory,  ahlauf  ' ds.  und  ksl.  chyra  , Gebrechlichkeit' ;  vielleicht  hierher  serb.-ksl^ ,Bohrer',  urslav.  *svhrdhlo.
WP.  II  52y,  Trautmann  295,  Krogmann  KZ.  59,  204,  VasmegS 3,  237,  243,  Loth  RC.  41,  233.
5.  suer-  ,wägen',  suero-  ,schwer',  s.  unter  1.  uer-.
suerbb-    (auch   Suer-?)    , drehen,    drehend    wischen,    fegen';   Verl suorbhom. Cymr.  chwerfu  ,das  Wirbeln,  Umdrehen',  chwerfan  ,whirl  for  a' chwyrn    ,schnell    (drehend)'    aus    *siierbh-nio-',    got.    a/-,   hi-swai wischen',  aisl.   sverfa  st.   V.   , feilen',  svarf  n.   , Abfall   beim   Feil sweorfan  ds.,  afr.  swerva  ,kriechen',  as.  sioertan  ,abwischen',  ahd,  I ,extergere',  suuarp,  swirhil  ,gurges,  vortex',  mhd.  swerhen  ,sich*1 bewegen';  aisl.  svar/a , umherschweifen ',  aschwed.  si; an; a  ,drechsel%1 ersinnen' ;
```


## [2026-09-14T03:09:41.726Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '84810,84845p' POK_full.txt"
}
```


### [2026-09-14T03:09:41.780Z] TOOL RESULT

```
Lithuanian yoa-/c»^i/s"anstandig, comfortable ' (£UTaKTO(;) = Latvian patags^ comfortable 
', Lithuanian su-togti' s\c\\ vertragen, sich verbinden'; 

Tocharian A tassiP\. " leader '. 

References: WP. I 704, Trautmann 312, van Windekens Ant. Class. 9, 67 f. 
Page(s): 1 055 

Root / lemma: tal- 

Meaning: to grow; young animals 

Material: Gr. tqAic; -i5oc; 'junges mannbares girl, bride' rriAic;, -sux;, Ionian -\oc, f. 

"HiJIsengewachs, Bockshorn', TnAsGau) ' blossom, spriefte'; 

Latin /5/ea"Stabchen, seedling, Setzreis', dial, for *talia, as also talla= talia 
"ZwiebelhiJIse'; denominative /a/za/ie 'split, cut, clip' (originally "* branch abscise '); 

Lithuanian a(t)t6las^Hac\\\\e\x, bumper crop, byproduct', talokas^ grown, nubile, 
marriageable'. 



References: WP. I 705, WH. II 643, Mayrhofer 1 , 498. 
Page(s): 1 055 



Root / lemma: ta- ta-, tai- tai- ff-, [tau^, tau- tu- 

Meaning: to melt, dissipate, decay 

Material: A. Osset. thayun' thaw, melt' {*ta/d) = Old Church Slavic tajg, tajetb 'melt', */a/b
```


## [2026-09-14T03:09:44.934Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\" POK_03.txt | grep -n \"\" >/dev/null; python3 - <<'EOF'\nimport re\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'tal|tāl',l) and ('Weinpalme' in l or 'talea' in l or 'talauar' in l or 'wachsen' in l and 'tal' in l):\n        print('LEAF',i)\n# find the t- section\nfor i,l in enumerate(leaves):\n    if 'Weinpalme' in l or 'tälea' in l or 'talea' in l:\n        print('HIT leaf',i, l[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T03:09:46.009Z] TOOL RESULT

```
LEAF 6
LEAF 174
LEAF 298
LEAF 382
HIT leaf 298   rrjXe&dcj  , grüne,  sprieße*; lat.  tälea  ,Stäbchen,  Setzling,  Setzreis*,  dial.  für  *^ä?ia,  wie  auch  tälla  = tälia  , Zwiebelhülse';  Denominativ  täliäre  , spalten,  schneiden*  (ursprü
```


## [2026-09-14T03:09:50.213Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==298' POK_03.txt"
}
```


### [2026-09-14T03:09:51.229Z] TOOL RESULT

```
0,  Max  Förster  Themse  728  ff.  .  J
täd-  etwa  ,mit  Vorbedacht  handeln* ;  nur  gr.  und  osk.  , ,
Gr.  iTtiTTjöeq  Adv.  ,mit  Vorbedacht,  geflissentlich'  (i^rtiti^Ssiog iTtiTTjösija)  ,betreibe  geflissentlich');  osk.  tadait  ,censeat'. WP.  I  705.
%i
u
tag-  (oder  teg-  :  tog-  :  teg-)  ,berühren,  angreifen'.
Gr.  TSTaycüv  , fassend'  (:  lat.  tetigl))  lat.  tanyö,  -ere,  tetigl  tai auch  aoristisches  tagö,  -ere)  , berühren',  integer  ,unversehrt  (um tagax  , diebisch*;  taxim  ,heimlich*,  taxö,  äre  , abschätzen,  betasten] mit  -gh-  volsk.  atahus  Fut.  II  ,attigerit',  marruc.  ta[K]a  ode^ jtangat';  lat.  contaminäre  ,entweihen'  zu  contagiö  , Berührung';   '^^
1055
^ffS.  daccian  , sanft  berühren,  streicheln*,  and.  thakolön  , streicheln*;  viel-
icbt  hierher  vom    Begriffe   , streicheln,   fein  anzufühlen' :  ir.  tais  ,weich,
acht,  sanft*,  gall.   Taximagulus]
falls  air.  tongid  ,schwört^,  dl-tong-  ^verneinen*,  Perf.  do-ru-tJiethaig  (*te- ^^)  Verhalnomen  dithech  (^dl-tego-)  dazu  gehört  (zu  cymr.  tyngu  ,schwören',
jj,  to-,  mbret.  toeaff,  nbret.  toui  ds.),  ist  vielleicht  eine  idg.  Wurzel  *teg-
2usetzen,  wozu  noch  phryg.  eti-te-tik-menos  ,verflucht'  gehört;  das  gr. .  j    a   wäre    dann   Red.-Stufe,  wie   lat.   a  in  frangö  (oben   S.   165),   usw.
^VP.  I  703,  WH.  II  647  f.,  0.  Schrader  Reallexikon  s.  v.  Eid.
an  den  rechten  Platz,  ordentlich  hinstellend
Gr.  tayög  m.  , Anführer,  Befehlshaber',  tayeva),  rayiw  ^beherrsche,  führe
|tj  nachhom.  rdaffo),  att.  tccztcü,  hayiqv,  raxTog  ,auf  einen  bestimmten jten,  in  Reih  und  Glied  stellen,  beordern,  ordnen,  regeln'  (Präs.  räaaw ilog.    statt    *Tatw),    tayrj    f.    ,Schlachtordnung',    zdyfia    n.    , Heerschar;
rdnung*,  rd^ig  f.  , Ordnung;  Anordnung;  Posten,  Rang^;
abrit.  PN  Pra-su-tagus  (vorkelt.  idg.  Lw.);
lit.  pa-togiXs  ,anständig,  bequem^  («iVaxTOg)  =  lett.  patägs  , bequem*,  lit.
.tögtl  ,sich  vertragen,  sich  verbinden*;
toch.  A  täsH  PL  ,Anführer*.
WP.  I  704,  Trautmann  312,  van  Windekens  Ant.  Class.  9,  67  f.
.,  take{i)-  , schweigen'.
Lat.  taceö,  -ere  , schweigen*,  umbr.  tagez  ,tacitus',  tasetur  Nom.  PL  ,taciti';
got.  pahan  , schweigen*,  pahains  ,Schweigen',  mit  gramm.  Wechsel  ahd.
igen,  as.  thagön,  thagian  ds.,  aisl.  pegja  ds.,  pagna  ,verstummen',  pagallj ül  , schweigsam* ;
vielleicht  als  Aktiv  zu  obiger  neutropassiven  Gruppe:  air.  tachtaid fjfürgt*,  cymr.  tagu,  com.  bret.  taga  ,das  Würgen'  als  ursprüngl.  ,zum fSchweigen  bringen^;  unklar  ist  cymr.  gos-teg  f.  ,Schweigen*.
WP.  I  703,  WH.  II  641  f.
^wachsen,  grünen;  Gewächs,  junger  Trieb*.
Gr.  TäXig,  -LÖog  ,junges  mannbares  Mädchen,  Braut'  TfjXig,  -stag,  ion.  -log [t  ,Hülsengewächs,  Bockshorn*,
```


## [2026-09-14T03:10:00.061Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; grep -n \"Weinpalme\\|talea\" WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-14T03:10:00.115Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
66556:     Ai. tala-h „Weinpalme <£ , tali „ein bestimmter                               Baum“;
66562:     lat.   talea „Stabchen, Setzling, Setzreis; jedes stabformig abgeschnittene
```


## [2026-09-14T03:10:01.868Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '66520,66600p' WLD_Bd1_pages.txt"
}
```


### [2026-09-14T03:10:01.926Z] TOOL RESULT

```
                                      ;                         ;




                                                  tad           teu-                                             705

tad- etwa „mit Vorbedacht handeln".
  Gr. imzrjdeg Adv. „mit Yorbedacht, geflissentlich“ (smzt]8eiog „geeignet“,
Imzgdevco „betreibe geflissentlich"), osk. tadait „censeat“. Biieheler, Bechtel
Lex. 134. Unannehmbar iiber intrudes Bgm. Dem. 140f.

1.   tap- „eintauehen; Nasse".
  Arm. tatavem „tauche ein“, ton (*tapni-) „Feuchtigkeit, Nasse, Regen;
  abg. topiti „immergere“, to(p)nqti „immergi“, wozu u. a. nsorb. ion „Tiimpel“,
cech. tune „Vertiefung im Flusse", russ. tonga ,.geschiitzte Bucht“. Hiibsch-
mann Gr. I 448 m. Lit.; Pedersen KZ. 36, 98; Petersson KZ. 47, 275
(der mit fraglichem Rechte an j5-Erw. von ta- „schmelzen“ denkt).

2.   tap- „niederdriicken, zusammendriicken“.
     Ai.    vi-tapati       „driickt      auseinander“, sam-tapati „driickt zusammen“, np.
taftan „niederdriicken“
     gr. zemstvos           ,,niedrig,    demiitig“         („*gedriickt“) ;          aisl.   pefja       „stampfen“,
pdf n. „Gedrange“ (norw. tuv „das Walken, Filz; dicht wachsendes Gras“),
pofi    m. „FiIz“. Fick I 4 56, 223, 439, III 4 180, Falk-Torp u. tave. DaS
die ar. Worte    nach Uhlenbeck Ai. Wb. 108 eher = ai. tdpati tapyaii „er-                            ,


hitzt, qualt; ist warm, wird gequalt, leidet“, np. taftan „brennen, warmen,
leuchten“ seien, ist besonders wegen np. taftan „niederdriieken“ nicht vor-
zuziehen.              Aus nord. pofi stammt lit. tuba              ,
                                                                        lett.    tuba, apr. tubo „Filz“.        Buga
Kalba ir senove 294 f.

tal- „wachsen, griinen; Gewachs, junger Trieb“ (ahnlich mit dhal- „bliihen,
        grfinen").
     Ai. tala-h „Weinpalme <£ , tali „ein bestimmter                               Baum“;
           „junges mannbares Madchen, Braut“ (Schulze GGA. 1897, 871;
     gr. zafag
nicht zu zrjMxog, lat. tails, zw. Leumann Adj. auf -l is 20 f.), zfjhg „Hulsen-
gewachs, Bockshorn“, zyXsdduj „griine, sprieBe“ (oder dies diss. aus
                   :   '&d)da>t Bechtel      Lex. 314 f.)
     lat.   talea „Stabchen, Setzling, Setzreis; jedes stabformig abgeschnittene
Stiick“, dial, fiir *talia,wie andererseits auch talla = talia „Zwiebelhiilse“,
Denominativ taliare (germ, und romanisch) ,’,spalten, schneiden (ursprgl.                                  11



„*Zweige abschneiden“; Ernout El. dial. lat. 235);
                                                        1
   lit. a{t)tolas „Nachheu, Grummet'     talokas „erwachsen, mannbar".
                                                            ,

   Bezz.-Fick BB. 6, 238, Fick I 4 440, s. auch Prellwitz 2 u. zdhg, Boisacq
u. zahg und dzakog. — Aksl. talijs      talija „griiner Zweig" ist entlehntes
                                                        ,

gr. ftalXtov = ftaXlog, Leskien IF. 19, 207. Wohl nicht als *tal-na hierher
aisl. pqll   junger Fichtenbaum" (Fick III 4 184, Falk-Torp u. tall, tol I).
               ,




teiq- „Zuversicht haben".
  Lit. tikiii, tiketi „glauben“; nasaliert ahd. dingan mhd. dingen „hoffen,            ,


glauben, Zuversicht haben", nhd. guter Binge sein. Fick III 4 185. Anders
Buga Kalba ir s. 101.
teu- „in freundlichem Sinne jmnd. die Aufmerksamkeitzuwenden, aufmerken".
     Lat. tueor,           -erl,   tuitus   nnd   tutus         sum       „ins     Auge       fassen,     betrachten,
worauf achtgeben,                  schiitzen"   (vgl. z.        Bed.       dt.   gewahren      :   wahren ), intueor
706                                             teu-, teu-, tu-



„betrachte“, urspriinglicher in-, ob-, con-tuor con-tuo; tutus „sicher“; (aber
                                                             4
air. cumtuth „beschutzen“ nicht aus *com-ocl-tutu -, Fick II   132); air. tuatli
„link, nordlich" (aus *„giinstig, gut“, vgl. die                  Bed. yon got. piup-, die linke
```


## [2026-09-14T03:10:16.633Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tālār\\|talar\\|tālāri\\|talawar\\|taławar\\|talauar\\|tałavar\" ISS_alt_DKS.txt | head -30"
}
```


### [2026-09-14T03:10:16.687Z] TOOL RESULT

```
2558:аја ‘halls (?)', K 99:255-6 bisa prrüva ysima ttala gandye salaba ysini námda їуе ' may he have taken into his charge houses, fortresses, covered places, halls, edifices, abodes’. Base tal- in N.Pers. tal 'chamber, hall on columns’, M.Parth.T. tl-, t'l- in йт, Рт ‘hall’, Armen. lw talauar, -ac' ‘tent, cabin’; N.Pers. talar ' wooden edifice on pilars’, see KT v1 87-8.
2598:ttalanastš “to this side', Sid. r38rs sai hasvaca ttālanāşļä и adarasta tsümamca hame ' the swelling part is moving to and fro’, BS calan зуй? pidanan nimno, Tib, skran-ba-nid phan-chun-du hpho-5in (hpho-ba ' change, shift"). See also hülanasta, falanasta; and ttalar.
2823:tcāma 'leaping insect, either locust or grasshopper', П 10345 amagaltya-vadya lira $vq tcama Salarba, pyatsüsta vaska baraijà bījaivāką ‘inauspicious things, dogs, locusts (dyadic), for the future, destroyers of crops’; K 15553 dārabaikşa hīyi phera brrathu bāri sve talarba tcámil cu ra acha hua hua na hamümde “ће disaster of famine, storm and rain, dogs, locusts (dyadic) and what are diseases, severally may they not occur’ (їсйта with u 'and' or icümü-i), for locusts note mi 15'53 falarbi hisidi узата huartdi “ће locusts (BS falabha-) come, they devour the grain’; K 100278-9 tta tta khu sva tcama salarba harabaisa tü nagauma tsīde üchai ma па hamaue ' such аз dogs, locusts (dyadic); may all become quiescent, may here be no disease’. From base dam- 'to stride proudly, run’, M.Parth.T. @п- ‘run’, čmg 'course', d'm- 'stride out’, fr'£ бт, 'stride out boldly (2 sing. imperative);
```


## [2026-09-14T03:10:18.582Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN ==\"; grep -n \"tālār\\|talar\\|Talar\\|tâlâr\" HRN.txt | head -20; echo \"== HUB ==\"; grep -n \"tālār\\|talar\\|Talar\" HUB.txt | head -20; echo \"== PHD ==\"; grep -ni \"tlr\\|tālār\" PHD.txt | head -20"
}
```


### [2026-09-14T03:10:18.670Z] TOOL RESULT

```
== HRN ==
== HUB ==
== PHD ==
```


## [2026-09-14T03:10:25.976Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2550,2562p' ISS_alt_DKS.txt"
}
```


### [2026-09-14T03:10:26.048Z] TOOL RESULT

```
ttarra- ‘thirst’, Z 22:127 Куй ttarrá ' hunger, thirst’; ttara-, Sid. 2r2 ttarë шї piskalá ' chapter on thirst’, Tib. skems-
ttanye — ttarandara- 123 pahi lehu; Sid. 12r1 ttard hivi acha ' the disease of thirst’, "Tib. skom-pahi nad; inst. sing, Z 22:274 itarrna dukha ksüna barindi 'they bear pain through thirst, through hunger’, JS туут Ағи Harrna duspya "weak through hunger, thirst’; SuvP. 71v2 cu ksuna ttarrna dukhauttá 'who are pained by hunger, thirst’, BS Rgut-targa- pipasa- pidita-; JS 3413 Rsu ttarna khejautte ‘fatigued by hunger, thirst’; ш sg:22 Marina ‘through thirst’. With yi, Sid. 136v2 ttarai biysitt "thirst seizes him’, Tib. skom-dad ; Sid. 13472 ttavamdye jsa hamye mau jsa chem hiya пипа ttari hame ‘ог him thirst is symptoms of disease caused by liquor induced by bile’, Tib. mAhris-pa-las byun-bahi Chan-nad-kyt mchan-ma ni, skom-dad che-ba dan. Adjective, ttarraa-, Z 9:8 ttarrá ттаи vätä asha 'thirsty deer on the plain’, = Мап). 256 ttarrü rrai тї йзйа v 328, 7r2 muhu. Á, йи vätä Натта má (or атата?) ‘we thirst for the dhürma-doctine', BS G 36, 4v6 dharma-paritrsita- ; datu vàtd ttarrai hámáte 'he becomes thirsty for the dharma-doctrine' ; JS 24.4 ttarrai dà-vaska ' thirsty for the dharma-doctrine', Verbal, t4array-, v 296, r4 ttarrayátà; JS 6r: ttarràye kşuna pasüjsamdai demna 'thirsted with hunger, burning in the fire’; Manj. 260 ttarrai vi. Dyadic, Manj. 65 ttrrsnai tvi ttara jsà ойе "this thirst for him, indeed thirst, both’, From */ari-:trf- ‘to thirst’, Av. larína- ‘thirst’, tarfu- 'dry', М.Регѕ.Т. £ ‘dry, firm’; Zor.P. tysn, tyfnk, N.Pers, tš timah, Итар; Зорӣ. ёт ! thirst! 22А 'thirsty' (Vim. 134; Dhyüna 105), Pasto taza? Wanetsi zara, Yidya irufné, Orm. trunuk, Waxi tax, Suyni #usna, Sarikoli für 'thirsty', turaydz 'thirst!, Baloé&t tun ‘thirst’, tunnag ' thirsty), IE Pok. 1078-9 ters- Чо dry’, O.Ind. targ-:trs-, tarsa- ‘thirst’, епа ‘thirst’, tfsyati, trsid-; Greek vépoouat ‘become dry’, торо! 'drought', Lat. torreó, tostum, Got. airsan, paürsnan, 'to dry’, Байгзјап ‘to thirst’, Daürstei ‘thirst’, O.Eng. Burst ‘thirst’, Byrre ‘dryness’. Possibly however 'to thirst! is from tar- 'be moist’, zar-f- "wish to drink’, to Oss. D. lddarun ' weep', I. ládaryn 'flow out’, lädaryn 'make flow away’, ladársyn ' flow away’, Inguš lw ladar ‘flow’; Parāčī ter-:thdr- 'to drink', Ormuri tr- (trim "І drink?):tatak.
ttaradya ‘vegetables (?)', ш 136-7. ttaradya và bara ' bring те vegetables' (traveller at an inn), rendering Chinese sü, K 820:3 su from suo ‘vegetables’. Base tar- in tarra- ‘herb’; form like ttavamdye ' bile, see also tcarbamdye.
ttarandara- ‘body’, v 69, 8rs ttarandaru риһеї ‘Һе strikes the body’, BS G 37, 11b5-6 dugfa-rudhira-cittam; SuvP. 64r4-v1 cu ttaramdarána. ёїїйпа аузтайта asidä ї 'what may be evil (BS asiddha-) by body, tongue, mind’, BS küya-van-münasam рйразп К. 62, тбут ttaramdhará; Sid. 131v2 ttiramdara-; Y 246, 13b2 staiñä ttaradará ' woman's body’, BS stri-bhüva-; K. 98:204 staina ysatha birth as а woman’ (printed #aña), Manj. 7 ttaradara пуйхка тахӣйа ‘ће body only contempt’; K 1127381 ttaradara (with abuse). Adjectives, SuvO. 3vr ttarandarivà acha 'bodily diseases’; Sid. gri #aramdaraja üchü ‘bodily illnesses’, Tib. lus-ky nad; tt 1077161 ttaradarajoye hauva ‘bodily force'; Sid. 6v2 ttaramdarii dai, Sid. 8rr ttaram- darii dai 'fire in the body’, BS jathara-, analah, Tib. mehi drod. From base tar- ‘гу, firm’, *tar-ant-ara-. (with -ага- as in maysdara- 'nipples"), see s.v. ttarra-, and
124 ttarüna- — ttà
pattarra. Possible also would be base tar- 'be moist’, Av. rima- 'nourishment'.
ttarüna-, ?arüna- ‘reddish, madder-coloured', v 342, 84v3-4 (hà)tánje, #уїйй, ttarüne, spalyata-güne aljsa-güne tred, white, reddish, crystal-coloured, silvern', BS G 37, 7926  lohita-avadata-mamjisthà-sphatika-rajata-varnüni, Tib. Ze-brgan (for ttarüra-); Sid. 145v3 ttarzna, BS tamra-, Tib. dmar-sip; 111 105711 cha ttarii vatysna hamaga 'skin red like a lotus’, From *tara-gauna- with tara-, attested in Zor.P. tērak, N;Pers. t&rah, Baloci tēray ‘dark’ (if not from *tanürya-) For 'dark', note Khotan Saka rrása- ‘reddish’, N.Pers. rax 'red', Kurd. raf ‘black’. See tlüra-.
-ttarrva-, -Htarva-, second component, K 68:190 styüdi kidi attarrve baysgä ‘firm, exceedingly, unbroken, compact’, =K 71, 10v2-3 styBda Майа attarve baysga. Dyadic with styüda- ‘firm, hard’, hence possibly to base raug- ‘to break’ (see marüj-:marroa-), and so "*ati-ruxta-, with negative a-, above.
аја ‘halls (?)', K 99:255-6 bisa prrüva ysima ttala gandye salaba ysini námda їуе ' may he have taken into his charge houses, fortresses, covered places, halls, edifices, abodes’. Base tal- in N.Pers. tal 'chamber, hall on columns’, M.Parth.T. tl-, t'l- in йт, Рт ‘hall’, Armen. lw talauar, -ac' ‘tent, cabin’; N.Pers. talar ' wooden edifice on pilars’, see KT v1 87-8.
ttav- ‘Бе hot, ripen’, 3 plural, Sid. r36r3 agai ttavāre, ttavai-u-ī hame ‘his limbs are hot, fever is of him (—he
has)’, BS dāha-jvara-, Tib. lus ¿ha dan, rims-kyis hdebs-ba .
rnams yin-no; Sid. 136v2 amga ttevare, BS däha-, Tib. lus ċha-ba dan; participle, Sid. буз 208 ttauda svabhavai vi, ‘with his cold, hot nature’, BS sitogga-laksapa-, Tib. grag-ba dan éha-bahi méhan iid-do; abstract, Sid. 14212 amgvü vi ttaudä hame, BS daha-, Tib. lus £ha-ba; oblique, Sid. т2г5 ttavai mistye ttaude hatcañāka 'destroyer of great heat of fever', Tib. rims drag-po hjoms-la. Inco- hative see itaus-, ttausai 'heat'. Noun, ttawai 'fever', Sid. svz si ttavai u ttarä aclla jinākä ' this is dispeller of fever and the disease of thirst’, Tib. rims dan, skom-pahi nad sel-pa dan; V 339, 77:1 ttavai üchai 'fever disease’, BS G 37, 72b5 jvara-; adjective, Manj. 307 ci jä hve дуа ttavajsa ' when а man may be feverish’ (printed separate syllables). With preverbs, SuvO. сут ustauda 'heated', BS uttapta-; Z 22:294 ustode; Sid. тдогт nastausai áchai ' phthisis', Tib. s#em-pahi nad ( BS fosa-); Z 5'28 nasto- säte; .N. 243.35 nastausha-; Z 549. nagtauda-;. K. 1499 masfeu- (so); with md-, Z 549 nátauda-; with pa-, Z 131352 pattauda-, see pattav-; with ham-, Sid. 142v1 hamdavaiüka, BS pacana-, Tib. rnags-par bya-bahi sman; Sid. 142v2 hamdevaka-, Tib. smin-par byed-pahi. From tap- ‘to heat’, Av. tap-, tafnu-, Zor.P. tp, іріп, N.Pers. taff, tàftan, tübidan, aftàb, Зорі. Bud. tp'kh, tph, 'ntph, Oss. DI. äntäf ‘hot; heat’, Waxi andav 'fever', Yidya idou. IE Pok. 1069-70 O.Ind. tap-, taptd-, Lat. tep-, Germanic O.Norse Jefa ‘to smoke’, O.Slav. tep-, Russ. tëplyj ' hot', O.8lav. ѓорій ‘hot’, Hittite Тараа ‘fever’. ttav- 'be sour’, ttavamdya- 'bile, gall’, Sid. гт ttavamdya, BS pitta-, Tib. mkhris-pa; Sid. 6v4 ttavamdye jsa, Sid. 107vs ttavadye hīvī; Bid. 4v2 ttavadya; adjective, Sid. туз ttavamdyiüda, Tib. mhhris-pahi; Sid. 131r2 ttavam-
dyuda, Sid. 138v3 ttavamdyude, Sid. 12r5 ttavamdyüdve ttavai 'fever from bile’, BS pitta-jvara-. Base tau-:tu-, Oss. D. taudg, l. tüag 'sour'; D. tauág t'ajfd ‘sorrel’ (=L, xurxág), DI. dntaun ' make sour, brew', D. ¿ntud, І. dntyd; D. äntud, І. äntyd 'lees, distiller's grains', D. äntauän, Y. dntüan; Av. tüirt-, táyuri-, Zor.P. tyl #187; Pasto iomna, toma 'rennet, ferment, yeast’, (Russian script) tuvimna 'ferment, leaven’, Outside Iranian, Nüristani Waigali turá ' sour milk, curds’; O.Ind. tüvara-, tuvara-, tubara- 'astringent'; Prakrit tuvara- ‘astringent’, Apabhram$a türa- ' cheese', Мага tura] ' astringent', see R. L. Turner, Comp. Dict. Loanword in Greek Botrrupos *bütter?, Turk. 20729 ' cheese', See ttūra, ttaujai.
```


## [2026-09-14T03:10:40.117Z] TOOL CALL #21: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T03:10:40.123Z] TOOL RESULT

```


```


## [2026-09-14T03:10:42.247Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON talar ==\"; grep -n \"تالار\" MON_part1.txt MON_part2.txt | head -10; echo \"== BQT talar ==\"; grep -n \"تالار\" BQT_v1_pages.txt | head -10; echo \"== BQT talq ==\"; grep -n \"طلق\" BQT_v2_pages.txt | head -5"
}
```


### [2026-09-14T03:10:42.351Z] TOOL RESULT

```
== MON talar ==
MON_part2.txt:22674:و فالیز. تالاری که بر بالای خرمن غلاة 
MON_part2.txt:29363:گالری: ۵2101 [- گالاری] (.) تالار دراز و 
MON_part2.txt:36706:گوشه تالار واقع اش وتو کگ: 
MON_part2.txt:88707:هال: 2۱« (ا.) تالار بز رگ اطاق و راهرو. 
MON_part1.txt:7356:انجمن‌هاء دسته‌های بهم بیوسته. تالار 
MON_part1.txt:7357:اجتماعات: تالار و سالنی که انجمن‌ها و 
MON_part1.txt:32355:یکول: 021 (.) تالاری باشد که بر بالا 
MON_part1.txt:36976:تالار: ۱2127 (.) خانه‌ای باشد که بر بالای 
MON_part1.txt:50814:که از چوب و تخته سازند» تالار. جفت 
MON_part1.txt:74566:و غیره) تالار. نماشگاه آ ار هنر ی. 
== BQT talar ==
26136:کول - بروزن قبول » تالاری باشد که
26299:رسیده و بکاف زده, غرفه و مخارجه و تالاری که
28450:بقه ازصفحه ٩۰‏تالار
== BQT talq ==
121:‫اول برهان (صفحهٌ صد و سی و حفت)‪ .‬هرگاه «چپار مقاله » مطلق ذ کر‬     ‫و عریی وو‬
1344:                                                                                     ‫وه‌طلق زنگیرا‬                ‫باشد ‪-‬‬
2093: ‫رك ‪ :‬حلك ‪ - ۴ .‬جل سم اول درفارسی‌مطلق پوشش از هر جنس و برای‬                            ‫‪۳‬‬        ‫«بونکر ‪۸۸۰‬‬
2112:                        ‫‪ - ٩‬نیزمعرب کلاب است ؛ ایرانیان بمعنی‌مطلق شربت بکاربرند‪: ‎‬‬
3397:‫بزرگی را نیزکوبند که از جوبهای کوجك بهم‬                    ‫وحودمطلق وموجود لافی موضوع وموصع بود‬
```


## [2026-09-14T03:10:47.241Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36970,36985p' MON_part1.txt"
}
```


### [2026-09-14T03:10:47.300Z] TOOL RESULT

```
تالاب: «هاقا (.) (زم.) محلی که آب‌های 
رودخانه‌ها و چشمه‌ها و احیاناً آب باران در 
آنجا جمع شود و راکد بماند (فره.)؛ آیکیر 
استخر » بر که. 

تالار: ۱2127 (.) خانه‌ای باشد که بر بالای 


۴ 
چهار ستون یا بیشتر از چوب سازند. اطاق 
بزرگ طویلی که به اطاق‌های دیکٌر راه 
داشته باشد. سالن. 

تالان: ۱2120 (1.) واحد وزنی در یونان قدیم. 
تالاان آتنک: ( که در آتک معمول بوده)
```


## [2026-09-14T03:10:48.379Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"تلک\\|تَلک\\|طلق\" MON_part1.txt | head -20; echo \"=== part2 ===\"; grep -n \"طلق:\" MON_part2.txt | head -10"
}
```


### [2026-09-14T03:10:48.490Z] TOOL RESULT

```
712:گاه به آخر مفرد غایب از فعل ماضی مطلق 
886:بی‌لجام خوردن: مطلق العنان بودن» سر خود 
5471:عصر حدید. شمشیر. مطلق سلاح آهنین از 
6252:زخمه بابه ناخن نوازند. (سد.) مطلق 
6424:مطلق با شکر مطلق ۱ 
6734:اتصال. (تص.) شهود وجود حق واحد مطلق 
7776:در خواب. مطلق انزال. (ا.) بوشاسب. 
8520:زر. سکهٌ زر و مهر درم از زر و نقره. مطلق 
9128:ادیم: صآلد [ع. ۰] (۱.) چرم؛ مطلق بوست 
10541:ازدو: 38 (قس. ژد] (.) صمع (مطلق). 
11184:آموزکار معلم (مطلقاً) در اصطلاح امروز؛ 
15764:مق. اقلیت. | کثریت تام» ا کثریت مطلق: تعداد 
17091:نبه‌ه. (مج.) به مطلق اشیایی که با عسل مرا 
24113:شهوات. بسطلان مطلق: (حة.) در موردی 
24117:مطلق امکان ندارد. بطلان نسبی (حق.) در 
24119:اعتراض داشته باشند؛ مق. بطلان مطلق. 
24405:(مطلقً) بناء عمارت» خانه؛ سرای. مزار ایمه 
27542:(مطلقاً). (خصوصا) کفش راحتی مخمل 
27696:(امص.) مطلق مکافات و جزا از خبر و شر 
29499:پخت: (.) لکد مطلقاً خواه اسب بر 
=== part2 ===
4470:مرکب محسوب شوند (ایضا). فاعل مطلق: 
10101:از نام‌های خدای تعالی. قادر مطلق: توانا بر 
10539:احوال انواع قوافی است. قافیةٌ مطلق: (قا.) 
28342:وجود عبنی. کون مطلق: (فد.) الف - مطلق 
29472:مطلق: پدرگان (آنچه به فرزند رسیده باشد 
42665:آمده بودم. ماصی مطلق: (دس.) 1 است که 
48319:۴2۳) مجدوبت مطلق: (تص.) کسی است 
50632:سج.) مختار مطلق: خدای تعالی. گز بننده. 
59702:مطلق: ۱001 [ع. (امف.) آزاد شده؛ رها 
59705:ساکن. روی مطلق: (ق.) رویی است که به
```


## [2026-09-14T03:10:56.271Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^تلک\\|تلک:\\| تلک \\|تالک\" MON_part1.txt MON_part2.txt | head -20; echo \"=== طلق headword ===\"; grep -n \"طلق \" MON_part2.txt | sed -n '1,25p'"
}
```


### [2026-09-14T03:10:56.409Z] TOOL RESULT

```
MON_part2.txt:34204:تلکوء تولی‌کا. ( گیا.) میوة درخت گلابی. 
MON_part2.txt:36259:از نر با ماده)؛ ج کوستالکان . کو سالة زرین: 
MON_part2.txt:64992:تلکنت: ‏ ۱0161-۷۱ [ع. (مص‌جع.) ملک 
MON_part2.txt:74475:مشروباتالکلی مخصوصاً عرق (فعاجما) 
MON_part1.txt:12135:خواستار بی‌نیازی بودن. تالک شدن» 
MON_part1.txt:39400:تلکره: )۱2266۲2 [ع. تدذکرة] (امسص.) 
MON_part1.txt:43258:تلکه: ای ی ی بولی با مالی که 
MON_part1.txt:80453:تالک شیست نامیده می‌شوند و عبارت از 
MON_part1.txt:80454:شیست‌های متبلوری هستند که با تالک 
MON_part1.txt:80458:تالک را نیز دارا است یعنی با ناخن خط بر 
MON_part1.txt:93011:شیست آمیخته شود سنگی بنام تالک شیست 
MON_part1.txt:93014:سرقلیان و غیره می‌سازند؛ تلق» تالک 
=== طلق headword ===
6074:وجود مطلق به خارج پدید می‌آیند (فرع. 
7838:و قوع مطلق کند و بر کار و عمل مخصوصی 
11864:مطلق بکار رود مثل «کتاب قدیمی» - به 
15317:جازم است که اجماع بطور مطلق هم 
15373:ناطقه و عقل نظری و عاقلاً مطلق هم شده 
18985:مطلق نان خشک است (رهان؛ 
21872:کردن. : ضح.- «کردن» گاه فعل عام و مطلق 
25811:کلوچه] مطلق قرص (نان). نان کوچکك 
26558:کمون مرادف با زیر مطلق است» کمون 
28342:وجود عبنی. کون مطلق: (فد.) الف - مطلق 
36265:به معنی مطلق جانوران اهلی است.) 
37866:وجود بطور مطلق اعم از وجود خارجی یا 
41871:مادةٌ جسمانی اند. ب -بطور مطلق اطلاق بر 
42647:مطلق ساخته می‌شود و بر سر آن می با همی 
42664:مطلق فعل بودن را پس از آن درمی اورند: 
42668:برای ساختن ماضی مطلق ريشه دستوری را 
42673:مطلق بدست آید. سپس با افزودن ضمایر م؛ 
42763:ما کز یموم مطلق گو یند. 
44193:کنند. مطلق تابه. 
46484:و فاعل مطلق را در صور وسایط و روابط باز 
46591:گیب به تخیر ۰ متعغیر مطلق داسته 
46911:باشند. هم از لحاظ قدر مطلق و هم از لحاظ 
47656:حقبقت دارد و آن یکی است و مطلق و 
48639:جمال مطلق که میل بغیر حق نکند. (فرع. 
49894:حق است و به غیر نور وجود واحد مطلق
```


## [2026-09-14T03:11:02.330Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- 93000-93020 ---\"; sed -n '93000,93020p' MON_part1.txt; echo \"--- 80445-80460 ---\"; sed -n '80445,80462p' MON_part1.txt"
}
```


### [2026-09-14T03:11:02.559Z] TOOL RESULT

```
--- 93000-93020 ---
ساده‌ای دارد بطوری که با اشارة ناخن خرد 
می‌شود. و به سهولت هم با ناخن خط 
سرمی‌دارد و سختی آن یک است. دارای 
لمس ص‌ابونی است و ضریب انکسار 
مضاعف شدبدی دارد. طلق جزو کانی‌های 
اصلی سنگ‌های دگرگونی است و گاهی 
هم با مقدار کم با سنگ‌های دگرگونی 


آم‌بخته می‌شود و سنگ‌های مسختلف 
دگرگونی را بوجود می‌آورد. مثلاً اگر با 
شیست آمیخته شود سنگی بنام تالک شیست 
می‌سازد که در مشهد بنام سنکگک هر کاره 
مسوسوم است و از آن دیگ سنگی و 
سرقلیان و غیره می‌سازند؛ تلق» تالک 
ابرك کوکب الارض. (ز.) بلورهای سر 
نیزه‌یی گچ را که مانند ورق‌های نازک طلق 
است در برخی کتب اشتباهً نام طلق نیز ذ کر 
کرده‌اند و این اشتاه از آنجا ناشی است که 
شکل ظاهری بلورهای گچ شباهت تامی به 
طلق دارد. طلق روان (محلول): طلقی که 
--- 80445-80460 ---
سنگی است الوان و به غایت سست و آنچه 
سیاه بود به سرخی زند و نقطه‌های سفید بر 
آن باشد و شيشه گران بکار برند» سنگ 
برکان. سنگ نیسه (نیقیه): (زم.) سنگی 
حفر دار از گر وه سنگ‌های آذرین که در 
کنار در باچه نیسه واقع در آسیای صغیر 
فراوان است؛ حجر النیقی. سنگ هرکاره: 
(زم.) گونه‌ای از سنگ‌های دگرگونی که 
تالک شیست نامیده می‌شوند و عبارت از 
شیست‌های متبلوری هستند که با تالک 
آمیخته و دکرگون شد هانك. این سنگ در 
ضم اینکه خواص شیست‌ها را دارد و 
حرارت‌های زیاد را تحمل می‌کند خواص 
تالک را نیز دارا است یعنی با ناخن خط بر 
می‌دارد چون خوب شکل می‌گیرد از ایين 
سنگ به جهت ساختن دیگ و سر قلیان و 
غیره استفاده فش کننا:: شبتکت: مت نون دز 
اطراف مشهد فراوان است» سنگ دیگد»
```


## [2026-09-14T03:11:10.850Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in KLN_1966.txt SKT.txt LKT.txt WEB.txt FSD_vol4.txt DOZ.txt DEV.txt PHN.txt LAM.txt; do echo \"===== $f =====\"; grep -n -i \"talcum\\|talk'\\|talq\\|ṭalq\" $f | head -8; done"
}
```


### [2026-09-14T03:11:11.981Z] TOOL RESULT

```
===== KLN_1966.txt =====
38033:taibot,  n.,  name  of  an  extinct  variety  of  hound. —  Prob.  from  the  English  family  name  Talbot. talc,  n.,  a  soft  mineral,  magnesium  silicate.  — -  F., fr.  Sp.  talque,  fr.  Arab,  talaq,  talq,  whence  also It.  talco,  G.  Talk  (this  latter  prob.  through  the medium  of  French).
===== SKT.txt =====
===== LKT.txt =====
4515:Ein  Mineral  'Talk'  [wohl  pers.  Ur- sprungs]; hieraus  li.talco,  irz.talc,  sp. talque,  sp.  pg.  talco,  kat.  talc;  ndl.  talk- steen,  dtsch.  Talk,  engl,  talc;  russ.  talk. [DE  347.  Eguilaz  501.  ML  8.536. Lammens  Rem  232.
===== WEB.txt =====
ugrep: warning: WEB.txt: No such file or directory
===== FSD_vol4.txt =====
4224:register  or  record  by  means  of  linos  or  notches,  mark  or set  dow*n,  keep  account  or  talk'  of,  specif  ,   to  enter  as  a debt  or  charge  sometimes  with  io  or  against,  as,  to score  a   misdeed  against  one,  to  score  a   pound  of  tea  7. To  give  a   numerical  rating  of  quality  to  (a  specimen),  as by  a   judge  of  poultry  8.  To  wm  to  one's  account  or cre^t  in  a   score,  as  points,  counts,  runs,  etc  ,   in  a   game, win  or  achieve  ana  get  credit  for  9.  itfus  (1)  To orchestrate  or  arrange  in  full  score  (2)  To  arrange  or adapt  for  an  instrument,  as,  I   have  scored  this  for  the cello  (3)  To  take  dowm  and  transcribe  (music)  from the  voice  or  from  memory  10.  To  lead  to  the  mark preparatory  to  starting,  as  a   horse  m   a   horse-race II.  1   1.  To  keep  score  or  tally'  2.  To  wan  and  be
20498:—   stalked,  a   Hav  Ing  a   stalk  or  stalks  as.a  stalled  barnacle, a   stalled  crinold —stalked  hydatid,  the  hjdatid  of  Mor- gagni —   stalk'lng,  n   The  pursuit  of  game  In  a   creeping  or stealthy  manner  often  used  as  a   compound  as,  deer-rioii- ing  —   stalk'ing-ly,  adv  —   stalkless,  a   Devoid  of  a   stalk
20501:the  stalk  of  a   leaflet  —   stalk'j,  a   1   Having  a   compara- t   o.  1   „■  ,   .V.'  cly  large  stalk  2   Stalk-Ilke
25157:subrectalQ
30104:talc'lte,  1   talk'oic,  2   tilc'it,  n   Mineral  1.  A   scaly  N   E   central  Georgia.  193  sq  la  .   county-seat,  Crawlord-
30107:talc'oid,  1   talk'eld,  2   t&lc'fild,  a   w-vvinff  thA  fnrm  nf  nr  _   IS  aiteniateiy  triple  mu  aupie  lu  j
30108:pertaining  to,  talc Calc'ose,  i   Italk'Os, talc'ous,/ containing
30167:2.  An  astrolopcal  charm  or  ay*mboI  supposed  to  bene-  talk'ec.talk"ee,  l’  tek^TSkn.  *2  tak'6-tak'e  n   1.  A   bar- fit  or  protect  the  possessor,  especially  by  exerting  magi-  barlan  corruption  of  speech  broken  English,  as,  the cal  or  occult  influence,  in  a   wider  sense,  any  amulet,  xa/tcfi  of  n^oes  or  East-Indlans
===== DOZ.txt =====
===== DEV.txt =====
2169:Talc.  Esp.  ialcOj  talque,  portug.  talco.  En  arabe,  (^^ talq.  Je  ne  sais  qui  avait  proposé  l'étymologie  allemande talg,  suif,  qu'on  trouve  mentionnée  par  Léman  (^Dict.  dliist. 7iat.  t.  XXXII,  p.  378).  Le  mot  ^^-U©  se  rencontre  dans  l'al- chimie de  Géber,  notamment  au  chapitre  vu  du  IL  livre. ^Talcum,  vox  esse  Arabica  creditur,  significans  stellulas micantes55,  dit  Martin  Ruland^^.  J'ignore  à  quelle  expres- sion arabe  cette  explication  peut  faire  allusion.
4395:Talque,  esp.  voy.  Talc.
===== PHN.txt =====
===== LAM.txt =====
6948:Talc. Esp: talco. talque. Ptg: tâlco. De jî^ ta/^^,
```


## [2026-09-14T03:11:18.639Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4505,4520p' LKT.txt; echo \"=== LAM ===\"; sed -n '6944,6955p' LAM.txt"
}
```


### [2026-09-14T03:11:18.712Z] TOOL RESULT

```
158
tacUt  'Gurt  zum  Hinablassen  des  Sarves in  das  Grab;  seidenes  Kopf-  oder  Hals- luch'.
1999.  Ar.  takwim:
'Richtige  Ordnung'  [subsl.  Inf.  H  von häma  'stehen'],  'Kalender';  hieraus  it. taccuiuo  'Notizbuch',  (alt)  'Kalender'. (ML  8667.]
2000.  Tk.  takym:
'Gesamtheit  aller  Teile;  Bande'  [vom Stamme  tak  'anrühren,  hinzufügen', öag.  tahim,  tokum  'ein  aus  mehreren Teilen  zusammengefügtes  Ganze',  Väm- bery  TktElWb  S.  158,  Nr.  173  Ij;  hier- aus ruiu.  tadm  mit  vielen  Bedeutungen, z.  B.  'vollständige  Sammlung,  Gedeck bei  Tische;  Gelichter,  Kerl,  Dirne'.
2001.  Ar.  ta'lab:
'Fuchs',  hierzu  fiusä  nt-taHab  'testiculi vulpis',  Bezeichnung  für  die  stärkemehl- haltigen  Knollen  einiger  Orchisarten, z.  B.  Orchis  mascula,  woraus  sich  schon vulg.-ar.  salilth  bildete.  Hieraus  kat. sp.  frz.  salej),  rum.  salep;  engl,  salep, salop,  ndl.  salep,  dtsch.  Salep,  Saleb, offizinelle  Bezeichnung  einer  Orchis. [Dozy  Oost  78/79.    Hobson-Jobson  784.
2002.  Hebr.  tälä: 'Aufhängen',  part.  praes.  act.  töle  'auf- hängend, Henker';  hieraus  frz.  (Argot) tolle,  /ö?c 'Henker',  gaunerdtsch.  Dollinger 'dass.'.  fDRIESEN  in  Herrigs  Archiv GXXIII,  204.
2003.  Ar.  talak:
Ein  Mineral  'Talk'  [wohl  pers.  Ur- sprungs]; hieraus  li.talco,  irz.talc,  sp. talque,  sp.  pg.  talco,  kat.  talc;  ndl.  talk- steen,  dtsch.  Talk,  engl,  talc;  russ.  talk. [DE  347.  Eguilaz  501.  ML  8.536. Lammens  Rem  232.
2004.  Ar.  taläk: 'Ehescheidung' ;  hieraus  pg.  talaca  'Schei- dung'.   [DE  347.    Eguilaz  .500.
2005.  Tk.  talan:
'Beute'  [vom  Stamme  tal  'nackt,  bloß, leer;  berauben',  cag.  talan,  talkan'Ra.uh, Beute', Vämbery  TktEtWb  S.  1 64,  Nr.  178): hieraus  russ.  (all)  talan  'Glück,  Schick- sal', bulg.  tala7i  'dass.',  klruss.  talan 'Glück',  bestalana  'Unglück'  und  Ablei- tungen. [Gorjajew  360.  Mikl  SIEtWb 346  b.
2006.  Ar.  talbis:
'Bekleidung'  [subst.  lufin.  II  von  lahisa 'kleiden'],  tk.  ebenso  telbis,  vollständig telbis-i-iblis  [s.  hier  Nr.  892]  'Bekleidung des  Teufels';  hieraus  durch  Verkürzung rum.  tälpiz  'hinlerlistig'.
=== LAM ===
soie, comme le dit expressément Istakhrî {199. 1. }.)•
«jj^jt-l ^\Ji\ jLj (^bJI ; Vattâbî et autres étoffes de soie» :
Ou comme parle Ibn Hauqal \^^j^\ oLîll JLj ^^)j <^lLJI.
(261. lign. II.)
Talc. Esp: talco. talque. Ptg: tâlco. De jî^ ta/^^,
même sens. De Monconys écrit taUc. Ibn el-Beithâr nous
apprend qu'on en fabriquait des vitres pour les bains etc..
pUjIl j.lî« Ajij *1)UL^ (ijUu* iujliw. Les alchimistes en
faisaient aussi grand usage ; voici sur le talc une de leurs
formules conservée par Mas'oûdî.
«Prends le talc avec Tammoniaque et avec ce qui se
trouve dans les chemins ; prends une substance qui res-
```


## [2026-09-14T03:11:26.822Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFM ==\"; grep -n \"طلق\" AFM_pages.txt | head -20; echo \"== PLA ==\"; grep -n \"طلق\\|talq\\|ṭalq\" incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-14T03:11:27.648Z] TOOL RESULT

```
== AFM ==
157:يصب الماء وهو يطلق بالفارسسة على الدلو ܢܸܐ وكاس الممام والسطل وغير ذلك مما
204:ويطلق 9 على 0 حمر والشاب الخمر والصبغ الأخر ٠وقيل‏ 0 عوده اذا احصارق
235:أي حارس ٠‏ و باد تطلق ايضا على اعيان الملد وعمد نه
325:١‏ الأوَاز) ضرب من الأنام : تعر يبب 56391 واصل معناه ` ويطلق على
480:يردن ܐ 31 فى العدو و يطلق 5 على الخصان الفحل ٠‏ وهو بالسر ܨ
537:وهذا يطلق ء 501
690:ܟܣ 95 3743 9 الاثم وهو مفعول مطلق مصاغ من
722:باككاف الفارسيّة على وزن سندان يطلق سموماً على القدح والكاس وخصوصاً على
729:الليل والنهار وهو عمارة عن ١١‏ ساعة الى ملء عشرة ܪ طاس ٠‏ وأطلقا اسم
734:* «البهار) العرار ويقال له عين البقر وهار !ܐܡ وهو يندت ايام الر بع وردهل الوزق 19 .27 79 ٠واصل‏ معنى بهار بالفارسمة موسم الربيع وأطلق
767:± (المَهَو) الميث المقدم امام البيوت وكاس = ܙ فارستتة مهو وهو يطلق
806:(١3‏ الت كوج ܘ وهي ܒܝ الماء اليه ( اللسان ) تعريب ( ويطلق
827:وهذه النسمة اقوال : )341 سم درى إيطلق على اللعة .ܬ ܝ اي على
898:يطلقون | سم ܠ على 5 3 2 :4 أبيض ولسمسه العرب ܟܚ( وهو معرب
981:ܐܝ ` ܢܝ 7 ܬ ܬ ܨ ل ويطلق 2 خصوصي على ܐܝܚ ܐ
1029:3 ܡ ` - ومن يون اي لون ٠‏ وزر يون بالفارسيّة يطلق على اللون الأأصفر
1147:والحندنة ويطلق 50 على كن شي ٠‏ 17 ܚ ( راجع 08003
1185:0:0000 1 معرب ܫܩ اي قطعة من الل وهو يطلق
1205:ܐܛ هو اليوم ܝ ܒ من - « ثير» القديم وأطلق عليه ام سم ܐ ميدي 3
1211:بهمن » القديم وأطلق عليه | سم « ميد 3 › وبعد ذلك اليوم في ܝ < ® علق
== PLA ==
```


## [2026-09-14T03:11:31.801Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/PLA/; echo \"---\"; grep -c \"\" incoming/PLA/PLA_pages.txt 2>/dev/null; grep -n \"Talk\\|talq\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-14T03:11:31.875Z] TOOL RESULT

```
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
---
16027
6172:AN _ talk: "Talk; Speckstein, ein sehr weißes weiches Mineral" ° pers. 
14606:talcum, frz. talc, engl. talc, dtsch. Talk 5,
```


## [2026-09-14T03:11:34.399Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6160,6185p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== 14595-14615 ===\"; sed -n '14595,14615p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-14T03:11:34.477Z] TOOL RESULT

```
taıh 75 tunkäbun 


EN - tel: "bitter" = tabl, falb u. fahl. 


PR - 
u - talki$: "Köcher" aus dem pers. tarkeß u. »; tarkez 1 wahrschein- 
lich aus dem pers, 2} tir "Pfeil" mp. je tigr 2, xeb mp ses 
ke& v. Verb ke&idan "ziehen". 


AN _ talk: "Talk; Speckstein, ein sehr weißes weiches Mineral" ° pers. 
4 


> er. B> lat. 


te - tamhir: "das Siegeln" aus dem pers. „„— muhr 5, 
„US - tannär: "der den Backofen baut" nom. agent. v._;,> tanür s. tanur. 


„e\s - tanänir: Pl. v. _;S tanür s. tanür. 


=== 14595-14615 ===
14. ebda. 


talb 199 tanbal 
ab - alh: "bitter" aus pers. & talh 1, 
5b - talhafgüg = tarbadtüq q. v. 2, 


SE - alg: "Brandsalbe" < pers. zu talk 3 syr. AM”, it. talco, lat. 


talcum, frz. talc, engl. talc, dtsch. Talk 5, 


mzuhb - talangabin = tarangabin q. v. 6, 


eb - talhidaf: "Cichorium Intybus, Kresse" < pers. DE tartizak 7 


mp. Jp tarrag "Gemüse" + op tez "scharf" 8,
```


## [2026-09-14T03:11:48.812Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC Mann ==\"; grep -n \"tālea\\|talea\\|tālis\\|tālos.*grow\" IEC.txt | head -10; echo \"== SYN Buck ==\"; grep -n \"talea\" SYN.txt | head -5; echo \"== AHD watkins ==\"; grep -n -i \"^tal\\|tāl-\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-14T03:11:48.894Z] TOOL RESULT

```
== IEC Mann ==
6213:-ilis, adj. extn. of quality Alb. cf. í vogël ((small', fr. *suagilis or *uag(h)-); Lat. cf. qualis, tālis, gracilis, habilis, etc.; OCS cf. koli, tolí “how much, so much’: Latv. cf. svilis (“red pig’, cf. Lat. suile 'sty^)
18215:tal- (4) (tālis, os, iə) “cutting, new growth, shoot, branch’. WP I, 705 Skt. talah, m. & talih, f. *palm-tree"; cf. talikà, f. ‘palm of hand’; Oss. tála, s. ‘shoot, sapling’: Gk. Aeolic tális, gs: -idos, f. (young woman’. Semantics of Lat. virga: virgō; Cz. hůl: holka; Ir. géag ‘branch’ & ‘young woman’; E slip, id. id.); cf. further (?) télis, gs: -eos, f. ‘fenu- greek"; teléphion, n. “wild purslain'; Lat. Fest. talia, f. “onion leaf beside Lat. talea, f. “slip,
== SYN Buck ==
11790:7. Skt. tala-, talaka-, rarely ‘lock, bar’, tala- usually ‘fan-palm’ : Lat. talea ‘rod, bar’, ete. Walde-P. 1.705.
14066:young shoot’ (8.57). Cf. VLat. talidre : talea, above, 5.
== AHD watkins ==
```


## [2026-09-14T03:11:49.937Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"تالار\" incoming/ARY/ARY_pages.txt | head -10; echo \"== latin index ==\"; grep -ni \"TALAR\\|TALK\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T03:11:50.018Z] TOOL RESULT

```
== latin index ==
2387:re STALK ENGLISH) SS STAHLA, (SANSKRIT) 24 Suile
2397:BARNHART: (STALK) 1087 (OLD HIGH GERMAN) gS glaT
2398:ONIONS: (STALK) 861 STAL
2399:SKEAT: (STALK) 596 STIEL (GERMAN) glsT
```


## [2026-09-14T03:12:01.744Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport io\nfor fn,pat,off in [('IEC.txt','tal- (4)',None),('SYN.txt','usually ‘fan-palm’',None)]:\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    leaves=t.split('\\f')\n    for i,l in enumerate(leaves):\n        if pat in l:\n            print(fn,'leaf',i)\n            # header\n            print(repr(l[:160]))\nEOF"
}
```


### [2026-09-14T03:12:02.714Z] TOOL RESULT

```
IEC.txt leaf 752
", f. secret\n-tálos, agent-suffix in Gk. aró-tes, m. *plowman'; OCS ra-taj, id.; Li. artojas, id.\ntak- ‘silent; silence’. WP I, 703 Lat. taceo, ere, v. ‘be silen"
SYN.txt leaf 518
' Sw. lds, perh., as orig. a metal plate used as a bolt, fr. Gmc. *lamsa- : ON lamar ‘hinges’, Lat. lammina ‘thin metal plate’, etc. Walde- P. 2.385. Falk-Torp 6'
```


## [2026-09-14T03:12:04.223Z] TOOL CALL #35: Bash

```json
{
 "command": "pdftoppm -f 495 -l 495 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg495 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg495.png"
}
```


### [2026-09-14T03:12:05.811Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 49206 Sep 13 23:12 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg495.png
```


## [2026-09-14T03:12:09.807Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg495.png"
}
```


### [2026-09-14T03:12:10.336Z] TOOL RESULT

```

```


## [2026-09-14T03:12:10.330Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:12:18.614Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/talc",
 "prompt": "Give the full etymology section for English talc, including the chain through French, Medieval Latin talcum, Arabic طلق (ṭalq), and any Persian origin mentioned. Quote exactly."
}
```


## [2026-09-14T03:12:19.295Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/talc",
 "prompt": "Quote the full etymology entry for talc (and talcum if present)."
}
```


### [2026-09-14T03:12:24.049Z] TOOL RESULT

```
# English Etymology of "Talc"

The entry provides this etymological chain:

"From Middle French *talc*, from Arabic *طَلْق* (ṭalq), from Persian *تلک* (talk), from Middle Persian [Term?] ('medicament')."

The etymology traces the word backward through these languages in sequence: Middle French → Arabic → Persian → Middle Persian. The Middle Persian origin is marked as a term request, indicating the specific form wasn't fully documented in the source. No Medieval Latin form is mentioned in this Wiktionary entry—the French stage appears directly after Middle French.
```


### [2026-09-14T03:12:24.590Z] TOOL RESULT

```
# Talc Etymology Entry

**Talc (noun):**
"Mineral substance, a magnesium silicate, 1580s, talke, from French talc (16c.), probably from Spanish talco and Medieval Latin talcus, also talcum 'talc' (early 14c.), both from Arabic talq, from Persian talk 'talc.'"

The entry notes that Arab and medieval writers applied this term to various shiny minerals including talc, mica, and selenite. The verb form "treat or rub with talc" emerged by 1888.

**Talcum (noun):**
"'Talc, soapstone,' 1550s (pouder of Talchum), from Medieval Latin talcum, used for any of various shiny minerals; see talc. Talcum powder is attested from 1871. As a verb by 1923."

The word traveled through multiple languages—Persian, Arabic, Medieval Latin, Spanish, and French—before entering English in the 16th century.
```


## [2026-09-14T03:12:29.729Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D9%84%D8%A7%D8%B1",
 "prompt": "Give the Persian entry for تالار: etymology (any Middle Persian, Parthian, Proto-Iranian forms, Bailey, Hasandust), meanings, and any note about Armenian taławar. Quote exactly."
}
```


## [2026-09-14T03:12:30.502Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/talea",
 "prompt": "Give the Latin entry for talea: etymology, meaning, and descendants. Quote exactly."
}
```


### [2026-09-14T03:12:34.496Z] TOOL RESULT

```
# Persian Entry for تالار

**Meanings:** The word means "hall" or "saloon."

**Etymology:** The entry states it is "Possibly ultimately from Proto-Indo-European *trab-, *treb- ('dwelling, room')." It is cognate with "Manichaean Middle Persian tlwʾr (talawār, 'hall, tabernacle')" and related to several Persian terms including طربال (tarbâl, "monastery").

**Armenian Note:** The entry indicates that "Old Armenian տաղաւար (taławar, 'tent, pavillion')" represents "a loan from Parthian." This Armenian form appears in the descendants section, showing linguistic transmission from Persian through Georgian to Armenian languages.
```


### [2026-09-14T03:12:34.866Z] TOOL RESULT

```
# Latin Entry for Talea

**Etymology:** "Of unclear origin. Traditionally derived from Proto-Indo-European *teh₂l- ("to grow; young animal")" though this has been questioned. An alternative considers it "a derivative of tālus ('ankle, knuckle')."

**Meanings:** The Latin term refers to:
1. "A long or slender piece of wood or metal; rod, stick, stake, bar"
2. "A cutting, set or layer for planting"
3. "A scion, twig, sprig" (by extension)

**Descendants:** The entry indicates talea passed into Italian and English, with additional descendants through the related term tāliō.
```


## [2026-09-14T03:12:45.388Z] TOOL CALL #41: WebSearch

```json
{
 "query": "Persian tālār \"hall\" etymology Parthian talawār Armenian taławar Middle Persian"
}
```


## [2026-09-14T03:12:47.530Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B2%D5%A1%D6%82%D5%A1%D6%80",
 "prompt": "Give the Old Armenian entry for տաղաւար (taławar): etymology, meaning, cited sources (Hübschmann, Bailey, Olsen), and descendants. Quote exactly."
}
```


### [2026-09-14T03:12:50.685Z] TOOL RESULT

```
Web search results for query: "Persian tālār "hall" etymology Parthian talawār Armenian taławar Middle Persian"

Links: [{"title":"տաղաւար - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B2%D5%A1%D6%82%D5%A1%D6%80"},{"title":"Talar","url":"https://en.wikipedia.org/wiki/Talar"},{"title":"تالار - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D9%84%D8%A7%D8%B1"},{"title":"Talar (disambiguation)","url":"https://en.wikipedia.org/wiki/Talar_(disambiguation)"},{"title":"Parthian language","url":"https://en.wikipedia.org/wiki/Parthian_language"},{"title":"Persian language - Wikipedia","url":"https://en.wikipedia.org/wiki/Persian_language"},{"title":"-shat","url":"https://en.wikipedia.org/wiki/-shat"},{"title":"Talar","url":"https://grokipedia.com/page/talar"},{"title":"What does TALAR mean?","url":"https://www.definitions.net/definition/TALAR"}]

Based on the search results, here's what I found about the etymology of Persian tālār:

The Persian word tālār (hall) is cognate with Manichaean Middle Persian tlwʾr (talawār, "hall, tabernacle"), and the Armenian form taławar derives from Parthian talawār meaning "hall, tabernacle".

The word possibly ultimately derives from Proto-Indo-European *trab-, *treb- ("dwelling, room"). This suggests a deep etymological connection across multiple Iranian language branches, with the word being inherited or borrowed among Parthian, Middle Persian, and eventually modern Persian, while also entering Armenian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-14T03:12:54.740Z] TOOL RESULT

```
# Old Armenian Entry: տաղաւար (taławar)

## Etymology
The term derives "From Parthian _𐫤𐫓𐫇𐫀𐫡_ (tlwʾr /⁠talawār⁠/, 'hall, tabernacle')." It compares to Persian _تالار_ (tâlâr, "hall, saloon").

## Meaning
The word signifies "tent, tabernacle, booth, cottage"—structures for shelter or gathering.

## Cited Sources
The entry references several etymological authorities:

- **Ačaṙean** (1971–1979): Consulted in the _Armenian Etymological Dictionary_
- **Awetikʻean, Siwrmēlean, and Awgerean** (1836–1837): Listed in the _New Dictionary of the Armenian Language_
- **Olsen, Birgit Anette** (1999): Her work on "The noun in Biblical Armenian" appears relevant to "origin and word-formation" analysis

## Descendants
The word evolved into:
- **Modern Armenian**: տաղավար (taġavar)
- **Aghwan**: 𐕜𐔰𐔾𐔰𐕛𐔰𐕙 (ṭalavar)
- **Old Georgian**: ტალავარი (ṭalavari)
```


## [2026-09-14T03:13:03.191Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A4%BE%E0%A4%B2",
 "prompt": "Give the Sanskrit entry for ताल (tāla): etymology (any Dravidian origin, Mayrhofer), and meanings. Quote exactly. Is it a palm tree (Borassus flabellifer) or a vine?"
}
```


## [2026-09-14T03:13:05.032Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/teh%E2%82%82l-",
 "prompt": "Give the reconstruction page for PIE *teh₂l-: meaning, descendants, and any note about which forms belong. Quote exactly."
}
```


### [2026-09-14T03:13:06.247Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T03:13:09.366Z] TOOL RESULT

```
# Sanskrit Entry for ताल (tāla)

## Etymology
According to the Wiktionary entry, Sanskrit ताल is "Borrowed from Dravidian; ultimately from Proto-Dravidian *tāẓ." The document notes Mayrhofer's etymological dictionary as a reference source.

## Primary Meaning
The main Sanskrit definition states: "the palm tree, palmyra tree, or fan palm (Borassus flabelliformis, producing a sort of spirituous liquor)."

The entry specifies **Borassus flabelliformis** (fan palm), not a vine. This is a palm tree species that produces toddy, a fermented beverage.

## Additional Meanings
Other Sanskrit senses include:
- The nut of fan palm
- Toddy (the beverage)
- A fragrant earth

The document consistently identifies ताल as a palm tree across multiple language entries and derived words.
```


## [2026-09-14T03:13:19.905Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"talea\\|tälea\\|talca\" LEW_1910.txt | head -10; echo \"== WEB files ==\"; ls | grep -i \"^WEB\""
}
```


### [2026-09-14T03:13:19.973Z] TOOL RESULT

```
== WEB files ==
WEB_vol1.txt
```


## [2026-09-14T03:13:23.780Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30095,30110p' FSD_vol4.txt"
}
```


### [2026-09-14T03:13:23.844Z] TOOL RESULT

```
silicate  (HiMgiSiiOu),  crystallizing  in  the  orthorhom-  talcs'mant.— tale'tell^lng,  c   An bic  or  monocUnlc  system  Different  varieties  are  called  tale'vrlse.  1   tei'wolz,  2   tfil'wls,  ede  In  the  manner  of  a   tale poisUme,  rensselaerite,  soapstone,  steatite,  agalUe,  etc  Talc  Tal'fourd,  1   tol'fdrd,  2   tarford  Thomas  Noon  (»/al795- when  powdered  Is  extensiv  ely  used  in  making  lubricators,  V«18S4)  An  English  lawyer,  dramatist  and  essayist  ber'- toHet»powders,  etc  and  in  solid  slabs  for  hearthstones,  etc  geant  TalTourdJ.
2>  (1)  [CoUoq  1   Mica  (2)  A   mica  slide  for  micros-  1   t€'lal  2   ti'U,  n   Rlural  of  talus copy  [F  ,   <   Ar  falff,  talc  1   talckt —Indurated  talc,  fall^  1   ta'U  2ta*lj,  n   IE  Ind)  Same  as  tahli an  Impure  hard  slatj’  varietj  of  talc  talc'*slatc^t.— Ta"lTi,  1   toll',  2taTi',  n   A   city  In  Yimnan  province,  W. oil  of  t.t>  see  OIL  —   talc'sschlst",  n   Geol  A   schistose  China
rock  containing  considerable  talc  Much  of  the  schist  so  TaT'Ia-co'tlan.l  taTya-kfi'^an,  2tM  ya-cS'shan  a   Named called  In  the  older  works  Is  sericlte  or  hydro*mlca  schist,  after  the  Bolognese  surgeon  TaUacotlus  or  Tagllacozzl
(1546-*V7l599)  Tagl"la-co'tlant —Tallacotlan  opera- tion (Surff),  an  operation  In  plastic  surgery,  for  forming  a new  nose,  which  consists  la  paring  the  surface  to  which  the new  nose  Is  to  be  attached  and  unlilng  It  to  a   flap  taken  from the  arm,  hut  not  entirely  se\  ered  until  union  has  taken  place By  the  Hindu  method  the  graft  la  taken  from  the  forehead TaTla-fcrro,  1   telWer.  2   tal'i-ver.  n   1   William  Booth
talc-schist  la  not  common  talcose  schlstj.— tal^-co- chlo-rit'lc,  a   Containing  both  talc  and  chlorite,  as, talco^ehlortitc  schist  taF'co-chJo'rlfcf  —   taT'co-ml-ca'’- ceous,  a   Consisting  of  both  talc  and  mica Tal'ca,  1   tol'ka,  2   tal'ca,  n   1.  A   province  In  central  Chile 3   839  sq  tn.  2.  Its  capital  [See  gum
taVca*gum'',  1   tal'ka  gom’,  2   tfil'ca-gflm’,  n   Gum  sav  akin
[name be  Chinese I   A   fan* leav  es  arc
used  by  the  natives  for  writing  upon,  and  hence  the  tree  Is
’Tal-cher’,  I'tfii^eri,  2   lal-ch6r’,  n   1’  A   native  state  In  0VtslS22-VjTl898),  an  American  malor-general  In  the  Con- Bengal  province,  India  319  sq  m.  2   Its  capital  federate  Army  defended  Fort  Wagner  2.  A   county  in
talc'lte,  1   talk'oic,  2   tilc'it,  n   Mineral  1.  A   scaly  N   E   central  Georgia.  193  sq  la  .   county-seat,  Crawlord-
^ taai'an.I  fo-ir-on.  2tS'ir-Sn.n  [Boh]  1   An  old  Bobemlan
talSi'rTt^'.  Same  as  TAteosn  talc'yt.  SddK  aUeraatei  S'£dSe“  ^
talc'oid,  1   talk'eld,  2   t&lc'fild,  a   w-vvinff  thA  fnrm  nf  nr  _   IS  aiteniateiy  triple  mu  aupie  lu  j
pertaining  to,  talc Calc'ose,  i   Italk'Os, talc'ous,/ containing
“o  rauid  the  book.palm.  tal"f-e'ra.palm''t.
h,  Tnl'd-e'sln,  1   tal't-€  sut  2   tai'l-e  sin.  n   A   Cymric  bard  as-
```


## [2026-09-14T03:13:34.707Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3; echo ...; grep -n \"تلک\\|تَلک\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-14T03:13:34.785Z] TOOL RESULT

```
...
20706:اول بز تون آعده است:که تلکس باشد .
```


## [2026-09-14T03:13:37.519Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 BQT_v1_pages.txt; echo; echo \"=== formfeeds ===\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('pages',t.count('\\f')+1)\nimport re\nprint(re.findall(r'\\[pdf page \\d+\\]',t)[:5])\n\""
}
```


### [2026-09-14T03:13:38.990Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�
=== formfeeds ===
pages 777
[]
```


## [2026-09-14T03:13:42.026Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:509 2>&1 | head -60"
}
```


### [2026-09-14T03:13:43.070Z] TOOL RESULT

```
no scan of BQT covers printed page 509 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:13:45.183Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\" | head -60"
}
```


### [2026-09-14T03:13:46.215Z] TOOL RESULT

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


## [2026-09-14T03:13:51.983Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(733,742):\n    print('==== leaf',i,'(printed ~',i-228,') ====')\n    print(t[i][:900])\nEOF"
}
```


### [2026-09-14T03:13:53.110Z] TOOL RESULT

```
==== leaf 733 (printed ~ 505 ) ====
وکاف " بمعنی تکس است که نخم و امتخوان
انگور باشد . و بکسر اول هم آهمده است ۰
تکسل « بنتح اول و ثانی و سکون‌تالث
ولام ۰ بمعتی تکك است که دانه 1 هستةانگور
باشد .
لکسیی » بز وزن تسین » نام بزر کی
لس 8 بزرکان تر له 5
نکش ه بفتح اول رثانی بر وزن‌حش»
نام مکی از ملوك و سلاطین است ۴ - رتخداة
انگور راهم گفته‌اند و ٩‏
کل - بنتح اول و کسر ثانی و سکون
لام . گومفند شاخدار جدکی. زا گزنند - ویس
سادة تو خط را نیز گفته‌اند - و مردم ابله و بی
اندام را هم میگوند ۰ و تین اول نمز درست
ات .
تکله بشم اول بروزنعقله . نامهیکی
از انابکان است که در شیراز پادشاهی کردند ۴
- ودیوانه را نز گونند.
نگهاد » بر وزن و معنی تسار است»
وآن یری باشد بی پیکان و بجای پیکان کرهی
دارد 1
مخفف تکمار است؛ ران تیری باشد بی‌بسکان
و بجای پبکان آگرعن ازچوب با استخوان دارد.
۱ _ ظ, مصحف: تکن ( « .م ۳
خوارژشاه ( ۵۸ ۵45) است .
تکمهه س بنم اووسکون انی وفتح‌عيم
کوی کریبان و امتال آفراگویند..
تکند - بقتح اول بروزن کمند. آشيانه
مرغانرا کونند» وی
==== leaf 734 (printed ~ 506 ) ====
تکیز
اوواحت
کفده اند - وبکسراول لقمه و بارمای از هرچز
باشد ۱ چنانکه کویند *«فلانی چیز را نکه تکه
کرد » » یمنی پاره پاره ساخت ۴ .
لگیز - بر وزن تمیز » تخم واستخوان
انگور راگویند؟ .
تکین بر وزن زمین .نام بادشاهی‌بوده
است ۴ - و بمعنی زیرین هم همت 6 - و تخم
واستخوان انگور را نیز گویشدا .
لگ » بفتح اول وسکون‌انی » بمعنی
نه و پن و پایین باشد همچو ته حوض و ین چاه
وامثال آن۸ - وبمعنی‌دودن‌رنكودوه‌هست 4
وبوم و زمین را نیز گوبند - وفرباد کردن‌وبانگه
بلند وجار را نیز کفته‌اند - وبلفت زندوپازند(»)
خرهای رسیده باشد*۱.
کنند وآنرا بعربی قیف کویند - و زهین نثیب
پر سبزه وعاف را یز کوبندکهآب باران برآن
بدود وجابسا بماند - ونام روستابی است ازولات
کنجه۱۴- وجنگ و خصومت رانیز کفته‌انه -
وفام پرده ایست ازموسیقی۷۴.
تگا وه با واو . بر وزن ومعنی‌تگاب
است که زمین‌پست پ رآب‌وعلفت وظرف ی کهبصربی
قیف مبگویند - وجنکگ وخصومت - وروستابی
(۱) چك: حردحم.
ازچیز» استمال شود.
۴ - نیز بمعنی قطعه وجزئی
۴ - ترکی بمعنی خوش ثر کیب
==== leaf 735 (printed ~ 507 ) ====
یدای ‌-
از ولات کنجه - و پرده ای ازموسيقی‌باشد .
تگتارا . غتح اول و ای قرشت
بر وزن پرواز » ناختن و دویدن - و جتجو
کردن ماشه .
تگرگ؟ صبفتح اول و ثانی و سکون
رای فرشث وکاف فارسی ۰ معروف است که ژاله
وبخچه باشد - و بفتح دای فرشت بروزن‌نفزك.
تلای
یاه وی دبواررا گویند.
یگ - بفتح اول بر وزن حمل » قوچ
جاعه بثه کنند؟ .
تگمر م اول و فتح میم بس وزن
دختی » تیر تخمار است(۱) » وآن نبری‌باشد که
بجای پیکان کرعی از چوب دارد .
قل » بنتح اول وسکون ثانی , کوه‌یست
ويشتهة بلند راگویند؟ - و هرچیزی که برروی
هم ربخته خرمن کرده باشند - و کنابه از پس
امردمز لف‌ومضخم(۲) باشد» کوبندعربی‌است6 .
تلا توف بفتح اول وثانیبالف کشیده
وفوقانی بواو رسیده و بفا زده » شور و غوغا را
کویند - وکی را نیز کنته اند که خود را
وتفوها .
هر کجا ربدکی بود تگلم
چبر کین(۳) و بلید نگهدارد و از کثافت‌ونجاست
پرهیزنکند ومردم ازونفرت کنندلا .
اج بفتح اول بر وز نکلاح» بانگ
ومتغله وشور وغوغا وغلغله باشد » و باین ءعنی
لاس « بفتح اول بر وزن ممای ,
ن
==== leaf 736 (printed ~ 508 ) ====
تلاخان
قلاشان - با شین‌نفطه‌دار بروزن‌هراسان؛
نام مرغزارست بز ره در صفاهان٩‏ 3
کوند که درمیان فرح زنان است- وبمعنی یاچ
تنبان وشلوار عماهده است
قالالا ‏ بر وزن جلالا » نقش وصوت
و ۷ | گویند .
لا و 0 - بفتح اول ونون بروزن‌ادارج »
بانگگ ومشفله وشور 0 را گویند» وبکون
لون ِ است؟ .
تلیا ۴ با بای ابجد بر وژن حلوا ؛
عافت زند و بزند(۱) د.ه گوسفند و کار و امتال
آن باشد .#
تلج جکو ك س باخای قطه دار وجیم
وکاف و واو وکاف دیگر وحرکت حجهول . نام
کاسنی صحرابی‌است» ومعربآن طرخشقوق‌باشد,
و بعربی نید کویند .
تلخ جو لك » با جبم و اف بر وزن
گرم سود ؛ بمعنی تلخ جکوك است که کاسنی
صحرانی باشد ۰
(۱) چك: ژئذ ویاژند.
با هواس
تللخ عیشی ۰ کناه از کی است. که
آزاری ومکروهی ومصیبتی از حوادث رو زکار
یذو رسنده باشد .
تلخلت ح بر وزن زرواه . صتیر تلخ
باشد - و نام گیاهی است بغایت تلخ , و بسنی
گویند خربزة نلخ است که مربی حنظل
وقثاهء‌النمام خوانند. و بعضی کاسنی را گفته‌اند
و نام یکی از ظرفای سلطان محمود غزنوی
بوده -.
دناست .
ت
==== leaf 737 (printed ~ 509 ) ====
9 کین
0 هیرین نله » با نون بر وزن چرنده ۰ کچ
است٩‏ - و ثلق وزر ورق را ليز گویند » و طلق زبالرا گوشد بعنی شخص ی که درست تکلم قوادد
ممربآست - ولوعی از قماش هم حست - وبضم | نمود؟ * واو را جربی فأفاً خوانشد .
اول وسکون انی‌غلهای باشب کهآ ن را لوییاخوانند تلنگی ضتح اول و نون و سکون تالی
وبکسراول وفتحثالی‌جامة پیش‌واز وآستین کوتامرا +کاف . میوه ای بود شبیه بشفتالو - و نم اول
یند - و درخت سیب حمرایی را یذ | وکاف‌فارسی مروزن تفن , حاجت و ضروری-
کفته اند که بونانی زعرور و جمربی ذوئلاث | ومیل و خواهشس ویاز و آرزو باشد ۵ . چه
حبات و بثیرازی کیل و درخرامان علف شیران | تلشگی ییازمند وخواهش کننده را گویند و باین
خوانند؟ - وبکسر اول وسکون نانی » زنجبیل | معنی بر وزن خدیکه هم آمده اسکر. رخ یکی
تر و تازه را گونند .9 ید نت اه من واه
تلهی؟ - بنتع اول وسکون ثانی وم | وامتالآن - وخوشةٌکوچك انگور که برخوشة
مکسور شون رده پیش آ خعور و رالات زانگر کلان چسبیده بود - و بکر اود و قح ای
باشد بزبان زند و پازد (۱) و ب
==== leaf 738 (printed ~ 510 ) ====
وآن دارونی باشد شیرین و تون عون
شتر می‌شنند ۷ .
لنگی - بن اول وتح ای . لازمند
وخواعش کننده و کدا را گویند - و بکسرثانی
مخثف تولنگی است کسیان‌پاچه باشد - و کنابه
از سر امرد و خیم ومترش - وبی‌باك و خونی
- وتولی هم هست ۰
تلنه ینم اول وسکون انی و فتح
نون » بمعتی حاجت و خواهش ونیاز وضرورت
باشد ۴ .
تلو ح بفتح اول بر وزن زلو ۰ مطلق
خار را کوبند؟ - و منم اول پابین تبر باشد
اک و بان
و 0 و ی وت ۹ بچیزی
داشتن باشد؟ .
تلو سه ختح اول بر وزن وسوسه ۰
تعفف واه اآست که اشظرالب و مس فرازع
واندوه باشده - و بضم اول وثانی . غلاف کارد
و شمشیر و امثالآترا کونند » و باینممنی بفتح
اول بر وزن سبوچه هم بنظرآمده است - وبقتح
اول و ثانی , غلاف خوشةٌ خرما و غلاف دا
خرما را گونند - و تشه درودکربرا
گفته اند .
تلو 2 ه بنتح اول وضم ثاني و سکون
واوات
واو وکای ؛ شانهً تبر باشد که بعربی هدف
خوانند - وظرف و صراح ی که آنرا بصورت شیر
وگاو و حیوانات دیگر ساخته باشند و بدان
شراب خورند .
که سب ال وی دش سا
آنچه جاور در آن بقید درآی
==== leaf 739 (printed ~ 511 ) ====
قم ع بفتح اول دسکون ثانی ۰ آفنی
امت که در چشم پیدا میشود مانند پرده؛ وآ را
بعربی شاوه
تماجح نم اول بر وزن اعاج ۰
کي درازی را کویند که از پارچه دوزند وبا
از ابربشم بافند .
تماخره - بتح اول وخای نقطه‌دار
و رای بی نقطه . بمعنی‌هزلومزاح ومسخر کی
و ظرافت باشد - و بسکون خای نقطه دار هم
طبعی و غیرآن .
تهساشا؟ - با دار اف کنیده
«دبوان ناسر خسروص۹۵۹ مشون۱.
نظر کردن بچیزی باشد از روی حظ با ازروی
عبرت .9
آمام شدن - بسی باهبا رسیدن
کاری باشد - و کنابه از مردن و فوت شدن‌هم
هت .4 ۱
لهقم ه بنم حر دو فوفانی وج
تومیم , قطای ؟ باشد.وآن دم کاو کوهی‌است
سپاهیانآنرا از تیزه وعلمآویز ند وبر ۷2
بندند؟ - و یکسر هردو فوقانی بحربی سماقی را
گوین که درآش و طعام کنزر6 ۰ ۱
نمیا با خاو بای خن بر وزن مد
ولفة بمعنی بابکدیگر پیادمرفتن است,چون باران برای تفرحاکثر باهم پیاد‌سیر میکنند لهذا در
2
س رکرمی و مشفولی: هو بفرمود تاهمةٌ مطربان و مسض رکان و هزالان و سگان شکاری و بوزنه
وازین جنسپاکه تماشاء ملوك باشد . ازسرای خلافت ب
==== leaf 740 (printed ~ 512 ) ====
اي س
مر - و
قطه .آب مرواربد رااگوبند وآن علتین است که
بعضی از مردم را در سن چیل سالگی در چشم
بهم میرسد و چشم تاربکی میکند وییثایی ضان
می پذیرد د چون سن از پنجاء تجاوز نماید آن
علت بخودی خود برطرف گردد ؛ و بر اول
اول نیز باين ممنی بنظر آمده است؟ - و در
عربی خرما راکوبند - و بضم ثالی بزبان تو کی
آهن را کویند؟ - و بکسر اول و ثانی بزبان
علمی هند بمعنی تاریکی باشد که در مقابل
روشنی است  .‏ «-
نم قز لش هت بفتح اوز وکر ثانی
بکاف‌زده کلام خدا وفرآن مهد و گویند ۰
وضم انی‌هم گفته‌اند . گوبند ث رکی‌است.*
تمغو در با زای هوز بر وزن ححفوظ»
بیرامون دهان ومنقار مرغان باشده .
تملول - با لام بروزن مقبول» رستنیی
۱ رک*: تمنده 2
باشد خودروی شسه باسفناج » وآنرا در خراسان
بوضت و سربی قثاء دبری خوانتدا..
تملیت ‏ با تای فرشت بر وزن تمليكه
بار کوچکی باشد که بریار بز رکه بندند ‏ وکاه بر
مشت چاروااندازند ویر بالایآ نصوار شوند - ويك
لنکه بار رائیز گفته‌اند .
هی »بر وزن چمن » میغ راگویند ۰
وآن بخاری باشدتار مككسلاصق 
==== leaf 741 (printed ~ 513 ) ====
آمور ۱ -_بنتح اود و انی ءضوم
بواو وزای نقطه دار زده , کرمای سخت باشد -
و نام اه اول نابنتان - وماه دهم از سالرومیان
وبودن افتاب در برج سرطان .
تمو ك بفتح اول و ضم انی و سکون
ثالت‌وکاف » ۳
و تیرمرا نیز کفته‌اند که پیکان پهنی دارد وچون
شت با استخوان فرو رود بآسانی برتساید-
وهرچیزبرا لیز کویند که‌درچیزی‌رود که‌بر آوردن
آن دشوار باشد .
نمیته بفتع اول و کر انی هشدد
وسکون تحتانی مجهول وشن نقطه دار مفتوح »
نام شهری و «دینه ای باشد - و نام بشه ات
در تواحی شهرآمل که درمیان آملیان بشیمای
بیشه شهرت دارد۴
تمیلك بفتح اول بر وزن شربك ,
رستذیی باشد سرخ رنگه ونرش‌مزه» وبکسر اول
هم آمده است
محسوب میشد وهمی‌نام
عمر برف است و آفتاب نموز
۴ - پسرخواجه دست برد بکو
۳ «نمیشه هر کیست(از
آند کی مانده خواجه غره هنوز .
۱ سعدی شیوازی.
خواجه او را بزد بتیر نموه .
عمار؟ مروزی . «لفت فرس ۰۲۷ .
شه از صفحهٌ ۵۱۲
۷ - ببرهان نکو دانم اين سر درودن
۸ ره : تمنه.
وکیلان‌فراوان است
«نأسی ۱۷۳ *.
ستراباد راییئو .
الف:شاخه‌ومیوه: ب
```


## [2026-09-14T03:14:11.946Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زرورق\\|ورق را نیز\" BQT_v1_pages.txt | head -10; echo \"---\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\np=t[737]\ni=p.find('ورق را')\nprint(repr(p[max(0,i-300):i+200]))\n\""
}
```


### [2026-09-14T03:14:13.098Z] TOOL RESULT

```
---
'9 کین\n0 هیرین نله » با نون بر وزن چرنده ۰ کچ\nاست٩\u200f - و ثلق وزر ورق را ليز گویند » و طلق زبالرا گوشد بعنی شخص ی که درست تکلم قوادد\nممربآست - ولوعی از قماش هم حست - وبضم | نمود؟ * واو را جربی فأفاً خوانشد .\nاول وسکون انی\u200cغلهای باشب کهآ ن را لوییاخوانند تلنگی ضتح او'
```


## [2026-09-14T03:14:23.979Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -sL -o bqt509-495.jpg \"https://archive.org/download/borhan-ghate-v1/page/n737_w1400.jpg\" && file bqt509-495.jpg && ls -la bqt509-495.jpg"
}
```


### [2026-09-14T03:14:26.999Z] TOOL RESULT

```
bqt509-495.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
-rw-rw-r-- 1 sfmqrb sfmqrb 501912 Sep 13 23:14 bqt509-495.jpg
```


## [2026-09-14T03:14:30.506Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt509-495.jpg')\nw,h=im.size\n# crop top-right quadrant (RTL: first column is right)\nim.crop((int(w*0.45),0,w,int(h*0.45))).resize((int(w*0.55*0.7),int(h*0.45*0.7))).save('bqt509-495-tr.png')\nprint(im.size)\n\""
}
```


### [2026-09-14T03:14:31.802Z] TOOL RESULT

```
(2479, 3508)
```


## [2026-09-14T03:14:33.609Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt509-495-tr.png"
}
```


### [2026-09-14T03:14:33.631Z] TOOL RESULT

```

```


## [2026-09-14T03:14:57.798Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -sL -o bqt508-495.jpg \"https://archive.org/download/borhan-ghate-v1/page/n736_w1400.jpg\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt508-495.jpg'); w,h=im.size\nim.crop((0,int(h*0.55),int(w*0.55),int(h*0.95))).resize((int(w*0.55*0.75),int(h*0.40*0.75))).save('bqt508-495-bl.png')\nprint(im.size)\""
}
```


### [2026-09-14T03:15:00.307Z] TOOL RESULT

```
(2479, 3508)
```


## [2026-09-14T03:15:02.536Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt508-495-bl.png"
}
```


### [2026-09-14T03:15:02.556Z] TOOL RESULT

```

```


## [2026-09-14T03:15:19.299Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt508-495.jpg'); w,h=im.size\nim.crop((int(w*0.05),int(h*0.40),int(w*0.55),int(h*0.66))).resize((1000,int(0.26*h*1000/(0.50*w)))).save('bqt508-495-bl2.png')\""
}
```


### [2026-09-14T03:15:20.597Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:15:22.780Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt508-495-bl2.png"
}
```


### [2026-09-14T03:15:22.803Z] TOOL RESULT

```

```


## [2026-09-14T03:15:48.475Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/509.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 509 (archive.org borhan-ghate-v1, leaf n737) — read from the page image by Claude, page 495 verification]\n\nRunning head: - ۵۰۹ -\n\n(continuation, right column top, of the entry «تَلَک» whose headword stands at the foot of the left column of p. 508: «تَلَک - بفتح اول و ثانی و سکون کاف، کسی را گویند که سبلتش بسیار کنده و پر باشد، و درجای دیگر سبلت برکنده نوشته بودند بفتح بای ابجد و کاف، الله اعلم - و بفتح ...»)\n\np. 509: «... اول و سکون ثانی بمعنی تلخ بود که ضد شیرین است۱ - و تلق و زر ورق را نیز گویند، و طلق معرب آنست - و نوعی از قماش هم هست - و بضم اول و سکون ثانی غله‌ای باشد که آن را لوبیا خوانند، و بکسر اول و فتح ثانی جامهٔ پیش‌واز و آستین کوتاه را گویند - و درخت سیب صحرایی را نیز گفته‌اند که بیونانی زعرور و بعربی ذوثلاث حبات و بشیرازی کبل و درخراسان علف شیران خوانند۳ - و بکسر اول و سکون ثانی، زنجبیل تر و تازه را گویند.»\n\nThen: «تَلَمن۴ - بفتح اول و سکون ثانی و میم مکسور بنون زده، بینی آدمی و حیوانات دیگر باشد بزبان زند و پازند (۱) و بعربی انف گویند.»\n\nKey phrase for the verification: «و تلق و زر ورق را نیز گویند، و طلق معرب آنست» = \"they also call it telq and zarvaraq; and (Arabic) طلق ṭalq is the Arabicized form of it.\"\n\nAlso p. 508, Mo'in's footnote 5 (on تلخ) contains the Latin-script forms: «تلخی - حاصل مصدر از تلخ ... tâxlîk (در «بندهش ۴۸» بمعنی تلخی)، طبری tal ... پازندی و پهلوی tal ... (رک: تلک)».\nEOF\necho saved"
}
```


### [2026-09-14T03:15:49.461Z] TOOL RESULT

```
saved
```


## [2026-09-14T03:15:50.660Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page 15[0-9]\\]\" incoming/BQT/BQT_v3_pages.txt | head; echo ---; python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    n=m.group(1) if m else '?'\n    if n in ('152','153','154'):\n        print('=== pdf',n,'===')\n        print(p[:1500])\nEOF"
}
```


### [2026-09-14T03:15:51.709Z] TOOL RESULT

```
11142:[pdf page 150]
11218:[pdf page 151]
11300:[pdf page 152]
11349:[pdf page 153]
11422:[pdf page 154]
11502:[pdf page 155]
11559:[pdf page 156]
11631:[pdf page 157]
11721:[pdf page 158]
11765:[pdf page 159]
---
=== pdf 152 ===
[pdf page 152]
هو ات ۱ طولره

بروزن(۳) امواج» نام ولابتی‌است ات رکستان ۷.
‎clin’‏ خانه ۲ - ‎Salat‏

بوده: و بعضی گوبند نام پادشاهان تبت‌وبفماست.

طمع خام ‎ats»‏ از توق ‎oh‏
‏بچیزی است که ممکن‌الحصول باشد(۱).
طمغاج » بنتح ‎Jy!‏ و ‎ond‏ شلددار(۷)

بیان نهم

در طای بی نقطه با نون مشتمل برسه لغت
طنباك ۴ )8( = بنم اول وفتح بای‌ابجد ‎ub‏ ۴ » بر وزن کنجه , للم شهری
بر وزن اردك » ‎ples‏ باشد دم دراز که ‎LT‏ از است(۵) در جالب مقرب ‎Chay‏ بکوه قاف.

چوب و کاهی از سقال ‎wile 5a‏ و ‎AIL‏ طنطنه ‎oo‏ با طای ‎ge‏ بر وزن
و سرآوازه خوانان در زبر بغل گرفته لوازند | زیکنه » آواز رباب و بربط ورود و امثال آنبارا
وخوانند .۷ ‎aay‏ .

بیان دهم

در طای بی نقطه با واو مشتمل بر بیست وپنج لغت ‏ و کنایت

‎dl gh‏ - بر وزن ‎Lt‏ پیعنی‌بیش | گوند با ماه پروین در بیکجا روید لیکن تم
است» وآن بیخی باشد مانند ماء پروین ‎٩‏ . | قائل است.

‏(۱) چش : ‎(x) )( ash‏ چك : - شطه دار . (۳) چك : بوزن .

‏(4) چك : طنبکه . (ه) چش:شهراست

‎٩‏ - شفاج با «چونکدو» با ‎Gauls?‏ با «خان‌بالیغ» همان شهر پکن 0ات۲ ( پایخت
قدیم چین) است .(محمدگروینی) ‎By‏ تملیقات چهار مقاله طبع نگارنده (فهرست).

‎cab? nme ۴‏ خان» است « اغلب ملوث ‎Dg‏ ممروف بخایه که.فبل از مفول در
آن‌نواحی‌سلطنت لموده‌اند ملقب بطمناج غان بوده‌ادد واحتمال میف میرود که ممنی‌طمفاج‌خان»
خان ‎club‏ باشد» (چپارمقاله طبع ‎God‏ ص۹۳-۹۲ح).

‏۴ - رك ‎cds:‏ . ۴ - شهری برساحل بحر »غرب مقابل جز یرتالتضراه رك:
معجم البلدان ‎pulldss co gi? Tanger‏ دمشقی ‎of Lvit‏ شپر وبندری درمراکش » در
کنار ‎M5‏ چبل‌طارق , دارای ‎4٩۰۰۰‏ سکنه . - (عر) «طنطنه» بآواز آوردن تشت
وجزآن را - وحکایت آواز طنب
=== pdf 153 ===
[pdf page 153]
طوافص کش

طو اف سر کش - شخصیرا کوبنه
که ‎ogee‏ و امثال ‎OT‏ را برسر کرفته کرد کوچه
و بازار ‎th‏ یفروشد - و عس و شبرو را
لیر کوبند - و بمعنی دزد و راهزن هم آمده

است +

طور ’- ‎ce‏ اول و ‎sto‏ ورای
قرشت (۱) ؛ بمعنی طرز وروش و لوع ر قاعده
وقالون ‎ath‏ - و ‎gine:‏ حد وطرف هم آمده‌است
- و ‎pie‏ اول و ثالی مجپول » بمعنی وحشی‌است
که درمقابل رام ‎Pash‏ - وبائالی‌معروف‌ام کوهی
‎col‏ مشهور و عربی است ۴ .

‎gles gh‏ - با ‎Jb‏ ابجد بر وزن
دودمان » اسب و استر و شتر بزرکه بار کش
و رونده راکویند.

‏طور ‎TS‏ » بکرزای‌هوزوسکون
بای ‎hor‏ و بای ابجد بالف کشیده. نام کوهی‌است

‏(۱) چك : ورا .

‎VW

‏تزديك به بیت‌المقدس و مشرف بمسجد اقصی.
‎ls Toate‏ هفتاد هزار پیفمبر رحلت کرده‌اند
و عیسی علیه‌اللام ازآنجا بآسسان رفته است.

‏طور سقوس ‎ne‏ اول ؛ ‎wae‏
‏طرسیقوس است که نام زاهدی وحکیمیوپادشاهی
بوده از تساری .

‏طور ‎po Ve‏ سین , کوهی
است در حدود مصر تزديك بشهری که ما بين
شام و وادی قری است و محل مناجات موسی
‎Sede‏ بوده ؛ و ‎yen‏ کویند در صحرای تیه
باشد لرديك بشهر قلزم که بهایت دربای فاری
است .

‏طورك ۷ - بطم اول بروزن ‎thse‏
‏نام مپم-الار ضحاك ‎A‏ اسدی بوده .

‏طور هارون » کرمی ات که

‏۱-(عر) «طور بالفتح ‎LG‏ - صاری ومقابل چیزی- حدوقدر ولهات — ‎glade‏ و حد
فاصل ‎Ole‏ دو چیز - نوع و صنف - پیرامون چیزی گردیدن - ‎hog‏ شدن بچیزی »

‏«منتهی الارب > . ۴ سرك : تور .

‎pu ۴‏ چند کوه است و مشهور رین آنها

‏«طور سیتاء » ‎(pin)‏ است ‎Ay.‏ ممجم البلدان : طور ۰ طور سیناء .
۴ - مصحف ‎sgh?‏ زیتا» ‎Jalen)‏ وفتح چهارم) زتا بمعنی زیتون است ؛ نام کوهی‌نزديك

‎oe oly‏ مجاور قنطرءالخابور ؛ بربالای ‎OT‏ درخ
=== pdf 154 ===
[pdf page 154]
“Ve

هارون برادر موسی عایه‌اللام در آنجا مدفون
است ۱ .
طوری؟ = ‎ath‏ مجهول بر وزن (۱)
توری » ‎seer‏ رمید کی ووحشت باشد که لقیض
رام شدن وانس است.
‎gh‏ سك - با سین بی نقطه_ بر وزن
خوبك , توعی از خار است که آنرا بعربی
ش و کذالدراجین وخس ‎CEN‏ ومشطالراعی خوانند.
کوبند اکر قدری از کل ‎OT‏ بکوبند و در شیر
‎wl‏ شیر ‎ae‏ کردد و اکر بجوشانند و بر
۰ موضییکه خواهند قطم کردن ضماد کنند پیحس
گرداند .
طوط بر وزن لوط » بمعنی پنبه
باشك که بعربی قطن گوبند ۴ - ومرد دراز قد را
ی زکنته اند در عربی .
طو طاق اغر یوس * ‎dest=‏
‎AAT‏ و ‎Gli‏ زده و فتح همزه ‏ و کسررای

(۱) چك: بوزن .

Jt
‏زده»‎ Mtg ‏بوا و کشیده و بسین‎ glory ‏قرشت‎
‏بعربی‌حماش‌البری‎ OT ine ‏و‎ gly ‏لنتی است‎
‏باشد که حماض‌الیقروسلق‌بری‎ yey ‏است وآن‎
‏هم میگویند , وآتراحماش آغریون هم خوانشد‎

که بجای سین دون باشد .

‎Ve gh‏ © بر وزن خوبك .ناهمرفی
است مشهور بطوملی .۰

‎ay ‏نوش = نام دییراسکندر‎ Lb gb
‏و اورا در لشکر پادشاء زاگ بقتلآوردندوخون‎
. ۷ ‏ار را خوردند‎

‎va ‏بزیادنی تستابی‎ - sdb sb
‏همان طومایانوش است که دبیر ومنشی‎ , oy ‏از‎
‎. ‏سکندر باشد‎

‏طو طی صحر | - کنابه ازسبز4 محرا
است .
طوف « بر وزن صوف » زلیرا گونند
که بات پبر و کهنه شده باشد.*

‏۱ - کوهی است مرتفع مشرف در جهت قبلی ‎ce‏ المقدس و قبر هارون آمجاست .

‏« معجم‌البلدان © .

‏۴ -از:طور(ه.م) ج-ی(مصدری). ‏ ۴ - (عر) «طوط بالضم؛ ماربپنبه - مرو

‏بلندبالا- باشه - شب‌پرم خرد وریزه - مردسخت‌پیکار وخصومت ودلیر- گشن نیزشهوت. اطواط

‎+ ‏«منتهی‌الارب»‎ oe
Cpe) ‏نرتك‎ = ۷

‎coton = ۴‏ (فر) «لك ۲ س 4۱۹

‏۵ - رك : افربوی .

‎nas ۷‏ طوطیان ‎purl)‏ سخن‌پروری طوطیالوش‌دا
```


## [2026-09-14T03:16:02.616Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'طلق' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('pdf',m.group(1) if m else '?', '| count', p.count('طلق'))\nEOF"
}
```


### [2026-09-14T03:16:03.798Z] TOOL RESULT

```
pdf 11 | count 1
pdf 15 | count 1
pdf 27 | count 1
pdf 42 | count 2
pdf 54 | count 2
pdf 55 | count 1
pdf 57 | count 1
pdf 60 | count 1
pdf 80 | count 1
pdf 81 | count 1
pdf 83 | count 1
pdf 86 | count 1
pdf 93 | count 1
pdf 127 | count 1
pdf 151 | count 3
pdf 157 | count 1
pdf 163 | count 1
pdf 169 | count 1
pdf 190 | count 1
pdf 217 | count 1
pdf 220 | count 1
pdf 236 | count 1
pdf 254 | count 1
pdf 255 | count 1
pdf 262 | count 1
pdf 285 | count 1
pdf 296 | count 1
pdf 337 | count 1
pdf 353 | count 1
pdf 354 | count 1
pdf 355 | count 1
pdf 373 | count 1
pdf 376 | count 1
pdf 388 | count 2
pdf 390 | count 1
pdf 391 | count 1
pdf 410 | count 1
pdf 425 | count 1
pdf 426 | count 2
pdf 433 | count 1
pdf 447 | count 1
pdf 450 | count 1
pdf 455 | count 1
pdf 460 | count 2
pdf 468 | count 2
pdf 477 | count 1
pdf 480 | count 1
pdf 496 | count 1
pdf 498 | count 1
pdf 512 | count 1
pdf 515 | count 1
pdf 538 | count 1
pdf 552 | count 1
pdf 559 | count 1
pdf 571 | count 1
pdf 587 | count 1
pdf 597 | count 1
pdf 600 | count 1
pdf 602 | count 1
pdf 609 | count 1
pdf 633 | count 1
pdf 651 | count 1
pdf 652 | count 2
pdf 659 | count 1
pdf 661 | count 1
pdf 664 | count 1
pdf 694 | count 1
```


## [2026-09-14T03:16:06.733Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and m.group(1)=='151':\n        print(p)\nEOF"
}
```


### [2026-09-14T03:16:07.985Z] TOOL RESULT

```
[pdf page 151]
طلحند = یفتح اول‌وحای بی‌نقطه‌بروزن.:

فرزدد , نام پادشاه عندوستان است که از مردم
چین شکست خورد و ‎cosy OT Lab‏ فیل‌جان
داد ؛ و ‎aS gen‏ از برادر خودشکت بافت:
و جمعی )6 بآ نند که سکندر او راشکست‌داد
و مادر او از فراق او بیطاقتی میکرد؛ مصه‌بن
داه رکه .یکی از حکمای هند ‎oy‏ بجهت سکن
‎gl‏ شطرنح را وضع کرد و درمجلس اومیباخت ‎We‏
‏او مشفول شود وازآن اندوه بازآید.

طلق » ‎ca‏ اول وسکون ‎Il‏ وقاف +
کرهری باشدکالی. کوبند ه ‎Sou‏ کرد آنرا
بربدن مالد آتش بر بدن اواثر نکند ۱ وبعربی
ک وکپ‌الارش خوانند - و بکسر اول ؛ درعریی

بیان

—\tea—

بمعتی حلال باشد که در ‎ly‏ حرام است ۴ -
و ‎eet‏ آزاد هم هنت که در مقابل بنده
باشد ۴ .

طلق وان » بکس قان ‎Habs,‏
‏شراب است وبعربی خم رگوشه .

طلل = بر وزن غلل « بمعنی نان سرا
و عمارت خراب باشد ۴ - و تن و بدن ‎wil‏
‏و حیوانات دیگر را یز کنته اند ۵ . و کوید
عربی است. ۱

طلیسا ۱ = بنتح او و سکون ثالی
و تحتالی بالف کشیده , لوعی ازصدف باشد وآن
کوچك میشود . تمك سود کرده بانان خورند.

هشتم

در طای بی‌نقطه با میم مشتمل بر پنج لفت و کذایت

ظمر | - با رای بی ‎abit‏ بروزن حلوا .
بید انجیر را گوشد ۷ , وآن دانه‌ای ‎ash‏ که‌از
‎Ol‏ روف نگیرند ۰ وعربی خروم خوانند .

() چس: بمطی .

طهطراق ۸ ‎cao‏ هر دوطای‌حطی,
بمعنی طاق و ترلب است که کروفر و خودلمایی
‎acl‏ .

= tale ‏ممرب « لك » فارسی «اقرب الموارد» ؛ ازعربی وارد فرادوی شده‎ - ٩
: ۰۲-۱ ‏(فر) «لك۲ ص ۰۸۱4 < شب الذخاثر‎ mica = amiante

تا مگر ‎glk‏ پوشی جدم

۴ - )4 منتپی الارب » اقرب‌الموارد .
۴ -(مر) «طلل محر ‎AS‏ انر سرای وجای خراب شده»
6 - (عی) ومنه : ‎Sle‏ طللك . ای ‎Chant‏ «منتهی‌الارپ *:

ر: م:تهی الارب » آفرب‌الموارد .

« منتهی ‎COM‏ .
کوی برده زهم‌تکان ‎aS) ALL‏ خر)

" طلق ریزد بر ‎pee AT‏
‎alles‏ کنجوی. « کنجینه ۱۰۹ *.

۴ - طلیق (عر) بدین معنی است .

برده ‎SS‏ از همه تن شکفلش.

‎pile >‏ کنجوی . هفت پیکرچاپ ارمغان ۷۲ ۰ .
۱ - مسحف «طلینا» درسوربه ‎Sb)‏ . در عصر «دلیشی»  ‎tellime‏ (فر)؛لوعی‌صدف

‎. ۲ : ‏ص۵۸‎ t ‏ص 8۱۷ «دزی‎ yee

‎Ticin = ۲‏ (فر) «لك۲ س ۰4۱۸ « دزی

‏ج ۲ ص ۲۰ . ۸ - ‎gi‏ اول وسوم ؛ عربی است .

‏(برهان فاطع ‎(We‏
```


## [2026-09-14T03:16:33.527Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'تالار' in p or 'تالاد' in p or 'قالار' in p:\n        print('leaf',i,'printed ~',i-215)\n        for ln in p.split('\\n'):\n            if 'الار' in ln: print('   ',ln.strip())\nEOF"
}
```


### [2026-09-14T03:16:34.572Z] TOOL RESULT

```
leaf 639 printed ~ 424
    کول - بروزن قبول » تالاری باشد که
leaf 643 printed ~ 428
    رسیده و بکاف زده, غرفه و مخارجه و تالاری که
leaf 688 printed ~ 473
    تالار
```


## [2026-09-14T03:16:47.655Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[688][:1800])\""
}
```


### [2026-09-14T03:16:48.633Z] TOOL RESULT

```
تالار
تالاد ۱ «بروزن سالاژ» نختی ما خانه‌ای
باشد که بر بالای چهارستون با یشثر از چوب
و نخنه سازند ۰
میوه‌ایست شبیه بشفتالو ۴ .
تالا نه بروزن کاشانه ۰ نوعی ازشفتالو
ند و حضیکویند میوماست قبیه بعجو ۳ .
تالسقیر- بکسر الك و سکون سین‌بی
نقطه و فاف بتحتانی کشده برای فرشت زده ؛
بیونانی تخم سپند است که آن خردل فنارسی
باشد - و نخم تره تیزله را نیز گوبند ؛ و این
لفت در چندنسخه صحاح الادوبه چنن بودیکن
در اختیارات ‏ تالبسیقیر توشته اند باسین
و تحتانی دیگر وا اعلم هُ
قالش ح بروزن بااش . فومی باشند از
مروم کیلان ه .
تالعی- بسکون ثاك و کاف بتحتانی
کشیده , کثنی زکوهی وصحرایی را گویند .
تالمن؟ - بسکون الث و کسر میم
ونون ساکن» باغت زنسویازند (۱) جاتورست که
(۱) چك: ژند ویاژند .
در گاکی 5۳414021
<<
آنرا رویاه خوانند .
تا لو اسه- بسا واو بر وزن شاععاسه »
بی قراری و بی آرامی و اشطراب واندوه ۷ -
ومیل بچپزی کردن باشد .
تال‌ومال۸ « باهیم بروزن دال وذال»
این لفت از انباع است بمعنی ریزه ریزه شده
و آزهم ریخته ویاشیده ومتفرق وپربشان گردیده
باشد ٩‏
۵9 ه بر وژن جلم ۰ به‌عثی بسیار کم
و ,غایت اندك باشد - و با تشدید آخر در عرهی
یمعثی تمام است.
تام ول بروزن شاقول بر کی باشد که
آن رادر عندوستان بافوفل واه خورندرلبهارا
بدان سرخ ساژند ۷. .
ان بسکون نون, بمعنی دمان باشد که
بعربی فم خوانند وبعضی اندرون‌دهن را گفته‌اند-
- و تار را نیز کویند که شض پود باشد -
ورشته‌ای چند(۲)را هم میگوین که جولاهگان
از بپنای کار زناده آورند و آن دا بافند ۷۱-
وضمیر مخاطب و جمم مخاطب هم‌هست» همچو
۴ بر :؛ :الانه .
۶ اختارات بدسمی» است .
تألیف وی» دفتر ,یکم.
۷ مرمرا ای دروفگوی ست رکه
۸ -ممدال 0 تار ومار.
* - نهمتن بزابستانست وذال
ی رژگ: تانمول ۰
تالواسه گرفت ازاین‌ترفند. خفاف.
مسقل ۷ لغت فری 1۰ءِ*- رژد: نلواسد.
شردکار ابران همه تال‌ومال. فردوسصی طوسی.
```


## [2026-09-14T03:17:01.935Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -sL -o bqt460-495.jpg \"https://archive.org/download/borhan-ghate-v1/page/n688_w1400.jpg\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt460-495.jpg'); w,h=im.size\nprint(im.size)\nim.crop((int(w*0.45),int(h*0.03),w,int(h*0.30))).save('bqt460-495-a.png')\nim.crop((0,int(h*0.62),w,int(h*0.95))).resize((1200,int(0.33*h*1200/w))).save('bqt460-495-fn.png')\n\""
}
```


### [2026-09-14T03:17:05.068Z] TOOL RESULT

```
(2479, 3508)
```


## [2026-09-14T03:17:07.586Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt460-495-fn.png"
}
```


### [2026-09-14T03:17:07.606Z] TOOL RESULT

```

```


## [2026-09-14T03:17:24.187Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/460.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. ~460 (archive.org borhan-ghate-v1, leaf n688) — read from the page image, page 495 verification]\n\nHeadword (col. 1): «تالار۱ - بروزن سالار، تختی یا خانه‌ای باشد که بر بالای چهارستون یا بیشتر از چوب و تخته سازند.»\n\nMo'in's footnote 1 (foot of the page): «۱ - گورانی tâlâr «کردی ۲۱»، گیلکی tálár، گیلکی shálának.»\n(i.e. Mo'in gives only Iranian dialect cognates — Gurani tâlâr, Gilaki tálár / shálának — and offers NO Indo-European root, no Latin or Armenian comparison.)\n\nNeighbouring footnotes on the same page, for orientation: «۶ - حز. tâlm(a)n، پهلوی rôpâs، روباه، «پوکنر ۱۱۹».» / «۱۱ - از ریشهٔ اوستایی tan (تنیدن). رک: تانه و تونه.»\nEOF\necho ok"
}
```


### [2026-09-14T03:17:24.240Z] TOOL RESULT

```
ok
```


## [2026-09-14T03:17:25.091Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=talc",
 "prompt": "Quote the American Heritage Dictionary entry for talc, especially the bracketed etymology."
}
```


### [2026-09-14T03:17:27.918Z] TOOL RESULT

```
# Talc Etymology

According to the American Heritage Dictionary, the word "talc" originates from multiple language sources:

"[French, from Medieval Latin _talcum_ and Old Spanish _talco_, both from Arabic _ṭalq_, from Persian _talk_.]"

This bracketed etymology traces the term backward through Romance and Semitic languages to its Persian root.
```


## [2026-09-14T03:17:32.948Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%B7%D9%84%D9%82",
 "prompt": "Quote Mo'in's (فرهنگ معین) entry for طلق, including any origin tag in brackets such as [ع.] or [فر.]."
}
```


## [2026-09-14T03:17:34.550Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D8%A7%D9%84%DA%A9/",
 "prompt": "Quote the فرهنگ معین section for تالک, including any bracketed origin tag such as [فر.] (French)."
}
```


### [2026-09-14T03:17:36.121Z] TOOL RESULT

```
# Mo'in's Dictionary Entry for طلق

According to the Mo'in Dictionary (فرهنگ انتشارات معین), the entry states:

"(طَ) [معر.] (اِ.) معرب تلک ؛ سنگی معدنی که به رنگ سفید نقره ای شفاف و براق و قابل تورق است"

This indicates that طلق is a Arabicized term (معرب) derived from تلک, referring to a mineral stone characterized by a white-silvery, transparent, lustrous appearance with the ability to be split into sheets.
```


### [2026-09-14T03:17:38.803Z] TOOL RESULT

```
I've reviewed the web page content provided, but I cannot find a "فرهنگ معین" (Farhang-e Moein) section for the word تالک (talc) in the material shared.

The page includes definitions from several sources:
- لغت نامه دهخدا (Dehkhoda Dictionary)
- فرهنگ فارسی (Farhangi Farsi)
- فرهنگ عمید (Farhang-e Amid)
- گویش مازنی (Mazani Dialect)
- دانشنامه آزاد فارسی (Free Persian Encyclopedia)

However, there is no distinct "فرهنگ معین" entry visible in the content provided. The page does mention that the Abadis dictionary includes "فرهنگ معین" among its resources, but the specific entry for تالک from that particular source is not included in this excerpt.
```


## [2026-09-14T03:17:44.798Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%AA%D8%A7%D9%84%DA%A9",
 "prompt": "Quote Mo'in's (فرهنگ معین) entry for تالک, including any bracketed origin tag such as [فر.] (French)."
}
```


### [2026-09-14T03:17:45.916Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T03:17:46.307Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B7%D9%84%D9%82",
 "prompt": "Give the Arabic entry for طلق, especially any sense 'talc/mica' and its etymology (Persian talk?). Also any Persian entry for طلق. Quote exactly."
}
```


### [2026-09-14T03:17:52.750Z] TOOL RESULT

```
# Arabic Entry for طلق (Talc)

## Noun Definition
"**طَلْق** (ṭalq) m: 1. talc, talcum. Alternative form: تَلْك (talk)"

## Etymology
"Borrowed from Persian تلک (talk)."

## Additional Information
The entry includes a historical quotation from Ibn al-Baytar (1248) describing talc as "حجر براق يتحلل إذا دق إلى طاقات صغار دقاق" (a shiny stone that dissolves into small fine layers when broken).

The Wiktionary page also documents descendants showing how the Persian-origin term spread to European languages through Medieval Latin (talcum) and Middle French (talc), eventually reaching English, German, Polish, Russian, and Ukrainian.

**Note:** The webpage does not contain a separate Persian entry for طلق; it only documents the Arabic borrowing from Persian talk.
```


## [2026-09-14T03:17:59.957Z] TOOL CALL #74: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/talc\" \\\n \"https://www.etymonline.com/word/talc\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D9%84%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/talea\" \\\n \"https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B2%D5%A1%D6%82%D5%A1%D6%80\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A4%BE%E0%A4%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%B7%D9%84%D9%82\" \\\n \"https://www.ahdictionary.com/word/search.html?q=talc\" \\\n \"https://vajehyab.com/moein/%D8%B7%D9%84%D9%82\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 495 (roots Tâl, Talk): verification of talc chain / tālār / tāla\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T03:18:03.637Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/adf14f40cc5cb428.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/325e77b64973106a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5594ea4c1f84d178.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ad32bc0970b3c5b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b8443a3380396f59.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84a539100a0bc435.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6cff3d67bdc43194.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/87a102a606da0356.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1c578009874821dd.txt
```


## [2026-09-14T03:18:12.406Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD watkins talea/tal ==\"; grep -n \"talea\\|tālis\\|tālī\" AHD_watkins1985.txt | head -5; echo \"== PHD tālār ==\"; grep -n -i \"tlwl\\|tālār\\|talar\" PHD.txt PHD_mackenzie.txt | head -5; echo \"== NYB ==\"; grep -n -i \"tālār\\|talar\\|tlwl\" NYB_vol2_glossary.txt | head -5; echo \"== SOD ==\"; grep -n -i \"talar\\|tālār\" SOD.txt | head -5; echo \"== CHEUNG ==\"; grep -n -i \"tālār\" CHEUNG.txt | head -3; echo \"== BRT ==\"; grep -n -i \"talar\" BRT.txt | head -3"
}
```


### [2026-09-14T03:18:12.546Z] TOOL RESULT

```
== AHD watkins talea/tal ==
== PHD tālār ==
== NYB ==
== SOD ==
== CHEUNG ==
== BRT ==
25639:—  giusca  'va  dami-datS  Yt74.S4;  — gsus  *van»m  asavatum  alaAe  ratüm  G. 4.b\  —  gSus  Auüih^As  'vatvm  5,2.14, Y.  16.  4,  26. 4;  —gfus  hiäiänhS  'une  FrW. 6',  I  ä ;  —  gaom  ''  afüBJstoAe  'uns . .  gaom  " pauru.sar^aAe  'itnS  fravahm  S.2.  la;  — (äj  at  yatamaidl g!ul 'varumca  talaramiä Y.^g.i;  —  gsu/ tasne  gJu/ 'utu  S.j.14, Y.1.3,  jo.i,  FrW.  6.  i^;  —  gSusca  lasnl g^sca  'uns  Vr.5.  5.
```


## [2026-09-14T03:18:20.094Z] TOOL CALL #76: WebSearch

```json
{
 "query": "حسن‌دوست ریشه‌شناختی تالار پهلوی tālār ریشه"
}
```


### [2026-09-14T03:18:25.986Z] TOOL RESULT

```
Web search results for query: "حسن‌دوست ریشه‌شناختی تالار پهلوی tālār ریشه"

Links: [{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"فرهنگ ریشه‌شناسی فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه شناختی فارسی، دکتر محمد حسندوست","url":"https://ariabod.blogfa.com/post/92"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"}]

I've performed the web search for your query. The search results relate to Mohammad Hassan Doost's Etymology Dictionary of Persian Language (Farhang-e Riše-šenāxti-ye Zabān-e Fārsī), which was published in five volumes from "A" to "Y" in spring 1394 (2015).

The results include information about this comprehensive etymological dictionary project, but they don't contain specific information about "Tālār Pahlavi" (تالار پهلوی) or its etymological roots from Doost's work. The search results mainly discuss the dictionary itself and its publication history rather than specific etymological entries.

If you're looking for information about a specific word's etymology or a particular section of Doost's dictionary, you may want to try a more targeted search or consult the dictionary directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:19:02.565Z] TOOL CALL #77: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T03:19:02.609Z] TOOL RESULT

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


## [2026-09-14T03:19:10.529Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFM (الطلق) ==\"; grep -n \"الطلق\\|طلق )\\|( الطلق\" AFM_pages.txt AFM.txt AFM_alt.txt 2>/dev/null | head -10; echo \"== AFA ==\"; grep -n -i \"talq\\|Talk\" AFA.txt | head -5; echo \"== HJB ==\"; grep -n -i \"talc\" HJB.txt | head -5; echo \"== DOZ ==\"; grep -n -i \"talc\\b\" DOZ.txt | head -5"
}
```


### [2026-09-14T03:19:10.637Z] TOOL RESULT

```
== AFM (الطلق) ==
== AFA ==
== HJB ==
9586:"Public  servants  as  follows: — ^1  Vakeel , 2  Moomheei,  4  Chcbdars,  2  Jemadars,  20 PeoMy  10  Muttalckeety  12  Bearers,  2  Ohowry Bearers,  and  such  a  number  of  Frosts  and Lascars  as  he  ma^  have  occasion  for  remoT- ing  his  tents." — ui  Long,  406.
== DOZ ==
```


## [2026-09-14T03:20:04.617Z] AGENT

Now I'll write the verification file.


## [2026-09-14T03:26:29.038Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-495.json <<'JSONEOF'\n{\n  \"pdf_page\": 495,\n  \"book_page\": 465,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 2,\n      \"root\": \"Tâl\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *tāl- (*teh₂l-) 'to grow, sprout; growth, young shoot' (Pokorny 1055 = Walde-Pokorny I 705)\",\n      \"note\": \"The root box itself is real and the two citations are exact: Pokorny IEW 1055 has 'tāl- „wachsen, grünen; Gewächs, junger Trieb\\\"' and Walde-Pokorny I 705 has the same lemma with the same gloss. The LANGUAGE label (Indo-European) is right. The GLOSS is where Nourai departs from his sources: Pokorny/WP give only 'to grow, green; plant, young shoot'; 'twig, wood, a piece of wood used as a unit of length' is Nourai's own extension, evidently read back from Lat. tālea 'rod, stake' and from Bailey's Khotanese material, and is not in either cited page. The root is also contested: Ernout-Meillet (LAT s.v. talea) reject it outright — 'L'indo-européen n'admettant pas de racines de la forme *tal-, les rapprochements proposés ... sont à écarter ... Terme technique, sans doute emprunté' — and Wiktionary notes the traditional *teh₂l- derivation of talea 'has been questioned'. Watkins/AHD's IE appendix does not list the root at all. Of the four daughter nodes only the Latin one is actually in the cited pages: the Persian and Armenian words come from Bailey (ISS/KT VI 87-8, = DKS 123-4), where they are grouped under a Khotanese base tal- 'hall' with no link to Pokorny's 'grow' root, and the Sanskrit word is in WP I 705 but glossed 'Weinpalme' (toddy palm), not 'vine'.\",\n      \"note_fa\": \"ریشهٔ *tāl- واقعاً در پوکورنی ص ۱۰۵۵ و والده‌ـ‌پوکورنی ج ۱ ص ۷۰۵ با معنی «روییدن، سبز شدن؛ رستنی، جوانهٔ نورس» ثبت شده است، پس برچسب زبانی (هندواروپایی) و خودِ ریشه درست است. اما معنایی که نورایی می‌آورد («چوب، شاخه، قطعه‌چوبی که واحد اندازه‌گیری طول بوده») در هیچ‌یک از آن دو صفحه نیست و افزودهٔ خود اوست که از معنی لاتینی tālea «چوب‌دستی» بازخوانده شده است. افزون بر این، ارنو و مه‌یه در ریشه‌شناسی لاتینی این ریشه را یکسره رد می‌کنند و می‌گویند هندواروپایی ریشه‌ای به ساخت *tal- نمی‌پذیرد و tālea اصطلاحی فنی و به‌احتمال وام‌واژه است؛ واتکینز نیز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage چنین ریشه‌ای نیاورده است. از چهار شاخهٔ نمودار تنها شاخهٔ لاتینی در منبعِ استنادشده هست؛ «تالار» فارسی و talauar ارمنی از بِیلی گرفته شده که آن‌ها را زیر ستاکِ ختنی tal- «تالار» می‌آورد و هیچ پیوندی با ریشهٔ «روییدن» پوکورنی نمی‌زند. بنابراین ادعای نورایی در کلیت با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/talea\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1055\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 298 (printed p. 1055, running number '1055' visible in the leaf): 'tāl- ,wachsen, grünen; Gewächs, junger Trieb'. Gr. τᾶλις -ιδος ,junges mannbares Mädchen, Braut', τῆλις ,Hülsengewächs, Bockshorn', τηλεθάω ,grüne, sprieße'; lat. tālea ,Stäbchen, Setzling, Setzreis' ... WP. I 705, WH. II 643, Mayrhofer 1, 498.' The root, its language and the Latin daughter are exactly as drawn; the gloss 'twig, wood, a piece of wood used as a unit of length' is NOT Pokorny's.\"},\n        {\"ref\": \"WLD1:705\", \"status\": \"supports\", \"note\": \"incoming/WLD/WLD_Bd1_pages.txt lines 66556-66562, page header 'tad — teu- 705': 'tal- „wachsen, grünen; Gewächs, junger Trieb\\\" (ähnlich mit dhal- „blühen, grünen\\\"). Ai. tāla-ḥ „Weinpalme\\\", tālī „ein bestimmter Baum\\\"; gr. τᾶλις ... lat. talea „Stäbchen, Setzling, Setzreis; jedes stabförmig abgeschnittene Stück\\\" ... lit. a(t)tolas, talokas'. Nourai's page number is exact. Note WP gives no Persian and no Armenian form.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"p. 1055 (POK_03.txt leaf 298; POK_full.txt line 84819 'Root/lemma: tal-, Page(s): 1055')\", \"stance\": \"supports\", \"note\": \"'tāl- ,wachsen, grünen; Gewächs, junger Trieb'' — root real, but only Greek, Latin and Baltic material; no Iranian, no Armenian, no Sanskrit.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 705\", \"stance\": \"partial\", \"note\": \"same lemma with Ai. tāla-ḥ added, glossed 'Weinpalme'; no Persian/Armenian.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, searched 'talea', 'tāl-'\", \"stance\": \"silent\", \"note\": \"Watkins's Indo-European Roots appendix has no *tāl- root and no entry citing Latin talea — grep returns nothing.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 752 (≈ p. 1474), s.v. 'tal- (4)'\", \"stance\": \"supports\", \"note\": \"'tal- (4) (tālis, os, iə) \\\"cutting, new growth, shoot, branch\\\". WP I, 705. Skt. talah, m. & tali, f. \\\"palm-tree\\\"; cf. talikā, f. \\\"palm of hand\\\"; Oss. tāla, s. \\\"shoot, sapling\\\"; Gk. Aeolic tális ... Lat. talea, f. \\\"slip\\\"'. Mann adds the Ossetic (Iranian) member — the only Iranian form any of these books puts under the root.\"},\n        {\"src\": \"SYN\", \"where\": \"SYN.txt leaf 518 (= printed p. 494), note 7\", \"stance\": \"partial\", \"note\": \"'Skt. tala-, talaka-, rarely \\\"lock, bar\\\", tala- usually \\\"fan-palm\\\" : Lat. talea \\\"rod, bar\\\", etc. Walde-P. 1.705.' Buck too glosses the Sanskrit word 'fan-palm', not 'vine'.\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. talea (LAT.txt line 62777 ff.)\", \"stance\": \"contradicts\", \"note\": \"'talea, -ae f.: rejeton, bouture; piquet, pointe ... L'indo-européen n'admettant pas de racines de la forme *tal-, les rapprochements proposés, qui comporteraient pareille forme radicale, sont à écarter. Ils sont du reste rares et vagues pour le sens. Terme technique, sans doute emprunté.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Latin\",\n          \"words\": \"tâlea\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin tālea f. 'a slender rod, stake; a cutting or slip set for planting; twig' is the single daughter of Pokorny's *tāl- that his page actually prints: IEW 1055 'lat. tālea \\\"Stäbchen, Setzling, Setzreis\\\", dial. für *tālia, wie auch tālla = tālia \\\"Zwiebelhülse\\\"; Denominativ tāliāre \\\"spalten, schneiden\\\" (ursprüngl. \\\"Zweige abschneiden\\\")'. Morphologically tālea is the dialectal (rustic) outcome of *tal-ia-, beside the -ll- form talla; semantically the root sense 'young shoot, sprout' (as in Gk. τηλεθάω 'sprout', τᾶλις 'nubile girl') narrowed in the agricultural language of Cato (De agri cultura 45,3 'cum taleam demittes, pede taleam opprimito') to 'a cutting set in the ground', and from there to 'stake, rod, bar' — hence the Roman taleae ferreae, iron bars, which is presumably where Nourai's 'a piece of wood used as a unit of length' comes from. Late Latin tāliāre gave Old French tailler and thence English tailor, detail, retail. The reservation: Ernout-Meillet refuse the root altogether ('L'indo-européen n'admettant pas de racines de la forme *tal- ... Terme technique, sans doute emprunté'), and Wiktionary records the derivation from *teh₂l- as 'traditionally' held but 'questioned', with a rival connection to tālus 'ankle-bone'. So the arrow is what Nourai's source says, but it is not a settled result.\",\n          \"derivation_fa\": \"لاتینی tālea «چوب‌باریک، قلمهٔ نشاندنی، شاخهٔ بریده» تنها فرزندی است که پوکورنی در ص ۱۰۵۵ زیر ریشهٔ *tāl- واقعاً چاپ کرده است: «لاتینی tālea، گونهٔ گویشی از *tālia، مانند tālla = tālia؛ فعل برساختهٔ tāliāre «شکافتن، بریدن» که در اصل «شاخه بریدن» بوده». از نظر معنایی، معنی ریشه‌ایِ «جوانه، نورَسته» در زبان کشاورزی روم (کاتو، سدهٔ دوم پیش از میلاد) به «قلمهٔ نشاندنی» و سپس به «میخ چوبی، میله» تحول یافته است؛ همین معنی اخیر است که نورایی را به افزودنِ «قطعه‌چوبی به‌عنوان واحد طول» در معنی ریشه واداشته. از tāliāre لاتینیِ متأخر، فرانسویِ tailler و از آن‌جا انگلیسی tailor و detail برآمده است. با این‌همه ارنو و مه‌یه این ریشه‌یابی را رد می‌کنند و ویکی‌واژه نیز آن را «سنتی ولی مورد تردید» می‌خواند و ریشهٔ جایگزین tālus «قوزک» را یاد می‌کند؛ پس پیکان نمودار همان است که منبع نورایی می‌گوید، اما نتیجه‌ای قطعی نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/talea\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1055\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 298 / POK_full.txt line 84819: 'Latin tālea \\\"Stäbchen, seedling, Setzreis\\\", dial. for *talia, as also talla = talia; denominative taliare \\\"split, cut, clip\\\"'. Exactly the arrow drawn.\"},\n            {\"ref\": \"ISS:88\", \"status\": \"not_checked\", \"note\": \"Bailey, Indo-Scythian Studies / Khotanese Texts VI p. 88 is not online (HathiTrust mdp.39015034317936 is search-only). The substitute on disk, Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt), cites 'KT vI 87-8' at s.v. ttala but lists only Iranian and Armenian forms there — no Latin tālea. So Nourai's ISS:88 cannot be confirmed for the Latin word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1055\", \"stance\": \"supports\", \"note\": \"lat. tālea listed under tāl-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 705\", \"stance\": \"supports\", \"note\": \"'lat. talea „Stäbchen, Setzling, Setzreis; jedes stabförmig abgeschnittene Stück\\\", dial. für *talia ... Denominativ taliare (germ. und romanisch) „spalten, schneiden\\\" (ursprgl. „*Zweige abschneiden\\\"; Ernout El. dial. lat. 235)'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. talea (LAT.txt l. 62777)\", \"stance\": \"contradicts\", \"note\": \"'talea, -ae (talia Gloss.) f.: rejeton, bouture; piquet, pointe. Ancien (Cat.), technique ... L'indo-européen n'admettant pas de racines de la forme *tal- ... sont à écarter ... Terme technique, sans doute emprunté.'\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 752 (≈ p. 1474) s.v. tal- (4)\", \"stance\": \"supports\", \"note\": \"'cf. further (?) télis ... Lat. Fest. talia, f. \\\"onion leaf\\\" beside Lat. talea, f. \\\"slip\\\"'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 494 n. 7\", \"stance\": \"supports\", \"note\": \"'Lat. talea \\\"rod, bar\\\", etc. Walde-P. 1.705.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"tâlâr «تالار»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian word and its gloss are right: Borhan-e Qate' (ed. Mo'in) p. ~460 s.v. تالار — «بروزن سالار، تختی یا خانه‌ای باشد که بر بالای چهارستون یا بیشتر از چوب و تخته سازند» ('a platform or house built on four or more posts of wood and planking'), which is precisely Nourai's 'a roof or room on top of (wooden) pillars'; Mo'in's Farhang-e Farsi s.v. تالار gives the same and adds 'سالن'. The source of the arrow is Bailey: DKS 123-4 s.v. ttala 'halls (?)' reads 'Base tal- in N.Pers. tal \\\"chamber, hall on columns\\\", M.Parth.T. tl-, t'l- ... \\\"hall\\\", Armen. lw talauar, -ac' \\\"tent, cabin\\\"; N.Pers. talar \\\"wooden edifice on pillars\\\", see KT vI 87-8' — i.e. Nourai's ISS:88 exactly. But Bailey posits a Khotanese/Iranian base tal- 'hall' and nowhere identifies it with Pokorny's *tāl- 'to grow, sprout': the equation of the two roots, and hence the arrow from the IE root box, is Nourai's own step. The competing modern account starts from the attested Manichaean Middle Persian/Parthian tlwʾr /talawār/ 'hall, tabernacle' (whence Old Armenian taławar) and takes NP تالار from it, with *-rb-/-rw- > -lw- > -lā-, connecting the family ultimately to PIE *treb-/*trəb- 'dwelling, building' (Pokorny 1090) — the same root as Persian طربال tarbāl and Latin trabs; Wiktionary's Persian entry gives exactly this. Mo'in's own etymological footnote on the Borhan page offers no root at all, only dialect cognates (Gurani tâlâr, Gilaki tálár, shálának). Horn, Hübschmann, MacKenzie and Nyberg are all silent on the word. So: real word, right meaning, right ultimate family in Bailey's sense, but the specific descent from *tāl- 'grow' is unproved and a rival derivation is at least as strong.\",\n          \"derivation_fa\": \"خودِ واژه و معنی آن درست است: در «برهان قاطع» چاپ معین، ص ~۴۶۰: «تالار ـ بر وزن سالار، تختی یا خانه‌ای باشد که بر بالای چهارستون یا بیشتر از چوب و تخته سازند» — دقیقاً همان معنایی که نورایی می‌دهد؛ فرهنگ معین نیز همین را با افزودن «سالن» آورده است. سرچشمهٔ پیکانِ نمودار بِیلی است: در «فرهنگ ختنی سَکا» ص ۱۲۳ـ۱۲۴ ذیل ttala آمده «ستاک tal- در فارسی نو tal «اتاق، تالارِ ستون‌دار»، پارتی مانوی tl-/t'l- «تالار»، وام‌واژهٔ ارمنی talauar «خیمه، کلبه»؛ فارسی نو talar «بنای چوبیِ ستون‌دار»، نک. KT VI ۸۷ـ۸۸» که همان ارجاع ISS:88 نورایی است. ولی بِیلی این ستاک را هرگز با ریشهٔ «روییدنِ» پوکورنی یکی نمی‌گیرد؛ این یکی‌گرفتن کار خود نورایی است. ریشه‌شناسی رقیب از صورت گواهی‌شدهٔ فارسی میانه/پارتی مانوی tlwʾr (talawār) «تالار، خیمهٔ گاهواره» آغاز می‌کند و «تالار» فارسی نو را از آن می‌گیرد و خانواده را سرانجام به ریشهٔ هندواروپایی *treb- «خانه، بنا» (پوکورنی ۱۰۹۰، هم‌ریشه با «طربال» و لاتینی trabs) می‌رساند؛ ویکی‌واژه همین را می‌آورد. حاشیهٔ ریشه‌شناختی معین بر همان صفحهٔ برهان هیچ ریشه‌ای نمی‌دهد و تنها هم‌ریشه‌های گویشی (گورانی tâlâr، گیلکی tálár و shálának) را می‌آورد؛ هرن، هوبشمان، مکنزی و نیبرگ هم خاموش‌اند. پس: ادعای نورایی با احتیاط پذیرفتنی است، اما پیوند آن با ریشهٔ «روییدن» اثبات‌نشده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D9%84%D8%A7%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"ISS:88\", \"status\": \"partial\", \"note\": \"KT VI p. 88 itself is not online; Bailey's own later Dictionary of Khotan Saka (ISS_alt_DKS.txt, p. 123-4 s.v. ttala) refers to exactly that place — 'N.Pers. talar \\\"wooden edifice on pillars\\\", see KT vI 87-8' — so the citation is genuine and does contain the Persian word. It does NOT contain the step to Pokorny's IE root *tāl- 'to grow', which is Nourai's addition.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS pp. 123-4 s.v. ttala\", \"stance\": \"partial\", \"note\": \"'ttala \\\"halls (?)\\\" ... Base tal- in N.Pers. tal \\\"chamber, hall on columns\\\", M.Parth.T. tl-, t'l- in ʾm, ʿm \\\"hall\\\", Armen. lw talauar, -ac' \\\"tent, cabin\\\"; N.Pers. talar \\\"wooden edifice on pilars\\\", see KT vI 87-8.' — supports the word family, silent on the PIE 'grow' root.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, printed p. ~460 = archive.org borhan-ghate-v1 leaf n688 (image read; saved to sources/refs/ocr/BQT/460.vision.txt)\", \"stance\": \"partial\", \"note\": \"headword «تالار۱ - بروزن سالار، تختی یا خانه‌ای باشد که بر بالای چهارستون یا بیشتر از چوب و تخته سازند»; Mo'in's footnote 1: «گورانی tâlâr «کردی ۲۱»، گیلکی tálár، گیلکی shálának» — dialect cognates only, no root.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 36976 s.v. تالار\", \"stance\": \"supports\", \"note\": \"«تالار: خانه‌ای باشد که بر بالای چهار ستون یا بیشتر از چوب سازند. اطاق بزرگ طویلی که به اطاق‌های دیگر راه داشته باشد. سالن.» — gloss identical to the chart; no etymology in this (2-vol Adena) text.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'talar|tālār|Talar'\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for tālār.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'talar|tālār'\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien does not treat the word.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, grep 'tālār|talar|tlwl'\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary (Book Pahlavi only) has no tālār; the form tlwʾr is Manichaean, outside his corpus.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'talar|tlwl'\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary does not list it.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'تالار'\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian IE-roots dictionary has no تالار entry.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Armenian\",\n          \"words\": \"talauar\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Old Armenian տաղաւար taławar 'tent, tabernacle, booth, cottage' is a real word (it is the Septuagint/Armenian Bible word for the Tabernacle, whence the feast Vardavaṙ/Taławaraharkʿ, and it lives on as Mod. Arm. տաղավար taġavar, Old Georgian ṭalavari, Caucasian Albanian ṭalavar). But it is not an independent Armenian descendant of an Indo-European root, as the chart draws it: every source — including Nourai's own — calls it an Iranian loanword. Bailey at the very place cited (DKS 123-4 = KT VI 87-8) writes 'Armen. lw talauar, -ac' \\\"tent, cabin\\\"', 'lw' being his abbreviation for 'loanword'; Ačaṙean's Armenian Etymological Dictionary and Olsen, The Noun in Biblical Armenian (1999) derive it from Parthian 𐫤𐫓𐫇𐫀𐫡 tlwʾr /talawār/ 'hall, tabernacle', the same Middle Iranian word that underlies NP تالار. Armenian took the word from Parthian in the Arsacid period (the -aw- of taławar renders Parthian -aw- exactly, and the declension in -ac' is the regular Armenian treatment of an -ar stem), so the correct arrow is Parthian → Armenian, parallel to (not sibling of) Persian tālār. Nourai has therefore turned his source's 'loanword' into a direct genetic descent, and hung it on a root (*tāl- 'grow') that Bailey never invokes.\",\n          \"derivation_fa\": \"ارمنی کهن տաղաւար (taławar) «خیمه، خیمهٔ عبادت، کلبه» واژه‌ای واقعی است (در ترجمهٔ ارمنی کتاب مقدس برابرِ «خیمهٔ اجتماع» و ریشهٔ نام جشن وارداوار است) و بازماندهٔ امروزین آن taġavar و وام‌های گرجی ṭalavari و آلبانیایی قفقازی ṭalavar است. اما آن‌گونه که نمودار می‌کشد فرزند مستقیم ریشه‌ای هندواروپایی نیست: همهٔ منابع ـ از جمله منبع خود نورایی ـ آن را وام‌واژهٔ ایرانی می‌دانند. بِیلی در همان جای مورد استناد می‌نویسد «وام‌واژهٔ ارمنی talauar»؛ آجاریان در «ریشه‌شناسی ارمنی» و اولسن (۱۹۹۹) آن را از پارتی tlwʾr (talawār) «تالار، خیمه» می‌گیرند ـ همان واژهٔ ایرانی میانه که «تالار» فارسی نو نیز از آن است. ارمنی این واژه را در دورهٔ اشکانی وام گرفته و ـaw- ارمنی دقیقاً بازتاب -aw- پارتی است. پس پیکان درست «پارتی ← ارمنی» است، نه «ریشهٔ هندواروپایی ← ارمنی»؛ نورایی «وام‌واژه»‌ی منبعش را به وراثت مستقیم بدل کرده و آن را به ریشه‌ای («روییدن») بسته که بِیلی هرگز از آن نام نبرده است. پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D5%BF%D5%A1%D5%B2%D5%A1%D6%82%D5%A1%D6%80\"],\n          \"ref_check\": [\n            {\"ref\": \"ISS:88\", \"status\": \"contradicts\", \"note\": \"The cited Bailey passage (reachable through DKS 123-4, which refers to 'KT vI 87-8') has the word, but labels it 'Armen. lw talauar, -ac' \\\"tent, cabin\\\"' — a LOANWORD from Iranian, not a direct descendant of an IE root. Nourai's arrow from the root box misstates his own reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS pp. 123-4 s.v. ttala\", \"stance\": \"contradicts\", \"note\": \"'Armen. lw talauar, -ac' \\\"tent, cabin\\\"' — 'lw' = loanword.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt (Persische Studien), grep 'talawar|talauar|Talar'\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persian volume does not treat it (his Armenische Grammatik, which does, is not on disk).\"},\n            {\"src\": \"BRT\", \"where\": \"BRT.txt, grep 'talar|talauar'\", \"stance\": \"silent\", \"note\": \"No Old Iranian antecedent in Bartholomae; the only hit is OCR noise in a Yasna citation.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1055\", \"stance\": \"silent\", \"note\": \"Pokorny lists no Armenian form under tāl-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"tâla\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two problems. (1) The gloss is wrong: Sanskrit ताल tāla- is the palmyra or fan palm, Borassus flabellifer — Monier-Williams 'the palm tree, palmyra tree or fan-palm ... producing a sort of spirituous liquor', Mann 'palm-tree', Buck 'fan-palm'. Nourai's 'vine' is a mis-rendering of Walde-Pokorny's German gloss 'Weinpalme' ('wine palm', i.e. the toddy palm from whose sap palm wine is made), the very page he cites; the printed book (p. 465) really does read 'vine', so this is the author's error and the extraction is faithful. (2) The derivation is rejected by modern Indo-Aryan etymology: Mayrhofer (KEWA I 498, the page Pokorny himself points to, and EWAia) treats tāla- as a non-Indo-European culture word, and Wiktionary follows him — 'Borrowed from Dravidian; ultimately from Proto-Dravidian *tāẓ' (cf. Tamil tāḻai) — which is the expected source for the name of a South Indian palm. Walde-Pokorny's inclusion of tāla-/tālī under *tāl- (1930) is thus a pre-Mayrhofer guess that is no longer held; Pokorny himself in 1959 dropped the Sanskrit word from the entry and only cross-referenced Mayrhofer. Note too that nothing in the chart's own chain requires it: the Latin, Persian and Armenian words are unaffected.\",\n          \"derivation_fa\": \"دو اشکال دارد. نخست، معنی نادرست است: سنسکریت ताल (tāla-) نام «نخل تال / نخل بادبزنی» (Borassus flabellifer) است ـ مونیه‌ویلیامز «درخت نخل، نخل تال که از شیرهٔ آن نوعی نوشابهٔ الکلی می‌گیرند»، مان «درخت نخل»، باک «نخل بادبزنی». ترجمهٔ «مو/تاک» (vine) در کتاب، برگردانِ نادرستِ واژهٔ آلمانی Weinpalme «نخلِ می‌ده» در همان صفحهٔ والده‌ـ‌پوکورنی است که نورایی به آن استناد کرده؛ صفحهٔ چاپیِ کتاب (ص ۴۶۵) نیز همین «vine» را دارد، پس خطا از خودِ کتاب است نه از خوانش اسکن. دوم، ریشه‌شناسی امروزی این اشتقاق را رد می‌کند: مایرهوفر (KEWA ج۱ ص۴۹۸ ـ همان صفحه‌ای که پوکورنی به آن ارجاع می‌دهد) tāla- را واژه‌ای غیرهندواروپایی می‌داند و ویکی‌واژه نیز آن را «وام‌گرفته از دراویدی، در نهایت از دراویدیِ آغازین *tāẓ» (قس تامیلی tāḻai) می‌شمارد ـ که برای نام نخلی جنوب‌هندی انتظار می‌رود. آوردن tāla- زیر ریشهٔ *tāl- در والده‌ـ‌پوکورنی (۱۹۳۰) حدسی پیش از مایرهوفر است و خودِ پوکورنی در ۱۹۵۹ آن را از مدخل برداشت و تنها به مایرهوفر ارجاع داد.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"tâla : vine\",\n          \"correct_form\": \"tāla- 'palmyra / fan palm (Borassus flabellifer)', not 'vine'\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A4%BE%E0%A4%B2\"],\n          \"ref_check\": [\n            {\"ref\": \"WLD1:705\", \"status\": \"partial\", \"note\": \"WLD_Bd1_pages.txt line 66556 (page header 'tad — teu- 705'): 'Ai. tala-h „Weinpalme\\\", tali „ein bestimmter Baum\\\"'. The word is on the cited page under the cited root, but glossed 'Weinpalme' = wine/toddy PALM, not 'vine'; and WP 1930 predates Mayrhofer's Dravidian etymology.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 705\", \"stance\": \"partial\", \"note\": \"'Ai. tala-h „Weinpalme\\\", tali „ein bestimmter Baum\\\"' — under tal-, but the gloss is 'toddy palm'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1055 (POK_full.txt, 'References: WP. I 705, WH. II 643, Mayrhofer 1, 498')\", \"stance\": \"contradicts\", \"note\": \"Pokorny 1959 prints only Greek, Latin and Lithuanian under tāl- — the Sanskrit word has been removed from the material and survives only as a cross-reference to Mayrhofer I 498, i.e. Pokorny no longer claims it for the root.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 752 (≈ p. 1474) s.v. tal- (4)\", \"stance\": \"partial\", \"note\": \"'Skt. talah, m. & tali, f. \\\"palm-tree\\\"' — keeps it under the root but glosses 'palm-tree'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 494 n. 7\", \"stance\": \"partial\", \"note\": \"'Skt. tala-, talaka-, rarely \\\"lock, bar\\\", tala- usually \\\"fan-palm\\\" : Lat. talea \\\"rod, bar\\\", etc. Walde-P. 1.705.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Talk\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"New Persian تَلْک talk 'talc, a soft laminated mineral (also used of mica and of gypsum)'\",\n      \"note\": \"The root box is exactly right, in word, script, language and gloss, and the two citations are precise. Borhan-e Qate' (ed. Mo'in) prints the headword «تَلَک» at the foot of p. 508 and continues on p. 509 — Nourai's BQT:509 — with «و تلق و زر ورق را نیز گویند، و طلق معرب آنست» ('they also call it telq and gold-leaf; and ṭalq is the Arabicized form of it'). Mo'in's Farhang-e Farsi s.v. طلق likewise opens '[معر.] معرب تلک' ('Arabicized; the muʿarrab of talk'). This is one of the clearest Persian→Arabic→Europe→Persian round trips in the book, and every independent authority consulted agrees: Wiktionary (Arabic طلق 'Borrowed from Persian تلک talk'), AHD ('French, from Medieval Latin talcum and Old Spanish talco, both from Arabic ṭalq, from Persian talk'), Etymonline, Asbaghi's Persische Lehnwörter im Arabischen p. 199, and Lokotsch no. 2003 ('Ar. talak: ein Mineral \\\"Talk\\\" [wohl pers. Ursprungs]'). The only books that stop at Arabic without naming Persian are Klein, Devic, Lammens and Funk & Wagnalls.\",\n      \"note_fa\": \"جعبهٔ ریشه بی‌کم‌وکاست درست است: واژه، خطِ فارسی «تَلک»، برچسب زبانی و معنی، و هر دو ارجاع دقیق‌اند. «برهان قاطع» چاپ معین سرمدخل «تَلَک» را در پایان ص ۵۰۸ می‌آورد و در ص ۵۰۹ ـ همان BQT:509 نورایی ـ می‌نویسد: «و تلق و زر ورق را نیز گویند، و طلق معرب آنست». فرهنگ معین نیز ذیل «طلق» با «[معر.] معرب تلک» آغاز می‌کند. این یکی از روشن‌ترین نمونه‌های رفت‌وبرگشت «فارسی ← عربی ← اروپا ← فارسی» در کتاب است و همهٔ منابع مستقل با آن هم‌داستان‌اند: ویکی‌واژه (عربی طلق «وام‌گرفته از فارسی تلک»)، فرهنگ American Heritage («از فرانسوی، از لاتینی میانه talcum و اسپانیایی کهن talco، هر دو از عربی ṭalq، از فارسی talk»)، اتیمانلاین، اصبغی در «وام‌واژه‌های فارسی در عربی» ص ۱۹۹ و لوکوچ شمارهٔ ۲۰۰۳ («عربی talak، کانی «تالک»، ظاهراً فارسی‌تبار»). تنها کلاین، دُویک، لامنس و فانک‌واگنالز در عربی می‌ایستند و از فارسی نام نمی‌برند. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B7%D9%84%D9%82\",\n        \"https://www.ahdictionary.com/word/search.html?q=talc\",\n        \"https://www.etymonline.com/word/talc\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"MON:1133\", \"status\": \"supports\", \"note\": \"Mo'in's Farhang-e Farsi: the local 2-vol Adena text (different pagination from Nourai's 6-vol Amir Kabir set, so the page number itself could not be checked) has the mineral described at MON_part1.txt l. 93005-93015 with the synonym string «تلق، تالک، ابرک، کوکب‌الارض»; the online Mo'in text (vajehyab.com/moein/طلق) reads «(طَ) [معر.] (اِ.) معرب تلک؛ سنگی معدنی که به رنگ سفید نقره‌ای شفاف و براق و قابل تورق است» — 'muʿarrab of talk', i.e. exactly the arrow Persian talk → Arabic ṭalq.\"},\n        {\"ref\": \"BQT:509\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 509 (archive.org borhan-ghate-v1 leaf n737, running head ۵۰۹ verified on the image; text saved to sources/refs/ocr/BQT/509.vision.txt). The entry «تَلَک» begins at the foot of p. 508 and continues: «... اول و سکون ثانی بمعنی تلخ بود که ضد شیرین است - و تلق و زر ورق را نیز گویند، و طلق معرب آنست - و نوعی از قماش هم هست ...». Nourai's page is exact and it carries precisely the claim of the chart.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BQT\", \"where\": \"ed. Mo'in pp. 508-509 s.v. تلک; and vol. 3 p. 1358 s.v. طلق\", \"stance\": \"supports\", \"note\": \"p. 509: «و طلق معرب آنست»; p. 1358 Mo'in's footnote 9: «معرب «تلک» فارسی «اقرب الموارد»؛ از عربی وارد فرانسوی شده talc = amiante = mica».\"},\n        {\"src\": \"MON\", \"where\": \"Mo'in s.v. طلق (vajehyab) and MON_part1 s.v. طلق/تالک\", \"stance\": \"supports\", \"note\": \"«[معر.] معرب تلک».\"},\n        {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen p. 199 s.v. ṭalq (and the index p. 75 s.v. talk)\", \"stance\": \"supports\", \"note\": \"'ṭalq: \\\"Brandsalbe\\\" < pers. talk, syr. …, it. talco, lat. talcum, frz. talc, engl. talc, dtsch. Talk'; and 'talk: \\\"Talk; Speckstein, ein sehr weißes weiches Mineral\\\" ° pers. …'.\"},\n        {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2003\", \"stance\": \"supports\", \"note\": \"'Ar. talak: Ein Mineral \\\"Talk\\\" [wohl pers. Ursprungs]; hieraus it. talco, frz. talc, sp. talque, sp. pg. talco, kat. talc; ndl. talksteen, dtsch. Talk, engl. talc; russ. talk.'\"},\n        {\"src\": \"KLN\", \"where\": \"Klein s.v. talc (KLN_1966.txt l. 38033)\", \"stance\": \"partial\", \"note\": \"'talc, n., a soft mineral, magnesium silicate. — F., fr. Sp. talque, fr. Arab. talaq, talq, whence also It. talco, G. Talk' — stops at Arabic, no Persian.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"talq\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic طَلْق ṭalq 'talc, mica' is a muʿarrab (Arabicized borrowing) of Persian talk, taken over in the ʿAbbasid period through the alchemical and pharmacological literature — the word is standard in Jābir/Geber's alchemy and in the materia medica (Ibn al-Bayṭār, d. 1248, defines it 'حجر براق يتحلل إذا دق إلى طاقات صغار دقاق', a shiny stone that splits into fine flakes). Phonetically the adaptation is the routine one: Persian t- was taken into the emphatic ṭāʾ (Arabic has no plain-t/emphatic contrast matching Persian t before back vowels, and the emphatic spelling طلق also kept the word out of the homograph تلك 'that'), the final -k became -q, and the short vowel of talk was reanalysed as the Arabic CaCC noun pattern ṭalq; Wiktionary records تَلْك talk as an alternative Arabic form, showing the older un-emphatic shape. Nourai's own sources say so in as many words: Borhan p. 509 «و طلق معرب آنست»; Mo'in's footnote at Borhan p. 1358 «معرب «تلک» فارسی «اقرب الموارد»»; and AHD 'from Arabic ṭalq, from Persian talk'. Asbaghi's Persische Lehnwörter im Arabischen p. 199 lists it among the certain Persian loans in Arabic.\",\n          \"derivation_fa\": \"عربی «طَلْق» معرّبِ فارسیِ «تلک» است که در دورهٔ عباسی از راه ادبیات کیمیاگری و داروشناسی (جابر/گِبِر، و ابن‌البیطار در «الجامع» که آن را «حجر براق یتحلل اذا دق الی طاقات صغار دقاق» تعریف می‌کند) وارد عربی شده است. دگرگونی آوایی همان دگرگونی عادی معرّب‌سازی است: «ت» فارسی به «ط» مفخّم بدل شده (عربی برای t فارسی پیش از واکهٔ پسین برابر دقیقی ندارد و نگارش با طاء واژه را از «تلك» به‌معنی «آن» هم جدا می‌کند)، «ک» پایانی به «ق» و ساختِ واژه بر وزن فَعْل (طَلْق) بازتحلیل شده است؛ ویکی‌واژه صورت کهن‌ترِ «تَلْک» را هم به‌عنوان گونهٔ عربی ثبت کرده است. منابع خودِ نورایی همین را می‌گویند: برهان ص ۵۰۹ «و طلق معرب آنست»؛ حاشیهٔ معین بر برهان ص ۱۳۵۸ «معرب «تلک» فارسی «اقرب الموارد»»؛ و AHD «از عربی ṭalq، از فارسی talk». اصبغی نیز آن را در شمار وام‌واژه‌های قطعی فارسی در عربی آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B7%D9%84%D9%82\",\n            \"https://www.ahdictionary.com/word/search.html?q=talc\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1133\", \"status\": \"supports\", \"note\": \"Mo'in s.v. طلق (vajehyab.com/moein/طلق): «(طَ) [معر.] (اِ.) معرب تلک؛ سنگی معدنی که به رنگ سفید نقره‌ای شفاف و براق و قابل تورق است». (Page number not verifiable: the local copy is the 2-vol abridgement, not Nourai's 6-vol set.)\"},\n            {\"ref\": \"SHP:349\", \"status\": \"not_checked\", \"note\": \"Shipley, Dictionary of Word Origins (1945) is lending-only on archive.org and the HathiTrust full-view copy (uc1.32106001576476) cannot be fetched page by page; p. 349 not read.\"},\n            {\"ref\": \"AHD:1312\", \"status\": \"supports\", \"note\": \"Nourai cites the AHD New College Edition main entry. The current online AHD (ahdictionary.com/word/search.html?q=talc) gives '[French, from Medieval Latin talcum and Old Spanish talco, both from Arabic ṭalq, from Persian talk.]' — the Arabic←Persian step and the whole downstream chain of the chart.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 199 s.v. ṭalq\", \"stance\": \"supports\", \"note\": \"'ṭalq ... < pers. talk, syr. …, it. talco, lat. talcum, frz. talc, engl. talc, dtsch. Talk'.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2003\", \"stance\": \"supports\", \"note\": \"'Ar. talak: Ein Mineral \\\"Talk\\\" [wohl pers. Ursprungs]'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. talc\", \"stance\": \"partial\", \"note\": \"gives 'Arab. talaq, talq' as the source of the European words but does not trace it to Persian.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt / AFM.txt, grep 'الطلق', 'طلق'\", \"stance\": \"silent\", \"note\": \"Addi Shir's list of Persian Arabisms: no entry found (the OCR of this Beirut 1908 scan is badly corrupted by Syriac-type character substitutions, so a negative grep is weak evidence).\"},\n            {\"src\": \"DEV\", \"where\": \"Devic s.v. Talc (DEV.txt l. 2169)\", \"stance\": \"partial\", \"note\": \"'Talc. Esp. talco, talque, portug. talco. En arabe, طلق talq ... Le mot طلق se rencontre dans l'alchimie de Géber, notamment au chapitre VII du IIe livre' — confirms the Arabic word and its alchemical transmission, but names no Persian source.\"},\n            {\"src\": \"LAM\", \"where\": \"Lammens, Remarques s.v. Talc (LAM.txt l. 6948)\", \"stance\": \"partial\", \"note\": \"'Talc. Esp: talco, talque. Ptg: tâlco. De طلق talq, même sens. ... Ibn el-Beithâr nous apprend qu'on en fabriquait des vitres pour les bains' — Arabic source only.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"talq «طلق» \",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian طلق ṭalq 'mica, talc (the transparent laminated mineral used for lamp-glasses, lantern panes, and — in the folk tradition — as a fire-proofing)' is the Arabicized form re-imported into Persian: a classic muʿarrab round trip, Persian talk → Arabic ṭalq → Persian ṭalq, in which the borrowed spelling with ط and ق displaced the native تلک in learned and pharmacological usage. Both of Nourai's references say exactly this. Borhan-e Qate', ed. Mo'in, p. 1358: «طلق - بفتح اول و سکون ثانی و قاف، گوهری باشد کانی. گویند هر که گرد آن را بر بدن مالد آتش بر بدن او اثر نکند، و بعربی کوکب‌الارض خوانند», with Mo'in's footnote «معرب «تلک» فارسی «اقرب الموارد»؛ از عربی وارد فرانسوی شده talc = amiante = mica». Mo'in's own dictionary s.v. طلق opens «[معر.] معرب تلک». The two Persian forms therefore coexist as a doublet (دوگانه): inherited تلک and re-borrowed طلق, with the modern scientific تالک (node 5) as a third, European-mediated layer.\",\n          \"derivation_fa\": \"«طلق» فارسی همان معرّبِ «تلک» است که دوباره به فارسی بازگشته: نمونه‌ای آشکار از رفت‌وبرگشتِ «فارسی ← عربی ← فارسی»، که در آن املای عربیِ با «ط» و «ق» در کاربرد ادبی و داروشناسی جای «تلک» بومی را گرفت. معنی «ابرک، کانیِ ورقه‌ورقه و شفاف» است که برای شیشهٔ فانوس و چراغ به کار می‌رفت و در باور عامیانه بدن را از آتش نگاه می‌داشت. هر دو ارجاع نورایی دقیقاً همین را می‌گویند: «برهان قاطع» چاپ معین ص ۱۳۵۸: «طلق ـ بفتح اول و سکون ثانی و قاف، گوهری باشد کانی. گویند هر که گرد آن را بر بدن مالد آتش بر بدن او اثر نکند، و بعربی کوکب‌الارض خوانند»، با حاشیهٔ معین: «معرب «تلک» فارسی «اقرب الموارد»؛ از عربی وارد فرانسوی شده talc = amiante = mica». فرهنگ معین نیز ذیل «طلق» با «[معر.] معرب تلک» آغاز می‌کند. پس «تلک» و «طلق» در فارسی دوگانه (doublet) اند و «تالک» علمی امروز لایهٔ سومِ اروپایی‌تبار است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/moein/%D8%B7%D9%84%D9%82\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2232\", \"status\": \"supports\", \"note\": \"Mo'in s.v. طلق: «(طَ) [معر.] (اِ.) معرب تلک؛ سنگی معدنی که به رنگ سفید نقره‌ای شفاف و براق و قابل تورق است» (vajehyab.com/moein/طلق). Volume/page of the 6-vol set not checkable against the local abridgement, but the entry is verbatim what the chart needs.\"},\n            {\"ref\": \"BQT:1358\", \"status\": \"supports\", \"note\": \"Borhan vol. 3, printed p. 1358 = incoming/BQT/BQT_v3_pages.txt [pdf page 151]: «طلق - بفتح اول وسکون ثانی وقاف، گوهری باشد کانی. گویند هرکه گرد آنرا بربدن مالد آتش بر بدن او اثر نکند۱، وبعربی کوکب‌الارض خوانند»; footnote: «معرب «تلک» فارسی «اقرب الموارد»؛ از عربی وارد فرانسوی شده talc = amiante = mica (فر) «لک۲ ص ۱۸۰...»». Page number exact and it states both the Arabic→Persian and the Arabic→French steps.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1358 s.v. طلق\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote: «معرب «تلک» فارسی «اقرب الموارد»».\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in s.v. طلق; MON_part1.txt l. 93005-93015\", \"stance\": \"supports\", \"note\": \"«[معر.] معرب تلک»; the mineralogical description ends with the synonyms «تلق، تالک، ابرک، کوکب‌الارض».\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 199 s.v. ṭalq\", \"stance\": \"supports\", \"note\": \"treats ṭalq as a Persian loan in Arabic, i.e. the Persian ط-form is the returned muʿarrab.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'طلق'\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary has no entry (it covers inherited Iranian vocabulary, not Arabisms).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"talcum\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Medieval Latin talcum (also talcus) 'talc, any shiny laminated mineral' entered scholastic Latin in the early 14th century through the Latin translations of Arabic alchemy — the pseudo-Geber corpus and the Latin Ibn al-Bayṭār/Avicenna tradition — where Arabic ṭalq was simply Latinized with the neuter -um suffix and the emphatic ṭ rendered by plain t and the qāf by c: ṭalq > talc-um. Etymonline dates 'Medieval Latin talcus, also talcum \\\"talc\\\"' to the early 14c.; AHD gives 'Medieval Latin talcum ... from Arabic ṭalq'. Because it was a Latin word of the laboratory rather than of speech, medieval and Renaissance writers applied it loosely to talc, mica and selenite alike (Martin Ruland, quoted by Devic: 'Talcum, vox esse Arabica creditur, significans stellulas micantes'). Note that Klein and Devic route the European words through Spanish talque/talco rather than through Latin; AHD accepts both paths ('from Medieval Latin talcum and Old Spanish talco'), so the chart's Latin link is right but is only one of two attested channels.\",\n          \"derivation_fa\": \"لاتینیِ میانه (قرون‌وسطایی) talcum / talcus «تالک، هر کانیِ ورقه‌ورقهٔ براق» در آغاز سدهٔ چهاردهم میلادی از راه ترجمه‌های لاتینیِ کیمیای عربی (مجموعهٔ منسوب به جابر و سنت ابن‌البیطار و ابن‌سینا) وارد لاتینی مدرسی شد: «طلق» عربی با پسوند خنثای -um لاتینی شد و «ط» مفخّم به t ساده و «ق» به c بدل گشت (ṭalq > talcum). اتیمانلاین صورت‌های talcus/talcum را به اوایل سدهٔ ۱۴ می‌رساند و AHD «لاتینی میانه talcum ... از عربی ṭalq» می‌دهد. چون این واژه‌ای آزمایشگاهی بود نه گفتاری، نویسندگان سده‌های میانه و رنسانس آن را بی‌دقت برای تالک و ابرک و سنگ گچِ شفاف به کار می‌بردند (مارتین رولاند به نقل دُویک: «Talcum را واژه‌ای عربی می‌دانند به معنی ستارک‌های درخشان»). یادآوری: کلاین و دُویک واژه‌های اروپایی را از راه اسپانیایی talque/talco می‌گیرند نه لاتینی؛ AHD هر دو راه را می‌پذیرد، پس حلقهٔ لاتینیِ نمودار درست است اما تنها یکی از دو مسیرِ گواهی‌شده است.\",\n          \"sources\": [\"https://www.etymonline.com/word/talc\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1312\", \"status\": \"supports\", \"note\": \"AHD online s.v. talc: '[French, from Medieval Latin talcum and Old Spanish talco, both from Arabic ṭalq, from Persian talk.]' — the Medieval Latin link from Arabic is exactly as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. talc\", \"stance\": \"partial\", \"note\": \"'F., fr. Sp. talque, fr. Arab. talaq, talq' — Klein routes French through Spanish, not through Medieval Latin.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2003\", \"stance\": \"partial\", \"note\": \"derives it. talco, frz. talc, sp. talque directly from Ar. talak without an intervening Latin stage.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 199\", \"stance\": \"supports\", \"note\": \"explicitly lists 'lat. talcum' in the chain between Arabic and French.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic s.v. Talc\", \"stance\": \"supports\", \"note\": \"quotes Martin Ruland: '\\\"Talcum, vox esse Arabica creditur, significans stellulas micantes\\\"' — the Latin form in the alchemical literature.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"talc\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French talc, first attested in the 16th century (and in the alchemical and mineralogical writing of the period), is the Latin laboratory word talcum stripped of its ending — the regular French treatment of a learned Latin neuter in -um (cf. album, opium kept, but talcum > talc as with Lat. sulphur-type technical borrowings taken through Spanish/Italian forms talque, talco). AHD: 'French, from Medieval Latin talcum and Old Spanish talco'; Etymonline: 'French talc (16c.), probably from Spanish talco and Medieval Latin talcus, also talcum'. Mo'in's own footnote at Borhan p. 1358 knows the step and states it from the Persian side: «از عربی وارد فرانسوی شده talc = amiante = mica». French then became the distributing language for the modern technical term across Europe and the Middle East (node 5) — pharmaceutical 'talc de Venise' in the 17th-18th c., and 'talc' as the standard mineralogical name after Mohs.\",\n          \"derivation_fa\": \"فرانسویِ talc، نخستین‌بار در سدهٔ شانزدهم میلادی در نوشته‌های کیمیایی و کانی‌شناسی گواهی شده، همان واژهٔ لاتینیِ آزمایشگاهیِ talcum است که پایانهٔ -um آن افتاده ـ رفتار عادی فرانسوی با وام‌واژه‌های عالمانهٔ لاتینی، احتمالاً با میانجیِ صورت‌های اسپانیایی/ایتالیایی talque و talco. AHD: «از فرانسوی، از لاتینی میانه talcum و اسپانیایی کهن talco»؛ اتیمانلاین: «فرانسوی talc (سدهٔ ۱۶)، احتمالاً از اسپانیایی talco و لاتینی میانه talcus/talcum». حاشیهٔ معین بر برهان ص ۱۳۵۸ همین گام را از سوی فارسی می‌بیند: «از عربی وارد فرانسوی شده talc = amiante = mica». فرانسوی سپس زبانِ پخش‌کنندهٔ این اصطلاح فنی در اروپا و خاورمیانه شد (بند ۵). ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=talc\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1312\", \"status\": \"supports\", \"note\": \"AHD online: 'talc ... [French, from Medieval Latin talcum and Old Spanish talco, both from Arabic ṭalq, from Persian talk.]' — French from Medieval Latin, as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. talc\", \"stance\": \"supports\", \"note\": \"'F., fr. Sp. talque' — agrees that French is the immediate donor to English, differs on French's own source.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2003\", \"stance\": \"supports\", \"note\": \"'hieraus it. talco, frz. talc, sp. talque ... engl. talc; russ. talk'.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard vol. IV s.v. talc (FSD_vol4.txt l. 30104 ff.)\", \"stance\": \"partial\", \"note\": \"'[F., < Ar. ṭalq, talc]' — French from Arabic, with no Latin and no Persian stage.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 199\", \"stance\": \"supports\", \"note\": \"'lat. talcum, frz. talc, engl. talc, dtsch. Talk'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"tâlk «تالک»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Modern Persian تالک tālk 'talc, talcum powder' is a 20th-century European re-borrowing of the very word Persian had given away a millennium earlier — the third layer of the doublet (inherited تلک, Arabicized طلق, European تالک). The form itself shows it is not inherited: an inherited talk would not have long ā in the first syllable, whereas تالک with alef renders the [a] of French talc as Persian ā in the usual way scientific loans are naturalized (cf. فرانسه، آتم، تالک‌شیست), and the cluster -lk is kept as in the donor. Mo'in's dictionary uses تالک as the technical mineral name throughout the geology entries — «سنگ هرکاره ... گونه‌ای از سنگ‌های دگرگونی که تالک شیست نامیده می‌شوند ... این سنگ ... خواص تالک را نیز دارا است» and, s.v. طلق, the synonym list «تلق، تالک، ابرک، کوکب‌الارض» — so the word is certainly current. What could not be verified is the chart's claim that French specifically was the mediating language: Moshiri's Farhang-e Vazheha-ye Orupayi dar Farsi (VOP:135) is not obtainable in any library scan, and no other consulted source discusses the modern Persian form. French is nevertheless the likeliest channel, since Persian mineralogical and chemical vocabulary of the Dar al-Fonun era was taken from French, and Mo'in himself glosses the modern term from French at Borhan p. 1358 («از عربی وارد فرانسوی شده talc»); English or Russian mediation cannot be excluded on the evidence available.\",\n          \"derivation_fa\": \"«تالک» فارسیِ امروز به معنی «تالک، پودر تالک» وام‌گیریِ دوبارهٔ همان واژه‌ای است که فارسی هزار سال پیش‌تر به عربی و از آن‌جا به اروپا داده بود ـ لایهٔ سومِ این دوگانه (تلکِ بومی، طلقِ معرّب، تالکِ اروپایی). خودِ صورت واژه نشان می‌دهد که موروثی نیست: «تلک» موروثی الفِ کشیده ندارد، حال آن‌که «تالک» با الف، واکهٔ کوتاه [a] فرانسویِ talc را به شیوهٔ معمولِ فارسی‌سازیِ وام‌واژه‌های علمی به ā بدل کرده و خوشهٔ پایانی -lk را نیز مانند زبان مبدأ نگاه داشته است. فرهنگ معین این صورت را در مدخل‌های زمین‌شناسی به‌عنوان نام فنی کانی به کار می‌برد («سنگ هرکاره ... گونه‌ای از سنگ‌های دگرگونی که تالک شیست نامیده می‌شوند ... خواص تالک را نیز دارا است») و ذیل «طلق» هم‌معناهای «تلق، تالک، ابرک، کوکب‌الارض» را می‌آورد؛ پس واژه بی‌گمان رایج است. آنچه بررسی‌پذیر نبود، میانجی بودنِ «فرانسوی» به‌طور مشخص است: کتابِ مشیری «فرهنگ واژه‌های اروپایی در فارسی» (VOP:135) در هیچ کتابخانهٔ اسکن‌شده‌ای یافت نشد و هیچ منبع دیگری دربارهٔ صورت فارسیِ امروزین سخن نگفته است. با این‌همه فرانسوی محتمل‌ترین راه است، چون واژگان کانی‌شناسی و شیمی فارسی از عصر دارالفنون از فرانسوی گرفته شده و خود معین در حاشیهٔ برهان ص ۱۳۵۸ اصطلاح امروزی را از فرانسوی نقل می‌کند؛ میانجیِ انگلیسی یا روسی هم یکسره منتفی نیست. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://vajehyab.com/moein/%D8%B7%D9%84%D9%82\"],\n          \"ref_check\": [\n            {\"ref\": \"VOP:135\", \"status\": \"not_checked\", \"note\": \"Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371/1992): refs_online.json records kind 'none' — no scan on archive.org, ketabnak, noorlib or the open web; re-checked, still nothing. Page 135 could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt ll. 80453-80458 and 93011-93014\", \"stance\": \"supports\", \"note\": \"«... گونه‌ای از سنگ‌های دگرگونی که تالک شیست نامیده می‌شوند ... خواص تالک را نیز دارا است»; and, under طلق, the synonyms «تلق، تالک، ابرک، کوکب‌الارض» — the European form تالک is the modern technical term in Persian.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1358, Mo'in's footnote on طلق\", \"stance\": \"partial\", \"note\": \"«از عربی وارد فرانسوی شده talc = amiante = mica (فر)» — Mo'in cites the French word (marked «فر») as the modern equivalent, but does not say the Persian تالک was taken from it.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt and ARY_latin_index_pages.txt, grep 'تالک' / 'TALK'\", \"stance\": \"silent\", \"note\": \"no entry; Aryanpur covers inherited Indo-European vocabulary, not modern European loans.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"talc; talcum\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"talc is right as drawn: English talke is first recorded in the 1580s, borrowed from French talc (16c.), and the modern spelling and the sense 'magnesium silicate, the softest mineral (Mohs 1)' follow the French mineralogical usage; AHD 'talc … [French, from Medieval Latin talcum …]'; Klein 'F., fr. Sp. talque, fr. Arab. talaq, talq'. talcum, however, is drawn from French here, and that is not what the English record shows: it appears earlier than talc, in the 1550s, in the phrase 'pouder of Talchum', taken straight from the Medieval Latin alchemical term talcum (Etymonline, s.v. talcum: '\\\"talc, soapstone,\\\" 1550s (pouder of Talchum), from Medieval Latin talcum, used for any of various shiny minerals'); 'talcum powder' is attested from 1871. So the arrow for talcum should run from the Middle Latin node (#3), not from French (#4). Both words are of course ultimately the same Persian talk. Verdict for the node is the worse of the two: talc confirmed, talcum mis-routed.\",\n          \"derivation_fa\": \"دربارهٔ talc نمودار درست است: صورت انگلیسیِ talke نخستین‌بار در دههٔ ۱۵۸۰ گواهی شده و از فرانسویِ talc (سدهٔ ۱۶) گرفته شده است؛ املا و معنی امروزی («سیلیکات منیزیم، نرم‌ترین کانی، سختی ۱ در مقیاس موس») نیز از کاربرد کانی‌شناسیِ فرانسوی می‌آید (AHD و کلاین). اما talcum را نورایی از فرانسوی گرفته و این با گواهی‌های انگلیسی نمی‌خواند: این صورت پیش از talc، در دههٔ ۱۵۵۰ و در ترکیب «pouder of Talchum»، مستقیماً از اصطلاح لاتینیِ کیمیاگریِ talcum به انگلیسی رفته است (اتیمانلاین ذیل talcum: «از لاتینی میانه talcum که برای هر کانی براقی به کار می‌رفت»)، و ترکیب talcum powder از ۱۸۷۱ ثبت شده است. پس پیکانِ talcum باید از گرهٔ لاتینیِ میانه (#۳) کشیده شود نه از فرانسوی (#۴). هر دو واژه البته در نهایت همان «تلک» فارسی‌اند. حکم این گره بدترینِ دو واژه است: talc تأییدشده، talcum با مسیر نادرست.\",\n          \"sources\": [\"https://www.etymonline.com/word/talc\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1312\", \"status\": \"partial\", \"note\": \"AHD online s.v. talc gives '[French, from Medieval Latin talcum and Old Spanish talco, both from Arabic ṭalq, from Persian talk.]' — supports English talc < French, but AHD's headword etymology does not make English talcum a French derivative either; talcum is a separate learned Latin borrowing.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. talc (KLN_1966.txt l. 38033)\", \"stance\": \"supports\", \"note\": \"'talc, n., a soft mineral, magnesium silicate. — F., fr. Sp. talque, fr. Arab. talaq, talq, whence also It. talco, G. Talk (this latter prob. through the medium of French).'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard vol. IV s.v. talc\", \"stance\": \"supports\", \"note\": \"'[F., < Ar. ṭalq, talc]' — English from French.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'talc', 'talcum'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise Etymological Dictionary has no entry for talc.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"only volume 1 (A–?) of Webster's New Twentieth Century is on disk; the T section is in the missing vol. 2.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2003\", \"stance\": \"supports\", \"note\": \"'... ndl. talksteen, dtsch. Talk, engl. talc; russ. talk' — English among the European descendants of the Arabic word.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-495.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-14T03:26:30.274Z] TOOL RESULT

```
JSON OK
```


## [2026-09-14T03:26:32.440Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 tools/verify_check.py 495"
}
```


### [2026-09-14T03:26:33.520Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'plausible': 4, 'disputed': 2, 'confirmed': 4}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 7, 'not_checked': 3, 'partial': 3, 'contradicts': 1}
books consulted: {'supports': 19, 'contradicts': 3, 'partial': 12, 'silent': 13} | by book: {'PLA': 4, 'LKT': 4, 'KLN': 4, 'POK': 3, 'BQT': 3, 'MON': 3, 'ARY': 3, 'WLD': 2, 'IEC': 2, 'SYN': 2, 'ISS_alt_DKS': 2, 'HUB': 2, 'DEV': 2, 'FSD': 2, 'LAT': 1, 'HRN': 1, 'PHD': 1, 'NYB': 1, 'BRT': 1, 'AFM': 1, 'LAM': 1, 'SKT': 1, 'WEB': 1}
```


## [2026-09-14T03:26:38.706Z] TOOL CALL #81: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg495.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/495.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/495.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/{460,509}.vision.txt"
}
```


### [2026-09-14T03:26:39.721Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 49206 Sep 13 23:26 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/495.png
-rw-rw-r-- 1 sfmqrb sfmqrb   865 Sep 13 23:17 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/460.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2009 Sep 13 23:15 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/509.vision.txt
```


## [2026-09-14T03:27:00.662Z] AGENT

Page 495 verified. `verify_check.py 495`: 10/10 nodes, 0 PROBLEM lines.

**Counts** — roots: 1 confirmed (Talk), 1 plausible (Tâl). Nodes: 4 confirmed, 4 plausible, 2 disputed. Ref checks: 7 supports, 3 partial, 1 contradicts, 3 not_checked (ISS:88 = Bailey KT VI, not online; SHP:349; VOP:135 — Moshiri has no scan anywhere).

**Disputed**
- **Tâl #3 Armenian `talauar`** — Nourai draws it straight from the IE root, but Bailey at the very page cited writes "Armen. **lw** talauar" (loanword); Ačaṙean/Olsen and Wiktionary derive Old Arm. տաղաւար from Parthian *tlwʾr* (talawār). Correct arrow: Parthian → Armenian.
- **Tâl #4 Sanskrit `tâla` "vine"** — gloss is a mistranslation of Walde-Pokorny's "Weinpalme"; the word is the palmyra/fan palm (Borassus), and Mayrhofer/Wiktionary make it a Dravidian loan (*tāẓ), not IE. Pokorny 1959 himself dropped it from the entry.

**Other notable findings**
- Root **Tâl**: POK:1055 and WLD1:705 are exact, but the gloss "twig, wood, a piece of wood used as a unit of length" is Nourai's own addition — neither page has it. Ernout-Meillet reject the root outright ("L'indo-européen n'admettant pas de racines de la forme *tal- … Terme technique, sans doute emprunté"); Watkins/AHD has no such root.
- **Tâl #2 Persian تالار** — word and gloss confirmed from Borhan p. ~460 and Mo'in, and Bailey (DKS 123-4, citing "KT vI 87-8" = Nourai's ISS:88) does group it under a base *tal-*; but the identification with Pokorny's "grow" root is Nourai's own, and the rival account (Manich. MP/Parth. *talawār* → PIE **treb-* "dwelling") is at least as strong. Marked plausible.
- **Talk entry is a clean hit**: Borhan p. 509 literally prints «و طلق معرب آنست», and Mo'in's footnote at Borhan p. 1358 «معرب «تلک» فارسی «اقرب الموارد»؛ از عربی وارد فرانسوی شده talc». AHD, Etymonline, Wiktionary, Asbaghi p. 199 and Lokotsch no. 2003 all confirm Persian talk → Ar. ṭalq → ML talcum → Fr. talc → Eng.
- **Talk #6** marked plausible only because English *talcum* (1550s, "pouder of Talchum") comes straight from Medieval Latin, earlier than *talc* (1580s) — the arrow for *talcum* should come from node #3, not from French.

**Extraction errors: none.** I rendered PDF p. 495 (saved to `data/verification/sources/refs/ocr/BOOK/495.png`) and the JSON matches the printed chart exactly, including the erroneous "vine" gloss, which is the book's own error.

Artefacts written: `/home/sfmqrb/git/rishe/data/verification/page-495.json`, plus page-image transcriptions `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/509.vision.txt` and `.../BQT/460.vision.txt`; 9 web pages archived via `fetch_source.py`.
