# Verification process log — verify-page-555


## [2026-10-17T00:00:15.818Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 555 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-555.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-555.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-555.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 555` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.893Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:24.252Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:24.279Z] TOOL RESULT

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


## [2026-10-17T00:00:24.749Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-555.txt"
}
```


### [2026-10-17T00:00:24.785Z] TOOL RESULT

```
1	=== PDF page 555 (book page 525) ===
2	--- entry 0 ---
3	ROOT Woid -> redirect to Weid
4	--- entry 1 ---
5	ROOT [Indo-European] Woin, Win : wine  (refs AHD:1547; ROE:265)
6	#1 (parent #0) [Persian] refs=FVF:695; AFM:159; BQT:2302; FSF:341 | vîn «وین» : black grape, color, vineyard (world ?)
7	#2 (parent #0) [Latin] refs=AHD:1547 | vînum : wine ; vînum-acer : sharp (sour) wine, vinegar ☞Ak ; vinea : vine
8	  #3 (parent #2) [English] refs=AHD | wine, vinegar, vine
9	--- entry 2 ---
10	ROOT Wokso -> redirect to Weg 1
11	--- entry 3 ---
12	ROOT Wolko -> redirect to Wel 2
13	--- entry 4 ---
14	ROOT Wopsâ -> redirect to Webh
15	--- entry 5 ---
16	ROOT Worda -> redirect to Wer 6
17	--- entry 6 ---
18	ROOT Wordia -> redirect to Wer 6
19	--- entry 7 ---
20	ROOT Wordos -> redirect to Wer 6
21	--- entry 8 ---
22	ROOT Wôs -> redirect to Wes 1
23	--- entry 9 ---
24	ROOT Wôsos -> redirect to Wes 1
25	
```


## [2026-10-17T00:00:25.378Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-555.json"
}
```


### [2026-10-17T00:00:25.420Z] TOOL RESULT

```
1	{
2	  "pdf_page": 555,
3	  "book_page": 525,
4	  "entries": [
5	    {"root": {"name": "Woid", "redirect": "Weid"}, "nodes": []},
6	    {
7	      "root": {
8	        "name": "Woin, Win",
9	        "lang": "Indo-European",
10	        "refs": "AHD:1547; ROE:265",
11	        "gloss": "wine"
12	      },
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Persian",
18	          "refs": "FVF:695; AFM:159; BQT:2302; FSF:341",
19	          "words": [
20	            {"translit": "vîn", "gloss": "black grape, color, vineyard (world ?)", "script": "وین"}
21	          ],
22	          "note": null,
23	          "quote": {"text": "اگر زندگانی بود دیریاز - براین وین خرّم بمانم دراز", "poet": "Ferdowsî"}
24	        },
25	        {
26	          "id": 2,
27	          "parent": 0,
28	          "lang": "Latin",
29	          "refs": "AHD:1547",
30	          "words": [
31	            {"translit": "vînum", "gloss": "wine", "script": null},
32	            {"translit": "vînum-acer", "gloss": "sharp (sour) wine, vinegar", "script": null, "see": ["Ak"]},
33	            {"translit": "vinea", "gloss": "vine", "script": null}
34	          ],
35	          "note": null,
36	          "quote": null
37	        },
38	        {
39	          "id": 3,
40	          "parent": 2,
41	          "lang": "English",
42	          "refs": "AHD",
43	          "words": [
44	            {"translit": "wine, vinegar, vine", "gloss": null, "script": null}
45	          ],
46	          "note": null,
47	          "quote": null
48	        }
49	      ],
50	      "note": "This is probably a Mediterranean word."
51	    },
52	    {"root": {"name": "Wokso", "redirect": "Weg 1"}, "nodes": []},
53	    {"root": {"name": "Wolko", "redirect": "Wel 2"}, "nodes": []},
54	    {"root": {"name": "Wopsâ", "redirect": "Webh"}, "nodes": []},
55	    {"root": {"name": "Worda", "redirect": "Wer 6"}, "nodes": []},
56	    {"root": {"name": "Wordia", "redirect": "Wer 6"}, "nodes": []},
57	    {"root": {"name": "Wordos", "redirect": "Wer 6"}, "nodes": []},
58	    {"root": {"name": "Wôs", "redirect": "Wes 1"}, "nodes": []},
59	    {"root": {"name": "Wôsos", "redirect": "Wes 1"}, "nodes": []}
60	  ]
61	}
62	
```


## [2026-10-17T00:00:29.716Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['AHD','ROE','FVF','AFM','BQT','FSF','POK','WLD','IEC','SYN','KLN','SKT','FSD','WEB','HRN','HUB','MON','ARY','PHD','NYB','LKT','PLA','FVQ']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; command ls sources/refs | head -100; cat sources/SOURCE_MATRIX.md | head -80"
}
```


### [2026-10-17T00:00:30.220Z] TOOL RESULT

```
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
ROE {"title": "R. Claiborne, The Roots of English: A Reader's Handbook of Word Origins, New York 1989", "edition_found": "1989 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/rootsofenglish00clai ; rootsofenglishre0000robe (lending)", "identifier": "rootsofenglish00clai (also rootsofenglishre0000robe)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow 
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
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
SIN.txt
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
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
```


## [2026-10-17T00:00:42.096Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:2302 --image 2>&1 | head -80"
}
```


### [2026-10-17T00:00:47.447Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 385; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2302.png
REF: BQT:2302  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 385  OCR-lang: fas

وبلااج ۳۰۲۳
کار را بکنند ومیانر بگذارند ؛ وان معنی راور | باشد عموماً ۴ - وانگور سیاه را کوبند خسوصا.
عرمی‌طفره وبپندی ناغه میگوبند ۰ و بند ۰ « بکر اول » بر وزن ومعنی

وپلانج - بالام الف ودون وجیم | بیند باشد که از دیدن است.
و حر کت غیر معلوم . مطلق حلوا راکونند. و بنداناگ - یکر اول و ثانیمجهول
ویله * بروزن حیله , بمعنی‌سدا وآواز | وفتح دون و دال ابجد بالف کشیده بروزن بی
باغد ۱ - و فریاد عظیم وشور و واوبلاکردن را | زبانك, نافهٌ مشغك راکوبند ‎٩‏ - وبفتح‌اول‌ونانی»
نز کونند؟ . در موبدالفتلاء ناغه ۷ دوشته‌اند که بعریی طفره
وم - بروزن جیم » سیم کل راکوبند | کوبند. اسّاعلم.
وآن کلابه‌ایست که بردیرارمالند و بربالای آن ویو ۸ * بفتح اول و ضم ثانی وسکون
کاهگل کنند ۳ . واو مجپهول » بمعنی عروی است که زن داماد
وان « بروزن سین » بمعنی رنکه ولون | باشد ؛ و بکسراول هم‌آمده است .4
‎٩‏ - باز دانی بطم منطق طیر لحن موسیچه را ز وبلةٌ زاغ .
مجدهمگر « فرهنگه نظام >.
درین بیم بودلد و غم یکره که کرشاسپ زد ویله‌ای از دره .»
« لغت فری می 9۶۳ ؟.
چو رعد خروشان یکی وبله کرد تر کفتی بدرید دشت نبرد .
فردوسی‌طوسی . « فرهنگه نظام ».
۴ - سرای خود راکرده ستانهٌ زرین بقف خانه پدر برندیده کهگل و ویم.
سوزبی سمرقندی « جهالگیری » .
۴ - رك : جهانگیری. * . لهجه‌ایست در ۶ بیند ». رك : دیدن .
۹« نافة مشك باشد » «سروری». ۷ -ظ. ممحف « ناقه ». (ناغه را درمعنی

وبلان[ «.م.] دوشته‌اند). ‏ ۸ ۳ بیو(ه.م.) ۳ بیوکه («.م ) ۳ وبوك (ه.م.) و رك : بیوگاای .

2 وبوفبی - بفتح اول ۳ بی و که (<.م.) ( رك : بیوگانی ) ۳ بو (.م.)؛ عروی :

که جاوید این سرا آراسته باد پر از شادی و ناز و خواسته باد

درو خرم وبوکان و خوران عروسان دختران داماد پوران .
ویی‌ورامین مصحح میئوی ص ۵۱ ۰
```


## [2026-10-17T00:00:51.076Z] TOOL CALL #6: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2302.png"
}
```


### [2026-10-17T00:00:51.512Z] TOOL RESULT

```

```


## [2026-10-17T00:00:51.508Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:00:55.906Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; cat > ocr/BQT/2302.vision.txt <<'EOF'\n[BQT p. 2302, read from image; entry وین]\nوین - بروزن سین، بمعنی رنگ و لون باشد عموماً ۴ - و انگور سیاه را گویند خصوصاً.\n[footnote] ۴ - رک: جهانگیری.\n(Mo'in gives no etymological note for وین on this page.)\nEOF\ngrep -n 'pdf page' AFM_pages.txt | head -3; grep -n -i 'page_offset' ../refs_online.json | head -0; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['AFM','FSF','FVF']: print(k, json.dumps(d[k],ensure_ascii=False))\""
}
```


### [2026-10-17T00:00:56.465Z] TOOL RESULT

```
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"}
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."}
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."}
```


## [2026-10-17T00:00:58.065Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'الوين\\|( وين\\|(الوين' AFM_pages.txt AFM.txt | head; echo ---; grep -n 'وین' FSF_pages.txt | head -20"
}
```


### [2026-10-17T00:00:58.404Z] TOOL RESULT

```
AFM_pages.txt:1678:( !)ܕ ) تعر يب 4 دهي و للف السترويشار هلالوين 0 ܟ مئه 4 فراء وشال
AFM.txt:2704:( !)ܕ ) تعر يب 4 دهي و للف السترويشار هلالوين 0 ܟ مئه 4 فراء وشال 
---
203:‫مورد است و گوینده کیست و گفتارش درباره کدام کس است تامقصود شاعر و‬
343:              ‫ذیل واژه «با‬     ‫چ‪.‬نوین‬
373:‫‪ ۱‬این واژه نامک برپاية پنج نسحه معتبر شاهنامه تدوین شده است‪ .‬بدین قرار‪:‬‬
532: ‫قبای نبردی برون آختند‬                                        ‫نپیوندند باهم مهر کوینه‬
663:‫«آذوینک» پسهلوی است به معنی رسوم و‬                   ‫همی روزگارم زند‪ .‬نیست ننگ‬
669:   ‫«آذوین» بهمهنیآیینو شعایر ملیباشد»‪.‬‬                          ‫تاکیّماز چرخ رسد آذرنگ‬
957:‫(‪)۶-۳۶۳-۲۶۱‬‬                                         ‫بگویند کاین شهریار رمه‬
1042:   ‫‪:)۰۴۳-۵‬‬     ‫اموین‬
1061: ‫اموین ‪:)۸۶۱-۶۰۱‬‬
1132:‫به روشن گلاب اندر آشامشان‬                           ‫اموین ‪:)۱۶۱-۴‬‬
1244:‫اگزرفخگرانی (رویاسموین ‪ ۴۴۱-۵۷۱‬و‬                                       ‫(لغت فرس)‬
1290:                        ‫گویند‪ .‬فرالاوی گفت‪:‬‬                    ‫فرهنگ رشیدی رویداده است‪.‬‬
1367: ‫(دقیقی ‪-‬نقل از صحاح‌الفرس)‬                      ‫هم «آغشته» گویند» (صحاح _بی‌شاهد)‪:‬‬
1393:               ‫آفریند ‪+‬الف آرزومندی د‬           ‫از گفخررگانی (رویاسموین ‪:)۲۴۴-۳۰۵‬‬
1578:                                                       ‫اشارات نزدیک (اینک) و دور (آنک) گویند‪.‬‬
1841:   ‫از گفرخرگانی (رویاسموین ‪:)۶۶-۱۲‬‬               ‫زگیتی بی آه و نیابی کسی‬
1842:           ‫مخوینخت‬
1863:                                ‫کیش‪:‬‬       ‫[هوشنگ از پویندگان هرچ مویش نکوست‬
1866: ‫کهکیرهکنیونره وین ی‬                       ‫بسسرینگونه از جرم پسویندگان‬
1867: ‫(‪)۵-۸۰۲-۲۱۱۲‬‬                              ‫بپوشید ببللای گویندگان‬
```


## [2026-10-17T00:01:00.656Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'بمانم\\|زندگانی بود\\|دیریاز' FSF_pages.txt | head; grep -c 'pdf page' FSF_pages.txt; grep -n '^\\[pdf page\\|pdf page' FSF_pages.txt | tail -3"
}
```


### [2026-10-17T00:01:01.177Z] TOOL RESULT

```
3609:                            ‫بمانم ت‬                  ‫نماز‬          ‫برآمد‪ .‬پری روی [رو‬
8061:                         ‫(ویس ‪:)۶۳۱-۷۴‬‬     ‫که چندان بمانم به گیتی به پای‬
9203: ‫که چندان بمانم گبیهتی به جای‬                     ‫ناصر خسرو آنها را در این بیت آورده‬
12606: ‫دیریاز‬
12670:                                       ‫دیریاز‬         ‫بر‬            ‫ر و داد یر م‬
12686:                                   ‫(بهار عجم)‬         ‫این دولت دیریاز‬        ‫بترسم که‬
14996:                                                    ‫گبیهتی بمانم یکی داستان‬
20251: ‫بمانم به گیتی یکی داستان‬                                    ‫زریر سپهبد سپه را بماند‬
21243:        ‫از پند حق و خوب سخن سیری‬                ‫بگهیتی بمانم یکی یادگار‬
22538:           ‫اگر زندگانی بود دیسریاز‬                  ‫(‪)۲-۴۲۱۰-۱۷۸‬‬
0
```


## [2026-10-17T00:01:03.057Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22500,22580p FSF_pages.txt; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); c+=n-1; if(c>=22538){print \"page\",NR; exit}}' FSF_pages.txt"
}
```


### [2026-10-17T00:01:03.540Z] TOOL RESULT

```
                                                                              ‫کار بردن‪:‬‬   ‫‪۳‬به‬
‫سخنگوی و بینا دل و یادگیر‬
 ‫(‪)۱-۲۹-۲۲۲‬‬                                                ‫سخن‌های من چون شنیدی بورز‬
                        ‫(ناصر ‪:)۱-۸۱‬‬              ‫مگر باز دانی ز ناارز ارز‬

         ‫این جهان را فریب بسیارست‬                  ‫(‪)۷۰-۶۸۱۰-۸۴۵‬‬
                                                                              ‫(ویس ‪:)۷۴-۳۴‬‬
 ‫بفروشد به نرخ سوسن سیر‬
        ‫نتواند‬      ‫راثشاخت‬    ‫حسیلشر‬                   ‫من از تو راستی خواهم کهجویی‬
 ‫جکزسی تیزهوش و روشن‌ویر‬                           ‫وویی‬
                                                      ‫همیشه راستی ورزی گ‬
                                     ‫ویژه‬                                       ‫ورزیده‬
                                ‫‪-۱‬پاک‪:‬‬              ‫(اسم مفعول از ورزیدن)‪ :‬به‌دست آمده‪:‬‬

             ‫جهان ویژه کردم ز پتیارها‬
‫بسی شهر کردم بسی بارها‬                            ‫همان باره و تاج گوهر نگار‬
‫(‪)۱-۷۳۴۲-۰۳۶۱‬‬                                                  ‫فرستم به گنج تو ازگنج خویش‬
                ‫‪-۲‬ویژه بویژه» بخحصوص‪:‬‬              ‫همان نیز ورزیده رنج خويش‬
        ‫مرا زین سخن ویژه اندوه تست‬
                                                   ‫(‪)۶-۷۹۳-۰۷۲‬‬

 ‫که بیدار دل بادی و تندرست‬
‫(‪)۲۰۴۴-۱۳۲-۳۲‬‬
 ‫وین‬                                          ‫‪۹۵۴‬‬


           ‫فرود آمد از تخت ويله کنان‬                        ‫سزاوار هر کس ببخشید گنج‬
 ‫زنان بر سروموی و رخ راکنان‬                         ‫بویژه کسی کش فزون بود رنج‬
 ‫)‪(1-۳-4۳‬‬                                           ‫(‪)۲-۲۲۱-۲۶۸‬‬


                                        ‫وین‬         ‫‪-۳‬ویژه‪.‬ویذگان‪:‬حاصءخاصان‪,‬آشنایان نزدیک‪:‬‬
             ‫‪-۱‬از دیباچۀ داستان سیاوش‪:‬‬                       ‫برون رفت با ویژه گردان خویش‬
           ‫گزفتار دهقان کنون داستان‬                 ‫کهبااویکی بودشان رای و کیش‬
 ‫تو برخوان و برگوی با راستان‬                         ‫(‪)۱-۵۵۱-۰۹۲‬‬
           ‫کهن گشته این داستان‌هاء زمن‬                     ‫به یک هفته با ویژگان می به‌چنگ‬
 ‫همی نو شود بر سر انجمن‬                             ‫به مازندران کرد زآن پس درنگ‬

           ‫اگر زندگانی بود دیسریاز‬                  ‫(‪)۲-۴۲۱۰-۱۷۸‬‬
                                                                                            ‫ویک‬
 ‫بسرین وین خرم بمانم دراز‬
                                                    ‫«بجای ویحک باشد» (لغت فرس؛ صحاح؛‬
 ‫(‪۳‬سو‪)۱.‬‬
                                                    ‫جهانگیری رشیدی)؛ «کلمۀ حطاب به‌معنی‬
               ‫یکی میوه داری بماند زمن‬
                                                               ‫ای نیکبخت‪ .‬ای نیک» (برهان)‪:‬‬
 ‫که نازد همی بار او بر چمن‬
       ‫نرسخه لندن آمده است‪.‬‬
                          ‫واه «وین» د‬
                                                                   ‫اگر شاخ بد خیزد از بیخ نیک‬
 ‫نسخة قاهره نیزآن را تأييدمی‌کند‪ .‬ولی در‬
                                                    ‫تو باشاخ تندی میاغاز ویک‬
                                                    ‫(‪)۲-۶۷-۵‬‬
‫نسخه قاهره «دین» [با دال] نوشته شده که‬
                                                    ‫(در شاهنامة چاپ مسکو با آنکه در‬
             ‫«وین» است‪.‬‬   ‫بی‌گمان مصحف‬
                                                    ‫نسخه‌ها «ویک» ضبط است‪« .‬ریک» جاپ‬
 ‫در سه نسخه لنینگراد مصراع دوم بیت‬
                                                                         ‫وادرست است)‪.‬‬
                                                                                    ‫شده ن‬
 ‫شاهد چنین است‪« :‬بدین دير خرم بماند‬
                                   ‫دراز)‪.‬‬
                                                                     ‫از رودکی (لفت فرس‪ :‬صحاح)‪:‬‬
                                                     ‫ماده گفتا هیچ شرمت نیست ویک‬
 ‫از آنجاکهدیربهمعنی جهان‪ ,‬گیتی در‬
                                                    ‫چون [صحا‌بس] سبکساری نه بد دانی نه نیک‬
 ‫شاهنامه به کارنرفته است من در شاهنامه‬
                                                                            ‫(اسدی ‪:)۶۳۲-۵4‬‬
 ‫چاپ مسکو «وین» را در متن قرار دادم‪.‬‬
  ‫فردوسی این واژه‌ها و ترکیب‌ها را بکهار‬
                                                            ‫پشیمان نگردد کس از کار نیک‬
  ‫برده است‪ :‬روزگار‪ .‬جهان‪ .‬گیتی‪ .‬خاک‬             ‫نکوتر ز نیکی چه چیزست‪ .‬ویک‬
                                                                                            ‫ويله‬
 ‫خونخوار مرکز ماه و پرگار تنگ [همی‬
‫نامکوشم کهماندنهننگ ×بدین مرکز ماه‬                                    ‫بانگ» فریاد‪ .‬زاری» شیون‪:‬‬
                                                           ‫بهپیش سپاه اندر آمد چو گرد‬
 ‫پورگار تنگ‪ .‬مقدمۂ پادشاهی اسکندر ]؛‬
                                                    ‫چو رعد خروشان یکی ویله کرد‬
                                                    ‫(‪)۲-۵۸۱-۴۰۲‬‬
                                                ‫‪۳۹۰‬‬                                            ‫وین‬

page 463
```


## [2026-10-17T00:01:14.687Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad\nfor u in 'Reconstruction:Proto-Indo-European/wóyh₁nom' 'وین' 'vinum' 'wine' 'vinegar' 'vinea'; do e=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$u\"); curl -s \"https://en.wiktionary.org/w/api.php?action=parse&page=$e&prop=wikitext&format=json&formatversion=2\" | python3 -c \"import json,sys;d=json.load(sys.stdin);print(d.get('parse',{}).get('wikitext','NONE'))\" > wk555-$(echo $u|md5sum|cut -c1-6).txt; echo \"$u $(wc -c < wk555-$(echo $u|md5sum|cut -c1-6).txt)\"; done"
}
```


### [2026-10-17T00:01:16.725Z] TOOL RESULT

```
Reconstruction:Proto-Indo-European/wóyh₁nom 60
وین 378
vinum 3382
wine 31736
vinegar 13396
vinea 1484
```


## [2026-10-17T00:01:19.508Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for f in wk555-*; do echo \"== $f\"; head -c 300 $f; echo; done; curl -s \"https://en.wiktionary.org/w/api.php?action=query&list=search&srsearch=intitle:w%C3%B3yh%E2%82%81nom&srnamespace=118&format=json\" | head -c 800"
}
```


### [2026-10-17T00:01:20.127Z] TOOL RESULT

```
== wk555-1a0494.txt
{{also|وين}}
==Persian==
{{wp|fa:}}

===Etymology 1===
{{ety|fa|:bor|ar:وَيْن|text=+|tree=1}}

====Noun====
{{fa-noun|tr=vin}}

# black [[grape]]

===Etymology 2===
{{ety|fa|:bor|fr:Vienne|text=+|tree=1}}

====Pronunciation====
* {{IPA|fa|[viˈjæn]|a=IR}}

====Proper noun====
{{fa-proper no
== wk555-451ffd.txt
==Latin==

===Etymology===
{{ety|la|:nom|vīneus<t:of or relating to wine>|text=2}}

===Pronunciation===
* {{la-IPA|vīnea}}

===Noun===
{{la-noun|vīnea<1>}}

# [[vineyard]]
# A [[vine]], especially a [[grapevine]]
# {{lb|la|military}} a moveable [[bower]] used as a shelter, see [[testudo]]

====De
== wk555-7ef15c.txt
==English==
{{wp}}

===Etymology===
{{etymon|en|:inh|enm:vynegre|tree=1}}
{{root|en|ine-pro|*h₂eḱ-}}
From {{inh|en|enm|vynegre}}, from {{der|en|fro|vinaigre}} from {{der|en|fro|vyn egre}}, based on {{der|en|la|vīnum||wine}} + {{der|en|la|ācer||sour}}. Displaced {{cog|ang|æċed}} (survived in 
== wk555-c5ce55.txt
{{also|Wine|WINE|winę|Wîne}}
==English==
{{wp}}
[[Image:Red Wine Glas.jpg|thumb|A glass of red wine]]

===Pronunciation===
* {{IPA|en|/ˈwaɪ̯n/|[ˈwaɪ̯n]}}
** {{audio|en|en-uk-wine.ogg|a=UK}}
** {{audio|en|en-us-wine.ogg|a=US}}
* {{rhymes|en|aɪn|s=1}}
* {{hyph|en|wine}}
* {{hmp|en|whine<aa:wi
== wk555-c87e1d.txt
{{also|vínům}}
==Icelandic==

===Noun===
{{head|is|noun form}}

# {{inflection of|is|vinur||indef|dat|p}}

==Latin==
[[File:Red and white wine 12-2015.jpg|thumb]]

===Alternative forms===
* {{alt|la|vīnus||nonstandard}}

===Etymology===
{{etymon|la|id=wine|:inh|itc-pro:*wīnom}}
From {{inh|la|itc
== wk555-d44ff3.txt
#REDIRECT [[Reconstruction:Proto-Indo-European/wéyh₁ō]]

{"batchcomplete":"","query":{"searchinfo":{"totalhits":1},"search":[{"ns":118,"title":"Reconstruction:Proto-Indo-European/w\u00e9yh\u2081\u014d","pageid":5235071,"size":4690,"wordcount":882,"snippet":"(see there for further descendants) *<span class=\"searchmatch\">w\u00f3yh</span>\u2081n-eh\u2082 Proto-Hellenic: *w\u00f3in\u0101 Ancient Greek: \u03bf\u1f34\u03bd\u03b7 (o\u00edn\u0113, \u201cvine\u201d) *<span class=\"searchmatch\">w\u00f3yh</span>\u2081n-o-s Proto-Albanian: *wain\u0101 or *woin\u0101","timestamp":"2026-08-23T21:58:43Z"}]}}
```


## [2026-10-17T00:01:24.099Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for u in 'Reconstruction:Proto-Indo-European/wéyh₁ō' 'وين'; do e=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$u\"); curl -s \"https://en.wiktionary.org/w/api.php?action=parse&page=$e&prop=wikitext&format=json&formatversion=2\" | python3 -c \"import json,sys;d=json.load(sys.stdin);print(d.get('parse',{}).get('wikitext','NONE'))\" ; echo =======; done | head -150; sed -n 1,40p wk555-c87e1d.txt | tail -28"
}
```


### [2026-10-17T00:01:24.621Z] TOOL RESULT

```
{{reconstructed}}
==Proto-Indo-European==

===Etymology===
{{etymon|ine-pro|id=wine|pos=word|:af|*weh₁y-<unc:1>|*-ō}}
{{unk|ine-pro|Disputed}};<ref>{{R:ine:Beekes 2011|36}}</ref><ref name="Fortson">{{R:ine:IELC|II|38}}</ref> possibly from {{suf|ine-pro|*weh₁y-|t1=to twist; to wrap|*ō}},<ref name="Beekes" /><ref name="EDL">{{R:itc:EDL|head=vīnum|page=680}}</ref><ref name="Mallory" /><ref name="Schrader">{{R:Schrader:1912|page=29}}</ref> compare {{cog|grc|ὑιήν|t=grapevine}}, from {{m|ine-pro||*wih₁-ḗn}},<ref name="Mallory" /> and {{cog|la|vītis|t=vine}}, from {{m|ine-pro|*wéh₁itis}}, or perhaps borrowed from either {{cog|sem-wes-pro|*wayn-}} or {{cog|ccs-pro|*ɣwino-}}, if those terms are not instead borrowings of the Proto-Indo-European.<ref name="Fortson" /><ref name="Nichols">{{cite-journal|year=1997|author=Nichols, J.|editor=Blench, R.; M. Spriggs|chapter=The epicentre of the Indo-European linguistic spread|journal=Archaeology and Language I: Theoretical and Methodological Orientations|location=London|publisher=Routledge|page=126|url=https://www.academia.edu/28869625/The_epicenter_of_the_Indo-European_linguistic_spread}}</ref><ref name="Fenwick">{{R:ccs:Fenwick:2017|2}}</ref><ref name="Klimov">{{R:ccs:Klimov:1994|pages=79-82}}</ref> Possibly all ultimately borrowed from an unattested Mediterranean {{der|ine-pro|qfa-sub|-}} language.<ref>{{R:Sihler 1995|53}}</ref><ref>{{R:ine:HCHIEL|832}}</ref>

===Noun===
{{ine-noun|m}}<ref>{{cite-journal|year=1987|author={{w|Robert S. P. Beekes|Beekes, Robert S. P.}}|chapter=On Indo-European ‘wine’|journal=Münchener Studien zur Sprachwissenschaft|pages=21-26}}</ref><ref name="Kloekhorst" /><ref name="Klimov" />

# {{topics|ine-pro|Wine|Zymurgy}} [[wine]]
# {{topics|ine-pro|Grapevines}} [[vine]]

====Reconstruction notes====
The source of the [[o-grade|''o''-grade]] in some descendants is not well explained by the paradigm given above. It is probably of innovative origin post-PIE and analogical with thematic paradigms, namely those in {{m|ine-pro|*-os|id=thematic|*(ó)-o-s}} and {{m|ine-pro|*-éh₂|id=o-grade|*(o)-éh₂}}, though explanations in terms of an original ''o''-ablaut are also possible, such as a separate, neuter form of the word with an acrostatic paradigm {{m|ine-pro||*wóyh₁-n̥ ~ *wéyh₁-n̥-s}} (compare {{m|ine-pro|[[*wósn̥|*wós-n̥]] ~ *wés-n̥-s|t=price}}), or even (more controversially) a three-way ''e ~ o ~ ∅'' ablaut such as {{m|ine-pro||*wéyh₁-ō}} with the addition of accusative {{m|ine-pro||*woyh₁-nó-m}}.<!--similar situation to {{m|ine-pro|*kres-|*kr(e/o)s-n-|gush of water}}?--> This may all be misguided if it is a non-Indo-European loanword, however.

====Inflection====
{{ine-decl-noun-mf|ac=amphikinetic|wéyh₁on|wih₁n̥|loc_sg=wih₁én}}

====Derived terms====
* {{l|ine-pro||*wéyh₁n-o-m}}<ref name="Fenwick" />
** {{desc|hyx-pro|alt=*ɣʷeinyo-}} {{q|or from *wóyh₁n-o-s<ref>{{R:ine:IEL|429}}</ref>}}<ref>{{R:xcl:Martirosyan|head=gini|page=214–215}}</ref>
*** {{desc|xcl|գինի}} {{see desc}}
** {{desc|itc-pro|*wīnom}} {{see desc}}
*** {{desc|la|vīnum}} {{see desc}}
**** {{desc|cel-pro|*wīnom|bor=1}} {{see desc}}
**** {{desc|gem-pro|*wīną|bor=1}} {{see desc}}
**** {{desc|sla-pro|*vīnò|bor=1}} {{see desc}}
* {{l|ine-pro||*wóyh₁n-eh₂}}
** {{desc|grk-pro|alt=*wóinā}}
*** {{desc|grc|οἴνη|t=vine}}
* {{l|ine-pro||*wóyh₁n-o-s}}<ref name="Mallory">{{R:ine:Mallory:2006|pages=166-167}}</ref><ref name="Fenwick" /><ref name="Beekes">{{R:grc:Beekes|head=οἶνος|pages=1058-1059}}</ref>
** {{desc|sqj-pro||alt=*wainā}}<ref>{{R:sq:Orel:2000|page=50}}</ref> or {{l|sqj-pro||*woinā}}<ref name="Demiraj">{{R:sq:Demiraj|head=vër/ë,-a|page=414}}</ref>
*** {{desc|sq|verë|venë}}
** {{desc|grk-pro|*wóinos}} {{see desc}}
* {{l|ine-pro||*wih₁-on-}}<ref name="Kloekhorst">{{R:hit:Kloekhorst:2008|head=u̯ii̯an-|page=1012}}</ref><ref name="EDL" /><ref name="Fenwick" />
** {{desc|ine-ana-pro}}
*** {{desc|hit|𒃾𒅖|tr=GEŠTIN-iš|ts=wiyanis|t=wine}}
*** {{desc|xlu|-}}
***: {{desc|xlu|tr=winiya-|sc=Xsu(eval):1: ====== not found
x|sclang=1}}
* {{l|ine-pro||*wih₁n-yó-s}}<ref name="Fenwick" />
** {{desc|ine-ana-pro}}
*** {{desc|hit|𒌑𒄿𒉌𒅀𒀭𒋫𒀭|ts=*winiyantan|tr=ú-i-ni-ya-an-ta-an|t=wine (deified)|pos=accusative}}
*** {{desc|xlu|-}}
***: {{desc|xlu|ts=wiyan(i)-|sc=Hluw|sclang=1}}, {{l|xlu|ts=win(i)-|sc=Hluw|t=of wine}}
* {{desc|ccs-pro|*ɣwino-|bor=1|unc=1|qq=possibly via Armenian}} {{see desc}}
* {{desc|sem-wes-pro|*wayn-|bor=1|unc=1}} {{see desc}}
* {{desc|xag|𐕔𐔼|bor=1|unc=1}} {{see desc}}

===References===
{{reflist}}

===Further reading===
* {{R:ine:Gorton:2017}}
* {{R:ine:Lipp:2019}}
* {{alt|la|vīnus||nonstandard}}

===Etymology===
{{etymon|la|id=wine|:inh|itc-pro:*wīnom}}
From {{inh|la|itc-pro|*wīnom}}, from a [[thematicized]] form of {{inh<!--arguably der-->|la|ine-pro|*wéyh₁ō}}.

===Pronunciation===
* {{la-IPA|vīnum}}

===Noun===
{{la-noun|vīnum<2>}}

# [[wine]]
#: {{syn|la|merum|Bacchī hūmor|Bacchus}}
#: {{ux|la|[[in vīnō vēritās|In '''vīnō''' vēritās]].|[[in wine, there is truth|In '''wine''', there is truth]].}}
#* {{Q|la|Virgil|Aeneid|1|195|thru=197|quote='''Vīna''' bonus quae deinde cadīs onerārat Acestēs<br/>lītore Trīnacriō dederatque abeuntibus hērōs<br/>dīvidit [...].|trans=''Next, '''wine''' – which good Acestes had loaded in casks along the Sicilian shore, and [which that] hero had given upon our departures – [Aeneas] divided up.''<br/>(See: [[Acestes]]/{{w|Acestes}}; [[Aeneas]]/{{w|Aeneas}}; “[[Trinacria]]” was an ancient name for [[Sicily]]/{{w|Sicily}}.)}}
#* {{Q|la|Ovid|Fasti|3|305|quote='''vīna''' quiēs sequitur|trans=''Rest is following the '''wines.'''''<br/>Or, in more natural English, as implied by the plural ''vīna'':<br/>''[Drink] '''[enough] wine''', [and] rest follows.''}}
# {{lb|la|figuratively}} [[grape]]s
# {{lb|la|figuratively}} a [[grapevine]]

====Declension====
{{la-ndecl|vīnum<2>}}

====Hyponyms====
{{col|la|vappa|merum|vītis|uva}}

====Derived terms====
{{col6|la
```


## [2026-10-17T00:01:28.635Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for u in 'Reconstruction:Proto-West Semitic/wayn-' 'وين'; do e=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$u\"); curl -s \"https://en.wiktionary.org/w/api.php?action=parse&page=$e&prop=wikitext&format=json&formatversion=2\" | python3 -c \"import json,sys;d=json.load(sys.stdin);print(d.get('parse',{}).get('wikitext',str(d)[:300]))\" | head -60; echo =====; done"
}
```


### [2026-10-17T00:01:29.120Z] TOOL RESULT

```
Exit code 1
{{reconstructed}}
==Proto-West Semitic==

===Etymology===
{{etymon|sem-wes-pro|id=wine}}
Possibly borrowed from {{cog|ine-pro|*wéyh₁ō|t=wine, vine}},<ref>{{R:ine:Beekes 2011|36}}</ref><ref name="Fortson">{{R:ine:IELC|II|38}}</ref><ref name="Nichols">{{cite-journal|year=1997|author=Nichols, J.|editor=Blench, R.; M. Spriggs|title=The epicentre of the Indo-European linguistic spread|work=Archaeology and Language I: Theoretical and Methodological Orientations|location=London|publisher=Routledge|page=126|url=https://www.academia.edu/28869625/The_epicenter_of_the_Indo-European_linguistic_spread}}</ref><ref>{{R:ccs:Klimov:1994|pages=79-82}}</ref> if not [[vice versa]],<ref name="Fortson"/><ref name="Nichols"/><ref name="Fenwick">{{R:ccs:Fenwick:2017|2}}</ref><ref name="Klimov">{{R:ccs:Klimov:1994|pages=79-82}}</ref> or a common loanword from Asia Minor.<ref>{{R:he:Rabin-Hit.|pages=138–139}}</ref><ref>{{R:gez:Leslau-Comp.|page=623}}</ref>

===Noun===
{{head|sem-wes-pro|noun|g=m}}<ref>{{R:sem-pro:Weninger-Handbook|page=241}}</ref>

# [[wine]]

====Descendants====
* Central Semitic:
** {{desc|ar|وَيْن|t=black grape}} {{q|rare}}
*** {{desc|fa|وین|tr=vin|t=black grape|bor=1}}
** Northwest Semitic:
*** Canaanite:
**** {{desc|he|יַיִן|tr=yáyin|t=wine}}
**** {{desc|phn|𐤉𐤍}}
*****{{desc|xpu|𐤉𐤍}}
*** {{desc|uga|𐎊𐎐|ts=yênu}}
** {{desc|sem-srb|-}}
*** {{desc|xqt|𐩥𐩺𐩬|tr=wyn|t=vineyard}}
*** {{desc|xsa|𐩥𐩺𐩬|tr=wyn|t=vineyard}}
* Ethiopian Semitic:
** {{desc|am|ወይን}}
** {{desc|gez|ወይን|t=grapevine, wine}}
** {{desctree|ti|ወይኒ|t=wine, grape}}

===References===
{{reflist}}
(eval):1: ==== not found
```


## [2026-10-17T00:01:32.969Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '( *الو\\|( *و' AFM_pages.txt | sed -n 1,80p | cut -c1-120"
}
```


### [2026-10-17T00:01:33.406Z] TOOL RESULT

```
115:. , ܢܐܝ ܨܐܐ ܚܠ 03 ܐ 5 ܨ جار ܕܥ( وجعدر
150:( الوبريز والاإبريزي » من 4 الخمالص قال عنة فرتكل في كتابه في
205:تفع لاإننات ܚܟ .ܕܟܕ بالارامية ܐܪܥܘܝܐܝ ܙ( 5 6( و 6 1
401:الفارسي ومعناه الوعاء وشرنقة القز او 55( ومعناه القدح © ¢ كك .
496:ܐܝܐ ܨ نشت على اللفظة الفارسيّة فلم 0 سوى ܕ( وهو اصطفاف 1 والرجالة
709:. (البندّار) التاجر الذي يازم العادن ܘܰܐܚܠܳܐ ܠܙܐ( واصل معناه صاحب
806:(١3‏ الت كوج ܘ وهي ܒܝ الماء اليه ( اللسان ) تعريب ( ويطلق
898:يطلقون | سم ܠ على 5 3 2 :4 أبيض ولسمسه العرب ܟܚ( وهو معرب
912:ܝܫܐ( والطنجير) الا جانة تعيب تغار ومن التري تغار
931:( الثنبور) القصير القامة ٠و١‏ التذّل $ والتذالة 6( والتأتل < |
960:0 1 0 فارسلتة جو ܢ( وهو مركت من جوى
991:1 ܨ( الثيء الفليظ 85( واصل 5 الثقيل الردي .
1095:( 5 القطعة من الارض الغليظة 007 5 ܐܟܐ 8( وابللون)
1190:( الجهارة ) . حسن |( والن تعر يب جهره ومعئاه ما الانسان وطاعتة ووجهة
1262:( ܝܐ( وهر معروف ܨ 3 جام
1334:الثىء 6( والقماحة ومن بال اي القامة :
1417:( 15 ] ) طير من طبور الماء ( سَفاء الغليل ٠)‏ معرب عن ܐܚܐ( وهو طير
1487:( الور ;31( الدنيا تعريب خنور وهي كئابة عن جيع 53 1
1546:الظلمة ܀ ( والد > والد رجنّة والد ܨ والدجمّة والدكغى ) الظلمة ٠ ١‏ والد خناء )
1547:الذي <١‏ ودثيا م 0 أظلم . (وأدجى وتدجى وادجوجى ) :كل دف
1620:من دست أي يد ومن :15 اي ( ومئة الم 317 ܕܣܬܝܥܙ
1672:(والدقدّان) ما تميس :عله 1 نرد كك مخ د يلك ومن < أن وهي اداة تدل على
1836:(الرازق ) السب املاحي 390 6 ( والخمر:
1987:+ |( © ما اتحدر من السيول ١‏ التابج ) معرب 95( واصل '
2210:خورنه وهو ءارة بديعة من غرائب الدهر بناها النهان بن الللذر 0 ® ( وهو00
2398:(السَمَنْدَر ܕ( والسَمَنْدَل) دابة معروفة عند اهل الصين والهند ٠‏ وسماها
2451:#* ( 9 ¥ 05 والطويل والشديد والأسد. (وَالسَئْدَر) 5 <
2561:. (الكية) القوس لست مهدئدة ولا علق مرركة. مزق" ستايز( وظرات 1
2628:(الشنجار) 3 ܚܢܐ( وهو ܨ اراز 1050 له ܐܐܟ ܒ¿ الكحلاء
2744:* (الصرق) الرقيق من كل شيء ( والصريقة ) الرقاقة من اأبز معربان عن
2747:01 1 )4 ` 890( وهو (03±
2838:+ (الطنتدر) الشر تعرس ܢܐܦ( ومعناة ܐܢ الفساد
2864:ܸ ܐܨ الليل أظلم ( وطرمش ܕ)ܟܐܨ ܨ ) ܐܝܐܝ فيه ( ܕܐܨ .| َّ )
2989:اللغات 30 | فخ ܐܢܐ( وفق بالتركّة ܦܢܢܐ بالسمر يانية و52 بالعبرانية ܀ ¿!)&
3048:( ܐܝܟ( وهو معروف تعريب يسْنه وهو مركب من 9 اي السّويق ومن
3123:( الوم ) ععنى النطة والختص !ܡ وسائر المموب التي 9 فارستتها فوم
3188:”,݇ܐ .وام بالعبرائئّة التدعة فهو ده و ܪܟܡ ١؟‏ ايام: ¥ :3 :€( و1:5١).‏
3215:الرجل 050 21 ذلك معرب ܪܝܕ( ومعناه العظيم العريز
3405:4 5 74( والكرسوفة والكرشن لغات فيه ٠‏ فارستة
3442:( الكزمازّج ) ثرة الطرفاء < 92( وهي 6 من كزم اي طرفاء
3766:ملو ول يوان فقيه الفرس ܠ المجوس 3:5( وججعة
3817:(الأنار) فارسي محض اي 21( واصل 0 المت ومنسة الارائئ”
3916:* 5 السكران ܐ :¥97 اي سكر ومن بان (ويقال .50
3933:وهو فارسي | الاصل ܨܚ( وهو تين بخ انسار وهو مر ܝ ܢܝ اي مقاوب
3973:في طلوع الشمس فوق الماء ويزهر وفي غرويها يع في 2( وقيل اله عند وقوعه
4001:» ( )74 ܟ ) السئ الخاق تعريب 900( واصل ܐ يقطع الفا .
4014:( الول ) سم 507 ܢܝ ملاهل
4051:( الوبر) فارسيتة وبر 905 اصغر 7 »× 0:37371
4325:ܐ ܦ \ ( وم١١‏
6254:¥ ( و2061
```


## [2026-10-17T00:01:35.112Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4040,4075p AFM_pages.txt | cut -c1-200; grep -n 'pdf page' AFM_pages.txt | awk -F: '$1<4075' | tail -2"
}
```


### [2026-10-17T00:01:35.368Z] TOOL RESULT

```
* ( هوم ) المجوس : فارسيَّنهُ هوم ٠‏ قال في البرهان القاطع :« ܐܬܕ شجر يشبه
الصنوبر كثير الوجود في بلاد فارس «عقود الساق ورقه سُبيه بورق الياسسين.
وكان المجوس £ طقّوسهم ܒ بإباذييم | منه ولذا سني هوم المجوسل | ܘ | صمت
,3 ܚܝ
و3 ( الحاوآت 22 الذى يدق شه الدواء وغاره 2 هاون ܦ 4 ة هاون
بالتركة 313 بالكردنة
د ( | ܙ ) ܐܕܒ ^ 7 32 هيرون 2 بضصرب °ܝ القصب علو
الداخل ̄ܒ 4 زم ر سّليه با لقَطن :رفير 354
+ ا ( 00:0 وقمل اسم اداته 0 56 هس وهو الحراث
ܒܝܒܗ ® (م 026 © جرمعى
153
( الوبر) فارسيتة وبر 905 اصغر 7 »× 0:37371
5 10509
9 الرَح) ضرب من الأدوية وهو اصول نبات كالبردي تعريب‎ ١
0 ( 565 الا الَهُ اعظم من يكون في ܝ ܐ
والصحارى 27 171
140000 من امات محتبل ان :536 كته الى
النقطة ومنه الكردي تت
` ضرب من الاوتار او العود او ܗ معرب وله بالفارسّة 15
1 ܝܐ ) ٠‏ قات و 3 د تت اللغة اله ܢ بيدي بل ونك بعنى الصدى
والصوت
( ! العنب الاسود 3 او هو من توافق 335( ܒܣ ®
ܛ الشراب و 053 ܢ ܐܚܝܬ يعنى الكرمة والشراب و يوراه بالونائيّة و نامف
بالروممة و7111 ا و 82110 بالروسمة و7110 بالايطاليائة و 5711
بالانتكليزية و ܐ 5 0 9 0 ±
جنسيليوس ) ٠‏ ويوافقة ايضاً العتى ]ܐܟ £¿ ܕ ܥܢܒܐ بالاراميّة
معدو بدهܡܗ ܀ ¥ ܐ| وه
باب 0
1
والمتفر ٠‏ و يرادفة التي ينان وقالوا فيه يس :
( المَارَّج والمَارّق ) القلى والسوار تعريب بآرَه
( الإبأرجة).مسجون.مسهل معرب ااره ومنة اللدر الى 201
( الي تدج ). السوات وداه صرمت رانده عمقي عر الا
( اليَرمنآن) نسيج رفيع من ܐܝܠܨ ܨ فارسيّة ومعناه ܩܠ ܘܬܐ ܚܨ به لاله
ما يهندى ٠‏ واأشهور على لسان العوام ارمغان ( حيظ ]` ¬ © ?00
على 4 والفضّة 3 ومئة ارمغان بالتركيّة ܦ 23
```


## [2026-10-17T00:01:41.684Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'woin\\|w-oin' AHD_watkins1985.txt | head; echo ---POK; grep -n -i 'oinos\\|u̯oino\\|uoino\\|u̯īno\\|vinum' POK_full.txt | head; echo ---WLD; grep -n -i 'vinum\\|oivo\\|oinos' incoming/WLD/WLD_Bd1_pages.txt | head -5; echo ---IEC; grep -n -i 'woin\\|vīnum\\|vinum' IEC.txt | head; echo ---SYN; grep -n -i 'vinum\\|WINE' SYN.txt | head"
}
```


### [2026-10-17T00:01:42.208Z] TOOL RESULT

```
1110:[vinum. Wine. Latin noun, related to Greek oinos, wine. Probably from a Mediterranean word *win-, *woin- meaning “wine.” 1. Latin vinum: VINACEOUS, VINE, VINI-, WINE; VINEGAR. 2. Greek oinos (earlier woinos): OENOLOGY, OENOMEL.]
---POK
2876:Material: Gr. {*avinumai) a'lvupai 'take, pack, touch', only present and imperfect tense. 
26022:Latin Onus, old oinos. 
26103:Sardinian unu, Celtic: Proto-Celtic+ oinos, Gaulish+ *6nos, Brythonic (P-Celtic) : Welsh un, 
52085:urbanized for the plebeian *cenum irom * co/nom, *quoinom), in-, con-qu/nare^ smudge, 
76762:vinum fundebatur ' s. WH. I 320; 
93633:Latin *a/77c»/ (compare Summo/C\L. II 1750) could amoinos= amoenus shaped sein, as 
---WLD
4865:Sunimoi OIL. II 1750) konnte amoinos = amornus gebildet sein (amoenus
4871:ferner durch gr. rogyovi] (zu /op/co) neben rogyoivog (zu rooyiot ) gestiitzt
9117:  gr. oivog, omj „eins auf dem Wfirfel“, lat. anus, alt oinos, air. den „ein“,
10341:*oinos.
12628:zum Zorn"       (ob hierher aucli gig,                 oivog „]Sase“         als   „die rinnende"?        Yf.
---IEC
---SYN
896:Grk. Adrayes ‘drops of wine in the bottom of the cup’, Lat. latex ‘liq- uid’, OHG letto ‘clay’ (NHG letten), etc. Walde-P. 2.381. Walde-H 1.770.
1972:Br. latar : Corn. lad ‘liquid’, W. laid, Ir. lathach ‘mud’, Grk. \arayes ‘drops of wine in the bottom of the cup’, all fr. the notion of ‘wet, liquid’. Walde-P. 2.381. Henry 180.
2449:Sw. gosse : Norw. gosse ‘strong fellow’ and ‘boar’, NE dial. gussze ‘swine, pig’, etc., a collog. word of the most diverse applications. Bjérkman, IF 30.252 ff. Hellquist 294.
3771:such diverse creatures as ‘ox’, ‘swine’,
3784:5 ff.). , ae ae generic terms for bovine anl- mals, sheep, and swine have become specialized in Germanic to denote the female, as NE cow, ewe, sow.
3785:Conversely, words for a special class, especially the young or the female, may be used generically, as Lat. porcus, NE pig for swine, NE hen or chicken for do-
3867:1. Grk. éxréuyw lit. ‘cut out’, epd. of Tépvw ‘cut’ (9.22). Hence éxroun ‘cas- tration’, éxrouias or rouias ‘castrated man or animal’, the latter the regular term in Aristot. HA for the castrated ox, Swine, sheep.
3921:For the classification of ‘large’ and small cattle’, cf. that of Grk. rpéBara (below, 2; in the Arc. inscription ‘swine’ are mentioned separately as if not falling clearly in either division), Lat. (Varro, RR 2.1.10, 12) pecus maius (boves, asini, au BECuS minus (oves, caprae, sues), It. 5 € grosse, minute, Fr. gros, petit bétail, oe eater, minor, Rum. vite ais Gee : HG gross-, Kleinvieh, etc.; Geen e ALT aps small cattle’ vo rote camel), ee Sa € identi é , :
4060:6. ChSI. pastyr?, pastucht, fr. past; ‘pasture’ (3.16), and so the other Slavic words. Beside these and in more com- mon use in some of the Slavic languages is a series of specific terms derived from the names of the animals, as SCr. gove- dar, kravar, ovéar, svinjar, kozar ‘cattle-, cow-, shep-, swine-, goat-herd’, Boh. kravdk, ovéak, etc., like Fr. bouvier, va- cher, berger, etc.
4288:3.31-3.35. Note that in the headings and translations either swine or hog, is used as the generic term, barrow for the castrated, and pig for the young animal, that is, in accordance with its original (and still mainly U.S.) use, in contrast to the now current British generic use.
```


## [2026-10-17T00:01:46.705Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wine' POK_full.txt | head -15; echo ---; grep -n -i ' Wein\\b\\|„Wein' incoming/WLD/WLD_Bd1_pages.txt | head -8; echo ---SYN; grep -n 'WINE\\|5\\.92' SYN.txt | head -5; echo ---IEC; grep -n -i 'wine' IEC.txt | head -10"
}
```


### [2026-10-17T00:01:47.010Z] TOOL RESULT

```
3709:Indie tamas; Lithuanian tamsa' {\n addition o^ivr) "harrow' Hes.), 6^0(; "wine vinegar'. - 
9616:plugs) ', Old English pgegelvn. " wine pot ', engl. paiV bucket ' from Middle Latin pagella^ 
10918:flask, a large cask or barrel, used esp. for wine, ale, or beer ' derives from Latin buttis ' 
12528:mould on the wine'; Latin bnsa irom dem Venet. or Messapic). 
14194:Material: gr. -n'xQoq, n. "barrel, vat, cask, wine cask ', niGoKvp, Attic cpiSoKvp ds., Latin fidelia 
14523:gr. oivo-cpAu^ " wine-drunken '; cpAu^u) " to bubble up, boil up, surge up, overflow, also 
17575:hoe', lengthened grade dolium^a wine-jar, cask, barrel, vat' (as proto Slavic Ic^/y" barrel. 
18512:German trottei. " wine-press ', Intens. Old High German trotton 'tread'; Modern High 
18732:drav/st, Latvian dravat ' wood beehive ', in addition Old Prussian drawinei. 'prey, bee's 
20774:alb. drefh {stem *dredh-), Aor. drodha^ turn round, turn together, twine, spin ', alb.- 
29004:slaughtered swine '; 
29429:Old Latin aser {asset), ass>r "blood', assaratum^ drink from the mixed wine and blood ' 
31361:capital of a column, in this form, wine-cooler, mould for casting iron, reservoir of an oil- 
33210:interweave, intertwine ', gaubiu, gaubti^ cover, wrap up, curve ', gaubtis ' crook oneself ', 
34648:Material: Gr. ypu 'a grunt, as of swine', ypu^oo (*ypu5jaj) "to grunt, grumble, mutter', 
---
2975:tdmas-, lit. tamsd (dazu dgivrj ,,Egge“ Hes.), d'fo? „Weinessig“.
3180: f.   „Trane“. Ygl. ai. agiayumi lit. asaroju „weine".
14942:   alat. aser (asscr) „Blut“, assaraium „Trank aus Wein und Blut gemischt“
15130:arm. ttigi „Weinstock“ (Liden; kann *oiuiia aus              aber auch diviia
19521:ahd. weinon „weinen ‘, ags. tcdnian , aisl. veitm „jammern
20001:as. wGpian ( iviop ) ds. (wop „Jammer“), ags. arepan ( wrop) „weinen“ (wop
20853:wohl der Kame des Veins: gr. olvog „Wein“, oi'vij „Weinstock“, otvag,
20854:-adog ,,Weinstoek, Rebe, Wein“, arm. gini „Wein“ (*iioinio-, Jensen ZdMG.
---SYN
4289:3.31 SWINE
8285:ON gir, later glvadr, fr. ol ‘ale, beer’ (5.92).
8314:CHAPTER 5 FOOD AND DRINK; COOKING AND UTENSILS 5.11 Eat 5.57 Minn 5.12 Foop 5.61 Mezar 5.13 Drink (vb.) 5.612 Burcurr 5.14 Hunexr (sb.) 5.62 Brrr 5.15 Turrsrt (sb.) 5.63 Sausace 5.16 Suck (vb.) 5.64 Sour, Brots 5.17 Mrx 5.65 VEGETABLES ' 5.21 Cook (vb.) 5.66 Bran ? 5.22 Bor 5.67 Pra 5.23 Roast, Fry 5.68 Onion 5.24 Baxe 5.69 CaBBAGE 5.25 Oven 5.70 Porato 5.26 Por 5.71 Fruir 5.27 Kerrin 5.72 APPLE 5.28 Pan 5.73 PEAR 5.31 Disx 5.74 Pracu 5.32 Prats 5.75 Wie : 5.33 Bown 5.76 Grape 5.34 Pircuer, Jue 5.77 Nur 5.35 Cup 5.78 OLIvE 5.36 Saucer 5.79 Om 5.37 Spoon 5.80 Berry 5.38 Kyire 5.81 Saur 5.39 Fork 5.82 Prpprr 5.41 A Mua, 5.83 VINEGAR 5.42 BReakFast Bi Rdeer ona 5.43 Luncx 585 § 544 Dinner een Base Sucnbn. 5.86 Mixx (sb.) 5.51 Breap 5.87 Minx (vb.) 5.52 Caxn 5.88 CHEESE 5.58 Dover 5.89 Burrer 5.54 Kwrap 5.91 Merap 5.55 Mzau, Frour 5.92 Wine 5.56 Grinp 5.93 Brrr
9741:5.92
9752:WINE Lith. vynas Lett. vins ChSl. vino SCr. vino Boh. vino Pol. wino Russ. vino Skt. draksarasa- Av. masu-, xSudra-(?)
---IEC
494:ambhmn- (ombhmn-, period". WP I, 41 - Arm. (ambig.) am (i-stem: ‘year’. Cf. samos}; Oss. cf. anz (cyear: Li. amžius "age Lat. cf. soll-emnis “annual, ritual’; OLat. per- emnis ‘annual’; MIr. amm “point of time’; Gael. ám, id.; Sequanian amn, amb, am ‘time’; cf. the cpd. am-ser (“time in W. Br.OBrit.Cor.); ON cf. imbru-dagar ('ember-days', fr. *ambheso); OE ymbryne; ymbren; WG imbs *wine-festival
1101:bhal- (2) ‘forehead; prominence’. WP II, 175 Skt. cf. (a)bhalam (1) ‘forehead’; Gk. cf. pháios ‘forepiece on helmet? a component also of phál-agx ‘wedge-shaped frontal formation’, phalaris ‘coot; Alb. ballë ‘forehead, front of a formation’; Lat. fala *battering-ram', beside in-fula ‘headgear, garland on animal fore- head; W bâl, pl. baloedd (*bhalos, -es-) ‘peak, prominence’; ON bali 'grass-bank' ; OPr. ballo ‘forehead’. Cf. also the Gk. cpd. phal- akrós ‘bald’. Cf. bhàal- (2). The form re- presented in Lat. balaena seems to represent a non-Greek form of phálaina (‘whale’, lit. ‘hostile forehead’, cf. nuino- ‘hostile’ in Gk. ainós: Olr. anfine, s. ‘enemy’: OE unwine, id.). For OHG belihha ‘coot’, see FK: Belche
1428:bhluks- (bhlugs-, bhlusk-) ‘gush, flow? Arm. byxem, v. id. beside byxim, id.; Gk. *phláxo, v. “will gush' (to phláo and phlüzo), ` cf. oinó-phlux, gs: -phlugos ‘flushed with wine’; Lat. fluxus, adj. & m. ‘gushing; gush’; OE blyscan, v. ‘blush’; E blush. (Isophonic Du. blusschen and blussen, v. uit- 'extin- guish")
2654:duinos, à (2) (duisnos?) ‘turn, spin’. Cf. WP I, 820 Gk. dinos, dinë *'eddy; giddiness; lathe; threshing-floor'; cf. kor-dinéma *head-spin- ning; vertigo’; én-dina (pl. *entrails"); dinéo, v. “spin” (but Aeolic dinna ‘eddy’ suggests a type *duisnà, q. v.); OE twin ‘twine’; Du. twijn, id.; Sw. cf. tvinna 'twine, spin'; Nor. tvinne, id. cf. tvist ( yarn, twist’, fr. *duistós). See duisnos
3134:dhrudho, ið ‘thrust, poke, squeeze’. Cf. WP I, 871 and see drudh-. (The Alb. Ir. & MHG evidence is ambig.) Arm. drdem ‘provoke’; Ir. druidim (ambig.) ‘push, drive, force, close’; Alb. (ambig.) drudh ‘squeeze’; MHG trut ‘goblin’; trute, f. “evil fairy’; trote, trotte “winepress'; LG Drude ‘bogey’. (A possible isophone occurs in Cz. drdat ‘pluck feathers’ and in Pol. derdać ‘rush, dash’)
3514:eksto- (eKst-, oKst-) “out, outside; beyond, excep. WP I, 116 _ Arm. əst- (cpds. "out, beyond"); ost (prp. 'ac- cording to"); Gk. ektós; Alb. jashtë; Lat. cf. exta ‘bowels; middlings; dregs; must of wine’; Mir acht "but
3690:nantism obscure); Per. ašk ‘teardrop’ beside (cpd.) sir-iSk, id.; Tokh. AB ysar, B yasar- ‘blood’; Arm. ariwn, gs arean “blood? beside err ‘caries’; Hitt. eshar, gs esnas, eshanas “blood? beside eshahru ‘tears’; Gk. éar, ear, ds eíari ‘blood’; OLat. aser (for *asser), id. cf. assar-atum “drink of blood and wine’; Umb. erus ‘blood’; Li. ãšara ‘teardrop’; Latv. asara, id. beside asins ‘blood’. (The ultimate pho- nology of this word-type is entirely obscure. Cf. speléghnos, splighén- for a similar problem)
4559:ghal- “hard, strong, able; hardness, strength, ability'. WP I, 539. Cf. ghalmos Gk. cf. khal- in kbalepós "hard": khál-ups "steel": khal-kós, and perh. kbális “strong wine’; Lat. cf. hal- (in hal-lex, -licis “big toe’, fr. *ghal-di&-, cf. pol-lex ‘thumb’, fr. *p]-diK-); Olr. gal, gail *valour, feat, battle; OBr. gal ‘strength’; W gallaf ‘I can’; gâll ‘energy’; Br.
5226:guinó (guein-, guoin-) “harm; be harmed, fail Skt. jinàmi ‘defeat; Av zinā- ‘harm’; OPer. -dinam ‘rob’; OE -cwinan “fail, go out; Du. kwijnen, Fris. kwine ^waste away'; LG quie- nen, id. Cf. o-gde Du. kween ('barren, sterile’, fr. *guoin-)
5397:orkor, o-st. (throat, fr. *guoreus; Gk. br-, -bros in br-ágkhos, br-ógkhos, -okhthos, br- ókhos, br-ókhó, -ükho, molo-brós, etc.; Alb. cf. gur-mac, -maz ‘throat’; Lat. voro, are; OCS Zro, Zréti ‘devour’; Li. cf. girà small beer, sour milk’; girtas ‘drunk’; girtüs ‘heady’, of wine; Latv. dzira ‘drink’; dzīres ‘feast’
```


## [2026-10-17T00:01:50.377Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 20848,20862p incoming/WLD/WLD_Bd1_pages.txt; grep -n 'pdf page' incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<20853' | tail -1; echo ---SYN; sed -n 9741,9775p SYN.txt | cut -c1-600; echo --POK; grep -n -i 'u̯oino\\|woinom\\|u\\̯oi-no\\|oinos)' POK_full.txt | head; grep -n \"olvo\\|oivo\" POK_full.txt | head"
}
```


### [2026-10-17T00:01:51.001Z] TOOL RESULT

```
wohl ags. icine-winda „Uferschnecke“, wining „Binde“.                       —
                                                                 Hierher auch
wohl der Kame des Veins: gr. olvog „Wein“, oi'vij „Weinstock“, otvag,
-adog ,,Weinstoek, Rebe, Wein“, arm. gini „Wein“ (*iioinio-, Jensen ZdMG.
48. 429 if Bugge KZ. 32, 83), alb. true, tosk. cere ,,Wein“ ( *uoina G. Meyer
            .
                                                                                    ,

Alb. Wb. 465 f.), lat. vhtum letztere ist nicht bloB die Quelle von air. fin.
                                     ;


---SYN
5.92
olvos kpagl Goth. wein Yinum ON vin vino Dan. vin vin Sw. vin ving OE win vin ME wine fi in NE wine tion Du. wijn min OHG win win MHG win
NHG  wein
igitized by Arya Samaj Foundation Chennai and eGangotri
COOKING AND UTENSILS 389
5.91 MEAD Goth. *midus
Lith. midus Lett. medus ChSl. (medi) SCr.  medovina
medo Boh. medovina Pol. mi6d Russ. med
Skt. madhu- was used for any sweet in- toxicating drink, especially the soma juice. Av. maéu- was a kind of wine or beer (Barth. 1114. NPers. mai ‘wine’, Horn 1003). Grk. pé6v occurs only as a poetical word for ‘wine’, but is the source of the common prose words pefiw, peOicxw ‘be drunk, make drunk’, whence NG peOucpévos ‘drunk’.
2. Grk. pedirecov (Plut. Mor. 672b of the drink of the barbarians), deriv. of perc ‘honey’.
3. Late Grk. sdpopedr, cpd. of téwp ‘water’ and pédt ‘honey’, whence Lat. hydromel(t), It. idromele, Fr. hydromel (> Rum. hidromel), Sp. hidromel (also aguamel, with substitution of agua ‘water’). These words are those em- ployed to denote the ‘mead’ of other peoples, though also used of an unfer- mented mixture of honey and water.
WINE Lith. vynas Lett. vins ChSl. vino SCr. vino Boh. vino Pol. wino Russ. vino Skt. draksarasa- Av. masu-, xSudra-(?)
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
i ' | { : | ' { I } t
: vs sf
Digitized by Arya Samaj Foundation Chennai and eGangotri
390 SELECTED INDO-EUROPEAN SYNONYMS
The intensive cultivation of the vine and the use of wine as the customary alcoholic drink had its home in the east- ern Mediterranean region, whence it spread over Europe, mainly through the Romans. In ancient India and Iran wine was not one of the common al- coholic drinks. Schrader, Reallex. 2.642 ff.
1. Grk. ofvos, early fotvos, Lat. vtnum (prob. fr. *woinom, like vicus, vidi : Grk. fotos, fotéa; in which case Umbr. vinu must be a Lat. loanword), Alb. vené, Arm. gini, together with the Semitic words, Arab. wain, Hebr. yayin, all prob. loanwords fr. some prehistoric Mediterranean source. So Meillet, MSL 15.168, Ernout-M. 1111. But even so, the source could be some IE language of that region. For if we as- sume that the orig. sense was ‘vine’, it is attractively derived fr. the same root as Lat. vitis ‘vine’ (IE *wei- in words for ‘twist, wind’, see 8.67). Walde-P. 1.226. Schrader, Reallex. 
Lat. vinum is the source of all the other Eur. words, except the Greek and Albanian.
2. NG xpact, fr. dim. of Gr ‘mixture’, its use arising from mon Greek practice of mixing water. The use of ofvos for th the sacrament may have been & factor in its disappearance from common speech.
k. Kpaors the Com. Wine and wine of
3. Skt. draksarasa- (rare), cpd. of draksa- ‘vine, grape’ (5.76) and rasa- ‘juice’.
Av. maéu- : Skt. madhu-, etc, 5.91.
Av. x§udra-, ‘liquid, semen’ also an ‘alcoholic drink’ (‘wine’? So Barth, 555) : x8usta- ‘liquid’, xgaosah- ‘stream, flood’, Skt. ksoda- ‘swell’ (of the waves), Walde-P. 1.502. t
Among other Indo-Iranian words for alcoholic drinks are: Skt. soma-, Ay. haoma- ‘juice of the soma plant? : Skt, su- ‘press, extract’ (Walde-P. 2.468); Skt. mada- ‘intoxication’ and Av. maga- ‘intoxicating drink’ : Skt. mad- ‘be glad, be drunk’, Lat. madére, ‘be wet’, ete. (Walde-P. 2.230f.). See also under ‘beer’ (5.93).
See
5.93 BEER Grk. — (Bpiros, tis) Goth. .... Lith.  alus, pyvas NG Hripa (fd00s lit.) ON bjorr, ol Lett. alus Lat.  (zythum, cervesia) Dan. gl ChSI. pivo, olit It. birra Sw. él SCr. _pivo Fr. bitre OE béor, ealu (alu) Boh. pivo Sp. cerveza ME bere, ale Pol. piwo Rum. bere NE beer Russ. pivo Ir. cuirm, laith, beoir Du. bier Skt.  yavasurd- Nir. —_ lionn, beoir OHG bior Av. (hura-) W. curw MHG bier Br. bier NHG bier
Beer was a common drink among most of the European peoples, as well as in Egypt and Mesopotamia, but was known to the Greeks and Romans only as an exotic product. Schrader, Reallex. 1.142 ff.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1. Grk, pros or -ov, first used (Ar- chil.) with reference to Thracian of Phrygian beer and properly a Thracian form : OE bréowan ‘brew’, etc. Walde- P. 2.168.
Grk. fifos (> Lat. zythum), first used
fooD 4 Hdt. 2.77 re- ounueve)s and
Dos, a xadolpevo? g kal ex rev KpLOaY
g xadéovor £80s, genuine Grk. te. Walde-
--POK
ugrep: error: error at position 24
(?mi)u̯oino\|woinom\|u\̯oi-no\|oinos)
     invalid escape___/


6379:'shining'; es^stem in £vapyr|(; " perspicuous, clear ', apy£a-Tn(; epithet oivoioc,, " 
14523:gr. oivo-cpAu^ " wine-drunken '; cpAu^u) " to bubble up, boil up, surge up, overflow, also 
25133:Tpau|jaTa Hes., eAKoivoo ' I am wounded '; 
37657:thrak. ^iAai 6 olvog Hes. {*ghe/-). 
40073:ds., cpovEuq "murderer', avSpocpovoq " men killing ' (see also Boisacq under cpoivoc;); Note: 
62416:vr|- in vnTTOivo(; " unavenged ', Doric vqttoivoc;, etc.);
```


## [2026-10-17T00:01:55.358Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'gini\\b\\|arm. gini' POK_full.txt | head; grep -n -a -i 'wine\\|wein' KLN_1966.txt | grep -i 'vinum\\|oinos' | head; grep -n -a 'vinaigre' KLN_1966.txt SKT.txt | head -5; grep -n -a -i '^vine\\b\\|^vinegar\\|^wine\\b\\|^VINE\\|^WINE' SKT.txt | head"
}
```


### [2026-10-17T00:01:55.710Z] TOOL RESULT

```
89981:verge : Latin virgo : Portuguese virgem : Sardinian Campidanesu birgini : Valencian verge 
24480:moss,  n.  —  ME.  mos,  fr.  OE.  mos,  ‘marsh,  moor  , rel.  to  OE.  meos,  ‘moss’,  ON.  mosi,  Dan.  mos, ‘moss’,  Swed.  mossa,  ‘moss’,  mosse,  ‘moor’, MDu.  mosse,  Du.  mos,  ‘moss',  OHG.,  MHG. mos,  ‘moss,  swamp,  moor’,  OHG.  mios,  MHG. mies,  ‘moss’,  G.  Moos,  ‘moss’,  ON.  myrr,  ‘bog, swamp’,  fr.  I.-E ,*meu-s-,  whence  also  L.  museus, ‘moss’,  Lith.  miisaX,  ‘mold,  mildew’,  OSlav. mucha,  ‘moss’  and  perh.  L.  mustus,  ‘fresh,  new’ (if  fr.  *mus-tos,  ‘wet,  moist’),  whence  mustum (short  for  mustum  vinum),  ‘new  wine’.  F.  mousse, ‘moss’,  is  a  Teut.  loan  word.  I.-E.  *meu-s-  is  an -s-enlargement  of  base  *meu-,  ‘moist;  marsh; moss’.  Cp.  mire,  muscoid,  muscology,  mushroom, must,  ‘new  wine’,  mustard.  For  derivatives  of base  *meu-d-,  a  -(/-enlargement  of  base  *meu-, see  mother,  ‘dregs’,  and  cp.  words  there  referred to.
24618:malmal.  Cp.  mull,  ‘muslin’, mulse,  n.,  wine  mixed  with  honey.  — •  L.  mulsum (scil.  vinum),  neut.  of  mulsus,  ‘mixed  with  honey', which  stands  for  *meI-sos  and  is  cogn.  with  L. mel,  gen.  mellis,  ‘honey.’  See  mel. mult-,  form  of  multi-  before  a  vowel, multeity,  n.,  the  quality  of  being  many.  —  Form¬ ed  with  suff.  -ity  fr.  L.  multus,  ‘much,  many’. See  multi-.
20912:Vine.  Vinegar  ;  fee  Wine,
21912:Wine.  Some  think  that  Gk.  o7vot  ta not  of  Aryan  origin;  cf.  Heb  yajrim,  winei Ethiopic  tttfioi,  tuamg  wine.
```


## [2026-10-17T00:01:59.492Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i 'oinos' KLN_1971.txt | head -5; grep -n -a -i 'Armenian gini\\|alb. vere\\|vere, vene\\|\\bvere\\b' POK_full.txt | head; sed -n 21905,21916p SKT.txt; sed -n 20905,20914p SKT.txt; grep -n -a -i 'vinaigre' KLN_1971.txt | head -3"
}
```


### [2026-10-17T00:02:00.148Z] TOOL RESULT

```
52069:lic’, formed fr. co- and OL. moinos, moenus (L. 
147337:L. munus (OL. moinos, moenus), ‘service, of- 
163626:dimin. of OL. oinos (whence L. unus), ‘one’. See 
167063:oinos , L. unus, ‘one’, OSlav. -inu (in jed-inu, 
257086:ty’, and rel. to OL. oinos, L. unus, ‘one’. See 
40048:Avestan y^z?M/5-, Old Church Slavic z^fva), vrtra-han-. Gen. -ghn-ah{= Avestan vere&ra- 
89649:-aboc, ' grapevine, vine, wine ', Armenian g/n/^mne ', ( *uoi-nJom), alb. vene, Tosc vere 
92267:Maybe alb. verej^ perceive, spot, detect ' > folk etymology ve re^ perceive ' Latvian 
One  (i).  Already  written  vfon  in  M.E. See  Guy  of  Warwick,  cd.  Zupitia.  note  to
l.  7027.
Oolite,  a  kind  of  limestone.  (F.  -  Gk.) F.  ocUthe  (with  th  sounded  as  /).  — Gk. il/ii-f.  egg;  Ai9-«r,  stone.  LiC  'egg-stone.' Sec  Oval.
Bock  (i).  We  actually  find  A. S  sidtt- rocca,  gen.  pi.,  to  transUle  L.  icopulorum. Thii  may  have  been  borrowed  from  Celtic At  any  rate,  it  is  strong  evidence  agamst  a Latin  origin.
She.  The  A.  S,  seS,  Icel.  Tjd^  answcn to  Skt.  tyd,  fem.  of  syas,  that.  Frob.  from Aryan  SA.  be;  YA,  that.
Slender.  Really  (F.  -  O-Du).  OF. uclendrt  (Palsgrave).  — O.Du.  tUtider,
Trunk  (2),  of  an  elephant.  Comipted from  F.  trompe.  'a  irump;  also,  the  snowt of  an  elephant;*  Cotgrave.
Wine.  Some  think  that  Gk.  o7vot  ta not  of  Aryan  origin;  cf.  Heb  yajrim,  winei Ethiopic  tttfioi,  tuamg  wine.
I
I
APPENDIX.
I.    LIST  OF  PREFIXES.
VINCULUM.
uiila.  a  farm-house.  Der.  vilUtin-y,  O.  K. viUnii,  vi/a»ig,  scn'itude,  baseness. Vinculum,  a  link.  (L.)  L.  uineulum, a  bond,  fetter.  — L.  uincire,  to  bind. Vindicate.  (L.)  I'Vom  pp.  of  L.  uindi' care,  to  arrogate,  lay  claim  to.^L.  uinefic-, gtem  of  uinUcx,  a  claiinanl,  lit.  'one  who cx|.r(SMs  a  desire.'  —  L.  uin-,  si^ifytng '  desire,'  allinl  to  uenia,  favour,  pcrmis- 8ton  ;  Mc-,  base  of  diatre,  to  appoint, dh'ere,  to  s-iy.
avenge.  {¥.  —  L.)  O.K.  avfngier,  to a%"cfipc.  —  F.  a  (L.  d.i^,  to ;  vfngt'er,  to nvtr.ge,  from  L.  uiniHcare,  to  Iny  claim  to, also  to  avcn^  (above).
revenge.  {¥.  -  L.)  O.  F.  rrvtn^s^r, later  rtvituhtr,  to  Avenge  oneself.  (F.  re- fUHM^/-.)—  K.  rr-  ( =  L  nr-),  again  ;  O.  F. tfctt^'er.  Vftt^er,  from  L.  tiinduart.
vengeance.  ^F.  —  U)  F.  vrn^qmnci, ■vengeance;*  Cot.  —  F.  i/fln^r,  to  avenge.
»L.  uinriicart.
vindictive.  (F.  — L.)  Shortened  from F.  vhuiitatif,  *  revenging  ;"  Cot,  From  L. uirti/irafHs,  pp.  of  uintiicare,  to  avenge ; with  siiffix  -iUMS.    See  Vindio&te  (above).
Vine.  Vinegar  ;  fee  Wine,
Vinowed,  mouldy.  (E.)  Also  ftu- Vitd^fenowed  (Narcs).  From  AS.  Jituggd, Xf[*.  ai  Jine^an,  to  become  mouldy.  — A.  S. /i'tig,  mouldy  (Joshon.  \x.  5).  The  right form  seems  to  he  fetti'g,  answering  lo  M.  E. /ettfty,  dirty,  vile,  also  used  to  mean '  mouldy,*  adj.  from  A.  S.  fenn.  mire,  the same  word  as  mod.  ^.fttt'.  see  Pen.
Vintage,  Vintner ;  sec  Wine.
262203:vinaigrette, n., a bottle for holding aromatic 
262204:vinegar, etc. — F., dimin. of vinaigre, ‘vinegar’.
```


## [2026-10-17T00:02:01.853Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89640,89660p POK_full.txt; grep -n -a '^vinegar\\|^wine, n\\|^vine, n' KLN_1971.txt | head; "
}
```


### [2026-10-17T00:02:02.276Z] TOOL RESULT

```
E. With /^formant: 

Gr. !(;, \yoc, "sinew' (*Fi-v-: Czech K/>7e/r"band, strap, headband ' or *Fia-v- zur root form 
ueis-2)\ Old Church Slavic i/e/7i.C6 "Kranz'; probably Old English wine-wincia {bes\6es 
pTne-wincle) "Uferschnecke', w/>7/>7^ "bandage'; about gr. \c, compare Schwyzer Gr. Gr. 1, 
5702; 

barely here the name of Weins: gr. oTvoc; (myk. vo-no-) "wine ', oivr) " grapevine ', o\ydc„ 
-aboc, ' grapevine, vine, wine ', Armenian g/n/^mne ', ( *uoi-nJom), alb. vene, Tosc vere 
"wine ' {*uoina), Latin vTnum, latter is not bare die wellspring from Old Irish ffn, cymr. gwin 
and from Gothic wein. Old High German Old Saxon Old English Old Church Slavic vTn 
(from which again Old Church Slavic v/no and from dem Slavic Lithuanian vynas), but 
probably also die from Faliscan Volscan uinu, Umbrian vinu, uinu, da the Pontus the 



originator of tlie Weinkultur war, liandelt es sich wobi urn ein vorderasiat. word; compare 
Proto Semitic *wa/nu {arab. athiop. wa/n, hebr.jaj/n, assyr. Ihu) and Hittite wi-ja-na-a-, 
Hieroglyphic-Hittite wa(i)ana-, Luvian dial, win-, s. lastly Laroche BSL 51, XXXIII, A. 
Kammenhuber Munch, stem f. Spr. 6, 53 f. 
6516:vinegar. Cp. also mediocre, ocrea, Ocimum, Oxa- 
262204:vinegar, etc. — F., dimin. of vinaigre, ‘vinegar’. 
262297:vine, n. — ME., fr. OF. (F. vigne), fr. L. vinea , 
262319:vinegar, vineyard, vinous, vintage, vintner. Cp. 
262323:vinegar, n. — ME. vinegre , fr. OF. (= F.) vi- 
262327:vinegaroon, n., a whip scorpion of Mexico (Mas- 
267456:wine, n. — ME. win , fr. OE. win , fr. L. vinvm ,
```


## [2026-10-17T00:02:05.929Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=89500 && NR<=89640 && /Page\\(s\\)|^Root|Pokorny/' POK_full.txt | tail -5; sed -n 262297,262330p KLN_1971.txt; sed -n 267456,267466p KLN_1971.txt"
}
```


### [2026-10-17T00:02:06.343Z] TOOL RESULT

```
Root / lemma: ueiR-, uiR-, uoiRo-{* duei- ksayatlj 
Root/ lemma: ueiR-, uiR-, uoiRo-{* duel- ksayati): "house, settling' derived from Root/ 
Page(s):1131 
Root / lemma: uei-1, ueia- : uT- 
Root/ lemma: uei-1, ueia-. uT-\ "to turn, bend, wind, *branch out' derived from Root/ 
vine, n. — ME., fr. OF. (F. vigne), fr. L. vinea , 
‘vineyard’ (whence also It. vigna, Rum. vie , 
Proven?, vinha , Catal. vinya, Sp. viha, Port. 
vinha, ‘vine’), prop. fern, of vineus , ‘pertaining 
to wine’, used as a noun, fr. vinum , ‘wine’ 
(whence It., Sp. vino. Rum. vin, Proven?., Catal. 
v/, F. vin. Port, vinho, Goth, wein, OHG. 
(MHG.), OFris., OS., OE. win (G. Wein), 
OSlav. vino (Russ, vind), OIr. fin, W., Bret. 
gwin, ‘wine’ and prob. also Etruscan vinu, of 
s.m. Cp. ofvT) (for *folvY]) ‘the vine’, olvo? 
(dial. Foivo?), ‘wine’, Alb. vene. Arm. gini , 
Georgian yvino, ‘wine’. Cp. also Heb. ydyin 
(prob. for *wdyin), Ugar. yn, ‘wine’, Ethiop. 
wayn, ‘grape, wine’, Akkad, inu, ‘wine’. (Cp. 
also Basque ayen, aihen , ‘vine’, which was prob. 
borrowed from the Semites through Carthagin- 
ian mediation.) The ult. origin of these words is 
unknown. Some scholars trace them to the 
Semites, others seek their origin in the Aegean, 
still others in Asia Minor, Caucasia or in Ar- 
menia. Cp. wine. Cp. also Vendemiaire, vignette, 
vinegar, vineyard, vinous, vintage, vintner. Cp. 
also oeno-, Oenantbe, Oenius, oenomel, Oenone. 
Derivative: vin-y, adj. 

vinegar, n. — ME. vinegre , fr. OF. (= F.) vi- 
naigre, compounded of vin aigre, ‘sour wine’. 
See vine and eager and cp. vinegaroon and agrito. 
Derivative: vinegar-y, adj. 
vinegaroon, n., a whip scorpion of Mexico (Mas- 
tigoproctus giganteus). — Fr. Sp. vinagre, ‘vine- 
gar’ (see prec. word); so called from the odor 
it emits when frightened, 
wine, n. — ME. win , fr. OE. win , fr. L. vinvm , 
‘wine’, whence also OS., OFris., OHG., MHG. 
win, ON. vin, Dan., Swed. vin, Du. wijn, ‘wine’, 
G. Wein, Goth, wein, OSIav. vino, Lith. vpnas, 
W. gwin, Olr. fin. See vine. 

Derivatives: wine, tr. and intr. v., wine-less , adj., 
win-er, n., win-ery , n., win-y, adj. 
winebibber, n., a drunkard. — Loan translation 
of G. Weinsdufer, which is compounded of wein , 
‘wine 7 , and Sdufer, ‘bibber’. See wine and bibber,
```


## [2026-10-17T00:02:10.843Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -w 'vin\\|win\\|wīn\\|vīn' HRN.txt HUB.txt | head; grep -n -a -w 'wyn\\|wīn\\|vīn' PHD.txt NYB_vol2_glossary.txt | head; grep -n 'وین' incoming/ARY/ARY_pages.txt | head -5; grep -n -i 'WIN\\b\\|VIN\\b' incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-10-17T00:02:11.322Z] TOOL RESULT

```
HRN.txt:12011:</^^m vin, 6ia
PHD.txt:99:didan, wën- [HZYTWN-tn' < A Угу; dytn', wyn- | M dydn, wyn-, N =, bin-] see. 7-ASn : sight, seeing. ««išnīģ : visible.
PHD.txt:102:(7) wes dytn! spells the infinitive didan, and (4) -p1 wyn- the present stem wén-.
PHD.txt:103:In Manichaean Middle Persian the corresponding forms are spelt dydn, wyn- respectively, indicating the same pronunciation. In New Persian the infinitive is still didan, but the present stem has become, regularly, bin-.
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD.txt:653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
NYB_vol2_glossary.txt:440:„a thousand times as much as... 10072; ~-susr cand having as much sperm [a bahuvrihi-compound] as 41?! (cf MPrs ’wyn’m ‘of such, or that, name, fame, Sogd. 214-22). - MPrs "nd; Paz. NP and. Probably a secondary formation from cand, q. v.
535:رو با زبانهاي یافثی اروپا خویشی دارند. این وضع ادامه داشت تا اینکه دیدمان فرگشت چارلز داروین
724:سده‌های نوین و زبان هند و اروپایی بنیادین محسوب می‌شوند. داش ما درباره فارسی کهن پیشتر ."
729:ترکی) ز همچنین بهواسطه‌ی تطور طبیعی زبان» زبان پهلوی تبدیل ه فارسی نوین شد. امروزه مد
749:آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
783:۰ میلیون نفر به آن سخن می‌گویند و زبان رسمی چندین کشور دیگر و زبان بین‌المللی جهان
354:Sp copy stall epbss] ga pb Ob; OT 3 Sey ELAM hh abwin i
518:sheyea Sobel gS pl gly s1 0 AB4 dle y2 (CHARLES DARWIN, 1809-1882)
647:JF Shae 3 showin 99 al Wj ois) 65 phy od 5 35 Sle
6161:‘MALLORY & ADAMS: JEvOS ‘OVIN, JEVIN (RUSSIAN) .o9,
6736:VIN gV¥e 1 gb dby XACANEM, (ARMENIAN) ,¢ |
```


## [2026-10-17T00:02:15.178Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for n in 6161 6736; do awk -v n=$n 'NR<=n && /pdf page/{p=$0} NR==n{print p}' ARY_latin_index_pages.txt; sed -n \"$((n-6)),$((n+4))p\" ARY_latin_index_pages.txt; echo ----; done; grep -n 'WOIN\\|WEIH\\|wine' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:02:15.512Z] TOOL RESULT

```
[pdf page 213]
JAU, JE (KURDISH) 52,5
‘REFERENCES ete 10, JAVA(BALUCHD sh
Poko S:S*~*~CS~*~“S*«*«OR yu | TOKHARIAN B) B 3,65
DELAMARRE: (CEREALE) 160 YAVA, YAVAS (SANSKRIT) cy Site
‘MACKENZIE: (BARLEY) 103 ZEIAL GREEK) gy
BUCK: 516 JECZMIEN POLISH) glo)
‘MALLORY & ADAMS: JEvOS ‘OVIN, JEVIN (RUSSIAN) .o9,
ow seb day JACHMEN (SLOVAK), $1 jlet
cetlool
waytg: OWI OSE F gba 4 alia! He hdl) Ha PU or!
Sa a REGS Rte rm a so
----
[pdf page 233]
Mey) E> coal s Aa sadly; ster 9 sale 9 DEH goa a gees edly Bean’
sdstan GLE" Sof] Gates MET E "ESE" UUs" slaajly 1
XAs, KANI-, KANN- :(AVESTAN) lcs!
‘REFERENCES [Oe a KANN- (OLD PERSIAN) slat go 5
Poko ==~*~*~*~S*S~«S SANSKRIT) «Saito
BUCK: 809 KHADATI, KHANATI, KHAD-
VIN gV¥e 1 gb dby XACANEM, (ARMENIAN) ,¢ |
xomos (GREEK) gli,
HAMUS A(LATIN) o3¥
KANDU (LITHUANIAN) gle}
lentlooh
----
```


## [2026-10-17T00:02:19.340Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -15; curl -s -L 'https://vajehyab.com/moein/%D9%88%DB%8C%D9%86' | python3 -c \"import sys,re,html;t=re.sub(r'<[^>]+>',' ',sys.stdin.read());t=html.unescape(t);i=t.find('انگور');print(t[max(0,i-600):i+400])\""
}
```


### [2026-10-17T00:02:20.227Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.

{
          const token = localStorage.getItem("vy_token");
          document.documentElement.setAttribute("data-authenticated", (!!token).toString());
        } catch (e) {}

        try {
          const user = JSON.parse(localStorage.getItem("vy_user") || "");
          document.documentElement.setAttribute("data-has-subscription", (!!user?.hasSubscription).toString());
        } catch (e) {}
      })();
     
     
     
     
     
     
     
     
     
     
     
     {"@context":"https://schema.org","@graph":[{"@type":"DefinedTerm","name":"وین","description":"(وَ) [ ع . ] (اِ.) 1 - انگور سیاه . 2 - عیب . 3 - در فارسی به معنای : رنگ ، لون .","url":"https://vajehyab.com/moein/%D9%88%DB%8C%D9%86","inDefinedTermSet":{"@type":"DefinedTermSet","name":"فرهنگ انتشارات معین"}}]} 
      window.__INITIAL_DATA__ = {"key":"/moein/%D9%88%DB%8C%D9%86","result":{"document":{"description":"(وَ) [ ع . ] (اِ.) 1 - انگور سیاه . 2 - عیب . 3 - در فارسی به معنای : رنگ ، لون .","dictionaryId":"5591
```


## [2026-10-17T00:02:27.705Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; N='page 555, root Woin/Win'; python3 tools/fetch_source.py 'https://vajehyab.com/moein/%D9%88%DB%8C%D9%86' --note \"$N: Mo'in s.v. vin - [Ar.] black grape; in Persian colour\" ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%88%DB%8C%D9%86' --note \"$N: Persian vin black grape borrowed from Arabic wayn\"; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9yh%E2%82%81%C5%8D' --note \"$N: PIE wine word, disputed origin, possibly Mediterranean, Semitic wayn\"; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Semitic/wayn-' --note \"$N: PWS *wayn- > Ar. wayn black grape > Pers. vin\"; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/vinum' --note \"$N: Latin vinum\"; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/vinea' --note \"$N: Latin vinea\"; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/vinegar' --note \"$N: vinegar < OF vinaigre < vin + aigre (L. acer)\"; python3 tools/fetch_source.py 'https://www.etymonline.com/word/wine' --note \"$N: wine < OE win < L. vinum\"; python3 tools/fetch_source.py 'https://www.etymonline.com/word/vinegar' --note \"$N: vinegar\"; python3 tools/fetch_source.py 'https://www.etymonline.com/word/vine' --note \"$N: vine < OF vigne < L. vinea\""
}
```


### [2026-10-17T00:02:31.018Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe-private/data/verification/sources/web/89e51ce1512ecbaf.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2d6912fc5119e69a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2edcf5b45cfd81d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/060efd28b42e9e36.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6896e5ca51aae06d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e80a4909237d2230.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fa0be8d73ad64d58.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/91bb34ec83377833.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/81bae94ad15b6157.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/17136d40e4558bdc.txt
```


## [2026-10-17T00:02:33.109Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 91bb34ec83377833 81bae94ad15b6157 17136d40e4558bdc; do echo == $f; grep -i -m3 'vinum\\|vinaigre\\|vigne' $f.txt | cut -c1-400; done; tail -3 index.jsonl | cut -c1-200"
}
```


### [2026-10-17T00:02:33.451Z] TOOL RESULT

```
Exit code 1
(eval):1: = not found
```


## [2026-10-17T00:02:35.587Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 91bb34ec83377833 81bae94ad15b6157 17136d40e4558bdc; do echo \"-- $f\"; grep -i -m3 'vinum\\|vinaigre\\|vigne' $f.txt | cut -c1-400; done; tail -3 index.jsonl | cut -c1-250"
}
```


### [2026-10-17T00:02:36.009Z] TOOL RESULT

```
-- 91bb34ec83377833
-- 81bae94ad15b6157
-- 17136d40e4558bdc
{"url": "https://en.wiktionary.org/wiki/Venice", "file": "data/verification/sources/web/4f08c3db5c8bd565.txt", "fetched": "2026-10-17T00:02:34Z", "status": 200, "bytes": 14655, "title": "Venice - Wiktionary, the free dictionary", "note": "page 543, r
{"url": "https://en.wiktionary.org/wiki/venereal", "file": "data/verification/sources/web/d633287e4b6e46c3.txt", "fetched": "2026-10-17T00:02:34Z", "status": 200, "bytes": 13015, "title": "venereal - Wiktionary, the free dictionary", "note": "page 54
{"url": "https://en.wiktionary.org/wiki/venery", "file": "data/verification/sources/web/6d1a7deddcaaefe2.txt", "fetched": "2026-10-17T00:02:34Z", "status": 200, "bytes": 5727, "title": "venery - Wiktionary, the free dictionary", "note": "page 543, ro
```


## [2026-10-17T00:02:38.949Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -c 'page 555' index.jsonl; grep 'etymonline.com/word/wine\"\\|etymonline.com/word/vine\"\\|word/vinegar\"' index.jsonl | cut -c1-300; wc -c 91bb34ec83377833.txt 81bae94ad15b6157.txt 17136d40e4558bdc.txt; head -c 600 91bb34ec83377833.txt"
}
```


### [2026-10-17T00:02:39.243Z] TOOL RESULT

```
10
{"url": "https://www.etymonline.com/word/vinegar", "file": "data/verification/sources/web/81bae94ad15b6157.txt", "fetched": "2026-09-04T19:16:06Z", "status": 200, "bytes": 6392, "title": "Vinegar - Etymology, Origin & Meaning", "note": "pdf page 42, root Ak/Aq/Aken: English/French/Persian reflexes (
{"url": "https://www.etymonline.com/word/wine", "file": "data/verification/sources/web/91bb34ec83377833.txt", "fetched": "2026-10-17T00:02:30Z", "status": -1, "bytes": 39, "title": "", "note": "page 555, root Woin/Win: wine < OE win < L. vinum"}
{"url": "https://www.etymonline.com/word/vinegar", "file": "data/verification/sources/web/81bae94ad15b6157.txt", "fetched": "2026-10-17T00:02:30Z", "status": -1, "bytes": 39, "title": "", "note": "page 555, root Woin/Win: vinegar"}
{"url": "https://www.etymonline.com/word/vine", "file": "data/verification/sources/web/17136d40e4558bdc.txt", "fetched": "2026-10-17T00:02:30Z", "status": -1, "bytes": 39, "title": "", "note": "page 555, root Woin/Win: vine < OF vigne < L. vinea"}
131 91bb34ec83377833.txt
134 81bae94ad15b6157.txt
131 17136d40e4558bdc.txt
396 total
URL: https://www.etymonline.com/word/wine
FETCHED: 2026-10-17T00:02:30Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-17T00:02:42.495Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/wine' --note \"page 555, root Woin/Win: wine < OE win < Proto-West Germanic *wīn < L. vinum\"; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/vine' --note \"page 555, root Woin/Win: vine < OF vigne < L. vinea\"; grep 'page 555' data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['status'],d['bytes'],d['url'])\""
}
```


### [2026-10-17T00:02:43.709Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d041281230574eba.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/43335313f56d0deb.txt
200 365 https://vajehyab.com/moein/%D9%88%DB%8C%D9%86
200 2961 https://en.wiktionary.org/wiki/%D9%88%DB%8C%D9%86
200 10063 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9yh%E2%82%81%C5%8D
200 4943 https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Semitic/wayn-
200 7617 https://en.wiktionary.org/wiki/vinum
200 5065 https://en.wiktionary.org/wiki/vinea
200 22704 https://en.wiktionary.org/wiki/vinegar
-1 39 https://www.etymonline.com/word/wine
-1 39 https://www.etymonline.com/word/vinegar
-1 39 https://www.etymonline.com/word/vine
200 45913 https://en.wiktionary.org/wiki/wine
200 22982 https://en.wiktionary.org/wiki/vine
```


## [2026-10-17T00:02:46.047Z] TOOL CALL #32: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/sources/web/89e51ce1512ecbaf.txt; grep -n 'page_offset\\|AHD' /dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'));print(d['AHD'].get('page_offset'), d['AHD'].get('lookup_hint'))\""
}
```


### [2026-10-17T00:02:46.423Z] TOOL RESULT

```
URL: https://vajehyab.com/moein/%D9%88%DB%8C%D9%86
FETCHED: 2026-10-17T00:02:28Z
STATUS: 200
TITLE: معنی وین | فرهنگ انتشارات معین | واژه یاب

معنی وین | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 وین

 فرهنگ انتشارات معین
 (وَ) [ ع . ] (اِ.) 1 - انگور سیاه . 2 - عیب . 3 - در فارسی به معنای : رنگ ، لون .
 وین در فرهنگ‌های دیگر
 معنی وین در لغت‌نامه دهخدا 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
```


## [2026-10-17T00:03:01.999Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=20853 && /pdf page/{p=$0} NR==20853{print p}' incoming/WLD/WLD_Bd1_pages.txt; awk 'NR>20700 && NR<20853' incoming/WLD/WLD_Bd1_pages.txt | grep -n '^ *[0-9][0-9][0-9] *$\\|  2[0-9][0-9]  ' | tail -3; grep -n -a 'Wine\\b' SKT.txt | head -3; grep -n -a -i '^Wine\\|^Vine' SKT.txt | head"
}
```


### [2026-10-17T00:03:02.396Z] TOOL RESULT

```
20895:Vi|a:nette :  see  Wine.
20912:Vine.  Vinegar  ;  fee  Wine,
20914:Vintage,  Vintner ;  sec  Wine.
20912:Vine.  Vinegar  ;  fee  Wine,
21912:Wine.  Some  think  that  Gk.  o7vot  ta not  of  Aryan  origin;  cf.  Heb  yajrim,  winei Ethiopic  tttfioi,  tuamg  wine.
```


## [2026-10-17T00:03:04.814Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 300 incoming/WLD/WLD_Bd1_pages.txt; echo; awk 'BEGIN{RS=\"\\f\"} /olvog „Wein/{print NR; print substr($0,1,200)}' incoming/WLD/WLD_Bd1_pages.txt; grep -n -a -i 'Wine, sb\\|^WINE\\|wine,' SKT.txt | head -5"
}
```


### [2026-10-17T00:03:05.152Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D.G.A. 79
                      ALOIS WALDE


VERGLEICHENDES WftRTERBDCH
                         
235
226                                                 uei-



wohl ags. icine-winda „Uferschnecke“, wining „Binde“.                       —
                                                              
2728:kennel  ( j),  a  gutter.  (F. »  L) tion  of  M.  E.  fa«^/.  a  channel :  i Canary,    a     bird,     a    wine,    • (Canary   Islands.)      All   named Canary  i&Iaods. Cancel;  see  Cancftr. Cancer,  (L)    L  %anfe^,  a  crib;  «h». 'eating*  tumour.  +  t'k.  xv^wdroc,  Shi. ka\ay  a  ciab ;  cf.  Skt.  hixrketn^t  hanL  N from  its  hard  shell.
3061:Cask.  (Span.-L.)    Span,  to^..-^  a sherd,  coat  of  an  onion :  also  1 wine,  a  casque  or  helmet.     The is    '  htisk ;'    cf.  Span,   rdxfrtna,    |^ shell,  Port   casca,  rind.  — Sjian. burst  open  ;  formed  (as  if  from  ' cart  *)  from  an  extension  of  I* to  break,  bunt  ;  see  Quaih.
15513:Rack  (3).  to  pour  off  liquor,  to  clear  it from  drc^  or  lees.  (F.  — L.  ?)  MinUicu (iftJ7)  s]xaks  of  ' ra^kt  wines.'  — F.  riupu\ whence  vin  raqtuK  'small,  or  cor^e  wine, squeezed  from  the  drcj^s  of  the  grapes, already  drained  of  all  their  best  moisture;  * Cot.  Cf.  Span.  tascoHt  sour;  raaar,  to scmpe.     Prob.  of  L.  origin  ;  see  RaAoal.
17104:iytitp.  —  Span,  xaropt,  a.  drink.  —  At skardb,  shurdb,  wine,  beverage,  syruj] Arab,  root  skariba  (above).
17915:swine,  a  sow.  pig,  pigs.  (E.)  M.  E swin,  both  sing,  and  pV  A-  S.  swin,  a pig;  pi,  stt/in,  swine.  +  Du.  iwij'h,  a swine,  hug;  Iccl.  jr/»,  pi.  tvin,  Dan. sviin,  pi.  sviiH,  Swed.  jvim,  G.  sckuftM, O.  H.  G.  rufin ;  Goth,  sweitt,  neut.  sb. sini;.  So  also  Kuss.  svintya,  a  swine, jvinka,  a  pig,  sinfuHt  swinish.  All  orig. ad]ccti\*al  fonns,  like  L,  suinus  (Varto), related  to  swine,  formed  from  i«i-,  crude form  of  ius,  a  sow.
```


## [2026-10-17T00:04:14.507Z] TOOL CALL #35: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build555.py <<'EOF'\nimport json\nWK = \"https://en.wiktionary.org/wiki/\"\nPIE = WK + \"Reconstruction:Proto-Indo-European/w%C3%A9yh%E2%82%81%C5%8D\"\nPWS = WK + \"Reconstruction:Proto-West_Semitic/wayn-\"\nFA = WK + \"%D9%88%DB%8C%D9%86\"\nMON = \"https://vajehyab.com/moein/%D9%88%DB%8C%D9%86\"\nVINUM = WK + \"vinum\"; VINEA = WK + \"vinea\"; VINEGAR = WK + \"vinegar\"; WINE = WK + \"wine\"; VINE = WK + \"vine\"\n\npok = {\"src\": \"POK\", \"where\": \"p. 1120-1121 s.v. u̯ei-1 (POK_full.txt l. 89648 ff.)\", \"stance\": \"partial\",\n       \"note\": \"'barely here the name of Weins: gr. oinos (myk. vo-no-) wine, oinē grapevine ... Armenian gini (*u̯oi-ni̯om), alb. vene, Tosc vere (*u̯oinā), Latin vīnum ... da the Pontus the originator of the Weinkultur war, handelt es sich wohl um ein vorderasiat. Wort; compare Proto Semitic *wainu (arab. äthiop. wain, hebr. jajin, assyr. īnu) and Hittite wijana-' — Pokorny lists the word only tentatively under u̯ei- and calls it a Near-Eastern culture word.\"}\nwld = {\"src\": \"WLD\", \"where\": \"Bd. I p. 226 s.v. u̯ei- (WLD_Bd1_pages.txt l. 20853)\", \"stance\": \"partial\",\n       \"note\": \"'wohl der Name des Weins: gr. oinos „Wein“, oinē „Weinstock“ ... arm. gini „Wein“ (*u̯oinio-), alb. vere „Wein“ (*u̯oina), lat. vīnum, letztere ist nicht bloß die Quelle von air. fīn...' — same tentative attachment to u̯ei- 'twist'.\"}\nsyn = {\"src\": \"SYN\", \"where\": \"5.92 WINE, p. 390\", \"stance\": \"supports\",\n       \"note\": \"'Grk. oinos, early woinos, Lat. vīnum (prob. fr. *woinom ...), Alb. venë, Arm. gini, together with the Semitic words, Arab. wain, Hebr. yayin, all prob. loanwords fr. some prehistoric Mediterranean source. So Meillet ... But even so, the source could be some IE language of that region ... Lat. vīnum is the source of all the other Eur. words, except the Greek and Albanian.' Also: 'In ancient India and Iran wine was not one of the common alcoholic drinks' (no Iranian reflex listed; Av. madu-, NP mai).\"}\nkln_vine = {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. vine (KLN_1971.txt l. 262297-262319)\", \"stance\": \"supports\",\n            \"note\": \"'vine, n. — ME., fr. OF. (F. vigne), fr. L. vinea, vineyard ... prop. fem. of vineus, pertaining to wine, used as a noun, fr. vinum, wine ... Cp. oinē ... Alb. vene, Arm. gini, Georgian ɣvino ... Heb. yáyin (prob. for *wáyin), Ugar. yn, Ethiop. wayn, grape, wine, Akkad. inu ... The ult. origin of these words is unknown.'\"}\niec = {\"src\": \"IEC\", \"where\": \"grep 'woin', 'vinum' in IEC.txt\", \"stance\": \"silent\", \"note\": \"no entry for the wine word found in Mann's OCR text.\"}\nskt_wine = {\"src\": \"SKT\", \"where\": \"s.v. Wine (SKT.txt l. 21912; 'Vine. Vinegar; see Wine' l. 20912)\", \"stance\": \"supports\",\n            \"note\": \"'Wine. Some think that Gk. oinos is not of Aryan origin; cf. Heb. yayin, wine; Ethiopic wayn, wine' — Skeat files vine and vinegar under wine.\"}\n\nroot_rc = [\n {\"ref\": \"AHD:1547\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt l. 1110), the revised text of the 1976 appendix entry: '[vinum. Wine. Latin noun, related to Greek oinos, wine. Probably from a Mediterranean word *win-, *woin- meaning “wine.” 1. Latin vinum: VINACEOUS, VINE, VINI-, WINE; VINEGAR. 2. Greek oinos (earlier woinos)...]' — exactly Nourai's root form and his 'probably a Mediterranean word' note (AHD gives no Persian reflex).\"},\n {\"ref\": \"ROE:265\", \"status\": \"not_checked\", \"note\": \"Claiborne, Roots of English — lending-only on archive.org, no text accessible.\"}\n]\n\nnodes = [\n {\"id\": 1, \"lang\": \"Persian\", \"words\": \"vîn\", \"verdict\": \"disputed\",\n  \"derivation\": \"Persian وین vin/vayn 'black grape' (Borhan: 'rang o lun ... va angur-e siyah') is not an inherited Iranian reflex of the IE wine word: no Old or Middle Iranian *wain-/wīn 'wine' exists (MacKenzie and Nyberg have none; Iranian uses Av. madu-, MP may, NP mey), and Mo'in marks the word '(vay) [Ar.]' — it is a loan from Arabic وَيْن wayn 'black grape' (rare), which continues Proto-West Semitic *wayn- 'wine' (Heb. yayin, Ge'ez wäyn). That Semitic word and PIE *wóyh₁nom are related only as parallel borrowings of one Mediterranean/Near-Eastern culture word (or one borrowed from the other), so the arrow PIE → Persian should run Mediterranean word → Semitic *wayn- → Ar. wayn → Pers. vin. Nourai's sources FVF and AFM treat Arabic wayn as a Persian loan (the reverse direction), but Addi Shir himself hedges with 'or it is a coincidence of languages'. The other senses on the chart are unrelated homonyms: 'colour' is the native Persian vin (Borhan, Mo'in 'in Persian: colour'), and 'world' is only Noushin's conjectural reading 'bar in vin-e xorram' in a Shahnameh verse where other MSS read din/deyr.\",\n  \"derivation_fa\": \"«وین» (vayn/vin) به معنی «انگور سیاه» در فارسی بازماندهٔ ایرانی باستان نیست: در اوستایی، پارسی باستان و فارسی میانه هیچ واژهٔ *wain-/wīn برای «می» دیده نمی‌شود (مکنزی و نیبرگ چنین واژه‌ای ندارند و ایرانی برای «شراب» madu-/may/می دارد). معین آن را با نشانهٔ [ع.] آورده است: وام‌واژه‌ای است از عربی «وَیْن» «انگور سیاه» که خود از سامی غربی آغازین *wayn- «شراب» (عبری yayin) است؛ این واژهٔ سامی و هندواروپایی *wóyh₁nom تنها هم‌خانوادهٔ یک واژهٔ فرهنگی مدیترانه‌ای/خاور نزدیکی‌اند، نه هم‌ریشهٔ موروثی. پس پیکان مستقیم از ریشهٔ هندواروپایی به «وین» فارسی را پژوهش امروزی نمی‌پذیرد و راه درست «واژهٔ مدیترانه‌ای ← سامی ← عربی ← فارسی» است. معنای «رنگ» واژه‌ای جدا و فارسی است و معنای «جهان» تنها خوانش پیشنهادی نوشین در بیتی از شاهنامه است که در دستنویس‌های دیگر «دین/دیر» آمده است.\",\n  \"sources\": [FA, PWS, MON, PIE],\n  \"ref_check\": [\n   {\"ref\": \"BQT:2302\", \"status\": \"partial\", \"note\": \"Read from the page image (ocr/BQT/2302.png, saved as 2302.vision.txt): 'وین - بروزن سین، بمعنی رنگ و لون باشد عموماً ۴ - و انگور سیاه را گویند خصوصاً.' Footnote 4 only 'رک: جهانگیری' — the word and both senses are there, but Mo'in gives no etymology and no link to wine.\"},\n   {\"ref\": \"AFM:159\", \"status\": \"partial\", \"note\": \"Addi Shir (AFM_pages.txt l. 4064-4070, just after printed p. 153 marker; OCR garbled): '(الوَيْن) العنب الاسود ... او هو من توافق اللغات ... يعني الكرمة والشراب ... باليونانية ... بالرومية ... بالانكليزية ...' — lists Arabic wayn 'black grape' as possibly Persian, or else a concordance with Greek oinos, Latin vinum, English wine, Aramaic. Supports the wine connection, but as Arabic wayn, and hedged.\"},\n   {\"ref\": \"FSF:341\", \"status\": \"partial\", \"note\": \"Noushin's Vazhe-namak, this scan p. ~459-460 (FSF_pages.txt l. 22520-22575; not p. 341 — different printing): headword 'وین' with the verse 'اگر زندگانی بود دیرباز / برین وین خرم بمانم دراز'; Noushin says the London MS has 'وین', Cairo 'دین' ('بی‌گمان مصحف وین'), Leningrad 'بدین دیر خرم', and since deyr 'world' is not Shahnameh usage he put 'وین' into the Moscow text in the sense 'world, earth'. Source of Nourai's '(world ?)'; no etymology given.\"},\n   {\"ref\": \"FVF:695\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari — PDF only behind login/JS (noorlib/ketabnak), not accessible here.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/moein s.v. وین\", \"stance\": \"contradicts\", \"note\": \"'(وَ) [ ع . ] (اِ.) 1 - انگور سیاه . 2 - عیب . 3 - در فارسی به معنای : رنگ ، لون .' — Mo'in marks the 'black grape' word as Arabic, and only 'colour' as Persian.\"},\n   {\"src\": \"PHD\", \"where\": \"grep wyn/wīn in PHD.txt\", \"stance\": \"silent\", \"note\": \"no Pahlavi wīn/wayn 'wine, grape'; only 'win [wn'] vina, lute' (unrelated) and wēn- 'see'.\"},\n   {\"src\": \"NYB\", \"where\": \"grep wyn/wīn in NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"no Pahlavi 'wine/grape' word of this shape.\"},\n   {\"src\": \"HRN\", \"where\": \"grep vin/wīn in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn has no entry vīn 'grape' (single OCR hit l. 12011 is noise).\"},\n   {\"src\": \"HUB\", \"where\": \"grep vin/wīn in HUB.txt\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n   {\"src\": \"ARY\", \"where\": \"grep وین / WIN in ARY_pages.txt and ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur has no IE-root entry for وین.\"},\n   {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. vine\", \"stance\": \"partial\", \"note\": \"'Heb. yáyin (prob. for *wáyin), Ugar. yn, Ethiop. wayn, grape, wine ... The ult. origin of these words is unknown' — puts the Semitic wayn beside the IE word, as a parallel, not as Iranian.\"},\n   {\"src\": \"SYN\", \"where\": \"5.92 p. 390\", \"stance\": \"partial\", \"note\": \"'Arab. wain, Hebr. yayin, all prob. loanwords fr. some prehistoric Mediterranean source'; 'In ancient India and Iran wine was not one of the common alcoholic drinks' — no Iranian reflex.\"}\n  ]},\n {\"id\": 2, \"lang\": \"Latin\", \"words\": \"vînum; vînum-acer; vinea\", \"verdict\": \"plausible\",\n  \"derivation\": \"Latin vīnum 'wine' < Proto-Italic *wīnom < *woinom (Latin regularly turns oi > ū/ī; the ī here as in vīcus beside Gk. woikos), cognate with Gk. (w)oinos, Arm. gini, Alb. verë, Hitt. wiyana-; confirmed. vīnea 'vineyard, vine' is the feminine of the adjective vīneus 'of wine' used as a noun; confirmed. 'vīnum-acer' is not an attested Latin compound (and the neuter would be vīnum ācre): 'vinegar' was formed in Old French as vin aigre 'sour wine', from vīnum + ācer/ācrem 'sharp' (PIE *h₂eḱ-); the components are right, the Latin compound is Nourai's shorthand — hence plausible for that word.\",\n  \"derivation_fa\": \"لاتین vīnum «شراب» از ایتالیک آغازین *wīnom و آن از *woinom است (oi در لاتین به ī بدل شده) و هم‌ریشه با یونانی oinos (کهن‌تر woinos)، ارمنی gini و آلبانیایی verë؛ این درست است. vīnea «تاکستان، تاک» مؤنثِ صفت vīneus «شرابی» است که اسم شده؛ این هم درست است. اما «vīnum-acer» ترکیب لاتینی ثبت‌شده‌ای نیست؛ «سرکه» (vinegar) در فرانسوی کهن به صورت vin aigre «شراب ترش» از vīnum و ācer «تیز، ترش» ساخته شده است. پس اجزا درست‌اند ولی این صورت لاتین ساختهٔ نورایی است و با احتیاط پذیرفتنی است.\",\n  \"sources\": [VINUM, VINEA, VINEGAR, PIE],\n  \"ref_check\": [\n   {\"ref\": \"AHD:1547\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. vinum: '1. Latin vinum: VINACEOUS, VINE, VINI-, WINE; VINEGAR.' — Latin vinum with vine and vinegar as derivatives, as charted.\"}\n  ],\n  \"consulted\": [kln_vine,\n   {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. vinegar (l. 262323)\", \"stance\": \"partial\", \"note\": \"'vinegar, n. — ME. vinegre, fr. OF. (= F.) vinaigre, compounded of vin aigre, sour wine' — the compound is Old French, not Latin.\"},\n   wld, syn, pok]},\n {\"id\": 3, \"lang\": \"English\", \"words\": \"wine, vinegar, vine\", \"verdict\": \"confirmed\",\n  \"derivation\": \"wine: OE wīn, from Proto-West Germanic *wīn, an early (pre-5th-c.) Germanic borrowing of Latin vīnum (Goth. wein, OHG wīn); vine: ME vine < Old French vigne/vine < Latin vīnea 'vineyard'; vinegar: ME vinegre (13th-14th c.) < Old French vinaigre = vin 'wine' + aigre 'sour' (< Latin ācrem). All three go back to Latin vīnum as drawn.\",\n  \"derivation_fa\": \"انگلیسی wine از انگلیسی باستان wīn است که ژرمنی‌ها در روزگار رومیان از لاتین vīnum وام گرفتند (گوتی wein، آلمانی Wein)؛ vine «تاک» از فرانسوی کهن vigne از لاتین vīnea آمده؛ vinegar «سرکه» از فرانسوی کهن vinaigre یعنی vin «شراب» + aigre «ترش» (از لاتین ācer). هر سه از لاتین vīnum می‌آیند و ادعای نورایی درست است.\",\n  \"sources\": [WINE, VINE, VINEGAR],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. vinum lists 'VINE, ... WINE; VINEGAR' as English derivatives of Latin vinum.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. wine (l. 267456), vine (l. 262297), vinegar (l. 262323)\", \"stance\": \"supports\", \"note\": \"'wine, n. — ME. win, fr. OE. win, fr. L. vinum'; 'vine, n. — ME., fr. OF. (F. vigne), fr. L. vinea'; 'vinegar, n. — ME. vinegre, fr. OF. vinaigre, compounded of vin aigre, sour wine'.\"},\n   skt_wine,\n   {\"src\": \"SYN\", \"where\": \"5.92 p. 389-390\", \"stance\": \"supports\", \"note\": \"table 'OE win, ME wine, NE wine ... Goth. wein' and 'Lat. vīnum is the source of all the other Eur. words, except the Greek and Albanian'.\"}\n  ]}\n]\n\nentry = {\"entry\": 1, \"root\": \"Woin, Win\", \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *wóyh₁nom / *wéyh₁ō 'wine, vine' (Wiktionary); Watkins: non-IE Mediterranean *win-, *woin-\",\n \"note\": \"The wine word (Gk. woinos, Lat. vīnum, Arm. gini, Alb. verë, Hitt. wiyana-) is real and Nourai's root form and gloss match AHD (Watkins files it under 'vinum ... probably from a Mediterranean word *win-, *woin-'), and his chart note 'probably a Mediterranean word' is the majority view (Meillet, Buck, Watkins; Pokorny 1120f. 'wohl ein vorderasiatisches Wort'); a minority derives it from PIE *weh₁y- 'twist' (vītis 'vine'; Beekes, de Vaan). Hence 'plausible' rather than a secure PIE root. The Semitic *wayn- (Ar. wayn, Heb. yayin) is a parallel borrowing of the same culture word, and that is the real source of the Persian node (via Arabic), not Iranian inheritance.\",\n \"note_fa\": \"واژهٔ «شراب» در یونانی woinos، لاتین vīnum، ارمنی gini، آلبانیایی verë و هیتی wiyana- واقعی است و صورت و معنای ریشه در نمودار نورایی با واتکینز (AHD) می‌خواند؛ واتکینز آن را زیر vinum آورده و «احتمالاً از واژه‌ای مدیترانه‌ای *win-, *woin-» می‌داند، و پوکورنی هم آن را «احتمالاً واژه‌ای از آسیای نزدیک» می‌خواند. پس یادداشت نورایی («احتمالاً واژه‌ای مدیترانه‌ای») با دیدگاه بیشتر پژوهشگران سازگار است، اما ریشهٔ هندواروپایی استواری نیست و برخی آن را از *weh₁y- «پیچیدن» (هم‌ریشه با vītis «تاک») می‌گیرند؛ از این رو با احتیاط پذیرفتنی است. صورت سامی *wayn- (عربی وَیْن، عبری yayin) وام‌گیری موازی همین واژهٔ فرهنگی است و «وین» فارسی از همین راه عربی آمده، نه از میراث ایرانی.\",\n \"sources\": [PIE, PWS, VINUM],\n \"ref_check\": root_rc,\n \"consulted\": [pok, wld, syn, kln_vine, iec,\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. vinum (AHD_watkins1985.txt l. 1110)\", \"stance\": \"supports\", \"note\": \"'Probably from a Mediterranean word *win-, *woin- meaning “wine.”'\"}],\n \"nodes\": nodes}\n\nout = {\"pdf_page\": 555, \"book_page\": 525, \"verified_by\": \"claude-opus-5-5\", \"verified_on\": \"2026-10-16\", \"entries\": [entry]}\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-555.json\", \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build555.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-555.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 555"
}
```


### [2026-10-17T00:04:15.078Z] TOOL RESULT

```
nodes verified: 3/3
node verdicts: {'disputed': 1, 'plausible': 1, 'confirmed': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 3, 'not_checked': 1, 'supports': 2}
books consulted: {'contradicts': 1, 'silent': 5, 'partial': 5, 'supports': 5} | by book: {'KLN': 4, 'SYN': 3, 'MON': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1, 'WLD': 1, 'POK': 1, 'SKT': 1}
```


## [2026-10-17T00:04:24.133Z] TOOL CALL #36: SubagentHandback

```json
{
 "message": "Page 555 (book page 525) is verified. I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-555.json`, and `verify_check.py 555` reports 0 PROBLEM lines.\n\nThe page has one real chart, Woin/Win \"wine\". The other 9 charts are redirects and were skipped.\n\n**Verdicts:** root 1 plausible; nodes 1 confirmed, 1 plausible, 1 disputed (3/3 verified).\n\n- **Root (plausible):** *woin-/*win- \"wine\" matches AHD. Watkins files it under vinum as \"probably from a Mediterranean word *win-, *woin-\". Pokorny (p. 1120f.) and Buck (5.92) also call it a Near-Eastern/Mediterranean culture word. That agrees with Nourai's own note, but it is not a secure PIE root.\n- **Disputed: Persian vîn «وین» \"black grape\".** It is not inherited from the IE root. Mo'in marks it [ع.], and Wiktionary agrees: it is a loan from Arabic wayn \"black grape\", from Proto-West Semitic *wayn-. That Semitic word is only a parallel borrowing of the same culture word. No Old or Middle Iranian *wain- exists; MacKenzie and Nyberg have nothing, and Horn, Hübschmann and Aryanpur are silent. The other senses on the chart are separate words:\n  - \"colour\" is a native Persian homonym.\n  - \"world ?\" comes only from Noushin's conjectural reading «وین» in a Shahnameh verse where other manuscripts read دین/دیر.\n- **Plausible: Latin node.** vînum and vinea are fine. \"vînum-acer\" is not an attested Latin compound: vinegar was formed in Old French as vin aigre.\n- **Confirmed: English** wine, vine, vinegar.\n\n**Nourai's own references:**\n- AHD:1547 supports.\n- BQT:2302, AFM:159 and FSF:341 are partial: each has the word but no derivation from the root. Addi Shir hedges between a Persian origin and a cross-language coincidence.\n- In the FSF scan the entry is on about p. 459–460, not p. 341, so that copy is a different printing.\n- FVF and ROE could not be reached and are marked not_checked.\n\nI saved my reading of the Borhan page to `data/verification/sources/refs/ocr/BQT/2302.vision.txt`. The Etymonline fetches returned 403 and are not cited.\n\nNo transcription_suspect items, and no extraction errors (the JSON matches the chart)."
}
```


### [2026-10-17T00:04:24.509Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
