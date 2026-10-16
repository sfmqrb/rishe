# Verification process log — verify-page-530


## [2026-10-16T05:13:01.887Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 530 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-530.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-530.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-530.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 530` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.957Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.266Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.287Z] TOOL RESULT

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


## [2026-10-16T05:13:05.768Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-530.txt"
}
```


### [2026-10-16T05:13:05.793Z] TOOL RESULT

```
1	=== PDF page 530 (book page 500) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Weg 2 : to be lively, strong  (refs POK:1117)
4	#1 (parent #0) [Iranian] refs=AEF:201; IEC:1499 | vâz, wâz : a root indicating power, largeness, being active or rising.
5	  #2 (parent #1) [Old Persian] refs=POK:1117 | vazraka : large
6	    #3 (parent #2) [Pahlavi] refs=HRN | vajarg, bazurk : big
7	      #4 (parent #3) [Persian] refs=BQT:272; POK:1117 | bozorg «بزرگ» : large
8	    #5 (parent #2) [Sogdian] refs=SOD:429 | wz`rk : big
9	  #6 (parent #1) [Avestan] refs=POK:1117 | vazra : a club
10	    #7 (parent #6) [Pahlavi] refs=HRN:202 | vazr : a club
11	      #8 (parent #7) [Persian] refs=BQT:1793 | gorz «گرز» : a club
12	  #9 (parent #1) [Pahlavi] refs=HUB:22; AEF:201 | vâzîtan : to rise up, be active, play ; bâxtan : to rise up, play | NOTE: HUB:22 does not accept the "bâxtan" form
13	    #10 (parent #9) [Persian] refs=AEF:201; HUB:22; IEC:1499 | bâzîdan «بازیدن» : to play ; bâxtan «باختن» : to play, also to lose in a game | extra: بازنده ، بازی
14	#11 (parent #0) [Sanskrit] refs=POK:1117 | vâja : power, to rise up
15	#12 (parent #0) [Germanic] refs=AHD | waken : wake ; wakjan : watch ; waht : wait
16	  #13 (parent #12) [English] refs=None | wake ; awake ; watch ; wait
17	#14 (parent #0) [Latin] refs=AHD | vegĕre, vîgere : to be lively ; vĕlôx : lively
18	  #15 (parent #14) [English] refs=None | vegetable ; vigor ; vigilant ; velocity
19	
```


## [2026-10-16T05:13:06.505Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-530.json"
}
```


### [2026-10-16T05:13:06.766Z] TOOL RESULT

```
1	{
2	  "pdf_page": 530,
3	  "book_page": 500,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Weg 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:1117",
10	        "gloss": "to be lively, strong"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Iranian",
17	          "refs": "AEF:201; IEC:1499",
18	          "words": [
19	            {"translit": "vâz, wâz", "gloss": "a root indicating power, largeness, being active or rising.", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Old Persian",
28	          "refs": "POK:1117",
29	          "words": [
30	            {"translit": "vazraka", "gloss": "large", "script": null}
31	          ],
32	          "note": null,
33	          "quote": null
34	        },
35	        {
36	          "id": 3,
37	          "parent": 2,
38	          "lang": "Pahlavi",
39	          "refs": "HRN",
40	          "words": [
41	            {"translit": "vajarg, bazurk", "gloss": "big", "script": null}
42	          ],
43	          "note": null,
44	          "quote": null
45	        },
46	        {
47	          "id": 4,
48	          "parent": 3,
49	          "lang": "Persian",
50	          "refs": "BQT:272; POK:1117",
51	          "words": [
52	            {"translit": "bozorg", "gloss": "large", "script": "بزرگ"}
53	          ],
54	          "note": null,
55	          "quote": null
56	        },
57	        {
58	          "id": 5,
59	          "parent": 2,
60	          "lang": "Sogdian",
61	          "refs": "SOD:429",
62	          "words": [
63	            {"translit": "wz`rk", "gloss": "big", "script": null}
64	          ],
65	          "note": null,
66	          "quote": null
67	        },
68	        {
69	          "id": 6,
70	          "parent": 1,
71	          "lang": "Avestan",
72	          "refs": "POK:1117",
73	          "words": [
74	            {"translit": "vazra", "gloss": "a club", "script": null}
75	          ],
76	          "note": null,
77	          "quote": null
78	        },
79	        {
80	          "id": 7,
81	          "parent": 6,
82	          "lang": "Pahlavi",
83	          "refs": "HRN:202",
84	          "words": [
85	            {"translit": "vazr", "gloss": "a club", "script": null}
86	          ],
87	          "note": null,
88	          "quote": null
89	        },
90	        {
91	          "id": 8,
92	          "parent": 7,
93	          "lang": "Persian",
94	          "refs": "BQT:1793",
95	          "words": [
96	            {"translit": "gorz", "gloss": "a club", "script": "گرز"}
97	          ],
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 9,
103	          "parent": 1,
104	          "lang": "Pahlavi",
105	          "refs": "HUB:22; AEF:201",
106	          "words": [
107	            {"translit": "vâzîtan", "gloss": "to rise up, be active, play", "script": null},
108	            {"translit": "bâxtan", "gloss": "to rise up, play", "script": null}
109	          ],
110	          "note": "HUB:22 does not accept the \"bâxtan\" form",
111	          "quote": null
112	        },
113	        {
114	          "id": 10,
115	          "parent": 9,
116	          "lang": "Persian",
117	          "refs": "AEF:201; HUB:22; IEC:1499",
118	          "words": [
119	            {"translit": "bâzîdan", "gloss": "to play", "script": "بازیدن"},
120	            {"translit": "bâxtan", "gloss": "to play, also to lose in a game", "script": "باختن"}
121	          ],
122	          "script_extra": "بازنده ، بازی",
123	          "note": null,
124	          "quote": {
125	            "text": "شاه دل گم گشت وچون شطرنج را شه گم شود - کی تواند باختن شطرنج را ، شطرنج باز",
126	            "poet": "Manûchehrî"
127	          }
128	        },
129	        {
130	          "id": 11,
131	          "parent": 0,
132	          "lang": "Sanskrit",
133	          "refs": "POK:1117",
134	          "words": [
135	            {"translit": "vâja", "gloss": "power, to rise up", "script": null}
136	          ],
137	          "note": null,
138	          "quote": null
139	        },
140	        {
141	          "id": 12,
142	          "parent": 0,
143	          "lang": "Germanic",
144	          "refs": "AHD",
145	          "words": [
146	            {"translit": "waken", "gloss": "wake", "script": null},
147	            {"translit": "wakjan", "gloss": "watch", "script": null},
148	            {"translit": "waht", "gloss": "wait", "script": null}
149	          ],
150	          "note": null,
151	          "quote": null
152	        },
153	        {
154	          "id": 13,
155	          "parent": 12,
156	          "lang": "English",
157	          "refs": null,
158	          "words": [
159	            {"translit": "wake", "gloss": null, "script": null},
160	            {"translit": "awake", "gloss": null, "script": null},
161	            {"translit": "watch", "gloss": null, "script": null},
162	            {"translit": "wait", "gloss": null, "script": null}
163	          ],
164	          "note": null,
165	          "quote": null
166	        },
167	        {
168	          "id": 14,
169	          "parent": 0,
170	          "lang": "Latin",
171	          "refs": "AHD",
172	          "words": [
173	            {"translit": "vegĕre, vîgere", "gloss": "to be lively", "script": null},
174	            {"translit": "vĕlôx", "gloss": "lively", "script": null}
175	          ],
176	          "note": null,
177	          "quote": null
178	        },
179	        {
180	          "id": 15,
181	          "parent": 14,
182	          "lang": "English",
183	          "refs": null,
184	          "words": [
185	            {"translit": "vegetable", "gloss": null, "script": null},
186	            {"translit": "vigor", "gloss": null, "script": null},
187	            {"translit": "vigilant", "gloss": null, "script": null},
188	            {"translit": "velocity", "gloss": null, "script": null}
189	          ],
190	          "note": null,
191	          "quote": null
192	        }
193	      ]
194	    }
195	  ]
196	}
197	
```


## [2026-10-16T05:13:14.006Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['AEF','IEC','POK','HRN','BQT','SOD','HUB','AHD','WLD','BRT','KNT','PHD','NYB','MON','ARY','CHEUNG','KLN','SKT','SYN']:\n  v=d.get(k);print(k, json.dumps(v,ensure_ascii=False)[:400] if v else None)\n\"; ls sources/refs | head -100"
}
```


### [2026-10-16T05:13:14.467Z] TOOL RESULT

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
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG None
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
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
```


## [2026-10-16T05:13:22.578Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; grep -l -E '\"(bozorg|gorz|bâzîdan)' page-*.json | head; grep -l 'wake' page-*.json | head; ls page-*.json | wc -l; ls page-52*.json page-53*.json 2>/dev/null"
}
```


### [2026-10-16T05:13:22.953Z] TOOL RESULT

```
page-184.json
page-175.json
page-270.json
page-376.json
page-409.json
page-450.json
page-95.json
page-84.json
488
Permissions Size User   Date Modified Name
.rw-r--r--   50k sfmqrb 14 Oct 22:14  page-52.json
.rw-r--r--   53k sfmqrb 14 Oct 22:14  page-53.json
```


## [2026-10-16T05:13:26.442Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'EOF'\nimport json,glob\nfor f in ['page-184.json','page-175.json','page-270.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            w=n.get('words','')\n            if any(k in w for k in ['bozorg','gorz','bâzîdan','bâxtan','vazra']):\n                print(f,e['root'],n['id'],w,n['verdict'])\n                print(' D:',n['derivation'][:600])\n                for c in n.get('ref_check',[])+n.get('consulted',[]): print('  ',json.dumps(c,ensure_ascii=False)[:400])\n                print(' S:',n.get('sources'))\nEOF"
}
```


### [2026-10-16T05:13:26.872Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:13:29.390Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; grep -o -E '.{0,100}\"(bozorg|gorz|bâzîdan)[^\"]*\".{0,50}' page-184.json page-175.json page-270.json | head; python3 -c \"\nimport json;d=json.load(open('page-501.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:5000])\""
}
```


### [2026-10-16T05:13:32.472Z] TOOL RESULT

```
ugrep: error: error at position 404
\xbf][\x80-\xbf]*){0,50}
                        \___exceeds complexity limits


{
 "entry": 0,
 "root": "Ten 1, Tengh, Temp",
 "verdict": "confirmed",
 "modern_form": "PIE *ten- 'to stretch' (Pokorny 1. ten- 1065-1066; LIV 626 f.), with the enlargements *tengʰ- 'to pull, draw' (Pokorny 1067; Cheung *θanǰ) and *temp- 'to stretch' (Pokorny 1064; Watkins temp-)",
 "note": "The root box is correct: Pokorny p.1064 has 'temp- to extend, stretch, span; Note: extension from *ten-', p.1067 'tengh- to extend, stretch, span; Aryan *thengh-, yet probably extension from ten-1', and pp.1065-1066 the base '1. ten-, tend- to extend, stretch'. Nourai's citation POK:1064,1067 covers the two enlargements; the base is on p.1065. Watkins (AHD) lists ten- and temp- with exactly Nourai's English outcomes (SITAR under ten-, TAFFETA and TAPESTRY under temp-). Problems lie in individual branches: (1) Av. tauruna- 'young' (#8) belongs to a different root, PIE *ter-/teru- 'tender, weak' (Pokorny 1070-1071, Mann teren-, Klein s.v. tender), so the tar/tarāneh/tūleh/tūrah branch does not belong under Ten; (2) Greek kithara (#14) is not from Persian tār/si-tār — it is a Pre-Greek word attested from Homer (kitharis), centuries before the Persian si-tār, although Klein (whom Nourai follows) writes 'Gk. kithara, fr. Pers. sihtār'; (3) English tape is a native Old English word (tæppe), not from the Persian/Greek carpet word; (4) Persian tābīdan 'twist' comes from the *temp- enlargement (Iranian *tāp-), not from Av. tan- as drawn; (5) hanjār 'path, norm' has no secure link to *θanǰ (Wiktionary: from Parthian anjār 'behaviour'; Mo'in compares Skt saṃcāra). The Avestan 'tathra' and 'thri-thatra' are not attested: the first is the reconstructed *tąθra- of Horn and Pokorny, the second appears to be Nourai's own back-projection of si-tār. The JSON matches the printed page (checked against the page image), including the inconsistent spellings tathra / thri-thatra and the reference 'KLN:572', which is a misprint in the book for KLN:1572 (tapestry). No extraction errors.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *ten- «کشیدن، کش دادن» (پوکورنی ۱۰۶۵–۱۰۶۶) و دو گونهٔ گسترش‌یافتهٔ آن، *tengʰ- «کشیدن، بیرون کشیدن» (پوکورنی ۱۰۶۷) و *temp- «کش دادن» (پوکورنی ۱۰۶۴)، درست آمده است و واتکینز نیز همین سه را با sitar و taffeta و tapestry آورده است؛ پس سرریشهٔ نورایی درست است. ایراد در چند شاخه است: «تئوروونه» (tauruna) اوستایی به معنای «جوان» از ریشهٔ دیگری (*ter- / *teru- «نرم، نازک») است، نه از *ten-؛ «کیثارا»ی یونانی از «سه‌تار» فارسی نیست و پژوهش امروزی آن را واژه‌ای پیشایونانی می‌داند؛ tape انگلیسی واژه‌ای بومی است؛ «تابیدن» از ستاک ایرانی *tāp- (گونهٔ *temp-) است نه از tan- اوستایی؛ و پیوند «هنجار» با *θanǰ ثابت نیست. «tathra» و «thri-thatra» در اوستا گواهی نشده‌اند و بازسازی (یا ساختهٔ خود نورایی) است. خطای استخراج دیده نشد؛ «KLN:572» در خود کتاب چاپ شده و خطای چاپی به جای ۱۵۷۲ است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temp-"
 ],
 "ref_check": [
  {
   "ref": "POK:1064",
   "status": "supports",
   "note": "POK_full.txt line 85474 ff. (Page(s): 1064-1065), 'Root / lemma: temp- Meaning: to extend, stretch, span; Note: extension from *ten- ds.; Material: Npers. tāb-ad, Inf. tāftan and tāb-ī-dan \"drehen, spinnen\" ... (from one to *tap = Indo Germanic *tmp- ...), wherefore probably as Iran. loanword gr. tapēs, tapis \"cover, rug\"'."
  },
  {
   "ref": "POK:1067",
   "status": "supports",
   "note": "POK_full.txt line 85513 ff. (Page(s): 1067), 'Root / lemma: tengh- Meaning: to extend, stretch, span; Note: Aryan *thengh-, yet probably nevertheless extension from ten-1; Material: Avestan θang- (θanjasante, θanjayente, participle θaxta-) \"ziehen, Bogen spannen\"'. The base 1. ten- itself is on pp.1065-1066 (line 85746), not cited by Nourai but consistent."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I pp.~721-725 (WLD_Bd1_pages.txt leaves 729-730)",
   "stance": "supports",
   "note": "temp-: 'npers. tāb-ad Inf. tāftan und tāb-ī-dan \"drehen, wenden, spinnen\" ... (aus einem zu *tap = idg. *tmp- analogisch gebildeten Kaus. *tāpayati), wozu wohl als iran. Lw. ...'; ten-: 'tantra-m \"Zettel, Aufzug am Webstuhl\" = np. tār (av. *taθra-) ds.' (grep 'tab-ad', 'tantra')."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, roots temp- and ten- (AHD_watkins1985.txt line 1079-1080)",
   "stance": "supports",
   "note": "temp-: '... TAFFETA; b. Iranian *tap-, \"carpet,\" in Greek tapēs, carpet: TAPESTRY. [Pok. temp- 1064.]'; ten-: '4. Suffixed form *ten-tro- in Persian tār, string: SITAR ... [Pok. 1. ten- 1065.]'."
  },
  {
   "src": "IEC",
   "where": "Mann col. ~1378-1379, s.v. ten- (2), tempó (2)",
   "stance": "supports",
   "note": "'ten- (2) radical: \"stretch; spread; thin\"'; 'tempó (2) \"stretch, pull\" ... Li. tempiù, tępti \"stretch, pull, drag\"'. Mann files Av. tauruna- under a separate 'teren- (terun-) \"weak, tender
```


## [2026-10-16T05:13:35.263Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Root / lemma: (u̯eg|weg|ueĝ|u̯eĝ)' POK_full.txt | head; grep -n 'Page(s): 1117' POK_full.txt | head"
}
```


### [2026-10-16T05:13:35.628Z] TOOL RESULT

```
89087:Page(s): 1117-1118
```


## [2026-10-16T05:13:37.361Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89060,89130p POK_full.txt"
}
```


### [2026-10-16T05:13:37.698Z] TOOL RESULT

```
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

Meaning: wet; to irrigate; ox (?) 

Material: Gr. uYp6(; 'humid, wet, fluid'; Latin Jiz/io'^s 'humid, wet, damp' (out of it udus, 

whereof OiTgo'd\e natijrliche dampness of Bodens'), uvor, -oris' dampness, damp ', 



uvesco, -e/"© "humid, wet become, sich betrinken', Ji/e/7s "humid, wet, damp' (place a 
*Ji/c»sfrom *J^"'c»-s ahead); umeo, -eAe "humid, wet sein', umor^ dampness ', umecto 
"befeuchte' (based on auf *ug"'smos)\ Middle Irish fuar urine ' {*uog"-lo-)\ 

Old Icelandic vgkr{f\Vk. vgkuan) "humid, wet', vgkvixw., vgkvat " damp ', wherefore Old 
Icelandic v0kva, i/e/rA/a "(blood) shed, flow let', vgkt {*vakvd) "offene (nasse) place in 
Else', Middle Low German wakei. "hole in Else', Dutch M/a/r"humid, wet, damp', engl. 
(from dem Nord.) bya/re"Kielwasser'; 

5-Erweit.: Old Indie ^/rsa// "befeuchtet, besprengt', Avestan i/A'SKe///"spruht' (of water 
and fire); common Old Indie -gh- > -ks- : Avestan -gh- > -xs- 

in addition (with the same Verhaltn. as Old Indie vrsan- "virile', Latin verres:0\6 Indie 
i/a/'S5-/77"rain', s. uer- "feuchten') Indo Germanic ulcsen-^ buW, Tiermannchen' in: Old Indie 
uksam., Avestan uxsan- "bull' (in addition? fem. *uk"sdr^6\e Besprengte' > Latin uxor 
"wife'); cymr. ych^ox' (= Indo Germanic *uk"sd, urbrit. *uchu> -/" with umlaut yc/?), PI. 
mcymr. ychen, ncymr. ychain, bret. ouhen, oc'hen, corn. 0/75/7 "Ochsen', Middle Irish oss 
"deer'; PN Os-C5/'"hirschliebend', Demin. 0/ss//7"0ssian'; Gothic auhsus {Gen. PI. 
auhsne). Old Icelandic oxi. Old English oxa. Old High German Old Saxon 0/750 "ox'; 
Tocharian B oAso "rother, cattle, bull'. 

Maybe zero grade in alb. {*oxa) ka'ox', {*ox/e) qeP\. "oxen'. 

References: WP. I 248 f., WH. II 815, 849, Mayrhofer 1 , 98. 
Page(s):1118 

Root / lemma: ueib- 
See also: see below ue/p- 
Page(s):1124 

Root/ lemma: ueti'^-, uii'^-
```


## [2026-10-16T05:13:39.657Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89035,89062p POK_full.txt"
}
```


### [2026-10-16T05:13:40.085Z] TOOL RESULT

```
Geratewohl dransetzen, venture, n'sK), Old Saxon waga^\av\x\ Old English w^g, waege 
'Wage, a certain weight '; 

Lithuanian vezu, i/ez// "drive', vezimas^ cart', i/eze'Wagengeleise', p/'ai/eza 
'Wagengeleise'; Old Bulgarian vezg, i/esZ/'vehere', veslo^ ru66er ' {*uegh-s/o-), vozb' 
cart', vozg, i/oz/// "drive, guide, lead'; also Old Russian i/eza 'Wohnwagen, tower'. 

References: WP. I 249 f., WH. II 742 f., 744, Trautmann 356 f., Vasmer 1, 178 f. 
Page(s): 1118-1120 



Root / lemma: ueg- 

Meaning: fresh, strong 

Grammatical information: stative verb uege- 

Material: Old Indie vaja- m. " power, quickness, contest, price of the battle, cut-throat price 

', vaJayati^reQi an, treibt an, lauft urn die Wette'; vajra-m. 'thunderbolt, club, mace, joint' = 

Avestan vazra- 'club, mace, joint'. Old pers. vazrka-, npers. buzurg^b\Q, large', derivative 

from *uazarn.; 

Latin veged, -ere 'bin alert, awake, smart', trans, 'errege', i//g//' watchful, wakeful' and 
'Wache, Wachter' {*vegilis), thereafter vigilare^ awake sein'; vegetus^ strenuous, alert,
```


## [2026-10-16T05:13:46.844Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^weg|weg-\\.|VELOCITY|VEGETABLE' AHD_watkins1985.txt | head -20"
}
```


### [2026-10-16T05:13:47.247Z] TOOL RESULT

```
1121:weg:'
1130:weg-'. To weave a web. Related to wokso-. Suffixed
1131:weg-?
1132:form *weg-slo- in Latin vélum, a sail, curtain, veil: VEIL, VELUM, VEXILLUM, VOILE; REVEAL. [Pok. weg- 1117.] weg-2. To be strong, be lively. 1. Suffixed o-grade form *wog-é- in Germanic *wakén in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE}. 2. Suf- fixed o-grade form *wog-no- in Germanic *waknan in Old English wecnan, wecnian, to awake: WAKEN. 3. Germanic *wakjan in Old English weccan, to be awake: WATCH. 4. Germanic *wahtwo in Old High Ger- man wahta, watch, vigil, in dialectal German beiwacht, supplementary night watch: BIvouac. 5. Germanic *waht- in: a. Old North French waitier, to watch: WAIT; b. Middle Low German wachten, to watch, guard: WAFT. 6. Suffixed (causative) o-grade form *wog-eyo- in Latin vegére, to be lively: VEGETABLE. 7. Suffixed (stative) form *weg-é- in Latin vigére, to be lively: vicor. 8. Suf- fixed form *weg-eli- in Latin vigil, watchful, awake (> vigilare, to watch, be awake): VEDETTE, VIGIL, (VIGI- LANT), VIGILANTE; REVEILLE, SURVEILLANT. 9. Suffixed form *weg-slo- in Latin véldx, fast, “lively”: VELOCITY. [Pok. weg- 1117.] wegh-. To go, transport in a vehicle. 1. Germanic *wegan in Old English wegan, to carry, balance in a scale: WEIGH}. 2. Germanic lengthened form *wég-6 in Old English wég(e), weight, unit of weight: WEE. 3. Suffixed form *wegh-ti- in Germanic *wihti- in Old English wiht, gewiht, weight: WEIGHT. 4. Germanic *wegaz, course of travel, way, in Old English weg, way: WAY; ALWAYS, (Away). 5. Suffixed form *wogh-no- in Germanic *wag- naz, vehicle, in: a. Old English we(g)n, wagon: WAIN; b. Middle Dutch wagen, wagon: WAGON. 6. Suffixed o-grade form *wogh-lo- in: a. Germanic *waglaz in Old Norse vagl, chicken roost, perch, beam: WALLEYED; b. Greek okhlos, populace, mob (< “moving mass’): OCHLOCRACY, OCHLOPHOBIA. 7. Distantly related to this root are: a. Germanic *wag-, “to move about,” in (i) possibly Middle English waggen, to wag: wac! (ii) Old High German waggo, wacko, boulder rolling on a river- bed (> German Wacke, boulder): GRAYWACKE; b. Ger- manic *wéga-, water in motion, in Old Italian vogare, to row: VOGUE; c. Germanic *wig- in (i) Old English wicga, insect (< “thing that moves quickly”): EARWIG (ii) Middle Dutch and Middle Low German wiggelen, to move back and forth, wag: WIGGLE. 8. Basic form *wegh- in Latin vehere (past participle vectus), to carry: VECTOR, VEHICLE; ADVECTION, CONVECTION, EVECTION, INVEIGH. 9. Suffixed basic form *wegh-yd in Latin via, way, road: FOY, VIA, VOYAGE; CONVEY, DEVIATE, DEVIOUS, (ENVOI), ENVOY!, OBVIOUS, PERVIOUS, PREVIOUS, (TRIVIAL), TRIV- IUM, (vIADUCT). 10. Suffixed form *wegh-s- in Latin vexdre, to agitate (< “to set in motion”): VEX. 11. Prob- ably suffixed form *wegh-so- in Latin convexus, “carried or drawn together (to a point),” convex (com-, together; see kom): CONVEX. [Pok. vegh- 1118.] weg-. Wet. 1. Germanic *wakw-6 in Old Norse vdk, a crack in ice (< “wet spot’): WAKE?. 2. Suffixed zero-grade form *ug’-sm- in: a. Latin (hjiimére, to be wet: HUMECTANT, HUMID; b. Latin (hj)iimor, fluid: HU- mor. 3. Suffixed zero-grade form *ug’-ro- in Greek hugros, wet, liquid: HYGRO-. 4. Regarded by some as an extended form of this root (with the meaning “the impregnator”), but probably a distinct Indo-European word, is *uk”s-en-, bull, ox, in Germanic *uhs6dn- in: a. Old English oxa, ox: 0x; b. Old High German ohso, ox, in German Aurochs, aurochs: AUROCHS. [Pok. uweg#- 1118.] weg”h-, Also eug’h-. To preach, speak solemnly. Suf- fixed o-grade form *wog’h-eyo- in Latin vovére, to pledge, vow: VOTARY, VOTE, (VOTIVE), VOW; DEVOTE, (DEvouT). [Pok. ewegvh- 348.] wei-'. Also weie-. To turn, twist; with derivatives refer- ring to suppleness or binding. I. Form *wei-. 1. Germanic suffixed form *wi-ra-, *wé-ra- in Old English wir, wire: WIRE. 2. Probably suffixed Germanic form *wai-ra- in
2447:VARY wer-? VASSAL upo vaT ped-2 vaTic wet-1 VAULT! wel-3 VAULT2 wel-3 VAUNT eu-2 VEAL wet-2 VECTOR wegh- VEDA weid- VEDANTA ant- VEDETTE weg-2 VEER2 per! VEGETABLE weg-2 VEHICLE wegh- VEIL weg-! VELDT pele-2 VELIGER gerere VELLEITY wel-2 VELOCITY weg-2 VELOURS wel-4 VELUM weg-1 VELVET wel-4 VENAL wes-1 VENATIC wen-1 VEND d6-, wes-! VENDETTA deik- VENEER per! VENERATE wen-! VENEREAL wen-! VENERY! wen-1 VENERY2 wen-! VENIAL wen-! VENIRE gWa- VENISON wen-! VENOM wen-! VENT wé- VENTAIL wé- VENTER udero- VENTILATE weé-
```


## [2026-10-16T05:14:03.473Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'b[aā]x(tan|t)|b[aā]z[iī]dan' CHEUNG.txt | head -20"
}
```


### [2026-10-16T05:14:04.048Z] TOOL RESULT

```
1451:*MISC: Arab. (LW) baxt ‘luck’, bagt ‘incident, occasion’ (< WIr.), waqt ‘time’ (< 
2485:*bxšyhyd, 3р1. MMP “’bxsyhynd; Partic.: pres. MMP bxš’g, perf. pass. BMP bht /baxt/, MMP bxsyhyst || 
24370:baxtoyd ‘to flow down’ (-X- < ?) || (+ *abi-) Sh. vidäj-/vidüyd ‘to irrigate’, Sh. (Baj.) 
27892:*NWIR: Widely attested: NP bazidan/baz-, vazidan/vaz- ‘to blow (as the wind)’ 
28008:*NWIR: NP bazidan/baz-, Khuns. baz-/bat (LW) ‘to play’, NP baxtan/baz-, Tt. (Cha.) 
40811:bazidan/baz-, 431 
40825:baxtan/baz-, 433 
40829:bazidan/baz-, 433 
50001:baxtoxs-/baxtoyd, 373 
54989:baxt, 2
```


## [2026-10-16T05:14:07.406Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27980,28030p CHEUNG.txt"
}
```


### [2026-10-16T05:14:07.887Z] TOOL RESULT

```
*ui(H)z ? 433 


Pres. athem.: IND. 1pl. YAv. uzamöhi (Y 65.1). 0 On the analysis of this (hapax) form see Kümmel, l.c. 
490. 


*SOGDIAN: (+ *api-) MSogd. ’ywp’zky’ ‘guesthood’ (< metathes. *api-uazaka°) 
*CHORESMIAN: (+ *api-) bw’zk, bw’zyk (m.) ‘guest’ (Benzing 1983: 181 f.) 

*NEIR: (+ *ui-) Oss. І. wazeg, D. iwazag ‘guest’ (not from *yaz) 

*SANSKRIT: vah ‘to respect; [med.] to acknowledge’ || (+ *api-) ‘to respect, honour’ 
= EWAia: — 

0 On Ir. *uäz', Skt. vah see Insler 1996: 169 ff. and Kümmel 2000: 488 ff. On the Ir. 


(Sogd., Chor. and Oss.) continuations of *uaz' see Schwartz 1990: 200 ff. 
*REFERENCES: Abaev, Slovar’ IV: 60 f. 


*uaz? ‘to play, contend; [pass. ?] to lose (in games)’ 

*MIDDLE PERSIAN: ВМР w'c- / waz-/ ‘to play’, BMP w’cyk /wazig/ ‘game, play’ 
Partic.: perf. pass. BMP w’cyt/wazid/; Inf.: BMP w'cytn /wazidan/ 

*NWIR: NP bazidan/baz-, Khuns. baz-/bat (LW) ‘to play’, NP baxtan/baz-, Tt. (Cha.) 
vaz/vast, Gz. vaz-/vaza, vaZ-/vaZa ‘to lose (in game)’, Varz. vazä/väz- ‘to lose’, NP 
Балх ‘play’, Kurd. (Kurm.) baz (Ё), (Ѕог.) bazi (LW), Gz. vazi, Khuns. vazi ‘play’, ? 
Bal. ba(y) da- ‘to give up, lose’ (< Pash. ?) 

*NEIR: ? Pash. bay ‘loss (at play)’, baylal ‘to lose (in game)’ (-y- < ?) 

*SANSKRIT: vaja- (m.) ‘contest, decisive battle, war, prize, booty, gain, reward’ 
(RV+) > EWAia II: 540 

0 Skt. vaja- does seem to have exact Ir. correspondences, which have not been 
recognised by Mayrhofer, EWAia, lc. et al. The generally assumed connection 
between Skt. väja- and vàjáyati ‘incites’ (Lat. uegére ‘to incite’, Goth. uswakjan ‘to 
arouse, awaken’, etc., Pokorny, Le: LIV: 660 f.) can now be doubted with the 
equation of the Ir. forms with vaja-: the Ir. forms are semantically irreconcilable 
with the strong, awake root *ueg-. The noun *uäza- / Skt. vaja- may be a blend of 


*yan / Skt. van ‘to win’ and *Haz / aj ‘to drive’ (cf. Skt. aji- m. ‘contest, race’). 
*REFERENCES: Horn 1893: 35; Yarshater 1969: 183; WIM I: 66, 387; WIM II/1: 85; WIM II/2: 750; 
Vahman-Asatrian 1991: 81; Cabolov 2001: 161; Lecoq 2002: 135; NEVP: 16
```


## [2026-10-16T05:14:12.267Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'buzurg|gurz|bäzïdan|bazidan|bāzīdan|bâzîdan|baxtan|bäxtan|bāxtan' HRN.txt | head -30; echo ===; grep -n -E 'buzurg|gurz|bāzīdan|bäzïdan|baxtan|bāxtan|wazr|vazr' HUB.txt | head -30"
}
```


### [2026-10-16T05:14:12.763Z] TOOL RESULT

```
Exit code 1
2256:214. buzurg 'gross'.
7861:906. ffuri^j gurze 'Keule', arab. LW. jurz,
10730:cend^ göyed ze/nfhä-yt gurz-l sän
(eval):1: == not found
```


## [2026-10-16T05:14:15.656Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2256,2270p HRN.txt; echo ...; sed -n 7861,7872p HRN.txt; echo ...; grep -n -E '^1?[0-9]+\\. +b[aä]z' HRN.txt|head; grep -n -i -E 'b.z.dan|b.xtan' HRN.txt | head"
}
```


### [2026-10-16T05:14:16.062Z] TOOL RESULT

```
214. buzurg 'gross'.
mäz. bazarg.
*) Kä§. hürndn etc. haben secundär wieder das alte rn des Praesens
erhalten; dialektisch findet sich die Überführung in die neunte Klasse
häufig (vergl. Fr. Müller SWAW. Vol. XLV, 1864, Seite 283, Hern,
KZ. 32, 580 No. 6).
*) Bartholomae setzt Studien II, 107 Anm. 4, 180 die Wurzel
als hha^r- an, woraus hhrl- eine 'Weiterbildung' sei.
') Nach Nöldeke, Beiträge zur Geschichte des Aloxander-
romans, Denkschr. der Wiener Akad. , Band 38, Iß, ist np. x^rhitz
*Eselsziege' nach einem gr. ^ovorqayo^ gebildet.
Hörn, Grundriss d. neup. Etymologie. 4— 50 -
ap. vazarka- gross*; phlv. vajarg (Bund., zu lesen
vazarg), vacurg (Men., zu lesen vaziirg),
215. bezni *Fest'.
...
906. ffuri^j gurze 'Keule', arab. LW. jurz,
aw. vazra- 'Keule ; phlv. vazr, arm. LW. varz; ai.
vdjra- ^Donnerkeil (Indra's)'.
wa;^. LW. gilrz,
906^** ger^män (falsch kerzman) Himmel'.
V
aw. garö demmia-^ garö nmäna- (S alemann, SF,
pag. 99»; dann auch Fr. Müller, WZKM. 5, 187, der
arm. LW. gerezman 'Grab' Gruft, Friedhof dazu stellt).
907. {\)gtir8 'Hunger, gursene, gursenegt; gtcsne, n22/}^
(Js. 8, 4), ^r:i'^i: (Js. 5, 13).
g. vasne, vasnegi; Kä§. ves, vesd, vesS, vesegl.
...
1821:1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
```


## [2026-10-16T05:14:20.353Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'spielen' HRN.txt | head; grep -n -i 'spielen' HUB.txt | head"
}
```


### [2026-10-16T05:14:20.669Z] TOOL RESULT

```
400:(in Muhammed Ja'far Qarajadäyl^s Lustspielen, z. B. öfter im
1716:[/150. hätten 'spielen , Praes. baz-em, bozl ('Spiel*).
1718:ai. vergl. vdja-^ väjäyati (spec. von Kampf spielen) 2);
1724:af/. bOelal 'verspielen, verlieren ; bei. gväzi 'Spiel*
526:haz^. *Spier), also = Masselbe Spiel spielend'. Dagegen
528:spielen*, bdzi 'Spiel' zu geh5ren, sondern kann z. B.
3614:schlagen'? Es bedeutet ein Instrument spielen (oder
5424:§ 44. Ap. t; = np. 6 : haxtan 'spielen', phi. vazUan
6686:spielen. Im Phi. erscheint hier stets t^ ebenso im Armeni-
6890:eine so grosse Ajizahl von Beispielen sicher gestellt, dass
8344:In den voranstehenden Beispielen steht xs immer nach
```


## [2026-10-16T05:14:24.312Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1714,1735p HRN.txt; echo ====; sed -n 5415,5435p HUB.txt; echo; sed -n 520,532p HUB.txt"
}
```


### [2026-10-16T05:14:24.617Z] TOOL RESULT

```
Exit code 1
rückwärts gelegen*. Die Erklärung aus apa-\-aytara'
(vgl. No. 66) ist falsch.
[/150. hätten 'spielen , Praes. baz-em, bozl ('Spiel*).
g. vä/ten; Käs. vözt.
ai. vergl. vdja-^ väjäyati (spec. von Kampf spielen) 2);
phlv. baj^tan, bä/t 'er erhob sich' (kräftig, schnell),
Bund. 8, 2 (Diese Anwendung von phlv. ba/tan erklärt
sich aus der ursprünglichen Bedeutung 'seine Kraft,
Behendigkeit entfalten*; np. bäxten soll auch 'tanzen*
bedeuten).
af/. bOelal 'verspielen, verlieren ; bei. gväzi 'Spiel*
(149).
Dialektisch (Kasan) finden sich die Analogiebildungen
dervösUn, dervdst (Inf.).
151. {i)bäd 'Wind*,
g. vad; Käs. vöd, vöi; mäz. va.
aw. väta- 'Wind*; phlv. vüt; ai. väta-,
kurd. ha, wäi; afy. vö; oss. t. wäd, vad (69); bei.
gvät, n. gvä&, gväs (148).
152. {lyhäd '-geschützt* (Comp.),
aw. pata- geschützt; phlv. -patx skr. patd-.
153. hädreng 'Citrone*.
(eval):1: === not found
```


## [2026-10-16T05:14:27.898Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 515,535p HUB.txt; echo =====; sed -n 5420,5430p HUB.txt"
}
```


### [2026-10-16T05:14:28.351Z] TOOL RESULT

```
Exit code 1
sprochen wurde. War ap. w ein reducierter Nasal?
Vgl. Brugmann, griech. Gram.* p. 40.
109. Np. utned {umm&d, OmSd) 'Hoffnung (afgh. umTd mit
i bei Raverty) = paz. DmBd u. s. w. bleibt trotz
') Ausgenommen ist die Partikel ham in Comp. (wie hamhasm,
hamhistar u, s. w.). Darflber im zweiten Teil unter m.
Hubschmann^ Persische Studien.- 18 -
aller Erklarungsversuche noch vollkommen dunkel.
Ap. Grundform *avamaiti-, zd. *avama^ti'?
110. Np. hamhd^ nach Zenker = 'Mitspieler ist gebildet
aiis ham 'derselbe' = ap. hama- und "^baz ^SpieF (vgl.
haz^. *Spier), also = Masselbe Spiel spielend'. Dagegen
braucht anhdx 'Genosse, Theilhaber nicht zu baxtan
spielen*, bdzi 'Spiel' zu geh5ren, sondern kann z. B.
zu skr. bhaj *Antheil geben, Antheil erhalten' (vgl.
'bhdjin theilhaftig*), zd. baz 'zutheilen* gehoren. Das
anlautende an- ist regelrecht aus ap. ham vor Ver-
schlusslauten entstanden (siehe den zweiten Theil
unter m),
114. Hier fehlt zd. hanjamana- *Versammlung'.
115. Trotz Horn's Hinweis auf ctdan = Wnmeln, lesen,
(eval):1: ==== not found
```


## [2026-10-16T05:14:32.137Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5418,5432p HUB.txt; echo '---'; grep -n -E 'Persische Studien.- 2[1-3] -' HUB.txt"
}
```


### [2026-10-16T05:14:32.457Z] TOOL RESULT

```
Kapitel 9: np. v.
§ 43. Ap. V (= idg. v) bleibt im Anlaut vor Vokalen
als V im Phi. und Paz. und wird im Np. vor a, a, e, i und
iy zu bj wahrend anl. v im Paz. und Np. vor u zn g wird
(paz. np. gu' aus *vu = ap. vi- ; paz. np. gur- aus *vwr =
ap. Vf = v'r^),
§ 44. Ap. t; = np. 6 : haxtan 'spielen', phi. vazUan
(oben p. 22), bal. gvazi; bad *Wind* = paz. vad Min. 61.
212, zd. vdta-; bddrang 'Citrone =^ phi. vatrang\ badam
*Mander, sTvend. vayam^ skr. vatama-; baran *Regen' =
paz. varan Min. 61. 212, zd. vara- ; bara 'Mauer , zd. vara-
in pairivara-; bazar *Markt' = paz. vazar Shk. 272, phi.
^) Also ap.
va-
— np. 6a-,
---
```


## [2026-10-16T05:14:34.976Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Studien.{0,4}- ?2[0-3] ?-|^- 2[0-3] -' HUB.txt | head; grep -n -i -E 'v.z.tan|vazitan|vazidan' HUB.txt | head"
}
```


### [2026-10-16T05:14:35.293Z] TOOL RESULT

```
6816:paivazidan
```


## [2026-10-16T05:14:38.009Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *150\\.' HUB.txt | head; grep -n -E 'baxtan|bäxtan|bdxtan|b.xtan' HUB.txt | head"
}
```


### [2026-10-16T05:14:38.276Z] TOOL RESULT

```
673:150. Wenn bal. gvdzl 'Spiel' (niir bei Pierce) — np. hazl^)
527:braucht anhdx 'Genosse, Theilhaber nicht zu baxtan
5466:zd. vahista-; bayo *Braut', skr. vadhu; bBxtan 'sieben = paz.
10325:baxtan 22.
```


## [2026-10-16T05:14:40.106Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 665,690p HUB.txt"
}
```


### [2026-10-16T05:14:40.388Z] TOOL RESULT

```
p. 190.
^) Nur in Compositen, deren urspriingliche Bedeutung Tergessen
war, h&tte upa- zu ba- werden konnen. Daraus konnte sich aber koin
selbstSndiges ba entwickeln.
') Man beachte, dass im Paz. nur pa, pad, nicht aber ato (= upa)
als selbstandige Praeposition Torhanden ist.
*) Das Wb. fiihrt auoh badid auf, zu dem jiid. tat. wedi', wedif'
(Miller p. 59-60) stimmt.~ 22 -
150. Wenn bal. gvdzl 'Spiel' (niir bei Pierce) — np. hazl^)
zuverlassig ist, so muss vCLz (mit z aus g^) als iranische
Wurzel angesetzt und np. hdxtati (statt *hastan) als
Analogiebildung nach afrdzam : afrdxtan etc. aufgefasst
werden. Dann ware im Phi. mzitan (nicht vajUan
oder vacUan)^) zu lesen, vgl. Matikan i catrang § 21,
p. 5, Z. 15, und die Dialectformen vonKasan wie dervostdn
(Shuk. p. 66) waren urspriinglich. Horn's Bemerkun gen
sind falsch.
153. Das armenische Wort ist modern und badrinj zu
sprechen, geh5rt also hierher. Als np. Nebenformen
von bddrang nennt Vuller's noch vOrang (= maz.
vareng) und bdlang. Die Bedeutung ist nicht nur
'Citrone' (Citronat-Citrone) sondem auch 'species cucu-
meris', vgl. afgh. LW. badrang a kind of cucumber*.
Im Altarmenischen klingt varung *Gurke, Citrone,
Herbstfrucht' an, differirt aber lautlich stark von phi.
vcUrang.
```


## [2026-10-16T05:14:44.384Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(wuzurg|wazr|wāz|gurz|wazurg)' PHD_mackenzie.txt | head; grep -n -E 'wuzurg|wazr\\b|wāzīdan|wāzīg|gurz' PHD_mackenzie.txt | head -20"
}
```


### [2026-10-16T05:14:44.788Z] TOOL RESULT

```
5306:wazr [wzl] = ~warz.
5519:wuzurg [LBA < Arb'; wc(w)lg I M wzrg, N buzurg] big, great.
9423:wuzurg   I
9425:wuzurgihI                  ~J           ul l                     ~
9427:wuzurg-framadar \ , . .   ~ Q) ~        ulihI
10144:wazr                      '\5,      wahmiin\ wan, win                 \\\
5219:3warz [wlz I N gurz] club, mace.
5306:wazr [wzl] = ~warz.
5519:wuzurg [LBA < Arb'; wc(w)lg I M wzrg, N buzurg] big, great.
5521: wuzurg-fram.iidiir [LBA plm)t)l] prime minister.
6027: bear (v.) burdan; ,..., offspring zadan,    big wuzurg, stabr.
6210:club gad, warz, (wazr); bearing a -      completeness hangirdigih, spurrigih.
6700:giving dahisn.                                great meh, wuzurg.
6703:gleam bdzidan.                                greatness wuzurgih.
7004:liquid susar.                            mace gad, warz, (wazr).
7093:minister dastwar; prime ...... wuzurg-         mouse musk.
7351:prime minister wuzurg-framadar.                   pasbanih, pust, pustibanih, sray-
7609:size wuzurgih, zaha, zahih.                   sodomy kiinmarz.
9423:wuzurg   I
9425:wuzurgihI                  ~J           ul l                     ~
9427:wuzurg-framadar \ , . .   ~ Q) ~        ulihI
9928:wis6bisn                     , I"'U eu t"'U \       wuzurg                         )),,,,
9930:wisuftan                      \\¥' CO \"'U \        wuzurgih
9939:wiskin(n)-                       -\.YU,             wuzurg
9940:wiskOf-                      -V\~\                  wuzurgih
10144:wazr                      '\5,      wahmiin\ wan, win                 \\\
```


## [2026-10-16T05:14:49.163Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^w[aā]z' PHD_mackenzie.txt | head; grep -n -E 'play' PHD_mackenzie.txt | head; grep -n -E 'w[aā]z[iī]d|wcytn|wazr|wuzurg|wcwlg|wazurg' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:14:49.606Z] TOOL RESULT

```
5288:waz-, ......isn(-ig), v. wazidan.
5289:waz [w)e I = M, (N haJ)] word, speech; 'grace' (before meals).
5294:wazay [wzyl N -, bazay] frog.
5296:wazaragan [w)c)lk)n l I M w)e)rg)n, N haztirgan] merchant.
5298:wazidan, waz- [we-ytn l P wz-, N -] move, blow (of wind).
5304:wazig [w)eyk I N hazi] game, play.
5306:wazr [wzl] = ~warz.
9987:waz-                           -'\'     Widadafs                 "UCO~\
10142:wazay                      §.,      windisn
10144:wazr                      '\5,      wahmiin\ wan, win                 \\\
631:for    wizIg ... read .wi.zIg [-w'cyk' I N -baz] -player.
3685: -- pazd- : blow, play the flute.
4179: pazd- [pzd- I = M] blow, play (flute).
4651:srQdan, srAy- [slwtn', sPd- I M sr'y-, N sur--] sing, recite, play (an in-
5303:2wazidan, waz- [w)e-ytn l I N hazidan] play.
5304:wazig [w)eyk I N hazi] game, play.
7260:perseverance pattiigih.                    play (n.) wazig.
7261:persevering pattiig.                       play (v.) wazidan; (instrument)
4062:vazitan [wcytn'] to travel, to ride: tē... ké vazäh [subju. 2nd p. sg. = ind.] pat vài i dérang-x"atà$ thou ... who ridest on the long-dominating Wind 9914-15, — Av. (1386) vaz-; MPrth. pres. wz- ‘to blow’ of the wind’, ‘to move, to go’ (MHC); Ghilain 52.70, cf Verbum 170; Paz.
```


## [2026-10-16T05:14:54.046Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'vazurk|vazurg|vazr|varz\\b|vazik|vāzīk|vazik' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:14:54.368Z] TOOL RESULT

```
1001:bitaxš [bythš] the Grand Vizier, of Jä- mäsp at Vištāsp's court 21—24. 2713; of the corresponding official at Arjasp’s court 2511, 287... A Prth. Arsacid title, adopted by the Sassanid kings of the 3d c., but later replaced by vazurg framatär (v. the 2nd w.); survived in independent Armenia governed by Arsacids (until A. D. 430) and in Georgia. Sas. inser. Prth byths, Prs bythšy KZSPrth a) 1. 23, b) l. 25, c) l. 27 = Prs ll. 29. 31. 33 Gr. v. a) Bde (in the list of the late Artaxšēr's officials), b) miridēng of Shapur’s own vizier, c)
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1095:eak [ck'] the top of the skull; of a sheep: the extremity of the head = the nose and the chin 1028. — NP cak ‘the lower jaw and chin', but Bal. prep. cak*-à *upon'. cand [end] 1. interrogative: how much? how many? 2412-13, 629. 8313. ki... ~ in- direct interr. 213-4 — 2. relative: as much, as many as: ---šān tuvān dätan as much as they are able to bestow 79%; apärik ~ vazurg-kunisndn the other performers
1393:var(e)št (Mx), corresponding to Phl *duš- varšt; from varz-, v. varzitan.
1477:ēvarz ['dwlc'] review, muster, as a mili- tary term: ~ kartan to review, to muster (an. army) 2014; — [hence ēvarzīk kas probably *a man called up for military service, DkM 750!?]. — Originally ‘com- putation, calculation, account’, ef the following examples: ~ 4 x“atdydn 6 osti- kan the rulers’ calling of their trustees to account DkM 40416; étar *zarvan i (K drang) àivan (< K) andak, ~ züt; änöd dātavār (!) rāst here (in this world) the term of the court is short, and the account swift; there (in heaven) is & righteous *judgment DkM 5481-11; apar hān 4 andar nihvārēh ~ about the items (necessary) in combat FrP 14, heading. In all probability to be connected with NP dvàr(ah) ‘calculation, reckoning; an account-book’ (of which dvārjah, dvarcah ‘a cash-book, a book of receipts and dis- boursments, a diary, or register’ is the diminutive) < *abi-varda- SW form of *abi-varza-; dvdr : ēvarz, cf ēvāc, Evar, évar. (Wrong interpretation by Nyberg, TMK 69 sq., Pagliaro, Iscr. Dura-Europo 592. 595). — From varz-, v. varz, varzitan.
1530:framatar [prmt?l] commander, leader: the title of the Grand Vizier is vazurg ~ F:
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
2171:kamak 1. will, wish, desire (= kam): 6 ~ rasét (imp.) may you attain, (the ful- filment of) your Royal Pleasure! 107; brihenisn u spahr u ~ i yazdān the predestination, Heaven, and the will of the gods 69°; pat ~ as teng as ever you wish 5915; ke Būšāsp ~ nē varzét he who does not (work the will of =) addict himself to Drowsiness 841%; ~ dátan 6 to direct one's will towards
2237:ikartan [krtn'; klty; ‘BYDWN-t'] kun- [ BYDWN-;forms v. I, 179; pres. 3d p.sg. kwnd: read kund] to make, to do, to per- form, to exercise, to commit, to cause, to bring about; to manufacture, to construct (hac ‘of’ a material); — forms active deriva- tive vbs. a) from v.ns. in -išn, e.g. āsāyišn ^ to repose, azbäyisn ~ to invoke; gar- zišn, īzišn, koxšišn, nikērišn, pursišn, za- nisn ete.ete. ~ ; b) from other nouns: čfrin, amoxtareh, appar, hampursakeh, tak, varz ete. ete. —, v. the resp. ws.; — with a pred. adj., e.g. 73. 34" etc.; girt kart = girt kartak (g. v.); vat-kart v. vat; or a pred. subst., e.g. api-$ ... bitaxš kunom 2510-11; . with kart as its cognate obj. P2:6-7. 8 [read (TB =) nev kart" kunän that I may do good deeds]. — With prev.: andar 6 kar ~, v. kar; api-§ Mānušcihr andar 6 Patisz"argar kart he brought M. (as a captive) to P. 1164-5, cf Bd A p. 2315-5; — apüc ~ to repel 42*3 gl.; to reflect 1125; — pat ddr apar ~ to crucify a p. 208; — bé ~ to remove 65; — berön asmän kunst he wil turn them out of heaven 10318; — frāc ~ to send forth 161!5; to bring forth, to produce 48?9; to attempt 81?!. — NB: man kart HWH-wm 374-5 for man kart-om by me it was done, v.s. v. h- and -m. — *BYDWN.x,ot' = kunät 5314, cf BY- DWN-x,-yd = 2nd p.sg.kunēKnS VII, 11. — Av. (444 sqq.) tkar-, pres.ko ranu-; OP kar- kunav-; MPrth kyrdn kr-; MPrs kyrdn kwn-; Paz. NP kardan kun-; cf s.v. hangirtikeh.
2252:kärvän [k’lw’n'] troup: with the indef. art. ~-é gróh-é 8*; an army as mobilized and ready for war 20U (v. ēvarz)!t. — V.s. v. kārēcār. Arm. lw. karawan, kare- wan; Paz. kāravgn (SGV); the w. com- monly refers to a troup of travelling merchants, hence the Skr. v. vänijya and the use of it in our languages. NP kārvān.
```


## [2026-10-16T05:14:57.548Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(vazr|vazurg|varz|vāzītan|vazitan)\\b' NYB_vol2_glossary.txt | head; grep -n -o -E '^vazr.{0,500}' NYB_vol2_glossary.txt | head -3; grep -n -o -E '^vazurg.{0,400}' NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-16T05:14:57.846Z] TOOL RESULT

```
3994:varzč-kar [wlcykl] farmer 1478.17, 1519.27,
3999:varzītārēh practice, performance 6971.
4000:varz-kartar artisan 2°.
4062:vazitan [wcytn'] to travel, to ride: tē... ké vazäh [subju. 2nd p. sg. = ind.] pat vài i dérang-x"atà$ thou ... who ridest on the long-dominating Wind 9914-15, — Av. (1386) vaz-; MPrth. pres. wz- ‘to blow’ of the wind’, ‘to move, to go’ (MHC); Ghilain 52.70, cf Verbum 170; Paz.
4065:vazitan [w’cytn'] caus. of the preceding v., to move: 1. trans. catrang — to play at chess 11915, 121%, — 2. intrans. to travel, to ride (= vazitan) 519-14. 6019, — Cf MPrth pdw’z ‘suite, followers’, pres. prw’z- ‘to cause to fly’, Ghilain 70; NP bazidan, büxtan ‘to play; to fly’.
4066:vazr [wzl] mace 851%, — Av. (1392) vazra-; Paz. vazr(a); NP gurz; also, with meta- thesis, varz (q. v.).
4070:vazurgēh [wewlgyh, LB’-yh] greatness 517.26, size 151.
4071:vazurg-kunišn [LB’ kwnšn'] of great achievements, executor of grand achieve- ments; pl. cas. obl. —-än 1068.
4073:vazurg-späs [LB? sp’s] of lofty service, performing high duties, pl. cas. obl. —-än 106!, v. späs.
6876:vazr(a): vazr
4066:vazr [wzl] mace 851%, — Av. (1392) vazra-; Paz. vazr(a); NP gurz; also, with meta- thesis, varz (q. v.).
5433:vazra-: vazr
6876:vazr(a): vazr
4069:vazurgakän [LB’-k’n'] pl. cas. obl. of vazurg: (0) Col xakan u ~ to the Khakan of C. and his magnates 11323. — Cf váspuhr : lydspuhrakan (g. v.).
4070:vazurgēh [wewlgyh, LB’-yh] greatness 517.26, size 151.
4071:vazurg-kunišn [LB’ kwnšn'] of great achievements, executor of grand achieve- ments; pl. cas. obl. —-än 1068.
```


## [2026-10-16T05:15:02.006Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4067,4068p NYB_vol2_glossary.txt | cut -c1-600; grep -n -E '^(vazra|vazraka|vazarka|vazrka)' BRT.txt | head; grep -n -E 'vazra-|vazrka|vazarka|vazṛka' BRT.txt | head"
}
```


### [2026-10-16T05:15:02.384Z] TOOL RESULT

```
"| vazurg [LB”, Prth RB’; wewrg, inscr.
welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
9930:KompA.  —  fli.  gada-  f.,  mp.  gas  (geschr.  dt); s.  noch  Osthoff  Par.  143.  —  ")  Im  Gegens. va  vazra-,  womit  gehauen  wuide.  Vgl.  Vt 10.  131  f.,  wonach  sich  in  ;1/f%ras  Wagen  1000 gaiä-  belinden,  aber  nur  ^in  zaim-.  Anders Galt,  OK,  445 ,  der  auf  die  Grundbedealnng von  saina.  lu  viel  Gewicht  legi.
10844:•  p.  xsäyaSiya-''  i)  Adj.  (fem.  'y3-)  'im Besitz  der  Herrschergewalt,  KönigswQrde, souverain' ;  Aa/ä  paruviyata  Ayä  amäxam tauml  yä  akc^  Bh. /.  3.  2I  m,  'Herr- scher, König' :  darayJ'v<^us  ya"  *'vazarka'' 'ya*  yanam  'ya"  pärsaiy  "yJ^  dahyUnam  \ Bh./.  I ;  —  darayaf'vi/'us  ya*  *vazarit/'  yc^ yanSm  'yt^  dakyünäm  yc^  ahyäyä  bumiyä D.i2;  j,  5.  I,  6.  2,  4,  16,  18,  ig,  X.  j,  2, 3  3,  5,  7-  3>  Am.  i,  2  '>,  3,  Ao.  /.  2  »_  K.  j, Bb-j.  i;  /.  2C,  2.  iff.,  j.  ifE,  4-1«:,  5. iff.,  D.4-  a,  3,  5-  3.  3.  6^,  3,  4,  s,  7,  J^, /7-3.  X.2.3,  3-3,  4-3,  S,  1.^,4,  7-3, Ao.  J.  3,4;  —  a'ur^mazdä..hycr  däraytr- vt^um    'yam    akiaaus   aivam  parHvnam
17377:•  g,,  j.'\  p.  bümi-  f.  'Erde';  II  («ä/«  'mim ,  .  avam  asmänam  D.  6.  i,  X.  i.  i,  6,  i, Ao.i.i  {tto'mäm);  D.6.4;  —  paitt 'mxm kaptai^yqm  Vt  JJ).  26;  —  raocaicä  .  . •mm^a  vTipäcä  vcha  Y.J/.  i;  42.  y,  — 'myä  (GS.)  haptai^e  (sd.)  Y.  32.  3;  — \xl3y^iya'  ahyäyä  'mtya  ^vazarkayil  D. 6.  2,  X.  /.  2 ;  Am.  7,  3,  Ao.  /.  2,  D.  72.
23211:•  p.  '''vazarka-  Adj.  (fem,  'kä-)  'gross': xiaya%iyi^  ahyöyä  bümiya  'kSyS  (GSf.) D.  (*.  2,  H. /.  i;  —  x^aSi''am  tyam  'kam D.J7.  a;  —  xlaya%iy(^    "ia*    "ö  /tej-asl
23256:!  •  j.  vazra-  m.  'Keule';  insbes.  Ilaukeule' " : yailqm    zayanqm    raäsSiili  .  .  '^ritys    'rS V.  J4.9;  —  •rif  Aunivix/if{sd.)  Ytlj.jx; 10.133;  —   'ra^J  (NP.)  .  .  hunivixia  ydi niyraire  saraiu  YL 10. 40;  —  tisit  kanta ndii  'ra  Ytl.  18;  —  apayüxtai  (sd.)  paiti 'rät  V.iS.^o,  36;  —  ist  Mi^rai  Haupt- waffe'': mihrahe'nm  ..satafitän^m  sats.- danm  ß-avafy»m  vjrd.nyancim  xar^i/(sd.) ayanhB frakixhm  amavats^tantiyehe  ama- vattmum  tayanqm  Yt.  10. 132 ;  96,  6. 5. ai.  vijta'  m. ;  np.  jk«.  —  Pü. :  vaa-.  —  i)  Im Gegens.  tu  gaiä-;   sd.  —  »1  Wie  der  väjra^ die  des  Indra.
```


## [2026-10-16T05:15:05.931Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E 'vazraka-.{0,300}' KNT_full.txt | head -4; grep -n -i -E 'wz.rk|wzrk' SOD.txt | head"
}
```


## [2026-10-16T05:15:06.707Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/tools; sed -n 1,80p verify_check.py | head -100"
}
```


### [2026-10-16T05:15:07.025Z] TOOL RESULT

```
5375:vazraka- ‘great’, in the royal 
28886:vazraka- adj. ‘great’: NPers. buzurg; deriv. of 
64850:wazark,  mazex  ©Idg.;  pi.  -t(h)  ^wz'rk 
79631:10575  wz'rk   B  JjJti 
79713:10587  wzrg    M  =*  wz>rk
```


### [2026-10-16T05:15:07.082Z] TOOL RESULT

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
```


## [2026-10-16T05:15:08.920Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/tools; sed -n 80,200p verify_check.py | grep -n -E 'PROBLEM|problems.append|sources|web' | head -40"
}
```


### [2026-10-16T05:15:09.398Z] TOOL RESULT

```
11:        print("PROBLEM:", p)
```


## [2026-10-16T05:15:13.257Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 79629,79634p SOD.txt; sed -n 79711,79716p SOD.txt; grep -n -E 'wz.rk' SOD_pages.txt | head -3; grep -n \"^10575\\|10575 \" SOD_pages.txt | head"
}
```


## [2026-10-16T05:15:14.068Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:272 2>&1 | tail -40"
}
```


### [2026-10-16T05:15:14.477Z] TOOL RESULT

```
TSP  3.204  apud.  Hen.  Texts.  729 

10575  wz'rk   B  JjJti 
wazark   (RB,  wzrg)  ©<OP  vazarka  ©pi.  -t(t) 

=»RBk(,) 
TSP  3.172;  Hen.  Texts.  727.172 

10587  wzrg    M  =*  wz>rk 

10588  wzrw   B  c^lj 
wizru   (wyrzr)  =*wrzr-,  wyzr- 
28090:       gaOra-rayant; Khot. raU Yaghn. roy; Wakh.                  wazark, mazex ©Idg.; pi. -t(h) ^wz'rk
34314:      terrible, awesome                                         10575 wz'rk     B                              JjJti
34389:10587 wzrg       M =* wz>rk                                                  x'ny, STi 31.16; Sund, AoFviii 1981, 5R14-,
34314:      terrible, awesome                                         10575 wz'rk     B                              JjJti
37748:(^)be pleased     7911,7914                  10575                               blood-stained     10760
38423:   5703, 10575                                  half and half 6270                        hated    4613, 11589, 11591, 11597
```


### [2026-10-16T05:15:15.393Z] TOOL RESULT

```
no scan of BQT covers printed page 272 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:15:20.296Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=34314 && /\\[pdf page/ {l=$0} END{}; NR==34314{print l}' SOD_pages.txt; sed -n 34310,34320p SOD_pages.txt | cut -c1-200; grep -n -E 'بزرگ' BQT_v1_pages.txt | head -5"
}
```


### [2026-10-16T05:15:20.942Z] TOOL RESULT

```
       Mack. AI 25, 1985, 422, 20                                     wazande =»wz-
10564 wyzpywn'k B
                                                                       TSP 3.204 apud. Hen. Texts. 729
      Mzb-yone (wyzpywny) *=*wyzp, wzpywn}k/y
      terrible, awesome                                         10575 wz'rk     B                              JjJti
      TSP 6.193; Hen. Texts. 723; GMS 212 n 2, 1114,                   wazark     (RB, wzrg) ©<OP vazarka ©pi. -t(t)
        C2, nom. 5V28, gen. 61V20, loc. 31R24,
         69V30; pi. -/, C2, 60V28; Ben v. JA 1955, 317;
                                                                       big, great
         -/A, TSP 3.150
                                                                             RBk(16,)6, VJ 206, GMS 50, 976, W-Lii
167:( در ارمشتان) وسوئز ( درمصر ) . نوشتة بفستان ازداریوش بزرگ که‌مانند
415:نیایش و دوسیروزه ( بزرگ و کوچك ) و برخی دیگر نماژها و درودهای
444:یا پار سيك» وبونانی. بکی‌از این سنگنبشتهای بزرگ ومهم امروزه برون از
989:وبزرگان دورءآنانو اوایل عبداسلا) بقل شده گاه بزبان پارسی‌است وگاه
3261:بزرگ » زروان بزرگ » شید » يشتن » (متقلا وذیل : درون ) .
```


## [2026-10-16T05:15:24.484Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk '/\\[pdf page/ {l=$0} NR==34314{print l; exit}' SOD_pages.txt; grep -n -E '^ *بزرگ|بزرك' BQT_v1_pages.txt | head -8; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False)[:1500])\""
}
```


### [2026-10-16T05:15:24.860Z] TOOL RESULT

```
287:بعش بزرك آن از دست رفته و از یست ويك نسك (کتاب) که در روز کار
3261:بزرگ » زروان بزرگ » شید » يشتن » (متقلا وذیل : درون ) .
9507:بقلم جمال زاده. مجلهٌ کاره سل پنجم شمار *۱ (شمار؛ مسلسل 6۵) و بزرك : والرة و
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir}
```


## [2026-10-16T05:15:28.985Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'vazarka|vazṛka|vazrka|vuzurg|wuzurg|vazurg|buzurg' BQT_v1_pages.txt BQT_v1.txt | head; grep -n -i -E 'vazra|gurz|varz' incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-10-16T05:15:29.312Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:31.573Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; head -c 600 data/verification/sources/refs/BQT_v1_pages.txt; echo; python3 tools/ref_page.py BQT:1793 2>&1 | tail -40"
}
```


### [2026-10-16T05:15:39.731Z] TOOL RESULT

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
REF: BQT:1793  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 590  OCR-lang: fas

۱۷۹۳۳ کرزن
گرد ۱ -بنم اول وسکون ثانی وزای کویند ۴ ؛ و باکاف تازی هم بنظر آمده است.
آعنین راکویند جوز | نات ومیم . برادراعیانی‌اسفندباراست واوی دکوبی
اسفندبار پیش گشتاسب کرد و کشتاسب اسفندبار
و چماق چوب را کوز را بند فرمود ها را
هم کعته‌اند - و دستهٌ هاون را نیز کوبند - َ رما 1 ۱
وکنایه ازقضیب هم هت که آت تناسل باشد. گرز نس - بفتح اول وثانی و رایع
ی بالف کشیده بروزن فلك‌سان » آسمان را گوبند؛
گرددمن بفتح اول وئانی‌وسکون ما 1 مد اس ۰
ی ۹ وبفتح ول وسکون ثانی هم آمده است - وعرش
زای نقطه‌دار وفتح دال بی‌نقطه وکسر میم ونون اعظم را نیز گفته اند که" فلك الافلاك باشد ۷ .
ساکرن. داغت ند وبازند نمعنی‌دشمرن وغنم‌باشد. 0
نی 9 ۳ ی ۳۳ ۱ گردن < بر وزن آرزن » تاج مرصعی
گرد ثت‌ - جم اول وفتح ثانی‌ورا بم بوده کیانرا بیار بز رکه وسنگین وآنرا پربالای
وسکون ثالث ونون آخر . بمعنی چاره کردن | تخت‌محاذی سر ایغان‌با زنجیرطلامی آويشته‌اند .
و شش ۰.۰ ۰ ۰ ‌
گردش - بفتح اول و کس ثالث‌بروزن | بیضهٌ کنجشگی وآن بانوشیروان رسیده و عربان
ورزش,تظلم وداد خواهی وتضرع وزاری‌نمودن را | آنرا قنقل بروزن منقل کفتندی و قنقل کیله
۱ - پهلوی ۰۷227 اوستا- ۷2272 « بارتولمه۱۳۹۲*. معرب جرز. ارمنی ع۷272هندی
باستان- ۷4[۲۵ (کرز رعد [ایندرا]) «اسشق ۹۰۹ « نیب رکه ص۲۳۷ کردی 8072 « ژابا ص
۵۹ - ۳۹۰ *.ورك :کرزه. ۴ نمهز. 887220427328. 8۳۵[45038. ۰12۳741322
پهلوی 25۳2۳ [۱ شم ( ای بونگر ص ۱۱۷۲ . ۴ - موف «گزردن ۰ (ه.م.) -
بده داد من زان لبانت و کرته سوی خواجه خواهم شد از تو بگرزش.»
آقای دهغخدا کلمهرا مصحف «گزرش » ۳ (کزاری) میدانند . « لغخت فرسی ۲۱۳ .۰
8 - و نیز یکی از قهرمانان تورانی . رك : فهرست ولف .
‎٩‏ - کلمهٌ پارسی ( مستعمل زرتشتیان ) - فارسی 82721121 ( آسمان ) . این‌کلمه‌در
اوستا 0438۳282 8807۵6 . ۳۱288 827۵ پازند 82761۳۲28 ۰ مغدی ۰8۳27043۳88
پارتی 8270108 » اوراق مانوی بپارسی‌میانه 8472577128 . وكلمهٌ پارسی- فارسی82۳2128
تلفظ متأخر ومفلوط است بمعنی (آسمان علیین ۰ عرش خدا) با بهمنی وسیمتر (آسمان,بهشت).
رد : (۱57 . 0 . ۷۷۵۲۵۶ ۸9128 |6218 1۷0 ,ع 1162810 ) ورد :
( ۱,0.82 ,13 , 8505 ب ... ققنوت۳ ۷۵۵۱6 0۶ 1۶4 ۸ « قصادی۲
۷ - ۶ پارسیان کوبند عرش است و شمراکویندآسمان است . دقیقی (طوسی) کوید :
مه وخورشید با برجیس وبهرام زحل با تیر و زهره بر کرزمان
همه حکمی بفرمان تورانند که ایزدمرترا داده است‌فرمان.»
‌ لهخت فری ۹۷
```


## [2026-10-16T05:15:45.736Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /بزرگ|بزرك/ && /بضم|بروزن/ {print NR-1\": \"substr($0,1,80)}' BQT_v1_pages.txt | head -20; awk 'BEGIN{RS=\"\\f\"} {if (match($0,/۲۷۲/)) print NR-1}' BQT_v1_pages.txt | head"
}
```


### [2026-10-16T05:15:46.585Z] TOOL RESULT

```
246: آزدن
رذن . بازای فارسی » بروزن و معنی
آزدن بلشد که خلانیدن سوزن وامشالآنست .-
و 
257: ۰- 1 حه
شا فه ۱ - بروزن‌تلزبانه.بمعنیآشیان
است که خانهٌ مرغان - و سقف خانه باشد 
436: با
خوانند و آنراکبوتر بیار دوست دارد . 9
پاار لك - بکر تاكث و سکون کاف ؛
مشفف با
520: مکتك ون
بلکنجات سم .اول و ثالث که کاف
فارسی باشد و فتع جیم که خامس باشد وسکون
ان
536: بورش
باشد که درخانةُ ل و کنند. :
بو د بطش « با ناك بتحتانی رسیده .
وطای حطی مکسو
550: یم - بر وزن فهیم : تلم یکی آزرابان
18
25
27
28
128
160
335
420
434
574
```


## [2026-10-16T05:15:50.634Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT'];print(d.get('page_offset'));print(d.get('scans'));print(d['lookup_hint'][-800:])\"; grep -rl 'BQT:272' ../page-*.json | head -3"
}
```


### [2026-10-16T05:15:51.002Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
ext page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-10-16T05:15:53.811Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 490 491 492 493 494; do echo \"LEAF $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -5; done"
}
```


### [2026-10-16T05:15:54.483Z] TOOL RESULT

```
LEAF 490
و کار بهوده و بیفایده کردن باشد . #
پر ود قلكك - کنابه ازماه است که‌قمر
باشد - و ژحل را نی زگفته‌اند 3
بر لژزن - بکر اول و تحتانی مجهول
بروزن شیمن » پرویزن باشد که بعربی غرپال
LEAF 491
سه اوه -ت
رای تس ی
آن بکار برند و بردمید کیها یز مالند .
یر بش - بکسر اولو انی رسکون‌تاث
و شین قرشت » بمعنی آخربراش است کهپاتیدن
LEAF 492
راد ب‌آمده
پز اد بر آهفه - زیی را گویند که
بسیار پیر شده باشد و سال بسیاری بر وگذشته
باشد .
باشد که از چستن است - و بمعنی وزنده‌هم‌هت
LEAF 493
آب بندند( ‏ و سکون ثابی گوی باشد که آب
درآن جمع شود - و رنگهآبرا نیز کوبند . *
بز چا لهفلاك - کنابه از برج جدی
است .
بز سم - بنتح اول و انی و سین بی
LEAF 494
کنفه . کوبند که‌درخت‌پسته مکال میوه‌فزدار
بارآورد و یکسال بی‌مفز , وآنراکه بی‌مفز است
بزغنج گویند ِ.
ز نف - با دال ابجد » بروزن و معنی
بزغنج است و آن پته مانندی باشد که بدان
```


## [2026-10-16T05:15:57.217Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 495 496 497; do echo \"LEAF $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n -E 'بزر|vaz|buz|عظیم|کلان' ; done"
}
```


### [2026-10-16T05:15:57.901Z] TOOL RESULT

```
LEAF 495
LEAF 496
6:چلپاسه لیکن از چلیاسه بزر کتر میباشد و آنرا
LEAF 497
6:وبزر کان روز های عید و جشن ومردمان درروز
```


## [2026-10-16T05:16:02.270Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 494 495 496 497; do awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-530-$l.txt; done; cat /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-530-495.txt | head -80"
}
```


### [2026-10-16T05:16:02.897Z] TOOL RESULT

```
ی ۱۷
۵ » بفتح اول وثانی . بمحتی کناموخطا
باشد ٩‏ - و مردم نامراد ومسکین رانیز گوشد
و بمعنی جور و حیف:همآمده. است - و جنم اول
ز مین پشته‌پشته‌باشد - د نوعی ازمیو؛ خوشبوی‌هم
۳
یز هش - بنم اود وکسر ها بر وزن
پرسش ۰ بممنی مقابله باشد که در برابر مقارنه
اس ..
ه گاد ۴ ه با کاف بروزن مزمدار ء
بمعن ی گنه کار و خطا کننده باشد و آنرآبربی
آثیم خوانند , و با کاف فارسی هم گفته اند  .‏
بر بچه ۴ بر وزن کلجه » پزغاله را
رم
کوند و بمربی حلان و علام خوانند بخم حای
ي‌قطه , و حلوان غلط است - و برج جدی را
هم کفته اند - و سه پابٌ قصاب و سلاخ را نیز
گویند .
بر بدن ٩‏ بفتح اول » بروزن و حعنی
وزبدن باشد .
بر بش ه بانحتانی محهول وشن نقطه‌دار
بروژن‌کیجه » اردءٌ (۱) کتد زا کولاب و ثفل
کذجد روغن کشیده را هم میگونند .
لژ للن « بر وزن حزین » بمعنی وزنده
باشد که ازوزیدن است ۷- ونام آتشکده ای هم
بوده دز روستای نیشابور ۷ , و باین‌معنی با رای
فرشت هم 1 ۳
باشد - و سرماریژه را گوبند و آن چیزیاست
که در وفت شدت سرما بمانند زرك و زر ورق
ازهوا رد .
یز کم ‌- بفتح اول و کاف )۲ وسکرن
الیو یم ء. بممنی بازداشتن و منم باشد -
بر کول 9 بفتح‌اول بروزن بککول.
باشد و حریص در کار ها بود » و بکسر اول هم
رم « بفتح اول و سکون انی و میم .
۱ پپلوی 08021 «منای 4۲۹۹ , پازند 082102 «تیب رکك ۲٩‏ :
زه رگونه‌ای نعام آراستم بگفتم درآن هر چه خودخواستم
اکی چهدلم بوداز آن‌بامزء همی کاشتم تخم وزر « بزه .
بوسف وزلیخای منسوب بفردوسی درعذر از داستانهای اغراق آمیز.
۳ س بزه طم اول حنسوب‌به بز ومر ادبرحجدی است . ۴ پپلوی ۳(
*عنای ۲۹۹ . ۴ < بز + بجه ( علامت صخیر » چون : وریجه) «اسفا ۱ :۲ص *۷».
٩‏ رگ : وزسن . ۱ - رك: پزیدن و وژسن.
۷ - مسحف برزین *مزدینا ۲۱۷ رگ : آذربرزین .
شکولیدن (بانیروبودن) از شکول (چايك) «اسفا ۰۱: ۷ س ۱۹۰ .
ج رهکاری . پهلوی 10 «ناي ۲۹۹ ؛ کناهعاری .
۸ 7 بشکول از مصدر
٩‏ - رك : بشم .
```


## [2026-10-16T05:16:07.241Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; grep -n -E 'بز ?ر ?[كکگ]|ستر|اسفا|پهلوی|پارسی باستان' bqt-530-494.txt bqt-530-495.txt bqt-530-496.txt | head -30"
}
```


### [2026-10-16T05:16:07.772Z] TOOL RESULT

```
bqt-530-495.txt:41:*عنای ۲۹۹ . ۴ < بز + بجه ( علامت صخیر » چون : وریجه) «اسفا ۱ :۲ص *۷».
bqt-530-495.txt:44:شکولیدن (بانیروبودن) از شکول (چايك) «اسفا ۰۱: ۷ س ۱۹۰ .
bqt-530-495.txt:45:ج رهکاری . پهلوی 10 «ناي ۲۹۹ ؛ کناهعاری .
bqt-530-496.txt:6:چلپاسه لیکن از چلیاسه بزر کتر میباشد و آنرا
bqt-530-496.txt:46:۲ - پهلوی ۷۵5 . پارسی
```


## [2026-10-16T05:16:14.587Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=split($0,L,\"\\n\"); for(i=1;i<=n;i++) if (L[i] ~ /^ *(بزر ?[كکگ]|بزرك|بزرگ) *[-ـ]/) print NR-1\": \"L[i]}' BQT_v1_pages.txt | head"
}
```


### [2026-10-16T05:16:15.294Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:16:18.666Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-10-16T05:16:18.924Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "data", "verification", "sources", "web")
INDEX = os.path.join(WEB, "index.jsonl")
UA = "rishe-verification/1.0 (+https://github.com/sfmqrb/rishe; etymology source archiving)"


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    note = ""
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
        print(__doc__); return 2
    url = args[0]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    # IRI -> URI: percent-encode non-ASCII path/query characters so urllib accepts them
    parts = urllib.parse.urlsplit(url)
```


## [2026-10-16T05:16:23.777Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weǵ-' 'https://en.wiktionary.org/wiki/بزرگ' 'https://en.wiktionary.org/wiki/گرز' 'https://en.wiktionary.org/wiki/باختن' 'https://en.wiktionary.org/wiki/بازیدن' 'https://en.wiktionary.org/wiki/vazra' 'https://en.wiktionary.org/wiki/वाज' 'https://www.etymonline.com/word/wake' 'https://www.etymonline.com/word/watch' 'https://www.etymonline.com/word/wait' 'https://www.etymonline.com/word/vegetable' 'https://www.etymonline.com/word/vigor' 'https://www.etymonline.com/word/vigilant' 'https://www.etymonline.com/word/velocity' 'https://vajehyab.com/moein/بزرگ' 'https://en.wiktionary.org/wiki/vēlōx' 'https://en.wiktionary.org/wiki/𐎺𐏀𐎼𐎣'; do python3 tools/fetch_source.py \"$u\" --note \"page 530, root Weg 2: etymology check\" 2>&1 | tail -1; done"
}
```


### [2026-10-16T05:16:31.278Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/86af466221981ad2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bbdcccf5c18a5950.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/28124131c88d8743.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e2823c51ebf4a2e1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/417aabf70780e5d6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1eaba955373d4436.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bf9ac64442721c10.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/55297c26231c16b8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7f46a71fbad5f6bf.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ae94e44f4861fb2e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f174aa38b07fb55c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1bd17baaf0bf1068.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1be6f2e985d75e04.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/408bcf2582376c0a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/28489330988df176.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0e9da593fd48830f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9365781aaa87e85b.txt
```


## [2026-10-16T05:16:34.589Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 86af466221981ad2 bbdcccf5c18a5950 28124131c88d8743 e2823c51ebf4a2e1 417aabf70780e5d6 1eaba955373d4436 bf9ac64442721c10 9365781aaa87e85b; do echo \"## $f $(wc -c <$f.txt)\"; grep -n -i -A3 -E '^Etymology|Etymology [0-9]' $f.txt | head -14 | cut -c1-500; done"
}
```


### [2026-10-16T05:16:34.944Z] TOOL RESULT

```
## 86af466221981ad2 5661
## bbdcccf5c18a5950 10588
## 28124131c88d8743 7221
## e2823c51ebf4a2e1 17501
## 417aabf70780e5d6 138
## 1eaba955373d4436 131
## bf9ac64442721c10 9973
## 9365781aaa87e85b 5036
```


## [2026-10-16T05:16:37.587Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 86af466221981ad2 bbdcccf5c18a5950 28124131c88d8743 e2823c51ebf4a2e1 bf9ac64442721c10 9365781aaa87e85b 417aabf70780e5d6; do echo \"## $f\"; grep -i -E 'from|inherit|borrow' $f.txt | head -8 | cut -c1-600; done"
}
```


### [2026-10-16T05:16:38.074Z] TOOL RESULT

```
## 86af466221981ad2
 From Wiktionary, the free dictionary
 Terms derived from the Proto-Indo-European root *weǵ- (46 c, 0 e) 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/weǵ-&oldid=93412532 "
## bbdcccf5c18a5950
 From Wiktionary, the free dictionary
 Borrowed from Urdu بزرگ or Pashto بزرگ , from Persian بزرگ .
 From Middle Persian 𐭥𐭰𐭥𐭫𐭢 ( ʿcʿlg /⁠wuzurg/, /wazurg⁠/ , “ big, great ” ) , from Old Persian 𐎺𐏀𐎼𐎣 ( v-z-r-k /⁠vazr̥kaʰ⁠/ ) .
 Borrowed from Classical Persian بُزُرْگ ( buzurg ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=بزرگ&oldid=93411699 "
 Gawar-Bati terms borrowed from Urdu 
 Gawar-Bati terms derived from Urdu 
 Gawar-Bati terms borrowed from Pashto 
## 28124131c88d8743
 From Wiktionary, the free dictionary
 From Middle Persian [script needed] ( wlz /⁠warz⁠/ , “ mace ” ) , from earlier [script needed] ( wzl /⁠wazr⁠/ ) , from Avestan 𐬬𐬀𐬰𐬭𐬀 ( vazra , “ mace ; main weapon of Mithra ” ) , from Proto-Iranian *wájrah , from Proto-Indo-Iranian *wáȷ́ras . Cognate with Sanskrit वज्र ( vájra , “ thunderbolt ; especially that of Indra ” ) , Erzya: узере ( uzere , “ axe ” ) and Northern Sami: veahčir ( “ hammer ” ) , as well as akin to Old Armenian վարզ ( varz , “ mace ” ) .
 An Indo-Persian گرز ( gurz , "mace", "club") from the 17 th century 
 Borrowed from Classical Persian گُرْز ( gurz ) . [ 1 ] In the Indo-Persian tradition, it became associated with lightning-bolts, thunder and storms. It became a metaphor for strength and force as well, especially in relation to the warrior and fighter . ( Can this ( + ) etymology be sourced ?) 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=گرز&oldid=92088782 "
 Categories : Persian terms derived from Middle Persian 
 Persian terms derived from Avestan 
 Persian terms derived from Proto-Iranian 
## e2823c51ebf4a2e1
 From Wiktionary, the free dictionary
 From Middle Persian [Book Pahlavi needed] ( wʾc- /⁠wāz-⁠/ ) , from Proto-Iranian *wāz- ( “ to play, contend ” ) , probably from a blend of Proto-Iranian *wan- ( “ to win ” ) +‎ *Haz- ( “ to drive ” ) , from Proto-Indo-European *wenh₁- ( “ to love, wish ” ) + Proto-Indo-European *h₂eǵ- ( “ to drive ” ) , respectively. Likely related to Sanskrit वाज ( vāja , “ contest; conflict; battle ” ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=باختن&oldid=91790413 "
 Categories : Persian terms derived from Middle Persian 
 Persian terms inherited from Middle Persian 
 Persian terms inherited from Proto-Iranian 
 Persian terms derived from Proto-Iranian 
 Persian terms inherited from Proto-Indo-European 
## bf9ac64442721c10
 From Wiktionary, the free dictionary
 From Proto-Indo-Aryan *wā́ȷ́as , from Proto-Indo-Iranian *wā́ȷ́as , from Proto-Indo-European *weǵ- ( “ lively ” ) . Cognate with Latin vegeō , Gothic 𐍅𐌰𐌺𐌰𐌽 ( wakan ) , English wake .
 Lubotsky, Alexander ( 2011 ), The Indo-Aryan Inherited Lexicon (in progress) (Indo-European Etymological Dictionary Project), Leiden University, page 577 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=वाज&oldid=91925063 "
 Categories : Sanskrit terms inherited from Proto-Indo-Aryan 
 Sanskrit terms derived from Proto-Indo-Aryan 
 Sanskrit terms inherited from Proto-Indo-Iranian 
 Sanskrit terms derived from Proto-Indo-Iranian 
## 9365781aaa87e85b
 From Wiktionary, the free dictionary
 Originally meaning “ endowed with generative power ” , from vazra- , borrowed from Old Median *vazr̥kah , from Proto-Iranian *wájrakah , from Proto-Indo-Iranian *wáȷ́rakas ( “ strong, hard ” ) (compare Sanskrit वज्र॑क ( vájraka , “ diamond ” , literally “ strong/hard one ” ) ), from *wáȷ́ras ( “ strong ” ) , from Proto-Indo-European *weǵ- ( “ to be strong, lively, awake ” ) + *-ros , + Proto-Indo-Iranian *-kas . Compare Old English wacor , Proto-Norse ᚹᚨᚲᚱᚨᛉ ( wakraʀ , “ awake, alert, watchful ” ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=𐎺𐏀𐎼𐎣&oldid=93413073 "
 Categories : Old Persian terms derived from the Proto-Indo-European root *weǵ- 
 Old Persian terms borrowed from Old Median 
 Old Persian terms derived from Proto-Indo-European 
 Old Persian terms derived from Proto-Indo-Iranian 
 Old Persian terms derived from Old Median 
## 417aabf70780e5d6
```


## [2026-10-16T05:16:41.924Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 1,200p 86af466221981ad2.txt | grep -v '^\\s*$' | head -90 | cut -c1-200; for f in 55297c26231c16b8 7f46a71fbad5f6bf ae94e44f4861fb2e f174aa38b07fb55c 1bd17baaf0bf1068 1be6f2e985d75e04 408bcf2582376c0a 28489330988df176 0e9da593fd48830f; do echo \"## $f $(wc -c < $f.txt)\"; done"
}
```


### [2026-10-16T05:16:42.403Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weǵ-
FETCHED: 2026-10-16T05:16:25Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/weǵ- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/weǵ- - Wiktionary, the free dictionary 
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
 1.2 
 References 
 1.3 
 Further reading 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ weǵ- 
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
 See also: Reconstruction:Proto-Indo-European/weǵʰ- 
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative eviden
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *weǵ- [ 1 ] [ 2 ] [ 3 ] 
 to be lively , awake 
 Synonym: *bʰewdʰ- 
 to be strong 
 Alternative reconstructions
## 55297c26231c16b8 131
## 7f46a71fbad5f6bf 132
## ae94e44f4861fb2e 131
## f174aa38b07fb55c 136
## 1bd17baaf0bf1068 132
## 1be6f2e985d75e04 135
## 408bcf2582376c0a 135
## 28489330988df176 1705
## 0e9da593fd48830f 133
```


## [2026-10-16T05:16:45.443Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 86af466221981ad2.txt | sed -n 90,200p | cut -c1-200; cat 55297c26231c16b8.txt; grep -v '^\\s*$' 28489330988df176.txt | tail -15"
}
```


### [2026-10-16T05:16:45.970Z] TOOL RESULT

```
 Alternative reconstructions
 [ edit ] 
 *h₂weǵ- [ 4 ] 
 *h₂weg- [ 5 ] ( as Schwebeablaut variant of *h₂ewg- ) 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *weǵ- (46 c, 0 e) 
 *woǵ- ( o-grade root present ) 
 Proto-Germanic: *wakaną ( “ to wake up ” ) ( see there for further descendants )
 ⇒ Proto-Germanic: *wahtwō ( see there for further descendants )
 *woǵ-éye-ti ( causative ) 
 *weǵ-eh₁-(ye)- or *woǵ-eh₁-(ye)- ( stative ) 
 Proto-Germanic: *wakāną ( “ to wake, be awake ” ) ( see there for further descendants )
 Proto-Italic: *wegēō ?
 Latin: vigeō ( “ to thrive, flourish; to be vigorous, lively, alive ” ) ( see there for further descendants )
 *weǵ-(dʰ)l-i-s ( formation unclear ) 
 Proto-Italic: 
 Latin: vigil ( “ awake, watching, alert ” ) ( see there for further descendants )
 *wóǵ-o-s 
 Proto-Indo-Iranian: *wā́ȷ́as ( “ strength, energy ” ) 
 Proto-Indo-Aryan: *wā́ȷ́as 
 Sanskrit: वाज ( vā́ja ) 
 *wóǵ-ro-s 
 Proto-Germanic: *wakraz ( “ watchful, awake ” ) ( see there for further descendants )
 Proto-Indo-Iranian: *wáȷ́ras ( “ strong, hard ” ) ( see there for further descendants )
 → Proto-Uralic: *waśara ( “ hammer ” ) ( see there for further descendants )
 *(s)weǵ-i-s 
 Proto-Balto-Slavic: *(s)wēˀźis 
 > ? Proto-Slavic: *svěžь ( doubtful ) [ 6 ] 
 References
 [ edit ] 
 ^ De Vaan, Michiel ( 2008 ), “ vegeō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pag
 ^ Rix, Helmut , editor ( 2001 ), “ *u̯eg̑- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , pages 
 ^ Sihler, Andrew L. ( 1995 ), New Comparative Grammar of Greek and Latin , Oxford, New York: Oxford University Press, →ISBN , pages 40, 497 
 ^ Mayrhofer, Manfred ( 1996 ), “ vā́ja- ”, in Etymologisches Wörterbuch des Altindoarischen [ Etymological Dictionary of Old Indo-Aryan ]‎ [1] (in German), volume II, Heidelberg: Carl Winter Universi
 ^ Kümmel, Martin Joachim ( 2011–2026 ), “ *u̯eg̑- ”, in Addenda und Corrigenda zu LIV² ‎ [2] 
 ^ Chernykh, P. Ja. ( 1999 ), “ свежий ”, in Историко-этимологический словарь русского языка [ Historical-Etymological Dictionary of the Russian Language ] (in Russian), 3rd edition, volume 2 (панцирь
 Further reading
 [ edit ] 
 Pokorny, Julius ( 1959 ), Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume III, Bern, München: Francke Verlag, pages 1117-8 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/weǵ-&oldid=93412532 "
 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European ReC-shaped roots 
 ine-pro:Sleep 
 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 Sanskrit terms with non-redundant manual transliterations 
 This page was last edited on 4 October 2026, at 16:18.
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
 Reconstruction:Proto-Indo-European/ weǵ- 
 Add languages 
 Add topic
URL: https://www.etymonline.com/word/wake
FETCHED: 2026-10-16T05:16:28Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden معنی بزرگ در فرهنگ مترادف و متضاد 
 معنی بزرگ در فرهنگ نام‌ها 
 واژه‌های مشابه
 بزرگ خوانده 
 بزرگ داشتن 
 بزرگ سال 
 بزرگوار 
 نوروز بزرگ 
 ببرگ 
 بارگاه 
 بارگی 
 بارگیر 
 بارگیر چوبین 
 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید
```


## [2026-10-16T05:16:51.304Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/velox' 'https://en.wiktionary.org/wiki/vegeo' 'https://en.wiktionary.org/wiki/vigeo' 'https://en.wiktionary.org/wiki/wait' 'https://en.wiktionary.org/wiki/watch' 'https://en.wiktionary.org/wiki/vegetable' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/wáȷ́ras' 'https://abadis.ir/fatofa/بزرگ/'; do python3 tools/fetch_source.py \"$u\" --note \"page 530, root Weg 2: etymology check\" 2>&1 | tail -1; done"
}
```


### [2026-10-16T05:17:00.148Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f3a774b54f77a8e5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c23f2f353c7a9dc0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/231d32f2835cfdd9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/400e9c3e5cf03bb6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2e4861b12c68a197.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e9a246cfeefd89ce.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/06aa9a90478f9d5b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d48581c81d7f5ec0.txt
```


## [2026-10-16T05:17:06.512Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in f3a774b54f77a8e5 c23f2f353c7a9dc0 231d32f2835cfdd9 400e9c3e5cf03bb6 2e4861b12c68a197 e9a246cfeefd89ce 06aa9a90478f9d5b; do echo \"## $f $(wc -c <$f.txt)\"; grep -E '^ ?(From|Inherited|Borrowed|Uncertain|Probably|Possibly)' $f.txt | head -4 | cut -c1-500; done; grep -n -E 'معین|پهلوی|vazurg|wuzurg' d48581c81d7f5ec0.txt | head"
}
```


### [2026-10-16T05:17:06.894Z] TOOL RESULT

```
## f3a774b54f77a8e5 6092
 From Wiktionary, the free dictionary
 From Proto-Indo-European *h₂weh₁-lo- ( “ wind ” ) , from *h₂weh₁- ( “ to blow ” ) , named after the speed of wind. [ 1 ] 
## c23f2f353c7a9dc0 7548
 From Wiktionary, the free dictionary
## 231d32f2835cfdd9 7613
 From Wiktionary, the free dictionary
 Uncertain. Perhaps a stative form from the Proto-Indo-European root *weǵ- ( “ to be lively ” ) , possibly via Proto-Italic *wegēō . De Vaan and Sihler relate the term to vegeō , which De Vaan argues is indicative of an original adjective *weg-o- ( “ active , alive , awake ” ) , which De Vaan suggests may be the source of the Latin term. [ 1 ] The *-i- is unexpected in the Latin form; De Vaan suspect this to be a vowel raising from original *-e- after the labial v- , as also seen in firmus and v
## 400e9c3e5cf03bb6 31698
 From Wiktionary, the free dictionary
 From Middle English waiten , from Anglo-Norman waiter , waitier (compare French guetter from Old French gaitier , guaitier ), from Frankish *wahtwēn ( “ to watch, guard ” ) , derivative of Frankish *wahtu ( “ guard, watch ” ) , from Proto-Germanic *wahtwō ( “ guard, watch ” ) , from Proto-Indo-European *weǵ- ( “ to be fresh, cheerful, awake ” ) . 
 From Old Norse hvítr , from Proto-Germanic *hwītaz . Cognate with Swedish vit .
 Inherited from English white .
## 2e4861b12c68a197 50804
 From Wiktionary, the free dictionary
 From Middle English wacchen , from Old English wæċċan , from Proto-West Germanic *wakkjan , from Proto-Germanic *wakjaną .
## e9a246cfeefd89ce 13295
 From Wiktionary, the free dictionary
 From Middle English vegetable , from Old French vegetable , from Latin vegetābilis ( “ able to live and grow ” ) , derived from vegetāre ( “ to enliven ” ) . Displaced Old English wyrt and ofett , whence modern wort and ovest .
## 06aa9a90478f9d5b 6210
 From Wiktionary, the free dictionary
65: فرهنگ معین
225:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
227:• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
240: بزرگ واژه ای فارسی و بر گرفته از واژه �wuzurg� در فارسی میانه می باشد 
270:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
272:• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
312:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
314:• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
335: بزرگ از پهلوی گرفته شده و صددرصد فارسی است
364:ترکیب ( صفت ) [پهلوی: bazurg، مقابلِ کوچک]
```


## [2026-10-16T05:17:11.202Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -n -E '\\^ ' web/f3a774b54f77a8e5.txt | head -3 | cut -c1-300; sed -n 360,368p web/d48581c81d7f5ec0.txt; grep -n -E 'v[eē]l[oō]x' refs/LAT.txt | head -5; grep -n -E 'v[eē]l[oō]x' refs/LEW_1910.txt | head -5"
}
```


### [2026-10-16T05:17:11.557Z] TOOL RESULT

```
299: ^ De Vaan, Michiel ( 2008 ), “ vēlōx ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 659-60 
معادل ابجد 229
تعداد حروف 4
تلفظ bozorg
نقش دستوری صفت
ترکیب ( صفت ) [پهلوی: bazurg، مقابلِ کوچک]
مختصات ( بُ زُ ) ( ص . ) 
آواشناسی bozorg
الگوی تکیه WS
شمارگان هجا 2
```


## [2026-10-16T05:17:16.847Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^ ?v.l.x|velox' LAT.txt LEW_1910.txt | head -8; grep -n -i -E '^VELOCITY|^VIGOUR|^VIGOR|^VIGILANT|^VEGETABLE|^WAIT|^WATCH|^WAKE\\b' SKT.txt | head"
}
```


### [2026-10-16T05:17:17.203Z] TOOL RESULT

```
20896:Vigour;  see  Vigil.
21079:WAKE,
21100:Wait.  «b.  and  vb. ;  *«  Wb»1l«  (ty "W^iVQ,    to    relinc^uUh   a  cVivm.   ^P.  — Scand.)     M.  E.   a-aiiwH,  U'^tw*"  Vnwivcn
21111:WAKE.
21134:watch,  sb.    (E)    M.E.  wwrA*;  A.S.
21237:Watch :  sec  Wake  (i).
21334:waiten,  to  roll.     Ct  Coth.  tn-tua/Z/ntt,  lo subvert.     (Base  WALT,  from  V  WAR.)
21335:waits,  a  dance.  (G.1  Short  for  G. waJur,  a  waltz  (with  s  sounded  as  //).• G.  waistM,  to  roll,  revolve  ;  sec  above.
22844:wake,  ware,  wax,  weed,  weld,  well,  wharC; wheal,  wick,  wight,  wUt,  wimble,  windt windlau,  wise,  wit,  wood,  wort,  wont^ wrinkie.
```


## [2026-10-16T05:17:19.922Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Velocity|Vigil[,.]|Vegetable' SKT.txt | head; sed -n 21079,21095p SKT.txt; grep -n -E 'w.it,|Wait,' SKT.txt | head -4"
}
```


### [2026-10-16T05:17:20.309Z] TOOL RESULT

```
20883:\  tee  Vigil.
20896:Vigour;  see  Vigil.
WAKE,
pnblisfa  abroad.  •>  L.  t/'i-,  for  ^&^, uu/gare,  to  publish,  from  uul^t  [\
Vulnerable.  (L. )  1*  uuln liable  to  injuiy. —  L.  uulnerart,  to —  L.vw/H/r-, crude  forrn  oiuHlnuj.i Allied  to  uttlert.  to  pluck.,  tear, vraaa,  a  wound,  Ir&cture.     l^  W>
Vulpine.  fojt-Uke.  (K.-U)  F. Cot.  —  L.  uulpittus,  fox-like,  m  L, crude  fonn  of  uu/j>u^  a  fox.
Vultoire.   (L)     L    uttlemrA lit.  'tearcr.'  — L,  ww/-,  as  in of  uiiUre,  to  pluck,  tear.     Allied nerable.
WA-WE.
Wabble,  Wobble ;  see  Wliap.
Waoke.  a  kind  of  soft  rock.  (G.)  G. uKxrke,  a  stone  consisting  of  quartz,  sand, and  mica.
Wad,  a  small  bundle  of  stuff,  little  mass of  low.  (Scand.^  Swed.  vatfJ.  wadding. O-  Swed.  wad,  clothing,  'tXvSi,  Icel.  vah. tMiii,  wadmal,  a  plain  woollen  stuff.  +  G. UKitte,  wadding,  wad ;  wat.  cloth  (whence V.ouate,8icX  Allied  to  "Weed  (a).  Der. waJd-in^,  waJ-mal.
Waddle ;  see  W^ade.
Wade,  to  walk  slowly,  esp.  through walCT.  ^E.)  A.  S.  waJan,  pt.  t  iwW,  to wade,  go.  -f-  Du.  waden,  Icel.  va^a,  pt. 11^,  to  wade ;  Icel.  va^.  a  ford ;  Dan. vadt,  Swed.  vada,  O.  H.  G.  ivatan,  to wade,  go.  Further  allied  to  L.  tmdum (for  ttadhMm*),  a  ford,  uaJire,  to  go,  SkL gddJta,  shallow.
praddle.  to  walk  clunuily.  (E.)     Fre- quentative of  wade  (above).
Wafer.  (F.-O.  Low  G.)  M.  E.  wa/re. «  O.  F.  wau/re  {¥.  gaufre\  a  wafer. "•  O.  Du.  watffei,  a  wafer  (Da.  UHt/el); Low  G.  wa/ti :  G.  waffel,  wafer.
Waft;  see  Wave  (.i).
Wag;  sec  Weigh.
Wage,  Wager ;  sec  Wed.
Waggle,    Waggon,    Wagtail ;    sec 'elgh.
1762:Bide,  to  await,  wait.  (K  )  M.  E.  biden. A.SMdan.^Uu.beiden;  \cc\.Mtia:  Swed. ^'da ;  Dan.  Inr ;  Goth,  beidan ;  O.  il.  G. fffan-
8589:\0,    ketr)  ;    wa!J,    wait,
10824:imken  *  (not  found).  —  Si Dan.  lusii,  to  lurk,  sneak,  listen ;  C Imeh^H,  to  lurk,  G.  ianuhem,  ti We  also  And  Swed.  lura,  Dan. lurk  ;  G.  laturn,  Icel.  A/orUf  (< (BaseHLU-VKRU)  AlUedto lurch  ( I ).  to  lurk,  dodge,  pilfer. A  weakened  form  of  Lurk.  Th are  (1)  to  lie  in  wait,  lurk,  (a)  t steal.  Der.  lurehtr,  'one  that  % the  lurch,  or  upon  the  catch,  alac of  hunting-dog;''  Phillips. Lury ;  see  Lorj. LtiBcious,  delidoot.  (E. Also  ItuhioHj  (Spenser) ;  Imssywm grave).  Lussyoust  is  prob.  for  An of  which  it  is  an  easy  comiptioo  t by  adding  -out  to  E.  inxty^  pleas licious,  which  is  the  usual  old  t Shak.  bos  lush  (short  for  Uiukigm Chaucer  would  have  &aid  Ituty  \  hi singular  result  that  Shak.  usca  Istfi at  once :  *  How  lush  and  tu^y  tl looks; '  Temp.  ii.  i.  5J ;  see  Loat. Lust.  (E.)  The  ugual  old  mei pleasure.  A.S.  luxt,  pleasure. IceL  lyst,  UsH,  Dan.  /yj/.  Si /Mr/,  Goth,  lustus,  pleasure, formerly  *  pleasant.'  And  see  lusH list  (4),  to  please.  (E.)  U.E. luttH\  'if  thee  imt* ^\i  it Ch.  C.  T,  1185.  A.  S.  ly:tan, used  impersonally.  »  A.  S. (above). +  Du./<Aj/rff,  Icel. /fx/o,  Di Swcd.  lysta,  Goth,  luxton',  G. from  the  sb.
10942:mate  (i),  a  companion,  comrade,  eqtint. (E.)  M.  E.  matt,  a  comipiion  of  the  older form  maie,  a  companion,  which  is  the commoner  form.  (So  also  ^/,  □  mammal, from  M.  E.  6aJk\  and  esp.  note  O.  Fries,  matia (for  rftaJkta*),  to  make,  which  is  a  related word.)*  A.  S.  mofa,  a  companion;  also gemaca.  +  Icel-  wah',  Swcd.  maJtt,  Dan. magt,  O.  Sax.  gimako,  a  mate,  comrade; but  O.  Du.  wait,  Du.  maat,  a  mate,  with  / as  in  English,  douhtic*^  on  O.  Frie-iic  form.
```


## [2026-10-16T05:17:23.190Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^velocity|^vigor|^vigilant|^vegetable|^wait,|^wake,|^watch,|^wait\\b|^wake\\b|^watch\\b' KLN_1966.txt | head -20"
}
```


### [2026-10-16T05:17:23.533Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:17:29.555Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E 'velocity, n.{0,400}' KLN_1966.txt | head -2; grep -n -o -E 'wait, intr..{0,400}|wait, v.{0,400}' KLN_1966.txt | head -2; grep -n -o -E 'vigor, n.{0,300}|vigil, n.{0,300}' KLN_1966.txt | head -3"
}
```


### [2026-10-16T05:17:29.990Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:17:36.116Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'velocity|velox|vēlōx' KLN_1966.txt | head -5; grep -n -i -E 'vigil' KLN_1966.txt | head -5"
}
```


### [2026-10-16T05:17:36.523Z] TOOL RESULT

```
2739:anemology,  n.,  the  science  of  wind.  —  Com¬ pounded  of  anemo-  and  Gk.  -Xoyla,  fr.  -Xoyoc, ‘one  who  speaks  (in  a  certain  manner) ;  one  who deals  (with  a  certain  topic)’.  See  -logy. Derivative:  anemolog-ic-al,  adj. anemometer,  n.,  an  instrument  for  measuring  the velocity  of  the  wind.  —  Compounded  of  anemo- and  Gk.  pixpov,  ‘measure’.  See  meter,  ‘poet¬ ical  rhythm.’
3875:atrium,  n.,  1)  the  central,  courtlike  room  of  the ancient  Roman  house;  2)  ( anat .)  cavity  in  the heart  or  in  the  ear.  —  L.  atrium;  according  to Varro,  De  Lingua  Latina  5,  §  161,  a  word  of Etruscan  origin  and  rel.  to  the  Etruscan  town Atria,  as  the  place  of  origin  of  this  kind  of  ar¬ chitecture.  The  connection  of  atrium  with  ater, ‘black,  dark’,  is  folk  etymology, atrocious,  adj.,  extremely  cruel  or  wicked.  — Formed  with  suff.  -ous  fr.  L.  atrox,  gen.  atrdcis, ‘cruel,  fierce’,  prop,  ‘dark-looking,  gloomy’, and  compounded  of  ater,  ‘black,  dark’,  and -ox,  gen.  dcis,  ‘looking’.  For  the  first  element  see atrabilious.  The  second  element  is  cogn.  with Gk.  1,  gen.  cot to?,  ‘eye,  sight’.  See  -ops  and  cp. the  second  element  in  ferocious,  velocity. Derivatives:  atrocious-ly,  adv.,  atrocious-ness. atrocity,  n.,  atrociousness.  —  F.  atrocite,  fr.  L. atrocitdtem,  acc.  of  atrocitas,  ‘cruelty’,  fr.  atrox. See  prec.  word  and  -ity.
10484:Derivatives:  deceiv-abil-ity,  n.,  deceiv-able,  adj., deceiv-able-ness,  n.,  deceiv-abl-y,  adv.,  deceiv¬ er,  n.,  deceiv-ing,  adj.,  deceiv-ing-ly,  adv. decelerate,  tr.  v.,  to  decrease  the  velocity  of; intr.  v.,  to  decrease  in  velocity.  —  Formed  on analogy  of  accelerate  fr.  de-  (in  the  privative sense  of  this  pref.)  and  celeratus,  pp.  of  celerare, ‘to  hasten’.
14244:eye,  n.  —  ME.  eige,  eye,  eie,  fr.  OE.  eage,  rel.  to OS.  oga,  OFris.  age,  ON.  auga,  Swed.  oga,  Dan. oie,  OFris.  age,  MDu.  oghe,  Du.  oog,  OHG. ouga,  MHG.  ouge,  G.  Auge,  Goth,  augo,  ‘eye", fr.  I.-E.  base  *oqu-,  ‘to  see;  eye’,  whence  also OI.  dksi,  gen.  akfnah,  ‘eye’,  akfdh,  ‘die’,  fkfate. ‘sees’,  Toch.  A  ak,  B  ek,  ‘eye’.  Arm.  akn,  gen, akan,  ‘eye,  opening,  hole’,  Gk.  6xxo?,  ‘eye’, Sane  (for  oqwi-),  ‘the  two  eyes’,  fiaaeafiai,  ‘to see,  look  at,  presage’,  6 xrfj,  ‘opening,  hole', 6^o[jiai,  ‘I  shall  see’,  671x6?,  ‘seen;  visible’, 671x1x6?,  ‘pertaining  to  sight’.  Alb.  sii,  ‘eye’,  L. oculus,  ‘eye’,  OSlav.  oko,  ‘eye’,  okno,  ‘window", Lith.  akis,  ''eye'.  Fr.  *oqm-,  collateral  form  of base  *oqw-,  derive  Gk.  £r\>,  gen.  cixo?,  ‘eye, face’,  and  the  second  element  in  L.  atrox, ‘cruel,  fierce’,  ferox,  ‘wild,  savage’,  velox,  ‘swift, quick’.  Cp.  eyelet,  ogle  and  the  second  element in  daisy,  walleyed,  window.  Cp.  also  ocular, omma,  optic,  ullage,  the  first  element  in  ophthal- mo-  and  the  second  element  in  antler.  Cp.  also the  second  element  in  atrocious,  ferocious, velocity.  Derivatives:  eye,  tr.  v.,  ey-ed,  adj.
14589:femandinite,  n.,  a  hydrous  calcium  vanadyl  vana¬ date  {mineral.)  —  Named  after  Eulagio  E.  Fer- nandini,  from  whose  vanadium  deposit  it  was first  obtained.  For  the  ending  see  subst.  suff.  -ite. ferocious,  adj.,  fierce.  —  Formed  with  suff.  -ous fr.  L.  ferox,  gen.  ferocis,  ‘wild,  savage,  un- tameable,  bold*,  prop,  ‘wild-looking’,  fr.  ferus, ‘wild’,  and  -ox,  gen.  -ocis,  ‘looking’.  For  the etymology  of  L.  ferus  see  fierce.  The  second element  in  L.  fer-ox,  ‘wild’,  is  cogn.  with  Gk. totji,  gen.  ‘eye,  sight’.  See  eye  and  cp.  -ops. Cp.  also  the  second  element  in  atrocious, velocity.
19832:Derivatives:  invidious-ly,  adv.,  invidious-ness,  n. invigilate,  tr.  v.,  to  keep  watch  over.  - —  L.  invigi¬ lates,  pp.  of  invigilare,  ‘to  be  awake,  be  watch¬ ful,  watch  over’,  fr.  in-,  ‘in’,  and  vigilare,  ‘to watch,  be  awake’,  fr.  vigil,  ‘awake,  wakeful’. See  vigil  and  verbal  suff.  -ate.
19833:Derivatives:  invigilat-ion,  n.,  invigilat-or ,  n. invigorate,  tr.  v.,  to  make  vigorous.  —  Formed fr.  in-,  ‘in’,  L.  vigor,  ‘strength’  (see  vigor),  and verbal  suff.  -ate.
28163:Derivative:  periheli-al,  adj. peril,  n.,  danger.  —  ME.,  fr.  OF.  peril  (F.  peril), fr.  L.  periculum,  ‘trial,  experiment,  risk,  danger’, which  is  rel.  to  peritus,  ‘experienced’,  experiri, ‘to  try,  prove,  test’,  and  cogn.  with  Gk.  raipa, ‘trial,  attempt,  experience’,  Spratpo?,  ‘exper¬ ienced’,  Arm.  p'orj,  ‘trial,  attempt’,  OIr.  aire, ‘vigilance’,  Mir.  airim,  ‘I  am  awake,  watch’, Goth,  ferja,  ‘watcher’,  OE.  fser,  ‘danger,  fear’. Cp.  empiric,  experience,  experiment,  expert,  pi¬ rate.  Cp.  also  fear.  All  these  words  derive  fr. I.-E.  base  *per-,  ‘to  lead  across’,  which  is  ult. identical  with  base  *per-,  ‘through,  across, beyond’.  See  per  and  cp.  words  there  referred  to. Perilla,  n.,  a  genus  of  plants  (bot.)  —  ModL.,  fr. Sp.  perilla,  dunin.  of  per  a,  ‘pear’,  fr.  VL.  pira,  fem. sing.,  for  L.  pira,  pi.  of  pirum,  ‘pear’.  See  pear, perilous, adj. .dangerous.  —  ME.,  fr.  OF.perillous, perilleus  (F.  perilleux),  ‘dangerous,  hazardous’, fr.  L.  periculosus,  fr.  periculum,  ‘danger’.  See peril  and  -ous.
32672:reveille,  n.,  signal  on  a  drum  or  a  bugle  at  sun¬ rise.  — -  F.  reveillez(-vous),  'wake  up  ,  imper.  of (ve)  reveiller,  ‘to  wake  up’,  fr.  MF.  reveiller,  ‘to awake,  rouse’,  fr.  re-  (see  re-)  and  eveiller,  fr. OF.  esveillier,  fr.  VL.  *ex vigilare,  fr.  1st  ex-  and L.  vigilare,  ‘to  watch'.  See  vigil, revel,  intr.  v.,  to  feast  in  noisy  manner.  —  ME. revelen,  fr.  OF.  reveler,  ‘to  rebel,  revolt,  make an  uproar’,  fr.  L.  rebellare,  ‘to  wage  war  again, revolt’.  See  rebel.
37615:surround,  tr.  v.  —  ME.  surrounden.  The  word  orig. meant  ‘to  overflow’,  and  derives  fr.  MF.  so- ronder ,  ‘to  overflow’,  fr.  OF.,  fr.  Late  L.  super - undare  of  s.m.,  fr.  super-  and  L.  unda,  ‘wave’. See  undate  and  cp.  abound.  E.  surround  was  in¬ fluenced  both  in  form  and  meaning  by  an  er¬ roneous  association  with  the  adjective  round. Derivatives:  surround,  n.,  surround-ed,  adj.,  sur- round-ed-ly,  adv.,  surround-er ,  n.,  surround-ing, adj.  and  n.,  surround-ings,  n.  pi. surtax,  n.,  an  extra  tax.  —  Formed  on  analogy  of F.  surtaxe,  fr.  sur-,  ‘above’,  and  tax,  n. Derivative:  surtax,  tr.  v. surtout,  n.,  overcoat.  —  F.,  lit.  ‘an  over  all’,  fr. sur,  ‘on,  upon,  over,  above’,  and  tout,  ‘all’,  fr.  L. lotus.  See  sur-,  ‘above’,  and  total.  For  sense  de¬ velopment  cp.  E.  overalls. surveillance,  n.,  watch  kept  over  a  person;  super¬ vision.  —  F.,  ‘supervision’,  lit.  ‘a  watching  over’, fr.  surveiller,  ‘to  watch  over’,  fr.  sur-,  ‘above’, and  veiller,  ‘to  watch’,  fr.  L.  vigilare,  ‘to  be awake’,  fr.  vigil,  ‘awake,  wakeful’.  See  vigil  and -ance.
```


## [2026-10-16T05:17:45.559Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -i -E 'velocity,? n\\..{0,500}' KLN_1971.txt | head -2; grep -n -o -i -E 'vigor,? n\\..{0,300}' KLN_1971.txt | head -2; grep -n -o -i -E 'wait,? (intr|tr)\\..{0,400}' KLN_1971.txt | head -2"
}
```


### [2026-10-16T05:17:46.088Z] TOOL RESULT

```
259964:velocity, n., swiftness; speed. — MF. (— F.) velo- 
24041:wait, tr. v. — ME. awaiten , fr. ONF. await ter , 
264473:wait, intr. and tr. v. — ME. waiten, ‘to watch’, fr.
```


## [2026-10-16T05:17:53.164Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 259964,259975p KLN_1971.txt; echo; sed -n 264473,264484p KLN_1971.txt; grep -n -E '^vigor, n|^vegetable, adj|^vigilant|^vigil, n' KLN_1971.txt | head"
}
```


### [2026-10-16T05:17:53.536Z] TOOL RESULT

```
velocity, n., swiftness; speed. — MF. (— F.) velo- 
city, fr. L. velocitatem, acc. of velocitas, ‘swift- 
ness’, fr. velox, gen. - ocis , ‘swift’, which is of 
uncertain origin. It possibly stands for * weg-slo-s 
and lit. means ‘moving along quickly, rushing’, 
and is rel. to vehere , ‘to carry, convey’. See 
vehicle and -ity and cp. velites. 
velours, n., a velvetlike material. — F., alteration 
of OF. velous , fr. OProven?. velos, of s.m., fr. L. 
villdsus, shaggy’, taken as a noun, from villus, 
‘shaggy hair’. See villus and cp. velure. Cp. also 
flue, ‘fluff’. 

wait, intr. and tr. v. — ME. waiten, ‘to watch’, fr. 
ONF. waitier , corresponding to OF. guaitier , 
gaitier, ‘to watch* (whence F. guetter, ‘to watch, 
lie in wait for’), fr. Frankish *wahtdn , which is 
rel. to OS., OHG. wahta, Du. wacht, MHG. 
wahte, G. Wacht , ‘watch’, and to OHG, wah- 
hen, wahhon , OE. wacian, ‘to be awake’. See 
wake, v., watch, and cp. wait, ‘singer’. 
Derivatives: wait, n., the act of waiting, wait- 
ing, n. and adj., wait-ing-ly , adv. 
wait, n., one of a band of persons singing Christ- 
mas carols. — ME. wait , ‘watchman’, fr. ONF. 
259816:vegetable, adj. — ME., fr. Late L. vegetabilis , 
261978:vigil, n. — ME. vigile, fr. OF. (= F.) vigile, fr. 
261991:vigilant, adj., alert; watchful. — ME., either fr.
```


## [2026-10-16T05:18:03.359Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'vazra|vajra|vazarka|buzurg' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n -E 'vazra|vajra|buzurg|bāzīdan|bazidan|vāja' IEC.txt | head"
}
```


### [2026-10-16T05:18:03.755Z] TOOL RESULT

```
23001: -m    „Donnerkeil           (des      Indra)“ = av. vazra-            „Keule.       bes.          Haukeule (des
23031:wachnr wakar „regsam, frisch, wacker“ (formell = ai. vajra -, av. vazra -)
23039:ai. vaja-h. Zu ivacker, vajra- vielleicht auch ahd. waits „scharf (nicht                                 -<
649:apo-teros ‘further, following’. WP I, 47. Cf. apo, -teros Skt. OPer. apataram; Arm. var, varo, i vajr, vajra- ‘down, below’; Gk. apóteros; Cor. ater, adar “out of, without’; Go. aftaro (:Gk. apo- . téro); OHG aftaro; ON aptr, eptir; OE efter
19650:uá$-, uàgəros lively, dashing, flashing; dash, élan'. Skt. vajah, m. ‘speed, vigour’; vájrab, m. ‘thunderbolt’; Ober cf. vazraka-, adj. ‘great’; Per. buzurg, id.; W gwair, góer, adj. ‘fresh, keen, lively; OHG wackar, wahhar, d: OE wacor ‘vigilant’; ON vakr, f: vokr ‘alert’; Sw. vacker “fine, noble, great, lively, beautiful; (long-gde in) Go. wokrs, m. ‘yield’; MHG wuocher, sm. ‘usury’; OE wocor, f. ‘growth, progeny’
19825:ue£ó, eið (2) ‘rouse, make move; move’. Cf. aueĝ-. WP cf. I, 246 & I, 669 Skt. vajāmi, v. "eo: (long-gde in) vajah, m. ‘speed, vigour, gain’; Av. vaz-, v. ‘reinforce’; cf. važdris, m. ‘doer, achiever’; Per. bāzīdan, inf. ‘play’; Tokh. A cf. wac, s. ‘fight’; Gk. cf. aékso, tr. ('increase', fr. *auegs- or *nue8s-); Lat. vegeo, ere, v. ‘thrive, stir; W cf. gwaint & gwain, adj. ((brisk, smart, fr. *uegont, *uegnt-); MHG wicken, v. “jump, dance”; Eng. dial. wick, adj. ‘alive’; (uncertainly) cf. Gk. ep-eígo, v. tr. (press, drive, urge, hasten’, if fr. *epi-uegio)
```


## [2026-10-16T05:18:15.305Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 19640,19650p IEC.txt | cut -c1-200; awk 'NR>=19600 && NR<=19830 && /^ *1[45][0-9][0-9] *$/ {print NR\": \"$0}' IEC.txt; sed -n 19820,19826p IEC.txt | cut -c1-150; sed -n 23025,23045p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-200"
}
```


### [2026-10-16T05:18:15.937Z] TOOL RESULT

```
vaó, n., Sw. vad, n. id.; (long-gde in) ON væðr and æðr “fordable?
uag- (1) *wandering, swaying'. Cf. uang- Lat. vagus, vagulus, adj. ‘wandering’; vagor, vagari, v. ‘wander’; MHG cf. wackeln, v. 'tot- ter; dodder’; Sw. (fr. Ger.) vackla, Dan. vakle, id.; cf. ON vakka
uag- (2) *wet; water Gk. cf. -agos, eos, n. (in pél-agos “open seg’, lit. ‘pleine mer’; ten-agos, n. “low water, cf. fenio, etc.); Du. wak, adj. ‘wet, damp’; ON vokr, id. beside vokva, f. ‘moisture’; 
(uàg-, uàgər-, see uàgər-)
uāgh- (1) “weigh, depress, press’. Cf. uogh- (as an alternative) Skt. vāhe, v. ‘press’; Srb. Cz. važiti, vážit, inf. ‘weigh’; OCS cf. vaga, f. ‘weight’; Cz. váha, f. ‘balance’; (SI. LW in) Li. vóga ‘w
uāgh- (2) ‘bitter’ LG woge, adj. id.; Li. vogùs, adj. id.
uagh- (uåghos) (3) ‘surge, billow, swell’. WP L 215 Ir. fágh, fágha, f. id.; G. (fr. LG) Woge, f. (*wave'. LW in Fr. vague; links w. It. voga ‘rowing; vogue; impetus’, whence Fr. vogue, uncertain. À t
1485
vóga *clod, sod")
uaghlos, us (variant: uaghulos) ‘faint, dim; faintness, dimness'. Cf. WP I, 41 Gk. akhlüs, gs: -àos, f. ‘dimness, weak sight ; Phryg. aglíe, f. ‘cast in eye’; Alb. vágull, adj. “dim, faint, weak-sigh
uá$-, uàgəros lively, dashing, flashing; dash, élan'. Skt. vajah, m. ‘speed, vigour’; vájrab, m. ‘thunderbolt’; Ober cf. vazraka-, adj. ‘great’; Per. buzurg, id.; W gwair, góer, adj. ‘fresh, keen, liv
19611: 1482
19623: 1483
19637: 1484
19647: 1485
19664: 1486
19676: 1487
19694: 1488
19701: 1489
19717: 1490
19729: 1491
19744: 1492
19751: 1493
19766: 1494
19776: 1495
19789: 1496
19796: 1497
19812: 1498
19821: 1499
uëghros, is (uëghlis) ‘slim, tiny’ Arm. girg, adj. ‘tender, delicate’; Alb. i vogërr,
1499
adj. “stunted”; beside i vogël, adj. ‘small’; Ir. cf. fíghe fíghe “trifle, triviality”
ueĝer- (uegor-) ‘rouse; lively’. Cf. ueg20, uo- Leið, uoĝeros Hitt. cf. wakariya(mi), wagar-, v. incite’, prob. o-gde); Gk. egeíro, v. id.; cf. Lat. v
uégo- (1), element of the following (?) Av. cf. vazaya, f. ‘lizard’; Per. vazaq, s. ‘frog’; Li. véZys, m. ‘crab, crayfish’; veZlys, m. “tor- toise’; L
ue£ó, eið (2) ‘rouse, make move; move’. Cf. aueĝ-. WP cf. I, 246 & I, 669 Skt. vajāmi, v. "eo: (long-gde in) vajah, m. ‘speed, vigour, gain’; Av. vaz-
uegh- “carry, convey, transport; conveyance, roadway, means of transport. WP I, 249. Cf. uogh- Skt. váhami, v. ‘convey, transport'; Av. vazà- mi, v. “

(:                wokains
  lat. vigil ) ; got.     f. „das \Yachcn“  anord. vakr ags. waco>\ ahd.
                                                                     ;                   ,


wachnr wakar „regsam, frisch, wacker“ (formell = ai. vajra -, av. vazra -)
             ,

anord. vaskr „munter, flink“ ( *vnk-ska  Fiek III 4 380) die Bed. von ags.           ;


wcecnan „geboren werden" erklart auch die Bed.-Entwickung von got.
wokrs usw. (s. unter Wz. *aiieg- „vermehren“), vgl. in der Yokalstufe auch
ai. vaja-h. Zu ivacker, vajra- vielleicht auch ahd. waits „scharf (nicht                                 -<



zu uogjjini- „Pflugschar“).
                           99 f. Vf. LEWb. 2 812, Falk-Torp 1573 unter
  Lit. z. B. bei Zupitza GG.                    1
```


## [2026-10-16T05:18:21.715Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22990,23010p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-200; awk 'NR<=23001 && /\\[pdf page/ {l=$0} NR==23001{print l}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-16T05:18:22.051Z] TOOL RESULT

```
 bei der Wiederkehr derselben Bed. auf germ, und slav. Gebiete doch
 ganz problematisch bleibt.

 neg- ,,frisch. rege,             kriiftig sein *.

      Lat. regpo.   -err.        „in   Bewegung setzen, antreiben**. daraus (nach vigil aus
 *>:egil)   vigeo, -ere          ,.frisch    und   kriiftig sein.     in   Kraft und Ansehen stehn“,
 rrgetus „riihrig. lebhaft. munter**, rigii ,,wach. wachsam**                                     vigil are , rigilia ):
                                                                                              (
    Ai. raja-h ,.Kraft. Schnelligkeit, Wettkampf, Kampfpreis, Gewinn, wert-
 volles Gut**, riijdi/ati „regt an. treibt zur Eile: lauft urn die Wette**, vdjm-h,
 -m    „Donnerkeil           (des      Indra)“ = av. vazra-            „Keule.       bes.          Haukeule (des
                                                                                                                      ; ,




Mithra)",         ap. vasarka-           „gro8‘'    (nach Bartholomae Altiran. Wb. 1390 aus
iran.       *uazrka-, Ableitung von *uazar n.,               vgl. vazarot- ..mit Energie, Kraft,

Macht sich aufmachend“ aus *vaza- m. — arot).
```


## [2026-10-16T05:18:35.465Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -E 'BOZORG|GORZ|BAXTAN|BAZIDAN|BÂXTAN|BOZOR' ARY_latin_index_pages.txt | head; grep -n -E '^ *(بزرگ|گرز|باختن|بازیدن)' ARY_pages.txt | head"
}
```


### [2026-10-16T05:18:35.779Z] TOOL RESULT

```
3236:BAXTAN, BAXSHISHN, BHAJ.,
```


## [2026-10-16T05:18:40.738Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 3225,3245p ARY_latin_index_pages.txt; grep -n -E 'بزرگ|گرز' ARY_pages.txt | head -10"
}
```


### [2026-10-16T05:18:41.120Z] TOOL RESULT

```
BUCK: 1095 BHAKSHATI (SANSKRIT) 2, Ss
AMINDAROV: 13 BOGATE ARMENIAN) ga)
rid iebv by (OLD CHURCH SLAVIC) 245 5 s%e\
icetloal
: sty THY
[pdf page 114]
i, !
VO | ghtdy Ode be
PHAGEIN (GREER) gly BREH, BRAY, BAG, :(AVESTAN) gles!
(OLD CHURCH SLAVIC) oS 5 5% BAXSHAITI, BAGHA-
BOGU, UBOGU BAXSH, BRIN, (PAHLAVI) 5 3
BAXTAN, BAXSHISHN, BHAJ.,
‘REFERENCES beth BAXSHITAN
POKORNY SSS~S~*~*~«OT (SANSKRIT) eS
MACKENZIE: 17, (BESTOWAL) 104 BHIKSHATE, BHAJI.,
THI gi he iebbly BHAG, BHAGAH, BHAJATI
BOGATU ARMENIAN) a,
deaths
Tg See yeti
12g ty 05 22 5s cal et
valet arly gene Sh "Eat Leall slushy
47:«هند و اروپایی» نامی است که به خانواده‌ی بزرگی از زبانها داده می‌شود. این خانواده شامل
75:خانواده‌ی بزرگك از هندوستان و فلات ایران تا باختر اروپا و بریتانیای کبیر گسترش دارند. برخی
82:تنها در اشاره به یک خانواده‌ی بزرگك زبانها بلکه در اشاره به تیره‌ی بخصوص از نژاد سفید بکار
117:اطراف آنها دارای وسعت نسبتاً کمی هستند و بعید است سرچشمه‌ی کوج‌های بزرگی باشند که تا مرکز؛
292:بوده‌اند و تحرکك و تفوقی که سوارکاری و ترابری به آنها داده عامل بزرگی در گسترش آنها بوده
326:(16780۸71) ساخته شده. در کنار جسد گنجانه‌ی سفالی (و در مورد بزرگان قوم) اسلحه و سپر قرار . ذٌ
327:دارد. استخوان اسب موجود درکنار برخی جسدها نشان می‌دهد که اسب بزرگان را با جسد آنها دفن .|
634:نظر شمار سخنگویان (بیش از یک میلیارد نفر) بزرگترین خانواده‌ی زبان‌های هند و اروپایی
636:کتابها این دو خانواده‌ی بزرگ را با هم تحت عنوان «زبانهای هند و ایرانی» (12100-78۸011۸37)
816:ولی درگذشته‌ی نزدیکك بخش بزرگی از شمال خاوری ترکیه هم ارمنی نشین بود.
```


## [2026-10-16T05:18:45.372Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -E 'VAZRA|VAJRA|VAZARKA|VAZRKA|WUZURG|VAZURG|VAJA\\b|VEGERE|VIGIL|WAKE' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-16T05:18:45.724Z] TOOL RESULT

```
3648:WACAN, (OLD ENGLISH) oS lS} VAZRA AVESTAN) glee!
3649:WECCAN VAZRAKA, :(OLD PERSIAN) oles p+,
3650:WAKE ENGLISH) SS} VAZARKA
3651:VAAGE DANISH) Sails ‘WUZURG, BAZURG (PAHLAVI) (5 4,
3654:WAKEN x(DUTCH) (sce VAJA, VAIRA SANSKRIT) cy Sule
3656:REFERENCES taenthay VEGERE LATIN) 5
3658:BARNHART: (WAKE) 1216 VAK {OLD SCANDINAVIAN) Ss-the!
3661:SKEAT: (WAKE) 698 WAKA
3663:wr sbi iby WAKEN, WAHHEN
14400:NAVE (ITALIAN) .yiSes\ NAV, NAVAJA, (SANSKRIT) cy Site
```


## [2026-10-16T05:18:47.952Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 3630,3670p ARY_latin_index_pages.txt; grep -n '\\[pdf page 1[23][0-9]\\]' ARY_pages.txt | head -30"
}
```


### [2026-10-16T05:18:48.272Z] TOOL RESULT

```
BECCO (SPANISH) g\ ile!
REFERENCES Ucathany (OLD SCANDINAVIAN) i655 hes!
POKORNY: 114 BUKKR
BARNHART: (BUCK) 122 BUKKR (OLD NORSE) pS es5
DELAMARRE: 132 BOCK HOLD SAXON) pS gi pS
‘MACKENZIE: (Goat) 116 OLD HIGH GERMAN) pS galt
BUCK: 164-166 BOC, BUKKA
ONIONS: (BUCK) 122-123 BOCK GERMAN) glST
SKEAT: (BUCK) 77 BUC, HOLD ENGLISH) pS 51531
AMINDAROY: (GOAT) 231 BUCCA
MALLORY & ADAMS: BHUGOS BUCK ENGLISH) 153)
rvi-rvr road Olay BUK DANISH) 5 jila
[pdf page 128]
ee
| ; ,
4 | Sy nee, ws
oO vo
|
WACAN, (OLD ENGLISH) oS lS} VAZRA AVESTAN) glee!
WECCAN VAZRAKA, :(OLD PERSIAN) oles p+,
WAKE ENGLISH) SS} VAZARKA
VAAGE DANISH) Sails ‘WUZURG, BAZURG (PAHLAVI) (5 4,
vAKA (SWEDISH) «58 yo WASIR {(TOKHARIAN A) A «555
VAKE s(NORWEGIAN) $535 WASIR :(TOKHARIAN B) B (5 )\at
WAKEN x(DUTCH) (sce VAJA, VAIRA SANSKRIT) cy Sule
VZRUK, VZURK — (ARMENIAN) 5,1
REFERENCES taenthay VEGERE LATIN) 5
poKORNY, =SOS~*~*~S~S~«SaT WAKAN (GOTHIC) 38
BARNHART: (WAKE) 1216 VAK {OLD SCANDINAVIAN) Ss-the!
MACKENZIE: (BIG) 104 WAKON — (OLD SAXON) 5 giy-S te
BUCK: 878-880 WAKIA, (OLD FRISIAN) oS $32.9
SKEAT: (WAKE) 698 WAKA
MALLORY: a) | (OLD HIGH GERMAN) pS gt
wr sbi iby WAKEN, WAHHEN
WACHEN GERMAN) gist
lenthooy
ee pty gh ey Stl 9 Sly gal ge
2S 0 MB AE gly Cbd gta) GUUS 22 Sy cal
Spe sctigvabs palsalae :
u
BASTAN APAHLAVD) (5 ghey BANDH-, HAVESTAN) glee 3\
3489:[pdf page 120]
3518:[pdf page 121]
3554:[pdf page 122]
3583:[pdf page 123]
3615:[pdf page 124]
3644:[pdf page 125]
3672:[pdf page 126]
3700:[pdf page 127]
3731:[pdf page 128]
3761:[pdf page 129]
3790:[pdf page 130]
3817:[pdf page 131]
3845:[pdf page 132]
3875:[pdf page 133]
3906:[pdf page 134]
3938:[pdf page 135]
3970:[pdf page 136]
3995:[pdf page 137]
4021:[pdf page 138]
4051:[pdf page 139]
```


## [2026-10-16T05:18:55.817Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 3731,3761p ARY_pages.txt"
}
```


### [2026-10-16T05:18:56.225Z] TOOL RESULT

```
[pdf page 128]
نگ کی .
: ۱
0 بزرگ / ۱۳۹
ل
اوستایی (487۸4): ۷۸۸ آنگلیسی کهن (0ل8ال2(/0 ۰:0۵ ,۷/۸۲۸۷
پارسی باستان (۶8514/7 012): بشلف۷۸2 ۷۸
۷۸7۸6۸ انگلیسی (8۸01/538): ۷۸5
پهلری (/(۵ا(۳۸): 8۸286 ,۲:26 دانمارکی (0۸27]577): ۷۸۸025
تخاری 4 (۸ ۷(ل7072۸#): ۳۹ سرئدی (7ل352(8): ۰ ها /
تخاری 8 (8 (9مل#م7ل70): 3 ان نروژی (۷ل014 7077۷5 ۷۸
سانسکریت (84288707): ۸۸ ۷2۸ هلندی (0076[7). ده ۱
ارمنی (4ف/0/80/): ۰ ۷21786 ب6ا[ا :۷2
لاتین (۸7/2ا): ۷۹ پسگشت‌ها 5
گوتیک (007710): ۸۵۵۷ زا
ایسلندی‌کهن (۵07 00ید صام: ۸ 6 (۷۸6۳) :8۸7
ساکسرنی کهن (54200۸ 0۵): ۰ ۷۷۸۵۲ 4 (8[0) :۸1۸55/258
فریزی کهن (/۲۸-540 00): بش۱۸ 30 ین
۱/۸۸ 8 (8۸36) : 57
آلمانی کهن ((02704۸ ا0الز ان): اوه یهام
7 ,۷۷۸3۲ برهان قاطع + ۷۲
آلمانی (0872/۵): لد اه
یادداشت:
معنی این واژه در سانسکریت: یرو؛ سرعت.
.۰ معنی اين واژه در زبان‌های ژرمنی: بیدار» بیدار شدن» نظاره کردن.
‌ ۰ معلی این واژه در زبان لاتین: شاد و خرم کردن.
1 1
اوستایی (4887۸27): ,8۸/۷01 پهلری ال ۸): 8۸7۸7
,8۸107۸۸ ,8۸011۸۸7 کردی (00137): زد اند [ دی(
پارسی پاستان (28۲۶4(۷ صا0): 8۸87۸ سانسکریت (54(/۶8/7): ۰ 38۸0۸3۸171
[pdf page 129]
```


## [2026-10-16T05:19:02.872Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'vazurg|wuzurg|vazr\\b|vazra|vāzīdan|vazidan|wāzīdan' MON_part1.txt MON_part2.txt | head"
}
```


### [2026-10-16T05:19:03.299Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:19:10.513Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://abadis.ir/fatofa/گرز/' 'https://abadis.ir/fatofa/باختن/' 'https://abadis.ir/fatofa/بازیدن/'; do p=$(python3 tools/fetch_source.py \"$u\" --note \"page 530, root Weg 2: Mo'in entry\" 2>&1 | tail -1); echo \"## $p\"; grep -n -E 'پهلوی|اوستا|\\[|معین' \"$p\" | head -12 | cut -c1-200; done"
}
```


### [2026-10-16T05:19:14.801Z] TOOL RESULT

```
## /home/sfmqrb/git/rishe-private/data/verification/sources/web/78bc7204592b8652.txt
20: گرز. [ گ ُ ] ( اِ ) پهلوی وزر ، اوستا وزرا ، معرب آن جُرز، ارمنی ورز ، هندی باستان وجره ( گرز رعد [ ایندرا ]، کردی گورز . و رجوع به گرزه شود. ( از حاشیه برهان قاطع چ معین ). عمود آهنین. ( برهان ).
46: گرز. [ گْرُ / گ ِ رُ ] ( اِخ ) ژان باتیست. نقاش فرانسوی ، متولد در تورنوس ( 1725-1805 م. ) ( سون و لوار ) . وی در ساختن صحنه های خانوادگی و تصاویر اشخاص مهارت داشت و آثار عمده او عبارتند از: نامزد
50: ژان باتیست نقاش فرانسوی ( و . ۱۷۲۵ ف. ۱۸٠۵ م . ) . وی در ساختن صحنه های خانوادگی و تصاویر اشخاص مهارت داشت . آثار مهم وی عبارتند از : [ نامزد دهکده ] [ لعنت پدری ] [ پسر تنبیه شده ] [ پرنده مرده ]
54: فرهنگ معین
56: (گُ ) [ په . ] (اِ. ) عمود آهنین ، کوپال . 
74:این واژه در پارسی میانه به ریخت وَزر ( wazr ) بوده است. همچنین در این زبان به گرز، گَد ( gad ) هم می گفتند که از اوستایی گَدا - ( - gadā ) گرفته شده بود. 
118: ... [مشاهده متن کامل] 
128:لینک کتاب فرهنگ واژه های اوستا
131: ... [مشاهده متن کامل] 
135:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
137:• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
141:این واژه با ریخت� vazra� در اوستایی آمده است .
## /home/sfmqrb/git/rishe-private/data/verification/sources/web/e232138a2af1a182.txt
14: معنی انگلیسی : to lose , [game.] to lose , [fig.] to give away , [lit.] to play 
20: باختن. [ ت َ ] ( مص ) لازم و متعدی هر دوآمده است. مقابل بردن ، در قمار. گم کردن در قمار. زیان کردن در قمار. باختن چیزی بگرو. مقامره. ( منتهی الارب ). تقامر. ( منتهی الارب ) ( کازیمیرسکی ). قمار با
25: || ورزیدن. کردن. || بازی کردن. ( غیاث ). مشغول شدن. سرگرم شدن : گوی ، نرد، شطرنج باختن : قلی قلواً؛ غوک چوب [الک دولک ] باخت. ( منتهی الارب ). گوز باختن ؛ گردوبازی کردن : 
55: فرهنگ معین
64:۴. (مصدر لازم ) [قدیمی] بازی کردن: چوگان باختن. 
89: ... [مشاهده متن کامل] 
103:پختن در زبان مازندرانی ( زبان پهلوی ) بَپِتِن بوده که با تبدیل پ به ف بفتن و سپس بفتن به بافتن تغییر یافت 
104: ... [مشاهده متن کامل] 
127: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آ
## /home/sfmqrb/git/rishe-private/data/verification/sources/web/2671edfd26f53f44.txt
16: بازیدن. [ دَ ] ( مص ) بازی کردن. باختن. ( شعوری ج 1 ص 180 ) ( ناظم الاطباء ) ( حاشیه برهان قاطع چ معین ) : 
63: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن
```


## [2026-10-16T05:19:28.679Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=split($0,L,\"\\n\"); for(i=1;i<=n;i++) if (L[i] ~ /باختن|بازیدن|بازیدن/) print NR-1\": \"L[i]}' BQT_v1_pages.txt | head -12"
}
```


### [2026-10-16T05:19:29.194Z] TOOL RESULT

```
248: ]ر هدن « با زای هوز بر وزن بازیدن حطی و غین قطهدار ۰ تنفر و نفرتی را کویند
441: ۵ از دید باختن , بازی کردن ۰
604: پرداختی "هبروزن سر باختن؛ بمعنی
622: ز اخقی ه بفتح اول بر وزن نباختن ,
```


## [2026-10-16T05:19:33.823Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==442' BQT_v1_pages.txt | grep -n -E 'باخت|باز|پهلوی|vāz|۱ -|۲ -' | head -20"
}
```


### [2026-10-16T05:19:34.176Z] TOOL RESULT

```
7:«بازبرة اول وبازبر؛ آخر» » مراد از آن پاره‌ای
54:۵ از دید باختن , بازی کردن ۰
```


## [2026-10-16T05:19:38.164Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'buzurg|vazarka|vazrka' SYN.txt | head -5; grep -n -E 'gurz|vazra' SYN.txt | head -5; grep -n -E 'vigil|wacian|wacan' SYN.txt | head -5"
}
```


### [2026-10-16T05:19:38.595Z] TOOL RESULT

```
22437:Rum. mare NE large, big (great) Russ.  bol’§oj (velikij) Ir. mar, bras(s), oll Du. groot Skt. mahant-, mah- NIr. mar OHG = mihhil, groz Av. mazant-, maz-, W. mawr MHG gréz, michel masan-; OPers. Br. bras NHG gross vazarka-
22466:OPers. vazarka- (‘great’ king and ‘great’ = ‘large’ earth) : Skt, vaja- ‘speed, vigor, contest’, vajra- ‘thunder- bolt’, Av. vazra- ‘club’, Lat. vegére ‘set in
34676:Ay. vazra~ (Barth. 1392) = Skt. vajra- “Indra’s thunderbolt’ : Skt. vdja- ‘strength’, OPers. vazarka- ‘great’, etc. Walde-P. 1.246 f.
1814:6. Skt. vajra-, a term of mythology, Indra’s ‘thunderbolt’ : Av. vazra- ‘club’, NPers. gurz ‘club’. }
22466:OPers. vazarka- (‘great’ king and ‘great’ = ‘large’ earth) : Skt, vaja- ‘speed, vigor, contest’, vajra- ‘thunder- bolt’, Av. vazra- ‘club’, Lat. vegére ‘set in
34634:as- ‘throw’. Uhlenbeck 19. Walde-P. | 298 ff. Macdonell-Keith, 2.591 f. with 1.134. refs. Geiger, Ostiranische Kultur 441 ff. 20.22 CLUB Grk.  pdradov, kopbyn, EbAov Goth. (¢riu) Lith. kuoka, kilé NG  pérado, parcobxa ON klumba, klubba, kylfa, Lett. vale Lat. clava, fistis rudda ChSl.  dritkolt It. mazza Dan. ikfélle SCr.  buzdovan Fr. massue Sw. klubba Boh. _ palice, obuSek Sp. porra OE sdagol, cycgel Pol. patka Rum. mdciucé ME _clubbe (kuggel) Russ. bulava, dubyna ir. lorg NE club (cudgel) Skt. vadha-, vadhar, gada- Nir. —_ lorg, lorgaid Du. knots Ay. vazra-, vadar, gasa- W. wb OHG = kalbo Br. bataraz MHG kolbe, kiule NHG keule
34676:Ay. vazra~ (Barth. 1392) = Skt. vajra- “Indra’s thunderbolt’ : Skt. vdja- ‘strength’, OPers. vazarka- ‘great’, etc. Walde-P. 1.246 f.
6963:Lat. excildre (a, pass. b), ON vekja (a), vakna (b), Lett. muodinat (a), muo- expergisct (b) vaka (b) dit (a), muost (b) It. destare (a, refl. b), Dan.  vekke (a), vaagne (b), ChSl. buditi (a), biidéli (b) svegliare (a, refi. b) vaage (b) SCr.  probuditi (a, refl. b) Fr. (r)éveiller (a, refi. b) Sw. vicka (a), vakna (b), Boh.  probuditi (a, refi. b), Sp. despertar (a,b, refi. b) vaka (b) bditz (b) Rum. destepta (a, refi. b) OE weccan (a), onwac- Pol. obudzié (a, refl. b), Ir. do-fitiscim (a, b) nan (b), wacian (b) czuwaé (b) Nir. _dilisighim (a, b), ME wecche (a), wake (a,b) Russ. (raz)budit’ (a, refl. b), miisclaim (a, b) NE wake (a, b) prosnut'sja (b) W. dihuno (a, b), deffroi Du. (op)wekken (a), Skt.  budh- (b, caus. a), (ont-)waken (b) jagr- (b, caus. a) Br. dihuna (a, b) OHG (ar)wecchan (a), wa- Ay. gar- (b, caus. 2) chén MHG (er)wecken (a), (er)wachen (b) NHG (er)wecken (a),
6983:It. svegliare, Fr. éveiller (more com- monly deriv. réveiller), VLat. *exvigilare, epd. of Lat. vigildre ‘stay awake, keep watch’ (> Fr. veiller, etc.), deriv. of vigil ‘awake, lively’ : vigére ‘be lively, vigorous’, etc. (cf. the Gmc. group, be- low, 6). REW 3114. Ernout-M. 1064 f.
6993:come awake’. In ME the forms of the strong OE (wecnan), woc, wocon coa- lesced with the weak OE wacian and ME (a)wake, (a)wakene are used indiscrimi- nately for ‘be awake, become awake’, and also with causative sense supersed- ing ME (a)wecche, OE weccan. Hence NE wake, awake, waken, awaken trans. and intr., but in common use wake ‘be- come awake’, awake only adj., whence be awake for the state. Cf. NED s.vv. wake, vb. and waken, vb.
10290:chsl. vigil (0d), jehla, Pol. | grain, sting’, Av. sikd- ‘needle’, with t scr. Russ. 4 la, fabs Berne- | Skt. s for ¢, perh. influenced by the init. yss. ayoun”s ie of siv-, syu- ‘sew’ (6.35). Barth. 1582. Brickner 189, i Wackernagel-Debrunner, KZ 67.174 f. 6.37 AWL 5 Lith. yla reas tae alr Lett. ilens oupht Dan. syl ChSl Silo sibula Sw. syl SCr. Silo Iesina OE al Boh. dlo aléne ME al, aule Pol. szydto Tesna NE awl Russ. Silo Colle Du. els, priem ray ara- sa i OHG dla, alansa, siula Vv. gana athe) MHG dle, pfriem(e) hd NHG _ahle, pfriem
12180:Most of the words are derived from those for ‘light’ or ‘shine’, with speciali- zation to ‘candle’. Some are from other Sources, as ‘vigil, watch’, name of a
```


## [2026-10-16T05:20:01.736Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/530.* 2>/dev/null; python3 -c \"\nfrom PIL import Image; im=Image.open('site/pages/530.jpg'); print(im.size)\""
}
```


### [2026-10-16T05:20:02.137Z] TOOL RESULT

```
Exit code 1
Permissions Size User   Date Modified Name
.rw-r--r--   55k sfmqrb 14 Oct 22:15  site/pages/530.jpg
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('site/pages/530.jpg'); print(im.size)
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-16T05:20:05.359Z] TOOL CALL #74: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/530.jpg"
}
```


### [2026-10-16T05:20:05.411Z] TOOL RESULT

```

```


## [2026-10-16T05:23:06.936Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-530.py <<'EOF'\nimport json\nW = {\n 'pie': \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weǵ-\",\n 'bozorg': \"https://en.wiktionary.org/wiki/بزرگ\",\n 'gorz': \"https://en.wiktionary.org/wiki/گرز\",\n 'baxtan': \"https://en.wiktionary.org/wiki/باختن\",\n 'vaja': \"https://en.wiktionary.org/wiki/वाज\",\n 'op': \"https://en.wiktionary.org/wiki/𐎺𐏀𐎼𐎣\",\n 'velox': \"https://en.wiktionary.org/wiki/velox\",\n 'vigeo': \"https://en.wiktionary.org/wiki/vigeo\",\n 'wait': \"https://en.wiktionary.org/wiki/wait\",\n 'watch': \"https://en.wiktionary.org/wiki/watch\",\n 'vegetable': \"https://en.wiktionary.org/wiki/vegetable\",\n 'ab_bozorg': \"https://abadis.ir/fatofa/بزرگ/\",\n 'ab_gorz': \"https://abadis.ir/fatofa/گرز/\",\n 'ab_baxtan': \"https://abadis.ir/fatofa/باختن/\",\n 'ab_bazidan': \"https://abadis.ir/fatofa/بازیدن/\",\n}\nPOK = {\"ref\": \"POK:1117\", \"status\": \"supports\", \"note\": \"POK_full.txt line ~89047 ff. 'Root / lemma: ueg- Meaning: fresh, strong; Grammatical information: stative verb uegē-; Material: Old Indic vāja- m. \\\"power, quickness, contest, price of the battle\\\" ... vajra- m. \\\"thunderbolt, club\\\" = Avestan vazra- \\\"club, mace\\\". Old pers. vazrka-, npers. buzurg \\\"big, large\\\", derivative from *uazar n.; Latin vegeō, -ēre ... vigil ... Gothic gawaknan ... uswakjan ... Old English wacian ... OHG wahta' (Page(s): 1117-1118).\"}\nAHD_C = {\"src\": \"AHD\", \"where\": \"Watkins 1985, weg-2 (AHD_watkins1985.txt line 1132)\", \"stance\": \"supports\", \"note\": \"'weg-2. To be strong, be lively. 1. ... Germanic *wakēn ... WAKE ... 3. Germanic *wakjan ... WATCH ... 5. Germanic *waht- in Old North French waitier, to watch: WAIT ... 6. ... *wog-eyo- in Latin vegēre, to be lively: VEGETABLE. 7. ... Latin vigēre ... VIGOR. 8. ... Latin vigil ... VIGILANT ... 9. Suffixed form *weg-slo- in Latin vēlōx, fast, \\\"lively\\\": VELOCITY. [Pok. weg- 1117.]'\"}\nWLD_C = {\"src\": \"WLD\", \"where\": \"Bd. I pp. 246-247 s.v. ueg- (WLD_Bd1_pages.txt line ~22993-23040)\", \"stance\": \"supports\", \"note\": \"'ueg- \\\"frisch, rege, kräftig sein\\\". Lat. vegeō ... vigeō ... vigil ... Ai. vāja-h \\\"Kraft, Schnelligkeit, Wettkampf\\\" ... vajra-h \\\"Donnerkeil (des Indra)\\\" = av. vazra- \\\"Keule\\\" ... ap. vazarka- \\\"groß\\\" (nach Bartholomae Altiran. Wb. 1390 aus iran. *uazrka-, Ableitung von *uazar n.)' and 'ahd. wachar \\\"regsam, frisch, wacker\\\" (formell = ai. vajra-, av. vazra-)'.\"}\nIEC_buz = {\"src\": \"IEC\", \"where\": \"Mann p. 1485 s.v. uāĝ-, uāĝəros (IEC.txt line 19650)\", \"stance\": \"supports\", \"note\": \"'lively, dashing ... Skt. vājah, m. \\\"speed, vigour\\\"; vájrah, m. \\\"thunderbolt\\\"; OPer. cf. vazraka-, adj. \\\"great\\\"; Per. buzurg, id.; ... OE wacor \\\"vigilant\\\"'.\"}\nIEC_baz = {\"src\": \"IEC\", \"where\": \"Mann p. 1499 s.v. ueĝō (2) 'rouse, make move' (IEC.txt line 19825)\", \"stance\": \"supports\", \"note\": \"'Skt. vajāmi ... vājah, m. \\\"speed, vigour, gain\\\"; Av. vaz-, v. \\\"reinforce\\\" ...; Per. bāzīdan, inf. \\\"play\\\"; ... Lat. vegeo, ēre, v. \\\"thrive, stir\\\"'.\"}\nSYN_big = {\"src\": \"SYN\", \"where\": \"Buck §12.55 'large' (SYN.txt line 22466)\", \"stance\": \"supports\", \"note\": \"'OPers. vazarka- (\\\"great\\\" king and \\\"great\\\" = \\\"large\\\" earth) : Skt. vāja- \\\"speed, vigor, contest\\\", vajra- \\\"thunderbolt\\\", Av. vazra- \\\"club\\\", Lat. vegēre \\\"set in motion\\\"'.\"}\nSYN_club = {\"src\": \"SYN\", \"where\": \"Buck §20.22 'club' (SYN.txt lines 1814, 34676)\", \"stance\": \"supports\", \"note\": \"'Av. vazra- (Barth. 1392) = Skt. vajra- \\\"Indra's thunderbolt\\\" : Skt. vāja- \\\"strength\\\", OPers. vazarka- \\\"great\\\", etc. Walde-P. 1.246 f.'; '§1.?: Skt. vajra- ... Av. vazra- \\\"club\\\", NPers. gurz \\\"club\\\"'.\"}\nARY_C = {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 128], entry بزرگ (Latin index ARY_latin_index_pages.txt line 3648-3666)\", \"stance\": \"supports\", \"note\": \"Aryanpur files بزرگ under the same IE root with: Avestan VAZRA, Old Persian VAZRAKA/VAZARKA, Pahlavi WUZURG, BAZURG, Sanskrit VAJA, VAJRA, Latin VEGERE, OE WACAN/WECCAN, English WAKE, Gothic WAKAN; references Pokorny, MacKenzie (BIG) 104, Buck 878-880; note: 'معنی این واژه در سانسکریت: نیرو، سرعت ... در زبان‌های ژرمنی: بیدار، بیدار شدن، نظاره کردن'.\"}\n\nnodes = []\ndef N(id, lang, words, verdict, der, der_fa, sources, rc, cons):\n    nodes.append(dict(id=id, lang=lang, words=words, verdict=verdict, derivation=der, derivation_fa=der_fa, sources=sources, ref_check=rc, consulted=cons))\n\nN(1, \"Iranian\", \"vâz, wâz\", \"plausible\",\n \"Nourai's 'vâz, wâz' is not an attested word but a generic label for the Iranian continuation of PIE *weǵ-: the Indo-Iranian o-grade noun *wā́ȷ́as 'strength, vigour' (Skt. vā́ja-) and the ro-stem *wáȷ́ras 'strong, hard' (> Av. vazra-, OP vazṛka-). Proto-Iranian *ȷ́ > z, so the Iranian forms have z where Sanskrit has j. The 'play' verb *wāz- (MP wāz-, NP bāz-) is grouped here as well, following Horn and Mann; Cheung (2007) and Wiktionary keep it apart (see #9/#10). The label holds as an umbrella for vazra-/vazṛka-, but as a single root with the meaning 'power, largeness, being active or rising' it is Nourai's own synthesis.\",\n \"«واز / wāz» در ایرانی گواهی‌شده نیست و برچسبی کلی است که نورایی برای بازماندهٔ ایرانی ریشهٔ *weǵ- ساخته است: نام‌واژهٔ هندوایرانی *wā́ȷ́as «نیرو» (سنسکریت vā́ja-) و صفت *wáȷ́ras «سخت، نیرومند» که به اوستایی vazra- و پارسی باستان vazṛka- رسیده است؛ ج هندوایرانی در ایرانی به z بدل شده است. اینکه «بازیدن» هم زیر همین ریشه بیاید، رأی هرن و مان است، ولی چونگ و ویکی‌واژه آن را جدا می‌دانند. پس این گره به عنوان چتری کلی پذیرفتنی است، ولی ریشه‌ای واحد با معنای «نیرو، بزرگی، برخاستن» ساختهٔ خود نورایی است.\",\n [W['pie'], W['baxtan']],\n [{\"ref\": \"AEF:201\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Persian translation of Horn is not on disk; its content for this entry equals Horn no. 150 (HRN.txt line 1716: 'bāxtan \\\"spielen\\\" ... ai. vergl. vāja-, vājayati'), which links the Persian verb to Skt. vāja- — consistent with Nourai.\"},\n  {\"ref\": \"IEC:1499\", \"status\": \"supports\", \"note\": \"Mann p. 1499 'ueĝō (2) \\\"rouse, make move; move\\\" ... Skt. vājah \\\"speed, vigour, gain\\\"; Av. vaz-, v. \\\"reinforce\\\"; Per. bāzīdan \\\"play\\\"' (IEC.txt line 19825).\"}],\n [IEC_buz, WLD_C,\n  {\"src\": \"CHEUNG\", \"where\": \"p. 433 s.v. *u̯āz 'to play, contend' (CHEUNG.txt line 28005-28030)\", \"stance\": \"partial\", \"note\": \"Cheung sets up a separate Iranian root *u̯āz 'to play, contend' = Skt. vā́ja- 'contest', but: 'the Ir. forms are semantically irreconcilable with the strong, awake root *ueg-. The noun *u̯āza- / Skt. vāja- may be a blend of *u̯an / Skt. van \\\"to win\\\" and *Haz / aj \\\"to drive\\\"'.\"}])\n\nN(2, \"Old Persian\", \"vazraka\", \"confirmed\",\n \"OP vazṛka- (Kent: vazraka-, older reading vazarka-) 'great' is attested in the royal titulary (xšāyaθiya vazṛka 'great king', DB 1.1) and in 'this great earth' (DNa, XPa). It is a -ka- derivative of Proto-Iranian *wazr̥- / *wáȷ́ra- (cf. Skt. vájra-) from PIE *wóǵ-ro- 'strong', root *weǵ-; Wiktionary regards the OP word as a loan from Median *vazr̥ka-, with the original sense 'endowed with power'.\",\n \"صفت پارسی باستان vazṛka- (کنت: vazraka-) «بزرگ» در لقب شاهی «خشایثیه وزرک» (شاه بزرگ) در سنگ‌نبشتهٔ بیستون و در «این زمین بزرگ» آمده است. این واژه با پسوند -ka- از *wazr̥- ایرانی ساخته شده که هم‌ریشهٔ vájra- سنسکریت است و به هندواروپایی آغازین *wóǵ-ro- «نیرومند» از ریشهٔ *weǵ- برمی‌گردد. ویکی‌واژه آن را در پارسی باستان وام‌واژه‌ای از مادی می‌داند. ادعای نورایی درست است.\",\n [W['op'], W['bozorg'], W['pie']],\n [POK],\n [{\"src\": \"KNT\", \"where\": \"Lexicon s.v. vazraka- (KNT_full.txt line 28886)\", \"stance\": \"supports\", \"note\": \"'vazraka- adj. \\\"great\\\": NPers. buzurg; deriv. of ...'\"},\n  {\"src\": \"BRT\", \"where\": \"col. 1390 s.v. vazarka- (BRT.txt line 23211)\", \"stance\": \"supports\", \"note\": \"'p. vazarka- Adj. (fem. -kā-) \\\"groß\\\": xšāyaθiya ahyāyā būmiyā vazarkāyā D. 6.2 ...'\"},\n  WLD_C, IEC_buz, SYN_big])\n\nN(3, \"Pahlavi\", \"vajarg, bazurk\", \"plausible\",\n \"The Middle Persian word is real: Book Pahlavi wc(w)lg, Manichaean wzrg, read wuzurg (MacKenzie) or wazurg/vazurg (Nyberg), 'big, great', the regular outcome of OP vazṛka- (syllabic ṛ > ur/ar, intervocalic -k- > -g). Nourai's forms are older readings: 'vajarg' is Horn's (1893) transcription of the Bundahišn spelling, which Horn himself says should be read vazarg (the Pahlavi letter c here writes z), and 'bazurk' is a Pazand/NP-influenced form with b- (Mo'in also gives 'bazurg'). The descent is correct; the cited forms are not the standard modern readings.\",\n \"واژهٔ فارسی میانه درست است: در پهلوی کتابی wc(w)lg و در مانوی wzrg نوشته شده و مکنزی آن را wuzurg و نیبرگ vazurg می‌خواند، به معنای «بزرگ». این واژه بازماندهٔ قاعده‌مند vazṛka- پارسی باستان است: ṛ هجایی به ur/ar و k میان دو واکه به g بدل شده است. «vajarg» در کتاب نورایی خوانش کهنهٔ هرن (۱۸۹۳) از املای بندهشن است، و خود هرن می‌گوید باید vazarg خواند. «bazurk» هم گونه‌ای با b آغازین است که در حاشیهٔ معین هم به صورت bazurg آمده. پس اشتقاق درست است، ولی صورت‌های آورده‌شده خوانش‌های امروزی نیستند.\",\n [W['bozorg'], W['ab_bozorg']],\n [{\"ref\": \"HRN\", \"status\": \"supports\", \"note\": \"Horn no. 214 (HRN.txt line 2256 ff.): 'buzurg \\\"groß\\\" ... ap. vazarka- \\\"groß\\\"; phlv. vajarg (Bund., zu lesen vazarg), vazurg (Mēn., zu lesen vazurg)'. Nourai's 'vajarg' is copied from Horn.\"}],\n [{\"src\": \"PHD\", \"where\": \"s.v. wuzurg (PHD_mackenzie.txt line 5519)\", \"stance\": \"supports\", \"note\": \"'wuzurg [LBA < Arb'; wc(w)lg | M wzrg, N buzurg] big, great.'\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. vazurg (NYB_vol2_glossary.txt line 4067)\", \"stance\": \"supports\", \"note\": \"'vazurg [LB', Prth RB'; wcwrg, inscr. wclk] great, big ... OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk ...; Paz. guzurg, guzarg; NP buzurg.'\"},\n  ARY_C])\n\nN(4, \"Persian\", \"bozorg\", \"confirmed\",\n \"NP بزرگ bozorg/buzurg 'big, great' < MP wuzurg/wazurg < OP vazṛka- (Wiktionary; MacKenzie). The initial w- of Middle Persian becomes b- in New Persian (Hübschmann §43: OP v- > NP b- before vowels, cf. wād > bād 'wind'), and the first vowel is assimilated to the following u. Root PIE *weǵ- 'to be strong, lively' (Pokorny 1117 explicitly gives 'npers. buzurg').\",\n \"«بزرگ» (بُزُرگ) فارسی نو از فارسی میانهٔ wuzurg / wazurg و آن از پارسی باستان vazṛka- «بزرگ» است. w آغازین فارسی میانه در فارسی نو به b بدل شده (چنان‌که wād به «باد» رسیده) و واکهٔ نخست با u بعدی همگون شده است. پوکورنی (ص ۱۱۱۷) خود «buzurg» فارسی را زیر ریشهٔ هندواروپایی *weǵ- «نیرومند و سرزنده بودن» آورده و هرن، مکنزی، نیبرگ، آریان‌پور و حاشیهٔ معین (پهلوی bazurg) نیز همین را می‌گویند. ادعای نورایی درست است.\",\n [W['bozorg'], W['op'], W['ab_bozorg']],\n [{\"ref\": \"BQT:272\", \"status\": \"not_found\", \"note\": \"BQT vol. 1 OCR (BQT_v1_pages.txt, leaves ~490-497 around printed p. 272) is too garbled to locate the headword بزرگ or its footnote; Mo'in's etymology was read via abadis.ir instead (Farhang-e Mo'in: '[پهلوی: bazurg، مقابلِ کوچک]').\"},\n  POK],\n [{\"src\": \"HRN\", \"where\": \"no. 214, p. 49-50 (HRN.txt line 2256)\", \"stance\": \"supports\", \"note\": \"'buzurg \\\"groß\\\" ... māz. bazarg ... ap. vazarka- \\\"groß\\\"; phlv. vajarg (Bund., zu lesen vazarg), vazurg'.\"},\n  {\"src\": \"HUB\", \"where\": \"§43, p. ~180 (HUB.txt line 5419-5424)\", \"stance\": \"supports\", \"note\": \"'Ap. v (= idg. v) bleibt im Anlaut vor Vokalen als v im Phl. und Paz. und wird im Np. vor a, ā, e, i ... zu b' — the sound law behind w- > b- in buzurg.\"},\n  {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. بزرگ via abadis.ir\", \"stance\": \"supports\", \"note\": \"'(بُ زُ) (ص.) [پهلوی: bazurg، مقابلِ کوچک]'. Local MON OCR files are silent (grep vazurg/wuzurg: no hit).\"},\n  {\"src\": \"PHD\", \"where\": \"s.v. wuzurg (line 5519)\", \"stance\": \"supports\", \"note\": \"'N buzurg'.\"},\n  ARY_C,\n  {\"src\": \"CHEUNG\", \"where\": \"whole file\", \"stance\": \"silent\", \"note\": \"Cheung covers verbs only; no entry for buzurg.\"}])\n\nN(5, \"Sogdian\", \"wz`rk\", \"plausible\",\n \"Buddhist Sogdian wz'rk /wazark/ (Manichaean wzrg) 'big, great' is real (Gharib no. 10575). It is the Sogdian outcome of Proto-Iranian *wazr̥ka-, the same formation as OP vazṛka-, so it is a cognate (sister form) of the Old Persian word, not a descendant of it as the chart's arrow from OP suggests; Gharib's entry gives the OP form as a comparison ('< OP vazarka').\",\n \"سغدی wz'rk (خوانده: wazark، در متن‌های مانوی wzrg) به معنای «بزرگ» در فرهنگ قریب (شمارهٔ ۱۰۵۷۵) آمده است. این واژه بازماندهٔ سغدیِ ایرانی باستان *wazr̥ka- است، یعنی همان ساختی که در پارسی باستان vazṛka- شده. پس سغدی هم‌ریشه (خواهر) واژهٔ پارسی باستان است، نه برگرفته از آن چنان‌که پیکان نمودار نشان می‌دهد. واژه درست است و فقط مسیر اشتقاق باید اصلاح شود.\",\n [W['op']],\n [{\"ref\": \"SOD:429\", \"status\": \"supports\", \"note\": \"Gharib, entry 10575 (SOD.txt line 79631; SOD_pages.txt line 34314 — Nourai's 429 is the printed page): '10575 wz'rk B ... wazark (RB, wzrg) < OP vazarka; pl. -t(t) ... big, great'; and '10587 wzrg M = wz'rk'.\"}],\n [{\"src\": \"SOD\", \"where\": \"no. 10587\", \"stance\": \"supports\", \"note\": \"'10587 wzrg M = wz'rk' — Manichaean spelling of the same word.\"},\n  {\"src\": \"ISS_alt_DKS\", \"where\": \"grep 'wazark|wz'rk'\", \"stance\": \"silent\", \"note\": \"Bailey's Khotanese dictionary has no entry for this Sogdian word.\"},\n  ARY_C])\n\nN(6, \"Avestan\", \"vazra\", \"confirmed\",\n \"Av. vazra- m. 'club, mace' (especially Mithra's weapon, Yt. 10.96, 10.132) = Skt. vájra- 'Indra's thunderbolt', from Proto-Indo-Iranian *wáȷ́ras, PIE *wóǵ-ro- 'strong, hard' (root *weǵ-). Indo-Iranian *ȷ́ became Iranian z. Proto-Uralic *waśara 'hammer' is an early borrowing from Indo-Iranian.\",\n \"اوستایی vazra- «گرز» (به‌ویژه سلاح میترا در مهریشت) هم‌ریشه با سنسکریت vájra- «آذرخشِ ایندرا» است. هر دو از هندوایرانی *wáȷ́ras و هندواروپایی آغازین *wóǵ-ro- «سخت، نیرومند» از ریشهٔ *weǵ- آمده‌اند و ج هندوایرانی در ایرانی به z بدل شده است. بارتولومه (ستون ۱۳۹۲) و پوکورنی (ص ۱۱۱۷) همین را می‌گویند. ادعای نورایی درست است.\",\n [W['gorz'], W['pie']],\n [POK],\n [{\"src\": \"BRT\", \"where\": \"col. 1392 s.v. vazra- (BRT.txt line 23256)\", \"stance\": \"supports\", \"note\": \"'vazra- m. \\\"Keule\\\"; insbes. Haukeule ... Mithras Hauptwaffe ... ai. vájra- m.; np. gurz' (with note 'Wie der vájra- des Indra').\"},\n  WLD_C, SYN_club])\n\nN(7, \"Pahlavi\", \"vazr\", \"confirmed\",\n \"Book Pahlavi wzl = wazr 'mace' directly continues Av. vazra- (loss of the final -a). MacKenzie gives it as the older/learned spelling of 3warz [wlz] 'club, mace', the metathesised form from which NP gurz comes; Nyberg: 'vazr [wzl] mace — Av. vazra-; Paz. vazr(a); NP gurz; also, with metathesis, varz'.\",\n \"پهلوی wazr (نوشته: wzl) به معنای «گرز» دنبالهٔ مستقیم اوستایی vazra- است که واکهٔ پایانی‌اش افتاده. مکنزی آن را صورت کهن‌تر یا ادبیِ warz «گرز» می‌داند که با قلب (جابه‌جایی z و r) ساخته شده و «گرز» فارسی از همین warz آمده است. نیبرگ نیز می‌نویسد: vazr «گرز»، از اوستایی vazra-، فارسی نو gurz. ادعای نورایی درست است.\",\n [W['gorz']],\n [{\"ref\": \"HRN:202\", \"status\": \"supports\", \"note\": \"Horn no. 906 (HRN.txt line 7861; p. 202): 'gurz, gurze \\\"Keule\\\", arab. LW. jurz, aw. vazra- \\\"Keule\\\"; phlv. vazr, arm. LW. varz; ai. vájra- \\\"Donnerkeil (Indra's)\\\"'.\"}],\n [{\"src\": \"PHD\", \"where\": \"s.v. warz, wazr (PHD_mackenzie.txt lines 5219, 5306)\", \"stance\": \"supports\", \"note\": \"'3warz [wlz | N gurz] club, mace.'; 'wazr [wzl] = 3warz.'\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. vazr (NYB_vol2_glossary.txt line 4066)\", \"stance\": \"supports\", \"note\": \"'vazr [wzl] mace 85 — Av. (1392) vazra-; Paz. vazr(a); NP gurz; also, with metathesis, varz (q.v.).'\"}])\n\nN(8, \"Persian\", \"gorz\", \"confirmed\",\n \"NP گرز gorz/gurz 'mace, club' < MP warz (metathesis of earlier wazr) < Av. vazra- (Wiktionary; MacKenzie). The New Persian gu- reflects MP w- before u (*wurz > gurz), the regular development Hübschmann describes (v before u > g, as in gurg 'wolf' < wurg). Arabic جرز jurz and Armenian varz are loans from Persian/Middle Persian.\",\n \"«گرز» فارسی از فارسی میانهٔ warz است که خود با قلب از wazr کهن‌تر ساخته شده، و آن از اوستایی vazra- است. w پیش از u در فارسی نو به گ بدل شده (*wurz > گرز)، همان دگرگونی آوایی که در «گرگ» از wurg دیده می‌شود. «جُرز» عربی معرّب همین واژه است و ارمنی varz نیز از پهلوی گرفته شده. معین در حاشیهٔ برهان قاطع (ص ۱۷۹۳) همین را آورده است. ادعای نورایی درست است.\",\n [W['gorz'], W['ab_gorz']],\n [{\"ref\": \"BQT:1793\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:1793 (vol. 3 pdf page 590), headword گرز 'عمود آهنین' with Mo'in's footnote 1: 'پهلوی vazr، اوستا vazra «بارتولمه ۱۳۹۲». معرب جرز. ارمنی varz، هندی باستان vajra (گرز رعد [ایندرا]) ... کردی gurz' (OCR rough; same footnote quoted verbatim by Dehkhoda on abadis.ir: 'پهلوی وزر، اوستا وزرا، معرب آن جُرز، ارمنی ورز، هندی باستان وجره ... (از حاشیه برهان قاطع چ معین)').\"}],\n [{\"src\": \"HRN\", \"where\": \"no. 906, p. 202 (HRN.txt line 7861)\", \"stance\": \"supports\", \"note\": \"'gurz ... aw. vazra- \\\"Keule\\\"; phlv. vazr, arm. LW. varz; ai. vájra-'.\"},\n  {\"src\": \"HUB\", \"where\": \"§43 (HUB.txt line 5419-5423)\", \"stance\": \"supports\", \"note\": \"'während anl. v im Paz. und Np. vor u zu g wird (paz. np. gu- aus *vu ...; paz. np. gur- aus *vur)' — explains gurz < *wurz.\"},\n  {\"src\": \"PHD\", \"where\": \"s.v. warz (line 5219)\", \"stance\": \"supports\", \"note\": \"'3warz [wlz | N gurz] club, mace.'\"},\n  {\"src\": \"NYB\", \"where\": \"s.v. vazr (line 4066)\", \"stance\": \"supports\", \"note\": \"'NP gurz; also, with metathesis, varz'.\"},\n  {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. گرز via abadis.ir\", \"stance\": \"supports\", \"note\": \"'(گُ) [په.] (اِ.) عمود آهنین، کوپال' — marks it as Pahlavi.\"},\n  SYN_club,\n  {\"src\": \"ARY\", \"where\": \"Latin index grep GORZ/GURZ\", \"stance\": \"silent\", \"note\": \"Aryanpur has no separate گرز entry; VAZRA appears only within the بزرگ entry (pdf page 128).\"}])\n\nN(9, \"Pahlavi\", \"vâzîtan; bâxtan\", \"disputed\",\n \"MP wāzīdan, wāz- [wʾc-ytn] 'to play' (MacKenzie 2wāzīdan; NP bāzīdan) and wāzīg 'game' are real, e.g. in Mādayān ī čatrang 'to play chess'. The chart's second form, Pahlavi 'bâxtan' 'to rise up', is Horn's reading of a Bundahišn verb (Horn no. 150: 'phlv. baxtan, baxt \\\"er erhob sich\\\"'), which Hübschmann rejected: he reads Pahlavi vāzītan and explains NP bāxtan as an analogical new past stem. The chart's NOTE ('HUB:22 does not accept the bâxtan form') reports this correctly, and modern dictionaries side with Hübschmann: MacKenzie and Nyberg have no Pahlavi bāxtan. On the origin, Nyberg takes wāzītan as the causative of vazītan 'to travel, ride' (Av. vaz- < PIE *weǵʰ- 'carry'), while Cheung posits an Iranian *u̯āz 'to play, contend' = Skt. vā́ja- 'contest' and rejects a link with *weǵ- 'strong, awake' as 'semantically irreconcilable'. Wiktionary follows Cheung. So the attachment of this verb to *weǵ- 'be lively' (Pokorny/Mann/Horn) is no longer the preferred view.\",\n \"فارسی میانهٔ wāzīdan، ستاک wāz- «بازی کردن» (مکنزی) و wāzīg «بازی» واقعی‌اند، مثلاً در «ماتیکان چترنگ» به معنای شطرنج باختن. ولی «باختن» پهلوی به معنای «برخاستن» خوانش هرن از فعلی در بندهشن است که هوبشمان (ص ۲۲) آن را نپذیرفته و آن را vāzītan خوانده است؛ یادداشت نمودار هم همین را می‌گوید و مکنزی و نیبرگ هم «باختن» پهلوی ندارند. دربارهٔ ریشه، نیبرگ wāzītan را سببیِ vazītan «رفتن، سوار شدن» از ریشهٔ *weǵʰ- «بردن» می‌داند و چونگ ریشهٔ جداگانهٔ ایرانی *wāz- «بازی کردن، هماوردی کردن» (هم‌ریشه با vā́ja- سنسکریت) را پیشنهاد می‌کند و پیوند آن را با *weǵ- «بیدار و نیرومند بودن» از نظر معنایی ناسازگار می‌داند. پس پژوهش امروزی وابستگی این فعل به ریشهٔ Weg 2 را نمی‌پذیرد.\",\n [W['baxtan']],\n [{\"ref\": \"HUB:22\", \"status\": \"supports\", \"note\": \"HUB.txt line 673-683 (printed p. 22, no. 150): 'Wenn bal. gvāzī \\\"Spiel\\\" ... zuverlässig ist, so muss vāz (mit z aus ĝ) als iranische Wurzel angesetzt und np. bāxtan (statt *bāstan) als Analogiebildung nach afrāzam : afrāxtan etc. aufgefasst werden. Dann wäre im Phl. vāzītan (nicht vajītan oder vacītan) zu lesen ... Horn's Bemerkungen sind falsch.' — supports vāzītan and the chart's NOTE (Pahlavi bāxtan rejected).\"},\n  {\"ref\": \"AEF:201\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Persian Horn not on disk; equivalent Horn no. 150 (HRN.txt line 1716-1724) has 'phlv. baxtan, baxt \\\"er erhob sich\\\" (kräftig, schnell), Bund. 8,2' — the source of Nourai's 'to rise up'.\"}],\n [{\"src\": \"PHD\", \"where\": \"s.v. 2wāzīdan, wāzīg (PHD_mackenzie.txt lines 5303-5304)\", \"stance\": \"partial\", \"note\": \"'2wāzīdan, wāz- [wʾc-ytn | N bāzīdan] play.'; 'wāzīg [wʾcyk | N bāzī] game, play.' — confirms the MP word; no Pahlavi bāxtan; no etymology.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. vāzītan (NYB_vol2_glossary.txt line 4065)\", \"stance\": \"contradicts\", \"note\": \"'vāzītan [wʾcytn'] caus. of the preceding v. [vazītan \\\"to travel, to ride\\\" — Av. vaz-], to move: 1. trans. čatrang ~ to play at chess ... NP bāzīdan, bāxtan \\\"to play; to fly\\\"' — derives the verb from *waz- 'move' (PIE *weǵʰ-), not *weǵ-.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"p. 433 s.v. *u̯āz (CHEUNG.txt line 28005-28030)\", \"stance\": \"contradicts\", \"note\": \"'*u̯āz \\\"to play, contend; [pass.?] to lose (in games)\\\" — MIDDLE PERSIAN: BMP wʾc- /wāz-/ \\\"to play\\\" ... The generally assumed connection between Skt. vāja- and vājayati \\\"incites\\\" (Lat. vegēre ...) can now be doubted ... the Ir. forms are semantically irreconcilable with the strong, awake root *ueg-'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 150 (HRN.txt line 1716)\", \"stance\": \"supports\", \"note\": \"'bāxtan \\\"spielen\\\" ... ai. vergl. vāja-, vājayati ...; phlv. baxtan, baxt \\\"er erhob sich\\\"' — Horn's view, which Nourai follows.\"}])\n\nN(10, \"Persian\", \"bâzîdan; bâxtan\", \"disputed\",\n \"NP بازیدن bāzīdan 'to play' (present stem bāz-, whence bāzī 'game', bāzande 'player/loser') < MP wāzīdan, wāz- with w- > b- (as in buzurg). باختن bāxtan 'to play; to lose (at a game)' is a secondary past stem built on bāz- by analogy with afrāz-/afrāxtan, sāz-/sāxtan (Hübschmann), the sense 'lose' coming from 'play (and forfeit) a stake'; Manūčehrī's verse uses bāxtan for playing chess. The words and their Persian history are right. The derivation from PIE *weǵ- is disputed: Cheung (2007) and Wiktionary derive them from Proto-Iranian *wāz- 'to play, contend', related to Skt. vā́ja- 'contest' but probably a blend of *wan- 'win' + *Haz- 'drive', and Nyberg from the causative of *waz- 'move' (*weǵʰ-). Only Horn and Mann (IEC 1499) put them under *weǵ-.\",\n \"«بازیدن» (ستاک حال «باز»، و از آن «بازی» و «بازنده») از فارسی میانهٔ wāzīdan / wāz- است و w آغازین، چنان‌که در «بزرگ»، به ب بدل شده. «باختن» به معنای «بازی کردن» و «در بازی از دست دادن» ستاک گذشتهٔ ثانوی است که به قیاس «افراز / افراختن» و «ساز / ساختن» بر «باز» ساخته شده (هوبشمان). معنای «از دست دادن» از «بازی کردن بر سر گرو» آمده و منوچهری «باختن شطرنج» را به معنای بازی کردن به کار برده است. واژه‌ها و تاریخ فارسی‌شان درست است، ولی ریشه‌شناسی هندواروپایی مورد اختلاف است: چونگ و ویکی‌واژه آن را از ایرانی باستان *wāz- «بازی کردن، هماوردی» می‌دانند (هم‌ریشه با vā́ja- سنسکریت، احتمالاً آمیزه‌ای از *wan- «بردن» و *Haz- «راندن»)، و نیبرگ آن را به *waz- «حرکت کردن» (*weǵʰ-) می‌برد. تنها هرن و مان آن را زیر *weǵ- آورده‌اند.\",\n [W['baxtan'], W['ab_baxtan'], W['ab_bazidan']],\n [{\"ref\": \"IEC:1499\", \"status\": \"supports\", \"note\": \"Mann p. 1499 'ueĝō (2) \\\"rouse, make move; move\\\" ... Per. bāzīdan, inf. \\\"play\\\"' (IEC.txt line 19825).\"},\n  {\"ref\": \"HUB:22\", \"status\": \"partial\", \"note\": \"HUB p. 22 no. 150: Iranian root vāz with z < ĝ; 'np. bāxtan (statt *bāstan) als Analogiebildung nach afrāzam : afrāxtan' — supports the Persian forms and the MP link but says nothing about Latin/Germanic cognates.\"},\n  {\"ref\": \"AEF:201\", \"status\": \"not_checked\", \"note\": \"Not on disk; corresponds to Horn no. 150 'bāxtan \\\"spielen\\\", Praes. bāz-em, bāzī (\\\"Spiel\\\") ... ai. vergl. vāja-, vājayati' (HRN.txt line 1716).\"}],\n [{\"src\": \"CHEUNG\", \"where\": \"p. 433 s.v. *u̯āz (CHEUNG.txt line 28008)\", \"stance\": \"contradicts\", \"note\": \"'NP bāzīdan/bāz-, ... NP bāxtan/bāz- ... \\\"to lose (in game)\\\" ... the Ir. forms are semantically irreconcilable with the strong, awake root *ueg-'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 150 (HRN.txt line 1716)\", \"stance\": \"supports\", \"note\": \"'bāxtan \\\"spielen\\\", Praes. bāz-em, bāzī (\\\"Spiel\\\") ... ai. vergl. vāja-, vājayati (spec. von Kampf spielen)'.\"},\n  {\"src\": \"HUB\", \"where\": \"§44 (HUB.txt line 5424)\", \"stance\": \"supports\", \"note\": \"'Ap. v = np. b: bāxtan \\\"spielen\\\", phl. vāzītan (oben p. 22), bal. gvāzī' — w > b sound law.\"},\n  {\"src\": \"NYB\", \"where\": \"s.v. vāzītan (line 4065)\", \"stance\": \"contradicts\", \"note\": \"'caus. of [vazītan \\\"to travel\\\"] ... NP bāzīdan, bāxtan \\\"to play; to fly\\\"' — root *waz- 'move'.\"},\n  {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in / Dehkhoda s.v. باختن, بازیدن via abadis.ir\", \"stance\": \"silent\", \"note\": \"Mo'in: 'باختن ... ۴. [قدیمی] بازی کردن: چوگان باختن'; Dehkhoda s.v. بازیدن: 'بازی کردن. باختن ... (حاشیه برهان قاطع چ معین)' — meanings only, no etymology.\"},\n  {\"src\": \"ARY\", \"where\": \"Latin index grep BAXTAN/BAZIDAN\", \"stance\": \"silent\", \"note\": \"Only hit 'BAXTAN' (ARY_latin_index_pages.txt line 3236) belongs to the بخت/BHAJ entry (Pahlavi baxtan 'to distribute'), not to bāxtan 'play'.\"}])\n\nN(11, \"Sanskrit\", \"vâja\", \"confirmed\",\n \"Skt. vā́ja- m. 'strength, vigour, speed; contest, race; prize, booty' (Rigveda) < Proto-Indo-Iranian *wā́ȷ́as < PIE o-grade *wóǵ-o-s from *weǵ- (Lubotsky; Wiktionary; Pokorny 1117), with the denominative vājayati 'incites, races'. Indo-Iranian *ȷ́ gives Sanskrit j. Nourai's gloss 'to rise up' is loose: the word is a noun meaning 'vigour, contest'. Cheung (2007: 433) doubts the link with *weǵ- because of the Iranian 'play' cognates, but the standard view (Mayrhofer, Lubotsky, Watkins) keeps it.\",\n \"سنسکریت vā́ja- (نام‌واژهٔ مذکر) در ریگ‌ودا به معنای «نیرو، چالاکی، هماوردی، جایزهٔ نبرد» است. این واژه از هندوایرانی *wā́ȷ́as و هندواروپایی آغازین *wóǵ-o-s (بالاگونهٔ o از ریشهٔ *weǵ-) آمده و فعل vājayati «برمی‌انگیزد» از آن ساخته شده است. معنای «برخاستن» که نورایی آورده دقیق نیست. چونگ پیوند آن را با *weg- به سبب هم‌ریشه‌های ایرانیِ «بازی» تردیدآمیز می‌داند، ولی رأی رایج (مایرهوفر، لوبوتسکی، واتکینز، پوکورنی) همین پیوند است. ادعای نورایی درست است.\",\n [W['vaja'], W['pie']],\n [POK],\n [WLD_C, IEC_buz, SYN_big])\n\nN(12, \"Germanic\", \"waken; wakjan; waht\", \"confirmed\",\n \"These are Watkins's Proto-Germanic forms: *wakēn (stative, o-grade *wog-ē-) 'to be awake' > OE wacian, Goth. wakan; *wakjan (causative *wog-eyo-) > OE weccan, wæccan 'to keep watch', Goth. uswakjan 'awaken'; and *waht- / *wahtwō 'watch, guard' > OHG wahta, Frankish *wahtu. Germanic *k and *h(t) regularly reflect PIE *ǵ (Grimm's law: *ǵ > *k; before t, *kt > *ht).\",\n \"این‌ها صورت‌های ژرمنی آغازینِ واتکینز هستند: *wakēn «بیدار بودن» (انگلیسی کهن wacian، گوتی wakan)، *wakjan به معنای سببی «بیدار نگه داشتن، پاییدن» (انگلیسی کهن weccan، گوتی uswakjan) و *waht- / *wahtwō «پاس، نگهبانی» (آلمانی کهن wahta). k ژرمنی بنا به قانون گریم از ǵ هندواروپایی است و kt در ژرمنی به ht بدل شده است. ادعای نورایی درست است.\",\n [W['pie'], W['watch'], W['wait']],\n [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1132, weg-2: '1. ... Germanic *wakēn in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE ... 3. Germanic *wakjan in Old English weccan, to be awake: WATCH. 4. Germanic *wahtwō ... 5. Germanic *waht- in: a. Old North French waitier, to watch: WAIT'.\"}],\n [{\"src\": \"POK\", \"where\": \"p. 1117 (POK_full.txt line ~89068)\", \"stance\": \"supports\", \"note\": \"'Gothic gawaknan \\\"wake up\\\" ... Kaus. Gothic uswakjan \\\"awaken\\\" ... Zustandsverbum Germanic *wakēn: Gothic wakan ... Old English wacian ... Old High German wahta'.\"},\n  WLD_C,\n  {\"src\": \"SYN\", \"where\": \"Buck §4.64? 'wake' (SYN.txt line 6993)\", \"stance\": \"supports\", \"note\": \"'In ME the forms of the strong OE (wæcnan), wōc, wōcon coalesced with the weak OE wacian ... Hence NE wake, awake, waken, awaken'; '(cf. the Gmc. group ...)' linked to Lat. vigil, vigēre.\"}])\n\nN(13, \"English\", \"wake; awake; watch; wait\", \"confirmed\",\n \"wake < ME waken < OE wacian 'be awake' and wæcnan 'arise' (Germanic *wakēn/*waknan); awake < OE āwæcnan/āwacian (prefix ā-); watch < ME wacchen < OE wæccan (Proto-Germanic *wakjaną, with the kk geminate giving -tch); wait < ME waiten 'to watch' < Anglo-Norman/Old North French waitier < Frankish *wahtōn 'to watch, guard' < Proto-Germanic *wahtwō. The sense 'wait' (stay in expectation) developed from 'watch, lie in wait' in Middle English.\",\n \"wake و awake از انگلیسی کهن wacian و āwæcnan «بیدار شدن» هستند. watch از انگلیسی کهن wæccan (ژرمنی *wakjaną) است و kk مضاعف در انگلیسی به -tch بدل شده. wait از انگلیسی میانه waiten «پاییدن» است که از فرانسوی کهن شمالی waitier و آن از فرانکیِ *wahtōn «نگهبانی کردن» گرفته شده و معنای «انتظار کشیدن» بعدها از «در کمین بودن، پاییدن» پدید آمده است. واتکینز، کلاین و ویکی‌واژه همین را می‌گویند. ادعای نورایی درست است.\",\n [W['watch'], W['wait']],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node; AHD weg-2 (see parent) lists WAKE, WATCH, WAIT.\"}],\n [AHD_C,\n  {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. wait (KLN_1971.txt line 264473)\", \"stance\": \"supports\", \"note\": \"'wait, intr. and tr. v. — ME. waiten, \\\"to watch\\\", fr. ONF. waitier, corresponding to OF. guaitier, gaitier ... fr. Frankish *wahtōn, which is rel. to OS., OHG. wahta ... and to OHG wahhēn, wahhōn, OE. wacian, \\\"to be awake\\\". See wake, v., watch'.\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Wake / Watch (SKT.txt lines 21111, 21237)\", \"stance\": \"supports\", \"note\": \"'Watch: see Wake (1)' — Skeat groups watch with wake (OCR of the entry body is garbled).\"}])\n\nN(14, \"Latin\", \"vegĕre, vîgere; vĕlôx\", \"plausible\",\n \"Lat. vegēre 'to arouse, enliven' (causative *wog-eyo-) and vigēre 'to thrive, be vigorous' (stative *weg-ē-, with i from e after v-, de Vaan) are secure reflexes of *weǵ-, as are vigil 'awake' and vegetus 'lively' (Pokorny 1117; de Vaan; Watkins). The book's vowel marks are off (it prints 'vegĕre, vîgere' for vegēre, vigēre and 'vĕlôx' for vēlōx); the JSON copies the page faithfully. vēlōx 'swift' is uncertain: Watkins (AHD) derives it from *weg-slo- under this root, Klein suggests *weg-slo- related to vehere 'carry' (*weǵʰ-), and de Vaan/Wiktionary derive it from *h₂weh₁-lo- 'wind'. Two of the three words are confirmed and vēlōx is only one view, hence 'plausible'.\",\n \"vegēre لاتین «برانگیختن» و vigēre «شاداب و نیرومند بودن»، و نیز vigil «بیدار» و vegetus «سرزنده»، بی‌گمان از ریشهٔ *weǵ- هستند (پوکورنی، دو وان، واتکینز). نشانه‌های واکه‌ها در کتاب نادرست چاپ شده (vegĕre و vîgere به جای vegēre و vigēre، و vĕlôx به جای vēlōx)، ولی استخراج با صفحهٔ چاپی یکی است. دربارهٔ vēlōx «تند، چابک» اختلاف هست: واتکینز آن را از *weg-slo- زیر همین ریشه می‌آورد، کلاین آن را با vehere «بردن» (*weǵʰ-) مرتبط می‌داند و دو وان و ویکی‌واژه آن را از *h₂weh₁-lo- «باد» می‌دانند. پس دو واژهٔ نخست درست‌اند و vēlōx تنها با احتیاط پذیرفتنی است.\",\n [W['vigeo'], W['velox'], W['pie']],\n [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins weg-2 nos. 6-9: 'Latin vegēre, to be lively ... Latin vigēre ... Latin vigil ... Suffixed form *weg-slo- in Latin vēlōx, fast, \\\"lively\\\": VELOCITY. [Pok. weg- 1117.]' (AHD_watkins1985.txt line 1132).\"}],\n [{\"src\": \"POK\", \"where\": \"p. 1117 (POK_full.txt line ~89059)\", \"stance\": \"partial\", \"note\": \"'Latin vegeō, -ēre \\\"am alert, awake\\\" ... vigil \\\"watchful, wakeful\\\" ... vigilāre ... vegetus \\\"strenuous, alert\\\"' — vēlōx not listed under ueg-.\"},\n  WLD_C,\n  {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. velocity (KLN_1971.txt line 259964)\", \"stance\": \"partial\", \"note\": \"'velox, gen. -ōcis, \\\"swift\\\", which is of uncertain origin. It possibly stands for *weg-slo-s and lit. means \\\"moving along quickly, rushing\\\", and is rel. to vehere, \\\"to carry, convey\\\"'.\"},\n  {\"src\": \"LAT\", \"where\": \"grep 'velox|vēlōx|vigeo'\", \"stance\": \"silent\", \"note\": \"Ernout-Meillet OCR: no usable hit for velox.\"}])\n\nN(15, \"English\", \"vegetable; vigor; vigilant; velocity\", \"plausible\",\n \"vegetable < ME/OF vegetable < Late Lat. vegetābilis 'able to live and grow' < vegetāre 'to enliven' < vegetus < vegēre; vigor < OF vigour < Lat. vigor < vigēre; vigilant < (O)F vigilant < Lat. vigilāns, present participle of vigilāre < vigil 'awake'. All three are confirmed reflexes of *weǵ-. velocity < MF vélocité < Lat. vēlōcitās < vēlōx 'swift', whose link to this root is only one of three proposals (Watkins yes; Klein *weǵʰ-; de Vaan *h₂weh₁-lo- 'wind').\",\n \"vegetable از لاتین متأخر vegetābilis «توانا به رشد و زندگی» و آن از vegetāre «جان بخشیدن» و vegēre است. vigor از vigor لاتین (از vigēre) و vigilant از vigilāns لاتین، صفت فاعلی vigilāre «بیدار ماندن» از vigil، هستند. این سه واژه بی‌گمان از ریشهٔ *weǵ- هستند. velocity از vēlōcitās لاتین و آن از vēlōx «تند» است که پیوندش با این ریشه تنها یکی از سه پیشنهاد است (واتکینز: آری؛ کلاین: از *weǵʰ-؛ دو وان: از *h₂weh₁-lo- «باد»). پس سه واژه درست‌اند و velocity با احتیاط پذیرفتنی است.\",\n [W['vegetable'], W['velox']],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node; AHD weg-2 lists VEGETABLE, VIGOR, VIGILANT, VELOCITY.\"}],\n [AHD_C,\n  {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. velocity, vegetable, vigil, vigilant (KLN_1971.txt lines 259964, 259816, 261978, 261991)\", \"stance\": \"partial\", \"note\": \"velocity: 'fr. velox ... of uncertain origin ... possibly *weg-slo-s ... rel. to vehere'; vegetable: 'ME., fr. Late L. vegetābilis'; vigilant: 'ME., either fr. ...' (fr. L. vigilāns) — vegetable/vigor/vigilant consistent, velocity doubted.\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Vigil (SKT.txt line 20883-20896)\", \"stance\": \"supports\", \"note\": \"'Vigour; see Vigil.' — Skeat groups vigour with vigil (Lat. vigil, vigēre).\"}])\n\nentry = {\n \"entry\": 0,\n \"root\": \"Weg 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *weǵ- (Pokorny ueg- 'frisch, kräftig sein' 1117; Watkins weg-2 'to be strong, be lively'; LIV *u̯eǵ-)\",\n \"note\": \"The root box is correct: Pokorny p. 1117 'ueg- Meaning: fresh, strong', Watkins weg-2 'to be strong, be lively', Wiktionary *weǵ- 'to be lively, awake; to be strong'. Pokorny himself lists Skt. vāja-, vajra-, Av. vazra-, OP vazṛka-, NP buzurg, Lat. vegēre/vigil and Gmc. *wakēn/*wakjan, so the backbone of the chart is standard. There are two weak points. (1) The Persian 'play' verbs bāzīdan/bāxtan and MP wāzīdan (#9, #10) are attached to the root following Horn and Mann. Cheung (2007) and Wiktionary derive them from a separate Iranian *wāz- 'to play, contend' (a probable blend of *wan- 'win' and *Haz- 'drive'), and Nyberg derives them from *waz- 'move' (*weǵʰ-), so the attachment is disputed. The Pahlavi 'bâxtan' 'to rise up' is Horn's reading, rejected by Hübschmann; the chart's own NOTE says so, and modern scholarship sides with Hübschmann. (2) Lat. vēlōx/velocity rests on Watkins alone; de Vaan prefers *h₂weh₁-lo- 'wind' and Klein *weǵʰ-. Minor points: the Pahlavi forms vajarg/bazurk are Horn-era readings of wuzurg/wazurg; Sogdian wz'rk is a cognate of OP vazṛka-, not a descendant; and the book's Latin vowel marks (vegĕre, vîgere, vĕlôx) are wrong for vegēre, vigēre, vēlōx. The JSON matches the printed page (checked against site/pages/530.jpg). No extraction errors.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *weǵ- «سرزنده، بیدار و نیرومند بودن» (پوکورنی ص ۱۱۱۷: ueg- «تازه، نیرومند»؛ واتکینز weg-2) درست آمده است. خود پوکورنی vāja- و vajra- سنسکریت، vazra- اوستایی، vazṛka- پارسی باستان، «بزرگ» فارسی، vegēre و vigil لاتین و wake ژرمنی را زیر آن آورده، پس شاخه‌های اصلی نمودار («بزرگ»، «گرز»، wake، watch، vigor) درست‌اند. دو ایراد هست. نخست اینکه «بازیدن / باختن» و wāzīdan پهلوی را نورایی به پیروی از هرن و مان زیر این ریشه آورده، ولی چونگ و ویکی‌واژه آن‌ها را از ریشهٔ جداگانهٔ ایرانی *wāz- «بازی کردن» و نیبرگ از *waz- «حرکت کردن» می‌دانند. «باختن» پهلوی به معنای «برخاستن» نیز خوانش هرن است که هوبشمان آن را رد کرده است. دوم اینکه پیوند vēlōx لاتین (velocity) با این ریشه تنها رأی واتکینز است. «vajarg» پهلوی خوانش کهنهٔ wuzurg است و نشانه‌های واکه در واژه‌های لاتین در خود کتاب نادرست چاپ شده. خطای استخراج دیده نشد.\",\n \"sources\": [W['pie'], W['vaja'], W['op']],\n \"ref_check\": [POK],\n \"consulted\": [WLD_C, AHD_C,\n   {\"src\": \"IEC\", \"where\": \"Mann pp. 1485, 1499 (IEC.txt lines 19650, 19825)\", \"stance\": \"supports\", \"note\": \"'uāĝ-, uāĝəros \\\"lively, dashing\\\" ... Skt. vājah ... vájrah ... OPer. vazraka-; Per. buzurg' and 'ueĝō (2) \\\"rouse, make move\\\" ... Per. bāzīdan ... Lat. vegeo'.\"},\n   SYN_big, ARY_C],\n \"nodes\": nodes,\n}\nout = {\"pdf_page\": 530, \"book_page\": 500, \"verified_by\": \"claude-opus-5-5\", \"verified_on\": \"2026-10-16\", \"entries\": [entry]}\njson.dump(out, open('/home/sfmqrb/git/rishe-private/data/verification/page-530.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-530.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-530.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 530"
}
```


### [2026-10-16T05:23:07.622Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'plausible': 5, 'confirmed': 8, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'not_checked': 5, 'supports': 13, 'not_found': 1, 'partial': 1}
books consulted: {'supports': 43, 'partial': 5, 'silent': 6, 'contradicts': 4} | by book: {'WLD': 6, 'SYN': 5, 'PHD': 5, 'NYB': 5, 'ARY': 5, 'CHEUNG': 4, 'HRN': 4, 'IEC': 3, 'HUB': 3, 'MON': 3, 'KLN': 3, 'BRT': 2, 'POK': 2, 'AHD': 2, 'SKT': 2, 'KNT': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'LAT': 1}
```


## [2026-10-16T05:23:11.715Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; sed -i \"s/Buck §4.64? 'wake'/Buck, 'wake' section/; s/'§1.?: Skt. vajra-/(line 1814): 'Skt. vajra-/\" build-530.py && python3 build-530.py && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 530 | grep -c PROBLEM; grep -c '§1\\.?\\|4.64?' /home/sfmqrb/git/rishe-private/data/verification/page-530.json"
}
```


### [2026-10-16T05:23:12.555Z] TOOL RESULT

```
0
0
```


## [2026-10-16T05:23:21.647Z] TOOL CALL #77: SubagentHandback

```json
{
 "message": "I verified page 530 (book page 500, root Weg 2) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-530.json. The file is valid JSON, and `verify_check.py 530` reports 0 PROBLEM lines.\n\n- **Root:** PIE *weǵ- 'to be strong, lively' is confirmed. Pokorny p. 1117, Walde-Pokorny I 246 f., Watkins (AHD) weg-2 and Mann all list it.\n- **Nodes (15):** 8 confirmed, 5 plausible, 2 disputed, 0 transcription_suspect.\n- **Disputed:**\n  - #9, Pahlavi vâzîtan; bâxtan: MP wāzīdan 'to play' is a real word. The Pahlavi 'bâxtan' meaning 'to rise up' is Horn's reading, which Hübschmann (p. 22) rejected; the chart's own NOTE says this, and MacKenzie and Nyberg agree with Hübschmann. Cheung and Wiktionary derive the verb from a separate Iranian root *wāz- 'to play, contend', and Nyberg from *waz- 'to move' (*weǵʰ-). Neither puts it under *weǵ-.\n  - #10, Persian bâzîdan; bâxtan: the same origin problem. Only Horn and Mann (IEC:1499) put these under *weǵ-.\n- **Plausible, in brief:**\n  - The Iranian umbrella root 'vâz' is Nourai's own label, not an attested word.\n  - Pahlavi 'vajarg, bazurk' are old readings of the word MacKenzie reads wuzurg.\n  - Sogdian wz'rk is a sister form of Old Persian vazṛka-, not derived from it as the arrow shows.\n  - Latin vēlōx and English velocity: only Watkins puts them under this root. De Vaan derives vēlōx from *h₂weh₁-lo- 'wind', and Klein links it to *weǵʰ- 'carry'.\n- **Book misprint, not an extraction error:** the Latin vowel marks are wrong in the printed book ('vegĕre, vîgere, vĕlôx' for vegēre, vigēre, vēlōx). The JSON matches the page image.\n- **Extraction errors:** none.\n- **Reference gaps:**\n  - BQT:272 (bozorg) could not be found in the garbled vol. 1 OCR, so I took Mo'in's etymology from abadis.ir instead.\n  - AEF:201 is not on disk; Horn no. 150 stands in for it.\n  - Etymonline blocked fetching (403), so I used Wiktionary pages instead. All web sources were archived with fetch_source.py."
}
```


### [2026-10-16T05:23:21.916Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
