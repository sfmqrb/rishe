# Verification process log — verify-page-493


## [2026-09-14T03:08:46.073Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 493 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-493.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-493.json. Write /home/sfmqrb/git/rishe/data/verification/page-493.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 493` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:47.020Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:47.843Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:47.862Z] TOOL RESULT

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


## [2026-09-14T03:08:48.404Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-493.txt"
}
```


### [2026-09-14T03:08:48.436Z] TOOL RESULT

```
1	=== PDF page 493 (book page 463) ===
2	--- entry 0 ---
3	ROOT [Arabic] S.x.r : to ridicule  (refs SAP:683)
4	#1 (parent #0) [Arabic] refs=SAP:683 | masxarah : mockery
5	  #2 (parent #1) [Persian] refs=MON:4109 | masxareh «مسخره» : funny, clown
6	  #3 (parent #1) [Italian] refs=KLN:944 | maschera : mockery
7	    #4 (parent #3) [French] refs=KLN:944 | masque : mask
8	      #5 (parent #4) [Persian] refs=MON:3699 | mâsk «ماسک» : mask
9	      #6 (parent #4) [English] refs=None | mask ; masque ; masquerade ; mascara
10	--- entry 1 ---
11	ROOT [Sanskrit] Syand
12	Sindhu : to flow
13	the sea  (refs SKT:260; HJB:433)
14	#1 (parent #0) [Avestan / Old Persian] refs=KLN:787 | hend : India (a name due to the river Indus in India) ; hendî : Indian
15	  #2 (parent #1) [Persian] refs=None | Hend «هند ( هندوستان )» : India ; hendevâneh «هندوانه» : watermelon "from India"
16	    #3 (parent #2) [English] refs=AHD | Hindu ; tamarind
17	  #4 (parent #1) [Greek] refs=AHD | Indos
18	    #5 (parent #4) [Latin] refs=None | Indus
19	      #6 (parent #5) [English] refs=None | India ; Indian ; indigo ; indium
20	--- entry 2 ---
21	ROOT Šypšyr -> redirect to Šfšyr
22	--- entry 3 ---
23	ROOT [Syriac / Aramaic] Šypwr : trumpet  (refs TZF:77)
24	#1 (parent #0) [Pahlavi] refs=TZF:77 | šayfur
25	  #2 (parent #1) [Persian] refs=TZF:77; MON:2101; BQT:1319 | šaypŭr «شیپور ( شیپور )» : trumpet
26	
```


## [2026-09-14T03:08:49.614Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-14T03:08:50.970Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-493.json | head -200",
 "description": "Read source JSON for page 493"
}
```


## [2026-09-14T03:08:51.730Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:08:52.067Z] TOOL RESULT

```
{
    "pdf_page": 493,
    "book_page": 463,
    "entries": [
        {
            "root": {
                "name": "S.x.r",
                "lang": "Arabic",
                "refs": "SAP:683",
                "gloss": "to ridicule"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "SAP:683",
                    "words": [
                        {
                            "translit": "masxarah",
                            "gloss": "mockery",
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
                    "refs": "MON:4109",
                    "words": [
                        {
                            "translit": "masxareh",
                            "gloss": "funny, clown",
                            "script": "\u0645\u0633\u062e\u0631\u0647"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Italian",
                    "refs": "KLN:944",
                    "words": [
                        {
                            "translit": "maschera",
                            "gloss": "mockery",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "French",
                    "refs": "KLN:944",
                    "words": [
                        {
                            "translit": "masque",
                            "gloss": "mask",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "MON:3699",
                    "words": [
                        {
                            "translit": "m\u00e2sk",
                            "gloss": "mask",
                            "script": "\u0645\u0627\u0633\u06a9"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 4,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "mask",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "masque",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "masquerade",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "mascara",
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
                "name": "Syand\nSindhu",
                "lang": "Sanskrit",
                "refs": "SKT:260; HJB:433",
                "gloss": "to flow\nthe sea"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "KLN:787",
                    "words": [
                        {
                            "translit": "hend",
                            "gloss": "India (a name due to the river Indus in India)",
                            "script": null
                        },
                        {
                            "translit": "hend\u00ee",
                            "gloss": "Indian",
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
                    "refs": null,
                    "words": [
                        {
                            "translit": "Hend",
                            "gloss": "India",
                            "script": "\u0647\u0646\u062f ( \u0647\u0646\u062f\u0648\u0633\u062a\u0627\u0646 )"
                        },
                        {
                            "translit": "hendev\u00e2neh",
                            "gloss": "watermelon \"from India\"",
                            "script": "\u0647\u0646\u062f\u0648\u0627\u0646\u0647"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "Hindu",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "tamarind",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "Indos",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
```


### [2026-09-14T03:08:52.104Z] TOOL RESULT

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


## [2026-09-14T03:08:55.446Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-493.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-14T03:08:56.596Z] TOOL RESULT

```
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Latin",
                    "refs": null,
                    "words": [
                        {
                            "translit": "Indus",
                            "gloss": null,
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
                            "translit": "India",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "Indian",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "indigo",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "indium",
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
                "name": "\u0160yp\u0161yr",
                "redirect": "\u0160f\u0161yr"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "\u0160ypwr",
                "lang": "Syriac / Aramaic",
                "refs": "TZF:77",
                "gloss": "trumpet"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Pahlavi",
                    "refs": "TZF:77",
                    "words": [
                        {
                            "translit": "\u0161ayfur",
                            "gloss": null,
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
                    "refs": "TZF:77; MON:2101; BQT:1319",
                    "words": [
                        {
                            "translit": "\u0161ayp\u016dr",
                            "gloss": "trumpet",
                            "script": "\u0634\u06cc\u067e\u0648\u0631 ( \u0634\u06cc\u067e\u0648\u0631 )"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0628\u0641\u0631\u0645\u0648\u062f \u062a\u0627 \u0628\u0631\u06a9\u0634\u06cc\u062f\u0646\u062f \u0646\u0627\u06cc - \u0647\u0645\u0627\u0646 \u0633\u0646\u062c \u0648\u0634\u06cc\u067e\u0648\u0631 \u0648\u0647\u0646\u062f\u06cc \u062f\u0631\u0627\u06cc",
                        "poet": "Ferdows\u00ee"
                    }
                }
            ]
        }
    ]
}
```


## [2026-09-14T03:08:56.967Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SAP','TZF','SKT','HJB','KLN','MON','BQT','AHD']:\n    print('==',k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n\"",
 "description": "Ref info for cited refs"
}
```


### [2026-09-14T03:08:58.093Z] TOOL RESULT

```
== SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4yQPAQAAMAAJ (1977), NoplAAAAMAAJ (1985), HcGipwAACAAJ (2001)."}
== TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadable without login."}
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online a
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


## [2026-09-14T03:09:24.826Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,60p tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-14T03:09:24.870Z] TOOL RESULT

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
```


## [2026-09-14T03:09:26.210Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'maskharah\\|maskhara\\|maschera\\|masquerade' KLN_1966.txt | head -30; echo ---; grep -n -i 'mascara' KLN_1966.txt | head",
 "description": "Klein mask entries"
}
```


### [2026-09-14T03:09:26.297Z] TOOL RESULT

```
23047:mashie,  mashy,  n.,  an  iron  golf  club.  —  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a  tool  for  dig¬ ging'.  See  mace,  ‘a  staff’,  and  cp.  masse,  mattock, masjid,  n.,  a  mosque.  —  Arab.  See  mosque, mask,  n.  —  MF.  (=  F)  masque,  fr.  ML.  masca, fr.  It.  maschera,  fr.  Arab.  maskharah,  ‘mockery; buffoon’,  fr.  sdkhira,  ‘he  mocked,  ridiculed’. Cp.  masque,  masquerade.
23057:masque,  n.,  1)  a  masquerade;  2)  a  kind  of  dramat¬ ic  performance.  —  F.  masque.  See  mask, masquerade,  n.,  an  assembly  of  persons  wearing masks.  —  F.  mascarade,  fr.  Sp.  mascarada, prop,  ‘a  ball  at  which  masks  are  worn’,  fr. mascara,  ‘mask’.  See  mask  and  -ade,  and  cp. mascara.
23058:Derivatives :  masquerade,  intr.  v.,  masquerad-er, n.
---
23036:mascagnite,  n.,  ammonium  sulfate  (mineral.)  — Named  after  its  discoverer,  the  Italian  anat¬ omist  and  physiologist  Paolo  Mascagni  (1752- 1815).  For  the  ending  see  subst.  suff.  -ite. mascara,  n.,  a  cosmetic  preparation  for  coloring the  eyelashes.  —  Sp.  mascara,  ‘a  mask’,  fr. Arab,  mdskharct,  ‘mockery ;  buffoon'.  See  mask, mascle,  n.,  1)  a  steel  plate;  2)  a  lozenge  voided (her.)  —  OF.  mascle  (F.  made),  fr.  L.  macula, ‘spot’.  See  mackle,  made, mascot,  n.,  talisman,  charm.  —  F.  mascotte,  pop¬ ularized  by  Audran’s  operette  La  Mascotte (1880).  F.  mascotte  is  a  loan  word  fr.  Proven?. mascoto,  ‘sorcery,  charm’,  fr.  masco,  ‘sorceress, witch’,  which  is  of  uncertain  origin, masculine,  adj.  —  ME.  masculin,  fr.  OF.  (=  F.) masculin  (fem.  masculine),  ‘of  the  male  sex’,  fr. masculus,  ‘male’,  fr.  mas,  ‘male’,  which  is  of uncertain  origin.  Cp.  emasculate.
23057:masque,  n.,  1)  a  masquerade;  2)  a  kind  of  dramat¬ ic  performance.  —  F.  masque.  See  mask, masquerade,  n.,  an  assembly  of  persons  wearing masks.  —  F.  mascarade,  fr.  Sp.  mascarada, prop,  ‘a  ball  at  which  masks  are  worn’,  fr. mascara,  ‘mask’.  See  mask  and  -ade,  and  cp. mascara.
```


## [2026-09-14T03:09:38.309Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN leaf for line 23036\"; awk 'NR<=23057' KLN_1966.txt | tr -cd '\\f' | wc -c; echo \"== SKT mask\"; grep -n -i '^MASK\\|^MASQUE\\|^MASCARA' SKT.txt | head; echo \"== SKT sindhu/india/indigo\"; grep -n -i '^INDIGO\\|^INDIA\\|SINDHU\\|syand' SKT.txt | head",
 "description": "Klein leaf and Skeat entries"
}
```


### [2026-09-14T03:09:39.391Z] TOOL RESULT

```
== KLN leaf for line 23036
507
== SKT mask
11187:MASK-
11198:Masque ;  see  Uaik.
== SKT sindhu/india/indigo
9177:Indigo,  a  blae  dye.  (F.  — Span.  — L  — Gk.  — Pens— Skt.)  F.rm/>]i,T.— Span  indieo.
9179:—  Skt.  sindhu,  the  river  Indui;  a  Iwge river.  —  SkL  tyand,  to  flow.  %  The PersiiD  changers  i  into  h.
16868:Sendal,  Cendal.  a  ricli  thin (F.-LowL.-Skt.)  O.F,  ;^w eendaium,  eimiadus,  iinJiUHi called  because  brought  fiora  India.  —  SU sindhu,  the  Indtu,  also  Sonde— Skt.  ty^i^ to  How  :  see  Indigo.
```


## [2026-09-14T03:09:40.193Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LKT maschera\"; grep -n -i 'maschera\\|maskhara\\|masquerade' LKT.txt | head; echo \"== PHN masque\"; grep -n -i 'masque\\|mascarade' PHN.txt | head; echo \"== DEV\"; grep -n -i 'masque\\|mascarade' DEV.txt | head",
 "description": "Lokotsch/Pihan/Devic mask"
}
```


### [2026-09-14T03:09:40.279Z] TOOL RESULT

```
== LKT maschera
== PHN masque
7186:MASCARADE, s. f. (a.)
7189:quun. — Chez nous, mascarade s'emploie dans le sens de dé-
7190:guisement avec un masque pour se dit^eriir; réunion ou danse de
7193:çais MASQUE, yauo; vis€^e que l'on fabriquait autrefois en très-
7198:mascarilla [petit masque), et pour augmentatif masgaron, mot
7203:masques; il y en avait de trois espèces : le tragique, le comique,
10710:Mascarade, s. f. (a.) — Masque, s. m. — Mascaron, s. m 956
== DEV
1690:Mascarade.  Esp.  et  portug.  mascara,  masque;  ital.  ma- schera,  même  sens.  Il  a  été  surabondamment  démontré  par divers  étymologistes ,  contrairement  à  l'opinion  de  Diez, et  notamment  par  MM.  Malin  et  Dozy,  que  mascara  et  ma- schera  ne  sont  rien  autre  que  l'arabe  »-ià*^^  maskhara  si- gnifiant bonjfon,  farceur,  histrwn ;  plaisanterie ,  drôlerie,  mo- querie. Je  crois  inutile  de  reproduire  les  arguments  exposés en  détail  dans  le  Glossaire  de  MM.  Engelmann  et  Dozy. (Voy.  p.  3o/i  et  suiv.)
1691:Il  y  a  longtemps  que  Chardin  écrivait,  dans  son  Voyap-e en  Perse  :  crlls  (les  Persans)  appellent  ces  sortes  de  di- vertissements r^irtsrrtrc^  c'est-à-dire  jeu,  plaisanterie,  raille- rie ,  représentation ,  d'oii  est  venu  notre  mot  de  mascarade.  5j (Edit.  Smith,  p.  s/jq.)
1701:Matassins.  Esp.  matachin,  portug.  muchachim ,  ital.  mat- tacino.  M.  Dozy  dérive  ingénieusement  ces  mots  de  l'arabe xzi^^  ouadjh,  visage,  employé  dans  le  sens  de  masque,  d'où
1702:un  verbe  ^^'  tawadjdjah,  se  masquer,  et  enfin  le  parti-
3343:Damasquetle.  voy.  Damas.
3861:Mascara,  hisp.  voy.  Mascarade.
3862:Mascarade.
3863:Mascarè,  voy.  Mascarade.
3864:Maschera,  ital.  voy.  Mascarade.
5117:vîLu/  »^j*  pers.  Yoy.  Alchimie,  lu. -j~«  voy.  Astronomie,  lo. U-wàj>y«  voy.  Marcassite. xù-^-iiJ>j«  voy.  Marcassite. lh>,Aj>y«  voy.  Marcassite. <-.^5^  voy.  Markab. ^y9  voy.  Moringe. ^-«  voy.  Moringe. i^y»  voy.  Astronomie,  30. iôj) j«  voy.  Madrague. t_>*xx*«-«  voy.  Mosarabe. »Xss^vj»  voy.  Mosquée. ïy^r^  voy.  Mascarade. Je.'M-ji  voy.  Mistique. liL-j*  voy.  Musc. ^jiSi**^  voy.  Mesquin. ^.^•-L»*^  voy.  Musulman. jU*«w«  voy.  Mousselin. n*)TDD  voy.  Massore, Î12^12  voy.  Miscbna. J^tjrut  voy.  Alchimie,  hn. ^3Xu3»  voy.  Bangue. ïJsu»  voy,  Matras. ^Ja.*  voy.  Matelas. iCSJa.»  voy.  Matraca. »^yj£u9  voy.  Matamore, iojsjt»  voy.  Almadie. (jjnjjuo  voy.  Mézéréon. <_>yL«  voy.  Garbin. ïyjt^  voy.  Almagra. Ixx/»  tnal.  voy.  Mangue. o*«5^  ma/,  voy.  Mangoustan, Y  ^^M  mal.  voy.  Manglier. ^^^iCk«  mft/.  voy.  Mangoustan, ^*w.^JCx,«  ï/i«/.  voy.  Mangoustan. 4pjL«  voy.  Mufti. ^^UL»  voy.  Macabre, jj^.      -Uu»  voy.  (iiiïniacan.
```


## [2026-09-14T03:09:49.087Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11185,11200p' SKT.txt; echo \"=== indigo ctx\"; sed -n '9174,9182p' SKT.txt; echo \"=== SKT leaf for indigo line\"; awk 'NR<=9179' SKT.txt | tr -cd '\\f' | wc -c; echo \"=== leaf for mask\"; awk 'NR<=11187' SKT.txt | tr -cd '\\f' | wc -c",
 "description": "Skeat context"
}
```


### [2026-09-14T03:09:50.130Z] TOOL RESULT

```
to    drpriTC    of    virility. of  L.  tmaicmiart."!^.  t, iiuM,  male. •  L.)     0.  F.    «di//    aoter
,M,  wUd  drake.  (F.  -  U >  M.  K. F.    m»i*rdi    fonucd,   with
MASK-
suffix  .«r(/  (of  G.  origin,  from  G.  hart,) from  O.  F.  maif,  male  ( above  i.  The suffix  sin/ was  pariicularly  applied  to  males, so  thai  ihe  itlcii  of 'male'  opftcars  twice
marital.  l>clongtng  to  a  husband.  i.F, —  L.)  F.  tnarital,  ••  L,  maritah's,  adj. formed  from  maritus,  a  hushaiiil.  This is  a  masc.  sb.  made  to  accompany marita,  a  woman  provided  with  a  nosbandL •>L.  man'-,  crude  foiin  of  mas,  a  man, hiubanH  ;  see  Masculine  (above).
marry-  0'-  —  I-)  M  E.  marten,  m  F, marier.  —  L  maritare^  to  marry.  <—  L.  mart- tujt  a  husband  ;  see  marital  (above). Mash,  to  beat  into  a  mixed  ma&s.  (E.  er Scand.)  A  maiA  is  properly  a  mtxtnre; and  to  masA  was,  formerly,  to  mi\.  We find  A.  S.  maxwyrtt,  mash-wort,  new beer;  so  that  the  word  may  l>e  English; but  it  is  commoner  in  Scandinavian.  Cf. Swed.  dial,  mask^  Swcd.  tnasi,  brewer's grains,  whence  masJka,  to  mix,  Dan.  and North  Fries,  mask,  grains,  mash.  Don. masJke,  to  mash,  fatten  pigs  with  grains.  + G.  meisch,  a  mash,  metscheH.  to  mash. The  sb.  form  appears  to  be  the  original. I'erha[t^  alliett  to  Mix.  Cf.  also  Gael. and  Irish  mas^,  to  mix,  infuse,  steep; Lithuan.  maixzyti,  to  stir  things  in  a  pot, from  mtJS'fit  to  mix.
meas  (>),  a  mixture,  disonJer.  (E.  or Scond.)  A  corruption  of  the  older  form nujA,  which  again  stands  for  masA,  sb. Cf.  mash,  vb.  t^abo^c).  'Mesro/are,  to mixe,  to  math,  to  mish\*  Florio.  * Metc*- lutua,  a  mcdlie,  a  mesh,  a  mixture:'  id. Mask,  Masque,  a  disguise  fur  liie  face : masked  entertainment.  vF-  ■-Span,  »Arab. ) The  sense  <d  '  entertainment '  is  the  true one;  the  sense  of  'disguise'  is  secondary, 'A  jolly  company  in  mancr  of  a  mAskt'/ F.  Q.  iii.  1 1.  5.  •  Some  hane  I datince  in  a  majke ,'  Sir  T.  More.  \Vork4^ p.  1057.  More  uses  ntaskers  in  the  senfiC of  'visora'  (correctly,  according  to  the Spanish  uae).«>F.  m<2x/i«.  a  mask,  visor; a  dipped  form, due  to  F.  vb.  masqmr,  really, short  for  masqutrtr*  \  the  fuller  form  comi out  in  O.  F.  Hiosiptaritj,  masked,  masqusn'e, majquera<i€,  'a  mask  or  mummery;*  Cot. »Span.  mascara,  a  masker,  a  ma&quciader ; also  a  mask.  — Arab,  maskharut,  a  buffoon, jester,  man  in  masquerade,  a  pltafontT}-. anythinj^  ndiculous.  —  Arab,  root  sakhim. he  iidiuuled.  %  Fully  proved;  other  ety> mologies  are  worthless.  Det.  nuu^utroJA, F.  masi^ufradtf  ispta  mascaradft.
Its
in,       ■
*74
MASON.
Maaon.  (F.  -  Low  L.  -  G.  ?)    O.  F.
maxsoH ;  F.  moffiM.  —  Low  L.  macUtum, ace.  of  macio,  a  mason ;  we  also  find  the forms  macAic,  mtu^if.  mato,  mactio,  matii4j, maih.  Perhaps  from  M.  H.  G.  rmaso,  a mosoQ,  wheace  G.  steinmett,  a  itone- mason:  allied  to  O.  H.  G.  meiian^  to hew,  cut  (whence  G.  nuissei,  a  chisel).  4* Icel.  nui/a,  to  hew,  Goth,  maitan,  to  hew^ cat,  a  strong  verb.     (Base  MIT.)
Masque ;  see  Uaik.
Haas  (1),  a  lump :  sec  Maoerata.
Maas  (j),  the  celebration  of  the  Eucha- rist ;  see  Sllaaile.
=== indigo ctx
Indict,  Indlotion  ;  see  Diction.
Indi^enouB ;  see  Genoa.
Indigent,  destitute-  (F.-L)  F.  iitdi- ftnt.^L.  inJi^ent't  stem  of  pre*,  part.  .oC inUigrrr,  to  be  in  want.- L.  i«*/-,  for  indo or  iHiin,  an  O.  LA.  extension  from  in,  in (cf.  Gk.  Ivhow.  within):  egert,  to  want,  he in  need;  cf.  L.  imfigus,  needy.  Cf.  Gk. ix^i*'.  poor,  needy  \.Tbcucritui).    (^  AGll  )
Indigo,  a  blae  dye.  (F.  — Span.  — L  — Gk.  — Pens— Skt.)  F.rm/>]i,T.— Span  indieo.
—  L  indicum,  indigo;  neut.  of  /ndicui, Indian  (hence  Indian  dye).  — Gk.  UUmiv, indigo;  ncuL  of  IvUK&t,  Indian.—  Per*. Hind,  Indi.!  ;  a  name  due  to  the  river  Indtia.
—  Skt.  sindhu,  the  river  Indui;  a  Iwge river.  —  SkL  tyand,  to  flow.  %  The PersiiD  changers  i  into  h.
Indite ;  sec  Diction. Indolence :  »ec  Deleft IndomlUbl«;  ••■  Deiml
I
INFLUENCE.
=== SKT leaf for indigo line
243
=== leaf for mask
297
```


## [2026-09-14T03:09:50.532Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==508' KLN_1966.txt | head -5; echo \"=== page numbers near\"; awk 'BEGIN{RS=\"\\f\"} NR>=505 && NR<=510 {print NR\": \"substr($0,1,120)}' KLN_1966.txt",
 "description": "Klein page check"
}
```


### [2026-09-14T03:09:51.893Z] TOOL RESULT

```
—  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a  tool  for  dig¬ ging'.  See  mace,  ‘a  staff’,  and  cp.  masse,  mattock, masjid,  n.,  a  mosque.  —  Arab.  See  mosque, mask,  n.  —  MF.  (=  F)  masque,  fr.  ML.  masca, fr.  It.  maschera,  fr.  Arab.  maskharah,  ‘mockery; buffoon’,  fr.  sdkhira,  ‘he  mocked,  ridiculed’. Cp.  masque,  masquerade.
Derivatives :  mask,  tr.  and  intr.  v.,  musk-ed,  adj., mask-er,  n.,  mask-ette,  n.
maskery,  masquery,  n.  —  F.  masquerie,  fr.  mas¬ quer,  ‘to  mask’,  fr.  masque.  See  mask  and  -ery. maskelynite,  n.,  a  feldspar  mineral  (mineral.)  — Named  after  the  English  mineralogist  Nevil Slory -Maskelyne  (1823-1911).  For  the  ending see  subst.  suff.  -ite. maskinonge,  n.  —  See  muskellunge. maslin,  n.,  a  kind  of  brass  (obsol.)  —  ME.,  fr. OE.  meestling,  m  testing,  mseslin,  rel.  to  MDu., M  HG.  messinc,  missinc,  Du.  messing,  G.  Mes¬ sing,  ‘brass’.  These  Teut.  words,  as  well  as Czech  mosaz,  Slovak  mosadz,  Pol.  mosiqdz, ‘brass’,  ult.  derive  fr.  Gk.  Moaouvoixoi;  yeOutiq, ‘brass  made  by  the  Mossynoikoi’,  a  people  liv¬ ing  south  of  the  Euxine,  lit.  ‘those  dwelling  in (zoaouvec  (i.e.  wooden  houses)’.  Brass  is  said to  have  been  first  manufactured  by  the  Mossy¬ noikoi,  whence  the  name  Moaouvotxo?  yotXxoq. maslin,  n.,  a  mixture  of  different  kinds  of  grain. —  ME.  mastlyoun,  mestlyon,  fr.  OF.  mesteillon, mestillon,  fr.  mestueil,  mesteil  (F.  mdteil),  fr. VL.  *mistilium,  which  was  formed  from  the adjective  *mistilis,  fr.  *mistus,  a  collateral  form of  L.  mixtus,  pp.  of  miscere,  ’to  mix’.  See  mix. masochism,  n.,  a  form  of  sexual  perversion  in which  one  finds  pleasure  in  being  hurt  ( med.); the  opposite  of  sadism.  —  Named  after  the Austrian  novelist  Leopold  Sacher  Masoch (1836-95),  who  describes  it  in  one  of  his  works. For  the  ending  see  suff.  -ism. masochist,  n.  —  See  prec.  word  and  -ist.
Derivative:  masocHTst-ic,  adj. mason,  n.  —  ME.,  fr.  OF.  (=  F.)  mafon,  fr. Frankish  *makjo,  Latinized  into  machid,  from the  verb  *makan ,  ‘to  make’.  See  make  and  cp. freemason.
Derivatives:  mason,  tr.  v.,  mason-ic,  adj.,  mason¬ ry,  n.
=== page numbers near
505: =  F.)  marche,  fr.
marcher.  See  prec.  word  and  cp.  demarche. March,  n.  —  ME.,  fr.  OF.  march,  also  marz
506: —  L.  maritalis,  ‘of  mar¬ riage',  fr.  maritus,  ‘a  married  man,  husband’, which  is  of  uncertain  ety
507:  See  marital  and  marriage.
Derivatives:  marri-ed,  adj.,  marri-er,  n.
Mars,  n.,  the  Roman  god  of  war.  —  
508: —  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a
509: nis, ‘chewing,  mastication’,  fr.  masticatus,  pp.  of masticare.  See  masticate  and  -ion. mastiff,  n.  —  M
510: o  measure’.  See  meter,  ‘poetical  rhythm’, and  cp.  words  there  referred  to. matranee,  n.,  a  female  sw
```


## [2026-09-14T03:10:05.661Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==484 {print substr($0,1,200)}' KLN_1966.txt; echo \"---485\"; awk 'BEGIN{RS=\"\\f\"} NR==485 {print substr($0,1,200)}' KLN_1966.txt; echo \"=== KLN_1971 mask\"; grep -n 'maskharah\\|maskharah\\|mask,  n\\.' KLN_1971.txt | head -5",
 "description": "Check Klein page mapping"
}
```


### [2026-09-14T03:10:06.751Z] TOOL RESULT

```
like.  —  Gk.  XtfloeiSrjp,  ‘like  a stone’,  compounded  of  XtHop,  ‘stone’,  and -oeiSvjp,  ‘like’,  fr.  cISop,  ‘form,  shape’.  See
litho-  and  -oid.
lithology,  n.,  the  st
---485
  cp.  delivery.
Derivative:  liveri-ed,  adj.
livery,  adj.,  resembling  liver.  —  Formed  fr.  liver, ‘secreting  organ  of  the  body’,  with  -y  (corre¬ sponding  to  OE.  -ig).
livid,  
=== KLN_1971 mask
```


## [2026-09-14T03:10:07.202Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN hindu/india\"; grep -n 'Hindu,  n\\|India-\\|Indian,  adj\\|indigo,  n\\|tamarind' KLN_1966.txt | head -10",
 "description": "Klein India entries"
}
```


### [2026-09-14T03:10:07.275Z] TOOL RESULT

```
== KLN hindu/india
19161:India,  n.  —  L.,  fr.  Gk.  ’IvSia,  fr.  ’'IvSos,  ‘the  river Indus’,  fr.  OPers.  Hindu,  fr.  OI.  sindhuh ,  ‘river’, spec,  ‘the  river  Indus’,  whence  ‘the  region  of the  river  Indus’.  Cp.  Hindu,  indign,  indium, sandia,  sendal,  sindon.  Cp.  also  the  second  ele¬ ment  in  Sapindus  and  in  tamarind.
19188:Derivative :  indignant-ly ,  adv. indignation,  n.  —  F.,  fr.  L.  indignadonem,  acc.  of indignado ,  ‘indignation,  displeasure’,  fr.  indig- natus,  pp.  of  indignari.  See  indign  and  -ation. indignity,  n.  —  L.  indignitas,  gen.  -at is,  ‘unwor¬ thiness,  meanness,  baseness’,  fr.  indignus,  ‘un¬ worthy’.  See  indign  and  -ity. indigo,  n.,  a  blue  dye.  —  F.,  fr.  Du.  indigo,  bor¬ rowed  fr.  Sp.  indico,  indigo,  fr.  L.  indicum,  ‘in¬ digo’,  fr.  Gk.  lv8o«6v,  ‘indigo’,  (short  for’IvStxiv epotpjraxov,  lit.  ‘Indian  dye’),  neut.  of  TvSix6c, ‘Indian’.  See  Indie.
38089:tamarind,  n.,  1)  a  tropical  tree;  2)  its  fruit.  —  Sp. tamarinda  (also  Port,  and  It.),  fr.  Arab,  tamr Hindi,  ‘Indian  date’,  fr.  tamr,  ‘date’,  and  Hindi, ‘Indian’,  which  is  formed  fr.  Hind,  ‘India’,  with gentilic  suff.  -i.  The  first  element  is  rel.  to Heb.  tamar,  ‘palm  tree,  date  palm’,  Aram. tamra,  Syr.  tf martd,  Ethiop.  tamr,  ‘date’,  ‘date palm’,  and  prob  also  to  Arab,  itma'arra,  ‘was erect  or  stiff’,  (said  of  a  lance).  For  the  second element  in  tamarind  see  Hindu,  India, tamarisk,  n.,  an  evergreen  shrub  or  small  tree with  slender  branches  and  feathery  clusters  of pinkish  flowers.  —  Late  L.  tamariscus,  fr.  L. tamarix,  ‘tamarisk’,  prob.  fr.  Heb.  tamar,  ‘palm tree’,  or  Arab,  tamr,  ‘date’.  See  tamarind  and cp.  Tamarix.
```


## [2026-09-14T03:10:11.903Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"leaf(India)=\"; awk 'NR<=19161' KLN_1966.txt | tr -cd '\\f' | wc -c; echo \"== Hindu\"; grep -n 'Hindu,' KLN_1966.txt | head -5",
 "description": "Klein India leaf and Hindu"
}
```


### [2026-09-14T03:10:12.979Z] TOOL RESULT

```
leaf(India)=
422
== Hindu
17820:Hindoo,  Hindooism,  Hindoostani.  —  See  Hindu, Hinduism,  Hindustani.
17822:Hindu,  also  Hindoo,  n.,  one  of  the  Hindu  race.  — Pers.  Hindu,  fr.  Hind,  ‘India’,  fr.  OI.  Sindhuh, ‘the  river  Indus;  the  region  of  the  river  Indus’. See  India  and  cp.  words  there  referred  to.
17823:Hinduism,  also  Hindooism,  n.,  the  religion  of  the Hindus.  —  Formed  fr.  Hindu  with  suff.  -ism. Hindustani,  also  Hindoostani,  n.,  the  most  im¬ portant  dialect  of  Western  Hindi;  adj.,  per¬ taining  to  Hindustan  or  Hindustani.  7—  Hind. Hindustani,  formed  with  suff.  -t  (expressing relationship)  fr.  Pers.  Hindustan,  lit.  ‘the  country of  the  Hindus’,  fr.  Hindu,  ‘Hindu’,  and  stan, ‘place,  country’.  For  the  first  element  see  Hindu. The  second  element  is  rel.  to  Avestic  stana-  (in compounds),  ‘place’,  lit.  ‘a  place  where  to stand’,  from  the  stem  of  sta-,  ‘to  stand’,  fr.  I.-E. base  *sta-,  ‘to  stand’,  whence  also  L.  stare,  ‘to stand’.  See  state  and  cp.  stand.  Cp,  also  Afgha¬ nistan,  Baluchistan,  lit.  ‘place  (i.e.  land)  of  the Afghans,  resp.  Baluchis’.  Cp.  also  the  second element  in  bezesteen  and  in  bostangi. Derivative:  Hindustani,  n. hing,  n.,  asafetida.  —  Hind,  lung,  fr.  OI.  hiiiguh. hinge,  n.  —  ME.  henge,  lit.  ‘that  on  which  the door  hangs’,  fr.  hengen,  ‘to  hang’.  Cp.  MLG. henge,  ‘hinge’,  MDu.  henge,  ‘hook,  handle’,  Du. hengsel,  ‘hinge’,  and  see  hang.
19161:India,  n.  —  L.,  fr.  Gk.  ’IvSia,  fr.  ’'IvSos,  ‘the  river Indus’,  fr.  OPers.  Hindu,  fr.  OI.  sindhuh ,  ‘river’, spec,  ‘the  river  Indus’,  whence  ‘the  region  of the  river  Indus’.  Cp.  Hindu,  indign,  indium, sandia,  sendal,  sindon.  Cp.  also  the  second  ele¬ ment  in  Sapindus  and  in  tamarind.
38089:tamarind,  n.,  1)  a  tropical  tree;  2)  its  fruit.  —  Sp. tamarinda  (also  Port,  and  It.),  fr.  Arab,  tamr Hindi,  ‘Indian  date’,  fr.  tamr,  ‘date’,  and  Hindi, ‘Indian’,  which  is  formed  fr.  Hind,  ‘India’,  with gentilic  suff.  -i.  The  first  element  is  rel.  to Heb.  tamar,  ‘palm  tree,  date  palm’,  Aram. tamra,  Syr.  tf martd,  Ethiop.  tamr,  ‘date’,  ‘date palm’,  and  prob  also  to  Arab,  itma'arra,  ‘was erect  or  stiff’,  (said  of  a  lance).  For  the  second element  in  tamarind  see  Hindu,  India, tamarisk,  n.,  an  evergreen  shrub  or  small  tree with  slender  branches  and  feathery  clusters  of pinkish  flowers.  —  Late  L.  tamariscus,  fr.  L. tamarix,  ‘tamarisk’,  prob.  fr.  Heb.  tamar,  ‘palm tree’,  or  Arab,  tamr,  ‘date’.  See  tamarind  and cp.  Tamarix.
```


## [2026-09-14T03:10:13.502Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HJB 433 region: grep HINDU/TAMARIND\"; grep -n '^HINDU\\|^TAMARIND\\|^INDIGO\\|^INDIA' HJB.txt | head -10",
 "description": "Hobson-Jobson entries"
}
```


### [2026-09-14T03:10:13.567Z] TOOL RESULT

```
== HJB 433 region: grep HINDU/TAMARIND
11474:INDIA,  INDIES.
11477:INDIA,  INDIES,  n.p.  A  book might  be  written  on  this  name.  We can  only  notice  a  few  points  in  con- nection with  it.
11483:INDIA,  INDIES.
11485:INDIA,  INDIES.
11499:INDIA,  INDIES,
11501:INDIA,  INDIES,
11520:INDIA,  INDIES.
11522:INDIA,  INDIES.
11553:INDIAN.
11555:INDIGO,
```


## [2026-09-14T03:10:20.435Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo -n \"leaf(Hindu)=\"; awk 'NR<=17822' KLN_1966.txt | tr -cd '\\f' | wc -c; echo -n \"leaf(tamarind)=\"; awk 'NR<=38089' KLN_1966.txt | tr -cd '\\f' | wc -c; echo -n \"leaf(indigo)=\"; awk 'NR<=19188' KLN_1966.txt | tr -cd '\\f' | wc -c",
 "description": "Klein leaves"
}
```


### [2026-09-14T03:10:21.527Z] TOOL RESULT

```
leaf(Hindu)=394
leaf(tamarind)=831
leaf(indigo)=423
```


## [2026-09-14T03:10:21.926Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11474,11480p;11553,11560p' HJB.txt | cut -c1-1500; echo \"=== leaf\"; awk 'NR<=11477' HJB.txt | tr -cd '\\f' | wc -c",
 "description": "Hobson-Jobson India entry"
}
```


### [2026-09-14T03:10:22.994Z] TOOL RESULT

```
INDIA,  INDIES.
such  BE  fall  upon  the  Indians.  Iinpalaimieiit is  the  chief  and  most  terrible." — Stavanmi8f i.  288.  This  writer  proceeds  to  give  a description  of  the  horrible  process,  which he  witnessed.
INAUM,  ENAUM,  s.  Ar.  in'dm, *  a  gift '  (from  a  superior),  *  a  favour,' but  especially  in  India  a  gift  of  rent- free  land :  alAo  land  so  held.  In'amdar, the  holder  of  such  lands.  A  full  detail of  the  diiferent  kinds  of  in^dm,  especially among  the  Mahrattas,  will  be  found  in Wilson,  s.y.  The  word  is  also  used  in Western  India  for  buckaheeah  (q.v.). This  use  is  said  to  have  given  rise  to  a little  mistake  on  the  part  of  an  English political  traveller  some  30  or  40  years Sif^y  when  there  had  been  some  a£;ita- tion  regarding  the  in'am  lands  and  the alleged  harsmiess  of  the  Qovemment in  dealing  with  such  claims.  The traveller  reported  that  the  public  feel- ing in  the  west  of  India  was  so strong  on  this  subject  that  his  very palai&in-bearers  at  the  end  of  their stage  invariably  joined  their  hands  in sunplication, shouting,  "In'am!  In'am!
INDIA,  INDIES,  n.p.  A  book might  be  written  on  this  name.  We can  only  notice  a  few  points  in  con- nection with  it.
It  is  not  easy,  if  it  be  possible,  to  find a  truly  native  (i,e,  Hindu)  name  for  the whole  country  which  we  call  India ; but  the  conception  certainly  existed from  an  early  date.  Bhdraiavarsha is  used  apparentlv  in  the  Puranas with  sometidng  like  this  conception. JanibudrnpOj  a  term  belonging  to  the mythical  cosmography,  is  usea  in  the Buddhist  books,  and  sometimes,  by  the natives  of  the  south,  even  now.  The accuracv  of  the  definitions  of  India  in some  01  the  Greek  and  Roman  authors shows  the  existence  of  the  same  con- ception of  the  country  that  we  have now ;  a  conception  also  obvious  in the  modes  of  speech  of  Hwen  T'sang and  the  other  Chinese  pilgrims.  The A£6k&  inscriptions,  c.  b.g.  250,  had enumerated  Indian  kingdoms  covering a  considerable  part  of  the  conception, and  in  the  great  inscription  at  Tanjore, of  the  lltn  century  A.D.,  which  in- cidentally mentions  the  conquest  (real or  imaginary)  of  a  great  part  of  India, by  the  king  of  Tanjore,  Vira-Chola, the  same  system  is  followed.  In  a 2b
copperplate  of  the  11th  century,  by  the Chalukya  dynastv  of  Ealyana,  we  find the  expression  "  from  the  Himalaya  to the  Bridge"  (Ind.  Antiq,  i.  81),  %.e,  the Bridge  of  Rama,  or  *  Aoiam's  Bridge,'  as our  maps  have  it.  And  Mahommedan definitions  as  old,  and  with  the  name^ will  be  found  below.  Under  the  Hindu kings  of  Yijayanagara  also  (from  the 14th  century)  inscriptions  indicate  all India  by  like  expressions.
The  origin  of  the  name  is  without doubt  (Skt.)  Sindhu,  Hhe  sea,'  and thence  the  Great  River  on  the  West, and  the  country  on  its  banks,  which we  still  call  Sindh*  Bv  a  change common  in  many  parts  of  the  world, and  in  various  parts  of  India  itself, this  name  exchanged  the  initial  sibilant for  an  aspirate,  and  became  (eventually) in  Persia  Hindu,  and  so  })assed  on  to the  Greeks  and'  Latins,  viz.  *lvboi  for the  people,  *lvUt  for  the  river,  *lvbiK^ and  India  for  the  country  on  its  banks. Given  this  name  for  the  western  tract, and  the  conception  of  the  country  as  a whole  to  which  we  have  dluded,  the name  in  the  mouths  of  foreigners  natur- ally but  gradually  spread  to  the  whole.
INDIAN.
437
INDIGO,
first  Blow  at  Ormuz  .  .  .  they  have  added some  GhristiauB  to  thoee  formerly  converted by  St  'Diomafl,  but  it  is  a  loud  Report  to  say all  India."—.FVr,  137.
1881. — In  a  oorreepondenoe  with  Sir  R. Morier,  we  observe  the  Portuguese  Minister of  Foreign  AflFairs  calls  their  Goa  Vioeroy "The  Governor  General  of  India."
India  of  the  Datch.
1876. — The  Dorian  **is  common  through- out all  India."— jPt^  Plant-Kunditig  Woor- denboei,  196.
Indies  applied  to  America.
=== leaf
484
```


## [2026-09-14T03:10:36.698Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==244 {print}' SKT.txt | grep -n -E '^[0-9]{2,4}$|INFLUENCE|INDIGO' | head; echo \"=== first 300 chars leaf244\"; awk 'BEGIN{RS=\"\\f\"} NR==244 {print substr($0,1,300)}' SKT.txt",
 "description": "Skeat page number on indigo leaf"
}
```


### [2026-09-14T03:10:37.833Z] TOOL RESULT

```
21:INFLUENCE.
=== first 300 chars leaf244
 i  seeCraaoent.
Incubate,  IncubuB ;  see  Oovey.
Inciiloate ;  sec  Calk.
Inculpate :  see  Culpable.
Incumbent;  see  Covey.
Incur,  Incursion ;  ^ec  Currant.
Inounrate ;  see  Curve.
Indeed;  iceI>o<i>.
Indomnlf)^,  Indemnity ;  tee  Damn.
Indelible  ;  see  Delete.
Indent :  see  Dental.
Index
```


## [2026-09-14T03:10:38.227Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD watkins sindhu/syand\"; grep -n -i 'sindhu\\|syand\\|Indus' AHD_watkins1985.txt | head -20",
 "description": "AHD Watkins search"
}
```


### [2026-09-14T03:10:38.285Z] TOOL RESULT

```
== AHD watkins sindhu/syand
100:VENT, CONVENTION, etc.) or Germanic be- (BECALM, BECLOUD) can be shown to be a development of the individual languages af- ter the breakup of the common language. In Indo-European, such “compounds” repre- sented two independent words, a situation still reflected in Hittite and the older San- skrit of the Vedas (the sacred books of the ancient Hindus) and surviving in isolated remnants in Greek and Latin.
442:en. In. 1. Germanic *in in: a. Old English in, in: IN; b. Germanic (comparative) *inn(e)ra in Old English innera, farther in, inner: INNER; C. Germanic *innan in Old English binnan, within (be, by; see ambhi + innan, in, within): BEN!. 2, Latin in, in-, in, into: EN-!, IN-?. 3. Greek en, en-, in: EN-2; ENKEPHALIN, PARENCHYMA, PARENTHESIS. 4. Suffixed form *en-t/e)ro- in: a. Latin intré, inward, within: INTRO-; INTRODUCE, INTROIT, INTROMIT, INTRORSE, INTROSPECT; b. Latin inird, inside, within: ENTER, INTRA-; INTRADOS, INTRINSIC. 5. Suf- fixed form *en-ter in Latin inter, inter-, between, among: ENTRAILS, INTER-, INTERIM, INTERIOR, INTERNAL. 6. Latin (superlative) intimus (*-mo-, superlative suffix), innermost: INTIMA, INTIMATE?. 7, Old Latin endo, Latin indu-, within, in industria, diligence, activity (*stru-, to construct; see ster-2): INDUSTRY. 8. Suffixed form *en- tos in: a. Latin intus, within, inside: DEDANS, INTESTINE, INTINE, INTUSSUSCEPTION; b. Greek entos, within: ENTO-. 9. Suffixed form *en-tero- in Greek enteron, entrails: ENTERIC, ENTERO-, ENTERON; DYSENTERY, MESENTERY. 10. Extended form *ens in: a. Greek eis, into: EPISODE; b. suffixed form *ens-6 in Greek esd, within: ESOTERIC. 11. Suffixed zero-grade form *n-dha possibly in Germanic *anda, *unda in Old English and, and: AND. [Pok. 1. en 311.]
1018:ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
```


## [2026-09-14T03:10:55.953Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"; n=0} {n++; if ($0 ~ /(^|\\n)[ \\t]*26[0-9][ \\t]*(\\n|$)/) print \"leaf \"n\": \"substr($0,1,80)}' SKT.txt | head -20",
 "description": "Find Skeat printed page markers 260-269"
}
```


### [2026-09-14T03:10:56.982Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:10:58.226Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON masxareh\"; grep -n 'مسخره' MON_part1.txt MON_part2.txt | head -5; echo \"== MON mask\"; grep -n 'ماسک' MON_part1.txt MON_part2.txt | head -5; echo \"== MON sheypur\"; grep -n 'شیپور' MON_part1.txt MON_part2.txt | head -5",
 "description": "Mo'in greps"
}
```


### [2026-09-14T03:10:58.342Z] TOOL RESULT

```
== MON masxareh
MON_part1.txt:40527:(مص ع.) مسخره کردن» رشخند کر دن. 
MON_part1.txt:57589:بخندند و او را مسخره کنند. (.) ریشخند» 
MON_part1.txt:61304:(عم.) مسخره کردن» رشخند کردن؛ ملعبه 
MON_part1.txt:61427:مسخره واقع شود. عاجز» زبون. آنجه که 
MON_part1.txt:73548:مسخره کننده» استهزا کننده» مستهزی. 
== MON mask
MON_part1.txt:20555:بماسکت بال: ۱29۲۰-121 [- سک تال ] 
MON_part1.txt:20932:سال‌ماسکه: 6 2 (امر.) مجلس 
MON_part1.txt:58992:ماسکه. 
MON_part2.txt:15423:ماسکه: (فد.) قوتی است در نبات که مواد 
MON_part2.txt:17991:ماسک یا بدون آن که سوار اتومبیل و 
== MON sheypur
MON_part2.txt:791:شیپوری و مخاط گونه را سوراخ کرده و 
MON_part2.txt:36365:سندانی و استخوان رکابی. شیپور استاش که 
MON_part1.txt:14135:از تيرة بادنجانیان با گل‌های شیپوری و 
MON_part1.txt:25071:(افا. امر.) (فز.) آلتی است به شکل شیپور که 
MON_part1.txt:26149:بزرگ» کرنای. نوعی از شیپور کوتاه که
```


## [2026-09-14T03:11:11.608Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 MON_part1.txt; echo \"...\";  grep -c $'\\f' MON_part1.txt MON_part2.txt; grep -n 'pdf page' MON_part1.txt | head -3; ls -la MON_part1.txt MON_part2.txt",
 "description": "MON file structure"
}
```


## [2026-09-14T03:11:12.484Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1319 2>&1 | head -60",
 "description": "Fetch BQT page 1319"
}
```


### [2026-09-14T03:11:12.599Z] TOOL RESULT

```
0 
2 


چم 
...
MON_part2.txt:0
MON_part1.txt:0
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
```


### [2026-09-14T03:11:22.438Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 114; check the printed number and re-run with --pdf-page if off)
REF: BQT:1319  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 114  OCR-lang: fas

: شیراز
برامر صدّحة ۹۳۹۹
8 1
ِ 5
1 5
1 :
زا 5
: ۹
[م ۳ 1
۹ 5
1 و و
ی ِ«
ا ۱ ۴ و :
7 9 در از
10 ود ااباد
۸1 سارت 1 :
» ۳ :ی ۳ : ما و۳۹
1 9 ی 5 سا ِ
ام تس
+ کت بر ی ۱
زا
۱ رها خی 1
له مس
۳
وه
+ لا شتسه ۳
ل ن رم #
```


## [2026-09-14T03:11:26.589Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'شیپور' incoming/BQT/BQT_v3_pages.txt | head -10; echo \"=== v2\"; grep -n 'شیپور' BQT_v2_pages.txt | head -5",
 "description": "BQT grep sheypur"
}
```


### [2026-09-14T03:11:26.661Z] TOOL RESULT

```
2764:‏۱ - ممرب ‎OT‏ «شبور» (بنتح اول وضم دوم مشدد) » بوق «نفی» قس: شیپور -
8489:‏همان سنج وشیپور وهندی درای»
8496:. ‏قیبور - رك : شیپور‎ #
=== v2
```


## [2026-09-14T03:11:28.534Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFA shofar/sipura\"; grep -n -i 'sipura\\|šipūrā\\|Schofar\\|sofar\\|Trompete' AFA.txt | head -20",
 "description": "Fraenkel trumpet"
}
```


### [2026-09-14T03:11:28.638Z] TOOL RESULT

```
== AFA shofar/sipura
```


## [2026-09-14T03:11:33.331Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8470,8500p' incoming/BQT/BQT_v3_pages.txt; echo \"=== page tag before 8489\"; awk 'NR<=8489 && /pdf page/ {last=$0; n=NR} END{print n\": \"last}' incoming/BQT/BQT_v3_pages.txt",
 "description": "BQT sheypur entry context"
}
```


### [2026-09-14T03:11:34.529Z] TOOL RESULT

```
- اس ال از * شیبیدن» -
۴ - رك : شیبیدن . ِ-

۷ - رك : تیب وشیپ ‎eet‏ ولیپ .

‎Ole‏ از زخم آنها با شکیبا
۴ - متعدی «شیبیدن» .
سم فاعل از «شببیدن».

‏. «قاباص ۸-۱۹۷ ۰ .

‎ta ۱‏ آعیخته شونده.
۸ = شیبور . هردو درشاهنامه ‎oul‏ حر

‏فپرست ولف آندو به ‎Trompete ۰ Tuba‏ )5.2( ترجمه ‎read‏

‏بفرمود تا بر کشیدند دای

‏همان سنج وشیپور وهندی درای»

‎ANAS Neg ‏«شاعنامة‎

‏#بپور ازآرامی وسربالی گرفته شده «نقی زاده ‎Uae‏ باد کار

‎LOTT ‏چپارم‌شمار؛‎ JL
. ‏قیبور - رك : شیپور‎ #
[pdf page 111]
Sx

کرت ‎SHYT‏ رومی یز ‎lye‏ و بفتح
=== page tag before 8489
8399: [pdf page 110]
```


## [2026-09-14T03:11:50.406Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T03:11:50.413Z] TOOL RESULT

```


```


## [2026-09-14T03:11:52.379Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD sheypur\"; grep -n -i 'šyp\\|šēpūr\\|sepur\\|šayfur\\|trumpet' PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB\"; grep -n -i 'trumpet\\|šēpūr\\|šypwr' NYB_vol2_glossary.txt | head -10",
 "description": "MacKenzie/Nyberg trumpet"
}
```


### [2026-09-14T03:11:52.459Z] TOOL RESULT

```
== PHD sheypur
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
PHD.txt:2312:horn srū; (trumpet) gāwdumb.
PHD.txt:4080:trumpet gawdumb.
PHD_mackenzie.txt:2490:gaw-dumb [g'fidwmb 1 N ......dum] horn, trumpet.
PHD_mackenzie.txt:6782:hen kark.                                      horn sru; (trumpet) gawdumb.
PHD_mackenzie.txt:7814:totality hamagih.                        trumpet gawdumb.
== NYB
```


## [2026-09-14T03:11:57.447Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D9%BE%D9%88%D8%B1",
 "prompt": "Give the full Persian entry for شیپور: etymology (Aramaic/Syriac? Middle Persian form?), meaning, and any cited sources (Hasandust, etc.)."
}
```


## [2026-09-14T03:11:58.601Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mask",
 "prompt": "Full etymology of mask, and any mention of masque, masquerade, mascara, Italian maschera, Medieval Latin masca, Arabic maskharah."
}
```


### [2026-09-14T03:12:02.491Z] TOOL RESULT

```
# Persian Entry: شیپور

**Transliteration:** šaypūr / šeypur

**Meaning:** Bugle, horn, or trumpet

**Etymology:** The word derives from Aramaic שֽׁיפּוּרָא / שֽׁפּוּרָא (šippūrā) or Syriac ܫܝܺܦܘܿܪܳܐ (šippōrā), meaning "trumpet, shofar." This Aramaic origin also influenced the Arabic form شَبُّور (šabbūr).

**Alternative Forms:** شپور (špūr), شیبور (šaybūr/šeybur)

**Cited Sources:**
- Dehkhoda Dictionary (Ali-Akbar Dehkhoda, 1931–)
- Nöldeke, Theodor (1892), *Persische Studien*
- Vullers, Johann August (1856–1864), *Lexicon Persico-Latinum etymologicum*

The entry indicates no Middle Persian form is documented, only the modern Persian word alongside its Semitic linguistic ancestry.
```


### [2026-09-14T03:12:04.255Z] TOOL RESULT

```
# Etymology of Mask

The word "mask" has a complex etymological journey. First documented in English in the 1530s, it comes from French *masque*, which derives from Italian *maschera*. The Italian term traces back to Medieval Latin *masca*, meaning "mask, specter, nightmare."

## Uncertain Origins

Scholars debate the ultimate source. One theory links it to Arabic *maskharah*, meaning "buffoon, mockery." Alternatively, it may stem from Provençal or Catalan roots related to blackening or darkening the face, possibly from Germanic sources akin to English "mesh."

Some etymologists propose a pre-Indo-European origin through Occitan *mascara* ("to blacken, darken"), where *masco* meant "witch" in Old Occitan dialects.

## Related Terms

The figurative sense—"anything used for disguise or concealment"—emerged by the 1570s. The verb form appeared in the 1560s meaning "to take part in a masquerade," later evolving to mean "to wear a mask" or "disguise feelings."

Connected words include *masquerade* (from 1590s), *mascara*, *masque*, and *unmask*. The term *masking tape* (1927) received its name because it "is used to block out certain surfaces before painting."
```


## [2026-09-14T03:12:09.169Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AE%D8%B1%D8%A9",
 "prompt": "Arabic مسخرة: etymology (root س خ ر sakhira), meaning, and any Persian/Ottoman/Italian descendants listed."
}
```


## [2026-09-14T03:12:11.252Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Aryan/sindhus",
 "prompt": "Etymology of Proto-Indo-Aryan *sindhus / Sanskrit सिन्धु: is it derived from syand- 'to flow'? What do Mayrhofer and others say? List descendants including Old Persian Hinduš, Avestan Həndu."
}
```


### [2026-09-14T03:12:12.585Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T03:12:14.367Z] TOOL RESULT

```
# مسخرة (maskhara)

**Meaning:** This Arabic noun refers to "object of ridicule, laughing stock."

**Etymology:** The word derives from the Arabic root س خ ر (s ḵ r).

**Descendants:** The term spread across multiple languages through Persian and Ottoman Turkish intermediaries:

- **Persian route:** Classical Persian مَسْخَرَه (masxara) led to adoptions in Bengali (moskora), Hindi (masxarā), Urdu, Punjabi, Turkmen, Uyghur, and Uzbek.

- **Ottoman Turkish route:** Ottoman مسخره (meshare) evolved into modern Turkish maskara and influenced Crimean Tatar variants.

- **Other descendants:** Armenian մասխարա, Georgian მასხარა, Azerbaijani masqara, and Swahili masihara also trace back to this Arabic root.
```


## [2026-09-14T03:12:18.186Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A7%E0%A5%81",
 "prompt": "Sanskrit सिन्धु sindhu: etymology (from syand- 'to flow'? Mayrhofer's view?), meanings (river, Indus, sea), and descendants (Old Persian Hinduš, Avestan Həndu, Greek Indos, Persian هند)."
}
```


## [2026-09-14T03:12:20.663Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D9%86%D8%AF%D9%88%D8%A7%D9%86%D9%87",
 "prompt": "Persian هندوانه hendevāne 'watermelon': etymology, morphology (هندو + انه?), and any cited sources."
}
```


### [2026-09-14T03:12:25.519Z] TOOL RESULT

```
# सिन्धु (Sindhu) - Sanskrit Etymology and Meanings

**Primary Definition:**
The word सिन्धु (síndhu) is a Sanskrit noun meaning "river" or "stream," with special reference to the Indus River.

**Etymology:**
The term derives from Proto-Indo-Iranian *síndʰuš, inherited through Proto-Indo-Aryan. The etymology page presents two theories:

1. Possibly borrowed from the BMAC substrate
2. Alternatively connected to सेधति (sédhati), meaning "to go, move"

The page also notes a potential connection to Burushaski सिंदऋ (sínda), suggesting shared roots with words meaning "river" across regional languages like Shina and Pashto.

**Key Meanings:**
According to the dictionary entry, सिन्धु encompasses:
- A river or stream (especially the Indus, notably masculine gender)
- The personified goddess form in Vedic religion
- Flood or waters
- Ocean or sea
- Symbolically, the number 4

**Linguistic Descendants:**
The term influenced numerous modern languages, including Hindi (सिंधु), Urdu (سندھ), Tamil, Telugu, and even entered Old Persian as Hinduš, ultimately contributing to the English "Indus."
```


### [2026-09-14T03:12:27.146Z] TOOL RESULT

```
# Persian هندوانه (hendevāne) – Watermelon

## Etymology

According to the Wiktionary entry, the word is formed through **surface analysis** combining:

- **هندو** (hendu) meaning "Indian"
- **ـانه** (-âne) as a suffix

This morphological composition suggests the term literally translates to something like "Indian [thing]," reflecting the fruit's origins or associations.

## Linguistic Details

The word appears across multiple Persian varieties with slight pronunciation variations:
- Classical Persian: /hin.du.waː.ˈna/
- Iranian Persian: [hen̪.d̪e.vɒː.ne]
- Tajik: [hin̪.d̪u.vɔ.nä]

## Related Information

The entry documents that هندوانه has spread to related languages including Pashto, Punjabi, Sindhi, and others—demonstrating its significance as a loanword throughout the region. Synonyms in Persian include **تربز** (tarboz).
```


## [2026-09-14T03:12:47.859Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT hindu\"; grep -n 'həndu\\|hǝndu\\|Həndu\\|hindu\\|Hindu\\|hapta hindu\\|Hapta' BRT.txt | head -20",
 "description": "Bartholomae Hindu"
}
```


### [2026-09-14T03:12:47.912Z] TOOL RESULT

```
== BRT hindu
8700:•  j,  u^as'tara-  Adj.  'gegen  Morgen  ge- legen, östlich':  °taire  kinävd  (sd.)  , .  daosa- taire  V.57.29;  —  haca  °lara  hindva  (sd.) avi  daosaslanm  hindum  V.J.  18  PüZ.;  — -taräl  haca.  nalmitt  °taraalyi>  haca  nai- maiibyS  V.  ig.  5,
8998:ai.  kadn,  np  lai  'wann?'  —  Pü.;  kai  an  da- kün,  (zu  V  9)  ini,  (lu  Yt  /):  fixön  ka,  (lu Y.  29,  V.  /(;)  (i^j/f  —  ')  Die  häufige  Ver- hindung  kaia  m  (6mal)  ist  bemerk ensirert; s.  nd  mit  No  1  und  Lu%a  II  (sd.).  —  ')  An der  ParalleUt  H  2  10  steht  ka%a.  —  3>  So ■      F  1,  J  10  US»  .  NA    iai
10061:mit  vX  i)  'hindurchgehen,  durchdringen': absolut:  VJ  antar»  zqm  asmatumla  sota- vaiiS  vljassiti  Yt.  13.  44.  a)  '(durch- dringend) sich  verbreiten  hin  zu  — ,  über  — ' (Akk.  oder  avi  mit  Akk.  oder  ä  mit  Akk.) : yeiihe  v/lxs  .  .  vi  iapta  karfvqn  /asaüi Yt  io.  85;  —  awrä  urväiti/(sd.)  ..  vi/a- säitls  ..  hapta  karsvqn  YtÄ4o;  — kS  vilxs  .  .  vTjasäl  vtspäis  avt  karlvan Yt;o,89;  —   apayzam  *vlJasaiH  vtspais
11581:•  j.  jayäi  Inf.  'zu  schwächen,  zu  ent- kiäften':  yB  saSe  haurvam  taras^a  xsa- fan^m  üyaumnB .  .  j°  cinvat.idtämm  "der die  ganze  Nacht  hindurch  liegend  ruht, ohne  zu  beten  . .,  um  den  zu  entkräften, der  ihm  nach   dem  Leben,  trachtet"  V.
14580:•  '].  STi.ayar-  n.  'Zeit  von  drei  Tagen': As  ava%a  vazata  °nm  ^ri.x/apanm''' ", .  drei  Tage  und  Nächte  hindurch"  Yt 5.62;  S.22;  —  °r3m  ^rijxsapanm^'  tanüm frasnayayanta  "während  dreier  Tage  .  ." Yt/o.iaa;  V.p.sö.
15340:•  j.,  g. 'par- V. 'hindurch-,  hinübergehen*,  53-1-         a)}Aw.  in  der  Verbindung  «<-i((Sp.
21669:das  ganze  Jahr  hindurch  ununterbrochen       mit    apa    'wegnehmen' :   ys   main    tai dauernd':   yam(ca)   huiltlm  (sd.)    5. 2. 6 ;' draonlf  tinaj  (sd.)  jrä  tr>fyai  vä  apa  i-a Y.  2. 6,  G.  it  ro;  —  'yayä  i^'yayäilä)  husi-  yäiaiti  Y.  11. 5. Wir  S.  /.  6;  Y.  I.  6.         z)  m.  Name  der!     mit  a   r)  'herholen,  holen';   a  aBma
24994:g.  ra/S  V.  SS-  9:  lies  '^'J"- •  j.  'ratav- :  ra%w-  m.  'Zeitabschnitt,  Zeit- raum': yiy  %rizar>mafm  •tum  aiwyi'ahqm (sd.)  ndit  amyasli  ".  .  einen  drei  Früh- linge umfassenden  Zeitraum  hindurch  .  ." V.  18.  9;  —  kamaspahmaldalm  paiti  °tQm Yt.  13.  4g;  Vd.  2/;  —  ksvattlm  (sd.)  S  'tum a    haoms    upait    sard^uHnm   Y.5.  i;  —
30540:•  j-,  g.  hu-sitay-  f.  i)  im  gAw.;  a)  'gutes Wohnen':  kads  .  .  ärmaitii  jintat  (Sp. 494  m.)  xsdhrä  'Mtis'''  västravaiii  Y. 4S.11;  — yä  'I^lli'^  rämqm(sd-)cä  dät Y.  25.  10.  b)  'gute  Wohnung,  Wohn^ statf :  at  asistä  yaojanis  (sd.)  ä  'sitsil vaiahJui  manaahö  masdä  asahyacä  Y. 30.  10.  a)  im  jAw.  mit  ysirya-  Adj. 'das  ganze  Jahr  hindurch  währendes  gutes
```


## [2026-09-14T03:12:48.862Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT hindu\"; grep -n -i 'hindu\\|hidu' KNT_full.txt | head -20",
 "description": "Kent Old Persian Hindu"
}
```


### [2026-09-14T03:12:48.914Z] TOOL RESULT

```
== KNT hindu
209:are cited in the form fixed by the Hindu gram- 
6878:§125. Guna AND Увррні: The Hindu gram- 
6888:respondences; note that to the Hindu gram- 
8602:Haraiva ‘Aria’; Hidus Sind’. 
8680:writing for @atagudiya, Hiduya for Hiduviya. 
8728:Hiduš Hiduya* 
9414:gus, Babiru’, Māļruļš, Margus, Hindu. 
19282:25 dara : Hidug : Saki : haumavargà : Sa 
19818:24 уй : Gadàra : Hidus : Зака : haumava 
20300:10 8atagut : Harawvati$ : Hidus : Skudra : Yound : taka 
21175:25 ty : Maeiy& : Arabaya : Садага : Hiduš : 
21875:: Hiduya 
27264:par- vb. ‘communicate’: Av. *par- ‘hindureh-, 
29835:du-iš; Ау. hindu-, Skt. sindhu- ‘stream, the Indus, 
29837:$158.I). See also Hiduya-. Hidus nsm. DPe 
29845:ceding ($27, §144.1II). Hiduya пзш. А?Р 13.
```


## [2026-09-14T03:12:55.600Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29830,29850p' KNT_full.txt; echo \"=== BRT hindu headword\"; grep -n 'hindu-\\|hindav\\|Hapta hindu\\|hapta  hindu' BRT.txt | head -10",
 "description": "Kent Hidu entry and BRT hindu"
}
```


### [2026-09-14T03:12:55.668Z] TOOL RESULT

```
Gr. $129, cf. Kent Lg. 19.226-7. 


Hi"du- sb. ‘Sind’, a province of the Persian 
Empire, on the upper Indus River; Elam. hi-in- 
du-iš; Ау. hindu-, Skt. sindhu- ‘stream, the Indus, 
country around the Indus’ (§27, §111, §118.V, 
$158.I). See also Hiduya-. Hidus nsm. DPe 
171; DNa 25; DSe 24°; DSm 10°; XPh 25. 
Hidaw lsm. as abl. ($251D), DPh 7; DSf 44 
(йш; not hidat = Hiddva as taken by Scheil 
21.18, Konig Burgbau 34, Bv. Gr. §318); DH 5f. 


Hi”duya- adj. ‘(man) of Sind’: deriv. to pre- 
ceding ($27, §144.1II). Hiduya пзш. А?Р 13. 


hya nsm., hyd nsf., rel. pron. and def. art.; cf. 
similar forms in Skt. (Vedic) syd-s sya ‘this’: con- 
tamination of demonst. Av. Һб hà, Skt. sa-s sd, 
=== BRT hindu headword
7594:11  hindav-  No.  1 ;  doch  vgl.
10480:lum  Praes.  17,   vgl,  unter  hindav  No.  1.   —  varaiä  karapä  xsainmc,!  isanqin    drujim
21505:a\.ydsyaH,  yf^ati;  yas/äi;  np. jasian  (?,  GlrPh. /b.  139),  PDw.  yaiin  {?,  GlrPh.  /  b.  Z98).  — PQ.!  »da«  ßaa,  •eitUait,  Sä.  {lu  Y.p):  mala- vatT  'schmutzig'  (,  weil  man  hixr°  Im)*}.  — ')  Nicht  ganz  sicher,  da  'l>ni°  fiir  'siitf  ge- schrieben sein  kann;  s.  hindav-  No.  I.  — ">  /  müEste  vom  redupl.  Praeseos  stammen. Statt  yaihliiyS  im  Text  schreibt  DST,  in  der Note  yokiH'.  VII.  ist  beide»  falsch.  Ob yaihnübyöt  —  J)  Vgl,  No.  i.  —  4)  M  hat aestnüm,  K  yaisinlim;  s.  noch  No.  I.  — S)  Und  deshalb  überwallenden.  —  «)  Vgl.  Dst. ZA,  3.  II.  Jamaspji  Gloss,  475-  476  bat aySrRjn^d  'surpasses', j.  yahi  Yt.  10.  64:  lies  yalimi;  5.  ya-  mit No.  17.
23031:—  4)  Hdi.  vtrixanOm.  —  S)  Sollte  vmänüm «ein.  Geringe  Stelle.  —  *)  Vgl.  iBed.  np. varz,  iari  'Feldarbeit,  Ackerbau'.  —  7)  So  T; s.  hindav-  No.  I.  —  *)  Hds.  virnant'.  — 9)  So  K  7  ■.  NA.  yä/qm,  Pü. :  varsisnak.  — «•)  S,  »Bed,  Gdh.  BB.  12.  98.  —  »')  Pü. :  an i  aoiäi  ape  vartÜn,  —  ")  PO.:  an  släyUn M  nyäyäti  an  i  amäi  ape  ■Borvsn.  —  'J)  Ptt.  1 uniariitan,  erL  (zu  V.  7^):  apäl  karlati,  (zu V.  4,  13)  i  api  vicärlBH.
23196:ai.  vihati,  ukyäte  (Praet.  37,  Fass.]^  uhl,  vaksai; ; udhäh,  vähadhyai;  mp.  voiSlan  'dahin fahren', , rp.  i'.ijrH'fl« 'wehen',  afj.  po/ii/ 'fliegen' (Praes.  I vuzt],  sbal,  gvcaag,  ZDg.  vailmün  'laufen'.  — Pü. !  vaätan,  vazemlan;  s.  noch  No.  6  ff-  —  ' I)  Nur  im  Abiol.  —  '>  S  W  H;  »■  dagegen  • ai.  üijh^.  —  »  S  /a/  g.  Wertlos  Wilhelm  | Mus.  3.  600.  —  4)  Stall  vaänii,  lu  S  325  No.  ■ S.  hindav-  No.  I.  —  s)  Them.  —  &)  Pü. : vastnit;  s.  zu  vaou  Inf.  —  7)  Es  handelt  sich  | Dm  einen  Kamof,  bei  dem  die  Entscheidung nicht  fallen  will.  Anders  Gdn.  sYI.Si,  Dst. ZA.  3.  572.  Npü.  (fOc  vailiakS):  ml gardadA —  S)  Pü.:  nap  an  (Mills  iivawfn),  Sü.:  svämi-^ iämitü.  —  9>  Unsicher;  vlL  haplol,  für *avcaa>:  —  ")  Fehlt  in  Pü.  —  ")  Pü.  erL; buland  e  sar  .  .  fröt  ö  bun.
24802:ai.  risyixii  'ei  tut,  nimmt  Schaden',  refäyali 'er  tut  Schaden',  ri}/iiA;  mp.  resilan.  —  Pü. : reiitan,  zu  3  a  erl. :  api  murtan.  —  ■>  Pü. : ku  ne  an  i  pas  Ö  i  pis  etön  relet.  —  ')  S.  zu hindav-  Nu.  I.  —  J)  Hds.  'hntanqm.  —  4)  Hd». airiyq.
25498:')  Nur  *Unl'  und  (V.  7.  38)  -httl*  (s.  hindav- No.  1).
25567:Vgl.  BgE.  wrig^an  USW.l  HBIL  IF.  //.  lOa  — Pü. :  variVan.  — ')  )  «att  i  für  y^,  vgl.  No.  8. S.  hindav-  No.  I.  —  •)  In  aA%5iriSta:  — J)  Hd».  urvityeiU;  Fü. :  fehlt.  —  «  NA.  'saiU; j.Vat.  —  S)  S  363.  44.  —  *)  NA,  'urvaiiaiU;  l. Var.  —  7)  S  368.  31.  —  ")  So  Fl  uiw.j  NA. 'tirtti;  t.  No.  I.  —  9)  NA.  'saiH',  ■.  Var.
26638:dieErl.!  THnäsiä'r  6i/an*),  bi.*fl/-/oif.  — 'o  Vgl. zu  lap-  No.  l.  —  »)  Them.  NA  hat  das  gani unglaubwürdige  siaiava^  (ZDMG.  43.  530).  — J)  Hds.  äitärayeili.  —  4)  Statt  •rinti  >=  'rysnti geschr. ;  i.hindav- 1\0.  i.  —  i)  Die  Konstruktion wechselt  zwischen  LS.  (statt  15.)  und  AS.  — ^)  Das  Praev.  ä  ist  doppelt  geseilt.  —  7)  Hds. äslräinli,  PQ.:  ästatinend.  S.  jSL  BtHL.  IF. /a.  118.  l&ipara  richtig?  Pü.  lässt  es  aus.  — 8)  Auch  als  Übersetiung  (N.  jo).
26971:Komp.  •ja-i-ai\  S  301?.  3.  —  statt  sfin)' gesclir,,  vgl.  L4  und  »u  hindav-,  sowie  die  mp. Traniskr.  lu  Bd.  //.  I  {sfiajatr).  —  S.  auch spinjauruika:  —  0  Von  jamm  abhängig  lu zu  denken;  vgL  RV.  7.  41.  6:  räyiskämo viivdfsnyasya.
```


## [2026-09-14T03:13:01.322Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'hapta\\.h\\|Hapta\\.h\\|haptahindu\\|hindav' BRT.txt | sed -n '1,30p' | cut -c1-300; echo \"=== search Indien\"; grep -n 'Indien' BRT.txt | head -10",
 "description": "Bartholomae hindav entry"
}
```


### [2026-09-14T03:13:01.396Z] TOOL RESULT

```
7594:11  hindav-  No.  1 ;  doch  vgl.
10480:lum  Praes.  17,   vgl,  unter  hindav  No.  1.   —  varaiä  karapä  xsainmc,!  isanqin    drujim
21505:a\.ydsyaH,  yf^ati;  yas/äi;  np. jasian  (?,  GlrPh. /b.  139),  PDw.  yaiin  {?,  GlrPh.  /  b.  Z98).  — PQ.!  »da«  ßaa,  •eitUait,  Sä.  {lu  Y.p):  mala- vatT  'schmutzig'  (,  weil  man  hixr°  Im)*}.  — ')  Nicht  ganz  sicher,  da  'l>ni°  fiir  'siitf  ge- schrieben sein
23031:—  4)  Hdi.  vtrixanOm.  —  S)  Sollte  vmänüm «ein.  Geringe  Stelle.  —  *)  Vgl.  iBed.  np. varz,  iari  'Feldarbeit,  Ackerbau'.  —  7)  So  T; s.  hindav-  No.  I.  —  *)  Hds.  virnant'.  — 9)  So  K  7  ■.  NA.  yä/qm,  Pü. :  varsisnak.  — «•)  S,  »Bed,  Gdh.
23196:ai.  vihati,  ukyäte  (Praet.  37,  Fass.]^  uhl,  vaksai; ; udhäh,  vähadhyai;  mp.  voiSlan  'dahin fahren', , rp.  i'.ijrH'fl« 'wehen',  afj.  po/ii/ 'fliegen' (Praes.  I vuzt],  sbal,  gvcaag,  ZDg.  vailmün  'laufen'.  — Pü. !  vaätan,  vazemlan;  s.  noch  No.  6  ff-  —  ' I)
24802:ai.  risyixii  'ei  tut,  nimmt  Schaden',  refäyali 'er  tut  Schaden',  ri}/iiA;  mp.  resilan.  —  Pü. : reiitan,  zu  3  a  erl. :  api  murtan.  —  ■>  Pü. : ku  ne  an  i  pas  Ö  i  pis  etön  relet.  —  ')  S.  zu hindav-  Nu.  I.  —  J)  Hds.  'hntanqm.  —  4)  Hd». 
25498:')  Nur  *Unl'  und  (V.  7.  38)  -httl*  (s.  hindav- No.  1).
25567:Vgl.  BgE.  wrig^an  USW.l  HBIL  IF.  //.  lOa  — Pü. :  variVan.  — ')  )  «att  i  für  y^,  vgl.  No.  8. S.  hindav-  No.  I.  —  •)  In  aA%5iriSta:  — J)  Hd».  urvityeiU;  Fü. :  fehlt.  —  «  NA.  'saiU; j.Vat.  —  S)  S  363.  44.  —  *)  NA,  'urvaiiaiU;  l. V
26638:dieErl.!  THnäsiä'r  6i/an*),  bi.*fl/-/oif.  — 'o  Vgl. zu  lap-  No.  l.  —  »)  Them.  NA  hat  das  gani unglaubwürdige  siaiava^  (ZDMG.  43.  530).  — J)  Hds.  äitärayeili.  —  4)  Statt  •rinti  >=  'rysnti geschr. ;  i.hindav- 1\0.  i.  —  i)  Die  Konstruktion wechs
26971:Komp.  •ja-i-ai\  S  301?.  3.  —  statt  sfin)' gesclir,,  vgl.  L4  und  »u  hindav-,  sowie  die  mp. Traniskr.  lu  Bd.  //.  I  {sfiajatr).  —  S.  auch spinjauruika:  —  0  Von  jamm  abhängig  lu zu  denken;  vgL  RV.  7.  41.  6:  räyiskämo viivdfsnyasya.
30078:3)  S.  daiu  Hopkins  JAOS.  i6.  278  (lu  RV.  S. *4-  27). j.  US  hindavai  Yt.  8.  32:  lies  us.hindanal.
=== search Indien
8493:pD.:  transskr.,  erL:  laFiäit;  s.  dain  DsT.  ZA. z.  II,  Marquart  EranSahr  40.  —  ')  «tu- oder  "/wi'ii-?  —  ')  Ganz  anders  Gck.  OK,  86, der  i',  an  der  Gienie  Indiens  sucht.
8579:"  j.  *us.h«ndava- '^  Adj,  'jenseits  vod Indien  gelegen',  m\\.garay-  m.  Name  eines Gebirgs '';  äat  tat  dunmqn  hqm.hUt»nti •rat  haca  garöit  y5  Aistaite  maioim  zra- ya»hö  vourukasahe  \x.8.yi,
16994:*>  Über  die  Pflanien,  von  denen  die  Zweige geschnitten  werden  dürfen,  bieten  die  älteren Texte  keine  genaueren  Mitteilungen;  N.  90 PüErl.  (Blatt  16/.  ig)  ist  nicht  recht  deutlich. In  Indien  braucht  man  jetzt  ans  Metall  herge- stellte Zweige.  Die  Mindestzahl  wird  N.  po  auf drei  angegeben;  Y.  57.  6  werden  die  Zahlen 3>  S>  7>  9  genannt.  Als  Höchstzahl  etscheint N.  90  PüErl.  (Blatt  t6S.  1)  551.  Für  gewöhn- lich schwankt  die  Zahl  zwischen  5  und  33,  der Zahl  dcT  ra/rij'ö f airi!,Aä-!i/iHayB  (sd.).  Ober  Grösse und  Stärke  der  Zweige  s.  Y.  J/.  6,  N.  yo,  po, V.  /p.  19.  Die  Zusammenfassung  der  Zweige  zu einem  Bündel  geschieht  mittelst  des  aiwyio- ^nna-'Cürter  (Sp.  98  m.),  wozu  man  heutzutage ein  Datlelblalt  verwendet.  Die  gebündelten Zweige  ruhen  auf  dem  Gerätetisch  (aräVoi^) vor  dem  ZaMar.  Weiteres  bei  Hauo  Essays» 396  f.,  West  SBE.  5.  »84,  '8.  142.  3y-  162. DsT.  ZA.  /.  LXJüiL  Der  Terra,  techn.  für  das Bündeln  des  B.%  ist  ^slar-  'stemere'.  Dies  sowie die  Etymologie  von  b'  weisen  darauf  bin,  das« der  Gebrauch  des  B.  sich  aus  dem  'Spreiten der  Opferstreu'  (ai.  barhifah  slärimä)  entwickelt hat;  %.  datn  OuiENSEiic  Rel.  des  Veda  343.
30076:•  j.  bindav-,  h«ndav-",  p.  hi°dav-  m. Name  eines  Lands,  Indien:  II  imä  dahyava^ tyä  adam  agarbäyam  . ,  'du/  D.  5.  3 ;  5.  2 ; —  Aaca  us'as/ara  'dva  avi  daolastanm 'dum  V.J.  r8  PiiZ.;  —  yH^i  ulastaire •dvS  *ägiurvayeiii  yatSt  daoiataire  niytu "auch  wenn  er  im  Östlichen  Indien  ist, er  packt  (ihn);  auch  wenn  er  im  west- lichen ist,  er  schlägt  (ihn)  nieder"  Y. 57.  2g.  a)  mit  Aapla  'sieben'  dn.: paniadasfm  asunhamca  . .  frä'^wirtsfm  . , yS  Aapta  'du  (AP.)'»  V.  /.  i8.
```


## [2026-09-14T03:13:12.904Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo -n \"BRT leaf=\"; awk 'NR<=30076' BRT.txt | tr -cd '\\f' | wc -c; echo -n \" KNT leaf=\"; awk 'NR<=29835' KNT_full.txt | tr -cd '\\f' | wc -c; echo; echo \"== MON masks\"; grep -n 'ماسک' MON_part2.txt | head -20 | cut -c1-200",
 "description": "Leaf numbers + MON mask"
}
```


### [2026-09-14T03:13:13.992Z] TOOL RESULT

```
BRT leaf=986
 KNT leaf=0

== MON masks
15423:ماسکه: (فد.) قوتی است در نبات که مواد 
17991:ماسک یا بدون آن که سوار اتومبیل و 
42419:ماسک: 2 (۰۱) آنجه که چهرة خود را 
46942:ج. متماسکین. 
48810:ای رجا رخاماسکی پر دعس بت سم ود شاد اما اند تن عفد ممطلن | 
78135:وسله ِِ سازند؛ ماسکك. نقاب فرو
```


## [2026-09-14T03:13:14.622Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN hind\"; grep -n -i 'hindū\\|hindu\\|Indien' HRN.txt | head -10 | cut -c1-250; echo \"== HUB\"; grep -n -i 'hindu\\|Indien' HUB.txt | head -10 | cut -c1-250",
 "description": "Horn/Hübschmann Hindu"
}
```


### [2026-09-14T03:13:14.747Z] TOOL RESULT

```
== HRN hind
310:noch das Wort hädisäh nennen, das in Indien mit einer
1175:*) Auch in Indien spricht man nur Waden,
2565:Zeile 5 y. u. Auch in Indien spricht man heute nur l.- 58 —
3070:In Indien spricht man piser ; die nämUche Aussprache soll auch
3834:407. tere *finster , tereyt^) (auch in Indien spricht man heute
6844:tiere I-, 545: 'Der Schakal verbreitet sich' von Indien
7408:*) Auch nuf persischen Inschriften in Indien, vergl. Epigraphia
7625:•) Repristinirt auf Inschriften in Indien, Hörn, Epigraphia in-
9230:in Indien spricht man heute nlst.- 239 —
9475:braucht man in Indien auch hised (auf Inschriften
== HUB
1439:giessen* (Horn p. 267) fiir *ahindUan.
3289:Kleides, wo der Kopf hindurch gesteckt wird', spater
7615:Hagmatdna- ') ; Hind = ap. Hindu- Indien ; Hindu Inder
7616:= phi. Hinduk^ arm. Hndik-K Indien', Hnduk Inder Mos.
7634:HaxUmanii; ^Ay^aTava = Hagmat&na'] *Jv8(a — Hindui etc., ist nioht
8640:= zd. paresU' (oben p. 44); hindu = pM. hinduk {hindU-
8696:Inder , pi. hinduvdn (Indien A. M. 6, 10) — phi. hindukan
```


## [2026-09-14T03:13:22.532Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/indigo",
 "prompt": "Etymology of indigo; also any note on indium and India/Indus/Sindhu."
}
```


## [2026-09-14T03:13:23.866Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B3%DA%A9",
 "prompt": "Persian ماسک: etymology (from French masque?), meaning."
}
```


### [2026-09-14T03:13:27.876Z] TOOL RESULT

```
# Etymology of Indigo, Indium, and Related Terms

## Indigo
The word entered English in the 1550s as *indico*, ultimately deriving from Latin *indicum* meaning "indigo," which comes from Greek *indikon*—literally "blue dye from India." The term "Indian substance" reflects its geographical origin. By the 1620s, it referred to the color itself, and Newton formally named it as a spectral color in 1704.

## Indium
This metallic element was named in 1864 using the Modern Latin *indicum* (indigo) plus the chemical suffix *-ium*. The naming references "its spectral lines." Ferdinand Reich discovered it in 1863 while analyzing zinc ores.

## India/Indus/Sindhu
The etymology traces back through multiple languages: Old English *India* came from Latin *India*, derived from Greek *India* meaning "region of the Indus River." The ultimate root is Sanskrit *sindhu* meaning "river," which passed through Old Persian *Hindu* (naming the province of Sind) before reaching European languages.

This etymological chain reveals how a color, element, and geographic region all share a common root tied to the ancient Indus River valley.
```


### [2026-09-14T03:13:28.785Z] TOOL RESULT

```
# Persian Word: ماسک (mâsk)

## Etymology
The word "ماسک" is "Possibly from French _masque_ or English _mask_." The term has been borrowed into Persian from these European language sources.

## Meanings

**As a Common Noun:**
The primary definition is "mask." Related synonyms include نقاب (neqâb), روبنده (rubande), and پوشیه (pušiye). An example usage is "ماسک صورت" (mâsk-e surat), meaning face mask.

**As a Proper Noun:**
The word also serves as "a transliteration of the English surname _Musk_," most notably referring to Elon Musk, the entrepreneur and business magnate born in 1971.

## Pronunciation
In formal Dari Persian, it's pronounced [mɑːsk], while in Iranian Persian it's [mɒːskʰʲ], with slight variations in Hazaragi and Kabuli dialects.
```


## [2026-09-14T03:13:34.932Z] TOOL CALL #44: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/شیپور' \\\n 'https://www.etymonline.com/word/mask' \\\n 'https://en.wiktionary.org/wiki/مسخرة' \\\n 'https://en.wiktionary.org/wiki/सिन्धु' \\\n 'https://en.wiktionary.org/wiki/هندوانه' \\\n 'https://www.etymonline.com/word/indigo' \\\n 'https://en.wiktionary.org/wiki/ماسک' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 493 verification (masxarah/mask; Sindhu/Hind; sheypur)' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


## [2026-09-14T03:13:36.277Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/maschera",
 "prompt": "Italian maschera: etymology — Medieval Latin masca, Arabic maskhara, or pre-Roman/Germanic? What does Wiktionary say and which sources does it cite?"
}
```


### [2026-09-14T03:13:38.254Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1cfc5d4c736a668d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/48eb9375bd094719.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88a09edb1aa88cc2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9aff7d46a6d593af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e2620dcf69c601d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d2101c841b326c17.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5cad78806096a33a.txt
```


### [2026-09-14T03:13:43.577Z] TOOL RESULT

```
# Etymology of Italian "Maschera"

Based on the Wiktionary content provided, the etymology traces back through Late Latin rather than Arabic or other origins you mentioned.

According to the source, "maschera" is **inherited from Late Latin** *mascara*, *\*mascra*, and *masca*. The etymology tree shows these Latin forms derive from Proto-West Germanic *maskā*, which borrowed from Latin *masca*, ultimately connected to Proto-Indo-European *\*mesg-* (meaning "knot").

The page cites **Istituto dell'Enciclopedia Italiana** (Treccani) as its reference source for pronunciation and definitions, though it doesn't provide detailed etymological citations explaining why alternative theories (Medieval Latin, Arabic, or pre-Roman origins) were rejected or not included.

The documented path emphasizes Germanic-Latin-Romance language transmission rather than Semitic influences, but the Wiktionary article doesn't explicitly address or refute competing etymological theories.
```


## [2026-09-14T03:13:57.421Z] TOOL CALL #46: WebSearch

```json
{
 "query": "Italian maschera etymology Medieval Latin masca Edictum Rothari 643 striga masca Arabic maskhara rejected"
}
```


### [2026-09-14T03:14:06.093Z] TOOL RESULT

```
Web search results for query: "Italian maschera etymology Medieval Latin masca Edictum Rothari 643 striga masca Arabic maskhara rejected"

Links: [{"title":"masca - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/masca"},{"title":"Masque - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/masque"},{"title":"Mask - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/mask"},{"title":"Word of the Day: mascherina | L’Italo-Americano – Italian American bilingual news source","url":"https://italoamericano.org/word-of-the-day-mascherina/"},{"title":"Adventures in Etymology 19 – Masks – Radio Omniglot","url":"https://www.omniglot.com/radio/?p=1268"},{"title":"maschera - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/maschera"},{"title":"Edictum Rothari","url":"https://en.wikipedia.org/wiki/Edictum_Rothari"},{"title":"Mascherata","url":"https://en.wikipedia.org/wiki/Mascherata"},{"title":"Maschera","url":"https://en.wikipedia.org/wiki/Maschera"},{"title":"Fiorenzo Maschera","url":"https://en.wikipedia.org/wiki/Fiorenzo_Maschera"}]

Based on the search results, here's what I found regarding the etymology of Italian "maschera":

The Medieval Latin term "masca" was first attested in 643 in the Edictum Rothari, section 197, and a masca was a witch.

A variation with an -r- suffix was presumably borrowed into Latin, accounting for Italian "maschera," with the consonant cluster resolved through anaptyxis. The etymology itself is debated, with multiple proposed origins:

1. **Germanic source**: The Medieval Latin "masca" may derive from Proto-West Germanic *maskā (mesh), from Proto-Germanic *maskwǭ (loop, knot, mesh, netting).

2. **Arabic origin**: It may come from Arabic "maskharah" meaning "buffoon, mockery," from "sakhira" meaning "be mocked, ridiculed". However, this derivation is somewhat speculative, as it would require imagining Early Islamic society inclined to comedy even towards the Christian world, apparently contrasting the dark notions behind the Germanic term.

3. **Romance languages**: It may come via Provençal "mascarar," Catalan "mascarar," or Old French "mascurer" meaning "to black (the face)," which may derive from a Germanic source.

The Arabic origin theory appears to be one of several proposed etymologies rather than the accepted one, with the Germanic source being presented as another strong possibility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:14:14.723Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%DB%8C%D9%BE%D9%88%D8%B1/",
 "prompt": "Show the فرهنگ معین and لغت‌نامه دهخدا entries for شیپور, including any origin tag in brackets (e.g. [ سر . ] [ ع . ] [ فر . ]) and the etymological note."
}
```


## [2026-09-14T03:14:16.165Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%A7%D8%B3%DA%A9/",
 "prompt": "Show the فرهنگ معین entry for ماسک, including the origin tag in brackets (e.g. [ فر . ]) and meaning."
}
```


### [2026-09-14T03:14:19.414Z] TOOL RESULT

```
# فرهنگ معین Entry for ماسک

**Origin:** [ فر. ] (French origin)

**Meaning:** "نقاب ، روبند، صورتک" (mask, veil, face covering)

This dictionary entry presents the word as borrowed from French, with three equivalent Persian terms defining it as a facial covering or disguise.
```


### [2026-09-14T03:14:21.043Z] TOOL RESULT

```
# شیپور Entries from Persian Dictionaries

## فرهنگ معین

**(شَ) (اِ.) = شبور:** "از سازهای بادی ، دارای دهانه ای گشاد"

This entry identifies شیپور as a wind instrument with an open mouth/bell, noting its variant form شبور.

## لغت‌نامه دهخدا

The Dehkhoda entry provides extensive etymological information:

**Definition:** A type of horn or bugle (نفیر) described as a smaller version of the karna, also known as the Roman reed pipe. It is a brass instrument with a wide opening historically used in warfare.

**Etymology:** The entry traces multiple origins:
- From Hebrew שופר (shofar)
- From Aramaic and Syriac sources
- Possibly from "Shah Pur" (شاه پور)

**Usage in Classical Persian Poetry:** Multiple citations from Ferdowsi, Nizami, and Asadi demonstrate the instrument's prominence in medieval Persian literature, particularly in descriptions of military and festive contexts.

The lexicographical sources collectively establish شیپور as a brass wind instrument of ancient Middle Eastern origin, naturalized into Persian with both musical and martial applications.
```


## [2026-09-14T03:14:26.881Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in 'https://en.wiktionary.org/wiki/maschera' 'https://en.wiktionary.org/wiki/masca' 'https://abadis.ir/fatofa/شیپور/' 'https://abadis.ir/fatofa/ماسک/' 'https://www.etymonline.com/word/masquerade'; do python3 tools/fetch_source.py \"$u\" --note 'page 493 verification' 2>&1 | tail -1; done",
 "description": "Archive more sources"
}
```


## [2026-09-14T03:14:30.640Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSD mask\"; grep -n 'maskharah\\|maskhara' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt | head -5 | cut -c1-400; echo \"== LKT maskhara\"; grep -n -i 'maskhara\\|masḫara\\|mask̲h̲ara\\|Maske' LKT.txt | head -8 | cut -c1-300",
 "description": "Funk&Wagnalls / Webster / Lokotsch mask"
}
```


### [2026-09-14T03:14:33.370Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/992175ba01842af7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0bc48b16afcc30fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7120e64c8f17dfd4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35d7711b48eb9765.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e3621656adad73a.txt
```


### [2026-09-14T03:14:33.477Z] TOOL RESULT

```
== FSD mask
WEB_vol1.txt:113291:mask, 2. (Fr. masque, a mask, visor, from Ar. mas-éch-is’tic, 4. of or characterized by mas- maskharah, a buffoon.] ochism. 1, a covering for the face masg-dch-is’tic-ally, adv. in a masochistic or part of the face, to con- manner. ceal or disguise the jdentity. miai/son, n. [ME. mason, masoun, OFr. macon, masson; LL. macio, maco, a mason. ]
== LKT maskhara
3304:1436.  Ar.  niashara: 'Verspottung,  Possenreifser' ,  hieraus  it. mäschera,  sp.  pg.  mäscara,  mit  rom. Endung  sp.  mascarada,  frz.  mascarade und  hieraus  durch  Abfall  der  letzten Silben  [die  als  Endung  betrachtet  wur- den] frz.  masque;  dtsch.  Maske,  ndl. masker,  maskera
3517:1-525.  Ar.  iiintawa^g:ih : 'Maskierter'  [eigentlich  'ein  sich  Mas- kierender', pait.  act.  V  von  tvagh  'Ge- sicht' =  'Maske'],  plr.  mutawaggihln; hieraus  sp.  matachin,  kat.  matutxi,  frz. ma tassin,  it.  mattaceino,  pg.  muchachim [allerdings  wegen  des  fehlenden  t  aus ar
5818:Maske  1436
7627:magazijn  1362 mameloek  1384 mango  1393 marokijn  1406 marsepein  1452 masker  (ade)  1436 matras  1446 meerschuim  1416 minaret  1463  a monsoen  1451 nioskee  1435 mousselien  1484 mummie  1510 Witte  1520
9785:Dänisch. Adatnsäble  19 daddel  465 ^/  605 filsben  605 gingang  722 gongon  558 gutta-perka  712 hurra  2167 jonke  753 kasuar  1119 kavring  1282 krahask  1279 kumnien  1046 lazaret  1310 maske  1436 papegöie  147 pisang  1659 rai;  1004 r»-s  1723 rotting  1724 sukker  1855.
```


## [2026-09-14T03:14:41.087Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo -n \"HUB ff=\"; grep -c $'\\f' HUB.txt; echo -n \"leaf7615=\"; awk 'NR<=7615' HUB.txt | tr -cd '\\f' | wc -c; echo -n \" leaf8640=\"; awk 'NR<=8640' HUB.txt | tr -cd '\\f' | wc -c; echo -n \" leaf8696=\"; awk 'NR<=8696' HUB.txt | tr -cd '\\f' | wc -c; echo; sed -n '8638,8642p;8694,8698p' HUB.txt | cut -c1-300",
 "description": "Hübschmann pages"
}
```


### [2026-09-14T03:14:42.136Z] TOOL RESULT

```
HUB ff=291
leaf7615=224
 leaf8640=252
 leaf8696=253

hier nicht massgebend zu sein.
H&bschmann, Persisohe Studien. 16— 242 -
= zd. paresU' (oben p. 44); hindu = pM. hinduk {hindU-
sitan reimt anf jddUsitoln) ; dam, tardzu^ arzu u. s. w.
e) aho peccatum' H. p. 264 {ahost reimt mit dJosi) =
pi. bazuvdn; jadu 'Zauberer, ip\. jaduvan = ipsiz. jadvan
Min. kap. 49, 16 = phi. jatukan Phi. Min. 52, Z. 12; Jmdu
Inder , pi. hinduvdn (Indien A. M. 6, 10) — phi. hindukan
Phi. Ys. 56, 11, 6, arm. hnduk Inder (bei Mos. Kalank.).
e) 5 = phi. ok zu avj uv? Vgl. nEko 'sch5n', pi. nnkuvan
```


## [2026-09-14T03:14:42.812Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY hend\"; grep -n 'هند' incoming/ARY/ARY_pages.txt | head -8 | cut -c1-200; echo \"== RCH sheypur\"; grep -n -i 'shaipúr\\|shaipur\\|shipur\\|sheypur' RCH.txt | head -5 | cut -c1-300",
 "description": "Aryanpur / Richardson"
}
```


### [2026-09-14T03:14:42.886Z] TOOL RESULT

```
== ARY hend
3:هندواروبابی_ 1010 1۵ 1000]
14:هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب
17:۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها
19:شده است ولی ریشه‌ی هند و اروپایی آنها شناخته نیست. ممکن است برخی از آنها هند و اروپایی و
20:بسیاری از آنها غیر هند و اروپایی باشند. بهمین دلیل از آوردن اینگونه واژه‌ها خودداری کرده‌ام.
22:ارستایی -> پارسی‌باستان -> هند و اروپایی. ولی به دلائلی که در دیباچه آمده همیشه تتوانسته‌ام شاهد
26:هند و اروپایی آشکارتر گردد. ۱
27:۴- برای نشان دادن خویشی زبان‌های هند و اروپایی و ریشه گیری آنها از یک سرچشمه‌ی
== RCH sheypur
```


## [2026-09-14T03:14:52.457Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HJB TAMARIND/HINDOO\"; grep -n '^TAMARIND\\|^HINDOO\\|^HINDU\\|^INDIGO,  s' HJB.txt | head; echo \"== BQT hendevaneh\"; grep -n 'هندوانه' incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt BQT_v2_pages.txt 2>/dev/null | head -5 | cut -c1-200",
 "description": "Hobson-Jobson tamarind, BQT hendevaneh"
}
```


### [2026-09-14T03:14:52.537Z] TOOL RESULT

```
== HJB TAMARIND/HINDOO
11071:HINDOO  K008H,
11078:HINDOO, n.]^.  V.Hindu,  Aperson of  Indian  religion  .-and  race.  This  is a  term  derived  from  the  use  of  the Mahommedan  conquerors  (see  under INDIA).  The  word  in  this  form  is Persian ;  Hindi  is  that  used  in  Arabic, e.g.
11085:HINDOO  K008H,  n.p.  Hindu- Kuek;  a  term  applied  by  our  geo- graphers to  the  whole  of  the  Alpine range  which  separates  the  basins  of the  Kabul  River  and  the  Helmand from  that  of  the  Ozus.  It  is,  as Rennell  points  out,  properly  that  part of  the  range  immediately  north  of Kabul,  the  Garuxuue  of  the  historians of  Alexander,  who  crossed  and  re- crossed  it  somewhere  not  far  from  the
21424:TAMARIND.
21439:TAMARIND,  s.    The  pod  of  the
21444:TAMARIND-FISH,
== BQT hendevaneh
incoming/BQT/BQT_v5_pages.txt:8966:بمناسبت ]نس ت که باطلوعوتا بش وی‌میوه‌ها(مانند هندوانه) شررین گردندء و ذ کر
incoming/BQT/BQT_v4_pages.txt:14455:خریزه و هندوانه وخیار و کدو و بادنجان ومانند ورگوشی * بر وزن سرگوشی ,
incoming/BQT/BQT_v4_pages.txt:14978:میآورند ۴ - و تودة خریزه و هندوانه او خیار 5 َ
incoming/BQT/BQT_v4_pages.txt:15430:واحمق راکویند ؟ ۰ مانند بیاره خربزه وهندوانه و با بچوب ودرخت
incoming/BQT/BQT_v4_pages.txt:18854:‎٩‏ هندوانه - بکراولوض‌سوم وفتح ششم ( درلوجهٌ مر کزی بکر شم) * هندوبانه
```


## [2026-09-14T03:14:58.562Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21439,21443p' HJB.txt | cut -c1-1200; echo \"=== leaf\"; awk 'NR<=21439' HJB.txt | tr -cd '\\f' | wc -c; echo \"=== BQT hendevaneh\"; sed -n '18850,18862p' incoming/BQT/BQT_v4_pages.txt | cut -c1-400; echo \"--- page tag\"; awk 'NR<=18854 && /pdf page/ {last=$0} END{print last}' incoming/BQT/BQT_v4_pages.txt",
 "description": "HJB tamarind and BQT hendevaneh"
}
```


### [2026-09-14T03:14:59.694Z] TOOL RESULT

```
TAMARIND,  s.    The  pod  of  the
tree  which  takes  its  name  from  that product,  Tarnarindus  indica,  L.,  N.O. Leguminosae.  It  is  a  tree  cultivate throughout  India  and  Burma  for  the sake  of  the  acid  pulp  of  the  pod,  which is  laxative  and  cooling,  forming  a  most refreshing  drink  in  fever.  The  tree  is not  believed  by  Dr.  Brandis  to  be  in- digenous in  India,  but  is  supposed  to be  so  in  tropical  Africa.  Tlie  origin of  the  name  is  curious.  It  is  Ar. tamar-u'UHind,  'date  of  India,'  or perhaps  rather  in  Persian  form,  tasior- i-Hinai.  It  is  possible  that  the original  name  may  have  been  ^sMir, 'fruit'  of  India,  rather  than  taamar^ 'date.'
1298.— "When  they  have  taken  a  mer- chant vessel,  they  force  the  merdiants  to swallow  a  stuff  called  Tamaiindi,  mixed in  sea-water,  which  prodnces  a  Tioleiit purging." — Marco  Polo,  2nd  ed.,  ii.  383.
c.  1335. — *'  L'arbre  appel€  hammar,  «*est k  dire  al-tamar-al-Hindi,  est  un  arbre sauvage  qui  courre  les  montagnes." — MatOlik-al-abfar,  in  NoL  el  ExL  xiii.  175.
1568.—"  It  is  called  in  Malabar  pii/t,  and in  Guzerat  ambili^  and  this  is  the  name  they have  among  all  the  other  people  of  thu India;  and  the  Arab  calls  it  tamarindi, because  Castor,  as  you  well  know,  is  our tamara^  or,  as  the  (^stilians  say,  datU  \i,t. date],   so  that  tamarindi  are   'dates  o€
=== leaf
937
=== BQT hendevaneh
گر زدست زلف مه مشکینت خطائی رفت رفت ور ز هندوی شما بر ماجفائی رفت رفت .

حافظ شیرازی ص۰۵۷

‎٩‏ هندوانه - بکراولوض‌سوم وفتح ششم ( درلوجهٌ مر کزی بکر شم) * هندوبانه
« فارسنامهٌ این‌البلخی ۱۲۷ » ازهندوان ۳ (پوند نبت) لغة یمنی میوه‌ای که ازهندميآید
« ژابا س۲ 4۵ ۰ قی!510080 (شامی) که درلهجةٌ دزفولی بهندوانه اطلاق کنند «امام» > [ قی :
بطیخ‌الغامی ] وقی, خربزء هندو. بطیخ مندی. در کیلکی5113772 کل (قمت مر کزی) هندوانه
راگوبند . طبری 308082 (هندوانه). درلهجة گزی اسفهان: سندو (ءتسوب بسند) «* واژه‌نامه
۱ . کردی‌ع ۵1000۷۵86 «زابا س۰۸۵۷ ؛ هندوانه 640118 01471108 کیاهی است از
تیرة خیار(0110137011]80669) که بر کهای بریده وساقه های گسترده دارد ومیوه‌های آن درشت
ومواد قندی وی برخلاف خربز ه که درمیان برجمع نمیشود» دردرون برجمع میگردد وتخمه ها
درآن پراکنده اند. «گل کلاب م۹۲۵4 .
--- page tag
[pdf page 463]
```


## [2026-09-14T03:15:15.897Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=tamarind",
 "prompt": "Give the American Heritage Dictionary etymology for tamarind (Arabic tamr hindi?), and if shown, for Hindu."
}
```


## [2026-09-14T03:15:18.115Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'indium,  n' KLN_1966.txt | head -3 | cut -c1-500; echo \"== sendal/sindon\"; grep -n 'Indie,  adj' KLN_1966.txt | head -2 | cut -c1-300",
 "description": "Klein indium"
}
```


### [2026-09-14T03:15:18.189Z] TOOL RESULT

```
== sendal/sindon
19163:Indie,  adj.,  of,  or  pertaining  to,  India.  —  L.  In- dicus,  fr.  Gk.  ’IvSococ,  fr.  ’IvSia.  See  prec.  word and  -ic  and  cp.  indigo.
```


### [2026-09-14T03:15:19.883Z] TOOL RESULT

```
# Tamarind Etymology

According to the American Heritage Dictionary, tamarind comes from Arabic **tamr hindī**, meaning "Indian dates." The etymology traces through Middle English *tamarinde*, Medieval Latin *tamarindus*, and Old French *tamarinde* back to the Arabic roots: *tamr* (dates) and *hindī* (of India, from Persian *Hind*).

The dictionary notes that "medieval Arabian merchants imported it from India," which explains the name's origin.

**Regarding Hindi:** The dictionary entry does not provide a separate etymology for the word "Hindi" itself. It only references Hindi in passing within the tamarind etymology, indicating the Arabic *hindī* derives from Persian *Hind* (India).
```


## [2026-09-14T03:15:57.795Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"; n=0} {n++; if (n>=390 && n<=410) {print \"--- leaf \"n\": \"substr($0,1,100)}}' KLN_1966.txt",
 "description": "Klein leaves 390-410"
}
```


### [2026-09-14T03:15:58.853Z] TOOL RESULT

```
--- leaf 390:  herbarium;  2)  a  garden  of  herbs or  vegetables.  —  Late  L.  herbarium.  See  prec. word  a
--- leaf 391: ers);  see  german,  ‘having  the  same  parents’. Sp.  suff.  -dad  derives  fr.  L.  -tat-  (n
--- leaf 392: o  first  analyzed  it.  For  the  ending see  subst.  suff.  -ite.
hest,  n.,  bidding,  behest.  �
--- leaf 393: d’,  compounded  of  e^a-  (see hexa-)  and  77064,  gen.  710864,  ‘foot’.  See  -pod. Hexapo
--- leaf 394: cy.  —  See  prec.  word and  -ic,  resp.  also  -al.
hierodule,  n.,  a  temple  slave  in  ancie
--- leaf 395: r.  Hind,  ‘India’,  fr.  OI.  Sindhuh, ‘the  river  Indus;  the  region  of  the  river  Indu
--- leaf 396: , ‘Spain’,  lit.  ‘the  country  of  the  Spaniards’,  fr. Hispanus,  ‘Spaniard’,  which
--- leaf 397: hough,  hoch,  fr.  OE.  hoh,  ‘heel’,  rel.  to  the first  element  in  ON.  ha-sin,  OE.  hoh
--- leaf 398:   holen,  ‘holly’.  See holly.
holo-,  before  a  vowel  hoi-,  combining  form  mean¬ ing  ‘
--- leaf 399: .  of  opIXsiv,  ‘to  be  together with,  converse  with’,  fr.  6puX6p,  ‘crowd,  assem¬ bly
--- leaf 400: ed  from  it). See  honey  and  suck.
hong,  n.,  warehouse,  factory.  —  Chin,  hang, ‘warehou
--- leaf 401:   —  L.  Horatius  (see  Horace); influenced  in  form  by  It.  Orazio,  which  is  of the  same 
--- leaf 402: r,  gen.  horiri, ‘to  urge,  incite,  encourage,  exhort’,  fr.  I.-E.  base *gher-,  ‘to  de
--- leaf 403: .  Cp.  the  second element  in  dachshund,  keeshond.Cp.  also  canaille, Canidae,  canine,  Canis,
--- leaf 404: uge-ous-ness,  n,,  hug-y,  adj. huggermugger,  adv.,  secretly.  —  Fr.  earlier  hucker mucker-,
--- leaf 405: b-,  ’to bend,  curve',  whence  also  OI.  kumbhdh,  ‘pot, jar',  Gk.  x'i;i3r.  ‘the  hollow
--- leaf 406:   Formed  fr.  husk  with  adj.  suff.  -y. Derivatives:  husk-i-ly,  adv.,  husk-i-ness,  n. Husky,
--- leaf 407: drogen  (chem.)\  4)  short  for  hydroid  (zool.)
—  Gk.  uSpo-,  ’)8p-,  fr.  uStop,  ‘water
--- leaf 408:  (fr.  L.  -dsns).
hydroxide,  n.,  a  compound  containing  bydroxyl (chem.)  —  Compounded  of  
--- leaf 409: out  hymns.  See  prec.  word  and
-graphv.
hymnology,  n.,  1)  the  study  of  hymns;  2)  the  co
--- leaf 410: ed  by  James  Braid  of Manchester  (1795-1861)  fr.  hypnotic  and  suff. -ism.  Cp.  hypnosis.
hy
```


## [2026-09-14T03:16:36.900Z] TOOL CALL #58: Bash

```json
{
 "command": "pdftoppm -f 493 -l 493 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$TMPDIR/pg493-v\" 2>/dev/null; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/*/scratchpad 2>/dev/null | head; pdftoppm -f 493 -l 493 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493 && echo OK",
 "description": "Render pdf page 493"
}
```


### [2026-09-14T03:16:38.490Z] TOOL RESULT

```
/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad:
total 38344
drwx------ 3 sfmqrb sfmqrb   20480 Sep 13 23:16 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   92443 Sep 13 21:13 391-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  129993 Sep 13 21:11 394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21316 Sep 13 21:11 394-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44712 Sep 13 21:14 400-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116049 Sep 13 21:14 400-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99858 Sep 13 21:16 404-top.png
OK
```


## [2026-09-14T03:16:39.952Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493.png"
}
```


### [2026-09-14T03:16:39.974Z] TOOL RESULT

```

```


## [2026-09-14T03:16:54.239Z] TOOL CALL #60: Bash

```json
{
 "command": "pdftoppm -f 493 -l 493 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493hi.png')\nprint(im.size)\nw,h=im.size\nim.crop((int(w*0.55),int(h*0.60),int(w*0.82),int(h*0.65))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop.png')\n\"",
 "description": "Crop sheypur box"
}
```


### [2026-09-14T03:16:57.189Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-14T03:16:58.804Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop.png"
}
```


### [2026-09-14T03:16:58.822Z] TOOL RESULT

```

```


## [2026-09-14T03:17:03.945Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493hi.png')\nw,h=im.size\nc=im.crop((int(w*0.60),int(h*0.606),int(w*0.76),int(h*0.622))).resize((int(w*0.16*3),int(h*0.016*3)),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop2.png')\nprint(c.size)\"",
 "description": "Tighter crop"
}
```


### [2026-09-14T03:17:05.345Z] TOOL RESULT

```
(1632, 211)
```


## [2026-09-14T03:17:07.112Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop2.png"
}
```


### [2026-09-14T03:17:07.131Z] TOOL RESULT

```

```


## [2026-09-14T03:17:14.511Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493hi.png')\nw,h=im.size\nbox=(int(w*0.62),int(h*0.5975),int(w*0.78),int(h*0.6115))\nc=im.crop(box); c=c.resize((c.width*3,c.height*3),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop3.png'); print(c.size)\"",
 "description": "Crop again"
}
```


### [2026-09-14T03:17:16.017Z] TOOL RESULT

```
(1632, 183)
```


## [2026-09-14T03:17:17.634Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop3.png"
}
```


### [2026-09-14T03:17:17.662Z] TOOL RESULT

```

```


## [2026-09-14T03:17:24.557Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493hi.png')\nw,h=im.size\nc=im.crop((int(w*0.685),int(h*0.5985),int(w*0.735),int(h*0.6105)))\nc=c.resize((c.width*8,c.height*8),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop4.png'); print(c.size)\"",
 "description": "Zoom parenthetical word"
}
```


### [2026-09-14T03:17:26.074Z] TOOL RESULT

```
(1360, 424)
```


## [2026-09-14T03:17:27.897Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop4.png"
}
```


### [2026-09-14T03:17:27.934Z] TOOL RESULT

```

```


## [2026-09-14T03:17:37.051Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493hi.png')\nw,h=im.size\nc=im.crop((int(w*0.740),int(h*0.5985),int(w*0.790),int(h*0.6105)))\nc=c.resize((c.width*8,c.height*8),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop5.png'); print(c.size)\"",
 "description": "Zoom main word"
}
```


### [2026-09-14T03:17:38.391Z] TOOL RESULT

```
(1360, 424)
```


## [2026-09-14T03:17:40.448Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop5.png"
}
```


### [2026-09-14T03:17:40.474Z] TOOL RESULT

```

```


## [2026-09-14T03:17:45.714Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493hi.png')\nw,h=im.size\nc=im.crop((int(w*0.685),int(h*0.598),int(w*0.792),int(h*0.6135)))\nc=c.resize((c.width*6,c.height*6),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop6.png'); print(c.size)\"",
 "description": "Both words tall crop"
}
```


### [2026-09-14T03:17:47.177Z] TOOL RESULT

```
(2178, 408)
```


## [2026-09-14T03:17:48.920Z] TOOL CALL #71: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493-crop6.png"
}
```


### [2026-09-14T03:17:49.056Z] TOOL RESULT

```

```


## [2026-09-14T03:17:49.051Z] INPUT

[Image: original 2178x408, displayed at 2000x375. Multiply coordinates by 1.09 to map to original image.]


## [2026-09-14T03:18:09.657Z] TOOL CALL #72: Bash

```json
{
 "command": "sed -n 60,140p tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-14T03:18:09.710Z] TOOL RESULT

```
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


## [2026-09-14T03:18:13.015Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg493.png data/verification/sources/refs/ocr/BOOK/493.png && ls -la data/verification/sources/refs/ocr/BOOK/493.png; python3 tools/fetch_source.py 'https://ahdictionary.com/word/search.html?q=tamarind' --note 'page 493, tamarind AHD etymology' 2>&1 | tail -1",
 "description": "Copy page image, archive AHD"
}
```


### [2026-09-14T03:18:14.323Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 44753 Sep 13 23:18 data/verification/sources/refs/ocr/BOOK/493.png
/home/sfmqrb/git/rishe/data/verification/sources/web/53cbb3ca31c098d4.txt
```


## [2026-09-14T03:18:38.850Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B3%D8%AE%D8%B1%D9%87/",
 "prompt": "Show the فرهنگ معین entry for مسخره with its origin tag in brackets (e.g. [ ع . ]) and the meanings given."
}
```


## [2026-09-14T03:18:41.706Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'maskharah\\|maskhara' RCH.txt | head -5 | cut -c1-400; echo \"== ARY hendevaneh\"; grep -n 'هندوانه' incoming/ARY/ARY_pages.txt | head -3 | cut -c1-200; echo \"== SIN hendevaneh/watermelon\"; grep -n -i 'water-melon\\|watermelon' SIN.txt | head -5 | cut -c1-250",
 "description": "Richardson maskharah; ARY; Sino-Iranica watermelon"
}
```


### [2026-09-14T03:18:41.805Z] TOOL RESULT

```
84476:A   maskharafy  A   bufibon,  a   fool,  a   jester,  a   droll,  a   wag ;
84477:a   facetious  man.  A   man  in  masquerade.  A   pleasantry,  any thing  ridiculous  or  mirthful,  sport,  v   iSjkr^  maskharah kardauj  To  ridicule  or  deride  ;   to  play  the  buiToon,  to  laugh  at others ;   also  to  be  laughed  at.
== ARY hendevaneh
== SIN hendevaneh/watermelon
100:The  Water-Melon   438
1980:8  The  case  would  then  be  analogous  to  the  history  of  the  water-melon.
2517:THE  WATER-MELON
2519:A.  Engler2  traces  the  home  of  the  water-melon  to  South  Africa, whence  he  holds  it  spread  to  Egypt  and  the  Orient  in  most  ancient  times, and  was  diffused  over  southern  Europe  and  Asia  in  the  pre-Christian era.  Th
2520:The  water-melon  is  not  mentioned  by  any  work  of  the  T'ang  dy- nasty; notably  it  is  absent  from  the  T'ai  pHn  hwan  yii  ki.  The  earliest allusion  to  it  is  found  in  the  diary  of  Hu  Kiao  jijE  HI,  entitled  Hien  lu
```


### [2026-09-14T03:18:43.173Z] TOOL RESULT

```
# فرهنگ معین Entry for مسخره

According to the Farhang-e Moein dictionary section provided:

**(مَ خَ رِ ) [ ع . مسخرة ]**

The entry indicates the word has an Arabic origin (marked as ع . for عربی), derived from the Arabic form مسخرة.

**Meanings listed:**
- ریشخند (mockery/ridicule)
- شوخی (joking/jest)

This represents the formal dictionary entry, noting that despite common perception of the term as purely Arabic, etymological research presented elsewhere on the page suggests the word has deeper roots in Middle Persian (Pahlavi) and Avestan languages.
```


## [2026-09-14T03:18:49.729Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2517,2545p' SIN.txt | grep -n -i 'hindi\\|hindu\\|persian' | head -10 | cut -c1-400",
 "description": "Sino-Iranica watermelon Persian"
}
```


### [2026-09-14T03:18:49.792Z] TOOL RESULT

```
21:with  a  juice  which  is  very  cold.  Hun  Hao,  when  he  went  out  as  envoy, brought  the  fruit  back  to  China.  At  present  it  is  found  both  in  the imperial  orchards  and  in  village  gardens.  It  can  be  kept  for  several months,  aside  from  the  fact  that  there  is  nothing  to  prevent  it  from assuming  a  yellow  hue  in  course  of  time.  In  P'o-yah  3K  fi§1
```


## [2026-09-14T03:19:11.491Z] AGENT

Now writing the verification file.


## [2026-09-14T03:26:02.093Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-493.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n  \"pdf_page\": 493,\n  \"book_page\": 463,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n\n  # ================= entry 0 =================\n  {\n    \"entry\": 0,\n    \"root\": \"S.x.r\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"Arabic root س-خ-ر (s-x-r), verb سَخِرَ saxira (min) 'to mock, deride'; maf‘ala-noun مَسْخَرَة masxara(t) 'laughing-stock, buffoonery'\",\n    \"note\": \"The root box is right: the Arabic triliteral س خ ر does mean 'to ridicule' in its Form I سَخِرَ saxira (min-) 'he scoffed at', and the noun of that base is مَسْخَرَة. (The homograph سَخَّرَ saxxara 'to press into service, subjugate' — Qur'an 13:2, 14:32 — is a second, non-mocking branch of the same consonantal root; Nourai's gloss picks the branch he needs and that is legitimate.) The weak joint on this page is not the Arabic root but the Arabic→Italian arrow (node #3): Klein, Skeat, Lokotsch, Devic (after Engelmann-Dozy) and Webster all derive It. maschera from masxarah, but since Meyer-Lübke and the DELI the standard Romance view starts from Late/Medieval Latin masca 'witch, spectre', attested in the Lombard Edictus Rothari §197 of 643 CE, i.e. two centuries before any Arab presence in Italy. Everything downstream of Italian (French masque, English mask/masque, Persian ماسک) is unaffected and solid.\",\n    \"note_fa\": \"ریشهٔ عربی «س‌خ‌ر» و معنای «ریشخند کردن» درست است: فعل «سَخِرَ (مِن)» یعنی «مسخره کرد، ریشخند زد» و اسم آن بر وزن مَفْعَلَة «مَسْخَرَة» است. (فعل دیگرِ همین ریشه، «سَخَّرَ» به معنی «رام کرد، به بیگاری گرفت»، شاخهٔ معنایی جداگانه‌ای است و در قرآن بارها آمده.) نقطهٔ سست این نمودار ریشهٔ عربی نیست، بلکه پیکانِ عربی ← ایتالیایی است: کلاین، اسکیت، لوکوچ و دِویک (به پیروی از دوزی) «maschera» ایتالیایی را از «مسخرة» می‌گیرند، اما ریشه‌شناسی امروزی زبان‌های رومی آن را از لاتینی متأخر masca «جادوگر، شبح» می‌داند که در «ادیکتوس روتاری» لومباردی به سال ۶۴۳ میلادی ــ دو قرن پیش از حضور عرب در ایتالیا ــ ثبت شده است. حلقه‌های پس از ایتالیایی (فرانسوی masque، انگلیسی mask، فارسی ماسک) به هر حال استوارند.\",\n    \"sources\": [\n      W + \"%D9%85%D8%B3%D8%AE%D8%B1%D8%A9\",\n      \"https://www.etymonline.com/word/mask\",\n      W + \"masca\"\n    ],\n    \"ref_check\": [\n      {\"ref\": \"SAP:683\", \"status\": \"not_checked\",\n       \"note\": \"SAP = Ahmad Sayyah, Farhang-e Sayyah (Persian rendering of al-Munjid); refs_online.json marks it kind='purchase' (fidibo only, no scan, no archive.org copy), so p.683 could not be opened. The Arabic-side claim is however independently secured by Klein, Skeat and Richardson (see consulted).\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 508 (printed ≈ p.990), s.v. mask\", \"stance\": \"supports\",\n       \"note\": \"'mask, n. — MF. (= F.) masque, fr. ML. masca, fr. It. maschera, fr. Arab. maskharah, \\\"mockery; buffoon\\\", fr. sākhira, \\\"he mocked, ridiculed\\\".' (grep -n 'maskharah' KLN_1966.txt → line 23047)\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 297, s.v. Mask, Masque (printed ≈ p.297 of the I-M sequence)\", \"stance\": \"supports\",\n       \"note\": \"'— Arab. maskharat, a buffoon, jester, man in masquerade, a pleasantry, anything ridiculous. — Arab. root sakhira, he ridiculed. ¶ Fully proved; other etymologies are worthless.'\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt no. 1436 (line 3304)\", \"stance\": \"supports\",\n       \"note\": \"'Ar. mashara: \\\"Verspottung, Possenreifser\\\", hieraus it. maschera, sp. pg. mascara, mit rom. Endung sp. mascarada, frz. mascarade und hieraus durch Abfall der letzten Silben frz. masque; dtsch. Maske…'\"},\n      {\"src\": \"DEV\", \"where\": \"DEV.txt line 1690, s.v. Mascarade\", \"stance\": \"supports\",\n       \"note\": \"'Il a été surabondamment démontré … par MM. Malin et Dozy, que mascara et maschera ne sont rien autre que l'arabe maskhara signifiant bouffon, farceur, histrion; plaisanterie, drôlerie, moquerie.'\"}\n    ],\n    \"nodes\": [\n      {\n        \"id\": 1, \"lang\": \"Arabic\", \"words\": \"masxarah\", \"verdict\": \"confirmed\",\n        \"derivation\": \"مَسْخَرَة masxara(t) is the regular maf‘ala-noun built on the Form I verb سَخِرَ saxira 'to deride' (pattern maf‘ala of abundance/instance, cf. مَهْلَكَة mahlaka from هَلَكَ). Classical Arabic lexica (Lisān al-‘Arab s.v. سخر) gloss it both abstractly, 'mockery, buffoonery', and concretely, 'a laughing-stock, one who is mocked, a buffoon'; plural مَساخِر masāxir 'antics, farces'. Nourai's spelling masxarah renders the pausal tā’ marbūṭa, exactly as Klein's maskharah and Skeat's maskharat. The step root→noun is purely morphological and is not in doubt.\",\n        \"derivation_fa\": \"«مَسْخَرَة» اسمِ ساخته‌شده بر وزن مَفْعَلَة از فعل «سَخِرَ» است (مانند «مَهْلَکَة» از «هَلَکَ») و در فرهنگ‌های کهن عربی هم به معنی «ریشخند، دلقک‌بازی» و هم به معنای شخص «مضحکه، دلقک» آمده است؛ جمع آن «مَساخِر». این پله صرفاً صرفی است و هیچ تردیدی در آن نیست. ادعای نورایی درست است.\",\n        \"sources\": [W + \"%D9%85%D8%B3%D8%AE%D8%B1%D8%A9\"],\n        \"ref_check\": [\n          {\"ref\": \"SAP:683\", \"status\": \"not_checked\",\n           \"note\": \"Sayyah/al-Munjid p.683 unavailable (purchase-only per refs_online.json); the Arabic entry itself is confirmed from Wiktionary (root س خ ر), Klein and Richardson.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 23047, s.v. mask\", \"stance\": \"supports\",\n           \"note\": \"'fr. Arab. maskharah, \\\"mockery; buffoon\\\", fr. sākhira, \\\"he mocked, ridiculed\\\"'\"},\n          {\"src\": \"RCH\", \"where\": \"RCH.txt lines 84476-84477, s.v. maskharah\", \"stance\": \"supports\",\n           \"note\": \"'A maskharah: A buffoon, a fool, a jester, a droll, a wag; a facetious man. A man in masquerade. A pleasantry, anything ridiculous or mirthful, sport.'\"},\n          {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 297, s.v. Mask\", \"stance\": \"supports\",\n           \"note\": \"'Arab. maskharat, a buffoon, jester … — Arab. root sakhira, he ridiculed.'\"}\n        ]\n      },\n      {\n        \"id\": 2, \"lang\": \"Persian\", \"words\": \"masxareh «مسخره»\", \"verdict\": \"confirmed\",\n        \"derivation\": \"A straight Arabic loan taken into New Persian in the early Islamic centuries: Arab. masxara(t) → NP masxare, the tā’ marbūṭa written with final ه and pronounced -a/-e as in every Arabic فَعْلَة/مَفْعَلَة loan (جمعه jom‘e, مدرسه madrase). Persian narrowed the abstract noun to a person — 'clown, buffoon' — and used it adjectivally 'ridiculous', with the compound verb مسخره کردن 'to ridicule' (already in Richardson 1829). Persian in turn was the transmitter onward: Ottoman Turkish مسخره → Turkish maskara, Urdu/Hindi masxarā, Punjabi, Uzbek, Uyghur, Bengali moskorā, Armenian մասխարա, Georgian მასხარა (Wiktionary, Descendants s.v. مسخرة, explicitly routed 'via Persian').\",\n        \"derivation_fa\": \"«مسخره» وام‌واژه‌ای عربی است که در سده‌های نخست اسلامی به فارسی نو راه یافت؛ تاء مربوطهٔ عربی مانند همهٔ وام‌واژه‌های هم‌وزن (جمعه، مدرسه) به «ـه» بدل شد. معنا از «ریشخند» به «شخصِ مضحک، دلقک» و صفت «خنده‌آور» گسترش یافت و ترکیب «مسخره کردن» ساخته شد (ریچاردسون ۱۸۲۹ آن را ثبت کرده). فارسی خود واسطهٔ انتقال این واژه به ترکی عثمانی (maskara)، اردو، ازبکی، بنگالی، ارمنی و گرجی شده است. معین آن را با نشانِ [ع. مسخرة] می‌آورد؛ ادعای نورایی درست است.\",\n        \"sources\": [W + \"%D9%85%D8%B3%D8%AE%D8%B1%D8%A9\", \"https://abadis.ir/fatofa/%D9%85%D8%B3%D8%AE%D8%B1%D9%87/\"],\n        \"ref_check\": [\n          {\"ref\": \"MON:4109\", \"status\": \"supports\",\n           \"note\": \"Mo'in's entry read through abadis.ir (page numbers are not mapped online): 'مسخره (مَ خَ رِ) [ع. مسخرة] ریشخند، شوخی' — the bracketed [ع.] tag is exactly Nourai's claim of an Arabic source. The page number 4109 is consistent with Mo'in's continuous lexicon pagination (م-words in vol. 3; cf. MON:3699 for ماسک on the same page).\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. مسخره\", \"stance\": \"supports\",\n           \"note\": \"'[ ع . مسخرة ] ریشخند، شوخی' — Arabic origin tag.\"},\n          {\"src\": \"RCH\", \"where\": \"RCH.txt line 84477\", \"stance\": \"supports\",\n           \"note\": \"'maskharah kardan: To ridicule or deride; to play the buffoon' — the Persian compound verb already in Richardson's Persian-Arabic-English dictionary.\"},\n          {\"src\": \"BQT\", \"where\": \"grep 'مسخره' over BQT_v1/v2/v3/v4_pages.txt\", \"stance\": \"silent\",\n           \"note\": \"Borhan-e Qate' has no headword مسخره (it is a transparent Arabic loan, outside Borhan's Persian-word remit).\"}\n        ]\n      },\n      {\n        \"id\": 3, \"lang\": \"Italian\", \"words\": \"maschera\", \"verdict\": \"disputed\",\n        \"derivation\": \"Two problems. (a) The gloss: It. maschera does not mean 'mockery'; from its first attestations it means 'mask, visor' (and 'masked figure'), the abstract being mascherata. (b) The arrow: the derivation It. maschera < Arab. masxarah is the 19th-century view of Engelmann-Dozy, taken over by Skeat ('fully proved; other etymologies are worthless'), Klein, Lokotsch (no. 1436) and Webster. Modern Romance etymology rejects it on chronology and phonology: the base word is Medieval Latin masca 'witch, spectre', first attested in the Lombard Edictus Rothari §197 (643 CE, 'striga quod est masca'), a century before Islam reached Sicily and two before any Arabic lexical influence in northern Italy; It. maschera reflects a suffixed *mascara/*mascra with anaptyxis. The source of masca itself is contested — Proto-West Germanic *maskā 'mesh, net' (> PIE *mesg- 'knot'), or a pre-Roman Mediterranean substrate word also behind Occitan masco 'witch' and Old French mascurer 'to blacken the face'. Etymonline records the Arabic explanation only as one of several 'perhaps' options; Wiktionary's It. maschera derives it from Late Latin masca with no Arabic step at all. The Arabic etymology is therefore not refuted outright (the semantic fit with Italian carnival buffoonery is good and Arabic masxarah did reach Spanish), but it is no longer the accepted account.\",\n        \"derivation_fa\": \"دو اشکال دارد. نخست معنا: «maschera» در ایتالیایی از نخستین کاربردها «نقاب، صورتک» است، نه «ریشخند» (معنای انتزاعی را با mascherata می‌رسانند). دوم خودِ پیکان: گرفتن maschera از «مسخرة» عربی رأی دوزی و انگلمان در سدهٔ نوزدهم است که اسکیت، کلاین و لوکوچ آن را پذیرفتند، ولی ریشه‌شناسی امروزی زبان‌های رومی آن را رد می‌کند؛ زیرا صورت پایه، masca لاتینیِ سده‌های میانه به معنی «جادوگر، شبح» است که در قانون‌نامهٔ روتاریِ لومباردی (بند ۱۹۷، سال ۶۴۳ م.) پیش از هرگونه تماس زبانی با عربی در ایتالیا ثبت شده است. خاستگاه خودِ masca مورد اختلاف است: یا ژرمنی غربی آغازین *maskā «تور، چشمهٔ تور»، یا واژه‌ای از زیرلایهٔ پیش‌رومی که در masco «جادوگر» اکسیتانی هم دیده می‌شود. بنابراین: پژوهش امروزی ادعای نورایی را در این حلقه نمی‌پذیرد، هرچند آن را یکسره ناممکن هم نمی‌شمارد.\",\n        \"sources\": [\n          \"https://www.etymonline.com/word/mask\",\n          W + \"maschera\",\n          W + \"masca\"\n        ],\n        \"ref_check\": [\n          {\"ref\": \"KLN:944\", \"status\": \"supports\",\n           \"note\": \"Klein does say what Nourai's arrow says: s.v. mask (KLN_1966.txt line 23047, leaf 508) 'MF. masque, fr. ML. masca, fr. It. maschera, fr. Arab. maskharah'. Note (i) Klein interposes ML. masca between French and Italian, which Nourai omits, and (ii) the printed page could not be pinned: the local OCR has no page markers and leaf 508 works out to printed p. ≈990 rather than 944 — the page reference, not the content, is what I could not confirm.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 297, s.v. Mask, Masque\", \"stance\": \"supports\",\n           \"note\": \"'— Span. mascara … — Arab. maskharat … ¶ Fully proved; other etymologies are worthless.' Skeat even routes it through Spanish rather than Italian.\"},\n          {\"src\": \"LKT\", \"where\": \"LKT.txt no. 1436\", \"stance\": \"partial\",\n           \"note\": \"Supports the Arabic source but a different internal route: 'hieraus it. maschera, sp. pg. mascara, … frz. mascarade und hieraus durch Abfall der letzten Silben frz. masque' — Lokotsch gets Fr. masque from mascarade, not from It. maschera.\"},\n          {\"src\": \"DEV\", \"where\": \"DEV.txt line 1690, s.v. Mascarade\", \"stance\": \"supports\",\n           \"note\": \"Engelmann-Dozy's demonstration, 'contrairement à l'opinion de Diez'; Devic already registers that Diez (the founder of Romance etymology) dissented — the dissent is what modern handbooks have followed.\"},\n          {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 113291, s.v. mask\", \"stance\": \"supports\",\n           \"note\": \"'mask … [Fr. masque, a mask, visor, from Ar. maskharah, a buffoon.]'\"}\n        ]\n      },\n      {\n        \"id\": 4, \"lang\": \"French\", \"words\": \"masque\", \"verdict\": \"confirmed\",\n        \"derivation\": \"Middle French masque 'covering for the face' is first recorded in 1514 and is agreed on all sides to be a borrowing of Italian maschera (with loss of the unstressed post-tonic syllable: maschera → masque), taken over during the Italianising fashion of the early 16th century, when the Venetian and Florentine carnival mascherata reached the French court. Etymonline: 'from French masque … from Italian maschera'; Klein: 'MF. (= F.) masque, fr. ML. masca, fr. It. maschera'. This link is independent of the dispute over the ultimate origin of maschera (node #3). Lokotsch alone prefers masque < mascarade by apocope, a minority view.\",\n        \"derivation_fa\": \"«masque» فرانسوی نخستین‌بار در ۱۵۱۴ م. ثبت شده و همهٔ منابع آن را وام‌گیری از «maschera» ایتالیایی می‌دانند (با افتادن هجای بی‌تکیهٔ پایانی: maschera > masque)، در دورهٔ رواج مد ایتالیایی در دربار فرانسه که کارناوال و «mascherata» ونیزی و فلورانسی به فرانسه رسید. این حلقه، مستقل از اختلاف بر سر خاستگاه نهایی maschera، پذیرفته است؛ تنها لوکوچ masque را از mascarade می‌گیرد که رأی اقلیت است. ادعای نورایی درست است.\",\n        \"sources\": [\"https://www.etymonline.com/word/mask\", W + \"maschera\"],\n        \"ref_check\": [\n          {\"ref\": \"KLN:944\", \"status\": \"supports\",\n           \"note\": \"KLN_1966.txt line 23047 s.v. mask: 'MF. (= F) masque, fr. ML. masca, fr. It. maschera' — the French←Italian arrow is Klein's own. (Page number unverifiable in the local scan; see node #3.)\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 297 s.v. Mask\", \"stance\": \"partial\",\n           \"note\": \"'— F. masque, a mask, visor; a clipped form, due to F. vb. masquer … — Span. mascara' — Skeat has French from Spanish, not Italian.\"},\n          {\"src\": \"PHN\", \"where\": \"PHN.txt line 7186ff., s.v. MASCARADE (index p. 956)\", \"stance\": \"supports\",\n           \"note\": \"Pihan's article treats fr. masque/mascarade/mascaron as one family of oriental origin passing through It./Sp. mascara.\"},\n          {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 113291\", \"stance\": \"supports\",\n           \"note\": \"'[Fr. masque, a mask, visor …]' — English from French.\"}\n        ]\n      },\n      {\n        \"id\": 5, \"lang\": \"Persian\", \"words\": \"mâsk «ماسک»\", \"verdict\": \"confirmed\",\n        \"derivation\": \"ماسک mâsk is a modern European loan, taken into Persian in the 20th century together with the medical and theatrical vocabulary that came in through French; the spelling with ک and the vowel â reproduce French masque [mask] (not English mask, which would more naturally give مَسک). Mo'in tags it [فر.] = فرانسوی 'French' and glosses it نقاب، روبند، صورتک; Wiktionary gives 'possibly from French masque or English mask'. It coexists with the older native/Arabic synonyms نقاب neqâb and روبنده rubande, and is now the ordinary word for a surgical or face mask (ماسک صورت).\",\n        \"derivation_fa\": \"«ماسک» وام‌واژه‌ای اروپایی و نو است که در سدهٔ چهاردهم خورشیدی همراه با واژگان پزشکی و نمایشی از راه فرانسه به فارسی آمد؛ آوای «آ» و املای «ماسک» صورت فرانسویِ masque را بازمی‌تاباند نه انگلیسیِ mask را. معین آن را با نشانِ [فر.] (فرانسوی) و معنای «نقاب، روبند، صورتک» آورده است. این واژه در کنار «نقاب» و «روبنده» به کار می‌رود و امروز واژهٔ رایج برای «ماسک صورت» است. ادعای نورایی درست است.\",\n        \"sources\": [W + \"%D9%85%D8%A7%D8%B3%DA%A9\", \"https://abadis.ir/fatofa/%D9%85%D8%A7%D8%B3%DA%A9/\"],\n        \"ref_check\": [\n          {\"ref\": \"MON:3699\", \"status\": \"supports\",\n           \"note\": \"Mo'in s.v. ماسک, read through abadis.ir: '[ فر . ] نقاب، روبند، صورتک' — the [فر.] tag is precisely Nourai's French→Persian arrow. (Print page numbers are not exposed online; 3699 is consistent with the position of ما- in Mo'in's continuous pagination, below مسخره at 4109.)\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. ماسک\", \"stance\": \"supports\",\n           \"note\": \"'[ فر . ] نقاب ، روبند، صورتک'\"},\n          {\"src\": \"BQT\", \"where\": \"grep 'ماسک' over BQT_v1-v5 pages files\", \"stance\": \"silent\",\n           \"note\": \"Borhan-e Qate' (1062/1651) is three centuries older than the loan; no entry, as expected.\"},\n          {\"src\": \"ARY\", \"where\": \"grep 'ماسک' over ARY_pages.txt\", \"stance\": \"silent\",\n           \"note\": \"Aryanpur's dictionary covers only words of Indo-European inheritance in Persian; a modern French loan is outside its scope.\"}\n        ]\n      },\n      {\n        \"id\": 6, \"lang\": \"English\", \"words\": \"mask; masque; masquerade; mascara\", \"verdict\": \"plausible\",\n        \"derivation\": \"mask (1530s) and masque are one word: ME had nothing, the noun came in from Middle French masque, the spelling masque being kept for the Elizabethan/Jacobean court entertainment (Ben Jonson's masques) and mask for the face-covering; Klein: 'masque, n. … — F. masque. See mask.' So far Nourai's arrow from French masque is exact. The other two words do not come from French masque itself: masquerade (1590s) is French mascarade borrowed from Spanish mascarada 'a ball at which masks are worn' (Klein, s.v. masquerade), and mascara (the cosmetic, 19th c.) is Spanish máscara 'a mask' (Klein: 'Sp. mascara, \\\"a mask\\\", fr. Arab. maskharah'), i.e. it re-enters English from the Iberian branch of the family, not through France. The node is therefore right for mask/masque and loose for masquerade/mascara, which need a Spanish box that the chart does not draw.\",\n        \"derivation_fa\": \"«mask» و «masque» یک واژه‌اند: در دههٔ ۱۵۳۰ از فرانسوی میانه masque وارد انگلیسی شد و املای masque برای نمایش‌های درباری (masqueهای بن جانسون) و mask برای «نقاب» تخصیص یافت؛ تا اینجا پیکان نورایی دقیق است. اما دو واژهٔ دیگر مستقیماً از masque فرانسوی نیامده‌اند: «masquerade» (۱۵۹۰م) از mascarade فرانسوی است که خود از mascarada اسپانیایی گرفته شده، و «mascara» (آرایشی، سدهٔ نوزدهم) از máscara اسپانیایی است. پس این گره برای mask/masque درست و برای masquerade/mascara تقریبی است؛ شاخهٔ اسپانیایی در نمودار رسم نشده است. با احتیاط پذیرفتنی است.\",\n        \"sources\": [\"https://www.etymonline.com/word/mask\", \"https://www.etymonline.com/word/masquerade\"],\n        \"ref_check\": [\n          {\"ref\": \"None\", \"status\": \"not_checked\",\n           \"note\": \"The node carries no refs= in the book; the parent node's KLN:944 was checked instead and it covers mask, masque, masquerade and mascara in adjacent entries (KLN_1966.txt lines 23036, 23047, 23057).\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 23047 (mask), 23057 (masque, masquerade), 23036 (mascara)\", \"stance\": \"partial\",\n           \"note\": \"'masquerade, n. — F. mascarade, fr. Sp. mascarada … fr. mascara, \\\"mask\\\"'; 'mascara, n. … — Sp. mascara, \\\"a mask\\\", fr. Arab. maskharah' — Spanish, not French, for these two.\"},\n          {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 297, s.v. Mask, Masque\", \"stance\": \"partial\",\n           \"note\": \"'Der. masquerade, F. mascarade, from Span. mascarada' — same split.\"},\n          {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 113291, s.v. mask\", \"stance\": \"supports\",\n           \"note\": \"'mask … [Fr. masque, a mask, visor, from Ar. maskharah, a buffoon.] 1. a covering for the face … to conceal or disguise the identity.'\"}\n        ]\n      }\n    ]\n  },\n\n  # ================= entry 1 =================\n  {\n    \"entry\": 1,\n    \"root\": \"Syand\\nSindhu\",\n    \"verdict\": \"plausible\",\n    \"modern_form\": \"Sanskrit सिन्धु síndhu- m. 'river, stream; the Indus; sea' (< Proto-Indo-Iranian *sindʰu-); Sanskrit √syand (syándate) 'to flow' is a real but probably unrelated root\",\n    \"note\": \"Both words in the root box are genuine Sanskrit: √syand 'to flow, run' (syándate, RV) and síndhu- 'river, flood, the Indus; ocean' (RV, and the river-goddess Sindhu). Nourai's gloss 'the sea' for sindhu is one of its attested senses (it is Hobson-Jobson's rendering, whence his HJB:433). What is not current is the derivation of síndhu- FROM syand-: that is the traditional Indian/19th-century etymology which Skeat repeats verbatim ('Skt. sindhu … — Skt. syand, to flow'), but it fails phonologically (a derivative of syand- should show *syandhu-/*syand-), and Mayrhofer's EWAia leaves síndhu- unexplained. Wiktionary's current Sanskrit entry offers instead a BMAC substrate loan or, alternatively, a connection to sedhati 'to go, move'. The rest of the box — that síndhu- is the etymon of Hind/India — is beyond doubt and is what the whole chart actually rests on; hence 'plausible' rather than 'disputed'.\",\n    \"note_fa\": \"هر دو واژهٔ جعبهٔ ریشه، سنسکریت اصیل‌اند: ریشهٔ «syand-» (syándate) «روان شدن» و «síndhu-» «رود، سیل، رودِ سند؛ دریا» (هر دو در ریگ‌ودا). معنای «دریا» که نورایی آورده یکی از معانی ثبت‌شدهٔ sindhu است (برگرفته از هابسن‌جابسن). آنچه امروزه پذیرفته نیست، اشتقاقِ síndhu- از syand- است: این ریشه‌شناسی سنتیِ دستورنویسان هند و سدهٔ نوزدهم (اسکیت) است، ولی از نظر آوایی درست درنمی‌آید (از syand- باید *syandhu- ساخته شود) و مایرهوفر síndhu- را «نامعلوم» می‌داند؛ ویکی‌واژه آن را وام‌واژه‌ای از زیرلایهٔ باختریِ BMAC یا مربوط به sedhati «رفتن» می‌شمارد. اما بخش دوم ادعا ــ اینکه síndhu- اصلِ «هند» و India است ــ قطعی است و ستون همین نمودار است؛ از این‌رو حکم «با احتیاط پذیرفتنی».\",\n    \"sources\": [\n      W + \"%E0%A4%B8%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A7%E0%A5%81\",\n      \"https://www.etymonline.com/word/indigo\"\n    ],\n    \"ref_check\": [\n      {\"ref\": \"SKT:260\", \"status\": \"supports\",\n       \"note\": \"Skeat s.v. Indigo (SKT.txt leaf 244, the I-section — the OCR carries no page digits, but Indigo falls where p.260 of the 1911 Concise would be): 'Indigo, a blue dye. (F. — Span. — L. — Gk. — Pers. — Skt.) … — Pers. Hind, India; a name due to the river Indus. — Skt. sindhu, the river Indus; a large river. — Skt. syand, to flow. ¶ The Persian changes s into h.' This is verbatim Nourai's root box, and the ¶ note is the source of his Avestan/Old Persian s→h remark.\"},\n      {\"ref\": \"HJB:433\", \"status\": \"supports\",\n       \"note\": \"Hobson-Jobson s.v. INDIA, INDIES (HJB.txt line 11477, leaf 484; the following leaf is headed 'INDIAN. 437 INDIGO,' so the article does begin at p.433): 'The origin of the name is without doubt (Skt.) Sindhu, \\\"the sea,\\\" and thence the Great River on the West … this name exchanged the initial sibilant for an aspirate, and became (eventually) in Persia Hindu, and so passed on to the Greeks and Latins, viz. Ἰνδοί for the people, Ἰνδός for the river.' Nourai's gloss 'the sea' is taken straight from here.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 19161, leaf 422, s.v. India\", \"stance\": \"partial\",\n       \"note\": \"'India, n. — L., fr. Gk. Ἰνδία, fr. Ἰνδός, \\\"the river Indus\\\", fr. OPers. Hindu, fr. OI. sindhuh, \\\"river\\\", spec. \\\"the river Indus\\\"' — the whole chain, but Klein stops at sindhu- and says nothing about syand-.\"},\n      {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, full-text grep for 'sindhu', 'syand', 'Indus'\", \"stance\": \"silent\",\n       \"note\": \"Watkins' Indo-European Roots appendix has no entry covering sindhu-/Hindu-/India (the only hits are the word 'Hindus' in the introduction and 'INDIGENT/INDIGO'-type index lines under other roots). Nourai's bare 'AHD' on nodes #3 and #4 must therefore point at the main AHD dictionary, not the IE appendix.\"},\n      {\"src\": \"HJB\", \"where\": \"HJB.txt line 11477ff., s.v. INDIA, INDIES\", \"stance\": \"supports\",\n       \"note\": \"As quoted above; also 'Sindh' as the surviving native name of the lower Indus country.\"},\n      {\"src\": \"SYN\", \"where\": \"SYN.txt (Buck), grep 'sindhu'\", \"stance\": \"silent\",\n       \"note\": \"Buck's synonym dictionary treats 'river' and 'sea' but does not discuss Skt. sindhu-'s internal etymology.\"}\n    ],\n    \"nodes\": [\n      {\n        \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"hend; hendî\", \"verdict\": \"plausible\",\n        \"derivation\": \"The forms are real but Nourai's citation shape is New-Persian-ised. Avestan has hindu-/həndu- 'river; the land of the Indus, India' — Bartholomae's AiW s.v. hindav-, həndav- 'Name eines Lands, Indien', citing Vd 1.18 hapta həndu 'the seven rivers' (= Skt. saptá síndhavaḥ) and Yt 5(?) 'haca usastara həndva avi daošastarəm həndum' 'from the eastern Hindu to the western'. Old Persian has Hiⁿdu- (written h-i-du-u-š, DPe, DNa 25, DSe 24, DSm 10, XPh 25), Elamite hi-in-du-iš, the satrapy of Sind; Kent's lexicon s.v. Hiⁿdu- gives exactly 'Av. hindu-, Skt. sindhu- \\\"stream, the Indus, country around the Indus\\\"'. The sound law is the regular Proto-Iranian *s > h before a vowel (Skt. sáptá : Av. hapta, Skt. sóma : Av. haoma), which is what Skeat's '¶ The Persian changes s into h' means. Two reservations: (a) neither Avestan nor Old Persian has a form 'hend' with e — that vocalism is the later New Persian هند; (b) 'hendî' is NOT Avestan or Old Persian: the Old Persian gentilic is Hiⁿduya- (Hiduya, A?P 13), while hendī/hindī with the nisba -ī is an Arabic-Persian formation of the Islamic period (it is the Arabic form, as Hobson-Jobson notes s.v. HINDOO: 'The word in this form is Persian; Hindi is that used in Arabic'). The missing middle link, unmentioned by Nourai, is Middle Persian Hindūg/Hindūk (Hübschmann, Persische Studien: 'hindu = phl. hinduk', pl. 'hinduvān … phl. hindukān', Arm. Hndik-k' 'India').\",\n        \"derivation_fa\": \"صورت‌ها واقعی‌اند اما املای نورایی «هندی‌شده» است. در اوستا hindu-/həndu- «رود؛ سرزمین سند، هند» آمده است (بارتولومه، فرهنگ ایرانی باستان، ذیل hindav-: «نام سرزمینی، هند»، با شاهدِ وندیداد ۱٫۱۸ «hapta həndu» = سنسکریت saptá síndhavaḥ «هفت رود»)، و در پارسی باستان Hiⁿdu- (به خط میخی h-i-du-u-š در کتیبه‌های DNa و XPh) نام ساتراپیِ سند است؛ کنت نیز همین را با مقایسهٔ «اوستایی hindu-، سنسکریت sindhu-» می‌آورد. قانون آوایی، تبدیل منظم *s ایرانی آغازین به h در آغاز واژه است (سنسکریت sapta : اوستایی hapta). دو نکته: نخست آنکه صورت «hend» با «ـه‌ـ» نه اوستایی است نه پارسی باستان، بلکه تلفظ فارسی نو است؛ دوم آنکه «hendî» اصلاً اوستایی/پارسی باستان نیست ــ صفت پارسی باستان Hiⁿduya- است و «هندی» با یای نسبت ساختی عربی‑فارسی و متعلق به دورهٔ اسلامی است. حلقهٔ میانیِ ناگفته هم فارسی میانهٔ Hindūg/Hindūk است (هوبشمان: «hindu = phl. hinduk»). پس: با احتیاط پذیرفتنی است.\",\n        \"sources\": [\n          W + \"%E0%A4%B8%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A7%E0%A5%81\",\n          \"https://www.etymonline.com/word/indigo\"\n        ],\n        \"ref_check\": [\n          {\"ref\": \"KLN:787\", \"status\": \"supports\",\n           \"note\": \"Klein s.v. Hindu (KLN_1966.txt line 17822, leaf 395): 'Hindu, also Hindoo, n., one of the Hindu race. — Pers. Hindu, fr. Hind, \\\"India\\\", fr. OI. Sindhuh, \\\"the river Indus; the region of the river Indus\\\".' The h-section of Klein sits at leaf 395 ≈ printed p.767-787, so 787 is within reach; the local OCR has no page markers, so the exact page could not be confirmed. Note Klein labels the intermediary 'Pers.', not Avestan/Old Persian.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BRT\", \"where\": \"BRT.txt line 30076 (leaf 986), s.v. hindav-\", \"stance\": \"supports\",\n           \"note\": \"'j. hindav-, həndav-, p. hiⁿdav- m. Name eines Lands, Indien: … haca usastara °dva avi daošastarəm °dum V.1.18 … mit hapta \\\"sieben\\\" dn.: … yō hapta °du' — Avestan and Old Persian forms side by side, exactly as the chart's language label has them.\"},\n          {\"src\": \"KNT\", \"where\": \"KNT_full.txt line 29835, lexicon s.v. Hiⁿdu-\", \"stance\": \"supports\",\n           \"note\": \"'Hiⁿdu- sb. \\\"Sind\\\", a province of the Persian Empire, on the upper Indus River; Elam. hi-in-du-iš; Av. hindu-, Skt. sindhu- \\\"stream, the Indus, country around the Indus\\\". … Hiduš nsm. DPe; DNa 25; DSe 24; DSm 10; XPh 25.' Kent also has the separate adjective 'Hiⁿduya- adj. \\\"(man) of Sind\\\"', which is what 'hendî' should have been.\"},\n          {\"src\": \"HUB\", \"where\": \"HUB.txt lines 7615, 8640, 8696 (Persische Studien pp. ~214, 242-243)\", \"stance\": \"partial\",\n           \"note\": \"'Hind = ap. Hindu- Indien; Hindu Inder = phl. Hinduk, arm. Hndik-k\\\\' \\\"Indien\\\"'; 'hindu = phl. hinduk'; 'hindu Inder, pl. hinduvān … phl. hindukān Phl. Ys. 56, 11, 6' — supports the chain but inserts the Middle Persian stage the chart skips.\"}\n        ]\n      },\n      {\n        \"id\": 2, \"lang\": \"Persian\", \"words\": \"Hend «هند ( هندوستان )»; hendevâneh «هندوانه»\", \"verdict\": \"confirmed\",\n        \"derivation\": \"NP هند Hend continues Old Persian Hiⁿdu- through Middle Persian Hindūg/Hind (Hübschmann: 'hindu = phl. hinduk'), the OP -u stem being reduced to a bare consonant stem; هندوستان Hendūstān is the same word with the productive place-suffix -stān (Av. stāna- 'place', from stā- 'to stand'), and هندو hendū 'an Indian, a Hindu' is the u-stem preserved. هندوانه hendevâne 'watermelon' is a transparent Persian derivative: هندو hendū 'Indian' + the relational suffix ـانه -āne, i.e. 'the Indian one', so Nourai's gloss \\\"from India\\\" is right. The naming is the same as Arabic بطّيخ هندي biṭṭīx hindī and Persian خربزهٔ هندو 'Indian melon' listed in Borhan-e Qate', which also records the older variant هندوبانه hendūbāne (Ibn al-Balkhi's Fārs-nāma, 12th c.) and quotes a Yemeni gloss 'a fruit that comes from India'. (Mo'in, in his Borhan footnote, adds the dialect forms: Dezfuli, Gilaki, Tabari, and Isfahani gazi sendū, 'attributed to Sind'.)\",\n        \"derivation_fa\": \"«هند» فارسی دنبالهٔ Hiⁿdu- پارسی باستان است که از راه فارسی میانهٔ Hindūg/Hind به فارسی نو رسیده (هوبشمان: «hindu = phl. hinduk»)؛ «هندوستان» همان واژه با پسوند جای‌نام‌سازِ «ـستان» (اوستایی stāna- «جای») است و «هندو» صورتِ ستاکِ ـu را نگاه داشته است. «هندوانه» ساختی سرراست فارسی است: «هندو» + پسوند نسبت «ـانه»، یعنی «(میوهٔ) هندی»؛ پس شرح نورایی «از هند» درست است. همین نام‌گذاری در عربی «بِطّیخ هندی» و در فارسی «خربزهٔ هندو» دیده می‌شود. برهان قاطع صورت کهن‌تر «هندوبانه» (فارس‌نامهٔ ابن‌البلخی) و شرح «لغت یمنی: میوه‌ای که از هند می‌آید» را آورده و معین در حاشیه گونه‌های گویشی (دزفولی، گیلکی، طبری و گزیِ اصفهان «سِندو») را افزوده است. ادعای نورایی درست است.\",\n        \"sources\": [\n          W + \"%D9%87%D9%86%D8%AF%D9%88%D8%A7%D9%86%D9%87\",\n          W + \"%E0%A4%B8%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A7%E0%A5%81\"\n        ],\n        \"ref_check\": [\n          {\"ref\": \"None\", \"status\": \"not_checked\",\n           \"note\": \"The node carries no refs= in the book, so there is nothing of Nourai's to check here; the claim was tested against Borhan-e Qate', Hübschmann and Wiktionary instead (see consulted).\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BQT\", \"where\": \"BQT_v4_pages.txt line 18854, [pdf page 463], s.v. هندوانه\", \"stance\": \"supports\",\n           \"note\": \"'هندوانه … * هندوبانه «فارسنامهٔ ابن‌البلخی ۱۲۷» از هندوان … لغت یمنی: میوه‌ای که از هند می‌آید … [قی: بطیخ‌الهندی] و قی: خربزهٔ هندو، بطیخ هندی … در لهجهٔ گزی اصفهان: سندو (منسوب به سند)' — 'the fruit that comes from India', with the Sind-based dialect form as a bonus.\"},\n          {\"src\": \"HUB\", \"where\": \"HUB.txt line 8696 (Persische Studien p. ~243)\", \"stance\": \"supports\",\n           \"note\": \"'hindu Inder, pl. hinduvān (Indien A.M. 6, 10) — phl. hindukān Phl. Ys. 56, 11, 6' — the Persian word and its Pahlavi antecedent.\"},\n          {\"src\": \"HJB\", \"where\": \"HJB.txt line 11078, s.v. HINDOO\", \"stance\": \"supports\",\n           \"note\": \"'This is a term derived from the use of the Mahommedan conquerors (see under INDIA). The word in this form is Persian; Hindi is that used in Arabic.'\"}\n        ]\n      },\n      {\n        \"id\": 3, \"lang\": \"English\", \"words\": \"Hindu; tamarind\", \"verdict\": \"plausible\",\n        \"derivation\": \"Hindu is correctly drawn from Persian: English (from the 17th c., via Persian usage in Mughal India and the travellers' literature) Hindoo/Hindu < Pers. هندو Hindū 'an Indian' (Klein s.v. Hindu: 'Pers. Hindu, fr. Hind, \\\"India\\\"'), the word having been applied by the Muslim conquerors to the non-Muslim natives, whence the religious sense. tamarind, however, does not come from Persian directly: it is Arabic تمر هندي tamr hindī 'Indian date', latinised as Medieval Latin tamarindus, Old French tamarinde, Middle English tamarinde — the AHD entry gives exactly this chain and notes that 'medieval Arabian merchants imported it from India'. Persian is present only inside the Arabic compound (Arab. hindī is built on Hind, itself the Persian name, as AHD says: 'hindī, of India, from Persian Hind'); Hobson-Jobson adds that the name may 'perhaps rather [be] in Persian form, tamr-i-Hindī'. So the arrow is right about the ultimate Persian element but skips the Arabic and Romance mediation that actually carried the word.\",\n        \"derivation_fa\": \"«Hindu» به‌درستی از فارسی گرفته شده است: انگلیسی Hindoo/Hindu از سدهٔ هفدهم، از راه کاربرد فارسی در هندِ گورکانی، از «هندو»ی فارسی (کلاین: «Pers. Hindu, fr. Hind»)، واژه‌ای که فاتحان مسلمان به بومیان نامسلمان می‌دادند و از همین‌جا معنای دینی یافت. اما «tamarind» یکسره از فارسی نیامده است: از «تمر هندی» عربی («خرمای هندی») است که در لاتینیِ سده‌های میانه tamarindus و در فرانسوی کهن tamarinde شد و از آنجا به انگلیسی میانه رسید؛ فرهنگ American Heritage همین زنجیره را می‌دهد و می‌افزاید که «بازرگانان عرب آن را از هند می‌آوردند». سهم فارسی تنها در جزءِ «هندی» است. هابسن‌جابسن نیز می‌گوید شاید صورت اصلی فارسیِ «تمرِ هندی» بوده باشد. پس: با احتیاط پذیرفتنی است؛ واسطهٔ عربی و رومی در نمودار رسم نشده.\",\n        \"sources\": [\"https://ahdictionary.com/word/search.html?q=tamarind\"],\n        \"ref_check\": [\n          {\"ref\": \"AHD\", \"status\": \"partial\",\n           \"note\": \"Checked twice. (a) The local Watkins 1985 IE-roots appendix (AHD_watkins1985.txt) has no entry for sindhu-/Hindu-/tamarind — grep is silent, so the citation cannot mean the IE appendix. (b) The main AHD (ahdictionary.com, archived) s.v. tamarind does support it, but with the Arabic step Nourai leaves out: 'Middle English tamarinde, from Medieval Latin tamarindus, from Arabic tamr hindī, Indian dates: tamr, dates + hindī, of India, from Persian Hind, India.'\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 38089 (tamarind), line 17822 (Hindu)\", \"stance\": \"partial\",\n           \"note\": \"'tamarind … — Sp. tamarinda (also Port. and It.), fr. Arab. tamr Hindī, \\\"Indian date\\\" … For the second element in tamarind see Hindu, India.' — Klein too routes tamarind through Arabic and Spanish, and only Hindu directly from Persian.\"},\n          {\"src\": \"HJB\", \"where\": \"HJB.txt line 11439ff., leaf 937, s.v. TAMARIND (printed ≈ p.890)\", \"stance\": \"supports\",\n           \"note\": \"'The origin of the name is curious. It is Ar. tamar-u'l-Hind, \\\"date of India,\\\" or perhaps rather in Persian form, tamr-i-Hindī.'\"},\n          {\"src\": \"AID\", \"where\": \"AID.txt, grep 'tamarind'/'Hindu'\", \"stance\": \"silent\",\n           \"note\": \"Whitworth's Anglo-Indian Dictionary gives the plant but no etymological chain beyond 'Hind.'\"}\n        ]\n      },\n      {\n        \"id\": 4, \"lang\": \"Greek\", \"words\": \"Indos\", \"verdict\": \"confirmed\",\n        \"derivation\": \"Greek Ἰνδός 'the river Indus' (and Ἰνδοί 'the Indians', Ἰνδία 'India') is a direct borrowing of Old Persian Hiⁿdu-, taken over in Ionian Asia Minor in the 6th-5th c. BCE — the Persians were the Greeks' informants about the eastern satrapies, and Hekataios and then Herodotos (3.94, 4.44) use Ἰνδοί of the people of the Achaemenid satrapy Hiⁿduš. The loss of the initial h- is the psilosis of the East Ionic dialect through which the word passed (the same dialect that gave ἵππος : Ion. ἴππος), so OPers. Hindu- → Ion. Ἰνδός, not *Ἵνδος. Klein states the chain without comment: 'Gk. Ἰνδία, fr. Ἰνδός, \\\"the river Indus\\\", fr. OPers. Hindu'.\",\n        \"derivation_fa\": \"«Ἰνδός» یونانی (نام رود سند) و «Ἰνδοί» (هندیان) و «Ἰνδία» وام‌گیریِ مستقیم از Hiⁿdu- پارسی باستان است که در سدهٔ ششم و پنجم پیش از میلاد در آسیای صغیر ایونی صورت گرفت؛ آگاهی یونانیان از ساتراپی‌های خاوری از راه هخامنشیان بود و هکاتایوس و سپس هرودوت (۳٫۹۴ و ۴٫۴۴) «Ἰνδοί» را برای مردم ساتراپیِ Hiⁿduš به کار می‌برند. افتادن «ه» آغازین پیامد «سایش‌زدایی» (psilosis) گویش ایونی خاوری است که واژه از آن گذر کرده؛ از این‌رو Ἰνδός و نه *Ἵνδος. کلاین همین زنجیره را بی‌چون‌وچرا می‌آورد. ادعای نورایی درست است.\",\n        \"sources\": [\"https://www.etymonline.com/word/indigo\"],\n        \"ref_check\": [\n          {\"ref\": \"AHD\", \"status\": \"not_found\",\n           \"note\": \"AHD_watkins1985.txt (the local Watkins IE-roots appendix, which is what Nourai's bare 'AHD' normally means) has no entry for Indos/Indus/sindhu-: grep for 'sindhu', 'syand', 'Indus' returns only unrelated index and preface lines. The main AHD dictionary does carry the etymology under India/Indus, but a page could not be cited.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 19161, s.v. India\", \"stance\": \"supports\",\n           \"note\": \"'L., fr. Gk. Ἰνδία, fr. Ἰνδός, \\\"the river Indus\\\", fr. OPers. Hindu, fr. OI. sindhuh'\"},\n          {\"src\": \"HJB\", \"where\": \"HJB.txt line 11477, s.v. INDIA, INDIES (p.433)\", \"stance\": \"supports\",\n           \"note\": \"'…became (eventually) in Persia Hindu, and so passed on to the Greeks and Latins, viz. Ἰνδοί for the people, Ἰνδός for the river, Ἰνδική and India for the country on its banks.'\"},\n          {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 244, s.v. Indigo\", \"stance\": \"supports\",\n           \"note\": \"'— Gk. Ἰνδικόν, indigo; neut. of Ἰνδικός, Indian. — Pers. Hind, India; a name due to the river Indus.'\"}\n        ]\n      },\n      {\n        \"id\": 5, \"lang\": \"Latin\", \"words\": \"Indus\", \"verdict\": \"confirmed\",\n        \"derivation\": \"Latin Indus 'the river Indus; an Indian' and India 'India' are ordinary Hellenistic-period borrowings of Gk. Ἰνδός / Ἰνδία with the regular Latin substitution of -us/-a for Greek -ος/-ία; they enter Latin with the Alexander literature and the geographers (Pliny, NH 6.71ff., 'Indus incolis Sindus appellatus' — Pliny even knows the native s-form). The adjective Indicus (< Gk. Ἰνδικός) yields indicum 'indigo', the vehicle of node #6. Klein: 'India, n. — L., fr. Gk. Ἰνδία'.\",\n        \"derivation_fa\": \"«Indus» و «India» لاتینی وام‌گیری‌های عادیِ دورهٔ هلنیستی از Ἰνδός و Ἰνδία یونانی‌اند، با جایگزینی منظم پایانهٔ ‑us/‑a به‌جای ‑ος/‑ία؛ این واژه‌ها با ادبیات اسکندر و جغرافی‌نویسان وارد لاتین شدند (پلینی، تاریخ طبیعی ۶٫۷۱: «Indus incolis Sindus appellatus» ــ او حتی صورت بومی با «س» را می‌شناسد). صفت Indicus (از Ἰνδικός) واژهٔ indicum «نیل» را می‌دهد که پایهٔ گرهِ بعدی است. ادعای نورایی درست است.\",\n        \"sources\": [\"https://www.etymonline.com/word/indigo\"],\n        \"ref_check\": [\n          {\"ref\": \"None\", \"status\": \"not_checked\",\n           \"note\": \"No refs= on this node in the book; checked against Klein and Skeat instead.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 19161, 19163 (India, Indic)\", \"stance\": \"supports\",\n           \"note\": \"'India, n. — L., fr. Gk. Ἰνδία'; 'Indic, adj. … — L. Indicus, fr. Gk. Ἰνδικός, fr. Ἰνδία.'\"},\n          {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 244, s.v. Indigo\", \"stance\": \"supports\",\n           \"note\": \"'— L. indicum, indigo; neut. of Indicus, Indian (hence Indian dye).'\"},\n          {\"src\": \"LAT\", \"where\": \"LAT.txt (Ernout-Meillet), grep 'Indus'\", \"stance\": \"silent\",\n           \"note\": \"Ernout-Meillet's dictionary of inherited Latin excludes Greek-derived proper names of this kind.\"}\n        ]\n      },\n      {\n        \"id\": 6, \"lang\": \"English\", \"words\": \"India; Indian; indigo; indium\", \"verdict\": \"confirmed\",\n        \"derivation\": \"India (OE India, re-borrowed in ME from Latin) and Indian (ME Indien, from Old French indien / Med. Latin indianus) are the Latin word naturalised. indigo is the same root by a commercial route: Gk. ἰνδικόν (φάρμακον) 'the Indian dye', neut. of Ἰνδικός → L. indicum → Sp. índico / Port. endego → Du. indigo → Fr./Eng. indigo, first in English 1550s as indico, the colour sense from the 1620s and Newton's spectral band in 1704. indium is a learned 19th-century coinage: Reich and Richter discovered the metal at Freiberg in 1863 and named it in 1864 from Modern Latin indicum 'indigo' + -ium, for the brilliant indigo-blue line in its spark spectrum. All four therefore descend from Latin Indus/Indicus as the chart draws them.\",\n        \"derivation_fa\": \"«India» و «Indian» همان واژهٔ لاتینی‌اند که از راه فرانسوی کهن و لاتینیِ سده‌های میانه در انگلیسی جا افتاده‌اند. «indigo» از همان ریشه اما از راه بازرگانی آمده است: یونانی ἰνδικόν (φάρμακον) «رنگِ هندی» ← لاتین indicum ← اسپانیایی índico ← هلندی indigo ← انگلیسی indigo (نخستین کاربرد ۱۵۵۰م به صورت indico؛ معنای «رنگ» از ۱۶۲۰م و نامِ نوار طیفی از نیوتن، ۱۷۰۴م). «indium» ساختی علمی است: رایش و ریشتر در ۱۸۶۳م این فلز را در فرایبرگ یافتند و در ۱۸۶۴م از indicum «نیل» به‌علاوهٔ پسوند ‑ium نامیدند، به سبب خطِ نیلی‌رنگِ درخشان در طیف آن. پس هر چهار واژه، چنان‌که نمودار می‌کشد، از Indus/Indicus لاتینی‌اند. ادعای نورایی درست است.\",\n        \"sources\": [\"https://www.etymonline.com/word/indigo\"],\n        \"ref_check\": [\n          {\"ref\": \"None\", \"status\": \"not_checked\",\n           \"note\": \"No refs= on this node; the parent chain's AHD/KLN citations were checked instead.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 19161, 19188, s.v. India / indigo\", \"stance\": \"supports\",\n           \"note\": \"'indigo, n., a blue dye. — F., fr. Du. indigo, borrowed fr. Sp. indico, indigo, fr. L. indicum … fr. Gk. ἰνδικόν (short for Ἰνδικὸν φάρμακον, lit. \\\"Indian dye\\\"), neut. of Ἰνδικός, \\\"Indian\\\". See Indic.' Klein's India entry also cross-refers 'Cp. Hindu, indign, indium, sandia, sendal, sindon.'\"},\n          {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 244, s.v. Indigo\", \"stance\": \"supports\",\n           \"note\": \"'Indigo, a blue dye. (F. — Span. — L. — Gk. — Pers. — Skt.) F. indigo. — Span. indico. — L. indicum … — Gk. ἰνδικόν … — Pers. Hind, India.'\"},\n          {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt, s.v. indium\", \"stance\": \"supports\",\n           \"note\": \"Webster gives indium as named from the indigo-blue line of its spectrum, matching Etymonline's 1864 dating.\"}\n        ]\n      }\n    ]\n  },\n\n  # ================= entry 3 =================\n  {\n    \"entry\": 3,\n    \"root\": \"Šypwr\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"Syriac ܫܝܦܘܪܐ šīpūrā / Jewish Babylonian Aramaic שִׁיפּוּרָא šīppūrā 'horn, trumpet, shofar'\",\n    \"note\": \"The root box is right in language, form and gloss. Aramaic šīpūrā / Syriac šīpōrā 'trumpet' is the Aramaic counterpart of Hebrew שׁוֹפָר šōfār (the ram's-horn of the synagogue), the p being spirantised to [f] in Aramaic; the same word gave Arabic شَبُّور šabbūr 'trumpet', which Borhan-e Qate' registers as a mu‘arrab beside šeypūr. Nourai's 'Šypwr' is simply the consonantal skeleton š-y-p-w-r. The Aramaic→Persian borrowing is the standard explanation of شیپور in Persian lexicography (Mo'in's footnote in Borhan, Dehkhoda, Nöldeke's Persische Studien, Vullers) and is what Wiktionary now gives. The one weak link is the intermediate Pahlavi box (node #1), which no Middle Persian lexicon attests.\",\n    \"note_fa\": \"جعبهٔ ریشه از هر سه جهت ــ زبان، صورت و معنی ــ درست است. «شیپورا»ی آرامی/سریانی «بوق، کَرِنا» همتای آرامیِ «شوفار» عبری (شاخِ قوچِ کنیسه) است و «پ» در آرامی به [ف] سایشی بدل شده؛ همین واژه «شَبّور» عربی را هم داده که برهان قاطع آن را معرّب و هم‌ارز «شیپور» می‌آورد. نگارشِ «Šypwr» در کتاب صرفاً اسکلتِ همخوانیِ ش‑ی‑پ‑و‑ر است. وام‌گیری آرامی ← فارسی، تبیین معیار در فرهنگ‌نویسی فارسی است (حاشیهٔ معین بر برهان، دهخدا، نولدکه، ولرس) و ویکی‌واژه نیز همان را می‌آورد. تنها حلقهٔ سست، جعبهٔ فارسی میانه است (گرهِ ۱) که در هیچ واژه‌نامهٔ پهلوی شاهدی ندارد.\",\n    \"sources\": [\n      W + \"%D8%B4%DB%8C%D9%BE%D9%88%D8%B1\",\n      \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D9%BE%D9%88%D8%B1/\"\n    ],\n    \"ref_check\": [\n      {\"ref\": \"TZF:77\", \"status\": \"not_checked\",\n       \"note\": \"TZF = Abolghasemi, Tārīx-e Moxtaṣar-e Zabān-e Fārsī; refs_online.json has no downloadable copy (ketabnak.com login-only, not on archive.org), so p.77 could not be read. The Aramaic→Persian claim is independently confirmed by Mo'in's own footnote in Borhan-e Qate' and by Wiktionary (see consulted).\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"BQT_v3_pages.txt line 8496 ([pdf page 110-111] of the vol.3 scan ≈ printed p.1315-1319), s.v. شیپور\", \"stance\": \"supports\",\n       \"note\": \"Mo'in's etymological footnote: 'شیپور از آرامی و سریانی گرفته شده «نقی‌زاده … یادگار، سال چهارم، شمارهٔ …»' — 'šeypūr is taken from Aramaic and Syriac'. The entry also equates it with شیبور ('۸ = شیبور. هر دو در شاهنامه آمده'), noting that Wolff's Shahnameh index renders both by Tuba/Trompete.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. شیپور\", \"stance\": \"partial\",\n       \"note\": \"'(شَ) (اِ.) = شبور: از سازهای بادی، دارای دهانه‌ای گشاد' — Mo'in equates šeypūr with شبور but gives no origin tag in the online text.\"},\n      {\"src\": \"AFA\", \"where\": \"AFA.txt (Fraenkel, Die aramäischen Fremdwörter im Arabischen), grep 'sipura', 'Schofar', 'Trompete'\", \"stance\": \"silent\",\n       \"note\": \"No hit; Fraenkel treats Aramaic loans in Arabic and does not cover the Persian word.\"}\n    ],\n    \"nodes\": [\n      {\n        \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"šayfur\", \"verdict\": \"unverified\",\n        \"derivation\": \"A Sasanian-period borrowing of Aramaic šīpūrā into Middle Persian is entirely plausible in principle — Aramaic supplied Middle Persian with a whole stratum of vocabulary (and its writing system), and the -f- Nourai writes is in fact the right reflex: post-vocalic p in Aramaic is spirantised to [f] (šīp̄ūrā), so an MP *šēfūr/šayfūr is what one would expect. But I could find no attestation. MacKenzie's Concise Pahlavi Dictionary has no šēpūr/šayfūr (its word for 'trumpet' is gāw-dumb, lit. 'ox-tail', PHD.txt lines 2312, 4080); Nyberg's glossary is likewise silent; Wiktionary's شیپور entry records no Middle Persian form at all and derives the New Persian word straight from Aramaic/Syriac. Nourai's only authority is TZF:77, which I could not open. The Pahlavi box should be read as a reconstruction, not an attested form, and its vocalism (šay- rather than šē-) is Nourai's New-Persian-style transcription.\",\n        \"derivation_fa\": \"وام‌گیری «شیپورا»ی آرامی به فارسی میانه در دورهٔ ساسانی به‌خودی‌خود پذیرفتنی است ــ آرامی لایه‌ای بزرگ از واژگان (و خطِ) فارسی میانه را فراهم کرده ــ و حتی «ف»ی که نورایی می‌نویسد بازتاب درستی است، زیرا «پ» پس از واکه در آرامی سایشی و [ف] می‌شود (šīp̄ūrā). اما هیچ شاهدی نیافتم: در فرهنگ پهلویِ مکنزی چنین واژه‌ای نیست (واژهٔ پهلویِ «بوق» در آن gāw-dumb «دُمِ گاو» است) و واژه‌نامهٔ نیبرگ هم خاموش است؛ ویکی‌واژه نیز هیچ صورت فارسی میانه‌ای ثبت نکرده و واژهٔ فارسی نو را یکسره از آرامی/سریانی می‌گیرد. تنها مأخذ نورایی TZF:77 است که در دسترس نبود. پس این جعبه را باید بازسازی (با ستاره) دانست نه صورتی گواهی‌شده؛ آوانگاریِ šay- هم به سبک فارسی نو است نه فارسی میانه.\",\n        \"sources\": [W + \"%D8%B4%DB%8C%D9%BE%D9%88%D8%B1\"],\n        \"ref_check\": [\n          {\"ref\": \"TZF:77\", \"status\": \"not_checked\",\n           \"note\": \"Abolghasemi's Tārīx-e Moxtaṣar-e Zabān-e Fārsī is not available online (login-gated PDF at ketabnak.com; not on archive.org) — this is the only place Nourai's Pahlavi form could be sourced.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, grep 'šyp', 'šēpūr', 'šayfur', 'trumpet'\", \"stance\": \"contradicts\",\n           \"note\": \"MacKenzie has no such headword. The š-section (PHD.txt line 583) runs šēb 'declivity', šēb- 'move quickly', šēdā, šēr, šēwan — no šēpūr. MacKenzie's English-Pahlavi index gives 'trumpet gawdumb' (line 4080) and 'horn srū; (trumpet) gāwdumb' (line 2312).\"},\n          {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'trumpet', 'šēpūr', 'šypwr'\", \"stance\": \"silent\",\n           \"note\": \"Nyberg's Pahlavi glossary returns no hit for the word.\"},\n          {\"src\": \"BQT\", \"where\": \"BQT_v3_pages.txt, Mo'in's footnote s.v. شیپور\", \"stance\": \"partial\",\n           \"note\": \"Mo'in names Aramaic and Syriac as the source but says nothing about a Pahlavi intermediary, i.e. he does not corroborate this box.\"}\n        ]\n      },\n      {\n        \"id\": 2, \"lang\": \"Persian\", \"words\": \"šaypŭr «شیپور ( شیپور )»\", \"verdict\": \"transcription_suspect\",\n        \"error_in\": \"extraction\",\n        \"book_prints\": \"شیپور ( شیبور )\",\n        \"correct_form\": \"شیپور ( شیبور )\",\n        \"derivation\": \"The etymology itself is confirmed: NP شیپور šeypūr 'trumpet, bugle' is a loan from Aramaic/Syriac šīpūrā (Hebrew šōfār), already fully naturalised in the 10th-11th c. — Ferdowsi uses it in the line the book quotes, «بفرمود تا برکشیدند نای / همان سنج و شیپور و هندی درای», and Nizami and Asadi have it too; Dehkhoda glosses it 'نفیر، کرنای کوچک' and lists the Hebrew/Aramaic/Syriac derivation (alongside a folk-etymological 'shāh-pūr' which should be rejected). Borhan-e Qate' records the doublet شیبور šeybūr with b for p, 'both occurring in the Shahnameh'. THE EXTRACTION IS AT FAULT IN THE SCRIPT FIELD: the printed page (pdf p.493, copied to data/verification/sources/refs/ocr/BOOK/493.png) shows «شیپور ( شیبور )» — the parenthetical variant is written with ب (one dot below), as a 400-dpi enlargement of the box makes plain, and as Borhan's entry independently predicts — whereas the JSON has «شیپور ( شیپور )», repeating the headword. The transliteration šaypŭr with a breve is Nourai's own rendering of the long ū and is faithful to the page (the book prints šaypŭr).\",\n        \"derivation_fa\": \"ریشه‌شناسی خودِ واژه تأیید می‌شود: «شیپور» فارسی وام‌واژه‌ای است از «شیپورا»ی آرامی/سریانی (هم‌ریشه با «شوفار» عبری) که تا سدهٔ چهارم و پنجم هجری کاملاً فارسی شده بود؛ فردوسی همان بیتی را دارد که کتاب نقل کرده («بفرمود تا برکشیدند نای / همان سنج و شیپور و هندی درای») و نظامی و اسدی نیز آن را به‌کار برده‌اند. دهخدا آن را «نفیر، کرنای کوچک» معنی می‌کند و اشتقاق عبری/آرامی/سریانی را می‌آورد (در کنار ریشه‌شناسی عامیانهٔ «شاه‌پور» که پذیرفتنی نیست). برهان قاطع گونهٔ «شیبور» را نیز ثبت کرده و می‌گوید «هر دو در شاهنامه آمده است». خطا از خوانشِ اسکن است: صفحهٔ چاپی «شیپور ( شیبور )» دارد ــ واژهٔ داخل پرانتز با «ب» (یک نقطه) نوشته شده، چنان‌که بزرگ‌نماییِ ۴۰۰ نقطه‌بر‌اینچ نشان می‌دهد و برهان قاطع نیز مستقلاً تأیید می‌کند ــ ولی در JSON هر دو «شیپور» آمده است.\",\n        \"sources\": [\n          W + \"%D8%B4%DB%8C%D9%BE%D9%88%D8%B1\",\n          \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D9%BE%D9%88%D8%B1/\"\n        ],\n        \"ref_check\": [\n          {\"ref\": \"TZF:77\", \"status\": \"not_checked\",\n           \"note\": \"Abolghasemi's Tārīx-e Moxtaṣar-e Zabān-e Fārsī not obtainable (see root ref_check).\"},\n          {\"ref\": \"MON:2101\", \"status\": \"supports\",\n           \"note\": \"Mo'in s.v. شیپور, read through abadis.ir: '(شَ) (اِ.) = شبور: از سازهای بادی، دارای دهانه‌ای گشاد' — the word and the equation with شبور are there; the page number cannot be checked online, but 2101 is consistent with the ش-section of Mo'in's continuous pagination.\"},\n          {\"ref\": \"BQT:1319\", \"status\": \"supports\",\n           \"note\": \"Found in the vol.3 scan text at BQT_v3_pages.txt line 8489-8496, tagged [pdf page 110-111]; with the tool's offset (printed = pdf + 1205) that is printed p.1315-1316, i.e. within four pages of Nourai's 1319 — the offset in ref_page.py is approximate for this volume. The entry carries the very Ferdowsi verse the book quotes ('همان سنج وشیپور وهندی درای، شاهنامه') and Mo'in's footnote 'شیپور از آرامی و سریانی گرفته شده', plus the cross-reference '# شیبور - رك: شیپور'.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BQT\", \"where\": \"BQT_v3_pages.txt lines 8489-8496 ([pdf page 110-111] ≈ printed 1315-1319)\", \"stance\": \"supports\",\n           \"note\": \"'شیپور … ۸ = شیبور. هر دو در شاهنامه آمده… فهرست ولف آن دو را به Tuba, Trompete ترجمه کرده… «بفرمود تا برکشیدند نای / همان سنج وشیپور وهندی درای» شاهنامه … شیپور از آرامی و سریانی گرفته شده.' Also, at line 2764, the Arabic doublet: 'معرب … شبور … بوق … قس: شیپور'.\"},\n          {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین and لغت‌نامهٔ دهخدا s.v. شیپور\", \"stance\": \"supports\",\n           \"note\": \"Dehkhoda: 'نفیر … کرنای کوچک … بوق برنجین', with the etymology given as Hebrew שופר and Aramaic/Syriac (and a rejected 'شاه‌پور').\"},\n          {\"src\": \"PHD\", \"where\": \"PHD.txt, grep 'trumpet'\", \"stance\": \"contradicts\",\n           \"note\": \"MacKenzie's Pahlavi word for 'trumpet' is gāw-dumb, not a šēpūr — reinforcing that the Persian word's Semitic source reached Persian without an attested Middle Persian stage.\"}\n        ]\n      }\n    ]\n  }\n  ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-493.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-493.py && python3 -m json.tool data/verification/page-493.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 493",
 "description": "Write and validate page-493.json"
}
```


### [2026-09-14T03:26:03.409Z] TOOL RESULT

```
written
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 8, 'disputed': 1, 'plausible': 3, 'unverified': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'not_checked': 7, 'supports': 7, 'partial': 1, 'not_found': 1}
books consulted: {'supports': 28, 'silent': 6, 'partial': 7, 'contradicts': 2} | by book: {'SKT': 7, 'KLN': 6, 'BQT': 5, 'WEB': 4, 'MON': 3, 'HJB': 3, 'RCH': 2, 'HUB': 2, 'PHD': 2, 'LKT': 1, 'DEV': 1, 'PHN': 1, 'ARY': 1, 'BRT': 1, 'KNT': 1, 'AID': 1, 'LAT': 1, 'NYB': 1}
```


## [2026-09-14T03:26:07.277Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"in'di-um\\|indium\" WEB_vol1.txt | head -3 | cut -c1-400",
 "description": "Check Webster indium"
}
```


### [2026-09-14T03:26:07.351Z] TOOL RESULT

```
95841:In, in SME indium, in, prep. E. in, yn; AS. in, in: wi ple form of in there became Mie the sim. inne, from AS. inne, in, within Ss the ME 1. contained or enclosed by, į 4
```


## [2026-09-14T03:26:12.110Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'indigo-blue line\\|in-di-um\\|indium' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -5 | cut -c1-400",
 "description": "Funk Wagnalls indium"
}
```


### [2026-09-14T03:26:12.198Z] TOOL RESULT

```
FSD_vol1.txt:13185:iron,  indium,  or  gallium,  and  a   sulfate  or  a   selenate  of sodium,  potassium,  rubidium,  cesium,  ammonium,  sil- ver, or  thallium.  Other  combinations  are  possible.
```


## [2026-09-14T03:26:18.895Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json,io\np=\"data/verification/page-493.json\"\nd=json.load(open(p))\nn=[x for x in d[\"entries\"] if x[\"entry\"]==1][0][\"nodes\"]\nnode6=[x for x in n if x[\"id\"]==6][0]\nfor c in node6[\"consulted\"]:\n    if c[\"src\"]==\"WEB\":\n        c[\"where\"]=\"WEB_vol1.txt, grep 'indium' / 'in-di-um'\"\n        c[\"stance\"]=\"silent\"\n        c[\"note\"]=\"Webster's New Twentieth Century vol. 1 as OCR'd here has no usable indium entry (the only 'indium' hit, line 95841, is OCR noise inside the entry for the preposition 'in'), so it could not corroborate the 1863/64 naming; that rests on Etymonline s.v. indium.\"\njson.dump(d,io.open(p,\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=2)\nio.open(p,\"a\",encoding=\"utf-8\").write(\"\\n\")\nprint(\"patched\")\nPY\npython3 -m json.tool data/verification/page-493.json >/dev/null && python3 tools/verify_check.py 493",
 "description": "Fix unverified WEB citation"
}
```


### [2026-09-14T03:26:20.030Z] TOOL RESULT

```
patched
nodes verified: 14/14
node verdicts: {'confirmed': 8, 'disputed': 1, 'plausible': 3, 'unverified': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'not_checked': 7, 'supports': 7, 'partial': 1, 'not_found': 1}
books consulted: {'supports': 27, 'silent': 7, 'partial': 7, 'contradicts': 2} | by book: {'SKT': 7, 'KLN': 6, 'BQT': 5, 'WEB': 4, 'MON': 3, 'HJB': 3, 'RCH': 2, 'HUB': 2, 'PHD': 2, 'LKT': 1, 'DEV': 1, 'PHN': 1, 'ARY': 1, 'BRT': 1, 'KNT': 1, 'AID': 1, 'LAT': 1, 'NYB': 1}
```


## [2026-09-14T03:26:37.320Z] AGENT

Page 493 verified. `verify_check.py 493` → 14/14 nodes, 0 PROBLEM lines.

**Verdicts** — roots: 2 confirmed, 1 plausible. Nodes: 8 confirmed, 3 plausible, 1 disputed, 1 unverified, 1 transcription_suspect.

**Disputed**
- *S.x.r* #3 **Italian maschera** — Nourai (after Klein/Skeat/Lokotsch/Dozy-Devic) takes it from Arabic *masxarah*; modern Romance etymology starts from Medieval Latin *masca* 'witch, spectre', attested in the Lombard *Edictus Rothari* §197 (643 CE), two centuries before Arabic contact in Italy. Also the gloss is wrong: It. *maschera* means 'mask', not 'mockery'. Everything downstream (Fr. *masque*, Eng. *mask*, Pers. ماسک) is unaffected.

**Transcription_suspect — EXTRACTION ERROR for the owner to fix**
- *Šypwr* #2 Persian: the book prints «شیپور ( شیبور )» — the parenthetical variant has **ب**, not پ (confirmed at 400 dpi; page PNG saved to `data/verification/sources/refs/ocr/BOOK/493.png`, and Borhan-e Qate' independently lists شیبور as the Shahnameh doublet). The JSON at `data/extracted/batch/page-493.json` has «شیپور ( شیپور )». The etymology itself is confirmed.

**Unverified**
- *Šypwr* #1 Pahlavi *šayfur* — no attestation anywhere: MacKenzie's Pahlavi for 'trumpet' is *gāw-dumb*, Nyberg silent, Wiktionary records no MP form; Nourai's sole authority TZF:77 (Abolghasemi) is not obtainable online. Treat as a reconstruction.

**Other caveats worth noting**
- Root *Syand/Sindhu* marked plausible: Skt. *síndhu-* → Hind/India is certain, but its derivation from √*syand* 'to flow' is the old Indian/Skeat etymology; Mayrhofer leaves *síndhu-* unexplained and Wiktionary prefers a BMAC substrate loan.
- *Sindhu* #1: "hendî" is not Avestan/Old Persian (OP gentilic is *Hiⁿduya-*; *hindī* is the Arabic-Persian nisba); the Middle Persian link *Hindūg/Hindūk* (Hübschmann) is missing from the chart.
- *Sindhu* #3: **tamarind** reaches English via Arabic *tamr hindī* → Med. Lat. *tamarindus*, not straight from Persian. Nourai's bare "AHD" here cannot mean the Watkins IE-roots appendix (silent on *sindhu-*); the main AHD dictionary does support it.
- Inaccessible references: SAP:683 (purchase-only) and TZF:77 (login-gated) — both marked `not_checked`; their claims were corroborated from Klein/Skeat/Richardson and from Mo'in's own footnote in Borhan-e Qate' (BQT:1319, found at vol. 3 pdf p. 110-111, ≈4 pages off the tool's offset).
