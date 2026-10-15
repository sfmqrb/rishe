# Verification process log — verify-page-510


## [2026-10-15T02:44:16.431Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 510 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-510.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-510.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-510.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 510` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.502Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.101Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.137Z] TOOL RESULT

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


## [2026-10-15T02:44:19.610Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-510.txt"
}
```


### [2026-10-15T02:44:19.661Z] TOOL RESULT

```
1	=== PDF page 510 (book page 480) ===
2	--- entry 0 ---
3	ROOT [Chinese] Tien : store, shop  (refs ETM:63)
4	#1 (parent #0) [Sogdian] refs=ETM:63; SOD:394 | bazaar, inn
5	  #2 (parent #1) [Persian] refs=ETM:63; MON; BQT:547 | tîm «تیم ۱» : bazaar, caravansary | extra: تیمچه
6	--- entry 1 ---
7	ROOT [Indo-European] Titi, Titil : imitation of a bird song  (refs POK:1086)
8	#1 (parent #0) [Sanskrit] refs=POK:1086 | tittibha : a water bird
9	  #2 (parent #1) [Persian] refs=BQT:1364 | tîtŭ «تیتو» : a water bird | extra: طیتو
10	#3 (parent #0) [Latin] refs=POK:1086 | titiô : sparrow
11	--- entry 2 ---
12	ROOT Titil -> redirect to Titi
13	--- entry 3 ---
14	ROOT [Avestan] Tkaeša : agreement, commitment  (refs BQT:1755; HRN:196)
15	#1 (parent #0) [Pahlavi] refs=MON:3153 | kěš : religious belief, religion
16	  #2 (parent #1) [Persian] refs=HRN:196; BQT:1755; MON:3153 | kîš 3 «کیش ۳» : religion
17	--- entry 4 ---
18	ROOT [Arabic] T.L.S : to wipe out, clean  (refs KLN:122; SAP:964)
19	#1 (parent #0) [Arabic] refs=SAP:964 | atlas : a wiped, clean silk cloth
20	  #2 (parent #1) [Persian] refs=MON | atlas «اطلس ۴» : silk or satin cloth
21	  #3 (parent #1) [English] refs=KLN:122 | atlas 2 : silk, satin
22	--- entry 5 ---
23	ROOT To -> redirect to So
24	--- entry 6 ---
25	ROOT Tôgei -> redirect to Tôkei
26	
```


## [2026-10-15T02:44:20.393Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-510.json"
}
```


### [2026-10-15T02:44:20.467Z] TOOL RESULT

```
1	{
2	  "pdf_page": 510,
3	  "book_page": 480,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Tien",
8	        "lang": "Chinese",
9	        "refs": "ETM:63",
10	        "gloss": "store, shop"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Sogdian",
17	          "refs": "ETM:63; SOD:394",
18	          "words": [
19	            {"translit": "bazaar, inn", "gloss": null, "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "ETM:63; MON; BQT:547",
29	          "words": [
30	            {"translit": "tîm", "gloss": "bazaar, caravansary", "script": "تیم ۱"}
31	          ],
32	          "script_extra": "تیمچه",
33	          "note": null,
34	          "quote": {"text": "من ز تیم تو بتیمار گرفتار شدم - تو بتیمار مهل باز بتیم ۱ آر مرا", "poet": "Farhang Fors"}
35	        }
36	      ]
37	    },
38	    {
39	      "root": {
40	        "name": "Titi, Titil",
41	        "lang": "Indo-European",
42	        "refs": "POK:1086",
43	        "gloss": "imitation of a bird song"
44	      },
45	      "nodes": [
46	        {
47	          "id": 1,
48	          "parent": 0,
49	          "lang": "Sanskrit",
50	          "refs": "POK:1086",
51	          "words": [
52	            {"translit": "tittibha", "gloss": "a water bird", "script": null}
53	          ],
54	          "note": null,
55	          "quote": null
56	        },
57	        {
58	          "id": 2,
59	          "parent": 1,
60	          "lang": "Persian",
61	          "refs": "BQT:1364",
62	          "words": [
63	            {"translit": "tîtŭ", "gloss": "a water bird", "script": "تیتو"}
64	          ],
65	          "script_extra": "طیتو",
66	          "note": null,
67	          "quote": null
68	        },
69	        {
70	          "id": 3,
71	          "parent": 0,
72	          "lang": "Latin",
73	          "refs": "POK:1086",
74	          "words": [
75	            {"translit": "titiô", "gloss": "sparrow", "script": null}
76	          ],
77	          "note": null,
78	          "quote": null
79	        }
80	      ]
81	    },
82	    {
83	      "root": {
84	        "name": "Titil",
85	        "redirect": "Titi"
86	      },
87	      "nodes": []
88	    },
89	    {
90	      "root": {
91	        "name": "Tkaeša",
92	        "lang": "Avestan",
93	        "refs": "BQT:1755; HRN:196",
94	        "gloss": "agreement, commitment"
95	      },
96	      "nodes": [
97	        {
98	          "id": 1,
99	          "parent": 0,
100	          "lang": "Pahlavi",
101	          "refs": "MON:3153",
102	          "words": [
103	            {"translit": "kěš", "gloss": "religious belief, religion", "script": null}
104	          ],
105	          "note": null,
106	          "quote": null
107	        },
108	        {
109	          "id": 2,
110	          "parent": 1,
111	          "lang": "Persian",
112	          "refs": "HRN:196; BQT:1755; MON:3153",
113	          "words": [
114	            {"translit": "kîš 3", "gloss": "religion", "script": "کیش ۳"}
115	          ],
116	          "note": null,
117	          "quote": {"text": "لب یاقوت رنگ و نالهٔ چنگ - می لعلگون و کیش ۳ زرتهشتی", "poet": "Daqîqî Tŭsî"}
118	        }
119	      ]
120	    },
121	    {
122	      "root": {
123	        "name": "T.L.S",
124	        "lang": "Arabic",
125	        "refs": "KLN:122; SAP:964",
126	        "gloss": "to wipe out, clean"
127	      },
128	      "nodes": [
129	        {
130	          "id": 1,
131	          "parent": 0,
132	          "lang": "Arabic",
133	          "refs": "SAP:964",
134	          "words": [
135	            {"translit": "atlas", "gloss": "a wiped, clean silk cloth", "script": null}
136	          ],
137	          "note": null,
138	          "quote": null
139	        },
140	        {
141	          "id": 2,
142	          "parent": 1,
143	          "lang": "Persian",
144	          "refs": "MON",
145	          "words": [
146	            {"translit": "atlas", "gloss": "silk or satin cloth", "script": "اطلس ۴"}
147	          ],
148	          "note": null,
149	          "quote": null
150	        },
151	        {
152	          "id": 3,
153	          "parent": 1,
154	          "lang": "English",
155	          "refs": "KLN:122",
156	          "words": [
157	            {"translit": "atlas 2", "gloss": "silk, satin", "script": null}
158	          ],
159	          "note": null,
160	          "quote": null
161	        }
162	      ]
163	    },
164	    {
165	      "root": {
166	        "name": "To",
167	        "redirect": "So"
168	      },
169	      "nodes": []
170	    },
171	    {
172	      "root": {
173	        "name": "Tôgei",
174	        "redirect": "Tôkei"
175	      },
176	      "nodes": []
177	    }
178	  ]
179	}
180	
```


## [2026-10-15T02:44:23.942Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; ls | tail -5; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['ETM','SOD','MON','BQT','POK','HRN','KLN','SAP','WLD','AHD','HUB','PHD','NYB','ARY','SKT','BRT','IEC','SYN','CHEUNG','LKT','FSD','WEB','PLA','AFM','FVQ']:\n  print(k, {x:d.get(k,{}).get(x) for x in ['kind','local_file','page_offset','lookup_hint']})\n\""
}
```


### [2026-10-15T02:44:24.516Z] TOOL RESULT

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
ETM {'kind': 'catalog', 'local_file': None, 'page_offset': None, 'lookup_hint': 'Searched archive.org, ketabnak, noorlib, web: not found.'}
SOD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}"}
MON {'kind': 'website+archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
POK {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
HRN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
SAP {'kind': 'purchase', 'local_file': None, 'page_offset': None, 'lookup_hint': "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages)."}
WLD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
HUB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
PHD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
ARY {'kind': 'local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
SKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
BRT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
IEC {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
SYN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
CHEUNG {'kind': None, 'local_file': None, 'page_offset': None, 'lookup_hint': None}
LKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
FSD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
WEB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
PLA {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'], 'page_offset': '301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).', 'lookup_hint': 'HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)'}
AFM {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'], 'page_offset': "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", 'lookup_hint': "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."}
FVQ {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)', 'lookup_hint': 'Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).'}
```


## [2026-10-15T02:44:27.037Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/page-5*.json; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));print(json.dumps(d,ensure_ascii=False,indent=1)[:5000])\"; sed -n 1,200p tools/verify_check.py | grep -n -i -E 'PROBLEM|def |required|source' | head -60"
}
```


### [2026-10-15T02:44:27.823Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
.rw-r--r--   99k sfmqrb 14 Oct 22:14  data/verification/page-51.json
.rw-r--r--   50k sfmqrb 14 Oct 22:14  data/verification/page-52.json
.rw-r--r--   53k sfmqrb 14 Oct 22:14  data/verification/page-53.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-54.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  data/verification/page-55.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-56.json
.rw-r--r--   58k sfmqrb 14 Oct 22:14  data/verification/page-57.json
.rw-r--r--   79k sfmqrb 14 Oct 22:14  data/verification/page-58.json
.rw-r--r--   75k sfmqrb 14 Oct 22:14  data/verification/page-59.json
{
 "pdf_page": 499,
 "book_page": 469,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-10-14",
 "entries": [
  {
   "entry": 0,
   "root": "Tel",
   "verdict": "confirmed",
   "modern_form": "PIE *telh₂- 'to lift, bear, weigh; endure' (Pokorny 1. tel-, telə-, tlē-, tlā- 1060-1061; Watkins/AHD telə-; LIV² 622-623)",
   "note": "Pokorny IEW pp.1060-1061 heads the entry '1. tel-, telə-, tle(i)-, tlā-' 'to transport, carry; to bear, suffer', Watkins (AHD) 'telə- to lift, support, weigh', modern notation *telh₂-. Nourai's 'Tel : to lift', the label Indo-European and both his citations (POK:1060; KLN:122 = Klein s.v. Atlas, which spells out the base *tel-, *tal-, *tol- 'to bear, lift, suffer') are correct. The Greek, Latin, Sanskrit and English branches are standard (Pokorny, Walde-Pokorny, Watkins, Klein all list them). Two Iranian/Persian problems: (1) the 'Avestan' tara-āz(u) is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word; (2) the Persian tarāz/طراز box mixes tarāzū 'balance' (correct) with ṭarāz/tarāz 'adornment' and the city Ṭarāz of Farrokhī's verse, and the Persian atlas 'world' (falak-e atlas) is native Arabic aṭlas 'plain, smooth', not Greek Atlas. Toll's Greek origin is contested (Wiktionary prefers a native Germanic word). No extraction errors: the JSON matches the printed page, including the odd ref 'MON5:5155' (a misprint in the book, presumably for MON5:155).",
   "note_fa": "ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-",
    "https://en.wiktionary.org/wiki/Ἄτλας",
    "https://en.wiktionary.org/wiki/τάλαντον"
   ],
   "ref_check": [
    {
     "ref": "POK:1060",
     "status": "supports",
     "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
    },
    {
     "ref": "KLN:122",
     "status": "supports",
     "note": "Klein 1966 (KLN_1966.txt leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τάλαντον, ... L. tollere 'to lift up, raise', tolerare 'to bear, support''."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I pp.738-740 s.v. 1. tel-",
     "stance": "supports",
     "note": "Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'."
    },
    {
     "src": "AHD",
     "where": "Watkins s.v. telə-",
     "stance": "supports",
     "note": "Watkins AHD Roots (local AHD_watkins1985.txt line 1078) s.v. telə-: 'To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment' — 2a 'Greek telos, tax, charge: TOLL1'; 2b 'Latin tolerare ... TOLERATE'; 4 '*tala-nt- in Greek talanton, balance, weight ... TALENT'; 6 'Perhaps zero-grade form *tla- in Greek Atlas ... ATLANTIC, ATLAS'; 8 '*tl-to- in Latin lātus ... RELATE ... TRANSLATE'; 9 '*tl-ā- in Sanskrit tulā, scales, balance, weight'; 10 '*tl-n-a- in Latin tollere'. [Pok. 1. tel- 1060.]"
    },
    {
     "src": "IEC",
     "where": "s.v. tl- (1) (line 18624)",
     "stance": "supports",
     "note": "'tl- (1) (tlō, tolō, iō) 'lift, raise, bear, suffer'. WP I, 701 & 738-9 ... Tokh. A B tal-, v. 'lift, carry'; Gk. tlēmi, aor. etlēn 'bear, support, suffer'; Lat. perf. (te)tulī; Go. þulan'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Sanskrit",
     "words": "tulâ, tulya",
     "verdict": "confirmed",
     "derivation": "Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo
16:def page_no(path):
20:def main(argv):
22:    missing_pages, problems = [], []
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
```


## [2026-10-15T02:44:39.077Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/510.jpg; R=data/verification/sources/refs; grep -n -i -E 'lemma: *titi|lemma: *tit' $R/POK_full.txt | head; grep -n -i -E '^ *(tym|tym.k|tymc)|inn\\b' $R/SOD_pages.txt | head -20"
}
```


### [2026-10-15T02:44:39.442Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   60k sfmqrb 14 Oct 22:15  site/pages/510.jpg
8407:      inn, rest house
8464:1617 Vy^k         B                   (Jj^^^^xJ^^j^                      inn, rest house
10698:     rest house, inn                                                      2407 (ync M                                                 jj
31834:                                                                        tym ^tymp^y
31837:                                                                         inn, resting place
31851:9739 ty2 B         (0^^^^)^^^^^*^                                       inn-keeper
33242:    5 '■'%XP?2ffiF^'7^;?:*F*!??Z7~Ki?:         ^4^r««isqp9wii!wiinn
38603: indefinable meaning        5705              inn 1598, 1628, 2391, 9747                  internal      3237, 3238, 3350, 3351,
38605: independent       1999, 8684, 8685           inn-keeper     9750                         interpreter          7275, 9683
```


## [2026-10-15T02:44:42.431Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 31820,31860p $R/SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR<=0' /dev/null; python3 -c \"\nt=open('$R/SOD_pages.txt').read().split('\\f')\nfor i,p in enumerate(t):\n  if '9747' in p and 'inn' in p: print('leaf',i)\n\"; grep -n -i 'titi' $R/POK_full.txt | head"
}
```


## [2026-10-15T02:44:42.527Z] TOOL CALL #8: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/510.jpg"
}
```


### [2026-10-15T02:44:42.815Z] TOOL RESULT

```
                                                          <cd >>
 9733 twz-     C => twz-
                                                                   9745 tyqws C =* tyk}ws-
 9734 twz>nk S                                            -elf,    9746 tym1                               ^A^O^O^
      tuzang, twazang ? ©MP        do-zang                                =»tymn
                                                                        tim (tymh) ©<*ati-ima-, <*ati-imi Yaghn. tint
      two-fold ?
         Sund. MSP p53-4, pi. tvfznku b30, 100                           still, yet, again, moreover
                                                                         S W, BSOAS 1975, 136; VJ pl21; TSP p274;
 9735 txm-      C                            x j^s «j\j&>- «u3*r
        taxm, tsxm ©nom. txmy% ace. /jemw; pi. txmt}                       BBB; KG pl90; MSP bl38; C2 p228; STii 6.6,
          =*twxmy, tym                                                     1.43; Sund. AoFviii 1981 p218; MDii p2l3;
        seed, descendant, child                                            Frag. Len.
        C2, 52R9, 54R27, 60R9                                      9747 tern
                                                                        tym ^tymp^y
                                                                             C                 (ot^<^)l^jl^<©l^b         <J^c*
 9736 txmy =* twxmy
                                                                         inn, resting place
9737 txyz- M, C                       *j*/jyl ^j^A
     toxez =*xwrtxyz, nVx txyz                                           STi 36.2; pi. tymu STii 3.27; Hen. LW
     (to)set, 0<?)go down                                          9748 tymh    B, S =* tym1
     BSTii 827.48: C2, 94V 18; GMS 662; Gersh.                     9749 tymn    B                                ojljxjyjxjl
       BSOAS 14, 1952, 488f; AVS 136
                                                                         timanagain,
                                                                         still, ^tym1then
9738 ty' S, C                                                 y
     te, ti ©<*tai ©2sg. pers. pron. gen. =4-t                           TSP; BSTBL; STii 7.6; -w, TSP 2.724, 741; Frag.
                                                                           Len.
     you, of you
     MDii p218; C2 p77.31, 31V3151V6,9                             9750 tymp^y C    (^j ^ cmJj^J)^>-<^I^a < jbl^ jU^
                                                                        tem-pase ©<*pa0raka
9739 ty2 B         (0^^^^)^^^^^*^                                       inn-keeper
     ti Ozwty) ©in compd. with pron. indf. adj. &
                                                                         STi 36.5, tem+ pase
          adv. =»ZY, >cwty, 'kwC-Jty, ^ty*, p>rwty
        emphatic particle                                          9751 tympn C                                       jy**^
        VJ pl21; TSP p273                                               timpan ?
                                                                        still, yet
9740 ty3 C                                                   ^
     tay -*ty, t'yh                                                     C2, 48R13; S W, BSOAS 1975, 132.139
     thief
leaf 461
leaf 560
2013:Jo- stem: Irish aige^race'. Old Indie in /7/:^a/7^ya/77 'competition'. 
2032:Gr. dycbv " race, competition '; ayuia 'street' (part. Perf.), from which about newer *aY£ia 
2088:French aisselle : Calabrese ma-scidda; sciddra; titiddra; titilla : Albanian Geg sqetlla, Tosc 
2890:References: Pedersen Groupement 20, Hittitisch 115, Tocharisch 227; Frisk Indo- 
3897:References: WP. I 34 f., WH. I 60, 848, Feist 18 f., Pedersen Hittitisch 128, Tocharisch 
5297:References: WP. I 60. Pedersen Hittitisch 183 f., Hendriksen Unters. 28, Benveniste 
7356:as resting places in the course of the sun {solstitium), then ' year, solstice, anniversary ' 
9347:References: WH. I 61, 65, 848, Feist 72, Trautmann 22, Pedersen Hittitisch 27, 164. 
11968:Old High German Old Saxon i6'a//rc»"balk, beam'; Old Icelandic it's/Zr/'" partition wall, dividing 
11969:off, partitioning off, i6'(?/Ar"dividing off, partitioning off;
```


### [2026-10-15T02:44:42.833Z] TOOL RESULT

```

```


## [2026-10-15T02:44:47.916Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==462' $R/SOD_pages.txt | head -5; awk 'BEGIN{RS=\"\\f\"} NR==462' $R/SOD_pages.txt | grep -n -E '^ *3[89][0-9] *$|39[0-9]'; grep -n -E 'lemma: *t[iī]' $R/POK_full.txt | head -30"
}
```


### [2026-10-15T02:44:48.349Z] TOOL RESULT

```
                                                                                                                         394
 twz-

           gloss.; Benv. BSL 1951, 39; twy'z, MDii p213;                 (to)Iook at
           AVS 138                                                       VJ pl20; TSP p273; C2, 12R10, 60R28, 60V2, 27
1:                                                                                                                         394
86829:Root / lemma: tieg"-
```


## [2026-10-15T02:44:50.182Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -E 'Page\\(s\\): *108[5-7]' $R/POK_full.txt; "
}
```


### [2026-10-15T02:44:50.610Z] TOOL RESULT

```
86950:Page(s): 1086-1087
```


## [2026-10-15T02:44:52.673Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 86930,86990p $R/POK_full.txt; grep -n -i -E 'titt?ibh|titio|tittib' $R/POK_0*.txt | head"
}
```


### [2026-10-15T02:44:53.069Z] TOOL RESULT

```
8. Old Indie e>-/ai/a/7/"tantus', Avestan ae-tavantds. from Indo Germanic *tauQt, tauont-; 
gr. hom. Tr|0(; (newer tsux;), laFot;; through influence of m. tc(Fo(vt)(; wurde das to 
erwartende *TC(Fa(T) to *tc(Fo(t), from which laFoq; here also after Szemerenyi Latin tantus 
(see above); compare Schwyzer Gr. Gr. 1 , 609 Anm. 5. 

9. Der ending from TO-cppa "inzwischen' (in addition compare o-cppa "solange as') 
perhaps to Tocharian A ku-pre, B kwri'W , ta-par(k)^ r\o^, yet'. 

10. Ein stem Indo Germanic //b- besides to- in Old Indie tya- "that, that bekannte', alb. 
5e(Gen. Dat. Sg. f.) etc. (s-from //■), Proto Norse ^Tt, Old Saxon //7//"dorthin' (Rosenfeld 



Forsch. under Fortschr. 29, 177); Lithuanian c/a'here\ c/on'here'; Old pers. /ya'weiclies, 
das', leg. taya{*to+jo), absents (Risch, Asiat. Stud. 8, 151 f.). 

maybe alb. a-ty, aty, atje 'there' 

References: WP. I 742 f., WH. I 721 f., II 644, 645 f., 648, Trautmann 31 1 ff., Vasmer 3, 
113, 128, Szemerenyi Gl. 35, 42 ff., Mayrhofer 1, 499. 
Page(s): 1086-1087 

Root / lemma: to-2 

Meaning: prefix 

See also: see above S. 71 and 129 (Messapic tabara) 

Page(s): 1 088 

Root / lemma: tolk"- 

Meaning: to speak 

Material: Latin loquor, -/" locutus sum 'speak, say, name'; 

Old Irish ad-t/uch- ^danken' (1. Sg. atluchui), to-t/uch-'b\6, beg, ask' {dotluchur); Old 
Church Slavic //b/rb {*tb/kb), russ. to/kb " interpretation, explanation' (Lithuanian tu/kas 
"Dolmetsch' is Slavic loanword). 

References: WP. 1 744 f., WH. I 821 , Vasmer 3, 1 15. 
Page(s): 1 088 

Root / lemma: tong-1{ *teng^ 

Meaning: to think, feel 

Material: Latin tonged, -e/ie'nosse, scire', pran. tong/W ^r\6t\6'; Oscan Ablat. tanginud 

"sententia' (Messapic loanword?); alb. /5/7^e 'resentment'; 

Gothic ^agkjan, l=>ahta^ think; consider ', Old Icelandic A'eAA/a "become aware, 
understand, comprehend, know' (jfc'eMr'pleasant'), Old High German denchen 'think'. Old 
English dencands.; Gothic t^ugkjan, f^uMa'seem, shine, appear, seem'. Old Icelandic 
Pykkja'ds., gefallen'. Old High German dunchen 'sh\ne, appear, seem'. Old English 
dyncands.; Gothic *t^agks' gratitude ', Old Icelandic t^gkki. " gratitude, contentedness ', 
Old High German dank' reasoning, thought, notion, gratitude ' Old English d5/7c 'thought, 
notion, emotion, contentedness, gratitude '; Middle High German danknseme. Old Danish 
taknem ' grateful '; 


data/verification/sources/refs/POK_03.txt:4667:Ai.  tittibha-  m.  ,Parra  jacana';  lett.  titühis,  titübite  ,Wasserla  f --^-^ tilvikas,  titilvtkas,  tiülvis  , Brachhuhn,  Schnepfe' ;  gr.  TiTvSiCtü  o/l       * ßitw  ,gackern  (vom  Rebhuhn,  der  Schwalbe');  lat.  titiöj  -äre    zw^i^^^ vom  Sperling';  lett.  titet  ,singen'.  TT?***»
```


## [2026-10-15T02:44:55.448Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 4655,4675p $R/POK_03.txt; grep -n -B2 -A6 'Ai. tittibha' $R/POK_full.txt | head -30; grep -n -i 'tittibha\\|titi-' $R/incoming/WLD/WLD_Bd1_pages.txt | head; grep -n -i 'tittibha' $R/WLD_band3.txt | head"
}
```


### [2026-10-15T02:44:55.867Z] TOOL RESULT

```
Gr.  ivrvTtag  Adv.,  II.  24,  163,  wenn  ,kauernd,  hockend'  bedeutend; vermutlich  aisl.  ßopta  f.  ,Ruderbank'  (,auf  der  gehockt  wird'),  ahd.  dofta f.,  mnd.  ducht  f.,  ags.  dofi  ds.  (wozu  aisl.  ßopti  m.  ,Mitruderer',  ags. ^edofta  , Genosse',  ahd.  gidufto  , Mitruderer,  Genosse*)  und  got.  piubjö jheimlich',  ßiubs  ,Dieb',  aisl.  pjöfr,  ags.  deof^  as.  thiof,  ahd.   diob  jDieh^ -^
lit.  tüpiü,  tüpti  ,sich  hinhocken,  in  die  Knie  setzen',  tüpiü,  tupUi ,hocken,  in  den  Knien  sitzen',  lett.  tupt  , hockend
WP.  I  714.
teus-  ,leeren';  tus-sko-,  -sk-io-  ,leer'.
Av.  Kaus.  taosayeiti  ,macht  los,  läßt  los'  (*touseiö),  Inchoativ  (*tus-skö) av.  tusdn  ,sie  verlieren  die  Fassung*,  baludi  tusag,  thuay  ,verlassen  werden' ; ai.  tucchd-j  tucchyd-  {^tus-sko-,  *tus-sk-io-)  ,leer,  öde,  nichtig',  afghan.  tas ,leer*;  lat.  tesqua  n.  PI.  »Einöden'  (^^tueskua)-^  ags.  dost  , Dünger',  ahd. iost  ds.  (,* Ausleerung');  aksl.  t^Hh  „-nsvög",  russ.  tö§cij  ,leer;  mager,  hager' usw.  (=  ai.  tucchyd').
WP.  I  714,  WH.  II  675,  Trautmann  333,  Vasmer  3,  130,  Mayrhofer  1, 508  f.
teus-,  tuä-  , sieben,  durchschlagen'.
Ai.  tUau-  (dreisilbig,  aus  *titavu-?)  ,Sieb,  Getreideschwinge';
gr.  adct)  (ion.),  tu)  (att.  EM.),  att.  ÖLafTdü)  ,siehe'  (%/ai(ü),  ölaTTog  m. ,Sieb'  Hes.,  hzrjfieva '  aearj^sva  Hes.,  dXsvQÖTrjOig  f.  , Mehlsieb'  (EM.), orjd-ü)  ,siebe'.
WP.  I  713;  Mayrhofer  1,  499  f.
1086
ti-ti-,  {ti)til-  ^Nachahmung  von  Vogelrufen';  kaum  ursprachlich
Ai.  tittibha-  m.  ,Parra  jacana';  lett.  titühis,  titübite  ,Wasserla  f --^-^ tilvikas,  titilvtkas,  tiülvis  , Brachhuhn,  Schnepfe' ;  gr.  TiTvSiCtü  o/l       * ßitw  ,gackern  (vom  Rebhuhn,  der  Schwalbe');  lat.  titiöj  -äre    zw^i^^^ vom  Sperling';  lett.  titet  ,singen'.  TT?***»
WP.  I  742,  WH.  II  686,  Mayrhofer  1,  457.  M
ticg^-  ,scheu  vor  etwas  zurücktreten  oder  auffahren';  Nom.  ao-entis
H^gX-tor*
Ai.  tydjati  (=  gr.  Geßcx})  ,verläßt,  steht  von  etwas  zurück',  mit  «i. scheuchen,  verdrängen',  mit  nis-  , hinaustreiben,  verjagen',  Partia  t^h^ (=  gr.  Geniöq),  Nomen  agentis  tyaktar-  (=  gr.  ^sooirtTcoQ  , Anbeter  'Ja- Gottheit'),  Kaus.  tyäjdyati  ,macht  zurücktreten',  tydjas-  n.  VerlasBÄnWi* =  av.  i^yajah-,  id-yejah-  n.  ds. ;  ai.  tyägd-  m.  »Hingabe,  Freigebj|k«b* usw.;  "^r"  '
gr.  asßü)  (nur  Präs.  und  Impf.),  osßofxca  bom.  ,(die  Götter)  t^M»«' nachhom.  ,(die  Götter)  verehren,  ehren',  oemog  ,( verehrt  ==)  ehrwMI» heilig',  oeßag,  PL  osßr)  n.  hom.  ,fromme  Scheu,  Ehrfurcht',  nackk(tt|u , Heiligkeit,  Majestät',  hom.  aeßaaaaxo  , scheute  ehrfürchtig*,  asj.tvög  C^üi/h^ ,verehrungswürdig,  erhaben,  heilig;  gravitätisch,  einherstolzierend  prti* kend*,  aoßea)  ,tue  etwas  von  mir  weg,  entferne  schnell,  verjage**  l^Hi ,gehe  eilig,  stolziere  einher',  Goßagög  , rasch,  schnell;  hochfahrend,  pntt« kend*,  aoßdg,  -dSog  f.  ,beftig,  eitel',  aößr]  ,Pferdeschwanz*.  ^p.
WP.  I  746,  Mayrhofer  1,  529.
1.  to-,  tä-f  tio-  Pronominalstamm  ,der,  die*  (Nom.  Sg.  m.  f.  so,  sS,  siehe  doH)| Nom.  Akk.  Sg.  n.  tod,  Akk.  Sg.  m.  tom^  f.  täm,  Gen.  Sg.  m.  (Ol^ f.  tesläs.
Ai.  tdd  (tdt)  ,das',  av.  tat,  Akk.  Sg.  ai.  tdm  m.,  täm  f.,  av.  tom  flkf täm  f.,  tat  n.,  usw.;  arm.  -d  (z.  B.  ter-d  ,der  Herr  da,  du  der  Herr*,  4q^ ,der  da'),  da  , dieser*,  doin  , derselbe',  usw. ;  .  *ffc
70261:   Ar. tittibha-h „Parra jacana";                                      lett. titilbis, titilblte „Wasserlaufer",                       lit.    til-
```


## [2026-10-15T02:45:02.109Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -c '' $R/incoming/WLD/WLD_Bd1_pages.txt $R/WLD_band3.txt; sed -n 70250,70270p $R/incoming/WLD/WLD_Bd1_pages.txt; grep -n -i -E 'titi' $R/AHD_watkins1985.txt $R/IEC.txt | head"
}
```


### [2026-10-15T02:45:02.664Z] TOOL RESULT

```
<persisted-output>
Output too large (32KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/b3sgf3jma.txt

Preview (first 2KB):
data/verification/sources/refs/WLD_band3.txt:4012
data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt:81975
        allenfalls in:
  Lat. titio, -onis „Feuerbrand, brennendes Scheit“ und lit. t'dnagas ,.Feuer-
stein" (Fick I 4 62). Aber gr. t?tco „Tag, Sonne", Tnav, - avog jon. Tizr/v,
fjvog „Sonnengott“ (weder nach Fick als ,.rachender Gott" zu zlvco, noch
nach Dohring Progr. Konigsberg 1912,9 ans *kulto- „weiB“) scheint aus
dem Wortschatz der vorgriechisch-kleinasiat. Bevolkerung zu stammen;
iiber ai. tilhl „Zeitraum, den der Mond gebraucht, urn sich je 12° von
der Sonne zu entfernen", s. Zubaty IF. 19, 370ff., Kielhorn IF. 20, 228.

ti-ti-, (ti)til- „Nachahmung von Yogelrufen"; urspraehliches Alter nicht er-
        weislich.
   Ar. tittibha-h „Parra jacana";                                      lett. titilbis, titilblte „Wasserlaufer",                       lit.    til-

                          „Brachhuhn, Schnepfe" gr. zizvftt^co oder zizzvfh^m
vlkas, titilvikas, titilvis                                                                             ;


„vom Rebhuhn, der Schwalbe". Fick I 4 63, Uhlenbeck Ai. Wb. 105, lat.
titio, -are „zwitschern, vom Sperling" (ob auch lat. titubare „stottern; wanken,

straucheln", so daB ,.stottern“ das Ursprgl. ware? Anders Yf. LEWb. 2 s. v.).
...
</persisted-output>
```


## [2026-10-15T02:45:05.646Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; head -n 70261 $R/incoming/WLD/WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c; grep -n -i -E '^ *(kēš|kesh|kes|kech|kish)\\b' $R/HRN.txt | head; grep -n -i -E 'tkae' $R/HRN.txt $R/HUB.txt $R/BRT.txt $R/NYB_vol2_glossary.txt $R/PHD.txt | head -20"
}
```


### [2026-10-15T02:45:06.017Z] TOOL RESULT

```
750
7658:kes, vergl. pö^yötkes (nur umschreibend), arm. LW. ßes.
data/verification/sources/refs/NYB_vol2_glossary.txt:3163:pūryētkēš [pwlywtkyš] adherent, teacher of the primeval (Zoroastrian) religion 11118; pl. cas. obl. —-än the first Zoro- astrian believers 621, 1115. 1124-16, — Bor- rowed from Av. (877) paoiryö.tkaesa-, ci keš.
data/verification/sources/refs/BRT.txt:2528:i)  'Strafe'  (nur  Ableit.).  a)  Du.  'Schuld  16;  —  U  gaumillc^  . .  xia>^am  . .  agarbä- und  Strafe':  kö  asti  tkaEsü  *visätö  (sd.)  ?  yata  .  .  '/a*  xsdi''am  .  .  Bh.  /.  11  f ;  — yö  'ta  pairi  ar>>rra  frazänaiti  ".  .    vie.t\yäsaDAa..l>aoi'j7m 'tarn  baoi'jTm  K. 103;  —
data/verification/sources/refs/BRT.txt:3304:•  j.  a-daratö.tkaesa-  Adj.  'der  den  Lehrer nicht  achtet':  vlspe  drrantö  tanu.drujö yS'^ •sd'''  vXspe  'sS'*  yß'>  asnifs'ß'''  "alle  sind ungläubig  und  leibhaftig  mit  der  Dr.  ver- bunden, die  den  Lehrer  nicht  achten;  all die  achten  den  Lehrer  nicht,  die  (ihm) ungehorsam  sind"  \.i(J.i8.
data/verification/sources/refs/BRT.txt:4660:•  j.  anya.tkae§a-  Adj.  (fem.  'sa-)-.  s. unter  anyS.th'.
data/verification/sources/refs/BRT.txt:4728:.  i.  anyö.tkaeäa-'>,  anya.!kaeäii-«  Adj.  ''«»«)«    mlKdayatnlil  J.' js-  i,    Vr. ,,.
data/verification/sources/refs/BRT.txt:5668:•  }.  ari.tkaesa-  Adj.  'die  rechte  Lehre btsitiend,  kennend,  rechtgläubig';  °wm'> fstaa  NS.)  bm>sM  ya'^a  rahus  Az.  7.
data/verification/sources/refs/BRT.txt:6232:•  j.  aSava.tkae§a-  Adj.  'der  Lehre  der Gläubigen  zugetan':  vJspa^a  däma  ..ya  .. 'sa  (APn.)  Y.7/.6.
data/verification/sources/refs/BRT.txt:6407:•  j.  aäö.tkaeia-  Adj.  'der  Lehre  des  A/a (des  heiligen  Rechts)  zugetan':  *JriyOs7i( *'/e'l  Yt. /0. 84;  —  driyaos  'sähe  Y.44-
data/verification/sources/refs/BRT.txt:6898:•  j.  ahura.tkaeäa- '',  TÖ.tkaeäa- '>  Adj. (fem.  'Sä-)  i)  'j4/iurashehie  enthaltend': väät/i ..vidsyum  's?m  Yt./^.go'.  2) 'Ahuras Lehre  zugetan,  anhangend':  mazdayasnö zara^us^tri/  vTdagZ'3  's3  Y. /2.1,  Yt  iS-Zq; Y-5-i3>  —  ar>dvtm  .  .  vldaivam  'Sam Y.  65. 1.
data/verification/sources/refs/BRT.txt:6919:•  j.  ahurö.tkaesa-  Adj.  (fem.  'si-)-.  s. unter  ahura.tk'.
data/verification/sources/refs/BRT.txt:14719:•  j.,  g.  'tkaeSa-  m.  i)  'Lehre'  bes.  auf religiösem  Gebiet,  'Glaubenslehre';  a)  im gAw.  spez.  von  der  Lehre  des  falschen Glaubens  'Irr-,  Afterlehre'":   a^^ä  ahmät
data/verification/sources/refs/BRT.txt:14721:8i3  tkaeia-  i  b  —  tbaeSah-  i  814
data/verification/sources/refs/BRT.txt:14736:•  j.,  g.  'tkaeäa-  m.  1)  'Lehrer*  bes.  auf  Vyt5/{?).
data/verification/sources/refs/BRT.txt:15808:*1  Vgl,  Y.  23.  a,  Yt  13.  17.  DsT.s  Bemer- kangen  ZA.  J.  xxix  sind  unzutrefTend,  wenn ich  schon  nicht  leugnen  will,  dass  man  später die  Stelle  so  gefasst  hat.  Der  Gegensatz  von afiara-  ist  paurva-,  nicht  paoirya-.  S-  ''tkaela- No.  2.
```


## [2026-10-15T02:45:09.256Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 14715,14740p $R/BRT.txt | cut -c1-400; echo ----; sed -n 7645,7662p $R/HRN.txt; head -n 7658 $R/HRN.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-10-15T02:45:09.866Z] TOOL RESULT

```
g,  134,  Ggk.  OK.  138,  LiNDKER  Festgr.Roth 214.
•  j.  Orizvat  Adv.  'dreimal':  ^ritlm  upa maypm  5r°  aps  äat  hvqm  tanüm  pairi.- yaozdaiülta  V.^.  31.
Ableit.  aus  %rui  vgl.  tihiat  und  wegen  des  i itoc\  xh'aiaya,  %riiaii/:  Woher  i?  Falsch S  3S4-   "■  —  P".:  3  ^•^^
•  j.  OxyaxStay-  f.:  s.  unter  %ri.yaxstay:
•  j.,  g.  'tkaeSa-  m.  i)  'Lehre'  bes.  auf religiösem  Gebiet,  'Glaubenslehre';  a)  im gAw.  spez.  von  der  Lehre  des  falschen Glaubens  'Irr-,  Afterlehre'":   a^^ä  ahmät
dby  Google
8i3  tkaeia-  i  b  —  tbaeSah-  i  814
23.i.        s)  'Richtef,  im  jAw.:  ilf  mti
'in  '"vivi^äätS  (si)?  yö  alta  (sd.)  pairi ari^ra  frazSnaiH  F.  5;  5;    —   tat  *!ahe tat  ^vjkayehe  "das  (gilt)  für  den  Richter, das  fUr  den  Zeugen"  F.a/b;  —  myaidavh ratui  amyazdavantm    ratunaim    ähüirTm 'i?tn    frapfnnaoiti    (sd.)     A.  J.  12;     — urvaxiayB  (sd.)  ..'s5..  däte.räzS  Y.ß.  10. KompE.  —  VgL  "ifaÄa-  mit  No.  I,  wo  wei- teres, —   Fü.  {la
•  j.  jbaeä-,  dvaeS-,  g.  dvbaeS-''  V.  'an-
■  feinden',  uzw.  nur  wenn  sich  die  Feind- ;   Schaft    gegen    iT:5Krische   Wesen    richtet
~  I  daibil-,  ibis-,  2  7  daibifya-,  tbilya-,
30  (Iter.)/iaa'«;'a-;  Perf.  i  didva^-.didvis-.
■  PPfP.  pii'fa-,  'Ufsta-,  PFP.  dvaisfva-.
i)   'anfeinden,    feind    sein',    mit    Akk.:
■  tlrig  darayö  (sd.)  yH  vä  daibUantl  ■>  Y.  J2. 1 ; -/W/awK^a'' V.^.saPUZ.;  —  asa  vakista
"  yaskanqm  yaskffJtmgm  janüt  .  .  Iballayät ...„.„Z"    -  16*';    —   tbis'yant-,  daibis-
u  fasimärTk  'Anütge  und  Verieidig'^rg"  und  i^-o«/-''  sbes.  s)  Tcr��nken,  beleidigen", vicir  II  ditawarik  "Entscheid  und  Urteil';  (lu  mit  Akk.:  ratavS  vJspe  masista  ,  .  yai  vS i  t):  dätmoar;  {t^  3):  dSlinaarih,  etL;  "icir.^ ^^f/j/gg^^  _  „gfig„^g  ^  .j,acargAa  . .  syaeÜFfta .SQ. :  ayäyai.    Zu  F.  S  wird  gesagt,  liaiii  be- 1  ,        azaosa  V  7  3  a  
deule  meist  ^J/oj/J»,  aber  au  eh  dälavmt.  —  ' '  "^f  ■"*  " '  ^f?'^  ,  *  ■  'l"  ' '  ^  ^ '  "'"Tratte . . »  irfoÄa- (und  ebenso  "/*nAV,  sd.)  gehört  also  !>'«/  3«"*  dtdvXsma  Y.Öff.i;  —  i?  Ja/a/« wie  'daiira-  (sd.  *)),  wn|f-  usw.  zu  den  Schlag-  ^yim  afturnn  .  .  masUta  tbalsanha  ibaisa- und  Kampfwörtem   der  jn^aSüi/nschen  Zeil.  \ yäti  V.  18.  6jJ  —  t
rs6,s /i;iir_'rÄ,Mrs  j  (^i)  vi™.  .09; ->.vv»  ~^^^^^
Unrichtig  DsT,  ZA-  3.  xxix,  197;  t.  paeiryö.-  —  yanva  (naml.  nmänähu)  tbtstB  eavaitt lialia-.  —  Sl  Die  Gebete  Y.  3?.  14  und  15  (nSml.  OT/ärS)  YL/0,z8;  —  yahmai  xSnBtS . . enthalten  drei,  27.13  fünf  rtoSa. —  4)  Sicher  |j,o^mJi /^»//ir  iai/a/ft' »»»■^/-ff..Yt.i0.87;  — Wsch  ZDMG.  so.  134.  N^,Y/J  W/..;»J  j/b«/a,itf  mainyJui dämqn
•  j.,  g.  'tkaeäa-  m.  1)  'Lehrer*  bes.  auf  Vyt5/{?).
religiösem  Gebiet,  'Lehrer  des  Glaubens,!     mit  upa  dnwS.a:    mtiirs  grants  upa.- Rabbi';  a)  im  gAw.  spez.  vom  Lehrer'_/i(Y/ff  Yt  10.18,  19,  39,  43.
vannai  mazdä  mdat»m  aiim  iüidyäi  'iäi rasayeAk!  druxi  "und  in  diesen  (unsem) Glauben  ist  das  ÄSa  niedergelegt,  um  den Nutzen,  in  die  Afterlehre  die  Drug,  um  den Schaden  zu  schaffen"  Y.^p.  3.  b)  im
jAw.  allgemein:  zara%ustrahe  vanmmca 'simca  Y,  iG.  2 ;  —yävaranS  as  zara\ultr5 .  .  tä  var^näcä  'säcä  mazdayastiB  akmJ .^.12.^;  —  aparimla  'hm  yasamaide  "Atu zweiten  Teil'*  der  Glaubenslehre  . ."  G. 9.7,  a)mita^Ärij)'- Adj.  'die  aA«nsche, d.  i.  von  AA.  erteilte  Lehre,  Belehrung': ahairiS  frams  (sd.)  ,  .  ahairis  'sö  Y.  57. 24;  60.  3;  —  ähUirTm  frasmm  .
liche Auslegung  des  Gesetzes,  Richter- spruch', nur  jAw.:  °sS  F.  5.
----
afy. kala ; oss. d. t. ßäd wenn, ob* (158) ; bei. kad'i
wann?' (182).
879. (2)kei 'Herrscher (wie /iisrev 'Herrscher ursprünglich
N. pr.).
aw. kavi-; phlv. ke, vergl. Kerat (Gemme, Hörn,
ZDMG. 44, 675 No. 139); ai. kavi- weise.
Dazu got. us'skava 'vorsichtig, nüchtern*, ahd. scou-
wön 'schauen', Brugmann, Grundriss I, § 528.
880. kes 'Religion .
Siw. tka^Sa- 'Bekenntniss, Gelöbniss (so — nicht
mehr als 'ketzerisches Bekenntniss, Irrglaube' aus
*atika^sa'j wie KZ. 28, 2 — fasst auch Bartholomae
jetzt nach brieflicher Mitteilung das Wort auf ') ; phlv.
kes, vergl. pö^yötkes (nur umschreibend), arm. LW. ßes.
881. ktn 'Feindschaft, Hass, Zorn', Mne.
aw. ka^nä' 'Strafe, Rache'; phlv. ken (paz. ;^fM),
kemtan, arm. LW. ken, jünger Mnavor,
kurd. LW. km; bei. kenay 'Feindschaft, Hass,
217
```


## [2026-10-15T02:45:13.386Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -E '^ *k[eē][sš]\\b' $R/PHD.txt $R/NYB_vol2_glossary.txt | head; grep -n -E '^ *880\\.|k[eē]s .Religion|kes ' $R/HUB.txt | head"
}
```


### [2026-10-15T02:45:13.801Z] TOOL RESULT

```
data/verification/sources/refs/PHD.txt:5002:kēšīdan
data/verification/sources/refs/NYB_vol2_glossary.txt:2294:keš [kyš] faith, religion, both of the Zoroastrian religion and of others, 8015-18, 8212, 108%. — Av. (812 sq.) tkačša-; MPrs kyš ‘doctrine, dogma’; NP kčš (Sn).
1942:stockes und der Dattelpalme). Ebenso urteilt Geiger,
7507:H. 1021 (aber zd. oka sat 'erblickte', kis. ipt. bikes Shuk.
9607:werden. Wahrend des Druckes ist mir NOldeke's Rath
```


## [2026-10-15T02:45:16.112Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 4990,5004p $R/PHD.txt; grep -n -i 'kēš\\|keš ' $R/PHD.txt $R/PHD_mackenzie.txt | head; head -n 2294 $R/NYB_vol2_glossary.txt | tr -cd '\\f' | wc -c; grep -n -E '(^| )88[0-1]\\.' $R/HUB.txt | head"
}
```


### [2026-10-15T02:45:16.484Z] TOOL RESULT

```
PAHLAVI KEY
\ KE
karbāš karbunag karg kirīh- askamb! kirrén- kirrēnīdan kilēl
diz!
xwan-!
xwandan!
kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
kardārīh
[121]
Neds >Da
kirbakkarih kirbag, kofag
koftan
kēšīdan
kosk
ku&tan
data/verification/sources/refs/PHD.txt:428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
data/verification/sources/refs/PHD.txt:430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
data/verification/sources/refs/PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
data/verification/sources/refs/PHD.txt:1673:dogma kēš.
data/verification/sources/refs/PHD.txt:1868:faith kēš, xwastügih; breaking ~ mihródrujih.
data/verification/sources/refs/PHD.txt:2934:non-Mazdean kēšdār; v. heretic.
data/verification/sources/refs/PHD.txt:3035:palace dar, darbās, kēšk, šāhīgān.
data/verification/sources/refs/PHD.txt:3059:pavilion kēšk, mašk; royal ~ mašk- abarzēn.
data/verification/sources/refs/PHD.txt:3555:sectary kēšdār; v. heretic.
data/verification/sources/refs/PHD.txt:3964:pēryētkēš;
131
3172:881. Lies arm. LW. U^n 'GroU, Hass, Feindschaft, Rache',
8483:kamk, zd. ap. kama-^ u. s. w., vgl. H. 831 — 881. — Fiir k
```


## [2026-10-15T02:45:20.368Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 3160,3172p $R/HUB.txt; head -n 3165 $R/HUB.txt | tr -cd '\\f' | wc -c; grep -n -E 'atlas|ṭalas|talasa' $R/KLN_1966.txt | head"
}
```


### [2026-10-15T02:45:20.809Z] TOOL RESULT

```
Hier fehlt np. Uui {kUz und kUza) gekriimmt' {kuz-pust
Fird. I, 503, Z. 7), afgh. ko^ (LW.?) crooked, bent*
= skr. kubja^ 'krumm, bucklig*.
873. Die Zusammenstellung setzt eine idg. Wrzl. kul-
(hochstufig ketd^ kouT) voraus, die es nicht giebt.
874. Zu streichen.
875. Dazu arm. LW. ioAai 'Berg, Woge' und nach Geiger
afgh. kvah *H6cker .
Hier fehlt np. kavl», kavHz = arab. LW. qafiz u. s. w., phi.
kapU (so zu lesen) Gl. and Ind. 197 u.s.w., arm. LW.
kapic 'ein Maass fur Getreide' etc., ap. xan/drj de La-
garde, Ges. Abh. 198.— 90 ~
881. Lies arm. LW. U^n 'GroU, Hass, Feindschaft, Rache',
99
3850:Atlas,  n.,  one  of  the  Titans,  son  of  lapetus  and Clymene,  supporting  the  heavens  on  his  shoul¬ ders;  later,  a  king  of  Mauretania,  changed  by Perseus  into  Mt.  Atlas  ( Greek  mythol.)  —  L. Atlas  (gen.  Atlantis),  fr.  Gk.  ’'AxXocp  (gen.  "Ax- Xavxop),  which  stands  for  ”A-xXa<;  and  lit.  means ‘the  Bearer  (scil.  of  Heaven)’,  fr.  copul.  pref.  4- and  the  stem  of  xXrjvoa,  ‘to  bear’  (cp.  jxoXu- xXa?,  ‘much-enduring’).  Copul.  pref.  4-  stands for  I.-E.  *sm-,  a  weak  gradational  form  of  I.-E. base  *sem-,  ‘one,  together’ ;  see  same.  Gk.  xXrjvai derives  fr.  *//-,  zero  degree  of  I.-E.  base  *tel-, *tal-,  *tol-,  ‘to  bear,  lift,  suffer’,  whence  xaXa 4, gen.  xaXcrvop  and  x4Xavxo9,  ‘bearing,  suffer¬ ing’,  TxXdooai  (aor.),  ‘to  bear,  suffer’,  L.  tol- lere,  ‘to  lift  up,  raise’,  tolerare,  ‘to  bear,  sup¬ port’.  See  tolerate  and  cp.  atlas,  name  of  the first  vertebra,  atlantes,  Atlantic,  Atalanta, talent.
3851:atlas,  n.,  a  collection  of  maps  bound  into  a  book. —  First  so  called  by  the  geographer  Mercator because  the  figure  of  Atlas  supporting  the  world was  frequently  put  on  the  front  page  of  such collections.  (The  first  part  of  Mercator’s  Atlas, sive  cosmographicae  meditaliones  defabrica  mun- di  appeared  in  1585.)  See  prec.  word, atlas,  n.,  name  of  the  first  vertebra  ( anal .)  — From  Atlas  (q.v.);  so  called  because  it  bears  the
3853:skull.  This  name  was  given  to  the  first  vertebra by  the  Belgian  anatomist  Andreas  Vesalius (1514-64).  See  Joseph  Hyrtl,  Onomatologia anatomica,  Vienna,  1880,  p.59. atlas,  n.,  silk-satin.  —  Arab,  atlas,  lit.  ‘wiped smooth’,  fr.  talasa,  ‘he  wiped,  smoothed  away’, atle,  atlee,  n.,  the  tamarisk  salt  tree.  —  Arab. athlah,  ‘a  species  of  tamarisk’,  prop,  unit  name of  athl,  rel.  to  Aram,  athld,  Heb.  eshel,  ‘tama¬ risk  tree’.
33793:Derivative:  satiat-ion,  n. satiety,  n.  —  MF.  (=  F.)  satiete,  fr.  L.  satietatem, acc.  of  satietas,  ‘sufficiency,  abundance’,  fr.  sa¬ tis,  ‘enough’.  See  satiate,  adj.,  and  -ity. satin,  n.  —  F.,  fr.  Arab,  atlas  zaytunt,  ‘tissue brought  from  Zaitun,  Arabic  name  of  the  Med¬ ieval  Chinese  shipping  port  Tzu-t'ing  (later  call¬ ed  Chuanchow,  now  Tsinkiang),  in  the  province Fukien.  F.  satin  was  prob.  influenced  in  form  by It.  setino,  a  word  of  identical  origin,  but  assim¬ ilated  to  seta,  ‘silk’.  Cp.  sateen.
```


## [2026-10-15T02:45:26.180Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; head -n 3853 $R/KLN_1966.txt | tr -cd '\\f' | wc -c; grep -n -i -E '^ATLAS|atlas' $R/SKT.txt | head -5; grep -n -i -E 'a[tṭ]las' $R/LKT.txt | head; grep -n -E '^atlas|^at.las' $R/WEB_vol1.txt | head; grep -n 'أطلس\\|اطلس' $R/AFM_pages.txt $R/incoming/PLA/PLA_pages.txt | head"
}
```


### [2026-10-15T02:45:26.597Z] TOOL RESULT

```
76
1094:Atlas.  (Gk.)  Named  afler  Atlns,  the demi-god  who  was  said  to  bear  the  world on  his  shDulders ;  his  figure  used  often  lo appear  on  the  title-page  of  atlases.  — Gk. ■'AtAoj  Cficn.  'ArAo»'Tiit>,  prob.  "the  sus- tainer'  or  l»earer,  from  ^  TAL,  to  bear.
1095:&U.autic,  sn  ocean,  named  after  Ml. Atlas,  in  the  N.W.  of  Africa;  from  aude form  'ArAavn-,
516:131.  Ar.  atlas:
517:'Glatt,  fein'.  Von  einem  Manne,  der nicht  viel  taugte,  sagte  man,  er  sei atlas;  ebenso  von  Seide,  sie  sei  atlas, d.  h.  minderwertig;  schheßlich  blieb das  Adjektiv  allein  zur  Bezeichnung  des Stofifes  [wie  z.  B.  im  Romanischen,  wo aus  lat.  ieciir  firatum  frz.  foie  'Leber', aus  lat.  caseum  fonnaticum  frz.  froinaffe 'Käse'  wurde],  und  zwar  des  sog.  Seiden- satins  [s.  hier  Nr.  2188].  Rum.  atlas, atlaz;  russ.  atlas,  bulg.  atlaz,  serb.  cech. atlas,  poln.  atlas  'Satin'.  Dtsch.  Atlas, ndl.  atlas.  [Joseph  Karabacek,  Über einige  Benennungen  mittelalterlicher Gewebe.  Wien  188±  S.  llfT.  Gorjajew 7.  Hobson-Jobson  39/40.  Kluge  '25. Dozy  Oost  22.
1689:Vulg.  gemesit  [aus  pers.  gärni  'Avarm' Horn  NpEt  S.  203,  Nr.  911,  und  süd 'Nutzen,  Vorteil'  ebenda  S.  166,  Nr.  751] 'eine  Art  Stoff' ;  hieraus  rum.  ghermesit 'Art  Atlas'.
2910:'Kleiderstoff,  Zeug',  tk.  und  kas.-tat.  ku- mas;  hieraus  russ.  kumac  'bucharisctier roter  oder  blauer  Baumwollstoff,  bulg. kumaS  'Stoff',  serb.  kttmaS  'Seidenzeug, Atlas',  ßech.  kumaö  'Baum wollsl off'; rum.  comas,  cumas  'Seidenstoff'.  [Bern SlEtWb  643.
4463:Auch  Tafilet,  N.  pr.,  zu  Marokko  ge- hörige Oase  südlich  des  Atlas,  in  der Lederindustrie  heimisch  ist;  hieraus  kat. pg.  tafilet,  sp.  tafilete  'feines  Leder, Saffian'.
4892:N.  pr.,  Name,  mit  dem  im  MA  der  große chinesische  Ausfuhrhafen  Tseutung  oder Tswan-tschou-fu  in  Fokien  [MP  408/410; JB  246/247]  bezeichnet  wurde.  Hier- nach wurden  gewisse  Damaststoffe  ar. atlas  zaitüm  'zaitunischer  Satin'  ge- nannt; hieraus  sp.  aceituni,  setuni,  mfrz. zatony,  frz.  satin,  mit.  zetani,  it.  zetani- no,  setino  [mit  Anlehnung  an  seta];  engl. satin,  dtsch.  Satin.  Vgl.  ausführlich Karabacek,  Über  einige  Benennungen mittelalterlicher  Gewebe.  I.  Wien  1882. S.  12/13.  Hirth  ChinFW  204/205  weist darauf  hin,  daß  in  den  Seidenfabriken Kantons  noch  heutzutage  derselbe  Stoff, den  wir  gewöhnlich  als  Seidenatlas  be- zeichnen, unter  den  Namen  ssü-tuan, kantonesisch  szetün  'Seiden-Atlas'  ver- kauft wird.  Es  scheint,  daß  ar.  Käufer im  Laufe  der  Jahrhunderte  dieses  un- mittelbar eingeführte  Wort  mit  dem ähnlich  klingenden  Namen  ihrer  schon vor  Kanton  berühmt  gewordenen  Han- delskolonie Zaitiln  verwechselt  haben. [Hobson-Jobson  797.  DE  340.  Eguilaz 20/21.    ML  8962.
12900:atlas fōl’ið, a large, square folio size of books.
```


## [2026-10-15T02:45:29.138Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; ls $R | grep -i -E 'hjb|aid|fsd'; sed -n 12895,12902p $R/WEB_vol1.txt | cut -c1-600; head -n 516 $R/LKT.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-10-15T02:45:29.568Z] TOOL RESULT

```
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
8. a collection or volume of plates or en- gravings explanatory of some subject.
9. the atlas beetle, Chalcosoma atlas.
10. pl. at-lan’tés, in architecture, any of the atlantes. x
Allas powder; a compound of nitroglycerin used in blasting.
at/l4s, n. [Ar., smooth, bare, satin.] a fine fabric of silk and satin, manufactured in the East Indies.
atlas fōl’ið, a large, square folio size of books.
at/lds grid, a system of parallel and perpen- dicular lines on an aerial photograph, divid- ing it into small squares for locating points 0n the photograph quickly. e
at/lee, n. [native name.] the East Indian „tamarisk salt tree, Tamarix orientalis.
38
```


## [2026-10-15T02:45:31.392Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -E '^ *ATLAS|ATLAS, s' $R/HJB.txt | head -3; grep -n -A8 -E '^ *ATLAS' $R/HJB.txt | head -20"
}
```


### [2026-10-15T02:45:32.422Z] TOOL RESULT

```
2254:ATLAS,
2276:ATLAS,  s.  An  obsolete  word  for '  satin,'  from  the  Ar.  afhuy  used  in  that sense,  literally  *bare'  or  *bald'  (comp. the  Ital.  raso  for  'satin').  The  word is  still  used  in  Qerman.  [The  Draper's Did.  (s.y.)  says  that  "a  silk  stuff wrought  with  threads  of  gold  and silver,  and  known  by  this  name,  was at  one  time  imported  from  India." Yusuf  Ali  {Mon.  on  SUk  Fabrics,  p. 93)  writes  :  ^^  Atlas  is  the  Indian  satin, but  the  term  satan  (corrupted  from  the English)  is  also  applied,  and  sometimes specialised  to  a  tnicker  form  of  the fabric.  This  fabric  is  always  sub- stantial, %.e,  never  so  thin  or  netted as  to  be  semi-transparent ;  more  of  the weft  showing  on  the  upper  surface than  of  the  warp."]
2254:ATLAS,
2255-plained  by  Klinkert  as  '  a  short  wooden throwing-spear,'  which  is  possibly  that referred  to  by  G.  de  Eredia.]
2256-e.  1270. — "TlierB  was  the  King  standing with  three  '  ezortins '  (or  men  of  the  g:uard) by  his  ade  anned  with  javelins  [ab  Ivor  atm- gajM  'HL — CkrmdeU  of  K.  Jama  of  Aragon, tr.  by  Mr.  Foster,  1883,  i.  173.
2257-c  1444. — •*  .  .  .  Tliev  have  a  quantity  of ,  which  are  a  kind  of  light  darts." ,  NoMgofSo  pririuira,  32.
2258-1562.^"  Bat  in  general  thev  all  came armed  in  their  fashion,  some  vnm  ajwigaias and  shields  and  others  with  bows  and quivers  of  arrows."— -Borrtw,  I.  iii.  1.
2259-1672.— "  Hum  de  esoodo  embracado,  e  de  aiftglla,
2260-Outro  de  aroo  encorvaao,  e  setta  ervada." CkeaUkty  i.  86.
2261-By  Barton: "  this,  taxge  on  arm  and  aaiigai  in  hand,
2262-that,  witii  his  bended  bow,  and  venom'd reed."
--
2276:ATLAS,  s.  An  obsolete  word  for '  satin,'  from  the  Ar.  afhuy  used  in  that sense,  literally  *bare'  or  *bald'  (comp. the  Ital.  raso  for  'satin').  The  word is  still  used  in  Qerman.  [The  Draper's Did.  (s.y.)  says  that  "a  silk  stuff wrought  with  threads  of  gold  and silver,  and  known  by  this  name,  was at  one  time  imported  from  India." Yusuf  Ali  {Mon.  on  SUk  Fabrics,  p. 93)  writes  :  ^^  Atlas  is  the  Indian  satin, but  the  term  satan  (corrupted  from  the English)  is  also  applied,  and  sometimes specialised  to  a  tnicker  form  of  the fabric.  This  fabric  is  always  sub- stantial, %.e,  never  so  thin  or  netted as  to  be  semi-transparent ;  more  of  the weft  showing  on  the  upper  surface than  of  the  warp."]
2277-1284. — "Cetto  m6me  nuit  par  ordre  du Sultan  quinze  cents  de  ses  Mamlouks  furent revdtus  de  robes  d'atlaa  rouges  brod^es.  .  ." —Makridy  t.  ii.  pt  i.  69.
2278-„  <*The  Sultan  Mas'ud  clothed  his dogs  with  trappings  of  a^las  of  divers  colours, and  put  bracelets  upon  them." — FaJehr\ p.  68.
2279-1505.— "Raso  por  seda  rasa."— Atlis, Voeabular  Arauigo  of  Ft.  P.  de  Ateala.
2280-1678.— "They  go  Rich  in  Apparel,  their Turbats  of  Gold,  Damask'd  Gold  Atlas  Coats to  their  Heels,  Silk,  Alajah  or  Cuttanee breeches."— .FVyer,  196.
2281-1683.— "I  saw  ye  TaffatUs  and  AtUsses in  ye  Warehouse,  and  gave  directions  con- cerning their  several  colours  and  stripes." — Hedges,  Diary,  May  6 ;  [Hak.  Soc.  i.  85].
2282-1689.— (Surat)  "is  renown'd  for  ...  . rich  Silks,  such  as  AtUsses  ....  and  for ZarbaftB  [Zerbaft]   "—Ovin^foii,  218,  <
2283-ATOLL.
2284-40
```


## [2026-10-15T02:45:35.817Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 547 1364 1755; do python3 tools/ref_page.py BQT:$p 2>&1 | head -60; echo =========; done"
}
```


### [2026-10-15T02:45:36.245Z] TOOL RESULT

```
Exit code 1
no scan of BQT covers printed page 547 (see 'scans' in refs_online.json)
(eval):1: ======== not found
```


## [2026-10-15T02:45:37.851Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 1364 1755; do python3 tools/ref_page.py BQT:$p --image 2>&1 | tail -40; echo \"=========\" ; done"
}
```


### [2026-10-15T02:45:48.339Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 159; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1364.png
REF: BQT:1364  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 159  OCR-lang: fas

گفتار هفدهم
تبجی مبتنی بر نوزده بیان و محتوی بر بکصد
وهشناد و دو لت و کذایت
بیان اول
ات عار بت سر) «کنایه از دنیای‌فانی کنایه از عاشق خسیس ورذل و بی‌صدق و لیتالی
و سکون قاف و بای ابجد بالف کشیده , یام | طلبان و طالبان دیا باشد.
اوعی از طعام است که آترا با سر که یاآب‌لیمو عاقول < باقاف بواو کشیده و بلام
پزند ۳ . زده » لوعی از خرنوب است که کبر باشد؛ویسی .
* ع (عین) - حرف بیست وبکم ازالفبای فارسی وحرف هیجدهم از الفبای‌عربی(ابتث)
و دراب جمل آبرا هفتاد گیرند. در لغأت فارسی این حرف نیامده و درلغات دخیل آبرا مانند
(۳۱ء.) نلفظ کنند . تلفظ این حرف در عربی از زديك کردن بالا و پایین حلق بهم وبیرون
دادن هوا صورت کیرد ۰
‎٩‏ - ازعاعق (عر )اج با ( اب (همب)
۴ - پیش ازآندم که مزعفر شکند همچون کل
داغ او چون حبشی بر دل ماشقبا بود.
« دبوان اطعمه‌بحاق شیرازی‌چاپ‌استالبول ۱۱ )۰
( برهان قاطع ۱۷۹ )

=========

پلندیهای اطراف‌هرموز برمیآیند مان د کیش که کیش هند ‎٩‏ - بنتح اول ومیم‌بروزن
رکش باشد بتظر درمیآیید ۴ - ونوعی ازجامه | روت مند » بمعنی جباری و فهاری باشد پلفت
بو د که ا زکتان بافند 6 - وتنام جانوری‌است که زید واوستا .۰
از پوست آن پوستین کنبد ‎٩‏ - ودرخت شمشادرا ۱ ۳ ۰ بکسر اول بروزن تیغ چر

۱ - رك : رکش » ترکش :
آسمان کر ملاح بر بندد تیر قدییر تو نهد درکیش *
«انوری آبیوردی چاپ تبربزص۰۴۶۱۲۲ .
۲ سول ارستا- 1865102(اعتراف ۰ عهد).پهلوی 5650 (قی :۵ ۲۵)
ارمنی ع18512 «اسشق ۸۸*۰ . در اوستا «تکششه» در مورد آیین اهریمنی استعمال شده » درمقابل
««ئنا» (دین) ‏ ولی در فارسی‌کیش بمعنی مطلق آیین ودین آمده :
لب با قوت رنگه وئالهٌ چنگه می چون لمل وکیش زرتهشتی. دفیقی طرسی .
۴ - زرای اوست‌کار ملك و ملت چوتیر چارکیش از فاق وییکان ۰
عبداقادرايينی جپانگیری» «رشیدی».
۴ - «کیش » جزیره‌ای‌ازجزایر بحر فاری » ودر تاریخ وصاف است که چون‌ازمکانهای
مرتفع بینند زمین آن بهیلت کیش یعنی ترکش نماید وقیس معرب آن وبهرموز اشتهار داود ۰ >
«سراج اللغات بنقل فرهنگه تظام» . بمد از قشم مهمترین جزیرء ساحلی ایران«کیش» اس ت که

۵ کیلو متر طول و ۸ کیلومتن عرض دارد و بواسطةٌ تنگه ای بعرض ۱۸ کیلومتر ازساحل جدا-

شده, این‌تنگه بخوبی قابل کشتیرانی است . جمعیت آن قربب 4۰۰۶ تن است «جغرافیای‌طبیعی

کیهان ص۱۰۹ ورك : ممجم‌البلدان : قیی. این جزبره غیرجزیرء هرموز (هرمز) است ولی‌در
زمان اهمیت جزبرة هرمز کیش باادیگر جزایر خلیج فاری جزو منطقةٌ حکمرالن پادشاه هرمز
بود . ۵ -<خیش (و.م.) » قن : یزدی «کیش» (مقنعهٌ زن) » درسبزواره کیش‌حمام» يك

قم کتان است «قرهنگه نظام» . ‎٩‏ -ر3 : جهانگیری, رشیدی ۰

۷ -رك : جهانگیری » رشیدی . درکیلان 81510 بدمنادآهای کوتاه و. پلریکی که در

حاشةٌ باغچه‌ها کارند , اطلاق‌شود . ۸ -قی : کعت ( ر3 : شه در همین کتاب) .

‎٩‏ - از دساتیر «فرهنگه دساتیر ۰.۲۹۲ ۹ کیخ «کیغ : رمص باش دکه‌پن

‏مره شم ننیند . ابوشعیب (هروی) گوید :
شگفت ست اکر کیغ چشم هن .سرخ است بلی چو سرخ بود اغك » سرخ باش دکیخ.»

‏دلفی فری۲۳۸*.

=========
```


## [2026-10-15T02:45:54.810Z] TOOL CALL #24: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1364.png"
}
```


### [2026-10-15T02:45:55.204Z] TOOL RESULT

```

```


## [2026-10-15T02:45:55.201Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-15T02:45:57.435Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 157 158; do python3 tools/ref_page.py BQT:1364 --pdf-page $p --image 2>&1 | grep -n -E 'IMAGE|طیت|طیط|تیتو|۱۳۶' ; done"
}
```


### [2026-10-15T02:45:58.022Z] TOOL RESULT

```
1:IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1364.png
1:IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1364.png
```


## [2026-10-15T02:45:59.472Z] TOOL CALL #26: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1364.png"
}
```


### [2026-10-15T02:45:59.887Z] TOOL RESULT

```

```


## [2026-10-15T02:45:59.883Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-15T02:46:02.911Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt; python3 - <<'E'\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt').read().split('\\f')\nfor i,p in enumerate(t):\n  for k in ['طیطو','طیتو','تیتو','طیطوی']:\n    if k in p: print(i,k)\nE"
}
```


### [2026-10-15T02:46:03.467Z] TOOL RESULT

```
139 طیطو
156 طیطو
156 طیتو
156 تیتو
156 طیطوی
248 تیتو
```


## [2026-10-15T02:46:05.691Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; awk 'BEGIN{RS=\"\\f\"} NR==157' data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt | grep -n -C4 -E 'طیطو|طیتو|تیتو|titt|ṭiṭ|tit' | head -60"
}
```


### [2026-10-15T02:46:06.205Z] TOOL RESULT

```
5-‎Olan‏ - با ‎oth‏ حطی تالی بر وزن
6-‎OOS‏ » بلفت سریالی ‎SUAS‏ صحراییرا کوشد
7-وحربی ‎oy AS‏ خوانند ‎٩‏ .
8-- طیطاو ۲ - با ای حطی بروزن ‎ied‏
9:‎ey‏ از مرغابی باشد؛ وطیتو ‎ps‏ کنته‌اند کسلای
10-دوم ای فرشت ‎ath‏
11-
12-‏طیفود ۴ بنتح او وضم فا بر وزن
13-دیجور + مطلق پرنده را کوبند اعم ازمرغ ‎ges‏
--
47-
48-‏بلون زده , لوعی از رحیالمالم است که بستان | کوچکتر است .
49-
50-‎porreau= ۱‏ (فر) « لك ۲س1۲۱. ۴ لل‌طوی ‏ نیتو " از سانسکربت
51:‎tittibha‏ مرغی است) ‎ply?‏ 4۷4 : ۰۳ . این کلمه توسط برزوبه مترجم ‎LIS‏ ودمنه
52:‎us shee‏ وارد زبان مزبور شد" ودرفارسی بصورت ‎Ss‏ درآمد : « تیتو , مرغ ‎BT‏ است » رود کی
53-(سمرقندی ) گوید :
54-
55:‎Atay peal? ‏وبچه بدان تیتو سپرد.‎ (als ‏خانه (ظ.‎ aut ‏را‎ lus ‏سیمرغ‎ Leak
56-
57-‎AIT >‏ ودمنه این الستفع
58-
59-‏) چاپ مرصفی ص ۱۳۸و۱۳۹) و کلیله ودمنة & پارسی ‎nl pape te‏
60-
61:‏عدالحمید ( چاپ‌چهارم قریب ص۷٩)‏ « طیطوی » آمده ورك: حياة لحیوان‌دمیری : طیطوی.
62-
63-‎.* ‏(عر) «طیفور » طائرصفیر» « اقرب الموارد‎ - ۴
64-. he relat cs) Telephium —e
65-‏چادو. معرب است‎ + Weds, pill oLLb -
--
86-
87-‎ve pv elle (3) ۳6۲0۲15 = ۰‏ 4>ورك : نیهو: «وبهتر وزود کوارتر کوشت‌ما کیادست
88-وآن کبوتر بچه ودراج وطیهوح» (الابنیه : لحوم ص ۱۸۲ الق)-
89-
90:‏# طیطوی ره : طیطو .
91-
```


## [2026-10-15T02:46:11.948Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls -la data/verification/sources/refs/ocr/BQT/ | grep -E '136[0-9]|175' ; git status --short data/verification/sources/refs/ocr | head"
}
```


### [2026-10-15T02:46:12.304Z] TOOL RESULT

```
.rw-r--r--  230k sfmqrb 14 Oct 22:45  1364.png
.rw-r--r--  1.5k sfmqrb 14 Oct 22:45  1364.txt
.rw-r--r--  427k sfmqrb 14 Oct 22:19  1754.png
.rw-r--r--  4.2k sfmqrb 14 Oct 22:19  1754.txt
.rw-r--r--  468k sfmqrb 14 Oct 22:45  1755.png
.rw-r--r--  4.5k sfmqrb 14 Oct 22:45  1755.txt
.rw-r--r--  454k sfmqrb 14 Oct 22:19  1759.png
.rw-r--r--  4.3k sfmqrb 14 Oct 22:19  1759.txt
.rw-r--r--  175k sfmqrb 14 Oct 22:19  1862.png
.rw-r--r--  175k sfmqrb 14 Oct 22:19  2165.png
```


## [2026-10-15T02:46:14.359Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; rm data/verification/sources/refs/ocr/BQT/1364.png data/verification/sources/refs/ocr/BQT/1364.txt; python3 tools/ref_page.py BQT:1364 --pdf-page 157 --image 2>&1 | head -5"
}
```


### [2026-10-15T02:46:21.311Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1364.png
REF: BQT:1364  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 157  OCR-lang: fas

له ماضا
طیسه - بفتح اول رسین بی‌شطه ‏ بتر | افروز باشد؛ وبستی تشم بستان افروژرا گفته‌اند.
```


## [2026-10-15T02:46:22.680Z] TOOL CALL #31: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1364.png"
}
```


### [2026-10-15T02:46:23.295Z] TOOL RESULT

```

```


## [2026-10-15T02:46:23.290Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-15T02:46:31.689Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat > data/verification/sources/refs/ocr/BQT/1364.vision.txt <<'E'\n[BQT p.1364, vol 3 pdf page 157; read from the page image]\nطیطاو ۲ - با طای حطی بروزن تیهو، نوعی از مرغابی باشد؛ وطیتو نیز گفته‌اند کهطای دوم تای قرشت باشد.*\nحاشیه ۲ - طیطوی = تیتو، از سانسکریت tittibha (مرغی است) «ویلیامز ۴۲۹ : ۳». این کلمه توسط برزویه مترجم کلیله ودمنه بپهلوی، وارد زبان مزبور شد ودرفارسی بصورت تیتو درآمد: «تیتو، مرغ آبی است» رودکی (سمرقندی) گوید:\nپادشا سیمرغ دریا را ببرد      خانه (ظ. خایه) وبچه بدان تیتو سپرد.   «لغت فرس ۴۱۸».\nدرکلیله ودمنهٔ ابن المقفع (چاپ مرصفی ص ۱۳۸و۱۳۹) وکلیله ودمنهٔ پارسی مترجم نصرالله بن عبدالحمید (چاپ چهارم قریب ص۹۷) «طیطوی» آمده ورك: حیاة الحیوان دمیری: طیطوی.\n* طیطوی - رك: طیطو.\nE\ngrep -n -A3 'tym\\b\\|تیم' data/verification/sources/refs/BQT_v2_pages.txt | head -0; python3 - <<'E'\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt').read().split('\\f')\nfor i,p in enumerate(t[:15]):\n  if 'تیم' in p: print(i, p.count('تیم'))\nE"
}
```


### [2026-10-15T02:46:32.179Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:35.750Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'E'\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n  t=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/'+f).read().split('\\f')\n  for i,p in enumerate(t):\n    for k in ['تیمچه','تیمار','tim','tēm']:\n      if k in p: print(f,i,k)\nE"
}
```


### [2026-10-15T02:46:36.467Z] TOOL RESULT

```
BQT_v1_pages.txt 36 تیمار
BQT_v1_pages.txt 533 تیمار
BQT_v1_pages.txt 595 تیمار
BQT_v1_pages.txt 775 تیمار
```


## [2026-10-15T02:46:38.479Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=data/verification/sources/refs/BQT_v1_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==776' $F | head -60; echo; awk 'BEGIN{RS=\"\\f\"} NR==1' data/verification/sources/refs/BQT_v2_pages.txt | head -20"
}
```


### [2026-10-15T02:46:39.091Z] TOOL RESULT

```
اي محِ
چنبر رسن تابی را گوبند م ویفتح اول‌جعل‌منقش
دا یازا 9
تیلیاك - یکی اول وئالث وسکون‌ثانی
گویند .
لیم سم بر وزن میم » کاروان سرای
بز رگه را گرد چبه ه تیمحهکاروان سرای کوچك
است؟ .
تیه - بر وزن سیما » دشت و بیابانرا
گوته .
تیمار س بر وزن‌بیمار» خدهت وغه‌خواری
و محافكت کردن کی را که ممار بود و با به
بلیتی کرفتار شده باشد گ و بمعتی نگاهدافتن
ومحافظت نبودن وغمخواری۴ - وفکر واندیشه
کردن همآمده است - وآنرا تیماره بازباوتی‌ها
نیز خوانند .
قیماس ه بر وژن ربوای » یثه
و له نیشان و جنگل را کویند » وسری اجم
خوانند .
(۱) چك :
۱ ظ , محرف «رتیلا» .
ره
زند و باژند 2
تیماو - بسکون واو ؛ بمعتی بلادت
باشد وآن تعطیل قوت تفس ناطقه است بی آنکه
تقصیری در خلفت آن شده باشد .*
تیمسار؟ » با سین بی نقطه بر وزن
میشکار . کته ابت که آرا بعربی حضرت
می گوبند .
قیمنالگ - با نون بالف کشیده وبعاف
زده » بمعتی مواسات باشد و آن معاوت باران
ودوستان وستحفن کردن است .#
قیمو م2 » با اول بثائی رسیدد و الث
بواو کشیده و یکاف زده » ؛معنی شون ات 15
آن ترش روبی کردن و اظهار کراهیت نمودن
باشد .
لین « بروزن سین» بزبان زند وپازند(۱)
انجر را کوننده
عربی نیز همین نام داررا .
بکسر اول بر وزن مینا » بلفت
زند و پازند (۱) کل راکویند۷ و بعربی طن
خوانند .
وآن مبوه‌است ممروف ودر
وزشمار دگران چون در نیم فو فر است 6
«لغت فری۳۲*.
من ز نیم تو بتیمار گرفتار شدم
نو بتبمار مهل باز بتیم آر مرا . »
( لت رس ۳۵۱ * .
چه ) بسوند صفر )
بازار تهران).
۱ #۹ ۷ و ۳ عو-ی
سلطنت کردند .
6 . #۶
شه دز صفحه ۵8۸
```


## [2026-10-15T02:46:44.505Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-15T02:46:44.521Z] TOOL RESULT

```


```


## [2026-10-15T02:46:46.572Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تیم",
 "prompt": "Give the full Persian etymology section(s) verbatim, especially for the sense 'caravanserai/bazaar' (Sogdian, Chinese origin?)."
}
```


## [2026-10-15T02:46:47.156Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تیمچه",
 "prompt": "Give the Persian etymology verbatim."
}
```


## [2026-10-15T02:46:48.191Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/店",
 "prompt": "Give the Chinese etymology and Middle Chinese / Old Chinese reconstructions for 店, and any mention of Sogdian or Persian borrowings (tym, tīm, تیم)."
}
```


### [2026-10-15T02:46:51.252Z] TOOL RESULT

```
# Persian Etymology

According to the Wiktionary entry, the Persian etymology is:

"From _[تیم](/wiki/%D8%AA%DB%8C%D9%85#Persian "تیم")_ (tim) + _[ـچه](/wiki/%D9%80%DA%86%D9%87#Persian "ـچه")_ (če)."

This indicates that تیمچه (timče) is composed of two morphological elements: the word تیم (tim) combined with the suffix ـچه (če).
```


### [2026-10-15T02:46:54.393Z] TOOL RESULT

```
# Persian Etymology for تیم (tīm)

## Etymology 2: Caravanserai Sense

**Etymology origin:** "Borrowed from Sogdian [script needed] (tym /⁠tēm⁠/, 'inn'), from Middle Chinese 店 (temH)."

**Meaning:** This archaic sense refers to a "caravanserai (especially a large and grand one)" - a type of inn or waystation.

**Related terms:** Synonyms include خان (xân), کاروانسرای (kâravânsarây), and تیمچه (timče).

**Historical attestation:** The word appears in a circa 1060 text by Nāṣir-i Khusraw's *Safarnāma*, where it describes a rental property: "the rent for this **caravanserai**" brought in significant annual revenue and existed among "two hundred caravenserais" in a city.

This etymology demonstrates the word's journey along trade routes from Middle Chinese through Sogdian intermediary into Persian, reflecting historical commercial infrastructure terminology.
```


### [2026-10-15T02:46:57.943Z] TOOL RESULT

```
# Etymology and Historical Reconstructions of 店 (Shop)

## Chinese Etymology
The character 店 is a "phono-semantic compound" combining the semantic radical 广 ("house built to depend on a cliff") with the phonetic element 占.

## Historical Reconstructions

**Middle Chinese:** temH (departing tone)

**Old Chinese reconstructions vary by scholar:**
- Baxter–Sagart system: /\*tˤem-s/
- Zhengzhang Shangfang system: /\*tiːms/

## Sogdian and Persian Borrowings

The document notes a fascinating borrowing chain: "Sogdian: \[script needed\] (tym /⁠tēm⁠/) → Classical Persian: تیم (tēm, 'caravanserai') → Persian: تیمچه (timče, 'small market')."

This demonstrates how the Chinese commercial term traveled westward along trade routes, entering Persian vocabulary with shifted semantic focus toward marketplaces and inns.

[WebFetch note: this page's text is 126215 characters long and the answer above covers only characters 0 to 100000; the final 26215 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-15T02:46:59.773Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/टिट्टिभ",
 "prompt": "Give the Sanskrit etymology, meaning, and descendants (any Persian/Arabic borrowings like تیتو, طیطوی)."
}
```


## [2026-10-15T02:47:00.780Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/titio",
 "prompt": "Give all Latin entries: meanings (verb 'to twitter (of sparrows)'? noun 'firebrand'?) and etymology verbatim."
}
```


## [2026-10-15T02:47:01.803Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/کیش",
 "prompt": "Give the Persian etymology for the sense 'religion, faith' verbatim (Middle Persian kēš, Avestan tkaēša-, Proto-Iranian)."
}
```


## [2026-10-15T02:47:02.770Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أطلس",
 "prompt": "Give Arabic etymology and meanings verbatim for أَطْلَس (satin; smooth; root ط ل س), and any Persian section."
}
```


### [2026-10-15T02:47:07.041Z] TOOL RESULT

```
# Arabic Etymology and Meanings for أَطْلَس

## Etymology 3 (Satin/Adjective/Noun)
This entry derives from the Semitic root **ط ل س** (ṭ l s), containing 3 related terms.

### As Adjective
The adjective describes qualities including "worn-out" with "the quality of a rag," "filthy" with a "dusty hue," and having "skin of dark pigmentation."

### As Noun
The noun **أَطْلَس** (ʔaṭlas) means **"satin"** with plural **طُلْس** (ṭuls).

## Persian Section
The provided document does not include a dedicated Persian language section for this entry. However, it notes that Arabic **اطلس** (atlas) meaning satin descended into Persian as **اطلس** (atlas), which subsequently influenced Hindustani languages (Urdu and Hindi).
```


### [2026-10-15T02:47:07.092Z] TOOL RESULT

```
# Sanskrit Etymology and Meaning of टिट्टिभ

## Etymology
The word derives "from substrate," indicating it originates from non-Indo-European language sources predating Sanskrit's classical period.

## Meaning
टिट्टिभ (ṭiṭṭibha) functions as a noun with two primary definitions:
1. A bird species identified as *Parra jacana* (a tropical wading bird)
2. The name of a particular insect or bug species

## Descendants and Borrowings
The provided Wiktionary entry does not include information about Persian or Arabic borrowings derived from this Sanskrit term, nor does it document later linguistic descendants beyond noting the word's existence across multiple scripts (Devanagari, Bengali, Kannada, Tamil, Telugu, etc.).

The entry indicates the word's gender remains unspecified, marked as a category requesting clarification in Sanskrit linguistics resources.
```


### [2026-10-15T02:47:07.498Z] TOOL RESULT

```
# Persian Etymology for "Religion, Faith"

Based on the Wiktionary article, the Persian term کیش (kêš) meaning "religion" or "faith" is:

**Inherited from Middle Persian** _𐭪𐭩𐭱_ **(kyš /⁠kēš⁠/, "faith; dogma").**

The article does not provide etymological information extending to Avestan or Proto-Iranian forms for this particular sense, despite your request. Only the Middle Persian source is documented in the content provided.
```


### [2026-10-15T02:47:08.145Z] TOOL RESULT

```
# Latin Entry: "titio"

**Meaning:** The entry defines titio as a noun meaning "firebrand (tool)" — specifically a wooden stick used for fire.

**Etymology (verbatim):** "From Proto-Italic *tītjō ("heating"), possibly from Proto-Indo-European *teyh₁- ("to become hot, melt or to end")."

The word is cognate with Old Irish tinaid ("to melt, disappear"), Icelandic þíður ("melted, thawed"), and Hittite terms related to cooking and finishing actions.

**Note:** The page lists titio as a third-declension masculine noun with the genitive form tītiōnis. No verb entry for "twitter" appears in this Latin section.
```


## [2026-10-15T02:47:12.255Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/𐭪𐭩𐭱",
 "prompt": "Give the Middle Persian etymology verbatim (Avestan tkaēša-, Proto-Iranian reconstruction) and descendants."
}
```


## [2026-10-15T02:47:12.994Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/satin",
 "prompt": "Quote the etymology verbatim; does it mention Arabic atlas?"
}
```


### [2026-10-15T02:47:13.478Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:47:16.009Z] TOOL RESULT

```
# Middle Persian Etymology and Descendants for "kyš"

## Etymology

The Middle Persian etymology provided in the Wiktionary article traces back through the following chain:

"From Proto-Iranian *kayšás, from Proto-Indo-Iranian *kayšás, from Proto-Indo-European *kʷoys-ó-s"

The article does not mention Avestan tkaēša- or provide that specific reconstruction.

## Descendants

The documented descendant listed is:

"Persian: کیش (kiš)"

This represents the Modern Persian form that evolved from the Middle Persian term.
```


## [2026-10-15T02:47:20.233Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kayšás",
 "prompt": "Quote etymology, meaning and descendants verbatim (Avestan tkaēša-? Middle Persian kēš? Sogdian?)."
}
```


### [2026-10-15T02:47:20.700Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-10-15T02:47:22.391Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/kayšás",
 "prompt": "Quote etymology, meaning and descendants verbatim (Avestan tkaēša-? Middle Persian kēš?)."
}
```


### [2026-10-15T02:47:23.217Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-10-15T02:47:29.904Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; T=tools/fetch_source.py; python3 $T 'https://en.wiktionary.org/wiki/تیم' --note 'page 510, root Tien: Persian tīm caravanserai < Sogdian tym < MC 店 temH' ; python3 $T 'https://en.wiktionary.org/wiki/تیمچه' --note 'page 510, root Tien: timče = tīm + -če'; python3 $T 'https://en.wiktionary.org/wiki/店' --note 'page 510, root Tien: MC temH, OC *tˤem-s; Sogdian tym descendant'; python3 $T 'https://en.wiktionary.org/wiki/टिट्टिभ' --note 'page 510, root Titi: Skt ṭiṭṭibha Parra jacana, substrate origin'; python3 $T 'https://en.wiktionary.org/wiki/titio' --note 'page 510, root Titi: Latin titio = firebrand only'; python3 $T 'https://en.wiktionary.org/wiki/کیش' --note 'page 510, root Tkaesa: Persian kēš religion < MP kyš'; python3 $T 'https://en.wiktionary.org/wiki/𐭪𐭩𐭱' --note 'page 510, root Tkaesa: MP kēš < PIr *kayšás (PIE *kʷoys-ó-s)'; python3 $T 'https://en.wiktionary.org/wiki/أطلس' --note 'page 510, root T.L.S: Arabic aṭlas satin, root ṭ-l-s; Persian atlas' 2>&1 | tail -3"
}
```


### [2026-10-15T02:47:32.254Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/be0830d702b50183.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4e766f2a7cca9324.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/420d3dbc7339b60c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f76225192cb5a5a0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/577eb6b8cd9c205a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/61e101f76fd72493.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3bee53a942e5fd85.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3329c633bc58c88d.txt
```


## [2026-10-15T02:47:37.350Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -o -i '.\\{100\\}tkaē.\\{100\\}' web/3bee53a942e5fd85.txt web/61e101f76fd72493.txt | head -3; grep -n -o 'اطلس.\\{0,150\\}' refs/MON_part1.txt | head -5; grep -n -o '.\\{0,10\\}تیم.\\{0,120\\}' refs/MON_part1.txt | grep -E 'کاروان|سغد' | head; grep -n -o 'کیش.\\{0,150\\}' refs/MON_part2.txt | grep -i -E 'tka|اوستا|په' | head -3; grep -n 'کیش' refs/incoming/ARY/ARY_pages.txt | head -5; grep -n -i 'KISH\\b\\|KESH\\b' refs/incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-15T02:47:39.159Z] TOOL RESULT

```
14117:اطلس: ۵ (زمعر.] پرنیان» دینا» بارچه 
14122:اطلس تشر یح. 
14124:اطلس. 
14126:اطلسی: :2018 [معر. ف.] (ص نس.) 
14129:اطلس. (گیا.) گیاهی است زینتی 
45690:تیم: «[ (۰.) کاروان‌سرای رکف 
45711:تیمجه. (0-)۱[0-82 (ا.مصف.) کاروانسرای 
15140:ال ها دنل پسگشت‌ها کیش دی
8557:DEvo- (GAUKISH) zEU (RUMANIAN) gle,
11829:REFERENCES beta KASHITAN, KESHIDAN, KESH-
14084:MEKKISH HITTITE) ca MAESTRO S(TTALIAN) gid
```


## [2026-10-15T02:47:41.137Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; sed -n 14115,14125p refs/MON_part1.txt; sed -n 45688,45714p refs/MON_part1.txt; grep -n '^ *کیش\\|کیش:' refs/MON_part2.txt | head"
}
```


### [2026-10-15T02:47:41.757Z] TOOL RESULT

```
حقی که به نوسندة مفاصا حساب پرداخته 
می‌شد» حق الاطلاق) ج. اطلاقات. 
اطلس: ۵ (زمعر.] پرنیان» دینا» بارچه 
ابر شمی. ساده» بی‌برز. (جاذ.) فقر و اول از 
فقرات گردن که بلافاصله زیر استخوان 
قمحدوه قرار گرفته و بر آن سوار است. 
(جف.) کتاب مصور جغرافی» هر کتابی که 
دارای نقشه‌های متعدد باشد: اطلس تشر یح. 
(نج.) سطح مقعر فلکك نهم. (اخ.) اقیانوس 
اطلس. 



تیم: «[ (۰.) کاروان‌سرای رکف 
تیم: :۱1 (.) تعهد» غمخواری. 
: ۱18 (۱.) (ور.) دسته‌ای ورزشکار که در 


از فنون ورزشی کار کنند: تیم فوتبال» 
تیم والیبال. 
تتته ۶ 8 (ع.ف. تیما] (.) نجد؛ 


دشت» سابان. 

تیماج: ۱2 (.) بوست بز دباغی شده. 
تیمار: ۲ (.) خدمت و غمخواری و 
محافظت کسی که بیمار بود؛ تعهد. فکر» 
اند بشه. 

تیمارستان: 1021-0] (امر.) (فره.) 
جابی که دیوانگان را نگهداری و مداوا 
کنند؛ دارالمجانین. 

تیمجه. (0-)۱[0-82 (ا.مصف.) کاروانسرای 
کوچکٌ» سرایی‌دارای چند دکان که تاجران 
در آن داد و ستد کنند. (فره.) 

28879:کیش: (قد. 113)056 (.) آلتی که تبر در آن 
28881:کیش: (قد. ۷35058 (.) دین» آیین 
28882:کیش: (قد. ۱18)654 (.) پر مرغ (مطلق. 
28884:چارکیش: تیر چهار پر. 
28885:کیش (قد. 1316 [- خیش» بزدی» مقنعة 
28888:کیش: (قد. )114 [شمشاد کوتاه و باریکك 
28900:کیش: 5 (صت.) کلمه‌ای که برای راندن 
28903:کیش: 5[* (.) (جاد.) جانوری که از پوستش 
41675:کیش 0 ی هم روی صعحد نمی‌شود 
91482:هم‌کیش: (15026-. (ص.) دارای همان
```


## [2026-10-15T02:47:46.114Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '\\btim\\b|\\btlm\\b|Karawan' HRN.txt HUB.txt | head -5; grep -n -i -E 'tit[iu]' HRN.txt HUB.txt | head -5; grep -n -i 'tittibha\\|titti' AHD_watkins1985.txt IEC.txt SYN.txt | head -3; grep -n -i -E '\\btym\\b|\\btem\\b' PHD.txt | head -3"
}
```


### [2026-10-15T02:47:46.676Z] TOOL RESULT

```
HRN.txt:7253:np. karwän 'Karawane' finden; Nöldeke (mündliche
HRN.txt:16561:öt>äi-tim 132.
HRN.txt:19642:timü/ 109.
HUB.txt:117:Ueber das Vorkommen von np. avar certitudo',
HUB.txt:211:^) Daneben stehen afgh. 5rSr, avar 'injustice* — np. ardra *iniustitia'
HUB.txt:2541:(Vullers: mos, institutum, modus, ratio; apparatus
HUB.txt:3111:867. Das Verhaitniss von np. kamar 'altitude, collis, tumu-
HUB.txt:3849:167. Zd. paititi- = 'Siihne*.
IEC.txt:18458:teteruos (tetruos), a, is *heathcock, caper- cailie'. WP I, 718. Onomat. Skt. cf. (z-gde onomat.) tittirab, m. ‘francolin, partridge’; Medic tétaros, tatüras, s. (phea- sant’; Per. tazarv, s. id. (and “jungle-cock); Gk. cf. tétrix & tétrax, m. 'guinea-fowl, heath- cock’; (LW in) Arm. tatrak, i, av, s. *wood- pigeon’; ON pióurr, pl: piórar, m. *capercailie'; Sw. tjäder, id.; OCS tetrěví, gs: -i, m. “phea- sant ` R téterev, m. fheathcock'; Cz. tetřev *capercailie'; Li. tetervà, tetirvà, f. “black grouse, heath-fowl; Latv. teteris, id.; OPr. tatarwis, f. id.
IEC.txt:18619:Skt. cf. tittiráh, -íh, m. ‘francolin’; Gk. cf. tettix, m. 'tree-cricket'; Lat. titus, gs: -1, m. ‘woodpigeon’; cf. also titius, m. *birdwatcher' and titiae aves ‘wild pigeons’; Li. cf. tytaras,
IEC.txt:18621:m. ‘turkey’; titilvis, m. ‘wader, sandpiper’; Latv. titilbis, id., and Skt. tittibhah ‘jacana, a water-bird'. Cf. also WP I, 742. Long-gde in Gk. tītis, gs: -ídos, f. (“tið or sim. bird) beside titízo, tittubízō, v. ‘chirrup’
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
595:~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišnag [tyfnk! | M tyšng, N ~a] thirsty. ~th: thirst. Tištar [гуй | № ~] astr. Sirius. të [LK < A l-k | M tw, N tu] thou, thee. *tóf [twp | N to] layer. tóhmag [twhmk' | M twhmg, N tuxma] seed; stock, family. tom [t(w)m | M tm, N tam] darkness. -tom [-twm | (M. -dwm)] suffix forming superlative adjectives. tóm [twm | (M twhm, N tuxm)] seed, family. tórag [twlk' | N tora] jackal. tūšag [twšk! | N tófa] provisions. tóxtan, töz- [twhtn', twc- | M twz-, N ~] atone, expiate. ~išn: atonement, expiation. tóz [twe | N ~] bark, skin.
```


## [2026-10-15T02:47:49.536Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 18616,18619p IEC.txt | cut -c1-300"
}
```


### [2026-10-15T02:47:49.968Z] TOOL RESULT

```
Skt. cf. tithah, m. ‘fire’; Lat. titio, gs: -onis, m. ‘firebrand’; Li. cf. tit-nagas, tit-ilingas, m. ‘flint’
(titěn-, see ton-, ten- and extns. Redup. in Skt. tatane, mp. intr. ‘extend’; titanis-, desid. ‘would extend’; Gk. titaíno, v. ‘extend’. NB. For ON biðna, v. ‘thaw’, cf. tài- (1) bíða)
titt- (tit-) element in bird-names. Cf. WP I, 718. Onomat.
Skt. cf. tittiráh, -íh, m. ‘francolin’; Gk. cf. tettix, m. 'tree-cricket'; Lat. titus, gs: -1, m. ‘woodpigeon’; cf. also titius, m. *birdwatcher' and titiae aves ‘wild pigeons’; Li. cf. tytaras,
```


## [2026-10-15T02:48:12.205Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A2 '^تیتو\\|^طیطو' MON_part1.txt MON_part2.txt | head; grep -c 'تیتو' incoming/ARY/ARY_pages.txt; grep -n -i 'titio\\|titiare' LEW_1910.txt LAT.txt | head -5"
}
```


### [2026-10-15T02:48:12.586Z] TOOL RESULT

```
0
LAT.txt:3404:peut-etre k 1'influence de fluuius (sur la r6partition des formes
LAT.txt:4810:cher". Dans les mas., Ia r6partition de arcesso et de accerso d6pend
LAT.txt:7566:parce que bouis ivite la ripetition de w qui aurait lieu dans uouis ;
LAT.txt:12001:La forme A repetition circumcirca appartient surtout k la langue popu¬
LAT.txt:16281:d'oh dentitio, et par haplologie dentiS; M.L.3565; dentex ( dentix)
```


## [2026-10-15T02:48:14.798Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *titi|titi[oō], ' LAT.txt LEW_1910.txt | head -5; grep -n 'تیتو\\|طیطو' MON_part1.txt MON_part2.txt | head -4"
}
```


### [2026-10-15T02:48:15.163Z] TOOL RESULT

```
LAT.txt:16281:d'oh dentitio, et par haplologie dentiS; M.L.3565; dentex ( dentix)
LAT.txt:28279:titia est, ut eam nemo hominem ( = nne creature hnnaine) appellare
LAT.txt:45490:ont etd faits postdrieurement bi-, tri-pertio,-is, bi-pertitio, etc.;
LAT.txt:47189:(= opeEjtc), appetitio, cf.Cic., Fin.3,33; Ac.3,34; Tuse.4,13, -tibilis,
LAT.txt:47741:Cf. titio, titiunculus. Les formes en pip(p) sont frequentes dans
MON_part2.txt:87190:دریا: مرغی است افسانه‌ای که آن را طیطو 
MON_part2.txt:87191:هم گویند (هرچند طیطو به دو نوع مرغ 
MON_part1.txt:194:سلسله کتب فارسی و عربی از طرف انیستیتوی ابران و فرانسه (به فارسی و 
MON_part1.txt:312:(فارسی - فرانسوی) حاپ انیستیتوی ايران و فرانسه. تهران ۱۳۳۲ (حائز جابرة
```


## [2026-10-15T02:48:16.851Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 47730,47745p LAT.txt; grep -n -E '^titi' LAT.txt | head; sed -n 87186,87193p MON_part2.txt"
}
```


### [2026-10-15T02:48:17.279Z] TOOL RESULT

```
piulare, M.L.6551), piailler, glousser"; C&M.L.6533 pipilare (arec t);
geri.: r.b.a.£/t//a, etc.
Formes nominales: pipi 5 : jeune oiseau qui pianle; pipiones, pulli
columbam* (Gloss.), cf.M.L.6533a pipiS et *pibio > fr. pigeon; r. Rer.
de ling. roaane, I 336; pipiunculus: accipiter, accipitor (Gloss.);
pipizS, -Vnis a.: petit de la grue; pipStiS,-Snis f.: — clamor plorantis
lingua Oscorum , P.F.335,11; pipulum (pipulus): criaillerie, cbari-
rari; cf. Varr., L.L.7,103 [pioutus] in Aulularia (446): "pipulo te
differam ante aedis", i.e. conuicio, declinatum a pi<p>atu pullorum.
Faut-il y rattacher *pi (p)po, -.as, *pip(p)a, dUiproriennent les
aots du type fr .pipe, M.L. 6530 ( cf. O.Blocb, Dict. 6tya.), iri. etc.?
Cf. titio, titiunculus. Les formes en pip(p) sont frequentes dans
les langues i.-e.: aStr.pippaka, pippikali "sorte d*oiseau", gr. 7 ti 7 toc,
nnaiiCfo, etc.
PipilT) r appelle sibilV pour la formation.
pipinna, -ae f.: parna mentula (Mart.11,73,1). Mot enfantin; cf.
28279:titia est, ut eam nemo hominem ( = nne creature hnnaine) appellare
56979:titive qu'admet sisto, il fallait une sorte de causatif; or, le
64579:titia} xpea vrjiuajv $ Xefoucn, CGL II 198,43« Glose obscure;
64582:titillti, -as, -aui, -itum, -are: chatouiller (sens physique et
64590:titilldmentum (Fulg.), tit i l latus (Plin., Cael.Aur.). Certaines formes
64597:titillus est le meme qu'entre mamma et mamilla. Cf. aussi tittex.
64600:titio, -onis m.: tison. Mot populaire d'aprbs Lactance, 4,14:
64601:titionem uulgus appellat extractum foco torrem semiustum et extinctum.
64604:titio, - 5 s: pdpier. Autre forme de pipio. Cf. le suivant.
(-دربار) نماینده‌ای بوده است که امرا و 
حکام اطراف در درگاه پادشاه مقیم 
می‌داشته‌اند که کارهای مربوط به ابشان را 
انجام دهد و مراقت مصلاح کار باشد. و کیل 
دریا: مرغی است افسانه‌ای که آن را طیطو 
هم گویند (هرچند طیطو به دو نوع مرغ 
مو جود اطلاق شده.) سیمرغ دربا. وکیل 
دبوان اعلی: ممکن است این وکیل دیوان
```


## [2026-10-15T02:48:18.682Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 64600,64612p LAT.txt"
}
```


### [2026-10-15T02:48:19.026Z] TOOL RESULT

```
titio, -onis m.: tison. Mot populaire d'aprbs Lactance, 4,14:
titionem uulgus appellat extractum foco torrem semiustum et extinctum.
Attest£ depuis Varron. Panroman. M.L.8758. C{.*attitiare "attiser",
M.L.769.
titio, - 5 s: pdpier. Autre forme de pipio. Cf. le suivant.
tl tlun culus, -I m.: xeyxptc,, ei8o$ lepaxoc p.txpou CGL II 347,13;tltta •
1334
dont il exiate an doublet pipiunculus: accipiter, acceptor (Gloas.).
Utrasque d'apros Nebring, Glotta XIV 153V Cf. tinnid.
%
tltta: r.titille.
tlttex: nucrotj CGL II 198,38* Sans donte a rapprocher de titil¬
lus, titta,
```


## [2026-10-15T02:50:19.777Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-510.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nE=[]\n# ---------- entry 0 Tien\nE.append({\"entry\":0,\"root\":\"Tien\",\"verdict\":\"confirmed\",\n\"modern_form\":\"Middle Chinese 店 temH 'shop, inn' (Mandarin diàn; Old Chinese *tˤem-s, Baxter-Sagart)\",\n\"note\":\"Nourai's 'Tien' is a Wade-Giles-style spelling of Mandarin diàn 店 'shop, store; inn'. Wiktionary (s.v. 店 and Persian تیم) gives exactly Nourai's chain: Middle Chinese temH → Sogdian tym /tēm/ 'inn' → Classical Persian tīm/tēm 'caravanserai' → timče. Gharib's Sogdian dictionary (SOD p.394, entry 9747) has tym 'inn, resting place' with a reference to Henning's loanword study. The Sogdian box prints only the gloss 'bazaar, inn' (no Sogdian word); the extraction copied that faithfully into the translit field. ETM (Nourai's source) is not accessible.\",\n\"note_fa\":\"ریشه واژهٔ چینی 店 (چینی میانه temH، ماندارین diàn) به معنای «دکان، مسافرخانه» است و «Tien» نورایی صورت لاتینی کهنهٔ همین واژه است. ویکی‌واژه و فرهنگ سغدی قریب زنجیرهٔ نورایی را تأیید می‌کنند: چینی temH ← سغدی tym (tēm) «مسافرخانه» ← فارسی «تیم» «کاروانسرای بزرگ» و «تیمچه». ادعای نورایی درست است؛ تنها در خانهٔ سغدی خود واژه چاپ نشده و فقط معنا آمده است.\",\n\"sources\":[W+\"店\",W+\"تیم\"],\n\"ref_check\":[{\"ref\":\"ETM:63\",\"status\":\"not_checked\",\"note\":\"ETM not available (refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: not found').\"}],\n\"consulted\":[{\"src\":\"SOD\",\"where\":\"p.394 (SOD_pages.txt leaf 461, running head '394'), entries 9747, 9750\",\"stance\":\"supports\",\"note\":\"'9747 tym ... inn, resting place ... STi 36.2; pl. tymu STii 3.27; Hen. LW' (Henning, loanword) and '9750 tymp'y ... tem-pase ... inn-keeper' — Sogdian tēm 'inn' as a loanword.\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Sogdian\",\"words\":\"bazaar, inn\",\"verdict\":\"confirmed\",\n\"derivation\":\"The box gives no Sogdian form, only the gloss 'bazaar, inn'; the word meant is Sogdian tym /tēm/ 'inn, resting place' (Gharib no. 9747; also tympʾy 'inn-keeper'), borrowed from Middle Chinese 店 temH along the Silk Road where Sogdian merchants ran the caravan trade (Tang period, 7th–8th c.). Chinese -e- was rendered by Sogdian ē (written -y-). The gloss 'bazaar' is looser than the attested 'inn'.\",\n\"derivation_fa\":\"در این خانه واژهٔ سغدی چاپ نشده و تنها معنا آمده است؛ واژهٔ مورد نظر سغدی tym (tēm) «مسافرخانه، منزلگاه» است (قریب، شمارهٔ ۹۷۴۷) که بازرگانان سغدی در راه ابریشم از چینی میانه 店 temH وام گرفتند. معنای «بازار» در کتاب گشاده‌تر از معنای ثبت‌شده («مسافرخانه») است، ولی وام‌گیری از چینی درست است.\",\n\"sources\":[W+\"店\"],\n\"ref_check\":[{\"ref\":\"ETM:63\",\"status\":\"not_checked\",\"note\":\"ETM not accessible.\"},\n {\"ref\":\"SOD:394\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 461 has running head '394'; entry 9747 'tym ... inn, resting place ... Hen. LW'. Page reference correct.\"}],\n\"consulted\":[{\"src\":\"SOD\",\"where\":\"p.394, entry 9750\",\"stance\":\"supports\",\"note\":\"'tymp'y C ... tem-pase ... inn-keeper' (tēm + pāse 'keeper') confirms tēm 'inn'.\"},\n {\"src\":\"PHD\",\"where\":\"grep 'tym'\",\"stance\":\"silent\",\"note\":\"MacKenzie has only tēmār [tymʾl] 'sorrow, care'; no Pahlavi *tēm 'inn' — consistent with the word entering Persian via Sogdian, not Middle Persian.\"}]},\n{\"id\":2,\"parent\":1,\"lang\":\"Persian\",\"words\":\"tîm\",\"verdict\":\"confirmed\",\n\"derivation\":\"Classical Persian tīm (older tēm) 'large caravanserai' (attested in Nāṣir-i Khusraw's Safarnāma, c.1050, and in the Lughat-i Furs verse quoted by Nourai) is a Sogdian loan (tym tēm 'inn') entering Persian in Transoxiana in the early New Persian period; Sogdian ē > Persian ī with the general merger of majhūl ē into ī. The diminutive timče (tīm + -če) 'small caravanserai, covered arcade of shops' is the living word ('bazaar' sense).\",\n\"derivation_fa\":\"«تیم» در فارسی کهن به معنای «کاروانسرای بزرگ» است (سفرنامهٔ ناصرخسرو؛ بیت لغت فرس) و از سغدی tēm «مسافرخانه» وام گرفته شده که خود از چینی 店 است؛ یای مجهول ē در فارسی امروز به ī بدل شده. «تیمچه» (تیم + چه) کاروانسرای کوچک و راستهٔ دکان‌های سرپوشیده است. برهان قاطع و معین همین معنا را می‌آورند؛ ادعای نورایی درست است.\",\n\"sources\":[W+\"تیم\",W+\"تیمچه\"],\n\"ref_check\":[{\"ref\":\"ETM:63\",\"status\":\"not_checked\",\"note\":\"ETM not accessible.\"},\n {\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"Mo'in (2-vol abridgement, MON_part1.txt line 45690) 'تیم: ... کاروان‌سرای' and line 45711 'تیمچه ... کاروانسرای کوچک، سرایی دارای چند دکان که تاجران در آن داد و ستد کنند'.\"},\n {\"ref\":\"BQT:547\",\"status\":\"supports\",\"note\":\"BQT_v1_pages.txt leaf 775 (last page of vol.1, continuation note to p.548): 'تیم - بر وزن میم، کاروان سرای بزرگ را گویند و تیمچه کاروان سرای کوچک است' with footnote verse 'من ز تیم تو بتیمار گرفتار شدم / تو بتیمار مهل باز بتیم آر مرا (لغت فرس ۳۵۱)' — the verse Nourai quotes. Mo'in's etymological footnote is illegible in the OCR.\"}],\n\"consulted\":[{\"src\":\"HRN\",\"where\":\"grep 'tim'\",\"stance\":\"silent\",\"note\":\"Horn has no entry tīm.\"},\n {\"src\":\"HUB\",\"where\":\"grep 'tim'\",\"stance\":\"silent\",\"note\":\"No entry.\"},\n {\"src\":\"PHD\",\"where\":\"grep 'tym'\",\"stance\":\"silent\",\"note\":\"Only tēmār 'care' (→ NP tīmār); no *tēm 'inn' in Pahlavi.\"}]}]})\n# ---------- entry 1 Titi\nE.append({\"entry\":1,\"root\":\"Titi, Titil\",\"verdict\":\"plausible\",\n\"modern_form\":\"onomatopoeic ti-ti-, (ti)til- 'imitation of bird calls' (Pokorny 1086: 'kaum ursprachlich')\",\n\"note\":\"Pokorny p.1086 lists 'ti-ti-, (ti)til- Nachahmung von Vogelrufen; kaum ursprachlich' — a recurrent sound-imitative element, not a true PIE root (Walde-Pokorny I 742: 'ursprachliches Alter nicht erweislich'). Nourai's root and gloss match Pokorny, but the label 'Indo-European' overstates it. Sanskrit ṭiṭṭibha is real; the Persian tītū/ṭīṭū is indeed borrowed from it via Burzoy's Pahlavi Kalīla wa Dimna (Mo'in). The Latin gloss is wrong: titiō, -āre is a verb 'to twitter (of the sparrow)' (Pokorny; Ernout-Meillet: 'pépier'), not a noun 'sparrow'.\",\n\"note_fa\":\"پوکورنی (ص ۱۰۸۶) «ti-ti-, (ti)til-» را «تقلید آواز پرندگان» و «به‌سختی هندواروپایی آغازین» می‌داند؛ پس این یک عنصر نام‌آوا (onomatopoeia) است نه ریشهٔ واقعی. واژهٔ سنسکریت ṭiṭṭibha درست است و «تیتو/طیطو»ی فارسی، به گفتهٔ معین، از همین واژه از راه ترجمهٔ پهلوی کلیله و دمنه به دست برزویه آمده است. معنای «گنجشک» برای لاتین titiō نادرست است: titiō فعلی است به معنای «جیک‌جیک کردن (گنجشک)». ادعای نورایی با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"टिट्टिभ\",W+\"titio\"],\n\"ref_check\":[{\"ref\":\"POK:1086\",\"status\":\"supports\",\"note\":\"POK_03.txt line ~4667 (page 1086): 'ti-ti-, (ti)til- Nachahmung von Vogelrufen; kaum ursprachlich. Ai. tittibha- m. Parra jacana; lett. titilbis ... Wasserläufer; ... lat. titiō, -āre zwitschern vom Sperling; lett. titēt singen. WP. I 742, WH. II 686, Mayrhofer 1, 457.'\"}],\n\"consulted\":[{\"src\":\"WLD\",\"where\":\"Bd. I p.742 (WLD_Bd1_pages.txt leaf 751)\",\"stance\":\"supports\",\"note\":\"'ti-ti-, (ti)til- „Nachahmung von Vogelrufen“; ursprachliches Alter nicht erweislich. Ar. tittibha-h „Parra jacana“; lett. titilbis ... lat. titio, -are „zwitschern, vom Sperling“'.\"},\n {\"src\":\"IEC\",\"where\":\"line 18618 s.v. titt- (tit-)\",\"stance\":\"supports\",\"note\":\"'titt- (tit-) element in bird-names. Cf. WP I, 718. Onomat. ... Lat. titus ‘woodpigeon’ ... Skt. tittibhah ‘jacana, a water-bird’. Cf. also WP I, 742.'\"},\n {\"src\":\"AHD\",\"where\":\"grep 'titi'\",\"stance\":\"silent\",\"note\":\"Watkins has no titi- root (not a reconstructable root).\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Sanskrit\",\"words\":\"tittibha\",\"verdict\":\"plausible\",\n\"derivation\":\"Sanskrit ṭiṭṭibha- m. 'Parra jacana / red-wattled lapwing' (the 'ṭiṭṭibha and the ocean' fable of the Pañcatantra) is a reduplicated imitation of the bird's cry; Pokorny and Walde-Pokorny list it under ti-ti-, but its retroflex ṭ-ṭṭ- point to a Middle-Indic/substrate formation (Wiktionary: 'from substrate'; Mayrhofer onomatopoeic). The word and gloss are correct; 'descends from PIE' is only true in the loose sense of a shared sound-imitation.\",\n\"derivation_fa\":\"سنسکریت ṭiṭṭibha «مرغ آبی، دیتار/کاکایی» (در داستان پنچه‌تنتره) واژه‌ای نام‌آوا با تکرار هجاست. پوکورنی آن را زیر ti-ti- آورده، ولی واج‌های برگشتی ṭ آن نشان از ساخت هندیِ میانه یا زبان زیرین دارد (ویکی‌واژه: «از زبان زیرین»). واژه و معنا درست است، اما پیوند آن با هندواروپایی آغازین تنها از راه تقلید آواست.\",\n\"sources\":[W+\"टिट्टिभ\"],\n\"ref_check\":[{\"ref\":\"POK:1086\",\"status\":\"supports\",\"note\":\"'Ai. tittibha- m. Parra jacana' under ti-ti-, with 'kaum ursprachlich'.\"}],\n\"consulted\":[{\"src\":\"WLD\",\"where\":\"Bd. I p.742\",\"stance\":\"supports\",\"note\":\"'Ar. tittibha-h „Parra jacana“'.\"},\n {\"src\":\"IEC\",\"where\":\"line 18621\",\"stance\":\"supports\",\"note\":\"'Skt. tittibhah ‘jacana, a water-bird’' under titt- 'element in bird-names ... Onomat.'\"}]},\n{\"id\":2,\"parent\":1,\"lang\":\"Persian\",\"words\":\"tîtŭ\",\"verdict\":\"confirmed\",\n\"derivation\":\"Persian tītū / ṭīṭū (also ṭīṭawī, ṭīṭāw) 'a water bird, sandpiper/lapwing' comes from Sanskrit ṭiṭṭibha through the Pañcatantra: Burzoy's 6th-c. Pahlavi translation (Kalīlag ud Damanag) carried the bird of the fable, Ibn al-Muqaffaʿ's Arabic Kalīla wa Dimna has ṭīṭawā/ṭīṭawī, and Rudaki's verse version already has tītū (Lughat-i Furs 418). The variant spelling with ط (طیطو) reflects the Arabic-mediated form; Mo'in states the whole route on the cited page.\",\n\"derivation_fa\":\"«تیتو» یا «طیطو/طیطوی» نام مرغی آبی است. معین در حاشیهٔ برهان قاطع (ص ۱۳۶۴) می‌گوید از سنسکریت tittibha است و به دست برزویه، مترجم کلیله و دمنه به پهلوی، به آن زبان راه یافت و در فارسی به صورت «تیتو» درآمد (بیت رودکی: «پادشا سیمرغ دریا را ببرد / خایه و بچه بدان تیتو سپرد»)؛ در کلیلهٔ ابن مقفع و ترجمهٔ نصرالله منشی «طیطوی» آمده است. صورت با «ط» معرّب است. ادعای نورایی درست است.\",\n\"sources\":[W+\"टिट्टिभ\"],\n\"ref_check\":[{\"ref\":\"BQT:1364\",\"status\":\"supports\",\"note\":\"BQT vol.3 pdf page 157, printed 1364 (read from image; saved to ocr/BQT/1364.vision.txt): 'طیطاو - ... نوعی از مرغابی باشد؛ وطیتو نیز گفته‌اند'; fn.2 'طیطوی = تیتو، از سانسکریت tittibha (مرغی است) ... این کلمه توسط برزویه مترجم کلیله ودمنه بپهلوی، وارد زبان مزبور شد ودرفارسی بصورت تیتو درآمد'. Note: ref_page.py's default offset lands on pdf p.159 (start of ع); the correct pdf page is 157.\"}],\n\"consulted\":[{\"src\":\"MON\",\"where\":\"MON_part2.txt line 87190 s.v. وکیل دریا\",\"stance\":\"partial\",\"note\":\"'وکیل دریا: مرغی است افسانه‌ای که آن را طیطو هم گویند (هرچند طیطو به دو نوع مرغ موجود اطلاق شده)' — confirms the bird name, no etymology in the abridgement.\"},\n {\"src\":\"HRN\",\"where\":\"grep 'tit'\",\"stance\":\"silent\",\"note\":\"No entry tītū in Horn.\"},\n {\"src\":\"HUB\",\"where\":\"grep 'tit'\",\"stance\":\"silent\",\"note\":\"No entry.\"}]},\n{\"id\":3,\"parent\":0,\"lang\":\"Latin\",\"words\":\"titiô\",\"verdict\":\"plausible\",\n\"derivation\":\"Latin titiō, -āre is a rare verb 'to twitter, cheep' used of the sparrow (Pokorny: 'zwitschern vom Sperling'; Ernout-Meillet: 'titio, -ās: pépier. Autre forme de pipio'), an imitative formation parallel to pipiō 'to peep'. It belongs with ti-ti- only as onomatopoeia. Nourai's gloss 'sparrow' misreads Pokorny's 'vom Sperling'; the homonymous noun titiō, -ōnis 'firebrand' (Wiktionary) is unrelated. The closest Latin bird noun is titus 'wood-pigeon' (Mann).\",\n\"derivation_fa\":\"لاتین titiō, -āre فعلی کم‌کاربرد به معنای «جیک‌جیک کردن» است که دربارهٔ گنجشک به کار رفته (پوکورنی؛ ارنو-میه: «جیک‌جیک کردن، صورت دیگر pipio»). این واژه نیز نام‌آواست. معنای «گنجشک» که نورایی داده برداشت نادرست از عبارت پوکورنی «از گنجشک» است؛ اسم titiō به معنای «هیزم نیم‌سوخته» هم‌آوای بی‌ارتباط است. پیوند با ti-ti- پذیرفتنی است ولی معنا اصلاح می‌خواهد.\",\n\"sources\":[W+\"titio\"],\n\"ref_check\":[{\"ref\":\"POK:1086\",\"status\":\"partial\",\"note\":\"Pokorny p.1086: 'lat. titiō, -āre zwitschern vom Sperling' — the word is there, but as a verb 'to twitter (of the sparrow)', not a noun 'sparrow'.\"}],\n\"consulted\":[{\"src\":\"LAT\",\"where\":\"Ernout-Meillet p.~1334 (LAT.txt line 64604)\",\"stance\":\"partial\",\"note\":\"'titio, -ās: pépier. Autre forme de pipio.' and separately 'titio, -onis m.: tison' — verb 'to chirp', not 'sparrow'.\"},\n {\"src\":\"WLD\",\"where\":\"Bd. I p.742\",\"stance\":\"partial\",\"note\":\"'lat. titio, -are „zwitschern, vom Sperling“'.\"},\n {\"src\":\"IEC\",\"where\":\"line 18616/18619\",\"stance\":\"partial\",\"note\":\"Lists 'Lat. titio ... ‘firebrand’' under a different root and 'Lat. titus ‘woodpigeon’' under titt- bird-names; no titio 'sparrow'.\"}]}]})\n# ---------- entry 3 Tkaesa\nE.append({\"entry\":3,\"root\":\"Tkaeša\",\"verdict\":\"plausible\",\n\"modern_form\":\"Avestan tkaēša- m. 'doctrine, (religious) teaching; teacher; legal ruling' (Bartholomae col. 812-813)\",\n\"note\":\"Avestan tkaēša- is real (Bartholomae col. 812-813: 1) 'Lehre, Glaubenslehre', in the Gāthās especially 'false doctrine'; 2) 'Lehrer'; also 'Rechtsentscheid, Richter'). Nourai's gloss 'agreement, commitment' follows Horn no. 880 ('Bekenntniss, Gelöbniss') and Mo'in in Borhan ('اعتراف، عهد'), an older interpretation; modern lexica give 'doctrine, teaching'. The line Av. tkaēša- → MP kēš 'faith, dogma (esp. non-Mazdean)' → NP kēš 'religion' is standard (Horn, Nyberg, MacKenzie, Mo'in). Wiktionary instead reconstructs MP kēš < Proto-Iranian *kayšás (PIE *kʷoys-ó-s) without the t-, which is a minority/alternative statement of the same connection (the Avestan tk- would be simplified to k- in Western Iranian either way).\",\n\"note_fa\":\"اوستایی tkaēša- واژه‌ای واقعی است و بارتولومه آن را «آموزه، آموزهٔ دینی» (در گاهان بیشتر «آموزهٔ دروغین»)، «آموزگار» و «حکم دینی» معنا کرده است. معنای «پیمان، تعهد» نورایی از هرن (Bekenntnis, Gelöbnis) و معین در حاشیهٔ برهان («اعتراف، عهد») گرفته شده که برداشتی کهنه‌تر است. زنجیرهٔ اوستایی tkaēša- ← پهلوی kēš ← فارسی «کیش» را هرن، نیبرگ، مکنزی و معین می‌پذیرند؛ پس ریشه درست است ولی معنای آن با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"کیش\",W+\"𐭪𐭩𐭱\"],\n\"ref_check\":[{\"ref\":\"BQT:1755\",\"status\":\"supports\",\"note\":\"BQT p.1755 (ocr/BQT/1755.txt) s.v. کیش fn.2: 'اوستا tkaēša (اعتراف، عهد). پهلوی kēš ... ارمنی ... در اوستا «تکئشه» در مورد آیین اهریمنی استعمال شده در مقابل «دئنا» (دین) ولی در فارسی کیش بمعنی مطلق آیین ودین آمده: لب یاقوت رنگ ونالهٔ چنگ ... کیش زرتهشتی. دقیقی طوسی' — Nourai's gloss, chain and verse all come from here.\"},\n {\"ref\":\"HRN:196\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 217 = p.196, no. 880: 'kēš Religion. aw. tkaēša- Bekenntniss, Gelöbniss ...; phlv. kēš, vergl. pōryōtkēš; arm. LW. k'ēš'.\"}],\n\"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 812-813 s.v. tkaēša-\",\"stance\":\"partial\",\"note\":\"'tkaēša- m. 1) Lehre bes. auf religiösem Gebiet, Glaubenslehre; a) im gAw. spez. von der Lehre des falschen Glaubens Irr-, Afterlehre' ... 'tkaēša- m. 1) Lehrer ... 2) ... Richter' — same word, but 'doctrine/teacher', not 'agreement'.\"},\n {\"src\":\"NYB\",\"where\":\"Part II p.~123 (leaf 131) s.v. kēš\",\"stance\":\"supports\",\"note\":\"'kēš [kyš] faith, religion, both of the Zoroastrian religion and of others ... — Av. (812 sq.) tkaēša-; MPrs kyš doctrine, dogma; NP kēš'.\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"kěš\",\"verdict\":\"confirmed\",\n\"derivation\":\"Pahlavi (Zoroastrian Middle Persian) kēš [kyš], Manichaean MP kyš 'faith, dogma, (esp. non-Mazdean) creed', with kēšdār 'sectary'; it continues Old Iranian *tkaiša- (Av. tkaēša-) with the initial cluster tk- simplified to k- and OIr. ai monophthongised to ē; the compound pōryōtkēš 'of the first teaching' is a learned borrowing of Av. paoiryō.tkaēša- that preserves the t-. Armenian borrowed it as k'ēš 'religion'.\",\n\"derivation_fa\":\"پهلوی kēš «دین، آیین (به‌ویژه آیین غیرزرتشتی)»، و در مانوی kyš «اصول عقیده»؛ از ایرانی باستان *tkaiša- (اوستایی tkaēša-) با افتادن t آغازین از خوشهٔ tk- و تبدیل ai به ē. واژهٔ عالمانهٔ pōryōtkēš «پیرو آموزهٔ نخستین» t کهن را نگه داشته است. ارمنی k'ēš را از همین وام گرفته است. ادعای نورایی درست است.\",\n\"sources\":[W+\"𐭪𐭩𐭱\"],\n\"ref_check\":[{\"ref\":\"MON:3153\",\"status\":\"not_checked\",\"note\":\"6-vol Mo'in page 3153 not accessible; the 2-vol abridgement (MON_part2.txt line 28881) has 'کیش: ... دین، آیین' without the Pahlavi form.\"}],\n\"consulted\":[{\"src\":\"PHD\",\"where\":\"s.v. kēš (PHD.txt line 428)\",\"stance\":\"supports\",\"note\":\"'kēš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dār sectary, non-Mazdean'; also 'pōryōtkēš = Av. paoiryō.tkaēša-'.\"},\n {\"src\":\"NYB\",\"where\":\"Part II s.v. kēš and pūryōtkēš\",\"stance\":\"supports\",\"note\":\"'kēš [kyš] faith, religion ... — Av. (812 sq.) tkaēša-'; 'pūryōtkēš ... Borrowed from Av. paoiryō.tkaēša-, cf. kēš'.\"}]},\n{\"id\":2,\"parent\":1,\"lang\":\"Persian\",\"words\":\"kîš 3\",\"verdict\":\"confirmed\",\n\"derivation\":\"New Persian kēš > kīš 'religion, creed' continues Pahlavi kēš unchanged except for the later merger of majhūl ē into ī; in Avestan the word mostly meant the doctrine of the false faith, but in Persian it became a neutral word for 'religion', as in Daqīqī's 'mey-e la'l-gun o kīš-e zartoshtī' (quoted by Nourai from Borhan). Homonyms kīš 'quiver' and the island Kīš are unrelated (Mo'in lists them separately, hence Nourai's index 3).\",\n\"derivation_fa\":\"«کیش» فارسی (kēš ← kīš) دنبالهٔ پهلوی kēš است و تنها یای مجهول آن در فارسی امروز به یای معروف بدل شده. در اوستا بیشتر دربارهٔ آیین اهریمنی به کار می‌رفت ولی در فارسی معنای عام «دین و آیین» یافت، چنان‌که در بیت دقیقی «می لعلگون و کیش زرتهشتی». «کیش» به معنای ترکش و جزیرهٔ کیش هم‌آوای بی‌ارتباط‌اند. ادعای نورایی درست است.\",\n\"sources\":[W+\"کیش\"],\n\"ref_check\":[{\"ref\":\"HRN:196\",\"status\":\"supports\",\"note\":\"Horn no. 880 p.196 'kēš Religion. aw. tkaēša- ...; phlv. kēš'.\"},\n {\"ref\":\"BQT:1755\",\"status\":\"supports\",\"note\":\"Borhan p.1755 'کیش ... دین و آیین' fn.2 'اوستا tkaēša ... پهلوی kēš ... در فارسی کیش بمعنی مطلق آیین ودین آمده' with Daqīqī's verse.\"},\n {\"ref\":\"MON:3153\",\"status\":\"not_checked\",\"note\":\"6-vol page not accessible; abridgement line 28881 'کیش: ... دین، آیین'.\"}],\n\"consulted\":[{\"src\":\"HUB\",\"where\":\"pp.89-90 (notes on Horn 873-881)\",\"stance\":\"silent\",\"note\":\"Hübschmann comments on Horn 873, 874, 875, 881 but makes no correction to no. 880 kēš — tacit acceptance.\"},\n {\"src\":\"PHD\",\"where\":\"s.v. kēš\",\"stance\":\"supports\",\"note\":\"'kēš [kyš | = M, N ~] dogma, faith' — N(ew Persian) same form.\"},\n {\"src\":\"ARY\",\"where\":\"grep 'کیش' / KESH\",\"stance\":\"silent\",\"note\":\"Aryanpur has KESHIDAN (kašīdan) but no entry for kīš 'religion'.\"}]}]})\n# ---------- entry 4 TLS\nE.append({\"entry\":4,\"root\":\"T.L.S\",\"verdict\":\"confirmed\",\n\"modern_form\":\"Arabic root ṭ-l-s (ط ل س): ṭalasa 'to efface, wipe out (writing)'; aṭlas 'smooth, worn; dusky; satin'\",\n\"note\":\"Klein s.v. atlas 'silk-satin': 'Arab. aṭlas, lit. wiped smooth, fr. ṭalasa, he wiped, smoothed away' — exactly Nourai's root and gloss. Wiktionary lists aṭlas 'satin' under root ṭ-l-s and notes the Persian loan اطلس. Lokotsch no.131 explains the semantic route: aṭlas 'smooth, fine' (also 'worthless') applied to silk, then the adjective alone named silk-satin, whence Turkish/Russian/German Atlas. SAP (Sayyah) not accessible.\",\n\"note_fa\":\"ریشهٔ عربی ط‌ل‌س (طَلَسَ «پاک کردن، زدودن نوشته») است و «أطلس» یعنی «صاف، ساییده، بی‌نقش» و سپس «پارچهٔ ابریشمی صاف». کلاین می‌گوید: «عربی aṭlas به معنای لفظی صاف‌شده، از ṭalasa: پاک کرد، صاف کرد». لوکوتش نیز نشان می‌دهد که این صفت نخست دربارهٔ ابریشم ساده به کار رفت و سپس خود نام پارچه شد. ادعای نورایی درست است.\",\n\"sources\":[W+\"أطلس\"],\n\"ref_check\":[{\"ref\":\"KLN:122\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 76 (≈pp.122-127): 'atlas, n., silk-satin. — Arab. atlas, lit. ‘wiped smooth’, fr. talasa, ‘he wiped, smoothed away’.'\"},\n {\"ref\":\"SAP:964\",\"status\":\"not_checked\",\"note\":\"Sayyah's dictionary not available (refs_online.json: kind 'purchase').\"}],\n\"consulted\":[{\"src\":\"LKT\",\"where\":\"p.12 (LKT.txt leaf 38), no.131\",\"stance\":\"supports\",\"note\":\"'131. Ar. aṭlas: Glatt, fein. ... ebenso von Seide, sie sei aṭlas ... schließlich blieb das Adjektiv allein zur Bezeichnung des Stoffes ... des sog. Seidensatins. Rum. atlas ... russ. atlas ... Dtsch. Atlas'.\"},\n {\"src\":\"HJB\",\"where\":\"s.v. ATLAS (HJB.txt line 2276)\",\"stance\":\"supports\",\"note\":\"'ATLAS, s. An obsolete word for satin, from the Ar. aṭlas used in that sense, literally bare or bald'.\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Arabic\",\"words\":\"atlas\",\"verdict\":\"confirmed\",\n\"derivation\":\"Arabic aṭlas is an afʿal adjective of ṭ-l-s: 'effaced, worn smooth, plain (without design); dusky-coloured', used of a plain, unfigured silk; as a noun aṭlas (pl. ṭuls) came to mean 'satin'. Nourai's 'a wiped, clean silk cloth' paraphrases the 'smoothed/effaced' sense correctly. The same adjective in falak al-aṭlas 'the plain (starless) ninth sphere' explains Persian falak-e atlas.\",\n\"derivation_fa\":\"«أطلس» صفتی بر وزن أفعل از ریشهٔ ط‌ل‌س است به معنای «زدوده، ساییده و صاف، بی‌نقش؛ تیره‌رنگ»، و دربارهٔ ابریشم ساده و بی‌نقش به کار رفت تا خود نام «اطلس/ساتن» شد (جمع: طُلْس). «فلک اطلس» (فلک نهم بی‌ستاره) نیز از همین معنای «بی‌نقش» است. ادعای نورایی درست است.\",\n\"sources\":[W+\"أطلس\"],\n\"ref_check\":[{\"ref\":\"SAP:964\",\"status\":\"not_checked\",\"note\":\"Sayyah not accessible.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"leaf 76 s.v. atlas (silk-satin)\",\"stance\":\"supports\",\"note\":\"'Arab. atlas, lit. wiped smooth, fr. talasa, he wiped, smoothed away'.\"},\n {\"src\":\"LKT\",\"where\":\"no.131\",\"stance\":\"supports\",\"note\":\"'Ar. aṭlas: Glatt, fein ... von Seide, sie sei aṭlas'.\"}]},\n{\"id\":2,\"parent\":1,\"lang\":\"Persian\",\"words\":\"atlas\",\"verdict\":\"confirmed\",\n\"derivation\":\"Persian atlas (اطلس) 'satin, plain silk cloth' is a direct loan of Arabic aṭlas (Mo'in tags it [معر.] and glosses 'پرنیان، دیبا، پارچهٔ ابریشمی ساده، بی‌پرز'); Persian ṭ is merely orthographic (pronounced t). From Persian/Arabic the word spread to Ottoman Turkish atlas, Hindustani atlas and Russian atlas.\",\n\"derivation_fa\":\"«اطلس» فارسی به معنای «پارچهٔ ابریشمی صاف، دیبا» وام‌واژهٔ مستقیم از عربی «أطلس» است؛ معین آن را معرّب و «پرنیان، دیبا، پارچهٔ ابریشمی ساده، بی‌پرز» معنا کرده است. «ط» در فارسی تنها نشانهٔ املای عربی است. از فارسی و عربی به ترکی، اردو و روسی نیز رفته است. ادعای نورایی درست است.\",\n\"sources\":[W+\"أطلس\"],\n\"ref_check\":[{\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"Mo'in abridgement (MON_part1.txt line 14117): 'اطلس: [معر.] پرنیان، دیبا، پارچهٔ ابریشمی ساده، بی‌پرز' (followed by the anatomical, cartographic and astronomical senses).\"}],\n\"consulted\":[{\"src\":\"LKT\",\"where\":\"no.131\",\"stance\":\"supports\",\"note\":\"Arabic aṭlas → Turkish atlas → Rum., Russ., Bulg., Germ. Atlas 'Satin'.\"},\n {\"src\":\"HJB\",\"where\":\"s.v. ATLAS\",\"stance\":\"supports\",\"note\":\"'from the Ar. aṭlas ... 1678 Fryer: Damask'd Gold Atlas Coats' — the word in Persianate India.\"},\n {\"src\":\"HRN\",\"where\":\"grep 'atlas'\",\"stance\":\"silent\",\"note\":\"Horn treats only native Persian words; no entry.\"}]},\n{\"id\":3,\"parent\":1,\"lang\":\"English\",\"words\":\"atlas 2\",\"verdict\":\"confirmed\",\n\"derivation\":\"English atlas 'a silk-satin fabric of the East' (17th c., Fryer 1678, Hedges 1683) was taken by East India Company traders from Persian/Hindustani atlas < Arabic aṭlas; it is a homonym of Atlas the Titan and atlas 'book of maps' (Greek), hence Nourai's index 2. Now obsolete in English but still German Atlas 'satin'.\",\n\"derivation_fa\":\"انگلیسی atlas به معنای «پارچهٔ ساتن ابریشمی شرقی» در سدهٔ هفدهم از راه بازرگانان کمپانی هند شرقی از فارسی/هندوستانی atlas و آن از عربی «أطلس» وام گرفته شد؛ با Atlas تیتان یونانی و atlas «کتاب نقشه» هم‌آوای بی‌ارتباط است. امروز در انگلیسی کهنه شده ولی در آلمانی Atlas «ساتن» زنده است. ادعای نورایی درست است.\",\n\"sources\":[W+\"أطلس\"],\n\"ref_check\":[{\"ref\":\"KLN:122\",\"status\":\"supports\",\"note\":\"Klein 'atlas, n., silk-satin. — Arab. atlas, lit. wiped smooth, fr. talasa, he wiped, smoothed away'.\"}],\n\"consulted\":[{\"src\":\"WEB\",\"where\":\"WEB_vol1.txt line ~12899 s.v. atlas\",\"stance\":\"supports\",\"note\":\"'atlas, n. [Ar., smooth, bare, satin.] a fine fabric of silk and satin, manufactured in the East Indies.'\"},\n {\"src\":\"HJB\",\"where\":\"s.v. ATLAS\",\"stance\":\"supports\",\"note\":\"'An obsolete word for satin, from the Ar. aṭlas ... literally bare or bald'; citations 1678 Fryer, 1683 Hedges, 1689 Ovington.\"},\n {\"src\":\"SKT\",\"where\":\"grep 'atlas'\",\"stance\":\"silent\",\"note\":\"Skeat has only Atlas (Gk.) 'book of maps'.\"}]}]})\nout={\"pdf_page\":510,\"book_page\":480,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-14\",\"entries\":E}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-510.json','w'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-510.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-510.json >/dev/null && python3 tools/verify_check.py 510"
}
```


### [2026-10-15T02:50:20.403Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'confirmed': 8, 'plausible': 2}
root verdicts: {'confirmed': 2, 'plausible': 2}
ref checks: {'not_checked': 5, 'supports': 9, 'partial': 1}
books consulted: {'supports': 12, 'silent': 10, 'partial': 4} | by book: {'PHD': 4, 'HRN': 3, 'HUB': 3, 'WLD': 2, 'IEC': 2, 'LKT': 2, 'HJB': 2, 'SOD': 1, 'MON': 1, 'LAT': 1, 'NYB': 1, 'ARY': 1, 'KLN': 1, 'WEB': 1, 'SKT': 1}
```


## [2026-10-15T02:50:30.777Z] TOOL CALL #57: SubagentHandback

```json
{
 "message": "I verified page 510 (book page 480) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-510.json. `verify_check.py 510` shows 0 PROBLEM lines.\n\n- **Counts:** 4 roots (2 confirmed, 2 plausible) and 10 nodes (8 confirmed, 2 plausible). No node is disputed or transcription_suspect. The 3 redirect entries (Titil, To, Tôgei) were skipped.\n- **Tien (Chinese 店):** confirmed. The route is Middle Chinese 店 temH → Sogdian tym (tēm, \"inn\"; Gharib p. 394, entry 9747) → Persian tīm \"caravanserai\" → timče. Borhan p. 547 and Mo'in support it. ETM could not be checked (no copy is available).\n- **Titi, Titil (root, plausible):** Pokorny 1086 calls it \"kaum ursprachlich\", meaning bird-call imitation and not a real PIE root.\n  - Sanskrit ṭiṭṭibha is plausible: Wiktionary says it comes from a substrate language.\n  - Persian tītū is confirmed. Borhan p. 1364 (Mo'in's footnote) traces it from Sanskrit tittibha through Burzoy's Pahlavi Kalila wa Dimna.\n  - Latin titiô is plausible, but Nourai's gloss \"sparrow\" is wrong. Pokorny and Ernout-Meillet give titiō, -āre as a verb, \"to twitter (of the sparrow)\".\n- **Tkaeša (root, plausible):** the gloss \"agreement, commitment\" comes from Horn 880 and Mo'in (\"اعتراف، عهد\"). Bartholomae's col. 812 has \"doctrine; teacher\". The Avestan → Pahlavi kēš → Persian kīš chain itself is standard (Horn, Nyberg, MacKenzie, Borhan p. 1755).\n- **T.L.S (Arabic ṭ-l-s):** confirmed throughout (Klein, Lokotsch no. 131, Hobson-Jobson, Webster). SAP could not be checked (no copy is available).\n- **Extraction errors:** none. The JSON matches the printed page. The Sogdian box prints only the gloss \"bazaar, inn\" with no Sogdian word, and the extraction copied that faithfully into `translit`.\n- **Tool issue:** `ref_page.py BQT:1364`'s default offset lands on pdf page 159, but the correct pdf page is 157. That run had cached the wrong page as `BQT/1364.png` and `1364.txt`, so I deleted the cache and re-rendered from pdf page 157. I also saved what I read from the page image to `data/verification/sources/refs/ocr/BQT/1364.vision.txt`.\n- **Web sources:** the 8 Wiktionary pages cited in the file are archived with `fetch_source.py`."
}
```


### [2026-10-15T02:50:31.109Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
