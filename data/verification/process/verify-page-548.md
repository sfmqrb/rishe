# Verification process log — verify-page-548


## [2026-10-17T00:00:15.495Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 548 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-548.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-548.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-548.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 548` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.565Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.319Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.372Z] TOOL RESULT

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
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:00:18.808Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-548.txt"
}
```


### [2026-10-17T00:00:18.841Z] TOOL RESULT

```
1	=== PDF page 548 (book page 518) ===
2	--- entry 0 ---
3	ROOT Weredh -> redirect to Ered
4	--- entry 1 ---
5	ROOT [Indo-European] Weren : lamb  (refs POK:1170)
6	#1 (parent #0) [Avestan / Old Persian] refs=POK:1170 | varnak : lamb
7	  #2 (parent #1) [Pahlavi] refs=POK:1170; BQT:268 | varrak : lamb ; vâra-ğna, vâre-ğna, vâren-žar, varâğ : lamb killer (referred to falcon or crow) ☞Gwhen 2
8	    #3 (parent #2) [Sogdian] refs=SOD:398 | w`rğn`k : falcon
9	    #4 (parent #2) [Persian] refs=BQT; POK:1170; HRN:192; SOD:398 | barreh «برّه» : lamb ; varğeneh «ورغنه» : falcon ; kalâğ «کلاغ» : crow
10	
```


## [2026-10-17T00:00:19.390Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-548.json"
}
```


### [2026-10-17T00:00:19.578Z] TOOL RESULT

```
1	{
2	  "pdf_page": 548,
3	  "book_page": 518,
4	  "entries": [
5	    {
6	      "root": {"name": "Weredh", "redirect": "Ered"},
7	      "nodes": []
8	    },
9	    {
10	      "root": {
11	        "name": "Weren",
12	        "lang": "Indo-European",
13	        "refs": "POK:1170",
14	        "gloss": "lamb"
15	      },
16	      "nodes": [
17	        {
18	          "id": 1,
19	          "parent": 0,
20	          "lang": "Avestan / Old Persian",
21	          "refs": "POK:1170",
22	          "words": [
23	            {"translit": "varnak", "gloss": "lamb", "script": null}
24	          ],
25	          "note": null,
26	          "quote": null
27	        },
28	        {
29	          "id": 2,
30	          "parent": 1,
31	          "lang": "Pahlavi",
32	          "refs": "POK:1170; BQT:268",
33	          "words": [
34	            {"translit": "varrak", "gloss": "lamb", "script": null},
35	            {"translit": "vâra-ğna, vâre-ğna, vâren-žar, varâğ", "gloss": "lamb killer (referred to falcon or crow)", "script": null, "see": ["Gwhen 2"]}
36	          ],
37	          "note": null,
38	          "quote": null
39	        },
40	        {
41	          "id": 3,
42	          "parent": 2,
43	          "lang": "Sogdian",
44	          "refs": "SOD:398",
45	          "words": [
46	            {"translit": "w`rğn`k", "gloss": "falcon", "script": null}
47	          ],
48	          "note": null,
49	          "quote": null
50	        },
51	        {
52	          "id": 4,
53	          "parent": 2,
54	          "lang": "Persian",
55	          "refs": "BQT; POK:1170; HRN:192; SOD:398",
56	          "words": [
57	            {"translit": "barreh", "gloss": "lamb", "script": "برّه"},
58	            {"translit": "varğeneh", "gloss": "falcon", "script": "ورغنه"},
59	            {"translit": "kalâğ", "gloss": "crow", "script": "کلاغ"}
60	          ],
61	          "note": null,
62	          "quote": null
63	        }
64	      ]
65	    }
66	  ]
67	}
68	
```


## [2026-10-17T00:00:24.844Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','BQT','HRN','HUB','SOD','PHD','NYB','BRT','KNT','MON','ARY','IEC','SYN','CHEUNG']:\n  v=d.get(k);print(k,v and {x:v.get(x) for x in ['local_file','page_offset','lookup_hint','scans']})\n\""
}
```


### [2026-10-17T00:00:25.233Z] TOOL RESULT

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
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", 'scans': None}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.", 'scans': None}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'scans': None}
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'scans': [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", 'scans': None}
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", 'scans': None}
SOD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", 'scans': None}
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).", 'scans': None}
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", 'scans': None}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.", 'scans': None}
KNT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.", 'scans': None}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'scans': None}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", 'scans': [{'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", 'scans': None}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", 'scans': None}
CHEUNG None
```


## [2026-10-17T00:00:34.095Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -A25 'lemma: wer-3\\|lemma: wren\\|lemma: wr̥ēn\\|lemma: u̯ren\\|lemma: wr̥\\b' POK_full.txt | head -60; grep -n 'Page(s): 1170' POK_full.txt"
}
```


### [2026-10-17T00:00:34.477Z] TOOL RESULT

```
92403:Page(s): 1170-1171
```


## [2026-10-17T00:00:37.140Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92380,92460p POK_full.txt"
}
```


### [2026-10-17T00:00:37.525Z] TOOL RESULT

```
mcymr. gwest, AyM/es/"Ruheplatz', gwest, cywestach ^co\\.us\ ^M/es//"dwelling', dirwest 
{*dhro-ues-t-) and darwest{*to-are-ues-t-) " fast '; 

Gothic wisan{^. Sg. preterit was) "sein, abide, remain ', Old Icelandic i/es5 (later vera). 
Old English Old Saxon Old High German wesan {ev\ig\. preterit was). Old Frisian wesa 
"sein, abide, remain ', Modern High German war, gewesen, substantivierter Infin. "entity'; 
Gothic w/stst "entity'. Old Icelandic v/st. Old English Old High German iy/5/ "entity, abode, 
residence, Dasein'; Old Icelandic i/^/r" peaceful ' (or identical with dem 2. part from g/- 
vaerr, see above S. 1165; certainly here belongs /7e/'5d-i/^/r"berechtigt, in district, region, 
area to sein'); Old Saxon weron. Old High German n/e/'e'/? 'endure, wahren' (in addition Old 
High German wirig^ lasting, dauerhaft'. Modern High German lang-wierig) and Old Saxon 
waron. Middle Low German n/a/ie/? "endure'; perhaps Gothic nvis" calm (at sea) ', if actually 
" tranquility '); 

Tocharian A wsen/ie' lair', wast, B os/ "house', M/as5/r7c» "friend', PI. wasmoh, wsassam 
" dwells '; 

Hittite {*hueis-) huis-^ live, am Leben bleiben', {*hueisa-) /7^/sa-" mirror'. 



References: WP. I 306 f., WH. II 773, Frisk 25, 173 f., 576 f., VendryJs RC. 35, 89 f.. Loth 
RC. 38, 297, Ifor Williams BBCS. 2, 41 ff., R. A. Fowkes JC. stem 2, 1 f. 
Page(s): 1170-1171 



Root / lemma: ues-2 {* hauhes-2) 
Meaning: to feast 

Material: Old Indie anu vavase^has aufgezehrt', vastoh'vor dem ravenousness', Avestan 
vasfraTresse, muzzle', vastrsm loo6' , vas far- ^H\rte'; about Latin vescor^as meal eat, be 
nourished ' see above S. 73; Middle Irish fess, fe/sslood, eating' {*ues-ta). Old Irish fi'ach 
"raven' ( *uesakos), out of it borrowed cymr. gwyach "Steiftfuft' (ein bird); Old Irish ban- 
[f]ess^ wedding ' (Trauen-fesf), bret. /7a/7i/e5 'festival', cymr. ^n/es/ 'festival'; Gothic waila 
wisan 'to feast, delight ', frawisan 'consume', wizon 'indulge oneself, waila-wizns ' feast ', 
gawizneigs' s\c\\ mitfreuend'. Old English tvesa/? 'to feast' (only Beowulf 3115, Hs. 
weaxan); Old High German firwesan. Middle High German i/e/wese/7 'consume'; Old 
Icelandic vist. Old English Old High German wisti. 'dish, food'; in ablaut probably Old High 
German M/as/e/( French gateau) ' cake'; 

Hittite {*hauhes^ ^es/- 'pasture', uesua-^qraze, abweiden; lead, regieren'; {*hauhes- 
)i/es/a/'a- 'herdsman, shepherd'. 

Maybe alb. ushq/mlood', ushqejleed'. 

References: WP. I 307 f., Vendryes RC. 35, 89 f., WH. II 769 

See also: probably to uesu- 'good'. 

Page(s):1171 

Root / lemma: ues-3 {* hyes-3) 
Meaning: wet 

Material: Gr. sapov Aournpa, n Trpoxouv Hes., alt-theraisch hsapa (meaning 
unacquainted); Umbrian i/es/z/ra/^'libato' (formation as Latin lectTca); 
Maybe alb. vese^ dew ' 

Old High German wasa/^ra\n', Old High German waso'\a\Nn, clod of earth, pit, pothole'. 
Modern High German l/Vasen lawn' , Old Saxon waso, Middle Low German wase^damp 
Erdgrund, slime, mud; clod of earth, lawn'; Middle Low German wasemm. 'Wasserdampf, 
haze, mist'; Old English wosn. ' dampness, juice, sap'; engl. ooze' dampness, slime, 
mud', as verb 'durchsickern, spring up, bubble'. Middle Low German wos'scum, froth. 



foam, decoction, extract acquired by boiling, juice, sap'. Old Danish Norwegian os' plant 
juice '; 

presumably Avestan varjhu-tat-t "blood', varjhu&wa-u. "Blutvergieflen, bloody fight', 
vohuna- m. 'blood' and Old Indie vasa, Kas5 "bacon, fat, lard ' (also i/asa inscribed, as 
vasa-m "flijssiges fat'); 

here with the meaning "male animal' (compare Latin verresetc: uer-, t/eA-s-'feuchten'): 
Old Indie ustra- m. 'Buffel, Kamel', ^s/5/'-'Pflugstier', Avestan ustrom. 'Kamel' (also in 
Zaral=>-ustrd)\ Old Indie ^5/5'Pflugstier'. 

References: WP. I 308, Trautmann 343, Mayrhofer 1 , 113 f.. Frisk 433. 
Page(s): 1171-1172
```


## [2026-10-17T00:00:43.391Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lamb\\b\\|Lamm\\b\\|sheep' POK_full.txt | grep -i 'urēn\\|ren\\|lemma\\|meaning' | head; grep -n -i -B2 -A3 'Meaning: lamb\\|Meaning: sheep' POK_full.txt | head -40"
}
```


### [2026-10-17T00:00:43.789Z] TOOL RESULT

```
2131:Meaning: lamb' 
2800:{* heg^h-no-s): lamb' and Root/ lemma: ag-\ "goaf : Root/ lemma: kago-or kogo- -a-: 
10193:Meaning: sheep's bleating 
16129:Note: imitation of the sheep sound with different guttural extensions; in the Germanic with 
27875:Meaning: goat; sheep 
43112:{* heg^h-no-s): lamb' and Root/ lemma: ag-\ "goaf : Root/ lemma: kago-ox kogo-, -a-\ 
61206:Meaning: sheep; hide, leatherwork 
64306:Meaning: sheep 
93483:Meaning: ram, sheep, lamb 
2129-Root / lemma: ag'^h-no-s {* Jag^h-no-s) 
2130-
2131:Meaning: lamb' 
2132-
2133-Note: (z. T. also *ag"'nos'7) 
2134-
--
10191-
10192-Root / lemma: be, ba 
10193:Meaning: sheep's bleating 
10194-
10195-Material: Gr. pn, Latin bebo, -are^ bleat, shout, from a young deer', balareaud Vulgar 
10196-Latin belare^ bleat ', Modern High German bah, Slavic (e.g. kir.) bekatT bleat ', Latvian 
--
61204-Root / lemma: moiso-s or maiso-s 
61205-
61206:Meaning: sheep; hide, leatherwork 
61207-
61208-Material: Old Indie mesa-m. 'aries, ram', mesh' fleece ', Avestan maesa-^anes, ram, 
61209-
--
64304-Root / lemma: oui-s 
64305-
64306:Meaning: sheep 
64307-
64308-Grammatical information: m. f. Gen. Sg. ouios, f. ouikads. 
64309-
```


## [2026-10-17T00:00:52.988Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 93475,93530p POK_full.txt"
}
```


### [2026-10-17T00:00:53.568Z] TOOL RESULT

```
References: WP. II 374 f., Trautmann 246, Vasmer 2, 529, Jacobsohn Arier 133 ff., where 

also about uralische equivalent (probably Indo Germanic loanword). 

Page(s):1183 

Root / lemma: Ueren- {* hauers-en^ 

Meaning: ram, sheep, lamb 

Material: Old Indie *uran-{irorc\ *vuran-), Akk. * uranam, Nom. ura, from which urana- m. 

"lamb, aries, ram', ura\. "sheep', in addition urabhra-rw. "aries, ram' for *ura-b^a- {as 

vrsabba- to vrsan-); compare npers. barra {* varnak) "lamb'; Pahlavi varak^aues, ram'; Iran. 

varan-jar-, i/a/'a-i77a-"Lammerschlager' (Humbach DLZ. 78, 299 f.); 

Armenian garn. Gen. ^5/7/7 "lamb'; 

gr. hom. (F)apr|v, Gen. apv6(; "lamb', Cretan Fappv; also in tsakon. vanna, from lakon. 
Fapviov "lamb', in addition -Fpr|v in hom. noAuppnv "schafreich', out of it late ppv), with 
ablaut. apv£i6(; "aries, ram', whether not rather from *apav£i6(; (*apav-r|F6(;) to apar|v " 
virile ' (above S. 336); 



derivative *urendn- in Latin (as Germanic loanword) reno Tierfell as ciotliing , Pelz'; 

unclear as derivative Latin vervex, -ecis (-/>, -Tcis) " wether, castrated ram '; unclear is 
also das relationship to den auf *eruo(s)- "wool' ruckfijhrbaren gr. words slpoc; n. 
"Wollflieft', derived sipiov, Attic spiov "wool', Attic £U£pO(;, £U£pr|(; "schonwollig', Aeolic £tt- 
£poc; "aries, ram' ("whereupon Wolle is'), Ionian £iplv£0(;, Attic i^wizoc, "from wool'; 
aniautendes F lasst sich not nachweisen. 

References: WP. I 269 f., WH. II 429, Specht Indo Germanic Dekl. 33 f.. Frisk 137 f., 468 f. 

Page(s):1170 

Root / lemma: ud- {*heud-s) 

Meaning: upwards; away 

Note: besides Jo^-s (compare Latin ab\ abs) 

Material: 1 . Old Indie ud-, ut- "empor, out' proverb; Avestan us-, uz- {*uds-) ds., ap. ^s-ds. 

{ud- in ud-apatata^ex lehnte sich auf, fiel ab' is probably *uz-); 

gr. u- in u-ppiq (see below g'^er-^ heavy '), uarpi^ "porcupine', uanAr)^ "Startseil', Cypriot 
u-xnpo<; "Aufgeld' (Attic "ra £nix£ipa') and in this Mundart generally zum Ersatze from £ni 
has changed: adnominal with Lok. e.g. u-Tuxa "£ni Tuxp'; eine (an Gothic /i/pa besides 
*i/yC?c» gemahnende) full grade probably in Cypriot £UTp6aa£a0ai £niaTp£(p£a0ai. flacpioi and 
£uxou(; x^vn ("Trichter') laAafjivioi Hes.; (because of uoioo,, uaT£pa see below udero- 
"belly');
```


## [2026-10-17T00:01:06.731Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo ==PHD; grep -n -i '^warrag\\|^warag\\|warrag\\|^waragn\\|warāɣ\\|wālan' PHD.txt | head; echo ==NYB; grep -n -i 'varrak\\|varak\\b\\|varāk' NYB_vol2_glossary.txt | head; echo ==HRN; grep -n -i 'barra\\|kalāγ\\|kalāgh\\|kalag\\|varγ\\|warγ' HRN.txt | head -20; echo ==HUB; grep -n -i 'barra\\|kalāγ\\|kalāg\\|varγan' HUB.txt | head; echo ==BRT; grep -n -i 'vārəγ\\|varəγ\\|vāraγ\\|Vogel' BRT.txt | head -20"
}
```


### [2026-10-17T00:01:07.142Z] TOOL RESULT

```
Exit code 1
(eval):1: =PHD not found
```


## [2026-10-17T00:01:11.600Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo \"--PHD\"; grep -n -i 'warrag\\|^warag\\|warāɣ\\|wārǝɣn\\|lamb' PHD.txt | head; echo \"--NYB\"; grep -n -i 'varrak\\|varak\\b\\|varāk\\|lamb' NYB_vol2_glossary.txt | head; echo \"--HRN\"; grep -n -i 'barra\\|kalāγ\\|kalāgh\\|kalag\\|varγ\\|warγ\\|Lamm' HRN.txt | head -20; echo \"--HUB\"; grep -n -i 'barra\\|kalāγ\\|kalāg\\|varγan\\|Lamm' HUB.txt | head; echo \"--BRT\"; grep -n -i 'vārəγ\\|varəγ\\|vāraγ\\|Rabe\\b\\|Falke' BRT.txt | head -20"
}
```


### [2026-10-17T00:01:12.053Z] TOOL RESULT

```
--PHD
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
832:Aries Warrag.
2550:lamb warrag.
3322:ram warān, warrag.
5041:warrag
5163:warrag
--NYB
487:v. dast. Paz. erroneously ac-dast, Skr. v. hastavalambin-.
3428:*2gīh: restore in 717-24, 8? the reading lk 4-7 of the MSS instead of conjectured wlk-- 1 (= varrak-ē) and 7?9. 8° Ik of the MSS instead of conjectured wlk' (= varrak), and read lk as the figure 30 = sih, lk--1 as 80+1 = sih-é. It is not advisable to emend a reading so persistently repeated and so unyieldingly maintained by all MSS, in spite of its enigmatic character. Of course, it cannot be the numeral thirty; the context requires a w. signifying a supernatural being which is finally un- veiled as the Glory (x%arrah, x"aranah) of the Kayanian kings. I venture the
3430:hypothesis that we have to do with OP *oi- — NW (Av. 1645) sri- (Bthl srāy-) "beauty, splendour’ = Kkr sri- ‘splendour, majesty’, also personified as the goddess of beauty, of fortune, or of sovereign power; Milr *si(y) alternates freely with sih according to the common rule. This divine power is apparently miaterialized in some animal which is said to be very stout (71%), the most beautiful imaginable (718-18), very big and brisk (87%). In the Sn, where the episode is told at length (Book 21, v. 231 sqq., Tehr 4, p. 1697- 98 — Mohl V, p. 288), it is said to bea ram (yurm), but deseribed as a guite mythical, mysterious being: “I have not seen its equal painted in any palace”, one of the witnesses says, “with wings as Simurgh, with a tail as the peacock, like a flash of lightning, bold of head and ears and hoofs, purple-coloured, swift as the wind, in its way it does not remind of a ram at all". The conjecture varrak, adopted by Nöldeke and Antiä, robs the narration of the air of divine mystery essential to it. Sanjana’s remarks are worthless. — OP *ei- is also attested in NP séy ‘beautiful, elegant, excellent’ < MiPrs *sēk < OP *cayaka- for NW *srayaka- from Av. (1638 sg.) srayan- ‘beauty’ and ‘beautiful’; in a pejorative sense in NP sihah ‘harlot’ < MiPrs *sthak; possibly also in NP siyäb, whose meaning is, however, somewhat uncertain (v. Steingass and BQ). — It is not all too difficult to guess why the scribe chose such a strange way of writing this w.: by spelling it phonetically he would have got a very ambiguous and polyphonic graphic symbol. His spelling 30 guaran- teed safe reading. Certainly this is be- wildering for us who read with our eyes, but in antiquity all texts were intended to be perceived by ear. Cf also s. v. nist.
3979:*varrak [wlk'] 717-24.26, 87.9, restore the reading lk = 30 and v. ?sih.
--HRN
2229:211. berre, bere 'Lamm*.
2232:ai. ürana- *Widder, Lamm'; phlv. varak', arm. gam
2253:'Bock', bukka- 'Ziege'; arm. buc 'Lamm' (H. No. 60).
5300:ai. l/'dlp-, drpyate ^flammen, strahlen, glänzen*;
5596:licht, Sonne* (824) ; wa/. räiij 'Flamme'.
--HUB
5258:Krone', barad *tragt', bar *Brust*, barra *Lamm\ bar *auf,
5283:= skr. giras' ; har "Brust* = skr. tiros (aus *vura8) ; harra *Lamm' aus
5457:61. 204, zd. vafra-; barg *Blatt' = zd. vareka-; barra 'Lamm'
7930:auch aspal (in Klammern) an, das = ap. ^sparda-lw&TQ, Aber in echt
9287:= *bhrnami (oben p. 28) ; barra, bara *Lamm* aus *varnaky
--BRT
25787:KompE.  —  VgL  'saina-  EN,  —  mp.  sinmun; np.  (Npü.)  änmur^;  ai.  vgL  lyeni-  m.  'Adler, Falke'  (S  po.  1);  s.  dazu  Hbm.  AGt.  /.  499,
```


## [2026-10-17T00:01:20.668Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2225,2240p HRN.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"211. berre\")) print NR-1}' HRN.txt; sed -n 5280,5286p HUB.txt; sed -n 9284,9290p HUB.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"bara *Lamm* aus\")) print NR-1}' HUB.txt; grep -n -i 'Lämmer\\|Lammer\\|Rabe\\|vāragan\\|värəyan\\|vārəɣ\\|varəyan\\|Vogels' BRT.txt | head"
}
```


### [2026-10-17T00:01:21.164Z] TOOL RESULT

```
aw. *upairivara- oder wohl besser ^upairivärana- ;
vergl. de Lagarde, Beitr. z. altbaktr. Lex. 54 folg.,
Semitica, I, 38.
»j Vergl. auch 'Prinzmetall*, Pott ZKM. IV, 264.- 49 -
211. berre, bere 'Lamm*.
g. vare; semn. vara; mäz. vare; Kä§. verrd, verä,
veri,
ai. ürana- *Widder, Lamm'; phlv. varak', arm. gam
Xamm' (H. No. 64).
kurd. vark^ garik, bar/, bar/ik (H.-Sch.); af;'. vrai\
oss. d. warik^ urek, t. värjg (78) ; bei. gvarak, n. gvaraU
(137); wa;K. vurk, siyn. varg, sar. barka,
212. burrtden, burTden 'schneiden ^).
aw. V^bray-'^) 'schneiden', pairLbrinenti, pairLbrina-
fiuha; phlv. burUan (was ebenso gut auch burntan
sein kann); ai. V^bhray-, bhnndti Versehren; arm.
70
dar gam *lange' = skr. dlrghdm; parana' 'frilher', skr. puran&'\ parW
Mel = skr. jowni-; paruva-, paruviya- *frilher\ skr. pdrva^, purvyd^^
doch siehe oben § 35, a. Dazu np. arm 'Arm* = skr. irmd' ; sar 'Eopf
= skr. giras' ; har "Brust* = skr. tiros (aus *vura8) ; harra *Lamm' aus
^varn-ak, skr. tirana- (aus *t?Mrow(i-), gr. j^aQsr- (nom. urspr. *vren
und *vfrBn, gen. *vpio8) ; guSarad *geht vorbei* =: skr. vi-tirati ; sard
*kalt* = zd. sar eta- (skr. *girta'); arask, rask *Neid*, skr. irasyati
*Thal, Schlucht* = zd. darenO^; darndan, darfdan zer-
reissen', skr. 3. pr. drnati ; garr, gar *Kratze' == zd. ^areww- ?;
burrldan, burtdan (Fird. I, 449, 265) 'schneiden , pr. burram
= *bhrnami (oben p. 28) ; barra, bara *Lamm* aus *varnaky
idg. vfren- (vgl. § 13 am Ende), skr. urana-, arm. garn;
tar, tarr 'feucht' A. M. 5, 15, tarn 'Feuchtigkeit* A. M. 7, 3,
vgl. zd. tauruna-, gr. rsprjv ; zarr, zar *Gold', zarr%n 'golden*,
269
194:besagen,  dass  der  links  davon  angegebene  Paragraph  dem  oder  den  rechts  ange- gebenen ganz  oder  teilweise  gleich  oder  ähnlich  ist  —  Die  eingeklammerten ZifTem  —  bei  Y,,  Vr.,  V.  —  geben  die  abweichende  Kapitel-  und  Paragraphen- zählung in  Spiegels  Ausgabe  der  Fahlavi-  und  SanskiitUbersetzung  aa
3317:Eig.  'Graben,  Aussteclien  der  Bewässeningi- liinäU';  'kaaay-i.,ima.\ .  kaH-;i^.  ai.  Handy' Adj.  'grabend',  f.  'Mine'.
4536:•  j.  an-us'kante  Inf.  'nicht  (wieder)  aus- zugraben':^j/  aitika  zsmS  nikante  spsnasifa irista  ,  .  ttaimtm  yär3.dräjS  an'  "wenn man  hier  in  die  Erde  eingräbt  tote  Hunde und  . .,  ein  halbes  Jahr  lang,  (um  sie  nicht sva.)  ohne  sie  wieder  auszugraben"  V.  J.36.
5005:•  j.  ava-lcana-  in.  i)  'Graben,  fossa':  ys atttm  'tum  avalianta\.lyz^-  a)'Gnibe': aSa'iii  .  .  mazdayasna  ai-^hä  s»mS  'mm aiaJianayin  V. i'.8".
5007:•  j.  ava-kanay-  m.  'Graben,  fossa*:  ys aitfm  ai'aAan^m  avakatäa  yeiihä  v5  aisS 'nis  anhat  V.  75.39  ■>.
5009:•  j.  ava-kanta-  n.  'Graben,  fossa':  yai aisa  gaViOa  'ttüfva  frajasät  V.  /5.38,
5799:•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
8277:•  j,  upa.9TVarätay-  f.  'Anschneiden  sva. Durchstechen  des  Grabendamms,  Damm- durchstich': yaval  ai^a  ä/s  byärixti  (sd.) 'ti  {VA.)  frabavät  ^.14.1$.
8971:•  p.  ka"tanaiy  Inf.  'zu  graben ;  durch Graben  (Meiseln  udgl.)  herzustellen':  adam niyastnyam    itnäm  yuviyätn  (sd.)    ka"   D.
9056:•  j-,  p.  'kan-"  V.  'graben'.  Praes.  i ian-,  2  kana-,  30  (Iter.)  kiltiaya-.'*  — PPfP.    -ianta-^^;     Inf.  ka'tanaiy,    -kantSe,
```


## [2026-10-17T00:01:26.217Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==214' HRN.txt | head -60; echo ----BRT; grep -n -i 'Yt\\. *14\\.\\(19\\|35\\|36\\)\\|14\\.19\\|vär3j\\|vär3γ\\|värs[yγ]' BRT.txt | head -20"
}
```


### [2026-10-17T00:01:26.671Z] TOOL RESULT

```
800. kef \Schaiiin'.
aw. kafa- *SchaunV; phlv. kaf (AV., nicht kef)\ skr.
kapha- 'Schleim'.
kurd. kaf Schaum'; oss. d. /äfä, t. /äf Hotz,
Schleim' (299); bei. kap^) (188); wa/. ;^w/, sar. /^/.
861. kul *krnmm, gekrümmt'-).
Nach Nöldeke (mündliche Mitteilung) zu gv. y.vkhig
*krumm'. Dann vergl. auch gr. xt;(}rog gekrümmt', aw.
skarena- 'rund'. — Fortunatow stellt (BB. 6, 216)
gr. y.vXXog zu skr. kuni- *lahm am Arm' (aus "^kulni-),
862. keläy, kulüy liabe', ixiD (Is. 34, 11, etwa statt ixiD?).
aw. «;ära;72rt- (?) ; phlv. varäy^ varäk.
Das np. k könnte dann eben so wenig ursprünglich
sein wie in kiisüden statt gusciden. Anderenfalls würde
die Zusammenstellung unstatthaft sein. Nöldeke will
daher (mündliche Mitteilung) gr. v.ogai, etc. vergleichen
und auch phlv. rardy, varOk ganz aus dem Spiele
lassen; jüd.-pers. JIXID sei in jNHp zu emendiren, wie
auch das Gazophylacium schreibe (D und p seien
in hebräischen Handschriften oft nicht von einander
zu unterscheiden)-^). Diese Erklärung ist gewiss vor-
zuziehen, zumal die Bedeutung *Rabe' für das Avesta-
wort gar nicht passt (sie beruht zudem nur auf einer
Vermutung Destür Daräb's) *).
863. Ualäh \VIütze'; Helm (aus Stahl, Sahn. I, 100 Vers
711)', kidä, hdeli.
') Vergl. g. kaj).
^) Durch einen Vers des vorfirdusischen Dichters Abu Öekür
belegt.
^) Im Neupersischen wird das Wort aber nie mit q^ sondern stets
mit k geschrieben. Es müsste also ein Schnitzer im Gazophylacium
und in der jüd.-pers. Schreibung vorliegen.
*) Nachträglich sehe ich Hübsch mann's Bemerkungen in
KZ. 26, 607 folg., der auch aw. väi^ayun- nicht als *Rabe* gelten lassen
will und bei. f/nräy *crow\ köh-f/uräy Vaven' (Damea, S. 104) heran-
zieht ( Corrokturnoto ).
----BRT
20366:—  'ya{\S.)  ass.zusia  {sd.)  V.  77.  g';  — °yaAe  kfhrpa  värsynahe  (sd.)  Y\.i4.t<i, ;p.  35;  34;  —  'yahe  pilö.parinahe  värtnfi- nahe  (^)  Yt  14.35.  a)  vom  Hahn, Huhn:  alsS  °yü  pa rff. dar f  (sd.)  al^ff  -ys yS  kantcdastiiisd.)  FrW.  70.  41;  V./<?.  16;
```


## [2026-10-17T00:01:31.116Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'värs[yɣγ]an\\|värsyna\\|värijina\\|vär3[yγ]n\\|vārə' BRT.txt | head; grep -n -i \"Vogel.*Falke\\|Falke\\|Rabe\" BRT.txt | head"
}
```


### [2026-10-17T00:01:31.504Z] TOOL RESULT

```
20366:—  'ya{\S.)  ass.zusia  {sd.)  V.  77.  g';  — °yaAe  kfhrpa  värsynahe  (sd.)  Y\.i4.t<i, ;p.  35;  34;  —  'yahe  pilö.parinahe  värtnfi- nahe  (^)  Yt  14.35.  a)  vom  Hahn, Huhn:  alsS  °yü  pa rff. dar f  (sd.)  al^ff  -ys yS  kantcdastiiisd.)  FrW.  70.  41;  V./<?.  16;
3317:Eig.  'Graben,  Aussteclien  der  Bewässeningi- liinäU';  'kaaay-i.,ima.\ .  kaH-;i^.  ai.  Handy' Adj.  'grabend',  f.  'Mine'.
4536:•  j.  an-us'kante  Inf.  'nicht  (wieder)  aus- zugraben':^j/  aitika  zsmS  nikante  spsnasifa irista  ,  .  ttaimtm  yär3.dräjS  an'  "wenn man  hier  in  die  Erde  eingräbt  tote  Hunde und  . .,  ein  halbes  Jahr  lang,  (um  sie  nicht sva.)  ohne  sie  wieder  auszugraben"  V.  J.36.
5005:•  j.  ava-lcana-  in.  i)  'Graben,  fossa':  ys atttm  'tum  avalianta\.lyz^-  a)'Gnibe': aSa'iii  .  .  mazdayasna  ai-^hä  s»mS  'mm aiaJianayin  V. i'.8".
5007:•  j.  ava-kanay-  m.  'Graben,  fossa*:  ys aitfm  ai'aAan^m  avakatäa  yeiihä  v5  aisS 'nis  anhat  V.  75.39  ■>.
5009:•  j.  ava-kanta-  n.  'Graben,  fossa':  yai aisa  gaViOa  'ttüfva  frajasät  V.  /5.38,
8277:•  j,  upa.9TVarätay-  f.  'Anschneiden  sva. Durchstechen  des  Grabendamms,  Damm- durchstich': yaval  ai^a  ä/s  byärixti  (sd.) 'ti  {VA.)  frabavät  ^.14.1$.
8971:•  p.  ka"tanaiy  Inf.  'zu  graben ;  durch Graben  (Meiseln  udgl.)  herzustellen':  adam niyastnyam    itnäm  yuviyätn  (sd.)    ka"   D.
9056:•  j-,  p.  'kan-"  V.  'graben'.  Praes.  i ian-,  2  kana-,  30  (Iter.)  kiltiaya-.'*  — PPfP.    -ianta-^^;     Inf.  ka'tanaiy,    -kantSe,
9057:'eingraben' :  y'fi  h:tnti  aifjhh  stmö kaiunti  "diejenigen  die  Wesenheiten  (Ani- malta)  in  die  Erde  vergraben"  V.  y.  40 PüZ.     S.  noch  No.  2.
9058:mit  aipi  'durch  Graben  ausfiillen,  zu- schütten': basi-arj  mayanqm  .  ,  aitihä wmO  aipi-kanyät  V,  14. 6.
```


## [2026-10-17T00:01:49.467Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'Raubvogel\\|Vogelname\\|Name eines Vogels\\|eines Vogels' BRT.txt | head"
}
```


### [2026-10-17T00:01:49.848Z] TOOL RESULT

```
17240:Ar.  'biäsa-  m.  Name  eines  Raubvogels'),  — ai.  bhäsa-  m.  (auch  als  EN.);  mp.  bähai  EN. (=  ai.  ikäsaka-  EN.\  S.  noch  Marquart EranSahr  128.  —  ')  Zn  gr.  ^n;  {eine  Adler- att)  s.  Bthl.  IF.  8.  235.
23513:•  j.  vära-gan- :  °jn-  m.  Name  eines Vogels'*:  afimäi  .  .  ajasa^  vazfmnS  v»r»- %rayne  .  .  niirr/ahe  kthrpa  •ynake'''  . . yS  vayam  aiti  asUtS  Yt.  i^l.  19;  —  lusai il'arynS  yimai  kaca  . .  mirriahe  kthrpa -ynahe''^  Vt /p.  35.
25654:ITA.,  aus  ar.  *nrattt;  Praes.  1.  —  Vgl,  gr, fX«^'Fang,  Beute',  Ist.  i'dZiv«-;  s.  dainSOLMSEN Slud.  15.  —  Npü.:  bar  iulanät'1.  —  >)  Vgl. zSt.  Bkehm  Tierleben>,  Vögel  7.  523;  "Zum Fangen  dienen  (dem  Raubvogel)  die  Füsse  . ., zum  Zerstückeln  der  Nahrung  .  ,  der  Schna- bel . .".   —  J)  S.  »n  'urvala:
```


## [2026-10-17T00:01:57.112Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23513,23518p BRT.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"vära-gan-\")) {print NR-1; n=split($0,a,\"\\n\"); for(i=1;i<=6;i++) print a[i]}}' BRT.txt | head -10"
}
```


### [2026-10-17T00:01:57.512Z] TOOL RESULT

```
•  j.  vära-gan- :  °jn-  m.  Name  eines Vogels'*:  afimäi  .  .  ajasa^  vazfmnS  v»r»- %rayne  .  .  niirr/ahe  kthrpa  •ynake'''  . . yS  vayam  aiti  asUtS  Yt.  i^l.  19;  —  lusai il'arynS  yimai  kaca  . .  mirriahe  kthrpa -ynahe''^  Vt /p.  35.
Vgl.  värin-gan-.  —  Eig.  Bed.?  Man^  hat  den Vogel  Damen  mit  'flügelschlagend'  überaetit nnd  für  *3i'J/'-  auf  np.  fj/ 'Feder,  Flügel'  nnd ai.  J-äta-  m.  verwiesen;  5.  Sp.  Komm.  3.  1Ö4, Heu.  KZ.  27.  607.  Aber  ai.  vära-  bedeutet 'Schweifhaar',  bes.  des  Kosses  (wie  lit.  ialtd), und  np,  bäl  ist  vielmehr  gleich  ai.  barha-  [v') 'Schwan ife der"  lu  seWen,  Ander»  jetii  Richtir IF.  p.  185.  —  Npü.:  fehlt.  —  II  Welche»? Falsch  Dst.  ZA.  z.  566;  vgl.  Hbm.  PSi.  87. HoRN  GlrPh.  7  b.  56.  —  '}  Them.
•  j.  väi^man-  n.  'Wehr,  Bnistw-ehr': naire  Aam.vaniti^  *diirisia  (sd.)  Yt  //.  2.
KompE.  —  Zum  V.  ^var.;  vgl.  viB-Aa-  nnd IQ  vä%man-,  —  Pü.;  varük,  Hpä.:  Jauian.
•  j.  'vära^ajua-  Adj.  'siegreich,  sieg- haft' :  va^m  valjS  (sd.)  yim  •yn»m  Yl ig. 92;  —  ma^ranam  *°ynfm^^  ..  vär»- hrayHysJim>m  Yt^.  5-
Ableil.  (mit  Vf-ddhih)  aus  i/jrjSfajBa-.  —  aL varlragkna-  Adj,  —  >)  J  lO,  K  36.  NA.  korri- girt  in  'yti.     Geringe  Stelle.
775
 seinem  Wohlgefallen"  Y.^.  a;  —  AS. mit  °a  (vanma)  als  Adv.  sbes.  a)  'Aus- lese' (nur  vAbleiL).  (Y.  to.  14:  lies vär7ma.\
vAbieit.  —  Zum  V.  'var-.  —  Vgl.  matdä.vara-. —  Pü. :  (pa)  iämai.
•  j.  värant-  Adj.  (fem.  •r»ntl-),  PPA,: s.  *var:
KompE.
•  j.  vär«n-gan-  m.  Name  eines  Vogels*': msn-jahe  . .  'nn/tnahe'^  par»rum  ayasaisa Yt.  14-  35-
Komp.  mit  AS.  im  I.  Glied;  S  ^65.  1.  — NpH. !  ta  farandagi  i  xüi.  —  ')  Des  selben, der  sonit  väDgan-  genannt  wird,  sd.  — »)  Them.;  i  nach  %  29S.  4.
```


## [2026-10-17T00:02:02.205Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"vära-gan-\")) print \"leaf\",NR-1}' BRT.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"vära-gan-\")) print $0}' BRT.txt | grep -n '^ *1[34][0-9][0-9] *$' | head"
}
```


### [2026-10-17T00:02:02.605Z] TOOL RESULT

```
leaf 775
```


## [2026-10-17T00:02:05.206Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"falcon\\|w'r[γɣy]n\\|wr[γɣ]n\" SOD_pages.txt | head -20"
}
```


### [2026-10-17T00:02:05.818Z] TOOL RESULT

```
21403:     falcon
25009:7394 pryt* ? S                                    *• ±>J><             liking hunting with falcon
32116:                                                               9848 wVyn'y =* w'ryn'k
32152:9843 w'pryt =* w>Pr>y5                                         9855 w'ryn'k     B                         <^jj0^j=*^
32157:                                                                    falcon
37184:      falcon
38178:evil 464, 579, 592, 605, 2981, 3059,      expedient    7108                     falcon    6154,9855,11501
38754:    1227, 1739, 1741, 3881, 6978,          Liang-chou-fu      4700                  liking hunting with falcon         7406
```


## [2026-10-17T00:02:09.266Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 32110,32162p SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"9855 w\")) print \"leaf\",NR-1}' SOD_pages.txt; sed -n 21395,21406p SOD_pages.txt; sed -n 37178,37186p SOD_pages.txt"
}
```


### [2026-10-17T00:02:09.623Z] TOOL RESULT

```
                                                                       BSTBL, Padm. 44, 55; GMS 807; wVf, TSP
9833 w>n(k)
     wan(k) S, B                                  xjUo^-
                                                                       3.231, 242, 243, 247
                                                                       (to)ra'm
      so, as
                                                               9848 wVyn'y =* w'ryn'k
      Frag. Len. 37.17, 61.7                                        empty B
                                                               9849 wVk                   (Ji^ c~*)*> jia'^J*-
9834 w'n-qt C                                       ^^1             ware (w*ry, wVy) ©Khot. vara ^w^c
     wankat ? ©conj. ^w'n
     so that                                                         VJ pl21; BSTBL pl38; TSP 9, 91625 etc. p274;
      C2 gloss. p229                                                  C2, 31R26-, pi. uV>V, VJ 188; C2, 55V28:
9835 w'nkw => wWkw                                                    BSTii 898.118; wVJfcw, VJ 431; Prolexis. 326;
                                                                      CII 1990 G 19
9836 w'nt C                                  t«j7
     wand (w>ndt) ©pi. demons, pron. ^w-, wW                   9850 w'r'y =* w>r>k
     those                                                          empty C
                                                               9851 w»rc                                              cf4;
      BBB 566; GMS 45, 1402; Hen. Cosm. 312, 114;
                                                                    warc      (w'rch) ©f. adj. ^w'r'k
        C2, 39R6, 40V17, 60V21
9837 w>ntt       M =» w>nt                                          C2, 61V16, 23; BSTii 910.46, 911, 53; TSP 2.851;
                                                                      BSTBL, Dhu. 177; wVyc, MDiii pi 30
9838 w'nw «» w>n>w
9839 w'pVyzt B                                                 9852 w>rch B, S =* w>rc
                                                    j^^
                                                               9853 w'ren S        t                                  J&
     wa-prayzt ? (w'pry'zt) ©elat.
     how excellent                                                  warcan, wacarn ©<*wacarn ©ob. w'rcnyh
      BSTBL, Dhu. 292, Vim. 42; GMS 1313                              ^w'crn, w*cn
                                                                    market f
9840 wyt        M ^ w'pt-
                                                                    Hen. Tales. 466 nb; BBB 136
9841 w'pry'zt =» w'p'r'yzt
                                                               9854 w>r8-/t ? B                     jji\>f<j*fid±*/
9842 w^rmCw) S                              Jl^l- < JU-^*
     waparm(u) =»c}prmw                                             war6/t- ?
     so long
                                                                    GcOturnLen. 93, 8
                                                                    Frag.
     MDii A-15, 10; Anc. Lett. 2.25, 27; GMS 1608
9843 w'pryt =* w>Pr>y5                                         9855 w'ryn'k     B                         <^jj0^j=*^

9844 w'pt- B, S, C                     .          frbsl             warayne (w^yn'y) ©Av. vardYna-,
                                                                      Khwar.wVrnwib; Oss. uari\ Pahl. varisak/varis
     wapat (w'p't) ©impf. =»'wpt-
                                                                    falcon
     (to)fall
     VJ 1022, 205 etc. pl06; TSP 21 ii 13; KG 619;                  TSP I3ii 14 n p228; SCE 359; Ben v. Vxtra et
                                                                                                                   wHmyc

 399
leaf 465
                                                                 6164 nwsc M, C, S(AL)    (oy> j^> j->)«-^ <Jijl=r <L*^
       ambrosia
                                                                      nose ©f. adj. of nw^k
       BSTBL, Dhy. 227; Benv. Notesii 233
                                                                      immortal
6154 nws2 ? B                                     iAj5 O^js*^
     zws ? =>zws                                                      GMS 1273; W-Li 62, 76; BBB b99 f83; Hen.
                                                                        BSOAS 12, 307.19; STi; Sund. AoFviiii 1981,
     falcon
     SCE 226.359; TSP 2.278                                             31V3; STii 6.44; BSTii: C2 gloss, nwsc zw'n(y)

6155 nwswtr B                                     ^Uj^U^T       6165 nwsyw^-         ? B => nsyw'y-, nysyw'y-
11504 zwstmby        M                                                      Schwartz. STSC 134.33 n pl44
      zu-stambe          ©pi. -t ^zwP'st'npy                         11511 zwydm* C                                           jojl^j
      tyrant                                                               zwe8ma ©<*uz-vaedaya            ©f. n. =»zwy5-
      Hen. BSOAS 11.66.8                                                   threat
11501 zws    B                                                              C2, 4V3, 66V4, 104R8, 111V1; Benv. IIJ 1959,
      n/zus ? =»nws2 ?                            J,j9 «■jjAli,                132-6, JA 1955, 330.23
      falcon
                                                                     11512 zwyn»kh M                          (^^y-^/oj
      SCE 226, 359; Hen. Texts. 722 n 1                                    zwinak ?
```


## [2026-10-17T00:02:14.965Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 484 485 486 487 488 489 490; do echo \"== leaf $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n 'بره\\|برّه\\|varrak\\|varak\\|warrak\\|ورک' | head -5; done"
}
```


### [2026-10-17T00:02:15.604Z] TOOL RESULT

```
== leaf 484
== leaf 485
== leaf 486
== leaf 487
== leaf 488
20:بره ح بفتح اول و انی و ظهور ها .
23:و کتانه از عاجز و زیون باشد - و ابره وروی‌قبا
41:بره گر فقو - باخفای‌ها » کنابهازماجز
42:و زبون گرفتن باشد » چدبره بمعنی عاجز وزبون
49:۵ - رگ : برهیختن .
== leaf 489
19:برههی ؟ » بتح اول و ثالی و حیم
23:و نجیب هنود را نز برهم نگویند » و بفتح‌اول گویند - و بمعنی کمر گاه و کم رکوه هم بنظر
27:برهمن است ت که پیر ومرشد - وحکیم ودانشمند
30:برهمن است که اصیل و نجیب - وحکیم سوپیر
40:پیشوابان روحانی؛ یکی از سهطبقةٌ مردم درآیین برهمابی «مزدیسنا ۹4*۵» راجم بتصور عسلمانان
== leaf 490
44:‌ برهنگی _ بهلوی حاامصطاعره «هنای ۲۷۰ ؛ لختث. بودن » عور بودن .
```


## [2026-10-17T00:02:18.907Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==488 || NR==489' BQT_v1_pages.txt | grep -n -i 'بره\\|گوسفند\\|varr\\|var\\|ura\\|۲۶' | head -30"
}
```


### [2026-10-17T00:02:19.450Z] TOOL RESULT

```
69:بره ح بفتح اول و انی و ظهور ها .
72:و کتانه از عاجز و زیون باشد - و ابره وروی‌قبا
90:بره گر فقو - باخفای‌ها » کنابهازماجز
91:و زبون گرفتن باشد » چدبره بمعنی عاجز وزبون
98:۵ - رگ : برهیختن .
101:بره (برح) ونشانةً لحرمی آن
```


## [2026-10-17T00:02:22.627Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==488' BQT_v1_pages.txt | sed -n 1,120p"
}
```


### [2026-10-17T00:02:22.998Z] TOOL RESULT

```
سای هس
و بفتح او وسکون ائی‌نام ماه - و ستارمشتری
باشد ۱ - و بفتح اول و ضم ثانی ابرو را گونند
بر وار ِ بروزن هموار» خانه‌ناستانی
باشد .
پر واده ۳ بروزن عمواره , بالاخانه
و حجر بالای‌حجره باشد - وراهی را نیز کویند
توان نمود .
بر واد » بروزن دمساز, جای‌قرار و آرام
باشد - و نشیمن باز و شاهین و امثال !نرا نیز
۷
پر وازه» بروژن‌دروازه ۰آنشی‌را گونند
که بیش بیش عروی افررزند و خوردلی‌وطعامی
پرو انا با نون مکور وئحتانی‌بالف
کشیده . بلفت بونانی 9 رستنی باشد که مانند
عثفه بر درختها پیچد و میوٌ آن شبیه بانگور
است. بجهت دباغت کردن چرم بکارآبد» و آنرا
بعربی حااق‌الثعر خوانند چه‌از آن ریشها آویزان
میباشد , و باین‌سبب هزاز افثان گویندش .
ثر وه ع بروزن سفدر . فراویزو سجاف
حامد ودامن وسر های‌استن پوستی‌را گونند ۳
۲۱) چك : ژند و باژند .
بروفند
و مخفف بارورهم هست ک:باردار و میومدارباش
و بلغت زند و بازند (۱) بمعنی برادر باشد ۷-
ویمعنی اول بازای تقطمداربروزن ۰ر کز٩‏ وبروزن
رموز هر دو آمده اسث - و جملهرا نیز گونند .
پروسان ۵ - با سن بی نقطه بر وزن
عروسان » مطلق‌امت را گویند ازهر ببغمبری(؟)
که باشد - و کروههای مردمان از هر جن سکه
عاشند .
بروشان ۶ ع با شین نقطمدار بر وزن
خروشان ؛ بمعنی بروسان است که امت پیقمبر
باشد .
پر و شا -بنم اول و ثانی و سکون
الث و فتح شین نقطه‌دار و کاف حاکن » یمعنی
بز و قرو گ » بنتح‌اول و کسر‌فا ؛ بمعنی
فراز و نشیب است که بلند وپست و بلندی‌وپستی
باشد .
۳ وفه - ضم‌اولوثانی وسکون واووفتح
فا » بمعثی دستاروفوطه باش که مندیلو کمربد
پر ومند ٩‏ - بر وژن ننومند » باردار
وبارور و صاحب نفم باشد و بمعنی بر خوردار
و کامیاب هم بنظر آمده است .
هه
ببالای تو درچمن سرونیست
«فرهنکه‌شاهنامه» و رث . لت نامه: برو.
۱ - مصحف: بروز (« . م).
۹ -مر کباز: بر(بار) 4
```


## [2026-10-17T00:02:25.683Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:268 --image 2>&1 | head -80"
}
```


### [2026-10-17T00:02:26.170Z] TOOL RESULT

```
no scan of BQT covers printed page 268 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:02:29.140Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if ($0 ~ /varrak|varak|warrak|uraṇa|urana/) print \"leaf\",NR-1}' BQT_v1_pages.txt | head; grep -n -i 'varrak\\|varak\\b\\|warrak' BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:02:30.433Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:02:34.074Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 476 477 478 479 480 481 482 483; do echo \"== leaf $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -3; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n 'بره\\|بر ه\\|بزغاله\\|گوسفند'|head -4; done"
}
```


### [2026-10-17T00:02:35.359Z] TOOL RESULT

```
== leaf 476
" بر‌سان « بنتح اول می وزن نرسان :
دوشاب میاء رنگه خوشبوی را گویند - و مطلق
امت را لیز کفته‌اند از هر پیعمبی که باشد ٩‏ -
37:( برهان فاطع ۳۷ )
== leaf 477
ده
نسکهای عشهور زند )۱( آست سی و پنج برسم
بدست گیرید ؛ و بجهت نك بشت ٩‏ بیست
== leaf 478
می شیر آن" زین نهادن
سرخ‌مرد گوبند و بعربی عصا الراعی خوانندا ۰
بر شیر فرد ین نهادن - کنابه از
25:و بضی کویند کوهی است در آن جزبر هکه‌شبها
== leaf 479
-- ۷6 سس
بیشتراوفات‌بخر وکاو دهند» وبخورند وبسنی‌دمگر
گفته‌اند ترمایست بپاری و طعم تیژی دارد » تازهٌ
== leaf 480
بر فشا ندن‌ذست ه کنابه ازرقصدن
بر قنجاك » بنتح او و سکون ثالی
و فتح ثاكث و سکون نون و فتح جیم و سکون
== leaf 481
۳
بر گ ید - معروفست - و نوعی از
پیکان تیر هم هست که آنرا بهیشت بر کك بید
== leaf 482
باقاف فارسی هم آمده است- و بکر انی‌طایفه‌ای
بر لنگار دن ع کنابهاز کریختن‌باشد.
بر ۵ - بفتح اول و ثانی بر وزن عجم .
37:برهتی « ختح اون و ثالث و سکون‌انی
39:بر همچیفن ه با جیم فارسی بر وزن بر
44:بر هتیادان - بروزن‌سرشخیدن,مخالفت
49:بر هر ع بر وزن زر کر » بمعنی اتظار
== leaf 483
5
رما ۱ ه بر وزن نتزك ؛ دام جابی
و مقامی و ولایتی است - و لقب جعفر پدر خالد
```


## [2026-10-17T00:02:39.897Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if ($0 ~ /بچه.? ?گوسفند|بچهٔ گوسفند|بچه گوسفند/) print \"leaf\",NR-1}' BQT_v1_pages.txt | head; "
}
```


### [2026-10-17T00:02:40.323Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:02:42.941Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'گوسفند' BQT_v1_pages.txt | head -30"
}
```


### [2026-10-17T00:02:43.276Z] TOOL RESULT

```
3409:وذیل < ولوالی > نویسد : < بلفت‌اهل سمرقند رودة گوسفند را گوین دکه
8204:صحرا بجپت خوایدن گوسفندان سازند .
12516:و گوسفند بجبد و خون از بدن آنها بسکد .
13867:آن باشیر گوسفند بخورند قوت‌باه دهد » ویضی
16638:هبت- و گله و رمة کاو و گوسفند واسب وامثال
16954:باغل- بروزن بابل .جای کاو و گوسفند
17928:لءل و طلا در آنجا هست و گوسفند آنجا را از
21736:هر چیز باشد ۷ - و رود گوسفند وگاو وامثال
25950:گوسفند وبز و آهو و شتر باشده .
25962:۵ . رك: شکل .اشکل , عمروفست که سرکن گوسفند و آخو
26825:بهعنی پوستگال است که پوست زبردنبةٌ گوسفند
29409:ریزند و اکر میسر نباشد شیر گوسفند» و آنرا
30578:عافت زند و بزند(۱) د.ه گوسفند و کار و امتال
31472:و لام حلوابی هم هت - وعزار خانة گوسفند را
```


## [2026-10-17T00:02:49.699Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wr%CC%A5h%E2%82%81%E1%B8%97n' 'https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%D8%BA' 'https://en.wiktionary.org/wiki/warrag'; do python3 tools/fetch_source.py \"$u\" --note 'page 548, root Weren: lamb/crow etymology' 2>&1 | tail -2; done"
}
```


### [2026-10-17T00:02:51.743Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3afd812292290233.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6426beb1702213f5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e2aa0d836d062be.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d9b0d127535889d8.txt
```


## [2026-10-17T00:02:54.431Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 3afd812292290233 6426beb1702213f5 1e2aa0d836d062be d9b0d127535889d8; do echo \"=== $f\"; wc -c $f.txt; grep -n -i -A6 'Etymology' $f.txt | head -40; done"
}
```


### [2026-10-17T00:02:54.760Z] TOOL RESULT

```
=== 3afd812292290233
6314 3afd812292290233.txt
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
84: Etymology 1 
85-
86- 3.1.1 
87- Pronunciation 
88-
89- 3.1.2 
90- Noun 
--
96: Etymology 2 
97-
98- 3.2.1 
99- Pronunciation 
100-
101- 3.2.2 
102- Noun 
--
190: Etymology
191- [ edit ] 
192-
193: See the etymology of the corresponding lemma form.
194-
195- Pronunciation
196- [ edit ] 
197-
198- IPA ( key ) : /bu.rah/ 
199-
--
224: Etymology 1
225- [ edit ] 
226-
227- Ultimately from Proto-Iranian *varn-aka- , from Proto-Indo-Iranian *wr̥Hánas , from Proto-Indo-European *urh₁en- ( “ ram ” ) .
228-
=== 6426beb1702213f5
5762 6426beb1702213f5.txt
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Inflection 
--
143: Etymology
144- [ edit ] 
145-
146: Possibly related to Latin vervēx ( “ wether ” ) and Ancient Greek εἶρος ( eîros , “ wool ” ) . [ 1 ] This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 
147-
148- Noun
149- [ edit ] 
150-
151- *wr̥h₁ḗn 
152-
=== 1e2aa0d836d062be
4250 1e2aa0d836d062be.txt
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
152: Etymology
153- [ edit ] 
154-
155- From a Proto-Iranian root not attested in Middle Persian. Cognate with Baluchi کلاگ ( kalág ) , Mazanderani کلاج ( kalāǰ ) , Gilaki کلاچ ( kəlāč ) , Southwestern Fars قلاغ ( qalâğ ) , قلا ( qalâ ) , Northern Luri قلا ( qelā ) , Ossetian халон ( xalon ) . Probably ultimately onomatopoeic, but perhaps from Proto-Indo-European *ḱer- ( “ crow ” ) ; compare Latin corvus , Ancient Greek κόρᾰξ ( kórăx ) , Proto-Germanic *hrabnaz .
156-
157- Pronunciation
158- [ edit ] 
=== d9b0d127535889d8
132 d9b0d127535889d8.txt
```


## [2026-10-17T00:02:58.400Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 150,175p 6426beb1702213f5.txt; sed -n 224,240p 3afd812292290233.txt; cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo AHD; grep -n -i -A8 '^wren\\|^wrən\\|^wr̥ēn' AHD_watkins1985.txt | head -20; echo IEC; grep -n -i 'lamb' IEC.txt | head; echo WLD; grep -n -i 'u̯ren\\|uren-\\|vren-\\|Lamm' incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:02:58.803Z] TOOL RESULT

```
 *wr̥h₁ḗn 

 lamb in general, or more probably only the male, ram . [ 2 ] 
 Synonym: *h₂egʷnós 

 Inflection
 [ edit ] 

 Athematic, hysterokinetic

 singular

 nominative

 *wr̥h₁ḗn 

 genitive

 *wr̥h₁nés 

 singular

 dual

 plural
 Etymology 1
 [ edit ] 

 Ultimately from Proto-Iranian *varn-aka- , from Proto-Indo-Iranian *wr̥Hánas , from Proto-Indo-European *urh₁en- ( “ ram ” ) .

 See also Mazanderani وره ( vare ) , [ 1 ] Sanskrit उरण ( úraṇa ) , Central Kurdish بەرخ ( berx ) , Northern Kurdish berx , Zazaki verek , Baluchi گْوّرگ ( gwarag ) , Ancient Greek ἀρήν ( arḗn ) , Old Armenian գառն ( gaṙn ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /bar.ˈra/ 

 ( Dari, formal ) IPA ( key ) : [bär.rá] 

 ( Dari, formal ) IPA ( key ) : [bär.rá] 
 ( Kabuli ) IPA ( key ) : [bär.rá] 

AHD
IEC
251:aguniio, aguhniió "lamb, yean'. WP I, 39. See next. OE eanian; Du. oonen; Cz. jehniti se
252:agunos, aguhnos, (agunos) “lamb”. WP I, 39 Gk. amnós, amnís; Lat. agnus; Ir. uan; W oen; OCor.oin; Cor.on; Br. oan; OE eane; (a) OCS agne; Cz. jehné; Latv. (Gmc.LW?) aun ‘ram’
1514:bhorda, iə (0-gde variant of bherdà, q.v.) ‘with young, pregnant. Illyr. bardia; Alb. barsé; Lat. forda; Umb. furfað (for *furfaf: Lat. fordās “in lamb’. Cf. Umb. mefiaí: mediae); MHG cf. barzen ‘swell, be full; Swiss barzen, id.; Barz ‘crowd’: Alb. m-bars ffecundate'
1894:bhuĝos, ios, o(n) ‘small animal’. WP II, 189 Av. büzo ‘buck’; Per. buz ‘goat; Oss. bodz, Dig. bodzo, id.; Arm. buc, a-st. lamb; MHG boc, gs bockes ‘he-goat’; ON bokkr, bukkr, id. Finn. LW pukki, id.
2763:dhel$- ‘pet, fondle, suckle’. Cf. WP I, 866 & ` 830. See dhél- (1), aĝō Gk. thélgo ‘stroke, charm’; a-thélgo “milk; suck’; Alb. (ambig.) pérké-dhel (fondle', loss of *$ as in mjel, v. ‘milk’) beside dhelé *fond- ling’; ON dilkr (^sucking-lamb' or "os"
2773:Oss. dalis ‘lamb’; Gk. thēlé ‘teat’: thëlus & theleia ‘female’; Alb. (*-é-) djalë ‘boy’, dele ‘sheep’; cf. also djelmé, djemë (‘boys’, fr. *dhelmenes); Umb. feliu, filiu, adj. “sucking; milch’; MIr. del, dela ‘teat’ beside del fola ‘leech’; OHG tili ‘nipple’; OE delu, id.; ON dæla *suction-pump'; Li. delé ‘leech’, beside pirma-dele ‘mother of first-born’; -delys “first- born’; Latv. dels ‘son’, dele ‘leech’
3962:gëros, à (2) (?) ‘young animal’. Alb. gorë ‘pup’; Li. gëras “lamb”
4128:(glombh- in Gmc. only. Cf. OE clamm, clemman; MHG klambe, klamme and klam- men, klamben; ON klombr, gs klambrar. Cf. glembh-)
4131:‘muzzle, bridle; MHG  klamer(e) “vice, bracket; G Klammer E dial. cf. to clammer ‘clutter; ON klombr, gs klambrar “vice, clamp, cramp; tight corner”; Icel. cf. klambra, v. ‘bungle’
5085:ghür-(1) *sway, rollick, revel'. Cf. ghül- and gür- (1). Evidence ambig. Skt. (ambig.) ghür- nàmi (‘sway’, but equally to ghül-, q. v.); Cz. hytit, v. (2) ‘reveľ, but see gür-; (R cf. elo girla ‘estuary’, but equally to gür-, q. v.); Latv. cf. güra ‘strutter, flamboyant person?
WLD
472:jahrige Tiere wie russ. jdrecz      einjahriger Biber     jdrla ..Schaflamm",    .
628:    ai.inddhe „entzundet, entflammt (pass, idhyate pf. idhU, ppp. iddhd-h ),                          ,
691:in ags. mlan „brennen“, in-, on-celan „in Brand stecken      eel, al „Flamme“
3657:ag°h-no-s            (z.   T. auch *ag*inos‘i)         „Lamm“.
3658:      Lat. agnus  fem. -a „Lamm“ ( agnlle „Schafstall“, obne Suffixverwandt-
3663:Yerbum jagniti „lammen“);     gr. apvos, dfivg „Lamm“ (Walter KZ. 11,
3664:429, Fick KZ. 20, 175); air. Ran cymr. oen, acorn, oin, bret. oan „Lamm“
3671:KG. I 32) ags. Sanian engl. to yean „lammen“, ndl. oonen ds. (aus *aundn
3676:aksl. jagnc „Lamm“ (um das bei Bezeichnungen junger Tiere belicbte
3677:Formans -qt- erweitert), jagmcb „Lammehen“ (Fick aaO; a- wohl Anlaut-
```


## [2026-10-17T00:03:03.070Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=277 && NR<=280' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i -B2 -A6 'urana\\|urana-\\|barra\\|garn\\|Widder' | head -50; echo AHD; grep -n -i 'wren-\\|wr.n-\\|URANA\\|ram\\b' AHD_watkins1985.txt | head; echo IEC; grep -n -i 'urana\\|wrēn\\|ūrana\\|^u̯r\\|arḗn\\|arén' IEC.txt | head"
}
```


### [2026-10-17T00:03:03.571Z] TOOL RESULT

```
181- 4.     ner- „Wolle; Wolltier, Schaf".
182-                                 wohl ..Wolltriiger"), urd f. ..Schaf" (fem.
183:       Ai. urabhra- m. .,Widder“ (d. i.
184- Kurzform zum vorigen?            Qu. ep. 119), n-Ableitung ttrana- m.
185-                                             Schulze
186: .YYidder, Lamm", np. harm „Lamnv‘ (* varnalc pehl. rural: „Widder"            ,
187-
188-
189- arm. gain, gen. garin ,.Lamnr (Iliibschmann KZ. 23, 16 Anm. 1. Arm.
190- Gr. I 432)
191-       gr. agrjv , agvog, gort. fagyv ..Lamm", agvay.ig „Schaffell”, agreidg ,,Y idder",
192-  schwundstufig *j-gyv in horn, n oti’-ggyr                         ..reich   an Schafen" ulanach spates
AHD
63:The comparative method remains today the most powerful device for elucidating lin- guistic history. When it is carried to a suc- cessful conclusion, the comparative method leads not merely to the assumption of the previous existence of an antecedent common language, but to a reconstruction of all the salient features of that language. In the best circumstances, as with Indo-European, we can reconstruct the sounds, forms, words, even the structure of sentences—in short, both grammar and lexicon—of a language spoken before the human race had invented the art of writing. It is worth reflecting on this accomplishment. A reconstructed gram- mar and dictionary cannot claim any sort of completeness, to be sure, and the reconstruc- tion may be changed because of new data or better analysis. But it remains true, as one distinguished scholar has put it, that a recon- structed proto-language is “a glorious arti- fact, one which is far more precious than anything an archaeologist can ever hope to unearth.”
102:The comparative study of Indo-European poetics has shown that such compounds were considered particularly apt for elevated, for- mal styles of discourse; they are a salient characteristic especially of Indo-European poetic language. In addition, it is amply clear that in Indo-European society the names of individual persons—at least in the priestly and ruling (or warrior) classes—were formed by such two-member compounds. Greek names like Sophocles, “famed for wisdom,” Celtic names like Vercingetorix, “warrior- king,” Slavic names like Wenceslas, “having greater gory,” Old Persian names like Xerxes, “ruling men,” Germanic names like Bertram, “bright raven,” are all compounds. The type goes as far back as Proto-Indo-Huropean, even if the individual names do not. English family names continue the same tradition with such types as Cartwright and Shake- speare, as do those of other languages, like Irish (O’)Toole, “‘people’s valor.”
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
344:bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
348:bhugo-. Male animal of various kinds; stag, ram, he-goat. 1. Germanic *bukkaz (possibly borrowed from the Celtic form in 2. below) in: a. Old English buc, bucca, stag, he-goat: BUCK}; b. Middle Dutch boc, bok, buck: BLEs- BOK, BONTEBOK, SPRINGBOK, STEENBOK; C. Old High German boc, buck: GEMSBOK. 2. Celtic *bukkos, he-goat, in Old French boc, buck: BUTCHER. [Pok. bhiigo-s 174.]
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
396:dhwer-. Door, doorway (usually in plural). Originally an apophonic noun *dhwor-, *dhur-, in the plural, designat- ing the entrance to the enclosure (*dhwor-o-) surround- ing the house proper. 1. Zero-grade form *dhur- in suffixed forms *dhur-ns (accusative plural) and *dhur-o- (neuter) respectively in Germanic *durunz and *duram in Old English duru, door (feminine, originally plural), and dor, door (neuter): DooR. 2. Suffixed o-grade form
417:ed-. To eat; original meaning “‘to bite.” See dent-. 1. Ger- manic *etan in: a. Old English etan, to eat: EAT; b. Old High German ezzen, to feed on, eat: ETCH; c. Middle Dutch eten, to eat: orT; d. Germanic compound “fra- etan, to eat up (*fra-, completely; see per’), in Old English fretan, to devour: FRET). 2. Latin edere, to eat: EDACIOUS, EDIBLE, ESCAROLE, ESCULENT, ESURIENT; COMEDO, COMESTIBLE, OBESE. 3. Zero-grade form *d- in Latin compound prandium (< *pram-d-ium), “first meal,” lunch (*pram-, first; see per’): PRANDIAL. 4. Suf- fixed form *ed-un-d in Greek oduné, pain (< “gnawing care”); ANODYNE. [Pok. ed- 287.]
452:er-3. Base of designations of various domestic horned animals. Extended form *eri- in Latin ariés, ram: ARIES. [Pok. 2. er- 326.]
IEC
19771:uarén- (uaron-, uarn-) ‘lamb’. WP I, 269 Pahl. cf. (dim.) varak, id.; Per. bare, id. (and *kid"); Oss. cf. wárlnk, Dig. wär, wärinkä, pl. wálità (sic), id.; Arm. garn, gs: garin, ab. s. -amb, id.; Cypro-Minoan warno (oblique cases), id.; Cret.. waren, Gk. arén, gs: arnós, mf. id.
```


## [2026-10-17T00:03:07.627Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'barra\\|arēn\\|úraṇa\\|urana' SYN.txt | head -8; grep -n -i 'crow' SYN.txt | head -5; grep -n -i 'kalāγ\\|kalāgh\\|kalâğ\\|kalag' SYN.txt KLN_1966.txt | head"
}
```


### [2026-10-17T00:03:08.074Z] TOOL RESULT

```
4177:Dan. faar vaedder Sw. far bagge, viédur, gumse OE sctap ramm, weder ME _ schepe ram, wether NE sheep ram Du. _—schaap ram OHG | scaf ram(mo), widar MHG schaf - wider, ram NHG ss schaf widder, schafbock Lith. avis tekis, avinas Lett. atta, avs auns, tekulis Chsl.  ovica ovinit SCr. ovca ovan Boh. _ ovce beran Pol. owca baran Russ. ovea baran Skt. avi- mesa-, urana-
4229:Skt. urana-, with wra- ‘ewe’ : Lat. verver ‘wether’ (3.27), Grk. apy ‘lamb’, etc. (3.29).
4274:2. Grk. apnv (Cret. rapqy), gen. apvos, dim. dpviov, NG dpvi, dpvax : Skt. urad- ‘ewe’, urana- ‘ram’, Lat. vervex ‘wether’, Grk. épov ‘wool’, Aeol. éepos lit. ‘having wool on’ used for ‘male sheep’ (érepor kal dpynades ‘male sheep and ewes’), all going back to a word for ‘wool’ or the wool-bearing animal. Walde-P. 1.268 ff.
21132:Sp. barato, fr. baratar ‘buy a thing at less than its value’ : It. barattare ‘ex- change’, OFr. barate ‘strife, trade, de- ceit’, etc., a widespread group, including NE barrat (obs.) and barter, but of uncertain orig. REW 9438 a (giving as source ON baraita ‘strife’ but this rather fr. OFr.). Gamillscheg 78. NED s.v. barrat. Diez 41.
27975:3 Lat, ridére, both ‘laugh’ and ‘smile’ (VLat. *ridere > the Romance words for augh’), but for ‘smile’ esp. sub-ridére (VLat. *surridere > the Romance words for ‘smile’), etym. dub. Walde-P. 1.277 (twriz-d- : Skt. vrid- ‘be embarrassed, ashamed’, etc.). Ernout-M. 865 (: Skt. hntd- ‘play, jest’).
30096:Lat. turpis ‘ugly, base, shameful’, used in both a moral and a physical sense, perh. as orig. describing what one tums away from: Grk. rpémw ‘turn’; cf. Skt. trap- ‘be embarrassed, ashamed’, trapa- “embarrassment, shame’, also Fey trent historical develop-
2684:following the husband, hence in sense b); ‘taking the hand’ (either husband taking the hand of the bride, hence sense a, or conversely, hence sense b); ‘veiling’ (of the bride, hence orig. in sense b) ; ‘crown- ing’ (orig. used of the one performing the ceremony, then in mid. or refl. ‘get crowned’, of either party).
2688:NG orepav-dvopat, used with special reference to the ceremony, lit. ‘be crowned’ fr, orépavos ‘crown’ (wreaths are placed on the head of the bride and groom). Hence the similar use of Rum. cununa (fr. sb. cunund, Lat. corona ‘crown’) and other Balkan words. Pus- cariu 448. Sandfeld, Ling. balk. 35.
3739:7. Skt. kula- ‘family’ in narrow and broad senses, also ‘herd, crowd’, etc. : ChSl. éeljadt ‘household, body of sery- ants’, Walde-P. 1.517. Berneker 141 f.
4658:Av. xzara- (NPers. xzar) : Skt. khara- ‘harsh’, also ‘ass’, ‘mule’, ‘crow’, etc. fr. their harsh cries. Barth. 531.
5102:2. NE bug (the pop. word in U.S.; in British use ‘bedbug’), prob. the same word as ME bugge ‘scarecrow, bugbear’
SYN.txt:8780:5.34 PITCHER, JUG ; aurkjé (gen. pl.) Lith. qsotius, izbonas ag, aupopedsy RANTS) Goth krukka Lett. kriza rk. aie la Dan. krukke ChSl. kritéagit, &vanit aver ay orapvl Sw. kruka, krus (vritét) NG urceus OE crég, criice SCr. kréag, vré Jat poccale, bracca ME picher — Boh. dzbdan y eruche, br ae NE pitcher, jug Pol. — dzban 3 * — gdntaro, JarT J Du. kruik Russ. kuvin, kruzka an urcior OHG  kruog pea kalaga- i ns i . eee ler (ciolarn) MEG ,,kruoc M Niteu eS , NHG krug W. pise brog p e of the words listed here under | of jar’, perh. an old loanword. Lat. U r 2 5 sas lied to a great variety of | urceus or orca > OE orc, Goth. aurkjus
SYN.txt:8826:7. Skt. kalaga- (vessel for holding liquids, esp. the soma) : Grk. «ict, Lat. caliz ‘cup’ (5.35).
SYN.txt:8834:Skt. kalaga- ‘pot, pitcher’, root connec- tion? Walde-P. 1.442. Ernout-M. 136. Walde-H. 1.138 f. Grk. roripiov (NG rorfpx ‘a glass’) : mtvw ‘drink’, ete. Walde-P. 271 ff. Grk. xbreddov ‘large drinking-cup, beaker’ (> NG xtmeddo) : Lat. ciipa ‘tub,
```


## [2026-10-17T00:03:12.178Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; grep -n 'ورغنه\\|ورغن' BQT/BQT_v4_pages.txt BQT/BQT_v5_pages.txt | head; grep -n 'کلاغ' BQT/BQT_v3_pages.txt | head -5; grep -n 'بره\\b\\|برّه\\|BARRE\\|BARRA' ARY/ARY_pages.txt ARY/ARY_latin_index_pages.txt | head -8"
}
```


### [2026-10-17T00:03:12.569Z] TOOL RESULT

```
12691:‏از جنس کلاغ .
13484:و بانگه کلاغ ‎AST,‏ - و بمعنی فتنه وآشوب
13845:© - نم اول ( عی ) زاغ , کلاغ . 1 - رك ‎oi‏ ؛ غرچه .
14939:ساء و سفید و آترا عکه و کلاغ یسه (۷) حم
14975:‏0 چك ‎bate BIT:‏ چش : کلاغ‌پشه ؛
ARY/ARY_latin_index_pages.txt:3580:BARRAN RUSSIAN) +3) WAR HOSSETIC) sl
ARY/ARY_latin_index_pages.txt:10909:MACKENZIE", we (CAMEL) 106 BARRAO PORTUGUESE) J's 4
ARY/ARY_pages.txt:226:8 اوستایی: ۸1۸183۸ سانسکریت: ۸11۸7۸ بازگشت به برهان قاطع» صفحه‌ی ۹۳۴
ARY/ARY_pages.txt:291:همریشه‌اند می‌توان نتیجه گرفت که آنان در رام کردن اسب و استفاده از ترابرهای چرخدار پیشگام
ARY/ARY_pages.txt:560:واژه‌ی بنیادین را احیاکرد. مثلاً پس از تعبین برابرهای واژه‌ی «زمین» (سانسکریت: 4۵7۸8 یونانی؛ . ,
ARY/ARY_pages.txt:963:(۸7۳8۸) الهه‌ی خرد ودانش و فنوری بود. در هند نیز سه «کست» (۸8772) به نام‌های «برهمان ۱
ARY/ARY_pages.txt:1035:می‌شد. (برابرهای این واژه چنین‌اند - سانسکریت: ۷181۳۸77؛ لیتوانی: ‎٩۷18871۳۸75‏
ARY/ARY_pages.txt:1139:اندازه‌ای است که برخی از واژه‌ها و جمله‌های سانسکریتکاملاً مشاب پرابرهای اوستایی ود هستند.
```


## [2026-10-17T00:03:15.495Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; grep -n 'LAMB\\|URANA\\|ARE[NM]\\b' ARY/ARY_latin_index_pages.txt | head; grep -n 'WER-EN\\|WREN\\|WER-3\\|WER EN' ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:03:15.810Z] TOOL RESULT

```
3440:ror sebb iby GEBAREN (GERMAN) lat
3574:TRAN, URANA, VURAN URA-, VAREN, AVESTAN) glee
3576:ARONS, WAREN (GREEK) gh VARMAK, | :(OLD RERSIAN) dlls y+ 34
3586:MACKENZIE: (LAMB) 121 VAN HOLD IRISH) sy 5521p!
4748:VAREN (DANISH) Sats PIPARTI, PRU:, PR-
4751:VAREN (DUTCH) gache (LATIN) 3
6211:ONIONS: (YEAST) 1019 GAREN, GISCHT — (GERMAN) ,glT
6918:CHVORY (CZECH) Soy SCHWARE, SCHWAREN, SCHWERT
9853:‘APSPAREM, SPARNAL SPARAITI AAVESTAN) glo
9968:STELLA, STERLA_ ALATIN) 3 STAR, STARO, STAREM
2953:ar) 1ebG ob, WRENDE ALBANIAN) glST
4229:POWER ENGLISH) goSSi PADIXSHAYA-, PATI-
```


## [2026-10-17T00:03:18.839Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; sed -n 3565,3592p ARY/ARY_latin_index_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"URANA, VURAN\")) print \"leaf\",NR-1}' ARY/ARY_latin_index_pages.txt; grep -n 'pdf page' ARY/ARY_latin_index_pages.txt | awk -F: '$1<3574' | tail -1"
}
```


### [2026-10-17T00:03:19.230Z] TOOL RESULT

```
POKORNY, = SS”™S*~*~S~*~«S BARN {OLD SAXON) AS pip Ste
BARNHART: (BAIRN) 71 HOLD HIGH GERMAN) op gil
MACKENZIE: (CHILD) 106 BARN
ONIONS: (BAIRN) 69 BEARN (OLD ENGLISH) op 3S)
SKEAT: (BAIRN) 44 BAIRN ENGLISH) ,gS&i
ver rgbtoly| © BARN DANISH) jails
leatlosl
23)9 pte “2g! Gedy AED Lodls cal GO “V
ngs ay 15259 Sed 9 hed 9 gt} GUUS 9 Ble 9 shes! 254 at pT
TRAN, URANA, VURAN URA-, VAREN, AVESTAN) glee
GARN, GARIN (ARMENIAN) .¢,l URAN
ARONS, WAREN (GREEK) gh VARMAK, | :(OLD RERSIAN) dlls y+ 34
VERVEX LATIN) oS VARANA
BEDE DANISH) Sails VARAK, WARRAG, — :(PAHLAVI) 54
BARAN, BARANEK (POLISH) gt} VARRAN
BARRAN RUSSIAN) +3) WAR HOSSETIC) sl
BERANEK (CZECH) So (SANSKRIT) <x Sie
[pdf page 126]
em
REFERENCES beh BARANCHEK (SLOVAK) S101
poKoRe ==~O*~*~S*~*«s VERAS LITHUANIAN) ge)
MACKENZIE: (LAMB) 121 VAN HOLD IRISH) sy 5521p!
BUCK: 156-160
(MALLORY & ADAMS: URHEN
eet
pea ble Sid 3205 cel om
-
for on |
leaf 124
3555:[pdf page 125]
```


## [2026-10-17T00:03:30.517Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://vajehyab.com/?q=%D9%88%D8%B1%D8%BA%D9%86%D9%87' 'https://en.wiktionary.org/wiki/%D9%88%D8%B1%D8%BA%D9%86%D9%87'; do python3 tools/fetch_source.py \"$u\" --note 'page 548, root Weren: varghaneh falcon' 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:03:31.837Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/94a3bdc1335cbe32.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9f6195e035250e35.txt
```


## [2026-10-17T00:03:34.501Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c 94a3bdc1335cbe32.txt 9f6195e035250e35.txt; grep -n 'ورغنه' 94a3bdc1335cbe32.txt | head -20; grep -n -i -A4 'Etymology' 9f6195e035250e35.txt | head -20"
}
```


### [2026-10-17T00:03:34.841Z] TOOL RESULT

```
1886 94a3bdc1335cbe32.txt
 156 9f6195e035250e35.txt
2042 total
4:TITLE: معنی ورغنه | واژه یاب
6:معنی ورغنه | واژه یاب
```


## [2026-10-17T00:03:37.982Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%88%D8%B1%D8%BA%D9%86%D9%87/' --note 'page 548, root Weren: varghaneh falcon (Dehkhoda/Moin)' 2>&1 | tail -1"
}
```


### [2026-10-17T00:03:40.791Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e59b070d628d0d03.txt
```


## [2026-10-17T00:03:43.009Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c e59b070d628d0d03.txt; grep -n 'ورغنه\\|ورغن\\|شاهین\\|باز\\|عقاب' e59b070d628d0d03.txt | head -20"
}
```


### [2026-10-17T00:03:43.528Z] TOOL RESULT

```
4241 e59b070d628d0d03.txt
4:TITLE: ورغنه - معنی در دیکشنری آبادیس
6:ورغنه - معنی در دیکشنری آبادیس 
10: ورغنه
15:زبان های ترکی�در چند مرحله بر�زبان فارسی�تأثیر گذاشته است. نخستین تأثیر زبان ترکی بر پارسی، در زمان حضور سربازان تُرک در ارتش�سامانیان�روی داد. پس از آن، در زمان فرمان روایی�غزنویان، �سلجوقیان�و پس از�حملهٔ مغول، تعداد بیشتری�وام واژهٔ�ترکی به زبان فارسی راه یافت؛ اما بیشترین راه یابی واژه های ترکی به زبان فارسی در زمان فرمانروایی�صفویان، که ترکمانان�قزلباش�در تأسیس آن نقش اساسی داشتند، و�قاجاریان�بر ایران بود.
```


## [2026-10-17T00:03:52.982Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; command ls page-54*.json | head; python3 -c \"\nimport json;d=json.load(open('page-538.json'));e=d['entries'][0];print(d.keys(),e.keys());print(e['nodes'][0].keys());print(d['verified_by'])\""
}
```


### [2026-10-17T00:03:53.705Z] TOOL RESULT

```
page-54.json
dict_keys(['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']) dict_keys(['entry', 'root', 'verdict', 'modern_form', 'note', 'note_fa', 'sources', 'ref_check', 'consulted', 'nodes'])
dict_keys(['id', 'lang', 'words', 'verdict', 'derivation', 'derivation_fa', 'sources', 'ref_check', 'consulted'])
claude-opus-5.5
```


## [2026-10-17T00:04:53.770Z] TOOL CALL #40: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-548.json",
 "content": "{\n  \"pdf_page\": 548,\n  \"book_page\": 518,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Weren\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *wr̥h₁ḗn (gen. *wr̥h₁nés) 'ram, lamb' (Pokorny u̯eren-, IEW 1170; older *u̯r̥ēn-)\",\n      \"note\": \"Root, label and gloss are correct: Pokorny IEW 1170 'u̯eren- ram, sheep, lamb' (Skt. úraṇa-, Gk. arḗn/arnós, Arm. garn, NP barra < *varnak, Pahl. varak). The modern reconstruction is *wr̥h₁ḗn (Wiktionary), with Indo-Iranian *wr̥Hána-. The bird-name branch (Av. vārəγan-/vārəṇjan- 'a bird of prey' read as 'lamb-slayer') follows Humbach's interpretation, which Pokorny cites; Bartholomae left the meaning open. The 'kalâğ' (crow) link at the end is not accepted by modern sources.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wr̥h₁ḗn (پوکورنی: u̯eren-) به معنای «قوچ، بره» است و سنسکریت úraṇa-، یونانی arḗn، ارمنی garn و فارسی «برّه» از آن آمده‌اند. ریشه، برچسب زبان و معنا در کتاب نورایی درست است. شاخهٔ دوم، یعنی نام پرندهٔ شکاری اوستایی vārəγan- که به «بره‌کُش» تعبیر شده، برداشت هومباخ است که پوکورنی هم آورده، و با احتیاط پذیرفتنی است. اما پیوند «کلاغ» با این ریشه را پژوهش امروزی (هرن، ویکی‌واژه) رد می‌کند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wr%CC%A5h%E2%82%81%E1%B8%97n\",\n        \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1170\", \"status\": \"supports\", \"note\": \"POK_full.txt l.93480 ff., 'Root / lemma: Ueren- … Meaning: ram, sheep, lamb … Old Indie urana- … compare npers. barra (*varnak) \\\"lamb\\\"; Pahlavi varak \\\"aries, ram\\\"; Iran. varan-jar-, vara-γna \\\"Lämmerschläger\\\" (Humbach DLZ. 78, 299 f.); Armenian garn … gr. arēn' — 'Page(s): 1170'. This matches the root box exactly.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 269 f. (WLD_Bd1_pages.txt leaves 277-280)\", \"stance\": \"supports\", \"note\": \"'Ai. urabhra- m. Widder … n-Ableitung urana- m. Widder, Lamm, np. barra Lamm (*varnak) pehl. varak Widder … arm. garn, gen. garin Lamm … gr. arēn, arnos, gort. warēn Lamm'\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt l.19771\", \"stance\": \"supports\", \"note\": \"'uarén- (uaron-, uarn-) lamb. WP I, 269 Pahl. cf. (dim.) varak, id.; Per. bare, id. … Arm. garn … Cret. waren, Gk. arén, gs. arnós'\"},\n        {\"src\": \"SYN\", \"where\": \"§3.29 LAMB, SYN.txt l.4274\", \"stance\": \"supports\", \"note\": \"'Grk. arēn (Cret. warēn) … : Skt. urā- ewe, urana- ram, Lat. vervex wether … Walde-P. 1.268 ff.'\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\", \"note\": \"grep for 'wren-', 'URANA' found no entry for this root in the 1985 Watkins appendix (only er-3 'ram' for Lat. aries).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"varnak\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"*varnak(a)- is a reconstructed Old Iranian form, not an attested Avestan or Old Persian word. It is the zero-grade *wr̥Hn- of *wr̥h₁ḗn plus the diminutive suffix -aka-, Proto-Iranian *varn-aka- (Wiktionary). Hübschmann and Horn set it up to account for NP barra, with the assimilation -rn- > -rr-. The form and meaning are right, but it should carry an asterisk; no Avestan or Old Persian text has it.\",\n          \"derivation_fa\": \"صورت *varnaka- در هیچ متن اوستایی یا پارسی باستان نیامده و ساختهٔ زبان‌شناسان است: ستاک ضعیف *varn- از ریشهٔ هندواروپایی *wr̥h₁ḗn به‌اضافهٔ پسوند کوچک‌ساز -aka-. هوبشمان و هرن این صورت را برای توضیح «برّه» بازسازی کرده‌اند (همگونی rn به rr). معنا و ساخت درست است، ولی باید ستاره‌دار و بازسازی‌شده نوشته شود، نه واژه‌ای اوستایی یا پارسی باستان.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1170\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'compare npers. barra (*varnak) \\\"lamb\\\"'. Pokorny gives the form as a starred reconstruction, not as an Avestan or Old Persian word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.5283 and l.9287 (Persische Studien §§ on rr)\", \"stance\": \"supports\", \"note\": \"'barra Lamm aus *varn-ak, skr. urana-, gr. warēn-' and 'barra, bara Lamm aus *varnak, idg. vr̥ren-, skr. urana-, arm. garn'\"},\n            {\"src\": \"BRT\", \"where\": \"grep varna/varənaka\", \"stance\": \"silent\", \"note\": \"Bartholomae has no Avestan *varnaka- 'lamb', so the word is unattested in Old Iranian.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt [pdf page 125-126] s.v. بره\", \"stance\": \"partial\", \"note\": \"Aryanpur lists 'VARNAK (OLD PERSIAN)' beside 'URAN, VAREN (AVESTAN)' and 'VARAK, WARRAG (PAHLAVI)'. He gives the same unstarred Old Persian label as Nourai.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"varrak; vâra-ğna, vâre-ğna, vâren-žar, varâğ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"MP warrag 'lamb, ram; Aries' (PHD), written wlk', is a direct continuation of *varnaka-, with -rn- > -rr-. This part is confirmed. The bird names vāra-γna-/vārəγan- and vārən-jan- (Nourai's 'vâren-žar', Pokorny's 'varan-jar-') are Avestan, not Pahlavi. They occur in Yašt 14.19 and 14.35 as the bird form of Vərəθraγna. Humbach reads them as *vara-γna- 'lamb-slayer' (vara- 'lamb' + -γna- 'striking', PIE *gʷʰen-). Pokorny accepts this, but Bartholomae left the meaning open ('Eig. Bed.?'), so the reading is plausible but not settled. MP warāγ means 'crow' (PHD). Calling it 'lamb killer' depends on the same Humbach analysis.\",\n          \"derivation_fa\": \"پهلوی warrag «بره، قوچ؛ برج حمل» (مکنزی) با همگونی rn به rr مستقیماً از *varnaka- آمده و درست است. اما vārəγna- / vārəṇjan- واژه‌های اوستایی‌اند، نه پهلوی: نام پرنده‌ای شکاری که در بهرام‌یشت (یشت ۱۴) پیکر ایزد بهرام است. هومباخ آن را *vara-γna- «بره‌کُش» تعبیر کرده و پوکورنی پذیرفته، ولی بارتولومه معنای اصلی آن را نامعلوم دانسته است. پهلوی warāγ هم به معنای «کلاغ» است. این بخش با احتیاط پذیرفتنی است و برچسب «پهلوی» برای صورت‌های اوستایی نادرست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:1170\", \"status\": \"supports\", \"note\": \"'Pahlavi varak \\\"aries, ram\\\"; Iran. varan-jar-, vara-γna \\\"Lämmerschläger\\\" (Humbach DLZ. 78, 299 f.)' (POK_full.txt, IEW 1170)\"},\n            {\"ref\": \"BQT:268\", \"status\": \"not_found\", \"note\": \"BQT vol. 1 p. 268 should hold the بره entries with Mo'in's footnote. ref_page.py has no scan for vol. 1, and the OCR in BQT_v1_pages.txt is poor. Grepping 'بره', 'گوسفند', 'varrak/varak' found leaf 488 with the بره/برو… headwords but no legible Pahlavi footnote.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt l.607 (p. ~90)\", \"stance\": \"supports\", \"note\": \"'warrag [KMMA < ?; wlk' | M wrg, N barra] lamb, ram; astr. Aries' and 'warāɣ [wl'g | J bry] crow'\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt l.3979, 3428\", \"stance\": \"partial\", \"note\": \"'*varrak [wlk'] 717-24.26, 87.9' and the reading 'wlk' (= varrak)' adopted by Nöldeke for the ram in Kārnāmag. Nyberg confirms the word but disputes that passage.\"},\n            {\"src\": \"BRT\", \"where\": \"leaf 775, s.v. vāra-γan-, vārən-jan-\", \"stance\": \"partial\", \"note\": \"'vāra-γan- m. Name eines Vogels … Yt. 14.19; 14.35 … Eig. Bed.?' and 'vārən-jan- m. Name eines Vogels … Yt. 14.35 … Des selben, der sonst vāraγan- genannt wird'. Bartholomae gives no 'lamb' etymology.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"w`rğn`k\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian w'rγn'k /wārayne/ 'falcon' is well attested. Gharib's entry 9855 derives it from Av. vārəγna- and compares Khwarezmian w'rγnwk and Ossetic wari. It descends from Old Iranian *vārəγna-, so it is a cognate of the Avestan bird name, not a descendant of Pahlavi. The word itself is correct. The 'lamb-slayer' etymology above it remains Humbach's hypothesis.\",\n          \"derivation_fa\": \"سغدی w'rγn'k (خوانش wārayne) به معنای «شاهین، باز» در متن‌های بودایی سغدی آمده است. قریب (شمارهٔ ۹۸۵۵) آن را با اوستایی vārəγna-، خوارزمی w'rγnwk و آسی wari هم‌ریشه می‌داند. پس این واژه از ایرانی باستان *vārəγna- آمده و هم‌ریشهٔ واژهٔ اوستایی است، نه بازماندهٔ پهلوی. خود واژه و معنایش درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:398\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 465 (printed p. 399; the entry runs over the page break from 398): '9855 w'ryn'k B … warayne (w'ryn'y) ©Av. varəγna-, Khwar. w'rγnwk; Oss. uari … falcon'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"leaf 775 s.v. vāra-γan-\", \"stance\": \"supports\", \"note\": \"Gives the Avestan source word 'Name eines Vogels', Yt 14.19, 35.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1170\", \"stance\": \"partial\", \"note\": \"Pokorny cites only 'Iran. vara-γna \\\"Lämmerschläger\\\"' and says nothing of Sogdian.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"barreh; varğeneh; kalâğ\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"barreh: NP barra < MP warrag < *varnaka-. NP b- for MP w- is the regular word-initial change (cf. warg > barg, wārān > bārān), and the final -ag is lost. This is confirmed by Horn, Hübschmann and Wiktionary, with dialect cognates Mazand. vare, Kurd. berx, Bal. gwarag. varğeneh 'falcon' is a learned or literary form taken from Av. vārəγna- with initial v- kept. It is not an inherited NP word, so it is plausible only as a revival. kalâğ 'crow' is disputed. Horn (no. 862) records the old comparison with Av. vārəγna- and Pahl. varāγ but rejects it in favour of Nöldeke: NP k- cannot come from Iranian v-, and 'raven' does not fit the Avestan word. Wiktionary gives kalāγ as onomatopoeic (cf. Bal. kalāg, Gilaki kəlāč), perhaps from PIE *ḱer- 'crow'.\",\n          \"derivation_fa\": \"«برّه» از پهلوی warrag و آن از *varnaka- آمده است. w آغازین فارسی میانه در فارسی نو به b بدل شده (مانند warg > برگ، wārān > باران) و پسوند -ag افتاده است. این بخش را هرن، هوبشمان و ویکی‌واژه تأیید می‌کنند. «ورغنه» واژه‌ای کتابی است که مستقیماً از اوستایی vārəγna- گرفته شده و بازماندهٔ طبیعی فارسی نیست. اما «کلاغ» نمی‌تواند از این ریشه باشد: k فارسی از v ایرانی برنمی‌آید، و هرن (شمارهٔ ۸۶۲) به پیروی از نولدکه این پیوند را رد کرده است. ویکی‌واژه «کلاغ» را نام‌آوا می‌داند (هم‌ریشه با بلوچی kalāg). ادعای نورایی دربارهٔ «کلاغ» را پژوهش امروزی نمی‌پذیرد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87\",\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%D8%BA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:192\", \"status\": \"contradicts\", \"note\": \"HRN.txt leaf 213 (p. 192), no. 862: 'keläγ, kulāγ Rabe … aw. vārəγna- (?); phlv. varāγ, varāk. Das np. k könnte dann eben so wenig ursprünglich sein … Nöldeke will daher gr. κόραξ etc. vergleichen und auch phlv. varāγ ganz aus dem Spiele lassen … Diese Erklärung ist gewiss vorzuziehen, zumal die Bedeutung Rabe für das Avestawort gar nicht passt'. For barreh see Horn no. 211 (p. 49): 'berre, bere Lamm … ai. urana- Widder, Lamm; phlv. varak, arm. garn', which supports.\"},\n            {\"ref\": \"POK:1170\", \"status\": \"partial\", \"note\": \"Pokorny supports 'npers. barra (*varnak) lamb' but says nothing of kalâğ or varğeneh.\"},\n            {\"ref\": \"SOD:398\", \"status\": \"partial\", \"note\": \"Entry 9855 (p. 399) supports the falcon word only, through the Sogdian cognate.\"},\n            {\"ref\": \"BQT\", \"status\": \"not_found\", \"note\": \"No page given. Grepping BQT_v3_pages.txt for 'کلاغ' found only gloss uses (l.12691 'از جنس کلاغ', l.13845 'زاغ، کلاغ'). 'ورغنه' was not found in BQT_v4_pages.txt or BQT_v5_pages.txt.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.9287\", \"stance\": \"supports\", \"note\": \"'barra, bara Lamm aus *varnak, idg. vr̥ren-, skr. urana-, arm. garn' (barreh only)\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt l.607\", \"stance\": \"partial\", \"note\": \"'warrag … N barra' supports barreh. 'warāɣ [wl'g | J bry] crow' gives no NP kalāγ, only a Judeo-Persian cognate.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt [pdf page 125-126] s.v. بره\", \"stance\": \"supports\", \"note\": \"Cognates 'URANA (SANSKRIT)', 'ARĒN (GREEK)', 'GARN (ARMENIAN)', 'VARAK, WARRAG (PAHLAVI)'; refs 'POKORNY', 'MACKENZIE (LAMB) 121', 'BUCK 156-160' (barreh only).\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt leaf 488\", \"stance\": \"silent\", \"note\": \"The بره headwords are present, but the OCR is too poor to read Mo'in's footnote.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-17T00:04:53.863Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-548.json (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:04:58.172Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -m json.tool data/verification/page-548.json >/dev/null && echo ok; python3 tools/verify_check.py 548"
}
```


### [2026-10-17T00:04:58.971Z] TOOL RESULT

```
ok
nodes verified: 4/4
node verdicts: {'plausible': 2, 'confirmed': 1, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 3, 'not_found': 2, 'contradicts': 1, 'partial': 2}
books consulted: {'supports': 5, 'silent': 2, 'partial': 5} | by book: {'BRT': 3, 'HUB': 2, 'ARY': 2, 'PHD': 2, 'NYB': 1, 'POK': 1, 'BQT': 1}
```


## [2026-10-17T00:05:07.665Z] TOOL CALL #42: SubagentHandback

```json
{
 "message": "I verified PDF page 548 (book page 518) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-548.json. It passes json.tool, and verify_check.py 548 reports 4/4 nodes and no PROBLEM lines.\n\nThe page has one real chart, Weren. I skipped the other entry because it is only a redirect (Weredh → Ered).\n\n**Verdicts:**\n- Root: 1 confirmed. Pokorny p. 1170 has this root (u̯eren- \"ram, sheep, lamb\", today written *wr̥h₁ḗn) and supports Nourai's chart directly.\n- Nodes: 1 confirmed, 2 plausible, 1 disputed.\n  - Node 1, plausible: the Avestan/Old Persian \"varnak\" is a reconstructed form that appears in no text, so it should carry an asterisk.\n  - Node 2, plausible: Pahlavi warrag \"lamb\" is correct. But vāraγna / vārənjan are Avestan bird names, not Pahlavi. Reading them as \"lamb killer\" is Humbach's idea; Pokorny accepts it, but Bartholomae leaves the meaning open.\n  - Node 3, confirmed: Sogdian w'rγn'k \"falcon\" is in Gharib, entry 9855.\n\n**Disputed:**\n- Weren, node 4, kalâğ \"crow\": Horn (p. 192, no. 862) rejects the link to Avestan vāraγna / Pahlavi warāγ, because Persian k- cannot come from Iranian v-. Wiktionary calls kalāγ onomatopoeic. In the same node, barreh is confirmed, and varğeneh \"falcon\" is only a bookish borrowing from Avestan.\n\n**Transcription suspects:** none.\n\n**Extraction errors for you to fix:** none; I found no case where the JSON differs from the book. One citation in the book is off: SOD:398 is the Sogdian dictionary's p. 399 (the entry crosses the page break).\n\n**References I could not check:** BQT:268 (Borhan-e Qate' vol. 1). There is no scan for that volume and the OCR is unreadable, so it is marked not_found."
}
```


### [2026-10-17T00:05:07.994Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
