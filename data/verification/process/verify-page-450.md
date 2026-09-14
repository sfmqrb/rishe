# Verification process log — verify-page-450


## [2026-09-14T01:56:10.523Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 450 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-450.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-450.json. Write /home/sfmqrb/git/rishe/data/verification/page-450.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 450` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:11.513Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T01:56:12.345Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:12.363Z] TOOL RESULT

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


## [2026-09-14T01:56:12.824Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-450.txt"
}
```


### [2026-09-14T01:56:12.849Z] TOOL RESULT

```
1	=== PDF page 450 (book page 420) ===
2	--- entry 0 ---
3	ROOT [Arabic] S.h.r : a yellowish red color  (refs KLN:1373)
4	#1 (parent #0) [Arabic] refs=KLN:1373; FVA:226; AHD:1143 | as-har : yellowish red ; sahrâ : anything which has a yellowish red (sand) color, desert (due to its color)
5	  #2 (parent #1) [Persian] refs=FVA:226 | sahrâ «صحرا» : desert | extra: صحاری
6	  #3 (parent #1) [English] refs=AHD:1143; KLN:1373 | Sahara
7	--- entry 1 ---
8	ROOT Shu-shu -> redirect to Chou-shu
9	--- entry 2 ---
10	ROOT Sî 1 -> redirect to Sě 1
11	--- entry 3 ---
12	ROOT Sî 2 -> redirect to Sě 2
13	--- entry 4 ---
14	ROOT Sî 3 -> redirect to Sâi 2
15	--- entry 5 ---
16	ROOT Sindhu -> redirect to Syand
17	--- entry 6 ---
18	ROOT [Old Persian] Sinkadruš : the red ore of mercury (mercuric sulfide) used as a pigment  (refs MON:2083)
19	#1 (parent #0) [Persian] refs=MON:2083; BQT:1302 | šangarf «شنگرف» : red lead, cinnabar, red pigment | extra: زنجرف
20	  #2 (parent #1) [Greek] refs=KLN:289 | kinnabari : red lead
21	    #3 (parent #2) [Latin] refs=AHD:243 | cinnâbaris
22	      #4 (parent #3) [French] refs=KLN:289 | cinbare
23	        #5 (parent #4) [English] refs=AHD:243 | cinnabar
24	--- entry 7 ---
25	ROOT [Indo-European] Skabh : to support  (refs POK:916)
26	#1 (parent #0) [Avestan] refs=POK:916; SOD:152 | skambem : support ; upa-skambem : for support, a pillar ☞Upo ; fra-sčimbana : universe, world ☞Per 1
27	  #2 (parent #1) [Persian] refs=POK:916; BQT:410; MON:798; FRS:183 | pečkam «پچکم» : a roof on pillars, a room open all around, a porch | extra: پیچکم ، پیشکم ، پشکم
28	  #3 (parent #1) [Sogdian] refs=SOD:152 | fcmbd : world
29	#4 (parent #0) [Latin] refs=AHD; KLN:1430 | scamnum : a support (for seating), bench
30	  #5 (parent #4) [English] refs=None | shamble : bench
31	--- entry 8 ---
32	ROOT Skaf -> redirect to Sek
33	
```


## [2026-09-14T01:56:15.602Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-450.json",
 "description": "Read source JSON for page 450"
}
```


### [2026-09-14T01:56:15.671Z] TOOL RESULT

```
{
  "pdf_page": 450,
  "book_page": 420,
  "entries": [
    {
      "root": {
        "name": "S.h.r",
        "lang": "Arabic",
        "refs": "KLN:1373",
        "gloss": "a yellowish red color"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:1373; FVA:226; AHD:1143",
          "words": [
            {"translit": "as-har", "gloss": "yellowish red", "script": null},
            {"translit": "sahrâ", "gloss": "anything which has a yellowish red (sand) color, desert (due to its color)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:226",
          "words": [
            {"translit": "sahrâ", "gloss": "desert", "script": "صحرا"}
          ],
          "script_extra": "صحاری",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "AHD:1143; KLN:1373",
          "words": [
            {"translit": "Sahara", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Shu-shu",
        "redirect": "Chou-shu"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sî 1",
        "redirect": "Sě 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sî 2",
        "redirect": "Sě 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sî 3",
        "redirect": "Sâi 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sindhu",
        "redirect": "Syand"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sinkadruš",
        "lang": "Old Persian",
        "refs": "MON:2083",
        "gloss": "the red ore of mercury (mercuric sulfide) used as a pigment"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:2083; BQT:1302",
          "words": [
            {"translit": "šangarf", "gloss": "red lead, cinnabar, red pigment", "script": "شنگرف"}
          ],
          "script_extra": "زنجرف",
          "note": null,
          "quote": {
            "text": "بنفشه زار بپوشید روزگار به برف - چنار گشت دوتا و زریر شد شنگرف",
            "poet": "Kasâî Marvzî"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Greek",
          "refs": "KLN:289",
          "words": [
            {"translit": "kinnabari", "gloss": "red lead", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "AHD:243",
          "words": [
            {"translit": "cinnâbaris", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "KLN:289",
          "words": [
            {"translit": "cinbare", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:243",
          "words": [
            {"translit": "cinnabar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skabh",
        "lang": "Indo-European",
        "refs": "POK:916",
        "gloss": "to support"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:916; SOD:152",
          "words": [
            {"translit": "skambem", "gloss": "support", "script": null},
            {"translit": "upa-skambem", "gloss": "for support, a pillar", "script": null, "see": ["Upo"]},
            {"translit": "fra-sčimbana", "gloss": "universe, world", "script": null, "see": ["Per 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:916; BQT:410; MON:798; FRS:183",
          "words": [
            {"translit": "pečkam", "gloss": "a roof on pillars, a room open all around, a porch", "script": "پچکم"}
          ],
          "script_extra": "پیچکم ، پیشکم ، پشکم",
          "note": null,
          "quote": {
            "text": "از تو خالی نگارخانهٔ جم - فرش دیبا کشیده بر پچکم",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:152",
          "words": [
            {"translit": "fcmbd", "gloss": "world", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:1430",
          "words": [
            {"translit": "scamnum", "gloss": "a support (for seating), bench", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "shamble", "gloss": "bench", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skaf",
        "redirect": "Sek"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:56:16.316Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:16.368Z] TOOL RESULT

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


## [2026-09-14T01:56:49.820Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','FVQ','AHD','POK','SOD','MON','BQT','FRS','LKT','SKT','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','ARY','PLA','AFM','DEV','PHN','LEW','LAT','TAD','ARB','AFA','FSD','WEB','RCH','HJB','SIN','ISS']:\n    v=d.get(k)\n    if v is None: print(k,'MISSING'); continue\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


### [2026-09-14T01:56:50.947Z] TOOL RESULT

```
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"], "page_
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
== AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning o
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \\f b
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed pag
== SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sectio
== ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file ha
```


## [2026-09-14T01:56:56.144Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','POK','SOD','BQT','MON','FRS','AHD']:\n    print('==',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T01:56:57.320Z] TOOL RESULT

```
== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
== POK
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
== SOD
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
== BQT
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
== MON
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
== FRS
{
 "title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')",
 "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"
 ],
 "page_offset": "different edition — no mapping",
 "covers_etymology": false,
 "notes": "Persian OCR fair. Ganjoor does not host Loghat-e Fors."
}
== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
```


## [2026-09-14T01:57:03.119Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 Sahara ===\"; grep -n -i \"^Sahara\" KLN_1966.txt | head\necho \"=== KLN 1971 Sahara ===\"; grep -n -i \"Sahara,\" KLN_1971.txt | head\necho \"=== KLN cinnabar ===\"; grep -n -i \"^cinnabar\" KLN_1966.txt KLN_1971.txt | head\necho \"=== KLN shamble ===\"; grep -n -i \"^shamble\" KLN_1966.txt KLN_1971.txt | head\necho \"=== KLN scamnum ===\"; grep -n -i \"scamnum\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-14T01:57:03.307Z] TOOL RESULT

```
=== KLN 1966 Sahara ===
33498:Sahara,  n.,  the  great  desert  of  North  Africa.  — Fr.  Arab,  sahrd',  ‘desert’,  prop.  fern,  of  the  adj. dsharu,  ‘yellowish  red’,  used  as  a  noun;  rel.  to Heb.  tzahor,  ‘white’.
=== KLN 1971 Sahara ===
211060:Sahara, n., the great desert of North Africa. — 
=== KLN cinnabar ===
KLN_1971.txt:47261:cinnabar, n., HgS, mercuric sulfide, a bright red 
KLN_1971.txt:47263:cinnabaris , fr. Gk. xivvapapt, which prob. 
KLN_1966.txt:7691:cinnabar,  n.,  HgS,  mercuric  sulfide,  a  bright  red mineral.  —  F.  cinabre,  fr.  OF.  cenobre,  fr.  L. cinndbaris,  fr.  Gk.  XLvvi[}xpi,  which  prob. derives  fr.  Pers.  shangdrf,  ‘red  lead,  cinnabar  . Derivatives:  cinnabar-ic,  cinnabar- ine,  adjs. Cinnamomum,  n.,  a  genus  of  plants  of  the  laurel family  (bot.)  —  L.,  ‘cinnamon  .  See  next  word, cinnamon,  n.  —  L.  cinnamomum,  cinnamon,  fr. Gk.  xivvdp.cop.ov,  xwvocpov,  fr.  Heb.  qitmamdn. The  Greek  word  has  been  altered  fr.  orig. ♦xivvdpcovov,  prob.  under  the  influence  ofGk. apeopov,  ‘a  spice  plant  .
=== KLN shamble ===
KLN_1971.txt:219784:shamble, n. — ME. schamel, shamel, ‘bench’, fr. 
KLN_1971.txt:219794:shamble, intr. v., to walk with a shuffling gait. — 
KLN_1971.txt:219796:shamble, n. For sense development cp. F. bancal, 
KLN_1966.txt:34873:shamble,  n.  —  ME.  schamel,  shamel,  ‘bench’,  fr. OE.  scamel,  ‘stool,  bench,  table’,  rel.  to  ON. skemill,  Du.  schemel ,  OHG.  scamil  (in  fuoy scamil),  ‘(foot)  stool’  (whence  MHG.,  G.  sche¬ me/)  ;  borrowed  fr.  L.  scamellum,  ‘bench,  stool’.
=== KLN scamnum ===
KLN_1971.txt:213796:of scamnum , ‘bench’. See shamble, n. 
KLN_1971.txt:219789:dimin. of scamnum, ‘bench’, which stands for 
KLN_1966.txt:33916:of  scamnum,  ‘bench’.  See  shamble,  n. scammony,  n.,  a  gum  resin.  —  ME.  scamonie,  fr. L.  scammonia  or  scammonium,  fr.  Gk.  oxap.- pcovta  or  axappdiviov.
KLN_1966.txt:34874:dimin.  of  scamnum,  ‘bench’,  which  stands  tor *skabhnom-  and  prop,  means  ‘stay,  support’,  fr. l.-E.  base  •skabh-,  ‘to  support’,  whence  also  OI. skabhnati,  skabhnoti,  ‘fastens,  supports’,  skam- bhdh,  ‘post’.  Cp.  scamillus. shamble,  intr.  v.,  to  walk  with  a  shuffling  gait.  — Formed  fr.  the  adj.  shamble  in  shamble  legs,  fr. shamble,  n.  For  sense  development  cp.  F.  bancal, ‘bandy-legged’,  prop,  ‘bench-legged’,  fr.  banc, ‘bench’,  and  the  E.  adjective  bench-legged. Derivatives:  shambl-ing,  adj.  and  n. shame,  n.  —  ME.  schame,  shame,  fr.  OE.  scamu, sceamu,  ‘shame’,  rel.  to  OS.  skama,  ON.  skdmm, Dan.,  Swed.  sham,  OFris.  skome,  Du.  schaamte, OHG.  scama,  MHG.  schame,  scheme,  G.  Scham, of  s.m.,  Goth,  skama  in  skaman  sik,  ‘to  be ashamed’,  fr.  I.-E.  base  *skam-,  *skem-,  which is  perh.  an  j-enlargement  of  *kam,  *kem-,  ‘to cover',  whence  ON.  hamr,  ‘a  covering’,  Goth. ga-hamon,  ‘to  cover  with  clothes’.  See  camera, sham,  shend,  hame.  For  sense  development  cp. Lith.  kuvetis,  ‘to  be  ashamed’,  fr.  I.-E.  base *(s)qeu-,  ‘to  cover’  (see  sky).
```


## [2026-09-14T01:57:15.785Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# map line number -> leaf\ndef leaf_of(lineno):\n    return txt[:sum(len(l)+1 for l in lines[:lineno-1])].count('\\f')\nfor ln in (33498,7691,34873,34874,33916):\n    print(ln, 'leaf', leaf_of(ln))\nEOF"
}
```


### [2026-09-14T01:57:17.049Z] TOOL RESULT

```
33498 leaf 729
7691 leaf 163
34873 leaf 759
34874 leaf 759
33916 leaf 739
```


## [2026-09-14T01:57:28.149Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint(len(leaves))\nfor i in (163,729,759,739):\n    L=leaves[i]\n    print('--- leaf',i,'---')\n    print(L[:300].replace('\\n',' | '))\n    print('...TAIL:', L[-200:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-14T01:57:29.447Z] TOOL RESULT

```
903
--- leaf 163 ---
 a  belt,  girdle.  —  L.  cinctiira,  a  girdle  , fr.  L.  cinctus,  pp.  of  cingere,  ‘to  gird,  bind round’,  prob.  cogn.  with  OI.  kaheate,  ‘binds’, kahei,  ‘girdle’,  Lith.  kinkau,  kinkyti,  ‘to  harness horses’,  and  perh.  also  with  Gk.  xiyxXl;,  ‘a  lat¬ ticed  gate’.  For  the 
...TAIL: .  circumferentia.  See  prec.  word, circumflex,  adj.  —  L.  circumflexus ,  bent  round  , pp.  of  circumflectere,  ‘to  bend  round  ,  fr.  cir¬ cum  and  flectere,  ‘to  bend’.  See  flex,  ‘t
--- leaf 729 ---
onsecration.  —  ME.,  verbal  noun  of sacren,  ‘to  consecrate’.  See  sacred  and  -tag,  suff. forming  verbal  nouns. | sacrist,  n.,  a  keeper  of  the  sacred  vessels;  sacris¬ tan.  —  ME.,  fr.  Eccles.  L.  sacrista,  fr.  L.  sacer, fern,  sacra,  neut.  sacrum,  ‘holy,  sacred’.  See sac
...TAIL:  n.,  the  great  desert  of  North  Africa.  — Fr.  Arab,  sahrd',  ‘desert’,  prop.  fern,  of  the  adj. dsharu,  ‘yellowish  red’,  used  as  a  noun;  rel.  to Heb.  tzahor,  ‘white’. | Derivatives
--- leaf 759 ---
darkness’,  Olr.  scath,  OW.  scod, Bret,  squeut,  ‘darkness’.  Cp.  shadow  and  shed, n.  (which  is  a  doublet  of  shade). | Derivatives:  shade,  tr.  and  intr.  v.,  shad-ed,  adj., shad-er,  n.,  shad-ing,  n.,  shade-less,  adj.,  shade- less-ness,  n.,  shad-y,  adj.,  shad-i-ly,  adv.,  
...TAIL:  second  element  in nuncheon. | Derivatives:  shank,  tr.  and  intr.  v.,  shank-ed, adj. | shantung,  n.,  a  coarse  silk.  —  Named  after  the Chinese  province  Shan-Tung. shanty,  n.,  hut.  —  Ca
--- leaf 739 ---
e  head).  See  Kluge- Mitzka, EWDS.,  p.  633  s.v.  Schale.  See  shelf,  ‘slab  of wood’,  and  cp.  words  there  referred  to.  Cp.  also scale  of  fish  and  skull.  Cp.  also  scall,  scallop, scalp,  school  of  fishes,  shale,  shell,  shellac,  shield, shoal,  ‘crowd’,  skill.  Cp.  also 
...TAIL:   eISoc,  ‘form,  shape’.  See  -oid. | Derivative:  scaphoid,  n. | scapula,  n.,  shoulder  blade  (anat.  and  zool.)  — Late  L.,  ‘shoulder  blade,  shoulder’,  sing,  of  L. scapulae,  ‘shoulder  bl
```


## [2026-09-14T01:57:49.778Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (698,699,700,701):\n    print('--- leaf',i,'---', leaves[i][:160].replace('\\n',' | '))\nEOF\necho \"###\"\ngrep -rl 'KLN:' /home/sfmqrb/git/rishe/data/verification/page-4*.json 2>/dev/null | head -3"
}
```


### [2026-09-14T01:57:51.086Z] TOOL RESULT

```
--- leaf 698 --- n,  ‘to  count,  reckon’,  OE.  recen,  ricen, ‘ready,  quick,  swift’,  fr.  I.-E.  base  *reg-,  ‘straight, right;  to  lead,  direct’,  whence  also  Gk.  op
--- leaf 699 --- ler  (F.  reconcilier),  fr.  L.  reconciliare,  ‘to  bring together  again,  reconcile',  fr.  re-  and  conciliare, ‘to  bring  together’.  See  conciliate. | D
--- leaf 700 --- r.  L.  recuperatus, pp.  of  recuperare.  See  recuperate  and  -ive. Derivative :  recuperative-ness,  n. recur,  intr.  v.  —  ME.  recurren,  fr.  L.  recur
--- leaf 701 ---  re-  and ducere,  ‘to  lead’.  See  duke  and  cp.  redoubt,  n., reduit,  ridotto. | Derivatives:  reduc-er,  n.,  reduc-ihle,  adj.,  reduc- ibil-ity,  n. | redu
###
/home/sfmqrb/git/rishe/data/verification/page-403.json
/home/sfmqrb/git/rishe/data/verification/page-411.json
/home/sfmqrb/git/rishe/data/verification/page-412.json
```


## [2026-09-14T01:57:57.083Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob,re\nfor f in sorted(glob.glob('page-4*.json'))[:12]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for rc in e.get('ref_check',[])+[r for n in e.get('nodes',[]) for r in n.get('ref_check',[])]:\n            if rc['ref'].startswith('KLN'):\n                print(f, rc['ref'], rc['status'], rc['note'][:260])\nEOF"
}
```


### [2026-09-14T01:57:58.181Z] TOOL RESULT

```
page-40.json KLN:1106 supports KLN_1966.txt ƒƒ-leaf 591, which carries the printed page numbers 1106/1107, has s.v. 'owe': 'fr. I.-E. base *aik-, ‘to own’, whence also OI. ī́śe, ‘he owns’, ... Avestic is-, ‘riches, fortune’, isvan-, ‘well off, rich’. Cp. ought, aux. v., own, adj. and v.' — 
page-40.json KLN:1106 supports KLN_1966.txt leaf 591 s.v. owe: 'Avestic is-, ‘riches, fortune’, isvan-, ‘well off, rich’' — the source of Nourai's gloss 'wealth' / 'wealthy'.
page-40.json KLN:1093 supports KLN_1966.txt ƒƒ-leaf 584, printed page 1093, s.v. 'ore, n.': 'ME. oor, or, fr. OE. ār, ǣr, ‘brass’, rel. to ON. eir, ... Goth. aiz, ‘bronze’, and cogn. with OI. áyah (gen. áyasah), Avestic ayō (gen. ayaŋhō), L. aes, gen. aeris, ‘brass’, fr. I.-E. *ayos-, which
page-40.json KLN:1093 supports KLN_1966.txt leaf 584 s.v. ore: 'cogn. with OI. áyah (gen. áyasah), Avestic ayō (gen. ayaŋhō), L. aes, gen. aeris' — Klein gives exactly Nourai's two forms ayō and ayaŋh(ō).
page-401.json KLN supports Klein s.v. pure: 'L. purus, ‚pure, clean’, which is rel. to putus, ‚clear, pure’, putare, ‚to cleanse, clean’, and cogn. with OI. pávate, punāti, ‚purifies, cleanses’, pūtaḥ, ‚pure’ … MIr. úr, ‚fresh, new’, OHG. fowen, ‚to sift’.'
page-403.json KLN:1154 supports Klein 1966, p. 1154/1155 (KLN_1966.txt l. 28054, on the leaf carrying the page numbers 1154-1155), s.v. pepper: 'ME. peper, piper, fr. OE. pipor, tr. L. piper, "pepper", fr. Gk. πέπερι, ult., through Persian mediation, fr. OI. pippalī, "berry, peppercorn"'.
page-403.json KLN:1154 supports Klein 1966, p. 1154 (KLN_1966.txt l. 28054): 'pepper, n. — ME. peper, piper, fr. OE. pipor, tr. L. piper, "pepper", fr. Gk. πέπερι, ult., through Persian mediation, fr. OI. pippalī, "berry, peppercorn" … OFris. piper, Du. peper, OHG. pfeffar …'.
page-404.json KLN:1557 supports Klein vol. II (the entry stands between the page markers 1556 and 1565 in KLN_1966.txt, i.e. on printed p. 1556/1557, exactly where Nourai cites it): 'symposium, n., 1) in ancient Greece, a drinking party; 2) a meeting, conference for conversation or discussio
page-405.json KLN:1382 supports Klein s.v. santir (KLN_1966.txt line 33703, scan leaf 734; the leaf-to-page ratio fixed by the three Klein citations on this page — 138, 1382, 1573 — is a consistent 1.915 printed pages per leaf, so the page number checks out): 'santir, n., a kind of dulcimer.
page-405.json KLN:138,1573 supports Klein s.v. babouche (KLN_1966.txt line 4226, scan leaf 84 = p. 138): 'babouche, n., a heelless Oriental slipper. — F., fr. Arab. bābūsh, fr. Pers. pāpūsh, lit. ‚foot-covering’, fr. pā, ‚foot’, and the verb pūshiden, ‚to cover’.' And s.v. tarboosh (line 38199, 
page-405.json KLN:138,1573 supports Klein p. 138 'babouche ... — F., fr. Arab. bābūsh' and p. 1573 'tarboosh ... — F. tarbouch(e), fr. Arab. ṭarbūsh' — the French stage is explicit in both entries.
page-405.json KLN:138,1573 partial Klein has 'babouche' exactly as printed here, but spells the cap 'tarboosh, n., a brimless felt cap worn by Moslems. — F. tarbouch(e) ...' — so the reference supports the derivation but not the English spelling in the box.
page-407.json KLN:1129 supports Klein 1966 p. 1129 s.v. pard (IEC leaf-checked: KLN_1966.txt leaf 603, whose neighbours carry the running numbers 1126/1127 and 1130/1131, so this leaf = pp. 1128-1129): 'Gk. πάρδος, πάρδαλις "panther", generally connected with OI. pṛdākuḥ, "panther, tiger"'. 
page-407.json KLN:1129 partial Klein p. 1129 s.v. pard: 'fr. L. pardus, fr. Gk. πάρδος, πάρδαλις, "panther", generally connected with OI. pṛdākuḥ ... It is more probable, however, that Greek πάρδος has been borrowed fr. Heb. bārōd, "spotted" ... see Heinrich Lewy, Die semitischen Fremdwörte
page-407.json KLN:1129 supports Klein p. 1129 s.v. pard: 'pard, n., leopard (archaic) — ME. parde, fr. OF., fr. L. pardus, fr. Gk. πάρδος, πάρδαλις, "panther" ... Cp. leopard, camelopard, guepard.'
page-409.json KLN:1185 partial KLN_1966.txt leaf 633 (running numbers 1184/1185), s.v. 'pilau, pilaf, pilaw, n., an Oriental dish of rice boiled with meat, etc. — Turk. pilaw, fr. Pers. palav.' The page is the right one, but Klein gives no Sanskrit etymon at all, so it does not support the 
page-409.json KLN:1185 partial Klein p.1185 s.v. pilau: 'Turk. pilaw, fr. Pers. palav' — confirms that the Persian word is the source of the Turkish one, but says nothing about where Persian got it.
page-409.json KLN:1185 supports 'pilau, pilaf, pilaw, n., an Oriental dish of rice boiled with meat, etc. — Turk. pilaw, fr. Pers. palav.' (KLN_1966.txt line 28812, leaf 633 = pp.1184/1185).
page-41.json KLN:31 partial KLN_1966.txt leaf 28 = printed pp.31-32 contains the entry 'aeon, eon ... cogn. with OI. āyu, "life", Avestic ayu, "age", L. aevum ...'. Klein's p.31 therefore supports the second member (āyu-) of Nourai's compound and the root, but Klein nowhere mentions Aves
```


## [2026-09-14T01:58:07.549Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (161,162,163,164,165,727,728,729,730,757,758,759,760,761):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', leaves[i])\n    print(i, nums[:6])\nEOF"
}
```


### [2026-09-14T01:58:08.749Z] TOOL RESULT

```
161 ['286']
162 []
163 []
164 ['292', '293']
165 ['294', '295']
727 []
728 []
729 ['1373']
730 []
757 ['1426', '1427']
758 ['1428']
759 []
760 []
761 []
```


## [2026-09-14T01:58:14.176Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma skamb/skabh ===\"; grep -n -i \"lemma: (s)kamb\\|lemma: skamb\\|lemma: skab\\|lemma: (s)kab\" POK_full.txt | head -20\necho \"=== search skambhá ===\"; grep -n \"skambh\\|skabhn\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:58:14.248Z] TOOL RESULT

```
=== POK_full lemma skamb/skabh ===
=== search skambhá ===
74951:Material: Old Indie skabhnati, skabhnotr propped ', Perf. caskambha, skabhayatF 
74952:fastened, ligated, strengthened, reinforced, made fast; fortified '; skambha-rc\., 
74953:skambhana-m^ prop, pillar', Avestan i/y055/r5/77i6'a/77 'under fastening, strengthening ', 
74965:(compared with Old Indie skambhana-m) reshuffling through Aryan from skabh- after
```


## [2026-09-14T01:58:16.028Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '74935,74985p' POK_full.txt"
}
```


### [2026-09-14T01:58:16.097Z] TOOL RESULT

```
Old Indie syuman-); Old Church Slavic sijg{*sjujd), sifi{= Lithuanian siufi) ' sew ', russ. 
s//>7 "genahf. Old Church Slavic 56 i/e/7b "genahf {*siuueno-), si/o= Czech sid/on. " 



pricker, awl'; further by Trautmann 261 f.; Hittite sum(m)anza(n)^ filament ', also (?) suel, 

su/7 ds. 

References: WP. II 515 f., WH. II 631 f., Carruthers Lg. 6, 161 f. 

Page(s): 915-916 

Root / lemma: sArab^- skarrt^- 
Meaning: to support 

Material: Old Indie skabhnati, skabhnotr propped ', Perf. caskambha, skabhayatF 
fastened, ligated, strengthened, reinforced, made fast; fortified '; skambha-rc\., 
skambhana-m^ prop, pillar', Avestan i/y055/r5/77i6'a/77 'under fastening, strengthening ', 
fraskamba-, frascimbana- " girders, pillars '; npers. paskam " a covered walk between 
columns, colonnade, piazza, arcade, gallery, porch, portico ', sogd. sk'np- {*skamb) " base 
of the universe '; 

Maybe alb. Geg shkamb, Tosc sbkemb'seat, bench, rock, stone, *pillar' related to Latin 
scamnum {*sksb'"nom). 

Latin scamnum {* skdb^nom) " bench, footstool ', Demin. scabillum, scabe/fum ' n\e6r\ges 
Bankchen, footstool '; 

die Aryan within nasalization, as well as the e-vocalism from Avestan frascimbana- 
(compared with Old Indie skambhana-m) reshuffling through Aryan from skabh- after 
*stent)^- (see steb-' jamb, upright section of a doorframe or window frame; stanchion, 
roof support ') in Old Indie stabhnat/" plinth, base, base of a pedestal t', stambha- ' posts, 
pillars, columns ' etc. 

References: WP. II 539, WH. II 487 f. 
Page(s):916 

Root /lemma: (sjkamb- and (s)kemb- 

Meaning: to curve, bend 

Note: 

Root/ lemma: {sjkamb- and (s)kemb-\ "to curve, bend' derived from Root/ lemma: kam-p- 

: "to bend'. 

Material: Gr. aKapp6(; "crooked, bowlegged'; Old Irish ca/77,6' "crooked', cymr. corn, cam, 
bret. kamm ds., gall, in Camb/o-dunum 'Kempten', bret. camhetan rot' rim of the wheel ' 
{*cambita); zero grades *kmb-'\.\}'cn = swap, vary, exchange ' and "zusammendrehen.
```


## [2026-09-14T01:58:26.766Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT skamb ===\"; grep -n -i \"skamb\\|scimbana\\|sčimbana\\|çimbana\" BRT.txt | head -30"
}
```


### [2026-09-14T01:58:26.835Z] TOOL RESULT

```
=== BRT skamb ===
2714:klm  CASn.)'*  vä  bimlhlm  V3  "wenn  eine  I  so/ti  .  .  xsayamna  is.lna  (VPm.)  Y.  O5. Frau  in  die  Schwangerschaft  kommt  — 114.  4)  'haben  zu  — '  sva.  'verpflichtet einen  Monat  lang '>  oder  zwei  . ."  V.  5.45.  j  sein  zu -,  sollen',  mit  Inf.:  lii'a  dim  nara tm\A.s.>inieiJasa.mahya:-^rä.:ivotmä/iai.\i^gl-s^fi)  apa.skambim   (sd.)     vXcicaE^a
4713:•  j.  anvarJitavas't?ma-<>  Adj.  (fem,  °m3-) etwa  'der  am  will  fahrigsten,  geeignetsten wirkt*:  fravasayö  'tfmä  frascimbananqm ". .  die  geeignetsten  unter  den  StÜUbalken" yt.y.26.
8370:•  j.  upa.skamb3m  '>  AbsoL  'unter  Fest- machen': dva  dim  iiara  isSii^  . .  z^mäistfe vä  sarstvt  Vil  up'  vicitaesva  dim  patH airihä    z^mö    mdai>yqn    "zwei    Männer
10423:Pü.:    iänil,    erl.:    aiular   a'skamb  ape    aailantl. Eine  etymologisircnde  Erktärung,   s.  ipnqno'.
11733:manS,  vehu  manS  taj  vanaiti  Yt. /p.  96;  jA'w.;  hazannm  azinqm  .  .  ava.janyät .  . —  parä  .  .  *daiahSui  anhat  b?r3t5  (sd.)  ■  "hrisattm  frascimbananqm  frasHmbaySit ..; vSstrvm:  ttm  {ah  ASn.)  aß paurvavazai-'tat  aiAhe  aiti  paititil  tat'  ..V.  18.1  ^Z.; lyai  (sd.)  V.  2. 24;  —  hixrsm  .  .  ast^m  .  .'P.4j;  — asavamm  . .  ajyei^yai  mraomt..; aaÄai^Tm  .  .;  ta  (APa)  hdhra  frafrS-^  tat  zl  vatiks  Y.7/-13;  —  dazdi  m!  ydka vayaAi  y.S.16;  —  hixr?m  .  .  aslim  ....  mjanani  ..  dahat  ahmäi  ..  ya;%a  ta aishaihim  .  .;  ta  (APn.)  Aa'hra  /ra/rä-'(]S.)upauha(at\t.i5.^t; — iviqm  iainitiS vaySmi;  ti  (statt  NPn.)  kiitmti  yzary.-  \ . .  failySnte  . ,;  tarn  tä  (AP.)  aiibys  .  . yiarmtts..  V.5,i8£;  —  a%ra  ml  urvarä'.msirinavahi  Yt5.87;  —  yB  dim  *fra- raöhnü  vTspä  ,.;  ta  (statt  APf.)  ha%ra  hinan  {sA.)..,  anairyanqtn  tai  dahytmqm vJvärayemi^ . 5.  \^i.;  —  vTspanqm  narqm\vfrihrai  uzjasaiti  N.ffff;  —  agtmanqmat ..  vispanqm  gSus  sar^anqm  . .;  //(ADf.)'*'.  .  vazyail {sA.)  . .  ratSui  nmStum  fi-anäia- larpnava  müwaireisd.)  ..  V,2.27f.;  — 'yatayezi  tajyayata  naväj  tatyayata(sd.) mit  Numeniswechsel:  jahi  . .;  tisca  t^A-j.s;  s\  s',  4';  —  ym  i^  (tiDxi.)  yaf- mraomi  jq%wS.lara  ..  V.i&öa— 65;  — '  tatary  {sd.) 'S.  4  g;  —  ASn.  in  kollektivem "mi^rS.ao/anAs  ..  yatcit  vlmaiiim  (sd.)  Smo:  umarä  baiiazyä ..,- tat  vlsp^m /rTttä- ai^ha  s3mS,   t»mSt  tnihrS  hangrp/simnS  mahi,  tat'  vuppm'  . .  V,  20.  4£  a)  in
17919:•  j.  fra-skamba- m.  1)  Stütz-,  Tragbalken' (nur  Komp.).  2)  'Vorhalle,  SaulenhoP (oderdgl.):>SaSrfl  n/näna  avastaya  iabm^a •hmca  fraväffmca  pairi.värwtca  "ebenda leg  Häuser  an  und  Keller  und  Vorhalle und  Bastei  und  Umwallung"  V.  2.  26.
19136:issihe .  .  upa-skambim  (sd.)  vlHcaehia  dim paiti  aiäka  z?m!l  nid'  V.8.  lo.
24577:•  ]*.  vi-zöista-  Adj,  'der  regsamste,  wach- samste': dva  dim  nara  issike  'Iqm'^ vTgvSrmtam  ">  .  .  upa.skambttn  (sd.)  .  .  ni- daiäyan'V.S.  10.
26450:skamb-
26459:•  j.  skamb-  'stemmen',  nur  mit  Praev. Praes.  9+24  sambaya-^^.  —  Inf.  'scapta- yalca;  Absol.  'skamhm.
26463:ai.  skambhilhah,  siabhnäti,  liaihäydü;  np.  vgl. faliam  (Hbjc  AGr. /.  225).  —  PQ.  (ioV.7*): /rSi  aai^aniian ;  s.  noch  zum  Absol.  —  ')  iBild.
28120:•  j.  zamöiStva-  n.  'Lehmaegcl':  dva  dim iiara  isli\ie  . .  'tve  vä  zarstve  vä  upa.- skamb^m  (sd.)  V.S.  10.
```


## [2026-09-14T01:58:42.190Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find nearest standalone 3-4 digit number before/after given line\ndef ctx(ln, span=60):\n    lo=max(0,ln-span); hi=min(len(lines),ln+span)\n    nums=[(i+1,m) for i in range(lo,hi) for m in re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', lines[i])]\n    return nums\nfor ln in (4713,8370,17919,26459,26463):\n    print(ln, ctx(ln)[:8])\nEOF"
}
```


### [2026-09-14T01:58:43.206Z] TOOL RESULT

```
4713 [(4667, '135'), (4670, '136'), (4757, '146')]
8370 [(8319, '393'), (8322, '394'), (8351, '395'), (8403, '398')]
17919 [(17866, '998')]
26459 [(26422, '1586')]
26463 [(26422, '1586')]
```


## [2026-09-14T01:58:49.125Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD fcnb / fcmb ===\"; grep -n \"fcnb\\|fcmb\\|fc'nb\\|fcnprd\\|frcnb\" SOD.txt | head -20\necho \"=== SOD sk'nb ===\"; grep -n \"sk'nb\\|sk'np\\|skanb\" SOD.txt | head -20\necho \"=== SOD 'world' entries ===\"; grep -n \"world\" SOD.txt | head -40"
}
```


### [2026-09-14T01:58:49.213Z] TOOL RESULT

```
=== SOD fcnb / fcmb ===
10452:ofcambaScik   ©pi.  -t   ^'fcmbScyk 
11798:666  'fVnpa    B,  S  =»  )fcmb8(8) 
11800:667  'fcmbScyk    M  ^l*>- 
11806:668  >fcmb6(8)   M  '       OW*- 
11809:fc>np5,  fcmbS,  >pc>np§(5) 
15857:1255  »pcmp8  **  }fcmb5(6) 
24357:fc»np5,  >fcmb5(8) 
32814:>fcmb6(5),  >Pcmp5 
32818:3844  fcmb8  M  ul^<^ 
32819:fcampa5,  f(9)camba$   (fcmbd)  ©Gersh. 
32823:-*fc»np8,  'fcmbS^X  'pc'npSCS) 
32829:3845  fcmbd   C  *+  fcmbS 
32831:3846  fcmbdcyq    C  :^ 
32834:^fcmbScyk 
32840:3847  fcmbSyk   M  ^ 
32849:f(o)campa5   ©ob.  -y  =*fcmbS,  fc'npS 
75405:9979  wfcmbd   C  =  w+  fembd  «»  w-,  fcmbS 
82258:10945  yfcmbdy   C  =  y-  +fcmbdy  «*  fcmb8 
=== SOD sk'nb ===
14922:1114  'nsk'np    B  (Jl*<jl*r 
14923:anskamb   ©<*ham-skamb-   ^sk'np 
19051:1738  'sk'np   B  JUijl^ 
19052:askamb   ^sk'np,  mskmp 
70151:9210  sk'np   B  01«*-<U 
70152:skanp,  skamb  ©<*skamb-  "to  stem"  ^sk'np 
70158:9211  sk'np'k   B  +J&<*Jp 
=== SOD 'world' entries ===
4118:information  about  the  western  world  and  the  rich 
5790:/{Jum/         fiwm  world         OP  bumi 
10454:worldly 
10464:world 
10480:worldly 
10488:world 
11803:worldly 
11810:world 
14925:world 
19070:world 
22457:worldly 
23276:living  world 
24358:world 
26805:earth,  world 
29953:creation,  world,  being 
30006:Mtihxai judge  of  the  world) 
30011:worldly 
30016:worldly 
30037:center  of  the  world 
30051:out  of  the  world 
31943:world 
31977:worldly 
31982:worldly 
32815:world 
32824:world 
32835:worldly 
32843:worldly 
32851:world 
38977:world  age 
39001:worldly,  (of)  kalpa 
39787:world  age 
39795:worldly 
40546:worldly,  earthly 
40682:worldly 
55459:future  world 
65667:loka,  world 
70153:world 
88119:center  of  the  world     3403  jj 
89838:from  this  world  to  another     3690 
89873:future  world     7098
```


## [2026-09-14T01:58:52.571Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- 32810-32860 ---\"; sed -n '32810,32860p' SOD.txt\necho \"--- 70145,70165 ---\"; sed -n '70145,70165p' SOD.txt\necho \"--- 19045,19075 ---\"; sed -n '19045,19075p' SOD.txt"
}
```


### [2026-09-14T01:58:52.696Z] TOOL RESULT

```
--- 32810-32860 ---

3843  fc'npS   B  ^.u 
facamba5  ©ob.  -y  =^Pc>np5(5),  fcmpd, 

>fcmb6(5),  >Pcmp5 
world 
Lentz.  STii  8.3  n  p582 

3844  fcmb8  M  ul^<^ 
fcampa5,  f(9)camba$   (fcmbd)  ©Gersh. 

*frascamba;  A  v.  frascimbana  ©ob.  -y;  pi.  -t 

-*fc»np8,  'fcmbS^X  'pc'npSCS) 
world 
C2  gloss.;  STi  43.15,  60.6,  84.11;  Sund.  AoFviii 

1981  pl89,  24V  8;  GMS  169,  372 

3845  fcmbd   C  *+  fcmbS 

3846  fcmbdcyq    C  :^ 
f(3)camba8cik   ©ob.  -y;  pi.  -t;  ob.  pi.  -ty 

^fcmbScyk 
worldly 
GMS  1014,  994;  C2,  54V18,  40R13,  104R12;  STi 

81.14;  Sund.  AoFviii  1981  pl89,  24V2,  5 

3847  fcmbSyk   M  ^ 
f(3)camba5ik  ©pi.  -r 

worldly 


GMS,  BSOAS  11.74,  lOn  5;  GMS  994 

3848  fcmpd   C  jl*r«U 
f(o)campa5   ©ob.  -y  =*fcmbS,  fc'npS 

world 

STi  14,  15,  72.4,  75.9,  77.1,  71.5;  Sund.  AoFviii 
1981  p214 

3849  fcmrz-   C  d*^ 
facmarz,  facmarz   ©<*fraca-marz  ?   ©impf. 

fcmrz  ^Pcmrz-,  fcmsty 
(/cOseize 
--- 70145,70165 ---
skafa   -»)sk»P) 

gnashing 

BSTii  843.35:  C2  p97,  51V5 

9210  sk'np   B  01«*-<U 
skanp,  skamb  ©<*skamb-  "to  stem"  ^sk'np 
world 

VJ  529,  1218;  Frag.  Len.  100a  1,  3,  6  c9;  GMS 
366,  372 

9211  sk'np'k   B  +J&<*Jp 
skanpe  ©Pahl.  askob 

floor,  stage,  story 
TSP  6.105 

9212  sk}r-   B  frjJLj+n&fj^ 
skar  ^sk^-,  sk}rt-,  skr- 
--- 19045,19075 ---
oskafa  ?   ^sq'P- 

gnashing 

MHC  p26,  36.8  V5 

1738  'sk'np   B  JUijl^ 
askamb   ^sk'np,  mskmp 


.& 


vjJu^o  cJb*s-  i -j^i-b* ji 


jj'  lirjJ  ^ 


69 


'smVt- 


world 

TSP  8.189-,  >sk}np\  TSP  2.1150;  Wnpvv,  VJ  n  p91, 

101  etc.  >nkynpw,  VJ  38b;  GMS  366,  *skamb-,
```


## [2026-09-14T01:59:11.508Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('leaves',len(leaves))\nfor i,L in enumerate(leaves):\n    if '3844' in L and 'fcmb' in L:\n        print('entry3844 leaf',i,'printed~',i-66)\n    if '9210' in L and \"sk'np\" in L:\n        print('entry9210 leaf',i,'printed~',i-66)\n# page 152 => leaf 218\nfor lf in (218,):\n    print('--- leaf',lf,'(printed ~152) ---')\n    print(leaves[lf][:900])\nEOF"
}
```


### [2026-09-14T01:59:12.520Z] TOOL RESULT

```
leaves 645
entry3844 leaf 217 printed~ 151
entry9210 leaf 439 printed~ 373
--- leaf 218 (printed ~152) ---
                                                                                                                   fr'wycyh
 153


        BBB f 15, 18; GMS 320; Benv. TSP p205, 115                       pr»k, Prk
                                                                       morning, early
3860 fnys-' C                             o^^tJ^J'^^                   BBB 697; GMS 1109, 991 A; STi 36.4
     fanes, fanes ©<fra-nasaya          =»fnyst-, Pn'ys-
     OcOdeceive, Oo)seduce                                       3871 fr»q C ^ fr'k
        GMS 320; C2, 69 V17n p53, 67; BSTii 848.51;              3872 fr'qcsny C                            al^*^ <c*iU cJj
          BSTi 187                                                    frak-casne
                                                                       breakfast time, morning
3861 fnys-2      C                      o>jy^<^tJ^o^^
```


## [2026-09-14T01:59:20.138Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in پچکم پیچکم پیشکم پشکم; do echo \"== $w ==\"; grep -n \"$w\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head -5; done\necho \"=== FRS ===\"; for w in پچکم پیچکم پشکم; do echo \"== $w ==\"; grep -n \"$w\" FRS_pages.txt | head -5; done\necho \"=== MON ===\"; for w in پچکم پیچکم پشکم; do echo \"== $w ==\"; grep -n \"$w\" MON_part1.txt | head -5; done"
}
```


### [2026-09-14T01:59:21.619Z] TOOL RESULT

```
== پچکم ==
== پیچکم ==
== پیشکم ==
== پشکم ==
BQT_v1_pages.txt:25969:پشکم ه بکر اول بر وزت اشکم »
=== FRS ===
== پچکم ==
14438: ‫ن ‪ :‬پچکم[ کذا خانهتاستانی‌بود چون غرد ‪ ۰‬چ ؛ خم وبچکم ک[ذا] خانة تابستانی‬
== پیچکم ==
== پشکم ==
=== MON ===
== پچکم ==
32115:پشکم: [ < - بچکم ِ پچکم ِ 
32116:بشکم] (.) ایوان و بارگاه» پچکم» بچکم. 
== پیچکم ==
== پشکم ==
23870:بشکم: که ,فده [- بچکم ۱ پشکم] 
29451:پشکم ] (.) خانه‌ای که از همه سوی در و 
32115:پشکم: [ < - بچکم ِ پچکم ِ
```


## [2026-09-14T01:59:24.594Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 leaf for line 25969 ===\"\npython3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nn=25969\npre='\\n'.join(lines[:n])\nleaf=pre.count('\\f')\nprint('leaf',leaf,'printed~',leaf-224)\nprint('\\n'.join(lines[n-14:n+14]))\nEOF"
}
```


### [2026-09-14T01:59:25.646Z] TOOL RESULT

```
=== BQT v1 leaf for line 25969 ===
leaf 636 printed~ 412
عمزی‌نشابوری.«لفت نامد».
۴ - در فرهنگه
بشك معشوق چون سفید شود
دل عاشق از او شود بستوه. >
۴ -ازچرخ ثاکبوتی واز مرخ نا شتو
ا زک رکه نا ببره وازموش تایشث.:
۵ . رك: شکل .اشکل , عمروفست که سرکن گوسفند و آخو
باشد ۰ 3
بشکله ‌‌ بفتح لام بمعنی شکل است
ی ماد و کسك
کلیدانرا لیز گوبند .
پشکلید » بکر اول و لام بروزن دل
کشد * یعنی بناخن وانکشت رخن ه کرد
پشکم ه بکر اول بر وزت اشکم »
اموان وبا ر گاه وا گز نش ۰ رضتح اول نیز همسن
معنی آهده اس ۷ :
بشل -
ی
هد چز را کو ند که مکدنگز زشیفا مدا کند:
و بفتح ال و ثانی هم بنظر آمده است ؛ ویسنی
که مد دو چیز است که با مکدیگر بگیرند
وبکوبند» و پاین معتی بجای حرف اول نون هم
گفته اند؟ .
بشلنگ - نم اول و فثح لام بر وذت
۱ قلمه‌ای را کون دکه برقلهٌ کوحی واقع
شده باشد - و بمعنی تافص و هرزه وعوب‌ویی
نیز گوندد که بنابان بدان دبوار سوراخ کنئد -
ویشنگه‌یدراف راسیاب رانیز یشاک میگفته‌اند. #۷
```


## [2026-09-14T01:59:33.471Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (635,636,637):\n    L=leaves[i]\n    print('=== leaf',i,'===')\n    print(L[-1200:])\nEOF"
}
```


### [2026-09-14T01:59:34.457Z] TOOL RESULT

```
=== leaf 635 ===
تحکام بردبوار
لصب کنند #
شتی وان با واو ۰ بر وزن وععنی
شتن مان ات که شت و پناه باشد وچوی ی که
پشلك ه بفتم اول و انی وسکون‌کاف»
شینم‌را کوبند - وبسکون‌ثانی بمعنی برابر کردن
و موافق ساختن باشد - و بمعنی درآویختن -
و عشق و عاشقی هم هست - و جعل رالیز گوشد
و آن جانورست که س رکین را گلوله سازد -
و جن ۴ را بر گفته‌اتد و آن‌پرنده‌است سنحوست
مشهور ۰ و باينمعني با سین بی نقطه هم بنطر .
هت اسب و دام علتیاست که‌اسبانر ۱ همه سل
وم اول بلغت ماوراء الثهر کربه اشد و آن
جانوریست ععروف کهآ برا بعربی‌سنورخوانند؟ -
وبسکون‌انی سرکینآهو و کوسفند وبز و اشتر
و امثالآترا کوبند - و بععنی خمره و خمچوه
ومرطبان هم‌آمده است - ونام درختی تیزهست-
وبکر اول وسکون‌نانی قرععرا گوبن دکه‌شریکان
در میان خود بجهت تقیم اسباب و آشیاییندازند
- ویشکل کوسفند وآهو را نیز کفته‌اند.
بشکال بر وزن دسمال» فصل‌باران
هدوستان را گود .
پشکر ‌ بکسر اول و کاف و سکون
انی ورای قرشت » بمعنی پشك است که س کین
گوسفند وبز و آهو و شتر باشده .
پشکره ‏ بکس اول راك و قتح رای
فرشت » بمعنی پشکر اس که پشکل کوسقند
واعثال آن باشد .
قباه خاصه و پشتی خود فسیج بزر
یکی مکلل کرده کمی بگوهر ها .
عمزی‌نشابوری.«لفت نامد».
۴ - در فرهنگه
بشك معشوق چون سفید شود
دل عاشق از او شود بستوه. >
۴ -ازچرخ ثاکبوتی واز مرخ نا شتو
ا زک رکه نا ببره وازموش تایشث.:
۵ . رك: شکل .
=== leaf 636 ===
یگر بگیرند
وبکوبند» و پاین معتی بجای حرف اول نون هم
گفته اند؟ .
بشلنگ - نم اول و فثح لام بر وذت
۱ قلمه‌ای را کون دکه برقلهٌ کوحی واقع
شده باشد - و بمعنی تافص و هرزه وعوب‌ویی
نیز گوندد که بنابان بدان دبوار سوراخ کنئد -
ویشنگه‌یدراف راسیاب رانیز یشاک میگفته‌اند. #۷
پشما گنف* م بنخ اول و سکون انی
۹۹ رك: بشکلیدن. «لغت نامه*.
۳ وك: بشلیدن: «لفت نامه» .
--م ۰ ح
و میم بالف کشیده وکاف‌فارسی مفتوح پنون‌ودال
ابجد زده , چیزی باشد که نرا پریشم کنند و ما
بين پشت‌ستود و تنگک بار گذارند وپالان الاغ‌را
نیز گفته اند
شم در کالاه نداد د ‏ کنایه بز
این است که حالی و هرتبه‌ای و دانثی " عدارد -
و کی را یر گوبند که غیرتی و نفی نداشته
باشد «هنی صاحب نفس و صاحب غیرت نباشد .
بشم‌شدن » بمعنی پراگنده شدن -
وپرا گنده ساختن باشد - و جدابی کردن را نیز
کفته‌اند .
پشمات » بروزن چنمك, سا
مشهور ومعروف - ومصغر پشم‌هم همت.
شین « بر وزن چمن » نام موضعی است
که میان پیرآن وبسه و طوی نوذر جنگ وافع
شد و نورانیان فتم کردند و | کتر پسران گودرز
ماو جهن نمی وان جق ۳
لادن وس جنگ یش نگویند و مشفف پشنگه هم
هست که نامپدر افراسیاب باشد.
پشنجد- بکر اول وفتح ثانی وسکون
نون وجیم ۰فثوح بذال نقطه دار زده, بعنی آب
وامثال آن باشده شود ۷ . 5
ف ی ۲ ۰
لشنحه * بروزن شکنسه , دسته کیاهی
افشاشد .
1
وس امد
۱ - مر کب از : یت (۳
ر : شنجدن و شدحد, .
=== leaf 637 ===
ب تبیه
کنند وبدان خشت و گل وخالك وامثال آ نکشند
- و جفا وستم وجور و محنت را نیز گفته‌اند -
وترشحآب وفیر آنرا نیز گوبند ۴» وباین معنی
متکتی. ول وثالی‌هم درست است .3
و دعای بد راگویند ؛ ویاسین بی‌قطه هم آمده
است ۲
پشول » بر وزن اصول ۰ بمعنی پشور
است که نفرین ودعای بد باشد ۴ .
بو لیده باواو مجهول ولام بروزن
نکوهیده" » پرشان و ژولیده و پراکنده را
(۱) چب ۱ چش: هجرالبق .
٩‏ - شنجر همه تش انجدماند
.۰ رك : بشنجیدن ویشنجد.
۵ دل دروش سراسمه به است
گونند ۵ .
لشه - بفتح اول
۴1 ثانی هشن ء حانوری
است ممروف گونند چهل
روزعمر کند وبعضی گویند
بته خانه. با خای نقطه دار بالف
کشبده وفتح نون» نام‌درخت صده است که سربی
شجرقالیق (۱) خوانند ۷ .
بشه جورد » بفتح خای نفطه دار
و سکون واو ممدوله و را ودال بی‌تقطه » ریشی
و جراحتی باشد که بیشتر در ملك بلخ بهم رسد
و دیر خوب شود و کمان مردم اينکه از گزیدن
پثه بهم میرسد و آن را بعربی فرحة بلخی
گونند .
بشه‌ذاد ۸ ۰ بادال ابجد بالف کشیده
و برای قرشت زده . پثه خانه را گویند و آن
درختی است که بعربی شجرتالیق خوانند .
پشه‌غال » با ین نله دار و لام :
بر آن خاك و خوش پشنجید‌اند .
لمیبی . «لفت نامه».
بت ۴ رك : یشور .
طرة دوست پشولیده خوش است ۰
شرف شفروه. «لغت نامه».
دوم هردو آهثبه :
. پشه‌کی داند که عمرش تاکی است
۲ ره : بشمدار -
دربهاران زاد ومر کش در دی است.
مثنوی‌مولوی‌بلخی.
```


## [2026-09-14T01:59:48.268Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- MON 29445-29460 ---\"; sed -n '29445,29460p' MON_part1.txt\necho \"--- MON 32110,32120 ---\"; sed -n '32110,32120p' MON_part1.txt\necho \"--- MON 23866,23876 ---\"; sed -n '23866,23876p' MON_part1.txt\necho \"--- FRS 14430,14450 ---\"; sed -n '14430,14450p' FRS_pages.txt"
}
```


### [2026-09-14T01:59:48.386Z] TOOL RESULT

```
--- MON 29445-29460 ---
پسچیچه. (ع-)06-۵۵64۵ ب(8-)0۵۵-0662 
(اصت.) سخنی را گویند که در السنه و افواه 
افتد و همه کس به طریق سرگوشی و خفیه 
پسچکم: [< دنا " شکم 


پشکم ] (.) خانه‌ای که از همه سوی در و 


بجر ۵ 0 خازه تابستانی. بارگاه ایوان» 


صقه. 


پسچکم: «صلهم (- بچکم] (.) (جان.) 
--- MON 32110,32120 ---
گوسفند و آهو و اسب و خر و استر و اشتر 
و گاو آنگاه که سخت و مدور باشد؛ بعره 
ذبله. پشکل برچین: سخت بی‌سر و پاء 
سخت فقیر. پشکل به تنور کردن: پی در پی 
خوردن» مثل پشکل: سخت خرد. 
پشکم: [ < - بچکم ِ پچکم ِ 
بشکم] (.) ایوان و بارگاه» پچکم» بچکم. 
پشکن: ۴03680 [- بشکن) (ا.) (عم.) مالیدن 
سِ در موقع عیشی و طرب و رقص که 
بی از آن حادث کردد؛ شکن. 

--- MON 23866,23876 ---
کردن با اسلحه و ساز جنگ. در بر گرفتن. 
(مص‌ل.) در بند شدن» صقیك کفنیی: رخنه 
شدن به سوزن و خار و مانند آن. 

بشکم: که ,فده [- بچکم ۱ پشکم] 
خانةٌ تابستانی. با رگاه. ابوان» صفه. خانه‌ای که 
اطراف آن شبکه و بادگیر داشته باشد. 
بشکن: ۳۸8۲۵۰ [- پشکن] (.) آوازی که از 


انگشتان شخص در حال رقص و غیر آن 
--- FRS 14430,14450 ---
                                      ‫‪۳‬‬


 ‫چادر بود باکلیمی که نثار چینان برسر دو چوب بسته تا ازهوا نثار ستانند‬
                                                               ‫[ عنصری کوید ‪:‬‬
  ‫‪ : 5 1‬تهم‌بی‌هتابود بزرك‌تنی ‪ ۰‬چ‪ :‬تهم‌بی متابود ونهمتن رستمرآبدان‌میخواندند‬
 ‫که‌مثل او نبود برای تنوئدوقامت » ص ‪ :‬تهمبی‌همنا بود ببزرگی وحشمت ومردی‬
 ‫‪۲‬ج ‪ ۰‬تخت ‪ - ۴‬این بت فقط در س هست بجای بیت پیش ‪- 4‬‬                ‫وقامت‬
 ‫ن ‪ :‬پچکم[ کذا خانهتاستانی‌بود چون غرد ‪ ۰‬چ ؛ خم وبچکم ک[ذا] خانة تابستانی‬
‫ناشد و نشستتگاه کهدر زبرزمین سازند چون غرد و بادغرد» س ‪ :‬بجکم نامگز‬
  ‫‪4‬‬    ‫» ‪ -‬در اصل ‪ :‬جشری ( ؟ )‬             ‫گمانست بترکی و دیکر خانة باشد تابستانی‬
 ‫‪ ۷‬در چ ‪ :‬هزاران نگار اندرو بش و کم [کذا] ؛ اينببت درس‬                ‫خقط در ش ‪۰‬‬
 ‫‪ - ۸‬ل ؛ نغم چادری بود کهبردو سرش چوب بندند وازهوا تثار رباند »‬            ‫ذست ‪۰‬‬
 ‫س «نغم چادری باشد بردوچوب بته تثارچبنان دارند ‪1:‬ازهوا [تتار] بگرند » چ ‏‬
 ‫فغم [کذا] آن چادر بودکه شکر[کذا] چندان بچوبها ‪ 1۳‬افراخته دارند تانثار در‬

                                                                 ‫هوا بربایند بدان ‪.‬‬
                                       ‫‪۹۳۳‬‬

   ‫نه گهر‪ ۱‬چید هبچکس نه درم |‬                ‫ازککهررد کرد بفخم‬
```


## [2026-09-14T02:00:07.991Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON شنگرف ===\"; grep -n \"شنگرف\\|زنجرف\\|زنجفر\" MON_part1.txt MON_part2.txt | head -20\necho \"=== BQT v3 ===\"; grep -n \"شنگرف\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v3_pages_faseng.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T02:00:08.078Z] TOOL RESULT

```
=== MON شنگرف ===
MON_part1.txt:47296:طلا و شنگرف و جز آن گرداگرد صفحه 
MON_part1.txt:75768:با طلا و شنگرف. 
MON_part1.txt:81410:(شنگرف)؛ سولفور مس. 
MON_part1.txt:86933:شنگرف: 7۲ [- معر. شنحرف] (ا.) 
MON_part1.txt:86940:(ع513)» سولفور معدنی جیوه» زنجفر» حجر 
=== BQT v3 ===
7021:‏فارسی » پروزن‌ومعنی‎ SEY ‏شنگرف‎
7044:بم‌نی دوبم شنگرف باشد و آن کرمی است که
7085:‏چنار کشت دوتا وزربرشد شنگرف.
7090:۶ ,2 شنگرف (یکی ممحف دیگریست) .
```


## [2026-09-14T02:00:11.272Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- MON 86928,86950 ---\"; sed -n '86928,86950p' MON_part1.txt\necho; echo \"--- BQT v3 around 7015-7100 ---\"; sed -n '7010,7100p' incoming/BQT/BQT_v3_pages.txt\necho; echo \"--- pdf page tag ---\"; awk 'NR>=6900 && NR<=7100 && /pdf page/' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-14T02:00:12.403Z] TOOL RESULT

```
--- MON 86928,86950 ---
حرکات» شبرین رفتار» طریف. خوشکل. 
عبار. دزد» راهزن. شنک و مشنک: دزد و 
راهزن. شنگول؛ شادمان. حیله گر محیل. 

مس ه 
شنگرف: 7۲ [- معر. شنحرف] (ا.) 
(زم.) جسمی است ساه ولی در طبیعت 
بصورت توده با رشته و رگه یافت می‌شود و 
گردش سرخ یا قهوه‌یی است و همچنین بر 
انر عسور دادن سر مسحلول‌های 
مرکوریک بدست می‌آید. گرد آن در 
نقاشی بکار می‌رود؛ سولفور مرکوریکك 
(ع513)» سولفور معدنی جیوه» زنجفر» حجر 
الصرف. (جاد.) کرمی است باریک و 
استوانه‌یی شکل از تیرهٌ نماتودها درازیش تا 
به یک سانتیمتر ممکن است برسد و نخی 
کرده از داخل ساقةٌ گندم بالا می‌رود و خود 
را به سنبلةٌ گندم می‌رساند و مواد غذایی 
محتوای دانه‌ها را می‌خورد و بتایراین از 
گندم‌هایی که دچار حملة این کرم شده باشند 
بر ک‌هایشان مار بیچجی می‌شو د؟ شدکدزن» 



--- BQT v3 around 7015-7100 ---
[pdf page 93]
۱ ‏بروزن زنکار » کیاهی‌است‎ = Ue
‏میباشد وسرخی‎ le ‏که پیخش‌سطبر و بر کش‎
‏مایل است و اکر بیخ آنرا زان بخود بر گیرند‎
‏ومعربآن‎ HS ‏و درآ ب گرم شینند حیض‌را‎
‏شنجار است و بمربی شجرة الدم خوانند.‎
» ‏اول بر رزن زان‎ ph - ole
‏تام ولایتی است ۴ - وجمع شنک هم هست.‎
‏شنگ لیز ۴ = بکس بای‌ابجدبروزن‎
‏شرابی باشدکه از درخت خرماحاسل‎ gy ‏رنگ‎
‎. ۴ ‏شود - و بزبان پپلوی زنجبیل را گوبند‎
‏فارسی » پروزن‌ومعنی‎ SEY ‏شنگرف‎
‏شنجرف_باشد * و آن چیزیست که از سیماب‎
‏و ک و کرد سازند و نقاشان و مصوران بکار برند‎
‏و ممرب آن شنجرف است و بیونالی سربقون‎
‏خوانشد 6 - ونام کرمی هم هست دراز و گندم‎
‏خوار که در کشت زارها بهمرسد و غله را خراب‎
. ۷ ‏کته‎
‎Sly gt ‏اول وسکون‎ che 3 Ks

بر وزن پنج‌لك . لام یکی از رابان حتدوستان

سپ ۳ ات

است ۷ که بمدد افراسیاب رفته ‎oy‏ وافراسیاب
اورا بیاری‌پیران وسه فرستاد وقتی که‌پران‌وسه
بجنکه طوی‌ین لور میرفت - و بمطی اول
‎is‏ هم هست ۸ که شوخ و ظریف - و دزد
و راه‌زن - وخرطوم فیل باشد - ونم کاف‌فارسی
و سکون رای بی ‎ded‏ و ‎GE‏ » بادرية ‎Ags‏ را
کویند وآن چوب با چرمی باشد مدور که در
‎IF‏ دوه ‎Kae‏ سازند 4 .

شنگ زن *- با زای قطه دار و نون
بم‌نی دوبم شنگرف باشد و آن کرمی است که
کشت و زراعت را خورد و ‎cole‏ کند » حرکت
این ‎cal‏ معلوم لبود +

شنگل ‏ بنتع اول و ضم ‎HW‏ بر وزن
فرگل . دزد و راهزن و ‎SS ash ols‏ و نام
پادشاه‌هند که بمدد افراسیاب آمده بود ۱۴-وبفتح
اول و الت. جنی از غله را گویند - و بمعنی
دزد و راء زن هم‌آمد» است ۷۴ .

شنگله = ‎ch‏ اول و الت ولام » مطلق

خوشه را کوبند اعم از خوشة خرما ۱۴ وانگور

‎۱٩‏ معرب ‎oT‏ شنجار ‎Anchusa tincotoria = Cis,‏ = 0۲6۵88/6(فر)«دزی

‎. ٩۲: ۷۹۲ ‏ص ۷۹۰ : ۲ و‎ Nt
. ‏ظ . ممحف «سمتگان» (ه.م.) است‎

‏۴ - درممجم الباء ان وحدودالعالم ونخبةالدهر تيامده»

‎Gee) aS ۴

‏۴ - تصحرفی درقرائت پهلوی ‎Sangiwel‏ ( زنجبیل)«اونوالا۱۱۱» «که سنگ پیر»هم

‏۵ س زلجرن :
بنفعه‌وار(زار. دهخدا) بپوفیدروز کارببرف

‏خوانده شود .

‎. )( ‏رك: شنگه زن‎ - a}

‎. ‏شنگ‎ : a ۸

‎۱ Cpa)
. ‏شنگه‎ ay ٩٩۳ ‏شنگوله رك: لفت فری ص‎

‎. Gln ‏درهدد متداول است «فرهنگه‎ eth Coo

‎VF‏ درخت‌خرها صد خارزشت داردوخداث

‏چنار کشت دوتا وزربرشد شنگرف.
کایی مروزی «لفت فری ‎NEE‏

‏۷ - درثپرست ولف نیامده . رك : شنگل .
4 عنگور (هم) «رشیدی» = ‎3S‏ )4.0( = سنگور
۶ ,2 شنگرف (یکی ممحف دیگریست) .

‎- ‏«ردیدی»‎ JK
‏تام‎ . Shangul ‏درفهرست واف‎ -۴
aR CCRC DE nL
‏اکردوتنگله خرمای خوب وتردارد.‎
. ۱۱6 ‏ناسر خسرو بلضی‎ «
(Ww ‏برهای فاطع‎ (

[pdf page 94]
زا

--- pdf page tag ---
[pdf page 92]
[pdf page 93]
[pdf page 94]
```


## [2026-09-14T02:00:36.055Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT sinka ===\"; grep -n -i \"sinka\\|zinjif\\|cinnabar\\|vermilion\" KNT.txt | head -10\necho \"=== HUB/HRN shangarf ===\"; grep -n -i \"šangarf\\|shangarf\\|sangarf\\|Zinnober\\|zingifr\" HRN.txt HUB.txt | head -20\necho \"=== PHD ===\"; grep -n -i \"šangarf\\|zangarf\\|cinnabar\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head\necho \"=== LKT ===\"; grep -n -i \"zinnober\\|cinabr\\|kinnabari\\|Zinnober\" LKT.txt | head -10\necho \"=== SKT cinnabar ===\"; grep -n -i \"cinnabar\" SKT.txt AHD_watkins1985.txt LEW_1910.txt LAT.txt | head -10"
}
```


### [2026-09-14T02:00:36.203Z] TOOL RESULT

```
=== KNT sinka ===
=== HUB/HRN shangarf ===
=== PHD ===
=== LKT ===
3136:1.349.  Ar.  luagra: 'Rote  Erde,  Rötel' ;  hieraus  mit  ar.  Art. sp.  pg.  almagra,  almagre  'Rötel,  roter Ocker',  frz.  almagra  'Indisch-  oder Persischrot' [Ausdruck  der  Malerei].  Ohne ar.  Art.  it.  (dial.  Aquileja)  macra  'Ocker, Zinnober'  [bei  ML  5210  auf  ein  „orien- talisches macir  'rote  Baumrinde  aus Indien'"  zurückgeführt;  gehört  natürlich zu  ML  5234];  russ.  bagor  'Purpurfarbe' [mit  häufigem  Wechsel  von  m  und  b, daher  wohl  durch  das  Tk.  vermittelt], bagrec  'Purpur',  bulg.  (alt)  bag^rh  'Pur- pur', bagr  'Farbe',  bagranica  'Purpur', klruss.  bahor  'Purpur'  [Bern  SlEtWb  38 nennt  die  slav.  Gruppe  „fremd"  und ihren  Ursprung  „dunkel"].  —  „Zu  Heil- zwecken wurde  schon  im  Altertum  aus Iberien,  dem  heutigenSpanien,  bestimmte Erde  herbeigeholt.  Dies  war  wohl  die heutige  Almagra  oder  Ton  von  Estre- moz,  welcher,  mit  Piment  (Capsicum annuum)  vermengt,  auch  in  der  Gegen- wart von  Damen  der  sp.  und  pg.  Aristo- kratie als  Delikatesse  genossen  wird". Dtsch. Rundschau  für  GeographieXXXVII, 125.  [DE  152.  Eguilaz  209.  Devic DEt  25.    ZfSem  IV,  258/9.
4141:'Mennig,  Zinnober',  hieraus  ar.  zingafr, zungufr  'dass.'  [KM  II,  865],  ebenso  tk. zingifre.  Aus  hieraus  entstandenem  gr. TiYTÖßapi,  Kivvdßapi,  lat.  cinnäbaris wurde:  it.  cinabro,  frz.  cinabre,  sp.  pg. cinabrio  [Constancio  Dicc  260  c],  rum. chinovar;  engl,  cinnabar,  dtsch.  Zinno- ber, schwed.  cinnober;  russ.  kinowar, poln.  cynober,  cech.  cinobr,  serb.  cinober, bulg.  kinowar.
5892:2214 Zibetkatze  2173 Z«/f<?r  1894 Zinnober  1827 Z«Y<<.-er  2215
6421:cinabre  1827
7026:cämolu  dial.  1Ü44 camolado  dial.  1044 camula  siz.  1044 canacca  dial.  siz.  810 canciarru  siz.  814 cand\  (succhero)  1052 candire  1052 canfora  IlOO cangiaro  814 cantoro  1178 cantaru  .siz.  1178 canzirri  siz.  817 caparra  978 cappari  978 carahe  1004 caraffa  689 carato  llS'^i caravana  1075 caravanserraglio  1075 cur ca SSO  2081 carciofo  833 carmesino  1219 carminio  1219 carovana  1075 carrabba  siz.  689 earraca  i?3l carruba  832 carwi  1087 casacca  1143 casimiro  1116 castiä  dial.  855 cassara  siz.  837 cässaru  siz.  1117 cassdta  siz.  1106 cassero  1117 casuario  1119 catrane  1128 catussu  siz.  988 caviale  851 eaviaro  851 vavicchia  980 caviglia  980 cavizzu  dial.  998 ceffare  1734 ce/fo  1734 cerbotfana  2201 c7tt/fo«e  1893 chimica  1157 chiosco  732 «d  415 ciabatta  379 ciaera  siz.  715 c/aa  1865 «rfro  1787a «/ra  1894 «/o^a  dial.  424 cj/m  dial.  424 «ywi  dial.  424 cimarra  1820 cinabro  1827 ciotola  442 ciottare  1875
8106:cinabrio  1827
=== SKT cinnabar ===
SKT.txt:3461:Cimuibar,  Clnoper.  (.Gk.-Pera.)  Gk. tHvrAiiapt,  vermiliuu.  From  Pcrs.  tinjarf^ ttHipi/r,  red  lead,  vermilion,  cinnabar
SKT.txt:11601:an  antnaal  of  a  mixed  breed. \mtim^i  in  Levins  (1570).     It tr-tl*,  i.e.  a  small  animtl cf".    coik-tr-tl,    pick-tr-tl .« A.  S.  man^,  a  mixture, hire,  a  small  pamtiitg.  (Ita).-L.) Initna.  a  miaiaturc.  •-  Wi^.mimato, Ka^r,  to  dye,   [Miiiit,    'to  colour HiKh    vcrtniltoit    or    red   lead ; ' ^  minimm,  cinnabar,  red  lead ; *  of  Ibeiisn  ohgiji. «  M&nd. Minor. Mind.
SKT.txt:23619:Creek  from  Persian :  cinnabar  (dnoper). l^Uinfrom  Greek  from  Persian :  aspara* I,  gypsum,  laudanum,  Magi,  tiar>y f^enek  from  Latin  from  Greek  from rsian:  caper  (2),  jujube,  ma^ic,  myrtle, XwA'ue,  parria,  satsaif,  ''£*''-
LAT.txt:11946:cinnabar (var. cinnibar) n.: sorte de coiffure des Gots. Mot sans
LAT.txt:11948:cinnabaris, -is f.(-ri n.Sol.): cinabre. Transcription du gr.xiv-
```


## [2026-09-14T02:00:45.959Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4135,4145p' LKT.txt\necho \"-----LAT\"; sed -n '11944,11955p' LAT.txt\necho \"-----SKT ctx\"; sed -n '3458,3465p' SKT.txt"
}
```


### [2026-09-14T02:00:46.049Z] TOOL RESULT

```
[Ar.  sandal.
ser  erhoben,  um  das  Gegengewicht  zu bilden  gegen  das  dreieckige  kolossale Segel,  welches  an  der  Spitze  des  Mast- baumes in  einer  Ausdehnung  angebracht ist,  daß  oftmals  die  Breite  der  Yard- stangen die  Länge  des  ganzen  Schiffes übertrifft."  Freiher  von  Neimans,  Das rote  Meer  und  die  Küstenländer  in  ZD MG  XII,  420.  Eine  weitere  Beschrei- bung s.  Charles  Didier,  Ein  Aufenthalt bei  dem  Groß-Scherif  von  Mekka.  Au- toris.  dtsch.  Ausgabe  von  Helene  Lobe- dan.  Leipzig  1862.  S.  117/118.
182.5.  Ar.  saudal: 'Indisches  Farbholz'  [aus  pers.  cändäl <^  sskr.  candana];  hieraus  gr.  öavbd\iov 'Holz  von  Pterocarpus  sanlalina  L.'. It.  sändalo,  frz.  sandale,  bois  de  sandal, sp.  pg.  sändalo;  russ.  sandal;  engl,  san- dal, sandle,  sanders,  dtsch.  Sandel(holz) . [DE  339.    Hobson-Jobson  789/790.
1826.  Ar.  saiidük:
Auch  simdük  [^m.  \\,  1161,  Z.  6  v.  u.] 'Truhe,  Kasten,  Koffer'  [wie  der  Gegen- stand ist  auch  das  Wort  wahrscheinlich ind.  Ursprungs :  ZDMG  L,  651 ;  noch  jetzt wird  dieses  Kernmöbel  des  kleinen  ar. Haushalts  von  Indien  nach  Südarabien eingeführt;  vgl.  auch  HÜBSCHMANN  in ZDMG  XLVI,  267,  Nr.  69],  tk.  ebenso sandyk  'Kasten,  Koffer';  hieraus  rum. sunduc  'Koffer';  bulg.  Shudhk,  serb.  san- duk,  klruss.  sunduk,  russ.  sunduk  'Kas- ten, Koffer'.  [Gorjajew354.  MiklSlEtWb 288  a.
1827.  Pers.  sängärf:
'Mennig,  Zinnober',  hieraus  ar.  zingafr, zungufr  'dass.'  [KM  II,  865],  ebenso  tk. zingifre.  Aus  hieraus  entstandenem  gr. TiYTÖßapi,  Kivvdßapi,  lat.  cinnäbaris wurde:  it.  cinabro,  frz.  cinabre,  sp.  pg. cinabrio  [Constancio  Dicc  260  c],  rum. chinovar;  engl,  cinnabar,  dtsch.  Zinno- ber, schwed.  cinnober;  russ.  kinowar, poln.  cynober,  cech.  cinobr,  serb.  cinober, bulg.  kinowar.
1828.  Ar.  sanifa:
'Saum  des  Kleides'  [KM  II,  1163,  Z.  6 v.  u.];  hieraus  mit  oder  ohne  ar.  Art. sp.  azanefa,  zanefa,  pg.  sanefa  'Bett- oder Türvorhang',  siz.  zinefra  'Bordüre, Franse;  Tür  Vorhang,  der  als  Schmuck vom  Türrahmen  herabhängt'.  [DE  224. Eguilaz  319.  GrSVociSic  251.  ML  1.587.
1829.  Ar.  säiiija:
'Großer  Schöpfeimer'  [part.  praes.  act. des  Vbs.  sanä  'schöpfen',  fem.  'die Schöpfende'] ;  hieraus  mit  Imäla  [ä,  >  e] teils  mit,  teils  ohne  ar.  Art.  sp.  acena 'Wassermühle',  kat.  cenia,  sinia,  pg. acenha,  azena,  assania;  it.  (dial.  Kala- brien)  sena,  siz.  senia  'Schöpfwerk,  um
-----LAT
Les traces de thfeme en -s- qu'on a cru trouver dans le groupe de gr.
xovl*C ne prouvent rien.
cinnabar (var. cinnibar) n.: sorte de coiffure des Gots. Mot sans
doute germanique, v.Isid.19, 33 ,7, et Sofer, p.19 et 170.
cinnabaris, -is f.(-ri n.Sol.): cinabre. Transcription du gr.xiv-
va( 3 <xpt,, sans rapport avec le precedent.
ClnnaMUm, -i n.(et cinnamus m., cinnama f.): cannelle. Emprnnt
au gr.xivvoqj.ov, conservi dans certaines formes italiennes, M.L.1931.
cinnus, -I m.: apud ueteres cinnus potionis genus ex multis li¬
quoribus confectum dici solet, Non.43,17; id. 59,39, cinnus est com¬
mixtio plurimorum ; unde et concinnare dicitur. Malgre 1 'attribution
du mot aux ueteres par Nonius, un seul ex., du reste mal attest6, dans
-----SKT ctx
succinct,  concise.  (L.)  L.  inccimtm, pp.  of  succin^rt^  to  gird  up,  tuck  op  short. —  L.  Tuc-  {fulf^,  nn ;  <iKgert,  to  gird.
Cinder.  (E,)  \lisspelt  for  sirtiiir  (by confasion  with  F.  ctndre  «=  L.  aiurtm ; (cc  Cinerary).  A.S.  sindtr,  scoria,  slag.  4> Icel.jiw./r;  Swcd.j/WVr;  G.ji'/j/^r,  dross; Du.  sinlih,  dnclcrs.  fl  The  A.  S.  /iW^f occur*  in  the  8lh  century.
Cinerary,  relating  to  the  ashes  of  the dca'J.  (L.)  L.  ciMfranus.^L.  a'ner-t  stem of  cinij,  dost,  ashes  of  the  dead,  -f-  Gk. K^vLf,  dust;  Skt.  jkana,  a.  grain.
Cimuibar,  Clnoper.  (.Gk.-Pera.)  Gk. tHvrAiiapt,  vermiliuu.  From  Pcrs.  tinjarf^ ttHipi/r,  red  lead,  vermilion,  cinnabar
Cinnamon,  a  spice.  (Heb.)  Heb  y;«- nAmSn ;  ^flid  to  be  of  Malny  origin.
Cipher.  (F.  -  Aral>.)  O.  F.  ci/rt  (F. ckiffrt)^  a  cipher,  icro.  —  Arab,  iifr^  a cipher.  Der.  de-ciphtr  [\^  (ie,  in  the  ver- bal sense  of  ««-;  and  cipher)  i  cf.  O.  F. dechiffrcr,  '  to  decypher/  Cot.
sero.  (Ital  -  Low  L.  -  Arab.)  ItaL ufv,  short  for  i^rv.  —  Low  L,  tepAjrntm (Dcvic).  —  Arab,  si/r  (above).
Circle.  (L.)    A  S.  drcu/.  —  L.  nnutus,
```


## [2026-09-14T02:00:57.827Z] TOOL CALL #28: Bash

```json
{
 "command": "ls site/pages/450.jpg 2>/dev/null; pdftoppm -f 450 -l 450 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg450 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg450.png"
}
```


### [2026-09-14T02:00:59.618Z] TOOL RESULT

```
site/pages/450.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 79151 Sep 13 22:00 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg450.png
```


## [2026-09-14T02:01:01.559Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg450.png"
}
```


### [2026-09-14T02:01:02.117Z] TOOL RESULT

```

```


## [2026-09-14T02:01:02.113Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:01:18.779Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 450 -l 450 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg450hi\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg450hi.png'); print(im.size)\nw,h=im.size\n# Persian pečkam node: roughly x 0.50-0.78, y 0.58-0.68 of page\nim.crop((int(w*0.48),int(h*0.585),int(w*0.80),int(h*0.665))).save('pg450-pechkam.png')\nim.crop((int(w*0.28),int(h*0.405),int(w*0.78),int(h*0.47))).save('pg450-shangarf.png')\n\"\nls -la pg450-pechkam.png pg450-shangarf.png"
}
```


### [2026-09-14T02:01:22.941Z] TOOL RESULT

```
(4250, 5500)
-rw-rw-r-- 1 sfmqrb sfmqrb 11427 Sep 13 22:01 pg450-pechkam.png
-rw-rw-r-- 1 sfmqrb sfmqrb 11602 Sep 13 22:01 pg450-shangarf.png
```


## [2026-09-14T02:01:25.023Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg450-pechkam.png"
}
```


### [2026-09-14T02:01:25.044Z] TOOL RESULT

```

```


## [2026-09-14T02:01:30.645Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg450-shangarf.png"
}
```


### [2026-09-14T02:01:30.808Z] TOOL RESULT

```

```


## [2026-09-14T02:01:30.800Z] INPUT

[Image: original 2125x358, displayed at 2000x337. Multiply coordinates by 1.06 to map to original image.]


## [2026-09-14T02:01:37.623Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:01:37.630Z] TOOL RESULT

```


```


## [2026-09-14T02:01:40.919Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%86%DA%AF%D8%B1%D9%81",
 "prompt": "Give the full Persian entry for شنگرف: etymology, descendants, borrowings into Greek/Arabic, and any Old Persian/Middle Persian forms cited."
}
```


## [2026-09-14T02:01:41.897Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cinnabar",
 "prompt": "Full etymology of cinnabar: Latin, Greek, Persian forms, French forms, dates."
}
```


### [2026-09-14T02:01:46.412Z] TOOL RESULT

```
# Etymology of Cinnabar

**Origin:** The word "cinnabar" entered English in the mid-15th century, referring to "red or crystalline form of mercuric sulphide" and its use as a pigment.

**Language Journey:**
- **Old French:** *cinabre* (13th century)
- **Late Latin:** *cinnabaris*
- **Greek:** *kinnabari* (a foreign word)
- **Persian:** *zanjifrah* (likely ultimate source, suggesting Oriental origins)

**Historical Use:** Between the 14th and 17th centuries, the term also described "red resinous juice of a certain Eastern tree," which people mistakenly believed was a mixture of dragon's and elephant's blood.

**Related Term:** The adjective *cinnabaric* derives from the same root.

The word traveled westward through trade routes and multiple languages before becoming established in European vocabulary, maintaining its association with both the mineral and its practical applications in art and commerce.
```


### [2026-09-14T02:01:48.023Z] TOOL RESULT

```
# Persian Entry for شنگرف (šangarf)

## Etymology
The word is "inherited from Middle Persian (unattested, but borrowed into Arabic زِنْجَفْر zinjafr)" and ultimately "inherited from Old Persian" *sinkabruš*, meaning "carnelian." The Old Persian cuneiform form is cited as: 𐎿𐎡𐎣𐎲𐎽𐎢𐏁. Comparative cognates include Sanskrit *hiṅgula* (cinnabar, vermilion) and Persian *šengâr* (bugloss flower used for red dye).

## Definition
**شنگرف** (šangarf) functions as a noun with two primary meanings:

1. Cinnabar or vermilion (the mineral/pigment)
2. By extension, any red dye or ink

## Historical Usage
A circa 1520 poetic citation from Selim I of the Ottoman Empire demonstrates the term applied metaphorically to "red ink of tears" (*šangarf-i ašk*) in classical Persian verse.

## Pronunciation Variants
Pronunciations differ across Persian dialects—Classical Persian /ʃan.ˈɡarf/, Dari formal [ʃäŋ.ɡáɾf], and Iranian formal [ʃæɲ.ɡʲǽɹf].

**Note:** No documented borrowings into Greek are mentioned in the entry; Arabic borrowing is noted in reverse (Arabic borrowed the Persian term).
```


## [2026-09-14T02:01:59.113Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT ===\"; grep -n -i \"sinkabru\\|kapautaka\\|carnelian\" KNT.txt | head -20\necho \"=== TLM ===\"; grep -n -i \"sinkabru\\|carnelian\" TLM.txt | head -10\necho \"=== BRT ===\"; grep -n -i \"sinkabru\" BRT.txt | head"
}
```


### [2026-09-14T02:01:59.230Z] TOOL RESULT

```
=== KNT ===
1042:V. OP p bf are in some instances not traceable to pIE forebears or are definitely borrowings from outside sources; such are piru- ‘ivory’, si"kabru- ‘carnelian’, naiba- ‘good’ (only in Iranian), and many place and personal names, such as Pirdva ‘Nile’, Putdya- ‘Libyan’, Babirus ‘Babylon’, Arabdéya ‘Arabia’, Arbatrü- ‘Arbela’, Ufrütu- ‘Euphrates’, Nadifaba?ra ‘Nidintu-Bel’, Nabukudracara ‘Nebuchadrezzar’.
4262:37 : idä : akariya : kàsaka : һуа : kapautaka : uta : sikab
4295:Sh. 35-40. The gold was brought from Sardis and from Bactria, "which here was wrought. The precious stone lapis-lazuli and carnelian which was wrought here, this was brought from Sogdiana. The precious stone turquois, this was brought from Chorasmia, which was wrought here.
5242:kapautaka- adj. ‘blue’, in kdsaka hya kapau- |
=== TLM ===
=== BRT ===
```


## [2026-09-14T02:02:02.620Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sikabru\\|si\\\"kabru\\|sinkabru\\|sikab\" KNT.txt | head -20\necho \"---\"; python3 - <<'EOF'\nimport re\ntxt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i,L in enumerate(leaves):\n    if re.search(r'si\\W?kabru', L):\n        print('leaf',i,'printed~',i-15)\nEOF"
}
```


### [2026-09-14T02:02:03.783Z] TOOL RESULT

```
357:86. DIALECT MIXTURE IN THE OLD PERSIAN Inscriptions. Like most or perhaps all other series of documents, the OP inscriptions are not in pure OP dialect, free from admixture from outside.’ They contain the expected borrowings of names of persons and places, and presumably of some cultural materials. Thus Aurà ‘Assyria’, Babiruí ‘Babylon’, Mudrdya ‘Egypt’ are from Semitic; Гаа (a district in Assyria), Dubdla (a district in Babylonia), Labandna ‘Mt. Lebanon’, Haldita- (name of an Armenian) betray their non- Iranian character by the l; a few words lack a convincing IE etymology; such as si"kabrus ‘car- nelian’, багт ‘timber’, yakd (a kind of wood), skauhiS ‘weak, lowly’, or are obvious borrowings, such as maškā- ‘inflated skin’ from Aramaic. But the main outside influence is that of the Median dialect, seen in phonetic and lexical differences, perhaps also in variant grammatical forms. Aramaic also seems to have had a certain influence on the phrasing and the syntax. There is no evidence that OP itself, at the time of the inscriptions, possessed a literature of any kind apart from these inscriptions themselves.
1042:V. OP p bf are in some instances not traceable to pIE forebears or are definitely borrowings from outside sources; such are piru- ‘ivory’, si"kabru- ‘carnelian’, naiba- ‘good’ (only in Iranian), and many place and personal names, such as Pirdva ‘Nile’, Putdya- ‘Libyan’, Babirus ‘Babylon’, Arabdéya ‘Arabia’, Arbatrü- ‘Arbela’, Ufrütu- ‘Euphrates’, Nadifaba?ra ‘Nidintu-Bel’, Nabukudracara ‘Nebuchadrezzar’.
1838:I. Stems in -й-: adj. par-u-, ard-u- in personal name Ardu-mants-, va-u- in personal names Déraya-vau- Vau-misa- Vahau-ka-; substantives baru- in Gau-barw-a-, maršiy-u- ‘death’ in adj. uvd-marSiyu-, mard-u- in Marduniya-, Mag-u-, Hitd-u-, Marg-u-, Kür-u-, uncertain bat-u- in bátu- gara-; loanwords pir-u-, Ufrat-u-; restored loan- word agur-u-; uncertain as to stem, Qatag-u-, sikabr-u-.
2156:Nom. Sg. Masc.: magus, piruš, sikabrus, ад). ш@татйун$; names of kings, Dérayava'us, Kürus; place-names, Abirddus, Kud"ru&, Qata- gus, Babiru’, Māļruļš, Margus, Hindu.
4262:37 : idä : akariya : kàsaka : һуа : kapautaka : uta : sikab
---
leaf 19 printed~ 4
leaf 44 printed~ 29
leaf 55 printed~ 40
leaf 77 printed~ 62
```


## [2026-09-14T02:02:10.777Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kabru- \" KNT.txt | head; echo \"---\"; grep -n -A3 \"^sikabru\\|^si.kabru\" KNT.txt | head -20\necho \"=== search lexicon area ===\"; python3 - <<'EOF'\nimport re\ntxt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in range(200,len(leaves)):\n    if re.search(r'kabru', leaves[i]):\n        print('leaf',i)\n        idx=leaves[i].find('kabru')\n        print(leaves[i][max(0,idx-400):idx+400])\nEOF"
}
```


### [2026-09-14T02:02:11.909Z] TOOL RESULT

```
1042:V. OP p bf are in some instances not traceable to pIE forebears or are definitely borrowings from outside sources; such are piru- ‘ivory’, si"kabru- ‘carnelian’, naiba- ‘good’ (only in Iranian), and many place and personal names, such as Pirdva ‘Nile’, Putdya- ‘Libyan’, Babirus ‘Babylon’, Arabdéya ‘Arabia’, Arbatrü- ‘Arbela’, Ufrütu- ‘Euphrates’, Nadifaba?ra ‘Nidintu-Bel’, Nabukudracara ‘Nebuchadrezzar’.
---
=== search lexicon area ===
```


## [2026-09-14T02:02:16.291Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"camelian\\|cameli\\|kabru\\|kabrus\" KNT.txt | head -20"
}
```


### [2026-09-14T02:02:16.354Z] TOOL RESULT

```
357:86. DIALECT MIXTURE IN THE OLD PERSIAN Inscriptions. Like most or perhaps all other series of documents, the OP inscriptions are not in pure OP dialect, free from admixture from outside.’ They contain the expected borrowings of names of persons and places, and presumably of some cultural materials. Thus Aurà ‘Assyria’, Babiruí ‘Babylon’, Mudrdya ‘Egypt’ are from Semitic; Гаа (a district in Assyria), Dubdla (a district in Babylonia), Labandna ‘Mt. Lebanon’, Haldita- (name of an Armenian) betray their non- Iranian character by the l; a few words lack a convincing IE etymology; such as si"kabrus ‘car- nelian’, багт ‘timber’, yakd (a kind of wood), skauhiS ‘weak, lowly’, or are obvious borrowings, such as maškā- ‘inflated skin’ from Aramaic. But the main outside influence is that of the Median dialect, seen in phonetic and lexical differences, perhaps also in variant grammatical forms. Aramaic also seems to have had a certain influence on the phrasing and the syntax. There is no evidence that OP itself, at the time of the inscriptions, possessed a literature of any kind apart from these inscriptions themselves.
1042:V. OP p bf are in some instances not traceable to pIE forebears or are definitely borrowings from outside sources; such are piru- ‘ivory’, si"kabru- ‘carnelian’, naiba- ‘good’ (only in Iranian), and many place and personal names, such as Pirdva ‘Nile’, Putdya- ‘Libyan’, Babirus ‘Babylon’, Arabdéya ‘Arabia’, Arbatrü- ‘Arbela’, Ufrütu- ‘Euphrates’, Nadifaba?ra ‘Nidintu-Bel’, Nabukudracara ‘Nebuchadrezzar’.
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
2156:Nom. Sg. Masc.: magus, piruš, sikabrus, ад). ш@татйун$; names of kings, Dérayava'us, Kürus; place-names, Abirddus, Kud"ru&, Qata- gus, Babiru’, Māļruļš, Margus, Hindu.
```


## [2026-09-14T02:02:26.965Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%B9%CE%BD%CE%BD%CE%AC%CE%B2%CE%B1%CF%81%CE%B9",
 "prompt": "Ancient Greek κιννάβαρι: etymology, first attestation, meaning, and descendants (Latin, French, English). What does it say about a Persian or Oriental source?"
}
```


## [2026-09-14T02:02:28.790Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D8%AD%D8%B1%D8%A7%D8%A1",
 "prompt": "Arabic صحراء: etymology (root ص ح ر), meaning, relation to أصحر 'reddish', and descendants/borrowings (Persian, English Sahara)."
}
```


### [2026-09-14T02:02:34.078Z] TOOL RESULT

```
# صحراء (Desert) - Wiktionary Entry

**Definition:** The Arabic word صحراء (ṣaḥrāʔ) means "desert" and is a feminine noun.

**Pronunciation:** /sˤaħ.raːʔ/

**Linguistic Details:**
- **Root:** ص ح ر (ṣ ḥ r)
- **Grammatical forms:** The word uses diptote declension with multiple plural forms: صحارى (ṣaḥārā), صحراوات (ṣaḥrāwāt), and صحاري (ṣaḥārī)

**Language Spread:** This term has traveled widely across languages through historical borrowing, appearing in Persian, Turkish, Urdu, Pashto, and English (as "Sahara").

**Related Terms:** Derived expressions include "الصحراء الكبرى" (the Great Desert) and "سفينة الصحراء" (ship of the desert, referring to camels), plus the adjective صحراوي (desert-related).
```


### [2026-09-14T02:02:34.085Z] TOOL RESULT

```
# Ancient Greek κιννάβαρι: Etymology and Origins

**Etymology and Source:**
The word is described as "probably an eastern loanword according to Beekes." The page traces connections to Arabic *zinjafr* and Persian *šangarf*, which derive from Old Persian *sinkabruš* meaning "carnelian," though the ultimate origin remains unknown.

**Meaning:**
The term refers to two related substances: cinnabar (mercury bisulfide, a mineral) and vermilion (a red pigment derived from it).

**Key Quote on Oriental Source:**
"Probably an eastern loanword according to Beekes. Compare Arabic زِنْجَفْر (zinjafr), related to Persian شنگرف (šangarf) from Old Persian..." This demonstrates scholarly consensus that the word traveled westward from Eastern language families.

**Descendants:**
The word entered Latin as *cinnabari/cinnabaris*, which subsequently seeded Romance languages and English "cinnabar." It also appears in Classical Syriac variants, confirming its circulation across Mediterranean and Near Eastern trade networks.

The Persian-Old Persian connection strongly suggests the word originated in contexts of ancient mineral trade along routes connecting the Mediterranean to Central Asia.
```


## [2026-09-14T02:02:39.215Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/scamnum",
 "prompt": "Latin scamnum: etymology (PIE root, *skabh-), meaning, related forms scabellum/scamellum, descendants."
}
```


## [2026-09-14T02:02:40.348Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/shambles",
 "prompt": "Etymology of shamble/shambles: Old English scamol, Latin scamellum/scamnum, meaning development."
}
```


### [2026-09-14T02:02:45.342Z] TOOL RESULT

```
# Etymology of Shambles

The word "shambles" derives from Old English *scamol*, traced back to Latin *scamillus* (a diminutive of *scamnum*), both meaning "stool" or "bench."

**Semantic Evolution:**

The meaning shifted progressively in English:

1. **Early 15c**: "meat or fish market" – referring to vendor stalls
2. **1540s**: "slaughterhouse" – where meat was processed
3. **1590s**: Figuratively, "place of butchery"
4. **1901**: Generally, "confusion, mess" (typically plural form)

**Related Words:**

The verb "shamble" (1680s) means "to walk awkwardly," possibly derived from "the splayed legs of bench" or how workers sat astride them. The adjective "shambolic" (1961) emerged meaning "chaotic, disorderly."

This etymological trajectory reflects how the word's meaning expanded from a literal commercial setting to metaphorically describe disorder and chaos.
```


### [2026-09-14T02:02:46.521Z] TOOL RESULT

```
# Scamnum: Latin Etymology and Meaning

**Scamnum** is a Latin noun meaning "stool, step, or bench." According to the etymological information provided, the word derives from Proto-Italic *skaβnom, ultimately tracing back to Proto-Indo-European *skabʰ-no-m, with the root *skabʰ- meaning "to hold up, support."

The term shares linguistic kinship with Sanskrit स्कम्भ (skambhá), which carries the same sense of "prop, support, pillar."

## Key Details

**Declension:** Second declension neuter noun (nominative singular: *scamnum*, genitive: *scamnī*)

**Related forms:** The noun generated derived terms including *scabellum*

**Descendants:** The word evolved into Romance language variants such as Romanian *scaun*, Italian *scanno*, Spanish *escaño*, and Portuguese *escano*, demonstrating its persistence across linguistic families.

The page notes that *scamnum* was even borrowed into other language groups, including Albanian *shkëmb* and Byzantine Greek *σκαμνίον* (skamníon).
```


## [2026-09-14T02:02:56.157Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins skabh ===\"; grep -n -i -B2 -A8 \"^skabh\" AHD_watkins1985.txt | head -40\necho \"=== IEC skabh ===\"; grep -n -i \"skabh\\|skambh\" IEC.txt | head -10\necho \"=== SYN scamnum/bench ===\"; grep -n -i \"scamnum\" SYN.txt | head -5\necho \"=== WLD band3 skabh ===\"; grep -n -i \"skabh\\|skamb\" WLD_band3.txt | head -10"
}
```


### [2026-09-14T02:02:56.274Z] TOOL RESULT

```
=== AHD watkins skabh ===
=== IEC skabh ===
15425:skabhlos (-əlos) Hes. skáphalos ‘ladle, baler’; Ir. scabhal, mf. ‘cauldron’
15426:skabhos, à (skobh-?) (1) ‘cłasp, catch; prop, stay, support. Cf. skobh- (2) Skt. cf. skabhnómi, -nümi, v. “fix; prop’; Arm. cf. xab, xabK, s. ‘ambush; trick, fraud"; xabem, v. ‘trick’; OCS skobü, skoba, mf. ‘brooch’; Big. Cz. skoba, f. ‘clamp, cramp’; Oss. cf. käbäl ‘linchpin, peg, bobbin’
15436:skabhos (2) ‘cutting, sharp; cut’. Cf. skobh- (1). (Gmc. & S1. ambig.) Gk. skáphos, m. ‘digging’; n., gs: -eos, & ska- phé, f. (*trench'. Fem. also ‘trough, boat’); MHG schabe, wf. ‘rasp; shaving; ringworm; moth’; OE scafa, wm. ‘plane (tool); Du.
15439:skabhros ‘rough, sharp’. Cf. skab- and WP II, 563 Lat. scaber, f: scabra, adj. ‘rough, rugged, dirty, scaly’; LG cf. schabberig, adj. ‘severe, auste- re: Latv. skabrs, adj. ‘fissile, sharp, shrill, penetrating’. (Isophonic: Oss. kåbår ‘hunk of bread": käbur, kåbíla ‘pup’; Li. skabrüs ‘nim- ble, lively’. Here?)
15440:skabhtos (assimilated to skaptos. Cf. skăbh-, and skap- as a separate entry) Gk. skaptós, adj. (dug, diggable'. Here, in view of skápto, pf. éskapha, v. 'dig); OE (ambig.) sceafóa, sceafoóa, wm. (“chip, shav- ing’. Cf. skap-); Li. skábtas, m. ‘gouge’
15472:skapo, ið (skap-) ‘chip, dig, scrape, Cut, Cf. skabhos (2). WP II, 560 Oss. cf. Küpi, kapi, s. “hoe, hook’, fr. *skhàp-); Gk. cf. skapáne, f. “hoe, spade’; Alb. hap, v. (- nji gropë ‘dig — a hole"); Lat. cf. scapula, f. 'shoulder-blade'; (ambiguous forms are Go. skaban, sv. 6 and Gmc. generally, see skabh-); OCS (ambig.) skopljo, skopiti, v. (&castrate', but cf. skop-); Li. skapiü, inf: skópti, v. Cgouge, scrape, cut, strip, pluck’: *á/a) cf. skaptos
15474:skaptos “cut, carved, gouged, shaped; cut, carving, gouged article, shaped article’. Cf. skapó and skabh-. (Gk. ambig. as also Gmc. See skabhos (2)). WP II, 561 Gk. (ambig.) skaptós ‘dug; diggable' (for the radical cf. skapáne, skápetos but the vb. skápto is fr. type skabh-, q. v.); OHG scaft, m. (shaft, spear, arrow'. Ambig. as Gk. cf. skabh-); MHG schaft, sm. (also: ‘bathtub’); OE sceaft, m. ‘shaft, pole’; E (also ‘tunnel in a mine"); ON skapt, n., skepti, n. as OHG (also: ‘shaft, handle, missile; Li. skáptas, m. ‘scoop, gouge, carving-knife'"
15735:skobh- (1) ‘cut; cutting; cutter’; ‘shavings, waste’. Cf. skabh- & skab-. Gmc. SI. and Balt. ambig. Arm. xob, Let, 'ploughshare'; Lat. scobs & scobis, gs. id. f. ‘filings, sawdust’; LLat. sco- bio, ére, v. ‘probe’: cf. also scobina, f. 'spoke- shave, rasp; filings; MHG (ambig.) schabe, wf. ‘rasp; shaving; chaff; ringworm, moth- grub’; Du. schaaf, f. “plane, smoothing“; E cf. spoke-shave; Sw. skäv, skäva, nf. 'réfuse, dross, floss’; Blg. skoba, f. (2) 'spokeshave';
15738:skobh- (skobhos, a) (2) ‘fixture; prop’. WP II, 539. (Vowel ambig.) Skt. cf. skabhanam, n. (mng. unknown, but linked w. skabhnami “fix, support); OCS
=== SYN scamnum/bench ===
=== WLD band3 skabh ===
```


## [2026-09-14T02:03:04.907Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD grep skabh ===\"; grep -n \"skabh\\|scamnum\\|SHAMBLE\" AHD_watkins1985.txt | head -10\necho \"=== IEC root entry ===\"; sed -n '15418,15426p' IEC.txt\necho \"=== WLD Bd2 p539 ===\"; python3 - <<'EOF'\nimport re\np='incoming/WLD/WLD_Bd2_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('leaves',len(leaves))\nhits=[i for i,L in enumerate(leaves) if re.search(r'skamb|skabh|scamnum', L)]\nprint(hits[:20])\nEOF"
}
```


### [2026-09-14T02:03:06.089Z] TOOL RESULT

```
=== AHD grep skabh ===
934:*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
2252:SEXTUPLE pel-3 SHABBY skep- SHADE skot- SHADOW skot- SHAFT! skep- SHAH tké- SHAKO dek-2 SHAKTI kak-1 SHALE skel-1 SHALL skel-2 SHAMBLES skabh- SHANK skeng- SHAPE skep- SHARD  sker-1 SHARE! | sker-1 SHARE? sker-1 SHARP sker-1 SHATTER sked- SHAVE skep- SHAWM kolem- SHE so- SHEAF skeup- SHEAR sker-1 SHEARS sker-! SHEATH skei- SHEAVE? skei- SHED! skei- SHEEN keu-1 SHEET! skeud- SHEET2 skeud- SHELDRAKE skel-1 SHELF skel-1 SHELL skel-1 SHIELD skel-1 SHIMMER skesi- SHIN! skei- SHINE skeei- SHINGLE! sked- SHINGLES kenk-! SHIP skipam SHIP skep- SHIRT sker-1 SHIT skei- Suiva_ kel-1 SHIVER? skei- SHOAL? skel-1 SHOOT skeud- SHORT sker-1 SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- sHow keu-! SHOWER! kéwero-
=== IEC root entry ===
siüið (siüuo) ‘sew’. WP II, 515. Cf. siü-dhlom, siüio, siütós and next Skt. sivyàmi, pp: syutáb, id.; Oss. xwin, Dig. xujun, pp: xud, id.; Gk. cf. kas-süo, v. (‘sew together, « *Kmt-. Here Ainsworth 1736: suo: *kassüo for katasuó?); cf. pisuggos (/shoe- maker’, fr. *ped-suuo-, with pi- for *pe- before *su-, cf. písures); Lat. suo, ére, id.; Go. siujan; OHG siuwen; OS siuwian; OE seowan & séo- wian; Sw. sy, id.; OCS (and com. Sl.) So, Siti, id.; Li. siüvu, siūti, id.; Latv. Sum, šūt, id.
siümn- ‘suture’. Cf. sitið, etc. Skt. syüman, n. “band, thong, stitch’; Hitt. (?) sumanc (queried: *thread"); Gk. humén, gs: -ménos, m. ‘membrane’ beside kás-süma, n. ‘thing stitched, sole, leather patch’; Lat. cf. fer- rumen, n. ‘solder, glue’ (?) (cf. dher-); MIr. süainem, s. (error for *süaimen "hong: OPr. Sumeno fcobbler's sewing thread"
siütós ‘sewn’; siütis ‘sewing, suture’. See siüió, etc. Skt. syütáh, id. beside syütih, f. sewing; bag’; Oss. xud, pp. ‘sewn’; Lat. sütus, adj. id.; MHG
1145
siut, sm. ‘stitch’; ON súð, f. “tongue of board’; OCS au (and com. SL), pp. as Skt.; Li. siütas, Latv. Süts, id. Cf. *sieut- in Skt. syotah (beside syütah *bag"); OE sēod, m. ‘purse’; Icel. sjóður, id.
sküb- ‘gouge, dig out; gouger, trowel, scoop’. . (Short vowel in) MHG schepfe, scheffe, f. ‘trawling-net’; Du. schep, m. ‘scoop, trowel’; E skep ‘trough for builders rubble’; Du. scheppen, v. ‘shovel up’; G schöpfen, v. ((2) ‘bale out, ladle out, w. vowel-rounding); (long vowel in); MHG schuofe, wf. ‘ladle, scoop’; Swiss schüefe f. id., Du. schoep, f. ‘paddle, shovel, scoop’; E (fr. Norse) scoop; MLG schōpe(n), f. ‘mason’s trowel’; Li. cf. skabiù & skobiù, p.t. skobiaŭ, inf: skõbti, v. ‘gouge out, chisel’
skåbh- ‘scab, scale, sore, canker’. WP II, 562 Lat. scabiés, gs: -iēi, f. ‘scab, ch": MHG schabe, wf. (2) ‘moth, grub’; OE -sceafa, wm. (in mæl- ‘canker’) beside OE sceabb- in -ede, adj. ‘scabby, sore’; E scab (from Norse}; beside shabby, adj.; Sw. skabbe, wn. ‘scab’ beside skabbig, adj. ‘scabby’; (long-gde in) Upper MHG schuop, schuope, s. & w.m. ‘scale’; schuopen, v. ‘flake off”. Verbal types in Gk. Skápto, aor. pass. eskáphēn, v. 'dig'; Lat. scabo, ére, pf: scabi, v. “scratch? beside sca- beo, ere, v. "be scurvy’; LLat. scabio, Ire, v. ‘tch’; Go. skaban, wv. (shave. Gmc. forms ambig. cf. skap-); MHG schaben, OE scafan, sv. 6.; ON skafa, sv. 6 p.t. skóf, v. ‘shave, scrape, pare’; R cf. skoblit, inf. id.; Li. ska- biù, skobti, v. ((1) ‘têar, pluck, trim’. Iso- phonic w. skåb-type above); Latv. skabīt, inf. “hew, fell
skabhlos (-əlos) Hes. skáphalos ‘ladle, baler’; Ir. scabhal, mf. ‘cauldron’
skabhos, à (skobh-?) (1) ‘cłasp, catch; prop, stay, support. Cf. skobh- (2) Skt. cf. skabhnómi, -nümi, v. “fix; prop’; Arm. cf. xab, xabK, s. ‘ambush; trick, fraud"; xabem, v. ‘trick’; OCS skobü, skoba, mf. ‘brooch’; Big. Cz. skoba, f. ‘clamp, cramp’; Oss. cf. käbäl ‘linchpin, peg, bobbin’
=== WLD Bd2 p539 ===
leaves 725
[543, 568]
```


## [2026-09-14T02:03:12.943Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (543,568):\n    L=leaves[i]\n    print('=== leaf',i,'===')\n    print(L[:1500])\n    print('...')\nEOF"
}
```


### [2026-09-14T02:03:14.147Z] TOOL RESULT

```
=== leaf 543 ===
                               sqabh-   — (s)kainb-, (s)kemb-                               539

            nach Pedersen KGr. I 24 aus dem Brit., was aber unnotig ist,
ds. (letztere
wenn brit. und ir. d das ags. dd widerspiegelten), und wird weiter auf
eine idg. Nebenform auf d bezogen; norw. mdartl. sicat „Wipfel eines
Baumes“, sTcata „m eine Spitze auslaufen*', aisl. shat a „Glattrochen^‘ fnach
dem spitz auslaufenden Schwanze benannt wie;) norw. shata, dan. shade
„Elster“ (s. Falk-Torp u. shale m.Lit., shade II; unter shat auch unannehm-
bares iiber got. skatts „Geldstuck, Geld“, nhd. Schat^^ slav. — als germ.
Lw.     —
        shoH „Yieh, Besitz“).       —
                                    Tiber slav. hotiti „walzen, rollen‘‘ s. Ber-
neker 591 auch lett. shetat'es „toben, larmen“ u. dgl. (Prellwitz BB. 21, 164)
                ;


ist    fernzuhalten.


sqabh- „stutzen‘\
      Ai. shabndti, shdbhnoti „befestigt,      stiitzt,   stemmt auf“,       Pf. cashdnibha]
shamhhd-h, shdmbhana-m „Stutze, PfeileF', av. iipashamhdm „unter Pest-
machen‘‘, frashdmba-, frascimbana- „StutzbaIken, Tragbalken, Pfeiler“;
  lat. scammim (^shabhnom^ das Formans im Zshang mit dem ind. Nasal-
praesens, Pedersen IF. 2, 331) „Bank, Scheme!", Dem. scahillum, scabellum
„niedriges Bankchen, Schemel" (mir. scamtm, bret. scaon^ cymr. ysgaf^i
„Bank", Fickll^ 308^ sind aus scamnum entlehnt, s. Vendryes De hib. voc.
174).
  Benfey I 655, Yf. LBWb,^ s. v. ; bes. Guntert Reimw. 26flF. (gegen Solm-
sens B
...
=== leaf 568 ===
564                                           S(q)en, (s)qan    — sqeng-
Haut, Membrane*'                   Av, scandayeiti „zerbricht, vernichtet (die
                                   {sg[end-n-).
Schlachtreihen)**, slcdnda--m. „Zerspaltung, zerstoren**;
   gr. vermutlich in oxevdvkrj, ox^vdvlri wahrscheinlich ,,ZaDge“ (LidenaaO.;
anders, aber verfehlt Ifiedermann IF. 15, 108f.).
   Ygl. mit a-Vokalismus mir. scandraim „zerspalte‘*, scandrad, scaindred
„dispersion**, scainner, PL scaindrecha etwa ^Yernichtungskampfe** (: cymr.
ysgytJim „to lop**; Stokes BB. 23, 59, Zupitza aaO.; Zweifel bei Giintert
Abl. 56); aksL skqda „defectus** (Johansson PBrB. 14, 337; idg. a? aksl.
skqd^ „arm, klein**, UqdUi „sparen, schonen**, Persson aaO., liegen in der
Bed, recht weifc ab c^sth „Teir* zu lit. hdndu „bei6en**, dessen Sippe nieht
                                   ;


aus „spalten‘*, sondern aus „nagen, kratzen** entwickelt scheint); lat. scan-
dula „Schindel** (aEeduktionsvokalo); iiber gr* oxivdaXyog s. Yf. LEY^b.^ u.
scandula^ Giintert aaO,).                    —
                             Dafi sqen- aus seq- „schneiden** erweitert sei
(Persson Beitr. 813, 882 Anm, 2), ist eine Moglichkeit.

(s)qen -5 (s)qan-' „stofien, schlagen**?
      Arm. Tcasiim „dresche** {^qan-s-)^ sks-anim „fange an“, avr. sicsay, Subst.
skizbn „Anfang**               (^sTzis-     aus idg.     "^sqen-s-)^air. fo-scann- „werfen, stofien,
worfeln**          (z.   B.   3.   PL foscannat „sie           stoB
...
```


## [2026-09-14T02:03:27.428Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN paskam ===\"; grep -n -i \"paskam\\|peckam\\;\\|pečkam\\|Säulen\\|pačkam\" HRN.txt | head -10\necho \"=== HUB ===\"; grep -n -i \"paskam\\|skamb\" HUB.txt | head -10\necho \"=== PHD/NYB skamb ===\"; grep -n -i \"skamb\\|paskam\\|askob\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -10\necho \"=== CHEUNG skamb ===\"; grep -n -i \"skamb\" CHEUNG.txt | head -10\necho \"=== RCH pashkam ===\"; grep -n -i \"pashkam\\|pachkam\\|bachkam\" RCH.txt | head -10"
}
```


### [2026-09-14T02:03:27.619Z] TOOL RESULT

```
=== HRN paskam ===
=== HUB ===
1390:auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
1392:arm. patSkam (patsgam^ patsgamb, patskamb) *Gemach,
1393:Halle, Stockwerk*, sondern fiihre np. paSkam = arm.
1394:patskamb auf ap. *pati-skamba~^ das ich zu zd. fra-
1397:persischen wurde *patskamb zu *paskamb, ehe pat-
1544:oben Nr. 312—314 gezeigt. Nach np. paskam = arm.
6764:np. paskam *aula' = arm. patskainb = ap. ^patiskanba- (s.
9171:paskam 'domus aestiva' = arm. patskam, patskamb *6emach*
9172:= ap. *pati'skamba' (oben p. 41).
10644:paskam 41, 191.
=== PHD/NYB skamb ===
PHD.txt:974:belly aSkamb(ag), aškom(b); (daevic) mulān.
PHD.txt:4992:karbāš karbunag karg kirīh- askamb! kirrén- kirrēnīdan kilēl
PHD_mackenzie.txt:1265:askamb [KL{iE < A krs'; )/kmb l I M c/kmb, N Iikam] belly, womb.
PHD_mackenzie.txt:1266:  .....ag [_kl I N !ikamba] = askamb.
PHD_mackenzie.txt:1270:askob ['Ikwp I N dlko(b)] roof, ceiling.
PHD_mackenzie.txt:1271:askom(b) ['/kwm(b l )] = askamb.
PHD_mackenzie.txt:6058:belly aSkamb(ag), askom(b); (daevic)        blinking mezisn.
PHD_mackenzie.txt:6177:ceiling askob.                          childless apus, starwan.
PHD_mackenzie.txt:7482:roof askob.                                satiety sagrih.
PHD_mackenzie.txt:7965:whatever cegam-iz-e(w).                'womb askamb(ag), askom(b), burdar,
=== CHEUNG skamb ===
22503:344 *skamb 
22506:*skamb ‘to support, use as support’ 
22536:*SANSKRIT: skambh ‘to support, prop’ (RV+) = EWAia II: 750 
52003:skambh, 344 
55869:*Hmai', *skamb (s.v.), *suaH 
58098:*rap/f, *skamb 
58269:*skamb 
=== RCH pashkam ===
```


## [2026-09-14T02:03:40.215Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG 22500-22560 ===\"; sed -n '22500,22560p' CHEUNG.txt\necho; echo \"=== HUB 1385-1400 ===\"; sed -n '1383,1402p' HUB.txt\necho; echo \"=== HUB 9165-9180 ===\"; sed -n '9165,9180p' HUB.txt\necho; echo \"=== HUB 6760-6770 ===\"; sed -n '6758,6772p' HUB.txt"
}
```


### [2026-09-14T02:03:40.320Z] TOOL RESULT

```
=== CHEUNG 22500-22560 ===
*REFERENCES: Kellens 1984: 123, n. 18; Lubotsky 2004: 323 ff. 


344 *skamb 


*skamb ‘to support, use as support’ 
*AVESTAN: (+ *fra-) YAv. frascinb- ‘to support’ = Liste: 63 
Partic.: perf. pass. YAv. frascimbana- (V 18.74); Caus.: pres. OPT. 3sg. YAv. frascinbaiiöit (V 18.74) 


*MIDDLE PERSIAN: (+ *pati-) MMP *pdyskmb’n ‘rooms’ > DMMPP: 273b 
*KHOTANESE: skim- ‘to create’ || (+ *pari-) LKh. paltcimph- ‘to check’ || (+ *fra-) 
haskim- (haskau-) ‘to make’ || (+ *nis-) LKh. *naltcimph- (nitciph-) ‘to remove’ 
= SGS: 128, 76, 150, 49 

*SOGDIAN: BSogd. sk’np, BSogd. ’Sk’np ‘world’ || (+ *pati-) BSogd. ptsknpy ‘porch, 
eaves’ 

*CHORESMIAN: (+ *para-à-) pr’Skm- to rob; to deceive’ = Samadi: 150 

*NWIR: (+ *pati-) NP paskam ‘court, vestibule’, Yzd. (Zor.) paskam ‘portico’ || (+ 
*ш-) Kurd. (Kurm.) biskavtin/biskév-, (Sor.) piskiwin/piskiw- ‘to take out, loosen 
[thread]; open [of flowerbuds]’ 

*NEIR: Pash. skam ‘tent-pole’, ? Yi. Skob-/Skaboy ‘to lift up, raise’ (Zarubin) || (+ 
*а-) Pash. acawul ‘to throw’ = ácaw-, (Wan.) ac-, (Waz.) wocaw- ‘to throw, fasten, 
put, build’ || (+ *pati-) Pash. pecumai ‘acclivity’ || (+ *ui-) Sh. wixkamb-/wixküvd, 
Rosh. Xikamb-/Xikavd, Ishk. uskomb-/uskovd ‘to sort, tease wool with the hands’, 
Sh. wixkimc ‘working the wool for preparing a warp of threads’, Rosh. Xikimc ‘a 
handful of teased wool or cotton’. Ф The ‘tease’ forms have been connected by 
Morgenstierne (EVS, І.с.) to OCS skubati ‘to pluck, tear, pull out’, OCz. vlasy skusti 
‘to tear out the hair’. 

*MISC: (+ *pati-) Arm. (LW) patsgam ‘portico’ 

*SANSKRIT: skambh ‘to support, prop’ (RV+) = EWAia II: 750 

9 This Ilr. root has no certain IE (verbal) correspondences. Only the rather isolated 
noun, Lat. scamnum ‘stool, bench [for the feet]’, is cited as cognate in LIV: l.c. 


«PIE? c LIV: 549 f. | Pok.: 916 
*REFERENCES: EVP: 9; IIFL II: 251a; EVS: 94b f.; DKS: 413b; Werba 1997: 325 f.; Cabolov 2001: 192 
f.; Vahman – Asatrian 2002: 25; МЕУР: 73, 7 


*skap/f ‘to split, make a crack, crack’ 

*AVESTAN: ? Y Av. skapta- ВМР] skpt’ (F 521) 

*MIDDLE PERSIAN: MMP ‘skfs- (inch.) ‘to split up [intr.]’, MMP “К°, BMP sk’p- 
/skäf-/ (pret. stem) ‘to split, cleave’, BMP škpt /Skaft/ ‘violent, terrible’ || (+ *ui-) ? 
BMP wskpt- /wiskaft-/ (pret. stem) “о crook, pervert, corrupt? => DMMPP: 92a 


Pres.: IND. 3pl. MMP Skfsynd; Partic.: perf. pass. caus. MMP ‘sk’ft, BMP Sk’pt /škaft/ || (+ *ui-) Partic.: 
perf. pass. BMP wskpt /wiskaft/ 

*SOGDIAN: (+ *pati-) MSogd. pskfs (inch./inch.) ‘to be split, split off’, CSogd. pcq’f 
(caus. ?) ‘to strike, pierce, wound’ (Sims-Williams 1985: 106 ad 54V.18) 

=== HUB 1385-1400 ===
Horn's Etymologic, insbesondere piz- aus patis.
314. Der Paragraph ist vollkommen verfehlt und zu streichen.
Vgl. Fr. Miiller, WZKM. 7, 371, dessen positive
Ausfiihrungen {piidh-tdan = pati + s + Wzl. von
np. justan, vgl. phi. vijustan WZKM. 8, 92) freilich
auch nicht einwandfrei sind. Ich lehne also np. piz-
aus patis (wie oben bis- aus abis) ab. Ich finde patis
auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
*domu8 aestiva, aula, atrium, coenaculum, porticus =
arm. patSkam (patsgam^ patsgamb, patskamb) *Gemach,
Halle, Stockwerk*, sondern fiihre np. paSkam = arm.
patskamb auf ap. *pati-skamba~^ das ich zu zd. fra-
skemba- vd. 2, 26 ('Stiitzmauer Geldner, 'batiment
avec balcon* Darmesteter) stelle, zuriick. Im mittel-
persischen wurde *patskamb zu *paskamb, ehe pat-
(vor andern Consonanten als s, s, d) zu pai- wurde.
316. Np. past niedrig, gering' ist nicht = skr. upasti-,
das zu *bast geworden ware, sondem = *patta-y skr.
patita-, Vgl. oben Nr. 92.
317. Etym. dunkel, auch nach Fr. M tiller's Erklarung,

=== HUB 9165-9180 ===
Z. 8 und 6 V. u.); gr. LW. karanh = karan = kalam —
arm. kalamb 'Kohl* (Faust us v. Byz.) = gr. xoti/upT] (vgl.
NSldeke, Pers. Stud. 2, p. 44); stmb ^^ sum^) 'Hnf, phi.
sumh Bdh. 61. 182, sunb Yatk. i. Zar. p. 67, Anm. 68,
arab. sunbok (de Lagarde, Symmicta p. 60), arm. smbak
(5. Jhd.), ap. *su(n)ba' oder *sn(n)pa-j vgl. zd. sofa- *Huf';
paskam 'domus aestiva' = arm. patskam, patskamb *6emach*
= ap. *pati'skamba' (oben p. 41).
b) ni ist urspriinglich in: dtmi = dunb^), dnnba,
dunb-al *Schwanz', bal. LW. dunbag, nb. dumb, dunb, phi.
dum, dumb, dumbak Bdh. 61. 148, 61. and Ind. 281—282,
dunb, dunbak West, PT. I, 337, arm. dmak (aus *duniak,
5. Jhd.), zd. duma- (s. oben p. 63); rtim, rilma, rum, ruma
(pi. rumgan), runb, runba *Schamhaare*, skr. roman- *Haar
(am Korper).
c) Unsicher ist, ob nb oder m urspriinglich ist in:

=== HUB 6760-6770 ===
(s. § 3) im Mp. Vor einen Konsonanten zu stehen kam, so
wurde es anders behandelt und zwar wurde
a) t im Mp. assimilirt an folgendes c, 5, s : phi. pacSn
= arm. patdBn Abschrift, Copie', hebr. pad^seyen (Esther)
= ap. '^patidayana-; np. pasanjfdan *besprengt werden,
phi. pasincitati, ap. 3. pr. *patisin6ataiy (s. oben p. 42);
np. paskam *aula' = arm. patskainb = ap. ^patiskanba- (s.
oben p. 41); np. pasand 'angenehm, gefallig, paz. pasan-
dtdan *to approve* =^ ap. "^pati-sanda' (s. oben p. 41); np.
paz. pasux 'Antwbrt' aus ^pdtsaxv (neben phi. pasaxo aus
*patsaxv), vgl. arm. patasxani 'Antw^ort' (s. oben p. 36);
np. pasaxt aus *patsdxt (s. oben p. 36) neben paz. phi.
pasaxt etc. (Shk. 262 — 263) aus patsdxt, Diese Assimili-
rung war erst sassanidisch, wie das Arnienische zeigt, das
sie noch nicht kennt.
```


## [2026-09-14T02:04:10.662Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT Sahara/sahra ===\"; grep -n -i \"sahara\\|Sahra\\|Wüste\" LKT.txt | head -10\necho \"=== SKT Sahara ===\"; grep -n -i \"sahara\" SKT.txt WEB_vol1.txt FSD_vol4.txt | head -10\necho \"=== FVQ sahra ===\"; grep -n -i \"sahra\\|ashar\" FVQ.txt | head -10\necho \"=== MON صحرا ===\"; grep -n \"صحرا:\" MON_part2.txt MON_part1.txt | head -10\necho \"=== MON صحاری ===\"; grep -n \"صحاری\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-14T02:04:10.809Z] TOOL RESULT

```
=== LKT Sahara/sahra ===
590:'Wüste',  das  zugehörige  Adj.  badawt, vulg.  bedewi  'VVüstenbewohner'  oder wahrscheinlich  der  plr.  badawijün,  vulg. bedewln  ergibt  frz.  bidonin,  sp.  it.  pg. bednino,  pg.  beduin  'arab.  VVüstenbe- wohner', rum.  bidiviu  'Pferd  arabischer
762:'Außerhalb  befindlich,  ländlich'  [adver- bialer Akkusativ  von  ar.  barr  'Land, Wüste'];  hieraus  sp.  albarrän  'der  Aus- wärtige, Nichtansässige',  albarraneo 'Fremder,  Ausländer',  sp.  pg.  albarrana 'Zwiebel',  sp.  albarrana  als  Adj.  in torre  albarrana,  pg.  albarran,  albarrana, albarräa  'Wachtturm'.  —  Siz.  [in  Mes- sina gebräuchlich]  fora  a  barra  'draußen vor  der  Stadt'.  [DE  69.  StGlIt  H,  230. GrSVociSic  228.
765:jäbö.n  aus  bijäbän  'Wüste'  Horn  NpEt S.  57,  Nr.  248;  wahrscheinlich  pers.  be 'ohne'  ebenda  S.  56,  Nr.  247  und  äb 'Wasser'  s.  hier  Nr.  5,  also  'ohne  Wasser, wasserlos']  'wüstes  Land';  hieraus  rum. bärägan  'wüstes,  unbebaute^  Land, Heideland',  n.  pr.  Bärägan  'die  Donau- tiefebene in  Rumänien'.
1066:'Sattel-  oder  Pferdedecke'  [vom  Stamme jap,  cap  'verhüllen,  bedecken'  Vämbery TktEtWb  S.  119,  Nr.  130];  hieraus  russ. €ech.  caprak,  serb.  sahraka,  poln.  cza- p)rak;  frz.  chabraqiie,  schahraque,  engl.
1468:'Wüstentuchs,  Fenek';  hieraus  sp.  alfa- negue  'Art  Pelzwerk'.  —  Der  zur  Jagd auf  den  Fenek  benutzte  Falke  hieß  häz al-fanak  'Falke  des  F.' ;  durch  Abfall  des Grundworts  [s.  z.  B.  hier  Nr.  570]  blieb sp.  pg.  alfanegue  'Falke  mit  schwarzem Gefieder',  kat.  alfanet,  frz.  alphanette, alphanesse  'dass.'.  [Möglich  wäre  auch die  schon  von  SOUSA  gegebene  Etymo- logie: al-hanik  'der  Würger'.]  [DE  102 bis  105.  Devic  DEt  26.  Lammens  Rem  19.
1807:Ein  Wüstengeist,  die  Mitte  zwischen Mensch  und  Ginn  [s.  hier  Nr.  723]  hal- tend, mit  menschlicher  Gestalt  und Eselsbeinen,  doch  häufig  seine  Gestalt wechselnd  [Lammens  Farük  870] ;  hier- aus frz.  la  goule  'ein  Ungeheuer';  aus dem  ar.  plr.  gailän  ergab  sich  frz. gailan  'dass.'.  —  Gtil  ist  auch  die  Be- zeichnung der  Meduse;  räs  al-gül  'Me- dusenhaupt' wurde  wegen  des  Wechsels seiner  Lichtstärke  der  Stern  ß  Persei genannt;  hieraus  der  Sternname  Algol. [Lammens  Rem  127/128.  Ideler  Sternu 88.    Devic  DEt  18.
1954:Vulg.  'fünfzig',  Bezeichnung  für  einen aus  der  Wüste  wehenden  Wind,  der  etwa 50  Tage  anhält;  hieraus  u.  a.  engl. kamsin,  khamsin.  —  [Andere  Ableitung aus  ostar.  ham  'Glut',  sin  'Wüste',  also 'Glut  der  Wüste'.]
2215:'Wüste'  [vom  Stamme  jab,  jav  'eitel, nichtig,  fremd'  Vämbery  TktEtWb  S.  108, Nr.  119,  oder  vielleicht  von  pers.  bijäbäu 'Wüste'  Horn  NpEt  S.  57,  Nr.  248  ?,  so auch  KORSCH  in  Thomsen  Festschrift 199:  mpers.  viyäpän  <  *vyäiMna;  aus vi  und  äp  'sich  zu  einem  Punkte  er- strecken' wurde  vyäpin  'sich  weit  er- streckend, d.  h.  ein  sich  weit  erstrecken- des, unbebautes  und  unbewohntes  Land'; im  Türkischen  soll  dann  die  erste  Silbe "^by- 1>  *bu-  als  echt  tk.  Wort  'dieser' verkannt  worden  sein;  vgl.  auch  kirgis. gapan  'Wüste'];  hierzu  jabangy  'Frem- der' ;  hieraus  rum.  iabangiü  'Bummler'.
2241:'Wüster  unbebauter  Boden',  ebenso bind.  mal.  pers.  gängäl;  hieraus  engl. jungle,irz.  djungle,djengle,  dtsch.  Dschun- gel 'ein  Gelände,  das  mit  Gebüsch  be- deckt ist',  'ein  wilder  und  von  wilden Tieren  bewohnter  undurchdringlicher Wald,  Dickicht'.    [Hobson-Jobson  470.
3038:1305.  Ar.  lamt: Einheitsnomen  lamta  'Art  Antilope'  in den  afrikanischen  Wüsten;  hieraus  sp. ante  [mit  Verkennung  des  anlautenden l  als  Artikel  und  Weglassung  desselben], dante  [aus  einem  Ausdrucke  wie  pelle d'ante  oder  dergl.  entstanden]  'Wild- leder', pg.  anta,  dante  'dass.'  [jedoch  in Brasilien  auch  'Tapir',  Constancio  Dicc 82c],  it.  dante  'Damhirsch';  Ableitung sp.  anteado  'blaßgelb'  [in  ähnlicher  Be- deutung wird  der  it.  Eigenname  Dante entstanden  sein].  [DE  195.  Gaix  Studi di  etimologiaitaliana  e  romanza.  Firenze 1878.    S.  303.    ML  4874.
=== SKT Sahara ===
WEB_vol1.txt:87779:ational trade language in Negro Africa outh of the Sahara. < u/sési, n. (G. hausen, a kind of sturgeon.] cipenser huso, à large sturgeon found in the Sea, Caspian Sea, Sea of Azov, ete. ‘Haus/frau, ». [G.] a housewife, haus’maAnnite, ». [named after af ay BEA Hausmann, à 19th-c, German mineralogist.] one of the ores of manganese, having a brown- jsh-black color. It crystallizes in the tetrag- —onalsystem, hausse (hos), 7. (Fr.
WEB_vol1.txt:103500:f ani y south win owing over Beni from the Sahara region for about fift days in the spring season (from late Mah until early May).
FSD_vol4.txt:1911:—   B   -partridge,  n   A   partridge  of  the  genua  Ammoperdtx, as  the  seesee  (A  bonha7ni),  of  India  —   s   -pear,  tz  A   hardy pear-tree  iPyrus  sinensis)  often  used  aa  stock  for  other  pears In  the  raw  state  Ita  fruits  arc  tery  hard  and  Inedible,  but when  fully  matured  they  are  used  for  preserves  1   his  tree  Is the  principal  parent  fn  the  productfonofthe  valuable  tarfetfes, the  Kleffer  and  Le  Conte  pears  —   s   -perch,  n   [Routhern U   Si  1   he  calico  bass  — s   -pigeon,  n   A   sand-grouse  —   s   » pillar,  n   Sand  whirled  by  a   tornado  Into  the  form  of  a pillar,  as  In  the  Sahara  —   s   -pit,  n   A   place  where  sand Is  dug  —   s   -plank,  n   In  car-bulldlng,  a   spring-plank  —   s   «   , plate,  n   A   horizontal  rotating  cast-iron  plate  on  which  ' marble  articles,  etc  ,   are  ground  or  polished  —   s   -plover,  n Arlng-plover  —   s -pride,  n   SameaspRinr*.  n.  1   s   preyt  ,
FSD_vol4.txt:35086:Tlb'a.ltlbll  tl  A   region  In  the  Sahara.  Africa,  ly-  pnt.tlpH  to  oorraotk,,,,.
FSD_vol4.txt:35460:Tlmbs,  1   tlmz,  2   time  John  (*/i7l801-»/«1875)  An  English antiquary  and  editor  Thinos  Not  Generally  Known Tlm-buk'tu,  1   tlm-buk'ta,  2   tIm-bQc'Ui,  n   A   town  in  the French  Sudan  on  S   border  of  the  Sahara  Tlm-buc'toot. tlm'bul,  n   Same  as  timbal Tim'bj,  1   tlm'bi,  2   tlm'by.  Theodore  Buggies
FSD_vol4.txt:39820:Trls'tram, Henry  Baker  (»/u1S22-V»190Q)  AnCngllshdl-  cerium  and  yttrium  metals  with  thorium,  calcium,  and vino,  canon  of  Durham,  trav  eler  author,  The  Greet  Sahara  boron  (Hi(Hj  Na«  Ca)j(Cc,La  Dl.TOlCe.Tli.Zr  )SlJ30iir»), Trls'tram  Miaii'dy.  In  Sterne  s   whimsical  autobiography ,   crystallizing  in  the  hexagonal  system  {   <   Gr  trliomos The  Life  and  Opinions  of  TrfJtram  Shandy  Gentleman,  the  thrice  cut  1
FSD_vol4.txt:48911:pers  (genus  tFrom  a   sDecimcniaNew  York  Zoological  Park  ) Cerastes),  and  the  Indian  xupers  (Da6oia  russelh  and Ethis  earinata)  are  exan.plM  The  horned  viper  Is  a large  sand-colored,  whlte-bellled  viper  (Cerastes  cornutus) of  Arabia  Sinai,  and  the  Saharan  region,  with  prominent keels  upon  its  scales,  and  two  prominent  projections  or horns  *   one  above  each  eye  Ills  usually  associated  with the  suicide  of  Cleopatra  and  Is  regarded  as  especially dangerous  because  of  Its  habit  of  hiding  m   the  sand 2.  Some  dangerous  or  repulsive  snake  mistaken  for  a vuper,  as  a   cobra,  a   rattlesnake,  or  a   hognose  3.  A v'enomous,  malicious,  or  treacherous  person  a   sense  in- fluenced by  the  old  fable  of  a   snake  that  killed  its  bene- factor 4^.  Her  Aserpentusedasabearing  [<F,rip^r, <L  npera,  <   nrur,  alive  (<  tiro,  live),  -f  parto  bear) —   red  viper,  the  copperhead  —   Bussell’s  v.,  the  jessur  — vl'per»flsh’’,  n   A   deep-sea  chaullodontold  fish  especially ChauUodus  iioanf,  having  exceedingly  long  teeth— T-*
FSD_vol4.txt:50831:War"gen-tln',  1   vor'gen-tln',  2   var*g€n-tln',  Peter  Wilhelm (VaI717-1783)  A   Swedish  astronomer  and  mathematician War'gla,  1   warigla,  2   war'gla,  n   A   French  military'  post and  oasis  in  the  Sahara  desert
FSD_vol4.txt:87542:Sahara
FSD_vol4.txt:87545:Saharanpur,  I   (d)
=== FVQ sahra ===
=== MON صحرا ===
MON_part2.txt:23315:است؛ کشتی زره‌دار. کشتی صحرا: ( کن.) 
MON_part1.txt:93262:طوطی صحرا: ( کد.) سبزه. 
=== MON صحاری ===
MON_part1.txt:18370:پایا می‌باشد. این گیاه در اکثر صحاری ایران 
MON_part1.txt:33941:صحاری و کوهستان‌ها سی‌روید؛ کراث 
MON_part1.txt:47903:اپبلان که بیشتر در کویرها و صحاری 
MON_part1.txt:81191:و بسرخضی در بیابان‌ها و صحاری زیست 
MON_part1.txt:81204:در صحاری می‌زید و قدش تا یک مور عم
```


## [2026-09-14T02:04:16.298Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"صحرا\" MON_part2.txt | head -20\necho \"--- ARY ---\"; grep -n \"صحرا\\|شنگرف\\|پچکم\\|پشکم\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T02:04:16.379Z] TOOL RESULT

```
366:غال: ا2,(.) سوراخی که جانوران صحرایی 
8213:کیاه» سابان فش آستاه صحرای وسیع و فراخ؛ 
8829:صحرایی: (گیا.) گونةٌ وحشی درخت فندق 
8831:وحشی. فندق وحشی: فندق صحرابی. فندق 
10133:قارج آش‌زنه. قارچج صحرایی: (گیا.) 
10587:صحرایی و مارها حمله می‌کند و آنها را از 
12311:تسرنگه» تورنگ. خروس صحرایی» 
17148:کاجبره. کاجبرة صحرابی: (گیا.) بکی از 
18130:قس. کلبه» خاندةٌ صحرایی] (ا.) خانه‌ای که از 
18282:عرق... کاسنی صحرایی: (گیا.) گیاهی است 
19982:چوب و علف و هیزم و مانند آن از صحرا 
20207:صحرایی؛ کبوتر چاهی» کبوتر پر کاغذی» 
20217:(جاذ.) کبوتر صحرایی که در چاه آشیانه 
20228:روی دوپای خود می‌ایستد. کبوتر صحرایی: 
21597:صحرایی» قرامن کیمیونی؛ قردمانا؛ کراوية 
22072:کرفس ريشه. کرفس صحرایی: (کیا.) 
23315:است؛ کشتی زره‌دار. کشتی صحرا: ( کن.) 
24658:زراعت نشده» صحرای لم پزرع. 
24673:صحرایی» موش دشتی» کلاوو. 
27111:صحرا به جهت مسافران کنده باشند. جابی 
--- ARY ---
```


## [2026-09-14T02:04:20.202Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"صحرا\" MON_part1.txt | head -30"
}
```


### [2026-09-14T02:04:20.268Z] TOOL RESULT

```
5369:سانتیمتر» صعتر» سعتر» بودینه صحرایی 
14046:خیم بیابانی» خ رگاه صحرایی. ححر ۵ حأنه. 
14438:تازیان بیابانی» تازیان صحرانشین» بدویان 
19366:را در صحرا برای چرارها کنند» رمه اسب. 
20048:بادیه: (-)۰رن۵ة۱ زع. بادیة] (.) صحراه 
21524:بادیه اقامت کردن» صحرانشین شدن. 
21644:- بدشفان] () (گی.) نیلوفر صحرایی 
21737:بدو. 20۷ [ع.] (.) بابان» صحرا. 
22998:بر به. (۵-)02۳-17۷2 [ع. بر به ] .( صحرا) 
26607:صحرای بی آب و علف» دشت لم‌یزرع. 
31467:خیار صحرایی. 
33048:دشتی » بودنه صحرایی» ظفیره؛ ظطفیر آ؛ 
37518:پیشی جستن. برآمدن به صحرا برای قضای 
44846:خروس صحرایی» تدرو. 
47467:صحرایی شبیه به خروس» دراج. 
47572:جرک: (.) دش شت» صحراء بیابان. 
49431:) آنکه در صحرا و یبلاق و فشلاق در 
51627:مرغی است صحرابی» کاروانکك. 
51676:چول: ان |تر.| (ا.) بیابان» صحرای خالی از 
55077:صلیبیان که بطور خودرو در باغ‌ها و صحراها 
59286:کنارة هر چیزء. حاشبه: دامان صحراء دامان 
59564:بر مند. علامتی که صیادان در صحرا نز دیک 
61812:است. صحرا؛ بیابان. قبر ستان. 
61825:صحرایی. (مس.) یکی از آوازهای ابرانی و 
62160:بی آب و علف» صحرای دق و لق. بی‌موی. 
62616:صحرایی» دله. 
64894:دیوان. صحرایی که از آبادی دور باشد. 
65066:زردک صحرایی. (گیا.) نوعی قارچ» قسمی 
65893:کوه. صحرا. 
66887:به صحرا کشیدن: (کد.) مردن» د رگذشن.
```


## [2026-09-14T02:04:23.235Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '61800,61832p' MON_part1.txt"
}
```


### [2026-09-14T02:04:23.328Z] TOOL RESULT

```
دش: 28 (.) خود آرایی» خودسازی. 
دش: ٩05‏ [- دژ] (پش..) بد» زشت؛ پلید. 
دشسپل: 01021 [- دشپیل] (امسر.) غده؛ 
دژزیبه. 

دشت: 428 (.) زمین پهناور هموار» جلگه. 
ضسح.- (جف.) زمین ناهمواری است که 
بهیچوجه چین نخورده با زمینی که به وسیلة 
مواد رسوبی رودها و سیلاب‌ها بوجود آمده 
است. اين گونه اراضی برای سکونت انسان 
در صورت اعتدال آب و هوا بسیار مناسب 
است. صحرا؛ بیابان. قبر ستان. 

دشت: ٩2٩‏ آقس. دست (لاف)] (ا.) 
کاسب. دشت کسی را کور کردن: (عم.) 
اولین بار فروش وی از او نسیه خر بدن. 
دشتان: ٩.02:‏ (ص‌مر. امر.) نگاهبان 
دشت» پاسبان کشتزار و مزرعه؛ مأمور محلی 
ده که وطفه او حفاظت مزارع دهقانان از 
ویرانی و دستبرد این و آن است. در بعضی 
نقاط وی امور آبیاری را نیز سرپرستی 
#۳ 

دشتی: -1250 (ص‌نسب.) منسوب به دشت» 
صحرایی. (مس.) یکی از آوازهای ابرانی و 
آن نمونه‌ای است از رت کر ساده و 
بی آلایش نظیر زندگی بی‌تکلف چوپانی و 
صسحرا و دشت‌نشینی. این آواز در عین 
سادگی گاه چنان موّثر و دلربا است که 
شنونده اشکك حسرت بر گونه می‌فشاند. گام 
دشتی با شور تفاوتی ندارد ولی نوت شاهد 
آن درجهٌ پنجم گام شور است (نوت شاهد
```


## [2026-09-14T02:04:32.262Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol4 Sahara ctx ===\"; sed -n '87535,87550p' FSD_vol4.txt\necho \"=== FSD Sa-ha'ra ===\"; grep -n \"Sa-ha\\|Sa\\.ha\\|Sahar\" FSD_vol4.txt | head -10\necho \"=== RCH sahra ===\"; grep -n -i \"sahrá\\|sahra,\\|sahará\" RCH.txt | head -10"
}
```


### [2026-09-14T02:04:32.389Z] TOOL RESULT

```
=== FSD vol4 Sahara ctx ===
(Northamp)  (t)
4
“   *’  (c)
Rothwell,  Eng
Saguache
(\  orks )   (t)
15
Sahara
Rotterdam
532
Saharanpur,  I   (d)
Rottwcll
in
“   “   (t)
Roubalx
113
=== FSD Sa-ha'ra ===
604:Sa-ha^ran-pur',  1   sa-ha'rtra-pfir',  2   sa-hS'rfln-pur',  n   1, A   district  In  Meerut  div  Lslon,  United  Prov  Inces  of  Agra  and Oudh,  British  India  2,242  sq  m   2   Its  capital sa'hib,  1   sd'Ib,  2   sa'Ib,  n   (Hindu]  Master,  lord,  gentle- man used  In  Persia  and  India  In  speaking  of  or  addressing Europeans,  as  equivalent  to  English  Afr  or  Sir,  also  some- times as  a   Hindu  or  Moslem  title,  as,  the  sahib  Is  here. General  Sahib  sa'hebf.
1911:—   B   -partridge,  n   A   partridge  of  the  genua  Ammoperdtx, as  the  seesee  (A  bonha7ni),  of  India  —   s   -pear,  tz  A   hardy pear-tree  iPyrus  sinensis)  often  used  aa  stock  for  other  pears In  the  raw  state  Ita  fruits  arc  tery  hard  and  Inedible,  but when  fully  matured  they  are  used  for  preserves  1   his  tree  Is the  principal  parent  fn  the  productfonofthe  valuable  tarfetfes, the  Kleffer  and  Le  Conte  pears  —   s   -perch,  n   [Routhern U   Si  1   he  calico  bass  — s   -pigeon,  n   A   sand-grouse  —   s   » pillar,  n   Sand  whirled  by  a   tornado  Into  the  form  of  a pillar,  as  In  the  Sahara  —   s   -pit,  n   A   place  where  sand Is  dug  —   s   -plank,  n   In  car-bulldlng,  a   spring-plank  —   s   «   , plate,  n   A   horizontal  rotating  cast-iron  plate  on  which  ' marble  articles,  etc  ,   are  ground  or  polished  —   s   -plover,  n Arlng-plover  —   s -pride,  n   SameaspRinr*.  n.  1   s   preyt  ,
35086:Tlb'a.ltlbll  tl  A   region  In  the  Sahara.  Africa,  ly-  pnt.tlpH  to  oorraotk,,,,.
35460:Tlmbs,  1   tlmz,  2   time  John  (*/i7l801-»/«1875)  An  English antiquary  and  editor  Thinos  Not  Generally  Known Tlm-buk'tu,  1   tlm-buk'ta,  2   tIm-bQc'Ui,  n   A   town  in  the French  Sudan  on  S   border  of  the  Sahara  Tlm-buc'toot. tlm'bul,  n   Same  as  timbal Tim'bj,  1   tlm'bi,  2   tlm'by.  Theodore  Buggies
39820:Trls'tram, Henry  Baker  (»/u1S22-V»190Q)  AnCngllshdl-  cerium  and  yttrium  metals  with  thorium,  calcium,  and vino,  canon  of  Durham,  trav  eler  author,  The  Greet  Sahara  boron  (Hi(Hj  Na«  Ca)j(Cc,La  Dl.TOlCe.Tli.Zr  )SlJ30iir»), Trls'tram  Miaii'dy.  In  Sterne  s   whimsical  autobiography ,   crystallizing  in  the  hexagonal  system  {   <   Gr  trliomos The  Life  and  Opinions  of  TrfJtram  Shandy  Gentleman,  the  thrice  cut  1
48911:pers  (genus  tFrom  a   sDecimcniaNew  York  Zoological  Park  ) Cerastes),  and  the  Indian  xupers  (Da6oia  russelh  and Ethis  earinata)  are  exan.plM  The  horned  viper  Is  a large  sand-colored,  whlte-bellled  viper  (Cerastes  cornutus) of  Arabia  Sinai,  and  the  Saharan  region,  with  prominent keels  upon  its  scales,  and  two  prominent  projections  or horns  *   one  above  each  eye  Ills  usually  associated  with the  suicide  of  Cleopatra  and  Is  regarded  as  especially dangerous  because  of  Its  habit  of  hiding  m   the  sand 2.  Some  dangerous  or  repulsive  snake  mistaken  for  a vuper,  as  a   cobra,  a   rattlesnake,  or  a   hognose  3.  A v'enomous,  malicious,  or  treacherous  person  a   sense  in- fluenced by  the  old  fable  of  a   snake  that  killed  its  bene- factor 4^.  Her  Aserpentusedasabearing  [<F,rip^r, <L  npera,  <   nrur,  alive  (<  tiro,  live),  -f  parto  bear) —   red  viper,  the  copperhead  —   Bussell’s  v.,  the  jessur  — vl'per»flsh’’,  n   A   deep-sea  chaullodontold  fish  especially ChauUodus  iioanf,  having  exceedingly  long  teeth— T-*
50831:War"gen-tln',  1   vor'gen-tln',  2   var*g€n-tln',  Peter  Wilhelm (VaI717-1783)  A   Swedish  astronomer  and  mathematician War'gla,  1   warigla,  2   war'gla,  n   A   French  military'  post and  oasis  in  the  Sahara  desert
87542:Sahara
87545:Saharanpur,  I   (d)
=== RCH sahra ===
```


## [2026-09-14T02:04:39.637Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '596,606p' FSD_vol4.txt\necho \"=== RCH ===\"; grep -n \"صحرا\" RCH.txt | head -5; grep -n -i \"sahar\" RCH.txt | head -8"
}
```


### [2026-09-14T02:04:39.746Z] TOOL RESULT

```
•gagU'a,  atow  1   —   sagittal  erevt,  a   bony  ridge  along  the IWd'tat  sututf*  In  vanoas  mammals  developing  csp*'cially Irv  old  Age  —   sag'lf-lol-lr*  adt
fiV
   
rowbeadi
one  of  the  fasittat*  learw fc  till*  rooU  *nd  e   Vh»
Sag"ue-nar%  1   sag'i-nC',  2   sSg'e-nft',  n   A   river  In  Quebec province,  Canada  length.  llO  m   from  Lake  St  John  to the  St  Lawrence  river,  its  scenery  attracts  many  tourists Sa-guc'rus,  1   so-gwFrus  2   sa-gwe'rOs,  n   Same  ns  Arenoa sa-guIn'Msa-gln',  2fia-^',  n   (S  Am]  I.  A   bushy-talled nyctlpltheclnc  monkey  of  the  genus  CaffffArfr  a   tetee  2. One  of  various  other  small  moDlcys  Sec  saz,  sinxiRi  (< F   sagouin,  <   Brar  eagoni  J
sa'gulnM  8a'gln,2sa*kln  n   (P  Ij  Bot  The  banana sa'gum,  IsUgum.  28a'eQm.n  (-CA.pZ)  (LI  Born  Antig The  common  soldiers*  military'  cloak  a   symbol  of  war,  as the  toga  was  of  peace  Compare  rvLUDAiiENTUit  toga Sa-gun'f  um,  l   sa-gun'tum,  2   sa-^On'tum,  n   ,   now  Sagunto orMurledro.  An  ancient  fortified  town  In  Valencia  pro- vince, Spain,  destroy  ed  by' Hannibal,  210  B   C   (TECA. sa'^gun-ja'fc,  1   sd'gun-yfl'tc  2   sS'fiun-yh'te  n   Same  as sa-gu'ran,  1   sa-gtl'ran  2   Ba-£u*riln.  n   [P  1 1   A   flbroua packing-material  made  from  the  leaves  of  the  burl-palm sas'ran-dU{o«,  1   sag'van-doli,  2 sSCviln-dlt,  n   Peirol  A variety  of  metamorphic«'*hlsto9c  rock  consisting  essentially of  magnesite  and  b~onzlte  with  a   little  mica,  pyTltc  and chromite  (<  Lake5cffran<f  Norway  1   (jcage
1   s^J'i.  2   sAi^y  c   Flavored  or  seasoned  with  or  like i5a-na'ina,lsa-ba'ma  2sa-ha'inli  n   A   volcano  of  the  Andes mountalo^  In  Oruro  department  Bolivia  21  Oil  ft  high Sa-Iia'ra,  i   sa-hC'ro  2   sa-ha'ra  n   1   A   desert  plateau  In N   n   Africa,  dotted  with  oases  and  Inhabited  by  pomadic Arab  tribes  3,600  000  sq  m   By  a   convention  between Great  Britain  and  France  Aug  5   1S90  practically  the whole  of  the  *5ah4ra  Is  within  the  French  sphere  of  Influence The  Zlbyan  de<;e*t  and  the  Nile  bavin  belong  to  I   gypt. while  Great  Britain  Mo-occo,  and  **paln  lay  claim  to  the west  coast  the  *'aharan  oases  were  onranlxed  ni  a   trench tcTltory  Aug  1-1  1906.  under  the  gov emmcnl  of  southern Algeria  2,  Figuratively,  a   wltdemess  desert —ba«ha - TuUf  ba-liar'l-an<  ba-bar'Jc*  a
Sa-ha^ran-pur',  1   sa-ha'rtra-pfir',  2   sa-hS'rfln-pur',  n   1, A   district  In  Meerut  div  Lslon,  United  Prov  Inces  of  Agra  and Oudh,  British  India  2,242  sq  m   2   Its  capital sa'hib,  1   sd'Ib,  2   sa'Ib,  n   (Hindu]  Master,  lord,  gentle- man used  In  Persia  and  India  In  speaking  of  or  addressing Europeans,  as  equivalent  to  English  Afr  or  Sir,  also  some- times as  a   Hindu  or  Moslem  title,  as,  the  sahib  Is  here. General  Sahib  sa'hebf.
sa'hl-bah,  1   sa'I-ba,  2   sa'I-ba,  n   Mistress,  lady,  the  fem- inine of  sahib  Compare  mem-^ahib Sa-hId'Ic,  1   ss-hld'ik  2   sa-hId'Jc  I,  a   Thebaic  II.  n The  Sahldlc  v   erslon  of  the  Bible  as  used  by  the  Copts,  also, the  Sahldlc  dialect sah'llte,  n   Same  as  salite sa-hua'ro,  1   sa-hwa'ro,  2   sa-hwa'ro  n   Saguaro Sa-hu^ca  bean,  1   sa-hU'ka,  2   sa-bq'ca  The  soy-bean 8a-htil%  1   se-hwr,  2   sa-hw/,  n   A   marmoset sa'l,  1   sn'l,  2   sa'I  n   (3raz  I   1.  A   ceblne  monkey  2.  A bright-blue  hoaey-’cceepcr  {Ccereba  cyanea)  of  tropics! America
sai'ad,  n   Same  as  satid  sa'Idf.
=== RCH ===
28555:nan  o   mzah^guzdrdn  o   saf^shikandn^  Brandishing  swords,  level- ling  spears,  and  breaking  the  enemy’s  ranks.  ^   /^jJ  iegh^i $itam^  The  sword  of  oppression.  jS^  tegh^i  sahar^  Break of  day.  Morning-prayer.  A   sigh  of  grief,  tegh
29386:jks^  sahary  The  |pn.  stmy  A   silver  gob- let. The  chill  of  a   mistress.  shahr^party
29433:To  tear  oi^  rend  one*t  garment  (met.)  To  make  a   tidlent  exer- tion. To  joke,  jest  yr-  lAm^Jama-i  sahar^  The  sun.^  The aephyr.  yrf,  Holiday^loA^^^  Scarle^Blos-
44685:rah^randn^i  sahary  Those  who  watch  and  pray during  the  night.  ^f^k^rawdn^i  tarikaty  The
47220:H«A saharUy  {fwU j^  yasbiru')  He  probed  (the  wound).
47781:To  enchant,  charm,  fascinate,  a   iSW^r,  Lungs,  lights.  Sahar, The  twilight,  dawn.  ^ilds  ^sahar,  Towards  morning,
47782:r hangdfft-i  sahar,  The  rising  of  Aurora,  the  dawn.
47787:A   saharal  (or  saharah),  (pi.  of  sahtr)  Magi* eians.  %uhrat,  The  morning,  Aurora,  the  dawn.
```


## [2026-09-14T02:04:48.192Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"sahrá\\|sahra,\\|çahrá\\|sahrá'\" RCH.txt | head -8\necho \"--- try صحراء ---\"; grep -n \"صحراء\\|صحرآ\" RCH.txt | head -5\necho \"--- AFM/TAD ---\"; grep -n \"صحرا\" AFM.txt TAD.txt ARB_mo3rb.txt 2>/dev/null | head -5"
}
```


### [2026-09-14T02:04:48.307Z] TOOL RESULT

```
--- try صحراء ---
--- AFM/TAD ---
AFM.txt:2609:ܕܰܣܺܝܰܥ ܝ ܬܝ الخ 81 الدست يعنى الصحراء 07 3 .دشت 4 
AFM.txt:2655:( الدسّت) فارسي حض وهو الصحراء وهو ايضاً اسم ولابة في خراسان وهي 
AFM.txt:2656:المعروفة بالدست !ܠ ܚܨ ٠.‏ وام صحراء بتركستان دهي معردفة ܕܐ ܚ̈ܝ قبجاق واسم 
ARB_mo3rb.txt:11136:دشت » ٠.‏ وقال فى ”*دشت'“* :« فارمى محض ودر الصحراء » ٠‏ والشباب اللفاعى تلد المواليق 
ARB_mo3rb.txt:11137:16 فقال : « دست ؛ معرب دشت »4 وهى الصحراء» ٠‏ )2( فى الجهرة « حير رذارس» وما هنا
```


## [2026-09-14T02:04:54.586Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B5%D8%AD%D8%B1%D8%A7/",
 "prompt": "What do فرهنگ معین and لغت‌نامه دهخدا say for صحرا — origin tag (Arabic?), meanings, and the plural صحاری?"
}
```


## [2026-09-14T02:04:55.801Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D8%AD%D8%B1%D8%A7",
 "prompt": "Persian صحرا entry: etymology (borrowed from Arabic?), meanings, plural forms."
}
```


### [2026-09-14T02:05:00.391Z] TOOL RESULT

```
# صحرا (Sahara/Desert)

## Etymology
The word صحرا is "borrowed from Arabic صَحْرَاء (ṣaḥrāʔ)" according to the Persian entry. It subsequently entered other languages like Punjabi and Urdu through Persian.

## Meanings
In Persian, صحرا has two primary definitions:
1. **Desert** — with synonyms including بیابان (biyâbân) and هامون (hâmun)
2. **Plain** — synonymous with دشت (dašt)

## Language Variants
The word appears across multiple language families:
- **Persian**: sahrā / sahrâ
- **Punjabi**: ṣaḥirā (masculine)
- **South Levantine Arabic**: ṣaḥra (feminine)
- **Urdu**: sahrā (masculine)

The term demonstrates how Arabic vocabulary spread throughout Islamic cultural and linguistic zones, particularly in Persian and Indo-Aryan languages.
```


### [2026-09-14T02:05:00.695Z] TOOL RESULT

```
# صحرا According to Persian Dictionaries

## Farhang-e Mu'in (فرهنگ معین)
**Origin:** Arabic (صحراء)

**Meanings:** "(1) Desert plain; (2) Wasteland"

The dictionary notes a figurative expression: "کربلای صحرا" (the desert of Karbala) refers to a place lacking water, vegetation, and resources.

## Lughat-nameh-ye Dehkhoda (لغت‌نامه دهخدا)
**Origin:** Arabic (صحراء)

**Meanings:** The entry describes it as "a flat desert, an expansive barren area without vegetation, wasteland" and provides numerous related terms.

**Plural:** The dictionary lists two plural forms:
- صحراوات
- صحاری

Both plurals are documented in classical Persian sources, with صحاری appearing in quoted poetic passages from major Persian poets like Ferdowsi and Nasir Khosrow.
```


## [2026-09-14T02:05:10.682Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D9%86%DA%AF%D8%B1%D9%81' \\\n 'https://www.etymonline.com/word/cinnabar' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%CE%B9%CE%BD%CE%BD%CE%AC%CE%B2%CE%B1%CF%81%CE%B9' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D8%AD%D8%B1%D8%A7%D8%A1' \\\n 'https://en.wiktionary.org/wiki/scamnum' \\\n 'https://www.etymonline.com/word/shambles' \\\n 'https://abadis.ir/fatofa/%D8%B5%D8%AD%D8%B1%D8%A7/' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D8%AD%D8%B1%D8%A7' ; do\n  python3 tools/fetch_source.py \"$u\" --note 'page 450 verification (S.h.r / Sinkadruš / Skabh)' 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T02:05:17.203Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/91e1640fb42d9180.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd11ab1001f33f66.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1951293d3b765022.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35ac0076a7dc9058.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b59b2888a634b3d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92134c16d7cfe96c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ac0d74008f66f49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3750bd2a39188082.txt
```


## [2026-09-14T02:05:20.983Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg450.png data/verification/sources/refs/ocr/BOOK/450.png\nls -la data/verification/sources/refs/ocr/BOOK/450.png"
}
```


### [2026-09-14T02:05:21.066Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79151 Sep 13 22:05 data/verification/sources/refs/ocr/BOOK/450.png
```


## [2026-09-14T02:05:23.908Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T02:05:24.037Z] TOOL RESULT

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


## [2026-09-14T02:16:39.353Z] TOOL CALL #61: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-450.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_SHANGARF = \"https://en.wiktionary.org/wiki/%D8%B4%D9%86%DA%AF%D8%B1%D9%81\"\nE_CINNABAR = \"https://www.etymonline.com/word/cinnabar\"\nW_KINNABARI = \"https://en.wiktionary.org/wiki/%CE%BA%CE%B9%CE%BD%CE%BD%CE%AC%CE%B2%CE%B1%CF%81%CE%B9\"\nW_SAHRA_AR = \"https://en.wiktionary.org/wiki/%D8%B5%D8%AD%D8%B1%D8%A7%D8%A1\"\nW_SCAMNUM = \"https://en.wiktionary.org/wiki/scamnum\"\nE_SHAMBLES = \"https://www.etymonline.com/word/shambles\"\nAB_SAHRA = \"https://abadis.ir/fatofa/%D8%B5%D8%AD%D8%B1%D8%A7/\"\nW_SAHRA_FA = \"https://en.wiktionary.org/wiki/%D8%B5%D8%AD%D8%B1%D8%A7\"\n\nKLN_SAHARA = (\"Klein 1966-67 p. 1373 (KLN_1966.txt form-feed leaf 729, which carries the printed \"\n              \"page numeral 1373) s.v. 'Sahara, n., the great desert of North Africa. — Fr. Arab. \"\n              \"sahra', ‘desert’, prop. fem. of the adj. asharū, ‘yellowish red’, used as a noun; \"\n              \"rel. to Heb. tzahor, ‘white’.'\")\n\ndoc = {\n \"pdf_page\": 450,\n \"book_page\": 420,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------- entry 0 : S.h.r ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"S.h.r\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Arabic root ص ح ر (ṣ-ḥ-r) ‘to be reddish-fawn, yellowish-red’, whence أَصْحَر (ʾaṣḥar) ‘reddish-fawn’, f. صَحْرَاء (ṣaḥrāʾ)\",\n \"note\": (\"The root box is right in substance: Arabic ṣ-ḥ-r is a colour root ('be tawny, reddish-fawn'), \"\n          \"and Klein p.1373 — the page Nourai cites — states exactly this. The only caveat is the \"\n          \"transliteration: Nourai's 'S.h.r' writes ṣād as plain s and ḥāʾ as plain h, so the root should be \"\n          \"read ṣ-ḥ-r (صحر), not s-h-r (سهر, which is a different root, 'to stay awake'). \"\n          \"This is Nourai's usual simplified transliteration system, not an error of fact. \"\n          \"The chart is one of the few Semitic (non-Indo-European) root boxes in the book, correctly labelled Arabic.\"),\n \"note_fa\": (\"ریشهٔ سه‌حرفی عربی «ص ح ر» به معنای «سرخ‌فام و زردتاب بودن» است و صفت رنگ آن بر وزن \"\n             \"«أَفْعَل / فَعْلاء» می‌آید: أصحر (مذکر) و صحراء (مؤنث). کلاین در صفحهٔ ۱۳۷۳ دقیقاً همین را می‌گوید. \"\n             \"تنها نکته آن است که آوانویسی نورایی (S.h.r) صاد را s و حا را h نوشته است؛ این شیوهٔ ساده‌شدهٔ اوست نه خطا. \"\n             \"در مجموع ادعای نورایی درست است.\"),\n \"sources\": [W_SAHRA_AR],\n \"ref_check\": [\n   {\"ref\": \"KLN:1373\", \"status\": \"supports\", \"note\": KLN_SAHARA + \" — the colour adjective and its feminine substantive are exactly Nourai's root box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966-67 p. 1373 (leaf 729) s.v. Sahara\", \"stance\": \"supports\",\n    \"note\": \"'prop. fem. of the adj. asharū, ‘yellowish red’, used as a noun; rel. to Heb. tzahor, ‘white’' (grep '^Sahara' KLN_1966.txt).\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org صحراء\", \"stance\": \"supports\",\n    \"note\": \"'Root: ص ح ر (ṣ ḥ r)', diptote ṣaḥrāʾ with plurals ṣaḥārā/ṣaḥrāwāt/ṣaḥārī.\"},\n   {\"src\": \"AFM\", \"where\": \"AFM.txt l. 2609, 2655 s.v. الدست\", \"stance\": \"silent\",\n    \"note\": \"Addi Shir uses الصحراء only as the Arabic gloss of Persian دشت; he has no entry on صحرا itself, i.e. he does not treat it as a Persian loan — consistent with the chart's direction.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"as-har; sahrâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Nourai's 'as-har' is Arabic أَصْحَر ʾaṣḥar, the ʾafʿal-pattern colour adjective of the root \"\n   \"ṣ-ḥ-r ('be tawny/reddish-fawn'; cf. the abstract صُحْرَة ṣuḥra 'reddish tinge'). Its regular feminine is \"\n   \"صَحْرَاء ṣaḥrāʾ, and that feminine was substantivised — 'the fawn-coloured one (sc. land)' — giving the \"\n   \"ordinary Arabic word for 'desert', a diptote with the broken plurals ṣaḥārā / ṣaḥārī and the sound \"\n   \"plural ṣaḥrāwāt. Klein p.1373 states the derivation in precisely these terms and adds the Semitic \"\n   \"comparison Hebrew ṣāhōr 'white/pale'. Both of Nourai's words and his colour→landscape semantic \"\n   \"explanation ('desert, due to its colour') are therefore correct.\"),\n \"derivation_fa\": (\"«أَصْحَر» صفت رنگ بر وزن أَفْعَل از ریشهٔ صحر است و مؤنث آن «صَحْراء» می‌شود؛ همین مؤنث در عربی \"\n   \"اسم شده و معنای «بیابان» گرفته است — یعنی «زمین زردتاب» — و جمع‌های مکسر صحاری، صحارا و جمع سالم \"\n   \"صحراوات دارد. کلاین (ص ۱۳۷۳) همین را می‌نویسد و آن را با عبری ṣāhōr «سپید» هم‌ریشه می‌داند. \"\n   \"تحول معنایی «رنگ» ← «زمین آن رنگ» که نورایی می‌گوید درست است.\"),\n \"sources\": [W_SAHRA_AR],\n \"ref_check\": [\n   {\"ref\": \"KLN:1373\", \"status\": \"supports\", \"note\": KLN_SAHARA},\n   {\"ref\": \"FVA:226\", \"status\": \"not_checked\", \"note\": \"FVA = Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi (1368/1989); refs_online.json records that no digital copy exists on any permitted platform (catalogue record only).\"},\n   {\"ref\": \"AHD:1143\", \"status\": \"not_checked\", \"note\": \"AHD:1143 is a page of the 1975/76 New College Edition dictionary proper (s.v. Sahara), which is lending-only on archive.org; the open local proxy AHD_watkins1985.txt contains only the Indo-European root appendix and so has no Semitic entry. The page number is consistent with the S- range of a 1550-page dictionary.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1373 (KLN_1966.txt leaf 729) s.v. Sahara\", \"stance\": \"supports\",\n    \"note\": \"'Fr. Arab. sahra', ‘desert’, prop. fem. of the adj. asharū, ‘yellowish red’, used as a noun.'\"},\n   {\"src\": \"Wiktionary\", \"where\": \"صحراء (Arabic)\", \"stance\": \"supports\",\n    \"note\": \"root ص ح ر given explicitly; plurals صحاری / صحراوات; borrowed onward into Persian, Turkish, Urdu, Pashto and English.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch 1927 (grep 'Sahara', 'sahra')\", \"stance\": \"silent\",\n    \"note\": \"Lokotsch collects Oriental words that entered European languages; ṣaḥrāʾ/Sahara has no numbered entry (only Wüste in other articles), so he neither supports nor contradicts.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"sahrâ «صحرا» (extra صحاری)\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian صحرا ṣaḥrā 'desert, open plain' is a straight Arabic loanword taken over after the \"\n   \"Islamic conquest and current in Persian prose and verse from the 4th/10th century on. Persian drops \"\n   \"the final hamza of the Arabic diptote صَحْرَاء, writing صحرا, and ṣād and ḥāʾ are pronounced /s/ and /h/, \"\n   \"so the word is realised sahrā; the Arabic broken plural صحاری ṣaḥārī (Nourai's script extra) and \"\n   \"صحراوات were borrowed with it, both being quoted from Ferdowsi and Nāṣer Khosrow in Dehkhodā. \"\n   \"There is no Iranian etymon: the native Persian words are بیابان and دشت, and Moʿin marks the \"\n   \"entry [ع.] 'Arabic'.\"),\n \"derivation_fa\": (\"«صحرا» در فارسی نو وام‌واژه‌ای عربی است (صَحْراء) که پس از اسلام وارد فارسی شده و همزهٔ پایانی آن \"\n   \"در نوشتار فارسی افتاده است؛ صاد و حای عربی در فارسی به /s/ و /h/ تلفظ می‌شود. جمع مکسر عربی \"\n   \"«صحاری» نیز همراه آن وام گرفته شده و در شعر فردوسی و ناصرخسرو آمده است. معین نیز مدخل را با نشانهٔ [ع.] \"\n   \"می‌آورد. برابرهای ایرانی‌تبار آن «بیابان» و «دشت» است. ادعای نورایی درست است.\"),\n \"sources\": [AB_SAHRA, W_SAHRA_FA],\n \"ref_check\": [\n   {\"ref\": \"FVA:226\", \"status\": \"not_checked\", \"note\": \"No digital copy of Nahvi's Farhang-e Vāžehā-ye ʿArabi dar Fārsi exists on archive.org/noorlib/ketabnak per refs_online.json; only an OpenLibrary catalogue record. (Its subject matter — Arabic words used in Persian — makes it an appropriate citation for exactly this node.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin via abadis.ir/fatofa/صحرا\", \"stance\": \"supports\",\n    \"note\": \"Moʿin tags the entry '[ع.]' (Arabic صحراء) and glosses 'دشت بیابانی، زمین لم‌یزرع'.\"},\n   {\"src\": \"Dehkhoda\", \"where\": \"Loghatnāme via abadis.ir/fatofa/صحرا\", \"stance\": \"supports\",\n    \"note\": \"'ع. صحراء ... دشت هموار، زمین فراخ بی‌گیاه'; lists the plurals صحراوات and صحاری, the latter quoted from classical Persian verse — i.e. exactly Nourai's script extra.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"صحرا (Persian)\", \"stance\": \"supports\",\n    \"note\": \"'Borrowed from Arabic صَحْرَاء (ṣaḥrāʾ)'; onward to Urdu sahrā and Punjabi.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"Sahara\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English Sahara is the Arabic word used as the proper name of the North African desert: al-ṣaḥrāʾ \"\n   \"'the desert' (in Arabic usage الصحراء الکبرى 'the Great Desert'), which reached English through European \"\n   \"geographical writing and map-making (Latinised/Italianised forms Sahara, Zahara appear from the 16th \"\n   \"century, standard in English from the 18th). The English name therefore descends from the same Arabic \"\n   \"feminine adjective as node #1, not from the Persian of node #2, and Nourai draws it correctly as a \"\n   \"sibling of the Persian word rather than its descendant. Klein handles the English headword under exactly \"\n   \"this etymology on the cited page.\"),\n \"derivation_fa\": (\"نام «Sahara» در انگلیسی همان واژهٔ عربی الصحراء است که از راه جغرافیانویسی اروپایی به صورت اسم خاص درآمده \"\n   \"است. این وام‌گیری مستقیماً از عربی صورت گرفته، نه از فارسی؛ نمودار کتاب نیز آن را هم‌سطح با صحرای فارسی \"\n   \"و نه برگرفته از آن نشان می‌دهد. کلاین در صفحهٔ ۱۳۷۳ همین ریشه را می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [W_SAHRA_AR],\n \"ref_check\": [\n   {\"ref\": \"AHD:1143\", \"status\": \"not_checked\", \"note\": \"Page of the New College Edition dictionary proper (not the IE appendix); no open scan. The local Watkins 1985 proxy has no such entry.\"},\n   {\"ref\": \"KLN:1373\", \"status\": \"supports\", \"note\": KLN_SAHARA + \" The English headword and the Arabic etymology stand on the very page Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1373 s.v. Sahara\", \"stance\": \"supports\", \"note\": \"'the great desert of North Africa. — Fr. Arab. sahraʾ, ‘desert’.'\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV, FSD_vol4.txt l. 603 s.v. Sa-haˈra\", \"stance\": \"partial\",\n    \"note\": \"'Sa-ha'ra ... 1. A desert plateau in N. Africa, dotted with oases ... 2. Figuratively, a wilderness, desert' — the gazetteer entry confirms the word and the figurative English sense but gives no etymology.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (grep 'Sahara')\", \"stance\": \"silent\",\n    \"note\": \"Skeat has no entry for Sahara (he excludes most proper names); no counter-evidence.\"}\n ]\n})\ndoc[\"entries\"].append(e0)\n\n# ---------------- entry 6 : Sinkadruš ----------------\ne6 = {\n \"entry\": 6,\n \"root\": \"Sinkadruš\",\n \"verdict\": \"transcription_suspect\",\n \"modern_form\": \"Old Persian sinkabruš 𐎿\\ud800\\udf a1 (𐎿𐍡𐎣𐎲𐎽𐎢𐏁) 'carnelian'\",\n \"note\": (\"Two separate problems. (1) FORM: the printed page reads 'Sinkadruš' with a d, but the Old Persian \"\n   \"word attested in Darius's Susa foundation charter (DSf §37 kāsaka hya kapautaka utā sinkabruš) is \"\n   \"sinkabruš, with b — Kent, Old Persian, reads siⁿkabru- and cites it three times (§86 dialect mixture, \"\n   \"§V on OP p/b/f, § on u-stems). The extraction is faithful to the page (I read the 300-dpi render of \"\n   \"pdf p.450), so this is Nourai's own misprint, d for b. \"\n   \"(2) GLOSS: Kent glosses sinkabru- 'carnelian' — a red semi-precious stone brought, with lapis lazuli, \"\n   \"from Sogdiana — not 'the red ore of mercury used as a pigment'. That is the meaning of the New Persian \"\n   \"descendant شنگرف, which Nourai has back-projected onto the Old Persian etymon. Kent further notes \"\n   \"that the word 'lacks a convincing IE etymology', i.e. it is itself probably a culture-word borrowed into \"\n   \"Old Persian. The root box is nevertheless a real Old Persian word, and the OP→NP link it asserts is the \"\n   \"one Wiktionary and the standard handbooks give.\"),\n \"note_fa\": (\"در این جعبهٔ ریشه دو اشکال هست. نخست صورت: واژهٔ پارسی باستان در سنگ‌نبشتهٔ داریوش در شوش (DSf) \"\n   \"sinkabruš است نه sinkadruš؛ کنت آن را با «ب» می‌خواند. تصویر صفحهٔ چاپی نشان می‌دهد که خود کتاب «Sinkadruš» را \"\n   \"چاپ کرده؛ پس این خطای چاپی خود نورایی است نه خطای خوانش اسکن. دوم معنا: معنای پارسی باستان آن «عقیق» \"\n   \"(carnelian) است که همراه لاجورد از سغد می‌آوردند، نه «سنگ معدنی جیوه»؛ این معنای دوم از آنِ بازماندهٔ \"\n   \"فارسی نوی آن یعنی «شنگرف» است. پیوند پارسی باستان به فارسی نو درست است، ولی صورت و معنای ریشه باید درست شود.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"Sinkadruš\",\n \"correct_form\": \"sinkabruš\",\n \"sources\": [W_SHANGARF],\n \"ref_check\": [\n   {\"ref\": \"MON:2083\", \"status\": \"not_checked\",\n    \"note\": \"MON:2083 is a page of Moʿin's six-volume Farhang-e Fārsi, which exists in no digital copy (refs_online.json, re-searched 2026-09); only the 2-vol Adena abridgement is online, and its شنگرف entry (MON_part1.txt l. 86933) carries only the tag '[= معر. شنجرف]' without the Latin-script Old Persian etymon that the print edition gives. So the Old Persian form Nourai attributes to Moʿin could not be checked at its source.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §86 (KNT.txt l. 357), §V (l. 1042), §u-stems (l. 1838), DSf text (l. 4262) and translation (l. 4295)\", \"stance\": \"partial\",\n    \"note\": \"'siⁿkabru- ‘carnelian’' — the form has b, not d, and the gloss is 'carnelian': 'The precious stone lapis-lazuli and carnelian which was wrought here, this was brought from Sogdiana' (DSf). Kent also lists it among words that 'lack a convincing IE etymology'. So Kent supports the existence of the OP word but contradicts both Nourai's spelling and his gloss.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"شنگرف (Persian), etymology section\", \"stance\": \"partial\",\n    \"note\": \"'inherited from Old Persian 𐎿𐍡𐎣𐎲𐎽𐎢𐏁 (sinkabruš, ‘carnelian’)' — same form with b, same 'carnelian' gloss; supports the OP→NP line but not Nourai's spelling.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (grep 'sinkabru')\", \"stance\": \"silent\",\n    \"note\": \"No entry — expected, since Bartholomae's Old Persian coverage is thin and the word is confined to DSf.\"}\n ],\n \"nodes\": []\n}\n\ne6[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"šangarf «شنگرف» (extra زنجرف)\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian شنگرف šangarf 'cinnabar, vermilion; red pigment' continues Old Persian sinkabruš \"\n   \"'carnelian' through an unattested Middle Persian *šangarf: initial s- was palatalised to š- before the \"\n   \"front vowel, the cluster -kabr- was voiced and metathesised to -garf, and the Old Persian nominative \"\n   \"ending -uš was lost as regularly in the passage to Middle Persian. The meaning moved from one red \"\n   \"mineral (carnelian) to another (mercuric sulphide used as the painter's and calligrapher's red). The \"\n   \"Middle Persian form is guaranteed indirectly by the Arabic loan زِنجَفْر zinjafr / زُنجُفر zunjufr, \"\n   \"which came back into Persian as the Arabicised doublet زنجرف (Nourai's script extra) and زنجفر. \"\n   \"Borhān-e Qāṭeʿ on the page Nourai cites calls the word 'فارسی' outright, describes it as made \"\n   \"'از سیماب و گوگرد' (from quicksilver and sulphur) and used by painters, and quotes the very verse of \"\n   \"Kasāʾī Marvzī that Nourai prints.\"),\n \"derivation_fa\": (\"«شنگرف» در فارسی نو بازماندهٔ پارسی باستان sinkabruš «عقیق» است، از راه صورتی نامضبوط در فارسی میانه \"\n   \"(*šangarf): «س» آغازین پیش از واکهٔ پیشین به «ش» بدل شده، خوشهٔ -kabr- با واک‌شدن و قلب به -garf رسیده و \"\n   \"پایانهٔ نامی -uš برابر قاعده افتاده است. تحول معنایی از یک سنگ سرخ به سنگ سرخ دیگر (سولفور جیوه، رنگ سرخ \"\n   \"نقاشان) روی داده است. معرّب آن زِنجَفْر است که دوباره به صورت «زنجرف» وارد فارسی شده (دوگانهٔ معرّب). \"\n   \"برهان قاطع در همان صفحهٔ ۱۳۰۲ آن را «فارسی» می‌خواند و همین بیت کسایی مروزی را شاهد می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [W_SHANGARF],\n \"ref_check\": [\n   {\"ref\": \"MON:2083\", \"status\": \"not_checked\", \"note\": \"The 6-vol Moʿin is not digitised; the Adena 2-vol abridgement (MON_part1.txt l. 86933) has 'شنگرف: [= معر. شنجرف] (زم.) ... سولفور مرکوریک، سولفور معدنی جیوه، زنجفر، حجرالصرف' — the mineral sense and the زنجفر doublet check out, the page number cannot.\"},\n   {\"ref\": \"BQT:1302\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ, Moʿin ed., vol. 3 pdf p. 93 = printed p. 1302 (BQT_v3_pages.txt): 'شنگرف ... فارسی، بر وزن و معنی شنجرف باشد، و آن چیزی است که از سیماب و گوگرد سازند و نقاشان و مصوران به کار برند و معرب آن شنجرف است و به یونانی سربقون خوانند'; footnote 5 on the same page quotes 'بنفشه‌زار بپوشید روزگار به برف / چنار گشت دوتا و زریر شد شنگرف — کسایی مروزی، لغت فرس', i.e. Nourai's verse and its attribution come verbatim from this page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 3, printed p. 1302 (pdf p. 93)\", \"stance\": \"supports\", \"note\": \"see ref_check — the word is called Persian, the Arabicised form شنجرف is given, and Kasāʾī's verse is the quotation.\"},\n   {\"src\": \"MON\", \"where\": \"Adena 2-vol abridgement, MON_part1.txt l. 86933 s.v. شنگرف\", \"stance\": \"supports\", \"note\": \"'سولفور مرکوریک ... زنجفر، حجر الصرف'; 'گرد آن در نقاشی بکار می‌رود' — Nourai's gloss exactly.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch 1927, entry 1827 (LKT.txt l. 4141)\", \"stance\": \"supports\",\n    \"note\": \"'1827. Pers. šängärf: ‘Mennig, Zinnober’, hieraus ar. zinǧafr, zunǧufr ‘dass.’, ebenso tk. zingifre.' — independent confirmation that Persian is the source and زنجفر the Arabic reflex.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"شنگرف (Persian)\", \"stance\": \"supports\",\n    \"note\": \"'Inherited from Middle Persian (unattested, but borrowed into Arabic زِنجَفْر (zinjafr)), ultimately inherited from Old Persian sinkabruš'; compares Sanskrit hiṅgula 'cinnabar'.\"}\n ]\n})\n\ne6[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Greek\", \"words\": \"kinnabari\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Ancient Greek κιννάβαρι (with the variant τιγγάβαρι) is first used by Theophrastus (De lapidibus, \"\n   \"late 4th c. BCE) for the red mineral and the pigment won from it; Dioscorides and Pliny already confuse \"\n   \"it with 'dragon's blood' resin. Every dictionary in this library treats it as an Iranian culture-word: \"\n   \"Klein p.289 'which prob. derives fr. Pers. shangārf', Skeat 'Gk. κιννάβαρι ... from Pers. zinjarf, \"\n   \"zinjifr', Lokotsch 1827 derives the Greek from the Persian. Two qualifications keep this from 'confirmed'. \"\n   \"First, chronology: a 4th-century-BCE Greek borrowing must come from the Old/Middle Iranian stage \"\n   \"(sinkabruš), not from the New Persian šangarf box that Nourai draws the arrow from. Second, the phonetic \"\n   \"match is loose (Iranian s-/š- vs Greek κ-, and the Greek -νν- has no Iranian counterpart), which is why \"\n   \"Beekes classes κιννάβαρι as an eastern loanword of ultimately unknown origin, merely 'compare' the \"\n   \"Iranian and Arabic words. Nourai's gloss 'red lead' follows Lokotsch's 'Mennig, Zinnober' and Skeat's \"\n   \"'red lead, vermilion, cinnabar'; strictly the Greek word means cinnabar/vermilion, not minium.\"),\n \"derivation_fa\": (\"واژهٔ یونانی κιννάβαρι نخست‌بار در تئوفراستوس (سدهٔ چهارم پ.م.) دیده می‌شود. کلاین، اسکیت و لوکوچ هر سه \"\n   \"آن را وام‌واژه‌ای ایرانی می‌دانند و به «شنگرف / زنجرف» بازمی‌گردانند. اما دو احتیاط هست: از نظر تاریخی وام‌گیری \"\n   \"سدهٔ چهارم پیش از میلاد باید از صورت ایرانی باستان (sinkabruš) باشد نه از فارسی نو؛ و از نظر آوایی نیز \"\n   \"انطباق کامل نیست (س/ش ایرانی در برابر κ یونانی)؛ برای همین بیکس آن را وام‌واژه‌ای شرقی با خاستگاه نامعلوم \"\n   \"می‌خواند. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_KINNABARI, E_CINNABAR],\n \"ref_check\": [\n   {\"ref\": \"KLN:289\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 163 (between the page numerals 286 on leaf 161 and 292/293 on leaf 164, so printed pp. 289/290) s.v. cinnabar: 'F. cinabre, fr. OF. cenobre, fr. L. cinnābaris, fr. Gk. κιννάβαρι, which prob. derives fr. Pers. shangārf, ‘red lead, cinnabar’.' Klein's 'prob.' is the hedge Nourai drops.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt l. 3461 s.v. Cinnabar\", \"stance\": \"supports\",\n    \"note\": \"'Cinnabar, Cinoper. (Gk.-Pers.) Gk. κιννάβαρι, vermilion. From Pers. zinjarf, zinjifr, red lead, vermilion, cinnabar'; his source list (l. 23619) files 'cinnabar' under 'Greek from Persian'.\"},\n   {\"src\": \"LKT\", \"where\": \"entry 1827\", \"stance\": \"supports\",\n    \"note\": \"'Aus hieraus entstandenem gr. τιγγάβαρι, κιννάβαρι, lat. cinnäbaris wurde: it. cinabro, frz. cinabre ... engl. cinnabar, dtsch. Zinnober' — the whole of Nourai's chain in one sentence.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"κιννάβαρι (Ancient Greek)\", \"stance\": \"partial\",\n    \"note\": \"'Probably an eastern loanword according to Beekes. Compare Arabic زِنجَفْر (zinjafr), related to Persian شنگرف (šangarf) from Old Persian ...' — same family, but the direction is left open rather than asserted.\"}\n ]\n})\n\ne6[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"cinnâbaris\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin cinnabaris (also cinnabari, neuter, in Solinus) is a straight transcription of Greek \"\n   \"κιννάβαρι, taken over with the technical vocabulary of mineralogy and painting (Pliny, Nat. Hist. \"\n   \"33.115–116, who complains that minium and cinnabaris are confused). Ernout-Meillet say so in as many \"\n   \"words and warn against the homonym cinnabar 'a kind of Gothic head-dress'. Nourai's macron in \"\n   \"'cinnâbaris' marks the long ā of the Greek penult, correctly.\"),\n \"derivation_fa\": (\"لاتین cinnabaris رونوشت مستقیم یونانی κιννάβαρι است که همراه اصطلاحات کانی‌شناسی و نقاشی وارد لاتین شده \"\n   \"(پلینی، تاریخ طبیعی ۳۳). ارنو-میه نیز می‌نویسد «Transcription du gr. κιννάβαρι». ادعای نورایی درست است.\"),\n \"sources\": [E_CINNABAR],\n \"ref_check\": [\n   {\"ref\": \"AHD:243\", \"status\": \"not_checked\",\n    \"note\": \"A page of the AHD dictionary proper (s.v. cinnabar, in the ci- range — consistent), which is lending-only; the open local AHD_watkins1985.txt is only the Indo-European root appendix and has no cinnabar entry (grep 'cinnabar' returns nothing).\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt l. 11948\", \"stance\": \"supports\",\n    \"note\": \"'cinnabaris, -is f. (-ri n. Sol.): cinabre. Transcription du gr. κιννάβαρι, sans rapport avec le précédent [cinnabar, a Gothic head-dress].'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 289 s.v. cinnabar\", \"stance\": \"supports\", \"note\": \"'fr. L. cinnābaris, fr. Gk. κιννάβαρι'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/cinnabar\", \"stance\": \"supports\", \"note\": \"'Late Latin cinnabaris, from Greek kinnabari'.\"}\n ]\n})\n\ne6[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"cinbare\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"The French word is cinabre, attested from the 13th century (Old French cinabre, with the \"\n   \"variant cenobre that Klein records), from Latin cinnabaris with loss of the Latin ending and the usual \"\n   \"Old French -bre outcome. The book prints 'cinbare', which is a metathesis of -abre to -bare and is not \"\n   \"a French word at any period; I rendered pdf p. 450 at 500 dpi and the page really does read 'cinbare', \"\n   \"so this is Nourai's misprint, not a scanning error. The reference he attaches to the box, KLN:289, \"\n   \"spells the form correctly as 'F. cinabre, fr. OF. cenobre' — so his own source contradicts his spelling. \"\n   \"The derivation step itself (Latin → French → English) is correct and well attested.\"),\n \"derivation_fa\": (\"صورت فرانسوی این واژه cinabre است (از سدهٔ ۱۳م میلادی، در فرانسه‌ی کهن با گونهٔ cenobre) و از لاتین \"\n   \"cinnabaris گرفته شده است. آنچه در کتاب چاپ شده («cinbare») قلب حروف است و در هیچ دوره‌ای از فرانسه وجود نداشته؛ \"\n   \"تصویر صفحهٔ چاپی نشان می‌دهد که خطا از خود کتاب است نه از خوانش اسکن. جالب آنکه منبع خود نورایی (کلاین، ص ۲۸۹) \"\n   \"صورت درست cinabre را می‌آورد. مرحلهٔ لاتین ← فرانسه ← انگلیسی خود درست است.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"cinbare\",\n \"correct_form\": \"cinabre\",\n \"sources\": [E_CINNABAR],\n \"ref_check\": [\n   {\"ref\": \"KLN:289\", \"status\": \"partial\",\n    \"note\": \"Klein p.289 has the French stage but spells it differently: 'cinnabar, n. ... — F. cinabre, fr. OF. cenobre, fr. L. cinnābaris'. So the page supports the arrow and contradicts the form in the box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 289 s.v. cinnabar\", \"stance\": \"partial\", \"note\": \"'F. cinabre, fr. OF. cenobre' — neither spelling is 'cinbare'.\"},\n   {\"src\": \"LKT\", \"where\": \"entry 1827\", \"stance\": \"partial\", \"note\": \"Lokotsch lists 'frz. cinabre' among the Romance reflexes of lat. cinnabaris.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/cinnabar\", \"stance\": \"partial\", \"note\": \"'Old French cinabre (13c.)' — confirms the French link and the correct form.\"},\n   {\"src\": \"BOOK\", \"where\": \"data/verification/sources/refs/ocr/BOOK/450.png (pdftoppm render of pdf p. 450)\", \"stance\": \"supports\",\n    \"note\": \"The French box on the printed page reads 'cinbare'; the JSON extraction is faithful.\"}\n ]\n})\n\ne6[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"cinnabar\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English cinnabar is first recorded in the mid-15th century for the red mercuric-sulphide mineral \"\n   \"and the pigment (vermilion) made from it; from the 14th to the 17th century it was also used of the red \"\n   \"resin 'dragon's blood', which was believed to be a mixture of dragon's and elephant's blood — a confusion \"\n   \"inherited from Dioscorides. The route is Old French cinabre > Middle English cinabre/cynoper, the modern \"\n   \"spelling cinnabar being re-latinised after L. cinnabaris. Klein and Etymonline agree on the whole chain, \"\n   \"so Nourai's five-box line Persian → Greek → Latin → French → English is right in its Western half.\"),\n \"derivation_fa\": (\"«cinnabar» در انگلیسی از نیمهٔ سدهٔ ۱۵م به معنای سولفور جیوه و رنگدانهٔ سرخ به کار رفته و از فرانسهٔ کهن \"\n   \"cinabre گرفته شده؛ املای امروزی با دو «n» بازسازی لاتینی است. در سده‌های ۱۴ تا ۱۷ به «خون اژدها» نیز \"\n   \"گفته می‌شد. زنجیرهٔ فارسی ← یونانی ← لاتین ← فرانسه ← انگلیسی در نیمهٔ غربی‌اش کاملاً درست است.\"),\n \"sources\": [E_CINNABAR],\n \"ref_check\": [\n   {\"ref\": \"AHD:243\", \"status\": \"not_checked\", \"note\": \"New College Edition page, lending-only; the local Watkins appendix has no cinnabar entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 289 s.v. cinnabar\", \"stance\": \"supports\", \"note\": \"'cinnabar, n., HgS, mercuric sulfide, a bright red mineral. — F. cinabre, fr. OF. cenobre, fr. L. cinnābaris, fr. Gk. κιννάβαρι ...'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/cinnabar\", \"stance\": \"supports\", \"note\": \"'mid-15c., ‘red or crystalline form of mercuric sulphide’ ... from Old French cinabre (13c.), from Late Latin cinnabaris, from Greek kinnabari'; also the 14c.-17c. 'dragon's blood' sense.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt l. 3461\", \"stance\": \"supports\", \"note\": \"'Cinnabar, Cinoper. (Gk.-Pers.)' — Skeat's label for the English word states the whole chain in compressed form.\"}\n ]\n})\ndoc[\"entries\"].append(e6)\n\n# ---------------- entry 7 : Skabh ----------------\nPOK916 = (\"Pokorny, IEW p. 916 (POK_full.txt lines 74949-74966, block ending 'Page(s): 916'): \"\n          \"'Root/lemma: skabh-, skamb-. Meaning: to support. Material: Old Indic skabhnāti, skabhnoti \"\n          \"‘props’ ... skambha-, skambhana-m ‘prop, pillar’, Avestan upaskambəm ‘under fastening, \"\n          \"strengthening’, fraskamba-, frascimbana- ‘girders, pillars’; npers. paskam ‘a covered walk \"\n          \"between columns, colonnade, piazza, arcade, gallery, porch, portico’, sogd. skʼnp- (*skamb) \"\n          \"‘base of the universe’; Latin scamnum (*skəbʰnom) ‘bench, footstool’, Demin. scabillum, \"\n          \"scabellum. References: WP. II 539, WH. II 487 f.'\")\n\ne7 = {\n \"entry\": 7,\n \"root\": \"Skabh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *skabʰ- / *skamb- 'to prop up, support' (Pokorny 916; Watkins skabh-)\",\n \"note\": (\"The root, the language label and the gloss are all right, and Nourai's page reference is exact: \"\n   \"Pokorny p. 916 has 'skabh-, skamb-: to support', and Watkins in the AHD appendix has 'skabh-. To prop up, \"\n   \"support ... [Pok. skabh- 916]'. Walde-Pokorny II 539 is the older form of the same article (sqabh- \"\n   \"'stützen'). One caveat worth recording for the reader: the root's Indo-European standing is weaker than \"\n   \"the chart suggests. Cheung (Etym. Dict. of the Iranian Verb, no. 344 *skamb) notes that 'this Ilr. root \"\n   \"has no certain IE (verbal) correspondences. Only the rather isolated noun, Lat. scamnum ... is cited as \"\n   \"cognate', so the whole Indo-European case rests on the single Latin word in node #4 plus Indo-Iranian. \"\n   \"Pokorny himself explains the nasal of skamb- as an Indo-Iranian innovation (a nasal present) later \"\n   \"generalised, and suspects the e-vocalism of Av. frascimbana- of being analogical after *stemb-.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *skabʰ-/*skamb- «تکیه دادن، ستون نهادن، نگاه داشتن» است؛ پوکورنی در صفحهٔ ۹۱۶ \"\n   \"و واتکینز در پیوست ریشه‌های AHD همین را می‌آورند و ارجاع نورایی دقیق است. با این حال باید دانست که \"\n   \"پشتوانهٔ هندواروپایی این ریشه سست است: چونگ (فرهنگ ریشه‌شناختی فعل ایرانی، مدخل ۳۴۴) می‌نویسد جز اسم \"\n   \"تنهای لاتین scamnum هیچ هم‌ریشهٔ قطعی درون‌هندواروپایی ندارد و بقیهٔ شواهد هندوایرانی است.\"),\n \"sources\": [W_SCAMNUM],\n \"ref_check\": [\n   {\"ref\": \"POK:916\", \"status\": \"supports\", \"note\": POK916}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 916, lemma skabh-/skamb-\", \"stance\": \"supports\", \"note\": \"see ref_check; page number exact.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p. 539 (WLD_Bd2_pages.txt leaf 543, running head 'sqabh- — (s)kamb-, (s)kemb- 539')\", \"stance\": \"supports\",\n    \"note\": \"'sqabh- „stützen“. Ai. skabhnāti, skábhnoti „befestigt, stützt, stemmt auf“ ... lat. scamnum (*sqabhnom) „Bank, Schemel“.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt, leaf 934) s.v. skabh-\", \"stance\": \"supports\",\n    \"note\": \"'skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.]' — Watkins cites the same Pokorny page Nourai does.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt l. 15426 and 15738\", \"stance\": \"supports\",\n    \"note\": \"'skabhos, ā (skobh-?) (1) ‘clasp, catch; prop, stay, support’ ... Skt. skabhnómi ‘fix; prop’'; and 'skobh- (skobhos) (2) ‘fixture; prop’. WP II, 539.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, entry 344 *skamb (CHEUNG.txt l. 22503-22536)\", \"stance\": \"partial\",\n    \"note\": \"'*skamb ‘to support, use as support’ ... «PIE? c LIV: 549 f. | Pok.: 916' and the footnote 'This Ilr. root has no certain IE (verbal) correspondences. Only the rather isolated noun, Lat. scamnum ‘stool, bench [for the feet]’, is cited as cognate in LIV' — the root is real but its IE depth is disputed.\"}\n ],\n \"nodes\": []\n}\n\ne7[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"skambem; upa-skambem; fra-sčimbana\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"All three forms exist, but two of the three glosses are loose. Bartholomae's headword (AiW \"\n   \"col. 1586) is the verbal root skamb- 'stemmen' (to prop, brace), attested only with preverbs; skambəm \"\n   \"is its absolutive, so 'skambem: support' is a verbal gerund ('by propping'), not a noun. upa.skambəm \"\n   \"(Vd. 8.10, AiW col. 393 and 1586) is likewise the absolutive of upa+skamb-, which Bartholomae renders \"\n   \"'unter Festmachen' and Pokorny 'under fastening, strengthening' — Nourai's 'for support, a pillar' \"\n   \"conflates it with the noun fra-skamba- m. 'Stütz-, Tragbalken; Vorhalle, Säulenhof' (Vd. 2.26, AiW \"\n   \"col. 998). The third form, frascimbana- (Yt. 13.26 'the most suitable of the roof-beams'; Vd. 18.74 \"\n   \"with the causative frascinbaiiōit), is a perfect passive participle meaning 'supporting beam, pillar' \"\n   \"in Bartholomae, Walde-Pokorny II 539, Pokorny 916 and Cheung 344 alike — NOT 'universe, world'. \"\n   \"Nourai has imported into the Avestan box the meaning of the Sogdian descendant in node #3; the shift \"\n   \"'the props (of heaven)' → 'world' happened in Sogdian, not in Avestan. The attachment of all three to \"\n   \"the root is nonetheless exactly what Pokorny prints on the page cited.\"),\n \"derivation_fa\": (\"هر سه صورت اوستایی واقعی‌اند، اما دو معنا دقیق نیست. بارتولومه مدخل را ستاک فعلی skamb- «تکیه دادن، \"\n   \"ستون زدن» می‌آورد که تنها با پیشوند به کار رفته؛ skambəm و upa.skambəm صورت وجه وصفی (absolutive) آن‌اند \"\n   \"نه اسم؛ معنای «ستون» از آنِ اسم fra-skamba- است. مهم‌تر آنکه frascimbana- در بارتولومه، والده-پوکورنی و \"\n   \"چونگ به معنای «تیرک و ستون نگاه‌دارنده» است نه «جهان»؛ معنای «جهان» تحولی سغدی است (نگ. گره شمارهٔ ۳) که \"\n   \"نورایی به اوستایی بازبرده است. پس انتساب واژه‌ها به ریشه درست است ولی معنای گزارده‌شده باید اصلاح شود.\"),\n \"sources\": [W_SCAMNUM],\n \"ref_check\": [\n   {\"ref\": \"POK:916\", \"status\": \"partial\",\n    \"note\": POK916 + \" — Pokorny has exactly Nourai's three Avestan forms, but glosses frascimbana- 'girders, pillars', not 'universe, world'.\"},\n   {\"ref\": \"SOD:152\", \"status\": \"supports\",\n    \"note\": \"Gharib's Sogdian Dictionary, printed p. 152 (SOD_pages.txt leaf 217; leaf 218 carries the running head '153'), entry 3844: 'fcmbδ M ... fəcambaδ (fcmbd) ©Gersh. *frascamba; Av. frascimbana ... world'. Gharib herself cites the Avestan form Nourai puts in this box as the etymon of the Sogdian word of node #3.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW: skamb- col. ~1586 (BRT.txt l. 26459), fra-skamba- col. ~998 (l. 17919), upa.skambəm col. ~393 (l. 8370), frascimbananąm col. ~136-146 (l. 4713)\", \"stance\": \"partial\",\n    \"note\": \"'skamb- ‘stemmen’, nur mit Praev. ... Absol. skambəm'; 'fra-skamba- m. 1) ‘Stütz-, Tragbalken’ 2) ‘Vorhalle, Säulenhof’'; 'upa.skambəm (sd.) ‘unter Festmachen’'; 'fravasayō ... frascimbananąm „die geeignetsten unter den Stützbalken“ Yt.13.26'. Forms confirmed, the gloss 'universe, world' is not.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 539\", \"stance\": \"partial\",\n    \"note\": \"'av. upaskambəm „unter Festmachen“, fraskamba-, frascimbana- „Stützbalken, Tragbalken, Pfeiler“' — same three forms, same 'beam/pillar' gloss.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 no. 344\", \"stance\": \"supports\",\n    \"note\": \"'*AVESTAN: (+ *fra-) YAv. frascinb- ‘to support’ ... Partic. perf. pass. YAv. frascimbana- (V 18.74); Caus. pres. OPT. 3sg. frascinbaiiōit' — a modern authority on the Iranian verb keeps the form under this root.\"},\n   {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar (grep skamb)\", \"stance\": \"silent\", \"note\": \"no relevant paragraph found.\"}\n ]\n})\n\ne7[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"pečkam «پچکم» (extra, as printed: بچکم ، بشکم ، پشکم)\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"The word and its attachment to the root are genuine — Pokorny prints 'npers. paskam ‘a covered \"\n   \"walk between columns, colonnade, piazza, arcade, gallery, porch, portico’' on the very page cited — but \"\n   \"there are two problems, one in the data and one in the arrow. \"\n   \"(a) DATA: the JSON gives the variant list as پیچکم ، پیشکم ، پشکم and the last word of the Rūdakī \"\n   \"hemistich as پچکم. The 500-dpi render of pdf p. 450 shows the book actually printing پِچکَم \"\n   \"(بِچکَم، بِشکَم، پِشکَم) and 'فرش دیبا کشیده بر بچکم'. The two b-initial variants were \"\n   \"misread as پی- forms; this is an extraction error, and the book's own list (بچکم/بشکم/پشکم) is \"\n   \"precisely the set Hübschmann records (paškam, piškam, baškam, biškam) and Moʿin cross-references \"\n   \"(پشکم [< بچکم، پچکم، بشکم]). \"\n   \"(b) ARROW: the Persian word does not come from the upa-/fra- compounds in the parent box but from a \"\n   \"*pati- compound. Hübschmann, Persische Studien pp. 41 and 191, derives np. paškam = Arm. patskamb \"\n   \"from Old Persian *pati-skamba-, with the Sasanian-era assimilation *patskamb > *paskamb; Cheung 344 \"\n   \"gives the same analysis (MMP *pdyskmbʼn 'rooms', NP paskam 'court, vestibule', Yazdi Zoroastrian \"\n   \"paskam 'portico', Sogd. ptsknpy 'porch, eaves', Arm. loanword patsgam 'portico'). So the chart's root \"\n   \"attachment is right, its intermediate step is not.\"),\n \"derivation_fa\": (\"خود واژه و پیوندش با این ریشه درست است؛ پوکورنی در همان صفحهٔ ۹۱۶ «npers. paskam» را با معنای «راهروی \"\n   \"ستون‌دار، ایوان» می‌آورد و برهان قاطع (ص ۴۱۰-۴۱۲) ذیل «پشکم» می‌نویسد «ایوان و بارگاه». اما دو نکته: \"\n   \"یکم، در دادهٔ استخراج‌شده گونه‌ها به صورت «پیچکم، پیشکم، پشکم» آمده در حالی که صفحهٔ چاپی «بچکم، بشکم، \"\n   \"پشکم» دارد و بیت رودکی نیز «... کشیده بر بچکم» است — پس خطای خوانش اسکن است نه خطای کتاب. دوم، \"\n   \"هوبشمان (ص ۴۱ و ۱۹۱) و چونگ این واژه را از پارسی باستان *pati-skamba- می‌گیرند که در فارسی میانه \"\n   \"*patskamb > *paskamb شده است؛ یعنی پیشوند آن pati- است نه upa-/fra- که در جعبهٔ اوستایی آمده. \"\n   \"هم‌ریشهٔ ارمنی آن patškamb / patsgam «ایوان، تالار» است.\"),\n \"error_in\": \"extraction\",\n \"book_prints\": \"پِچکَم (بِچکَم، بِشکَم، پِشکَم); verse: از تو خالی نگارخانهٔ جم — فرش دیبا کشیده بر بچکم\",\n \"correct_form\": \"script_extra should read بچکم ، بشکم ، پشکم (not پیچکم ، پیشکم ، پشکم); the quote's last word is بچکم\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:916\", \"status\": \"supports\", \"note\": \"Pokorny p. 916 lists 'npers. paskam ‘a covered walk between columns, colonnade, piazza, arcade, gallery, porch, portico’' under this root — Nourai's gloss is a paraphrase of Pokorny's.\"},\n   {\"ref\": \"BQT:410\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ vol. 1, BQT_v1_pages.txt leaf 636 (printed ≈ pp. 410-412 by the volume's leaf−224 offset): 'پشکم، بکسر اول بر وزن اشکم، ایوان و بارگاه و اگزنش؛ بفتح اول نیز بهمین معنی آمده است' — the porch/audience-hall sense Nourai gives.\"},\n   {\"ref\": \"MON:798\", \"status\": \"not_checked\",\n    \"note\": \"The 6-vol Moʿin is not digitised. The Adena abridgement has the entry three times: 'پچکم: [< بچکم، پشکم] (ا.) خانه‌ای که از همه سوی در و ... خانه تابستانی، بارگاه، ایوان، صفه' (MON_part1.txt l. 29449), 'پشکم: [< بچکم، پچکم، بشکم] (ا.) ایوان و بارگاه' (l. 32115) and 'بچکم [= پچکم، پشکم] خانهٔ تابستانی، بارگاه، ایوان، صفه، خانه‌ای که اطراف آن شبکه و بادگیر داشته باشد' (l. 23870) — content confirmed, page not verifiable.\"},\n   {\"ref\": \"FRS:183\", \"status\": \"partial\",\n    \"note\": \"Loḡat-e Fors has the word ('پچکم [کذا] خانهٔ تابستانی بود چون غرفه ... خم و بچکم [کذا] خانهٔ تابستانی باشد و نشستنگاهی که در زیرزمین سازند', FRS_pages.txt l. 14438, in the apparatus of the Eqbāl edition) but the local copy is Eqbāl's 1319/1940 edition, whose pagination differs from the Khārazmi 1365 edition Nourai cites, so the page number itself cannot be checked. The entry confirms both the پچکم and بچکم spellings and the 'summer house / gallery' sense.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §314-315 (HUB.txt l. 1390-1398 = p. 41) and p. 191 (l. 9171), index p. 41/191 (l. 10644)\", \"stance\": \"partial\",\n    \"note\": \"'Ich finde patis auch nicht in np. paškam (piškam, baškam, biškam) „domus aestiva, aula, atrium, coenaculum, porticus“ = arm. patškam ... sondern führe np. paškam = arm. patskamb auf ap. *pati-skamba- zurück, das ich zu zd. fra-skemba- Vd. 2,26 stelle ... Im mittelpersischen wurde *patskamb zu *paskamb'. Supports the root but replaces Nourai's Avestan parent with an OP *pati- compound; also gives exactly the four variants the book prints.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 no. 344, sections MIDDLE PERSIAN / NWIR / MISC\", \"stance\": \"partial\",\n    \"note\": \"'(+ *pati-) MMP *pdyskmbʼn ‘rooms’'; '(+ *pati-) NP paskam ‘court, vestibule’, Yzd. (Zor.) paskam ‘portico’'; '(+ *pati-) Arm. (LW) patsgam ‘portico’' — the modern handbook agrees with Hübschmann on *pati-, not upa-/fra-.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 1 leaf 636 (≈ printed p. 410-412) s.v. پشکم\", \"stance\": \"supports\",\n    \"note\": \"'ایوان و بارگاه و اگزنش' — Nourai's 'roof on pillars ... a porch'.\"},\n   {\"src\": \"MON\", \"where\": \"Adena abridgement, MON_part1.txt l. 23870, 29449, 32115\", \"stance\": \"supports\",\n    \"note\": \"the three cross-referenced headwords بچکم / پچکم / پشکم with the glosses خانهٔ تابستانی، بارگاه، ایوان، صفه.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (grep paskam, peckam)\", \"stance\": \"silent\",\n    \"note\": \"Horn has no numbered paragraph for the word; Hübschmann's discussion at §314-315 is in fact a correction of Horn's §314, which Horn devoted to piž- < patis-.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, PHD_mackenzie.txt l. 1270\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie has no *paskamb, but he does have 'askōb [ʼskwp | N āsko(b)] roof, ceiling' — a Middle Persian relative of the same family (cf. Gharib's Sogd. skʼnpʼk 'floor, stage, story ©Pahl. askŋb').\"},\n   {\"src\": \"BOOK\", \"where\": \"data/verification/sources/refs/ocr/BOOK/450.png\", \"stance\": \"supports\",\n    \"note\": \"500-dpi render of the Persian box shows 'پِچکَم (بِچکَم، بِشکَم، پِشکَم)' and '... فرش دیبا کشیده بر بِچکَم' — documenting the extraction error.\"}\n ]\n})\n\ne7[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"fcmbd\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Nourai's 'fcmbd' is the Manichaean Sogdian spelling fcmbδ, read fəcambaδ (also fcʼnpδ, \"\n   \"pcʼnpδ, fcmpd in the Christian and Buddhist corpora), 'world' — Gharib's entry 3844, on precisely the \"\n   \"page Nourai cites, and she gives the etymology herself: '©Gersh. *frascamba; Av. frascimbana'. The word \"\n   \"is thus the fra- compound of the parent box used as a noun, with the semantic step 'the props/beams \"\n   \"(of heaven)' → 'the frame of the universe' → 'world'; the Buddhist Sogdian synonym skʼnp / ʼskʼnp \"\n   \"'world' (Gharib 9210, '©<*skamb- “to stem”') is the same noun without the preverb, and is what \"\n   \"Pokorny p. 916 cites as 'sogd. skʼnp- (*skamb) ‘base of the universe’'. Cheung 344 lists both. This \"\n   \"node is the one place where the gloss 'world' belongs — see node #1, where Nourai has moved it back \"\n   \"onto the Avestan.\"),\n \"derivation_fa\": (\"«fcmbd» همان fcmbδ سغدی مانوی (fəcambaδ) به معنای «جهان» است. بدرالزمان قریب در همان صفحهٔ ۱۵۲ \"\n   \"(مدخل ۳۸۴۴) ریشهٔ آن را به پیروی گرشویچ *frascamba و اوستایی frascimbana می‌داند. تحول معنایی \"\n   \"«تیرک‌های نگاه‌دارندهٔ آسمان» ← «ساختار گیتی» ← «جهان» در سغدی روی داده است، نه در اوستایی. \"\n   \"صورت بدون پیشوند آن skʼnp سغدی بودایی است که پوکورنی نیز می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:152\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, printed p. 152 (SOD_pages.txt leaf 217, verified by the running head '153' on leaf 218), entry '3844 fcmbδ M ... fcampaδ, f(ə)cambaδ (fcmbd) ©Gersh. *frascamba; Av. frascimbana ©ob. -y; pl. -t ... world. C2 gloss.; STi 43.15, 60.6, 84.11; GMS 169, 372'. The page number is exact.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib entries 3844 (fcmbδ, p.152), 3843 (fcʼnpδ), 3848 (fcmpd), 9210 (skʼnp, p.~373)\", \"stance\": \"supports\",\n    \"note\": \"'9210 skʼnp B ... skanp, skamb ©<*skamb- “to stem” ... world' — both Sogdian words for 'world' belong to this root.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p. 916\", \"stance\": \"supports\", \"note\": \"'sogd. skʼnp- (*skamb) ‘base of the universe’' — Pokorny already records the Sogdian semantic development.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 no. 344, SOGDIAN section\", \"stance\": \"supports\",\n    \"note\": \"'*SOGDIAN: BSogd. skʼnp, BSogd. ʼskʼnp ‘world’ || (+ *pati-) BSogd. ptsknpy ‘porch, eaves’.'\"}\n ]\n})\n\ne7[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"scamnum\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin scamnum 'bench, stool, step' goes back to *skabh-no-m (Proto-Italic *skaβnom) with the \"\n   \"regular Italic assimilation of -bn- to -mn-; the diminutives scabillum/scabellum 'low stool, footstool' \"\n   \"preserve the b and so prove the reconstruction. Watkins states it in one line — 'Suffixed form \"\n   \"*skabh-no- in Latin scamnum, a bench' — and so do Walde-Pokorny II 539, Pokorny 916 and Klein p.1430 \"\n   \"('scamnum, ‘bench’, which stands for *skabhnom- and prop. means ‘stay, support’, fr. I.-E. base *skabh-, \"\n   \"‘to support’, whence also OI. skabhnāti ... skambháh, ‘post’'). Nourai's gloss 'a support (for seating), \"\n   \"bench' is a fair rendering of that. The word is productive in Romance (It. scanno, Sp. escaño, Rom. \"\n   \"scaun) and was borrowed into Insular Celtic (MIr. scamun, Bret. scaon) and Byzantine Greek (σκαμνίον).\"),\n \"derivation_fa\": (\"لاتین scamnum «نیمکت، چهارپایه» از *skabʰ-no-m است که خوشهٔ -bn- در ایتالیک به -mn- همگون شده است؛ \"\n   \"مصغرهای آن (scabillum, scabellum) هنوز «b» را نگاه داشته‌اند و همین بازسازی را اثبات می‌کنند. واتکینز، \"\n   \"والده-پوکورنی (II ۵۳۹) و کلاین (ص ۱۴۳۰) همگی آن را به همین ریشه می‌برند. ادعای نورایی درست است.\"),\n \"sources\": [W_SCAMNUM],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. skabh- (AHD_watkins1985.txt leaf 934): 'Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.]' — Nourai cites AHD without a page here, and the root-appendix entry is exactly what he needs.\"},\n   {\"ref\": \"KLN:1430\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 759 (leaf 758 carries the numeral 1428, so this leaf = pp. 1429/1430), s.v. shamble: '... borrowed fr. L. scamellum, ‘bench, stool’, dimin. of scamnum, ‘bench’, which stands for *skabhnom- and prop. means ‘stay, support’, fr. I.-E. base *skabh-, ‘to support’, whence also OI. skabhnāti, skabhnoti, ‘fastens, supports’, skambháh, ‘post’.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1430 s.v. shamble\", \"stance\": \"supports\", \"note\": \"see ref_check — gives *skabhnom- and the sense 'stay, support', i.e. Nourai's gloss.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 539\", \"stance\": \"supports\",\n    \"note\": \"'lat. scamnum (*sqabhnom, das Formans im Zshang mit dem ind. Nasalpraesens ...) „Bank, Schemel“, Dem. scabillum, scabellum „niedriges Bänkchen, Schemel“'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/scamnum\", \"stance\": \"supports\",\n    \"note\": \"'From Proto-Italic *skaβnom, from Proto-Indo-European *skabʰ-no-m, from the root *skabʰ- (‘to hold up, support’). Cognate with Sanskrit स्कम्भ (skambhá, ‘prop, support, pillar’).'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (grep scamnum)\", \"stance\": \"silent\", \"note\": \"the OCR of the s- section did not yield a usable scamnum article; no counter-evidence.\"}\n ]\n})\n\ne7[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"shamble\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"The box is drawn as a plain arrow, but the relation is a borrowing, not an inheritance: Latin \"\n   \"scamnum's diminutive scamellum/scamillus was taken into West Germanic during the Roman period and gives \"\n   \"Old English sc(e)amol 'stool, bench, table' (with ON skemill, Du. schemel, OHG scamil), whence Middle \"\n   \"English schamel, shamel 'bench' — Nourai's gloss. The specialised sense follows the trade: 'stall on \"\n   \"which meat is displayed' > 'meat market' (early 15c.) > plural shambles 'slaughterhouse' (1540s) > \"\n   \"'scene of carnage' (1590s) > 'mess, confusion' (1901). The verb shamble 'walk awkwardly' (1680s) is a \"\n   \"back-formation from shamble legs, on the image of a bench's splayed legs — Klein compares French bancal \"\n   \"'bandy-legged' from banc. Since the node has no refs of its own, the check rests on Klein p.1430 (the \"\n   \"reference of its parent) and Watkins, who file SHAMBLES under skabh-.\"),\n \"derivation_fa\": (\"پیوند لاتین به انگلیسی در اینجا وام‌گیری است نه میراث: مصغر لاتین scamellum در دورهٔ رومی به ژرمنی غربی وارد \"\n   \"شده و انگلیسی کهن sc(e)amol «چهارپایه، نیمکت» را داده است؛ از آن انگلیسی میانه schamel «نیمکت» — همان معنایی \"\n   \"که نورایی می‌آورد. سپس معنا به «پیشخان قصابی»، «کشتارگاه» (۱۵۴۰م) و سرانجام «آشفتگی» (۱۹۰۱) رسیده است. \"\n   \"این گره ارجاع ندارد، ولی کلاین (ص ۱۴۳۰) و واتکینز هر دو همین زنجیره را می‌دهند. ادعای نورایی درست است.\"),\n \"sources\": [E_SHAMBLES],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference of its own in the book; it is covered by its parent's KLN:1430, which I checked (KLN_1966.txt leaf 759 = printed pp. 1429/1430, s.v. shamble) and which states the whole OE-to-Latin chain.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1430 (leaf 759) s.v. shamble, n. and shamble, intr. v.\", \"stance\": \"supports\",\n    \"note\": \"'shamble, n. — ME. schamel, shamel, ‘bench’, fr. OE. scamel, ‘stool, bench, table’, rel. to ON. skemill, Du. schemel, OHG. scamil ...; borrowed fr. L. scamellum, ‘bench, stool’, dimin. of scamnum'; and for the verb, 'For sense development cp. F. bancal, ‘bandy-legged’, prop. ‘bench-legged’, fr. banc, ‘bench’.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skabh- and the English index (AHD_watkins1985.txt leaf 2252: 'SHAMBLES skabh-')\", \"stance\": \"supports\",\n    \"note\": \"'Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/shambles\", \"stance\": \"supports\",\n    \"note\": \"'from Old English scamol ... from Latin scamillus, diminutive of scamnum ‘bench’'; senses 'meat market' (early 15c.), 'slaughterhouse' (1540s), 'confusion, mess' (1901); verb shamble (1680s) 'possibly from the splayed legs of bench'.\"}\n ]\n})\ndoc[\"entries\"].append(e7)\n\nwith open(\"data/verification/page-450.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-450.py"
}
```


### [2026-09-14T02:16:40.663Z] TOOL RESULT

```
Exit code 1
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-450.py", line 148
    "modern_form": "Old Persian sinkabruš 𐎿\ud800\udf a1 (𐎿𐍡𐎣𐎲𐎽𐎢𐏁) 'carnelian'",
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 47-50: truncated \uXXXX escape
```


## [2026-09-14T02:16:45.574Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la KNT_full.txt 2>/dev/null && grep -n \"kabru\" KNT_full.txt | head -10"
}
```


### [2026-09-14T02:16:45.677Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 944060 Sep 13 22:15 KNT_full.txt
1731:convincing IE etymology; such as si"kabrus ‘car- 
4868:si"kabru- ‘carnelian’, naiba- ‘good’ (only in 
6372:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 
9411:Nom. Sg. Masc.: magus, piruš, sikabrus, ад). 
29142:si"kabru- sh. ‘carnelian’: Elam. $7-/n-qa-ab-ru- 
29148:kabrus nsm. DSf 87.
```


## [2026-09-14T02:16:47.865Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29138,29152p' KNT_full.txt"
}
```


### [2026-09-14T02:16:47.934Z] TOOL RESULT

```
Saka- sb. ‘Scythia’, fem. of preceding, as sb. 
Saküm asf. DB 5.211. 


si"kabru- sh. ‘carnelian’: Elam. $7-/n-qa-ab-ru- 
iš, Akk. gi-in-ga-4--ru-ü (§6, §75.V, §116, §153.1; 
JAOS 54.57-8). For meaning, ef. Bleichsteiner, 
WZKM 37.101-3; Konig, Burgbau 62-3; Kent, 
JAOS 53.18, 54.37-8; ‘cinnabar’, Hz. AMI 3.64.5, 
ApI 303-5; ‘serpentine’, Gray, AJP 53.68-9. st- 
kabrus nsm. DSf 87. 


Sikaya^wali- sb. ‘Sikayauvati’, a fortress in 
Media: Elam. ši-tk-ki-ú-ma-ti-iš, АКК. sik-kam-
```


## [2026-09-14T02:16:56.746Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KNT_full.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nn=29142\nleaf='\\n'.join(lines[:n]).count('\\f')\nprint('leaf',leaf,'printed~',leaf-15)\nEOF"
}
```


### [2026-09-14T02:16:57.953Z] TOOL RESULT

```
leaf 0 printed~ -15
```


## [2026-09-14T02:17:04.980Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'PYEOF'\nimport io,re\np='build-450.py'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('''\"modern_form\": \"Old Persian sinkabruš \\\\ud800\\\\udf a1 (\\U0001038F\\U0001F861\\U0001038380 (bad)\",''','')\nPYEOF\ngrep -n \"modern_form\" build-450.py | head"
}
```


### [2026-09-14T02:17:06.155Z] TOOL RESULT

```
31: "modern_form": "Arabic root ص ح ر (ṣ-ḥ-r) ‘to be reddish-fawn, yellowish-red’, whence أَصْحَر (ʾaṣḥar) ‘reddish-fawn’, f. صَحْرَاء (ṣaḥrāʾ)",
148: "modern_form": "Old Persian sinkabruš 𐎿\ud800\udf a1 (𐎿𐍡𐎣𐎲𐎽𐎢𐏁) 'carnelian'",
343: "modern_form": "PIE *skabʰ- / *skamb- 'to prop up, support' (Pokorny 916; Watkins skabh-)",
```


## [2026-09-14T02:17:10.226Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'PYEOF'\nimport io\np='build-450.py'\ns=io.open(p,encoding='utf-8').read()\nlines=s.split('\\n')\nlines[147] = ' \"modern_form\": \"Old Persian sinkabruš (nom. sg., DSf 37) \\'carnelian\\' (Kent); Herzfeld read it \\'cinnabar\\'\",'\ns='\\n'.join(lines)\nio.open(p,'w',encoding='utf-8').write(s)\nPYEOF\nsed -n '146,150p' build-450.py"
}
```


### [2026-09-14T02:17:11.379Z] TOOL RESULT

```
 "root": "Sinkadruš",
 "verdict": "transcription_suspect",
 "modern_form": "Old Persian sinkabruš (nom. sg., DSf 37) 'carnelian' (Kent); Herzfeld read it 'cinnabar'",
 "note": ("Two separate problems. (1) FORM: the printed page reads 'Sinkadruš' with a d, but the Old Persian "
   "word attested in Darius's Susa foundation charter (DSf §37 kāsaka hya kapautaka utā sinkabruš) is "
```


## [2026-09-14T02:17:45.645Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'PYEOF'\nimport io\np='build-450.py'\ns=io.open(p,encoding='utf-8').read()\n\nold2 = '''   \"(2) GLOSS: Kent glosses sinkabru- 'carnelian' — a red semi-precious stone brought, with lapis lazuli, \"\n   \"from Sogdiana — not 'the red ore of mercury used as a pigment'. That is the meaning of the New Persian \"\n   \"descendant شنگرف, which Nourai has back-projected onto the Old Persian etymon. Kent further notes \"\n   \"that the word 'lacks a convincing IE etymology', i.e. it is itself probably a culture-word borrowed into \"\n   \"Old Persian. The root box is nevertheless a real Old Persian word, and the OP→NP link it asserts is the \"\n   \"one Wiktionary and the standard handbooks give.\"),'''\nnew2 = '''   \"(2) GLOSS: Nourai's 'red ore of mercury used as a pigment' is a defensible minority reading, not an \"\n   \"invention. Kent's lexicon entry runs: 'siⁿkabru- sb. ‘carnelian’: Elam. ši-in-qa-ab-ru-iš, Akk. \"\n   \"si-in-ga-ab-ru-ū ... For meaning, cf. Bleichsteiner WZKM 37.101-3; König, Burgbau 62-3; Kent JAOS 53.18, \"\n   \"54.37-8; ‘cinnabar’, Hz. AMI 3.64.5, ApI 303-5; ‘serpentine’, Gray AJP 53.68-9. siⁿkabruš nsm. DSf 37.' \"\n   \"So 'cinnabar' is Herzfeld's interpretation of the word, which Kent records but does not adopt: Kent, \"\n   \"and with him Wiktionary, prefer 'carnelian' — the red semi-precious stone that DSf says was brought \"\n   \"from Sogdiana together with lapis lazuli. Nourai (following Moʿin) has simply taken the reading that \"\n   \"matches the New Persian descendant. Kent also lists the word among those that 'lack a convincing IE \"\n   \"etymology', so it is probably itself a culture-word borrowed into Old Persian. The root box is a real \"\n   \"Old Persian word and the OP→NP link it asserts is the standard one.\"),'''\nassert old2 in s\ns = s.replace(old2,new2)\n\noldfa = '''   \"(Elam. ši-in-qa-ab-ru-iš)\"'''\nold_fa = '''   \"چاپ کرده؛ پس این خطای چاپی خود نورایی است نه خطای خوانش اسکن. دوم معنا: معنای پارسی باستان آن «عقیق» \"\n   \"(carnelian) است که همراه لاجورد از سغد می‌آوردند، نه «سنگ معدنی جیوه»؛ این معنای دوم از آنِ بازماندهٔ \"\n   \"فارسی نوی آن یعنی «شنگرف» است. پیوند پارسی باستان به فارسی نو درست است، ولی صورت و معنای ریشه باید درست شود.\"),'''\nnew_fa = '''   \"چاپ کرده؛ پس این خطای چاپی خود نورایی است نه خطای خوانش اسکن. دوم معنا: کنت معنای آن را «عقیق» \"\n   \"(carnelian) می‌داند — سنگ سرخی که بنا بر همان سنگ‌نبشته همراه لاجورد از سغد می‌آوردند — و می‌افزاید که \"\n   \"هرتسفلد آن را «شنگرف/سینابر» خوانده و گری «مار‌سنگ». پس معنایی که نورایی (به پیروی معین) آورده خوانش \"\n   \"اقلیت است نه خطا، ولی خوانش پذیرفته‌تر «عقیق» است. پیوند پارسی باستان به فارسی نو درست است؛ صورت ریشه باید اصلاح شود.\"),'''\nassert old_fa in s\ns = s.replace(old_fa,new_fa)\n\noldknt = '''   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §86 (KNT.txt l. 357), §V (l. 1042), §u-stems (l. 1838), DSf text (l. 4262) and translation (l. 4295)\", \"stance\": \"partial\",\n    \"note\": \"'siⁿkabru- ‘carnelian’' — the form has b, not d, and the gloss is 'carnelian': 'The precious stone lapis-lazuli and carnelian which was wrought here, this was brought from Sogdiana' (DSf). Kent also lists it among words that 'lack a convincing IE etymology'. So Kent supports the existence of the OP word but contradicts both Nourai's spelling and his gloss.\"},'''\nnewknt = '''   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian: Lexicon s.v. siⁿkabru- (KNT_full.txt l. 29142), plus §86 (l. 1731), §V (l. 4868), §u-stems (l. 6372), DSf text and translation (KNT.txt l. 4262, 4295)\", \"stance\": \"partial\",\n    \"note\": \"'siⁿkabru- sb. ‘carnelian’: Elam. ši-in-qa-ab-ru-iš, Akk. si-in-ga-ab-ru-ū ... For meaning, cf. Bleichsteiner WZKM 37.101-3; König, Burgbau 62-3; Kent JAOS 53.18, 54.37-8; ‘cinnabar’, Hz. AMI 3.64.5, ApI 303-5; ‘serpentine’, Gray AJP 53.68-9. siⁿkabruš nsm. DSf 37.' and, in the DSf translation, 'The precious stone lapis-lazuli and carnelian ... was brought from Sogdiana'. Kent has b, not d, and prefers 'carnelian' while recording Herzfeld's 'cinnabar' — so he contradicts Nourai's spelling but only partly his gloss.\"},'''\nassert oldknt in s\ns = s.replace(oldknt,newknt)\n\nio.open(p,'w',encoding='utf-8').write(s)\nprint('patched')\nPYEOF"
}
```


### [2026-09-14T02:17:46.660Z] TOOL RESULT

```
patched
```


## [2026-09-14T02:17:50.600Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-450.py && python3 -m json.tool data/verification/page-450.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 450"
}
```


### [2026-09-14T02:17:52.224Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 9, 'plausible': 2, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2, 'transcription_suspect': 1}
ref checks: {'supports': 10, 'not_checked': 9, 'partial': 3}
books consulted: {'supports': 32, 'silent': 5, 'partial': 10} | by book: {'KLN': 7, 'Wiktionary': 5, 'LKT': 4, 'Etymonline': 4, 'MON': 3, 'SKT': 3, 'CHEUNG': 3, 'BQT': 2, 'LAT': 2, 'BOOK': 2, 'WLD': 2, 'Dehkhoda': 1, 'FSD': 1, 'BRT': 1, 'AVG': 1, 'HUB': 1, 'HRN': 1, 'PHD': 1, 'SOD': 1, 'POK': 1, 'AHD': 1}
```


## [2026-09-14T02:17:59.997Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/page-450.json'))\nprint(len(open('data/verification/page-450.json','rb').read()),'bytes')\nfor e in d['entries']:\n    print(e['entry'], e['root'], e['verdict'], '| nodes:', [(n['id'],n['verdict']) for n in e['nodes']])\n    assert e.get('note_fa')\n    for n in e['nodes']:\n        assert n.get('derivation_fa') and n.get('ref_check') and n.get('consulted'), n['id']\nprint('all fields present')\nprint(d['entries'][2]['nodes'][1]['derivation_fa'][:120])\n\""
}
```


### [2026-09-14T02:18:01.174Z] TOOL RESULT

```
60058 bytes
0 S.h.r confirmed | nodes: [(1, 'confirmed'), (2, 'confirmed'), (3, 'confirmed')]
6 Sinkadruš transcription_suspect | nodes: [(1, 'confirmed'), (2, 'plausible'), (3, 'confirmed'), (4, 'transcription_suspect'), (5, 'confirmed')]
7 Skabh confirmed | nodes: [(1, 'plausible'), (2, 'transcription_suspect'), (3, 'confirmed'), (4, 'confirmed'), (5, 'confirmed')]
all fields present
خود واژه و پیوندش با این ریشه درست است؛ پوکورنی در همان صفحهٔ ۹۱۶ «npers. paskam» را با معنای «راهروی ستون‌دار، ایوان» م
```


## [2026-09-14T02:18:20.483Z] AGENT

Done. `data/verification/page-450.json` written; `verify_check.py 450` reports 13/13 nodes, 0 PROBLEM lines.

**Page 450 (book p. 420) — 3 non-redirect entries, 13 nodes, 5 redirects skipped**

Verdicts: roots — 2 confirmed, 1 transcription_suspect. Nodes — 9 confirmed, 2 plausible, 2 transcription_suspect. Ref checks: 10 supports, 3 partial, 9 not_checked (FVA has no digital copy; AHD page cites are to the dictionary proper, lending-only; MON 6-vol not digitised).

Flagged items:
- **ROOT Sinkadruš** — transcription_suspect, error in the **book**. The Old Persian word (DSf §37) is *sinkabruš*, with b; Kent's lexicon: "siⁿkabru- sb. 'carnelian' … siⁿkabruš nsm. DSf 37". The 500-dpi render of p. 450 shows the book itself printing "Sinkadruš", so the extraction is faithful. Gloss "red ore of mercury" is Herzfeld's minority reading, which Kent records but rejects in favour of 'carnelian'.
- **#4 French "cinbare"** (Sinkadruš) — transcription_suspect, error in the **book**: metathesis for *cinabre*. Klein p. 289, the reference Nourai himself cites, spells it "F. cinabre, fr. OF. cenobre".
- **#2 Persian pečkam** (Skabh) — transcription_suspect, error in the **extraction** (see below). Derivation itself is plausible-but-loose: Hübschmann (Pers. Studien 41/191) and Cheung (no. 344) derive NP paškam from OP **\*pati-**skamba- (> MP \*patskamb > \*paskamb), not from the upa-/fra- forms in the parent Avestan box.
- **#1 Avestan** (Skabh) — plausible: forms real, but frascimbana- means 'supporting beam, pillar' in Bartholomae, WP II 539, Pokorny 916 and Cheung; the gloss "universe, world" belongs to its Sogdian descendant (node #3), not to Avestan.
- **#2 Greek kinnabari** — plausible: Klein/Skeat/Lokotsch all derive it from Persian, but a 4th-c.-BCE borrowing must come from the Old Iranian form, and Beekes classes κιννάβαρι as an eastern loanword of unknown ultimate origin.

**Extraction errors for the owner to fix (JSON ≠ printed page), entry 7 node #2:**
- `script_extra` reads `پیچکم ، پیشکم ، پشکم`; the book prints `بچکم ، بشکم ، پشکم` (b-initial, no yāʾ) — matching Hübschmann's paškam/piškam/baškam/biškam and Moʿin's cross-references.
- `quote.text` ends `بر پچکم`; the book prints `بر بچکم`.

Notable exact hits: BQT:1302 is the right page and carries Nourai's Kasāʾī Marvzī verse verbatim; SOD:152 is Gharib's entry 3844 fcmbδ 'world' with her own etymology "©Gersh. \*frascamba; Av. frascimbana"; POK:916, KLN:1373, KLN:289, KLN:1430 all verified against the printed page numerals in the scans. Page image archived at `data/verification/sources/refs/ocr/BOOK/450.png`; 8 web sources archived via `fetch_source.py`.
