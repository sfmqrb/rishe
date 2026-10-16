# Verification process log — verify-page-529


## [2026-10-16T05:13:01.847Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 529 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-529.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-529.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-529.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 529` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.915Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.349Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.374Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
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
279	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-10-16T05:13:05.847Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-529.txt"
}
```


### [2026-10-16T05:13:05.868Z] TOOL RESULT

```
1	=== PDF page 529 (book page 499) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wedh 2 : to push, strike, hit  (refs POK:1115)
4	#1 (parent #0) [Avestan] refs=POK:1115 | vâdâya : push, push back ; vada : wedge ; vadar : weapon for striking ; vadhğan : ax
5	#2 (parent #0) [Greek] refs=POK:1115; AHD | ôthein : to push ; ôsmos : act of pushing (liquids)
6	  #3 (parent #2) [Latin] refs=None | 
7	    #4 (parent #3) [French] refs=KLN:1100 | osmose
8	      #5 (parent #4) [Persian] refs=VOP:52 | osmoz «اُسمُز» : osmosis | extra: اسمزی
9	    #6 (parent #3) [English] refs=AHD | osmosis
10	--- entry 1 ---
11	ROOT [Indo-European] Weg 1 / Wokso : to weave / woven (by the bees), wax  (refs POK:1117, 1180)
12	#1 (parent #0) [Russian] refs=? | 
13	  #2 (parent #1) [Persian] refs=MON:4958 | vâks «واکس» : wax
14	#3 (parent #0) [Germanic] refs=AHD:1550 | wahsam ; weke
15	  #4 (parent #3) [English] refs=None | wax ; wick
16	#5 (parent #0) [Latin] refs=KLN:1695 | velum : woven fabric
17	  #6 (parent #5) [English] refs=None | veil ; reveal
18	
```


## [2026-10-16T05:13:06.466Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-529.json"
}
```


### [2026-10-16T05:13:06.732Z] TOOL RESULT

```
1	{
2	  "pdf_page": 529,
3	  "book_page": 499,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wedh 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:1115",
10	        "gloss": "to push, strike, hit"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1115",
18	          "words": [
19	            {"translit": "vâdâya", "gloss": "push, push back", "script": null},
20	            {"translit": "vada", "gloss": "wedge", "script": null},
21	            {"translit": "vadar", "gloss": "weapon for striking", "script": null},
22	            {"translit": "vadhğan", "gloss": "ax", "script": null}
23	          ],
24	          "note": null,
25	          "quote": null
26	        },
27	        {
28	          "id": 2,
29	          "parent": 0,
30	          "lang": "Greek",
31	          "refs": "POK:1115; AHD",
32	          "words": [
33	            {"translit": "ôthein", "gloss": "to push", "script": null},
34	            {"translit": "ôsmos", "gloss": "act of pushing (liquids)", "script": null}
35	          ],
36	          "note": null,
37	          "quote": null
38	        },
39	        {
40	          "id": 3,
41	          "parent": 2,
42	          "lang": "Latin",
43	          "refs": null,
44	          "words": [],
45	          "note": null,
46	          "quote": null
47	        },
48	        {
49	          "id": 4,
50	          "parent": 3,
51	          "lang": "French",
52	          "refs": "KLN:1100",
53	          "words": [
54	            {"translit": "osmose", "gloss": null, "script": null}
55	          ],
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 5,
61	          "parent": 4,
62	          "lang": "Persian",
63	          "refs": "VOP:52",
64	          "words": [
65	            {"translit": "osmoz", "gloss": "osmosis", "script": "اُسمُز"}
66	          ],
67	          "script_extra": "اسمزی",
68	          "note": null,
69	          "quote": null
70	        },
71	        {
72	          "id": 6,
73	          "parent": 3,
74	          "lang": "English",
75	          "refs": "AHD",
76	          "words": [
77	            {"translit": "osmosis", "gloss": null, "script": null}
78	          ],
79	          "note": null,
80	          "quote": null
81	        }
82	      ]
83	    },
84	    {
85	      "root": {
86	        "name": "Weg 1 / Wokso",
87	        "lang": "Indo-European",
88	        "refs": "POK:1117, 1180",
89	        "gloss": "to weave / woven (by the bees), wax"
90	      },
91	      "nodes": [
92	        {
93	          "id": 1,
94	          "parent": 0,
95	          "lang": "Russian",
96	          "refs": "?",
97	          "words": [],
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 2,
103	          "parent": 1,
104	          "lang": "Persian",
105	          "refs": "MON:4958",
106	          "words": [
107	            {"translit": "vâks", "gloss": "wax", "script": "واکس"}
108	          ],
109	          "note": null,
110	          "quote": null
111	        },
112	        {
113	          "id": 3,
114	          "parent": 0,
115	          "lang": "Germanic",
116	          "refs": "AHD:1550",
117	          "words": [
118	            {"translit": "wahsam", "gloss": null, "script": null},
119	            {"translit": "weke", "gloss": null, "script": null}
120	          ],
121	          "note": null,
122	          "quote": null
123	        },
124	        {
125	          "id": 4,
126	          "parent": 3,
127	          "lang": "English",
128	          "refs": null,
129	          "words": [
130	            {"translit": "wax", "gloss": null, "script": null},
131	            {"translit": "wick", "gloss": null, "script": null}
132	          ],
133	          "note": null,
134	          "quote": null
135	        },
136	        {
137	          "id": 5,
138	          "parent": 0,
139	          "lang": "Latin",
140	          "refs": "KLN:1695",
141	          "words": [
142	            {"translit": "velum", "gloss": "woven fabric", "script": null}
143	          ],
144	          "note": null,
145	          "quote": null
146	        },
147	        {
148	          "id": 6,
149	          "parent": 5,
150	          "lang": "English",
151	          "refs": null,
152	          "words": [
153	            {"translit": "veil", "gloss": null, "script": null},
154	            {"translit": "reveal", "gloss": null, "script": null}
155	          ],
156	          "note": null,
157	          "quote": null
158	        }
159	      ]
160	    }
161	  ]
162	}
163	
```


## [2026-10-16T05:13:11.977Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','VOP','MON','WLD','IEC','SYN','BRT','KNT','SKT','FSD','WEB','ARY']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-16T05:13:12.350Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-10-16T05:13:20.303Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/ | tail -5; ls data/verification/page-52*.json; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','WLD']:\n  e=d[k]; print(k, {x:e.get(x) for x in ['local_file','page_offset','lookup_hint','notes']})\n  print()\n\""
}
```


### [2026-10-16T05:13:20.749Z] TOOL RESULT

```
.rw-r--r--   40k sfmqrb 14 Oct 22:50  page-514.json
.rw-r--r--   22k sfmqrb 14 Oct 22:47  page-515.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  page-518.json
Permissions Size User   Date Modified Name
.rw-r--r--   50k sfmqrb 14 Oct 22:14  data/verification/page-52.json
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", 'notes': "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)"}

AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'notes': 'AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.'}

KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'notes': 'Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)'}

MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'notes': "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم\u200cها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100)."}

WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.", 'notes': 'Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Library of India scans on archive.org (open, OCR layer in the _text.pdf).'}
```


## [2026-10-16T05:13:23.200Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-518.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:5000])\"; cat tools/verify_check.py | head -80"
}
```


### [2026-10-16T05:13:23.592Z] TOOL RESULT

```
{
 "pdf_page": 518,
 "book_page": 488,
 "verified_by": "claude-opus-5.5",
 "verified_on": "2026-10-14",
 "entries": [
  {
   "entry": 0,
   "root": "Umm",
   "verdict": "confirmed",
   "modern_form": "Proto-Semitic *ʔimm- / *ʔumm- 'mother' (< Proto-Afroasiatic *ʔim-)",
   "note": "The Semitic 'mother' word is secure: Arabic umm (dial. imm), Hebrew ʾēm, Aramaic-Syriac ʾem, Ethiopic ʾem, Akkadian ummu, all < Proto-Semitic *ʔimm-/*ʔumm-. Root, label and gloss correct. The weak point of the chart is NOT the root but the Turkic branch (#3-#5): Klein (and Skeat) analyse begum as beg + Arabic umm 'mother of the bey', but Hobson-Jobson, Lokotsch, Webster, Mo'in and modern Wiktionary/AHD/Nişanyan take Eastern Turkic begim/begüm and xanım as beg/xan + Turkic suffix -im/-üm (1st-person possessive 'my lord', used as a feminine title), so the Arabic 'umm' there is a learned folk etymology. The Persian script for ommî's parenthetical is printed '(امّل)' in the book itself (an odd form, probably meant for a plural such as امّیّون/امّیّین); the extraction is faithful.",
   "note_fa": "واژهٔ «اُم» (مادر) از سامی آغازین *ʔimm-/*ʔumm- است و هم‌ریشه با عبری ʾēm، آرامی ʾem و اکدی ummu؛ پس ریشه و معنای آن درست است. اما شاخهٔ ترکی نمودار سست است: کلاین و اسکیت «بیگم» را ترکیبِ beg با «اُم» عربی («مادرِ بیگ») دانسته‌اند، ولی هابسن‌جابسن، لوکوچ، معین و پژوهش امروزی begim/begüm و xanım را از beg/xan با پسوند ترکیِ -im/-üm (ضمیر ملکی «ـَم»: «بیگِ من، خانِ من») می‌دانند و پیوند آن با «اُم» عربی را ریشه‌شناسی عامیانه می‌شمارند. ادعای نورایی دربارهٔ خود ریشه درست است، دربارهٔ بیگم و خانم با پژوهش امروزی سازگار نیست.",
   "sources": [
    "https://en.wiktionary.org/wiki/أم"
   ],
   "ref_check": [
    {
     "ref": "KLN:160",
     "status": "supports",
     "note": "KLN_1966.txt leaf 95 (pp. ~160-161), s.v. begum (line 4670): 'Turk., a hybrid coined fr. beg and Arab. umm, 'mother', ... The second element is rel. to Heb. em, Aram.-Syr. em, Ethiop. em, Akkad. ummu, 'mother''. Also s.v. aunt (line 3982): 'Arab. umm, imm, Ethiop. em, Akkad. ummu, 'mother''. Supports the Semitic root."
    }
   ],
   "consulted": [
    {
     "src": "FVQ",
     "where": "p. 85-86 fn. 3 (FVQ.txt line ~5633, grep 'Ummij')",
     "stance": "partial",
     "note": "Jeffery quotes Horovitz: Muhammad 'wendet öfter das dasselbe besagende Ummī an, welches ... die eigentliche arabische Übertragung von 'Am ha'arez darstellt' — treats umm/umma family as native Arabic; no comment on 'mother' itself."
    },
    {
     "src": "SKT",
     "where": "SKT.txt line 23803, s.v. Begum",
     "stance": "supports",
     "note": "'Pers. begam, a queen, lady of rank; lit. 'mother of the governor.' — Turk. beg, bey, governor; Arab. um, umm, mother.' Confirms umm 'mother'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Arabic",
     "words": "umm; umme-ğîlân",
     "verdict": "confirmed",
     "derivation": "Arabic أُمّ umm 'mother' is the inherited Semitic word (Proto-Semitic *ʔimm-/*ʔumm-, cf. Heb. ʾēm, Akk. ummu). أُمّ غَيْلان umm ghaylān, lit. 'mother of the ghūls' (ghaylān, pl. of ghūl 'desert demon'), is the classical Arabic name of the thorny desert acacia (Vachellia nilotica / gummifera); the name reflects the belief that ghouls haunt such thickets. 'Umm X' is a productive Arabic naming pattern for plants and animals ('possessor/abode of X').",
     "derivation_fa": "«اُمّ» در عربی همان واژهٔ موروثیِ سامی برای «مادر» است (سامی آغازین *ʔimm-، عبری ʾēm). «اُمّ غَیلان» یعنی «مادرِ غول‌ها» (غَیلان جمعِ غول) و نامِ درختچهٔ خاردار بیابانی، گونه‌ای اقاقیا (صمغ عربی)، است؛ عرب‌ها این خاربُن‌ها را جایگاه غولان می‌پنداشتند. الگوی «اُمّ + اسم» در عربی برای نام‌گذاری گیاهان و جانوران رایج است. ادعای نورایی درست است.",
     "sources": [
      "https://en.wiktionary.org/wiki/أم",
      "https://en.wiktionary.org/wiki/أم_غيلان"
     ],
     "ref_check": [
      {
       "ref": "KLN:160",
       "status": "partial",
       "note": "KLN_1966 leaf 95 s.v. begum: 'Arab. umm, 'mother' ... rel. to Heb. em, Aram.-Syr. em, Ethiop. em, Akkad. ummu' — supports umm; Klein has no entry for umm ghaylān (grep 'ghailan|ghaylan' silent)."
      }
     ],
     "consulted": [
      {
       "src": "SKT",
       "where": "line 23803 s.v. Begum",
       "stance": "supports",
       "note": "'Arab. um, umm, mother'."
      },
      {
       "src": "AFM",
       "where": "AFM.txt grep 'ام غیلان|أم غيلان'",
       "stance": "silent",
       "note": "Addi Shir lists Persian loans into Arabic; umm and umm ghaylān are native Arabic, not listed."
      },
      {
       "src": "MON",
       "where": "vajehyab.com/moein/مغیلان",
       "stance": "supports",
       "note": "'امُ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید' [ع.]"
      }
     ]
    },
    {
     "id": 2,
     "lang": "Persian",
     "words": "omm; ommî; moğîlân",
     "verdict": "plausible",
     "derivation": "omm أمّ (pl. ommahât أمّهات) is a learned Arabic loan in Persian, used beside native mâdar (e.g. omm-ol-ketâb). moğîlân مغیلان is
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
```


## [2026-10-16T05:13:25.254Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 80,200p tools/verify_check.py"
}
```


### [2026-10-16T05:13:25.557Z] TOOL RESULT

```
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


## [2026-10-16T05:13:29.604Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"lemma: (u̯edh|wedh|u̯eg|weg|u̯ok|wok|uok)\" POK_full.txt | head -30"
}
```


### [2026-10-16T05:13:29.890Z] TOOL RESULT

```
93217:Root / lemma: uokso- {*hauokso-)
```


## [2026-10-16T05:13:32.848Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^Root / lemma: .*(edh|eg-|eg\\b)\" POK_full.txt | grep -i -E \"u.?edh|u.?eg|ueg|uedh\" | head; sed -n 93217,93260p POK_full.txt"
}
```


### [2026-10-16T05:13:33.168Z] TOOL RESULT

```
7731:Root / lemma: aueg-, yog-, aug-, ug- 
29030:Root / lemma: eueg^h-i* huehueg^h-) 
83939:Root / lemma: sueng-, suenk- : sueg-, suek- {*g"heng- : ksueng-) 
88897:Root / lemma: ueg- 
89047:Root / lemma: ueg- 
89089:Root / lemma: ueg"- : ug"-, ulcs- 
91166:Root / lemma: uerg-2, ureg- {*hueig-2) 
93309:Root / lemma: ureg- (and uerg-1) {*hauerg-) 
93410:Root / lemma: ureg-, urog-, urag- {*hauerg^ 
Root / lemma: uokso- {*hauokso-) 
Meaning: wax 

Material: Old High German Old Saxon wahs. Old English weax. Old Icelandic vaxv\. ' wax 

'; Lithuanian vaskas, Latvian i/as/rsds.; russ. -Church Slavic (etc.) vosk-b6s.\ to *ueg-'to 

weave', as Old High German n/Si^a 'honeycomb' to *ueb^-^to weave', s. Tornquist, Studia 

Neophilol. 17, 99f. 

References: WP. I 315, Trautmann 343, Vasmer 1, 231. 

Page(s):1180 

Root / lemma: uortoko- {* hauortoko-) 



Meaning: quail 

Material: Old Indie vartaka-m., vartikai. " quail '; gr. opru^, -uyoc;, by Gramm. also -UKoq 

and with -u-, by Hes. yopru^, i.e. Fopru^ ' quail ', dessen ending after ipu^, paTpu^, -\jkoc,, 

KOKKu^, -uyo(; (and nrspu^, -uyot;?) transfigured is; Ionian 'Opruyin "Delos' 

CWachtelinsel'). 

References: WP. I 316. 

Page(s):1180 

Root / lemma: uoro- -a{*hauer-) 

Meaning: deceit; madness 

Material: Gr. cbpoKiav " senseless, unconscious become, erblassen' belongs to a stem 

cbpoK-; independent therefrom alts, n/o/'/g 'weakened, tired, faint, languid'. Old English 

werig, engl. weary^ tired ', Old High German wuorag' intoxicated, drunk '; the /r-derivative 

lacks in Old Icelandic 6rar\. PI. "Betaubtsein', 0rr{*udrio) "geistesgestort, baffle, furious '
```


## [2026-10-16T05:13:37.386Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88897,88920p POK_full.txt; sed -n 89047,89089p POK_full.txt; grep -n -E \"^Root / lemma: ued\" POK_full.txt"
}
```


### [2026-10-16T05:13:37.793Z] TOOL RESULT

```
Root / lemma: ueg- 
Meaning: to weave, bind 

Material: Old Indie i/5g^/'5"Fangstrick, net zum Wildfang, thread, string'; Latin velum^saW, 
sleeve, wrapping, kerchief, cloth, curtain' (therefrom velare^ veil, cover'), Demin. vexillum 
"banner, ensign, flag, Fahnchen'; Old Irish figim^ weave ', fige^\he weaving ', abret. gueig 
"textrix', nbret. gwea6s., acymr. ^^ee//ic "textilis', ncymr. ^n/e^ "to weave, tie, bind, knot', 
gwe{*uego-) " texture ', acorn. guiat<^\. "tela', ncorn. gwia\o weave'; Middle Irish indech, 
cymr. anwe' texture '; gall, veadia {*vegiadia) "Spinnwirtel' (J. Loth RC. 38, 86); 



Old English w/ce'\N'\ck\ Modern High German Bavarian w/chengarn'BaunwNoWeio 
Dochten', Norwegian v/'kt Titze or Docke thread, string' (diese and other /-forms through 
interference from ue/'k-, ueig- "bend, coil ' under S. 11 30, Persson Beitr. 323a 3?); Middle 
High German w/M'mck'; Old English wecca^\N\ck', Old Low German wekko. Middle Low 
German n/ec/re "wick, Lunte', Middle High German tv/ic/re "wick, Scharpie', Modern High 
German dial. wicke^\he um die spindle gewickelte Flachs', Old High German wickilT(n) 
"Wickel zum Abspinnen', Modern High German Wicker diS much, as jedesmals zum 
Abspinnen um den distaff (= staff for holding flax, wool, etc., in spinning) gewickelt wird'. 
Middle High German Modern High German wickein; o-grade Old English wocig^ loop, 
noose, snare, Fallstrick' (in ablaut and meaning genau to Old Indie va g u ra sWxrwneud); 
Norwegian dial, o/re "verfitzte mass, e.g. from Zwirn' (vonTorp 473 as "connection' to ok = 
/ugump\ace6, but probably with Aniautdehnung from *[i/v\dkan-); zero grade {*Ueg-or *ug- 
Root / lemma: ueg- 

Meaning: fresh, strong 

Grammatical information: stative verb uege- 

Material: Old Indie vaja- m. " power, quickness, contest, price of the battle, cut-throat price 

', vaJayati^reQi an, treibt an, lauft urn die Wette'; vajra-m. 'thunderbolt, club, mace, joint' = 

Avestan vazra- 'club, mace, joint'. Old pers. vazrka-, npers. buzurg^b\Q, large', derivative 

from *uazarn.; 

Latin veged, -ere 'bin alert, awake, smart', trans, 'errege', i//g//' watchful, wakeful' and 
'Wache, Wachter' {*vegilis), thereafter vigilare^ awake sein'; vegetus^ strenuous, alert, 
awake, smart'; 

Maybe from Latin ex v/g/7are der'wed Italian svegliare= alb. zgjoj^ wake up' (common alb. 
9l->9J-)- 

Alb. vigjeloj^ guard' a Latin loanword. 

Gothic gawaknan 'wake up, arouse' = Old Icelandic vakna ds., Old English wsecnan 
(preterit woe), waecnian' be born '; Old Icelandic vakinn' awake'; Kaus. Gothic uswakjan' 
awaken ' (besides the abbreviation = Old Indie vajayati) = Old Icelandic vekja, Old High 
German etc. wecchan 'waken, arouse, revive'; Zustandsverbum Germanic *waken\n: 
Gothic wakan. Old Icelandic vaka {schw. Verb) 'watch'. Old English wacian. Old Saxon 
wakon. Old High German wahhon, wahhen 'watch' Old High German wachal' awake'. 
Old English wacol{*wakala-). Old Icelandic vgkull{*wakula-: Latin vigil); Gothic wokainsi. 
'das Wachen'; Old Icelandic i/a/r/". Old English wacor. Old High German wachar, wakar' 
active, fresh, wackei* (formal = Old Indie vajra-, Avestan vazra-); Old Icelandic vaskr'a\ert, 
awake, smart, agile' {*vak-ska-); perhaps also Old High German waiis ' sharp' . 

Tocharian AB wasir' lightning '; 

References: WP. I 246 f., WH. II 741. 

See also: compare aueg- aug- above S. 84 f., from dem ueg- barely to separate is. 

Page(s): 1117-1118 

Root / lemma: ueg"- : ug"-, ulcs- 
88773:Root / lemma: ued^-l 
88893:Root / lemma: ued-
```


## [2026-10-16T05:13:39.821Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88730,88800p POK_full.txt; sed -n 88920,88935p POK_full.txt"
}
```


### [2026-10-16T05:13:40.169Z] TOOL RESULT

```
Tocharian B n/ap- 'to weave', wapatsa^ weaver', wpelme^ texture '. 

References: WP. I 257, Mayrhofer 1, 107; 

See also: belongs to au-S^io weave' S. 75; in addition "i/ob^sa 'wasp'. 

Page(s):1114 

Root / lemma: udcl^-2 

Meaning: to wander, roam, swarm 

Material: Middle High German weben^v(\QNQ, swing', weberen^ €\c\\ tummein', webelen 

'waver'. Modern High German East Prussian wibbeln; Middle High German waben, 

waberen, wabe/en^\n unsteter Bewegung sein', wappen'h\n and her schwanken'. Modern 

High German (Low German) M/5i6'i6'e//ig'wackelnd, e.g. from Gallertigem', Old English 

waf/an {esp. with handum) 'sich bewegen'. Middle English waveren, engl. M/ai/e/''wobble, 

waver'. Old Icelandic i/a/7a 'wobble, sway', vafra^s\dc\ unstet hin and back bewegen, 

wabern' (i/5/Wo^'Waberlohe'), vefjast6s.\ 

Old Icelandic i/a/^'schweben, dangle'. Old English wsefre^uusiei, flackernd'; 

Lithuanian vebzd-u, -e//"wimmeln, sich verwirren, durcheinander bewegen'; 

in addition Old High German wibilm. 'beetle, chafer, Kornwurm'; Old Saxon wivil. 
Middle Low German wevelAs., Old English M///fe/' Kornwurm', Old Icelandic V/Min tordyfiil 
'Mistkafer', Old English wibba^Ro^kaief; Lithuanian i/5i6'5/5S 'beetle, chafer', vabuolas 
ds., zem. i/5/?c»/e 'Mistkafer', Latvian i/ai7^c»//5 'beetle, chafer' (besides East Lithuanian dial. 
vobuolas^beeWe, chafer', zem. vambo/e, Latvian vambale, vambuole^U\s\kaief). 

References: WP. I 257 f., WH. II 733, Trautmann 336, Vasmer 1, 176; 



See also: moreover: ued- 
Page(s): 1114-1115 

Root / lemma: ued^-l 

Meaning: to push, hit 

Material: Old Indie vadhati, avadhTt^hW, bump, poke, destroy', Kaus. vadhayati, vadha-xx\. 

"killing, Mordwaffe (esp. from Indras projectile); blow, knock, annihilation ' = Avestan vada- 

m. "wedge zum Spaltendes Holzes', Old Indie vadhar-v\. "Mordwaffe (esp. from Indras 

projectile)' = Avestan vadar- n. "weapon (for hitting)', i/ao'/7/'a/77"Lederriemen', Old Indie 

vadhasna-m. ds., Avestan i/ad/a/a-'zuriJekstoften' (lengthened grade as gr. cbGsu)); 

gr. £0£i cpGEipei. spsGi^si Hes., hom. eGojv "pushing, thrusting, zerwijhlend', sGsipa " hair 
of the head, mane'; wGeu) "poke, push' (: Avestan vadaya-), wok; " shove ', evoaic; " tremor 
' ( *en-uo6!^-tis)\ also in svoaixGojv, £vvoaiYaiO(;, £ivoai(puAAo(; (svv-, £iv- metr. lengthening); 

Old Indie vadhri-^ castrated ' ("with zerstoftenen testicles') = gr. sGpic; Topiac;, Kpioc; 
Hes.; secondary iGpK;, aGpi(;; 

Lithuanian vedega^a kind of axe', Latvian vedga^EisayX, crowbar'. Old Prussian 
i4/eo''/gc»"Zimmerbeir, Old Irish /o^yi? "Waffenbeute' {*uo6'^-uo-)\ is also Avestan vadayan- 
"EN eines glaubensfeindlichen FiJrsten' as "axe, Schlager' to deuten? 

ein s/r-present seems Irish /^/sc- "press', mcymr. gwascu, bret. gwaska ^'^ress' (certainly 
ablaut d\d). 

/ugump\ace6, but probably with Aniautdehnung from *[i/v\dkan-); zero grade {*Ueg-or *ug- 
with takeover from M/-from den lengthened grade forms) Middle Low German wocke, 
i4/c»c/re/7 "distaff; flax or Wolle auf dem Rockenstock', Old Saxon M/occc»"cicindela (wick, 
Lunte)'; auf redupl. *ue-ug- based on probably Old English weoce. Middle Low German 
weke, weike. Old High German M//bc/7a"gedrehtes thread, string, Lunte', Modern High 
German dial. Wieche. 

References: WP. I 247 f., WH. II 745 f.; 
See also: here uokso- " wax '. 
Page(s):1117 

Root / lemma: uegh- 

Meaning: to move, carry, drive 

Note: a zero grade ugh- on\Y in Aryan and probably also in Alb.
```


## [2026-10-16T05:13:53.520Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(wedh|weg|wokso)\" AHD_watkins1985.txt; grep -n -E \"^(osmosis|osmose|wax|wick|veil|reveal|velum),\" KLN_1966.txt | head -20"
}
```


### [2026-10-16T05:13:53.896Z] TOOL RESULT

```
1121:weg:'
1129:wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
1130:weg-'. To weave a web. Related to wokso-. Suffixed
1131:weg-?
26677:osmose,  tr.  v.,  to  subject  to  osmosis;  intr.  v.,  to undergo  osmosis.  —  Back  formation  fr.  osmosis.
26678:osmosis,  n.,  intermixture  of  two  fluids  separated by  a  porous  membrane.  —  ModL.,  formed  with suff.  -osis  fr.  Gk.  coapms,  ‘a  thrusting,  impulse’, from  the  stem  of  w&siv,  ‘to  thrust,  push’,  which is  rel.  to  2v-oot?,  ‘shaking,  quake’,  fr.  I.-E.  base *wedh-,  ‘to  strike’,  whence  also  OI.  vadhati, ‘pushes,  strikes,  destroys’,  Avestic  vadaya-,  ‘to repulse’.
32671:reveal,  tr.  v.  —  ME.  revelen,  fr.  MF.  reveler  (F. reveler ),  fr.  OF.,  fr.  L.  revelare,  ‘to  uncover, disclose’,  lit.  ‘to  draw  back  the  veil’,  fr.  re-  and velum,  'a  veil’.  See  veil  and  cp.  revelation. Derivatives :  reveal,  n.,  reveal-er,  n.,  reveal-ment, n.
41184:velum,  n.,  the  soft  palate  (a not.)  ;  a  membranous covering  in  fungi,  in  the  jelly  fish,  etc.  ( hot .  and zool.)  _  L.  velum,  ‘sail;  piece  of  cloth;  awning, curtain,  veil’.  See  veil, velure,  n.  —  A  var.  of  velours  (q.v.) velvet,  n.  —  ME.  veluet,  velwet,  fr.  VL.  velluetum, fr.  *villutus,  ‘shaggy’,  fr.  L.  villus,  ‘shaggy  hair’. See  villus  and  cp.  velours,  velure.
```


## [2026-10-16T05:13:59.484Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1121,1140p AHD_watkins1985.txt; grep -n \"^wokso\" AHD_watkins1985.txt; grep -n -E \"^(veil|wax|wick)\" KLN_1966.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==563{print NR\": \"substr($0,1,300)}' KLN_1966.txt"
}
```


### [2026-10-16T05:13:59.934Z] TOOL RESULT

```
weg:'
(see koro-). 3. Suffixed extended o-grade form *wold-ti- in Russian oblast’, oblast: OBLAST. [Pok. wal- 1111.]
walso-. A post. 1. Latin vallus, post, stake, whence vallum, a palisade, wall: VALLATION, WALL; INTERVAL. 2. Greek hélos (< *hdlos < *walsos), stud, nail, wart: MYCELIUM. [In Pok. 7. yel- 1140.]
we-. We. For oblique cases of the pronoun see nes-2, Suffixed variant form *wei-es in Germanic *wiz in Old English wé, we, we: we. [Pok. ué- 1114.]
wé-. To blow. Contracted from “*wea-; oldest basic form *gwé- (< *owea-). 1. Suffixed irregular shortened form *we-dhro- in Germanic *wedram, wind, weather, in Old English weder, weather, storm, wind: WEATHER. 2. Suf- fixed (participial) form *wé-nt-o-, blowing, in: a. Ger- manic *windaz in (i) Old English wind, wind: wIND! (ii) Old Norse vindr, wind: wInpow; b. Latin ventus, wind: VENT, VENTAIL, VENTILATE. 3. Suffixed Germanic form *wé-ingjaz in Old Norse vengr, wing, akin to the Scandi- navian source of Middle English wenge, wing: WING. 4. Basic form *wé- in Sanskrit vdti (stem *vd-), he blows: NIRVANA. [Pok. 10. aw/é)- 81.]
webh-. To weave, also to move quickly. 1. Germanic *weban in Old English wefan, to weave: WEAVE, WOOF'. 2. Germanic *wefta- in Old English wefta, weft, cross thread: wert. 3. Suffixed o-grade form *wobh-yo- in Germanic *wabjam, fabric, web, in Old English webb), web: WEB, WEBSTER. 4. Suffixed Germanic form *webila- in Old English wifel, weevil (< “that which moves briskly”): WEEVIL. 5. Suffixed Germanic form *wabila-, web, honeycomb, in: a. Middle Low German wdfel, hon- eycomb, akin to the source of Old North French waufre, wafer: GOFFER, WAFER; b. obsolete Dutch waefel, honey- comb: WAFFLE}. 6. Possibly Germanic *wab-, to move back and forth as in weaving, in: a. Old English wafian, to move (the hand) up and down: WAVE; b. Low German wabbeln, to move from side to side, sway: WOBBLE. 7. Suffixed zero-grade form “ubh-d- in Greek huphé, web: HYPHA. [Pok. vebh- 1114.]
wed-'. Water; wet. 1. Suffixed o-grade form *wod-6r in Germanic *watar in Old English weter, water: WATER. 2. Suffixed lengthened-grade form *wéd-o- in Germanic *wéd- in Old English wt, wét, wet: WET. 3. O-grade form *wod- in Germanic suffixed form “wat-skan, to wash, in Old English wescan, wacsan, to wash: WASH. 4. Nasalized form *we-n-d- in Germanic *wintruz, win- ter, “wet season,” in Old English winter, winter: WINTER. 5. Suffixed zero-grade form *ud-d6r in Greek hudor, water: (HYDRANT), HYDRO-, (HYDROUS); ANHYDROUS, CLEPSYDRA, DROPSY, HYDATHODE, HYDATID. 6. Suffixed nasalized zero-grade form *u-n-d-d- in Latin unda, wave: UNDINE, UNDULATE; ABOUND, INUNDATE, (REDOUND), REDUNDANT, SURROUND. 7. Suffixed zero-grade form *ud-ro-, *ud-rd-, water animal, in: a. Germanic *otraz, otter, in Old English ofor, otter: OTTER; b. Latin Jutra, otter (with obscure /-): NUTRIA; C. Greek hudros, a water snake: Hyprus; d. Greek hudra, a water serpent, Hydra: Hypra. 8. Suffixed zero-grade form *ud-skio- in Scottish and Irish Gaelic uisge, water: USQUEBAUGH, (WHISKEY). 9. Suffixed o-grade form *wod-d- in Russian voda, water: VODKA. [Pok. 9. au(e)- 78.]
wed-2, To speak. 1. Possibly oldest root form *awed- becoming *awed- in reduplicated form *awe-ud- dissimi- lated to *aweid-, with suffixed o-grade form *awoid-o- respectively in Greek aeidein (Attic aidein), to sing, and aoidé (Attic didé), song, ode (but more likely a separate root *aweid- becoming Greek *aweid-, to sing): ODE; COMEDY, EPODE, HYMNODY, MELODY, MONODY, PARODY, RHAPSODY, TRAGEDY. 2. Sanskrit vddah, sound, state- ment: THERAVADA. [Pok. 6. au- 76.]
wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
weg-'. To weave a web. Related to wokso-. Suffixed
weg-?
form *weg-slo- in Latin vélum, a sail, curtain, veil: VEIL, VELUM, VEXILLUM, VOILE; REVEAL. [Pok. weg- 1117.] weg-2. To be strong, be lively. 1. Suffixed o-grade form *wog-é- in Germanic *wakén in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE}. 2. Suf- fixed o-grade form *wog-no- in Germanic *waknan in Old English wecnan, wecnian, to awake: WAKEN. 3. Germanic *wakjan in Old English weccan, to be awake: WATCH. 4. Germanic *wahtwo in Old High Ger- man wahta, watch, vigil, in dialectal German beiwacht, supplementary night watch: BIvouac. 5. Germanic *waht- in: a. Old North French waitier, to watch: WAIT; b. Middle Low German wachten, to watch, guard: WAFT. 6. Suffixed (causative) o-grade form *wog-eyo- in Latin vegére, to be lively: VEGETABLE. 7. Suffixed (stative) form *weg-é- in Latin vigére, to be lively: vicor. 8. Suf- fixed form *weg-eli- in Latin vigil, watchful, awake (> vigilare, to watch, be awake): VEDETTE, VIGIL, (VIGI- LANT), VIGILANTE; REVEILLE, SURVEILLANT. 9. Suffixed form *weg-slo- in Latin véldx, fast, “lively”: VELOCITY. [Pok. weg- 1117.] wegh-. To go, transport in a vehicle. 1. Germanic *wegan in Old English wegan, to carry, balance in a scale: WEIGH}. 2. Germanic lengthened form *wég-6 in Old English wég(e), weight, unit of weight: WEE. 3. Suffixed form *wegh-ti- in Germanic *wihti- in Old English wiht, gewiht, weight: WEIGHT. 4. Germanic *wegaz, course of travel, way, in Old English weg, way: WAY; ALWAYS, (Away). 5. Suffixed form *wogh-no- in Germanic *wag- naz, vehicle, in: a. Old English we(g)n, wagon: WAIN; b. Middle Dutch wagen, wagon: WAGON. 6. Suffixed o-grade form *wogh-lo- in: a. Germanic *waglaz in Old Norse vagl, chicken roost, perch, beam: WALLEYED; b. Greek okhlos, populace, mob (< “moving mass’): OCHLOCRACY, OCHLOPHOBIA. 7. Distantly related to this root are: a. Germanic *wag-, “to move about,” in (i) possibly Middle English waggen, to wag: wac! (ii) Old High German waggo, wacko, boulder rolling on a river- bed (> German Wacke, boulder): GRAYWACKE; b. Ger- manic *wéga-, water in motion, in Old Italian vogare, to row: VOGUE; c. Germanic *wig- in (i) Old English wicga, insect (< “thing that moves quickly”): EARWIG (ii) Middle Dutch and Middle Low German wiggelen, to move back and forth, wag: WIGGLE. 8. Basic form *wegh- in Latin vehere (past participle vectus), to carry: VECTOR, VEHICLE; ADVECTION, CONVECTION, EVECTION, INVEIGH. 9. Suffixed basic form *wegh-yd in Latin via, way, road: FOY, VIA, VOYAGE; CONVEY, DEVIATE, DEVIOUS, (ENVOI), ENVOY!, OBVIOUS, PERVIOUS, PREVIOUS, (TRIVIAL), TRIV- IUM, (vIADUCT). 10. Suffixed form *wegh-s- in Latin vexdre, to agitate (< “to set in motion”): VEX. 11. Prob- ably suffixed form *wegh-so- in Latin convexus, “carried or drawn together (to a point),” convex (com-, together; see kom): CONVEX. [Pok. vegh- 1118.] weg-. Wet. 1. Germanic *wakw-6 in Old Norse vdk, a crack in ice (< “wet spot’): WAKE?. 2. Suffixed zero-grade form *ug’-sm- in: a. Latin (hjiimére, to be wet: HUMECTANT, HUMID; b. Latin (hj)iimor, fluid: HU- mor. 3. Suffixed zero-grade form *ug’-ro- in Greek hugros, wet, liquid: HYGRO-. 4. Regarded by some as an extended form of this root (with the meaning “the impregnator”), but probably a distinct Indo-European word, is *uk”s-en-, bull, ox, in Germanic *uhs6dn- in: a. Old English oxa, ox: 0x; b. Old High German ohso, ox, in German Aurochs, aurochs: AUROCHS. [Pok. uweg#- 1118.] weg”h-, Also eug’h-. To preach, speak solemnly. Suf- fixed o-grade form *wog’h-eyo- in Latin vovére, to pledge, vow: VOTARY, VOTE, (VOTIVE), VOW; DEVOTE, (DEvouT). [Pok. ewegvh- 348.] wei-'. Also weie-. To turn, twist; with derivatives refer- ring to suppleness or binding. I. Form *wei-. 1. Germanic suffixed form *wi-ra-, *wé-ra- in Old English wir, wire: WIRE. 2. Probably suffixed Germanic form *wai-ra- in
74
weia-
Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
weik-'
derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
75
wel-3
for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
563:   niter, nitro,  adj.,  containing  nitrogen.  —  From  nitro-.
nitrogen,  n.,  a  colorless,  tastless,  odorless  gase¬ ous  chemical  element.  —  F.  nitrog&ne,  coined by  the  French  chemist  Jean-Antoine  Chaptal (1756-1832)  in  1790  fr.  nitro-  and  suff.  -gene  (fr. Gk.  -Y£v%,  ‘born
```


## [2026-10-16T05:14:04.523Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \"wokso-\\..{0,300}\" AHD_watkins1985.txt | head; grep -n -E \"^(wax|wick|veil)[0-9]*,? \" KLN_1966.txt | head; grep -n -E \"osmosis|osmose\" KLN_1966.txt | head -3"
}
```


### [2026-10-16T05:14:05.061Z] TOOL RESULT

```
1130:wokso-. Suffixed
1172:wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you
13135:endosmosis,  n.,  inward  osmosis  (physiol.)  — Compounded  of  end-  and  osmosis.  Cp.  exos¬ mosis.
14063:exordium,  n.,  beginning.  —  L.  exordium,  ‘begin¬ ning  of  a  web,  beginning  of  a  speech,  beginning (in  general)’  fr.  exordiri,  ‘to  lay  the  warp,  begin a  web,  begin’,  fr.  1st  ex-  and  ordiri,  ‘to  lay  a warp,  begin’,  which  is  rel.  to  or  do,  ‘a  straight row,  order’.  See  order  and  cp.  ornament, exoskeleton,  n.,  the  skeleton  of  invertebrates  in contradistinction  to  the  skeleton  of  vertebrates (zoo/.)  —  Compounded  of  exo-  and  skeleton. The  term  exoskeleton  was  introduced  into  science by  the  English  anatomist  Sir  Richard  Owen (1804-92).  Cp.  endoskeleton,  splanchnoskeleton. Derivative:  exoskelet-al,  adj. exosmosis,  also  exosmose,  n.,  outward  osmosis. —  Compounded  of  3rd  ex-  and  osmosis.  Cp. end  osmosis.
26674:Derivatives:  osm-ic,  osmi-ous,  adjs. osmo-,  before  a  vowel  osm-,  combining  form meaning  ‘smell,  odor’,  as  in  Osmorhiza.  —  Gk. 6ap.o-,  fr.  oap.y],  ‘odor’.  See  osmium, osmo-,  combining  form  for  osmosis  or  osmotic,  as in  osmology,  osmometer.  —  See  osmosis. Osmond,  masc.  PN.  —  OE.  Osmund,  lit.  ’divine protection’,  compounded  of  os,  ‘a  god’,  and mund,  ‘protection’.  For  the  first  element  see Oscar  and  cp.  Oswald.  The  second  element  is rel.  to  ON.  mund,  OHG.  munt,  ‘hand,  protec¬ tion’,  and  cogn.  with  L.  manus,  ‘hand’.  See manual  and  cp.  mound,  ‘heap  of  earth’.  Cp.  also the  second  element  in  Edmond,  Raymond,  Si- gismund.
```


## [2026-10-16T05:14:10.211Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; leaf(){ head -n $1 KLN_1966.txt | tr -cd '\\f' | wc -c; }; echo osmosis $(leaf 26678) reveal $(leaf 32671) velum $(leaf 41184); grep -n -E \"^\\s*(veil|wax|wick)[0-9 ]*,  ?(n|v)\" KLN_1966.txt | head; grep -n -E \"^(wax|veil|wick)\" KLN_1966.txt | head"
}
```


### [2026-10-16T05:14:10.741Z] TOOL RESULT

```
osmosis 588 reveal 713 velum 899
```


## [2026-10-16T05:14:17.842Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 589 900; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -o -E \"\\b1[0-9]{3}\\b\" | head -5; echo --; done; grep -n -i -E \"^ *(wax|veil|wick)[0-9¹²]*,\" KLN_1966.txt | head; grep -n -E \"wax[0-9¹]?,  n\" KLN_1966.txt | head"
}
```


### [2026-10-16T05:14:18.309Z] TOOL RESULT

```
1259
1326
1761
1815
1803
--
1696
1793
--
27757:Derivatives:  paxill-ar,  paxill-ate,  adjs. paxwax,  n.,  the  nuchal  ligament  of  mammals.  — - ME.,  dissimilated  fr.  ME.  faxwax,  which  is prob.  a  compound  of  fax,  ‘hair’  (fr.  OE.  feax), and  wax,  ‘growth’  (fr.  waxen,  ‘to  grow’).  The first  element  is  rel.  to  ON.  fax,  ‘mane’,  OHG. fahs,  ‘hair’,  and  to  ON./a?r(for  *faheza),  ‘sheep’, fr.  I.-E.  base  *pek-,  ‘to  pluck  (wool  or  hair)’, whence  also  Gk.  mjxos,  ‘fleece’,  L.pecus,  ‘cattle, flock’,  pexus,  ‘woolly’,  pecten,  ‘comb’.  See  fee, ‘cattle,  money’,  and  cp.  words  there  referred  to. For  the  second  element  see  wax,  ‘to  grow’, pay,  tr.  and  intr.  v.,  to  requite,  reward  —  ME. paten,  payen,  fr.  OF.  paier,  paer  (F.  payer),  fr. L.  pacare,  ‘to  pacify,  appease’,  in  VL.  also  ‘to pay’,  fr.  pax,  gen.  pads,  ‘peace’.  See  pact  and  cp. peace.
41170:vehmgericht,  n.,  in  medieval  Germany,  a  kind  of secret  tribunal.  —  G.  Femgericht,  compounded of  Vehme,  Feme,  ‘secret  tribunal’,  which  is  rel. to  M H G .  veime,  MDu.  veme,  veem,  Du.  veem, of  js.m.,  and  Gericht,  ‘judgment,  court  of  jus- tic?’,  which  derives  fr.  MHG.  gerihte,  fr.  OHG. ginhti,  fr.  rihten,  ‘to  judge’,  which  is  rel.  to OHG.,  MHG.  reht,  ‘right’.  See  right,  adj. vebmic,  adj.,  pertaining  to  the  vehmgericht.  — See  prec.  word  and  adj.  suff.  -ic. veil,  n.  —  ME.  veile,  fr.  OF.  veile  (F.  voile),  fr.  L. vela,  pi.  of  velum,  ‘sail;  piece  of  cloth;  awning, curtain,  veil’,  but  in  VL.  mistaken  for  a  fem. sing.  noun.  L.  velum  prob.  stands  for  *wexlom (cp.  vexillum,  ‘banner,  flag’,  the  dimin.  of  velum), fr,  I.-E.  base  *t veg-,  ‘to  weave’,  whence  also  OE. weoce,  weoc,  ‘wick’.  See  wick  and  cp.  wax,  n. Cp.  also  velamen,  velar,  velic,  velum,  voile,  re¬ veal,  revelation.
```


## [2026-10-16T05:14:25.087Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 588 589 590; do echo \"== $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -n -o -E \"(^|[^0-9.,])1[01][0-9]{2}([^0-9]|$)\" | head -5; done; grep -n -E \"wax,  n\\.|wick,  n\\.|wax,  (intr|tr)\" KLN_1966.txt | head"
}
```


### [2026-10-16T05:14:25.533Z] TOOL RESULT

```
== 588
== 589
== 590
19:1103
4293:bailiwick,  n.,  the  district  of  a  bailiff.  —  ME. baillifwik,  compounded  of  baillif  (see  prec. word)  and  wick,  ‘village’, baillone,  adj.,  holding  a  staff  in  the  mouth  (her.) —  F.  batllonne,  lit.  ‘gagged’,  pp.  of  bdillonner, ‘to  gag’,  fr.  bdiller,  ‘to  gape,  yawn’,  fr.  VL.  bata- culare,  fr.  batdre,  ‘to  gape,  yawn’.  Cp.  OProv- eng.  badalhar,  It.  badigliare,  sbadigliare,  ‘to
27757:Derivatives:  paxill-ar,  paxill-ate,  adjs. paxwax,  n.,  the  nuchal  ligament  of  mammals.  — - ME.,  dissimilated  fr.  ME.  faxwax,  which  is prob.  a  compound  of  fax,  ‘hair’  (fr.  OE.  feax), and  wax,  ‘growth’  (fr.  waxen,  ‘to  grow’).  The first  element  is  rel.  to  ON.  fax,  ‘mane’,  OHG. fahs,  ‘hair’,  and  to  ON./a?r(for  *faheza),  ‘sheep’, fr.  I.-E.  base  *pek-,  ‘to  pluck  (wool  or  hair)’, whence  also  Gk.  mjxos,  ‘fleece’,  L.pecus,  ‘cattle, flock’,  pexus,  ‘woolly’,  pecten,  ‘comb’.  See  fee, ‘cattle,  money’,  and  cp.  words  there  referred  to. For  the  second  element  see  wax,  ‘to  grow’, pay,  tr.  and  intr.  v.,  to  requite,  reward  —  ME. paten,  payen,  fr.  OF.  paier,  paer  (F.  payer),  fr. L.  pacare,  ‘to  pacify,  appease’,  in  VL.  also  ‘to pay’,  fr.  pax,  gen.  pads,  ‘peace’.  See  pact  and  cp. peace.
41170:vehmgericht,  n.,  in  medieval  Germany,  a  kind  of secret  tribunal.  —  G.  Femgericht,  compounded of  Vehme,  Feme,  ‘secret  tribunal’,  which  is  rel. to  M H G .  veime,  MDu.  veme,  veem,  Du.  veem, of  js.m.,  and  Gericht,  ‘judgment,  court  of  jus- tic?’,  which  derives  fr.  MHG.  gerihte,  fr.  OHG. ginhti,  fr.  rihten,  ‘to  judge’,  which  is  rel.  to OHG.,  MHG.  reht,  ‘right’.  See  right,  adj. vebmic,  adj.,  pertaining  to  the  vehmgericht.  — See  prec.  word  and  adj.  suff.  -ic. veil,  n.  —  ME.  veile,  fr.  OF.  veile  (F.  voile),  fr.  L. vela,  pi.  of  velum,  ‘sail;  piece  of  cloth;  awning, curtain,  veil’,  but  in  VL.  mistaken  for  a  fem. sing.  noun.  L.  velum  prob.  stands  for  *wexlom (cp.  vexillum,  ‘banner,  flag’,  the  dimin.  of  velum), fr,  I.-E.  base  *t veg-,  ‘to  weave’,  whence  also  OE. weoce,  weoc,  ‘wick’.  See  wick  and  cp.  wax,  n. Cp.  also  velamen,  velar,  velic,  velum,  voile,  re¬ veal,  revelation.
```


## [2026-10-16T05:14:29.557Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \"(^| )(wax|wick)[0-9]?,  ?(n|v)[^—]{0,10}—.{0,400}\" KLN_1966.txt | head -5; grep -n -o -E \"wahs.{0,200}\" KLN_1966.txt | head -3"
}
```


### [2026-10-16T05:14:29.952Z] TOOL RESULT

```
3936:wahsjan,  OE. weaxan,  ‘to  grow’.  See  wax,  v.,  and  cp.  auxiliary, auxano-,  auxesis,  auxetic,  auxo-.
```


## [2026-10-16T05:14:33.231Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \"(wax|wick)[0-9]?, n\\..{0,400}\" KLN_1971.txt | head -4; echo ===SKT; grep -n -E \"^(Wax|Wick|Veil|Reveal|Osmosis)\" SKT.txt | head"
}
```


### [2026-10-16T05:14:33.767Z] TOOL RESULT

```
Exit code 1
24934:wick, n., the district of a bailiff. — ME. 
175998:wax, n., the nuchal ligament of mammals. — 
259887:wax, n. 
265416:wax, n., beeswax. — ME. wax , fr. OE. weax, rel. to 
(eval):1: ==SKT not found
```


## [2026-10-16T05:14:36.676Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 265416,265432p KLN_1971.txt; grep -n -E \"^wick, n\\.\" KLN_1971.txt; grep -n -E \"^(WAX|WICK|VEIL|REVEAL|OSMOSIS|Wax|Wick|Veil)\\b\" SKT.txt | head"
}
```


## [2026-10-16T05:14:37.972Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^ *(wax|wick|veil|reveal)[ ,(1]\" SKT.txt | head; grep -n -i \"osmos\" SKT.txt FSD_vol3.txt | head -3"
}
```


### [2026-10-16T05:14:38.332Z] TOOL RESULT

```
wax, n., beeswax. — ME. wax , fr. OE. weax, rel. to 
OS., OHG., MHG. wahs , ON., Swed. vax, Dan. 
voks, Du. was, G. Wachs , and cogn. with OSlav. 
vosku, Lith. vaskas, Lett, vasks, Pol. wosk, 
Russ., Czech, Slovak vosk , ‘wax’. All these 
words are derivatives of I.-E. base *weg-, ‘to 
weave’, and lit. ‘mean that which is woven (by 
the bees)’. See wick and cp. veil, n. 

Derivatives: wax, tr. v., to cover with wax, wax- 
en, adj., waxy (q.v.) 

wax, intr. v., to grow. — ME. waxan, fr. OE. 
weaxan , ‘to grow’, rel. to OS., OHG. wahsan, 
ON. vaxa, Swed. vaxa, Dan. vokse, OFris. wax a, 
Du. wassen , MHG. wahsen, G. wachsen , Goth. 
wahsjan , ‘to grow’, fr. I.-E. base *aw(e)ks-, 
267003:wick, n., twisted thread. — ME. wicke, wike, fr. 
267015:wick, n., village (now found only in compounds). 
21244:Wax  (1),  to  grow,  (U,^    M.U,  waxen, pi.  L  j/vjT,  wex,  pp.  waxen,  waxen.     K.i> tMOJrats,    pt    L    utix,    pp.    ^tuwoxen.  ^\  ^«i«vwx.  Ot-\     "^ -"^ « t}Q.  twz//i#,  Icel.  ws*a.l5an.  w«ct.  S^t&Awij«i  *  ^t*v».\\>^
21249:Wax  (3),  a  substance  made  by  bees. (E.)  M.  E.  wfljr:  A.  S.  a««tx.+Do.  v^. Icel.  Swed.  vox,  Dan.  uur,  G.  waehs.  Raft vosk\  Lith.  wankai.
21428:WICK.
21444:WICK.
```


### [2026-10-16T05:14:38.340Z] TOOL RESULT

```
3257:wax,  +  Gk.  *v^'  ^''*
16020:Reveal :  see  Vehicle.
20649:veiL  ^  I«  r«s  back;  mUum,  tciJ;   see
20659:veil,  lb.  (F.  -  L.)  O.  F.  veiU,  later ili.  —  L.  91^/itm,  a  sail ;  also  a  cloth.  Lit jropeller '  of  a  ship ;  from  uiAin,  to  carry
21244:Wax  (1),  to  grow,  (U,^    M.U,  waxen, pi.  L  j/vjT,  wex,  pp.  waxen,  waxen.     K.i> tMOJrats,    pt    L    utix,    pp.    ^tuwoxen.  ^\  ^«i«vwx.  Ot-\     "^ -"^ « t}Q.  twz//i#,  Icel.  ws*a.l5an.  w«ct.  S^t&Awij«i  *  ^t*v».\\>^
21249:Wax  (3),  a  substance  made  by  bees. (E.)  M.  E.  wfljr:  A.  S.  a««tx.+Do.  v^. Icel.  Swed.  vox,  Dan.  uur,  G.  waehs.  Raft vosk\  Lith.  wankai.
FSD_vol3.txt:1516:!• The great world; the universe or cosmos exterior to
FSD_vol3.txt:36768:experiments on osmose — iiil'cro-iner"al, a Ot or per-
FSD_vol3.txt:104421:sure, pressure due to or considered as oaiislng osmose, ospe-
```


## [2026-10-16T05:14:41.378Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 20659,20661p SKT.txt; sed -n 21428,21450p SKT.txt; sed -n 267003,267012p KLN_1971.txt"
}
```


### [2026-10-16T05:14:41.685Z] TOOL RESULT

```
veil,  lb.  (F.  -  L.)  O.  F.  veiU,  later ili.  —  L.  91^/itm,  a  sail ;  also  a  cloth.  Lit jropeller '  of  a  ship ;  from  uiAin,  to  carry
Ollg.
vein.  (F.-L.)  F.  wiwr.-L.  uina,  a in.  Lit,  'conveyer'  of  the  blood.  — L. hertt  to  carry.
WICK.
5«i
(BarboDr).  A.  S.  Avrilc,  hwtk,  which ; short  for  kw/Z/e,  lit.  'why-lilte,'  i.e.  how like,  in  what  way  lifce.  — A.  S.  Aw/,  how, instrumental  case  of  AwA,  who;  l/c,  like; see  Why  and  Like.  +  O.  Sax.  Atfilik, O.  Fries.  Awt/iA,  Du,  ««i!*,  Icel.  Av/l/kr, Dan.  Swed.  AvilJten,  G.  wd<Atr,  O.  H.  G. hwtlik.     Cf.  L.  qualit,
whither.  (E.)  M.  E.  wA»dW-.  A.  S. Avfider,  AwatUr,  whither,  -f  Goth.  Awtn/rt, Cf.  AiM/r,  /Ai/^^r.
why.  (.E.)  M.  E.  wAix  for  ufAi=  oa what  accoant  (common).  A.  S.  Axo/,  in what  way,  instrtimental  case  of  Awd,  who; see  Who  (abo\'e).
Whole;  see  Hale  (i).
Whoop,  to  shout.  (F.  -  Teui.)  The initial  w  is  unoriginal;  fonnerly  Aivfi. M.  E.  Aau/fH.  —  F.  Aou^cr,  'to  hoop unto;*  Cot.  Of  Teut.  ongiu ;  cf.  Goth. Aloof  jan,  to  boast  I  Romans  ix.  8).  Der. tuhooping-taugh  or  hooping'CougA.
hubbub.  vF.-Tcut.)  Formerly  also wAoebub,  a  confused  Dolse.  HubkuA  - AooP'Aoop,  reduplication  of  Aoop.  WAoodub » tukoop-Aoop.
Whore,  sb,  (Scand.)  The  w  is  unori- ginal.  M.  E.  ^i»r¥.  — Iccl.  Aira,  an  adul* teress,  fern,  of  A6rr,  an  adulterer;  Dan. Aort,  Swed,  Aom.  -+•  t)u,  Aoer,  G.  Aurt, O.  H.  G.  Aucra;  Goth.  Acn,  masc.  an adulterer.  Allied  to  Polish  Auram,  Church- Slavonic  kurttva,  an  aduttereaa.  Prob. also  to  L.  rarMT,  loving,  Skt.  kdmaga,  a lascivious  woman  (from  /tarn,  to  love). ^[Certainly  not  allied  to  hire  I
WhorL  ^E.)  The  same  as  wAar!,  %■ piece  of  bone  placed  on  a  spindle  to  twist It  by.  The  likenciis  between  a  wAarl  on  a spindle  and  a  wAori  of  leaves  is  sufhcietttly cioM.  Contraction  of  M,  £,  wAarvtl, whorvil;  from  A.  S.  Aweor/a,  a  wharl.— A.  S.  Autor/an,  to  turn ;  see  Wharf, Whirl.  +  O.  Du.  worvet,  a  whari; tvorvflen,  to  twist  or  twine.
Why;  see  Who.
WI-WY.
\  a  twtst  of  threads  for  a  tamp. L  -utiei:*,  weyke,  ivtteAe.  A.  S. rick.  +  O  Du  wwAe  ;  Low  G i  Din.  f&Y.  Swed.  vfAt,  a  wick. '-  'pliant^  or  'soft;'  allied  to A.  S.  «e^.  weak,  and  ttft^a  ( • wtck.  ve  both  ftom  tt/u-m,  pp.
of  v/ifOH,  to  give  way.  Cf.  O.  Du.  weirkt soft,  Dan.  v£g,  pliant,  Norw.  vt'A,  a  bend, a  skein  of  thread,  Swed.  vtA.  soft,  wkna,  to soften,  G.  weuA,  soft,  pliant.  Hence  the senK  is  'a  bit  of  soft  stuff,'  soch  as  Unt,
Wlok    (J),   a   town.    ^U)    A.S.  tnkN
56a
WICK.
borrowed  from  L.  »;Vhj,  a  Tillage.    Se« Vicinity.
Wlok  is),  Wioh,  a  creek,  bay.  &alc-piL (Scand.)  icel.  r/<(,  a  small  creek,  inlet, bay ;  see  Vikinjp-
"Wicked;  see  Wit  fi).
Wicker,  made  of  twigs.  (E.  tfr  Scand.) M.  E.  wiktr,  a  pliant  twig,  properly  a  sb. —  A.S.  wic-en,  pp.  of  wuan.  to  give  way, bend,  ply  ;  see  Weak,  -f  Dan.  dial.  z>igref a  phant  lod,  allied  to  Dan.  veg,  pliant, weak ;  Swcd.  dial,  evidnr,  vtAker,  willow, from  Swcd.  vekiL,  to  bend,  ply.  See wit-chelxn  (below).
wicket,  a  small  gate.  (F.  -  Scand.) M.  E.  ttfii£t.  — O.  F.  wiht*  (the  right  form), also  written  witiet  (with  intrusive  j)  and vi(juet\  mod.  Y.guichet;  Walloon  mV/i^/. Fonned,  with  F.  dimin.  sufTia  -r/,  from Icel-  vik-inn.  pp.  of  the  strong  verb  vlkja, to  move,  turn,  veer.  Qi.  Swcd.  t/k-iix,  to uag,  vika^  to  turn  away,  K.  S.  wkan^  to give  way.  Lit.  *  a  small  thinj;  that  easily tarns;*  esp.  used  of  a  small  door,  easily opened,  made  within  a  large  gate.  Ser. wicket  (at  cricket),  which  was  at  first  '  a small  gate,'  being  made  a  feet  wide  by  l foot  high  (a.d.  1 700).
witch-elm.  wych-elm.  (E.)  M.  E. wicht.  A.  S.  wice.  The  sense  is  •bcnd- iog.'  or  drooping;  from  the  pendulous branches.  — A.  S.  wUnn,  pp.  of  w/om,  to bend ;  see  Wicker.
wick, n., twisted thread. — ME. wicke, wike, fr. 
OE. weoce, ‘wick’, rel. to MDu. wieke, Du. wiek, 
OHG. wiohha, MHG., G. wieche , fr. I.-E. base 
*weg-, ‘to weave’, whence also L. velum (for 



WIELD 

*wexlom), ‘sail, curtain, veil’. See veil, n., and
```


## [2026-10-16T05:14:48.136Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"vadar|vaδar|vādaya|vadaya|vaδaya|vaδaγan|vadağan|vadaγan\" BRT.txt | head -20"
}
```


### [2026-10-16T05:14:48.435Z] TOOL RESULT

```
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
18759:. .   vadar»  (s '
21203:—  aitatahqm  urvaranqm  y  IUn.H^ranqm Y.  Ä  7  5 ;  —  aSaesqm  y  daxmanqm  V.  7. 51;  Yt_5.  9, 13; —  aäanhqm  y  myazda- nqm  N.  ^2.  Anhang.  Auftallig  ist  die Wortfolge  (zu  c):  daiiikanqmcli  aidyünam hyat  urunayazamaidfY.3g,3*'>.  2)oluie erkennbare  Bedeutung;  A)imgAw.;a)vor clt  in  ya-  hyalclt  'quicunque'  (Sp.  593  u., 1230  u.):  yä  mazdd^a  (sd.)  hyatüt}^  vt- du!iY.30.\.  b)  vor  cä:  däröi  ahvä astvatascä  hyaicä^l  mananhS  ayapta(sd.) "vitarum  et  (vitae)  corporeae  et  (vitae) animi  fclicitatcs"  Y.  2Ä3;  —  varp^aitl  .. ratui  syaoianS  razistä  (sd.)  drigvataüä hyaicä^'^  *asaom  yehyaca  hsm>myasaill (sd.)  . .  Y.33. 1.  c)  zur  Einleitung  einer Aufforderung:  hy^  höi  hudsmSm  (sd.)  dyäi vax)lrahya  Y.2g.B.  b)  im  jA^p.;  zur Einleitung  der  Antwort:  kva paoirJm  aiiihä zsniB  asailtimi  ..  y^  arpzürahe  grivaya V.J.  7;  —  zur  Einleitung  des  Refrains: paiti  /ahikayai . .  kthrpjm  näämnäi  asaone . .  vadar»  jatäi  y'^^  hl  k»hrppm  . .  vadar> jaiii  Y.5.  33;—  sonst:  bval  vispB  ankul astvä  *azar>s5 ..  daryypm  _y'"  yave  vispai F._3  h;  —  daiiihSul  dairihupaUlm  bisatyai vähm  .  .  anjB  y'i'>  paoirlm  nmana/ie nmänäpaitlm  näirikqm  bHasyät  ka'hioa daSnu  arsjB  V.  7.  41  f.;  —  vTtasti.dra/s y'fi huSkanqm  (sd.)  .  .  aiiihS  s»mB  mdat^yqn V.  7.  29;  29f.3,  33  f.*;  —  das?mB  y  ahmi spanB  alvandasö  spanaauha  .  ,  lutvadasa y    ahmi   data   visqstPmB   ahmi  y    ahmi
22418:vadar-
22422:•  j.,  g.  vadar-  n.  'Waffe  (zum  Schlagen)': yasla  'dar!  vSisdai  aläuns  "und  der  die Waffe  wider  den  Rechtgläubigen  erhebt" Y._j2.  lo;  —  paifi  .  .  kihrpim  .  .  haoma . .  'dar}  /ai\i^'>  "gegen  den . .  Leib  schlag . . die  Waffe"  Y.o.  30;  30—32*,
23785:mit  asti  (Sp.  a  7 1  m.)  sva.  'er  ist  die  Freude  j  '(eine  Waffe)  erheben  gegen  Jemanden' des  .  .'  (Gen.):  äiar/  V  matää  ahurahya  \  (Dat.):  yasca  vadarS  (sd.)  vHidai  asäunt aht  mainyui  v   ahyä   spSnistö  ahl  "alsjY-52.  i-
```


## [2026-10-16T05:14:51.158Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22405,22425p BRT.txt | cut -c1-600; grep -n -E \"^\\s*\\*?vad[aä]\" BRT.txt | head -20"
}
```


### [2026-10-16T05:14:51.573Z] TOOL RESULT

```
V.Ä16.
PDs.  du'v'tiata  'ich  bringe  hinein',  ar^.  rä- vali 'er  bringt';  ksL  vaiq,  liLiin/ü  'ich  fahre, heirate'.  S.  noch  ZuBATif  ASlPh.  l6.  104.  — Fü. :  väitnltan,  zu  V.  4  erL :  bii  lau  l  dafund^ (lu  V.  18]'.  frarämenUan.  —  ')  Das  zweite Praer.  wiederholt;  a,  V.  8.  16.  Pü.  an  1^  n ist  undeutlich.
•  j.  vada-  m.  'Keil'  zum  Spalten  des Holzes":  'dtm  titiMrim  tiiiJnüttm  V. 14.  7.
Vgl,  vadoT'.  —  ai.  vadhä-  m.  von  Indrat  Ge- EchosE.   —   Pü.:   kartinak  (Tgl.  tärt  'Messer*) □der  kultnak  (vgl.  np.  kudina  'Hammer')?  — 0  VgL  därv  .  .  äpävadlüi  RV.  10.  146.  4. j.  viAcürttyoi,  Var.  *yoB  F.  8-.  lies  'iairya^.
*  j.  va<)a')^n-  m.  EN.  eines  glaubensfeind- lichen  Fürsten:  adavata  ..  aarS  mainyui: ,  ,  tard^uilra  .  .  apastavartuha  .  .  dabtqm mätdayasnJm  vindäi  ystum  ya^a  vindai °nS  (NS.)  ■'  daiähupaitis  ". .  Zar. !  schwör der  maid.  Religion  ab,  um  die  Gunst  zn erlangen,  wie  sie  der  Landesherr  V.  er- langte" V.J5.6;  —  •7a(NS.)  Y.8'\
*)  Nach  mp.  Schriften  mit  AiDahik  identisch; vgl.  Mx.  j/.  24f. :  ahraman  e  sara%u!l  dräyitt  itt haiar  hal  in  din  . .  i  matdaymnän  aj>ik  itti än^äk  at  1000  säl  j^aläiJi  . .  dahem  Hgön  1/08070«« (geschr.  ntkann)»  dahyupeU  dahAk  dir.
Eig.  Bed.?  —  ■)  Them.  —  '}  Hds.  vatara; '  ■  -      dy).  -   J)  S.  dazu  West  SEE.  24.
103.  ■
-  3»-
•  j.  va8ay- :  vaili-  f.  'Wasserlauf,  Be- wässerungskanal': nil  tat  3p»m  hintatä ' yavd.caränlm  (sd.)  ana  tä  '%Tnt  ayä  ana bittm  . .  pasla  tüirJm  nasäum  ava.iansfnti (sd.)  "entlang  dem  Kanal  läuft  es  (das Wasser)  alsdann,  entlang  zum  zweiten Mal  . .,  dann  .  ."  V.  5.  5;  — ■  °}>Tm  taci.- apqm  .  .  nistrinuyHt  .  .  cvat  yaval  °hXm1 spä.b}nz»n  (sd.)  späfrdk  m  "einen  Be- wässerungskanal mit  tliessendem  Wasser  . ." \.  14.12.  [F-S:  lies  vaSim.]
Zum    au   V.   undlä.   —    VgL   *uia:  —   Vgl.
dby  Google
1345
vadar-
vafav-
*346
arm.    gil    'fluss';     PDw.     v5d    'Kanal'.     —
•  j.,  g.  vadar-  n.  'Waffe  (zum  Schlagen)': yasla  'dar!  vSisdai  aläuns  "und  der  die Waffe  wider  den  Rechtgläubigen  erhebt" Y._j2.  lo;  —  paifi  .  .  kihrpim  .  .  haoma . .  'dar}  /ai\i^'>  "gegen  den . .  Leib  schlag . . die  Waffe"  Y.o.  30;  30—32*,
Vgl,  vada-  und  vädäya:  —  ai,  vidhar-  n.  (bes. von  Indrai  Waffe).  —  PS-  (lu  Y,  32):  hacai pa  ptAlikik  ösiin  dal  ö  oAravän,  (lu  Y,  9); paltäklne  (SQ.:  paraiäiaya)  lanän,  erl,;  ia! iärai  api  gäw,  —  ')  VgL  jahi  vädhak  RV.  4. i%.  9.
•  j.  vaSairyav-"  Adj.  'nach  Begattung veitangend,  brünstig',  vom  Kamelhengst'': uitrS  'rii^^  Yt.i4.39;  12;  —  uÜrahe hhrpa  'ryaol  Yt  i^.  n ;  *F.  8;  —  uitr&nh5 .  .  p»r3tamna  (sd.)  'ryavd  Yt, /7. 13,
PPA,  (Saqp.  4),  aus  •i^iaiVj'i- den.  Praes.  31 ; s.  i'oJü-.  —  ai.  vgl.  vadküyäv-  Ad],  (und  vadhar- yäniim  RV.  /.  161.9?);  Gdn.  3Yt  68,  —  Pu.: vaharn),  Npii.:  xabar  dar  n  rik  däHnnda.  — •)  NA.  auLh  •lar:  —  >)  VgL  zBed.  Yt,  14.11 mit  7,  15.  —  J>  Sta(t  'ryiä  geschr.,  S  2öä  14-
22418:vadar-
```


## [2026-10-16T05:14:54.637Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"v[äa]d[äa]ya\" BRT.txt | head; "
}
```


### [2026-10-16T05:14:54.938Z] TOOL RESULT

```
22423:Vgl,  vada-  und  vädäya:  —  ai,  vidhar-  n.  (bes. von  Indrai  Waffe).  —  PS-  (lu  Y,  32):  hacai pa  ptAlikik  ösiin  dal  ö  oAravän,  (lu  Y,  9); paltäklne  (SQ.:  paraiäiaya)  lanän,  erl,;  ia! iärai  api  gäw,  —  ')  VgL  jahi  vädhak  RV.  4. i%.  9.
23478:•  g.  vädäya-  Praes.  33  'zurUckslossen'. 'zurUcksIossen,    -drängen,    fernhalten':
30034:•  j.    hEjm.srut-vädaya- ",    -vlcya-   n.
```


## [2026-10-16T05:14:56.869Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23470,23486p BRT.txt | cut -c1-500"
}
```


### [2026-10-16T05:14:57.211Z] TOOL RESULT

```
•  j.  väiti-gaesa-  in.  Name  eines  Gebirgs*>: ; akmal  hala  garayS  fraexsyan  . .  dvadasS  j 'SS  Yt  ig.  2.
♦)    Bd.  13.  2,   19:    ySlgfr   Ijetit  BSdgls),    ein' vom  Xui^nu  durchbrochener  Höhenzug  nörd- ,
lieh  TOD  Hiräi;  vgl.  Gaa.  OK.  65 ;  s.  noch  Hbu. AGr.  /.  79.     Die  Erklärung  in  SWienAW.  6/. S41.  13  ist  geitörl. Eig.  Bcd.?
•  j.  vätya-  (Adj.  'zum  Wind  gehÖrig">, als)  m.  Bezeichnung  eines  Dafva,  des  D. des  verderblichen  Winds '*:  paiti.ptrstu varmya  dalvB  paiti.pinne  'tTm  dalvS  V. V.  10. 14".
Ableit  am  väia-*).  —  ai.  vätya-  Adj.  O.  — Pü.;  vSIli,  erl.;  välai  kor.  —  i)  So  nach  Pü. —  »)  Ungrammatische,  geringe  Stelle.
■  j.  vädtnan-  n.  'Erschlaffung,  Abspannung* :
'maini  *asaya  (sd.)  :^aßta  vd  anaivilti astryeiti  N-l^.
Zum  ai^  V.  väyaiit).  —  Pü.;  taitj  (in  SQ.  lu Sg.  äyäiak).  —  >)  Zur  Sufüxfonn  i.  Bau. GrGr.3   189  und  värAman-.
•  g.  vädäya-  Praes.  33  'zurUckslossen'. 'zurUcksIossen,    -drängen,    fernhalten':
k3m  höi  ustä  (sd.)  ahuntn  yS  ^dngvBjhbfi
alhmim  (sd.)  vädäyöit  Y.  20.  2.
Vgl.  er.  «ä.'»i  %  144.  —  Pü.1  if  .  .  £amm daAel,  Sü. :  j/e  . .  fädanäm  [%,  'van-  No.  l6) daitt.
•  j.  vävarää-  f.  Name  einer  Krankheit'': paitistätse  garmäuUa  tafnaoUa  naUah^a iSrastSilca  'lyas^a  YtJ^.  131.
Ir.  wohl  'sfä/fcSä-  (IF.  p.  261),  Bildung  mit Int-Red.  —  ")  Ohne  Wert  Gdn.  KZ.  ij.  551 1 'Wolkenbruch',    Dst.   ZA.  2.  5491    *rinconti-
•  j,  vävsrszana-  Adj.,  PPfM:  s.  'vans-.
•  j.  vävsrszvah- :  •aä-  Adj.,  PPfA. :  s. 'vanz:
•  j.  'vir-  m.  1)  'Regen':  staomi  marjimca 'r^mta  ya  ti  (näml.  haomahe)  kthrpfm vaxiayatS  Y,  10.  y,  —  äsyaipAa  (sd.) 'raübya  Y.  57.  28;  —  *'rS  (GS.?) F.8'>.        2)  'Regentropfen'  (nur  Komp.).
```


## [2026-10-16T05:15:03.961Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88800,88815p POK_full.txt; grep -n -E \"w[oō]ks|woksos|wokso|w[eē]dh[oōa-]\" IEC.txt | head -20"
}
```


### [2026-10-16T05:15:04.288Z] TOOL RESULT

```
References: WP. I 254 f.. Frisk 446 f., 449 f. 
Page(s):1115 

Root/ lemma: ue6y-2, vor Nasalen ued- 

Meaning: to lead 

Material: Old Indie vadhu-i. "bride, young wife, woman', Avestan va5u- ds., vaSayeiti 

(Kaus.) "leads, zieht', with upa- "eine Frau zur matrimony give', with us- "(Frauen) 

entfijhren, rob', KaJ/ya-"heiratsfahig (from girl)'; 

Old Irish /eo'/io'" leads, goes, carries, brings ', mcymr. go-di-wawd^ overtaken ', Old Irish 
to-fed-, to-dhfed- 'gu'\de, lead', cymr. arweddu 'gu'\de, lead, bring', Verbalnom. mcymr. 
20275:uidheuos, å ‘set aside, separated, separate’; (f.) ‘widow’. WP I, 240 Skt. vidhúh ‘solitary’; vidhávā, f. ‘widow’; Per. biva, bīve ‘widow’; Alb. e ve, f. id.; Lat. viduus ‘bereft, destitute, void”; vidua, f. ^wi- dow, unmarried woman'; (cf. the Rom. form via *vuidu-: Sard. boidu “empty, void'; Ru- mansh vód, f: vóda, id.; OFr. (dial. -t- for -d- as in vert, verte (green) vuit, Fr. vide and Anglo-Norman void, de-void fr. *dē-°, cf. so- lum arboribus viduum ‘soil devoid of trees’ — Columella); Olr. fedb, Ir. feadhbh, f. ^wid- ow, nun’; W gweddw, adj. (single), ambig. cf. uiduilos) beside gweddw, f. ‘widow’; Cor. gwedhow, adj. ‘widowed’; f. ‘widow’; Go. wi- duwo, OHG wituwa, OS widuwa, OE wudu- we, Du. weduwe, id.; OCS (and com. Sl.) vídova, f. id.; Slovene (also) vdov, adj. *widow- ed'; OPr. widdewü (sic), id.
```


## [2026-10-16T05:15:07.204Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^u[oō]ks|^u[eē]dh|^u[eē]g[^ʷh]|^uog\" IEC.txt | head -20; grep -n -c \"\" IEC.txt"
}
```


### [2026-10-16T05:15:07.723Z] TOOL RESULT

```
19800:uedh- (1) “marry; marriage; bride, bridal. Cf. ufuédh- and WP I, 254 Skt. vadhüh, f. ‘bride’; Av. cf. vaóryo, adj. ‘marriageable’; Oss. cf. ár-wád, s. &bride-price'; W cf. dy-weddi, pl. -iau, mf. ‘marriage’; Li. vedýs, gs: védzZio, m. ‘bridegroom’; védes *married'; Latv. vedēji, mpl. ^wedding-guests of the bridegroom’; vedibas, fpl. ‘homing of the bride’; Gk. cf. n&thís, f. (spinster, fr. *ne- uedhi-); eitheos (bachelor, fr. a type *ne- ufuédh-, see ufuédh-); G cf. Wittum (confu- sion w. type uedm- and w. OHG widamo *widow's endowment. See uidheua)
19801:uedh- (2) “lead, bring, carry’. WP I, 254 Skt. vadhami, v. (“take home’. Infl. of uedh- (D, q.v); Av. vad-, v. tr. & intr. “lead; go’; Tokh. AB, cf. wày-, v. “lead”; Hitt. wedàmi, v. ‘carry, bring’; Olr. fedim, v. “lead, bring"; OCS vedo, vesti (and com. SLL v. tr. "lead, bring’; Li. vedü, vèsti, v. lead, guide; wage, carry on’; Latv. vedu, vest, v. “lead; travel’; OPr. cf. wedeis, 2sg. opt. ‘mayest lead"; prob. o-gde in Gk. oth-neios (stranger, newcomer’, cf. neu-)
19802:uedh- (3) “join, fit’. Cf. uedh- (1) OW E W gweddu, inf. ‘suit, fit, yoke’; gwedd, pl. au, f. ‘yoke’; gweddw, adj. (1) “fitting,
19814:uedh- (4) “fight Tokh. B wat. wet-, v. id.; weta, s. id.; Gk. cf. á-ethlon, n. (contest', fr. *sm-uedhlom); Hes. cf. éthon, gs: -ontos ‘striking’; (alleged) étho, v. tr. ‘strike’; Lat. cf. bellum, n. (war, fr. *dui-uedhlom) beside pro-ellium, n. (battle, fr. *pro-uedhlio-); Olr. cf. feidm, m. ‘effort’; Ger. cf. Wett- in Wett-streit (icontest'. Su. un- tics of R o-gde po-vodevàt' ‘wage war’)
19815:uedher- (uedhr-) ‘weather’. WP I, 222. Cf. auedhr- Skt. vadhar, n. ‘thunderbolt’; vadharyàmi, v. ‘hurl thunderbolts; OHG wétar, OE weder, ON veðr, n. “weather, wind, lower air, sky”; OCS vedrü, vedro, mn. (‘fine weather; heat- wave’, and com. Sl.);
19816:uedhlom, see uedh- (4)
19817:uedhris ‘castrated animal; wether’. WP I, 255 Skt. vádhrih, adj. (castrated'; m. ‘castrated animal’; Hes. ethrís, m. ‘wether’; OE weder, m. id. (but weóer, id. unrelated. See uetos, -es-); ON (ambig.) veðr, gs: veórs, m. ‘wether’
19818:ueg- “twist, weave". WP I, 247. Cf. uig- (1) Alb. vegj, v. ‘weave’; vegjë, f. doom’; Olr. figim, Ir. fighim, v. ‘weave’; -fige, cpds. '*-weav- ing; cf. Ir. feagán, m. ‘flange of spinning- wheel; W gweu, inf. ‘weave’; gwau, pl: gweu- oedd, m. ‘weave, texture’; G cf. Wocken, m. ‘distaff
20499
```


## [2026-10-16T05:15:13.469Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \".{0,200}(ōthé|othéō|otheo|ōsmós|osmós).{0,200}\" IEC.txt | head; grep -n -E \"^u[oō]ks|^uoks|^u[aā]ks\" IEC.txt | head; sed -n 19818,19820p IEC.txt | cut -c1-900"
}
```


### [2026-10-16T05:15:16.965Z] TOOL RESULT

```
ugrep: error: error at position 115
eo|ōsmós|osmós)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                       exceeds complexity limits___/


19686:uaks- ‘growth’, cf. aueKs-
ueg- “twist, weave". WP I, 247. Cf. uig- (1) Alb. vegj, v. ‘weave’; vegjë, f. doom’; Olr. figim, Ir. fighim, v. ‘weave’; -fige, cpds. '*-weav- ing; cf. Ir. feagán, m. ‘flange of spinning- wheel; W gweu, inf. ‘weave’; gwau, pl: gweu- oedd, m. ‘weave, texture’; G cf. Wocken, m. ‘distaff
uegh- ‘say, utter’ Skt. cf. vāghát, nt-st, m. “official at sacrifice’; Per. güvam, guftan, v. ‘say’; Arm. gogem, aor. 3s. gog, v. ‘say, utter’; Hitt. hwekmi, hwikmi (hweikm:i), 3pl: hukanci, v. ‘pronounce, de- clare’
uëghros, is (uëghlis) ‘slim, tiny’ Arm. girg, adj. ‘tender, delicate’; Alb. i vogërr,
```


## [2026-10-16T05:15:19.690Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"ōthé|othéō|ōsmó\" IEC.txt | cut -c1-300 | head; grep -n -E \"vosk|vaškas|vaskas\" IEC.txt | cut -c1-400 | head -3"
}
```


### [2026-10-16T05:15:20.111Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:22.471Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"wax\" IEC.txt | cut -c1-400 | head -5; grep -n -E \"wax|Wachs\" SYN.txt | head -5"
}
```


### [2026-10-16T05:15:22.764Z] TOOL RESULT

```
942:biĝ- ‘wax, glue, resin’ or sim. Oss. bidz, D bedzä ‘lees of beeswax’; Ir. bigh ‘glue’; Arm. cf. piyc (‘dirty’, fr. *biglo-)
1583:bhra$mn- (1) “break, break-up, breakdown'. See bhra$o, ið k Alb. brâm “lees of wax’; Lat. fragmen ‘scrap’; (LLat. also *breakage, refraction, broken speech’); Br. cf. di-framm ‘rupture, breach?
1952:bhunghos, à ‘hump, bulge, growth; drum; bulging’, etc. Cf. bhun$- Kurd. bong ‘conceited’; Alb. bungé ‘lump, gnurl; Lat. fungus, m. ‘growth, fungus, blight, wax round wick; OHG bunga, f., bungo, wm. ‘lump, hump; knob’; G Bun- ge ‘drum; bownet'; Fris. bonge ‘bladder, blister’; Icel. bunga ‘lump’; Latv. bungas, fpl. “drum”
2322:dieus, obl. diu- (cons. stem) ‘god, sky”. Cf. diu-, etc. WP I, 772. Also: deiuos, à (variant) ‘god, goddess; demon, demoness' Skt. dyáuh; deváb; Per. div ‘demon’; Oss. cf. äv-dīw, -dew (*demon'. Cf. G “Ab-gott'); Thess. cf. dagüs “ritual wax image”; Arm. tiwr, tir ‘god, idol; tiv ‘day’; Av. cf. paiti-dayus *very-deceitful' beside daevo ‘demon’; Myc. cf. diwijewe ds.; Gk. Zeüs; Gk-Albanian Die
6801:kārios, iə ‘wax, honeycomb’. WP I, 355 Gk kërós ‘wax’; kēríon ‘honeycomb’ (LW in Lat. cera); Li, korýs, m. ‘honeycomb’; Latv. kāre, id. (Gk. ē is panhellenic accdg. to L & S, if so, Lat. cera is a cognate, and Li. Latv. are unrelated)
2229:tive of the word for ‘sulphur’; and some of these remained, either generally or locally, in common use for the ‘match’, regardless of the change in materials used. Less common was the use of ‘phosphorus’ for ‘match’. Terms which apply to the wax tapers but not to matches in general, as It. cerino (vs. flammifero), Sp. cerilla (Am. Sp. cerillo) are not included in the list. The wooden ‘stick’ appears in some of the words, either in combination (NHG streichholz, etc.) or alone (SCr. sibica, Russ. spi¢ka). The important notion of friction has
2237:Sp. fésforo ‘phosphorus’ and the usual word for ‘match’, except the wax taper (cerilla, cerillo). Similar words elsewhere are quotable for ‘match’, as NG dwe¢épor, but are not common in this sense.
2456:5. Lith. vaikas, OPruss. wax : Lith. viekas ‘strength’, vezkti ‘do, work’ (these : Lat. vincere ‘conquer’, Goth. wethan ‘fight’, etc. Walde-P. 1.232 ff.). Brug- mann, IF 38.141.
12182:town, some material used, as wax. But several words for ‘wax candles’ are used only for those in ceremonial, not in do- mestic, use.
12183:1. NG xept, fr. Grk. xnplov, dim. of knpés ‘wax’ (xnpol ‘wax candles’ from ad cent. A.D.), whence Lat. céra ‘wax; céreus ‘wax-candle’ (> It. cero, SP. cirio, OF r. cirge > ME cerge). Trnout- M. 176. Walde-H. 1.202. REW 1829.
```


## [2026-10-16T05:15:27.682Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for n in 263 264 256 324; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' WLD_Bd1_pages.txt | grep -n -E \"pages|ued|ueg|uok|vadh|vada|ὠθ|wθ|Wachs|wahs|wick|Docht|velum|Keil\" | head -12; done"
}
```


### [2026-10-16T05:15:28.039Z] TOOL RESULT

```
=== leaf 263
6:254                                                ued-    — uedh-
87: l.    uedh- „sto8en, schlagen“.
88:      Ai. vadhuti , avcidhit „schlagen, stoBen, vernichten“. kaus. v adhayati, uaditu-
90: av. vada- m. „I\eil zum Spalten des IIolzes“, ai. vadhar- n. „Mordwaffe
91: (bes. von Indras GeschoB)“ = av. vadar- n. „Waffe (zum Schlagen)", av.
=== leaf 264
34:                                          *uodh-uo-)\        ist   auch    av. vadayan- „EN\ eines glaubens-
46:zu TFos.w, s. *ued „netzen“?).
49:2.    uedh „fiihren; heimfiihren, heiraten (vom Manne)“.
52:Frau  vadayeiti (Kaus.) „fiihrt, zieht, schleppt". mit upa- „eine Frau zur
=== leaf 256
36:wcecnan „geboren werden" erklart auch die Bed.-Entwickung von got.
56:meymr. gweir „Heu“, ncymr. gwair, acorn, gttgraf ds. ( *uegro -) an ''etwas
62:„vermehren“; Fick II 4 266 stellt sie zu ueg'i- „netzen“, s. d.).
63:  Yereinigung von *ueg- mit *aueg- ,.vermehren“ etwa unter **anc- „frisch,
67:ueg- „schwach, klein"?
77:   Ai. vagurd „Fangstrick, Ketz zum Wildfang, Garn“; lat. velum „Segel;
79:Fahnchen" (uber abweichende Auffassungen von velum s. Liden Stud. 20ff.
90:   ags. wice „Docht“, nhd. bair. wichengani „Baumwolle zu Dochten           norw.                             ,
96:s. Falk-Torp      u. veege  Persson Beitr. 323a 3); mhd. wiht „Docht“ ags.
103:wecca „Docht“, and. wekko mnd. weeke „Docht, Lunte", mhd. ivicke „Docht,
107: Scharpie", nhd. mdartl. ivicke „der um die Spindel gewickelte Flachs“, ahd.
=== leaf 324
47:ijokso- ,,Wachs“.
48:   Ahd.           as.   wafts, ags.          waw, aisl. vttx n. ,.Wachs*‘                  ;
50:ds. ;       russ. ksl. (usw.) voslz                   ds.    Yerniutlich       zu *ueg-             ..weben”,      wie ahd.
54:lat.       corn mit       cri-sco,      s.   u.   *qar- ,,Wachs‘‘), Trautmann Bsl. Wb. 343.
```


## [2026-10-16T05:15:37.524Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==263' WLD_Bd1_pages.txt | sed -n 86,110p; awk 'BEGIN{RS=\"\\f\"} NR==324' WLD_Bd1_pages.txt | sed -n 1,8p | head -3"
}
```


### [2026-10-16T05:15:37.953Z] TOOL RESULT

```
 l.    uedh- „sto8en, schlagen“.
      Ai. vadhuti , avcidhit „schlagen, stoBen, vernichten“. kaus. v adhayati, uaditu-
 m. „totend, Mordwaffe (bes. von Indras GeschoB); Schlag, Yernichtung" =
 av. vada- m. „I\eil zum Spalten des IIolzes“, ai. vadhar- n. „Mordwaffe
 (bes. von Indras GeschoB)“ = av. vadar- n. „Waffe (zum Schlagen)", av.
 imdaya- zuriickstoBen“ (dehnstufig wie gr. wdko) gr. k’der g-dsigei. igi&tgei     ;

 Hes., hom. I'&cov „stoBend, zerwiihlend" (s. K. Fr. W. Schmidt KZ. 45,

                                     uis-en-      — uog“hni-s. nog“hnes-, noguliio-                                      315

   Mit 7:          lat.   vir ,,Mann“, in der                  altern   Sprache auch das einzige Wort
```


## [2026-10-16T05:15:42.232Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^واکس|واکس[ .]\" MON_part2.txt | head -5; grep -n -E \"اسمز|اُسمُز|اسموز\" MON_part1.txt | head -5; grep -n -E \"واکس|اسمز\" incoming/ARY/ARY_pages.txt | head; grep -n -i -E \"^(VAKS|OSMOZ)\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-16T05:15:42.558Z] TOOL RESULT

```
83751:واکس: ۶(.) مده‌ای روغنی به 
83755:واکسن: ۱۶ (.) (یز.) هر ماده‌ای که به 
83764:واکسسی: -۷2۷2 (ص‌نسب.) منسوب به 
83767:واکسیل: ۷2۳۰ [- وکسیل مخف. واکسیل 
83771:واکسسیناسیون: «مرحقدآی۷2 (.)
```


## [2026-10-16T05:15:45.336Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 83749,83756p MON_part2.txt; grep -n -E \"^ا?سم[زر]|اسمز|أسمز|اسمُز\" MON_part1.txt | head"
}
```


### [2026-10-16T05:15:45.820Z] TOOL RESULT

```
ِ 

واکس: ۶(.) مده‌ای روغنی به 
رنگ‌های مسختلف جهت رنگ کردن 
کفش‌ها بکار برند. 

واکسن: ۱۶ (.) (یز.) هر ماده‌ای که به 
موجود زنده‌ای جهت ابجاد مصونیت در 
13122:اسمر: 7۲ [ع.] (ص.) گندم‌گون. 
75931:سمزد و اجرت. تمسحر» لغ شسوس.
```


## [2026-10-16T05:15:59.793Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-10-16T05:16:00.271Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-16T05:16:06.231Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-\" \"https://en.wiktionary.org/wiki/ὠθέω\" \"https://en.wiktionary.org/wiki/ὠσμός\" \"https://www.etymonline.com/word/osmosis\" \"https://en.wiktionary.org/wiki/osmose\" \"https://en.wiktionary.org/wiki/wax\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wókso\" \"https://en.wiktionary.org/wiki/wick\" \"https://en.wiktionary.org/wiki/vakso\" \"https://en.wiktionary.org/wiki/вакса\" \"https://en.wiktionary.org/wiki/واکس\" \"https://en.wiktionary.org/wiki/velum\" \"https://en.wiktionary.org/wiki/veil\" \"https://www.etymonline.com/word/reveal\" \"https://www.etymonline.com/word/wax\" \"https://www.etymonline.com/word/wick\" \"https://en.wiktionary.org/wiki/vadar\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weg-\" \"https://www.etymonline.com/word/veil\"; do python3 tools/fetch_source.py \"$u\" --note \"page 529: Wedh 2 / Weg 1 entries\" 2>&1 | tail -1; done"
}
```


### [2026-10-16T05:16:14.259Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f007cfce6fb527b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/40b6f1ac92b2b2dc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/105daa35bdad0d89.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dad6a69b9e5ca63e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2565da7d64f72299.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5ae9e65d18cfa982.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2410cd5cece4f75.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/11752dac8d0a63d6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/10f58356b0c06c94.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f40ede120cfda7b6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/15899fe244113dc5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/61c60b3cff0d0a87.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7c9e0a65dbc92863.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ab1b9a6581e17005.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/efccaa678dab028d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2e4fef09823eaf45.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3785aa08e6d8ae3d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/02e338ba4c7926fb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f72603b648ea1af.txt
```


## [2026-10-16T05:16:16.741Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -19 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['url'])\"; grep -n -i -A3 \"etymology\" 8f007cfce6fb527b.txt | head -40"
}
```


### [2026-10-16T05:16:17.244Z] TOOL RESULT

```
200 4837 https://en.wiktionary.org/wiki/osmose
200 38980 https://en.wiktionary.org/wiki/wax
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wókso
200 45150 https://en.wiktionary.org/wiki/wick
200 3752 https://en.wiktionary.org/wiki/vakso
200 4498 https://en.wiktionary.org/wiki/вакса
200 2376 https://en.wiktionary.org/wiki/واکس
200 13564 https://en.wiktionary.org/wiki/velum
200 17906 https://en.wiktionary.org/wiki/veil
-1 39 https://www.etymonline.com/word/reveal
-1 39 https://www.etymonline.com/word/wax
-1 39 https://www.etymonline.com/word/wick
200 3972 https://en.wiktionary.org/wiki/vadar
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weg-
-1 39 https://www.etymonline.com/word/veil
200 42888 https://en.wiktionary.org/wiki/wave
200 2231 https://abadis.ir/fatofa/وردیج/
200 20826 https://en.wiktionary.org/wiki/Norway
200 725 https://vajehyab.com/dehkhoda/وردیج
```


## [2026-10-16T05:16:20.188Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep \"page 529\" index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['file'],d['url'])\""
}
```


### [2026-10-16T05:16:20.751Z] TOOL RESULT

```
200 14469 data/verification/sources/web/8f007cfce6fb527b.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-
200 22007 data/verification/sources/web/40b6f1ac92b2b2dc.txt https://en.wiktionary.org/wiki/ὠθέω
200 4122 data/verification/sources/web/105daa35bdad0d89.txt https://en.wiktionary.org/wiki/ὠσμός
-1 39 data/verification/sources/web/dad6a69b9e5ca63e.txt https://www.etymonline.com/word/osmosis
200 4837 data/verification/sources/web/2565da7d64f72299.txt https://en.wiktionary.org/wiki/osmose
200 38980 data/verification/sources/web/5ae9e65d18cfa982.txt https://en.wiktionary.org/wiki/wax
-1 39 data/verification/sources/web/c2410cd5cece4f75.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wókso
200 45150 data/verification/sources/web/11752dac8d0a63d6.txt https://en.wiktionary.org/wiki/wick
200 3752 data/verification/sources/web/10f58356b0c06c94.txt https://en.wiktionary.org/wiki/vakso
200 4498 data/verification/sources/web/f40ede120cfda7b6.txt https://en.wiktionary.org/wiki/вакса
200 2376 data/verification/sources/web/15899fe244113dc5.txt https://en.wiktionary.org/wiki/واکس
200 13564 data/verification/sources/web/61c60b3cff0d0a87.txt https://en.wiktionary.org/wiki/velum
200 17906 data/verification/sources/web/7c9e0a65dbc92863.txt https://en.wiktionary.org/wiki/veil
-1 39 data/verification/sources/web/ab1b9a6581e17005.txt https://www.etymonline.com/word/reveal
-1 39 data/verification/sources/web/efccaa678dab028d.txt https://www.etymonline.com/word/wax
-1 39 data/verification/sources/web/2e4fef09823eaf45.txt https://www.etymonline.com/word/wick
200 3972 data/verification/sources/web/3785aa08e6d8ae3d.txt https://en.wiktionary.org/wiki/vadar
-1 39 data/verification/sources/web/02e338ba4c7926fb.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weg-
-1 39 data/verification/sources/web/0f72603b648ea1af.txt https://www.etymonline.com/word/veil
```


## [2026-10-16T05:16:22.769Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 1,80p 8f007cfce6fb527b.txt | cut -c1-300"
}
```


### [2026-10-16T05:16:23.098Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-
FETCHED: 2026-10-16T05:16:06Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/wedʰ- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/wedʰ- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Alternative reconstructions 

 1.1.2 
 Derived terms 

 1.1.3 
 References 

 1.2 
 Root 

 1.2.1 
 Reconstruction notes 

 1.2.2 
 Alternative reconstructions
```


## [2026-10-16T05:16:26.181Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v \"^\\s*$\" 8f007cfce6fb527b.txt | sed -n '/^ *Root/,$p' | sed -n 1,140p | cut -c1-250"
}
```


### [2026-10-16T05:16:26.664Z] TOOL RESULT

```
 Root 
 1.1.1 
 Alternative reconstructions 
 1.1.2 
 Derived terms 
 1.1.3 
 References 
 1.2 
 Root 
 1.2.1 
 Reconstruction notes 
 1.2.2 
 Alternative reconstructions 
 1.2.3 
 Derived terms 
 1.2.4 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ wedʰ- 
 Add languages 
 Reconstruction 
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
 Get shortened URL 
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *wedʰ- [ 1 ] [ 2 ] [ 3 ] [ 4 ] 
 to lead , [ 5 ] [ 1 ] conduct 
 to bring 
 Alternative reconstructions
 [ edit ] 
 *h₂wed- , *h₂wedH- [ 5 ] 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *wedʰ- (lead) (24 c, 0 e) 
 *wédʰ-e-ti ( thematic root present ) 
 *wédʰ-se-ti ( se-desiderative ) [ 2 ] 
 Proto-Indo-Iranian: *wádzʰati [ 2 ] 
 Proto-Iranian: *wájati 
 Younger Avestan: 𐬬𐬀𐬰𐬌𐬌𐬀𐬨𐬥𐬁 ( vaziiamnā , “ leading ” , fut med ptcp ) 
 ⇒ Proto-Iranian: *wājayati [ 6 ] 
 Khwarezmian: 𐾶𐾰𐾸𐾺𐿄 ( wʾzyt /⁠wāzēt⁠/ , “ to lead out ” , 3 sg impf caus ) 
 *wḗdʰ-s-t ~ *wédʰ-s-n̥t ( s-aorist ) [ 1 ] [ 7 ] [ 8 ] 
 Proto-Balto-Slavic: 
 Proto-Slavic: *věsъ ( 1 sg aor ) 
 Old Church Slavonic: вѣсъ ( věsŭ , “ I lead, I conducted ” ) 
 Proto-Celtic: *-wīss ( 3 sg subj ) 
 Old Irish: do-n·fé 
 *wodʰ-éye-ti ( eye-causative ) [ 1 ] 
 Proto-Anatolian: 
 ⇒ Hittite: [script needed] ( u-watemi , “ bring forth ” ) 
 Proto-Balto-Slavic: *wádīˀtei ( “ to lead, conduct ” ) ( see there for further descendants )
 Proto-Indo-Iranian: *wādʰáyati 
 Proto-Iranian: *wādáyati ( “ to lead, conduct; to bring ” ) ( see there for further descendants )
 → ? Proto-Uralic: *wetä- ( “ to lead, guide, pull ” ) 
 *wedʰ-o-s 
 Proto-Anatolian: *wedos 
 Hittite: *wedaš [ 9 ] 
 ⇒ Hittite: 𒌋𒄿𒁕𒀀𒂊𒍣 ( ú-i-da-a-ez-zi /⁠wedaezi⁠/ ) ~ 𒌋𒂊𒁕𒀭𒍣 ( ú-e-da-an-zi /⁠wedanzi⁠/ , “ to bring (here) ” ) 
 *wodʰ-eh₂ [ 10 ] 
 Proto-Albanian: *wada [ 11 ] 
 > ? Albanian: udhë ( “ path ” ) 
 *wodʰ-o-s 
 Proto-Balto-Slavic: *wadas 
 Lithuanian: vãdas ( “ leader, commander ” ) 
 References
 [ edit ] 
 ↑ 1.0 1.1 1.2 1.3 Rix, Helmut , editor ( 2001 ), “*u̯edʰ- ‘führen’”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 659 
 ↑ 2.0 2.1 2.2 Kümmel, Martin Joachim ( 2011–2026 ), “ *u̯edʰ-e/o- ”, in Addenda und Corrigenda zu LIV² ‎ [1] , page 79 
 ^ Pokorny, Julius ( 1959 ), “ 2. *u̯edh- ‘führen’ ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, pages 1115-1116 
 ^ Kölligan, Daniel ( 2018 ), “Chapter XX: Proto-Indo-European”, in Klein, Jared S., Joseph, Brian D. , Fritz, Matthias , editors, Handbook of Comparative and Historical Indo-European Linguistics: An International Handbook (Handbücher zur Sprach- und
 ↑ 5.0 5.1 Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), “*h₂u̯ed(hₓ)- ‘lead; take to wife’”, in Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn Publishers, page 346 
 ^ Benzing, Johannes ( 1983 ), “ 1 w’zyt-”, in Chwaresmischer Wortindex , Wiesbaden: Harrasowitz, page 642 : “ *wāzay- ” 
 ^ Petit, Daniel ( 2018 ), “Chapter XVIII: Balto-Slavic”, in Klein, Jared S., Joseph, Brian D. , Fritz, Matthias , editors, Handbook of Comparative and Historical Indo-European Linguistics: An International Handbook (Handbücher zur Sprach- und Kommun
 ^ Tremblay, Xavier ( 2009 ), “Die thematischen Wurzelpräsentia im Hethitischen. Die indogermanischen Konjugationen im Anatolischen I”, in Lühr, R., editor, Protolanguage and Prehistory (in German), page 503 of 478-512: “ air. Konj. do-n·fé < *u̯étˢ-
 ^ Kloekhorst, Alwin ( 2008 ), “u̯edae- zi ”, in Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 5), Leiden, Boston: Brill, →ISBN , pages 1009-1010 : “ unattested noun *u̯eda- ” 
 ^ Dočkalová, Lenka; Blažek, Václav ( 2011 ), “On Indo-European roads”, in The Journal of Indo-European Studies ‎ [2] , volume 39 , number 3/4 , page 315 of 299–341: “ udhj “path” < *u̯odhā from the verb *u̯edh- “to lead” ” 
 ^ Orel, Vladimir ( 1998 ), “ udhë ”, in Albanian Etymological Dictionary , Leiden; Boston; Cologne: Brill, →ISBN , pages 482–483 : “ EPA *wada ” 
 Root
 [ edit ] 
 *wedʰ- [ 1 ] [ 2 ] 
 to bind , [ 1 ] join [ 3 ] 
 Synonyms: *bʰendʰ- , *sh₂ey- , *yewg- 
 to marry [ 4 ] [ 5 ] [ 2 ] 
 Synonyms: *ǵem- , *snewbʰ- 
 Reconstruction notes
 [ edit ] 
 Rix merges this root with that of *wedʰ- ( “ lead ” ) above, whereas others, following Pokorny, maintain that the two were distinct roots. [ 6 ] [ 7 ] 
 Alternative reconstructions
 [ edit ] 
 *h₁wed- [ 5 ] [ 8 ] 
 *h₂wedʰ- , *h₂wedʰH- [ 4 ] 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *wedʰ- (bind) (18 c, 0 e) 
 *wédʰ-e-ti ( thematic root present ) 
 *wodʰ-éye-ti ( eye-causative ) 
 Proto-Indo-Iranian: *wādʰáyati 
 Proto-Iranian: *wādáyati ( “ to marry ” ) ( see there for further descendants )
 *wédʰ-mn̥ ~ *udʰ-mén-s ( “ bride price, dowry ” ) 
 *wedʰ-ó-s [ 9 ] 
 Proto-Celtic: *wedos ( “ yoke, harness ” ) ( see there for further descendants )
 Proto-Indo-Iranian: *wadʰás 
 Proto-Indo-Aryan: *wadʰás 
 ⇒ Sanskrit: विवध ( vivadhá , “ yoke ” ) 
 *wedʰ-r- 
 ⇒ ? *wódʰr-i-s ~ *wédʰr-i-s ( “ castrated ” ) [ 10 ] [ 11 ] [ 12 ] 
 Proto-Hellenic: *wétʰris 
 Ancient Greek: ἔθρις ( éthris ) 
 Proto-Indo-Iranian: *wádʰriš 
 Proto-Indo-Aryan: *wádʰriš 
 Sanskrit: वध्रि ( vádhri ) ( see there for further descendants )
```


## [2026-10-16T05:16:30.494Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 40b6f1ac92b2b2dc 105daa35bdad0d89 2565da7d64f72299 3785aa08e6d8ae3d; do echo \"=== $f\"; grep -v \"^\\s*$\" $f.txt | grep -n -i -A8 \"^ *Etymology\" | head -25 | cut -c1-400; done"
}
```


### [2026-10-16T05:16:30.806Z] TOOL RESULT

```
=== 40b6f1ac92b2b2dc
41: Etymology 
42- 1.3 
43- Pronunciation 
44- 1.4 
45- Verb 
46- 1.4.1 
47- Conjugation 
48- 1.4.2 
49- Derived terms 
--
102: Etymology
103- [ edit ] 
104- Possible Greek relations, even if ruled out by Beekes as highly unlikely, are the verbal present form ἔθει ( éthei ) , the participle ἔθων ( éthōn , “ damaging, plaguing; pushing, tossing (?) ” ) and the nouns ἔθρις ( éthris , “ castrated ram ” ) , ἔθειρα ( étheira , “ horses' hair, mane ” ) . The lemma could be an old lengthened grade of one of the underlying roots. Compare ὄθομαι ( óthomai 
105- Taking in account Avestan 𐬬𐬁𐬛𐬁𐬌𐬌𐬋𐬌𐬝 ( vādāiiōit̰ , “ he may push back ” ) and Sanskrit अवधीत् ( ávadhīt , “ he killed ” ) (root वध् ( vadh , “ to kill, destroy (a man's ability to procreate) ” ) ), as well as Hittite [script needed] ( ḫuett- tta(ri) , “ to draw, pull ” ) , Beekes constructed a root Proto-Indo-European *h₂wedʰh₁- ( “ to push away, slay ” ) , whence an iterative *h₂wodʰh₁-éye-t
106- Pronunciation
107- [ edit ] 
108- IPA ( key ) : /ɔː.tʰé.ɔː/ → /oˈθe.o/ → /oˈθe.o/ 
109- ( 5 th BCE Attic ) IPA ( key ) : /ɔː.tʰé.ɔː/ 
110- ( 1 st CE Egyptian ) IPA ( key ) : /oˈtʰe.o/ 
=== 105daa35bdad0d89
41: Etymology 
42- 1.3 
43- Pronunciation 
44- 1.4 
45- Noun 
46- 1.4.1 
47- Declension 
48- 1.4.2 
49- Descendants 
--
94: Etymology
95- [ edit ] 
96- From ὠθέω ( ōthéō , “ to push ” ) +‎ -μός ( -mós ) .
97- Pronunciation
98- [ edit ] 
99- IPA ( key ) : /ɔːz.mós/ → /ozˈmos/ → /ozˈmos/ 
100- ( 5 th BCE Attic ) IPA ( key ) : /ɔːz.mós/ 
101- ( 1 st CE Egyptian ) IPA ( key ) : /ozˈmos/ 
102- ( 4 th CE Koine ) IPA ( key ) : /ozˈmos/ 
=== 2565da7d64f72299
39: Etymology 
40- 1.2 
41- Verb 
42- 1.2.1 
43- Derived terms 
44- 1.2.2 
45- Translations 
46- 1.3 
47- Noun 
--
130: Etymology
131- [ edit ] 
132- Back-formation from osmosis .
133- Verb
134- [ edit ] 
135- osmose ( third-person singular simple present osmoses , present participle osmosing , simple past and past participle osmosed ) 
136- ( intransitive ) To diffuse by osmosis .
137- ( transitive ) To cause to diffuse by osmosis.
138- Derived terms
=== 3785aa08e6d8ae3d
41: Etymology 
42- 1.3 
43- Pronunciation 
44- 1.4 
45- Verb 
46- 1.4.1 
47- Conjugation 
48- 1.4.2 
49- Derived terms 
--
108: Etymology
109- [ edit ] 
110- Borrowed from  English wade ,  German waten ,  Italian guadare ,  Spanish vadear . Decision no. 1335, Progreso VII .
111- Pronunciation
112- [ edit ] 
113- IPA ( key ) : /vaˈdar/ 
114- Verb
115- [ edit ] 
116- vadar ( present vadas , past vadis , future vados , conditional vadus , imperative vadez )
```


## [2026-10-16T05:16:46.555Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/osmosis\" \"https://fr.wiktionary.org/wiki/osmose\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wahsą\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wekō\" \"https://en.wiktionary.org/wiki/vēlum\" \"https://en.wiktionary.org/wiki/reveal\" \"https://en.wiktionary.org/wiki/revelo\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰh₁-\" \"https://vajehyab.com/moein/واکس\" \"https://vajehyab.com/moein/اسمز\" \"https://abadis.ir/fatofa/اسمز/\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weg-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wókso\" \"https://en.wiktionary.org/wiki/Wichse\"; do python3 tools/fetch_source.py \"$u\" --note \"page 529: Wedh 2 / Weg 1 entries\" 2>&1 | tail -1; done; grep \"page 529\" data/verification/sources/web/index.jsonl | tail -14 | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['file'],d['url'])\""
}
```


### [2026-10-16T05:16:54.229Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b266cbf73f2efdea.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/10aa22b8bedb82d1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/26b8b6cb7eb07581.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9b624f6ab7e12a3e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0282049467de711c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f00ea94fbf571f4a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6d3c6c17007b6c74.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a6f238500c05d849.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/da445095e80cc674.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f4120ac53946ddbf.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/57f5937afea74ff0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/02e338ba4c7926fb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2410cd5cece4f75.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/868dbaa1a1748ac9.txt
-1 39 data/verification/sources/web/02e338ba4c7926fb.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weg-
-1 39 data/verification/sources/web/0f72603b648ea1af.txt https://www.etymonline.com/word/veil
200 9271 data/verification/sources/web/b266cbf73f2efdea.txt https://en.wiktionary.org/wiki/osmosis
200 6066 data/verification/sources/web/10aa22b8bedb82d1.txt https://fr.wiktionary.org/wiki/osmose
200 4963 data/verification/sources/web/26b8b6cb7eb07581.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wahsą
-1 39 data/verification/sources/web/9b624f6ab7e12a3e.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wekō
-1 39 data/verification/sources/web/0282049467de711c.txt https://en.wiktionary.org/wiki/vēlum
200 12945 data/verification/sources/web/f00ea94fbf571f4a.txt https://en.wiktionary.org/wiki/reveal
200 7630 data/verification/sources/web/6d3c6c17007b6c74.txt https://en.wiktionary.org/wiki/revelo
-1 39 data/verification/sources/web/a6f238500c05d849.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰh₁-
200 524 data/verification/sources/web/da445095e80cc674.txt https://vajehyab.com/moein/واکس
-1 39 data/verification/sources/web/f4120ac53946ddbf.txt https://vajehyab.com/moein/اسمز
200 7401 data/verification/sources/web/57f5937afea74ff0.txt https://abadis.ir/fatofa/اسمز/
200 3743 data/verification/sources/web/868dbaa1a1748ac9.txt https://en.wiktionary.org/wiki/Wichse
```


## [2026-10-16T05:16:59.840Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; e(){ grep -v \"^\\s*$\" $1.txt | grep -n -i -A${2:-5} \"^ *(Etymology|Étymologie)\" -E | grep -v \"^\\S*- *[0-9.]* *$\" | head -${3:-14} | cut -c1-500; }; for f in b266cbf73f2efdea 10aa22b8bedb82d1 26b8b6cb7eb07581 5ae9e65d18cfa982 11752dac8d0a63d6 f40ede120cfda7b6 15899fe244113dc5 61c60b3cff0d0a87 7c9e0a65dbc92863 f00ea94fbf571f4a 6d3c6c17007b6c74 868dbaa1a1748ac9; do echo \"=== $f $(sed -n 1p $f.txt)\"; e $f; done; cat da445095e80cc674.txt; grep -v \"^\\s*$\" 57f5937afea74ff0.txt | grep -n -E \"اسمز|اُسمُز|معین\" | head"
}
```


### [2026-10-16T05:17:00.396Z] TOOL RESULT

```
=== b266cbf73f2efdea URL: https://en.wiktionary.org/wiki/osmosis
39: Etymology 
41- Pronunciation 
43- Noun 
54: Etymology 
56- Pronunciation 
58- Noun 
136: Etymology
137- [ edit ] 
138- From endosmose and exosmose , both coined by French physician Henri Dutrochet in 1826; from (respectively) Ancient Greek ἔνδον ( éndon , “ within ” ) and Ancient Greek ἔξω ( éxō , “ outer, external ” ) , plus Ancient Greek ὠσμός ( ōsmós , “ push, impulsion ” ) , from ὠθέω ( ōthéō ) .
139- Pronunciation
140- [ edit ] 
141- enPR : ŏz-mōˈ -sĭs , ŏs- 
230: Etymology
231- [ edit ] 
=== 10aa22b8bedb82d1 URL: https://fr.wiktionary.org/wiki/osmose
49: Étymologie 
51- Nom commun 
53- Synonymes 
122: Étymologie 
123- [ modifier le wikicode ] 
124- ( 1865 ) De l’ anglais osmosis [ 1 ] , créé en 1854 par le chimiste Thomas Graham en s'inspirant de endosmose et exosmose , formés à partir du grec ancien ὠσμός , ôsmos («   poussée   ») . 
125- Nom commun 
126- [ modifier le wikicode ] 
127- Singulier Pluriel 
=== 26b8b6cb7eb07581 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wahsą
39: Etymology 
41- Pronunciation 
43- Noun 
85: Etymology
86- [ edit ] 
87- Of somewhat disputed origin. Cognate with Proto-Balto-Slavic *wáśkan ( “ wax ” ) , from Proto-Indo-European *woḱso ( “ idem ” ) , [ 1 ] which was originally reconstructed by Pokorny as *wokso , *wos-ko- . [ 2 ] However, others have compared the terms with Latin velum ( “ sailcloth ” ) and Dutch wiek ( “ windmill sail ” ) , from *weg- ( “ to weave ” ) (though the semantic link appears tenuous). [ 3 ] The Germanic and Balto-Slavic terms could instead be from a pre-Indo-European substrate .
88- Pronunciation
89- [ edit ] 
90- IPA ( key ) : /ˈwɑx.sɑ̃/ 
=== 5ae9e65d18cfa982 URL: https://en.wiktionary.org/wiki/wax
39: Etymology 
41- Symbol 
43- See also 
50: Etymology 1 
52- Noun 
54- Derived terms 
70: Etymology 2 
72- Verb 
74- Derived terms 
80: Etymology 3 
82- Verb 
84- Usage notes 
98: Etymology 4 
100- Noun 
=== 11752dac8d0a63d6 URL: https://en.wiktionary.org/wiki/wick
41: Etymology 1 
43- Noun 
45- Derived terms 
57: Etymology 2 
59- Noun 
61- Usage notes 
69: Etymology 3 
71- Adjective 
73- Related terms 
79: Etymology 4 
81- Noun 
83- Translations 
85: Etymology 5 
87- Noun 
=== f40ede120cfda7b6 URL: https://en.wiktionary.org/wiki/вакса
46: Etymology 
48- Pronunciation 
50- Noun 
57: Etymology 
59- Pronunciation 
61- Noun 
127: Etymology
128- [ edit ] 
129- From Proto-Tungusic *ŋiaksa .
130- Pronunciation
131- [ edit ] 
132- IPA ( key ) : /waːksa/ 
143: Etymology
144- [ edit ] 
=== 15899fe244113dc5 URL: https://en.wiktionary.org/wiki/واکس
39: Etymology 
41- Noun 
43- Derived terms 
87: Etymology
88- [ edit ] 
89- From Russian ва́кса ( váksa ) , from German Wachs .
90- Noun
91- [ edit ] 
92- واکس • ( vâks ) ( plural واکس‌ها ) 
=== 61c60b3cff0d0a87 URL: https://en.wiktionary.org/wiki/velum
39: Etymology 
41- Pronunciation 
43- Noun 
63: Etymology 
65- Pronunciation 
67- Noun 
74: Etymology 1 
76- Pronunciation 
78- Noun 
80: Etymology 2 
82- Pronunciation 
84- Noun 
91: Etymology 
93- Pronunciation 
=== 7c9e0a65dbc92863 URL: https://en.wiktionary.org/wiki/veil
39: Etymology 
41- Pronunciation 
43- Noun 
60: Etymology 
62- Pronunciation 
64- Verb 
150: Etymology
151- [ edit ] 
152- From Middle English veil , veyl , from Anglo-Norman and Old Northern French veil ( “ sail, veil, shroud ” ) ( Francien Old French voil , French voile ), Latin vēlum ( “ cloth, covering ” ) . Displaced Middle English scleire , scleyre , sleyre , slyre ( “ veil ” ) (compare German Schleier ). Doublet of velum and voile .
153- Pronunciation
154- [ edit ] 
155- ( Received Pronunciation , General American ) IPA ( key ) : /veɪl/ 
380: Etymology
381- [ edit ] 
=== f00ea94fbf571f4a URL: https://en.wiktionary.org/wiki/reveal
39: Etymology 
41- Pronunciation 
43- Noun 
144: Etymology
145- [ edit ] 
146- From Middle English revēlen , from Old French reveler , from Latin revēlāre ( “ to reveal, uncover ” ) , from re- ( “ back, again ” ) + vēlāre ( “ to cover ” ) , from vēlum ( “ a cloth, covering, curtain, veil, awning, sail ” ) (whence also English veil , English unveil , English voile , Russian вуаль ( vualʹ ) , Russian завуали́ровать ( zavualírovatʹ , “ to veil ” ) (compare typologically)).
147- Also compare typologically English uncloak , dismantle , divest , invest , unmask , Russian разобла́чать ( razobláčatʹ ) (akin to облаче́ние ( oblačénije ) , срыва́ть покро́вы ( sryvátʹ pokróvy ) ( покро́в ( pokróv , “ cover, covering ” ) ).
148- Pronunciation
149- [ edit ] 
=== 6d3c6c17007b6c74 URL: https://en.wiktionary.org/wiki/revelo
44: Etymology 
46- Pronunciation 
48- Verb 
121: Etymology
122- [ edit ] 
123: Etymology tree
124- Proto-Italic *wre- 
125- Latin re- 
126- Proto-Indo-European *weg- 
127- Proto-Indo-European *wegslom der. ? 
128- Proto-Indo-European *weǵʰ- der. ? 
=== 868dbaa1a1748ac9 URL: https://en.wiktionary.org/wiki/Wichse
39: Etymology 
41- Pronunciation 
43- Noun 
93: Etymology
94- [ edit ] 
95- In the sense “polish” an 18th-century back-formation from wichsen ( “ to polish ” ) , from a variant of wachsen ( “ to wax ” ) . The former verb then developed the sense “to wank, masturbate (of a male)” based on the back-and-forth movement. The noun sense “cum, semen” thence, but plausibly reinforced by the already existing sense of the noun.
96- Pronunciation
97- [ edit ] 
98- IPA ( key ) : /ˈvɪksə/ , [ˈvɪksə] , [ˈʋɪksə] 
URL: https://vajehyab.com/moein/واکس
FETCHED: 2026-10-16T05:16:51Z
STATUS: 200
TITLE: معنی واکس | فرهنگ انتشارات معین | واژه یاب

معنی واکس | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 واکس

 فرهنگ انتشارات معین
 [ روس . ] (اِ.) مادة چربی که رنگ های مختلف دارد و رویة کفش را با آن تمیز و براق کنند.
 واکس در فرهنگ‌های دیگر
 معنی واکس در لغت‌نامه دهخدا 
 معنی واکس در فرهنگ فارسی عمید / قربان‌زاده 
 معنی واکس در دیکشنری فارسی به انگلیسی 
 واژه‌های مشابه
 واکسن 
 واکسیل 
 واکسیناسیون 
 واکسینه 
 وابسته 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید1:URL: https://abadis.ir/fatofa/اسمز/
4:TITLE: اسمز - معنی در دیکشنری آبادیس
5:اسمز - معنی در دیکشنری آبادیس 
7: اسمز
14: اُسمُز یا گذرندگی[ ۱] ( به فرانسوی: Osmose ) به فرایندی گفته می شود که طی آن حلال از طریق یک غشای نیمه تراوا از جایی که محلول رقیق تر است به جایی که محلول غلیظ تر است، نفوذ می کند. [ ۲] عبور آب از غشای تراوائی نسبی را اسمز می گویند که حرکت از ناحیه رقیق به غلیظ است. در اسمز برای جابجایی انرژی مصرف نمی شود. برای مثال: هنگامی که در یک شاخه ی ظروف مرتبط، آب خالص و در شاخه دیگر محلول آب و شکر و بین آنها غشای تراوائی نسبی وجود داشته باشد، به طوری که حجم مواد در دو شاخه ظرف یکسان باشد، آب از ناحیه رقیق ( آب خالص ) به ناحیه غلیظ ( محلول آب و شکر ) حرکت می کند. 
15:اسمز، حرکت و جنبش خود به خودی مولکول های حلال در میان بخشی از غشای نفوذپذیر به درون منطقه ای از غلظت بیشتر مواد حل شونده در جهتی که تمایل به تعادل مواد حل شونده در هر دو طرف وجود دارد. احتمالاً برای توصیف یک فرایند فیزیکی استفاده می شود که هرگونه حلالی به در جریان غشا ی نیمه نفوذ پذیر حرکت می کند ( نسبت به حلال نفوذ پذیر می باشد، اما نسبت به مواد حل شونده نفوذ پذیر نمی باشد ) دو تا حلال را با غلظت های متفاوت از هم جدا می کند. اسمز می تواند برای انجام کار صورت گیرد. [ ۳] 
16:در مورد عمل «اسمز» جریان مخلوط شدن از راه جدارهای نازک ریشه های ظریف مویی یک گیاه یا جدارهای روده در حیوانات انجام می گیرد. 
17:غشاء جدارهای مزبور عمل مخلوط شدن را کند می کند ولی هرگز آن را متوقف نمی کند. در بدن جانداران، هنگام فعالیت اسمز، غشاهای مذکور اجازه می دهند که فقط مواد خاصی از آن ها عبور کنند و مواد دیگر را متوقف می سازند. این عمل تا اندازه ای مربوط به ساختار نوع ماده ای است که با آن تماس پیدا می کند. مواد محلول هنگام تماس با غشاء به آن فشار وارد می کند و این فشار را، فشار اسمُزی می نامند. 
19:فشار اسمُزی به صورت حداقل فشار مورد نیاز تعادل و بدون هیچ جنبشی ( حرکت ) حلال در شبکه تعریف می شود. فشار اسمُزی یک ویژگی اتصال ( خاصیت جمعی ) می باشد به این معنی که فشار اسمُزی وابسته به غلظت مولی مواد حل شونده می باشد اما وابسته به هویت آن نمی باشد. اسمز یک فرایند حیاتی در سیستم های بیولوژی می باشد، غشای بیولوژیکی نیمه نفوذپذیری می باشد. در حالت کلی، این غشاها نسبت به ملوکول های قطبی و بزرگ مانند یون ها، پروتئین ها و پلی ساکاریدها، نشت ناپذیر ( نفوذ ناپذیر ) می باشند، در حالیکه نفوذ پذیری نسبت به ملوکول های غیر قطبی یا آب گریز مانند لیپیدها، و همچنین ملوکول های کوچک مانند اکسیژن، دی اکسید کربن، نیتروژن و اکسید نیتریک وجود دارد. نفوذ پذیری وابسته به قابلت حل بار یا شیمی و همچنین اندازه مواد حل شونده می باشد ملوکول های آب از طریق غشای پلاسما غشای تونوپلاسم یا پورتو پلاست به وسیله انتشار فسفودپیت های دولایه از طریق آکوپورنیس حرکت می کند ( پروتئین های عبورکننده از غشا که کوچک می باشند مشابه با کانال های یونی وانتشار تسهیل شده می باشند ) اسمز ابزارهای اولیه را ایجاد می کند که آب را به داخل و خارج سلول ها انتقال می دهد. فشار تورگور یک سلول عمدتاً به وسیله فرایند اسمُزی بین سلول های داخلی و محیط هیپوتونیک نسبی حفظ می شود . 
20: wiki: اسمز
```


## [2026-10-16T05:17:05.607Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v \"^\\s*$\" f40ede120cfda7b6.txt | sed -n 140,150p | cut -c1-400; grep -v \"^\\s*$\" 5ae9e65d18cfa982.txt | grep -n -A3 \"Etymology 1$\" | cut -c1-900 | sed -n 1,12p; grep -v \"^\\s*$\" 11752dac8d0a63d6.txt | grep -n -A3 \"Etymology 1$\" | cut -c1-900 | head -12"
}
```


### [2026-10-16T05:17:05.916Z] TOOL RESULT

```
 S. N. Onenko ( 1980 ), “ вакса ”, in V. A. Avrorina, editor, Нанайско-русский словарь [ Nanai-Russian dictionary ], Moscow : Издательство «Русский Язык» 
 Russian
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from German Wachs .
 Pronunciation
 [ edit ] 
 IPA ( key ) : [ˈvaksə] 
 Audio ( Moscow ) : ( file ) 
 Noun
283: Etymology 1
284- [ edit ] 
285- From Middle English wax , from Old English weax , from Proto-Germanic *wahsą , possibly from Proto-Indo-European *woḱ-so- . 
286- Cognate with Saterland Frisian Woaks ( “ wax ” ) , West Frisian waaks ( “ wax ” ) , Dutch was ( “ wax ” ) , German Wachs ( “ wax ” ) , German Low German Wass ( “ wax ” ) , Luxembourgish Wuess ( “ wax ” ) , Vilamovian wāhs ( “ wax ” ) , Danish , Norwegian Bokmål , Norwegian Nynorsk voks ( “ wax ” ) , Faroese vaks ( “ wax ” ) , Icelandic , Swedish vax ( “ wax ” ) ; and with Lithuanian vaškas ( “ wax ” ) , Proto-Slavic *voskъ ( “ wax ” ) .
--
1016: Etymology 1
1017- [ edit ] 
1018- From Old English weax , from Proto-West Germanic *wahs , from Proto-Germanic *wahsą .
1019- Alternative forms
240: Etymology 1
241- [ edit ] 
242- The noun is derived from Middle English wek , weke , wicke ( “ fibrous cord drawing fuel to flame of a candle, etc.; material used to make this object ” ) , [ 1 ] from Old English wēoce ( “ wick ” ) , [ 2 ] from Proto-West Germanic *weukā ( “ flax bundle; wick ” ) , possibly from Proto-Indo-European *weg- ( “ to weave ” ) . [ 3 ] [ 4 ] [ 5 ] 
243- It has been suggested that noun noun sense 2 (“penis”) is derived from Hampton Wick , used as rhyming slang for prick . [ 3 ] If so, that sense should be placed under etymology 2 .
```


## [2026-10-16T05:17:10.871Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v \"^\\s*$\" 61c60b3cff0d0a87.txt | grep -n -i -B2 -A4 \"Latin\" | grep -i -E \"From|PIE|Proto|weg|vehō\" | cut -c1-700 | head -10"
}
```


### [2026-10-16T05:17:11.343Z] TOOL RESULT

```
181- Proto-Indo-European *weǵʰ- der. ? 
182- Proto-Italic *wekslom 
185: Borrowed from Latin vēlum ( “ a cloth, covering, awning, curtain, veil ” ) . Doublet of veil .
231: Learned borrowing from Latin vēlum ( “ veil, sail ” ) .
247: Learned borrowing from Latin vēlum .
260: From English vellum , from Old French velin (Modern French vélin ), from Latin vitulinus ( “ of a calf ” ) .
283- Proto-Indo-European *weǵʰ- der. ? 
284- Proto-Italic *wekslom 
286: From Proto-Italic *wekslom ( note the Latin term's diminutive form vēxillum , as in pālus > pāxillus ), which lends credence to this reconstruction ) , with two competing theories:
287- From Proto-Indo-European *wegslom , from *weg- ( “ to weave, bind ” ) . Cognate with English wick , Welsh gweu ( “ to weave ” ) . [ 1 ]
```


## [2026-10-16T05:17:14.185Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v \"^\\s*$\" 61c60b3cff0d0a87.txt | sed -n 286,292p | cut -c1-600; grep -v \"^\\s*$\" 40b6f1ac92b2b2dc.txt | sed -n 105p"
}
```


### [2026-10-16T05:17:14.544Z] TOOL RESULT

```
 From Proto-Italic *wekslom ( note the Latin term's diminutive form vēxillum , as in pālus > pāxillus ), which lends credence to this reconstruction ) , with two competing theories:
 From Proto-Indo-European *wegslom , from *weg- ( “ to weave, bind ” ) . Cognate with English wick , Welsh gweu ( “ to weave ” ) . [ 1 ] 
 Others refer it to *weǵʰ- ( “ to ride ” ) , thus "that which propels"; in this case, cognate with Proto-Slavic *veslo ( “ oar ” ) . This is semantically less attractive than the above theory.
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [ˈweː.ɫũː] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈvɛː.lum] 
 Taking in account Avestan 𐬬𐬁𐬛𐬁𐬌𐬌𐬋𐬌𐬝 ( vādāiiōit̰ , “ he may push back ” ) and Sanskrit अवधीत् ( ávadhīt , “ he killed ” ) (root वध् ( vadh , “ to kill, destroy (a man's ability to procreate) ” ) ), as well as Hittite [script needed] ( ḫuett- tta(ri) , “ to draw, pull ” ) , Beekes constructed a root Proto-Indo-European *h₂wedʰh₁- ( “ to push away, slay ” ) , whence an iterative *h₂wodʰh₁-éye-ti . [ 1 ] Mark that also ἔθρις ( éthris ) seems to be cognate to Sanskrit वध्रि ( vádhri , “ castrated ” ) .
```


## [2026-10-16T05:17:43.761Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^os.?mo.?sis|^os'mose|^os-mose|osmose, n|os.mo.sis\" FSD_vol3.txt | head -5; grep -n -i -E \"^(veil|wax|wick)\\b\" FSD_vol4.txt | head -5"
}
```


### [2026-10-16T05:17:44.101Z] TOOL RESULT

```
47169:veil
51563:wax*,  Iwaks,  2wSks,  r   I.f  Tocontwith  wax,  treat  with wax  or  apply  wax  to  for  any  purpose,  as,  to  wax  a   floor Old  furniture  was  vaxed  till  it  shone  like  a   mirror
51569:wax’,  tf  [Colloql  To  beat  thoroughly  gain  a   decisive  victory ov  er.  as,  we  wlU  wax  them
51570:wax,  n   1.  A   yellow  fatty  sobd  of  ammal  ongm,  excreted by  bees  from  the  abdominal  rings  beeswax.  Ithasahoney- llke  odor  and  a   balsamic  taste,  becomes  plastic  with  the  heat of  the  hand,  has  a   specific  gravity  of  0   951  to  0   9G0  at  25®  C   , and  a   melting-point  of  62®  to  64®  C   is  insoluble  in  water, but  Is  almost  completely  dl^lved  by*  boUlng  alcohol  Its principal  components  arc  cerotic  acid  (C^HwOi)  and  myrlcll palmltate  (C*)Hu  Ci#H«Or)  In  Its  crude  or  honey  comb form  it  Is  known  as  yeliow  wax.  White  wax  Is  prepared from  yellow  wax  by  roUing  the  latter  Into  strips  of  thin  bull", moistening,  and  leaving  It  to  the  action  of  air  and  light  The principal  uses  of  beeswax  are  for  modeling,  making  candles, pharmaceuticals,  and  surgical  dressings 2   Any  of  several  substances  of  wax-like  appearance  and consistency  Specif  (1)  Chem  Any  wax-forming  ester The  trores  are  dietin^uisbed  from  the  fats  m   that  they  consist of  esters  of  xnonobydne  alcohols  with  hiirh  molecular  weicht, trberess  the  fats  are  the  esters  of  the  tnbjdnc  edcohol  glycerol. Spermaceti  helonss  to  the  wax  vanct>
51574:wax-scale,  especially  the  Chinese  Erieerus  pela,  furnishing Chlnesewax  Otherspeciesof  Cocrfdaandmanyof  the  ApM- dldx  also  secrete  wax  2.  One  of  various  East-IndJan  fulgor- Ids,  especially  of  thegenusLyrfra,  that  secrete  waxen  thinaidB from  the  abdomen  —   wanUght,  n   A   candle,  taper,  or  the like,  made  of  wax  —   wax*modellng,  n   The  act  or  process of  shaping  figures  in  wax,  ceroplasty  —   wax»moth,  n   A bee-moth  or  galerlld  —   wax*  or  candleberry  smyTtle,  n   A shrub  or  small  tree  (Myrica  cerifera)  that  grows  from  Nova Scotia  to  Florida  and  along  the  Great  Lakes,  with  fragrant leaves,  resinous-dotted,  and  nuts  covered  with  white  wax, which  fs  often  used  for  making  candles  — wax  opal,  a   va- riety of  opal  with  a   wax-llke  luster.—  wax*paintlng,  n   En- caustic painting  See  encaustic  —   wax*palm,  n   Either  of two  South-American  palms  (Ceroxylon  andieota  and  Coper” nicia  cerifera)  y   lelding  wax  The  former  has  a   lofty  straight trunk,  a   foot  In  diameter,  covered  with  a   whitish  waxy  resin- ous substance,  which  by  mixing  with  tallow  makes  excellent candles  The  other  tree  Is  the  Brazilian  wax-palm,  from which  the  wax  attached  to  the  young  leaves  Is  obtained  by shaking  and  beating  It  Is  exported  under  the  name  of Brazil  wax  or  carnauba,  for  use  In  making  candles  — wax* paper,  n   Paper  made  Impermeable  to  water  by  coating  or saturating  it  with  wax  waxed  paperf.— wax»plne,  n Any  tree  of  the  genus  Dammara  that  exudes  resin  —   wax* plant,  n   Any  one  of  various  plants  so  called  from  the  wax- llke  appearance  of  the  flowers  or  leaves  or  both  Specif  (1) Any  species  of  Boya  See  Hota  (2)  Any  one  of  several  be- gonias (3)  One  of  the  honeyworts  {Cerinihe  major)  See HOKEYWORT,  Under  honey  (4)  The  IndJan-pIpe  — wax* pocket,  n   One  of  the  eight  depositories  under  the  rings  on the  under  side  of  the  abdomen  of  a   worker  bee  In  which wax-scales  are  secreted  —   wax  polish,  a   paste  consisting  of wax  and  other  Ingredients,  used  to  produce  a   glistening  sur- face on  wood,  especially  on  floors  —   wax  process,  cerotype process —   wax »red,  a   Bright-red  like  sealing-wax— wax* scale,  n   1.  One  of  the  plates  of  wax  secreted  In  the wax-pocket  of  a   worker  bee  2.  A   coecid  wax-insect  The Florida  wax-scale  Is  Ceroplastes  floridensis;  the  Indian wax-scale  Is  C   cerf/’erus  — wax'seotf,  n   A   parish  ta-x for  furnishing  wax  candles  to  a   church  — wax'StItched,  a Stitched  with  waxed  thread  —   wax  wall  (Mining),  a   clay wall  —   wax*worm,  n   The  larva  of  a   wax-moth —wax* yellow,  n   The  color  of  natural  beeswax  —   white  wax,  any wax  of  a   white  color  Specif  (1)  See  Wax,  t»  ,   1.  (2) Chinese  wax  —   >   ellow  wax,  see  wax.  n   1 Wax"a-hach'Ie,  1   woks'e-badh'i  2   w^ks'a-hfich'l  n   A town  county-seat  of  Ellis  county,  Texas  seat  of  Trinity University  (Presbyterian),  founded  In  1869 wax'bep"ry,  1   waksTier  i   2   w&ks'b6r*y,  n   [-ries,  1   -iz,  2   -if, pi  1   The  bayberry  or  Its  fruit
```


## [2026-10-16T05:19:58.157Z] TOOL CALL #49: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-529.json",
 "content": "{\n  \"pdf_page\": 529,\n  \"book_page\": 499,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Wedh 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *wedʰ- 'to push, strike' (Pokorny 1. u̯edh- 1115; Beekes *h₂wedʰh₁- 'push away, slay')\",\n      \"note\": \"Pokorny's first u̯edh- 'to push, hit' (p. 1115, = WP I 254 f.) groups exactly Skt. vadhati/avadhīt 'strike, kill', Av. vada- 'wedge', vadar- 'weapon', vādāya- 'push back', Gk. ōthéō 'push'. AHD wedh- 'To push, strike ... Greek ōthein, to push: osmosis' gives the same set. Modern work (Beekes, via Wiktionary s.v. ὠθέω) reconstructs it with laryngeals as *h₂wedʰh₁-; this is the root Nourai means. It must not be confused with the homophonous *wedʰ- 'to lead, marry' (Pokorny 2. u̯edh-), which Wiktionary's *wedʰ- page treats; Nourai's '2' is his own numbering. Root, label and gloss are correct. The only soft points on the page are the gloss 'ax' for Av. vaδaγan- (attested only as a proper name) and the French link, since French osmose (1865) was taken from English osmosis rather than the other way round.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wedʰ- «هل دادن، زدن» (نزد پوکورنی 1. u̯edh-، ص ۱۱۱۵؛ بیکس با لارنگال‌ها *h₂wedʰh₁- «پس زدن، کشتن») است. سنسکریت vadhati «زدن، کشتن»، اوستایی vada- «گُوه»، vadar- «جنگ‌افزار» و vādāya- «پس راندن» و یونانی ōthéō «هل دادن» همه از آن‌اند. نباید آن را با *wedʰ- دیگر به معنای «بردن، زن گرفتن» یکی گرفت. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/ὠθέω\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1115\", \"status\": \"supports\", \"note\": \"POK_full.txt line 88773 'Root / lemma: ued^-1 / Meaning: to push, hit / Material: Old Indie vadhati ... = Avestan vada- m. \\\"wedge zum Spalten des Holzes\\\", ... vadar- n. \\\"weapon (for hitting)\\\", ... Avestan vādaya- 'zurückstoßen' (lengthened grade as gr. ὠθέω) ... ὠθέω \\\"poke, push\\\"' ... 'Page(s):1115'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 254 (WLD_Bd1_pages.txt leaf 263)\", \"stance\": \"supports\", \"note\": \"'1. uedh- „stoßen, schlagen“. Ai. vadhati ... av. vada- m. „Keil zum Spalten des Holzes“ ... av. vadar- n. „Waffe (zum Schlagen)“, av. vādaya- „zurückstoßen“ (dehnstufig wie gr. ὠθέω)'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1129\", \"stance\": \"supports\", \"note\": \"'wedh-. To push, strike. Suffixed lengthened o-grade form *wōdh-eyo- in Greek ōthein, to push: osmosis. [Pok. 1. uedh- 1115.]'\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 19814, uedh- (4)\", \"stance\": \"partial\", \"note\": \"Mann lists 'uedh- (4) \\\"fight\\\" ... Hes. cf. éthon ... \\\"striking\\\"; (alleged) étho, v. tr. \\\"strike\\\"' but does not cite ōthéō or the Avestan words; uedh- (1)/(2) are the 'marry/lead' roots.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"vâdâya; vada; vadar; vadhğan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Gathic vādāya- 'to push back, keep off' (Y. 29.2 vādāyōit̰) is a causative-iterative with lengthened o-grade *wōdʰ-éye- (< *h₂wodʰh₁-éye-), the exact formal match of Greek ōthéō. Young Av. vada- m. 'wedge for splitting wood' (V. 14.7) = Skt. vadhá- 'deadly weapon', and vadar- n. 'weapon for striking' (Y. 32.10, 9.30) = Skt. vádhar- 'Indra's weapon'; both are regular *wedʰ-o-/*wedʰ-r̥ with Iranian dʰ > d. vaδaγan- (Nourai's vadhğan) is attested only as the name of a prince hostile to the faith (V. 19.6), identified with Aži Dahāka in Pahlavi texts. Bartholomae marks its meaning 'Eig. Bed.?' and Pokorny only asks whether it means 'axe, striker', so the gloss 'ax' is a guess. The first three words are confirmed, vadhğan 'ax' only plausible.\",\n          \"derivation_fa\": \"اوستایی گاهانی vādāya- «پس راندن، دور داشتن» ستاک سببی با بالاندِ کشیدهٔ o (*wōdʰ-éye-) است و همتای دقیق یونانی ōthéō. اوستایی نو vada- «گُوهِ هیزم‌شکنی» و vadar- «جنگ‌افزار زدنی» با سنسکریت vadhá- و vádhar- هم‌ریشه‌اند و dʰ هندواروپایی در ایرانی d شده است. اما vaδaγan- تنها نام شاهی دین‌ستیز (یکی با ضحاک در متون پهلوی) است. بارتولومه معنایش را نامعلوم می‌داند و پوکورنی فقط می‌پرسد که آیا «تبر، زننده» است. پس سه واژهٔ نخست درست‌اند و معنای «تبر» برای vadhğan حدسی و با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ὠθέω\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1115\", \"status\": \"supports\", \"note\": \"POK_full.txt line 88773ff.: 'Avestan vada- m. \\\"wedge zum Spalten des Holzes\\\", ... vadar- n. \\\"weapon (for hitting)\\\", ... Avestan vādaya- \\\"zurückstoßen\\\" ... is also Avestan vadayan- \\\"EN eines glaubensfeindlichen Fürsten\\\" as \\\"axe, Schläger\\\" to deuten?' Supports the first three words; for vadhğan Pokorny only asks the question.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 1344-1346 (BRT.txt lines ~22405-22423) and s.v. vādāya- (line 23478)\", \"stance\": \"partial\", \"note\": \"'vada- m. \\\"Keil\\\" zum Spalten des Holzes V. 14.7'; 'vadar- n. \\\"Waffe (zum Schlagen)\\\" ... Vgl. vada- und vādāya-; ai. vádhar-'; 'vādāya- ... \\\"zurückstoßen, -drängen, fernhalten\\\" Y. 29.2'; but 'vaδaγan- m. EN. eines glaubensfeindlichen Fürsten ... Eig. Bed.?', so no meaning 'axe'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I pp. 254-255 (leaves 263-264)\", \"stance\": \"partial\", \"note\": \"'av. vada- m. „Keil zum Spalten des Holzes“ ... vadar- n. „Waffe (zum Schlagen)“, av. vādaya- „zurückstoßen“'; leaf 264: 'ist auch av. vadayan- „EN eines glaubens[feindlichen Fürsten]“ ...' given only as a question.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"ôthein; ôsmos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ὠθεῖν ōthein (pres. ὠθέω) 'to push, thrust' continues the lengthened o-grade iterative *wōdʰ-éye- (Beekes *h₂wodʰh₁-éye-). The *w- was lost in Attic-Ionic, though Hesychius and the old aorist ἔωσα show it, and PIE *dʰ became Greek th. ὠσμός ōsmós 'a push, thrust, impulse' is the action noun in -μός, with *-th-m- > -sm-. The gloss 'of liquids' reflects the modern scientific use (osmosis), not the ancient meaning.\",\n          \"derivation_fa\": \"یونانی ōthéō (مصدر ōthein) «هل دادن، راندن» از بالاندِ کشیدهٔ o ریشه (*wōdʰ-éye-) است. w آغازی در یونانی آتیک-ایونی افتاده و dʰ هندواروپایی در یونانی th شده است. ōsmós «ضربه، رانش» اسم کنش با پسوند -μός است که در آن -th-m- به -sm- بدل شده. قید «مایعات» معنای علمی امروزی است، نه معنای یونانی باستان. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ὠθέω\",\n            \"https://en.wiktionary.org/wiki/ὠσμός\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1115\", \"status\": \"supports\", \"note\": \"POK_full.txt line 88773ff.: 'ὠθέω \\\"poke, push\\\" (: Avestan vadaya-), ὠσμός \\\"shove\\\", ἔνοσις \\\"tremor\\\" (*en-wodʰ-tis)'.\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1129: 'Suffixed lengthened o-grade form *wōdh-eyo- in Greek ōthein, to push: osmosis.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 254 (leaf 263)\", \"stance\": \"supports\", \"note\": \"'av. vādaya- „zurückstoßen“ (dehnstufig wie gr. ὠθέω) ... hom. ἔθων „stoßend, zerwühlend“'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 588 (~p. 1100), line 26678 s.v. osmosis\", \"stance\": \"supports\", \"note\": \"'Gk. ὠσμός, \\\"a thrusting, impulse\\\", from the stem of ὠθεῖν, \\\"to thrust, push\\\", which is rel. to ἔνοσις, \\\"shaking, quake\\\", fr. I.-E. base *wedh-, \\\"to strike\\\"'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 19814\", \"stance\": \"silent\", \"note\": \"Mann's uedh- (4) 'fight' cites only Hes. éthon 'striking'; ōthéō and ōsmós are not listed (grep 'ōthé|ōsmó' gives nothing).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"This is an empty pass-through box. No classical or medieval Latin word lies between Greek ōsmós and the modern words. 'osmosis' is a Neo-Latin scientific coinage, made by Thomas Graham in 1854 from ōsmós plus the Greek-Latin suffix -osis and modelled on Dutrochet's French endosmose/exosmose (1826). The box is acceptable only in the sense of 'scientific (Neo-)Latin'.\",\n          \"derivation_fa\": \"این خانه خالی و گذرگاهی است. میان یونانی ōsmós و واژه‌های امروزی هیچ واژهٔ لاتین کلاسیک یا میانه نیست. osmosis ساختهٔ لاتین علمی نو است که توماس گراهام در ۱۸۵۴ از ōsmós و پسوند -osis، به الگوی endosmose و exosmose فرانسوی دوترشه (۱۸۲۶)، ساخت. تنها به معنای «لاتین علمی» پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/osmosis\",\n            \"https://fr.wiktionary.org/wiki/osmose\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited for this pass-through box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 588 (~p. 1100), line 26678\", \"stance\": \"supports\", \"note\": \"'osmosis, n. ... — ModL., formed with suff. -osis fr. Gk. ὠσμός'. This supports a Modern Latin, not classical, intermediate.\"},\n            {\"src\": \"AHD\", \"where\": \"line 1129\", \"stance\": \"silent\", \"note\": \"Goes straight from Greek ōthein to English OSMOSIS, with no Latin stage named.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"osmose\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French osmose 'osmosis' is real. Its history goes the other way from the chart's Latin → French → English order. Dutrochet coined endosmose and exosmose in French in 1826 from Greek ōsmós. Graham then made English/Neo-Latin osmosis in 1854, and the simple French osmose is recorded from 1865 as a borrowing of English osmosis, influenced by Dutrochet's compounds (TLFi via fr.wiktionary). So osmose does go back to Greek ōsmós, but through the scientific coinages rather than through a Latin word.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی osmose درست است، اما تاریخش واژگونهٔ ترتیب نمودار است. دوترشه در ۱۸۲۶ endosmose و exosmose را از یونانی ōsmós ساخت. گراهام در ۱۸۵۴ osmosis انگلیسی و لاتین علمی را ساخت، و osmose ساده در فرانسوی از ۱۸۶۵ دیده می‌شود و وام‌واژه‌ای از osmosis انگلیسی است. پس پیوند با ōsmós درست است، ولی راه آن از لاتین نمی‌گذرد. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://fr.wiktionary.org/wiki/osmose\",\n            \"https://en.wiktionary.org/wiki/osmosis\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1100\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 588 (pages ~1100-1101; leaf 590 shows '1103'), line 26677-8: 'osmose, tr. v., to subject to osmosis ... — Back formation fr. osmosis' and 'osmosis ... ModL., formed with suff. -osis fr. Gk. ὠσμός'. The page and the Greek etymon match, but Klein's osmose is the English back-formed verb, not French osmose.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FSD\", \"where\": \"FSD_vol3.txt line 36768\", \"stance\": \"partial\", \"note\": \"Shows 'experiments on osmose' (osmose as the older English/French name of the process); no etymology given in the OCR line.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt grep 'osmos'\", \"stance\": \"silent\", \"note\": \"No entry for osmosis/osmose.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"osmoz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian اُسمُز osmoz 'osmosis' (adj. اسمزی osmozi 'osmotic') is a 20th-century scientific loan from French osmose. Persian school and scientific terminology mostly took French forms, and Persian renders final French -ose /oːz/ as -oz. The Academy's equivalent is گذرندگی. The Persian Wikipedia text quoted on Abadis gives it as 'اُسمُز یا گذرندگی (به فرانسوی: Osmose)'.\",\n          \"derivation_fa\": \"«اُسمُز» (و صفت «اسمزی») وام‌واژهٔ علمی سدهٔ بیستم از فرانسوی osmose است. اصطلاحات علمی و درسی فارسی بیشتر از فرانسوی گرفته شده‌اند و -ose فرانسوی در فارسی -oz شده است. برابرنهادهٔ فرهنگستان «گذرندگی» است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/اسمز/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:52\", \"status\": \"not_checked\", \"note\": \"Moshiri's Farhang-e Vazheha-ye Orupayi dar Farsi is not available online or on disk (refs_online.json: kind 'none').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt (2-vol Adena abridgement), grep 'اسمز'\", \"stance\": \"silent\", \"note\": \"Only 'اسمر: [ع.] (ص.) گندم‌گون' found; no اسمز entry in the abridgement. vajehyab.com/moein/اسمز did not load (status -1).\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt grep 'اسمز'\", \"stance\": \"silent\", \"note\": \"Aryanpur covers only inherited IE vocabulary; no entry.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"osmosis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English osmosis (1854, Thomas Graham) is a Neo-Latin formation from Greek ōsmós 'push, impulse' + -osis. It abstracts the earlier endosmose/exosmose (Dutrochet 1826, anglicized endosmosis/exosmosis), and its sense is the passage of a solvent through a semi-permeable membrane. The back-formed verb osmose followed.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی osmosis را توماس گراهام در ۱۸۵۴ از یونانی ōsmós «رانش» و پسوند -osis، به لاتین علمی، ساخت. این واژه از endosmose و exosmose دوترشه (۱۸۲۶) برگرفته شده است و معنای آن گذر حلال از غشای نیم‌تراواست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/osmosis\",\n            \"https://en.wiktionary.org/wiki/osmose\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1129: 'wedh-. To push, strike. ... Greek ōthein, to push: osmosis.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 588 (~p. 1100), line 26678\", \"stance\": \"supports\", \"note\": \"'osmosis, n., intermixture of two fluids separated by a porous membrane. — ModL., formed with suff. -osis fr. Gk. ὠσμός ... fr. I.-E. base *wedh-, \\\"to strike\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt grep 'osmos'\", \"stance\": \"silent\", \"note\": \"Not in Skeat's Concise dictionary.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Weg 1 / Wokso\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *weg- 'to weave, bind' (Pokorny 1117) and *wokso- / *woḱso- 'wax' (Pokorny 1180)\",\n      \"note\": \"Both roots are real and correctly glossed. Pokorny treats them as two lemmata, ueg- 'to weave, bind' (1117-1118, with Latin vēlum, OE wēoce 'wick', 'See also: here uokso- \\\"wax\\\"') and uokso- 'wax' (1180). He links them only tentatively ('to *ueg- \\\"to weave\\\", as OHG wabo \\\"honeycomb\\\" to *uebʰ- \\\"to weave\\\"', after Törnqvist). AHD says 'wokso-. Wax. Related to weg-1', and Klein says wax 'lit. means that which is woven (by the bees)', which Nourai repeats. Modern Wiktionary (s.v. Proto-Germanic *wahsą) calls the origin 'somewhat disputed'. Cognates are Balto-Slavic *wáśkan; the comparison with *weg- is called 'tenuous', and a pre-IE substrate word is also possible. The merger of the two boxes into one root is therefore an old hypothesis, not established. On the Russian→Persian branch: Persian واکس is from Russian вакса 'shoe polish', a borrowing from German (Wachs / Wichse). It is not the native Russian воск 'wax'.\",\n      \"note_fa\": \"دو ریشهٔ هندواروپایی آغازین *weg- «بافتن، بستن» (پوکورنی ۱۱۱۷) و *wokso- «موم» (پوکورنی ۱۱۸۰) هر دو درست‌اند. پوکورنی آن‌ها را جدا آورده و پیوندشان را تنها گمان‌وار دانسته است. کلاین و AHD موم را «بافتهٔ زنبور» می‌گیرند و نورایی همین را آورده است. پژوهش امروزی (ویکی‌واژه) خاستگاه *wahsą را «تا اندازه‌ای مورد بحث» و پیوند با «بافتن» را سست می‌داند، و احتمال وام‌واژه‌ای از زبانی پیشاهندواروپایی را نیز مطرح می‌کند. پس یکی گرفتن این دو ریشه با احتیاط پذیرفتنی است. «واکس» فارسی از روسی вакса «واکس کفش» است که خود از آلمانی گرفته شده، نه از واژهٔ بومی روسی воск «موم».\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wahsą\",\n        \"https://en.wiktionary.org/wiki/wax\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1117\", \"status\": \"supports\", \"note\": \"POK_full.txt line 88897: 'Root / lemma: ueg- / Meaning: to weave, bind / Material: ... Latin velum \\\"sail, ... cloth, curtain\\\" ... Old English wēoce, ... Middle Low German weke, weike ...' ending 'See also: here uokso- \\\"wax\\\". Page(s):1117'.\"},\n        {\"ref\": \"POK:1180\", \"status\": \"partial\", \"note\": \"POK_full.txt line 93217: 'Root / lemma: uokso- / Meaning: wax / Material: OHG OS wahs, OE weax, ON vax; Lithuanian vaškas, ... russ.-Church Slavic vosk ... to *ueg- \\\"to weave\\\", as OHG wabo \\\"honeycomb\\\" to *uebʰ- \\\"to weave\\\", s. Tornquist ... Page(s):1180'. The root is right, but the weave link is given only as a suggestion.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 315 (leaf 324) and p. 247 (leaf 256)\", \"stance\": \"partial\", \"note\": \"Leaf 324: 'u̯okso- „Wachs“. Ahd. as. wahs, ags. weax, aisl. vax ... russ. ksl. (usw.) vosk ... Vermutlich zu *u̯eg- „weben“'. Leaf 256: u̯eg- with 'lat. velum „Segel ...“' and 'ags. wēoce „Docht“'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt lines 1130, 1172\", \"stance\": \"supports\", \"note\": \"'weg-1. To weave a web. Related to wokso-. ... *weg-slo- in Latin vēlum ... VEIL, VELUM, VEXILLUM, VOILE; REVEAL. [Pok. weg- 1117.]' and 'wokso-. Wax. Related to weg-1. Germanic *wahsam in Old English weax, wax: WAX1. [Pok. uokso- 1180.]'\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 19818\", \"stance\": \"partial\", \"note\": \"'ueg- \\\"twist, weave\\\". WP I, 247 ... Olr. figim \\\"weave\\\"; W gweu \\\"weave\\\" ... G cf. Wocken \\\"distaff\\\"'. Mann has no wokso- headword (grep '^u[oō]ks' finds only 'uaks- \\\"growth\\\"').\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Russian\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"This is an empty Russian box under the root. Russian has two relevant words. The inherited воск vosk 'wax' (< Proto-Slavic *voskъ < Balto-Slavic *wáśkan, cognate of wax) does go back to the root. The word that actually feeds Persian vâks, however, is вакса váksa 'shoe polish, blacking', a borrowing of German Wachs 'wax' (or Wichse 'polish', from wichsen 'to wax'). So the Russian stage is right for the Persian loan, but the Russian word is not inherited from the PIE root directly; it came through German.\",\n          \"derivation_fa\": \"این خانه روسی و خالی است. روسی دو واژه دارد: воск (vosk) «موم» که موروثی و از اسلاوی آغازین *voskъ، هم‌ریشه با wax، است، و вакса (váksa) «واکس کفش» که وام‌واژه‌ای از آلمانی Wachs (یا Wichse «جلا») است. «واکس» فارسی از همین واژهٔ دوم آمده است. پس گذر از روسی درست است، اما واژهٔ روسی مستقیم از ریشهٔ هندواروپایی نیست و از راه آلمانی رسیده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/вакса\",\n            \"https://en.wiktionary.org/wiki/Wichse\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"?\", \"status\": \"not_checked\", \"note\": \"The book prints '?' as the reference; nothing to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1180, POK_full.txt line 93217\", \"stance\": \"partial\", \"note\": \"'russ.-Church Slavic (etc.) voskъ' cited as the native Slavic cognate; vaksa not mentioned.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1971.txt line 265416 s.v. wax, n.\", \"stance\": \"partial\", \"note\": \"'cogn. with OSlav. voskŭ, Lith. vaškas, Lett. vasks, Pol. wosk, Russ., Czech, Slovak vosk, \\\"wax\\\"'. Only the native vosk is given, not vaksa.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"vâks\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian واکس vâks 'shoe polish' (also, loosely, 'wax') was borrowed in the Qajar period from Russian вакса váksa 'blacking', itself from German Wachs/Wichse. Mo'in marks it [روس.] and defines it as a coloured greasy substance for cleaning and shining shoes. Russian a → Persian â and -a dropped is the usual treatment of Russian loans, cf. سماور samovar, استکان stakan.\",\n          \"derivation_fa\": \"«واکس» در دورهٔ قاجار از روسی вакса (váksa) «واکس کفش» گرفته شده، و آن خود از آلمانی Wachs/Wichse است. معین آن را [روس.] و «مادهٔ چربی که رنگ‌های مختلف دارد و رویهٔ کفش را با آن تمیز و براق کنند» آورده است. افتادن -a پایانی روسی، مانند «سماور» و «استکان»، الگوی رایج وام‌واژه‌های روسی در فارسی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/واکس\",\n            \"https://en.wiktionary.org/wiki/واکس\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:4958\", \"status\": \"supports\", \"note\": \"vajehyab.com/moein/واکس: 'واکس [روس.] (اِ.) مادة چربی که رنگ های مختلف دارد و رویة کفش را با آن تمیز و براق کنند.' The page number of the 6-vol edition cannot be mapped online.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt line 83751 (2-vol Adena abridgement)\", \"stance\": \"supports\", \"note\": \"'واکس: (اِ.) مادّه‌ای روغنی به رنگ‌های مختلف جهت رنگ کردن کفش‌ها بکار برند.' The OCR lost the origin tag.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt grep 'واکس'\", \"stance\": \"silent\", \"note\": \"No entry; Aryanpur covers only inherited vocabulary.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"wahsam; weke\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *wahsą 'wax' (OE weax, OHG/OS wahs, ON vax) continues PIE *wokso- with *k > Gmc h before s (Grimm's law); its Balto-Slavic cognates are Lith. vaškas and OCS voskŭ. 'weke' is the Middle Low German form weke/wēke 'wick' (cf. MDu. wieke, OHG wioh(h)a, OE wēoce) < West Gmc *weukō-, which Pokorny explains from a reduplicated *we-ug- of *weg- 'weave'. Wiktionary says only 'possibly from *weg-'. Both forms are real and the root assignments follow Pokorny/AHD.\",\n          \"derivation_fa\": \"ژرمنی آغازین *wahsą «موم» (انگلیسی کهن weax، آلمانی کهن wahs) از هندواروپایی *wokso- است، و در آن k پیش از s طبق قانون گریم به h بدل شده. هم‌ریشه‌های بالتی-اسلاوی آن لیتوانیایی vaškas و اسلاوی کهن voskŭ‌اند. weke صورت آلمانی پست میانه برای «فتیله» است (انگلیسی کهن wēoce) که پوکورنی آن را از *weg- «بافتن» می‌داند و ویکی‌واژه «احتمالاً» از آن. هر دو صورت واقعی‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wahsą\",\n            \"https://en.wiktionary.org/wiki/wick\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1550\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1172: 'wokso-. Wax. Related to weg-1. Germanic *wahsam in Old English wex, weax, wax: WAX1.' The 1976 page 1550 is the last page of the appendix (w-roots), consistent with the citation; the 1985 text is used as proxy.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1117 (line 88897ff.) and p. 1180\", \"stance\": \"supports\", \"note\": \"p. 1117: 'auf redupl. *ue-ug- based on probably Old English wēoce, Middle Low German weke, weike, Old High German wiohha \\\"gedrehter Faden, Lunte\\\"'; p. 1180: 'Old High German Old Saxon wahs, Old English weax'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 247 (leaf 256)\", \"stance\": \"supports\", \"note\": \"'ags. wēoce „Docht“ ... mnd. weke „Docht, Lunte“'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line ~21444 s.v. Wick (1)\", \"stance\": \"contradicts\", \"note\": \"Skeat explains wick as 'pliant' or 'soft', 'allied to A.S. wāc, weak', i.e. from the 'yield, bend' family (*weik-), not from 'weave'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"wax; wick\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English wax (n.) < Middle English wax < OE weax < Proto-Gmc *wahsą; it is distinct from wax 'to grow' (OE weaxan < *h₂weks-). English wick < ME wek(e), wicke < OE wēoce, wēoc < West Gmc *weukā 'flax bundle, wick'. Klein and AHD put it under *weg- 'weave', Wiktionary says 'possibly', and Skeat dissents. The Germanic → English edge is certain for both words.\",\n          \"derivation_fa\": \"انگلیسی wax «موم» از انگلیسی میانه wax و انگلیسی کهن weax و ژرمنی آغازین *wahsą است، و با wax «بالیدن» (از *h₂weks-) جداست. wick «فتیله» از انگلیسی کهن wēoce است. کلاین و AHD آن را از *weg- «بافتن» می‌دانند، ویکی‌واژه «احتمالاً» می‌گوید و اسکیت مخالف است. گذر ژرمنی به انگلیسی برای هر دو واژه قطعی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/wax\",\n            \"https://en.wiktionary.org/wiki/wick\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited for this node; Nourai's AHD:1550 on the parent covers it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1971.txt lines 265416 (wax, n.) and 267003 (wick, n.)\", \"stance\": \"supports\", \"note\": \"wax: 'ME. wax, fr. OE. weax ... All these words are derivatives of I.-E. base *weg-, \\\"to weave\\\", and lit. \\\"mean that which is woven (by the bees)\\\". See wick'; wick: 'ME. wicke, wike, fr. OE. wēoce ... fr. I.-E. base *weg-, \\\"to weave\\\", whence also L. vēlum'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt lines 21249 (Wax (3)) and ~21444 (Wick)\", \"stance\": \"partial\", \"note\": \"'Wax (3), a substance made by bees. (E.) M.E. wax; A.S. weax ... Russ. vosk, Lith. waszkas' supports wax; for wick Skeat gives 'pliant or soft; allied to A.S. wāc, weak'.\"},\n            {\"src\": \"AHD\", \"where\": \"lines 1130, 1172\", \"stance\": \"supports\", \"note\": \"'wokso- ... Germanic *wahsam in Old English weax: WAX1'; weg-1 entry lists WICK1 (truncated in OCR before '*weg-slo-').\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"velum\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin vēlum 'sail; cloth, awning, curtain, veil' < Proto-Italic *wekslom (cf. the diminutive vēxillum 'banner', as pālus : pāxillus), with -ksl- > -l- and compensatory lengthening. The majority view (Pokorny, Walde-Pokorny, AHD, Klein, Wiktionary's first theory) takes it from *weg-slom 'something woven' (*weg- 'weave'). Other scholars refer the 'sail' sense to *weǵʰ- 'to carry, ride' ('that which propels', cf. Slavic *veslo 'oar'), which Skeat already preferred. Two competing etymologies therefore remain, and the chart's 'woven fabric' follows the first.\",\n          \"derivation_fa\": \"لاتین vēlum «بادبان، پارچه، پرده» از ایتالیک آغازین *wekslom است (مقایسه با مصغّر vēxillum «درفش»). در آن -ksl- به -l- بدل شده و واکه کشیده شده است. بیشتر پژوهشگران (پوکورنی، والده-پوکورنی، AHD، کلاین) آن را از *weg-slom «بافته» و از ریشهٔ *weg- «بافتن» می‌دانند. گروهی دیگر، از جمله اسکیت، معنای «بادبان» را از *weǵʰ- «بردن، راندن» (هم‌ریشه با اسلاوی *veslo «پارو») می‌گیرند. پس ادعای نورایی پذیرفتنی است، اما تنها دیدگاه نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/velum\",\n            \"https://en.wiktionary.org/wiki/revelo\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1695\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 899 (page numbers 1696 on the leaf), line 41170 s.v. veil: 'L. vēlum prob. stands for *wexlom (cp. vexillum, \\\"banner, flag\\\", the dimin. of velum), fr. I.-E. base *weg-, \\\"to weave\\\", whence also OE. wēoce, \\\"wick\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1117, line 88897ff.\", \"stance\": \"supports\", \"note\": \"'Latin velum \\\"sail, ... wrapping, kerchief, cloth, curtain\\\" (therefrom velare \\\"veil, cover\\\"), Demin. vexillum \\\"banner\\\"' under ueg- 'to weave, bind'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 247 (leaf 256)\", \"stance\": \"partial\", \"note\": \"'lat. velum „Segel ...“ ... Fähnchen“ (über abweichende Auffassungen von velum s. Lidén Stud. 20ff.)'. The derivation is accepted, but alternative views are noted.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 20659 s.v. veil\", \"stance\": \"contradicts\", \"note\": \"'L. vēlum, a sail; also a cloth. Lit. \\\"propeller\\\" of a ship; from vehere, to carry'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"veil; reveal\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English veil < ME veile, veil < Anglo-Norman/Old Northern French veil(e) (Central OF voile) < Latin vēla, plural of vēlum, reinterpreted in Vulgar Latin as a feminine singular. English reveal < ME revelen < Old French reveler < Latin revēlāre 'to unveil, disclose' (re- 'back' + vēlāre 'to cover', from vēlum), lit. 'draw back the veil'. The religious sense 'make known by divine agency' comes through the Vulgate (revelatio). Both edges are certain whatever the deeper origin of vēlum.\",\n          \"derivation_fa\": \"انگلیسی veil «روبند» از انگلیسی میانه veile و فرانسوی کهن شمالی veil(e) و لاتین vēla، جمعِ vēlum، است که در لاتین عامیانه مفرد مؤنث پنداشته شد. reveal «آشکار کردن» از فرانسوی کهن reveler و لاتین revēlāre «پرده برداشتن» (re- «باز» + vēlāre «پوشاندن»، از vēlum) است. معنای دینی «وحی» از ترجمهٔ لاتین کتاب مقدس (revelatio) آمده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/veil\",\n            \"https://en.wiktionary.org/wiki/reveal\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited for this node; KLN:1695 on the parent covers veil.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 41170 (veil, leaf 899) and line 32671 (reveal, leaf 713)\", \"stance\": \"supports\", \"note\": \"veil: 'ME. veile, fr. OF. veile (F. voile), fr. L. vela, pl. of velum ... but in VL. mistaken for a fem. sing. noun'; reveal: 'ME. revelen, fr. MF. reveler ... fr. L. revelare, \\\"to uncover, disclose\\\", lit. \\\"to draw back the veil\\\", fr. re- and velum'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt lines 16020, 20659\", \"stance\": \"supports\", \"note\": \"'veil, sb. (F.-L.) O.F. veile ... L. vēlum' and 'Reveal: see Vehicle' (same chain to vēlum, though Skeat derives vēlum from vehere).\"},\n            {\"src\": \"AHD\", \"where\": \"line 1130\", \"stance\": \"supports\", \"note\": \"'*weg-slo- in Latin vēlum, a sail, curtain, veil: VEIL, VELUM, VEXILLUM, VOILE; REVEAL.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-16T05:19:58.224Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-529.json (file state is current in your context — no need to Read it back)
```


## [2026-10-16T05:20:01.233Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -m json.tool data/verification/page-529.json >/dev/null && echo OK; python3 tools/verify_check.py 529"
}
```


### [2026-10-16T05:20:01.964Z] TOOL RESULT

```
OK
nodes verified: 12/12
node verdicts: {'plausible': 5, 'confirmed': 7}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 7, 'not_checked': 5, 'partial': 1}
books consulted: {'partial': 7, 'supports': 13, 'silent': 7, 'contradicts': 2} | by book: {'KLN': 6, 'SKT': 6, 'WLD': 4, 'AHD': 3, 'POK': 3, 'MON': 2, 'ARY': 2, 'BRT': 1, 'IEC': 1, 'FSD': 1}
```


## [2026-10-16T05:20:11.058Z] TOOL CALL #51: SubagentHandback

```json
{
 "message": "I verified page 529 (book page 499) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-529.json. It is valid JSON, and `verify_check.py 529` shows 12/12 nodes with 0 PROBLEM lines.\n\n**Verdicts:**\n- **Roots:** 1 confirmed (Wedh 2, Pokorny 1115 \"to push, hit\") and 1 plausible (Weg 1 / Wokso). Pokorny lists \"weave\" (1117) and \"wax\" (1180) as two roots and links them only tentatively. Modern sources call the origin of Proto-Germanic *wahsą \"wax\" disputed, and the link to \"weave\" weak.\n- **Nodes:** 7 confirmed, 5 plausible. No node is disputed or transcription_suspect.\n\n**Plausible nodes:**\n- Avestan vadhğan \"ax\": Bartholomae and Pokorny know vaδaγan- only as the name of a prince hostile to the faith; the meaning \"axe\" is Pokorny's question, not a fact. The other three Avestan words are confirmed.\n- Latin pass-through box: osmosis is a scientific Neo-Latin coinage by Graham in 1854, not a classical or medieval Latin word.\n- French osmose: the order is reversed. French osmose (1865) was borrowed from English osmosis; the older French words are Dutrochet's endosmose/exosmose (1826).\n- Russian empty box: Persian vâks comes from Russian вакса \"shoe polish\", which Russian borrowed from German Wachs/Wichse. It is not the native Russian воск \"wax\".\n- Latin velum: two etymologies compete, *weg- \"weave\" (most sources) and *weǵʰ- \"carry\" (Skeat and others).\n\n**Extraction errors:** none found. The JSON matches the chart text, so I did not need to check the page image.\n\n**References I could not check:** VOP:52 (Moshiri's dictionary is not online or on disk), plus the \"?\" and None references, which give nothing to check. The page number in MON:4958 cannot be mapped online, although Mo'in's entry for واکس (marked [روس.], Russian) supports the node."
}
```


### [2026-10-16T05:20:11.334Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
