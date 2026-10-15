# Verification process log — verify-page-515


## [2026-10-15T02:44:16.647Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 515 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-515.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-515.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-515.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 515` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.737Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.358Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.379Z] TOOL RESULT

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


## [2026-10-15T02:44:19.877Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-515.txt"
}
```


### [2026-10-15T02:44:19.976Z] TOOL RESULT

```
1	=== PDF page 515 (book page 485) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Twerk, Twrk : to cut  (refs POK:1102)
4	#1 (parent #0) [Avestan] refs=POK:1102 | thwares : to cut
5	#2 (parent #0) [Sanskrit] refs=POK:1102 | tvâsta, tvastar : cut
6	#3 (parent #0) [Greek] refs=POK:1102; KLN:1383 | sarkh, sarx : a cut of meat, flesh ; sarca-sein : to tear flesh like dogs, to speak bitterly ; sarcasmos : bitter talk, mockery
7	  #4 (parent #3) [Latin] refs=KLN:1383 | sarcasmos
8	    #5 (parent #4) [French] refs=KLN:1383 | sarcasme
9	      #6 (parent #5) [English] refs=KLN:1383 | sarco- : flesh ; sarcology, sarcoma, sarcasm, sarcastic
10	--- entry 1 ---
11	ROOT Twrk -> redirect to Twerk
12	
```


## [2026-10-15T02:44:20.679Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-515.json"
}
```


### [2026-10-15T02:44:20.711Z] TOOL RESULT

```
1	{
2	  "pdf_page": 515,
3	  "book_page": 485,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Twerk, Twrk",
8	        "lang": "Indo-European",
9	        "refs": "POK:1102",
10	        "gloss": "to cut"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1102",
18	          "words": [
19	            {"translit": "thwares", "gloss": "to cut", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 0,
27	          "lang": "Sanskrit",
28	          "refs": "POK:1102",
29	          "words": [
30	            {"translit": "tvâsta, tvastar", "gloss": "cut", "script": null}
31	          ],
32	          "note": null,
33	          "quote": null
34	        },
35	        {
36	          "id": 3,
37	          "parent": 0,
38	          "lang": "Greek",
39	          "refs": "POK:1102; KLN:1383",
40	          "words": [
41	            {"translit": "sarkh, sarx", "gloss": "a cut of meat, flesh", "script": null},
42	            {"translit": "sarca-sein", "gloss": "to tear flesh like dogs, to speak bitterly", "script": null},
43	            {"translit": "sarcasmos", "gloss": "bitter talk, mockery", "script": null}
44	          ],
45	          "note": null,
46	          "quote": null
47	        },
48	        {
49	          "id": 4,
50	          "parent": 3,
51	          "lang": "Latin",
52	          "refs": "KLN:1383",
53	          "words": [
54	            {"translit": "sarcasmos", "gloss": null, "script": null}
55	          ],
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 5,
61	          "parent": 4,
62	          "lang": "French",
63	          "refs": "KLN:1383",
64	          "words": [
65	            {"translit": "sarcasme", "gloss": null, "script": null}
66	          ],
67	          "note": null,
68	          "quote": null
69	        },
70	        {
71	          "id": 6,
72	          "parent": 5,
73	          "lang": "English",
74	          "refs": "KLN:1383",
75	          "words": [
76	            {"translit": "sarco-", "gloss": "flesh", "script": null},
77	            {"translit": "sarcology, sarcoma, sarcasm, sarcastic", "gloss": null, "script": null}
78	          ],
79	          "note": null,
80	          "quote": null
81	        }
82	      ]
83	    },
84	    {
85	      "root": {
86	        "name": "Twrk",
87	        "redirect": "Twerk"
88	      },
89	      "nodes": []
90	    }
91	  ]
92	}
93	
```


## [2026-10-15T02:44:26.904Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','WLD','AHD','IEC','SYN','BRT','KNT','SKT','FSD','WEB']:\n  print(k,d.get(k))\"; ls data/verification/sources/refs/ | head -100"
}
```


### [2026-10-15T02:44:27.936Z] TOOL RESULT

```
<persisted-output>
Output too large (29.5KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/brsn50qc8.txt

Preview (first 2KB):
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
...
</persisted-output>
```


## [2026-10-15T02:44:29.902Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/brsn50qc8.txt | grep -E '^\\- \\*\\*|^  `|^##' | head -120"
}
```


### [2026-10-15T02:44:30.426Z] TOOL RESULT

```
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


## [2026-10-15T02:44:31.685Z] AGENT

Now grep the local books.


## [2026-10-15T02:44:33.351Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['POK','KLN','WLD','AHD','BRT']:\n  v=d.get(k,{}); print(k,v.get('page_offset'),v.get('local_file'),v.get('lookup_hint'))\"\ngrep -n -i 'tu̯er(e)k\\|tuer(e)k\\|tu̯erk\\|θwarəs\\|twars' POK_full.txt | head -20"
}
```


### [2026-10-15T02:44:33.850Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
```


## [2026-10-15T02:44:35.483Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Page(s): 1102' POK_full.txt | head; grep -n -i 'lemma: tu.er' POK_full.txt | head -30"
}
```


### [2026-10-15T02:44:35.873Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:44:37.670Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '1102' POK_full.txt | head; grep -n -i 'schneiden' POK_full.txt | grep -i 'tu' | head; grep -n -i 'σάρξ\\|sarx\\|sárx' POK_full.txt POK_0*.txt | head"
}
```


### [2026-10-15T02:44:38.089Z] TOOL RESULT

```
87806:Page(s):1102 
87956:Page(s):1102 
87968:Page(s):1102 
75146:footstool ', QKoAuTTTEiv " mutilate, beschneiden' Hes., anooKoAunTU) "kastriere'; auf eine 
76073:Haarschneiden; allotment ', Old High German sca/'a"Heeresabteilung, troop, multitude, 
POK_full.txt:71510:Denominativa auf -a/g/m {cymr. -haafj\ Old Irish sarxw. "harm, iniuria ' {*sag-ro-), verbal
```


## [2026-10-15T02:44:39.800Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 87900,87970p POK_full.txt"
}
```


### [2026-10-15T02:44:40.220Z] TOOL RESULT

```
tveru, tverV grasp, catch, hold, stop', ablaut. Lithuanian turiCi, turet/"}r\o\d, stop, have', 
Latvian turu, turet ds.. Old Prussian tur/t^have, sollen'; Lithuanian ap-tvaras' paddock ', 
/i/5/:^55"Einzaunung', /i/5/'s/K//"mehrfach to hem, gird, border', Latvian tvarstFt' grasp, 
catch, capture '; Church Slavic tvorb "forma'. Old Church Slavic tvor/'t/" create, make'. Old 
Russian tvorh' appearance ', serb. fvorac' creator, god'; lengthened grade Lithuanian 
t\/ora, Latvian tvare ler\ce' , Old Church Slavic fvarb " creation, creature'; in addition russ. 
tvarogm. (from which Modern High German 'Quark = curd), compare zur formation 
Lat\r\ format/cum, French Yromage', originally participle: Lithuanian tvir-tas, Latvian tvirts 
"strong, tight, firm' {*tur-to-). Old Church Slavic tvrbd'b, russ. tverdyj ds. {*tur-, the variation 
/: d\rorr\ originally konson. Stammzu define); in addition still Old Russian tvhrdbi. " vault 
of the sky, firmament, heavens, skies, fortification '. 



References: WP. I 750 f., Trautmann 333 f., Vasmer 3, 85 ff., Hofmann Gr. etym. Wb. 305, 

308, 353. 

Page(s):1101 

Root / lemma: tuei-1 

Meaning: to cut down, hack, hit 

Material: Old English dwTtan siem V. "cut, clip, abscise ' (would be o'-present; in addition) 

gedwit^cWi'Q, splinter'. Old Icelandic A'i/e///'"Querhieb, incision ', f^ve/ta^\r\e\N, hit, bump, 

poke'; Lithuanian tvyskinu, -//7//"vast, grand anklopfen', tvoju, /i/d//Scherzwort for 

"proficient thrash'; infolge of Knomatopoelcwor^sSclJ the Lithuanian words 

dubious Vergleich. 

References: WP. I 747 f. 

Page(s): 1 099 

Root / lemma: tub'^- 

Meaning: hollow 

Note: only gr. and Latin 

Material: Gr. alcpwv, -wvoq m. "Abzugsrohre, Weinheber, Feuerspritze, Weinschlauch', 

aicpv£U(; " mole ' ("rohrenformige Gange burrowing '), ai(pv6(; Kzybc, Hes. (actually "hollow'), 

probably also ai(pA6(; "hollow, fragile, easily broken; unstable, dilapidated, lame', aicpAouv 

"spoil'; Latin /A&/a"Schienbeinknochen; gerade whistle, flute', belongs barely to sffb(h)-^ 

shaft, pole' (above S. 1015), das festes s- has. 

References: WP. I 751 f., WH. II 680. 

Page(s):1102 

Root / lemma: tu6[u]- : tuau- : tu-l- 
Meaning: tube 

Material: Old Indie tuna- m., tOmi. " quiver ', tOnava- m. "flute' {*fu/-n-): Old Church Slavic 
/i//b" quiver'; gr. awAnv "gully, duct, tube, pipe, canal'; with reduplication-stem *tyau-. 
*aaupoc; or *aaupa "duct, tube, pipe am unteren end the lance ', in aaupwrrip "ein about 
das untere Lanzenende gestijlptes, rohrenartiges piece', with /7-forms aauviov "to 
av5p£Tov ai5oTov' ("*duct, tube, pipe'), in the Koine "spear, javelin, spit, pike'. 
References: WP. I 752, WH. II 688, Vasmer 3, 150, Mayrhofer 1, 518, J. Hubschmid, Bibl. 
Faculte de Philos. et Lettres de I'Univ. de Liege, Fasc. 129 (1953), 194. 
Page(s):1102 

Root / lemma: tu-/o-
```


## [2026-10-15T02:44:42.449Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>87700 && NR<87900 && /lemma/' POK_full.txt; grep -n 'lemma: tuer\\|lemma: tu\\(e\\|e\\)r' POK_full.txt | head"
}
```


### [2026-10-15T02:44:42.852Z] TOOL RESULT

```
Root / lemma: tue/-2, extended tuei-s- 
Root / lemma: tuengh- 
Root / lemma: tuen- 
Root / lemma: tuerR- 
Root /lemma: tuer-1: /it//"- and tuf- 
Root / lemma: tuer-2 : tur-, tuera- 
87790:Root / lemma: tuerR- 
87808:Root /lemma: tuer-1: /it//"- and tuf- 
87885:Root / lemma: tuer-2 : tur-, tuera-
```


## [2026-10-15T02:44:44.205Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 87785,87808p POK_full.txt"
}
```


### [2026-10-15T02:44:44.575Z] TOOL RESULT

```
Page(s): 1 099 



Root / lemma: tuerR- 
Meaning: to cut 

Material: Avestan ^waras-^cut, clip, schnitzend gestalten', participle ^warsta-, dworsstar- 
or z?M/5/'aA's/a/'- "creator, god, molder': Old Indie GN Tvasta{-ar-) from *Tvarstar, in addition 
probably gr. aap^, -koc, "flesh", PI. "FleischstiJcke' (Aeolic aupKsc;), aapKo^siv "tear, sich auf 
die Lippen beiften, mock ', aapK6-(paY0(; " carnivorous ', Subst. 'Sarg = coffin' (> Latin 
sarcophagus> Old High German sarch. Modern High German Sarg); if as "Ouerschnitf 
here also die family of Old High German dwerah^o^uef (etc., see below terk- "turn')? 

Ein from turk- entstandenes *truR-seeks man in Latin trux, /mc/s "rough, prickly, 
durchbohrend (of look), abstoftend, fierce, grim, defiant', truculentus' dim in den Mienen, 
griesgramig', /At/c/o'5/'e"niedermetzeln' (from *truci-caidos\.o Latin caedo above S. 917), to 
Old Irish tru{*truk-s) "totgeweihf. Gen. troch{*truk6s). 

References: WP. I 751, WH. II 695, 709, 711 f., Mayrhofer 1 , 539. 
Page(s):1102 

Root /lemma: tuer-1: /it//"- and tuf-
```


## [2026-10-15T02:44:48.423Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^twerk\\|twerk-' AHD_watkins1985.txt | head; grep -n -i '^sarcasm\\|^sarco\\|^sarcoma\\|^sarcology\\|^sarcastic' KLN_1966.txt | head; grep -n -i '^sarcasm\\|^sarco' SKT.txt | head; grep -n -i 'tuerk\\|tuerk\\|twerk\\|tvarst\\|tvasht\\|tvaṣṭ' IEC.txt | head"
}
```


### [2026-10-15T02:44:48.827Z] TOOL RESULT

```
1100:twerk-. To cut. Zero-grade form *twrk- in Greek sarx, flesh (< “piece of meat”): SARCASM, SARCO-, (SARCOID), (SARCOMA), (SARCOUS); ANASARCA, ECTOSARC, PERISARC, (SARCOCARP), SARCOPHAGUS, (SARCOPTIC MANGE), SYS- SARCOSIS. [Pok. tuerk- 1102.]
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2212:SAPID sep-1 SAPIENT sep-1 SAPONACEOUS _ seib- SAPONATE seib- SAPONIFY seib- SAPONIN seib- SAPONITE seib- SAPOR sep-! SAPROBE gWei- SAPSAGO skep- SARCASM twerk- SARCO-  twerk- SARCOCARP twerk- SARCOID twerk- SARCOLEMMA lep-1 SARCOMA twerk- SARCOPHAGUS twerk- SARCOPTIC MANGE skep-, twerk- SARCOUS twerk- SARDONIC sward- SARDONYX nogh- SARMENTOSE serp-1 SARTORIUS serk- SASTRUGA ghd, ster-2 SATE! sa-
2333:SYNARTHROSIS ar- SYNCLINAL klei- SYNCOPE skep- SYNDESMOSIS dé- SYNDETIC dé- SYNDIC deik- SYNECDOCHE dek-', eghs SYNERGID werg- SYNERGISM werg- SYNESIS yé- SYNIZESIS sed-1 SYNKARYON kar-! SYNOD sed-2 SYNONYMOUS nd-men- SYNOPSIS OkW- SYNOSTOSIS ost- SYNTAX tag- SYRINGOMYELIA mis- SYSSARCOSIS twerk- SYSTALTIC stel- SYSTEM sta-
33700:sarcoae
33738:sarcocarp,  n.,  the  fleshy  part  of  a  fruit.  —  Com¬ pounded  of  sarco-  and  Gk.  xapiro?,  ‘fruit’.  See
33740:sarcode,  n.,  animal  protoplasm. — Gk.  oapxtoSes, ‘fleshy  substance’,  subst.  use  of  the  neut.  of capxco87)<;,  ‘fleshlike’,  which  is  compounded  of
33741:Sarcodina
33746:Sarcodina,  n.  pi.,  a  class  of  Protozoa  ( zool .)  — ModL.,  fr.  Gk.  crapzuSrjp,  ‘fleshlike’.  See  prec. word.
33747:sarcology,  n.,  the  anatomy  of  the  soft  parts  of  the body.  —  Compounded  of  sarco-  and  -logy, sarcoma,  n.,  tumor,  malignant  growth.  —  Med¬ ical  L.,  fr.  Gk.  aapxoifia,  ‘fleshy  substance’,  fr. ad p§,  gen.  aapxAp,  ‘flesh’.  See  sarco-  and  -oma. sarcophagus,  n.,  stone  coffin.  —  L.,  fr.  Gk. erapxocpixYoi;,-n.,  ‘coffin’,  fr.  aapKoepd-yai;,  adj., ‘eating  flesh’,  fr.  aapE,,  gen.  csa.py.6q,  ‘flesh’,  and (paytiM,  ‘to  eat’.  See  sarco-  and  -phagous.  In  an¬ cient  Greece  coffins  were  made  of  a  kind  of limestone  that  consumed  the  flesh  of  the  body enclosed.  L.  sarcophagus  was  shortened  into  VL. *sarcus,  whence  OF.  sarcou  (F.  cercueil),  ‘coffin’, OHG.  sarc,  saruh  (MHG.  sarc  and  sarch,  G. Sarg),  of  s.m.,  MDu.  sarc,  sere  (Du.  zerk), ‘tombstone’.
33748:sarcosine,  n.,  a  crystalline  amino  acid  ( chem .)  — G.  Sarkosin,  coined  by  the  German  chemist, Baron  von  Justus  Liebig  (1803-73)  in  1847  fr. Gk.  oap5,  gen.  aapx6p,  ‘flesh’,  and  suff.  -in.  See sarco-  and  chem.  suff.  -ine. sarcous,  n.,  pertaining  to  flesh  or  muscle.  — Formed  with  suff.  -ous  fr.  Gk.  ad  pi;,  gen. aapxop,  ‘flesh’.  See  sarco-. sard,  n.,  a  variety  of  quartz.  —  F.  sarde,  fr.  L. sarda,  fr.  Gk.  aapSiov,  prob.  meaning  lit.  ‘Sar¬ dian  stone’,  fr.  ZdcpScip,  ‘Sardis’,  the  capital  of ancient  Lydia.  Cp.  sardine,  ‘a  precious  stone’, sardius.
16478:SARCASM.
16489:Sarcasm,  a  meer.    (F.— L.-Ck.) sarcasme.^'L.  sasrasmus.^GV.  tfa, a  sneer.  — Gk.  oapma^uv,  to  tear bite  the  Iii:is  in  rage,  to  sneer.  — stem  of  crapf,   Acsh.     l^vt. aapHaoTiitit,  sneering.
16490:sarcophagus.  ;U  -  Ck,y    L.  m phagut,  a  ^tone  tomb;  nude  of stone  which  was  suppoaed  to corpse   (Pliny^.  —  Gk.  «e ouusumuig ,  beoo:  Umr-atnnc-  *  Uk.  ^V
19431:tuerk-, tuork- (?) ‘grip, press, fix MHG cf. zwergen, v. “press, knead, squeeze"; Li. cf. (o-gde) tvarküs, adj. ‘orderly’; tvarkà, f. ‘orderliness’
19432:tuerK- ‘athwart, across; cross, transverse; crosscut, section’. Cf. WP I, 751 Av. (z-gde) Oworos-, v. ‘resect, cut off; Ówarso, m. ‘section’; Lat. cf. furca, f. (2) *crosspiece', cf. Lat. *quadri-furcum (*crossroads' in Fr. carrefour); (for Lat. furca (1), see bhrk-); Go. pwaírhs, adj. “angry, cross’; pwairhei, f. “anger, strife’; OHG thwérh, dwérh; MHG twérch, dwérch & twér, dwér; OE pweorh, ON pverr, adj. 'oblique, athwart, askew’; Ger. dial. zwerch, id. cf. Zwerchfell ‘diaphragm’; Sw. tvår, adj. & adv. “cross, athwart, steep, brus- que’; MDu. dwers, Du. dwars, adj. ‘evil’; LG dweer and dwars, adv. ‘askew’; dwer, adj. *obli- que’; Fris. cf. it is my twer ‘I loathe it’; (OCS črěsň, prp. “across, through is fr. a type ker- sos, Q. V.)
19439:tuerk-, tuork- — tuis-
19483:tuorst- (tuort-) “fixed, firm'. Cf. tuer- (2) and tur- (2), tuor- (1) Av. Owarsta, pp. as adj. "limited, fixed; suit- able’; Li. tvarstas, m. ‘bandage’; tvartas, m. id. (and ‘stable, fold, pen"); Latv. tvarts, m. “shelter”. (For the initial cf. Go. ga-pwastjan, v. ‘secure, fix"). Cf. turtos, is
19497:turk-, cf. tuerk- (tuork-) MHG dürchen (OHG *duruhen) ‘pierce’; Li. tvirkstu, tvirkti, v. ‘degenerate’
```


## [2026-10-15T02:44:51.744Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'sarcasm' KLN_1966.txt | head; grep -n -i 'sark\\|sarx\\|sarco' IEC.txt | head; grep -n -i 'sarx\\|σάρξ\\|flesh' SYN.txt | head -5"
}
```


### [2026-10-15T02:44:52.517Z] TOOL RESULT

```
24224:Momus,  n.,  1)  the  god  of  censure  and  sarcasm (Greek  mythol.);  hence  2)  a  carping  critic.  —  L., fr.  Gk.  Mcopoi;,  fr.  propo;,  ‘blame,  ridicule’, which  is  prob.  rel.  to  a-pupcov,  ‘irreproach¬ able’;  of  uncertain  origin, mon-,  form  of  mono-  before  a  vowel.
33736:sarbacane,  n.,  a  blowgun.  —  F.,  changed  under the  influence  of  canne,  ,‘cane,  reed’,  fr.  sarbatane (still  used  in  1798  by  the  French  Academy),  fr. Sp.  cerbatana,  zarbatana,  fr.  VArab.  zarbatanJ ’, fr.  Arab.  zabatanah,  ult.  fr.  Malay  sumpitan,  of s.m.,  fr.  sumpit,  ‘narrow’.  Cp.  sumpit. sarc-,  form  of  sarco-  before  a  vowel, sarcasm,  n.,  a  taunting  remark;  an  ironical  jibe. —  F.  sarcasme,  fr.  L.  sarcasmos,  fr.  Gk. oapxaopios,  ‘jest,  taunt,  mockery’,  fr.  oap- iv,  ‘to  tear  flesh  like  dogs;  to  bite  the  lips  in rage;  to  speak  bitterly,  sneer’,  fr.  aotp5,  gen. aiy.py.be,  ‘flesh’.  See  sarco-. sarcastic,  adj.  —  Gk.  oapxaa-ixoi;,  fr.  oap- xa^civ.  See  prec.  word  and  adj.  suff.  -ic. Derivatives:  sarcastic-ness,  n.,  sarcastic-al,  adj., sarcastic-al-ly,  adv.,  sarcastic-al-ness,  n. sarcenet,  sarsenet,  n.,  a  fine  silk  material.  —  Late ME.  sarsenet,  fr.  AF.  sarzinet,  dimin.  of  ME. sarzin,  ‘Saracen’.  See  Saracen.
2186:derghó (dorgh-, drgh-) 'hurt, torture'. Cf. WP I, 801. See dhrgh- Alb. (ambig.) dergjem “lie ill, mp: Tokh. tsárk-, B tsark- ‘annoy, worry’; Ir. deargaim (2) “hurt, wound’; OE tregian ‘harass’;. ON trega ‘grieve’; Li. dérgiu, dérgti (2) ‘abuse’; o-gde in OE tergan, tiergan ‘tease’; Du. ter- gen; G zergen, id.; Cz. drázditi, id.; z-gde in R dérgat ‘scour; pill flax’ and Cz. drhnou- ti, id.
3060:dhrághó, ið ‘harass’. Cf. dhràgh- (2) and dhraghoó Gk. thrásso, Hom. pf. té-trékha ‘disturb’; Skt. draghe “strain, torture oneself; Tokh. tsárk-, B tsark- ‘harass’; OCS draZo, dražiti “irritate”
8572:Karkos (Kork- ?) ‘enclosure’. Cf. WP I, 31 Alb. thark, pl. -a & tharqe, m. id.; Rum. sub- strate tarc, m. id.; OE hearg, m. & hearga, wm. ‘tempie, grove’. (OE serce, serc ‘shirt, corselet’; ON serkr and E sark, LW in Finn. sarkki and sarka ‘coarse woollen cloth’ appear to derive from Gk. sērikón ‘silk robe’ via Lat. sēricum ‘muslin’ and sērica ‘muslin garment’, but Li. Sarkas ‘garment, jacket; OCS sraka and sraky, f. gs sraküve, id. display an un- usual initial if derived from Gmc. Alb. shark ‘jacket derives from the Lat. form, as also Rum. saricá)
8741:Kolkolos ‘pebble-. Variant of type Kolos? q. v. Cf. WP I, 463 Skt. Sarkarab, id.; Lat. calculus, id.
9152:Ksuark- ?, Ksark- ? “coat, jacket, garment;
9153:homespun material'. An early Tataric word in IE? Phonology obscure, and there is some confusion with a Latin word sericum, lit. *Chi- nese’. The Tataric origin is reinforced by the existence of a Turkish type sírka *jacket'. Cf. Kark- (Kork- ?) Hitt. cf. sarku(mi) (queried: ‘put on, don’); Alb. shark “jacket; enclosure'; LLat. cf. sarcia and sareca ‘shirt’, perh. from Gmc. cf. OE sier- ce *coat, shirt, armour'; ON serkr, id.; Scots sark “shirt, shift, but see W. Steinhauser, Slavonic Review, 1950, 284-8; OCS sraka jacket; R cf. sorócka, dim. ‘shirt’. Specula- tions and lit. in AP: ESRJ a, p. 358b: soróka (2); Li. Sarkas & švarkas, ai «coat; Latv. svārki, mpl. id. The Finn. LW sarka ‘homespun cloth’ is apparently a Gmc. LW. Cf. WP I, 751
15238:serguho ‘languish, be ill. (WP II, 498 er- roneous) Tokh. A cf. särk, B sark, s. “illness”; Ir. sear- gaim, seirgim, v. “pine, languish’; MHG sër- wen, sérben, v. id.; G dial. serben, id.; Li. sergù, sitgti, v. ‘be il; cf. (z-gde) Latv. sirgstu, sirgt, id.; Alb. cf. dérgjem, v. “lie ill, be il^; dergjë, f. “illness? (if fr. *de-serguh-io or sim.). Nominal types: Olr. serg, seirge, f.; Ir. searg, f. ‘decay, decline’; MHG serwe and serbe, sf. id.; Li. dial. sergà, f. ‘indisposition’; Latv. sēr- ga “epidemic, illness?
16731:Icel. sarga, v. (1) ‘hack’; Sw. sarga, v. ‘wound, graze, têar’; OCS sragü, adj. “awfuP. (Hitt. sarkus, adj. = ‘mighty, glorious’ or sim.) sorguhð ‘watch, observe, sleuth, pester’. (Evidence ambig.). Cf. WP II, 529 Hitt. sarkumi, v. ‘equip myself”; sarikuwas, s. (equipment? or “armed soldier”); Ir. suir- ghim, v. ‘woo’; (Go. sarwa, npl. ‘armour’; OE searu, searo, n. ‘craft, device’); Li. sargùs, adj. “watchfuP; Latv. sargs, m., sardze, f. ‘watch’; sargu, inf: sargāt (sic) ‘watch’. (Li. sarginti, inf. ‘make ill’ is factitive to type ser- guhō, q. v.). For Gmc. (ambig.) see soruos (1) sormos (sormonos, sormot-) ‘glum, gloomy, downcast, shamed'. Gk. ambig. cf. suorm- Cf. Gk. hormaíno, v. ‘sulk’ ?; Hes. hormanós, adj. ‘saturnine’?; OCS sramü, m. ‘shame’; sraméjo, čti, v. “be ashamed'; sramota, f. *shame'; Ukr. sorom, m. id.; Li. sarmatà, f. ‘shame’
17141:Skt. cf. sürks(y)àmi, v. “care, trouble’; Pol. sarkac, v. ‘complain’ (isophonic w. Cz. srkat, v. ‘whimper’. Mourek), otherwise ‘sup’; Srb. sikati, id. Itkonen & Joki derive the Finn. LW surku “pity? fr. Gmc., cf. OHG sorgen and sworgen, of uncertain background)
18807:torqueió ‘twist, turn’. (Gk. variant troqu-); torquos, à, is, us (troqu-) “turn, twist; turned, twisted’. Cf. WP I, 735 Tokh. B tsárk-, tsark-, v.? ( torture’. Here WH,
2030:Av. xruézdra-, xraozdva- ‘hard’, all fr. *krus-, *krus-t, *kruz-d, with the com- mon notion of ‘hard, hard surface’, whence ‘ice’ in xpicraddos and second- arily ‘icy cold’ in xpios. Further con- nection with the group meaning ‘bloody, raw, raw flesh’ (Skt. Kravis, Grk. xpéas, Lat. cruor, etc.), if actual, is more re- mote. Walde-P. 1.479.
2395:Pol. pteé: ChSl. plhiti, Russ. plot ‘flesh, body’, Boh. plet ‘complexion’ (also Zenska plet ‘female sex’). Briick- ner 420 f.
4239:Sp. carnero now generic, but orig. ‘wether’ (now carnero Ulano with llano ‘plain’), as the fatted sheep, deriv. of carne ‘flesh’. REW 1706.
5192:4.11 Bopy 4.12 Skin; Hipp 4.13 FLesH 4.14 Hair 4.142 Brarp 4.15 Butoop 4.16 Bone 4.162 Ris
5279:Several of the words must have been applied originally to the main part of the body, the ‘trunk’ as distinguished from the extremities (as sometimes NE body, cf. NED s.v., 5) and reflect notions like ‘swelling, curved, bulging shape’. Some go back to ‘covering’, or ‘surface’, whence ‘form, shape, body’. Some words for ‘flesh’ were also used for ‘body’, as Grk. capt, Lat. card, ME, NE flesh in ills of the flesh, etc., as conversely words for ‘body’ may be used for ‘flesh’, as Lat. corpus.
```


## [2026-10-15T02:44:55.710Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'Avest. thwares\\|9waras\\|Owaras\\|θwarəs\\|tvastr\\|Tvastar' SYN.txt | head; grep -n '4.13 FLESH' SYN.txt; awk '/^4.13 FLESH/{f=1} f{print; n++} n>40{exit}' SYN.txt | grep -n -i 'grk\\|cap' | head"
}
```


### [2026-10-15T02:44:56.150Z] TOOL RESULT

```
14034:cher OE sceran, ceorfan, Pol. kraja¢, rznqé, aa Sp. cortar, tajar snipan, héawan rqbaé, siec : Rum. (dia ME _ sschere, cerve, hewe, Russ. _rezat’, rubit', seg" Ir. tescaim, snaidim, culle Skt. krt-, chid-, lu-, cas. scothaim NE cut Av. karat-, Owaras-, bri- NIr. — gearraim, snoighim Du. snijden, houwen ; W. torri, naddu, trychu OHG  snidan, houwan, mei- Br. trouc’ha, skeja zan MHG sniden, houwen, mei- zen NHG = schneiden
22915:OE pweorh: ON pverr ‘crosswise’, OHG dwerah ‘slanting, oblique, across’ (NHG zwerch ‘across’), Goth. bwairhs ‘angry’, root connection dub., but pos- sibly as orig. ‘cut (crosswise)’ : Av. Owaras- ‘cut’, Grk. capt ‘flesh’, root *twerk-; or as ‘twisted’ fr. the root in OHG dweran ‘turn rapidly’, OF pweran ‘twirl, stir’, Skt. tur- ‘hasten’, etc. Walde-P. 1.736. Weigand-H. 2.1353. Feist 507. NED s.v. thwart, adv.
5343:Falk-Torp 997. aja-, etc. Walde-P. 1.38. fe 4.13 FLESH NG ia xptas Goth. mimz, mammé Lith. mésa oe a aidan ON hold, horund Lett. miesa It. carne Dan. kd ChSl. _pliitt, meso Be igtiags Sw. kétt SCr. meso Sp. carne OE Sl@sc Boh. maso Rims carne ME fleshe Pol. —_ mieso ae feoil, cua NE flesh Russ. mjaso Nir, feoil oe é ei Skt.  mdnsa-, mas- ‘cig, evs Av. av- (NPers. gust Br kig giaiad tS vleisch es be Most of th ee € words ‘ : ot all, are also ead a flesh’, though | semantic sources, where clear, are partly Meat (5,61), Words Ae Beshy as food, | ‘covering, surface’, referring to ‘flesh’ vs. Wed, ep. in. eco] ‘or ‘flesh’ are also | ‘bone’, but oftener ‘cut’, or ‘raw and €ccl. writings, for ‘body? : x ; : ale nversely some oeds f ody’, bloody’, or name of an animal, in all © used for ‘flesh’ or ‘body’ are | these cases referring to the flesh of an
```


## [2026-10-15T02:44:57.838Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5344,5375p SYN.txt | grep -n -i 'capt\\|cap£\\|Owaras\\|twerk\\|tvar' "
}
```


### [2026-10-15T02:44:58.237Z] TOOL RESULT

```
8:2. Grk. capt : Av. @wares- ‘cut’, with development as in Lat. card (below, 3). Walde-P. 1.751. Boisacq 854.
```


## [2026-10-15T02:44:59.300Z] AGENT

Now BRT, WLD, and Sanskrit/Tvashtar.


## [2026-10-15T02:45:01.038Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'schnitzen\\|schnitzend\\|zurechtschneiden\\|Bildner' BRT.txt | head; grep -n 'twerk\\|tuerk\\|tuerḱ\\|t$uerk' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n -i 'σάρξ\\|oapE\\|sarx' WLD_band3.txt | head -5"
}
```


### [2026-10-15T02:45:01.470Z] TOOL RESULT

```
12129:Messer  oder  Axt:  tas'tpin  däuru  (sd.)  V. y-  30-  a)  insbes.  'schnitzen   sva.  ver-
14392:•  j.  ÖTvar^xätar-  m.  'Bildner,  Schöpfer':
14398:1) '(schnitzen  sva.)  schneideDd  gestalten,  %w?fytai  (näml-  AhM.)  nafS  airyatuim schaffen,  hervorbringen':  yS ..yatata  payB  äaXyuttamYtij.Sj;  —  mainyavaia yauita %wSrfäära  ya  vupa  'hwfniats  (3DPrA.)  yai^a  gaii^ya  _/ra>warsta  FiW.  1,2;  — damanW.^/.s; — tuudiha  upa  ^'h warst a    s.    noch    '/ra%waräa-.  a)    dnwS.  z:
14434:•  j.,  g.  dTWÖr«ätar-  m.  'Bildner,  Schöpfer'  ■> : al  zi  %wa  fsuyatiit^a  västryaica  'ta  iatalü "denn  es  hat  dich  der  Bildner  für  den Viehzüchter  und  Bauern  geschaffen"  Y. 29.  6".  a)  Du.  in  Verbindung  mit payav-  m.  Du.:  payü  (sd.)  "«ra  (AD.)  yä vTspa  %w)r?sats  dämqn  Y.  57.  2; —  *pä- yBc'a  (sd.)   'iara  Y.  42.  2.
20625:        Flechtwerk. Rankengewachsen. Ygl. im allgem. Curtius 3 3S9f., 504.
20681:   Got. waddjus „Wall, Mauer“ (ursprgl. aus Flechtwerk s. Meringer Abh.                                             ;
24505:anord. vandahils „Haus von Flechtwerk“, schwed. mdartl. vann „Schling-
26437:   Gr. gtip gletos. jon. gTeios n. ,.Fleehtwerk yon jungen Zweigen, geflocb-
27565:dazu air. frui<i ..Wand”, nir. fraiyh ..Wand aus Flechtwerk, Dach, Fliirde
28680:got. ivalus „Stab"; air .felmae ,,saepes" (vermutlich    *Flechtwerk“, vgl. dt.               .
28905:mit Formans -hi klr. Visa ,,Iliirde, FlechtwerkA nsloven. Ida ..aus Ruten
31906:Wz. kagh- angeblich „umfassen" (s. kagh- „Flechtwerk‘').
31919:qagh- „geflochtene Hiirde, Flecbtwerk u. dgl.“
31945:Durchschlag, Fischreuse (alles aus Flechtwerk nicht wahrscheinlicher zu
123:red ahoapetl amet: ah | dhenje Sk pale ra 2p
```


## [2026-10-15T02:45:03.544Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14392,14400p BRT.txt | cut -c1-500; awk 'NR<14400' BRT.txt | grep -c $'\\f'; grep -n -i 'schneiden' incoming/WLD/WLD_Bd1_pages.txt | grep -i 'tu\\|t\\\\u' | head"
}
```


### [2026-10-15T02:45:04.040Z] TOOL RESULT

```
•  j.  ÖTvar^xätar-  m.  'Bildner,  Schöpfer':
dby  Google
795  S'warss-  —  S-waritay-  796
am»saitqm  sptnianqm  . .  joi  Asnti  anhqm '  (DämL  aurvatam)  safinks  tarattya  paiH.- dämattam  .  .  datarasca  wtanxäarasca  %waritäaAs  "ihre  hömemea  Hufe  sind 'tarasia  aiwyäxHarasiä  Yt.  jg.  18.  mit  Gold  ausgelegt"  ¥.57.27*'.
Zum  V.  in-arjj- ;  xit  nach  l  S6  aE.  Doch  «.        mit  /rä  i)  dnwS.  i :  mi^rTM  . .  yoAmai
ueh  BTHi,  IF.  3. 3  Ko.  3.  -  Vgl  \t«^,st^..  ^g^an»m  fräkw?r»sat  yö  dt^a  aAurd •  j'i  g-  8'warfls-  V.  'schneideo'.  Pracs. !  masdä  Yt  10.  50;  —  paoinm  asa^kamca 3  %uin3ta;  1 5  %wani-^^,  24  %Wfr3saya-;  .  .  fnü^w^nsim  astm  yS  ahurB  ..  V.l.z; t-Aot.  I   äwar?/-*'.  —  PPfP.  'hwaräa:      —  gaye^  mah^niff  .  .  yaAmat  kaca  frä-
1) '(schnitzen  sva.)  schneideDd  gestalten,  %w?fytai  (näml-  AhM.)  nafS  airyatuim schaffen,  hervorbringen':  yS ..yatata  payB  äaXyuttamYtij.Sj;  —  mainyavaia yauita %wSrfäära  ya  vupa  'hwfniats  (3DPrA.)  yai^a  gaii^ya  _/ra>warsta  FiW.  1,2;  — damanW.^/.s; — tuudiha  upa  ^'h warst a    s.    noch    '/ra%waräa-.  a)    dnwS.  z:
rtucäY.34-  a)mitDaL  comm.:  AaAmäi  aexiS  ratus  .  .  ^am  Jrahut^rvtaüi ,  V, mJ  ^warsidam  (j-Aor.)  ii  ma  tasat  "für  1  7,71;  —  .  .  cihqm  fra%wtr»t«Sit  V.  7. wen  habt  ihr  mich  gestaltet?  wer  hat  i  71  (?);  —  bajS.baxt^m  paiti  yaorum  fra- mich  geschaffen?"  Y.  2p.  1.  2)  'etwas  läwor//?/«  paiti  srvärum  Yl  jj.  56;   —
(vorschneiden  sva.)  bestimmen,  festsetzea,  &t7^.AzM!M>r  paiti  yaotum  fra~^warst3m voT%dttähKa':pfnnayuicikqtH  %w»r7saiti  ] paiti  afant^m  YtA'.  35.  3)  'einschnei-
451
2916:lichen s- im Anlaut der Yerbindung mitunserer Wz.               eher zu skcr- „schneiden,  ;
36107:facht, nicht zu hammer „verstummelt‘ = *hnb-md- s. sqep-, sqnp- ,,schneiden“) •
50947: glid- „schneiden“), arm. jol „PfahI, langer Zweig usw.“, lit. suolis „Stuck
51803:III* 139, Kluge 9 s. v.).  Ahd. inginnan „auftun, offnen, aufschneiden,
71143:tuerk- „schneiden".
```


## [2026-10-15T02:45:06.272Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 71130,71165p incoming/WLD/WLD_Bd1_pages.txt; grep -n -i 'Tvast\\|Tvasht' SYN.txt IEC.txt AHD_watkins1985.txt | head -4"
}
```


### [2026-10-15T02:45:06.630Z] TOOL RESULT

```
„gro(3er Korb", Boisacq keine p-Erw.; oder                                        ist   in letzterer              Form tup- zu
tp diss. und danach auch raoy- neben oagy- aufgekommen?)
  Lat. paries „Wand" (von Sommer Hdb. 1 270, 2 221, Heringer IF. 18.
267       u. a. als       tiyiet- angereiht)             gehort nach Persson Beitr. 472 zu pbrq,
*perti ,.stiitzen, als Stiitze, Spreize anlehnen", bezeichnete also ursprgl. die
Seitenstiitzen eines Zeltes u. dgl.
   Unsere Wz. wird von Fick 1* 449 mit Recht von tuer-                                                            ,
                                                                                                                      herumdrehen,
quirlen, riihren" gesondert; von einer unbewiesenen Urbedeutung „*drehen“
aus die Bed. ,.einen Zaun, ein Gehege drehen" usw. abzuleiten, fehlt mir
die Lust.


tuerk- „schneiden".
   Av. dicarss - „schneiden -< {hjosrssaiti, Ptc. divarlta -') dazu wohl vgl. lat. caro     ;                         ;                           :




xeigoj) gr. odg f, -xdg Fleisch", pi. ..Fleischstiicke" (aol. ovgxeg, siehe dazu
                                     ,


Boisacq s. v. m. Lit.), v. Bradke ZdmG. 40, 352. Zu oag£ auch oagxaCea’
in alien, auch der Bed. ,,hohnen‘ (s. Boisacq s. v.). Ob als .,Querschnitt“
hierher auch die Sippe von ahd. dwerah ,,quer (usw., s. u. terek- ,,drehen“)?      ‘



   Ein aus turk- entstandenes *truk- sucht man in lat. trux, tracts rauh,                                                              ,;


stachelig zum Anfiihlen, durchbohrend (vom Blick), abstoBend, grimmig,
trotzig", truculenius „finster in den Mienen, griesgramig" (v. Bradke ZdmG.
40, 352 trifft die lat. Bedeutungsfarbung nicht fractd&re niedermetzeln"                ;                     ,
```


## [2026-10-15T02:45:09.789Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-10-15T02:45:10.402Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-15T02:45:13.593Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/twerḱ-' 'https://en.wiktionary.org/wiki/σάρξ' 'https://en.wiktionary.org/wiki/σαρκάζω' 'https://www.etymonline.com/word/sarcasm' 'https://www.etymonline.com/word/sarco-' 'https://www.etymonline.com/word/sarcoma' 'https://en.wiktionary.org/wiki/त्वष्टृ' 'https://en.wiktionary.org/wiki/sarcasmus' 'https://en.wiktionary.org/wiki/sarcasme'; do python3 tools/fetch_source.py \"$u\" --note \"page 515, root Twerk: IE root, Av/Skt/Greek sarx, sarcasm chain\"; done"
}
```


### [2026-10-15T02:45:20.518Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c122d4e55887a012.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/11eace40a8aebc79.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/185242239f5ffb2e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d3c306729323ea5c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f3f639b032ab8535.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/edd135defae2e8c7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/25a0317de2e668c8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b591b837244585dd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f6b371ce7098524a.txt
```


## [2026-10-15T02:45:22.919Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -9 index.jsonl | cut -c1-300; for f in c122d4e55887a012 11eace40a8aebc79 185242239f5ffb2e d3c306729323ea5c 25a0317de2e668c8; do echo \"=== $f\"; grep -i -A12 'etymology' $f.txt | head -30; done"
}
```


### [2026-10-15T02:45:23.286Z] TOOL RESULT

```
{"url": "https://en.wiktionary.org/wiki/lacayo", "file": "data/verification/sources/web/34c44f1071b8697f.txt", "fetched": "2026-10-15T02:45:20Z", "status": 200, "bytes": 3001, "title": "lacayo - Wiktionary, the free dictionary", "note": "page 517 lookup"}
{"url": "https://en.wiktionary.org/wiki/sarcasme", "file": "data/verification/sources/web/f6b371ce7098524a.txt", "fetched": "2026-10-15T02:45:20Z", "status": 200, "bytes": 5468, "title": "sarcasme - Wiktionary, the free dictionary", "note": "page 515, root Twerk: IE root, Av/Skt/Greek sarx, sarcasm 
{"url": "https://en.wiktionary.org/wiki/lacchè", "file": "data/verification/sources/web/25e70a618a71bfb2.txt", "fetched": "2026-10-15T02:45:20Z", "status": 200, "bytes": 2369, "title": "lacchè - Wiktionary, the free dictionary", "note": "page 517 lookup"}
{"url": "https://en.wiktionary.org/wiki/الاغ", "file": "data/verification/sources/web/efc85a25804d619f.txt", "fetched": "2026-10-15T02:45:21Z", "status": 200, "bytes": 3825, "title": "الاغ - Wiktionary, the free dictionary", "note": "page 517 lookup"}
{"url": "https://en.wiktionary.org/wiki/ulak", "file": "data/verification/sources/web/8cd399cfbc20568b.txt", "fetched": "2026-10-15T02:45:21Z", "status": 200, "bytes": 6088, "title": "ulak - Wiktionary, the free dictionary", "note": "page 517 lookup"}
{"url": "https://www.nisanyansozluk.com/kelime/ulak", "file": "data/verification/sources/web/b1e71d556641d496.txt", "fetched": "2026-10-15T02:45:22Z", "status": 200, "bytes": 219, "title": "ulak - Nişanyan Sözlük", "note": "page 517 lookup"}
{"url": "https://en.wiktionary.org/wiki/uterus", "file": "data/verification/sources/web/9599f908e7f3eb61.txt", "fetched": "2026-10-15T02:45:22Z", "status": 200, "bytes": 15005, "title": "uterus - Wiktionary, the free dictionary", "note": "page 517 lookup"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/udéros", "file": "data/verification/sources/web/5b0cfc1edcfd50ae.txt", "fetched": "2026-10-15T02:45:22Z", "status": -1, "bytes": 39, "title": "", "note": "page 517 lookup"}
{"url": "https://www.etymonline.com/word/uterus", "file": "data/verification/sources/web/c0328894477fcf9f.txt", "fetched": "2026-10-15T02:45:23Z", "status": -1, "bytes": 39, "title": "", "note": "page 517 lookup"}
=== c122d4e55887a012
=== 11eace40a8aebc79
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 

 1.4.1 
 Usage notes 

 1.4.2 
 Declension 
--
 Etymology
 [ edit ] 

 From Proto-Hellenic *súrks , *swə́rks , originally denoting "a piece of meat", from Proto-Indo-European *turḱ-s , a zero-grade s-stem nominal from the root *twerḱ- ( “ to cut ” ) . [ 1 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /sárks/ → /ˈsarks/ → /ˈsarks/ 

 ( 5 th BCE Attic ) IPA ( key ) : /sárks/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈsarks/ 
=== 185242239f5ffb2e
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Conjugation 

 1.3.2 
 Derived terms 
--
 Etymology
 [ edit ] 

 From σᾰ́ρξ ( sắrx , “ meat; flesh ” ) +‎ -ᾰ́ζω ( -ắzō , verbal suffix ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /sar.káz.dɔː/ → /sarˈka.zo/ → /sarˈka.zo/ 

 ( 5 th BCE Attic ) IPA ( key ) : /sar.káz.dɔː/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /sarˈka.zo/ 
=== d3c306729323ea5c
=== 25a0317de2e668c8
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 

 1.4.1 
 Declension 

 1.5 
 Proper noun 
--
 Etymology
 [ edit ] 

 From Proto-Indo-Aryan *twá(r)ṣṭā , from Proto-Indo-Iranian *twárštā , from Proto-Indo-European *twr̥ḱ-tēr , from *twerḱ- ( “ to cut, trim, carve off ” ) .

 Pronunciation
 [ edit ] 

 ( Vedic ) IPA ( key ) : /tʋɐ́ʂ.ʈr̩/ 

 ( Classical Sanskrit ) IPA ( key ) : /t̪ʋɐʂ.ʈr̩/ 

 Noun
```


## [2026-10-15T02:45:25.820Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -E 'twer|sarc|σάρξ|σαρκ|त्वष्टृ' index.jsonl | cut -c1-260; wc -c c122d4e55887a012.txt d3c306729323ea5c.txt f3f639b032ab8535.txt edd135defae2e8c7.txt b591b837244585dd.txt"
}
```


### [2026-10-15T02:45:26.212Z] TOOL RESULT

```
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res", "file": "data/verification/sources/web/7f1273ffcd63ff3f.txt", "fetched": "2026-09-06T22:40:52Z", "status": 200, "bytes": 6499, "title": "Reconstruction:Proto-Indo-
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/twerḱ-", "file": "data/verification/sources/web/c122d4e55887a012.txt", "fetched": "2026-10-15T02:45:14Z", "status": 200, "bytes": 4481, "title": "Reconstruction:Proto-Indo-European/twer
{"url": "https://en.wiktionary.org/wiki/σάρξ", "file": "data/verification/sources/web/11eace40a8aebc79.txt", "fetched": "2026-10-15T02:45:16Z", "status": 200, "bytes": 7551, "title": "σάρξ - Wiktionary, the free dictionary", "note": "page 515, root Twerk: IE r
{"url": "https://en.wiktionary.org/wiki/σαρκάζω", "file": "data/verification/sources/web/185242239f5ffb2e.txt", "fetched": "2026-10-15T02:45:18Z", "status": 200, "bytes": 11807, "title": "σαρκάζω - Wiktionary, the free dictionary", "note": "page 515, root Twer
{"url": "https://www.etymonline.com/word/sarcasm", "file": "data/verification/sources/web/d3c306729323ea5c.txt", "fetched": "2026-10-15T02:45:18Z", "status": -1, "bytes": 39, "title": "", "note": "page 515, root Twerk: IE root, Av/Skt/Greek sarx, sarcasm chain
{"url": "https://www.etymonline.com/word/sarco-", "file": "data/verification/sources/web/f3f639b032ab8535.txt", "fetched": "2026-10-15T02:45:18Z", "status": -1, "bytes": 39, "title": "", "note": "page 515, root Twerk: IE root, Av/Skt/Greek sarx, sarcasm chain"
{"url": "https://www.etymonline.com/word/sarcoma", "file": "data/verification/sources/web/edd135defae2e8c7.txt", "fetched": "2026-10-15T02:45:18Z", "status": -1, "bytes": 39, "title": "", "note": "page 515, root Twerk: IE root, Av/Skt/Greek sarx, sarcasm chain
{"url": "https://en.wiktionary.org/wiki/त्वष्टृ", "file": "data/verification/sources/web/25a0317de2e668c8.txt", "fetched": "2026-10-15T02:45:19Z", "status": 200, "bytes": 6656, "title": "त्वष्टृ - Wiktionary, the free dictionary", "note": "page 515, root Twerk
{"url": "https://en.wiktionary.org/wiki/sarcasmus", "file": "data/verification/sources/web/b591b837244585dd.txt", "fetched": "2026-10-15T02:45:20Z", "status": 200, "bytes": 3747, "title": "sarcasmus - Wiktionary, the free dictionary", "note": "page 515, root T
{"url": "https://en.wiktionary.org/wiki/sarcasme", "file": "data/verification/sources/web/f6b371ce7098524a.txt", "fetched": "2026-10-15T02:45:20Z", "status": 200, "bytes": 5468, "title": "sarcasme - Wiktionary, the free dictionary", "note": "page 515, root Twe
4907 c122d4e55887a012.txt
 134 d3c306729323ea5c.txt
 133 f3f639b032ab8535.txt
 134 edd135defae2e8c7.txt
3986 b591b837244585dd.txt
9294 total
```


## [2026-10-15T02:45:28.387Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 1,200p c122d4e55887a012.txt | grep -v '^\\s*$' | head -70; grep -v '^\\s*$' b591b837244585dd.txt | grep -i -A3 'etymology' | head; grep -v '^\\s*$' f6b371ce7098524a.txt | grep -i -A3 'etymology' | head"
}
```


### [2026-10-15T02:45:29.069Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/twerḱ-
FETCHED: 2026-10-15T02:45:14Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/twerḱ- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/twerḱ- - Wiktionary, the free dictionary 
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
 Derived terms 
 1.2 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ twerḱ- 
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
 Etymology 
 1.2 
 Pronunciation 
 1.3 
--
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-European *twerḱ- 
 Proto-Indo-European *-s 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
--
 Etymology 
 2.2 
 Pronunciation 
 2.3 
--
```


## [2026-10-15T02:45:32.090Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' c122d4e55887a012.txt | sed -n 70,140p; grep -v '^\\s*$' b591b837244585dd.txt | grep -n -i -B2 -A6 'σαρκασμ' | head -20; grep -v '^\\s*$' f6b371ce7098524a.txt | grep -i -B2 -A4 'sarcasmus\\|Borrowed\\|from Latin' | head -20"
}
```


### [2026-10-15T02:45:32.778Z] TOOL RESULT

```
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
 *twerḱ- [ 1 ] [ 2 ] [ 3 ] [ 4 ] 
 to carve , cut off , trim 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *twerḱ- (18 c, 0 e) 
 *twr̥ḱ-é-ti ( zero-grade thematic present ) [ 2 ] 
 Proto-Indo-Iranian: *twr̥ćáti 
 Proto-Iranian: *twr̥cáti 
 Younger Avestan: 𐬟𐬭𐬁𐬚𐬡𐬆𐬭𐬆𐬯𐬀𐬉𐬙𐬀 ( frāθβər ə saēta , “ to cut ” , 2pl.opt.act. ) 
 *tworḱ-ó-s ( “ cutter, boar ” ) [ 3 ] 
 Proto-Celtic: *tworkos ( “ boar ” ) [ 3 ] 
 Proto-Indo-Iranian: *twarćas 
 Proto-Iranian: *θwarcah 
 Avestan: 𐬚𐬡𐬆𐬭𐬆𐬯𐬋 ( θβər ə sō , “ piglet ” ) 
 *twr̥-n-ḱ-ó-s ( nasal-infix ) 
 Proto-Italic: *trunkos 
 Latin: truncus ( “ a cut off piece; maimed ” ) ( see there for further descendants )
 *turḱ-s ( s-stem ) [ 4 ] 
 Proto-Celtic: *truxs ( “ slain, cut man ” ) [ 3 ] ( see there for further descendants )
 Proto-Hellenic: *súrks , *swə́rks 
 Ancient Greek: σύρξ ( súrx ) , σάρξ ( sárx , “ piece of meat, body part ” ) 
 Proto-Italic: *truks 
 Latin: trux ( “ wild, fierce, harsh ” ) ( see there for further descendants )
 ⇒ *turḱ-s-os 
 Proto-Celtic: *truxsos ( “ a cut off piece ” ) [ 3 ] ( see there for further descendants )
 *twérḱ-tōr 
 Proto-Indo-Iranian: *twárštā ( see there for further descendants )
 References
 [ edit ] 
 ^ Mallory, J. P. with Adams, D. Q. ( 2006 ), “*twerḱ- 'to cut out'”, in The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 157 
 ↑ 2.0 2.1 Rix, Helmut , editor ( 2001 ), “*tu̯erk̑- 'schnitzen, zurechtschneiden'”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 656 
 ↑ 3.0 3.1 3.2 3.3 3.4 Matasović, Ranko ( 2009 ), “*truk-, *truxso-”, in Etymological Dictionary of Proto-Celtic (Leiden Indo-European Etymological Dictionary Series; 9), Leiden: Brill , →ISBN , page 391 : “ *trewk- 'cut' ” 
 ↑ 4.0 4.1 Beekes, Robert S. P. ( 2010 ), “ σάρξ, σαρκός ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , page 1309 : “ *turk̂- 'cut' ” 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/twerḱ-&oldid=92151826 "
 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European CReRC-shaped roots 
 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 This page was last edited on 23 August 2026, at 21:58.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy 
 About Wiktionary 
 Disclaimers 
 Legal & safety contacts 
 Code of Conduct 
 Developers 
 Statistics 
 Cookie statement 
 Mobile view 
 Search 
 Search 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ twerḱ- 
 Add languages 
 Add topic
98- Proto-Indo-European *-mós 
99- Ancient Greek -μός ( -mós ) 
100: Ancient Greek σαρκασμός ( sarkasmós ) der. 
101- Latin sarcasmus 
102: Derived from Ancient Greek σαρκασμός ( sarkasmós ) .
103- Pronunciation
104- [ edit ] 
105- ( Classical Latin ) IPA ( key ) : [sarˈkas.mʊs] 
106- ( modern Italianate Ecclesiastical ) IPA ( key ) : [sarˈkaz.mus] 
107- Noun
108- [ edit ] 
 Etymology
 [ edit ] 
 Learned borrowing from Late Latin sarcasmus .
 Pronunciation
 [ edit ] 
 IPA ( key ) : ( Northern , Balearic , Central ) [sərˈkaz.mə] 
 IPA ( key ) : ( Valencia ) [saɾˈkaz.me] 
--
 Etymology
 [ edit ] 
 From French sarcasme , from Late Latin sarcasmus , from Ancient Greek σαρκασμός ( sarkasmós ) .
 Pronunciation
 [ edit ] 
 Audio : ( file ) 
 Noun
--
 Etymology
 [ edit ] 
 Learned borrowing from Late Latin sarcasmus , itself a borrowing from Ancient Greek σαρκασμός ( sarkasmós ) .
 Pronunciation
```


## [2026-10-15T02:45:44.275Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/sarcasm' 'https://en.wiktionary.org/wiki/sarcoma' 'https://en.wiktionary.org/wiki/sarco-' 'https://en.wiktionary.org/wiki/sarcastic' 'https://en.wiktionary.org/wiki/sarcology' 'https://en.wiktionary.org/wiki/σαρκασμός' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/twárštā'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 515, root Twerk: sarcasm/sarco- chain, Skt Tvastar\"); echo \"=== $u\"; grep -v '^\\s*$' $f | grep -A4 '^ Etymology$' | grep -v 'edit\\|Etymology' | head -8; done"
}
```


### [2026-10-15T02:45:53.616Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/sarcasm
 Proto-Indo-European *twerḱ- 
 Proto-Indo-European *-s 
--
 Borrowed from French sarcasme , from Latin sarcasmus .
 Noun
=== https://en.wiktionary.org/wiki/sarcoma
 From Latin sarcoma , from Ancient Greek σάρκωμα ( sárkōma ) , from σάρξ ( sárx , “ flesh ” ) +‎ -ωμα ( -ōma , “ process ” ) or from Ancient Greek σαρκόω ( sarkóō ) , itself from σάρξ ( sárx ) ; by surface analysis , sarc- +‎ -oma .
 Pronunciation
--
 Borrowed from Latin sarcoma , from Ancient Greek σάρκωμα ( sárkōma ) , from σάρξ ( sárx , “ flesh ” ) +‎ -ωμα ( -ōma , “ process ” ) or from Ancient Greek σαρκόω ( sarkóō ) , itself from σάρξ ( sárx ) .
 Noun
--
 Borrowed from Late Latin sarcōma , from Ancient Greek σάρκωμα ( sárkōma ) , from σάρξ ( sárx , “ flesh ” ) +‎ -ωμα ( -ōma , “ process ” ) or from Ancient Greek σαρκόω ( sarkóō ) , itself from σάρξ ( sárx ) .
 Pronunciation
=== https://en.wiktionary.org/wiki/sarco-
 From Ancient Greek σάρξ ( sárx ) .
 Prefix
=== https://en.wiktionary.org/wiki/sarcastic
 Proto-Indo-European *twerḱ- 
 Proto-Indo-European *-s 
--
 Proto-Indo-European *twerḱ- 
 Proto-Indo-European *-s 
=== https://en.wiktionary.org/wiki/sarcology
 From sarco- +‎ -logy .
 Noun
=== https://en.wiktionary.org/wiki/σαρκασμός
 From σᾰρκᾰ́ζω ( sărkắzō , “ to tear or lacerate ” ) +‎ -μός ( -mós ) .
 Pronunciation
--
 From Ancient Greek σαρκασμός ( sarkasmós ) .
 Noun
=== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/twárštā
 From Proto-Indo-European *twérḱ-tōr , from *twerḱ- ( “ to carve, cut off ” ) +‎ *-tōr .
 Noun
```


## [2026-10-15T02:45:57.115Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f=$(python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/sarcastic'); grep -v '^\\s*$' $f | grep -i -B1 -A3 'from sarcasm\\|French sarcastique\\|enthusiastic' | head; f=$(python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/sarcasm'); grep -v '^\\s*$' $f | grep -i 'Ancient Greek σαρκ' | head -3; ls data/verification/page-51[0-4].json 2>/dev/null; grep -n -E 'PROBLEM|def |required|must' tools/verify_check.py | head -40"
}
```


### [2026-10-15T02:45:58.123Z] TOOL RESULT

```
 French sarcasme 
 French sarcastique der. 
 English sarcastic 
 Either from sarcasm +‎ -astic or from French sarcastique , from French sarcasme , from Late Latin sarcasmus , ultimately from Ancient Greek σαρκασμός ( sarkasmós , “ sarcasm ” ) , itself from Ancient Greek σάρξ ( sárx , literally “ meat, flesh ” ) .
 Pronunciation
 [ edit ] 
 ( Received Pronunciation ) IPA ( key ) : /sɑːˈkæs.tɪk/ 
--
 French sarcasme 
 French sarcastique bor. 
 Ancient Greek σαρκασμός ( sarkasmós ) der. 
 From Late Latin sarcasmus , from Ancient Greek σαρκασμός ( sarkasmós , “ a sneer ” ) , from σαρκάζω ( sarkázō , “ to gnash the teeth (in anger) ” , literally “ to strip off the flesh ” ) , from σάρξ ( sárx , “ flesh ” ) .
(eval):1: no matches found: data/verification/page-51[0-4].json
16:def page_no(path):
20:def main(argv):
90:        print("PROBLEM:", p)
```


## [2026-10-15T02:45:59.701Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,95p tools/verify_check.py; ls data/verification/ | head"
}
```


### [2026-10-15T02:46:00.205Z] TOOL RESULT

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

Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  agent
drwxr-xr-x     - sfmqrb 14 Oct 22:34  process
drwxr-xr-x     - sfmqrb 14 Oct 22:19  sources
.rw-r--r--  9.7k sfmqrb 14 Oct 22:19  COORDINATOR.md
.rw-r--r--   89k sfmqrb 14 Oct 22:14  page-31.json
.rw-r--r--   33k sfmqrb 14 Oct 22:14  page-32.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-33.json
.rw-r--r--   85k sfmqrb 14 Oct 22:14  page-34.json
.rw-r--r--   87k sfmqrb 14 Oct 22:14  page-35.json
```


## [2026-10-15T02:46:04.306Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<33736' KLN_1966.txt | grep -c $'\\f'; ls | grep -i 'FSD\\|WEB'; grep -n -i '^sarcasm' FSD*.txt WEB*.txt 2>/dev/null | head -4; grep -n -i 'tvashtar\\|tvaṣṭ\\|tvast' SYN.txt POK_full.txt | head -3"
}
```


### [2026-10-15T02:46:04.969Z] TOOL RESULT

```
735
FSD_vol3.txt:249400:sarcasm [ Rini, t ] - antimony rubber, u variety of
POK_full.txt:87794:or z?M/5/'aA's/a/'- "creator, god, molder': Old Indie GN Tvasta{-ar-) from *Tvarstar, in addition
```


## [2026-10-15T02:46:08.822Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==736' KLN_1966.txt | grep -o -E '^[0-9]{4}|[0-9]{4}$' | head; awk 'BEGIN{RS=\"\\f\"} NR==736' KLN_1966.txt | head -3 | cut -c1-200; grep -n -i 'sarcasm' FSD_vol3.txt | head -3"
}
```


### [2026-10-15T02:46:09.313Z] TOOL RESULT

```
 ‘soap’,  which  is a  Teut.  loan  word.  See  soap.
Derivative:  saponaceous-ness,  n.
Saponaria,  n.,  a  genus  of  plants  of  the  pink  fam¬ ily  (bot.)  —  ModL.,  fr.  ML.  saponarius,  ‘per¬ taining  to  soap',  fr.  L.  sapo,  gen.  saponis,  ‘soap’ (see  saponaceous  and  -ari
76169:sharp saying, cutting remark, petty sarcasm or taunt;
123098:of sarcasm 2. 'I’o evade or shiM off os a pavmi'iit
202324:keen, racy; as, pungent sarcasm, pungent gossip. 4.
```


## [2026-10-15T02:47:17.861Z] TOOL CALL #30: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-515.py <<'EOF'\nimport json\nW='https://en.wiktionary.org/wiki/'\nPIE=W+'Reconstruction:Proto-Indo-European/twerḱ-'\nPOKq='POK_full.txt l.87790 \"Root / lemma: tuerk- / Meaning: to cut / Material: Avestan θwarəs- \\'cut, clip, schnitzend gestalten\\', participle θwarštа-, θwōrəštar- \\'creator, god, molder\\': Old Indic GN Tvaṣṭā (-ar-) from *Tvarṣṭar, in addition probably gr. σάρξ, -κός \\'flesh\\' ... σαρκάζειν \\'tear, sich auf die Lippen beißen, mock\\' ... References: WP. I 751 ... Page(s): 1102\"'\nWLDq='WLD_Bd1_pages.txt l.71143 \\'tuerk- „schneiden\". Av. θwarəs- „schneiden\" (θwarəsaiti, Ptc. θwaršta-) ... gr. σάρξ, -κός „Fleisch\", pl. „Fleischstücke\" ... Zu σάρξ auch σαρκάζειν in allen, auch der Bed. „höhnen\"\\''\nAHDq='AHD_watkins1985.txt l.1100 \"twerk-. To cut. Zero-grade form *twrk- in Greek sarx, flesh (< \\'piece of meat\\'): SARCASM, SARCO-, (SARCOMA) ... [Pok. tuerk- 1102.]\"'\nKLNq='KLN_1966.txt l.33736 s.v. sarcasm: \"F. sarcasme, fr. L. sarcasmos, fr. Gk. σαρκασμός, \\'jest, taunt, mockery\\', fr. σαρκάζειν, \\'to tear flesh like dogs; to bite the lips in rage; to speak bitterly, sneer\\', fr. σάρξ, gen. σαρκός, \\'flesh\\'. See sarco-.\"'\nKLN2='KLN_1966.txt l.33747 s.v. sarcology \"Compounded of sarco- and -logy\"; sarcoma \"Medical L., fr. Gk. σάρκωμα, \\'fleshy substance\\', fr. σάρξ, gen. σαρκός, \\'flesh\\'\"'\nSYNq='SYN.txt l.5351 (4.13 FLESH) \"2. Grk. σάρξ : Av. θwarəs- \\'cut\\', with development as in Lat. caro. Walde-P. 1.751. Boisacq 854.\"'\nIECq='IEC.txt l.19432 \"tuerK- \\'athwart, across; cross, transverse; crosscut, section\\'. Cf. WP I, 751 Av. (z-gde) θwarəs-, v. \\'resect, cut off\\'; θwarəsa, m. \\'section\\'\" -- Mann files the Avestan verb here but lists no Greek σάρξ and no Sanskrit Tvaṣṭar'\nBRTq='BRT.txt col. 795-796 (l.14392-14400) \"θwarəs- V. \\'schneiden\\' ... 1) \\'(schnitzen sva.) schneidend gestalten, schaffen, hervorbringen\\' ... PPfP. θwaršta-\"; \"θwōrəštar- m. \\'Bildner, Schöpfer\\'\" (Y. 29.6)'\nSKTq='SKT.txt l.16489 \"Sarcasm, a sneer. (F.-L.-Gk.) F. sarcasme - L. sarcasmus - Gk. σαρκασμός, a sneer - Gk. σαρκάζειν, to tear flesh, bite the lips in rage, to sneer - stem of σάρξ, flesh\"'\n\ndef rc(ref,status,note): return {\"ref\":ref,\"status\":status,\"note\":note}\ndef c(src,where,stance,note): return {\"src\":src,\"where\":where,\"stance\":stance,\"note\":note}\n\nnodes=[\n dict(id=1,lang=\"Avestan\",words=\"thwares\",verdict=\"confirmed\",\n  derivation=\"Avestan θwarəs- (Nourai's 'thwares') 'to cut, carve; fashion, create', present θwarəsaiti, ppp. θwaršta-, agent noun θwōrəštar- 'fashioner, creator'. It continues Proto-Iranian *θwarc- < Proto-Indo-Iranian *twarć- < PIE *twerḱ-: PIE *t before *w gives Iranian θ (as in θwąm 'thee' < *twām), and the palatal *ḱ gives Avestan s (satem treatment). Meaning 'cut' is primary, 'shape by carving > create' secondary.\",\n  derivation_fa=\"فعل اوستایی θwarəs- «بریدن، تراشیدن؛ شکل دادن، آفریدن» (با صفت مفعولی θwaršta- و نام‌کنندهٔ θwōrəštar- «سازنده، آفریدگار») از ایرانی باستان *θwarc- و هندوایرانی *twarć- و سرانجام از ریشهٔ هندواروپایی آغازین *twerḱ- «بریدن» است. در ایرانی، t پیش از w به θ دگرگون شده و ḱ کامی هندواروپایی (چنان‌که در زبان‌های ساتم) به s بدل شده است. بارتولومه و پوکورنی و ویکی‌واژه همگی همین را می‌گویند؛ ادعای نورایی درست است.\",\n  sources=[PIE],\n  ref_check=[rc(\"POK:1102\",\"supports\",POKq)],\n  consulted=[c(\"BRT\",\"col. 795-796\",\"supports\",BRTq),c(\"WLD\",\"Bd. I 751\",\"supports\",WLDq),c(\"IEC\",\"p. s.v. tuerK-\",\"partial\",IECq),c(\"SYN\",\"4.13 FLESH and 9.22 CUT\",\"supports\",SYNq+'; also 9.22 CUT table lists \"Av. karət-, θwarəs-\"')]),\n dict(id=2,lang=\"Sanskrit\",words=\"tvâsta, tvastar\",verdict=\"plausible\",\n  derivation=\"Vedic Tváṣṭṛ- (nom. Tváṣṭā), the divine craftsman who fashioned Indra's vajra, < Proto-Indo-Aryan *twá(r)ṣṭā < Proto-Indo-Iranian *twárštā < PIE *twérḱ-tōr 'carver, fashioner'; the cluster *-rḱt- was simplified to -ṣṭ- with loss of r in Indo-Aryan (Avestan keeps θwōrəštar-). The etymology is accepted (Pokorny, Mayrhofer, Wiktionary), but Nourai's gloss 'cut' is loose: tvaṣṭṛ means 'carpenter, fashioner, the Artificer (god)', not 'cut' (the Sanskrit verb itself, *tvarṣ-, is not attested). 'tvâsta' is a simplified transliteration of tváṣṭā (nom.), not a misreading.\",\n  derivation_fa=\"«توَشْتْر» (Tváṣṭṛ-، حالت فاعلی Tváṣṭā) در ودا نام ایزد صنعتگر و سازندهٔ گرز ایندره است و از هندوایرانی *twárštā و هندواروپایی آغازین *twérḱ-tōr «تراشنده، سازنده» برآمده؛ در هندوآریایی r از خوشهٔ -ršt- افتاده و -ṣṭ- مانده است، در حالی که اوستایی θwōrəštar- آن را نگه داشته. پیوند با ریشهٔ *twerḱ- را پوکورنی و ویکی‌واژه می‌پذیرند، اما معنای «بریدن» که نورایی آورده دقیق نیست: معنای واژه «درودگر، سازنده، ایزد صنعتگر» است. پس ریشه‌شناسی درست است و تنها معنای داده‌شده با احتیاط پذیرفتنی است.\",\n  sources=[W+'त्वष्टृ',W+'Reconstruction:Proto-Indo-Iranian/twárštā',PIE],\n  ref_check=[rc(\"POK:1102\",\"supports\",POKq+\" -- Pokorny gives the Sanskrit only as a divine name, 'creator, god, molder', not 'cut'.\")],\n  consulted=[c(\"WLD\",\"Bd. I 751\",\"silent\",WLDq+\" -- the OCR of the entry shows Av. and Greek only; no Sanskrit form legible\"),c(\"AHD\",\"Watkins 1985 p. 72 s.v. twerk-\",\"silent\",AHDq+\" -- no Indic form listed\"),c(\"IEC\",\"s.v. tuerK-\",\"silent\",IECq),c(\"SYN\",\"4.13 FLESH\",\"silent\",\"Buck cites only Av. θwarəs- with Grk. σάρξ; no Tvaṣṭṛ\")]),\n dict(id=3,lang=\"Greek\",words=\"sarkh, sarx; sarca-sein; sarcasmos\",verdict=\"confirmed\",\n  derivation=\"Ancient Greek σάρξ, gen. σαρκός 'flesh', pl. 'pieces of meat' (Aeolic σύρκες) < Proto-Hellenic *súrks/*swə́rks < PIE zero-grade s-stem *turḱ-s / *twr̥ḱ- 'a cut (piece)': *tw- > Greek s- (as in σύ < *tu), syllabic *r̥ > αρ (Aeolic υρ), *ḱ > κ (centum). Semantic shift 'a cut (of meat)' > 'flesh' (cf. Latin caro 'flesh' beside Oscan karu 'part'). From it the verb σαρκάζω 'to tear flesh like dogs; bite the lips in rage; sneer', and its action noun σαρκασμός 'sneer, mockery' (-μός). Pokorny says 'probably', Beekes 2010 (p. 1309) and Watkins accept *turḱ-; 'sarkh' and 'sarca-sein' are Nourai's transliterations of σάρξ / σαρκάζειν.\",\n  derivation_fa=\"یونانی باستان σάρξ (sarx، اضافی sarkos) «گوشت، تکه‌گوشت» از یونانی آغازین *súrks و هندواروپایی آغازین *turḱ-s با درجهٔ صفرِ ریشهٔ *twerḱ- «بریدن» است، یعنی در اصل «تکهٔ بریده‌شده». در یونانی *tw- آغازی به s- و r هجایی به ar دگرگون شده و ḱ (زبان‌های کنتوم) k مانده است؛ تحول معنایی «بُرِش» ← «گوشت» مانند لاتین caro است. از آن فعل σαρκάζω «گوشت دریدن مانند سگ، لب گزیدن از خشم، طعنه زدن» و اسم σαρκασμός «نیشخند، طعنه» ساخته شده. پوکورنی آن را «محتمل» و بیکس و واتکینز پذیرفته می‌دانند؛ ادعای نورایی درست است.\",\n  sources=[W+'σάρξ',W+'σαρκάζω',W+'σαρκασμός',PIE],\n  ref_check=[rc(\"POK:1102\",\"supports\",POKq),rc(\"KLN:1383\",\"supports\",KLNq)],\n  consulted=[c(\"WLD\",\"Bd. I 751\",\"supports\",WLDq),c(\"AHD\",\"Watkins 1985 s.v. twerk-\",\"supports\",AHDq),c(\"SYN\",\"4.13 FLESH\",\"supports\",SYNq),c(\"IEC\",\"s.v. tuerK-\",\"silent\",\"Mann's tuerK- entry lists Av. θwarəs- and Germanic 'athwart' words only; no Greek σάρξ (grep 'sarx|sark' finds nothing relevant)\")]),\n dict(id=4,lang=\"Latin\",words=\"sarcasmos\",verdict=\"confirmed\",\n  derivation=\"Late Latin sarcasmos / sarcasmus 'sarcasm' is a learned borrowing of Greek σαρκασμός, used by the Roman grammarians as a rhetorical term (a figure of bitter mockery); -os is the Greek ending kept, -us the Latinised one. Klein gives 'L. sarcasmos'; Wiktionary lists Latin sarcasmus. No sound change beyond the regular transliteration κ > c.\",\n  derivation_fa=\"لاتین متأخر sarcasmos / sarcasmus «طعنه، ریشخند» وام‌واژه‌ای ادبی از یونانی σαρκασμός است که دستورنویسان و علمای بلاغت رومی چون اصطلاحی بلاغی به کار بردند؛ صورت sarcasmos پایانهٔ یونانی را نگه داشته و sarcasmus لاتینی‌شدهٔ آن است. کلاین و ویکی‌واژه هر دو همین راه را می‌دهند؛ ادعای نورایی درست است.\",\n  sources=[W+'sarcasmus',W+'σαρκασμός'],\n  ref_check=[rc(\"KLN:1383\",\"supports\",KLNq)],\n  consulted=[c(\"SKT\",\"s.v. sarcasm\",\"supports\",SKTq),c(\"LAT\",\"s.v. sarcasmus\",\"silent\",\"Ernout-Meillet not consulted in detail for a Greek rhetorical loan; Klein and Skeat cover the link\")]),\n dict(id=5,lang=\"French\",words=\"sarcasme\",verdict=\"confirmed\",\n  derivation=\"Middle French sarcasme (16th c., Rabelais era humanist vocabulary) is a learned borrowing from Late Latin sarcasmus, with the French learned ending -isme/-asme replacing Latin -asmus (cf. enthousiasme). It passed into English in the 1570s-80s.\",\n  derivation_fa=\"فرانسوی sarcasme (سدهٔ ۱۶) وام‌واژه‌ای ادبی از لاتین متأخر sarcasmus است که پایانهٔ لاتینی -asmus در آن به -asme فرانسوی (مانند enthousiasme) بدل شده؛ از فرانسوی در سدهٔ ۱۶ به انگلیسی رسید. کلاین، اسکیت و ویکی‌واژه همین را می‌گویند؛ ادعای نورایی درست است.\",\n  sources=[W+'sarcasme',W+'sarcasm'],\n  ref_check=[rc(\"KLN:1383\",\"supports\",KLNq)],\n  consulted=[c(\"SKT\",\"s.v. sarcasm\",\"supports\",SKTq)]),\n dict(id=6,lang=\"English\",words=\"sarco-; sarcology, sarcoma, sarcasm, sarcastic\",verdict=\"plausible\",\n  derivation=\"sarcasm (1570s) < French sarcasme < Late Latin sarcasmus — exactly the chart's route. sarcastic (1690s) is either formed in English from sarcasm on the model of enthusiasm/enthusiastic, or borrowed from French sarcastique; either way it belongs here. But sarco- (combining form of σάρξ, σαρκ-), sarcology (sarco- + -logy, 18th-c. anatomical coinage) and sarcoma (17th c., Medical/Late Latin sarcoma < Greek σάρκωμα 'fleshy excrescence') did NOT pass through French sarcasme: they are direct learned borrowings from Greek σάρξ via Neo-/Medical Latin, so they should hang from the Greek node (#3), not from #5. Roots correct; the drawn route is too simplified for three of the five words.\",\n  derivation_fa=\"انگلیسی sarcasm (دههٔ ۱۵۷۰) از فرانسوی sarcasme و لاتین متأخر sarcasmus آمده و sarcastic (دههٔ ۱۶۹۰) یا در خود انگلیسی از sarcasm (به قیاس enthusiastic) ساخته شده یا از فرانسوی sarcastique گرفته شده؛ این دو درست در جای خود نشسته‌اند. اما sarco- «گوشت» (پیشوندِ ساخته از σαρκ- یونانی)، sarcology «گوشت‌شناسی، کالبدشناسی بافت‌های نرم» و sarcoma «سارکوم، غدهٔ گوشتی» (از لاتین پزشکی sarcoma و یونانی σάρκωμα) مستقیماً از یونانی σάρξ وام گرفته شده‌اند و از راه فرانسوی sarcasme نیامده‌اند. پس هم‌ریشگی همه درست است ولی مسیر رسم‌شده برای این سه واژه ساده‌سازی شده است؛ با احتیاط پذیرفتنی است.\",\n  sources=[W+'sarcasm',W+'sarcastic',W+'sarco-',W+'sarcoma',W+'sarcology'],\n  ref_check=[rc(\"KLN:1383\",\"partial\",KLNq+\"; \"+KLN2+\" -- Klein derives sarcoma and sarco- directly from Greek, not via French.\")],\n  consulted=[c(\"SKT\",\"s.v. sarcasm\",\"supports\",SKTq),c(\"AHD\",\"Watkins 1985 s.v. twerk-\",\"supports\",AHDq+\" -- lists the English words under the root without route detail\")]),\n]\nentry=dict(entry=0,root=\"Twerk, Twrk\",verdict=\"confirmed\",\n modern_form=\"PIE *twerḱ- 'to cut, carve, trim' (Pokorny tu̯erk̂- 1102; LIV² 656 *tu̯erk̑- 'schnitzen, zurechtschneiden')\",\n note=\"Pokorny 1102 tuerk- 'schneiden' (WP I 751) gives exactly Nourai's three branches: Av. θwarəs-, Skt. Tvaṣṭar (from *Tvarṣṭar) and 'probably' Gk. σάρξ with σαρκάζειν. Modern sources (LIV², Mallory-Adams, Beekes 2010, Wiktionary, Watkins) all keep the root and the Greek link. Root, language label and gloss correct. 'Twrk' is the zero grade *twr̥ḱ- (Watkins), not a different root; the redirect entry 1 is skipped.\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *twerḱ- (درجهٔ صفر *twr̥ḱ-) به معنای «بریدن، تراشیدن» در پوکورنی (ص ۱۱۰۲، tuerk-)، والده-پوکورنی (ج ۱، ص ۷۵۱)، واتکینز و فرهنگ فعل‌های هندواروپایی (LIV) آمده است. بازمانده‌های آن اوستایی θwarəs- «بریدن، آفریدن»، نام ایزد ودایی Tvaṣṭṛ «سازنده» و یونانی σάρξ «گوشت» (در اصل «تکهٔ بریده») است که واژه‌های انگلیسی sarcasm و sarcoma از آن آمده‌اند. ادعای نورایی دربارهٔ ریشه، زبان و معنا درست است.\",\n sources=[PIE],\n ref_check=[rc(\"POK:1102\",\"supports\",POKq)],\n consulted=[c(\"WLD\",\"Bd. I 751\",\"supports\",WLDq),c(\"AHD\",\"Watkins 1985 s.v. twerk-\",\"supports\",AHDq),c(\"IEC\",\"s.v. tuerK-\",\"partial\",IECq),c(\"SYN\",\"4.13 FLESH\",\"supports\",SYNq)],\n nodes=nodes)\nout=dict(pdf_page=515,book_page=485,verified_by=\"claude-opus-5.5\",verified_on=\"2026-10-14\",entries=[entry])\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-515.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\ncd /home/sfmqrb/git/rishe-private && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-515.py && python3 -m json.tool data/verification/page-515.json >/dev/null && python3 tools/verify_check.py 515"
}
```


### [2026-10-15T02:47:18.643Z] TOOL RESULT

```
nodes verified: 6/6
node verdicts: {'confirmed': 4, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 6, 'partial': 1}
books consulted: {'supports': 10, 'partial': 1, 'silent': 6} | by book: {'WLD': 3, 'IEC': 3, 'SYN': 3, 'AHD': 3, 'SKT': 3, 'BRT': 1, 'LAT': 1}
```


## [2026-10-15T02:47:21.376Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'sarcasm' LAT.txt LEW_1910.txt | head -3"
}
```


### [2026-10-15T02:47:21.972Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:47:26.571Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-515.py; python3 - \"$S\" <<'EOF'\nimport sys\np=sys.argv[1]; s=open(p).read()\ns=s.replace('\"Ernout-Meillet not consulted in detail for a Greek rhetorical loan; Klein and Skeat cover the link\"','\"grep -i \\'sarcasm\\' on LAT.txt and LEW_1910.txt finds nothing: Ernout-Meillet and Walde have no entry for this Greek rhetorical loan\"')\ns=s.replace(\"Middle French sarcasme (16th c., Rabelais era humanist vocabulary)\",\"Middle French sarcasme (16th c. humanist vocabulary)\")\ns=s.replace('\"Watkins 1985 p. 72 s.v. twerk-\"','\"Watkins 1985 s.v. twerk- (line 1100)\"')\nopen(p,'w').write(s)\nEOF\npython3 $S && python3 -m json.tool data/verification/page-515.json >/dev/null && python3 tools/verify_check.py 515 | grep -c PROBLEM"
}
```


### [2026-10-15T02:47:27.309Z] TOOL RESULT

```
0
```


## [2026-10-15T02:47:36.701Z] TOOL CALL #33: SubagentHandback

```json
{
 "message": "I wrote the page 515 file (book page 485) at /home/sfmqrb/git/rishe-private/data/verification/page-515.json. `verify_check.py 515` shows 0 PROBLEM lines and 6 of 6 nodes verified.\n\n- **Root (Twerk, PIE *twerḱ- \"to cut\"): confirmed.** Pokorny p. 1102 (tuerk- \"schneiden\", WP I 751) gives the same three branches as the chart: Avestan θwarəs-, Sanskrit Tvaṣṭar, and \"probably\" Greek σάρξ. Walde-Pokorny, Watkins and Wiktionary also keep the root and the link to σάρξ, and Wiktionary cites Beekes 2010 for it. Entry 1 (Twrk) is a redirect and was skipped.\n- **Nodes:** 4 confirmed, 2 plausible, none disputed, none `transcription_suspect`.\n  - #1 Avestan thwares, #3 Greek sarx / sarkazein / sarkasmos, #4 Latin sarcasmos and #5 French sarcasme are confirmed.\n  - #2 Sanskrit tvâsta, tvastar is plausible. The derivation from *twérḱ-tōr is accepted, but Nourai's gloss \"cut\" is loose: Tvaṣṭṛ means \"fashioner, carpenter\", the divine craftsman.\n  - #6 English is plausible. sarcasm and sarcastic do come through French sarcasme. But sarco-, sarcology and sarcoma come straight from Greek σάρξ through scientific or medical Latin, not through French, so they belong under node #3.\n- **Nourai's own references:** 6 support the chart and 1 is partial. POK:1102 supports every node it is cited for. KLN:1383 (s.v. sarcasm) supports nodes #3–#5 but is only partial for #6, because Klein derives sarcoma and sarco- directly from Greek.\n- **Other books on disk:** Bartholomae, Walde-Pokorny, Watkins/AHD 1985, Mann, Buck and Skeat. Mann puts θwarəs- under tuerK- \"athwart\" and does not mention σάρξ. Ernout-Meillet (LAT) and Walde (LEW) have no entry for sarcasmus.\n- **Extraction errors:** none. The JSON matches the chart text, and the odd spellings (thwares, tvâsta, sarkh, sarca-sein) are Nourai's simplified romanizations.\n\nAll 12 web pages cited are archived with fetch_source.py: Wiktionary, including the *twerḱ-, σάρξ and त्वष्टृ pages. The Etymonline fetches failed, so Etymonline is not cited."
}
```


### [2026-10-15T02:47:37.190Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
